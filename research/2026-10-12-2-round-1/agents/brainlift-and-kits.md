# Round 1: the BrainLift sources and the pipeline kits

A read-only search agent, 2026-10-12 07:48 to 2026-10-12 08:06 UTC. Its brief and its final report, verbatim.

## Brief

Find lessons learned that hold for ANY lesson and ANY text (not specific to Othello, Shakespeare, or one team's tools), each with its exact evidence, from a research record and two reusable pipeline kits. Thoroughness: very thorough.

STRICT RULES: read-only. Do not create, edit, move or delete any file, and run no command that writes. Do not open .env files, key or token files, and never print a secret or bearer token. Do not fetch URLs. Do NOT read ~/Projects/g9/.local/ela-gravity/ at all.

Sources (only these):
- ~/Projects/g9/.local/brainlift-sources/ (especially v5/: plan7.json, nodes-live-12.json and similar JSON holding the research record's claims, facts and evidence nodes; read their text content)
- ~/Projects/unit-video-kit/ (README files, skills/, workflows/, docs: the rules a narrated-lesson-video pipeline enforces and why)
- ~/Projects/othello-unit-video/kit/ and ~/Projects/othello-unit-video/.claude/ (the public, stripped copy of that kit)
- ~/Projects/g9/tools/unit-video-modules/ (README, HANDOFF.md, docs and test notes of reusable video frame modules)

We ALREADY HAVE these 14 (skip them unless you find new, stronger evidence or a counter-example): (1) an unsure judge is neither pass nor miss; (2) a choice question needs one answer the text settles, each option checked on its own; (3) wrong-answer feedback sends the student back without the answer and says only true things; (4) keep students' written words, a model's reading may choose a hint but not a grade (AI marker 58 of 63); (5) check whether a student's words are aimed at the marker; (6) accept an unplanned right answer only when the judge is sure, and log it; (7) two tries then the answer; (8) cite words, not line numbers; (9) quote exactly, checked in code; (10) background at the line that needs it (6 of 26); (11) a picture should show what the voice says, structural lines need labelled plates (12 of 22); (12) gate every check; (13) check machine output against something that does not assume the answer (blind transcription 4 of 4); (14) scripted readers play every lesson first.

Look especially for: rules about narration (pace, verbatim scripts, style instructions, splitting long media), on-screen text, accessibility (captions, reduced motion), how media timing is bound to the voice, what a review of AI-made media must check, provenance and hashing of assets, and claims in the research record with their evidence and counter-evidence.

Return up to 15 NEW candidates, most important first. For each give:
1. statement: one plain sentence that holds for any lesson (no Othello terms, no people's names or job roles).
2. kind: "measured" (our own numbers), "adopted rule" (enforced by the kit or modules, and what made it), "external research" (a cited study, DOI/URL as written), or "open question".
3. evidence: exact file path plus JSON key, section heading or line numbers, the sentence quoted exactly, numbers as written.
4. against: counter-evidence or limits stated in the same sources, quoted, or "none found".
Then a short list of borderline items left out and why. Keep the whole answer under 1,500 words.

## Report

Roots: BL=~/Projects/g9/.local/brainlift-sources · UVK=~/Projects/unit-video-kit · OUV=~/Projects/othello-unit-video · MOD=~/Projects/g9/tools/unit-video-modules. "fact k" means the fact whose `key` is k in that file's `tree`. "plan7 [i]" means BL/v5/plan7.json `patches[i].content`.

**1. Nothing a student sees or hears before the first try may give the answer: put it after the check, or hide it while the check is open.**
- Kind: measured + adopted rule (made by plates that showed their answers).
- Evidence: plan7 [26]: "Anything shown before a question can answer it: a plate, a summary, a model quote." BL/comparison.json fact core-14: "checks 1 and 2 opened over plates that showed their answers". OUV/.claude/skills/uvk-checks-make/SKILL.md L32–33: "the question's own wording included". BL/checks.json fact ploetzner-2024-interaction-features-meta: "if a video is not paused … learning is impeded" (https://doi.org/10.1080/10494820.2022.2123002).
- Against: BL/checks.json fact is-answer-first: "the narration states each answer just before its check". Fact pl-replay: the "Hear the scene again" button replays the scene before the check is done.

**2. Meet a length limit by changing the voice model or splitting the video into parts, never by cutting words or speeding up the voice.**
- Kind: measured + adopted rule (made by a version that was cut and sped up, then rejected).
- Evidence: plan7 [6]: "Cut from 434 words to 299 and sped up, the film lost its style; read in full and split into parts, it kept it." BL/narration.json fact p-paced-slower: asking for a pace "made it slower: 66.76 s against 59.24 s". OUV/kit/docs/STANDARDS.md L11–12: "never by cutting lines or time-stretching a take". BL/film.json fact rey-2019-segmenting-meta: segments "improved retention and transfer (small to medium effects)" (https://doi.org/10.1007/s10648-018-9456-4).
- Against: BL/parts/film-research.json doubts[5]: "No study was found comparing a re-performed narration with a time-stretched take"; "Murphy et al. (2022) suggests speed itself costs little comprehension up to 2x."

**3. Keep instructions on how to read apart from the words to be spoken, and let them describe only the tone.**
- Kind: external research + adopted rule (made by a voice model reading its instructions aloud).
- Evidence: BL/narration.json fact google-gemini-tts-verbatim-transcript: "treats the text field strictly as a verbatim transcript"; "sustained style belongs in a separate speech_metadata.style field" (https://ai.google.dev/gemini-api/docs/speech-generation). plan7 [19]: "One voice model read its own style instructions aloud at the start of all four of its takes." UVK/.claude/skills/uvk-narration-make/SKILL.md L16: "The direction describes the register only."
- Against: the kit still sends both in one string (UVK/tools/narration/generate_takes.py L84: "contents=STYLE + text"). BL/parts/production-research.json dropped[2]: no peer-reviewed study of this was found.

**4. Time every cut, caption and music cue from measured word times, each tied to a phrase that occurs once; build captions from the exact script; stop the build rather than guess.**
- Kind: adopted rule (made so that a new voice recording re-times the whole film without hand editing; BL/narration.json summary s-edit-1).
- Evidence: UVK/tools/film/render-narrated.js L56: "Fails loudly when absent or ambiguous." UVK/.claude/skills/uvk-film-make/SKILL.md L11: "must appear exactly once in that scene's script". BL/narration.json fact e-captions: "the render stops if the joined caption text is not the exact script; v7's 51 cues match the alignment with 0 s error."
- Against: fact e-short-shots: "ten warnings for cuts landing under its 1.5 s warning threshold". BL/comparison.json fact yue-2013-partial-redundancy: "Text identical to the narration impaired learning" (https://doi.org/10.1037/a0031971). Yet captions are on by default (UVK/tools/player/template/index.html L98).

**5. Show on screen only a few keywords the voice is saying, each appearing as it is spoken, and count printed text as clutter.**
- Kind: measured + external research.
- Evidence: BL/comparison.json fact plt-organiser: a plate "printed all eight unit words … before any of them was spoken". Same file, rejected[1]: "his film shows text 95% of the time." OUV/kit/docs/STANDARDS.md L34: "A plate shows only words the narration speaks while it is on screen". Fact mayer-johnson-2008-short-labels: "2–3 printed words per slide … improved retention (d = 0.47 and 0.70 …) but not transfer" (https://doi.org/10.1037/0022-0663.100.2.380).
- Against: fact richter-2018-signals-prior-knowledge: "for students with high prior knowledge the added signals were detrimental".

**6. Give every visual a reduced-motion version with the same information and a full text description, and never let colour alone carry meaning.**
- Kind: adopted rule (part of the module design; no failure behind it is recorded).
- Evidence: MOD/packages/core/README.md L26: "Use `motion: 'reduced'` for the same information without fades, pans, or fast motion." MOD/packages/evidence-plate/README.md L18: "includes every line regardless of animation time". MOD/packages/argument-map/README.md L3: "Color is reinforced by position, labels, and full `accessibilityText`." MOD/INTEGRATION.md L20: "it does not replace captions or human review".
- Against: BL/seven/ext/course-renderer-INSTRUCTION-BRAINLIFT.md L256: in another course, the share of accessibility rules with no check was "accessibility 100% (7 rules, no checks)".

**7. Check every AI-made or AI-repainted image by eye against its brief and its source, and draw maps and diagrams from data.**
- Kind: measured + adopted rule (made by a repaint that changed the content and still passed).
- Evidence: OUV/.claude/skills/uvk-art-make/SKILL.md L61–63: "in 1 of 18 repaints the model added an embracing couple to an empty bedchamber and put out its last lit candle, and the film's frame check passed it". UVK/.claude/skills/uvk-art-make/SKILL.md L36, L38: "one in 22 finished paintings came back with a paper border drawn in"; "faces moved 30–60 px". UVK/docs/TROUBLESHOOTING.md L13: "A generated map gets the geography wrong".
- Against: none found. The frame-check fault is also behind your (13).

**8. Treat AI judges, speech recognisers and detectors only as flags for a person who watches and listens: never score on them, shuffle the judging order, and check automatic measures by eye.**
- Kind: measured + adopted rule (made by judging passes that all heard the same order) + external research.
- Evidence: UVK/.claude/skills/uvk-narration-make/SKILL.md L42–43: "A judge assists a listen; it never replaces one." BL/narration.json fact j-7oct-same-order: "every judge heard the takes in the same order". Fact zheng-2023-position-bias: "Most LLM judges favor the first position" (https://doi.org/10.48550/arXiv.2306.05685). OUV/.claude/skills/uvk-video-compare/SKILL.md L58–59: "one film here came out at 98.4% purely from recogniser errors." BL/comparison.json fact fb-rej-cut-detection: "misses 27 of the 35 transitions". OUV/.claude/skills/uvk-checks-make/SKILL.md L105–106: "Automated runs are muted, so a person still has to watch the film with sound."
- Against: fact chiang-2025-audio-llm-style-judges: agreement "comparable to the agreement between human evaluators". BL/narration.json open_questions[4]: "26 plausible extra words" against a clean "83 of 83"; "no record reconciles the two".

**9. Record each asset's source, settings and hashes, verify the hash before use, run one generator per folder, and treat a source note as a record of origin, not permission to reuse.**
- Kind: adopted rule (made by parallel runs overwriting each other's records).
- Evidence: BL/narration.json fact l-parallel-manifest: "6 parallel gen-othello-narration runs overwrote each other's narration-manifest.json entries". OUV/.claude/skills/uvk-narration-make/SKILL.md L42–43: "a new voice in an old folder leaves old takes under a new label." MOD/INTEGRATION.md L16: "verifies the SHA-256 before returning"; "An asset source note is provenance, not a grant of reuse rights."
- Against: BL/narration.json caveats[10]: align-words.py "writes the same method string … whether or not ALIGN_NO_PROMPT is set". OUV/.claude/skills/uvk-art-make/SKILL.md L72: the export "removes every metadata block (EXIF, XMP, IPTC, ICC, C2PA, comments)".

**10. Fix the rubric and pass marks before measuring, measure every version the same way, and change one part at a time.**
- Kind: adopted rule (made by a three-film comparison) + measured.
- Evidence: BL/comparison.json fact fb-rubric-fixed: "Fixed before looking at the other two videos' results". Fact core-12: "audio byte-identical: 22 of 22 lines carry." plan7 [37]: "a pass mark agreed in advance". OUV/kit/templates/review/rubric.example.md L5: "change a row only as a dated correction with its reason."
- Against: fact fb-fid-scripts-not-audio: the fidelity row fixed in advance ("word-level diff of what is spoken") had to change. The loudness limit is also inconsistent: UVK/tools/film/render-narrated.js L354 says "true peak <= -1 dBTP", UVK/.claude/skills/uvk-film-make/SKILL.md L29 says "true peak under -0.5 dBTP", and OUV/.claude/skills/uvk-film-make/SKILL.md L80 reports "-0.9 dBTP, 0.1 dB over."

**11. Treat "it looks AI-made" as a question about the finish, to be tested on the same content, and do not read liking as learning.**
- Kind: open question + external research.
- Evidence: BL/film.json insights[0]: "\"Looks AI-generated\" is a verdict on the finish, not the format." Fact millet-2023-anthropocentric-bias: "the same artwork was preferred less when labelled AI-made than human-made" (https://doi.org/10.1016/j.chb.2023.107707). BL/comparison.json fact sung-mayer-2012-liking-not-learning: "Every kind of graphic raised satisfaction ratings over no graphics, but only the instructive graphics raised recall." (https://doi.org/10.1016/j.chb.2012.03.026)
- Against: plan7 [29]: "none says how believable a format looks". BL/parts/film-research.json doubts[7]: "no peer-reviewed study of how AI-looking illustrations affect students' learning was found."

**12. First-try answers measure attention in the moment; showing that learning lasts needs a later test on new questions.**
- Kind: open question + external research.
- Evidence: plan7 [30]: "Whether any of it helps a week later is untested." BL/checks.json fact roediger-karpicke-2006-delayed-retention: "On a final test 5 minutes later restudying won, but after 2 days and 1 week "prior testing produced substantially greater retention than studying"" (https://doi.org/10.1111/j.1467-9280.2006.01693.x). BL/seven/ext/course-renderer-INSTRUCTION-BRAINLIFT.md L243–245: "only a delayed, different-day, no-feedback assessment on novel items at 80% proves the second."
- Against: none found.

**Borderline, left out**
- **Right-answer position:** BL/checks.json fact v7-shape: "the right one is listed first in five of the seven choice steps", and the player never shuffles the options. Close to your (2).
- **Gate forward only:** BL/checks.json fact p1-gating: "Locking backward removes re-reading". Refines your (12).
- **Synthetic voice only where learners can hear its errors:** BL/film.json fact fb-tts-ok. It rests on one reviewer's note, and the kit voices everything synthetically.
- **Presenter on screen only at set moments:** "2 of those 11 shots carry" (BL/comparison.json fact fb-pk-archivist-time). A case of your (11).
- **Background music; stills versus motion:** the research conflicts and nothing has been tested.
- **"A rule no build can fail is not held":** comes from another course's record.
- **Counter-evidence to your list:**
  - (10): BL/film.json fact mayer-mathias-wetzell-2002-pre-training: teaching the parts first "did better on transfer in all three experiments".
  - (12): BL/checks.json fact decieux-2015-forced-answering: forced answering "increases dropout rates and decreases quality of answers".
  - (13): the record disagrees on its own count. BL/narration.json fact core-1 says "2 of 4 scene-1 takes" read the instructions aloud, where plan7 says all four. Also, fact zheng-2023-reference-guided-judge: giving GPT-4 a reference answer cut its false passes from "14/20" to "3/20".
  - (7): BL/answers.json fact brief-cap: "the v7 player has no cap."
