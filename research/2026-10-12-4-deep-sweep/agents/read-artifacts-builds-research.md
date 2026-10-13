# read:artifacts-builds-research

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "artifacts-builds-research",
 "coverage": {
  "read": [
   "~/Projects/grade3-reading/artifacts/DECISIONS-2026-08-24.md",
   "~/Projects/grade3-reading/artifacts/CLOSURE-PLAN-2026-08-25.md",
   "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
   "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md, LANE2_GENERATOR.md, LANE3_FIRST_EXPERIMENT.md, LANE3_LLM.md, LANE3_LLM_UPDATED.md",
   "~/Projects/grade3-reading/artifacts/X1_staar_map_overlap_probe_2026_06_16.md",
   "g5-course/: all ADVERSARIAL-REVIEW rounds R1-R26 (R13-R16, R19-R21 skimmed), LESSON-AUTHORING-PLAYBOOK, AUTHORING-RULINGS-R1-R10, VOCAB-DECISIONS-U1/U9, VOCAB-PRONOUNCE-STEP-DECISION, VOCAB-PROGRAM-CROSSREF, PD-FICTION-RESEARCH, pd-texts/winnie-the-pooh-onepager + readability.py/analyze.py + readability-results.json header, G5-CURRICULUM-ONE-PAGER, G5-CURRICULUM-OUTLINE (first 140 lines), CURRICULUM-REVIEW-STANDING, COVERAGE-CLOSURE-VERIFICATION, RULING-B-CARRIED-MASTERY, TERMINOLOGY-AUDIT, WWVCD-HARNESS-AUDIT, G3-U1-L4-RESIDUAL-ADJUDICATION, CAPSTONE-PROCEDURE-RULING, PROCEDURE-RULINGS/U1L7 (part), PROCEDURE-AND-IWY-FOCUS (headers), GAP-ANALYSIS, DATA-FIX-DOSSIER, HUMAN-BODY-III-DECISION",
   "g5-book-2026-09-29/: logs/GATE-VERDICT.md, SCOUT-AND-PLAN.md, BUILD-SPEC-G5-U1-L1.md (grep)",
   "g5-merged-course/: corrective-feedback-policy, audit-heuristic-finding, a2-cross-family-regate, leaky-vs-gate-unreachability, GENERATOR_DIRECTIVE, g5-course-bar-checklist-v1, VERDICT_TEMPLATE, a11y-static-scan, markdown-normalization, option_cap_report (head), MERGED_COURSE_SPEC (grep)",
   "g5_build_2026_07_02/: BUILD_FACTS, feedback_clean (external review), approval_clean (case + BrainLift), mapproxy_clean (SPOVs/insights), g5_analysis_digest (first 60 lines)",
   "course-json-standard-2026-07-13/: README.md, examples/reverify-v022-report.md (grep)",
   "course-factory-skills/PLAN.md (head)",
   "decision-brief-2026-09-10/DECISION-BRIEF.md",
   "decision-matrix/: README, STATS, slice headers + a few targeted rows (07, 08)",
   "decision-packets-2026-09-03/PACKETS.md (first 50 lines)",
   "wiki-research/: redteam-standard, cross-cutting (sections 4-6), pedagogy-llm-evals, pedagogy-llm-method (grep)",
   "team-direction-2026-09-09/: GATE-STANDARD-DRAFT, CONVERSION-RATE, AUDIT-RECALIBRATED, REVIEW, DIRECTION-2026-09-09, research/02 (SPOV audit), research/03 (grep)",
   "edullm-agent-entrypoint-g3-practical-test-2026-08-06/REPORT.qmd",
   "edullm-standards-centralization-2026-08-05/: README.qmd, IMPLEMENTATION-PLAN.md (parts), EXECUTOR-RUNBOOK.qmd (lines 520-560), SOURCE-AND-AUTHORITY-LEDGER (grep)",
   "baseline-submission/CHANGES-FOR-REVIEW-L4-2026-08-31.md",
   "build-closing-questions-2026-09-25/: BUILD-SPEC.md, verify/DIGEST.md, logs/baseline-reds.md",
   "Dated folders: course_approaches_20260616 (Proposal Review & Synthesis docx via textutil; [name] v2 brainlift/README/course-skeleton part; [name] v3 brainlift), knowledge-first-reading-course-proposal-2026-07-09 (00-04, 06-09, 13-15, STATUS), g5-expansion-session-2026-07-08-codex (QUESTION_GENERATION_RETROSPECTIVE), g5-expansion-session-2026-07-08-claude (BANK_REPORT, SOLVER_V2, CONTROL_INSTRUCTIONS), scoring-rule-probe-2026-07-10, g3-control-set-2026-07-10 (G3-CALIBRATION-REPORT), op-taxonomy-calibration-2026-07-10 (calibration + round-2 review text), demo-unit-2026-07-10 (knowledge inventory, difficulty notes, factuality claims head, phase-d gate summary, DELTA-REPORT grep), curriculum-adherence-2026-09-24 (CRITIC, REPORT head), arc-audit (SIM-REVIEW-D1-D4, SIM-REVIEW-D7-D8-D10-D12 parts), takeover-audit-2026-07-13 (pr68-enforcement-audit, g5-clean-baseline parts), art-qa-redcontrol-2026-09-11/RECORD, whisper-qa-2026-09-02/REPORT, HUMAN-REVIEW-2026-09-21/README, l4-p3-stale-clip-2026-09-29/README, sim-review-2026-09-02/FINDINGS, qc-run-2026-09-04 QC run report (head), feedback-inceptbench-2026-09-30 (REGISTER, BUILD-SPEC-batch head)"
  ],
  "skipped": [
   "g5-course/OVERNIGHT-LOG-2026-08-18.md (383 KB run log), pd-texts/raw/* (full novels), probes/* (code + raw JSON), other pd-texts one-pagers/content screens (one sampled), PLAYER-GENERALIZATION-SPEC, PLATFORM-DECISION-DOSSIER, FIGURE-SPECS-NEEDED, STATION-AUTHORING-PROPOSAL, COURSE-PLAN, COURSE-INVENTORY, PLAN-G5-ONTO-RENDERER, MEETING-EXTRACT, HANDOVERs, CLOSE-OUT, SYNC-BRIEF, PR3-ANALYSIS, PR-CLOSURES, F1-FORK-CLOSURE-LOG, UPSTREAM-STATE, OVERNIGHT-MISSION (time; mostly process/handover); g5-course/[name]-ido-redesign/* (person-named path, read once, not used)",
   "g5-book-2026-09-29: html-structures (multi-MB HTML), JSON specs, tools, logs except GATE-VERDICT",
   "g5-merged-course: approval-package/* (person-named '[name]' files), JSON manifests/reports, python scripts, readback/stimuli data",
   "g5_build_2026_07_02: meeting_clean (meeting notes, organisational), doc_chunks (duplicates), lessons/*.json and raw snapshots (data)",
   "course-json-standard: schema, validator code, conversion spec, skills (tooling)",
   "decision-matrix: CSV slices beyond header/few rows and shards/*.jsonl (data dumps per rules), miner scripts",
   "edullm-standards-centralization: runs/*.csv (data), most runs/*.qmd, scripts",
   "build-closing-questions: specs/scratch JSON and scripts",
   "team-direction: TEAM-MESSAGE, DIRECTION-ONE-PAGE, DIRECTION-ARC, AUDIT-AND-FOCUS, research/01 (team direction/organisational)",
   "session-analysis-2026-09-22 (raw user-message dumps), listen-qa-* and l1-parity-untracked (transcript data), qc-2026-09-29/30-staging (large staging dumps), visual-audit-2026-09-07, compare-*, branch-audit-2026-09-24, hosted, kb-rebuild (empty), wip-backup, pr27-frozen, agentize-upstream (git/tooling state), plan-2026-09-10 (process plans), red-team-2026-09-23, rulings-2026-09-23 (empty), g5-media-recovery-2026-08-12, p0_apply/p1p2_apply logs, sim-review-2026-09-24/CLOSURE-PLAN, most arc-audit registers and PEDAGOGY-L* files, curriculum-adherence designs/texts, initiative-g9-othello-2026-10-01 (other project), feedback-* dated folders other than feedback-inceptbench-2026-09-30 (time; likely another direction)",
   "Person-named folders (catchup-[name], feedback-[name]-*, feedback-[name]-[name], feedback-[name]-qc, [name]-*, [name]-[name]-coverage, top-level [name] v2/v3, ujjawal_[name]_rex_v2_compare, u4l2-[name]-style) per scope rule; only the [name] v2/v3 copies inside the dated course_approaches_20260616 folder were read, for the AP evidence"
  ],
  "notes": "AP: the only AP material in scope is AP-history pipeline evidence inside person-named proposal folders (course_approaches_20260616/Course Approaches/[name] v2 and [name] v3): cheap holistic ranker kappa=0 with zero best-of-N lift, verifier sets the ceiling, 10 hand-fixes failed vs best-of-N pass in 2, flip-band defects and ~21% non-deterministic verdicts, 16.7% machine-human agreement on a loose essay rubric, and the subject-dependent meaning of a leak (history source vs reading text). Those candidates are flagged name_bearing_source=true; non-name corroboration was used where it exists (approval_clean.md, the codex retrospective). Knowledge: strongest knowledge lessons come from the two external reviews (g5_build_2026_07_02/feedback_clean.md; op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt), the knowledge-first proposal packet, the demo-unit knowledge inventory and difficulty notes, SIM-REVIEW D7, GAP-ANALYSIS and CURRICULUM-REVIEW-STANDING, and VERDICT_TEMPLATE (knowledge-recall items fall to ~0 under the text-dependence gate). Conflicts worth noting: hot-text leak ~17.5% in one pool (LANE1) vs 90.6% in another under two-family scoring (a2); multiple-choice never reveals and open responses get three turns (counter to truth 4); student quote matching uses 95% similarity in one renderer vs exact-match fail-closed in the G5 playbook (limit on truth 17); assemble-and-tag-only authoring doctrine was superseded by pedagogy-trained authoring models (limit on truth 29). Proposal Review & Synthesis docx line numbers refer to textutil plain-text output. Read-only throughout; nothing written."
 },
 "candidates": [
  {
   "statement": "Before acting on an audit finding, re-check it against the current file and against the approved reference lessons; many critical findings do not survive that check.",
   "kind": "measured",
   "found_by": "Across one build session roughly half of critical audit claims were false, each traceable to not checking whether the approved reference lessons did the same; a later residual list of ten findings had nine dismissed this way; two independent audit lanes measured an 8–15% false-positive rate for single-pass findings.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/DECISIONS-2026-08-24.md",
     "lines": "78",
     "quote": "roughly half of \"CRITICAL\" audit claims were false"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md",
     "lines": "10",
     "quote": "Verdicts: **1 CONFIRMED, 9 DISMISSED** (plus the 3 engine-debt items carried unchanged)."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "129",
     "quote": "false-positive rate of single-layer findings is 8–15% across two independent lanes"
    }
   ],
   "against": "The reference test can bless a gap the references share: \"aspiration the references do not meet either. Not a defect.\" (g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md line 27).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a check reports defects, test the check before fixing the content; broken probes produce convincing false defects.",
   "kind": "measured",
   "found_by": "Half of reported audio defects were faults in the checking probe; a transcription batch writing outputs by bare filename invented 27 cross-lesson errors; a leak probe was trusted only after it scored a known-clean pool near zero.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "108",
     "quote": "Provenance: probe-is-often-the-bug — half of \"audio defects\" were defective"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/whisper-qa-2026-09-02/REPORT.md",
     "lines": "10",
     "quote": "itself and \"finds\" cross-lesson bleed that isn't there. First pass flagged 27 such"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md",
     "lines": "47",
     "quote": "The same probe scored the **172 certified-clean** pool at ~0–1.7% leak — the"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never certify a course from the lesson that was reviewed; recompute each quality claim across every lesson, because a quality or a fix in one lesson often does not hold in the others.",
   "kind": "measured",
   "found_by": "A quality standard recorded that real modelling held in 1 of 18 lessons — the one that had been reviewed; a later simulated review found a defect recurring one lesson after its fix.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "118",
     "quote": "Never certify on the lesson the reviewer saw. Recompute every quality"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "120",
     "quote": "\"real modeling in 1 of 18 lessons — the reviewed one.\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D1-D4.md",
     "lines": "301",
     "quote": "recurrence of the PP-12 defect pattern one lesson after its fix"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Treat your own completion claims as hypotheses and re-derive them from the delivered content; a count can be right while the quality it implies is not.",
   "kind": "measured",
   "found_by": "A claim of 7–8 generated responses per lesson was true by count but 5 of 7 spoken moments were canned; a status file claimed a unit's audio done when 3 of 9 lessons had it; a format-compliance claim could not be checked from the files it relied on.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "123",
     "quote": "was \"true by count, misleading by quality — 2-3 trivial say-backs; 5 of 7 spoken moments canned.\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/GAP-ANALYSIS-2026-08-18.md",
     "lines": "47",
     "quote": "`AUDIO_STATUS.md` falsely claims all of Unit 4 is done — only 3 of 9 are"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md",
     "lines": "15",
     "quote": "Any G5 gate report claiming format compliance based only on these artifacts would be dishonest."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    61,
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An item format that usually needs the text does not guarantee it; check every item for text dependence on its own.",
   "kind": "measured",
   "found_by": "353 items held back as format-safe were blind-solved by two independent solver families and 334 leaked (94.6%); a calibration on another grade found as-written items solvable without the passage regardless of format.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md",
     "lines": "19",
     "quote": "**Verdict: the 353 are overwhelmingly leaky.** Only **19 items** genuinely require the passage under a"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md",
     "lines": "21",
     "quote": "anti-leak FORMAT ≠ low leak"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g3-control-set-2026-07-10/G3-CALIBRATION-REPORT.md",
     "lines": "49",
     "quote": "Construction, not format or grade, is the lever."
    }
   ],
   "against": "Format still shifts the odds: in another pool \"| hot-text | 1,479 | ~17.5% | ~1,220 |\" against 99.5% for multiple choice (LANE1_COURSE.md line 136).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Accept an item only when a solver from a different model family than the writer answers it correctly with the text and cannot recover the answer without it; each test rejects items the other passes.",
   "kind": "measured",
   "found_by": "In a generation run 417 of 1,152 items failed the with-text control (ambiguous keys) while 186 of 299 control-passing items still leaked without the text; with-text success did not predict text dependence.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "11",
     "quote": "They were accepted only when a different model family could answer them with the passage and could not recover the keyed"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "182",
     "quote": "Control-pass rate did not predict certification."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "222",
     "quote": "That second condition matters. It prevented \"anti-leak but broken\" items from entering the final set."
    }
   ],
   "against": "How strict the without-text bar is matters: \"Both bars were designed to avoid frontier-model-proofing a Grade 5 assessment\" (QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md line 304).",
   "adds_to_existing": [
    5,
    6,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Run the without-text check with more than one solver family other than the writer's, count an item clean only if all fail, and verify that a claimed independent check really used a different family.",
   "kind": "measured",
   "found_by": "When one family errored, 24 items looked clean on the other family alone; firming both families left 19. Separately, 191 items had been certified on a same-family lane while documents claimed otherwise, and a self-check-only pass was named the one unmitigated risk.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md",
     "lines": "53",
     "quote": "9 of which rested on gpt-4.1 alone; the real two-family number is **19**."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
     "lines": "184",
     "quote": "Same-family 'cross-family' claims"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "204",
     "quote": "Same-family generation bias (Claude generates + Claude blind-solves) is the one unmitigated risk"
    }
   ],
   "against": "One independent family is accepted as a named gap rather than a failure: \"A second working non-generator family would harden the leak claim\" (g5-merged-course/VERDICT_TEMPLATE.md line 77).",
   "adds_to_existing": [
    66,
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count a without-text recovery as a leak only when a typical student at the target level could reproduce it, not merely a strong model.",
   "kind": "adopted rule",
   "found_by": "Calibration showed the strong solver out-reads the child; a level-conditioned bar removed low-confidence forced guesses (43 to 39 recoveries out of 45) while still separating good constructions from bad.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g3-control-set-2026-07-10/G3-CALIBRATION-REPORT.md",
     "lines": "62",
     "quote": "recovery counts as leak only when a typical THIRD grader could plausibly reproduce it"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-claude/run/SOLVER_V2.md",
     "lines": "14",
     "quote": "The bar is a savvy student, not an expert."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "304",
     "quote": "explicitly asks whether a real fifth grader could reproduce the blind recovery"
    }
   ],
   "against": "An earlier protocol counted any model recovery: \"**Threshold:** 2/3 correct recoveries = LEAKED.\" (LANE3_LLM.md line 270).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-run text-dependence checks when stronger solvers arrive; an earlier pass does not stay valid.",
   "kind": "measured",
   "found_by": "An item an older solver could not answer without the text (0 of 3) was answered 3 of 3 by a newer one and decertified; a calibration noted the live course moves and must be re-pulled before re-measuring.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
     "lines": "22",
     "quote": "Current Gemini 3.5 is 3/3 in both conditions, so the item is directly gameable"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g3-control-set-2026-07-10/G3-CALIBRATION-REPORT.md",
     "lines": "84",
     "quote": "- The live course moves — this distribution is dated 2026-07-10; re-pull before re-measuring."
    }
   ],
   "against": "A stronger solver is not a student: \"out-reads the child; near-chance forced guesses are not leaks\" (G3-CALIBRATION-REPORT.md line 57).",
   "adds_to_existing": [
    42
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A text built from facts most readers already know lets its questions be answered without it; when the text is the evidence being assessed, build it around particular events, decisions, arguments or surprising claims that only that text supplies.",
   "kind": "measured",
   "found_by": "Blind-solving thousands of generated items traced near-total multiple-choice leakage (99.5%) to passages restating well-documented school facts; later runs saw items leak through ordinary school knowledge.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "21",
     "quote": "**Root cause: passages describe well-documented curriculum facts.**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "29",
     "quote": "The generator asks \"what does the passage say about X?\" — but X is something any educated reader already knows from school."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "269",
     "quote": "- MCQ leaked through ordinary school knowledge, such as Gutenberg, scurvy/citrus, or vocabulary clues."
    }
   ],
   "against": "Learning texts should let taught knowledge help; an external review faulted a design that kept knowledge from paying off: \"It cites Hirsch and Willingham and then forbids knowledge from helping.\" (g5_build_2026_07_02/feedback_clean.md line 43).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A gate that rejects every question answerable without the text also rejects every question about knowledge the unit taught, so measure knowledge gains separately, for example by comparing students' explanations of the unit's concept before and after.",
   "kind": "measured",
   "found_by": "The knowledge-recall share of a certified bank fell to about zero by design once text-dependence filtering ran, after being underweighted at 12.4% beforehand, leaving knowledge growth unmeasured by the item bank.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/VERDICT_TEMPLATE.md",
     "lines": "70",
     "quote": "2. **KCT1 Domain-knowledge ≈ 0 — by design.** Domain-recall items are passage-independent → removed"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "198",
     "quote": "| KCT1 Domain Knowledge | 67 | 12.4% | Underweighted; RI.5.x informational heavy |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/04-evidence-contract.md",
     "lines": "11",
     "quote": "> Improvement from pre-unit to post-unit student explanation of the unit concept."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Sequence learning texts so taught knowledge recurs and pays off, and keep cold, unrelated texts for tests and diagnostics only.",
   "kind": "adopted rule",
   "found_by": "An external review judged a course a practice engine rather than a curriculum because it kept assessment passages from overlapping taught topics; a second round found passages jumping between unrelated topics with nothing revisited.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "45",
     "quote": "Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "25",
     "quote": "The passages jumped from e.g. the axolotl to shadows with no visible link, there is no pre-teaching of key ideas, and no strategy is revisited at greater depth."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/03-transfer-practice-layer.md",
     "lines": "59",
     "quote": "- do not use cold passages as the main teaching surface;"
    }
   ],
   "against": "When the target test mixes unrelated texts, topic coherence has to fade before it: \"is the last scaffold, and like every other scaffold it fades gradually\" (g5_build_2026_07_02/approval_clean.md line 296).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose a unit's texts before writing any questions and give each one a stated knowledge role; if a text could be swapped out without changing the unit, the sequence is not building knowledge.",
   "kind": "adopted rule",
   "found_by": "After skill-practice courses were rejected in review, the course plan required a concept arc and a planned text sequence, naming interchangeable texts as a failure sign.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/01-course-graph.md",
     "lines": "63",
     "quote": "A planned set of texts selected before questions are written."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/01-course-graph.md",
     "lines": "75",
     "quote": "Bad sign: any text can be swapped out without changing the unit."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "53",
     "quote": "Choose texts for a coherent knowledge sequence and a genre balance that includes poetry, drama and more literary work, and judge complexity qualitatively as well as by Lexile."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Record the knowledge each text assumes and adds, tying each addition to the sentence that carries it, and open each lesson with a question that needs the specific knowledge the previous lesson built.",
   "kind": "adopted rule",
   "found_by": "A demonstration unit listed per-text assumed and added knowledge with carrying sentences; a simulated review credited a sequence whose openers each tested the prior lesson's specific knowledge as genuine compounding.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md",
     "lines": "8",
     "quote": "Proposed adds / assumes per text, with carrying spans."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "35",
     "quote": "restates and tests the prior lesson's narrative state, always using a question that requires the"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/01-course-graph.md",
     "lines": "87",
     "quote": "- What later text depends on this beat?"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record and confirm what each lesson assumes from earlier grades, and measure how many lessons actually draw on that prior knowledge.",
   "kind": "measured",
   "found_by": "A 55-lesson course had no confirmed link to earlier grades' knowledge; the share of lessons citing the prior grade fell from 57% between two lower grades to 13% between the next two.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/GAP-ANALYSIS-2026-08-18.md",
     "lines": "51",
     "quote": "There is no G3→G5 or G4→G5 transfer arc encoded anywhere in the canon."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/CURRICULUM-REVIEW-STANDING-2026-08-17.md",
     "lines": "66",
     "quote": "G3→G4: 9 arcs, 28/49 lessons (57%) citing G3 content."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/CURRICULUM-REVIEW-STANDING-2026-08-17.md",
     "lines": "67",
     "quote": "G4→G5: 7 arcs, 7/55 lessons (13%) citing G4 content — a real 7x drop in citation density."
    }
   ],
   "against": "The drop was a disclosed choice: \"as a deliberate design choice (G5's canon was authored\" (g5-course/CURRICULUM-REVIEW-STANDING-2026-08-17.md line 70).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Go deep on a topic with a set of texts, and return to it in later grades only with new, more sophisticated knowledge; a unit repeating angles an earlier grade already covered is redundant.",
   "kind": "external research",
   "found_by": "A curriculum directory (https://knowledgematters.org/curriculum-directory/) describes knowledge-building curricula as deep text sets that spiral back with more sophistication; a proposed unit was declined because an earlier grade already covered its angles and a similar repeated unit had been retired.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/13-candidate-themes-and-selection-rubric.md",
     "lines": "5",
     "quote": "spiraling back to topic areas with more sophistication."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/13-candidate-themes-and-selection-rubric.md",
     "lines": "7",
     "quote": "Source: https://knowledgematters.org/curriculum-directory/"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/HUMAN-BODY-III-DECISION.md",
     "lines": "10",
     "quote": "exact mistake for which G4's Human Body II was retired, and the G4 crosswalk already"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Readability formulas miss knowledge load and hide variation inside a book; measure the exact excerpt used and judge complexity qualitatively too.",
   "kind": "measured",
   "found_by": "A text that measured easier by formula (grade 2.7 vs 3.5) carried more new ideas; one book's chapters ranged from grade 4.84 to 7.91; a review noted a single difficulty number mishandles poetry and narrative.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "18",
     "quote": "measures lexically simpler than the primer (FK 3.5) because its sentences are short; its"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "20",
     "quote": "denser stated/implied layering, which the FK heuristic does not see."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/pd-texts/winnie-the-pooh-onepager.md",
     "lines": "28",
     "quote": "Chapter range FK 4.84 (ch VI) to"
    }
   ],
   "against": "Measures disagree, and a documented level was preferred over the formula: \"documented 790L remains the better band evidence\" (g5-course/pd-texts/winnie-the-pooh-onepager.md line 27).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Pin the exact edition or translation of a source text, since its reading level and rights status can differ by edition.",
   "kind": "adopted rule",
   "found_by": "Text research found one translation of a book far below the reading level of other translations, and that only original editions of some series were in the public domain.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/PD-FICTION-RESEARCH-2026-08-19.md",
     "lines": "25",
     "quote": "pin the Stork 1915 translation specifically (others run 1200L)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/PD-FICTION-RESEARCH-2026-08-19.md",
     "lines": "13",
     "quote": "only the ORIGINAL edition text is PD — the revised editions everyone knows are still"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A word taught in depth must recur — more than once in its own text and again later in the unit — and words picked because they look hard mostly fail that test.",
   "kind": "measured",
   "found_by": "A recurrence rule was written after seven of nine taught words appeared exactly once while every other check passed; source-chosen hard words failed it (0 of 4 in one lesson); a simulated review found each taught word met only 4–5 times, short of a ~6 standard.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "69",
     "quote": "unit, counted by word family (R-VOC-7/13 — written after seven of nine taught words turned out"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/VOCAB-DECISIONS-U1.md",
     "lines": "19",
     "quote": "| U1L1 | atmosphere, hydrosphere, geosphere, biosphere | **0 of 4** — each appears once |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "87",
     "quote": "Across the arc, each target word gets approximately 4–5 exposures, not 6+, and drops out after"
    }
   ],
   "against": "Some designs withhold the word from the text on purpose: \"**Adversarial refutation attempt:** The words are encapsulating words by design (vocabulary\" (arc-audit/SIM-REVIEW-D7-D8-D10-D12.md line 91).",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give each taught word one definition across the whole course, and define its real meaning; a student who gives the true meaning must not fail.",
   "kind": "measured",
   "found_by": "A word card defined a common word by the lesson's own distinction, so a student giving the dictionary meaning failed the rubric; one source defined a key term three different ways across lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "217",
     "quote": "subject and verb\" fails the rubric for being right. If the card must exist, define"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/VOCAB-DECISIONS-U1.md",
     "lines": "31",
     "quote": "the canon defines `evidence` three different ways"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "186",
     "quote": "A2 one verbatim definition per concept"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make sure no wrong option can be ruled out by surface cues — absolute words, the key being the longest or shortest option, two options that contradict each other, or one option sounding more textbook-correct.",
   "kind": "measured",
   "found_by": "Without the passage a solver recovered 62.7% of generated multiple-choice keys; leaked items showed absolute-word tells, longest-is-correct keys (512 items over a 20% length margin), paired contradictions and textbook-sounding keys.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "60",
     "quote": "1. **Absolute language tells** — wrong options use \"always\"/\"never\"/\"all\"/\"completely\" → flagged"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "61",
     "quote": "2. **Longest-option wins** — correct answer systematically longest (>20% margin)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "270",
     "quote": "- MCQ also leaked when one option was the obvious balanced or textbook-sounding answer."
    }
   ],
   "against": "The length rule does not apply where length reveals nothing: \"does not transfer to match extras. No action.\" (g5-course/ADVERSARIAL-REVIEW-2026-09-04-R16.md line 52); surface fixes alone left most items leaking (LANE1_COURSE.md line 167).",
   "adds_to_existing": [
    6,
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fix systematic leakage at its source — the text or the item format — rather than by patching options or regenerating more of the same.",
   "kind": "measured",
   "found_by": "Regeneration with option fixes cut multiple-choice leakage only from 99.5% to 90.0%; option-length patches were judged unable to fix it, and redesigning the test plan around other formats removed the need to regenerate.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "167",
     "quote": "Regen pilot (Wave 3) showed 9.5pt improvement in MCQ leak (99.5% → 90.0%) but leak remained"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "31",
     "quote": "**Fix verdict:** NOT fixable with option-length patches. Requires passage strategy redesign."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "152",
     "quote": "- Skeleton redesign (V2) resolves the regen problem by eliminating MCQ/MSQ from the build and substituting passage-dependent formats with sufficient pool depth."
    }
   ],
   "against": "A format change alone is not enough either: \"anti-leak FORMAT ≠ low leak\" (g5-merged-course/a2-cross-family-regate.md line 21).",
   "adds_to_existing": [
    65
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A skill that is itself word knowledge (word parts, synonyms, connotation) cannot be tested by questions that need the text; decide separately how to assess it.",
   "kind": "measured",
   "found_by": "Of 45 generated vocabulary items, 36 were answered without the passage; word-part, synonym and connotation items leaked 100%, so those slots needed a different design or removal from the text-dependent plan; a later bank of 120 such items leaked 99.2%.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "242",
     "quote": "Skill IS word-part knowledge, not passage inference — cannot be made passage-dependent."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "246",
     "quote": "cannot be tested as passage-dependent items and should be excluded from the comprehension-course blueprint"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md",
     "lines": "41",
     "quote": "the 120 L.5 vocab seeds LEAK 99.2% and must be re-authored + re-certified, never deployed as-is"
    }
   ],
   "against": "Context-clue items partly worked: \"**Best-performing.** 8 survivors: technical/domain-specific words\" (LANE1_COURSE.md line 240).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In context-clue word questions, use words in senses the reader can't already know; words used in their everyday meaning get answered without the text.",
   "kind": "measured",
   "found_by": "In context-clue items the 8 survivors used technical or domain-specific senses while the 7 that leaked used dominant everyday meanings.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "240",
     "quote": "8 survivors: technical/domain-specific words (normal, base, draws, channels, reservations, niche, range, intrusive). 7 leaked: dominant-meaning words"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE3_LLM.md",
     "lines": "244",
     "quote": "a word's meaning must be derivable only from the passage, not from world knowledge"
    }
   ],
   "against": "Small sample: \"| L.5.4a (context clues) | 15 | 7 | **8** | 47% |\" (LANE1_COURSE.md line 240).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An ordering task leaks when its steps follow common logic or a familiar story or process order; use steps whose order only the text settles.",
   "kind": "measured",
   "found_by": "Ordering items survived blind-solving best among non-matching formats but failed whenever fragments had a natural order (problem to solution to result, cause to effect); ordering items built on world-knowledge sequences leaked about 55%.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "278",
     "quote": "Sequence worked better than the other non-match formats, but it failed whenever the fragments had a natural order:"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "285",
     "quote": "The surviving sequence items need neutral, non-orderable details whose order depends on passage location, not common logic."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "50",
     "quote": "| sequence | 100% | ~45% (world-knowledge seqs) | Some steps deducible without passage |"
    }
   ],
   "against": "Order-by-location items can turn mechanical: \"Anti-leak success is not enough.\" (QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md line 89).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In select-from-the-text items, include at least two competing spans of the same shape and a question that cannot be resolved without the text; wording that signposts the right spans gives them away.",
   "kind": "measured",
   "found_by": "Gap-fill generation found select-from-text items survived only with two or more same-shaped competitors and an unresolvable question referent; signposted questions and spans leaked.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "66",
     "quote": "- hot-text survives only with >=2 same-shaped competitor spans AND a stem referent"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "69",
     "quote": "Arc-schema stems, paraphrase-matchable stems, and self-evident-cost spans all leaked."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "272",
     "quote": "- Hot-text leaked when the question or span wording signposted the correct phrases."
    }
   ],
   "against": "The format often works because the answer sits in the text: \"these items work because the answer is literally IN the passage text\" (LANE2_GENERATOR.md line 37).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Key questions to details only the text holds — who did it, in what order, which source said it — or make the commonsense answer a wrong option; a key that matches the likeliest guess from the story's general shape leaks.",
   "kind": "measured",
   "found_by": "8 of 11 cause questions leaked because their key was the solver's most likely narrative guess; survivors hid the key behind text-internal details or made the world-favourite answer a decoy.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "62",
     "quote": "key is the blind solver's plurality narrative guess dies (8/11 cause leaks, incl."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "64",
     "quote": "referents (event order, actor identity, note provenance) or anti-schema keys where"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "202",
     "quote": "every correct answer depends on a passage-specific invented detail that cannot be retrieved from prior knowledge"
    }
   ],
   "against": "The 100% pass for invented-detail items was a same-family self-check: \"Same-family generation bias (Claude generates + Claude blind-solves) is the one unmitigated risk\" (LANE2_GENERATOR.md line 204).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Name sorting categories neutrally (for example Source A, Source B, Both); titles or topic words used as category labels give the answer away.",
   "kind": "measured",
   "found_by": "A source-attribution sorting construction with neutral labels produced 700 certified items; titles used as categories were recorded as a leak path.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "16",
     "quote": "- Passage titles were never used as category labels."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "315",
     "quote": "- Passage titles as categories: titles leak."
    }
   ],
   "against": "Neutral labels left keys ambiguous where a 'both' category was loosely keyed: \"The control failures were usually partial matches, often 4/5 or 5/6 statements correct.\" (QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md line 132).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In two-part answer-plus-evidence items, make sure neither part gives away the other.",
   "kind": "measured",
   "found_by": "Two-part answer-plus-evidence items leaked 94% in a generated bank, and the elaborate-option version was recorded as able to self-solve.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "314",
     "quote": "- Sophisticated-option EBSR: Part A/Part B can self-solve."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "41",
     "quote": "| EBSR (corpus) | 1,475 | 94% | 89 |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Use only item types suited to the learners' level and the target test's blueprint, not every format available.",
   "kind": "adopted rule",
   "found_by": "External reviewers judged a two-part evidence type added for format variety developmentally inappropriate for the grade; it was later ruled off-construct, yet every lesson of one package still contained it.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "56",
     "quote": "the added two-part (Part A / Part B) evidence items are likely developmentally inappropriate for grade 3 — that type generally appears on state tests around grade 4 and above."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
     "lines": "135",
     "quote": "Current: ruled off-construct (~grade-4+), 56 items declared"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/edullm-agent-entrypoint-g3-practical-test-2026-08-06/REPORT.qmd",
     "lines": "36",
     "quote": "- 48/48 lessons include banned G3 EBSR items."
    }
   ],
   "against": "An earlier design required \"every MAP format practiced\" from the start (g5_build_2026_07_02/approval_clean.md line 290).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Fact-check every student-facing string — model answers, feedback, hints, definitions and marking guides — against the source, not only the text and the key.",
   "kind": "measured",
   "found_by": "A source-fidelity review found an invented causal chain in a model answer and in corrective feedback, and a marking guide that failed the correct pairings while passing wrong ones; an external check found five feedback lines contradicting the story.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R3.md",
     "lines": "31",
     "quote": "that light-blocking leads to low oxygen. Canon never states that mechanism."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R3.md",
     "lines": "88",
     "quote": "criterion; a child stating the authored wrong pairs passes. The node's own grounding"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "120",
     "quote": "Five feedback/reveal lines contradict the story"
    }
   ],
   "against": "A true but unsupported addition was rated lower harm: \"Not CRITICAL: the claim is factually true of real\" (g5-course/ADVERSARIAL-REVIEW-2026-08-20-R4.md line 56).",
   "adds_to_existing": [
    59,
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep every claim within what the source supports: don't turn one case's outcome into a general truth, and don't present a planned level or an estimate as a measured one.",
   "kind": "adopted rule",
   "found_by": "Corrective feedback half-conceded a distractor's universal claim and was rewritten; plans carried an explicit disclaimer that a reading-level target was not a measurement; a factual-claims protocol treated any wrong world claim as fatal to a text.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R3.md",
     "lines": "47",
     "quote": "since restoration always works\" — the feedback half-concedes the distractor's premise."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R18.md",
     "lines": "129",
     "quote": "900L is a provisional planning target, not a measured score or approved readability level."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "22",
     "quote": "child's science text is a kill, not a footnote."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never refer students to a label, code, control, highlight or line they can't see on the current screen.",
   "kind": "measured",
   "found_by": "Reviews found a question citing a source label that no page showed, help hints on about 28 word cards pointing to text not yet on screen, and nine hints telling students to reread a highlight that never appeared.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "18",
     "quote": "passage, booktag, or heading in this lesson ever names a \"Source C\". It is leaked"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "62",
     "quote": "has not met and cannot see.** Vocab pages come before any passage and render in"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "110",
     "quote": "is ever highlighted.** `grounding` is scorer-only (verified: `SpeakGate`/`ScrItem`"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make each rung of a hint ladder add information and lead toward what the marking requires; a first hint that restates the task adds nothing, and a hint pointing elsewhere fails the student who follows it.",
   "kind": "measured",
   "found_by": "The first hint on all 28 word cards repeated the failed task; a later fix pointed a second hint at an unrelated fact, so a student following it would fail; the course gate then required a second hint that is not the first reworded.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "117",
     "quote": "a restatement of the say_back task the child just failed. Rung 1 adds zero"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-20-R7.md",
     "lines": "119",
     "quote": "correctly from the hint given (\"light\") will say something about light, not about a home or"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "54",
     "quote": "first reworded, and a `reveal` — three scored turns, escalating, ending in the one line allowed"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make sure an answer revealed, hinted or prompted for one task does not hand over the answer to a later task in the same lesson.",
   "kind": "measured",
   "found_by": "A spoken task's reveal was near word-for-word the model answer for the next writing task; another prompt stated both required clues before the student answered; wrong-answer feedback named the key, making the retry free.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "84",
     "quote": "pattern in U9-L3 and U1-L6. A child who exhausts the speak's 3 tries is handed the"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "130",
     "quote": "The extra-thinking prompt states both rubric-required clues outright before the student answers"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md",
     "lines": "12",
     "quote": "which names the right answer (flying) so the second try is free."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3,
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep teaching examples and the independent check of the same idea on different screens, and don't let an answer option repeat five or more words of teaching text that is on screen.",
   "kind": "adopted rule",
   "found_by": "A first-pass audit finding led to the rule; a later review found teaching articles pre-answering their own certified release checks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "86",
     "quote": "The teaching display (example/nonexample) and the independent check may not share a screen"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "301",
     "quote": "word overlap between an option and same-screen teaching text = fail)."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
     "lines": "27",
     "quote": "Gradual-release leak: l0/l1 teaching articles pre-answered their certified release checks (must-fix)"
    }
   ],
   "against": "Approved reference lessons check a just-taught idea on the same page: \"Teaching-then-checking on one page is the pattern, not a leak.\" (g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md line 35).",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Put no answer text on a picture or diagram, and make sure neither the picture alone nor the prose alone lets a student pass every check.",
   "kind": "adopted rule",
   "found_by": "A first-pass diagram printed the rule and role labels, which let a student pass every check without reading the passage.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "254",
     "quote": "- **The artifact is neutral: no answer text on it.** This is the F1 lesson from the U4L2 build —"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "256",
     "quote": "let a student pass every check without reading the passage, defeating the lesson's entire"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "269",
     "quote": "check from the artifact alone, or from the prose alone? If either answer is yes, the lesson is"
    }
   ],
   "against": "Labels naming what an element is may stay: 'names what an element IS — e.g. \"habitat, not food\" — is contractual and stays' (g5-course/LESSON-AUTHORING-PLAYBOOK.md line 259).",
   "adds_to_existing": [
    64,
    21,
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make modelling, guided practice and independent practice all practise the same process under the same step names; the model must not just reveal the answer, the guided step must not just hint, and the independent step must not switch skills.",
   "kind": "adopted rule",
   "found_by": "External reviewers found the model only revealed the answer, guided practice only hinted and independent work switched to a different skill; a later simulated review found an independent step dropping two of the four steps its guided step used.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "14",
     "quote": "the \"I do\" only reveals the answer instead of modelling the thought process; the \"we do\" only offers a hint; the \"you do\" switches to a different skill (supporting details)."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D1-D4.md",
     "lines": "29",
     "quote": "- **Criterion:** D1.6 (Triple-presence: model/guide/release share an identical ordered step list),"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "94",
     "quote": "Never rename a step mid-lesson. The names must survive the strip-the-labels test (they describe"
    }
   ],
   "against": "Keeping the same question from model to guided step was accepted as the house pattern: \"The I-do→we-do handoff keeping the same question is the house release pattern; the\" (g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md line 24).",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Show the tempting wrong choice and why it is rejected inside a worked example, and build worked examples only from steps already taught; teach a new step before it appears in one.",
   "kind": "adopted rule",
   "found_by": "The lesson template made the rejected alternative part of every model; a practice principle held that worked examples assemble known steps; a review singled out a model rejecting outside knowledge as the best in the course.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "83",
     "quote": "think-aloud prose that **includes the explicitly rejected alternative** from `decision_point`"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "54",
     "quote": "Worked examples assemble the known — a novel step must be taught before it appears inside one."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "179",
     "quote": "water is not evidence from this text\") is exactly the epistemic move the unit"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a skill returns in a later lesson, raise the demand — go deeper or combine it with earlier skills; re-teaching it word for word at the same depth adds nothing.",
   "kind": "adopted rule",
   "found_by": "A simulated review found two consecutive lessons with word-for-word identical skill introductions and no combined task; earlier external review had criticised that no strategy was revisited at greater depth.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "115",
     "quote": "Evidence: L6 p12 and L7 p12 contain verbatim-identical skill-intro text:"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "140",
     "quote": "skill identically, not cumulatively. The deeper coordination (e.g., \"find the evidence, then"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/G5-CURRICULUM-OUTLINE.md",
     "lines": "44",
     "quote": "(29 lessons), then at `deepen` phase in a new knowledge domain (26 lessons — the canon's"
    }
   ],
   "against": "Repetition was defended as practice: \"**Adversarial refutation attempt:** This is by design — the FIND skill is practiced in two\" (arc-audit/SIM-REVIEW-D7-D8-D10-D12.md line 129).",
   "adds_to_existing": [
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Frame a multi-lesson set of texts with one visible purpose question from the start, and give each lesson's reading purpose before pre-teaching its words.",
   "kind": "adopted rule",
   "found_by": "A simulated review against a 285-criterion standard flagged a missing overarching purpose question and reading-purpose pages placed after vocabulary teaching in three lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "153",
     "quote": "Dimension criterion: a visible overarching purpose-question frames a multi-lesson text set from"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "495",
     "quote": "Reading-goal page comes AFTER vocabulary instruction in L5–L7 (vocab gates orientation)"
    }
   ],
   "against": "The missing overarching question was rated a note: \"**Why it is a NOTE, not a finding:** The canopy deficiency is real at the arc-text level (four\" (arc-audit/SIM-REVIEW-D7-D8-D10-D12.md line 170).",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the text on screen whenever a task asks for evidence from it, and make sure the part shown is the part that holds the evidence.",
   "kind": "adopted rule",
   "found_by": "External reviewers found evidence prompts with the passage hidden; a walkthrough found transfer items shown beside the wrong text, with the marker given that text, and a pinned excerpt holding only wrong answers.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "45",
     "quote": "Prompts ask students to cite text evidence, but the passage is hidden at that point (\"try looking back at the text\" — but the text is gone)."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "76",
     "quote": "WRONG pinned passage, and the open-response scorer is handed that wrong text.**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "124",
     "quote": "the pin shows only wrong"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    30
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check in the delivered lesson that each required response is actually required and that its gates block a real miss.",
   "kind": "measured",
   "found_by": "A browser walked an 18-scene lesson to its congratulatory ending without one answer; mastery was earned at about 20% accuracy by clicking through; later a task was passed while answering every question wrongly.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/edullm-agent-entrypoint-g3-practical-test-2026-08-06/REPORT.qmd",
     "lines": "42",
     "quote": "- A browser completed U1·L3's 18 scenes with zero answers and reached the congratulatory ending."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "95",
     "quote": "at about 20 percent accuracy by clicking through without reading, then advanced with the passage hidden from view."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "61",
     "quote": "in a main-idea task we earned the pass while answering every question incorrectly."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28,
    46,
    47
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count a fix only once it is verified in the product as actually served; status reports, clean source pools and stale builds can all differ from what students get.",
   "kind": "measured",
   "found_by": "External reviewers found most items reported done and live unresolved in the app; one verification ran against a build older than the edited file; a certified pool was clean while live tests still exposed leaky items in 60 of 81 forms.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "3",
     "quote": "most of the items reported as \"done & live\" are not yet resolved in the app"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/build-closing-questions-2026-09-25/verify/DIGEST.md",
     "lines": "42",
     "quote": "every verdict in this digest is against the 11:41 build"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/leaky-vs-gate-unreachability.md",
     "lines": "86",
     "quote": "Pool-purity and gate-purity are separate properties; only the former is satisfied"
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
   "statement": "Probe how the live system actually scores each item shape, and compute guessing floors per item from that, not from the format label.",
   "kind": "measured",
   "found_by": "A live probe found two-answer selection items paid full credit when the first pick was correct, raising their guessing floor about tenfold (≈0.167 vs ≈0.015).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/scoring-rule-probe-2026-07-10/scoring-rule-probe.md",
     "lines": "60",
     "quote": "submitted array to its **first element** and pays full credit if that single token matches"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/scoring-rule-probe-2026-07-10/scoring-rule-probe.md",
     "lines": "70",
     "quote": "is **k/n_tokens** (e.g. 2 of 12 → ≈ 0.167), not 1/C(n,k) (≈ 0.015) — an order of magnitude"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g3-control-set-2026-07-10/G3-CALIBRATION-REPORT.md",
     "lines": "77",
     "quote": "Standing rule: chance floors are computed per item from its responseDeclaration, never from the"
    }
   ],
   "against": "The probe warns against over-generalising: \"not generalize beyond the probed endpoint and item shapes.\" (scoring-rule-probe-2026-07-10/scoring-rule-probe.md line 8).",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check ordering and selection items without the text under many shuffles, and set the leak threshold well above each item's guessing floor; one shuffle is not enough.",
   "kind": "measured",
   "found_by": "Ordering items certified against one seeded shuffle were re-probed under many shuffles and 72 were decertified; a calibration then set eight or more shuffles and a threshold at least 0.20 above the floor.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
     "lines": "180",
     "quote": "items certified against one seeded shuffle; multi-shuffle re-probe decertified 72 incl. one"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g3-control-set-2026-07-10/G3-CALIBRATION-REPORT.md",
     "lines": "63",
     "quote": "scored on >=8 shuffles for order/selection formats, with per-format chance floors as computed in"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    35
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a checker error or a missing result as no verdict, and make a broken checker fail loudly rather than report content passes or failures.",
   "kind": "measured",
   "found_by": "A solver hit its output limit on 82 long items — a transport limit, not an item signal — and was re-run; a walker run against a keyless marker produced 11 phantom failures; certification required a full valid set of without-text attempts.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md",
     "lines": "50",
     "quote": "a transport limit, not item signal."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "101",
     "quote": "— a broken harness must fail loud, never leak into the walk as phantom content failures"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "50",
     "quote": "leaky never re-rolled, certification requires a FULL valid blind set)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9,
    36
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make sure every field students see or hear is read by at least one check; unread fields let silent clips, stale audio and hint leaks through a passing build.",
   "kind": "measured",
   "found_by": "Lesson-page clips were never checked and three played as silence behind a green build; review clips with no text hash went stale after a definition edit; an audit script never read the fields that held a hint leak.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/DECISIONS-2026-08-24.md",
     "lines": "39",
     "quote": "clips were never checked for existence — three played as silence"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/l4-p3-stale-clip-2026-09-29/README.md",
     "lines": "14",
     "quote": "Class gap: frame `rows[].audio_path` review clips have no `audio_of`, so a definition edit leaves the clip silently stale."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "139",
     "quote": "The audit script (audit.py) never reads think_aloud.states[].search / we_do.search fields at all"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-review after every change — including fixes and changes to the code that displays unchanged content — because each new surface can bring new critical faults.",
   "kind": "measured",
   "found_by": "After content reviews converged with zero critical faults, a port of display code introduced two; a fix in one field broke another field; reworded item variants inherited certification without being re-checked.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-21-R8.md",
     "lines": "10",
     "quote": "*content* surface; this round exists because 8 new engine commits landed after R7's base."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-21-R9.md",
     "lines": "6",
     "quote": "the loop's rule is that a fix commit gets fresh eyes before the loop may claim convergence."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-20-R7.md",
     "lines": "133",
     "quote": "is exactly the defect class this round was asked to hunt: a fix that solved its target problem"
    }
   ],
   "against": "Re-review is scoped to what changed (g5-course/ADVERSARIAL-REVIEW-2026-08-20-R6.md line 10: runs twice on unchanged content\" confines it to the four commits above.).",
   "adds_to_existing": [
    42
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Run review rounds through changing lenses — a student walk answering everything right and everything wrong twice, source fidelity, an outside expert's first read, consistency with a shipped course — since each new lens found critical faults the earlier ones missed.",
   "kind": "measured",
   "found_by": "Successive rounds on the same nine lessons with new lenses found 5, 5, 5, 1 and 1 critical faults before a round found none.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "4",
     "quote": "(a) gets everything right, (b) gets every gated item wrong twice before recovering."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R3.md",
     "lines": "19",
     "quote": "Totals: **5 CRITICAL / 2 WORTH-FIXING / 1 POLISH.**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-20-R4.md",
     "lines": "178",
     "quote": "| CRITICAL | 1 (U1-L6 item-4-evidence self-negating keyed answer) |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    47,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When content or display code is shared or ported between courses or levels, compare conventions one by one and check what the shared code assumes; silent departures and level-specific wording slip through.",
   "kind": "measured",
   "found_by": "One level silently dropped a say-the-word step on 28 of 28 cards that the shipped level used on 12 of 12; a shared marking prompt hard-coded a younger grade; ported display code assumed a field the new course never had and degraded silently.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-20-R5.md",
     "lines": "45",
     "quote": "established on every card, course-wide (28/28 G5 cards vs 12/12 G4 cards).**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-15-R22.md",
     "lines": "34",
     "quote": "#503 fragment rule (`oneWordRule`): **hardcodes \"a sentence a third grader could say"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-21-R8.md",
     "lines": "35",
     "quote": "(`station`) that G5 never authored, and the fallback silently produces a worse UI than what it"
    }
   ],
   "against": "Differences licensed by content are not defects: \"licensed by different canon, different genre (continuous Odyssey narrative vs. four\" (g5-course/ADVERSARIAL-REVIEW-2026-08-20-R5.md line 11).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make the marker's rules agree with what the question asks; a rule rejecting short fragments failed students who quoted a short phrase exactly as told.",
   "kind": "measured",
   "found_by": "A fragment rule gave no credit to the short phrase a question explicitly asked for; a rubric edit dropping a phrase the marker keyed on would have refused one-word answers; one blank carried two acceptance rules that disagreed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-16-R25.md",
     "lines": "48",
     "quote": "So a Grade-5 child who does exactly what the stem asks, \"Quote a short"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "152",
     "quote": "the speak-score route's fragment gate keys on it, so a one-word answer would have been refused"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "117",
     "quote": "The blank's own acceptance rules disagree"
    }
   ],
   "against": "The harm was bounded: \"Not CRITICAL because the child who then\" (g5-course/ADVERSARIAL-REVIEW-2026-09-16-R25.md line 53).",
   "adds_to_existing": [
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When checking for copying, compare a student's words only with text the student was shown; counting the marking guide's own wording rejected word-perfect recall.",
   "kind": "measured",
   "found_by": "An anti-copying check counted marking criteria as copy sources; on three recall pages whose criterion contained the target sentence (overlap 0.74 above a 0.70 threshold) exact recall was rejected and the student was told the words were on the page when they were hidden.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/build-closing-questions-2026-09-25/verify/DIGEST.md",
     "lines": "23",
     "quote": "contains the sentence at 84/114 = 0.74, threshold 0.70"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/build-closing-questions-2026-09-25/verify/DIGEST.md",
     "lines": "29",
     "quote": "is false to the child because the sentence is hidden on p0b."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-16-R26.md",
     "lines": "18",
     "quote": "a criterion states the standard, it does not quote the"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    30,
    56
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give an identical answer the same mark every time; judging a resubmission afresh gave one answer 'Almost' and then full credit.",
   "kind": "measured",
   "found_by": "The same typed word received two different verdicts on resubmission; the fix ran the first judgment at the most deterministic setting and returned the stored verdict for identical resubmissions.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/baseline-submission/CHANGES-FOR-REVIEW-L4-2026-08-31.md",
     "lines": "33",
     "quote": "An identical typed answer now always returns the same verdict"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/baseline-submission/CHANGES-FOR-REVIEW-L4-2026-08-31.md",
     "lines": "107",
     "quote": "an identical resubmitted answer now returns the same verdict instantly instead of a fresh judgment"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Once the answer has been shown after failed tries, show no praise; the screen must not say 'Yes' to a student who was just given the answer.",
   "kind": "measured",
   "found_by": "After item components were rewritten, every multi-select item in the course printed authored praise lines beside the shown answer; a later marking rule held that running out of tries is not passing.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-27-R12.md",
     "lines": "39",
     "quote": "child who just failed to the floor read \"Yes.\" — unearned praise contradicting the"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-15-R23.md",
     "lines": "53",
     "quote": "running out of tries is not passing"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record whether a student solved an item alone or with help, and let summaries list only what actually happened — completion, never mastery.",
   "kind": "adopted rule",
   "found_by": "Lesson-end summaries credited words a lesson never taught and no check compared them with the word cards; the honesty contract then required real counts, help recorded as help and no mastery claims.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "234",
     "quote": "and the receipt records it as practiced-with-help, never as solved-alone."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "33",
     "quote": "moment and it names the wrong trophies. No validator compares receipt words to"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "228",
     "quote": "3. **Completion, never mastery.** No string anywhere claims mastery, certification, approval,"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    14,
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count a lesson as done only when its checks were actually attempted, and make attention prompts blocking; points for volume and skippable nudges reward clicking through.",
   "kind": "adopted rule",
   "found_by": "Converging course proposals awarded points only for attempted scored checks to stop volume gaming; external reviewers then found a non-blocking 'read first' nudge skipped by clicking Next twice.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "42",
     "quote": "\"honest completion\" = XP only on a scored check"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "289",
     "quote": "\"Done\" counts only when the check is *attempted* (honest completion)."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "35",
     "quote": "where a \"not so fast — read, read\" nudge appeared it was non-blocking and skipped by clicking Next twice."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Stage high mastery bars — advisory at first, blocking later — because a flat high bar from the start leaves most learners no way in.",
   "kind": "measured",
   "found_by": "Only about 17% of an existing cohort cleared a 90% bar on an equivalent instrument.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "273",
     "quote": "a flat wall on the on-ramp has no path for the other 83%."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
     "lines": "147",
     "quote": "- **Only ~17% of students clear a 90% mastery bar** under the incumbent design (page 2). Our"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "After a miss, reteach and retry on a parallel item of the same difficulty; never escalate difficulty after a failure or re-serve the identical item.",
   "kind": "measured",
   "found_by": "In an existing course whose retry raised difficulty after a miss, second-attempt accuracy on one skill fell from 64% to 41%.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "46",
     "quote": "Data-derived: the incumbent's harder-on-retry drops supporting-details 64%→41% (−22.6pt)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "310",
     "quote": "**Never re-serve the identical item; never hand a harder item after failure.**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
     "lines": "122",
     "quote": "attempt-2 accuracy drops 64% → 41%"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never use the instrument that gates progress as the measure of growth; measure growth on held-out items that are never practised or gated.",
   "kind": "adopted rule",
   "found_by": "An adversarial review of a course plan found one instrument doing both jobs; the revision separated a held-out growth measure, and the instruction model required checks to be delayed, varied and independent before counting as mastery.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "321",
     "quote": "We never teach to or gate on it"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/02-[name]-instruction-model.md",
     "lines": "95",
     "quote": "Checks are not mastery unless delayed, varied, independent, and no-feedback."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "53",
     "quote": "Platforms that collapse the two masteries (acquisition vs durable) into one binary gate either over-reteach or under-practise"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Offer supports while students learn but switch them off for scored checks, and fade engagement supports before test conditions so they don't become crutches.",
   "kind": "adopted rule",
   "found_by": "A course plan drew the support boundary at the scored step so every score measures unsupported performance, and dropped permanent picture and character wrappers because supports that never fade teach dependency.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "330",
     "quote": "### Insight 7 — Word Assist boundary: practice on, scored off"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "332",
     "quote": "every scored item is a clean cold-condition measure"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "147",
     "quote": "• Permanent illustration/character wrapper — engagement scaffolds must fade to cold plain text or they teach dependency."
    }
   ],
   "against": "Whether video belongs at all stayed contested: \"This is a genuine, load-bearing tension\" (wiki-research/cross-cutting.md line 141).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Don't time a task unless speed is what it measures, but log response times quietly and treat scores from rapid guessing as invalid.",
   "kind": "adopted rule",
   "found_by": "Course and assessment plans noted that time pressure rewards rapid guessing and that the target test's publisher invalidates tests above 25% rapid guessing.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "265",
     "quote": "rewards rapid-guessing, which MAP penalizes."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/mapproxy_clean.md",
     "lines": "211",
     "quote": "NWEA invalidates tests above 25% rapid-guessing; disengagement deflates scores (Wise & DeMars 2005)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep corrective feedback short — never longer than the item, let alone the text — and if correcting a response needs more words than the instruction did, fix the item or where it sits.",
   "kind": "adopted rule",
   "found_by": "External reviewers found corrective feedback at times longer than the passage itself; a practice principle and a word cap followed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "12",
     "quote": "Corrective feedback now appears on many wrong answers, but it is far too long — at times longer than the passage itself (see the attached \"Nibbles\" warm-up)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "52",
     "quote": "If the feedback needed to correct a response is longer and more complex than the original instruction, the ITEM has crossed the acquisition boundary — fix the item or the placement, not the feedback."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "201",
     "quote": "evidence-anchored, ≤40 words target, never >60 (G5-POL-INS-008); wrong-"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26,
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Print everything that is spoken on the same screen, sentence for sentence, so the lesson still works with audio off.",
   "kind": "measured",
   "found_by": "The rule was written after two pages drifted 16 lines into paraphrase between narration and print; a level with read-aloud off by default required everything to be followable muted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "59",
     "quote": "- Nothing is spoken that is not printed on the same page, sentence for sentence — a spoken line"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "61",
     "quote": "exists because two pages drifted 16 lines into paraphrase)."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "61",
     "quote": "readable on screen. Read-aloud is OFF by default at G5: the lesson must be 100% followable"
    }
   ],
   "against": "The rule runs one way: \"read-along rule runs one way; printed-but-unspoken is\" (g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md line 90).",
   "adds_to_existing": [
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After any text edit, re-check its narration: tie each clip to a hash of its text and transcribe the clip back against the text.",
   "kind": "measured",
   "found_by": "A review clip with no text hash kept speaking an old definition; one same-day rewrite orphaned 117–179 narrated lines; a transcript check caught a reverted pronunciation that a re-voice had already cut.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/l4-p3-stale-clip-2026-09-29/README.md",
     "lines": "7",
     "quote": "**STALE** (older definition)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "185",
     "quote": "one real lesson had 117-179 narrated strings orphaned by a same-day rewrite whose"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/qc-run-2026-09-04/QC Run Report — Peter Pan L4-L7 + G5 (2026-09-04).md",
     "lines": "28",
     "quote": "the 02.09 course-tts re-voice then cut the regressed text. Whisper part-read check caught"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    50,
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check generated pictures of people with several independent reads and a planted control, rejecting ones that look machine-made; single reads were unstable.",
   "kind": "measured",
   "found_by": "A new image check was first proved to fire on machine-made film frames and stay quiet on drawn art; two runs then disagreed on 3 of 7 images, so three reads with majority rule became required.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "7",
     "quote": "Purpose: prove the new check DISCRIMINATES — fires on AI-generated film frames with humans, stays"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "42",
     "quote": "Runs 1 and 2 disagreed on vf07 (FAIL → note), vf08 (note → FAIL) and vf10 (note → FAIL) — the"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "45",
     "quote": "now requires three independent reads with majority rule on film frames and near-photoreal humans."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    22,
    34,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Label adapted, retold or newly written text as such on the page where it is read, so no one mistakes it for the original.",
   "kind": "adopted rule",
   "found_by": "A fidelity review found adapted reading pages without an adaptation marker in one unit, while another unit labelled every retelling on the reading page itself.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R17.md",
     "lines": "140",
     "quote": "written and labeled an adaptation, not a quotation or original chapter."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R18.md",
     "lines": "73",
     "quote": "an explicit attribution `booktag` on the reading page itself (not only on a later evidence/reference"
    }
   ],
   "against": "The gap was judged minor: \"No child is actively misled by this gap (L1 establishes context; meaning is preserved); no CRITICAL\" (g5-course/ADVERSARIAL-REVIEW-2026-09-08-R17.md line 144).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Credit only what was shown in the mode being assessed; a written plan is not evidence of a spoken performance.",
   "kind": "adopted rule",
   "found_by": "A unit on performance required delivery to be observed before it is credited, with redundant guards in the rubric, the instructions and the summary.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R18.md",
     "lines": "131",
     "quote": "\"Do not infer actual oral performance from typed claims\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R18.md",
     "lines": "134",
     "quote": "\"Your written explanation does not by itself prove spoken delivery.\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Name the thinking a lesson models by reading the definitions of the available labels, never by picking the nearest accepted label to pass a validator.",
   "kind": "adopted rule",
   "found_by": "A capstone lesson was nearly labelled with a procedure it did not model just to satisfy a validator; a later review confirmed, 2 votes to 1, a mislabel where the modelled trace related nothing.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/CAPSTONE-PROCEDURE-RULING-2026-08-18.md",
     "lines": "43",
     "quote": "Labelling that WEIGH would be mislabelling to satisfy a validator, which is exactly the"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-25-R10.md",
     "lines": "70",
     "quote": "carried `procedure: \"CONNECT\"` for a trace with nothing related."
    }
   ],
   "against": "The relabel had no visible effect for students: \"the D25 chrome decision means the procedure value renders no child-visible chip, so the relabel\" (g5-course/ADVERSARIAL-REVIEW-2026-08-25-R10.md line 62).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Never alter content or weaken a check just to make a build pass; fewer findings from a weakened check are not progress.",
   "kind": "measured",
   "found_by": "An uncommitted edit disabled detection and cut findings from 28/12 to 15/8, a mix of real cleanup and disabled checks; an earlier fix had inserted a word into another lesson to pass a validator and was reverted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/takeover-audit-2026-07-13/g5-clean-baseline.md",
     "lines": "146",
     "quote": "More importantly, the uncommitted linter edit reduces findings by weakening the gate:"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/takeover-audit-2026-07-13/g5-clean-baseline.md",
     "lines": "152",
     "quote": "Therefore, `28/12 -> 15/8` is a mix of real cleanup and disabled detection. It cannot be used as progress toward approval."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/DECISIONS-2026-08-24.md",
     "lines": "33",
     "quote": "that is editing someone else's lesson to satisfy our validator, and was"
    }
   ],
   "against": "Bending content to a checker is sometimes chosen, but recorded as such: \"Honest, but it is content bent to an engine\" (g5-course/ADVERSARIAL-REVIEW-2026-09-16-R25.md line 66).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Trace every threshold a check enforces to its source before failing content on it; a gate without a sourced reason is a preference.",
   "kind": "measured",
   "found_by": "An audit failed 81 of 81 item banks on a size floor of 15 that was really the top of an 8–15 target band, cited circularly; against the real floor of 8, 79 passed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/audit-heuristic-finding.md",
     "lines": "8",
     "quote": "The `>=15` bar is an **arbitrary auditor heuristic**, not a"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/audit-heuristic-finding.md",
     "lines": "82",
     "quote": "- Against the **correct floor of 8**: **79/81 pass**; **2 fail**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "168",
     "quote": "a gate without provenance is a preference, and preferences don't gate."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A check that trusts the writer's own skill labels cannot catch a wrong label; classify what each item actually asks independently.",
   "kind": "measured",
   "found_by": "Calibrating a lint against ten reviewer-found failures, mistagged items passed because the rules consumed the tags; external review had found items assessing something other than their tags; a keyword heuristic undercounted one skill fivefold (9.7% vs 2%).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/op-taxonomy-calibration.md",
     "lines": "68",
     "quote": "The mistag IS the failure, so deterministic rules that consume tags cannot see it"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "51",
     "quote": "Tagging still does not match what items assess."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/Grade 3 Reading - Proposal Review & Synthesis.docx",
     "lines": "164 (textutil plain-text output)",
     "quote": "inference was 5× undercounted by the heuristic (actually 9.7%, not 2%)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43,
    49,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make the skill list a check uses fine enough to separate the skills a lesson might confuse; when two skills share one label, switching between them passes every check.",
   "kind": "measured",
   "found_by": "A lesson that modelled one skill and released another passed the full lint because both skills mapped to one identifier.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/op-taxonomy-calibration.md",
     "lines": "46",
     "quote": "| fc-04b-skill-switch-collapsed-tag.json | PASS | (none - taxonomy blind spot, see fc-04) |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/op-taxonomy-calibration.md",
     "lines": "84",
     "quote": "skill switch is inexpressible - measured: `fc-04b-skill-switch-collapsed-tag.json`"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When sources or reviews set incompatible rules, record both and decide once with a recorded ruling, instead of silently picking one or changing content piecemeal.",
   "kind": "adopted rule",
   "found_by": "Two expert reviews directly conflicted — one requested an answer frame the other proposed replacing; planning named a silently flattened conflict as a failure; review practice routed contradictions to a record.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/edullm-standards-centralization-2026-08-05/IMPLEMENTATION-PLAN.md",
     "lines": "227",
     "quote": "### F5 - conflict is silently flattened"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/decision-brief-2026-09-10/DECISION-BRIEF.md",
     "lines": "43",
     "quote": "*requested* the \"The story says / so my answer is\" frame the 09-10 report proposes replacing."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "115",
     "quote": "Rulings are dated; a newer ruling beats an older register; contradictions between reviewers go"
    }
   ],
   "against": "Some conflicts are settled by an authority order: \"- **D4 — RULED: the ladder wins.** Per-lesson docs outrank the generic spec (tier rule);\" (DECISIONS-2026-08-24.md line 118).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Turn each piece of review feedback into a dated rule or an automated check, so the same kind of comment never has to be made twice.",
   "kind": "adopted rule",
   "found_by": "A narration comment had been made over and over without being implemented; after the fix a check was added so it could not recur, and a draft certification standard made this its governing principle.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "26",
     "quote": "> **No reviewer ever makes the same class of comment twice.**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/baseline-submission/CHANGES-FOR-REVIEW-L4-2026-08-31.md",
     "lines": "28",
     "quote": "shared over and over and continues not to be implemented"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/baseline-submission/CHANGES-FOR-REVIEW-L4-2026-08-31.md",
     "lines": "97",
     "quote": "We also added an automated check so a long opener like this cannot land again without being caught before it reaches you."
    }
   ],
   "against": "The standard itself was only a draft: \"Not shared, not adopted, binds nobody.\" (team-direction-2026-09-09/GATE-STANDARD-DRAFT.md line 5).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write a plan for each lesson before authoring it, review the built lesson against the plan, and record why each item format was chosen.",
   "kind": "adopted rule",
   "found_by": "Codified among the lesson certification gates; the course proposal likewise required success to be defined before building.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "81",
     "quote": "- One plan per lesson, written before authoring, reviewed against the built lesson after; the"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/04-evidence-contract.md",
     "lines": "3",
     "quote": "Per `eval-contract`, define success before building the prototype."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Leave hedging words out of student-facing instructions; they add processing load without adding information.",
   "kind": "adopted rule",
   "found_by": "A communication principle from direct-instruction guidance was adopted into lesson-writing rules; lessons state limits plainly instead of hedging.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "50",
     "quote": "Hedged language is not politeness, it is load: 'might', 'maybe', 'a little' are excluded because they add processing cost without information."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "205",
     "quote": "representation CANNOT show (\"Neither source named the fish's diet\"), without hedging into"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    2
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make praise name what the student's move accomplished; identical generic praise becomes wallpaper.",
   "kind": "adopted rule",
   "found_by": "A walkthrough found the same 'You did it!' and medal on all nine lesson endings; the writing rules require specific process praise.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "198",
     "quote": "Praise is specific process praise naming what the student's move accomplished"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "127",
     "quote": "lesson three the trophy is wallpaper. The `did`/`now` lines are honest and specific"
    }
   ],
   "against": "It was graded as polish only: \"**P-1. POLISH — all nine receipts are the identical \"You did it!\" + gold medal.**\" (g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md line 126).",
   "adds_to_existing": [
    2
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Author content for each level from that level's own sources, putting the difficulty in the task rather than in inflated prose; never reuse a lower level's lesson with harder words.",
   "kind": "adopted rule",
   "found_by": "A review found below-level distractors, answerable without the passage, in a higher-grade lesson; the authoring rules and later build plans require level-specific content from that level's own canon.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "53",
     "quote": "3. **Genuinely G5, never G3 dressed up.** Complexity lives in the task, not inflated prose. The"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "171",
     "quote": "`item-2-cards` distractors are below band."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-book-2026-09-29/SCOUT-AND-PLAN.md",
     "lines": "12",
     "quote": "\"never a Grade 3 copy; consult the canon; log the rule behind each decision\""
    }
   ],
   "against": "Mechanisms may carry across levels unchanged: \"(1) ALL G3-acquired mechanisms carry to G5 as-is\" (g5-book-2026-09-29/BUILD-SPEC-G5-U1-L1.md line 4).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the case used to model a skill out of every assessed item, and assess on new material.",
   "kind": "adopted rule",
   "found_by": "A fix-pass ruling removed a modelling-case distractor from an assessed item and made the separation absolute.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/AUTHORING-RULINGS-R1-R10.md",
     "lines": "80",
     "quote": "The kitchen/greenhouse/classroom modelling case never appears inside an assessed item."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Limit the reading load at each step — new names per section, length of answer options, and stretches of reading without a check.",
   "kind": "measured",
   "found_by": "Reviews flagged a ~204-word part introducing eight new names with options of 50–70 words each, four consecutive reading pages with no interaction, and narrated chunks of 241–279 words leaving students passive for over a minute.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "43",
     "quote": "~204-word part introduces EIGHT new proper names (Juniper, Vela, Nori, Moss, Lark,"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "258",
     "quote": "- **W-11. WORTH-FIXING — four consecutive reading pages with no interaction"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "493",
     "quote": "3 passage chunks exceed 60s passive during autoplay narration"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    7,
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't reuse one name for a different kind of thing across lessons read in sequence.",
   "kind": "adopted rule",
   "found_by": "A review found the same names used for a person in one lesson and for a source or record in the next.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "105",
     "quote": "same tokens keep changing referent class. Cheap to fix (rename L6's sources or L4's"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write instructions a literal reader can follow: the verb must match the action, the units must match what can be selected, and a fill-in frame must stay grammatical for every allowed answer.",
   "kind": "measured",
   "found_by": "A walkthrough found a 'select' verb on a free-writing box and a 'tap two sentences' task whose tappable units were whole paragraphs; a sentence frame produced 'has a enchanting'.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "172",
     "quote": "selection verb on a free-writing box; a child looks for four sentences to pick."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/baseline-submission/CHANGES-FOR-REVIEW-L4-2026-08-31.md",
     "lines": "32",
     "quote": "frame breaks grammar ('has a enchanting')"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    2
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Cap the number of selectable options in an item and keep each task on one screen without scrolling at the target display size.",
   "kind": "adopted rule",
   "found_by": "External reviewers called a twelve-option item an excessive load; a scan found 137 of 772 items over a five-option cap; a one-screen census found tasks running past the fold and split them.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "103",
     "quote": "one hot-text item offered twelve selectable options, an excessive motor and cognitive load for an eight-year-old."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/option_cap_report.md",
     "lines": "7",
     "quote": "- items over cap: **137**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/qc-run-2026-09-04/QC Run Report — Peter Pan L4-L7 + G5 (2026-09-04).md",
     "lines": "31",
     "quote": "### 3. HIGH — one-screen census, our lane (additions row I/census)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26,
    27
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Take every count in every document about a course from one named, dated data pull, and generate the documents from one source.",
   "kind": "adopted rule",
   "found_by": "An external review found the course's own documents disagreeing on lesson and item counts; the next package made one dated pull binding, and an audit recommended regenerating all documents from one ledger.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "111",
     "quote": "The email says 52 lessons, 745 items and 56 cold passages; the infographic says 47 lessons and 713 graded items"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
     "lines": "18",
     "quote": "- Every count in every doc must trace to one named pull with a date."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/takeover-audit-2026-07-13/g5-clean-baseline.md",
     "lines": "160",
     "quote": "should be derived from one structured source rather than hand-edited independently."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Enforce limits on claims in code: a score the evidence can't yet support should not appear in the output at all.",
   "kind": "adopted rule",
   "found_by": "Two audits found numbers drifting between documents (0.930 vs 0.928), so unsupported score scales were blocked in the scoring code rather than disclaimed in prose.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/mapproxy_clean.md",
     "lines": "161",
     "quote": "RIT, percentile, and CGP are **blocked in the engine**."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/mapproxy_clean.md",
     "lines": "163",
     "quote": "The two audits found number-drift in our *documents* (0.930 vs 0.928)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Let students practise the item formats they will be tested on, because an unfamiliar interface adds noise to the score.",
   "kind": "adopted rule",
   "found_by": "Students had practised only on multiple choice while the target test used other formats for over 30% of items; an assessment plan cited testing standards on construct-irrelevant variance.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/mapproxy_clean.md",
     "lines": "179",
     "quote": "Interface novelty is construct-irrelevant variance (AERA/APA/NCME Standard 1.13)."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "47",
     "quote": "B is the only one to flag that live course is 100% MCQ while MAP is >30% tech-enhanced"
    }
   ],
   "against": "Format practice can inflate internal growth readings: \"so a rise isn't format-practice inflation.\" (g5_build_2026_07_02/approval_clean.md line 321).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Before optimizing toward a benchmark, check that it measures the target skill; a pipeline bug can silently drop a whole domain.",
   "kind": "measured",
   "found_by": "A benchmark analysis concluded the target test was mostly grammar and phonics; the conclusion came from a pipeline bug that had dropped the entire informational-reading domain.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/Grade 3 Reading - Proposal Review & Synthesis.docx",
     "lines": "88 (textutil plain-text output)",
     "quote": "produced by a pipeline bug that dropped the entire RI domain"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before redesigning the teaching, check how much of the intended work learners actually do; low completion can be the binding problem rather than low accuracy.",
   "kind": "measured",
   "found_by": "An existing course's cohort completed about 30% of intended work (median completion 12.5%) while accuracy on attempted items averaged 83%.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "42",
     "quote": "Dosage is the measured #1 problem (12.5% completion, 7.6/25 min, ~0 acceleration)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "243",
     "quote": "The completion floor — 12.5% — is much further from acceptable than 39% is."
    }
   ],
   "against": "The accuracy baseline came from easy items: \"the wrong-instrument correction of the 83% baseline\" (team-direction-2026-09-09/DIRECTION-2026-09-09.md line 89).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Size a course to what learners actually complete; long courses collapse well before the end.",
   "kind": "measured",
   "found_by": "In an existing 120-lesson course with 12.5% median completion, completion failure began at about lesson 32.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/Grade 3 Reading - Proposal Review & Synthesis.docx",
     "lines": "192 (textutil plain-text output)",
     "quote": "the completion failure starts at ~32 lessons in the current course"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/Grade 3 Reading - Proposal Review & Synthesis.docx",
     "lines": "585 (textutil plain-text output)",
     "quote": "The incumbent has 120 lessons and 12.5% median completion."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build text length up toward what learners will eventually need to read; mastering short snippets never trains sustained reading.",
   "kind": "adopted rule",
   "found_by": "An external review found a course of passages averaging about 166 words, so a student could finish it without ever sustaining attention across a multi-passage block.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "69",
     "quote": "A child can master the whole course one short snippet at a time and never once sustain attention across a multi-passage block."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build purposeful rereads into each lesson rather than one read followed by questions.",
   "kind": "measured",
   "found_by": "A practical test of a 48-lesson package found every lesson used a single read pass; the course quality standard treats how a text is read as instruction.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/edullm-agent-entrypoint-g3-practical-test-2026-08-06/REPORT.qmd",
     "lines": "39",
     "quote": "- 48/48 lessons use a single explicit read pass."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "137",
     "quote": "5. How the text is READ is instruction, not delivery (Shanahan IES panel chair; REL West) → D3."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Have lessons say plainly what a source cannot show, and model refusing inferences it doesn't support.",
   "kind": "adopted rule",
   "found_by": "Written into a level's writing rules as its distinctive register; the transfer layer allows teaching students to explain why an option is unsupported.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "206",
     "quote": "vagueness and without overclaiming. Model honest refusal of unsupported inferences."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/03-transfer-practice-layer.md",
     "lines": "71",
     "quote": "- explain why an option is unsupported;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In inference questions, set a text-supported answer against one that is true in the world but unsupported by the text, and key the supported one even when the other is factually true.",
   "kind": "adopted rule",
   "found_by": "A course proposal's mastery design used supported versus true-but-unsupported pairs as its main defence against overreaching inference.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
     "lines": "80",
     "quote": "every inference CFU pairs \"supported by the text\" vs \"true but not supported,\" and the correct answer is the one with explicit line support **even when the alternative is factually true.**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/course-skeleton.md",
     "lines": "46",
     "quote": "Inference ~33–36% of items via evidence-bounded \"supported vs true-but-unsupported\" pairs."
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
   "statement": "Make items hard through the knowledge the lesson taught rather than through subtle distractors, so a student who learned it finds the item easy and a surface guesser is trapped; revise or retire items that true masters miss.",
   "kind": "adopted rule",
   "found_by": "A course proposal reconciled a 90% per-item success target for masters with near-miss distractors by sourcing difficulty from the taught knowledge and retiring items that masters miss.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
     "lines": "95",
     "quote": "We hold both by sourcing difficulty from the **knowledge gate, not distractor subtlety**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/course-skeleton.md",
     "lines": "35",
     "quote": "per-item p_m measured on real masters (drifters retired)"
    }
   ],
   "against": "The success target could not yet be measured: \"is a target we measure, not a property we ship.\" (g5_build_2026_07_02/approval_clean.md line 326).",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Use a model to predict where students will stumble, but don't treat its simulated answers as evidence of how students learn.",
   "kind": "adopted rule",
   "found_by": "All converging course proposals adopted the model as an expert predictor, not a student simulator, to avoid synthetic outcome claims.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "51",
     "quote": "LLM as expert-predictor not student-simulator"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "131",
     "quote": "expert-predictor not student-simulator. Six of eight (A–F) sit inside this cluster."
    }
   ],
   "against": "Scripted student walks are still used to test the flow: \"The contract gates read the JSON; the walker plays the lesson as a student against the live app\" (team-direction-2026-09-09/GATE-STANDARD-DRAFT.md line 91).",
   "adds_to_existing": [
    44,
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Claim the direction of an expected effect, not its size, until the outcome has been measured on the same learners.",
   "kind": "adopted rule",
   "found_by": "A database join found zero overlap between the cohort with the external test and the cohort with the internal proxy, so any transfer function was a measured void; plans refused to give a size until a pilot.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "259",
     "quote": "refuse to put a number on RIT until an in-cohort MAP pilot exists"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/X1_staar_map_overlap_probe_2026_06_16.md",
     "lines": "17",
     "quote": "it's a measured void, not an assumed one"
    }
   ],
   "against": "Later data partly changed the picture: \"old: no bridge possible (0/313 overlap). Current: 409 real G3 MAP RIT records\" (wiki-research/pedagogy-llm-evals.md line 130).",
   "adds_to_existing": [
    48,
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat structural quality, text dependence and teaching quality as separate properties, each with its own check.",
   "kind": "measured",
   "found_by": "A generated question scored a perfect structural score while being 100% answerable without its text, and a generator rewarded on structure converged on such questions; conversely, 13 of 13 rewritten items passed the without-text check but only 4 passed a quality rubric.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/GENERATOR_DIRECTIVE.md",
     "lines": "34",
     "quote": "**IB = 1.0. Blind-solve = 100%.**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/GENERATOR_DIRECTIVE.md",
     "lines": "44",
     "quote": "Structural quality and passage-dependency are **orthogonal**. Both must be in the signal."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "84",
     "quote": "- only 4/13 passed the LLM quality-B rubric"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge a course as a whole — coverage, difficulty ramp, balance against the test plan, distinct forms — not by its average item score.",
   "kind": "adopted rule",
   "found_by": "A generation directive reframed the target after a course of perfectly scored items turned out mostly answerable without its texts, and required a difficulty ramp across units.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/GENERATOR_DIRECTIVE.md",
     "lines": "13",
     "quote": "A 772-item course where every item scores IB 1.0 but 90% are blind-solvable is a **failed course**."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/GENERATOR_DIRECTIVE.md",
     "lines": "100",
     "quote": "- Lexile ramp **830 → 1010L**."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Sequence a course by both knowledge and difficulty; grouping by standard alone left difficulty flat, and grouping by difficulty band alone left no knowledge progression.",
   "kind": "measured",
   "found_by": "A coherence check found four units flat at about 900–913 on the readability scale because they were organised by standard; another build grouped items by difficulty band and had no knowledge progression; an external review called one course a readability staircase rather than a knowledge progression.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "208",
     "quote": "Units are organized by CCSS domain, not by difficulty progression."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md",
     "lines": "40",
     "quote": "groups by LEXILE band (830/920/1010L), not topic coherence; no knowledge progression exists"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "43",
     "quote": "The course is sequenced as a Lexile staircase, not a knowledge progression"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Prove each standard is covered by reading the scored item against the standard's boundary, count depth rather than mere presence, and never place a skill in a slot it doesn't fit just to close a gap.",
   "kind": "adopted rule",
   "found_by": "Closing 15 zero-coverage sub-skills to 0 was verified item by item, with prior-grade skills held out rather than fake-placed; a later count found all 82 sub-codes present but 61 only thinly covered.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/CURRICULUM-REVIEW-STANDING-2026-08-17.md",
     "lines": "81",
     "quote": "reading the actual scored item (not just relabeling a slot)."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/GAP-ANALYSIS-2026-08-18.md",
     "lines": "49",
     "quote": "but 61/82 rated \"Low\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/RULING-B-CARRIED-MASTERY.md",
     "lines": "20",
     "quote": "without being counted as coverage zeros, and without fake-placing them into slots they don't"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Screen every generated text for age-appropriateness and sensitive content, and check the generator's target-level setting, before any student sees it.",
   "kind": "measured",
   "found_by": "Reading the generation code found no age or sensitivity screen and a generator set to grade 11 for a grade-3 course.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "328",
     "quote": "MANDATORY on every auto-generated passage before it can reach a child"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "328",
     "quote": "fix the generator's grade setting (currently grade 11 → grade 3"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
     "lines": "194",
     "quote": "Safety items (S1, S2) test refusal behavior: S1 (suspenseful home-invasion passage for G3)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63,
    19
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Drop any generated content containing a number that can't be traced to its source; leaving a fact out teaches nothing false, while inventing one teaches a falsehood.",
   "kind": "measured",
   "found_by": "An early generated corpus showed a 2.4% fabrication rate; a lint dropping untraceable numbers removed about 2.8% of items, and fabrication scored zero in evaluation.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-method.md",
     "lines": "94",
     "quote": "an omitted number teaches nothing false; a fabricated number would be trained in as truth"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
     "lines": "71",
     "quote": "Fabrication scores 0 — not 0.5. The timeline notes a 2.4% fabrication rate in early synthetic"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    57,
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare judged scores only under the same judge and judge version; a judge change alone shifts absolute scores.",
   "kind": "measured",
   "found_by": "Re-scoring the same answers with a new judge moved them from 23.5 to 17.0 out of 25.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
     "lines": "68",
     "quote": "subset vs 23.5 in July — absolute numbers shifted with the judge; only within-eval comparisons"
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
   "statement": "Whenever a marker's rules change, replay a fixed set of scenarios — the intended answer, partial routes and a wrong-answer control, several runs each — and compare turn by turn; reasoning can't settle how a model will read a new rule.",
   "kind": "measured",
   "found_by": "A new anti-copy rule could be read two ways, so it was run: four scenarios times three runs on old and new rules matched in 12 of 12, the wrong-answer control held 3 of 3, and a later change shifted one scenario's first turn deterministically.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-16-R24.md",
     "lines": "41",
     "quote": "Reasoning cannot settle whether an LLM judge reads"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-16-R24.md",
     "lines": "65",
     "quote": "| wrong-answer control (\"Jo looks inside the basket\") | no pass | 3/3 off | 3/3 off |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-16-R26.md",
     "lines": "42",
     "quote": "All 18 turns identical in band AND ticked criteria to the R25 baseline (18/18)."
    }
   ],
   "against": "Each probe covered one item only: \"Not probed this tick (one step per tick).\" (g5-course/ADVERSARIAL-REVIEW-2026-09-16-R25.md line 60).",
   "adds_to_existing": [
    37,
    38,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "What counts as a leak depends on the subject: in source-based questions an answer found in the source is a leak, while in reading questions finding it in the text is the skill, so there the without-text check is a build-time lint, not proof of comprehension.",
   "kind": "adopted rule",
   "found_by": "Reading grading code first built for history items showed it skipped the history-style leak check for reading; the history pipeline's best result had relied on stem-only items that reading questions cannot use.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "328",
     "quote": "is a build-time lint (answer not in the stem, honest distractors)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v3/brainlift.md",
     "lines": "71",
     "quote": "In history, an answer you can find in the source counts as a leak. In reading, finding the answer"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/course-skeleton.md",
     "lines": "33",
     "quote": "my strongest history result used stem-only items that *skip* the leak-probe, which reading (passage-bound) cannot."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Picking the best of several drafts helps only when the picker is a rubric-grounded grader; a cheap overall ranker agreed only at the base rate and added nothing, and the checker rather than the writer set the quality ceiling.",
   "kind": "measured",
   "found_by": "Measured on an AP history item pipeline: a cheap holistic ranker had kappa 0 and best-of-N with it gave zero lift; quality was bounded by the verifier.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
     "lines": "102",
     "quote": "κ = 0, agreement = base rate; best-of-N with a cheap ranker = ZERO lift"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
     "lines": "102",
     "quote": "the verifier sets the ceiling, not the generator"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "337",
     "quote": "The system improved question quality by making bad output expensive to survive, not by trusting the generator."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    65,
    66
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Repeatedly hand-fixing one failing item against a grader may never converge because the failing dimension moves with each re-grade; generating several candidates and certifying the passer worked instead.",
   "kind": "measured",
   "found_by": "Measured on AP history items: 10 sequential expert hand-fixes failed while best-of-N produced a pass within 2 candidates.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
     "lines": "103",
     "quote": "10 sequential expert hand-fixes failed — the failing dimension migrated on each re-grade — while **best-of-N got a pass in 2 candidates**."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/course-skeleton.md",
     "lines": "29",
     "quote": "Hand-iteration doesn't converge (10 fails); best-of-N does (pass in 2)."
    }
   ],
   "against": "Re-sampling did not fix a systematic leak: \"Regen pilot (Wave 3) showed 9.5pt improvement in MCQ leak (99.5% → 90.0%) but leak remained\" (LANE1_COURSE.md line 167).",
   "adds_to_existing": [
    65
   ],
   "name_bearing_source": true
  },
  {
   "statement": "An item whose verdict flips between identical re-grades usually has a real defect; measure the grader's agreement with itself first and promote only items that pass on at least three re-grades.",
   "kind": "measured",
   "found_by": "Measured on AP history items: boundary items flipped on identical re-grades and the flips held real defects; verdicts were about 21% non-deterministic.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
     "lines": "104",
     "quote": "Items near the threshold **flip verdicts on identical re-grades** — and the flips contain *real* defects"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/course-skeleton.md",
     "lines": "30",
     "quote": "eduacc-style verdicts are ~21% non-deterministic; a single lucky grade is not a pass."
    }
   ],
   "against": "A tightly specified marker can be stable: \"Bands, banked criteria and passing turn are IDENTICAL across routes in 12/12 scenario runs.\" (g5-course/ADVERSARIAL-REVIEW-2026-09-16-R24.md line 67).",
   "adds_to_existing": [
    34,
    9
   ],
   "name_bearing_source": true
  },
  {
   "statement": "If the items that survive the checks can't fill the test plan, report a failure, not a pass with gaps.",
   "kind": "adopted rule",
   "found_by": "With multiple-choice items leaking about 90%, the gate-report template made too few survivors a hard failure; one plan had 36 of 44 vocabulary slots without a viable item.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/VERDICT_TEMPLATE.md",
     "lines": "28",
     "quote": "> not PASS-with-named-gaps. No green verdict over a vacuous pool."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "246",
     "quote": "**Implication for vocab slots:** 36 of 44 vocab-mcq slots in V2 skeleton have no viable items."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "How many words should a lesson teach in depth — exactly one, or two to three? The project's own sources disagree.",
   "kind": "open question",
   "found_by": "A rule pack set exactly one taught word per lesson, while the quality guidance asks for two to three academic words per lesson; a simulated review left it as an unresolved conflict.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/DECISIONS-2026-08-24.md",
     "lines": "26",
     "quote": "- **Exactly one taught word per lesson.** The rule pack sets this. Aladdin"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D1-D4.md",
     "lines": "221",
     "quote": "only 1 new word/lesson in L5/L6/L7 is below the wiki's own \"2-3 Tier-2 words per lesson\" rule, and is an open, unresolved conflict per the case study itself"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "How should a knowledge-building course give credit for knowledge built in earlier lessons, when the text-dependence gate removes every question answerable from prior knowledge?",
   "kind": "open question",
   "found_by": "An external review faulted a design that kept taught knowledge from helping, while the certification template accepted knowledge-recall items falling to about zero under the text-dependence gate; plans resolved only part of it by fading topic coherence before tests.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "43",
     "quote": "It cites Hirsch and Willingham and then forbids knowledge from helping."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/VERDICT_TEMPLATE.md",
     "lines": "70",
     "quote": "2. **KCT1 Domain-knowledge ≈ 0 — by design.** Domain-recall items are passage-independent → removed"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "296",
     "quote": "is the last scaffold, and like every other scaffold it fades gradually"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    48
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/corrective-feedback-policy.md",
   "lines": "48",
   "quote": "**concrete, addressable locus**, never a generic \"look again\":"
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "51",
   "quote": "- Every surface a child can miss must name the misconception and leave a way forward WITHOUT"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "231",
   "quote": "No hint or support is visible before the student's first genuine"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/14-prototype-unit-power-course-graph.md",
   "lines": "195",
   "quote": "- no new teaching before first attempt;"
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/CLOSURE-PLAN-2026-08-25.md",
   "lines": "19",
   "quote": "with a written pedagogical argument (a closed set the child works through)"
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "45",
   "quote": "- No `reveal_after_tries` on single-select — exhausting a closed list IS the thinking; a reveal"
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/decision-matrix/slices/07-SCORING-FEEDBACK-XP.csv",
   "lines": "55",
   "quote": "third miss the reveal that names the gap, states the answer, cites the text, and opens the gate"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "75",
   "quote": "- Items answerable without the passage are defects, not questions (provenance: ~78% of raw"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
   "lines": "232",
   "quote": "- **6/6** — the number of items an LLM-judge passed that a blind-solve cracked, the commitment-9"
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
   "lines": "43",
   "quote": "It cites Hirsch and Willingham and then forbids knowledge from helping."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
   "lines": "186",
   "quote": "- **W-8. WORTH-FIXING — `item-8-match` prompt 1 is a coin-flip between two dated"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-25-R10.md",
   "lines": "104",
   "quote": "per the lesson's own gloss pattern) can defensibly pick the distractor and be marked wrong."
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
   "lines": "145",
   "quote": "p7–p12 (never more than 2 reads without a check)"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
   "lines": "96",
   "quote": "79% (correct at position A, G4 census n=100 MCQ + 116 EBSR)"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
   "lines": "29",
   "quote": "Key-position imbalance, 12/19 A with a 5-run (must-fix)"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "119",
   "quote": "The word bank lists answers in the same order as the blanks (free, swords, sea), so tapping the first three words in order gets everything right without reading"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-28-R13.md",
   "lines": "40",
   "quote": "12 pass distinct-letters / 40%-cap / no-triple-run."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/edullm-standards-centralization-2026-08-05/README.qmd",
   "lines": "105",
   "quote": "> **BLOCKED — evidence missing; no pass inferred.**"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/edullm-standards-centralization-2026-08-05/IMPLEMENTATION-PLAN.md",
   "lines": "253",
   "quote": "3. Return `NOT_EVALUABLE` for affected rule."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/decision-brief-2026-09-10/DECISION-BRIEF.md",
   "lines": "57",
   "quote": "The judge accepted a misspelled \"magician\" as full credit. Comprehension currently tolerates"
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "175",
   "quote": "no `scoring`/`accept` spec passes on keyword presence alone"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R3.md",
   "lines": "10",
   "quote": "193 paragraphs, 1 deviation"
  },
  {
   "truth": 17,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/decision-matrix/slices/07-SCORING-FEEDBACK-XP.csv",
   "lines": "20",
   "quote": "ScrItem's quote gate requires 95% token-window similarity against candidate lines"
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/VOCAB-DECISIONS-U9.md",
   "lines": "68",
   "quote": "all clear the counting rule and are still wrong to teach: a Grade-5 card is spent on a word"
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
   "lines": "44",
   "quote": "REVISE cannot swap payload words out"
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-25-R10.md",
   "lines": "89",
   "quote": "Harm: the lesson's single most title-central term has a definition a child can never tap on the"
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/02-[name]-instruction-model.md",
   "lines": "29",
   "quote": "The bridge must be short and targeted. It is not a recall quiz and not a mini-lecture that drains the text."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/decision-packets-2026-09-03/PACKETS.md",
   "lines": "12",
   "quote": "the TEXT on p10. The image spoils him a page early and depicts action not on this page."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/GAP-ANALYSIS-2026-08-18.md",
   "lines": "6",
   "quote": "mechanically verified this session, not read from commit messages or status docs."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/DECISIONS-2026-08-24.md",
   "lines": "83",
   "quote": "- **Verify against the file, not the report.** Confident-wrong moments this"
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "64",
   "quote": "- Spoken lines never open with \"Name:\" — the TTS drops the label silently (speaker-label trap,"
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "42",
   "quote": "- 25-word ceiling on any sentence a child must act on (story prose and taught frames exempt,"
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
   "lines": "66",
   "quote": "rendered black text on a black background, legible only on hover"
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/sim-review-2026-09-02/FINDINGS.md",
   "lines": "5",
   "quote": "- CRITICAL: L6 p18 + L7 p18 `cfu` dialogues had NO gate key — closing comprehension"
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
   "lines": "157",
   "quote": "This is a hard, cited number (74% majorly flawed for LLM-generated items) that bears directly"
  },
  {
   "truth": 29,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
   "lines": "137",
   "quote": "old: LLMs assemble-and-tag only (generic model evidence). Current"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
   "lines": "94",
   "quote": "verbatim can be scored as off-text. Fix: author a pinned copy of the target"
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
   "lines": "88",
   "quote": "**The two FRQ rubrics — binary, AND-gated, shown not asserted.**"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
   "lines": "211",
   "quote": "calibrate**: v4 sprays (26 hits / 494 false-positive extras / 4-of-10 clean-correct out of a"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
   "lines": "120",
   "quote": "— but v4 \"sprays ~12 uncited extras per artifact\" (root cause: S3 stream was 6:1 flawed:clean)."
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
   "lines": "215",
   "quote": "the criterion text in context \"may simply not know where the line is\" (missing discrimination"
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
   "lines": "42",
   "quote": "Runs 1 and 2 disagreed on vf07 (FAIL → note), vf08 (note → FAIL) and vf10 (note → FAIL) — the"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/LANE3_LLM.md",
   "lines": "302",
   "quote": "**Calibration threshold:** If spot-check shows <70% agreement with gate labels → the gate threshold needs recalibration."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
   "lines": "93",
   "quote": "*(MEASURED-in-AP-history: Gemini↔IB DBQ agreement 16.7%)*"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/CRITIC.md",
   "lines": "27",
   "quote": "label consistency across four audit agents + eight skeptics was not tested"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/edullm-standards-centralization-2026-08-05/EXECUTOR-RUNBOOK.qmd",
   "lines": "523",
   "quote": "1. Positive, negative, boundary, and missing-input fixture for every blocking rule."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/op-taxonomy-calibration.md",
   "lines": "132",
   "quote": "fc-09 all flagged, zero false flags on controls, and the mandatory per-unit human"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/audit-heuristic-finding.md",
   "lines": "62",
   "quote": "Our ids are `g5-reading-merged-pp-9802-*`, so **the real enforcement"
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
   "lines": "55",
   "quote": "- Independent verify: every verdict recomputed from raw attempts alone"
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
   "lines": "225",
   "quote": "- **W-9. WORTH-FIXING — gradual release runs backwards, only here.** p14's chart"
  },
  {
   "truth": 42,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-claude/bank/final/BANK_REPORT.md",
   "lines": "43",
   "quote": "- **Variants are NOT independently anti-leak-gated.** They inherit their base item's certified"
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/takeover-audit-2026-07-13/pr68-enforcement-audit.md",
   "lines": "27",
   "quote": "lesson can omit both. An exact set diff would check declared identical strings only; it would"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
   "lines": "247",
   "quote": "- The \"43 of 285 criteria require a named human — no script or LLM-judge can close them\" fact,"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/course-json-standard-2026-07-13/README.md",
   "lines": "59",
   "quote": "- Schema validity is a document-integrity floor, not a course-quality, child-readiness, or"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/04-evidence-contract.md",
   "lines": "58",
   "quote": "If human review is unavailable, mark the claim as `owner_gap`, not `verified`."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
   "lines": "11",
   "quote": "File: `eval/eval.jsonl`. Authored 2026-07-21 from source documents BEFORE any system was built."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
   "lines": "12",
   "quote": "child's screen\" below is what the engine renders, not what the JSON suggests."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-27-R12.md",
   "lines": "52",
   "quote": "Why the suite missed it: `item-engine.test.mjs` tests the pure module and MsqItem's"
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/CRITIC.md",
   "lines": "7",
   "quote": "Why: what the child sees ≠ what the file holds."
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/decision-matrix/slices/08-VERIFICATION-DISCIPLINE.csv",
   "lines": "11",
   "quote": "the walk-lesson script must drive the real app in a real browser through the whole lesson and assert each step, rather than spot-checking"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/03-transfer-practice-layer.md",
   "lines": "95",
   "quote": "It proves assessment integrity, not curriculum quality."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
   "lines": "350",
   "quote": "- Blended: 83% (heavily weighted by easier item types)"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/edullm-agent-entrypoint-g3-practical-test-2026-08-06/REPORT.qmd",
   "lines": "31",
   "quote": "one ZIP-only file and two byte mismatches"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R18.md",
   "lines": "25",
   "quote": "exactly before trusting any line-level comparison against it."
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/G5-CURRICULUM-ONE-PAGER.md",
   "lines": "35",
   "quote": "noted, not treated as approval."
  },
  {
   "truth": 52,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
   "lines": "141",
   "quote": "This is a genuine, load-bearing tension"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
   "lines": "200",
   "quote": "the child who freezes needs scaffold-down"
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "174",
   "quote": "16. **Grading guidance MUST demand stance, not tokens; quotes fail closed (F16).**"
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "46",
   "quote": "1. **The canonical file is the sole truth.** Every passage sentence, span id, item, misconception"
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/AUTHORING-RULINGS-R1-R10.md",
   "lines": "106",
   "quote": "For every gated non-mcq item, each hint/second_hint/reveal must trace to canon"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/Grade 3 Reading - Proposal Review & Synthesis.docx",
   "lines": "164 (textutil plain-text output)",
   "quote": "the 92% mismatch rate in literary units (12/13 guiding items ask wrong-subject questions)"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/LANE3_LLM.md",
   "lines": "347",
   "quote": "prevents the PPO loop from finding reward by maximizing all other checks while ignoring the one that matters"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
   "lines": "139",
   "quote": "Items are learning events; a bad item teaches a false belief"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-book-2026-09-29/logs/GATE-VERDICT.md",
   "lines": "3",
   "quote": "Failure lines identical step by step"
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "366",
   "quote": "- After the agent returns, spot-verify checklist items 2, 7, 11, and 17 independently before"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R17.md",
   "lines": "19",
   "quote": "against the geology canonical files would produce a 100% spurious mismatch on every passage and"
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "251",
   "quote": "No contract ⇒ no diagram —"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
   "lines": "215",
   "quote": "The gate was not a self-check. The authoring model family was GPT; the gate solver was Gemini."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
   "lines": "105",
   "quote": "a same-family picker + judge produces Goodhart inflation"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/corrective-feedback-policy.md",
   "lines": "33",
   "quote": "No model call decides"
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "118",
   "quote": "— targeted verifiers read one slice; the colon-fix went red on a validator the listen pipeline"
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/build-closing-questions-2026-09-25/BUILD-SPEC.md",
   "lines": "66",
   "quote": "per-lesson md5 of every OTHER lesson unchanged after each step"
  }
 ]
}
```
