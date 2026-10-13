# verify:kb-learning-science

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "kb-learning-science",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "statement": "Before trusting a score, high or low, test the harness that produced it: a wrong field, the wrong grader host, mis-routing or cut-off output can fake a failure, and a run that tested nothing can pass for green.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "39-41",
     "quote": "the \"stuck at ~28%\" narrative was largely **measurement artifact** (wrong field read, grader on wrong host, MCQ_SET mis-route 0→0.77, DBQ truncation 0.55→1.0 at 6000 tok)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "75-76",
     "quote": "aptraining burned weeks \"stuck at 28%\" that were **4 eval-harness bugs** — proof that an unvalidated measurement can masquerade as a real number.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "185-186",
     "quote": "never read a 0/0 verdict as green — treat it as a harness bug until proven otherwise.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "72-73",
     "quote": "half of 'audio defects' were defective checks",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "All three cited quotes are verbatim at the cited lines, and the numbers (0→0.77, 0.55→1.0, 6000 tok) match. kb-0063 says the AP generator's 28% story was 'largely' an artifact, so 'four harness bugs caused it' slightly overstates. The cited evidence only showed faked failures, so 'high or low' needed a faked pass; kb-0199 supplies one (a 0/0 run read as green). Both local aptraining snapshots end on 4 June, so the mid-June bug records can't be checked at source and the KB syntheses are the only evidence. Related to truth 38, but this one is about the measuring harness, not the content check."
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "statement": "A gain seen only under a stand-in judge doesn't count until the grader of record confirms it.",
   "kind": "measured (one case) plus adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "24-25",
     "quote": "That **0.29→0.95** jump existed only under a **discredited Gemini judge**. On the **binding grader** it **collapsed to ~28%**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "55",
     "quote": "real-grader confirmation of an uncached served KC is BLOCKED.",
     "verbatim": true
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/aptraining/workspace/comms/to_orch/2026-06-01T2032Z_ALERT_IB_grader_v266_curriculum_API_401_pivoting_gemini_judge.md",
     "lines": "38",
     "quote": "**Final mission-claim eval**: requires IB fixed.",
     "verbatim": true
    }
   ],
   "against": "kb-0064 line 36: \"The **\\\"28%\\\" was four eval-harness bugs**\". The same file, and kb-0063 lines 39-41, put the ~28% down to harness bugs, while kb-0063 line 55 says the real-grader check of this win was blocked. The two same-day AP syntheses therefore disagree on whether the binding grader ever scored the jump.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The line-9 quote is verbatim, but its key claim is contradicted between sources. kb-0064 says the jump collapsed on the binding grader; kb-0063 says that grader never confirmed it (blocked), and both files elsewhere call the 28% a harness artifact. Both agree the jump doesn't count. The project's own 1 June alert, a primary record, held the mission claim for the binding grader while a substitute judge was used internally. The statement is narrowed to what all sources support; 'can vanish under the binding grader' rested on the contested figure."
  },
  {
   "index": 2,
   "verdict": "keep",
   "statement": "A change that passes a check by removing what the check inspects is gaming the check, not fixing the item.",
   "kind": "measured (one case)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "9",
     "quote": "the actual MCQ fix was the OPPOSITE: REMOVING the stimulus so the grader's leak-probe is skipped (grader-gaming)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "26-27",
     "quote": "it was **REMOVING the stimulus** so the grader's leak-probe is skipped. That's **grader-gaming**, not a provenance win.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Verbatim in the summary (line 9) and restated in the body (lines 26-27). It is one AP case from a secondary synthesis, but the principle is general and the statement doesn't overstate it. Close in spirit to candidate 83 (an exemption must cost an outcome)."
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "statement": "Don't let a judge from the writer's own model family certify the writer's output; gate it with a different family.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "231",
     "quote": "Use a different family for the gate than for the author. Never same-family certify.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "106-108",
     "quote": "The binding gate must stay **cross-family** (solver family != generator family); IB self-certification is not anti-leak evidence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd",
     "lines": "21",
     "quote": "4/11 CONFIRMED leaks. 8/11 answerable-blind. Only 3/11 cleanly passage-dependent. → 36% leaky.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "407-408",
     "quote": "The audit-only LLM verifier cannot be from the renderer's family.",
     "verbatim": true
    }
   ],
   "against": "kb-0096 line 69: \"Blind-solve calibration matters more than judge identity alone.\" In kb-0070 the same-family benchmark never ran a passage-withheld solve, so model family and check type are confounded.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Both original quotes are verbatim, and 4/11 and 36% match. The measured case doesn't isolate model family, though: the same-family benchmark grades instructional quality and ran no blind solve. The 4 leaks show what a blind solve catches, not what a different family adds. The kb-0131 line is a preregistration rule. Recast as an adopted rule, with the project's explicit cross-family rules (kb-0091, kb-0235) as evidence."
  },
  {
   "index": 4,
   "verdict": "keep",
   "statement": "A content-quality score does not certify an item; make the answerability (leak) check a separate blocking gate.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd",
     "lines": "54",
     "quote": "IB passed all 11; the different-family blind solve failed 4.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "47",
     "quote": "separate from InceptBench, which graded answer-leaking items 1.0",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "103-104",
     "quote": "a course where every item scores IB 1.0 but 90% is blind-solvable is a failed course",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "5",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 11 items, 4 failed, and the 1.0 scores match. It overlaps truth 5 (blind solve) and the separate-blocking-check pattern of truth 58. It is kept because it adds evidence that a quality benchmark scores leaking items at 1.0, including a generated item scored 1.0 that a blind solve answered every time (kb-0235)."
  },
  {
   "index": 5,
   "verdict": "keep",
   "statement": "Run the blind solve against chance over repeated trials: an item passes only if it is answered right with the source and near chance without it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "40-41",
     "quote": "PASS if with-passage correct-rate >= 0.80 AND without-passage correct-rate <= chance-rate + 0.15 margin",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd",
     "lines": "180-181",
     "quote": "model answers without passage in >=3/5 trials at temp 0.3 = fail",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "233",
     "quote": "Always run with-passage control before blind certification.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "64-65",
     "quote": "Rejected items recovered far above chance (sequence 58% vs. 3% blind; hot-text 79% vs. 14%; match 86% vs. 41%)",
     "verbatim": true
    }
   ],
   "against": "kb-0080 line 182: \"LLM ablation may false-positive/negative vs real students\"",
   "general": true,
   "duplicate_of": "5",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim and the thresholds match (0.80, chance + 0.15, 3 of 5 trials at temperature 0.3). kb-0243 is a proposed schema and kb-0080 a benchmark hard gate. It duplicates truth 5 but adds the with-source control and a chance-relative bar (kb-0091, kb-0235). The chance level should come from the item's real scoring rule (candidate 9). The found_by line about 'rubric and regex' is not in the cited text."
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "statement": "Build items on details only the source supplies, such as invented names rather than well-known real entities; items about familiar real-world topics invite answers from general knowledge.",
   "kind": "measured (small sample)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd",
     "lines": "59",
     "quote": "prefer fictional proper nouns over real-world entities",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd",
     "lines": "47-48",
     "quote": "a world-knowledge-rich passage invites guessing; a savvy test-taker could beat it without reading.",
     "verbatim": true
    }
   ],
   "against": "kb-0235 line 105: \"Measured leak by type: MCQ 99.5%, MSQ 100%\". The multi-select tip from the 11-item run did not hold at scale. Also kb-0158 line 108, the multi-select guessing jackpot.",
   "general": true,
   "duplicate_of": "5",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. In the 11-item run the invented-names tip rests on one item and the needs-both multi-select tip on two (the per-item table at lines 30-32). A larger measurement found multi-select items 100% leaky, so that tip is dropped. The four world-knowledge items were attempted but all missed, hence 'invite' rather than 'answer'. It is a technique serving truth 5 and is kept for the world-knowledge evidence; the evidence is thin."
  },
  {
   "index": 7,
   "verdict": "keep",
   "statement": "No surface cue may give the key away: the key must not be the longest, shortest, odd-one-out or most stem-echoing option, and the item must not yield to keyword matching or elimination.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "63-64",
     "quote": "The right option must not be the longest, the shortest, the odd one out, or the one that reuses the most words from the stem.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "77",
     "quote": "79% of correct answers in a generated course sat at option position A, and the correct option was systematically the longest",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "133",
     "quote": "Closed-response items must require the target reasoning and must not be answerable by surface cues, keyword matching, option length, or test-wise elimination.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 79% and 'systematically the longest' match the census (100 multiple-choice plus 116 two-part items), and the rule is enforced by two validators (kb-0183 lines 67-70). Distinct from truth 8: this is about the shape of the options and surface cues, not position."
  },
  {
   "index": 8,
   "verdict": "keep",
   "statement": "In a two-part item, the evidence part must not restate or reveal the answer part.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "78",
     "quote": "6 of 6 sampled two-part evidence items were blind-solvable, with Part B restating Part A",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "83",
     "quote": "include prior-knowledge answerability, EBSR Part-B-restates-Part-A, and keyword-match answerability.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim and '6 of 6' matches; the same root cause measured 33% gameable in another grade (same line). It applies to any subject that uses two-part evidence items."
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "statement": "Work out each item's guessing floor from how the platform actually scores it, not from its format name.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0100-[name]-lanes-execution-2026-07-10.qmd",
     "lines": "92",
     "quote": "floors are computed per item from its responseDeclaration, never from the format label.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0100-[name]-lanes-execution-2026-07-10.qmd",
     "lines": "90-91",
     "quote": "select-k hot-text authored `cardinality=\"single\"` scores \"first submitted token in correct set\" -> floor k/n (~0.167 for 2-of-12), ~11x above 1/C(n,k).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true,
   "reason": "The rule quote sits on line 92 alone, not 91-92. The numbers check out: 2/12 ≈ 0.167 against 1/C(12,2) ≈ 0.015 is about 11x. The only source is a file whose path carries a person's name, and no other KB file reports this scoring probe."
  },
  {
   "index": 10,
   "verdict": "keep",
   "statement": "Before trusting a mastery gate, try to pass it without doing the work: click through, guess, or answer everything wrong.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "120",
     "quote": "earned a stamp on \"The Amazing Axolotl\" at about 20 percent accuracy by clicking through without reading, then advanced with the passage hidden from view.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "101",
     "quote": "In a main-idea task, reviewers earned the pass while answering every question incorrectly.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "122",
     "quote": "then demonstrate it blocking a real miss in a live walkthrough.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim ('about 20 percent', every answer wrong). It sits next to truths 38 (a check proves nothing until it catches a planted fault) and 47 (scripted readers), but names the specific gaming paths to try against a gate."
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "statement": "Every screen should ask for a response that serves the teaching, and no check may be skippable; a nudge students can click past is not a check.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "37",
     "quote": "every screen requires a specific interaction (no passive screens,",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "27",
     "quote": "The interaction must be substantive to the teaching move; a decorative tap control does not satisfy the concern.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "79",
     "quote": "the \"not so fast\" nudge is non-blocking and can be skipped by clicking Next twice.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "130",
     "quote": "skippable \"pause and think\" is not a check.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The original quotes are verbatim, but 'every screen' was only implied by them. kb-0180 line 37 states the ruling outright, and kb-0172 line 27 requires the response to serve the teaching move. The no-skip half overlaps truth 28; the every-screen half is new."
  },
  {
   "index": 12,
   "verdict": "keep-with-fix",
   "statement": "Match the response to the target: when students must explain or produce, have them produce (say, write, type), since selecting can't show it; in lessons, weight production over selection.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "124",
     "quote": "N3: recognition-vs-production match. \"Write/explain/draw\" targets cannot be assessed by MCQ alone.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "86-87",
     "quote": "recognition is not enough for productive, representational, justificatory, or integrative constructs;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "38-39",
     "quote": "judge a lesson by *production* (say/write/type) over *selection* (click)",
     "verbatim": true
    }
   ],
   "against": "kb-0154 line 86: \"For diagnostic assessment, the much-maligned MCQ is not a compromise — it is the optimal format.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 'Prefer producing over selecting' in general is too broad: the diagnostic BrainLift argues selection is the best format for diagnosis. The evidence supports matching the response mode to the target, plus a production preference inside lessons."
  },
  {
   "index": 13,
   "verdict": "keep",
   "statement": "Gradual release runs one process with falling support: model the thinking, have the student complete a partial answer of the same process, then release that same process. A hint is not guided practice.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "60",
     "quote": "I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "34-36",
     "quote": "the we-do gives a *partial* answer the child completes (a hint is not a we-do, a fresh question is not a we-do); I-do, we-do and you-do must run the *same skill*, never switch mid-lesson.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. It adds fidelity detail to truth 40's lesson order (same process, partial answer, a hint is not guided practice). Candidate 14 is the check for this same rule and could be merged into it."
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "statement": "Check gradual release with the labels stripped off: the steps must still read as one process at falling support; correctly labelled steps with the wrong substance are the usual failure.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-1/teacher-skill/candidate/brainlifts/core/gradual-release.md",
     "lines": "17",
     "quote": "Acceptance test: strip the I-do/we-do/you-do labels; a reviewer must still see one process at decreasing support (standard §1).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-1/teacher-skill/candidate/brainlifts/core/gradual-release.md",
     "lines": "21",
     "quote": "The labels are where generators fail: round-2 found correctly-labeled sections with wrong substance (answer-reveal I-do, hint we-do, skill-switch you-do). Test substance, never labels.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "136",
     "quote": "gradual-release fidelity: labels alone are insufficient;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "43-44",
     "quote": "gradual-release doses that survive the strip-the-labels test",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The cited quotes are verbatim, but neither KB file says what the strip-the-labels test is, so the original statement's definition was the reader's inference. The definition sits in the gradual-release lattice file (lines 17, 21), now cited, and the statement follows it. Overlaps candidate 13."
  },
  {
   "index": 15,
   "verdict": "keep-with-fix",
   "statement": "In a modelled example, carry every step up to the final substantive thinking move and leave that move to the student.",
   "kind": "course convention",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "83-84",
     "quote": "the teacher models every step up to but not including the final substantive thinking move; the child does that move",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim. It is one course's fixed convention; the next lines carve out an exception where composing the answer is itself the student's work. It fits the completion-problem pattern and is general enough, but it is a ruling, not a measured result, so the kind is corrected."
  },
  {
   "index": 16,
   "verdict": "keep",
   "statement": "Before students start, tell them what they are reading or working to find out, and keep the lesson's question and the current steps visible while they work.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "61",
     "quote": "Children need a reason to read before they start",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "84",
     "quote": "The steps and live question must remain visible, and the model should surface one thing at a time",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "207",
     "quote": "Every lesson has one learning question, and every phase of the lesson builds toward answering it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "210",
     "quote": "It is annotated, and pinned to the top of every screen.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. A grade-3 review and a grade-9 design spec agree, so the rule holds across grades."
  },
  {
   "index": 17,
   "verdict": "keep",
   "statement": "Write questions specific to the source; generic rules of thumb such as 'find the one key sentence' or 'check the title' mislead.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "73",
     "quote": "Titles frequently do not state the main idea, so checking against the title is not a dependable rule.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "75",
     "quote": "but the question must be bespoke to the text.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "81-82",
     "quote": "questions are bespoke to the text, never a generic template like \"find the one sentence the whole story is about,\"",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and the same ruling was carried into the course rulebook (R-Q-4)."
  },
  {
   "index": 18,
   "verdict": "keep-with-fix",
   "statement": "When a task asks for evidence, keep the source visible, have students find and mark the evidence before writing about it, and show a model of a strong response.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "86",
     "quote": "Prompts ask for textual evidence, but the passage is hidden when the student needs to cite it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "87",
     "quote": "No model of a strong response is shown.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "116",
     "quote": "Students should first find and highlight the sentence, then write it in their own words",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The first quote is on line 86 alone, not 86-87. Line 87 carries the missing-model finding the statement relies on, so it is now cited."
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "statement": "Keep corrective feedback short and aimed at the specific error, and never longer than the source or than the instruction it corrects.",
   "kind": "proposed rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "59",
     "quote": "it is too long, sometimes longer than the passage",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "89",
     "quote": "target <=40 words;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "90",
     "quote": "cap around 60 words;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "96-97",
     "quote": "if corrective feedback is longer or more complex than the original instruction, the item has crossed into new instruction.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, but the '40 words' figure wasn't in the cited lines. It is a grade-3 lint proposal (target 40 or fewer, cap about 60; kb-0093 lines 89-90), not an adopted rule. A word count is grade-bound, so it is moved out of the statement and kept here as an example."
  },
  {
   "index": 20,
   "verdict": "keep-with-fix",
   "statement": "Order hints from general criterion cues to specific ones, and name the clue's own words only in the last hint.",
   "kind": "fix pattern from a census (not yet a validator)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "52-54",
     "quote": "a we-do nudge names the clue's own words instead of a criterion cue — fix pattern: reword to criterion cues, naming a clue's actual words only in the *last* nudge",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "50",
     "quote": "not yet a hard validator",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim. It comes from a census fix pattern that the file says is not yet enforced, so it is a convention rather than an adopted rule. It complements truths 1 and 4 without duplicating them."
  },
  {
   "index": 21,
   "verdict": "keep-with-fix",
   "statement": "Keep every sentence a student must act on short (one grade-3 course capped instructions, questions, hints and feedback at 25 words, exempting story prose and taught sentence frames), and enforce the same cap at runtime on any reply generated live.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "96-97",
     "quote": "Instructions, question stems, hints, second hints, reveals, the reply to a wrong answer, and the guide's own think-aloud commentary: 25 words a sentence, maximum.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "95-96",
     "quote": "putting a 14-word sentence at ~90% understood and a 43-word sentence under 10%",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "99",
     "quote": "Two deliberate exemptions, both because a blanket cap would break them: **story prose**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "109-110",
     "quote": "since no static validator can see a line that does not exist until a child answers.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The readability quote is on lines 95-96, not 96-97; the numbers (14 words at about 90%, 43 words under 10%, a 25-word cap) match. The cap was set for one grade band, and the exemptions cover taught sentence frames as well as story prose, so the number becomes an example. The runtime-check point is general. Related to truth 26."
  },
  {
   "index": 22,
   "verdict": "keep",
   "statement": "Teach a concept with an example and a non-example that differ only in the defining feature, and say why the non-example fails; ambiguous examples teach the wrong rule.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "33-34",
     "quote": "example and non-example differ in only the one defining feature, and the non-example states why it fails",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "83",
     "quote": "If the learner can logically infer the wrong rule from the examples provided, the fault lies with the instruction, not the learner.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The rule is validator-enforced (minimal pair, same length band), and the platform's own principles state the same Direct Instruction idea."
  },
  {
   "index": 23,
   "verdict": "keep",
   "statement": "Give each term one wording and use it everywhere it recurs; terms taught together must be distinct, and none may appear inside another's definition.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "38",
     "quote": "One definition per word, used everywhere it recurs — reading goal, passage glossary,",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "30-31",
     "quote": "Taught words in one lesson must be distinct — never overlapping in meaning, never one appearing inside another's own definition",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The one-definition rule is validator-enforced; the distinctness rule is marked 'Not enforced' in the source. The found_by example of one word sitting inside another's definition isn't shown; the reviewers' example was three overlapping words."
  },
  {
   "index": 24,
   "verdict": "keep-with-fix",
   "statement": "Every taught term needs at least one graded task where the student must use it; mentioning or recognising it doesn't count.",
   "kind": "measured (audit finding) and adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "135-136",
     "quote": "merciless/triumphant were acquired but no graded surface required using them",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "138",
     "quote": "a cash point is **graded usage, not mention**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim. The source defines the requirement as graded use rather than mention (line 138), which says more than 'multiple choice doesn't count', so the wording follows it."
  },
  {
   "index": 25,
   "verdict": "keep-with-fix",
   "statement": "Plan repeated later encounters of each taught word across the unit (one course ruled 10 to 12); unplanned natural reading teaches few new words.",
   "kind": "adopted rule plus external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "69",
     "quote": "A word needs **10 to 12 encounters** across the unit/course to be retained",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "69",
     "quote": "Only \\~5–15 of 100 unfamiliar words met in natural reading are learned; misdirective contexts teach approximately zero",
     "verbatim": true
    }
   ],
   "against": "kb-0121 line 67: \"*incidental* vocabulary: η²=.625, no meanings taught, target words recurring \\~6× across the set\". Engineered recurrence of about 6 encounters worked without any teaching, so 10-12 is a ruling, not a measured threshold.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and the numbers (10 to 12; 5–15 of 100) match. The 10-12 figure is a ruling with no cited study; its validator only reports a shortfall against ten. The found_by link between this ruling and the natural-reading finding is the reader's, not the source's. The number is kept as an example."
  },
  {
   "index": 26,
   "verdict": "keep-with-fix",
   "statement": "Treat a student's self-report as a starting guess that item evidence can overturn, never as proof of mastery; for word knowledge, 'I know it' often outruns what the student can explain.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "108",
     "quote": "The key design principle: self-report is a prior, not a verdict.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "72",
     "quote": "\\~80% of students check a word as \"known,\" \\~50% can give an example, \\~20% can explain it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "21",
     "quote": "Do not advance students based on time, completion, or self-report.",
     "verbatim": true
    }
   ],
   "against": "kb-0155 line 207: \"Research on metacognition confirms that students are better at judging their knowledge than the assessment literature implies — at least for coarse judgments.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim and ~80%/~50%/~20% match. The 80/20 finding comes from vocabulary checklists, and the diagnostic sources call coarse topic self-reports fairly accurate. The original 'I know it overstates' clause generalised beyond its evidence, so it is narrowed to word knowledge."
  },
  {
   "index": 27,
   "verdict": "keep",
   "statement": "While students are learning, use sources that build on one topic so knowledge compounds; keep unseen, unrelated sources for the test.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "70",
     "quote": "Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "66",
     "quote": "Coherent-set readers gained 5.59 vs 2.63 concept idea-units (η²=.32) over six texts in three days",
     "verbatim": true
    }
   ],
   "against": "kb-0111 lines 736-737: \"this study took place in one rural school and included only fourth grade students who were reading on grade level.\" The study's comprehension-question scores were not significant (kb-0111 summary).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 5.59 vs 2.63 and partial η² .324 were checked against the full paper (kb-0111 lines 466, 574), as were the DOI and the random assignment. The gains were in topic knowledge, vocabulary and novel-text retelling, not comprehension-question scores. The evidence doesn't rely on the name-bearing file."
  },
  {
   "index": 28,
   "verdict": "keep-with-fix",
   "statement": "Build the background knowledge a source needs instead of only activating what students already bring; what they already know predicts how much new knowledge they gain from it.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0111-cervetti-2016-knowledge-effect-full.qmd",
     "lines": "723-724",
     "quote": "students initial knowledge of the topic of birds was a significant predictor of posttest topic knowledge",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0111-cervetti-2016-knowledge-effect-full.qmd",
     "lines": "725-726",
     "quote": "students who have topic knowledge not only understand related texts better, but also build more knowledge from those texts.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0111-cervetti-2016-knowledge-effect-full.qmd",
     "lines": "729-730",
     "quote": "Relying mainly on activating knowledge students bring to school likely contributes to Matthew Effects in reading.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0110-can-reading-comprehension-be-taught.qmd",
     "lines": "47",
     "quote": "strategy instruction may have an upper limit, but building background knowledge does not; the more students know, the broader the range of texts they can comprehend.",
     "verbatim": true
    }
   ],
   "against": "kb-0111 lines 736-737: one rural school, on-grade fourth graders only (N=59).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true,
   "reason": "Quotes are verbatim. 'Decides' overstated a significant predictor from one N=59 study, so it is now 'predicts'. The no-upper-limit line is an argument in a commentary, not a review finding. The study evidence sits in a file whose path carries an author's name, and no other file gives the predictor result."
  },
  {
   "index": 29,
   "verdict": "keep",
   "statement": "Teach general strategies briefly, explicitly and inside content; extra strategy drill adds nothing, and the time is better spent building knowledge.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0110-can-reading-comprehension-be-taught.qmd",
     "lines": "45",
     "quote": "Ten sessions yield the same benefit as fifty sessions. The implication seems obvious; RCS instruction should be explicit and brief.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0104-comprehension-research-agenda.qmd",
     "lines": "80-81",
     "quote": "fosters deeper comprehension development than strategies taught in isolation",
     "verbatim": true
    }
   ],
   "against": "kb-0104 lines 82-83: \"too-wide content/text range = strategies not fully learned; too-narrow = transfer fails\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 'Ten vs fifty' is a commentary's reading of eight reviews, none of which found a benefit from more practice (line 45)."
  },
  {
   "index": 30,
   "verdict": "keep",
   "statement": "Design the knowledge sequence first, and use standards only to fix scope and check coverage afterwards; standards are not a teaching plan.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "59",
     "quote": "use the standard to constrain scope (what must appear), but apply independent judgement about order, depth, prerequisite structure, and cognitive demand.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "32",
     "quote": "standards alignment is a *check run afterward*",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the curriculum-architecture source is cross-subject, so the rule isn't reading-only."
  },
  {
   "index": 31,
   "verdict": "keep-with-fix",
   "statement": "A bank of practice and test items is not a course; without explicit teaching inside a knowledge sequence it does not work as instruction.",
   "kind": "reviewer verdict and design simulation",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "40",
     "quote": "Reading Explorers v2 is a well-built, MAP-styled practice-and-assessment engine, not a comprehension curriculum, and on its current form it should not be approved as one.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
     "lines": "70",
     "quote": "Strong questions do not become a course unless they sit inside this flow and the actual app proves students can experience it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
     "lines": "56",
     "quote": "| `V0_skill_drill_practice_engine` | 0 | 0 | 12 |",
     "verbatim": true
    }
   ],
   "against": "kb-0099 line 23: \"not student outcome evidence\"; kb-0081 line 40: \"If it is decided that this should be a MAP practice app, the recommendations below would be different.\"",
   "general": true,
   "duplicate_of": "40",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim and the 12 personas are confirmed. But the simulation is a deterministic stress test scored against the team's own doctrine, so calling it 'measured' overstated it. The reviewers' verdict (kb-0081 line 40) is the real support. It restates truth 40 negatively and is kept for that reviewer evidence."
  },
  {
   "index": 32,
   "verdict": "keep",
   "statement": "Teach the combining of parts explicitly; tasks that select, combine or justify parts must be taught and gated, not assumed once each part is passed.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "110",
     "quote": "Students can \"master\" individual KCs yet fail whenever they must select, combine, or justify them in context.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "116",
     "quote": "The mastery gate for an integrative lesson must test the integration — requiring the combined move, not re-testing the parts in isolation.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; it is curriculum-architecture doctrine and applies across subjects."
  },
  {
   "index": 33,
   "verdict": "keep",
   "statement": "Assess the same operation, at the same cognitive level, that the lesson taught, and match every skill tag to the work the item actually requires.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "92",
     "quote": "Example found: a main-idea lesson served an inference/evidence item.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "122",
     "quote": "N1: DOK-level alignment. Coverage is false if an \"analyze\" standard is assessed by \"identify.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "132",
     "quote": "do not teach one cognitive operation and assess another.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The rule itself is now quoted (kb-0086 line 132) as well as the defect found."
  },
  {
   "index": 34,
   "verdict": "keep",
   "statement": "If simplifying an item's wording without changing what it tests would make it easier, or you can't explain why it is hard, the difficulty is irrelevant; remove it.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "152",
     "quote": "if I simplified the wording of this item without changing what it tests, would it become easier? If yes, the current difficulty is at least partly extraneous.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "126",
     "quote": "N5: linguistic validity. Untaught vocabulary or syntax can create construct-irrelevant difficulty.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the test rests on cognitive load theory as summarised in the MCQ BrainLift."
  },
  {
   "index": 35,
   "verdict": "keep",
   "statement": "Tag an item's cognitive level by the process it requires, not by its pass rate; a judge prompted with the same mixed-up definitions will confirm the mistake.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "73",
     "quote": "When tagging items by cognitive level, describe the cognitive process required, not the expected pass rate.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0161-assessment-item-difficulty-core.qmd",
     "lines": "96",
     "quote": "your \"difficulty alignment\" check will confirm the misclassification because it's using the same flawed definitions.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. Related to truth 43 (check against something that doesn't assume the answer) but specific to tagging cognitive level."
  },
  {
   "index": 36,
   "verdict": "keep",
   "statement": "Size a check to the decision it supports: five items can't support a mastery call, and on a short test a percentage bar can quietly demand a perfect score.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "188",
     "quote": "a 5-item MCQ quiz is useful for retrieval practice and rough formative diagnosis but is too unreliable for mastery decisions.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "188",
     "quote": "A 10–15 item assessment begins to support cautious inferences about whether a student has grasped the core content.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "141",
     "quote": "gate-arithmetic trap where small tests make 90 percent require a perfect score;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and 5, 10–15 and 20–30 items match line 188. Related to truth 15 but about test length and decision stakes."
  },
  {
   "index": 37,
   "verdict": "keep",
   "statement": "A percent-correct mastery bar means something only under fixed task conditions; set it per skill by weighing the cost of a false pass against a false fail.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd",
     "lines": "60",
     "quote": "Percent-correct only means something when task difficulty and evidence conditions are held steady; otherwise it is entangled with item easiness, scaffolding, and cueing.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd",
     "lines": "57",
     "quote": "Every mastery rule is a trade: false promotion risks downstream failure; false non-promotion wastes time and motivation.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "88",
     "quote": "define mastery through controlled evidence and downstream risk, not a global raw `90%`;",
     "verbatim": true
    }
   ],
   "against": "kb-0028 line 21: \"**Enforce mastery gates at ≥90% accuracy.**\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; both cited research sources appear in the evidence base (kb-0156 line 142, kb-0157 lines 417-418). The tension with the platform's fixed 90% rule is real and kept in the against field."
  },
  {
   "index": 38,
   "verdict": "keep-with-fix",
   "statement": "A mastery system needs a third outcome, switching to reteaching, for when practice stops producing gains; without it, persistence becomes the real pass criterion.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd",
     "lines": "65",
     "quote": "A mastery system that lacks an explicit “switch mode” state will inevitably turn persistence into the hidden criterion for passing.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0157-mastery-signal-evidence-base.qmd",
     "lines": "430",
     "quote": "when a learner is failing, we currently just let them keep attempting items.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The text is at line 65, but the source uses curly quotes around switch mode; the quote is corrected so it is verbatim. Supported as stated."
  },
  {
   "index": 39,
   "verdict": "keep",
   "statement": "After reteaching, confirm recovery with different evidence, such as new items or near-miss variants, not the items used to reteach.",
   "kind": "external research and adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd",
     "lines": "230",
     "quote": "After corrective instruction, the system should re-check using near-miss and transfer variants to confirm the misconception was actually repaired, not merely coached.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "67-68",
     "quote": "Rebuild every assessment and writing criterion as failed function -> relevant taught check -> different-evidence retry.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The AP audit's repair was later implemented: kb-0170 lines 86-89 close all six buckets, including criterion-level correction mappings. It applies truth 48 to the reteaching loop."
  },
  {
   "index": 40,
   "verdict": "keep-with-fix",
   "statement": "An independent (transfer) task must not reuse the answer-bearing evidence or claims the worked example already used.",
   "kind": "measured (audit finding) and adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "64",
     "quote": "Replace independent tasks that reuse answer-bearing modeled evidence in Lessons 1, 3, and 6.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd",
     "lines": "81-82",
     "quote": "\"Independent item claim_ids must be a subset of independent_claim_ids and disjoint from teaching_claim_ids\")",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "87",
     "quote": "independent different-evidence release",
     "verbatim": true
    }
   ],
   "against": "kb-0121 line 47: an in-lesson knowledge check answerable from taught knowledge is legitimate (candidate 41).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. Reused modelled evidence was one of six repair items behind the AP audit's block, not its sole cause. 'Keep scored claims separate from taught claims' was too broad, since in-lesson knowledge checks may legitimately test taught claims (candidate 41), so the rule is limited to independent work."
  },
  {
   "index": 41,
   "verdict": "keep",
   "statement": "Decide whether an item checks taught knowledge or tests transfer before judging its overlap with the teaching; the same overlap is correct in one and a leak in the other.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "47",
     "quote": "An in-lesson knowledge check answerable from explicitly-taught knowledge is legitimate (that's what checking taught knowledge means); the same overlap in a comprehension/transfer item is a leak.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "26-27",
     "quote": "in reading, finding the answer in the passage IS the skill, so the usual history-style \"answer is in the source\" leak check is deliberately skipped.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 'five adversarial rounds' is stated on line 47. The second quote shows the leak definition also depends on the subject (reading vs history)."
  },
  {
   "index": 42,
   "verdict": "keep-with-fix",
   "statement": "After a miss, correct and reteach before retesting, and don't raise the difficulty of the retry.",
   "kind": "adopted rule with one confounded measurement",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "143",
     "quote": "Error correction should be immediate and brief: correct, test, give intervening items, then retest later.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "37",
     "quote": "| 4 | Retry makes students worse | Difficulty escalates after a miss; attempt-2 supporting-detail accuracy **64% -> 41%** |",
     "verbatim": true
    }
   ],
   "against": "The 64% -> 41% drop comes with harder retry items, so it shows escalating difficulty produces more failure, not that students got worse.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true,
   "reason": "The quote is verbatim and 64% -> 41% matches, but the accuracy drop is confounded with the harder retry items, so it is not evidence that retrying harms students. The reteach-first half rests on the error-correction rule in kb-0086 line 143. The 'don't escalate' half has only the name-bearing source. Overlaps candidates 38 and 39."
  },
  {
   "index": 43,
   "verdict": "keep-with-fix",
   "statement": "Re-run blind-solve checks when a stronger solver becomes available; items that resisted an older or weaker solver can leak to a stronger one.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "33",
     "quote": "Current Gemini 3.5 replay: 3/3 in both conditions - direct blind leak; old lift is historical.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "53",
     "quote": "invalidation by a stronger current plain-blind solver; stale solver results are not certification.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "67-69",
     "quote": "showed the weak gpt-4o-mini gate had over-credited items — of v1's 95 re-gated \"clean\" items, only **20 (21%) survived**; **75 leaked** under the strong solver.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "37",
     "quote": "cert stamp + recert (re-run on drift/flip/generator-version bump).",
     "verbatim": true
    }
   ],
   "against": "kb-0080 line 182: \"LLM ablation may false-positive/negative vs real students\". kb-0096 made the opposite move, re-baselining to a weaker solver (see candidate 45).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim and 0/3 and 3/3 match lines 32-33. A second, larger case is added from kb-0235: of 95 items a weak solver cleared, 75 leaked to a strong one. The statement now says 'stronger', as the sources do, rather than 'strongest'. Related to truth 5."
  },
  {
   "index": 44,
   "verdict": "keep",
   "statement": "A blind solver's low self-reported confidence does not cancel exact recoveries of the key; count repeated exact hits as leaks.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "43-45",
     "quote": "Promotion review found `r3-09` at 3/8 exact plain-blind recovery and 0.71875 mean partial accuracy; the sealed rule had ignored those hits because the solver reported low confidence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "59-60",
     "quote": "model self-confidence cannot erase exact blind recoveries.",
     "verbatim": true
    }
   ],
   "against": "kb-0100 lines 38-39: \"the loosened bar correctly discards low-confidence forced guesses\" (an earlier, name-bearing file, cited only as the counter).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim, and 3/8 and 0.71875 match. The earlier loosened-bar reading (kb-0100, lines 38-39 rather than 39-40) is the counter, but the later promotion review reversed a pass on exactly this point, so the newer evidence stands. Compatible with truth 9, which covers the judge's own uncertainty."
  },
  {
   "index": 45,
   "verdict": "drop",
   "statement": "Calibrate the blind solver itself; one that bluffs with test-taking tricks inflates leak rates, so let it answer 'unknown' when the source is genuinely needed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "31",
     "quote": "it returned blind accuracy of `1.0` on items that genuinely needed the passage.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "70",
     "quote": "A solver that can bluff its way through without the passage will inflate leak rates.",
     "verbatim": true
    }
   ],
   "against": "kb-0120 lines 59-60: \"model self-confidence cannot erase exact blind recoveries.\" kb-0235 lines 67-69: a stronger solver exposed 75 of 95 weak-solver passes as leaks.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The quotes are verbatim, but the claim overstates its evidence. kb-0096 is one calibration note with no student data or independent ruling on which solver was right, and its fix made 10 flagged items pass. The 'tricks' it discounts (picking the longest option, crossing out absolutes, distractor tells) are the surface cues the course bans (candidate 7) and that test-wise students use. Later evidence goes the other way: a stronger solver exposed most weak-solver passes as leaks (kb-0235), and an exact blind hit can't be waved away (kb-0120). It also contradicts candidate 43. A narrower point may hold: a model knows more of the world than a child, so its world-knowledge hits can overstate leaks. That is not what the statement says."
  },
  {
   "index": 46,
   "verdict": "keep",
   "statement": "Measure a generator on one attempt per preregistered item against a fixed denominator, with no retries, reranking, repair, cache or hidden selection, and report served or best-of-N results separately.",
   "kind": "measured (exploit found) and adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "58-60",
     "quote": "Raw generator quality is `raw_k1`: one candidate, one attempt, no retry, reranking, repair, cache substitution, rejection sampling, best-of-N, or hidden human selection.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "60-62",
     "quote": "Raw acceptance is fixed at 100 preregistered records per family, with no early success or denominator top-up. Served-bank and cache/runtime evidence stays in a separate lane.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "9",
     "quote": "BUT the headline '99%' is a build-time best-of-N + serve-from-cache EXPLOIT (SCOREBOARD_99 itself: 'NOT the model generating'), which violates the K=1/no-BoN constraint",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The AP contract is frozen but unexecuted ('No InceptBench run has been executed', kb-0170 line 64); the exploit is documented in kb-0063 lines 47-50. Distinct from truth 65: this is about reporting raw single-attempt quality apart from served results."
  },
  {
   "index": 47,
   "verdict": "keep",
   "statement": "Count unique, eligible items and check the spread of what survives; gross row counts and template-stamped passes hide a thin, duplicated bank.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "73",
     "quote": "143,026 gross APUSH rows;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "74",
     "quote": "- 49,571 sampling-eligible exact unique candidate bodies;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "78",
     "quote": "The 100,000 unique/usable-sample claim is therefore rejected.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
     "lines": "74-75",
     "quote": "0/8,937 sequence/match survive strict QA",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
     "lines": "75",
     "quote": "ONE template stamped 1,475×",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and 143,026, 49,571, 100,000, 8,937 and 1,475 all match. The found_by numbers are now quoted directly from the AP corpus audit and the self-audit."
  },
  {
   "index": 48,
   "verdict": "keep-with-fix",
   "statement": "At the gate, treat a check that never ran, and any output that is empty, invalid, timed out or unscorable, as a failure, never as a pass.",
   "kind": "measured and adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
     "lines": "48-49",
     "quote": "The cold-transfer keystone is a LABEL, not a measurement.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0070-passage-blind-solve-g5-seedbank-2026-06-24.qmd",
     "lines": "56",
     "quote": "`NEEDS_LLM_GRADE` (solve not run) is a FAIL, not UNVERIFIED.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "315",
     "quote": "Invalid, empty, timed-out, or unscorable artifacts are failures.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "185-186",
     "quote": "never read a 0/0 verdict as green — treat it as a harness bug until proven otherwise.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the kb-0131 sentence is on line 315, not 316. The 'never ran = fail' half had no direct quote until kb-0070 line 56. This is a certification gate, where 'not a pass' means blocked, so it doesn't clash with truth 9 (student marking). Related to truth 38."
  },
  {
   "index": 49,
   "verdict": "keep",
   "statement": "Check what an output must contain as well as what it must avoid; an empty or minimal output that breaks no rule still fails.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "405-406",
     "quote": "Positive obligations and prohibitions are both required; an empty/minimal artifact fails completeness even if it avoids violations.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim; it is an experiment-design rule, as the kind says."
  },
  {
   "index": 50,
   "verdict": "keep-with-fix",
   "statement": "When scoring a model's rule decisions, report recall on the rare decision against an always-majority baseline so class imbalance can't pass for compliance; set the bar from the agreement independent people reach, and use a model verifier only to audit.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "316-318",
     "quote": "compute a per-rule modal-decision prior and an always-modal strict artifact-pass baseline; report per-rule macro-F1 and minority-decision recall so class imbalance cannot masquerade as contract obedience.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "398-399",
     "quote": "Semantic-label ceiling is measured agreement from independent human/expert reviewers before adjudication.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "403-404",
     "quote": "A different-family LLM verifier is audit-only and cannot establish the ceiling or headline result.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the original quote sits on lines 317-318, not 318-319. The source applies the imbalance rule to scoring a model's obedience to a rule contract, not to scoring a judge, so the wording is corrected. 'Score on person-labelled cases' already is truth 37, and 'a model verifier only audits' overlaps truth 44. The new content is the majority baseline and the human-agreement ceiling."
  },
  {
   "index": 51,
   "verdict": "keep-with-fix",
   "statement": "Keep missing, ambiguous and conflicting answers marked as such until a person rules on them; never infer them, and label anything built on unattributed rules as provisional.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "151-152",
     "quote": "No answer may be inferred merely because a question is phrased yes/no. Missing stays `missing`; ambiguous stays `ambiguous`; conflicting sources stay in conflict until adjudicated.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0242-decision-matrix-judgment-corpus.qmd",
     "lines": "67-68",
     "quote": "876 records `binding=true` (both a date AND an authority are extractable from the source text, and the text is not explicitly marked pending); **1715 `binding=false`**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0242-decision-matrix-judgment-corpus.qmd",
     "lines": "70",
     "quote": "but any eval probe built on them must be labeled provisional.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the kb-0242 phrase is on line 70 only, not 69-70. 1715 is confirmed. A person owning adjudication is named at kb-0131 line 149."
  },
  {
   "index": 52,
   "verdict": "keep",
   "statement": "Passing a format or schema check proves the shape of an output, not that it embodies the intended teaching.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "117",
     "quote": "Shape validity does not establish semantic compliance.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "285-286",
     "quote": "JSON Schema/AJV can reject malformed structures; it cannot prove that a lesson embodies the pedagogy.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "117-118",
     "quote": "schema validity is a document-integrity floor only, never a course-quality/child-readiness/outcome verdict.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and kb-0131 lines 285-286 state the 'embodies the teaching' point directly. Distinct from truth 67."
  },
  {
   "index": 53,
   "verdict": "keep",
   "statement": "No writer, whether model, agent or lane, may certify its own output; its self-reported compliance is not evidence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "255",
     "quote": "A model may assist extraction but may not certify its own atom.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "26",
     "quote": "unaudited LLM self-assessment of its own content (empirically worthless — see DOK1-11)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "157-158",
     "quote": "no lane can self-certify the whole course.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The 'empirically worthless' line cites a leak-rate fact (DOK1-11) rather than a study of self-assessment, but the other two are explicit rules. Related to truths 61 and 66, not a duplicate."
  },
  {
   "index": 54,
   "verdict": "keep",
   "statement": "A model's score on pedagogy-knowledge questions is not evidence that the content it generates teaches well; measure the generated content itself.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0124-eduqwen-pedagogical-llm-paper.qmd",
     "lines": "94-95",
     "quote": "strong benchmark performance on pedagogical knowledge questions does not itself constitute evidence of effective classroom tutoring",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "46",
     "quote": "Knowing-that (answering pedagogy questions) and generating-aligned (producing content that embodies the pedagogy) are different capabilities",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the paper's own limitation sentence also appears in its summary (line 12)."
  },
  {
   "index": 55,
   "verdict": "keep-with-fix",
   "statement": "Give a writer model only the few rules that apply to the piece at hand, not the whole rulebook; across 18 models, rule-following fell as instructions got harder.",
   "kind": "external research plus architectural inference",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
     "lines": "73-74",
     "quote": "across 18 models, constraint adherence fell materially as instruction difficulty increased",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
     "lines": "74-76",
     "quote": "**Our architectural inference:** compile a small active contract rather than prompt with the full rule base",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
     "lines": "285",
     "quote": "The raw bank never enters the renderer prompt.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim and 18 models is confirmed. The study measured instruction difficulty, not the size of the rulebook; 'only the few rules' is the team's own labelled inference (lines 74-76), so the kind is corrected. Effects of rule load are planned (kb-0131 line 315) but not reported."
  },
  {
   "index": 56,
   "verdict": "keep-with-fix",
   "statement": "Different models follow the same explicit rule contract very differently; qualify each model and version separately, and test that rules aren't applied outside their scope.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd",
     "lines": "12",
     "quote": "OpenAI 60/140 exact and 0/20 robust clusters, Claude 67/140 and 0/20, DeepSeek 136/140 and 17/20",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd",
     "lines": "86",
     "quote": "Failure localization across the 157 tested misses:",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd",
     "lines": "89",
     "quote": "- negative-control gate: 43;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0166-counterfactual-authority-a1b-terminal-causal-control.qmd",
     "lines": "110",
     "quote": "It was steerable but not safely scoped.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
     "lines": "46",
     "quote": "every model/version requires conformance qualification.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The table-row quote is on line 79 alone, not 79-81, and shows only one model. The full range (60/140 to 136/140) is now quoted from the summary on line 12. 157 misses and 43 negative-control failures are confirmed. All three were small, fast model versions."
  },
  {
   "index": 57,
   "verdict": "keep",
   "statement": "Don't let a model pick the sequence or merge sources on its own taste: give it the progression policy, and process sources in authority order instead of blending them in one pass.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "74",
     "quote": "the sequence will reflect whatever assumptions the model happens to import",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "67",
     "quote": "is not synthesis at all; it is compromise",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "68",
     "quote": "Proper synthesis is staged. Different sources contribute different things and must be processed in order:",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and line 68 shows the authority order (scope, evidence, representation). Overlaps truths 29 and 57 in spirit."
  },
  {
   "index": 58,
   "verdict": "keep-with-fix",
   "statement": "When combining similar standards from several jurisdictions, don't merge them into one abstract description; that loses the specifics teaching needs.",
   "kind": "measured (one attempt)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd",
     "lines": "51",
     "quote": "The result was flattened abstractions that lost the specificity needed for teaching.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd",
     "lines": "52",
     "quote": "it proves that naive merging (abstracting away specifics to find a common description) is the wrong approach.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim. The source shows naive merging failed, but offers keeping each source's specifics inside a shared node only as an untested possibility ('might perhaps'), so the statement no longer asserts it."
  },
  {
   "index": 59,
   "verdict": "keep-with-fix",
   "statement": "Count a prerequisite as met only when it is fluent enough not to load working memory, and beware teaching a restricted case apart from the general case, which can create a misconception.",
   "kind": "doctrine (curriculum-architecture position)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "63",
     "quote": "A prerequisite that is technically met but not automated enough to free working memory makes the target skill unteachable.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "62",
     "quote": "Splitting a restricted case from a general case (e.g., same-denominator before unlike-denominator fractions) causes students to build predictive models that become entrenched and must be actively undone.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. Both halves are a BrainLift's stated positions with examples, not results measured here, so the kind is corrected. The hedged wording ('beware', 'can') doesn't overstate them."
  },
  {
   "index": 60,
   "verdict": "keep-with-fix",
   "statement": "Record which pairs students commonly confuse; choose first-teaching examples so the confusion doesn't form, and interleave the pair only once both are learned.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd",
     "lines": "80",
     "quote": "where interleaving after both are learned builds discrimination",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0119-curriculum-architecture-brainlift-evidence.qmd",
     "lines": "240",
     "quote": "Novices may need initial blocked exposure before productive interleaving.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0119-curriculum-architecture-brainlift-evidence.qmd",
     "lines": "242",
     "quote": "but only after students have enough initial understanding to make the contrast meaningful.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "160",
     "quote": "Interleaving is only appropriate after the skill is ready; massed/blocked first, interleaved later.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 'Keep them apart during first teaching' went beyond the sources, which say example selection can prevent the confusion forming and novices 'may need' blocked exposure first."
  },
  {
   "index": 61,
   "verdict": "keep",
   "statement": "Keep earlier knowledge alive by making later lessons use it, revisit an idea only with a real upgrade and say what is new, and leave isolated spaced review for what's left over.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "82",
     "quote": "use the curriculum to keep generative knowledge warm by use; use spaced practice for the residue.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "131",
     "quote": "The strong version is a learning progression: each revisit adds a real upgrade",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0118-curriculum-architecture-brainlift-core.qmd",
     "lines": "132",
     "quote": "Earlier knowledge stays warm because later lessons use it to do new work.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd",
     "lines": "41",
     "quote": "[Spiral review of G2 Unit 2, A3-A4 — what is new:",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim (the line-82 sentence recurs at lines 269-270). Supported as stated."
  },
  {
   "index": 62,
   "verdict": "keep",
   "statement": "Shrink guidance and grow independent work as expertise grows; heavy guidance helps novices but slows learners who already know the material.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "284",
     "quote": "The expertise reversal effect (Kalyuga et al.): heavy guidance helps novices but slows down learners who already know the material.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
     "lines": "281",
     "quote": "As students gain expertise, new knowledge and guided practice shrink and independent practice grows.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. It overlaps candidate 102 (adjust help as proficiency grows), and the two could be merged."
  },
  {
   "index": 63,
   "verdict": "keep",
   "statement": "Pair plausible wrong options with corrective feedback; without it, students later reproduce the wrong options as facts.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "176",
     "quote": "Without feedback, the negative suggestion effect persists.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "175",
     "quote": "Students produce MC lures as answers on later tests, even when warned not to guess.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "95-96",
     "quote": "potent misconception-based distractors require product-appropriate corrective feedback or post-test correction because plausible lures can seed false knowledge;",
     "verbatim": true
    }
   ],
   "against": "kb-0159 line 176: \"The minimum effective feedback is showing the correct answer.\" This conflicts with the course rule that a single-select item is never revealed (kb-0183 lines 135-137) and with truth 1's 'never the answer'.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The cited research's corrective feedback is showing the correct answer, which the course's never-reveal rule for single-select items withholds, so the lure risk may persist there. That tension is kept visible."
  },
  {
   "index": 64,
   "verdict": "keep",
   "statement": "Use only as many options as you can make plausible (research favours three), and never add a filler option to reach a count.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "69",
     "quote": "The research consensus (Rodriguez, 2005; Elraiyah et al., 2025) clearly favours three options",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "69",
     "quote": "if you cannot write a third plausible distractor for a given item, use three options rather than adding filler.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "104-105",
     "quote": "An agent must not resolve this by adding filler",
     "verbatim": true
    }
   ],
   "against": "kb-0183 lines 80-81: \"four-option MCQs only, decided 2026-08-04: \\\"standardized to include exactly four options to prevent guessing\\\"\"; kb-0136 line 112: \"MCQs need at least four options.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. A later course ruling fixed exactly four options, which conflicts with 'never add filler' whenever a fourth plausible option can't be written. That conflict is kept visible."
  },
  {
   "index": 65,
   "verdict": "keep",
   "statement": "Cover the options: a student who knows the material should be able to answer from the stem alone.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "65",
     "quote": "read the stem, cover the options, and ask whether a knowledgeable student could formulate an answer.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim; standard item-writing guidance."
  },
  {
   "index": 66,
   "verdict": "keep",
   "statement": "An item is higher-order only if it presents material the student hasn't met; a longer stem doesn't turn recall into analysis.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "58",
     "quote": "no new material, no higher-order thinking.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim, and line 58 also states the stem-length point."
  },
  {
   "index": 67,
   "verdict": "keep-with-fix",
   "statement": "After real use, review each item's statistics: investigate items that weaker students answer correctly more often than stronger ones, and distractors chosen more by stronger students (often a wrong or ambiguous key); revise or remove distractors almost no one picks.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "85",
     "quote": "Negatively discriminating items — where weaker students outperform stronger students — are almost always flawed and should be investigated immediately.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "85",
     "quote": "A distractor selected more by high-performing students than low-performing students suggests the keyed answer is wrong or ambiguous.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "85",
     "quote": "Non-functioning distractors (selected by <5%) should be revised or the item reduced to fewer options.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd",
     "lines": "204",
     "quote": "item retirement (INFIT > 1.30 or pt-biserial < 0.20)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and the <5%, 1.30 and 0.20 thresholds match. The source says revise the distractor or reduce the options, not simply drop it; the negative-discrimination rule is now quoted."
  },
  {
   "index": 68,
   "verdict": "keep-with-fix",
   "statement": "Check an assembled test for items that cue, duplicate or contradict each other, and keep items that prime later answers away from checks used for mastery claims.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
     "lines": "81",
     "quote": "Cueing enemies: one item's stem or options give away the answer to another.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "280",
     "quote": "A preceding item defines “opportunity cost,” making the next item easier; fine for an in-lesson quiz, risky for “stable mastery” claims.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "282",
     "quote": "For generalisable mastery claims, avoid strong primes or move them out of proximity",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "kb-0158 line 280 uses curly quotes; the quote is corrected so it is verbatim. The source calls priming fine in an in-lesson quiz, so the statement now limits it to mastery claims."
  },
  {
   "index": 69,
   "verdict": "keep-with-fix",
   "statement": "Mark short explanations with a small rubric of 0/1/2 checks rather than an ever-growing list of accepted answers; switch when the list passes about 15–20 variants or the key keeps being patched.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "160",
     "quote": "Default: use a micro-rubric (0/1/2) for short text and explanations.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "163",
     "quote": "Your “acceptable answers” list exceeds ~15–20 variants.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "164",
     "quote": "You’ve edited the key twice post-launch to add more exceptions.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "56",
   "name_bearing_source": false,
   "reason": "kb-0158 line 163 uses curly quotes; the quote is corrected. It overlaps truths 56 and 10 and is kept for the switch-over thresholds (about 15–20 variants; the key edited twice after launch)."
  },
  {
   "index": 70,
   "verdict": "keep",
   "statement": "Run a conversational check as a fixed script with set prompts, capped follow-ups and declared supports; free chat leads the witness.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "564",
     "quote": "State machine, not free chat",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "555",
     "quote": "Ungoverned LLM prompts can lead the witness (construct creep and validity loss).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "562",
     "quote": "Set min/max turns and branching conditions (e.g., 1 prompt + up to 2 follow-ups).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the capped-follow-ups detail is now quoted. Related to truth 29."
  },
  {
   "index": 71,
   "verdict": "keep-with-fix",
   "statement": "Give spoken-response tasks a text fallback of equal status unless speaking is itself what is taught or tested, and keep speech-recognition errors from counting against content.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "567",
     "quote": "Always provide a text-response fallback of equal status",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "554",
     "quote": "Speech recognition errors, accent bias, and background noise can contaminate evidence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "539",
     "quote": "Evidence of racial disparities in major ASR systems",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "64",
     "quote": "don't penalize accent or a noisy room",
     "verbatim": true
    }
   ],
   "against": "kb-0181 line 58: \"The say-back specifically must be **spoken**; typing is not an accepted substitute\"; lines 61-62: \"a child with no working microphone has no fallback here.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. Where the spoken say-back is the target (a vocabulary ruling holds that speaking matters for spelling), a typed answer can't substitute, and the KB records that clash as unresolved. The statement is limited accordingly."
  },
  {
   "index": 72,
   "verdict": "keep",
   "statement": "Label how much support each task gives, and base decisions on unaided work; success with scaffolds is weaker evidence, and any claim must say what support was given.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "72",
     "quote": "base high-stakes decisions on the first unaided check (or transfer task) that follows.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
     "lines": "71",
     "quote": "State the claim to match support.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0153-assessment-pack-brainlift.qmd",
     "lines": "61",
     "quote": "The amount of scaffolding and guidance in a task directly affects its difficulty and therefore has implications for how we interpret student attainment.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The 'claim must say what support was given' part is now quoted directly (line 71). The kb-0153 line sits under its AP-style constructed-response section."
  },
  {
   "index": 73,
   "verdict": "keep",
   "statement": "Say what each assessment is for (formative, mastery, diagnostic, placement, summative or cold transfer) before reading its result; one instrument can't do all of these jobs.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "89-90",
     "quote": "declare whether a resource is formative, mastery, diagnostic, summative, or cold measurement before interpreting its result;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "102",
     "quote": "Trying to do both at once with a single instrument wastes items and confuses the design.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "61",
     "quote": "acquisition mastery is not durable mastery — they need different instruments",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. kb-0154 shows the one-instrument problem for placement versus gap-finding; kb-0121 adds acquisition versus durable mastery, which widens the 'can't do all these jobs' claim's footing."
  },
  {
   "index": 74,
   "verdict": "keep",
   "statement": "In any record of what a student knows, keep 'not tested' separate from 'not known'.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "75",
     "quote": "An unassessed KC is not the same as a failed KC, and conflating the two is one of the most common errors in diagnostic systems.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim. Related to truth 9, but about missing evidence rather than an unsure judge."
  },
  {
   "index": 75,
   "verdict": "keep",
   "statement": "To diagnose, test one piece of knowledge per item in the plainest format; exam-style items bundle content with format skill and elimination, so a miss can't show what is missing.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "68",
     "quote": "The question is evaluative (it tells you whether the student can do this task) but not diagnostic (it doesn't tell you what's missing).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0155-diagnostic-assessment-evidence-base.qmd",
     "lines": "255",
     "quote": "The completed practice test is insufficient to establish this proficiency at topic level.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The AP context is explicit: line 68 uses an AP-style exam question as the example, and line 255 is a project concern about AP practice tests rather than a measurement."
  },
  {
   "index": 76,
   "verdict": "keep",
   "statement": "With few students per item, run on expert-set defaults and simple rules; 'optimal' adaptive algorithms on uncalibrated items do no better, and revising an item resets its data.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "117",
     "quote": "will outperform a statistically \"optimal\" approach running on uncalibrated data.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "115",
     "quote": "If items are revised (as they should be, based on early evidence), the clock resets.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "114",
     "quote": "requires at minimum 100-200 student responses to that item.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. 'About 10 students per course' and '100-200 responses' match lines 114-115, now quoted. The source says 'no better than heuristic selection, and may be worse'."
  },
  {
   "index": 77,
   "verdict": "keep",
   "statement": "Judge a diagnostic by whether students who follow its routing learn faster, and stop testing when the next item is worth less than the study time it costs.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "77",
     "quote": "do students who follow its recommendations learn more efficiently than students who don't?",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
     "lines": "40",
     "quote": "test until the expected value of the next item (in terms of improved routing) is lower than the expected value of the student spending that time studying",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; supported as stated."
  },
  {
   "index": 78,
   "verdict": "keep-with-fix",
   "statement": "Treat any predicted item difficulty as a starting estimate that carries its method, sample size and uncertainty; don't set cut scores on it until real responses (on the order of 200 per item) replace it.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0161-assessment-item-difficulty-core.qmd",
     "lines": "89",
     "quote": "Difficulty should always travel with uncertainty and provenance",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0161-assessment-item-difficulty-core.qmd",
     "lines": "91",
     "quote": "How much data it is based on (N, SE).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0161-assessment-item-difficulty-core.qmd",
     "lines": "190",
     "quote": "“<200 responses ⇒ item difficulty is provisional; do not use to set cuts”",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "97-98",
     "quote": "predicted difficulty is a prior with method, population, provenance, and uncertainty; live data must eventually replace it;",
     "verbatim": true
    }
   ],
   "against": "kb-0086 line 43: \"786 items vs 650, RMSE 3.20 vs the prior disclosed simulation miss around 4.12\". A later rerun on a bigger bank met both targets before any calibration, so pinning both misses on expert-set difficulties is not settled.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The original quotes are verbatim (kb-0161 line 190 has curly quotes, now corrected), and 0.928/≥0.93 and 4.12/<4.0 match kb-0080. But the 'measured' attribution is weak: a simulation assumes the item parameters, and a later rerun met both targets before calibration. The rule now rests on the BrainLift guidance, so the kind is corrected and the kb-0080 attribution moved to against."
  },
  {
   "index": 79,
   "verdict": "keep-with-fix",
   "statement": "Don't rely on a model's direct rating of how hard an item is for students; models underestimate difficulty, and more capable ones often do so more. Use direct ratings only as a sanity check, and have the model extract features or compare against calibrated anchors.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "43",
     "quote": "scaling up model capability does not improve difficulty alignment with human learners — it often makes it worse.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "41",
     "quote": "Direct LLM ratings show moderate correlations with empirical difficulty at best (often r ≈ 0.4–0.6)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "41",
     "quote": "They are outperformed by feature extraction plus simple ML, by comparative judgment with anchors, and often by structured rubric-based scoring.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "41",
     "quote": "Treat direct rating as a fast sanity check or tiebreaker, not as the backbone of your difficulty engine.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, and r ≈ 0.4–0.6 matches. The source keeps direct rating as a sanity check, so 'don't ask' became 'don't rely on', and 'often' was added to match the source."
  },
  {
   "index": 80,
   "verdict": "keep",
   "statement": "Report each readiness gate on its own; averaging them into one score hides the gates sitting at zero.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0171-apush-full-course-local-authoring-review-hub-archive.qmd",
     "lines": "50",
     "quote": "Do not average the independent readiness gates into a fake single quality score.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0171-apush-full-course-local-authoring-review-hub-archive.qmd",
     "lines": "52",
     "quote": "The zero-percent rows are later acceptance gates, not missing lessons.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim, and the AP percentage ledger (lines 38-48) confirms 100% authored against 0% reviewed, certified and runtime-verified. Related to truths 49 and 60, but about readiness gates rather than skill accuracy."
  },
  {
   "index": 81,
   "verdict": "keep-with-fix",
   "statement": "Summaries can drift from the records they summarise, usually toward a rosier story; regenerate them from the certified files and never cite a pass that no on-disk record backs.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
     "lines": "27-28",
     "quote": "BRIEFING (the synthesized view) has drifted **ahead of** the certified COMPLIANCE files into a rosier, less-traceable story.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
     "lines": "62-63",
     "quote": "regenerate views FROM the certified files; never cite a PASS no on-disk COMPLIANCE.md + fresh pull backs.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0122-g3-reading-course-graph.qmd",
     "lines": "82-83",
     "quote": "earlier metadata said \"5 edge types\" while both the builder and the enumerated schema define exactly four.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; 3 FAIL and five versus four edge types match. One case of rosier drift plus one plain metadata error doesn't show that summaries always drift rosier, so the claim is softened. Related to truth 24."
  },
  {
   "index": 82,
   "verdict": "keep-with-fix",
   "statement": "Recompute every check and headline number from the content and the raw records; don't trust annotations that travel with the content or a harness's own summary.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "50-51",
     "quote": "added 2026-07-13 after a fresh unit reproduced a dose-item leak — trust the recompute, not the annotation",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "54-55",
     "quote": "adversarially recomputed from the raw per-call JSONL (not trusted from the run harness's own summary).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "61",
   "name_bearing_source": false,
   "reason": "The original short quote is on line 51; it is extended to lines 50-51 for context. The wording is changed so the statement names no role. Not trusting the content's own notes is close to truth 61; the harness-summary case adds evidence."
  },
  {
   "index": 83,
   "verdict": "keep-with-fix",
   "statement": "An exemption from a check must be explicitly granted and cost a measured replacement outcome, and a list of known exceptions may only shrink.",
   "kind": "proposed rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
     "lines": "54-55",
     "quote": "**Make it reviewer-granted, requiring a measured engagement OUTCOME to REPLACE each nullified row** — so it costs an outcome, not waives one.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "67-68",
     "quote": "known-debt list (can only shrink, never padded to pass a build).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. Both are recommendations, a self-audit fix and a draft standard that 'binds nobody' (kb-0217 line 58), not adopted rules, so the kind is corrected."
  },
  {
   "index": 84,
   "verdict": "keep-with-fix",
   "statement": "Turn every class of review comment into a dated rule and, where it can be checked, an automated check, so the same comment never has to be made twice.",
   "kind": "draft standard",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "59-60",
     "quote": "**no reviewer ever makes the same class of comment twice** (comment -> dated register entry -> rule/validator -> structurally extinct)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "58",
     "quote": "Status: DRAFT, not shared, binds nobody",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "65-66",
     "quote": "from 7/9 taught words appearing only once",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim and 7/9 is confirmed. The standard is a draft that binds nobody, and not every class of comment can be automated (the source says 'rule/validator'), so the statement and kind are corrected."
  },
  {
   "index": 85,
   "verdict": "keep-with-fix",
   "statement": "Expect some audit findings to be false (9% in one audit, 8-15% in another); confirm each finding before acting on it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "101",
     "quote": "**6/65 = 9%**, independently matching the arc-audit lane's measured 8-15%.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "76",
     "quote": "two-layer audits (8-15% FP rate)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim, and 6/65 = 9% and 8-15% match. A rate measured on two internal audits is not a general constant, so it is given as examples rather than as 'one in ten'."
  },
  {
   "index": 86,
   "verdict": "keep-with-fix",
   "statement": "Build the student-facing view from an allowlist that leaves out answer-bearing fields students should not see, and test that view for answer leakage.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "71-72",
     "quote": "Define a student-only source projection containing `student_material` plus approved citation metadata, excluding teacher-only answer-bearing fields.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "88-89",
     "quote": "the explicit student-source allowlist",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "126",
     "quote": "mutation tests for student-answer leakage",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the kb-0170 phrase is on line 126 only, not 125-126. In the AP course the allowlist was built (kb-0170 lines 86-89), but the leakage mutation tests were still planned at the pause. The statement is reworded to drop a job role. Distinct from truth 30."
  },
  {
   "index": 87,
   "verdict": "keep-with-fix",
   "statement": "In modelled inferences, use the source's clues plus knowledge students can be expected to have; never lean on outside cultural facts the source doesn't give.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "76",
     "quote": "**INFER** (\"combine text clues with what you know\";",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "79-80",
     "quote": "struck an earlier worked example that let the 4b extension reach for outside-world knowledge",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "80-82",
     "quote": "an inference may only use what the passage's own words show; extension deepens the mood from remaining text clues, never a civic/cultural fact the passage never gave.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim. The same file defines inference as text clues plus what you know, so 'only what the source supplies' contradicted the course's own definition; the ruling targets outside facts students can't be expected to know. The kb-0204 line is about which context to teach (truth 20), so it is removed."
  },
  {
   "index": 88,
   "verdict": "keep",
   "statement": "Every claim about the source in a stem, model answer or feedback line must trace to the source's own words; invented causes and unsupported 'only' claims are defects.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "167-168",
     "quote": "must be directly traceable to the passage's own words — invented causes and unsupported superlatives are a defect class, not a style choice",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim. Lines 153-156 record the live-walk findings (an invented cause, an unsupported 'only' claim) fixed in one batch. It extends truth 1's 'only what is true' to stems and model answers."
  },
  {
   "index": 89,
   "verdict": "keep",
   "statement": "Test any copy-detection guard against correct answers; with a long target sentence, exact correct recall gets marked as copying.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "194-195",
     "quote": "misreads a child's exact, correct recall as an illegitimate copy and demotes it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "194-196",
     "quote": "the answer checker's echo guard (0.70 threshold) misreads a child's exact, correct recall as an illegitimate copy and demotes it — proven when an 86-character L5 candidate sentence failed and a 66-character one",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim, and 86 vs 66 characters and the 0.70 threshold match. Related to truths 10 and 36, but specifically about false positives from a copy guard."
  },
  {
   "index": 90,
   "verdict": "keep-with-fix",
   "statement": "Tie each option's feedback to the option itself, not to its position, so shuffling the options keeps the feedback correct.",
   "kind": "adopted gate",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
     "lines": "38",
     "quote": "zero option-position fallback IDs and zero truncated claim/recheck templates",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
     "lines": "71-73",
     "quote": "the detector and gates now cover every supported selected-response format. All 1,234 option-specific routes have zero option-position fallback IDs",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The quote is on line 38, not 38-39 (it also recurs at lines 72-73). The shuffling rationale is an inference; the source records a gate result over 1,234 option-specific routes, and the re-review found a generic-feedback blind spot rather than position-keyed errors as such."
  },
  {
   "index": 91,
   "verdict": "keep-with-fix",
   "statement": "Present every explanatory model or diagram as a simplification, not literal reality.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0141-cross-cutting-science-misconception-synthesis.qmd",
     "lines": "144",
     "quote": "it MUST include a brief framing statement indicating that the model is a simplification.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0141-cross-cutting-science-misconception-synthesis.qmd",
     "lines": "140",
     "quote": "**Every model should carry an explicit health warning:**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "66",
     "quote": "diagrams or models presented as literal reality;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. The scope is narrowed to explanatory models, since the source means scientific models, not every map or diagram. The point holds for models in any subject."
  },
  {
   "index": 92,
   "verdict": "keep",
   "statement": "When content carries another subject's ideas, revisit what that subject has taught from a fresh angle, keep its framing, check it against that subject's misconception list, and don't make it the first place students meet a new concept.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "36",
     "quote": "the Read/Write lesson should be consistent with how it was framed in the subject app",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "75",
     "quote": "must go through the misconception-check process.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "81",
     "quote": "It is better to re-encounter ideas from earlier grades than for Alpha Read or Alpha Write to be the first place a student meets an idea.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "19",
     "quote": "so at any given moment we cannot be sure whether a student has studied a topic.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the found_by reason is now quoted from line 19. The misconception check is required for science content in particular."
  },
  {
   "index": 93,
   "verdict": "keep",
   "statement": "Choose content by a visible, scored rule that others can challenge, and let a person override it with a stated reason.",
   "kind": "reviewer-endorsed practice",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "17",
     "quote": "Scoring topic selection with a formula is the reviewers' favorite feature because it is testable.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "18",
     "quote": "A person overrode the score and gave a reason rather than allowing the number to decide.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. It rests on one review's praise and is a preference about how decisions are made, not a learning result; kept as reviewer-endorsed practice."
  },
  {
   "index": 94,
   "verdict": "keep-with-fix",
   "statement": "State each unit's target as one plain-language sentence, and link units through big ideas rather than surface facts.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "51",
     "quote": "one plain-language sentence stating what the whole unit is really about.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "52",
     "quote": "Make cross-unit links about big ideas rather than surface facts.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, but 'testable' was not in the source, so it is removed."
  },
  {
   "index": 95,
   "verdict": "keep",
   "statement": "What a test asks shapes what gets taught; if the default check is a short source with a few multiple-choice questions, teaching narrows to that.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0108-rand-appendix-b-assessment-rfa.qmd",
     "lines": "127-131",
     "quote": "as long as we define comprehension by default as reading a passage and answering a few multiple-choice questions about it, teachers will have little incentive to instruct children in ways that reflect a deeper and more accurate conceptualization of the construct.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim. It is an expert panel's argument (2002), not a measurement; the statement doesn't overstate it."
  },
  {
   "index": 96,
   "verdict": "keep",
   "statement": "Agreement that comes from one source copied twice is not independent replication.",
   "kind": "measured (one case)",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "30-31",
     "quote": "not two teams replicating independently. Treat it as a hypothesis-transfer, not a cross-validated law.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim (the claimed convergence was between the AP generator project and grade 3). Related to truth 35, but about where agreement comes from rather than model samples."
  },
  {
   "index": 97,
   "verdict": "keep-with-fix",
   "statement": "Label machine-written and machine-checked material for what it is; don't call it real, authentic or cleared.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "45",
     "quote": "don't relabel machine-authored cold passages as \"real.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "120-121",
     "quote": "Replace the two remaining `cleared` phrases in MCQ/MCQ_SET with `machine-checked` or `selected`.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "81",
     "quote": "\"built and machine-verified, awaiting human review,\" never more.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "44",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the kb-0064 phrase is on line 45, not 44-45. 'Certified' was removed: the project deliberately uses machine certification (its own certification standard and certified banks), and the sources only rule out 'real' and 'cleared'. It applies truth 44 to labels."
  },
  {
   "index": 98,
   "verdict": "keep",
   "statement": "Open question: can item- or lesson-level benchmarks judge how a course sequences and builds knowledge across units, or does course quality need course-level measures?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0125-coe-catchup-2026-07-13.qmd",
     "lines": "101-103",
     "quote": "Incept Bench remains useful at question/lesson level, but new metrics are needed to assess lesson sequencing and knowledge building",
     "verbatim": true
    }
   ],
   "against": "kb-0093 line 63: \"course A4/A5 reward redundancy, spaced revisiting, and knowledge compounding;\". Some course-level criteria already exist, so the open part is whether they suffice.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The original quote is on lines 102-103; it is extended to lines 101-103. It records meeting notes, so it stays an open question rather than a finding."
  },
  {
   "index": 99,
   "verdict": "keep",
   "statement": "Open question: should named thinking routines fade once a stated condition is met, or keep returning as scheduled retrieval?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "41",
     "quote": "named inference routines as *fading scaffolds* retired on a stated condition (our stance, per Willingham DOK1-3) vs. scheduled recurring retrieval of the routine",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "41-42",
     "quote": "scaffolds fade across a unit (a procedure \"collapses into a two-step option after five successful uses,\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "42-43",
     "quote": "G3 Peter Pan never got past one lesson per scaffold level, so this stayed unimplemented",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; the KB holds the dispute open and records the ruled fade as never implemented."
  },
  {
   "index": 100,
   "verdict": "keep",
   "statement": "Open question: for spaced review, is it better to keep fine-grained knowledge units and cluster them, or merge them into fewer, richer units?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0116-graph-architecture-brainlift-core.qmd",
     "lines": "83",
     "quote": "There is one proven response and one speculative alternative, and it is not yet clear which is better.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim; the source says outright that it is unresolved."
  },
  {
   "index": 101,
   "verdict": "keep",
   "statement": "Open question: should mastery checks use the formats practised during teaching, or should practice deliberately differ from the final test's format?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "140",
     "quote": "Mastery tests should match formats experienced during instruction.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
     "lines": "61",
     "quote": "Assessment format is not instruction format (the marathon rule)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd",
     "lines": "123-124",
     "quote": "Format familiarity is measurement hygiene, not test prep (construct-irrelevant variance, AERA/APA/NCME Standard 1.13).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim; three sources genuinely pull in different directions, so it is properly an open question."
  },
  {
   "index": 102,
   "verdict": "keep-with-fix",
   "statement": "Adjust feedback and help as proficiency grows; too much lowers active processing and masks misconceptions, too little leaves students floundering.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "161",
     "quote": "Too much feedback can reduce active processing; feedback timing should shift as proficiency improves.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0157-mastery-signal-evidence-base.qmd",
     "lines": "437",
     "quote": "Explains why simply increasing support (hints/steps) can raise short-term success without improving learning, and why too little support produces floundering.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd",
     "lines": "239",
     "quote": "Too much guidance can mask misconceptions; too little creates failure loops",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim, but 'masks misconceptions' had no cited support until kb-0156 line 239, now added. It overlaps candidate 62 and could be merged with it."
  },
  {
   "index": 103,
   "verdict": "keep",
   "statement": "A mastery check should vary the surface form, include near-miss contrasts, and withhold scaffolds and feedback, so it tests the intended generalisation rather than same-day recall.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0156-assessment-mastery-signal-core.qmd",
     "lines": "238",
     "quote": "first-exposure gating must include surface variation and near-miss contrasts—not only isomorphic items.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "158",
     "quote": "E4 mastery gate: no feedback, delayed, varied, independent.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. It adds design detail (surface variation, near-miss contrasts, no scaffolds) to truth 48."
  },
  {
   "index": 104,
   "verdict": "keep-with-fix",
   "statement": "Keep content-file checks, live walkthroughs and package or claim audits apart; a content check must not claim how the lesson behaves at runtime.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "52",
     "quote": "InceptBench should not overclaim runtime behavior or package truth.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "49",
     "quote": "| 2 | runtime / behavioral enforcement | live student-seat walkthrough harness | only encoded intent, not actual enforcement |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The quote is on line 52, not 52-53; the three-way split is now quoted from the table (line 49). Related to truths 24 and 46."
  },
  {
   "index": 105,
   "verdict": "keep-with-fix",
   "statement": "Declare what a product is, a teaching course or a practice and assessment tool, before judging it; the declaration decides which criteria apply.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "135",
     "quote": "product-type declaration: comprehension curriculum vs MAP-practice determines applicable criteria;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "40",
     "quote": "If it is decided that this should be a MAP practice app, the recommendations below would be different.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quote is verbatim. The found_by claim (a practice-app framing would change the recommendations) is now quoted from the review itself. Related to truth 63."
  },
  {
   "index": 106,
   "verdict": "keep",
   "statement": "When reviewing, define the student as the full range of real users, including below-level readers, language learners, keyboard and screen-reader users, guessers and click-throughs, not one ideal path.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0092-student-ready-criticism-framework-2026-07-09.qmd",
     "lines": "23-24",
     "quote": "A student is not a solver, a row in a ledger, a completed QTI attempt, or an ideal reviewer clicking the intended path.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0092-student-ready-criticism-framework-2026-07-09.qmd",
     "lines": "25-27",
     "quote": "Include below-grade readers, English learners, keyboard-only users, screen-reader users, frustrated students, test-wise students, and students willing to click through or guess.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "Quotes are verbatim. It adds the population definition behind truths 46 and 47."
  },
  {
   "index": 107,
   "verdict": "keep-with-fix",
   "statement": "A stem must not contain, define or share the root of what it tests.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "48-49",
     "quote": "the `L.3.4` template pre-defined the affix in the stem → rewritten to be passage-dependent",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "51-52",
     "quote": "**VOCAB-ROOT-IN-STEM** (a stem contains the root of the taught word it is testing)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The original quote is on line 49; it is extended to lines 48-49 to include the template. The root check is a census flag, not yet a validator (kb-0183 line 50). Serves truths 3 and 5."
  },
  {
   "index": 108,
   "verdict": "keep-with-fix",
   "statement": "Report completion alongside accuracy; accuracy can't show a course works when most students do little of the intended work.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "37-38",
     "quote": "the incumbent's real failure is 12.5% median completion, ~30% of intended work done;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false,
   "reason": "The original quote (kb-0079 line 34) is verbatim, but that path carries a person's name. kb-0217 lines 37-38 report the same 12.5% and ~30% figures, so the evidence moves there. The found_by claim that accuracy was measured only on completed items is an inference, not stated in either source."
  }
 ],
 "existing_checked": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
   "lines": "118",
   "quote": "A wrong answer is told why it is wrong and where to go, never what the answer is",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports (lines corrected from 130-131)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
   "lines": "129-130",
   "quote": "were handing over the Step 3-4 answer outright; fix was to rewrite to criterion cues only",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "43",
   "quote": "an immediately available hint lowers desirable difficulty. The durable rule is attempt first, then targeted help.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports (weakly: a 40-student design pilot, not a randomised result)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
   "lines": "63",
   "quote": "design-science pilot reported more consistent scaffolding and less premature answer-giving",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter (single-select items are never revealed after N tries)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
   "lines": "135-137",
   "quote": "a single-select (`mcq`) item is *never* revealed after N tries (`validate-contracts.mjs` fails an `mcq` carrying `reveal_after_tries`), because a short, closed option list lets the child eliminate their way to the answer",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "supports (the review faulted feedback that never showed the correct answer)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
   "lines": "50",
   "quote": "with no explanation and no correct answer shown",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
   "lines": "66-67",
   "quote": "~78% of raw generated items were blind-solvable before this gate; G5 bank certified 1.67%/0%/0% across 172 items",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
   "lines": "45",
   "quote": "An item answerable without the passage is not measuring reading",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "qualifies (a model blind solve may misjudge what real students can do), not a counter to the rule",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd",
   "lines": "182",
   "quote": "LLM ablation may false-positive/negative vs real students",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
   "lines": "50-51",
   "quote": "(correct answers were ~75% option \"A\" → shuffled ~even A/B/C/D)",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "56",
   "quote": "Key-position/length balance needs an authoring-time check (12/19 A-keys shipped before the lens).",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0159-mcq-principles-blueprints.qmd",
   "lines": "56",
   "quote": "positional bias of B ≈ 30%, C ≈ 29% vs. A ≈ 19%, D ≈ 22%",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports (a judge that could not run produced 11 phantom fails)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
   "lines": "70-71",
   "quote": "preflight refuses a keyless judge (\"HARNESS, NOT CONTENT\" — 2026-09-03 cost 11 phantom FAILs once)",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports (source uses a curly apostrophe; quote corrected)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
   "lines": "629",
   "quote": "If language mechanics are not part of the claim, either score them separately or don’t score them.",
   "ok": true
  },
  {
   "truth": 12,
   "effect": "supports by analogy only (evaluators veto instructions injected into the content they score, not student words)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
   "lines": "64",
   "quote": "all three evaluators have Step-0 injection veto;",
   "ok": true
  },
  {
   "truth": 13,
   "effect": "supports (pre-specify accepted variants and near-misses in advance)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0153-assessment-pack-brainlift.qmd",
   "lines": "120",
   "quote": "pre-specify acceptable variants (equivalence classes) and typical partial solutions (near-misses)",
   "ok": true
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
   "lines": "71",
   "quote": "a single correct answer is not proof of knowledge and a single incorrect answer is not proof of ignorance.",
   "ok": true
  },
  {
   "truth": 15,
   "effect": "supports (two sentinel items per unit, a third when they disagree)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0154-diagnostic-assessment-brainlift.qmd",
   "lines": "159",
   "quote": "so that a single lucky guess or unlucky slip doesn't derail the binary search.",
   "ok": true
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0251-g9-prep-pack-index-manifests-leadership-playbook.qmd",
   "lines": "38-39",
   "quote": "Open Source Shakespeare numbers it 43, and Gutenberg and MIT have no numbers.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports (lines corrected from 59-60)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0115-reading-science-folder-2026-07-10.qmd",
   "lines": "58-59",
   "quote": "Full texts attached by file copy, never re-emitted through a model",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
   "lines": "139",
   "quote": "| **Context must be what the text uses.** | Recht & Leslie (1988); Smith et al. (2021) | Only context students will need in Act 1, not general history. |",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0204-g9-year-9-ela-lesson-design-specification.qmd",
   "lines": "137",
   "quote": "A map, a chain-of-command diagram, and key words appearing as they're spoken.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports (line corrected from 54-55)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "55",
   "quote": "the live-rendered surface must be reviewed, not just source artifacts.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
   "lines": "24",
   "quote": "the historical model snapshots are withdrawn after source changes.",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "31",
   "quote": "remove redundant UI prose such as instructions whose action is already obvious",
   "ok": true
  },
  {
   "truth": 27,
   "effect": "supports (contrast failure)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "105",
   "quote": "rendered black text on a black background, legible only on hover.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0121-teaching-comprehension-insights-brainlift.qmd",
   "lines": "34",
   "quote": "design-time contracts alone demonstrably failed to prevent any of it.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "does not support: it is about predictions swinging under paraphrase, not verdicts varying between runs",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
   "lines": "65",
   "quote": "if small wording changes cause wild swings in your predicted difficulty, the prediction is probably wrong.",
   "ok": false
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
   "lines": "83-84",
   "quote": "same-model resamples (agreement = self-consistency, not cross-family agreement)",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
   "lines": "482",
   "quote": "Models converge on machine consensus, not human difficulty.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports (position effects)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
   "lines": "655",
   "quote": "LLM judges show left/right (or first/second) position effects and favour more verbose responses",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
   "lines": "64-65",
   "quote": "GO requires every in-scope case caught, zero false flags on controls, agreement >= 0.8. **NO-GO stands; semantic lints remain advisory.**",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0153-assessment-pack-brainlift.qmd",
   "lines": "69",
   "quote": "include an ex-post agreement check against human scoring and record thresholds for acceptable concordance.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
   "lines": "42-43",
   "quote": "drive ONE real sub-90% attempt and observe the block",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
   "lines": "472",
   "quote": "use seeding (gold scripts) to check drift",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0099-student-simulation-lab-2026-07-09.qmd",
   "lines": "67",
   "quote": "Prepare knowledge -> encounter text -> model thinking -> guided same-process practice -> student articulation -> evidence check -> delayed/varied transfer",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
   "lines": "62",
   "quote": "Students need to read the text first",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
   "lines": "55-56",
   "quote": "That green state is not the semantic verdict.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "57",
   "quote": "A clean automated report is useful pre-review evidence, never a substitute for reviewer judgment.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0131-pedagogy-decision-bank-experiment-intake.qmd",
   "lines": "359-360",
   "quote": "the metric and aggregation may not be changed after pilot results.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports as a cautionary case (the AP bar was moved mid-project)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
   "lines": "9",
   "quote": "The bar was REPINNED 2026-06-08 from the original (overall >=0.85 on 99% across all 10 cells, clean K=1) down to",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports (source uses a curly apostrophe; quote corrected)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
   "lines": "612",
   "quote": "don’t create ad-hoc categories after seeing scripts.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
   "lines": "99",
   "quote": "they want to click through a complete lesson exactly as a student would to confirm the flow.",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "qualifies (simulated students cannot fully play low ability; the model's competence leaks through)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
   "lines": "75",
   "quote": "the model's underlying competence leaks through role-play.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "149",
   "quote": "A same-day lesson gate proves at most \"I can do it now,\" not \"I can still do it later under changed conditions.\"",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
   "lines": "19",
   "quote": "In-app success must predict performance on credible external assessments.",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0119-curriculum-architecture-brainlift-evidence.qmd",
   "lines": "226",
   "quote": "restudy feels productive, but retrieval produces stronger delayed learning.",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0033-problem.qmd",
   "lines": "88",
   "quote": "Gamification often rewards *completion* rather than *mastery*.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0158-assessment-pattern-library-brainlift.qmd",
   "lines": "475",
   "quote": "Two-to-four checks: (1) correct principle stated, (2) applied to the case, (3) addresses counter-case/constraint, (4) conclusion warranted.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports, but contested: kb-0063 lines 53-55 call the source-grounding win smoke-only (n=6, unconfirmed by the real grader), and kb-0064 calls the jump refuted (lines corrected from 71-72)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
   "lines": "72",
   "quote": "let it write only the questions) was the biggest real lever",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "undercuts the supporting entry above (the jump was a judge artifact); it is not evidence against the rule itself",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
   "lines": "9",
   "quote": "aptraining's headline '0.29→0.95 via real passages' is REFUTED",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "counter by doctrine only (prescribes prohibition lists for AI content; reports no measured effect)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0141-cross-cutting-science-misconception-synthesis.qmd",
   "lines": "214",
   "quote": "Tier 1: Absolute Prohibitions (Apply at ALL grade levels, ALL subjects)",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0075-incept-curriculum-api-g5-backbone-2026-06-30.qmd",
   "lines": "9",
   "quote": "(NOT CC/Reading/5, which is only a curated L+RL subset)",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0069-self-audit-insights.qmd",
   "lines": "73",
   "quote": "The \"8,937 passes\" is the served-99 best-of-N exploit reborn.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports (lines corrected from 115-117)",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0080-map-proxy-case-for-approval-2026-07-02-incept-map-proxy-approval-package.qmd",
   "lines": "116-117",
   "quote": "The audits found number drift in documents (0.930 vs 0.928) — which is why the gate lives in code.",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0153-assessment-pack-brainlift.qmd",
   "lines": "323",
   "quote": "rubric use can increase scoring consistency, especially when rubrics are analytic, task- or topic-specific, and supported with exemplars and/or rater training.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports (two things changed at once, so no lift follows); the file's path carries a person's name",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0100-[name]-lanes-execution-2026-07-10.qmd",
   "lines": "46-47",
   "quote": "No lift or calibrated discrimination follows.",
   "ok": true
  }
 ]
}
```
