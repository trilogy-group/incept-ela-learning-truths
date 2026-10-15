# Incept ELA learning truths

Research and shared formats for the questions lane. Each learning keeps its evidence, scope and counterarguments. Courses are sources and examples; the aim is knowledge that applies across lessons.

The three repositories are:

- [incept-ela-learning-truths](https://github.com/trilogy-group/incept-ela-learning-truths): the public library, proposal and shared contract.
- [question-generator](https://github.com/trilogy-group/incept-ela-question-generator): an offline template baseline and an optional model writer using supplied lesson and task context.
- [question-evaluator](https://github.com/trilogy-group/incept-ela-question-evaluator): standalone field checks and separate development reviews of items and instructional sequences. Academic accuracy is not qualified.

Start with [AGENTS.md](AGENTS.md) and [IDEAS.md](IDEAS.md). [PERFECT-QUESTION.md](PERFECT-QUESTION.md) and [GENERATING.md](GENERATING.md) summarize the records. [RELATED.md](RELATED.md) links the related repositories.

[contract/](contract/) defines the inputs and outputs. Its reference has 40 extracted units from the authored Othello 1.1 lesson at source commit `3ed708e`. It includes guided practice and writing subchecks; these are reference questions, not gold labels.

```sh
python3 run.py
```

This builds the pages, checks the library and contract, and exports public generation inputs to `exports/generator/`. Source checks use the registered research clones. It calls no model. [CLAUDE.md](CLAUDE.md) covers record maintenance.

[knowledge-v1](https://github.com/trilogy-group/incept-ela-learning-truths/tree/knowledge-v1) pins the initial library and shared formats in [baseline.json](baseline.json). Held, contested and open statuses remain intact; this is a research baseline, not academic qualification. Maintain it through specific corrections or dated rulings with evidence. Later changes do not alter this pin; a new baseline needs its own version.

Reference example collection: [examples/sources.json](examples/sources.json) pins the source versions. `python3 run.py --collect-examples` reads matching bytes from `.local/example-sources/` and builds `.local/question-examples/`: `browse.json` gives one example per available source kind, `questions.jsonl` holds the collection, and `catalog.json` records hashes, source pointers, context and coverage gaps. Use `--source-cache <directory>` for another cache. Course snapshots, historical variants, guided tasks and generated formative prompts remain distinguishable. Intended answers are source material, not quality labels. The full corpus stays local; the normal runner checks it when present. The original 40-unit contract and `knowledge-v1` remain pinned.

Refresh the current teaching references with `python3 scripts/current_reference.py --refresh`. It compares both hosted layouts with current source main, records routes and asset hashes in a new private snapshot, preserves previous collections and source pins, and refreshes local examples. It keeps distinct references when deployment lags behind source changes. The current authored references are the default positive baselines designated by the user; this supplies no independent quality labels.

## Review before the next stage

Implementation snapshot: [evaluator `48d9c43`](https://github.com/trilogy-group/incept-ela-question-evaluator/commit/48d9c43a32c04d0f42d3b9d66d2b2bca3ce16d07), [generator `ed8aae4`](https://github.com/trilogy-group/incept-ela-question-generator/commit/ed8aae40112401e609cc1cf2fb3bf34ba71e7ddf), and the [shared context contract](contract/README.md). The library still contains 1,279 records with their scope and counterevidence.

Checks passed at those versions: 333 evaluator tests, 78 focused tests on Node 18.20.8, and 55 Python plus 42 Node generator tests. The 14-item text and 50-activity native handoffs are producer-generated offline mock fixtures. Supplied context and field pointers resolve; the checks do not establish context completeness, the pointers' role as response evidence or writing quality. The original 40-unit reference remains a separate historical snapshot. No dedicated evaluator or generator UI exists.

Separate read-only Claude Code reviews of the evaluator and generator are complete. Each reviewer received permitted public knowledge and only its own half's internals. The reviews cover concrete defects, unsupported claims and the top three next steps; they are not academic qualification. Documentation claims have been narrowed where needed. Implementation suggestions remain unapplied, with receipts in the evaluator's private evidence index and the raw generator review kept with its owner.

The next evidence gap is academic accuracy: reconstruct accepted and defective cases with complete lesson context, resolve conflicting rulings, and measure a fixed evaluator against independent held-out judgments. Compare it with a strong ordinary AI review given the same context. Software checks, model agreement and exact quotations do not establish question quality or learning gains. Public evaluator code and development cases must stay out of generator contexts; independent gold labels and sealed tests belong in separate restricted storage.

<!-- generated: start -->

## What is here

1279 learnings: 605 criteria, 562 methods and 112 on context. Where the evidence came from: Grade 9 in 251, Grade 3 and 5 reading in 861, AP in 329, published studies in 172 (a learning can draw on several). 1121 are held, 61 contested and 97 open.

- [What a perfect question is](PERFECT-QUESTION.md): the criteria, by facet
- [How to generate perfect questions](GENERATING.md): the methods, by stage
- [What a student is told](groups/what-a-student-is-told.md): 116
- [Writing questions](groups/writing-questions.md): 170
- [Checking answers](groups/checking-answers.md): 73
- [The text and its sources](groups/the-text.md): 109
- [Pictures, sound and film](groups/pictures-sound-film.md): 116
- [Generating with a model](groups/generating-with-a-model.md): 88
- [AI judges and markers](groups/ai-judges-and-markers.md): 108
- [How people learn](groups/how-people-learn.md): 169
- [Making and reviewing lessons](groups/making-and-reviewing.md): 233
- [Not settled yet](groups/not-settled.md): 97

Learnings that hold only in one domain: [Grade 9](domains/g9.md) 27, [Grade 3 and 5 reading](domains/g3.md) 37, [AP](domains/ap.md) 10.

Research runs, each recorded in full under [research/](research/):

- [Seed: the first 14 truths](research/2026-10-12-1-seed/)
- [Round 1: the film, the lesson engine, the reading engine, the BrainLift sources and the kits](research/2026-10-12-2-round-1/)
- [Round 2: the AP work and the knowledge bot](research/2026-10-12-3-round-2/)
- [Run 4: the deep sweep of the AP and knowledge work](research/2026-10-12-4-deep-sweep/)
- [Run 5: the crawl of the remaining Grade 3, Grade 9 and repository material](research/2026-10-12-5-full-crawl/)
- [Run 6: the lesson engine's ideas, and how universal they are](research/2026-10-12-6-transformer-ideas/)

<!-- generated: end -->
