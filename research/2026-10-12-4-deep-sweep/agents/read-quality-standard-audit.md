# read:quality-standard-audit

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "quality-standard-audit: the course-plan quality standard (Golden Checklist v2 / Hub v1, red-team base protocol, G3 profile), how it was audited (red-team rounds, gauntlets, clean-room replays, course-level evaluator layer) and what failed (reviewer rounds 1–5, G3/G4/G5/MAP-proxy findings)",
 "coverage": {
  "read": [
   "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/{README.md,CATALOG.md,AGENTS.md,CLAUDE.md}",
   "…/ti-courseplans-quality-standard-audit-handoff-20260806/docs/{instruction-quality-standard.md,practice-layer-spec.md,instruction-modes-spec.md,generator-insights.md,course-creation-spovs.md,course-formula-agents.md,academics-alignment-plan.md,grade-band-profiles.md,teaching-reading-comprehension-brainlift.md,train-teacher-requirements.md,plain-english-explainer.md,PIPELINE-QUICKSTART.md (parts)}",
   "…/docs/handoffs-2026-07-13/ (README, pedagogy-llm-eval-contract.md, course-eval-layer/README.md, evaluator-spec.md, course-evidence-workbench.html via textutil, labeled-defect-corpus.jsonl first 5 records only)",
   "…/docs/redteam-sources/ (README, g4 round 1, g5 round 1)",
   "…/docs/standards/ (course-quality.qmd, source-course-refinement.qmd, templates/compliance.qmd, course-json/README.md grep)",
   "…/docs/standards/student-course-quality/ (README, AUTHORITY, PROJECTION, evaluator-contracts/*, crosswalk/CONFLICT-LEDGER.qmd, profiles READMEs, versions/2.0.0 STANDARD/GOLDEN-CHECKLIST/PROFILE-PARITY, versions/1.0.0/STANDARD.qmd, profiles/base/RED_TEAM_BASE.source.json principles/probes/contracts, provider-qualification JSON; CSV crosswalks header rows only)",
   "…/docs/reading-science/ (README, PRIORITIES, SYNTHESIS §5–10, DIGEST-singh-eduqwen-2026, EXTRACTION_EVIDENCE, sources.qmd)",
   "…/skills/course-red-team/ (SKILL.md, references/finding-taxonomy.md, report-template.md, opportunities-to-respond-brainlift.md)",
   "…/skills/g3-reading-red-team/ (SKILL.md, references/g3-reading-standard.md §1–2 and §7, IES-CORPUS-REVIEW-2026-08-05.md, dimensions D1, D2, D5, D6, D7, D8, D10, D11)",
   "…/skills/{course-content-integrity,train-teacher (SKILL, gauntlet-spec, teacher-contract, text-quality-lane, curriculum-architecture),train-assessor,edullm-quality-standard,knowledge-ingest,timeback-course-eval (eval-criteria, worked example),video-red-team (finding-taxonomy, rubric)}",
   "…/.beads (interactions.jsonl is empty)",
   "~/Projects/ti-courseplans, ~/Projects/ti-courseplans-agent-entrypoint-20260806, ~/Projects/ti-courseplans-full-audit-tool-20260806 (offload stubs) and their iCloud chain; the two Aug-27 worktree archives compared by file listing (extra files: audit_course.py header, test_agent_entrypoint.py size, test-results/.last-run.json)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans: skills/course-red-team/SKILL.md (diff vs audit copy), skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md, docs/standards/student-course-quality/{AUTHORITY,README,STANDARD,CONFLICT-LEDGER diffs; evidence/AGENT-ENTRYPOINT-CLEAN-ROOM…, AGENT-LIBRARY-USABILITY-CLEAN-ROOM…; sources/knowledge-bot/kb-0081, kb-0093, kb-0164, kb-0169, kb-0172}",
   "…(iCloud) courses/g3-reading/{FEEDBACK-LEDGER.md (parts I.A, III–V), iteration-3/CONTENT-FAILURE-CLASSES.md, iteration-3/BUILD-RULES.md (rules, register, 06.08 rules, coupling trap), iteration-3/FEEDBACK-AUDIT-2026-07-29.md (head), iteration-4/REDTEAM-R2-2026-08-06.md (§0–3), iteration-4/REDTEAM-U1L1-2026-08-05.md (head), iteration-1/teacher-skill/gauntlet/{CONVERGENCE-REPORT.md,layer5/RESULT.md}, iteration-1/timeback-pull/COURSE_BUNDLE_BRAINLIFT.md (grep)}",
   "…(iCloud) courses/g5-reading/approval-package/D9-GATE-WALKTHROUGH.md; courses/map-proxy-assessment/{validity/00_AUDITS_AND_FIXES.md, red-team/RED_TEAM_FINDINGS.md head}; courses/g5-reading-v2/audit/full-course-review-red-team-interim-2026-07-20.md (head); courses/g4-reading/approval-package/CRITIQUE-AND-VERIFICATION.md (headings)",
   "…(iCloud) feedback/feedback1/Reading_Explorers_v2_Feedback (1).docx and feedback/feedback5/Feedback 11.08.docx (textutil text)"
  ],
  "skipped": [
   "iCloud brainlift/ academics dump and the large research PDFs/decks in feedback/feedback2 (consume-only sources; their claims are already digested and quote-verified in docs/reading-science)",
   "feedback/feedback1–4 academics BrainLift .md files, App Review V3 pdf, science misconception guidance .docx and the science workbook .xlsx (academics-owned domain guidance and data; summarized by the standard, ledger and taxonomy I did read)",
   "courses/*/ lesson JSON, audio/TTS clips, build trees, AUTHORING-NOTES, unit specs, per-grade BrainLifts and plan packages (course-specific content, data, likely other directions)",
   "g5-reading AUDITS_AND_FIXES and RED_TEAM_ROUND2–4, map-proxy validity design/simulation docs, g4 approval-package plan docs (time; their findings appear with numbers in finding-taxonomy and course-formula-agents)",
   "iteration-4 feedback-0806-pedagogy/verification, SKILLS-G3-READING, agent/constitution, pedagogy-digest, iteration-3 UX-PRACTICES, BORROWED-INSTRUCTION-PATTERNS, iteration-2 red-team rounds (time; partly duplicated in the addendum and ledger)",
   "registry.sql, bundle.json, internal/red-team/READING_G3.json, COVERAGE-LEDGER.csv and other crosswalk CSVs beyond headers, labeled-defect-corpus.jsonl beyond five records (generated data / data dumps)",
   "predictor/, service/, scripts/ and *.py/*.mjs code (code, not findings), timeback-*-alpha platform skills (API mechanics), daily-update-message skill, chief-of-staff.md, agent-service-plan.md (team process / infrastructure)",
   "docs/handoffs-2026-07-13/[name]-unit-sizing.* (person's name in path; item budgets)"
  ],
  "notes": "The three other ~/Projects/ti-courseplans* folders are offload stubs; their content lives in iCloud archives whose path contains a person's name ('[name]’s Mac mini'), so every candidate relying on an iCloud file is flagged name_bearing_source=true and local copies in the audit-handoff folder were preferred wherever the same evidence existed. Quotes that span wrapped lines are given joined with single spaces (all verified by grep against whitespace-joined text); for .docx files the line numbers are lines of `textutil -convert txt -stdout` output. Process slip: early in the run one command wrote a file listing to /tmp/x_a.txt (no secrets); per the read-only rule it was left in place, and nothing else was written. Discrepancy found: the showcase-modelling count is '1 of 18' in course-red-team/SKILL.md but '3 of 18' in finding-taxonomy.md. Strongest counter-evidence to the existing list: the adopted DI error-correction protocol and a live gate show the correct answer after a first miss (vs truths 1 and 4); a reviewer floated three consecutive errors as the hint trigger (vs 4); the blind expert panel used an adversarial 'try to refute' framing (vs 32); reviewers asked for exactly four options while the universal standard forbids filler options."
 },
 "candidates": [
  {
   "statement": "Run the hidden-text check a second time giving the solver everything earlier lessons taught, because well-sequenced earlier lessons can let a later question be answered without its own text.",
   "kind": "measured",
   "found_by": "A replay that gave the solver the prior-lesson corpus but not the new text caught 1 of 16 later items that the ordinary hidden-text check had passed (0/3 without context, 3/3 with prior lessons).",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "135-137",
     "quote": "the historical Gemini 2.5 run found **1 catch of 16**. `rivers-demo-choice-hottext-20` was **0/3 exact plain-blind but 3/3 exact + high confidence spine-conditioned.**"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "106-108",
     "quote": "the solver receives all prior lesson content (on-ramp pre-teach, ledger state, prior passages) but not the new text; later items must fail."
    }
   ],
   "against": "evaluator-spec.md 138-139: \"A calibrated 2026-07-13 Gemini 3.5 Flash replication was 3/3 in both conditions, so the same item is currently a direct plain-blind leak and the historical context-lift interpretation does not generalize across model versions.\" practice-layer-spec.md 106: \"(measured on one theme, not universal)\"",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-run hidden-text checks with a current, capable solver before relying on an old pass, because a newer solver can answer without the text an item an older one could not.",
   "kind": "measured",
   "found_by": "A current-model re-check, after a with-text calibration, solved the item 3/3 without its text and reversed the historical 0/3 verdict.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/README.md",
     "lines": "90",
     "quote": "The required current-model check changed the verdict."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/README.md",
     "lines": "92",
     "quote": "The old context-lift claim does not survive model drift; the item is directly gameable."
    }
   ],
   "against": "README.md 93: \"This supports its existing removal from serving. It does not certify the rest of the course.\" (one item only)",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before trusting that a solver cannot answer an item without its text, confirm the same solver answers it correctly with the text, and certify only items that fail hidden and pass shown.",
   "kind": "adopted rule",
   "found_by": "The hardened certification protocol required both conditions after rubric-only and same-family checks let guessable items through.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-assessor/SKILL.md",
     "lines": "29-30",
     "quote": "every item blind-probed (must fail without the passage, succeed with it)"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "233",
     "quote": "the solver family must differ from the generator's, blind-solve must fail AND with-passage must pass, and no certification is carried forward from a cached bundle."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A quality score or rubric judgment says nothing about whether an item can be answered without its text, so keep the hidden-text check as its own gate and never report a quality pass as protection against guessing.",
   "kind": "measured",
   "found_by": "A guessable item scored 1.0 on an item-quality judge; a rubric gate passed all six items a hidden-text probe then solved; a model judge passed items a hidden-text solve cracked 6/6.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "233",
     "quote": "InceptBench scored one gameable item **1.0** — so the gate is dual: an item ships only if a quality score clears **AND** a blind solver cannot answer it without the passage"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "51",
     "quote": "The rubric gate (item ≥0.85 + lesson-level >20% rule) passed all six of these items — so the rubric is demonstrably not a substitute for the empirical run."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D11-anti-gaming-claim-integrity.md",
     "lines": "6",
     "quote": "we've watched an LLM-judge pass items that a blind-solve cracked 6/6."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Generate questions by a construction that forces use of the text rather than by cloning question types, because most raw generated questions can be answered without the text.",
   "kind": "measured",
   "found_by": "Construction-first items survived the hidden-text gate at 60% versus 6% for clones; raw generated banks leaked about 94%; 78% of raw items failed text-dependence alone.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "21-23",
     "quote": "construction-first generation survived the anti-leak gate at 60% vs 6% for encyclopedic clones; one production campaign yielded 48.7% (738 certified of 1,516); raw generated banks leaked ~94% blind."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "59-60",
     "quote": "78% of raw machine-generated items failed the passage-dependence gate alone"
    }
   ],
   "against": "course-formula-agents.md 233: \"G5 proved format is necessary but not sufficient (the anti-leak-*format* pool still leaked ~78%)\"; practice-layer-spec.md 20-21 calls these figures \"pricing and design evidence, not current readiness\".",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a two-part item the second part must not restate the first part's answer, because linked parts that echo each other let the item be solved without the material.",
   "kind": "measured",
   "found_by": "Two-part evidence items were guessable 33% of the time because the second part restated the first; a later six-item sample showed verbatim restatements.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "134-135",
     "quote": "In the recorded G3 case, EBSR was gameable 33% of the time because Part B restated Part A"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "46",
     "quote": "Part B restates Part A — G3's measured root cause, verbatim present"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-content-integrity/SKILL.md",
     "lines": "158-159",
     "quote": "For EBSR, Part B needs one uniquely strongest evidence choice and must not reveal Part A."
    }
   ],
   "against": "course-red-team/SKILL.md 135: \"that is evidence for that profile, not a universal format rule.\"",
   "adds_to_existing": [
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When material teaches real-world knowledge or follows a familiar story pattern, check that its questions can't be answered from general knowledge or genre logic, and ask about what only this material settles, such as a detail, a sequence, a cause or a number.",
   "kind": "measured",
   "found_by": "A cold solver answered all four in-reading stop questions from world knowledge and genre logic; knowledge-rich items were answerable by any knowledgeable solver with no text.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "47",
     "quote": "Prior-knowledge answerability — the knowledge-expedition design makes items about real-world facts (pitch physics, Magellan, explorer funding) answerable by any knowledgeable solver with no passage."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-R2-2026-08-06.md",
     "lines": "151",
     "quote": "\"Anansi is a spider, and spiders are tiny. That alone kills B, C and D.\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-R2-2026-08-06.md",
     "lines": "192",
     "quote": "ask about something only this retelling decides (a detail, a sequence, a causal link, a number)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    6
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Check where the right answer sits within each sequence a learner meets, not only across the whole bank, because a balanced total can hide a visible streak.",
   "kind": "measured",
   "found_by": "Before the fix, 12 of 19 keys sat at option A with a five-in-a-row run, while the item judge checked only course-wide balance.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "151-152",
     "quote": "does not detect within-lesson position *runs* (a student-visible streak that a course-wide histogram averages away)."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "168",
     "quote": "**12 of 19 single-select keys at A, with a 5-run.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the right answer from being the longest or most detailed option by putting the verdict in the option and the reasoning in the feedback, and check length in both words and characters.",
   "kind": "measured",
   "found_by": "In one generated course 79% of keys sat at A and the key was systematically the longest; after fixes one key was still longest by words (12 v 11) though not by characters (61 v 62); shuffling does not remove the cue.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "165-166",
     "quote": "**79% of correct answers sat at position A and the key was systematically the longest**"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "172",
     "quote": "key longest by word count 12 v 11 but not by characters 61 v 62"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "130-131",
     "quote": "**Length parity**: verdict in the option, mechanism in per-option feedback — the key is never systematically longest."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check option sets for cues that need no knowledge — a key that is the only option of its grammatical kind or the only one with a dash or hedge, or distractors with absolute or absurd wording — since shuffling removes none of them.",
   "kind": "measured",
   "found_by": "The only dashed option in one lesson's stops was the key; a grammatical odd-one-out key survived a seeded shuffle; absolute-language distractors let a hidden-text solver eliminate options.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "214-216",
     "quote": "The key is the only option of its grammatical kind — a bare proper noun among three \"The …\" / \"He …\" options. Position shuffling does not remove this; a seeded shuffle already removed position information from these items and the cue survived intact."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "41",
     "quote": "U1-L1's read stops the *only* option carrying a dash was the key"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "48",
     "quote": "Distractor tells — wrong options use absolute/absurd language (\"no real hardships\", \"relocate their entire kingdoms\"); the correct option is consistently the longest and most detailed."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Keep the facts used while modelling or practising a skill apart from the facts the following skill questions test, and label each question as a check of taught knowledge (overlap allowed) or a use of the skill (overlap not allowed).",
   "kind": "measured",
   "found_by": "Teaching steps modelled the exact proposition a later item tested, so the item checked recall of the demonstration; it recurred across units, a fresh unit re-made it, and the knowledge-check versus skill-item distinction took five rounds to isolate.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "88",
     "quote": "a teaching dose models the exact proposition an item tests → the item checks recall of the modeled sentence, not the skill. Reproduced across 2 units."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/teacher-contract.md",
     "lines": "59-61",
     "quote": "Authoring a fresh unit (u03 respiratory) REPRODUCED the dose-item leak the hibernation unit took 5 rounds to eliminate"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "85-86",
     "quote": "Mis-classifying the item makes the same text both correct and defective — it took five adversarial rounds to isolate this."
    }
   ],
   "against": "teacher-contract.md 67-68: \"Knowledge-CFU items are exempt: they legitimately check taught knowledge; classify explicitly.\"",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Probe order-sensitive items under several shuffles and judge by the worst case, because certifying against a single shuffle lets guessable items through.",
   "kind": "measured",
   "found_by": "Items certified against one seeded shuffle were re-probed under several and 72 were decertified, including one exact 1.000.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "20",
     "quote": "sequence items certified against one seeded shuffle; multi-shuffle re-probe decertified 72 incl. one exact 1.000"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-assessor/SKILL.md",
     "lines": "43-44",
     "quote": "(anonymized labels, seeded+multi shuffles, three blind votes incl. temp variation, leak = exact or partial ≥0.6, cross-family solver, no self-certification)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    35
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Work out each item's guessing floor from how it is actually scored where it is served, not from its format label, and never set a pass bar close to that floor.",
   "kind": "measured",
   "found_by": "A live probe found binary scoring with no partial credit and a select-several item scored on its first choice, so its floor was k/n rather than the 1/C(n,k) its label implied.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "115",
     "quote": "Chance floors are stated **per item from its responseDeclaration under the actual serving scoring rule**"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "117-118",
     "quote": "a select-k interaction authored `cardinality=\"single\"` scores \"first token in correct set\" (floor k/n, not 1/C(n,k)), so the format label alone never determines the floor."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "119-120",
     "quote": "A bar within noise of its floor measures nothing."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Work out what a percentage pass mark demands on each test's actual length, because on short tests 90% can mean a perfect score.",
   "kind": "measured",
   "found_by": "Purging guessable items shrank tests to 5–9 items and turned a 90% gate into a perfect-score-only gate.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "14",
     "quote": "leak-purge shrank tests to 5–9 items → 90% gate = perfect-score-only (ceil(0.9n)=n for n≤9)"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "63-64",
     "quote": "**Arithmetic traps hide in small n.** ceil(0.9×n) = n for n ≤ 9: a 90% gate on a ≤9-item test demands a perfect score."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Declare each assessed resource's purpose — in-lesson check, interval assessment or benchmark — before judging it, and put pass thresholds only on assessments, since judging one by the other's rules misfires.",
   "kind": "measured",
   "found_by": "Every lesson resource carried a 90% threshold, so teaching lessons behaved as practice-test gates; an evaluator that kept one course-level type penalised deliberate feedback suppression on the assessment.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "230-231",
     "quote": "masteryThreshold=90 on all 5 lesson resources** -- the three teaching lessons and the transfer lesson behaved as 90% practice-test gates over their own formative checks."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "90-92",
     "quote": "judging one by the other's bar."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/timeback-course-eval/references/eval-criteria.md",
     "lines": "102",
     "quote": "The single most important criterion."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Include tasks that require combining taught skills and verify that each one really demands the combination, because passing every part separately does not show the whole and calling a task integrative does not make it so.",
   "kind": "measured",
   "found_by": "Ten tasks declared integrative were all refused by the full gate (8 hidden-text leaks, 2 prior-lesson leaks, 0 integrative verified); an evaluator counted a multi-skill bank as integrative.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "246-247",
     "quote": "A gate of individually-good atomized checks licenses \"passed the parts,\" never \"acquired the theme.\""
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "274-276",
     "quote": "the full gate certified **0/10** (8 plain-blind leaks, 2 spine-conditioned leaks; 0 integrative verified), so nothing was published."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Call a check delayed only when the delay is enforced and the elapsed time is recorded, because same-day success shows short-term memory rather than learning.",
   "kind": "measured",
   "found_by": "A 90% gate was verified live, but the platform did not enforce the intended 24-hour delay and no elapsed time was captured.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/README.md",
     "lines": "116-117",
     "quote": "The platform does not enforce the intended 24-hour delay, and no elapsed-time evidence was captured, so this is not a verified delayed assessment."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "38-40",
     "quote": "release-day completion never qualifies (Practice BrainLift: same-day testing measures working memory, not learning)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make every wrong option an error a learner would really make, and don't pad an item with filler options to reach a fixed count.",
   "kind": "adopted rule",
   "found_by": "Reviewers and the assessment guidance found weak fourth options added to meet a count; a filler option is judged worse than fewer options.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "160",
     "quote": "can you name what a student choosing each distractor is thinking? if not, it's filler (worse than 3 options)"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "773",
     "quote": "J16-ASS-001: Use only plausible, diagnostically useful response options; do not add filler to meet a count."
    }
   ],
   "against": "D5-assessment-item-construction.md 12: \"Every MCQ has ≥4 options; no 2-option / True-False item in the mastery pool (a yes/no is a 50/50 guess)\" — the scoped profile fixes a minimum count.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give every plausible wrong option feedback that addresses the error it represents and is true for every response routed to it, because a strong lure left uncorrected can teach the error.",
   "kind": "measured",
   "found_by": "Corrective feedback did not match the misconception of the chosen option; branch feedback made claims false for some responses in its branch; the guidance warns uncorrected lures teach the error.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/labeled-defect-corpus.jsonl",
     "lines": "5",
     "quote": "Corrective feedback did not match the construct the distractor represents (feedback not misconception-keyed to the chosen option)."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "166",
     "quote": "strong misconception distractors + no feedback = teaching the error (negative suggestion effect)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "26-28",
     "quote": "must be true for EVERY index classified into that branch"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": true
  },
  {
   "statement": "A question claimed to need application or analysis must present material the learner has not seen, otherwise it is recall with a longer stem.",
   "kind": "adopted rule",
   "found_by": "Items labelled inference were found to be recall of taught content.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "163",
     "quote": "genuine higher-order needs a NOVEL stimulus (unseen passage/scenario); else retag recall"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Screen content questions for untaught vocabulary, hard syntax and idioms that make them test reading ability rather than the content.",
   "kind": "adopted rule",
   "found_by": "Curriculum-architecture guidance and the evaluator gap analysis named construct-irrelevant language difficulty in learner-facing items.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md",
     "lines": "33",
     "quote": "Autonomous items are screened for untaught Tier-2 vocab, grade-inappropriate syntax, and idioms that make them test reading, not content"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/curriculum-architecture.md",
     "lines": "99-100",
     "quote": "**linguistic-validity QC** (untaught Tier-2 vocab, syntax, idioms — required for teacherless delivery)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make each diagnostic item test one thing so a wrong answer can be interpreted, and don't make later parts of an item depend on earlier parts.",
   "kind": "adopted rule",
   "found_by": "Bundled items mixing reading, content and reasoning gave uninterpretable wrong answers.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "165",
     "quote": "passage-parse + content + reasoning in one item → wrong answer uninterpretable"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "31",
     "quote": "No all-or-nothing multi-part item where (b) depends on (a); split into independent items"
    }
   ],
   "against": "finding-taxonomy.md 165 allows an exception: \"(reading exception: OK when the stimulus IS the KC, then strip everything else)\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Base a mastery decision on several different items and item families, because passing by retrying near-identical items or on a handful of items is practice, not mastery.",
   "kind": "adopted rule",
   "found_by": "Grind-through gates were passed by retrying near-identical items.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "168",
     "quote": "mastery evidence must span item families; a gate decision on <10 items is retrieval practice, not mastery"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "42",
     "quote": "No mastery decision rests on a single MCQ (≥25% guess); use item bundles"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    15,
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "State the supports a result was earned with, because doing something with cues is not doing it unaided.",
   "kind": "adopted rule",
   "found_by": "Highlighting, word banks and pre-located evidence were present but not reflected in mastery claims.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "169",
     "quote": "\"can do X with cues\" ≠ \"unaided\""
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "46",
     "quote": "The mastery claim states its support level (\"unaided\" vs \"with cues\"); high-stakes scores only the unaided check"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Watch items after use — revise options almost nobody chooses, flag items that discriminate the wrong way, and replace predicted difficulty with live data.",
   "kind": "adopted rule",
   "found_by": "Reviewer obligations required predicted difficulty to be treated as a prior and live item functioning to be monitored.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
     "lines": "47",
     "quote": "Distractor-level data reviewed; non-functioning distractors (<5%) revised; negative-discrimination items flagged"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "455",
     "quote": "J16-ASS-008: Treat predicted difficulty as a prior awaiting live calibration."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "If the goal is for learners to produce something — explain, write or say it — assess it with a production task, because selecting an answer can't show it.",
   "kind": "adopted rule",
   "found_by": "The first build had no writing or explanation at all; every response was a click.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "132",
     "quote": "Production targets get production formats."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/opportunities-to-respond-brainlift.md",
     "lines": "30",
     "quote": "If a child never has to compose or explain an answer, the app cannot tell whether the child understood"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Score every model answer against its own marking rule, because a rule that would mark down its own exemplar is broken.",
   "kind": "measured",
   "found_by": "A written-response rule required one exact term while its own model answer used a synonym; checks that only counted strings never opened them.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "132-134",
     "quote": "U2-L6's SCR required the term \"sacrifice\"; its own model answer said \"gave up\". The exemplar the teacher reads aloud would have been marked down by the rule printed underneath it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    10,
    56
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Check that what one lesson marks correct agrees with what earlier lessons taught, because checks that read one lesson at a time can't see a learner marked wrong for learning an earlier lesson correctly.",
   "kind": "measured",
   "found_by": "A warm-up rewarded an answer that contradicted how the previous lesson filled the same row; five other gates missed it.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "142",
     "quote": "A child who learned L5 **correctly** was marked wrong."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "144-145",
     "quote": "Invisible to five other gates because **every other gate reads one lesson at a time.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Check that every item assesses the skill its lesson claims to teach, because retagging does not fix an item that demands a different operation.",
   "kind": "measured",
   "found_by": "After 193 items were retagged, a lesson on one skill still served an item testing another.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "79-80",
     "quote": "A lesson's items must assess the KC the lesson claims to teach (construct coherence — a main-idea lesson serving inference items is a tagging *and* teaching defect)."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "84",
     "quote": "main-idea lesson served an inference item after a \"successful\" retag"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Audit standard tags against what each item actually demands and report the error rate, because tag coverage is not a curriculum and can hide whole missing strands.",
   "kind": "measured",
   "found_by": "Systematic mistags required 193 items to be retagged; tags existed only at lesson level so whole strands could be absent without any check failing.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "224",
     "quote": "G3 had systematic mistags (vocab-in-context wrongly on L.3.4; comprehension on the wrong strand); **193 items retagged** — audit tags and report an error rate"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "57-58",
     "quote": "Reading standards are skills, not knowledge — CASE-tag coverage is plumbing, never the curriculum claim."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Use diagnostics to route support under stated uncertainty, never as a grade or mastery label.",
   "kind": "adopted rule",
   "found_by": "Reviewer obligations required declaring an assessment's product type before interpreting it and handling slips, guesses and unassessed knowledge.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "99",
     "quote": "Product type, sampling limits, uncertainty, slips, guesses, unassessed knowledge, and routing behavior are explicit and tested."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "785",
     "quote": "Failure signals: Diagnostic score directly promotes, punishes, or labels mastery; uncertainty hidden."
    }
   ],
   "against": "D7-knowledge-first-curriculum.md 35 doubts any valid knowledge-gap diagnostic exists: \"a valid one does not exist — \\\"nailing jelly to the wall\\\"\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When validating an assessment against an external test, make sure it doesn't act as practice for that test, for example by counterbalancing the order.",
   "kind": "open question",
   "found_by": "A red-team review found the validation study would give the external test's format as a rehearsal days before it, with no order-effect design.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md",
     "lines": "21",
     "quote": "**Counterbalancing / order-effect design is not addressed anywhere in the CVP.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Show every metric at its measured value in every summary, including the failing one, because rounding up to meet a bar or leaving out the failing metric is a false pass.",
   "kind": "measured",
   "found_by": "An audit found 0.928 reported as '0.930 ✅' against a ≥0.93 bar and the one failing metric omitted from every summary table.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "9",
     "quote": "Summary tables reported reliability as \"0.930 ✅\" against a ≥0.93 benchmark the underlying reports state as 0.928, below"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "10",
     "quote": "The one failing metric (RMSE 4.12 vs <4.0 target) was omitted from every summary table"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Don't reuse pass bars, yields or thresholds measured on one course or level for another; recalibrate them on a control set first.",
   "kind": "adopted rule",
   "found_by": "Every threshold planned for a new course had been measured on a different grade's course.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "139-141",
     "quote": "All historical G5-derived bars and yields require a **G3 recalibration control set before any G3 gate or generation budget goes live** (blocking precondition)"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md",
     "lines": "33",
     "quote": "Every G5-derived threshold/yield is recalibrated on a G3 control set before any G3 gate goes live"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make the model, guided and independent stages one and the same process at decreasing support, so that with the labels removed it still reads as one process fading.",
   "kind": "measured",
   "found_by": "Reviewers found the routine misapplied in successive rounds: the model only revealed answers, the guided step only hinted, and the independent step switched skill.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-creation-spovs.md",
     "lines": "107-109",
     "quote": "round 2 found our gradual release **misapplied**: the I-do revealed answers instead of modelling the thought process, the we-do gave hints instead of walking the same steps with immediate corrective feedback, and the you-do switched skills."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "24-25",
     "quote": "strip the labels; a reviewer must still be able to say \"these three artifacts teach the same process at decreasing support.\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "348",
     "quote": "Violated in rounds 1, 2, V3, and still being refined at 08-06"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": true
  },
  {
   "statement": "A worked example must show the reasoning on the material as it is spoken — where to look, the tempting wrong choice and why it is rejected — rather than just the finished answer.",
   "kind": "measured",
   "found_by": "Modelling steps showed only the filled-in answer; the standard now requires a plausible alternative, its rejection and the construction, synchronised with the narration.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "16-17",
     "quote": "Revealing the answer is not modelling."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "52",
     "quote": "Visible evidence, a plausible alternative, the reason it is rejected, and construction of the answer are synchronized and semantically sound."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "164-165",
     "quote": "the screen says \"watch\" but only shows the organizer filled with the finished right answer."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40,
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In guided practice hand the learner a partly finished answer to complete with feedback at each step, and in independent practice apply the same steps to new material with no more support than the guided step had.",
   "kind": "measured",
   "found_by": "A guided step was secretly independent ('I filled this row, now you answer'); a clean-room review found independent practice reusing the model's own example; an independent step was given more scaffolding than the guided one.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "169-171",
     "quote": "\"I filled this row, now you answer\" with NO partial/seeded answer = the middle rung is missing"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd",
     "lines": "57-58",
     "quote": "You-do returns to the model's animal, evidence, and constructed answer instead of requiring the same operation on new evidence."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "332",
     "quote": "a you-do step may never be more scaffolded than the corresponding we-do step."
    }
   ],
   "against": "feedback-2026-08-06-addendum.md 340-344 records that this rule was argued and overruled for one lesson, which shipped a default gap-fill at the independent step.",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Keep feedback short — about 40 words at most and never longer than the task — and lint its mechanics, because generated feedback ran to a median of about 91 words.",
   "kind": "measured",
   "found_by": "Reviewers found feedback longer than the passage and miscapitalised; the generator's median was measured at about 91 words.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "31-33",
     "quote": "Target ≤ 40 words; hard cap 60. A grade-3 child will not read feedback longer than the passage (round-2 verified: our generator's median was ~91 words)."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "75",
     "quote": "G3 round-2: feedback longer than the passage, lowercase after full stops; G5 generator lineage measured at ~91-word median"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1,
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After a miss, reteach and retry at the same difficulty instead of escalating it, because escalating difficulty after a failure lowered second-attempt accuracy from 64% to 41%.",
   "kind": "measured",
   "found_by": "Data from the incumbent course showed difficulty escalating after a miss and second-attempt accuracy dropping from 64% to 41%.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-1/timeback-pull/COURSE_BUNDLE_BRAINLIFT.md",
     "lines": "44",
     "quote": "Difficulty escalates after a miss; attempt-2 supporting-detail accuracy **drops from 64% to 41%**"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
     "lines": "46",
     "quote": "retry that drops accuracy 64%→41%"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": true
  },
  {
   "statement": "After a failed checkpoint, reteach and retest once on new items after a delay, and send a second failure to a review of placement or sequence rather than an endless loop.",
   "kind": "adopted rule",
   "found_by": "Practice guidance rejected immediate-retry lockout loops in favour of bounded reteach and delayed retest.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "72-74",
     "quote": "D15 failure routing: reteach via M7 → one delayed retest on new items → a second failure routes to placement/sequence review. No infinite retest loop"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "36",
     "quote": "A second consecutive failed delayed retest routes to placement/sequence review — never an infinite loop."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "If the correction a learner needs is longer or more complex than the original teaching, treat it as new teaching rather than practice feedback.",
   "kind": "adopted rule",
   "found_by": "The practice boundary rule, applied after feedback grew longer than the instruction it followed.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md",
     "lines": "23",
     "quote": "If the corrective feedback needed exceeds the original instruction in length/complexity, it's new instruction, not practice"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "For an idea learners commonly get wrong, draw out their intuitive wrong belief once at the start and then resolve it, without repeating the wrong belief later.",
   "kind": "adopted rule",
   "found_by": "Guidance from the curriculum side, citing research where clear-only explanation barely moved scores and the misconception-first version nearly doubled the gain.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/SKILL.md",
     "lines": "72",
     "quote": "A clear explanation that never engages the prior belief produces confident non-learning (Muller: clear-only exposition barely moved scores; misconception-first nearly doubled the gain)."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "199-202",
     "quote": "The wrong belief is voiced at most once, at the open, and never rehearsed/scolded in the body"
    }
   ],
   "against": "none found (the underlying study is cited without a DOI or URL)",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Test an opening hook by deleting it: if the rest still teaches an unrelated objective unchanged, the hook is misaligned with the core point.",
   "kind": "adopted rule",
   "found_by": "Hooks that were accurate but detached from the lesson's core question.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/rubric.md",
     "lines": "74-75",
     "quote": "If deleting the hook leaves the body teaching an unrelated objective unchanged, the hook is misaligned."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A reply that could have been written before the learner answered is not a response to them, so branch on what the learner actually produced and test that every branch, including 'I don't know', can fire.",
   "kind": "measured",
   "found_by": "All 18 checks branched on a tap index rather than the spoken answer; the silent branch was authored in 18/18 but could never fire.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "185",
     "quote": "the spoken answer never drives the branch"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "187",
     "quote": "branch authored + gated in 18/18 but **can never fire**"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/opportunities-to-respond-brainlift.md",
     "lines": "71",
     "quote": "A reply that would read the same no matter what the child answered is not a third turn."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    55
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a specific point must be learned exactly, prompt the learner to say it again in their own words rather than restating it for them, because learners often don't notice a restatement.",
   "kind": "external research",
   "found_by": "Lyster & Saito (2010) meta-analysis, https://doi.org/10.1017/S0272263109990520, as summarised in the review guidance used to set follow-up criteria.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/opportunities-to-respond-brainlift.md",
     "lines": "71",
     "quote": "A recast keeps a conversation moving and grows how much a child says, but because children often do not notice a recast, it does not reliably teach one specific point (Lyster & Saito, 2010)."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/opportunities-to-respond-brainlift.md",
     "lines": "198",
     "quote": "https://doi.org/10.1017/S0272263109990520"
    }
   ],
   "against": "opportunities-to-respond-brainlift.md 168: \"Drawn from second-language classrooms, so applied here by analogy to early oral language.\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When counting learner responses by type, check what each one is, because echo or say-back answers inflate production counts and a count that meets its target can still mislead about quality.",
   "kind": "measured",
   "found_by": "A self-audit reported 7–8 production responses per lesson; 2–3 were trivial say-backs, real production was about 2, and 5 of 7 spoken moments got canned replies.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "183",
     "quote": "G3 iter-3 claimed \"7–8 generate/lesson, over-delivered\" — but 2–3 were trivial *say-backs* (repeat a word) and the real generative-comprehension production was ~2"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "83-85",
     "quote": "Iter-3's \"7–8 generate, over-delivered\" was true by count and misleading by quality (2–3 trivial say-backs; 5 of 7 spoken moments canned). Verify the number AND what it measures."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/opportunities-to-respond-brainlift.md",
     "lines": "23",
     "quote": "A high number of responses per minute is not evidence of quality if the app reached that number by asking only recognition questions."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Don't let more than about a minute of passive content pass without a meaningful response from the learner, and don't count a decorative tap as one.",
   "kind": "adopted rule",
   "found_by": "Passive screens invited click-through; a later meeting ruled that every screen needs a substantive action.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "49",
     "quote": "a consequential check at least every 60s of passive content (Generic Instruction SS6)"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D10-delivery-ux-accessibility.md",
     "lines": "23",
     "quote": "No continuous passive segment beyond ~60s; a consequential check appears at least every 60s"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "27",
     "quote": "passive listening or text-only screens invite click-through rather than attention. The interaction must be substantive to the teaching move; a decorative tap control does not satisfy the concern."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Reveal steps when the learner acts rather than on a timer, because a timer can't pace itself to a slow reader and turns the step into passive watching.",
   "kind": "adopted rule",
   "found_by": "Timed reveals collided with the active-screen rule; a reviewer asked for a per-step 'next' because modelling moved too fast for some learners.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "308-311",
     "quote": "A timer also cannot pace itself to a slow reader. Tap-to-continue satisfies both."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback5/Feedback 11.08.docx",
     "lines": "11 (textutil text)",
     "quote": "Otherwise, it will move too fast for some students."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Open each section with a link to what was just taught, because a section that is good on its own but disconnected in context passes every per-section check.",
   "kind": "adopted rule",
   "found_by": "One video closed on one idea and the next opened on a new character with nothing between them; no existing gate could see it.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "305",
     "quote": "Cheap to author and invisible to every existing gate."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Record how each scaffold fades as data — how many uses remain and what retires it — and check that support shrinks across the sequence, because a fade plan written only in prose never fades.",
   "kind": "measured",
   "found_by": "The fade-condition criterion stayed open for two review rounds because a sentence in a document satisfied it while nothing faded.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "238-239",
     "quote": "The reason it stays open is that \"states a condition\" is satisfiable by a sentence in a document nothing reads, so nothing ever fades."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md",
     "lines": "24",
     "quote": "every scaffold states a fade/retirement condition"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "For evidence-based answers, have learners locate and mark the evidence first and then write in their own words, allowing evidence drawn from several places; write-then-find and copy-then-paraphrase prompts invert the task.",
   "kind": "adopted rule",
   "found_by": "Reviewers found evidence tasks ordered backwards, teaching that evidence is one sentence, and prompts that taught copying.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "81",
     "quote": "find+highlight FIRST, then write in own words"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "80",
     "quote": "often it's 2 ideas synthesized from different places"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "179-180",
     "quote": "copy-then-paraphrase writing prompts that teach plagiarism"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Don't score learners on a form of answer the teaching never demonstrates.",
   "kind": "measured",
   "found_by": "A lesson graded learners on producing a quoted form while its modelling omitted the quote marks, across lessons where reproduced text lacked quote marks 60 times.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "404-406",
     "quote": "the lesson grades the child on producing `The text says \"…\"` while the modelling omits the quote marks, so we grade a form we do not demonstrate."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Plan rereading as passes with a stated, deepening purpose aimed at specific parts, because a single read followed by questions, and whole-text repetition by habit, both miss.",
   "kind": "measured",
   "found_by": "Across 18 lessons the text was read once with no mid-text stops; later feedback warned against whole-text repetition as a ritual.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "204",
     "quote": "G3 iter-3: the passage is one block read ONCE, all questions after it (0 mid-passage stops across 18 lessons)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "39",
     "quote": "For unfamiliar material, build more knowledge and reread selected parts of the text; do not make whole-text repetition a universal ritual."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    7
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Keep practice of a new skill blocked until it passes a delayed retest on new items, then mix it into review with no two consecutive items on the same skill.",
   "kind": "adopted rule",
   "found_by": "Practice guidance holding that same-day success measures working memory, applied to interleaving eligibility.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "38",
     "quote": "a delayed (≥24h) retest passed on *new* parallel items — release-day completion never qualifies"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "40-41",
     "quote": "Cumulative interleaved review keeps every cleared track alive, no two consecutive items on the same skill"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Practise understanding by retrieving it and then transforming it — explaining, comparing or placing it — and keep bare recall for fixed facts.",
   "kind": "adopted rule",
   "found_by": "A single mastery gate collapsed acquisition with durable mastery and treated all knowledge alike; guidance split fixed facts from schema-dependent knowledge.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "45-46",
     "quote": "Fixed retrieval is reserved for the anchor class; comprehension KCs never run as bare recall."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "66",
     "quote": "Classify KCs into **Fixed Retrieval**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make most practice build knowledge and understanding rather than imitate the final test, keeping test-format and timed practice for late in the sequence.",
   "kind": "adopted rule",
   "found_by": "Reviewers objected that the course was a practice-test engine; the guidance adopted a 'marathon' rule.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "32-34",
     "quote": "test-format practice concentrated late, timed conditions last."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md",
     "lines": "18",
     "quote": "Knowledge-building activity looks nothing like the paragraph-plus-questions test (marathon-training analogy)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep transfer benchmarks sealed: never teach from them or gate on them, and verify they share nothing with the taught material.",
   "kind": "adopted rule",
   "found_by": "Cold finals were verified to share zero passages with taught units; the benchmark was defined as never a gate or teaching material.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "71",
     "quote": "The cold benchmark is **never a mastery gate and never teaching material**"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-assessor/SKILL.md",
     "lines": "27-28",
     "quote": "passages with ZERO overlap with instruction (verified, the G4/G5 cold-finals property); parallel forms, disjoint."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Sequence learning material so topic knowledge recurs and builds, keeping unrelated unfamiliar material for the test, because coherent sets build more knowledge and incidental vocabulary than unrelated pieces.",
   "kind": "external research",
   "found_by": "Cervetti, Wright & Hwang (2016), DOI 10.1007/s11145-016-9628-x; the first build kept learning texts deliberately non-overlapping and reviewers called that the deepest issue.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "130-131",
     "quote": "Coherent-set readers gained 5.59 vs 2.63 concept idea-units (η²=.32) over six texts in three days (Cervetti 2016, pp. 769–771)."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "166",
     "quote": "Cold plain text belongs at the *test*, not throughout learning; sequence passages so knowledge recurs and compounds"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/sources.qmd",
     "lines": "18",
     "quote": "DOI: 10.1007/s11145-016-9628-x"
    }
   ],
   "against": "SYNTHESIS.qmd 186-187: \"**Cervetti's limits** — N=59, one rural school, on-grade readers, 3-day intervention, null (unreliable) comprehension-questions measure\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Teach general strategies briefly and explicitly and then spend the time on knowledge, because strategy instruction gives its benefit quickly and then stops adding.",
   "kind": "external research",
   "found_by": "Willingham & Lovette (2014), http://www.danielwillingham.com/ : across eight reviews about 10 sessions gave the same benefit as about 50.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "134-135",
     "quote": "Across eight quantitative reviews, ~10 strategy-instruction sessions produce the same comprehension benefit as ~50 — no dose-response (Willingham 2014, p. 2)."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D7-knowledge-first-curriculum.md",
     "lines": "15",
     "quote": "Strategies are a one-time \"bag of tricks,\" taught explicitly then stopped; no strategy-mastery gating (added practice confers no advantage)"
    }
   ],
   "against": "SYNTHESIS.qmd 176: \"The claim is *bounded value*, not *no value*.\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Plan the whole teaching episode — its throughline and persistent example — before breaking it into items, because item-by-item generation yields locally correct pieces that never cohere.",
   "kind": "adopted rule",
   "found_by": "The round-2 sequencing finding on atomise-first generation.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/academics-alignment-plan.md",
     "lines": "16-18",
     "quote": "Atomise-first on narrative subjects produces \"locally-correct micro-lessons that never cohere\" — the round-2 sequencing finding."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "97",
     "quote": "per-item generation with no throughline reasoning → \"locally-correct micro-lessons that never cohere\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make the knowledge sequence visible in the delivered material, because claimed links between lessons that can't be seen by working through it don't count.",
   "kind": "measured",
   "found_by": "A fix report claimed three compounding threads; the reviewers saw unrelated texts with no link, no pre-teaching and no revisit.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "92",
     "quote": "\"3 compounding threads\" claimed; reviewer saw axolotl→shadows with no link, no pre-teach, no revisit"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/timeback-course-eval/references/eval-criteria.md",
     "lines": "153",
     "quote": "Claims that can't be seen by clicking through do not count."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Let a lesson assume only what earlier lessons taught and the learner has shown on a later day, and check that chain in code, because each lesson can look fine on its own.",
   "kind": "measured",
   "found_by": "A negative fixture in which lesson 2 assumed knowledge no earlier lesson added was scored fine lesson by lesson; only the cross-lesson check failed it.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "103-104",
     "quote": "IB scores each of those two lessons as individually fine; only the cross-lesson invariant separates them."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "62-64",
     "quote": "so an anchor first taught the same day never satisfies an `assumes` edge, and an anchor that is present-but-not-fluent is treated as not met."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make every reference to earlier material, such as 'as you saw last lesson', true in the order the learner actually meets it, and check it.",
   "kind": "adopted rule",
   "found_by": "The evaluator gap analysis and gauntlet lint for relational-reference factuality.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "14",
     "quote": "Relational-reference truth check (\"last lesson\" must be factually last)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Label each prerequisite link as logical, evidence-based or merely conventional, and don't let a conventional link block a learner, since prerequisite structures are design choices rather than facts.",
   "kind": "adopted rule",
   "found_by": "A conventional ordering passed off as logical was recognised as a known trap that entrenches misconceptions.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "123-125",
     "quote": "classify each edge logical / empirical / conventional (kc-graph change proposal, warrant field); a conventional edge may not block the on-ramp until upgraded by evidence"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "126",
     "quote": "a *conventional* (untested tradition) edge passed off as *logical* is the Engelmann trap (like/unlike-denominator)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Have people set the sequencing policy and treat a model-generated sequence as a proposal to check against it.",
   "kind": "adopted rule",
   "found_by": "Curriculum-architecture guidance that sequence judgement can't be outsourced to a model.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/curriculum-architecture.md",
     "lines": "31-33",
     "quote": "**You cannot outsource sequence judgment to the model** — the human supplies the policy (spine, entry assumptions, prereq strictness, priority order); the model generates an auditable proposal obeying it."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "75-77",
     "quote": "Any model-generated sequence is an auditable proposal reviewed against this policy, not against taste."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Define each concept once and reuse that exact definition everywhere it is defined, and make the definition complete for the learner, since a true but partial definition teaches the wrong concept.",
   "kind": "measured",
   "found_by": "One concept carried four different definitions in a single lesson; another definition passed four vocabulary criteria and still taught the wrong concept; a later round found the inconsistency still present.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "126-129",
     "quote": "A child cannot resolve that."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "134-135",
     "quote": "the definition passes D4.4, D4.5, D4.17 and D4.24 and is still the wrong concept."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback5/Feedback 11.08.docx",
     "lines": "4 (textutil text)",
     "quote": "This screen is still defining trickster in different language to the vocab screen for it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Define a concept by what it does rather than by a property it often has, because property definitions invite over-generalisation.",
   "kind": "adopted rule",
   "found_by": "A definition that made a typical property definitional produced a wrong generalisation in examples.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "137-140",
     "quote": "Property definitions are what generate the over-generalisation in A3."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Teach a distinction with an example and a non-example that differ in one feature, say why the non-example fails by naming that feature, and then add a very different example that still fits.",
   "kind": "measured",
   "found_by": "53 of 58 non-example cards gave no reason; all four cards in one lesson varied three features at once; a minimal pair alone left an over-generalisation in place.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "396",
     "quote": "| **S1** | Every vocab `non_example` states **why** it is not an example | 53 / 58 cards state no reason |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "158-159",
     "quote": "only the max-different example *kills the over-generalisation the pair invites*."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md",
     "lines": "28",
     "quote": "Non-examples are minimally different from examples to mark the boundary"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Teach a word no later than its first heavy use, make sure every taught word appears in the lesson's own material, and keep what learners are invited to use identical to what was taught.",
   "kind": "measured",
   "found_by": "12 of 46 taught words never appeared in their own passage; one word appeared 8 times in a lesson's passage and 48 times in its bank but was taught a lesson later; word prompts pointed at the wrong words in 16 of 19 lessons.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "210",
     "quote": "iter-3: 12 of 46 taught words never occur in their own passage, so they can't be met in context or tapped there"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "71",
     "quote": "The rule is **first heavy use**, not peak use."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "401",
     "quote": "| **S6** | A declared set equals the set actually used (chips == taught words; scorer credits them) | chips wrong in **16 / 19** |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Count something as already shown to a learner only if every path to that point shows it, because branches they may not take and skippable media establish nothing.",
   "kind": "measured",
   "found_by": "Re-checking prompts with an intersection over branch paths, instead of a union, turned '39 of 46 clean' into 6 more real defects.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "152",
     "quote": "**\"Already seen\" must be an INTERSECTION over branch points, never a union.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "163-164",
     "quote": "The intersection changed the finding from *\"39 of 46 clean\"* to **6 more real defects**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Give each unit one primary understanding and link units by ideas rather than by shared words or names.",
   "kind": "adopted rule",
   "found_by": "Reviewer obligations flagged links based only on shared words and surface cross-unit links.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "237",
     "quote": "J16-CUR-003: Give every unit one primary understanding."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "237",
     "quote": "J16-CUR-004: Use conceptual rather than surface cross-unit links."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Flag simplified models as simplifications and check wording for misconceptions it implies even without a banned phrase, because text that embeds a folk belief undoes correct teaching.",
   "kind": "adopted rule",
   "found_by": "Domain-misconception guidance listed meaning-embedded errors and models presented as literal reality.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "145",
     "quote": "\"the plant grows by taking food from the soil\" implies plants-eat-soil without the literal phrase"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "802",
     "quote": "Simplification is acceptable only when it remains accurate and does not create a later-blocking misconception."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep terms and explanations consistent with how other units and courses teach the same idea, reinforcing established framings rather than silently redefining them.",
   "kind": "adopted rule",
   "found_by": "Cross-unit inconsistency of the same concept's wording was named as a defect class.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "805",
     "quote": "J16-SCI-003: Reinforce rather than silently redefine established domain knowledge."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "149",
     "quote": "reinforce-don't-redefine (consistent with the subject app's framing)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep fact, interpretation, opinion and uncertainty distinct in what learners read.",
   "kind": "adopted rule",
   "found_by": "Reviewer obligation on domain-bearing content.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "805",
     "quote": "J16-SOC-002: Preserve distinctions among fact, interpretation, opinion, and uncertainty."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose material for purpose, genre balance and quality rather than by a single difficulty score.",
   "kind": "measured",
   "found_by": "Selecting texts by readability score alone left about 22% literary content against a 40% target.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "166",
     "quote": "G3 was flagged at **~22% literary vs ~40% target** because texts were picked on Lexile alone"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md",
     "lines": "22",
     "quote": "No rigid monotonic Lexile laddering is imposed, since prior knowledge can make a harder text accessible"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Screen every generated text for difficulty and cohesion, and let the automatic screen reject or flag but never approve, because generated texts tend to run too hard and cohere poorly.",
   "kind": "measured",
   "found_by": "The screen flagged a passage experts had called too hard at cohesion density 0.17 with a three-sentence static run, while a clean sample scored 0.58.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/text-quality-lane.md",
     "lines": "34",
     "quote": "the screen independently flagged **cohesion density 0.17 with a 3-sentence static run**"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/text-quality-lane.md",
     "lines": "5-6",
     "quote": "the machine stage never approves, it only rejects and orders the queue."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md",
     "lines": "21",
     "quote": "AI-generated texts get human/expert QA because they run too hard in syntax and vocabulary and too weak on cohesion"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check a generator's target level before every batch.",
   "kind": "measured",
   "found_by": "A generator was producing passages pitched at grade 11 for a grade-3 course.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "224",
     "quote": "the generator was calibrating passages at **grade 11, not grade 3**; verify the target grade before any batch"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Ramp the length and demand of materials toward what the target task requires, because practising only on short pieces never builds the stamina.",
   "kind": "measured",
   "found_by": "Course passages ran 58–217 words while the target test presents about 2,740 words across passages.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "224",
     "quote": "G3 passages were 58–217w when the test reality is multi-passage (~2,740w); ramp length toward test stamina"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Clear the rights to a source before writing material tied to its exact words, because material coupled to a withdrawn source is lost.",
   "kind": "adopted rule",
   "found_by": "Scripts and citation items couple to exact text, so a passage pulled after authoring loses the lesson's artifacts.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
     "lines": "110-112",
     "quote": "copyright clears **passages before span-anchored authoring begins** — scripts and cite-items couple to exact text; a passage pulled after authoring loses the lesson's artifacts."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When several courses for different levels come from the same guidance, require each to differ in more than difficulty and length, because near-copies tend to be rejected together.",
   "kind": "adopted rule",
   "found_by": "The standing concern that same-guidance courses for several grades were converging and would 'fail in parallel'.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/grade-band-profiles.md",
     "lines": "7",
     "quote": "rejected for the same underlying reasons. We're just failing in parallel."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "99-101",
     "quote": "**\"Sibling clone\" is a blocking red-team finding class**: a design whose only deltas from the nearest sibling are lesson spines/difficulty/units fails review before the academics ever see it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "An in-text explanation works only if readers read it as one, so treat a misread gloss as failed and make it explicit.",
   "kind": "adopted rule",
   "found_by": "A gloss given by apposition was read as a second object rather than an explanation.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "355",
     "quote": "When a reviewer misreads an in-text gloss, the gloss has failed by demonstration; make it explicit."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Word each claim only as strongly as the instrument that measured it, keeping 'built', 'checked', 'live', 'accepted' and 'works' as separate states.",
   "kind": "adopted rule",
   "found_by": "Every build-gate row could be satisfied from metadata and structure; an earlier package asserted 'mastery means mastery' until it was disproven.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/course-quality.qmd",
     "lines": "61",
     "quote": "A fully green build gate proves the course is well-built. It does not prove the course works."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/practice-layer-spec.md",
     "lines": "157",
     "quote": "Claims are licensed by instruments, nothing else"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "26",
     "quote": "Authored, mechanically validated, runtime verified, human accepted, production verified, and outcome validated remain distinct states."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44,
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check every lesson rather than the polished one already shown, and record what was checked, unchecked and excluded, because a quality present in the showcase can be missing from most of the rest.",
   "kind": "measured",
   "found_by": "Real modelling that rejected the tempting alternative held in only a small fraction of 18 lessons, and the reviewed lesson was one of them.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "77-78",
     "quote": "G3 iter-3's real \"reject-the-alternative\" modeling held in 1 of 18 lessons; the reviewed lesson (U2·L1) was that one."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "29",
     "quote": "A coverage manifest names every governed object, checked scope, unchecked scope, failures, and exclusions."
    }
   ],
   "against": "finding-taxonomy.md 191 gives a different count for the same audit: \"existed in **3 of 18** lessons — the reviewed lesson (U2·L1) plus two\".",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Don't let the maker of content certify it, and check any claimed independence of the checker against the record of who actually ran the check.",
   "kind": "measured",
   "found_by": "A deploying lane certified its own items until banned; 191 items were certified on a same-family lane while documents claimed cross-family probing.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "22",
     "quote": "G5 R4: 191 choice items certified on a same-family lane while docs said \"every item blind-probed under a different model family\""
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-content-integrity/SKILL.md",
     "lines": "263-264",
     "quote": "Do not certify your own authored content. The author may fix findings; an independent reviewer must close them."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/evaluator-contracts/SEMANTIC-JUDGE.qmd",
     "lines": "8",
     "quote": "Use a model family independent of generation"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat any relevant change to content, scoring rules, model or display as voiding the checks and certifications done on the old version, and re-run them instead of carrying results forward.",
   "kind": "adopted rule",
   "found_by": "Certification snapshots were withdrawn after source changes; a cached bundle could certify content no longer deployed.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "35",
     "quote": "Evidence records carry artifact and dependency digests; relevant changes force the affected checks to be rerun."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "46-47",
     "quote": "never cache-as-truth (a cached bundle can certify content no longer deployed)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    42
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After fixing or filtering material, check what survived, because a purge of faulty items can silently remove a whole format or a strength that was working.",
   "kind": "measured",
   "found_by": "Every one of 20 two-part evidence items fell into the excluded bucket although reviewers had praised that format, so six-format coverage quietly became five.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "27",
     "quote": "6-format MAP coverage quietly becomes 5-format on the certified core."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "183",
     "quote": "Visual alignment deletes reasoning; simpler flow removes access; old evidence reused after change."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "33",
     "quote": "Impact analysis names affected PRESERVE results; each guard is rerun on changed bytes and passes an equivalence-or-better test."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Quote every count from one dated, re-runnable source and give reviewers the data and tools to recompute it, because hand-typed figures drift between documents and undermine the review.",
   "kind": "measured",
   "found_by": "Counts disagreed across documents (52/745/56 vs 47/713; 541 vs 549 vs 559; tables summing to 520 while claiming 650), and one package cited evidence files it did not include.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "262",
     "quote": "G3's email said 52/745/56 while the infographic said 47/713 (finding #11); G5 certified-count drifted **541 vs 549 vs 559** across docs; MAP-proxy summary tables summed to 520 while claiming 650."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "65-66",
     "quote": "**Prose drifts; data doesn't.** Hand-typed figures across ~15 artifacts WILL drift."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "263",
     "quote": "G4's package cited `course_bank.json`, `item_ledger_manifest.json`, `EVIDENCE_AND_CRITERIA.qmd` etc. but bundled **none** of them, so a reviewer without repo access takes every count on trust."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Never borrow another group's numbers or a biased slice's baseline as your own; mark unmeasured figures as open and re-measure before claiming.",
   "kind": "measured",
   "found_by": "A retired baseline from a biased slice (206.4 / 72nd percentile) overstated the real figure (196.0 / 46th percentile, n=915).",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "262",
     "quote": "the MAP-proxy shipped a retired \"206.4 / 72nd percentile\" baseline that was a biased slice; the real figure was **196.0 / 46th pctile (n=915)**."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "29-30",
     "quote": "**Never invent a magnitude.** Do not carry another grade's/cohort's numbers as if they were this one's."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a reported fix as unverified until it is shown working on the surface the review uses, with the same exploits, because most of one round's 'done and live' fixes failed review.",
   "kind": "measured",
   "found_by": "Most of an 11-item fix report, including the original exploit, failed when reviewers re-tested it live.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "101-102",
     "quote": "Round 2: most of an 11-item fix report failed live review, including the original kill exploit."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "91-93",
     "quote": "**No \"done & live\" without an independent student-seat walkthrough on the same surface the reviewer uses, running the reviewer's exact bypasses.** Two rounds of unverified fix reports is how trust dies."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After a round of fixes, re-derive every earlier finding from the current material and look for new defects the fixes introduced, such as stale figures and contradictions.",
   "kind": "adopted rule",
   "found_by": "Fix waves repeatedly introduced stale paragraphs, count walks that didn't sum and version mismatches.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "306",
     "quote": "Re-verify **every** prior finding by recomputation — not the disposition table."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "308-309",
     "quote": "Sweep for NEW issues introduced by the fix wave (fixes introduce contradictions:"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A rule written into a document is not enforced until a check runs it, so before closing a review round check every previously adopted rule against the material by name.",
   "kind": "measured",
   "found_by": "A round re-reported nine rules adopted five days earlier, three rounds running; 22 of 30 reviewer points were already in the standard but the build shipped without running it.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "87",
     "quote": "The G3 2026-08-11 round re-reported NINE rules adopted five days earlier"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "89-90",
     "quote": "Three consecutive rounds, one unenforced rule. Prose in an addendum gets read, not run."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "1045-1046",
     "quote": "the standard was not missing them, this build shipped without running them."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Before relying on a new check, confirm it catches the example that prompted it and doesn't fire on nearly everything, and report its counts as raw, exempted and real with the exemption rule stated.",
   "kind": "measured",
   "found_by": "Two checks missed their motivating example; a first cut fired 13 of 213 with 11 false; an all-caps sweep read 392 raw of which 284 were real.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "96-98",
     "quote": "correct-is-longest and stem-overlap missed the seed entirely (the real cue was grammatical odd-one-out, 2/151), the first cut of that check fired 13/213 with 11 false"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "102-104",
     "quote": "An all-caps sweep read 392 raw; 104 were play-script speaker labels and a skill name; the real number was 284."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Before reporting something as missing, prove the instrument can see a case known to be there, because an empty result from a blind check is not evidence of absence and two checks using the same blind method agreeing count only once.",
   "kind": "measured",
   "found_by": "An analyzer reported zero standards because it scanned the wrong field; two agents both reported an absence because a NUL byte made their search treat the file as binary.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/timeback-course-eval/examples/reading-explorers-g3-allqtypes.md",
     "lines": "123",
     "quote": "the morning analyzer missed them because it only scanned `rawXml`; standards are in structured metadata, not inline XML"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "96-97",
     "quote": "**Two agents independently agreeing via the same blind method is one unverified claim counted twice, not corroboration**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "98-99",
     "quote": "For a claim of ABSENCE, prove your instrument can see a string you know is there before you trust the empty result."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38,
    35
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Ask what a passing check would still pass on, because a check can be true about the wrong element or data stream and stay green while the real thing is broken.",
   "kind": "measured",
   "found_by": "Three same-day assertions were true about the wrong subject; a header-swap mutation passed 34/34 while the screen showed a wrong total.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "220",
     "quote": "**a gate that asserts something true about the wrong subject.**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "225-226",
     "quote": "a header-swap mutation passed 34/34 while the receipt showed teaching as −1 under \"Reading questions\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Read each rendered screen whole and in display order as the learner meets it, because parts that each pass their own check can add up to a contradictory screen.",
   "kind": "measured",
   "found_by": "Five patches to one panel each passed their own gate while the panel stayed incoherent, showing three ticks for a four-criterion rubric.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "265",
     "quote": "Five patches to one panel each passed their own gate while the panel stayed incoherent."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "267-268",
     "quote": "the tick row showed three criteria while the rubric graded four, so the one criterion that decided the verdict was invisible."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    46
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Run layout checks at the learners' real screen size, because checks run only at desktop size hid an overflow on every screen.",
   "kind": "measured",
   "found_by": "About 29 gates all ran at a desktop size and hid a phone-width overflow on every beat of every lesson.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "280-281",
     "quote": "~29 gates all ran at 1400×1000, hiding a top-bar overflow on **every beat of every lesson**."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    46
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Apply a check to every item type and every file that holds learner-facing content, and fail if that list comes out empty, because checks wired to part of the material leave whole types unguarded.",
   "kind": "measured",
   "found_by": "A position fix covered two item types and missed a third whose keys sat at A 98% of the time (53 of 54); a text check's file list omitted files holding over 120 learner-facing strings.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "120-121",
     "quote": "hook 69% A, we-do 53% A, **vocab 98% A** (53 of 54). A child tapping A scored nearly three quarters of the course's vocabulary."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "127",
     "quote": "**Enumerate every item type that carries a key**, then assert the enumeration"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "84-86",
     "quote": "Its corpus is `FILES` at line 110, five names, which omits `read_stops.json`, `story_pattern.json` and `skill.json`: over 120 strings carrying every stop MCQ and story-pattern row"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    8
   ],
   "name_bearing_source": true
  },
  {
   "statement": "When text that drives generated audio or other media changes, regenerate and verify that media in the same run with exact whole-string matching, because steps that can be run separately get run separately and leave silent gaps.",
   "kind": "measured",
   "found_by": "A rewrite orphaned 117 of 179 narrated strings because regeneration hadn't run; a prefix-tolerant check would have called extended strings healthy.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "61-62",
     "quote": "found **117 of 179 narrated strings orphaned** by the round's own rewrite"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "64-65",
     "quote": "two checks that *can* be run separately *will* be run separately."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "76-77",
     "quote": "**A drift check that tolerates prefixes silently exempts every string that was EXTENDED, and extension is the most common shape of a feedback edit**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24,
    50
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Fix a defect in the source specification or generator as well as in the delivered copy, because a downstream-only fix is undone by regeneration and an upstream-only fix never reaches material already built.",
   "kind": "measured",
   "found_by": "Generator output and shipped lessons were coupled by nothing, and post-hoc fixes were clobbered by a regeneration.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-content-integrity/SKILL.md",
     "lines": "44-46",
     "quote": "A rendered lesson that silently fixes a bad specification does not close the upstream defect because regeneration can reintroduce it."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "392-393",
     "quote": "A rule fixed in the generator prompt does not reach any lesson already on disk, and a fix applied on disk does not survive the next regen"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Where a model speaks before the learner has read the material, don't give it that material, so it cannot give away what comes next; a constraint the system can't break beats a rule the model must remember.",
   "kind": "measured",
   "found_by": "Before the story was opened, the narrator answered a learner by summarising the plot; the fix was to send the model an empty passage before reading.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "45-47",
     "quote": "pre-passage moments send the scorer an **empty passage and empty vocab list**, so it *cannot* quote what the child hasn't read."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "47",
     "quote": "A rule you can't violate beats a rule you must remember."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3,
    67
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Pin each model verdict to a hash of the rules version and the exact content, prefilter in code so the model judges only the suspects, and calibrate on known-good cases every run, so re-runs can't flip results and a broken judge is caught.",
   "kind": "measured",
   "found_by": "A copy-edit gate cut 5,396 strings to about 65 suspects with a code prefilter, pinned verdicts by hash, and refused to run unless 20 known-good strings came back clean.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "84",
     "quote": "**Regex prefilter** cuts 5,396 strings to ~65 suspects, so the LLM judges 1% of the corpus."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "85",
     "quote": "**Verdicts pinned** by `sha256(RULES_VERSION + string)` — a model that flips its mind can't flap the gate."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "86",
     "quote": "feeds 20 known-good strings; all must come back clean, or the judge is broken."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34,
    37,
    67
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Have a model judge quote the evidence it relies on and use a family independent of the generator, keeping its verdict advisory until it is calibrated on expert-labelled examples.",
   "kind": "adopted rule",
   "found_by": "A model judge passed items a hidden-text solve cracked, so semantic checks were made advisory pending expert-labelled anchors.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md",
     "lines": "45",
     "quote": "scored on a model family ≠ the generator, with evidence quotes, against academics-labeled anchor lessons."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a judge that returns the same verdict for everything as having given no answer, not a pass.",
   "kind": "adopted rule",
   "found_by": "Video review lanes saw judges return undiscriminating rows.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/finding-taxonomy.md",
     "lines": "93-94",
     "quote": "**Flat score row** — the judge returns identical/undiscriminating statuses; treat as a non-answer (re-ask once, then RED), never as a pass."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Tag every claim and threshold with its evidence status — measured, asserted, open or working heuristic — and never quietly promote it to a stronger status.",
   "kind": "adopted rule",
   "found_by": "Unsourced or imported numbers kept reappearing as if measured.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "35-37",
     "quote": "**Epistemic tags on shipped claims.** Verified (recomputed/measured) · Asserted (stated in a design, checkable only in delivery) · Open (needs data that doesn't exist yet). Never silently promote Asserted→Verified or Open→Asserted."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/rubric.md",
     "lines": "8",
     "quote": "An [OH] is never cited as a proven learning threshold."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Turn every defect found in review into a permanent test before the fix ships, so the test catches the defect if it ever returns.",
   "kind": "measured",
   "found_by": "A permanent probe for teaching that leaked an item's answer caught that same defect regressing in the next round.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/SKILL.md",
     "lines": "67-68",
     "quote": "**Every externally demonstrated defect becomes a permanent gauntlet probe before any fix ships** (the strongest guarantee in the system: the test outlives the fix)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-1/teacher-skill/gauntlet/CONVERGENCE-REPORT.md",
     "lines": "20-21",
     "quote": "is now a permanent gauntlet probe that earned its keep in round 2 by catching its own regression."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Stop reviewing a layer only after two consecutive rounds find nothing new.",
   "kind": "adopted rule",
   "found_by": "A first zero-finding round was not treated as converged; a confirming round was required.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "3-4",
     "quote": "each layer must go **dry** (two consecutive rounds, zero new findings) before the next."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep checks from becoming the target: rotate probes, hold some back, use judges the builder never used, re-anchor with experts, and audit the checks themselves.",
   "kind": "adopted rule",
   "found_by": "A single-shuffle certification bug showed the gate itself can be the defect.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/SKILL.md",
     "lines": "116-119",
     "quote": "Rotate probe seeds and personas every round; hold out one probe family per promotion; judges from unseen model families; periodic expert re-anchoring; and red-team the gauntlet itself with `course-red-team` (our own single-shuffle gate bug is the standing reminder that the gate can be the bug)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record conflicts between sources, reviewers or rules as named open questions for a decision, and never average them or quietly pick one.",
   "kind": "adopted rule",
   "found_by": "Conflicting guidance (for example on option counts and step order) was logged rather than flattened.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/SKILL.md",
     "lines": "47-48",
     "quote": "Conflicts are recorded in `tensions.md`, never averaged."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/crosswalk/CONFLICT-LEDGER.qmd",
     "lines": "8",
     "quote": "open decisions and fixes are explicit; no conflict was flattened."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "191",
     "quote": "a domain scoring high on frequency but low on load-bearing (present the tension, don't average it away)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Map every point of feedback individually to a decision and evidence, neither dropping it nor silently turning it into a universal rule, because bulk 'addressed' statements lose points.",
   "kind": "adopted rule",
   "found_by": "Bulk 'feedback addressed' claims lost points that reviewers then re-raised line by line.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "25",
     "quote": "Each source point has a disposition and links to one or more requirements, exact evidence, an owner when open, and a closed or unresolved state."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/profiles/base/RED_TEAM_BASE.source.json",
     "lines": "1410",
     "quote": "Feedback is neither dropped nor silently promoted into universal policy."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "54",
     "quote": "Bulk addressed claims; missing source points; evidence with no feedback link."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep a rule scoped to the level, subject or source it came from until someone decides it applies more widely, because grouping or indexing a rule does not make it universal.",
   "kind": "adopted rule",
   "found_by": "Scoped option-count and format rules were explicitly fenced off from other profiles.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/AUTHORITY.qmd",
     "lines": "31-32",
     "quote": "A scoped overlay never silently becomes universal; a runtime or context asset never silently becomes"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
     "lines": "231-233",
     "quote": "The current G3 profile requires at least four options on every MCQ, prohibits mastery True/False, and prohibits EBSR; do not generalize those thresholds to another profile."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In a review of outside sources, treat a technique seen once as a candidate and promote it to a rule only when it recurs across independent batches.",
   "kind": "adopted rule",
   "found_by": "Method used to review 269 teaching transcripts against the standard.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/IES-CORPUS-REVIEW-2026-08-05.md",
     "lines": "17-18",
     "quote": "Findings that recurred across *independent* batches were treated as high-confidence; a technique seen once was treated as a candidate, not a rule."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Research that supports a design is not evidence that your implementation of it works, so never cite it as an outcome.",
   "kind": "adopted rule",
   "found_by": "The evidence base was being read as proof of the courses built on it.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/PRIORITIES.qmd",
     "lines": "82-83",
     "quote": "corpus grounds DESIGN, it does not prove OUR implementation works. Never cite it as evidence about our courses' outcomes."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48,
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When turning source documents into a knowledge base, check each extraction reaches the document's true end, never ingest an empty extraction, and copy source text by file rather than having a model retype it.",
   "kind": "measured",
   "found_by": "Two sources failed ingestion when agents re-emitted full text; boundary spot-checks were added to confirm complete extraction.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/EXTRACTION_EVIDENCE.qmd",
     "lines": "39",
     "quote": "(does each extraction reach the document's true end?)"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/EXTRACTION_EVIDENCE.qmd",
     "lines": "47-49",
     "quote": "the full texts here were never re-typed through a model."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/knowledge-ingest/SKILL.md",
     "lines": "41-42",
     "quote": "a scanned PDF yielding whitespace is `skipped: needs-manual-export`, never ingested empty."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Label results from simulated learners as predictions, never outcomes, and calibrate them against real learners when that data exists.",
   "kind": "adopted rule",
   "found_by": "Role-played students were judged structurally flawed and synthetic-profile numbers untrustworthy in magnitude.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "50-51",
     "quote": "**All results labeled SIMULATED**; calibrate against real-student data as pilots run."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
     "lines": "123-124",
     "quote": "LLM student role-play is structurally flawed and caps ~67% accuracy; teacher-as-predictor reaches r≈0.72–0.79 population-level"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    47
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Put nothing in front of learners that no person has read, since even a sampled human review is far better than none.",
   "kind": "measured",
   "found_by": "Two courses went to review with every item (772/772 and 957/957) marked as never read by a person.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "263",
     "quote": "`humanApproved:false` on 772/772 (G5) / 957/957 (G4) submitted to educators means \"no human has read what you'd put in front of ten-year-olds\""
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
     "lines": "101",
     "quote": "Human edit pass before ship — \"several read as unedited AI output\" must never recur."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Remove items known to be faulty from what learners see, not just from scoring, because a guessable item still rewards skipping the work.",
   "kind": "measured",
   "found_by": "231 of 772 items (30%) classified as guessable stayed live in front of learners though excluded from gates.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
     "lines": "233",
     "quote": "G5 shipped with **231/772 (30%) classified known_leaky still live** (excluded from gates but in front of children)"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "17",
     "quote": "A leaky item awards progress for non-reading"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Provide an unlocked path through every lesson for review, but keep its controls out of learners' reach and stop it creating learner records.",
   "kind": "measured",
   "found_by": "Locked progression left 4 of 11 review items unverifiable; the rule now requires reviewer controls to leave learner records unchanged.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "105-106",
     "quote": "Locked lesson progression blocked half the round-2 review — 4 of 11 items came back \"unable to verify\"."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "34",
     "quote": "Free navigation, answer reveal, reset, and reviewer-only controls leave mastery, reward, completion, and unlock records unchanged."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Formats chosen to resist guessing are often the least accessible, so prove keyboard and assistive-technology operation for every interaction type and don't let anti-guessing controls block legitimate access.",
   "kind": "measured",
   "found_by": "A design concentrated 525 of 772 items in guess-resistant formats that were the accessibility-risk types; 406 of 1,005 items (40%) were not keyboard or assistive-technology operable.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "15",
     "quote": "the anti-leak thesis deliberately concentrates items in the TEI formats (hot-text/sequence/match = 525/772) that are precisely the accessibility-risk types."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "63",
     "quote": "Accessibility: 406/1,005 (40%) not keyboard/AT-operable"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "535",
     "quote": "Anti-gaming controls must not block legitimate accessibility paths."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    27
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a bypassable gate as a teaching failure, not just a security gap, because it moves learners past what they know and corrupts the data used to improve the material.",
   "kind": "adopted rule",
   "found_by": "A gameable course was recognised as producing unusable outcome data as well as mis-placing learners.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/timeback-course-eval/references/eval-criteria.md",
     "lines": "135",
     "quote": "produces a *poisoned feedback signal* — kid-outcome data from a gameable course can't improve"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "58-59",
     "quote": "A gate a child can bypass doesn't just corrupt the data; it places the child outside their zone of proximal development *by construction*"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count content that is authored but never shown as missing, and check the delivered surface rather than the data.",
   "kind": "measured",
   "found_by": "Word-use prompts were authored at full quality in all 18 lessons but never rendered; modelling rationales existed in the data while the screen performed none of them.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "350",
     "quote": "Clicks counted as production; authored prompts never render"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/FEEDBACK-AUDIT-2026-07-29.md",
     "lines": "45",
     "quote": "are authored at full quality in all 18 lessons and **never rendered**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "325",
     "quote": "every I-do step carried its span anchor and its rationale, and the screen performed none of them."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Give progress and rewards only for verified learning, so unmastered work, guessed-through retries and replays earn nothing.",
   "kind": "measured",
   "found_by": "A reward broker fabricated quiz rewards with no accuracy floor; a later build correctly recorded a four-tap guess-through as zero.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "73",
     "quote": "One reward unit has a published meaning; full reward follows verified mastery; non-mastered work earns zero; nothing below eighty percent earns reward; replay cannot duplicate it; ledger and display agree."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/timeback-course-eval/examples/reading-explorers-g3-allqtypes.md",
     "lines": "187",
     "quote": "Team found the broker fabricates quiz XP with **no 80% floor**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-R2-2026-08-06.md",
     "lines": "185-186",
     "quote": "so the 4-of-4 guess-through banks **zero** quality."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    14
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Don't rely on learners' own sense of whether they understood, because people judge their own comprehension poorly; check with a task.",
   "kind": "external research",
   "found_by": "RAND Reading Study Group (2002), https://www.rand.org/pubs/monograph_reports/MR1465.html, App. A pp. 108-109.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/SYNTHESIS.qmd",
     "lines": "180-181",
     "quote": "\"most child and adult readers have a poor ability to calibrate the success of their comprehension\""
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D6-practice-durable-mastery.md",
     "lines": "25",
     "quote": "schedule on accuracy+latency, not self-report"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Assess more than a few task types, because assessments built on a narrow set of tasks tend to shrink teaching to rehearsing those tasks.",
   "kind": "external research",
   "found_by": "RAND Reading Study Group (2002), https://www.rand.org/pubs/monograph_reports/MR1465.html, p. xix.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/SYNTHESIS.qmd",
     "lines": "127-129",
     "quote": "\"assessments that are widely used today focus heavily on only a few tasks and thus may inadvertently limit the reading curriculum to preparation for those few tasks.\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A model's score on questions about teaching does not show it can produce good teaching material, so judge the material it generates.",
   "kind": "external research",
   "found_by": "Singh et al. (2026), Frontiers in AI, DOI 10.3389/frai.2026.1851993 (the authors' own limitation); reviews also found a generator that 'knew' the method still produced answer-reveals.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/DIGEST-singh-eduqwen-2026.qmd",
     "lines": "34",
     "quote": "strong benchmark performance on pedagogical knowledge questions does not itself constitute evidence of effective classroom tutoring"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/DIGEST-singh-eduqwen-2026.qmd",
     "lines": "6",
     "quote": "DOI 10.3389/frai.2026.1851993"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/train-teacher-requirements.md",
     "lines": "19-20",
     "quote": "a generator can \"know\" gradual release and still emit answer-reveals."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Evaluate a content generator on topics kept out of its training and prompts, against a baseline given identical inputs, and replicate before claiming a gain.",
   "kind": "adopted rule",
   "found_by": "A pre-registered evaluation contract for a teaching-model experiment.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "71",
     "quote": "A model trained on a cold topic cannot be evaluated on it."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "53-54",
     "quote": "Isolates what training added; run it or the result is uninterpretable."
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "75-76",
     "quote": "any bar-hit claim needs 2 independent generation runs; a single run is a single-point estimate."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    70,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prefer assembling and adapting vetted material over generating items from scratch, and treat anything generated as a candidate until a separate check passes it.",
   "kind": "adopted rule",
   "found_by": "A cited review of nine quiz generators found 80% of items broke a guideline and 74% had major flaws.",
   "evidence": [
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
     "lines": "56-57",
     "quote": "But of 9 Gen-AI quiz builders studied, **80% of items violated ≥1 best-practice guideline and 74% had major flaws — only 1 in 5 usable**"
    },
    {
     "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
     "lines": "59-60",
     "quote": "**Design generators that assemble + transform vetted material and tag to standards — not ones that invent items from scratch.**"
    }
   ],
   "against": "practice-layer-spec.md 21-22: construction-first generation still certified \"48.7% (738 certified of 1,516)\" under gates; the cited review has no DOI or URL in these files.",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "114",
   "quote": "On a miss: **Correct** (answer + brief why) → **Test** (re-ask immediately) →"
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D1-gradual-release-explicit-instruction.md",
   "lines": "36",
   "quote": "wrong answers corrected immediately with the correct answer + brief why"
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g5-reading/approval-package/D9-GATE-WALKTHROUGH.md",
   "lines": "30",
   "quote": "**The correct answer is shown after a miss** (auto-highlighted)"
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
   "lines": "50",
   "quote": "a wrong answer returns only \"Good try, let's look again,\" with no explanation and no correct answer shown."
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D2-opportunities-to-respond.md",
   "lines": "25",
   "quote": "The app never restates the correct answer for the child; it prompts the child to complete/say it"
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "399",
   "quote": "Immediate answer reveal; identical retry; endless loop; supported retry counted as first independent success."
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/rubric.md",
   "lines": "88",
   "quote": "One calm, grade-appropriate voice, conversational 2nd person (r15)."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/labeled-defect-corpus.jsonl",
   "lines": "2",
   "quote": "teaching content leaking the answer to the check it precedes."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "883",
   "quote": "Vocabulary support must not pre-answer the target question."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "43",
   "quote": "The durable rule is attempt first, then targeted help."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
   "lines": "226-227",
   "quote": "RT-10 found the video-2 check answerable from the title alone."
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "43",
   "quote": "offered three consecutive errors as a possible backend trigger"
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-R2-2026-08-06.md",
   "lines": "159",
   "quote": "`buildMCQ` has no lockout and never withholds the key, so every stop released on or before the 4th tap."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
   "lines": "43",
   "quote": "6/6 were solvable without the passage:"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
   "lines": "233",
   "quote": "a course-wide audit found **~half of ~700 items gameable**"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-R2-2026-08-06.md",
   "lines": "88",
   "quote": "A clean-room blind-solver with no passage got **4/4** and reported that not one item required reading."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-content-integrity/SKILL.md",
   "lines": "155-156",
   "quote": "\"The intended answer is stronger\" does not repair a hard-scored item when another option also answers the question."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd",
   "lines": "59-60",
   "quote": "One hot-text prompt can reasonably be answered by either winter or spring camouflage, while only the winter sentence is keyed."
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "205",
   "quote": "stop at key points INSIDE the text and ask right there (REL West), not only at the end"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
   "lines": "225",
   "quote": "the G4 pull found **79% of MCQ correct answers at Choice A**"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
   "lines": "255",
   "quote": "`shuffle=\"true\"` in the authored XML neutralizes an answer-position skew ONLY if each renderer honors it."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-content-integrity/SKILL.md",
   "lines": "24-25",
   "quote": "`NEEDS_HUMAN`: evidence is missing, conflicting, inaccessible, malformed, or specialist judgment is genuinely required."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/course-quality.qmd",
   "lines": "77",
   "quote": "A surface may have emission code but an unreadable or under-scoped token (a reachability gap), or may not emit at all (a coding gap). The first is `UNVERIFIED` pending a scoped read; the second is `FAIL`."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "655",
   "quote": "Keyword or word-count pass called comprehension"
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-LIBRARY-USABILITY-CLEAN-ROOM-2026-08-07.qmd",
   "lines": "64",
   "quote": "Written-response completion can accept a fluent but false response through length and selection counts."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
   "lines": "32",
   "quote": "Short-text items use a small 0/1/2 micro-rubric, not an ever-growing exact-match list"
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/grade-band-profiles.md",
   "lines": "44",
   "quote": "child-ASR ~13% error blocks production mastery"
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "705",
   "quote": "Speech can support practice without becoming protected evidence unless its scoring is validated."
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/PROJECTION.qmd",
   "lines": "50-51",
   "quote": "a prompt-like unknown field also fails the closed input contract and is never treated as an instruction."
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "400",
   "quote": "Repair evidence remains distinct from first-try evidence."
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D5-assessment-item-construction.md",
   "lines": "42",
   "quote": "No mastery decision rests on a single MCQ (≥25% guess); use item bundles"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/IES-CORPUS-REVIEW-2026-08-05.md",
   "lines": "121",
   "quote": "116 of 116 confirmed as real substrings, zero invented."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/reading-science/EXTRACTION_EVIDENCE.qmd",
   "lines": "32",
   "quote": "230/230 extracted quotes verified verbatim at extraction time"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-1/teacher-skill/gauntlet/layer5/RESULT.md",
   "lines": "39",
   "quote": "**Fabricated evidence**: Q16 Part B quotes a sentence not in the text."
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "210",
   "quote": "iter-3: 12 of 46 taught words never occur in their own passage, so they can't be met in context or tapped there"
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/rubric.md",
   "lines": "13",
   "quote": "Audio is the master clock; a reveal MUST NOT complete before its term is spoken (r4)."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback5/Feedback 11.08.docx",
   "lines": "14 (textutil text)",
   "quote": "The things being done to the text must happen immediately after they are spoken about."
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "24",
   "quote": "image-model text corruption"
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/source-course-refinement.qmd",
   "lines": "102",
   "quote": "If an additive layer changes source content, split the change and re-run no-cut."
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/source-course-refinement.qmd",
   "lines": "47",
   "quote": "| No silent cuts | Missing source ids fail the build. |"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "91",
   "quote": "Unit-2: a fix-note said \"11w\" while the delivered option was 10w"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "176",
   "quote": "Measured: informational passages were **312–333** while"
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D10-delivery-ux-accessibility.md",
   "lines": "18",
   "quote": "No on-screen text that merely duplicates speech"
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "83",
   "quote": "too much on screen"
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "88",
   "quote": "**Automated WCAG contrast checks** in render QA (round-2 found black-on-black)."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "84-85",
   "quote": "**Attention/read gates must block.** Any nudge skippable by an extra click is a"
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-LIBRARY-USABILITY-CLEAN-ROOM-2026-08-07.qmd",
   "lines": "65",
   "quote": "One incorrect comprehension response unlocks `Next` while the feedback still says `Pick again`."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-4/REDTEAM-U1L1-2026-08-05.md",
   "lines": "41",
   "quote": "**one child tap defeats every gate in the lesson** (live-proven)"
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-modes-spec.md",
   "lines": "34",
   "quote": "Deterministic span-acceptance rules first; LLM grading only after a calibration pass — until then this step never blocks progression."
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
   "lines": "86-87",
   "quote": "so author annotations (\"possibly removed\") register as false positives."
  },
  {
   "truth": 32,
   "effect": "counter",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/train-teacher/references/gauntlet-spec.md",
   "lines": "38-39",
   "quote": "adversarial framing (\"try to refute that this teaches\")"
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
   "lines": "231",
   "quote": "IB quality scores are the MEDIAN of 3 runs (non-determinism precedent: 0.95/0.92/0.98 on identical content)."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
   "lines": "34",
   "quote": "now \"internal cross-bank consistency (synthetic),\" explicitly not MAP agreement"
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "20",
   "quote": "sequence items certified against one seeded shuffle; multi-shuffle re-probe decertified 72 incl. one exact 1.000"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/SKILL.md",
   "lines": "110",
   "quote": "advisory until calibrated on academics-labeled anchor lessons"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "102-103",
   "quote": "No auto-score gates progress until the rubric-calibration harness proves LLM-vs-SME agreement"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "208",
   "quote": "`UNIT=2` instead of `U2` matched no lessons — judged 6% of the corpus, printed ALL PASS"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
   "lines": "75",
   "quote": "8 failing fixtures + 1 passing unit, one failing"
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "77",
   "quote": "camouflage lesson modeled BEFORE the child read the text and set no reading purpose"
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "643",
   "quote": "J16-LES-002: Provide a complete first encounter before close analysis."
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
   "lines": "208-209",
   "quote": "Two independent instruments landing on one item is the strongest signal in the document, and it is the argument for running both."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
   "lines": "69",
   "quote": "Structurally-verified ≠ instructionally-sound."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "57",
   "quote": "A clean automated report is useful pre-review evidence, never a substitute for reviewer judgment."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback5/Feedback 11.08.docx",
   "lines": "4 (textutil text)",
   "quote": "no one has managed to come up with a perfect set of rules to get an LLM to generate these without human review yet."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
   "lines": "5-7",
   "quote": "primary metric, test set, baselines, ceiling, and gates are fixed now; any later change is an appended methodology-correction note, never a rewrite."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
   "lines": "206-207",
   "quote": "A gate proven on one surface proves nothing about another."
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "86-87",
   "quote": "**Wrong answers must not pass.** Re-run the reviewer's exploit — all-wrong answers through a full lesson — on every delivery surface before any gate claim."
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback1/Reading_Explorers_v2_Feedback (1).docx",
   "lines": "61 (textutil text)",
   "quote": "in a main-idea task we earned the pass while answering every question incorrectly."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/course-quality.qmd",
   "lines": "61",
   "quote": "A fully green build gate proves the course is well-built. It does not prove the course works."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/instruction-quality-standard.md",
   "lines": "120-121",
   "quote": "Durable mastery requires a **delayed"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "284-285",
   "quote": "Twice I reported results from a file that moved mid-run."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
   "lines": "24",
   "quote": "Source commit, source digest, release digest, live digest, route, and evidence identify the same immutable artifact."
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
   "lines": "143",
   "quote": "A generator optimizing for pass-rates or engagement will quietly lower rigor"
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/rubric.md",
   "lines": "100",
   "quote": "suppressed when a text card shows the same words (r18)."
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/feedback/feedback5/Feedback 11.08.docx",
   "lines": "10 (textutil text)",
   "quote": "not everything Scout says needs to appear on screen"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D2-opportunities-to-respond.md",
   "lines": "18",
   "quote": "is actually reachable for the child who freezes or says \"I don't know\""
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/generator-insights.md",
   "lines": "71",
   "quote": "**Ungrounded generation is where the 74%-flaw rate lives.**"
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
   "lines": "10",
   "quote": "Facts: ONLY this lesson's `lesson.json` passage."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "168",
   "quote": "Human override cannot erase factual, safety, or integrity failures."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/SKILL.md",
   "lines": "308-309",
   "quote": "Sweep for NEW issues introduced by the fix wave (fixes introduce contradictions:"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/README.md",
   "lines": "132",
   "quote": "scope mismatch, two schema/policy misses, one metadata-confirmed conflict"
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/g3-reading-red-team/references/dimensions/D8-text-quality.md",
   "lines": "32",
   "quote": "Reject passages whose graphics decorate rather than carry meaning"
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "36",
   "quote": "| Decorative filler | b-roll/motion with no fact_id |"
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/course-formula-agents.md",
   "lines": "218",
   "quote": "systematic defect patterns (same defect class across a whole batch = generator prompt bug, not per-item fixes)."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "21",
   "quote": "G5: deploying lane certified its own items until the protocol banned it"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
   "lines": "69",
   "quote": "op-lint's deterministic layer catches **6 of the 10 round-2 academics failure shapes**"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "275-277",
   "quote": "That's a 7,000× difference."
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
   "lines": "224-225",
   "quote": "a token which uniquely identifies one item's key must not appear in another item's stem, options, or feedback anywhere in the same lesson"
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "79",
   "quote": "is the comprehension question bespoke to THIS text, or a generic template?"
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/Offloaded Project Archives/[name]’s Mac mini/20260902T193311Z/Projects/ti-courseplans/courses/g3-reading/iteration-1/teacher-skill/gauntlet/layer5/RESULT.md",
   "lines": "34",
   "quote": "**Generic identical feedback on all 16 items**"
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/docs/plain-english-explainer.md",
   "lines": "40",
   "quote": "Two of those five things actually helped. Three made it worse."
  }
 ]
}
```
