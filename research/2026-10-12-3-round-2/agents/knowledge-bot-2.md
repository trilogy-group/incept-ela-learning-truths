# Round 2: the knowledge bot, second half

A read-only search agent, 2026-10-12 08:21 to 2026-10-12 08:44 UTC. Its brief and its final report, verbatim.

## Brief

Find lessons learned that hold for ANY lesson, course or set of learning materials, whatever the subject, grade or text, each with its exact evidence. Thoroughness: very thorough. The source is a knowledge store kept for a Grade 3 (and Grade 5) reading course build: each entry under knowledge/ summarises one source (course-build retrospectives, reviews, learning-science notes and BrainLifts on practice, direct instruction, curriculum and knowledge, feedback documents, evaluation reports).

STRICT RULES: read-only. Do not create, edit, move or delete files; run no command that writes; no network fetches; do not run the bot or any script. Never open any .env file (one exists in ~/Projects/grade3-reading/knowledge_bot/), key or token files, and never print a secret.

Sources (only these), under ~/Projects/grade3-reading/knowledge_bot/:
- knowledge/kb-0126 … kb-0251 (use INDEX.md to choose: lesson and course design, assessment and question quality, learning science and its sources, review feedback and what reviewers found, evaluation of courses or items, AI generation or judging of learning content; skip vendor or platform notes and tooling)
- handoffs/, pr-proposals/, skills/ and templates/ (skim for rules about making or checking learning content)
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

**New candidates, most important first** (all paths under `~/Projects/grade3-reading/knowledge_bot/`, written in full; L = file line)

**1. If practice questions use plausible wrong options, each one needs corrective feedback; without it, learners later recall the wrong options as true.**
- Kind: external research, adopted as an obligation.
- Evidence:
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd` L54: "Butler & Roediger (2008) showed that feedback largely neutralises this risk, while the absence of feedback leaves it unchecked."
  - Citation as written, with no DOI or URL: `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0160-multiple-choice-questions-evidence-base.qmd` L117, "Feedback enhances the positive effects and reduces the negative effects of multiple-choice testing."
  - Adopted: `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd` L95-96: "potent misconception-based distractors require product-appropriate corrective feedback or post-test correction because plausible lures can seed false knowledge"
- Against: kb-0160 (same path) L123: "Lab setting. Feedback was simple (correct answer shown)."

**2. When repeated attempts stop improving, switch to re-teaching and recheck on fresh parallel items; passing by persistence is not mastery.**
- Kind: external doctrine adopted as an obligation; never measured here. It partly answers #55.
- Evidence:
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd` L63: "The system needs three outcomes, not two: promote, keep practising, or switch to corrective instruction." and L90: "If learners can eventually pass by repeatedly sampling similar items, the gate is measuring persistence (or luck) rather than acquisition mastery."
  - `~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl` L48: "repeated non-progress must trigger an explicit escalation rather than endless retries."
  - `~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md` L56: "(≥2, zero shared items) are required for three-state retry"
- Against: `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd` L43: "neither the exact count nor an exception policy was finalized."

**3. Model one new procedure per lesson by thinking it aloud, including what was rejected and why, then have learners use the same named steps in guided and independent work.**
- Kind: adopted rule, checked in code. One measured defect.
- Evidence:
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd` L31-32: "the I-do must model thinking — why this detail and not that one, what was rejected and why — never just reveal a filled-in organiser" and L35-36: "I-do, we-do and you-do must run the same skill, never switch mid-lesson."
  - `~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md` L17: "every non-review atom carries exactly the lesson's one `operation_id`."
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd` L55: "MAJOR — we-do renames three of the four I-do step labels (R-KC-11)."
- Against: `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd` L65: "NO-GO stands; semantic lints remain advisory." (The quality of a think-aloud cannot yet be judged by machine.)

**4. Anything taught needs at least one graded task where the learner must produce it; picking it out from options is not evidence it was learned.**
- Kind: measured incident, then adopted rule.
- Evidence:
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd` L134-136: "Taught word never cashed in L6/L7 — merciless/triumphant were acquired but no graded surface required using them" and L143-144: "MCQ recognition alone — however many options — never counts as a cash point"
  - `~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md` L64: "Do not certify productive or integrative knowledge with recognition alone."
- Against: kb-0160 L129: "MC practice tests showed a larger effect size (g = +0.70) than short-answer tests (g = +0.48)"

**5. Every screen, and every stretch of video, needs a required response that serves the teaching.**
- Kind: adopted rule plus external research.
- Evidence:
  - kb-0172 L27: "students should do something on every screen: passive listening or text-only screens invite click-through rather than attention."
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd` L211-213: "Interpolated memory tests inserted into recorded lectures cut mind-wandering by roughly a third and improved recall versus uninterrupted video." Source URL as written: https://www.pnas.org/doi/pdf/10.1073/pnas.1221764110
- Against:
  - kb-0172 L27: "a decorative tap control does not satisfy the concern"
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd` L119-120: "sync checks becoming compliance checks... too much with texts that are too short"

**6. A lesson may assume, and a check may test, only what earlier lessons taught or what every learner can safely be assumed to know, and this can be checked mechanically.**
- Kind: adopted rule, checked in code. Extends #20.
- Evidence:
  - op-lint README (path above) L16: "`lesson.assumes` is a subset of the union of prior lessons' `adds`, in unit order."
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd` L74: "Taught word "betrayal" never appears in the L1 passage" and L75-76: "yet p23/p27b/p28 assess the child on "betrayal.""
- Against: op-lint README L67-69: "no cross-unit baseline exists in the contract, so a unit's first lesson must have empty `assumes`"

