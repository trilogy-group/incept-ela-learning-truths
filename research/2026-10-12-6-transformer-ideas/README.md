# Run 6: the lesson engine's ideas, and how universal they are

2026-10-12.

## Scope

The lesson engine (`g9/transformer`, commit `7acdba0`) read through six lenses (the making pipeline, the reading and
checking blocks, the writing and thinking blocks, the media blocks, the runtime and quality machinery, the glue and the
surface), and a universality test: all 16 blocks made for a poem and for prose on 12 October 2026
(`universality-test.json`, `universality-test.py`, `universality-test-gettysburg.txt`), each block's record in
`g9-transformer-runs/blocks/`.

## Method

The learnings-sweep workflow (run ID `wf_9aff1090-fd5`) over 7 directions (`directions.json`): a deep reader per
direction, an adversarial verifier re-reading every cited line, a completeness critic and two gap directions it asked
for (the engine's 9 October audit, and the judge logs of drafts against remakes). Its readers were given the 55
statements then on record. It was merged after run 4 (the learnings-merge workflow, run ID `wf_62909ca9-c8a`), so its
findings were deduplicated against run 4's 714 records; assimilated on 13 October with every quote checked
(`assimilated.json`), then reviewed (the learnings-review workflow, run ID `wf_7fac03ac-4a2`, `review.json`).

## Results

- 19 agents. 339 candidates came back; the verifiers kept 331 and dropped 8. Per direction, in `coverage.json`.
- The merge turned them into 57 records, after folding 10 into others, and 310 additions to records already there, more
  than five for every new record: most of what the engine does was already on record from the earlier runs.
- 2,051 quotes were checked as they were written, 7 not found verbatim and left out. Four folders were registered first
  so that every piece of evidence sits in one: the engine's run records, its 9 October audit, the module packages it
  installs, and the reading engine's vendored content evaluator.
- The review fixed 20 records and folded 3 into the record they repeat. 54 records remain, and 163 records already there
  gained evidence.
- What the universality test added: a block meant for any text holds nothing made for one text unless each text gets
  its own, checked for fit; lines code writes around a text say only what code can know; mechanical slips, such as
  missing quotation marks round the text's words, are repaired in code; a judgment-call key ships only when a judge
  that never saw it picks it by a clear margin; a text without a lesson question gets several drafts, kept only on a
  judge's positive evidence that the text answers one.

## Left out

The engine's source beyond what each direction named, its dependencies and media, the 3D build's mirror (read once,
not cited: it names a person), and every .env, key and token file.
