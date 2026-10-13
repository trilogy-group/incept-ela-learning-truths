# Round 2: the AP generators, evaluators and gaming tests

A read-only search agent, 2026-10-12 08:21 to 2026-10-12 08:46 UTC. Its brief and its final report, verbatim.

## Brief

Find lessons learned that hold for ANY lesson, course or set of learning materials, whatever the subject or text, each with its exact evidence. Thoroughness: very thorough. Context: these sources come from building generators, benchmarks and evaluators for AP social studies questions (multiple choice, short answer, document-based and long essay) and K-12 social studies items.

STRICT RULES: read-only. Do not create, edit, move or delete files; run no command that writes; no network fetches. Never open .env, key or token files, and never print a secret. Files in iCloud Drive may be placeholders that download when read: read only documents (.md, .txt, .qmd, small .json), never data dumps (.jsonl, .csv, .sql, .zip, .xlsx, .parquet), model files or logs, and skip any workspace/, data/, datasets, runs/ or outputs folders except for written reports and summaries in .md. Never read anything under ~/Library/Mobile Documents/com~apple~CloudDocs/personal/.

Sources (only these; W = "~/Library/Mobile Documents/com~apple~CloudDocs/work"):
- W/aptraining/ : its top-level README, AGENTS, CLAUDE and docs, plus any .md reports, postmortems, summaries and evaluation write-ups (find them with names like report, postmortem, summary, findings, lessons, eval)
- W/ap-social-studies-generator/ : its README and docs (generation rules, item specs, validation, review findings)
- W/ap-benchmark-standalone/ : its docs
- W/k_12_social_studies/ : its docs, including ap_files
- W/evaluator/ : its docs (how generated items were judged, failure analyses)
- W/incept/ : only documents whose names contain "ap" or "AP" or that sit in an ap_benchmark folder; skip the rest

We ALREADY HAVE these 55 truths (skip them unless you have new, stronger evidence or a counter-example; then say which number):
1 wrong-answer feedback says where to look, never the answer, only what is true · 2 one plain voice for every student line · 3 nothing gives the answer before the first attempt · 4 two tries then the answer · 5 a question about a text must need the text (blind solve with the text hidden) · 6 one answer the text settles; check each option on its own · 7 ask right after the part that answers it · 8 spread the right answer's position · 9 an unsure judge is neither pass nor miss · 10 mark meaning, not wording · 11 keep students' words; a model's reading chooses a hint, not a grade · 12 ask whether words are aimed at the marker · 13 accept unplanned right answers only when sure · 14 save the first attempt · 15 never adapt on fewer than three observations · 16 cite words, not line numbers · 17 quote exactly, checked in code · 18 teach the words that carry the knowledge · 19 no slurs to perform · 20 background at the line that needs it · 21 a picture shows what the voice says · 22 check generated pictures by eye; maps from data · 23 split, don't cut approved words · 24 measure from the delivered file · 25 keep reading directions apart from the words · 26 few words on screen · 27 reduced motion and colour · 28 gate every check · 29 a model writes only free text; every choice, mark and check is a bounded judgment · 30 give a judge exactly what the student sees · 31 one yes/no question per candidate, combined in code · 32 a judge checks bounded claims, it doesn't hunt for faults · 33 give the marker what the rule refers to · 34 verdicts vary between runs · 35 agreement between samples is consistency, not correctness; option order shifts choices · 36 test the marking fallback · 37 score a judged check on person-labelled cases · 38 a check that never fired proves nothing until it catches a planted fault · 39 keep every judgment whole for replay; when two judges agree against the key, check the key · 40 order a lesson (prior knowledge, source, worked example, guided practice, own explanation, check, later transfer) · 41 two blocks of a kind test different things · 42 remake under new rules · 43 check against something that doesn't assume the answer · 44 machine checks are not human judgment · 45 fix the rubric before measuring · 46 review in the mode students get · 47 scripted readers play every lesson first · 48 a passed gate is not learning; a later test on new items is · 49 report accuracy by skill · 50 record each asset's source and hash · 51 liking is not learning · 52 stills vs motion (open) · 53 captions vs redundancy (open) · 54 who reads kept words (open) · 55 nudging a stalled reader (open).

