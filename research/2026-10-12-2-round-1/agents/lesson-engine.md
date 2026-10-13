# Round 1: the lesson engine

A read-only search agent, 2026-10-12 07:47 to 2026-10-12 07:58 UTC. Its brief and its final report, verbatim.

## Brief

Find rules and lessons in a lesson engine (it turns any text and question into checked lesson blocks; an AI judge checks every block and every student action) that hold for ANY lesson and ANY text, each with its exact evidence. Thoroughness: very thorough.

STRICT RULES: read-only. Do not create, edit, move or delete any file, and run no command that writes (no npm, no node scripts, no tests). Do not open .env files, key or token files, and never print a secret. Do not fetch URLs.

Sources (only these), all under ~/Projects/g9/transformer/:
- DECISIONS.md, README.md, v01/README.md, v01/QA.md, v02/README.md, v02/QA.md (results and what was found and fixed); v03–v11 README.md only to note planned ideas as open questions
- src/mechanics/util.js (the HOUSE writer prompt and the house checks every block gets), src/house.js (rules for every line a student reads)
- src/mechanics/*.js (each block's rules: when the answer is released, what is never marked, what a hint may say, what Jev must confirm), src/transform.js, src/blocks.js
- src/glue/*.js comments (rules brought over from the animated and 3D builds: marking contract, reply cleaners, release rule)
- src/quality/ (personas, playtest, calibrate) and test/*.test.mjs (test names and assertions encode rules)

We ALREADY HAVE these 14 (skip them unless you find new, stronger evidence or a counter-example): (1) an unsure judge is neither pass nor miss; (2) a choice question needs one answer the text settles, each option checked on its own; (3) wrong-answer feedback sends the student back without the answer and says only true things; (4) keep students' written words, a model's reading may choose a hint but not a grade; (5) check whether a student's words are aimed at the marker; (6) accept an unplanned right answer only when the judge is sure, and log it; (7) two tries then the answer; (8) cite words, not line numbers; (9) quote exactly, checked in code; (10) background at the line that needs it; (11) a picture should show what the voice says; (12) gate every check; (13) check machine output against something that does not assume the answer; (14) scripted readers play every lesson first.

Look especially for: rules about the tone and form of what a student reads (praise, exclamation marks, how many questions per reply), what a writer model may and may not decide, how a second block of the same kind must differ, slur guards on lines a student performs, what a hint may reveal, what the engine refuses to show and why, how a judge question must be shaped (bounded, evidence in its state), why a fast typed judge beats a second model for marking, how decisions are kept for replay and re-judging.

Return up to 15 NEW candidates, most important first. For each give:
1. statement: one plain sentence that holds for any lesson (no Othello terms, no people's names or job roles).
2. kind: "measured" (numbers from QA records), "adopted rule" (enforced in code or docs, and what made us adopt it), or "open question".
3. evidence: exact file path and line numbers or section heading, the code or sentence quoted exactly, and any number as written.
4. against: counter-evidence or limits stated in the same sources, quoted, or "none found".
Then a short list of borderline items left out and why. Exclude Othello-specific content, plumbing that teaches nothing about lessons, and anything you cannot cite. Keep the whole answer under 1,500 words.

## Report

Fifteen new candidates follow, most important first. All paths are under `~/Projects/g9/transformer/`. Every quote was checked against its line.

**1. A writer model drafts, before play, only the free text a block needs; every choice, mark, rank and check is a typed judgment, and every reply at play time is a pre-written line that a judgment selects.**
- kind: adopted rule (an audit found one exception, since fixed)
- evidence: `DECISIONS.md` L27–28 "A writer model only writes the free text that has to be written, and Jev picks among or checks what it writes". `v02/QA.md` L98–99 "an audit of every AI call found one judgment not on Jev … now a Jev choice among four authored steps". `src/glue/animated-judge.js` L4 "writes no reply of its own". `src/mechanics/debate.js` L2–3 "drafted in advance for each side, so no writer runs at play time".
- against: the writer still picks content that the judge only checks (`v02/QA.md` L82–83 "the writer picks the text's big idea and key words; Jev checks").

**2. Every line a student reads is cleaned in code: no praise, no "!" outside a quotation, no opening verdict, at most one question while a try remains, and none in a final line.**
- kind: adopted rule
- evidence: `src/house.js` L1–4 "no gushing; at most one question, none in a closing line … both builds show the verdict themselves". `test/glue.test.mjs` L6: "Great job! You found the line. Which word matters? And why?" becomes "You found the line. Which word matters?". `v02/QA.md` L66, fixed: "feedback opened with "This is correct;" under the build's own YES". `src/quality/playtest.js` L87 counts a shown "!" as an engine fault.
- against: `src/glue/threejs.js` L73 `if (!available) return text;`. Without the other build's mirror, the praise and question rules do not run.

**3. Nothing the student must work out is on screen before they answer: the key, feedback, evidence, gloss and model answer appear only after the attempt.**
- kind: adopted rule (after two faults)
- evidence: `src/glue/animated.js` L29 "Nothing a student needs to work out is on screen before they answer". `src/blocks.js` L127 "never the item, the checks or the reasons". `v02/QA.md` L63–64 "the word-in-focus card showed the meaning before the question; direct the line showed what the speaker wants before the pick".
- against: the animated export still carries the key in its data (`src/glue/animated.js` L76 `correct: it.answer`). The playtest guard checks field names only (`src/quality/playtest.js` L17 `FORBIDDEN`).

**4. Each judge question asks one bounded thing about named fields of its state, keeps the student's words in their own field, and states what evidence counts, using a test the statement can actually meet.**
- kind: adopted rule
- evidence: `README.md` L59 "one bounded yes-or-no question per remaining check, with the evidence in its state". `src/glue/threejs-archivist.js` L27 "the student's words are in their own field". `src/mechanics/open-check.js` L86 "a famous text's answer is known to anyone who knows the work", fixed in `v02/QA.md` L139–140 "(now: the question's own words only)". `src/mechanics/film-check.js` L84 "Is question_${k} answered by said_by_${k}?". `src/mechanics/video-essay.js` L123 "two readings pose a question, which is neither true nor false: there, nothing said may go against the passage".
- against: `v01/QA.md` L46 "their precision is not yet measured". Four-way choices are also used (`src/mechanics/cer-frame.js` L75).

**5. Marking with a fast typed judge instead of a second writing model is many times faster, and it gave no hard fail on another build's own answer table.**
- kind: measured
- evidence: `DECISIONS.md` L29–30 "(6.6 s through a second model) became a Jev choice of one next step (0.26 to 0.48 s live)". `v02/QA.md` L54–55 "43 answers, 0 hard fails, 1 soft miss. 31 reached the judge, median 266 ms, slowest 437 ms (its design note gives 1.7 s median for its Gemini endpoint)". L77–78 "median 261 ms".
- against: the 6.6 s was "including Jev's advisory check" (`v02/QA.md` L34). The 1.7 s comes from a design note, not a measurement. `v01/QA.md` L45 "One sample per judge question".

**6. Keep every judgment whole (state, questions, answers), so any block, play or session can be re-asked of a second judge, or replayed from the recorded verdicts without calling the judge.**
- kind: adopted rule (measured)
- evidence: `src/blocks.js` L93 "so the block can be re-judged through a second judge". `test/positive-evidence.test.mjs` L164 "replayable records". `src/quality/playtest.js` L158 "must match tick for tick and never ask the judge". `v02/QA.md` L24 "8 ticks, 0 differences".
- against: `src/quality/calibrate.js` L137–138 says incomplete records "are counted, not replayed". Agreement with a second judge is "the cheapest signal" (L132), not accuracy.

**7. A hint says where to look but withholds what the task asks the student to produce; a nearly-right quotation is told it is near, without being given the text's wording.**
- kind: adopted rule
- evidence: `src/mechanics/open-check.js` L63–64 "a hint may quote the text, even the line to read … but it uses no leak word and copies no four-word run of the reveal". `src/mechanics/evidence-hunt.js` L28, where the line is the answer: "without quoting the line". `src/glue/animated-judge.js` L8 ""Nearly…", without the wording".
- against: `src/glue/threejs-archivist.js` L52 gives the wording in the final reply ("The text has it as"). `src/mechanics/key-words.js` L121 gives the answer's first letter as a hint.

**8. A student is never asked to perform a line containing a slur: a block ships only when the judge positively confirms the line is clean, though a gloss may name an epithet as an insult.**
- kind: adopted rule
- evidence: `src/mechanics/util.js` L105–107 "so a block ships only on positive evidence that the line is clean … a student is never asked to perform one". `test/laws.test.mjs` L153.
- against: `src/glue/threejs.js` L79 "Without the mirror there is none, and the Jev question carries the guard". Yet that question (`cleanLine(`) is asked only in direct-the-line, word-in-focus and worked-model. Say-it-back, whose sentence the student says back, has no guard at all.

**9. A second block of the same kind in one lesson must be built on a different point: the writer is told what earlier blocks cover, and code holds back a repeat.**
- kind: adopted rule
- evidence: `src/mechanics/util.js` L82–83 "a second block of a kind on the same text is not about what an earlier one was". L141 "do not repeat or reword those". `v02/QA.md` L64–65 "QC-2 was a copy of QC-1".
- against: the repeat test only compares words (`util.js` L49 "most of its words shared", at 0.6), so a reworded repeat passes. Some kinds allow only one block per lesson (`src/glue/animated.js` L101).

**10. Only a block made under today's rules is shown: the rules' version is part of its key, so changing a prompt or check remakes every block it affects.**
- kind: adopted rule (after a measured fault)
- evidence: `src/blocks.js` L17 "so an old block is made again, not served". `v02/QA.md` L193–194 "a playtest sent the saved link's first six blocks, all made before the line-number rule, and played them; three cited line numbers". `test/server.test.mjs` L100.
- against: the version is bumped by hand (`README.md` L99–100).

**11. An optional part the judge does not confirm is left out, rather than holding back the whole block.**
- kind: adopted rule
- evidence: `v02/QA.md` L141–142 "word classes are shown only where Jev confirmed them". `src/mechanics/video-essay.js` L146 "a painting Jev did not find fitting is left out of the frame (the claims stay)". `src/mechanics/glossary.js` L130–131 a word the reader already knows "is dropped, unless that would leave nothing".
- against: `src/mechanics/glossary.js` L121 shows another build's notes even if unconfirmed: "Jev's reading of them is kept, and never holds them".

**12. Mark meaning, not wording: any wording counts, a short answer that says it is enough, and an answer is called off task only when the judge is sure and nothing in it was met.**
- kind: adopted rule
- evidence: `src/mechanics/open-check.js` L14 "a short answer that says it is enough"; L100 "Any wording counts". `test/animated-judge.test.mjs` L53 "off task only on a confident no, and never with a criterion met". `v02/QA.md` L57 "a criterion met on an earlier try still counts".
- against: `v02/QA.md` L55–56, one answer "came back not met where the table wants partial". The two builds differ on earlier tries: `animated-judge.js` L83 "together with earlier_answers" versus `threejs-archivist.js` L130 "on its own".

**13. A judged check should hold back a block or steer a student only after person-labelled cases show it is right, and advisory checks need the same.**
- kind: adopted rule (the harness exists; not yet met)
- evidence: `src/quality/calibrate.js` L6 "a model-made label measures nothing". L105 "should not hold a block or decide what a student is told". L79–80 "an advisory check still changes what a student is told".
- against: `README.md` L111 "Calibration has seed sets only: it proves the wiring and measures nothing".

**14. Teach and gloss the words that carry the knowledge a reader needs, not the rarest ones, each glossed for its sense in its own line.**
- kind: adopted rule
- evidence: `src/mechanics/word-in-focus.js` L17 "Chosen by knowledge carried, not by difficulty". `v02/QA.md` L83–85 "key words were hard words from the text … and Jev held it". `src/mechanics/glossary.js` L3–4 "each one required, since a wrong gloss … misleads quietly".
- against: the check on whether a reader needs a word is advisory only (`src/mechanics/glossary.js` L126 `required: false`).

**15. A reader who stalls or keeps guessing should be nudged or released; nothing does this yet.**
- kind: open question
- evidence: `src/quality/playtest.js` L156 "nothing nudges a reader who is stuck"; L8 "no way out for a guesser". `v02/QA.md` L135 "no idle nudge, v05". `v05/README.md` L5–6 "never adapt on fewer than three observations".
- against: guessers still finish (`test/quality.test.mjs` L35).

**Counter-examples to the 14 you already have**
- (1): the animated build's word web counts a word the judge is unsure of (`src/glue/animated-judge.js` L99–100 "an unsure word goes in"), while our own web keeps it pending.
- (7): choice blocks never release the answer (`src/mechanics/quick-check.js` L90 `done: correct`). The playtest records this as "no attempt ceiling and no reveal" (L153). The 3D build counted a given answer as passed; the glue now records it as given, "never marked Accepted" (`src/glue/threejs-render.js` L369).

**Borderline, left out**
- At most one judge request per student action (`v02/README.md` L18–19): mostly plumbing.
- Correction notes say exactly what to change (`v02/QA.md` L140, L191): partly covered by (1).
- Student text never uses build terms such as "beat", "cue", "caption" or "frame" (`src/mechanics/util.js` L111–113): an extension of (8).
- Ask each question right after the text that answers it (`src/glue/threejs-render.js` L45): close to (10); the judging half is in candidate 4.
- Spelling counts only where the word itself is being taught (`key-words.js` L3–4 versus `say-it-back.js` L3–4): narrow.
- No length or order clue gives the answer away (`quick-check.js` L55, `key-words.js` L100): close to (2).
- Interpretive answers are released as "one way to see it" (`open-check.js` L108): wording only.
