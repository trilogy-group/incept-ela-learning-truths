# verify:kb-reviews-evaluation

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "kb-reviews-evaluation (candidate indices are 0-based, in list order; every quote re-checked against the file, line numbers corrected where the quote sat elsewhere)",
 "verified": [
  {
   "index": 0,
   "verdict": "keep-with-fix",
   "reason": "All quotes verbatim at the cited lines; 39 checks, 5 weeks, 7-10 a week match. The clause about counting repeat classes had no cited line, so kb-0201 line 50 is added. Distinct from 38 and complementary to candidate 19.",
   "statement": "Close a defect by adding a standing check for its whole class that asserts what the student experiences, and count new versus repeat defect classes in every round; patching single instances lets the same class recur or silently revert.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "18",
     "quote": "39 checks were added in 5 weeks (7-10 a week), yet the glow/scroll defect class was",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "43",
     "quote": "**A finding closes when its CLASS has an executable experience invariant**, not when the specific item",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "50",
     "quote": "**Every round report counts NEW defect classes vs REPEAT classes.**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "102",
     "quote": "silently reverted an earlier phonetic fix",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The original said failures become invisible to 'every other check'; the source says invisible to every check built around word matching. Narrowed, and lines 32-33 added.",
   "statement": "Every rule that fails safe by going quiet (for example, missing media plays as silence) needs its own detector; otherwise its failures stay invisible to the checks built to catch other faults.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "31",
     "quote": "A safety rule without a matching detector is a permanent blind spot.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "32-33",
     "quote": "made missing audio literally invisible to every check built around \"does the words match,\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
     "lines": "457-458",
     "quote": "Every rule that degrades to quiet needs a detector",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The source covers a check and a fix that share one mental model; 'the same author as the content' was not in the evidence, so it is removed. Added line 30 (the instrument that worked had a different model). This adds independence of the instrument to 43, which is about a reference that does not assume the answer.",
   "statement": "A check built on the same mental model as the fix it verifies, or on the same enumeration as other checks, shares their blind spots; verify with an instrument built on a different model of the problem.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "28",
     "quote": "**The check and the fix shared one author and one mental model**, so they shared a blind spot.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "30",
     "quote": "simply had a DIFFERENT model of the problem than the one that wrote the original fix.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
     "lines": "1215",
     "quote": "If a clip class is invisible to one, assume it is invisible to all.",
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
   "reason": "Both quotes verbatim at the cited lines. In both cases the defects sat just outside a check's stated scope. The fix was a law that covers every referenced clip in any field, plus a phone/tablet lens.",
   "statement": "Defects pile up where a check's scope stops: write each check's scope down and add a simple check that covers every reference.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0189-validators-and-laws.qmd",
     "lines": "59-60",
     "quote": "Every wrong-voice report we have logged came from exactly that excluded set.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0216-codex-visual-audit-2026-09-07.qmd",
     "lines": "44-45",
     "quote": "the content-check battery is desktop-only, so all three classes were invisible to it",
     "verbatim": true
    }
   ],
   "against": "Phone and tablet findings were later ranked secondary to the laptop student view (kb-0207, laptop-student-first memory, lines 1501-1524).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 4,
   "verdict": "keep",
   "reason": "Quote verbatim; 1466/1466 matches. Lines 100-102 state the reason: a targeted verifier reads one slice of the contract. This is distinct from 70 (isolate a change) because it is about running the whole suite after any fix.",
   "statement": "After any targeted fix, rerun every check, not just the one aimed at the fix; a fix that satisfies its own verifier can break another rule on the same field.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0185-quality-discipline-rules.qmd",
     "lines": "97-98",
     "quote": "a speaker-label fix passed every targeted check — machine re-listen, walkers, a 1466/1466 live battery — and still turned `npm run check` red on main",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The numbers match: 9 of 12, 6/65 = 9% alongside 8-15%, and 20 of 124 rows. 'A large share' overstated the evidence, since two of the three sources show 9-16% and only the L4 audit shows a majority refuted. The findings came from audit agents and an automated benchmark, so the statement now says review or audit findings.",
   "statement": "Check every review or audit finding against the current material before fixing anything; some are false and some are already fixed, and in one audit most serious findings were refuted.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "9",
     "quote": "9 of 12 serious findings were refuted with evidence",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "100-101",
     "quote": "audit false-positive rate **6/65 = 9%**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "101",
     "quote": "independently matching the arc-audit lane's measured 8-15%",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
     "lines": "1550",
     "quote": "20 rows already FIXED-ON-BRANCH",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 6,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 4 of 5 matches, and 25% matches 31 of 123 (line 85, added). The method 'on items known to be correct' was not in the evidence, so it is reworded. This adds a heuristic to 37/38: a high alarm rate is itself evidence against the check.",
   "statement": "When a check raises many alarms, suspect the check before the content and confirm the flags are real before treating them as defects; a check that fires at random is itself broken.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "141-142",
     "quote": "the probe is often the bug (4 of 5 listen findings that day were probe-classes, not real defects)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "85",
     "quote": "an onset-audibility check flagged 31 of 123 clips \"WEAK ATTACK,\" all false",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "87-88",
     "quote": "an onset detector firing on 25% of clips at random was itself evidence the check, not the audio, was broken",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 7,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The source says the 'stuck at ~28%' story was 'largely' a measurement artifact of four harness bugs (MCQ_SET 0→0.77, DBQ 0.55→1.0); 11 phantom FAILs matches. Added the AP insight line that states the rule. Statement unchanged.",
   "statement": "Before trusting any score, confirm the measurement harness: the scorer is live, reads the right field, runs on the right host and does not truncate output.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "40",
     "quote": "(wrong field read, grader on wrong host, MCQ_SET mis-route 0→0.77, DBQ truncation",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "62-63",
     "quote": "a scorer-less dev server produced 11 phantom FAILs because nobody preflighted that the scoring API had credentials",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "80",
     "quote": "Prove the gate measures what it claims before trusting any verdict.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (120 spans; 5 of 6 checks). The inherited-checker half restates 38, and kb-0187's remedy is a red-first fixture harness, which contradicts 'a pass on test fixtures does not show the check works'. Reframed around kb-0165's distinct point that proof on fixtures and application to the real items are different claims.",
   "statement": "A check proven on test fixtures has not been shown to work on the real items: run it on every real item and record the result, and treat an inherited checker that has only ever passed as unproven.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0165-eppc-g3-reviewer-qualification-terminal-outcomes-human-next-gate.qmd",
     "lines": "81",
     "quote": "predicate to all 120 final private spans. Those are different claims.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0187-skill-catalogue-and-workflows-index.qmd",
     "lines": "53-54",
     "quote": "where 5 of 6 checks were silently broken behind a green run.",
     "verbatim": true
    }
   ],
   "against": "kb-0187 lines 51-52 prescribe positive and near-miss-negative fixtures as the proof for inherited checks, so fixtures are necessary even though they are not sufficient.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 9,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The evidence covers a stronger solver and source changes, but not a generator change, so 'the generator' is removed. Distinct from 42.",
   "statement": "Re-check items whenever the solver or the content changes; an earlier certification or model verdict goes stale.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "53",
     "quote": "stale solver results are not certification",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
     "lines": "24",
     "quote": "the historical model snapshots are withdrawn after source changes",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 10,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. An unqualified 'never loosen the check' conflicts with candidates 6 and 66, where the check itself was wrong and was fixed, so the rule is qualified to a sound check.",
   "statement": "When content fails a sound check, fix the content rather than loosening the check; record existing violations as debt that can only shrink, and fail any new violation.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "37",
     "quote": "never weaken the rule",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0189-validators-and-laws.qmd",
     "lines": "72",
     "quote": "entry (matches nothing) also FAILS — the list can only shrink.",
     "verbatim": true
    }
   ],
   "against": "kb-0229 lines 76-80: an anti-copy gate was itself wrong and its strings were reworded; see candidate 66.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 11,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; the kb-0173 quote sits on line 94. 'Its reason, its source' had no support in the cited lines, so it is removed. The 'law without a check' line is about workspace laws, but it generalizes.",
   "statement": "Record each content rule's scope and how it is checked (code; a model judge, advisory until calibrated; the live student surface; or a person); a rule nothing checks is only a reminder.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0189-validators-and-laws.qmd",
     "lines": "96-97",
     "quote": "A law without a check is not a law here — it is a memory.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0173-edullm-standards-centralization-plan.qmd",
     "lines": "94",
     "quote": "2. semantic LLM judge, advisory until calibrated;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "109",
     "quote": "recommended a consistent `SCOPE:` line on its own",
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
   "verdict": "keep-with-fix",
   "reason": "All quotes verbatim. The original kb-0185 line-25 quote names a group of people, so role-free quotes from lines 24-29 are used. 'Harm to a learner' narrowed the source's bar, which also counts embarrassment. The rule governs an unsupervised improve-loop, so the statement is scoped to that, and each clause now has its own line.",
   "statement": "In a repeated review loop, act only on findings that show harm, not preference; treat earlier decisions as settled unless new evidence arrives; hold changes of direction for one joint decision; and pause the loop after a round with nothing critical.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0185-quality-discipline-rules.qmd",
     "lines": "24-25",
     "quote": "a finding must prove harm, not preference",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0185-quality-discipline-rules.qmd",
     "lines": "26-27",
     "quote": "recorded decisions (prior rulings, prior rounds' deferred/POLISH lists, any fix a prior round already made) are immutable inside the loop",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0185-quality-discipline-rules.qmd",
     "lines": "29",
     "quote": "a round that produces zero CRITICALs pauses the loop",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
     "lines": "70",
     "quote": "recency/confidence/citation-count do not supersede an earlier academic decision.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
     "lines": "72-73",
     "quote": "**change of direction or conflict** (HOLD — side-by-side, one consolidated decision",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0224-g3-dialogue-branches-pace-gate-roll-forward-2026-09-22-23.qmd",
     "lines": "85",
     "quote": "downgrade to NOTE unless it actively harms the child",
     "verbatim": true
    }
   ],
   "against": "Two reviews genuinely conflicted, so holding to an earlier decision needed an explicit ruling (kb-0218 lines 74-75).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 13,
   "verdict": "keep-with-fix",
   "reason": "The kb-0210 quote sits at lines 120-121, not 121-122. Added the authority line (114-115) that makes the design document the build spec. 'Line by line' appears in no source, so it is removed. The 'defects fell monotonically' figure is a self-report over three consecutive lessons and is confounded with learning, so it is weak.",
   "statement": "Treat the lesson's own design document as its build spec: write the spec from it before authoring, then audit the built lesson against it and against the whole programme, not just the passages.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0210-aladdin-2508-feedback-and-pr27-safety-snapshots.qmd",
     "lines": "114-115",
     "quote": "the build spec for a lesson is its own per-lesson **design doc**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0210-aladdin-2508-feedback-and-pr27-safety-snapshots.qmd",
     "lines": "120-121",
     "quote": "L4 as authored/reviewed/deployed was missing three components the design doc mandated",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0187-skill-catalogue-and-workflows-index.qmd",
     "lines": "62",
     "quote": "proven L5→L6→L7 (defects fell monotonically; L7 shipped zero content-validator defects).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
     "lines": "87",
     "quote": "but not yet at the programme level",
     "verbatim": true
    }
   ],
   "against": "kb-0218 lines 87-89 call the programme-level gap an open scope question, not a defect.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 14,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; the kb-0185 fragment is on line 120. The cited kb-0072 fragment stopped before 'INCOHERENCE' and did not state the remedy, so it is replaced with lines 102-103. 'Are where errors come from' generalized from one day in which all 5 errors were inherited figures, so the statement now says what was measured. Overlaps 24 only loosely.",
   "statement": "Work out every figure in a report from the primary source at writing time, and keep one canonical numbers block that other documents point to; in one day's documents every error was a figure copied from an intermediate source and no derived figure was wrong.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0185-quality-discipline-rules.qmd",
     "lines": "118-119",
     "quote": "**Every number or scope claim is derived from the primary artifact at writing time, never copied from an intermediate report**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0185-quality-discipline-rules.qmd",
     "lines": "120",
     "quote": "every single one was a figure inherited from an intermediate",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "102-103",
     "quote": "one canonical numbers block per course; all other docs POINT to it",
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
   "reason": "Quotes verbatim. The AP gate table at kb-0171 lines 38-48 (100% authored, every other gate 0%) matches the gates listed in the statement. Distinct from 9 and 59.",
   "statement": "Report each readiness gate separately (authoring, human review, rights, accessibility, item certification, live delivery) and say exactly what each proof covers; never average gates, and missing evidence means 'not evaluable', never a pass.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0171-apush-full-course-local-authoring-review-hub-archive.qmd",
     "lines": "50",
     "quote": "Do not average the independent readiness gates into a fake single quality score.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0173-edullm-standards-centralization-plan.qmd",
     "lines": "99-100",
     "quote": "`NOT_EVALUABLE` with named missing inputs and blocks any rejection-grade completion claim.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0210-aladdin-2508-feedback-and-pr27-safety-snapshots.qmd",
     "lines": "142-143",
     "quote": "this release proves only the Part-1 (L4) vertical slice",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; the three rings are at kb-0093 lines 46-50. 'Says nothing about the others' overstated the evidence and is reworded. This adds a claim-integrity layer to 44 and 46.",
   "statement": "Keep three layers of checking separate: the content files, what the student actually experiences at runtime, and the claims made about the course; passing one does not show the others pass.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "52",
     "quote": "InceptBench should not overclaim runtime behavior or package truth.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "118",
     "quote": "document-integrity floor only, never a course-quality/child-readiness/outcome verdict.",
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
   "reason": "Quotes verbatim. The original statement used a job role and is rewritten. Added the role-separation line (kb-0165 line 119); the section heading above it names a person, but the path and the quotes do not. Distinct from 37, which is about labelled cases for a judged check.",
   "statement": "Qualify anyone whose judgments will serve as a standard, human or model, on a fresh blind test (familiarity is not qualification), and keep reviewing, adjudicating and signing off separate, so no one certifies their own work.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0165-eppc-g3-reviewer-qualification-terminal-outcomes-human-next-gate.qmd",
     "lines": "113-114",
     "quote": "Familiarity with the project is not automatic qualification; the new blind result must demonstrate competence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0165-eppc-g3-reviewer-qualification-terminal-outcomes-human-next-gate.qmd",
     "lines": "119",
     "quote": "a third qualified human adjudicates, and a fourth human signs",
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
   "name_bearing_source": false
  },
  {
   "index": 18,
   "verdict": "keep",
   "reason": "Quote verbatim (lines 25-27). The source defines the student for one Grade 5 course, but the population list generalizes. It adds to 46/47 who the playthroughs must stand for.",
   "statement": "For review purposes, 'student' means a real learner in the real delivery flow: below-level readers, language learners, keyboard and screen-reader users, frustrated and test-wise students, and those who click through or guess.",
   "kind": "adopted rule",
   "evidence": [
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
   "name_bearing_source": false
  },
  {
   "index": 19,
   "verdict": "keep",
   "reason": "Both quotes verbatim. Complements candidate 0: search the whole set for the class, then guard the class.",
   "statement": "When one instance of a defect turns up, search the whole set and the sibling lessons for the same pattern before calling it a one-off.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "28",
     "quote": "census ALL colon-openers in the grade JSON rather than assuming a one-off",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0223-g3-review-rounds-and-tooling-2026-09-18-to-21.qmd",
     "lines": "37",
     "quote": "Class sweep (PARALLEL-LEAD / connective-tell rule) run over every grade",
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
   "reason": "Quotes verbatim: 3,003 strings scanned, 0 live contradictions after triaging 95 raw hits. The scan found nothing new, so its value is as a guard. Human review did find such contradictions: the 'two strongest' miscount and a 'three parts' vs 'two parts' card (kb-0238 lines 68-69).",
   "statement": "Scan all student-facing text for internal contradictions: counts that don't match, one term with two meanings, instructions that don't fit the interaction, and references to things not on the page.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "65-66",
     "quote": "regex-hunting for number-word/countable-noun mismatches, same-term double-meanings, instruction/interaction-type mismatches, off-page references",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0223-g3-review-rounds-and-tooling-2026-09-18-to-21.qmd",
     "lines": "52",
     "quote": "L6 p14 I-do state[9] contradicted its own write-up",
     "verbatim": true
    }
   ],
   "against": "The scan found 0 live contradictions after triage, so its value was as a guard rather than a finder.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 21,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The fixed-sample and separate-bank clauses had no cited line, so AP lines 60-62 are added (100 preregistered records per family; the served bank kept in a separate lane). The contract is frozen design: no raw run had been executed (kb-0170 lines 64-65). Adds to 65/66.",
   "statement": "Measure a generator's raw quality as one attempt per pre-registered input, with no retries, reranking, repair, caching, best-of-N or human picking, at a fixed sample size; report results from a curated bank separately.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "59",
     "quote": "one attempt, no retry, reranking, repair, cache substitution, rejection sampling, best-of-N, or",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "60-61",
     "quote": "Raw acceptance is fixed at 100 preregistered records per family, with no early success or denominator top-up.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "61-62",
     "quote": "Served-bank and cache/runtime evidence stays in a separate lane.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "34",
     "quote": "The headline **\"99%\" was cache + best-of-N**",
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
   "reason": "Quote verbatim (line 27). The AP multiple-choice 'fix' removed the stimulus so the leak probe was skipped. kb-0064 lines 49-50 state the general proxy-gaming warning.",
   "statement": "Watch for fixes that pass a check by avoiding it, such as removing the source text so a leak probe is skipped; that is gaming the grader, not improving the item.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "27",
     "quote": "the grader's leak-probe is skipped. That's **grader-gaming**, not a provenance win.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. Added the AP insight line saying why the quality grader misses leaks. The found_by figure of 5,860 'structure' failures includes 1,557 rows failed only for being outside the course's standards (kb-0068 lines 110-113), so it slightly overstates and is not used.",
   "statement": "Know what each evaluator measures; a general quality grader can give answer-leaking items top marks, so run leak, format and structure checks separately.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "47",
     "quote": "separate from InceptBench, which graded answer-leaking items 1.0",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "68-69",
     "quote": "InceptBench grades *instructional* quality, **not** test-security — so it won't catch a leaky-stimulus gap; anti-leak must be enforced upstream.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd",
     "lines": "195",
     "quote": "Independent passage-blind review is still required; IB+Opus passing is not enough.",
     "verbatim": true
    }
   ],
   "against": "Passage-blind re-checks of items that passed both graders were once ruled redundant (kb-0071, a name-bearing path, not cited).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 24,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Producer' is reworded so the statement names no role. Adds to 17 and 43.",
   "statement": "Never accept pass labels or measured fields that arrive with content (certification, length, reading level, verbatim spans); recompute them on arrival.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "96",
     "quote": "`word_count`/Lexile and a 30-char substring \"verbatim\" check (defeated by paraphrase).",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "51",
     "quote": "trust the recompute, not the annotation",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd",
     "lines": "231",
     "quote": "Embedded `certification: pass/pass` is not enough.",
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
   "verdict": "keep-with-fix",
   "reason": "kb-0170 line 78 verbatim; 143,026 gross, 49,571 unique and 0 certified match (lines 73-75, added). The kb-0068 figure (one question text reused 1,475 times) equals that file's EBSR pass-row count, so it is most likely a shared template stem, not duplicate items. It is replaced with the AP split evidence (606 lineage groups, zero collisions; contamination rejected), which supports the 'split' clause.",
   "statement": "Count a content bank by unique, eligible and independently certified items, not gross rows, and split evaluation sets so related items never land on both sides.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "73-75",
     "quote": "143,026 gross APUSH rows; - 49,571 sampling-eligible exact unique candidate bodies; - 0 independently certified rows; and",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "78",
     "quote": "The 100,000 unique/usable-sample claim is therefore rejected.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "78-79",
     "quote": "The deterministic split has 606 indivisible lineage-connected groups and zero cross-stratum collisions.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "139",
     "quote": "reject train/dev/audit contamination",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 113/299 matches (lines 160-161). Added lines for the discard claim and an AP line saying the generated APUSH candidates bypass no gate. 'Producer's' is reworded. Distinct from 39.",
   "statement": "Plan generation for heavy discards and keep the full trace of accepted and rejected outputs; the quality comes from the gates, not from trusting the generator.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "26",
     "quote": "The questions were good because the generator was not trusted.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "36",
     "quote": "- discarding large volumes of plausible-looking output.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "161",
     "quote": "| Grade 5 blind-certified | 113/299 |",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd",
     "lines": "33",
     "quote": "accepted_and_rejected_generation_trace",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "88-89",
     "quote": "None bypasses source identity, current-format, factuality, answerability, independence, or human review gates.",
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
   "reason": "Quotes verbatim: 60/140, 67/140 and 136/140, with 0/20, 0/20 and 17/20 robust clusters, out of 420/420 rows. The names are model products, not people. Distinct from 70.",
   "statement": "Qualify each generator model and version against your teaching rules separately; one model following the rules does not mean another will.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd",
     "lines": "50",
     "quote": "OpenAI 60/140 and 0/20 robust clusters, Claude 67/140 and 0/20, DeepSeek 136/140 and 17/20",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
     "lines": "46",
     "quote": "every model/version requires conformance qualification",
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
   "reason": "Quote verbatim (18 models). The study measured instruction difficulty, not rulebook length. The 'few rules' remedy is the entry's own labelled 'architectural inference' (lines 75-76), and the prototype that would test it never ran (kb-0168 table: NOT RUN). Rewritten so the untested part is marked as untested.",
   "statement": "Writer models follow constraints less reliably as instructions get harder; giving the writer only the rules that apply to the task, not the whole rulebook, is a plausible remedy that is still untested.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
     "lines": "73-74",
     "quote": "across 18 models, constraint adherence fell materially as instruction difficulty increased",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
     "lines": "75-76",
     "quote": "compile a small active contract rather than prompt with the full rule base",
     "verbatim": true
    }
   ],
   "against": "The same study found targeted training improved adherence (kb-0128 line 74); the entry rates success at thousands-rule scale at 40-50%, a personal estimate (lines 103-104).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 29,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (8 of 12). 'A judge's failure mode is confident wrongness' generalized one screenshot judge to all judges, so it is reworded. Added kb-0190 line 63, which requires human labels before a judge acts alone (Jev is a model). This adds a blocking rule to 37.",
   "statement": "Don't let a model-judged check block content until its precision has been measured on known cases; a judge can be confidently wrong, which is worse for a gate than an honest 'cannot tell'.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
     "lines": "132",
     "quote": "was wired as a blocker and held back 8 of 12 lessons on a question the judge was never shown the",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
     "lines": "77",
     "quote": "incompleteness**, which is worse for an automated gate than an honest \"cannot tell.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0190-jev-skills-and-engine-lane.qmd",
     "lines": "63",
     "quote": "against human labels before a gate is allowed to act alone on a Jev verdict.",
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
   "reason": "The kb-0190 quote sits at lines 70-71, not 71-72; kb-0208 is verbatim (five choices). Distinct from 31.",
   "statement": "When a judge chooses among candidates, 'none of these' must be a valid answer; forcing a pick returns the least-bad option.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0190-jev-skills-and-engine-lane.qmd",
     "lines": "70-71",
     "quote": "`noMatch` is a real, valid answer — a search with no good hit should return zero results, not the least-bad one.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
     "lines": "1313-1314",
     "quote": "five choices with no no-match outcome, which were forcing the closest wrong answer",
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
   "verdict": "keep-with-fix",
   "reason": "The kb-0196 quote is on line 122; line 121 ends 'Three defects fixed: bank'. kb-0238 is verbatim.",
   "statement": "Run on each item type only the checks written for it; a check built for one format produces spurious findings on another.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
     "lines": "122",
     "quote": "types are not interchangeable (MCQ-style questions asked of cloze/hot-text items produced",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "90",
     "quote": "check written only for L4's syllable-breakdown pattern wrongly applied to L5/L6/L7's simpler vocab",
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
   "reason": "Quotes verbatim. The cited line 428 is about beating simple baselines, which the statement does not claim. It is replaced with the feature-extraction and anchor lines (44, 46) and kb-0164 lines 97-98 (method, population, provenance). arXiv:2512.18880 is confirmed at kb-0163 lines 293 and 481; 'r ≈ 0.4–0.6' is at line 41.",
   "statement": "Treat any difficulty estimate made before an item is used as a provisional prior that records its method and how many responses it rests on, and replace it with live data; models misjudge difficulty because they cannot unknow answers, so prefer item-feature models or comparison with calibrated anchor items over a model's direct rating.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "43",
     "quote": "scaling up model capability does not improve difficulty alignment with human learners — it often makes it worse",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "49",
     "quote": "Every pre-use difficulty value must travel with a provenance label (\"pre-use predicted, N=0\") and an uncertainty indicator",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "44",
     "quote": "**SPOV 3: Feature extraction is the unsexy workhorse that consistently wins**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "46",
     "quote": "**SPOV 4: Comparative judgment with anchors is underrated and should be your first move when you have even a small calibrated bank**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "97-98",
     "quote": "predicted difficulty is a prior with method, population, provenance, and uncertainty; live data must eventually replace it;",
     "verbatim": true
    }
   ],
   "against": "Simulated students tuned to item response theory are promising but not yet reliable as a primary signal (kb-0163 line 75).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 33,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim; the ~12% RMSE reduction matches (Sarkar et al. 2025, AIED, kb-0163 lines 451 and 500, no DOI). The source is about difficulty estimates only; 'a model's judgment' went beyond it, so the statement is narrowed. Related to 34/35.",
   "statement": "Check that a model's difficulty estimate holds when the item is reworded without changing what it tests; if small wording changes swing it, distrust it.",
   "kind": "external research",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "65",
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
   "index": 34,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; the kb-0198 quote starts after a person's name on line 29 and excludes it. The ruling is about fiction ('Authentic fiction only'), and original informational passages written to spec passed review, so the statement is scoped to fiction.",
   "statement": "Prefer authentic literary texts, split into parts, over model-written fiction, and label machine-written passages honestly.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0198-meetings-decisions-timeline-0819-1001.qmd",
     "lines": "29-30",
     "quote": "LLM-generated fiction \"is never going to be great\"; real, split-into-parts texts are the priority",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "45",
     "quote": "don't relabel machine-authored cold passages as \"real.\"",
     "verbatim": true
    }
   ],
   "against": "Original passages written to spec passed review with a verdict of 'GREAT' (kb-0120 line 24).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 35,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; 417 = 1,152 minus 735 (line 141). The source says 'often', not 'usually'. Added line 172 for the second clause. This adds a procedure to 5 and 6.",
   "statement": "Before a blind test, confirm the item can be answered with the text; failing with the text often means ambiguity or a broad key, and passing with the text does not predict passing blind.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "146",
     "quote": "The 417 with-passage control failures were often ambiguity or broad `Both` keying, not necessarily",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "172",
     "quote": "Measured lesson: control-pass rate did not predict blind certifiability.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "40-41",
     "quote": "PASS if with-passage correct-rate >= 0.80 AND without-passage correct-rate <= chance-rate + 0.15 margin",
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
   "reason": "Quote verbatim; 13/13 passed the sound gate and only 4/13 passed quality-B (lines 122-125). Added kb-0092 line 31, which states the same rule. Statement unchanged.",
   "statement": "Passing a leak test does not make an item good; separately check that it still tests the intended skill.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "127",
     "quote": "Lesson: anti-leak success alone is insufficient.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0092-student-ready-criticism-framework-2026-07-09.qmd",
     "lines": "31",
     "quote": "Anti-leak certification is necessary but not sufficient.",
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
   "reason": "Quotes verbatim (lines 208-210 and 214). The per-format pass rates at lines 165-170 back the claim. Refines 5.",
   "statement": "Item formats leak differently: single-choice items through general knowledge or a 'textbook-correct' option, multi-select through mutually reinforcing options, highlight items through stems that signpost the span, ordering items through events with a natural order. Design each against its own leak.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "208-210",
     "quote": "- MCQ leaked through ordinary school knowledge, vocabulary, or a \"textbook correct\" option; - MSQ leaked through mutually reinforcing correct options; - hot-text leaked when stem/span wording signposted the answer.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "214",
     "quote": "- failed when fragments had natural story/process order;",
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
   "verdict": "keep-with-fix",
   "reason": "The quote sits at lines 45-46, not 46-48. It is extended to line 44 for the neutral-label clause. 700 certified matches lines 62 and 144.",
   "statement": "In items asking which source states a detail, use neutral labels and topically balanced statements, so only reading the sources reveals which one says what.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "44-46",
     "quote": "- categories were neutral: `Source A`, `Source B`, `Both`; - passage titles were not category labels; - statements were topically symmetric;",
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
   "reason": "Quote verbatim; cold-solvable ~0.8 and 1 of 20 rejected match (lines 113-121). One case, but the logic generalizes. Corollary of 5.",
   "statement": "If an item's answer is common general knowledge, no rewrite of the distractors can fix it; replace the content.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "120",
     "quote": "general knowledge; distractor surgery can't close it, needs full content replacement",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; blind accuracy went from 1.0 to about 0.0 on 10 items (lines 44-49). The audit's 'honest gate' claim is contested. Items flagged for correct_is_longest were certified clean after the switch, yet the adopted rule fails any key that is the longest option, and test-wise students are part of the target population. The statement is reworded to keep both sides; it stays compatible with candidate 41.",
   "statement": "A blind solve is only as good as its solver, so calibrate the solver before trusting leak rates: one that bluffs with world knowledge flags items that do need the text, while one that abstains can clear items a test-wise student would crack by option length or wording, so check those tells separately.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "70",
     "quote": "2. A solver that can bluff its way through without the passage will inflate leak rates.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "71",
     "quote": "3. A solver that responds `UNKNOWN` on true comprehension items gives a more honest gate.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "56",
     "quote": "- `correct_is_longest`",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0092-student-ready-criticism-framework-2026-07-09.qmd",
     "lines": "26-27",
     "quote": "test-wise students, and students willing to click through or guess.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "67-68",
     "quote": "anti-gaming rule: length must never be the tell",
     "verbatim": true
    }
   ],
   "against": "kb-0096 itself says it does not prove the new baseline is the only correct one (line 80). Candidate 41: low self-confidence must not erase exact blind recoveries.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 41,
   "verdict": "keep",
   "reason": "Quotes verbatim; 3/8 exact recoveries and 0.71875 mean partial accuracy (line 43). Compatible with 40 as fixed: abstaining is acceptable, but an exact recovery counts whatever confidence the solver states.",
   "statement": "Count a blind solver's exact correct answers as leaks even when it reports low confidence; self-reported confidence must not erase exact recoveries.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "44",
     "quote": "the sealed rule had ignored those hits because the solver reported low",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "59-60",
     "quote": "model self-confidence cannot erase exact blind recoveries",
     "verbatim": true
    }
   ],
   "against": "A calibration note held that discarding low-confidence forced guesses was correct (kb-0100, name-bearing, not cited); see also kb-0096.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 42,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (0/3 vs 3/3). The found_by figure '9 of 70 showcase candidates' could not be found anywhere in the knowledge base. The cited item later leaked with no text at all under a stronger solver (line 33), so that catch was partly a weak-solver artifact. The capstone gate's 2 leaks conditioned on earlier-lesson texts (lines 39-40, added) give independent support.",
   "statement": "Test whether an item can be answered from texts in earlier lessons, not just with no text; knowledge carried forward can give away later answers.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "32",
     "quote": "(choice-hottext-20: plain-blind 0/3 but 3/3 with prior-lesson corpus)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "39-40",
     "quote": "10 candidates, 0 certified, 8 plain-blind leaks, 2 spine-conditioned leaks, 0 defective.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0098-incept-service-coe-catchup-2026-07-09.qmd",
     "lines": "39",
     "quote": "later questions become answerable from earlier lessons without proving true comprehension.",
     "verbatim": true
    }
   ],
   "against": "kb-0120 line 33: under a newer solver the same item was solved 3/3 with no text at all, so its earlier-lesson catch is historical.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 43,
   "verdict": "keep",
   "reason": "Quote verbatim (lines 26-27). It contrasts reading with history (AP-style) source tasks and generalizes across subjects. Refines 5.",
   "statement": "Fit the leak check to the subject: when the task is reading a text, finding the answer in it is the skill; in source-based history tasks, the answer appearing in the source counts as a leak.",
   "kind": "adopted rule",
   "evidence": [
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
   "name_bearing_source": false
  },
  {
   "index": 44,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The original statement and the kb-0167 line-72 quote named a job role, so the statement is rewritten and the quote moved to line 71. Added the AP mutation-test line (kb-0170 line 126). Distinct from 3: this is about the data reaching the screen, not the wording.",
   "statement": "Test that what reaches the student's screen carries no answer keys, rubrics, stored feedback or other answer-bearing fields meant to stay hidden.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
     "lines": "50",
     "quote": "tested at every step to carry none of `answer_index`, `correct_indices`, `rubric`, `criteria`,",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "71",
     "quote": "Define a student-only source projection containing `student_material` plus approved citation",
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
   "name_bearing_source": false
  },
  {
   "index": 45,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; the kb-0172 line names people elsewhere, but the quote does not. The kb-0234 STEM-LEAK line is about stem-to-option word overlap, which is candidate 60's claim, not question-to-text matching. It is replaced with two keyword-matching lines. Refines 5.",
   "statement": "A question that can be answered by matching visible words, rather than by rereading and understanding, tests matching; independent tasks must require real rereading.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "35",
     "quote": "The independent text/task must require genuine rereading rather than a visible word-match.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "133",
     "quote": "- Closed-response items must require the target reasoning and must not be answerable by surface cues, keyword matching, option length, or test-wise elimination.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "45",
     "quote": "and no keyword-answerability",
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
   "reason": "kb-0231 is verbatim: a probe of 18 items found 1 stated conclusion and 0 reverse defects (lines 79-87). The kb-0180 quote sits at lines 105-106, not 104-105.",
   "statement": "An inference item is invalid if the text states its conclusion outright, and a retrieval item is invalid if it secretly needs inference; check both directions, and word each item for the skill it really tests.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd",
     "lines": "75",
     "quote": "behavior is fine — that's the clue; stating the trait/conclusion itself is a disguised-FIND",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "105-106",
     "quote": "a FIND question dressed as INFER (or the reverse) is a defect, not style",
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
   "reason": "Quotes verbatim. 'Keep scored assessment items separate from what was taught' clashed with assessing taught knowledge (candidate 58). The source keeps only the independent/transfer items disjoint from taught claims, so the statement is narrowed.",
   "statement": "Let taught knowledge recur and compound across the learning texts, but test independent comprehension on cold passages whose answers were not taught.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "70",
     "quote": "Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd",
     "lines": "81-82",
     "quote": "\"Independent item claim_ids must be a subset of independent_claim_ids and disjoint from teaching_claim_ids\"",
     "verbatim": true
    }
   ],
   "against": "Knowledge carried forward can leak answers (kb-0098 line 39, kb-0120 line 32), and the 'disjoint' rule was verified only at design level (kb-0074 lines 85-88).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 48,
   "verdict": "keep",
   "reason": "Quotes verbatim. kb-0093 line 115 also asks for a claimed-vs-assessed construct check. Distinct from 49 and 63.",
   "statement": "Check each item's declared skill or standard against what it actually assesses, including thinking level: 'identify' cannot assess 'analyze'.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "122",
     "quote": "- N1: DOK-level alignment. Coverage is false if an \"analyze\" standard is assessed by \"identify.\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "92",
     "quote": "- Example found: a main-idea lesson served an inference/evidence item.",
     "verbatim": true
    }
   ],
   "against": "One cited mistag was defended as defensible (kb-0074 line 51).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 49,
   "verdict": "keep-with-fix",
   "reason": "The kb-0093 N8 quote is on line 129, not 128 (line 128 is N7). kb-0086 is verbatim.",
   "statement": "Include tasks that require combining several pieces of knowledge, not only one-at-a-time checks; students can master parts and still fail to combine them.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "123",
     "quote": "- Integrative lessons matter: students can master parts and still fail when asked to select, combine, or justify them in context.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "129",
     "quote": "- N8: integrative-assessment presence. Include tasks that coordinate multiple KCs, not only atomized checks.",
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
   "reason": "Quotes verbatim, and the arithmetic holds: 90% of 4 or 5 items needs every item correct.",
   "statement": "Check the arithmetic of a pass threshold: on a short test, a 90% bar demands a perfect score.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
     "lines": "37",
     "quote": "two 4-5 item tests are un-gateable (no \"90% of 4\")",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "141",
     "quote": "- gate-arithmetic trap where small tests make 90 percent require a perfect score;",
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
   "reason": "Quotes verbatim; 5/8 matches, and the repaired two-span form fell to 2/8 (kb-0134 lines 108-109).",
   "statement": "Check each item's scoring settings and its real chance of being guessed; a wrong setting can accept incomplete answers, and a one-of-four pick may be guessed blind often.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "99-100",
     "quote": "right buckets keyed 2x with `match-max=1`, which would have let a spec-conformant renderer accept an incomplete response",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0134-g5-reading-v2-local-design-package.qmd",
     "lines": "99-100",
     "quote": "I03 had leaked through forced one-of-four guessing: 5/8 plain-blind exact guesses.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (2-3 forms). 'Re-showing the same test measures memory of the items' appears in no cited line and is removed. This is essentially 48 applied to retakes; it is kept because it adds the parallel-forms requirement and the delayed-test-with-new-items rule as evidence for 48.",
   "statement": "A retest after reteaching needs new items (parallel forms), given after a delay.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
     "lines": "60",
     "quote": "**Author parallel forms per lesson test** (BLOCKING for hole-filling) — 2-3 forms each so three-state retry works",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "141",
     "quote": "- Require 90% to advance; if not met, give intensive instruction and a delayed test with new items.",
     "verbatim": true
    }
   ],
   "against": "kb-0164 line 88 warns against a global raw 90% mastery bar, which kb-0086 line 141 assumes.",
   "general": true,
   "duplicate_of": "48",
   "name_bearing_source": false
  },
  {
   "index": 53,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'The same students, close together' had no cited line, so the linking-study design (kb-0086 line 36) is added. Adds to 48 and 67.",
   "statement": "Don't claim a practice or proxy test predicts the real test, or report on the real test's scale, until the same students have taken both close together; enforce that limit in code.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "63",
     "quote": "3. **No-RIT-pre-pilot is enforced in CODE**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "40",
     "quote": "- Honesty gate preserved in the email: no RIT output; engine physically will not emit RIT until linked to real MAP scores.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "36",
     "quote": "same students take both tests within two weeks, order-counterbalanced",
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
   "reason": "Quotes verbatim; Holland & Wainer 1993 is confirmed at kb-0162 lines 118 and 343-344.",
   "statement": "After items go live, review how they behave: fairness across groups, drift over time, and students stuck repeating failure. This is part of an item's life, not optional cleanup.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "99-100",
     "quote": "escalation are part of the lifecycle rather than optional cleanup.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0162-assessment-item-difficulty-evidence.qmd",
     "lines": "119",
     "quote": "an item’s difficulty may differ systematically across subgroups even when overall ability is matched.",
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
   "reason": "Quote verbatim (lines 95-96). Compatible with 1 and 4: the correction may come after the test.",
   "statement": "When a distractor is built on a real misconception, follow it with corrective feedback or correction after the test, because a plausible wrong option can plant false knowledge.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "95-96",
     "quote": "post-test correction because plausible lures can seed false knowledge;",
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
   "reason": "Quotes verbatim.",
   "statement": "Declare each assessment's purpose (practice, mastery, diagnostic, summative or unseen-text measure) before reading its results; teaching checks and gated assessments are different things.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "89-90",
     "quote": "- declare whether a resource is formative, mastery, diagnostic, summative, or cold measurement before interpreting its result;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "36-37",
     "quote": "l0-l3 now declare teaching-check / non-gating behavior; l4 is the gated interval assessment at 90%",
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
   "reason": "Quote verbatim. The DOI for Mislevy, Almond & Lukas 2003 is confirmed at kb-0162 line 269.",
   "statement": "Before writing an assessment item, define the knowledge it targets, the claim, the evidence, the task conditions, the range of possible answers and the scoring rule.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "84-85",
     "quote": "- no KC, claim, evidence indicators, task conditions, outcome space, and scoring rule means no assessment;",
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
   "reason": "The kb-0181 quote is on line 143, not 142. 'Counts as learned' stretched the source's 'cash point', which means graded productive use (lines 138-140), so it is reworded.",
   "statement": "Match the task to the kind of knowledge: picking from options cannot show productive or explanatory knowledge, so a taught word is cashed in only when a graded task makes the student produce it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "86-87",
     "quote": "- match the task family to the knowledge: recognition is not enough for productive, representational, justificatory, or integrative constructs;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "143",
     "quote": "MCQ recognition alone — however many options — never counts as a cash",
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
   "reason": "Quote verbatim. It is a single line from a BrainLift summary, but it is a standard Direct Instruction rule.",
   "statement": "Mastery tests should use the formats students met during instruction.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "140",
     "quote": "- Mastery tests should match formats experienced during instruction.",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 60,
   "verdict": "keep",
   "reason": "Quotes verbatim (626 longest-option rows). The kb-0183 line names the ruling's author before the quote; the quote itself has no name. Distinct from 6 and 8.",
   "statement": "The right option must not stand out: not the longest, not the shortest, not the odd one out in form, not the one sharing most words with the question. Distractors should be plausible near-misses of the same length and grammatical form.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "63-64",
     "quote": "The right option must not be the longest, the shortest, the odd one out, or the one that reuses the most words from the stem.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0223-g3-review-rounds-and-tooling-2026-09-18-to-21.qmd",
     "lines": "24",
     "quote": "option 2 reworded from a *the*-opener to match the wh-form distractors",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd",
     "lines": "117",
     "quote": "longest-option-tell: 626",
     "verbatim": true
    }
   ],
   "against": "A re-calibrated blind solver cleared items flagged `correct_is_longest` (kb-0096 line 56).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 61,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim. 'No yes/no questions' had no cited line, so kb-0136 line 112 is added. 'Four, not two' was stated as settled, but kb-0164 records a research consensus for three and forbids filler. The statement now keeps only what both sides agree on.",
   "statement": "Don't use two-option or yes/no choice items, which make guessing pay half the time, and never pad an item with filler distractors; whether three or four options should be the default is still unsettled.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "80-81",
     "quote": "to prevent guessing\" — a two-option item is a 50/50 guess)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "112",
     "quote": "A two-option yes/no item permits a 50/50 guess.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "102-103",
     "quote": "the MCQ BrainLift reports a research consensus favoring three",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "104-105",
     "quote": "An agent must not resolve this by adding filler",
     "verbatim": true
    }
   ],
   "against": "kb-0183 lines 80-81 record an adopted exactly-four-options rule; kb-0164 lines 102-105 record a research consensus for three and leave the default to an explicit decision.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 62,
   "verdict": "keep",
   "reason": "Quotes verbatim (31 items swept, line 24). This adds form-level review to 8 and 68. The path names a fictional book, not a person.",
   "statement": "Review a test form as a whole: the answer to one item must not give away another, and answer positions, option lengths and blueprint coverage must balance across the form.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0211-peter-pan-reviewer-round-2708.qmd",
     "lines": "24",
     "quote": "Both usage checks were crackable via the single pair \"baby\"+\"sleep\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "93-94",
     "quote": "- answer position, option length, distractor function, enemy items, blueprints, and independent cold review are form-level obligations;",
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
   "reason": "Quotes verbatim (638 and 192). The elimination rationale is not stated in the source, but it follows from the check's own name.",
   "statement": "Matching items need at least one unused option, or the last match comes free by elimination; the unused option must not be labelled as a decoy.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd",
     "lines": "116",
     "quote": "unused-right-bucket-exists: 638",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "58",
     "quote": "192 match items announce a decoy bucket",
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
   "reason": "Quote verbatim; the pinned defect is at lines 40-43.",
   "statement": "When students choose from excerpts of a text, list the excerpts in the order they appear in the text.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "39-40",
     "quote": "a `hot_text` question's tappable sentence list must be offered in the same order those sentences occur in the passage",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim; the kb-0059 fragment is on line 49. The source says the template pre-defined the affix, not the root, so 'root' was wrong.",
   "statement": "A test of a taught word must not define the word or its parts (such as its affix) in the question, and its right answer must not just repeat the taught definition.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "49",
     "quote": "pre-defined the affix in the stem",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "93-94",
     "quote": "DEFINITION-ECHO (a vocab-testing item's correct option must not just echo the taught definition).",
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
   "reason": "The kb-0229 quote spans lines 78-79. The 0.74 vs 0.70 ratio and 3 of 117 cases are confirmed (lines 76-77 and 96, added). The kb-0237 line shows the empty-answer failure, so the statement now names both probes. Specializes 37/38.",
   "statement": "Test every automated marker with the ideal answer and with an empty or off-topic one: a guard against copying rejected word-perfect recall of the sentence the lesson taught, and other judges accepted empty answers.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0229-closing-questions-build-2026-09-25.qmd",
     "lines": "78-79",
     "quote": "the gate was punishing the child for saying the taught sentence exactly.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0229-closing-questions-build-2026-09-25.qmd",
     "lines": "96",
     "quote": "117 judge cases authored, 114 OK/3 WRONG pre-fix (all three the echo class)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "63",
     "quote": "oral/typed judges accept empty or content-blind answers.",
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
   "reason": "Quote verbatim. This is the remedy for 34, not a duplicate of it.",
   "statement": "Give the same verdict to an identical resubmitted answer: mark at the most deterministic setting and cache repeat submissions.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "39-40",
     "quote": "running the first judging attempt at the most deterministic model setting and caching identical resubmits to return the same verdict instantly.",
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
   "reason": "The kb-0245 quote is on line 39, not 37-38; those lines name people. kb-0238 is verbatim.",
   "statement": "A sentence frame must stay grammatical for every word a student might put in it; check frames with the blank filled in.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "35-36",
     "quote": "which stays grammatical regardless of the filling word.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
     "lines": "39",
     "quote": "checks a lead's grammatical fit under substitution",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. Distinct from 40.",
   "statement": "A worked example must show the reasoning, including what was rejected and why, as an expert thinking aloud; it must not hand over a filled-in answer or make the thinking look easy.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "32",
     "quote": "one, what was rejected and why — never just reveal a filled-in organiser.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "64",
     "quote": "Do not model the thinking as if it is easy.",
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
   "reason": "Quotes verbatim; the partial-answer clause is at kb-0180 line 34. kb-0232 contradicts itself: the heading says three of four labels were renamed, the body (lines 58-59) says all four diverge.",
   "statement": "Modelling, guided practice and independent practice must run the same skill with identically named steps, and the stages must be recognisable even with their labels removed; guided practice gives a partly finished answer for the student to complete.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "35",
     "quote": "we-do, a fresh question is not a we-do); I-do, we-do and you-do must run the *same skill*, never",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "55",
     "quote": "**MAJOR — we-do renames three of the four I-do step labels (R-KC-11).**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "44",
     "quote": "that survive the strip-the-labels test",
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
   "verdict": "keep-with-fix",
   "reason": "The kb-0226 quote is on line 40, not 41. 'As students succeed' mixed two sources: kb-0174 fades support by exposure, while kb-0180 fades it after five successful uses (added). Reworded to cover both.",
   "statement": "Plan how support fades across a unit, from heavy modelling to hand-over, and remove supports such as pre-highlighted candidates and stated counts from independent practice.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
     "lines": "72-73",
     "quote": "exposure-based fade progression per skill (heavy model 5/2/1 → shift 3/2/3 → hand-over 1/2/5)",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "41-42",
     "quote": "scaffolds fade across a unit (a procedure \"collapses into a two-step option after five successful uses,\"",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0226-g3-pre-submission-closure-audit-2026-09-24.qmd",
     "lines": "40",
     "quote": "3. Independent Find pre-glows candidates and states the count (L5-L7), where the design wants an open hunt",
     "verbatim": true
    }
   ],
   "against": "The fading rule was never implemented or measured (kb-0180 lines 41-44).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 72,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds modelling choreography to 21 and 26.",
   "statement": "When modelling, say what you will do, show it done, then check; show nothing before it has been thought aloud, keep one target of attention at a time, and keep the steps and the live question visible.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
     "lines": "62-63",
     "quote": "then the check; nothing on screen before it is thought aloud; feedback finishes before the next step renders; one attention target at a time; only the current sentence highlighted.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "84",
     "quote": "The steps and live question must remain visible, and the model should surface one thing at a time",
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
   "reason": "Quotes verbatim. The playback-speed clause is in the same kb-0172 line 27.",
   "statement": "Every screen should ask for a response that serves the teaching move; a decorative tap or skippable nudge doesn't count, and students must not be able to speed through narration they need to hear.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "27",
     "quote": "a decorative tap control does not satisfy the concern",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "130",
     "quote": "- Keep passive episodes short and make active checks consequential; skippable \"pause and think\" is not a check.",
     "verbatim": true
    }
   ],
   "against": "Some feedback worried that too many checks become compliance rather than learning (kb-0212, name-bearing, not cited).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 74,
   "verdict": "keep",
   "reason": "Quotes verbatim; the PNAS URL for Szpunar, Khan & Schacter 2013 is at kb-0248 line 213. The statement concerns video that carries content, not short intro previews.",
   "statement": "Break up any long video that carries essential content with required quick checks.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "31",
     "quote": "If video carries essential context, interrupt it with mandatory quick checks so the learner does not watch a long unexamined clip.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "211-212",
     "quote": "Interpolated memory tests inserted into recorded lectures cut mind-wandering by roughly a third and improved recall versus uninterrupted video.",
     "verbatim": true
    }
   ],
   "against": "The intro-video BrainLift bans a question after the preview that asks what happens next, because it signals which story threads matter (kb-0220 lines 23-24).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 75,
   "verdict": "keep",
   "reason": "Quote verbatim; a single BrainLift line.",
   "statement": "Practise a new skill in a block first, and mix it in with other skills only once it is ready.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "160",
     "quote": "- Interleaving is only appropriate after the skill is ready; massed/blocked first, interleaved later.",
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
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim. The source says feedback timing should shift as proficiency grows, not that feedback should shrink, and too much feedback 'can' reduce processing, not that it does.",
   "statement": "Too much feedback can reduce active thinking; shift when feedback comes as proficiency grows.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "161",
     "quote": "- Too much feedback can reduce active processing; feedback timing should shift as proficiency improves.",
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
   "reason": "Quotes verbatim (~90:10).",
   "statement": "Keep several strands going at once, with only one introducing new material while the rest review (about 90:10 review to new).",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "145",
     "quote": "- Keep multiple tracks alive over time; only one track should introduce new material while the rest is review.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "43",
     "quote": "lesson composition as interleaved tracks at ~90:10 review:new",
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
   "reason": "Quotes verbatim. The AP repair bucket was later closed (kb-0170 lines 86-88). Overlaps 4 and candidate 52, but this one covers the item-level correction loop.",
   "statement": "After an error, correct it briefly, send the student to the taught check for that skill, and retest later with different items or evidence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "143",
     "quote": "- Error correction should be immediate and brief: correct, test, give intervening items, then retest later.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "67-68",
     "quote": "4. Rebuild every assessment and writing criterion as failed function -> relevant taught check -> different-evidence retry.",
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
   "reason": "Quote verbatim. It is one of six AP repair buckets that blocked replication (lines 58-60), later closed (kb-0170 lines 86-88). Related to 41.",
   "statement": "Independent tasks must not reuse the answer-bearing evidence the worked example already used; require new evidence.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "64",
     "quote": "2. Replace independent tasks that reuse answer-bearing modeled evidence in Lessons 1, 3, and 6.",
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
   "reason": "Quotes verbatim.",
   "statement": "Every activity should state its rationale (the target knowledge and performance, the failure it guards against, why this activity, when its support is withdrawn), and every assessment item should justify its format.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "134",
     "quote": "- Any activity needs a rationale: target knowledge type, performance, failure mode it protects against, why this activity, and scaffold retirement condition.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0189-validators-and-laws.qmd",
     "lines": "37",
     "quote": "every assessment item argues its format",
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
   "reason": "Quotes verbatim.",
   "statement": "Standards set scope, not sequence: build an explicit progression spine (entry assumptions, prerequisites, source ladder, evidence model), and link units by their big ideas rather than surface facts.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "119",
     "quote": "- Standards constrain scope but do not provide a teachable sequence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "121",
     "quote": "- A course needs an explicit progression spine, entry assumptions, prerequisite policy, source ladder, and evidence model.",
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
   "name_bearing_source": false
  },
  {
   "index": 82,
   "verdict": "keep",
   "reason": "Quotes verbatim. Adds a reading purpose to 40.",
   "statement": "Give a purpose for reading before the text, and reread chosen parts for that purpose instead of rereading the whole text by habit.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "61",
     "quote": "Children need a reason to read before they start",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "93",
     "quote": "4. Rereads point to a text subset for a declared knowledge purpose rather than replaying a whole text by habit.",
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
   "reason": "Quote verbatim; only the leading indent is dropped.",
   "statement": "When a task asks for evidence from a text, keep the text visible.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "86",
     "quote": "- Prompts ask for textual evidence, but the passage is hidden when the student needs to cite it.",
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
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim. 'Rely only on what the text and lesson have given' clashed with the inference frame itself, which combines text clues with 'what I know' (lines 76-78). The ruling bars outside cultural facts the text never gave, so the statement is narrowed.",
   "statement": "An inference task must not depend on cultural or world facts the text never gave and students may lack; its clues come from the text's own words.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "81",
     "quote": "inference may only use what the passage's own words show; extension deepens the mood from",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Hunt for keywords' had no support in the cited file and is removed; added line 72 for the one-sentence main idea.",
   "statement": "Don't teach rules of thumb that many texts break, such as 'the title states the main idea' or 'the main idea sits in one sentence', and don't teach that evidence is always one sentence.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "72",
     "quote": "- A fable's meaning is rarely contained in one sentence.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "73",
     "quote": "- Titles frequently do not state the main idea, so checking against the title is not a dependable rule.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "80",
     "quote": "The lesson may also embed the misconception that text evidence always points to one sentence.",
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
   "reason": "Quotes verbatim: 58 to 217 words, about 166, against roughly 2,740 for the state test (line 92). That the team accepted the point could not be confirmed and is not needed.",
   "statement": "Choose texts for a knowledge sequence, genre balance and quality, judging complexity by reading it rather than by a readability number alone, and include longer and paired texts that build stamina.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "78",
     "quote": "Choose texts for a coherent knowledge sequence and a genre balance that includes poetry, drama and more literary work, and judge complexity qualitatively as well as by Lexile.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "94",
     "quote": "Course passages run 58 to 217 words, averaging about 166.",
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
   "verdict": "keep",
   "reason": "Quotes verbatim; kb-0172 line 95 restates the hint-after-attempt rule. Adds timing and escalation to 1 and 3.",
   "statement": "Help comes only after an attempt, and hints escalate from criterion cues; only the last hint names the evidence's own words.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "43",
     "quote": "The durable rule is attempt first, then targeted help.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "53-54",
     "quote": "reword to criterion cues, naming a clue's actual words only in the *last* nudge",
     "verbatim": true
    }
   ],
   "against": "The exact trigger count for help (for example, three errors) was never settled (kb-0172 line 43).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 88,
   "verdict": "keep-with-fix",
   "reason": "The kb-0224 quote is on line 57, not 58. The 1.00 overlap was the reply to a student who stayed silent, not one who was unsure. This is mostly 3 applied to every line type; it is kept because it adds evidence that praise, nudge and silent-branch lines handed over answers.",
   "statement": "Check every line around a question for the answer (instructions, praise, nudges, replies to a student who stays silent), not only the replies to wrong answers.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "129-130",
     "quote": "nudge/instruction lines on L4 p22, L5 p15b/p16, L6 p15b, L7 p16 were handing over the Step 3-4 answer outright",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0224-g3-dialogue-branches-pace-gate-roll-forward-2026-09-22-23.qmd",
     "lines": "57",
     "quote": "our L4 silent branch was at **1.00** overlap (verbatim echo)",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "3",
   "name_bearing_source": false
  },
  {
   "index": 89,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'No claim of work the student didn't do' had no cited line, so audit row F15 (kb-0237 line 71) is added.",
   "statement": "Feedback and summaries must be true to what the page offers and what the student did: no promised replay that doesn't exist, no canned line posing as a response, no claim of work the student didn't do.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "70",
     "quote": "The welcome beat overclaims contingent listening while still issuing a static, answer-independent recast",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "71",
     "quote": "The receipt screen asserts out-loud/self-done events that did not actually happen on the typed/floor interaction paths.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
     "lines": "45",
     "quote": "the L4 video \"Listen again\" false-promise fix",
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
   "reason": "Quotes verbatim. The original merged two rules, 'longer than the passage' and 'longer than the instruction'; they are now stated separately, with line 94 added.",
   "statement": "Keep corrective feedback shorter and simpler than the instruction it supports; feedback longer or more complex than that instruction has become new instruction, and feedback longer than the passage is a defect.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "96-97",
     "quote": "if corrective feedback is longer or more complex than the original instruction, the item has crossed into new instruction.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "94",
     "quote": "- feedback longer than the passage is a defect.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "59",
     "quote": "it is too long, sometimes longer than the passage, and has basic capitalization defects.",
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
   "reason": "Quotes verbatim (25 words). The cited research is for one grade band (lines 93-96), but the source applies the same cap to Grade 9 (line 112).",
   "statement": "Cap every sentence a student must act on (instructions, questions, hints, feedback) at about 25 words, leaving the source text and taught frames exempt, and apply the same cap to feedback generated live.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "97",
     "quote": "25 words a sentence, maximum",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "109-110",
     "quote": "since no static validator can see a line that does not exist until a child answers.",
     "verbatim": true
    }
   ],
   "against": "kb-0195 line 69 caps a whole feedback reply at 40 words (never over 60) for older students; that is a per-reply cap, not a per-sentence one, so it does not conflict.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 92,
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Motives, absolutes' were not evidenced; the case was an invented cause. Extends 17 to unquoted claims.",
   "statement": "Every claim a lesson makes about what a text says, including any cause it gives, must trace to the text's own words; check unquoted attributions ('the story says…') as strictly as quotes.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "48-49",
     "quote": "exact defect class (grounding inference in invented rather than real textual evidence) the lesson exists to teach the child to avoid.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "79",
     "quote": "phrasing — the shape that hides the worst defects, since unquoted claims look like nothing).",
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
   "reason": "Quotes verbatim.",
   "statement": "Any line referring to earlier or later material must be true to the actual order, and no question, option or hint may depend on something the student hasn't reached yet.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "123",
     "quote": "- N2: relational-reference factuality. \"As you saw last lesson\" claims must be true against order.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "86-87",
     "quote": "a question/option/hint on page N must not depend on a concrete story noun the child has not read yet",
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
   "reason": "Quotes verbatim (22 hits across 8 lessons). 'List the misconceptions each unit must avoid' had no cited line, so kb-0136 line 53 is added.",
   "statement": "List the misconceptions each unit must avoid, and check every text that carries subject content against expert misconception lists, even in another subject's course; keep observation, theory, interpretation and opinion distinct.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "53",
     "quote": "- Add unit-level misconceptions to guard against alongside each unit spine, including the science misconceptions discussed below.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "48",
     "quote": "4. apply the misconception-check process to every science-bearing Read/Write text;",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "49-50",
     "quote": "5. distinguish observation, hypothesis, theory, consensus, measurement, interpretation, and opinion accurately.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
     "lines": "84-85",
     "quote": "22 Tier-1 misconception hits across 8 lessons",
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
   "verdict": "keep-with-fix",
   "reason": "The quote is trimmed to drop a historical author's name, and the AP citation-correction line (65) is added. 'Author' is reworded. This was one AP audit bucket, later closed (kb-0170 lines 86-88).",
   "statement": "When students work from primary sources, show who wrote each source and why, and cite it accurately.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "66",
     "quote": "reform-advocate purpose to student-visible citation context.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "65",
     "quote": "chapters I, III, and V and Library of Congress General Collections",
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
   "reason": "Quote verbatim; the 'why' for each example is at kb-0181 line 37. The ruling's author is named after the quote, not inside it.",
   "statement": "Teach a concept with an example and a non-example that differ only in its defining feature, each saying why.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "33-34",
     "quote": "example and non-example differ in only the one defining feature, and the non-example states why it fails",
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
   "reason": "Quotes verbatim; kb-0181 line 30 (distinct taught words) also supports.",
   "statement": "Define each taught term one way and use that exact definition everywhere it appears, and make words taught together clearly distinct in meaning.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "38",
     "quote": "One definition per word, used everywhere it recurs",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "105",
     "quote": "- Choose distinct vocabulary words.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim (7/9). The kb-0181 line 49-50 quote names a group of people, so it is replaced with lines 46-48. Added line 69 for 'many encounters' (10 to 12).",
   "statement": "A taught word needs many encounters to stick (a working rule of 10 to 12 across the unit), so plan its reappearances; when the source text can't carry them, meet the need in the activities, never by editing an approved source text.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "65-66",
     "quote": "from 7/9 taught words appearing only once",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "69",
     "quote": "A word needs **10 to 12 encounters** across the unit/course to be retained",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "46-48",
     "quote": "a word not carried twice by the passage is still \"earned\" if the lesson's own activities (questions, options, feedback, frames, retell, recap) use it at least 3 times",
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
   "reason": "Quotes verbatim; kb-0181 line 41 (untaught hard words read aloud) also supports.",
   "statement": "Support every hard word in a text (let students hear it and see its meaning), not just the taught words, and don't let a check hinge on vocabulary the student hasn't been given.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "107",
     "quote": "- Make difficult words tappable and readable aloud—\"hear it, say it, map it\"—for students who cannot yet decode them.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "126",
     "quote": "- N5: linguistic validity. Untaught vocabulary or syntax can create construct-irrelevant difficulty.",
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
   "reason": "Quotes verbatim: 5 of 23 flagged, one with a wrong base word (line 54). The word-part tool is rule-generated, not a dictionary (line 49), so its flags still need a dictionary check.",
   "statement": "Verify word-part breakdowns and pronunciations against reference sources, never by intuition.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "50",
     "quote": "to all 23 authored vocab decompositions; 5 flagged for review",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "96-97",
     "quote": "look up dictionary IPA (Wiktionary + Merriam-Webster), never guess",
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
   "verdict": "keep-with-fix",
   "reason": "The kb-0213 quote spans lines 108-109, not 109-110. kb-0181 is verbatim.",
   "statement": "Ask one thing per turn and one question per screen, so feedback can address each part and nothing overflows.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "55-56",
     "quote": "complicates simultaneous feedback if a child gets both parts wrong",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "108-109",
     "quote": "two MCQs stacked on one page",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The video half is contested: a later meeting agreed intro videos may reveal the plot and characters. The statement is therefore scoped to pictures shown with a passage, and the video 'no spoilers' directive is dropped as evidence.",
   "statement": "A picture shown with a passage must match that passage and must not show characters or events the text hasn't introduced yet.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "69",
     "quote": "**L1 p8 opening image is a spoiler**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0210-aladdin-2508-feedback-and-pr27-safety-snapshots.qmd",
     "lines": "35",
     "quote": "opening image is a spoiler/mismatch",
     "verbatim": true
    }
   ],
   "against": "For intro videos, a later meeting 'agreed to reveal the plot and characters' (kb-0220 lines 45-47), so the no-spoiler rule for videos is not settled.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 103,
   "verdict": "keep",
   "reason": "Quotes verbatim (audit rows F1 and F11). The first half is a case of 3; the accessible equivalent is new.",
   "statement": "Diagrams and pictures must not reveal the answers to the questions they support, and every diagram needs an accessible text or table equivalent.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "57",
     "quote": "prints its own answer key in-diagram",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "67",
     "quote": "The diagram is not element-addressable and has no accessible table equivalent.",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. 'Because students dismiss fake AI' was not stated; the source sets a child's-eye test instead (lines 3929-3930, added). The kb-0207 lines nearby name people, but the quotes do not. Adds to 22 and 34.",
   "statement": "Generated human figures must pass a 'would a child call this fake AI?' check; if they can't, stylize away from realism or cut their screen time, and judge near-photoreal faces by three independent reads with majority rule.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0207-memory-digest-project-reference-user.qmd",
     "lines": "3929-3930",
     "quote": "add an explicit \"would a child call this fake AI?\" gate for humans",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0207-memory-digest-project-reference-user.qmd",
     "lines": "3931",
     "quote": "- If a human cannot be made to pass, prefer stylization away from realism (more cartoon, less",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
     "lines": "91-92",
     "quote": "any near-photoreal human face now requires three independent reads with majority rule",
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
   "reason": "Quote verbatim. The line opens with a person's name before the quoted rule; the quote itself has no name.",
   "statement": "Never ship placeholder-looking elements; if the real asset isn't available, redesign without it and note the omission.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0207-memory-digest-project-reference-user.qmd",
     "lines": "2390",
     "quote": "never ship placeholder-looking elements; if an asset can't be obtained, admit it in notes and redesign the layout honestly instead",
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
   "verdict": "keep-with-fix",
   "reason": "Quotes verbatim. The original named a job role and is reworded. Added lines for 'the same across lessons' (kb-0189 lines 64-66) and the provenance stamp (kb-0200 line 49). Consistent with 2 and 50.",
   "statement": "Give the voice that reads the text and the voice that teaches different voices, keep each role's voice the same across lessons, and stamp every clip with its generator and voice; a text check cannot hear a wrong voice.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "58-59",
     "quote": "keeping the two voices distinct is how a student hears 'the story' and 'the teaching' as separate things.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0189-validators-and-laws.qmd",
     "lines": "64-66",
     "quote": "The violation is the SAME role (derived from filename stripped of page-prefix/trailing-index) cut in DIFFERENT voices across lessons",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "49",
     "quote": "a provenance stamp embedded in every mp3",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "45-46",
     "quote": "a correctly-worded clip in the wrong voice passes every automated check.",
     "verbatim": true
    }
   ],
   "against": "One grade keeps a single voice for every role, but only because its audio had already shipped (kb-0182 lines 59-60).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 107,
   "verdict": "keep",
   "reason": "Quotes verbatim. The fall-through default is at kb-0194 lines 72-75.",
   "statement": "Set each course's register (tone, praise, feedback length, voice and pace) for its own learners, and never let it default to another age group's settings.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "76-77",
     "quote": "reading about salinity gradients would have been read to as if this were a bedtime story",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0195-g5-book-lane-secret-garden-closed.qmd",
     "lines": "69",
     "quote": "medals/confetti) — specific process praise instead; feedback ≤40 words (never >60), one",
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
   "reason": "Quotes verbatim (16 lines). Captions here are an access requirement for video that gates progress; this does not settle open item 53.",
   "statement": "Narration must never say words the page doesn't print, and any narration or video that gates progress needs captions taken from the approved script.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "155-156",
     "quote": "two pages had drifted into a paraphrase of their own spoken script, 16 lines between them, while every other validator passed.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "187-188",
     "quote": "captions are the only way through for a child who cannot hear",
     "verbatim": true
    }
   ],
   "against": "The rule runs one way: a page may print words that are not spoken (kb-0194 lines 151-153).",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  },
  {
   "index": 109,
   "verdict": "keep",
   "reason": "Quotes verbatim (twelve options; 525/772). The source says the items were pushed into TEI formats; 'least accessible' in found_by is the reader's gloss. kb-0081 line 130 states the rule.",
   "statement": "Every interaction must work by keyboard and assistive technology with a capped number of options, and check what each quality rule does to accessibility.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "128",
     "quote": "one hot-text item offered twelve selectable options, an excessive motor and cognitive load for an eight-year-old.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0085-g5-red-team-findings-2026-07-06.qmd",
     "lines": "25",
     "quote": "RT-2 accessibility: anti-leak concentrates items into TEI formats (525/772), no",
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
   "reason": "Quotes verbatim. About checkers using the engine's own code, so distinct from 24 and 46.",
   "statement": "Check content with the delivery system's own logic, not an approximation; content that is valid as text can still fail on screen, and a text search can't answer questions about structure.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "111-112",
     "quote": "`validate-passage-refs` only proves the span text is a SUBSTRING of the passage; it does not run the engine's own unit-boundary logic",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
     "lines": "1211",
     "quote": "A substring search is not a structural test.",
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
   "reason": "Quotes verbatim; production had 1,077 items, all single-choice, and no other format had ever rendered (line 69). This is largely 46 applied to item formats; it is kept because it adds deliverability evidence.",
   "statement": "Certify an item format only once it has been rendered and answered live; a form can pass every check and still be impossible to deliver or answer.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "70-71",
     "quote": "we can fully certify a form that **physically cannot be delivered**",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0134-g5-reading-v2-local-design-package.qmd",
     "lines": "110-111",
     "quote": "all hot-text items were hardcoded as radios, so a two-span key was impossible to submit",
     "verbatim": true
    }
   ],
   "against": "none found",
   "general": true,
   "duplicate_of": "46",
   "name_bearing_source": false
  },
  {
   "index": 112,
   "verdict": "keep-with-fix",
   "reason": "Quote verbatim. The original named a role, and 'that bypass gates' is not stated in the source. The toggle was put behind a flag on a branch awaiting sign-off (kb-0208 lines 1717-1718). This is a single instance, but the principle is general.",
   "statement": "Keep review-mode or test shortcuts out of students' reach.",
   "kind": "measured",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0179-g3-peter-pan-close-out-state-and-reusable-process.qmd",
     "lines": "35-36",
     "quote": "reviewer-mode toggle behind `?review=1` / `NEXT_PUBLIC_REVIEWER_UI`, red-first test)",
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
   "verdict": "keep",
   "reason": "Quotes verbatim. The kb-0172 line names people outside the quote. The excerpt-rights gate is from the AP course (kb-0167 lines 74-76).",
   "statement": "Confirm the rights and permitted use of any third-party teaching material or excerpt before using it.",
   "kind": "adopted rule",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "65",
     "quote": "Confirm receipt, rights, and permitted use before placing any material in a training corpus.",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "75",
     "quote": "NPS excerpt-rights confirmation",
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
   "verdict": "keep",
   "reason": "Quotes verbatim (.30 to .07). Interpolated tests in recorded lectures point the other way, and the source marks the issue ruling-needed. The two findings involve different media and question types, so it stays open. Counter-evidence for 7.",
   "statement": "Should comprehension questions be asked during reading or only after it? One study found mid-text inferential questions cut recall, while interpolated tests in video improved it.",
   "kind": "open question",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
     "lines": "43",
     "quote": "inferential questions cut grade-4 recall .30->.07; her rule is ask AFTER not DURING reading, a",
     "verbatim": true
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "211-212",
     "quote": "Interpolated memory tests inserted into recorded lectures cut mind-wandering by roughly a third and improved recall versus uninterrupted video.",
     "verbatim": true
    }
   ],
   "against": "kb-0248 lines 211-213 (Szpunar et al. 2013, https://www.pnas.org/doi/pdf/10.1073/pnas.1221764110) found interpolated tests improved recall in recorded lectures.",
   "general": true,
   "duplicate_of": "",
   "name_bearing_source": false
  }
 ],
 "existing_checked": [
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0192-g3-book-component-catalogue.qmd",
   "lines": "40-42",
   "quote": "**a single-select answer is never revealed**, even after many tries — the option list is short and exhausting it finds the answer",
   "ok": true
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
   "lines": "50",
   "quote": "a wrong answer returns only \"Good try, let's look again,\" with no explanation and no correct answer shown.",
   "ok": true
  },
  {
   "truth": 7,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
   "lines": "43",
   "quote": "inferential questions cut grade-4 recall .30->.07; her rule is ask AFTER not DURING reading, a",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
   "lines": "66-67",
   "quote": "(~78% of raw generated items were blind-solvable before this gate",
   "ok": true
  },
  {
   "truth": 5,
   "effect": "qualifies",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
   "lines": "72",
   "quote": "4. Passage-dependent items can look \"kid-gameable\" under the wrong blind-solver and still be clean.",
   "ok": true
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0223-g3-review-rounds-and-tooling-2026-09-18-to-21.qmd",
   "lines": "31",
   "quote": "explicitly **not** the report's own suggested fix (a plant nursery is itself a correct use of the word).",
   "ok": true
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0187-skill-catalogue-and-workflows-index.qmd",
   "lines": "97",
   "quote": "\"first run caught a recurring rail defect and a 72.5% answer-position skew.\"",
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
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0190-jev-skills-and-engine-lane.qmd",
   "lines": "80-81",
   "quote": "each check returns `holds` / `fails` / **`unclear`**, and `unclear` is not a pass.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "72",
   "quote": "The local evaluation fallback grades free responses by keyword overlap, and a porting note propagates that defect.",
   "ok": true
  },
  {
   "truth": 10,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
   "lines": "25",
   "quote": "Misspelled \"magician\" marked correct; decide a comprehension spelling policy",
   "ok": true
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
   "lines": "41",
   "quote": "a short typed justification that is logged, not auto-graded",
   "ok": true
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0190-jev-skills-and-engine-lane.qmd",
   "lines": "36",
   "quote": "will judge injected user text as if it were yours — quarantine it.",
   "ok": true
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
   "lines": "67",
   "quote": "the model fabricated a second occurrence it then quoted back verbatim",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
   "lines": "1283",
   "quote": "image with a 0.46 match was being served (pictures now need positive evidence, accepted count fell 16 → 9)",
   "ok": true
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
   "lines": "59-60",
   "quote": "the model drifts on count once past roughly four figures",
   "ok": true
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0198-meetings-decisions-timeline-0819-1001.qmd",
   "lines": "92",
   "quote": "(a 1-minute cut lost cohesion)",
   "ok": true
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
   "lines": "96",
   "quote": "voice-provenance and voiceover-sync were all green because none of them opens the file.",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
   "lines": "86",
   "quote": "reached \"Great Work!\" across all 18 of U1·L3's scenes with **zero answers given**",
   "ok": true
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
   "lines": "20",
   "quote": "comprehension check was silently optional while every sibling page gates.",
   "ok": true
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
   "lines": "62-63",
   "quote": "Their 40-student design-science pilot reported more consistent scaffolding and less premature answer-giving.",
   "ok": true
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
   "lines": "114",
   "quote": "(a wide N-way choice never clears the 0.15 margin gate)",
   "ok": true
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0190-jev-skills-and-engine-lane.qmd",
   "lines": "92-93",
   "quote": "used AS the detector on raw items, it flagged 47% of items nobody had ever complained about",
   "ok": true
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
   "lines": "145-146",
   "quote": "traced to one broken check (`JUDGE-ANSWERABLE` firing on 77 of 78 items because it was shown a bare stem with no passage/options)",
   "ok": true
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
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
   "lines": "144",
   "quote": "First run: recall 0.625 but a **98.6% false-positive rate**",
   "ok": true
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
   "lines": "47-48",
   "quote": "38% is the first point on the curve; no pipeline seat until it beats the frontier-model critic on a real round.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
   "lines": "33-34",
   "quote": "run on the arrival page — a false 15/15 clean). Lens now builds paths and asserts the landed page id.",
   "ok": true
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
   "lines": "150",
   "quote": "`JUDGE-GRADE` had fired zero times across both runs",
   "ok": true
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
   "lines": "54-55",
   "quote": "adversarially recomputed from the raw per-call JSONL (not trusted from the run harness's own summary).",
   "ok": true
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd",
   "lines": "64",
   "quote": "Non-repetitiveness is by far the weakest dimension: **avg 0.14; 65 of 76 bundles scored exactly 0** on it.",
   "ok": true
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
   "lines": "231",
   "quote": "3. Use a different family for the gate than for the author. Never same-family certify.",
   "ok": true
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
   "lines": "34-35",
   "quote": "findings landed on lessons the calibration log marked green at review time",
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
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd",
   "lines": "62",
   "quote": "\"inconclusive therefore continue\" outcome.",
   "ok": true
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "54",
   "quote": "Publish-time flattening created NEW defects the local lint could not see",
   "ok": true
  },
  {
   "truth": 47,
   "effect": "qualifies",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
   "lines": "75",
   "quote": "even sophisticated persona prompting cannot fully overcome the Curse of Knowledge",
   "ok": true
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "159",
   "quote": "- Same-day testing after practice measures working memory more than long-term memory.",
   "ok": true
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
   "lines": "29-30",
   "quote": "review clips have no `audio_of` sha256, so a text edit (e.g. a definition rewording) leaves the clip silently stale",
   "ok": true
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0162-assessment-item-difficulty-evidence.qmd",
   "lines": "140",
   "quote": "Warns us not to rely on students’ subjective ease or fluency as indicators of mastery",
   "ok": true
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0192-g3-book-component-catalogue.qmd",
   "lines": "74-75",
   "quote": "after 4 wrong taps, Scout offers to find the remaining clues",
   "ok": true
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
   "lines": "24-25",
   "quote": "On the **binding grader** it **collapsed to ~28%**",
   "ok": false
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
   "lines": "39-40",
   "quote": "the class of defect that \"passes item evals but fails the holistic course eval.\"",
   "ok": true
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
   "lines": "31",
   "quote": "veto** caps the score at 0.84 if any CRITICAL metric is 0",
   "ok": true
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0186-scope-lane-and-model-routing-rules.qmd",
   "lines": "50",
   "quote": "confirm which course/artifact it was actually about",
   "ok": true
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
   "lines": "24",
   "quote": "That **0.29→0.95** jump existed only under a **discredited Gemini judge**.",
   "ok": true
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
   "lines": "149",
   "quote": "**Root cause:** a prompt instruction is not a write guard",
   "ok": true
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
   "lines": "100",
   "quote": "a one-rule edit causes unrelated behavior changes, kill it as the primary control plane",
   "ok": true
  }
 ]
}
```
