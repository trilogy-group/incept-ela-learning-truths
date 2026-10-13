# Round 1: the reading engine

A read-only search agent, 2026-10-12 07:47 to 2026-10-12 08:00 UTC. Its brief and its final report, verbatim.

## Brief

Find lessons learned in a Grade 3 reading game engine and its project that hold BEYOND Grade 3 and beyond reading, for any lesson and any text, each with its exact evidence. Thoroughness: very thorough.

STRICT RULES: read-only. Do not create, edit, move or delete any file, and run no command that writes (no npm, no node, no tests). Do not open any .env file (one exists at ~/Projects/grade3-reading/knowledge_bot/.env: never open it), key or token files, and never print a secret. Do not fetch URLs.

Source: ~/Projects/grade3-reading/ only. Start with its README files and any docs/, research, QA, eval, findings, decisions or notes folders; then engine/src/decide/ (support gates, option-order rotation, sampling, replay, logs), the engine's game loop (look for addresses_grader), its personas or playtest code, and any evaluation results with numbers. Skip node_modules, build output, media and data dumps.

We ALREADY HAVE these 14 (skip them unless you find new, stronger evidence or a counter-example): (1) an unsure judge is neither pass nor miss; (2) a choice question needs one answer the text settles, each option checked on its own; (3) wrong-answer feedback sends the student back without the answer and says only true things; (4) keep students' written words, a model's reading may choose a hint but not a grade; (5) check whether a student's words are aimed at the marker; (6) accept an unplanned right answer only when the judge is sure, and log it; (7) two tries then the answer; (8) cite words, not line numbers; (9) quote exactly, checked in code; (10) background at the line that needs it; (11) a picture should show what the voice says; (12) gate every check; (13) check machine output against something that does not assume the answer; (14) scripted readers (strong, guesser, stuck, adversarial) play every lesson first.

Look especially for: how an AI judge's answers shift with option order and what was done about it; how many samples a judgment needs; how support gates were chosen and whether they are calibrated; what replaying recorded decisions shows; what personas found; any measured learning results (engagement, accuracy, timing) and any learning-science principles the project adopted with their sources.