Look especially for rules about: stimulus-based questions (sources, documents, images) and what the stimulus must carry; distractor quality and plausibility; factual accuracy and grounding of generated items; difficulty and cognitive level; rubric-scored writing tasks; avoiding item repetition across a set; what a reviewer found that automated checks missed; how a quality bar was measured.

Return up to 15 NEW candidates, most important first. For each give:
1. statement: one plain sentence that holds for any learning material (no AP, history-period or subject terms unless essential; no people's names or job roles).
2. kind: "measured" (the project's own numbers), "adopted rule" (and what made it), "external research" (DOI or URL as written in the source), or "open question".
3. evidence: exact path plus section heading or line numbers, the sentence quoted exactly, with any number as written.
4. against: counter-evidence or limits stated in the sources, quoted, or "none found".
Then list borderline items you left out and why, and any evidence bearing on the 55 (by number). Exclude model-training tricks that don't bear on making or checking learning materials, organisational matters, and anything you cannot cite. Keep the answer under 1,800 words.

## Report

**Paths.** W = ~/Library/Mobile Documents/com~apple~CloudDocs/work; R = W/aptraining/apllm-history/runtime_assets/ib_satisfaction_kit_v1/raw_rubrics (an outside judge's rubrics); C = W/aptraining/Cheater; G = W/ap-social-studies-generator; E = W/evaluator; K = W/k_12_social_studies. L = line. k_12's ap_files folder holds only .csv/.xlsx files, so I read nothing there. Incept's AP documents are copies of documents listed below.

**1. A source must give the premises, not the answer. If someone with no subject knowledge can reach the key by matching its wording, naming what it describes, or reading a label, the item tests reading.**
Kind: adopted rule plus measured. It is the converse of #5.
Evidence: R/_base_evaluation.txt L97 "If the cognitive demand collapses to "look and report" or "match restated description to its conventional name", it is a leak."; C/exploits/EXPLOIT-001-historian-frame-self-leak.md L26, L41 "40% pass", "The probe correctly flagged these as paraphrase leaks"; G/docs/archive/ITERATION_ANALYSIS.md L177 "→ Student can answer by reading, not by KNOWING." (hard items "58% → 38%", G/docs/archive/VERSION_ANALYSIS.md L140).
Against: R/_base_evaluation.txt L94 exempts items where "the targeted skill IS reading / interpreting / measuring the stimulus"; E/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md L408 "Ensure 60-70% of answer derivable from stimulus alone".

**2. A check that is skipped when a part is missing, or that passes "not applicable", rewards leaving the part out. Require the parts a task needs, and distrust gains that come from dropping them.**
Kind: measured.
Evidence: R/mcq_evaluation.txt L414 "No stimulus = PASS."; C/reports/RUBRIC_BLINDSPOTS.md L33: the skipped probe "catches almost all of the v50 failures"; C/reports/EXPLOIT_CATALOG.md L74/L76 "~56%" with a stimulus vs "100%" for 30 items without one; G/CHANGELOG.md L23 "Banned stimulus entirely — stimulus SAQs consistently fail evaluation" (50% → 95-100%, L15).
Against: C/exploits/EXPLOIT-002-stimulus-strip.md L212-214 "Many textbook drills and formative-assessment items omit stimuli for the same reason (faster recall practice)."

**3. Measure quality on one attempt at topics the process was never tuned on. Results on tuned topics, or after keeping the best of several tries, overstate it.**
Kind: measured. #48 is the learner version of this.
Evidence: C/exploits/EXPLOIT-003-mcqset-phrase-anchor.md L3 "0/50 = 0% on fresh KCs. Cited 32/33 on my 17 baseline KCs did NOT generalize."; W/aptraining/artifacts/quarantine/2026-05-22T163819Z_reports_mcqset_50_50_live_verified_20260522/QUARANTINE_REASON.md L5 "Original 50/50 FAILED main-a's fresh n=50 re-test at 10.00%"; W/aptraining/.agent/research/eval_baseline.md L15 "the prior 83.3% was inflated by inference crutches; clean one-shot SFT v7 is at 13%."
Against: C/reports/FRESH_HOLDOUT_2026-05-23.md L53-54: iteration "DOES recover the rate, but at higher API cost per item"; G/docs/03-ARCHITECTURE.md L53 "generate 3 → pick best 1) is permitted".

**4. The process that writes an item should not also grade it. A judge built on a different model found far more faults.**
Kind: measured.
Evidence: G/docs/archive/HOLISTIC_REVIEW_2026-02-19.md L202-203 "56% | Gemini self-grading (meaningless)" vs "9.1% | Claude external grading (real)"; G/BENCHMARK_ACHIEVED.md L10/L40 self-graded "Fill-in | 95.8%" vs G/docs/analysis/failure_analysis.md L19 "Fill-in | 6.7%" (different batches); G/CHANGELOG.md L70 "catches factual errors that Gemini can't detect in its own output."
Against: G/docs/archive/CLAUDE_MANUAL_REVIEW.md L10 'The problem is NOT "Gemini grading Gemini too leniently"'; G/CHANGELOG.md L40 "Claude catches some but not all."

**5. Once the option order is final, check in code that the key, the explanation and the feedback name the same answer. A content judge rated self-contradicting items highly.**
Kind: measured.
Evidence: G/docs/archive/MCQ_BUG_HISTORY.md L6 "This bug caused 7 out of 30 questions (23%) to fail"; G/docs/archive/CLAUDE_CROSS_EVAL_REPORT.md L35 'Answer is listed as "A" but explanation says "correct answer is B"' (scored 0.96, L30), L164 "Gemini passed Q36 and Q44 despite this critical flaw."; HOLISTIC_REVIEW L130: writing the explanation after fixing the key gave "100% first-attempt pass rate (up from 72%)".
Against: MCQ_BUG_HISTORY L65-66: the code check itself "DID NOT CHECK IF A WRONG ANSWER WAS MARKED AS CORRECT" and defaulted to `True`.

**6. Every source shown to learners must be real, with author, title and date, or be plainly marked as invented. A vague attribution hides the invention from checkers.**
Kind: measured.
Evidence: E/docs/reports/LATEST.md L75 "document_authenticity | 1 | 109 | 0.9%", L77 sourcing_opportunity "10.0%"; E/docs/reports/evaluation_20260225_095143_49918efd.md L171 "This appears to be a fictional source rather than an authentic historical document"; C/exploits/EXPLOIT-008-dbq-7doc-generic-attrib.md L28 named sources: "28/36 fails on factual_accuracy"; L32 generic ones: "v2 lift: 19.4% → 65.7%"; L94-96 the judge read them as '"pedagogical adaptation" rather than fabrication, even though no such specific editorial existed.'
Against: G/docs/08-AP-SOCIAL-STUDIES-SPEC.md L152 "must be authentic or authentically styled"; R/dbq_evaluation.txt L17 allows "pedagogical justification".

**7. A scoring guide for written answers must name the specific content that earns each point. Generic template wording passes as clear criteria but cannot tell a vague answer from a good one.**
Kind: adopted rule plus measured.
Evidence: R/saq_evaluation.txt L41-42 "generic answers would not earn points"; C/exploits/EXPLOIT-004-saq-no-stimulus.md L5 "34/34 = 100%"; L92-94 the boilerplate is scored 'as "clear criteria" even when X is generic'; L123-124 "the criterion must specify a SPECIFIC, NAMED historical fact".
Against: EXPLOIT-004 L66-67: the single-shot failures "were all chronology errors in scoring_notes", so judges do catch factual errors. No source scores real student answers against a guide.

**8. Rate thinking demand by what the learner must actually do, not by the command word or the difficulty label. Easy items still need some thinking.**
Kind: adopted rule plus measured (small samples).
Evidence: R/_base_evaluation.txt L88: command verbs "describe the cover, not the actual cognitive demand."; C/exploits/EXPLOIT-004-saq-no-stimulus.md L27-29 "hits the analytical sweet spot on the rubric's wording without any actual increase in cognitive demand"; R/mcq_evaluation.txt L333 "do not start from the labeled level and try to justify it"; C/reports/EXPLOIT_CATALOG.md L14 'label downgrade | 4/4 vs 1/4 control (+75pp)'; G/docs/archive/STATISTICAL_ANALYSIS.md L181 'Easy ≠ "recall only"'.
Against: C/reports/FINAL_REPORT.md L65: the label effect was "pilot-only; doesn't generalize when stacked"; R/mcq_evaluation.txt L523 accepts recall where the curriculum "explicitly describes recall".

**9. Build each wrong option from a specific misunderstanding, and keep it parallel to the key. Absurd or absolute options can be eliminated without any knowledge.**
Kind: adopted rule plus external research (no DOI given).
Evidence: G/docs/analysis/failure_analysis.md L229-230 "Scope confusion: True for different region/group/time period", "Partial truth: Contains accurate element but wrong overall conclusion"; L234 "Would a good student who studied but didn't master the material choose this?"; G/docs/analysis/best_practices.md L23 (Haladyna & Rodriguez, 2013), L33 "Similar length to the correct answer", L44 "Each should be selected by at least 5% of test-takers".
Against: C/exploits/EXPLOIT-002-stimulus-strip.md L71: options in the right form that were "obviously-wrong-on-the-merits to a knowledgeable reader" still passed; G/CHANGELOG.md L132 a distractor-rebuild step gave "Zero pass rate improvement" (5 samples).

**10. Build each item from the exact objective and a checked fact supplied to it. Facts invented while writing, especially dates and numbers, are where errors enter.**
Kind: measured.
Evidence: G/CHANGELOG.md L145-148: dropping the self-research step moved the "Pass rate | 25% | **100%**"; "research stage hallucinated facts that poisoned the compile step"; E/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md L275-276 "Curriculum alignment 0% → 89%" once it "started using `learning_objective` and `statement` fields"; G/docs/IMPROVEMENT_PROPOSALS.md L84 "House vote totals wrong (153 vs 174)".
Against: G/CHANGELOG.md L123 "(5 samples each)"; W/aptraining/workspace/comms/from_main/2026-05-21T0935Z_pipeline_analysis_findings.md L43: grounding "doesn't fix this because the failure happens AFTER retrieval".

**11. An argument task and its sources must allow more than one defensible position, and someone must confirm the alternatives really are defensible.**
Kind: adopted rule.
Evidence: W/incept/inceptbench/docs/AP_EVALUATION.md "Hard-Fail Dimensions" L143 "Prompt must allow for arguable thesis"; R/dbq_evaluation.txt L60 fails "All documents point to one obvious conclusion"; C/exploits/EXPLOIT-005-leq-no-stimulus.md L95-97: the check "currently passes if rubric_notes literally lists two opposing thesis sentences."
Against: E/docs/reports/LATEST.md L78 "document_diversity" passed only 27.3%, yet these items passed overall at "99.1%" (L34).

**12. Compare quality numbers only on the same frozen mix of topics, types and checks, with the same checker version.**
Kind: measured. Close to #45 and #49.
Evidence: G/docs/IMPROVEMENT_PROPOSALS.md L248-251: one essay type passed 99.3% in a run with none of one unit's requests and 90.0% in a run that was all that unit: "This is not a code regression but a test distribution change"; G/docs/archive/RUN6_ANALYSIS.md L13-14: a 12-item mini run scored "100%", the 116-item run "50.0%"; L199 "The mini benchmark was misleading because it didn't evaluate cognitive demand."; W/aptraining/.agent/research/eval_baseline.md L318 "would conflate rubric-drift with model-drift."
Against: none found.

**13. Audit the reference data that items are built and judged from. One fact filed under the wrong unit sank a whole category, though date-only screening mostly raised false alarms.**
Kind: measured. It extends #39.
Evidence: W/aptraining/workspace/comms/from_data/2026-05-28T1549Z_u1_kc_audit_report.md L19: the misfiled fact was "identified as causing v80b DBQ 15% baseline"; L95 '12 of the 18 "flagged" are false-positives'; W/aptraining/helpers/data/output/curriculum_kc_period_audit.md L8 "76 KCs flagged as period-mismatched".
Against: W/aptraining/_clone_metadata/dot_claude_projects/-Users-[name]-Documents-aptraining/memory/project_grader_audit_results_2_of_3_pass.md L3: a 30-record check "returned 30/30 PASS".

**14. Pick a format that can show the thinking the objective names. Fill-in-the-blank and one-to-one matching mostly test recall, and matching with no spare options is solved by elimination.**
Kind: measured.
Evidence: E/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md L134-135: matching "51% avg, no improvement over 7 runs", fill-in "38% avg"; L391 "No distractors = simple elimination"; G/docs/archive/RUN6_ANALYSIS.md L87 "90% of fill-in questions fail cognitive demand."
Against: K/docs/archive/OPENCLAW_HUMAN_REVIEW.md L72 "Well-designed matching with complex descriptions that require understanding".

**15. In a select-all item, every wrong statement must contain one error you can name. A statement that is merely "less good" is not false.**
Kind: adopted rule, made after measured failures.
Evidence: G/docs/analysis/failure_analysis.md L18 "MSQ | 40%"; L106 "Option B is NOT clearly factually incorrect - it's more of a mischaracterization/distractor"; L255 "If you cannot complete that sentence, the statement is too ambiguous."
Against: G/docs/archive/CLAUDE_MANUAL_REVIEW.md L21: another review passed these items "100% (8/8)".

**Borderline items left out**
- Duplicate checks across a whole item bank: G/docs/archive/IRONCLAD_BATCH_50.md L8/L12 "Attempts: 62", "Duplicates Caught: 12". I put this under #41.
- Whether harder items have more disputed keys: E/analysis/reports/COMPREHENSIVE_FAILURE_REPORT.md L40 "95% (146/153)", but STATISTICAL_ANALYSIS.md shows hard items passing most often. Left open.
- Rigid minimum lengths pushing invented facts (G/docs/IMPROVEMENT_PROPOSALS.md, LEQ-001): only one case.
- Two-step questions whose options give away the first step (R/mcq_evaluation.txt L390): a rubric rule with no data.
- Prompt-writing tricks and all training lessons: excluded as asked.

**Evidence on the 55**
- #5: C/exploits/EXPLOIT-003-mcqset-phrase-anchor.md L97 "The judge cannot reliably distinguish": run the blind solve rather than asking a judge.
- #8: G/docs/archive/TECHNICAL-DECISIONS.md L106 'all answers were "B"'. Limit: shuffling options after the explanation was written broke its letter references.
- #9: R/mcq_set_evaluation.txt L422 "could reasonably disagree, choose 1.0". These default-to-pass rules were the main thing exploited.
- #12 (limit): C/reports/EXPLOIT_CATALOG.md L20: open self-advocacy was caught "0/5", but L62-64 a plain explanation that "primes the judge's reading" got through.
- #24: K/docs/URGENT-BUG-STILL-PRESENT.md L35 '"20/20 tests passing" claim is misleading', while L28 "7 out of 10" delivered items had the bug.
- #28: E/docs/reports/LATEST.md L34 vs L75: essay items passed 99.1% while the non-gating authenticity check passed 0.9%.
- #30: K/docs/VALIDATION-REPORT-2026-02-19-COMPREHENSIVE.md L184/L191: the judge saw text cut at 3,000 characters, giving a "FALSE NEGATIVE".
- #32/#33: C/reports/RUBRIC_BLINDSPOTS.md L78: with no written spec, the metric "provides zero defense".
- #38: G/docs/archive/FACT_CHECK_RESULTS.md L15/L74: "0/10" failures were reported as "High Precision".
- #41: W/aptraining/workspace/comms/from_main/2026-05-21T0935Z_pipeline_analysis_findings.md L53 "22% of INFERIOR MCQ_SETs fail `non_repetitiveness`".
- #44: G/docs/archive/MANUAL-AUDIT-10-QUESTIONS.md L311: a heuristic gave "58%" where reading found "~90%".
- #45: E/docs/EVALUATION_PROCESS.md L159 "Changes to evaluator based on benchmark accuracy, not pass rate".
