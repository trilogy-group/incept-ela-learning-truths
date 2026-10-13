# read:ti-courseplans

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "ti-courseplans",
 "coverage": {
  "read": [
   "docs/*.md: key-quality-gates, instruction-quality-standard, generator-insights, course-creation-spovs, instruction-modes-spec, practice-layer-spec, train-teacher-requirements, course-formula-agents, grade-band-profiles, teaching-reading-comprehension-brainlift, academics-alignment-plan, plain-english-explainer, chief-of-staff, PIPELINE-QUICKSTART, decision-record.schema.json (head); agent-service-plan (scan only)",
   "docs/reading-science: SYNTHESIS, PRIORITIES, README, sources, EXTRACTION_EVIDENCE, DIGEST-singh-eduqwen, DIGEST-cervetti (all claims), claim headings of DIGEST-willingham, DIGEST-hennessy x2; applied/README, applied/g3-course-graph, applied insights brainlift (diffed against docs copy)",
   "docs/handoffs-2026-07-13: README, pedagogy-llm-eval-contract, course-eval-layer/README, course-eval-layer/evaluator-spec, first 5 records of labeled-defect-corpus.jsonl",
   "docs/redteam-sources: README, g4-reading round 1, g5-reading round 1",
   "docs/standards: course-quality, source-course-refinement, course-json/README (rule sections); student-course-quality AUTHORITY, README, PROJECTION, evaluator-contracts (4), crosswalk/CONFLICT-LEDGER, profiles/README, library/README + CONSERVATION, versions/2.0.0 STANDARD + GOLDEN-CHECKLIST + PROFILE-PARITY, versions/1.0.0 STANDARD (all failure signals/claim boundaries + selected items), evidence clean-room x2, sources/knowledge-bot kb-0081, kb-0093, kb-0164, kb-0169, kb-0172 (kb-0121 = duplicate of insights brainlift), sources/meetings (INDEX, MEETING-EXCERPTS, TEAM-UPDATES), sources/alpha-read INDEX, sources/review-hub INDEX + ATOMS.json claims (incl. AP U.S. History claims RHBL-027..031)",
   "feedback/feedback1: Generic Instruction BrainLift (all), Direct Instruction BrainLift (SPOV section + overview), Practice BrainLift (SPOVs, insights, instructional hierarchy), Curriculum & Knowledge BrainLift (SPOVs/insights of Curriculum Architecture, Knowledge Clusters & Components, Knowledge Graph & Curriculum Graph, Knowledge Demand Typology), Reading_Explorers_v2_Feedback docx (textutil)",
   "feedback/feedback2: Curriculum Architecture BrainLift (diffed; SPOV6 + revised Insight 6), Knowledge Graph BrainLift (headings, same as feedback1), Reading explorers meeting transcript",
   "feedback/feedback3: FEEDBACK_RESPONSE, social-science & science coherence brainlift, Cross-Cutting Synthesis docx, headers of Biology/Chemistry/Physics misconception docx, App feedback v2 pdf, Assessment & Feedback BrainLifts (Assessment Pack, Diagnostic incl. APUSH two-tier protocol, Mastery signal, Pattern Library, MCQ, Item Difficulty, Cold-Start Difficulty Estimation)",
   "feedback/feedback 4: App Review V3 pdf, Opportunities to Respond BrainLift, interactive read-alouds transcript, youtube transcript (head)",
   "feedback/feedback 5: Feedback 11.08 docx (text), task-breakdown.html (text)",
   "brainlift/: HIGHLIGHTS, SCHEMA",
   "skills/: course-red-team SKILL + finding-taxonomy; g3-reading-red-team SKILL, IES-CORPUS-REVIEW, feedback-2026-08-06-addendum, dimensions/D7, teaching-moves strategy-text-fit + knowledge-scaffolds; timeback-course-eval eval-criteria (+ example scan); train-teacher references gauntlet-spec, teacher-contract, text-quality-lane, curriculum-architecture, scale-orchestration, source-registry; train-assessor SKILL; course-content-integrity SKILL; knowledge-ingest SKILL; edullm-quality-standard SKILL (scan); video-red-team finding-taxonomy + rubric",
   "handoff/timeback-course-explorer: references/approval-criteria (duplicate of eval-criteria), references/eval-analysis (scan)",
   "courses/g3-reading: FEEDBACK-LEDGER; iteration-1 PILOT-AND-MEASUREMENT-DESIGN; iteration-2 approval-package-v2/sources RESPONSE-MATRIX, ASSESSMENT-QUALITY-MEMO, KNOWLEDGE-COHERENCE, LOAD-BEARING-METRIC, TOPIC-SELECTION, VOCAB-AUDIT; iteration-3 CONTENT-FAILURE-CLASSES (all), BUILD-RULES (rule sections); iteration-6 distilled 00-INDEX + excerpts of 03 and 07",
   "courses/g5-reading: brainlifts/v0.6 (measured figures), analysis/seq-reprobe-2026-07-07, approval-package/D9-GATE-WALKTHROUGH",
   "courses/g2-reading/analysis: dropout-3-data-integrity, redteam-1-data-integrity",
   "courses/g4g5-writing/approval-package: RED_TEAM_R1, RED_TEAM_R4 (scan)",
   "courses/g6-reading: G6-DOK-FINDING",
   "courses/g7-science/brainlifts: video-generation-agent-v0.2, video-generation-human-v0.2",
   "courses/map-proxy-assessment: README (head), validity/05_LIMITATIONS, validity/00_AUDITS_AND_FIXES",
   "courses/hs-civics: README, reference/[name]-ap-brainlift (SPOVs/insights only; name-bearing path)"
  ],
  "skipped": [
   "brainlift/INDEX.md and COURSE_BUILD_SOURCES.md (navigation indexes; brainlift/chunks is gitignored and absent)",
   "service/ (Dockerfile, task-def, server code, rollout) and docs/agent-service-plan detail: deployment infrastructure, excluded by the task",
   "skills/timeback-*-alpha, daily-update-message, video-quality-review, course-json SKILL: platform API packs, status messaging, or tooling",
   "crosswalk CSVs, *.sql, registry/profile/manifest JSON, ledgers: data dumps (headers only)",
   "labeled-defect-corpus.jsonl beyond 5 records; handoff bundle JSONs; Science_Curriculum_Review_Workbook.xlsx: data dumps",
   "research PDFs in feedback/feedback2 (MR1465, Willingham, Cervetti, Hennessy x2, Bringing Words to Life): used the quote-verified digests instead",
   "name-bearing reference files under courses/*/reference ([name]-*, alex-*, [name]-*, [name]-*, pritish-*, crissy-*, david-b-*, peter-*, [name]-* except the AP SPOVs): preferred non-name-bearing evidence",
   "not read in full for time: g4-reading approval-package (60 docs; its findings are mirrored in docs/redteam-sources and course-formula-agents), most g5-reading analysis READMEs, g3-reading iteration 1-6 working files, unit specs, html renderings and raw lesson content, g1/g2/g4/g5/g6/g7 v0.x brainlifts, g4g5-math-checkpoints, g7g8-prealgebra, g5-reading-v2 docs/audit, map-proxy red-team round docs, g7-science analysis scripts"
  ],
  "notes": "AP material sits mainly in feedback3's Assessment & Feedback BrainLift (Diagnostic BrainLift with the APUSH two-tier protocol; AP-style items confound content with format skill; flat prerequisite structure in AP history/government), the review-hub ATOMS (AP U.S. History retrieval, repair, held-out evidence, source identity and claim-bound rules), the AP-science misconception cards (Cross-Cutting Synthesis) and the hs-civics AP BrainLift (name-bearing path, used only for one open question). Knowledge material: feedback1 Curriculum & Knowledge BrainLift (4 sub-BrainLifts), feedback2 Curriculum Architecture SPOV6, instruction-modes/practice-layer specs, the load-bearing topic metric and knowledge-coherence memo. Discrepancies found: real reject-the-alternative modelling is reported as 1 of 18 lessons (course-red-team SKILL) and 3 of 18 (finding-taxonomy); the G5 'sequence 0% leak' figure was later shown to be partly an artifact of single-shuffle checking (72 of 118 failed multi-shuffle). Several sources contradict existing truths 1 and 4 (direct-instruction protocol gives the answer immediately on a miss). Quotes that span wrapped lines are joined with single spaces. No files were written and no mgr command was run (read-only task)."
 },
 "candidates": [
  {
   "statement": "Before writing content, find and read every design source it must follow, transfer what they specify rather than regenerating it, and record every divergence with its ruling, because building correctly to the wrong specification is the costliest failure and no test of the finished artifact can catch it.",
   "kind": "adopted rule",
   "found_by": "A lesson set was authored from summary tiers while the per-lesson design documents sat unread; a later census caught renamed source folders.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "29",
     "quote": "Class 1 is the expensive one and the one artifact testing can never catch."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "50-52",
     "quote": "An undocumented divergence is a build error regardless of who requested it verbally."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "141",
     "quote": "1. Transfer, don't generate; mark no-canon layers explicitly."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Modelling, guided practice and independent practice must teach one process at falling support: showing the answer is not modelling, a hint is not guided practice, and switching to another skill is not independent practice.",
   "kind": "adopted rule",
   "found_by": "A human review found modelling that only revealed answers, guided steps that only gave hints and independent work that switched skill; a generator that 'knew' the routine still emitted answer reveals; a deterministic lint later caught all three shapes.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "24-25",
     "quote": "Generator acceptance test: strip the labels; a reviewer must still be able to say \"these three artifacts teach the same process at decreasing support.\""
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/train-teacher-requirements.md",
     "lines": "19-20",
     "quote": "a generator can \"know\" gradual release and still emit answer-reveals."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "69-71",
     "quote": "op-lint's deterministic layer catches **6 of the 10 round-2 academics failure shapes** -- including all three gradual-release exploits (answer-reveal I-do, hint-style we-do, skill-switch you-do)."
    }
   ],
   "against": "Surface format may change between stages when the operation stays the same: \"Claim boundary: Surface format may change only when the target operation remains demonstrably stable.\" (versions/1.0.0/STANDARD.qmd line 317).",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Guided practice must leave the substantive step unfinished for the learner, independent practice must apply the operation to new material rather than re-run the modelled example, and the independent step must never be more scaffolded than the guided one.",
   "kind": "measured",
   "found_by": "A clean-room review found independent work returning to the model's own example and evidence; a requested gap-fill on the independent step would have made it easier than the guided step.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd",
     "lines": "57-58",
     "quote": "You-do returns to the model's animal, evidence, and constructed answer instead of requiring the same operation on new evidence."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "245",
     "quote": "Guided work leaves the substantive learner move genuinely unfinished and increases support without completing it for the learner."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "332",
     "quote": "The gradient half: a you-do step may never be more scaffolded than the corresponding we-do step."
    }
   ],
   "against": "One lesson ships a deliberate inversion accepted on instruction after the objection was argued and overruled (same addendum, section C4).",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A worked model must show the hard decision being made on the visible source — where it looked, a tempting wrong choice and why it was rejected — and must perform each step on screen as it is narrated, not merely store a rationale.",
   "kind": "measured",
   "found_by": "Review compared the modelling to copying a neighbour's work; the reject-the-alternative move held in only one of 18 lessons; every modelling step had a stored anchor and rationale that the screen never performed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "52",
     "quote": "Visible evidence, a plausible alternative, the reason it is rejected, and construction of the answer are synchronized and semantically sound."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "77-78",
     "quote": "G3 iter-3's real \"reject-the-alternative\" modeling held in 1 of 18 lessons; the reviewed lesson (U2·L1) was that one."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "324-325",
     "quote": "every I-do step carried its span anchor and its rationale, and the screen performed none of them."
    }
   ],
   "against": "The same measure is reported as 3 of 18 lessons in skills/course-red-team/references/finding-taxonomy.md line 191 (count drift between sources).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A loop of read-then-answer items with right/wrong feedback is an assessment, not a course: every lesson needs an explicit teaching step, and assessment must never ship ahead of the instruction that prepares learners for it.",
   "kind": "measured",
   "found_by": "The first build was rejected by human review as a practice-and-assessment engine that taught nothing.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "40",
     "quote": "Reading Explorers v2 is a well-built, MAP-styled practice-and-assessment engine, not a comprehension curriculum, and on its current form it should not be approved as one."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-creation-spovs.md",
     "lines": "92",
     "quote": "A read-then-test loop with binary \"good try\" is not a course; it's an assessment engine."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "398",
     "quote": "Do not ship an assessment layer ahead of the instruction and knowledge-compounding layer that prepares learners for it."
    }
   ],
   "against": "A practice-only course may defer teaching to a separate course, but only to one that exists: \"deferring to a course that doesn't exist failed review.\" (docs/course-creation-spovs.md lines 114-115).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Sequence the texts learners study so knowledge recurs and compounds across them, and keep unrelated never-taught texts for testing transfer only.",
   "kind": "adopted rule",
   "found_by": "The first build kept every text topically unrelated throughout learning so items could not be answered from recall; review called this the deepest flaw of the design.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "70",
     "quote": "Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "166",
     "quote": "Cold plain text belongs at the *test*, not throughout learning; sequence passages so knowledge recurs and compounds"
    }
   ],
   "against": "What crosses to cold text is the operations, vocabulary and format fluency, not the topic: \"Topic knowledge is the vehicle, never the cargo.\" (docs/practice-layer-spec.md line 127-128).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Texts that repeat and elaborate the same concepts build more knowledge and more incidental vocabulary than the same amount of reading across unrelated topics.",
   "kind": "external research",
   "found_by": "Randomised study of 59 learners reading six concept-coherent vs six unrelated texts (Cervetti, Wright & Hwang 2016, DOI: 10.1007/s11145-016-9628-x).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd",
     "lines": "69-70",
     "quote": "\"For the total concept units, the main effect of treatment is significant in favor of the CC group, F(1, 56) = 26.84, p = .000, partial g2 = .324\""
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd",
     "lines": "72-75",
     "quote": "the main effect of treatment is significant, F(1, 56) = 93.16, p = .000, partial g2 = .625.\" (p. 772) — despite the CC words being *rarer* in English."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/DIGEST-cervetti-wright-hwang-2016.qmd",
     "lines": "39",
     "quote": "\"using the reading of a series of texts to build substantive understanding of a set of concepts through repetition, elaboration, and examples provided across the texts\""
    }
   ],
   "against": "\"Cervetti's limits — N=59, one rural school, on-grade readers, 3-day intervention, null (unreliable) comprehension-questions measure\" and it is unclear whether merely topical sets work (docs/reading-science/SYNTHESIS.qmd lines 186-189).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Claim that knowledge compounds only when removing an earlier lesson would break a later one; each lesson names what it adds, which earlier knowledge it reuses and what breaks without it, and links between units connect big ideas rather than shared words.",
   "kind": "adopted rule",
   "found_by": "Human review could not see knowledge being built (topic jumps, no link) and flagged cross-unit links that only matched surface facts.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "344",
     "quote": "Claim knowledge compounding only when removing an earlier anchor removes a later explanatory, comparative, interpretive, or decision resource."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "233",
     "quote": "- Failure signals: Topic list; links based only on shared words; orphan lessons; final recall of disconnected facts."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "97-98",
     "quote": "19. **Cross-unit links about the BIG IDEA, not surface facts** — not \"matching gods' names\" but the deep thematic connection, stated as a high-level understanding."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A lesson may assume only knowledge that earlier lessons taught and that the learner has retained on a later day, checked across the sequence in code, because scoring each lesson on its own cannot see the gap.",
   "kind": "adopted rule",
   "found_by": "A committed negative fixture (a lesson assuming knowledge no earlier lesson added) passed the per-lesson quality judge but failed the cross-lesson check.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
     "lines": "63-64",
     "quote": "an anchor first taught the same day never satisfies an `assumes` edge, and an anchor that is present-but-not-fluent is treated as not met."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "103-104",
     "quote": "IB scores each of those two lessons as individually fine; only the cross-lesson invariant separates them."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "42",
     "quote": "Each prerequisite is established, activated, retaught, newly introduced, or routed through a tested on-ramp."
    }
   ],
   "against": "The code check \"supplements, never replaces, human sequence review\" (docs/instruction-modes-spec.md lines 59-60).",
   "adds_to_existing": [
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Plan a group of related knowledge as a whole — one target performance, a throughline, a persistent example — before splitting it into small pieces, and keep each generation unit to one performance and one kind of knowledge.",
   "kind": "adopted rule",
   "found_by": "Piece-by-piece generation produced correct micro-lessons that never cohered; larger generation units made model output drift from its targets.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
     "lines": "16-18",
     "quote": "Atomise-first on narrative subjects produces \"locally-correct micro-lessons that never cohere\" — the round-2 sequencing finding."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "544",
     "quote": "The generic reason: as the surface area of the task grows, the precision and discipline of the LLM's output degrade — examples drift from the named target, scaffolding lands in the wrong place, and convention requirements that were live in section one silently disappear by section four."
    }
   ],
   "against": "\"For modular, abstract material (much of maths) this matters little, because the atoms genuinely are near-independent and atomise-first is close to lossless.\" (Curriculum & Knowledge BrainLift line 538).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Decide how much prerequisite structure a domain really has: tag every prerequisite link as logical, evidence-based or merely conventional, give helpful-but-not-required links a fluency threshold, and never force prerequisite chains onto knowledge that has none.",
   "kind": "adopted rule",
   "found_by": "In comprehension and in history-type domains most ordering is designed, not intrinsic; forcing chains produces fragile hierarchies, and a conventional link passed off as logical blocks learners on tradition.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "70",
     "quote": "\"A before B\" is a curriculum design choice, not a logical necessity."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "380",
     "quote": "The response cannot be to force a prerequisite structure onto content that doesn't naturally have one — that produces a fragile, artificial hierarchy that doesn't reflect how students actually learn the material."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
     "lines": "124-125",
     "quote": "classify each edge logical / empirical / conventional (kc-graph change proposal, warrant field); a conventional edge may not block the on-ramp until upgraded by evidence"
    }
   ],
   "against": "In hierarchical domains chains are real: \"In mathematics, prerequisite chains are deep and reliable\" (Assessment & Feedback Brain line 368).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "How knowledge is split into lessons can itself create misconceptions: teach the general case before a restricted one, and count a prerequisite as met only when it is fluent enough not to load working memory.",
   "kind": "adopted rule",
   "found_by": "Splitting a restricted case from the general one entrenched a wrong rule that later had to be undone; binary met/not-met prerequisites hid overload.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "36",
     "quote": "*Wrong atom boundaries create misconceptions.* Splitting a restricted case from a general case (e.g., same-denominator before unlike-denominator fractions) causes students to build predictive models that become entrenched and must be actively undone. The decomposition itself generates the misconception."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "37",
     "quote": "*Right edges with missing fluency thresholds cause cognitive overload.* A prerequisite that is technically met but not automated enough to free working memory makes the target skill unteachable."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write the curriculum sequence before writing items, and declare the sequencing policy (progression spine, entry assumptions, prerequisite strictness, priority order) before a model proposes an order, which is then reviewed against that policy rather than against taste.",
   "kind": "adopted rule",
   "found_by": "Asking a model for 'the best sequence' without a policy yields arbitrary orders that become debates about taste; item-first authoring lets available questions become the curriculum.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "308",
     "quote": "Author the curriculum graph and lesson sequence before item authoring so available questions cannot become the curriculum by accident."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "48",
     "quote": "Every output becomes a debate about taste rather than a review against a policy."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Use standards to bound what must be covered, not as the teaching plan: their order and grain say nothing about learnability, and tagging items to standards is not a curriculum.",
   "kind": "adopted rule",
   "found_by": "Skills-only standards carry no content, sequence or prerequisites; coverage of tags was being presented as the curriculum claim.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "25",
     "quote": "State standards are scope documents written for accountability and comparability, not for novice learnability."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "36-37",
     "quote": "Skills-only reading standards (\"determine the central idea\") are architecturally unusable: they carry no content, no sequence, no prerequisites"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "57-58",
     "quote": "Reading standards are skills, not knowledge — CASE-tag coverage is plumbing, never the curriculum claim."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Combine sources in authority order — standards set scope, assessments set what counts as evidence, texts and resources supply examples — never in one blended pass, and never let a text widen scope without sign-off.",
   "kind": "adopted rule",
   "found_by": "One-pass model synthesis averages conflicts, imports assumptions from low-authority sources and expands scope unnoticed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "41",
     "quote": "The model will average conflicts (producing something that matches no source well), import hidden assumptions from lower-authority sources (textbook idiosyncrasies becoming core curriculum), and expand scope without anyone noticing"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
     "lines": "108-109",
     "quote": "a text that smuggles new scope fails placement rather than silently widening the theme."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When merging similar standards or sources into one shared unit, keep each source's specific detail inside it, because a merged abstract description is too vague to drive lessons.",
   "kind": "measured",
   "found_by": "An attempt to unify similar standards across jurisdictions produced flattened abstractions that could not drive lesson design.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "1257",
     "quote": "The result was flattened abstractions that lost the specificity needed for teaching."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/curriculum-architecture.md",
     "lines": "90-91",
     "quote": "**Preserve state-specific detail INSIDE nodes — never merge into abstract common nodes**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Make later lessons need earlier knowledge so retrieval happens through use, and send to separate spaced review only the residue that nothing later recruits; drilling everything forever compensates for a poorly connected curriculum.",
   "kind": "adopted rule",
   "found_by": "Treating retention as an after-market spaced-review problem was costly and kept knowledge compartmentalised; the practice spec adopted the curriculum as the first spaced-practice system.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md",
     "lines": "55",
     "quote": "The practical rule is: use the curriculum to keep generative knowledge warm by use; use spaced practice for the residue. A platform should not compensate for a poorly connected curriculum by drilling everything forever."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "35-36",
     "quote": "it keeps warm exactly the residue the ladder cannot honestly recruit downstream, and the size of that residue is a design metric on theme"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Return to a topic only with a real upgrade — a new representation, wider scope, more abstraction, a stronger reason or harder transfer — because re-covering it at the same depth wastes time.",
   "kind": "adopted rule",
   "found_by": "Throughlines were labelled but did not deepen; weak spirals rebuilt context without getting further.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback2/WF - Curriculum Architecture Br - 260713-123107.md",
     "lines": "104",
     "quote": "The strong version is a learning progression: each revisit adds a real upgrade — a new representation, wider scope, greater abstraction, stronger warrant, or more demanding transfer. The weak version is annual re-coverage with tiny increments."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "125",
     "quote": "claimed throughlines (adaptation, power) must recur at greater depth, not just be labeled"
    }
   ],
   "against": "Sometimes a block beats a spiral: \"use blocks where coherence and immersion are essential\" (Curriculum Architecture BrainLift line 108).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose what knowledge to teach by its leverage — how often later texts assume it, what builds on it, how often target tests draw on it and how widely it transfers — not by how commonly others teach it or how interesting it seems, and let a person override the score only with written grounds.",
   "kind": "adopted rule",
   "found_by": "The most frequently taught candidate scored the lowest leverage; interest was struck as a selection ground because it tested flat; human review praised the testable score and the reasoned override.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/LOAD-BEARING-METRIC.md",
     "lines": "132",
     "quote": "Note what was **rejected** as grounds: the earlier \"student interest\" justification — interest tested flat as a learning driver, so it was struck from the record (Honesty log)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/TOPIC-SELECTION.md",
     "lines": "31-33",
     "quote": "\"what the field commonly teaches\" is a set of other people's design choices, not a discovered structure, so it carries *less* authority than powerful/portable knowledge."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/LOAD-BEARING-METRIC.md",
     "lines": "138",
     "quote": "The mirror image of Greek myth: *most* frequently taught, *lowest* leverage."
    }
   ],
   "against": "The weighting and per-factor split are declared dials, not measurements (LOAD-BEARING-METRIC.md lines 144-146).",
   "adds_to_existing": [
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Passing checks on separate parts does not show the whole performance: teach learners to coordinate the parts and put tasks that require the combined move into the mastery check, since declaring an item integrative proves nothing.",
   "kind": "measured",
   "found_by": "A mastery check of single-operation items licensed only 'passed parts'; a trial of ten declared-integrative items certified none.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "85",
     "quote": "Failure mode if ignored: \"passed parts, failed whole.\" Students look successful on micro-gates but break at any authentic task."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "273-276",
     "quote": "the full gate certified **0/10** (8 plain-blind leaks, 2 spine-conditioned leaks; 0 integrative verified), so nothing was published. This is a demonstrated open content gap and a proof that declaration alone is insufficient."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Some performances must stay whole: define them by exemplars and a rubric rather than slicing them into ever smaller skills.",
   "kind": "adopted rule",
   "found_by": "Slicing integrated performances too thin destroys the coordination the learner needs to develop.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
     "lines": "26-27",
     "quote": "4. **Decomposition floor.** Integrated performances (passage comprehension) stay whole as capstone KCs — exemplars + rubric-anchored outcome spaces, never sliced thinner."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "551",
     "quote": "In these cases, the capstone KC should be treated as an integrative construct — defined by rich exemplars and rubric-anchored outcome spaces rather than an exhaustive list of component KCs."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Treat confusable pairs as first-class knowledge: teach the contrast explicitly before building on it, record the pair in the knowledge map, and interleave the two only after both are learned.",
   "kind": "measured",
   "found_by": "A 47-component knowledge graph contained one confusable link; learners do not discover distinctions on their own.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
     "lines": "24-25",
     "quote": "Discriminations are gateway hard prerequisites and chronically under-modelled (G5 graph: 1 confusable edge / 47 KCs)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "1286",
     "quote": "Confusable pairs (students commonly mix up A and B — the graph should encode these for both initial instruction decisions, where example selection can prevent confusion from forming, and scheduling decisions, where interleaving after both are learned builds discrimination)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
     "lines": "57",
     "quote": "Students don't reliably discover discriminations alone."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose the teaching method by what the knowledge is like — a fact to recall fluently, a concept, a procedure, a distinction, a causal explanation — rather than by subject habit, since no method is good or bad in general.",
   "kind": "adopted rule",
   "found_by": "Cross-subject design principles adopted from the learning-science corpus as the defaults for generated lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "1732",
     "quote": "**SPOV1 - Subjects don’t tell us how to teach; the knowledge type does. **Profile what the knowledge is like (evaluability, decomposability, representation, fluency needs, etc.) and let that drive downstream choices, rather than defaulting to subject stereotypes."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "1735",
     "quote": "Methods aren’t universally good or bad; they’re conditionally apt given the KC’s evaluability, decomposability, and representation profile."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Practise stable facts with brief, frequent, tapering retrieval and quick firming of errors, and practise schema-dependent knowledge by retrieval, feedback and then a task that uses it under new conditions.",
   "kind": "adopted rule",
   "found_by": "A single practice pattern either over-reteaches or under-practises; the practice spec adopted two practice routes by knowledge type.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md",
     "lines": "19",
     "quote": "Practice is frequent and brief early on, then tapered, with occasional maintenance checks. Errors are met with targeted firming, not full reteaching."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md",
     "lines": "20",
     "quote": "The sequence is: retrieval → feedback → update task (explanation, comparison, discrimination, boundary case, application in a new context)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Practise a new skill in a block while it is being acquired and mix it with other skills only after it survives a retest on a later day with new items, because same-day success measures working memory.",
   "kind": "adopted rule",
   "found_by": "Mastery forms served same-session with feedback were being counted as durable mastery.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "37-40",
     "quote": "Blocked practice while a skill is in acquisition. **Interleaving eligibility = E2-cleared**: a delayed (≥24h) retest passed on *new* parallel items — release-day completion never qualifies (Practice BrainLift: same-day testing measures working memory, not learning)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "433",
     "quote": "- Claim boundary: Interleaving is introduced only after prerequisite acquisition is secure."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Practice and retrieval must not require or grade knowledge the course has not taught: if correcting a practice item needs more explanation than the lesson gave, the item is new teaching, not practice.",
   "kind": "adopted rule",
   "found_by": "An independent-practice step required untaught knowledge and became a permanent regression probe.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md",
     "lines": "38",
     "quote": "The design heuristic: if the feedback needed to correct the response is longer and more complex than the original instruction, the item has crossed the boundary."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "452",
     "quote": "Retrieval may activate prior knowledge, but it must not grade content the course has not taught or established as a prerequisite."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "82",
     "quote": "| You-do requires untaught knowledge | round 1 F3 |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Never grade a response form the lesson has not modelled exactly; if learners are marked on a format the modelling omits, the lesson is grading something it never showed.",
   "kind": "measured",
   "found_by": "A static audit found 60 places where learners were graded on quoted-evidence form that the modelling did not show.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "404-406",
     "quote": "the lesson grades the child on producing `The text says \"…\"` while the modelling omits the quote marks, so we grade a form we do not demonstrate."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/alpha-read/modelling-moment-procedures-v2/INDEX.qmd",
     "lines": "147-149",
     "quote": "It labels and executes the real procedure steps; it does not introduce an untaught response routine. A point-evidence-explanation paragraph is parked until an explicit writing lesson teaches it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A percentage pass mark means something only while task mix, difficulty and support stay fixed, so set each bar by how costly it is to advance a learner too early rather than by one global figure.",
   "kind": "adopted rule",
   "found_by": "Assessment BrainLift analysis of mastery decisions; adopted into the reviewer-routed assessment obligations.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "766-767",
     "quote": "Percent-correct only means something when task difficulty and evidence conditions are held steady; otherwise it is entangled with item easiness, scaffolding, and cueing. If we change the task mix, we change what “90%” means, which makes the system look consistent while the standard drifts."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "789",
     "quote": "So a single global “90%” (or global posterior cut) is structurally incoherent: high-dependency atoms merit conservative thresholds (higher than 90%); low-dependency atoms can advance on lighter evidence with follow-up checks."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "88",
     "quote": "- define mastery through controlled evidence and downstream risk, not a global raw `90%`;"
    }
   ],
   "against": "The platform's non-negotiable fixes a global bar: \"Enforce mastery gates at ≥90% accuracy.\" (skills/timeback-course-eval/references/eval-criteria.md line 24).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Recompute what a percentage gate demands at the real item count whenever items are removed, because on a test of nine or fewer items a 90% gate requires a perfect score.",
   "kind": "measured",
   "found_by": "Purging leaky items shrank tests to 5–9 items and silently turned a 90% gate into a perfect-score gate.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "14",
     "quote": "leak-purge shrank tests to 5–9 items → 90% gate = perfect-score-only (ceil(0.9n)=n for n≤9)"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "63-64",
     "quote": "ceil(0.9×n) = n for n ≤ 9: a 90% gate on a ≤9-item test demands a perfect score. Check every gating test's size."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A mastery gate needs three outcomes — advance, keep practising, or switch to re-teaching — and must change the item families when practice continues, otherwise persistence becomes the hidden pass criterion.",
   "kind": "adopted rule",
   "found_by": "Mastery-signal analysis identified 'grind-through' (passing by repeated sampling of similar items) as the key failure mode.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "771",
     "quote": "A mastery system that lacks an explicit “switch mode” state will inevitably turn persistence into the hidden criterion for passing."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "796-798",
     "quote": "If learners can eventually pass by repeatedly sampling similar items, the gate is measuring persistence (or luck) rather than acquisition mastery. To prevent grind-through, mastery evidence must include breadth (multiple item families / near-miss contrasts) and recovery verification after any corrective branch. In other words: if the system stretches, it must also change the evidence slice, not merely add more of the same."
    }
   ],
   "against": "An earlier evaluation read retry-until-100% as stronger than a 90% gate: \"the student re-attempts until 100%, which is *stricter* than a 90% gate\" (handoff/timeback-course-explorer/references/eval-analysis.md line 96).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "After an error, correct it, re-test on a new parallel item, re-check later, cap the retries and escalate to re-teaching or re-placement after repeated failure rather than looping.",
   "kind": "adopted rule",
   "found_by": "An incumbent course had only one form per test, so a retry could only re-serve the same items; long feedback plus lockout dead-ended learners.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "56",
     "quote": "The trace shows correction, an alternate explanation or representation, a parallel new attempt, a delayed recheck where claimed, retry bounds, and escalation after non-progress."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
     "lines": "36",
     "quote": "A second consecutive failed delayed retest routes to placement/sequence review — never an infinite loop."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/handoff/timeback-course-explorer/references/eval-analysis.md",
     "lines": "103",
     "quote": "**No parallel forms** — only one form per lesson test, so \"retry on a parallel same-difficulty passage\" (Insight 4) isn't possible yet."
    }
   ],
   "against": "The direct-instruction protocol re-asks the same item immediately after correcting it: \"On a miss: **Correct** (answer + brief why) → **Test** (re-ask immediately) →\" (docs/instruction-quality-standard.md line 114).",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep first independent attempts separate from supported or repaired ones: base mastery on unaided checks, let supported steps feed feedback, and never count a retry after help as a first success.",
   "kind": "adopted rule",
   "found_by": "Failure signal in the student-course standard; modelled handoffs were being read as independent evidence.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "399-400",
     "quote": "- Failure signals: Immediate answer reveal; identical retry; endless loop; supported retry counted as first independent success. - Claim boundary: Repair evidence remains distinct from first-try evidence."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1380",
     "quote": "Score where inference is clean. Use supported steps mainly for feedback; base high-stakes decisions on the first unaided check (or transfer task) that follows."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/alpha-read/modelling-moment-procedures-v2/INDEX.qmd",
     "lines": "161",
     "quote": "A modelling handoff is supported practice, not independent mastery evidence."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    14
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Plausible wrong options can implant false knowledge, so every misconception-based distractor needs feedback that corrects it.",
   "kind": "external research",
   "found_by": "Negative suggestion effect: feedback largely neutralises the risk (Butler, A. C., & Roediger, H. L., III. (2008). Memory & Cognition, 36(3), 604–616; no DOI given in the source).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1991",
     "quote": "Butler & Roediger (2008) showed that feedback largely neutralises this risk, while the absence of feedback leaves it unchecked."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "95-96",
     "quote": "- potent misconception-based distractors require product-appropriate corrective feedback or post-test correction because plausible lures can seed false knowledge;"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "166",
     "quote": "strong misconception distractors + no feedback = teaching the error (negative suggestion effect)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Write each wrong option as the answer a specific misconception would give and name that misconception in its feedback; an option nobody would choose for a reason is filler that only adds cues.",
   "kind": "measured",
   "found_by": "An audit found only about 7% of choice items named the misconception a distractor targeted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "129-130",
     "quote": "Distractors are misconception-coded (each = the answer a named misconception picks); feedback names the misconception."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md",
     "lines": "44",
     "quote": "The one honest edge: distractors are currently **plausible and text-grounded**, but only **~7% of choice items (15 of 48 lessons)** name the *specific misconception* a distractor targets in its feedback"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "160",
     "quote": "can you name what a student choosing each distractor is thinking? if not, it's filler (worse than 3 options)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a lesson targets a known misconception, voice the tempting wrong belief once at the start and then resolve it, because a clear explanation alone can leave the misconception intact.",
   "kind": "external research",
   "found_by": "Refutation openings beat concise correct exposition on immediate conceptual gains (Muller 2008: refutation ≈ d 0.79, dialogue ≈ d 0.83; reference [20], no DOI given).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
     "lines": "116-118",
     "quote": "concise correct exposition on immediate conceptual gains (Muller 2008: refutation ≈ d 0.79, dialogue ≈ d 0.83) [20]. Scope: immediate, undergraduate, misconception-central"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "238-240",
     "quote": "the instructional open must SURFACE the intuitive wrong belief once then RESOLVE it — a lesson that teaches the correct model cleanly but never engages the prior belief is a 🟡 finding (confident non-learning: clear-only exposition barely moves scores)."
    }
   ],
   "against": "Misconceptions caused by poor instruction should not be foregrounded: \"*From poor instruction*: don't foreground — fix the explanation so it isn't produced.\" (Generic Instruction BrainLift line 61); the evidence is immediate, undergraduate and not shown for delayed retention.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Treat an item as higher-order only if it presents material the learner has not seen; a longer stem over familiar content is still recall, and difficulty is a separate dimension from cognitive level.",
   "kind": "adopted rule",
   "found_by": "Item tagging conflated hard recall with higher-order thinking; 'inference' items were recall with longer stems.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1995",
     "quote": "The novel stimulus requirement is the single most reliable test of whether an item is genuinely higher-order: no new material, no higher-order thinking."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "2010",
     "quote": "A hard recall item is still recall. An easy application item is still application. These are independent dimensions, and conflating them is the most common tagging error in item banks."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "An item's difficulty must come from the target knowledge; hardness from wording, negatives, obscure context or a clumsy response interaction is invalid, so match the input gesture to the shape of the answer.",
   "kind": "measured",
   "found_by": "An ordering item built from number dropdowns taxed exactly the working memory it was meant to measure.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "2366",
     "quote": "Any item whose difficulty cannot be explained in KC/KDT terms (steps, conversions, cue structure, etc.) is almost certainly measuring a messy mix of construct and noise."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "760-761",
     "quote": "**The interaction taxed exactly the working memory the item exists to measure comprehension with.**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "766",
     "quote": "* **Match the gesture to the shape of the answer.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write options so test-wiseness cannot win: keep the key the same length, form and punctuation as the distractors, avoid absolute or ungrammatical distractors, make the stem answerable with the options covered, and never use all/none of the above.",
   "kind": "measured",
   "found_by": "A rubric gate passed six items a blind probe solved from length and absolute-language tells; an odd-one-out key survived shuffling; the only dashed option was the key.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "225",
     "quote": "the rubric gate passed 6/6 such items (g4 F1)"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "214-216",
     "quote": "The key is the only option of its grammatical kind — a bare proper noun among three \"The …\" / \"He …\" options. Position shuffling does not remove this; a seeded shuffle already removed position information from these items and the cue survived intact."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "2002",
     "quote": "read the stem, cover the options, and ask whether a knowledgeable student could formulate an answer"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check items against each other and against everything the learner meets first: no title, narration, earlier item or modelled answer may give away a later item's key, and consecutive questions must not re-ask what was just asked or modelled.",
   "kind": "measured",
   "found_by": "A check was answerable from the lesson title alone; a guided question asked for an answer the model had just stated; a cross-item word leak was found.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "224-226",
     "quote": "a token which uniquely identifies one item's key must not appear in another item's stem, options, or feedback anywhere in the same lesson, nor in a Scout line the child hears before reaching it. The lesson title counts as a surface"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "33",
     "quote": "> **Design rule:** the we-do must **extend** the modeled skill, never replay it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3,
    41,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Declare each item's class before judging its overlap with teaching: a knowledge check may test what was taught, but a comprehension or transfer item must not test facts the lesson's own teaching used, and this disjointness is checked at generation time.",
   "kind": "measured",
   "found_by": "The same overlap made one text both correct and defective until items were classed; it took five rounds to isolate, and a fresh unit reproduced the leak.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "84-86",
     "quote": "the same overlap in a comprehension/transfer item is a leak. Mis-classifying the item makes the same text both correct and defective — it took five adversarial rounds to isolate this."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/teacher-contract.md",
     "lines": "59-60",
     "quote": "Authoring a fresh unit (u03 respiratory) REPRODUCED the dose-item leak the hibernation unit took 5 rounds to eliminate: the you-do modeled the same inference an item tested."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "88",
     "quote": "list every FACT the dose (I-do/we-do/you-do) uses vs every FACT the MOVE items test — must be DISJOINT (knowledge-CFU items exempt)"
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
   "statement": "Run the without-text check with the learner's earlier lessons available, under several option orders judged by the worst case, with a model unlike the generator, and with a with-text control, because a single plain run passes items that leak.",
   "kind": "measured",
   "found_by": "A prior-lessons-available probe caught 1 of 16 items plain checking missed; a multi-shuffle re-probe of 118 'certified' ordering items decertified 65 and flagged 7 as broken.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "106-109",
     "quote": "the solver receives all prior lesson content (on-ramp pre-teach, ledger state, prior passages) but not the new text; later items must fail. The Rivers calibration caught **1 of 16** items that plain-blind certification missed"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g5-reading/analysis/seq-reprobe-2026-07-07/README.md",
     "lines": "4-5",
     "quote": "The sequence anti-leak gate scored **one** seeded shuffle per item. A leaky ordering item can pass on a single lucky shuffle."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g5-reading/analysis/seq-reprobe-2026-07-07/README.md",
     "lines": "31-33",
     "quote": "- Actually sequence & re-probed: **118** - **Decertified (leak + answerable): 65** - Broken-flagged (leak + NOT answerable, left certified, flagged): **7**"
    }
   ],
   "against": "\"This validates the need for the instrument on that bounded sample, not a general yield or course-readiness claim.\" (docs/practice-layer-spec.md lines 109-110).",
   "adds_to_existing": [
    5,
    35
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A without-text verdict belongs to the model that produced it, so re-run it with current models, because a newer model can turn an item that passed into a direct leak.",
   "kind": "measured",
   "found_by": "An item an older solver could not answer without the text was solved 3/3 by a current model.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/README.md",
     "lines": "92",
     "quote": "The old context-lift claim does not survive model drift; the item is directly gameable."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "138-140",
     "quote": "the same item is currently a direct plain-blind leak and the historical context-lift interpretation does not generalize across model versions."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Build items to need the text from the start rather than filtering generated clones: in one bank, single- and multi-select items were answerable without the text almost every time, while items constructed for text dependence survived certification ten times as often.",
   "kind": "measured",
   "found_by": "Cross-family blind runs on the same texts by item format, and survival rates of construction-first versus clone generation.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g5-reading/brainlifts/v0.6.qmd",
     "lines": "24-26",
     "quote": "different blind-solve leak rates by question *format*: MCQ 99.5%, MSQ 100% — hot-text 1.67%, sequence 0%, match 0%, EBSR 0% (cross-family run, 2026-06-23/24). The passage is not the only lever. > **MCQ/MSQ format does not force reading; hot-text, sequence and match do.**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "21-23",
     "quote": "construction-first generation survived the anti-leak gate at 60% vs 6% for encyclopedic clones; one production campaign yielded 48.7% (738 certified of 1,516); raw generated banks leaked ~94% blind."
    }
   ],
   "against": "The 0% ordering-format figure was partly an artifact of single-shuffle checking (courses/g5-reading/analysis/seq-reprobe-2026-07-07/README.md lines 4-6).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Remove or replace items known to be answerable without the text instead of only excluding them from gates, because a leaky item still awards progress for not reading.",
   "kind": "measured",
   "found_by": "A submission left 231 of 772 items classified as known-leaky in front of learners.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "233",
     "quote": "G5 shipped with **231/772 (30%) classified known_leaky still live**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "17",
     "quote": "The ledger honestly classifies 231/772 items (29.9%) as known_leaky — excluded from gate instruments, but not removed from the live course."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After certification removes items, recheck format and coverage, because exclusions can silently drop a whole item format from what learners practise.",
   "kind": "measured",
   "found_by": "Every two-part evidence item failed certification, so a six-format course quietly became five-format.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g5-reading-redteam-round1-2026-07-06.md",
     "lines": "27",
     "quote": "All 20 EBSR items sit in the excluded bucket."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In a two-part item the second part must neither restate nor depend on the first, because dependent parts leak the answer and tell you nothing when the first part fails.",
   "kind": "measured",
   "found_by": "Six of six sampled two-part items were solvable without the text because part B restated part A.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "156-157",
     "quote": "6 of 6 sampled two-part evidence items were blind-solvable, with Part B restating Part A — the same root cause measured at 33% gameable in G3"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "402",
     "quote": "Multi-part items where you need to get part (a) right to attempt part (b). If the student fails, you learn about part (a) but nothing about part (b). For diagnostics, split these into independent items."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Items that bundle content knowledge, question-format skill and reasoning cannot show what is missing: a diagnostic isolates one piece of knowledge with the simplest format, and is judged by whether the learners it routes learn faster.",
   "kind": "adopted rule",
   "found_by": "Diagnostic BrainLift (worked on an AP history course): exam-style items mis-diagnose learners who know content but not the format, and vice versa.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "310",
     "quote": "Using test items (such as AP-style exam questions) that confound core knowledge with experience in answering that type of question. A student who knows the content but hasn't practised the question format will look like they don't know the content."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "307",
     "quote": "A diagnostic is good if students who follow its recommendations learn more efficiently than students who don't."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "308",
     "quote": "The key trade-off that governs the entire design is: *time spent testing is time not spent studying*."
    }
   ],
   "against": "For broad comprehension no valid diagnostic exists: \"You wouldn't be able to do a diagnostic comprehension test. We studied this, it doesn't exist.\" (feedback/feedback2/Reading explorers Transcript (1).txt line 125).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Report knowledge per component with its uncertainty and keep 'not tested' separate from 'not known', since one right answer is not proof of knowledge and one wrong answer is not proof of ignorance.",
   "kind": "adopted rule",
   "found_by": "Diagnostic BrainLift; adopted as the course's mastery framing.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "343",
     "quote": "An unassessed KC is not the same as a failed KC, and conflating the two is one of the most common errors in diagnostic systems."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "339",
     "quote": "But the minimum requirement is that your system understands that a single correct answer is not proof of knowledge and a single incorrect answer is not proof of ignorance."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9,
    15,
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "With few learners per course, set item parameters from expert defaults and course structure rather than statistics, label every estimate with how it was made and how much data it rests on, and replace it with live data as responses accrue.",
   "kind": "adopted rule",
   "found_by": "About ten learners per course make calibration that needs 100–200 responses per item impossible for years; an assessment bank of 650 items had no empirical difficulty data.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "382",
     "quote": "Estimating a single item's difficulty and discrimination parameters with reasonable precision requires at minimum 100-200 student responses to that item."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "385",
     "quote": "At Alpha's scale, a simple rule-based approach — select by prerequisite structure, sample across clusters, use sentinel items for boundary detection — will outperform a statistically \"optimal\" approach running on uncalibrated data."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "3180",
     "quote": "Every pre-use difficulty value must travel with a provenance label (\"pre-use predicted, N=0\") and an uncertainty indicator"
    }
   ],
   "against": "Expert-assigned values leave real difficulty unknown: \"This means we do not know how hard any individual item actually is for students.\" (courses/map-proxy-assessment/validity/05_LIMITATIONS.md line 11).",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A model cannot simulate what learners don't know, because its knowledge leaks through role-play, so simulated learners and model-rated difficulty overstate success and must be labelled as predictions, not results.",
   "kind": "external research",
   "found_by": "Curse-of-knowledge findings in LLM difficulty work (Li et al. 2025, arXiv:2512.18880); internal: learner role-play capped near 67% accuracy.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "3174",
     "quote": "They cannot simulate what students don't know, even when explicitly prompted to adopt a student persona. This is not a prompt-engineering problem"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/generator-insights.md",
     "lines": "123-124",
     "quote": "LLM student role-play is structurally flawed and caps ~67% accuracy; teacher-as-predictor reaches r≈0.72–0.79 population-level"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/train-teacher-requirements.md",
     "lines": "184-185",
     "quote": "simulated students are a prediction, not a result — sim results are labeled as such everywhere"
    }
   ],
   "against": "Predicting as an experienced teacher works better (r≈0.72–0.79) and aligned simulated students are 'promising but not yet production-ready' (Assessment & Feedback Brain, Cold-Start Insight 10).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Estimate item difficulty from extracted features or by placing new items against calibrated anchor items rather than from a model's direct rating, and distrust any estimate that swings under small rewording.",
   "kind": "external research",
   "found_by": "Direct model ratings correlated only r≈0.4–0.6 with empirical difficulty versus up to r≈0.87 for feature models (Razavi & Powers 2025; paraphrase consistency: Sarkar et al. 2025; no DOI given).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "3172",
     "quote": "Direct LLM ratings show moderate correlations with empirical difficulty at best (often r ≈ 0.4–0.6), exhibit systematic overconfidence, and cluster narrowly around the middle of the scale."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "3184",
     "quote": "Typical r ≈ 0.7–0.87 with empirical difficulty."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "3196",
     "quote": "if small wording changes cause wild swings in your predicted difficulty, the prediction is probably wrong."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A model's score on teaching-knowledge questions is not evidence that the content it generates teaches well; measure the generated material itself.",
   "kind": "external research",
   "found_by": "The authors of a pedagogy-benchmark model state this limit themselves (Singh et al. 2026, Frontiers in AI, https://doi.org/10.3389/frai.2026.1851993); the project's training experiment made such benchmarks explicit non-metrics.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/DIGEST-singh-eduqwen-2026.qmd",
     "lines": "34",
     "quote": "\"strong benchmark performance on pedagogical knowledge questions does not itself constitute evidence of effective classroom tutoring; actual educational impact depends on teacher judgment, learner epistemic beliefs\""
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "80-81",
     "quote": "the gap must be measured at the artifact level rather than inferred from benchmark scores."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Fix the metric, test set, baselines (including the untrained model on the same inputs), chance floors and pass/abort gates before generating or training, append rather than rewrite any later change, and require two independent runs before claiming a bar is met.",
   "kind": "adopted rule",
   "found_by": "Pre-registered contract written before a model-training experiment so its results could not be reinterpreted afterwards.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "5-7",
     "quote": "primary metric, test set, baselines, ceiling, and gates are fixed now; any later change is an appended methodology-correction note, never a rewrite."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "53-54",
     "quote": "- **Arm B (base): the untrained base model + the SAME prompts and briefs.** Isolates what training added; run it or the result is uninterpretable."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "75-76",
     "quote": "- **Replication:** any bar-hit claim needs 2 independent generation runs; a single run is a single-point estimate."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "The step that generates content must never certify it: certification, mastery judgments and semantic review belong to a separate lane using a different model family, and every claim of independence must match the build record.",
   "kind": "measured",
   "found_by": "A deploying lane certified its own items until banned; 191 items were certified by the same model family while documents claimed cross-family checking.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "21-22",
     "quote": "| **Self-certification** | G5: deploying lane certified its own items until the protocol banned it | ask who ran the gate vs who authored the items | | **Same-family \"cross-family\" claims** | G5 R4: 191 choice items certified on a same-family lane while docs said \"every item blind-probed under a different model family\""
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/train-teacher-requirements.md",
     "lines": "269-270",
     "quote": "must remain independent lanes — different agents, different judge families, neither certifies the other's output."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
     "lines": "263",
     "quote": "Do not certify your own authored content. The author may fix findings; an independent reviewer must"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "State every claim at the level its evidence reaches — written, machine-checked, verified in the running product, accepted by people, verified in production, or shown to improve outcomes — and never upgrade it by confidence or repetition.",
   "kind": "adopted rule",
   "found_by": "Machine passes were presented as approval and previews as production; 'green' drifted into 'ready for learners' in prose.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "26",
     "quote": "Authored, mechanically validated, runtime verified, human accepted, production verified, and outcome validated remain distinct states."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "104",
     "quote": "- Claim boundary: A weaker evidence type cannot be upgraded by confidence or repetition."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
     "lines": "98-99",
     "quote": "- **Verdict inflation** — \"GREEN\" drifting into \"ready for kids\" in prose; GREEN is only \"no defect found on the checked dimensions\"."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44,
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A check that could not run, lacked its inputs or returned an undiscriminating answer is reported as not evaluable or unverified, never as a pass.",
   "kind": "adopted rule",
   "found_by": "Judges returning identical statuses and unavailable source tools were at risk of being read as clean.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/PROJECTION.qmd",
     "lines": "10",
     "quote": "Use `NOT_EVALUABLE` as a stop signal, never as a pass."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
     "lines": "93-94",
     "quote": "- **Flat score row** — the judge returns identical/undiscriminating statuses; treat as a non-answer (re-ask once, then RED), never as a pass."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "38-39",
     "quote": "gog-unavailable is a loud UNVERIFIED failure, never a pass."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before reporting that something is absent, prove the check could have seen it: look everywhere it could live and confirm the selection the check ran on was not empty.",
   "kind": "measured",
   "found_by": "An analyzer that scanned one field reported zero standards on 745 items that all carried them; a mistyped selection judged 6% of the corpus and printed ALL PASS.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/handoff/timeback-course-explorer/references/eval-analysis.md",
     "lines": "117",
     "quote": "(the morning analyzer missed them because it only scanned `rawXml`; standards are in structured metadata, not inline XML)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "208",
     "quote": "| empty selection | `UNIT=2` instead of `U2` matched no lessons — judged 6% of the corpus, printed ALL PASS |"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/edullm-quality-standard/SKILL.md",
     "lines": "16-17",
     "quote": "Never treat an unreturned rule as absent: search is a bounded relevance lookup, not a completeness oracle."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A new check must report how often it fires and show that it catches the example that motivated it, because a check that fires on everything cannot rank and one that misses its own seed is not measuring it.",
   "kind": "measured",
   "found_by": "Two new cue checks missed their motivating example; a first cut fired 13/213 with 11 false; a near-synonym check was cut for failing its seed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "95-99",
     "quote": "A check firing on everything cannot rank items; a check missing its own seed is not measuring what prompted it. Both occurred in one round: correct-is-longest and stem-overlap missed the seed entirely (the real cue was grammatical odd-one-out, 2/151), the first cut of that check fired 13/213 with 11 false"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "203-204",
     "quote": "Break the thing deliberately; confirm the gate fails. **Five gates asserted nothing** and every one was found this way, never by re-running:"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask what a check would still pass on: checks can assert something true about the wrong thing, so read checks in review and assert the intended contract rather than whatever string happened to be present.",
   "kind": "measured",
   "found_by": "Three green assertions measured the wrong element; a check pinned the canned congratulation that praised wrong answers, so fixing the product turned it red.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "219-220",
     "quote": "A different question from \"does it red when broken\" — and it catches a different class: **a gate that asserts something true about the wrong subject.**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "259-261",
     "quote": "the canned congratulation that **congratulated wrong answers**. Fixing the player made a green gate fail. Assert the *contract* (\"the head derives from the score\"), not the string that happened to be there."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A rule written only in prose is not enforced: turn every human catch into an automatic check in the same cycle, and before closing a review round check each adopted rule against the content by name.",
   "kind": "measured",
   "found_by": "A round re-reported nine rules adopted five days earlier; 22 of 30 human findings were criteria already written into the standard that the build never ran.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "87-90",
     "quote": "The G3 2026-08-11 round re-reported NINE rules adopted five days earlier — and the rule that was supposed to prevent that (08-06 C3, \"a prior ruling that survives in the content is our miss\") had itself been written after the same thing happened on 08-04. Three consecutive rounds, one unenforced rule. Prose in an addendum gets read, not run."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "1044-1046",
     "quote": "Twenty-two of them were already criteria in the red-team standard (`skills/g3-reading-red-team/references/dimensions/`), which is the more useful fact: the standard was not missing them, this build shipped without running them."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "144",
     "quote": "3. The ratchet: every human catch becomes a machine check the same cycle —"
    }
   ],
   "against": "Defects visible only in the running application cannot be content checks: \"putting it in a content gate manufactures a check that can never be green or red.\" (skills/course-red-team/SKILL.md lines 108-109).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A finding is closed only when the check that found it passes on the current delivered version: treat reported fixes as claims, re-verify every earlier fix and sweep for new problems the fixes introduced.",
   "kind": "measured",
   "found_by": "Most items in an 11-item 'done and live' fix report failed live review, including the original exploit; one item was falsely closed by citing a commit.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "136-137",
     "quote": "Closure = re-run the finder on the current build; \"fixed in <commit>\" is not closure (one item was falsely closed this way)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "101-102",
     "quote": "Round 2: most of an 11-item fix report failed live review, including the original kill exploit."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "172",
     "quote": "*Recheck mode after a fix wave* — re-verify every prior fix line-by-line (closed/half/open) and sweep for issues the fix wave introduced"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never judge a course by its best-looking lesson or a sample: recompute each quality claim across all lessons, report the share that holds, and name what any sample or gate did not cover.",
   "kind": "measured",
   "found_by": "The reviewed lesson was the only one with genuine modelling; a completion gate covered quizzes but not 40 project lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "29",
     "quote": "Unreviewed content cannot inherit the result of a strong sample."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "249",
     "quote": "the completion-gate covered quiz/onboarding lessons but **not the 40 PowerPath expeditions**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "76-77",
     "quote": "8. **Showcase ≠ corpus.** Never grade the one lesson the reviewer already saw — it is the polished one."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check across lessons, not only one at a time: an answer key must agree with what earlier lessons taught, and 'already seen' must mean seen on every path a learner can take, not on some path.",
   "kind": "measured",
   "found_by": "A warm-up marked a learner wrong for answering as the previous lesson taught; switching the 'already seen' test from union to intersection over branches exposed six more defects.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "141-144",
     "quote": "A child who learned L5 **correctly** was marked wrong. **Gate:** `crosslesson_check`. Invisible to five other gates because **every other gate reads one"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "152",
     "quote": "> **\"Already seen\" must be an INTERSECTION over branch points, never a union.**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "163",
     "quote": "The intersection changed the finding from *\"39 of 46 clean\"* to **6 more real defects**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Every reference to earlier learning ('last lesson', 'remember last time') must be true for the actual teaching order; when generation cannot know the neighbouring lesson, use a safely vague phrase.",
   "kind": "adopted rule",
   "found_by": "A 'remember last time' prompt appeared on the very first story.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
     "lines": "47",
     "quote": "Under batched or parallel generation the author may not know the true teaching-order neighbour, so a confidently-named one can simply be wrong; an unverifiable relational claim is a defect, not a flourish."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "64",
     "quote": "small bugs jar (\"remember last time\" on the first story; \"inspiration tap\")."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When content is generated and then copied or edited, apply every fix both to the generator and to the stored content, and fix a faulty upstream specification at its source before regenerating, because a patch on rendered content is undone by the next regeneration.",
   "kind": "measured",
   "found_by": "Generator output was hand-copied into lessons with nothing linking the two; a regeneration clobbered post-hoc fixes.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "392-394",
     "quote": "A rule fixed in the generator prompt does not reach any lesson already on disk, and a fix applied on disk does not survive the next regen (that is the `g3-regen-clobbers-posthoc-fixes` failure, and it has happened). So every adopted rule needs BOTH homes,"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
     "lines": "45-46",
     "quote": "A rendered lesson that silently fixes a bad specification does not close the upstream defect because regeneration can reintroduce it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "List every item type and content path a check must cover and assert the list is not empty, because a balancing pass on graded items left the teaching items' answers clustered at one position.",
   "kind": "measured",
   "found_by": "Teaching-step multiple-choice items bypassed the key-balancing pass: vocabulary checks were 98% key A (53 of 54); a semantic checker once collected only multiple-choice nodes while breaches sat in narrated text.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "119-120",
     "quote": "Dose teach MCQs bypassed the QTI debias pass, so rebalancing the graded bank never touched them: hook 69% A, we-do 53% A, **vocab 98% A** (53 of 54)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "127-128",
     "quote": "**Enumerate every item type that carries a key**, then assert the enumeration > is non-empty."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "74-75",
     "quote": "Known scope trap: it once collected only MCQ nodes while breaches lived in narrated text nodes"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    8,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Score every model answer against its own rubric, and anchor each pass line with a borderline example rather than only a top-score model.",
   "kind": "measured",
   "found_by": "A written-response rubric required a word its own model answer did not use; exemplars existed only at the top score.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "132-133",
     "quote": "U2-L6's SCR required the term \"sacrifice\"; its own model answer said \"gave up\". The exemplar the teacher reads aloud would have been marked down by the rule printed underneath it."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md",
     "lines": "83",
     "quote": "each SCR declares the cut *and* carries a **borderline** exemplar at that cut — not only a top-score model — so \"meets\" is anchored where the decision is actually hard."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    10,
    45
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Feedback attached to a branch must be true for every answer routed to it and must use what the learner actually said; a reply that would read the same whatever the answer is not feedback, and a hint must add something the learner has not already written.",
   "kind": "measured",
   "found_by": "Canned replies ignored learners' answers; a hint restated the learner's own correct answer as advice.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "26-28",
     "quote": "4. **Branch feedback true for every index** (branch_check): every partly/off `turn3` / `retap_wrong_hint` claim about \"the line you tapped\" must be true for EVERY index classified into that branch"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback 4/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "71",
     "quote": "A reply that would read the same no matter what the child answered is not a third turn."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "184",
     "quote": "the reply reads the same no matter what the child said (`recast_template`, `recast_close` are static strings)"
    }
   ],
   "against": "Restating the learner's idea does not reliably teach a specific point: \"because children often do not notice a recast, it does not reliably teach one specific point\" (OTR BrainLift line 70).",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test that every adaptive branch can actually fire — especially the one for a learner who freezes — and offer an 'I'm not sure' route only after a delay, because shown up front it becomes the easy way out.",
   "kind": "measured",
   "found_by": "A no-response branch was authored in 18 of 18 lessons but could never fire, so stuck learners were forced to guess.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "187",
     "quote": "iter-3 `silent`/\"I don't know\" branch authored + gated in 18/18 but **can never fire**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "876-878",
     "quote": "* **An escape hatch offered up front stops being an escape hatch.** The door is revealed after ~20s (`CFU_UNSURE_MS`), below the tappables, deliberately. It is the one button on screen that cannot be wrong, so mounted with the options it becomes the *cheap path*"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "97",
     "quote": "Every branch is reachable in tests; correct, partial, misconception, off-topic, silence, error, and missing-data routes receive semantically appropriate next moves."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep corrective feedback short (about 40 words, never over 60), mechanically clean and at the learner's reading level, because feedback longer or more complex than the original teaching has become new teaching.",
   "kind": "measured",
   "found_by": "Human review found feedback longer than the text it referred to; the generator's median was about 91 words.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "31-32",
     "quote": "Target ≤ 40 words; hard cap 60. A grade-3 child will not read feedback longer than the passage (round-2 verified: our generator's median was ~91 words)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "94-95",
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
   "statement": "Whenever a prompt or feedback asks the learner to look back at the source, keep the source visible, and place each question beside the text it asks about.",
   "kind": "adopted rule",
   "found_by": "Prompts said 'look back at the text' with the text hidden; checks below the text forced scrolling and split attention.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "38-40",
     "quote": "Whenever feedback or a prompt asks the student to cite or look back at the text, the text must be visible. \"Try looking back at the text\" with the passage hidden is a defect class, not a UX nit."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "140",
     "quote": "15. Put the check **next to** the text, not below (below = split attention, scrolling up to find the answer)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Interrupt passive content with a meaningful, non-bypassable response at least every minute or so, because anything skippable without consequence gets skipped.",
   "kind": "measured",
   "found_by": "A learner could finish a whole course by clicking through without engaging; a read gate was bypassed by clicking Next twice.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
     "lines": "37",
     "quote": "\"Pause and think\" is not an active check: anything skippable without consequence is skipped."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/meetings/incept-service-coe-2026-08-10/MEETING-EXCERPTS.qmd",
     "lines": "27-28",
     "quote": "> A user could complete the entire course simply by clicking through the green buttons without > engaging with the material."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
     "lines": "35",
     "quote": "No continuous passive segment beyond ~60s."
    }
   ],
   "against": "Not every screen needs a click: \"required learner work must be meaningful and non-bypassable, while reading, listening, transition, and accessibility steps use task-appropriate completion evidence rather than decorative clicks.\" (MEETING-EXCERPTS.qmd lines 31-33).",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't let learners skip or speed up instruction, because they judge poorly what they can skip, but let them advance modelled steps themselves on a tap rather than on a timer.",
   "kind": "adopted rule",
   "found_by": "Learners rushed when given speed control; timed reveals could not pace themselves to slow readers.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "58",
     "quote": "- No child control over pace or skipping (children are poor judges of what they can skip)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "310-311",
     "quote": "A timer also cannot pace itself to a slow reader. Tap-to-continue satisfies both."
    }
   ],
   "against": "Direct instruction allows earned skipping: \"**Require students to earn Test Out through repeated mastery on prior lessons**\" (Direct Instruction BrainLift line 19).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Comprehension work must make learners produce — say, write, explain — and counts of productive responses must discount trivial echoes, because a high response rate reached through recognition is not quality.",
   "kind": "measured",
   "found_by": "A self-audit claimed 7–8 productive responses per lesson; 2–3 were one-word say-backs and real productive work was about 2.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback 4/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "23",
     "quote": "A high number of responses per minute is not evidence of quality if the app reached that number by asking only recognition questions."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "183",
     "quote": "G3 iter-3 claimed \"7–8 generate/lesson, over-delivered\" — but 2–3 were trivial *say-backs* (repeat a word) and the real generative-comprehension production was ~2"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback 4/WF - Brainlift Opportunities to - 260724-110911.md",
     "lines": "30",
     "quote": "If a child never has to compose or explain an answer, the app cannot tell whether the child understood"
    }
   ],
   "against": "For fast routing diagnostics, selected response is preferred: \"For diagnostic assessment, the much-maligned MCQ is not a compromise — it is the optimal format.\" (Assessment & Feedback Brain line 354).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Have learners locate evidence in the text first and then explain it in their own words; a task that asks them to copy a sentence and paraphrase it in the same box teaches copying.",
   "kind": "adopted rule",
   "found_by": "Human review flagged the evidence task as backwards in two consecutive rounds.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "215",
     "quote": "- **The writing task teaches plagiarism**: find-and-copy-the-sentence then own-words in one box. Highlight/underline in the text first, then write in own words; or split into two parts."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "54-55",
     "quote": "9. **\"Say it with evidence\" is backwards.** Reverse to **find-and-highlight the sentence FIRST, then write it in your own words**;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Set a purpose before the learner meets the source, let them encounter the whole source before close modelling, and open each section by linking to what was just learned.",
   "kind": "adopted rule",
   "found_by": "Lessons modelled before learners had read the text and set no purpose; sections opened 'cold' after the previous one.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "25-26",
     "quote": "2. **Read the text BEFORE modeling.** The child reads (or hears) the whole text first; you can't dive deep into part of a text you haven't engaged with."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "317",
     "quote": "Complete a first encounter with the whole text before close modelling or analysis."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "302-303",
     "quote": "the defect it catches is a section that is individually well-written and contextually cold"
    }
   ],
   "against": "Stopping to ask inside the text during reading is also recommended: \"stop at key points INSIDE the text and ask right there (REL West), not only at the end\" (finding-taxonomy.md line 205).",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep background-knowledge building short — about ten minutes — so most of the lesson is spent in the main text, optionally preceded by an easier text on the same topic.",
   "kind": "external research",
   "found_by": "IES teaching-video corpus (YouTube IDs _9KCwZCvrUo and H2qrN8Hh37o), citations phrase-verified against transcripts.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/knowledge-scaffolds-bridge-canopy-cap.md",
     "lines": "23",
     "quote": "\"At the same time, activating or building background knowledge should take 10 minutes or so.\""
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/knowledge-scaffolds-bridge-canopy-cap.md",
     "lines": "25",
     "quote": "\"I once saw a class where a teacher spent 35 minutes activating and building background knowledge, and then 10 minutes where the kids actually read.\""
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/knowledge-scaffolds-bridge-canopy-cap.md",
     "lines": "19",
     "quote": "\"asking students to read an easier brief passage before presenting the higher-level text on the same topic\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Choose each practice text so the taught move is actually needed on it, and rate surface difficulty and conceptual difficulty separately, because a familiar or predictable text lets learners succeed without the process.",
   "kind": "external research",
   "found_by": "IES/WWC practice-guide videos (YouTube IDs ooEq08Gs1IU, V4atucROaSQ), phrase-verified.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/strategy-text-fit.md",
     "lines": "7",
     "quote": "Pick the passage *after* you pick the target strategy, and pick it so the strategy is the only way through."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/teaching-moves/strategy-text-fit.md",
     "lines": "13",
     "quote": "\"and by level of difficulty we're not just talking about the word reading demands of the text that is how hard the words are for a student to read but also the comprehension demands of the text how hard is it to understand this text these two things are not always aligned\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Text difficulty depends on what the reader already knows: highly cohesive text helps low-knowledge readers but can lower deep understanding for high-knowledge readers, and harder texts become accessible as knowledge builds.",
   "kind": "external research",
   "found_by": "RAND Reading Study Group MR-1465 (https://www.rand.org/pubs/monograph_reports/MR1465.html), App. A pp. 107-108; adopted as 'difficulty is a match, not a number'.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd",
     "lines": "106-111",
     "quote": "for low-knowledge readers, \"For these readers, texts with high coherence consistently produced higher performance scores than texts with low coherence.\" For HIGH-knowledge readers the reverse appears on deep measures: \"A coherent text base slightly enhanced recall, but actually lowered performance on tests that tapped the mental model.\""
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "114-115",
     "quote": "7. Text difficulty is a match among text factors, reader knowledge, and task — no single readability number can gate a text (RAND; the within-unit flex principle)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Treat generated texts and items as untrusted until a person has read at least a sample: code screens for syntax, vocabulary and cohesion reject and queue, never approve, because generated texts tend to run too hard and cohere poorly.",
   "kind": "measured",
   "found_by": "Human review called generated texts almost always too hard; a screen flagged cohesion 0.17 on an incumbent text versus 0.58 on a clean one; submissions put 772 and 957 unreviewed items before educators.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/text-quality-lane.md",
     "lines": "5-6",
     "quote": "All text is `humanApproved:false` until the specialist signs off — the machine stage never approves, it only rejects and orders the queue."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/text-quality-lane.md",
     "lines": "34-37",
     "quote": "the screen independently flagged **cohesion density 0.17 with a 3-sentence static run** — the machine-detectable half of exactly the defect humans named. On a clean target-quality sample: cohesion 0.58, passes. The screen discriminates; it does not approve."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "263",
     "quote": "even a sampled ~60-item review converts \"0 human-reviewed\" into \"sampled + attested\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Text that carries another subject's content must pass that subject's misconception check — banned phrasings plus a meaning-level probe, because a misconception can be implied without the phrase — and every simplified model or diagram is framed as a simplification.",
   "kind": "adopted rule",
   "found_by": "Subject leads made the check mandatory because folk-science wording in reading texts undoes correct teaching elsewhere.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md",
     "lines": "24",
     "quote": "Good science instruction is undone by encounters with folk science that is intuitively appealing but scientifically incorrect."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "145",
     "quote": "| **Meaning-embedded misconception (no exact phrase)** | \"the plant grows by taking food from the soil\" implies plants-eat-soil without the literal phrase |"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "147",
     "quote": "| **Model without health-warning** | a food chain / atom / cell diagram presented as literal reality |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Simplify only in ways that stay accurate and will not block later learning, because early everyday wording can plant misconceptions that later courses must undo.",
   "kind": "adopted rule",
   "found_by": "Cross-subject misconception review traced errors re-taught in later courses to early loose wording.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
     "lines": "802",
     "quote": "- Claim boundary: Simplification is acceptable only when it remains accurate and does not create a later-blocking misconception."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "136-137",
     "quote": "it actively undoes correct science instruction (the ATP case: even students who learned it right get re-taught the error)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a course meets knowledge taught elsewhere, reinforce that framing rather than redefine it, prefer re-encounters from a fresh angle to first exposure, and keep fact, interpretation and opinion distinct with claims bounded by who, where, when and which source.",
   "kind": "adopted rule",
   "found_by": "Cross-app guidance for reading/writing courses that carry science and social-studies content; history-course rules on claim bounds.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md",
     "lines": "11",
     "quote": "The aim is for the re-encounter to feel like a new angle, not a repeat."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/Brainlift social science and science coherence.md",
     "lines": "14",
     "quote": "Where a topic has already been covered, the Read/Write lesson should be consistent with how it was framed in the subject app — vocabulary, level of nuance, framing."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "488",
     "quote": "Bound historical claims by actor, region, period, institution, and source function rather than flattening them into generic narratives."
    }
   ],
   "against": "A push for more fiction sits in tension with a knowledge-heavy spine: \"Log as a question, not a silent rebalance.\" (feedback/feedback3/FEEDBACK_RESPONSE.md line 128).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "If learners choose their own path or order, the course cannot assume which knowledge they have met, so sequencing and retrieval must rest on what every path guarantees.",
   "kind": "adopted rule",
   "found_by": "Human review flagged learner-chosen characters and flow as the biggest threat to retrieval and sequencing.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "65",
     "quote": "because the child picks their character and flow isn't fixed, you can't be sure which knowledge/folktales they've met — undermines retrieval and sequencing."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Declare whether each check is teaching practice, a gating assessment or a transfer benchmark, judge each by its own criteria, and put mastery thresholds only on gates.",
   "kind": "measured",
   "found_by": "All five lesson resources, including the teaching lessons, carried a 90% threshold and behaved as practice-test gates.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
     "lines": "229-231",
     "quote": "masteryThreshold=90 on all 5 lesson resources** -- the three teaching lessons and the transfer lesson behaved as 90% practice-test gates over their own formative checks."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "90-92",
     "quote": "the declaration lets the evaluator judge teaching checks by teaching criteria and interval forms by assessment criteria instead of judging one by the other's bar."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep a sealed transfer test whose topics never appear in teaching material, generation prompts or training data; it is never a gate and never taught from.",
   "kind": "adopted rule",
   "found_by": "Design of the practice layer and the training experiment; held-out sources kept separate in an AP history course.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "71",
     "quote": "The cold benchmark is **never a mastery gate and never teaching material**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
     "lines": "71-72",
     "quote": "A model trained on a cold topic cannot be evaluated on it."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "470",
     "quote": "Keep held-out assessment sources separate from lesson-visible teaching and practice sources."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Preview and review access must never create learning evidence: free navigation, answer reveals and resets leave mastery, rewards and progress unchanged.",
   "kind": "adopted rule",
   "found_by": "Unlocked review builds were required, which risked minting mastery outside real learner use.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "34",
     "quote": "Free navigation, answer reveal, reset, and reviewer-only controls leave mastery, reward, completion, and unlock records unchanged."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "152-153",
     "quote": "a reviewer mode that unlocks lessons **without minting mastery evidence** — stamps earned under compressed calendars are marked non-evidence."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A gate learners can bypass is a teaching failure, not only a security gap: it moves them past knowledge they lack and poisons the outcome data used to improve the content.",
   "kind": "adopted rule",
   "found_by": "A mastery stamp was earned at about 20% accuracy by clicking through; data from a gameable course cannot improve generators.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "58-61",
     "quote": "A gate a child can bypass doesn't just corrupt the data; it places the child outside their zone of proximal development *by construction* — advanced past knowledge they don't hold, or held below knowledge they do."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/timeback-course-eval/references/eval-criteria.md",
     "lines": "134-136",
     "quote": "a gate that doesn't require reading produces a *poisoned feedback signal* — kid-outcome data from a gameable course can't improve the generators."
    }
   ],
   "against": "\"Claim boundary: Anti-gaming controls must not block legitimate accessibility paths.\" (versions/1.0.0/STANDARD.qmd line 535).",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat gaming and misunderstanding differently: rapid guessing and hint abuse get an integrity response, while flat learning gain, not merely low accuracy, triggers re-teaching.",
   "kind": "adopted rule",
   "found_by": "Assessment-quality design for the course's adaptive policy.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md",
     "lines": "72",
     "quote": "The load-bearing signal is **flat gain, not low accuracy** — a child who is genuinely learning but not yet at cut is *keep practising*, not *corrective*. And **gaming ≠ misunderstanding** (#32): rapid-guessing and help-abuse get an integrity response, not reteaching."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When the system fills in an answer after repeated misses, say so, and never present it as the learner's success.",
   "kind": "adopted rule",
   "found_by": "Dated product ruling enforced by a contract validator after write-ups dressed filled answers as wins.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md",
     "lines": "135-137",
     "quote": "On a first miss, echo the child's words with a try-again; on a second miss, fill the slot with the correct ending and say so — never dress a filled answer as a child win"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every number in course documents carries a source, comes from one dated record that readers can recompute, and is never borrowed from another course or copied from a summary without recomputing it.",
   "kind": "measured",
   "found_by": "The same course quoted 52/745/56 in one document and 47/713 in another; certified counts drifted 541/549/559; a figure of '~150 responses' copied from an agent summary was invented (actual 48).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "262",
     "quote": "G3's email said 52/745/56 while the infographic said 47/713 (finding #11); G5 certified-count drifted **541 vs 549 vs 559** across docs"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/RED_TEAM_R1.md",
     "lines": "43-44",
     "quote": "a number that reads authoritative and is wrong, inherited from a research-agent summary I did not independently recompute before writing it down."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "29-30",
     "quote": "2. **Never invent a magnitude.** Do not carry another grade's/cohort's numbers as if they were this one's."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Summaries must match the reports beneath them: never round a value across its threshold, never drop the failing metric, and label each result by what it actually measures.",
   "kind": "measured",
   "found_by": "Audits of an assessment's approval case found 0.928 shown as '0.930 ✅' against a 0.93 bar, the one failing metric omitted from every summary, and a synthetic consistency check presented as agreement with the real test.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "9",
     "quote": "| 1 | Summary tables reported reliability as \"0.930 ✅\" against a ≥0.93 benchmark the underlying reports state as 0.928, below |"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "10",
     "quote": "| 2 | The one failing metric (RMSE 4.12 vs <4.0 target) was omitted from every summary table |"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "34",
     "quote": "| 9 | \"Sim 4\" reads as MAP agreement evidence | **Relabeled** — now \"internal cross-bank consistency (synthetic),\" explicitly not MAP agreement"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Compute outcome rates over the learners actually enrolled, from one consistent source, and compare the same learners over time, because the wrong denominator or mixed populations manufacture failures and declines.",
   "kind": "measured",
   "found_by": "A whole-network denominator turned a 0.707 completion average into 0.007; a cross-grade 'decline' came from which schools entered the sample; growth claims were tied to instrumenting actual dose.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g2-reading/analysis/dropout-3-data-integrity.md",
     "lines": "12",
     "quote": "**The headline \"low completion\" numbers are ~90% MEASUREMENT ARTIFACT, not abandonment.**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g2-reading/analysis/dropout-3-data-integrity.md",
     "lines": "29",
     "quote": "Alpha Reading Fluency G2 — the course that looked catastrophic at `avg_pct = 0.007` — actually shows the **highest** average completion of the bunch (0.707) once the dead universe rows are removed."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g2-reading/analysis/redteam-1-data-integrity.md",
     "lines": "14",
     "quote": "2. **The \"G1→G3 slide (77→50→45)\" is a Simpson's-paradox / season-composition artifact, not a within-student decline (FATAL to the causal framing).**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Published research can justify a design but does not show that a particular course works; until outcome data from its own learners exists, claim only direction and a validation plan.",
   "kind": "adopted rule",
   "found_by": "A retired baseline from a biased slice (206.4/72nd percentile) was shipped where the full-population figure was 196.0/46th; design evidence was being cited as outcome evidence.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/PRIORITIES.qmd",
     "lines": "81-83",
     "quote": "this corpus grounds DESIGN, it does not prove OUR implementation works. Never cite it as evidence about our courses' outcomes."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/course-quality.qmd",
     "lines": "81",
     "quote": "Synthetic prediction, IB scores, or reviewer approval are not outcome evidence."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "262",
     "quote": "the real figure was **196.0 / 46th pctile (n=915)**. No RIT/growth number pre-pilot; direction, not magnitude"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48,
    51
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Bars, yields and magnitudes measured in one course, grade or cohort do not carry to another without recalibration; mark unknown values as to-be-sourced rather than borrowing them.",
   "kind": "adopted rule",
   "found_by": "Planning for a new grade was reusing another grade's measured gates and yields.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "139-140",
     "quote": "Historical G5 volume does not validate a G3 estimate."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/grade-band-profiles.md",
     "lines": "17-18",
     "quote": "Every cell cites its source; empty cells are `[TO SOURCE]` — **never invent them**."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A course for a different level must differ on the dimensions that change with level — text demand, stamina, formats, and the knowledge and operations to master — not just in topics or harder texts.",
   "kind": "adopted rule",
   "found_by": "Courses for adjacent grades built under the same guidance converged, so one rejection risked rejecting all.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/grade-band-profiles.md",
     "lines": "8-10",
     "quote": "> A course for grade N must be **demonstrably different** from its siblings on the > dimensions below, with grade-specific sources — not a re-skinned port of the > nearest sibling."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
     "lines": "416",
     "quote": "Differentiate adjacent grades by the knowledge and operation learners must master rather than cloning a sibling course with harder text."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose item formats to match what the knowledge requires and what the target test and the learner's level demand: cover the test's formats, drop formats too advanced for the level, and require production where the target is production.",
   "kind": "measured",
   "found_by": "An incumbent course was 100% single-select against a test using six formats; a two-part format above the grade level was added and flagged.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/generator-insights.md",
     "lines": "102",
     "quote": "The incumbent's #1 measured failure was 100% single-select MCQ vs MAP's 6 formats."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "122",
     "quote": "- N3: recognition-vs-production match. \"Write/explain/draw\" targets cannot be assessed by MCQ alone."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "77-78",
     "quote": "- Item formats must match the grade's state-blueprint reality: **EBSR / two-part evidence items are ~grade-4+**; do not ship them at G3."
    }
   ],
   "against": "The same reviewers first praised two-part items and then called them developmentally inappropriate (iteration-6/distilled/07-SCORING-FEEDBACK-XP.md lines 229-230); for routing diagnostics single-select is preferred (Assessment & Feedback Brain line 354).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Plan text length and genre mix toward the target test's reading load from the start rather than backfilling, because practice on short single texts never builds stamina for long multi-text reading.",
   "kind": "measured",
   "found_by": "Practice texts ran 58–217 words against a test presenting about 2,740 words; literary share was about 22% against a 40% target because texts were picked on readability alone.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "224",
     "quote": "G3 passages were 58–217w when the test reality is multi-passage (~2,740w); ramp length toward test stamina"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "166",
     "quote": "G3 was flagged at **~22% literary vs ~40% target** because texts were picked on Lexile alone"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Prefer assembling, transforming and tagging vetted material over inventing items from scratch, and treat generator output as a candidate until a separate check certifies it.",
   "kind": "external research",
   "found_by": "A study of 9 generative quiz builders found 80% of items violated at least one guideline and 74% had major flaws, while model tagging reached 87–95% accuracy (cited via the organisation's knowledge tree; no DOI given).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/generator-insights.md",
     "lines": "56-57",
     "quote": "But of 9 Gen-AI quiz builders studied, **80% of items violated ≥1 best-practice guideline and 74% had major flaws — only 1 in 5 usable**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/generator-insights.md",
     "lines": "90",
     "quote": "**Treat generator output as *candidate* until a separate check passes.**"
    }
   ],
   "against": "Construction-first generation under certification gates can work: it survived at 60% vs 6% for clones (docs/practice-layer-spec.md lines 21-22).",
   "adds_to_existing": [
    57,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Where possible make a rule impossible to break by construction — for example, never give a generator or scorer the text before the learner has read it — instead of relying on a check to catch the breach.",
   "kind": "measured",
   "found_by": "A pre-reading reply quoted the plot to a learner who had not opened the story; the fix sent pre-reading moments an empty text so they could not quote it.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "45-47",
     "quote": "pre-passage moments send the scorer an **empty passage and empty vocab list**, so it *cannot* quote what the child hasn't read. A rule you can't violate beats a rule you must remember."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Narration must match the on-screen text word for word, checked by exact whole-line identity rather than substring matching, because text edits silently leave stale or missing audio.",
   "kind": "measured",
   "found_by": "After one round of text edits, 117 of 179 narrated strings had no matching audio; a prefix-tolerant check missed an extended line whose new sentences had no audio.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "1085-1086",
     "quote": "found 117 of 179 narrated strings already orphaned by the round's own rewrite, with 686 clips on disk the generator will now skip."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "1099-1100",
     "quote": "**a drift check that tolerates prefixes silently exempts every string that was EXTENDED, and extension is the most common shape of a feedback edit.**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "115",
     "quote": "- Audio: printed==spoken; frozen TTS voice/style prompts; holds land ON mark"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17,
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In narrated media let the audio set the timing: nothing is revealed before it is spoken, one new label appears at a time, music stays off under teaching speech, and the voice is never stretched to fit the visuals.",
   "kind": "adopted rule",
   "found_by": "Video QC history: reveals ahead of audio, label dumps and time-stretched narration were recurring render defects.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "30",
     "quote": "4. Say-while-showing. Audio is the MASTER CLOCK. Schedule every visual event off forced-alignment word timestamps. A reveal MUST NOT complete before its term is spoken."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "31",
     "quote": "5. NEVER time-stretch the voice to fit visuals. Re-cut visuals instead."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "46",
     "quote": "20. Music/SFX OFF under teaching narration; any intro/outro bed ≥20 dB below speech; an SFX must have an instructional job."
    }
   ],
   "against": "Pacing bands are heuristics from adult data: \"Child WPM band is unestablished. 120–145 wpm is an [OH] from adult anchors.\" (video-generation-human-v0.2.md line 285).",
   "adds_to_existing": [
    21,
    23
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't speed up narration or playback to save time: playing instruction at 1.4–1.5× costs about g = −0.21 and at 1.8–2× about g = −0.36.",
   "kind": "external research",
   "found_by": "Meta-analytic evidence cited as reference [21] in the video BrainLift (no DOI given); learner speed control was also removed because learners rushed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
     "lines": "195",
     "quote": "Artificially speeding playback costs learning (1.4–1.5× ≈ g−0.21; 1.8–2× ≈ g−0.36) [21]."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
     "lines": "33",
     "quote": "1. **No user-controlled audio playback speed** — kids rush; enforce a consistent age-appropriate rate."
    }
   ],
   "against": "\"Elementary learners are under-studied. The corpus skews adult/higher-ed\" (video-generation-human-v0.2.md line 284).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Fade scaffolds across a unit as learners gain expertise, and record each scaffold's retirement condition as data with counts that only fall, because a fade promised in prose never happens.",
   "kind": "measured",
   "found_by": "Expertise-reversal evidence (pre-training g ≈ 0.28–0.78 for novices can harm experts); a 'state a fade condition' criterion stayed open two review rounds because a sentence satisfied it.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
     "lines": "138-140",
     "quote": "Pre-training part-names before explaining interactions helps novices (g ≈ 0.28–0.78); worked examples help novices (g=0.48) [14]. But the same scaffolding can harm relative experts (expertise reversal) [12]."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "233",
     "quote": "Prose in an authoring note does not satisfy D1.13, and a"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "248",
     "quote": "- **Counts are monotonically non-increasing across the unit.**"
    }
   ],
   "against": "Whether taught routines should fade or be retrieved on a schedule is an open dispute (docs/teaching-reading-comprehension-brainlift.md lines 68-70).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Tag every design rule with the kind of evidence behind it and never cite an operating heuristic as a proven threshold; discount effect sizes reported by a principle's originators, and let the course's own delayed-outcome data override cited effects.",
   "kind": "adopted rule",
   "found_by": "Rules mixed learning evidence, accessibility standards, platform limits and guesses; inflated originator effect sizes were being quoted as thresholds.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "19",
     "quote": "- `[OH]` operating heuristic (current guess; has owner + validation experiment; NEVER cite as a proven learning threshold)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
     "lines": "293",
     "quote": "- **Effect sizes inflate when a principle's originator is an author;** we cite conservative independent numbers and treat any single effect as a direction."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
     "lines": "306",
     "quote": "when our own delayed-recall data contradicts a cited effect, our data wins and"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When sources or rulings conflict, record the conflict as a named open question with an owner and enforce neither side until it is decided; never average it or settle it silently.",
   "kind": "adopted rule",
   "found_by": "Source documents gave steps in conflicting orders; human rulings contradicted each other on answer reveal and on item formats.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/train-teacher-requirements.md",
     "lines": "253-254",
     "quote": "the conflict is logged as a named tension and reserved for a working session — never silently resolved in either direction"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/crosswalk/CONFLICT-LEDGER.qmd",
     "lines": "20",
     "quote": "DECODE Step 2 and Step 3 appear in conflicting orders; do not enforce an ordered DECODE sequence until the curriculum owner resolves it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep every source statement as retained, with its scope and provenance; indexing or summarising a source never makes it an accepted universal rule, and compressed summaries never replace the source as the authority.",
   "kind": "adopted rule",
   "found_by": "Design of the quality-knowledge library after rules from many sources were being merged and generalised.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/AUTHORITY.qmd",
     "lines": "10",
     "quote": "Source atoms are never silently deleted, merged, universalized, or promoted."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/AUTHORITY.qmd",
     "lines": "22-23",
     "quote": "In particular, `UNIVERSAL` and `FINAL` require an attributable decision; ingestion never supplies either by default. Conflicts remain open and source-faithful until an evidence-bound decision resolves them."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/README.qmd",
     "lines": "29-30",
     "quote": "not receive `PRIORITY` retrieval metadata or become accepted requirements merely because they were indexed."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Copy source text into a knowledge store by file rather than having a model retype it, verify every quoted span and citation against the source in code, and check that each extraction reaches the document's end, since verified quotes do not prove the extraction is complete.",
   "kind": "measured",
   "found_by": "Subagents re-emitting copyrighted text failed; 230/230 and 271/271 quotes and 49/49 citations were verified mechanically with zero fabrications surviving.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/knowledge-ingest/SKILL.md",
     "lines": "71",
     "quote": "never re-type source text through a model."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/EXTRACTION_EVIDENCE.qmd",
     "lines": "34-35",
     "quote": "The four EduQwen checks establish presence in the scoped extraction only, not full-paper coverage."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/IES-CORPUS-REVIEW-2026-08-05.md",
     "lines": "24-25",
     "quote": "So **no citation here rests on the reviewer model's say-so.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat a finding that recurs across independent sources as a rule and one seen once as a candidate, and never count two checks that agree by the same method as corroboration.",
   "kind": "measured",
   "found_by": "Two agents reached the same conclusion with the same blind instrument, which was not independent; two genuinely different instruments found the same faulty item.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/IES-CORPUS-REVIEW-2026-08-05.md",
     "lines": "17-18",
     "quote": "- Findings that recurred across *independent* batches were treated as high-confidence; a technique seen once was treated as a candidate, not a rule."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
     "lines": "1115-1116",
     "quote": "**Two agents independently agreeing via the same blind method is not corroboration; it is one unverified claim counted twice.**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "208-209",
     "quote": "Two independent instruments landing on one item is the strongest signal in the document, and it is the argument for running both."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    35
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before filing a defect in learning content, check whether it was requested, capture the whole page over time before claiming nothing happened, wait out designed timers, separate environment faults from content faults, and publish how many findings were retracted.",
   "kind": "measured",
   "found_by": "A first uncalibrated sweep had 4 of 6 blockers retracted; a team was once told to revert to a design that had been explicitly rejected.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "134-136",
     "quote": "Publish the correction rate when findings are disputed (ours: 4 of 6 blockers retracted on the first uncalibrated sweep — the number that made the second sweep trustworthy)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "129",
     "quote": "3. **Wait out the designed timer** (compute it) before calling a gate broken."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "172",
     "quote": "*A finding that rests on a checkable factual error damages the audit more than the package*"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write each finding as one falsifiable problem with exact evidence, why it matters, the exact location, a specific change and the rechecks needed, and report counts as raw, exempted and real with the exemption rule stated.",
   "kind": "measured",
   "found_by": "A sweep read 392 raw hits of which 104 were exempt; publishing the raw number would have discredited the finding.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/course-json/README.md",
     "lines": "115-116",
     "quote": "A failure additionally needs one falsifiable problem, exact evidence, why it matters, an exact target object/path, a specific proposed change, a repair-owner skill, and named rechecks."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "103-104",
     "quote": "sweep read 392 raw; 104 were play-script speaker labels and a skill name; the real number was 284."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Review one frozen version per round and bind every piece of evidence to the exact content it checked, so any relevant change withdraws that evidence and forces the affected checks to rerun.",
   "kind": "measured",
   "found_by": "Changes landing mid-round invalidated in-progress review rounds three times; a stale package matched 0 of 55 current lesson digests.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "148-149",
     "quote": "5. One pinned build per round — including our own internal work; mid-flight main movement has invalidated in-progress rounds three times."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "35",
     "quote": "Evidence records carry artifact and dependency digests; relevant changes force the affected checks to be rerun."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
     "lines": "136-137",
     "quote": "current build it matches 0/55 lesson digests and 0/7 showcase digests and produces 12 current-validator errors."
    }
   ],
   "against": "\"Claim boundary: Unrelated changes need not invalidate scoped evidence.\" (versions/1.0.0/STANDARD.qmd line 216).",
   "adds_to_existing": [
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When improving content, protect verified strengths with regression checks so that changes do not flatten what already helps learners.",
   "kind": "adopted rule",
   "found_by": "Human review listed strengths to keep while asking for repairs; the standard added a 'preserve' verdict with regression guards.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/GOLDEN-CHECKLIST.qmd",
     "lines": "33",
     "quote": "Improvement never flattens or deletes behavior that already benefits learners."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "8",
     "quote": "## What's landing well (KEEP — do not break these)"
    }
   ],
   "against": "\"Claim boundary: A different implementation may be preserved when it meets the same outcome with equal or stronger evidence.\" (versions/1.0.0/STANDARD.qmd line 184).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When refining an existing course, work on a copy, preserve every original item, add new material as separate layers, and prove nothing was dropped with an item-level audit.",
   "kind": "adopted rule",
   "found_by": "Generalised raw-source to refined-clone process for course repair.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/source-course-refinement.qmd",
     "lines": "5",
     "quote": "This is a preservation-first workflow. The source course is treated as the content floor. The refined clone adds compliance, delivery, assessment, and evidence layers without cutting source content."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/source-course-refinement.qmd",
     "lines": "47",
     "quote": "| No silent cuts | Missing source ids fail the build. |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    23
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give every scored task an evidence contract — the knowledge it licenses, the claim, evidence indicators, conditions, scoring rule, acceptable variants, near-misses and forbidden shortcuts — because a learning goal written only in prose lets every writer and marker imagine a different task.",
   "kind": "measured",
   "found_by": "An audit found 0 of 432 items carried knowledge, scoring-rule or cue fields; clean-room review found a constructed response with no rubric or scorer.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "541",
     "quote": "Two people can read the same prose KC and imagine completely different tasks, difficulty levels, and acceptance thresholds — which means they're not really agreeing on the same KC at all."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md",
     "lines": "52",
     "quote": "The banks today carry **zero** `kc`, `scoring_rule`, or `cue`/`supports` fields (verified: 0/432)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
     "lines": "21",
     "quote": "A KC without a pack is prose, not a construct."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    33,
    69
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mark short written answers with a small rubric rather than an ever-growing list of accepted strings, and switch once the list passes about 15–20 variants or the key keeps being patched.",
   "kind": "adopted rule",
   "found_by": "Assessment pattern-library analysis of auto-scored short responses turning into brittle rule sets.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1470-1474",
     "quote": "- Switch to a rubric if any of these are true: - Your “acceptable answers” list exceeds ~15–20 variants. - You’ve edited the key twice post-launch to add more exceptions. - You keep finding “should-be-correct” responses that the rules miss. - Authors can’t confidently predict what the rules will mark."
    }
   ],
   "against": "Full automation stays appropriate for numeric or property tasks with explicit tolerances (same file, line 1469).",
   "adds_to_existing": [
    10,
    56
   ],
   "name_bearing_source": false
  },
  {
   "statement": "State in each multi-select stem how many options to choose and declare its scoring rule, and keep two-option and true/false items out of decisions because guessing swamps them.",
   "kind": "measured",
   "found_by": "4 of 48 multi-select stems lacked the select-how-many cue; a two-option item was a 50/50 guess.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-2/approval-package-v2/sources/ASSESSMENT-QUALITY-MEMO.md",
     "lines": "35",
     "quote": "Today **44 of 48** MSQ stems cue this; **4 do not**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/course-quality.qmd",
     "lines": "40",
     "quote": "- explicit count in multi-select stems;"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1403",
     "quote": "These formats are unusually sensitive to guessing, cueing, and ambiguous category boundaries—systematically inflating scores and undermining validity."
    }
   ],
   "against": "\"In bundles of 15+, the guessing averages out and T/F becomes more defensible.\" (Assessment & Feedback Brain line 2008).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Taught words must appear in the text the learner reads, be taught where the text first leans on them heavily, stay distinct from each other with none inside another's definition, and come back for the learner to use later.",
   "kind": "measured",
   "found_by": "12 of 46 taught words never appeared in their own lesson's text; a word used 8 times in one lesson was taught in the next; taught words recurred once; overlapping target words were flagged.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "53",
     "quote": "* **Never met in its own story.** 12 of 46 taught words appeared nowhere in their own lesson's"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "56-57",
     "quote": "`oxygen` appears **8× in U3-L1's passage** and 48× in its graded bank, and was taught in U3-L2."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "62",
     "quote": "self-check: no target word appears inside another target word's definition."
    }
   ],
   "against": "Contrast pairs taught together can legitimately share definition wording: \"They are semantic **oppo[sites]**\" — \"deliberate **contrast pairs** taught in parallel\" (VOCAB-AUDIT.md line 51).",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a word-meaning check every distractor must be a word the lesson taught, because an untaught distractor can be eliminated by unfamiliarity and so tests nothing.",
   "kind": "adopted rule",
   "found_by": "Meaning checks were found using untaught words as distractors.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
     "lines": "73-74",
     "quote": "Also: a meaning-check distractor must be a word **this lesson teaches**. A distractor naming an untaught word can only be eliminated by unfamiliarity, so it tests nothing."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give each taught concept one definition used verbatim on every surface, complete enough that it does not teach a different concept, and define it by what the thing does rather than a property it happens to have.",
   "kind": "measured",
   "found_by": "One concept carried four different definitions in one lesson, two making an incidental property definitional; another definition omitted the concept's main function.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "106-107",
     "quote": "**Rule.** A taught concept has exactly **one** authored definition string, and every surface that defines it uses that string verbatim."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "111-113",
     "quote": "Second half of the rule: the definition must be **complete for the age**, not merely accurate. A definition that omits the load-bearing part of the concept teaches a wrong one even though every word in it is true."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "126",
     "quote": "- *trickster* carried **four** definitions in one lesson"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Teach a concept with an example and a non-example that differ in exactly one feature, add a maximally different positive example to block over-generalisation, and state why the non-example fails by naming the method, not a property.",
   "kind": "measured",
   "found_by": "53 of 58 vocabulary non-examples gave no reason; all four cards in one lesson varied three features at once; one non-example made an incidental property disqualifying.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "396",
     "quote": "| **S1** | Every vocab `non_example` states **why** it is not an example | 53 / 58 cards state no reason |"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
     "lines": "158-159",
     "quote": "the minimally-different pair marks the boundary, but only the max-different example *kills the over-generalisation the pair invites*."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
     "lines": "81",
     "quote": "Engelmann-Carroll: vary surface features holding the distinction constant; vary the distinction holding surface features constant; never both on one item."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write questions and modelled answers specific to each text rather than generic templates, because a generic routine can teach a false rule.",
   "kind": "adopted rule",
   "found_by": "A generic 'find the one sentence, check it against the title' routine taught that evidence is always one sentence and that titles state the main idea.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "79",
     "quote": "| **Generic-not-bespoke question** | round-3: \"find the one sentence + check the title\" is bad advice — a fable's meaning is a synthesis, titles often don't tell the main idea |"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/FEEDBACK_RESPONSE.md",
     "lines": "37",
     "quote": "5. **Questions bespoke to the text, not generic templates.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    69
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test every learner-facing screen with a deletion test — remove each label, instruction, explanation, repeat and control that can go without losing learning, clarity or access — because models are poor at spotting excess text.",
   "kind": "adopted rule",
   "found_by": "Screens kept redundant instructions and restated questions; models had been 'terrible' at detecting and fixing excess text.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/meetings/incept-service-coe-2026-08-10/TEAM-UPDATES.qmd",
     "lines": "17-18",
     "quote": "> The one aspect where I feel we still need work is to ensure we have just enough text and none more > than absolutely necessary. LLMs have been terrible at detecting and fixing this so far"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/meetings/incept-service-coe-2026-08-10/TEAM-UPDATES.qmd",
     "lines": "21-23",
     "quote": "This is retained as a semantic deletion test, not a universal word cap: on the exact student surface, remove each label, instruction, explanation, repeated statement, and control that can be deleted without reducing learning, task clarity, continuity, or accessibility."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Make the learner's task the visually dominant element on each screen and check it on rendered pixels, because text-pattern checks can pass a screen where supporting material overwhelms the task.",
   "kind": "measured",
   "found_by": "A source text outweighed the learner's task about 4:1 on screen; a tripwire-only validator passed a failing screen.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "27",
     "quote": "passage outweighing the child's task 4:1"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "87-89",
     "quote": "primary must win the squint test (≥25% viewport on stage screens; ≥ largest competitor on work screens — enforce with pixels, not seam greps: a tripwire-only validator once passed a failing screen)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Reviews of learning content should credit genuine strengths specifically, not only list defects, because an audit that concedes nothing reads as rhetoric and loses trust.",
   "kind": "adopted rule",
   "found_by": "Red-team rounds learned that conceding strengths, including a team's self-imposed decertifications, kept adversarial review trusted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
     "lines": "172",
     "quote": "*Concede genuine strengths up front* — an audit that concedes nothing reads as rhetoric"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
     "lines": "154",
     "quote": "8. Credit what is good, specifically; open decisions get named owners, not"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Clear the rights to a text before writing anything anchored to its exact words, because a text withdrawn later strands every item and script tied to it.",
   "kind": "adopted rule",
   "found_by": "Span-anchored modelling scripts and evidence items couple to exact wording, so late withdrawal loses the lesson's artifacts.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
     "lines": "110-112",
     "quote": "copyright clears **passages before span-anchored authoring begins** — scripts and cite-items couple to exact text; a passage pulled after authoring loses the lesson's artifacts."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check a measure's reliability before reading anything into a null result, because an unreliable measure cannot show an effect either way.",
   "kind": "external research",
   "found_by": "A comprehension-question measure in an otherwise positive study had Cronbach's alpha .46 (Cervetti et al. 2016, DOI: 10.1007/s11145-016-9628-x).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/DIGEST-cervetti-wright-hwang-2016.qmd",
     "lines": "99",
     "quote": "> \"The Cronbach’s alpha was .46 which is considered far below acceptable criterion.\" — p. 770"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/DIGEST-cervetti-wright-hwang-2016.qmd",
     "lines": "101",
     "quote": "*Design relevance:* A methodological caution for assessment design: short open-ended comprehension-question batteries for young children can have poor reliability, so course assessments should pilot and report reliability before trusting question-level results."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Teach a general comprehension strategy briefly, explicitly and with the content it serves, then spend the time on knowledge, because extra strategy sessions add nothing.",
   "kind": "external research",
   "found_by": "Eight quantitative reviews: about 10 strategy sessions gave the same benefit as about 50 (Willingham & Lovette 2014, http://www.danielwillingham.com/); strategies divorced from content are not learned fully (RAND MR-1465 p. 39).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "134-135",
     "quote": "3. Across eight quantitative reviews, ~10 strategy-instruction sessions produce the same comprehension benefit as ~50 — no dose-response (Willingham 2014, p. 2)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd",
     "lines": "55-58",
     "quote": "\"Unless the strategies are closely linked with knowledge and understanding in a content area, students are unlikely to learn the strategies fully, may not perceive the strategies as valuable tools\" (p. 39)."
    }
   ],
   "against": "\"**Strategies genuinely work** (NRP; RAND Ch.4's \"well-replicated\" set...)... The claim is *bounded value*, not *no value*.\" (SYNTHESIS.qmd lines 172-176).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Record response time alongside correctness, because fast wrong answers signal confident misconceptions and slow right answers signal fragile knowledge that accuracy alone misclassifies.",
   "kind": "adopted rule",
   "found_by": "Practice BrainLift adopted into the instruction standard as the scheduling signal.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Practice BrainLift.md",
     "lines": "35",
     "quote": "Platforms that rely on accuracy alone will systematically misclassify learners, extending intervals for students who are computing rather than retrieving, and failing to catch fragile knowledge before it collapses."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
     "lines": "125",
     "quote": "The four-cell diagnostic (fast/slow × correct/incorrect) drives scheduling."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "If learners who succeed with an idea in one representation fail it in another, the knowledge unit is mis-specified, so treat representation shifts as a test of how the knowledge was carved.",
   "kind": "adopted rule",
   "found_by": "Knowledge-components BrainLift guidance on diagnosing badly sized or merged components.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Curriculum & Knowledge BrainLift.md",
     "lines": "549",
     "quote": "If learners who master a KC via text-based items fail when the same construct appears as a diagram, graph, or symbolic expression, that is not an item quirk — it is evidence about the KC boundary."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Split a knowledge unit only when its success condition changes; variations in difficulty, representation or method belong inside the unit rather than becoming new units.",
   "kind": "adopted rule",
   "found_by": "Over-granular graphs made prerequisite structure unmanageable for scheduling; the course graph absorbed variants into nodes.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/curriculum-architecture.md",
     "lines": "50-51",
     "quote": "3. **KC Mapping & Variant Handling** — exact/close/partial/none match rules; **fork a KC only when the success condition changes**."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Use low-stakes retrieval questions as learning events, not only as measurement, because retrieval practice beats restudying.",
   "kind": "external research",
   "found_by": "Testing effect for multiple-choice practice, g ≈ +0.70 versus restudying (MCQ BrainLift, citing Roediger & Karpicke 2006, https://doi.org/10.1111/j.1467-9280.2006.01693.x among others).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "1989",
     "quote": "The testing effect for MCQ-based practice (g = +0.70 vs. restudying) is one of the largest effect sizes in educational psychology."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/timeback-course-eval/references/eval-criteria.md",
     "lines": "38",
     "quote": "- **Retrieval practice** — Active recall is the primary learning event, not passive consumption."
    }
   ],
   "against": "Plausible distractors without feedback can implant false knowledge (same file line 1991).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Turn writers' own notes about fragile couplings ('must match', 'silently', 'or it will') into automatic checks, because they point at failures that are otherwise invisible.",
   "kind": "measured",
   "found_by": "A shipped note said a string must match the source character for character or a control silently degraded, and no check enforced it.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "121-124",
     "quote": "One shipped comment read \"must match the passage sentence character for character or the tap target silently falls back to buttons\" — a free specification for a check nobody wrote, guarding a **silent** failure mode."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Record review objections that were overruled, with the reasoning, and re-check them in the next round, because they become calibration evidence when the issue recurs.",
   "kind": "measured",
   "found_by": "An objection about a scaffold inverting the release gradient was overruled, and a later human review raised the same point independently.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/SKILL.md",
     "lines": "115-118",
     "quote": "When we raise an objection and are directed to proceed, record it with the reasoning. On 08-06 we argued a pre-filled quote inverts the release gradient, were told to implement without pushback, and on 08-11 the reviewer raised it independently."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When review rounds converge on cosmetic findings, check the design against the target it claims to serve, because quiet rounds can mask a real gap.",
   "kind": "measured",
   "found_by": "Three rounds of cosmetic findings hid that nobody had checked a plan against the test blueprint it targeted; the fourth found a coverage gap.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/RED_TEAM_R4.md",
     "lines": "12-14",
     "quote": "The convergence to cosmetics in R1–R3 was masking that nobody had checked the plan against the blueprint it claims to target — R4 did, and found a gap."
    }
   ],
   "against": "The factory's stopping rule is two consecutive rounds with zero new findings (docs/train-teacher-requirements.md lines 164-165).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Measure what items actually demand at the item level rather than from lesson-level tags, because retagging does not fix a mismatch between what a lesson teaches and what its items assess.",
   "kind": "measured",
   "found_by": "A course tagged 64% higher-order at lesson level was 58% / 42% at item level; 193 items were retagged and lessons still served items for a different skill.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g6-reading/G6-DOK-FINDING.md",
     "lines": "5-7",
     "quote": "**Distribution: 58% DOK-2 / 42% DOK-3.** Target is 60–70% DOK-3. **Why the gap:** the lesson-level \"64% DOK-3\" was misleading"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g6-reading/G6-DOK-FINDING.md",
     "lines": "12",
     "quote": "**Tagging cannot fix this — it's a content-rigor gap.**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
     "lines": "84",
     "quote": "| **Construct incoherence** | main-idea lesson served an inference item after a \"successful\" retag |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compute each item's chance of a correct guess from the scoring rule actually in use, not from the format label, because a pass bar within noise of chance measures nothing.",
   "kind": "measured",
   "found_by": "Live probing showed a select-k item authored as single-cardinality scored on the first token, changing its chance floor.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
     "lines": "117-120",
     "quote": "a select-k interaction authored `cardinality=\"single\"` scores \"first token in correct set\" (floor k/n, not 1/C(n,k)), so the format label alone never determines the floor. Pair-accuracy 0.50 is a solver-metric floor only, never a serving floor. A bar within noise of its floor measures nothing."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "End teaching media with a prompted recall rather than a summary, and put at least one prediction or discrimination before the answer is given.",
   "kind": "adopted rule",
   "found_by": "Video review classes: restatement outros and answers arriving before any learner operation.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "40",
     "quote": "14. ≥1 prediction/discrimination beat BEFORE the answer; recall-based outro (a prompted recall, not a restatement); paired retrieval item on the exact taught `fact_id`s; re-surface ≥1 day later."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
     "lines": "83-84",
     "quote": "| No prediction beat | answer arrives before any learner operation | 01_script (r14) | | Restatement outro | summary instead of prompted recall | 01_script (r14) |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Cut any media element that cannot name the fact it teaches or protects; decorative motion, b-roll, textured backgrounds and music are off by default, because completion is not success.",
   "kind": "adopted rule",
   "found_by": "Video QC found decorative filler and off-topic elements competing with teaching.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "12-13",
     "quote": "Every second must ENCODE a target fact or PROTECT the encoding of one. A second that does neither is a cut candidate. Completion ≠ success."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
     "lines": "29",
     "quote": "3. Cut any element that cannot name its target `fact_id`. Default OFF: music under narration, decorative b-roll, textured backgrounds, non-process motion, off-topic jokes."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    21,
    64
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check accessibility for every interaction type from the start, because formats chosen to resist guessing are often the least accessible, and an inaccessible format is not a faithful rehearsal of the test.",
   "kind": "measured",
   "found_by": "406 of 1,005 items were not keyboard or assistive-technology operable; the anti-guessing design concentrated items in exactly those formats; a 12-option item overloaded young learners.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
     "lines": "63",
     "quote": "* Accessibility: 406/1,005 (40%) not keyboard/AT-operable — disclosed, bigger than G5's exposure, platform-dependent."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "128",
     "quote": "An item type that cannot be made accessible is also not a faithful rehearsal of the test."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    27
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat 'where should this learner start?' and 'what are their gaps?' as different diagnostic problems: placement in a sequential course needs only a short binary search, while gap-finding needs sampling across the domain and a find-size-fill-verify cycle.",
   "kind": "adopted rule",
   "found_by": "Diagnostic BrainLift worked example on a nine-unit AP history course.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "370",
     "quote": "A placement diagnostic can be done in 10-15 items and 5 minutes."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "418",
     "quote": "This typically takes 3-4 items for a 9-unit course (log₂(9) ≈ 3.2)."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "373",
     "quote": "**Insight 6: You don't need to find all the holes at once — find a hole, size it, fill it, repeat.**"
    }
   ],
   "against": "Binary-search placement assumes the course is roughly sequential; without that structure \"this diagnostic is inappropriate\" (same BrainLift, Blueprint 2).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Knowledge taught together tends to be known or missing together, so in domains with few prerequisites use shared teaching history (the unit taught) to target sampling instead of testing every component.",
   "kind": "adopted rule",
   "found_by": "Diagnostic BrainLift: with few learners and flat prerequisite structure in AP history-type courses, cluster inference replaces prerequisite propagation.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "349",
     "quote": "KCs taught in the same unit, by the same teacher, in the same week, will be correlated in their mastery status — not because the KCs are logically related, but because the *causes* of knowing or not knowing them are shared."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "How many options should a multiple-choice item have — the three that research favours or the four that human review asks for — given that a weak fourth distractor adds cues?",
   "kind": "open question",
   "found_by": "Human review required four options while the MCQ BrainLift reports a research consensus for three (Rodriguez 2005 meta-analysis of 80 years of research); the conflict was routed to an owner.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "2006",
     "quote": "The discipline: if you cannot write a third plausible distractor for a given item, use three options rather than adding filler."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "102-105",
     "quote": "The reviewer asks for at least four MCQ options, while the MCQ BrainLift reports a research consensus favoring three and recommends four as Alpha's default only when all distractors remain plausible and diagnostically useful. An agent must not resolve this by adding filler; the assessment owner must approve the default and exception."
    }
   ],
   "against": "\"Claim boundary: No fixed option count belongs in the universal standard.\" (versions/1.0.0/STANDARD.qmd line 770).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Should a taught routine fade away once a stated condition is met, or keep being retrieved on a schedule?",
   "kind": "open question",
   "found_by": "Held dispute between the scaffold-fading reading of the research and the practice-architecture reading, pending a ruling.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "68-70",
     "quote": "- **T2:** named inference routines as *fading scaffolds* retired on a stated condition (our stance, per Willingham DOK1-3) vs. scheduled recurring retrieval of the routine (a plain reading of practice-architecture doctrine)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Should practice match the format of the final test, or mostly not resemble it, with test-format practice saved for the end?",
   "kind": "open question",
   "found_by": "Direct instruction says mastery tests should match instruction formats; the 'marathon rule' says early practice should mostly not look like the test; recorded as an open tension.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Direct Instruction BrainLift.md",
     "lines": "11",
     "quote": "- You should ensure test items in mastery tests match the formats experienced during instruction."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/gauntlet-spec.md",
     "lines": "32-34",
     "quote": "- **Marathon-rule probe** (reading): does early practice look like the test? (It mostly shouldn't — vocabulary-in-context, monitoring prompts, knowledge work; test-format practice concentrated late, timed conditions last.)"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
     "lines": "98-99",
     "quote": "1. **\"Test formats match instruction formats\" (DI) vs our cold-transfer thesis** — compatible read: format familiarity + passage coldness. Confirm."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Does transfer to unpredictable test content come from covering many knowledge areas broadly or from covering fewer ideas in depth?",
   "kind": "open question",
   "found_by": "The reading doctrine bets on breadth because test topics are unpredictable, while an AP course BrainLift argues fewer ideas in depth retain and transfer better.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "90-92",
     "quote": "so the only rational hedge is breadth: many knowledge networks + Tier-2 vocabulary + taught comprehension monitoring. Measurement cannot rescue a narrow curriculum."
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-ap-brainlift.md",
     "lines": "91",
     "quote": "- Covering less, better, leads to stronger retention and better thinking. Quality of effort > quantity of material."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": true
  },
  {
   "statement": "How far can learners' own reports of what they know be trusted for routing their study?",
   "kind": "open question",
   "found_by": "The diagnostic BrainLift calls self-report the cheapest underused signal in low-stakes settings, while reading research finds readers calibrate their understanding poorly and word-knowledge self-checks overstate knowledge.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
     "lines": "352",
     "quote": "- **SPOV 9: The student is a diagnostic instrument — ask them. Self-report is the cheapest, fastest, and most underused signal in diagnostic assessment.**"
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/SYNTHESIS.qmd",
     "lines": "180-181",
     "quote": "\"most child and adult readers have a poor ability to calibrate the success of their comprehension\""
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
     "lines": "142-143",
     "quote": "7. Word knowledge is a continuum: ~80% of students check a word as \"known,\" ~50% can give an example, ~20% can explain it"
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
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
   "lines": "78",
   "quote": "Minimum: reveal the correct answer; standard: name the misconception and offer a re-attempt."
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Direct Instruction BrainLift.md",
   "lines": "60",
   "quote": "- You should correct the response immediately when a student answers a question incorrectly by stating the correct answer with a brief explanation."
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
   "lines": "36",
   "quote": "- **Evidence-anchored.** Names the passage evidence in one sentence; never generic"
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
   "lines": "27-29",
   "quote": "must be true for EVERY index classified into that branch (a \"what happened\" claim may not cover a speech line). Never misquote the passage inside quotation marks."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "43",
   "quote": "The durable rule is attempt first, then targeted help."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/labeled-defect-corpus.jsonl",
   "lines": "2",
   "quote": "teaching content leaking the answer to the check it precedes."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "883",
   "quote": "- Claim boundary: Vocabulary support must not pre-answer the target question."
  },
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/07-SCORING-FEEDBACK-XP.md",
   "lines": "223-226",
   "quote": "- **Single-select reveal**: R-Q-20 ([name] Cottinghatt, during-reading checks get two attempts then a reveal) and the §3 no-reveal rule above give opposite instructions on the exact item type [name] wrote about. This repo ships the no-reveal behavior on its own reasoning; [name]'s ruling is still pending."
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-6/distilled/03-INSTRUCTION-DESIGN.md",
   "lines": "136-137",
   "quote": "on a second miss, fill the slot with the correct ending and say so — never dress a filled answer as a child win"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
   "lines": "233",
   "quote": "a course-wide audit found **~half of ~700 items gameable**. InceptBench scored one gameable item **1.0**"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
   "lines": "47",
   "quote": "* Prior-knowledge answerability — the knowledge-expedition design makes items about real-world facts (pitch physics, Magellan, explorer funding) answerable by any knowledgeable solver with no passage."
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/practice-layer-spec.md",
   "lines": "27-28",
   "quote": "- *fixed-retrieval anchors* (vocabulary/canonical facts from the taught spine): exempt from passage-dependence **by design**; gated instead on spine membership (taught content only) and"
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-ENTRYPOINT-CLEAN-ROOM-G3-U4-L1-2026-08-06.qmd",
   "lines": "59-60",
   "quote": "3. One hot-text prompt can reasonably be answered by either winter or spring camouflage, while only the winter sentence is keyed."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
   "lines": "155-156",
   "quote": "\"The intended answer is stronger\" does not repair a hard-scored item when another option also answers the question."
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "205",
   "quote": "stop at key points INSIDE the text and ask right there (REL West), not only at the end"
  },
  {
   "truth": 7,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "639",
   "quote": "- Failure signals: Analysis before encounter; hidden source; universal title shortcut; valid synthesis rejected."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/redteam-sources/g4-reading-redteam-round1-2026-07-07.md",
   "lines": "53",
   "quote": "Census over all 116 EBSR + a random 100-MCQ sample: 79% of MCQ correct answers sit at Choice A (expected ~25%); EBSR corrects are 65% Choice A, and the (Part A, Part B) pair (A,A) covers 50% of all EBSR."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/evaluator-spec.md",
   "lines": "150-152",
   "quote": "and does not detect within-lesson position *runs* (a student-visible streak that a course-wide histogram averages away)."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "2020",
   "quote": "Test makers systematically over-place correct answers in middle positions (B ≈ 30%, C ≈ 29% vs. A ≈ 19%, D ≈ 22% across large-scale exams)."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "93-94",
   "quote": "- **Flat score row** — the judge returns identical/undiscriminating statuses; treat as a non-answer (re-ask once, then RED), never as a pass."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-LIBRARY-USABILITY-CLEAN-ROOM-2026-08-07.qmd",
   "lines": "64",
   "quote": "2. Written-response completion can accept a fluent but false response through length and selection counts."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "655",
   "quote": "- Failure signals: Keyword or word-count pass called comprehension; unbounded judgment; no uncertainty route; hidden target leaked to learner."
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/alpha-read/modelling-moment-procedures-v2/INDEX.qmd",
   "lines": "152-153",
   "quote": "When an open-answer accept-list contains varied answer families, feedback branches by family and never credits language the learner did not supply."
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/PROJECTION.qmd",
   "lines": "50-51",
   "quote": "a prompt-like unknown field also fails the closed input contract and is never treated as an instruction."
  },
  {
   "truth": 14,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "400",
   "quote": "- Claim boundary: Repair evidence remains distinct from first-try evidence."
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "1999",
   "quote": "A 5-item quiz is useful for retrieval practice but too unreliable for mastery decisions."
  },
  {
   "truth": 15,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "499",
   "quote": "- 1/2 → Uncertain. In a low-stakes diagnostic context, treat as a probable gap and route to remediation (erring on the side of over-scoping rather than missing a gap."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/reading-science/EXTRACTION_EVIDENCE.qmd",
   "lines": "32-36",
   "quote": "- **Quote integrity:** 230/230 extracted quotes verified verbatim at extraction time (`verify_quotes.py --json claims.json`); **271/271** quoted spans verified in the rendered SYNTHESIS + DIGEST files (incl. the 4 EduQwen digest quotes added 2026-07-13). The four EduQwen checks establish presence in the scoped extraction only, not full-paper coverage. Zero fabricated quotes survived the pipeline."
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/teaching-reading-comprehension-brainlift.md",
   "lines": "136-137",
   "quote": "4. Only ~5–15 of 100 unfamiliar words met in natural reading are learned; misdirective contexts teach approximately zero (Beck et al. 2013, pp. 5–8)."
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "39",
   "quote": "| Term before taught | technical term used before defined | 01_script sequencing |"
  },
  {
   "truth": 20,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/1.0.0/STANDARD.qmd",
   "lines": "249",
   "quote": "- Failure signals: Unverified exposure assumption; accidental first instruction; support arrives after it is needed."
  },
  {
   "truth": 21,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "35",
   "quote": "| Narrated change never shown | \"watch it divide\" over a static cell (the 10b atomic-question class) | 07_clips |"
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "182-183",
   "quote": "> **Editing a passage has a hard constraint:** audio clips are keyed on > `sha1(VOICE|STYLE|text)`, so **insert whole new sentences; never extend an existing one.**"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "176-177",
   "quote": "Docs said fiction runs 450–500 words. Measured: informational passages were **312–333** while stories were 451–502. The reviewer noticed before we did."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/FEEDBACK-LEDGER.md",
   "lines": "173",
   "quote": "- **#14 is the highest-leverage item: the endorsed chunked variant is NOT in content/course.json (RT-11) — unreachable by children. Promote it first.**"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/teacher-contract.md",
   "lines": "69-70",
   "quote": "- **Length-parity recompute.** Compute option word counts programmatically; the correct option must not be the max. Do not trust the authored annotation — recompute."
  },
  {
   "truth": 26,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Direct Instruction BrainLift.md",
   "lines": "44",
   "quote": "- You should avoid presenting redundant text that duplicates the speech."
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-quality-standard.md",
   "lines": "88",
   "quote": "- **Automated WCAG contrast checks** in render QA (round-2 found black-on-black)."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
   "lines": "120",
   "quote": "In a hands-on walkthrough one of us earned a stamp on \"The Amazing Axolotl\" at about 20 percent accuracy by clicking through without reading, then advanced with the passage hidden from view."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
   "lines": "91",
   "quote": "item, empty-answer Next on every gate (leaks award XP — found live twice),"
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/evidence/AGENT-LIBRARY-USABILITY-CLEAN-ROOM-2026-08-07.qmd",
   "lines": "65",
   "quote": "3. One incorrect comprehension response unlocks `Next` while the feedback still says `Pick again`."
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/source-registry.md",
   "lines": "5",
   "quote": "gauntlet results, telemetry) · **D** = model judgment / synthesis (never load-bearing"
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/gauntlet-spec.md",
   "lines": "86-88",
   "quote": "The hedge/feedback lints scan the whole authoring file, so author annotations (\"possibly removed\") register as false positives. Fix: target only child-facing instructional strings, not authoring notes."
  },
  {
   "truth": 32,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/train-teacher/references/gauntlet-spec.md",
   "lines": "38-40",
   "quote": "Three judge agents from model families the Builder never used, adversarial framing (\"try to refute that this teaches\"), scoring against instruction-quality standard §1–11 as a rubric."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
   "lines": "231",
   "quote": "IB quality scores are the MEDIAN of 3 runs (non-determinism precedent: 0.95/0.92/0.98 on identical content)"
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "85-86",
   "quote": "* **Verdicts pinned** by `sha256(RULES_VERSION + string)` — a model that flips its mind can't flap the gate."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g5-reading/analysis/seq-reprobe-2026-07-07/README.md",
   "lines": "4-5",
   "quote": "The sequence anti-leak gate scored **one** seeded shuffle per item. A leaky ordering item can pass on a single lucky shuffle."
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "3192",
   "quote": "Zotos et al. (2025) demonstrate that LLM uncertainty — measured as first-token probability and sensitivity to answer-choice ordering — correlates better with human difficulty than the model's actual correctness."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g4g5-writing/approval-package/RED_TEAM_R1.md",
   "lines": "41-42",
   "quote": "So the true statement is **\"12 items × 4 banded responses = 48 scored responses; 87.5% agreement (42/48), 1 false-high, 0 concerning.\"**"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/instruction-modes-spec.md",
   "lines": "92-94",
   "quote": "These run as LLM-judge with a mandatory human sample per unit and become blocking only after a calibration pass against the round-2 failure examples."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/course-eval-layer/README.md",
   "lines": "44-45",
   "quote": "- Before claiming sensitivity/specificity, materialize each row as machine-readable input plus an expected assertion, version both, and run the implementation against them."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
   "lines": "281",
   "quote": "For every claimed gate, plant a representative defect and prove that the gate rejects it."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
   "lines": "47-49",
   "quote": "The Review Evidence consistency linter passes all 13 fail-closed mutation checks, including a clean `graph.dangling_edge` finding for a broken hard-prerequisite endpoint rather than an uncaught traceback."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "2022",
   "quote": "A distractor selected more by high-performing students than low-performing students suggests the keyed answer is wrong or ambiguous."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/course-quality.qmd",
   "lines": "55",
   "quote": "- generation trace including rejected attempts."
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
   "lines": "46-48",
   "quote": "10. **Openers**: motivate (create the headache / set the throughline / confront a misconception) → orient (problem + target performance) → one prerequisite retrieval prompt. Never lead with vocabulary or an unrelated hook."
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "33",
   "quote": "> **Design rule:** the we-do must **extend** the modeled skill, never replay it."
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
   "lines": "147-153",
   "quote": "1. hide the intended key; 2. enumerate every defensible answer or answer set; 3. cite the passage or representation evidence for each; 4. repeat with at least three option-aliased or shuffled views; 5. reveal the key only after the alternatives are recorded."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "57",
   "quote": "A clean automated report is useful pre-review evidence, never a substitute for reviewer judgment."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
   "lines": "23",
   "quote": "Deterministic screens route every passage to named human review; machine checks do not approve content."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
   "lines": "5-7",
   "quote": "primary metric, test set, baselines, ceiling, and gates are fixed now; any later change is an appended methodology-correction note, never a rewrite."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "280-281",
   "quote": "* **Test at 390px.** ~29 gates all ran at 1400×1000, hiding a top-bar overflow on **every beat of every lesson**."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
   "lines": "255",
   "quote": "if either renders in authored order, \"always click the first option\" clears the 90% gate"
  },
  {
   "truth": 47,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/key-quality-gates.md",
   "lines": "84-86",
   "quote": "Walker end-to-end green (`scripts/verify/walk-lesson.mjs` — keep model answers + fixtures current; a stale fixture once masked a real regression and once hid an engine crash)."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/course-quality.qmd",
   "lines": "61",
   "quote": "A fully green build gate proves the course is well-built. It does not prove the course works."
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
   "lines": "71-72",
   "quote": "Serving mastery forms same-session with feedback measures acquisition and calls it mastery — their SPOV1 critique verbatim."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "343",
   "quote": "A score of \"65% on Unit 3\" is useless for personalisation."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/review-hub/course-insights-d7f57fb/ATOMS.json",
   "lines": "479",
   "quote": "Preserve each historical source's identity, repository, edition or representation boundary, rights note, student material, and content digest."
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/generator-insights.md",
   "lines": "143-144",
   "quote": "**A generator optimizing for pass-rates or engagement will quietly lower rigor and destroy the very thing that works.**"
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
   "lines": "101",
   "quote": "That is encouragement, not acceptance, certification, or proof of learning."
  },
  {
   "truth": 52,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-agent-v0.2.md",
   "lines": "38",
   "quote": "12. Animate ONLY genuine motion/process (procedural animation can win up to d≈1.06; loses to statics when transient). Use progressively built statics for structure."
  },
  {
   "truth": 52,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback1/Generic Instruction BrainLift.md",
   "lines": "108",
   "quote": "Test: replace the motion with a still of the end state — does the student lose something essential?"
  },
  {
   "truth": 52,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/academics-alignment-plan.md",
   "lines": "102-103",
   "quote": "3. **DI video-first vs Generic Instruction \"default to text\" (§20)** — their docs disagree; ask which governs reading."
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g7-science/brainlifts/video-generation-human-v0.2.md",
   "lines": "286",
   "quote": "- **Captioning benefit for our learners is uncertain.** Strong evidence is L2/vocab; benefit for fluent learners in dense instructional video is not established."
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/video-red-team/references/finding-taxonomy.md",
   "lines": "76",
   "quote": "| Caption duplicates text card | same words twice on screen | 09_captions suppression (r18) |"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
   "lines": "876-879",
   "quote": "The door is revealed after ~20s (`CFU_UNSURE_MS`), below the tappables, deliberately. It is the one button on screen that cannot be wrong, so mounted with the options it becomes the *cheap path* and children who would have answered take it."
  },
  {
   "truth": 56,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/feedback/feedback3/WF - Assessment  Feedback Brain - 260624-200115.md",
   "lines": "1471",
   "quote": "- Your “acceptable answers” list exceeds ~15–20 variants."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/BUILD-RULES.md",
   "lines": "30-32",
   "quote": "5. **Grounding** (grounding_check): every claim in I-do answer cards + chart frame values must be verifiable from THIS lesson's passage (not another lesson's, not the hook item). Think-alouds may paraphrase but never invent sensory/setting details."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
   "lines": "121",
   "quote": "and model memory cannot support `PASS`."
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-content-integrity/SKILL.md",
   "lines": "155",
   "quote": "is `NEEDS_HUMAN`; repeated support for two answers is `FAIL`."
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g6-reading/G6-DOK-FINDING.md",
   "lines": "7-9",
   "quote": "**Why the gap:** the lesson-level \"64% DOK-3\" was misleading — every lesson front-loads 3–4 DOK-2 boilerplate items"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
   "lines": "224",
   "quote": "the generator was calibrating passages at **grade 11, not grade 3**; verify the target grade before any batch"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/versions/2.0.0/PROFILE-PARITY.qmd",
   "lines": "9-10",
   "quote": "it never infers a grade or capability from filenames, prose, or a reviewer request."
  },
  {
   "truth": 65,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/course-formula-agents.md",
   "lines": "218",
   "quote": "systematic defect patterns (same defect class across a whole batch = generator prompt bug, not per-item fixes)"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/course-red-team/references/finding-taxonomy.md",
   "lines": "22",
   "quote": "191 choice items certified on a same-family lane while docs said \"every item blind-probed under a different model family\""
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/g3-reading/iteration-3/CONTENT-FAILURE-CLASSES.md",
   "lines": "84",
   "quote": "* **Regex prefilter** cuts 5,396 strings to ~65 suspects, so the LLM judges 1% of the corpus."
  },
  {
   "truth": 68,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/skills/g3-reading-red-team/references/feedback-2026-08-06-addendum.md",
   "lines": "223",
   "quote": "**And the leak is per-lesson, not per-item.**"
  },
  {
   "truth": 69,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/standards/student-course-quality/sources/knowledge-bot/kb-0164-g3-v2-feedback-agent-routing.qmd",
   "lines": "84-85",
   "quote": "- no KC, claim, evidence indicators, task conditions, outcome space, and scoring rule means no assessment;"
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/docs/handoffs-2026-07-13/pedagogy-llm-eval-contract.md",
   "lines": "53-54",
   "quote": "- **Arm B (base): the untrained base model + the SAME prompts and briefs.** Isolates what training added; run it or the result is uninterpretable."
  }
 ]
}
```