**7. Never teach anything false: anything presented as coming from the source must be in it, taught facts are checked against a reference, and simplified models are labelled as simplifications.**
- Kind: measured plus adopted rule. Extends #17 to claims that aren't quoted.
- Evidence:
  - kb-0232 L41: "fabricated claim printed as textual fact"
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd` L78-79: "the shape that hides the worst defects, since unquoted claims look like nothing"
  - kb-0213 L65-66: "merciless and stranger are the two teaching a flatly wrong rule on screen."
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0141-cross-cutting-science-misconception-synthesis.qmd` L140: "Every model should carry an explicit health warning"
- Against: kb-0234 L73: "not referenced by `npm run check` or any other known gate"

**8. The right option must not be findable without the knowledge: no clue from length, shortness, odd-one-out or echoing the question, and a learner who knows should be able to answer with the options covered.**
- Kind: adopted rule enforced in code, plus external research.
- Evidence:
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd` L63-64: "The right option must not be the longest, the shortest, the odd one out, or the one that reuses the most words from the stem."
  - kb-0159 L103: "re-read the stem with options covered. If you cannot answer from the stem alone, revise the stem."
  - kb-0160 L78 (Downing 2005, no DOI): "47% of students passed flawed items vs. 53% passing standard items"
- Against: kb-0160 L80: "Medical education context. Small sample of four exams from one institution."

**9. Check that each item needs the skill it is labelled with: an "inference" item whose answer the source states outright is recall, and only new material makes an item higher-order.**
- Kind: measured, plus external research.
- Evidence:
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd` L84 (items probed / clean / answer stated / not applicable): "| **Total** | **18** | **16** | **1** | **1** |"; L96-98: "The item framed itself as inference while handing the child the two exact adjectives the very next sentence states outright"
  - kb-0159 L58: "no new material, no higher-order thinking."
- Against: kb-0160 L149: "Practical guidance paper, not a systematic empirical study."

**10. The maker cannot certify its own work: checks must come from a different author or model family, and a generator must not be judged only by the score it was tuned on.**
- Kind: measured plus adopted rule. Related to #35 and #43.
- Evidence:
  - item-quality.md L64-66: "an InceptBench judge that runs on the same Gemini as the generator passed answer-leaking items 1.0"; L69: "a same-family-IB-passed bank that is 36% leaky"
  - `~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd` L115-116: "IB score: 1.0. Blind-solve rate: 100%."
  - assessment-item-agent.md L65: "Do not use the authoring model as its own certifier."
- Against: `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd` L398: "different LLMs converge on a shared difficulty ranking that diverges from human rankings"

**11. Re-check every reported fault against the actual material before fixing it, and suspect the checker first when it flags many items.**
- Kind: measured. This is the converse of #38.
- Evidence:
  - kb-0213 L141-142: "the probe is often the bug (4 of 5 listen findings that day were probe-classes, not real defects)"
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd` L85: "flagged 31 of 123 clips "WEAK ATTACK," all false"
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd` L144-145: "98.6% false-positive rate"
- Against: kb-0245 L34-35: "26 of [name]'s findings landed on lessons the calibration log marked green at review time"

**12. Close a defect by its class, with a check of what the learner experiences run on every lesson, and count how many classes recur rather than how many items were closed.**
- Kind: measured.
- Evidence: `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd`
  - L18: "39 checks were added in 5 weeks (7-10 a week)"
  - L20: "silent/missing-audio class has seven separate commits"
  - L50: "Every round report counts NEW defect classes vs REPEAT classes."
- Against: kb-0234 L83-85: "QUESTION HOME, was specified but is explicitly NOT shipped/wired"

**13. Give each term one definition used everywhere; when material revisits a topic taught elsewhere, reinforce that framing rather than redefine it.**
- Kind: adopted rule enforced in code, plus a measured scan.
- Evidence:
  - kb-0181 L39-40: "choose the best definition and make sure your LLM uses the same one throughout"
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd` L34: "Reinforce, do not redefine"
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd` L67: "Result: 0 live contradictions"
- Against: kb-0159 L132: "sometimes testing whether students can transfer across surface variation is the point"

**14. Fade guidance across lessons as learners gain expertise.**
- Kind: external research (no DOI given), adopted in a design spec; not implemented in this build.
- Evidence: `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd` L284: "The expertise reversal effect (Kalyuga et al.): heavy guidance helps novices but slows down learners who already know the material."
- Against:
  - kb-0180 L42-43: "G3 Peter Pan never got past one lesson per scaffold level, so this stayed unimplemented"
  - kb-0204 L306: "guided practice grows again"

