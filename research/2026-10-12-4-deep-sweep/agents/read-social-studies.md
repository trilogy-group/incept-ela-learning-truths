# read:social-studies

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "social-studies",
 "coverage": {
  "read": [
   "ap-social-studies-generator: README.md, CLAUDE.md, CHANGELOG.md, BENCHMARK_ACHIEVED.md, article-planning-with-claude.md, HANDOFF-finetune-status.md (outcome sections), PLAN-finetune-qwen.md (mission, insight stack, filters, data decisions), PLAN-user-prompts.md (grep)",
   "ap-social-studies-generator/docs: 00-CHARTER, 01-NORTH-STAR, 03-ARCHITECTURE, 04-QUALITY-STANDARDS, 05-OPERATING-PRINCIPLES, 07-SUCCESS-CRITERIA, 08-AP-SOCIAL-STUDIES-SPEC, 11-DATA-SOURCES, IMPROVEMENT_PROPOSALS, TRAINING_DECISIONS, MODEL_HISTORY, validation_rules",
   "ap-social-studies-generator/docs/analysis: all files (AGENT_BRIEFING, EVALUATOR_API_SPEC, best_practices, evaluation_audit, failure_analysis, prompt_options)",
   "ap-social-studies-generator/docs/archive: every report read in full or by headings plus finding greps (CLAUDE_VS_GEMINI_EVAL, CLAUDE_CROSS_EVAL_REPORT, CLAUDE_MANUAL_REVIEW, FRESH_CLAUDE_EVAL, EVALUATION-ANALYSIS, STATISTICAL_ANALYSIS, FACT_CHECK_RESULTS, MCQ_BUG_HISTORY, MCQ_ALIGNMENT_FIX, MCQ_VERIFICATION_100, MSQ_FIX_RESULTS, FILLIN_FIX_RESULTS, MANUAL-AUDIT-10-QUESTIONS, DECISIONS, decisions/2026-02-16, TECHNICAL-DECISIONS, EXPERIMENT_RESULTS, GENERATOR_STATUS, GEN5_OPTIMIZATION_REPORT, HOLISTIC_REVIEW, INCEPTBENCH_INTEGRATION_PLAN, RUN6_ANALYSIS, RUN7_BLUEPRINT, VERSION_ANALYSIS, ITERATION_ANALYSIS, ITERATION_LOG, OPTIMIZATION_LOG, PROMPT_EVOLUTION, PROMPT_EVOLUTION_2026-02-19, SAQ_RALPH_PROMPT, CONSOLIDATION, COMPREHENSIVE-AUDIT, COMPREHENSIVE-TEST, COMPREHENSIVE-TEST-V2, TEST-FINDINGS, FINAL_BENCHMARK_RESULTS, BENCHMARK_360_RESULTS, FINAL_QUALITY_ASSESSMENT, QUALITY_ANALYSIS, QUALITY_OVERHAUL_REPORT, STATUS-AUDIT, improvement_plan_prompts, VALID_QUESTION_TYPES, GEMINI-BEST-PRACTICES, and others by grep)",
   "ap-social-studies-generator/data: model_findings.md (all 1,342 lines), analysis_report.md, validation_report.md, pilot_reconstruction_report.md, progress.md",
   "ap-social-studies-generator/python: CLAUDE.md, HANDOVER.md, benchmark/CHANGELOG_RELENTLESS.md, benchmark/changelog.md (all outcome lines), benchmark/agents/{retester,analyst,fixer}.md, benchmark_results/unit_{1,2,3}/diagnosis.md, benchmark_runs/{analysis_iter1,analysis_iter2,failures_20260226_172346,failures_20260226_181058,BENCHMARK_README,PARTIAL_RESULTS_SUMMARY}.md, generators/saq.py and generators/mcq_set.py (rule text only, by grep)",
   "ap-social-studies-generator: curriculum/README.md; curriculum/ceds/ap-european-history-ced.pdf (exam format, task verbs, example SAQ/DBQ and scoring guidelines, via pdftotext); orchestrator/course_checker_blueprint.md and orchestrator CLAUDE/AGENT_INSTRUCTIONS/ARCHITECTURE (grep); course-checker/README.md; workspace/INBOX_FROM_EXTERNAL/2026-04-28T00_first-contact.md; ralph/perfect-mcq/RESULTS.jsonl (3 records); .beads/interactions.jsonl (first 3 records)",
   "k_12_social_studies: every document checked by md5 against the AP copies; read the unique ones: docs/BENCHMARK-RIGOR-ANALYSIS, EVALUATOR-TEAM-HANDOFF, EVALUATOR-CALIBRATION-SET.json, URGENT-BUG-STILL-PRESENT, VALIDATION-REPORT-15-45, -2026-02-18-1730, -2026-02-19-1030, -2026-02-19-COMPREHENSIVE, -2026-02-19-FINAL, ULTIMATE-VALIDATION-REPORT, COMPREHENSIVE-VALIDATION-2026-02-18-1600, archive/OPENCLAW_HUMAN_REVIEW, python/docs/EVALUATION-RESULTS-2026-02-23, python/.claude/skills/monitor-evaluator.md (others by grep), python/workflow/reports/REPORT_20260223_154247.md",
   "k_12_social_studies/ap_files: Knowledge Schema Generator - AP USH Unit 1 - Instructions.csv (all of it), AP Knowledge Schema Work Tracker - APUSH.csv (header rows), AP US History - Knowledge Schema - SME Tracker.xlsx (verdict and comment columns for all unit node and link sheets), Knowledge Schema Generator - AP USH Unit 1.xlsx (Configuration, Mapping, Consolidation Audit, Refinement, Node Metadata, Relationship Gen Audit: summaries only), Articles Tracker.xlsx (review, readability-experiment, line-comment and image-QC sheets), and the eight 'Unit N KS--<name> Review.xlsx' files (aggregate counts only; no candidate rests on them)"
  ],
  "skipped": [
   ".env files, gcs-service-account.json (root and python/), .claude settings JSON: credentials and settings, never opened",
   "questions.db, every training/DPO/eval/knowledge-corpus .jsonl, eval_results*.json, benchmark_results_*.json, *.log, data/models, model_backups, generated_images: data dumps, logs or binaries",
   "Copies named ' 2.md' or ' 2.py' in the AP generator (same size as the originals) and k_12 docs that are byte-identical to AP copies (checked by md5); each was read once, from the AP copy",
   "The other four CED PDFs (Human Geography, Macro, Micro, US Government): official format material already covered by the AP European History CED, and large",
   "Other knowledge-schema generator workbooks (APUSH units 3-9, the AP World UNIT 1-9 files, the [TOOL] template), the Curriculum Data Model Generator CSV/xlsx and AP Knowledge Schema Work Tracker.xlsx: large data or staff tracking; one representative generator workbook was inspected",
   "Generated-item dumps (HUMAN_REVIEW_SAMPLE, IRONCLAD_*, QUALITY_BATCH, RELENTLESS_BATCH_1, python/example_questions.md): only headers, metrics and spot checks",
   "Infrastructure, interface and staffing docs (02-MILESTONES, 06-ACCOUNTABILITY, 09-GENERATOR-INTERFACE, 10-GLOSSARY, 12-MONGODB-SETUP, API-README, DATA_MANIFEST, PIPELINE_STATUS, INDEX, REFACTORING_PLAN, REFACTOR_LOG, MIGRATION, TIMEOUT_FIX, SWARM-*), most Python source, k_12 HTML visualizations (styling only), node_modules, .venv, .git, .beads/backup"
  ],
  "notes": "No subagent tool was available in this session, so the fan-out was done serially by one agent. Spreadsheet evidence is cited by sheet and cell; PDF evidence by line in the pdftotext -layout output. The verdict and comment counts for the knowledge-schema review, and the 23-to-7 readability preference count, are my own tallies of the sheet columns. Comment categories came from keyword coding and are approximate. Eight review workbooks have a person's name in the path; I read their aggregate counts but every candidate relies on non-name files instead, so name_bearing_source is false throughout. ULTIMATE-VALIDATION-REPORT-2026-02-18.md contains a database credential in plain text; it was not quoted or reproduced. Much of the AP generator's tuning optimised for one automated judge, so several 'findings' are really that judge's preferences; the against fields say where official items or other evidence disagree. Process: one command accidentally created an empty directory, /tmp/claude-ro-scripts. No file was written and nothing in the scoped folders was changed. One iCloud read of Articles Tracker.xlsx failed briefly and succeeded on retry."
 },
 "candidates": [
  {
   "statement": "Don't let the model that wrote the items also grade them: grading by the same model gave a pass rate several times what an independent judge gave the same day's items, and it passed explanations that contradicted the key.",
   "kind": "measured",
   "found_by": "A 95.2% headline came from the writing model grading its own output. On the same day self-grading passed 56% where an independent model passed 9.1%, and the self-grader passed items whose explanations named a different answer than the key.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/HOLISTIC_REVIEW_2026-02-19.md",
     "lines": "202-203",
     "quote": "| Feb 17 AM | 56% | Gemini self-grading (meaningless) |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/DECISIONS.md",
     "lines": "7",
     "quote": "- Pass rates were inflated by 10-17%"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md",
     "lines": "164",
     "quote": "Questions Q36, Q44, and Q46 have explanations that contradict their answer keys. Gemini passed Q36 and Q44 despite this critical flaw."
    }
   ],
   "against": "CLAUDE_MANUAL_REVIEW.md line 10: \"**CRITICAL FINDING:** The problem is NOT \"Gemini grading Gemini too leniently\" - it's the **EVALUATOR being TOO STRICT**.\" On one 14-item sample the gap was small (CLAUDE_CROSS_EVAL_REPORT.md line 17: \"| Questions Passed | 4/14 (29%) | 3/14 (21%) | 71% |\"). The independent judge was never itself scored against person-labelled items.",
   "adds_to_existing": [
    43,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Whenever the judge or its version changes, re-check what each judging criterion actually rewards: one criterion first failed item sets whose difficulty didn't vary and, in a later version, failed sets whose difficulty did vary.",
   "kind": "measured",
   "found_by": "Item sets were rebuilt to vary difficulty because an earlier judge failed uniform sets. Under a later judge version the same change raised that criterion's share of set failures from 50% to 86%, and it was reverted.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
     "lines": "17",
     "quote": "The difficulty distribution is narrow; there are no 'Easy' questions present, and over 60% of the quiz sits at the Medium level. This lacks the progression needed for effective differentiation."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1176",
     "quote": "The evaluator does NOT want Q1<Q2<Q3 difficulty — it wants all 3 at the SAME stated difficulty level."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/PLAN-finetune-qwen.md",
     "lines": "520",
     "quote": "2. **InceptBench version gate:** prefer v2.3.10 and v2.3.8. Accept v2.3.6 only if score ≥ 0.98 (high bar compensates for weaker evaluator)"
    }
   ],
   "against": "The earlier diagnosis file doesn't record its judge version. The reversal is inferred from dates and from the version logged for the later runs (model_findings.md line 1005: \"| IB version | v2.4.0 |\").",
   "adds_to_existing": [
    45,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't judge a change from a dozen items: pass rates on 10–25 items per type swung 14–50 points with nothing changed, so size samples to the difference you need to see and treat unchanged item types as the noise floor.",
   "kind": "measured",
   "found_by": "A 12-item check scored 100% while the 116-item run of the same version scored 50%. One type rose 25 points on 13 items with no change to it. Swings in unchanged types were repeatedly written off as variance.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN6_ANALYSIS.md",
     "lines": "10",
     "quote": "**Mini benchmark (100%) was misleading.** Comprehensive benchmark revealed cognitive demand collapse."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "413",
     "quote": "4. **SAQ improvement (+25pp) is sampling variance.** Only 13 SAQ items in this run. No SAQ-specific changes made. Not a real improvement."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1260",
     "quote": "4. **MCQ_SET and DBQ high variance**: With 17 and 24 items respectively, a 5-8 item swing produces ±14pp swings. Not statistically meaningful at N=17-24."
    }
   ],
   "against": "The project kept making decisions on small samples: winners were declared on 10 items (EXPERIMENT_RESULTS_2026-02-18.md line 15: \"| **Two-Stage Generation** | **100%** (10/10) | ✅ WINNER |\"), and the blueprint kept a 12-question check for iteration (RUN7_BLUEPRINT.md line 1005).",
   "adds_to_existing": [
    34,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare pass rates only between runs with the same mix of requests: a change in which topics or difficulties were requested moved one item type from 99.3% to 90.0% with no change to the generator.",
   "kind": "measured",
   "found_by": "What looked like a regression was a different request mix. Later drops were also traced to harder or differently weighted samples.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "248",
     "quote": "The 99.3% LEQ pass rate (run `fda3ba0f`) had **zero APUSH-5 LEQ** requests."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "251",
     "quote": "This is not a code regression but a test distribution change revealing an existing issue with APUSH Unit 5's time period (1844-1877) conflicting with topics like \"Reconstruction\" (1865-1877)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "571",
     "quote": "MCQ apparent regression (-11pp) is explained by sampling variance: Gate 3 included harder MCQ items (APWH, APEURO hard-difficulty)."
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
   "statement": "After every change, re-run a control set of items that already passed: batched edits aimed at failures raised the targeted pass rate by up to 4.6 points while 5–55% of the control set regressed, and every batch was reverted.",
   "kind": "measured",
   "found_by": "The improvement log records eight batches of prompt edits. Each was reverted because the control set regressed past the 3% limit.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/changelog.md",
     "lines": "157",
     "quote": "**Before:** 94.8% | **After:** 87.7% | **Control regression:** 54.9%"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/changelog.md",
     "lines": "462",
     "quote": "**Status:** REVERTED ✗ — control regression 7.1%, improvement +4.6%"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/agents/retester.md",
     "lines": "39",
     "quote": "- Control group regression > 3% (signs of overfitting/regression), OR"
    }
   ],
   "against": "Control samples were small (python/CLAUDE.md line 192: \".venv/bin/python -m benchmark.retest --unit 1 --concurrency 30 --control-pct 15\"), so part of each regression may be judge noise.",
   "adds_to_existing": [
    60,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Confirm a fix on material it was not tuned on, and keep the requests used for evaluation out of anything used to build or tune the generator.",
   "kind": "measured",
   "found_by": "An evaluation set turned out to be 89% identical to the training prompts, so it measured memorised execution rather than generalisation. A prompt 'winner' had been tested only on easy topics. The improvement loop then required a fix to hold on a second unit before it was kept.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "135",
     "quote": "- **89% (5,219/5,878) prompts identical to training prompts** (500-char fingerprint match)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
     "lines": "466",
     "quote": "5. Only checkpoint if improvement holds across 2+ units"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/OPTIMIZATION_LOG.md",
     "lines": "42",
     "quote": "**Problem:** Gen 1 winner tested on easy topics. Needed harder topics."
    }
   ],
   "against": "The 97% headline was measured on the same 28 files the push was tuned against (python/CLAUDE.md line 7: \"raised the 28-file benchmark pass rate from **81.9% to 97%** (reported)\"), so it is not a held-out figure.",
   "adds_to_existing": [
    48,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never let a missing or unrecognised course or unit label fall back to a default; stop the request instead, because a silent default sent every request for one course through another course's content and skipped its scope rules.",
   "kind": "measured",
   "found_by": "An unmatched standard code silently defaulted to one course and unit. After the routing fixes, the affected course rose from 70.7% to 94.0% (cumulative with other fixes) and one unit from 43.3% to 100%.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
     "lines": "120",
     "quote": "`parse_substandard(\"KC-4.1.VI+1+D\")` in the generator code doesn't match any of the regex patterns for course detection (USH/WH/EH/MAC/MIC/GOV/HG/EURO prefix). It silently falls through to the default: `{course=\"APUSH\", unit=1}`."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
     "lines": "145",
     "quote": "So `ctx.course` came back as \"APUSH\" for all APWH items. Because `ctx.course != \"APWH\"`, the `_build_apwh_unit_guidance()` function added in commit 2 was **silently skipped** for every APWH request."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
     "lines": "163",
     "quote": "APWH u3 going from 43.3% to 100% with 0 hard-fails is the definitive proof that the KC-prefix routing chain (commits 3+4+2) was the root cause."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Retrieve source material for an item by its exact topic or objective, not by its broad unit or period; matching only by unit handed the writer the wrong sources.",
   "kind": "measured",
   "found_by": "A document bank keyed by unit gave a topic request 2 relevant documents in 50. Matching by topic first took that item type from 30% to 75%. Exact lookup by the request's standard code replaced a fuzzy search that returned irrelevant facts.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "407",
     "quote": "1. **Topic mismatch is the root failure cause.** Bank indexed by (course, unit) — 50 entries spanning 30+ years and multiple topics. A \"Failure of Reconstruction\" request had only 2/50 chance of getting Reconstruction documents."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "421",
     "quote": "**75%** | 0.944 | +45pp ✅ PASS"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
     "lines": "151",
     "quote": "We were doing fuzzy topic-based MongoDB search and sometimes getting irrelevant facts."
    }
   ],
   "against": "The 75% rests on 8 items (model_findings.md line 421), so the size of the gain is uncertain.",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never show students generated text presented as a real person's words or a real document; supply verified sources instead, because recasting invented sources as paraphrase removed the false attribution but not the false content.",
   "kind": "measured",
   "found_by": "Invented excerpts and misattributed quotes were a leading cause of hard failures on source-based items. A rule written to dodge a copyright filter told the writer to imagine what a real author would have written.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "520",
     "quote": "- 3/5 = fabricated stimulus (invented pamphlet, fabricated Locke paraphrase, invented \"New Englanders\" excerpt) — anti-fabrication constraint PARTIALLY effective"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "521",
     "quote": "- 2/5 = \"A historian argues...\" format correct, but factual content of the argument wrong — constraint eliminated format-fabrication but not content-fabrication"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
     "lines": "591",
     "quote": "- Think: \"What WOULD they have written?\" not \"What DID they write?\""
    }
   ],
   "against": "The subject spec allowed invented sources (08-AP-SOCIAL-STUDIES-SPEC.md line 152: \"- Primary source excerpts must be authentic or authentically styled\"), and the copyright filter blocks verbatim recall (python/CLAUDE.md line 584: \"The model tries to reproduce actual quotes and triggers copyright filters.\"). Real excerpts therefore have to come from a vetted bank, not from the model.",
   "adds_to_existing": [
    17,
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check in code that each explanation endorses the keyed option and no other, and fail the item when the check can't tell; an explanation that contradicts the key misleads like a wrong fact, and lenient judges passed it.",
   "kind": "measured",
   "found_by": "Explanations naming a different letter from the key failed 7 of 30 items. The first validator never looked for a wrong letter called correct, and it returned pass by default.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md",
     "lines": "6",
     "quote": "This bug caused 7 out of 30 questions (23%) to fail in Claude cross-evaluation, making it a critical quality blocker."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md",
     "lines": "80",
     "quote": "return True  # ← WRONG! Should be False to trigger regeneration"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md",
     "lines": "197",
     "quote": "- This is functionally equivalent to a factual error"
    }
   ],
   "against": "Pattern checks only catch explicit letter phrases. An explanation can argue for a wrong option without naming it (python/benchmark_runs/analysis_iter1.md line 79: \"The explanation for why D is wrong actually confirms why D could be correct\").",
   "adds_to_existing": [
    59,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fix the key's position in code before the item is written, and write the explanation from the finished item: left to itself the writer put almost every key on one letter, and shuffling options after writing broke the explanation's letter references.",
   "kind": "measured",
   "found_by": "Keys clustered on one letter (every key was 'B'; 9 of 10 at low temperature). The shuffle added to fix this broke the explanations' letter references. The mismatch went away once the position was set first and the explanation was written in a second step.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TECHNICAL-DECISIONS.md",
     "lines": "106",
     "quote": "Fixed answer bias (all answers were \"B\") by shuffling options after generation."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/EXPERIMENT_RESULTS_2026-02-18.md",
     "lines": "118",
     "quote": "- Lower temperature made answer bias worse (9/10 picked \"B\")"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/DECISIONS.md",
     "lines": "49",
     "quote": "- No post-hoc shuffling that can desync answer/explanation"
    }
   ],
   "against": "A shuffle done in code with every letter reference rewritten also passed 10 of 10 (EXPERIMENT_RESULTS_2026-02-18.md line 17: \"| **Fixed Position + Shuffle** | **100%** (10/10) | ✅ WINNER |\"), so shuffling after writing can work if every reference is remapped.",
   "adds_to_existing": [
    8,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "List as accepted answers only different wordings of the same idea, never related but distinct ideas or a broader category; mixed lists made marking inconsistent.",
   "kind": "measured",
   "found_by": "Three separate reviews failed open-response keys that accepted a related concept, an era instead of an event, or a person instead of the movement asked for.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/evaluation_audit.md",
     "lines": "69",
     "quote": "4. The accepted answers (popular sovereignty, consent of governed, social contract) are related but distinct concepts, creating grading inconsistency"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter2.md",
     "lines": "40",
     "quote": "Part (a) scoring criteria lists both 'Compromise of 1877' and 'Reconstruction' as acceptable answers, which creates an internal contradiction"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/failures_20260226_172346.md",
     "lines": "79",
     "quote": "- Part (a) scoring accepts 'Martin Luther' or '95 Theses' as equivalent to 'Protestant Reformation,'"
    }
   ],
   "against": "The writer instructions pushed the other way (python/generators/saq.py lines 232-233: \"⛔ SCORING INCLUSIVENESS: If a reasonable AP student could cite evidence X and it's\" / \"factually correct AND relevant to the prompt, it MUST be in the acceptable list.\"), which grows lists that drift to related ideas.",
   "adds_to_existing": [
    10
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check that an item can't be answered from cues inside it: surrounding words that define the answer, extreme words that mark options as false, or options of telling length.",
   "kind": "measured",
   "found_by": "A 582-item review found absolute words in 191 items (35%), which let wrong options be eliminated without knowledge. Fill-in items whose sentences defined their own blanks passed only 6.7%.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/python/docs/EVALUATION-RESULTS-2026-02-23.md",
     "lines": "34",
     "quote": "**Frequency:** 191 questions (35% of all generated)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/failure_analysis.md",
     "lines": "28",
     "quote": "Question stems provide so much context that students can identify the answer without demonstrating historical thinking skills."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/archive/OPENCLAW_HUMAN_REVIEW.md",
     "lines": "34",
     "quote": "Option A (\"immediate collapse\") is a weak distractor — students could eliminate it by word choice alone"
    }
   ],
   "against": "A word ban is blunt: validation_rules.md line 193 fails a true statement (\"| \"The Civil War resulted in the **complete abolition** of slavery\" | ❌ FAIL: \"complete\" + \"abolition\" |\"). The ban written into the prompt was ignored in 35% of items until it was enforced in code (improvement_plan_prompts.md line 15).",
   "adds_to_existing": [
    3,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build each wrong option from a misconception students actually hold, so that some students choose it; options made only to resemble the key, or that nobody would pick, measure nothing.",
   "kind": "external research",
   "found_by": "The project's research summary cites a study (arXiv:2501.13125) in which distractors generated from predicted student choices beat similarity-based ones. Judges repeatedly failed options as implausible or as not reflecting a realistic misconception.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "69",
     "quote": "**Key Finding**: Distractors generated by predicting student choice behavior significantly outperform those generated by similarity-based methods."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "395",
     "quote": "- Lee, Y. et al. (2025). Generating Plausible Distractors via Student Choice Prediction. arXiv:2501.13125."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
     "lines": "24",
     "quote": "Q1-D (declaring war over the Treaty of Tordesillas) is easily eliminated and does not reflect a realistic student misconception."
    }
   ],
   "against": "No student responses were ever collected, so the test of whether a distractor works (best_practices.md line 44: \"- Each should be selected by at least 5% of test-takers\") was never applied; plausibility was judged only by models.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make each wrong option wrong as an answer to the question asked, not a false statement of fact; options that asserted invented facts were failed as factual errors that could mislead.",
   "kind": "measured",
   "found_by": "Judges failed single items and whole sets because a wrong option itself stated something untrue.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
     "lines": "34",
     "quote": "Option B in Question 3 contains a clear factual error: African American Exodusters were not legally barred from settling in Kansas."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/failures_20260226_181058.md",
     "lines": "11",
     "quote": "Option D contains a factual inaccuracy: Germany did not fully seize the Caucasus oil fields."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_3/diagnosis.md",
     "lines": "49",
     "quote": "A factual error is present in Question 3, where a distractor incorrectly describes the Virginia Plan as advocating for a unicameral legislature."
    }
   ],
   "against": "For select-all items the project's own analysis asked for the opposite (failure_analysis.md line 119: \"4. Wrong answers must be FACTUALLY FALSE statements, not \"distractors\"\"), so the rule depends on the item format.",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write the stem as a complete question that can be understood before the options are read.",
   "kind": "adopted rule",
   "found_by": "Adopted into the project's item checklist from item-writing guidance. A cross-review found an item with no actual question in it.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "381",
     "quote": "- [ ] **Clear stem**: Question understandable without reading options"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/best_practices.md",
     "lines": "159",
     "quote": "**Fix**: Review stems independently before adding options"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md",
     "lines": "80",
     "quote": "- ⚠️ Missing question stem (what exactly is being asked?)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Set difficulty by the reasoning an item demands (the number of steps, how familiar the material is, how much synthesis it needs), not by a label or by withholding context; labels alone changed nothing, and stems stripped of context became recall.",
   "kind": "measured",
   "found_by": "Adding difficulty labels in a retrain without changing content dropped one set type from 86% to 62%. Removing context from hard stems turned them into recall, and cognitive-demand passes fell to 51%. A single-step question pattern was rated medium, not hard.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/HANDOFF-finetune-status.md",
     "lines": "71",
     "quote": "**Lesson:** Label injection without content variation teaches nothing. The model needs examples with structurally different question types at each difficulty level."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN6_ANALYSIS.md",
     "lines": "41",
     "quote": "**ACTUAL:** Questions became cognitively shallow recall exercises"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "104",
     "quote": "\"What would X group think?\" pattern is single-step reasoning."
    }
   ],
   "against": "An earlier lesson in the same project said the reverse (ITERATION_ANALYSIS.md line 181: \"> **Hard questions must require RECALL, not READING.** Scaffolding makes hard questions into medium questions.\"). One review accepted heavy support for weaker students (evaluation_audit.md line 109: \"However, for a practice fill-in, this level of scaffolding might be acceptable for struggling students.\"). The 86%-to-62% drop came from a retrain that changed other things too.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a request can't be met as written (its labels contradict its scope, or it asks for an easy version of an inherently multi-step task), or when every generator fails it, fix or reject the request before changing the generator.",
   "kind": "measured",
   "found_by": "Two different models failed the same request. One objective demanded content that the judge, on another item, ruled outside the course. Some alignment failures traced to wrong unit assignments in the benchmark data (python/CLAUDE.md line 113), and requests for 'easy' essay tasks drew dozens of difficulty-mismatch failures.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "829",
     "quote": "Both models hard-failed at the same DBQ item (item 33) — confirming some eval samples are intrinsically difficult (wrong unit mapping, impossible spec, or IB v2.4.0 edge case)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
     "lines": "50",
     "quote": "The question fails to address the specific learning objective requested (Inca Empire) and instead focuses on a different group (Pueblo peoples)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
     "lines": "100",
     "quote": "The question targets the wrong curriculum. AP US History focuses on societies in what is now the United States; the Inca Empire is a South American civilization assessed in AP World History."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    39,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Let accuracy override any length or span quota in a writer's instructions; when a quota can't be met truthfully, the writer bends the facts to meet it.",
   "kind": "measured",
   "found_by": "A minimum-span rule for essay periods made the writer move a period's start date earlier than it really was. Replacing the rule with 'accuracy first' fixed it.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "18",
     "quote": "\"Use the FULL period or a large subset (minimum 20 years)\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "31",
     "quote": "4. LLM extends to 1850 to meet 20-year minimum → historically inaccurate"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "34",
     "quote": "**Principle:** Historical accuracy > arbitrary length requirements"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Treat every rule or example added to a writer's instructions as a change to test: added constraints and examples repeatedly made output worse, so remove old rules when adding new ones and check that the rules don't conflict.",
   "kind": "measured",
   "found_by": "Run-over-run analysis tied regressions to added rules and conflicting 'do not' lists. Adding 15 worked examples to one course's source-based task brought 4 failures, where the version without examples passed 98%.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/ITERATION_ANALYSIS.md",
     "lines": "93",
     "quote": "> **More rules ≠ better output.** The LLM has limited attention. Every added constraint dilutes the importance of existing ones."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
     "lines": "186",
     "quote": "APUSH DBQ had 4 failures after adding 15 document examples to prompts."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/VERSION_ANALYSIS.md",
     "lines": "88",
     "quote": "3. **Conflicting DO NOTs** - Model couldn't satisfy all constraints"
    }
   ],
   "against": "Examples helped elsewhere (IMPROVEMENT_PROPOSALS.md line 227: \"| Experiment | APEURO | 31 | 26.6 | 100% pass |\"; VERSION_ANALYSIS.md line 232: \"| Concrete bad examples | **Strong positive** |\"). The run comparisons also changed several things at once.",
   "adds_to_existing": [
    62,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give a writer concrete, checkable constraints that say what the item must make the student do, not abstract labels such as a taxonomy level or 'be specific'.",
   "kind": "adopted rule",
   "found_by": "After six runs the project concluded that abstract instructions and taxonomy labels did not change the output, while concrete constraints did.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md",
     "lines": "612",
     "quote": "- Every instruction should be checkable"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md",
     "lines": "637",
     "quote": "- Describe the BEHAVIOR you want, not the classification"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/PROMPT_EVOLUTION.md",
     "lines": "186",
     "quote": "**Why:** Bloom's taxonomy names don't constrain generation behavior."
    }
   ],
   "against": "The supporting evidence compares whole runs that changed several things at once (RUN7_BLUEPRINT.md line 579: \"- Can't isolate which change caused regression\").",
   "adds_to_existing": [
    62
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Nothing a student or marker sees may refer to the writer's working material that they can't see, such as a research brief or numbered source facts.",
   "kind": "measured",
   "found_by": "Marking notes referred to 'the brief', and articles cited numbered knowledge-base facts that were never shown. The writer rules were then changed to ban such references.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter2.md",
     "lines": "42",
     "quote": "Part (a) scoring is problematic: it references 'the brief'"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/archive/OPENCLAW_HUMAN_REVIEW.md",
     "lines": "106",
     "quote": "- Articles reference numbered \"Facts\" from knowledge base that aren't shown in the output"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
     "lines": "765-766",
     "quote": "must be self-contained and readable by someone who ONLY sees the question."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    30,
    61
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make each part of a multi-part task answerable and markable on its own, so a slip in one part doesn't cost the others.",
   "kind": "adopted rule",
   "found_by": "The official scoring guidelines award each point independently, and the generator adopted a rule against chaining parts.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf",
     "lines": "pdftotext -layout output, line 12633",
     "quote": "Each point is earned independently."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
     "lines": "771",
     "quote": "⛔ Parts must be independently scorable — no chaining."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Name everything a question asks students to relate (both sides of a comparison, the region, the period) so they never have to guess the frame.",
   "kind": "measured",
   "found_by": "Clarity failures came from comparisons with one side missing and from vague region labels. The writer rules then required naming both items being compared.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/python/docs/EVALUATION-RESULTS-2026-02-23.md",
     "lines": "259",
     "quote": "| **Unclear comparisons** | \"More significant than...\" (than what?) | Complete the comparison |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
     "lines": "76",
     "quote": "Part C of the prompt uses the vague descriptor 'southern regions,' which is imprecise."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
     "lines": "282",
     "quote": "RULE: A student should never need to infer WHAT is being compared — name both items."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write open-response prompts that admit more than one defensible position; prompts asking for 'the main cause' collapsed into yes/no claims and failed.",
   "kind": "measured",
   "found_by": "A writer that defaulted to 'primary cause' framing failed specification checks on essay prompts. Forbidding that framing raised the essay pass rate by 15.9 points.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1114",
     "quote": "- Pattern: \"primary cause\" framing generates falsifiable yes/no questions instead of nuanced analytical prompts"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
     "lines": "1257",
     "quote": "1. **LEQ fix works**: +15.9pp vs Gate 12b. The spec_compliance FORBIDDEN list genuinely helped."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/GENERATOR_STATUS.md",
     "lines": "27",
     "quote": "- Prompts are genuinely arguable — students can take multiple positions"
    }
   ],
   "against": "Official prompts use the same framing (ap-european-history-ced.pdf, pdftotext line 12700: \"Evaluate whether the Thirty Years’ War was fought primarily for religious or primarily for political reasons.\"), so the failures may reflect the judge rather than the prompt. The framing still accounted for 88% of the remaining essay failures (model_findings.md line 1258).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a judge rejects task forms that the real assessment uses, check the judge against official items instead of removing those forms from what students get.",
   "kind": "measured",
   "found_by": "To pass a judge that treated 'describe' and 'identify' as recall and failed source-based short answers, the generator banned both, even though the official exam's short-answer questions use sources and 'describe'.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
     "lines": "20",
     "quote": "**Root cause:** The evaluator treats \"Describe\" and \"Identify\" as recall-level verbs regardless of analytical keywords in the question."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
     "lines": "68",
     "quote": "1. **SAQ: No stimulus ever.** Stimulus-based SAQs always fail Part (a) as \"reading comprehension\" instead of \"historical thinking.\""
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf",
     "lines": "pdftotext -layout output, line 12078",
     "quote": "(A) Describe the historical situation in Spain reflected in the poster."
    }
   ],
   "against": "The program forbade changing the judge (03-ARCHITECTURE.md line 41: \"| **Modify the evaluator** | InceptBench is the immutable standard; gaming it is not an option |\"), which left changing the items as the only lever.",
   "adds_to_existing": [
    37,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Change a judge's criteria or thresholds only to agree better with labelled cases, never to raise a pass rate.",
   "kind": "adopted rule",
   "found_by": "Reviews proposed relaxing thresholds for item types that kept failing, and judge prompts were rewritten to stop penalising formats. The judge-monitoring guide made accuracy, not pass rate, the test for any change to the judge.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/python/.claude/skills/monitor-evaluator.md",
     "lines": "46",
     "quote": "- Changes to evaluator should be based on benchmark accuracy, not pass rate"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CLAUDE_MANUAL_REVIEW.md",
     "lines": "168",
     "quote": "cognitive_threshold = 0.70  # Relaxed from 0.85"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TEST-FINDINGS-2026-02-17.md",
     "lines": "55",
     "quote": "**Fix:** Updated evaluation prompts to focus on CONTENT quality only,"
    }
   ],
   "against": "Some judge changes fixed real judge bugs rather than lowering the bar (CLAUDE_MANUAL_REVIEW.md line 39: \"**The pass logic is checking `passed = false` even when `score >= 0.85`.**\").",
   "adds_to_existing": [
    37,
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Require a judge to quote the exact words behind each failure, and check in code that those words are in the item.",
   "kind": "measured",
   "found_by": "A judge failed about 14% of question sets by citing text that wasn't in them. A judge shown a cut-off copy reported complete items as truncated.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/workspace/INBOX_FROM_EXTERNAL/2026-04-28T00_first-contact.md",
     "lines": "49",
     "quote": "- We discovered an **InceptBench v2.4.0 false-positive `integrity_check` failure mode** on MCQ_SET (~14% of failures): the eval cites scoring-directive text that doesn't exist in our outputs."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/BENCHMARK-RIGOR-ANALYSIS.md",
     "lines": "27",
     "quote": "3. Score metrics (each 0.0 must cite an issue)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/VALIDATION-REPORT-2026-02-19-COMPREHENSIVE.md",
     "lines": "161",
     "quote": "- \"The article is truncated and ends mid-sentence\" - FALSE"
    }
   ],
   "against": "The 14% comes from a parallel team's runs on its own judge setup, not from this project's measurements.",
   "adds_to_existing": [
    17,
    32,
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't use keyword, verb or length counts as measures of quality; they pass wrong items and fail good ones.",
   "kind": "measured",
   "found_by": "A keyword-counting scorer produced a 58.8% pass rate that meant nothing. A topic check that matched title words rejected valid items whose topics had metaphorical or very short names. A judge keyed on task verbs rejected analytical parts.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/EVALUATION-ANALYSIS.md",
     "lines": "57",
     "quote": "- Score **1.00** but be factually wrong"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/EVALUATION-ANALYSIS.md",
     "lines": "130",
     "quote": "**The 58.8% pass rate is meaningless** because:"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/CONSOLIDATION_2026-02-19.md",
     "lines": "19",
     "quote": "1. **Metaphorical APWH titles** - Topics like \"The Global Tapestry (1200-1450)\" were rejected because validation looked for literal words (\"tapestry\", \"global\") instead of actual historical content (Mongol Empire, Song Dynasty)"
    }
   ],
   "against": "Used as gates rather than as scores, cheap word checks still caught a real cue that appeared in 35% of items (EVALUATION-RESULTS-2026-02-23.md line 34).",
   "adds_to_existing": [
    10,
    32
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check a bank of generated items for repeated sources and stems; a generator keeps returning to the same few well-known passages.",
   "kind": "measured",
   "found_by": "Among high-scoring items, 24.53% were near-duplicates by their opening text, and one excerpt opened 50 different items. A duplicate check caught 12 of 62 attempts in one batch.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/analysis_report.md",
     "lines": "403",
     "quote": "- Duplicate rate: 24.53%"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/analysis_report.md",
     "lines": "406",
     "quote": "- Count 50: [mcq/apush] Use the excerpt below to answer the question."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/IRONCLAD_BATCH_50.md",
     "lines": "12",
     "quote": "- Duplicates Caught: 12"
    }
   ],
   "against": "The near-duplicate count hashed only the first 200 characters (analysis_report.md line 399: \"- Total unique hashes (first 200 chars): 10382\"), so items sharing a passage but asking different questions were counted as duplicates.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Review machine-built knowledge for placement, repetition and scope as well as accuracy; most rejected facts and links were repeats or belonged to another topic rather than being false.",
   "kind": "measured",
   "found_by": "Across nine units of subject review, 69 of 1,633 facts were marked 'No' (11 more 'Partially') and 164 of 2,086 links between facts were rejected. Coding the comments by keyword, the commonest reasons for facts were placement (53 of 159 comments) and repeats (44), and repeats dominated for links (103 of 172). Accuracy notes were rare (2 for facts, 5 for links).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 6 Nodes', cell M16",
     "quote": "move to 6.2"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 3 Relationships', cell J14",
     "quote": "already covered"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 1 Nodes', cell M10",
     "quote": "Out of time frame for this course"
    }
   ],
   "against": "The comment categories are my keyword coding, not the sheet's. Many facts carry only a 'Yes' with no note, so the scarcity of accuracy notes may reflect how deep the review went rather than how accurate the facts were.",
   "adds_to_existing": [
    58,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check every generated cause-and-effect link for direction, directness and type; links came out reversed, stated an indirect cause as direct, or used the wrong relation.",
   "kind": "measured",
   "found_by": "Subject review of generated links between facts reversed causation, downgraded direct causes to indirect ones, and corrected link types.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 6 Relationships', cell J122",
     "quote": "The statements should be reversed since the E. C. Knight Co. decision influenced and changed the scope of the Sherman Antitrust act"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 8 Relationships', cell J6",
     "quote": "MAD was more of an indirect cause"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 6 Relationships', cell J69",
     "quote": "This should be \"details,\" not \"exemplifies\""
    }
   ],
   "against": "These were a minority of link comments (about 9 of 172 by keyword coding); repeats were far more common.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Map every fact extracted from source texts to a learning objective, and drop or review the ones that fit none; a large share of textbook-derived facts fit no objective.",
   "kind": "measured",
   "found_by": "In one unit's knowledge build, 437 extracted facts were labelled 'None' against 757 mapped to a topic, and the refinement step removed whole out-of-scope civilisations.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1.xlsx",
     "lines": "sheet '2. Mapping Output', column D ('Cluster'), e.g. cell D109",
     "quote": "None"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1.xlsx",
     "lines": "sheet '6. Fact Refinement Output', cell F2",
     "quote": "3. Out of Scope (Mesoamerican civilizations):"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1 - Instructions.csv",
     "lines": "16",
     "quote": "7. In the main.py script, run steps 1 and 2 (generate facts + map facts to curriculum)."
    }
   ],
   "against": "Unmapped facts may still be needed background (the reviews kept asking for added definitions and context), so dropping all of them could remove support students need.",
   "adds_to_existing": [
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check simplified text by reading it against the original: easier reading-level scores came with sentence splits that changed the meaning, everyday words in place of key terms, and mechanical prose.",
   "kind": "measured",
   "found_by": "In a readability trial, line-level review of simplified articles found a sentence split that re-paired ideas, repetitive sentence patterns, and curriculum terms replaced by everyday words.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'ReadabilityExperiment-dev-inter', cell N13",
     "quote": "In this instance, the sentence split separated \"missionaries\" and \"salvation,\" which led to it only being paired with \"wealth.\" This changes the meaning of the paragraph"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'ReadabilityExperiment-dev-inter', cell N8",
     "quote": "Some of these changes give the flow an overly predictable pattern. That's not always a bad thing, but it can feel very mechanical and repetitive, which is not ideal."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'APUSH Articles-readable-exp', cell M2",
     "quote": "This was pretty solid, but the biggest issue is that specific phrasing from the CED standards were simplified as well (items like \"social diversification\" and \"mobile lifestyles\"). These CED specific terms should stay in the article as much as possible."
    }
   ],
   "against": "The simplified version was still preferred in most pairs (sheet 'ReadabilityExperiment-dev-inter', column K 'final preference': 23 'New' against 7 'Old' by my count), so on balance simplification helped.",
   "adds_to_existing": [
    18,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Use real images of the real places, objects and documents students may need to recognise; generated likenesses don't match what they will actually be shown.",
   "kind": "measured",
   "found_by": "Review of generated articles asked why generated images stood in for real monuments, and named famous real images to use instead.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'Articles-readable-exp', cell M12",
     "quote": "When there are historical examples like Angkor Wat or Angkor Tom, why aren't we using actual images? Students will probably have to be able to identify these images on the exam, so why are we relying on AI generated images which often do not resemble fow the image would look in an existing photograph?"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'APUSH Articles', cell M38",
     "quote": "I recommend that you use this famous image illustrating the Anaconda Plan - link"
    }
   ],
   "against": "Real images raise rights questions; one note accepted the generated images where a real one was under copyright (sheet 'APUSH Articles-readable-exp', cell M28: \"If this is copyrighted, the ones you have work.\").",
   "adds_to_existing": [
    22
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prefer pictures that carry information (maps, comparison charts, diagrams) over decorative scenes, and place each one next to the text it supports.",
   "kind": "measured",
   "found_by": "Review of generated articles repeatedly asked to swap scene images for maps or comparison charts and to move images beside the paragraphs they illustrate.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'APUSH Articles', cell M17",
     "quote": "The two images are placed back to back in the article. In addition, if it's possible to replace an image (I would replace image #1) with one that has some information, like a chart comparing the Virginia and New Jersey plans or one that compares the Federalists & Anti-Federalist positions, it would be a better use of space."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'APUSH Articles', cell M34",
     "quote": "This should include a map that shows the Missouri Compromise. I would recommend eliminating the 2 image in favor of it."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'Sheet3', cell A19",
     "quote": "It would be most efficient for the reader to see a chart/table here actually comparing the two movements characteristics"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    21,
    64
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Review generated text and images for stereotyped or insensitive portrayals of people, and for atrocities use symbolic or archival images rather than generated realistic ones.",
   "kind": "measured",
   "found_by": "Line-level review flagged a simplified sentence as reinforcing a stereotype, and flagged a generated illustration of an atrocity with people in it as insensitive.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'Sheet9', cell C15",
     "quote": "suggests that their performance skills made them stand out. Please rephrase this, as this is a bias that African Americans still face today, limiting roles and spheres of influence."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'APUSH Articles', cell M12",
     "quote": "I don't think we should illustrate a slave ship using AI, at least not with people on it. It could be considered by many to be insensitive. I would create an alternate image that's more symbolic or has to do with something else in the topic."
    }
   ],
   "against": "Only two instances were recorded and no systematic check existed, so how often this happens is unknown.",
   "adds_to_existing": [
    19
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Trace every statement in generated text back to a source fact and flag the rest; an automatic 'extra facts' check reported none, while review estimated one or two untraced statements in every article.",
   "kind": "measured",
   "found_by": "The article tracker's automated 'Extra Facts' column was empty for every article, yet the editorial notes said the writer added statements beyond the knowledge base in every article, and asked for a view showing each statement's source.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'Articles-readable-exp', cell K2 (column K header 'Extra Facts')",
     "quote": "[]"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
     "lines": "sheet 'Sheet4', cell H8",
     "quote": "We definitely have more (maybe around 1-2 statement in every article from llm) and some of it seems important as it really ties things together in the article"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/03-ARCHITECTURE.md",
     "lines": "65",
     "quote": "- Every claim in generated questions must trace to a VKB entry"
    }
   ],
   "against": "The same note says some of the added statements were useful connecting text (\"some of it seems important as it really ties things together in the article\"), so a statement with no source is not necessarily wrong.",
   "adds_to_existing": [
    38,
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After the final attempt, explain why the key is right and why each wrong option is wrong; a quarter of generated items shipped with no explanation at all.",
   "kind": "measured",
   "found_by": "A 582-item review found 139 items (25%) with no explanation. The validation rules required each explanation to cover the key and at least one wrong option.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/python/docs/EVALUATION-RESULTS-2026-02-23.md",
     "lines": "104",
     "quote": "**Frequency:** 139 questions (25% of all generated)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/python/docs/EVALUATION-RESULTS-2026-02-23.md",
     "lines": "106",
     "quote": "**Impact:** Students cannot learn from their mistakes without explanations"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/validation_rules.md",
     "lines": "299",
     "quote": "- Must explain why at least one wrong answer is wrong (for MCQ)"
    }
   ],
   "against": "Explanations are themselves a source of errors (letter mismatches failed 23% of items, per MCQ_BUG_HISTORY.md line 6), so each one needs its own consistency check.",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Across the items written for one objective, cover each part the objective names rather than going deep on one part.",
   "kind": "measured",
   "found_by": "Judges failed item sets that tested one named part of an objective in depth and skipped another.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
     "lines": "114",
     "quote": "The quiz omits the 'Caste' (Casta) system entirely."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_3/diagnosis.md",
     "lines": "76",
     "quote": "While the quiz covers the role of women and 'Republican Motherhood' with great depth, it fails the 70% threshold for concept coverage."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/COMPREHENSIVE-TEST-2026-02-17.md",
     "lines": "82",
     "quote": "the question completely fails to address the required sub-topic 'disease'"
    }
   ],
   "against": "The counts were small (1, 3 and 6 coverage failures in units 1–3, per the diagnosis headers), and covering every part across a set can conflict with keeping each item narrow.",
   "adds_to_existing": [
    41,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask only for knowledge the course teaches plus what the item supplies; a part that needs an obscure fact from outside the course can't be answered fairly.",
   "kind": "measured",
   "found_by": "Judges failed parts that required off-curriculum knowledge, and the writer rules then required core-curriculum content only.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter2.md",
     "lines": "58",
     "quote": "However, Part (c) requires specific knowledge of the Timber Culture Act (1873), which is not a standard APUSH curriculum topic"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
     "lines": "247",
     "quote": "• ALL parts must be answerable using CORE AP curriculum content"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report pass rates over everything requested, counting a failure to produce an item as a failure, alongside any 'scoreable only' figure; leaving errors out inflated headline rates.",
   "kind": "measured",
   "found_by": "One run reported a 78.9% 'effective' pass rate that was 50.6% of all requests. A 95.2% headline was 340 of 360 only after 3 errors were dropped from the denominator.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/PARTIAL_RESULTS_SUMMARY.md",
     "lines": "13",
     "quote": "| ✅ Passed | 243 | 50.6% (of 480) |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/PARTIAL_RESULTS_SUMMARY.md",
     "lines": "22",
     "quote": "- **Effective Pass Rate:** 78.9%"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/BENCHMARK_ACHIEVED.md",
     "lines": "4",
     "quote": "**Pass Rate:** **95.2%** (340/360 questions)"
    }
   ],
   "against": "The project excluded infrastructure errors on purpose (CHANGELOG.md line 171: \"- 503 errors from Gemini excluded from pass rate (infrastructure issue, not quality)\"). All 101 errors in the 480-item run came from a difficulty value the test plan requested but the generator never supported (PARTIAL_RESULTS_SUMMARY.md line 26).",
   "adds_to_existing": [],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_3/diagnosis.md",
   "lines": "90",
   "quote": "The inclusion of Document 7 (Anderson's 'Crucible of War') constitutes an answer giveaway."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/IMPROVEMENT_PROPOSALS.md",
   "lines": "192",
   "quote": "- Document 7 \"performs analysis for student\" (answer leakage)"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
   "lines": "101",
   "quote": "The 'stimulus' is essentially the curriculum fact restated verbatim rather than a primary source, document excerpt, image, or data set"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
   "lines": "28",
   "quote": "It can be answered entirely from outside knowledge about Portuguese Indian Ocean strategy without any engagement with the stimulus."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
   "lines": "433",
   "quote": "⛔ STIMULUS INTEGRATION TEST: Cover the stimulus. Can ALL parts be answered"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Articles-readable-exp', cell M16",
   "quote": "There is a reference to Sumni/Shia in the reflection but they are not mentioned in this reading."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "635",
   "quote": "DBQ passage_reference: questions aren't explicitly referencing their assigned document."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
   "lines": "10",
   "quote": "There are two defensible correct answers."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/mcq_set.py",
   "lines": "400",
   "quote": "TEST: \"Could an AP teacher argue this distractor is also correct?\" → if yes, CHANGE IT."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "528",
   "quote": "**CRITICAL INSIGHT:** MCQ_SET is failing almost entirely because all 3 questions have the same correct answer letter (e.g., A/A/A or B/B/B)."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "615",
   "quote": "- **answer_balance: NOT PRESENT** ← constraint completely fixed this"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md",
   "lines": "190",
   "quote": "When validation is uncertain, the safe choice is to fail (and regenerate) rather than pass (and ship broken content)."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/FACT_CHECK_RESULTS.md",
   "lines": "42",
   "quote": "- **Analysis:** The knowledge base may lack specific WWI domestic policy facts"
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf",
   "lines": "pdftotext -layout output, line 12638",
   "quote": "Clarity: Exam responses should be considered first drafts and thus may contain"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
   "lines": "83",
   "quote": "While Ricci's journals are real, this stimulus is a paraphrase/reconstruction rather than a direct quotation."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
   "lines": "130",
   "quote": "Fabricated poem falsely attributed to Wilfred Owen"
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Sheet9', cell C3",
   "quote": "The language here is too simplistic, it should use \"mobile,\" incorporated in the sentence in a natural way, instead of \"moved around\""
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'ReadabilityExperiment-dev-inter', cell L10",
   "quote": "Prefer the term, 'factor' over 'trend' because the exam will use the word 'factor' in questions"
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Sheet9', cell C71",
   "quote": "term typically used here is \"power vacuum\""
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
   "lines": "sheet 'Unit 2 Relationships', cell J103",
   "quote": "change to \"Native American\" from American Indian"
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
   "lines": "sheet 'Unit 1 Nodes', cell M91",
   "quote": "A short definition of feudalism should be included here."
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Sheet9', cell C43",
   "quote": "Not sure if non-religious/non-Protestant students know what this means."
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
   "lines": "sheet 'Unit 7 Nodes', cell M53",
   "quote": "context for the Senate's vote needs to be included for this to make sense"
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'AP Us Images QC', cell M65",
   "quote": "it lacks clear and distinct visual representations of *both* Latin American and Asian cultural influences as specified by the image caption and topic context."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Articles-readable-exp', cell M40",
   "quote": "Map of Treaty of Brest-Litovsk is included in gen ai article but it is not mentioned in text"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'AP Us Images QC', cell M35",
   "quote": "Several vehicles visible in the driveways and on the streets are clearly modern car models (e.g., SUVs, modern sedans), which are anachronistic for a 1950s Levittown setting."
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Articles-readable-exp', cell M39",
   "quote": "Text in image on gen ai article is nonsensical"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'APUSH Articles', cell M36",
   "quote": "The first image should be regenerated. The clothing is far too modern."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/VALIDATION-REPORT-15-45.md",
   "lines": "118",
   "quote": "**Experiments ran in isolation. Production hasn't been tested.**"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
   "lines": "78",
   "quote": "The `simple_api.py` transform layer was silently dropping fields before sending to the evaluator, causing failures."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/ULTIMATE-VALIDATION-REPORT-2026-02-18.md",
   "lines": "195",
   "quote": "| Non-MCQ bypass quality gate | `server.py` | MSQ/fill-in/match/article unvalidated |"
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/COMPREHENSIVE-VALIDATION-2026-02-18-1600.md",
   "lines": "65",
   "quote": "FACT_CHECK_ENABLED = False  # EXPERIMENT: Disabled for exp_12_minimal_gates"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/VALIDATION-REPORT-2026-02-19-COMPREHENSIVE.md",
   "lines": "184",
   "quote": "**The evaluator truncates articles to 3000 characters before showing them to Claude!**"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/FINAL_BENCHMARK_RESULTS.md",
   "lines": "38-40",
   "quote": "**Fix applied:** Match evaluator prompt + field name fix (`text` vs `content`)"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/GENERATOR_STATUS.md",
   "lines": "54",
   "quote": "| Pre-fix | 17.8% | Evaluator couldn't read new format |"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TEST-FINDINGS-2026-02-17.md",
   "lines": "26",
   "quote": "**Result:** Evaluator saw incomplete content → flagged as \"truncated\""
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/SAQ_RALPH_PROMPT.md",
   "lines": "17",
   "quote": "All 12 dimensions score 1.0, but overall score is 0.4-0.6."
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/workspace/INBOX_FROM_EXTERNAL/2026-04-28T00_first-contact.md",
   "lines": "49",
   "quote": "the eval cites scoring-directive text that doesn't exist in our outputs."
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TECHNICAL-DECISIONS.md",
   "lines": "30",
   "quote": "4. **Evaluation Alignment**: Pass substandard info to evaluation and score 0.0 if off-topic"
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/BENCHMARK-RIGOR-ANALYSIS.md",
   "lines": "48",
   "quote": "InceptBench is designed for K-12 Common Core (math/ELA). It doesn't cover:"
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/INCEPTBENCH_INTEGRATION_PLAN.md",
   "lines": "24",
   "quote": "DEFAULT_CURRICULUM = \"common_core\""
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
   "lines": "101",
   "quote": "The InceptBench evaluator has a **20% rating-flip rate** on identical generations across 4 repeated trials."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/evaluation_audit.md",
   "lines": "237",
   "quote": "The evaluator passed this but failed similar fill-in questions. Inconsistent application."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/TRAINING_DECISIONS.md",
   "lines": "133",
   "quote": "N=3 is safe under a noisy evaluator (InceptBench alpha 0.37–0.50)."
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "131",
   "quote": "The dimension tracking code had a Python falsy evaluation bug: `v.get(\"score\") or v.get(\"value\")` drops score=0.0 values (0.0 is falsy)."
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md",
   "lines": "176",
   "quote": "### 1. Test the validation function itself"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/BENCHMARK-RIGOR-ANALYSIS.md",
   "lines": "62",
   "quote": "3. **Create human validation set** - 50 gold standard questions (25 good, 25 intentionally bad)"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/EVALUATOR-TEAM-HANDOFF.md",
   "lines": "149",
   "quote": "3. Run against calibration set until it matches expected results"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/evaluation_audit.md",
   "lines": "319",
   "quote": "- **False negatives:** ~10-15% of failed questions (like the Match question above)"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/FACT_CHECK_RESULTS.md",
   "lines": "101",
   "quote": "- **Made-up dates:** No false dates found in test sample"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/URGENT-BUG-STILL-PRESENT.md",
   "lines": "35",
   "quote": "2. **The \"20/20 tests passing\" claim is misleading** - tests may be checking something else"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/PROMPT_EVOLUTION_2026-02-19.md",
   "lines": "5",
   "quote": "**Major Finding: All prompt variants achieved 100% pass rate.**"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/BENCHMARK-RIGOR-ANALYSIS.md",
   "lines": "64",
   "quote": "4. **Add adversarial tests** - wrong answer marked correct, anachronisms, explanation contradictions, factual errors in distractors"
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/AP US History - Knowledge Schema - SME Tracker.xlsx",
   "lines": "sheet 'Unit 7 Nodes', cell M131",
   "quote": "this agricultural depression may confuse students with the one that comes later."
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'Sheet9', cell C55",
   "quote": "section B should go before section A"
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
   "lines": "74",
   "quote": "There is significant overlap between parts (a) and (c)."
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_runs/analysis_iter1.md",
   "lines": "42",
   "quote": "The three questions do not adequately cover distinct AP historical thinking skills."
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MCQ_BUG_HISTORY.md",
   "lines": "203",
   "quote": "- External verification (Claude, not Gemini)"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/archive/OPENCLAW_HUMAN_REVIEW.md",
   "lines": "13",
   "quote": "I read each one as a human reviewer would"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/COMPREHENSIVE-AUDIT-2026-02-18.md",
   "lines": "80",
   "quote": "| Cognitive Demand | C- | Mostly recall, light analysis |"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/GEN5_OPTIMIZATION_REPORT.md",
   "lines": "112",
   "quote": "The 85% first-attempt rate was misleading - it was measuring something other than structural validity."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/orchestrator/course_checker_blueprint.md",
   "lines": "16",
   "quote": "Evaluator:   InceptBench v2.3.3"
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'APUSH Articles', cell M32",
   "quote": "This article is great, but the column F link does not contain any images. The images in the column H link look great."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/STATISTICAL_ANALYSIS.md",
   "lines": "239",
   "quote": "| Feb 22 | 91.7% | APGOV-only (biased) |"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'APUSH Articles', cell M21",
   "quote": "note that the google doc in H is the old version, the approved version is the s3 in column F"
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "175",
   "quote": "15 of 17 factual_accuracy hard-fails came from SAQ scoring notes."
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "183",
   "quote": "**Data:** factual_accuracy hard-fails: 17 -> 2."
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/generators/saq.py",
   "lines": "226",
   "quote": "3. States what does NOT earn the point (e.g., \"just naming X without explaining = 0\")"
  },
  {
   "truth": 56,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/curriculum/ceds/ap-european-history-ced.pdf",
   "lines": "pdftotext -layout output, line 12660",
   "quote": "Examples that earn this point include the following:"
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
   "lines": "157",
   "quote": "**Decision:** Always prefer verified curriculum facts over LLM-generated research. The LLM should construct questions FROM verified facts, not invent its own."
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/TRAINING_DECISIONS.md",
   "lines": "142",
   "quote": "| Prompt engineering for factual_accuracy | No effect | Model uses parametric memory, not prompted context |"
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "232",
   "quote": "- The 0.00 failures still occur despite facts injection — hard fails are from document CONTENT quality, not missing facts context"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TECHNICAL-DECISIONS.md",
   "lines": "21",
   "quote": "Users could select \"Seven Years' War\" but get a question about \"African and European musical traditions\"."
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/analysis/failure_analysis.md",
   "lines": "324",
   "quote": "- Questions set DURING a time period but not ABOUT the period's key content"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/docs/BENCHMARK-RIGOR-ANALYSIS.md",
   "lines": "44",
   "quote": "Our weighted average could theoretically pass with a factual error if other scores are high."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
   "lines": "35",
   "quote": "A factual error was identified in the third question of the set during the individual question evaluation, which voids the factual accuracy of the quiz as a whole."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
   "lines": "455",
   "quote": "**The question is not \"did scores go down?\" but \"WHY did they go down and is the fix addressing the right thing?\"**"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "609",
   "quote": "Gate 3's MCQ failures were about fabricated stimuli. Gate 4's failures are about clarity (ambiguous stems) and factual accuracy in the historian-framing argument."
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
   "lines": "148",
   "quote": "**Decision:** Flash research stage hallucinated facts that poisoned the compile step. MongoDB verified facts are better."
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Knowledge Schema Generator - AP USH Unit 1 - Instructions.csv",
   "lines": "40",
   "quote": "20. Run step 11 in main.py which is to generate relationships. This will be the very last step after the KS for the unit has been approved."
  },
  {
   "truth": 62,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "1257",
   "quote": "1. **LEQ fix works**: +15.9pp vs Gate 12b. The spec_compliance FORBIDDEN list genuinely helped."
  },
  {
   "truth": 62,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/VERSION_ANALYSIS.md",
   "lines": "232",
   "quote": "| Concrete bad examples | **Strong positive** |"
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/improvement_plan_prompts.md",
   "lines": "39",
   "quote": "- BANNED WORDS has no **detection/rejection mechanism** - it's advisory only"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "41",
   "quote": "Every generated item for these units had content matching the TOPIC but metadata saying the wrong TIME PERIOD. The evaluator saw the mismatch and issued automatic curriculum_alignment hard-fails."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "43",
   "quote": "**Impact:** 77 curriculum_alignment hard-fails in baseline. This single config error was responsible for the majority of all failures."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/CHANGELOG.md",
   "lines": "71",
   "quote": "4. **APWH unit correction.** The evaluator returns systematically wrong unit numbers for APWH standards — we fix them before evaluation."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "54",
   "quote": "The InceptBench evaluator marks decorative SAQ images as INFERIOR (hard-fail on stimulus_quality)."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark/CHANGELOG_RELENTLESS.md",
   "lines": "62",
   "quote": "the evaluator saw a document declared as \"visual\" with no actual image, triggering a stimulus_quality hard-fail. 17 such failures in the baseline."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/HANDOFF-finetune-status.md",
   "lines": "64",
   "quote": "**Result:** DBQ scores shifted 0.80-0.82 → 0.84-0.98. Overall 80% → 83.3%."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/benchmark_results/unit_1/diagnosis.md",
   "lines": "124",
   "quote": "Document 3 provides a text description of a painting instead of the image itself."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/k_12_social_studies/ap_files/Articles Tracker.xlsx",
   "lines": "sheet 'APUSH Articles-readable-exp', cell M45",
   "quote": "There is a map the text references but it is not included in the article."
  },
  {
   "truth": 64,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/03-ARCHITECTURE.md",
   "lines": "88",
   "quote": "- Political cartoons and images (descriptions for text-based generation)"
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/05-OPERATING-PRINCIPLES.md",
   "lines": "48",
   "quote": "| Increase retry count to dilute failures | ❌ Bandaid |"
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/03-ARCHITECTURE.md",
   "lines": "94",
   "quote": "- Each retry should address a specific failure mode, not be a random re-roll"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/TRAINING_DECISIONS.md",
   "lines": "133",
   "quote": "**Research:** RBoN (NAACL 2025): Vanilla BoN degrades beyond N~16."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/PLAN-finetune-qwen.md",
   "lines": "553",
   "quote": "- Score threshold actually correlates with quality (no false positives)"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/MSQ_FIX_RESULTS.md",
   "lines": "100",
   "quote": "1. **Deterministic**: Single-answer MSQs always fail, not dependent on model"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/EXPERIMENT_RESULTS_2026-02-18.md",
   "lines": "104",
   "quote": "- Prompt instruction alone doesn't enforce length"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "953",
   "quote": "Chinese character `绥靖` (\"suí jìng\", appeasement) embedded in English text."
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "961",
   "quote": "MCQ_SET hard-fail dimensions cascade: when factual_accuracy fails, educational_accuracy, concept_coverage, localization_quality, difficulty_distribution, non_repetitiveness, test_preparedness, answer_balance, stimulus_quality, and integrity_check all fail together."
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
   "lines": "129",
   "quote": "| apeuro u7 MCQ_SET | factual | One question in set has documented factual error | Per-question independent validation |"
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/TEST-FINDINGS-2026-02-17.md",
   "lines": "40",
   "quote": "Articles were being evaluated with question criteria (distractor_quality, etc.)"
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/FRESH_CLAUDE_EVAL_2026-02-17.md",
   "lines": "134",
   "quote": "**Root Cause**: The article evaluator is treating articles as MCQs, expecting \"question stem\" and \"answer options\"."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/python/CLAUDE.md",
   "lines": "311",
   "quote": "Never batch multiple fixes. Never skip local testing. Always measure before/after."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/data/model_findings.md",
   "lines": "231",
   "quote": "- Cannot measure impact: no A/B control in this run"
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/ap-social-studies-generator/docs/archive/RUN7_BLUEPRINT.md",
   "lines": "579",
   "quote": "- Can't isolate which change caused regression"
  }
 ]
}
```
