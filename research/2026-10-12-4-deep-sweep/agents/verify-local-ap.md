# verify:local-ap

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "local-ap",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All quotes are verbatim at the cited lines, and 38% and 90% match. The original overstates the case. 'Can only test recall whatever the difficulty setting' rests on one model judge, and that judge's own context described fill-in as a vocabulary test while forbidding recall-only items (curriculum.py lines 335 and 351). Fill-in also passed 65.6% in Run 2, above MCQ at 60.9%, before it collapsed to 21% after a generator release. 'Single-blank' is not documented anywhere; Run 4's report proposes numbered blanks. I narrowed the statement to the defensible rule (fit the format to the objective's verb) and added Run 2's objective-level example.",
   "statement": "Match the item format to the thinking the objective asks for: a fill-in-the-blank item asks for a remembered term, so don't use it for an objective that asks learners to explain, and don't expect a harder setting to change that.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md",
     "lines": "108",
     "quote": "| \"Explain causes of the Columbian Exchange and its effects\" | Fill-in-blank for term \"Atlantic World\" | Tests vocabulary, not causation |",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "78",
     "quote": "- Tests recall regardless of difficulty setting",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN6_REPORT.md",
     "lines": "105",
     "quote": "**90% of fill-in questions fail cognitive demand.** The format is fundamentally incompatible with AP-level analytical requirements.",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "107",
     "quote": "| fill-in | 66% | 50% | **21%** | 25% | 23% | 45% | **38%** |",
     "verbatim": true
    }
   ],
   "against": "Every verdict came from one model judge. Its own context described the format as a vocabulary test ('\"fill-in\": \"Fill-in-the-blank testing key vocabulary/concepts\",', ~/Documents/APinceptbench/ap_benchmark/core/curriculum.py line 335) while also requiring '  - Questions should test historical thinking, not just factual recall' (line 351), so part of the failure was built into the rubric. The cognitive-demand rule was later relaxed ('PROMPT_VERSION = \"2026.02.24.1\"  # Relaxed cognitive demand - recall is OK', ap_benchmark/prompts/base.py line 15). In the first working run, fill-in passed more often than MCQ: '| **Fill-in** | 21 | 11 | 65.6% |' (docs/reports/BENCHMARK_RUN2_REPORT.md line 121). A course-design file whose name contains a person's name argues that the line to police is recall versus inference, not format (hs-civics/reference/peter-9-12-social-studies.md line 207).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 1,
   "verdict": "keep-with-fix",
   "reason": "All three quotes are verbatim at the cited lines, and the 38% for hard items in Run 5 matches. 'Extra explanation in the stem made items easier' was a model judge's rating with no learner data, so the because-clause now says that. The Run 3 line comes from the fill-in section, not from a finding across formats. Not a duplicate; it touches truth 3 (scaffolding that gives the answer away).",
   "statement": "Make a harder item demand more reasoning, not harder words or more context in the stem; a judge rated hard items padded with explanation in the stem as easier, not harder.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md",
     "lines": "211",
     "quote": "- Difficulty should affect cognitive demand, not just vocabulary",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "80",
     "quote": "- Difficulty adjustment only changes vocabulary complexity, not cognitive demand",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "114",
     "quote": "**Pattern:** The endpoint adds too much context/scaffolding, which paradoxically makes hard questions easier to answer.",
     "verbatim": true
    }
   ],
   "against": "The difficulty verdicts were a model judge's opinion, with no learner data, and the pattern swung between runs: '**Key observation:** Run 5 fixed easy difficulty (27% → 68%) but broke hard difficulty (58% → 38%) and cognitive demand (70% → 59%).' (~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md line 32).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 2,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim (650 items; 161–220 labels). The third original quote ('Hard questions now fail MORE than easy questions') is about quality pass rates, not about how hard items are for learners, so it does not bear on the claim. I replaced it with the Run 5 counts, where a judge rejected the writer's 'hard' label on 17 of 39 hard items. I also added the item bank's statement that every difficulty is expert-assigned with an infinite standard error. Kind changed to adopted rule, because the source records missing data, not a measurement.",
   "statement": "Treat any difficulty label, whether a writer, a judge or a person assigned it, as a guess until learners have answered the item, and recalibrate it from their responses.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md",
     "lines": "11",
     "quote": "This means we do not know how hard any individual item actually is for students.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
     "lines": "39",
     "quote": "the 161–220 figures above are authoring band labels, not measured difficulty.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
     "lines": "264",
     "quote": "The most fundamental gap: all b_provisional values are expert-assigned. SE(b̂) = ∞ pre-calibration.",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "92",
     "quote": "**24 out of 39 hard questions failed (62%)**",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "96",
     "quote": "| Difficulty Alignment | **17** |",
     "verbatim": true
    }
   ],
   "against": "Simulation suggests a well-built adaptive engine tolerates the guess: 'Simulation 3 shows the engine tolerates this at the expected σ ≈ 0.5–1.0 logits level (reliability ≥ 0.85 maintained) [SIMULATION], but precision is below what it will be post-calibration.' (05_LIMITATIONS.md line 14).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 3,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and 30.7%, 43.0%, 88.9% and 65.0% match. This duplicates truth 57 (verified facts as the writer's only source), together with 58. I kept it because it adds a measured before-and-after on the same benchmark. Fix: found_by calls the 30.7% run 'the first benchmark run', but the comprehensive report's Run 1 is a different, broken run at 0.0% (run IDs 3de8a1ae and 217a76cf). The generator received the statement and ignored it. The alignment verdicts came from a model judge.",
   "statement": "Give the writer the exact statement and objective an item must test, not just its topic, and check that the item tests that statement; a writer that ignored the statement wrote generic items about the topic, and alignment rose from 43% to 89% once it used it.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md",
     "lines": "33",
     "quote": "The generator ignores the specific `learning_objective` and `statement` provided in the request. Instead, it produces generic questions about the broad topic area.",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md",
     "lines": "25",
     "quote": "| Curriculum Alignment | 43.0% | 88.9% | **+45.9%** |",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md",
     "lines": "30",
     "quote": "The dramatic improvement in curriculum alignment (43% → 89%) confirms the endpoint is now properly utilizing the `learning_objective` and `statement` fields provided in requests.",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "123",
     "quote": "- A student who knows this fact MUST be able to answer the question correctly",
     "verbatim": true
    }
   ],
   "against": "Even with the statement, the writer still strayed beyond it: '- Scope expansion beyond provided curriculum (e.g., adding Syria/Libya when curriculum specifies Iraq/Afghanistan only)' (~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md line 60).",
   "general": true,
   "duplicate_of": "57",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and 15 of 26 (58%) matches. This duplicates truth 67 (settle in code what code can settle); I kept it for its measured case. The original because-clause ('a judge files a structural fault under whichever dimension is nearest') overstates. The main example was routed to alignment by the rubric itself (base.py lines 39 and 41), which leaves one clear misfiling: factual accuracy failed because the choices were missing. Nothing beyond that supported the advice to give each fault its own check, so I reworded the statement to what the evidence shows.",
   "statement": "Check in code that an item has the requested format and all its parts before any judge reads it; format faults that reached the judge were scored as alignment and factual-accuracy failures, which hid their real cause.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "24",
     "quote": "**15 out of 26 curriculum alignment failures (58%) are due to FORMAT MISMATCH.**",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "139-140",
     "quote": "factual_accuracy: \"Cannot verify factual accuracy because the actual answer choices are missing\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
     "lines": "245",
     "quote": "| Dim 13: Format compliance | Item structure matches format token (MCQ/MSQ/EBSR/hot-text/sequence/gap-match) | Hard gate |",
     "verbatim": true
    }
   ],
   "against": "Filing format faults under alignment is what the judge's rubric asked for, not drift: '3. Is the format correct (MCQ vs MSQ vs fill-in vs article)?' and 'If ANY of these fail, the content fails `curriculum_alignment` which is CRITICAL.' (~/Documents/APinceptbench/ap_benchmark/prompts/base.py lines 39 and 41; that file postdates the run).",
   "general": true,
   "duplicate_of": "67",
   "name_bearing_source": false
  },
  {
   "index": 5,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. DBQ 186 passed and 5 failed (97.4%), and document_authenticity 28 passed and 163 failed (85% fail); both match. The code's blocking set (document_count, prompt_structure, factual_accuracy, answer_validity; benchmark_official.py lines 196-201) leaves out the prompt's other DBQ critical dimensions. This duplicates truth 59 (no average buys back a voiding fault), generalised to every critical check and to keeping code and rubric in step; I kept it for that evidence. 'Nearly all items passed' held only for document-based items (the whole run passed 84.1%), so I made it specific.",
   "statement": "Make the code block on every check the rubric calls critical; when it blocked on only some and averaged the rest, 97% of document-based items passed while 85% failed a check the rubric called critical.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "34",
     "quote": "| DBQ      |    186 |      5 |      0 |     97.4% |      0.87 |",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "82",
     "quote": "| document_authenticity     |   28 |  163 |     14.7% |      0.15 |",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/prompts/official_ap_prompts.py",
     "lines": "315, 321-323",
     "quote": "- Does each document have proper attribution (author, date, source)?",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/benchmark_official.py",
     "lines": "214",
     "quote": "passed = not critical_failed and overall_score >= 0.70",
     "verbatim": true
    }
   ],
   "against": "The check also accepted simulated documents ('- Are documents historically accurate or properly simulated?', official_ap_prompts.py line 322), and the commonest recorded issue was missing attribution ('- (8x) Document 1 lacks specific attribution (author, date, source)', evaluation report line 63). Part of the failure rate may therefore be attribution format rather than invented sources. The pass code is read as it stands now. The 947-item run (2026-02-25 08:19) predates the repository's first commit (08:53), so the exact code that scored it can't be confirmed.",
   "general": true,
   "duplicate_of": "59",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and 26 of 37 matches. 'Easy items failed whatever they did' overstates: easy items passed 68% in Run 5, and MSQ at easy passed 92%. I reworded it to the double bind that Run 3's report names. The context file comes from the 2026-02-25 commit, after the runs, so the rules in force during Run 4 can't be confirmed; the run reports show the effect either way. Verification found a second conflict: after the relaxation, the judge's 25-case calibration set still expects recall-only questions to fail cognitive demand (ap_benchmark/calibration/gold_standard.json lines 193-194). Related to truth 45, not a duplicate.",
   "statement": "Check that a rubric's rules can all be met at once; when one rule defined easy items as recall and another failed items that only tested recall, easy items were failed both for being too simple and for being too hard.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/core/curriculum.py",
     "lines": "323",
     "quote": "\"easy\": \"Should test basic recall and comprehension of key concepts\",",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/core/curriculum.py",
     "lines": "351",
     "quote": "lines.append(\"  - Questions should test historical thinking, not just factual recall\")",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "63",
     "quote": "- Result: Questions are either too simple (cognitive fail) or too complex (difficulty fail)",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "80",
     "quote": "**26 out of 37 easy questions failed cognitive demand**",
     "verbatim": true
    }
   ],
   "against": "The conflict was resolved by relaxing the judge mid-series rather than by fixing the rule ('- Recall and memorization questions ARE ACCEPTABLE', ~/Documents/APinceptbench/ap_benchmark/prompts/base.py line 88), so runs before and after the change are not comparable.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. 520 vs 650, 52/745/56 vs 47/713, and 'exactly 3' (against 3-4 and 2-3 in sibling docs) all match. The 'hostile review ... fatal' in found_by had no citation; it is in the G5 package's red-team JSON (lines 34-35), which I added. I also added the build rule written after the count-drift attack (BUILD_FACTS.md line 18). One more instance sits inside a single report: Run 8 gives 58% (line 115) and 66.1% (line 137) for the same fill-in removal.",
   "statement": "Derive every count and structural rule from one named source and re-derive it before publishing, because the same quantity stated differently across documents was a recurring and damaging review finding.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "11",
     "quote": "| 3 | The item-bank source table summed to 520 while claiming 650 | Replaced with the verified 13-file breakdown; the fixtures were counted programmatically and sum to exactly 650 |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "111",
     "quote": "The email says 52 lessons, 745 items and 56 cold passages; the infographic says 47 lessons and 713 graded items; and the “45 instructional tests” are tests, not instruction. The course’s own materials disagree with each other.",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/EVALUATION_API.md",
     "lines": "286",
     "quote": "- ✅ `questions` - Required, must have **exactly 3** questions",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
     "lines": "18",
     "quote": "Every count in every doc must trace to one named pull with a date.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/package/RED_TEAM_FINDINGS.json",
     "lines": "34",
     "quote": "is enumerated FOUR mutually incompatible ways",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/package/RED_TEAM_FINDINGS.json",
     "lines": "35",
     "quote": "\"severity\": \"fatal\",",
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
   "reason": "Quotes are verbatim. 'Never exceeds 55%' matches the format table (R2-R7: 53, 45, 52, 55, 54, 48; R1 0%; Run 8 had no matching items). The reasons came from a model judge, but the claim also follows from arithmetic: with equal one-to-one lists, the last pair is forced. The counter (a platform's match tasks use no extra options) concerns practice tasks, not tests.",
   "statement": "Give a matching item more answers than prompts, or some other guard against elimination, because equal one-to-one lists let the last pairs be solved by elimination.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "390",
     "quote": "- 1:1 format eliminates analytical challenge",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "391",
     "quote": "- No distractors = simple elimination",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN7_REPORT.md",
     "lines": "119-120",
     "quote": "The 1:1 matching format with no distractors makes this more of a medium difficulty question despite being marked as hard",
     "verbatim": true
    }
   ],
   "against": "A shipped platform's guide prescribes the opposite for its match tasks: '- Include 4-6 objects, with no distractor items.' (~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md line 227, name-bearing). The same guide's cloze rule is '- Do include distractor words that are unused.' (line 221).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The evidence covers fill-in blanks only. I dropped 'short-answer' items, because AP short-answer parts accept many valid answers. These are a run report's recommendations after judge clarity failures (15 of 28 fill-ins in Run 4), not a tested fix. Adds to truth 6.",
   "statement": "Write each blank in a fill-in item so that only one answer fits, and say what kind and size of answer is wanted (a term, a phrase or a concept).",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "93",
     "quote": "**New clarity failures:** Fill-in blanks are ambiguous about expected answers.",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "97-98",
     "quote": "The range of acceptable answers for blank 1 creates ambiguity about the expected level of specificity",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "260",
     "quote": "1. Each blank should have ONE clear correct answer",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "261",
     "quote": "2. Specify expected granularity (term, phrase, concept)",
     "verbatim": true
    }
   ],
   "against": "The judge also penalized the obvious fix of listing accepted answers: 'Providing multiple pre-written acceptable answers reduces it to pattern matching rather than requiring critical thinking' (~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN6_REPORT.md lines 115-116). Truth 10 still applies: one answer in meaning may have several accepted wordings.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep",
   "reason": "Quotes are verbatim. The evidence is rules: a generation spec and a review team's stated standard. The counter checks out: the absolute-word regex is applied to distractors and to correct answers (rules.py lines 95-109), and any triggered rule fails the item (checker.py line 215).",
   "statement": "Make every option alike in length, grammar and qualification so that none can be chosen or ruled out by its form alone.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/AP_GENERATOR_SPEC.md",
     "lines": "29",
     "quote": "**Rules**: 4 options, 1 correct, plausible distractors, parallel structure, no absolutes",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "34",
     "quote": "Closed-response items must require the target reasoning and must not be answerable by surface cues, keyword matching, option length, or test-wise elimination.",
     "verbatim": true
    }
   ],
   "against": "A fixed word list is blunt. The benchmark's pre-judge regex fails any option containing words such as 'only', 'complete' or 'immediately' (~/Documents/APinceptbench/ap_benchmark/hard_fail/rules.py lines 30-41), while the judge's own rule allows absolutes when accurate: '5. Avoid absolute language (\"always\", \"never\", \"all\", \"none\") unless historically accurate' (official_ap_prompts.py line 34).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep",
   "reason": "Quotes are verbatim, and the statement is supported by the misconception field required on every wrong option. found_by misstates the spec, though. It reads 'Each MCQ has exactly 3 distractors, one of each:' and then lists four types (CAT_MAP_EXAM_SPEC.md lines 350-354), while the item bank's gate asks for 'Four distractor types present' (02_ITEM_BANK.md line 243). The spec contradicts itself, so 'one of each of four' can't hold for any single item. The benchmark's 'questions that passed tended to use distractors representing real misconceptions' is an observation, not a test.",
   "statement": "Build each wrong option from a named, predictable error and record which error it targets, instead of writing random plausible-but-wrong answers.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md",
     "lines": "356",
     "quote": "`options[i].misconception` field required on all non-key options.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/reference/CAT_MAP_EXAM_SPEC.md",
     "lines": "351",
     "quote": "- **Scope error** — true detail presented at wrong granularity",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "173",
     "quote": "- Distractors MUST represent plausible student misconceptions, not absurd options",
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
   "reason": "Quotes are verbatim. The evidence is adopted rules, with no measurement. I added a counter: the same contract allows 'reasonable outside knowledge' for short-answer parts, and the essay rubric rewards evidence beyond the documents, so 'target content' has to mean the content the course taught. Complements truth 5 and adds to 6.",
   "statement": "Check that every item can be answered by someone who learned the target content and needs nothing beyond it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "123",
     "quote": "- A student who knows this fact MUST be able to answer the question correctly",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "124",
     "quote": "- The question MUST NOT require knowledge outside the scope of this fact (except for scaffolding context)",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/prompts/official_ap_prompts.py",
     "lines": "239",
     "quote": "- FAIL if parts require obscure knowledge",
     "verbatim": true
    }
   ],
   "against": "The same contract loosens the rule for short-answer items: '- All parts MUST be answerable based on `curriculum_fact` + reasonable outside knowledge' (~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md line 242). The essay rubric also awards '| **Evidence (Outside)** | 0-1 | Uses specific evidence beyond the documents |' (ap_benchmark/prompts/official_ap_prompts.py line 309).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. Nothing supported the scoring-guide half, so I dropped it. The mismatch finding is 2 of 200 essay prompts in one judged run, and the one-thing rule is a single contract line, so I changed the kind to adopted rule. Not a duplicate of 56 or 69.",
   "statement": "Make each part of a question ask for one thing, and make the skill it declares match what its prompt actually asks.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
     "lines": "54",
     "quote": "- (2x) Mismatch between stated reasoning type (causation) and actual prompt structure (...",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/EVALUATION_API.md",
     "lines": "328",
     "quote": "- **NEVER** use compound verbs like \"identify AND describe\" in a single part",
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
   "reason": "Quotes are verbatim. The evidence is rules, and the counter (parts must build on each other) is a real tension inside the same project. Adds to truth 68.",
   "statement": "Keep items that share a source independent, so that no item reveals another's answer and each part can be scored on its own.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/AP_GENERATOR_SPEC.md",
     "lines": "44",
     "quote": "**Rules**: 3-4 questions, different skills, independent answers",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/prompts/official_ap_prompts.py",
     "lines": "229",
     "quote": "- Are parts logically connected but independently scorable?",
     "verbatim": true
    }
   ],
   "against": "The same project's generator contract also demands dependence: '- Parts MUST be scaffolded (build on each other OR test related aspects)' (~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md line 239).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 15,
   "verdict": "keep",
   "reason": "Quotes are verbatim. This is mostly a duplicate of truth 45 (fix the rubric before measuring), together with 37. I kept it because it adds the project's own written principle and, from verification, a contradiction between the relaxed judge and its calibration set: 7 of the 15 failing calibration cases expect a cognitive-demand failure, while the relaxed prompt accepts recall. The independence half is a stated principle with no measurement here.",
   "statement": "Judge content with a model or person independent of its maker, and change the judge only on its accuracy against labelled cases, never to move the pass rate.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/EVALUATION_PROCESS.md",
     "lines": "5",
     "quote": "It uses Claude API (not the same model as the generator) to ensure impartial evaluation.",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/EVALUATION_PROCESS.md",
     "lines": "158",
     "quote": "- Evaluator criteria should NOT be influenced by generator output",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/EVALUATION_PROCESS.md",
     "lines": "159",
     "quote": "- Changes to evaluator based on benchmark accuracy, not pass rate",
     "verbatim": true
    }
   ],
   "against": "The project broke its own rule. The judge's rubric was relaxed mid-series with no recorded accuracy check ('PROMPT_VERSION = \"2026.02.24.1\"  # Relaxed cognitive demand - recall is OK', ap_benchmark/prompts/base.py line 15). The calibration set uses a different threshold from the live 0.70 rule ('\"pass_threshold\": 0.85,', ap_benchmark/calibration/gold_standard.json line 4) and holds only 25 multiple-choice and multi-select cases. It also contradicts the relaxed rule: seven of its 15 failing cases expect a cognitive-demand failure, six of them for recall ('Recall-only question - just asks for a date without any analysis', gold_standard.json line 194), while the relaxed prompt says '- Recall and memorization questions ARE ACCEPTABLE' (base.py line 88).",
   "general": true,
   "duplicate_of": "45",
   "name_bearing_source": false
  },
  {
   "index": 16,
   "verdict": "keep",
   "reason": "Quotes are verbatim, and it is fair as an open question. Verification of the 15 failing calibration cases: 7 expect cognitive-demand failures (6 recall-only), 2 absolute language, 1 structural, 2 gross period misplacements and 3 factual errors, one of them subtle (1830 vs 1832). So 'blatant' is mostly but not wholly true. It refines truths 37 and 38 rather than duplicating them.",
   "statement": "Does a calibration set built from blatant faults show that a judge will catch the subtle faults that actually occur?",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/calibration/gold_standard.json",
     "lines": "194",
     "quote": "Recall-only question - just asks for a date without any analysis",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/ap_benchmark/calibration/gold_standard.json",
     "lines": "403",
     "quote": "Factual error: Midway was in the Pacific against Japan, not the Atlantic against Germany",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md",
     "lines": "87",
     "quote": "1. **Temporal confusion** - Misattributing events to wrong time periods",
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
   "reason": "Quotes are verbatim. I corrected 'cells of 4 to 15 items': the cells the routing rules used held 5 to 15 items (Run 3: 13; Run 4: 6 and 8; Run 5: 5, 6, 12, 13, 15). The 4-item cell appears in the comprehensive report's ranking, not in a routing rule. Matching at easy read 15% (13 items), then 0% (6 items), then 64%. Related to truths 15 and 34, not a duplicate.",
   "statement": "Don't reroute or redesign on pass rates from a handful of items, and report the count beside every rate; routing rules built on cells of 5 to 15 items flipped from run to run.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "35",
     "quote": "1. **Match + Easy = 15%** - Catastrophic failure rate",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md",
     "lines": "129",
     "quote": "- 13 easy+match questions → routed to MSQ (15% → ~78%)",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN4_REPORT.md",
     "lines": "50",
     "quote": "2. **Match + Easy = 0%** - All 6 questions failed",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "58",
     "quote": "| **Match** | 64% | 55% | 38% |",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md",
     "lines": "63",
     "quote": "2. **MCQ + Medium: 83%** (5/6) - Strong",
     "verbatim": true
    }
   ],
   "against": "The generator changed between runs, so the swings mix real change with sampling noise, and cells this small can't separate the two.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and 49.4% to 66.1% and fill-in counts of 20 to 39 match. The 66.1% recomputes one run without fill-in, so it shows the mix effect but not a case where quality stayed the same; I reworded 'moves' to 'can move'. My own arithmetic: applying Run 7's per-format rates to Run 6's mix gives about 59.5% instead of 62.9%, so roughly a quarter of the 50.0% to 62.9% 'recovery' came from fewer fill-in items. Adds to truth 49.",
   "statement": "Compare runs format by format and level by level, because a change in the mix of item types can move the overall pass rate even when no format got better or worse.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN8_REPORT.md",
     "lines": "137",
     "quote": "| Pass Rate | 49.4% | **66.1%** |",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "502",
     "quote": "| Run 6 | 39 | 26 | 28 | 23 | 116 |",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_COMPREHENSIVE_REPORT.md",
     "lines": "503",
     "quote": "| Run 7 | 20 | 33 | 34 | 29 | 116 |",
     "verbatim": true
    }
   ],
   "against": "The Run 8 report contradicts its own figure for the same removal: '   - Would be 58% pass rate without fill-in' (~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN8_REPORT.md line 115) against 66.1% at line 137; 39 of 59 is 66.1%. Run 8 also had no matching items and 39 generation errors, so its mix was not comparable to earlier runs.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep-with-fix",
   "reason": "I re-tallied the counts: 857 of 1,356 'Yes' in Unit 2 and 109 of 597 in Unit 7; 2,087 links with 160 'No'; exact notes 'already covered' 23 and 'already mentioned' 17. 'Commonest review note' holds for links, where most of the 160 rejections carry a repeat-type note. It does not hold for nodes, where placement narrowly led (see candidate 20), so I narrowed it to links. The pipeline's redundancy pass works only within the unit, yet people still flagged repeats across units ('already covered in 2.7', 'already defined in unit 8'), which supports 'whole course'.",
   "statement": "Expect knowledge drafted from several sources to overlap, and remove repeats across the whole course, not just within a unit, before human review; repeats were still the commonest reason people rejected generated links.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
     "lines": "sheet 'Instructions' (xl/worksheets/sheet1.xml), cell B2, step 14",
     "quote": "14. Run step 8 in main.py which will go through the current topic's facts and check for redundancies against previously processed topics in the unit.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 3 Relationships', rows 14 and 20, column J (Notes; Keep = 'No')",
     "quote": "already covered",
     "verbatim": true
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 3 Nodes', row 56, column M (Comment/Reason); column N reads 'Removed'",
     "quote": "already covered in 2.7, they should know this",
     "verbatim": true
    },
    {
     "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
     "lines": "sheet '4. Consolidation Audit' (xl/worksheets/sheet10.xml), row 2, column J ('Overlap Notes')",
     "quote": "Yes - Related to AMSCO_2_RP_IVxj; this adds detail to the English focus on land acquisition for agriculture.",
     "verbatim": true
    }
   ],
   "against": "Overlap varies by unit: in the UNIT 7 workbook's '4. All Consolidation Audits' sheet, 109 of 597 rows are marked Yes under 'Overlap Notes' (verified). The 857-of-1,356 Unit 2 flags are the model's own consolidation notes and mostly mark relatedness ('related to' 255 times, 'complements' 60), not duplicates.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 20,
   "verdict": "keep-with-fix",
   "reason": "Cells verified (Unit 1 row 10 'Removed'; Unit 9 rows 109-112 'Removed standard mapping'; Unit 6 row 202). I re-tallied 1,635 nodes and 160 comments. My hand coding gives about 40 placement, about 33 repeats, 20 explicit trims, about 13 wording or context and 1 evidence, so placement leads, narrowly. The exact action labels are 50 'Removed', 49 'Edited' and 14 'Added' (found_by's 49 and 48 are one short each), plus about 20 moves. Comments cluster in Units 3, 6 and 9 (44, 31 and 44), so the mix reflects a few reviewers. This duplicates truth 63 (check scope labels before judging content) applied to generated knowledge; I kept it because it adds human-review evidence.",
   "statement": "Check where each generated fact belongs (its unit, its period and the specific standard it serves), not only whether it is true; placement was the commonest comment people made on generated knowledge nodes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 1 Nodes', row 10, column M (Comment/Reason); column N reads 'Removed'",
     "quote": "Out of time frame for this course",
     "verbatim": true
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 9 Nodes', rows 109-112, column M; column N reads 'Removed standard mapping'",
     "quote": "Tricky, because these are significant events but they align with the overall learning objective rather than a specific standard",
     "verbatim": true
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 6 Nodes', row 202, column M",
     "quote": "This sentence is true but does not get to the heart of the divisions that occurred in the gilded age.",
     "verbatim": true
    }
   ],
   "against": "The tally comes from keywords in free-text comments, not from a coded field, so the categories overlap.",
   "general": true,
   "duplicate_of": "63",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep",
   "reason": "Cells verified. About 20 explicit trims ('too long', 'trimmed', 'shortened') and three 'split the previous fact into two' notes match. Two more splits exist: one fact broken into two (Unit 6) and one into four (Unit 7). Not a duplicate.",
   "statement": "Keep each knowledge statement short and about one idea, since over-long generated statements were trimmed and combined ones split during human review.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 3 Nodes', row 151, column M; column N reads 'Edited'",
     "quote": "og (too long) - In 1794, the Whiskey Rebellion occurred when western Pennsylvania farmers protested Alexander Hamilton's excise tax on whiskey;",
     "verbatim": true
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 3 Nodes', rows 152, 155 and 157, column M",
     "quote": "manual add - split the previous fact into two",
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
   "verdict": "keep-with-fix",
   "reason": "Cells verified. The original's 'related facts were often given the wrong kind of link' overstates. Reading all 160 rejection notes, about 20 concern the link's kind, direction or claim; the rest are repeats or blank. Per-type rates confirmed: 6 of 143 for 'causes', and 76 of 835 for 'exemplifies' with labels case-folded (833 counting lowercase labels only). I narrowed the statement accordingly and added a direction example.",
   "statement": "When content links two facts, check that the stated kind and direction of the link hold, not only that the facts are related; people rejected generated links for a wrong kind or direction of link, though repeats were the commoner reason.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 3 Relationships', row 74, column J (type 'enables', Keep 'No')",
     "quote": "The description is an over simplification of the two statements. Locke's ideas didn't necessarily enable the ideological shift--rather it inspired and gave language to republican principles of self governances.",
     "verbatim": true
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 7 Relationships', row 130, column J (type 'enables', Keep 'No')",
     "quote": "instead of \"enabled\" i think the term is \"included\"",
     "verbatim": true
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 5 Relationships', row 41, column J (type 'influences', Keep 'No')",
     "quote": "more the other way around",
     "verbatim": true
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 1 Relationships', row 134, column J (type 'exemplifies', Keep 'No')",
     "quote": "the trade networks don't exemplify how they adapted to their environments.",
     "verbatim": true
    }
   ],
   "against": "Most generated links were kept: 160 of 2,087 were marked 'No', and only about 20 of those notes concern the link's kind, direction or claim. The per-type rejection rates (4.2% for 'causes' to 9.1% for 'exemplifies') are driven mostly by repeats.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 23,
   "verdict": "keep",
   "reason": "I re-tallied: 1,163 agree and 370 differ (24%); 222 moved from essential to supporting and 139 the other way, plus 7 'both' moved to essential. Column D matches the Classification column of the generator's '7. Node Metadata Output' sheet, so it is the model's label; columns K-N are the human columns. There is no baseline of two people agreeing, so 24% measures disagreement, not model error. Not a duplicate (related to truth 44).",
   "statement": "Check a model's labels of which facts are essential against human judgment before they decide what is taught or tested, since they differed on about a quarter of facts, mostly by over-rating.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 1 Nodes', row 1, column D (generator label)",
     "quote": "Classification",
     "verbatim": true
    },
    {
     "path": "~/Downloads/AP US History - Knowledge Schema - SME Tracker.xlsx",
     "lines": "sheet 'Unit 1 Nodes', row 1, column L (human-set level)",
     "quote": "Essential/Supporting/Nuanced detail",
     "verbatim": true
    }
   ],
   "against": "Nothing records whether the human level was set before or after the person saw the model's label, so the agreement figure may be inflated.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep",
   "reason": "Quotes are verbatim. All 32 items written during the outage were replaced, and the red-team flag is at RED_TEAM_FINDINGS.md line 37. Not a duplicate of 28 or 36.",
   "statement": "Treat content produced while a check was out of service as never checked, and replace or re-check all of it before use.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
     "lines": "313",
     "quote": "The 32 G2 match/sequence items authored during the June-2026 quality-check service outage passed through no trustworthy gate.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md",
     "lines": "77",
     "quote": "The G2 match/sequence items originally authored during the June-2026 quality-check outage were **replaced 2026-07-07** with items quality-scored 1.0 by the healthy-period checker (engine PRs #64/#65; swap table in the engine repo).",
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
   "reason": "Quotes are verbatim. 0.930 vs 0.928 against the ≥0.93 target, and RMSE 4.12 against the <4.0 target, both match. Not a duplicate.",
   "statement": "Report every result as measured, misses included, in every summary: never round a near miss up to a pass or leave the failing metric out.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "9",
     "quote": "| 1 | Summary tables reported reliability as \"0.930 ✅\" against a ≥0.93 benchmark the underlying reports state as 0.928, below |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "10",
     "quote": "| 2 | The one failing metric (RMSE 4.12 vs <4.0 target) was omitted from every summary table |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
     "lines": "28",
     "quote": "Verdicts are **PASS-with-named-gaps**, never bare PASS.",
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
   "reason": "Quotes are verbatim. 630 items, r=0.948, rel=0.928 and RMSE 4.12 match. The production re-run's +2.62 bias and RMSE of 4.73 are at 05_LIMITATIONS.md lines 26 and 134. That bias was in the running estimate, not in the score the engine reports. Related to truths 24 and 46, but it adds the scope of the bank and of the learner population.",
   "statement": "Validate on the production path with the full bank and the full range of learners the claim covers, because a simplified run hid a bias and an error regression.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "12",
     "quote": "| 4 | Simulations were G3-scoped (630 items, G3 prior, simplified selector) but described as \"G2–G5, production code\" |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md",
     "lines": "134",
     "quote": "The initial-run results (r=0.948, rel=0.928, RMSE=4.12 RIT) could not expose production-path effects",
     "verbatim": true
    }
   ],
   "against": "Even the full simulation is not field evidence: 'If the Rasch model is misspecified, all simulation results — including the r=0.967 theta recovery and rel=0.931 reliability — overestimate actual field performance.' (05_LIMITATIONS.md line 97).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 27,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and 206.4 at the 72nd percentile, 196.0 at the 46th, and n=915 match. I dropped the second clause (an 83% baseline 'inflated' by easy items). Its source says the claim is 'only half-supported until re-measured on hard items', so the inflation was never measured, and the quoted line relays a file whose path contains a person's name.",
   "statement": "Take a baseline from the full current population, one record per learner, not from a convenient slice; one slice put a population at the 72nd percentile when the full population sat at the 46th.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "26",
     "quote": "| 1 | Population baseline (206.4 / 72nd pctile) is a biased slice |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_CASE_FOR_APPROVAL.md",
     "lines": "40",
     "quote": "n = 915, mean RIT 196.0, mean percentile 46.3",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_CASE_FOR_APPROVAL.md",
     "lines": "40",
     "quote": "The old figure was not an arithmetic slip but a compound of three biases we have now quantified",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. 'Code paths don't drift' is the source's slogan, not a finding, and code has its own faults: the benchmark scores a missing result as a pass (benchmark_official.py line 208). I replaced it with the drift that was actually observed. Related to truth 67, not a duplicate.",
   "statement": "Block in code any score or claim that has not been validated yet, rather than relying on disclaimers; one package's documents drifted (0.930 against 0.928) while its engine simply did not emit the unvalidated score.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
     "lines": "37",
     "quote": "Pre-pilot output is logit ± SE and domain sub-scores; RIT, percentile, and CGP are **blocked in the engine**. Documents can drift; code paths don't.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
     "lines": "39",
     "quote": "The two audits found number-drift in our *documents* (0.930 vs 0.928) — which is exactly why the load-bearing claim gate lives in code.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
     "lines": "229",
     "quote": "| Approximate RIT output (200 + 10θ) pre-linking | The transformation's coefficients are exactly what the linking study estimates; emitting the approximation would be the overclaim the design exists to prevent |",
     "verbatim": true
    },
    {
     "path": "~/Projects/incept-package-hub/docs/COURSE_PACKAGE_STANDARD.md",
     "lines": "203",
     "quote": "- generated UI cannot invent a stronger status than the manifest.",
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
   "reason": "Quotes are verbatim. It is a documentation practice adopted in three packages. Not a duplicate.",
   "statement": "Tag every claim about content with the kind of evidence behind it (measured, simulated, decided, derived or asserted), and state what each count does not prove.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
     "lines": "256",
     "quote": "- The ≥0.85 threshold is an authoring decision, not an empirically validated cutoff [AUTHORING-DECISION].",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/docs/FULL-COURSE-AUTHORING-STATUS.md",
     "lines": "15",
     "quote": "| Measure | Complete local inventory | What the count does not prove |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
     "lines": "31",
     "quote": "7-tag evidence provenance ([Direct-pull]/[Asserted]/[Open]/[AUTHORING-DECISION]/[DERIVED]/[ACADEMIC]/[SIMULATION] as applicable), prove/not-prove pairing.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim (~40 students, N=40, ≥90%, 30-60 minutes, <10%). The source says adaptive selection rarely serves the extreme items, not that ordinary use misses learners in general, so I tied the recruiting rule to that condition.",
   "statement": "Make only the claims a sample's size can support and set pilot success criteria that size can measure; when ordinary use rarely reaches the extremes, recruit learners at both ends on purpose.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/README.md",
     "lines": "122",
     "quote": "| Feasibility pilot | ~40 students (1–2 classes) | Usability, engagement, and early item red flags — no calibration claims at this size |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md",
     "lines": "196",
     "quote": "**Success/kill criteria (usage-based — all meaningful at N=40):** session completion ≥ 90%; session duration within the expected 30–60-minute envelope; rapid-guess rate < 10%.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "28",
     "quote": "| 3 | Natural CAT exposure under-samples tail items for calibration |",
     "verbatim": true
    }
   ],
   "against": "Eight learners per extreme is not tail validation: 'is directionally right and statistically decorative; fine for feasibility, but don't let it be read as tail validation.' (~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md line 59).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 31,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. Counterbalancing alone doesn't stop half the learners practising before the official test; it only measures the effect, which the plan reports as a study output (validity plan line 81). I corrected the statement to say so. found_by's 'redesigned with counterbalanced order' is disputed: the package's response says the order design (section 2.3) already existed, and that the additions were a criterion-integrity note and an optional arm given only after the official test.",
   "statement": "When validating a new measure against an established test, don't let it act as practice for that test: give it only after the official test, or counterbalance the order and report the practice effect on the official score.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md",
     "lines": "21",
     "quote": "rehearsal administered days before the real test is a **practice/familiarization intervention on the criterion measure**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md",
     "lines": "81",
     "quote": "Group B (MAP-first, ~50% of the cohort) provides a linking estimate with zero prior proxy exposure by construction.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md",
     "lines": "81",
     "quote": "a **post-MAP-only administration arm** is available: the proxy administered only after the official sitting.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/04_CONCURRENT_VALIDITY_PLAN.md",
     "lines": "65",
     "quote": "All students take both tests (within 2 weeks). Order is counterbalanced to control for practice effects and fatigue:",
     "verbatim": true
    }
   ],
   "against": "Accounts differ on whether the order design was new. The package's response says the red team's 'not addressed anywhere' claim was a factual error: 'three of its load-bearing findings rest on factual errors — a counterbalancing design it says doesn't exist' (~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_RESPONSE.md line 5).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 32,
   "verdict": "keep",
   "reason": "Quotes are verbatim. The reference test's 25% rapid-guess rule and the mastery stamp earned at about 20% accuracy both check out. Not a duplicate of truth 12.",
   "statement": "Record how long learners take on each item and flag rushed answers, because a disengaged attempt is not evidence of what they know.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
     "lines": "87",
     "quote": "The proxy captures per-item timing silently and flags rushing — so a disengaged student is coached before the official window, and a proxy score carries its own validity flag rather than silent noise.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "97",
     "quote": "Re-engineer the gate to block advancement on genuine misses, require reading or attention, and penalise rapid-guessing, then demonstrate it blocking a real miss in a live walkthrough.",
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
   "reason": "Quotes are verbatim. The original's unconditional rule conflicts with exam rehearsal, where the real exam is timed (the counter), so I qualified it. 'Rewards rapid guessing' is the source's claim about one test, and 'triples the accuracy penalty' has no citation in the audit row, so I kept neither in the statement.",
   "statement": "Don't put a clock on a test unless speed, or the timing of the exam it rehearses, is part of what it measures; on an untimed power test a clock changes what is measured.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
     "lines": "232",
     "quote": "| Timed sections | MAP is an untimed power test; a clock changes the construct and rewards the rapid-guessing MAP penalizes |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "46",
     "quote": "Comprehension is untimed; speed is a different construct; time-pressure triples the on-screen accuracy penalty.",
     "verbatim": true
    }
   ],
   "against": "When the real exam is timed, a readiness test may be timed to mirror it: '- Add a timer for the mock exam (to mirror AP-exams) and resolve the multi-part FRQ issue for AP-assessments.' (~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md line 27, name-bearing).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 34,
   "verdict": "keep",
   "reason": "Quote is verbatim. It is one package's position, citing the testing standards, and that package's own audit bounded it to three formats. A second package runs a non-gating practice lane for format exposure (incept-package-hub g8-reading case-for-review.md lines 48-49). The counter stands.",
   "statement": "Let learners practise the formats and interactions of the test that counts before it counts, because meeting an interface for the first time on the scored test adds noise to the score.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
     "lines": "55",
     "quote": "Alpha students practice on 100% MCQ material; their first multi-select or two-part evidence item is on the scored official MAP. Interface novelty is construct-irrelevant variance (AERA/APA/NCME Standard 1.13).",
     "verbatim": true
    }
   ],
   "against": "The benefit was later bounded: '| 11 | Format-familiarization benefit implied for all six formats | **Bounded** — one-line scope added: strongest for the 3 Reading-2–5-confirmed formats; the other 3 are low-harm additional practice |' (validity/00_AUDITS_AND_FIXES.md line 36). A red team noted that 'if familiarity moves scores at all, it moves the official ones.' (red-team/RED_TEAM_FINDINGS.md line 21).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 35,
   "verdict": "keep",
   "reason": "Quotes are verbatim. 29.4% overlap, 120 candidates and 182 sources match. Adds to truth 48.",
   "statement": "Keep test items out of practice and behind access control, and track how often a learner meets the same item again, because items seen before make a test a weaker measure.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
     "lines": "18",
     "quote": "| 10 | The public no-login test URL allows anonymous farming of the item bank |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md",
     "lines": "118",
     "quote": "- Item security is weaker: students who take the test multiple times will see repeated items (mean pairwise between-session overlap 29.4%)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/review/history/2026-07-27-review-preparation-projections.md",
     "lines": "17-18",
     "quote": "All 120 assessment candidates and 182 assessment/retry-only sources remain out of the learner projection.",
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
   "reason": "Quotes are verbatim. It is a design rule in one authored course that has not yet been run with learners. Not a duplicate of truths 4 or 48.",
   "statement": "After a wrong answer, teach the failed step and retry on a parallel item that uses different evidence, rather than repeating the same item.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/assessment-set.json",
     "lines": "26",
     "quote": "Score atomically, record the first failed historical function, teach through its resolved local check, and administer its parallel retry with different evidence before reassessment.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/incept-acceptance.json",
     "lines": "37",
     "quote": "Unit 1 exposes targeted feedback, correction, and different-evidence retry.",
     "verbatim": true
    }
   ],
   "against": "One platform reuses the same item in instruction and review and accepts the cue risk: 'This is a medium-to-low-priority concern, in part because courses typically have a large deck of questions in rotation.' (~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md line 195, name-bearing).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 37,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim. The reviewers' complaint was that independent work 'switches to a different skill'. The spec's fix keeps the skill and changes the material, so I added 'same skill'. found_by's 'then' implies the spec answered that review, but they concern different courses. Adds to truths 40 and 3.",
   "statement": "Release independent practice only after the worked model is hidden, and set it on the same skill but on material that neither the model nor the guided practice used.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
     "lines": "127",
     "quote": "Release only after the worked model and its completed analysis are removed.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
     "lines": "128",
     "quote": "The model uses a cross-period timeline and the guided task uses an imperial comparison; independent work shifts to a regional matrix that has not been modeled.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "26",
     "quote": "The I-do/we-do/you-do routine is misapplied: I-do reveals the answer instead of modeling thought; we-do is only a hint; you-do sometimes switches to a different skill.",
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
   "reason": "Quotes are verbatim. There are two independent sources: a course review, and a team position reached after five adversarial rounds. Adds to truths 48 and 18.",
   "statement": "Let taught knowledge recur and build across lessons and in-lesson checks, and keep unseen material for tests and transfer items, because the same overlap is teaching in one place and a leak in the other.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "45",
     "quote": "***To change this:*** Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only, where that property belongs.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "43",
     "quote": "by design ensures assessment passages never overlap taught topics so a student “can’t pass on recall.”",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "66",
     "quote": "Whether dose-item overlap is teaching or leaking depends on item class — the same overlap is legitimate in an in-lesson knowledge check and a leak in a comprehension/transfer item",
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
   "reason": "Quotes are verbatim. 39–48%, 12.5%, and 18 results from at most one real student all match. Not a duplicate.",
   "statement": "Report how many learners actually used and finished the material beside any accuracy figure, because accuracy measured only on finishers, or reach measured by distribution, hides non-use.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "72",
     "quote": "the 39–48% sub-skill numbers are measured only on students who *did* complete items, so the 12.5% completion floor is a worse problem than the skill gap.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_CASE_FOR_APPROVAL.md",
     "lines": "152",
     "quote": "an instrument that was distributed in the platform and produced no actionable output went unused (18 results, at most one real student).",
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
   "reason": "Quote is verbatim. It is a single rule borrowed from a practice framework, adopted rather than measured. Not a duplicate.",
   "statement": "If correcting a wrong answer needs more teaching than the lesson gave, fix the item or where it sits rather than lengthening the feedback.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "52",
     "quote": "If the feedback needed to correct a response is longer and more complex than the original instruction, the ITEM has crossed the acquisition boundary — fix the item or the placement, not the feedback.",
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
   "reason": "Quotes are verbatim. Both sources are files whose names contain a person's name, and I found no other source. Adds to truth 60.",
   "statement": "When many learners fail at the same point, treat it as a fault in the instruction and fix it there, keeping remediation for individual slips.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "291",
     "quote": "If many learners frequently fail at the same point in a course, the instruction itself has failed, not the learner.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/peter-9-12-social-studies.md",
     "lines": "154",
     "quote": "- Quality assurance for the course itself (if students can't pass, the course didn't work)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 42,
   "verdict": "keep",
   "reason": "Quote is verbatim. It is a reviewer finding recorded as a rule. A platform guide whose filename contains a person's name adds the same check ('No pre-supposed knowledge', [name]-alphatok-guide.md line 94). Adds to truths 40 and 20.",
   "statement": "Teach every new step before it appears inside a worked example, and check that no lesson leans on an idea not yet taught.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "54",
     "quote": "Worked examples assemble the known — a novel step must be taught before it appears inside one.",
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
   "reason": "Quote is verbatim. It is a review team's stated rule. The statement leaves out the source's 'performance' element but is otherwise faithful. Not a duplicate.",
   "statement": "Give every activity a stated rationale: the knowledge it targets, the failure it guards against, why this activity, and when its scaffold comes off.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "36",
     "quote": "Any activity needs a rationale: target knowledge type, performance, failure mode it protects against, why this activity, and scaffold retirement condition.",
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
   "reason": "Quote is verbatim, and the course is indeed the incumbent (03-other-teams-and-alpharead.md line 25). The quoted rule is relayed from a knowledge-base file whose filename contains a person's name (heading at line 42), so I flagged it name-bearing; I found no other source. Adds to truths 18 and 2.",
   "statement": "Give each key term one wording and use it verbatim wherever it appears: explanation, check, summary and review.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/03-other-teams-and-alpharead.md",
     "lines": "43",
     "quote": "every key term has ONE wording, propagated verbatim across the video, the CFU, the knowledge organiser, and the FSRS card",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 45,
   "verdict": "keep",
   "reason": "Quotes are verbatim. It is a course review's finding (no poetry or drama, short of the course's own 40/40/20 target). The team's reading canon says the same: 'Text difficulty is a match, not a single readability number' (01-brainlift-doctrine-and-our-spovs.md line 109). Not a duplicate.",
   "statement": "Choose texts for the knowledge sequence, genre balance and quality the course needs, not by a readability score alone.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "51",
     "quote": "Lexile alone also mishandles poetry and narrative and cannot tell you whether a text is worth reading.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "53",
     "quote": "***To change this:*** Choose texts for a coherent knowledge sequence and a genre balance that includes poetry, drama and more literary work, and judge complexity qualitatively as well as by Lexile.",
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
   "reason": "Quotes are verbatim, and 58–217 words matches. It is a review's judgment, not a measurement. Not a duplicate.",
   "statement": "Build practice up to the length and load of the target performance, because mastering only short pieces does not prepare learners for sustained work.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "69",
     "quote": "A child can master the whole course one short snippet at a time and never once sustain attention across a multi-passage block.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "71",
     "quote": "***To change this:*** Add longer passages and paired-text sets that build toward test-length and real-world reading.",
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
   "reason": "Quotes are verbatim. I dropped 'never for time spent' from the statement because the user's own projects disagree on it: one awards 0 XP for time, another one XP per focused minute; the conflict stays in against. I added the package's non-negotiable 'XP only for verified learning'. Adds to truths 48 and 51.",
   "statement": "Award mastery or points only for verified learning, never for navigation, reading or revealing answers.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/incept-acceptance.json",
     "lines": "55",
     "quote": "\"name\": \"XP only for verified learning\",",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/incept-acceptance.json",
     "lines": "57",
     "quote": "Candidate items, time, reading, voice, reviewer navigation, and answer reveal award 0 XP; production XP integration is not implemented.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "95",
     "quote": "In a hands-on walkthrough one of us earned a stamp on “The Amazing Axolotl” at about 20 percent accuracy by clicking through without reading, then advanced with the passage hidden from view.",
     "verbatim": true
    }
   ],
   "against": "Another release ties points to focused time at a successful finish: 'Preview XP is calculated once at a successful lesson finish from whole focused minutes at one XP per minute' (~/Projects/grade3-reading/artifacts/wiki-research/hub-review-model.md lines 329-330).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 48,
   "verdict": "keep",
   "reason": "Quotes are verbatim. It is adopted in one package, and the counter stands. Adds to truth 3.",
   "statement": "Build the learner-facing version as a separate projection that leaves out keys, rationales, rubrics, correction routes and test material, rather than hiding them in the page.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/case-for-review.md",
     "lines": "12-13",
     "quote": "Student projections omit assessment candidates, answer keys, rationales, rubrics, feedback, teacher-only supports, and correction routes.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/incept-acceptance.json",
     "lines": "81",
     "quote": "Unit 1 withholds independent and checkpoint evidence, excludes keys from student HTML, requires correction before retest, caps candidate attempts, and never unlocks on reviewer action.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/assessment-set.json",
     "lines": "18",
     "quote": "Withhold keys, rationales, lesson models, correction routes, and retries until the relevant response is submitted.",
     "verbatim": true
    }
   ],
   "against": "One platform stores the key in a fixed position and relies on delivery to hide it: 'where 'A' is always the correct answer since options are shuffled at delivery time.' (~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md line 197, name-bearing).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 49,
   "verdict": "keep",
   "reason": "Quotes are verbatim, and the eight defects match. This duplicates truth 47 (play every lesson as a learner first). I kept it for the evidence that element-existence checks passed while the experience failed, and for the requirement to test at each screen size.",
   "statement": "Test the learner's whole path at each screen size, because checks that prove page elements exist don't prove a learner can see, hear, answer, recover and finish.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/hub-review-model.md",
     "lines": "325-326",
     "quote": "the checks proved that elements existed, but did not prove that a learner could see, understand, hear, correct, complete, and resume the released experience.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/wiki-research/hub-review-model.md",
     "lines": "337",
     "quote": "all run \"at mobile and desktop viewports.\"",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "47",
   "name_bearing_source": false
  },
  {
   "index": 50,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and 137, 161 and 192 match. The original's source for the 192 items (BUILD_FACTS line 24) doesn't say the decoy is announced to screen readers; the executed-actions checklist does, so I swapped it in. Announcing an unused bucket gives away part of the answer, not the whole answer, so I reworded that. Adds to truth 27.",
   "statement": "Treat accessibility as part of validity: an item a learner can't operate, or whose screen-reader reading gives away part of the answer, yields an invalid score.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RED_TEAM_FINDINGS.md",
     "lines": "41",
     "quote": "an inaccessible item isn't just bad UX, it's an invalid score.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
     "lines": "103",
     "quote": "An item type that cannot be made accessible is also not a faithful rehearsal of the test.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/package/G5_EXECUTED_ACTIONS_CHECKLIST.md",
     "lines": "39",
     "quote": "192/198 match items announce a `__decoy_unused` \"Unused category\" target to screen readers",
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
   "reason": "Quotes are verbatim. This duplicates truth 11 (keep the words; no model grade), combined with truth 67 (settle in code the half that can be checked). I kept it because two separate packages adopted the split.",
   "statement": "When a written answer can't yet be marked reliably, check in code the part that can be checked (such as the cited evidence) and record the rest without grading it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
     "lines": "35",
     "quote": "\"attempting\"-gameable written step (F4 must log justification as attention evidence, machine-check the citation half)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/start-here.md",
     "lines": "19",
     "quote": "deterministic checking is limited to candidate MCQ choices; constructed historical reasoning remains ungraded until a trusted rubric grader and human escalation path are approved.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "11",
   "name_bearing_source": false
  },
  {
   "index": 52,
   "verdict": "drop",
   "reason": "Quotes are verbatim, but the claim overstates them. The test sends dummy values and checks the response's echo of the request, which proves the fields arrived and came back, not that the writer used them in what it wrote. Nothing shows the test would have caught the original failure, where the generator received the fields and ignored them. The real check, that the item tests the given statement, is truths 57 and 58.",
   "statement": "Prove a writer actually uses its inputs by sending marked dummy values and checking they come back unchanged.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "376",
     "quote": "To verify generator compliance, send this test request:",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "409",
     "quote": "If any field is missing, renamed, or has a different value, the generator is **non-compliant**.",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/GENERATOR_API_SPEC.md",
     "lines": "41",
     "quote": "MUST be echoed back unchanged. MUST NOT be transformed or auto-generated.",
     "verbatim": true
    }
   ],
   "against": "The checked field is the response's 'request' echo (GENERATOR_API_SPEC.md lines 393-407), not the generated content.",
   "general": false,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 53,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim, and 99.1% and 43.0% match and come from the same run. The original generalised from that one run, so I made the because-clause specific. Related to truth 58.",
   "statement": "Judge generated content on whether it hits its target at the right depth, not on polish; in one run 99% of generated items passed clarity while 43% matched their objective.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md",
     "lines": "103",
     "quote": "### 1. Clarity (99.1% pass rate) ✅",
     "verbatim": true
    },
    {
     "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_FAILURE_REPORT.md",
     "lines": "134",
     "quote": "### 7. Curriculum Alignment (43.0% pass rate) ❌❌",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
     "lines": "61",
     "quote": "A model's pedagogical knowledge does not survive the trip into its generated content",
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
   "reason": "Quotes are verbatim, and the workbook does pull released exam questions into its fact sources. The reasoning that the outline sets scope while released material shows what is valued comes only from guides whose filenames contain a person's name. Not a duplicate.",
   "statement": "Anchor content and items to the target exam's released questions and scoring guides as well as to its content outline, because the outline says what is in scope while the released material shows what is valued.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
     "lines": "sheet 'Instructions' (xl/worksheets/sheet1.xml), cell B2, step 5",
     "quote": "- Run \"Get Exam Question Inputs\" in the Functions Menu to get the scraped high-alignment MCQs and FRQs from AP Classroom in the \"Exam\" sheet.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "57",
     "quote": "The CED tells you what's in scope; the released materials and rubrics tell you what's actually valued and tested.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-ap-brainlift.md",
     "lines": "217",
     "quote": "- All questions must match CED examples in:",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 55,
   "verdict": "keep-with-fix",
   "reason": "Quotes are verbatim (24 items across ~24 standards; 30, 24 and 28 items). The original's 'a length where the pass mark is a whole number of allowed errors' misreads the arithmetic, since every length allows a whole number of errors. I restated it as the guide's actual point. Single guide, name-bearing, with no other source.",
   "statement": "Design a mastery test to separate learners by breadth, one item per standard across many standards, with items a learner who has mastered the material passes nearly every time; and check the error budget each form length gives at the pass mark (at 90%, 30 items allow three errors, 28 still only two).",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-bespoke-mastery-assessments.md",
     "lines": "52",
     "quote": "Discrimination between mastered and non-mastered students is delivered by breadth of coverage (24 items spanning ~24 standards), not by individually tricky items.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-bespoke-mastery-assessments.md",
     "lines": "39",
     "quote": "Given assessments are short, you will likely want to enforce a one-item-per-standard sampling rule.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-bespoke-mastery-assessments.md",
     "lines": "33",
     "quote": "- At a 90% pass threshold, a 30 item form would be more reliable than a 24 item form, but a 28 item form would not be.",
     "verbatim": true
    }
   ],
   "against": "A high fixed bar can be out of reach: 'only ~17% of cohort clears 90% today, so a flat wall has no on-ramp.' (~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md line 47).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 56,
   "verdict": "keep-with-fix",
   "reason": "Quote is verbatim (~17%). 'Gave most of them no path forward' asserts an outcome, but the source records a design decision justified by the 17% figure, so I reworded it.",
   "statement": "Stage a high mastery bar so learners have a way up to it; when only about one learner in six cleared a flat 90% bar, the course moved to staged gates.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
     "lines": "47",
     "quote": "Three difficulty bands (not five stages); staged 90% gates (not flat-90%) — only ~17% of cohort clears 90% today, so a flat wall has no on-ramp.",
     "verbatim": true
    }
   ],
   "against": "Elsewhere the bar is fixed for all courses: 'This is likely hard-coded school-wide at 90% mastery.' (~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-bespoke-mastery-assessments.md line 46, name-bearing).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 57,
   "verdict": "keep",
   "reason": "Quote is verbatim. It is one guide's efficiency claim, the guide's filename contains a person's name, and I found no other source. Not a duplicate.",
   "statement": "When most test items must be written from scratch, fix the test blueprint's slots first and then write items to fill them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-bespoke-mastery-assessments.md",
     "lines": "57",
     "quote": "When most items will be authored from scratch — as is true here — it is vastly more efficient to invert that order: do the sampling first, then author to meet the planned form and bank needs.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 58,
   "verdict": "keep",
   "reason": "Quotes are verbatim. This duplicates truth 61 (don't build on unchecked outputs), generalised to every costly stage. I kept it because the knowledge pipeline generates relationships only after approval and removes repeats before review (step 14), evidence from a file with no person's name. The cost claims come from a guide whose filename contains a person's name.",
   "statement": "Review each stage's output before the next, more expensive stage is built on it: knowledge units before scripts, scripts before media, and approved facts before the links between them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
     "lines": "sheet 'Instructions' (xl/worksheets/sheet1.xml), cell B2, step 20",
     "quote": "20. Run step 11 in main.py which is to generate relationships. This will be the very last step after the KS for the unit has been approved.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "89",
     "quote": "The cost of fixing a problem rises sharply once the video has been generated from the script.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "63",
     "quote": "KC errors propagate through every downstream stage, so this is the cheapest place to catch them.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "61",
   "name_bearing_source": true
  },
  {
   "index": 59,
   "verdict": "keep",
   "reason": "Quotes are verbatim. It is one guide's calibration step, the guide's filename contains a person's name, and I found no other source. Not a duplicate of truth 47.",
   "statement": "Before running a whole production pipeline, tune it on a spread of cases that includes every type and the hardest one.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "103",
     "quote": "- Include the script you think is hardest to generate.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
     "lines": "184",
     "quote": "Each course will need to go through a calibration process where around 10 diverse scripts from the course are used to adjust the prompts in the pipeline as needed.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 60,
   "verdict": "keep",
   "reason": "Quote is verbatim. It is a rule from a course-design template whose filename contains a person's name, and it is untested here. Not a duplicate of truth 62, though both warn that naming a wrong idea can plant it.",
   "statement": "Confront the misconceptions learners bring on their own with a direct contrast, but don't raise misconceptions that only poor teaching creates; teach precisely enough to prevent them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-how-to-write-a-course-brainlift.md",
     "lines": "31",
     "quote": "instinctive misconceptions (intuitive — students arrive with them or generate them naturally) require contrastive treatment in the script; misconceptions caused by poor instruction (artefacts of how the topic is typically taught) should not be surfaced in the script — the script just needs to be precise enough to prevent them.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 61,
   "verdict": "keep-with-fix",
   "reason": "The statement holds and the quotes are verbatim, but the cited source is garbled. The guide names 'Spacing Effects in Learning (Kornell & Bjork, 2008)' with DOI 10.1111/j.1467-9280.2008.02209.x. From memory, not checked online, that title and DOI belong to Cepeda, Vul, Rohrer, Wixted & Pashler (2008), a study of spacing intervals. The finding that interleaving feels harder belongs to Kornell & Bjork's 2008 category-learning paper (DOI 10.1111/j.1467-9280.2008.02127.x). Fix the citation before recording it. I swapped the DOI line for the guide's two insight lines as evidence. The guide's filename contains a person's name. Adds to truth 51.",
   "statement": "Space practice over time and interleave topics, even though learners find it harder than blocked practice.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-ap-brainlift.md",
     "lines": "507",
     "quote": "- Traditional AP courses often rely on massed practice (cramming), but spaced practice with increasing intervals leads to significantly better long-term retention and application",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-ap-brainlift.md",
     "lines": "508",
     "quote": "- Interleaving topics rather than blocking them feels harder to students but produces stronger learning and better transfer of knowledge",
     "verbatim": true
    }
   ],
   "against": "The guide's citation (line 495-496: 'Spacing Effects in Learning (Kornell & Bjork, 2008)' with DOI 10.1111/j.1467-9280.2008.02209.x) mixes two papers, so the external-research basis needs a correct citation before it is recorded.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": true
  },
  {
   "index": 62,
   "verdict": "keep",
   "reason": "Quotes are verbatim. The spec keys four corrective lines to four named errors (lesson-01.json lines 141-144), and the review faulted one generic message for every wrong answer. Adds a dimension to truth 1: feedback specific to the error, not only a pointer instead of the answer.",
   "statement": "Key corrective feedback to the specific error the learner made, telling them what to look at, rather than giving one generic message for every wrong answer.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
     "lines": "142",
     "quote": "Replace then with a mechanism such as supplied labor, structured diplomacy, or constrained settlement.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
     "lines": "91",
     "quote": "Ask what the earlier condition made possible, costly, contested, or more likely.",
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
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
   "lines": "250",
   "quote": "- Feedback Incorrect: One sentence shown to the student when they answer incorrectly (~15–25 words). Should state the correct answer as concisely as possible. No judgment — just the answer.",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
   "lines": "15",
   "quote": "a wrong answer returns only “Good try, let’s look again,” with no explanation and no correct answer shown.",
   "ok": true
  },
  {
   "truth": 1,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
   "lines": "91",
   "quote": "Ask what the earlier condition made possible, costly, contested, or more likely.",
   "ok": true
  },
  {
   "truth": 2,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/02-current-brainlift-spov-audit.md",
   "lines": "50",
   "quote": "Hedged language is not politeness, it is load: 'might', 'maybe', 'a little' are excluded because they add processing cost without information.",
   "ok": true
  },
  {
   "truth": 3,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
   "lines": "26",
   "quote": "I-do reveals the answer instead of modeling thought",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
   "lines": "248",
   "quote": "If the model selects the correct answer in ≥3/5 trials, the item fails — it is answerable from background knowledge alone, not from careful reading of the specific passage.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/incept-package-hub/course-packages/courses/g8-reading/review/evidence/case-for-review.md",
   "lines": "55-56",
   "quote": "The redesign defeats the G8 POC's 98.6%-leak failure.",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/g5_analysis_digest.md",
   "lines": "41",
   "quote": "the 120 L.5 vocab seeds LEAK 99.2% and must be re-authored + re-certified, never deployed as-is",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
   "lines": "254",
   "quote": "- Text-dependence ablation uses a language model, which may have different knowledge than a typical G3–G5 student. Items that fail for LLMs may be valid for students (false positives) or vice versa.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
   "lines": "241",
   "quote": "| Dim 9: Answer key defensibility | Correct answer is uniquely defensible from text | Hard gate |",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
   "lines": "47",
   "quote": "79% of correct answers sat at option position A",
   "ok": true
  },
  {
   "truth": 9,
   "effect": "counter",
   "path": "~/Documents/APinceptbench/ap_benchmark/prompts/base.py",
   "lines": "28",
   "quote": "**When in doubt, FAIL the question. Missing problems is worse than over-flagging.**",
   "ok": true
  },
  {
   "truth": 15,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
   "lines": "296",
   "quote": "One failure is almost certainly forgetting. Three consecutive failures almost certainly indicate an encoding problem.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
   "lines": "246",
   "quote": "| Dim 14: EBSR Part B verbatim | Part B options are verbatim passage sentences (EBSR only) | Hard gate |",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
   "lines": "185",
   "quote": "- Video validation: There is a video validation portal where a human watches newly generated videos and either accepts them or requests a re-generation. This should be done by a subject expert so that any inaccuracies in instruction are picked up.",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
   "lines": "36",
   "quote": "(1) Maps, even stylistic and approximate maps are poor",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/lesson-01.json",
   "lines": "35",
   "quote": "If source reading, discussion, accessibility support, or correction needs more time, split the lesson rather than compressing the required evidence work.",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/BUILD_FACTS.md",
   "lines": "16",
   "quote": "Use the render-truth manifest as the ONE source",
   "ok": true
  },
  {
   "truth": 27,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
   "lines": "28",
   "quote": "The reviewers identify this as a WCAG 2.1 AA contrast failure and unusable by all students.",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_BRAINLIFT.md",
   "lines": "91",
   "quote": "The discipline: any claim that would embarrass us if checked *was* checked, by an agent instructed to break it.",
   "ok": false
  },
  {
   "truth": 34,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/test_server.py",
   "lines": "208",
   "quote": "return matches >= total * 0.8  # Allow 20% variance due to LLM",
   "ok": true
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/05_LIMITATIONS.md",
   "lines": "61",
   "quote": "The v4 consistency result (r=0.918, LoA [−10.0, +10.0] RIT) is an engine consistency check — explicitly not MAP agreement evidence.",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/benchmark_official.py",
   "lines": "208",
   "quote": "score = dim_data.get(\"score\", 1.0) if isinstance(dim_data, dict) else dim_data",
   "ok": true
  },
  {
   "truth": 36,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/incept-acceptance.json",
   "lines": "37",
   "quote": "Eleven of 28 checks are visibly marked as uncertified fallback routes pending authored replacement.",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/ap_benchmark/calibration/gold_standard.json",
   "lines": "4",
   "quote": "\"pass_threshold\": 0.85,",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
   "lines": "33",
   "quote": "| LEQ      |    200 |      0 |      0 |    100.0% |      1.00 |",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
   "lines": "100",
   "quote": "| prompt_arguability        |  391 |    0 |    100.0% |      1.00 |",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
   "lines": "97",
   "quote": "then demonstrate it blocking a real miss in a live walkthrough.",
   "ok": true
  },
  {
   "truth": 40,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/start-here.md",
   "lines": "13",
   "quote": "- seven progressively revealed phases: retrieval, teaching dose, model, guided response, independent response, feedback and different-evidence retry, and checkpoint;",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/00_AUDITS_AND_FIXES.md",
   "lines": "34",
   "quote": "**Relabeled** — now \"internal cross-bank consistency (synthetic),\" explicitly not MAP agreement",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/incept-package-hub/docs/COURSE_PACKAGE_STANDARD.md",
   "lines": "237",
   "quote": "Warnings remain visible. Human-review requirements do not disappear when the release envelope passes.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/docs/FULL-COURSE-AUTHORING-STATUS.md",
   "lines": "49",
   "quote": "Automated structural, route, source-link, and mutation checks do not substitute for these gates.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/wiki-research/hub-review-model.md",
   "lines": "213-214",
   "quote": "Never describe mechanical validation as human review, certification, runtime verification, or release authorization.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/validity/02_ITEM_BANK.md",
   "lines": "307",
   "quote": "This instrument's item quality is established **empirically, not editorially** — and that is a design position, not an omission:",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/ap_benchmark/prompts/base.py",
   "lines": "15",
   "quote": "PROMPT_VERSION = \"2026.02.24.1\"  # Relaxed cognitive demand - recall is OK",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/ap_benchmark/core/scorer.py",
   "lines": "19",
   "quote": "Pass threshold: 0.85 (fixed, never changes)",
   "ok": true
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/benchmark_official.py",
   "lines": "214",
   "quote": "passed = not critical_failed and overall_score >= 0.70",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/incept-package-hub/docs/COURSE_PACKAGE_STANDARD.md",
   "lines": "156",
   "quote": "Copying an application's stylesheet, rebuilding its shell, or describing an artifact as an approximation never satisfies the presentation declaration, even when the Hub can preserve those bytes exactly.",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/team-direction-2026-09-09/research/01-brainlift-doctrine-and-our-spovs.md",
   "lines": "35",
   "quote": "Acquisition mastery and durable mastery are different. A same-day lesson gate proves at most 'I can do it now,' not 'I can still do it later under changed conditions.'",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/review/evidence/case-for-review.md",
   "lines": "10",
   "quote": "The nine assessment sets preserve held-out source use, function-level scoring, correction routes,",
   "ok": true
  },
  {
   "truth": 49,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/edullm-review-hub/course-packages/courses/apush/source/sealed-authoring/authoring/apush/canonical/unit2/assessment-set.json",
   "lines": "67",
   "quote": "Report performance by item and historical function. Do not convert this local sample into an AP score prediction.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
   "lines": "sheet '4. Consolidation Audit' (xl/worksheets/sheet10.xml), row 2, column F ('Sources')",
   "quote": "AMSCO, Princeton, Exam",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-ap-brainlift.md",
   "lines": "592",
   "quote": "- Student preference often conflicts with effective practice",
   "ok": true
  },
  {
   "truth": 53,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/hs-civics/reference/[name]-alphatok-guide.md",
   "lines": "191",
   "quote": "- The trade-off shifts for older students, where the cognitive load of reading along may outweigh the benefit, unless they are in a noisy environment or watching on mute (common on mobile).",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/evaluation_20260225_081919_0909a798.md",
   "lines": "67",
   "quote": "- (3x) Some documents appear to be simulated rather than authentic historical sources",
   "ok": true
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN2_REPORT.md",
   "lines": "60",
   "quote": "- Scope expansion beyond provided curriculum (e.g., adding Syria/Libya when curriculum specifies Iraq/Afghanistan only)",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN6_REPORT.md",
   "lines": "14-15",
   "quote": "| Avg Score | 0.795 | 0.801 | +0.006 |",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN3_REPORT.md",
   "lines": "15",
   "quote": "| Avg Score | 0.644 | 0.826 | 0.827 | → stable |",
   "ok": true
  },
  {
   "truth": 60,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/ti-courseplans/courses/map-proxy-assessment/red-team/RECHECK_FINDINGS.md",
   "lines": "7",
   "quote": "the fix wave introduced a handful of new inconsistencies.",
   "ok": true
  },
  {
   "truth": 61,
   "effect": "supports",
   "path": "~/Downloads/Knowledge Schema Generator - AP USH Unit 2.xlsx",
   "lines": "sheet 'Instructions' (xl/worksheets/sheet1.xml), cell B2, step 20",
   "quote": "20. Run step 11 in main.py which is to generate relationships. This will be the very last step after the KS for the unit has been approved.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/artifacts/g5_build_2026_07_02/feedback_clean.md",
   "lines": "85",
   "quote": "at least one item is mistagged (a vocabulary item labelled Inference and Evidence), which weakens the claim of full standards alignment.",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Downloads/unit-1-apush-benchmark.jsonl",
   "lines": "1",
   "quote": "{\"grade\":\"1\",\"subject\":\"apush\",\"type\":\"dbq\",\"difficulty\":\"easy\",\"quantity\":1,",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/EVALUATION_PROCESS.md",
   "lines": "127",
   "quote": "Hard fails trigger BEFORE the API call, saving time and money.",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Documents/APinceptbench/docs/reports/BENCHMARK_RUN5_REPORT.md",
   "lines": "32",
   "quote": "**Key observation:** Run 5 fixed easy difficulty (27% → 68%) but broke hard difficulty (58% → 38%) and cognitive demand (70% → 59%).",
   "ok": true
  }
 ]
}
```
