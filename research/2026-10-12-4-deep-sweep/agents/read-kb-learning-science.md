# read:kb-learning-science

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "kb-learning-science",
 "coverage": {
  "read": [
   "knowledge_bot/INDEX.md (all 249 index lines: id, tags, path; used to select scope)",
   "Read in full: kb-0005, kb-0015, kb-0059, kb-0063, kb-0064, kb-0069, kb-0070, kb-0074, kb-0080, kb-0086, kb-0092, kb-0093, kb-0096, kb-0097, kb-0099, kb-0100, kb-0110, kb-0115, kb-0120, kb-0121, kb-0122, kb-0123, kb-0124, kb-0128, kb-0131, kb-0135, kb-0136, kb-0137, kb-0153, kb-0154, kb-0155, kb-0156, kb-0158, kb-0159, kb-0164, kb-0167, kb-0169, kb-0170, kb-0171, kb-0172, kb-0180, kb-0181, kb-0183, kb-0242, kb-0243, kb-0246",
   "Read the core sections in full (SPOVs, insights, blueprints): kb-0116, kb-0118, kb-0161, kb-0163, kb-0204 (spec sections 3-10), kb-0217 (certification standard and audit sections), kb-0220 (video reconciliation), kb-0166 (design, result table, failure counts), kb-0141 (model and LLM-constraint sections), kb-0032 (learning-science, gaming and closed-loop sections), kb-0027, kb-0028, kb-0026",
   "Read targeted sections or greps: kb-0102 to kb-0109 RAND entries (summaries; kb-0104 instruction findings; kb-0108 assessment critique and requirements), kb-0111 (summary, reliability, discussion, limitations), kb-0112 to kb-0114 (summaries), kb-0117 and kb-0119 (summaries; spacing, retrieval and interleaving evidence), kb-0157 (spacing, calibration, wheel-spinning and worked-example sections), kb-0160 (item-flaw, testing-effect and negative-suggestion readings), kb-0162 (summary and grep), kb-0125, kb-0127, kb-0130 (summaries and benchmark/transfer lines), kb-0132, kb-0165, kb-0168 (summaries), kb-0142, kb-0143, kb-0147 (summaries and sampled rows), kb-0251 (key facts and research manifest), kb-0221 (summary), kb-0030, kb-0033, kb-0034 (greps), kb-0079, kb-0073, kb-0081 (greps), kb-0007, kb-0065, kb-0066, kb-0075, kb-0084 (summaries)"
  ],
  "skipped": [
   "kb-0006 (platform source-code notes, no learning-content findings)",
   "kb-0029, kb-0044, kb-0046, kb-0048 (interoperability and API reference docs)",
   "kb-0138, kb-0139, kb-0140 bodies (subject-specific misconception lists; the cross-cutting synthesis kb-0141 was used instead)",
   "kb-0144, kb-0145, kb-0146, kb-0148 to kb-0152 (science atom/composite ledgers: spreadsheet data dumps of ~600 KB; structure confirmed by sampling kb-0147 only)",
   "kb-0109 (bibliography and panel bios)",
   "kb-0112 to kb-0114 bodies (practitioner slide decks; only summaries read)",
   "knowledge_bot/skills/reading-science/ SYNTHESIS and digests (outside the knowledge/ folder scope)",
   "knowledge_bot/.env and .env backups (never opened, per rules)"
  ],
  "notes": "Quotes that span wrapped lines are joined with a single space; markdown marks are kept where they sit inside the quoted text. Name-bearing paths: kb-0005 ([name]), kb-0073 and kb-0100 ([name]), kb-0079 ([name]), kb-0111 (cervetti, an author), kb-0246 (ujjawal); candidates relying on kb-0100, kb-0079 or kb-0111 are flagged. Tensions found and kept visible: three vs four options (research vs a reviewer ruling); whether low blind-solver confidence should discount a leak (two measured results disagree); no reveal for single-select items vs 'two tries then the answer'; prohibition lists for writer models vs truth 62; spoken-only answers vs a text fallback; mastery tests in practised formats vs the 'marathon rule'. Most BrainLift entries (kb-0153 to kb-0163, kb-0116 to kb-0119) are literature summaries, not project measurements; where a statement relies only on them it is marked external research or adopted rule. AP-related material read in depth: the APUSH generator project (kb-0063, kb-0064), the APUSH course audits (kb-0167, kb-0170, kb-0171) and the diagnostic BrainLift's APUSH protocol (kb-0154, kb-0155)."
 },
 "candidates": [
  {
   "statement": "Before trusting a score, high or low, test the harness that produced it: a wrong field, the wrong grader host, mis-routing or cut-off output can fake a failure.",
   "kind": "measured",
   "found_by": "An AP question generator was 'stuck at ~28%' for weeks; four harness bugs caused it. A later lesson-QA lane found half its audio 'defects' were defective checks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "40-41",
     "quote": "(wrong field read, grader on wrong host, MCQ_SET mis-route 0→0.77, DBQ truncation 0.55→1.0 at 6000 tok)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "76",
     "quote": "proof that an unvalidated measurement can masquerade as a real number."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "72-73",
     "quote": "half of 'audio defects' were defective checks"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    36,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count a result only on the grader of record; a gain that shows up under one judge can vanish under the binding grader.",
   "kind": "measured",
   "found_by": "A reported jump from 0.29 to 0.95 existed only under a discredited judge and fell to about 28% on the binding grader.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "9",
     "quote": "that jump existed only under a discredited Gemini judge; on the binding grader it collapsed to ~28% (DBQ 0%, MCQ_SET 0%, a 'Gemini-judge artifact')"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A change that passes a check by removing what the check inspects is gaming the check, not fixing the item.",
   "kind": "measured",
   "found_by": "An item 'fix' removed the source text, so the grader's leak probe never ran.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "9",
     "quote": "the actual MCQ fix was the OPPOSITE: REMOVING the stimulus so the grader's leak-probe is skipped (grader-gaming)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't let a judge from the writer's own model family certify the writer's output; check with a different family.",
   "kind": "measured",
   "found_by": "The first different-family blind solve, run on 11 items a same-family benchmark had passed, found 4 confirmed leaks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd",
     "lines": "21",
     "quote": "4/11 CONFIRMED leaks. 8/11 answerable-blind. Only 3/11 cleanly passage-dependent. → 36% leaky."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "407-408",
     "quote": "The audit-only LLM verifier cannot be from the renderer's family."
    }
   ],
   "against": "kb-0096 line 69: \"Blind-solve calibration matters more than judge identity alone.\"",
   "adds_to_existing": [
    43,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A content-quality score does not certify an item; make the answerability (leak) check a separate blocking gate.",
   "kind": "measured",
   "found_by": "A quality benchmark passed all 11 items that a blind solve failed 4 of, and elsewhere it scored answer-leaking items 1.0.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd",
     "lines": "54",
     "quote": "IB passed all 11; the different-family blind solve failed 4."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "47",
     "quote": "separate from InceptBench, which graded answer-leaking items 1.0"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    58
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Run the blind solve against chance over repeated trials: an item passes only if it is answered right with the source and near chance without it.",
   "kind": "adopted rule",
   "found_by": "Text-dependence judged by rubric and regex passed items that blind probes solved easily, so a numeric probe rule was set.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "40-41",
     "quote": "PASS if with-passage correct-rate >= 0.80 AND without-passage correct-rate <= chance-rate + 0.15 margin"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd",
     "lines": "180-181",
     "quote": "model answers without passage in >=3/5 trials at temp 0.3 = fail"
    }
   ],
   "against": "kb-0080 line 182: \"LLM ablation may false-positive/negative vs real students\"",
   "adds_to_existing": [
    5,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Anchor questions on details only the source supplies, such as invented names or text-specific structure; content built on common knowledge invites answering without reading.",
   "kind": "measured",
   "found_by": "In a blind solve, items about a well-known real topic were attempted from world knowledge. Items with invented names, or needing both correct choices, stayed text-dependent.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd",
     "lines": "59-60",
     "quote": "prefer fictional proper nouns over real-world entities; MSQ-needs-both beats single-key MCQ for leak-resistance"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd",
     "lines": "47-48",
     "quote": "a world-knowledge-rich passage invites guessing; a savvy test-taker could beat it without reading."
    }
   ],
   "against": "Small sample (11 items). kb-0158 line 108: \"Guessing jackpot: Random \\\"select many\\\" can outscore partial knowledge unless a principled scoring rule is used.\"",
   "adds_to_existing": [
    5,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "No surface cue may give the key away: the key must not be the longest, shortest, odd-one-out or most stem-echoing option, and the item must not yield to keyword matching or elimination.",
   "kind": "measured",
   "found_by": "A generated course put 79% of keys at position A, and the key was systematically the longest. Reviewers could see the answer from length and phrasing alone.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "63-64",
     "quote": "The right option must not be the longest, the shortest, the odd one out, or the one that reuses the most words from the stem."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "77",
     "quote": "79% of correct answers in a generated course sat at option position A, and the correct option was systematically the longest"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "133",
     "quote": "Closed-response items must require the target reasoning and must not be answerable by surface cues, keyword matching, option length, or test-wise elimination."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a two-part item, the evidence part must not restate or reveal the answer part.",
   "kind": "measured",
   "found_by": "All 6 sampled two-part evidence items were blind-solvable because part B restated part A.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "78",
     "quote": "6 of 6 sampled two-part evidence items were blind-solvable, with Part B restating Part A"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "83",
     "quote": "include prior-knowledge answerability, EBSR Part-B-restates-Part-A, and keyword-match answerability."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Work out each item's guessing floor from how the platform actually scores it, not from its format name.",
   "kind": "measured",
   "found_by": "A live scoring probe showed a select-2-of-12 item scored on its first token, which put the guessing floor about 11 times above nominal chance.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0100-[name]-lanes-execution-2026-07-10.qmd",
     "lines": "91-92",
     "quote": "floors are computed per item from its responseDeclaration, never from the format label."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Before trusting a mastery gate, try to pass it without doing the work: click through, guess, or answer everything wrong.",
   "kind": "measured",
   "found_by": "Reviewers earned a mastery stamp at about 20% accuracy by clicking through, and passed a task with every answer wrong.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "120",
     "quote": "earned a stamp on \"The Amazing Axolotl\" at about 20 percent accuracy by clicking through without reading, then advanced with the passage hidden from view."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "101",
     "quote": "In a main-idea task, reviewers earned the pass while answering every question incorrectly."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28,
    38,
    47
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every screen should ask for a response that serves the teaching, and no check may be skippable; a nudge students can click past is not a check.",
   "kind": "adopted rule",
   "found_by": "An attention nudge could be skipped by clicking Next twice, and passive screens invited click-through.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "79",
     "quote": "the \"not so fast\" nudge is non-blocking and can be skipped by clicking Next twice."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "27",
     "quote": "passive listening or text-only screens invite click-through rather than attention"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26,
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prefer tasks where students produce (say, write, type) over tasks where they only select; recognition can't show that a student can explain or produce.",
   "kind": "adopted rule",
   "found_by": "Reviewers found a course where every response was a click. The resulting rule judges a lesson by what students produce.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "38-39",
     "quote": "judge a lesson by *production* (say/write/type) over *selection* (click)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "124",
     "quote": "N3: recognition-vs-production match. \"Write/explain/draw\" targets cannot be assessed by MCQ alone."
    }
   ],
   "against": "kb-0154 line 86: \"For diagnostic assessment, the much-maligned MCQ is not a compromise — it is the optimal format.\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Gradual release runs one process with falling support: model the thinking, have the student complete a partial answer of the same process, then release that same process. A hint is not guided practice.",
   "kind": "adopted rule",
   "found_by": "Reviewers found the modelled step revealing answers, the guided step reduced to a hint, and the independent step switching skills.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "60",
     "quote": "I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "34-36",
     "quote": "the we-do gives a *partial* answer the child completes (a hint is not a we-do, a fresh question is not a we-do); I-do, we-do and you-do must run the *same skill*, never switch mid-lesson."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check gradual release by stripping off the labels; if the steps no longer read as modelled, guided and independent work, the labels were decoration.",
   "kind": "adopted rule",
   "found_by": "Labelled steps were shown not to guarantee that the release was faithful, so a strip-the-labels test was built into authoring.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "43-44",
     "quote": "gradual-release doses that survive the strip-the-labels test"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "136",
     "quote": "gradual-release fidelity: labels alone are insufficient;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a worked model, take every step up to the final thinking move and leave that move to the student.",
   "kind": "adopted rule",
   "found_by": "A fixed modelling-moment split was ruled for all lessons, so the student always does the real cognitive work.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "83-84",
     "quote": "the teacher models every step up to but not including the final substantive thinking move; the child does that move"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before students start, tell them what they are reading or working to find out, and keep the lesson's question and the current steps visible while they work.",
   "kind": "adopted rule",
   "found_by": "Reviewers found a lesson with no stated purpose, and saw the steps and the live question scroll away during modelling.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "61",
     "quote": "Children need a reason to read before they start"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "84",
     "quote": "The steps and live question must remain visible, and the model should surface one thing at a time"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "210",
     "quote": "It is annotated, and pinned to the top of every screen."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write questions specific to the source; generic rules of thumb such as 'find the one key sentence' or 'check the title' mislead.",
   "kind": "adopted rule",
   "found_by": "Reviewers rejected generic strategy advice taught as if it applied to every text.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "73",
     "quote": "Titles frequently do not state the main idea, so checking against the title is not a dependable rule."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "75",
     "quote": "but the question must be bespoke to the text."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a task asks for evidence, keep the source visible, have students find and mark the evidence before writing about it, and show a model of a strong response.",
   "kind": "adopted rule",
   "found_by": "Evidence prompts hid the source, gave no model answer, and asked students to write before finding the evidence.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "86-87",
     "quote": "Prompts ask for textual evidence, but the passage is hidden when the student needs to cite it."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "116",
     "quote": "Students should first find and highlight the sentence, then write it in their own words"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep corrective feedback short and aimed at the specific error, about 40 words, and never longer than the source or the original instruction.",
   "kind": "adopted rule",
   "found_by": "Reviewers found feedback that ran longer than the passage, so a feedback length lint was specified.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "59",
     "quote": "it is too long, sometimes longer than the passage"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "96-97",
     "quote": "if corrective feedback is longer or more complex than the original instruction, the item has crossed into new instruction."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Order hints from general cues to specific ones, and use the clue's own words only in the last hint.",
   "kind": "adopted rule",
   "found_by": "A census found guided-practice nudges that named the clue's exact words, which handed over the answer.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "53-54",
     "quote": "reword to criterion cues, naming a clue's actual words only in the *last* nudge"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1,
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Cap every sentence a student must act on at about 25 words, leaving the source text itself exempt, and apply the same cap to replies a scorer writes live.",
   "kind": "adopted rule",
   "found_by": "An age-appropriateness check, backed by readability data, set the cap. Live-generated replies needed a runtime check because a static check cannot see them.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "96-97",
     "quote": "putting a 14-word sentence at ~90% understood and a 43-word sentence under 10%"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "109-110",
     "quote": "since no static validator can see a line that does not exist until a child answers."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Teach a concept with an example and a non-example that differ only in the defining feature, and say why the non-example fails; ambiguous examples teach the wrong rule.",
   "kind": "adopted rule",
   "found_by": "Reviewer rulings, enforced by a validator, adopt Direct Instruction's faultless-communication principle.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "33-34",
     "quote": "example and non-example differ in only the one defining feature, and the non-example states why it fails"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "83",
     "quote": "If the learner can logically infer the wrong rule from the examples provided, the fault lies with the instruction, not the learner."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give each term one wording and use it everywhere it recurs; terms taught together must be distinct, and none may appear inside another's definition.",
   "kind": "adopted rule",
   "found_by": "Reviewers found overlapping target words, one of them inside another's definition, and a word carrying two meanings across a course.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "38",
     "quote": "One definition per word, used everywhere it recurs — reading goal, passage glossary,"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "30-31",
     "quote": "Taught words in one lesson must be distinct — never overlapping in meaning, never one appearing inside another's own definition"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every taught term needs at least one graded task where the student must use it; recognising it in multiple choice doesn't count.",
   "kind": "measured",
   "found_by": "An arc audit found two taught words that students acquired but no graded task ever required them to use.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "135-136",
     "quote": "merciless/triumphant were acquired but no graded surface required using them"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Plan many later encounters of each taught term, about 10 to 12 across a unit; incidental reading teaches few new words.",
   "kind": "adopted rule",
   "found_by": "A reviewer ruling, enforced by a validator, rests on the research claim that only about 5–15 of 100 unfamiliar words are learned from natural reading.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "69",
     "quote": "A word needs **10 to 12 encounters** across the unit/course to be retained"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "69",
     "quote": "Only \\~5–15 of 100 unfamiliar words met in natural reading are learned; misdirective contexts teach approximately zero"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a student's self-report as a starting guess that item evidence can overturn, never as proof of mastery; 'I know it' overstates what students can explain.",
   "kind": "external research",
   "found_by": "A diagnostic BrainLift and platform rules, plus a cited finding (Curtis, via Beck 2013) that about 80% mark a word known while about 20% can explain it.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "108",
     "quote": "The key design principle: self-report is a prior, not a verdict."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "72",
     "quote": "\\~80% of students check a word as \"known,\" \\~50% can give an example, \\~20% can explain it"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "21",
     "quote": "Do not advance students based on time, completion, or self-report."
    }
   ],
   "against": "kb-0155 line 207: \"students are better at judging their knowledge than the assessment literature implies — at least for coarse judgments.\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "While students are learning, use sources that build on one topic so knowledge compounds; keep unseen, unrelated sources for the test.",
   "kind": "external research",
   "found_by": "Reviewers judged that cold, non-overlapping passages everywhere engineered knowledge out of the course. A randomised study found coherent text sets built more knowledge (Cervetti, Wright & Hwang 2016, DOI 10.1007/s11145-016-9628-x).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "70",
     "quote": "Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "66",
     "quote": "Coherent-set readers gained 5.59 vs 2.63 concept idea-units (η²=.32) over six texts in three days (Cervetti 2016, pp. 769–771)."
    }
   ],
   "against": "kb-0111 lines 736-737: \"this study took place in one rural school and included only fourth grade students who were reading on grade level\"",
   "adds_to_existing": [
    48,
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build the background knowledge a source needs instead of only activating what students already bring; what they already know decides how much new knowledge they gain.",
   "kind": "external research",
   "found_by": "Prior topic knowledge predicted new knowledge gained (Cervetti, Wright & Hwang 2016, DOI 10.1007/s11145-016-9628-x); a review found knowledge-building has no upper limit (Willingham & Lovette 2014, Teachers College Record ID 17701).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0111-cervetti-2016-knowledge-effect-full.qmd",
     "lines": "725-726",
     "quote": "students who have topic knowledge not only understand related texts better, but also build more knowledge from those texts."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0110-can-reading-comprehension-be-taught.qmd",
     "lines": "47",
     "quote": "strategy instruction may have an upper limit, but building background knowledge does not; the more students know, the broader the range of texts they can comprehend."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40,
    20
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Teach general strategies briefly, explicitly and inside content; extra strategy drill adds nothing, and the time is better spent building knowledge.",
   "kind": "external research",
   "found_by": "Eight quantitative reviews found 10 sessions give the same benefit as 50 (Willingham & Lovette 2014, Teachers College Record ID 17701). The RAND MR-1465 (2002) synthesis says content-embedded strategies beat isolated ones.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0110-can-reading-comprehension-be-taught.qmd",
     "lines": "45",
     "quote": "Ten sessions yield the same benefit as fifty sessions. The implication seems obvious; RCS instruction should be explicit and brief."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0104-comprehension-research-agenda.qmd",
     "lines": "80-81",
     "quote": "fosters deeper comprehension development than strategies taught in isolation"
    }
   ],
   "against": "kb-0104 lines 82-83: \"too-wide content/text range = strategies not fully learned; too-narrow = transfer fails\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Design the knowledge sequence first, and use standards only to fix scope and check coverage afterwards; standards are not a teaching plan.",
   "kind": "adopted rule",
   "found_by": "Curriculum-architecture doctrine: standards mislead on order, grain size and prerequisites, and skills-only standards carry no content.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "59",
     "quote": "use the standard to constrain scope (what must appear), but apply independent judgement about order, depth, prerequisite structure, and cognitive demand."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "32",
     "quote": "standards alignment is a *check run afterward*"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A bank of practice and test items is not a course; without explicit teaching inside a knowledge sequence it fails as instruction.",
   "kind": "measured",
   "found_by": "A reproducible design simulation scored practice-engine and thin-instruction variants red for all 12 personas; only the full teaching flow passed. Reviewers reached the same verdict.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
     "lines": "56",
     "quote": "| `V0_skill_drill_practice_engine` | 0 | 0 | 12 |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
     "lines": "70",
     "quote": "Strong questions do not become a course unless they sit inside this flow and the actual app proves students can experience it."
    }
   ],
   "against": "kb-0099 line 23 (it is a design stress test): \"not student outcome evidence\"",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Teach the combining of parts explicitly; tasks that select, combine or justify parts must be taught and gated, not assumed once each part is passed.",
   "kind": "adopted rule",
   "found_by": "Curriculum-architecture doctrine: students pass the parts and still fail the whole. Reviewers asked for integrative lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "110",
     "quote": "Students can \"master\" individual KCs yet fail whenever they must select, combine, or justify them in context."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "116",
     "quote": "The mastery gate for an integrative lesson must test the integration — requiring the combined move, not re-testing the parts in isolation."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Assess the same operation, at the same cognitive level, that the lesson taught, and match every skill tag to the work the item actually requires.",
   "kind": "measured",
   "found_by": "A main-idea lesson served an inference item, and coverage was claimed for 'analyze' targets tested only by 'identify' items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "92",
     "quote": "Example found: a main-idea lesson served an inference/evidence item."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "122",
     "quote": "N1: DOK-level alignment. Coverage is false if an \"analyze\" standard is assessed by \"identify.\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "If simplifying an item's wording without changing what it tests would make it easier, or you can't explain why it is hard, the difficulty is irrelevant; remove it.",
   "kind": "external research",
   "found_by": "MCQ and item-difficulty BrainLifts (Downing 2002/2005; cognitive load theory); an evaluator gap list on untaught vocabulary and syntax.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "152",
     "quote": "if I simplified the wording of this item without changing what it tests, would it become easier? If yes, the current difficulty is at least partly extraneous."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "126",
     "quote": "N5: linguistic validity. Untaught vocabulary or syntax can create construct-irrelevant difficulty."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Tag an item's cognitive level by the process it requires, not by its pass rate; a judge prompted with the same mixed-up definitions will confirm the mistake.",
   "kind": "external research",
   "found_by": "MCQ and item-difficulty BrainLifts: difficulty and cognitive level vary independently, and a judge given the same mixed-up definitions repeats the error.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "73",
     "quote": "When tagging items by cognitive level, describe the cognitive process required, not the expected pass rate."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0161-assessment-item-difficulty-core.qmd",
     "lines": "96",
     "quote": "your \"difficulty alignment\" check will confirm the misclassification because it's using the same flawed definitions."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Size a check to the decision it supports: five items can't support a mastery call, and on a short test a percentage bar can quietly demand a perfect score.",
   "kind": "external research",
   "found_by": "Spearman-Brown reasoning in an MCQ BrainLift (10–15 items for cautious calls, 20–30 for summative ones); an evaluator gap list flags the gate-arithmetic trap.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "188",
     "quote": "a 5-item MCQ quiz is useful for retrieval practice and rough formative diagnosis but is too unreliable for mastery decisions."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "141",
     "quote": "gate-arithmetic trap where small tests make 90 percent require a perfect score;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    15
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A percent-correct mastery bar means something only under fixed task conditions; set it per skill by weighing the cost of a false pass against a false fail.",
   "kind": "external research",
   "found_by": "Assessment-as-signal BrainLift (Zhang et al. 2025, DOI 10.5281/zenodo.15870292; Pelánek & Řihák 2018).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd",
     "lines": "60",
     "quote": "Percent-correct only means something when task difficulty and evidence conditions are held steady; otherwise it is entangled with item easiness, scaffolding, and cueing."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "88",
     "quote": "define mastery through controlled evidence and downstream risk, not a global raw `90%`;"
    }
   ],
   "against": "kb-0028 line 21: \"**Enforce mastery gates at ≥90% accuracy.**\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A mastery system needs a third outcome, switching to reteaching, for when practice stops producing gains; without it, persistence becomes the real pass criterion.",
   "kind": "external research",
   "found_by": "Assessment-as-signal BrainLift (Beck & Gong 2013 on wheel-spinning), which notes the platform simply let failing learners keep attempting.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd",
     "lines": "65",
     "quote": "A mastery system that lacks an explicit \"switch mode\" state will inevitably turn persistence into the hidden criterion for passing."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0157-mastery-signal-evidence-base.qmd",
     "lines": "430",
     "quote": "when a learner is failing, we currently just let them keep attempting items."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "After reteaching, confirm recovery with different evidence, such as new items or near-miss variants, not the items used to reteach.",
   "kind": "external research",
   "found_by": "Assessment-as-signal BrainLift; an independent audit of an AP course required a different-evidence retry for every criterion.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd",
     "lines": "230",
     "quote": "After corrective instruction, the system should re-check using near-miss and transfer variants to confirm the misconception was actually repaired, not merely coached."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "67-68",
     "quote": "Rebuild every assessment and writing criterion as failed function -> relevant taught check -> different-evidence retry."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "The student's independent task must not reuse evidence the worked example already used; keep scored claims separate from taught claims.",
   "kind": "measured",
   "found_by": "An independent audit blocked an AP course because its independent tasks reused answer-bearing evidence from the model. Another course wrote the separation in as an invariant.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "64",
     "quote": "Replace independent tasks that reuse answer-bearing modeled evidence in Lessons 1, 3, and 6."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd",
     "lines": "81-82",
     "quote": "\"Independent item claim_ids must be a subset of independent_claim_ids and disjoint from teaching_claim_ids\")"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Decide whether an item checks taught knowledge or tests transfer before judging its overlap with the teaching; the same overlap is correct in one and a leak in the other.",
   "kind": "measured",
   "found_by": "It took five adversarial rounds to isolate this. Where locating the answer in the source is the skill, the usual 'answer is in the source' leak check does not apply.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "47",
     "quote": "An in-lesson knowledge check answerable from explicitly-taught knowledge is legitimate (that's what checking taught knowledge means); the same overlap in a comprehension/transfer item is a leak."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "26-27",
     "quote": "in reading, finding the answer in the passage IS the skill, so the usual history-style \"answer is in the source\" leak check is deliberately skipped."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't make the retry harder after a miss; reteach first.",
   "kind": "measured",
   "found_by": "In a course already in use, difficulty rose after a miss and attempt-2 accuracy fell from 64% to 41%.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "37",
     "quote": "| 4 | Retry makes students worse | Difficulty escalates after a miss; attempt-2 supporting-detail accuracy **64% -> 41%** |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Re-run blind-solve checks with the current, strongest solver; an item that resisted an older model can leak to a newer one.",
   "kind": "measured",
   "found_by": "An item that resisted the older solver plainly blind (0/3) was solved 3/3 by the newer model in a replay.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "33",
     "quote": "Current Gemini 3.5 replay: 3/3 in both conditions - direct blind leak; old lift is historical."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "53",
     "quote": "invalidation by a stronger current plain-blind solver; stale solver results are not certification."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "37",
     "quote": "cert stamp + recert (re-run on drift/flip/generator-version bump)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A blind solver's low self-reported confidence does not cancel exact recoveries of the key; count repeated exact hits as leaks.",
   "kind": "measured",
   "found_by": "A sealed rule passed an item the solver recovered exactly 3 times in 8 because it reported low confidence; a later objective overlay reversed the pass.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "43-45",
     "quote": "Promotion review found `r3-09` at 3/8 exact plain-blind recovery and 0.71875 mean partial accuracy; the sealed rule had ignored those hits because the solver reported low confidence."
    }
   ],
   "against": "kb-0100 lines 39-40: \"the loosened bar correctly discards low-confidence forced guesses\"",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Calibrate the blind solver itself; one that bluffs with test-taking tricks inflates leak rates, so let it answer 'unknown' when the source is genuinely needed.",
   "kind": "measured",
   "found_by": "A solver role-playing a clever child scored 1.0 blind on items that needed the text. A re-baselined solver answered UNKNOWN, and 10 flagged items certified clean.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "31",
     "quote": "it returned blind accuracy of `1.0` on items that genuinely needed the passage."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "70",
     "quote": "A solver that can bluff its way through without the passage will inflate leak rates."
    }
   ],
   "against": "kb-0120 lines 59-60: \"model self-confidence cannot erase exact blind recoveries.\"",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure a generator on one attempt per preregistered item against a fixed denominator, with no retries, reranking, repair, cache or hidden selection, and report served or best-of-N results separately.",
   "kind": "measured",
   "found_by": "An AP generator's headline 99% came from build-time best-of-N plus serving from cache, not from the model generating.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "58-60",
     "quote": "Raw generator quality is `raw_k1`: one candidate, one attempt, no retry, reranking, repair, cache substitution, rejection sampling, best-of-N, or hidden human selection."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "9",
     "quote": "BUT the headline '99%' is a build-time best-of-N + serve-from-cache EXPLOIT (SCOREBOARD_99 itself: 'NOT the model generating'), which violates the K=1/no-BoN constraint"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    65,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count unique, eligible items and check the spread of what survives; gross row counts and template-stamped passes hide a thin, duplicated bank.",
   "kind": "measured",
   "found_by": "An AP corpus of 143,026 gross rows held 49,571 unique eligible items, and a claim of 100,000 usable items was rejected. In another bank, 8,937 passes hid formats that never survived strict QA.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "74",
     "quote": "- 49,571 sampling-eligible exact unique candidate bodies;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
     "lines": "74-75",
     "quote": "0/8,937 sequence/match survive strict QA"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "At the gate, treat a check that never ran, and any output that is empty, invalid, timed out or unscorable, as a failure, never as a pass.",
   "kind": "measured",
   "found_by": "The keystone answerability check had never actually run, yet items carried its label. An experiment protocol fixed unscorable outputs as failures.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
     "lines": "48-49",
     "quote": "The cold-transfer keystone is a LABEL, not a measurement."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "316",
     "quote": "Invalid, empty, timed-out, or unscorable artifacts are failures."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28,
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check what an output must contain as well as what it must avoid; an empty or minimal output that breaks no rule still fails.",
   "kind": "adopted rule",
   "found_by": "An experiment design guarding against outputs that pass by doing nothing.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "405-406",
     "quote": "Positive obligations and prohibitions are both required; an empty/minimal artifact fails completeness even if it avoids violations."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Score a judge against person-labelled cases: report recall on the rare decision against an always-majority baseline, and hold it to the agreement independent people reach; a model verifier can only audit.",
   "kind": "adopted rule",
   "found_by": "An experiment design guarding against class imbalance passing for accuracy.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "318-319",
     "quote": "report per-rule macro-F1 and minority-decision recall so class imbalance cannot masquerade as contract obedience."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "403-404",
     "quote": "A different-family LLM verifier is audit-only and cannot establish the ceiling or headline result."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    37,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep missing, ambiguous and conflicting answers marked as such until a person rules on them; never infer them, and label anything built on unattributed rules as provisional.",
   "kind": "adopted rule",
   "found_by": "Corpus-intake rules for a pedagogy decision bank, and a rulings corpus in which 1,715 records lacked a date or authority.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "151-152",
     "quote": "No answer may be inferred merely because a question is phrased yes/no. Missing stays `missing`; ambiguous stays `ambiguous`; conflicting sources stay in conflict until adjudicated."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0242-decision-matrix-judgment-corpus.qmd",
     "lines": "69-70",
     "quote": "but any eval probe built on them must be labeled provisional."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9,
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Passing a format or schema check proves the shape of an output, not that it embodies the intended teaching.",
   "kind": "adopted rule",
   "found_by": "Schema-valid course files and outputs were separated from pedagogy claims during experiment and standard design.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "117",
     "quote": "Shape validity does not establish semantic compliance."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "117-118",
     "quote": "schema validity is a document-integrity floor only, never a course-quality/child-readiness/outcome verdict."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "No writer, whether model, agent or lane, may certify its own output; its self-reported compliance is not evidence.",
   "kind": "adopted rule",
   "found_by": "The doctrine rejected unaudited self-assessment by models as empirically worthless; experiment and routing rules forbid self-certification.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "255",
     "quote": "A model may assist extraction but may not certify its own atom."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "26",
     "quote": "unaudited LLM self-assessment of its own content (empirically worthless — see DOK1-11)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "157-158",
     "quote": "no lane can self-certify the whole course."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    61,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A model's score on pedagogy-knowledge questions is not evidence that the content it generates teaches well; measure the generated content itself.",
   "kind": "external research",
   "found_by": "The paper's own stated limitation (DOI 10.3389/frai.2026.1851993) and the doctrine that knowing pedagogy and generating aligned content are separate capabilities.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0124-eduqwen-pedagogical-llm-paper.qmd",
     "lines": "94-95",
     "quote": "strong benchmark performance on pedagogical knowledge questions does not itself constitute evidence of effective classroom tutoring"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "46",
     "quote": "Knowing-that (answering pedagogy questions) and generating-aligned (producing content that embodies the pedagogy) are different capabilities"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give a writer model only the few rules that apply to the piece at hand, not the whole rulebook; rule-following falls as instructions get harder.",
   "kind": "external research",
   "found_by": "Across 18 models, constraint adherence fell as instruction difficulty rose (Ye et al., 2026, https://aclanthology.org/2026.findings-acl.99/).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
     "lines": "73-74",
     "quote": "across 18 models, constraint adherence fell materially as instruction difficulty increased"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "285",
     "quote": "The raw bank never enters the renderer prompt."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    62
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Different models follow the same explicit rule contract very differently; qualify each model and version separately, and test that rules aren't applied outside their scope.",
   "kind": "measured",
   "found_by": "On one frozen 20-case contract, exact compliance ranged from 60/140 to 136/140 rows across three models. 43 of 157 misses were rules applied outside their scope (the negative-control gate).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd",
     "lines": "79-81",
     "quote": "| OpenAI | 60/140 | 0/20 |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd",
     "lines": "89",
     "quote": "- negative-control gate: 43;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
     "lines": "46",
     "quote": "every model/version requires conformance qualification."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    29,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't let a model pick the sequence or merge sources on its own taste: give it the progression policy, and process sources in authority order instead of blending them in one pass.",
   "kind": "adopted rule",
   "found_by": "Curriculum-architecture doctrine: one-pass blending averages conflicts and smuggles in scope, and an unguided sequence imports arbitrary assumptions.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "74",
     "quote": "the sequence will reflect whatever assumptions the model happens to import"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "67",
     "quote": "is not synthesis at all; it is compromise"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    29,
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When combining standards from several sources, keep each source's specifics inside the shared node; merging them into one abstract description loses what teaching needs.",
   "kind": "measured",
   "found_by": "An attempt to merge similar standards from several jurisdictions into single nodes produced descriptions too vague to drive lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd",
     "lines": "51",
     "quote": "The result was flattened abstractions that lost the specificity needed for teaching."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Count a prerequisite as met only when it is fluent enough not to load working memory, and beware teaching a restricted case apart from the general case, which can create a misconception.",
   "kind": "adopted rule",
   "found_by": "Curriculum-architecture doctrine on the failure modes of graph decisions.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "63",
     "quote": "A prerequisite that is technically met but not automated enough to free working memory makes the target skill unteachable."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "62",
     "quote": "Splitting a restricted case from a general case (e.g., same-denominator before unlike-denominator fractions) causes students to build predictive models that become entrenched and must be actively undone."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Mark pairs students commonly confuse: keep them apart during first teaching, then interleave them once both are learned.",
   "kind": "external research",
   "found_by": "Graph-architecture doctrine, plus Rohrer (2012): interleaving trains discrimination, but novices may need blocked exposure first.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd",
     "lines": "80",
     "quote": "where interleaving after both are learned builds discrimination"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0119-curriculum-architecture-brainlift-evidence.qmd",
     "lines": "240",
     "quote": "Novices may need initial blocked exposure before productive interleaving."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep earlier knowledge alive by making later lessons use it, revisit an idea only with a real upgrade and say what is new, and leave isolated spaced review for what's left over.",
   "kind": "adopted rule",
   "found_by": "Curriculum-architecture doctrine; a curriculum ledger notes 'what is new' on every spiral-review row.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "82",
     "quote": "use the curriculum to keep generative knowledge warm by use; use spaced practice for the residue."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "131",
     "quote": "The strong version is a learning progression: each revisit adds a real upgrade"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd",
     "lines": "41",
     "quote": "[Spiral review of G2 Unit 2, A3-A4 — what is new:"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Shrink guidance and grow independent work as expertise grows; heavy guidance helps novices but slows learners who already know the material.",
   "kind": "external research",
   "found_by": "The expertise reversal effect (Kalyuga, Ayres, Chandler & Sweller 2003, Educational Psychologist 38(1)), cited by a lesson design spec.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "284",
     "quote": "The expertise reversal effect (Kalyuga et al.): heavy guidance helps novices but slows down learners who already know the material."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Pair plausible wrong options with corrective feedback; without it, students later reproduce the wrong options as facts.",
   "kind": "external research",
   "found_by": "The negative suggestion effect (Roediger & Marsh 2005) and its reduction by feedback (Butler & Roediger 2008, Memory & Cognition 36(3)).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "176",
     "quote": "Without feedback, the negative suggestion effect persists."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "95-96",
     "quote": "potent misconception-based distractors require product-appropriate corrective feedback or post-test correction because plausible lures can seed false knowledge;"
    }
   ],
   "against": "kb-0183 lines 135-136: \"a single-select (`mcq`) item is *never* revealed after N tries\"",
   "adds_to_existing": [
    1,
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Use only as many options as you can make plausible (research favours three), and never add a filler option to reach a count.",
   "kind": "external research",
   "found_by": "Rodriguez (2005) meta-analysis and Elraiyah et al. (2025), as summarised in an MCQ BrainLift.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "69",
     "quote": "A weak fourth distractor is worse than no fourth distractor because it provides testwiseness cues and wastes time."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "104-105",
     "quote": "An agent must not resolve this by adding filler"
    }
   ],
   "against": "kb-0136 line 112: \"MCQs need at least four options.\" (a reviewer request; a four-option rule was later adopted)",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Cover the options: a student who knows the material should be able to answer from the stem alone.",
   "kind": "external research",
   "found_by": "MCQ item-writing guidance (Haladyna, Downing & Rodriguez 2002, as summarised).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "65",
     "quote": "read the stem, cover the options, and ask whether a knowledgeable student could formulate an answer."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "An item is higher-order only if it presents material the student hasn't met; a longer stem doesn't turn recall into analysis.",
   "kind": "external research",
   "found_by": "An MCQ BrainLift's novel-stimulus requirement.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "58",
     "quote": "no new material, no higher-order thinking."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "After real use, review each item's statistics: investigate items that strong students get wrong more often than weak ones, and distractors favoured by strong students (often a wrong key); drop distractors almost no one picks.",
   "kind": "external research",
   "found_by": "Item-analysis guidance in an MCQ BrainLift; retirement thresholds in an assessment design.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "85",
     "quote": "A distractor selected more by high-performing students than low-performing students suggests the keyed answer is wrong or ambiguous."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd",
     "lines": "204",
     "quote": "item retirement (INFIT > 1.30 or pt-biserial < 0.20)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    39,
    59
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check an assembled test for items that cue, duplicate or contradict each other, and for neighbouring items that prime later answers.",
   "kind": "external research",
   "found_by": "MCQ and pattern-library BrainLifts (enemy items; proximity and priming audit).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "81",
     "quote": "Cueing enemies: one item's stem or options give away the answer to another."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "280",
     "quote": "A preceding item defines \"opportunity cost,\" making the next item easier; fine for an in-lesson quiz, risky for \"stable mastery\" claims."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mark short explanations with a small rubric of 0/1/2 checks rather than an ever-growing list of accepted answers; switch when the list passes about 15–20 variants or the key keeps being patched.",
   "kind": "external research",
   "found_by": "The 'scoring-complexity paradox' in the assessment pattern library.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "160",
     "quote": "Default: use a micro-rubric (0/1/2) for short text and explanations."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "163",
     "quote": "Your \"acceptable answers\" list exceeds ~15–20 variants."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    10,
    69
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Run a conversational check as a fixed script with set prompts, capped follow-ups and declared supports; free chat leads the witness.",
   "kind": "external research",
   "found_by": "The assessment pattern library's guidance on oral and LLM-conversational tasks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "564",
     "quote": "State machine, not free chat"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "555",
     "quote": "Ungoverned LLM prompts can lead the witness (construct creep and validity loss)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give every spoken-response task a text fallback of equal status, and don't let speech-recognition errors count against content.",
   "kind": "external research",
   "found_by": "The assessment pattern library, citing ASR disparities (Koenecke et al., PNAS, https://www.pnas.org/doi/pdf/10.1073/pnas.1915768117).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "567",
     "quote": "Always provide a text-response fallback of equal status"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "539",
     "quote": "Evidence of racial disparities in major ASR systems"
    }
   ],
   "against": "kb-0181 lines 61-62 (a ruling requiring spoken say-back): \"a child with no working microphone has no fallback here.\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Label how much support each task gives, and base decisions on unaided work; success with scaffolds is weaker evidence, and any claim must say what support was given.",
   "kind": "external research",
   "found_by": "Pattern-library, assessment-pack and assessment-signal BrainLifts.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "72",
     "quote": "base high-stakes decisions on the first unaided check (or transfer task) that follows."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0153-assessment-pack-brainlift.qmd",
     "lines": "61",
     "quote": "The amount of scaffolding and guidance in a task directly affects its difficulty and therefore has implications for how we interpret student attainment."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Say what each assessment is for (formative, mastery, diagnostic, placement, summative or cold transfer) before reading its result; one instrument can't do all of these jobs.",
   "kind": "external research",
   "found_by": "Assessment BrainLifts: finding where to start and finding gaps are different problems needing different designs.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "89-90",
     "quote": "declare whether a resource is formative, mastery, diagnostic, summative, or cold measurement before interpreting its result;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "102",
     "quote": "Trying to do both at once with a single instrument wastes items and confuses the design."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In any record of what a student knows, keep 'not tested' separate from 'not known'.",
   "kind": "external research",
   "found_by": "The diagnostic assessment BrainLift and its evidence base.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "75",
     "quote": "An unassessed KC is not the same as a failed KC, and conflating the two is one of the most common errors in diagnostic systems."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "To diagnose, test one piece of knowledge per item in the plainest format; exam-style items bundle content with format skill and elimination, so a miss can't show what is missing.",
   "kind": "external research",
   "found_by": "The diagnostic BrainLift, worked through AP courses; the project noted that a completed AP practice test did not establish topic-level knowledge.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "68",
     "quote": "The question is evaluative (it tells you whether the student can do this task) but not diagnostic (it doesn't tell you what's missing)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0155-diagnostic-assessment-evidence-base.qmd",
     "lines": "255",
     "quote": "The completed practice test is insufficient to establish this proficiency at topic level."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "With few students per item, run on expert-set defaults and simple rules; 'optimal' adaptive algorithms on uncalibrated items do no better, and revising an item resets its data.",
   "kind": "external research",
   "found_by": "The diagnostic BrainLift: at about 10 students per course, the 100-200+ responses per item needed for calibration take years to collect.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "117",
     "quote": "will outperform a statistically \"optimal\" approach running on uncalibrated data."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "115",
     "quote": "If items are revised (as they should be, based on early evidence), the clock resets."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    15
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge a diagnostic by whether students who follow its routing learn faster, and stop testing when the next item is worth less than the study time it costs.",
   "kind": "external research",
   "found_by": "The diagnostic BrainLift's routing-not-measurement position.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "77",
     "quote": "do students who follow its recommendations learn more efficiently than students who don't?"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "40",
     "quote": "test until the expected value of the next item (in terms of improved routing) is lower than the expected value of the student spending that time studying"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Treat any predicted item difficulty as a starting estimate that carries its method, sample size and uncertainty; don't set cut scores on it until real responses, on the order of 200 per item, replace it.",
   "kind": "measured",
   "found_by": "Both simulation misses in a proxy test (reliability 0.928 vs ≥0.93; RMSE 4.12 vs <4.0) traced to expert-assigned difficulties.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd",
     "lines": "94-95",
     "quote": "Both misses trace to one root cause: **item difficulties are expert-assigned, not estimated from student responses**."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0161-assessment-item-difficulty-core.qmd",
     "lines": "190",
     "quote": "\"<200 responses ⇒ item difficulty is provisional; do not use to set cuts\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Don't ask a model directly how hard an item is for students; models underestimate difficulty, and more capable ones do so more. Have it extract features, or compare the item against calibrated anchors.",
   "kind": "external research",
   "found_by": "Cold-start difficulty BrainLift (Li et al. 2025; Razavi & Powers 2025; BEA 2024 shared task).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "43",
     "quote": "scaling up model capability does not improve difficulty alignment with human learners — it often makes it worse."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "41",
     "quote": "Direct LLM ratings show moderate correlations with empirical difficulty at best (often r ≈ 0.4–0.6)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    31,
    32
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report each readiness gate on its own; averaging them into one score hides the gates sitting at zero.",
   "kind": "adopted rule",
   "found_by": "An AP course was 100% authored but 0% reviewed, certified and runtime-verified, so it was reported gate by gate.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0171-apush-full-course-local-authoring-review-hub-archive.qmd",
     "lines": "50",
     "quote": "Do not average the independent readiness gates into a fake single quality score."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    59,
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Status summaries drift rosier than the records; regenerate them from the certified files, and never cite a pass that no on-disk record backs.",
   "kind": "measured",
   "found_by": "A briefing cited a passing course found in no record, while the certified file recorded 3 failures; course metadata claimed 5 edge types where the schema defined 4.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
     "lines": "62-63",
     "quote": "regenerate views FROM the certified files; never cite a PASS no on-disk COMPLIANCE.md + fresh pull backs."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0122-g3-reading-course-graph.qmd",
     "lines": "82-83",
     "quote": "earlier metadata said \"5 edge types\" while both the builder and the enumerated schema define exactly four."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Recompute every check and headline number from the content and raw records; don't trust an author's annotation or a harness's own summary.",
   "kind": "measured",
   "found_by": "A fresh unit reproduced a leak that its annotation said was fixed; judge calibration was recomputed from raw per-call records.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "50-51",
     "quote": "trust the recompute, not the annotation"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "54-55",
     "quote": "adversarially recomputed from the raw per-call JSONL (not trusted from the run harness's own summary)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    61,
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An exemption from a check must be explicitly granted and cost a measured replacement outcome, and a list of known exceptions may only shrink.",
   "kind": "adopted rule",
   "found_by": "A self-declared exemption was found to let any course skip every outcome row.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
     "lines": "55",
     "quote": "so it costs an outcome, not waives one."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "68",
     "quote": "(can only shrink, never padded to pass a build)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Turn every class of review comment into a dated rule and an automated check, so the same comment never has to be made twice.",
   "kind": "adopted rule",
   "found_by": "Repeated review comments; for example, 7 of 9 taught words appeared only once until a validator was added.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "59",
     "quote": "no reviewer ever makes the same class of comment twice"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "65-66",
     "quote": "from 7/9 taught words appearing only once"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Expect about one audit finding in ten to be false; verify each finding before fixing it.",
   "kind": "measured",
   "found_by": "A content audit's false-positive rate was 6/65, matching another lane's measured 8-15%.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "101",
     "quote": "**6/65 = 9%**, independently matching the arc-audit lane's measured 8-15%."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build the student-facing view from an allowlist that excludes answer-bearing fields meant only for teachers, and test that view for answer leakage.",
   "kind": "measured",
   "found_by": "An independent audit of an AP course required a student-only source view before the course could be copied forward.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "71-72",
     "quote": "Define a student-only source projection containing `student_material` plus approved citation metadata, excluding teacher-only answer-bearing fields."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "125-126",
     "quote": "mutation tests for student-answer leakage"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    30
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Model inferences only from what the source itself supplies; never rely on outside cultural facts it doesn't give.",
   "kind": "adopted rule",
   "found_by": "A worked example was struck because its extension reached for outside-world knowledge that students may lack.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "80-81",
     "quote": "an inference may only use what the passage's own words show"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "139",
     "quote": "Only context students will need in Act 1, not general history."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every claim about the source in a stem, model answer or feedback line must trace to the source's own words; invented causes and unsupported 'only' claims are defects.",
   "kind": "measured",
   "found_by": "A live walkthrough found untrue-to-story lines (an invented cause, unsupported absolutes), which were fixed in a batch.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "167-168",
     "quote": "must be directly traceable to the passage's own words — invented causes and unsupported superlatives are a defect class, not a style choice"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test any copy-detection guard against correct answers; with a long target sentence, exact correct recall gets marked as copying.",
   "kind": "measured",
   "found_by": "An 86-character recall sentence failed the checker's echo guard while a 66-character one passed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "194-195",
     "quote": "misreads a child's exact, correct recall as an illegitimate copy and demotes it"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    36,
    10
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Tie each option's feedback to the option itself, not to its position, so shuffling the options keeps the feedback correct.",
   "kind": "measured",
   "found_by": "A re-review found generic and position-keyed feedback; the shipped bank was driven to zero position fallbacks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
     "lines": "38-39",
     "quote": "zero option-position fallback IDs and zero truncated claim/recheck templates"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Present every model or diagram as a simplification, not literal reality.",
   "kind": "adopted rule",
   "found_by": "Cross-subject misconception guidance: students take models literally, so every model needs a 'this is simplified' framing.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0141-cross-cutting-science-misconception-synthesis.qmd",
     "lines": "144",
     "quote": "it MUST include a brief framing statement indicating that the model is a simplification."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "66",
     "quote": "diagrams or models presented as literal reality;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When content carries another subject's ideas, revisit what that subject has taught from a fresh angle, keep its framing, check it against that subject's misconception list, and don't make it the first place students meet a new concept.",
   "kind": "adopted rule",
   "found_by": "Cross-subject guidance written because it is unknown what a student has already studied in the other subject.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "36",
     "quote": "the Read/Write lesson should be consistent with how it was framed in the subject app"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "75",
     "quote": "must go through the misconception-check process."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "81",
     "quote": "It is better to re-encounter ideas from earlier grades than for Alpha Read or Alpha Write to be the first place a student meets an idea."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose content by a visible, scored rule that others can challenge, and let a person override it with a stated reason.",
   "kind": "adopted rule",
   "found_by": "Reviewers praised a testable topic-selection formula and a reasoned override.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "17",
     "quote": "Scoring topic selection with a formula is the reviewers' favorite feature because it is testable."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "18",
     "quote": "A person overrode the score and gave a reason rather than allowing the number to decide."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "State each unit's target as one plain, testable sentence, and link units through big ideas rather than surface facts.",
   "kind": "adopted rule",
   "found_by": "Reviewers asked for a key understanding on every unit and found links between units that matched only surface facts.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "51",
     "quote": "one plain-language sentence stating what the whole unit is really about."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "52",
     "quote": "Make cross-unit links about big ideas rather than surface facts."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "What a test asks shapes what gets taught; if the default check is a short source with a few multiple-choice questions, teaching narrows to that.",
   "kind": "external research",
   "found_by": "RAND Reading Study Group, MR-1465 (2002), Appendix B.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0108-rand-appendix-b-assessment-rfa.qmd",
     "lines": "127-131",
     "quote": "as long as we define comprehension by default as reading a passage and answering a few multiple-choice questions about it, teachers will have little incentive to instruct children in ways that reflect a deeper and more accurate conceptualization of the construct."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Agreement that comes from one source copied twice is not independent replication.",
   "kind": "measured",
   "found_by": "A claimed convergence between two projects turned out to be one author carrying findings from one to the other.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "30-31",
     "quote": "not two teams replicating independently. Treat it as a hypothesis-transfer, not a cross-validated law."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Label machine-written and machine-checked material for what it is; never call it authentic, cleared or certified.",
   "kind": "adopted rule",
   "found_by": "Machine-written sources risked being called 'real', and showcase items called 'cleared' were only machine-checked.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "44-45",
     "quote": "don't relabel machine-authored cold passages as \"real.\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "120-121",
     "quote": "Replace the two remaining `cleared` phrases in MCQ/MCQ_SET with `machine-checked` or `selected`."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Open question: can item- or lesson-level benchmarks judge how a course sequences and builds knowledge across units, or does course quality need course-level measures?",
   "kind": "open question",
   "found_by": "The team questioned whether its benchmark could measure sequencing and pedagogy.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0125-coe-catchup-2026-07-13.qmd",
     "lines": "101-103",
     "quote": "useful at question/lesson level, but new metrics are needed to assess lesson sequencing and knowledge building"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Open question: should named thinking routines fade once a stated condition is met, or keep returning as scheduled retrieval?",
   "kind": "open question",
   "found_by": "This is held as a dispute in the doctrine; the ruled fade (after five successful uses) was never implemented.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "41",
     "quote": "named inference routines as *fading scaffolds* retired on a stated condition (our stance, per Willingham DOK1-3) vs. scheduled recurring retrieval of the routine"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "41-42",
     "quote": "scaffolds fade across a unit (a procedure \"collapses into a two-step option after five successful uses,\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Open question: for spaced review, is it better to keep fine-grained knowledge units and cluster them, or merge them into fewer, richer units?",
   "kind": "open question",
   "found_by": "The graph-architecture doctrine leaves the question unresolved.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd",
     "lines": "83",
     "quote": "There is one proven response and one speculative alternative, and it is not yet clear which is better."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Open question: should mastery checks use the formats practised during teaching, or should practice deliberately differ from the final test's format?",
   "kind": "open question",
   "found_by": "Direct Instruction doctrine conflicts with the 'marathon rule', while measurement guidance treats format familiarity as hygiene.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "140",
     "quote": "Mastery tests should match formats experienced during instruction."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "61",
     "quote": "Assessment format is not instruction format (the marathon rule)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd",
     "lines": "123-124",
     "quote": "Format familiarity is measurement hygiene, not test prep (construct-irrelevant variance, AERA/APA/NCME Standard 1.13)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Adjust feedback and help as proficiency grows; too much lowers active processing and masks misconceptions, too little leaves students floundering.",
   "kind": "external research",
   "found_by": "The practice BrainLift and the assistance dilemma (Koedinger & Aleven 2007, Educational Psychology Review 19).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "161",
     "quote": "Too much feedback can reduce active processing; feedback timing should shift as proficiency improves."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0157-mastery-signal-evidence-base.qmd",
     "lines": "437",
     "quote": "Explains why simply increasing support (hints/steps) can raise short-term success without improving learning, and why too little support produces floundering."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A mastery check should vary the surface form, include near-miss contrasts, and withhold scaffolds and feedback, so it tests the intended generalisation rather than same-day recall.",
   "kind": "external research",
   "found_by": "Assessment-signal and practice BrainLifts on acquisition versus durable mastery.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd",
     "lines": "238",
     "quote": "first-exposure gating must include surface variation and near-miss contrasts—not only isomorphic items."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "158",
     "quote": "E4 mastery gate: no feedback, delayed, varied, independent."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep content-file checks, live walkthroughs and package or claim audits apart; a content check must not claim how the lesson behaves at runtime.",
   "kind": "adopted rule",
   "found_by": "An evaluator gap analysis separated three rings of checks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "52-53",
     "quote": "InceptBench should not overclaim runtime behavior or package truth."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24,
    44,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Declare what a product is, a teaching course or a practice and assessment tool, before judging it; the declaration decides which criteria apply.",
   "kind": "adopted rule",
   "found_by": "Reviewers judged a practice engine as if it were a course, and said a practice-app frame would change their recommendations.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "135",
     "quote": "product-type declaration: comprehension curriculum vs MAP-practice determines applicable criteria;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When reviewing, define the student as the full range of real users, including below-level readers, language learners, keyboard and screen-reader users, guessers and click-throughs, not one ideal path.",
   "kind": "adopted rule",
   "found_by": "A framework for what academic reviewers would criticise.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0092-student-ready-criticism-framework-2026-07-09.qmd",
     "lines": "23-24",
     "quote": "A student is not a solver, a row in a ledger, a completed QTI attempt, or an ideal reviewer clicking the intended path."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0092-student-ready-criticism-framework-2026-07-09.qmd",
     "lines": "25-27",
     "quote": "Include below-grade readers, English learners, keyboard-only users, screen-reader users, frustrated students, test-wise students, and students willing to click through or guess."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    46,
    47
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A stem must not contain, define or share the root of what it tests.",
   "kind": "measured",
   "found_by": "A template defined the affix in the stem of the very vocabulary item testing it, and a census flagged stems that contained the tested word's root.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "48-49",
     "quote": "pre-defined the affix in the stem → rewritten to be passage-dependent"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "51-52",
     "quote": "**VOCAB-ROOT-IN-STEM** (a stem contains the root of the taught word it is testing)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3,
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report completion alongside accuracy; accuracy among the few who finish says little when most students don't.",
   "kind": "measured",
   "found_by": "In the course already in use, median completion was 12.5% of intended work, while sub-skill accuracy was measured only on items students completed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "34",
     "quote": "| 1 | No completion mechanism | ~30% of intended work done; **median completion 12.5%**; ~0 net acceleration (+0.026 grades-ahead) |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": true
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
   "lines": "118",
   "quote": "A wrong answer is told why it is wrong and where to go, never what the answer is"
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
   "lines": "130-131",
   "quote": "were handing over the Step 3-4 answer outright; fix was to rewrite to criterion cues only"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "43",
   "quote": "an immediately available hint lowers desirable difficulty. The durable rule is attempt first, then targeted help."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
   "lines": "63",
   "quote": "design-science pilot reported more consistent scaffolding and less premature answer-giving"
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
   "lines": "135-137",
   "quote": "a single-select (`mcq`) item is *never* revealed after N tries (`validate-contracts.mjs` fails an `mcq` carrying `reveal_after_tries`), because a short, closed option list lets the child eliminate their way to the answer"
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
   "lines": "50",
   "quote": "with no explanation and no correct answer shown"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
   "lines": "66-67",
   "quote": "~78% of raw generated items were blind-solvable before this gate; G5 bank certified 1.67%/0%/0% across 172 items"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
   "lines": "45",
   "quote": "An item answerable without the passage is not measuring reading"
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd",
   "lines": "182",
   "quote": "LLM ablation may false-positive/negative vs real students"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
   "lines": "50-51",
   "quote": "(correct answers were ~75% option \"A\" → shuffled ~even A/B/C/D)"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "56",
   "quote": "Key-position/length balance needs an authoring-time check (12/19 A-keys shipped before the lens)."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
   "lines": "56",
   "quote": "positional bias of B ≈ 30%, C ≈ 29% vs. A ≈ 19%, D ≈ 22%"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
   "lines": "70-71",
   "quote": "preflight refuses a keyless judge (\"HARNESS, NOT CONTENT\" — 2026-09-03 cost 11 phantom FAILs once)"
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
   "lines": "629",
   "quote": "If language mechanics are not part of the claim, either score them separately or don't score them."
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
   "lines": "64",
   "quote": "all three evaluators have Step-0 injection veto;"
  },
  {
   "truth": 13,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0153-assessment-pack-brainlift.qmd",
   "lines": "120",
   "quote": "pre-specify acceptable variants (equivalence classes) and typical partial solutions (near-misses)"
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
   "lines": "71",
   "quote": "a single correct answer is not proof of knowledge and a single incorrect answer is not proof of ignorance."
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
   "lines": "159",
   "quote": "so that a single lucky guess or unlucky slip doesn't derail the binary search."
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
   "lines": "38-39",
   "quote": "Open Source Shakespeare numbers it 43, and Gutenberg and MIT have no numbers."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0115-reading-science-folder-2026-07-10.qmd",
   "lines": "59-60",
   "quote": "Full texts attached by file copy, never re-emitted through a model"
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
   "lines": "139",
   "quote": "| **Context must be what the text uses.** | Recht & Leslie (1988); Smith et al. (2021) | Only context students will need in Act 1, not general history. |"
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
   "lines": "137",
   "quote": "A map, a chain-of-command diagram, and key words appearing as they're spoken."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "54-55",
   "quote": "the live-rendered surface must be reviewed, not just source artifacts."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
   "lines": "24",
   "quote": "the historical model snapshots are withdrawn after source changes."
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "31",
   "quote": "remove redundant UI prose such as instructions whose action is already obvious"
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "105",
   "quote": "rendered black text on a black background, legible only on hover."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
   "lines": "34",
   "quote": "design-time contracts alone demonstrably failed to prevent any of it."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
   "lines": "65",
   "quote": "if small wording changes cause wild swings in your predicted difficulty, the prediction is probably wrong."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
   "lines": "83-84",
   "quote": "same-model resamples (agreement = self-consistency, not cross-family agreement)"
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
   "lines": "482",
   "quote": "Models converge on machine consensus, not human difficulty."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
   "lines": "655",
   "quote": "LLM judges show left/right (or first/second) position effects and favour more verbose responses"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
   "lines": "64-65",
   "quote": "GO requires every in-scope case caught, zero false flags on controls, agreement >= 0.8. **NO-GO stands; semantic lints remain advisory.**"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0153-assessment-pack-brainlift.qmd",
   "lines": "69",
   "quote": "include an ex-post agreement check against human scoring and record thresholds for acceptable concordance."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
   "lines": "42-43",
   "quote": "drive ONE real sub-90% attempt and observe the block"
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
   "lines": "472",
   "quote": "use seeding (gold scripts) to check drift"
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
   "lines": "67",
   "quote": "Prepare knowledge -> encounter text -> model thinking -> guided same-process practice -> student articulation -> evidence check -> delayed/varied transfer"
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
   "lines": "62",
   "quote": "Students need to read the text first"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
   "lines": "55-56",
   "quote": "That green state is not the semantic verdict."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "57",
   "quote": "A clean automated report is useful pre-review evidence, never a substitute for reviewer judgment."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
   "lines": "359-360",
   "quote": "the metric and aggregation may not be changed after pilot results."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
   "lines": "9",
   "quote": "The bar was REPINNED 2026-06-08 from the original (overall >=0.85 on 99% across all 10 cells, clean K=1) down to"
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
   "lines": "612",
   "quote": "don't create ad-hoc categories after seeing scripts."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
   "lines": "99",
   "quote": "they want to click through a complete lesson exactly as a student would to confirm the flow."
  },
  {
   "truth": 47,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
   "lines": "75",
   "quote": "the model's underlying competence leaks through role-play."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "149",
   "quote": "A same-day lesson gate proves at most \"I can do it now,\" not \"I can still do it later under changed conditions.\""
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
   "lines": "19",
   "quote": "In-app success must predict performance on credible external assessments."
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0119-curriculum-architecture-brainlift-evidence.qmd",
   "lines": "226",
   "quote": "restudy feels productive, but retrieval produces stronger delayed learning."
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0033-problem.qmd",
   "lines": "88",
   "quote": "Gamification often rewards *completion* rather than *mastery*."
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
   "lines": "475",
   "quote": "Two-to-four checks: (1) correct principle stated, (2) applied to the case, (3) addresses counter-case/constraint, (4) conclusion warranted."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
   "lines": "71-72",
   "quote": "let it write only the questions) was the biggest real lever"
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
   "lines": "9",
   "quote": "aptraining's headline '0.29→0.95 via real passages' is REFUTED"
  },
  {
   "truth": 62,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0141-cross-cutting-science-misconception-synthesis.qmd",
   "lines": "214",
   "quote": "Tier 1: Absolute Prohibitions (Apply at ALL grade levels, ALL subjects)"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0075-incept-curriculum-api-g5-backbone-2026-06-30.qmd",
   "lines": "9",
   "quote": "(NOT CC/Reading/5, which is only a curated L+RL subset)"
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
   "lines": "73",
   "quote": "The \"8,937 passes\" is the served-99 best-of-N exploit reborn."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd",
   "lines": "115-117",
   "quote": "The audits found number drift in documents (0.930 vs 0.928) — which is why the gate lives in code."
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0153-assessment-pack-brainlift.qmd",
   "lines": "323",
   "quote": "rubric use can increase scoring consistency, especially when rubrics are analytic, task- or topic-specific, and supported with exemplars and/or rater training."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0100-[name]-lanes-execution-2026-07-10.qmd",
   "lines": "46-47",
   "quote": "No lift or calibrated discrimination follows."
  }
 ]
}
```
