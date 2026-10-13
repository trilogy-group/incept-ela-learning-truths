# verify:ti-courseplans

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ti-courseplans",
 "verified": [
  {
   "index": 0,
   "verdict": "keep",
   "reason": "Quotes verbatim at cited lines. Line 25 defines class 1 as building correctly to the wrong or no spec; Gates 0-1 give the source census and the divergence log. General, and not already on the list.",
   "statement": "Before writing content, find and read every design source it must follow, transfer what they specify rather than regenerating it, and record every divergence with its ruling, because building correctly to the wrong specification is the costliest failure and no test of the finished artifact can catch it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "29",
     "quote": "Class 1 is the expensive one and the one artifact testing can never catch.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "50-52",
     "quote": "An undocumented divergence is a build error regardless of who requested it verbally.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "141",
     "quote": "1. Transfer, don't generate; mark no-canon layers explicitly.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep",
   "reason": "Quotes verbatim, and '6 of the 10' matches. The same standard (lines 15-23) states each clause, so that quote is added. Complements truths 40 and 41. The against is verified.",
   "statement": "Modelling, guided practice and independent practice must teach one process at falling support: showing the answer is not modelling, a hint is not guided practice, and switching to another skill is not independent practice.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "24-25",
     "quote": "Generator acceptance test: strip the labels; a reviewer must still be able to say \"these three artifacts teach the same process at decreasing support.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "15-16",
     "quote": "Revealing the answer is not modelling.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "69-71",
     "quote": "op-lint's deterministic layer catches **6 of the 10 round-2 academics failure shapes** -- including all three gradual-release exploits (answer-reveal I-do, hint-style we-do, skill-switch you-do).",
     "verbatim": true
    }
   ],
   "against": "STANDARD.qmd (v1.0.0) line 317: \"Claim boundary: Surface format may change only when the target operation remains demonstrably stable.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The addendum (lines 335-337) resolves the gradient rule itself: a scaffold may be offered at the released end after a first miss, but not by default. The absolute 'never' needed that qualifier. Overlaps candidate 1 and truth 41.",
   "statement": "Guided practice must leave the substantive step unfinished for the learner, independent practice must apply the same operation to new material rather than re-run the modelled example, and the independent step must never be more scaffolded by default than the guided one; extra support there is offered only after a first miss.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd",
     "lines": "57-58",
     "quote": "You-do returns to the model's animal, evidence, and constructed answer instead of requiring the same operation on new evidence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "245",
     "quote": "Guided work leaves the substantive learner move genuinely unfinished and increases support without completing it for the learner.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "332",
     "quote": "The gradient half: a you-do step may never be more scaffolded than the corresponding we-do step.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "335-337",
     "quote": "a scaffold added at the released end is offered **after a first miss**, not imposed as the default — available rather than mandatory.",
     "verbatim": true
    }
   ],
   "against": "Addendum lines 340-345: one lesson ships a step-4 gap-fill as the default, 'a known and deliberate D1.15 inversion' that was accepted on instruction after the objection was argued and overruled.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep",
   "reason": "Quotes verbatim. There is a count discrepancy between sources: SKILL lines 77-78 say 1 of 18 lessons, and finding-taxonomy line 191 says 3 of 18. The statement carries no count, so it is unaffected.",
   "statement": "A worked model must show the hard decision being made on the visible source — where it looked, a tempting wrong choice and why it was rejected — and must perform each step on screen as it is narrated, not merely store a rationale.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "52",
     "quote": "Visible evidence, a plausible alternative, the reason it is rejected, and construction of the answer are synchronized and semantically sound.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "77-78",
     "quote": "G3 iter-3's real \"reject-the-alternative\" modeling held in 1 of 18 lessons; the reviewed lesson (U2·L1) was that one.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "324-325",
     "quote": "every I-do step carried its span anchor and its rationale, and the screen performed none of them.",
     "verbatim": true
    }
   ],
   "against": "skills/course-red-team/references/finding-taxonomy.md line 191 reports the same measure as 3 of 18 lessons (count drift between sources).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "Quotes verbatim. The against quote sits at line 115, not 114-115. Context at line 91 requires an explicit gradual-release teaching step in every dosed lesson.",
   "statement": "A loop of read-then-answer items with right/wrong feedback is an assessment, not a course: every lesson needs an explicit teaching step, and assessment must never ship ahead of the instruction that prepares learners for it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "40",
     "quote": "a well-built, MAP-styled practice-and-assessment engine, not a comprehension curriculum",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-creation-spovs.md",
     "lines": "92",
     "quote": "A read-then-test loop with binary \"good try\" is not a course; it's an assessment engine.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "398",
     "quote": "Do not ship an assessment layer ahead of the instruction and knowledge-compounding layer that prepares learners for it.",
     "verbatim": true
    }
   ],
   "against": "docs/course-creation-spovs.md line 115: a practice-only course may defer teaching to another course, but \"deferring to a course that doesn't exist failed review.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep",
   "reason": "Both quotes verbatim. The reviewer called the cold-throughout design 'the deepest issue with the design'. The against is verified.",
   "statement": "Sequence the texts learners study so knowledge recurs and compounds across them, and keep unrelated never-taught texts for testing transfer only.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "70",
     "quote": "Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "166",
     "quote": "Cold plain text belongs at the *test*, not throughout learning; sequence passages so knowledge recurs and compounds",
     "verbatim": true
    }
   ],
   "against": "docs/practice-layer-spec.md lines 127-128: what crosses to cold text is operations, vocabulary and format fluency: \"Topic knowledge is the vehicle, never the cargo.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep",
   "reason": "Quotes verbatim (the second starts at line 73). F, p and partial-eta values match the source, which renders eta as 'g2'. Two quotes added: the design (random assignment, six vs six texts, matched words) supports 'same amount of reading', and 'incidental' is confirmed in the brainlift.",
   "statement": "Texts that repeat and elaborate the same concepts build more knowledge and more incidental vocabulary than the same amount of reading across unrelated topics.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd",
     "lines": "62-65",
     "quote": "59 fourth graders randomly assigned to read six texts that either cohered around bird concepts or spanned six unrelated topics — matched for total words, readability, and embedded target words.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd",
     "lines": "69-70",
     "quote": "\"For the total concept units, the main effect of treatment is significant in favor of the CC group, F(1, 56) = 26.84, p = .000, partial g2 = .324\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd",
     "lines": "73-75",
     "quote": "the main effect of treatment is significant, F(1, 56) = 93.16, p = .000, partial g2 = .625.\" (p. 772) — despite the CC words being *rarer* in English.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "132",
     "quote": "The largest Cervetti effect was *incidental* vocabulary",
     "verbatim": true
    }
   ],
   "against": "SYNTHESIS.qmd lines 186-187: \"N=59, one rural school, on-grade readers, 3-day intervention, null (unreliable) comprehension-questions measure\"; the source adds it is unclear whether merely topical sets work.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep",
   "reason": "Quotes verbatim. STANDARD line 232 ('Accept when') supplies the names-what-each-part-adds clause. Distinct from candidate 16.",
   "statement": "Claim that knowledge compounds only when removing an earlier lesson would break a later one; each lesson names what it adds, which earlier knowledge it reuses and what breaks without it, and links between units connect big ideas rather than shared words.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "344",
     "quote": "Claim knowledge compounding only when removing an earlier anchor removes a later explanatory, comparative, interpretive, or decision resource.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "233",
     "quote": "- Failure signals: Topic list; links based only on shared words; orphan lessons; final recall of disconnected facts.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "97-98",
     "quote": "19. **Cross-unit links about the BIG IDEA, not surface facts**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 8,
   "verdict": "keep",
   "reason": "Quotes verbatim. Spec lines 61-63 define 'retained' as passing a retest at least 24 hours later on new items; evaluator-spec lines 101-103 show the committed negative fixture failing the check. Extends truth 20. The against is verified.",
   "statement": "A lesson may assume only knowledge that earlier lessons taught and that the learner has retained on a later day, checked across the sequence in code, because scoring each lesson on its own cannot see the gap.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
     "lines": "63-64",
     "quote": "an anchor first taught the same day never satisfies an `assumes` edge, and an anchor that is present-but-not-fluent is treated as not met.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "103-104",
     "quote": "IB scores each of those two lessons as individually fine; only the cross-lesson invariant separates them.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "42",
     "quote": "Each prerequisite is established, activated, retaught, newly introduced, or routed through a tested on-ramp.",
     "verbatim": true
    }
   ],
   "against": "docs/instruction-modes-spec.md lines 59-60: the code check \"supplements, never replaces, human sequence review\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The source unit is 'one named performance, 1–2 knowledge types' (lines 14-15), so 'one kind of knowledge' overstated it. The against (cluster-first matters little for modular maths) scopes the rule to narrative subjects.",
   "statement": "Plan a group of related knowledge as a whole — one target performance, a throughline, a persistent example — before splitting it into small pieces, keep each generation unit to one performance and one or two kinds of knowledge, and expect this to matter most in narrative subjects.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
     "lines": "14-15",
     "quote": "the *cluster* (one named performance, 1–2 knowledge types, 2–5 KCs, one load-bearing throughline)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
     "lines": "16-18",
     "quote": "Atomise-first on narrative subjects produces \"locally-correct micro-lessons that never cohere\" — the round-2 sequencing finding.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "544",
     "quote": "as the surface area of the task grows, the precision and discipline of the LLM's output degrade",
     "verbatim": true
    }
   ],
   "against": "Curriculum & Knowledge BrainLift line 538: \"For modular, abstract material (much of maths) this matters little, because the atoms genuinely are near-independent and atomise-first is close to lossless.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but the spec quote starts at line 123. The fluency-threshold clause had no support, so curriculum-architecture lines 78-80 are added. There is AP support: line 368 says AP history and government links are 'shallow and sparse'. Overlaps candidates 8 and 11.",
   "statement": "Decide how much prerequisite structure a domain really has: tag every prerequisite link as logical, evidence-based or merely conventional, give helpful-but-not-required links a fluency threshold, and never force prerequisite chains onto knowledge that has none.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "70",
     "quote": "\"A before B\" is a curriculum design choice, not a logical necessity.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "380",
     "quote": "The response cannot be to force a prerequisite structure onto content that doesn't naturally have one",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
     "lines": "123-125",
     "quote": "classify each edge logical / empirical / conventional (kc-graph change proposal, warrant field); a conventional edge may not block the on-ramp until upgraded by evidence",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/curriculum-architecture.md",
     "lines": "78-80",
     "quote": "**soft prereqs carry a fluency-threshold** (not binary met/unmet: \"fluent enough not to consume working memory\"), and **every edge carries a warrant tag** (logical / empirical / conventional).",
     "verbatim": true
    }
   ],
   "against": "Assessment & Feedback BrainLift line 368: \"In mathematics, prerequisite chains are deep and reliable\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Quotes verbatim. The general-first prescription was only implied, so C&K line 1262, which states it outright, is added. The fluency clause overlaps candidates 8 and 10.",
   "statement": "How knowledge is split into lessons can itself create misconceptions: teach the general case before a restricted one, and count a prerequisite as met only when it is fluent enough not to load working memory.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "36",
     "quote": "Splitting a restricted case from a general case (e.g., same-denominator before unlike-denominator fractions) causes students to build predictive models that become entrenched and must be actively undone.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "1262",
     "quote": "teach the most general case first, use carefully chosen examples to prevent induction of restricted rules.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "37",
     "quote": "A prerequisite that is technically met but not automated enough to free working memory makes the target skill unteachable.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 12,
   "verdict": "keep",
   "reason": "Quotes verbatim. C&K line 49 lists exactly the four policy items in the statement, including 'the sequencing priority order'.",
   "statement": "Write the curriculum sequence before writing items, and declare the sequencing policy (progression spine, entry assumptions, prerequisite strictness, priority order) before a model proposes an order, which is then reviewed against that policy rather than against taste.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "308",
     "quote": "Author the curriculum graph and lesson sequence before item authoring so available questions cannot become the curriculum by accident.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "48",
     "quote": "Every output becomes a debate about taste rather than a review against a policy.",
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
   "reason": "All three quotes verbatim. General across subjects and not already on the list.",
   "statement": "Use standards to bound what must be covered, not as the teaching plan: their order and grain say nothing about learnability, and tagging items to standards is not a curriculum.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "25",
     "quote": "State standards are scope documents written for accountability and comparability, not for novice learnability.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "36-37",
     "quote": "Skills-only reading standards (\"determine the central idea\") are architecturally unusable: they carry no content, no sequence, no prerequisites",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "57-58",
     "quote": "Reading standards are skills, not knowledge — CASE-tag coverage is plumbing, never the curriculum claim.",
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
   "reason": "Quotes verbatim. The authority-order clause had no quote, so curriculum-architecture lines 27-30 are added; they match C&K lines 42-45.",
   "statement": "Combine sources in authority order — standards set scope, assessments set what counts as evidence, texts and resources supply examples — never in one blended pass, and never let a text widen scope without sign-off.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "41",
     "quote": "The model will average conflicts (producing something that matches no source well), import hidden assumptions from lower-authority sources (textbook idiosyncrasies becoming core curriculum), and expand scope without anyone noticing",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/curriculum-architecture.md",
     "lines": "27-30",
     "quote": "Stage by authority: **standards = scope authority; assessments = evidence authority; textbooks = representational authority** (may not expand scope without human sign-off).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
     "lines": "108-109",
     "quote": "a text that smuggles new scope fails placement rather than silently widening the theme.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. C&K lines 1256-1258 describe a multi-state social-studies merge that 'became too vague to generate good instruction'.",
   "statement": "When merging similar standards or sources into one shared unit, keep each source's specific detail inside it, because a merged abstract description is too vague to drive lessons.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "1257",
     "quote": "The result was flattened abstractions that lost the specificity needed for teaching.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/curriculum-architecture.md",
     "lines": "90-91",
     "quote": "**Preserve state-specific detail INSIDE nodes — never merge into abstract common nodes**",
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
   "reason": "Quotes verbatim. The practice spec makes the theme sequence the first spaced-practice system and leaves separate spaced review as the backstop.",
   "statement": "Make later lessons need earlier knowledge so retrieval happens through use, and send to separate spaced review only the residue that nothing later recruits; drilling everything forever compensates for a poorly connected curriculum.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md",
     "lines": "55",
     "quote": "A platform should not compensate for a poorly connected curriculum by drilling everything forever.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "35-36",
     "quote": "it keeps warm exactly the residue the ladder cannot honestly recruit downstream, and the size of that residue is a design metric on theme",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. The against is verified at line 108.",
   "statement": "Return to a topic only with a real upgrade — a new representation, wider scope, more abstraction, a stronger reason or harder transfer — because re-covering it at the same depth wastes time.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md",
     "lines": "104",
     "quote": "each revisit adds a real upgrade — a new representation, wider scope, greater abstraction, stronger warrant, or more demanding transfer.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "125",
     "quote": "claimed throughlines (adaptation, power) must recur at greater depth, not just be labeled",
     "verbatim": true
    }
   ],
   "against": "Curriculum Architecture BrainLift line 108: \"use blocks where coherence and immersion are essential\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (the topic-selection quote is at 32-33). The original said 'not by how commonly others teach it', but the metric keeps frequency at 25% as a sanity check (lines 33-34). The four factors match lines 28-29.",
   "statement": "Choose what knowledge to teach mainly by its leverage — how often later texts assume it, what builds on it, how often target tests draw on it and how widely it transfers — keeping how commonly others teach it only as a minor sanity check and how interesting it seems not at all, and let a person override the score only with written grounds.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/LOAD-BEARING-METRIC.md",
     "lines": "132",
     "quote": "interest tested flat as a learning driver, so it was struck from the record (Honesty log).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/TOPIC-SELECTION.md",
     "lines": "32-33",
     "quote": "\"what the field commonly teaches\" is a set of other people's design choices, not a discovered structure, so it carries *less* authority than powerful/portable knowledge.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/TOPIC-SELECTION.md",
     "lines": "33-34",
     "quote": "Frequency stays at 25% as an external sanity check that forces every high-leverage outlier to be defended.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/LOAD-BEARING-METRIC.md",
     "lines": "138",
     "quote": "The mirror image of Greek myth: *most* frequently taught, *lowest* leverage.",
     "verbatim": true
    }
   ],
   "against": "LOAD-BEARING-METRIC.md line 146: the 0.75/0.25 weighting and the per-factor split are 'declared dials (not claimed as measured)'.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep",
   "reason": "Quotes verbatim, and 0/10 with 8 plus 2 leaks matches. C&K line 84 is added: it says the gate must test the combined move.",
   "statement": "Passing checks on separate parts does not show the whole performance: teach learners to coordinate the parts and put tasks that require the combined move into the mastery check, since declaring an item integrative proves nothing.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "85",
     "quote": "Failure mode if ignored: \"passed parts, failed whole.\" Students look successful on micro-gates but break at any authentic task.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "84",
     "quote": "The mastery gate for an integrative lesson must test the integration — requiring the combined move, not re-testing the parts in isolation.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "273-276",
     "quote": "the full gate certified **0/10** (8 plain-blind leaks, 2 spine-conditioned leaks; 0 integrative verified)",
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
   "reason": "Quotes verbatim. Related to candidate 19 but distinct: this one sets a floor on how finely to split.",
   "statement": "Some performances must stay whole: define them by exemplars and a rubric rather than slicing them into ever smaller skills.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
     "lines": "26-27",
     "quote": "4. **Decomposition floor.** Integrated performances (passage comprehension) stay whole as capstone KCs — exemplars + rubric-anchored outcome spaces, never sliced thinner.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "551",
     "quote": "the capstone KC should be treated as an integrative construct — defined by rich exemplars and rubric-anchored outcome spaces rather than an exhaustive list of component KCs.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim, and '1 confusable edge / 47 KCs' matches. Generic Instruction line 56 prescribes explicit near-miss contrasts.",
   "statement": "Treat confusable pairs as first-class knowledge: teach the contrast explicitly before building on it, record the pair in the knowledge map, and interleave the two only after both are learned.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
     "lines": "24-25",
     "quote": "Discriminations are gateway hard prerequisites and chronically under-modelled (G5 graph: 1 confusable edge / 47 KCs).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "1286",
     "quote": "interleaving after both are learned builds discrimination",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
     "lines": "57",
     "quote": "Students don't reliably discover discriminations alone.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 22,
   "verdict": "keep",
   "reason": "Quotes verbatim, including the curly apostrophes. Comes from the knowledge-type SPOVs and holds across subjects.",
   "statement": "Choose the teaching method by what the knowledge is like — a fact to recall fluently, a concept, a procedure, a distinction, a causal explanation — rather than by subject habit, since no method is good or bad in general.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "1732",
     "quote": "**SPOV1 - Subjects don’t tell us how to teach; the knowledge type does.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "1735",
     "quote": "Methods aren’t universally good or bad; they’re conditionally apt given the KC’s evaluability, decomposability, and representation profile.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep",
   "reason": "Both quotes verbatim. They describe the two practice routes (fixed retrieval and transformation retrieval).",
   "statement": "Practise stable facts with brief, frequent, tapering retrieval and quick firming of errors, and practise schema-dependent knowledge by retrieval, feedback and then a task that uses it under new conditions.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md",
     "lines": "19",
     "quote": "Practice is frequent and brief early on, then tapered, with occasional maintenance checks. Errors are met with targeted firming, not full reteaching.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md",
     "lines": "20",
     "quote": "The sequence is: retrieval → feedback → update task (explanation, comparison, discrimination, boundary case, application in a new context).",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep",
   "reason": "Quotes verbatim. Extends truth 48 with the order: blocked practice first, mixed practice only after a delayed retest. Not a duplicate.",
   "statement": "Practise a new skill in a block while it is being acquired and mix it with other skills only after it survives a retest on a later day with new items, because same-day success measures working memory.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "37-40",
     "quote": "**Interleaving eligibility = E2-cleared**: a delayed (≥24h) retest passed on *new* parallel items — release-day completion never qualifies",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "433",
     "quote": "- Claim boundary: Interleaving is introduced only after prerequisite acquisition is secure.",
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
   "reason": "Quotes verbatim. The ATOMS quote is the AP U.S. History atom RHBL-027, which is scoped to that subject. It agrees with the reading sources, so the rule is not subject-bound.",
   "statement": "Practice and retrieval must not require or grade knowledge the course has not taught: if correcting a practice item needs more explanation than the lesson gave, the item is new teaching, not practice.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md",
     "lines": "38",
     "quote": "if the feedback needed to correct the response is longer and more complex than the original instruction, the item has crossed the boundary.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "452",
     "quote": "Retrieval may activate prior knowledge, but it must not grade content the course has not taught or established as a prerequisite.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "82",
     "quote": "| You-do requires untaught knowledge | round 1 F3 |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 26,
   "verdict": "keep",
   "reason": "Quotes verbatim. The '60 places' figure matches the SKILL's S3 row at line 398.",
   "statement": "Never grade a response form the lesson has not modelled exactly; if learners are marked on a format the modelling omits, the lesson is grading something it never showed.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "404-406",
     "quote": "the lesson grades the child on producing `The text says \"…\"` while the modelling omits the quote marks, so we grade a form we do not demonstrate.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/alpha-read/modelling-moment-procedures-v2/INDEX.qmd",
     "lines": "147-149",
     "quote": "it does not introduce an untaught response routine.",
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
   "verdict": "keep-with-fix",
   "reason": "Quote 1 joined two separate bullets without the list marker, so it was not verbatim as given. It is now split into verbatim quotes from lines 766 and 767. The other quotes and the against are verified.",
   "statement": "A percentage pass mark means something only while task mix, difficulty and support stay fixed, so set each bar by how costly it is to advance a learner too early rather than by one global figure.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "766",
     "quote": "Percent-correct only means something when task difficulty and evidence conditions are held steady; otherwise it is entangled with item easiness, scaffolding, and cueing.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "767",
     "quote": "If we change the task mix, we change what “90%” means, which makes the system look consistent while the standard drifts.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "789",
     "quote": "So a single global “90%” (or global posterior cut) is structurally incoherent",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "88",
     "quote": "- define mastery through controlled evidence and downstream risk, not a global raw `90%`;",
     "verbatim": true
    }
   ],
   "against": "skills/timeback-course-eval/references/eval-criteria.md line 24: \"Enforce mastery gates at ≥90% accuracy.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 28,
   "verdict": "keep",
   "reason": "Quotes verbatim, and the arithmetic holds: ceil(0.9n)=n for every n up to 9 and fails at n=10. The G4 red-team (line 57) shows a 22-item gate that tolerates 2 misses.",
   "statement": "Recompute what a percentage gate demands at the real item count whenever items are removed, because on a test of nine or fewer items a 90% gate requires a perfect score.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "14",
     "quote": "leak-purge shrank tests to 5–9 items → 90% gate = perfect-score-only (ceil(0.9n)=n for n≤9)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "63-64",
     "quote": "ceil(0.9×n) = n for n ≤ 9: a 90% gate on a ≤9-item test demands a perfect score. Check every gating test's size.",
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
   "verdict": "keep-with-fix",
   "reason": "Quote 2 joined three bullets (lines 796-798) without list markers, so it is split into verbatim lines. The SPOV 3 heading (line 769), which states the three outcomes, is added. The against is verified.",
   "statement": "A mastery gate needs three outcomes — advance, keep practising, or switch to re-teaching — and must change the item families when practice continues, otherwise persistence becomes the hidden pass criterion.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "769",
     "quote": "**SPOV 3 – The system needs three outcomes, not two: promote, keep practising, or switch to corrective instruction.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "771",
     "quote": "A mastery system that lacks an explicit “switch mode” state will inevitably turn persistence into the hidden criterion for passing.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "796",
     "quote": "If learners can eventually pass by repeatedly sampling similar items, the gate is measuring persistence (or luck) rather than acquisition mastery.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "797",
     "quote": "To prevent grind-through, mastery evidence must include breadth (multiple item families / near-miss contrasts) and recovery verification after any corrective branch.",
     "verbatim": true
    }
   ],
   "against": "handoff/timeback-course-explorer/references/eval-analysis.md line 96: \"the student re-attempts until 100%, which is *stricter* than a 90% gate\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 30,
   "verdict": "keep",
   "reason": "Quotes verbatim. AP evidence is added: the AP U.S. History atom RHBL-028 (ATOMS line 461) says to reassess with a parallel task. Extends truth 4. The against is verified.",
   "statement": "After an error, correct it, re-test on a new parallel item, re-check later, cap the retries and escalate to re-teaching or re-placement after repeated failure rather than looping.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "56",
     "quote": "The trace shows correction, an alternate explanation or representation, a parallel new attempt, a delayed recheck where claimed, retry bounds, and escalation after non-progress.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
     "lines": "36",
     "quote": "A second consecutive failed delayed retest routes to placement/sequence review — never an infinite loop.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "461",
     "quote": "Route historical-thinking feedback to the failed function, then reassess with a parallel task that uses different evidence.",
     "verbatim": true
    }
   ],
   "against": "docs/instruction-quality-standard.md line 114 (direct-instruction protocol): \"On a miss: **Correct** (answer + brief why) → **Test** (re-ask immediately) →\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep",
   "reason": "Quotes verbatim. STANDARD line 400 is already filed under truth 14, so this duplicates 14. It is kept because it adds the decision rule: base mastery on the first unaided check and use supported steps only for feedback.",
   "statement": "Keep first independent attempts separate from supported or repaired ones: base mastery on unaided checks, let supported steps feed feedback, and never count a retry after help as a first success.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "399-400",
     "quote": "supported retry counted as first independent success. - Claim boundary: Repair evidence remains distinct from first-try evidence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1380",
     "quote": "base high-stakes decisions on the first unaided check (or transfer task) that follows.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/alpha-read/modelling-moment-procedures-v2/INDEX.qmd",
     "lines": "161",
     "quote": "A modelling handoff is supported practice, not independent mastery evidence.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "14",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep",
   "reason": "Quotes verbatim. The citation checks out: the BrainLift's reference list gives Butler & Roediger (2008), pages 604–616 (line 2192). Adds to truth 1.",
   "statement": "Plausible wrong options can implant false knowledge, so every misconception-based distractor needs feedback that corrects it.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1991",
     "quote": "Butler & Roediger (2008) showed that feedback largely neutralises this risk, while the absence of feedback leaves it unchecked.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "95-96",
     "quote": "plausible lures can seed false knowledge;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "166",
     "quote": "strong misconception distractors + no feedback = teaching the error (negative suggestion effect)",
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
   "reason": "Quotes verbatim, and '~7% (15 of 48 lessons)' matches. Assessment & Feedback line 2006 supports the 'only adds cues' clause.",
   "statement": "Write each wrong option as the answer a specific misconception would give and name that misconception in its feedback; an option nobody would choose for a reason is filler that only adds cues.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "129-130",
     "quote": "Distractors are misconception-coded (each = the answer a named misconception picks); feedback names the misconception.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md",
     "lines": "44",
     "quote": "only **~7% of choice items (15 of 48 lessons)** name the *specific misconception* a distractor targets in its feedback",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "2006",
     "quote": "A weak fourth distractor is worse than no fourth distractor because it provides testwiseness cues and wastes time.",
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
   "reason": "Quotes verbatim, and d 0.79 and 0.83 match. The original had no scope. The source limits the evidence to immediate gains in undergraduates when the misconception is central, and Generic Instruction says not to foreground misconceptions that poor teaching created.",
   "statement": "When learners commonly bring a misconception to a topic, voice the tempting wrong belief once at the start and then resolve it, because a clear correct explanation alone can leave the misconception intact; a misconception that poor teaching created is fixed by fixing the explanation, not by voicing it.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
     "lines": "113-115",
     "quote": "A clear explanation can produce the feeling of understanding while the misconception survives.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
     "lines": "116-118",
     "quote": "concise correct exposition on immediate conceptual gains (Muller 2008: refutation ≈ d 0.79, dialogue ≈ d 0.83) [20]. Scope: immediate, undergraduate, misconception-central",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
     "lines": "60",
     "quote": "teach explicitly with contrastive material; expect to revisit.",
     "verbatim": true
    }
   ],
   "against": "Generic Instruction BrainLift line 61: \"*From poor instruction*: don't foreground — fix the explanation so it isn't produced.\"; the effect is shown only as an immediate gain in undergraduates.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 35,
   "verdict": "keep",
   "reason": "Quotes verbatim. Line 1994 adds that without new material an item tests recall 'regardless of how elaborate the stem looks'.",
   "statement": "Treat an item as higher-order only if it presents material the learner has not seen; a longer stem over familiar content is still recall, and difficulty is a separate dimension from cognitive level.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1995",
     "quote": "The novel stimulus requirement is the single most reliable test of whether an item is genuinely higher-order: no new material, no higher-order thinking.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "2010",
     "quote": "A hard recall item is still recall. An easy application item is still application.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. Line 398 is added to support the wording clause.",
   "statement": "An item's difficulty must come from the target knowledge; hardness from wording, negatives, obscure context or a clumsy response interaction is invalid, so match the input gesture to the shape of the answer.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "2366",
     "quote": "Any item whose difficulty cannot be explained in KC/KDT terms (steps, conversions, cue structure, etc.) is almost certainly measuring a messy mix of construct and noise.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "398",
     "quote": "The item should not reward test-taking savvy or punish students who know the material but are tripped up by wording.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "760-761",
     "quote": "**The interaction taxed exactly the working memory the item exists to measure comprehension with.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "766",
     "quote": "* **Match the gesture to the shape of the answer.**",
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
   "reason": "Quotes verbatim, and 6/6 matches. The all/none-of-the-above ban is at line 1996, and the dash/hedge uniqueness rule is at addendum line 222. Adds to truth 8.",
   "statement": "Write options so test-wiseness cannot win: keep the key the same length, form and punctuation as the distractors, avoid absolute or ungrammatical distractors, make the stem answerable with the options covered, and never use all/none of the above.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "225",
     "quote": "the rubric gate passed 6/6 such items (g4 F1)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "214-216",
     "quote": "The key is the only option of its grammatical kind",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "2002",
     "quote": "read the stem, cover the options, and ask whether a knowledgeable student could formulate an answer",
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
   "reason": "Quotes verbatim. A title, narration or earlier item that gives away a key is the case truth 3 already covers, and the re-ask clause is truth 41. Kept because it adds evidence: the lesson-wide check that no item gives away another item's answer, and the leak from the title alone.",
   "statement": "Check items against each other and against everything the learner meets first: no title, narration, earlier item or modelled answer may give away a later item's key, and consecutive questions must not re-ask what was just asked or modelled.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "224-226",
     "quote": "a token which uniquely identifies one item's key must not appear in another item's stem, options, or feedback anywhere in the same lesson",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "226-227",
     "quote": "The lesson title counts as a surface: RT-10 found the video-2 check answerable from the title alone.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "33",
     "quote": "> **Design rule:** the we-do must **extend** the modeled skill, never replay it.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "3",
   "name_bearing_source": false
  },
  {
   "index": 39,
   "verdict": "keep",
   "reason": "Quotes verbatim, and '5 rounds' matches. Teacher-contract lines 61-62 add a new self-check that is mandatory at generation time.",
   "statement": "Declare each item's class before judging its overlap with teaching: a knowledge check may test what was taught, but a comprehension or transfer item must not test facts the lesson's own teaching used, and this disjointness is checked at generation time.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "84-86",
     "quote": "the same overlap in a comprehension/transfer item is a leak. Mis-classifying the item makes the same text both correct and defective — it took five adversarial rounds to isolate this.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/teacher-contract.md",
     "lines": "59-60",
     "quote": "Authoring a fresh unit (u03 respiratory) REPRODUCED the dose-item leak the hibernation unit took 5 rounds to eliminate",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "88",
     "quote": "list every FACT the dose (I-do/we-do/you-do) uses vs every FACT the MOVE items test — must be DISJOINT (knowledge-CFU items exempt)",
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
   "reason": "Quotes verbatim; 1 of 16, and 118/65/7, match. Two quotes are added to support the different-model and text-shown clauses. Taxonomy line 20 reports 72 decertified, where the re-probe report splits it into 65 plus 7.",
   "statement": "Run the without-text check with the learner's earlier lessons available, under several option orders judged by the worst case, with a model unlike the generator, and with a with-text control, because a single plain run passes items that leak.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "106-109",
     "quote": "the solver receives all prior lesson content (on-ramp pre-teach, ledger state, prior passages) but not the new text; later items must fail. The Rivers calibration caught **1 of 16** items that plain-blind certification missed",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g5-reading/analysis/seq-reprobe-2026-07-07/README.md",
     "lines": "4-5",
     "quote": "The sequence anti-leak gate scored **one** seeded shuffle per item. A leaky ordering item can pass on a single lucky shuffle.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/README.md",
     "lines": "90-92",
     "quote": "After a `1/1` with-passage calibration, `gemini-group/gemini-3.5-flash` solved the item `3/3` plain-blind and `3/3` with prior-course context.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "22",
     "quote": "191 choice items certified on a same-family lane while docs said \"every item blind-probed under a different model family\"",
     "verbatim": true
    }
   ],
   "against": "docs/practice-layer-spec.md lines 109-110: \"This validates the need for the instrument on that bounded sample, not a general yield or course-readiness claim.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep",
   "reason": "Quotes verbatim. README lines 86-91 give the matched history: 0/3 with the older model, 3/3 with the current one. Adds to truths 34 and 5.",
   "statement": "A without-text verdict belongs to the model that produced it, so re-run it with current models, because a newer model can turn an item that passed into a direct leak.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/README.md",
     "lines": "92",
     "quote": "The old context-lift claim does not survive model drift; the item is directly gameable.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "138-140",
     "quote": "the historical context-lift interpretation does not generalize across model versions.",
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
   "verdict": "keep-with-fix",
   "reason": "The G5 quote was not verbatim: the source is a blockquote with a '> ' at every line start, and only one marker was kept. It is now replaced with verbatim lines. The figures (99.5%, 100%, 60% vs 6%, 738/1,516) match.",
   "statement": "Build items to need the text from the start rather than filtering generated clones: in one bank, single- and multi-select items were answerable without the text almost every time, while items constructed for text dependence survived certification ten times as often.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g5-reading/brainlifts/v0.6.qmd",
     "lines": "24-25",
     "quote": "different blind-solve leak rates by question *format*: MCQ 99.5%, MSQ 100% — hot-text 1.67%, > sequence 0%, match 0%, EBSR 0% (cross-family run, 2026-06-23/24).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g5-reading/brainlifts/v0.6.qmd",
     "lines": "26",
     "quote": "**MCQ/MSQ format does not force reading; hot-text, sequence and match do.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "21-23",
     "quote": "construction-first generation survived the anti-leak gate at 60% vs 6% for encyclopedic clones",
     "verbatim": true
    }
   ],
   "against": "courses/g5-reading/analysis/seq-reprobe-2026-07-07/README.md lines 4-5: the sequence gate scored one seeded shuffle per item, so the 0% figure for ordering items was partly an artifact of that.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 43,
   "verdict": "keep",
   "reason": "Both quotes verbatim, and 231/772 = 29.9% matches. Red-team line 17 adds 'A leaky item awards progress' for not reading. Adds to truth 5.",
   "statement": "Remove or replace items known to be answerable without the text instead of only excluding them from gates, because a leaky item still awards progress for not reading.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "233",
     "quote": "G5 shipped with **231/772 (30%) classified known_leaky still live**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "17",
     "quote": "The ledger honestly classifies 231/772 items (29.9%) as known_leaky — excluded from gate instruments, but not removed from the live course.",
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
   "reason": "Quote verbatim. The same line states the consequence that the statement generalises (six formats became five), so it is added.",
   "statement": "After certification removes items, recheck format and coverage, because exclusions can silently drop a whole item format from what learners practise.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "27",
     "quote": "All 20 EBSR items sit in the excluded bucket.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "27",
     "quote": "6-format MAP coverage quietly becomes 5-format on the certified core.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 6 of 6 and 33% match. The source states the dependence rule for diagnostics only, and two-part evidence items rely on Part A by design. The unscoped 'nor depend' overstated it.",
   "statement": "In a two-part item the second part must not restate the first, because restating leaks the answer; and where items are used to diagnose, split dependent parts into independent items, because a miss on the first part says nothing about the second.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "156-157",
     "quote": "6 of 6 sampled two-part evidence items were blind-solvable, with Part B restating Part A",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "402",
     "quote": "If the student fails, you learn about part (a) but nothing about part (b). For diagnostics, split these into independent items.",
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
   "verdict": "keep-with-fix",
   "reason": "This comes from the AP U.S. History Diagnostic BrainLift. The time-trade-off quote (line 308) did not support the statement and is replaced with lines 336, 337 and 397. Line 337 notes about 10 students per course, so each item must isolate one thing by design. The against limits the rule to knowledge domains.",
   "statement": "Items that bundle content knowledge with question-format skill and disciplinary reasoning cannot show what is missing: a diagnostic item isolates one piece of knowledge in the simplest format that answers the question, and a diagnostic is judged by whether the learners it routes learn faster.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "310",
     "quote": "Using test items (such as AP-style exam questions) that confound core knowledge with experience in answering that type of question.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "336",
     "quote": "If a student gets it wrong, you don't know *why* they got it wrong.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "337",
     "quote": "we must ensure, by design, that each item measures one thing cleanly.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "397",
     "quote": "Prefer the simplest format that gives you the diagnostic information you need.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "307",
     "quote": "A diagnostic is good if students who follow its recommendations learn more efficiently than students who don't.",
     "verbatim": true
    }
   ],
   "against": "feedback/feedback2/Reading explorers Transcript (1).txt line 125: \"You wouldn't be able to do a diagnostic comprehension test. We studied this, it doesn't exist.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 47,
   "verdict": "keep",
   "reason": "Quotes verbatim. They come from SPOVs 2 and 4 of the Diagnostic BrainLift, which was built on AP courses. Adds to truths 9, 15 and 49.",
   "statement": "Report knowledge per component with its uncertainty and keep 'not tested' separate from 'not known', since one right answer is not proof of knowledge and one wrong answer is not proof of ignorance.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "343",
     "quote": "An unassessed KC is not the same as a failed KC, and conflating the two is one of the most common errors in diagnostic systems.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "339",
     "quote": "a single correct answer is not proof of knowledge and a single incorrect answer is not proof of ignorance.",
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
   "reason": "Quotes verbatim (AP Diagnostic BrainLift, Insight 9). Lines 383-384, which carry the core claim (about 10 students per course; expert defaults, not data), are added. The against is verified.",
   "statement": "With few learners per course, set item parameters from expert defaults and course structure rather than statistics, label every estimate with how it was made and how much data it rests on, and replace it with live data as responses accrue.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "382",
     "quote": "Estimating a single item's difficulty and discrimination parameters with reasonable precision requires at minimum 100-200 student responses to that item.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "383",
     "quote": "Alpha currently has perhaps 10 students going through a given course at a time.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "384",
     "quote": "It means the parameters must come from expert judgment and structural defaults, not from data.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "3180",
     "quote": "Every pre-use difficulty value must travel with a provenance label (\"pre-use predicted, N=0\") and an uncertainty indicator",
     "verbatim": true
    }
   ],
   "against": "courses/map-proxy-assessment/validity/05_LIMITATIONS.md line 11: for 650 expert-assigned items, \"This means we do not know how hard any individual item actually is for students.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 49,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; ~67% and r≈0.72–0.79 match. The train-teacher quote is at lines 183-184, not 184-185. Line 3174 also supports 'overstate success'. The against is verified at line 3205.",
   "statement": "A model cannot simulate what learners don't know, because its knowledge leaks through role-play, so simulated learners and model-rated difficulty overstate success and must be labelled as predictions, not results.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "3174",
     "quote": "They cannot simulate what students don't know, even when explicitly prompted to adopt a student persona.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/generator-insights.md",
     "lines": "123-124",
     "quote": "LLM student role-play is structurally flawed and caps ~67% accuracy",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/train-teacher-requirements.md",
     "lines": "183-184",
     "quote": "simulated students are a prediction, not a result — sim results are labeled as such everywhere",
     "verbatim": true
    }
   ],
   "against": "Assessment & Feedback BrainLift line 3205: simulation-based estimation \"is promising but not yet production-ready as a primary signal\"; generator-insights.md 123-124: teacher-as-predictor reaches r≈0.72–0.79.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 50,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; r 0.4–0.6 and 0.7–0.87 match. Both preferred methods need calibrated items, which the original omitted; this matters for the cold start in candidate 48. Line 3172 limits direct ratings to a sanity check. The named studies are in the source.",
   "statement": "Estimate item difficulty from extracted features (once enough items are calibrated to train on) or by placing new items against calibrated anchor items, use a model's direct rating only as a sanity check, and distrust any estimate that swings under small rewording.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "3172",
     "quote": "Treat direct rating as a fast sanity check or tiebreaker, not as the backbone of your difficulty engine.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "3184",
     "quote": "Best when you have ≥100 calibrated items to train on. Typical r ≈ 0.7–0.87 with empirical difficulty.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "3196",
     "quote": "if small wording changes cause wild swings in your predicted difficulty, the prediction is probably wrong.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. The digest gives the DOI 10.3389/frai.2026.1851993 at line 6.",
   "statement": "A model's score on teaching-knowledge questions is not evidence that the content it generates teaches well; measure the generated material itself.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/DIGEST-singh-eduqwen-2026.qmd",
     "lines": "34",
     "quote": "strong benchmark performance on pedagogical knowledge questions does not itself constitute evidence of effective classroom tutoring",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "80-81",
     "quote": "the gap must be measured at the artifact level rather than inferred from benchmark scores.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 52,
   "verdict": "keep",
   "reason": "Quotes verbatim. Chance floors (line 58) and pre-committed pass and abort gates (lines 92-100) are in the same contract. Overlaps truths 45 and 70 but adds pre-registration and replication.",
   "statement": "Fix the metric, test set, baselines (including the untrained model on the same inputs), chance floors and pass/abort gates before generating or training, append rather than rewrite any later change, and require two independent runs before claiming a bar is met.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "5-7",
     "quote": "primary metric, test set, baselines, ceiling, and gates are fixed now; any later change is an appended methodology-correction note, never a rewrite.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "53-54",
     "quote": "Isolates what training added; run it or the result is uninterpretable.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "75-76",
     "quote": "any bar-hit claim needs 2 independent generation runs; a single run is a single-point estimate.",
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
   "reason": "Quotes verbatim, and the 191-item count matches. Adds to truth 66 but is about self-certification, so not a duplicate.",
   "statement": "The step that generates content must never certify it: certification, mastery judgments and semantic review belong to a separate lane using a different model family, and every claim of independence must match the build record.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "21",
     "quote": "G5: deploying lane certified its own items until the protocol banned it",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/train-teacher-requirements.md",
     "lines": "269-270",
     "quote": "must remain independent lanes — different agents, different judge families, neither certifies the other's output.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
     "lines": "263",
     "quote": "Do not certify your own authored content.",
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
   "reason": "Quotes verbatim. Gives a general ladder of evidence levels; adds to truths 44 and 48.",
   "statement": "State every claim at the level its evidence reaches — written, machine-checked, verified in the running product, accepted by people, verified in production, or shown to improve outcomes — and never upgrade it by confidence or repetition.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "26",
     "quote": "Authored, mechanically validated, runtime verified, human accepted, production verified, and outcome validated remain distinct states.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "104",
     "quote": "- Claim boundary: A weaker evidence type cannot be upgraded by confidence or repetition.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
     "lines": "98-99",
     "quote": "GREEN is only \"no defect found on the checked dimensions\".",
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
   "reason": "Quotes verbatim. The clause about a judge returning the same verdict for everything overlaps truth 9. The candidate generalises it to checks that could not run or lacked their inputs.",
   "statement": "A check that could not run, lacked its inputs or returned an undiscriminating answer is reported as not evaluable or unverified, never as a pass.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/PROJECTION.qmd",
     "lines": "10",
     "quote": "Use `NOT_EVALUABLE` as a stop signal, never as a pass.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
     "lines": "93-94",
     "quote": "treat as a non-answer (re-ask once, then RED), never as a pass.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "38-39",
     "quote": "gog-unavailable is a loud UNVERIFIED failure, never a pass.",
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
   "reason": "Quotes verbatim; line 116 confirms that all 745 items carry standards. Adds to truth 38 and overlaps candidate 65.",
   "statement": "Before reporting that something is absent, prove the check could have seen it: look everywhere it could live and confirm the selection the check ran on was not empty.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/handoff/timeback-course-explorer/references/eval-analysis.md",
     "lines": "117",
     "quote": "(the morning analyzer missed them because it only scanned `rawXml`; standards are in structured metadata, not inline XML).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "208",
     "quote": "`UNIT=2` instead of `U2` matched no lessons — judged 6% of the corpus, printed ALL PASS",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/edullm-quality-standard/SKILL.md",
     "lines": "16-17",
     "quote": "Never treat an unreturned rule as absent: search is a bounded relevance lookup, not a completeness oracle.",
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
   "reason": "Quotes verbatim; 2/151 and 13/213 with 11 false match. Proving a check catches its motivating example is truth 38. Kept because it adds the requirement to report how often a check fires, with measured cases.",
   "statement": "A new check must report how often it fires and show that it catches the example that motivated it, because a check that fires on everything cannot rank and one that misses its own seed is not measuring it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "94-95",
     "quote": "**A new check must prove it discriminates before it ships.** Report (a) fires/eligible, and (b) that it catches the seed example that motivated it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "95-99",
     "quote": "the first cut of that check fired 13/213 with 11 false",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "203-204",
     "quote": "Break the thing deliberately; confirm the gate fails. **Five gates asserted nothing**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "38",
   "name_bearing_source": false
  },
  {
   "index": 58,
   "verdict": "keep",
   "reason": "Quotes verbatim. The source states 'read checks in review' itself at line 229. Distinct from truth 38: here the check asserts something true about the wrong subject.",
   "statement": "Ask what a check would still pass on: checks can assert something true about the wrong thing, so read checks in review and assert the intended contract rather than whatever string happened to be present.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "219-220",
     "quote": "**a gate that asserts something true about the wrong subject.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "229",
     "quote": "**Read gates in review, not just product code.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "259-261",
     "quote": "Assert the *contract* (\"the head derives from the score\"), not the string that happened to be there.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim; 22 of 30 matches (line 1043). SKILL lines 90-92 give the by-name walk. The against is verified.",
   "statement": "A rule written only in prose is not enforced: turn every human catch into an automatic check in the same cycle, and before closing a review round check each adopted rule against the content by name.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "87-90",
     "quote": "Three consecutive rounds, one unenforced rule. Prose in an addendum gets read, not run.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "1044-1046",
     "quote": "the standard was not missing them, this build shipped without running them.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "144",
     "quote": "3. The ratchet: every human catch becomes a machine check the same cycle —",
     "verbatim": true
    }
   ],
   "against": "skills/course-red-team/SKILL.md lines 108-109: a defect visible only in the running app cannot be a content gate; \"putting it in a content gate manufactures a check that can never be green or red.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 60,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds to truths 24 and 46.",
   "statement": "A finding is closed only when the check that found it passes on the current delivered version: treat reported fixes as claims, re-verify every earlier fix and sweep for new problems the fixes introduced.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "136-137",
     "quote": "Closure = re-run the finder on the current build; \"fixed in <commit>\" is not closure (one item was falsely closed this way).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "101-102",
     "quote": "Round 2: most of an 11-item fix report failed live review, including the original kill exploit.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "172",
     "quote": "re-verify every prior fix line-by-line (closed/half/open) and sweep for issues the fix wave introduced",
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
   "reason": "Quotes verbatim. Not already on the list.",
   "statement": "Never judge a course by its best-looking lesson or a sample: recompute each quality claim across all lessons, report the share that holds, and name what any sample or gate did not cover.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "29",
     "quote": "Unreviewed content cannot inherit the result of a strong sample.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "249",
     "quote": "the completion-gate covered quiz/onboarding lessons but **not the 40 PowerPath expeditions**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "76-77",
     "quote": "8. **Showcase ≠ corpus.** Never grade the one lesson the reviewer already saw — it is the polished one.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim; '39 of 46' and '6 more' match. Overlaps candidate 83.",
   "statement": "Check across lessons, not only one at a time: an answer key must agree with what earlier lessons taught, and 'already seen' must mean seen on every path a learner can take, not on some path.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "141-144",
     "quote": "A child who learned L5 **correctly** was marked wrong.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "152",
     "quote": "> **\"Already seen\" must be an INTERSECTION over branch points, never a union.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "163",
     "quote": "The intersection changed the finding from *\"39 of 46 clean\"* to **6 more real defects**",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. Generic Instruction line 46 gives the safe vague form ('earlier in the course').",
   "statement": "Every reference to earlier learning ('last lesson', 'remember last time') must be true for the actual teaching order; when generation cannot know the neighbouring lesson, use a safely vague phrase.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
     "lines": "47",
     "quote": "an unverifiable relational claim is a defect, not a flourish.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "64",
     "quote": "small bugs jar (\"remember last time\" on the first story; \"inspiration tap\").",
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
   "reason": "Quotes verbatim. Not already on the list.",
   "statement": "When content is generated and then copied or edited, apply every fix both to the generator and to the stored content, and fix a faulty upstream specification at its source before regenerating, because a patch on rendered content is undone by the next regeneration.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "392-394",
     "quote": "A rule fixed in the generator prompt does not reach any lesson already on disk, and a fix applied on disk does not survive the next regen",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
     "lines": "45-46",
     "quote": "A rendered lesson that silently fixes a bad specification does not close the upstream defect because regeneration can reintroduce it.",
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
   "reason": "Quotes verbatim; 98% (53 of 54) matches. Adds to truths 8 and 38 and overlaps candidate 56.",
   "statement": "List every item type and content path a check must cover and assert the list is not empty, because a balancing pass on graded items left the teaching items' answers clustered at one position.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "119-120",
     "quote": "Dose teach MCQs bypassed the QTI debias pass, so rebalancing the graded bank never touched them: hook 69% A, we-do 53% A, **vocab 98% A** (53 of 54).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "127-128",
     "quote": "**Enumerate every item type that carries a key**, then assert the enumeration > is non-empty.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "74-75",
     "quote": "Known scope trap: it once collected only MCQ nodes while breaches lived in narrated text nodes",
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
   "reason": "Quotes verbatim. Line 135 names the check that scores every model answer against its own criteria. Adds to truths 10 and 45.",
   "statement": "Score every model answer against its own rubric, and anchor each pass line with a borderline example rather than only a top-score model.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "132-133",
     "quote": "U2-L6's SCR required the term \"sacrifice\"; its own model answer said \"gave up\".",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md",
     "lines": "83",
     "quote": "each SCR declares the cut *and* carries a **borderline** exemplar at that cut — not only a top-score model",
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
   "reason": "Quotes verbatim. The hint clause had no quote; FEEDBACK-LEDGER line 396 records exactly that case and is added. Overlaps truths 1 and 11. The against is verified.",
   "statement": "Feedback attached to a branch must be true for every answer routed to it and must use what the learner actually said; a reply that would read the same whatever the answer is not feedback, and a hint must add something the learner has not already written.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "26-28",
     "quote": "must be true for EVERY index classified into that branch",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback 4/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "71",
     "quote": "A reply that would read the same no matter what the child answered is not a third turn.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "396",
     "quote": "When I press the hint, it just tells me to say where the hornets go. The answer already does this.",
     "verbatim": true
    }
   ],
   "against": "Opportunities to Respond BrainLift line 70: \"because children often do not notice a recast, it does not reliably teach one specific point\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 68,
   "verdict": "keep",
   "reason": "Quotes verbatim, and 18/18 matches. The delayed 'I'm not sure' clause rests on the same BUILD-RULES evidence already filed under open truth 55; the reachability clause is new.",
   "statement": "Test that every adaptive branch can actually fire — especially the one for a learner who freezes — and offer an 'I'm not sure' route only after a delay, because shown up front it becomes the easy way out.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "187",
     "quote": "branch authored + gated in 18/18 but **can never fire**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "876-878",
     "quote": "**An escape hatch offered up front stops being an escape hatch.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "97",
     "quote": "Every branch is reachable in tests; correct, partial, misconception, off-topic, silence, error, and missing-data routes receive semantically appropriate next moves.",
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
   "reason": "Quotes verbatim. The 40- and 60-word caps are a Grade 3 bar, set against that grade's passage length, so they are removed from the general statement. Overlaps candidate 25.",
   "statement": "Keep corrective feedback short, mechanically clean and at or below the learner's reading level, and never longer than the text it refers to, because feedback longer or more complex than the original teaching has become new teaching.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "31-32",
     "quote": "A grade-3 child will not read feedback longer than the passage (round-2 verified: our generator's median was ~91 words).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "94-95",
     "quote": "if corrective feedback is longer or more complex than the original instruction, the item has crossed into new instruction.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. General, and not already on the list.",
   "statement": "Whenever a prompt or feedback asks the learner to look back at the source, keep the source visible, and place each question beside the text it asks about.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "38-40",
     "quote": "Whenever feedback or a prompt asks the student to cite or look back at the text, the text must be visible.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "140",
     "quote": "15. Put the check **next to** the text, not below (below = split attention, scrolling up to find the answer).",
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
   "reason": "Quotes verbatim; the meeting quote includes the blockquote markers. The against is verified at lines 32-33. Adds to truth 28.",
   "statement": "Interrupt passive content with a meaningful, non-bypassable response at least every minute or so, because anything skippable without consequence gets skipped.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
     "lines": "35",
     "quote": "No continuous passive segment beyond ~60s.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
     "lines": "37",
     "quote": "\"Pause and think\" is not an active check: anything skippable without consequence is skipped.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/meetings/incept-service-coe-2026-08-10/MEETING-EXCERPTS.qmd",
     "lines": "27-28",
     "quote": "> A user could complete the entire course simply by clicking through the green buttons without > engaging with the material.",
     "verbatim": true
    }
   ],
   "against": "MEETING-EXCERPTS.qmd lines 32-33: reading, listening, transition and accessibility steps \"use task-appropriate completion evidence rather than decorative clicks.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 72,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The evidence concerns children ('poor judges of what they can skip'), so the claim is scoped to young learners. The against, that skipping can be earned through mastery, is folded into the statement.",
   "statement": "Don't let young learners skip or speed up instruction on their own judgment, because they judge poorly what they can skip — skipping must be earned by repeated mastery — but let them advance modelled steps themselves on a tap rather than on a timer.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "58",
     "quote": "- No child control over pace or skipping (children are poor judges of what they can skip).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "310-311",
     "quote": "A timer also cannot pace itself to a slow reader. Tap-to-continue satisfies both.",
     "verbatim": true
    }
   ],
   "against": "Direct Instruction BrainLift line 19: \"**Require students to earn Test Out through repeated mastery on prior lessons**\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 73,
   "verdict": "keep",
   "reason": "Quotes verbatim; '7–8' and '~2' match. The against is verified.",
   "statement": "Comprehension work must make learners produce — say, write, explain — and counts of productive responses must discount trivial echoes, because a high response rate reached through recognition is not quality.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback 4/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "23",
     "quote": "A high number of responses per minute is not evidence of quality if the app reached that number by asking only recognition questions.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "183",
     "quote": "but 2–3 were trivial *say-backs* (repeat a word) and the real generative-comprehension production was ~2",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback 4/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "30",
     "quote": "If a child never has to compose or explain an answer, the app cannot tell whether the child understood",
     "verbatim": true
    }
   ],
   "against": "Assessment & Feedback BrainLift line 354: \"For diagnostic assessment, the much-maligned MCQ is not a compromise — it is the optimal format.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 74,
   "verdict": "keep",
   "reason": "Quotes verbatim. The point was raised in two review rounds.",
   "statement": "Have learners locate evidence in the text first and then explain it in their own words; a task that asks them to copy a sentence and paraphrase it in the same box teaches copying.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "215",
     "quote": "Highlight/underline in the text first, then write in own words; or split into two parts.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "54-55",
     "quote": "Reverse to **find-and-highlight the sentence FIRST, then write it in your own words**;",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 75,
   "verdict": "keep",
   "reason": "Quotes verbatim. The purpose clause had no quote; FEEDBACK_RESPONSE line 21 states it and is added. Adds to truth 40 and is in tension with truth 7, as the against shows.",
   "statement": "Set a purpose before the learner meets the source, let them encounter the whole source before close modelling, and open each section by linking to what was just learned.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "21",
     "quote": "1. **Set a purpose for reading BEFORE reading.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "317",
     "quote": "Complete a first encounter with the whole text before close modelling or analysis.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "302-303",
     "quote": "the defect it catches is a section that is individually well-written and contextually cold",
     "verbatim": true
    }
   ],
   "against": "skills/course-red-team/references/finding-taxonomy.md line 205: \"stop at key points INSIDE the text and ask right there (REL West), not only at the end\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 76,
   "verdict": "keep",
   "reason": "Quotes verbatim (excerpts from IES video transcripts). The 10-minute and 35/10-minute figures match. Adds to truth 20.",
   "statement": "Keep background-knowledge building short — about ten minutes — so most of the lesson is spent in the main text, optionally preceded by an easier text on the same topic.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/knowledge-scaffolds-bridge-canopy-cap.md",
     "lines": "23",
     "quote": "\"At the same time, activating or building background knowledge should take 10 minutes or so.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/knowledge-scaffolds-bridge-canopy-cap.md",
     "lines": "25",
     "quote": "a teacher spent 35 minutes activating and building background knowledge, and then 10 minutes where the kids actually read.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/knowledge-scaffolds-bridge-canopy-cap.md",
     "lines": "19",
     "quote": "\"asking students to read an easier brief passage before presenting the higher-level text on the same topic\"",
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
   "reason": "Quotes verbatim. Holds for any text-based teaching.",
   "statement": "Choose each practice text so the taught move is actually needed on it, and rate surface difficulty and conceptual difficulty separately, because a familiar or predictable text lets learners succeed without the process.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/strategy-text-fit.md",
     "lines": "7",
     "quote": "Pick the passage *after* you pick the target strategy, and pick it so the strategy is the only way through.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/strategy-text-fit.md",
     "lines": "13",
     "quote": "but also the comprehension demands of the text how hard is it to understand this text these two things are not always aligned",
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
   "reason": "Quotes verbatim; the synthesis quote ends at line 110. The finding is from RAND, Appendix A, pages 107-108.",
   "statement": "Text difficulty depends on what the reader already knows: highly cohesive text helps low-knowledge readers but can lower deep understanding for high-knowledge readers, and harder texts become accessible as knowledge builds.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd",
     "lines": "106-110",
     "quote": "A coherent text base slightly enhanced recall, but actually lowered performance on tests that tapped the mental model.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "114-115",
     "quote": "7. Text difficulty is a match among text factors, reader knowledge, and task — no single readability number can gate a text",
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
   "verdict": "keep",
   "reason": "Quotes verbatim; cohesion 0.17 vs 0.58 matches. The G5 red-team (line 29) confirms 772 of 772 items were never human-reviewed. Adds to truth 44.",
   "statement": "Treat generated texts and items as untrusted until a person has read at least a sample: code screens for syntax, vocabulary and cohesion reject and queue, never approve, because generated texts tend to run too hard and cohere poorly.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/text-quality-lane.md",
     "lines": "5-6",
     "quote": "the machine stage never approves, it only rejects and orders the queue.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/text-quality-lane.md",
     "lines": "34-37",
     "quote": "On a clean target-quality sample: cohesion 0.58, passes. The screen discriminates; it does not approve.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "263",
     "quote": "even a sampled ~60-item review converts \"0 human-reviewed\" into \"sampled + attested\"",
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
   "reason": "Quotes verbatim. The same BrainLift line makes the misconception check mandatory for all science text.",
   "statement": "Text that carries another subject's content must pass that subject's misconception check — banned phrasings plus a meaning-level probe, because a misconception can be implied without the phrase — and every simplified model or diagram is framed as a simplification.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md",
     "lines": "24",
     "quote": "Good science instruction is undone by encounters with folk science that is intuitively appealing but scientifically incorrect.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "145",
     "quote": "\"the plant grows by taking food from the soil\" implies plants-eat-soil without the literal phrase",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "147",
     "quote": "a food chain / atom / cell diagram presented as literal reality",
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
   "reason": "Quotes verbatim. Not already on the list.",
   "statement": "Simplify only in ways that stay accurate and will not block later learning, because early everyday wording can plant misconceptions that later courses must undo.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "802",
     "quote": "- Claim boundary: Simplification is acceptable only when it remains accurate and does not create a later-blocking misconception.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "136-137",
     "quote": "it actively undoes correct science instruction (the ATP case: even students who learned it right get re-taught the error).",
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
   "reason": "Quotes verbatim; the ATOMS quote is AP U.S. History atom RHBL-031, scoped to that subject. Two clauses lacked quotes: the BrainLift's science rule (line 25) and its social-studies rule (line 21) are added. The claim-bounding clause is scoped to history and social studies. The against is verified.",
   "statement": "When a course meets knowledge taught elsewhere, reinforce that framing rather than redefine it, approach a topic already met from a fresh angle rather than repeating it, prefer re-meeting ideas to being the first place a learner meets them, and in history and social studies keep fact, interpretation and opinion distinct and bound claims by actor, place, period and source.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md",
     "lines": "14",
     "quote": "the Read/Write lesson should be consistent with how it was framed in the subject app — vocabulary, level of nuance, framing.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md",
     "lines": "11",
     "quote": "The aim is for the re-encounter to feel like a new angle, not a repeat.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md",
     "lines": "25",
     "quote": "It is better to re-encounter ideas from earlier grades than to be the first place a student meets an idea.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md",
     "lines": "21",
     "quote": "distinguishing fact, interpretation, and opinion is part of what social studies *is*.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "488",
     "quote": "Bound historical claims by actor, region, period, institution, and source function rather than flattening them into generic narratives.",
     "verbatim": true
    }
   ],
   "against": "feedback/feedback3/FEEDBACK_RESPONSE.md line 128: tension with a push for more fiction, \"Log as a question, not a silent rebalance.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 83,
   "verdict": "keep",
   "reason": "Quote verbatim. The coherence BrainLift (line 4) makes the same point: without integration 'we cannot be sure whether a student has studied a topic'. Overlaps candidate 62.",
   "statement": "If learners choose their own path or order, the course cannot assume which knowledge they have met, so sequencing and retrieval must rest on what every path guarantees.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "65",
     "quote": "because the child picks their character and flow isn't fixed, you can't be sure which knowledge/folktales they've met — undermines retrieval and sequencing.",
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
   "reason": "Quotes verbatim; the evaluator-spec quote starts at line 230.",
   "statement": "Declare whether each check is teaching practice, a gating assessment or a transfer benchmark, judge each by its own criteria, and put mastery thresholds only on gates.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "230-231",
     "quote": "the three teaching lessons and the transfer lesson behaved as 90% practice-test gates over their own formative checks.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "90-92",
     "quote": "the declaration lets the evaluator judge teaching checks by teaching criteria and interval forms by assessment criteria instead of judging one by the other's bar.",
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
   "reason": "Quotes verbatim; the ATOMS quote is AP U.S. History atom RHBL-029, corroborated by the reading sources. Adds to truth 48.",
   "statement": "Keep a sealed transfer test whose topics never appear in teaching material, generation prompts or training data; it is never a gate and never taught from.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "71",
     "quote": "The cold benchmark is **never a mastery gate and never teaching material**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "71-72",
     "quote": "A model trained on a cold topic cannot be evaluated on it.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "470",
     "quote": "Keep held-out assessment sources separate from lesson-visible teaching and practice sources.",
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
   "reason": "Quotes verbatim. Not already on the list.",
   "statement": "Preview and review access must never create learning evidence: free navigation, answer reveals and resets leave mastery, rewards and progress unchanged.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "34",
     "quote": "Free navigation, answer reveal, reset, and reviewer-only controls leave mastery, reward, completion, and unlock records unchanged.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "152-153",
     "quote": "a reviewer mode that unlocks lessons **without minting mastery evidence**",
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
   "reason": "The eval-criteria quote dropped the blockquote markers at line starts and is corrected to verbatim. Gating every check is truth 28. Kept as added evidence for why: a bypass moves learners past knowledge they lack and poisons the outcome data. The against is verified.",
   "statement": "A gate learners can bypass is a teaching failure, not only a security gap: it moves them past knowledge they lack and poisons the outcome data used to improve the content.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "58-61",
     "quote": "it places the child outside their zone of proximal development *by construction* — advanced past knowledge they don't hold, or held below knowledge they do.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/timeback-course-eval/references/eval-criteria.md",
     "lines": "134-136",
     "quote": "a gate that doesn't require reading > produces a *poisoned feedback signal* — kid-outcome data from a gameable course can't improve > the generators.",
     "verbatim": true
    }
   ],
   "against": "STANDARD.qmd (v1.0.0) line 535: \"Claim boundary: Anti-gaming controls must not block legitimate accessibility paths.\"",
   "general": true,
   "duplicate_of": "28",
   "name_bearing_source": false
  },
  {
   "index": 88,
   "verdict": "keep",
   "reason": "Quote verbatim, from a design memo. The Assessment & Feedback BrainLift (line 775) independently says to change approach when learning gain is flat, and is added. Overlaps candidate 29.",
   "statement": "Treat gaming and misunderstanding differently: rapid guessing and hint abuse get an integrity response, while flat learning gain, not merely low accuracy, triggers re-teaching.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md",
     "lines": "72",
     "quote": "The load-bearing signal is **flat gain, not low accuracy**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md",
     "lines": "72",
     "quote": "rapid-guessing and help-abuse get an integrity response, not reteaching.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "775",
     "quote": "When evidence is decisive, stop early; when ambiguous, gather more; when flat learning gain, change approach.",
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
   "reason": "Quote verbatim, inside the cited range. The same line says a contract validator enforces it. Adds to truths 4 and 1 but is distinct: it is about honesty in what counts as the learner's success.",
   "statement": "When the system fills in an answer after repeated misses, say so, and never present it as the learner's success.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md",
     "lines": "136-137",
     "quote": "on a second miss, fill the slot with the correct ending and say so — never dress a filled answer as a child win",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but the RED_TEAM_R1 quote runs to line 45, not 44. The '~150 is invented (actual = 48)' case is at lines 38-39. Adds to truth 50 and overlaps candidate 94.",
   "statement": "Every number in course documents carries a source, comes from one dated record that readers can recompute, and is never borrowed from another course or copied from a summary without recomputing it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "262",
     "quote": "G5 certified-count drifted **541 vs 549 vs 559** across docs",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/RED_TEAM_R1.md",
     "lines": "43-45",
     "quote": "a number that reads authoritative and is wrong, inherited from a research-agent summary I did not independently recompute before writing it down.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "29-30",
     "quote": "2. **Never invent a magnitude.** Do not carry another grade's/cohort's numbers as if they were this one's.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim; 0.928 vs 0.930 and RMSE 4.12 vs a 4.0 target match. Not already on the list.",
   "statement": "Summaries must match the reports beneath them: never round a value across its threshold, never drop the failing metric, and label each result by what it actually measures.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "9",
     "quote": "Summary tables reported reliability as \"0.930 ✅\" against a ≥0.93 benchmark the underlying reports state as 0.928, below",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "10",
     "quote": "The one failing metric (RMSE 4.12 vs <4.0 target) was omitted from every summary table",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "34",
     "quote": "now \"internal cross-bank consistency (synthetic),\" explicitly not MAP agreement",
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
   "reason": "Quotes verbatim; 0.007 vs 0.707 and 77→50→45 match. A general truth about outcome data, not already on the list.",
   "statement": "Compute outcome rates over the learners actually enrolled, from one consistent source, and compare the same learners over time, because the wrong denominator or mixed populations manufacture failures and declines.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g2-reading/analysis/dropout-3-data-integrity.md",
     "lines": "12",
     "quote": "**The headline \"low completion\" numbers are ~90% MEASUREMENT ARTIFACT, not abandonment.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g2-reading/analysis/dropout-3-data-integrity.md",
     "lines": "29",
     "quote": "the course that looked catastrophic at `avg_pct = 0.007` — actually shows the **highest** average completion of the bunch (0.707)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-1-data-integrity.md",
     "lines": "14",
     "quote": "2. **The \"G1→G3 slide (77→50→45)\" is a Simpson's-paradox / season-composition artifact, not a within-student decline (FATAL to the causal framing).**",
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
   "reason": "Quotes verbatim; 196.0, the 46th percentile and n=915 match. Adds to truths 48 and 51.",
   "statement": "Published research can justify a design but does not show that a particular course works; until outcome data from its own learners exists, claim only direction and a validation plan.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/PRIORITIES.qmd",
     "lines": "81-83",
     "quote": "this corpus grounds DESIGN, it does not prove OUR implementation works. Never cite it as evidence about our courses' outcomes.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/course-quality.qmd",
     "lines": "81",
     "quote": "Synthetic prediction, IB scores, or reviewer approval are not outcome evidence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "262",
     "quote": "the real figure was **196.0 / 46th pctile (n=915)**. No RIT/growth number pre-pilot; direction, not magnitude",
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
   "reason": "The grade-band-profiles quote dropped a blockquote marker inside it and is corrected to verbatim. The practice-spec quote is verbatim. Overlaps the third clause of candidate 90.",
   "statement": "Bars, yields and magnitudes measured in one course, grade or cohort do not carry to another without recalibration; mark unknown values as to-be-sourced rather than borrowing them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "139-140",
     "quote": "Historical G5 volume does not validate a G3 estimate.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/grade-band-profiles.md",
     "lines": "17-18",
     "quote": "Every cell cites > its source; empty cells are `[TO SOURCE]` — **never invent them**.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 95,
   "verdict": "keep",
   "reason": "Quotes verbatim; the ATOMS quote is a G7 atom. General.",
   "statement": "A course for a different level must differ on the dimensions that change with level — text demand, stamina, formats, and the knowledge and operations to master — not just in topics or harder texts.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/grade-band-profiles.md",
     "lines": "8-10",
     "quote": "> A course for grade N must be **demonstrably different** from its siblings on the > dimensions below",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "416",
     "quote": "Differentiate adjacent grades by the knowledge and operation learners must master rather than cloning a sibling course with harder text.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. The against is verified at lines 229-230.",
   "statement": "Choose item formats to match what the knowledge requires and what the target test and the learner's level demand: cover the test's formats, drop formats too advanced for the level, and require production where the target is production.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/generator-insights.md",
     "lines": "102",
     "quote": "The incumbent's #1 measured failure was 100% single-select MCQ vs MAP's 6 formats.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "122",
     "quote": "\"Write/explain/draw\" targets cannot be assessed by MCQ alone.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "77-78",
     "quote": "**EBSR / two-part evidence items are ~grade-4+**; do not ship them at G3.",
     "verbatim": true
    }
   ],
   "against": "courses/g3-reading/iteration-6/distilled/07-SCORING-FEEDBACK-XP.md lines 229-230: the same reviewers called two-part items \"well built\" and later \"likely developmentally inappropriate for grade 3\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 97,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 58–217 words vs about 2,740, and about 22% vs 40%, match. 'Never builds stamina' overstated the source, which says only to ramp length toward test stamina.",
   "statement": "Plan text length and genre mix toward the target test's reading load from the start rather than backfilling, because practice on short single texts does not build the stamina that long multi-text tests demand.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "224",
     "quote": "G3 passages were 58–217w when the test reality is multi-passage (~2,740w); ramp length toward test stamina",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "166",
     "quote": "G3 was flagged at **~22% literary vs ~40% target** because texts were picked on Lexile alone",
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
   "reason": "Quotes verbatim; 9 builders, 80% and 74% match. Line 55 gives 87–95% tagging accuracy. The against is verified. Adds to truths 57 and 66.",
   "statement": "Prefer assembling, transforming and tagging vetted material over inventing items from scratch, and treat generator output as a candidate until a separate check certifies it.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/generator-insights.md",
     "lines": "56-57",
     "quote": "But of 9 Gen-AI quiz builders studied, **80% of items violated ≥1 best-practice guideline and 74% had major flaws — only 1 in 5 usable**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/generator-insights.md",
     "lines": "90",
     "quote": "**Treat generator output as *candidate* until a separate check passes.**",
     "verbatim": true
    }
   ],
   "against": "docs/practice-layer-spec.md lines 21-22: construction-first generation under certification survived at 60% vs 6% for clones.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 99,
   "verdict": "keep",
   "reason": "Quote verbatim, inside the cited range. A general design principle; adds to truths 3 and 67.",
   "statement": "Where possible make a rule impossible to break by construction — for example, never give a generator or scorer the text before the learner has read it — instead of relying on a check to catch the breach.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "46-47",
     "quote": "so it *cannot* quote what the child hasn't read. A rule you can't violate beats a rule you must remember.",
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
   "reason": "Quotes verbatim; 117 of 179 matches. Adds to truths 17 and 24.",
   "statement": "Narration must match the on-screen text word for word, checked by exact whole-line identity rather than substring matching, because text edits silently leave stale or missing audio.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "1085-1086",
     "quote": "found 117 of 179 narrated strings already orphaned by the round's own rewrite",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "1099-1100",
     "quote": "**a drift check that tolerates prefixes silently exempts every string that was EXTENDED, and extension is the most common shape of a feedback edit.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "115",
     "quote": "- Audio: printed==spoken; frozen TTS voice/style prompts; holds land ON mark",
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
   "reason": "Quotes verbatim; the source tags them as learning evidence plus heuristics. The against is verified, quoted without the bold markers. Adds to truths 21 and 23.",
   "statement": "In narrated media let the audio set the timing: nothing is revealed before it is spoken, one new label appears at a time, music stays off under teaching speech, and the voice is never stretched to fit the visuals.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "30",
     "quote": "Audio is the MASTER CLOCK. Schedule every visual event off forced-alignment word timestamps. A reveal MUST NOT complete before its term is spoken.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "31",
     "quote": "5. NEVER time-stretch the voice to fit visuals. Re-cut visuals instead.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "46",
     "quote": "20. Music/SFX OFF under teaching narration; any intro/outro bed ≥20 dB below speech; an SFX must have an instructional job.",
     "verbatim": true
    }
   ],
   "against": "video-generation-human-v0.2.md line 285: \"120–145 wpm is an [OH] from adult anchors.\" (the pacing band for children is not established).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 102,
   "verdict": "keep",
   "reason": "Quotes verbatim; g−0.21 and g−0.36 match. The against is verified.",
   "statement": "Don't speed up narration or playback to save time: playing instruction at 1.4–1.5× costs about g = −0.21 and at 1.8–2× about g = −0.36.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
     "lines": "195",
     "quote": "Artificially speeding playback costs learning (1.4–1.5× ≈ g−0.21; 1.8–2× ≈ g−0.36) [21].",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "33",
     "quote": "1. **No user-controlled audio playback speed** — kids rush; enforce a consistent age-appropriate rate.",
     "verbatim": true
    }
   ],
   "against": "video-generation-human-v0.2.md line 284: \"The corpus skews adult/higher-ed; middle-school holds (~g 0.45) but elementary is non-significant [1].\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 103,
   "verdict": "keep",
   "reason": "Quotes verbatim. The line-233 fragment is replaced with the full sentence (233-235). Lines 238-239 are added as evidence that a fade promised in prose never happens. The against is verified; in tension with open candidate 143.",
   "statement": "Fade scaffolds across a unit as learners gain expertise, and record each scaffold's retirement condition as data with counts that only fall, because a fade promised in prose never happens.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
     "lines": "138-140",
     "quote": "But the same scaffolding can harm relative experts (expertise reversal) [12].",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "233-235",
     "quote": "Prose in an authoring note does not satisfy D1.13, and a gate must fail **by name** on a scaffold that has no fade record",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "238-239",
     "quote": "\"states a condition\" is satisfiable by a sentence in a document nothing reads, so nothing ever fades.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "248",
     "quote": "- **Counts are monotonically non-increasing across the unit.**",
     "verbatim": true
    }
   ],
   "against": "docs/teaching-reading-comprehension-brainlift.md lines 68-70: whether taught routines fade or are retrieved on a schedule is a held, open dispute (T2).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 104,
   "verdict": "keep",
   "reason": "Quotes verbatim. The line-306 fragment is extended through 307.",
   "statement": "Tag every design rule with the kind of evidence behind it and never cite an operating heuristic as a proven threshold; discount effect sizes reported by a principle's originators, and let the course's own delayed-outcome data override cited effects.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "19",
     "quote": "- `[OH]` operating heuristic (current guess; has owner + validation experiment; NEVER cite as a proven learning threshold).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
     "lines": "293",
     "quote": "- **Effect sizes inflate when a principle's originator is an author;** we cite conservative independent numbers and treat any single effect as a direction.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
     "lines": "306-307",
     "quote": "when our own delayed-recall data contradicts a cited effect, our data wins and this document is edited.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 105,
   "verdict": "keep",
   "reason": "Quotes verbatim. The scoring-feedback distillation (section 6) follows the same rule.",
   "statement": "When sources or rulings conflict, record the conflict as a named open question with an owner and enforce neither side until it is decided; never average it or settle it silently.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/train-teacher-requirements.md",
     "lines": "253-254",
     "quote": "the conflict is logged as a named tension and reserved for a working session — never silently resolved in either direction",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/crosswalk/CONFLICT-LEDGER.qmd",
     "lines": "20",
     "quote": "do not enforce an ordered DECODE sequence until the curriculum owner resolves it.",
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
   "reason": "Quotes verbatim. The boundary note in ATOMS.json likewise refuses to turn a course-specific decision into a universal rule.",
   "statement": "Keep every source statement as retained, with its scope and provenance; indexing or summarising a source never makes it an accepted universal rule, and compressed summaries never replace the source as the authority.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/AUTHORITY.qmd",
     "lines": "10",
     "quote": "Source atoms are never silently deleted, merged, universalized, or promoted.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/AUTHORITY.qmd",
     "lines": "22-23",
     "quote": "Conflicts remain open and source-faithful until an evidence-bound decision resolves them.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/README.qmd",
     "lines": "29-30",
     "quote": "not receive `PRIORITY` retrieval metadata or become accepted requirements merely because they were indexed.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. No source tells you to check that an extraction 'reaches the document's end'. The evidence says only that quote checks prove presence, not full coverage, so the clause is rewritten. Overlaps truth 17.",
   "statement": "Copy source text into a knowledge store by file rather than having a model retype it, verify every quoted span and citation against the source in code, and don't treat verified quotes as proof that the extraction covered the whole source.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/knowledge-ingest/SKILL.md",
     "lines": "71",
     "quote": "never re-type source text through a model.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/EXTRACTION_EVIDENCE.qmd",
     "lines": "34-35",
     "quote": "The four EduQwen checks establish presence in the scoped extraction only, not full-paper coverage.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/IES-CORPUS-REVIEW-2026-08-05.md",
     "lines": "24-25",
     "quote": "So **no citation here rests on the reviewer model's say-so.**",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, but the BUILD-RULES quote runs to line 1117. The same-method clause overlaps truth 35; the rule about recurrence across independent sources is new.",
   "statement": "Treat a finding that recurs across independent sources as a rule and one seen once as a candidate, and never count two checks that agree by the same method as corroboration.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/IES-CORPUS-REVIEW-2026-08-05.md",
     "lines": "17-18",
     "quote": "Findings that recurred across *independent* batches were treated as high-confidence; a technique seen once was treated as a candidate, not a rule.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "1115-1117",
     "quote": "**Two agents independently agreeing via the same blind method is not corroboration; it is one unverified claim counted twice.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "208-209",
     "quote": "Two independent instruments landing on one item is the strongest signal in the document",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 109,
   "verdict": "keep",
   "reason": "Quotes verbatim; 4 of 6 matches. Section 4 of the file lists every clause of the statement.",
   "statement": "Before filing a defect in learning content, check whether it was requested, capture the whole page over time before claiming nothing happened, wait out designed timers, separate environment faults from content faults, and publish how many findings were retracted.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "134-136",
     "quote": "Publish the correction rate when findings are disputed (ours: 4 of 6 blockers retracted on the first uncalibrated sweep",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "129",
     "quote": "3. **Wait out the designed timer** (compute it) before calling a gate broken.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "172",
     "quote": "*A finding that rests on a checkable factual error damages the audit more than the package*",
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
   "reason": "Quotes verbatim. Caveat: the source's figures do not reconcile as worded (392 − 104 = 288, but the source reports 284 here and again at SKILL lines 399 and 412), so the statement rightly carries no count.",
   "statement": "Write each finding as one falsifiable problem with exact evidence, why it matters, the exact location, a specific change and the rechecks needed, and report counts as raw, exempted and real with the exemption rule stated.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/course-json/README.md",
     "lines": "115-116",
     "quote": "A failure additionally needs one falsifiable problem, exact evidence, why it matters, an exact target object/path, a specific proposed change, a repair-owner skill, and named rechecks.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "103-104",
     "quote": "sweep read 392 raw; 104 were play-script speaker labels and a skill name; the real number was 284.",
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
   "reason": "Quotes verbatim; 0/55 and 0/7 match. The against is verified. Adds to truth 50.",
   "statement": "Review one frozen version per round and bind every piece of evidence to the exact content it checked, so any relevant change withdraws that evidence and forces the affected checks to rerun.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "148-149",
     "quote": "mid-flight main movement has invalidated in-progress rounds three times.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "35",
     "quote": "Evidence records carry artifact and dependency digests; relevant changes force the affected checks to be rerun.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
     "lines": "136-137",
     "quote": "current build it matches 0/55 lesson digests and 0/7 showcase digests",
     "verbatim": true
    }
   ],
   "against": "STANDARD.qmd (v1.0.0) line 216: \"Claim boundary: Unrelated changes need not invalidate scoped evidence.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 112,
   "verdict": "keep",
   "reason": "Quotes verbatim. The against is verified.",
   "statement": "When improving content, protect verified strengths with regression checks so that changes do not flatten what already helps learners.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "33",
     "quote": "Improvement never flattens or deletes behavior that already benefits learners.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "8",
     "quote": "## What's landing well (KEEP — do not break these)",
     "verbatim": true
    }
   ],
   "against": "STANDARD.qmd (v1.0.0) line 184: \"Claim boundary: A different implementation may be preserved when it meets the same outcome with equal or stronger evidence.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 113,
   "verdict": "keep",
   "reason": "Quotes verbatim. Related to truth 23 but about refining a whole course.",
   "statement": "When refining an existing course, work on a copy, preserve every original item, add new material as separate layers, and prove nothing was dropped with an item-level audit.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/source-course-refinement.qmd",
     "lines": "5",
     "quote": "The refined clone adds compliance, delivery, assessment, and evidence layers without cutting source content.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/source-course-refinement.qmd",
     "lines": "47",
     "quote": "| No silent cuts | Missing source ids fail the build. |",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 114,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, and 0/432 matches. 'Every writer and marker' is reworded to avoid role words. The clean-room line 61 is added to support the missing-rubric case. Adds to truths 33 and 69.",
   "statement": "Give every scored task an evidence contract — the knowledge it licenses, the claim, evidence indicators, conditions, scoring rule, acceptable variants, near-misses and forbidden shortcuts — because a goal written only in prose lets each reader imagine a different task, difficulty and pass bar.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "541",
     "quote": "Two people can read the same prose KC and imagine completely different tasks, difficulty levels, and acceptance thresholds",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md",
     "lines": "52",
     "quote": "The banks today carry **zero** `kc`, `scoring_rule`, or `cue`/`supports` fields (verified: 0/432).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
     "lines": "21",
     "quote": "A KC without a pack is prose, not a construct.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd",
     "lines": "61",
     "quote": "4. The constructed response has no rubric, acceptable variants, near misses, scorer, or feedback contract.",
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
   "reason": "Quote verbatim. Line 1471 is already filed under truth 56, so this duplicates 56. Kept because it adds the switch thresholds (about 15–20 variants, the key edited twice). The against is verified.",
   "statement": "Mark short written answers with a small rubric rather than an ever-growing list of accepted strings, and switch once the list passes about 15–20 variants or the key keeps being patched.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1470-1474",
     "quote": "- Switch to a rubric if any of these are true: - Your “acceptable answers” list exceeds ~15–20 variants. - You’ve edited the key twice post-launch to add more exceptions.",
     "verbatim": true
    }
   ],
   "against": "Assessment & Feedback BrainLift line 1469: \"Reserve full automation for numeric/diagram/property-based tasks with explicit tolerances.\"",
   "general": true,
   "duplicate_of": "56",
   "name_bearing_source": false
  },
  {
   "index": 116,
   "verdict": "keep",
   "reason": "Quotes verbatim; 44 of 48 matches. FEEDBACK_RESPONSE line 52 is added to support the two-option clause. The against is verified.",
   "statement": "State in each multi-select stem how many options to choose and declare its scoring rule, and keep two-option and true/false items out of decisions because guessing swamps them.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md",
     "lines": "35",
     "quote": "Today **44 of 48** MSQ stems cue this; **4 do not**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/course-quality.qmd",
     "lines": "40",
     "quote": "- explicit count in multi-select stems;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1403",
     "quote": "These formats are unusually sensitive to guessing, cueing, and ambiguous category boundaries",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "52",
     "quote": "A 2-option yes/no is a 50/50 guess.",
     "verbatim": true
    }
   ],
   "against": "Assessment & Feedback BrainLift line 2008: \"In bundles of 15+, the guessing averages out and T/F becomes more defensible.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 117,
   "verdict": "keep",
   "reason": "Quotes verbatim; '12 of 46' and '8×' match. The 'first heavy use' rule (line 71) is added. The against is verified. Adds to truth 18.",
   "statement": "Taught words must appear in the text the learner reads, be taught where the text first leans on them heavily, stay distinct from each other with none inside another's definition, and come back for the learner to use later.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "53",
     "quote": "12 of 46 taught words appeared nowhere in their own lesson's",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "71",
     "quote": "The rule is **first heavy use**, not peak use.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "62",
     "quote": "self-check: no target word appears inside another target word's definition.",
     "verbatim": true
    }
   ],
   "against": "courses/g3-reading/iteration-2/approval-package-v2/sources/VOCAB-AUDIT.md line 51: deliberate \"contrast pairs\" taught in parallel can legitimately share definition wording.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 118,
   "verdict": "keep",
   "reason": "Quote verbatim. A single source, but the test logic stands on its own.",
   "statement": "In a word-meaning check every distractor must be a word the lesson taught, because an untaught distractor can be eliminated by unfamiliarity and so tests nothing.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "73-74",
     "quote": "A distractor naming an untaught word can only be eliminated by unfamiliarity, so it tests nothing.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 119,
   "verdict": "keep",
   "reason": "Quotes verbatim. The method-over-property clause had no quote; addendum lines 137-138 state it and are added. Adds to truth 18.",
   "statement": "Give each taught concept one definition used verbatim on every surface, complete enough that it does not teach a different concept, and define it by what the thing does rather than a property it happens to have.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "106-107",
     "quote": "A taught concept has exactly **one** authored definition string, and every surface that defines it uses that string verbatim.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "111-113",
     "quote": "A definition that omits the load-bearing part of the concept teaches a wrong one even though every word in it is true.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "137-138",
     "quote": "Prefer a definition by **method** (what the character *does*) over one by **property** (what they *are*).",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, and 53/58 matches. 'Naming the method' fits concepts defined by an action, such as the trickster case (addendum line 164). It is generalised to the concept's defining feature.",
   "statement": "Teach a concept with an example and a non-example that differ in exactly one feature, add a maximally different positive example to block over-generalisation, and state why the non-example fails by naming the feature that defines the concept, never an incidental property.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "396",
     "quote": "| **S1** | Every vocab `non_example` states **why** it is not an example | 53 / 58 cards state no reason |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "158-159",
     "quote": "the minimally-different pair marks the boundary, but only the max-different example *kills the over-generalisation the pair invites*.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
     "lines": "81",
     "quote": "vary surface features holding the distinction constant; vary the distinction holding surface features constant; never both on one item.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "164",
     "quote": "**A3b — the non-example's stated reason must name the METHOD, never a property.**",
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
   "reason": "Quotes verbatim. Related to truth 69, but this one is about questions, not marking criteria.",
   "statement": "Write questions and modelled answers specific to each text rather than generic templates, because a generic routine can teach a false rule.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "79",
     "quote": "round-3: \"find the one sentence + check the title\" is bad advice — a fable's meaning is a synthesis, titles often don't tell the main idea",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "37",
     "quote": "5. **Questions bespoke to the text, not generic templates.**",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 122,
   "verdict": "keep",
   "reason": "Quotes verbatim. The source explicitly rejects a universal word cap, so this refines truth 26 rather than duplicating it.",
   "statement": "Test every learner-facing screen with a deletion test — remove each label, instruction, explanation, repeat and control that can go without losing learning, clarity or access — because models are poor at spotting excess text.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/meetings/incept-service-coe-2026-08-10/TEAM-UPDATES.qmd",
     "lines": "17-18",
     "quote": "LLMs have been terrible at detecting and fixing this so far",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/meetings/incept-service-coe-2026-08-10/TEAM-UPDATES.qmd",
     "lines": "21-23",
     "quote": "This is retained as a semantic deletion test, not a universal word cap",
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
   "reason": "Quotes verbatim. Adds to truth 26.",
   "statement": "Make the learner's task the visually dominant element on each screen and check it on rendered pixels, because text-pattern checks can pass a screen where supporting material overwhelms the task.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "27",
     "quote": "passage outweighing the child's task 4:1",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "87-89",
     "quote": "enforce with pixels, not seam greps: a tripwire-only validator once passed a failing screen).",
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
   "reason": "Quotes verbatim. The key-quality-gates rule was cut off at 'not' and is extended to its end (lines 154-155).",
   "statement": "Reviews of learning content should credit genuine strengths specifically, not only list defects, because an audit that concedes nothing reads as rhetoric and loses trust.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "172",
     "quote": "*Concede genuine strengths up front* — an audit that concedes nothing reads as rhetoric",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "154-155",
     "quote": "8. Credit what is good, specifically; open decisions get named owners, not verdicts.",
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
   "reason": "Quote verbatim. A single source, but it applies to any content anchored to exact text.",
   "statement": "Clear the rights to a text before writing anything anchored to its exact words, because a text withdrawn later strands every item and script tied to it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
     "lines": "110-112",
     "quote": "copyright clears **passages before span-anchored authoring begins** — scripts and cite-items couple to exact text; a passage pulled after authoring loses the lesson's artifacts.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim, and alpha .46 matches. 'Cannot show an effect either way' overstated it; the digest (line 97) says only that the null result should be read cautiously.",
   "statement": "Check a measure's reliability before reading anything into a null result, because an unreliable measure can hide a real effect, so its null says little.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/DIGEST-cervetti-wright-hwang-2016.qmd",
     "lines": "99",
     "quote": "> \"The Cronbach’s alpha was .46 which is considered far below acceptable criterion.\" — p. 770",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/DIGEST-cervetti-wright-hwang-2016.qmd",
     "lines": "97",
     "quote": "so its null result should be interpreted cautiously.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/DIGEST-cervetti-wright-hwang-2016.qmd",
     "lines": "101",
     "quote": "course assessments should pilot and report reliability before trusting question-level results.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; about 10 vs about 50 sessions matches. 'Extra strategy sessions add nothing' overstated 'no dose-response'. The against is verified at lines 172 and 175-176.",
   "statement": "Teach a general comprehension strategy briefly, explicitly and with the content it serves, then spend the time on knowledge, because across reviews about ten strategy sessions gave the same benefit as about fifty.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "134-135",
     "quote": "3. Across eight quantitative reviews, ~10 strategy-instruction sessions produce the same comprehension benefit as ~50 — no dose-response (Willingham 2014, p. 2).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd",
     "lines": "55-58",
     "quote": "\"Unless the strategies are closely linked with knowledge and understanding in a content area, students are unlikely to learn the strategies fully",
     "verbatim": true
    }
   ],
   "against": "SYNTHESIS.qmd lines 172-176: \"**Strategies genuinely work** (NRP; RAND Ch.4's ...\"; \"The claim is *bounded value*, not *no value*.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 128,
   "verdict": "keep",
   "reason": "Quotes verbatim. The meanings of the four cells (fast wrong = confident misconception, slow right = fragile) are quoted from the same Practice BrainLift line and added.",
   "statement": "Record response time alongside correctness, because fast wrong answers signal confident misconceptions and slow right answers signal fragile knowledge that accuracy alone misclassifies.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md",
     "lines": "35",
     "quote": "slow correct (fragile, shorten interval), fast incorrect (confident misconception, needs discrimination practice)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md",
     "lines": "35",
     "quote": "Platforms that rely on accuracy alone will systematically misclassify learners",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "125",
     "quote": "The four-cell diagnostic (fast/slow × correct/incorrect) drives scheduling.",
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
   "reason": "Quote verbatim. Line 548 adds that a shift in performance across representations is the clearest sign of a mis-sized unit. Mild tension with candidate 130.",
   "statement": "If learners who succeed with an idea in one representation fail it in another, the knowledge unit is mis-specified, so treat representation shifts as a test of how the knowledge was carved.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "549",
     "quote": "that is not an item quirk — it is evidence about the KC boundary.",
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
   "reason": "Quote verbatim. The clause about keeping variants inside the unit had no quote; line 81 states it and is added.",
   "statement": "Split a knowledge unit only when its success condition changes; variations in difficulty, representation or method belong inside the unit rather than becoming new units.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/curriculum-architecture.md",
     "lines": "50-51",
     "quote": "**fork a KC only when the success condition changes**.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/curriculum-architecture.md",
     "lines": "81",
     "quote": "**Absorb difficulty/representation/method variants INTO nodes**",
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
   "verdict": "keep",
   "reason": "Quotes verbatim, and g = +0.70 matches. Roediger & Karpicke (2006) appears in the BrainLift's sources. The against is verified.",
   "statement": "Use low-stakes retrieval questions as learning events, not only as measurement, because retrieval practice beats restudying.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1989",
     "quote": "The testing effect for MCQ-based practice (g = +0.70 vs. restudying) is one of the largest effect sizes in educational psychology.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/timeback-course-eval/references/eval-criteria.md",
     "lines": "38",
     "quote": "Active recall is the primary learning event, not passive consumption.",
     "verbatim": true
    }
   ],
   "against": "Assessment & Feedback BrainLift line 1991: plausible distractors without feedback can implant false knowledge.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 132,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim, inside the cited range. Reworded to drop the role word 'writers'. SKILL lines 123-125 give the grep keys.",
   "statement": "Turn comments in content that flag fragile couplings ('must match', 'silently', 'or it will') into automatic checks, because they point at failures that are otherwise invisible.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "121-123",
     "quote": "a free specification for a check nobody wrote, guarding a **silent** failure mode.",
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
   "reason": "Quote verbatim. The addendum's section C4 (lines 340-345) confirms the overruled objection.",
   "statement": "Record review objections that were overruled, with the reasoning, and re-check them in the next round, because they become calibration evidence when the issue recurs.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "115-118",
     "quote": "When we raise an objection and are directed to proceed, record it with the reasoning.",
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
   "verdict": "keep-with-fix",
   "reason": "The quote dropped blockquote markers at two line starts and is corrected to verbatim. The against is verified at lines 164-165.",
   "statement": "When review rounds converge on cosmetic findings, check the design against the target it claims to serve, because quiet rounds can mask a real gap.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/RED_TEAM_R4.md",
     "lines": "12-14",
     "quote": "The convergence to > cosmetics in R1–R3 was masking that nobody had checked the plan against the blueprint it claims to > target — R4 did, and found a gap.",
     "verbatim": true
    }
   ],
   "against": "docs/train-teacher-requirements.md lines 164-165: the stopping rule is \"two consecutive rounds with zero new findings\".",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 135,
   "verdict": "keep",
   "reason": "Quotes verbatim; 58%/42%, the 60–70% target and the lesson-level 64% match. The '193 retagged' figure in found_by is not in the G6 file, but the statement does not depend on it.",
   "statement": "Measure what items actually demand at the item level rather than from lesson-level tags, because retagging does not fix a mismatch between what a lesson teaches and what its items assess.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g6-reading/G6-DOK-FINDING.md",
     "lines": "5-7",
     "quote": "**Distribution: 58% DOK-2 / 42% DOK-3.** Target is 60–70% DOK-3. **Why the gap:** the lesson-level \"64% DOK-3\" was misleading",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g6-reading/G6-DOK-FINDING.md",
     "lines": "12",
     "quote": "**Tagging cannot fix this — it's a content-rigor gap.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "84",
     "quote": "main-idea lesson served an inference item after a \"successful\" retag",
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
   "reason": "Quote verbatim. The scoring rule was probed live. A single source, but the measurement point is general.",
   "statement": "Compute each item's chance of a correct guess from the scoring rule actually in use, not from the format label, because a pass bar within noise of chance measures nothing.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "117-120",
     "quote": "so the format label alone never determines the floor. Pair-accuracy 0.50 is a solver-metric floor only, never a serving floor. A bar within noise of its floor measures nothing.",
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
   "reason": "Quotes verbatim. Adds to truth 3.",
   "statement": "End teaching media with a prompted recall rather than a summary, and put at least one prediction or discrimination before the answer is given.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "40",
     "quote": "14. ≥1 prediction/discrimination beat BEFORE the answer; recall-based outro (a prompted recall, not a restatement)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
     "lines": "83-84",
     "quote": "| No prediction beat | answer arrives before any learner operation | 01_script (r14) |",
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
   "reason": "Quotes verbatim. Generalises truth 64 from pictures to every media element.",
   "statement": "Cut any media element that cannot name the fact it teaches or protects; decorative motion, b-roll, textured backgrounds and music are off by default, because completion is not success.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "12-13",
     "quote": "Every second must ENCODE a target fact or PROTECT the encoding of one. A second that does neither is a cut candidate. Completion ≠ success.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "29",
     "quote": "Default OFF: music under narration, decorative b-roll, textured backgrounds, non-process motion, off-topic jokes.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim, and 406/1,005 = 40% matches. The anti-guessing clause had no quote; the G5 red-team (line 15) states it and is added. Adds to truth 27.",
   "statement": "Check accessibility for every interaction type from the start, because formats chosen to resist guessing are often the least accessible, and an inaccessible format is not a faithful rehearsal of the test.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "63",
     "quote": "* Accessibility: 406/1,005 (40%) not keyboard/AT-operable",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "15",
     "quote": "the anti-leak thesis deliberately concentrates items in the TEI formats (hot-text/sequence/match = 525/772) that are precisely the accessibility-risk types.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "128",
     "quote": "An item type that cannot be made accessible is also not a faithful rehearsal of the test.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim, from the Diagnostic BrainLift's insights built on AP courses; log2(9) ≈ 3.2 checks. The source gives two placement sizes (10-15 items at line 370, 7-10 items at line 420); the statement uses neither. The against is verified.",
   "statement": "Treat 'where should this learner start?' and 'what are their gaps?' as different diagnostic problems: placement in a sequential course needs only a short binary search, while gap-finding needs sampling across the domain and a find-size-fill-verify cycle.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "370",
     "quote": "A placement diagnostic can be done in 10-15 items and 5 minutes.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "418",
     "quote": "This typically takes 3-4 items for a 9-unit course (log₂(9) ≈ 3.2).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "373",
     "quote": "**Insight 6: You don't need to find all the holes at once — find a hole, size it, fill it, repeat.**",
     "verbatim": true
    }
   ],
   "against": "Assessment & Feedback BrainLift line 414: \"If the course genuinely lacks sequential structure (e.g., a collection of independent topics with no progression), this diagnostic is inappropriate — go straight to full knowledge-mapping.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 141,
   "verdict": "keep",
   "reason": "Quote verbatim (SPOV 7). The few-prerequisites and not-every-component clauses had no quote. Line 380 (written for AP history, geography and government) and line 351 (400-600+ components per AP course) are added.",
   "statement": "Knowledge taught together tends to be known or missing together, so in domains with few prerequisites use shared teaching history (the unit taught) to target sampling instead of testing every component.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "349",
     "quote": "KCs taught in the same unit, by the same teacher, in the same week, will be correlated in their mastery status — not because the KCs are logically related, but because the *causes* of knowing or not knowing them are shared.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "380",
     "quote": "instructional clustering, which exploits shared exposure history rather than logical dependencies",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "351",
     "quote": "A well-decomposed AP course might contain 400-600+ knowledge components.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 142,
   "verdict": "keep",
   "reason": "Quotes verbatim. The Rodriguez (2005) meta-analysis of 80 years of research is at line 2082. FEEDBACK_RESPONSE line 52 records the request for at least four options. The against is verified. A genuine open question, already routed to an owner.",
   "statement": "How many options should a multiple-choice item have — the three that research favours or the four that human review asks for — given that a weak fourth distractor adds cues?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "2006",
     "quote": "The discipline: if you cannot write a third plausible distractor for a given item, use three options rather than adding filler.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "102-105",
     "quote": "The reviewer asks for at least four MCQ options, while the MCQ BrainLift reports a research consensus favoring three",
     "verbatim": true
    }
   ],
   "against": "STANDARD.qmd (v1.0.0) line 770: \"Claim boundary: No fixed option count belongs in the universal standard.\"",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 143,
   "verdict": "keep",
   "reason": "Quote verbatim; listed as held tension T2. Candidate 103 takes the fading side.",
   "statement": "Should a taught routine fade away once a stated condition is met, or keep being retrieved on a schedule?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "68-70",
     "quote": "named inference routines as *fading scaffolds* retired on a stated condition (our stance, per Willingham DOK1-3) vs. scheduled recurring retrieval of the routine (a plain reading of practice-architecture doctrine).",
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
   "reason": "Quotes verbatim. The alignment plan offers a reading under which both hold (familiar formats on new passages) but leaves it unconfirmed.",
   "statement": "Should practice match the format of the final test, or mostly not resemble it, with test-format practice saved for the end?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Direct Instruction BrainLift.md",
     "lines": "11",
     "quote": "- You should ensure test items in mastery tests match the formats experienced during instruction.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "32-34",
     "quote": "does early practice look like the test? (It mostly shouldn't",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
     "lines": "98-99",
     "quote": "compatible read: format familiarity + passage coldness. Confirm.",
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
   "verdict": "keep-with-fix",
   "reason": "Both quotes verbatim, but the depth-side source has a person's name in its path. It is replaced with the Curriculum Architecture BrainLift's review of international comparisons (line 427, Oates 2011), which that file flags as advocacy-oriented (line 432). After the fix, no evidence rests on a name-bearing path.",
   "statement": "Does transfer to unpredictable test content come from covering many knowledge areas broadly or from covering fewer ideas in depth?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "90-92",
     "quote": "so the only rational hedge is breadth: many knowledge networks + Tier-2 vocabulary + taught comprehension monitoring.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md",
     "lines": "427",
     "quote": "High-performing jurisdictions teach fewer topics per grade with greater depth. \"Fewer things in greater depth\" is the core design principle.",
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
   "reason": "Quotes verbatim; ~80/~50/~20% match. Line 353 limits self-report to setting a starting estimate that item responses then update.",
   "statement": "How far can learners' own reports of what they know be trusted for routing their study?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "352",
     "quote": "Self-report is the cheapest, fastest, and most underused signal in diagnostic assessment.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd",
     "lines": "180-181",
     "quote": "\"most child and adult readers have a poor ability to calibrate the success of their comprehension\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "142-143",
     "quote": "~80% of students check a word as \"known,\" ~50% can give an example, ~20% can explain it",
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
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
   "lines": "78",
   "quote": "Minimum: reveal the correct answer; standard: name the misconception and offer a re-attempt.",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Direct Instruction BrainLift.md",
   "lines": "60",
   "quote": "You should correct the response immediately when a student answers a question incorrectly by stating the correct answer with a brief explanation.",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
   "lines": "36",
   "quote": "- **Evidence-anchored.** Names the passage evidence in one sentence; never generic",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
   "lines": "27-29",
   "quote": "must be true for EVERY index classified into that branch (a \"what happened\" claim may not cover a speech line). Never misquote the passage inside quotation marks.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "43",
   "quote": "The durable rule is attempt first, then targeted help.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/labeled-defect-corpus.jsonl",
   "lines": "2",
   "quote": "teaching content leaking the answer to the check it precedes.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "883",
   "quote": "- Claim boundary: Vocabulary support must not pre-answer the target question.",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/07-SCORING-FEEDBACK-XP.md",
   "lines": "160-163",
   "quote": "**A single-select MCQ answer is NEVER revealed and has no ceiling on tries** (departs from the ladder rule above, which is written for OPEN responses): a wrong pick earns the R-Q-22 feedback above and the child picks again, because a short closed list cannot strand anyone and ruling options out is the thinking the item exists for.",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md",
   "lines": "136-137",
   "quote": "on a second miss, fill the slot with the correct ending and say so — never dress a filled answer as a child win",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
   "lines": "233",
   "quote": "a course-wide audit found **~half of ~700 items gameable**. InceptBench scored one gameable item **1.0**",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
   "lines": "47",
   "quote": "answerable by any knowledgeable solver with no passage.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
   "lines": "27-28",
   "quote": "exempt from passage-dependence **by design**; gated instead on spine membership (taught content only)",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd",
   "lines": "59-60",
   "quote": "One hot-text prompt can reasonably be answered by either winter or spring camouflage, while only the winter sentence is keyed.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
   "lines": "155-156",
   "quote": "\"The intended answer is stronger\" does not repair a hard-scored item when another option also answers the question.",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "205",
   "quote": "stop at key points INSIDE the text and ask right there (REL West), not only at the end",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "639",
   "quote": "- Failure signals: Analysis before encounter; hidden source; universal title shortcut; valid synthesis rejected.",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
   "lines": "53",
   "quote": "79% of MCQ correct answers sit at Choice A (expected ~25%)",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
   "lines": "151-152",
   "quote": "and does not detect within-lesson position *runs* (a student-visible streak that a course-wide histogram averages away).",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "2020",
   "quote": "Test makers systematically over-place correct answers in middle positions (B ≈ 30%, C ≈ 29% vs. A ≈ 19%, D ≈ 22% across large-scale exams).",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "93-94",
   "quote": "treat as a non-answer (re-ask once, then RED), never as a pass.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-LIBRARY-USABILITY-CLEAN-ROOM-2026-08-07.qmd",
   "lines": "64",
   "quote": "2. Written-response completion can accept a fluent but false response through length and selection counts.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "655",
   "quote": "- Failure signals: Keyword or word-count pass called comprehension; unbounded judgment; no uncertainty route; hidden target leaked to learner.",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/alpha-read/modelling-moment-procedures-v2/INDEX.qmd",
   "lines": "152-153",
   "quote": "feedback branches by family and never credits language the learner did not supply.",
   "ok": true
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/PROJECTION.qmd",
   "lines": "50-51",
   "quote": "a prompt-like unknown field also fails the closed input contract and is never treated as an instruction.",
   "ok": false
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "400",
   "quote": "- Claim boundary: Repair evidence remains distinct from first-try evidence.",
   "ok": true
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "1999",
   "quote": "A 5-item quiz is useful for retrieval practice but too unreliable for mastery decisions.",
   "ok": true
  },
  {
   "truth": 15,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "499",
   "quote": "- 1/2 → Uncertain. In a low-stakes diagnostic context, treat as a probable gap and route to remediation",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/EXTRACTION_EVIDENCE.qmd",
   "lines": "32-36",
   "quote": "230/230 extracted quotes verified verbatim at extraction time",
   "ok": true
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
   "lines": "136-137",
   "quote": "4. Only ~5–15 of 100 unfamiliar words met in natural reading are learned; misdirective contexts teach approximately zero (Beck et al. 2013, pp. 5–8).",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "39",
   "quote": "| Term before taught | technical term used before defined | 01_script sequencing |",
   "ok": true
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "249",
   "quote": "- Failure signals: Unverified exposure assumption; accidental first instruction; support arrives after it is needed.",
   "ok": true
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "35",
   "quote": "| Narrated change never shown | \"watch it divide\" over a static cell (the 10b atomic-question class) | 07_clips |",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "182-183",
   "quote": "so **insert whole new sentences; never extend an existing one.**",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "176-177",
   "quote": "Docs said fiction runs 450–500 words. Measured: informational passages were **312–333** while stories were 451–502.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
   "lines": "173",
   "quote": "the endorsed chunked variant is NOT in content/course.json (RT-11) — unreachable by children.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/teacher-contract.md",
   "lines": "69-70",
   "quote": "Do not trust the authored annotation — recompute.",
   "ok": true
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Direct Instruction BrainLift.md",
   "lines": "44",
   "quote": "- You should avoid presenting redundant text that duplicates the speech.",
   "ok": true
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
   "lines": "88",
   "quote": "- **Automated WCAG contrast checks** in render QA (round-2 found black-on-black).",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
   "lines": "120",
   "quote": "at about 20 percent accuracy by clicking through without reading, then advanced with the passage hidden from view.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
   "lines": "91",
   "quote": "item, empty-answer Next on every gate (leaks award XP — found live twice),",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-LIBRARY-USABILITY-CLEAN-ROOM-2026-08-07.qmd",
   "lines": "65",
   "quote": "3. One incorrect comprehension response unlocks `Next` while the feedback still says `Pick again`.",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/source-registry.md",
   "lines": "5",
   "quote": "gauntlet results, telemetry) · **D** = model judgment / synthesis (never load-bearing",
   "ok": false
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/gauntlet-spec.md",
   "lines": "86-88",
   "quote": "Fix: target only child-facing instructional strings, not authoring notes.",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/gauntlet-spec.md",
   "lines": "38-40",
   "quote": "Three judge agents from model families the Builder never used, adversarial framing (\"try to refute that this teaches\")",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
   "lines": "231",
   "quote": "IB quality scores are the MEDIAN of 3 runs (non-determinism precedent: 0.95/0.92/0.98 on identical content)",
   "ok": true
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "85-86",
   "quote": "a model that flips its mind can't flap the gate.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g5-reading/analysis/seq-reprobe-2026-07-07/README.md",
   "lines": "4-5",
   "quote": "A leaky ordering item can pass on a single lucky shuffle.",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "3192",
   "quote": "sensitivity to answer-choice ordering — correlates better with human difficulty than the model's actual correctness.",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/RED_TEAM_R1.md",
   "lines": "41-42",
   "quote": "87.5% agreement (42/48), 1 false-high, 0 concerning.",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
   "lines": "92-94",
   "quote": "These run as LLM-judge with a mandatory human sample per unit and become blocking only after a calibration pass against the round-2 failure examples.",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/README.md",
   "lines": "44-45",
   "quote": "Before claiming sensitivity/specificity, materialize each row as machine-readable input plus an expected assertion, version both, and run the implementation against them.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
   "lines": "281",
   "quote": "For every claimed gate, plant a representative defect and prove that the gate rejects it.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
   "lines": "47-49",
   "quote": "The Review Evidence consistency linter passes all 13 fail-closed mutation checks",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "2022",
   "quote": "A distractor selected more by high-performing students than low-performing students suggests the keyed answer is wrong or ambiguous.",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/course-quality.qmd",
   "lines": "55",
   "quote": "- generation trace including rejected attempts.",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
   "lines": "46-48",
   "quote": "→ one prerequisite retrieval prompt. Never lead with vocabulary or an unrelated hook.",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "33",
   "quote": "> **Design rule:** the we-do must **extend** the modeled skill, never replay it.",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
   "lines": "148-152",
   "quote": "5. reveal the key only after the alternatives are recorded.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "57",
   "quote": "A clean automated report is useful pre-review evidence, never a substitute for reviewer judgment.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
   "lines": "23",
   "quote": "Deterministic screens route every passage to named human review; machine checks do not approve content.",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
   "lines": "5-7",
   "quote": "primary metric, test set, baselines, ceiling, and gates are fixed now; any later change is an appended methodology-correction note, never a rewrite.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "280-281",
   "quote": "~29 gates all ran at 1400×1000, hiding a top-bar overflow on **every beat of every lesson**.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
   "lines": "255",
   "quote": "if either renders in authored order, \"always click the first option\" clears the 90% gate",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
   "lines": "84-86",
   "quote": "a stale fixture once masked a real regression and once hid an engine crash).",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/course-quality.qmd",
   "lines": "61",
   "quote": "A fully green build gate proves the course is well-built. It does not prove the course works.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
   "lines": "71-72",
   "quote": "Serving mastery forms same-session with feedback measures acquisition and calls it mastery",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "343",
   "quote": "A score of \"65% on Unit 3\" is useless for personalisation.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
   "lines": "479",
   "quote": "Preserve each historical source's identity, repository, edition or representation boundary, rights note, student material, and content digest.",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/generator-insights.md",
   "lines": "143-144",
   "quote": "**A generator optimizing for pass-rates or engagement will quietly lower rigor and destroy the very thing that works.**",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "101",
   "quote": "That is encouragement, not acceptance, certification, or proof of learning.",
   "ok": true
  },
  {
   "truth": 52,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
   "lines": "38",
   "quote": "12. Animate ONLY genuine motion/process (procedural animation can win up to d≈1.06; loses to statics when transient).",
   "ok": true
  },
  {
   "truth": 52,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
   "lines": "108",
   "quote": "Test: replace the motion with a still of the end state — does the student lose something essential?",
   "ok": true
  },
  {
   "truth": 52,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
   "lines": "102-103",
   "quote": "3. **DI video-first vs Generic Instruction \"default to text\" (§20)** — their docs disagree; ask which governs reading.",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
   "lines": "286",
   "quote": "Strong evidence is L2/vocab; benefit for fluent learners in dense instructional video is not established.",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "76",
   "quote": "| Caption duplicates text card | same words twice on screen | 09_captions suppression (r18) |",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
   "lines": "876-879",
   "quote": "It is the one button on screen that cannot be wrong, so mounted with the options it becomes the *cheap path* and children who would have answered take it.",
   "ok": true
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "1471",
   "quote": "- Your “acceptable answers” list exceeds ~15–20 variants.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
   "lines": "30-32",
   "quote": "must be verifiable from THIS lesson's passage (not another lesson's, not the hook item). Think-alouds may paraphrase but never invent sensory/setting details.",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
   "lines": "121",
   "quote": "and model memory cannot support `PASS`.",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
   "lines": "155",
   "quote": "is `NEEDS_HUMAN`; repeated support for two answers is `FAIL`.",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g6-reading/G6-DOK-FINDING.md",
   "lines": "7-8",
   "quote": "**Why the gap:** the lesson-level \"64% DOK-3\" was misleading — every lesson front-loads 3–4 DOK-2 boilerplate items",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
   "lines": "224",
   "quote": "the generator was calibrating passages at **grade 11, not grade 3**; verify the target grade before any batch",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/PROFILE-PARITY.qmd",
   "lines": "9-10",
   "quote": "it never infers a grade or capability from filenames, prose, or a reviewer request.",
   "ok": true
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
   "lines": "218",
   "quote": "systematic defect patterns (same defect class across a whole batch = generator prompt bug, not per-item fixes)",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "22",
   "quote": "191 choice items certified on a same-family lane while docs said \"every item blind-probed under a different model family\"",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "84",
   "quote": "* **Regex prefilter** cuts 5,396 strings to ~65 suspects, so the LLM judges 1% of the corpus.",
   "ok": true
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
   "lines": "223",
   "quote": "**And the leak is per-lesson, not per-item.**",
   "ok": true
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0164-g3-v2-feedback-agent-routing.qmd",
   "lines": "84-85",
   "quote": "- no KC, claim, evidence indicators, task conditions, outcome space, and scoring rule means no assessment;",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
   "lines": "53-54",
   "quote": "Isolates what training added; run it or the result is uninterpretable.",
   "ok": true
  }
 ]
}
```
