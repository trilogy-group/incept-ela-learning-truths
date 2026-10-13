# Round 2: the AP project's learnings and evaluator docs

A read-only search agent, 2026-10-12 08:21 to 2026-10-12 08:35 UTC. Its brief and its final report, verbatim.

## Brief

Find lessons learned that hold for ANY lesson, course or set of learning materials, whatever the subject or text, each with its exact evidence. Thoroughness: very thorough. Context: these sources come from a project that generated and evaluated AP social studies questions (multiple choice, short answer, document-based and long essay) with trained models, aiming at a 97% quality bar.

STRICT RULES: read-only. Do not create, edit, move or delete files; run no command that writes; no network fetches. Never open .env, key or token files, and never print a secret. Files in iCloud Drive may be placeholders that download when read: read only documents (.md, .txt, .qmd, small .json), never data dumps (.jsonl, .csv, .sql, .zip, .xlsx, .parquet), model files or logs. Never read anything under ~/Library/Mobile Documents/com~apple~CloudDocs/personal/.

Sources (only these):
- "~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/" (all documents; start with INDEX.md; especially evaluation_methodology, research_educational_content_generation, mcq_set_journey, failures_and_false_starts, cross_team_learnings_full, prompt_engineering_deep_dive, research_rag_factual_grounding, research_model_size_vs_data_quality, training_data_journey, sft_v7_benchmark_postmortem, stage2_postmortem_full, what_is_ap_and_why_it_matters)
- "~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/" (AP_EVALUATION.md, internals/ap-evaluation.md and any doc on how generated items are evaluated)
- ~/Documents/APinceptbench/docs/ (AP_GENERATOR_SPEC.md, AP_QUESTION_TYPES_SPEC.md)

We ALREADY HAVE these 55 truths (skip them unless you have new, stronger evidence or a counter-example; then say which number):
1 wrong-answer feedback says where to look, never the answer, only what is true · 2 one plain voice for every student line · 3 nothing gives the answer before the first attempt · 4 two tries then the answer · 5 a question about a text must need the text (blind solve with the text hidden) · 6 one answer the text settles; check each option on its own · 7 ask right after the part that answers it · 8 spread the right answer's position · 9 an unsure judge is neither pass nor miss · 10 mark meaning, not wording · 11 keep students' words; a model's reading chooses a hint, not a grade · 12 ask whether words are aimed at the marker · 13 accept unplanned right answers only when sure · 14 save the first attempt · 15 never adapt on fewer than three observations · 16 cite words, not line numbers · 17 quote exactly, checked in code · 18 teach the words that carry the knowledge · 19 no slurs to perform · 20 background at the line that needs it · 21 a picture shows what the voice says · 22 check generated pictures by eye; maps from data · 23 split, don't cut approved words · 24 measure from the delivered file · 25 keep reading directions apart from the words · 26 few words on screen · 27 reduced motion and colour · 28 gate every check · 29 a model writes only free text; every choice, mark and check is a bounded judgment · 30 give a judge exactly what the student sees · 31 one yes/no question per candidate, combined in code · 32 a judge checks bounded claims, it doesn't hunt for faults · 33 give the marker what the rule refers to · 34 verdicts vary between runs · 35 agreement between samples is consistency, not correctness; option order shifts choices · 36 test the marking fallback · 37 score a judged check on person-labelled cases · 38 a check that never fired proves nothing until it catches a planted fault · 39 keep every judgment whole for replay; when two judges agree against the key, check the key · 40 order a lesson (prior knowledge, source, worked example, guided practice, own explanation, check, later transfer) · 41 two blocks of a kind test different things · 42 remake under new rules · 43 check against something that doesn't assume the answer · 44 machine checks are not human judgment · 45 fix the rubric before measuring · 46 review in the mode students get · 47 scripted readers play every lesson first · 48 a passed gate is not learning; a later test on new items is · 49 report accuracy by skill · 50 record each asset's source and hash · 51 liking is not learning · 52 stills vs motion (open) · 53 captions vs redundancy (open) · 54 who reads kept words (open) · 55 nudging a stalled reader (open).

