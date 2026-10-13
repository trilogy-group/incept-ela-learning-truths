# read:gap:content-checkers-and-small-generators

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "content-checkers-and-small-generators",
 "coverage": {
  "read": [
   "~/Projects/shadow/content-eval/README.md",
   "~/Projects/shadow/content-eval/SKILL.md",
   "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
   "~/Projects/shadow/content-eval/reports/G3-U1-L2-main-review.md",
   "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
   "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
   "~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md",
   "~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md",
   "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "~/Projects/shadow/content-eval/reports/G3-U2-L1-main-review.md",
   "~/Projects/shadow/content-eval/references/closing_questions_pattern.md (compared line by line with the covered ~/Projects/grade3-reading/artifacts/feedback-closing-questions-2026-09-24/Closing_Questions_Pattern.txt; only the differing parts were mined)",
   "~/Projects/uae-education-ai/README.md",
   "~/Projects/uae-education-ai/EVALUATION.md",
   "~/Projects/uae-education-ai/DECISIONS.md",
   "~/Projects/uae-education-ai/HERETIC_PLAN.md",
   "~/Projects/uae-education-ai/REVIEW_PACKET.md",
   "~/Projects/uae-education-ai/CAPABILITY_GATE.md",
   "~/Projects/uae-education-ai/HARNESS.md",
   "~/Projects/uae-education-ai/reports/uae-heretic-smoke-20261009-ee31a9.md",
   "~/Projects/uae-education-ai/data/development_cases.json (structure, top-level notes, the 5-rule catalog, label/rule/family counts, and the single case D012 only)",
   "~/Projects/uae-education-ai/data/heretic_synthetic_v3/manifest.json (structure, provenance notes, alias list, summary counts)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/README.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/question-generator-api/README.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/question-generator-api/docs/GOALS.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/question-generator-api/docs/ISSUES.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/question-generator-api/docs/ARCHITECTURE.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/question-generator-api/docs/API.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/input-generator/README.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/input-generator/IMPLEMENTATION_SUMMARY.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/input-generator/UAE_EDUCATIONAL_ANALYSIS_FINAL_REPORT.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/input-generator/moe_extension_summary.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/input-generator/content_compliance_validation.js (framework list and prompt/rule text only)",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144550.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144619.md",
   "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144953.md"
  ],
  "skipped": [
   "content-eval/references/passages/ (texts by others, per instructions)",
   "content-eval/references/grade3_known_words.txt (known-word list, per instructions)",
   "content-eval/webapp/ (per instructions)",
   "content-eval/references/word_forms.tsv, word_derivations.tsv, syllables.json (data tables; their use and calibration are described in SKILL.md)",
   "content-eval/docs/ (deploy and MCP how-tos, outside the listed scope)",
   "content-eval/audit.py (code; its contract and calibration notes are in SKILL.md)",
   "content-eval/reports/*.html (rendered versions of the md reviews; the G3-U2-L1 v2 HTML has no md, but the v3 md summarises every v2 finding in its 'Changes since v2' table)",
   "uae-education-ai/.env and .env.example (credential files, never opened)",
   "uae-education-ai/reports/*.json (dry-run, preflight, run and watchdog JSON; outside the listed reports/*.md scope)",
   "uae-education-ai/heretic_harness/, scripts/, tests/ (code)",
   "uae-education-ai/data/heretic_synthetic_v1, v2 and the v3 jsonl files (data; only the v3 manifest structure was in scope)",
   "uae-education-ai/data/development_cases.json cases other than D012 (structure only, per instructions)",
   "incept/input-generator/.env and the uae_education_results_*.json files (never opened, per instructions)",
   "incept/workflow/reports REPORT_20260223_154247.md and the evaluation/generated JSON files (not in the listed scope; REPORT_154247 is the later AP run the ML report cites)",
   "incept/input-generator other .py/.js files and logs (code and logs)",
   "incept other subfolders (ap_benchmark, aplit-quiz-generation, inceptbench, nova_forge, reading-question-qc, sat-reading-generation and others; outside this direction's scope)",
   "incept/ML_TRAINING_INSIGHTS_REPORT.md training sections (SFT data size, KTO learning rate and KL, hyperparameters, GPU costs, deployment timeouts): excluded as training mechanics and infrastructure"
  ],
  "notes": "Every quote was machine-checked as a substring of the cited lines (whitespace normalised for multi-line spans). The question-generator-api docs (README, GOALS, ISSUES, ARCHITECTURE, API) hold a live bearer token in plain text; I did not reproduce it, but it should be rotated or removed. Those docs are almost entirely infrastructure; their content-quality material is the ~80% vs 85% benchmark gap, 'Basic arithmetic questions dominate', and silent repair of malformed outputs (used as counter-evidence in the denominator candidate). The API's own example 'match' item keys every pair in row order (a1-b1 ... a4-b4) and 'Square' also fits 'Opposite sides equal': an instance of truths 6 and 8 in a format example, not a measurement. input-generator/README.md and content_compliance_validation.js are generic compliance/security validators (GDPR, HIPAA, marketing, API docs) with no learning-content rules; the prompt tells the model to 'Be thorough' across six broad areas, which is the open-ended fault hunt truth 32 warns against, but no outcome is recorded. IMPLEMENTATION_SUMMARY.md splits analysis and question extraction into two prompts but reports no measured effect. The ML report's 'near-miss' recommendation would lift pass rates partly by 'difficulty relabeling', which is a projection and changes labels rather than content. The smoke-run replacement-help leak (candidate on checking replacements) is my reading of the logged JSON; the report grades only the decisions. development_cases.json rules are synthetic and provisional pending review, so quotes from them are cited as definitions, not as adopted rules. One internal tension: SKILL.md says gate.max_tries is an outage escape count, not tries a child gets (lines 301-302), while two reviews ask which tries value the renderer honours. Names: SKILL.md (line 153-154) and the condensed spec (line 4) name the spec's author in their text; none of those lines are quoted and no statement carries a name or role. The only name in any cited path is the machine's account folder (~), so I set name_bearing_source to false throughout. ML_TRAINING_INSIGHTS_REPORT.md was compiled partly from a file whose name carries a person's name (listed on its line 478, not opened); the report's own path has no name. I did not run mgr: the task is read-only and the parent session owns registration."
 },
 "candidates": [
  {
   "statement": "Check every completion of a sentence frame, including its revealed model answer, by joining the frame's fixed words to each accepted answer; the joined sentence must read correctly.",
   "kind": "measured",
   "found_by": "Hand review of five lessons found frames that turned most of their accepted answers, and their own reveals, into broken sentences; the automatic audit never joins a frame to its answers.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
     "lines": "12",
     "quote": "**1. p21 `step4` — the Step 4 sentence frame is ungrammatical for 3 of the 4 clues it accepts, including its own reveal.**"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
     "lines": "139",
     "quote": "- whether a frame's start plus the accepted quote and answer reads as a sentence (items 1, 4, 5),"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md",
     "lines": "163",
     "quote": "- whether the frame lead plus each accepted answer and the reveal read as the taught sentence (items 3, 7, 8),"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "In a task done in steps, whatever one step marks right must still be accepted when the student carries it into the next step; steps that contradict each other fail the students who follow the method.",
   "kind": "measured",
   "found_by": "Reviews of four lessons found later steps rejecting what earlier steps had just accepted, or sending students away from the evidence a later step required.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
     "lines": "22",
     "quote": "A student who carries their Step 3 words forward, as the method teaches, fails Step 4."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
     "lines": "26",
     "quote": "A student who follows steps 1 and 2 as taught ends up looking in the wrong paragraph for the clue they must copy."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
     "lines": "22",
     "quote": "A student who carries Step 3's answer forward gets marked unpredictably."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "The method a lesson teaches, the method its guided and independent practice actually use, and the method its recap says the student used must be the same, under the same step names.",
   "kind": "measured",
   "found_by": "Reviews found practice pages using another lesson's step names, frames that dropped a taught step, and recaps claiming steps the student never did.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md",
     "lines": "6",
     "quote": "the lesson teaches a two-line \"then line + now line\" method, but the model, the guided practice and the solo practice all use one \"now\" line, and the recap then says the student found both."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
     "lines": "30",
     "quote": "In the one guided rehearsal, the student never practises \"Find what it caused\"."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
     "lines": "44",
     "quote": "5. **p20 `finish-the-writeup` and p21 `step4`: the sentence frames leave out Step 4's \"I know\" part, although the lesson teaches it and the recap says the student did it.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A recap or record of what a student did must be written for that item and list only what the student actually did; a recap copied from another example gives a false record.",
   "kind": "measured",
   "found_by": "Recaps on one independent-practice page were copied from the earlier worked example and listed that example's wrong answers as the student's picks; a later summary row claimed an activity students had only watched.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
     "lines": "60",
     "quote": "**9. p21 — the teacher recaps for `step2`, `step3` and `step4` are copied from the cave example.**"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
     "lines": "65",
     "quote": "Teachers will see the wrong record of what the student did."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-main-review.md",
     "lines": "169",
     "quote": "- A frame row that claims an activity the child never did (p25 row 5)."
    }
   ],
   "against": "Limit: the copied recaps were not shown to students: \"These are teacher-facing, not student-facing, but teachers get a wrong record of what the child did.\" (~/Projects/shadow/content-eval/reports/G3-U1-L2-main-review.md line 108)",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A check on a taught word must put the word in a new situation; a key that repeats the teaching example can be picked from memory without knowing the meaning.",
   "kind": "measured",
   "found_by": "In four lessons the keyed sentence of a word check copied or nearly copied the teaching card's own example.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
     "lines": "64",
     "quote": "A student can answer from memory of the card, without knowing what eerie means."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
     "lines": "95",
     "quote": "Memory of the example answers both, with no need to know the meaning."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md",
     "lines": "79",
     "quote": "This tests memory of the card, not the meaning."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A retry or hint message that is shown for every wrong answer must fit every answer it can be shown for, and must not assume how the student answered another part.",
   "kind": "measured",
   "found_by": "Retry messages written for one expected wrong answer were shown for every miss, including answers the item itself accepted; one blank's feedback assumed the previous blank was right.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
     "lines": "52",
     "quote": "It is shown for every miss, including \"scary\" or \"gloomy\"."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md",
     "lines": "67",
     "quote": "A student who typed \"scared\" is told about \"miserable\", and a student who typed \"miserable\" passes."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "180",
     "quote": "The `depend` feedback on blank 3 (*\"That word is already in the gap before this one\"*) assumes blank 2 was answered correctly."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In a worked example, the reason for rejecting an option must not apply equally to the option chosen, and the write-up must not then rely on evidence the example rejected.",
   "kind": "measured",
   "found_by": "Modelled think-alouds in four lessons rejected a clue for a reason the chosen clue shared, or marked lines rejected and then quoted them as the evidence.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
     "lines": "34",
     "quote": "The rule the student is shown doesn't separate the two lines."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md",
     "lines": "46",
     "quote": "6. **p19b think-aloud: the write-up uses lines the student just saw rejected.**"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "86",
     "quote": "**5. p19b `mm-find-jobs` — the stem and leaves evidence is marked `rejected`, then used (still open from v2 #7).**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Every model answer or reveal must pass the rubric it models; mark each reveal with its own rubric before it ships.",
   "kind": "measured",
   "found_by": "Reviews found reveals that missed half of their own pass threshold, matched their rubric's listed near miss, or broke the rubric's stated answer form.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md",
     "lines": "104",
     "quote": "15. **p22 `wrap-q1` — the reveal fails its own rubric.**"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "77",
     "quote": "- **Slot 2's model answer fails its own rubric** (second read)."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-main-review.md",
     "lines": "89",
     "quote": "- The reveal *\"Aladdin feels brave and calm.\"* is a full sentence, which the rubric says an answer never is."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "An exact quote is not enough: check separately that the quoted evidence supports everything the answer claims.",
   "kind": "adopted rule",
   "found_by": "A model sentence quoted a line that named only two of the three things its answer required; one evaluation design checks quotes for exact match in code and rates their support separately.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "124",
     "quote": "- The quote doesn't mention water, so the model answer asserts something its own evidence doesn't show."
    },
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "50",
     "quote": "Mechanically verify that each quote is an exact fragment substring. Blinded educators then rate whether the quote actually supports the stated verdict and rule: 0 = absent or misleading, 1 = relevant but incomplete, 2 = sufficient and faithful."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "282",
     "quote": "- **Evidence that doesn't cover the claim** (#9). The script doesn't check a write-frame's revealed quote against the revealed answer."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "The instruction a student sees and the rubric that marks it must ask for the same things; a rubric that demands more than the prompt, or waives what the prompt demands, misgrades students who did what was asked.",
   "kind": "measured",
   "found_by": "In two lessons, open items had rubrics that marked a second thing the prompt never asked for, or called optional a word the prompt told students to use.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "145",
     "quote": "- A child who answers what was asked (\"bees and animals\") meets only half the rubric and is sent back to say what each helper carries, which the prompt never asked for."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
     "lines": "74",
     "quote": "12. **p24 speak:** the instruction says *\"use at least one of our lesson words\"*, but the rubric says a lesson word is *\"never required.\"*"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "62",
     "quote": "- The rubric then says the word is \"welcome and never required\", so the ask promises something the marking ignores."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Test the rubric for a stated rule with the rule's negation; the negated answer must fail, which a keyword match cannot guarantee.",
   "kind": "adopted rule",
   "found_by": "The review checklist asks whether each rubric rejects the negation of its rule; one lesson's rubric did so explicitly.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "357",
     "quote": "**Does the rubric reject the negation?** \"Trust can *never* be broken\" must fail."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "266",
     "quote": "| Q1 marks on meaning and rejects the negation | **Yes** (the rubric explicitly rejects \"no part has a job\"). Clean up the \"word for word\" clause. |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    10
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Questions, hints, feedback and rubrics may rely only on what the student's own version of the text has said by that point: not later pages, not an earlier lesson's text, and not the original work it was adapted from.",
   "kind": "measured",
   "found_by": "Feedback in three lessons referred to characters and lines the student had not reached yet, re-read hints pointed at the previous lesson's text, and rubrics used details found only in the unabridged original.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
     "lines": "68",
     "quote": "9. **p10 `check` option 3 feedback: it refers to part of the story the student hasn't read yet.**"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md",
     "lines": "32",
     "quote": "A student who follows \"Re-read\" finds nothing to re-read."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
     "lines": "90",
     "quote": "Winter is in the original book, not this retelling."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1,
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A rule a lesson presents as true in general must hold for every case the lesson itself teaches; checking that takes subject knowledge, not a script.",
   "kind": "measured",
   "found_by": "A lesson asked students to recite a general sentence that was false for two of the five cases it taught, contradicting its own rubric and closing text.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "23",
     "quote": "**1. p24c `name-it` — the threshold sentence is false for two of the five parts the lesson teaches.**"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "31",
     "quote": "- So a child who has understood p21 is being asked to recite a sentence that contradicts it."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "280",
     "quote": "- **Q1's truth.** No mechanical check can tell that \"every part keeps the plant alive\" is false for reproductive parts. That needs subject knowledge."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A question frame designed on one kind of text must be tried on each other kind before it is used there; a frame built to draw out events collapsed into a near-tautology on an informational text.",
   "kind": "measured",
   "found_by": "Applying the closing frame's 'when' slot to an informational lesson produced model answers of the form 'a part does its job when it does its job'.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "72",
     "quote": "That says \"a part does its job when it does its job\"."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "74",
     "quote": "- The spec's \"when, not what\" rule is written for narrative, where \"when\" gets the mechanism. Here there is no event to point at."
    }
   ],
   "against": "The condensed spec and the checker treat the pattern as text-neutral: \"Nothing in the pattern is fiction-specific.\" (~/Projects/shadow/content-eval/references/closing_questions_pattern.md lines 8-9); the review left the fix open: \"Nonfiction probably needs its own frame variant\" (~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md line 83).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Anything reused from another lesson or item, such as a check, step names, narration or a feedback line, must be rewritten for its new place; copied pieces brought in the wrong skill, wrong steps and invented facts.",
   "kind": "measured",
   "found_by": "Reviews traced a skill check, a narration string and a feedback detail to other lessons and items.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md",
     "lines": "15",
     "quote": "**1. p18-intro `skill-check` — the quick check teaches the wrong skill.**"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md",
     "lines": "94",
     "quote": "It is the same string found in L12 and L14."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
     "lines": "18",
     "quote": "It is the p4c Grandpa sentence (*\"Grandpa whistled and waved to every neighbor\"*) copied over."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "The key must not stand out by form: it must not be the only option of a different kind, the only one that echoes the stem, or one whose wording names and rules out another option.",
   "kind": "measured",
   "found_by": "Audit flags and hand review found keys findable by stem echo, by being the only abstract or only paired option, and by wording that rejected a distractor.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "65",
     "quote": "a content word from the stem appears in the correct option **and in no distractor** — word-matching finds the answer without comprehension."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "106",
     "quote": "- \"Instead of flowers\" in the key names and rejects that distractor, so the two options argue with each other and the student can pick without reading."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md",
     "lines": "100",
     "quote": "*\"The mood of the tale's closing part\"* is the only abstract option. The others are concrete details (the tunnel's history, the number of weasels, the cell)."
    }
   ],
   "against": "Most mechanical form flags were false positives once read: \"The options are parallel; they only open with different words.\" (~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md line 112); \"in none of them is the correct option the longest or shortest outlier in a way that gives it away.\" (~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md line 106).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Flag absolute words in options when they set the key apart, that is, when every wrong option carries one and the key does not.",
   "kind": "adopted rule",
   "found_by": "The audit fires on absolutes only in that pattern, because only then is the key findable by shape.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "78",
     "quote": "every distractor carries an absolute (always/never/all/none/only…) and the key does not, so the key is findable by shape"
    }
   ],
   "against": "Another benchmark rejects outright any item whose distractors use such words: \"- **Absolute language** in distractors: \"total\", \"complete\", \"immediate\", \"all\", \"never\"\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/README.md line 95).",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every wrong option must be attractive to a student who misunderstood; an option nobody would pick, or one the stem's own wording rules out, turns a four-option item into a two-option one.",
   "kind": "measured",
   "found_by": "Hand review found dead or stem-contradicted distractors in several lessons; a generator benchmark found multiple-choice formats failing far more often than fill-in and put it down to distractor quality.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "342",
     "quote": "4-option item with two dead distractors is a 2-option item."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "138",
     "quote": "- Those describe taking in, not releasing, so a child can drop them on the verb alone. That makes it a two-option item (sugar or oxygen)."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md",
     "lines": "430",
     "quote": "The model fundamentally struggles with generating plausible, pedagogically-grounded distractor options."
    }
   ],
   "against": "A recap cloze kept obviously wrong options as acceptable: \"For blank 3, `charged`/`marched` \"into the night\" are grammatical but clearly wrong, which is acceptable.\" (~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md line 100).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A wrong option that never appears in the text is usually a sound contrast, not a defect; don't flag absence from the text on its own.",
   "kind": "measured",
   "found_by": "A grounding check that flagged options absent from the text fired almost only on well-made contrast distractors across 11 lessons and was demoted to information.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "83-84",
     "quote": "`DISTRACTOR-UNGROUNDED` is deliberately `info` and must never be reported as a defect on its own."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "84-86",
     "quote": "Across 11 lessons nearly every hit was a *well-made* contrast distractor — for *\"Who lives in the Wild Wood besides Badger?\"* the wrong animal sets are absent from the story **because they are wrong**."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "87-88",
     "quote": "Reusing story vocabulary would make a distractor easier to eliminate, not harder, so the premise is inverted for this common, correct pattern."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Treat one manual review as a floor: a second independent read that has not seen the first finds problems the first missed, and a finding raised by only one read must be checked against the source before it is reported.",
   "kind": "measured",
   "found_by": "A merged review of one lesson combined two independent manual reads; four medium findings came only from the second, which also caught a page the first had misjudged.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "286",
     "quote": "The two manual reads agreed on every high and on most mediums, but each found things the other missed. Four of the mediums above (#9–#12) came only from the second read. Treat one manual read as a floor, not a complete review."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "5",
     "quote": "Every finding that only one read raised was checked against the lesson JSON before it was included."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "226",
     "quote": "(v3 as first published dismissed it on length. The second read caught that it's hidden.)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compute lesson-level counts, such as the mix of question kinds, step numbering and answer positions, only over what students can see; counting hidden items inflated the mix and produced false findings.",
   "kind": "measured",
   "found_by": "The audit counted hidden items in its cognitive mix and its step checks.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "230",
     "quote": "The script counts 12 recall, 4 inference, 10 strategy, 2 vocab, **including hidden items**. Visible items only: **9 recall, 2 inference, 7 strategy, 1 vocab.**"
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "304-305",
     "quote": "The hidden nodes in L5 and L7 carry old unnumbered heads; counting them produced 21 false `STEP-UNNUMBERED` hits."
    }
   ],
   "against": "Per-item checks deliberately still run on hidden items, because \"a hidden item can be unhidden, and its defects come with it.\" (~/Projects/shadow/content-eval/SKILL.md lines 318-319).",
   "adds_to_existing": [
    24,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A checker must say what it did not read or evaluate, including new fields it does not recognise, so a clean result is never taken for full coverage.",
   "kind": "adopted rule",
   "found_by": "Every review ended with a list of what the script never evaluated, and the audit names unread prose fields after each schema change.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/README.md",
     "lines": "113",
     "quote": "## Coverage — read this before trusting a clean result"
    },
    {
     "path": "~/Projects/shadow/content-eval/README.md",
     "lines": "123-124",
     "quote": "**Schema drift is reported, not silent.** `SCHEMA-UNREAD` (info) names any field that holds prose the auditor never reads."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
     "lines": "115",
     "quote": "- whether wrong-answer feedback agrees with the passage and with other feedback in the same activity (items 1, 9, 10),"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Pull the student-facing text for checking from an explicit list of fields; a block list let non-student text, such as audio file names and voice names, into the checks.",
   "kind": "measured",
   "found_by": "The first extraction used a block list, and the word report filled with file and voice names.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/README.md",
     "lines": "151-153",
     "quote": "A blacklist was tried first and leaked tokenized audio filenames and TTS voice names into the vocabulary report."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "405-406",
     "quote": "Extraction is a strict whitelist on purpose: a blacklist leaked tokenized audio filenames and TTS voice names into the vocabulary report."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Decide whether two words are forms of one word from a published word-form table, never from spelling rules, and extend the table rather than adding rules.",
   "kind": "measured",
   "found_by": "A suffix-trimming matcher produced 234 false unfamiliar-word flags over 25 lesson runs and invented word links until published inflection and derivation tables replaced it.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "140-142",
     "quote": "The suffix-trimmer this replaced missed every irregular form: 234 false unfamiliar-word candidates across the 25 lesson runs (chose ×9, given, forgotten, teeth, mice)."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "149",
     "quote": "- To add a missing form, append a line to the table. Don't add a rule."
    }
   ],
   "against": "Stated limit: \"- A word the tables don't list matches only itself.\" (~/Projects/shadow/content-eval/SKILL.md line 146).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A text-matching check must keep every sentence, however short; a minimum length silently dropped one-word sentences that carried the key word and made a correct key look unsupported.",
   "kind": "measured",
   "found_by": "A correctly keyed answer was flagged as unsupported because its supporting sentence was one word long.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "105-108",
     "quote": "An earlier minimum length of 10 characters silently dropped one-word dramatic sentences — `\"Gratitude.\"` is exactly 10 — which is where this prose puts its key words, and it made a correctly-keyed answer look unsupported."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Where an item teaches a long word, judge its readability by sentence length and clause depth, not by a formula score that the taught word inflates.",
   "kind": "measured",
   "found_by": "Readability flags on word-teaching items came mostly from the taught word itself; reviews dismissed them after checking clause depth.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "112-115",
     "quote": "On those items judge **sentence length and clause depth**, not the score — a 24-word option with an embedded `because` clause against a grade-4 passage is a real problem; four short sentences carrying one long target word is not."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
     "lines": "132",
     "quote": "- **READABILITY on p2c, p3c and p4c:** the options are single-clause sentences of 9–15 words. The inflated FK score comes from polysyllabic words, not clause depth."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Apply each check only to the item types it fits: single-answer rules misfire on multi-select items, and text-grounding rules misfire on invented examples and on questions about the student's own thinking.",
   "kind": "measured",
   "found_by": "Treating every option item as single-answer, and checking invented example sentences against the story, produced false findings that the calibration notes now forbid.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "127-129",
     "quote": "Treating every option-bearing node as `mcq` produces false \"missing answer_index\" and \"missing feedback\" findings."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "119-121",
     "quote": "Word Power uses invented example sentences, and Skill/Story Pattern are metacognitive — checking any of those for story grounding is a false positive."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Define a term the same way everywhere it is defined, on its teaching card, in the glossary, in narration and in review, and never with the word itself.",
   "kind": "adopted rule",
   "found_by": "One lesson's glossary and video defined the same words differently; the audit compares every definition of a word and flags circular ones.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
     "lines": "95",
     "quote": "The glossary and the video also define things differently: jewels are \"Rare stones\" vs \"precious stones\", and the glossary adds that a genie \"lives in a lamp or ring\"."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "281",
     "quote": "the card, glossary, review frame and meaning lines define the word differently (stemmed word overlap under 0.34)"
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "280",
     "quote": "| `VOCAB-DEF-CIRCULAR` | med | the definition uses the word itself |"
    }
   ],
   "against": "Word-level comparison needs stemming: \"Without stemming, L5 *menacing* was a false positive.\" (~/Projects/shadow/content-eval/SKILL.md lines 314-315).",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After a word is taught, use it again in what students read and answer, at least three times, and test it with a question beyond its own teaching card.",
   "kind": "adopted rule",
   "found_by": "House vocabulary rules built into the audit as reinforcement and untested-word checks.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "68",
     "quote": "R-VOC-7: count the visible uses of each Word Power word **after its card** — story, questions, models, frames. Zero is `med`; fewer than 3 is `low`."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "288",
     "quote": "| `VOCAB-UNTESTED` | med | a taught word that no Word Power question (and not the card's own check) tests (B4) |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't use a word students may not know before the lesson teaches it, and count everything they are told, narration included, as teaching when checking this.",
   "kind": "measured",
   "found_by": "Every review listed untaught words in questions, feedback and recaps; counting only formal definitions had produced false untaught flags for words the narration defined.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "63",
     "quote": "Counting only formal definitions reported `sultan`/`stranger`/`magic` as untaught when the L1 narration defines them outright"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md",
     "lines": "81",
     "quote": "It uses *\"that is how actions are a **catalyst** for change\"*, which isn't a grade-3 word and isn't taught."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18,
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Record each ruling that a flagged item is fine in a shared list the checker reads, so the same false flag doesn't return on later runs.",
   "kind": "adopted rule",
   "found_by": "The checker's known-word baseline grows each time a lesson's flagged words are adjudicated.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/README.md",
     "lines": "145-147",
     "quote": "It improves every time a lesson is adjudicated — adding a genuinely-known word there silences its false flags across all future runs. Treat it as accumulated judgment, not a static config."
    }
   ],
   "against": "The list lags the rulings: \"The other high-priority unexplained-word candidates are known at grade 3; I haven't added them to `grade3_known_words.txt`.\" (~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md line 94).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Report each finding with its location, the offending text verbatim, one plain sentence on what is wrong and a concrete fix, and keep findings that are certain apart from judgment calls.",
   "kind": "adopted rule",
   "found_by": "The audit's two-pass design and reporting contract.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "393-394",
     "quote": "Never present a judgment call as a mechanical fact."
    },
    {
     "path": "~/Projects/shadow/content-eval/README.md",
     "lines": "22-23",
     "quote": "This split is the whole point: mechanical findings are trustworthy as stated, judgment findings are the reviewer's and are labelled as such."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "389",
     "quote": "- what is wrong, in one plain sentence"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44,
    67
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When re-reviewing a revised version, recheck every earlier finding by number and mark it open, fixed or moot; hiding an item makes its finding moot, not fixed.",
   "kind": "measured",
   "found_by": "Re-reviews of two lessons after a release tracked each earlier finding; most were still open, and several had only been hidden.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-main-review.md",
     "lines": "10",
     "quote": "- **Now hidden:** three old findings are moot: #7 (p4), #8 (p23) and #12 (p24). So is the answer-position cluster."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-main-review.md",
     "lines": "11",
     "quote": "- **Still open:** every other finding from 24 Sep. That includes all six highs on p21, p20c and p10."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-main-review.md",
     "lines": "12",
     "quote": "- **Both highs and 10 mediums are still open.** They are listed below with their fixes."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "What is spoken and what is on screen must say the same thing at the same moment; audio that runs ahead gives answers away, and words shown only on screen are never heard.",
   "kind": "measured",
   "found_by": "Comparing narration text with screen text in five lessons found audio ahead of the screen, recaps whose key words were never spoken, and prompts heard twice.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
     "lines": "80",
     "quote": "A student who taps the sparkle line before the reeds line hears which clue is strongest before *\"Now tap the strongest clue.\"*"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md",
     "lines": "82",
     "quote": "It never says the words, which appear only on screen."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
     "lines": "123",
     "quote": "- **p19b state 8 audio** narrates the lines of states 9–12 (*\"First I write, 'The text says'…\"*) while the screen still shows state 8."
    }
   ],
   "against": "The reviews compared only the narration text, not the recordings: \"**Not covered:** the audio recordings themselves (only their text was compared with the screen text) and how the pages look in the renderer.\" (~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md line 8).",
   "adds_to_existing": [
    3,
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Once a sequence reaches its unsupported task, nothing after it should bring support back, and the last task should carry the least help.",
   "kind": "adopted rule",
   "found_by": "Two lessons ended with a selection cloze after the final open question, and one final open question carried more hints than the guided question before it.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "51",
     "quote": "- The cloze is also selection (`inline_choice`), which is support coming back after Q3 had none. That breaks \"support fades and never returns\"."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "165",
     "quote": "Q3 carries a `nudge`, a keyword-triggered `nudge_if` (#13), a `hint` and a `second_hint`. That is more scaffolding than Q2's slots have."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "204",
     "quote": "- **`CLOSE-AFTER-USE` on a trailing wrap-up `inline_choice`** is the common case on staging."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A key idea taught once must be asked for again later in the unit, from memory and without being shown first.",
   "kind": "adopted rule",
   "found_by": "The closing-question pattern requires recurrence; the audit searches later lessons of the unit for it, and one lesson passed.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-main-review.md",
     "lines": "52",
     "quote": "| The Q1 sentence recurs later without being shown | **Pass.** It is asked for from memory in G3-U1-L7 p0b and G3-U1-L14 p0b. |"
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "201",
     "quote": "a reworded recall is not recognised, so check `CLOSE-RECUR-MISSING` by eye before reporting it."
    },
    {
     "path": "~/Projects/shadow/content-eval/references/closing_questions_pattern.md",
     "lines": "86",
     "quote": "| Spaced, repeated retrieval | well evidenced |"
    }
   ],
   "against": "Mechanical matching misses reworded recalls (SKILL.md line 201), and recurrence can't be checked when later lessons are missing: \"U2-L2 isn't in the file, so recurrence can't be checked yet.\" (~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md line 229).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Every goal a lesson states for a page must be asked about there; a stated goal that no question tests goes unchecked, and questions should target what the text is for rather than a detail nothing depends on.",
   "kind": "measured",
   "found_by": "Hand review compared each page's stated reading goal with its questions.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
     "lines": "88",
     "quote": "- **p8:** the reading goal *\"Notice what the jewels buy\"* is never tested."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
     "lines": "85",
     "quote": "- **p14 `check`:** the densest page (test, servants, marriage) is only tested on its first sentence, but its reading goal is *\"what Aladdin uses the genie's power to reach for.\"*"
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "372-374",
     "quote": "Does each comprehension question ask about what the text is *for* (the turn, the character's reason, the idea the lesson teaches), or about a detail nothing depends on?"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Measure separately how many questions need reasoning rather than recall; authored and generated sets alike drifted to literal recall even where accuracy and alignment scored near-perfect.",
   "kind": "measured",
   "found_by": "A generated set of 1,030 questions, a 50-question generated set and a hand-reviewed lesson all leaned on recall.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md",
     "lines": "345",
     "quote": "Near-perfect curriculum alignment (10.0) and factual accuracy (9.96), but **Inference & Pedagogy is the weak link** at 6.76/10.0, especially for Grade 12 (4.97). Questions tend toward rote recall rather than higher-order thinking."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144619.md",
     "lines": "64",
     "quote": "| `cognitive_demand` | 35 | Questions test recall rather than higher-order thinking |"
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-main-review.md",
     "lines": "91",
     "quote": "- **Cognitive mix.** Every visible Read-the-text question is literal recall (visible mix: 9 recall / 2 inference / 7 strategy / 1 vocab)."
    }
   ],
   "against": "The labels behind such counts can be wrong: \"p14 `check` is tagged inference, but it is recall (*\"clear off\"* is quoted). That lowers the real inference share below 36%.\" (~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md line 155).",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give a content writer the same standards, boundaries and difficulty definitions that its checker will judge against; judging against criteria the writer never saw caused most failures.",
   "kind": "measured",
   "found_by": "A question generator's benchmark failures were traced to assessment boundaries, difficulty definitions and objectives that the evaluator used and the generator never received.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md",
     "lines": "309",
     "quote": "The single biggest discovery was that InceptBench evaluates questions against **curriculum metadata that the model never sees during generation**:"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md",
     "lines": "312",
     "quote": "- This mismatch caused 70%+ of failures"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md",
     "lines": "422",
     "quote": "The biggest pass-rate improvement came not from model training but from **closing the information gap** between what the model sees (bare request) and what the evaluator checks (full curriculum metadata)."
    }
   ],
   "against": "The 70%+ share is stated without a breakdown, and the same report's failure table puts factual accuracy first: \"| 1 | **Factual Accuracy** | 650 | 46.1% |\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md line 301).",
   "adds_to_existing": [
    33,
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Checking and correcting generated items after generation can raise quality about as much as retraining the generator.",
   "kind": "measured",
   "found_by": "A question pipeline's pass rate rose after validation layers and correction of failed items were added.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md",
     "lines": "426",
     "quote": "The 6-layer validation pipeline (type enforcement, number range validation, visual reference detection, factual conventions, Wolfram math verification, Claude auto-correction) improved pass rates from ~41% to ~70% -- a gain comparable to fine-tuning itself."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md",
     "lines": "265",
     "quote": "| 2026-02-06 | Lambda v1 Pipeline | 298 | **55.4%** | 121 original + 37 corrected + 7 regenerated |"
    }
   ],
   "against": "The ~70% came from 50 questions and a later 1,888-question run scored 25.3%: \"| 2026-02-06 | Lambda v2 Pipeline | 50 | **~70%** | With validation layers |\" and \"| 2026-02-08 | Full Analysis | 1,888 (Grades 4,6,7,8) | **25.3%** | Comprehensive multi-grade evaluation |\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md lines 266-267); all of these gains were scored by a model benchmark, not by people.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A check or report that ran over zero items must stop with an error; a 0% pass rate with no failures, or 'all checks passing' on empty data, proves nothing.",
   "kind": "measured",
   "found_by": "An evaluation report over no questions printed a pass rate, 'no hard fail rules triggered' and a routine sign-off; an extension declared every acceptance check passing while its new fields held 0 entries.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144550.md",
     "lines": "12",
     "quote": "| Questions Evaluated | 0 |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144550.md",
     "lines": "57",
     "quote": "*No specific recommendations at this time. Continue monitoring quality metrics.*"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/input-generator/moe_extension_summary.md",
     "lines": "168",
     "quote": "All acceptance checks passing, zero data quality issues detected."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Compare runs only over the same items: a trend measured against an empty run reported an 18-point gain and marked every issue new, and a re-report of the same evaluation was counted as another iteration.",
   "kind": "measured",
   "found_by": "Iteration reports compared a 50-question run with two runs that evaluated nothing; iterations 3 and 4 cite the same evaluation file, and iteration 4 is labelled UP at +0.0 points.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144619.md",
     "lines": "25",
     "quote": "**Trend:** Pass rate improved by 18.0 percentage points from previous iteration."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144953.md",
     "lines": "41",
     "quote": "**These problems did NOT exist before. What changed?**"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144953.md",
     "lines": "96",
     "quote": "*Source: evaluation_20260223_144514.json*"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    60,
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a whole item type scores zero, check whether one structural rule or format mismatch caused it before judging the content.",
   "kind": "measured",
   "found_by": "In one 50-question evaluation, all 18 structural failures were for a missing explanation and all 18 fill-in items failed.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144619.md",
     "lines": "33",
     "quote": "| FILL-IN | 18 | 0 | 0.0% |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144619.md",
     "lines": "57",
     "quote": "| `missing_explanation` | 18 | Question lacks required explanation for correct answer |"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md",
     "lines": "375",
     "quote": "Fill-in and Match question types were **completely broken** (0% pass rate) due to missing explanations (hard-fail rule)."
    }
   ],
   "against": "The other zero-scoring type failed on content, not on that rule; a sample matching item shows \"- Failed dimensions: `factual_accuracy, curriculum_alignment, cognitive_demand, clarity, difficulty_alignment`\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144619.md line 90).",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count what was checked, not what was filled: a populated answer, score or 'verified' field says nothing about whether the content is right or whether anyone reviewed it.",
   "kind": "measured",
   "found_by": "A report on 4,165 machine-extracted questions presented field population rates as accuracy; its 'human verified' field was 100% populated although the field defaults to false.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/input-generator/UAE_EDUCATIONAL_ANALYSIS_FINAL_REPORT.md",
     "lines": "233",
     "quote": "- 99.7% have correct answers"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/input-generator/UAE_EDUCATIONAL_ANALYSIS_FINAL_REPORT.md",
     "lines": "246",
     "quote": "- Achieved 99.9%+ accuracy in core educational data"
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/input-generator/UAE_EDUCATIONAL_ANALYSIS_FINAL_REPORT.md",
     "lines": "94",
     "quote": "| `human_verified` | 108/108 (100%) | Verification status   |"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep expected verdicts, answer keys, flaw names and split labels out of everything a judge or generator sees, including file names and retrieval queries.",
   "kind": "adopted rule",
   "found_by": "Evaluation designs for a rule judge and a hint-release reviewer.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "12",
     "quote": "It does not see `family_id`, `split`, `reviewer_annotation`, any expected verdict, or a flaw name."
    },
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "40",
     "quote": "Do not put expected labels, rationales, or flaw names in retrieval queries, filenames shown to the model, prompts, or tool responses."
    },
    {
     "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
     "lines": "7",
     "quote": "Family IDs, answer keys, gold decisions, reviewer annotations, and case-type labels stay outside model input and retrieval."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    30,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When testing a checker or generator, keep all variants of one item, such as paraphrases, number swaps and shared templates, in the same split, and count distinct structures rather than rows.",
   "kind": "measured",
   "found_by": "An audit of a 488-record synthetic test set found that its 48 locked problem sets used only 24 calculation structures, with possible aliases across splits.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
     "lines": "15",
     "quote": "Split by underlying problem and template generator, including near-duplicate wording and number substitutions, never by quartet row."
    },
    {
     "path": "~/Projects/uae-education-ai/data/heretic_synthetic_v3/manifest.json",
     "lines": "372",
     "quote": "The 96 numeric task quartets use 48 candidate calculation graphs; the 48 locked quartets use 24 candidate graphs. Algebraic aliases and control lineage overlap remain unreviewed. Do not claim 48 distinct locked templates or independent template-level observations."
    },
    {
     "path": "~/Projects/uae-education-ai/REVIEW_PACKET.md",
     "lines": "15",
     "quote": "Five potential cross-split task aliases, 12 control-to-task math aliases, and three repeated safety proposal archetypes are recorded in the v3 manifest."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test any judgment about releasing help with matched cases that differ only in context, such as the same full solution during practice and during review, so a reviewer that always holds back or always releases cannot pass.",
   "kind": "adopted rule",
   "found_by": "A four-case smoke run of a hint reviewer rejected a valid hint, which only the matched good-hint case exposed.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
     "lines": "9",
     "quote": "Each problem family contains a four-case quartet: (1) practice plus a good hint → **RELEASE**; (2) practice plus a premature full solution → **REVISE** without answer leakage; (3) review plus that *same* full solution → **RELEASE**; (4) practice plus a wrong hint → **REVISE** to a correct hint."
    },
    {
     "path": "~/Projects/uae-education-ai/reports/uae-heretic-smoke-20261009-ee31a9.md",
     "lines": "41",
     "quote": "The valid hint was rejected, which is a behavior error under the stated synthetic policy."
    }
   ],
   "against": "The smoke run was a deployment check, not an evaluation: \"These four responses establish that the live deployment served inference and returned outputs; they do not establish acceptable educational behavior or any Heretic effect.\" (~/Projects/uae-education-ai/reports/uae-heretic-smoke-20261009-ee31a9.md line 41).",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a reviewer replaces help it has rejected, check the replacement for the same leak; replacements written after rejecting a full solution still did the decisive steps.",
   "kind": "measured",
   "found_by": "Read from the four logged responses of a smoke run: after rejecting a full solution and a wrong hint during practice, the reviewer wrote replacement help that performed the decisive calculations; the report itself grades only the decisions.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/reports/uae-heretic-smoke-20261009-ee31a9.md",
     "lines": "48",
     "quote": "First, add 12 and 16 to get 28. Then, subtract 17 from 28 to find the result."
    },
    {
     "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
     "lines": "7",
     "quote": "The learner sees only `learner_help`; audit every returned text field for answer leakage in practice before delivery."
    },
    {
     "path": "~/Projects/uae-education-ai/data/development_cases.json",
     "lines": "18",
     "quote": "While learners work independently, prompts may clarify task directions but must not give the final answer or a decisive calculation for that task."
    }
   ],
   "against": "The report does not grade replacement text, the run had only four requests, and the leak definition quoted comes from a provisional synthetic rule catalog.",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep every failed, malformed or cut-off output in the denominator and report it as unusable; silently repairing it or retrying until it passes hides the failure rate.",
   "kind": "adopted rule",
   "found_by": "Scoring design and harness tests for the hint reviewer.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "27",
     "quote": "Output that breaks the schema is reported separately and counts as unusable, not silently repaired."
    },
    {
     "path": "~/Projects/uae-education-ai/HARNESS.md",
     "lines": "16",
     "quote": "It validates the whole batch before calls, requires different base/edited model references and claimed fingerprints, and retains failed case/arm slots in the denominator."
    },
    {
     "path": "~/Projects/uae-education-ai/REVIEW_PACKET.md",
     "lines": "17",
     "quote": "Malformed JSON mappings, exceptions, and truncated/exhausted responses retain slots."
    }
   ],
   "against": "A deployed question generator does the opposite: \"- Lambda retries forever until success (within timeout)\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/question-generator-api/docs/GOALS.md line 19) and \"- Fallback manual JSON extraction\" (~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/question-generator-api/docs/ISSUES.md line 168).",
   "adds_to_existing": [
    36
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Score a judge's abstentions: an abstention is right only on a case that truly can't be decided, and unresolved disagreement between labellers stays marked undecidable rather than forced into a verdict.",
   "kind": "adopted rule",
   "found_by": "Evaluation design for a three-verdict rule judge, with a development case whose vague rule made it undecidable.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "49",
     "quote": "An abstention on a decidable case is not a correct verdict."
    },
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "42",
     "quote": "Preserve unresolved ambiguity as `insufficient_evidence` or an explicit exclusion with a reason, rather than forcing consensus."
    },
    {
     "path": "~/Projects/uae-education-ai/data/development_cases.json",
     "lines": "264",
     "quote": "The rule does not define how many examples are enough or which contexts are familiar to these learners. The fragment alone cannot settle either point."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report a checker's false accepts and false rejects separately, each over its own denominator and broken down by rule, rather than as one accuracy figure.",
   "kind": "adopted rule",
   "found_by": "Evaluation designs for a rule judge and a hint-release reviewer.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "46",
     "quote": "Score the three verdicts with a confusion matrix and per-class precision/recall, reporting counts and denominators."
    },
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "48",
     "quote": "- **False accept:** `follows` prediction on an educator-labeled `violates` case; report count / all `violates` cases."
    },
    {
     "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
     "lines": "28",
     "quote": "Report quartet all-pass, false approvals/rejections, semantic leakage in every learner-visible field, repair quality, and ordinary/safety controls."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    49
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A fix proposed by a checker should change only the faulty span, keep the objective and the useful teaching content, add no unsupported claim, and count against the checker when it edits sound content.",
   "kind": "adopted rule",
   "found_by": "Correction-quality criteria for a rule judge.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "27",
     "quote": "A correction may alter only the cited span, preserve useful teaching content and the learning objective, and avoid unsupported claims."
    },
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "51",
     "quote": "penalize unnecessary edits on compliant cases and vague evidence requests on insufficient cases."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    23
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When content and its fixed source text disagree, change the content, never the source, and compare them paragraph by paragraph so that legitimate excerpts aren't reported as rewrites.",
   "kind": "measured",
   "found_by": "Passage-fidelity checks against canonical texts; whole-passage alignment had reported legitimate excerpts as rewrites.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/README.md",
     "lines": "110-111",
     "quote": "To update a text, replace its file. Don't edit it to match a lesson: the lesson is what gets fixed."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "242",
     "quote": "Whole-node alignment reported both as rewrites."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "227",
     "quote": "| `PASSAGE-TEXT-CHANGED` | high | a word is added, removed or replaced relative to the fixed text |"
    }
   ],
   "against": "Mandated house-style changes are exempt: \"**Mandated** by R-COPY-1 (no dashes in child-facing JSON), not a defect\" (~/Projects/shadow/content-eval/SKILL.md line 233).",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Cases where an explicit rule is simply applied test the plumbing, not judgment; a test of judgment needs cases with several valid approaches, competing goals or missing context.",
   "kind": "adopted rule",
   "found_by": "Scoping of a rule-judge evaluation built on twelve synthetic explicit-rule cases.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "5",
     "quote": "Applying explicit rules to short fragments is a control for rule lookup, output formatting, and basic rule application. It is not yet a distinctive test of pedagogical judgment."
    },
    {
     "path": "~/Projects/uae-education-ai/DECISIONS.md",
     "lines": "33",
     "quote": "Create a separately authored value set involving multiple valid approaches, goal conflicts, and insufficient context."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Label any run on mock or placeholder outputs as a test of the plumbing; it says nothing about content quality and must not be reported as a result.",
   "kind": "adopted rule",
   "found_by": "A dry run of an evaluation harness with a deliberately naive fake model.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/HARNESS.md",
     "lines": "12",
     "quote": "Its output is labeled `FAKE_PROVIDER_SOFTWARE_TEST_ONLY`; it is **not** model or pedagogy evidence."
    },
    {
     "path": "~/Projects/uae-education-ai/REVIEW_PACKET.md",
     "lines": "16",
     "quote": "The naive fake is not a model or pedagogical score."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Never tune on the final test or rerun it to chase a pass, never claim a gain from the cases used in development, and call a result inconclusive when its uncertainty interval includes zero.",
   "kind": "adopted rule",
   "found_by": "Analysis plan for a paired before-and-after comparison.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
     "lines": "30",
     "quote": "This sample cannot prove tight 5-point noninferiority or broad safety; if the improvement interval includes zero, call the result inconclusive. Never tune on final outputs or rerun a hidden test to chase a pass."
    },
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "36",
     "quote": "Do not infer a tuning gain from development cases."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    45,
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Judge any tuned or edited model against the same model given the same instructions, sources and output budget, and keep the simpler baseline unless the change beats it.",
   "kind": "adopted rule",
   "found_by": "Comparison designs for a judge and a hint-release reviewer.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
     "lines": "9",
     "quote": "This tests whether an edit improves context-sensitive judgment beyond an equally informed prompt. A null result is valid. The prompt-only baseline remains the default demo if the edited model fails."
    },
    {
     "path": "~/Projects/uae-education-ai/EVALUATION.md",
     "lines": "32",
     "quote": "Use the same inference prompt, rule text, source access, decoding settings, and output budget as the prompted base."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Hide from human raters which system produced each output, shuffle the order, and have a second rater independently score a preset share plus every disputed or severe case before reporting.",
   "kind": "adopted rule",
   "found_by": "Review protocol for 672 blinded first reviews and 168 second reviews.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
     "lines": "28",
     "quote": "Blind model IDs and response order."
    },
    {
     "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
     "lines": "30",
     "quote": "A second educator independently reviews a prespecified, family/condition-stratified 25% of first reviews (**168**, plus every disputed or severe case); adjudicate differences."
    },
    {
     "path": "~/Projects/uae-education-ai/HARNESS.md",
     "lines": "16",
     "quote": "Its first-review locked report is explicitly preliminary; an adjudicated report additionally requires the prespecified second reviews and dispute coverage."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test cases of wrong help must show a realistic wrong step; a bare false result doesn't test whether a checker spots the error behind it.",
   "kind": "adopted rule",
   "found_by": "An audit of a synthetic test set found that most of its wrong-help examples only claimed a false result.",
   "evidence": [
    {
     "path": "~/Projects/uae-education-ai/data/heretic_synthetic_v3/manifest.json",
     "lines": "359",
     "quote": "Arithmetic addition task/control examples compute a coherent subtract-instead result. Other rows are mechanically false result claims only; they do not test detection of a particular wrong operation. Educator-authored wrong-step hints remain required."
    },
    {
     "path": "~/Projects/uae-education-ai/README.md",
     "lines": "9",
     "quote": "Addition wrong-help examples now show the computed result of subtracting instead; other wrong-help examples claim a false result without a stated operation."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Find a lesson's parts and its source text by their content and structure, never by ids or titles, which drift.",
   "kind": "adopted rule",
   "found_by": "The audit's closing-question and passage checks; a course file's ids lagged its source folders.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "157",
     "quote": "- **Detection is structural, never by node id or title.**"
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "221-223",
     "quote": "The source is confirmed by what the lesson's reading chunks contain, not by the lesson's `lessonId`. A course file whose ids lag the folder scheme still gets checked; the mismatch is reported as info."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Calibrate every automatic check on real content before trusting it, and narrow or demote a check when most of its hits turn out to be sound.",
   "kind": "measured",
   "found_by": "Running the audit over 11 to 25 lessons showed several checks firing mostly on sound items; each was narrowed or demoted to information.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "90-91",
     "quote": "Across 11 lessons it fired 184 times — on most distractors in the course."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "81",
     "quote": "**Calibration notes, all learned from real data — do not undo these:**"
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "70",
     "quote": "Deliberately narrow (fires only at that extreme), because good distractors are built from real story phrases; everything short of the extreme goes to the evidence pack as per-option `passage_coverage` for the judgment pass"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    37,
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Text that models what students should write must be free of errors, because students copy it.",
   "kind": "measured",
   "found_by": "Annotation lines that model the method contained comma splices on three pages of one lesson.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "208",
     "quote": "These lines model the method for the child, so the punctuation is copied."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "On a branching path, every branch must teach what later pages assume and agree with the other branches on the facts.",
   "kind": "measured",
   "found_by": "Hand review of dialogue branches in two lessons.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
     "lines": "103",
     "quote": "Students on `partial`/`off`/`silent` never see it, yet p25 (*\"how an obsession can take control\"*) and p26 (*\"The obsession made him reckless\"*) use it."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md",
     "lines": "81",
     "quote": "9. **p23 dialogue `silent` follow-up — the key contradicts the other branches.**"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Every item needs an explanation that agrees with its key and says why the common wrong choices are wrong.",
   "kind": "adopted rule",
   "found_by": "A benchmark's top recommendation after 18 items failed for missing explanations, and a generator training plan's list of weakest areas.",
   "evidence": [
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/workflow/reports/REPORT_20260223_144619.md",
     "lines": "104",
     "quote": "Every question must include an explanation of why the correct answer is correct and why common wrong choices are incorrect."
    },
    {
     "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md",
     "lines": "211",
     "quote": "3. **Answer key consistency** -- explanation must match the marked answer"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When students pick evidence from a set, the strongest evidence must be in the set, and the rubric must not credit evidence they cannot pick.",
   "kind": "measured",
   "found_by": "Hand review of tap-the-evidence items in two lessons.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "201",
     "quote": "- The sentence that links the job to survival, *\"This natural way of spreading helps plants survive in new places.\"*, isn't in the tappable list at all."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md",
     "lines": "93",
     "quote": "The rubric accepts *\"He stayed close, guarded Mole's back\"*, but that sentence isn't one of the tappable evidence spans."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md",
     "lines": "94",
     "quote": "- **p20 tap-the-clue:** *\"I am the reason you have all been dragged into this mess.\"* is the strongest \"owning it\" clue in the paragraph, but it isn't tappable as a clue."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Open: whether a lesson's key idea should first appear at the step that names it, or may be stated earlier so that the naming step lands as a recap.",
   "kind": "open question",
   "found_by": "Two reviews found the closing sentence already stated earlier in the lesson; one judged that fine for learning and noted the spec is silent.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "176",
     "quote": "That's fine for learning."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
     "lines": "177",
     "quote": "The spec is silent on this."
    },
    {
     "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-main-review.md",
     "lines": "134",
     "quote": "- **p23b is not first exposure.** p19b already tells the child the sentence (*\"Keep that idea close\"*), so Name it lands as a recap."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Open: when pushing a student toward a stronger word, whether to push for the source text's own word or for the lesson's taught word when the text never uses the taught word.",
   "kind": "open question",
   "found_by": "Every word-push hit on staging was a taught word the text never used, which departs from the spec's 'the stronger word the text supplies'; the checker downgraded these to information pending a decision.",
   "evidence": [
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "203",
     "quote": "It is `info` for Word Power words, because on staging all seven hits are taught words the story itself never uses."
    },
    {
     "path": "~/Projects/shadow/content-eval/SKILL.md",
     "lines": "359",
     "quote": "**Is the pushed word genuinely stronger** than the likely child answer, and is it the text's word rather than the lesson's?"
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
   "path": "~/Projects/shadow/content-eval/SKILL.md",
   "lines": "93-96",
   "quote": "Feedback that explains *why* an option is wrong (*\"Copper coins are what Aladdin's father left behind\"*) is good feedback with or without a \"read it again\" cue, so its absence is a style observation, not a defect."
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/SKILL.md",
   "lines": "72",
   "quote": "feedback on a *wrong* option names the answer's own distinctive vocabulary — picking that wrong option reveals the right one."
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
   "lines": "77",
   "quote": "Two wrong-answer feedbacks give away the answer: *\"names the thing on Aladdin's own hand\"* and *\"Re-read what the great figure says about **the ring**.\"*"
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
   "lines": "18",
   "quote": "So the same activity tells the student both that Mole wasn't lonely and that he was."
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "lines": "197",
   "quote": "Reword feedback[0] to *\"The text does not say animals get water from plants.\"*"
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
   "lines": "42",
   "quote": "\"modelling\" is also an adult word for grade 3."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "lines": "60",
   "quote": "The push arrives *before* the child answers. The spec says to accept the answer first and then push once."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
   "lines": "51",
   "quote": "So the student just copies a word from the same sentence."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "lines": "164",
   "quote": "If labels render anywhere on screen (header, progress bar, nav), the sentence is visible on the child's own turn, which turns recall into copying."
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md",
   "lines": "98",
   "quote": "The rubric says to coach *\"without giving the word away\"*, but the instruction already says *\"Use the word courage.\"*"
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md",
   "lines": "141",
   "quote": "- **p21 Step 3 (`know-step`)** is a text-only node that lists the answer (*\"hopeful, loyal, together\"*). The independent Step 3 isn't checked."
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "lines": "163",
   "quote": "The spec says two attempts, then the answer. Check which value the renderer honours. If the gate wins, a child gets a third try."
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
   "lines": "82",
   "quote": "Other lessons use \"Here is the ending: …\", which tells the student what to type in the blank."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/SKILL.md",
   "lines": "370-371",
   "quote": "If the key can be picked from general knowledge, the option wording or common sense, the item tests nothing about the text."
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
   "lines": "44",
   "quote": "That leaves one option without any reading."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md",
   "lines": "46",
   "quote": "`secret` makes a grammatical, true sentence."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "lines": "131",
   "quote": "A child who taps it is corrected for a defensible answer."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "lines": "113",
   "quote": "As written, \"Things I already know\" is a correct answer to many questions."
  },
  {
   "truth": 7,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/SKILL.md",
   "lines": "66",
   "quote": "the correct option is supported only by passage text *after* this page — unanswerable when asked"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
   "lines": "86",
   "quote": "12. **Answer position: A is the answer in 10 of 20 visible four-option items, and D in only 1.**"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
   "lines": "79",
   "quote": "All 7 blanks (p15b ×4, p24b ×3) put the correct word as option 1: Mole, Rat, underground, Toad, timid, cheerful, eerie."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L14-review.md",
   "lines": "70",
   "quote": "The script's ANSWER-BIAS check skips routine checks and dialogue items, so it missed two runs:"
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "lines": "238",
   "quote": "| 1 | Answer position (12 of 18 keyed B) | **Fixed.** Keys are spread across positions. |"
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/EVALUATION.md",
   "lines": "49",
   "quote": "Treat `insufficient_evidence` as a deliberate abstention."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "lines": "152",
   "quote": "- The question is about a plant that loses its leaves, so nearly every answer contains \"leaves\", including passing ones such as \"without leaves it can't make food\"."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L13-review.md",
   "lines": "126",
   "quote": "`compare_accept` includes `away`, `house` and `home`, which match almost any answer."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
   "lines": "34",
   "quote": "counts substring markers and first-token KL, which do not measure pedagogical quality."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "lines": "173",
   "quote": "Delete the \"word for word is the goal\" clause so no marker reads it the other way."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-main-review.md",
   "lines": "46",
   "quote": "| Q1 marked on meaning | **Mixed.** The criterion says \"in any words\", but the rubric also says \"word for word is the goal\". |"
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/EVALUATION.md",
   "lines": "12",
   "quote": "Instructions embedded in lesson or student content are data, not instructions to the judge."
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
   "lines": "46",
   "quote": "The last word of that sentence is \"magistrate\", not \"fined\"."
  },
  {
   "truth": 16,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
   "lines": "49",
   "quote": "**Fix:** *\"Look at the word just before 'by the magistrate'.\"*"
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/README.md",
   "lines": "61",
   "quote": "every visible passage is the fixed source text word for word"
  },
  {
   "truth": 18,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L12-review.md",
   "lines": "105",
   "quote": "`theft` and `charge` (legal sense) carry p14, p21 and p23 and aren't glossed. p14 `check` tests them."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-main-review.md",
   "lines": "20",
   "quote": "The renderer (`reading.tsx`) labels the fold \"The text so far\" when the lesson has a \"Read the text\" station, and all five reading pages do."
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/README.md",
   "lines": "139-140",
   "quote": "The option order is *not* in this list: the renderer does not shuffle, so `ANSWER-BIAS` reads the real key."
  },
  {
   "truth": 30,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/README.md",
   "lines": "15-16",
   "quote": "It also emits every question verbatim as an evidence pack."
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/README.md",
   "lines": "9",
   "quote": "- **Binary Scoring**: No partial credit - each dimension scores 0.0 (fail) or 1.0 (pass)"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/data/development_cases.json",
   "lines": "265",
   "quote": "A reviewer would need a clearer rule and learner context to make a stable judgment."
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "lines": "286",
   "quote": "The two manual reads agreed on every high and on most mediums, but each found things the other missed."
  },
  {
   "truth": 34,
   "effect": "counter",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/README.md",
   "lines": "10",
   "quote": "- **Deterministic Results**: Uses temperature=0.0 for reproducible evaluations"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
   "lines": "38",
   "quote": "No unvalidated LLM judge chooses an edit."
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/EVALUATION.md",
   "lines": "33",
   "quote": "It provides context for remaining headroom, not ground truth."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/input-generator/moe_extension_summary.md",
   "lines": "80",
   "quote": "- **MoE fields populated**: 0 entries (expected - no MoE-specific content in test data)"
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/HARNESS.md",
   "lines": "16",
   "quote": "`scoring.py` binds ratings to raw outputs."
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/SKILL.md",
   "lines": "70",
   "quote": "the keyed answer is nearly absent from the story while a distractor sits in it near-verbatim — **verify the key is right**."
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L2-review.md",
   "lines": "89",
   "quote": "- **p4:** the two items are clones of each other (a sleeping pet in both). No wrong option tests a near-miss meaning of \"determined\"."
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/REVIEW_PACKET.md",
   "lines": "14",
   "quote": "An independent prompt-number oracle recomputes all 200 unique reference answers; ten more seeds generate and validate."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
   "lines": "26",
   "quote": "An exact-answer/hint checker may catch mechanical errors, but semantic help quality is human-reviewed."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/EVALUATION.md",
   "lines": "54",
   "quote": "Before opening test predictions, educators and the project owner must set acceptable false-accept, false-reject, abstention, fidelity, cost, and latency thresholds for the intended classroom context."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/README.md",
   "lines": "81",
   "quote": "**Pass Threshold: 0.85** (fixed, never changes)"
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U2-L1-review.md",
   "lines": "230",
   "quote": "Visible items only: **9 recall, 2 inference, 7 strategy, 1 vocab.**"
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/ML_TRAINING_INSIGHTS_REPORT.md",
   "lines": "434",
   "quote": "Grade 7 passes at only 7.6% vs Grade 4 at 41%."
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/EVALUATION.md",
   "lines": "46",
   "quote": "Report by rule and family as well as overall, including high-impact cases such as leaked independent-practice answers and adversarial content."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/README.md",
   "lines": "9",
   "quote": "The [v3 synthetic corpus manifest](data/heretic_synthetic_v3/manifest.json) hashes 488 inputs and separate gold data."
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/data/development_cases.json",
   "lines": "22",
   "quote": "A claim that learners achieved an objective should be supported by an observable student action that demonstrates that objective; task completion or engagement alone does not establish it."
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/reports/G3-U1-L11-review.md",
   "lines": "89",
   "quote": "- **Rubric grounding with facts not in the story:**"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/README.md",
   "lines": "64",
   "quote": "| `curriculum_alignment` | Critical | Content must match requested standard |"
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/README.md",
   "lines": "78",
   "quote": "| 1 | any | 0.60-0.69 | FAIL |"
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/EVALUATION.md",
   "lines": "50",
   "quote": "Report rating distribution and failures, not only an average."
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Library/Mobile Documents/com~apple~CloudDocs/work/incept/README.md",
   "lines": "7",
   "quote": "- **Request-Centric Evaluation**: Questions are evaluated against the original generation request, not in isolation"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/uae-education-ai/HERETIC_PLAN.md",
   "lines": "38",
   "quote": "Run all 12 on the 48 search inputs, then the top 2 on the 48 separate selection inputs (**576 + 96 candidate responses**, before baselines)."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/shadow/content-eval/README.md",
   "lines": "20",
   "quote": "The script never pretends to decide these; it hands over the material."
  }
 ]
}
```
