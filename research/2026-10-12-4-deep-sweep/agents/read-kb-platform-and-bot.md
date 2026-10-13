# read:kb-platform-and-bot

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "kb-platform-and-bot",
 "coverage": {
  "read": [
   "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
   "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
   "~/Projects/grade3-reading/knowledge_bot/MAP.md",
   "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
   "knowledge/ entries tagged timeback/qti/oneroster/caliper/sdk/alpharead/audio/course-renderer/atom-composite-ledger, read in full: kb-0003, 0004, 0006, 0007, 0008, 0009, 0013, 0014, 0016, 0018, 0019, 0020, 0021, 0022, 0024, 0025, 0026, 0027, 0028, 0029, 0030, 0031, 0032, 0033, 0034, 0039, 0046 (head), 0048 (head), 0056, 0057, 0058, 0060, 0072, 0079, 0082, 0090 (key sections), 0093, 0137, 0176 (body), 0182, 0191, 0193, 0194, 0199, 0200, 0211, 0222, 0227 (sections 1-2), 0228, 0230, 0235, 0237, 0241",
   "knowledge/ API/SDK reference entries searched by keyword for learning content (no learning rules beyond platform mechanics): kb-0035, 0036, 0037, 0040, 0041, 0042, 0043, 0044, 0045, 0047, 0049, 0050, 0051, 0052, 0053, 0054, 0055",
   "knowledge/ atom-composite ledgers: kb-0144, 0146, 0147, 0148, 0149 (summaries, evidence-boundary headers, sample rows), plus kb-0150 and kb-0152 headers (titled atom-composite-ledger)",
   "handoffs/2026-07-10-sonnet-ingest-handoff.md, handoffs/g5-reading-generator-output-spec.md, handoffs/[name]-g5-generator-execution-plan.md",
   "handoffs/g3-reading-v2-feedback-2026-07-16/: README.md, curriculum-agent.md, science-passage-agent.md, lesson-instruction-agent.md, assessment-item-agent.md, app-package-agent.md, execution-sequence.md, TOOLING.md, tooling-manifest.json, source-map.json (head), validate_handoff.py (header), feedback-obligations.jsonl (first 3 records only)",
   "handoffs/.../tooling/ti-courseplans-2169d1f/: op-lint README.md, lesson-schema.md, fixtures (listed; one opened), op_lint.py (docstrings + selftest), skills/course-content-integrity/SKILL.md, content_integrity.py (header), docs/standards/course-json/README.md, course_validate.py (rule comments/messages), course_lifecycle.py (header)",
   "pr-proposals/ti-courseplans-standards/: PR_PROPOSAL.md, AUDIT_ACTIONS.md, knowledge-[name]-additions/APPLY.md, knowledge-[name]-additions/docs/standards/course-quality.qmd",
   "pr-proposals/.../staged/docs/standards/: README.md, non-negotiables.md, item-quality.md, assessment-design.md, generator-output-spec.md, course-layout.md, timeback-integration.md, templates/COMPLIANCE.template.md",
   "pr-proposals/.../staged/courses/: g2, g3, g4, g7-science, hs-civics COMPLIANCE.md; g5-reading analysis/GENERATOR_ASSESSMENT.md, ITEM_INVENTORY.md, COURSE_SKELETON.md (grep), assessments/G5_PARAMETERS.md (grep), assessments/GENERATOR_OUTPUT_SPEC.md (grep), generator/G5_GENERATOR.md, generator/anti_leak_grader.py (header), generator/passage_blind_verdicts.json, generator/README_FOR_[name].md, llm/LLM_SPEC.qmd",
   "skills/reading-science/: SKILL.md, README.md, PRIORITIES.qmd, sources.qmd, EXTRACTION_EVIDENCE.qmd, verify_quotes.py (header), applied/README.qmd, applied/teaching-comprehension-insights-brainlift.qmd, applied/g3-course-graph.qmd, DIGEST-rand-mr1465-2002.qmd (ch.4 + appendix B sections), DIGEST-cervetti-wright-hwang-2016.qmd (limitations grep only)",
   "skills/timeback-app-state/SKILL.md (VERIFY checklist, snapshot routine, G3 specifics, gotchas), skills/timeback-course-fix/SKILL.md, skills/ingest-triage/SKILL.md, skills/ingest-batch/SKILL.md (hard rules, verification step), skills/reading-kb/kb.sh (header)",
   "templates/entry.template.qmd"
  ],
  "skipped": [
   ".env and .env.bak-* files (secrets; forbidden)",
   "kb-0017-timeback-credentials-access.qmd (credentials file, tagged sensitive)",
   "kb-0012 and kb-0038 beyond their summaries (access/onboarding status; organisational, no learning content)",
   "feedback-obligations.jsonl beyond 3 records, seed_bank.json, claims.json, timeback-roundtrip evidence/example JSON (data dumps)",
   "skills/reading-science/library/ full texts (copyrighted, author-name paths; digests and the applied BrainLift used instead)",
   "DIGEST-willingham-lovette-2014, DIGEST-hennessy-*, DIGEST-singh-eduqwen-2026 (author-name paths; their claims are carried by the non-name-bearing Insights BrainLift and PRIORITIES)",
   "course_import.py, course_project.py, course_lifecycle.py, content_integrity.py bodies (code beyond headers/rule text)",
   "skills/reading-kb/install.sh (script)",
   "INDEX.md, README.md, AGENTS.md, inbox/, _archive/, scripts/, .kb-index/, search-sources.txt, ai-usage file (outside the named scope)",
   "Untagged knowledge entries (kb-0010, 0015, 0063 aptraining, 0080, 0081, 0083, 0096, 0164 and others; other directions); kb-0224 was opened only to confirm what one kb-0227 number measures",
   "kb-0145 and kb-0151 (tagged atoms-composites/curriculum-ledger, not atom-composite-ledger)"
  ],
  "notes": "Measured during this audit (directory listings vs records): the pinned op-lint/Course-JSON tooling manifest lists 23 files with a recorded selftest 'PASS: 9 fixtures', but the folder holds 20 files (fail-l3-hint-style-we-do.json, fail-l5-spine-gap.json and schema/course.schema.json are absent), so the recorded pass cannot be reproduced; reading-science SKILL.md and README.md route to SYNTHESIS.qmd, which is absent, and library/ holds 3 of the 6 sources that sources.qmd lists while EXTRACTION_EVIDENCE still reports 271/271 verified quotes; PR_PROPOSAL.md says 25 staged files including honesty.md and SEED_BANK_REPORT.md, which are absent though several staged docs link honesty.md; the staged g3 COMPLIANCE.md headline says '4 PASS' while its rows show 3; COURSE_SKELETON.md assigns RI.5.7/RL.5.7 that G5_PARAMETERS.md excludes. Folder timestamps (Aug 13 13:50) match the 2026-08-13 consolidation/iCloud eviction recorded in HOTBUCKET line 17. Conflicts surfaced as open questions: two-part item scoring (partial credit vs both parts), where to centre test difficulty, three vs four options, whether to change the text or the question when they disagree, whether source-grounding lifts generated item quality. A counter-decision (APPLY.md dropping the blind-solve gate as redundant) is recorded against later leak measurements. AP-related material in scope: the aptraining lessons quoted in the G5 generator assessment/spec (best-of-N + cache inflation, harness bugs, proxy-picked preference data, few-shot exemplars, judge ceiling, source grounding), the 100K-agent AP simulator warning, AP Bio/Chem/Micro publishing gotchas behind the QTI plugin, APUSH readiness gates in HOTBUCKET, and EduBridge AP-readiness endpoints (platform API only, no learning rule). Platform (TimeBack) concept pages are the delivery platform's published rules that the project adopted as its bar, so they are labelled adopted rule. Quotes spanning lines are joined with single spaces; leading list/blockquote markers are dropped."
 },
 "candidates": [
  {
   "statement": "A high score from a general quality judge does not show an item is sound; items it rated perfect still leaked their answers, so whether the material is needed has to be checked separately.",
   "kind": "measured",
   "found_by": "A quality judge running on the same model family as the writer rated answer-leaking items 1.0; the first different-family blind solve on a bank it had passed found 4 of 11 leaks; a generated question scored 1.0 while being 100% blind-solvable.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "9-10",
     "quote": "**InceptBench ≥0.9 is necessary, not sufficient.** IB grades *instructional* quality — it scored **answer-leaking items 1.0**. So a clean IB score does **not** mean an item is sound."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md",
     "lines": "9-10",
     "quote": "**Result: 4/11 CONFIRMED leaks, 8/11 answerable-blind, only 3/11 cleanly passage-dependent → a 36%-leaky bank that IB had passed.**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd",
     "lines": "114-115",
     "quote": "Observed failure (DAPO epoch 0): model generated `\"What is the primary function of chlorophyll?\"` from a photosynthesis passage. IB score: 1.0. Blind-solve rate: 100%."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/knowledge-[name]-additions/APPLY.md lines 4-6: \"the question-quality re-check material was **dropped** as redundant (the main generated set already passed InceptBench AND Opus — a different model family — so a further blind-solve gate adds nothing; the 4/11 leak finding was an 11-item seed bank, not the validated set).\"",
   "adds_to_existing": [
    5,
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A writer optimized against a structural-quality score alone converges on well-formed questions that can be answered without the material, so text-dependence has to be part of what it is scored on.",
   "kind": "measured",
   "found_by": "In reinforcement tuning, a generator's reward plateaued while it produced structurally valid questions that a blind solver answered every time; the follow-up directive was to optimize the course, not the item.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd",
     "lines": "115-116",
     "quote": "Reward plateau at ~0.14 confirmed the model had converged to structurally-valid leaked questions."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd",
     "lines": "118",
     "quote": "The two quality dimensions are orthogonal. Both must be in the reward signal."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "102-104",
     "quote": "the correction is \"optimize the course, not the item\" — a course where every item scores IB 1.0 but 90% is blind-solvable is a failed course"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd lines 186-188: \"reward inversion/Goodhart (a reworded canonical leak scored higher than a genuine requires-reading item under the shipped code)\" — the heuristic added to fix this could itself be gamed.",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check items with a judge from a different model family than the writer; a same-family judge shares the writer's blind spots and passed leaking items.",
   "kind": "measured",
   "found_by": "The item writer and the quality judge ran on the same model family; the judge passed leaking items until a different-family blind solve exposed them.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/generator-output-spec.md",
     "lines": "27-29",
     "quote": "IB grades *instructional* quality (it scored answer-leaking items 1.0) **and IB itself grades via the same model family as the generator**, so a same-family judge cannot catch leakage. The different-family check is mandatory."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "26",
     "quote": "So **generator and judge are the same model family** — a built-in proxy-gaming hazard (the spec's §8 / §3 anti-leak warning, and exactly aptraining's failure mode)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0090-fable5-plan-traces-2026-07-09.qmd",
     "lines": "131",
     "quote": "a lane cannot certify its own items;"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd lines 188-189: \"single-family blind-solve confound (every label comes from one solver family; no two-family agreement had been measured;\" — one other family may still not be enough.",
   "adds_to_existing": [
    66,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "The blind solver's strength sets the bar: use a strong solver and count an item clean only if solvers from more than one model family all fail it without the material.",
   "kind": "measured",
   "found_by": "Re-gating a weak solver's 'clean' set with a strong solver left 21% standing; a two-family union re-gate found 334 of 353 supposedly safe items leaky, uniformly across difficulty bands.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "67-69",
     "quote": "showed the weak gpt-4o-mini gate had over-credited items — of v1's 95 re-gated \"clean\" items, only **20 (21%) survived**; **75 leaked** under the strong solver."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "127-129",
     "quote": "union-of-detection (clean only if BOTH fail to recover). Binding result: 334/353 leaky (94.6%), only **19 genuinely clean**; leak was uniform across all three Lexile bands (93-95%), i.e. systemic to how these items were authored, not band-specific."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md lines 320-322: \"the old `claude-fable-5` blind-solver was over-strict in the wrong way and inflated blind accuracy; `claude-haiku-4-5` re-baselined 10 MCQs to clean by returning `UNKNOWN` on true passage-dependent items.\" — a solver can also err the other way, so it needs calibration.",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Let the blind solver answer 'unknown', and count any correct blind answer as a leak whatever confidence the solver reports.",
   "kind": "measured",
   "found_by": "A promotion review found an item recovered blind 3 of 8 times that had been hidden because the solver reported low confidence; separately, a solver that would not abstain inflated blind accuracy until one that could return UNKNOWN re-baselined the set.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "180-182",
     "quote": "promotion review caught `r3-09` at 3/8 exact blind recoveries and 0.71875 mean partial accuracy; low model confidence had wrongly hidden those hits."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "320-322",
     "quote": "the old `claude-fable-5` blind-solver was over-strict in the wrong way and inflated blind accuracy; `claude-haiku-4-5` re-baselined 10 MCQs to clean by returning `UNKNOWN` on true passage-dependent items. Use this for blind-solver calibration."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Accept a question that depends on the material only if it is answered correctly with the material and fails without it, and compare blind accuracy against chance.",
   "kind": "adopted rule",
   "found_by": "The generation recipe accepted items only after a with-material control plus a cross-family blind failure; rejected items were recovered far above chance, which is how kept items were shown to need the text.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "305-306",
     "quote": "The key rule: accept only after with-passage control plus cross-family blind failure; this is generation/gating evidence, not SME approval or TimeBack publish proof."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "64-65",
     "quote": "Rejected items recovered far above chance (sequence 58% vs. 3% blind; hot-text 79% vs. 14%; match 86% vs. 41%), which is the evidence the kept 97 require the passage."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Material that retells a well-known case or encyclopedic fact lets questions be answered from general knowledge, so base text-dependent questions on specific, unfamiliar content such as a particular decision, stance, reversal or causal chain.",
   "kind": "measured",
   "found_by": "A course skeleton was only a third fillable because items leaked; item regeneration was abandoned once encyclopedic passages were found to be the cause; blind solvers answered items that mirrored a famous story, while invented names blocked world knowledge.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "37-38",
     "quote": "regeneration was abandoned — the root cause is passage design (encyclopedic passages), not item quality."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd",
     "lines": "50-52",
     "quote": "4 encyclopedic passage types to **avoid**: curriculum-fact, headline-figure, biography, generic-process 6 cold passage types to **use**: decision-reaction, argument-stance, obscure-consequence, surprising-reversal, specific-comparison, causal-chain The passage-necessity test: \"Could a student who studied this topic but did NOT read this passage answer correctly?\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/passage_blind_verdicts.json",
     "lines": "90",
     "quote": "General-knowledge leak (trophic cascade): the item mirrors the well-known Yellowstone wolf"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd line 29: \"Topics taught in an earlier grade are always fair game for re-encounter, even though we may not know the student's actual grade in social studies or science.\" — familiar topics are wanted for teaching material; the rule bites on transfer and blind-checked items.",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure blind-solve leakage per item format: raw single-choice items leaked almost entirely, while formats that make the student locate, order or sort evidence in the material leaked far less, though no format is leak-proof by design.",
   "kind": "measured",
   "found_by": "A cross-family anti-leak gate recorded blind recovery per format across a candidate pool and again after a passage-design fix.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "35-36",
     "quote": "because the anti-leak gate scored MCQ 97% / MSQ 100% / EBSR 80% blind-recovered (reject) vs. hot-text 24% / sequence 42% / match 0% (pass)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "105-106",
     "quote": "Measured leak by type: MCQ 99.5%, MSQ 100%, hot-text/sequence/match/EBSR ~0.56% after the 06-24 passage-design fix."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0090-fable5-plan-traces-2026-07-09.qmd lines 132 and 134: \"selected response is not inherently leaky, but raw selected-response items often are;\" and \"hot-text and sequence formats need extra suspicion because renderer/protocol and guessability issues can masquerade as content quality.\"",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Matching items resist guessing when the pairing is fixed by the material (who said it, which part of the text, or 'not mentioned') rather than by a common association, and when extra targets stop the last pair being found by elimination.",
   "kind": "adopted rule",
   "found_by": "Generation retrospectives found attribution-style matching the reliable design; a 3×3 equal-sided match left an elimination cue; an intake review asked for decoy targets.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0090-fable5-plan-traces-2026-07-09.qmd",
     "lines": "133",
     "quote": "match designs work when they force source/POV attribution, which-half attribution, or not-mentioned discrimination;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "48-49",
     "quote": "**Match** — ≥3 text-grounded pairs (note: 3×3 equal-sides has a minor elimination cue — prefer a 4th distractor category where the generator supports it)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "79-80",
     "quote": "The correct pairing must be fixed by the passage, NOT by a canonical real-world association."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd lines 132-133: \"192 match items announcing a decoy bucket\" was itself flagged — announcing the decoy is a cue.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Key a question to a relationship the material asserts, and make an inference question need two or more sentences together; a key that is one retrievable fact is easy to leak.",
   "kind": "adopted rule",
   "found_by": "The anti-leak generation harness was rewritten after blind solves showed single-fact keys and single-sentence inferences were recoverable.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "48-51",
     "quote": "prefer keys that hinge on a **relationship the passage asserts** (a cause the text names, a contrast the text draws, an inference the text licenses) rather than a lone retrievable noun — denser passages make relational keys both natural and harder to leak."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "53-54",
     "quote": "For inference/theme items, quote the two-or-more sentences whose combination licenses the inference (no single-sentence lift)."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd lines 64-66: \"whether the 20.09 reading-checks-stay-retrieval ruling (checks stay literal) extends to requiring the literal check be about the hinge specifically.\" — some in-lesson checks are deliberately literal retrieval.",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build each distractor from a real detail of the material with one element swapped, so rejecting it means returning to a specific sentence; absurd or filler options give the key away by elimination.",
   "kind": "adopted rule",
   "found_by": "A lesson audit found distractors that were self-declared filler; the item standard names 'one obvious right answer plus throwaways' as a fail.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "55-59",
     "quote": "**Near-neighbour distractors.** Distractors are built from *real passage details*, with the wrong actor / stage / effect / cause / claim swapped in. No distractor may be absurd or eliminable by world knowledge alone. (Absurd distractors leak the key by elimination.) At G5, a near-neighbour distractor should require *returning to a specific sentence to reject* — that is the bar."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "69",
     "quote": "| F13 | major | Chunk-stop distractors are self-declared filler, not real near-neighbour traps. |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "26",
     "quote": "| 5 | **Near-neighbour distractors** — plausible, text-adjacent, not obvious-eliminable | one-obvious-right + 3 throwaways |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Where a common-knowledge answer exists, make it a wrong option so a student who has not read the material is pulled toward it.",
   "kind": "adopted rule",
   "found_by": "Blind graders treated a key that matched the textbook default as a general-knowledge leak; the harness turned that default into a deliberate trap.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "60-62",
     "quote": "**Bait the blind solver.** When a world-knowledge default exists, make it a *wrong* option (a \"live trap\"). This actively *punishes* the non-reader rather than merely failing to help them."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "149",
     "quote": "if the key matches the textbook default, treat that as a GK leak.)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "The correct option must not stand out as the longest, most specific, most hedged or only grammatical choice; check option-length parity item by item and across the course.",
   "kind": "measured",
   "found_by": "A census of a generated course found the correct option systematically the longest (and at position A 79% of the time); evaluators had no length-parity check.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "66",
     "quote": "79% of correct answers in a generated course sat at option position A, and the correct option was systematically the longest"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "65-66",
     "quote": "**No surface tells.** Length- and structure-match the contending options. The key must NOT be the longest, the most specific, the most hedged, or the only grammatical fit."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "101-102",
     "quote": "The evaluators do not check the \"correct answer is longest\" tell. Build per-item and per-course length-parity census over correct vs distractor options."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A question must not define, cue or restate its own answer: no defined word part, no word shared with the key, no restated target inference.",
   "kind": "measured",
   "found_by": "In the first blind solve, the confirmed leaks were stem giveaways; the item standard lists a defined prefix in the stem as a fail; the evaluator gap list adds keyword-match answerability.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "24",
     "quote": "| 3 | **No answer giveaway in the stem** — no pre-defined affix/definition, no cue words | `\"the prefix 're-' means 'again'…\"` (answerable without reading) |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/passage_blind_verdicts.json",
     "lines": "137",
     "quote": "Stem giveaway + option self-evidence: the stem restates the full target inference"
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
   "statement": "In a two-part claim-and-evidence item, the evidence part must not restate or mirror the first part, and the first part must stand on its own instead of leaning on the second.",
   "kind": "measured",
   "found_by": "Sampled two-part items were all blind-solvable because the evidence part restated the claim part; the same root cause had been measured in an earlier course.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "67",
     "quote": "6 of 6 sampled two-part evidence items were blind-solvable, with Part B restating Part A — the same root cause measured at 33% gameable in G3"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "158-159",
     "quote": "For MSQ, all defensible answers must be keyed. For EBSR, Part B needs one uniquely strongest evidence choice and must not reveal Part A."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "74-75",
     "quote": "**Do not lean on Part B to rescue a GK-solvable Part A** — strengthen Part A independently."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Should a two-part claim-and-evidence item give partial credit (first part right earns some credit, both parts earn full credit) or require both parts? The project's documents point both ways.",
   "kind": "open question",
   "found_by": "A review of an external test's keys found partial-credit scoring and warned that binary scoring biases ability estimates, while the delivery scorer and the item standard require both parts.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "85-86",
     "quote": "**EBSR/Composite = PARTIAL CREDIT (0/1/2)** — `MAP_COHERENCE_SHERLOCK_REPORT.md` (Sherlock-verified vs NWEA keys; Part A alone=1, both=2, Part A wrong=0). Their own MLEF scorer is binary → biases ability."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0024-beyond-alpharead-pr45-all-qti-types.qmd",
     "lines": "36-37",
     "quote": "**EBSR requires both parts**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "46",
     "quote": "**EBSR** — Part B uses **verbatim** passage sentences as evidence; **both parts** required to score."
    }
   ],
   "against": "No measured comparison of the two scoring rules was found in scope; the live scorer and item standard use all-or-nothing while the measurement review recommends partial credit.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A multiple-select question states how many answers to choose, and the keyed set must not simply be the longest options.",
   "kind": "adopted rule",
   "found_by": "Item standards and the generation harness require an explicit count and forbid a longest-options key; the delivery player was also found to make an uncounted multi-select unanswerable.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/knowledge-[name]-additions/docs/standards/course-quality.qmd",
     "lines": "40",
     "quote": "explicit count in multi-select stems;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "86-87",
     "quote": "**msq** — exactly one defensible correct SET; the keyed set must NOT be \"the two/three longest\"; include at least one live-trap distractor"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd",
     "lines": "114-115",
     "quote": "**R2 — MSQ does not work.** `cardinality=\"multiple\"` renders but the reader makes it single-select (can't be answered)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A word-meaning-in-context item must test a word that actually appears in the material, key the sense the material forces, and offer the word's everyday meaning as a distractor.",
   "kind": "measured",
   "found_by": "An earlier course shipped items testing words that were not in their passage (the 'vocab-word-mismatch bug'); the fix rules came from that defect.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "90-95",
     "quote": "the keyed sense must be the one the PASSAGE forces, and at least one distractor must be the word's *common* dictionary sense that the passage does NOT use — so a blind solver who picks the everyday meaning is wrong. **The tested word and its keyed sense must both actually appear/operate in the passage** (guard against the G3 vocab-word-mismatch bug: never test a word that isn't in the passage, never key a sense the passage doesn't license)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md",
     "lines": "46-47",
     "quote": "**Vocab word-not-in-passage (NN#5):** FIX by editing the PASSAGE — `PUT {QTI}/stimuli/{id}` to use the word in context. Never reword the stem to dodge it; never delete the item."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md line 171: \"Never repair a missing quote by changing the passage unless the passage authority itself is wrong.\" — the fix direction is disputed.",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A picture or diagram must not print the answer to the checks it supports.",
   "kind": "measured",
   "found_by": "A lesson audit found a diagram that printed its own key, letting a student pass every diagram check without reading, and a trap item whose wording leaked the diagram's fact.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "57",
     "quote": "prints its own answer key in-diagram (a key line stating the arrow rule, plus \"eater\"/\"diet unknown\" sub-labels) — lets a child pass every diagram check without reading the passage."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "66",
     "quote": "| F10 | major | No rendered check requires integrating both sources; the trap-item stem leaks the diagram's own fact. |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    64,
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check each test form for items that give away other items' answers, including cross-form tells where one answer pair unlocks both forms.",
   "kind": "measured",
   "found_by": "A reviewer cracked both forms of a usage check with a single answer pair; the key was de-correlated and a sweep of the other items found no further cross-form tell.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0211-peter-pan-reviewer-round-2708.qmd",
     "lines": "24",
     "quote": "Both usage checks were crackable via the single pair \"baby\"+\"sleep\" | **FIXED** `f75a301` — Form 2's key de-correlated; a gameability sweep over all 31 L4+L5 MCQs found no other cross-form tell"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "51",
     "quote": "Form-level answer-position, option-length, duplicate, enemy-item, and blueprint reports."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check the whole bank for repeated and near-duplicate items; items generated one per call repeat in ways a per-item review cannot see.",
   "kind": "measured",
   "found_by": "A question bank built by one-question-at-a-time generation held repeats; a whole-course evaluator was requested because per-item review missed them; a candidate pool rejected tens of thousands of duplicates.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0057-incept-team-sync-2-2026-06-18.qmd",
     "lines": "21-22",
     "quote": "Question bank has **repeats** (his API generates **one question at a time**, multiple quiz calls → duplicates) → needs an agent cleanup."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0057-incept-team-sync-2-2026-06-18.qmd",
     "lines": "49-50",
     "quote": "a **whole-course evaluator agent** (not per-item — catch repeats etc. that manual review catches; IB team could build it)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "32-33",
     "quote": "Greedy-selection rejection counters: 19,387 duplicate-item-id, 31,240 duplicate-question-text, 1,329 near-duplicate-question."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a fourth plausible distractor cannot be written, should a question use three options rather than fill the slot with an implausible one? The reviewers' four-option demand and the research summary conflict.",
   "kind": "open question",
   "found_by": "A reviewer asked for at least four options while the assessment research summary favours three; the decision was left to a named owner.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "40-43",
     "quote": "The reviewer says MCQs need at least four options. The MCQ BrainLift says the research consensus generally favors three options and recommends four as Alpha's default only when a third plausible, diagnostically useful distractor exists. Do not fill a fourth slot with an implausible option. Return `NEEDS_HUMAN` until the owner approves the default and exception."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/README.md",
     "lines": "94",
     "quote": "decide the three-versus-four-option MCQ policy when a fourth plausible distractor cannot be written;"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0241-alpha-read-contract-investigation-and-packager-build-2026-06.qmd line 109: \"arpack's \\\"exactly 4 choices\\\" gate over-restricts vs the API's real 2-6+ floor\" — the delivery format itself accepts two or more options.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A mastery gate needs enough items: on four or five items a 90% bar demands a perfect score, and an adaptive gate with a one-item bank can never reach mastery.",
   "kind": "measured",
   "found_by": "An evaluation found 4-5 item tests un-gateable; a submit loop was traced to one-item adaptive banks where a correct answer moved the score from 0 to 14, not 100.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "54-55",
     "quote": "**A test with <5 items cannot certify mastery at 90%** (1 wrong = 80% on a 5-item test; un-gateable on a 4-item test). Gate tests carry **enough items** for a 90% threshold to be meaningful."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
     "lines": "37",
     "quote": "two 4-5 item tests are un-gateable (no \"90% of 4\"); no three-state retry / parallel forms."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0021-powerpath100-course-shape-rootcause.qmd",
     "lines": "26",
     "quote": "PowerPath scoring is **incremental**: one correct answer from 0 → score **14, not 100**."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd lines 137-138: \"an arbitrary `>=15` bank-depth constant hardcoded in `audit_compliance.py` itself (circular — the spec just quotes the auditor); the real platform/publisher floor is 8.\" — how many items are enough must itself be sourced.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give every gated test at least two parallel forms with no shared items, so a retake shows new items rather than the same ones.",
   "kind": "adopted rule",
   "found_by": "A retake re-showed the same test; a single static form was judged gameable in a course audit.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "39-40",
     "quote": "**Two parallel forms (A + B) sharing ZERO items.** Parallel forms are required for retry without answer leakage (a student who retests sees the other form)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0022-incept-team-sync-2026-06-17.qmd",
     "lines": "63",
     "quote": "**Reattempt:** same test re-shown (small chance of variety); randomizing via multiple tests is"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
     "lines": "32",
     "quote": "NN#7 single static form (gameable)"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd lines 75-76: \"97/172 items can't populate disjoint parallel forms without overlap.\" — a small clean bank cannot yet support parallel forms.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Spread item difficulty across easy, medium and hard; a single-difficulty form floors weak students, ceilings strong ones and silently disables adaptive selection.",
   "kind": "adopted rule",
   "found_by": "A verification pass found items all tagged medium, which leaves an adaptive engine that picks items by difficulty band nothing to ease or ramp.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "89-90",
     "quote": "A 100%-medium form **disables discrimination** — it floors weak readers and ceilings strong ones, measuring nothing. The form **must spread** across easy / medium / hard."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "29",
     "quote": "items carry easy/medium/hard (NOT 100%-medium) so PowerPath can ease/ramp. *(new — 100%-medium silently disables adaptivity)*"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0054-reference.qmd",
     "lines": "238-239",
     "quote": "difficulty by current score (0–49 easy; 50–89 medium+hard 75%/25%; 90–99 hard only)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Where should a predictive test's difficulty be centred — on the verified norm, on the actual cohort, or above grade? Centring above where students sit made on-grade students look as if they were failing.",
   "kind": "open question",
   "found_by": "A measurement review corrected a blueprint centred above the published norm; the staged assessment standard still says to centre above grade.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "90-92",
     "quote": "centering item difficulty at 200-210 (our kb-0059 \"by design\") maximizes info ~+1.3 logits ABOVE where students sit → makes an on-grade reader read as failing and biases logit→RIT regression."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "91-92",
     "quote": "**Center above grade.** A test centered at the grade median is too easy to confirm above-grade reading."
    }
   ],
   "against": "The two sources conflict; ~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd lines 93-94 add: \"FAIL blueprints centered above the verified spring mean; reconcile vs the observed cohort mean 206.4.\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A readability level is not item difficulty and cannot by itself decide whether a text fits; difficulty is a match among the text, the reader's knowledge and the task.",
   "kind": "adopted rule",
   "found_by": "The assessment standard demoted readability to a secondary proxy; the project's doctrine and the research it cites reject a single readability number as the gate.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "97-98",
     "quote": "Lexile is a readability proxy, **not** item difficulty itself — flag it `[SECONDARY]`."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "48",
     "quote": "Text difficulty is a match among text factors, reader knowledge, and task — no single readability number can gate a text"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "705",
     "quote": "different readability estimates don't agree with each other and provide no diagnostic information for individualizing instruction."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Label item difficulty by its state — predicted, provisional from live use, or calibrated — and treat cut scores and thresholds as defaults until tuned on real attempt data; a model's pre-use estimate is not a calibrated value.",
   "kind": "adopted rule",
   "found_by": "Routing thresholds and cut scores were shipped as reasoned pilot defaults; the assessment packet forbids passing off model-estimated difficulty as calibrated.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "54",
     "quote": "Difficulty metadata distinguishing predicted, provisional live, and calibrated states."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "66",
     "quote": "Do not call pre-use LLM difficulty a calibrated item parameter."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd",
     "lines": "153-154",
     "quote": "**No threshold calibration** — cut-scores, mastery gates, WCPM targets are reasoned pilot defaults, to be tuned against real attempt data."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    15
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After items are used, review each one's functioning — option performance, subgroup fairness, drift — and quarantine or retire failures; score differences must not come from language, culture or background unrelated to the target.",
   "kind": "adopted rule",
   "found_by": "The assessment packet requires a live-analysis plan; the research digest sets fairness to individual, linguistic and cultural variation as a requirement.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "55-56",
     "quote": "Live-analysis plan covering minimum N, item and option functioning, subgroup/DIF review, uncertainty, drift, quarantine, and retirement."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "753",
     "quote": "Good comprehension assessments must be adaptable to individual, social, linguistic, and cultural variation; if performance differences reflect such variation rather than comprehension itself, the test is inadequate for the research/instructional agenda."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Declare each assessment's purpose — teaching check, mastery gate, diagnostic, interval or growth measure — before judging it, because the criteria differ, and treat a diagnostic result as a guide to study, not a grade.",
   "kind": "adopted rule",
   "found_by": "A course validator fails any assessment with no declared purpose; the assessment packet requires the declaration first and bars calling a diagnostic score a grade.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "47",
     "quote": "Product declaration: formative, mastery, diagnostic, summative, or cold measurement."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py",
     "lines": "651",
     "quote": "product_type -- required to gate which criteria apply."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "63",
     "quote": "Do not call a diagnostic score a grade; diagnostics route study under uncertainty."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the mastery gate and the growth measure as separate instruments; the growth test uses unseen material, is never gated on, and supports only direction claims until it is linked to the external scale.",
   "kind": "adopted rule",
   "found_by": "A course conflated its mastery test with its growth proxy; the checklist and assessment standard were rewritten to keep them apart.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "139",
     "quote": "These are **two distinct instruments** — do not conflate them."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "31",
     "quote": "the 24-item mastery GATE (`masteryThreshold:90`) is DISTINCT from the MAP-equivalent proxy (cold passages, raw/40+band, `gating=false`, no 90 threshold). Don't conflate."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/assessment-design.md",
     "lines": "135-136",
     "quote": "The predictive claim (\"does well here → does well on MAP\") is **a design intent, not a measured result**, until the linking study runs."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Recognition items cannot certify production or integrated knowledge: a 'write' or 'explain' target needs a production task, and some tasks must combine several components.",
   "kind": "adopted rule",
   "found_by": "The evaluator gap analysis and the assessment packet list recognition-only certification as a rejection-grade gap.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "124",
     "quote": "N3: recognition-vs-production match. \"Write/explain/draw\" targets cannot be assessed by MCQ alone."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "129",
     "quote": "N8: integrative-assessment presence. Include tasks that coordinate multiple KCs, not only atomized checks."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "64",
     "quote": "Do not certify productive or integrative knowledge with recognition alone."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A standards tag or a lesson's claimed skill must match the thinking its items actually require; an 'identify' item does not cover an 'analyze' standard.",
   "kind": "adopted rule",
   "found_by": "Reviewers found standards tags that did not match the work delivered; evaluators checked tag spread but not whether claimed skills were assessed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "122",
     "quote": "N1: DOK-level alignment. Coverage is false if an \"analyze\" standard is assessed by \"identify.\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "282",
     "quote": "standards tags do not match delivered cognitive work"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "114-115",
     "quote": "`concept_coverage` checks spread, not whether each lesson's claimed KC/skill matches what its items actually assess."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Tag every item with the standard it measures in structured item metadata, not in titles or prose, using one code convention that resolves in the official framework.",
   "kind": "measured",
   "found_by": "Audits found zero standards on every item of a live course, codes present only in titles, and a false zero caused by standards written only inside item markup.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
     "lines": "32",
     "quote": "NN#4 **CCSS 0/28** (codes only in titles)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0082-rex-v2-live-course-pull-2026-07-02-rex-v2-live-course-pull.qmd",
     "lines": "71",
     "quote": "**No item in this dump carries any standards field.**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/timeback-integration.md",
     "lines": "146-147",
     "quote": "Standards live in **`metadata`, never inline in `rawXml`.** A rawXml-only authoring shortcut produces a false-zero on pull (this caused a spurious \"zero standards\" FAIL pre-re-pull)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Do not time an understanding task unless speed is what is being measured; time pressure raised the accuracy penalty about threefold and rewarded rapid guessing.",
   "kind": "measured",
   "found_by": "A course design's evidence summary found time pressure tripled the on-screen accuracy penalty and rewarded rapid guessing that the external test penalizes; the item standard then made every comprehension item untimed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "31",
     "quote": "| 10 | **Untimed comprehension** — `time-dependent=\"false\"` on every item | per-item timer on a comprehension item |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "163",
     "quote": "time pressure ~triples the on-screen accuracy penalty and rewards rapid-guessing, which MAP penalizes; clocks only where speed is the construct"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Keep answer keys off the student's device and score on the server; never accept a correctness flag sent from the screen.",
   "kind": "adopted rule",
   "found_by": "The production reading app and a custom delivery app both strip keys before sending items and block client scoring in code; the cross-thread briefing made it a standing rule.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
     "lines": "88",
     "quote": "**No client-side scoring, ever** — render + report responses; the server scores. Never send renderer outcomes."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0060-incept-read-app-field-notebook.qmd",
     "lines": "39-41",
     "quote": "The client must **never** extract the answer key, compute score/mastery/XP/accuracy/advancement, send `rendererOutcomes`, persist scores, or hold a secret. QTI is fetched `view=student-before-answer`."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0024-beyond-alpharead-pr45-all-qti-types.qmd",
     "lines": "37-38",
     "quote": "**never trusts client-reported correctness**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Test scoring with every wrong response as well as the right one; an invented scoring rule silently mis-scored two-part items.",
   "kind": "measured",
   "found_by": "A cross-check found the packager used a scoring template that does not exist, so two-part items would have scored wrongly; the later contract proof exercises every wrong response for each fixture item.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/README.md",
     "lines": "308-310",
     "quote": "The committed evidence is `course-json-live-evidence/3`: it binds schema, validator, projector, source, and manifest digests and proves one correct response plus every per-response negative case for all nine fixture items."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0241-alpha-read-contract-investigation-and-packager-build-2026-06.qmd",
     "lines": "106-107",
     "quote": "`map_response` is not a real QTI template (invented), EBSR scoring would be silently wrong"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    36
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep corrective feedback short (aim near 40 words, never over 60), name the misconception it addresses, and never make it longer or harder than the instruction it corrects — at that point it has become new instruction.",
   "kind": "adopted rule",
   "found_by": "Reviewers judged long feedback a failure for young students; a lesson lint now blocks feedback over 60 words or without a misconception key.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "96-97",
     "quote": "This incorporates the Practice BrainLift boundary rule: if corrective feedback is longer or more complex than the original instruction, the item has crossed into new instruction."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "15",
     "quote": "| L4 | feedback word caps | feedback must carry a `misconception_id` and be <= 60 words (hard cap); 41-60 words emits a non-blocking warning (40 is the standard's target). |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "283",
     "quote": "Long feedback text is itself a failure for Grade 3."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26,
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write feedback for each wrong option specifically, tied to the error that option represents; generic or position-keyed feedback is a defect.",
   "kind": "measured",
   "found_by": "A submission closure counted every option-specific feedback route and required zero generic or position-keyed ones; evaluators and the checklist require misconception-named feedback.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "64-65",
     "quote": "all 1,234 option-specific feedback routes have zero generic option-position IDs or truncated claim/recheck templates."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "125",
     "quote": "N4: misconception-coded distractors and misconception-named feedback."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "30",
     "quote": "every scored item has a `FEEDBACK` outcome + CORRECT/INCORRECT `qti-modal-feedback` (distractors→named misconception)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prove feedback actually fires in the delivered player; feedback present in the item data can silently never show.",
   "kind": "measured",
   "found_by": "A course audit found authored feedback silent on all 542 items; the renderer drops feedback whose linkage is incomplete.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
     "lines": "31",
     "quote": "NN#5 feedback **silent 0/542**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "44",
     "quote": "`process-response` returns the authored `FEEDBACK` (CORRECT/INCORRECT), NOT the generic fallback; wrong answer fires corrective feedback. *(new — the silent-no-op trap; \"authored\" ≠ \"resolves\")*"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0019-alphalearn-qti-renderer.qmd",
     "lines": "133",
     "quote": "Content lacking these will render with NO feedback in strict mode — author accordingly or risk silent gaps."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    46,
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give immediate feedback for simple facts and explained feedback, saying why, for concepts.",
   "kind": "adopted rule",
   "found_by": "The delivery platform's published learning-science tiers, adopted by the project as its bar.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd",
     "lines": "38",
     "quote": "| **Feedback**        | Immediate for basic facts; elaborated (explaining why) for concepts.   |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "65",
     "quote": "| **Feedback** | Immediate for basic facts; elaborated (explaining why) for concepts. |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Feedback and progress screens must be true to what the student actually did: no fixed reply presented as a response to the answer, and no claim of an action the student did not take.",
   "kind": "measured",
   "found_by": "A lesson audit found a welcome step that claimed to listen while giving the same recast to every answer, and a receipt screen asserting spoken or self-done events that never happened on typed paths.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "70",
     "quote": "| F14 | major | The welcome beat overclaims contingent listening while still issuing a static, answer-independent recast (\"However you put it...\"). |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "71",
     "quote": "| F15 | major | The receipt screen asserts out-loud/self-done events that did not actually happen on the typed/floor interaction paths. |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    11
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Modelled, guided and independent steps must practise the same operation with the same steps; a model that only reveals the answer, a guided step that is just a hint, or an independent task on a different skill breaks the release.",
   "kind": "measured",
   "found_by": "A review round found modelling that revealed the answer, hint-only guided practice and independent work on a different skill; a lesson lint now catches each shape.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "12",
     "quote": "| L1 | triple-presence | model, guide, release atoms exist for the lesson's operation_id, with one identical, non-empty ordered step list. Catches the round-2 answer-reveal I-do (payload only the answer = empty steps). |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "280-281",
     "quote": "I-do/we-do/you-do is misapplied (answer reveal / hint / different skill)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "46",
     "quote": "Gradual release is one process at decreasing support: the I-do models *thinking*, the we-do walks the same steps with immediate feedback, the you-do releases the same skill"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Introduce at most one new operation per lesson, and let review steps reuse only operations already taught, never smuggle in a new one.",
   "kind": "adopted rule",
   "found_by": "The platform bar forbids bundling new skills; a lint catches a second new operation and an adversarial review found one hidden in a review step.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "25",
     "quote": "4. **Design for cognitive load limits.** Keep granularity tight, reduce noise, avoid bundling multiple new skills in one lesson."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "17",
     "quote": "| L6 | one new operation per dose | every non-review atom carries exactly the lesson's one `operation_id`. Catches the round-2 skill-switching you-do (together with L1). |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/lesson-schema.md",
     "lines": "71-72",
     "quote": "(an undeclared new operation cannot be smuggled in as phase:\"review\")."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A lesson may assume only knowledge that earlier lessons in the sequence actually taught; check each lesson's assumptions against what came before and treat a missing link as a failure, not a skip.",
   "kind": "adopted rule",
   "found_by": "A lesson lint and the course validator both check that each lesson's assumed knowledge was added earlier, and fail an unresolved lesson rather than skipping it.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "16",
     "quote": "| L5 | spine check | `lesson.assumes` is a subset of the union of prior lessons' `adds`, in unit order. |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py",
     "lines": "592-593",
     "quote": "lesson '%s'%s assumes %s not added by any prior lesson in the unit (assumes[] must be a subset of prior lessons' adds[])."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py",
     "lines": "578",
     "quote": "# A missing lesson must fail here too; skipping it would make the spine check vacuous."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Any reference to earlier material ('as you saw last lesson') must be true in the actual sequence.",
   "kind": "measured",
   "found_by": "A lesson audit found its stated justification for prior exposure was false against the lesson's own lineage; the evaluator gap list adds the check.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "123",
     "quote": "N2: relational-reference factuality. \"As you saw last lesson\" claims must be true against order."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "60",
     "quote": "`exposure_justification` is factually wrong against the lesson's own U1-L6 lineage."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Every check must block progress until it is answered; a check that can be skipped by pressing Next twice, refreshing or tapping ahead is no check, and a step not declared blocking counts as skippable.",
   "kind": "measured",
   "found_by": "A 'Next-twice' exploit and hint-style steps let students skip checks; the player now records only banked progress so a refresh cannot open a gate. The doctrine treats a bypassable gate as misplacing the student, not only as a data problem.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "14",
     "quote": "| L3 | every check blocking | any non-blocking atom is a failure (the \"Next-twice\" exploit; the round-2 hint-style we-do). M5 carve-out below. |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "75-76",
     "quote": "**`blocking` defaults to false:** an atom that does not declare itself blocking is treated as skippable (absence of a guarantee is not a guarantee)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0191-g3-book-lesson-anatomy.qmd",
     "lines": "155-157",
     "quote": "Records only what is BANKED, never half-done state, so a refresh cannot open a gate the child has not passed."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep the material visible whenever a step asks the student to cite, quote or find evidence in it, and show the part the question is actually about.",
   "kind": "measured",
   "found_by": "Reviewers found an evidence-writing step that hid the passage; the renderer once pinned a different part of the story than the one a proof question asked about.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
     "lines": "13",
     "quote": "| L2 | passage visibility | `cites_text` implies `passage_visible` on every atom. |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "281-282",
     "quote": "evidence-writing hides the passage"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0191-g3-book-lesson-anatomy.qmd",
     "lines": "70-73",
     "quote": "A page's own passage wins over an earlier one — this was a real, fixed bug: the renderer used to pin whichever passage came last in the whole lesson and drop the page's own passage on the floor, which could show a different part of the story than the one a proof-question was asking about."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Have students select the evidence before they paraphrase it or write about it.",
   "kind": "adopted rule",
   "found_by": "Reviewer feedback demanded evidence-first articulation; the lesson packet fixed it in the required lesson sequence.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "42",
     "quote": "5. evidence selection before paraphrase or written articulation;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "94",
     "quote": "evidence-first articulation"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In the worked example, model the genuinely hard judgment on the visible material — including the tempting wrong alternative and why it is rejected — and then have the student do it cold.",
   "kind": "adopted rule",
   "found_by": "Reviewers wanted authentic modelling of the difficult step; a lesson audit kept, as verified-correct, a model that rejected the tempting alternative followed by a cold attempt with no hints first.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "40",
     "quote": "3. I-do on the visible text, exposing the genuinely difficult judgment;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "78-79",
     "quote": "(I-do models the rejected hunter-to-prey alternative; You-do re-elicits cold with `attempt_first:true` and \"no hints before you try\" — canonical, not a leak;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Model a skill in a fixed order — say what to do, show it done, then check — with one thing for the student to look at.",
   "kind": "adopted rule",
   "found_by": "Educator feedback on a lesson praised the think-aloud but demanded this modelling choreography.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "18",
     "quote": "modeling choreography (say → see it done → check, one attention target)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fade support by exposure across lessons, moving from mostly modelled to mostly independent work so the scaffolds end on plain material.",
   "kind": "adopted rule",
   "found_by": "Educator feedback specified an exposure-based fade; the review bar asked for explicit instruction with worked examples and fading.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "18",
     "quote": "exposure-based scaffold fade (5/2/1 → 3/2/3 → 1/2/5)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "288-289",
     "quote": "use explicit instruction with worked examples and fading"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd line 30 records a held dispute: \"named inference routines as *fading scaffolds* retired on a stated condition\" versus scheduled recurring retrieval of the routine.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Every screen asks the student for a purposeful response; avoid long passive stretches, interleave quick checks into explanation and cut redundant prose.",
   "kind": "adopted rule",
   "found_by": "Reviewer meetings required active, focused student flow; the evaluator gap list adds an active-check cadence.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "23",
     "quote": "each screen earns a purposeful response; knowledge building avoids redundant prose and interleaves quick checks"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "128",
     "quote": "N7: active-check cadence. No long passive segment without a non-bypassable check."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "68",
     "quote": "every screen needs meaningful student engagement; knowledge building should be focused and checked;"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd line 39: \"remove Scout's interjections at the top of each page. They take away from the reading flow.\" — added prompts can also break flow.",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every reread sends the student back to selected material for a stated purpose.",
   "kind": "adopted rule",
   "found_by": "Reviewer meetings asked that rereads serve the knowledge objective rather than repeat reading.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "23",
     "quote": "rereads return to selected text for a declared knowledge purpose."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "68",
     "quote": "targeted rereads serve the knowledge objective;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Aim each understanding check at the detail the lesson's main idea hinges on, not at an incidental detail.",
   "kind": "measured",
   "found_by": "A reviewer asked that a check target the detail crucial to the theme; a spot-check of four lessons then found two checks about incidental details.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "49",
     "quote": "\"can this check about his mother never mentioning the brother as it's a key/crucial bit for the theme of betrayal\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "60-62",
     "quote": "Two L4 checks are incidental rather than thematic: p10 \"Who jumped first?\" (purpose: what the children must believe before they can fly) and p12 \"What happened to the lights of London?\" (purpose: how Peter makes Neverland sound)."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd lines 64-66: the fix was held on \"whether the 20.09 reading-checks-stay-retrieval ruling (checks stay literal) extends to requiring the literal check be about the hinge specifically.\"",
   "adds_to_existing": [
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write questions for the specific material; do not turn a generic skill label into one question script used for every text.",
   "kind": "adopted rule",
   "found_by": "Reviewers asked for bespoke questions; the lesson lint explicitly cannot judge this, so it was made a stop rule for authors.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "60",
     "quote": "Do not turn a generic taxonomy label into a universal question script."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "93",
     "quote": "bespoke questions"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/TOOLING.md",
     "lines": "53-55",
     "quote": "It does not judge whether a think-aloud is authentic, whether a question is text-bespoke, or whether teaching is effective."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Freeze the course architecture and place the material before writing lessons; never author a lesson from a bare topic.",
   "kind": "adopted rule",
   "found_by": "Feedback lanes were sequenced so lesson authoring waits for a frozen unit architecture; delivery estimates start only from frozen inputs.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/curriculum-agent.md",
     "lines": "48",
     "quote": "Do not start lesson authoring from unresolved unit architecture."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "58",
     "quote": "Do not author from a bare topic or unplaced text."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "164",
     "quote": "start the clock only from frozen architecture/scope/acceptance inputs."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build each lesson from its own lesson-level design, not only from general guidance; a lesson built from correct general guidance lacked three required components.",
   "kind": "measured",
   "found_by": "A lesson built from the general workbook and procedure guide was correct but 'a tier too general'; its own design document mandated three components it lacked, so lesson designs were made the build specification.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "59",
     "quote": "Promoted 2026-08-25 after G3-U1-L4 was built from the KB workbook + procedure HTML alone: both correct, both a tier too general, and the design doc mandated three components the lesson lacked entirely (the Component 6 cloze, the Magic Doors, the INFER step rail) plus a canonical video we do not hold."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0176-g3-peter-pan-pr-timeline.qmd",
     "lines": "22-24",
     "quote": "**\"named designs govern\"** made the four original Peter Pan lesson-design DOCX (`~/Downloads/5. Curriculum`, PP1-PP4) the build specification for L4-L7, not the sourcing portal's 17-chapter novel."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "List the words that would block understanding and decide for each whether to pre-teach, gloss or leave it, deep-teaching only the words that actually block.",
   "kind": "measured",
   "found_by": "A lesson audit found familiar words deep-taught as if they blocked understanding; the lesson packet now requires a vocabulary ledger with a disposition per blocking word.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "52",
     "quote": "Vocabulary ledger: target word, blocking words, disposition, audio/definition requirement."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "59",
     "quote": "| F3 | major | \"producer\"/\"habitat\" are deep-taught as if they were blocking vocabulary (they aren't). |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Teach key words with a definition plus use in context and planned re-encounters across materials; incidental exposure and dictionary definitions alone teach little.",
   "kind": "adopted rule",
   "found_by": "The project's doctrine and authoring tier adopt this vocabulary recipe from the research it cites (a vocabulary-instruction book; no DOI given).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "45",
     "quote": "Tier-2 vocabulary requires direct robust instruction plus engineered re-encounters; incidental context is an unreliable acquisition channel"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd",
     "lines": "56-57",
     "quote": "Vocabulary recipe: definitional + contextual, multiple encounters, morphology (~60% of meanings predictable), taught words chosen for generative value."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "60",
     "quote": "Sentences students write from dictionary definitions are unacceptable 60–63% of the time"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check whether a student knows a word by asking for an example or an explanation, not by self-report; far more students say they know a word than can explain it.",
   "kind": "external research",
   "found_by": "Cited in the project's doctrine from a vocabulary-instruction book (pp. 10–11); no DOI or URL is given in the source. It matches the platform rule never to advance on self-report.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "61",
     "quote": "Word knowledge is a continuum: \\~80% of students check a word as \"known,\" \\~50% can give an example, \\~20% can explain it"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "21",
     "quote": "2. **Enforce mastery gates at ≥90% accuracy.** Do not advance students based on time, completion, or self-report."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Advance students only on demonstrated mastery on rigorous checks, never on time, completion or self-report, so that 'completed' means mastered.",
   "kind": "adopted rule",
   "found_by": "The delivery platform's non-negotiables and evaluation dimensions, adopted by the project as its bar.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "21",
     "quote": "2. **Enforce mastery gates at ≥90% accuracy.** Do not advance students based on time, completion, or self-report."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0026-evaluating-apps.qmd",
     "lines": "21",
     "quote": "| **Mastery truthfulness**       | \"Completed\" means mastered                         |"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0006-beyond-alpharead-source.qmd line 55: \"The **\\\"mastery\\\" metric (80% correct answers)** is accurately calculated on Dash.\"; ~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd line 123: \"**Staged 90% gates** — Band A advisory, blocking from Band B, final gate at course end (only ~17% reach 90% today).\" — the bar and its enforcement vary.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Prove that a mastery gate blocks a learner below the bar with a live attempt; a declared threshold can be missing or unenforced.",
   "kind": "measured",
   "found_by": "An evaluation found a 90% threshold declared but not enforced; a merge found the threshold null on two live courses, so the gate did not block.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
     "lines": "37",
     "quote": "`masteryThreshold:90` declared in metadata, not enforced by an observable mechanism; lesson tests carry NO threshold;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "91-92",
     "quote": "`masteryThreshold` was `null` on both live courses (the 90% gate didn't actually block)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md",
     "lines": "44-45",
     "quote": "PROVE it with a play-through, don't assert a metadata field as \"enforced.\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38,
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Reward only verified learning: no points for passive activity or for work below 80% accuracy, and penalties rather than points for gaming.",
   "kind": "adopted rule",
   "found_by": "The delivery platform's reward rules, adopted by the project; a custom app was found fabricating quiz points with no accuracy floor.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0030-xp-system.qmd",
     "lines": "54",
     "quote": "**Warning:** No XP is awarded below 80% accuracy. This discourages students from speed-running content or guessing until correct."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "174",
     "quote": "Rewards for fake progress train students to optimize the reward system, not their knowledge. Motivation follows mastery, not the reverse."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0060-incept-read-app-field-notebook.qmd",
     "lines": "52-53",
     "quote": "The broker previously **fabricated** quiz XP (`correct × 3`, no 80% floor, not time-based"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Assume students will take any shortcut the reward allows — tanking placement, clicking through explanations, guessing until correct, pattern-matching on items — and design so the target thinking cannot be skipped.",
   "kind": "adopted rule",
   "found_by": "The delivery platform's principles, adopted by the project; its list of observed gaming patterns.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "182-185",
     "quote": "Tanking placement tests to receive easier content Clicking through explanations without reading Guessing until correct Pattern matching on test items rather than learning concepts"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "94",
     "quote": "**Make the target cognitive process unavoidable.** If students can succeed via pattern matching, shallow guessing strategies, or memorizing repeated items, the app is gameable and its signals are untrustworthy."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Choose examples so that only one rule fits them — contrastive examples, near-misses that differ only in the critical feature, non-examples — because a wrong rule students can infer from the examples is the instruction's fault.",
   "kind": "adopted rule",
   "found_by": "The delivery platform's principles, adopted by the project as its bar.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "83",
     "quote": "If the learner can logically infer the wrong rule from the examples provided, the fault lies with the instruction, not the learner."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "87-88",
     "quote": "**Contrastive examples** that show what counts and what does not **Near-misses** that differ only in the critical feature"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "27",
     "quote": "5. **Make misconceptions hard to form.** Use clear examples, non-examples, and fast error correction."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "No added feature — spacing, multimedia, games — makes up for missing basics: unambiguous instruction, retrieval practice and mastery gating.",
   "kind": "adopted rule",
   "found_by": "The delivery platform's learning-mechanism hierarchy, adopted by the project; the compliance template certifies these basics as binary.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "77",
     "quote": "**Tip:** Tier 0 is binary. You either have faultless communication, retrieval practice, and mastery gating, or you do not. No amount of Tier 1 or 2 optimizations can compensate for a broken foundation. Features are liabilities; mechanisms are assets."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Practice must require recall, not only recognition, and review must be spaced and mixed across units rather than massed on one piece of material.",
   "kind": "adopted rule",
   "found_by": "A verification pass found spaced review missing; the checklist added recall-format items and cross-unit interleaved review.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "29",
     "quote": "6. **Build in retrieval practice and spaced review.** Practice must require recall, not just recognition."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "45",
     "quote": "cross-unit **interleaved** review present (not massed single-passage); recall/production-format items present (not recognition-only)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd",
     "lines": "35-36",
     "quote": "| **Spacing**         | Distribute practice over time. Cramming creates temporary performance. | | **Interleaving**    | Mix problem types to prevent context-dependency.                       |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Plan the sequence so key ideas and words recur across related materials; the curriculum itself is the first spaced-practice system, and separate spaced review covers only what is not reused.",
   "kind": "adopted rule",
   "found_by": "Curriculum-architecture doctrine adopted as the routing authority; the project's own doctrine counts engineered recurrence as vocabulary teaching, spaced retrieval and knowledge building at once.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "64",
     "quote": "\"use the curriculum to keep generative knowledge warm by use; use spaced practice for the residue.\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "38",
     "quote": "**The text set IS the practice schedule.** Engineered recurrence across a coherent text set is simultaneously vocabulary instruction (DOK1-2), spaced retrieval (endogenous, per Allen's curriculum-as-first-SRS), and knowledge building — one design decision doing three jobs, which is why set construction outranks exercise design."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "270-271",
     "quote": "the curriculum is the FIRST spaced-practice system."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Teach easily confused concepts explicitly, one at a time, and interleave them once both are learned.",
   "kind": "adopted rule",
   "found_by": "The course graph marks confusable pairs as their own edge type that drives example selection and interleaving.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd",
     "lines": "42",
     "quote": "**Gateway discriminations** (taught explicitly, interleaved after both learned): narrator vs author; main idea vs supporting detail; fact vs author's claim/opinion"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd",
     "lines": "15",
     "quote": "near-neighbor discriminations driving example selection"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd",
     "lines": "36",
     "quote": "| **Interleaving**    | Mix problem types to prevent context-dependency.                       |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Build knowledge through coherent sets of related materials on one topic; this builds topic knowledge and vocabulary and carries over to new related material, though only near the topic.",
   "kind": "external research",
   "found_by": "A controlled study (DOI 10.1007/s11145-016-9628-x) summarized in the project's evidence base; transfer measured as near-domain.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/README.md",
     "lines": "34-36",
     "quote": "What compounds is knowledge: reading conceptually coherent text sets measurably builds topic knowledge, accelerates incidental vocabulary acquisition, and transfers to comprehension of novel related texts"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/sources.qmd",
     "lines": "17",
     "quote": "DOI: 10.1007/s11145-016-9628-x"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "37",
     "quote": "knowledge transfer is near-domain at best (Cervetti η²=.09)"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/SKILL.md lines 40-41: \"(e.g. Cervetti: N=59, exploratory, comprehension-questions measure null;\" — small exploratory sample and a null result on one measure.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Teach general strategies briefly and inside coherent content, then spend the time building knowledge; strategy gains saturate quickly, and strategies taught apart from content are not fully learned.",
   "kind": "external research",
   "found_by": "Reviews summarized in the project's evidence base (author's copy at http://www.danielwillingham.com/; https://www.rand.org/pubs/monograph_reports/MR1465.html, both as listed in sources.qmd).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "57",
     "quote": "Across eight quantitative reviews, \\~10 strategy-instruction sessions produce the same comprehension benefit as \\~50 — no dose-response"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "529",
     "quote": "\"Unless the strategies are closely linked with knowledge and understanding in a content area, students are unlikely to learn the strategies fully, may not perceive the strategies as valuable tools\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "535",
     "quote": "\"If comprehension strategies are taught with an array of content and a range of texts that are too wide, then students will not fully learn them.\""
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd line 499: \"Explicit instruction generates the immediate use of comprehension strategies, but there is less evidence that students continue to use the strategies in the classroom and outside of school after instruction ends\" — durability is weak either way.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Design the knowledge curriculum — domains, throughlines, sets of materials — first and check standards alignment afterwards; skills-only standards carry no content, sequence or prerequisites.",
   "kind": "adopted rule",
   "found_by": "The project's teaching doctrine and the adopted curriculum-architecture authority both demote skills-only standards to an after-the-fact check.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "21",
     "quote": "Therefore the knowledge curriculum — domains, throughlines, text sets — is the load-bearing design object, and standards alignment is a *check run afterward*."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "268-269",
     "quote": "standards mislead as teaching plans — assessments are the evidence authority;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Type every prerequisite link — hard (logically required) or soft (eases learning, with a fluency threshold) — and record why it holds; only a hard link backed by more than convention may block a student, and do not invent prerequisite chains the domain lacks.",
   "kind": "adopted rule",
   "found_by": "The course validator fails links with no stated warrant and warns when a merely conventional link would block; the course graph forbids fabricated prerequisite chains and gives soft links a fluency threshold instead of a yes/no.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py",
     "lines": "616-617",
     "quote": "graph edge %s->%s carries no warrant (every typed edge must state WHY it holds: logical|empirical|conventional)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/tools/course_validate.py",
     "lines": "620-621",
     "quote": "hard_prereq edge %s->%s rests on a conventional warrant; it cannot justify a hard instructional block without stronger evidence."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd",
     "lines": "13",
     "quote": "the COMPREHENSION band is horizontal (knowledge-sequenced by design, cross-subject dependencies, no fabricated prereq chains)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Separate atomic knowledge statements from the composite tasks that combine them, and define the final integrated performance by exemplars and a rubric instead of decomposing it further.",
   "kind": "adopted rule",
   "found_by": "The draft curriculum workbook separates atoms from composites; the course graph defines its capstone by exemplars and rubric with a decomposition floor.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0150-science-g6-atom-composite-ledger.qmd",
     "lines": "9",
     "quote": "separating 140 atomic knowledge statements from 49 composite performance tasks"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd",
     "lines": "65",
     "quote": "defined by exemplars+rubric, NOT decomposed further"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0150-science-g6-atom-composite-ledger.qmd lines 24-25: \"All 189 `Reviewer Comments` cells are blank: that records an absence of reviewer comments, not reviewer approval.\" — the workbook is a draft.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "For each knowledge statement, record what is new compared with earlier grades and which earlier statement it builds on, and add a negative definition (what it is not) where a misconception is likely.",
   "kind": "adopted rule",
   "found_by": "Pattern used throughout the draft curriculum workbook attached to reviewer feedback; it applies the adopted rule to use non-examples against misconceptions.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd",
     "lines": "41",
     "quote": "[Spiral review of G2 Unit 2, A3-A4 — what is new: \"atoms\" replaces \"tiny pieces/particles\"; formal term introduced per D1 3-5 band]"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd",
     "lines": "42",
     "quote": "[New — D1 Section 2.1 negative definition; required at Grade 3]"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0028-non-negotiables.qmd",
     "lines": "27",
     "quote": "5. **Make misconceptions hard to form.** Use clear examples, non-examples, and fast error correction."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0147-draft-grade-3-science-ledger.qmd line 27: \"Every `Reviewer Comments` cell is blank; the source contains no completed reviewer feedback,\" — unreviewed draft.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check new material against later grades' curricula to catch concepts introduced too early, and do not let a text be the first place a student meets another subject's concept.",
   "kind": "adopted rule",
   "found_by": "Later-grade ledgers were preserved mainly as boundary checks; subject guidance and the passage-integrity packet forbid first introductions disguised as background.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0150-science-g6-atom-composite-ledger.qmd",
     "lines": "20",
     "quote": "Use this ledger mainly to check whether G3-G5 materials introduce Grade 6 concepts too early."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "81",
     "quote": "As a general rule, avoid implicitly introducing scientific concepts that students may not have encountered. It is better to re-encounter ideas from earlier grades than for Alpha Read or Alpha Write to be the first place a student meets an idea."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
     "lines": "54",
     "quote": "no cross-grade science first introduction disguised as Reading background;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When another subject's content appears, reinforce rather than redefine it — match its vocabulary, nuance and framing — and give it a new angle rather than repeating the same topic.",
   "kind": "adopted rule",
   "found_by": "Curriculum guidance for cross-subject re-encounters attached to reviewer feedback.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "36",
     "quote": "Where a topic has already been covered, the Read/Write lesson should be consistent with how it was framed in the subject app, including its vocabulary, level of nuance, and framing."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "31",
     "quote": "Avoid sitting squarely on top of an identical topic. The re-encounter should feel like a new angle rather than a repeat: use a different subtopic, example, lens, or question."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write cross-subject material so it works whether or not the student has had the other subject's lesson yet.",
   "kind": "adopted rule",
   "found_by": "Guidance written because students sit in different grades across subjects and the apps cannot tell whether a topic was studied.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "30",
     "quote": "Topics taught in the same grade are potentially acceptable, provided the Read/Write treatment works whether or not the substantive science or social studies lesson has happened yet."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A curriculum map records what should have been taught, not what a student has learned; never treat a map row as proof of prior knowledge.",
   "kind": "adopted rule",
   "found_by": "The feedback handoff and every draft ledger carry this boundary because the maps were at risk of being read as evidence of prior learning.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/README.md",
     "lines": "64-65",
     "quote": "Treat workbook rows as a candidate adult-facing vertical-coherence map, not approved student wording or proof that a student has already learned a concept."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0152-science-g8-atom-composite-ledger.qmd",
     "lines": "9",
     "quote": "not evidence that younger students learned these concepts"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0149-draft-grade-5-science-ledger.qmd",
     "lines": "10",
     "quote": "never assume the listed concepts were taught, mastered, reviewed, or approved for students."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Do not copy draft or adult-facing planning text straight into student-facing material without separate authoring and review.",
   "kind": "adopted rule",
   "found_by": "The passage-integrity packet and the draft ledgers forbid it because the planning standards are written for adults and are unreviewed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
     "lines": "55",
     "quote": "no draft workbook sentence copied directly into child-facing prose without separate review."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0150-science-g6-atom-composite-ledger.qmd",
     "lines": "25-26",
     "quote": "Do not convert the content statements into student prose without a separate authoring and review process."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Do not present a contested interpretation as settled or a model as literal reality, and make clear whether a statement is an observation, an interpretation, a consensus or an opinion.",
   "kind": "adopted rule",
   "found_by": "Subject-integrity guidance and the passage packet list these as non-negotiable checks on any text.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "58",
     "quote": "A passage should not present a matter as settled where that is unwarranted. Distinguishing fact, interpretation, and opinion is part of the discipline itself."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
     "lines": "53",
     "quote": "no model presented as literal reality;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "85",
     "quote": "The scientific process distinguishes observation, hypothesis, theory, consensus, measurement, and related categories; student writing should make clear which of these the student is doing."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Back every real-world claim with a recorded source of the strongest available kind (official, primary, or a reference the course owner chose); model memory, search snippets and blogs cannot verify a fact.",
   "kind": "adopted rule",
   "found_by": "The content-integrity skill sets a source hierarchy and record format; subject guidance warns that a vivid but loose passage embeds hard-to-undo misconceptions.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "119-121",
     "quote": "Record source title, publisher, direct URL, retrieval date, exact locator, bounded fact, scope boundary, and content digest when bytes are available. Search snippets, unsourced summaries, blogs, and model memory cannot support `PASS`."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0137-science-social-studies-reencounter-guidance.qmd",
     "lines": "40",
     "quote": "Nonfiction passages should be factually accurate and traceable to reputable sources. A vivid but factually loose passage creates downstream work for the subject team and risks embedding misconceptions that are hard to undo."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "96",
     "quote": "every science-bearing Read/Write object must use reputable sources and pass"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check each factual claim against its recorded source, not against what sounds plausible, looking for definitions that drop a category or qualifier, category mistakes, unsupported mechanisms, causal overclaims and intent given to impersonal processes.",
   "kind": "adopted rule",
   "found_by": "The content-integrity skill's factual lane, written from the blocking defect shapes found in generated course prose.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "135-138",
     "quote": "test definitions for missing categories and qualifiers; test ontology/category mistakes, unsupported mechanisms, causal overclaims, and contradictions; flag teleology or conscious intent attributed to evolved traits or impersonal processes; compare the claim with the frozen source boundary, not with what sounds plausible."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "140-142",
     "quote": "Examples of blocking shapes include defining a broad category as only one subtype, calling a process a body part, treating an animal as a producer, or replacing a causal definition with \"most connected.\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Text-dependence and factual truth are separate checks: a question can require the material while the material itself is unsourced or wrong.",
   "kind": "adopted rule",
   "found_by": "The anti-leak harness states its own boundary: its grader checks whether the material is needed, not whether the machine-written material is true.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "267-269",
     "quote": "Anti-leak (kb-0064) means \"you must read the passage to answer\" — it does NOT mean the passage's own facts are sourced or true. A perfectly anti-leak item can sit on an unsourced machine-authored passage."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "186",
     "quote": "**Note:** you grade **anti-leak + G5 compliance**, not source truth."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a lesson mixes an invented teaching case with real evidence, make the two clearly distinguishable to the student.",
   "kind": "adopted rule",
   "found_by": "A grade's narration voice was chosen specifically so a made-up teaching case and real evidence sound different.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "61-62",
     "quote": "its first unit mixes a made-up teaching case with real evidence and the two must be audibly distinguishable."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Never let the writer certify its own work: changed items are re-checked by a different checker from a different model family, and only unchanged passes carry forward.",
   "kind": "adopted rule",
   "found_by": "The content-integrity workflow, Course JSON lifecycle and assessment packet all forbid self-certification after finding self-grades generous.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "263-264",
     "quote": "Do not certify your own authored content. The author may fix findings; an independent reviewer must close them."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/README.md",
     "lines": "154-157",
     "quote": "`verify` replays the patch from the base, carries forward only digest-equivalent passing cases, requires fresh evidence for every changed semantic case, and forbids the repairer identity or model family from verifying its own work."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "65",
     "quote": "Do not use the authoring model as its own certifier."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report a writer's first-attempt pass rate per item type, deduplicated by template; survivor counts after many samples, or cached best picks, hide low yield and template stamping.",
   "kind": "measured",
   "found_by": "A pool's 8,937 'passes' turned out to be best-of-N with one template stamped about 1,475 times and no sequence/match item surviving; an earlier AP question-generation effort's headline 99% was best-of-N plus serving from cache while the single-attempt model sat near 0.29.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/generator-output-spec.md",
     "lines": "32-36",
     "quote": "A total like \"8,937 passes\" is **best-of-N reborn** — the same crutch aptraining's \"served-99%\" turned out to be — when it counts re-samples and template clones: in the G5 intake **one EBSR template was stamped ~1,475× and 0/8,937 sequence/match items survive the strict grader.**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "93",
     "quote": "aptraining's headline \"99%\" was a **build-time best-of-N + serve-from-cache exploit** (kb-0063; SCOREBOARD_99 \"NOT the model generating\"), and the raw K=1 model floored at mcq/mcq_set 0.292 while the stack masked it [M8]."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md",
     "lines": "28-29",
     "quote": "G5 intake gates on **first-attempt, per-template-deduplicated `raw_pass_rate` per type** — \"1 prompt → 1 sampled item → graded\", NOT \"cell has ≥20 survivors after N samples\"."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md lines 260-262: \"**Inference-time generate-and-verify is legitimate for a PRODUCTION generator** — shipping best-of-K verified items is a fine way to build a bank. But it is **NOT a K=1 single-model claim.**\" — a filtered bank is fine if reported as such.",
   "adds_to_existing": [
    65
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Validate the scoring harness before trusting its numbers, and record why each attempt failed, by cause; harness bugs can make a writer look stuck or make good items fail.",
   "kind": "measured",
   "found_by": "An earlier AP question-generation effort spent weeks 'stuck at 28%' that were four harness bugs; a later grader false-failed multi-answer keys and could not score matching items at all.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "76",
     "quote": "aptraining burned weeks \"stuck at 28%\" that were **4 harness bugs** (wrong field read `overall.score`, grader on wrong host, MCQ_SET mis-route 0→0.77, DBQ truncation at low max_tokens)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "76",
     "quote": "**Bucket failures by type** (gen-fail vs transport-5xx vs schema-fail), not one boolean"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "126-129",
     "quote": "The first grader run false-failed some MSQ/EBSR candidates because `_resolve_key` handled JSON-array keys but not comma-separated legacy strings such as `\"a, b\"` or `\"a,d\"`. The staged `anti_leak_grader.py` accepts both. `match` items still did not survive because the current checker is MCQ-style and does not model pair-key scoring."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38,
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before using a cheap heuristic as a gate or reward, measure whether it actually separates good items from bad.",
   "kind": "measured",
   "found_by": "Keyword heuristics proposed as reward terms were re-measured on verified items: one never fired and the other separated leaky from clean items at about chance.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "170-171",
     "quote": "**`cold_passage_bonus` fires 0% of the time** on the 163 verified items (near-useless on this genre); **`curriculum_penalty` separates leaky from clean by only +0.018** (AUC ~= 0.5)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "181-182",
     "quote": "Tier A+ (a cheap distilled passage-blind classifier, gated at AUC >= 0.80 before use)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/llm/LLM_SPEC.qmd",
     "lines": "125-126",
     "quote": "**Component 2 — Curriculum penalty (new)** Score contribution: −0.2 if passage hits any curriculum fingerprint; 0.0 otherwise."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Recompute every property a writer reports about its own output — length, reading level, quoted spans, counts — before gating on it; a partial-substring 'verbatim' check passed paraphrases.",
   "kind": "measured",
   "found_by": "A measurement review found generator-asserted lengths and levels trusted and a 30-character substring check defeated by paraphrase; a later handoff corrected two agent-reported numbers; generated passages leaked harder vocabulary on a first pass.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "95-99",
     "quote": "they trusted generator-asserted `word_count`/Lexile and a 30-char substring \"verbatim\" check (defeated by paraphrase). Our contract has the same shape. Action: independently recompute Lexile, word_count, hot-text/EBSR spans (NFKC exact-match against the tokenized passage), answer-checkability at intake; any self-reported field used as a gate is UNVERIFIED."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "168-169",
     "quote": "re-measures every agent-reported number independently rather than trusting it, and corrects two:"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd",
     "lines": "147",
     "quote": "fluency passages regenerated after a first pass leaked Tier-3 vocabulary;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    61,
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fix a writer's format errors by putting worked examples of the format in its prompt before retraining it.",
   "kind": "measured",
   "found_by": "In an earlier AP question-generation effort, few-shot exemplars fixed answer balance by 23 points with no retraining.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "88",
     "quote": "Mirrors aptraining [F5]: **few-shot exemplars fixed MCQ_SET answer-balance with NO retrain (+23pp)** — try in-context format exemplars before reaching for SFT."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    62
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When choosing examples to train or tune a writer, choose them on the quality you actually want, confirmed by an independent judge, not on a convenient proxy score.",
   "kind": "measured",
   "found_by": "An earlier AP question-generation effort hit a quality wall because preference pairs were picked on a proxy judge's axis; fixing the labels beat two retraining attempts that both regressed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "94",
     "quote": "aptraining's MCQ_SET wall was a **mislabeled-preference-data** problem (pairs picked on the IB axis, never verified on the true `educational_accuracy` axis) [M3/M8] — fixing the *data labels* beat 2 SFT warm-starts (both regressed, [M6])."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Set a judged pass bar against the judge's own agreement ceiling and a chance baseline, not at a near-perfect target the judge itself cannot reach.",
   "kind": "adopted rule",
   "found_by": "A lesson carried over from an earlier AP question-generation effort into the generator improvement plan.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "78",
     "quote": "**Define the eval contract up front** (oracle ceiling, class-prior baseline, shortcut-learning guard) — aptraining [P8]. On any format where judge self-agreement is low, the bar is `ceiling − margin`, not 99%."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Do not estimate a course's effect by simulating students with a model — simulated scores come from the model's pre-training and the imposed models — instead ask the model to predict where students will struggle, and check any prediction against real outcomes.",
   "kind": "adopted rule",
   "found_by": "The course-build repo's prediction engine was designed after research summaries and an in-house 100K-agent AP simulator whose scores came from pre-training; its outputs still await validation against real students.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
     "lines": "74",
     "quote": "Running 100K simulated students yields **zero new information** — outputs are determined by the imposed math models + pre-training."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
     "lines": "76",
     "quote": "100K-LLM-agent AP simulator (AP-score-from-pre-training artefact problem)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
     "lines": "84",
     "quote": "no self-validation (outputs must be validated against real student outcomes — Phase 6)."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md lines 313-315: \"practice/thin-instruction shapes fail; only the full student-ready candidate passes the simulation. This is design evidence, not live child-outcome proof.\" — persona simulation is still used as a design stress test.",
   "adds_to_existing": [
    47,
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A model's score on pedagogy-knowledge tests does not show that its generated material embodies that pedagogy; judge the material itself.",
   "kind": "adopted rule",
   "found_by": "The project's doctrine rejects pedagogy-benchmark scores as teaching evidence, including for the team's own benchmark paper, which states the same limit.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "35",
     "quote": "Knowing-that (answering pedagogy questions) and generating-aligned (producing content that embodies the pedagogy) are different capabilities; the gap is invisible to benchmarks and only measurable at the artifact level."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "256-257",
     "quote": "filed with its own caveat that benchmark PCK ≠ teaching ability"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "65",
     "quote": "REJECTS pedagogy-benchmark scores as teaching evidence."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Run independent adversarial checks on every generated artifact before a student sees it; design-time instructions to the writer did not prevent systematic leaks or answer-position bias.",
   "kind": "measured",
   "found_by": "Most raw generated items were answerable without the passage and most keys sat at one position even though the writer's contract forbade both; recurring defects passed every structural validator and were caught only by a machine ear, a human eye or an adversarial pass.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "23",
     "quote": "Generation systematically betrays declared pedagogy — \\~78% of raw generated reading items were answerable without the passage, correct answers sat at position A 79% of the time, and a dose that \"knew\" gradual release still leaked its item's answer — and design-time contracts alone demonstrably failed to prevent any of it."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "15-16",
     "quote": "Each is the kind of defect that leaves every text/structural validator green — only a machine ear, a human eye, or an adversarial pass caught it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    8,
    62
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Classify each item as a knowledge check or a transfer item before judging its overlap with the lesson: being answerable from taught content is correct for a knowledge check and a leak for a transfer item.",
   "kind": "measured",
   "found_by": "It took five adversarial rounds to see that the same overlap was right in one item class and a defect in another; the anti-leak filter removed nearly all knowledge-recall items by design.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "36",
     "quote": "An in-lesson knowledge check answerable from explicitly-taught knowledge is legitimate (that's what checking taught knowledge means); the same overlap in a comprehension/transfer item is a leak. Mis-classifying the item makes the same text both correct and defective — it took five adversarial rounds to isolate this."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "73-75",
     "quote": "KCT1 (domain-knowledge recall) is ~0 **by design** — passage-independent items are exactly what the anti-leak filter removes; covering KCT1 needs a different item design (generation), not relaxed gating."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A teaching policy written into prompts that steers one model may not carry over to another model; qualify each model separately before relying on it.",
   "kind": "measured",
   "found_by": "A prompt-level pedagogy control experiment failed exact cross-model portability (worst route 0 of 20 against 20 of 20) even though prompt-local steering worked.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "110-114",
     "quote": "adjacent A-only A1b completed 420/420 valid rows and failed exact cross-route portability: worst route 0/20 against 20/20. OpenAI and Claude each had 0/20 robust clusters; DeepSeek had 17/20. **BOUNDED POSITIVE:** the post-hoc semantic-facet diagnostic was 119/120. Prompt-local steering is real, but exact execution, negative-control locality, and invariant preservation were not portable."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "130",
     "quote": "bank but questioned universal cross-model transfer and expected model-by-model qualification."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep content changes as replayable edit operations and hash content files before and after any automated multi-agent work; telling an agent not to edit content does not stop it.",
   "kind": "measured",
   "found_by": "A fan-out agent overwrote a lesson file from a stale snapshot despite an explicit 'never edit' instruction; it was caught only because a count moved by one.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "149",
     "quote": "**Root cause:** a prompt instruction is not a write guard — a fan-out's Bash has the same filesystem"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "152-155",
     "quote": "before any fan-out that touches harnesses/tests, record `md5 -q public/lesson-json/grade-3.json` (and any other content file); re-check it when every agent returns and treat any change as an incident (re-apply from saved ops files, never hand-patch). Keep every content mutation as an ops file under the batch record (`apply-ops.py`) so re-application is one idempotent command."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When building from source material, give every input an explicit disposition — used, merged, split or skipped with a reason — because silent drops are the most common failure.",
   "kind": "adopted rule",
   "found_by": "Rule set for staging source dumps into the knowledge store.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/ingest-triage/SKILL.md",
     "lines": "22-23",
     "quote": "**Every input file gets a disposition line** in the final report — extracted, merged, split, pre-digested, skipped (with reason). Silent drops are the #1 triage failure."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When summarising sources, never pad a thin source, take numbers, names and dates verbatim, and spot-check model-written summaries against their sources.",
   "kind": "adopted rule",
   "found_by": "Ingestion rules written after model agents reported writes that never happened and summaries needed checking against sources.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/ingest-batch/SKILL.md",
     "lines": "33-34",
     "quote": "**One source → one entry. No invented facts.** A thin source gets a short entry — never pad. Numbers, names, dates come from the source verbatim."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/ingest-batch/SKILL.md",
     "lines": "125-126",
     "quote": "Spot-check ONE entry per batch by reading it against its source: numbers, names, and dates must match. Fabrication found → fix from the source, and say so in the report."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/templates/entry.template.qmd",
     "lines": "15-17",
     "quote": "Keep every fact; fix obvious formatting; drop boilerplate and noise. Preserve code blocks, lists, tables, and numbers verbatim. Do not invent anything that is not in the source."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Any claim about research carries its source and locator together with the source's limits, and a source is read before it is cited, never cited second-hand.",
   "kind": "adopted rule",
   "found_by": "Rules of the project's quote-verified research folder.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/SKILL.md",
     "lines": "32-34",
     "quote": "**Cite, don't vibe.** Any externally visible claim about reading science must carry a source + locator from SYNTHESIS/DIGEST files. If it's not in the folder, don't imply the literature says it."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/SKILL.md",
     "lines": "38-39",
     "quote": "**Don't cherry-pick.** SYNTHESIS.qmd has a \"What complicates knowledge-first\" section. If you cite the supporting evidence externally, know the limits listed there"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd",
     "lines": "79-80",
     "quote": "If an argument needs one of these directly, ingest it first (knowledge-ingest skill) rather than citing it second-hand."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Research behind a design is not evidence that your implementation works; outcome claims need an outcome measurement of your own material.",
   "kind": "adopted rule",
   "found_by": "Honesty rules attached to the evidence base and to the course-quality standard.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd",
     "lines": "82-83",
     "quote": "this corpus grounds DESIGN, it does not prove OUR implementation works. Never cite it as evidence about our courses' outcomes."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/knowledge-[name]-additions/docs/standards/course-quality.qmd",
     "lines": "81",
     "quote": "Synthetic prediction, IB scores, or reviewer approval are not outcome evidence."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "126",
     "quote": "Do not claim RIT/proven impact before a real linked/piloted outcome source exists."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Use only item types proven to render and score in the real student player, and keep a fallback for the rest; formats that validate and upload can still show blank or be unanswerable.",
   "kind": "measured",
   "found_by": "Live probes found three interaction types rendering blank after a successful upload, multi-select rendering as single-select, and a production course that had never rendered an interactive item, so a fully certified form could not be delivered.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd",
     "lines": "116-117",
     "quote": "**R3 — `match`, `hot-text`, `text-entry` render BLANK.** They push fine (201, valid QTI, GET 200) but the quiz body is empty — must be transformed to single-select choice."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "68-71",
     "quote": "a live probe found the PRODUCTION TimeBack G3 Reading course is **1,077 items, 100% `cardinality=single`, zero TE ever rendered**. Our G5 contract hard-requires all six formats + 40% TEI → we can fully certify a form that **physically cannot be delivered**."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0020-incept-timeback-plugin.qmd",
     "lines": "21",
     "quote": "items that return `200 OK` but render broken/empty in the student UI, silent data loss on updates, etc."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0022-incept-team-sync-2026-06-17.qmd line 33: \"All-MCQ/MSQ is a fallback only.\" — the team refused to restrict a course to the formats the player already supported.",
   "adds_to_existing": [
    46,
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Validate with the same logic the delivery engine uses, not a looser stand-in; a substring check passed evidence spans the engine could never highlight, and file checks passed audio that no check ever opened.",
   "kind": "measured",
   "found_by": "Clue spans passed a substring check but never highlighted for students; eleven clips saved as raw audio under the wrong format passed three validators because none opened the file.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "111-113",
     "quote": "**Root cause:** `validate-passage-refs` only proves the span text is a SUBSTRING of the passage; it does not run the engine's own unit-boundary logic (`unitsOf`/`partOfLine`), so a span that is textually valid but unit-misaligned passes the validator and silently fails the student experience."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
     "lines": "94-96",
     "quote": "**Eleven you-do aux clips were raw PCM saved under `.mp3` names** (`out.write_bytes(audio)` ran because the cutting shim had no `write_mp3`) — browser fired media errors on the first found reply; `validate-assets`, voice-provenance and voiceover-sync were all green because none of them opens the file."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prove appearance with a rendered look and interaction with a live walk-through; a markup assertion proves neither, and a screenshot does not prove interaction.",
   "kind": "measured",
   "found_by": "A layout fix passed its markup assertion but rendered wrongly and was caught only by a screenshot; a key-set comparison missed mid-page steps that only a live walk exposed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "139-140",
     "quote": "Lesson: any shell/layout change gets a rendered look (screenshot or computed layout of the control) before the PR, not only a markup-presence assertion."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/app-package-agent.md",
     "lines": "46",
     "quote": "Stop if screenshots are being used as proof of interaction."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0193-g3-book-grade-agnostic-vs-specific-g9-checklist.qmd",
     "lines": "170-172",
     "quote": "a key-set diff alone misses mid-page beats (best-pick, a reread hold, a follow-up ask) — walk the live page with a Playwright driver per mechanism, not just diff JSON."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fix content where it is authored and regenerate every derived copy; edits made to a deployed or rendered copy are overwritten by the next import or regeneration.",
   "kind": "measured",
   "found_by": "Edits to a deployed course were at risk of being reverted by a scheduled re-import; the content-integrity workflow found rendered fixes do not close a bad specification.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0060-incept-read-app-field-notebook.qmd",
     "lines": "74-75",
     "quote": "**Gotcha:** the allqtypes course is **re-imported on a schedule** → `primaryApp` edits may be reverted; needs to land in the upstream import source."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "44-46",
     "quote": "Upstream generation specifications are active content authorities. Include them in governed Course JSON extensions. A rendered lesson that silently fixes a bad specification does not close the upstream defect because regeneration can reintroduce it."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/curriculum-agent.md",
     "lines": "31",
     "quote": "7. Regenerate all downstream graph and reviewer views; do not edit mirrors independently."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When an upstream fact or specification fails, mark every dependent lesson, item, chart and feedback as stale, repair the source, regenerate, and rerun every check on the new versions.",
   "kind": "adopted rule",
   "found_by": "Content-integrity and passage-integrity lanes written to stop a false specification from propagating into later units.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "193-198",
     "quote": "When an upstream spec fails: mark dependents stale; repair the upstream object, not only rendered copies; regenerate descendants; rerun every named checker on the new hashes."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
     "lines": "34-35",
     "quote": "6. Propagate any upstream failure through every declared dependent lesson, item, chart, and feedback object."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep each number, rule and setting in one canonical place that everything else points to or is generated from; parallel copies drift apart.",
   "kind": "measured",
   "found_by": "A measurement review found scoring method, blueprint and item counts specified differently across files, with a wrong string reaching the gradebook; this audit found two documents staged in the same proposal disagreeing on which standards a generator may target.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "100-103",
     "quote": "their biggest systemic failure is spec INCOHERENCE (scoring method, TEI floor, blueprint, item count specified ≠ across files; a wrong string reached machine-consumed gradebook fields). Our kb-0069 drift risk, concrete. Action: one canonical numbers block per course; all other docs POINT to it; a cheap CI consistency check."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/assessments/G5_PARAMETERS.md",
     "lines": "61",
     "quote": "| `RI.5.7` | **EXCLUDE from single cold-text generator** — drawing on multiple print/digital sources / visual info. | NO for single-passage |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/COURSE_SKELETON.md",
     "lines": "78",
     "quote": "| E1 | L4 Two-text integration (food web + article) | RI.5.9, RI.5.7 | 8M · 2Q · 3H · 2A | 870L | 15 |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Derive structure from the content itself instead of keeping hand-maintained registries of it; registries went stale silently on a reshape, and a validator that keeps them in sync only patches the duplication.",
   "kind": "measured",
   "found_by": "A lesson reshape left three code registries stale so earned credit silently vanished; a sync validator was rejected as a bandaid in favour of deriving from the content; an emitted copy of the lesson file once disagreed with its own titles.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "93-94",
     "quote": "The failure mode was NOT an error: evidence simply wrote a no-op and provenance came back empty, so nothing looked broken until a human noticed missing credit."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "96-98",
     "quote": "\"this is a bandaid, not the solution\" — it fails loud, which is strictly better than silence, but it leaves the duplication in place and adds a fourth thing to maintain. **Real fix:** delete the registry; derive ownership from the node's own shape"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0191-g3-book-lesson-anatomy.qmd",
     "lines": "32-36",
     "quote": "Reintroducing an author script that emits `grade-N.json` is explicitly forbidden (AGENTS.md): it happened once, and a unit's lesson-title summary disagreed with the lesson's own title because the emitted JSON had drifted from the hand-edited contract."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check counts, versions and file references in documentation against the delivered files before trusting them; a reader who trusts a stale description plans against material that does not exist.",
   "kind": "measured",
   "found_by": "Live course counts diverged from the manifest and the package; a reference course's map named files and item counts that were not on disk; a file count disproved a 'complete' audio claim.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "498-499",
     "quote": "**Course truth (live):** 745 items / 52 tests / 13 units / 56 stimuli (`kb-0058`) — **diverges** from the manifest (`kb-0014`: 703/47/10) and the QTI pkg (`kb-0004`: 576). Confirm which is canonical."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/course-layout.md",
     "lines": "102-103",
     "quote": "These are honesty-discipline failures of the same family as content drift: a reviewer who trusts the README plans against a test that doesn't exist."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "118-119",
     "quote": "corrected a prior false claim (\"U4L1 through U4L9 complete\"): **only 6 of 12 built lessons have any audio at all.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before relying on a check's recorded result, confirm the checker exists, still runs and still has the files it ran on; recorded passes and cited harnesses can outlive their files or never have existed.",
   "kind": "measured",
   "found_by": "This audit compared records with disk: a pinned tooling manifest lists 23 files and a selftest pass over 9 fixtures, but 20 files remain (two failing fixtures and the schema are gone); a quote-verification record of 271/271 stands while 3 of its 6 source texts and its synthesis file are missing. Separately the project found a cited blind-solve harness was a phantom.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling-manifest.json",
     "lines": "11",
     "quote": "\"result\": \"PASS: 9 fixtures; all six rules exercised with failing cases\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/EXTRACTION_EVIDENCE.qmd",
     "lines": "32-34",
     "quote": "**Quote integrity:** 230/230 extracted quotes verified verbatim at extraction time (`verify_quotes.py --json claims.json`); **271/271** quoted spans verified in the rendered SYNTHESIS + DIGEST files"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "113-114",
     "quote": "no runnable blind solver existed in-repo at merge time (the \"Claude-strong harness\" referenced was a phantom;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make narration match the printed text sentence for sentence — nothing spoken that is not printed — because paraphrased narration drifted unnoticed while other checks passed.",
   "kind": "measured",
   "found_by": "Two pages drifted into a paraphrase of their own narration across 16 lines while every other validator passed; a read-along check was added.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "153-156",
     "quote": "**never speak words it does not print** — a spoken line with no printed home highlights nothing and cannot be tapped to hear again. This was a real, fixed bug: two pages had drifted into a paraphrase of their own spoken script, 16 lines between them, while every other validator passed."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "129",
     "quote": "(the read-along rule — nothing may be spoken that is not printed, sentence for sentence);"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd line 47: \"Combine verbal and visual when both add value. Avoid redundancy.\" — tension with full redundancy between voice and print.",
   "adds_to_existing": [
    53,
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a narration clip is missing, show the text silently rather than falling back to a synthetic voice, and record why each deliberate silence exists.",
   "kind": "adopted rule",
   "found_by": "A first build spoke with browser speech synthesis and was rejected on hearing; the rule and a required reason for every silent node followed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "33-35",
     "quote": "(2) a missing clip is SILENCE with the caption text visible — never a `speechSynthesis` fallback; (3) dynamic strings (interpolated answers, live feedback) render as text bubbles only, never synthetic speech;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "40",
     "quote": "every silent node must say WHY"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    2
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Generate captions from the approved script and the measured clip, and give every video that gates progress a caption track.",
   "kind": "adopted rule",
   "found_by": "A unit video gates the first lesson, so captions are the only way through for a student who cannot hear; hand-written captions are not allowed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "182-189",
     "quote": "captions are NEVER hand-written. `scripts/generate-video-captions.mjs` derives a WebVTT track from the authored `transcript[]` (the script a reviewer signed off) plus the clip's real measured duration via `ffprobe`, written next to the clip and pointed at by `captions_path`. `validate-contracts.mjs` fails a unit video with no caption track, because a unit video gates the hero pick, which gates lesson one — captions are the only way through for a child who cannot hear, not an accessibility nicety."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    53,
    27
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Set age-specific settings — voice, pace, tone — deliberately for each new grade; silently falling through to another grade's defaults produces plausible but wrong material.",
   "kind": "measured",
   "found_by": "A grade nearly shipped narration in a younger grade's storytime pace; a rebuilt lesson passed every validator but broke live because of a hard-coded grade; voiceless purpose lines fell through to the wrong narrator.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "72-77",
     "quote": "**No grade-9 entry exists.** Without one, G9 clips would silently fall through to `DEFAULT_VOICES`/`DEFAULT_STYLE` = grade 4's child voice and storytime pace — \"silent and plausible,\" per this same file's own comment about the identical mistake almost shipping for Grade 5 (\"a ten-year-old reading about salinity gradients would have been read to as if this were a bedtime story\")."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0193-g3-book-grade-agnostic-vs-specific-g9-checklist.qmd",
     "lines": "25-28",
     "quote": "a G5 rebuild passed every content validator and its unit test, yet the live page silently broke, because `bookCompoundResume.ts`'s `frameBlankInput()` hard-coded `grade: 3`"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
     "lines": "68-69",
     "quote": "L4's three purpose lines re-voiced to Scout (were bare stubs with no `voice` field, so the generator fell through to the narrator)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write a tone and register standard for each age group as a content standard separate from the mechanics, and do not inherit another age group's tone.",
   "kind": "adopted rule",
   "found_by": "Transferring a lesson shape to an older grade showed register (no cheerleading or confetti, short feedback, hedging allowed) lived entirely in content, not code; the transfer checklist requires a new register document per grade.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0193-g3-book-grade-agnostic-vs-specific-g9-checklist.qmd",
     "lines": "122-127",
     "quote": "**Register/content differences are separate from mechanism differences.** The build spec's \"Register (Grade 5)\" section (no \"You did it!\", no medals/confetti, ≤40-word feedback, epistemic hedging allowed, more writing than G3, retell demands taught terms) is entirely a CONTENT authoring standard, not a code change — it lived in the page files' prose, never in the renderer."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0193-g3-book-grade-agnostic-vs-specific-g9-checklist.qmd",
     "lines": "134-136",
     "quote": "**Register/pedagogy standard first**, separate from mechanism: define a G9-appropriate voice/tone doc (the G5 build's §3 register rules are the template for this document's shape, not its content — G9 needs its own,"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When one instance of a defect turns up, search the whole course for the same pattern before calling it a one-off, and turn a recurring defect into a standing check for its class.",
   "kind": "measured",
   "found_by": "A narration defect was patched as one-offs for weeks before a class-level check was built; one swallowed spoken header led to a census of all similar openers; a gameability fix was followed by a sweep of all related items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "27-28",
     "quote": "Once one instance is found, census ALL colon-openers in the grade JSON rather than assuming a one-off;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "78-79",
     "quote": "Voice defects repeated as one-off fixes for weeks (wrong/different voice on 2026-09-04 twice, 2026-09-07, 2026-09-21)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0211-peter-pan-reviewer-round-2708.qmd",
     "lines": "24",
     "quote": "a gameability sweep over all 31 L4+L5 MCQs found no other cross-form tell"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd lines 28-29: \"some renders do voice the header anyway, so check transcripts per case, don't blanket-assume.\"",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After any fix, rerun every check, not only the one aimed at the fix.",
   "kind": "measured",
   "found_by": "A narration fix passed every targeted check and broke a different validator.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "101-103",
     "quote": "Run per lesson immediately after cutting, and run the FULL suite before commit, not just the targeted verifier — PR #240 shipped a listen-fix that passed every targeted check but broke `validate-voiceover-sync`."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a check fires on a large, seemingly random share of items, suspect the check before the content.",
   "kind": "measured",
   "found_by": "An audio-onset check flagged 31 of 123 clips, all falsely, because it measured from the wrong point.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "85-88",
     "quote": "an onset-audibility check flagged 31 of 123 clips \"WEAK ATTACK,\" all false, because it measured loudness from the universal 0.28s lead-in at t=0 instead of from the actually-detected speech onset — fixed by measuring from detected onset, not from t=0 (an onset detector firing on 25% of clips at random was itself evidence the check, not the audio, was broken)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a check that found nothing to check (zero passes, zero failures) as broken, not passed.",
   "kind": "measured",
   "found_by": "A per-file gate reported 0 pass / 0 fail because every file lookup missed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "185-186",
     "quote": "never read a 0/0 verdict as green — treat it as a harness bug until proven otherwise."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a check fails falsely, fix the checker; never loosen the assertion to get a pass.",
   "kind": "adopted rule",
   "found_by": "A lesson walker went through sixteen versions, each fixing a false negative in the walker itself; test pins are re-set only for changes the diff explains.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
     "lines": "112-114",
     "quote": "**Driver** (Playwright-based walker) evolved v10.1 through v10.16 across the campaign, each version fixing a false-negative in the driver itself (nested-rail host filtering, we_do adapter, popover-close timing, bold-text normalization, reset-detector logic) — never by loosening an assertion."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "135-136",
     "quote": "never loosen a pin."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Before blaming your change for a failure, rerun the same check on the unchanged baseline; a failure that reproduces there is inherited.",
   "kind": "adopted rule",
   "found_by": "Repeated conflict rounds were spent fixing failures that already existed on the shared baseline; a classification recipe followed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
     "lines": "54-57",
     "quote": "Classify every red before touching it: extract `origin/staging` to a scratch tree (`git archive origin/staging | tar -x -C /tmp/stg-<sha>`), symlink `node_modules`, run the same test — a red that reproduces there is inherited (register it, never fix it); a red only on the combination is ours."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
     "lines": "75-76",
     "quote": "**Claim: this branch adds no failure beyond staging's own inherited reds.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Trace where a checker's threshold came from before acting on its failures.",
   "kind": "measured",
   "found_by": "An auditor failed every one of 81 item banks against an arbitrary constant that the specification merely quoted; against the real floor, 79 of 81 passed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "136-139",
     "quote": "the auditor's `thin_banks`/`enforcement_broken` FAIL (81/81) traced to an arbitrary `>=15` bank-depth constant hardcoded in `audit_compliance.py` itself (circular — the spec just quotes the auditor); the real platform/publisher floor is 8. After correcting the bar, 79/81 banks pass; 2 genuinely fall below 8 (a real, small, named gap)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A required check that has not run counts as not passed: report it as unverified, never as a pass, and state missing evidence rather than leave the line blank.",
   "kind": "adopted rule",
   "found_by": "A blind-solve gate that was skipped had been read as clean; the standards then made an un-run check a fail and an empty line 'unverified'.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "63-64",
     "quote": "**`NEEDS_LLM_GRADE` (the blind solve not run) is a FAIL, not a pass.**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/non-negotiables.md",
     "lines": "61",
     "quote": "No line may be left blank; absence of evidence is `UNVERIFIED`, not silence."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/docs/standards/course-json/README.md",
     "lines": "283-284",
     "quote": "If no suitable check exists, the contribution stays pending and the missing check is stated in the PR. Agents must not invent a passing verdict."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9,
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep model calls out of the pass/fail gate: freeze judged inputs with their evidence before the gate runs, so the same inputs always give the same verdict.",
   "kind": "adopted rule",
   "found_by": "Gate contract in the staged course standard.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/README.md",
     "lines": "60",
     "quote": "Same `course_id` + same `COMPLIANCE.md` + same referenced artifacts → same verdict and exit code. No model calls in the gate path; any machine-judged input must already be frozen into the ledger with its evidence tag before the gate runs."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count a change as done only when a check confirms it on the delivered state and the status quotes the exact field or line that proves it; success codes, 'looks fine' and an agent's report are not evidence.",
   "kind": "measured",
   "found_by": "Writes returned success and silently reverted; agents reported files written that never existed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "13-15",
     "quote": "\"done\" is what the **deterministic check confirms on live state**, never an agent's claim or an HTTP 200 — a PUT can return 200 yet silently revert. Re-read via GET / `process-response`."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/ingest-batch/SKILL.md",
     "lines": "25-26",
     "quote": "**Never trust a subagent's success claim.** Subagents have returned `wrote: true` for files that never landed."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/templates/COMPLIANCE.template.md",
     "lines": "32-33",
     "quote": "verbatim line/figure that proves the status. \"Looks fine\" is not evidence."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fix flawed items in place or add new ones, citing the principle behind each fix; never pass a check by deleting hard items, and test every change against a frozen baseline of item ids.",
   "kind": "adopted rule",
   "found_by": "Compliance could be faked by deleting hard items, so a no-cut gate against the source's item ids was added.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "34",
     "quote": "item-count + per-lesson item-id set ≥ a frozen source baseline; no validated item dropped/replaced — fixes are in-place or pure-add. `--assert-no-cut` → `no_cut_ok:true`. *(new — the hard rule; without it \"compliance\" can be faked by deleting hard items)*"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md",
     "lines": "16-19",
     "quote": "**Never cut / drop / replace a question.** Every item passed validation — it is good content. The only allowed operation is **fix-in-place** (edit metadata / passage / rawXml / wiring of the SAME item) or **pure addition** (new items for spacing/forms). Restoring a validated original counts as a fix. **Every fix cites a knowledge_bot principle** (kb id) as its justification."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When fixing material, list the verified-correct neighbouring decisions not to touch so the fixes don't regress them, and keep refuted challenges on record.",
   "kind": "adopted rule",
   "found_by": "A lesson audit's patch pass named five do-not-touch decisions and kept five refuted attacks with evidence.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "74-75",
     "quote": "Five \"do-not-touch\" items were explicitly called out so a later patch pass wouldn't regress a verified-correct decision while fixing an adjacent F-id"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "45-47",
     "quote": "**challenged and upheld** (an attack raised during the lens audit was refuted on re-verification — 5 such entries collected with file/line evidence as a diligence record, not noise)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Review the student view through a dedicated test account, never by impersonating a real student.",
   "kind": "adopted rule",
   "found_by": "The only route to the real student render listed real student accounts; that line was not crossed and a sandbox test account was recommended.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0241-alpha-read-contract-investigation-and-packager-build-2026-06.qmd",
     "lines": "121-124",
     "quote": "the only path to the real render is **Impersonate/View as Student**, which lists real student accounts -- **that line was not crossed**. Recommended safe resolution (not yet executed at this draft stage): provision a dedicated sandbox test-student account and impersonate that, never a real child."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prove one complete lesson through every check before producing the whole course; a pilot proves the format, item quality and auditability, not the course.",
   "kind": "adopted rule",
   "found_by": "A question-only pilot passed the quality judge but half failed structural checks and lacked provenance files, so the standards made pilot-before-scale a rule and delivery plans start with one audited slice.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/knowledge-[name]-additions/docs/standards/course-quality.qmd",
     "lines": "57",
     "quote": "Pilot before scale. A pilot proves schema, item quality, and auditability. It is not a course."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "156",
     "quote": "48 hours for one audit-clean 6-7 lesson vertical slice"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "164-166",
     "quote": "Replace all priors at the 48-hour vertical-slice gate. A missed gate changes the date, never the quality bar."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Finishing authoring is not readiness: expert subject review, source and rights review, accessibility, assessment certification and checks in the real delivery system are separate later gates.",
   "kind": "measured",
   "found_by": "An AP course passed full validation and every deterministic contract, yet an independent read blocked it on six content buckets and five readiness gates stayed open.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "36-38",
     "quote": "**NEXT GATES:** named human academic/historical review, source-line and rights review, accessibility, independent assessment certification, and target-runtime import/render/scoring. These are later readiness gates, not missing lessons."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "48-50",
     "quote": "**APUSH:** nine-unit architecture and deterministic Unit 1 contracts pass, but the independent read says BLOCKED FOR REPLICATION on six concrete content, release, source, correction, rubric, and student-projection buckets."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep three kinds of checks apart — content checks on the files, behaviour checks in the live player, claim checks on the package — and never let one stand in for another.",
   "kind": "adopted rule",
   "found_by": "An evaluator gap analysis split criteria into three rings after artifact-level evaluators were overclaiming runtime behaviour.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "52-53",
     "quote": "This boundary matters. InceptBench should not overclaim runtime behavior or package truth. It should get the artifact-checkable layer much stronger."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/TOOLING.md",
     "lines": "58-59",
     "quote": "Neither tool replaces item anti-leak certification, live student-seat verification, formal accessibility review, academics approval, or learner-outcome evidence."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Item-level quality scores do not measure sequencing or knowledge-building; lessons judged weak as wholes can be made of items that pass.",
   "kind": "measured",
   "found_by": "A lesson-level run of the quality evaluator rated 73 of 76 lessons inferior while their items passed; the benchmark was found to measure isolated content, not sequencing.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "361-362",
     "quote": "clone-lessons run (IB 2.7.5): **73/76 lessons INFERIOR** at lesson level while items pass — never claim course-level IB; internal-only number."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "232-233",
     "quote": "It measures isolated question/lesson content but **not sequencing or pedagogy** → the eval framework is slated to grow to assess lesson sequencing + knowledge-building across units"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A course teaches; it is not a series of practice tests — test at set points, and present test-practice products as practice, not instruction.",
   "kind": "adopted rule",
   "found_by": "Reviewers called an early build a well-made test-practice engine rather than a curriculum; the team then aligned on teaching-based, not drill-based, courses.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "227-229",
     "quote": "G3 course strategy is **teaching-based, not drill-based** — practice tests only at specific intervals;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "290-291",
     "quote": "MAP/practice apps must stay framed as practice/assessment, not instruction."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
     "lines": "50",
     "quote": "Assessment format is not instruction format (the marathon rule), and acquisition mastery is not durable mastery — they need different instruments"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Do not let one assessment format become the definition of the skill; a single format washes back into shallow teaching, and no single assessment serves every purpose.",
   "kind": "external research",
   "found_by": "A research-agenda report summarized in the project's evidence base (https://www.rand.org/pubs/monograph_reports/MR1465.html, as listed in sources.qmd).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "699",
     "quote": "**114. Defaulting to 'read a passage, answer a few multiple-choice questions' as the operational definition of comprehension gives teachers little incentive to teach toward a deeper, more accurate conception of the construct.**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
     "lines": "759",
     "quote": "**124. No single assessment can satisfy all these requirements; the RFA instead calls for building an integrated system of multiple assessments serving different purposes (accountability, diagnosis, instruction-guidance) and different reader groups.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Read outcome data by cause: low effort points to motivation, accuracy far too high or too low points to placement, and completion without later test gains points to the instruction.",
   "kind": "adopted rule",
   "found_by": "The delivery platform's diagnostic guidance, adopted with its closed-loop bar.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0031-how-it-works.qmd",
     "lines": "136-138",
     "quote": "**Motivation issues** (low minutes, high waste, inconsistent effort): the problem is upstream of your content **Placement issues** (accuracy too high or too low): students are in the wrong place in the curriculum **Curriculum issues** (students complete content but scores don't improve): your instruction needs work"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "After a failed test, teach only what was missed and retest before the student advances.",
   "kind": "adopted rule",
   "found_by": "The delivery platform's hole-filling rule, part of the evaluation dimensions the project adopted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0031-how-it-works.qmd",
     "lines": "156",
     "quote": "the platform analyzes which standards were missed and generates a **targeted remediation course** containing just the lessons needed to fill the specific gaps. The student completes the hole-filling content, retests, and"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0026-evaluating-apps.qmd",
     "lines": "24",
     "quote": "| **Hole-filling compatibility** | Targeted remediation is possible when gaps show up |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Measure how much of the intended work students actually complete, and when completion is very low fix completion before tuning item quality.",
   "kind": "measured",
   "found_by": "Incumbent-course data showed a 12.5% completion floor, so the redesign led with a daily completion mechanism before accuracy work.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
     "lines": "122",
     "quote": "2. **Dosage-first** — daily 25-min/25-XP doses lead; completion mechanics before accuracy lifts (cohort floor is 12.5%)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "After a wrong answer, diagnose, reteach a different way and retry on a parallel item of the same difficulty; never re-serve the identical item or hand over a harder one.",
   "kind": "measured",
   "found_by": "An incumbent course raised difficulty after a miss and second-attempt accuracy on that skill fell from 64% to 41%; the redesign locked in reteach-first retries on parallel items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "37",
     "quote": "Difficulty escalates after a miss; attempt-2 supporting-detail accuracy **64% -> 41%**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
     "lines": "57-58",
     "quote": "Remediation map with retry limits, alternate instruction, a new parallel check, and wheel-spinning escalation."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
     "lines": "44",
     "quote": "7. misconception-specific correction and a new parallel check where required."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Switch off supports such as word help during scored steps.",
   "kind": "adopted rule",
   "found_by": "A course design locked word help on for practice steps and off for scored steps.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "165",
     "quote": "Word Assist boundary: click-any-word audio definition ON in dose steps 1–4, OFF in scored steps 5–6, in every band."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "Screen every generated text for age-appropriateness and sensitive content, and check the writer's grade or level setting before generating.",
   "kind": "measured",
   "found_by": "A design review found the generator set to grade 11 for a grade-3 course and added a mandatory age and sensitive-content screen.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0079-g3-rex-v2-case-for-approval-2026-07-02-[name]-submission-brainlift.qmd",
     "lines": "165",
     "quote": "mandatory age-appropriateness/sensitive-content screen on every auto-generated passage; fix generator grade setting (was grade 11 -> grade 3)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    19,
    63
   ],
   "name_bearing_source": true
  },
  {
   "statement": "Measure growth with tests given before and after the course and separate from it, and put scores on an external scale only through a dual-tested linking study (about 200 students, tails oversampled, link error reported), with scale scores blocked in code until then.",
   "kind": "adopted rule",
   "found_by": "The platform runs pre/post tests outside the course; a parallel measurement effort specified the linking protocol and enforced its no-scale-score rule in code, which the project adopted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0016-timeback-alpharead-publishing-playbook.qmd",
     "lines": "62-65",
     "quote": "pre/post tests are assigned **separately from the course** and surface on the TimeBack UI dashboard as a pending test. **PowerPath is only for serving questions natively — not for pre/post gating.** Pilot: select a cohort, assign the test before + after the learning app to measure growth."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "59-61",
     "quote": "common-person (anchor-person) linking, **N≥200 dual-tested** (real MAP RIT + our-form score), tail oversampling, report link SE; dual-MAP preferred over STAAR-equate; RIT BLOCKED until the anchor holds."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "63-65",
     "quote": "**No-RIT-pre-pilot is enforced in CODE** — `engine/src/map_engine/scorer/report.py` hard-sets `rit_output=BLOCKED_PRE_PILOT`, gates RIT behind `PILOT_PHASE==\"post-pilot\"` AND non-null `LINK_COEFFICIENT_A/B`."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mark borrowed data — another grade's norms or weak-skill findings — as a placeholder, never as measured data for the new group of students.",
   "kind": "adopted rule",
   "found_by": "The generator harness for a new grade listed cohort data that must not be fabricated or carried over.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "277-279",
     "quote": "target the G3 weak-skills — compare/contrast, cause/effect, sequence — as a *marked placeholder*, explicitly flagged, never presented as measured G5 data); **G5 MAP norms** (do NOT reuse G3's 186.6 / 193.9 / 197.1);"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-validate a writer when moving it to a new grade or difficulty level, and expect items not to carry over — what carries over is the scaffolding: schemas, format examples, error lists and blueprints.",
   "kind": "measured",
   "found_by": "A generator proven at one grade had never produced material at the next level and already degraded at higher difficulty; an inventory of about 930 items found none usable at the new grade.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "60",
     "quote": "**Lexile-band extrapolation is unproven at G5.** Today's templates top out at 800–820L. G5 needs **830–1010L** — *above everything the generator has ever produced*. EBSR already proves the model degrades at higher Lexile (couldn't clear EBSR above 560L); pushing the whole bank +230–410L is into untested territory."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/ITEM_INVENTORY.md",
     "lines": "34",
     "quote": "Up-leveling a G3 item means a new cold passage + new stem + new distractors + re-eval = a regeneration, not a reuse."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/ITEM_INVENTORY.md",
     "lines": "36",
     "quote": "### What IS reusable (the real \"don't reinvent\" win — scaffolding, not items)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check the depth-of-thinking mix a writer actually produces against the target; asked for a spread, a writer produced the middle level on almost every kept item.",
   "kind": "measured",
   "found_by": "A count of kept generated items found 78 of 80 at the middle depth level.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/assessments/G5_PARAMETERS.md",
     "lines": "119",
     "quote": "**Honest reality flag (load-bearing):** the **proven G3 generator emitted DOK 2 on 78/80 kept items** (measured from form_a.jsonl + form_b.jsonl) — it does **not** reliably produce DOK 1 or DOK 3 even when the standard supports them."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/generator-output-spec.md",
     "lines": "47",
     "quote": "(honest flag: prompted generators tend to over-emit DOK-2; DOK-3 yield must be measured, not assumed)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "An exemption from an outcome requirement must be granted by someone other than the author and replaced by another measured outcome, never simply waived.",
   "kind": "adopted rule",
   "found_by": "A self-audit tightened an escape hatch that let an author waive the outcome measure for engagement-led material.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/templates/COMPLIANCE.template.md",
     "lines": "22-26",
     "quote": "exemption is **granted by a reviewer, not claimed by the author**. To use it: (1) the README declares the slice; (2) **each** MAP-coupled row marked `N/A — engagement-primary (see README)` is **replaced by a measured engagement OUTCOME** (retention / completion-quality / session-depth, with a path-backed figure) — so the hatch *costs* an outcome rather than *waiving* one;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md",
     "lines": "24-26",
     "quote": "reviewer-granted, NOT author-declared; each nullified MAP row must be **replaced by a measured engagement OUTCOME** (retention / completion-quality) so \"engagement-primary\" costs an outcome rather than waiving one."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Tag every rule and claim with how it was verified — walked live, full census, single probe, enforced in code, or not yet verified — and report each requirement as pass, partial, unverified or fail.",
   "kind": "adopted rule",
   "found_by": "The publishing rules carried evidence tags after render behaviour differed from documentation; the course standard fixed four status words.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd",
     "lines": "107-108",
     "quote": "Confidence tags: `[LIVE]` walked in the student app · `[CENSUS]` exhaustive content check · `[PROBE]` one live probe per format · `[CODE]` enforced in code+tests · `[OPEN]` not yet verified."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/knowledge-[name]-additions/docs/standards/course-quality.qmd",
     "lines": "13",
     "quote": "| `UNVERIFIED` | Not measured yet. Do not infer success. |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make any scored selection of topics or materials transparent — factors, weights and totals a checker can recompute — with a recorded human override and its reason.",
   "kind": "adopted rule",
   "found_by": "Reviewers praised a transparent topic scorecard and a reasoned human override; both were made preserve-obligations.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl",
     "lines": "2",
     "quote": "\"requirement\": \"Preserve the explicit topic scorecard and expose the inputs and weights so reviewers can inspect and challenge the result.\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl",
     "lines": "3",
     "quote": "\"requirement\": \"Retain a visible human override path where a person can keep or reject a topic against the score with a recorded reason.\""
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/feedback-obligations.jsonl line 3: \"Human override is a governance control, not evidence that the selected topic is effective.\"",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep one interface across lessons — the same controls and component shapes — and vary the content, not the mechanics.",
   "kind": "adopted rule",
   "found_by": "Reviewer feedback demanded interface standardization; lessons were rebuilt to match a reference lesson's shell exactly while keeping their own structure and content.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
     "lines": "22-23",
     "quote": "\"On all the other lessons, we have to follow the UI/UX to the tee — no variations at all.\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "18",
     "quote": "UI standardization"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
     "lines": "82-83",
     "quote": "rule: our structure stays, his components look exactly like his"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Every interaction must work by keyboard and assistive technology, and every diagram needs a text or table equivalent.",
   "kind": "adopted rule",
   "found_by": "Drag and click-only interactions were declared a legal blocker; a lesson audit found a diagram with no accessible equivalent.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "370",
     "quote": "**Accessibility (#10) is now a hard LEGAL blocker** (drag-to-order + hot-text keyboard/AT; check how MAP implements)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "67",
     "quote": "| F11 | major | The diagram is not element-addressable and has no accessible table equivalent. |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/app-package-agent.md",
     "lines": "37",
     "quote": "Keyboard-operable and screen-reader-aware vocabulary and audio controls."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    27
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Cap how many options a young student must weigh at once.",
   "kind": "measured",
   "found_by": "A static accessibility scan flagged 137 of 772 items over a five-option cap, mostly interactive items with many selectable spans.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
     "lines": "132-133",
     "quote": "flagged 137/772 items over a 5-option cognitive-load cap (mostly hot-text)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "140",
     "quote": "accessibility option-count caps;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Images of people must not look machine-generated, because a student who spots 'fake AI' disengages and skips.",
   "kind": "adopted rule",
   "found_by": "A ruling on video style options set this as the one binding requirement.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "137-138",
     "quote": "the human needs to look less AI generated... I never want a student to declare 'Fake AI video' and skip to the next."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    22
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give the material being read and the teaching around it different, consistent voices, so students hear them as different things and each role sounds the same in every lesson.",
   "kind": "adopted rule",
   "found_by": "Voice roles were chosen per grade with comments explaining the distinction; a later gate checks one voice per role across lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "81-84",
     "quote": "coach (Scout, Puck) and narrator (the book reader, Leda) are deliberately DIFFERENT voices so a child hears \"the story\" and \"the teaching\" as distinct — mirrors the G3 HTML player this engine ports. One voice per role, consistent across pages"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "57-59",
     "quote": "\"the coach coaches, the book reader reads, and keeping the two voices distinct is how a student hears 'the story' and 'the teaching' as separate things.\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    2
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Start a course with material students can handle and raise difficulty in steps.",
   "kind": "adopted rule",
   "found_by": "A course opened on a topic judged too hard for the start; the course structure ramps difficulty band by band.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0057-incept-team-sync-2-2026-06-18.qmd",
     "lines": "45-46",
     "quote": "**Lexile start too hard** — course opens on \"vertebrates and invertebrates\"; start easier and calibrate up."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0014-course-structure-manifest.qmd",
     "lines": "33",
     "quote": "**A · Hook (400-460L)** → **B · Bridge (480-540L)** → **C · Transfer (560-600L)**."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give every unit an explicit key understanding, its likely misconceptions and its links to other units, so the build-up of knowledge is visible.",
   "kind": "adopted rule",
   "found_by": "Reviewers said knowledge sequencing was not observable; the repair list and curriculum packet now require a unit ledger.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "91-92",
     "quote": "add unit key understandings, conceptual cross-unit links, and misconception sets;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "281",
     "quote": "knowledge sequencing is not observable"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/curriculum-agent.md",
     "lines": "41",
     "quote": "Unit ledger showing key understanding, misconceptions, fiction/nonfiction role, and cross-unit use."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Show results openly to students, families and operators, tying each piece of work to the student, the content and the attempt; never hide poor performance.",
   "kind": "adopted rule",
   "found_by": "The delivery platform's non-negotiables, adopted by the project as its bar.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
     "lines": "226",
     "quote": "The platform must be able to attribute work to student, content, and attempt. Results are surfaced to students, families, and operators. Apps cannot hide poor performance."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge material by how quickly students reach a verified outcome, not by time spent or completion; time measures presence, not learning.",
   "kind": "adopted rule",
   "found_by": "The delivery platform's evaluation dimensions and its reason for combining effort with proof.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0026-evaluating-apps.qmd",
     "lines": "23",
     "quote": "| **Efficiency**                 | Fewer hours to reach the same verified outcome     |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0030-xp-system.qmd",
     "lines": "19",
     "quote": "track **time** (which measures presence, not learning) or track **accuracy** (which ignores how much work was done)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a task promises 'all' of something or a range, check every member is present; a synthesis task must combine at least two earlier components, and a rubric must accept everything its own chart shows as valid.",
   "kind": "adopted rule",
   "found_by": "The content-integrity skill's closure lane, written for synthesis tasks and charts that omitted promised parts or contradicted their rubric.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "177-183",
     "quote": "expand ranges such as `L1-L7` and words such as `all` or `every` into canonical IDs; require `coverage_mode` to be `exhaustive`, `representative`, or `sampled`; treat explicit ranges and `all`/`every` as exhaustive; compare promised lessons, entities, operations, sources, chart rows, tasks, and rubric categories with what is actually present; require synthesis to coordinate at least two prior components rather than list isolated recalls; require chart and rubric closure: anything represented as valid must be accepted consistently."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "185-186",
     "quote": "Missing required entities, omitted operations, inconsistent row logic, or a rubric that rejects its own chart are `FAIL`."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a question and its material disagree (a missing word or a missing quotation), should you change the material or the question? The project's two fixing rules point opposite ways.",
   "kind": "open question",
   "found_by": "The course-fix skill repairs a word missing from the text by editing the text; the content-integrity skill forbids repairing a missing quotation by editing the text.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "171",
     "quote": "Never repair a missing quote by changing the passage unless the passage authority itself is wrong."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md",
     "lines": "46-47",
     "quote": "**Vocab word-not-in-passage (NN#5):** FIX by editing the PASSAGE — `PUT {QTI}/stimuli/{id}` to use the word in context. Never reword the stem to dodge it; never delete the item."
    }
   ],
   "against": "The rules come from different checks (quotation tasks vs vocabulary items); no ruling reconciling them was found in scope.",
   "adds_to_existing": [
    23
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give the writer the sequencing policy explicitly, and combine several sources in stages rather than all in one pass.",
   "kind": "adopted rule",
   "found_by": "Curriculum-architecture doctrine adopted as an authority for generated courses.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "269-270",
     "quote": "never blend sources in one pass; supply the sequence policy to the model;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    57,
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "People supply the curriculum sequence; a lesson-writing model works from it and does not author it.",
   "kind": "adopted rule",
   "found_by": "The course graph is produced by a separate curriculum layer that the lesson-writing skill only consumes; a meeting claim that the model now authors all curriculum was recorded as conflicting with that contract.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/g3-course-graph.qmd",
     "lines": "69",
     "quote": "the Teacher *consumes* this graph; it does not author it"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/ROUTER.md",
     "lines": "70",
     "quote": "Load the candidate SKILL.md to author a G3 lesson (start from a course-graph unit spec, not ad hoc)."
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md lines 219-220: \"the meeting report that the teacher now authors all curriculum/content conflicts with the verified human-supplied-graph contract and tier-NONE status\" — a contrary claim was made in a meeting.",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A pass on a sample does not clear the unsampled rest of the course.",
   "kind": "adopted rule",
   "found_by": "Stop rules in the passage-integrity packet and the content-integrity skill.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
     "lines": "65",
     "quote": "Do not approve the whole course from a sampled cohort."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
     "lines": "275",
     "quote": "convert `PASS` on a sampled cohort into a whole-course claim."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make a judge write down the evidence it is scoring, and how it reached its answer, before it gives a score.",
   "kind": "adopted rule",
   "found_by": "An evaluator's quote-before-score audit was singled out as a good adversarial pattern; the blind grader must record its answer and how it got there.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "65",
     "quote": "video script evaluator's quote-before-score `structure_audit` is a good adversarial pattern."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
     "lines": "146-147",
     "quote": "**Step 1 — Blind solve.** Attempt the item using only world knowledge and the options themselves. Write down the answer you reach and HOW."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    39,
    32
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mark every machine-written item and text as not yet human-approved until a person signs off, and keep that flag on the item itself.",
   "kind": "adopted rule",
   "found_by": "The ship gate keeps machine-authored tags, feedback and items unapproved until human review; the flag was confirmed to persist on the item.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/CHECKLIST.md",
     "lines": "65",
     "quote": "**Human content review** — machine-authored content (CCSS tags, feedback, recall/MAP items) `humanApproved=false` until a human signs off."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/timeback-course-fix/SKILL.md",
     "lines": "55-56",
     "quote": "**`metadata.humanApproved` persists** (PUT False → GET False) → the human-review gate can live on the item. All machine-drafted edits stay `humanApproved=false` until a human signs off."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Does grounding a question writer in real source texts raise item quality? A small test said yes, while a larger claimed gain was refuted on the binding grader.",
   "kind": "open question",
   "found_by": "An earlier AP question-generation effort reported source-grounding as its biggest lever on a six-item smoke test; the item standard records its larger reported gain as refuted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
     "lines": "92",
     "quote": "it's the one mechanism aptraining found that broke a wall (n=6 smoke, 5/6 pass@0.85)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "39-41",
     "quote": "(Real-source provenance is a *separate, UNPROVEN* lever: the aptraining \"0.29→0.95 via real passages\" result was **refuted** on the binding grader. Do not relabel machine-authored cold passages as \"real.\")"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g5-reading-generator-output-spec.md",
     "lines": "74",
     "quote": "**Source-grounding was the biggest real lever** (feed real stimuli, model writes the questions) — exactly the cold-passage/anti-leak standard in §3. Build the generator around it."
    }
   ],
   "against": "The sources conflict (above); no larger controlled comparison found in scope.",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Do not interrupt the reading of a text with voiced asides at the top of every page; they break the reading flow.",
   "kind": "adopted rule",
   "found_by": "A reviewer asked for page-top interjections to be removed; they were deleted across lessons and their clips retired.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "39",
     "quote": "\"remove Scout's interjections at the top of each page. They take away from the reading flow.\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
     "lines": "45-46",
     "quote": "nine `purpose` + `purpose_voiceover` fields deleted per lesson across L4-L7 + G5-U1-L1, nine clips retired,"
    }
   ],
   "against": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md line 92: \"rebuild reading purpose,\" — an earlier review round asked for an explicit reading purpose, so the purpose must live somewhere less disruptive.",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a failure count drops, check that no check was switched off; part of an apparent improvement came from disabled checks.",
   "kind": "measured",
   "found_by": "A working tree's lower failure count was traced partly to disabled linter rules, so both states were quarantined.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
     "lines": "193-195",
     "quote": "clean `origin/main` for G5 1,241 already fails 28 RED/12 YELLOW; the dirty tree's lower 15/8 result partly comes from disabled linter invariants, so both states are quarantined."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give every distractor a named error type from a fixed list, and validate that each wrong option carries one.",
   "kind": "adopted rule",
   "found_by": "Courses shipped distractors with no diagnostic intent; the item standard, a parallel measurement project and a remediation strand adopted a fixed error-type list per option.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
     "lines": "27",
     "quote": "| 6 | **Misconception-tagged distractors** — each wrong option maps to a named cluster: `schema_mis_mapping` / `strategy_substitution` / `inference_overreach` | distractors with no diagnostic intent |"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "105-106",
     "quote": "Action: add a per-option enum validator (fail-and-retry) to our generator;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0008-alpha-courses-repo.qmd",
     "lines": "132-133",
     "quote": "Every selected-response item carries **misconception-cluster tags** (A = strategy-substitution / B = schema-mismapping / C = inference-overreach)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Match how explicit and cohesive the material is to the reader's prior knowledge: highly cohesive texts help readers who know little about the topic but can under-stretch those who know a lot.",
   "kind": "adopted rule",
   "found_by": "Listed in the evidence base's authoring tier as a text-difficulty design rule drawn from the research it summarizes (no DOI given).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/PRIORITIES.qmd",
     "lines": "58-59",
     "quote": "The coherence x knowledge text-tuning interaction (high-coherence texts help low-knowledge readers; can under-stretch high-knowledge readers on deep measures)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "18",
   "quote": "scaffolding-question feedback (never the answer)"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "372",
   "quote": "hints-buttons **out**, scaffolding-on-2nd-attempt **in**"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "24",
   "quote": "hints follow an attempt;"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "68",
   "quote": "| F12 | major | The \"Dashed Line\" beat pre-teaches its own check on the same screen. |"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
   "lines": "63-64",
   "quote": "Silent branch on L4/L6 models a line from the story and asks its meaning (content-word overlap 1.00→0 on L4, 0.80→0 on L6; his L2 sits at 0.50)"
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "98-99",
   "quote": "miss 1 -> level-1 criterion cue, miss 2 -> level-2 evidence frame, attempt 3 -> level-3 release (`released:true`, framed as help, never \"solo pass\")"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
   "lines": "74-76",
   "quote": "Passage-dependency is currently judged by LLM rubric and regex, not by an empirical passage-withheld solve. Red-team history says rubric passage-dependency can pass while blind probes solve the items trivially."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
   "lines": "74-75",
   "quote": "(passage withheld, model+version pinned, temp 0.3, **N=5, FAIL at k≥3/5**, per-format answer-space rules, `ablation_trials[]` persisted)"
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/knowledge-[name]-additions/APPLY.md",
   "lines": "4-6",
   "quote": "the question-quality re-check material was **dropped** as redundant (the main generated set already passed InceptBench AND Opus — a different model family — so a further blind-solve gate adds nothing; the 4/11 leak finding was an 11-item seed bank, not the validated set)."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
   "lines": "154-156",
   "quote": "`PASS` requires one stable best answer/set and no material alternative. One credible competing answer is `NEEDS_HUMAN`; repeated support for two answers is `FAIL`. \"The intended answer is stronger\" does not repair a hard-scored item when another option also answers the question."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/applied/teaching-comprehension-insights-brainlift.qmd",
   "lines": "66",
   "quote": "79% of correct answers in a generated course sat at option position A, and the correct option was systematically the longest"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
   "lines": "60-62",
   "quote": "classifies answers 5 ways (full/partial/off/brief/silent), 120 clips on the pinned course-TTS route, all Puck-stamped; the off-branch answer no longer sits last in every lesson."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "180-182",
   "quote": "promotion review caught `r3-09` at 3/8 exact blind recoveries and 0.71875 mean partial accuracy; low model confidence had wrongly hidden those hits."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
   "lines": "24-25",
   "quote": "`NEEDS_HUMAN`: evidence is missing, conflicting, inaccessible, malformed, or specialist judgment is genuinely required."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "72",
   "quote": "| F16 | major | The local evaluation fallback grades free responses by keyword overlap, and a porting note propagates that defect. |"
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0050-timeback-events-api.qmd",
   "lines": "134",
   "quote": "repeated attempt numbers overwrite prior info"
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/assessment-item-agent.md",
   "lines": "62",
   "quote": "Do not infer knowledge from one noisy response."
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0191-g3-book-lesson-anatomy.qmd",
   "lines": "150-152",
   "quote": "The step id is the page's own authored id, never its position (a position rots the moment the lesson's shape changes; five probes pinned to `?page=<n>` broke the day L1 grew an opening video)."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
   "lines": "163-164",
   "quote": "Treat lifecycle `quote-integrity` findings as blocking. A prompt that asks for a quotation requires one unique contiguous passage match after only Unicode, whitespace, and punctuation normalization."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
   "lines": "95-96",
   "quote": "they trusted generator-asserted `word_count`/Lexile and a 30-char substring \"verbatim\" check (defeated by paraphrase)."
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "59",
   "quote": "| F3 | major | \"producer\"/\"habitat\" are deep-taught as if they were blocking vocabulary (they aren't). |"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
   "lines": "57-63",
   "quote": "a generated cover image duplicated a pinned character — 5 children shown instead of a pinned cast of 4. **Mechanism:** cast pinning inside a CAST block in the prompt is not enough; the model drifts on count once past roughly four figures, and pinning the count in only one place in the prompt doesn't anchor it. **Fix:** repeat the EXACT-N count inside the SCENE line itself (not just the CAST block), use explicit separation language, and enumerate individually for stubborn cases; EYEBALL every generated image before wiring it into `art.ts`."
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
   "lines": "171-173",
   "quote": "Segments are cut from one approved take with ffmpeg, never re-synthesized, so the voice a reviewer approved stays the voice a child hears even as new states are spliced in."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
   "lines": "95-98",
   "quote": "every text-side validator (voiceover-sync hashes, read-along marks, the walkers) can be green while the audio itself is wrong — a reviewer heard \"betrayal\" as \"trail\" because the /b/ onset sat at -84dB in the clip, and every text-side check passed."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "94-95",
   "quote": "**772/772 stimuli** had been flattened at publish time into one tagless `<p>` (titles welded onto bodies, e.g. \"PapyrusIn\"; \"surface.Passage 2\"; data tables collapsed)"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
   "lines": "31-32",
   "quote": "different snapshots; treat this live pull as current ground truth for the deployed course."
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "283",
   "quote": "Long feedback text is itself a failure for Grade 3."
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "370",
   "quote": "**Accessibility (#10) is now a hard LEGAL blocker** (drag-to-order + hot-text keyboard/AT; check how MAP implements)."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "188-190",
   "quote": "**PR 68 merged, but is not mandatory enforcement:** runnable tools and specs exist; no CI, publisher, or artifact-producing orchestration invokes them. The smallest defensible future gate needs persisted canonical lesson artifacts first; fixture-only CI would overstate enforcement."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0009-timeback-alpha-read-packager.qmd",
   "lines": "77-78",
   "quote": "fail-closed (a lesson that won't validate is reported + excluded, never silently shipped)."
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "142-143",
   "quote": "explicitly bars any LLM grader on the auto-score-to-100 path (feedback must be a deterministic function of the machine-scored response)."
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
   "lines": "96-97",
   "quote": "Above the default case limit, an unscoped run refuses to proceed; split by changed cohort instead of paying for an incoherent sweep."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/README.md",
   "lines": "60",
   "quote": "No model calls in the gate path; any machine-judged input must already be frozen into the ledger with its evidence tag before the gate runs."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/skills/course-content-integrity/SKILL.md",
   "lines": "150",
   "quote": "4. repeat with at least three option-aliased or shuffled views;"
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "63",
   "quote": "| F7 | major | The Generate level (I09) is missing; oral/typed judges accept empty or content-blind answers. |"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
   "lines": "21-23",
   "quote": "The two **semantic** checks in section 5 -- think-aloud authenticity (reasoning trace vs answer reveal) and release-item operation classification -- are advisory until an LLM-judge calibration pass and are deliberately NOT implemented here."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/tooling/ti-courseplans-2169d1f/scripts/lane-tools/op-lint/README.md",
   "lines": "42-44",
   "quote": "One passing unit and one failing fixture per rule, including all three round-2 failure shapes. Every rule has at least one failing case -- the selftest asserts the exact expected failure-rule set per lesson and fails if any rule loses its failing fixture."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "30",
   "quote": "full validation, fixed-point index, and 152/152 mutation cases pass in a fresh tree;"
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md",
   "lines": "32-34",
   "quote": "the G5 static dataset carries both an IB and an independent Opus score per pass-row — rank by max disagreement and send those to the passage-blind solver first; a ready-made, zero-cost leak-suspect signal."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/knowledge-[name]-additions/docs/standards/course-quality.qmd",
   "lines": "55",
   "quote": "generation trace including rejected attempts."
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/lesson-instruction-agent.md",
   "lines": "59",
   "quote": "Do not model analysis before the learner encounters the text."
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
   "lines": "493",
   "quote": "\"Explicit instruction provides a clear explanation of the criterion task, encourages students to pay attention, activates prior knowledge, breaks the task into small steps, provides sufficient practice at every step\""
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/TOOLING.md",
   "lines": "9-11",
   "quote": "A green deterministic gate is not academic, accessibility, factual, or readiness approval."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0228-g3-listen-qa-transcript-receipts-2026-09-24.qmd",
   "lines": "21",
   "quote": "no human has heard the 120 branch clips,\" meaning these are machine transcripts, not human listens)."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
   "lines": "104-108",
   "quote": "reproduced twice in dev-server walks but **zero times in production-build walks** (journey-23-prod: 27/27 clean). Root cause: the two dev reproductions coincided with concurrent file writes inside the worktree (other agents editing harness files, or `npm run` steps writing caches) triggering a Next.js hot-reload remount — never reachable by a real student on Amplify. Rule added to the recipe: dev-server walks need an idle worktree; proofs that must be clean run against the production build."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
   "lines": "36",
   "quote": "**Instruction quality — 3/5, CANNOT VERIFY from pull.** Pull is assessment-only; the instructional dose (hook→teach→guided→read→CFU→check) lives in PowerPath, not OneRoster."
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/HOTBUCKET.md",
   "lines": "313-315",
   "quote": "practice/thin-instruction shapes fail; only the full student-ready candidate passes the simulation. This is design evidence, not live child-outcome proof."
  },
  {
   "truth": 47,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0007-ti-courseplans-repo.qmd",
   "lines": "74",
   "quote": "Running 100K simulated students yields **zero new information** — outputs are determined by the imposed math models + pre-training."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0032-principles.qmd",
   "lines": "120",
   "quote": "| High in-app accuracy, low test scores | In-app tasks are not testing transfer |"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/knowledge-[name]-additions/docs/standards/course-quality.qmd",
   "lines": "61",
   "quote": "A fully green build gate proves the course is well-built. It does not prove the course works. Every gate row above is satisfiable from metadata and structure, so \"done\" and \"moves outcomes\" are decoupled unless an outcome measure is added."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
   "lines": "84",
   "quote": "**Mastery now requires COLD / unseen-passage transfer** — the fix for \"in-app high, MAP flat.\""
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
   "lines": "38",
   "quote": "**ZERO CCSS standards** across all 745 items (RL/RI/L.3.x absent from every rawXml + metadata). Format coverage excellent (all 6 MAP formats), but no alignment ⇒ can't map to MAP skills, can't feed CASE, blocks Level-2."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
   "lines": "29-31",
   "quote": "frame `rows[].audio_path` review clips have no `audio_of` sha256, so a text edit (e.g. a definition rewording) leaves the clip silently stale with nothing in the validator suite able to detect it"
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0176-g3-peter-pan-pr-timeline.qmd",
   "lines": "53-55",
   "quote": "Every deploy was proven by **hashing the served file**, never by a 200 response: fetch `/lesson-json/grade-3.json` from `https://staging.dh84taiokgj9u.amplifyapp.com` (cache-busted) and compare its md5/sha256 against the git blob at the merge commit."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/source-map.json",
   "lines": "5",
   "quote": "\"ai_use\": \"Resolve source IDs here; verify SHA-256 before treating archived bytes or KB entries as the reviewed input.\""
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0026-evaluating-apps.qmd",
   "lines": "26",
   "quote": "If an app performs well on engagement but poorly on externally validated outcomes, the closed loop forces the conversation back to instruction, mastery, and signal integrity."
  },
  {
   "truth": 51,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/skills/reading-science/DIGEST-rand-mr1465-2002.qmd",
   "lines": "547",
   "quote": "\"the most predictive statistical models show that engagement is a mediator of the effects of instruction on reading achievement\""
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
   "lines": "151-153",
   "quote": "a page may print words nobody reads aloud (question stems are deliberately silent per R-AUD-6), but it may **never speak words it does not print**"
  },
  {
   "truth": 53,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0027-learning-science.qmd",
   "lines": "47",
   "quote": "| **Multimedia**   | Combine verbal and visual when both add value. Avoid redundancy.                  |"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0227-g3-branch-hygiene-pr634-prep-2026-09-24.qmd",
   "lines": "63-64",
   "quote": "Silent branch on L4/L6 models a line from the story and asks its meaning"
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
   "lines": "92",
   "quote": "Feed the model real/cold G5-band stimuli and let it write **only the questions**; don't have it invent the passage from nothing."
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/docs/standards/item-quality.md",
   "lines": "39-41",
   "quote": "(Real-source provenance is a *separate, UNPROVEN* lever: the aptraining \"0.29→0.95 via real passages\" result was **refuted** on the binding grader."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
   "lines": "76",
   "quote": "Today 51% of attempts are an opaque `generated_item:null` — **instrument *why* each one died** (topic-reject vs format-fail vs truncation) before tuning"
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "168-169",
   "quote": "re-measures every agent-reported number independently rather than trusting it, and corrects two:"
  },
  {
   "truth": 62,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0235-g5-course-build-pipeline-2026-06-23-to-06-30.qmd",
   "lines": "163-164",
   "quote": "(input never contains the passage or key; `topic_seed` is audited to tell the generator WHAT to write, never the answer)."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/AUDIT_ACTIONS.md",
   "lines": "38-40",
   "quote": "the staged `g3-reading/COMPLIANCE.md` ports the eval of **`reading-explorers-g3-allqtypes` — [name]'s SOURCE course, not ours** (PR #3: \"not ours to edit\") — which says NOT MET / 3 FAIL. **These are two different course-ids.**"
  },
  {
   "truth": 64,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/BRIEFING.md",
   "lines": "31",
   "quote": "8 content bugs (mostly dangling-visual)"
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/analysis/GENERATOR_ASSESSMENT.md",
   "lines": "93",
   "quote": "(Our regenerate-until-pass loop is itself a soft best-of-N; report raw first-attempt yield separately.)"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
   "lines": "271-272",
   "quote": "**The INDEPENDENT-audit rate is the real metric**, not the in-loop self-grade (it is biased generous — it green-lit the item it later rates)."
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/pr-proposals/ti-courseplans-standards/staged/courses/g5-reading/generator/G5_GENERATOR.md",
   "lines": "214-215",
   "quote": "**The in-loop self-grade is NOT the headline metric.** It is a filter. The real metric is an INDEPENDENT audit by a fresh grader (or human) that did not participate in the loop,"
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
   "lines": "63-65",
   "quote": "**No-RIT-pre-pilot is enforced in CODE** — `engine/src/map_engine/scorer/report.py` hard-sets `rit_output=BLOCKED_PRE_PILOT`, gates RIT behind `PILOT_PHASE==\"post-pilot\"` AND non-null `LINK_COEFFICIENT_A/B`."
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/handoffs/g3-reading-v2-feedback-2026-07-16/science-passage-agent.md",
   "lines": "34-35",
   "quote": "6. Propagate any upstream failure through every declared dependent lesson, item, chart, and feedback object."
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
   "lines": "101-103",
   "quote": "run the FULL suite before commit, not just the targeted verifier — PR #240 shipped a listen-fix that passed every targeted check but broke `validate-voiceover-sync`."
  },
  {
   "truth": 70,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
   "lines": "115-116",
   "quote": "**\"Changes-first, then one walk\" discipline** (memory `changes-first-then-one-walk`) started formally at tick 30 after [name] stopped two walk-fail-patch-walk cycles (journeys 32/33):"
  }
 ]
}
```
