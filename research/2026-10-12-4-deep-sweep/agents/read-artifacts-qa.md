# read:artifacts-qa

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "artifacts-qa",
 "coverage": {
  "read": [
   "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
   "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21/ (README.md, index.html item list)",
   "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md (all 299 lines)",
   "~/Projects/grade3-reading/artifacts/criteria-register.csv (all 122 rows; a criteria register, not data)",
   "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
   "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/ (REPORT.md, CRITIC.md, RESUME.md, inputs/PRIOR-curriculum-verification-2026-09-10.md, inputs/procedures/*.txt)",
   "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/ (PP-STANDING, GAPS-2026-09-11, VISUAL-QA, L4-REVIEW-GAPS, L6-VALUE, ROUND-RESULT, GAP-CLOSURE-PLAN, PARITY-PLAN, QA-HANDOFF, PR-BODY x3, BOOK-WALK-DESIGN (grep), rulings/F1-README, rulings/L6p16-README, video-2026-09-16/PETER-PAN-PART-1-FILM.md, readiness-2026-09-16 docs incl. audio/*, annotation-and-walk/*, pr263-merge/RED-REGISTER, final-source-review, integration-check-02, historical-pointers, harness-runner/RESULT, book-driver FINAL-CLAIM-AUDIT and ANNOTATION-AUDIO-DISPOSITION, L5-L6-FIX-WORKFLOW-PLAN, PLAN, INTERNAL-REVIEW-MESSAGE, D5-11-STEM-PROPOSAL; readiness-l5-2026-09-17/L5-REVIEW-GAPS and sim-review/* lenses and agent A/B/C reviews)",
   "~/Projects/grade3-reading/artifacts/codex-qa/ (harness-2026-09-14.txt, tool-reuse-assessment, experience-2026-09-14/RESULT.md, independent-observer REVIEW and FINAL-REVIEW, verifier-controls FINAL-RESULT, recurrence/CLASSIFICATION-REVIEW-v3.md, controller-2026-09-14/PLAN.md and HANDOVER.md (grep), agent-guidance README)",
   "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/ (00-difficulty-notes, 00-knowledge-inventory, 02-factuality-claims, items/02-gate-summary, phase-d/02-gate-summary, phase-d/DELTA-REPORT, spine-gate/SPINE-GATE-REPORT, phase-e/capstone/exemplars-rubric.md, passage.md, gate-capstone-summary.json, phase-e/00-restructure-summary.json, publish/README.md, passages/kingfisher-bend-01.md header, 01-placement-record.json header)",
   "~/Projects/grade3-reading/artifacts/alpha-read-packager/ (BUNDLE_CONTENT_BUGS, LLM_GENERATION_BOUNDARY, RULES, FACTS_SHEET, SUMMARY_HUMAN, BRIEFING, FIX_LIST, GRADE5_COURSE_SPEC, TI_COURSEPLANS_PR_PROPOSAL (grep), SUMMARY_AGENT_G5 (key sections), agent.qmd/README/skill (grep), generator/GENERATOR.md and RESULTS.md, generator/g5/GATE1_BLIND_SOLVE_REPORT, G5_OPTION_A_GATE_REPORT, GENERATOR_REPAIR_KIT, MSQ_REGEN_GUIDE, PASSAGE_DESIGN_RULES, PASSAGE_GENERATOR head, MCQ_BEFORE_AFTER head, STANDARDS_COVERAGE_MATRIX (grep), PROMPT_INSTRUCTION_OPTION_LENGTH, G5_GENERATOR (headers); v2_final_package/WHY_V2_WINS, README, docs/COURSE_QUALITY_GATE_REPORT, FEEDBACK_RESPONSE, KB_FURTHER_IMPROVEMENTS, V2_MONSTER_DOSSIER, COMPLIANCE, SUMMARY_AGENT.qmd timeline/end-state)",
   "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
   "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/ (REGISTER.md, census-*.txt)",
   "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/ (REGISTER.md, BUILD-SPEC-batch.md headers, binding rules and appendix 2)",
   "~/Projects/grade3-reading/artifacts/feedback-content-review-2026-09-20/REGISTER.md",
   "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/ (Closing_Questions_Pattern.txt, REGISTER.md)",
   "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/ (REGISTER.md, BUILD-SPEC.md, PR-BODY.md, logs/walks/summary.txt)",
   "~/Projects/grade3-reading/artifacts/feedback-codex-visual-2026-09-07/REGISTER.md",
   "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/ (REGISTER.md, DECISION-BASELINE.md, analysis-current-courses/RESEARCH-BOUNDARIES.md, VERIFICATION-PROPOSALS.md, INDEPENDENT-REVIEW.md, G3-APPLICABILITY.md)",
   "~/Projects/grade3-reading/artifacts/feedback-argus-ui-2026-09-30/REGISTER.md",
   "~/Projects/grade3-reading/artifacts/feedback-pp-2026-08-27/REGISTER.md",
   "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/ (feedback-text.txt, REGISTER.md)",
   "~/Projects/grade3-reading/artifacts/feedback-ela-chat-2026-09-24/ (REGISTER.md, DEEP-READ-2026-09-24.md)",
   "~/Projects/grade3-reading/artifacts/compare-2026-09-22/*.html (text), compare-2026-09-23/index.html (text), compare-2026-09-24/FINDINGS.md",
   "~/Projects/grade3-reading/artifacts/eval-suite/ (RUBRIC.md, RANKING.md, items.csv header only)",
   "~/Projects/grade3-reading/artifacts/cert-layer/ (VISION-QA-CALIBRATION, AUTOMATED-CHECKS-ROADMAP, CONTRACT-v0, TELEMETRY-SCHEMA-v0)",
   "~/Projects/grade3-reading/artifacts/listen-qa-l4-l7-2026-09-24/ and listen-qa-l1-orphans-2026-09-24/ (sampled transcripts; escalated clips)",
   "~/Projects/grade3-reading/artifacts/l1-parity-untracked-2026-09-24/ (escalated listen-qa clips, authoring ops-silent-rewrite.json)"
  ],
  "skipped": [
   "All *.log files (pace-gate, pp-defense, codex-qa run logs, walker logs, cut logs): logs, per the read-only rules",
   "All .jsonl ledgers and large JSON data (findings.json, rows.json, audit JSON, served lesson JSON, TASK-FREEZE, observations, gauge JSON): data dumps",
   "Images, audio (mp3), screenshots, montage PNGs, PDFs in research-primary (relied on the RESEARCH-BOUNDARIES summary of those papers instead)",
   "Scripts and tests (*.py, *.mjs, *.ts, .sh) and .git/.beads internals: code, not findings",
   "alpha-read-packager/course-docs.enc: encrypted",
   "Files whose paths carry a person's name (BUNDLE_CONTENT_BUGS_[name].md, parity-l1-2026-09-17/[name]-L1-PARITY-2026-09-17.md, generator/g5/HANDOFF_FOR_[name].md, README_FOR_[name].md): avoided in favour of name-free sources covering the same ground",
   "Platform/vendor documents (OUTSIDE_POWERPATH.md, POWERPATH_L1_MIGRATION_CALL.md, POWERPATH.md, agent-guidance supplied-agents.md, EDULLM_* patch docs) and TEAM_COMMS_DRAFTS.md: infrastructure or organisational",
   "peter-pan-standing book-driver tail-driver READMEs, HOSTED-LOCAL and PR263 runbooks, baseline handovers (grepped only): harness engineering",
   "SUMMARY_AGENT.qmd per-item listing (>1,000 item rows) and sample_lesson XML: data",
   "demo-unit 03-build-manifest.json, ledger.json, corpus.json, unit-final.json: data"
  ],
  "notes": "Strongest knowledge-related findings come from demo-unit-2026-07-10 (knowledge inventory with carrying spans and a compounding check; a factuality ledger separating world claims from fiction; a spine-conditioned blind solve showing items answerable from earlier lessons' schema; FK readability blind to conceptual load) and from curriculum-adherence-2026-09-24 (a later unit's transfer questions depend on two ideas earlier lessons failed to land). 'AP' material in scope is limited to alpha-read-packager: FACTS_SHEET.md (the aptraining 0.29->0.95 lever refuted under the binding grader; '99%' = cache + best-of-N; '28%' = four harness bugs; convergence was one author, not replication) and generator/GENERATOR.md (anti-leak generation policy emulating the aptraining fine-tune goal). Conflicts recorded: truth 7 is limited by Van den Broek et al. 2001 (mid-text inferential questions cut grade-4 untargeted recall); truth 4 conflicts with a never-reveal rule for single-select items (R-Q-20/R-Q-24, recorded as an open contradiction); truth 28 is limited by a decision to make in-lesson teaching checks non-gating; truth 3 was overridden once where a design prescribed a goal line that pre-supplied the inference. Many numbers come from LLM blind solvers whose verdicts drift with model version (SPINE-GATE-REPORT); treat leak rates as dated measurements. The listen-qa folders hold raw transcripts without commentary; only the escalated and a few sampled clips were read."
 },
 "candidates": [
  {
   "statement": "Some question formats are far easier to make depend on the text than others: re-ordering text-specific fragments passed a blind test every time, while plain choice items mostly leaked.",
   "kind": "measured",
   "found_by": "A blind-solve gate (text withheld, plus a with-text control) over 76 generated items, tallied by construction family.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "20",
     "quote": "| fragment-sequence | 24 | 24 | 0 | 0 | 100% |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "22",
     "quote": "| choice-hottext | 24 | 4 | 19 | 1 | 17% |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "28",
     "quote": "Plain choice/hot-text confirms its high-leak prior (13/16 MCQ leaked)."
    }
   ],
   "against": "Ordering items about well-known processes leaked heavily elsewhere: \"| sequence | 185 | **58.4%** | 3.0% | **~19×** | adjacent-pair order 85.2% |\" (alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md:17), so the format helps only when the order is fixed by the text.",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Items whose answer follows a well-known real-world order or category can be answered without reading; tie the key to an order, entity or category that only this text defines.",
   "kind": "measured",
   "found_by": "Cross-family blind solve of 480 generated items with text, key and feedback withheld, compared with chance.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "17",
     "quote": "| sequence | 185 | **58.4%** | 3.0% | **~19×** | adjacent-pair order 85.2% |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "31-32",
     "quote": "real-world things have canonical categories — recoverable with zero reading."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "44",
     "quote": "items must hinge on passage-unique facts a general model can't recover"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When world knowledge points to an answer the text contradicts, make that default a wrong option; keys that match the world-knowledge guess can be found without reading.",
   "kind": "measured",
   "found_by": "Gate results on generated items: keys equal to the solver's narrative guess leaked; survivors hid the key in text-internal detail or ran against the schema with a world-favourite decoy; an independent audit confirmed the trap.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "62",
     "quote": "key is the blind solver's plurality narrative guess dies (8/11 cause leaks, incl."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "64-65",
     "quote": "a world-favorite decoy out-competes the key"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/RESULTS.md",
     "lines": "32",
     "quote": "GK default (d) \"walls keep out water\" is the trap; text says cold WINDS → blind solver actively misled to {a,d}; {a,b} text-locked"
    }
   ],
   "against": "When the text itself rules out the obvious causes, the distractors become easy once read: \"The quality screen flagged this on **14 of 26** items\" (alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md:96).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Generated multiple-choice items tend to make the right answer the longest option, so keep options to similar length, never let the key be uniquely longest, and check by counting.",
   "kind": "measured",
   "found_by": "A course-scale structural probe of generated items and forensic analysis of leaked items; a validator caught a rewrite that made the key longest.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
     "lines": "34",
     "quote": "At course scale the tell is endemic: 289/794 keyed MCQs have the correct option strictly longest (~36%)."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "16",
     "quote": "| Correct answer is the longest option | 28% | n/a | Length cue alone recovers the key |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/L5-REVIEW-GAPS-2026-09-17.md",
     "lines": "8",
     "quote": "the first wording made the correct option the single longest (95 vs 91) — validator caught it"
    }
   ],
   "against": "In multi-select items the cue can be confounded: \"A test-taking strategy of \"pick the two longest\" yields opt[1]+opt[2], which is one right and one wrong\" (peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md:102).",
   "adds_to_existing": [
    5,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Wrong options containing absolute words (always, never, all, only) can be crossed off without reading.",
   "kind": "measured",
   "found_by": "Forensic analysis of 150 multiple-choice and 100 select-all generated items with high leak rates.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "4",
     "quote": "**Based on:** Forensic analysis of 150 MCQ + 100 MSQ items (62.7% MCQ leak rate, 51.0% MSQ leak rate)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "15",
     "quote": "| Absolute language in wrong options | 27.3% | 34% | Students eliminate \"always/never/all/only\" without reading |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write every option in the same grammatical shape; a key that is the only option with a different opener, article or clause pattern can be found by shape alone.",
   "kind": "measured",
   "found_by": "An external quality audit of shipped lessons flagged keys identifiable by form; a class sweep then found the same tell on other items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "8",
     "quote": "\"The answer is the only option not shaped like a question\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "10",
     "quote": "\"The correct sentence is the only one that does not use 'because'\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
     "lines": "9",
     "quote": "key is the only option without an article"
    }
   ],
   "against": "Automated shape flags can be false positives: \"recorded so the raw score is not taken at face value\" (feedback-inceptbench-2026-09-18/REGISTER.md:14).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build wrong options as near-neighbours: a real detail of the text with one element changed; absurd, off-category or true-of-any-text options are eliminated without reading.",
   "kind": "measured",
   "found_by": "Leak forensics on generated items and an external audit of shipped checks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "184",
     "quote": "- Change ONE of: the subject, the cause, the effect, the relationship direction, or the scope."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "17",
     "quote": "| Generic topic-domain wrong option | 22% | 8% | \"Any passage on this topic\" option is trivially wrong |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "9",
     "quote": "\"One option is not a Darling child, so it is eliminable from the stem alone\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Each wrong option should carry a different misconception; when all wrong options share one tone or one misreading, the key wins by elimination.",
   "kind": "measured",
   "found_by": "An external audit, a live walkthrough and a simulated review found word-meaning checks whose distractors were all kind words or all the same misuse.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "64",
     "quote": "All three distractors (friendly, gentle, caring) share the same \"nice\" valence, so the only unpleasant word (menacing) wins by elimination"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/L5-REVIEW-GAPS-2026-09-17.md",
     "lines": "8",
     "quote": "all three distractors were the same misconception (menacing used for something pleasant)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
     "lines": "40",
     "quote": "author named misconception catalogue (M-REVERSE, M-EFFECT-AS-CAUSE, M-LAST-FIRST…), tag each distractor"
    }
   ],
   "against": "A usage check may legitimately test one register violation: \"Downgraded to MINOR; criterion was designed for comprehension MCQs\" (peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-B-D5-D6-D11-D13.md:21).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In select-all items each option is judged on its own, so every option must be decidable only from the text, and knowing one right answer must not reveal another.",
   "kind": "measured",
   "found_by": "A blind-solve audit of generated select-all items found none usable.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md",
     "lines": "3",
     "quote": "**Status:** MSQ pool is 100% leaked (0 of 1,346 structural-pass items usable)."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md",
     "lines": "12",
     "quote": "In MSQ each option is judged true/false independently."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md",
     "lines": "41",
     "quote": "**5. Knowing one correct answer must not help you find the other.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "No two wrong options may contradict each other and none may be ruled out by the stem alone, because either turns a four-option item into a coin flip.",
   "kind": "adopted rule",
   "found_by": "Distractor rules written from leak forensics on generated items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "95-96",
     "quote": "is left with a 50/50 — you have effectively built a 2-choice item."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "124",
     "quote": "Option C uses \"Both... agree\" on a question asking about a *difference* — eliminatable by reading the stem alone."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "For a main-idea item all options must be the same scope: no broad truism among the wrong options and no key that is the only broad option.",
   "kind": "measured",
   "found_by": "Leak analysis of generated items and an audit of a live practice pool (a 'pick the broadest option' leak).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md",
     "lines": "102",
     "quote": "`mainidea-earthworm-mcq-05` leaks instead via the \"pick the broadest option\" main-idea heuristic (its foils are all true narrow details)."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GENERATOR_REPAIR_KIT.md",
     "lines": "69-70",
     "quote": "main-idea status (a \"promoted supporting detail\" distractor)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Put the question's distinctive words on a wrong option, not on the key; when the key repeats the stem's words or is the only option of its kind, learners match words or sentence types instead of reading.",
   "kind": "measured",
   "found_by": "Audit of a live practice pool (14 leaky items of this class) and an external audit of shipped lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md",
     "lines": "92",
     "quote": "Student discriminates by sentence-TYPE, not support-relationship. Hottext variants leak because the prompt reuses the key's distinctive content words."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md",
     "lines": "108",
     "quote": "The verbatim-keyword sentence (h9) is a DISTRACTOR; the key (h8) shares no prompt keywords — keyword-matching points AWAY from the key"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "79",
     "quote": "Key is the only option that repeats the stem's verb ('find'→'found')"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Word stems so they point to the text (what the passage describes), never to how the world works, since a stem that invokes general knowledge invites answering without reading.",
   "kind": "measured",
   "found_by": "Audit of live mastery-form items found a matching stem that explicitly invited world knowledge.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md",
     "lines": "75",
     "quote": "Prompt 'Match each cause to its correct effect based on how the water cycle works' explicitly invites world-knowledge, not the text."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/MSQ_REGEN_GUIDE.md",
     "lines": "39",
     "quote": "The stem must invoke a passage-specific standard"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a sequence that builds knowledge, test items also against what earlier lessons taught: an item can fail the plain blind test yet be answerable from the earlier lessons' schema, so write distractors consistent with that schema that only the new text decides between.",
   "kind": "measured",
   "found_by": "A blind solve given the prior-lesson corpus with the new text withheld, run on certified items of a four-text unit and on capstone items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md",
     "lines": "19",
     "quote": "that the plain-blind certification gate structurally cannot see (same item: 0/3 exact"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md",
     "lines": "83",
     "quote": "exactly why the item cannot serve as evidence the student read text 4."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/gate-capstone-summary.json",
     "lines": "16",
     "quote": "\"spine_leaky\": 2,"
    }
   ],
   "against": "The headline example was later reclassified: \"calibrated Gemini 3.5 solves the target 3/3 without either passage or prior-course context.\" (demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md:7).",
   "adds_to_existing": [
    5,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A blind-solve verdict belongs to the solver and version that produced it; rerun old verdicts with a pinned current model before relying on them.",
   "kind": "measured",
   "found_by": "A newer solver replay of a historical result solved the item 3/3 even without any context.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md",
     "lines": "7",
     "quote": "calibrated Gemini 3.5 solves the target 3/3 without either passage or prior-course context."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/spine-gate/SPINE-GATE-REPORT.md",
     "lines": "113",
     "quote": "solver results drift and must be rerun with a pinned current model."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat text-dependence verdicts as stochastic: ship only items clean across several independent blind draws, and permanently exclude any item that ever leaked.",
   "kind": "measured",
   "found_by": "Repeated cross-family blind-solve draws on the same item pool.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "68",
     "quote": "Measured: ~22% flipped on the 2nd draw, 11.1% on the 3rd unified draw — it asymptotes but"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "69-70",
     "quote": "permanently excludes any item that *ever* leaked, so a"
    }
   ],
   "against": "A boundary score can be small-sample noise: \"(the 0.5 was small-sample noise)\" (same file:107).",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-run only measurements that failed to complete, never re-roll unfavourable verdicts, and never certify on missing evidence, because errored attempts bias toward passing.",
   "kind": "measured",
   "found_by": "A repair wave on a blind-solve gate flipped false certifications.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "47",
     "quote": "attempts bias toward certification; errored controls toward false defect). Leaky verdicts"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "48",
     "quote": "were never re-rolled. The wave flipped 2 false certifications to leaky and 2 to"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9,
    65
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Pair the blind test with a with-text control: an item must be answerable when the text is present as well as unanswerable without it.",
   "kind": "measured",
   "found_by": "Gate design and results (some items failed the with-text control); a separate blind probe named the missing control as a gap.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "9",
     "quote": "bar: plain-blind anti-leak (passage withheld) + with-passage answerability control"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
     "lines": "35-36",
     "quote": "genuinely ambiguous with the text"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "53",
     "quote": "**No passage-present control.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Certify text-dependence with solvers from model families other than the generator and call an item clean only if every family fails; a generator's own grader passes items that independent and deterministic checks catch.",
   "kind": "measured",
   "found_by": "Comparison of an in-loop grader, an independent audit and a post-deploy structural probe on generated items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
     "lines": "34",
     "quote": "In-loop grader passed at 100%; independent audit held ~89% (passed a half-leaky EBSR); a post-deploy structural probe then caught 5/15 longest-option tells *both* earlier graders missed."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "18",
     "quote": "**Intersection rule:** clean iff *every* family fails to recover (rate ≤ 0.5); leaky iff *any*"
    }
   ],
   "against": "Independence needs enforcement, not just separate agents: \"mistaking two agents with shared write access for enforced independence\" (codex-qa/tool-reuse-assessment-2026-09-14.md:47); and the generator itself stayed one family: \"**Single generator family.**\" (COURSE_QUALITY_GATE_REPORT.md:124).",
   "adds_to_existing": [
    43,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A high instructional-quality score says nothing about whether items need the text.",
   "kind": "measured",
   "found_by": "A quality benchmark run on a sample of items a blind solve had shown to be answerable without the passage.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "60",
     "quote": "Stratified 90-item sample (30 per type) scored **mean 0.932**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
     "lines": "65-66",
     "quote": "compliance, NOT passage-dependence."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
     "lines": "19",
     "quote": "wrong construct; green-lights leaks at 1.0"
    }
   ],
   "against": "It can still catch blatant mismatches: \"IB *can* catch a **blatant** passage mismatch and did here\" (alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md:254).",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure a quality judge's agreement with itself across independent draws before trusting it, especially on formats it has no native evaluator for.",
   "kind": "measured",
   "found_by": "Two full independent draws of a quality benchmark on the same 26 items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "31",
     "quote": "grader self-agreement was measured first"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "40",
     "quote": "| **no** | **match** | 2 | **0/2** (1.00↔0.55, 1.00↔0.95) | **flip-band — IB NON-DIAGNOSTIC** |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34,
    35
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Per-item checks cannot see course-level faults, so de-duplicate passages and stems across the whole set and keep parallel forms disjoint.",
   "kind": "measured",
   "found_by": "A course-level look at a generated course that had passed its per-item compliance gate.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
     "lines": "36",
     "quote": "947 passages collapse to 136 distinct (one reused 22×), 134 stems duplicated, MAP forms A/B share 3 stems. The compliance gate PASSED — it checks none of this."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "398",
     "quote": "4 parallel mastery forms fully **DISJOINT**: 114 distinct items, max pairwise overlap = 0."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A sentence frame with a blank must read correctly for every value the blank can take, including pronouns inside embedded quotes; check by substituting each value.",
   "kind": "measured",
   "found_by": "A shipped frame produced an article error with a learner's own word; a live walkthrough found an assembled sentence carrying a quoted speaker's 'me'.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "49",
     "quote": "an article/agreement mismatch (\"has a enchanting\") is a defect, not a copy nit"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "17",
     "quote": "assembled you-do sentence carries Peter's \"me\" (\"Captain Hook 'hates me…'\")"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write item stems as full questions, not sentence-completion fragments.",
   "kind": "adopted rule",
   "found_by": "Simulated review rounds flagged fragment stems in two lessons; they were rewritten against a reference lesson's shape.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L4-REVIEW-GAPS-2026-09-16.md",
     "lines": "117",
     "quote": "Item stems are questions, not completion fragments (D5.11)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/L5-REVIEW-GAPS-2026-09-17.md",
     "lines": "7",
     "quote": "was a completion fragment (\"…staying here could mean ___\"), the only fragment stems in L5"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Never ask a question answerable yes or no or by a two-way pick: recast it as what or how, with at least four plausible options.",
   "kind": "adopted rule",
   "found_by": "Content review of a shipped lesson; encoded as a criterion, a stem scan and a checklist gate.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "25",
     "quote": "Even though the app says you can't just answer it yes or no, we should just avoid these questions altogether."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "50",
     "quote": "Every MCQ has ≥4 plausible options; zero two-option coin flips"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Don't key a follow-up to the exact words the learner just heard or to the example used to teach; that tests echo, not understanding.",
   "kind": "measured",
   "found_by": "Overlap measured between dialogue follow-up keys and the spoken line before them; an external audit of a vocabulary check that reused the teaching card's example.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-23/index.html",
     "lines": "68",
     "quote": "Measured across every branched cfu, ours were the outliers: L4 echoed its answer at"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-23/index.html",
     "lines": "77",
     "quote": "The right answer is the sentence Scout just said, word for word."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "63",
     "quote": "and it reuses the p2 card's own key concept (bared teeth)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3,
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An earlier step must not use up the evidence or answer a later step teaches or tests; an early check keyed to the model's own clue, or a 'where to look' step that names the evidence, empties the later task.",
   "kind": "measured",
   "found_by": "A curriculum adherence audit and an external audit across four lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "112",
     "quote": "pre-spends the MM clue \"without a mother\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "94",
     "quote": "p13's key ('John grabbed a wooden sword and stood in front of his little brother.') is the exact line p14's I-do model later 'finds'"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "127",
     "quote": "The Search step's correct answer names two of the three Step-3 evidence lines directly"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3,
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When an answer must use a taught word, print that word nowhere in the question, instructions or hints that demand it.",
   "kind": "adopted rule",
   "found_by": "An AI review and an external audit flagged stems that gave away the required word; a census then checked every node that demands the word.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-ela-chat-2026-09-24/REGISTER.md",
     "lines": "10",
     "quote": "don't take this as a general licence to put the taught word in the stem"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
     "lines": "19",
     "quote": "you-do question gives away the magic word"
    }
   ],
   "against": "An exception was ruled for the first lesson of a course: \"I judged the item purely on retrieval strength and missed that at the very start of a course the trade-off runs the other way.\" (feedback-ela-chat-2026-09-24/REGISTER.md:14).",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Answer leaks come from every learner-facing line, not only wrong-answer feedback, so check praise, nudges, instructions and the guide's own turn as well.",
   "kind": "measured",
   "found_by": "A live walkthrough and an external audit found answers handed over by praise, nudges and instructions across four lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "15",
     "quote": "praise / nudges / instructions hand over the Step 3–4 answers"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/PR-BODY.md",
     "lines": "5",
     "quote": "Answers no longer handed over by nudges, praise, instructions or Scout's part"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "49",
     "quote": "before any miss is even required"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1,
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check for leaks mechanically: no hint may contain an answer word from its own marking criterion, and no wrong-answer reply may contain a word only the key carries.",
   "kind": "adopted rule",
   "found_by": "An item-statistics review method and a class sweep after an external audit found many leak sites.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
     "lines": "174",
     "quote": "Methodology: collect exemplar/answer words (> 4 characters, meaningful) from each criterion's `requirement` field; check whether those words appear in the same criterion's `hint` or `second_hint` text."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md",
     "lines": "175",
     "quote": "fix = printed-only rewrite of the wrong reply so it names no word only the key carries"
    }
   ],
   "against": "Over-strict leak checks can withhold useful hints: \"Withholding it was a false positive that left a child on their THIRD miss\" (peter-pan-standing-2026-09-11/readiness-2026-09-16/pr263-merge/RED-REGISTER.md:27).",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test leak detectors for false positives too: counting the marking criterion's own framing words as answer words withheld a hint a learner needed.",
   "kind": "measured",
   "found_by": "Adjudication of a test change after a merge altered which hint a learner received.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/pr263-merge/RED-REGISTER.md",
     "lines": "24",
     "quote": "ours' `leakedWords` flags `[\"reason\",\"any\"]` on that rung; staging's returns `[]`."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/pr263-merge/RED-REGISTER.md",
     "lines": "27",
     "quote": "Withholding it was a false positive that left a child on their THIRD miss"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a generated reply fails a check, fall back to the authored text verbatim instead of regenerating, because a regeneration that avoided the flagged words introduced a factual error about the text.",
   "kind": "measured",
   "found_by": "A live judge probe with hint-echo answers on open items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "57",
     "quote": "The replacement introduced a factual error."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "63",
     "quote": "The backstop should fall back to the authored hint verbatim rather than regenerating on this path"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Generated praise must reflect what the learner actually said; praise that credits a detail the answer never mentioned misleads them about what was right.",
   "kind": "measured",
   "found_by": "A live judge probe with a plausible wrong answer.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "81",
     "quote": "The praise attributes a correct story fact to the child that the child never said."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "85",
     "quote": "or directly reflect the child's stated idea"
    }
   ],
   "against": "Intermittent, not systematic: \"This run's praise misread. Again non-deterministic.\" (same file:83).",
   "adds_to_existing": [
    11
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Evaluate a judge's feedback text separately from its verdict, since every score can be right while the coaching text misreads the source or the answer.",
   "kind": "measured",
   "found_by": "A 16-call live judge probe across four open items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "37",
     "quote": "All 16 bands are correct. No held pass and no passed hold found. Two coaching-text issues found on p19, both in the `swyk-dialogue` node."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "97",
     "quote": "These findings are coaching-text quality failures, not scoring failures."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Probe every judged item with a fixed set of answers: a full pass, one criterion only, a plausible wrong answer, the hint echoed back, a misspelled right answer, keyword nonsense, a valid synonym, a fluent wrong answer and the answer's negation.",
   "kind": "adopted rule",
   "found_by": "Judge-probe method and proposed verification packages; a closing-question spec showed a negation passing a string match.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
     "lines": "10",
     "quote": "Four variants per item: full-pass, one-criterion-only, plausible wrong, hint-echo."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md",
     "lines": "8",
     "quote": "compare correct meaning with a typo, nonsense resembling a keyword, valid synonym, fluent wrong answer, partial answer and contradictory premise"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "68",
     "quote": "Never string-match. Matching on “broken” passes “trust can never be broken,” which is the opposite of the answer."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    37,
    10
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Define one acceptance rule per answer; when the rubric, accepted forms, word bank and hints each define it separately, they drift apart.",
   "kind": "measured",
   "found_by": "An external audit found disagreeing acceptance rules on blanks in several lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "18",
     "quote": "The mood blank has three acceptance rules that disagree"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "56",
     "quote": "Four rules for the final blank disagree"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "57",
     "quote": "but the reading-notes Step-3 hunt's accept list omits \"evil\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat the same piece of evidence the same way everywhere in a course; a sentence accepted on one page and rejected on another confuses what counts.",
   "kind": "measured",
   "found_by": "External audits of a reference lesson and of four other lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
     "lines": "20",
     "quote": "one sentence accepted on one page, rejected on another (magician)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "67",
     "quote": "is rejected as evidence on p16"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Every claim a lesson makes about its source must be true to it, not just its quotes: model write-ups, feedback, stems and answer keys paraphrased the text wrongly.",
   "kind": "measured",
   "found_by": "An external audit and a live walkthrough of four lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "25",
     "quote": "\"The children could not sleep and lay wide awake\" is wrong — only John lies wide awake"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "120",
     "quote": "Five feedback/reveal lines contradict the story"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "10",
     "quote": "find-it key teaches a fact not in the story (London bedtime/rules/grown-ups)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    59,
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Source design documents and knowledge bases can be wrong about the text, so check every quote, model answer and definition they supply against the text before copying it verbatim.",
   "kind": "measured",
   "found_by": "Criteria audit, curriculum audit and an external audit each found design-supplied content that the text does not support.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "71",
     "quote": "The KB-listed 'fire burned low' clue is NOT used because the story does not contain that line"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "41",
     "quote": "the Modelling Moment HTML itself has \"because they are bored\" (not in the story)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "153",
     "quote": "is PRESCRIBED by the PP3 design DOCX"
    }
   ],
   "against": "Where named designs govern, prescribed strings were kept pending a ruling: \"a design-prescribed string is NOT changed — say so in notes\" (feedback-live-walk-2026-09-30/BUILD-SPEC.md:4).",
   "adds_to_existing": [
    43,
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A definition gives the word's general meaning in the word's own grammatical form, without using the word itself or borrowing details from the text where it appears.",
   "kind": "adopted rule",
   "found_by": "An external audit found a definition carrying the text's situation; two reviews found a word-form mismatch; a review profile checks for circular definitions.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "83",
     "quote": "'Furious' is defined wrongly on every visible passage ('very fast and full of anger')"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/PP-STANDING.md",
     "lines": "34",
     "quote": "is a word-form error"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md",
     "lines": "79",
     "quote": "| D4.17 | Distinct target words | PASS | Only 1 word; definition uses \"dangerous\" (different word); morph gloss uses \"menace/harm\" (different words). No circular definition. |"
    }
   ],
   "against": "The flagged definition was prescribed by the governing design and reverted to it pending a ruling (feedback-inceptbench-2026-09-30/REGISTER.md:153).",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give each taught word and key idea one wording, used identically on the card, glossary, feedback, goal and summary; different definitions or rules for one concept within a lesson confused learners.",
   "kind": "adopted rule",
   "found_by": "Checklist gate; a live walkthrough found three trait rules and two meanings for one word in a lesson.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "43",
     "quote": "One definition per word, verbatim everywhere"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "19",
     "quote": "three different trait rules; feelings keyed as traits; invented \"again and again\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
     "lines": "46",
     "quote": "Canonical hinge proposition per weak skill** propagated verbatim teach→CFU→review"
    }
   ],
   "against": "Verbatim reuse also spreads an error: \"'Furious' is defined wrongly on every visible passage ('very fast and full of anger')\" (feedback-inceptbench-2026-09-30/REGISTER.md:83).",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A word learners are asked to find in a text must actually occur in it, exactly or as a word-family form; otherwise the search becomes tapping highlighted lines.",
   "kind": "measured",
   "found_by": "A shipped search task whose key word was not in the passage; a baseline evaluation counted vocabulary items about words absent from their passages.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "100",
     "quote": "A taught key word must actually occur in the passage or the hunt degrades into glowing-line tapping"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/SUMMARY_AGENT.qmd",
     "lines": "99",
     "quote": "~53 vocab-not-in-passage"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check word-part splits and affix meanings against a rule-based reference, never intuition; teach only real parts, and words that don't split as word families.",
   "kind": "measured",
   "found_by": "Verification of authored word-part splits; reviews of affix glosses; a calibration log naming this the most frequent class machines could not catch.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "224",
     "quote": "5 of 23 authored splits wrong"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/PP-STANDING.md",
     "lines": "37",
     "quote": "(\"-ing means it is happening right now\" for enchanting / menacing, whose definitions are descriptive)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md",
     "lines": "265-266",
     "quote": "judgment across all 9 logged rounds (4 hits, the top-ranked residue class)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Teach a new word with examples from outside the text being studied, easier than the word itself, that don't reveal what happens in the text.",
   "kind": "adopted rule",
   "found_by": "Review profile criterion; a vocabulary example rewritten so it no longer told the ending; a live walkthrough found examples harder than the word.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md",
     "lines": "70",
     "quote": "| D4.6 | Examples beyond story | PASS |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21/index.html",
     "lines": "215",
     "quote": "The example no longer tells the ending"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "25",
     "quote": "same-ending examples harder than the word"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A taught word must appear in its text, recur in later lessons, and be assessed by use, not only by recognition.",
   "kind": "adopted rule",
   "found_by": "Criteria register, a validator count and a review profile.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "12",
     "quote": "A taught word appears at least twice in its own passage and is met again in a later authored lesson"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md",
     "lines": "71",
     "quote": "| D4.7 | Use not recognition | PASS |"
    }
   ],
   "against": "The recurrence check had exemptions: \"`validate-vocab-earned.mjs:198–220` explicitly exempts encapsulating words from own-passage/later-lesson recurrence rules\" (feedback-devfactory-2026-09-10/analysis-current-courses/G3-APPLICABILITY.md:24).",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Machine transcription mishears letter names and word fragments, so have a person listen to word-part clips and print affixes with a hyphen so they don't read as words.",
   "kind": "measured",
   "found_by": "Listen-QA transcripts of vocabulary clips and an external audit of an affix gloss.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/listen-qa-l4-l7-2026-09-24/G3-U1-L6/p2-word.txt",
     "lines": "5",
     "quote": "Mercy, written with an eye,"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "291",
     "quote": "Whisper mis-hears short morphemes"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "132",
     "quote": "the morpheme gloss writes \"the suffix ant\" without a hyphen (reads as the insect to a grade-3 student)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a word is broken into parts for pronunciation, voice each part as it sounds inside the word, in the same voice as the whole word, and check the joined sequence reads back as the word.",
   "kind": "measured",
   "found_by": "Read-back transcription of syllable clips after a ruling on how parts should sound.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "101",
     "quote": "\"pronounce the parts as parts of that word, not as individual parts\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "107",
     "quote": "the old three-piece set read back \"Manganese\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "123",
     "quote": "\"same voice for the pieces and the full word\""
    }
   ],
   "against": "An external audit disputed the resulting split: \"splits the word into two syllables instead of the correct three\" (feedback-inceptbench-2026-09-30/REGISTER.md:65).",
   "adds_to_existing": [
    2
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Inventory what each text assumes and adds, tied to the words that carry each item, and make sure every assumption is covered by an earlier text or stated entry knowledge, with no forward references.",
   "kind": "adopted rule",
   "found_by": "Knowledge inventory for a four-text unit and a cross-lesson continuity review.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md",
     "lines": "8",
     "quote": "Proposed adds / assumes per text, with carrying spans."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md",
     "lines": "95-96",
     "quote": "Compounding check: every text's assumes are covered by earlier texts' adds or entry"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md",
     "lines": "32",
     "quote": "### L5 characters and places — introduced before first use?"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18,
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Order a set of texts so each builds on the knowledge the last added, and end with a transfer text that keeps the schema but changes the surface, avoids famous staple examples and teaches nothing new.",
   "kind": "adopted rule",
   "found_by": "Design of a four-text unit with an unseen capstone text.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "17",
     "quote": "Ladder note: the ramp is primer -> build -> deepen -> transfer-neighbor."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md",
     "lines": "83",
     "quote": "Adds (cluster 1, transfer rung -- reduced topical overlap, same schema):"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/passage.md",
     "lines": "14",
     "quote": "P6 (an invented flood-plain farm town, not the curriculum-staple Nile/Mississippi delta)"
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
   "statement": "Readability formulas don't see conceptual load, so judge a text's difficulty also by the new knowledge it carries, and pre-teach the words that carry that knowledge rather than swapping them out to hit a number.",
   "kind": "measured",
   "found_by": "Difficulty notes for four texts: the text that measured easiest was the harder step.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "18",
     "quote": "measures lexically simpler than the primer (FK 3.5) because its sentences are short; its"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "19",
     "quote": "step up is carried by conceptual load (five new knowledge ids, two taught terms) and by"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "44",
     "quote": "REVISE cannot swap payload words out"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18,
    23
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a story that carries real-world knowledge, list and check every world claim at the precision the grade needs, mark invented particulars as fiction, check invented numbers that embed real rates, and confirm characters' misconceptions are clearly refuted.",
   "kind": "adopted rule",
   "found_by": "A factuality ledger built during authoring of four informational stories.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "18",
     "quote": "Verify each at that precision (short causal statements, qualitative magnitudes) -- not at"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "113",
     "quote": "Where an invented number embeds a real-world RATE or MAGNITUDE claim, it"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "115",
     "quote": "Character misconceptions are deliberately planted and refuted; verify the REFUTATION is clear,"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    59,
    61
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check the knowledge model a sequence of texts builds as a whole, not only its separate claims, because individually true steps can still misteach in sequence.",
   "kind": "adopted rule",
   "found_by": "Factuality ledger protocol for a unit's causal model.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "96",
     "quote": "QC should sign the MODEL, not only the atoms: confirm no step of the chain as sequenced across texts 01->04 misteaches the standard account."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't let a text or a character's absolute statement over-generalize: check that no reader-facing line claims 'every' or 'never' where only some cases hold.",
   "kind": "adopted rule",
   "found_by": "Factuality protocol and a film script's production notes.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "72",
     "quote": "it does NOT overgeneralize to \"every river builds a delta.\" Verify no reader-facing overgeneralization."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "120",
     "quote": "Stance/rhetoric riding a character voice is not a taught universal"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "41",
     "quote": "Do not claim that all London had no cars or electricity."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep a lesson's key idea whole as designed, because later lessons ask learners to transfer it and a halved idea leaves a later question pointing at something the learner never met.",
   "kind": "measured",
   "found_by": "A curriculum adherence audit compared served lessons with their designs and with a later unit's transfer questions.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "67",
     "quote": "Cross-course dependency: WITW L11 Use it (PR #613) asks \"Where else have you seen a setting set the rules and the mood? Think about Peter Pan.\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "167",
     "quote": "WITW L11/L14 Form B now point at exactly the two ideas L4 and L7 fail to land"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "224",
     "quote": "Picking our four Name-it sentences without those two ideas leaves WITW pointing at content the child never met"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before removing a component, check what background knowledge only it supplied.",
   "kind": "measured",
   "found_by": "Curriculum audit traced the consequence of cutting a component.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "73",
     "quote": "the child would meet no old-London context at all"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check facts for consistency across the lessons of a sequence, not only within each lesson.",
   "kind": "measured",
   "found_by": "A cross-lesson continuity review found a location placed differently in two consecutive lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md",
     "lines": "67",
     "quote": "## MINOR-1 — Mermaid Lagoon geographical inconsistency"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md",
     "lines": "84",
     "quote": "This is a factual story-world inconsistency."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A lesson's key idea must come back in later lessons as something learners produce from memory, not something restated to them, and a later lesson that reuses it asks for it as already known.",
   "kind": "adopted rule",
   "found_by": "A closing-questions design spec (spaced retrieval rated well evidenced in its evidence table) and an analysis of a shared idea across units.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "118",
     "quote": "recur as something the child is asked to produce, not something restated at them"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "119",
     "quote": "If a threshold sentence appears once and never again, we have taught a slogan."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-ela-chat-2026-09-24/DEEP-READ-2026-09-24.md",
     "lines": "33",
     "quote": "provided L6 *asks for it as known* (Form B \"Think about Aladdin\", as L13 does) rather than introducing it as new"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Hide what learners must recall before they produce it, because producing it with the model still on screen is copying, not recall.",
   "kind": "adopted rule",
   "found_by": "Closing-questions spec; later encoded in a mutation-tested validator.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "54",
     "quote": "The sentence must not be visible when the child produces it."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md",
     "lines": "104",
     "quote": "sentence not printed"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Close a lesson with three moves on one idea: name it, find where it works in this text (asking when, not what), then use it beyond the text, with support fading and never returning.",
   "kind": "adopted rule",
   "found_by": "A closing-questions design spec adopted for every lesson.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "17",
     "quote": "Name it · Find it here · Use it."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "80",
     "quote": "The slots must ask when, not what."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "109",
     "quote": "Support fades and never returns. Maximum at Q1, a frame at Q2, nothing at Q3."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask learners to connect to another text only when a specific earlier text can be named in the question; otherwise ask for a prediction framed by the idea.",
   "kind": "adopted rule",
   "found_by": "Closing-questions spec, written against a transfer question asked before learners had texts to connect.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "102",
     "quote": "Rule of thumb: use Form B only when you can name the prior text inside the question. If you cannot name it, use Form A."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mark a prediction on whether the learner used the idea, not on whether the prediction comes true.",
   "kind": "adopted rule",
   "found_by": "Closing-questions spec.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "104",
     "quote": "Mark on whether the rule was used, not on whether the prediction turns out right."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    10
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Set a vocabulary floor: treat an answer in weaker words than the text supplies as unfinished and push once for the text's stronger word.",
   "kind": "adopted rule",
   "found_by": "Closing-questions spec.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "83",
     "quote": "Do not accept an answer in weaker language than the text supplies."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Set a target success rate for each question and read deviations as design faults: near everyone should name the idea, most should find it.",
   "kind": "adopted rule",
   "found_by": "Closing-questions spec citing high success in guided practice as well evidenced.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "110",
     "quote": "Success gradient: about 100%, about 80%, no key. If children are failing Q1, it is built wrong. If nearly everyone aces Q2, it is too easy to be worth asking."
    }
   ],
   "against": "Outcome rates were not auditable from the artifacts: CRITIC.md line 29 calls learning outcomes out of scope.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "State the evidence behind each design principle honestly, separating well-evidenced findings from frameworks and from weakly supported practices.",
   "kind": "adopted rule",
   "found_by": "The evidence-status table of a closing-questions spec.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "147",
     "quote": "So that nothing in this spec is defended on a stronger basis than it deserves."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
     "lines": "171",
     "quote": "There is no good evidence that saying something in unison builds durable knowledge."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A question asked before reading improves learning of what it asks about but hardly anything else, so aim it at the lesson's most important goal.",
   "kind": "external research",
   "found_by": "Primary-source check of research cited in an external review: King-Shepard et al. 2025, DOI10.1007/s10648-025-10075-7; St. Hilaire, Chan & Ahn, DOI10.3758/s13423-023-02353-8.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "37",
     "quote": "The publisher confirms **g=.66 for prequestioned information and g=.01 for other information**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "43",
     "quote": "The **g=.54 targeted / .04 general** estimates are confirmed (k97/91)."
    }
   ],
   "against": "\"Do not predict a .66 effect for Grade3, general transfer, or a particular tap-to-commit interface.\" (same file:39); the child-specific targeted estimate was .22 versus adults' .62 (same file:43).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Frequent inferential questions during reading can cut young readers' recall of the rest of the story, so keep mid-reading questions sparse, at natural boundaries, and measure whole-story recall when changing them.",
   "kind": "external research",
   "found_by": "Primary-source check of Van den Broek et al. 2001, DOI10.1037/0022-0663.93.3.521, cited in an external review.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "29",
     "quote": "The quoted **.30 control → .07 during-reading** result is Grade4 recall of **untargeted information**, not overall comprehension."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "31",
     "quote": "**Design conclusion:** frequent unsupported interruptions can be costly for younger readers."
    }
   ],
   "against": "\"This does not establish a non-negotiable ban on every mid-text check\" (same file:31); after-reading questioning was also worse than control (.16 versus .30, same file:29).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When text or a model answer is revealed progressively, reveal whole words or chunks with synchronized explanation rather than slow letter-by-letter tracing.",
   "kind": "external research",
   "found_by": "Primary-source check of Fiorella & Mayer 2016 (DOI 10.1037/edu0000065) and Ram & Zhao 2022 (https://synteraction.org/assets/files/Ram-A-et-al-2022-Does-Dynamically-Drawn-Text-Improve-Learning-Investigating-the-Effect-of-Text-Presentation-Styles-in-Video-Learning.pdf).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "11",
     "quote": "Transfer benefits were d=.58 for low-prior-knowledge students seeing the whole instructor draw, and d=.35 with a visible hand."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "19",
     "quote": "Whole-word appearance beat tracing on recall in Study1, d=.97."
    }
   ],
   "against": "Studies used adults and non-reading tasks: \"The paper does not require a mascot paw or establish that text appearing without one fails.\" (same file:13).",
   "adds_to_existing": [
    52
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check a cited study's population, task and contrast before turning it into a design rule; literature effect sizes justify a direction, not a predicted effect for your own learners.",
   "kind": "adopted rule",
   "found_by": "A research-boundary review of an external content review's citations, and an adversarial critique of a course improvement dossier.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
     "lines": "5",
     "quote": "The review contains useful ideas, but its **mandatory visible paw**, **universal after-reading-only rule**, and **feedback timing/size claims** exceed the evidence."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/V2_MONSTER_DOSSIER.md",
     "lines": "176",
     "quote": "justify DIRECTION not a v2 number"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "What the worked example models must match what learners then do: the same step names, frame, and number and kind of evidence across the model, the guided turn and independent work.",
   "kind": "measured",
   "found_by": "A value analysis, a step-label detector that found another shipped mismatch, and an external audit.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md",
     "lines": "23",
     "quote": "so what is modeled matches what is asked."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAP-CLOSURE-PLAN-2026-09-15.md",
     "lines": "46",
     "quote": "The detector's census found one more SHIPPED defect of the class: L5 p16 `youdo-clue-hunt` \"Step 2: Find the clues\" vs the model's and the we-do's \"Look for clues\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "114",
     "quote": "The we-do write-up frame has only one quote blank, while the I-do models two pieces of evidence and the you-do (p16) asks for two"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a worked example each step must add something; a 'what I know' step that repeats the conclusion never demonstrates the move it teaches.",
   "kind": "measured",
   "found_by": "Found independently by an external audit and a live walkthrough.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "24",
     "quote": "so the model never demonstrates the step it teaches"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "14",
     "quote": "model's \"I know\" repeats the conclusion"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A worked example must obey the lesson's own definitions, and its stated reasons must support its verdicts.",
   "kind": "measured",
   "found_by": "External audits of a reference lesson and four other lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "53",
     "quote": "The lesson defines a trait as repeated action, not a passing feeling"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
     "lines": "21",
     "quote": "a rejected think-aloud candidate whose aside argues for it"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A worked example should weigh plausible wrong options aloud and say why each is rejected, say which evidence it keeps when it finds more than it uses, and vary how many pieces it uses.",
   "kind": "adopted rule",
   "found_by": "A review profile criterion and a content review of a reference lesson.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md",
     "lines": "25",
     "quote": "| D1.10 | Model the hard part | PASS | States 4-7 show 4 plausible-but-wrong clues each weighed and rejected with genuine reasoning before the strongest is named |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-content-review-2026-09-20/REGISTER.md",
     "lines": "14",
     "quote": "Modeled answer must SHOW the choice when more clues are found than written"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-content-review-2026-09-20/REGISTER.md",
     "lines": "16",
     "quote": "Avoid modeling \"always exactly two\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Independent practice must not pre-mark candidates, state how many to find or name where to look; doing so turns it back into guided practice.",
   "kind": "measured",
   "found_by": "A curriculum adherence audit compared served independent tasks with their designs.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "47",
     "quote": "L6 p16/step3 hot_text, 8 glowing segments, \"Tap the three clues ... Not all the glowing clues are useful\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "135",
     "quote": "the Zoom MCQ pre-names the evidence region and undoes the open hunt"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt",
     "lines": "31",
     "quote": "usually by clicking the evidence in the shown passage (click-to-highlight) rather than choosing from options"
    }
   ],
   "against": "Whether a pre-glow-free hunt is possible was an engine question, not content (same REPORT.md:48).",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Model every task type before learners do it alone.",
   "kind": "measured",
   "found_by": "A gap register and value analysis found a judging task met cold in independent work.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "33-34",
     "quote": "child the six-statement judging task cold"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md",
     "lines": "36",
     "quote": "Refine arrives unmodeled"
    }
   ],
   "against": "Mitigated in that case because the task was objective with a retry ladder (GAPS-2026-09-11.md:34-35).",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every skill a gate tests must be practised before the gate.",
   "kind": "measured",
   "found_by": "A course-level structural screen of a practice pool.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/FEEDBACK_RESPONSE.md",
     "lines": "167",
     "quote": "layer has **zero main-idea (KCT1) drill and zero inference (KCT5) drill**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/FEEDBACK_RESPONSE.md",
     "lines": "168",
     "quote": "So a student practicing in this layer gets no repeated main-idea or"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep teaching checks separate from assessment: in-lesson checks give feedback but don't gate, and a later assessment carries the mastery gate.",
   "kind": "adopted rule",
   "found_by": "A gating restructure of a live demo unit after a decision not to conflate teaching with assessment.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
     "lines": "134-135",
     "quote": "conflated): l0-l3 are now non-gating formative"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/publish/README.md",
     "lines": "24",
     "quote": "Teaching checks are scored for immediate feedback but do not gate lesson progression; only the"
    }
   ],
   "against": "Elsewhere every check gates: \"No trap (child can always proceed by doing the work) and no leak (cannot proceed without it)\" (AlphaRead-QC-Checklist-v2-2026-09-04.md:126).",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A first check that opens a new knowledge unit can activate prior knowledge without blocking progress.",
   "kind": "adopted rule",
   "found_by": "A recorded renderer ruling for knowledge-building unit openers.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "129",
     "quote": "that first check activates and does not gate"
    }
   ],
   "against": "Scoped narrowly in the same row: every later check in the lesson still gates, and the rule applied to one grade only (same line).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Don't ask the same question twice in a row on consecutive pages.",
   "kind": "measured",
   "found_by": "A visual side-by-side of every first beat across five lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-24/FINDINGS.md",
     "lines": "24",
     "quote": "**The same question is asked twice in a row.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "While learners read, show only the text: questions come after the reading, the reading scaffold disappears when a question appears, and learners can move back freely.",
   "kind": "adopted rule",
   "found_by": "A content review of a reference lesson, encoded as criteria.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "110",
     "quote": "Only the passage on screen during reading; the question appears after the timer/read-aloud ends and the child clicks next"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "111",
     "quote": "Scout's reading commentary is a scaffold for the TEXT; it disappears when a quick-check question is on screen"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "7",
     "quote": "Lack of free movement around the book is one of the major drawbacks of not having a physical book"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26,
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Checks during reading should target cause and effect and the details the lesson builds on later, not low-leverage details.",
   "kind": "adopted rule",
   "found_by": "A content review of a reference lesson, encoded as a criterion and audited on another lesson.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "113",
     "quote": "Quick-checks mix cause-and-effect pickup with pointers at the key details the lesson focuses on later; no low-leverage detail questions"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "9",
     "quote": "They need to be a mix of ensuring students can pick up the cause and effect in the text"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check that each question's real demand matches the skill being practised; a locate question that needs inference, or a stem asking for the reason the text gives when it gives none, mis-tests the skill.",
   "kind": "measured",
   "found_by": "A content review and two independent item reviews of the same item.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "28",
     "quote": "This involves inference."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "61",
     "quote": "but the story never states a reason"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
     "lines": "258",
     "quote": "Either way the correct answer should be statable with a single-sentence verbatim pointer."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep what the text says apart from what the reader infers: inferences never sit in the evidence slot and never go inside quote marks.",
   "kind": "adopted rule",
   "found_by": "Criteria register and external audits that found quote marks around invented or inferred words.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "72",
     "quote": "Inferred mood words (gloomy, enchanting, etc.) live only in the 'I know' step, never inside 'The text says'"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
     "lines": "14",
     "quote": "quote marks around words the writer never wrote"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "113",
     "quote": "puts quotation marks around the model's own inferential words"
    }
   ],
   "against": "A validator in the same system required quote marks around a model inference, recorded as \"is a CONTRADICTION, not a fix\" (feedback-inceptbench-2026-09-29/REGISTER.md:57).",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A summary cloze blanks the causal links of what was learned, not incidental detail or connective words, and uses distractors that were true earlier but not now to test whether learners tracked change.",
   "kind": "adopted rule",
   "found_by": "A curriculum's lesson-component specification and the derived criteria register.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt",
     "lines": "20",
     "quote": "“true-earlier-but-not-now” distractors test that the child tracked how things changed"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "26",
     "quote": "exactly four blanks on the links of the mental model, bank of 6, answers text-true, no connective blank"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Name strategy steps in words that work on any text, not app mechanics, and frame the strategy as the learner's own tool.",
   "kind": "adopted rule",
   "found_by": "A content review of a reference lesson and a review profile criterion.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "21",
     "quote": "because ‘find’ captures what they will need to do in any text (not just on this app)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-A-D1-D4.md",
     "lines": "98",
     "quote": "**Rule cited:** D1.28 — \"Every strategy is explicitly framed as 'yours to use when the text gets hard', or the child treats it as a teacher-only activity.\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Ask for two different pieces of evidence to support a claim, since one quote only shows the learner can copy.",
   "kind": "adopted rule",
   "found_by": "Value analysis of a redesigned independent task.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md",
     "lines": "20-21",
     "quote": "child can copy; two different quotes prove the claim is supported"
    }
   ],
   "against": "The second quote is partly transcription labour and adds minutes (same file:32-35).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Follow locating evidence with a task that builds the concept, such as judging statements some of which the text contradicts, because locating alone leaves the concept unbuilt.",
   "kind": "adopted rule",
   "found_by": "Value analysis of a redesigned lesson.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md",
     "lines": "10-11",
     "quote": "evidence located, concept"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L6-VALUE.md",
     "lines": "12",
     "quote": "that is retrieval PLUS falsification"
    }
   ],
   "against": "The value claim was structural, not measured: \"NOT measured learning.\" (same file:4).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Put scaffolds such as prompts on what to look for on practice items only, never on assessment items.",
   "kind": "adopted rule",
   "found_by": "A copied reference pattern recorded in a parity plan.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/PARITY-PLAN-2026-09-14.md",
     "lines": "12",
     "quote": "practice pages only, never assessments, #488"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Show feedback right at the answer it responds to, and keep the source visible whenever feedback says to look back.",
   "kind": "measured",
   "found_by": "Checklist gates and a visual pass that found feedback far from the tapped line.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "103",
     "quote": "Wrong-answer reply renders directly under the tapped option, not below the list"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md",
     "lines": "46",
     "quote": "The feedback is right; its position is not where the child's eyes are."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep feedback short (about 40 words, 60 at most), at or below the learner's reading level, and keyed to the misconception behind each wrong option.",
   "kind": "adopted rule",
   "found_by": "Checklist gate; a lens fixed feedback that ran over 40 words in a live unit.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "71",
     "quote": "≤40 words target / 60 hard cap"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/publish/README.md",
     "lines": "55",
     "quote": "≤40-word misconception-keyed feedback"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When learners are let through after the allowed tries, say they are moving on and never dress it up as success; an honestly labelled final example is different from a hint that hands over the answer.",
   "kind": "adopted rule",
   "found_by": "Checklist gate and an applicability analysis of answer-supplying hints.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "130",
     "quote": "Release after N tries is named as moving on, never dressed as a win"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/G3-APPLICABILITY.md",
     "lines": "23",
     "quote": "These are pre-reveal answer-supplying hints, distinct from an honestly labeled final example."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Listen to every generated audio take and check both the words and the start: takes dropped words, and clips whose transcripts matched still had first words far quieter than the rest.",
   "kind": "measured",
   "found_by": "Listen-QA on re-cut clips and on a full lesson (55 clips).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/ROUND-RESULT.md",
     "lines": "21",
     "quote": "L6 p15 first take dropped \"then she would have to find another way\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-listen-qa.md",
     "lines": "19",
     "quote": "| Onset findings (WEAK ATTACK) | 13 |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-listen-qa.md",
     "lines": "220",
     "quote": "the first word's attack in the 60ms after that silence falls 25–74dB below the clip's own mean"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "On-screen text and its narration should match word for word with nothing spoken that isn't printed, and a missing clip should mean silence plus captions, not a substitute voice.",
   "kind": "adopted rule",
   "found_by": "Checklist gates and codebase rules.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "79",
     "quote": "audio\\_of \\= sha256 of the spoken text for every clip; zero mismatches"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "84",
     "quote": "Every measured voiceover mark must locate inside the prose displayed on the same page"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "85",
     "quote": "a missing clip means silence + captions, never browser TTS"
    }
   ],
   "against": "A recap narration spoke unprinted sentences and was accepted by precedent: \"wrap-steps-heading voiceover speaks 3 sentences not printed on p21\" (peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-C-D7-D8-D10-D12.md:40).",
   "adds_to_existing": [
    2
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Narration must not compete with the learner: don't auto-read a question before the learner has read it, and never play two audio sources at once.",
   "kind": "adopted rule",
   "found_by": "Checklist gates written after observed overlapping playback.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "90",
     "quote": "Stem audio plays only on demand, never autoplayed before the child reads"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "87",
     "quote": "No overlapping playback anywhere"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Sweep learner-facing text for leaked authoring markup and placeholders, such as heading tokens, formatting marks, HTML entities, draft metadata or codes standing in for a passage.",
   "kind": "measured",
   "found_by": "Content-coherence sweeps and render audits of live courses.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FIX_LIST.md",
     "lines": "114",
     "quote": "Both leak the literal authoring token `HEADING:` into student-visible body text."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/SUMMARY_AGENT.qmd",
     "lines": "138",
     "quote": "144 items rendered `&#x27;`/`&amp;#x27;`/`&quot;` literally in feedback."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "434",
     "quote": "passage text is literally the CCSS code string `RI.3.8`. No passage. Unanswerable."
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
   "statement": "Nothing in a lesson may preview content the learner has not reached yet: not the text, feedback, checks, pictures or introductory media.",
   "kind": "adopted rule",
   "found_by": "Checklist gate, a content review of a reference lesson's opening image, and an external audit of a model inference.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "47",
     "quote": "No text, feedback, or check previews content the child has not reached"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
     "lines": "6",
     "quote": "The image is a bad one for the start of the story as it’s a spoiler for what will happen but mostly because it does not match what happens in the text on screen."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "85",
     "quote": "the inference states 'Peter is wounded' before that happens in the story"
    }
   ],
   "against": "Teasers are allowed: \"no spoilers of events but teasers\" (feedback-aladdin-2026-08-25/feedback-text.txt:4).",
   "adds_to_existing": [
    3,
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Media about a text must be accurate about it, with no character labels or general claims the text doesn't support.",
   "kind": "adopted rule",
   "found_by": "A content review of introductory videos, encoded as a criterion; a film script's production notes.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "109",
     "quote": "Videos must be factually accurate about the text; Aladdin, Peter Pan and Toad are NOT heroes and must not be called that"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "79",
     "quote": "No hero/villain labels. No children flying out, parental decision or ending. Do not narrate the assessed London/Neverland mood words or complete their inference for the learner."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Change a video and everything tied to it together, including its checks, captions and transcript, and keep checks in the lesson rather than burned into the video.",
   "kind": "adopted rule",
   "found_by": "Planning a film replacement against the installed film contract.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "58",
     "quote": "Replacing only its MP4 would leave that check and the five short transcript segments mismatched."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "53",
     "quote": "Pauses, response UI and feedback belong to the app, not burned into the MP4."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In explanatory media show one main visual action at a time with the spoken concept and its referent together, add no decorative or invented on-screen text, and keep characters identical across shots.",
   "kind": "adopted rule",
   "found_by": "Production rules drawn from comments on a reference film.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "81",
     "quote": "One main visual action at a time. Spoken concepts and their referents appear together. Avoid eye-catching background motion during explanations."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "72",
     "quote": "No decorative lists, invented text or unspoken recap on notebook pages"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
     "lines": "69",
     "quote": "Lock cast sheets, scale, wardrobe, props and room geography"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    21,
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Generated images of people must not look machine-made, because learners who spot 'fake AI' disengage; prove the check tells real cases apart and use several independent reads on near-photoreal faces.",
   "kind": "adopted rule",
   "found_by": "A ruling on video style followed by a control run of a vision check whose verdicts flipped between runs.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "4",
     "quote": "I never want a student to declare 'Fake AI video'"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "42",
     "quote": "Runs 1 and 2 disagreed on vf07 (FAIL → note), vf08 (note → FAIL) and vf10 (note → FAIL)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "45",
     "quote": "now requires three independent reads with majority rule on film frames and near-photoreal humans."
    }
   ],
   "against": "The threshold stayed provisional pending a person's check (same file:70-72).",
   "adds_to_existing": [
    22,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Confirm any visual flag on the full-size, settled frame before filing it, because thumbnails, mid-animation frames and the checking tool's own scrolling produced false defects.",
   "kind": "measured",
   "found_by": "Visual reviews of contact sheets and screenshots across four lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "48",
     "quote": "Not defects (each re-read at full size; do not re-raise):"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "68-70",
     "quote": "the background paragraph is there (thumbnail artifact)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md",
     "lines": "93",
     "quote": "The jump was the harness's own scrolling."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before reporting that something does nothing, observe the whole page and wait out its designed timers.",
   "kind": "measured",
   "found_by": "A filing gate written after 'does nothing' claims turned out to be feedback shown elsewhere.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "134",
     "quote": "three \"does nothing\" claims were feedback in the other column"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "13",
     "quote": "Wait out the designed timer"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Before filing a defect, separate 'the specified step is wrong', which is a design question, from 'this instance is weak', which is a content defect.",
   "kind": "adopted rule",
   "found_by": "The filing gate of a combined human and AI QC checklist.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "15",
     "quote": "a specified step is not a defect; keep \"the step is wrong\" apart from \"this instance is weak\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A check covers only what it collects, so make every checker list what it read and treat anything outside its reach as unchecked.",
   "kind": "measured",
   "found_by": "A semantic judge, an asset validator and an external audit script each missed defects in fields they never read.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "244",
     "quote": "MCQ-only collection missed narrated-text breaches twice"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md",
     "lines": "29-30",
     "quote": "sees this because the path is derived at runtime, not authored (validate-audio-refs walks"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "139",
     "quote": "The audit script (audit.py) never reads think_aloud.states[].search / we_do.search fields at all"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Confirm a cited check exists and actually ran before counting it; a check that was never built or never run is unverified, not passed.",
   "kind": "measured",
   "found_by": "A checklist correction pass and a stress test of a course quality report.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "288",
     "quote": "claims \"the new verbatim-fidelity ratchet in course-renderer\" landed"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "525",
     "quote": "Do not ship \"v1 PASS\" on an unrun check."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep checking-tool failures apart from content failures; a missing judge, a crashed transcriber and a shared output folder each produced false content failures.",
   "kind": "measured",
   "found_by": "Harness incidents recorded in a QC checklist and a gap-closure plan.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "230",
     "quote": "11 phantom FAILs cost a diagnosis round"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "84",
     "quote": "27 false positives cost a full pass to disprove"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "250",
     "quote": "a transcript finding and a dead process are no longer the same red"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every check run must state which version and which learner-facing surface it checked.",
   "kind": "measured",
   "found_by": "Walk logs filed as one version were of another; a student walk ran on a deprecated surface; a capture run returned near-identical screenshots.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "196",
     "quote": "Silence-by-design class (qa-must-converge): a check that cannot say what it"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "231-232",
     "quote": "this lane, baselines included, is therefore a read of the deprecated surface, not of the page the"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "86",
     "quote": "first capture run produced 30 near-byte-identical screenshots before this"
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
   "statement": "When the checking tool itself fails on the unchanged baseline, judge a change by the failures it adds over that baseline.",
   "kind": "measured",
   "found_by": "Walker drift against a new release; later rounds compared fail sets with the base build.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "135",
     "quote": "The L4 annotation slice adds ZERO failures over base (4 base-subset fails on the"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
     "lines": "60",
     "quote": "battery 10 fail vs staging 11 (strict subset)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A check that only compares counts invites rubber-stamping; make it list what was added or removed so people review names, not a number.",
   "kind": "measured",
   "found_by": "Census pins were bumped every round without checking the new items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "81",
     "quote": "the assertion only asks \"does the count match\", never \"is the"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
     "lines": "84",
     "quote": "review is of names, not a number."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Re-check every reported problem on the current version before fixing it, and apply feedback only to the course and lesson it was raised about.",
   "kind": "measured",
   "found_by": "Incoming reports that targeted stale builds; a visual report run before a fix deployed; a cross-course feedback miss.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "204",
     "quote": "2 ALREADY-FIXED, 2 NOT-REPRODUCIBLE on c056d3e"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-codex-visual-2026-09-07/REGISTER.md",
     "lines": "26",
     "quote": "Codex's reproductions ran before the chip-glue merge built."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "205",
     "quote": "a matching term found elsewhere (another course's accepted list, a sibling system) is DROPPED"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check a suggested fix before applying it.",
   "kind": "measured",
   "found_by": "An audit's suggested distractor was itself a correct use, and a demanded spelling change was not supported by the dictionary.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "11",
     "quote": "NOT the report's own suggestion (a plant nursery is a CORRECT use of the word and cannot be a wrong option in \"uses the word correctly\")"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L4-REVIEW-GAPS-2026-09-16.md",
     "lines": "98",
     "quote": "Merriam-Webster recognizes -ry as a form of -ery, so “must change to -ery” was unsupported."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-derive every number in a report from its primary source at write time and state its denominator.",
   "kind": "measured",
   "found_by": "Errors traced in round reports came only from copied numbers; a limited run was cited as the whole course.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "211",
     "quote": "5 errors, all inherited; zero freshly-derived claims wrong"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "540",
     "quote": "The headline `/tmp/audit_compliance.json` is a `--limit` run (6 tests / 91 items), not the full course."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Freeze one version for the length of a review, and hold everything else equal when comparing versions.",
   "kind": "measured",
   "found_by": "Internal review rounds voided by a moving build; side-by-side comparisons built on one base commit.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "200",
     "quote": "mid-flight main movement voided three internal rounds"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-22/ours-only.html",
     "lines": "31",
     "quote": "Both sides are the same staging commit 5d033ac1. The only difference is our work."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Close a finding only by re-running the check that found it on the current version, and don't treat a later run that fails to reproduce a failure as a fix.",
   "kind": "measured",
   "found_by": "Closure rules in a QC checklist and an unexplained audio interruption that a diagnostic run did not reproduce.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "213",
     "quote": "\"fixed in \\<commit\\>\" is not closure"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/book-driver/FINAL-CLAIM-AUDIT.md",
     "lines": "14",
     "quote": "trace04's natural 8.6-second end is nonreproduction, not a repair or acoustic acceptance"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/book-driver/ANNOTATION-AUDIO-DISPOSITION.md",
     "lines": "22",
     "quote": "No repeated run until green is justified."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Turn every defect a person finds into a class check that is shown to fire on the pre-fix content, sweep all content for that class, and keep a ledger of rejected lines so they cannot return.",
   "kind": "measured",
   "found_by": "A checklist rule; a class sweep after an external finding that caught the same tell elsewhere; a roadmap answering a complaint repeated over rounds.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "212",
     "quote": "Each human-found defect became a machine check the same cycle, born red"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "21",
     "quote": "L7 p3 vocab-form1 carried the same \", because …\" tell → fixed"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md",
     "lines": "146-147",
     "quote": "operationalizes \"if a reviewer already killed this line, it can"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A green gate is not a defect-free lesson; people found many issues on lessons whose gate was green, mostly ones visible only on the rendered page or in the language.",
   "kind": "measured",
   "found_by": "A calibration log of review rounds analysed for an automated-checks roadmap.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md",
     "lines": "22",
     "quote": "**green at review time** (`ROUNDS.md` \"26 findings landed on lessons whose"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/AUTOMATED-CHECKS-ROADMAP-2026-08-31.md",
     "lines": "55-56",
     "quote": "JSON/JSX text**, and the findings that keep recurring are ones only visible"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Most defects people find appear only after a sequence of actions, so static captures can't certify a lesson, and a judge that never saw the defect's screen proves nothing.",
   "kind": "measured",
   "found_by": "Calibration of a screenshot judge against known findings.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "159-160",
     "quote": "checkpoint-seeked capture this run did not take) and 6 are sequence-only or"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "181",
     "quote": "The judge passed a screen that never contained the defect's own UI, so this is NOT evidence the fix holds"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    47,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure a model judge by running it on known cases rather than estimating what it would say; its main failure was confident, repeatable fabrication.",
   "kind": "measured",
   "found_by": "A real run of a screenshot judge compared with an earlier by-eye estimate.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "185-187",
     "quote": "the opposite of the first session's optimistic manual stand-in (which"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "180",
     "quote": "confirmed STABLE across 5 independent calls"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "311",
     "quote": "is not incompleteness, it is confident wrongness"
    }
   ],
   "against": "It still surfaced new real findings: \"It DID surface two plausible genuine findings\" (same file:319).",
   "adds_to_existing": [
    35,
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "If a judged question fails most items because of a deliberate design, rewrite the question before using it as a gate.",
   "kind": "measured",
   "found_by": "A screenshot judge failed most pages of a lesson on an intentional layout.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "203",
     "quote": "**`task-dominance`: 24/30 pages fail**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
     "lines": "217-218",
     "quote": "layout choice has low information value as currently worded"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Have someone other than a check's author write its test cases, with expected outcomes fixed before measuring.",
   "kind": "measured",
   "found_by": "A detector that passed its author's controls was challenged with independently written cases.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/RESULT.md",
     "lines": "29",
     "quote": "The original visibility implementation passed its 48 controls but missed 10 of 18 independently authored cases."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/independent-observer/REVIEW.md",
     "lines": "7",
     "quote": "Eighteen fixture expectations were fixed in the independent script and written into `run-01/INTENT.json` before the first measurement."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    37,
    38,
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count only what a check actually observed: empty observations, duplicate cases and timeouts are incomplete rather than passes, and a verdict carries every unverified part with it.",
   "kind": "adopted rule",
   "found_by": "Evidence-gate tests for a QA runner and a verdict-wording correction.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/harness-2026-09-14.txt",
     "lines": "9-10",
     "quote": "test_empty_observations_are_not_success"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "44",
     "quote": "Therefore the verdict is **\"PASS-with-Caliper-unverified\"**, NEVER a bare \"PASS\"."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the judge, the acceptance cases and the evidence out of reach of whatever writes the fix; a second agent with write access to the same files is not independent.",
   "kind": "adopted rule",
   "found_by": "Design of an automated repair controller and a tool-reuse assessment.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/controller-2026-09-14/PLAN.md",
     "lines": "30",
     "quote": "Tier 1: independent acceptance files must be outside the worker's enforced writable boundary."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/tool-reuse-assessment-2026-09-14.md",
     "lines": "105",
     "quote": "Hashes are not protection against a writer who can alter both result and evidence consistently."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Replace a checking method only after a trial on the same frozen cases shows no new misses or false alarms and a measured gain; being newer is not evidence.",
   "kind": "adopted rule",
   "found_by": "A bounded assessment of reusing earlier QA tools.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/tool-reuse-assessment-2026-09-14.md",
     "lines": "42",
     "quote": "Tier 1: current requirements and immutable original evidence govern; timestamps and test totals cannot establish superiority."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/tool-reuse-assessment-2026-09-14.md",
     "lines": "95",
     "quote": "No additional misses or false alarms on protected cases, no lost obligations, and a measured benefit on the declared target are needed for replacement. Do not accept a faster probe that silently stops exercising hard cases."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A problem's absence from a later review doesn't show it was fixed, because reviews with different builds and scope can't be compared.",
   "kind": "measured",
   "found_by": "A recurrence gauge over seven historical review records (183 entries, 54 defect reports).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/RESULT.md",
     "lines": "53",
     "quote": "Reported repeated classes trigger detector inspection, but absence from a later report cannot establish a fix or a declining rate."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/recurrence/CLASSIFICATION-REVIEW-v3.md",
     "lines": "233",
     "quote": "Round coverage is incomparable. Absence of a class is not resolved, retested or improved."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep internal procedure names, developer-speak and generic assistant phrasing out of learner-facing text and check for them as their own class, since this was the complaint raised again most often across reviews.",
   "kind": "measured",
   "found_by": "A recurrence classification of review records: the class first raised in one review recurred in four later sections.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/recurrence/CLASSIFICATION-REVIEW-v3.md",
     "lines": "21",
     "quote": "| aladdin-followup | 2 | — | procedure_language |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/recurrence/CLASSIFICATION-REVIEW-v3.md",
     "lines": "34",
     "quote": "| eight-gaps | 5 | hint_disclosure | magic_word_use, morphology_accuracy, procedure_language |"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "67",
     "quote": "Zero instances of generic-assistant phrasing that reads as \"every AI app\""
    }
   ],
   "against": "The gauge itself warns that sections are not comparable (CLASSIFICATION-REVIEW-v3.md:5).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep a recorded order of authority among design sources and log every divergence: a lesson-specific design over a generic one, a dated ruling over an undated principle, a later ruling over an earlier one.",
   "kind": "adopted rule",
   "found_by": "A lesson built from a too-general spec; a QC checklist's authority note.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "296",
     "quote": "a dated ruling beats an undated principle; a later ruling beats an earlier one"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "91",
     "quote": "promoted 2026-08-25 after L4 was built a tier too general"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Classify incoming feedback before acting on it as a demonstrated defect, a compatible refinement, a change of direction or insufficient evidence, and don't let recency or confidence alone override an earlier decision.",
   "kind": "adopted rule",
   "found_by": "A decision baseline written after a review proposed a large change of direction.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/DECISION-BASELINE.md",
     "lines": "17",
     "quote": "| Demonstrated defect | A factual/content error or observed malfunction with a clear expected behavior, consistent with the agreed approach."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md",
     "lines": "24",
     "quote": "do not alternate between competing standards without recording which one governs"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Record what people explicitly liked about a lesson as protected criteria so later changes don't remove it.",
   "kind": "adopted rule",
   "found_by": "A content review praised a feature, which was then registered as protected.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "122",
     "quote": "The answer-becomes-dialogue-with-Scout pattern on wrong answers is explicitly liked — do not remove in any redesign"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/REGISTER.md",
     "lines": "72",
     "quote": "recorded so nobody \"fixes\" it away (no-churn)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Fidelity checks show a lesson matches its design, not that the design teaches well.",
   "kind": "adopted rule",
   "found_by": "A certification contract and a curriculum fidelity report stating their own limits.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md",
     "lines": "223",
     "quote": "A perfectly-transferred bad design passes every gate."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/PRIOR-curriculum-verification-2026-09-10.md",
     "lines": "3",
     "quote": "do not replace student text, regenerate media, or claim curricular approval from source equality or passing technical tests"
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
   "statement": "Every audit should say what it did not check, because closed-world checks only check what they were told to.",
   "kind": "measured",
   "found_by": "Green audits failed a real review; an audit critic listed modalities and authorities it never consulted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md",
     "lines": "288",
     "quote": "six green audits failed a real review because none of them asked"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/CRITIC.md",
     "lines": "7",
     "quote": "Why: what the child sees ≠ what the file holds."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "State how each claim was verified (walked by a person, full census, single probe, code test or still open) and never word it more strongly than that basis.",
   "kind": "adopted rule",
   "found_by": "A rules document tagging every rule with its evidence, and a facts sheet correcting overstated claims.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/RULES.md",
     "lines": "4",
     "quote": "**Confidence tags:** `[LIVE]` walked in the student app myself · `[CENSUS]` exhaustive"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "30",
     "quote": "state non-leakage as \"grep-verified per item,\" not \"machine-proven.\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Report generate-and-filter yields as the yield of a search, not as what the generator does in one try, and trace any headline score to its source before believing it.",
   "kind": "measured",
   "found_by": "Honesty review of a prompt-only generator and of an earlier model-training project's headline numbers.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/GENERATOR.md",
     "lines": "152-153",
     "quote": "But it is **NOT a K=1"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "55",
     "quote": "the \"99%\" was **cache + best-of-N**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "56",
     "quote": "(not the model generating); the \"28%\" was **four harness bugs**."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    65
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Confirm an improvement with the grader of record, and watch for 'fixes' that only dodge the check, because a gain measured under one judge vanished under the binding grader.",
   "kind": "measured",
   "found_by": "Re-examination of a claimed content lever carried over from an earlier project.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "52",
     "quote": "aptraining's \"real passages = 0.29→0.95 lever\" is **REFUTED**: that jump existed only under a discredited"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "53",
     "quote": "Gemini judge; on the binding grader it collapsed to 28% (DBQ 0%, MCQ_SET 0%, \"Gemini-judge artifact\"). The"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "54",
     "quote": "actual MCQ fix was the OPPOSITE — *removing* the stimulus so the grader's leak-probe is skipped (grader-gaming)."
    }
   ],
   "against": "The underlying lever survived in a narrower form: \"anti-leak/answerability is a real, construct-general item-quality lever\" (same file:58).",
   "adds_to_existing": [
    35,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Agreement between two teams counts as replication only if they worked independently.",
   "kind": "adopted rule",
   "found_by": "Re-examination of a claim that two projects had converged on the same finding.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "57",
     "quote": "The \"two teams converged\" is **WEAK** — it's one author importing AP findings onto grade-3, not independent replication."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    35
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Generators drift toward their usual grade and plausible-looking standard tags, so enforce the grade band and check each tag against the text and skill outside the generator.",
   "kind": "measured",
   "found_by": "A generation run for a higher grade and a genre-aware tag audit of 26 items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
     "lines": "38",
     "quote": "Told \"G5,\" generate-agents produced 17/20 items at RI.3.x (prior-pull)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "147",
     "quote": "(literary tag on a purely informational creature passage)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Tag content metadata only where the delivered content still matches the source, since tags copied from a stale snapshot are fabrication.",
   "kind": "measured",
   "found_by": "A standards backfill gated on overlap between source and live passages.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/SUMMARY_AGENT_G5.qmd",
     "lines": "39",
     "quote": "each Unit-2 item was tagged **only where the live passage still"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/SUMMARY_AGENT_G5.qmd",
     "lines": "44-45",
     "quote": "from the stale snapshot would be fabrication, so they stay uncoded and named."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63,
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Take reference values such as test norms from a cited table, never from a model's memory.",
   "kind": "measured",
   "found_by": "A predictor whose norm values had drifted to wrong anchors from pre-training.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md",
     "lines": "18",
     "quote": "RIT meaning free-floats on pre-training (wrong 200-210 / 208/214 anchors)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A predicted learning outcome must carry its status as a prediction in the data itself, and a proxy test is never reported on the real test's scale.",
   "kind": "adopted rule",
   "found_by": "Review of a predictor's output schema and a course's honesty guardrails.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md",
     "lines": "19",
     "quote": "is a **naked number** — no field carrying \"model PREDICTION, not measured outcome; no in-cohort pilot validated this; not proven growth\""
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/V2_MONSTER_DOSSIER.md",
     "lines": "107",
     "quote": "**A proxy stays a proxy.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report completion gains only paired with the same learners' accuracy on unseen items, and take a baseline before changing anything.",
   "kind": "adopted rule",
   "found_by": "Honesty guardrails and an adversarial critique of a course improvement plan.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/V2_MONSTER_DOSSIER.md",
     "lines": "109",
     "quote": "completion-up-while-construct-accuracy-flat is the named failure, not a win."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/V2_MONSTER_DOSSIER.md",
     "lines": "148",
     "quote": "Ranking the thing-being-measured above the measurement is the classic optimize-before-instrument error."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    51,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mix practice across skills so learners must choose which schema applies, and spread review over expanding intervals rather than one pass.",
   "kind": "adopted rule",
   "found_by": "Course design rationale and a review against the knowledge base's principles.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/WHY_V2_WINS.md",
     "lines": "43-44",
     "quote": "so the student must *discriminate* schemas, not pattern-match one per lesson"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
     "lines": "75",
     "quote": "kb-0027 names this as cramming, not distributed practice"
    }
   ],
   "against": "The outcome effect is unmeasured: \"MAP **0/313** → no RIT, no \"proven growth.\"\" (alpha-read-packager/FACTS_SHEET.md:48).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Present text excerpts in their original order, because reordering can make a line seem to belong to the wrong speaker or event.",
   "kind": "measured",
   "found_by": "An external audit; then encoded as a validator class.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "81",
     "quote": "Tap list is out of story order"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md",
     "lines": "180",
     "quote": "STORY-ORDER (validate-passage-refs.mjs)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    23
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Locate a quoted span by where the whole quote occurs, not by matching a fragment, because short fragments recur elsewhere in a text.",
   "kind": "measured",
   "found_by": "A visual pass found highlighting lit an unrelated earlier line.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md",
     "lines": "34",
     "quote": "so the candidate `\"So these are Peter Pan's precious friends,\" he said.` also lit the `he said.` fragment of the unrelated `\"Hook,\" he said.` a whole part earlier"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    16
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check content at its extremes (longest word, option and sentence, most options) on phone, tablet and desktop widths.",
   "kind": "measured",
   "found_by": "A visual audit found three defect classes invisible to a desktop-only battery.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "113",
     "quote": "Longest word, longest option, longest sentence, max option count render clean at 1280 AND 390"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-codex-visual-2026-09-07/REGISTER.md",
     "lines": "14",
     "quote": "Class rule: battery is desktop-only; all three classes invisible to it"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep adult controls and metadata (timers, counters, build strings, skip or reviewer switches) off the learner's screen.",
   "kind": "measured",
   "found_by": "Checklist gates and a UI review that found a visible reviewer switch opening every gate.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "181",
     "quote": "if it stays, every gate is one tap from skippable"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-argus-ui-2026-09-30/REGISTER.md",
     "lines": "11",
     "quote": "every gate opens (`nextLive = !locked \\|\\| reviewer`)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Log raw learner events rather than model-derived scores, and keep analysis separate, so the record doesn't change when a model does.",
   "kind": "adopted rule",
   "found_by": "Design of a learning-telemetry schema before any pilot.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/TELEMETRY-SCHEMA-v0-2026-08-31.md",
     "lines": "365",
     "quote": "- **No inference fields computed and stored ahead of need**"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/cert-layer/TELEMETRY-SCHEMA-v0-2026-08-31.md",
     "lines": "368-369",
     "quote": "disagree with itself the day the model changes"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test anti-copying guards against the answer you actually want, since an exact recall of a long target sentence was flagged as echoing; keep recall targets short.",
   "kind": "measured",
   "found_by": "Building recall questions against an echo guard in the marking route.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md",
     "lines": "128",
     "quote": "a Name-it/recall sentence longer than ~66 normalized chars is ≥0.70 of its own criterion line"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md",
     "lines": "128",
     "quote": "an exact recall is demoted (\"page's own words\")"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    12
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a change alters what learners are handed, judge whether it is better or worse for them before updating a test's expectation, and never edit an expected answer just to make a check pass.",
   "kind": "adopted rule",
   "found_by": "Adjudication of test failures after a merge; a readiness plan's abort rule.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/pr263-merge/RED-REGISTER.md",
     "lines": "13",
     "quote": "because each had to be adjudicated as better-or-worse before the test was retargeted"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/PLAN.md",
     "lines": "68",
     "quote": "do not edit an expected answer merely to produce green"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give a judge or reviewing agent the underlying content as well as the rendered page.",
   "kind": "measured",
   "found_by": "An AI review of a lesson withdrew findings after reading the lesson data.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md",
     "lines": "28",
     "quote": "It withdrew two of its four findings once it had the node data."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    30,
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Hold a lesson's load steady: count every moment that asks for a response against a budget and pair any addition with a deletion.",
   "kind": "adopted rule",
   "found_by": "A checklist budget and a curriculum audit that found many added pages beyond the design.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "57",
     "quote": "\\~31 is the proven target, \\~55 the documented breach"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "125",
     "quote": "Under the conservation rule an addition that stays pairs with a deletion"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/CRITIC.md",
     "lines": "11",
     "quote": "the audit found 11 added pages with no design basis in L4 alone, so the 25-min envelope is likely blown but unmeasured"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write instructions and guide lines at an easier reading level than the text being taught.",
   "kind": "adopted rule",
   "found_by": "A QC checklist gate.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "64",
     "quote": "instructional/Scout lines BELOW the passage band"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A text may sit above learners' independent reading level when it is read aloud to them.",
   "kind": "adopted rule",
   "found_by": "A review profile criterion applied in a simulated review.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-C-D7-D8-D10-D12.md",
     "lines": "31",
     "quote": "D8.20 permits above-band text at listening-comprehension level; all passages carry full voiceovers."
    }
   ],
   "against": "A checklist requires \"Every passage slice inside the teaching band\" (AlphaRead-QC-Checklist-v2-2026-09-04.md:64).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Checks during the first read stay literal until the inference skill has been modelled, because independent inference before the model breaks the gradual release.",
   "kind": "adopted rule",
   "found_by": "A ruling on an external audit's finding that early checks were all literal.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
     "lines": "26",
     "quote": "an independent inference item there would break the gradual-release order"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
     "lines": "27",
     "quote": "The retrieval-only reading checks (L4–L7 p6–p12)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Should a lesson's closing questions require learners to use the taught word, or only the concept language?",
   "kind": "open question",
   "found_by": "An AI review raised it as a question for the curriculum author rather than as a defect.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/REGISTER.md",
     "lines": "60",
     "quote": "does the closing sequence have to make the child USE THE TAUGHT WORD, or is the reading-goal concept language the only target?"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "How should spelling count in comprehension answers, by task type and for typed versus spoken input?",
   "kind": "open question",
   "found_by": "A misspelled answer was accepted; the policy was held pending a decision.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/REGISTER.md",
     "lines": "17",
     "quote": "Misspelled answer marked correct (\"magician\")"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md",
     "lines": "16",
     "quote": "The spelling policy: what earns comprehension credit, when spelling is separately corrected, and how typed versus transcribed answers differ."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    10
   ],
   "name_bearing_source": false
  },
  {
   "statement": "How can learners be made to commit to the model's reasoning before it is revealed without timers, locked buttons or yes/no gates?",
   "kind": "open question",
   "found_by": "A content review proposed commit-before-reveal; it conflicted with an existing interaction policy.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/REGISTER.md",
     "lines": "29",
     "quote": "Explicit anti-patterns named: no timers, no disabled Next, no yes/no gates."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Is knowledge better built through one continuous storyline across lessons or through topic-coherent sets of texts?",
   "kind": "open question",
   "found_by": "A meeting directive on narrative continuity was answered with a recorded push-back.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "201",
     "quote": "Knowledge-first ≠ a single forced storyline; topic-coherent passage sets are the better unit"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "On a familiar topic, items that match their passage can still be answered from background knowledge, while making the text rule out the obvious answers weakens the distractors once read, so decide which goal each item serves.",
   "kind": "measured",
   "found_by": "A rebuild of a mis-assembled form on a familiar topic, and a quality screen of a blind-certified pool.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "313",
     "quote": "items become **blind-solvable from background knowledge** — all 5 carry `blind_solvable_risk=HIGH`"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "314",
     "quote": "This is the coherence↔leak tension"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "96",
     "quote": "The quality screen flagged this on **14 of 26** items"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "To make items need the text on a familiar topic, change the passage rather than the distractors, giving it something a student of the topic cannot already know.",
   "kind": "adopted rule",
   "found_by": "Passage design rules written after encyclopedic passages produced mostly answerable-without-reading items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/PASSAGE_DESIGN_RULES.md",
     "lines": "5",
     "quote": "The fix is not to write harder distractors; it is to write passages that carry information the student cannot have encountered before opening this specific text."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/PASSAGE_DESIGN_RULES.md",
     "lines": "11",
     "quote": "> If the answer is YES for any item, the passage is leaking. Do not patch the item — fix the passage first."
    }
   ],
   "against": "Text-dependence is not truth: \"it does NOT mean the passage's own facts are sourced or true\" (alpha-read-packager/generator/GENERATOR.md:160); and blocking curriculum topics (\"**Blocked domains (curriculum — leak risk):**\", alpha-read-packager/generator/g5/PASSAGE_GENERATOR.md:23) conflicts with a knowledge-building course's topics.",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write each text with explicit layers: what it states, what it implies with support, and plausible neighbours it does not support, kept for wrong options.",
   "kind": "adopted rule",
   "found_by": "Passage specification headers in an authored unit.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/passage.md",
     "lines": "18",
     "quote": "- unsupported-plausible neighbors (for distractors; NOT in the text):"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/passages/kingfisher-bend-01.md",
     "lines": "10",
     "quote": "- layers: stated = photo figure"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Define the mastery performance on an unseen text with worked examples of answers at each level, including one below the bar, and a whole-performance rubric on which every row must meet the bar.",
   "kind": "adopted rule",
   "found_by": "A capstone design after every selected-response capstone item failed the anti-leak gate.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md",
     "lines": "8",
     "quote": "the mastery performance; defined by exemplars + rubric, NOT decomposed further"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md",
     "lines": "103",
     "quote": "Score each row 1-4. \"Meets the capstone\" = every row at 3 or higher"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/gate-capstone-summary.json",
     "lines": "13",
     "quote": "\"certified\": 0,"
    }
   ],
   "against": "The rubric itself is a draft, not an approved scoring key (exemplars-rubric.md:13-16).",
   "adds_to_existing": [
    56,
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Accept every answer the text defensibly supports, and check that reveals and hints don't steer toward only one of them.",
   "kind": "measured",
   "found_by": "An external audit of independent tasks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "116",
     "quote": "Only one of two defensible actions is accepted"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "97",
     "quote": "the reveal and second_hint steer only toward Hook"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    13,
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A 'what causes this?' question over a causal chain has several defensible answers, so ask about one named link.",
   "kind": "measured",
   "found_by": "A quality screen of blind-certified items and a QA pass over a shared item bundle.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "104-105",
     "quote": "defensible, and anti-leak keying the *non-proximate* link worsens it."
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/BUNDLE_CONTENT_BUGS.md",
     "lines": "53",
     "quote": "The passage is one continuous transitive causal chain"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every reference from one step to another must match what is actually there.",
   "kind": "measured",
   "found_by": "Audits found hints pointing to steps that didn't exist, recaps describing another task, and feedback using retired step names.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "57",
     "quote": "whose hint says \"Use one of the words you locked in at Step 3\", a step that does not exist"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/REPORT.md",
     "lines": "98",
     "quote": "but the text describes the Hook task, not the Lost Boys model"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "115",
     "quote": "use \"Zoom in\", the retired step-name"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check that every authored element actually reaches the learner, because content no surface shows is dead data and a marking proof built from it is invisible to the learner.",
   "kind": "measured",
   "found_by": "An authored block on a node type nothing rendered; a quote blank whose proof came from notes the learner never saw.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
     "lines": "92",
     "quote": "A validator must FAIL an authored block sitting on a node type whose renderer never reads it (the 477-line dead hunt; the teacher_recap near-miss)"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAP-CLOSURE-PLAN-2026-09-15.md",
     "lines": "57",
     "quote": "so that quote blank's proof is invisible to the child"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    30
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Quote the exact specification into a generator's instructions instead of paraphrasing it.",
   "kind": "measured",
   "found_by": "A parity round traced many divergences to generation without the contract quoted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
     "lines": "223",
     "quote": "Generation without quoting the contract caused the 17-divergence parity round"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record a missing measurement as missing, never as zero.",
   "kind": "adopted rule",
   "found_by": "Logging rules for an automated repair controller.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/controller-2026-09-14/PLAN.md",
     "lines": "42",
     "quote": "Usage omissions remain explicit, never fabricated zeros."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Stop after two identical fixes that didn't work and review the process instead of repeating the remedy.",
   "kind": "adopted rule",
   "found_by": "A repair controller's stop rule; regeneration rounds where re-authoring the hardest leaky items made the leak rate rise.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/codex-qa/controller-2026-09-14/PLAN.md",
     "lines": "76",
     "quote": "stop earlier after two identical ineffective remedies"
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
     "lines": "59",
     "quote": "| Round 2 | 32 | 26 | 6 | 0.812 | re-author R1 leakers — leak rate *rose* (hard residue) |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    65,
    70
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "72",
   "quote": "\"Good try, let's look again\" is a defect; passage visible whenever feedback says look back"
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
   "lines": "17",
   "quote": "23 wrong-answer feedbacks explain without pointing back to the text"
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/BUILD-SPEC-batch.md",
   "lines": "6",
   "quote": "a wrong-answer reply never names or paraphrases the key and never quotes six words of the correct option (validate-feedback)"
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "88",
   "quote": "Wrong-answer feedback for option D points directly at the condition that identifies the key"
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "80",
   "quote": "guard added after L4 shipped a 3-clip model split"
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "83",
   "quote": "A clip that is hash-correct (audio\\_of green) but voice-wrong still FAILS this row"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md",
   "lines": "147",
   "quote": "the goal before the passage already knows the answer (\"gentle\") before watching the model"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
   "lines": "27",
   "quote": "| LENS1-01 | Gradual-release leak: l0/l1 teaching articles pre-answered their certified release checks (must-fix)"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-arc-continuity.md",
   "lines": "159-160",
   "quote": "to notice (how they feel/sound), without naming the mood answer"
  },
  {
   "truth": 3,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/ROUND-RESULT.md",
   "lines": "14",
   "quote": "PP2 P066 prescribes the sentence; observation only"
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
   "lines": "69",
   "quote": "Two attempts, then Scout gives it and the lesson moves on."
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "24",
   "quote": "Generic doc mandates 'two attempts, then reveal' on pauses; R-Q-20 fails any mcq authoring reveal_after_tries"
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
   "lines": "138",
   "quote": "plain MCQ items use unlimited retry until correct, matching L4 pattern"
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
   "lines": "150",
   "quote": "**Outlier: tap-the-clue (p15) has reveal_after_tries=7 vs 3 for all other items.**"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
   "lines": "58",
   "quote": "anti-leak/answerability is a real, construct-general item-quality lever"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/g5/GATE1_BLIND_SOLVE_REPORT.md",
   "lines": "38",
   "quote": "**But self-containment ≠ passage-dependence.**"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md",
   "lines": "97",
   "quote": "answerable from prior knowledge, so it fails Transfer and Evidence precision at the root."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "102",
   "quote": "6 practice items dropped after the screen credibly showed a **multi-defensible key** (verified by reading"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
   "lines": "258",
   "quote": "Either way the correct answer should be statable with a single-sentence verbatim pointer."
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "25",
   "quote": "the answer is stated in the just-read sentence"
  },
  {
   "truth": 7,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
   "lines": "29",
   "quote": "The quoted **.30 control → .07 during-reading** result is Grade4 recall of **untargeted information**, not overall comprehension."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-item-stats.md",
   "lines": "47",
   "quote": "L4's first round had 72.5% on one position"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
   "lines": "29",
   "quote": "| LENS1-03 | Key-position imbalance, 12/19 A with a 5-run (must-fix)"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/census-pp-L4-L7.txt",
   "lines": "6",
   "quote": "every blank's answer sits at option 0: [0, 0, 0]"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "119",
   "quote": "The word bank lists answers in the same order as the blanks"
  },
  {
   "truth": 8,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
   "lines": "117",
   "quote": "The correct fix is *re-keying Form A's static options*, not shuffling."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md",
   "lines": "285",
   "quote": "wiring) is marked UNVERIFIABLE, not PASS."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "151",
   "quote": "flagged not flipped, to avoid a confident"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
   "lines": "38",
   "quote": "Never certified on missing evidence"
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt",
   "lines": "68",
   "quote": "Never string-match. Matching on “broken” passes “trust can never be broken,” which is the opposite of the answer."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/agent-B-D5-D6-D11-D13.md",
   "lines": "58",
   "quote": "\"never mark down for grammar, spelling, or shortness\""
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md",
   "lines": "8",
   "quote": "Correctness must not collapse to keyword presence."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "156",
   "quote": "Accent or hesitation never fails a child; type path always offered"
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "132",
   "quote": "A silent/no-speech dictation makes ZERO /api/speak-score calls"
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
   "lines": "31",
   "quote": "overwrites a correct open answer that differs from the authored one"
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "116",
   "quote": "Only one of two defensible actions is accepted"
  },
  {
   "truth": 14,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/TELEMETRY-SCHEMA-v0-2026-08-31.md",
   "lines": "352",
   "quote": "- **No raw typed text for selected-response items**, only a hash"
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
   "lines": "50",
   "quote": "90% of 2 is impossible"
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "107",
   "quote": "(the 0.5 was small-sample noise)"
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/VISUAL-QA-2026-09-11.md",
   "lines": "34",
   "quote": "so the candidate `\"So these are Peter Pan's precious friends,\" he said.` also lit the `he said.` fragment of the unrelated `\"Hook,\" he said.` a whole part earlier"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "58",
   "quote": "Quoted spans verbatim in the passage"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "87",
   "quote": "Nudge quotes words not in the story"
  },
  {
   "truth": 17,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-29/REGISTER.md",
   "lines": "57",
   "quote": "is a CONTRADICTION, not a fix"
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt",
   "lines": "9",
   "quote": "Exactly one high-leverage word is taught — chosen to unlock this text and to feed the Phase 3 inference."
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
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "70",
   "quote": "Hard words in passages carry glossary affordance at first occurrence"
  },
  {
   "truth": 20,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/inputs/procedures/Example_Lesson_Components.txt",
   "lines": "7",
   "quote": "A short background-knowledge video plays first, building the knowledge the text takes for granted."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-aladdin-2026-08-25/feedback-text.txt",
   "lines": "4",
   "quote": "but you must show the image as you say the word and ideally they would see the word on screen and hear what it means"
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/video-2026-09-16/PETER-PAN-PART-1-FILM.md",
   "lines": "81",
   "quote": "One main visual action at a time. Spoken concepts and their referents appear together. Avoid eye-catching background motion during explanations."
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "180",
   "quote": "the model adds the mother unprompted, and once drew five children from a four-child cast"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/L4-REVIEW-GAPS-2026-09-16.md",
   "lines": "116",
   "quote": "Peter on the chimney with THREE legs"
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "171",
   "quote": "slice boundaries never orphan a sentence mid-thought"
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "77",
   "quote": "Narrative sentences are never cut down to hit a length number (Lexile-driven editing forbidden)"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "86",
   "quote": "### B5. Deploy verification proves bytes, not behavior — SOLID"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/SUMMARY_AGENT.qmd",
   "lines": "15",
   "quote": "never an agent's self-report and never an HTTP 200 (a PUT can return 200 yet silently revert)"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "259",
   "quote": "but because **nothing re-ran IB (or the deterministic coherence gate) on the assembled live form**"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/SUMMARY_AGENT.qmd",
   "lines": "110-111",
   "quote": "silent-no-op feedback writes**"
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "100",
   "quote": "Ask appears in exactly one surface; Scout frames, never restates"
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-argus-ui-2026-09-30/REGISTER.md",
   "lines": "23",
   "quote": "right/wrong never rest on colour alone"
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "91",
   "quote": "Every page completable with sound off"
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "157",
   "quote": "nothing essential rides on an entrance animation"
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "127",
   "quote": "Clicking forward with no answer records no progress and no XP (leaked live twice)"
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/FEEDBACK_RESPONSE.md",
   "lines": "93-94",
   "quote": "real accuracy by clicking through — the gate did not actually require reading."
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
   "lines": "135",
   "quote": "conflated): l0-l3 are now non-gating formative"
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "129",
   "quote": "that first check activates and does not gate"
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
   "lines": "57",
   "quote": "The replacement introduced a factual error."
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAP-CLOSURE-PLAN-2026-09-15.md",
   "lines": "57",
   "quote": "so that quote blank's proof is invisible to the child"
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "258-259",
   "quote": "with the blank's own ask → band full, score 1"
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
   "lines": "42",
   "quote": "Runs 1 and 2 disagreed on vf07 (FAIL → note), vf08 (note → FAIL) and vf10 (note → FAIL)"
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "68",
   "quote": "Measured: ~22% flipped on the 2nd draw, 11.1% on the 3rd unified draw — it asymptotes but"
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-l5-2026-09-17/sim-review/lens-judge-probe.md",
   "lines": "83",
   "quote": "This run's praise misread. Again non-deterministic."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
   "lines": "180",
   "quote": "confirmed STABLE across 5 independent calls"
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/codex-qa/tool-reuse-assessment-2026-09-14.md",
   "lines": "67",
   "quote": "Completeness and consistency do not prove the truth of observations."
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "131",
   "quote": "Infra-failure way-outs (StuckWayOut) hand back the authored reveal"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "152",
   "quote": "so a one-word answer would have been refused"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/VISION-QA-CALIBRATION-2026-08-31.md",
   "lines": "185",
   "quote": "**Recall on the ground-truth set: 0/3 evaluable-as-designed (0%).** This is"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/audio/RESULT.md",
   "lines": "10",
   "quote": "The original read of stdout silently yielded NaN and skipped the attack check."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/audio/RESULT.md",
   "lines": "11",
   "quote": "including an actual temporary weak-onset tone that the original tool incorrectly accepted"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md",
   "lines": "267",
   "quote": "- **Red-control or it didn't happen.**"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
   "lines": "7",
   "quote": "Purpose: prove the new check DISCRIMINATES"
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/items/02-gate-summary.md",
   "lines": "44",
   "quote": "Independent recompute `verify_gate.py`: VERIFY PASS -- every verdict, blind score, floor,"
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
   "lines": "28",
   "quote": "All 14 article stimuli rebuilt: Get ready > The text > Watch me think > Your turn > Say it with evidence > Our river map"
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-18/REGISTER.md",
   "lines": "26",
   "quote": "an independent inference item there would break the gradual-release order"
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-pp-2026-08-27/REGISTER.md",
   "lines": "10",
   "quote": "Cracked both usage checks via \"baby\"+\"sleep\""
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/eval-suite/RANKING.md",
   "lines": "16",
   "quote": "two-forms-same-job defect"
  },
  {
   "truth": 42,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/codex-qa/harness-2026-09-14.txt",
   "lines": "3",
   "quote": "test_changed_acceptance_contract_invalidates_old_pass"
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/GENERATOR.md",
   "lines": "123",
   "quote": "**Generator and grader are separate roles/contexts.** The grader must never receive the"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "13",
   "quote": "Machine verification is exhaustive on shape and silent on doability by a Grade-3"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-23/index.html",
   "lines": "122",
   "quote": "133 clips machine-checked, zero human listens"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/HUMAN-REVIEW-2026-09-21.md",
   "lines": "22",
   "quote": "whisper hears \"ant\" as \"and\"; does a child?"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/codex-qa/experience-2026-09-14/independent-observer/REVIEW.md",
   "lines": "7",
   "quote": "Eighteen fixture expectations were fixed in the independent script and written into `run-01/INTENT.json` before the first measurement."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/RULES.md",
   "lines": "42",
   "quote": "and \"AlphaBuild shows it Valid\" do **not** mean it renders in reading — only a live student-app walk proves"
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "232",
   "quote": "this lane, baselines included, is therefore a read of the deprecated surface, not of the page the"
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "94",
   "quote": "static grep proved dishonest twice on 2026-08-25"
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-argus-ui-2026-09-30/REGISTER.md",
   "lines": "31",
   "quote": "any shell change gets a rendered look (screenshot or computed layout of the control) before the PR, not only a markup assertion"
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/INTERNAL-REVIEW-MESSAGE.md",
   "lines": "28",
   "quote": "This is not one uninterrupted journey on the final source."
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/annotation-and-walk/C3-DOCUMENTATION-REVIEW.md",
   "lines": "14",
   "quote": "No source presence or page Next state alone proves every subtask."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/WHY_V2_WINS.md",
   "lines": "13-14",
   "quote": "practiced certifies *familiarity*, not reading ability"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "188",
   "quote": "Receipt claims completion/practice, never mastery"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/cert-layer/CONTRACT-v0-2026-08-31.md",
   "lines": "53",
   "quote": "\"this lesson will not waste a child's time or lie to them,\" not"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "48",
   "quote": "\"Is it adding value\" cannot improve past \"the design says so and the shape is coherent\""
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/WHY_V2_WINS.md",
   "lines": "12",
   "quote": "**The weakness is text structure** — compare/contrast 39%, cause/effect 42%, sequence 48% (vs 83% blended)."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
   "lines": "33",
   "quote": "The cold/transfer passages are **MACHINE-AUTHORED** (`humanApproved:false`), **NOT real / primary-source**."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/KB_FURTHER_IMPROVEMENTS.md",
   "lines": "87",
   "quote": "flip humanApproved:true ONLY on individually-reviewed items, stamped with provenance"
  },
  {
   "truth": 50,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/readiness-2026-09-16/audio/VOICE-IDENTITY-2026-09-16.md",
   "lines": "16",
   "quote": "i.e. the stamp's voice label is wrong"
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/VERIFICATION-PROPOSALS.md",
   "lines": "11",
   "quote": "“Looks more animated” alone is not evidence of better teaching."
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
   "lines": "59",
   "quote": "A visual preference alone cannot establish comprehension gains."
  },
  {
   "truth": 52,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
   "lines": "21",
   "quote": "**Design conclusion:** avoid slow letter tracing that obstructs reading; chunked reveal is a reasonable prototype."
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "150",
   "quote": "Every video carries a VTT; captions toggle works"
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md",
   "lines": "8",
   "quote": "the mastery performance; defined by exemplars + rubric, NOT decomposed further"
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/AlphaRead-QC-Checklist-v2-2026-09-04.md",
   "lines": "223",
   "quote": "Generation without quoting the contract caused the 17-divergence parity round"
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/TI_COURSEPLANS_PR_PROPOSAL.md",
   "lines": "18",
   "quote": "RIT meaning free-floats on pre-training (wrong 200-210 / 208/214 anchors)"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "217",
   "quote": "the exact class meeting #10 calls \"passes item evaluations but fails the holistic course"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "229-230",
   "quote": "aggregate first returned a false all-clear"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
   "lines": "21-22",
   "quote": "child's science text is a kill, not a footnote."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-e/capstone/exemplars-rubric.md",
   "lines": "103",
   "quote": "Score each row 1-4. \"Meets the capstone\" = every row at 3 or higher"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-live-walk-2026-09-30/REGISTER.md",
   "lines": "47",
   "quote": "POLISH (recorded, not acted on unless a line is untrue to the story)"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "102",
   "quote": "6 practice items dropped after the screen credibly showed a **multi-defensible key** (verified by reading"
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
   "lines": "12",
   "quote": "Author inner-loop verdicts are recorded per claim; the QC lane owns"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/criteria-register.csv",
   "lines": "87",
   "quote": "shipped L10 is Anansi (wrong unit, wrong story, wrong skill)"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "423",
   "quote": "Lesson \"Who Ruled the Republic?\" but passage is about aqueduct water engineering."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/BUNDLE_CONTENT_BUGS.md",
   "lines": "15",
   "quote": "unanswerable-needs-visual | asks how a picture/diagram helps; image not rendered |"
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "418",
   "quote": "\"Look at the labeled diagram to see where they are!\" — no image, no CDN URL, no inline labels."
  },
  {
   "truth": 64,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "534",
   "quote": "Flagging diegetic mentions risks crying wolf."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "59",
   "quote": "| Round 2 | 32 | 26 | 6 | 0.812 | re-author R1 leakers — leak rate *rose* (hard residue) |"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/generator/RESULTS.md",
   "lines": "47",
   "quote": "**Independent acceptance: 8/9 = 89% strict-hold; #7 is a self-grade-generous borderline"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/LLM_GENERATION_BOUNDARY.md",
   "lines": "12",
   "quote": "**Catch deterministic structural tells** (longest-option, key-validity, identity-order) — it estimates, doesn't count"
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/v2_final_package/docs/COURSE_QUALITY_GATE_REPORT.md",
   "lines": "215-216",
   "quote": "items are unanswerable as rendered.**"
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/peter-pan-standing-2026-09-11/GAPS-2026-09-11.md",
   "lines": "258",
   "quote": "same word, via /api/speak-score: \"angry\" with the frame prompt → band off, score 0"
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/compare-2026-09-22/ours-only.html",
   "lines": "31",
   "quote": "Both sides are the same staging commit 5d033ac1. The only difference is our work."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-devfactory-2026-09-10/analysis-current-courses/RESEARCH-BOUNDARIES.md",
   "lines": "59",
   "quote": "choose one variable"
  }
 ]
}
```