**15. Rules given to a generating model steer it but don't reliably control it, and compliance differs sharply between models, so re-test its output after any model change.**
- Kind: measured, plus external research.
- Evidence:
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd` L50: "OpenAI 60/140 and 0/20 robust clusters, Claude 67/140 and 0/20, DeepSeek 136/140 and 17/20; worst route 0/20 against 20/20."
  - `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd` L73-74: "constraint adherence fell materially as instruction difficulty increased"; URL as written: https://aclanthology.org/2026.findings-acl.99/
- Against: kb-0168 L70-71: "found the assigned taxonomy or ontology facet in 119/120 treatment outputs"

**Borderline items left out**
- **"Not checked" is its own state.** item-quality.md L63: "NEEDS_LLM_GRADE (the blind solve not run) is a FAIL, not a pass". Left out because it is close to #9 and #28.
- **A 90% pass mark is a convention, not a definition of mastery.** kb-0156 L59 (Zhang et al., https://doi.org/10.5281/zenodo.15870292). It overlaps #15 and #48, and conflicts with `~/Projects/grade3-reading/knowledge_bot/skills/timeback-app-state/SKILL.md` L357: "Enforce mastery gates at ≥90% accuracy".
- **Keep the question and steps on screen** (`~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd` L84). Close to #26.
- **Teach with example/non-example pairs that differ in one feature** (kb-0181 L33). The only evidence is from vocabulary.
- **Build units as concept-coherent sets** (Cervetti 2016, DOI 10.1007/s11145-016-9628-x, in `~/Projects/grade3-reading/knowledge_bot/skills/reading-science/sources.qmd` L17). One study, and its comprehension-question measure was null.
- **Don't teach shortcuts that often fail** (kb-0136 L70-73). Reading-only examples.
- **Messages must be true of what the learner actually did** (`~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd` L70-71). Found in one build only.
- **Check the assembled set for items that cue each other** (kb-0159 L81). Overlaps #3 and #41.
- **Analyse items after release using real responses.** Never possible here: kb-0245 L45 says "no server-side learner state" exists.
- **Generate from a real source passage.** Contradicted: `~/Projects/grade3-reading/knowledge_bot/handoffs/g5-reading-generator-output-spec.md` L74 versus item-quality.md L40, "refuted".
- **Mentor-style on-screen guide** (Baylor & Kim). Its DOI is flagged as malformed (`~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0202-g9-othello-video-research-fake-ai-attention.qmd` L32).
- **Caution on generalising reviewer rulings:** `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0186-scope-lane-and-model-routing-rules.qmd` L46: "never carried across courses".

**Evidence bearing on the 55**
- **#4 (counter-example):** kb-0183 L135: "a single-select (`mcq`) item is *never* revealed after N tries". `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0224-g3-dialogue-branches-pace-gate-roll-forward-2026-09-22-23.qmd` L87 records this as "logged as a contradiction awaiting the author's ruling".
- **#1 (tension):** kb-0159 L176: "The minimum effective feedback is showing the correct answer."
- **#15 (stronger):** kb-0159 L62: "A 5-item quiz is useful for retrieval practice but too unreliable for mastery decisions."
- **#2 (limit):** `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd` L58 keeps one voice per role: "keeping the two voices distinct".
- **#5:** LLM_SPEC.qmd L29: "MCQ 99.5%, MSQ 100%". `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0126-claude-takeover-audit-2026-07-13.qmd` L29: "low solver confidence had hidden those hits" (also bears on #9 and #35).
- **#24:** `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0206-memory-digest-feedback-rules.qmd` L207: "Zero derived claims were wrong."
- **#30:** kb-0196 L146: "shown a bare stem with no passage/options".
- **#34 (remedy):** kb-0238 L37-40: "caching identical resubmits to return the same verdict instantly".
- **#37:** `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0165-eppc-g3-reviewer-qualification-terminal-outcomes-human-next-gate.qmd` L113: "Familiarity with the project is not automatic qualification".
- **#38:** kb-0196 L150: "JUDGE-GRADE had fired zero times".
- **#39:** kb-0159 L85: "suggests the keyed answer is wrong or ambiguous".
- **#46:** `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0216-codex-visual-audit-2026-09-07.qmd` L44: "desktop-only".
- **#50:** `~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd` L9: "a definition edit leaves the clip silently stale".
- **#51/#52:** kb-0202 L37-39: "Still AI faces are now indistinguishable from real ones" and "no reliable learning loss, but a real engagement and comfort loss".
- **#53:** kb-0182 L129: "nothing may be spoken that is not printed".

**Files with people's names** (not used as evidence): kb-0177, kb-0178, kb-0212, kb-0214, kb-0246, kb-0247, kb-0250, `[name]-g5-generator-execution-plan.md`, `README_FOR_[name].md`, and the `knowledge-[name]-additions/` folder. The points they make that bear on this list are also in other files: kb-0212's sibling-defect audit matches kb-0201 (#12), kb-0178's "two meanings" matches kb-0183 L157 (#13), and kb-0246's point about checks from the same source matches kb-0201 L28 (#10).
