# read:incept-core

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "incept-core",
 "coverage": {
  "read": [
   "nova_forge/ root documents: README.md, EXECUTIVE_SUMMARY.md, EXISTING_GRADES_ANALYSIS.md, FAILURE_PATTERN_ANALYSIS.md, PASS_RATE_ANALYSIS.md, FIX_SUMMARY.md, PIPELINE_EVALUATION.md, DEPLOYMENT_TEST_RESULTS.md, MISSION_STATUS.md, AUTONOMOUS_MISSION.md, LIVE_STATUS.md, RUN_LOG.md, AGENT2_GRADES_3_8_BASELINE.md, AGENT3_EXECUTION_LOG.md, AGENT4_DECISIONS.md, [name]_REVIEW_2026-02-07.md (read, not cited), plus parts of AGENT3_SUMMARY.md, PIPELINE_READY.md, TEST_PLAN_GRADES_3_8.md, README_ANALYSIS.md, QUICK_REFERENCE.md; keyword scans of AGENT1, AGENT3_INDEX, AGENT3_PIPELINE_DOCS, AGENT6, BASELINE_QUICKSTART, QUICK_START, README_LOCAL_PIPELINE, GITHUB_REPO, DEPLOYMENT_GUIDE",
   "nova_forge/archive/old_docs/platform, gvc, root: all read or scanned; read in full BENCHMARK_FAILURE_ANALYSIS, PATTERN_ANALYSIS_RESULTS, CHECKPOINT_FEW_SHOT_REMOVAL, CHECKPOINT_SUMMARY, ITD_ENHANCED_FEW_SHOT, ENHANCED_FEW_SHOT_FINAL_STATUS, IMPORTANT_TECHNICAL_DECISIONS, PHASE1_CURRICULUM_SPEC_ENRICHER, PHASE2_MATH_AUDITOR, PROMPT_LENGTH_HANDLING, DEPLOYMENT_ITDS_AND_CRITICALS, SESSION_STEPS, GVC_V2_COMPREHENSIVE_VALIDATION, GVC_FINAL_ARCHITECTURE, GVC_ORCHESTRATOR_ARCHITECTURE, GVC_DEPLOYMENT_MANUAL, FINAL_STATUS_AND_NEXT_STEPS, NEXT_STEPS, root/INDEX",
   "nova_forge/docs/, qwen3-math/docs/ (all, incl. inceptml_full_report.md, inceptml_repository_story.md, TRAINING_FAILURES_REPORT.md), qwen3-math READMEs and delivery/README.txt, reward_training/ docs (HANDOVER, TRAINING_STRATEGY, ITD_PRIORITY_FIXES, TRAINING_RUN_LOG, FORMAT_SPECIFICATION, FINAL_TRAINING_READY, WHILE_TRAINING, READMEs)",
   "nova_forge/svg-llm/ README.md, TRAINING_BEST_PRACTICES.md, docs/REPORT_RECOMMENDATIONS.md, docs/SVG_GENERATION_STRATEGY.md, svg_pipeline/README.md",
   "nova_forge/inceptbench_lambda/TRAINING_GUIDE.md, question-gen-training/README.md, lambda_deployment/*.md (scanned), training/README.md, api/README.md",
   "nova_forge/scores/summary.txt, scores/*/results.txt (incl. aplit-quiz-generation), scores/*/sets/1/request.txt",
   "inceptlm/: README.md, docs/ (byte-identical to nova_forge/docs), training/README.md, api/README.md, quiz-frontend/README.md, scores/ (byte-identical to nova_forge/scores)",
   "incept-multilingual-generation/: README.md, incept_evaluator_documentation.md, DEPLOYMENT.md, instance_setup.md, spiky_points_of_view.json, src/evaluator/Readme.md, src/evaluator/reports/*.md, src/evaluator/EduBench/README.md, src/external_submodules/reading-question-qc/{README.md, BULK_GENERATOR_README.md, qc_pipeline/README.md, qc_pipeline/config/prompts.json, ck_gen - prompts.json}, demo_articles/*.md (scanned all, one in full), edu_configs/curriculum_grade_4.jsonl (first record only), edu_configs/di_formats.json (header only), data_visualization/*.html (text extraction; mostly JS shells), supabase/README.md, marketing-site/README.md, 2506.21734v3.pdf (pages 1-2, to identify it)",
   "incept-uae-api-website/: bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md (full), content/english/pages/*.md (all content pages), content/english/{inceptbench-docs,benchmarks,pedagogy,about}/_index.md, layouts (text spot checks), README.md and DEVELOPER_DOCS.md (template boilerplate), inceptapi.com/INCEPT_Benchmarking_Framework.html (full text), inceptapi.com/src/edubench_results.json, inceptapi.com/src/baseline_evaluation.json (summarised)"
  ],
  "skipped": [
   ".env, .env.local, .env.example and .claude/settings*.json in all four folders: credential files, never opened",
   "Code (.py, .ts/.tsx/.js, .yaml, .tf, .sh): scope is documents only",
   "Data dumps: grade-*-benchmark.jsonl, run-*.json, grade_*.json, qwen3_test_results.json, all *.csv, scores/*/sets/*/{raw,converted,scores}.json, ela-mock-fe evaluation jsonl, edu_configs jsonl beyond the first record, di_formats.json beyond its header, multilingual root qs*/output*/eval*/article_*/raw_*.json, *.xlsx, *.zip, sagemaker_endpoints.json",
   "Logs: api.log, balanced_test_full_logs.txt, generation_log.txt (empty), archive/temp_files/*.txt, *.log in incept-multilingual-generation, data/error_logs, data/logs",
   "Dependency, build and model folders: node_modules, .next, .git, .venv*, gvc_deployment/package*, reward_training/trained_models, bench.inceptapi.com/public (built copies of the content pages), themes/hugoplate",
   "Template boilerplate: blog posts, author pages, elements.md, privacy-policy.md, contact and testimonial sections",
   "Model-training mechanics (GPU/OOM, learning-rate/KL tuning, SageMaker/K8s/vLLM/Lambda deployment, credential rotation): read but excluded from candidates per scope",
   "Outside the four folders: incept/ML_TRAINING_INSIGHTS_REPORT.md and the AP-specific sibling folders (ap_benchmark, ap-benchmark-standalone, aplit-quiz-generation); personal/ never touched"
  ],
  "notes": "Many nova_forge documents report projected or 'expected' pass rates and per-layer 'Result' figures that no scored run backs; only measured numbers were used as measurements, and projections are cited as claims (see the claims-before-measurement candidate). AP-related material inside scope: the AP literature quiz generator's score files show the lowest keyed-answer accuracy of all benchmarks (66.7% at v1.4.0, 68.3% at v1.1.7), used as evidence for truth 6. Knowledge-related material: the pedagogy framework's knowledge-rich pillar and vocabulary targets, cited for truths 18 and 20. The one name-bearing file (nova_forge/[name]_REVIEW_2026-02-07.md) states outright that the 62% 'missing type field' diagnosis was wrong and that the 16 zero scores were generation failures. It is not cited: the misdiagnosis and pipeline-fault candidates rest on other files, so name_bearing_source is false throughout. I did not treat the shared home-directory prefix of every path as name-bearing. Several in-scope documents contain live-looking cloud access keys, API keys and service app IDs: AUTONOMOUS_MISSION.md, inceptbench_lambda/TRAINING_GUIDE.md, ENHANCED_FEW_SHOT_FINAL_STATUS.md, the GVC docs, SECURITY_* docs and the name-bearing review. None are reproduced here, and they are worth rotating. Person names appear inside some data fields (reviewer columns in the curriculum jsonl, localization name lists) and were not used. The EduBench task codes appear with different expansions across project documents. EC is Error Correction in the benchmark itself and in the project README, but Educational Curriculum Alignment in the benchmark report. IP is Idea Provision, Instructional Planning, Inference & Pedagogy or Improved Prompting, depending on the document. The PDF in the multilingual repo is an unrelated ML-architecture paper."
 },
 "candidates": [
  {
   "statement": "Give the writer the same specification the item will be judged against; a writer that never sees a boundary, a difficulty definition or a required format will break it.",
   "kind": "measured",
   "found_by": "A judged run of 197 generated items passed at 3.6%. The generator received empty curriculum metadata, and the wrapper had already stripped assessment boundaries, difficulty matrices, learning objectives and misconceptions to fit the prompt. The judge scored against exactly those fields, and 139 difficulty mismatches and 114 constraint violations followed. A validator given no boundaries likewise passed failing items and left the pass rate at 7%.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md",
     "lines": "62",
     "quote": "The model generates a 3-year interest problem because it doesn't know about the \"single year\" constraint. The evaluator fails it for violating a boundary the model never saw."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md",
     "lines": "125-130",
     "quote": "| Difficulty mismatch | 139 | Model ignores difficulty_definition |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/PROMPT_LENGTH_HANDLING.md",
     "lines": "49-54",
     "quote": "**Approach:** Strip verbose fields under `skills.substandard_metadata` before prompt construction:"
    }
   ],
   "against": "The size of the gain after the spec was injected is not isolated. The fix was logged as '- Pass rate improved from 8% → 60-75% (expected)' (inceptlm/README.md line 103). The next scored run, '- **Pass Rate:** 41.0% (121/295)' (nova_forge/RUN_LOG.md line 44), used a different item set and included other changes.",
   "adds_to_existing": [
    33
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When an item depends on a picture, table or model, a missing one fails the item: don't ship the text without it, and don't just delete the reference when the skill needs that representation.",
   "kind": "measured",
   "found_by": "The generator was set to keep serving questions when diagram generation failed. Across 1,888 judged items, 168 were unsolvable because the referenced diagram, table or number line was absent. Items that dropped the model no longer assessed a skill defined as using models.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/IMPORTANT_TECHNICAL_DECISIONS.md",
     "lines": "451-453",
     "quote": "**Decision:** Continue serving requests even if SVG generation fails, returning questions without images."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "302",
     "quote": "- **Missing Stimulus:** 168 questions unsolvable without images"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "377-379",
     "quote": "- Issue: The question targets “with models” but provides no models to interpret, so it does not assess the intended skill."
    }
   ],
   "against": "Rewriting the text helped but did not pass: '• Fixed questions improved from 0.60 avg → 0.76 avg (+16 points)' after '• Main issues fixed: References to missing images/figures' (qwen3-math/delivery/README.txt lines 36-37). That is still under the 0.85 pass mark. The image strategy listed '- Block question delivery on SVG failure' as a DON'T (svg-llm/docs/SVG_GENERATION_STRATEGY.md line 69), right after noting '**Result: Questions are unusable without visuals**' (line 18).",
   "adds_to_existing": [
    64
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Define each difficulty level per skill and check every label against that skill's own definition; one global rule for 'easy' or 'hard' mislabels items.",
   "kind": "measured",
   "found_by": "Difficulty alignment was the second-largest failure in 1,888 judged items: 564 of 1,410 failures. The analysis traced it to generic guidance, while the curriculum defines levels per skill (for example, which step of a pattern is asked about).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
     "lines": "80-83",
     "quote": "- Generic difficulty guidance (\"EASY: small numbers\") doesn't match specific requirements"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "56",
     "quote": "2. **Difficulty Alignment** - 564 failures (40.0%)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/edu_configs/curriculum_grade_4.jsonl",
     "lines": "1",
     "quote": "\"difficulty_matrix\": \"EASY\\n- Steps one to three are given and the question asks about step 4."
    }
   ],
   "against": "The pipeline then hard-coded one rule for every skill, \"'easy': (100, 999),\" (nova_forge/FIX_SUMMARY.md line 71). Its README reports '- **Result**: <1% range errors (was 15%)' (nova_forge/README.md line 197), with no scored run behind it.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Judge whether an item suits its level by comparing it with validated items at that level, weighing the inference it demands and the strength of its wrong options.",
   "kind": "adopted rule",
   "found_by": "The reading QC pipeline's difficulty check retrieves the five most similar validated benchmark items for the grade. It then rates the candidate as appropriate, too hard or too easy, using inference load and distractor strength as the two dimensions.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "43",
     "quote": "A set of the 5 most semantically similar validated test questions that are considered benchmarks for the specified grade level"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "43",
     "quote": "1.  **Level of Inference Required:** The cognitive steps a student must take to arrive at the correct answer (Low, Moderate, High)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "94-96",
     "quote": "- Assessed against benchmark questions from the same grade"
    }
   ],
   "against": "The check runs only when benchmark items are supplied: '- Question QC with both keys + --examples: 10-11 checks (adds too-close and difficulty)' (qc_pipeline/README.md line 236). No agreement with person ratings is recorded.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build each wrong option from a specific, likely error, so a choice shows what the learner misunderstood; options that are all correct, implausible or unrelated diagnose nothing.",
   "kind": "measured",
   "found_by": "On 36 judged items from a live generator, distractor quality was the most frequent zero (16/36), with reveals-misconceptions next (12/36). In the 1,888-item analysis, an item whose options were all correct could not separate understanding from error.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
     "lines": "368-370",
     "quote": "- `distractor_quality` (16/36)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
     "lines": "404",
     "quote": "- Distractors are often not tied to *specific misconceptions* (diagnostic weakness)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "489-491",
     "quote": "- Issue: Because every option is correct, the item cannot differentiate between correct understanding and common errors."
    }
   ],
   "against": "Distractor fixes were rated low-impact among near misses: '| Distractors | 30 | ⭐⭐⭐ HARDER (content) | Low |' (nova_forge/README.md line 303).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check that options differ in meaning, not just in wording; identical or equivalent options leave more than one right answer and no real distractor.",
   "kind": "measured",
   "found_by": "In two 298-item runs that passed at 3.7% and 3.0%, factual accuracy failed on 78% of items, including items whose four options were identical. The production wrapper later rejected equivalent options such as 1/2 and 5/10, and the reading QC checks for near-synonymous distractors.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md",
     "lines": "21-24",
     "quote": "- All options are identical (e.g., all 4 choices say \"Four thousand five hundred sixty-seven\")"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
     "lines": "73",
     "quote": "- Avoid **equivalent distractors** (e.g., `1/2` vs `5/10`) unless multi-answer is supported."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "21",
     "quote": "Synonymous or Near-Synonymous**: Uses different wording but conveys essentially the same meaning"
    }
   ],
   "against": "Equivalent options are allowed when all of them are keyed: the rule holds only 'unless multi-answer is supported' (inceptml_full_report.md line 73).",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep options parallel in grammar, category, length and detail so the right answer can't be spotted by its form, such as being the longest or most specific.",
   "kind": "adopted rule",
   "found_by": "The reading-question generation prompts and the published reading QC rubric both adopted length, specificity, grammatical and category balance checks to stop the key standing out by its form.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json",
     "lines": "12",
     "quote": "The correct answer MUST NEVER be the longest option."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "72-74",
     "quote": "- Prevents patterns where correct answer is consistently longest/shortest"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "64-66",
     "quote": "- Prevents correct answer from being notably more specific or vague than distractors"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3,
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "On an item with several right answers, say how many to choose and check each option's truth on its own.",
   "kind": "measured",
   "found_by": "Across 1,888 judged items, multiple-select items had the lowest pass rate: 15.27% overall, and 0% for one grade's 20 items. Their failures included keys that omitted correct options and no guidance on how many to select.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "75-81",
     "quote": "**Key Finding:** MSQ (Multiple Select Questions) have the lowest pass rate overall, with Grade 6 having 0% pass rate on MSQs."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "80-84",
     "quote": "- **Issue:** Missing guidance on how many answers to choose creates ambiguity for students."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "244-246",
     "quote": "- Issue: The labeled correct answer is wrong. 324 is divisible by 2, 4, and 9, but the key lists only A."
    }
   ],
   "against": "The 0% subgroup is small: '- **Grade 6 MSQ (20 questions):** 0% pass rate - all failing' (EXECUTIVE_SUMMARY.md line 296).",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check the whole item for agreement — the stem asks for what the options offer, the key names an option that exists, and the explanation supports the key; checking only the final answer misses the rest.",
   "kind": "measured",
   "found_by": "An answer-only math checker reported zero errors while the judge failed factual accuracy on 34 items. The judged failures included keys contradicted by their own explanations, stems that asked for a model while offering numbers, and keys naming options that did not exist.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
     "lines": "116-121",
     "quote": "- Wolfram validates the answer but not the explanation steps"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md",
     "lines": "137-139",
     "quote": "- Generated: Answer \"A\" but explanation proves \"B\" is correct"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "74-78",
     "quote": "- **Issue:** The stem asks for a model, but only numeric answers are provided and no model is shown, creating conflicting cues about what action is required."
    }
   ],
   "against": "The answer-only checker's own verdict was '- **Result:** ✅ All math is already correct!' (archive/old_docs/gvc/GVC_FINAL_ARCHITECTURE.md line 60).",
   "adds_to_existing": [
    59,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check that an item exercises the named skill itself, not a neighbouring skill on the same topic.",
   "kind": "measured",
   "found_by": "Curriculum-alignment failures were 122 of 1,410 in one analysis and 6 of 36 in another set ('often due to operation mismatch vs stated skill'). They were items that computed instead of modelling or writing an equation, or that used an operation the skill excluded.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "128-132",
     "quote": "- **Issue:** The task assesses basic subtraction rather than writing a one-step equation, which the stated standard/lesson emphasizes."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
     "lines": "406",
     "quote": "- Skill metadata can drift (questions sometimes include multiplication when the skill says add/sub only)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "27",
     "quote": "The question must directly assess the standard's specific skill, not a tangentially related skill."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Feedback on a wrong choice should name the specific error behind that choice and point to the evidence against it, not say a generic 'try again'.",
   "kind": "adopted rule",
   "found_by": "The explanation QC rubric scores feedback on each distractor for three things: the specific error, the misconception behind it, and textual refutation. The published rubric repeats the requirement.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "65",
     "quote": "It should explain what makes this specific option incorrect"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "69",
     "quote": "The feedback must categorize or name the type of thinking error"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "130-132",
     "quote": "- Identifies the specific error or misconception that led to the incorrect choice"
    }
   ],
   "against": "The same rubric also requires giving the answer away: 'The feedback must either explicitly state the correct answer or clearly guide the student to it' (qc_pipeline/config/prompts.json line 77).",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Audit the judge prompt that actually runs, not the rubric's description of it; the two can require opposite things.",
   "kind": "measured",
   "found_by": "I compared the published reading QC rubric with the pipeline's prompt config. The page says distractor feedback guides 'without giving it away directly', but the running prompt passes feedback that states the correct answer outright.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "142-144",
     "quote": "- Provides a path to the right answer without giving it away directly"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "77",
     "quote": "The feedback must either explicitly state the correct answer or clearly guide the student to it"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before reporting a score, confirm what its evaluator actually measures; a borrowed benchmark's task scores were reported as quality dimensions they never measured.",
   "kind": "measured",
   "found_by": "The external benchmark's Error Correction task scores how well a model responds to an item when asked to correct errors. A benchmark report presented that score as the items' 'Curriculum Alignment', at 10.00/10 across 873 items. The code IP is expanded four different ways across the project's documents: Idea Provision, Instructional Planning, Inference & Pedagogy and Improved Prompting.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md",
     "lines": "41",
     "quote": "#### 2. Educational Curriculum Alignment (EC) - Weight: 45%"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/EduBench/README.md",
     "lines": "54",
     "quote": "- Error Correction (EC)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/Readme.md",
     "lines": "122",
     "quote": "1. **`edubench_tasks`** (AI Model Response Testing): Tests how well an AI model (EDU-Qwen2.5-7B) can respond to your question across 6 task types (QA, EC, IP, AG, QG, TMG). This validates that your question is clear enough for AI to understand."
    }
   ],
   "against": "The repurposing was deliberate in the framework document, which describes the Error Correction row as 'Tests curriculum alignment and educational appropriateness. Does content match grade-level standards?' (incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html lines 261-263).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Report a generator's quality over everything it produced, counting what was removed; averaging only the items that survived a score filter inflates the result.",
   "kind": "measured",
   "found_by": "A benchmark report averaged 9.28/10 after keeping only items that scored at least 8.0, using a script that deletes low scorers from the database. An unfiltered 300-item run of the same pipeline averaged 8.48.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md",
     "lines": "81",
     "quote": "3. **Quality Filtering:** Only questions scoring ≥8.0/10.0 are retained in the dataset"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md",
     "lines": "13",
     "quote": "- **Weighted Overall Score:** 9.28/10.0"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/reports/evaluation_13-01-37_report.md",
     "lines": "17",
     "quote": "| **Weighted Score** | **8.48/10.0** | 300 |"
    }
   ],
   "against": "This is not a controlled comparison. The filtered report covers '- **Evaluation Period:** September 30, 2025 to October 02, 2025' (incept_benchmark_report.md line 17) across five grades, while the 8.48 run is a single grade-3 set.",
   "adds_to_existing": [
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Name the evaluator and version with every score and compare only within one; re-scoring the same item sets moved scores by up to five points and reversed the order of two generators.",
   "kind": "measured",
   "found_by": "The same benchmark sets were re-scored under different evaluator versions. The 60-item set went from 0.661 (v1.1.7) to 0.712 (v1.4.0), while the 82-item set went from 0.663 (v1.1.5) to 0.654, so the two swapped places. Within v1.4.0, one sub-evaluator scored the two sets 0.823 and 0.605, while another scored them 0.602 and 0.704.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/benchmarks/_index.md",
     "lines": "54-57",
     "quote": "| APLIT Quiz Generation | 0.661 (66%) | 0.832 | 0.612 | 68.3% | 60 (3 sets) | 1.1.7 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/scores/summary.txt",
     "lines": "38-41",
     "quote": "APLIT Quiz Generation        | 0.712 (71%) | 0.823   | 0.602      | 66.7%    | 60 (3 sets) | 1.4.0"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/scores/summary.txt",
     "lines": "40",
     "quote": "SAT Reading Generation       | 0.654 (65%) | 0.605   | 0.704      | 100.0%   | 82 (3 sets) | 1.4.0"
    }
   ],
   "against": "The version labels themselves are unreliable. The table is introduced with 'Results from evaluating various content generation systems using InceptBench v1.3.0.' (benchmarks/_index.md line 52), but its rows list versions 1.1.5 to 1.2.0. One set is recorded as 'InceptBench Version: mixed (1.4.0, unknown)' (nova_forge/scores/ela-mock-fe/results.txt line 4).",
   "adds_to_existing": [
    34,
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Claim an improvement only from a scored run of real output; projected gains, mock tests and blank test templates are not results.",
   "kind": "measured",
   "found_by": "A validation pipeline was declared complete on 95% mock-test success and a 99% 'projected' pass rate. Its README stated per-layer 'Result' figures, while the deployment test record stayed 'PENDING'. A later live comparison of six pipelines found this pipeline at 0% reliability, with its six validation layers 'not functioning' and every request producing addition problems.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/AGENT3_EXECUTION_LOG.md",
     "lines": "505-513",
     "quote": "| Pass Rate | 41% | 99% (projected) | +58% |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/README.md",
     "lines": "186-189",
     "quote": "- **Result**: 0% missing type fields (was 62%)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PIPELINE_EVALUATION.md",
     "lines": "84-95",
     "quote": "- \"6-layer validation\" not functioning"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Name a failure's cause from the judge's stated reasons on the failing items, not from a field the failing items happen to share.",
   "kind": "measured",
   "found_by": "A missing format field was blamed for 62% of failures, with a projected gain of 30-40 points from adding it. The analysis's own example item was failed by the judge for a disallowed option. In the same run, the judge's stated reasons for specification failures were rule violations in the content: disallowed options, missing units and models, and wrong stem forms.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
     "lines": "43",
     "quote": "- All questions with 0.00 spec compliance score are missing `content.type`"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
     "lines": "45",
     "quote": "- Example from failed question cc-math-4-mcq-easy-6:"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "292-293",
     "quote": "- Issue: Violates the boundary to use only >, <, and = by including \"+\" as an option."
    }
   ],
   "against": "The project recorded the field fix as a success, '| Type Field Present | 38% | 100% | +62% |' (nova_forge/README.md line 228), but no scored run after the fix is recorded.",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Rule out pipeline faults before reading a low score as a content failure; an empty or misparsed field scores like a bad item.",
   "kind": "measured",
   "found_by": "Fill-in and multi-select items both passed at 0% while the answer extractor read only one field name. Fill-in keys were empty, and the judge saw an empty multi-select key whose explanation named B and C. The 0% was attributed to missing examples. Separately, in a 295-item run, 16 items scored 0.0 with no question text (AGENT2_GRADES_3_8_BASELINE.md lines 86 and 104).",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md",
     "lines": "126-131",
     "quote": "1. **Bug Found:** Fill-in answers were empty because code only looked for `correct_answer`"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md",
     "lines": "152-158",
     "quote": "Answer field is [\"\"] but explanation states correct choices are B and C"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md",
     "lines": "45-48",
     "quote": "1. **Targeted Learning:** Fill-in questions were 0% pass rate because model had no fill-in examples"
    }
   ],
   "against": "The two causes were fixed in the same deployment, so the record never isolates either: '| 2 | Type-specific examples | Fixes 0% fill-in/MSQ | ✅ Deployed |' and '| 4 | Multi-field answer extraction | Fixes empty answers | ✅ Deployed |' (ITD_ENHANCED_FEW_SHOT.md lines 491 and 493).",
   "adds_to_existing": [
    9,
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure how often a check fires on good items before it gates; an over-eager check drives regenerate loops that empty the output.",
   "kind": "measured",
   "found_by": "A retry loop built on code-only math validators was recorded as producing 'false positives' and regenerating blindly. It was logged as failed, with 0% fill and 0-5% pass, and replaced. The replacement checker then fired on nothing: it found zero math errors in 257 items while the judge kept finding factual errors.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/gvc/GVC_DEPLOYMENT_MANUAL.md",
     "lines": "5",
     "quote": "This deploys the **Generate-Validate-Correct (GVC) Architecture** to replace the failed Phase 2 (math auditor retry loop)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/gvc/GVC_DEPLOYMENT_MANUAL.md",
     "lines": "109-115",
     "quote": "| Validation | Python-only (false positives) | Wolfram Alpha (definitive) |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/gvc/FINAL_STATUS_AND_NEXT_STEPS.md",
     "lines": "118-122",
     "quote": "| Fill rate | 0% | 80-90% |"
    }
   ],
   "against": "The records disagree on the outcome: '| Pass rate | 5% | Target: 15-25% |' (GVC_DEPLOYMENT_MANUAL.md line 115) against 0% (FINAL_STATUS_AND_NEXT_STEPS.md line 122). The false-positive rate itself was never itemized.",
   "adds_to_existing": [
    37,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Model judges rate generated educational content higher than people do and agree with them only moderately, so calibrate a model judge against person ratings before trusting its scores.",
   "kind": "external research",
   "found_by": "The external benchmark bundled in the evaluator, EduBench (https://arxiv.org/pdf/2505.16160), reports model-judge and human scores for the same outputs. A 7B model averaged 8.46 from one model judge but 7.50 from people. The benchmark notes that model evaluations do not fully align with human judgments; Kendall's W against humans is 0.56-0.63.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/EduBench/README.md",
     "lines": "121-125",
     "quote": "|                 | Qwen2.5-7B-Instruct    | 8.34 | 9.01 | 8.64 | 8.16 | 6.64 | 9.33 | 8.75 | 8.23 | 9.06 | 8.46 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/EduBench/README.md",
     "lines": "141-145",
     "quote": "|                 | Qwen2.5-7B-Instruct    | 6.78 | 7.63 | 7.93 | 7.74 | 6.79 | 7.86 | 7.79 | 7.55 | 7.42 | 7.50 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/EduBench/README.md",
     "lines": "218",
     "quote": "- **Consistency between humans and models**: The model evaluations do not fully align with human judgments, which may be due to limited understanding of the evaluation criteria by the models."
    }
   ],
   "against": "The rankings agree at the extremes: 'In Table 2, DeepSeek R1 and Qwen2.5-7B-Instruct still show the best and worst performances, respectively, which are consistent with the model-based evaluation results.' (EduBench/README.md line 193).",
   "adds_to_existing": [
    37,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Expect generated items to fall short most at the hardest levels and highest grades, and check difficulty hardest there.",
   "kind": "measured",
   "found_by": "Across 1,888 judged items, pass rates fell from 34.35% for easy items to 26.28% for medium and 14.14% for hard; one grade's hard items passed at 1.54%. A separate generator's notes record that higher-grade requests produced simpler, lower-grade questions.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "85-89",
     "quote": "| **Hard** | 587 | 83 | 504 | 14.14% |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "87",
     "quote": "| **Easy** | 658 | 226 | 432 | 34.35% |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/svg-llm/README.md",
     "lines": "43-45",
     "quote": "- Grades 9-10 produce elementary-level questions"
    }
   ],
   "against": "The gradient is not uniform. Within one grade alone, 'Performance is nearly identical across all difficulty levels' (AGENT2_GRADES_3_8_BASELINE.md line 60).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Judge a question set as a whole: it should span recall, inference and evaluation, with no single kind of demand in more than 70% of items.",
   "kind": "adopted rule",
   "found_by": "The reading-question generator's QC includes a set-level check that fails a set dominated by one competency. The pedagogy framework asks questions to progress from recall to application to reasoning.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json",
     "lines": "114",
     "quote": "No single competency should dominate (>70% of questions)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "262-263",
     "quote": "Questions move from basic recall to application to reasoning, helping students strengthen understanding step by step."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Localize names, places and settings only where they serve the objective; keep the concept, standard units and any context the lesson needs unchanged.",
   "kind": "adopted rule",
   "found_by": "The evaluation framework scores localization but lists what must not be localized. The generator's cultural guidelines limit cultural points to those relevant to the learning objective and put educational accuracy first.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html",
     "lines": "545-550",
     "quote": "Universal mathematical/scientific concepts"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/spiky_points_of_view.json",
     "lines": "125",
     "quote": "Only apply spiky points that are genuinely relevant to the learning objective"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/spiky_points_of_view.json",
     "lines": "126",
     "quote": "Maintain educational accuracy while incorporating cultural perspectives"
    }
   ],
   "against": "The same file also directs cultural framing everywhere: 'Prioritize Arabic and Islamic perspectives in all explanations.' (spiky_points_of_view.json line 9).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Revisit each skill at growing intervals and mix earlier items into later practice, so retention is checked rather than first success.",
   "kind": "adopted rule",
   "found_by": "The pedagogy framework behind the evaluators makes spaced repetition and cumulative practice one of its pillars, and lists cumulative review as an attribute of a good question.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "97-99",
     "quote": "Students revisit key skills at increasing intervals \\- after a day, a few days, a week, and beyond."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "271-272",
     "quote": "Later questions intentionally revisit earlier concepts to test retention and fluency."
    }
   ],
   "against": "none found (adopted without a project measurement)",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "For learners who are behind, keep the task's demand and add support (guided steps, vocabulary, targeted practice) instead of giving easier material.",
   "kind": "adopted rule",
   "found_by": "The pedagogy framework's guidance for students behind grade level.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "141-145",
     "quote": "Do not lower the cognitive demand of material. Instead, scaffold with guided reading, vocabulary support, and targeted practice."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Teach one well-defined skill per lesson and remove anything that doesn't serve it.",
   "kind": "adopted rule",
   "found_by": "The pedagogy framework's first attribute of a good lesson, and its cognitive-load rule.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "207-208",
     "quote": "Each lesson targets one skill or concept only. Students should know exactly what they are learning and why it matters."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "91",
     "quote": "Each focuses on a single, well-defined skill."
    }
   ],
   "against": "A criticism the site itself records against the approach: '- May not fully encourage critical thinking or open-ended exploration' (content/english/pages/direct-instruction.md line 63).",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Move a learner on only after independent, unprompted performance shows mastery; recognition with hints doesn't count.",
   "kind": "adopted rule",
   "found_by": "The pedagogy framework's mastery-learning rule, and its rule that every practice cycle ends with recall without hints.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/direct-instruction.md",
     "lines": "32-36",
     "quote": "Progression to the next lesson occurs only when students demonstrate mastery of current material."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "380",
     "quote": "Every cycle ends with independent recall \\- typing or saying the word without hints \\- to confirm mastery."
    }
   ],
   "against": "A criticism the site itself records against the approach: '- Sometimes criticized for being too rigid or prescriptive, potentially limiting teacher creativity' (content/english/pages/direct-instruction.md line 62).",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Teach and test a concept with examples and near-miss non-examples, so the learner has to tell close meanings apart.",
   "kind": "adopted rule",
   "found_by": "The pedagogy framework's definition of an effective question for learning a concept.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "407-410",
     "quote": "Present examples and near-misses, prompting learners to discriminate between related meanings."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Test a content generator with several phrasings of each request; its quality should not depend on how the request is worded.",
   "kind": "adopted rule",
   "found_by": "The benchmark's request set was designed to vary the wording of the same skill requests, alongside difficulty and item type.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "493-498",
     "quote": "Semantic variation \\- The same skills and topics are described in various semantically similar ways while sending requests to the LLM"
    }
   ],
   "against": "No results were recorded for the benchmark that uses it: '| Coming Soon | - | - | - | - |' (content/english/pages/uae-mathematics.md line 131).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Report a well-formed-output rate separately from judged quality; passing a structure or parse check says nothing about whether an item is right.",
   "kind": "measured",
   "found_by": "A live tracker headlined a 90.0% 'Overall Pass Rate' whose only listed failures were empty answers, missing fields and parse errors. The recommended production pipeline was picked on 20/20 parse reliability and 6/6 math checks, while the same evaluation notes that it 'Sometimes ignores themed instructions'.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/LIVE_STATUS.md",
     "lines": "5-7",
     "quote": "# 90.0% (54/60)"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/LIVE_STATUS.md",
     "lines": "20-26",
     "quote": "- **Empty or null 'answer'**: 2 occurrences"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PIPELINE_EVALUATION.md",
     "lines": "26-33",
     "quote": "| Reliability | **100%** (20/20 benchmark tests) |"
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
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/uae-mathematics.md",
   "lines": "38",
   "quote": "6. **Explanation Quality** - Explanations guide learning vs stating answers. Flag \"leakage\" if reveals exact option text."
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
   "lines": "142-144",
   "quote": "- Provides a path to the right answer without giving it away directly"
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
   "lines": "73",
   "quote": "The feedback must cite specific passage content that contradicts the wrong answer"
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
   "lines": "77",
   "quote": "The feedback must either explicitly state the correct answer or clearly guide the student to it"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/BENCHMARK_FAILURE_ANALYSIS.md",
   "lines": "69-75",
   "quote": "The diagram itself displays '135°,' giving away the answer before the student attempts the problem."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html",
   "lines": "496",
   "quote": "Scaffolding should guide students through problem-solving without revealing answers prematurely."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/glossary.md",
   "lines": "110",
   "quote": "Includes hard-fail gates for inappropriate content or answer leakage"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/demo_articles/grade4_fractions.md",
   "lines": "20-34",
   "quote": "**D)** 1/8 + 1/8 + 1/8 ✓"
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
   "lines": "105-107",
   "quote": "When students make errors, they are guided through the correct reasoning right away."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json",
   "lines": "96",
   "quote": "Determine whether a student must read this specific passage to answer the question correctly, or if they could answer it using general knowledge."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
   "lines": "21",
   "quote": "Equally Text-Supported**: Both correct answer and distractor are equally supported by passage evidence"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/scores/aplit-quiz-generation/results.txt",
   "lines": "8-13",
   "quote": "Accuracy:         66.7%"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/answer-verification.md",
   "lines": "100-105",
   "quote": "- **●●○○○○○○○○ (0-4)**: Low - manual review recommended"
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
   "lines": "384",
   "quote": "By **mastering roughly 300–400 high-utility academic words per grade level**, students gain the linguistic precision needed for strong reading comprehension and confident written expression."
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
   "lines": "342",
   "quote": "Vocabulary is taught explicitly and revisited frequently to connect decoding with comprehension, while background knowledge is deliberately built into texts to support understanding and schema formation."
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/svg-llm/svg_pipeline/README.md",
   "lines": "40-44",
   "quote": "3. **Verifiable by construction** - If params extracted correctly, SVG is correct"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/svg-llm/TRAINING_BEST_PRACTICES.md",
   "lines": "65-79",
   "quote": "- Manually review 20 generated SVGs"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
   "lines": "380-383",
   "quote": "- the wrapper filtered with `if validate_question(q)` but returned the original `q`"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/demo_articles/grade4_fractions.md",
   "lines": "52-56",
   "quote": "![Generated visual]([IMAGE_2])"
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
   "lines": "425",
   "quote": "| **Word Length (Questions / Items)** | 5–10 words per question. | 10–15 words per question. | 15–25 words per question. |"
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
   "lines": "95",
   "quote": "The feedback should be between 1-4 complete sentences"
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/BULK_GENERATOR_README.md",
   "lines": "10-12",
   "quote": "- Questions failing ≤1 QC check are tentatively accepted"
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/PHASE2_MATH_AUDITOR.md",
   "lines": "18-20",
   "quote": "- Attempt 3: force‑accept to guarantee output"
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/README.md",
   "lines": "119-122",
   "quote": "- Each check returns 0 (fail) or 1 (pass)"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/gvc/NEXT_STEPS.md",
   "lines": "13-21",
   "quote": "❌ Claude not finding format problems"
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/gvc/NEXT_STEPS.md",
   "lines": "32-34",
   "quote": "Claude is being asked to validate format, but it doesn't have the **specific assessment boundaries** that InceptBench uses."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/EduBench/README.md",
   "lines": "217-218",
   "quote": "- **Consistency among evaluation models**: The models show high consistency, with almost all Kendall's W values above 0.5 and most around 0.6, indicating strong agreement."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
   "lines": "116-118",
   "quote": "- GVC shows \"math_errors_found: 0\" but InceptBench still finds issues"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md",
   "lines": "15",
   "quote": "- **Educational Curriculum Alignment (EC):** 10.00/10.0 (n=873)"
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/direct-instruction.md",
   "lines": "46-52",
   "quote": "1. **Review and warm-up** - Recall prior knowledge"
  },
  {
   "truth": 42,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
   "lines": "208",
   "quote": "**Recommendation:** Consider regenerating questions scoring below 0.60 (97 questions) rather than fixing."
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/uae-mathematics.md",
   "lines": "64",
   "quote": "Answer Verification is an independent correctness validation submodule powered by GPT-5 that operates separately from the Pedagogical Evaluator to provide redundant correctness checking."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/AGENT4_DECISIONS.md",
   "lines": "52-60",
   "quote": "**Decision**: Use 0.85 threshold (NOT 0.94)"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md",
   "lines": "294",
   "quote": "**Pass threshold: 0.90+**"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/README.md",
   "lines": "233-236",
   "quote": "- Question QC with Anthropic key only: 8-9 checks (no too-close or difficulty)"
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
   "lines": "296",
   "quote": "- **Grade 6 MSQ (20 questions):** 0% pass rate - all failing"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/text-content-evaluator.md",
   "lines": "110",
   "quote": "**Query Relevance VETO:** Content with query_relevance < 0.4 is automatically rejected regardless of other scores."
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PIPELINE_EVALUATION.md",
   "lines": "91-95",
   "quote": "- Always generates addition problems regardless of topic"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/uae-mathematics.md",
   "lines": "33",
   "quote": "Auto-reject if answer key invalid."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html",
   "lines": "631",
   "quote": "Immediate rejection if answer is incorrect or ambiguous"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/reward_training/docs/training/TRAINING_STRATEGY.md",
   "lines": "96-99",
   "quote": "- These are \"sneaky bad\" - look okay but have critical flaws"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
   "lines": "210-214",
   "quote": "- **Issue:** The explanation incorrectly interprets x = 0 as “the first month.” The y-intercept corresponds to x = 0 (at opening), not the first month after opening."
  },
  {
   "truth": 59,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/math-content-evaluator.md",
   "lines": "109",
   "quote": "**Scoring:** Each criterion is evaluated as pass (1.0) or fail (0.0). Overall score = pass_count / 9"
  },
  {
   "truth": 59,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/README.md",
   "lines": "121-122",
   "quote": "- Questions with ≥0.8 overall score are considered \"passed\""
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
   "lines": "237-244",
   "quote": "5. Check for regression on previously passing questions"
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/edu_configs/curriculum_grade_4.jsonl",
   "lines": "1",
   "quote": "\"stimulus_needed\": 1.0, \"stimuli_categorization\": \"draw_stepwise_shape_pattern\""
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
   "lines": "306",
   "quote": "Distractions, unnecessary visuals, and redundant explanations are eliminated to keep cognitive load low."
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/demo_articles/grade4_fractions.md",
   "lines": "20-22",
   "quote": "**Question:** The rectangle below is divided into 8 equal parts, with 3 parts shaded."
  },
  {
   "truth": 64,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/svg-llm/README.md",
   "lines": "115-122",
   "quote": "1. **Topic is in SVG-beneficial list:**"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md",
   "lines": "35-38",
   "quote": "- No validation that correct answer is actually in the options"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
   "lines": "417-418",
   "quote": "- reject any item where computed answer ≠ keyed answer"
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json",
   "lines": "12",
   "quote": "Existing Questions to Avoid Duplication:"
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/README.md",
   "lines": "198",
   "quote": "- `{existing_questions}` - Previously generated questions for same passage"
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
   "lines": "244",
   "quote": "Incremental testing ensures we can validate each fix independently."
  }
 ]
}
```
