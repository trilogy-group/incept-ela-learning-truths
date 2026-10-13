# Shared question contract

The generator and evaluator share these formats and the public knowledge library. Private evaluator implementation, challenge labels and results do not belong here.

- `lesson-context 0.1`: public lesson context, with the lesson question, keywords and native pages in learner order.
- `question-set 0.1`: the returned sequence. Each unit keeps its native form and a plain view: choices and key, a prompt and marking rubric, or the format’s named fields.

The schemas are in schema/. examples/othello-1-1/ preserves the authored Othello Act 1, Scene 1 lesson at source commit `3ed708e126aec14b7456679b9236e01c1081df16`. Its 40 extracted units span ten kinds, including guided tasks and paragraph subchecks. This is a reference shape and target, not forty independent mastery checks or approved quality labels.

Learner-facing strings are unchanged. Personal metadata and text read only by the marker use `[name]` where needed; source.redacted lists those pointers. manifest.json pins the folded example/schema bytes and the source provenance.

From the repository root:

```sh
python3 contract/scripts/check.py
```

The check verifies fixture hashes, extractor parity and item pointers. When the recorded local mirror exists, it also compares every learner-facing context string with the pinned Git source and checks the source byte hash. It reports that comparison explicitly. With no source clone it verifies the committed snapshot, not a fresh word-for-word source comparison. To supply a different local clone, use `--source-root <repository>`.

Extract from a committed lesson with:

```sh
python3 contract/scripts/extract_authored.py --lesson <lesson.json> --mirror <repository> --remote <name> --out contract/examples/<id>
```

A changed format needs a new version and reviewed examples. Refresh the manifest only from a verified source extraction; a changed snapshot without a matching manifest fails the check.
