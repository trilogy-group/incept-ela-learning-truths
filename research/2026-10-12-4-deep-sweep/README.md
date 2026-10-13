# Run 4: the deep sweep of the AP and knowledge work

## Scope

19 directions (`directions.json`): the AP work in iCloud Drive (training, evaluators, generation service, generators,
learnings, past agent memories), the local AP copies and downloads, the knowledge bot's store in four topic slices, the
reading project's artifacts and course plans, the course-plan quality audit, and the exported curriculum folder.

## Method

The first version of the learnings-sweep workflow (`workflow-as-run.js`, run ID `wf_8d6e1149-6b1`): one deep reader per
direction, an adversarial verifier re-reading every cited line, a completeness critic with a gap round, and a synthesis
across all directions. Its readers were given 70 statements (`args.json`): the 55 records, numbered as on the front
page at commit `dd7de0f`, then round 2's 15 AP learnings (`already-found.json`); `existing-order.json` maps those numbers
back to record ids.

The synthesis did not fit one prompt, so every verified candidate was taken straight from the journal, with round 2's
candidates (`items.json`), and merged by the learnings-merge workflow (run ID `wf_605f4940-c1c`): 92 agents turned
batches of 25 into standard records, and one agent per group merged duplicates across batches. `scripts/run.py merged`
rebuilt its result from the journal (`merged.json`), and `scripts/run.py assimilate` wrote the records on 12 October,
checking every quote against its file (`assimilated.json` lists what it made and added to).

On 13 October the learnings-review workflow (run ID `wf_a62d8bcb-309`) went over the new records: 20 reviewers checked
them against the house standard (one sentence of at most 30 words, scope, role, stage, support, plain words), and 22
judges looked for the same learning in other words, one per page section with the older records included, and two over
74 close pairs from different sections. `scripts/run.py reviewed` applied what they returned (`review.json`). One merge
folded a rule for marking guides into a rule for what a writer is asked for; it was undone by hand.

## Results

- 52 agents: 19 readers, the critic, 6 gap readers it asked for (AP solver validation, AP lab runs and analyses, the AP
  project's root agent research, its live agent memories, the evaluator's 2.7.8 version and curriculum, and the content
  checkers and small generators), their 25 verifiers, and the synthesis, which failed.
- 1,898 candidates came back; the verifiers kept 1,864 and dropped 34. Per direction, in `coverage.json`.
- The merge turned 2,296 items into 766 records, after folding 913 into others across batches, with 477 additions to
  the records already there; it dropped 157 items. With `onto.json`'s 1,086 pieces of evidence on the 55 records, 9,330
  quotes were checked as they were written: 23 were not found verbatim and left out, and one was cut to its stretch
  without a job role. 31 pieces of evidence were left out because their file names carry a person's name.
- Ten sources were registered first, so that every piece of evidence sits in one: the local copy of the AP training
  work, three read-only mirrors of other teams' repositories (pinned at their commits), an arithmetic hint-review
  experiment, and agent memories. 234 quotes came from commit messages or from files at an earlier revision, checked
  against git.
- Assimilated: 765 new records (two of the run's records had the same title and became one), and evidence for or
  against 53 of the 55 records already there.
- The review fixed 501 records (480 statements cut to one sentence, what was cut moved into the detail), dropped none,
  folded 106 into the record they repeat (three of them into records from earlier runs, whose statements stayed as they
  were) and renamed 3. It left 240 flags in `review.json`, most saying a record also held a second learning, now in its
  detail. 659 of the run's records remain.
- One reader broke the read-only rule once: it saved four reports' text to a file under `/tmp` to read it, and deleted
  it straight away; it wrote nothing else.

## Left out

Data dumps, model files and logs; the `personal/` folder; folders judged unrelated (see `sources/TRIAGE.md`);
sources whose file names carry a person's name, and a cloud archive folder named after a person.
