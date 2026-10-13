# verify:incept-core

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "incept-core",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All quotes verbatim. 197 items, 3.6%, 139 and 114 match TRAINING_GUIDE.md lines 125-130. Line 47 shows the writer's request carried empty curriculum metadata, and lines 51-58 list the fields the judge scored against. 'Will break it' generalised one run, so the statement now says most items broke them (139 and 114 of 197). The two cited systems differ (a Lambda generator and a k8s wrapper), but both withheld the spec. In found_by, the 7% comes from the 257-item run that NEXT_STEPS.md line 26 calls 'Previous'; root/INDEX.md line 132 labels it a GVC v2.0 test, so it is unclear whether the boundary-less validator was live. This is the writer-side counterpart of truth 33, not a duplicate.",
   "statement": "Give the writer the same specification the item will be judged against; a writer that never sees the boundaries, difficulty definitions or required formats breaks them on most items.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md",
     "lines": "47",
     "quote": "\"curriculum_metadata\": {}  // EMPTY!",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md",
     "lines": "62",
     "quote": "The model generates a 3-year interest problem because it doesn't know about the \"single year\" constraint. The evaluator fails it for violating a boundary the model never saw.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md",
     "lines": "125",
     "quote": "### Run: 3f480de7 (197 questions, 3.6% pass rate)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md",
     "lines": "129",
     "quote": "| Difficulty mismatch | 139 | Model ignores difficulty_definition |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md",
     "lines": "130",
     "quote": "| Constraint violation | 114 | Model ignores assessment_boundaries |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/PROMPT_LENGTH_HANDLING.md",
     "lines": "49",
     "quote": "**Approach:** Strip verbose fields under `skills.substandard_metadata` before prompt construction:",
     "verbatim": true
    }
   ],
   "against": "The gain from supplying the spec is not isolated. The fix was logged as '- Pass rate improved from 8% → 60-75% (expected)' (inceptlm/README.md line 103), and a later scored run, '- **Pass Rate:** 41.0% (121/295)' (nova_forge/RUN_LOG.md line 44), used a different item set and other changes. The failure table also words the cause as 'Model ignores difficulty_definition' (TRAINING_GUIDE.md line 129), which could mean a writer ignoring a definition it had.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "Quotes verbatim. 168 matches EXECUTIVE_SUMMARY.md lines 69, 238-239 and 302; the line 239 problem statement was added. This adds something truth 64 lacks: when the skill needs the representation, deleting the reference does not rescue the item (FAILURE_PATTERN_ANALYSIS lines 377-395 show 'with models' items failing educational and curriculum accuracy). The sources do not link the serve-without-images decision to the 168 failures, and the statement does not need that link. The against was reworded: line 69 is not 'right after' line 18.",
   "statement": "When an item depends on a picture, table or model, a missing one fails the item: don't ship the text without it, and don't just delete the reference when the skill needs that representation.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/IMPORTANT_TECHNICAL_DECISIONS.md",
     "lines": "453",
     "quote": "**Decision:** Continue serving requests even if SVG generation fails, returning questions without images.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "302",
     "quote": "- **Missing Stimulus:** 168 questions unsolvable without images",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "239",
     "quote": "**Problem:** Questions reference diagrams, tables, or number lines that aren't provided",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "378",
     "quote": "- Issue: The question targets “with models” but provides no models to interpret, so it does not assess the intended skill.",
     "verbatim": true
    }
   ],
   "against": "Rewriting the text helped but did not pass: '• Fixed questions improved from 0.60 avg → 0.76 avg (+16 points)' after '• Main issues fixed: References to missing images/figures' (qwen3-math/delivery/README.txt lines 36-37), still under the 0.85 bar used in the project's analyses. The image strategy lists '- Block question delivery on SVG failure' as a DON'T (svg-llm/docs/SVG_GENERATION_STRATEGY.md line 69), in the same document that notes '**Result: Questions are unusable without visuals**' (line 18).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep",
   "reason": "Quotes verbatim. 564 of 1,410 (40.0%), second only to factual accuracy (650), matches EXECUTIVE_SUMMARY.md lines 52-56. The first curriculum record sets Easy, Medium and Hard by which pattern step is asked, which no global number range can express. The judge cites per-standard definitions (FAILURE_PATTERN_ANALYSIS line 23, added). The 'generic guidance' cause is the 295-item analysis's diagnosis, not a measurement. Close in spirit to truth 69, but about difficulty labels rather than marking criteria.",
   "statement": "Define each difficulty level per skill and check every label against that skill's own definition; one global rule for 'easy' or 'hard' mislabels items.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
     "lines": "81",
     "quote": "- Generic difficulty guidance (\"EASY: small numbers\") doesn't match specific requirements",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "56",
     "quote": "2. **Difficulty Alignment** - 564 failures (40.0%)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/edu_configs/curriculum_grade_4.jsonl",
     "lines": "1",
     "quote": "\"difficulty_matrix\": \"EASY\\n- Steps one to three are given and the question asks about step 4.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "23",
     "quote": "- **Issue:** Labeled as Easy but matches the provided Medium definition for this standard.",
     "verbatim": true
    }
   ],
   "against": "The pipeline then hard-coded one rule for every skill, \"'easy': (100, 999),\" (nova_forge/FIX_SUMMARY.md line 71). Its README reports '- **Result**: <1% range errors (was 15%)' (nova_forge/README.md line 197), with no scored run behind it.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Both prompt quotes are on prompts.json line 43, which also holds the distractor dimension (added); the third is us-reading-comprehension.md line 96. The check rates fit to the intended grade, not easy/medium/hard, so 'level' became 'grade'. This is adopted design only: it runs only when examples are supplied, and no agreement with person ratings is recorded.",
   "statement": "Judge whether an item suits its grade by comparing it with validated items for that grade, weighing the inference it demands and the strength of its wrong options.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "43",
     "quote": "A set of the 5 most semantically similar validated test questions that are considered benchmarks for the specified grade level",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "43",
     "quote": "1.  **Level of Inference Required:** The cognitive steps a student must take to arrive at the correct answer (Low, Moderate, High).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "43",
     "quote": "2.  **Distractor Difficulty:** The quality and plausibility of the incorrect answer choices (Weak, Plausible, Strong).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "96",
     "quote": "- Assessed against benchmark questions from the same grade",
     "verbatim": true
    }
   ],
   "against": "The check runs only when benchmark items are supplied: '- Question QC with both keys + --examples: 10-11 checks (adds too-close and difficulty)' (qc_pipeline/README.md line 236). No agreement with person ratings is recorded.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "Quotes verbatim. 16/36 and 12/36 match inceptml_full_report.md lines 369-370, the most frequent zeros on a 36-item run from the live endpoint; line 370 was added for the 12/36. Judges also mark all-correct and implausible options as non-diagnostic (FAILURE_PATTERN_ANALYSIS lines 490 and 406). Building distractors from misconceptions is adopted, not tested as an intervention.",
   "statement": "Build each wrong option from a specific, likely error, so a choice shows what the learner misunderstood; options that are all correct, implausible or unrelated diagnose nothing.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
     "lines": "369",
     "quote": "- `distractor_quality` (16/36)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
     "lines": "370",
     "quote": "- `reveals_misconceptions` (12/36)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
     "lines": "404",
     "quote": "- Distractors are often not tied to *specific misconceptions* (diagnostic weakness).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "490",
     "quote": "- Issue: Because every option is correct, the item cannot differentiate between correct understanding and common errors.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "406",
     "quote": "- Issue: One option (“+”) is non-parallel and implausible for a comparison task, reducing distractor quality.",
     "verbatim": true
    }
   ],
   "against": "Distractor fixes were rated low-impact among near misses: '| Distractors | 30 | ⭐⭐⭐ HARDER (content) | Low |' (nova_forge/README.md line 303).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "Quotes verbatim. 3.7% (11/298), 3.0% (9/298) and 78% match PATTERN_ANALYSIS_RESULTS.md lines 10-11 and 21. Line 73 states the requirement; the wrapper's filtering is line 41 (added). This is broader than truth 6: it covers equivalent wrong options and non-text items such as 1/2 vs 5/10.",
   "statement": "Check that options differ in meaning, not just in wording; identical or equivalent options leave more than one right answer and no real distractor.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md",
     "lines": "24",
     "quote": "- All options are identical (e.g., all 4 choices say \"Four thousand five hundred sixty-seven\")",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
     "lines": "73",
     "quote": "- Avoid **equivalent distractors** (e.g., `1/2` vs `5/10`) unless multi-answer is supported.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
     "lines": "41",
     "quote": "- filtering equivalent distractors",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "21",
     "quote": "Synonymous or Near-Synonymous**: Uses different wording but conveys essentially the same meaning",
     "verbatim": true
    }
   ],
   "against": "Equivalent options are allowed when all of them are keyed: the rule holds only 'unless multi-answer is supported' (inceptml_full_report.md line 73).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The ck_gen line 'MUST NEVER be the longest option' moved from evidence to against: as an absolute rule it turns length into a reverse cue, and the published rubric's balance wording (line 74) carries the statement instead. The rubric's grammar and category checks (lines 53, 61) and a judged failure for a non-parallel option (FAILURE_PATTERN_ANALYSIS line 406) were added. Distinct from truth 8, which covers position; this is a specific case of truth 3.",
   "statement": "Keep options parallel in grammar, category, length and detail so the right answer can't be spotted by its form, such as being the longest or most specific.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "74",
     "quote": "- Prevents patterns where correct answer is consistently longest/shortest",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "66",
     "quote": "- Prevents correct answer from being notably more specific or vague than distractors",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "53",
     "quote": "- Ensures consistent grammatical structure across all answer options",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "61",
     "quote": "- All options belong to the same conceptual category",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "406",
     "quote": "- Issue: One option (“+”) is non-parallel and implausible for a comparison task, reducing distractor quality.",
     "verbatim": true
    }
   ],
   "against": "A grades 9-10 reading generator makes the cue a fixed rule: '**SPECIAL CONSTRAINT**: The correct answer MUST NEVER be the longest option.' (reading-question-qc/ck_gen - prompts.json line 12, repeated on lines 6, 18, 48 and 54). A key that is never the longest is a pattern of its own.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 15.27% and the 20-item 0% match EXECUTIVE_SUMMARY.md lines 79 and 296. The cited 'key lists only A' case (FAILURE_PATTERN_ANALYSIS line 245) is an MCQ (cc-math-4-mcq-hard-31), not a multiple-select item, so it was replaced by the multiple-select case at line 249. The fix at line 83 states a count, while Pattern 4 (EXECUTIVE_SUMMARY line 257) asks for 'Select all that apply', so the statement allows either. Checking each option repeats truth 6; the selection instruction is new.",
   "statement": "On a multiple-select item, tell the student that more than one answer can be right (or how many to choose), and check each option's truth on its own.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "79",
     "quote": "| **MSQ** | 21.43% | 0.00% | 6.15% | 21.08% | 15.27% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "81",
     "quote": "**Key Finding:** MSQ (Multiple Select Questions) have the lowest pass rate overall, with Grade 6 having 0% pass rate on MSQs.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "84",
     "quote": "- **Issue:** Missing guidance on how many answers to choose creates ambiguity for students.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "257",
     "quote": "**Problem:** Missing \"Select all that apply\", unclear wording",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "249",
     "quote": "- Issue: All options A–D equal 7/11, but the key lists only A and C.",
     "verbatim": true
    }
   ],
   "against": "The 0% subgroup is small: '- **Grade 6 MSQ (20 questions):** 0% pass rate - all failing' (EXECUTIVE_SUMMARY.md line 296).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 34 matches PASS_RATE_ANALYSIS.md line 117. The cited line 121 ('Wolfram validates the answer but not the explanation steps') sits under 'Possible Causes' as a guess, so the measured lines 117-118 replace it. The 'key names an option that exists' clause had no evidence; FAILURE_PATTERN_ANALYSIS line 208 (key 'A' on an item with no choices) now covers it. The against now cites the judge's own 100% for that earlier run. Not a duplicate of truth 59 or 67: this is about agreement among stem, options, key and explanation.",
   "statement": "Check the whole item for agreement: the stem asks for what the options offer, the key names an option that exists, and the explanation supports the key; checking only the final answer misses the rest.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
     "lines": "117",
     "quote": "- 34 questions failed factual_accuracy",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
     "lines": "118",
     "quote": "- GVC shows \"math_errors_found: 0\" but InceptBench still finds issues",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md",
     "lines": "138",
     "quote": "- Generated: Answer \"A\" but explanation proves \"B\" is correct",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "78",
     "quote": "- **Issue:** The stem asks for a model, but only numeric answers are provided and no model is shown, creating conflicting cues about what action is required.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "208",
     "quote": "- **Issue:** Field mismatch: the answer is labeled “A” but no choices are presented; the item appears to be fill-in.",
     "verbatim": true
    }
   ],
   "against": "In an earlier 257-item run the answer-only check and the judge agreed: '- **Result:** ✅ All math is already correct!' and '- Math accuracy: 100% ✅' (archive/old_docs/gvc/GVC_FINAL_ARCHITECTURE.md lines 60 and 65). That run's failures were put down to format.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep",
   "reason": "Quotes verbatim. 122 (8.7% of 1,410) at FAILURE_PATTERN_ANALYSIS line 429 and 6/36 'often due to operation mismatch vs stated skill' at inceptml_full_report.md line 371 match; both were added. This is finer than truth 58: these items stayed on topic but tested a different skill, such as computing instead of writing an equation, or multiplying in an add/subtract skill.",
   "statement": "Check that an item exercises the named skill itself, not a neighbouring skill on the same topic.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "132",
     "quote": "- **Issue:** The task assesses basic subtraction rather than writing a one-step equation, which the stated standard/lesson emphasizes.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "429",
     "quote": "**Failures:** 122 questions (8.7% of all failures)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
     "lines": "371",
     "quote": "- `curriculum_alignment` (6/36; often due to operation mismatch vs stated skill)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
     "lines": "406",
     "quote": "- Skill metadata can drift (questions sometimes include multiplication when the skill says add/sub only).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "27",
     "quote": "The question must directly assess the standard's specific skill, not a tangentially related skill.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Naming the error behind the chosen option is new. Pointing to the refuting evidence overlaps truth 1 ('says where to look'), and prompts.json line 73 was added to back it. The against was corrected: line 77 accepts feedback that states the answer but does not require it. This is a rubric rule only, with no measured effect.",
   "statement": "Feedback on a wrong choice should name the specific error behind that choice and point to the evidence against it, not say a generic 'try again'.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "65",
     "quote": "It should explain what makes this specific option incorrect",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "69",
     "quote": "The feedback must categorize or name the type of thinking error",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "73",
     "quote": "The feedback must cite specific passage content that contradicts the wrong answer",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "131",
     "quote": "- Identifies the specific error or misconception that led to the incorrect choice",
     "verbatim": true
    }
   ],
   "against": "The same rubric also passes feedback that gives the answer away: 'The feedback must either explicitly state the correct answer or clearly guide the student to it' (qc_pipeline/config/prompts.json line 77). That is at odds with truth 1.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "reason": "Both quotes verbatim: the page at line 144, and prompts.json line 77, whose prompt also says 'The student should leave knowing what the right answer is and why'. qc_pipeline/README.md line 30 names config/prompts.json as 'All quality control prompts', so this is the prompt the pipeline runs. The running prompt accepts stating the answer outright but does not require it, so 'require opposite things' became 'disagree'.",
   "statement": "Audit the judge prompt that actually runs, not the published description of it; the two can disagree, one forbidding what the other passes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
     "lines": "144",
     "quote": "- Provides a path to the right answer without giving it away directly",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "77",
     "quote": "The feedback must either explicitly state the correct answer or clearly guide the student to it",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
     "lines": "77",
     "quote": "The student should leave knowing what the right answer is and why",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/README.md",
     "lines": "30",
     "quote": "prompts.json          # All quality control prompts",
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
   "reason": "Quotes verbatim. EduBench defines EC as 'Error Correction' and IP as 'Idea Provision' (README lines 54-55). The evaluator Readme (line 122) says the task mode tests an AI model's responses to the question. Yet the report scores 'Educational Curriculum Alignment' at 10.00 on 873 items (line 15, added). IP also appears as 'Instructional Planning' (incept-multilingual-generation/README.md line 337) and 'Inference & Pedagogy' (report line 16). The fourth expansion in found_by, 'Improved Prompting', was not found. Not covered by truths 37 or 44.",
   "statement": "Before reporting a score, confirm what its evaluator actually measures; a borrowed benchmark's task scores were reported as quality dimensions they never measured.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md",
     "lines": "41",
     "quote": "#### 2. Educational Curriculum Alignment (EC) - Weight: 45%",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md",
     "lines": "15",
     "quote": "- **Educational Curriculum Alignment (EC):** 10.00/10.0 (n=873)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/EduBench/README.md",
     "lines": "54",
     "quote": "- Error Correction (EC)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/Readme.md",
     "lines": "122",
     "quote": "1. **`edubench_tasks`** (AI Model Response Testing): Tests how well an AI model (EDU-Qwen2.5-7B) can respond to your question across 6 task types (QA, EC, IP, AG, QG, TMG). This validates that your question is clear enough for AI to understand.",
     "verbatim": true
    }
   ],
   "against": "The repurposing was deliberate in the framework document, which describes the Error Correction row as 'Tests curriculum alignment and educational appropriateness. Does content match grade-level standards?' (incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html lines 261-263).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep",
   "reason": "Quotes verbatim. 9.28 and 8.48 on 300 items match. The evaluator Readme (line 156, added) documents a script that deletes low scorers from the database, and the report averages only the items kept at 8.0 or above, so the 9.28 has a floor of 8.0 by construction. The 8.48 run's report does not say the set was unfiltered or came from the same pipeline. The remedy differs from truth 66: count the full denominator rather than confirm independently.",
   "statement": "Report a generator's quality over everything it produced, counting what was removed; averaging only the items that survived a score filter inflates the result.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md",
     "lines": "81",
     "quote": "3. **Quality Filtering:** Only questions scoring ≥8.0/10.0 are retained in the dataset",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md",
     "lines": "13",
     "quote": "- **Weighted Overall Score:** 9.28/10.0",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/Readme.md",
     "lines": "156",
     "quote": "Analyze question scores and remove low-performing questions from the database.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/reports/evaluation_13-01-37_report.md",
     "lines": "17",
     "quote": "| **Weighted Score** | **8.48/10.0** | 300 |",
     "verbatim": true
    }
   ],
   "against": "This is not a controlled comparison. The filtered report covers '- **Evaluation Period:** September 30, 2025 to October 02, 2025' (incept_benchmark_report.md line 17) across five grades, while the 8.48 run is a single grade-3 set.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim and all numbers match. For the AP Literature quiz set, the final score went from 0.661 to 0.712 (+5.1) while TI QA (0.832 to 0.823) and Reading QC (0.612 to 0.602) fell, so the aggregation changed rather than the judging. The cross-version 'reversal' started from a 0.002 near-tie (0.663 vs 0.661), so that claim was dropped. Within v1.4.0, TI QA ranks the AP set above SAT (0.823 vs 0.605) and Reading QC reverses it (0.602 vs 0.704). This states the same rule as truth 45 and is kept because it adds this evidence.",
   "statement": "Name the evaluator and its version with every score and compare only within one; a version change moved one benchmark's final score five points while its sub-scores barely moved, and two sub-evaluators of one version ranked the same two generators in opposite orders.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/benchmarks/_index.md",
     "lines": "57",
     "quote": "| APLIT Quiz Generation | 0.661 (66%) | 0.832 | 0.612 | 68.3% | 60 (3 sets) | 1.1.7 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/benchmarks/_index.md",
     "lines": "56",
     "quote": "| SAT Reading Generation | 0.663 (66%) | 0.619 | 0.712 | 98.7% | 82 (3 sets) | 1.1.5 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/scores/summary.txt",
     "lines": "41",
     "quote": "APLIT Quiz Generation        | 0.712 (71%) | 0.823   | 0.602      | 66.7%    | 60 (3 sets) | 1.4.0",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/scores/summary.txt",
     "lines": "40",
     "quote": "SAT Reading Generation       | 0.654 (65%) | 0.605   | 0.704      | 100.0%   | 82 (3 sets) | 1.4.0",
     "verbatim": true
    }
   ],
   "against": "The cross-version rows may not be the same items, since answer accuracy moved too (68.3% to 66.7%, 98.7% to 100.0%). The version labels are also inconsistent: a table 'using InceptBench v1.3.0' (benchmarks/_index.md line 52) has rows labelled 1.1.5 to 1.2.0, and one set reads 'InceptBench Version: mixed (1.4.0, unknown)' (nova_forge/scores/ela-mock-fe/results.txt line 4).",
   "general": true,
   "duplicate_of": "45",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 95% (22/23 mock tests) and 99% projected match AGENT3_EXECUTION_LOG.md lines 509 and 527. Nothing cited backed 'blank test templates'; DEPLOYMENT_TEST_RESULTS.md line 43, '[PENDING - To be filled after deployment]' for the nova-forge-improved-pipeline function (line 6), now does. PIPELINE_EVALUATION.md lines 84-95 rate P3-Improved, the 6-layer pipeline, at 0% reliability, always generating addition problems.",
   "statement": "Claim an improvement only from a scored run of real output; projected gains, mock tests and blank test templates are not results.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/AGENT3_EXECUTION_LOG.md",
     "lines": "509",
     "quote": "| Pass Rate | 41% | 99% (projected) | +58% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/AGENT3_EXECUTION_LOG.md",
     "lines": "527",
     "quote": "- ✅ Mock tests: 95% passing (22/23 tests)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/README.md",
     "lines": "189",
     "quote": "- **Result**: 0% missing type fields (was 62%)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/DEPLOYMENT_TEST_RESULTS.md",
     "lines": "43",
     "quote": "**Result:** [PENDING - To be filled after deployment]",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PIPELINE_EVALUATION.md",
     "lines": "88",
     "quote": "| Reliability | **0%** |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PIPELINE_EVALUATION.md",
     "lines": "94",
     "quote": "- \"6-layer validation\" not functioning",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 62% and '+30-40% pass rate' match PASS_RATE_ANALYSIS.md lines 38 and 67. Line 44 (added) shows the type field was absent from every item's content, passing items included. The judge failed the analysis's own example, cc-math-4-mcq-easy-6, for the '+' option (FAILURE_PATTERN_ANALYSIS line 293); that item is in the same 295-item, 121-pass Grade 4 set. The against was corrected: later scored runs exist (RUN_LOG.md lines 31-35), but they don't isolate the fix. Distinct from truth 60, which is about averages hiding failures.",
   "statement": "Name a failure's cause from the judge's stated reasons on the failing items, not from a field the failing items happen to share.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
     "lines": "38",
     "quote": "### CRITICAL ISSUE #1: Missing 'type' Field (62% of failures)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
     "lines": "43",
     "quote": "- All questions with 0.00 spec compliance score are missing `content.type`",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
     "lines": "44",
     "quote": "- Type is only in `request.type`, not in the question content being evaluated",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
     "lines": "45",
     "quote": "- Example from failed question cc-math-4-mcq-easy-6:",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
     "lines": "293",
     "quote": "- Issue: Violates the boundary to use only >, <, and = by including \"+\" as an option.",
     "verbatim": true
    }
   ],
   "against": "The project recorded the field fix as a success, '| Type Field Present | 38% | 100% | +62% |' (nova_forge/README.md line 228). A later logged run reached '- **Pass Rate:** 55.4%' on 298 items (RUN_LOG.md line 34) but mixed in '121 passed original, 37 corrected, 7 regenerated' (line 35), so the field's share is never isolated.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep",
   "reason": "Quotes verbatim. The old extractor read only correct_answer (ITD line 137), while fill-in used answer and multiple-select used correct_answers (lines 128-130; lines 130 and 137 added). That explains the empty keys the judge saw (PATTERN_ANALYSIS_RESULTS.md line 154), yet the same document puts the 0% down to missing examples (line 46). 16 zero scores matches AGENT2 line 86, but only the sampled items show 'Question: N/A' (lines 104-140), so this file does not show that all 16 lacked text.",
   "statement": "Rule out pipeline faults before reading a low score as a content failure; an empty or misparsed field scores like a bad item.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md",
     "lines": "126",
     "quote": "1. **Bug Found:** Fill-in answers were empty because code only looked for `correct_answer`",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md",
     "lines": "137",
     "quote": "\"answer\": result.get(\"correct_answer\", \"\")",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md",
     "lines": "130",
     "quote": "- MSQ uses `\"correct_answers\": [\"B\", \"C\"]`",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md",
     "lines": "154",
     "quote": "Answer field is [\"\"] but explanation states correct choices are B and C",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/ITD_ENHANCED_FEW_SHOT.md",
     "lines": "46",
     "quote": "1. **Targeted Learning:** Fill-in questions were 0% pass rate because model had no fill-in examples",
     "verbatim": true
    }
   ],
   "against": "The two causes were fixed in the same deployment, so the record never isolates either: '| 2 | Type-specific examples | Fixes 0% fill-in/MSQ | ✅ Deployed |' and '| 4 | Multi-field answer extraction | Fixes empty answers | ✅ Deployed |' (ITD_ENHANCED_FEW_SHOT.md lines 491 and 493).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "drop",
   "reason": "Quotes verbatim (the false-positive row is line 112), but the sources do not make the causal claim. The Phase 2 loop force-accepted on attempt 3 ('- Attempt 3: force‑accept to guarantee output', PHASE2_MATH_AUDITOR.md line 20), and no document ties the 0% fill rate to false positives. The found_by line 'zero math errors in 257 items while the judge kept finding factual errors' is wrong for that run: the judge also reported 'Math accuracy: 100% ✅' (GVC_FINAL_ARCHITECTURE.md line 65), and the 34 factual failures come from the 295-item run. The two records also disagree on the old pass rate (5% vs 0%). What remains, measuring how often a check misfires and distrusting a check that never fires, is truths 37 and 38.",
   "statement": "Measure how often a check fires on good items before it gates; an over-eager check drives regenerate loops that empty the output.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/gvc/GVC_DEPLOYMENT_MANUAL.md",
     "lines": "5",
     "quote": "This deploys the **Generate-Validate-Correct (GVC) Architecture** to replace the failed Phase 2 (math auditor retry loop).",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/gvc/GVC_DEPLOYMENT_MANUAL.md",
     "lines": "112",
     "quote": "| Validation | Python-only (false positives) | Wolfram Alpha (definitive) |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/gvc/FINAL_STATUS_AND_NEXT_STEPS.md",
     "lines": "120",
     "quote": "| Fill rate | 0% | 80-90% |",
     "verbatim": true
    }
   ],
   "against": "The records disagree on the outcome: '| Pass rate | 5% | Target: 15-25% |' (GVC_DEPLOYMENT_MANUAL.md line 115) against 0% (FINAL_STATUS_AND_NEXT_STEPS.md line 122). The false-positive rate itself was never itemized.",
   "general": true,
   "duplicate_of": "37",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 8.46 and 7.50 match lines 125 and 145, and all 20 judge-model averages in Table 1 are above the human average for the same model. Kendall's W with humans is 0.56-0.63 (line 207, added), about the same as among the model judges, which the authors call strong agreement (line 217). EduBench scores model responses in teaching scenarios, so 'generated educational content' became 'educational responses'. The calibration step overlaps truth 37; the leniency finding is new.",
   "statement": "Model judges score educational responses higher than people do and agree with them only moderately, so calibrate a model judge against person ratings before trusting its scores.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/EduBench/README.md",
     "lines": "125",
     "quote": "|                 | Qwen2.5-7B-Instruct    | 8.34 | 9.01 | 8.64 | 8.16 | 6.64 | 9.33 | 8.75 | 8.23 | 9.06 | 8.46 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/EduBench/README.md",
     "lines": "145",
     "quote": "|                 | Qwen2.5-7B-Instruct    | 6.78 | 7.63 | 7.93 | 7.74 | 6.79 | 7.86 | 7.79 | 7.55 | 7.42 | 7.50 |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/EduBench/README.md",
     "lines": "207",
     "quote": "| **Human**       | 0.63        | 0.56   | 0.63     | **0.63**    | -     |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/EduBench/README.md",
     "lines": "218",
     "quote": "- **Consistency between humans and models**: The model evaluations do not fully align with human judgments, which may be due to limited understanding of the evaluation criteria by the models.",
     "verbatim": true
    }
   ],
   "against": "The rankings agree at the extremes: 'In Table 2, DeepSeek R1 and Qwen2.5-7B-Instruct still show the best and worst performances, respectively, which are consistent with the model-based evaluation results.' (EduBench/README.md line 193).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 34.35%, 26.28% and 14.14% match, as does grade 7's 1.54% (1/65, EXISTING_GRADES_ANALYSIS.md line 196, added). 'Highest grades' was cut: grade 8, at 28.76%, passes more than grades 6 and 7. 'Check difficulty hardest there' was cut too, since the gradient is in overall failure, not in difficulty labels. The upper-grade clause rests on one generator's notes (svg-llm/README.md lines 39-45). Evidence covers math items only.",
   "statement": "Spot-check a generator's hardest requests most closely: pass rates fall as requested difficulty rises, and upper-grade requests can come back simpler than asked.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "87",
     "quote": "| **Easy** | 658 | 226 | 432 | 34.35% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
     "lines": "89",
     "quote": "| **Hard** | 587 | 83 | 504 | 14.14% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXISTING_GRADES_ANALYSIS.md",
     "lines": "196",
     "quote": "| Hard | 65 | 1 | 64 | 1.54% |",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/svg-llm/README.md",
     "lines": "40",
     "quote": "- Questions may be simpler than expected for grade level",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/svg-llm/README.md",
     "lines": "45",
     "quote": "- Grades 9-10 produce elementary-level questions",
     "verbatim": true
    }
   ],
   "against": "The gradient is not uniform. In one grade 'Performance is nearly identical across all difficulty levels' (AGENT2_GRADES_3_8_BASELINE.md line 60: 41.4%, 41.7%, 39.5%), and pass rates do not fall with grade ('| **6** | 398 | 13.82% |' vs '| **8** | 998 | 28.76% |', EXECUTIVE_SUMMARY.md lines 31 and 33).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The check asks for 'at least 2 of the 3 competency areas', not all three, so the statement was narrowed. The source is a set-level check in a grades 9-10 reading generator, and the 70% cut-off is that tool's setting. Adopted rule.",
   "statement": "Judge a question set as a whole: it should mix kinds of demand (literal, inferential, evaluative), covering at least two, with no one kind in more than 70% of items.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json",
     "lines": "114",
     "quote": "Set should include questions from at least 2 of the 3 competency areas",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json",
     "lines": "114",
     "quote": "No single competency should dominate (>70% of questions)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "263",
     "quote": "Questions move from basic recall to application to reasoning, helping students strengthen understanding step by step.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The framework localizes names, locations, objects and contexts in all questions (HTML line 518, added), so 'only where they serve the objective' was wrong for names and places. That limit applies to the cultural 'spiky points' (spiky_points_of_view.json line 125). HTML lines 545-550 list what is never localized. Adopted rule.",
   "statement": "Localize surface details such as names, places and currency, but never the concept, standard units or the context the lesson needs; add cultural framing only where it serves the objective.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html",
     "lines": "518",
     "quote": "Our localization framework ensures that all generated questions use culturally appropriate names, locations, objects, and contexts relevant to UAE students.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html",
     "lines": "547",
     "quote": "Universal mathematical/scientific concepts",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html",
     "lines": "549",
     "quote": "International context when pedagogically necessary",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html",
     "lines": "550",
     "quote": "Standard units of measurement",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/spiky_points_of_view.json",
     "lines": "125",
     "quote": "Only apply spiky points that are genuinely relevant to the learning objective",
     "verbatim": true
    }
   ],
   "against": "The same file also directs cultural framing everywhere: 'Prioritize Arabic and Islamic perspectives in all explanations.' (spiky_points_of_view.json line 9).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep",
   "reason": "Quotes verbatim; the line 272 text also appears at line 444. This is an adopted rule from the framework's spaced-practice pillar. Distinct from truth 48, which measures learning, while this schedules practice.",
   "statement": "Revisit each skill at growing intervals and mix earlier items into later practice, so retention is checked rather than first success.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "99",
     "quote": "Students revisit key skills at increasing intervals \\- after a day, a few days, a week, and beyond.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "272",
     "quote": "Later questions intentionally revisit earlier concepts to test retention and fluency.",
     "verbatim": true
    }
   ],
   "against": "none found (adopted without a project measurement)",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim. The parenthetical now matches the source: 'guided reading', not 'guided steps'. Adopted rule, with no measurement.",
   "statement": "For learners who are behind, keep the task's demand and add support (guided reading, vocabulary support, targeted practice) instead of giving easier material.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "143",
     "quote": "Do not lower the cognitive demand of material. Instead, scaffold with guided reading, vocabulary support, and targeted practice.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Neither cited quote backed 'remove anything that doesn't serve it'; line 223 ('Lessons eliminate unnecessary complexity, visuals, and multitasking.') now does. Adopted rule.",
   "statement": "Teach one well-defined skill per lesson and remove anything that doesn't serve it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "208",
     "quote": "Each lesson targets one skill or concept only. Students should know exactly what they are learning and why it matters.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "91",
     "quote": "Each focuses on a single, well-defined skill.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "223",
     "quote": "Lessons eliminate unnecessary complexity, visuals, and multitasking. Students focus on one process at a time.",
     "verbatim": true
    }
   ],
   "against": "A criticism the site itself records against the approach: '- May not fully encourage critical thinking or open-ended exploration' (content/english/pages/direct-instruction.md line 63).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Independent, unprompted' now rests on line 75 (mastery means applying a skill 'independently, accurately, and automatically') and lines 399-401 (unprompted recall comes after recognition); the direct-instruction page line alone did not support it. Line 380 is from the vocabulary cycle. Adopted rule. Not truth 48, which is about measuring learning later.",
   "statement": "Move a learner on only after independent, unprompted performance shows mastery; recognition with hints doesn't count.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/direct-instruction.md",
     "lines": "34",
     "quote": "Progression to the next lesson occurs only when students demonstrate mastery of current material.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "75",
     "quote": "Incept defines mastery as the point at which a student can apply a skill or concept independently, accurately, and automatically.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "380",
     "quote": "Every cycle ends with independent recall \\- typing or saying the word without hints \\- to confirm mastery.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "399",
     "quote": "* **Recall** (independent response without prompts)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "401",
     "quote": "This structured cycle ensures every new word moves from recognition to confident, fluent use.",
     "verbatim": true
    }
   ],
   "against": "A criticism the site itself records against the approach: '- Sometimes criticized for being too rigid or prescriptive, potentially limiting teacher creativity' (content/english/pages/direct-instruction.md line 62).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim, but it sits under 'What Makes a Good Vocabulary Question' (line 403, added) and covers questions, not teaching. 'Teach and test a concept' was narrowed to testing a word's meaning. Adopted rule.",
   "statement": "Test a word's meaning with examples and near-miss non-examples, so the learner has to tell close meanings apart.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "410",
     "quote": "Present examples and near-misses, prompting learners to discriminate between related meanings.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "403",
     "quote": "## **What Makes a Good Vocabulary Question**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep",
   "reason": "Quote verbatim. This is an adopted design for the UAE mathematics benchmark, which has over 4,000 requests (line 500). No results are recorded, as the against says.",
   "statement": "Test a content generator with several phrasings of each request; its quality should not depend on how the request is worded.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
     "lines": "498",
     "quote": "Semantic variation \\- The same skills and topics are described in various semantically similar ways while sending requests to the LLM",
     "verbatim": true
    }
   ],
   "against": "No results were recorded for the benchmark that uses it: '| Coming Soon | - | - | - | - |' (content/english/pages/uae-mathematics.md line 131).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep-with-fix",
   "reason": "LIVE_STATUS quotes verbatim: the '90.0% (54/60)' headline lists only empty answers, missing fields and a parse error. The PIPELINE_EVALUATION quote is verbatim but reports reliability and quality as separate metrics, so it does not show them conflated. It was replaced by root/INDEX.md lines 252-254: a 100% fill rate alongside a 7% judged pass rate.",
   "statement": "Report a well-formed-output rate separately from judged quality; passing a structure or parse check says nothing about whether an item is right.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/LIVE_STATUS.md",
     "lines": "7",
     "quote": "# 90.0% (54/60)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/LIVE_STATUS.md",
     "lines": "22",
     "quote": "- **Empty or null 'answer'**: 2 occurrences",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/root/INDEX.md",
     "lines": "252",
     "quote": "- Fill rate: 100% (was 0%)",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/root/INDEX.md",
     "lines": "254",
     "quote": "- Pass rate: 7% (format issues by design)",
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
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/uae-mathematics.md",
   "lines": "38",
   "quote": "6. **Explanation Quality** - Explanations guide learning vs stating answers. Flag \"leakage\" if reveals exact option text.",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/us-reading-comprehension.md",
   "lines": "144",
   "quote": "- Provides a path to the right answer without giving it away directly",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
   "lines": "73",
   "quote": "The feedback must cite specific passage content that contradicts the wrong answer",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
   "lines": "77",
   "quote": "The feedback must either explicitly state the correct answer or clearly guide the student to it",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/BENCHMARK_FAILURE_ANALYSIS.md",
   "lines": "73",
   "quote": "The diagram itself displays '135°,' giving away the answer before the student attempts the problem.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html",
   "lines": "496",
   "quote": "Scaffolding should guide students through problem-solving without revealing answers prematurely.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/glossary.md",
   "lines": "110",
   "quote": "Includes hard-fail gates for inappropriate content or answer leakage",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/demo_articles/grade4_fractions.md",
   "lines": "31",
   "quote": "**D)** 1/8 + 1/8 + 1/8 ✓",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
   "lines": "107",
   "quote": "When students make errors, they are guided through the correct reasoning right away.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json",
   "lines": "96",
   "quote": "Determine whether a student must read this specific passage to answer the question correctly, or if they could answer it using general knowledge.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
   "lines": "21",
   "quote": "Equally Text-Supported**: Both correct answer and distractor are equally supported by passage evidence",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/scores/aplit-quiz-generation/results.txt",
   "lines": "13",
   "quote": "Accuracy:         66.7%",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/answer-verification.md",
   "lines": "105",
   "quote": "- **●●○○○○○○○○ (0-4)**: Low - manual review recommended",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
   "lines": "384",
   "quote": "By **mastering roughly 300–400 high-utility academic words per grade level**, students gain the linguistic precision needed for strong reading comprehension and confident written expression.",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
   "lines": "342",
   "quote": "Vocabulary is taught explicitly and revisited frequently to connect decoding with comprehension, while background knowledge is deliberately built into texts to support understanding and schema formation.",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/svg-llm/svg_pipeline/README.md",
   "lines": "44",
   "quote": "3. **Verifiable by construction** - If params extracted correctly, SVG is correct",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/svg-llm/TRAINING_BEST_PRACTICES.md",
   "lines": "77",
   "quote": "- Manually review 20 generated SVGs",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
   "lines": "382",
   "quote": "- the wrapper filtered with `if validate_question(q)` but returned the original `q`",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/demo_articles/grade4_fractions.md",
   "lines": "56",
   "quote": "![Generated visual]([IMAGE_2])",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
   "lines": "425",
   "quote": "| **Word Length (Questions / Items)** | 5–10 words per question. | 10–15 words per question. | 15–25 words per question. |",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/config/prompts.json",
   "lines": "95",
   "quote": "The feedback should be between 1-4 complete sentences",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/BULK_GENERATOR_README.md",
   "lines": "12",
   "quote": "- Questions failing ≤1 QC check are tentatively accepted",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/PHASE2_MATH_AUDITOR.md",
   "lines": "20",
   "quote": "- Attempt 3: force‑accept to guarantee output",
   "ok": true
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/README.md",
   "lines": "120",
   "quote": "- Each check returns 0 (fail) or 1 (pass)",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/gvc/NEXT_STEPS.md",
   "lines": "19",
   "quote": "❌ Claude not finding format problems",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/gvc/NEXT_STEPS.md",
   "lines": "34",
   "quote": "Claude is being asked to validate format, but it doesn't have the **specific assessment boundaries** that InceptBench uses.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/EduBench/README.md",
   "lines": "217",
   "quote": "- **Consistency among evaluation models**: The models show high consistency, with almost all Kendall's W values above 0.5 and most around 0.6, indicating strong agreement.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
   "lines": "118",
   "quote": "- GVC shows \"math_errors_found: 0\" but InceptBench still finds issues",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/evaluator/reports/incept_benchmark_report.md",
   "lines": "15",
   "quote": "- **Educational Curriculum Alignment (EC):** 10.00/10.0 (n=873)",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/direct-instruction.md",
   "lines": "48",
   "quote": "1. **Review and warm-up** - Recall prior knowledge",
   "ok": true
  },
  {
   "truth": 42,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
   "lines": "208",
   "quote": "**Recommendation:** Consider regenerating questions scoring below 0.60 (97 questions) rather than fixing.",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/uae-mathematics.md",
   "lines": "64",
   "quote": "Answer Verification is an independent correctness validation submodule powered by GPT-5 that operates separately from the Pedagogical Evaluator to provide redundant correctness checking.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/AGENT4_DECISIONS.md",
   "lines": "54",
   "quote": "**Decision**: Use 0.85 threshold (NOT 0.94)",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/inceptbench_lambda/TRAINING_GUIDE.md",
   "lines": "294",
   "quote": "**Pass threshold: 0.90+**",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/qc_pipeline/README.md",
   "lines": "234",
   "quote": "- Question QC with Anthropic key only: 8-9 checks (no too-close or difficulty)",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/EXECUTIVE_SUMMARY.md",
   "lines": "296",
   "quote": "- **Grade 6 MSQ (20 questions):** 0% pass rate - all failing",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/text-content-evaluator.md",
   "lines": "110",
   "quote": "**Query Relevance VETO:** Content with query_relevance < 0.4 is automatically rejected regardless of other scores.",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PIPELINE_EVALUATION.md",
   "lines": "92",
   "quote": "- Always generates addition problems regardless of topic",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/uae-mathematics.md",
   "lines": "33",
   "quote": "Auto-reject if answer key invalid.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/inceptapi.com/INCEPT_Benchmarking_Framework.html",
   "lines": "631",
   "quote": "Immediate rejection if answer is incorrect or ambiguous",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/reward_training/docs/training/TRAINING_STRATEGY.md",
   "lines": "99",
   "quote": "- These are \"sneaky bad\" - look okay but have critical flaws",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/FAILURE_PATTERN_ANALYSIS.md",
   "lines": "214",
   "quote": "- **Issue:** The explanation incorrectly interprets x = 0 as “the first month.” The y-intercept corresponds to x = 0 (at opening), not the first month after opening.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/content/english/pages/math-content-evaluator.md",
   "lines": "109",
   "quote": "**Scoring:** Each criterion is evaluated as pass (1.0) or fail (0.0). Overall score = pass_count / 9",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/README.md",
   "lines": "122",
   "quote": "- Questions with ≥0.8 overall score are considered \"passed\"",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
   "lines": "242",
   "quote": "5. Check for regression on previously passing questions",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/edu_configs/curriculum_grade_4.jsonl",
   "lines": "1",
   "quote": "\"stimulus_needed\": 1.0, \"stimuli_categorization\": \"draw_stepwise_shape_pattern\"",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-uae-api-website/bench.inceptapi.com/Incept Pedagogy & Learning Science Overview.md",
   "lines": "306",
   "quote": "Distractions, unnecessary visuals, and redundant explanations are eliminated to keep cognitive load low.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/demo_articles/grade4_fractions.md",
   "lines": "22",
   "quote": "**Question:** The rectangle below is divided into 8 equal parts, with 3 parts shaded.",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/svg-llm/README.md",
   "lines": "116",
   "quote": "1. **Topic is in SVG-beneficial list:**",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/archive/old_docs/platform/PATTERN_ANALYSIS_RESULTS.md",
   "lines": "38",
   "quote": "- No validation that correct answer is actually in the options",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/qwen3-math/docs/inceptml_full_report.md",
   "lines": "418",
   "quote": "- reject any item where computed answer ≠ keyed answer",
   "ok": true
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/ck_gen - prompts.json",
   "lines": "12",
   "quote": "Existing Questions to Avoid Duplication:",
   "ok": true
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/incept-multilingual-generation/src/external_submodules/reading-question-qc/README.md",
   "lines": "198",
   "quote": "- `{existing_questions}` - Previously generated questions for same passage",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/nova_forge/PASS_RATE_ANALYSIS.md",
   "lines": "244",
   "quote": "Incremental testing ensures we can validate each fix independently.",
   "ok": true
  }
 ]
}
```
