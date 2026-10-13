# Round 2: the knowledge bot, first half

A read-only search agent, 2026-10-12 08:21 to 2026-10-12 08:40 UTC. Its brief and its final report, verbatim.

## Brief

Find lessons learned that hold for ANY lesson, course or set of learning materials, whatever the subject, grade or text, each with its exact evidence. Thoroughness: very thorough. The source is a knowledge store kept for a Grade 3 (and Grade 5) reading course build: each entry under knowledge/ summarises one source (course-build retrospectives, reviews, learning-science notes, feedback documents, evaluation reports).

STRICT RULES: read-only. Do not create, edit, move or delete files; run no command that writes; no network fetches; do not run the bot or any script. Never open any .env file (one exists in ~/Projects/grade3-reading/knowledge_bot/), key or token files, and never print a secret.

Sources (only these), under ~/Projects/grade3-reading/knowledge_bot/:
- README.md, INDEX.md (one line per entry: use it to choose), MAP.md, ROUTER.md, BRIEFING.md, CHECKLIST.md, HOTBUCKET.md
- knowledge/kb-0001 … kb-0125: read the entries about lesson and course design, assessment and question quality, learning science and its sources, review feedback and what reviewers found, evaluation of courses or items, and AI generation or judging of learning content. Skip vendor or platform product notes and tooling entries.
If a source file's name contains a person's name, say so, and give the same evidence from another file if one exists.

We ALREADY HAVE these 55 truths (skip them unless you have new, stronger evidence or a counter-example; then say which number). Entries kb-0069, kb-0070, kb-0099 and kb-0235 have already been used.
1 wrong-answer feedback says where to look, never the answer, only what is true · 2 one plain voice for every student line · 3 nothing gives the answer before the first attempt · 4 two tries then the answer · 5 a question about a text must need the text (blind solve with the text hidden) · 6 one answer the text settles; check each option on its own · 7 ask right after the part that answers it · 8 spread the right answer's position · 9 an unsure judge is neither pass nor miss · 10 mark meaning, not wording · 11 keep students' words; a model's reading chooses a hint, not a grade · 12 ask whether words are aimed at the marker · 13 accept unplanned right answers only when sure · 14 save the first attempt · 15 never adapt on fewer than three observations · 16 cite words, not line numbers · 17 quote exactly, checked in code · 18 teach the words that carry the knowledge · 19 no slurs to perform · 20 background at the line that needs it · 21 a picture shows what the voice says · 22 check generated pictures by eye; maps from data · 23 split, don't cut approved words · 24 measure from the delivered file · 25 keep reading directions apart from the words · 26 few words on screen · 27 reduced motion and colour · 28 gate every check · 29 a model writes only free text; every choice, mark and check is a bounded judgment · 30 give a judge exactly what the student sees · 31 one yes/no question per candidate, combined in code · 32 a judge checks bounded claims, it doesn't hunt for faults · 33 give the marker what the rule refers to · 34 verdicts vary between runs · 35 agreement between samples is consistency, not correctness; option order shifts choices · 36 test the marking fallback · 37 score a judged check on person-labelled cases · 38 a check that never fired proves nothing until it catches a planted fault · 39 keep every judgment whole for replay; when two judges agree against the key, check the key · 40 order a lesson (prior knowledge, source, worked example, guided practice, own explanation, check, later transfer) · 41 two blocks of a kind test different things · 42 remake under new rules · 43 check against something that doesn't assume the answer · 44 machine checks are not human judgment · 45 fix the rubric before measuring · 46 review in the mode students get · 47 scripted readers play every lesson first · 48 a passed gate is not learning; a later test on new items is · 49 report accuracy by skill · 50 record each asset's source and hash · 51 liking is not learning · 52 stills vs motion (open) · 53 captions vs redundancy (open) · 54 who reads kept words (open) · 55 nudging a stalled reader (open).

