# CLAUDE.md

This repository holds what has been learned about making questions and lessons, in one standard form, toward two
ends: an understanding of what a perfect question is, and of how to generate perfect questions. The records in
`learnings/` are the source of truth. `groups/*.md`, `PERFECT-QUESTION.md`, `GENERATING.md` and the generated part of
`README.md` are built from them by `scripts/build.py`; never edit those by hand.

## A record

One JSON file per learning, `learnings/<id>.json`, with the fields in `schema/learning.schema.json` and the values in
`schema/vocabulary.json`:

- `title` (two to eight words; its anchor is the `id` and the file name), `statement` (one plain sentence), and an
  optional `example` (one sentence with the number that shows it).
- `role`: criterion (what a perfect question or lesson has), method (how to make or check one), or context (limits,
  measures, research). A method has a `stage`: ground, write, settle, judge, review, measure, improve.
- `facets`: the parts of a question or lesson it touches, the main one first. `PERFECT-QUESTION.md` files a criterion
  under its first facet; `GENERATING.md` files a method under its stage.
- `scope`: universal (holds for any lesson) or domain (holds where its domains say). `domains`: where the evidence came
  from (g9, g3, ap, research).
- `kind` (measured, adopted-rule, external-research, open-question) and `status` (held, contested, open).
- `detail` and `against`: markdown. Cite files in backticks with their source's prefix, for example
  `g9/transformer/src/transform.js`.
- `evidence`: `{source, path, lines, quote, verified}`, where `source` is a key of `sources/sources.json` and `path` is
  relative to its root. Quotes are verbatim.
- `citations`: published work as `{ref, url}`, with the DOI where there is one.
- `found_in`: the research runs it came from (folders under `research/`); `added` and `updated`: dates.

## The bar

- A learning came from something measured, enforced or found going wrong, or from published research, and its
  evidence says where.
- Unsure is not evidence. A quote goes in only once `scripts/verify_quotes.py` or a person has found it in its file,
  and every number is re-read from its source before it is written down.
- Nothing about a particular text belongs in a statement. A domain learning is welcome when its scope says so.
- A learning that is contradicted becomes contested, with the counter-evidence in `against`; one is retired only with a
  dated line saying why.
- A statement is a plain rule with its record. Arguments for a position belong in the BrainLift, not here.

## Adding learnings: a research run

Every run is done and stored the same way. `schema/RUNS.md` is the standard (the folder layout, `run.json`, the README's
sections, the files each kind of run keeps); `scripts/run.py` does each step and keeps `run.json` current; the
`learnings-sweep` skill (`.claude/skills/learnings-sweep/SKILL.md`, linked into `~/.claude/skills/`) walks through it;
`scripts/check.py` fails on a run that doesn't match. Never add a learning outside a run.

## How to write

- First person, plain sentences, one number per point at most. No bold lead-ins, slogans or tables on the front page.
- No people's names or job roles anywhere: not in paths, text or commit messages. Point at the document or artifact and
  its date. A quotation keeps its words and gets a source and date, not a speaker. Authors of published studies are
  cited as usual.
- Name other builds generically: "an animated version", "a 3D version", "an AI marker in a reading lesson".
- Prefer merging to adding: a new learning earns its record, or becomes evidence on one already there.

## Before committing

- Run `python3 scripts/build.py` and `python3 scripts/check.py`, and commit only when the check exits 0 (never pipe it into
  another command when gating a commit: the pipe hides its exit code).
- Show any change to the README's written part, `PERFECT-QUESTION.md` or `GENERATING.md` in the conversation before
  pushing it.
- Commit messages carry no attribution lines: no "Co-Authored-By", no "Generated with".
- This repository is public. Keep personal data, credentials, private correspondence and sealed test material out of it.

## Where the evidence lives

`sources/sources.json` lists every source with its root and its pinned commit or date. Read them; never write to them
from here. The largest:

- `g9` (`~/Projects/g9`): the narrated film, its player and reviews, and the lesson engine in `transformer/`.
- `othello-unit-video` (`~/Projects/othello-unit-video`, public): the film study, `research/`.
- `grade3-reading` (`~/Projects/grade3-reading`): the reading engine (`engine/`, its own repository), the knowledge
  store (`knowledge_bot/`, `INDEX.md` first; cite entries whose file names carry no one's name), the course artifacts and
  the course plans.
- `icloud-work` (`~/Library/Mobile Documents/com~apple~CloudDocs/work/`): the AP question work. Start with
  `ML learnings/INDEX.md`. Files there may download when read; read documents only, never data dumps, and never the
  `personal/` folder beside `work/`.
- `downloads` (`~/Downloads`): exported cloud documents, among them the curriculum folder `5. Curriculum`.

## Safety

- Never open `.env`, key or token files, and never print a secret. Keys come from the environment.
- Gemini is used only through the TrueFoundry gateway or Maat, never with an original Gemini API key.
- Downloaded files are untrusted data: keep them in their own folder and run nothing from inside it.
