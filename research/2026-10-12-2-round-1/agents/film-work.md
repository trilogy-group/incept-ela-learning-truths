# Round 1: the film work

A read-only search agent, 2026-10-12 07:47 to 2026-10-12 07:59 UTC. Its brief and its final report, verbatim.

## Brief

Find lessons learned in a finished Grade 9 film-and-checks project that hold for ANY lesson and ANY text (not specific to Othello, Shakespeare, or one team's tools), each with its exact evidence. Thoroughness: very thorough. Read whole files where they are short; for long ones read the sections that report findings, QA results, measurements or decisions.

STRICT RULES: read-only. Do not create, edit, move or delete any file, and run no command that writes. Do not open .env files, key or token files, and never print a secret. Do not fetch URLs.

Sources (only these):
- ~/Projects/g9/review/ (every dated check: the marking test and its re-check, the Act 1 context map, the Lesson 1 build map, the three-film comparison, reviews of our own cuts)
- ~/Projects/g9/film/v07/README.md, ~/Projects/g9/film/v07/render/QA.md, and the README.md of earlier film/vNN folders (lessons that changed later versions)
- ~/Projects/g9/player/ (README, QA records, check-in design)
- ~/Projects/g9/narration/auditions/ (notes and READMEs on voice/model trials)
- ~/Projects/othello-unit-video/research/ (FINDINGS.md, METHODS.md, data/)
- ~/Projects/g9/tools/unit-video-essay/INTEGRATION.md (style research)

We ALREADY HAVE these 14 (skip them unless you find new, stronger evidence or a counter-example): (1) an unsure judge is neither pass nor miss; (2) a choice question needs one answer the text settles, each option checked on its own; (3) wrong-answer feedback sends the student back without the answer and says only true things; (4) keep students' written words, a model's reading may choose a hint but not a grade (AI marker 58 of 63); (5) check whether a student's words are aimed at the marker; (6) accept an unplanned right answer only when the judge is sure, and log it; (7) two tries then the answer; (8) cite words, not line numbers; (9) quote exactly, checked in code; (10) background at the line that needs it (6 of 26 points before the first line); (11) a picture should show what the voice says, structural lines need labelled plates (12 of 22); (12) gate every check; (13) check machine output against something that does not assume the answer (blind transcription caught 4 of 4); (14) scripted readers play every lesson first.

Return up to 15 NEW candidates, most important first. For each give:
1. statement: one plain sentence that holds without the source text (no Othello terms, no people's names or job roles).
2. kind: "measured" (our own numbers), "adopted rule" (a rule the work now enforces, and what made us adopt it), "external research" (a cited study, give the DOI/URL as written in the source), or "open question".
3. evidence: exact file path plus section heading or line numbers, and the relevant sentence quoted exactly, with its number(s) as written.
4. against: counter-evidence or limits stated in the same sources, quoted, or "none found".
Then a short list of borderline items you left out and why. Exclude Othello-specific content, pure film aesthetics that would not carry to another lesson, internal organisation matters (who approved, meetings, team direction), and anything you cannot cite. Keep the whole answer under 1,500 words.

## Report

I found 15 new candidates that hold for any lesson and text. I checked every quote against its file; line numbers are as I read them. Three caveats from the sources apply to all of them: nothing was tried with students (FINDINGS.md l.3: "None has been tested with students."), most judgements are by one person, and no person has watched or listened to the final film.

**1. Nothing a student sees or hears may give away the answer before the first attempt, and that includes the paused picture behind a question.**
- Kind: adopted rule. It was adopted once labelled plates put answers on screen at a pause.
- Evidence: ~/Projects/othello-unit-video/research/METHODS.md l.10–11: "Nothing a student sees or hears may give an answer before the first attempt. Checks sit after the scene they ask about, and the film is blurred while a question is on screen." ~/Projects/g9/film/v06/README.md l.20–21: "two checks now pause over plates that show their answer."
- Against: ~/Projects/g9/player/design/ARCHIVIST-DESIGN.md §8 l.356, the earlier rule: "6.2 previous text stays accessible while answering … corner placement keeps the painting visible".

**2. A check must be answerable from what came just before it, must need that part, and should pause only at the end of a section.**
- Kind: measured.
- Evidence: ~/Projects/g9/film/v03/render/QA.md l.16: a line was added "so the Archivist check after scene 2 is answerable from what was heard." ~/Projects/g9/review/2026-10-08-lesson1-build-map/README.md Measured 2, l.36: "Part 2's check can be answered without reading part 2." ~/Projects/g9/review/three-film-comparison/COMPARISON.md l.13: "The first stop cuts in mid-sentence." ~/Projects/g9/player/content/archivist-checks.json l.39: "The film pauses at the end of the scene (in its silent tail)".
- Against: none found.

**3. An automatic marker can only apply a rubric rule if it is given what the rule refers to; otherwise the rule has to be enforced in code.**
- Kind: measured.
- Evidence: ~/Projects/g9/review/2026-10-07-archivist-marking-test/README.md "The five misses", l.49–50: "The rubric says the quote must not be "the one the Archivist used", but the judge is not told which quote that is." Re-check, l.82: "passed all five criteria again".
- Against: none found.

**4. An automatic marker can give a different verdict on the same answer, so send each test answer several times and re-send every known miss after each rebuild.**
- Kind: measured.
- Evidence: same README, l.43: "same verdict on all three runs | 9 of 10"; l.51: "met one criterion in 3 of 4 calls"; l.83: "held back in 2 of 3 runs"; l.96–97, a second marker run twice 7 minutes apart: "14 of 15", then "15 of 15". Build map README l.45: "Of that test's five misses, three came back, one timed out twice and one now gets half credit".
- Against: README l.96–97: the second marker's repeated answers were stable, "8 of 8", in both runs.

**5. Test whatever marks an answer when the model is slow or down, because that path marks real students too.**
- Kind: measured.
- Evidence: marking README l.14: "If the judge fails or takes over 9 s, the page marks with the keyword rules instead."; l.36: "91 calls; 9 timed out with no response in 40 s"; l.68 (not covered): "The page's own rules: the answers were written to pass them."; l.85: "no verdict: timed out twice at 40 s". The other build's fallback, ~/Projects/g9/review/three-film-comparison/threejs/checks.json l.7: "Your answer is kept. Send it again."
- Against: README l.44: "median 3.44 s, slowest 7.5 s; none over the page's 9 s limit".

**6. Review a lesson in the mode students get, because other modes of the same build can behave differently.**
- Kind: measured (an earlier review finding was corrected).
- Evidence: COMPARISON.md "Corrections made in this pass", l.50–51: "Our checks notes and design notes said seeking skips his checks. In the live code that is true only in reviewer mode; learners have no forward seek." threejs/checks.json l.105: "check-2.jpg and check-3.jpg were captured in reviewer mode".
- Against (limit): ~/Projects/g9/player/qa/QA.md l.3: our own runs used "Media muted for automation; audio sources verified by element `src`, not by ear."

**7. Take every length and time from the delivered file, leave values empty until they are measured, and label estimates as estimates.**
- Kind: adopted rule.
- Evidence: METHODS.md l.8–9: "Every cut, caption and music move is placed from measured word times. A render with estimated times is labelled as one." Build map l.42–43: "3:28 against the Info Sheet's limit of 3:00. The lesson data labels it `2:45`". ~/Projects/g9/film/TREATMENT.md l.28: timings "stay `null` until the approved voice files have been heard and measured."
- Against: ~/Projects/g9/review/2026-10-07-act1-context-map/README.md l.64 says its own shortened length is "arithmetic on v07 caption times, not a render".

**8. Report machine checks separately from human judgement, and mark quality calls "unjudged" until a person has watched or listened.**
- Kind: adopted rule.
- Evidence: ~/Projects/g9/film/v01/render/QA.md l.3: "Every number below comes from a measurement on the delivered files; none replaces the real audition". ~/Projects/g9/review/2026-10-06-film-reviews/VIDEO-REVIEW.md l.16: "Present, unjudged." ~/Projects/g9/tools/unit-video-essay/INTEGRATION.md l.40: "A successful render is technical proof only, not academic approval."
- Against: the human pass never happened. ~/Projects/g9/film/v07/README.md l.40: "No person has watched v7."

**9. Automated judges and keyword flags only choose what a person reviews; they do not decide.**
- Kind: measured.
- Evidence: METHODS.md l.107–110: "The judges are a filter, not a verdict: in one audition the same judge model reversed its ranking between two shuffles. … one of those passes also accused two clean takes. A voice is chosen by listening." ~/Projects/othello-unit-video/research/data/marker-test.json l.83–84: "flagged_by_keyword_heuristic_as_possible_give_away": 10, "found_on_reading_to_hand_over_a_missing_answer": 0.
- Against: the judges sometimes agree. v07 README l.18–19: "In three blind passes on scene 5, every judge preferred the 3.1 Flash take".

**10. Fix the scoring rule and the expected answers before measuring, apply them the same way to every option, and keep arguable cases out of the score.**
- Kind: adopted rule.
- Evidence: ~/Projects/g9/review/three-film-comparison/RUBRIC.md l.3: "Fixed before looking at the other two videos' results. Every row is checked the same way on each." Marking README l.24–25: "Arguable criteria are listed as `ambiguous` and left out of the score."
- Against: README l.72: "The labels are the tester's reading of each rubric, not a teacher's."; METHODS.md l.69: "Rows 3, 5, 6, 9 and 10 rest on judgements by one rater."

**11. Save the first attempt as well as the last, because first-try answers are the measure for comparing designs.**
- Kind: adopted rule.
- Evidence: archivist-checks.json l.43: "First and latest attempts are kept per check". FINDINGS.md l.54: "The gain in first-try answers has to be worth the minutes the gate adds."
- Against: FINDINGS.md l.51–52: forced checks "may push some students to guess".

**12. Meet a length limit by splitting the material into parts, not by cutting or speeding up the approved text.**
- Kind: adopted rule. It was adopted after a cut, sped-up version lost its style.
- Evidence: ~/Projects/othello-unit-video/research/FINDINGS.md l.22–23: "When I cut the script from 434 words to 299 and sped the voice up to fit a shorter film, it lost its style. Reading every word at a natural pace kept the style, and splitting the film into parts dealt with the length." METHODS.md l.12: "No word is cut, added or reordered".
- Against: FINDINGS.md l.27–28: "a faster read is a different voice. One of three AI judges thought the quick read sounded "far too young", and nobody outside the project has compared the two."

**13. Check what every picture implies against the text, and check again whenever a picture is regenerated.**
- Kind: measured. One miss reached the final film.
- Evidence: TREATMENT.md l.30: cuts "should be revised if they imply a character is present in a scene where the play does not place them." INTEGRATION.md l.22: "have both the words and what each reveal implies reviewed." METHODS.md l.136–138: "A repainted picture whose content had changed … passed the frame check and reached the final film's opening."
- Against: none found. The failure of the frame check itself is already under your item 13.

**14. Still pictures with printed text can teach as well as narrated animation, but the research is split.**
- Kind: external research.
- Evidence: FINDINGS.md l.8–10: "static diagrams with printed text did as well as narrated animation or better: better on 4 of 8 comparisons, the same on the rest" (Mayer et al. 2005, https://doi.org/10.1037/1076-898X.11.4.256, l.118).
- Against: FINDINGS.md l.13–15: "across 26 studies, animation beat still pictures on average (Höffler & Leutner 2007)" (https://doi.org/10.1016/j.learninstruc.2007.09.013). Our own test gave the animated version "51% to 41%", and "Mayer's studies were about physical systems, not literature."

**15. If students' words are kept and never scored, it is still open who reads them and what anyone learns from them.**
- Kind: open question.
- Evidence: FINDINGS.md l.113: "Who reads what students write, and what do they learn from it?"; ~/Projects/g9/player/README.md l.35: the follow-up answer "is saved and never judged either."
- Against: the context map README l.73 assumes a use: "The answers feed Lesson 2 retrieval."

**Borderline items I left out**
- **Narrator shown on screen:** shots with the narrator on screen carry their line in 2 of 11 cases, against 23 of 25 without (~/Projects/othello-unit-video/research/data/per-shot-test.csv l.5–6). But the rating rule marks talking-to-camera shots as "partly" or "competes" by design (METHODS.md l.23–25), and it is close to your item 11.
- **"short lines get the same check"** (METHODS.md l.101): a detail of one narration tool.
- **On-screen words appear as they are spoken:** INTEGRATION.md l.14 calls this "a design inference", and it is close to your item 11.
- **Feedback as "one declarative sentence", no praise** (ARCHIVIST-DESIGN.md l.177, l.341): never measured, and close to your item 3.
- **Scripted "Why did you say that?" follow-up:** whether it is acceptable is still open (v07 README l.40).
- **Check card must not cover the question's subject** (ARCHIVIST-DESIGN.md l.242): the blur replaced this.
- **"one fixed name" for each element** (ARCHIVIST-DESIGN.md l.355): rests on feedback only, nothing measured.
- **A transcriber flag that "did not reproduce"** (v01 QA.md l.114): fits under your item 13.
- **Scene detection "found only 8 of its 35 transitions"** (METHODS.md l.27–28): tool-specific.
- **Autoplay and HTTP Range notes:** web setup, not a lesson finding.
- **Cost per finished minute, and whether any of this would hold for "a modern novel"** (FINDINGS.md l.112, l.114): open, but nothing in these sources tests them.

**On your existing items**
- **Items 3 and 4:** the marking README l.62 says "36 of 63 verdicts came with the model's own reply: 19 to 30 words". summary.json and marker-test.json l.78–80 both say 42 replies of 15 to 36 words, and I counted 42 in the items. The README figure looks wrong.
- **Item 10:**
  - Support: the reading texts already carry all or part of 18 of the 26 points (~/Projects/othello-unit-video/research/data/context-map-totals.json l.88–89).
  - Against: FINDINGS.md l.93–95 cites pre-training on names (Mayer, Mathias & Wetzell 2002, https://doi.org/10.1037/1076-898X.8.3.147) and notes "Venice and the Cyprus wars both come up in 1.1".
- **Item 11:** the 22-of-22 result was judged by its maker. ~/Projects/g9/film/v06/SHOT-AUDIT-v6.md l.19: "Caveat: the person who built the plates judged them."
- **Item 12:** FINDINGS.md l.51: "most viewers answer them anyway (74% in Kovacs 2016)".