Return up to 15 NEW candidates, most important first. For each give:
1. statement: one plain sentence that holds for any learning material (no Grade 3 or reading-only terms unless essential; no people's names or job roles).
2. kind: "measured" (the project's own numbers), "adopted rule" (and what made it), "external research" (DOI or URL as written in the source), or "open question".
3. evidence: exact path plus line numbers or section heading, the sentence quoted exactly, with any number as written.
4. against: counter-evidence or limits stated in the sources, quoted, or "none found".
Then list borderline items you left out and why, and any evidence bearing on the 55 (by number). Exclude organisational matters (approvals, meetings, team direction) and anything you cannot cite. Keep the answer under 1,800 words.

## Report

I found 15 new candidates. All come from the entries and root files you listed. I didn't open any `.env` file and didn't write or change anything. † marks a file whose name contains a person's name.

**Paths.** Root files: ~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md, ~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md, ~/Projects/grade3-reading/knowledge_bot/INDEX.md, ~/Projects/grade3-reading/knowledge_bot/ROUTER.md. Entries are in ~/Projects/grade3-reading/knowledge_bot/knowledge/:
- kb-0005-[name]-canonical-fsrs-hinge-discipline.qmd† ([name]), kb-0010-amalgamation-v2-engine-results.qmd, kb-0011-run6-amalgamation-v2-engine-output.qmd, kb-0022-incept-team-sync-2026-06-17.qmd, kb-0023-canonical-definition-debate.qmd, kb-0027-learning-science.qmd, kb-0028-non-negotiables.qmd
- kb-0058-eval-reading-explorers-g3-allqtypes.qmd, kb-0059-map-equivalent-test-design-v4.qmd, kb-0063-aptraining-prior-exploration.qmd, kb-0064-insight-stimulus-provenance-unlock.qmd, kb-0068-g5-static-dataset-intake-2026-06-23.qmd, kb-0071-knowledge-[name]-branch-and-additions-2026-06-24.qmd† ([name]), kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd, kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd, kb-0076-coe-catchup-2026-06-30.qmd
- kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd† ([name]), kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd, kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd, kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd, kb-0085-g5-red-team-findings-2026-07-06.qmd, kb-0086-round2-feedback-brainlifts-2026-07-09.qmd
- kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd, kb-0092-student-ready-criticism-framework-2026-07-09.qmd, kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd, kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd, kb-0098-incept-service-coe-catchup-2026-07-09.qmd, kb-0100-[name]-lanes-execution-2026-07-10.qmd† ([name])
- kb-0110-can-reading-comprehension-be-taught.qmd, kb-0111-cervetti-2016-knowledge-effect-full.qmd† (the author, Cervetti), kb-0118-curriculum-architecture-brainlift-core.qmd, kb-0120-rivers-demo-unit-live-2026-07-13.qmd, kb-0121-teaching-comprehension-insights-brainlift.qmd, kb-0124-eduqwen-pedagogical-llm-paper.qmd, kb-0125-coe-catchup-2026-07-13.qmd

## New candidates

**1. Teach, practise and test the same thinking step, and make every skill label match what the item actually asks.**
- Kind: adopted rule, made by the reviewers' second-round findings.
- Evidence: kb-0086 l.60 "I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill." l.92 "a main-idea lesson served an inference/evidence item." l.132 "do not teach one cognitive operation and assess another." kb-0093 l.122 "Coverage is false if an "analyze" standard is assessed by "identify.""
- Against: kb-0121 l.61 "Assessment format is not instruction format (the marathon rule)". The format may differ; the thinking step may not.

**2. A gate, read-check or feedback rule counts only once it is seen working in the delivered product against someone who clicks through, skips the material or answers everything wrong.**
- Kind: adopted rule, made by the reviewers' hands-on walkthroughs.
- Evidence: kb-0081 l.120 "earned a stamp on "The Amazing Axolotl" at about 20 percent accuracy by clicking through without reading". kb-0086 l.101 "reviewers earned the pass while answering every question incorrectly". kb-0086 l.130 "skippable "pause and think" is not a check". kb-0058 l.37 "`masteryThreshold:90` declared in metadata, not enforced by an observable mechanism". CHECKLIST.md l.44 ""authored" ≠ "resolves""; l.14–15 "a PUT can return 200 yet silently revert."
- Against: only intuition. kb-0076 l.26 "[name] manually disputes (a G3 student lacks the background knowledge to guess)"; the same line answers "the empirical signal is stronger than the intuition". This is the student-facing twin of #38.

**3. Let taught knowledge come back and build through the learning materials, and keep never-seen material for the test.**
- Kind: external research (Cervetti, Wright & Hwang 2016, DOI 10.1007/s11145-016-9628-x, from kb-0111† l.25) plus an adopted rule from review issue #3.
- Evidence: kb-0081 l.68 "A child can find the main idea fifty times on fifty disconnected passages and never accumulate the knowledge that makes main ideas easy to find." kb-0081 l.70 "reserve cold, non-overlapping passages for the test only". kb-0121 l.66 "Coherent-set readers gained 5.59 vs 2.63 concept idea-units (η²=.32)" — the same result without the person-named file (also l.54). kb-0118 l.82 "use the curriculum to keep generative knowledge warm by use; use spaced practice for the residue."
- Against: kb-0098 l.38–39 "knowledge-building can be gamed if later questions become answerable from earlier lessons". kb-0121 l.48 "near-domain at best (Cervetti η²=.09)". kb-0111† l.9 "comprehension-question scores were ns (measure unreliable, alpha=.46)".

**4. Items that pass one by one do not make a good lesson or course; judge whole lessons and the sequence as well.**
- Kind: measured.
- Evidence: kb-0083 l.30 lessons "| INFERIOR | **73** |" (of 76), against l.42 items "| SUPERIOR | 529 |" (of 1,026). kb-0083 l.64 "avg 0.14; 65 of 76 bundles scored exactly 0" on non-repetition. kb-0076 l.33 "G3 passed **individual item** evals but **NOT** the holistic **course-level** eval". kb-0125 l.102 "new metrics are needed to assess lesson sequencing".
- Against: kb-0083 l.94 "the 0.0s on multi-passage bundles say more about eval packaging than content."

**5. Nothing generated should reach learners on its author's judgment; certify each piece with an independent checker from a different model family.**
- Kind: adopted rule, made by measured leak rates.
- Evidence: kb-0121 l.34 "\~78% of raw generated reading items were answerable without the passage, correct answers sat at position A 79% of the time". kb-0091 l.231 "Use a different family for the gate than for the author. Never same-family certify." kb-0091 l.26 "The questions were good because the generator was not trusted." kb-0085 l.30 "RT-8 self-graded "PASS — 0 blocking"".
- Against: kb-0072 l.76–77 "prior call was that re-checking IB+Opus-passed items is redundant" (the same call is in kb-0071† l.49). kb-0096 l.44 shows the verdict swings with the solver chosen.

**6. Treat whatever an AI quality grader passes as candidates only: run deterministic structure checks and a separate leak test on all of it, and expect most to be cut.**
- Kind: measured.
- Evidence: kb-0068 l.66 "pass_rows: 8937", then l.109–110 "deterministic_pass: 3077" / "deterministic_fail: 5860". kb-0068 l.195 "IB+Opus passing is not enough". kb-0059 l.47: InceptBench "graded answer-leaking items 1.0". kb-0091 l.141 "735/1,152" passed even the with-passage control.
- Against: the redundancy call in kb-0072 l.76–77, and kb-0083 l.94 (graders also fail things wrongly). Fits #32.

**7. A model's score on questions about teaching is no evidence that what it generates teaches; judge the generated material itself.**
- Kind: external research (Singh et al. 2026, DOI 10.3389/frai.2026.1851993).
- Evidence: kb-0124 l.94–95 "strong benchmark performance on pedagogical knowledge questions does not itself constitute evidence of effective classroom tutoring". kb-0121 l.46 "the gap is invisible to benchmarks and only measurable at the artifact level". kb-0121 l.34 "a dose that "knew" gradual release still leaked its item's answer".
- Against: still an open question. kb-0124 l.88: the training moved the model "toward guided-learning-like response patterns". kb-0125 l.92–94 plans to train a model on "pedagogical principles". HOTBUCKET.md l.126–127 "left downstream transfer as an experiment".

**8. Before trusting a score or a gain, test the measuring set-up itself and keep the same judge, model and pass bar in every condition.**
- Kind: measured.
- Evidence: kb-0063 l.39–41 "the "stuck at ~28%" narrative was largely measurement artifact (wrong field read, grader on wrong host…)". kb-0064 l.24 "**0.29→0.95** jump existed only under a **discredited Gemini judge**". INDEX.md l.113 "claimed lift is INVALID because all sampled C0 records used GPT-4.1 under an older bar while C1 used Gemini 2.5 Flash under the loosened bar" — the same evidence as kb-0100† l.42–47.
- Against: none found. This widens #45.

**9. Results from simulated learners or expert-set difficulty show direction, not size; every result should say what it does not prove until real learners' data exist.**
- Kind: measured, plus external research (Wright & Stone 1979; Linacre 1994, as cited, no DOI).
- Evidence: kb-0010 l.57 "Direction is the trustworthy signal; magnitudes are not." kb-0010 l.110 "2 of 5 recs delivered as predicted, 3 backfired". kb-0010 l.124 "individual-level r ≈ 0.42". kb-0080 l.94 "item difficulties are expert-assigned, not estimated from student responses". kb-0080 l.157–158 "SE(b-hat) <= 0.30 logits needs N >= 200 responses/item".
- Against: kb-0010 l.41: the simulation still found a real "structural cliff". It is good for finding structure, not size. This limits #47.

**10. Fixing one failure can break another, so re-check every quality after a fix; leak-proof is necessary, not sufficient.**
- Kind: measured.
- Evidence: kb-0091 l.122–125: 13/13 items passed the structure and leak checks, "only 4/13 LLM quality-B pass". kb-0091 l.127 "anti-leak success alone is insufficient". kb-0085 l.25–26 "RT-2 accessibility: anti-leak concentrates items into TEI formats (525/772), no attestation." kb-0092 l.31.
- Against: none found, though the sample is small (kb-0091 l.239).

**11. After a miss, reteach and then retest later on new items of the same difficulty; never re-serve the same items or jump to harder ones.**
- Kind: measured (the incumbent course's cohort) plus an adopted rule.
- Evidence: kb-0079† l.37 "Difficulty escalates after a miss; attempt-2 supporting-detail accuracy **64% -> 41%**". No other file has this figure; kb-0011 l.121 only names the rule `retry_path_reteach_first_no_escalation`. kb-0086 l.141 "a delayed test with new items." kb-0058 l.60 "2-3 forms each so three-state retry works".
- Against: kb-0022 l.63 (an earlier design) "same test re-shown". kb-0080 l.252: a small bank means "repeated items on retake". Touches #15 and #48.

**12. Teach and test how parts combine, explicitly; passing each part does not mean learners can use them together.**
- Kind: adopted rule.
- Evidence: kb-0118 l.110 "Students can "master" individual KCs yet fail whenever they must select, combine, or justify them in context." kb-0118 l.116 "The mastery gate for an integrative lesson must test the integration". kb-0086 l.123. kb-0093 l.129.
- Against: none found.

**13. When learners must recall, explain or produce, check them that way; recognition items and "I know it" overstate knowledge.**
- Kind: external research (Curtis, via Beck, McKeown & Kucan 2013; no DOI in the source) plus an adopted rule.
- Evidence: kb-0121 l.72 "\~80% of students check a word as "known," \~50% can give an example, \~20% can explain it". kb-0093 l.124 ""Write/explain/draw" targets cannot be assessed by MCQ alone." kb-0028 l.29 "Practice must require recall, not just recognition."
- Against: kb-0074 l.49 "FRQ-stays-out" — matching the target test's all-selected-response format pulled the other way.

**14. Don't let surface cues give the answer away: a correct option longer than the others, a matching set with no spare option, or a second part that restates the first.**
- Kind: measured.
- Evidence: kb-0121 l.77 "the correct option was systematically the longest". kb-0068 l.117 "longest-option-tell: 626"; l.116 "unused-right-bucket-exists: 638". kb-0121 l.78 "6 of 6 sampled two-part evidence items were blind-solvable, with Part B restating Part A".
- Against: kb-0096 l.29 and l.72: a solver that "guessed from option-length and wording tells" flagged items that were "still clean". This extends #8.

**15. Standards fix what must be covered, not the teaching order; give any model drafting a sequence the ordering policy, and feed it the sources one at a time in order of authority.**
- Kind: adopted rule, from the Curriculum Architecture BrainLift, which ROUTER.md l.64 makes the authority.
- Evidence: kb-0118 l.59 "use the standard to constrain scope (what must appear), but apply independent judgement about order". kb-0118 l.74: without a policy "the sequence will reflect whatever assumptions the model happens to import". kb-0118 l.67: blending all sources in one pass "is not synthesis at all". kb-0086 l.119.
- Against: kb-0125 l.92–94 proposes training a model "on the team's pedagogical principles" instead; still open.

## Borderline items left out
- **"90%" on a very short test means a perfect score** (kb-0058 l.37; kb-0093 l.141): true but narrow.
- **One dated count per number** (kb-0080 l.116 "number drift in documents (0.930 vs 0.928)"): close to an organisational matter.
- **Difficulty is a match, not a single number** (kb-0121 l.59): the evidence is reading-only.
- **Strategy teaching saturates**, "Ten sessions yield the same benefit as fifty" (kb-0110 l.45): reading strategies only.
- **Partial credit for two-part items** (kb-0072 l.86): contested, since "the TR scores composite items dichotomously" (kb-0080 l.74).
- **Rewards only for verified learning** (kb-0028 l.23): a platform rule.
- **Hand-build the first one or two courses before automating** (kb-0076 l.16): a meeting decision.
- **Set the guessing floor from the actual scoring rule** (kb-0100† l.91–92): one person-named source only.
- **Block first, interleave later** (kb-0086 l.160): conflicts with CHECKLIST.md l.45.
- **One fixed wording per key term** (kb-0005†): contested as "just simulated students" (kb-0023 l.28).
- **Practise in the test's formats** (kb-0080 l.123): conflicts with the "marathon rule" (kb-0121 l.61).

## Evidence bearing on the 55
- **#5:** stronger numbers. kb-0121 l.76 "\~78% … answerable without the passage"; kb-0076 l.26 "75.3% leakable". Limits: kb-0121 l.47 says an in-lesson check of taught knowledge "is legitimate"; kb-0096 l.44 shows the same items scored "1.0" with one solver and "about 0.0" with another.
- **#5/#6:** only "735/1,152" items passed the with-text control (kb-0091 l.141), and "control-pass rate did not predict blind certifiability" (l.172).
- **#8:** "~75% option "A"" (kb-0059 l.50); "12/19 A-keys" (kb-0120 l.56).
- **#9 (counter-example):** "the sealed rule had ignored those hits because the solver reported low confidence" (kb-0120 l.44). The opposite view is in kb-0100† l.38.
- **#34:** "stale solver results are not certification" (kb-0120 l.53).
- **#15:** escalating after one miss took accuracy from 64% to 41% (kb-0079† l.37).
- **#17/#24:** "Recompute, never self-report"; a "30-char substring "verbatim" check (defeated by paraphrase)" (kb-0072 l.95–96).
- **#1/#26:** feedback was "sometimes longer than the passage" (kb-0086 l.59); feedback longer than the instruction "has crossed into new instruction" (kb-0093 l.97).
- **#27:** "black text on a black background" (kb-0086 l.105); keyboard and assistive-technology access added as a requirement (kb-0081 l.128).
- **#28 (limit):** "Distinguish failures (block) from flags (review queue)" (kb-0118 l.247–248).
- **#41:** "65 of 76 bundles scored exactly 0" on non-repetition (kb-0083 l.64).
- **#45:** "published kill criterion" (kb-0080 l.209).
- **#46:** "Publish-time flattening created NEW defects" (kb-0120 l.54).
- **#47:** the student definition includes "test-wise students, and students willing to click through or guess" (kb-0092 l.26–27).
- **#48:** "A same-day lesson gate proves at most "I can do it now,"" (kb-0086 l.149).
- **#53 (open):** reviewers asked for "captions" (HOTBUCKET.md l.18), while kb-0027 l.47 says "Avoid redundancy."
- **#55 (open):** the nudge "can be skipped by clicking Next twice" (kb-0086 l.79).
