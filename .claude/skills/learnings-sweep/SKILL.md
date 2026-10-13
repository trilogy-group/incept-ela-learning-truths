---
name: learnings-sweep
skill_name: learnings-sweep
version: 1.3.0
description: Run a research sweep for ~/Projects/learning-truths, the AP, Grade 9 and Grade 3 learnings place: triage sources, sweep them with read-only agents and an adversarial verifier, record the run in full, merge findings into standard records with every quote checked, build, check, show, push.
trigger: Use when asked to scour, sweep or mine a source (a repo, a cloud folder, an export, a knowledge store) for learnings about making questions and lessons, or to add learnings to learning-truths. Also when the user says "do another sweep", "scour these", "add these learnings".
---

# learnings-sweep: scour sources into standard learnings

The repository is `~/Projects/learning-truths` (github.com/StanHus/learning-truths, private). Its goal: an
understanding of what a perfect question is, and of how to generate perfect questions. Read its `CLAUDE.md` first; the
bar, the record format and the house rules are there. Register the work in the control center (`mgr start`) before
starting, and log as you go.

Everything below lives in the repository:

| what | where |
|---|---|
| sweep workflow | `.claude/workflows/learnings-sweep.js` (readers, verifiers, critic, gap round, synthesis into records) |
| merge workflow | `.claude/workflows/learnings-merge.js` (free-text findings into standard records) |
| review workflow | `.claude/workflows/learnings-review.js` (a run's new records against the standard; duplicates across sections) |
| map candidate folders | `scripts/triage.py` |
| build the sweep's args | `scripts/sweep_args.py` |
| record a run | `scripts/record_workflow.py` (workflow runs), `scripts/record_sweep.py` (single agents) |
| write findings into records | `scripts/add_records.py` (checks every quote; maps evidence to registered sources) |
| check quotes by hand | `scripts/verify_quotes.py` |
| build and check | `scripts/build.py`, `scripts/check.py` |
| the run standard | `schema/RUNS.md`, `schema/run.schema.json`, `scripts/run.py` (every step, review included) |
| a worked example | `research/2026-10-12-4-deep-sweep/` (its directions, args, coverage, agents and synthesis) |

## Steps

Every run is done and stored the same way: `schema/RUNS.md` is the standard, `scripts/run.py` does each step and keeps
the run's `run.json` current, and `scripts/check.py` fails on a run folder that doesn't match.

1. **Triage.** Map what is there: `python3 scripts/triage.py <roots> > $TMPDIR/triage.tsv`, then update
   `sources/TRIAGE.md` with what this run sweeps, leaves out (and why) and queues. Folders named after a person may be
   read but never cited; the iCloud root and `personal/` are never read.
2. **Make the run**: `python3 scripts/run.py new --slug SLUG --kind sweep --title "TITLE"` (creates
   `research/<date>-<n>-<slug>/` with `run.json` and the README's sections).
3. **Register sources** in `sources/sources.json`: root and prefix, and `commit` for a clean git repository
   (`git -C <root> rev-parse --short HEAD`), else `as_of` (also when a repository has uncommitted changes).
4. **Write `directions.json`**: `[{"id", "scope", "sources"}]`, one per coherent body of sources; each scope names exact
   absolute paths, what to read there and what earlier runs already used. Split big bodies across several directions.
5. **Run it**: `python3 scripts/run.py args RUN [--already FILE]`, then the Workflow tool with
   `scriptPath: "~/Projects/learning-truths/.claude/workflows/learnings-sweep.js"` and the contents of
   `.local/args/RUN.json` as `args` (`args.json` is its record, with home paths shortened)
   (a JSON value, not a string); then `python3 scripts/run.py start RUN --run-id <id> --transcript <folder>` with the
   run ID and transcript folder the Workflow tool reports.
6. **Record it** when it finishes: `python3 scripts/run.py record RUN`.
7. **Merge**: `python3 scripts/run.py items RUN --journal [--reports …]` (every verified candidate, from the journal),
   then `python3 scripts/merge_args.py research/RUN/items.json --batch-dir .local/batches/RUN > .local/batches/merge-args-RUN.json`
   and the Workflow tool with `scriptPath: "~/Projects/learning-truths/.claude/workflows/learnings-merge.js"` and that
   file's contents as `args` (small: the batches stay in files); note it with
   `python3 scripts/run.py start RUN --step merge --run-id <id> --transcript <folder>`, and when it finishes
   `python3 scripts/run.py merged RUN` rebuilds its result as `research/RUN/merged.json`.
8. **Assimilate**: `python3 scripts/run.py assimilate RUN --date <YYYY-MM-DD> --dry-run`, then without `--dry-run`. Every
   quote is checked against its file as it is written; `assimilated.json` lists the records made and added to. Evidence
   outside a registered source is reported: register the source (step 3) and assimilate again.
9. **Review**: `python3 scripts/run.py review RUN`, then the Workflow tool with
   `scriptPath: "~/Projects/learning-truths/.claude/workflows/learnings-review.js"` and the contents of
   `.local/review/RUN/args.json` as `args`; `python3 scripts/run.py start RUN --step review --run-id <id> --transcript <folder>`;
   when it finishes, `python3 scripts/run.py reviewed RUN --date <YYYY-MM-DD> --dry-run`, then without `--dry-run`.
10. **Read what changed**: the new statements, `review.json`'s fixes, drops, merges and flags, and the numbers against
   their quotes; fix by hand where needed. Fill in the README's Results and Left out.
11. **Build and check**: `python3 scripts/build.py && python3 scripts/check.py && python3 scripts/run.py status`. Commit
   only when the check exits 0; run it on its own, never piped.
12. **Show, then push.** Show the new statements and any change to `PERFECT-QUESTION.md` or `GENERATING.md`; commit (no
    attribution lines) and push on the user's word; close the control-center item with the commit, the counts and the
    run folder.

## Rules the agents follow (built into the workflows)

Read-only; no `.env`, key or token files; iCloud files download when read, so documents only, never data dumps; never
the `personal/` folder beside iCloud's `work/`; no names or roles in statements; evidence is an exact path, lines and a
verbatim quote; an adversarial verifier re-reads every cited line and drops what it cannot find.