Return up to 15 NEW candidates, most important first. For each give:
1. statement: one plain sentence that holds for any lesson (no Grade 3 or reading-only terms, no people's names or job roles).
2. kind: "measured" (numbers from the project's own records), "adopted rule" (enforced in code or docs, and what made it), "external research" (a cited study, DOI/URL as written), or "open question".
3. evidence: exact file path and line numbers or section heading, the code or sentence quoted exactly, numbers as written.
4. against: counter-evidence or limits in the same sources, quoted, or "none found".
Then a short list of borderline items left out and why. Keep the whole answer under 1,500 words.

## Report

I found 15 new candidates, most important first. Three things to know before reading them:

- **No real-learner results exist.** The project never measured learning gains, engagement or timing with real students. The only real-student numbers are accuracy on the course it set out to improve (item 6).
- **"My tally" numbers are mine.** I counted them from `~/Projects/grade3-reading/engine/runs/*/decisions.jsonl`; the project never reports them.
- **"EVIDENCE"** means `~/Projects/grade3-reading/engine/EVIDENCE-2026-09-22.md`.

**1. Have a model from a different family than the writer answer each question with the source hidden; if it still finds the key, the question does not test the source.**
- Kind: measured.
- Evidence:
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd:54` "IB passed all 11; the different-family blind solve failed 4."
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd:68-69` "only **20 (21%) survived**; **75 leaked** under the strong solver. Of 3,146 un-gated existing candidates, only 187 (5.9%) survived"
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd:70` "ban same-family certification"
- Against:
  - kb-0070:9: four items were "attempted-but-missed … world-knowledge tempts but the key needs the text".
  - kb-0235:37-38: "the root cause is passage design (encyclopedic passages)".
  - The engine's fallback breaks the rule: writer, judge and student all default to `"gemini-3.5-flash"` (`~/Projects/grade3-reading/engine/src/goal/derive.js:7`, `~/Projects/grade3-reading/engine/src/decide/providers/gemini.js:14`, `~/Projects/grade3-reading/engine/src/persona/llm.js:8`).

**2. Show the judge exactly what the learner sees (the text, the options, the whole task), or don't ask.**
- Kind: measured.
- Evidence:
  - `~/Projects/grade3-reading/engine/skills/jev-verify/SKILL.md:16` "Every failure this engine has had was a judge asked to rule with the evidence missing"
  - EVIDENCE:344-345 "fired on **77 of 78** items (99%)"
  - EVIDENCE:279-280 "held back 8 of 12 lessons … at p=0.27–0.38"
  - EVIDENCE:252-253 "dropped the unanswerable class from 10 to 6"
- Against: after the fix that check still fired on 41% (EVIDENCE:350-351).

**3. Use the AI judge to sort what fixed checks found, not to hunt for faults itself, and never let one judgment block.**
- Kind: measured.
- Evidence:
  - `~/Projects/grade3-reading/engine/skills/jev-triage/SKILL.md:16` "the judge flagged 47% of items nobody had ever complained about, and every fix worth making came from deterministic checks instead"
  - `~/Projects/grade3-reading/engine/src/course/checks.js:63` "Major, never a blocker: at our measured precision a single judgment must not hold a lesson back"
- Against: `~/Projects/grade3-reading/engine/skills/lesson-qc/SKILL.md:58-60` — it "ruled 790 of them in seconds and … called zero of them unknown" against a 1,081-word known list.

**4. Treat confidence thresholds as placeholders until the judge is scored on fixed labelled sets: planted faults for recall, never-flagged items for false alarms. Compare runs only like for like.**
- Kind: adopted rule. It was made after a first run had a 0.986 false-positive rate.
- Evidence:
  - `~/Projects/grade3-reading/engine/src/decide/questions.js:5` `{ confidence: 0.55, top: 0.6, margin: 0.15 }`, and :105 "not calibrated correctness"
  - `~/Projects/grade3-reading/engine/BRAINSTORM-2026-09-22-lesson-compiler.md:88` "Engineering rules lifted from Passage"
  - EVIDENCE:341-342 "makes the recall meaningless"
  - `~/Projects/grade3-reading/artifacts/spine-solve-calibration-2026-07-10/REPORT.md:126` "The delta is confounded and must not be called lift."
- Against: the engine's own 0.986 → 0.471 comparison changed the test set. `~/Projects/grade3-reading/engine/runs/calibration/calibration.json` has 47 findings and 70 negatives; `~/Projects/grade3-reading/engine/runs/calibration2/calibration.json` has 37 and 51, from the same 19 registers.

**5. A passed quality gate shows a lesson is well-formed, not that anyone learned; pair every completion claim with accuracy on new items.**
- Kind: adopted rule, never tested.
- Evidence:
  - kb-0069:34 "The gate certifies FORM, not OUTCOME, by construction."
  - `~/Projects/grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md:139` "completion-up is INSUFFICIENT"
  - `~/Projects/grade3-reading/engine/README.md:107` "passing tests proves plumbing, not learning."
- Against: `~/Projects/grade3-reading/NORTH_STAR.md:51-52` "MAP is NOT in TimeBack for our cohort (0/313 overlap)… OBSERVE-ONLY".

**6. Report learner accuracy per skill, on items that need the source; an average over easy items hides where learners fail.**
- Kind: measured.
- Evidence:
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd:40` "compare/contrast 39%, cause/effect 42%, sequence 48% — vs an 83% blended average… only **~17% of the cohort clears 90%**"
  - NORTH_STAR.md:55 "wrong instrument"
- Against: same line, "true baseline unknown". I found no re-measurement.

**7. Choose the number of samples by first showing it can tell a real effect from chance, and read agreement between samples as consistency, not correctness.**
- Kind: adopted rule. Four views proved too few, so it went to eight.
- Evidence:
  - `~/Projects/grade3-reading/.agent/LESSONS_LEARNED.md:141` "use eight views per blind condition and prove the detection threshold in a unit test"
  - spine-solve REPORT.md:29 "8 for order/selection-sensitive formats; 3 samples… for single-answer formats"
  - `~/Projects/grade3-reading/artifacts/semantic-judge-calibration-2026-07-10/JUDGE-CALIBRATION-REPORT.md:55` a FALSE FLAG at agreement 1.00, and :124 "self-consistency, not cross-family consensus"
  - My tally: all 222 of Jev's split two-sample answers failed the gates; for the LLM fallback, 34 of 200 passed.
- Against:
  - `~/Projects/grade3-reading/engine/bin/engine.mjs:51` defaults to `opt.samples ?? 1`.
  - Standalone play logs ran one sample (e.g. `~/Projects/grade3-reading/engine/runs/live-playtest-L4`, 175 records).
  - `passes()` (questions.js:106-116) never reads `agreement`.

**8. When a judge picks among options, rotate their order across samples and average, and check that more than one sample actually runs.**
- Kind: adopted rule, from the vendor's warning (BRAINSTORM:143 "option-order sensitive").
- Evidence: questions.js:118 "option order shifts answers; rotate and average".
- Against:
  - questions.js:120 `if (q.type !== "choice" || sample === 0) return q;` means a one-sample run never rotates.
  - The project never tested the effect itself. My tally: rotated choices split in 7 of 265 cases (2.6%), unrotated yes/no questions in 183 of 9,243 (2.0%), so no order effect is visible.

**9. Spread right-answer positions evenly across a set and check the spread in code; always picking the first option must not pass.**
- Kind: measured, plus external research.
- Evidence:
  - `~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D5-D6-D11-D13.md:37` "29 of 40 MCQs (72.5%) have the correct answer at position 0", and :41 "would pass 86–90% of items without comprehension work"
  - `~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/RESPONSE-MATRIX.md:21` "56% Choice A; now distributed A30/B29/C29/D29 across 117 MCQs"
  - `~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md:2234` "Attali, Y., & Bar-Hillel, M. (2003). Guess where…" (no DOI given)
- Against:
  - SIM-REVIEW:41 "blind-solve passes do not test key-position bias"
  - `~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md:65-66` "grade-4 was missed once"

**10. Ask the judge one yes/no question per candidate and combine the answers in code; any choice that remains needs a "none of these" option.**
- Kind: adopted rule. It was made after three failures: binding goals to passages, picking taught words, and picking moments to illustrate.
- Evidence:
  - EVIDENCE:221-222 "A wide choice is where this engine keeps failing"
  - `~/Projects/grade3-reading/engine/src/goal/from-text.js:66` "A twelve-way choice spread its mass and returned nothing at all."
  - `~/Projects/grade3-reading/engine/src/goal/hunt.js:50` "silence beats a line that does not fit"
- Against: hunt.js:43,46 still uses a wide choice (up to 12 lines plus `none`) to pick coach lines.

**11. Machine stand-ins for learners show a lesson runs, not that it teaches, because a model cannot hide what it knows.** (This is a limit on your 14.)
- Kind: external research, plus measured.
- Evidence:
  - `~/Projects/grade3-reading/ti-courseplans/courses/g5-reading/reference/[name]-llm-prediction-not-simulation.md:64` "LLMs cannot suppress pre-trained knowledge… too articulate, too compliant", and :209 https://doi.org/10.1145/3657604
  - `~/Projects/grade3-reading/engine/src/goal/lesson-personas.js:8`: the scripted perfect student's retell is a fixed flying story, yet `~/Projects/grade3-reading/engine/runs/unit2-playtest/playtest.json` reports, on the non-fiction lessons, "a perfect student could not satisfy the closing judgment"
  - EVIDENCE:130 "silently substituted the scripted persona"
- Against: EVIDENCE:20-21 shows play runs found real bugs ("unbounded probe loop").

**12. Log every judgment's full input so it can be re-run through a second judge; where two judges agree against the answer key, review the key.**
- Kind: measured.
- Evidence:
  - `~/Projects/grade3-reading/engine/runs/jev-replay-L4/summary.json`: agreement 0.946; `evidence_supports` 0.75 (n 8); every other question 1
  - EVIDENCE:43 "our key includes two non-descriptive fragments"
- Against:
  - EVIDENCE:75 "0.97 as a fragment under one wording and 0.035 as a whole sentence"
  - `~/Projects/grade3-reading/engine/src/replay/replay.js:5-10`: `agree()` ignores the gates, and 4 of 37 Jev answers were below them (`~/Projects/grade3-reading/engine/runs/jev-replay-L4/replay.csv` lines 2, 8, 10, 35)

**13. Never adapt to a learner on fewer than three observations.**
- Kind: adopted rule. A live run showed the first version "adapted off one tap" (EVIDENCE:101).
- Evidence: `~/Projects/grade3-reading/engine/src/goal/lesson.js:39` "thin evidence is not evidence".
- Against: three is not calibrated. In `~/Projects/grade3-reading/engine/runs/unit2-playtest-llm/playtest.json`, one reader had 7 hits and 10 misses yet had all four claims accepted.

**14. A check that has never fired proves nothing until it catches a planted fault.**
- Kind: adopted rule.
- Evidence:
  - EVIDENCE:356-357 "fired zero times in 135 asks… decoration"
  - GOAL_grade3_hootl_convergence_2026_06_15.md:113 "validated as leakage-stopped not probe-stopped-biting"
- Against: none found.

**15. Order each lesson: prepare knowledge, meet the source, watch a modelled step, guided practice, learner explains, evidence check, then delayed and varied transfer.**
- Kind: external research, plus adopted rule.
- Evidence:
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd:67` lays out this flow
  - lesson.js:41 "I do, then you try"
  - `~/Projects/grade3-reading/artifacts/g9-prep-pack-2026-10-02/03-research/MANIFEST.md:20` Rosenshine (2012) https://www.aft.org/sites/default/files/periodicals/Rosenshine.pdf, and :37 Kalyuga et al. (2003)
- Against:
  - kb-0099:9 "design-stress evidence, not live child outcome proof"
  - The engine's transfer item comes right after the claim, not later (hunt.js:115).

**Borderline, left out**
- **Only verified files are served** (`~/Projects/grade3-reading/engine/src/course/serve-bundle.js:1-2`): good engineering, but not a lesson rule.
- **The learner's screen never receives keys or rubrics** (`~/Projects/grade3-reading/engine/src/server/view.js:5`): close to your 3 and 12.
- **Limits on the system's own retry loops** (`~/Projects/grade3-reading/engine/src/engine/loop.js:16-17`): a variant of your 7.
- **No repeated coach line back to back** (EVIDENCE:72-73): minor.
- **Confidence demanded by stakes** (`~/Projects/grade3-reading/engine/skills/jev/SKILL.md:68`): vendor advice that was never applied.
- **New evidence for your 8:** `~/Projects/grade3-reading/artifacts/g9-prep-pack-2026-10-02/INDEX.md:22` notes that "line 45" is Folger's numbering, and Open Source Shakespeare numbers the same line 43.