Return up to 15 NEW candidates, most important first. For each give:
1. statement: one plain sentence that holds for any learning material (no AP, history-period or subject terms unless essential; no people's names or job roles).
2. kind: "measured" (the project's own numbers), "adopted rule" (and what made it), "external research" (DOI or URL as written in the source), or "open question".
3. evidence: exact path plus section heading or line numbers, the sentence quoted exactly, with any number as written.
4. against: counter-evidence or limits stated in the sources, quoted, or "none found".
Then list borderline items you left out and why, and any evidence bearing on the 55 (by number). Exclude model-training tricks that don't bear on making or checking learning materials (hyperparameters, GPUs, infrastructure, vendors), organisational matters, and anything you cannot cite. Keep the answer under 1,800 words.

## Report

I found 15 new candidates, listed most important first. Paths are shortened as follows:
- **ML** = `~/Library/Mobile Documents/com~apple~CloudDocs/work/ML learnings/`
- **IB** = `~/Library/Mobile Documents/com~apple~CloudDocs/work/inceptbench/docs/`
- **AP** = `~/Documents/APinceptbench/docs/`

IB/AP_EVALUATION.md and IB/internals/ap-evaluation.md are identical. The docs that cover only infrastructure (beads, render, fireworks) were searched for keywords, not read in full.

## New candidates

**1. Every name, date or figure a writer must list is another chance to be wrong, so marking guides should describe the reasoning that earns credit.**
- **Kind:** measured.
- **Evidence:** ML/gemini_benchmark_relentless.md L122–126: "15 of 17 factual_accuracy failures were in the scoring notes". After the guides were changed to "Describe analytical reasoning that earns the point (no evidence lists)": "15 of 17 factual_accuracy failures in SAQ disappeared immediately". L181: "The single biggest per-change jump". ML/prompt_engineering_deep_dive.md L56–57: with no named source, factual_accuracy was "70%" against a baseline of "60%".
- **Against:** AP/AP_GENERATOR_SPEC.md L69: "specific evidence required". ML/sft_v7_benchmark_postmortem.md L62: the smaller model ignored the ban — "it uses wrong specific facts instead of right ones."

**2. Give the writer one verified fact as its only source and forbid anything not in it, because facts offered as inspiration get embellished.**
- **Kind:** measured, plus external research.
- **Evidence:** ML/training_data_journey.md L119: "Even with 5 relevant curriculum facts injected, the model fabricates its own historical claims". ML/knowledge_and_rag_pipeline.md L102: "facts work better as CONSTRAINTS than as INSPIRATION". ML/mcq_set_journey.md L152–153: "~90-95%" rose to "97-100% | … Plan step added, anchor_fact". External (https://arxiv.org/html/2508.04442), quoted in ML/research_educational_content_generation.md L92: "RAG methods go from 12-15% validity to 92-96% validity".
- **Against:** on the small model it was "Not yet tested in benchmark" (ML/training_data_journey.md L128). Also: "the model will sometimes follow the constraint, sometimes not" (ML/prompt_engineering_deep_dive.md L113).

**3. Make "is this about what was asked?" its own blocking check, because overall quality scores barely penalise a well-made item on the wrong topic.**
- **Kind:** measured.
- **Evidence:** ML/stage2_postmortem_full.md L47: "The wrong-topic outputs scored 0.82 on InceptBench for a completely different topic." IB/legacy/EVALUATORS.md L122 already uses such a check: "`query_relevance` - Topic alignment (**VETO**: <0.4 = auto-reject)". An illustrative sample in IB/user_guides/examples.md L218–248 gives the lesson "Congruent and Similar Triangles" and the item "What is the value of x in 3x + 7 = 22?" a score of "0.88".
- **Against:** 0.82 still missed the 0.85 pass mark. curriculum_alignment is already a hard fail for SAQ, LEQ and DBQ (ML/evaluation_methodology.md L48–50).

**4. A wrong answer key or wrong fact must void the item, and no average may buy it back.**
- **Kind:** adopted rule, made after an averaging bug.
- **Evidence:** IB/legacy/EVALUATORS.md L47–51: "final score is overridden to 0.0 regardless of other evaluator scores" and "Prior to v1.4.0, answer verification incorrectly added 0.0 to the average (asymmetric penalty)." ML/evaluation_methodology.md L40: "An item can score 0.92 overall and still hard-fail". This refines #28.
- **Against:** "The evaluator was designed as a quality gate, not a reward shaper" (ML/grpo_failures_deep_dive.md L19). A pass/fail gate says nothing about near misses.

**5. Read the failing items themselves, because an unchanged average can hide a new kind of failure.**
- **Kind:** measured.
- **Evidence:** ML/stage2_postmortem_full.md L30: "Average score: 0.833 (Stage 2) vs 0.836 (sft-v4) — nearly identical". L49: "Caught by: Looking at the actual content of regressed items, not just the scores."
- **Against:** "Not every failure needs a full root-cause investigation" (ML/debugging_methodology.md L209).

**6. Don't let later steps build on the writer's own unchecked notes, because their errors compound.**
- **Kind:** measured.
- **Evidence:** ML/mcq_set_journey.md L44–48: "Research→Compile (single step): 60%" against "Stimulus (from scratch, no research)→Questions: 80% — best"; "The research step was a hallucination amplifier, not a quality gate."
- **Against:** the same file, L36: "MCQ: 96% → 100% (research step immediately improved factual accuracy)".

**7. Warnings and bans don't steer a writer; giving it the material it is allowed to use does.**
- **Kind:** measured.
- **Evidence:** ML/prompt_engineering_deep_dive.md L57 and L61: "baseline | 45%" against "caution | 30%". ML/failures_and_false_starts.md L124: such warnings "just introduce hedging behavior". ML/stage2_postmortem_full.md L77–82: after "DO NOT write about any other topic", "Failures persisted."
- **Against:** "Gemini is large enough to mostly respect the "no specific evidence" instruction" (ML/sft_v7_benchmark_postmortem.md L132).

**8. Check the scope labels an item is built from (course, unit, period) before judging its content, and pass them along explicitly rather than re-deriving them.**
- **Kind:** measured.
- **Evidence:** ML/gemini_benchmark_relentless.md L31: "No amount of prompt engineering can fix wrong metadata". L35: "All APEURO Unit 4 questions went from 0% to baseline pass rate (~80%) instantly". L79–83: "Pass explicit `course` and `unit` from the request body, not re-derived", giving "~3-4% total improvement".
- **Against:** none found.

**9. Never attach a picture the task doesn't use, or describe one the learner can't see.**
- **Kind:** measured.
- **Evidence:** ML/gemini_benchmark_relentless.md L45–49: "SAQs with decorative images are marked as INFERIOR"; removing them gave "~2-3% improvement". L65–69: "A "visual document" with no image is a structural contradiction"; fixing it gave "~2% improvement".
- **Against:** AP/AP_GENERATOR_SPEC.md L11 allows "image|map|chart" stimuli. Images in question sets were never judged: "Image is stripped before InceptBench evaluation" (ML/mcq_set_journey.md L72).

**10. Making several versions and keeping the best fixes only random slips; repeated mistakes need their cause fixed.**
- **Kind:** measured, by another team using the same evaluator.
- **Evidence:** ML/cross_team_learnings_full.md L27–33: "N=1: 88.89%", "N=5: 98.6%", "Best-of-N can't overcome systematic failures". ML/research_model_size_vs_data_quality.md L140: "even N=100 won't reliably get to 90%+ because the type of failures … is deterministic".
- **Against:** none found.

**11. Confirm items picked by a judge's score with a check that took no part in picking them.**
- **Kind:** external research, plus a proposed rule that was never adopted.
- **Evidence:** ML/research_dpo_grpo_factual.md L146 (https://arxiv.org/html/2510.17733v1): "continuous rewards get gamed by output style (longer, more confident responses get higher scores even with wrong facts)". ML/research_model_size_vs_data_quality.md L123: "reward model errors accumulate". ML/grpo_design_and_theory.md L171: "Use a held-out test set that's NOT used during GRPO training."
- **Against:** the top-scored candidate "correlates with being genuinely better even if the noise is high" (ML/evaluation_methodology.md L137).

**12. Settle anything that can be computed in code before a judge sees it, and bind the judge to the proven results.**
- **Kind:** measured. This extends #17 and #43.
- **Evidence:** IB/MATH_VERIFIER.md L7: the same question "may be scored 1.0 in one run and 0.0 in the next". L109–116: "81 unique math questions … 3 runs each", "Regressions | **0**", "Perfect consistency (0 variance) | All 81 questions". L84: "Evaluator MUST accept `factual_accuracy = 1.0`".
- **Against:** L88: "the extraction step can sometimes misrepresent the problem". The gain was only "Net improvements | **+3**".

**13. A source shared by several questions needs a distinct element for each question, and one error in it spoils all of them.**
- **Kind:** adopted rule (an evaluator hard fail); the sources don't record what made it.
- **Evidence:** ML/evaluation_methodology.md L107: a sound stimulus "can still fail stimulus_quality if it doesn't have enough substance for 3 different questions to reference". L54: "One bad detail in the stimulus fails the entire 3-question set."
- **Against:** the published spec only checks "Questions must require the stimulus" (IB/AP_EVALUATION.md L141).

**14. Write marking criteria for each question rather than generic ones.**
- **Kind:** external research.
- **Evidence:** ML/research_educational_content_generation.md L60 (https://arxiv.org/html/2503.23989v1): "Question-specific rubrics: Spearman correlation 0.763-0.906 with human grades vs 0.510 for generic rubrics".
- **Against:** the study is on "code evaluation" (L59). Candidate 1 shows that named examples specific to a question were where errors gathered.

**15. Revise one thing at a time and re-measure, so each gain or loss has one cause.**
- **Kind:** measured.
- **Evidence:** ML/overnight_automation.md L212: "Multiple simultaneous changes = unknown attribution". ML/gemini_benchmark_relentless.md L197: "~40-50 iterations over 48 hours. Most iterations were 0.0% improvement. 9 were significant."
- **Against:** the automated reviewer "Sometimes proposed a prompt change that made things slightly worse (0.5% regression)" and "Rarely caught code bugs" (ML/overnight_automation.md L225–226). An automated improvement agent with too broad an objective "Claimed 90% MCQ_SET pass rate (actual: 70-75%)" (ML/failures_and_false_starts.md L103).

## Borderline items left out
- **Example items leak their content into new ones** (ML/failures_and_false_starts.md L120–122, "40%" against "45%"): that is one item's difference at N=20.
- **A question set should cover the whole objective** (ML/sft_v7_benchmark_postmortem.md L71): one judge comment on 4 items, the fix is untested, and it is close to #41.
- **"plausible distractors, parallel structure, no absolutes"** (AP/AP_GENERATOR_SPEC.md L29): a spec rule only, and the matching check is soft (it doesn't block) in IB/AP_EVALUATION.md L150.
- **"Prompt must allow for arguable thesis"** (IB/AP_EVALUATION.md L143): applies to argument tasks only.
- **Rejecting stacked cultural clichés** (IB/legacy/EVALUATORS.md L244): nothing records what made the rule, and it is close to #19.
- **Rarer topics fail more** (ML/knowledge_and_rag_pipeline.md L217): the source only says it "partially explains", with no numbers.
- **Items that test only recall fail** (ML/what_is_ap_and_why_it_matters.md L57): specific to this course type.
- **Data audits, whole-item deduplication, hard negatives, thinking traces, token limits:** model training or infrastructure.

## Evidence bearing on the 55
- **#3:** an image hard fail, "`answer_leakage` - Shows solutions" (IB/legacy/EVALUATORS.md L150).
- **#5 and #6:** hard fails "Questions must require the stimulus" and "Exactly one answer must be defensibly correct" (IB/AP_EVALUATION.md L140–141). Also "Check all distractors against computed answer" (IB/MATH_VERIFIER.md L70).
- **#8:** "chi-square answer balance analysis" (IB/MATH_VERIFIER.md L74). A model "biased toward one answer class because training data had 70/30 split" (ML/cross_team_learnings_full.md L147).
- **#17 (the project did the opposite):** each source passage was a "primary source passage attributed to the historical author in the plan" (ML/mcq_set_journey.md L63). The judge marks down text that "doesn't sound like a period-authentic primary source" (ML/evaluation_methodology.md L102). So invented words were put under real names, and nothing checks them against a real text.
- **#24 and #38:** "We never got a clean MCQ benchmark on any SFT model until now" (ML/sft_v7_benchmark_postmortem.md L189). "EVERY tick was being silently aborted" (ML/overnight_automation.md L74). A planted fault was proposed but not done: "mutate one fact … confirm mutated version fails" (ML/master_strategy_apr24.md L82).
- **#30 (the project did the opposite):** "Image is stripped before InceptBench evaluation" (ML/mcq_set_journey.md L72).
- **#31:** each rule is "evaluated via its own micro-prompt that returns `score: 1` (pass) or `score: 0` (fail)" (IB/legacy/EVALUATORS.md L246).
- **#34 (stronger evidence):** over "N=4 repeated trials", flip rates were "MCQ_SET: 50%", "DBQ: 30%", "SAQ: 10%", "LEQ: 0%" and "MCQ: 0%" (ML/evaluation_methodology.md L123–128). That means "±10% uncertainty" at N=20 (L139). Reused items had only "just passed InceptBench at the time, which has a 50% flip rate" (ML/mcq_set_journey.md L112).
- **#36:** the math checker falls back "with zero degradation", and its test had "Regressions | **0**" over 486 evaluations (IB/MATH_VERIFIER.md L9, L113–114). Counter-case: a step that "silently fell back to a legacy one-shot path" (ML/mcq_set_journey.md L31).
- **#44:** "97% pass rate does NOT mean 97% of questions are publishable" and "a confusing but technically correct question can pass" (ML/evaluation_methodology.md L187–189). Externally, "31% are rejected" (ML/research_educational_content_generation.md L14).
- **#45 (counter-evidence, the project's docs disagree on the rubric):** ML/evaluation_methodology.md L38 and L46 say "Pass = overall_score >= 0.85 AND all hard-fail dimensions = 1.0", with MCQ hard fails "factual_accuracy, educational_accuracy". IB/AP_EVALUATION.md L139–160 says "Overall score > 0.90, OR" a borderline band, with different hard fails such as "answer_validity". One evaluator was "incorrectly weighted 3x" (IB/legacy/EVALUATORS.md L187). The API doc advises pinning a version for "Consistency across a batch" (IB/user_guides/api.md L308).
- **#50:** "Every response echoes the evaluator version that produced it" (IB/user_guides/api.md L292). Hashing only the first 200 characters gave "A 34% false dedup rate" (ML/training_data_journey.md L14).
- **#53:** the docs' own sample states the picture's content in words ("each basket contains 4 apples and there are 3 baskets") and scores "0.95" (IB/user_guides/examples.md L443–458), while decorative SAQ images were marked "INFERIOR".
