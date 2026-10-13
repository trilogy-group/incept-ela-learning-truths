# read:kb-reviews-evaluation

The agent's brief, verbatim, and its structured result.

## Brief

[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  make sure to triage and dig really deep into anything AP or knowledge related - we have had a LOT of different directions ultrathink ultracode fan out subagents

## Result

```json
{
 "direction": "kb-reviews-evaluation: knowledge_bot/knowledge entries on reviewer feedback and rounds, curriculum review, red team, anti-leak, calibration, InceptBench, generators, decisions/CoE, the G3/G5 close-out (lessons-learned, rulings, validators) and the AP/APUSH generator and course records, mined for general rules about making, judging, reviewing and measuring learning content.",
 "coverage": {
  "read": [
   "~/Projects/grade3-reading/knowledge_bot/INDEX.md (the index sits at knowledge_bot/, not in knowledge/; all 249 tag lines triaged)",
   "Closeout lessons and rulings, read in full: kb-0180, 0181, 0182, 0183, 0184, 0185, 0186, 0187, 0188, 0189, 0190, 0191, 0192, 0193, 0194, 0195, 0196, 0198, 0199, 0200, 0201",
   "Reviewer feedback and rounds: kb-0074, 0081, 0086, 0135, 0136, 0164, 0172, 0175, 0210, 0211, 0212, 0218, 0220, 0238",
   "Red team, evaluation and calibration: kb-0058, 0059, 0065, 0083, 0085, 0092, 0093, 0096, 0173, 0224, 0226, 0232, 0243",
   "Anti-leak and generator: kb-0064, 0066, 0067, 0068, 0071, 0073, 0091, 0100, 0236, 0242",
   "AP/APUSH: kb-0063, 0064, 0167, 0170, 0171",
   "Decisions, CoE and EPPC: kb-0022, 0076, 0078, 0097, 0098, 0125, 0127, 0128 (read in full); kb-0130, 0131, 0132, 0166 (summary plus grep); kb-0165, 0168",
   "Other evaluation entries: kb-0072, 0120, 0123, 0126, 0134, 0169, 0174, 0176, 0177, 0178, 0179, 0213, 0215, 0216, 0217, 0219, 0222, 0229, 0231, 0233, 0234, 0237, 0245",
   "kb-0162 and kb-0163, the calibration research BrainLifts: SPOV, insight and evaluation sections plus the DOK1 citations with DOIs",
   "kb-0206 (feedback memory digest): section list plus derive-dont-inherit, mixture-of-experts, no-firefighting, reading-checks-stay-retrieval, reuse-his-match-quality and vocab-parts sections",
   "kb-0207 (project memory digest, 4,000+ lines): section list plus deep-qc, deliverable-is-the-hosted-lesson, ela-reviewer-bot, grade5-content-integrity, laptop-student-first, close-what-we-can-document-first, no-placeholders and video-human-not-ai-looking sections",
   "kb-0208 (handover archive, 1,802 lines): outline, the Codex audit addendum, the gotchas and standing-corrections sections, and an engine-lane grep",
   "Science ledgers kb-0142 and kb-0144 to kb-0149: summaries, evidence boundaries and sample rows",
   "Outside scope, for one counter-quote only: kb-0248 lines 209-214"
  ],
  "skipped": [
   "Already used: kb-0069, 0070, 0099, 0235",
   "Never opened: knowledge_bot/.env and its .bak files",
   "Only skimmed: kb-0209 (artifact catalogue), 0221 (history and usage telemetry), 0225, 0227, 0228, 0230, 0244 (state records, no rules beyond those cited)",
   "Name-bearing paths (kb-0071, 0073, 0100, 0177, 0178, 0212, 0214, 0246) were read but not used as evidence; their content is referred to only in 'against' text",
   "Not read: the full rows of the science ledgers (draft data, every reviewer-comment cell blank)",
   "Outside this direction: TimeBack, API and platform entries, the reading-science and BrainLift research corpus (kb-0102 to 0121, 0153 to 0161), and the G9/Othello entries"
  ],
  "notes": "Line numbers come from cat -n or offset-corrected reads; key quotes were re-checked with grep. A quote that runs over two lines is joined with a single space. kb-0207's verbatim memories carry names inside the text, but its path does not. External research items give their DOI or URL as written in the source; where the source gave none, found_by says so. Kept apart deliberately: two measured tensions on blind solving (C-solver-unknown vs C-confidence-loophole) and two on the number of options (four options vs a research consensus for three)."
 },
 "candidates": [
  {
   "statement": "Close a defect by adding a standing check for its whole class that asserts what the student experiences, and count repeat classes per round; patching single instances lets the same class recur or silently revert.",
   "kind": "measured",
   "found_by": "39 checks added in 5 weeks while the same defect classes recurred 3-7 times; a later formatting commit reverted a pronunciation fix.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "18",
     "quote": "39 checks were added in 5 weeks (7-10 a week), yet the glow/scroll defect class was"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "43",
     "quote": "**A finding closes when its CLASS has an executable experience invariant**, not when the specific item"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "102",
     "quote": "silently reverted an earlier phonetic fix"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every rule that fails safe by going quiet (for example, missing media plays as silence) needs its own detector, or its failures become invisible to every other check.",
   "kind": "measured",
   "found_by": "The 'missing clip = silence' rule hid missing audio from all word-matching checks for weeks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "31",
     "quote": "A safety rule without a matching detector is a permanent blind spot."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
     "lines": "457-458",
     "quote": "Every rule that degrades to quiet needs a detector"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A check written by the same author as the content or fix, or built on the same enumeration as other checks, shares their blind spots; verify with an instrument built on a different model of the problem.",
   "kind": "measured",
   "found_by": "Bug and check shared one mental model; three audio checks enumerated clips the same way and all missed the same class.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "28",
     "quote": "**The check and the fix shared one author and one mental model**, so they shared a blind spot."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
     "lines": "1215",
     "quote": "If a clip class is invisible to one, assume it is invisible to all."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Defects pile up where a check's scope stops: write each check's scope down and add a simple check that covers every reference.",
   "kind": "measured",
   "found_by": "Every wrong-voice report came from the set a provenance check excluded; a desktop-only battery missed all phone/tablet defects.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0189-validators-and-laws.qmd",
     "lines": "59-60",
     "quote": "Every wrong-voice report we have logged came from exactly that excluded set."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0216-codex-visual-audit-2026-09-07.qmd",
     "lines": "44-45",
     "quote": "the content-check battery is desktop-only, so all three classes were invisible to it"
    }
   ],
   "against": "Phone and tablet findings were later ranked secondary to the laptop student view (kb-0207 laptop-student-first).",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "After any targeted fix, rerun every check, not just the one aimed at the fix; a fix that satisfies its own verifier can break another rule on the same field.",
   "kind": "measured",
   "found_by": "A speaker-label fix passed every targeted check and a 1466/1466 battery but turned the full suite red.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0185-quality-discipline-rules.qmd",
     "lines": "97-98",
     "quote": "a speaker-label fix passed every targeted check — machine re-listen, walkers, a 1466/1466 live battery — and still turned `npm run check` red on main"
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
   "statement": "Check every review finding against the current material before fixing anything; a large share of findings from reviewers and audit agents are false or stale.",
   "kind": "measured",
   "found_by": "An L4 audit: 9 of 12 serious findings were refuted. Audit false-positive rates ran 8-15%. 20 of 124 benchmark rows were already fixed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "9",
     "quote": "9 of 12 serious findings were refuted with evidence"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "101",
     "quote": "independently matching the arc-audit lane's measured 8-15%"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
     "lines": "1550",
     "quote": "20 rows already FIXED-ON-BRANCH"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    60
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a check raises many alarms, check the check first: confirm its false-positive rate on items known to be correct before treating flags as defects.",
   "kind": "measured",
   "found_by": "In a day of listening checks, 4 of 5 findings were probe errors. An onset check flagged 25% of clips at random.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "141-142",
     "quote": "the probe is often the bug (4 of 5 listen findings that day were probe-classes, not real defects)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "87-88",
     "quote": "an onset detector firing on 25% of clips at random was itself evidence the check, not the audio, was broken"
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
   "statement": "Before trusting any score, confirm the measurement harness: the scorer is live, reads the right field, runs on the right host and does not truncate output.",
   "kind": "measured",
   "found_by": "An AP question-generator project spent weeks 'stuck at ~28%' that turned out to be four harness bugs. A scorer with no credentials produced 11 phantom FAILs.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0063-aptraining-prior-exploration.qmd",
     "lines": "40",
     "quote": "(wrong field read, grader on wrong host, MCQ_SET mis-route 0→0.77, DBQ truncation"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0201-process-lessons-qa-convergence.qmd",
     "lines": "62-63",
     "quote": "a scorer-less dev server produced 11 phantom FAILs because nobody preflighted that the scoring API had credentials"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prove each checker on the real material before trusting it; a pass on test fixtures, an inherited checker or an old pass does not show the check works on these items.",
   "kind": "measured",
   "found_by": "5 of 6 inherited checks were silently broken behind a green run. A detector proven on fixtures was never run on the 120 real spans.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0187-skill-catalogue-and-workflows-index.qmd",
     "lines": "53-54",
     "quote": "where 5 of 6 checks were silently broken behind a green run."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0165-eppc-g3-reviewer-qualification-terminal-outcomes-human-next-gate.qmd",
     "lines": "81",
     "quote": "predicate to all 120 final private spans. Those are different claims."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    38,
    42
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Re-check items whenever the solver, the generator or the content changes; an earlier certification or model verdict goes stale.",
   "kind": "measured",
   "found_by": "A newer solver solved a previously certified item blind 3/3. Model evidence was withdrawn after source edits.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "53",
     "quote": "stale solver results are not certification"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0169-g5-reading-v2-final-submission-2026-07-20.qmd",
     "lines": "24",
     "quote": "the historical model snapshots are withdrawn after source changes"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    42
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When content fails a check, fix the content and never loosen the check; record existing violations as debt that can only shrink, and fail any new violation.",
   "kind": "adopted rule",
   "found_by": "Several gates were tightened lesson by lesson without weakening rules or pins.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "37",
     "quote": "never weaken the rule"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0189-validators-and-laws.qmd",
     "lines": "72",
     "quote": "entry (matches nothing) also FAILS — the list can only shrink."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Record every content rule with its reason, its source, its scope and how it is checked (code, a model judge kept advisory until calibrated, a live run, or a person); a rule nothing checks is only a reminder.",
   "kind": "adopted rule",
   "found_by": "A rule ledger; mis-scoped and ambiguous rules produced false audit findings.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0189-validators-and-laws.qmd",
     "lines": "96-97",
     "quote": "A law without a check is not a law here — it is a memory."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0173-edullm-standards-centralization-plan.qmd",
     "lines": "93-94",
     "quote": "2. semantic LLM judge, advisory until calibrated;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "109",
     "quote": "recommended a consistent `SCOPE:` line on its own"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Act only on review findings that show harm to a learner; keep earlier decisions unless new evidence arrives; hold changes of direction for one joint decision; stop the loop after a round with nothing critical.",
   "kind": "adopted rule",
   "found_by": "Unsupervised review loops oscillated, each round redoing the last round's choices.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0185-quality-discipline-rules.qmd",
     "lines": "25",
     "quote": "not preference — the bar is CRITICAL = would embarrass in front of the academics or lose a child"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
     "lines": "70",
     "quote": "recency/confidence/citation-count do not supersede an earlier academic decision."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0224-g3-dialogue-branches-pace-gate-roll-forward-2026-09-22-23.qmd",
     "lines": "85",
     "quote": "downgrade to NOTE unless it actively harms the child"
    }
   ],
   "against": "Two reviews genuinely conflicted, so holding to an earlier decision needs a named owner to rule (kb-0218 lines 74-75).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Write a build spec citing the lesson's own design document before authoring, then audit the result against that document line by line and against the whole programme, not just the passages.",
   "kind": "measured",
   "found_by": "Spec-first builds cut defects lesson after lesson. A deployed lesson lacked three components its design required. Passage-level alignment hid programme-level gaps.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0187-skill-catalogue-and-workflows-index.qmd",
     "lines": "62",
     "quote": "proven L5→L6→L7 (defects fell monotonically; L7 shipped zero content-validator defects)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0210-aladdin-2508-feedback-and-pr27-safety-snapshots.qmd",
     "lines": "121-122",
     "quote": "L4 as authored/reviewed/deployed was missing three components the design doc mandated"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
     "lines": "87",
     "quote": "but not yet at the programme level"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Work out every figure in a report from the primary source at writing time, and keep one canonical numbers block that other documents point to; figures copied from summaries are where errors come from.",
   "kind": "measured",
   "found_by": "All five errors found in one day's documents were inherited figures, and no derived figure was wrong. Reviewers attacked count drift.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0185-quality-discipline-rules.qmd",
     "lines": "120-122",
     "quote": "every single one was a figure inherited from an intermediate"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "100",
     "quote": "their biggest systemic failure is spec"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    24
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Report each readiness gate separately (authoring, human review, rights, accessibility, item certification, live delivery) and say exactly what each proof covers; never average gates, and missing evidence means 'not evaluable', never a pass.",
   "kind": "adopted rule",
   "found_by": "The AP course was 100% authored, but the other gates had not been run.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0171-apush-full-course-local-authoring-review-hub-archive.qmd",
     "lines": "50",
     "quote": "Do not average the independent readiness gates into a fake single quality score."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0173-edullm-standards-centralization-plan.qmd",
     "lines": "99-100",
     "quote": "`NOT_EVALUABLE` with named missing inputs and blocks any rejection-grade completion claim."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0210-aladdin-2508-feedback-and-pr27-safety-snapshots.qmd",
     "lines": "142-143",
     "quote": "this release proves only the Part-1 (L4) vertical slice"
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
   "statement": "Keep three layers of checking separate: the content files, what the student actually experiences at runtime, and the claims made about the course; passing one says nothing about the others.",
   "kind": "adopted rule",
   "found_by": "An evaluator gap analysis; schema-valid content was still not course-quality.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "52",
     "quote": "InceptBench should not overclaim runtime behavior or package truth."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "118",
     "quote": "document-integrity floor only, never a course-quality/child-readiness/outcome verdict."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    44,
    46
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Qualify every reviewer, human or model, on a blind test before treating their judgments as a standard; keep reviewing, adjudicating and signing off as separate roles, so no one certifies their own work.",
   "kind": "adopted rule",
   "found_by": "Reviewer-qualification rounds for a gold set failed, which set the role-separation rule.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0165-eppc-g3-reviewer-qualification-terminal-outcomes-human-next-gate.qmd",
     "lines": "113-114",
     "quote": "Familiarity with the project is not automatic qualification; the new blind result must demonstrate competence."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "157-158",
     "quote": "no lane can self-certify the whole course."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "For review purposes, 'student' means a real learner in the real delivery flow: below-level readers, language learners, keyboard and screen-reader users, frustrated and test-wise students, and those who click through or guess.",
   "kind": "adopted rule",
   "found_by": "A student-ready criticism framework, written after course packages were rejected.",
   "evidence": [
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
   "statement": "When one instance of a defect turns up, search the whole set and the sibling lessons for the same pattern before calling it a one-off.",
   "kind": "measured",
   "found_by": "A text-to-speech label trap and a give-away-cue class each recurred across lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "28",
     "quote": "census ALL colon-openers in the grade JSON rather than assuming a one-off"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0223-g3-review-rounds-and-tooling-2026-09-18-to-21.qmd",
     "lines": "37",
     "quote": "Class sweep (PARALLEL-LEAD / connective-tell rule) run over every grade"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Scan all student-facing text for internal contradictions: counts that don't match, one term with two meanings, instructions that don't fit the interaction, and references to things not on the page.",
   "kind": "measured",
   "found_by": "A scan of 3,003 strings; a modelled step said 'two strongest' but wrote one quote.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "65-66",
     "quote": "regex-hunting for number-word/countable-noun mismatches, same-term double-meanings, instruction/interaction-type mismatches, off-page references"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0223-g3-review-rounds-and-tooling-2026-09-18-to-21.qmd",
     "lines": "52",
     "quote": "L6 p14 I-do state[9] contradicted its own write-up"
    }
   ],
   "against": "The scan found 0 live contradictions after triage, so its value was as a guard rather than a finder.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Measure a generator's raw quality as one attempt per pre-registered input, with no retries, reranking, repair, caching, best-of-N or human picking, at a fixed sample size; report results from a curated bank separately.",
   "kind": "adopted rule",
   "found_by": "An AP question generator's headline '99%' was a best-of-N plus cache exploit, not the model generating.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "59",
     "quote": "one attempt, no retry, reranking, repair, cache substitution, rejection sampling, best-of-N, or"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "34",
     "quote": "The headline **\"99%\" was cache + best-of-N**"
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
   "statement": "Watch for fixes that pass a check by avoiding it, such as removing the source text so a leak probe is skipped; that is gaming the grader, not improving the item.",
   "kind": "measured",
   "found_by": "In the AP generator project, the MCQ score 'fix' was dropping the stimulus.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "27",
     "quote": "the grader's leak-probe is skipped. That's **grader-gaming**, not a provenance win."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Know what each evaluator measures; a general quality grader can give answer-leaking items top marks, so run leak, format and structure checks separately.",
   "kind": "measured",
   "found_by": "The quality grader scored answer-leaking items 1.0. 5,860 rows that passed two model graders failed deterministic structure checks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "47",
     "quote": "separate from InceptBench, which graded answer-leaking items 1.0"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd",
     "lines": "195",
     "quote": "Independent passage-blind review is still required; IB+Opus passing is not enough."
    }
   ],
   "against": "Passage-blind re-checks of items that passed both graders were once ruled redundant (kb-0071, a name-bearing path, not cited).",
   "adds_to_existing": [
    58,
    66
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never accept a producer's self-reported pass labels or fields (certification, length, reading level, verbatim spans); recompute them when the content arrives.",
   "kind": "measured",
   "found_by": "A substring 'verbatim' check was beaten by paraphrase. A recompute caught a leak the annotation hid.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "96",
     "quote": "`word_count`/Lexile and a 30-char substring \"verbatim\" check (defeated by paraphrase)."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "51",
     "quote": "trust the recompute, not the annotation"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd",
     "lines": "231",
     "quote": "Embedded `certification: pass/pass` is not enough."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17,
    43
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count a content bank by unique, eligible and independently certified items, not gross rows, and split evaluation sets so related items never land on both sides.",
   "kind": "measured",
   "found_by": "An AP corpus: a claimed 100,000 usable items was 49,571 unique and 0 certified. One generated question text recurred 1,475 times.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0170-apush-deliverable-shape-user-pause-checkpoint.qmd",
     "lines": "78",
     "quote": "The 100,000 unique/usable-sample claim is therefore rejected."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd",
     "lines": "104",
     "quote": "max_question_text_hash_reuse: 1475"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Plan generation for heavy discards, and require the producer's full trace of accepted and rejected outputs; the quality comes from the gates, not from trusting the generator.",
   "kind": "measured",
   "found_by": "Of 299 items that passed the with-text control, 113 were certified blind.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "26",
     "quote": "The questions were good because the generator was not trusted."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0067-g5-generator-pilot-intake-and-team-async-2026-06-23.qmd",
     "lines": "33",
     "quote": "accepted_and_rejected_generation_trace"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    39
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Qualify each generator model and version against your teaching rules separately; one model following the rules does not mean another will.",
   "kind": "measured",
   "found_by": "A rule-steering test across three model routes scored 60/140, 67/140 and 136/140.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd",
     "lines": "50",
     "quote": "OpenAI 60/140 and 0/20 robust clusters, Claude 67/140 and 0/20, DeepSeek 136/140 and 17/20"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
     "lines": "46",
     "quote": "every model/version requires conformance qualification"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    70
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give a writer model only the few rules that apply to the task at hand, not the whole rulebook; rule-following drops as instructions get harder.",
   "kind": "external research",
   "found_by": "Ye et al. 2026, https://aclanthology.org/2026.findings-acl.99/, cited in the policy-compiler proposal.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
     "lines": "73-74",
     "quote": "across 18 models, constraint adherence fell materially as instruction difficulty increased"
    }
   ],
   "against": "The same study found targeted training improved adherence (kb-0128 line 74).",
   "adds_to_existing": [
    62
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't let a model-judged check block content until its precision has been measured; a judge's failure mode is confident wrongness, which is worse than 'cannot tell'.",
   "kind": "measured",
   "found_by": "A judged key check, wired as a blocker, held back 8 of 12 lessons. A screenshot judge invented a defect and quoted it.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
     "lines": "132",
     "quote": "was wired as a blocker and held back 8 of 12 lessons on a question the judge was never shown the"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
     "lines": "77",
     "quote": "incompleteness**, which is worse for an automated gate than an honest \"cannot tell.\""
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    9,
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a judge chooses among candidates, 'none of these' must be a valid answer; forcing a pick returns the least-bad option.",
   "kind": "measured",
   "found_by": "Five judged choices with no no-match outcome forced the nearest wrong answer.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0190-jev-skills-and-engine-lane.qmd",
     "lines": "71-72",
     "quote": "`noMatch` is a real, valid answer — a search with no good hit should return zero results, not the least-bad one."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
     "lines": "1313-1314",
     "quote": "five choices with no no-match outcome, which were forcing the closest wrong answer"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    31
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Run on each item type only the checks written for it; a check built for one format produces spurious findings on another.",
   "kind": "measured",
   "found_by": "Multiple-choice checks run on cloze and highlight items flagged every page. An audio check written for one lesson's pattern misfired on the others.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
     "lines": "121",
     "quote": "types are not interchangeable (MCQ-style questions asked of cloze/hot-text items produced"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "90",
     "quote": "check written only for L4's syllable-breakdown pattern wrongly applied to L5/L6/L7's simpler vocab"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    30
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Treat any difficulty estimate made before an item is used as a provisional prior that records its method and how many responses it rests on; models misjudge difficulty because they cannot unlearn answers, so estimate from item features or calibrated anchors and replace with live data.",
   "kind": "external research",
   "found_by": "Cold-start difficulty BrainLift; Li et al. 2025, arXiv:2512.18880 (the 'curse of knowledge'); direct model ratings reach only r≈0.4-0.6.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "43",
     "quote": "scaling up model capability does not improve difficulty alignment with human learners — it often makes it worse"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "49",
     "quote": "Every pre-use difficulty value must travel with a provenance label (\"pre-use predicted, N=0\") and an uncertainty indicator"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "428",
     "quote": "If your new approach does not beat these, it is not adding value."
    }
   ],
   "against": "Simulated students tuned to item response theory are promising but not yet reliable as a primary signal (kb-0163 line 75).",
   "adds_to_existing": [
    37,
    47
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check that a model's judgment survives paraphrase; if small wording changes swing the result, distrust it.",
   "kind": "external research",
   "found_by": "Sarkar et al. 2025, ScoreCLIQ (AIED 2025; no DOI given): paraphrase-consistency training cut error by about 12%.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
     "lines": "65",
     "quote": "if small wording changes cause wild swings in your predicted difficulty, the prediction is probably wrong."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34,
    35
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Prefer authentic texts split into parts over model-written ones, and label machine-written texts honestly.",
   "kind": "adopted rule",
   "found_by": "Reviewer ruling on model-written fiction; an honesty correction about machine-written passages.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0198-meetings-decisions-timeline-0819-1001.qmd",
     "lines": "29-30",
     "quote": "LLM-generated fiction \"is never going to be great\"; real, split-into-parts texts are the priority"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
     "lines": "45",
     "quote": "don't relabel machine-authored cold passages as \"real.\""
    }
   ],
   "against": "Original passages written to spec passed review with a verdict of 'GREAT' (kb-0120 line 24).",
   "adds_to_existing": [
    23,
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Before a blind test, confirm the item can be answered with the text; failing with the text usually means ambiguity, and passing with the text does not predict blind safety.",
   "kind": "measured",
   "found_by": "417 of 1,152 failed the with-text control. Control pass rates did not predict blind certification.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "146",
     "quote": "The 417 with-passage control failures were often ambiguity or broad `Both` keying, not necessarily"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
     "lines": "40-41",
     "quote": "PASS if with-passage correct-rate >= 0.80 AND without-passage correct-rate <= chance-rate + 0.15 margin"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5,
    6
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Passing a leak test does not make an item good; separately check that it still tests the intended skill.",
   "kind": "measured",
   "found_by": "In an ordering pilot, all 13 items passed the blind gate and only 4 of 13 passed the quality review.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "127",
     "quote": "Lesson: anti-leak success alone is insufficient."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Item formats leak differently: single-choice items through general knowledge or a 'textbook-correct' option, multi-select through mutually reinforcing options, highlight items through stems that signpost the span, ordering items through events with a natural order. Design each against its own leak.",
   "kind": "measured",
   "found_by": "A generation retrospective measured blind-certification rates by format.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "208-210",
     "quote": "- MCQ leaked through ordinary school knowledge, vocabulary, or a \"textbook correct\" option; - MSQ leaked through mutually reinforcing correct options; - hot-text leaked when stem/span wording signposted the answer."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "214",
     "quote": "- failed when fragments had natural story/process order;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "In items asking which source states a detail, use neutral labels and topically balanced statements, so only reading the sources reveals which one says what.",
   "kind": "measured",
   "found_by": "This construction produced 700 certified items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
     "lines": "46-48",
     "quote": "- passage titles were not category labels; - statements were topically symmetric;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "If an item's answer is common general knowledge, no rewrite of the distractors can fix it; replace the content.",
   "kind": "measured",
   "found_by": "The one item rejected from a 20-item repair batch could be solved cold about 80% of the time.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "120",
     "quote": "general knowledge; distractor surgery can't close it, needs full content replacement"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Calibrate the blind solver itself: one that plays a test-wise student and bluffs inflates leak rates, while one allowed to answer 'unknown' gives an honest gate.",
   "kind": "measured",
   "found_by": "Switching solvers took blind accuracy from 1.0 to about 0.0 on 10 items, which were then certified clean.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "31",
     "quote": "- it returned blind accuracy of `1.0` on items that genuinely needed the passage."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
     "lines": "71",
     "quote": "3. A solver that responds `UNKNOWN` on true comprehension items gives a more honest gate."
    }
   ],
   "against": "The next candidate shows low-confidence correct answers can still be real leaks. The audited items included cues like 'correct answer is the longest' (kb-0096 line 56) that real students exploit.",
   "adds_to_existing": [
    5,
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Count a blind solver's exact correct answers as leaks even when it reports low confidence; self-reported confidence must not erase exact recoveries.",
   "kind": "measured",
   "found_by": "A sealed rule ignored an item solved exactly blind 3 of 8 times because the solver reported low confidence.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "44",
     "quote": "the sealed rule had ignored those hits because the solver reported low"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "59-60",
     "quote": "model self-confidence cannot erase exact blind recoveries"
    }
   ],
   "against": "A calibration note held that discarding low-confidence forced guesses was correct (kb-0100, name-bearing, not cited); see also kb-0096.",
   "adds_to_existing": [
    5,
    9
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test whether an item can be answered from texts in earlier lessons, not just with no text; knowledge carried forward can give away later answers.",
   "kind": "measured",
   "found_by": "One item was solved 0 of 3 times blind but 3 of 3 with the earlier lessons' texts; 9 of 70 showcase candidates leaked this way.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "32",
     "quote": "(choice-hottext-20: plain-blind 0/3 but 3/3 with prior-lesson corpus)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0098-incept-service-coe-catchup-2026-07-09.qmd",
     "lines": "39",
     "quote": "later questions become answerable from earlier lessons without proving true comprehension."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Fit the leak check to the subject: when the task is reading a text, finding the answer in it is the skill; in source-based history tasks, the answer appearing in the source counts as a leak.",
   "kind": "adopted rule",
   "found_by": "A leak-control schema for reading, contrasted with history (AP-style) source tasks.",
   "evidence": [
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
   "statement": "Test that what reaches the student's screen carries no answer keys, rubrics, feedback or teacher-only fields.",
   "kind": "adopted rule",
   "found_by": "An engine view test; an AP repair bucket required a student-only source view.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
     "lines": "50",
     "quote": "tested at every step to carry none of `answer_index`, `correct_indices`, `rubric`, `criteria`,"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "72",
     "quote": "metadata, excluding teacher-only answer-bearing fields."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A question that can be answered by matching words between the question and the text tests matching, not understanding; independent tasks must require real rereading.",
   "kind": "adopted rule",
   "found_by": "Reviewer meeting rule; a stem-leak checker.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "35",
     "quote": "The independent text/task must require genuine rereading rather than a visible word-match."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "92",
     "quote": "distinctive content word may sit in both the stem and only the correct option"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An inference item is invalid if the text states its conclusion outright, and a retrieval item is invalid if it secretly needs inference; check both directions, and word each item for the skill it really tests.",
   "kind": "measured",
   "found_by": "An integrity probe of 18 items found 1 'inference' whose answer the next sentence stated.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0231-pp-depth-6h-doc-diffs.qmd",
     "lines": "75",
     "quote": "behavior is fine — that's the clue; stating the trait/conclusion itself is a disguised-FIND"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "104-105",
     "quote": "a FIND question dressed as INFER (or the reverse) is a defect, not style"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    5
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Let taught knowledge recur and build up during learning, but keep scored assessment items separate from what was taught: connected while learning, unseen at the test.",
   "kind": "adopted rule",
   "found_by": "The deepest reviewer criticism was that unrelated texts everywhere engineered knowledge out of the course. The rebuilt course resolved it by separating roles.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "70",
     "quote": "Sequence the learning texts so taught knowledge recurs and compounds, and reserve cold, non-overlapping passages for the test only"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0074-g3-reviewer-feedback-distilled-for-g5-2026-06-30.qmd",
     "lines": "81-82",
     "quote": "\"Independent item claim_ids must be a subset of independent_claim_ids and disjoint from teaching_claim_ids\""
    }
   ],
   "against": "Knowledge carried forward can leak answers (kb-0098 line 39, kb-0120 line 32), and the 'disjoint' rule was verified only at design level (kb-0074 lines 86-88).",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check each item's declared skill or standard against what it actually assesses, including thinking level: 'identify' cannot assess 'analyze'.",
   "kind": "adopted rule",
   "found_by": "Reviewers found a main-idea lesson serving an inference item; evaluator gap analysis.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "122",
     "quote": "- N1: DOK-level alignment. Coverage is false if an \"analyze\" standard is assessed by \"identify.\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "92",
     "quote": "- Example found: a main-idea lesson served an inference/evidence item."
    }
   ],
   "against": "One cited mistag was defended as defensible (kb-0074 line 51).",
   "adds_to_existing": [
    49,
    63
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Include tasks that require combining several pieces of knowledge, not only one-at-a-time checks; students can master parts and still fail to combine them.",
   "kind": "adopted rule",
   "found_by": "Reviewer BrainLift; evaluator gap N8; an audit finding that no check required integrating both sources.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "123",
     "quote": "- Integrative lessons matter: students can master parts and still fail when asked to select, combine, or justify them in context."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "128",
     "quote": "- N8: integrative-assessment presence. Include tasks that coordinate multiple KCs, not only atomized checks."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Check the arithmetic of a pass threshold: on a short test, a 90% bar demands a perfect score.",
   "kind": "measured",
   "found_by": "Two 4-5 item tests could not be gated at 90%.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
     "lines": "37",
     "quote": "two 4-5 item tests are un-gateable (no \"90% of 4\")"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "141",
     "quote": "- gate-arithmetic trap where small tests make 90 percent require a perfect score;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check each item's scoring settings and its real chance of being guessed; a wrong setting can accept incomplete answers, and a one-of-four pick may be guessed blind often.",
   "kind": "measured",
   "found_by": "A matching setting accepted incomplete answers. Moving an item from a one-of-four pick to an exact two-span set cut blind guesses from 5/8 to 2/8.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "99-100",
     "quote": "right buckets keyed 2x with `match-max=1`, which would have let a spec-conformant renderer accept an incomplete response"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0134-g5-reading-v2-local-design-package.qmd",
     "lines": "99-100",
     "quote": "I03 had leaked through forced one-of-four guessing: 5/8 plain-blind exact guesses."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A retake needs new items (parallel forms) after reteaching; re-showing the same test measures memory of the items.",
   "kind": "adopted rule",
   "found_by": "The course evaluation lacked parallel forms. Direct Instruction rule: delayed test with new items.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0058-eval-reading-explorers-g3-allqtypes.qmd",
     "lines": "60",
     "quote": "**Author parallel forms per lesson test** (BLOCKING for hole-filling) — 2-3 forms each so three-state retry works"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "141",
     "quote": "- Require 90% to advance; if not met, give intensive instruction and a delayed test with new items."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    48
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Don't claim a practice or proxy test predicts the real test, or report on the real test's scale, until the same students have taken both close together; enforce that limit in code.",
   "kind": "adopted rule",
   "found_by": "The MAP proxy test had no outcome anchor (MAP 0/313 linked). The scorer blocked scale output until linked.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "63",
     "quote": "3. **No-RIT-pre-pilot is enforced in CODE**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "40",
     "quote": "- Honesty gate preserved in the email: no RIT output; engine physically will not emit RIT until linked to real MAP scores."
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
   "statement": "After items go live, review how they behave: fairness across groups, drift over time, and students stuck repeating failure. This is part of an item's life, not optional cleanup.",
   "kind": "adopted rule",
   "found_by": "Assessment BrainLift operational rules (Holland & Wainer 1993 on differential item functioning).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "99-100",
     "quote": "escalation are part of the lifecycle rather than optional cleanup."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0162-assessment-item-difficulty-evidence.qmd",
     "lines": "119",
     "quote": "an item’s difficulty may differ systematically across subgroups even when overall ability is matched."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When a distractor is built on a real misconception, follow it with corrective feedback or correction after the test, because a plausible wrong option can plant false knowledge.",
   "kind": "adopted rule",
   "found_by": "Assessment BrainLift rule.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "95-96",
     "quote": "post-test correction because plausible lures can seed false knowledge;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Declare each assessment's purpose (practice, mastery, diagnostic, summative or unseen-text measure) before reading its results; teaching checks and gated assessments are different things.",
   "kind": "adopted rule",
   "found_by": "Assessment BrainLift; a demo unit restructured to declare its teaching checks separately from its gated assessment.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "89-90",
     "quote": "- declare whether a resource is formative, mastery, diagnostic, summative, or cold measurement before interpreting its result;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
     "lines": "36-37",
     "quote": "l0-l3 now declare teaching-check / non-gating behavior; l4 is the gated interval assessment at 90%"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Before writing an assessment item, define the knowledge it targets, the claim, the evidence, the task conditions, the range of possible answers and the scoring rule.",
   "kind": "adopted rule",
   "found_by": "Evidence-centred design (Mislevy et al. 2003, https://doi.org/10.1002/j.2333-8504.2003.tb01908.x, cited at kb-0162 line 269); listed as an open authoring fix.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "84-85",
     "quote": "- no KC, claim, evidence indicators, task conditions, outcome space, and scoring rule means no assessment;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Match the task to the kind of knowledge: picking from options cannot show productive or explanatory knowledge, so a taught word counts as learned only when a graded task makes the student produce it.",
   "kind": "adopted rule",
   "found_by": "Taught words were never used on any graded task; assessment BrainLift rule.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "86-87",
     "quote": "- match the task family to the knowledge: recognition is not enough for productive, representational, justificatory, or integrative constructs;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "142",
     "quote": "MCQ recognition alone — however many options — never counts as a cash"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Mastery tests should use the formats students met during instruction.",
   "kind": "adopted rule",
   "found_by": "Direct Instruction BrainLift applied by reviewers.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "140",
     "quote": "- Mastery tests should match formats experienced during instruction."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "The right option must not stand out: not the longest, not the shortest, not the odd one out in form, not the one sharing most words with the question. Distractors should be plausible near-misses of the same length and grammatical form.",
   "kind": "adopted rule",
   "found_by": "Reviewers saw answers given away by length and phrasing. 626 generated rows failed the longest-option check.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "63-64",
     "quote": "The right option must not be the longest, the shortest, the odd one out, or the one that reuses the most words from the stem."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0223-g3-review-rounds-and-tooling-2026-09-18-to-21.qmd",
     "lines": "24",
     "quote": "option 2 reworded from a *the*-opener to match the wh-form distractors"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd",
     "lines": "117",
     "quote": "longest-option-tell: 626"
    }
   ],
   "against": "A re-calibrated blind solver cleared items flagged for 'correct is longest' (kb-0096 line 56).",
   "adds_to_existing": [
    6,
    8
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give choice items enough options that guessing rarely pays (four, not two; no yes/no questions), but never pad with weak filler distractors.",
   "kind": "adopted rule",
   "found_by": "Reviewer rule that two options make a 50/50 guess.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "80-81",
     "quote": "to prevent guessing\" — a two-option item is a 50/50 guess)"
    }
   ],
   "against": "kb-0164 lines 102-105: the MCQ BrainLift reports a research consensus favouring three options and says four only when every distractor stays plausible; filler must not be added.",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Review a test form as a whole: the answer to one item must not give away another, and answer positions, option lengths and blueprint coverage must balance across the form.",
   "kind": "measured",
   "found_by": "One word pair cracked both usage checks.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0211-peter-pan-reviewer-round-2708.qmd",
     "lines": "24",
     "quote": "Both usage checks were crackable via the single pair \"baby\"+\"sleep\""
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "93-94",
     "quote": "- answer position, option length, distractor function, enemy items, blueprints, and independent cold review are form-level obligations;"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    8,
    68
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Matching items need at least one unused option, or the last match comes free by elimination; the unused option must not be labelled as a decoy.",
   "kind": "measured",
   "found_by": "638 generated rows failed the unused-option check; 192 matching items announced their decoy.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0068-g5-static-dataset-intake-2026-06-23.qmd",
     "lines": "116",
     "quote": "unused-right-bucket-exists: 638"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
     "lines": "58",
     "quote": "192 match items announce a decoy bucket"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When students choose from excerpts of a text, list the excerpts in the order they appear in the text.",
   "kind": "adopted rule",
   "found_by": "A clue list out of text order sent a child backwards through the scene.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "39-40",
     "quote": "a `hot_text` question's tappable sentence list must be offered in the same order those sentences occur in the passage"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A test of a taught word must not put the word's root in its question, and its right answer must not just repeat the taught definition.",
   "kind": "adopted rule",
   "found_by": "A question template defined the affix inside its own stem; checkers for definition echo.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0059-map-equivalent-test-design-v4.qmd",
     "lines": "48-49",
     "quote": "pre-defined the affix in the stem"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "93-94",
     "quote": "DEFINITION-ECHO (a vocab-testing item's correct option must not just echo the taught definition)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    10
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Test every automated marker with the ideal answer; a guard against copying rejected word-perfect recall of the sentence the lesson taught.",
   "kind": "measured",
   "found_by": "An echo ratio of 0.74 against a 0.70 threshold. Before the fix, 3 of 117 judge cases were wrong, all in this class. Another judge accepted empty answers.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0229-closing-questions-build-2026-09-25.qmd",
     "lines": "78",
     "quote": "the gate was punishing the child for saying the taught sentence exactly."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "63",
     "quote": "oral/typed judges accept empty or content-blind answers."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    36,
    37
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Give the same verdict to an identical resubmitted answer: mark at the most deterministic setting and cache repeat submissions.",
   "kind": "measured",
   "found_by": "Reviewers saw the same typed answer get different results.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "39-40",
     "quote": "running the first judging attempt at the most deterministic model setting and caching identical resubmits to return the same verdict instantly."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A sentence frame must stay grammatical for every word a student might put in it; check frames with the blank filled in.",
   "kind": "measured",
   "found_by": "A frame broke grammatically once a student's word was filled in, and no validator caught it.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0238-l4-baseline-submission-and-signoff-packet-2026-08-31.qmd",
     "lines": "35-36",
     "quote": "which stays grammatical regardless of the filling word."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
     "lines": "37-38",
     "quote": "checks a lead's grammatical fit under substitution"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "A worked example must show the reasoning, including what was rejected and why, as an expert thinking aloud; it must not hand over a filled-in answer or make the thinking look easy.",
   "kind": "adopted rule",
   "found_by": "Reviewers likened a reveal-only model to copying a neighbour's work.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "32",
     "quote": "one, what was rejected and why — never just reveal a filled-in organiser."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "64",
     "quote": "Do not model the thinking as if it is easy."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Modelling, guided practice and independent practice must run the same skill with identically named steps, and the stages must be recognisable even with their labels removed; guided practice gives a partly finished answer for the student to complete.",
   "kind": "adopted rule",
   "found_by": "Reviewers found the routine misapplied. An audit found guided practice renamed three of four steps.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "35",
     "quote": "we-do, a fresh question is not a we-do); I-do, we-do and you-do must run the *same skill*, never"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "55",
     "quote": "**MAJOR — we-do renames three of the four I-do step labels (R-KC-11).**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "44",
     "quote": "that survive the strip-the-labels test"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40,
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Plan how support fades as students succeed, from heavy modelling to hand-over across a unit, and remove supports such as pre-highlighted candidates and stated counts in independent practice.",
   "kind": "adopted rule",
   "found_by": "Fading was never implemented beyond one lesson per level; an audit found independent tasks still pre-highlighted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
     "lines": "72-73",
     "quote": "exposure-based fade progression per skill (heavy model 5/2/1 → shift 3/2/3 → hand-over 1/2/5)"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0226-g3-pre-submission-closure-audit-2026-09-24.qmd",
     "lines": "41",
     "quote": "3. Independent Find pre-glows candidates and states the count (L5-L7), where the design wants an open hunt"
    }
   ],
   "against": "The rule was never implemented or measured (kb-0180 lines 41-44).",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When modelling, say what you will do, show it done, then check; show nothing before it has been thought aloud, keep one target of attention at a time, and keep the steps and the live question visible.",
   "kind": "adopted rule",
   "found_by": "Reviewer docs on modelling choreography; steps that scrolled away lost the student.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0174-august-consolidation-and-scout-lesson-feedback.qmd",
     "lines": "62-63",
     "quote": "then the check; nothing on screen before it is thought aloud; feedback finishes before the next step renders; one attention target at a time; only the current sentence highlighted."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "84",
     "quote": "The steps and live question must remain visible, and the model should surface one thing at a time"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    21,
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every screen should ask for a response that serves the teaching move; a decorative tap or skippable nudge doesn't count, and students must not be able to speed through narration they need to hear.",
   "kind": "adopted rule",
   "found_by": "Reviewers found passive screens and a skippable attention nudge.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "27",
     "quote": "a decorative tap control does not satisfy the concern"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "130",
     "quote": "- Keep passive episodes short and make active checks consequential; skippable \"pause and think\" is not a check."
    }
   ],
   "against": "Some reviewers worried that too many checks become compliance rather than learning (kb-0212, name-bearing, not cited).",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Break up any long video that carries essential content with required quick checks.",
   "kind": "adopted rule",
   "found_by": "Reviewer meeting feedback; Szpunar, Khan & Schacter 2013, https://www.pnas.org/doi/pdf/10.1073/pnas.1221764110.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "31",
     "quote": "If video carries essential context, interrupt it with mandatory quick checks so the learner does not watch a long unexamined clip."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0248-g9-video-research-full-files.qmd",
     "lines": "211-212",
     "quote": "Interpolated memory tests inserted into recorded lectures cut mind-wandering by roughly a third and improved recall versus uninterrupted video."
    }
   ],
   "against": "The intro-video BrainLift bans questions after a preview that signal which story threads matter (kb-0220 line 23).",
   "adds_to_existing": [
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Practise a new skill in a block first, and mix it in with other skills only once it is ready.",
   "kind": "adopted rule",
   "found_by": "Practice BrainLift applied by reviewers.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "160",
     "quote": "- Interleaving is only appropriate after the skill is ready; massed/blocked first, interleaved later."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give less feedback as proficiency grows; too much feedback reduces active thinking.",
   "kind": "adopted rule",
   "found_by": "Practice BrainLift applied by reviewers.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "161",
     "quote": "- Too much feedback can reduce active processing; feedback timing should shift as proficiency improves."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Keep several strands going at once, with only one introducing new material while the rest review (about 90:10 review to new).",
   "kind": "adopted rule",
   "found_by": "Direct Instruction BrainLift; built into the teacher skill's workflow.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "145",
     "quote": "- Keep multiple tracks alive over time; only one track should introduce new material while the rest is review."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0123-teacher-g3-reading-candidate-skill.qmd",
     "lines": "43",
     "quote": "lesson composition as interleaved tracks at ~90:10 review:new"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "After an error, correct it briefly, send the student to the taught check for that skill, and retest later with different items or evidence.",
   "kind": "adopted rule",
   "found_by": "Direct Instruction BrainLift; an AP course repair rule.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "143",
     "quote": "- Error correction should be immediate and brief: correct, test, give intervening items, then retest later."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "67-68",
     "quote": "4. Rebuild every assessment and writing criterion as failed function -> relevant taught check -> different-evidence retry."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    4
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Independent tasks must not reuse the answer-bearing evidence the worked example already used; require new evidence.",
   "kind": "measured",
   "found_by": "An independent audit of the AP course blocked replication over this in three lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "64",
     "quote": "2. Replace independent tasks that reuse answer-bearing modeled evidence in Lessons 1, 3, and 6."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    41
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every activity should state its rationale (the target knowledge and performance, the failure it guards against, why this activity, when its support is withdrawn), and every assessment item should justify its format.",
   "kind": "adopted rule",
   "found_by": "Generic Instruction BrainLift; a lesson-plan validator rule.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "134",
     "quote": "- Any activity needs a rationale: target knowledge type, performance, failure mode it protects against, why this activity, and scaffold retirement condition."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0189-validators-and-laws.qmd",
     "lines": "37",
     "quote": "every assessment item argues its format"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Standards set scope, not sequence: build an explicit progression spine (entry assumptions, prerequisites, source ladder, evidence model), and link units by their big ideas rather than surface facts.",
   "kind": "adopted rule",
   "found_by": "Curriculum & Knowledge BrainLift; reviewers wanted deeper links between units.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "119",
     "quote": "- Standards constrain scope but do not provide a teachable sequence."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "121",
     "quote": "- A course needs an explicit progression spine, entry assumptions, prerequisite policy, source ladder, and evidence model."
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
   "statement": "Give a purpose for reading before the text, and reread chosen parts for that purpose instead of rereading the whole text by habit.",
   "kind": "adopted rule",
   "found_by": "Reviewer feedback on lessons with no stated purpose; a rereading rule from a reviewer meeting.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "61",
     "quote": "Children need a reason to read before they start"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "93",
     "quote": "4. Rereads point to a text subset for a declared knowledge purpose rather than replaying a whole text by habit."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    40
   ],
   "name_bearing_source": false
  },
  {
   "statement": "When a task asks for evidence from a text, keep the text visible.",
   "kind": "adopted rule",
   "found_by": "Reviewers found the passage hidden at the moment students had to cite it.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "86",
     "quote": "   - Prompts ask for textual evidence, but the passage is hidden when the student needs to cite it."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    7
   ],
   "name_bearing_source": false
  },
  {
   "statement": "An inference task may rely only on what the text and lesson have given, never on outside cultural knowledge students may lack.",
   "kind": "adopted rule",
   "found_by": "A worked example was struck because it needed knowledge of a foreign city.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0180-lesson-structure-procedure-rulings.qmd",
     "lines": "81",
     "quote": "inference may only use what the passage's own words show; extension deepens the mood from"
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
   "statement": "Don't teach rules of thumb that many texts break (titles state the main idea, the main idea lives in one sentence, hunt for keywords), and don't teach that evidence is always one sentence.",
   "kind": "adopted rule",
   "found_by": "Reviewers rejected a lesson's main-idea shortcuts.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "73",
     "quote": "- Titles frequently do not state the main idea, so checking against the title is not a dependable rule."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "80",
     "quote": "The lesson may also embed the misconception that text evidence always points to one sentence."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Choose texts for a knowledge sequence, genre balance and quality, judging complexity by reading it rather than by a readability number alone, and include longer and paired texts that build stamina.",
   "kind": "adopted rule",
   "found_by": "A reviewer found passages of 58-217 words against a state test of about 2,740; the team accepted.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "78",
     "quote": "Choose texts for a coherent knowledge sequence and a genre balance that includes poetry, drama and more literary work, and judge complexity qualitatively as well as by Lexile."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "94",
     "quote": "Course passages run 58 to 217 words, averaging about 166."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Help comes only after an attempt, and hints escalate from criterion cues; only the last hint names the evidence's own words.",
   "kind": "adopted rule",
   "found_by": "Reviewers warned that instant hints remove desirable difficulty. A check found nudges naming the key.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "43",
     "quote": "The durable rule is attempt first, then targeted help."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "53-54",
     "quote": "reword to criterion cues, naming a clue's actual words only in the *last* nudge"
    }
   ],
   "against": "The exact trigger count for help (for example, three errors) was never settled (kb-0172 line 43).",
   "adds_to_existing": [
    1,
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check every line around a question for the answer (instructions, praise, nudges, replies to a student who is unsure), not only the replies to wrong answers.",
   "kind": "measured",
   "found_by": "Praise and nudge lines handed over answers; a reply to an unsure student repeated the key verbatim (overlap 1.00).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "129-130",
     "quote": "nudge/instruction lines on L4 p22, L5 p15b/p16, L6 p15b, L7 p16 were handing over the Step 3-4 answer outright"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0224-g3-dialogue-branches-pace-gate-roll-forward-2026-09-22-23.qmd",
     "lines": "58",
     "quote": "our L4 silent branch was at **1.00** overlap (verbatim echo)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1,
    3
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Feedback and summaries must be true to what the page offers and what the student did: no promised replay that doesn't exist, no canned line posing as a response, no claim of work the student didn't do.",
   "kind": "measured",
   "found_by": "Audit findings F14 and F15; a 'Listen again' reply on a page with no audio.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "70",
     "quote": "The welcome beat overclaims contingent listening while still issuing a static, answer-independent recast"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
     "lines": "45",
     "quote": "the L4 video \"Listen again\" false-promise fix"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    1
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Keep corrective feedback shorter and simpler than the teaching it supports; feedback longer than the passage has turned into new instruction.",
   "kind": "adopted rule",
   "found_by": "Reviewers found feedback longer than the passage; Practice BrainLift boundary rule.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "96-97",
     "quote": "if corrective feedback is longer or more complex than the original instruction, the item has crossed into new instruction."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
     "lines": "59",
     "quote": "it is too long, sometimes longer than the passage, and has basic capitalization defects."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Cap every sentence a student must act on (instructions, questions, hints, feedback) at about 25 words, leaving the source text and taught frames exempt, and apply the same cap to feedback generated live.",
   "kind": "adopted rule",
   "found_by": "An age-appropriateness review that cited sentence-length research.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "97",
     "quote": "25 words a sentence, maximum"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0183-copy-question-quality-rulings.qmd",
     "lines": "109-110",
     "quote": "since no static validator can see a line that does not exist until a child answers."
    }
   ],
   "against": "Older students: a register cap of 40 words, never over 60, was used for feedback (kb-0195 line 69).",
   "adds_to_existing": [
    26,
    29
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every claim a lesson makes about a text, whether causes, motives, absolutes or 'the text says…', must trace to the text's own words; check unquoted attributions as strictly as quotes.",
   "kind": "measured",
   "found_by": "The one critical audit finding was an invented cause shown to students as a fact from the text.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0232-l4-audit-nine-principles.qmd",
     "lines": "48-49",
     "quote": "exact defect class (grounding inference in invented rather than real textual evidence) the lesson exists to teach the child to avoid."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "79",
     "quote": "phrasing — the shape that hides the worst defects, since unquoted claims look like nothing)."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    17
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Any line referring to earlier or later material must be true to the actual order, and no question, option or hint may depend on something the student hasn't reached yet.",
   "kind": "adopted rule",
   "found_by": "Evaluator gap N2; a forward-reference checker.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "123",
     "quote": "- N2: relational-reference factuality. \"As you saw last lesson\" claims must be true against order."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
     "lines": "86-87",
     "quote": "a question/option/hint on page N must not depend on a concrete story noun the child has not read yet"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    7,
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "List the misconceptions each unit must avoid, and check every text that carries subject content against expert misconception lists, even in another subject's course; keep observation, theory, interpretation and opinion distinct.",
   "kind": "adopted rule",
   "found_by": "Reviewers supplied science misconception lists; a later run found 22 serious misconception hits across 8 lessons.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "48",
     "quote": "4. apply the misconception-check process to every science-bearing Read/Write text;"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0164-g3-v2-feedback-agent-routing.qmd",
     "lines": "49-50",
     "quote": "5. distinguish observation, hypothesis, theory, consensus, measurement, interpretation, and opinion accurately."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
     "lines": "84-85",
     "quote": "22 Tier-1 misconception hits across 8 lessons"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "When students work from primary sources, show each source's author, purpose and accurate citation.",
   "kind": "measured",
   "found_by": "An independent semantic audit of the AP course required this before replication.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "66",
     "quote": "Casas's reform-advocate purpose to student-visible citation context."
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Teach a concept with an example and a non-example that differ only in its defining feature, each saying why.",
   "kind": "adopted rule",
   "found_by": "A reviewer rule enforced by validator (after Engelmann).",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "33-34",
     "quote": "example and non-example differ in only the one defining feature, and the non-example states why it fails"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Define each taught term one way and use that exact definition everywhere it appears, and make words taught together clearly distinct in meaning.",
   "kind": "adopted rule",
   "found_by": "Reviewers found overlapping taught words; a word was taught with two meanings across a lesson.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "38",
     "quote": "One definition per word, used everywhere it recurs"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "105",
     "quote": "- Choose distinct vocabulary words."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18
   ],
   "name_bearing_source": false
  },
  {
   "statement": "A taught word needs many later encounters to stick, so plan its reappearances; meet that need in the activities, never by editing an approved source text.",
   "kind": "measured",
   "found_by": "7 of 9 taught words appeared only once; reviewer rule of 10-12 encounters.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
     "lines": "65-66",
     "quote": "from 7/9 taught words appearing only once"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "49-50",
     "quote": "Never edit the academics' story to satisfy this rule."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    18,
    23
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Support every hard word in a text (let students hear it and see its meaning), not just the taught words, and don't let a check hinge on vocabulary the student hasn't been given.",
   "kind": "adopted rule",
   "found_by": "Reviewers found hard passage words left undefined; evaluator gap N5.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0136-g3-reading-v2-reviewer-feedback.qmd",
     "lines": "107",
     "quote": "- Make difficult words tappable and readable aloud—\"hear it, say it, map it\"—for students who cannot yet decode them."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0093-evaluator-gap-analysis-inceptbench-academics-2026-07-09.qmd",
     "lines": "126",
     "quote": "- N5: linguistic validity. Untaught vocabulary or syntax can create construct-irrelevant difficulty."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    20
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Verify word-part breakdowns and pronunciations against reference sources, never by intuition.",
   "kind": "measured",
   "found_by": "A morpheme tool flagged 5 of 23 authored word-part splits, including a wrong base word.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "50",
     "quote": "to all 23 authored vocab decompositions; 5 flagged for review"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "96-97",
     "quote": "look up dictionary IPA (Wiktionary + Merriam-Webster), never guess"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    57
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Ask one thing per turn and one question per screen, so feedback can address each part and nothing overflows.",
   "kind": "adopted rule",
   "found_by": "Reviewer rule on two-part vocabulary turns; two stacked questions overflowed the screen.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0181-vocabulary-rulings.qmd",
     "lines": "55-56",
     "quote": "complicates simultaneous feedback if a child gets both parts wrong"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "109-110",
     "quote": "two MCQs stacked on one page"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    26
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Media shown before a text must set it up without spoiling or contradicting it.",
   "kind": "adopted rule",
   "found_by": "Reviewer feedback; an opening image showed a character before the text introduced him.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0210-aladdin-2508-feedback-and-pr27-safety-snapshots.qmd",
     "lines": "32",
     "quote": "Video 2 = text setup, no spoilers"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
     "lines": "69",
     "quote": "**L1 p8 opening image is a spoiler**"
    }
   ],
   "against": "Reviewers later agreed intro videos may reveal plot and characters (kb-0220 lines 45-47).",
   "adds_to_existing": [
    21
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Diagrams and pictures must not reveal the answers to the questions they support, and every diagram needs an accessible text or table equivalent.",
   "kind": "measured",
   "found_by": "A diagram printed its own key, letting students pass without reading.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "57",
     "quote": "prints its own answer key in-diagram"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
     "lines": "67",
     "quote": "The diagram is not element-addressable and has no accessible table equivalent."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    3,
    27,
    64
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Generated human figures must not look machine-made, because students dismiss 'fake AI'; if they can't pass, stylize away from realism or cut their screen time, and judge near-photoreal faces by three independent reads.",
   "kind": "adopted rule",
   "found_by": "A video ruling; calibration of the 'looks AI-made' art check.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0207-memory-digest-project-reference-user.qmd",
     "lines": "3931",
     "quote": "- If a human cannot be made to pass, prefer stylization away from realism (more cartoon, less"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0219-watch-48h-and-art-qa-redcontrol.qmd",
     "lines": "91-92",
     "quote": "any near-photoreal human face now requires three independent reads with majority rule"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    22,
    34
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Never ship placeholder-looking elements; if the real asset isn't available, redesign without it and note the omission.",
   "kind": "adopted rule",
   "found_by": "An emoji stood in for character art.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0207-memory-digest-project-reference-user.qmd",
     "lines": "2390",
     "quote": "never ship placeholder-looking elements; if an asset can't be obtained, admit it in notes and redesign the layout honestly instead"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Give the text reader and the teacher different voices, keep each role's voice the same across lessons, and stamp every clip with its generator and voice; a text check cannot hear a wrong voice.",
   "kind": "measured",
   "found_by": "Wrong-voice clips passed every automated check.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0182-audio-voice-rulings.qmd",
     "lines": "58-59",
     "quote": "keeping the two voices distinct is how a student hears 'the story' and 'the teaching' as separate things."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "45-46",
     "quote": "a correctly-worded clip in the wrong voice passes every automated check."
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    25,
    50
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Set each course's register (tone, praise, feedback length, voice and pace) for its own learners, and never let it default to another age group's settings.",
   "kind": "measured",
   "found_by": "An older grade nearly shipped read in a younger grade's storytime voice.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "76-77",
     "quote": "reading about salinity gradients would have been read to as if this were a bedtime story"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0195-g5-book-lane-secret-garden-closed.qmd",
     "lines": "69",
     "quote": "medals/confetti) — specific process praise instead; feedback ≤40 words (never >60), one"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    2
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Narration must never say words the page doesn't print, and any narration or video that gates progress needs captions taken from the approved script.",
   "kind": "measured",
   "found_by": "Two pages drifted into paraphrasing their own script (16 lines) while every other validator passed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "155-156",
     "quote": "two pages had drifted into a paraphrase of their own spoken script, 16 lines between them, while every other validator passed."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0194-g3-book-audio-clip-conventions.qmd",
     "lines": "187-188",
     "quote": "captions are the only way through for a child who cannot hear"
    }
   ],
   "against": "The rule runs one way: a page may print words that are not spoken (kb-0194 lines 151-153).",
   "adds_to_existing": [
    21,
    27,
    53
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Every interaction must work by keyboard and assistive technology with a capped number of options, and check what each quality rule does to accessibility.",
   "kind": "measured",
   "found_by": "Reviewers found 12 selectable options and non-keyboard items; a leak-resistance rule pushed 525 of 772 items into the least accessible formats.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
     "lines": "128",
     "quote": "one hot-text item offered twelve selectable options, an excessive motor and cognitive load for an eight-year-old."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0085-g5-red-team-findings-2026-07-06.qmd",
     "lines": "25",
     "quote": "RT-2 accessibility: anti-leak concentrates items into TEI formats (525/772), no"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    27
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Check content with the delivery system's own logic, not an approximation; content that is valid as text can still fail on screen, and a text search can't answer questions about structure.",
   "kind": "measured",
   "found_by": "Clue spans that existed in the text never lit up; text searches gave wrong answers three times.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
     "lines": "111-112",
     "quote": "`validate-passage-refs` only proves the span text is a SUBSTRING of the passage; it does not run the engine's own unit-boundary logic"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
     "lines": "1211",
     "quote": "A substring search is not a structural test."
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
   "statement": "Certify an item format only once it has been rendered and answered live; a form can pass every check and still be impossible to deliver or answer.",
   "kind": "measured",
   "found_by": "In production no non-choice format had ever rendered. A renderer could not accept a two-span answer.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0072-learnings-from-incept-map-proxy-2026-06-25.qmd",
     "lines": "70-71",
     "quote": "we can fully certify a form that **physically cannot be delivered**"
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0134-g5-reading-v2-local-design-package.qmd",
     "lines": "110-111",
     "quote": "all hot-text items were hardcoded as radios, so a two-span key was impossible to submit"
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
   "statement": "Keep unlabelled reviewer or test shortcuts that bypass gates out of students' reach.",
   "kind": "measured",
   "found_by": "A UI audit found an unlabelled reviewer-mode toggle open to students.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0179-g3-peter-pan-close-out-state-and-reusable-process.qmd",
     "lines": "35-36",
     "quote": "reviewer-mode toggle behind `?review=1` / `NEXT_PUBLIC_REVIEWER_UI`, red-first test)"
    }
   ],
   "against": "none found",
   "adds_to_existing": [
    28
   ],
   "name_bearing_source": false
  },
  {
   "statement": "Confirm the rights and permitted use of any third-party teaching material or excerpt before using it.",
   "kind": "adopted rule",
   "found_by": "Teacher decks and exemplar transcripts were offered without clear rights; excerpt-rights checks became a gate.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0172-g3-reading-course-feedback-2026-08-04.qmd",
     "lines": "65",
     "quote": "Confirm receipt, rights, and permitted use before placing any material in a training corpus."
    },
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
     "lines": "75",
     "quote": "NPS excerpt-rights confirmation"
    }
   ],
   "against": "none found",
   "adds_to_existing": [],
   "name_bearing_source": false
  },
  {
   "statement": "Should comprehension questions be asked during reading or only after it? One study found mid-text inferential questions cut recall, while interpolated tests in video improved it.",
   "kind": "open question",
   "found_by": "A reviewer cited Van den Broek 2001 (no DOI given); the issue was marked ruling-needed.",
   "evidence": [
    {
     "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
     "lines": "43",
     "quote": "inferential questions cut grade-4 recall .30->.07; her rule is ask AFTER not DURING reading, a"
    }
   ],
   "against": "kb-0248 lines 211-213 (Szpunar et al. 2013, https://www.pnas.org/doi/pdf/10.1073/pnas.1221764110) found interpolated tests improved recall in recorded lectures.",
   "adds_to_existing": [
    7
   ],
   "name_bearing_source": false
  }
 ],
 "evidence_for_existing": [
  {
   "truth": 4,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0192-g3-book-component-catalogue.qmd",
   "lines": "40-46",
   "quote": "a single-select answer is never revealed, even after many tries — the option list is short and exhausting it finds the answer"
  },
  {
   "truth": 4,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0081-g3-reviewer-feedback-raw-2026-07-02-reading-explorers-v2-review-verbatim.qmd",
   "lines": "50",
   "quote": "a wrong answer returns only \"Good try, let's look again,\" with no explanation and no correct answer shown."
  },
  {
   "truth": 7,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
   "lines": "43",
   "quote": "inferential questions cut grade-4 recall .30->.07; her rule is ask AFTER not DURING reading, a"
  },
  {
   "truth": 5,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
   "lines": "66-67",
   "quote": "(~78% of raw generated items were blind-solvable before this gate"
  },
  {
   "truth": 5,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0096-fable-vs-haiku-strictness-audit-2026-07-09.qmd",
   "lines": "72",
   "quote": "4. Passage-dependent items can look \"kid-gameable\" under the wrong blind-solver and still be clean."
  },
  {
   "truth": 6,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0223-g3-review-rounds-and-tooling-2026-09-18-to-21.qmd",
   "lines": "30-31",
   "quote": "explicitly **not** the report's own suggested fix (a plant nursery is itself a correct use of the word)."
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0187-skill-catalogue-and-workflows-index.qmd",
   "lines": "97",
   "quote": "\"first run caught a recurring rail defect and a 72.5% answer-position skew.\""
  },
  {
   "truth": 8,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "56",
   "quote": "Key-position/length balance needs an authoring-time check (12/19 A-keys shipped before the lens)."
  },
  {
   "truth": 9,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0190-jev-skills-and-engine-lane.qmd",
   "lines": "80-81",
   "quote": "each check returns `holds` / `fails` / **`unclear`**, and `unclear` is not a pass."
  },
  {
   "truth": 10,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0237-u4l2-carbon-copy-build-2026-08-13-to-08-21.qmd",
   "lines": "72",
   "quote": "The local evaluation fallback grades free responses by keyword overlap, and a porting note propagates that defect."
  },
  {
   "truth": 10,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0218-devfactory-review-and-decision-brief-2026-09-10.qmd",
   "lines": "25",
   "quote": "Misspelled \"magician\" marked correct; decide a comprehension spelling policy"
  },
  {
   "truth": 11,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0236-g5-package-build-facts-and-g3-fixlist-apply-2026-07-02.qmd",
   "lines": "40-41",
   "quote": "a short typed justification that is logged, not auto-graded"
  },
  {
   "truth": 12,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0190-jev-skills-and-engine-lane.qmd",
   "lines": "35-36",
   "quote": "will judge injected user text as if it were yours — quarantine it."
  },
  {
   "truth": 17,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
   "lines": "66-67",
   "quote": "the model fabricated a second occurrence it then quoted back verbatim"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
   "lines": "1282-1283",
   "quote": "image with a 0.46 match was being served (pictures now need positive evidence, accepted count fell 16 → 9)"
  },
  {
   "truth": 22,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0200-content-audio-review-traps.qmd",
   "lines": "59-60",
   "quote": "the model drifts on count once past roughly four figures"
  },
  {
   "truth": 23,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0198-meetings-decisions-timeline-0819-1001.qmd",
   "lines": "92",
   "quote": "(a 1-minute cut lost cohesion)"
  },
  {
   "truth": 24,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0222-g3-l4-l1-parity-rebuild-2026-09-17-to-21.qmd",
   "lines": "96",
   "quote": "voice-provenance and voiceover-sync were all green because none of them opens the file."
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0215-g5-media-recovery-plan-and-edullm-entrypoint-test.qmd",
   "lines": "86",
   "quote": "reached \"Great Work!\" across all 18 of U1·L3's scenes with **zero answers given**"
  },
  {
   "truth": 28,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0213-qc-week-0902-0904.qmd",
   "lines": "20",
   "quote": "comprehension check was silently optional while every sibling page gates."
  },
  {
   "truth": 29,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
   "lines": "62-63",
   "quote": "Their 40-student design-science pilot reported more consistent scaffolding and less premature answer-giving."
  },
  {
   "truth": 31,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
   "lines": "112-114",
   "quote": "(a wide N-way choice never clears the 0.15 margin gate)"
  },
  {
   "truth": 32,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0190-jev-skills-and-engine-lane.qmd",
   "lines": "92-93",
   "quote": "used AS the detector on raw items, it flagged 47% of items nobody had ever complained about"
  },
  {
   "truth": 33,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
   "lines": "145-146",
   "quote": "traced to one broken check (`JUDGE-ANSWERABLE` firing on 77 of 78 items because it was shown a bare stem with no passage/options)"
  },
  {
   "truth": 35,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
   "lines": "84",
   "quote": "same-model resamples (agreement = self-consistency, not cross-family agreement)"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
   "lines": "144-145",
   "quote": "First run: recall 0.625 but a **98.6% false-positive rate**"
  },
  {
   "truth": 37,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0217-team-direction-2026-09-09.qmd",
   "lines": "47-48",
   "quote": "38% is the first point on the curve; no pipeline seat until it beats the frontier-model critic on a real round."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0208-handover-archive-all.qmd",
   "lines": "32-34",
   "quote": "run on the arrival page — a false 15/15 clean). Lens now builds paths and asserts the landed page id."
  },
  {
   "truth": 38,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0196-engine-reading-game-engine-jev.qmd",
   "lines": "150-151",
   "quote": "`JUDGE-GRADE` had fired zero times across both runs"
  },
  {
   "truth": 39,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0243-generator-quality-schema-cluster-2026-07.qmd",
   "lines": "54-55",
   "quote": "adversarially recomputed from the raw per-call JSONL (not trusted from the run harness's own summary)."
  },
  {
   "truth": 41,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0083-clone-lessons-inceptbench-results-2026-07-02-eval-summary.qmd",
   "lines": "64",
   "quote": "Non-repetitiveness is by far the weakest dimension: **avg 0.14; 65 of 76 bundles scored exactly 0** on it."
  },
  {
   "truth": 43,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0091-g5-question-generation-retrospective-codex-2026-07-09.qmd",
   "lines": "231",
   "quote": "3. Use a different family for the gate than for the author. Never same-family certify."
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0245-coe-sync-2026-08-31-cert-layer-portal-fixes.qmd",
   "lines": "34-35",
   "quote": "**26 of [name]'s findings landed on lessons the calibration log marked green at review time**"
  },
  {
   "truth": 44,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0167-portable-workspace-checkpoint-apush-g5.qmd",
   "lines": "56",
   "quote": "That green state is not the semantic verdict."
  },
  {
   "truth": 45,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0168-eppc-bias-experiment-terminal-kill-and-salvage.qmd",
   "lines": "61-62",
   "quote": "\"inconclusive therefore continue\" outcome."
  },
  {
   "truth": 46,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0120-rivers-demo-unit-live-2026-07-13.qmd",
   "lines": "54-55",
   "quote": "Publish-time flattening created NEW defects the local lint could not see"
  },
  {
   "truth": 47,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0163-cold-start-item-difficulty-estimation.qmd",
   "lines": "75",
   "quote": "even sophisticated persona prompting cannot fully overcome the Curse of Knowledge"
  },
  {
   "truth": 48,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0086-round2-feedback-brainlifts-2026-07-09.qmd",
   "lines": "159",
   "quote": "- Same-day testing after practice measures working memory more than long-term memory."
  },
  {
   "truth": 50,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0230-late-sept-incidental-findings.qmd",
   "lines": "29-30",
   "quote": "review clips have no `audio_of` sha256, so a text edit (e.g. a definition rewording) leaves the clip silently stale"
  },
  {
   "truth": 51,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0162-assessment-item-difficulty-evidence.qmd",
   "lines": "140",
   "quote": "Warns us not to rely on students’ subjective ease or fluency as indicators of mastery"
  },
  {
   "truth": 55,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0192-g3-book-component-catalogue.qmd",
   "lines": "74-75",
   "quote": "after 4 wrong taps, Scout offers to find the remaining clues"
  },
  {
   "truth": 57,
   "effect": "counter",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
   "lines": "24-25",
   "quote": "On the **binding grader** it **collapsed to ~28%**"
  },
  {
   "truth": 58,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
   "lines": "39-41",
   "quote": "the class of defect that \"passes item evals but fails the holistic course eval.\""
  },
  {
   "truth": 59,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0234-misc-artifacts-gate-eval-checks-recovery.qmd",
   "lines": "31",
   "quote": "veto** caps the score at 0.84 if any CRITICAL metric is 0"
  },
  {
   "truth": 63,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0186-scope-lane-and-model-routing-rules.qmd",
   "lines": "50-51",
   "quote": "before citing reviewer feedback, confirm which course/artifact it was actually about"
  },
  {
   "truth": 66,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0064-insight-stimulus-provenance-unlock.qmd",
   "lines": "24",
   "quote": "That **0.29→0.95** jump existed only under a **discredited Gemini judge**."
  },
  {
   "truth": 67,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0199-engineering-git-gate-traps.qmd",
   "lines": "149",
   "quote": "**Root cause:** a prompt instruction is not a write guard"
  },
  {
   "truth": 70,
   "effect": "supports",
   "path": "~/Projects/grade3-reading/knowledge_bot/knowledge/kb-0128-externalized-pedagogy-policy-compiler-decision.qmd",
   "lines": "100",
   "quote": "a one-rule edit causes unrelated behavior changes, kill it as the primary control plane"
  }
 ]
}
```
