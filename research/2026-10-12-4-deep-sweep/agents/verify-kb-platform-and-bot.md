# verify:kb-platform-and-bot

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "kb-platform-and-bot",
 "verified": [
  {
   "index": 0,
   "verdict": "keep",
   "reason": "All three quotes are verbatim at the cited lines. The numbers match (1.0; 4/11, 8/11, 3/11, 36%; 100%). This is distinct from truth 5: it says a general quality score cannot stand in for the text-dependence check. The reader's counter sits in a folder whose name carries a person's name, so the same counter-decision is cited from kb-0072, together with the later re-gate that answers it.",
   "statement": "A high score from a general quality judge does not show an item is sound; items it rated perfect still leaked their answers, so whether the material is needed has to be checked separately.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "9-10",
     "quote": "**InceptBench ≥0.9 is necessary, not sufficient.** IB grades *instructional* quality — it scored **answer-leaking items 1.0**. So a clean IB score does **not** mean an item is sound.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md",
     "lines": "9-10",
     "quote": "**Result: 4/11 CONFIRMED leaks, 8/11 answerable-blind, only 3/11 cleanly passage-dependent → a 36%-leaky bank that IB had passed.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd",
     "lines": "114-115",
     "quote": "Observed failure (DAPO epoch 0): model generated `\"What is the primary function of chlorophyll?\"` from a photosynthesis passage. IB score: 1.0. Blind-solve rate: 100%.",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd lines 77-78 records a call to skip the blind re-check: \"prior call was that re-checking IB+Opus-passed items is redundant — logged as corroboration, not re-pushed.\" A later re-gate by two model families found 334 of 353 supposedly safe items leaky (knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd lines 127-129).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, and ~0.14, IB 1.0 and 100% match. The evidence is one tuning run plus the spec's reading of its plateau. I narrowed 'alone' to a score that does not test text-dependence, and widened 'scored on' to 'selects or rewards'. I also added the AP generation effort's record that its score rose when the passage was removed so the grader skipped its leak probe, which shows that tuning exploits whatever a score leaves out.",
   "statement": "A writer tuned against a quality score that does not test text-dependence converges on well-formed questions that can be answered without the material, so text-dependence has to be part of what selects or rewards it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd",
     "lines": "111-112",
     "quote": "InceptBench (existing reward function) measures structural quality: well-formed stem, single key, near-neighbour distractors, valid CCSS label. **It has no concept of passage-dependency.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd",
     "lines": "115-116",
     "quote": "Reward plateau at ~0.14 confirmed the model had converged to structurally-valid leaked questions.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd",
     "lines": "118",
     "quote": "The two quality dimensions are orthogonal. Both must be in the reward signal.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "102-104",
     "quote": "the correction is \"optimize the course, not the item\" — a course where every item scores IB 1.0 but 90% is blind-solvable is a failed course",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "26-27",
     "quote": "The actual MCQ fix was the **OPPOSITE** of \"add a real passage\" — it was **REMOVING the stimulus** so the grader's leak-probe is skipped. That's **grader-gaming**, not a provenance win.",
     "verbatim": true
    }
   ],
   "against": "The cheap text-dependence terms proposed for the reward barely separated leaky items from clean ones (knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd lines 170-171, AUC about 0.5). Under the shipped reward, a reworded leak outscored a genuine requires-reading item (lines 186-188). The recommended design keeps the cross-family blind solve as out-of-loop ground truth and checkpoint selection, not as the per-rollout reward (lines 180-184).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (1.0). The evidence does not isolate the claim that a same-family judge 'shares the writer's blind spots', because that judge never tested text-dependence. I restated it as what was observed and kept it as the adopted rule the spec makes mandatory. It is related to truth 66 but concerns the judge's model family.",
   "statement": "Check items with a judge from a different model family than the writer; the writer's own family, used as the quality judge, passed items that leaked their answers.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/generator-output-spec.md",
     "lines": "27-29",
     "quote": "IB grades *instructional* quality (it scored answer-leaking items 1.0) **and IB itself grades via the same model family as the generator**, so a same-family judge cannot catch leakage. The different-family check is mandatory.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "26",
     "quote": "So **generator and judge are the same model family** — a built-in proxy-gaming hazard (the spec's §8 / §3 anti-leak warning, and exactly aptraining's failure mode).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "64-65",
     "quote": "an InceptBench judge that runs on the same Gemini as the generator passed answer-leaking items 1.0.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0090-fable5-plan-traces-2026-07-09.qmd",
     "lines": "131",
     "quote": "a lane cannot certify its own items;",
     "verbatim": true
    }
   ],
   "against": "A different family is not enough on its own. A weak different-family solver over-credited items that a stronger one caught (knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd lines 67-69), and every label came from one solver family (lines 188-189). The same-family judge also had no text-dependence test at all (pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd lines 111-112), so the misses cannot be put down to model family alone.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "Both quotes are verbatim. 95, 20 (21%), 75, 334/353 (94.6%), 19 and 93-95% all match; the 'difficulty bands' in the finding were reading-level bands. It adds solver strength and a two-family union to truth 5. It overlaps candidates 2 and 7.",
   "statement": "The blind solver's strength sets the bar: use a strong solver and count an item clean only if solvers from more than one model family all fail it without the material.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "67-69",
     "quote": "showed the weak gpt-4o-mini gate had over-credited items — of v1's 95 re-gated \"clean\" items, only **20 (21%) survived**; **75 leaked** under the strong solver.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "127-129",
     "quote": "union-of-detection (clean only if BOTH fail to recover). Binding result: 334/353 leaky (94.6%), only **19 genuinely clean**; leak was uniform across all three Lexile bands (93-95%), i.e. systemic to how these items were authored, not band-specific.",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/HOTBUCKET.md lines 320-322: \"the old `claude-fable-5` blind-solver was over-strict in the wrong way and inflated blind accuracy; `claude-haiku-4-5` re-baselined 10 MCQs to clean by returning `UNKNOWN` on true passage-dependent items.\" A solver can also err the other way, so it needs calibration.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (3/8, 0.71875, 10 MCQs, N=5, k≥3/5). 'Count any correct blind answer as a leak' overstated the evidence: the caught item was judged on 3 of 8 exact recoveries, and the productized gate fails an item at 3 of 5 trials. One lucky guess is not the rule.",
   "statement": "Let the blind solver answer 'unknown' instead of forcing a guess, and judge leakage from its correct blind answers over repeated trials against chance, never discounting them for low reported confidence.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "180-182",
     "quote": "promotion review caught `r3-09` at 3/8 exact blind recoveries and 0.71875 mean partial accuracy; low model confidence had wrongly hidden those hits.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "320-322",
     "quote": "the old `claude-fable-5` blind-solver was over-strict in the wrong way and inflated blind accuracy; `claude-haiku-4-5` re-baselined 10 MCQs to clean by returning `UNKNOWN` on true passage-dependent items. Use this for blind-solver calibration.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "74-75",
     "quote": "(passage withheld, model+version pinned, temp 0.3, **N=5, FAIL at k≥3/5**, per-format answer-space rules, `ablation_trials[]` persisted)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 58/3, 79/14 and 86/41 match. It restates truth 5 (a question must need the text) but adds the with-material control and the chance baseline, with evidence. I kept it as evidence for truth 5.",
   "statement": "Accept a question that depends on the material only if it is answered correctly with the material and fails without it, and compare blind accuracy against chance.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "305-306",
     "quote": "The key rule: accept only after with-passage control plus cross-family blind failure; this is generation/gating evidence, not SME approval or TimeBack publish proof.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "64-65",
     "quote": "Rejected items recovered far above chance (sequence 58% vs. 3% blind; hot-text 79% vs. 14%; match 86% vs. 41%), which is the evidence the kept 97 require the passage.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "5",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The verdict-file line shows the solver flagging a general-knowledge path, not a confirmed leak: its blind pick did not match the key. The root-cause finding and the passage-type rules carry the claim. The later re-gate found leakage systemic to how the encyclopedic-heritage items were written (kb-0235 lines 127-129).",
   "statement": "Material that retells a well-known case or encyclopedic fact lets questions be answered from general knowledge, so base text-dependent questions on specific, unfamiliar content such as a particular decision, stance, reversal or causal chain.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "37-38",
     "quote": "regeneration was abandoned — the root cause is passage design (encyclopedic passages), not item quality.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd",
     "lines": "50-52",
     "quote": "4 encyclopedic passage types to **avoid**: curriculum-fact, headline-figure, biography, generic-process 6 cold passage types to **use**: decision-reaction, argument-stance, obscure-consequence, surprising-reversal, specific-comparison, causal-chain The passage-necessity test: \"Could a student who studied this topic but did NOT read this passage answer correctly?\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/passage_blind_verdicts.json",
     "lines": "90",
     "quote": "General-knowledge leak (trophic cascade): the item mirrors the well-known Yellowstone wolf",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd line 29: \"Topics taught in an earlier grade are always fair game for re-encounter, even though we may not know the student's actual grade in social studies or science.\" Familiar topics are wanted for teaching material, so the rule applies to transfer and blind-checked items.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (97/100/80 vs 24/42/0; 99.5/100/~0.56; 20 of 95; 187 of 3,146). The low rates for locate, order and sort formats came from the first gate. The strong-solver re-gate left about a fifth of the 'clean' items and 5.9% of candidates, so I restated the contrast as depending on the solver.",
   "statement": "Measure blind-solve leakage per item format and with a strong solver: single-choice items leaked almost entirely and formats that make the student locate, order or sort evidence leaked far less under the first gate, but a strong solver found most of those leaking too, so no format is leak-proof by design.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "35-36",
     "quote": "because the anti-leak gate scored MCQ 97% / MSQ 100% / EBSR 80% blind-recovered (reject) vs. hot-text 24% / sequence 42% / match 0% (pass).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "105-106",
     "quote": "Measured leak by type: MCQ 99.5%, MSQ 100%, hot-text/sequence/match/EBSR ~0.56% after the 06-24 passage-design fix.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "67-69",
     "quote": "showed the weak gpt-4o-mini gate had over-credited items — of v1's 95 re-gated \"clean\" items, only **20 (21%) survived**; **75 leaked** under the strong solver.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "69",
     "quote": "Of 3,146 un-gated existing candidates, only 187 (5.9%) survived the strong blind-solve.",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0090-fable5-plan-traces-2026-07-09.qmd lines 132 and 134: \"selected response is not inherently leaky, but raw selected-response items often are;\" and \"hot-text and sequence formats need extra suspicion because renderer/protocol and guessability issues can masquerade as content quality.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The generator quote sits at lines 78-79, not 79-80. I folded the counter-evidence (announcing the decoy is itself a cue) into the statement.",
   "statement": "Matching items resist guessing when the pairing is fixed by the material (who said it, which part of the text, or 'not mentioned') rather than by a common association, and when an extra target, not announced as a decoy, stops the last pair being found by elimination.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0090-fable5-plan-traces-2026-07-09.qmd",
     "lines": "133",
     "quote": "match designs work when they force source/POV attribution, which-half attribution, or not-mentioned discrimination;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "48-49",
     "quote": "**Match** — ≥3 text-grounded pairs (note: 3×3 equal-sides has a minor elimination cue — prefer a 4th distractor category where the generator supports it).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "78-79",
     "quote": "The correct pairing must be fixed by the passage, NOT by a canonical real-world association.",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd lines 132-133 flagged \"192 match items announcing a decoy bucket\": announcing the decoy is itself a cue.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. This is a harness rule, not a measured comparison. I scoped it to comprehension items because some in-lesson checks are meant to stay literal (see candidate 97).",
   "statement": "In a question meant to show the text was understood, key the answer to a relationship the material asserts and make an inference need two or more sentences together; a key that is one retrievable fact is easy to leak.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "48-51",
     "quote": "prefer keys that hinge on a **relationship the passage asserts** (a cause the text names, a contrast the text draws, an inference the text licenses) rather than a lone retrievable noun — denser passages make relational keys both natural and harder to leak.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "53-54",
     "quote": "For inference/theme items, quote the two-or-more sentences whose combination licenses the inference (no single-sentence lift).",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd lines 64-66: \"whether the 20.09 reading-checks-stay-retrieval ruling (checks stay literal) extends to requiring the literal check be about the hinge specifically.\" Some in-lesson checks are deliberately literal retrieval.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "All quotes are verbatim. It is distinct from truth 6, which checks each option; this candidate says how wrong options are built.",
   "statement": "Build each distractor from a real detail of the material with one element swapped, so rejecting it means returning to a specific sentence; absurd or filler options give the key away by elimination.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "55-59",
     "quote": "**Near-neighbour distractors.** Distractors are built from *real passage details*, with the wrong actor / stage / effect / cause / claim swapped in. No distractor may be absurd or eliminable by world knowledge alone. (Absurd distractors leak the key by elimination.) At G5, a near-neighbour distractor should require *returning to a specific sentence to reject* — that is the bar.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "69",
     "quote": "| F13 | major | Chunk-stop distractors are self-declared filler, not real near-neighbour traps. |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "26",
     "quote": "| 5 | **Near-neighbour distractors** — plausible, text-adjacent, not obvious-eliminable | one-obvious-right + 3 throwaways |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. 'Where a common-knowledge answer exists, make it a wrong option' dropped the harness's own condition: only when the passage takes a specific or counter-typical stance. Without that condition the rule would key against what is true. I extended the quote to include the condition.",
   "statement": "When the text takes a specific stance that differs from the common-knowledge default, offer that default as a wrong option, so a student who has not read the text is pulled toward it.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "60-64",
     "quote": "**Bait the blind solver.** When a world-knowledge default exists, make it a *wrong* option (a \"live trap\"). This actively *punishes* the non-reader rather than merely failing to help them. At G5, the most common GK default is the textbook-true generalization; if the passage takes a specific or counter-typical stance, key to the passage and make the textbook generalization a distractor.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "149",
     "quote": "if the key matches the textbook default, treat that as a GK leak.)",
     "verbatim": true
    }
   ],
   "against": "none found in scope",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep",
   "reason": "The quotes are verbatim and 79% matches. It adds a length tell to truth 8's position rule.",
   "statement": "The correct option must not stand out as the longest, most specific, most hedged or only grammatical choice; check option-length parity item by item and across the course.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "66",
     "quote": "79% of correct answers in a generated course sat at option position A, and the correct option was systematically the longest",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "65-66",
     "quote": "**No surface tells.** Length- and structure-match the contending options. The key must NOT be the longest, the most specific, the most hedged, or the only grammatical fit.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "101-102",
     "quote": "The evaluators do not check the \"correct answer is longest\" tell. Build per-item and per-course length-parity census over correct vs distractor options.",
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
   "reason": "The quotes are verbatim. The confirmed seed-bank leaks were stem giveaways (item-quality.md lines 69-70).",
   "statement": "A question must not define, cue or restate its own answer: no defined word part, no word shared with the key, no restated target inference.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "24",
     "quote": "| 3 | **No answer giveaway in the stem** — no pre-defined affix/definition, no cue words | `\"the prefix 're-' means 'again'…\"` (answerable without reading) |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/passage_blind_verdicts.json",
     "lines": "137",
     "quote": "Stem giveaway + option self-evidence: the stem restates the full target inference",
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
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 6 of 6 and 33% match.",
   "statement": "In a two-part claim-and-evidence item, the evidence part must not restate or mirror the first part, and the first part must stand on its own instead of leaning on the second.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "67",
     "quote": "6 of 6 sampled two-part evidence items were blind-solvable, with Part B restating Part A — the same root cause measured at 33% gameable in G3",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "158-159",
     "quote": "For MSQ, all defensible answers must be keyed. For EBSR, Part B needs one uniquely strongest evidence choice and must not reveal Part A.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "74-75",
     "quote": "**Do not lean on Part B to rescue a GK-solvable Part A** — strengthen Part A independently.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (0/1/2). I added that the measurement proxy later moved its two-part items to partial credit, while the delivery scorer and the item standard still score all-or-nothing. The question stays open.",
   "statement": "Should a two-part claim-and-evidence item give partial credit (first part right earns some credit, both parts earn full credit) or require both parts? The project's documents point both ways.",
   "kind": "open-question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "85-86",
     "quote": "**EBSR/Composite = PARTIAL CREDIT (0/1/2)** — `MAP_COHERENCE_SHERLOCK_REPORT.md` (Sherlock-verified vs NWEA keys; Part A alone=1, both=2, Part A wrong=0). Their own MLEF scorer is binary → biases ability.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0024-beyond-alpharead-pr45-all-qti-types.qmd",
     "lines": "36-37",
     "quote": "**EBSR requires both parts**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "46",
     "quote": "**EBSR** — Part B uses **verbatim** passage sentences as evidence; **both parts** required to score.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "354",
     "quote": "kb-0072's divergences RESOLVED (bank 38→650; EBSR now PCM 0/1/2)",
     "verbatim": true
    }
   ],
   "against": "No measured comparison of the two scoring rules was found in scope. The live scorer and the item standard use all-or-nothing; the measurement proxy moved to partial credit.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim, but the course-quality file sits in a folder whose name carries a person's name, so I cite the same rule from item-quality.md line 45. The player finding (multi-select rendered as single-select) applies to every multi-select, counted or not. It is a delivery limit (candidate 104), not support for stating the count, so I dropped it here.",
   "statement": "A multiple-select question states how many answers to choose, and the keyed set must not simply be the longest options.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "45",
     "quote": "**MSQ** — stem states the explicit count (`\"Which TWO…\"`).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "86-87",
     "quote": "**msq** — exactly one defensible correct SET; the keyed set must NOT be \"the two/three longest\"; include at least one live-trap distractor",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 17,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. Offering the everyday meaning as a distractor only makes sense when the keyed sense differs from it, so the statement now says so.",
   "statement": "A word-meaning item must test a word that actually appears in the material and key the sense the material forces; when that sense is not the everyday one, offer the everyday meaning as a wrong option.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "90-95",
     "quote": "the keyed sense must be the one the PASSAGE forces, and at least one distractor must be the word's *common* dictionary sense that the passage does NOT use — so a blind solver who picks the everyday meaning is wrong. **The tested word and its keyed sense must both actually appear/operate in the passage** (guard against the G3 vocab-word-mismatch bug: never test a word that isn't in the passage, never key a sense the passage doesn't license).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md",
     "lines": "46-47",
     "quote": "**Vocab word-not-in-passage (NN#5):** FIX by editing the PASSAGE — `PUT {QTI}/stimuli/{id}` to use the word in context. Never reword the stem to dodge it; never delete the item.",
     "verbatim": true
    }
   ],
   "against": "How to repair a mismatch is disputed. One rule edits the passage to use the word (knowledge_bot/skills/timeback-course-fix/SKILL.md lines 46-47). Another forbids editing the passage to fit a quotation unless the passage itself is wrong (handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md line 171).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. Truth 3 already says nothing a student sees, including a picture, may give the answer first. This candidate adds a measured case: a diagram printing its own key let a child pass every diagram check without the passage. I kept it as evidence for truth 3. I scoped it to checks meant to need the text, because a diagram must carry what a diagram-reading check asks.",
   "statement": "A picture or diagram must not print the answer to a check that is meant to need the text.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "57",
     "quote": "prints its own answer key in-diagram (a key line stating the arrow rule, plus \"eater\"/\"diet unknown\" sub-labels) — lets a child pass every diagram check without reading the passage.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "66",
     "quote": "| F10 | major | No rendered check requires integrating both sources; the trap-item stem leaks the diagram's own fact. |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "3",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep",
   "reason": "The quotes are verbatim and 31 MCQs matches. It is related to truth 41 but concerns answers leaking across items and forms.",
   "statement": "Check each test form for items that give away other items' answers, including cross-form tells where one answer pair unlocks both forms.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0211-peter-pan-reviewer-round-2708.qmd",
     "lines": "24",
     "quote": "Both usage checks were crackable via the single pair \"baby\"+\"sleep\" | **FIXED** `f75a301` — Form 2's key de-correlated; a gameability sweep over all 31 L4+L5 MCQs found no other cross-form tell",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "51",
     "quote": "Form-level answer-position, option-length, duplicate, enemy-item, and blueprint reports.",
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
   "verdict": "keep",
   "reason": "The quotes are verbatim; 19,387, 31,240 and 1,329 match. The same file also records 340 duplicated stem clusters (lines 47-49).",
   "statement": "Check the whole bank for repeated and near-duplicate items; items generated one per call repeat in ways a per-item review cannot see.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0057-incept-team-sync-2-2026-06-18.qmd",
     "lines": "21-22",
     "quote": "Question bank has **repeats** (his API generates **one question at a time**, multiple quiz calls → duplicates) → needs an agent cleanup.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0057-incept-team-sync-2-2026-06-18.qmd",
     "lines": "49-50",
     "quote": "a **whole-course evaluator agent** (not per-item — catch repeats etc. that manual review catches; IB team could build it)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "32-33",
     "quote": "Greedy-selection rejection counters: 19,387 duplicate-item-id, 31,240 duplicate-question-text, 1,329 near-duplicate-question.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. I rewrote the statement to drop the job role ('the reviewers'). The source leaves the default to a human decision.",
   "statement": "When a fourth plausible distractor cannot be written, should a question have three options rather than fill the slot with an implausible one? A four-option requirement raised in review conflicts with a research summary that favours three.",
   "kind": "open-question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "40-43",
     "quote": "The reviewer says MCQs need at least four options. The MCQ BrainLift says the research consensus generally favors three options and recommends four as Alpha's default only when a third plausible, diagnostically useful distractor exists. Do not fill a fourth slot with an implausible option. Return `NEEDS_HUMAN` until the owner approves the default and exception.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/README.md",
     "lines": "94",
     "quote": "decide the three-versus-four-option MCQ policy when a fourth plausible distractor cannot be written;",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0241-alpha-read-contract-investigation-and-packager-build-2026-06.qmd line 109: \"arpack's \\\"exactly 4 choices\\\" gate over-restricts vs the API's real 2-6+ floor\". The delivery format itself accepts two or more options.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "The quotes are verbatim; 90%, 80% on 5 items, 4-5 items and 14 rather than 100 all match. kb-0093 line 141 names the same gate-arithmetic trap.",
   "statement": "A mastery gate needs enough items: on four or five items a 90% bar demands a perfect score, and an adaptive gate with a one-item bank can never reach mastery.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "54-55",
     "quote": "**A test with <5 items cannot certify mastery at 90%** (1 wrong = 80% on a 5-item test; un-gateable on a 4-item test). Gate tests carry **enough items** for a 90% threshold to be meaningful.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
     "lines": "37",
     "quote": "two 4-5 item tests are un-gateable (no \"90% of 4\"); no three-state retry / parallel forms.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0021-powerpath100-course-shape-rootcause.qmd",
     "lines": "26",
     "quote": "PowerPath scoring is **incremental**: one correct answer from 0 → score **14, not 100**.",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd lines 137-138: \"an arbitrary `>=15` bank-depth constant hardcoded in `audit_compliance.py` itself (circular — the spec just quotes the auditor); the real platform/publisher floor is 8.\" How many items are enough must itself be sourced.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The meeting-note quote is a sentence fragment but exact.",
   "statement": "Give every gated test at least two parallel forms with no shared items, so a retake shows new items rather than the same ones.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "39-40",
     "quote": "**Two parallel forms (A + B) sharing ZERO items.** Parallel forms are required for retry without answer leakage (a student who retests sees the other form).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0022-incept-team-sync-2026-06-17.qmd",
     "lines": "63",
     "quote": "**Reattempt:** same test re-shown (small chance of variety); randomizing via multiple tests is",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
     "lines": "32",
     "quote": "NN#7 single static form (gameable)",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd line 76: \"97/172 items can't populate disjoint parallel forms without overlap.\" A small clean bank cannot yet support parallel forms.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep",
   "reason": "The quotes are verbatim, and the score bands (0-49, 50-89, 90-99) and the 75%/25% split match.",
   "statement": "Spread item difficulty across easy, medium and hard; a single-difficulty form floors weak students, ceilings strong ones and silently disables adaptive selection.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "89-90",
     "quote": "A 100%-medium form **disables discrimination** — it floors weak readers and ceilings strong ones, measuring nothing. The form **must spread** across easy / medium / hard.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "29",
     "quote": "items carry easy/medium/hard (NOT 100%-medium) so PowerPath can ease/ramp. *(new — 100%-medium silently disables adaptivity)*",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0054-reference.qmd",
     "lines": "238-239",
     "quote": "difficulty by current score (0–49 easy; 50–89 medium+hard 75%/25%; 90–99 hard only)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 25,
   "verdict": "keep",
   "reason": "The quotes are verbatim; +1.3 logits, 200-210 and 206.4 match. This is a real conflict between a measurement review and a staged standard.",
   "statement": "Where should a predictive test's difficulty be centred — on the verified norm, on the actual cohort, or above grade? Centring above where students sit made on-grade students look as if they were failing.",
   "kind": "open-question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "90-92",
     "quote": "centering item difficulty at 200-210 (our kb-0059 \"by design\") maximizes info ~+1.3 logits ABOVE where students sit → makes an on-grade reader read as failing and biases logit→RIT regression.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "91-92",
     "quote": "**Center above grade.** A test centered at the grade median is too easy to confirm above-grade reading.",
     "verbatim": true
    }
   ],
   "against": "The two sources conflict. knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd lines 93-94 add: \"FAIL blueprints centered above the verified spring mean; reconcile vs the observed cohort mean 206.4.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The digest line is the digest's own summary of the report's point on p.114.",
   "statement": "A readability level is not item difficulty and cannot by itself decide whether a text fits; difficulty is a match among the text, the reader's knowledge and the task.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "97-98",
     "quote": "Lexile is a readability proxy, **not** item difficulty itself — flag it `[SECONDARY]`.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "48",
     "quote": "Text difficulty is a match among text factors, reader knowledge, and task — no single readability number can gate a text",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "705",
     "quote": "different readability estimates don't agree with each other and provide no diagnostic information for individualizing instruction.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Label item difficulty by its state — predicted, provisional from live use, or calibrated — and treat cut scores and thresholds as defaults until tuned on real attempt data; a model's pre-use estimate is not a calibrated value.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "54",
     "quote": "Difficulty metadata distinguishing predicted, provisional live, and calibrated states.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "66",
     "quote": "Do not call pre-use LLM difficulty a calibrated item parameter.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd",
     "lines": "153-154",
     "quote": "**No threshold calibration** — cut-scores, mastery gates, WCPM targets are reasoned pilot defaults, to be tuned against real attempt data.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "After items are used, review each one's functioning — option performance, subgroup fairness, drift — and quarantine or retire failures; score differences must not come from language, culture or background unrelated to the target.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "55-56",
     "quote": "Live-analysis plan covering minimum N, item and option functioning, subgroup/DIF review, uncertainty, drift, quarantine, and retirement.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "753",
     "quote": "Good comprehension assessments must be adaptable to individual, social, linguistic, and cultural variation; if performance differences reflect such variation rather than comprehension itself, the test is inadequate for the research/instructional agenda.",
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
   "reason": "The quotes are verbatim. The validator rule applies to check-bearing teaching atoms that declare no product_type. kb-0093 line 135 names the same product-type declaration.",
   "statement": "Declare each assessment's purpose — teaching check, mastery gate, diagnostic, interval or growth measure — before judging it, because the criteria differ, and treat a diagnostic result as a guide to study, not a grade.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "47",
     "quote": "Product declaration: formative, mastery, diagnostic, summative, or cold measurement.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py",
     "lines": "651",
     "quote": "product_type -- required to gate which criteria apply.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "63",
     "quote": "Do not call a diagnostic score a grade; diagnostics route study under uncertainty.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep",
   "reason": "The quotes are verbatim; the 24-item gate and raw/40 match. It is related to truth 48 but about keeping the two instruments apart.",
   "statement": "Keep the mastery gate and the growth measure as separate instruments; the growth test uses unseen material, is never gated on, and supports only direction claims until it is linked to the external scale.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "139",
     "quote": "These are **two distinct instruments** — do not conflate them.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "31",
     "quote": "the 24-item mastery GATE (`masteryThreshold:90`) is DISTINCT from the MAP-equivalent proxy (cold passages, raw/40+band, `gating=false`, no 90 threshold). Don't conflate.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "135-136",
     "quote": "The predictive claim (\"does well here → does well on MAP\") is **a design intent, not a measured result**, until the linking study runs.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Recognition items cannot certify production or integrated knowledge: a 'write' or 'explain' target needs a production task, and some tasks must combine several components.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "124",
     "quote": "N3: recognition-vs-production match. \"Write/explain/draw\" targets cannot be assessed by MCQ alone.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "129",
     "quote": "N8: integrative-assessment presence. Include tasks that coordinate multiple KCs, not only atomized checks.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "64",
     "quote": "Do not certify productive or integrative knowledge with recognition alone.",
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
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "A standards tag or a lesson's claimed skill must match the thinking its items actually require; an 'identify' item does not cover an 'analyze' standard.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "122",
     "quote": "N1: DOK-level alignment. Coverage is false if an \"analyze\" standard is assessed by \"identify.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "282",
     "quote": "standards tags do not match delivered cognitive work",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "114-115",
     "quote": "`concept_coverage` checks spread, not whether each lesson's claimed KC/skill matches what its items actually assess.",
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
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (0/28). I added the one-convention evidence the statement relied on but did not cite (timeback-integration.md lines 144-145).",
   "statement": "Tag every item with the standard it measures in structured item metadata, not in titles or prose, using one code convention that resolves in the official framework.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
     "lines": "32",
     "quote": "NN#4 **CCSS 0/28** (codes only in titles)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0082-rex-v2-live-course-pull-2026-07-02-rex-v2-live-course-pull.qmd",
     "lines": "71",
     "quote": "**No item in this dump carries any standards field.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/timeback-integration.md",
     "lines": "146-147",
     "quote": "Standards live in **`metadata`, never inline in `rawXml`.** A rawXml-only authoring shortcut produces a false-zero on pull (this caused a spurious \"zero standards\" FAIL pre-re-pull).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/timeback-integration.md",
     "lines": "144-145",
     "quote": "Human codes (`RI.3.1`, `CCSS.ELA-LITERACY.RI.3.1`) are accepted but **pick one convention** and normalize (`CCSS.ELA-LITERACY.` → bare code) so the reader doesn't double-count.",
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
   "reason": "The quotes are verbatim. The 'about threefold' figure appears only in a design case whose file name carries a person's name, with no stated measurement behind it, so I dropped it from the statement and set the kind to adopted rule. item-quality.md line 31 carries the untimed rule on its own; the speed exception rests on the name-bearing file.",
   "statement": "Do not put a timer on a comprehension item; time a task only where speed itself is what is being measured.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "31",
     "quote": "| 10 | **Untimed comprehension** — `time-dependent=\"false\"` on every item | per-item timer on a comprehension item |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "163",
     "quote": "time pressure ~triples the on-screen accuracy penalty and rewards rapid-guessing, which MAP penalizes; clocks only where speed is the construct",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 35,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Keep answer keys off the student's device and score on the server; never accept a correctness flag sent from the screen.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
     "lines": "88",
     "quote": "**No client-side scoring, ever** — render + report responses; the server scores. Never send renderer outcomes.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0060-incept-read-app-field-notebook.qmd",
     "lines": "39-41",
     "quote": "The client must **never** extract the answer key, compute score/mastery/XP/accuracy/advancement, send `rendererOutcomes`, persist scores, or hold a secret. QTI is fetched `view=student-before-answer`.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0024-beyond-alpharead-pr45-all-qti-types.qmd",
     "lines": "37-38",
     "quote": "**never trusts client-reported correctness**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 36,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (nine fixture items). The cross-check found the rule before it shipped ('would be silently wrong'), so I changed 'silently mis-scored' to 'would have'.",
   "statement": "Test scoring with every wrong response as well as the right one; a cross-check found an invented scoring rule that would have silently mis-scored two-part items.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/README.md",
     "lines": "308-310",
     "quote": "The committed evidence is `course-json-live-evidence/3`: it binds schema, validator, projector, source, and manifest digests and proves one correct response plus every per-response negative case for all nine fixture items.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0241-alpha-read-contract-investigation-and-packager-build-2026-06.qmd",
     "lines": "106-107",
     "quote": "`map_response` is not a real QTI template (invented), EBSR scoring would be silently wrong",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep",
   "reason": "The quotes are verbatim, and 40 and 60 words match the lint and the evaluator plan. It is related to truths 1 and 26 but sets length and misconception naming for corrective feedback.",
   "statement": "Keep corrective feedback short (aim near 40 words, never over 60), name the misconception it addresses, and never make it longer or harder than the instruction it corrects — at that point it has become new instruction.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "96-97",
     "quote": "This incorporates the Practice BrainLift boundary rule: if corrective feedback is longer or more complex than the original instruction, the item has crossed into new instruction.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "15",
     "quote": "| L4 | feedback word caps | feedback must carry a `misconception_id` and be <= 60 words (hard cap); 41-60 words emits a non-blocking warning (40 is the standard's target). |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "283",
     "quote": "Long feedback text is itself a failure for Grade 3.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 38,
   "verdict": "keep",
   "reason": "The quotes are verbatim and 1,234 matches. It adds option-specific feedback to truth 1.",
   "statement": "Write feedback for each wrong option specifically, tied to the error that option represents; generic or position-keyed feedback is a defect.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "64-65",
     "quote": "all 1,234 option-specific feedback routes have zero generic option-position IDs or truncated claim/recheck templates.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "125",
     "quote": "N4: misconception-coded distractors and misconception-named feedback.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "30",
     "quote": "every scored item has a `FEEDBACK` outcome + CORRECT/INCORRECT `qti-modal-feedback` (distractors→named misconception).",
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
   "verdict": "keep",
   "reason": "The quotes are verbatim and 0/542 matches.",
   "statement": "Prove feedback actually fires in the delivered player; feedback present in the item data can silently never show.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
     "lines": "31",
     "quote": "NN#5 feedback **silent 0/542**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "44",
     "quote": "`process-response` returns the authored `FEEDBACK` (CORRECT/INCORRECT), NOT the generic fallback; wrong answer fires corrective feedback. *(new — the silent-no-op trap; \"authored\" ≠ \"resolves\")*",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0019-alphalearn-qti-renderer.qmd",
     "lines": "133",
     "quote": "Content lacking these will render with NO feedback in strict mode — author accordingly or risk silent gaps.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 40,
   "verdict": "keep",
   "reason": "Both quotes are verbatim; the same rule appears on two platform pages.",
   "statement": "Give immediate feedback for simple facts and explained feedback, saying why, for concepts.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd",
     "lines": "38",
     "quote": "| **Feedback**        | Immediate for basic facts; elaborated (explaining why) for concepts.   |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "65",
     "quote": "| **Feedback** | Immediate for basic facts; elaborated (explaining why) for concepts. |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep",
   "reason": "The quotes are verbatim. It extends truth 1's 'only what is true' from wrong-answer feedback to welcome and progress screens.",
   "statement": "Feedback and progress screens must be true to what the student actually did: no fixed reply presented as a response to the answer, and no claim of an action the student did not take.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "70",
     "quote": "| F14 | major | The welcome beat overclaims contingent listening while still issuing a static, answer-independent recast (\"However you put it...\"). |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "71",
     "quote": "| F15 | major | The receipt screen asserts out-loud/self-done events that did not actually happen on the typed/floor interaction paths. |",
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
   "reason": "The quotes are verbatim. It is distinct from truth 40, which orders the lesson; this candidate requires the same operation and steps across the release.",
   "statement": "Modelled, guided and independent steps must practise the same operation with the same steps; a model that only reveals the answer, a guided step that is just a hint, or an independent task on a different skill breaks the release.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "12",
     "quote": "| L1 | triple-presence | model, guide, release atoms exist for the lesson's operation_id, with one identical, non-empty ordered step list. Catches the round-2 answer-reveal I-do (payload only the answer = empty steps). |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "280-281",
     "quote": "I-do/we-do/you-do is misapplied (answer reveal / hint / different skill)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "46",
     "quote": "Gradual release is one process at decreasing support: the I-do models *thinking*, the we-do walks the same steps with immediate feedback, the you-do releases the same skill",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 43,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The lint makes the platform's 'avoid bundling new skills' rule concrete.",
   "statement": "Introduce at most one new operation per lesson, and let review steps reuse only operations already taught, never smuggle in a new one.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "25",
     "quote": "4. **Design for cognitive load limits.** Keep granularity tight, reduce noise, avoid bundling multiple new skills in one lesson.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "17",
     "quote": "| L6 | one new operation per dose | every non-review atom carries exactly the lesson's one `operation_id`. Catches the round-2 skill-switching you-do (together with L1). |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/lesson-schema.md",
     "lines": "71-72",
     "quote": "(an undeclared new operation cannot be smuggled in as phase:\"review\").",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 44,
   "verdict": "keep",
   "reason": "The quotes are verbatim; the validator message is the joined Python string literal.",
   "statement": "A lesson may assume only knowledge that earlier lessons in the sequence actually taught; check each lesson's assumptions against what came before and treat a missing link as a failure, not a skip.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "16",
     "quote": "| L5 | spine check | `lesson.assumes` is a subset of the union of prior lessons' `adds`, in unit order. |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py",
     "lines": "592-593",
     "quote": "lesson '%s'%s assumes %s not added by any prior lesson in the unit (assumes[] must be a subset of prior lessons' adds[]).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py",
     "lines": "578",
     "quote": "# A missing lesson must fail here too; skipping it would make the spine check vacuous.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 45,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Any reference to earlier material ('as you saw last lesson') must be true in the actual sequence.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "123",
     "quote": "N2: relational-reference factuality. \"As you saw last lesson\" claims must be true against order.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "60",
     "quote": "`exposure_justification` is factually wrong against the lesson's own U1-L6 lineage.",
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
   "reason": "The quotes are verbatim. Truth 28 already says a check a student can skip is decoration. This candidate adds the 'Next-twice' exploit, the rule that an undeclared check counts as skippable, and banked-only progress so a refresh cannot open a gate. I kept it as evidence for truth 28.",
   "statement": "Every check must block progress until it is answered; a check that can be skipped by pressing Next twice, refreshing or tapping ahead is no check, and a step not declared blocking counts as skippable.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "14",
     "quote": "| L3 | every check blocking | any non-blocking atom is a failure (the \"Next-twice\" exploit; the round-2 hint-style we-do). M5 carve-out below. |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "75-76",
     "quote": "**`blocking` defaults to false:** an atom that does not declare itself blocking is treated as skippable (absence of a guarantee is not a guarantee).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0191-g3-book-lesson-anatomy.qmd",
     "lines": "155-157",
     "quote": "Records only what is BANKED, never half-done state, so a refresh cannot open a gate the child has not passed.",
     "verbatim": true
    }
   ],
   "against": "op-lint README lines 61-63 carve out one oral mode that 'never blocks progression' until its grading is calibrated.",
   "general": true,
   "duplicate_of": "28",
   "name_bearing_source": false
  },
  {
   "index": 47,
   "verdict": "keep",
   "reason": "The quotes are verbatim. It is related to truth 7 (ask after the part that answers) but concerns keeping that part visible.",
   "statement": "Keep the material visible whenever a step asks the student to cite, quote or find evidence in it, and show the part the question is actually about.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "13",
     "quote": "| L2 | passage visibility | `cites_text` implies `passage_visible` on every atom. |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "281-282",
     "quote": "evidence-writing hides the passage",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0191-g3-book-lesson-anatomy.qmd",
     "lines": "70-73",
     "quote": "A page's own passage wins over an earlier one — this was a real, fixed bug: the renderer used to pin whichever passage came last in the whole lesson and drop the page's own passage on the floor, which could show a different part of the story than the one a proof-question was asking about.",
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
   "reason": "The quotes are verbatim; both come from the same review response.",
   "statement": "Have students select the evidence before they paraphrase it or write about it.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "42",
     "quote": "5. evidence selection before paraphrase or written articulation;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "94",
     "quote": "evidence-first articulation",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 49,
   "verdict": "keep",
   "reason": "The quotes are verbatim. It adds what the worked example in truth 40 must contain.",
   "statement": "In the worked example, model the genuinely hard judgment on the visible material — including the tempting wrong alternative and why it is rejected — and then have the student do it cold.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "40",
     "quote": "3. I-do on the visible text, exposing the genuinely difficult judgment;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "78-79",
     "quote": "(I-do models the rejected hunter-to-prey alternative; You-do re-elicits cold with `attempt_first:true` and \"no hints before you try\" — canonical, not a leak;",
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
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim but is a one-line summary. I added the fuller list of the same review demands from kb-0174, which also says nothing goes on screen before it is thought aloud.",
   "statement": "Model a skill in a fixed order — say what to do, show it done, then check — with one thing for the student to look at.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "18",
     "quote": "modeling choreography (say → see it done → check, one attention target)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
     "lines": "61-63",
     "quote": "Scout says what he will do, then it is seen done (ideally silently), then the check; nothing on screen before it is thought aloud; feedback finishes before the next step renders; one attention target at a time; only the current sentence highlighted.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 51,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (5/2/1 → 3/2/3 → 1/2/5). 'So the scaffolds end on plain material' is not in the cited evidence, so I dropped it. I added the fuller demand from kb-0174 (fade per skill).",
   "statement": "Fade support for each skill by exposure across lessons, moving from mostly modelled to mostly independent work.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "18",
     "quote": "exposure-based scaffold fade (5/2/1 → 3/2/3 → 1/2/5)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "288-289",
     "quote": "use explicit instruction with worked examples and fading",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
     "lines": "72-73",
     "quote": "exposure-based fade progression per skill (heavy model 5/2/1 → shift 3/2/3 → hand-over 1/2/5)",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd line 30 records a held dispute: \"named inference routines as *fading scaffolds* retired on a stated condition\" versus scheduled recurring retrieval of the routine.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 52,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Every screen asks the student for a purposeful response; avoid long passive stretches, interleave quick checks into explanation and cut redundant prose.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "23",
     "quote": "each screen earns a purposeful response; knowledge building avoids redundant prose and interleaves quick checks",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "128",
     "quote": "N7: active-check cadence. No long passive segment without a non-bypassable check.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "68",
     "quote": "every screen needs meaningful student engagement; knowledge building should be focused and checked;",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd line 39: \"remove Scout's interjections at the top of each page. They take away from the reading flow.\" Added prompts can also break flow.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 53,
   "verdict": "keep",
   "reason": "The quotes are verbatim; both come from records of the same meeting.",
   "statement": "Every reread sends the student back to selected material for a stated purpose.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "23",
     "quote": "rereads return to selected text for a declared knowledge purpose.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "68",
     "quote": "targeted rereads serve the knowledge objective;",
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
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The rule came from a review request that was applied to one lesson; applying it to the team's own lessons was held pending a ruling. The spot-check measured the lessons, not an effect, so the kind is adopted rule rather than measured.",
   "statement": "Aim each understanding check at the detail the lesson's main idea hinges on, not at an incidental detail.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "49",
     "quote": "\"can this check about his mother never mentioning the brother as it's a key/crucial bit for the theme of betrayal\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "60-62",
     "quote": "Two L4 checks are incidental rather than thematic: p10 \"Who jumped first?\" (purpose: what the children must believe before they can fly) and p12 \"What happened to the lights of London?\" (purpose: how Peter makes Neverland sound).",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd lines 64-66: the fix was held on \"whether the 20.09 reading-checks-stay-retrieval ruling (checks stay literal) extends to requiring the literal check be about the hinge specifically.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 55,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Write questions for the specific material; do not turn a generic skill label into one question script used for every text.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "60",
     "quote": "Do not turn a generic taxonomy label into a universal question script.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "93",
     "quote": "bespoke questions",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/TOOLING.md",
     "lines": "53-55",
     "quote": "It does not judge whether a think-aloud is authentic, whether a question is text-bespoke, or whether teaching is effective.",
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
   "reason": "The quotes are verbatim.",
   "statement": "Freeze the course architecture and place the material before writing lessons; never author a lesson from a bare topic.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/curriculum-agent.md",
     "lines": "48",
     "quote": "Do not start lesson authoring from unresolved unit architecture.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "58",
     "quote": "Do not author from a bare topic or unplaced text.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "164",
     "quote": "start the clock only from frozen architecture/scope/acceptance inputs.",
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
   "reason": "The quotes are verbatim; three components matches.",
   "statement": "Build each lesson from its own lesson-level design, not only from general guidance; a lesson built from correct general guidance lacked three required components.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "59",
     "quote": "Promoted 2026-08-25 after G3-U1-L4 was built from the KB workbook + procedure HTML alone: both correct, both a tier too general, and the design doc mandated three components the lesson lacked entirely (the Component 6 cloze, the Magic Doors, the INFER step rail) plus a canonical video we do not hold.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0176-g3-peter-pan-pr-timeline.qmd",
     "lines": "22-24",
     "quote": "**\"named designs govern\"** made the four original Peter Pan lesson-design DOCX (`~/Downloads/5. Curriculum`, PP1-PP4) the build specification for L4-L7, not the sourcing portal's 17-chapter novel.",
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
   "verdict": "keep",
   "reason": "The quotes are verbatim. Truth 18 already says to teach and gloss the words that carry the knowledge. This candidate adds a per-word disposition ledger and a measured case of words that do not block understanding being deep-taught, so I kept it as evidence for truth 18.",
   "statement": "List the words that would block understanding and decide for each whether to pre-teach, gloss or leave it, deep-teaching only the words that actually block.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "52",
     "quote": "Vocabulary ledger: target word, blocking words, disposition, audio/definition requirement.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "59",
     "quote": "| F3 | major | \"producer\"/\"habitat\" are deep-taught as if they were blocking vocabulary (they aren't). |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "18",
   "name_bearing_source": false
  },
  {
   "index": 59,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (~60%, 60–63%, 5–15 of 100). 'Incidental exposure alone teaches little' conflicted with the doctrine's own incidental-vocabulary result under engineered recurrence. I narrowed it to a single meeting in ordinary reading and added that line as evidence.",
   "statement": "Teach key words with a definition plus use in context, and plan re-encounters across related texts; one meeting in ordinary reading, or a dictionary definition alone, teaches little.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "45",
     "quote": "Tier-2 vocabulary requires direct robust instruction plus engineered re-encounters; incidental context is an unreliable acquisition channel",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd",
     "lines": "56-57",
     "quote": "Vocabulary recipe: definitional + contextual, multiple encounters, morphology (~60% of meanings predictable), taught words chosen for generative value.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "58",
     "quote": "Only \\~5–15 of 100 unfamiliar words met in natural reading are learned; misdirective contexts teach approximately zero",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "60",
     "quote": "Sentences students write from dictionary definitions are unacceptable 60–63% of the time",
     "verbatim": true
    }
   ],
   "against": "The same doctrine reports that the largest effect in a coherent-text study was incidental vocabulary, with no meanings taught, when target words recurred about six times across the set (knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd line 56). Planned recurrence alone can teach a lot.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 60,
   "verdict": "keep",
   "reason": "The quotes are verbatim (~80/~50/~20). It is a secondary citation of a vocabulary-instruction book, with no DOI.",
   "statement": "Check whether a student knows a word by asking for an example or an explanation, not by self-report; far more students say they know a word than can explain it.",
   "kind": "external-research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "61",
     "quote": "Word knowledge is a continuum: \\~80% of students check a word as \"known,\" \\~50% can give an example, \\~20% can explain it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "21",
     "quote": "2. **Enforce mastery gates at ≥90% accuracy.** Do not advance students based on time, completion, or self-report.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 61,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Advance students only on demonstrated mastery on rigorous checks, never on time, completion or self-report, so that 'completed' means mastered.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "21",
     "quote": "2. **Enforce mastery gates at ≥90% accuracy.** Do not advance students based on time, completion, or self-report.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0026-evaluating-apps.qmd",
     "lines": "21",
     "quote": "| **Mastery truthfulness**       | \"Completed\" means mastered                         |",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0006-beyond-alpharead-source.qmd line 55: \"The **\\\"mastery\\\" metric (80% correct answers)** is accurately calculated on Dash.\" knowledge/kb-0007-ti-courseplans-repo.qmd line 123: \"**Staged 90% gates** — Band A advisory, blocking from Band B, final gate at course end (only ~17% reach 90% today).\" The bar and its enforcement vary.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 62,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The merge quote sits at lines 92-93, not 91-92. Truth 38 already says a check proves nothing until it catches a planted fault. This candidate applies that to mastery gates (drive a below-bar attempt) and adds two live courses whose threshold was null, so I kept it as evidence for truth 38.",
   "statement": "Prove that a mastery gate blocks a learner below the bar with a live attempt; a declared threshold can be missing or unenforced.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
     "lines": "37",
     "quote": "`masteryThreshold:90` declared in metadata, not enforced by an observable mechanism; lesson tests carry NO threshold;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "92-93",
     "quote": "`masteryThreshold` was `null` on both live courses (the 90% gate didn't actually block)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md",
     "lines": "44-45",
     "quote": "PROVE it with a play-through, don't assert a metadata field as \"enforced.\"",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "38",
   "name_bearing_source": false
  },
  {
   "index": 63,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (80%, correct × 3). The 'passive activity' and 'penalties for gaming' parts had no cited evidence, so I added the platform's lines for both. The 80% floor is the platform's number; I kept it in the evidence rather than the statement.",
   "statement": "Reward only verified learning: no points for passive activity or for low-accuracy work, and penalties rather than points for gaming.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "23",
     "quote": "No XP for passive activity until learning is verified through retrieval. No XP below 80% accuracy.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0030-xp-system.qmd",
     "lines": "50",
     "quote": "| Any                     | Gaming/cheating | Negative XP        |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0030-xp-system.qmd",
     "lines": "54",
     "quote": "**Warning:** No XP is awarded below 80% accuracy. This discourages students from speed-running content or guessing until correct.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "174",
     "quote": "Rewards for fake progress train students to optimize the reward system, not their knowledge. Motivation follows mastery, not the reverse.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0060-incept-read-app-field-notebook.qmd",
     "lines": "52-53",
     "quote": "The broker previously **fabricated** quiz XP (`correct × 3`, no 80% floor, not time-based",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 64,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Assume students will take any shortcut the reward allows — tanking placement, clicking through explanations, guessing until correct, pattern-matching on items — and design so the target thinking cannot be skipped.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "182-185",
     "quote": "Tanking placement tests to receive easier content Clicking through explanations without reading Guessing until correct Pattern matching on test items rather than learning concepts",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "94",
     "quote": "**Make the target cognitive process unavoidable.** If students can succeed via pattern matching, shallow guessing strategies, or memorizing repeated items, the app is gameable and its signals are untrustworthy.",
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
   "reason": "The quotes are verbatim.",
   "statement": "Choose examples so that only one rule fits them — contrastive examples, near-misses that differ only in the critical feature, non-examples — because a wrong rule students can infer from the examples is the instruction's fault.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "83",
     "quote": "If the learner can logically infer the wrong rule from the examples provided, the fault lies with the instruction, not the learner.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "87-88",
     "quote": "**Contrastive examples** that show what counts and what does not **Near-misses** that differ only in the critical feature",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "27",
     "quote": "5. **Make misconceptions hard to form.** Use clear examples, non-examples, and fast error correction.",
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
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. The source calls spacing and interleaving mechanisms (Tier 1) and warns that features are liabilities, so calling spacing a 'feature' misread it. I reworded the statement.",
   "statement": "No optimization — spacing, interleaving, multimedia or game elements — makes up for missing basics: unambiguous instruction, retrieval practice and mastery gating.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "77",
     "quote": "**Tip:** Tier 0 is binary. You either have faultless communication, retrieval practice, and mastery gating, or you do not. No amount of Tier 1 or 2 optimizations can compensate for a broken foundation. Features are liabilities; mechanisms are assets.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 67,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Practice must require recall, not only recognition, and review must be spaced and mixed across units rather than massed on one piece of material.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "29",
     "quote": "6. **Build in retrieval practice and spaced review.** Practice must require recall, not just recognition.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "45",
     "quote": "cross-unit **interleaved** review present (not massed single-passage); recall/production-format items present (not recognition-only).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd",
     "lines": "35-36",
     "quote": "| **Spacing**         | Distribute practice over time. Cramming creates temporary performance. | | **Interleaving**    | Mix problem types to prevent context-dependency.                       |",
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
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. I trimmed the doctrine quote to stop before a person's name inside it.",
   "statement": "Plan the sequence so key ideas and words recur across related materials; the curriculum itself is the first spaced-practice system, and separate spaced review covers only what is not reused.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "64",
     "quote": "\"use the curriculum to keep generative knowledge warm by use; use spaced practice for the residue.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "38",
     "quote": "**The text set IS the practice schedule.** Engineered recurrence across a coherent text set is simultaneously vocabulary instruction (DOK1-2), spaced retrieval",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "270-271",
     "quote": "the curriculum is the FIRST spaced-practice system.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 69,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. 'One at a time' is not in the source, so I dropped it. The graph also uses the confused pair to drive example selection.",
   "statement": "Teach easily confused concepts explicitly and interleave them once both are learned, using the pair to choose examples.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd",
     "lines": "42",
     "quote": "**Gateway discriminations** (taught explicitly, interleaved after both learned): narrator vs author; main idea vs supporting detail; fact vs author's claim/opinion",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd",
     "lines": "15",
     "quote": "near-neighbor discriminations driving example selection",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd",
     "lines": "36",
     "quote": "| **Interleaving**    | Mix problem types to prevent context-dependency.                       |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 70,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim; η²=.09 and η²=.32 match, and the DOI matches sources.qmd. The study is small (N=59) and exploratory, and one comprehension measure was null. I put those limits into the statement in place of a general transfer claim.",
   "statement": "Build knowledge through coherent sets of related texts on one topic; in one small study this built topic knowledge and vocabulary, but transfer to new texts stayed near the topic and one comprehension measure showed no gain.",
   "kind": "external-research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/README.md",
     "lines": "34-36",
     "quote": "What compounds is knowledge: reading conceptually coherent text sets measurably builds topic knowledge, accelerates incidental vocabulary acquisition, and transfers to comprehension of novel related texts",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/sources.qmd",
     "lines": "17",
     "quote": "DOI: 10.1007/s11145-016-9628-x",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "55",
     "quote": "Coherent-set readers gained 5.59 vs 2.63 concept idea-units (η²=.32) over six texts in three days",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "37",
     "quote": "knowledge transfer is near-domain at best (Cervetti η²=.09)",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/skills/reading-science/SKILL.md lines 40-41: \"(e.g. Cervetti: N=59, exploratory, comprehension-questions measure null;\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 71,
   "verdict": "keep",
   "reason": "The quotes are verbatim (~10 vs ~50 sessions). This is external research summarized in the store; the sources are listed in sources.qmd.",
   "statement": "Teach general strategies briefly and inside coherent content, then spend the time building knowledge; strategy gains saturate quickly, and strategies taught apart from content are not fully learned.",
   "kind": "external-research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "57",
     "quote": "Across eight quantitative reviews, \\~10 strategy-instruction sessions produce the same comprehension benefit as \\~50 — no dose-response",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "529",
     "quote": "\"Unless the strategies are closely linked with knowledge and understanding in a content area, students are unlikely to learn the strategies fully, may not perceive the strategies as valuable tools\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "535",
     "quote": "\"If comprehension strategies are taught with an array of content and a range of texts that are too wide, then students will not fully learn them.\"",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd line 499: \"Explicit instruction generates the immediate use of comprehension strategies, but there is less evidence that students continue to use the strategies in the classroom and outside of school after instruction ends\". Durability is weak either way.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 72,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The 'carry no content, sequence or prerequisites' part had no cited quote, so I added it from the same line, stopping before a person's name. The doctrine is grounded in reading standards and holds for skills-only standards elsewhere.",
   "statement": "Design the knowledge curriculum — domains, throughlines, sets of materials — first and check standards alignment afterwards; skills-only standards carry no content, sequence or prerequisites.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "21",
     "quote": "Skills-only reading standards (\"determine the central idea\") are architecturally unusable: they carry no content, no sequence, no prerequisites",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "21",
     "quote": "Therefore the knowledge curriculum — domains, throughlines, text sets — is the load-bearing design object, and standards alignment is a *check run afterward*.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "268-269",
     "quote": "standards mislead as teaching plans — assessments are the evidence authority;",
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
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. I added the graph's edge definition for soft links with a fluency threshold, which the statement used but did not cite. Note that the validator warns, rather than fails, on a conventional hard link.",
   "statement": "Type every prerequisite link — hard (logically required) or soft (eases learning, with a fluency threshold) — and record why it holds; only a hard link backed by more than convention may block a student, and do not invent prerequisite chains the domain lacks.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py",
     "lines": "616-617",
     "quote": "graph edge %s->%s carries no warrant (every typed edge must state WHY it holds: logical|empirical|conventional).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py",
     "lines": "620-621",
     "quote": "hard_prereq edge %s->%s rests on a conventional warrant; it cannot justify a hard instructional block without stronger evidence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd",
     "lines": "13",
     "quote": "the COMPREHENSION band is horizontal (knowledge-sequenced by design, cross-subject dependencies, no fabricated prereq chains).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd",
     "lines": "15",
     "quote": "`soft_prereq` \\= A eases B; carries a fluency\\_threshold, not binary (SPOV3)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 74,
   "verdict": "keep",
   "reason": "The quotes are verbatim (140/49). Both sources are drafts, so this is kept as an adopted design pattern, with the draft status in against. The reader's line numbers for that counter were 24-25; the quote sits at 25-26.",
   "statement": "Separate atomic knowledge statements from the composite tasks that combine them, and define the final integrated performance by exemplars and a rubric instead of decomposing it further.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0150-science-g6-atom-composite-ledger.qmd",
     "lines": "9",
     "quote": "separating 140 atomic knowledge statements from 49 composite performance tasks",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd",
     "lines": "65",
     "quote": "defined by exemplars+rubric, NOT decomposed further",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0150-science-g6-atom-composite-ledger.qmd lines 25-26: \"All 189 `Reviewer Comments` cells are blank: that records an absence of reviewer comments, not reviewer approval.\" The course graph is also a draft pending a ruling.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 75,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The source is an unreviewed draft, as against records.",
   "statement": "For each knowledge statement, record what is new compared with earlier grades and which earlier statement it builds on, and add a negative definition (what it is not) where a misconception is likely.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd",
     "lines": "41",
     "quote": "[Spiral review of G2 Unit 2, A3-A4 — what is new: \"atoms\" replaces \"tiny pieces/particles\"; formal term introduced per D1 3-5 band]",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd",
     "lines": "42",
     "quote": "[New — D1 Section 2.1 negative definition; required at Grade 3]",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "27",
     "quote": "5. **Make misconceptions hard to form.** Use clear examples, non-examples, and fast error correction.",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd line 27: \"Every `Reviewer Comments` cell is blank; the source contains no completed reviewer feedback,\" so the ledger is an unreviewed draft.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 76,
   "verdict": "keep",
   "reason": "The quotes are verbatim. It is related to truth 20 but concerns not introducing another subject's concepts too early.",
   "statement": "Check new material against later grades' curricula to catch concepts introduced too early, and do not let a text be the first place a student meets another subject's concept.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0150-science-g6-atom-composite-ledger.qmd",
     "lines": "20",
     "quote": "Use this ledger mainly to check whether G3-G5 materials introduce Grade 6 concepts too early.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "81",
     "quote": "As a general rule, avoid implicitly introducing scientific concepts that students may not have encountered. It is better to re-encounter ideas from earlier grades than for Alpha Read or Alpha Write to be the first place a student meets an idea.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
     "lines": "54",
     "quote": "no cross-grade science first introduction disguised as Reading background;",
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
   "reason": "The quotes are verbatim.",
   "statement": "When another subject's content appears, reinforce rather than redefine it — match its vocabulary, nuance and framing — and give it a new angle rather than repeating the same topic.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "36",
     "quote": "Where a topic has already been covered, the Read/Write lesson should be consistent with how it was framed in the subject app, including its vocabulary, level of nuance, and framing.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "31",
     "quote": "Avoid sitting squarely on top of an identical topic. The re-encounter should feel like a new angle rather than a repeat: use a different subtopic, example, lens, or question.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 78,
   "verdict": "keep",
   "reason": "The quote is verbatim.",
   "statement": "Write cross-subject material so it works whether or not the student has had the other subject's lesson yet.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "30",
     "quote": "Topics taught in the same grade are potentially acceptable, provided the Read/Write treatment works whether or not the substantive science or social studies lesson has happened yet.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 79,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The README quote begins on line 63, so I corrected its lines to 63-65.",
   "statement": "A curriculum map records what should have been taught, not what a student has learned; never treat a map row as proof of prior knowledge.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/README.md",
     "lines": "63-65",
     "quote": "Treat workbook rows as a candidate adult-facing vertical-coherence map, not approved student wording or proof that a student has already learned a concept.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0152-science-g8-atom-composite-ledger.qmd",
     "lines": "9",
     "quote": "not evidence that younger students learned these concepts",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0149-draft-grade-5-science-ledger.qmd",
     "lines": "10",
     "quote": "never assume the listed concepts were taught, mastered, reviewed, or approved for students.",
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
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The ledger quote sits at lines 26-27, not 25-26.",
   "statement": "Do not copy draft or adult-facing planning text straight into student-facing material without separate authoring and review.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
     "lines": "55",
     "quote": "no draft workbook sentence copied directly into child-facing prose without separate review.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0150-science-g6-atom-composite-ledger.qmd",
     "lines": "26-27",
     "quote": "Do not convert the content statements into student prose without a separate authoring and review process.",
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
   "reason": "The quotes are verbatim. The passage packet also lists 'no contested interpretation presented as settled fact' (science-passage-agent.md line 58).",
   "statement": "Do not present a contested interpretation as settled or a model as literal reality, and make clear whether a statement is an observation, an interpretation, a consensus or an opinion.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "58",
     "quote": "A passage should not present a matter as settled where that is unwarranted. Distinguishing fact, interpretation, and opinion is part of the discipline itself.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
     "lines": "53",
     "quote": "no model presented as literal reality;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "85",
     "quote": "The scientific process distinguishes observation, hypothesis, theory, consensus, measurement, and related categories; student writing should make clear which of these the student is doing.",
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
   "reason": "The quotes are verbatim. I rewrote the statement to drop the job role ('the course owner').",
   "statement": "Back every real-world claim with a recorded source of the strongest available kind (an official or primary source, or a reference chosen for the course); model memory, search snippets and blogs cannot verify a fact.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "119-121",
     "quote": "Record source title, publisher, direct URL, retrieval date, exact locator, bounded fact, scope boundary, and content digest when bytes are available. Search snippets, unsourced summaries, blogs, and model memory cannot support `PASS`.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "40",
     "quote": "Nonfiction passages should be factually accurate and traceable to reputable sources. A vivid but factually loose passage creates downstream work for the subject team and risks embedding misconceptions that are hard to undo.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "96",
     "quote": "every science-bearing Read/Write object must use reputable sources and pass",
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
   "reason": "The quotes are verbatim.",
   "statement": "Check each factual claim against its recorded source, not against what sounds plausible, looking for definitions that drop a category or qualifier, category mistakes, unsupported mechanisms, causal overclaims and intent given to impersonal processes.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "135-138",
     "quote": "test definitions for missing categories and qualifiers; test ontology/category mistakes, unsupported mechanisms, causal overclaims, and contradictions; flag teleology or conscious intent attributed to evolved traits or impersonal processes; compare the claim with the frozen source boundary, not with what sounds plausible.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "140-142",
     "quote": "Examples of blocking shapes include defining a broad category as only one subtype, calling a process a body part, treating an animal as a producer, or replacing a causal definition with \"most connected.\"",
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
   "reason": "The quotes are verbatim.",
   "statement": "Text-dependence and factual truth are separate checks: a question can require the material while the material itself is unsourced or wrong.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "267-269",
     "quote": "Anti-leak (kb-0064) means \"you must read the passage to answer\" — it does NOT mean the passage's own facts are sourced or true. A perfectly anti-leak item can sit on an unsourced machine-authored passage.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "186",
     "quote": "**Note:** you grade **anti-leak + G5 compliance**, not source truth.",
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
   "reason": "The quote is verbatim. There is one source: a narration voice chosen for exactly this reason. The rule is general.",
   "statement": "When a lesson mixes an invented teaching case with real evidence, make the two clearly distinguishable to the student.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "61-62",
     "quote": "its first unit mixes a made-up teaching case with real evidence and the two must be audibly distinguishable.",
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
   "reason": "The quotes are verbatim. It is related to truth 66 and candidate 2, but adds re-checking only changed items and carrying forward only unchanged passes.",
   "statement": "Never let the writer certify its own work: changed items are re-checked by a different checker from a different model family, and only unchanged passes carry forward.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "263-264",
     "quote": "Do not certify your own authored content. The author may fix findings; an independent reviewer must close them.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/README.md",
     "lines": "154-157",
     "quote": "`verify` replays the patch from the base, carries forward only digest-equivalent passing cases, requires fresh evidence for every changed semantic case, and forbids the repairer identity or model family from verifying its own work.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "65",
     "quote": "Do not use the authoring model as its own certifier.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 87,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (8,937; ~1,475; 0/8,937; 0.292). The spec quote starts on line 33. I added the AP effort's own summary entry, which records its headline 99% as a best-of-N plus cache exploit.",
   "statement": "Report a writer's first-attempt pass rate per item type, deduplicated by template; survivor counts after many samples, or cached best picks, hide low yield and template stamping.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/generator-output-spec.md",
     "lines": "33-36",
     "quote": "A total like \"8,937 passes\" is **best-of-N reborn** — the same crutch aptraining's \"served-99%\" turned out to be — when it counts re-samples and template clones: in the G5 intake **one EBSR template was stamped ~1,475× and 0/8,937 sequence/match items survive the strict grader.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "93",
     "quote": "aptraining's headline \"99%\" was a **build-time best-of-N + serve-from-cache exploit** (kb-0063; SCOREBOARD_99 \"NOT the model generating\"), and the raw K=1 model floored at mcq/mcq_set 0.292 while the stack masked it [M8].",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md",
     "lines": "28-29",
     "quote": "G5 intake gates on **first-attempt, per-template-deduplicated `raw_pass_rate` per type** — \"1 prompt → 1 sampled item → graded\", NOT \"cell has ≥20 survivors after N samples\".",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "47-48",
     "quote": "**The headline \"99% / served-99\" is NOT a model achievement.** SCOREBOARD_99 itself says the served numbers are **\"cache-backed… NOT the model generating\"** and **\"not a verified 99%.\"**",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md lines 260-262: \"**Inference-time generate-and-verify is legitimate for a PRODUCTION generator** — shipping best-of-K verified items is a fine way to build a bank. But it is **NOT a K=1 single-model claim.**\" A filtered bank is fine if it is reported as such.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 88,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (28%, 4 bugs, 0→0.77). I added the AP effort's own summary, which records the same four harness bugs and the DBQ truncation (0.55→1.0 at 6000 tokens).",
   "statement": "Validate the scoring harness before trusting its numbers, and record why each attempt failed, by cause; harness bugs can make a writer look stuck or make good items fail.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "76",
     "quote": "aptraining burned weeks \"stuck at 28%\" that were **4 harness bugs** (wrong field read `overall.score`, grader on wrong host, MCQ_SET mis-route 0→0.77, DBQ truncation at low max_tokens)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "76",
     "quote": "**Bucket failures by type** (gen-fail vs transport-5xx vs schema-fail), not one boolean",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "126-129",
     "quote": "The first grader run false-failed some MSQ/EBSR candidates because `_resolve_key` handled JSON-array keys but not comma-separated legacy strings such as `\"a, b\"` or `\"a,d\"`. The staged `anti_leak_grader.py` accepts both. `match` items still did not survive because the current checker is MCQ-style and does not model pair-key scoring.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "39-41",
     "quote": "the \"stuck at ~28%\" narrative was largely **measurement artifact** (wrong field read, grader on wrong host, MCQ_SET mis-route 0→0.77, DBQ truncation 0.55→1.0 at 6000 tok)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 89,
   "verdict": "keep",
   "reason": "The quotes are verbatim (0%, +0.018, AUC ~0.5, ≥0.80, −0.2).",
   "statement": "Before using a cheap heuristic as a gate or reward, measure whether it actually separates good items from bad.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "170-171",
     "quote": "**`cold_passage_bonus` fires 0% of the time** on the 163 verified items (near-useless on this genre); **`curriculum_penalty` separates leaky from clean by only +0.018** (AUC ~= 0.5).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "181-182",
     "quote": "Tier A+ (a cheap distilled passage-blind classifier, gated at AUC >= 0.80 before use)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd",
     "lines": "125-126",
     "quote": "**Component 2 — Curriculum penalty (new)** Score contribution: −0.2 if passage hits any curriculum fingerprint; 0.0 otherwise.",
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
   "reason": "The quotes are verbatim (30-char check).",
   "statement": "Recompute every property a writer reports about its own output — length, reading level, quoted spans, counts — before gating on it; a partial-substring 'verbatim' check passed paraphrases.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "95-99",
     "quote": "they trusted generator-asserted `word_count`/Lexile and a 30-char substring \"verbatim\" check (defeated by paraphrase). Our contract has the same shape. Action: independently recompute Lexile, word_count, hot-text/EBSR spans (NFKC exact-match against the tokenized passage), answer-checkability at intake; any self-reported field used as a gate is UNVERIFIED.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "168-169",
     "quote": "re-measures every agent-reported number independently rather than trusting it, and corrects two:",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd",
     "lines": "147",
     "quote": "fluency passages regenerated after a first pass leaked Tier-3 vocabulary;",
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
   "reason": "The quote is verbatim (+23pp). It is one second-hand result, so the statement now says to try examples first rather than that they fix format errors.",
   "statement": "Before retraining a writer to fix its output format, try worked examples of the format in its prompt.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "88",
     "quote": "Mirrors aptraining [F5]: **few-shot exemplars fixed MCQ_SET answer-balance with NO retrain (+23pp)** — try in-context format exemplars before reaching for SFT.",
     "verbatim": true
    }
   ],
   "against": "This is a single second-hand report from an earlier AP question-generation effort; that effort's summary entry (knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd) does not repeat the figure.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 92,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. I added the primary summary: preference pairs rebuilt on the true axis gave +9.7 points with no regression. The wall itself stayed, so the effect is real but modest.",
   "statement": "When choosing examples to train or tune a writer, choose them on the quality you actually want, confirmed by an independent judge, not on a convenient proxy score.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "94",
     "quote": "aptraining's MCQ_SET wall was a **mislabeled-preference-data** problem (pairs picked on the IB axis, never verified on the true `educational_accuracy` axis) [M3/M8] — fixing the *data labels* beat 2 SFT warm-starts (both regressed, [M6]).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "37-38",
     "quote": "the **v97 clean-eduacc-axis DPO** (68 pairs, mcq_set 0.194→0.292, **+9.7pp**, no regression)",
     "verbatim": true
    }
   ],
   "against": "The AP effort's summary still records its multi-question cell stuck at 0.292 against a 0.70 floor and calls 95% single-shot a structural wall (knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd lines 44 and 51). Relabelling helped but did not break the wall.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 93,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. I added the AP effort's finding that a 95% single-shot bar on one format was a structural wall (~52% cap), which is the case for setting the bar against a ceiling.",
   "statement": "Set a judged pass bar against the judge's own agreement ceiling and a chance baseline, not at a near-perfect target the judge itself cannot reach.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "78",
     "quote": "**Define the eval contract up front** (oracle ceiling, class-prior baseline, shortcut-learning guard) — aptraining [P8]. On any format where judge self-agreement is low, the bar is `ceiling − margin`, not 99%.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "44",
     "quote": "**MCQ_SET ≥95% single-shot is a credible structural wall (~52% cap).**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 94,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (100K). The 'predict where students will struggle instead' part had no cited evidence, so I added the store's line on prediction accuracy across three research groups. The predictor itself is not yet validated (line 84).",
   "statement": "Do not estimate a course's effect by simulating students with a model — simulated scores come from the model's pre-training and the imposed models — instead ask the model to predict where students will struggle, and check any prediction against real outcomes.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
     "lines": "74",
     "quote": "Running 100K simulated students yields **zero new information** — outputs are determined by the imposed math models + pre-training.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
     "lines": "76",
     "quote": "100K-LLM-agent AP simulator (AP-score-from-pre-training artefact problem)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
     "lines": "75",
     "quote": "Teacher-as-predictor instead reaches r ≈ 0.72–0.79 population-level prediction across three independent research groups",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
     "lines": "84",
     "quote": "no self-validation (outputs must be validated against real student outcomes — Phase 6).",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/HOTBUCKET.md lines 313-315: \"practice/thin-instruction shapes fail; only the full student-ready candidate passes the simulation. This is design evidence, not live child-outcome proof.\" Persona simulation is still used as a design stress test.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 95,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "A model's score on pedagogy-knowledge tests does not show that its generated material embodies that pedagogy; judge the material itself.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "35",
     "quote": "Knowing-that (answering pedagogy questions) and generating-aligned (producing content that embodies the pedagogy) are different capabilities; the gap is invisible to benchmarks and only measurable at the artifact level.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "256-257",
     "quote": "filed with its own caveat that benchmark PCK ≠ teaching ability",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "65",
     "quote": "REJECTS pedagogy-benchmark scores as teaching evidence.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 96,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (~78%, 79%). The review-traps quote runs to line 17, so I corrected its lines to 15-17. It is related to truth 43 but adds that design-time instructions alone did not prevent the defects.",
   "statement": "Run independent adversarial checks on every generated artifact before a student sees it; design-time instructions to the writer did not prevent systematic leaks or answer-position bias.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "23",
     "quote": "Generation systematically betrays declared pedagogy — \\~78% of raw generated reading items were answerable without the passage, correct answers sat at position A 79% of the time, and a dose that \"knew\" gradual release still leaked its item's answer — and design-time contracts alone demonstrably failed to prevent any of it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "15-17",
     "quote": "Each is the kind of defect that leaves every text/structural validator green — only a machine ear, a human eye, or an adversarial pass caught it.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 97,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Classify each item as a knowledge check or a transfer item before judging its overlap with the lesson: being answerable from taught content is correct for a knowledge check and a leak for a transfer item.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "36",
     "quote": "An in-lesson knowledge check answerable from explicitly-taught knowledge is legitimate (that's what checking taught knowledge means); the same overlap in a comprehension/transfer item is a leak. Mis-classifying the item makes the same text both correct and defective — it took five adversarial rounds to isolate this.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "73-75",
     "quote": "KCT1 (domain-knowledge recall) is ~0 **by design** — passage-independent items are exactly what the anti-leak filter removes; covering KCT1 needs a different item design (generation), not relaxed gating.",
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
   "reason": "The quotes are verbatim (420/420, 0/20 vs 20/20, 17/20, 119/120). The 'routes' in the experiment were model families.",
   "statement": "A teaching policy written into prompts that steers one model may not carry over to another model; qualify each model separately before relying on it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "110-114",
     "quote": "adjacent A-only A1b completed 420/420 valid rows and failed exact cross-route portability: worst route 0/20 against 20/20. OpenAI and Claude each had 0/20 robust clusters; DeepSeek had 17/20. **BOUNDED POSITIVE:** the post-hoc semantic-facet diagnostic was 119/120. Prompt-local steering is real, but exact execution, negative-control locality, and invariant preservation were not portable.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "130",
     "quote": "bank but questioned universal cross-model transfer and expected model-by-model qualification.",
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
   "reason": "The quotes are verbatim. The entry records the count pin moving from 187 to 186.",
   "statement": "Keep content changes as replayable edit operations and hash content files before and after any automated multi-agent work; telling an agent not to edit content does not stop it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "149",
     "quote": "**Root cause:** a prompt instruction is not a write guard — a fan-out's Bash has the same filesystem",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "152-155",
     "quote": "before any fan-out that touches harnesses/tests, record `md5 -q public/lesson-json/grade-3.json` (and any other content file); re-check it when every agent returns and treat any change as an incident (re-apply from saved ops files, never hand-patch). Keep every content mutation as an ops file under the batch record (`apply-ops.py`) so re-application is one idempotent command.",
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
   "reason": "The quote is verbatim; the source states it for triage.",
   "statement": "When building from source material, give every input an explicit disposition — used, merged, split or skipped with a reason — because silent drops are the most common failure.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/ingest-triage/SKILL.md",
     "lines": "22-23",
     "quote": "**Every input file gets a disposition line** in the final report — extracted, merged, split, pre-digested, skipped (with reason). Silent drops are the #1 triage failure.",
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
   "reason": "The quotes are verbatim.",
   "statement": "When summarising sources, never pad a thin source, take numbers, names and dates verbatim, and spot-check model-written summaries against their sources.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/ingest-batch/SKILL.md",
     "lines": "33-34",
     "quote": "**One source → one entry. No invented facts.** A thin source gets a short entry — never pad. Numbers, names, dates come from the source verbatim.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/ingest-batch/SKILL.md",
     "lines": "125-126",
     "quote": "Spot-check ONE entry per batch by reading it against its source: numbers, names, and dates must match. Fabrication found → fix from the source, and say so in the report.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/templates/entry.template.qmd",
     "lines": "15-17",
     "quote": "Keep every fact; fix obvious formatting; drop boilerplate and noise. Preserve code blocks, lists, tables, and numbers verbatim. Do not invent anything that is not in the source.",
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
   "reason": "The quotes are verbatim. The skill names SYNTHESIS.qmd, which is absent from the folder; the rule still stands.",
   "statement": "Any claim about research carries its source and locator together with the source's limits, and a source is read before it is cited, never cited second-hand.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/SKILL.md",
     "lines": "32-34",
     "quote": "**Cite, don't vibe.** Any externally visible claim about reading science must carry a source + locator from SYNTHESIS/DIGEST files. If it's not in the folder, don't imply the literature says it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/SKILL.md",
     "lines": "38-39",
     "quote": "**Don't cherry-pick.** SYNTHESIS.qmd has a \"What complicates knowledge-first\" section. If you cite the supporting evidence externally, know the limits listed there",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd",
     "lines": "79-80",
     "quote": "If an argument needs one of these directly, ingest it first (knowledge-ingest skill) rather than citing it second-hand.",
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
   "reason": "The quotes are verbatim. The PRIORITIES quote starts on line 81. I dropped the course-quality quote because its folder is named after a person; the two remaining files carry the rule.",
   "statement": "Research behind a design is not evidence that your implementation works; outcome claims need an outcome measurement of your own material.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd",
     "lines": "81-83",
     "quote": "this corpus grounds DESIGN, it does not prove OUR implementation works. Never cite it as evidence about our courses' outcomes.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "126",
     "quote": "Do not claim RIT/proven impact before a real linked/piloted outcome source exists.",
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
   "reason": "The quotes are verbatim (201, GET 200, 1,077, 100%, 40%). The plugin entry's rules were distilled from AP Bio, AP Chem and AP Micro builds.",
   "statement": "Use only item types proven to render and score in the real student player, and keep a fallback for the rest; formats that validate and upload can still show blank or be unanswerable.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd",
     "lines": "116-117",
     "quote": "**R3 — `match`, `hot-text`, `text-entry` render BLANK.** They push fine (201, valid QTI, GET 200) but the quiz body is empty — must be transformed to single-select choice.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "68-71",
     "quote": "a live probe found the PRODUCTION TimeBack G3 Reading course is **1,077 items, 100% `cardinality=single`, zero TE ever rendered**. Our G5 contract hard-requires all six formats + 40% TEI → we can fully certify a form that **physically cannot be delivered**.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0020-incept-timeback-plugin.qmd",
     "lines": "21",
     "quote": "items that return `200 OK` but render broken/empty in the student UI, silent data loss on updates, etc.",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0022-incept-team-sync-2026-06-17.qmd line 33: \"All-MCQ/MSQ is a fallback only.\" The team refused to restrict a course to the formats the player already supported.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 105,
   "verdict": "keep",
   "reason": "The quotes are verbatim (eleven clips).",
   "statement": "Validate with the same logic the delivery engine uses, not a looser stand-in; a substring check passed evidence spans the engine could never highlight, and file checks passed audio that no check ever opened.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "111-113",
     "quote": "**Root cause:** `validate-passage-refs` only proves the span text is a SUBSTRING of the passage; it does not run the engine's own unit-boundary logic (`unitsOf`/`partOfLine`), so a span that is textually valid but unit-misaligned passes the validator and silently fails the student experience.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
     "lines": "94-96",
     "quote": "**Eleven you-do aux clips were raw PCM saved under `.mp3` names** (`out.write_bytes(audio)` ran because the cutting shim had no `write_mp3`) — browser fired media errors on the first found reply; `validate-assets`, voice-provenance and voiceover-sync were all green because none of them opens the file.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 106,
   "verdict": "keep",
   "reason": "The quotes are verbatim. It is related to truth 46 but concerns which kind of proof covers looks and which covers interaction.",
   "statement": "Prove appearance with a rendered look and interaction with a live walk-through; a markup assertion proves neither, and a screenshot does not prove interaction.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "139-140",
     "quote": "Lesson: any shell/layout change gets a rendered look (screenshot or computed layout of the control) before the PR, not only a markup-presence assertion.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/app-package-agent.md",
     "lines": "46",
     "quote": "Stop if screenshots are being used as proof of interaction.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0193-g3-book-grade-agnostic-vs-specific-g9-checklist.qmd",
     "lines": "170-172",
     "quote": "a key-set diff alone misses mid-page beats (best-pick, a reread hold, a follow-up ask) — walk the live page with a Playwright driver per mechanism, not just diff JSON.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 107,
   "verdict": "keep",
   "reason": "The quotes are verbatim. It overlaps candidates 108-110 (single source of truth) but concerns where a fix goes.",
   "statement": "Fix content where it is authored and regenerate every derived copy; edits made to a deployed or rendered copy are overwritten by the next import or regeneration.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0060-incept-read-app-field-notebook.qmd",
     "lines": "74-75",
     "quote": "**Gotcha:** the allqtypes course is **re-imported on a schedule** → `primaryApp` edits may be reverted; needs to land in the upstream import source.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "44-46",
     "quote": "Upstream generation specifications are active content authorities. Include them in governed Course JSON extensions. A rendered lesson that silently fixes a bad specification does not close the upstream defect because regeneration can reintroduce it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/curriculum-agent.md",
     "lines": "31",
     "quote": "7. Regenerate all downstream graph and reviewer views; do not edit mirrors independently.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 108,
   "verdict": "keep",
   "reason": "The quotes are verbatim. Truth 42 already says to remake what was made under an old rule. This candidate adds marking dependents stale and rerunning every check on the new versions after an upstream failure, so I kept it as evidence for truth 42.",
   "statement": "When an upstream fact or specification fails, mark every dependent lesson, item, chart and feedback as stale, repair the source, regenerate, and rerun every check on the new versions.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "193-198",
     "quote": "When an upstream spec fails: mark dependents stale; repair the upstream object, not only rendered copies; regenerate descendants; rerun every named checker on the new hashes.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
     "lines": "34-35",
     "quote": "6. Propagate any upstream failure through every declared dependent lesson, item, chart, and feedback object.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "42",
   "name_bearing_source": false
  },
  {
   "index": 109,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The parameter file excludes RI.5.7 only from a single-passage generator, and the cited skeleton row is a two-text lesson, so those two lines alone do not show a conflict. The parameter file's 18-code list (line 78) against the skeleton's generator enum (line 208), which includes RL.5.7 and RI.5.7, does show one. The enum quote stops before a person's name.",
   "statement": "Keep each number, rule and setting in one canonical place that everything else points to or is generated from; parallel copies drift apart.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "100-103",
     "quote": "their biggest systemic failure is spec INCOHERENCE (scoring method, TEI floor, blueprint, item count specified ≠ across files; a wrong string reached machine-consumed gradebook fields). Our kb-0069 drift risk, concrete. Action: one canonical numbers block per course; all other docs POINT to it; a cheap CI consistency check.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/assessments/G5_PARAMETERS.md",
     "lines": "78",
     "quote": "18 codes after excluding RL.5.7 / RI.5.7 as not cold-text-assessable.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/COURSE_SKELETON.md",
     "lines": "208",
     "quote": "`RL.5.1, RL.5.2, RL.5.3, RL.5.4, RL.5.5, RL.5.6, RL.5.7, RL.5.9, RI.5.1, RI.5.2, RI.5.3, RI.5.5, RI.5.6, RI.5.7, RI.5.8, RI.5.9, L.5.4, L.5.5, L.5.6`",
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
   "reason": "The quotes are verbatim. It overlaps candidate 109 (one canonical place). The registry deletion was on an unpushed branch, so the fix is adopted, not proven.",
   "statement": "Derive structure from the content itself instead of keeping hand-maintained registries of it; registries went stale silently on a reshape, and a validator that keeps them in sync only patches the duplication.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "93-94",
     "quote": "The failure mode was NOT an error: evidence simply wrote a no-op and provenance came back empty, so nothing looked broken until a human noticed missing credit.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "96-98",
     "quote": "\"this is a bandaid, not the solution\" — it fails loud, which is strictly better than silence, but it leaves the duplication in place and adds a fourth thing to maintain. **Real fix:** delete the registry; derive ownership from the node's own shape",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0191-g3-book-lesson-anatomy.qmd",
     "lines": "32-36",
     "quote": "Reintroducing an author script that emits `grade-N.json` is explicitly forbidden (AGENTS.md): it happened once, and a unit's lesson-title summary disagreed with the lesson's own title because the emitted JSON had drifted from the hand-edited contract.",
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
   "reason": "The quotes are verbatim (745/52/13/56, 703/47/10, 576, 6 of 12).",
   "statement": "Check counts, versions and file references in documentation against the delivered files before trusting them; a reader who trusts a stale description plans against material that does not exist.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "498-499",
     "quote": "**Course truth (live):** 745 items / 52 tests / 13 units / 56 stimuli (`kb-0058`) — **diverges** from the manifest (`kb-0014`: 703/47/10) and the QTI pkg (`kb-0004`: 576). Confirm which is canonical.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/course-layout.md",
     "lines": "102-103",
     "quote": "These are honesty-discipline failures of the same family as content drift: a reviewer who trusts the README plans against a test that doesn't exist.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "118-119",
     "quote": "corrected a prior false claim (\"U4L1 through U4L9 complete\"): **only 6 of 12 built lessons have any audio at all.**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 112,
   "verdict": "keep",
   "reason": "The quotes are verbatim. I re-measured on disk: the manifest lists 23 files and the folder holds 20. The schema file and the two failing fixtures for rules L3 and L5 are missing, although the op-lint README still lists them. library/ holds 3 of the 6 sources that sources.qmd lists, and SYNTHESIS.qmd is absent, while the record still claims 271/271.",
   "statement": "Before relying on a check's recorded result, confirm the checker exists, still runs and still has the files it ran on; recorded passes and cited harnesses can outlive their files or never have existed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling-manifest.json",
     "lines": "11",
     "quote": "\"result\": \"PASS: 9 fixtures; all six rules exercised with failing cases\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/EXTRACTION_EVIDENCE.qmd",
     "lines": "32-34",
     "quote": "**Quote integrity:** 230/230 extracted quotes verified verbatim at extraction time (`verify_quotes.py --json claims.json`); **271/271** quoted spans verified in the rendered SYNTHESIS + DIGEST files",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "113-114",
     "quote": "no runnable blind solver existed in-repo at merge time (the \"Claude-strong harness\" referenced was a phantom;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 113,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (16 lines). The rule is one-way: a page may print words nobody reads aloud. 'Match sentence for sentence' overstated it.",
   "statement": "Never narrate words that are not printed on the screen (printed words may stay silent), because narration that paraphrased its own text drifted unnoticed while every other check passed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "153-156",
     "quote": "**never speak words it does not print** — a spoken line with no printed home highlights nothing and cannot be tapped to hear again. This was a real, fixed bug: two pages had drifted into a paraphrase of their own spoken script, 16 lines between them, while every other validator passed.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "129",
     "quote": "(the read-along rule — nothing may be spoken that is not printed, sentence for sentence);",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0027-learning-science.qmd line 47: \"Combine verbal and visual when both add value. Avoid redundancy.\" This is in tension with full redundancy between voice and print (see truth 53).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 114,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "When a narration clip is missing, show the text silently rather than falling back to a synthetic voice, and record why each deliberate silence exists.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "33-35",
     "quote": "(2) a missing clip is SILENCE with the caption text visible — never a `speechSynthesis` fallback; (3) dynamic strings (interpolated answers, live feedback) render as text bubbles only, never synthetic speech;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "40",
     "quote": "every silent node must say WHY",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 115,
   "verdict": "keep",
   "reason": "The quote is verbatim. It is related to truth 53 but concerns how captions are made and when they are required.",
   "statement": "Generate captions from the approved script and the measured clip, and give every video that gates progress a caption track.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "182-189",
     "quote": "captions are NEVER hand-written. `scripts/generate-video-captions.mjs` derives a WebVTT track from the authored `transcript[]` (the script a reviewer signed off) plus the clip's real measured duration via `ffprobe`, written next to the clip and pointed at by `captions_path`. `validate-contracts.mjs` fails a unit video with no caption track, because a unit video gates the hero pick, which gates lesson one — captions are the only way through for a child who cannot hear, not an accessibility nicety.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 116,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Set age-specific settings — voice, pace, tone — deliberately for each new grade; silently falling through to another grade's defaults produces plausible but wrong material.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "72-77",
     "quote": "**No grade-9 entry exists.** Without one, G9 clips would silently fall through to `DEFAULT_VOICES`/`DEFAULT_STYLE` = grade 4's child voice and storytime pace — \"silent and plausible,\" per this same file's own comment about the identical mistake almost shipping for Grade 5 (\"a ten-year-old reading about salinity gradients would have been read to as if this were a bedtime story\").",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0193-g3-book-grade-agnostic-vs-specific-g9-checklist.qmd",
     "lines": "25-28",
     "quote": "a G5 rebuild passed every content validator and its unit test, yet the live page silently broke, because `bookCompoundResume.ts`'s `frameBlankInput()` hard-coded `grade: 3`",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
     "lines": "68-69",
     "quote": "L4's three purpose lines re-voiced to Scout (were bare stubs with no `voice` field, so the generator fell through to the narrator).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 117,
   "verdict": "keep",
   "reason": "The quotes are verbatim; the second stops before people's names. It is related to truth 2 (one plain voice) but asks for a per-age-group register standard kept apart from mechanics.",
   "statement": "Write a tone and register standard for each age group as a content standard separate from the mechanics, and do not inherit another age group's tone.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0193-g3-book-grade-agnostic-vs-specific-g9-checklist.qmd",
     "lines": "122-127",
     "quote": "**Register/content differences are separate from mechanism differences.** The build spec's \"Register (Grade 5)\" section (no \"You did it!\", no medals/confetti, ≤40-word feedback, epistemic hedging allowed, more writing than G3, retell demands taught terms) is entirely a CONTENT authoring standard, not a code change — it lived in the page files' prose, never in the renderer.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0193-g3-book-grade-agnostic-vs-specific-g9-checklist.qmd",
     "lines": "134-136",
     "quote": "**Register/pedagogy standard first**, separate from mechanism: define a G9-appropriate voice/tone doc (the G5 build's §3 register rules are the template for this document's shape, not its content — G9 needs its own,",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 118,
   "verdict": "keep",
   "reason": "The quotes are verbatim; the dates match.",
   "statement": "When one instance of a defect turns up, search the whole course for the same pattern before calling it a one-off, and turn a recurring defect into a standing check for its class.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "27-28",
     "quote": "Once one instance is found, census ALL colon-openers in the grade JSON rather than assuming a one-off;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "78-79",
     "quote": "Voice defects repeated as one-off fixes for weeks (wrong/different voice on 2026-09-04 twice, 2026-09-07, 2026-09-21)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0211-peter-pan-reviewer-round-2708.qmd",
     "lines": "24",
     "quote": "a gameability sweep over all 31 L4+L5 MCQs found no other cross-form tell",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd lines 28-29: \"some renders do voice the header anyway, so check transcripts per case, don't blanket-assume.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 119,
   "verdict": "keep",
   "reason": "The quote is verbatim. It is close to truth 70's re-measuring, but its point is rerunning the whole suite after any fix.",
   "statement": "After any fix, rerun every check, not only the one aimed at the fix.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "101-103",
     "quote": "Run per lesson immediately after cutting, and run the FULL suite before commit, not just the targeted verifier — PR #240 shipped a listen-fix that passed every targeted check but broke `validate-voiceover-sync`.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 120,
   "verdict": "keep",
   "reason": "The quote is verbatim (31 of 123, 25%, 0.28s).",
   "statement": "When a check fires on a large, seemingly random share of items, suspect the check before the content.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "85-88",
     "quote": "an onset-audibility check flagged 31 of 123 clips \"WEAK ATTACK,\" all false, because it measured loudness from the universal 0.28s lead-in at t=0 instead of from the actually-detected speech onset — fixed by measuring from detected onset, not from t=0 (an onset detector firing on 25% of clips at random was itself evidence the check, not the audio, was broken).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 121,
   "verdict": "keep",
   "reason": "The quote is verbatim. Truth 38 already says a check that never fired proves nothing, and a 0/0 result is a case of that. I kept it as evidence for truth 38 because it names a new failure shape.",
   "statement": "Treat a check that found nothing to check (zero passes, zero failures) as broken, not passed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "185-186",
     "quote": "never read a 0/0 verdict as green — treat it as a harness bug until proven otherwise.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "38",
   "name_bearing_source": false
  },
  {
   "index": 122,
   "verdict": "keep",
   "reason": "The quotes are verbatim (v10.1 to v10.16).",
   "statement": "When a check fails falsely, fix the checker; never loosen the assertion to get a pass.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
     "lines": "112-114",
     "quote": "**Driver** (Playwright-based walker) evolved v10.1 through v10.16 across the campaign, each version fixing a false-negative in the driver itself (nested-rail host filtering, we_do adapter, popover-close timing, bold-text normalization, reset-detector logic) — never by loosening an assertion.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "135-136",
     "quote": "never loosen a pin.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 123,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Before blaming your change for a failure, rerun the same check on the unchanged baseline; a failure that reproduces there is inherited.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "54-57",
     "quote": "Classify every red before touching it: extract `origin/staging` to a scratch tree (`git archive origin/staging | tar -x -C /tmp/stg-<sha>`), symlink `node_modules`, run the same test — a red that reproduces there is inherited (register it, never fix it); a red only on the combination is ours.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
     "lines": "75-76",
     "quote": "**Claim: this branch adds no failure beyond staging's own inherited reds.**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 124,
   "verdict": "keep",
   "reason": "The quote is verbatim (81/81, >=15, 8, 79/81, 2). It is related to truth 45 (fix the rubric first).",
   "statement": "Trace where a checker's threshold came from before acting on its failures.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "136-139",
     "quote": "the auditor's `thin_banks`/`enforcement_broken` FAIL (81/81) traced to an arbitrary `>=15` bank-depth constant hardcoded in `audit_compliance.py` itself (circular — the spec just quotes the auditor); the real platform/publisher floor is 8. After correcting the bar, 79/81 banks pass; 2 genuinely fall below 8 (a real, small, named gap).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 125,
   "verdict": "keep",
   "reason": "The quotes are verbatim. It is related to truth 9 (unsure is never a pass) but concerns checks that never ran.",
   "statement": "A required check that has not run counts as not passed: report it as unverified, never as a pass, and state missing evidence rather than leave the line blank.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "63-64",
     "quote": "**`NEEDS_LLM_GRADE` (the blind solve not run) is a FAIL, not a pass.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/non-negotiables.md",
     "lines": "61",
     "quote": "No line may be left blank; absence of evidence is `UNVERIFIED`, not silence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/README.md",
     "lines": "283-284",
     "quote": "If no suitable check exists, the contribution stays pending and the missing check is stated in the PR. Agents must not invent a passing verdict.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 126,
   "verdict": "keep",
   "reason": "The quote is verbatim. It is related to truths 34 and 67 but concerns keeping the pass/fail gate deterministic.",
   "statement": "Keep model calls out of the pass/fail gate: freeze judged inputs with their evidence before the gate runs, so the same inputs always give the same verdict.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/README.md",
     "lines": "60",
     "quote": "Same `course_id` + same `COMPLIANCE.md` + same referenced artifacts → same verdict and exit code. No model calls in the gate path; any machine-judged input must already be frozen into the ledger with its evidence tag before the gate runs.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 127,
   "verdict": "keep",
   "reason": "The quotes are verbatim. It is related to truth 24 but adds that success codes and agent reports are not evidence.",
   "statement": "Count a change as done only when a check confirms it on the delivered state and the status quotes the exact field or line that proves it; success codes, 'looks fine' and an agent's report are not evidence.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "13-15",
     "quote": "\"done\" is what the **deterministic check confirms on live state**, never an agent's claim or an HTTP 200 — a PUT can return 200 yet silently revert. Re-read via GET / `process-response`.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/ingest-batch/SKILL.md",
     "lines": "25-26",
     "quote": "**Never trust a subagent's success claim.** Subagents have returned `wrote: true` for files that never landed.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/templates/COMPLIANCE.template.md",
     "lines": "32-33",
     "quote": "verbatim line/figure that proves the status. \"Looks fine\" is not evidence.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 128,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Fix flawed items in place or add new ones, citing the principle behind each fix; never pass a check by deleting hard items, and test every change against a frozen baseline of item ids.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "34",
     "quote": "item-count + per-lesson item-id set ≥ a frozen source baseline; no validated item dropped/replaced — fixes are in-place or pure-add. `--assert-no-cut` → `no_cut_ok:true`. *(new — the hard rule; without it \"compliance\" can be faked by deleting hard items)*",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md",
     "lines": "16-19",
     "quote": "**Never cut / drop / replace a question.** Every item passed validation — it is good content. The only allowed operation is **fix-in-place** (edit metadata / passage / rawXml / wiring of the SAME item) or **pure addition** (new items for spacing/forms). Restoring a validated original counts as a fix. **Every fix cites a knowledge_bot principle** (kb id) as its justification.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 129,
   "verdict": "keep",
   "reason": "The quotes are verbatim (five items, five entries).",
   "statement": "When fixing material, list the verified-correct neighbouring decisions not to touch so the fixes don't regress them, and keep refuted challenges on record.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "74-75",
     "quote": "Five \"do-not-touch\" items were explicitly called out so a later patch pass wouldn't regress a verified-correct decision while fixing an adjacent F-id",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "45-47",
     "quote": "**challenged and upheld** (an attack raised during the lens audit was refuted on re-verification — 5 such entries collected with file/line evidence as a diligence record, not noise).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 130,
   "verdict": "keep",
   "reason": "The quote is verbatim. The test account was recommended and the line was not crossed.",
   "statement": "Review the student view through a dedicated test account, never by impersonating a real student.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0241-alpha-read-contract-investigation-and-packager-build-2026-06.qmd",
     "lines": "121-124",
     "quote": "the only path to the real render is **Impersonate/View as Student**, which lists real student accounts -- **that line was not crossed**. Recommended safe resolution (not yet executed at this draft stage): provision a dedicated sandbox test-student account and impersonate that, never a real child.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 131,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (48 hours). The 'a pilot is not a course' line sits in a folder whose name carries a person's name, so the statement now rests on the delivery-control lines instead.",
   "statement": "Prove one complete, audit-clean slice of lessons through every check before producing the whole course, and let a missed slice move the date, never the bar.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "156",
     "quote": "48 hours for one audit-clean 6-7 lesson vertical slice",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "164-166",
     "quote": "Replace all priors at the 48-hour vertical-slice gate. A missed gate changes the date, never the quality bar.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 132,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The 'blocked for replication' line comes from a superseded checkpoint whose buckets were later closed. I added the AP course's own completion entry, which puts each gate at 0% and forbids averaging them into one score. I also reworded 'expert subject review'.",
   "statement": "Finishing authoring is not readiness: human academic review, source and rights review, accessibility, independent assessment certification and checks in the real delivery system are separate later gates, never averaged into one score.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "36-38",
     "quote": "**NEXT GATES:** named human academic/historical review, source-line and rights review, accessibility, independent assessment certification, and target-runtime import/render/scoring. These are later readiness gates, not missing lessons.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "48-50",
     "quote": "**APUSH:** nine-unit architecture and deterministic Unit 1 contracts pass, but the independent read says BLOCKED FOR REPLICATION on six concrete content, release, source, correction, rubric, and student-projection buckets.",
     "verbatim": true
    },
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
   "name_bearing_source": false
  },
  {
   "index": 133,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Keep three kinds of checks apart — content checks on the files, behaviour checks in the live player, claim checks on the package — and never let one stand in for another.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "52-53",
     "quote": "This boundary matters. InceptBench should not overclaim runtime behavior or package truth. It should get the artifact-checkable layer much stronger.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/TOOLING.md",
     "lines": "58-59",
     "quote": "Neither tool replaces item anti-leak certification, live student-seat verification, formal accessibility review, academics approval, or learner-outcome evidence.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 134,
   "verdict": "keep",
   "reason": "The quotes are verbatim (73/76).",
   "statement": "Item-level quality scores do not measure sequencing or knowledge-building; lessons judged weak as wholes can be made of items that pass.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "361-362",
     "quote": "clone-lessons run (IB 2.7.5): **73/76 lessons INFERIOR** at lesson level while items pass — never claim course-level IB; internal-only number.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "232-233",
     "quote": "It measures isolated question/lesson content but **not sequencing or pedagogy** → the eval framework is slated to grow to assess lesson sequencing + knowledge-building across units",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 135,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "A course teaches; it is not a series of practice tests — test at set points, and present test-practice products as practice, not instruction.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "227-229",
     "quote": "G3 course strategy is **teaching-based, not drill-based** — practice tests only at specific intervals;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "290-291",
     "quote": "MAP/practice apps must stay framed as practice/assessment, not instruction.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "50",
     "quote": "Assessment format is not instruction format (the marathon rule), and acquisition mastery is not durable mastery — they need different instruments",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 136,
   "verdict": "keep",
   "reason": "The quotes are verbatim. They are the digest's summaries of the report's claims on p.113 and p.115; the report's URL is in sources.qmd line 15.",
   "statement": "Do not let one assessment format become the definition of the skill; a single format washes back into shallow teaching, and no single assessment serves every purpose.",
   "kind": "external-research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "699",
     "quote": "**114. Defaulting to 'read a passage, answer a few multiple-choice questions' as the operational definition of comprehension gives teachers little incentive to teach toward a deeper, more accurate conception of the construct.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "759",
     "quote": "**124. No single assessment can satisfy all these requirements; the RFA instead calls for building an integrated system of multiple assessments serving different purposes (accountability, diagnosis, instruction-guidance) and different reader groups.**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 137,
   "verdict": "keep",
   "reason": "The quote is verbatim.",
   "statement": "Read outcome data by cause: low effort points to motivation, accuracy far too high or too low points to placement, and completion without later test gains points to the instruction.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0031-how-it-works.qmd",
     "lines": "136-138",
     "quote": "**Motivation issues** (low minutes, high waste, inconsistent effort): the problem is upstream of your content **Placement issues** (accuracy too high or too low): students are in the wrong place in the curriculum **Curriculum issues** (students complete content but scores don't improve): your instruction needs work",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 138,
   "verdict": "keep",
   "reason": "The quotes are verbatim; the platform sentence goes on to say the student 'only advances once mastery is demonstrated'.",
   "statement": "After a failed test, teach only what was missed and retest before the student advances.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0031-how-it-works.qmd",
     "lines": "156",
     "quote": "the platform analyzes which standards were missed and generates a **targeted remediation course** containing just the lessons needed to fill the specific gaps. The student completes the hole-filling content, retests, and",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0026-evaluating-apps.qmd",
     "lines": "24",
     "quote": "| **Hole-filling compatibility** | Targeted remediation is possible when gaps show up |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 139,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim (12.5%). The source puts completion mechanics before accuracy lifts, not before item quality. The rest is a design decision, so the kind is adopted rule.",
   "statement": "Measure how much of the intended work students actually complete, and when completion is very low, fix completion before working on accuracy gains.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
     "lines": "122",
     "quote": "2. **Dosage-first** — daily 25-min/25-XP doses lead; completion mechanics before accuracy lifts (cohort floor is 12.5%).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 140,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (64% -> 41%). The 'same difficulty, never identical, never harder' parts and the measured drop come only from a file whose name carries a person's name. The two packet files carry reteach-plus-parallel-check without it. I added the fuller quote from the same name-bearing line.",
   "statement": "After a wrong answer, diagnose, reteach a different way and retry on a parallel item of the same difficulty; never re-serve the identical item or hand over a harder one.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "57-58",
     "quote": "Remediation map with retry limits, alternate instruction, a new parallel check, and wheel-spinning escalation.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "44",
     "quote": "7. misconception-specific correction and a new parallel check where required.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "37",
     "quote": "Difficulty escalates after a miss; attempt-2 supporting-detail accuracy **64% -> 41%**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "165",
     "quote": "Not-yet (diagnose the miss -> reteach in a different modality -> retry on a parallel same-difficulty passage -> after 2 cycles escalate; never re-serve the identical item, never hand a harder item after failure)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 141,
   "verdict": "drop",
   "reason": "The quote is verbatim, but its only source is a file whose name carries a person's name, and it records one untested design choice. Another entry (knowledge/kb-0011-run6-amalgamation-v2-engine-output.qmd lines 115-117, an engine prediction for a synthetic student) predicts that switching word help off in a scored writing step costs a weak decoder mastery credit 'even with intact comprehension'. The rule as stated is not general: it depends on whether the support touches what is measured.",
   "statement": "Switch off supports such as word help during scored steps.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "165",
     "quote": "Word Assist boundary: click-any-word audio definition ON in dose steps 1–4, OFF in scored steps 5–6, in every band.",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/knowledge/kb-0011-run6-amalgamation-v2-engine-output.qmd lines 115-117: \"Dose step 5 (`atom_dose_step_5_short_writing_scored`) is word-assist OFF and scored, so a writing-emergent decoder loses mastery credit there even with intact comprehension.\"",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 142,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim (grade 11 -> grade 3) but comes from a file whose name carries a person's name. I added the feedback handoff, which keeps age fit as a human decision, and the grade-default trap is backed separately (candidate 116).",
   "statement": "Screen every generated text for age-appropriateness and sensitive content, and check the writer's grade or level setting before generating.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "165",
     "quote": "mandatory age-appropriateness/sensitive-content screen on every auto-generated passage; fix generator grade setting (was grade 11 -> grade 3)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/README.md",
     "lines": "98",
     "quote": "approve cultural treatment, age fit, specialist factual judgments, accessibility, and final course readiness;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 143,
   "verdict": "keep",
   "reason": "The quotes are verbatim (N≥200).",
   "statement": "Measure growth with tests given before and after the course and separate from it, and put scores on an external scale only through a dual-tested linking study (about 200 students, tails oversampled, link error reported), with scale scores blocked in code until then.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0016-timeback-alpharead-publishing-playbook.qmd",
     "lines": "62-65",
     "quote": "pre/post tests are assigned **separately from the course** and surface on the TimeBack UI dashboard as a pending test. **PowerPath is only for serving questions natively — not for pre/post gating.** Pilot: select a cohort, assign the test before + after the learning app to measure growth.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "59-61",
     "quote": "common-person (anchor-person) linking, **N≥200 dual-tested** (real MAP RIT + our-form score), tail oversampling, report link SE; dual-MAP preferred over STAAR-equate; RIT BLOCKED until the anchor holds.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "63-65",
     "quote": "**No-RIT-pre-pilot is enforced in CODE** — `engine/src/map_engine/scorer/report.py` hard-sets `rit_output=BLOCKED_PRE_PILOT`, gates RIT behind `PILOT_PHASE==\"post-pilot\"` AND non-null `LINK_COEFFICIENT_A/B`.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 144,
   "verdict": "keep",
   "reason": "The quote is verbatim (186.6 / 193.9 / 197.1). It is related to truth 24's 'label an estimate as one' but concerns borrowed cohort data.",
   "statement": "Mark borrowed data — another grade's norms or weak-skill findings — as a placeholder, never as measured data for the new group of students.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "277-279",
     "quote": "target the G3 weak-skills — compare/contrast, cause/effect, sequence — as a *marked placeholder*, explicitly flagged, never presented as measured G5 data); **G5 MAP norms** (do NOT reuse G3's 186.6 / 193.9 / 197.1);",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 145,
   "verdict": "keep",
   "reason": "The quotes are verbatim (800–820L, 830–1010L, 560L, +230–410L). The ~930 figure is in ITEM_INVENTORY.md line 22, with 0 items at the new grade's band (lines 23-24).",
   "statement": "Re-validate a writer when moving it to a new grade or difficulty level, and expect items not to carry over — what carries over is the scaffolding: schemas, format examples, error lists and blueprints.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "60",
     "quote": "**Lexile-band extrapolation is unproven at G5.** Today's templates top out at 800–820L. G5 needs **830–1010L** — *above everything the generator has ever produced*. EBSR already proves the model degrades at higher Lexile (couldn't clear EBSR above 560L); pushing the whole bank +230–410L is into untested territory.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/ITEM_INVENTORY.md",
     "lines": "34",
     "quote": "Up-leveling a G3 item means a new cold passage + new stem + new distractors + re-eval = a regeneration, not a reuse.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/ITEM_INVENTORY.md",
     "lines": "36",
     "quote": "### What IS reusable (the real \"don't reinvent\" win — scaffolding, not items)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 146,
   "verdict": "keep",
   "reason": "The quotes are verbatim (78/80).",
   "statement": "Check the depth-of-thinking mix a writer actually produces against the target; asked for a spread, a writer produced the middle level on almost every kept item.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/assessments/G5_PARAMETERS.md",
     "lines": "119",
     "quote": "**Honest reality flag (load-bearing):** the **proven G3 generator emitted DOK 2 on 78/80 kept items** (measured from form_a.jsonl + form_b.jsonl) — it does **not** reliably produce DOK 1 or DOK 3 even when the standard supports them.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/generator-output-spec.md",
     "lines": "47",
     "quote": "(honest flag: prompted generators tend to over-emit DOK-2; DOK-3 yield must be measured, not assumed).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 147,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The template quote ends on line 25. I reworded the statement to drop the role word 'author'.",
   "statement": "An exemption from an outcome requirement must be granted by someone other than whoever claims it, and must be replaced by another measured outcome, never simply waived.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/templates/COMPLIANCE.template.md",
     "lines": "22-25",
     "quote": "exemption is **granted by a reviewer, not claimed by the author**. To use it: (1) the README declares the slice; (2) **each** MAP-coupled row marked `N/A — engagement-primary (see README)` is **replaced by a measured engagement OUTCOME** (retention / completion-quality / session-depth, with a path-backed figure) — so the hatch *costs* an outcome rather than *waiving* one;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md",
     "lines": "24-26",
     "quote": "reviewer-granted, NOT author-declared; each nullified MAP row must be **replaced by a measured engagement OUTCOME** (retention / completion-quality) so \"engagement-primary\" costs an outcome rather than waiving one.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 148,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The course-quality status table sits in a folder whose name carries a person's name, so I cite the four status words from item-quality.md lines 5-6 instead.",
   "statement": "Tag every rule and claim with how it was verified — walked live, full census, single probe, enforced in code, or not yet verified — and report each requirement as pass, partial, unverified or fail.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd",
     "lines": "107-108",
     "quote": "Confidence tags: `[LIVE]` walked in the student app · `[CENSUS]` exhaustive content check · `[PROBE]` one live probe per format · `[CODE]` enforced in code+tests · `[OPEN]` not yet verified.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "5-6",
     "quote": "**Status legend:** `PASS / PARTIAL / FAIL / UNVERIFIED` per the repo rubric.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 149,
   "verdict": "keep",
   "reason": "The quotes are verbatim; these are records 2 and 3 of the obligations file.",
   "statement": "Make any scored selection of topics or materials transparent — factors, weights and totals a checker can recompute — with a recorded human override and its reason.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl",
     "lines": "2",
     "quote": "\"requirement\": \"Preserve the explicit topic scorecard and expose the inputs and weights so reviewers can inspect and challenge the result.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl",
     "lines": "3",
     "quote": "\"requirement\": \"Retain a visible human override path where a person can keep or reject a topic against the score with a recorded reason.\"",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl line 3: \"Human override is a governance control, not evidence that the selected topic is effective.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 150,
   "verdict": "keep",
   "reason": "The quotes are verbatim and carry no speaker. kb-0174 lines 66-68 list the same standardization demand in detail.",
   "statement": "Keep one interface across lessons — the same controls and component shapes — and vary the content, not the mechanics.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
     "lines": "22-23",
     "quote": "\"On all the other lessons, we have to follow the UI/UX to the tee — no variations at all.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "18",
     "quote": "UI standardization",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
     "lines": "82-83",
     "quote": "rule: our structure stays, his components look exactly like his",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 151,
   "verdict": "keep",
   "reason": "The quotes are verbatim. It adds keyboard and assistive-technology access, and text equivalents for diagrams, to truth 27.",
   "statement": "Every interaction must work by keyboard and assistive technology, and every diagram needs a text or table equivalent.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "370",
     "quote": "**Accessibility (#10) is now a hard LEGAL blocker** (drag-to-order + hot-text keyboard/AT; check how MAP implements).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "67",
     "quote": "| F11 | major | The diagram is not element-addressable and has no accessible table equivalent. |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/app-package-agent.md",
     "lines": "37",
     "quote": "Keyboard-operable and screen-reader-aware vocabulary and audio controls.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 152,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (137/772, five options). The scan measured the bank against a chosen cap, not an effect of the cap, so the kind is adopted rule.",
   "statement": "Cap how many options a young student must weigh at once.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "132-133",
     "quote": "flagged 137/772 items over a 5-option cognitive-load cap (mostly hot-text)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "140",
     "quote": "accessibility option-count caps;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 153,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. It is a ruling stating a concern, not an observed result, so I softened the causal 'disengages and skips'. It adds a criterion to truth 22's eye check.",
   "statement": "Pictures of people must not look machine-generated, so that a student does not dismiss the material as fake and skip it.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "137-138",
     "quote": "the human needs to look less AI generated... I never want a student to declare 'Fake AI video' and skip to the next.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 154,
   "verdict": "keep",
   "reason": "The quotes are verbatim. Truth 2 is about register, not narration voices. kb-0182 notes that the one grade using a single voice did so only because its audio had already shipped.",
   "statement": "Give the material being read and the teaching around it different, consistent voices, so students hear them as different things and each role sounds the same in every lesson.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "81-84",
     "quote": "coach (Scout, Puck) and narrator (the book reader, Leda) are deliberately DIFFERENT voices so a child hears \"the story\" and \"the teaching\" as distinct — mirrors the G3 HTML player this engine ports. One voice per role, consistent across pages",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "57-59",
     "quote": "\"the coach coaches, the book reader reads, and keeping the two voices distinct is how a student hears 'the story' and 'the teaching' as separate things.\"",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 155,
   "verdict": "keep",
   "reason": "The quotes are verbatim (400-460L, 480-540L, 560-600L).",
   "statement": "Start a course with material students can handle and raise difficulty in steps.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0057-incept-team-sync-2-2026-06-18.qmd",
     "lines": "45-46",
     "quote": "**Lexile start too hard** — course opens on \"vertebrates and invertebrates\"; start easier and calibrate up.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0014-course-structure-manifest.qmd",
     "lines": "33",
     "quote": "**A · Hook (400-460L)** → **B · Bridge (480-540L)** → **C · Transfer (560-600L)**.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 156,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Give every unit an explicit key understanding, its likely misconceptions and its links to other units, so the build-up of knowledge is visible.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "91-92",
     "quote": "add unit key understandings, conceptual cross-unit links, and misconception sets;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "281",
     "quote": "knowledge sequencing is not observable",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/curriculum-agent.md",
     "lines": "41",
     "quote": "Unit ledger showing key understanding, misconceptions, fiction/nonfiction role, and cross-unit use.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 157,
   "verdict": "keep",
   "reason": "The quote is verbatim.",
   "statement": "Show results openly to students, families and operators, tying each piece of work to the student, the content and the attempt; never hide poor performance.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "226",
     "quote": "The platform must be able to attribute work to student, content, and attempt. Results are surfaced to students, families, and operators. Apps cannot hide poor performance.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 158,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Judge material by how quickly students reach a verified outcome, not by time spent or completion; time measures presence, not learning.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0026-evaluating-apps.qmd",
     "lines": "23",
     "quote": "| **Efficiency**                 | Fewer hours to reach the same verified outcome     |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0030-xp-system.qmd",
     "lines": "19",
     "quote": "track **time** (which measures presence, not learning) or track **accuracy** (which ignores how much work was done).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 159,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "When a task promises 'all' of something or a range, check every member is present; a synthesis task must combine at least two earlier components, and a rubric must accept everything its own chart shows as valid.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "177-183",
     "quote": "expand ranges such as `L1-L7` and words such as `all` or `every` into canonical IDs; require `coverage_mode` to be `exhaustive`, `representative`, or `sampled`; treat explicit ranges and `all`/`every` as exhaustive; compare promised lessons, entities, operations, sources, chart rows, tasks, and rubric categories with what is actually present; require synthesis to coordinate at least two prior components rather than list isolated recalls; require chart and rubric closure: anything represented as valid must be accepted consistently.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "185-186",
     "quote": "Missing required entities, omitted operations, inconsistent row logic, or a rubric that rejects its own chart are `FAIL`.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 160,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim. The two rules come from different checks, and the second allows editing when the text is itself wrong, which may reconcile them. I restated the question with that condition. It is related to truth 23 (don't cut approved words).",
   "statement": "When a question and its material disagree (a missing word or a missing quotation), should the material or the question change? One rule edits the text to fit a vocabulary item; another forbids editing the text to fit a quotation unless the text itself is wrong.",
   "kind": "open-question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "171",
     "quote": "Never repair a missing quote by changing the passage unless the passage authority itself is wrong.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md",
     "lines": "46-47",
     "quote": "**Vocab word-not-in-passage (NN#5):** FIX by editing the PASSAGE — `PUT {QTI}/stimuli/{id}` to use the word in context. Never reword the stem to dodge it; never delete the item.",
     "verbatim": true
    }
   ],
   "against": "No ruling reconciling the two rules was found in scope.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 161,
   "verdict": "keep",
   "reason": "The quote is verbatim. It summarizes the curriculum-architecture doctrine, which ROUTER line 64 lists as an authority on staged source synthesis and sequence policy.",
   "statement": "Give the writer the sequencing policy explicitly, and combine several sources in stages rather than all in one pass.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "269-270",
     "quote": "never blend sources in one pass; supply the sequence policy to the model;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 162,
   "verdict": "keep",
   "reason": "The quotes are verbatim. 'Teacher' here is the name of a lesson-writing skill, not a job role.",
   "statement": "People supply the curriculum sequence; a lesson-writing model works from it and does not author it.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd",
     "lines": "69",
     "quote": "the Teacher *consumes* this graph; it does not author it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "70",
     "quote": "Load the candidate SKILL.md to author a G3 lesson (start from a course-graph unit spec, not ad hoc).",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/HOTBUCKET.md lines 219-220: \"the meeting report that the teacher now authors all curriculum/content conflicts with the verified human-supplied-graph contract and tier-NONE status\". A contrary claim was made in a meeting.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 163,
   "verdict": "keep",
   "reason": "The quotes are verbatim. The skill line comes from its list of things it does not do.",
   "statement": "A pass on a sample does not clear the unsampled rest of the course.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
     "lines": "65",
     "quote": "Do not approve the whole course from a sampled cohort.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "275",
     "quote": "convert `PASS` on a sampled cohort into a whole-course claim.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 164,
   "verdict": "keep",
   "reason": "The quotes are verbatim. It is related to truths 30 and 39 but concerns making the judge record its evidence before scoring.",
   "statement": "Make a judge write down the evidence it is scoring, and how it reached its answer, before it gives a score.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "65",
     "quote": "video script evaluator's quote-before-score `structure_audit` is a good adversarial pattern.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "146-147",
     "quote": "**Step 1 — Blind solve.** Attempt the item using only world knowledge and the options themselves. Write down the answer you reach and HOW.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 165,
   "verdict": "keep",
   "reason": "The quotes are verbatim. Truth 44 already keeps a quality call unjudged until a person has reviewed it. This candidate adds a per-item approval flag shown to persist, so I kept it as evidence for truth 44.",
   "statement": "Mark every machine-written item and text as not yet human-approved until a person signs off, and keep that flag on the item itself.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "65",
     "quote": "**Human content review** — machine-authored content (CCSS tags, feedback, recall/MAP items) `humanApproved=false` until a human signs off.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md",
     "lines": "55-56",
     "quote": "**`metadata.humanApproved` persists** (PUT False → GET False) → the human-review gate can live on the item. All machine-drafted edits stay `humanApproved=false` until a human signs off.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "44",
   "name_bearing_source": false
  },
  {
   "index": 166,
   "verdict": "keep-with-fix",
   "reason": "The quotes are verbatim (n=6, 5/6, 0.29→0.95, ~28%). The '0.29→0.95' figure is the same six-item trial, not a larger claim. The AP effort's provenance entry records it as a judge artifact that collapsed on the binding grader, while its summary calls confirmation pending. I restated the question accordingly and added both AP entries.",
   "statement": "Does grounding a question writer in real source texts raise item quality? A six-item trial looked strong under one judge, but on the binding grader the gain disappeared as a judge artifact, so it is unproven.",
   "kind": "open-question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "92",
     "quote": "it's the one mechanism aptraining found that broke a wall (n=6 smoke, 5/6 pass@0.85).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "53-54",
     "quote": "**The recent \"source-grounding breaks the wall\" win is smoke only** (n=6, Unit-1: 5/6 pass@0.85, mean 0.953 vs 0.29)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "24-25",
     "quote": "That **0.29→0.95** jump existed only under a **discredited Gemini judge**. On the **binding grader** it **collapsed to ~28%** (DBQ 0%, MCQ_SET 0%) and was logged as a **\"Gemini-judge artifact.\"**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "39-41",
     "quote": "(Real-source provenance is a *separate, UNPROVEN* lever: the aptraining \"0.29→0.95 via real passages\" result was **refuted** on the binding grader. Do not relabel machine-authored cold passages as \"real.\")",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g5-reading-generator-output-spec.md",
     "lines": "74",
     "quote": "**Source-grounding was the biggest real lever** (feed real stimuli, model writes the questions) — exactly the cold-passage/anti-leak standard in §3. Build the generator around it.",
     "verbatim": true
    }
   ],
   "against": "The same standard still has the writer write only questions from a genuine source where one exists (knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md lines 41-42: \"Where a genuine source exists, the model writes the questions, not the passage.\"). The practice survives while the claimed quality lift does not.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 167,
   "verdict": "keep",
   "reason": "The quotes are verbatim (nine fields, nine clips). 'Scout' is the coach character, not a person.",
   "statement": "Do not interrupt the reading of a text with voiced asides at the top of every page; they break the reading flow.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "39",
     "quote": "\"remove Scout's interjections at the top of each page. They take away from the reading flow.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "45-46",
     "quote": "nine `purpose` + `purpose_voiceover` fields deleted per lesson across L4-L7 + G5-U1-L1, nine clips retired,",
     "verbatim": true
    }
   ],
   "against": "knowledge_bot/HOTBUCKET.md line 92: \"rebuild reading purpose,\". An earlier review round asked for an explicit reading purpose, so the purpose must live somewhere less disruptive.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 168,
   "verdict": "keep",
   "reason": "The quote is verbatim (1,241; 28 RED/12 YELLOW; 15/8).",
   "statement": "When a failure count drops, check that no check was switched off; part of an apparent improvement came from disabled checks.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "193-195",
     "quote": "clean `origin/main` for G5 1,241 already fails 28 RED/12 YELLOW; the dirty tree's lower 15/8 result partly comes from disabled linter invariants, so both states are quarantined.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 169,
   "verdict": "keep",
   "reason": "The quotes are verbatim.",
   "statement": "Give every distractor a named error type from a fixed list, and validate that each wrong option carries one.",
   "kind": "adopted-rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "27",
     "quote": "| 6 | **Misconception-tagged distractors** — each wrong option maps to a named cluster: `schema_mis_mapping` / `strategy_substitution` / `inference_overreach` | distractors with no diagnostic intent |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "105-106",
     "quote": "Action: add a per-option enum validator (fail-and-retry) to our generator;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd",
     "lines": "132-133",
     "quote": "Every selected-response item carries **misconception-cluster tags** (A = strategy-substitution / B = schema-mismapping / C = inference-overreach).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 170,
   "verdict": "keep-with-fix",
   "reason": "The quote is verbatim. This is a research finding, not a project rule: the RAND digest quotes the result directly (claims 69-70, pp. 107-108; URL in sources.qmd line 15). I changed the kind to external research and added that evidence.",
   "statement": "Match how explicit and cohesive the text is to the reader's prior knowledge: highly cohesive texts help readers who know little about the topic but can lower deeper understanding for those who know a lot.",
   "kind": "external-research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd",
     "lines": "58-59",
     "quote": "The coherence x knowledge text-tuning interaction (high-coherence texts help low-knowledge readers; can under-stretch high-knowledge readers on deep measures).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "425",
     "quote": "\"For these readers, texts with high coherence consistently produced higher performance scores than texts with low coherence.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "431",
     "quote": "\"A coherent text base slightly enhanced recall, but actually lowered performance on tests that tapped the mental model.\"",
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
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "18",
   "quote": "scaffolding-question feedback (never the answer)",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "372",
   "quote": "hints-buttons **out**, scaffolding-on-2nd-attempt **in**",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "24",
   "quote": "hints follow an attempt;",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "68",
   "quote": "| F12 | major | The \"Dashed Line\" beat pre-teaches its own check on the same screen. |",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
   "lines": "63-64",
   "quote": "Silent branch on L4/L6 models a line from the story and asks its meaning (content-word overlap 1.00→0 on L4, 0.80→0 on L6; his L2 sits at 0.50)",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "98-99",
   "quote": "miss 1 -> level-1 criterion cue, miss 2 -> level-2 evidence frame, attempt 3 -> level-3 release (`released:true`, framed as help, never \"solo pass\")",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
   "lines": "74-76",
   "quote": "Passage-dependency is currently judged by LLM rubric and regex, not by an empirical passage-withheld solve. Red-team history says rubric passage-dependency can pass while blind probes solve the items trivially.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
   "lines": "74-75",
   "quote": "(passage withheld, model+version pinned, temp 0.3, **N=5, FAIL at k≥3/5**, per-format answer-space rules, `ablation_trials[]` persisted)",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/knowledge-[name]-additions/APPLY.md",
   "lines": "4-6",
   "quote": "the question-quality re-check material was **dropped** as redundant (the main generated set already passed InceptBench AND Opus — a different model family — so a further blind-solve gate adds nothing; the 4/11 leak finding was an 11-item seed bank, not the validated set).",
   "ok": false
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
   "lines": "77-78",
   "quote": "prior call was that re-checking IB+Opus-passed items is redundant — logged as corroboration, not re-pushed.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
   "lines": "154-156",
   "quote": "`PASS` requires one stable best answer/set and no material alternative. One credible competing answer is `NEEDS_HUMAN`; repeated support for two answers is `FAIL`. \"The intended answer is stronger\" does not repair a hard-scored item when another option also answers the question.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
   "lines": "66",
   "quote": "79% of correct answers in a generated course sat at option position A, and the correct option was systematically the longest",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
   "lines": "60-62",
   "quote": "classifies answers 5 ways (full/partial/off/brief/silent), 120 clips on the pinned course-TTS route, all Puck-stamped; the off-branch answer no longer sits last in every lesson.",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "180-182",
   "quote": "promotion review caught `r3-09` at 3/8 exact blind recoveries and 0.71875 mean partial accuracy; low model confidence had wrongly hidden those hits.",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
   "lines": "24-25",
   "quote": "`NEEDS_HUMAN`: evidence is missing, conflicting, inaccessible, malformed, or specialist judgment is genuinely required.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "72",
   "quote": "| F16 | major | The local evaluation fallback grades free responses by keyword overlap, and a porting note propagates that defect. |",
   "ok": true
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0050-timeback-events-api.qmd",
   "lines": "134",
   "quote": "repeated attempt numbers overwrite prior info",
   "ok": true
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
   "lines": "62",
   "quote": "Do not infer knowledge from one noisy response.",
   "ok": true
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0191-g3-book-lesson-anatomy.qmd",
   "lines": "150-152",
   "quote": "The step id is the page's own authored id, never its position (a position rots the moment the lesson's shape changes; five probes pinned to `?page=<n>` broke the day L1 grew an opening video).",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
   "lines": "163-164",
   "quote": "Treat lifecycle `quote-integrity` findings as blocking. A prompt that asks for a quotation requires one unique contiguous passage match after only Unicode, whitespace, and punctuation normalization.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
   "lines": "95-96",
   "quote": "they trusted generator-asserted `word_count`/Lexile and a 30-char substring \"verbatim\" check (defeated by paraphrase).",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "59",
   "quote": "| F3 | major | \"producer\"/\"habitat\" are deep-taught as if they were blocking vocabulary (they aren't). |",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
   "lines": "57-63",
   "quote": "a generated cover image duplicated a pinned character — 5 children shown instead of a pinned cast of 4. **Mechanism:** cast pinning inside a CAST block in the prompt is not enough; the model drifts on count once past roughly four figures, and pinning the count in only one place in the prompt doesn't anchor it. **Fix:** repeat the EXACT-N count inside the SCENE line itself (not just the CAST block), use explicit separation language, and enumerate individually for stubborn cases; EYEBALL every generated image before wiring it into `art.ts`.",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
   "lines": "171-173",
   "quote": "Segments are cut from one approved take with ffmpeg, never re-synthesized, so the voice a reviewer approved stays the voice a child hears even as new states are spliced in.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
   "lines": "95-98",
   "quote": "every text-side validator (voiceover-sync hashes, read-along marks, the walkers) can be green while the audio itself is wrong — a reviewer heard \"betrayal\" as \"trail\" because the /b/ onset sat at -84dB in the clip, and every text-side check passed.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "94-95",
   "quote": "**772/772 stimuli** had been flattened at publish time into one tagless `<p>` (titles welded onto bodies, e.g. \"PapyrusIn\"; \"surface.Passage 2\"; data tables collapsed)",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
   "lines": "31-32",
   "quote": "different snapshots; treat this live pull as current ground truth for the deployed course.",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "283",
   "quote": "Long feedback text is itself a failure for Grade 3.",
   "ok": true
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "370",
   "quote": "**Accessibility (#10) is now a hard LEGAL blocker** (drag-to-order + hot-text keyboard/AT; check how MAP implements).",
   "ok": false
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "188-190",
   "quote": "**PR 68 merged, but is not mandatory enforcement:** runnable tools and specs exist; no CI, publisher, or artifact-producing orchestration invokes them. The smallest defensible future gate needs persisted canonical lesson artifacts first; fixture-only CI would overstate enforcement.",
   "ok": false
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd",
   "lines": "77-78",
   "quote": "fail-closed (a lesson that won't validate is reported + excluded, never silently shipped).",
   "ok": false
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "142-143",
   "quote": "explicitly bars any LLM grader on the auto-score-to-100 path (feedback must be a deterministic function of the machine-scored response).",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
   "lines": "96-97",
   "quote": "Above the default case limit, an unscoped run refuses to proceed; split by changed cohort instead of paying for an incoherent sweep.",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/README.md",
   "lines": "60",
   "quote": "No model calls in the gate path; any machine-judged input must already be frozen into the ledger with its evidence tag before the gate runs.",
   "ok": false
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
   "lines": "150",
   "quote": "4. repeat with at least three option-aliased or shuffled views;",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "63",
   "quote": "| F7 | major | The Generate level (I09) is missing; oral/typed judges accept empty or content-blind answers. |",
   "ok": false
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "72",
   "quote": "| F16 | major | The local evaluation fallback grades free responses by keyword overlap, and a porting note propagates that defect. |",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
   "lines": "21-23",
   "quote": "The two **semantic** checks in section 5 -- think-aloud authenticity (reasoning trace vs answer reveal) and release-item operation classification -- are advisory until an LLM-judge calibration pass and are deliberately NOT implemented here.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
   "lines": "42-44",
   "quote": "One passing unit and one failing fixture per rule, including all three round-2 failure shapes. Every rule has at least one failing case -- the selftest asserts the exact expected failure-rule set per lesson and fails if any rule loses its failing fixture.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "30",
   "quote": "full validation, fixed-point index, and 152/152 mutation cases pass in a fresh tree;",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md",
   "lines": "32-34",
   "quote": "the G5 static dataset carries both an IB and an independent Opus score per pass-row — rank by max disagreement and send those to the passage-blind solver first; a ready-made, zero-cost leak-suspect signal.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/knowledge-[name]-additions/docs/standards/course-quality.qmd",
   "lines": "55",
   "quote": "generation trace including rejected attempts.",
   "ok": false
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
   "lines": "60",
   "quote": "An item is **certified** only when ALL hold, each with a **stored verdict** the `COMPLIANCE.md` reads:",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
   "lines": "59",
   "quote": "Do not model analysis before the learner encounters the text.",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
   "lines": "493",
   "quote": "\"Explicit instruction provides a clear explanation of the criterion task, encourages students to pay attention, activates prior knowledge, breaks the task into small steps, provides sufficient practice at every step\"",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/TOOLING.md",
   "lines": "10-11",
   "quote": "A green deterministic gate is not academic, accessibility, factual, or readiness approval.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0228-g3-listen-qa-transcript-receipts-2026-09-24.qmd",
   "lines": "21",
   "quote": "no human has heard the 120 branch clips,\" meaning these are machine transcripts, not human listens).",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
   "lines": "104-108",
   "quote": "reproduced twice in dev-server walks but **zero times in production-build walks** (journey-23-prod: 27/27 clean). Root cause: the two dev reproductions coincided with concurrent file writes inside the worktree (other agents editing harness files, or `npm run` steps writing caches) triggering a Next.js hot-reload remount — never reachable by a real student on Amplify. Rule added to the recipe: dev-server walks need an idle worktree; proofs that must be clean run against the production build.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
   "lines": "36",
   "quote": "**Instruction quality — 3/5, CANNOT VERIFY from pull.** Pull is assessment-only; the instructional dose (hook→teach→guided→read→CFU→check) lives in PowerPath, not OneRoster.",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "313-315",
   "quote": "practice/thin-instruction shapes fail; only the full student-ready candidate passes the simulation. This is design evidence, not live child-outcome proof.",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
   "lines": "74",
   "quote": "Running 100K simulated students yields **zero new information** — outputs are determined by the imposed math models + pre-training.",
   "ok": false
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
   "lines": "120",
   "quote": "| High in-app accuracy, low test scores | In-app tasks are not testing transfer |",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/knowledge-[name]-additions/docs/standards/course-quality.qmd",
   "lines": "61",
   "quote": "A fully green build gate proves the course is well-built. It does not prove the course works. Every gate row above is satisfiable from metadata and structure, so \"done\" and \"moves outcomes\" are decoupled unless an outcome measure is added.",
   "ok": false
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md",
   "lines": "22",
   "quote": "Until it exists, \"certified\" ≠ \"works\";",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
   "lines": "84",
   "quote": "**Mastery now requires COLD / unseen-passage transfer** — the fix for \"in-app high, MAP flat.\"",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
   "lines": "38",
   "quote": "**ZERO CCSS standards** across all 745 items (RL/RI/L.3.x absent from every rawXml + metadata). Format coverage excellent (all 6 MAP formats), but no alignment ⇒ can't map to MAP skills, can't feed CASE, blocks Level-2.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
   "lines": "29-31",
   "quote": "frame `rows[].audio_path` review clips have no `audio_of` sha256, so a text edit (e.g. a definition rewording) leaves the clip silently stale with nothing in the validator suite able to detect it",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0176-g3-peter-pan-pr-timeline.qmd",
   "lines": "53",
   "quote": "Every deploy was proven by **hashing the served file**, never by a 200 response",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/source-map.json",
   "lines": "5",
   "quote": "\"ai_use\": \"Resolve source IDs here; verify SHA-256 before treating archived bytes or KB entries as the reviewed input.\"",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0026-evaluating-apps.qmd",
   "lines": "26",
   "quote": "If an app performs well on engagement but poorly on externally validated outcomes, the closed loop forces the conversation back to instruction, mastery, and signal integrity.",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
   "lines": "547",
   "quote": "\"the most predictive statistical models show that engagement is a mediator of the effects of instruction on reading achievement\"",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
   "lines": "151-153",
   "quote": "a page may print words nobody reads aloud (question stems are deliberately silent per R-AUD-6), but it may **never speak words it does not print**",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd",
   "lines": "47",
   "quote": "| **Multimedia**   | Combine verbal and visual when both add value. Avoid redundancy.                  |",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
   "lines": "63-64",
   "quote": "Silent branch on L4/L6 models a line from the story and asks its meaning",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
   "lines": "92",
   "quote": "Feed the model real/cold G5-band stimuli and let it write **only the questions**; don't have it invent the passage from nothing.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
   "lines": "39-41",
   "quote": "(Real-source provenance is a *separate, UNPROVEN* lever: the aptraining \"0.29→0.95 via real passages\" result was **refuted** on the binding grader.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
   "lines": "76",
   "quote": "Today 51% of attempts are an opaque `generated_item:null` — **instrument *why* each one died** (topic-reject vs format-fail vs truncation) before tuning",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "168-169",
   "quote": "re-measures every agent-reported number independently rather than trusting it, and corrects two:",
   "ok": true
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "163-164",
   "quote": "(input never contains the passage or key; `topic_seed` is audited to tell the generator WHAT to write, never the answer).",
   "ok": false
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md",
   "lines": "40-41",
   "quote": "**These are two different course-ids.** Fix: rebuild the g3 `COMPLIANCE.md` from PR #3's `rex-v2-compliance-comparison.qmd` (the real rex-clone-v2 eval)",
   "ok": true
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
   "lines": "31",
   "quote": "8 content bugs (mostly dangling-visual)",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
   "lines": "93",
   "quote": "(Our regenerate-until-pass loop is itself a soft best-of-N; report raw first-attempt yield separately.)",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
   "lines": "271-272",
   "quote": "**The INDEPENDENT-audit rate is the real metric**, not the in-loop self-grade (it is biased generous — it green-lit the item it later rates).",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
   "lines": "214-215",
   "quote": "**The in-loop self-grade is NOT the headline metric.** It is a filter. The real metric is an INDEPENDENT audit by a fresh grader (or human) that did not participate in the loop,",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
   "lines": "63-65",
   "quote": "**No-RIT-pre-pilot is enforced in CODE** — `engine/src/map_engine/scorer/report.py` hard-sets `rit_output=BLOCKED_PRE_PILOT`, gates RIT behind `PILOT_PHASE==\"post-pilot\"` AND non-null `LINK_COEFFICIENT_A/B`.",
   "ok": true
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
   "lines": "34-35",
   "quote": "6. Propagate any upstream failure through every declared dependent lesson, item, chart, and feedback object.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
   "lines": "101-103",
   "quote": "run the FULL suite before commit, not just the targeted verifier — PR #240 shipped a listen-fix that passed every targeted check but broke `validate-voiceover-sync`.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
   "lines": "115-116",
   "quote": "**\"Changes-first, then one walk\" discipline** (memory `changes-first-then-one-walk`) started formally at tick 30",
   "ok": true
  }
 ]
}
```
