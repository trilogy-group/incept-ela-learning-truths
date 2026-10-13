# How a research run is stored

Every run that adds to the records is one folder, `research/<YYYY-MM-DD>-<n>-<slug>/`, made by
`python3 scripts/run.py new` and kept in this form. `scripts/check.py` fails on a folder that doesn't match.

Every run keeps:

- `run.json`: its id, title, date, kind, status, method, sources and counts (`schema/run.schema.json`).
- `README.md`, with these sections in this order: `## Scope` (what was read, by source), `## Method` (how, by whom,
  how it was checked), `## Results` (the counts, and what was kept), `## Left out` (what was skipped or dropped, and why).

What else it keeps depends on its kind and how far it has got:

| kind | always | once recorded | once assimilated |
|---|---|---|---|
| manual | | | |
| agents | | `agents/*.md`: each agent's brief and report, verbatim | |
| sweep | `directions.json`, `args.json`, `existing-order.json` | `agents/*.md` (each agent's brief and structured result), `coverage.json` | `items.json`, `merged.json`, `onto.json`, `assimilated.json`; once reviewed, `review.json` |
| merge | `items.json` | `merged.json` | `onto.json` |

Everything recorded is redacted the same way (`scripts/redact.py`): people's names become `[name]`, home paths are
shortened to `~`, and the home folder spelt as an agent's project folder becomes `{home}`. A quote that names someone or
a job role keeps only its longest stretch without it, and evidence from a file whose name carries a person's name is
left out. A record's `found_in` names the runs it came from. Evidence can also be a commit's message (`commit`: the
path is then the repository), a file as it was at a revision (`at`: for a file deleted later), or a file
inside an archive (`member`: read in memory, never extracted). A quote of a code comment may run over lines.

The steps, each one a command that also updates `run.json`:

1. `python3 scripts/run.py new --slug SLUG --kind sweep --title "TITLE"` makes the folder, its README sections and `run.json`.
2. Write `directions.json` (`[{"id", "scope", "sources"}]`, sources being keys of `sources/sources.json`).
3. `python3 scripts/run.py args RUN` writes `args.json` and `existing-order.json` and notes the workflow's hash; run the
   `learnings-sweep` workflow with `.local/args/RUN.json` as its args (`args.json` is the same with home paths shortened).
4. `python3 scripts/run.py start RUN --run-id ID --transcript DIR` once the workflow is launched, then
   `python3 scripts/run.py record RUN` when it finishes: every agent's output and `coverage.json`.
5. `python3 scripts/run.py items RUN --journal [--reports ...]` writes `items.json` (every verified candidate, straight
   from the journal) and `onto.json` (evidence on records already there). Then
   `python3 scripts/merge_args.py research/RUN/items.json --batch-dir .local/batches/RUN > .local/batches/merge-args-RUN.json`
   and the `learnings-merge` workflow with those args, noted with `python3 scripts/run.py start RUN --step merge --run-id
   ID --transcript DIR`; when it finishes, `python3 scripts/run.py merged RUN` rebuilds its result from the journal as
   `merged.json`. (A sweep no longer synthesizes in one agent: run 4's 1,864 verified candidates did not fit one prompt.)
6. `python3 scripts/run.py assimilate RUN --date YYYY-MM-DD` writes the records and the evidence on existing ones,
   checking every quote, and lists the records it made and added to in `assimilated.json`.
7. Review: `python3 scripts/run.py review RUN` batches the run's new records (40 a batch) and every page section that
   holds one, old records included, with pairs of close records from different sections; run the `learnings-review`
   workflow with `.local/review/RUN/args.json` as its args, noted with `run.py start RUN --step review`; then
   `python3 scripts/run.py reviewed RUN --date YYYY-MM-DD --dry-run`, and without `--dry-run`. Reviewers fix statements to
   the standard (one sentence, at most 30 words), scope, role, stage and support, and drop what nothing supports; judges
   find the same learning in other words, and code folds a new record into the one it repeats. An older record is never
   dropped or folded, and keeps its statement. Everything applied is listed in `review.json`.
8. `python3 scripts/build.py && python3 scripts/check.py`, fill in the README's Results, and `python3 scripts/run.py status`.
