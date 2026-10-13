# verify:artifacts-builds-research

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "artifacts-builds-research",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All quotes verified. The first one wraps across lines 78-79, so the line number is corrected. Numbers match: 1 of 10 confirmed and 9 dismissed; 8–15% false positives from single-layer audits. General, and not on the list (nearest are 24 and 43). Overlaps candidate 1, but this one is about audit claims rather than broken probes.",
   "statement": "Before acting on an audit finding, re-check it against the current file and against the approved reference lessons; many critical findings do not survive that check.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/DECISIONS-2026-08-24.md",
     "lines": "78-79",
     "quote": "roughly half of \"CRITICAL\" audit claims were false",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md",
     "lines": "10",
     "quote": "Verdicts: **1 CONFIRMED, 9 DISMISSED** (plus the 3 engine-debt items carried unchanged).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "129",
     "quote": "false-positive rate of single-layer findings is 8–15% across two independent lanes",
     "verbatim": true
    }
   ],
   "against": "The reference test can bless a gap the references share: \"aspiration the references do not meet either. Not a defect.\" (g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md line 27).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: 27 false positives, and the 172-item clean pool scored ~0–1.7%. Added a non-name AP-history case from the honesty fact sheet, where a 28% pass reading turned out to be four harness bugs. Distinct from 38, which is about checks that never fire.",
   "statement": "When a check reports defects, test the check before fixing the content; broken probes produce convincing false defects.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "108",
     "quote": "Provenance: probe-is-often-the-bug — half of \"audio defects\" were defective",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/whisper-qa-2026-09-02/REPORT.md",
     "lines": "10",
     "quote": "itself and \"finds\" cross-lesson bleed that isn't there. First pass flagged 27 such",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md",
     "lines": "47",
     "quote": "The same probe scored the **172 certified-clean** pool at ~0–1.7% leak — the",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "56",
     "quote": "the \"28%\" was **four harness bugs**.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep",
   "reason": "Quotes verified: 1 of 18 lessons, and the PP-12 defect came back one lesson after its fix. General, and not on the list.",
   "statement": "Never certify a course from the lesson that was reviewed; recompute each quality claim across every lesson, because a quality or a fix in one lesson often does not hold in the others.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "118",
     "quote": "Never certify on the lesson the reviewer saw. Recompute every quality",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "120",
     "quote": "\"real modeling in 1 of 18 lessons — the reviewed one.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D1-D4.md",
     "lines": "301",
     "quote": "recurrence of the PP-12 defect pattern one lesson after its fix",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "Quotes verified: the 7–8 'generate' claim was true by count but 5 of 7 moments were canned; 3 of 9 lessons had audio; format compliance could not be audited from the files used. Overlaps 24 and candidate 43. Kept for the warning that a count can be right while the quality is not.",
   "statement": "Treat your own completion claims as hypotheses and re-derive them from the delivered content; a count can be right while the quality it implies is not.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "123",
     "quote": "was \"true by count, misleading by quality — 2-3 trivial say-backs; 5 of 7 spoken moments canned.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/GAP-ANALYSIS-2026-08-18.md",
     "lines": "47",
     "quote": "`AUDIO_STATUS.md` falsely claims all of Unit 4 is done — only 3 of 9 are",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md",
     "lines": "15",
     "quote": "Any G5 gate report claiming format compliance based only on these artifacts would be dishonest.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "Quotes verified. The table gives 353 items, 334 leaky and 19 clean (94.6%), with hot-text at 90.6%. Refines 5: an item's format does not stand in for its text dependence. The against quote is verified (LANE1 line 136).",
   "statement": "An item format that usually needs the text does not guarantee it; check every item for text dependence on its own.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md",
     "lines": "19",
     "quote": "**Verdict: the 353 are overwhelmingly leaky.** Only **19 items** genuinely require the passage under a",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md",
     "lines": "21",
     "quote": "anti-leak FORMAT ≠ low leak",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g3-control-set-2026-07-10/G3-CALIBRATION-REPORT.md",
     "lines": "49",
     "quote": "Construction, not format or grade, is the lever.",
     "verbatim": true
    }
   ],
   "against": "Format still shifts the odds: in another pool \"| hot-text | 1,479 | ~17.5% | ~1,220 |\" against 99.5% for multiple choice (LANE1_COURSE.md line 136).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "Quotes verified: 417 of 1,152 failed the with-text control, and 186 of 299 control-passers leaked (retrospective lines 228-229). Mostly truths 5, 6 and 66 combined. Kept as a duplicate because it adds measured evidence that the two controls reject different items.",
   "statement": "Accept an item only when a solver from a different model family than the writer answers it correctly with the text and cannot recover the answer without it; each test rejects items the other passes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "11",
     "quote": "They were accepted only when a different model family could answer them with the passage and could not recover the keyed",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "182",
     "quote": "Control-pass rate did not predict certification.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "222",
     "quote": "That second condition matters. It prevented \"anti-leak but broken\" items from entering the final set.",
     "verbatim": true
    }
   ],
   "against": "How strict the without-text bar is matters: \"Both bars were designed to avoid frontier-model-proofing a Grade 5 assessment\" (QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md line 304).",
   "general": true,
   "duplicate_of": "5",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "Quotes verified. One correction to found_by: 24 items looked clean under the union rule, 9 of them on one family alone, and running both families properly left 19. The 191 same-family certifications check out. Adds to 66: use a second family that is not the writer's, and check claims of independence.",
   "statement": "Run the without-text check with more than one solver family other than the writer's, count an item clean only if all fail, and verify that a claimed independent check really used a different family.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md",
     "lines": "53",
     "quote": "9 of which rested on gpt-4.1 alone; the real two-family number is **19**.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
     "lines": "184",
     "quote": "Same-family 'cross-family' claims",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "204",
     "quote": "Same-family generation bias (Claude generates + Claude blind-solves) is the one unmitigated risk",
     "verbatim": true
    }
   ],
   "against": "One independent family is accepted as a named gap rather than a failure: \"A second working non-generator family would harden the leak claim\" (g5-merged-course/VERDICT_TEMPLATE.md line 77).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep",
   "reason": "Quotes verified: recoveries fell from 43 to 39 on 45 served items. The bar was adopted at two grades. The earlier rule that counted any recovery (against) is verified. Refines 5.",
   "statement": "Count a without-text recovery as a leak only when a typical student at the target level could reproduce it, not merely a strong model.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g3-control-set-2026-07-10/G3-CALIBRATION-REPORT.md",
     "lines": "62",
     "quote": "recovery counts as leak only when a typical THIRD grader could plausibly reproduce it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-claude/run/SOLVER_V2.md",
     "lines": "14",
     "quote": "The bar is a savvy student, not an expert.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "304",
     "quote": "explicitly asks whether a real fifth grader could reproduce the blind recovery",
     "verbatim": true
    }
   ],
   "against": "An earlier protocol counted any model recovery: \"**Threshold:** 2/3 correct recoveries = LEAKED.\" (LANE3_LLM.md line 270).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: an item scored 0/3 without the text under Gemini 2.5 and 3/3 under Gemini 3.5, and stays out of serving. The calibration quote is about the course changing, not stronger solvers, so the statement now covers both. The report header adds that its results are a dated snapshot. Pairs with candidate 7: a stronger solver's recovery still has to be one a student could reproduce.",
   "statement": "Treat a without-text pass as dated to the solver and the content it was run on, and re-run it when a stronger solver arrives or the content changes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
     "lines": "22",
     "quote": "Current Gemini 3.5 is 3/3 in both conditions, so the item is directly gameable",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
     "lines": "5",
     "quote": "**AI use:** treat model results as a 2026-07-10 Gemini 2.5 snapshot, not current certification.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g3-control-set-2026-07-10/G3-CALIBRATION-REPORT.md",
     "lines": "84",
     "quote": "- The live course moves — this distribution is dated 2026-07-10; re-pull before re-measuring.",
     "verbatim": true
    }
   ],
   "against": "A stronger solver is not a student: \"out-reads the child; near-chance forced guesses are not leaks\" (G3-CALIBRATION-REPORT.md line 57).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: MCQ leaked 99.5%, with 7 of 1,473 usable. No quote supported the second clause; LANE2 line 33 now does, though as a prescribed fix rather than a measured one. Refines 5. The 'when the text is the evidence' condition handles the against (knowledge should pay off in learning texts).",
   "statement": "A text built from facts most readers already know lets its questions be answered without it; when the text is the evidence being assessed, build it around particular events, decisions, arguments or surprising claims that only that text supplies.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "21",
     "quote": "**Root cause: passages describe well-documented curriculum facts.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "29",
     "quote": "The generator asks \"what does the passage say about X?\" — but X is something any educated reader already knows from school.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "33",
     "quote": "passages must describe specific events, character decisions, author arguments, or surprising/counterintuitive claims that are genuinely unknowable without reading this specific passage.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "269",
     "quote": "- MCQ leaked through ordinary school knowledge, such as Gutenberg, scurvy/citrus, or vocabulary clues.",
     "verbatim": true
    }
   ],
   "against": "Learning texts should let taught knowledge help; an external review faulted a design that kept knowledge from paying off: \"It cites Hirsch and Willingham and then forbids knowledge from helping.\" (g5_build_2026_07_02/feedback_clean.md line 43).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. The 12.4% figure comes from a different pool than the certified bank, so the before-and-after link in found_by is not shown. Replaced it with the demo unit's spine gate, which decertified an item because content from earlier lessons answered it. Pairs with open question 111.",
   "statement": "A gate that removes every question answerable without the text also removes the questions the unit's own taught knowledge would answer, so the certified bank cannot show knowledge growth; measure that separately, for example by comparing students' explanations of the unit's concept before and after.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/VERDICT_TEMPLATE.md",
     "lines": "70",
     "quote": "2. **KCT1 Domain-knowledge ≈ 0 — by design.** Domain-recall items are passage-independent → removed",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
     "lines": "22",
     "quote": "Decertified `certified -> spine_leaky`",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/04-evidence-contract.md",
     "lines": "11",
     "quote": "> Improvement from pre-unit to post-unit student explanation of the unit concept.",
     "verbatim": true
    }
   ],
   "against": "The pre/post explanation measure is a proposal (04-evidence-contract.md), not a result.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Quotes verified: the external review said it twice, and the proposal states the rule. The proposal's layer structure keeps cold passages for diagnostics, as the statement says. The against (topic coherence fades before the test) is verified.",
   "statement": "Sequence learning texts so taught knowledge recurs and pays off, and keep cold, unrelated texts for tests and diagnostics only.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "45",
     "quote": "Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "25",
     "quote": "The passages jumped from e.g. the axolotl to shadows with no visible link, there is no pre-teaching of key ideas, and no strategy is revisited at greater depth.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/03-transfer-practice-layer.md",
     "lines": "59",
     "quote": "- do not use cold passages as the main teaching surface;",
     "verbatim": true
    }
   ],
   "against": "When the target test mixes unrelated texts, topic coherence has to fade before it: \"is the last scaffold, and like every other scaffold it fades gradually\" (g5_build_2026_07_02/approval_clean.md line 296).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. The source calls a swappable text a 'bad sign', not proof. Its list of text roles also includes genre and vocabulary demand, not only knowledge. Wording softened to match.",
   "statement": "Choose a unit's texts before writing any questions and give each one a stated role in the unit's knowledge arc; if any text could be swapped out without changing the unit, that is a sign the sequence is not building knowledge.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/01-course-graph.md",
     "lines": "63",
     "quote": "A planned set of texts selected before questions are written.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/01-course-graph.md",
     "lines": "75",
     "quote": "Bad sign: any text can be swapped out without changing the unit.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "53",
     "quote": "Choose texts for a coherent knowledge sequence and a genre balance that includes poetry, drama and more literary work, and judge complexity qualitatively as well as by Lexile.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep",
   "reason": "Quotes verified: the inventory pairs what each text assumes and adds with the spans that carry it, and the simulated review credits openers that need the prior lesson's specific knowledge. The opener part overlaps the prior-knowledge step in 40; the inventory part is new.",
   "statement": "Record the knowledge each text assumes and adds, tying each addition to the sentence that carries it, and open each lesson with a question that needs the specific knowledge the previous lesson built.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-knowledge-inventory.md",
     "lines": "8",
     "quote": "Proposed adds / assumes per text, with carrying spans.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "35",
     "quote": "restates and tests the prior lesson's narrative state, always using a question that requires the",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/01-course-graph.md",
     "lines": "87",
     "quote": "- What later text depends on this beat?",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep",
   "reason": "Quotes verified: 0 of 55 confirmed; 28 of 49 (57%); 7 of 55 (13%). The two reports even disagree on whether any G4-to-G5 links exist (none encoded vs 7 arcs), which is exactly why the links need recording and confirming. The against is verified.",
   "statement": "Record and confirm what each lesson assumes from earlier grades, and measure how many lessons actually draw on that prior knowledge.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/GAP-ANALYSIS-2026-08-18.md",
     "lines": "51",
     "quote": "There is no G3→G5 or G4→G5 transfer arc encoded anywhere in the canon.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/CURRICULUM-REVIEW-STANDING-2026-08-17.md",
     "lines": "66",
     "quote": "G3→G4: 9 arcs, 28/49 lessons (57%) citing G3 content.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/CURRICULUM-REVIEW-STANDING-2026-08-17.md",
     "lines": "67",
     "quote": "G4→G5: 7 arcs, 7/55 lessons (13%) citing G4 content — a real 7x drop in citation density.",
     "verbatim": true
    }
   ],
   "against": "The drop was a disclosed choice: \"as a deliberate design choice (G5's canon was authored\" (g5-course/CURRICULUM-REVIEW-STANDING-2026-08-17.md line 70).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep",
   "reason": "Quotes verified. The file describes the external curriculum directory; I did not fetch it. The ruling on the retired unit supports the redundancy clause.",
   "statement": "Go deep on a topic with a set of texts, and return to it in later grades only with new, more sophisticated knowledge; a unit repeating angles an earlier grade already covered is redundant.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/13-candidate-themes-and-selection-rubric.md",
     "lines": "5",
     "quote": "spiraling back to topic areas with more sophistication.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/13-candidate-themes-and-selection-rubric.md",
     "lines": "7",
     "quote": "Source: https://knowledgematters.org/curriculum-directory/",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/HUMAN-BODY-III-DECISION.md",
     "lines": "10",
     "quote": "exact mistake for which G4's Human Body II was retired, and the G4 crosswalk already",
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
   "verdict": "keep",
   "reason": "Quotes verified: the text at FK 2.7 carried more new ideas than the one at FK 3.5, and chapters ranged from FK 4.84 to 7.91. The one-pager's path names a book title, not a person. The against is verified.",
   "statement": "Readability formulas miss knowledge load and hide variation inside a book; measure the exact excerpt used and judge complexity qualitatively too.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "18",
     "quote": "measures lexically simpler than the primer (FK 3.5) because its sentences are short; its",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
     "lines": "20",
     "quote": "denser stated/implied layering, which the FK heuristic does not see.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/pd-texts/winnie-the-pooh-onepager.md",
     "lines": "28",
     "quote": "Chapter range FK 4.84 (ch VI) to",
     "verbatim": true
    }
   ],
   "against": "Measures disagree, and a documented level was preferred over the formula: \"documented 790L remains the better band evidence\" (g5-course/pd-texts/winnie-the-pooh-onepager.md line 27).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep",
   "reason": "Quotes verified: the 1915 translation is documented at 800L while others run 1200L, and only original editions of some series are in the public domain. Related to 50, but about choosing the edition.",
   "statement": "Pin the exact edition or translation of a source text, since its reading level and rights status can differ by edition.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/PD-FICTION-RESEARCH-2026-08-19.md",
     "lines": "25",
     "quote": "pin the Stork 1915 translation specifically (others run 1200L)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/PD-FICTION-RESEARCH-2026-08-19.md",
     "lines": "13",
     "quote": "only the ORIGINAL edition text is PD — the revised editions everyone knows are still",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep",
   "reason": "Quotes verified: seven of nine words appeared once; 0 of 4 passed; 4–5 exposures against a ~6 standard. The U1 table shows most words picked for being hard to pronounce fail the rule. Refines 18 by adding recurrence. The against is verified.",
   "statement": "A word taught in depth must recur — more than once in its own text and again later in the unit — and words picked because they look hard mostly fail that test.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "69",
     "quote": "unit, counted by word family (R-VOC-7/13 — written after seven of nine taught words turned out",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/VOCAB-DECISIONS-U1.md",
     "lines": "19",
     "quote": "| U1L1 | atmosphere, hydrosphere, geosphere, biosphere | **0 of 4** — each appears once |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "87",
     "quote": "Across the arc, each target word gets approximately 4–5 exposures, not 6+, and drops out after",
     "verbatim": true
    }
   ],
   "against": "Some designs withhold the word from the text on purpose: \"**Adversarial refutation attempt:** The words are encapsulating words by design (vocabulary\" (arc-audit/SIM-REVIEW-D7-D8-D10-D12.md line 91).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep",
   "reason": "Quotes verified: a dictionary-correct answer failed the rubric; one source defined 'evidence' three ways; the standard calls for one verbatim definition per concept.",
   "statement": "Give each taught word one definition across the whole course, and define its real meaning; a student who gives the true meaning must not fail.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "217",
     "quote": "subject and verb\" fails the rubric for being right. If the card must exist, define",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/VOCAB-DECISIONS-U1.md",
     "lines": "31",
     "quote": "the canon defines `evidence` three different ways",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "186",
     "quote": "A2 one verbatim definition per concept",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: 62.7% of keys were recovered without the text, and 512 items had the key over the 20% length margin (LANE2 line 68). Nothing supported 'shortest', so it is removed; the paired-contradiction quote (line 64) is added. Distinct from 6 and 8.",
   "statement": "Make sure no option can be ruled in or out by surface cues — absolute words in wrong options, a key that is systematically the longest, two wrong options that contradict each other, or one option that sounds more textbook-correct.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "60",
     "quote": "1. **Absolute language tells** — wrong options use \"always\"/\"never\"/\"all\"/\"completely\" → flagged",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "61",
     "quote": "2. **Longest-option wins** — correct answer systematically longest (>20% margin)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "64",
     "quote": "5. **Paired contradiction** — two wrong options logically contradict each other",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "270",
     "quote": "- MCQ also leaked when one option was the obvious balanced or textbook-sounding answer.",
     "verbatim": true
    }
   ],
   "against": "The length rule does not apply where length reveals nothing: \"does not transfer to match extras. No action.\" (g5-course/ADVERSARIAL-REVIEW-2026-09-04-R16.md line 52); surface fixes alone left most items leaking (LANE1_COURSE.md line 167).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "Quotes verified: regeneration cut MCQ leakage only from 99.5% to 90.0%. This is the other face of truth 65. Kept for the measured regeneration result and the remedy: redesign the passage or the format.",
   "statement": "Fix systematic leakage at its source — the text or the item format — rather than by patching options or regenerating more of the same.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "167",
     "quote": "Regen pilot (Wave 3) showed 9.5pt improvement in MCQ leak (99.5% → 90.0%) but leak remained",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "31",
     "quote": "**Fix verdict:** NOT fixable with option-length patches. Requires passage strategy redesign.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "152",
     "quote": "- Skeleton redesign (V2) resolves the regen problem by eliminating MCQ/MSQ from the build and substituting passage-dependent formats with sufficient pool depth.",
     "verbatim": true
    }
   ],
   "against": "A format change alone is not enough either: \"anti-leak FORMAT ≠ low leak\" (g5-merged-course/a2-cross-family-regate.md line 21).",
   "general": true,
   "duplicate_of": "65",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "Quotes verified: 36 of 45 vocabulary items leaked; word-part, synonym and connotation items leaked 100%; the 120 seed items leaked 99.2%. The against is verified.",
   "statement": "A skill that is itself word knowledge (word parts, synonyms, connotation) cannot be tested by questions that need the text; decide separately how to assess it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "242",
     "quote": "Skill IS word-part knowledge, not passage inference — cannot be made passage-dependent.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "246",
     "quote": "cannot be tested as passage-dependent items and should be excluded from the comprehension-course blueprint",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md",
     "lines": "41",
     "quote": "the 120 L.5 vocab seeds LEAK 99.2% and must be re-authored + re-certified, never deployed as-is",
     "verbatim": true
    }
   ],
   "against": "Context-clue items partly worked: \"**Best-performing.** 8 survivors: technical/domain-specific words\" (LANE1_COURSE.md line 240).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep",
   "reason": "Quotes verified: the 8 survivors used words in domain senses, and the 7 that leaked used everyday meanings. Only 15 items, as the against says.",
   "statement": "In context-clue word questions, use words in senses the reader can't already know; words used in their everyday meaning get answered without the text.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "240",
     "quote": "8 survivors: technical/domain-specific words (normal, base, draws, channels, reservations, niche, range, intrusive). 7 leaked: dominant-meaning words",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE3_LLM.md",
     "lines": "244",
     "quote": "a word's meaning must be derivable only from the passage, not from world knowledge",
     "verbatim": true
    }
   ],
   "against": "Small sample: \"| L.5.4a (context clues) | 15 | 7 | **8** | 47% |\" (LANE1_COURSE.md line 240).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep",
   "reason": "Quotes verified: sequences built on world knowledge passed the without-text check ~45% of the time, so ~55% leaked. The against is verified.",
   "statement": "An ordering task leaks when its steps follow common logic or a familiar story or process order; use steps whose order only the text settles.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "278",
     "quote": "Sequence worked better than the other non-match formats, but it failed whenever the fragments had a natural order:",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "285",
     "quote": "The surviving sequence items need neutral, non-orderable details whose order depends on passage location, not common logic.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "50",
     "quote": "| sequence | 100% | ~45% (world-knowledge seqs) | Some steps deducible without passage |",
     "verbatim": true
    }
   ],
   "against": "Order-by-location items can turn mechanical: \"Anti-leak success is not enough.\" (QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md line 89).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep",
   "reason": "Quotes verified. The gate summary covers one grade-3 unit; the grade-5 retrospective (line 272) corroborates it. The against is verified.",
   "statement": "In select-from-the-text items, include at least two competing spans of the same shape and a question that cannot be resolved without the text; wording that signposts the right spans gives them away.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "66",
     "quote": "- hot-text survives only with >=2 same-shaped competitor spans AND a stem referent",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "69",
     "quote": "Arc-schema stems, paraphrase-matchable stems, and self-evident-cost spans all leaked.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "272",
     "quote": "- Hot-text leaked when the question or span wording signposted the correct phrases.",
     "verbatim": true
    }
   ],
   "against": "The format often works because the answer sits in the text: \"these items work because the answer is literally IN the passage text\" (LANE2_GENERATOR.md line 37).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep",
   "reason": "Quotes verified: 8 of 11 cause items leaked. The LANE2 support comes from a check where the same model family wrote and solved the items, as the against notes.",
   "statement": "Key questions to details only the text holds — who did it, in what order, which source said it — or make the commonsense answer a wrong option; a key that matches the likeliest guess from the story's general shape leaks.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "62",
     "quote": "key is the blind solver's plurality narrative guess dies (8/11 cause leaks, incl.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "64",
     "quote": "referents (event order, actor identity, note provenance) or anti-schema keys where",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE2_GENERATOR.md",
     "lines": "202",
     "quote": "every correct answer depends on a passage-specific invented detail that cannot be retrieved from prior knowledge",
     "verbatim": true
    }
   ],
   "against": "The 100% pass for invented-detail items was a same-family self-check: \"Same-family generation bias (Claude generates + Claude blind-solves) is the one unmitigated risk\" (LANE2_GENERATOR.md line 204).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: the neutral source-attribution design produced the 700 certified items. Nothing supported 'topic words', so it is removed. The against is verified.",
   "statement": "Name sorting categories neutrally (for example Source A, Source B, Both); passage titles used as category labels give the answer away.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "16",
     "quote": "- Passage titles were never used as category labels.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "315",
     "quote": "- Passage titles as categories: titles leak.",
     "verbatim": true
    }
   ],
   "against": "Neutral labels left keys ambiguous where a 'both' category was loosely keyed: \"The control failures were usually partial matches, often 4/5 or 5/6 statements correct.\" (QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md line 132).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep",
   "reason": "Quote verified, but the mechanism rests on a single line of the retrospective. The 94% figure is the format's overall leak rate; nothing ties it to one part giving away the other.",
   "statement": "In two-part answer-plus-evidence items, make sure neither part gives away the other.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "314",
     "quote": "- Sophisticated-option EBSR: Part A/Part B can self-solve.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "41",
     "quote": "| EBSR (corpus) | 1,475 | 94% | 89 |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep",
   "reason": "Quotes verified: all 48 lessons contained the banned item type, and 56 items were ruled off-construct. The against (practise every format on the target test) agrees that the test plan decides.",
   "statement": "Use only item types suited to the learners' level and the target test's blueprint, not every format available.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "56",
     "quote": "the added two-part (Part A / Part B) evidence items are likely developmentally inappropriate for grade 3 — that type generally appears on state tests around grade 4 and above.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
     "lines": "135",
     "quote": "Current: ruled off-construct (~grade-4+), 56 items declared",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/edullm-agent-entrypoint-g3-practical-test-2026-08-06/REPORT.qmd",
     "lines": "36",
     "quote": "- 48/48 lessons include banned G3 EBSR items.",
     "verbatim": true
    }
   ],
   "against": "An earlier design required \"every MAP format practiced\" from the start (g5_build_2026_07_02/approval_clean.md line 290).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep",
   "reason": "Quotes verified: a model answer taught an invented mechanism, a rubric passed the wrong pairings, and five feedback lines contradicted the story. Extends 59 to every string a student sees.",
   "statement": "Fact-check every student-facing string — model answers, feedback, hints, definitions and marking guides — against the source, not only the text and the key.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R3.md",
     "lines": "31",
     "quote": "that light-blocking leads to low oxygen. Canon never states that mechanism.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R3.md",
     "lines": "88",
     "quote": "criterion; a child stating the authored wrong pairs passes. The node's own grounding",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "120",
     "quote": "Five feedback/reveal lines contradict the story",
     "verbatim": true
    }
   ],
   "against": "A true but unsupported addition was rated lower harm: \"Not CRITICAL: the claim is factually true of real\" (g5-course/ADVERSARIAL-REVIEW-2026-08-20-R4.md line 56).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep",
   "reason": "Quotes verified. Two parts under one rule: feedback must not half-concede an overgeneral premise, and a planning target must not pass as a measurement.",
   "statement": "Keep every claim within what the source supports: don't turn one case's outcome into a general truth, and don't present a planned level or an estimate as a measured one.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R3.md",
     "lines": "47",
     "quote": "since restoration always works\" — the feedback half-concedes the distractor's premise.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R18.md",
     "lines": "129",
     "quote": "900L is a provisional planning target, not a measured score or approved readability level.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/02-factuality-claims.md",
     "lines": "22",
     "quote": "child's science text is a kill, not a footnote.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: hints on ~28 word cards pointed to text not yet on screen, and 9 hints referred to a highlight that never appeared. Nothing supported 'control', so it is removed. Generalises the second half of 64.",
   "statement": "Never refer students to a label, code, highlight or line they can't see on the current screen.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "18",
     "quote": "passage, booktag, or heading in this lesson ever names a \"Source C\". It is leaked",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "62",
     "quote": "has not met and cannot see.** Vocab pages come before any passage and render in",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "110",
     "quote": "is ever highlighted.** `grounding` is scorer-only (verified: `SpeakGate`/`ScrItem`",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep",
   "reason": "Quotes verified: the first hint on all 28 cards was the same boilerplate, and a later second hint pointed at light rather than at home. Distinct from 1.",
   "statement": "Make each rung of a hint ladder add information and lead toward what the marking requires; a first hint that restates the task adds nothing, and a hint pointing elsewhere fails the student who follows it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "117",
     "quote": "a restatement of the say_back task the child just failed. Rung 1 adds zero",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-20-R7.md",
     "lines": "119",
     "quote": "correctly from the hint given (\"light\") will say something about light, not about a home or",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "54",
     "quote": "first reworded, and a `reveal` — three scored turns, escalating, ending in the one line allowed",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. Only the R1 line shows one task handing over the answer to a later one. The REGISTER and BUILD-SPEC lines are leaks within the same task, already covered by truths 3 and 1, so they are replaced by the demo unit's case of teaching text answering a later check. A case of truth 3, kept for that evidence.",
   "statement": "Make sure a reveal, hint or teaching text earlier in a lesson does not hand over the answer to a later task in the same lesson.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "84",
     "quote": "pattern in U9-L3 and U1-L6. A child who exhausts the speak's 3 tries is handed the",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
     "lines": "27",
     "quote": "Gradual-release leak: l0/l1 teaching articles pre-answered their certified release checks (must-fix)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "3",
   "name_bearing_source": false
  },
  {
   "index": 35,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. The approved reference lessons do check a just-taught idea on the same page (against, verified), so the rule is limited to independent checks. The five-word threshold is one playbook's choice.",
   "statement": "Keep a worked example and the independent check of the same idea on different screens, and fail any check option that repeats five or more consecutive words of on-screen teaching text.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "86",
     "quote": "The teaching display (example/nonexample) and the independent check may not share a screen",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "301",
     "quote": "word overlap between an option and same-screen teaching text = fail).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
     "lines": "27",
     "quote": "Gradual-release leak: l0/l1 teaching articles pre-answered their certified release checks (must-fix)",
     "verbatim": true
    }
   ],
   "against": "Approved reference lessons check a just-taught idea on the same page: \"Teaching-then-checking on one page is the pattern, not a leak.\" (g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md line 35).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 36,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. The 'could a student pass from one alone' test applies to lessons whose checks are meant to need both text and diagram, so it is narrowed. Labels that say what an element is may stay (against).",
   "statement": "Put no answer text on a picture or diagram, and when a lesson's checks are meant to need both the picture and the text, make sure neither one alone lets a student pass them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "254",
     "quote": "- **The artifact is neutral: no answer text on it.** This is the F1 lesson from the U4L2 build —",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "256",
     "quote": "let a student pass every check without reading the passage, defeating the lesson's entire",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "269",
     "quote": "check from the artifact alone, or from the prose alone? If either answer is yes, the lesson is",
     "verbatim": true
    }
   ],
   "against": "Labels naming what an element is may stay: 'names what an element IS — e.g. \"habitat, not food\" — is contractual and stays' (g5-course/LESSON-AUTHORING-PLAYBOOK.md line 259).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep",
   "reason": "Quotes verified: the review found the model only revealed, the guided step only hinted and the independent step switched skills; later an independent step dropped two of its four steps. Distinct from 40. The against is verified.",
   "statement": "Make modelling, guided practice and independent practice all practise the same process under the same step names; the model must not just reveal the answer, the guided step must not just hint, and the independent step must not switch skills.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "14",
     "quote": "the \"I do\" only reveals the answer instead of modelling the thought process; the \"we do\" only offers a hint; the \"you do\" switches to a different skill (supporting details).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D1-D4.md",
     "lines": "29",
     "quote": "- **Criterion:** D1.6 (Triple-presence: model/guide/release share an identical ordered step list),",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "94",
     "quote": "Never rename a step mid-lesson. The names must survive the strip-the-labels test (they describe",
     "verbatim": true
    }
   ],
   "against": "Keeping the same question from model to guided step was accepted as the house pattern: \"The I-do→we-do handoff keeping the same question is the house release pattern; the\" (g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md line 24).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 38,
   "verdict": "keep",
   "reason": "Quotes verified. The second clause is a principle borrowed from outside research (the audit marks it BORROWED-ACAD).",
   "statement": "Show the tempting wrong choice and why it is rejected inside a worked example, and build worked examples only from steps already taught; teach a new step before it appears in one.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "83",
     "quote": "think-aloud prose that **includes the explicitly rejected alternative** from `decision_point`",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "54",
     "quote": "Worked examples assemble the known — a novel step must be taught before it appears inside one.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "179",
     "quote": "water is not evidence from this text\") is exactly the epistemic move the unit",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 39,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. 'Adds nothing' overstated it: the review's own counter-argument credits repetition with building automaticity, so it is softened. Related to 41.",
   "statement": "When a skill returns in a later lesson, raise the demand — go deeper, apply it to a new domain, or combine it with earlier skills; repeating the same introduction at the same depth adds practice but no new demand.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "115",
     "quote": "Evidence: L6 p12 and L7 p12 contain verbatim-identical skill-intro text:",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "140",
     "quote": "skill identically, not cumulatively. The deeper coordination (e.g., \"find the evidence, then",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/G5-CURRICULUM-OUTLINE.md",
     "lines": "44",
     "quote": "(29 lessons), then at `deepen` phase in a new knowledge domain (26 lessons — the canon's",
     "verbatim": true
    }
   ],
   "against": "Repetition was defended as practice: \"**Adversarial refutation attempt:** This is by design — the FIND skill is practiced in two\" (arc-audit/SIM-REVIEW-D7-D8-D10-D12.md line 129).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 40,
   "verdict": "keep",
   "reason": "Quotes verified. Both are criteria from the review standard; the missing overarching question was rated only a NOTE (against).",
   "statement": "Frame a multi-lesson set of texts with one visible purpose question from the start, and give each lesson's reading purpose before pre-teaching its words.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "153",
     "quote": "Dimension criterion: a visible overarching purpose-question frames a multi-lesson text set from",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "495",
     "quote": "Reading-goal page comes AFTER vocabulary instruction in L5–L7 (vocab gates orientation)",
     "verbatim": true
    }
   ],
   "against": "The missing overarching question was rated a note: \"**Why it is a NOTE, not a finding:** The canopy deficiency is real at the arc-text level (four\" (arc-audit/SIM-REVIEW-D7-D8-D10-D12.md line 170).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep",
   "reason": "Quotes verified: the passage was hidden when evidence was asked for; the wrong passage was pinned and handed to the marker; one pinned excerpt held only distractors.",
   "statement": "Keep the text on screen whenever a task asks for evidence from it, and make sure the part shown is the part that holds the evidence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "45",
     "quote": "Prompts ask students to cite text evidence, but the passage is hidden at that point (\"try looking back at the text\" — but the text is gone).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "76",
     "quote": "WRONG pinned passage, and the open-response scorer is handed that wrong text.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "124",
     "quote": "the pin shows only wrong",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 42,
   "verdict": "keep",
   "reason": "Quotes verified: a browser finished 18 scenes with zero answers; a stamp was earned at ~20% accuracy; a pass came with every answer wrong. This is truth 28 checked in the delivered product (see also 46 and 47). Kept for three independent findings.",
   "statement": "Check in the delivered lesson that each required response is actually required and that its gates block a real miss.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/edullm-agent-entrypoint-g3-practical-test-2026-08-06/REPORT.qmd",
     "lines": "42",
     "quote": "- A browser completed U1·L3's 18 scenes with zero answers and reached the congratulatory ending.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "95",
     "quote": "at about 20 percent accuracy by clicking through without reading, then advanced with the passage hidden from view.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "61",
     "quote": "in a main-idea task we earned the pass while answering every question incorrectly.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "28",
   "name_bearing_source": false
  },
  {
   "index": 43,
   "verdict": "keep",
   "reason": "Quotes verified: most fixes reported 'done & live' were unresolved in the app; one digest's verdicts were all against a stale 11:41 build; leaky items sat in 60 of 81 live forms. Truth 24 applied to fixes; overlaps candidate 3.",
   "statement": "Count a fix only once it is verified in the product as actually served; status reports, clean source pools and stale builds can all differ from what students get.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "3",
     "quote": "most of the items reported as \"done & live\" are not yet resolved in the app",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/build-closing-questions-2026-09-25/verify/DIGEST.md",
     "lines": "42",
     "quote": "every verdict in this digest is against the 11:41 build",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/leaky-vs-gate-unreachability.md",
     "lines": "86",
     "quote": "Pool-purity and gate-purity are separate properties; only the former is satisfied",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "24",
   "name_bearing_source": false
  },
  {
   "index": 44,
   "verdict": "keep",
   "reason": "Quotes verified: ≈0.167 against ≈0.015, and floors are computed from each item's responseDeclaration. The probe limits its own scope (against).",
   "statement": "Probe how the live system actually scores each item shape, and compute guessing floors per item from that, not from the format label.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/scoring-rule-probe-2026-07-10/scoring-rule-probe.md",
     "lines": "60",
     "quote": "submitted array to its **first element** and pays full credit if that single token matches",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/scoring-rule-probe-2026-07-10/scoring-rule-probe.md",
     "lines": "70",
     "quote": "is **k/n_tokens** (e.g. 2 of 12 → ≈ 0.167), not 1/C(n,k) (≈ 0.015) — an order of magnitude",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g3-control-set-2026-07-10/G3-CALIBRATION-REPORT.md",
     "lines": "77",
     "quote": "Standing rule: chance floors are computed per item from its responseDeclaration, never from the",
     "verbatim": true
    }
   ],
   "against": "The probe warns against over-generalising: \"not generalize beyond the probed endpoint and item shapes.\" (scoring-rule-probe-2026-07-10/scoring-rule-probe.md line 8).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 45,
   "verdict": "keep",
   "reason": "Quotes verified: 72 items decertified; at least 8 shuffles; threshold at least 0.20 above the floor. Related to 35, but specific to guessing floors for ordering and selection items.",
   "statement": "Check ordering and selection items without the text under many shuffles, and set the leak threshold well above each item's guessing floor; one shuffle is not enough.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
     "lines": "180",
     "quote": "items certified against one seeded shuffle; multi-shuffle re-probe decertified 72 incl. one",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g3-control-set-2026-07-10/G3-CALIBRATION-REPORT.md",
     "lines": "63",
     "quote": "scored on >=8 shuffles for order/selection formats, with per-format chance floors as computed in",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 46,
   "verdict": "keep",
   "reason": "Quotes verified: 82 items hit a transport limit and were re-run; a broken harness produced 11 phantom FAILs; certification required a full valid set of without-text attempts. Extends 9 from unsure judges to broken checkers.",
   "statement": "Treat a checker error or a missing result as no verdict, and make a broken checker fail loudly rather than report content passes or failures.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/a2-cross-family-regate.md",
     "lines": "50",
     "quote": "a transport limit, not item signal.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "101",
     "quote": "— a broken harness must fail loud, never leak into the walk as phantom content failures",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
     "lines": "50",
     "quote": "leaky never re-rolled, certification requires a FULL valid blind set).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 47,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. The DECISIONS quote wraps across lines 39-40, so the line number is corrected. Three clips played as silence behind a green build; review clips had no text hash; the audit script never read the fields holding a hint leak.",
   "statement": "Make sure every field students see or hear is read by at least one check; unread fields let silent clips, stale audio and hint leaks through a passing build.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/DECISIONS-2026-08-24.md",
     "lines": "39-40",
     "quote": "clips were never checked for existence — three played as silence",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/l4-p3-stale-clip-2026-09-29/README.md",
     "lines": "14",
     "quote": "Class gap: frame `rows[].audio_path` review clips have no `audio_of`, so a definition edit leaves the clip silently stale.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "139",
     "quote": "The audit script (audit.py) never reads think_aloud.states[].search / we_do.search fields at all",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 48,
   "verdict": "keep",
   "reason": "Quotes verified: 8 engine commits landed after content had converged; round 8 found two criticals; one fix broke a field it didn't need to touch. Related to 70.",
   "statement": "Re-review after every change — including fixes and changes to the code that displays unchanged content — because each new surface can bring new critical faults.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-21-R8.md",
     "lines": "10",
     "quote": "*content* surface; this round exists because 8 new engine commits landed after R7's base.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-21-R9.md",
     "lines": "6",
     "quote": "the loop's rule is that a fix commit gets fresh eyes before the loop may claim convergence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-20-R7.md",
     "lines": "133",
     "quote": "is exactly the defect class this round was asked to hunt: a fix that solved its target problem",
     "verbatim": true
    }
   ],
   "against": "Re-review is scoped to what changed: the loop rule \"a lens never runs twice on unchanged content\" (g5-course/ADVERSARIAL-REVIEW-2026-08-20-R6.md lines 9-10).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 49,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: rounds 1 to 5 found 5, 5, 5, 1 and 1 critical faults, and round 6 found none. 'Outside expert' named a job role and the student walk was misdescribed, so the statement is rewritten.",
   "statement": "Run review rounds through changing lenses — a student walk that gets everything right and one that gets every gated item wrong twice, a line-by-line check against the source, a simulated first read by an outside reader, and a comparison with an already shipped course — since each new lens found critical faults the earlier ones missed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "4",
     "quote": "(a) gets everything right, (b) gets every gated item wrong twice before recovering.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R3.md",
     "lines": "19",
     "quote": "Totals: **5 CRITICAL / 2 WORTH-FIXING / 1 POLISH.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-20-R4.md",
     "lines": "178",
     "quote": "| CRITICAL | 1 (U1-L6 item-4-evidence self-negating keyed answer) |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 50,
   "verdict": "keep",
   "reason": "Quotes verified: 28 of 28 cards against 12 of 12; a shared prompt hard-coded a third grader; ported code assumed a field the new course never had. The against is verified.",
   "statement": "When content or display code is shared or ported between courses or levels, compare conventions one by one and check what the shared code assumes; silent departures and level-specific wording slip through.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-20-R5.md",
     "lines": "45",
     "quote": "established on every card, course-wide (28/28 G5 cards vs 12/12 G4 cards).**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-15-R22.md",
     "lines": "34",
     "quote": "#503 fragment rule (`oneWordRule`): **hardcodes \"a sentence a third grader could say",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-21-R8.md",
     "lines": "35",
     "quote": "(`station`) that G5 never authored, and the fallback silently produces a worse UI than what it",
     "verbatim": true
    }
   ],
   "against": "Differences licensed by content are not defects: \"licensed by different canon, different genre (continuous Odyssey narrative vs. four\" (g5-course/ADVERSARIAL-REVIEW-2026-08-20-R5.md line 11).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 51,
   "verdict": "keep",
   "reason": "Quotes verified. A later replay (R24/R26) confirmed that a short-phrase first answer scored nothing. The harm was bounded (against).",
   "statement": "Make the marker's rules agree with what the question asks; a rule rejecting short fragments failed students who quoted a short phrase exactly as told.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-16-R25.md",
     "lines": "48",
     "quote": "So a Grade-5 child who does exactly what the stem asks, \"Quote a short",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "152",
     "quote": "the speak-score route's fragment gate keys on it, so a one-word answer would have been refused",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
     "lines": "117",
     "quote": "The blank's own acceptance rules disagree",
     "verbatim": true
    }
   ],
   "against": "The harm was bounded: \"Not CRITICAL because the child who then\" (g5-course/ADVERSARIAL-REVIEW-2026-09-16-R25.md line 53).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 52,
   "verdict": "keep",
   "reason": "Quotes verified: overlap of 84/114 = 0.74 against a 0.70 threshold on three pages, and the message was false because the sentence was hidden.",
   "statement": "When checking for copying, compare a student's words only with text the student was shown; counting the marking guide's own wording rejected word-perfect recall.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/build-closing-questions-2026-09-25/verify/DIGEST.md",
     "lines": "23",
     "quote": "contains the sentence at 84/114 = 0.74, threshold 0.70",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/build-closing-questions-2026-09-25/verify/DIGEST.md",
     "lines": "29",
     "quote": "is false to the child because the sentence is hidden on p0b.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-16-R26.md",
     "lines": "18",
     "quote": "a criterion states the standard, it does not quote the",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 53,
   "verdict": "keep",
   "reason": "Quotes verified. Follows from 34, but adds the rule: run the first judgment at the most deterministic setting and return the stored verdict for an identical resubmission.",
   "statement": "Give an identical answer the same mark every time; judging a resubmission afresh gave one answer 'Almost' and then full credit.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/baseline-submission/CHANGES-FOR-REVIEW-L4-2026-08-31.md",
     "lines": "33",
     "quote": "An identical typed answer now always returns the same verdict",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/baseline-submission/CHANGES-FOR-REVIEW-L4-2026-08-31.md",
     "lines": "107",
     "quote": "an identical resubmitted answer now returns the same verdict instantly instead of a fresh judgment",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 54,
   "verdict": "keep",
   "reason": "Quotes verified: every multi-select item printed 'Yes.' next to the revealed answer after failed tries, and a later rule says running out of tries is not passing.",
   "statement": "Once the answer has been shown after failed tries, show no praise; the screen must not say 'Yes' to a student who was just given the answer.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-27-R12.md",
     "lines": "39",
     "quote": "child who just failed to the floor read \"Yes.\" — unearned praise contradicting the",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-15-R23.md",
     "lines": "53",
     "quote": "running out of tries is not passing",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 55,
   "verdict": "keep",
   "reason": "Quotes verified: help is recorded as help; lesson-end summaries named words the lesson never taught; the rule is completion, never mastery.",
   "statement": "Record whether a student solved an item alone or with help, and let summaries list only what actually happened — completion, never mastery.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "234",
     "quote": "and the receipt records it as practiced-with-help, never as solved-alone.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "33",
     "quote": "moment and it names the wrong trophies. No validator compares receipt words to",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "228",
     "quote": "3. **Completion, never mastery.** No string anywhere claims mastery, certification, approval,",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 56,
   "verdict": "keep",
   "reason": "Quotes verified: points only for an attempted scored check, and a non-blocking nudge was skipped by clicking Next twice. Related to 28 and candidate 42.",
   "statement": "Count a lesson as done only when its checks were actually attempted, and make attention prompts blocking; points for volume and skippable nudges reward clicking through.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "42",
     "quote": "\"honest completion\" = XP only on a scored check",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "289",
     "quote": "\"Done\" counts only when the check is *attempted* (honest completion).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "35",
     "quote": "where a \"not so fast — read, read\" nudge appeared it was non-blocking and skipped by clicking Next twice.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 57,
   "verdict": "keep",
   "reason": "Quotes verified: ~17% clear a 90% bar. Staging the bar is a design response to that number, not a measured effect.",
   "statement": "Stage high mastery bars — advisory at first, blocking later — because a flat high bar from the start leaves most learners no way in.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "273",
     "quote": "a flat wall on the on-ramp has no path for the other 83%.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
     "lines": "147",
     "quote": "- **Only ~17% of students clear a 90% mastery bar** under the incumbent design (page 2). Our",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 58,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: 64% fell to 41%. A harder retry will score lower anyway, so the drop shows more failure, not less learning; reclassified as an adopted rule, and a line on protecting confidence and dosage is added. No conflict with 4, which is about tries within one item.",
   "statement": "After a miss, reteach and retry on a parallel item of the same difficulty; never escalate difficulty after a failure or re-serve the identical item.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "46",
     "quote": "Data-derived: the incumbent's harder-on-retry drops supporting-details 64%→41% (−22.6pt)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "310",
     "quote": "**Never re-serve the identical item; never hand a harder item after failure.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "314",
     "quote": "The incumbent's retry path escalates difficulty and measurably destroys attempt-2 accuracy (supporting-details 64% → 41%). Reteach-first protects confidence AND dosage.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 59,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. The person-named instruction-model file is replaced by approval_clean line 318, where a review found one instrument doing both jobs. Close to 48; kept for the design detail that growth items are held out, never practised and never gated.",
   "statement": "Never use the instrument that gates progress as the measure of growth; measure growth on held-out items that are never practised or gated.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "318",
     "quote": "A v1 seam the adversarial review found: the same instrument was being used as both the mastery gate and the growth measure. Rev 2 separates them.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "321",
     "quote": "We never teach to or gate on it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "53",
     "quote": "Platforms that collapse the two masteries (acquisition vs durable) into one binary gate either over-reteach or under-practise",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "48",
   "name_bearing_source": false
  },
  {
   "index": 60,
   "verdict": "keep",
   "reason": "Quotes verified: support is on in practice steps and off in scored ones, and supports that never fade teach dependency. The video tension in the against is only loosely related.",
   "statement": "Offer supports while students learn but switch them off for scored checks, and fade engagement supports before test conditions so they don't become crutches.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "330",
     "quote": "### Insight 7 — Word Assist boundary: practice on, scored off",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "332",
     "quote": "every scored item is a clean cold-condition measure",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "147",
     "quote": "• Permanent illustration/character wrapper — engagement scaffolds must fade to cold plain text or they teach dependency.",
     "verbatim": true
    }
   ],
   "against": "Whether video belongs at all stayed contested: \"This is a genuine, load-bearing tension\" (wiki-research/cross-cutting.md line 141).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 61,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: the test publisher invalidates tests above 25% rapid guessing (external research). 'Treat as invalid' is tightened to what the source does, which is flag the score past a threshold.",
   "statement": "Don't time a task unless speed is what it measures, but log response times quietly and flag scores with heavy rapid guessing as invalid.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "265",
     "quote": "rewards rapid-guessing, which MAP penalizes.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/mapproxy_clean.md",
     "lines": "211",
     "quote": "NWEA invalidates tests above 25% rapid-guessing; disengagement deflates scores (Wise & DeMars 2005).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 62,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. Nothing supported 'never longer than the item'; the sources compare feedback with the passage and with the original instruction. Overlaps 26 and 1.",
   "statement": "Keep corrective feedback short — feedback longer than the passage goes unread — and if correcting a response takes more than the original instruction did, fix the item or its placement rather than the feedback.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "12",
     "quote": "Corrective feedback now appears on many wrong answers, but it is far too long — at times longer than the passage itself (see the attached \"Nibbles\" warm-up)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "52",
     "quote": "If the feedback needed to correct a response is longer and more complex than the original instruction, the ITEM has crossed the acquisition boundary — fix the item or the placement, not the feedback.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "201",
     "quote": "evidence-anchored, ≤40 words target, never >60 (G5-POL-INS-008); wrong-",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 63,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: two pages had drifted 16 lines into paraphrase. The playbook quote is on line 60, not 61. The one-way rule in the against is consistent with the statement.",
   "statement": "Print everything that is spoken on the same screen, sentence for sentence, so the lesson still works with audio off.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "59",
     "quote": "- Nothing is spoken that is not printed on the same page, sentence for sentence — a spoken line",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "61",
     "quote": "exists because two pages drifted 16 lines into paraphrase).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "60",
     "quote": "readable on screen. Read-aloud is OFF by default at G5: the lesson must be 100% followable",
     "verbatim": true
    }
   ],
   "against": "The rule runs one way: \"read-along rule runs one way; printed-but-unspoken is\" (g5-course/G3-U1-L4-RESIDUAL-ADJUDICATION-2026-08-21.md line 90).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 64,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: a stale review clip; 117–179 narrated strings orphaned by a rewrite; a reverted pronunciation caught by a transcript check. Added the standard's own hash and transcript rules. The QC report's path names a book title, not a person.",
   "statement": "After any text edit, re-check its narration: tie each clip to a hash of its text and transcribe the clip back against the text.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/l4-p3-stale-clip-2026-09-29/README.md",
     "lines": "7",
     "quote": "**STALE** (older definition)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "185",
     "quote": "one real lesson had 117-179 narrated strings orphaned by a same-day rewrite whose",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/qc-run-2026-09-04/QC Run Report — Peter Pan L4-L7 + G5 (2026-09-04).md",
     "lines": "28",
     "quote": "the 02.09 course-tts re-voice then cut the regressed text. Whisper part-read check caught",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "62",
     "quote": "- Clip hashes must match the authored text (`audio_of` on `voiceover.text` alone), so silent",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "107",
     "quote": "every cut is followed by listen-qa: whisper transcript against authored text",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 65,
   "verdict": "keep",
   "reason": "Quotes verified. The second run used tightened criteria, so two of the three changed verdicts may come from the tightening. The clean sign of instability is vf07, which got a softer verdict under stricter criteria, and the record still concludes single reads are unreliable. Builds on 22, 34 and 38.",
   "statement": "Check generated pictures of people with several independent reads and a planted control, rejecting ones that look machine-made; single reads were unstable.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "7",
     "quote": "Purpose: prove the new check DISCRIMINATES — fires on AI-generated film frames with humans, stays",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "42",
     "quote": "Runs 1 and 2 disagreed on vf07 (FAIL → note), vf08 (note → FAIL) and vf10 (note → FAIL) — the",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
     "lines": "45",
     "quote": "now requires three independent reads with majority rule on film frames and near-photoreal humans.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 66,
   "verdict": "keep",
   "reason": "Quotes verified; the gap was judged minor (against).",
   "statement": "Label adapted, retold or newly written text as such on the page where it is read, so no one mistakes it for the original.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R17.md",
     "lines": "140",
     "quote": "written and labeled an adaptation, not a quotation or original chapter.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R18.md",
     "lines": "73",
     "quote": "an explicit attribution `booktag` on the reading page itself (not only on a later evidence/reference",
     "verbatim": true
    }
   ],
   "against": "The gap was judged minor: \"No child is actively misled by this gap (L1 establishes context; meaning is preserved); no CRITICAL\" (g5-course/ADVERSARIAL-REVIEW-2026-09-08-R17.md line 144).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 67,
   "verdict": "keep",
   "reason": "Quotes verified: three redundant guards, in the rubric, the instructions and the closing summary.",
   "statement": "Credit only what was shown in the mode being assessed; a written plan is not evidence of a spoken performance.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R18.md",
     "lines": "131",
     "quote": "\"Do not infer actual oral performance from typed claims\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R18.md",
     "lines": "134",
     "quote": "\"Your written explanation does not by itself prove spoken delivery.\"",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 68,
   "verdict": "keep",
   "reason": "Quotes verified: the mislabel was confirmed 2 to 1. Students see no effect (against); it is a data-integrity rule.",
   "statement": "Name the thinking a lesson models by reading the definitions of the available labels, never by picking the nearest accepted label to pass a validator.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/CAPSTONE-PROCEDURE-RULING-2026-08-18.md",
     "lines": "43",
     "quote": "Labelling that WEIGH would be mislabelling to satisfy a validator, which is exactly the",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-25-R10.md",
     "lines": "70",
     "quote": "carried `procedure: \"CONNECT\"` for a trace with nothing related.",
     "verbatim": true
    }
   ],
   "against": "The relabel had no visible effect for students: \"the D25 chrome decision means the procedure value renders no child-visible chip, so the relabel\" (g5-course/ADVERSARIAL-REVIEW-2026-08-25-R10.md line 62).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 69,
   "verdict": "keep",
   "reason": "Quotes verified: findings went from 28/12 to 15/8 partly because detection was disabled, and a word inserted to pass a validator was reverted. The against is verified.",
   "statement": "Never alter content or weaken a check just to make a build pass; fewer findings from a weakened check are not progress.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/takeover-audit-2026-07-13/g5-clean-baseline.md",
     "lines": "146",
     "quote": "More importantly, the uncommitted linter edit reduces findings by weakening the gate:",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/takeover-audit-2026-07-13/g5-clean-baseline.md",
     "lines": "152",
     "quote": "Therefore, `28/12 -> 15/8` is a mix of real cleanup and disabled detection. It cannot be used as progress toward approval.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/DECISIONS-2026-08-24.md",
     "lines": "33",
     "quote": "that is editing someone else's lesson to satisfy our validator, and was",
     "verbatim": true
    }
   ],
   "against": "Bending content to a checker is sometimes chosen, but recorded as such: \"Honest, but it is content bent to an engine\" (g5-course/ADVERSARIAL-REVIEW-2026-09-16-R25.md line 66).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 70,
   "verdict": "keep",
   "reason": "Quotes verified. The ≥15 bar was the top of an 8–15 target band, cited circularly (audit-heuristic-finding lines 25 and 40-42); against the real floor of 8, 79 of 81 pass.",
   "statement": "Trace every threshold a check enforces to its source before failing content on it; a gate without a sourced reason is a preference.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/audit-heuristic-finding.md",
     "lines": "8",
     "quote": "The `>=15` bar is an **arbitrary auditor heuristic**, not a",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/audit-heuristic-finding.md",
     "lines": "82",
     "quote": "- Against the **correct floor of 8**: **79/81 pass**; **2 fail**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "168",
     "quote": "a gate without provenance is a preference, and preferences don't gate.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 71,
   "verdict": "keep",
   "reason": "Quotes verified: a mistagged lesson passed the lint, and one skill measured 9.7% against the heuristic's 2%, about 5×. An instance of 43; kept for the lint calibration evidence.",
   "statement": "A check that trusts the writer's own skill labels cannot catch a wrong label; classify what each item actually asks independently.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/op-taxonomy-calibration.md",
     "lines": "68",
     "quote": "The mistag IS the failure, so deterministic rules that consume tags cannot see it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
     "lines": "51",
     "quote": "Tagging still does not match what items assess.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/Grade 3 Reading - Proposal Review & Synthesis.docx",
     "lines": "164 (textutil plain-text output)",
     "quote": "inference was 5× undercounted by the heuristic (actually 9.7%, not 2%)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "43",
   "name_bearing_source": false
  },
  {
   "index": 72,
   "verdict": "keep",
   "reason": "Quotes verified: a lesson that switched skills under one shared label passed the full lint.",
   "statement": "Make the skill list a check uses fine enough to separate the skills a lesson might confuse; when two skills share one label, switching between them passes every check.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/op-taxonomy-calibration.md",
     "lines": "46",
     "quote": "| fc-04b-skill-switch-collapsed-tag.json | PASS | (none - taxonomy blind spot, see fc-04) |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/op-taxonomy-calibration.md",
     "lines": "84",
     "quote": "skill switch is inexpressible - measured: `fc-04b-skill-switch-collapsed-tag.json`",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 73,
   "verdict": "keep",
   "reason": "Quotes verified. Settling a conflict by an order of authority is itself a recorded decision (against).",
   "statement": "When sources or reviews set incompatible rules, record both and decide once with a recorded ruling, instead of silently picking one or changing content piecemeal.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/edullm-standards-centralization-2026-08-05/IMPLEMENTATION-PLAN.md",
     "lines": "227",
     "quote": "### F5 - conflict is silently flattened",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/decision-brief-2026-09-10/DECISION-BRIEF.md",
     "lines": "43",
     "quote": "*requested* the \"The story says / so my answer is\" frame the 09-10 report proposes replacing.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "115",
     "quote": "Rulings are dated; a newer ruling beats an older register; contradictions between reviewers go",
     "verbatim": true
    }
   ],
   "against": "Some conflicts are settled by an authority order: \"- **D4 — RULED: the ladder wins.** Per-lesson docs outrank the generic spec (tier rule);\" (DECISIONS-2026-08-24.md line 118).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 74,
   "verdict": "keep",
   "reason": "Quotes verified; the standard is only a draft (against).",
   "statement": "Turn each piece of review feedback into a dated rule or an automated check, so the same kind of comment never has to be made twice.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "26",
     "quote": "> **No reviewer ever makes the same class of comment twice.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/baseline-submission/CHANGES-FOR-REVIEW-L4-2026-08-31.md",
     "lines": "28",
     "quote": "shared over and over and continues not to be implemented",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/baseline-submission/CHANGES-FOR-REVIEW-L4-2026-08-31.md",
     "lines": "97",
     "quote": "We also added an automated check so a long opener like this cannot land again without being caught before it reaches you.",
     "verbatim": true
    }
   ],
   "against": "The standard itself was only a draft: \"Not shared, not adopted, binds nobody.\" (team-direction-2026-09-09/GATE-STANDARD-DRAFT.md line 5).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 75,
   "verdict": "keep",
   "reason": "Quotes verified. The second quote is a weaker rule, about defining success before building a prototype.",
   "statement": "Write a plan for each lesson before authoring it, review the built lesson against the plan, and record why each item format was chosen.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
     "lines": "81",
     "quote": "- One plan per lesson, written before authoring, reviewed against the built lesson after; the",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/04-evidence-contract.md",
     "lines": "3",
     "quote": "Per `eval-contract`, define success before building the prototype.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 76,
   "verdict": "keep",
   "reason": "Quotes verified: a principle borrowed from direct-instruction guidance. Refines 2.",
   "statement": "Leave hedging words out of student-facing instructions; they add processing load without adding information.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "50",
     "quote": "Hedged language is not politeness, it is load: 'might', 'maybe', 'a little' are excluded because they add processing cost without information.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "205",
     "quote": "representation CANNOT show (\"Neither source named the fish's diet\"), without hedging into",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 77,
   "verdict": "keep",
   "reason": "Quotes verified; the finding was graded as polish only (against).",
   "statement": "Make praise name what the student's move accomplished; identical generic praise becomes wallpaper.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "198",
     "quote": "Praise is specific process praise naming what the student's move accomplished",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "127",
     "quote": "lesson three the trophy is wallpaper. The `did`/`now` lines are honest and specific",
     "verbatim": true
    }
   ],
   "against": "It was graded as polish only: \"**P-1. POLISH — all nine receipts are the identical \"You did it!\" + gold medal.**\" (g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md line 126).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 78,
   "verdict": "keep",
   "reason": "Quotes verified. Mechanisms may carry across levels (against) while the content stays specific to each level.",
   "statement": "Author content for each level from that level's own sources, putting the difficulty in the task rather than in inflated prose; never reuse a lower level's lesson with harder words.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "53",
     "quote": "3. **Genuinely G5, never G3 dressed up.** Complexity lives in the task, not inflated prose. The",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "171",
     "quote": "`item-2-cards` distractors are below band.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-book-2026-09-29/SCOUT-AND-PLAN.md",
     "lines": "12",
     "quote": "\"never a Grade 3 copy; consult the canon; log the rule behind each decision\"",
     "verbatim": true
    }
   ],
   "against": "Mechanisms may carry across levels unchanged: \"(1) ALL G3-acquired mechanisms carry to G5 as-is\" (g5-book-2026-09-29/BUILD-SPEC-G5-U1-L1.md line 4).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 79,
   "verdict": "keep",
   "reason": "Quote verified; a single ruling that states a general principle.",
   "statement": "Keep the case used to model a skill out of every assessed item, and assess on new material.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/AUTHORING-RULINGS-R1-R10.md",
     "lines": "80",
     "quote": "The kitchen/greenhouse/classroom modelling case never appears inside an assessed item.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 80,
   "verdict": "keep",
   "reason": "Quotes verified: a ~204-word part with eight new names and options of 50–70 words; four reading pages with no interaction; narrated chunks of 241–279 words.",
   "statement": "Limit the reading load at each step — new names per section, length of answer options, and stretches of reading without a check.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "43",
     "quote": "~204-word part introduces EIGHT new proper names (Juniper, Vela, Nori, Moss, Lark,",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "258",
     "quote": "- **W-11. WORTH-FIXING — four consecutive reading pages with no interaction",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D7-D8-D10-D12.md",
     "lines": "493",
     "quote": "3 passage chunks exceed 60s passive during autoplay narration",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 81,
   "verdict": "keep",
   "reason": "Quote verified; it rests on a single finding.",
   "statement": "Don't reuse one name for a different kind of thing across lessons read in sequence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19.md",
     "lines": "105",
     "quote": "same tokens keep changing referent class. Cheap to fix (rename L6's sources or L4's",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 82,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified. Added the 'tap the two sentences' finding (R2 lines 158-159), which found_by cites but the evidence lacked.",
   "statement": "Write instructions a literal reader can follow: the verb must match the action, the units must match what can be selected, and a fill-in frame must stay grammatical for every allowed answer.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "172",
     "quote": "selection verb on a free-writing box; a child looks for four sentences to pick.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
     "lines": "159",
     "quote": "the child taps three-sentence paragraph blocks.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/baseline-submission/CHANGES-FOR-REVIEW-L4-2026-08-31.md",
     "lines": "32",
     "quote": "frame breaks grammar ('has a enchanting')",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 83,
   "verdict": "keep",
   "reason": "Quotes verified: one item offered twelve options; 137 of 772 items were over a cap of 5; a one-screen check found tasks running past the fold. The QC report's path names a book title, not a person.",
   "statement": "Cap the number of selectable options in an item and keep each task on one screen without scrolling at the target display size.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "103",
     "quote": "one hot-text item offered twelve selectable options, an excessive motor and cognitive load for an eight-year-old.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/option_cap_report.md",
     "lines": "7",
     "quote": "- items over cap: **137**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/qc-run-2026-09-04/QC Run Report — Peter Pan L4-L7 + G5 (2026-09-04).md",
     "lines": "31",
     "quote": "### 3. HIGH — one-screen census, our lane (additions row I/census)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 84,
   "verdict": "keep",
   "reason": "Quotes verified: 52 lessons, 745 items and 56 passages in one document against 47 and 713 in another; one named, dated pull made binding.",
   "statement": "Take every count in every document about a course from one named, dated data pull, and generate the documents from one source.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "111",
     "quote": "The email says 52 lessons, 745 items and 56 cold passages; the infographic says 47 lessons and 713 graded items",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
     "lines": "18",
     "quote": "- Every count in every doc must trace to one named pull with a date.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/takeover-audit-2026-07-13/g5-clean-baseline.md",
     "lines": "160",
     "quote": "should be derived from one structured source rather than hand-edited independently.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 85,
   "verdict": "keep",
   "reason": "Quotes verified: documents drifted (0.930 against 0.928), so unsupported score scales were blocked in code.",
   "statement": "Enforce limits on claims in code: a score the evidence can't yet support should not appear in the output at all.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/mapproxy_clean.md",
     "lines": "161",
     "quote": "RIT, percentile, and CGP are **blocked in the engine**.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/mapproxy_clean.md",
     "lines": "163",
     "quote": "The two audits found number-drift in our *documents* (0.930 vs 0.928)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 86,
   "verdict": "keep",
   "reason": "Quotes verified: students practised only on multiple choice, while over 30% of the target test used other formats.",
   "statement": "Let students practise the item formats they will be tested on, because an unfamiliar interface adds noise to the score.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/mapproxy_clean.md",
     "lines": "179",
     "quote": "Interface novelty is construct-irrelevant variance (AERA/APA/NCME Standard 1.13).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "47",
     "quote": "B is the only one to flag that live course is 100% MCQ while MAP is >30% tech-enhanced",
     "verbatim": true
    }
   ],
   "against": "Format practice can inflate internal growth readings: \"so a rise isn't format-practice inflation.\" (g5_build_2026_07_02/approval_clean.md line 321).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 87,
   "verdict": "keep-with-fix",
   "reason": "Quote verified. The benchmark was fine; the analysis of it was wrong, so the statement is reworded. Added the docx's own account (line 86) and non-name corroboration (GOAL line 9: the benchmark's informational-reading share was 0, with 68% grammar).",
   "statement": "Before building toward a target test, check your analysis of what it measures against its published blueprint; a pipeline bug can silently drop a whole domain and point a course at the wrong skills.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/Grade 3 Reading - Proposal Review & Synthesis.docx",
     "lines": "88 (textutil plain-text output)",
     "quote": "produced by a pipeline bug that dropped the entire RI domain",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/Grade 3 Reading - Proposal Review & Synthesis.docx",
     "lines": "86 (textutil plain-text output)",
     "quote": "not phonics/grammar/conventions, which a broken curriculum API had falsely elevated to 68% of the course focus",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md",
     "lines": "9",
     "quote": "the incumbent's own 684-item benchmark shows a high-fidelity proxy of the WRONG construct (RI=0, 68% grammar) is worse than useless",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 88,
   "verdict": "keep",
   "reason": "Quotes verified: about 30% of intended work done, 12.5% median completion, 83% accuracy on attempted items. That 83% was itself inflated by easy items (against).",
   "statement": "Before redesigning the teaching, check how much of the intended work learners actually do; low completion can be the binding problem rather than low accuracy.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "42",
     "quote": "Dosage is the measured #1 problem (12.5% completion, 7.6/25 min, ~0 acceleration)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "243",
     "quote": "The completion floor — 12.5% — is much further from acceptable than 39% is.",
     "verbatim": true
    }
   ],
   "against": "The accuracy baseline came from easy items: \"the wrong-instrument correction of the 83% baseline\" (team-direction-2026-09-09/DIRECTION-2026-09-09.md line 89).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 89,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: 120 lessons, 12.5% median completion, failure starting around lesson 32. One course does not show that long courses collapse in general, so the claim is softened.",
   "statement": "Size a course to the length learners actually complete, measured on the existing course, rather than to the content you want to cover.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/Grade 3 Reading - Proposal Review & Synthesis.docx",
     "lines": "192 (textutil plain-text output)",
     "quote": "the completion failure starts at ~32 lessons in the current course",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/Grade 3 Reading - Proposal Review & Synthesis.docx",
     "lines": "585 (textutil plain-text output)",
     "quote": "The incumbent has 120 lessons and 12.5% median completion.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 90,
   "verdict": "keep",
   "reason": "Quote verified: passages ran 58 to 217 words, about 166 on average.",
   "statement": "Build text length up toward what learners will eventually need to read; mastering short snippets never trains sustained reading.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "69",
     "quote": "A child can master the whole course one short snippet at a time and never once sustain attention across a multi-passage block.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 91,
   "verdict": "keep-with-fix",
   "reason": "Quotes verified: all 48 lessons used a single read. That finding shows an absence, not an effect, so this is an adopted rule resting on a research principle. The quote is trimmed to drop a researcher's name.",
   "statement": "Build purposeful rereads into each lesson rather than one read followed by questions.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/edullm-agent-entrypoint-g3-practical-test-2026-08-06/REPORT.qmd",
     "lines": "39",
     "quote": "- 48/48 lessons use a single explicit read pass.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
     "lines": "137",
     "quote": "5. How the text is READ is instruction, not delivery",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 92,
   "verdict": "keep",
   "reason": "Quotes verified.",
   "statement": "Have lessons say plainly what a source cannot show, and model refusing inferences it doesn't support.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
     "lines": "206",
     "quote": "vagueness and without overclaiming. Model honest refusal of unsupported inferences.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/03-transfer-practice-layer.md",
     "lines": "71",
     "quote": "- explain why an option is unsupported;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 93,
   "verdict": "keep",
   "reason": "Quotes verified, but only in a person-named proposal folder. The same pairing recurs in several other person-named proposals and in no non-name file I found. It is a proposal design, never measured. Refines 6.",
   "statement": "In inference questions, set a text-supported answer against one that is true in the world but unsupported by the text, and key the supported one even when the other is factually true.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
     "lines": "80",
     "quote": "every inference CFU pairs \"supported by the text\" vs \"true but not supported,\" and the correct answer is the one with explicit line support **even when the alternative is factually true.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/course-skeleton.md",
     "lines": "46",
     "quote": "Inference ~33–36% of items via evidence-bounded \"supported vs true-but-unsupported\" pairs.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 94,
   "verdict": "drop",
   "reason": "Quotes verified, but the only evidence is a person-named proposal, and the effect it claims was never measured. The non-name synthesis says p_m ≥ 0.90 'is a target we measure, not a property we ship' and keeps calibration observe-only. Difficulty that comes from taught knowledge also falls inside the open tension in candidate 111: the spine and without-text gates reject items that prior knowledge can answer.",
   "statement": "Make items hard through the knowledge the lesson taught rather than through subtle distractors, so a student who learned it finds the item easy and a surface guesser is trapped; revise or retire items that true masters miss.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
     "lines": "95",
     "quote": "We hold both by sourcing difficulty from the **knowledge gate, not distractor subtlety**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/course-skeleton.md",
     "lines": "35",
     "quote": "per-item p_m measured on real masters (drifters retired)",
     "verbatim": true
    }
   ],
   "against": "The success target could not yet be measured: \"is a target we measure, not a property we ship.\" (g5_build_2026_07_02/approval_clean.md line 326).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 95,
   "verdict": "keep",
   "reason": "Quotes verified: six of the eight proposals adopted it. Scripted student walks test the lesson flow, not learning (against).",
   "statement": "Use a model to predict where students will stumble, but don't treat its simulated answers as evidence of how students learn.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "51",
     "quote": "LLM as expert-predictor not student-simulator",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "131",
     "quote": "expert-predictor not student-simulator. Six of eight (A–F) sit inside this cluster.",
     "verbatim": true
    }
   ],
   "against": "Scripted student walks are still used to test the flow: \"The contract gates read the JSON; the walker plays the lesson as a student against the live app\" (team-direction-2026-09-09/GATE-STANDARD-DRAFT.md line 91).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 96,
   "verdict": "keep",
   "reason": "Quotes verified: 0 of 313 overlap. The 409 MAP records found later (against) still had no crosswalk to the cohort.",
   "statement": "Claim the direction of an expected effect, not its size, until the outcome has been measured on the same learners.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "259",
     "quote": "refuse to put a number on RIT until an in-cohort MAP pilot exists",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/X1_staar_map_overlap_probe_2026_06_16.md",
     "lines": "17",
     "quote": "it's a measured void, not an assumed one",
     "verbatim": true
    }
   ],
   "against": "Later data partly changed the picture: \"old: no bridge possible (0/313 overlap). Current: 409 real G3 MAP RIT records\" (wiki-research/pedagogy-llm-evals.md line 130).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 97,
   "verdict": "keep",
   "reason": "Quotes verified: a perfect structure score went with 100% blind-solvable, and only 4 of 13 passed the quality rubric. Related to 58.",
   "statement": "Treat structural quality, text dependence and teaching quality as separate properties, each with its own check.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/GENERATOR_DIRECTIVE.md",
     "lines": "34",
     "quote": "**IB = 1.0. Blind-solve = 100%.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/GENERATOR_DIRECTIVE.md",
     "lines": "44",
     "quote": "Structural quality and passage-dependency are **orthogonal**. Both must be in the signal.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
     "lines": "84",
     "quote": "- only 4/13 passed the LLM quality-B rubric",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 98,
   "verdict": "keep",
   "reason": "Quotes verified: a 772-item course with perfect item scores but 90% blind-solvable, and a Lexile ramp from 830 to 1010L. Related to 60.",
   "statement": "Judge a course as a whole — coverage, difficulty ramp, balance against the test plan, distinct forms — not by its average item score.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/GENERATOR_DIRECTIVE.md",
     "lines": "13",
     "quote": "A 772-item course where every item scores IB 1.0 but 90% are blind-solvable is a **failed course**.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/GENERATOR_DIRECTIVE.md",
     "lines": "100",
     "quote": "- Lexile ramp **830 → 1010L**.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 99,
   "verdict": "keep",
   "reason": "Quotes verified: units sat flat at ~900–913L; one build grouped by Lexile band; the external review called the course a staircase.",
   "statement": "Sequence a course by both knowledge and difficulty; grouping by standard alone left difficulty flat, and grouping by difficulty band alone left no knowledge progression.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "208",
     "quote": "Units are organized by CCSS domain, not by difficulty progression.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md",
     "lines": "40",
     "quote": "groups by LEXILE band (830/920/1010L), not topic coherence; no knowledge progression exists",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "43",
     "quote": "The course is sequenced as a Lexile staircase, not a knowledge progression",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 100,
   "verdict": "keep",
   "reason": "Quotes verified: 15 zero-coverage codes closed to 0 by reading each item; 61 of 82 rated Low; carried skills held out rather than placed where they don't fit.",
   "statement": "Prove each standard is covered by reading the scored item against the standard's boundary, count depth rather than mere presence, and never place a skill in a slot it doesn't fit just to close a gap.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/CURRICULUM-REVIEW-STANDING-2026-08-17.md",
     "lines": "81",
     "quote": "reading the actual scored item (not just relabeling a slot).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/GAP-ANALYSIS-2026-08-18.md",
     "lines": "49",
     "quote": "but 61/82 rated \"Low\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/RULING-B-CARRIED-MASTERY.md",
     "lines": "20",
     "quote": "without being counted as coverage zeros, and without fake-placing them into slots they don't",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 101,
   "verdict": "keep",
   "reason": "Quotes verified: the generator was set to grade 11 for a grade-3 course. That setting came from an AP US History pipeline (GOAL line 47), which also supports truth 63.",
   "statement": "Screen every generated text for age-appropriateness and sensitive content, and check the generator's target-level setting, before any student sees it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "328",
     "quote": "MANDATORY on every auto-generated passage before it can reach a child",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "328",
     "quote": "fix the generator's grade setting (currently grade 11 → grade 3",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
     "lines": "194",
     "quote": "Safety items (S1, S2) test refusal behavior: S1 (suspenseful home-invasion passage for G3)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 102,
   "verdict": "keep",
   "reason": "Quotes verified: the lint dropped ~2.8% of items, early data had a 2.4% fabrication rate, and fabrication scores 0. A concrete way to apply truth 59.",
   "statement": "Drop any generated content containing a number that can't be traced to its source; leaving a fact out teaches nothing false, while inventing one teaches a falsehood.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-method.md",
     "lines": "94",
     "quote": "an omitted number teaches nothing false; a fabricated number would be trained in as truth",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
     "lines": "71",
     "quote": "Fabrication scores 0 — not 0.5. The timeline notes a 2.4% fabrication rate in early synthetic",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 103,
   "verdict": "keep-with-fix",
   "reason": "Quote verified: scores moved from 23.5 to 17.0 out of 25. Added a non-name AP-history case: a jump from 0.29 to 0.95 existed only under one judge and fell to 28% on the binding grader.",
   "statement": "Compare judged scores only under the same judge and judge version; a judge change alone shifts absolute scores.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
     "lines": "68",
     "quote": "subset vs 23.5 in July — absolute numbers shifted with the judge; only within-eval comparisons",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "52",
     "quote": "that jump existed only under a discredited",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "53",
     "quote": "on the binding grader it collapsed to 28% (DBQ 0%, MCQ_SET 0%, \"Gemini-judge artifact\")",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 104,
   "verdict": "keep",
   "reason": "Quotes verified: 4 scenarios × 3 runs matched 12 of 12; the wrong-answer control held 3 of 3; a later round matched 18 of 18. Each probe covered one item (against).",
   "statement": "Whenever a marker's rules change, replay a fixed set of scenarios — the intended answer, partial routes and a wrong-answer control, several runs each — and compare turn by turn; reasoning can't settle how a model will read a new rule.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-16-R24.md",
     "lines": "41",
     "quote": "Reasoning cannot settle whether an LLM judge reads",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-16-R24.md",
     "lines": "65",
     "quote": "| wrong-answer control (\"Jo looks inside the basket\") | no pass | 3/3 off | 3/3 off |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-16-R26.md",
     "lines": "42",
     "quote": "All 18 turns identical in band AND ticked criteria to the R25 baseline (18/18).",
     "verbatim": true
    }
   ],
   "against": "Each probe covered one item only: \"Not probed this tick (one step per tick).\" (g5-course/ADVERSARIAL-REVIEW-2026-09-16-R25.md line 60).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 105,
   "verdict": "keep-with-fix",
   "reason": "AP item. Quotes verified in the person-named brainlift and course skeleton. Rebased on non-name files: approval_clean says the leak check is only a lint for reading; the honesty fact sheet records that the AP pipeline's MCQ fix removed the source so the grader's leak probe was skipped (grader-gaming); the proposal review notes the AP evidence comes from a different subject and grader. Not on the list; distinct from 5.",
   "statement": "A leak probe built for history source questions does not fit reading: in reading, finding the answer in the text is the skill, so there such a probe is only a build-time lint, not proof of comprehension, and items built to skip the probe gain nothing real.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "328",
     "quote": "for reading, \"anti-leak\" is a build-time lint (answer not in the stem, honest distractors) — NOT a comprehension guarantee, since finding the answer in the passage IS the reading skill.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "54",
     "quote": "actual MCQ fix was the OPPOSITE — *removing* the stimulus so the grader's leak-probe is skipped (grader-gaming).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "73",
     "quote": "G's certification evidence to date is AP-history, a different subject/grader, and reading runs the leak-probe \"hot\" (mandatory stimulus)",
     "verbatim": true
    }
   ],
   "against": "Two accounts of the same grader differ: the proposal review says reading runs the leak-probe \"hot\" because every item has a passage, while a later person-named brainlift says the grader already skips the history-style check for reading.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 106,
   "verdict": "keep-with-fix",
   "reason": "AP item. κ = 0 and zero lift are verified in the person-named brainlift. Rebased on non-name restatements: GOAL lines 9 and 67, and the fact sheet's note that the AP '99%' came from caching plus best-of-N, not from the generator. Measured on AP history only. Distinct from 65 and 66 because it is about whether the picker itself is valid.",
   "statement": "Picking the best of several drafts is only as good as the grader that picks: selection inherits the grader's link to the real criterion and adds none of its own, so a cheap holistic ranker that agreed only at chance gave zero lift.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md",
     "lines": "67",
     "quote": "best-of-N is mathematically argmax over the grader, so it INHERITS the grader's correlation-to-truth and ZERO of its own (measured: zero lift vs cheap same-family ranker, kappa~0",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md",
     "lines": "9",
     "quote": "the cheap holistic ranker is a kappa~0 rubber stamp on subtle failures",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/alpha-read-packager/FACTS_SHEET.md",
     "lines": "55",
     "quote": "the \"99%\" was **cache + best-of-N**",
     "verbatim": true
    }
   ],
   "against": "Measured once, by one author, on AP-history items: \"The \"two teams converged\" is **WEAK** — it's one author importing AP findings onto grade-3, not independent replication.\" (alpha-read-packager/FACTS_SHEET.md line 57).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 107,
   "verdict": "drop",
   "reason": "AP item. Quotes verified (and restated in GOAL line 67), but this is one item slot, measured once by one author on AP history; FACTS_SHEET line 57 calls the cross-team agreement one author's import, not replication. A failing dimension that moves on every re-grade is a symptom of grader noise (candidate 108; the same source puts verdicts at ~21% non-deterministic), so a pass within 2 candidates may be a lucky grade. What holds up is already in 106 and 108.",
   "statement": "Repeatedly hand-fixing one failing item against a grader may never converge because the failing dimension moves with each re-grade; generating several candidates and certifying the passer worked instead.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
     "lines": "103",
     "quote": "10 sequential expert hand-fixes failed — the failing dimension migrated on each re-grade — while **best-of-N got a pass in 2 candidates**.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/course-skeleton.md",
     "lines": "29",
     "quote": "Hand-iteration doesn't converge (10 fails); best-of-N does (pass in 2).",
     "verbatim": true
    }
   ],
   "against": "Re-sampling did not fix a systematic leak: \"Regen pilot (Wave 3) showed 9.5pt improvement in MCQ leak (99.5% → 90.0%) but leak remained\" (LANE1_COURSE.md line 167).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 108,
   "verdict": "keep-with-fix",
   "reason": "AP item. Quotes verified in the person-named brainlift and skeleton. Rebased on GOAL line 67 (non-name): flips at 0.80–0.85 were real defects, items at ≥0.95 held, and the gate filters noise, not bias, which is truth 35. 'Usually' is softened. The ~21% non-determinism figure appears only in the person-named skeleton. Measured on AP history only; related to 9, 34 and 35.",
   "statement": "When an item's verdict flips between identical re-gradings, treat the flip as a sign of a real defect and count the item as passing only if it passes every re-grading; this filters grading noise, not a grader's consistent bias.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md",
     "lines": "67",
     "quote": "The flip-band stably-pass gate is load-bearing hygiene every lens endorsed (0.80-0.85 flips are real defects, >=0.95 holds) but it filters score NOISE, not score BIAS",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/PROPOSAL_REVIEW_2026_06_16.md",
     "lines": "49",
     "quote": "flip-band/stably-pass certification",
     "verbatim": true
    }
   ],
   "against": "A tightly specified marker can be stable: \"Bands, banked criteria and passing turn are IDENTICAL across routes in 12/12 scenario runs.\" (g5-course/ADVERSARIAL-REVIEW-2026-09-16-R24.md line 67).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 109,
   "verdict": "keep",
   "reason": "Quotes verified: 36 of 44 vocabulary slots had no viable item, and the template expected ~90% multiple-choice leakage (line 40).",
   "statement": "If the items that survive the checks can't fill the test plan, report a failure, not a pass with gaps.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/VERDICT_TEMPLATE.md",
     "lines": "28",
     "quote": "> not PASS-with-named-gaps. No green verdict over a vacuous pool.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/LANE1_COURSE.md",
     "lines": "246",
     "quote": "**Implication for vocab slots:** 36 of 44 vocab-mcq slots in V2 skeleton have no viable items.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 110,
   "verdict": "keep",
   "reason": "Quotes verified: a genuine open conflict between a rule pack (exactly one word) and the review standard (2–3 words).",
   "statement": "How many words should a lesson teach in depth — exactly one, or two to three? The project's own sources disagree.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/DECISIONS-2026-08-24.md",
     "lines": "26",
     "quote": "- **Exactly one taught word per lesson.** The rule pack sets this. Aladdin",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/arc-audit/SIM-REVIEW-D1-D4.md",
     "lines": "221",
     "quote": "only 1 new word/lesson in L5/L6/L7 is below the wiki's own \"2-3 Tier-2 words per lesson\" rule, and is an open, unresolved conflict per the case study itself",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 111,
   "verdict": "keep",
   "reason": "Quotes verified. The tension is sharper than the statement suggests: the demo unit's spine gate decertifies items that earlier lessons' content answers (DELTA-REPORT line 22). Pairs with candidate 10, which proposes measuring knowledge growth separately.",
   "statement": "How should a knowledge-building course give credit for knowledge built in earlier lessons, when the text-dependence gate removes every question answerable from prior knowledge?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "43",
     "quote": "It cites Hirsch and Willingham and then forbids knowledge from helping.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/VERDICT_TEMPLATE.md",
     "lines": "70",
     "quote": "2. **KCT1 Domain-knowledge ≈ 0 — by design.** Domain-recall items are passage-independent → removed",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
     "lines": "296",
     "quote": "is the last scaffold, and like every other scaffold it fades gradually",
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
   "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/corrective-feedback-policy.md",
   "lines": "48",
   "quote": "**concrete, addressable locus**, never a generic \"look again\":",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "51",
   "quote": "- Every surface a child can miss must name the misconception and leave a way forward WITHOUT",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "231",
   "quote": "No hint or support is visible before the student's first genuine",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/14-prototype-unit-power-course-graph.md",
   "lines": "195",
   "quote": "- no new teaching before first attempt;",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter: single-select multiple choice gets no reveal at all, recorded as a sanctioned departure from the generic spec",
   "path": "~/Projects/grade3-reading/artifacts/CLOSURE-PLAN-2026-08-25.md",
   "lines": "19",
   "quote": "with a written pedagogical argument (a closed set the child works through)",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "45",
   "quote": "- No `reveal_after_tries` on single-select — exhausting a closed list IS the thinking; a reveal",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter: open responses get three scored turns before the reveal",
   "path": "~/Projects/grade3-reading/artifacts/decision-matrix/slices/07-SCORING-FEEDBACK-XP.csv",
   "lines": "55",
   "quote": "third miss the reveal that names the gap, states the answer, cites the text, and opens the gate",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "75",
   "quote": "- Items answerable without the passage are defects, not questions (provenance: ~78% of raw",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
   "lines": "232",
   "quote": "- **6/6** — the number of items an LLM-judge passed that a blind-solve cracked, the commitment-9",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
   "lines": "43",
   "quote": "It cites Hirsch and Willingham and then forbids knowledge from helping.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
   "lines": "186",
   "quote": "- **W-8. WORTH-FIXING — `item-8-match` prompt 1 is a coin-flip between two dated",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-25-R10.md",
   "lines": "104",
   "quote": "per the lesson's own gloss pattern) can defensibly pick the distractor and be marked wrong.",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
   "lines": "145",
   "quote": "p7–p12 (never more than 2 reads without a check)",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
   "lines": "96",
   "quote": "79% (correct at position A, G4 census n=100 MCQ + 116 EBSR)",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/DELTA-REPORT.md",
   "lines": "29",
   "quote": "Key-position imbalance, 12/19 A with a 5-run (must-fix)",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/feedback-inceptbench-2026-09-30/REGISTER.md",
   "lines": "119",
   "quote": "The word bank lists answers in the same order as the blanks (free, swords, sea), so tapping the first three words in order gets everything right without reading",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-28-R13.md",
   "lines": "40",
   "quote": "12 pass distinct-letters / 40%-cap / no-triple-run.",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/edullm-standards-centralization-2026-08-05/README.qmd",
   "lines": "105",
   "quote": "> **BLOCKED — evidence missing; no pass inferred.**",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/edullm-standards-centralization-2026-08-05/IMPLEMENTATION-PLAN.md",
   "lines": "253",
   "quote": "3. Return `NOT_EVALUABLE` for affected rule.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/decision-brief-2026-09-10/DECISION-BRIEF.md",
   "lines": "57",
   "quote": "The judge accepted a misspelled \"magician\" as full credit. Comprehension currently tolerates",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "175",
   "quote": "no `scoring`/`accept` spec passes on keyword presence alone",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R3.md",
   "lines": "10",
   "quote": "193 paragraphs, 1 deviation",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "counter: one renderer accepts a 95% similarity match instead of an exact one",
   "path": "~/Projects/grade3-reading/artifacts/decision-matrix/slices/07-SCORING-FEEDBACK-XP.csv",
   "lines": "20",
   "quote": "ScrItem's quote gate requires 95% token-window similarity against candidate lines",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/VOCAB-DECISIONS-U9.md",
   "lines": "68",
   "quote": "all clear the counting rule and are still wrong to teach: a Grade-5 card is spent on a word",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/00-difficulty-notes.md",
   "lines": "44",
   "quote": "REVISE cannot swap payload words out",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports (line corrected from 89 to 88)",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-25-R10.md",
   "lines": "88",
   "quote": "Harm: the lesson's single most title-central term has a definition a child can never tap on the",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports (person-named path)",
   "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/02-[name]-instruction-model.md",
   "lines": "29",
   "quote": "The bridge must be short and targeted. It is not a recall quiz and not a mini-lecture that drains the text.",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/decision-packets-2026-09-03/PACKETS.md",
   "lines": "12",
   "quote": "the TEXT on p10. The image spoils him a page early and depicts action not on this page.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/GAP-ANALYSIS-2026-08-18.md",
   "lines": "6",
   "quote": "mechanically verified this session, not read from commit messages or status docs.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/DECISIONS-2026-08-24.md",
   "lines": "83",
   "quote": "- **Verify against the file, not the report.** Confident-wrong moments this",
   "ok": true
  },
  {
   "truth": 25,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "64",
   "quote": "- Spoken lines never open with \"Name:\" — the TTS drops the label silently (speaker-label trap,",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "42",
   "quote": "- 25-word ceiling on any sentence a child must act on (story prose and taught frames exempt,",
   "ok": true
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/r2-feedback-docx-converted.txt",
   "lines": "66",
   "quote": "rendered black text on a black background, legible only on hover",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/sim-review-2026-09-02/FINDINGS.md",
   "lines": "5",
   "quote": "- CRITICAL: L6 p18 + L7 p18 `cfu` dialogues had NO gate key — closing comprehension",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
   "lines": "157",
   "quote": "This is a hard, cited number (74% majorly flawed for LLM-generated items) that bears directly",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
   "lines": "137",
   "quote": "old: LLMs assemble-and-tag only (generic model evidence). Current",
   "ok": true
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
   "lines": "94",
   "quote": "verbatim can be scored as off-text. Fix: author a pinned copy of the target",
   "ok": true
  },
  {
   "truth": 31,
   "effect": "supports (person-named path)",
   "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
   "lines": "88",
   "quote": "**The two FRQ rubrics — binary, AND-gated, shown not asserted.**",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
   "lines": "211",
   "quote": "calibrate**: v4 sprays (26 hits / 494 false-positive extras / 4-of-10 clean-correct out of a",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
   "lines": "120",
   "quote": "— but v4 \"sprays ~12 uncited extras per artifact\" (root cause: S3 stream was 6:1 flawed:clean).",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
   "lines": "215",
   "quote": "the criterion text in context \"may simply not know where the line is\" (missing discrimination",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports; the second run used tightened criteria, so the clean flip is vf07, which got a softer verdict under stricter criteria",
   "path": "~/Projects/grade3-reading/artifacts/art-qa-redcontrol-2026-09-11/RECORD.md",
   "lines": "42",
   "quote": "Runs 1 and 2 disagreed on vf07 (FAIL → note), vf08 (note → FAIL) and vf10 (note → FAIL) — the",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/LANE3_LLM.md",
   "lines": "302",
   "quote": "**Calibration threshold:** If spot-check shows <70% agreement with gate labels → the gate threshold needs recalibration.",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports, weakly: the figure is agreement between two automated graders (Gemini and the IB grader) on DBQ essays, not against person-labelled cases; person-named path; GOAL line 49 describes 16.7% as a grader-vs-human floor instead",
   "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
   "lines": "93",
   "quote": "*(MEASURED-in-AP-history: Gemini↔IB DBQ agreement 16.7%)*",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/CRITIC.md",
   "lines": "27",
   "quote": "label consistency across four audit agents + eight skeptics was not tested",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/edullm-standards-centralization-2026-08-05/EXECUTOR-RUNBOOK.qmd",
   "lines": "523",
   "quote": "1. Positive, negative, boundary, and missing-input fixture for every blocking rule.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/op-taxonomy-calibration-2026-07-10/op-taxonomy-calibration.md",
   "lines": "132",
   "quote": "fc-09 all flagged, zero false flags on controls, and the mandatory per-unit human",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/audit-heuristic-finding.md",
   "lines": "62",
   "quote": "Our ids are `g5-reading-merged-pp-9802-*`, so **the real enforcement",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/demo-unit-2026-07-10/phase-d/02-gate-summary.md",
   "lines": "55",
   "quote": "- Independent verify: every verdict recomputed from raw attempts alone",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
   "lines": "225",
   "quote": "- **W-9. WORTH-FIXING — gradual release runs backwards, only here.** p14's chart",
   "ok": true
  },
  {
   "truth": 42,
   "effect": "supports, loosely: reworded variants inherited their base item's certification without being re-checked",
   "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-claude/bank/final/BANK_REPORT.md",
   "lines": "43",
   "quote": "- **Variants are NOT independently anti-leak-gated.** They inherit their base item's certified",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/takeover-audit-2026-07-13/pr68-enforcement-audit.md",
   "lines": "27",
   "quote": "lesson can omit both. An exact set diff would check declared identical strings only; it would",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
   "lines": "247",
   "quote": "- The \"43 of 285 criteria require a named human — no script or LLM-judge can close them\" fact,",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/course-json-standard-2026-07-13/README.md",
   "lines": "59",
   "quote": "- Schema validity is a document-integrity floor, not a course-quality, child-readiness, or",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/04-evidence-contract.md",
   "lines": "58",
   "quote": "If human review is unavailable, mark the claim as `owner_gap`, not `verified`.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/pedagogy-llm-evals.md",
   "lines": "11",
   "quote": "File: `eval/eval.jsonl`. Authored 2026-07-21 from source documents BEFORE any system was built.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-19-R2.md",
   "lines": "12",
   "quote": "child's screen\" below is what the engine renders, not what the JSON suggests.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-08-27-R12.md",
   "lines": "52",
   "quote": "Why the suite missed it: `item-engine.test.mjs` tests the pure module and MsqItem's",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/curriculum-adherence-2026-09-24/CRITIC.md",
   "lines": "7",
   "quote": "Why: what the child sees ≠ what the file holds.",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/decision-matrix/slices/08-VERIFICATION-DISCIPLINE.csv",
   "lines": "11",
   "quote": "the walk-lesson script must drive the real app in a real browser through the whole lesson and assert each step, rather than spot-checking",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/knowledge-first-reading-course-proposal-2026-07-09/03-transfer-practice-layer.md",
   "lines": "95",
   "quote": "It proves assessment integrity, not curriculum quality.",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/approval_clean.md",
   "lines": "350",
   "quote": "- Blended: 83% (heavily weighted by easier item types)",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/edullm-agent-entrypoint-g3-practical-test-2026-08-06/REPORT.qmd",
   "lines": "31",
   "quote": "one ZIP-only file and two byte mismatches",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R18.md",
   "lines": "25",
   "quote": "exactly before trusting any line-level comparison against it.",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/G5-CURRICULUM-ONE-PAGER.md",
   "lines": "35",
   "quote": "noted, not treated as approval.",
   "ok": true
  },
  {
   "truth": 52,
   "effect": "supports (the open question of whether to use video at all)",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
   "lines": "141",
   "quote": "This is a genuine, load-bearing tension",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/cross-cutting.md",
   "lines": "200",
   "quote": "the child who freezes needs scaffold-down",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "174",
   "quote": "16. **Grading guidance MUST demand stance, not tokens; quotes fail closed (F16).**",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "46",
   "quote": "1. **The canonical file is the sole truth.** Every passage sentence, span id, item, misconception",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/AUTHORING-RULINGS-R1-R10.md",
   "lines": "106",
   "quote": "For every gated non-mcq item, each hint/second_hint/reveal must trace to canon",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/Grade 3 Reading - Proposal Review & Synthesis.docx",
   "lines": "164 (textutil plain-text output)",
   "quote": "the 92% mismatch rate in literary units (12/13 guiding items ask wrong-subject questions)",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/LANE3_LLM.md",
   "lines": "347",
   "quote": "prevents the PPO loop from finding reward by maximizing all other checks while ignoring the one that matters",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/redteam-standard.md",
   "lines": "139",
   "quote": "Items are learning events; a bad item teaches a false belief",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-book-2026-09-29/logs/GATE-VERDICT.md",
   "lines": "3",
   "quote": "Failure lines identical step by step",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "366",
   "quote": "- After the agent returns, spot-verify checklist items 2, 7, 11, and 17 independently before",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/ADVERSARIAL-REVIEW-2026-09-08-R17.md",
   "lines": "19",
   "quote": "against the geology canonical files would produce a 100% spurious mismatch on every passage and",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-course/LESSON-AUTHORING-PLAYBOOK.md",
   "lines": "251",
   "quote": "No contract ⇒ no diagram —",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-expansion-session-2026-07-08-codex/QUESTION_GENERATION_RETROSPECTIVE_2026-07-08.md",
   "lines": "215",
   "quote": "The gate was not a self-check. The authoring model family was GPT; the gate solver was Gemini.",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports (person-named path; AP history)",
   "path": "~/Projects/grade3-reading/artifacts/course_approaches_20260616/Course Approaches/[name] v2/brainlift.md",
   "lines": "105",
   "quote": "a same-family picker + judge produces Goodhart inflation",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5-merged-course/corrective-feedback-policy.md",
   "lines": "33",
   "quote": "No model call decides",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports, loosely: a targeted verifier missed a failure elsewhere, which is why the full suite runs after each change",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/GATE-STANDARD-DRAFT.md",
   "lines": "118",
   "quote": "— targeted verifiers read one slice; the colon-fix went red on a validator the listen pipeline",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/build-closing-questions-2026-09-25/BUILD-SPEC.md",
   "lines": "66",
   "quote": "per-lesson md5 of every OTHER lesson unchanged after each step",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports (added by the verifier from the AP review, non-name path): passing every re-grade shows consistency; a confidently mis-graded item still passes",
   "path": "~/Projects/grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md",
   "lines": "67",
   "quote": "it filters score NOISE, not score BIAS — a confidently mis-graded item certifies forever",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports (added by the verifier from the AP review, non-name path): the grader must clear an agreement floor against human labels before it scores items",
   "path": "~/Projects/grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md",
   "lines": "49",
   "quote": "prove grader-vs-human kappa clears the 16.7 percent floor and holds across re-audits before it scores any item",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports (added by the verifier from the AP review, non-name path): a grader's pass rate measures item quality, not learning",
   "path": "~/Projects/grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md",
   "lines": "9",
   "quote": "It is item-quality-against-a-rubric, NOT learning",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports (added by the verifier from the AP review, non-name path): a grade setting carried over from another course went unchecked",
   "path": "~/Projects/grade3-reading/artifacts/GOAL_grade3_hootl_convergence_2026_06_15.md",
   "lines": "47",
   "quote": "grade hardcoded 11 from AP US History",
   "ok": true
  }
 ]
}
```
