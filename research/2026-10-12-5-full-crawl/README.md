# Run 5: the crawl of the remaining Grade 3, Grade 9 and repository material

2026-10-12.

## Scope

The remaining Grade 3, Grade 9 and repository material chosen on 12 October 2026, in 17 directions (`directions.json`):
the reading project's UI audit, visual findings, renderer and review-hub documentation, archive, experiments, and the
artifacts and course plans run 4 did not reach; the Grade 9 team-chat transcript, library, curriculum sources and
production notes; the Grade 9 renderer draft, the package hub, the 3D-build fork and the kit variant.

## Method

The learnings-sweep workflow (run ID `wf_edb31f4f-67b`), launched once run 4 was assimilated, so its readers were given
the 714 statements then on record (`existing-statements.txt`): a deep reader per direction, an adversarial verifier
re-reading every cited line, a completeness critic and six gap directions it asked for (the AP archive's documents, the
Grade 3 audits of one novel's lessons, the reading project's skills and rulings, one Grade 5 lesson's audit, the Grade 9
handover's prototypes, and a map-reading proxy test's validity work). The learnings-merge workflow (run ID
`wf_f0127559-0e6`) turned the verified candidates into records against the 768 then on record; assimilated on 13 October
with every quote checked (`assimilated.json`), and reviewed by the learnings-review workflow (run ID `wf_ce937c29-25b`,
`review.json`). One merge, which folded the order in which a performance's parts are taught into a record on assuming
only what was taught, was undone by hand.

## Results

- 47 agents: 17 readers, the critic, 6 gap readers, their 23 verifiers. 1,207 candidates came back; the verifiers kept
  1,192 and dropped 15. Per direction, in `coverage.json`.
- The merge turned 1,185 items into 557 records, after folding 141 into others across batches, with 638 additions to
  the records already there; with `onto.json`'s 2,301, 7,308 quotes were checked as they were written and 13 were not
  found verbatim and left out. 24 quotes were cut to their stretch without a name or job role.
- Readers cited files inside archives (the reading project's consolidation snapshots, the Grade 9 handover packages,
  the package hub's approval packages) and code comments running over several lines. The quote check now reads an
  archive's member in memory, never extracting it, and joins a comment's lines; before that, 647 quotes failed.
- Two sources were registered first, both kept on this machine and out of git: the Grade 9 handover packages and the
  first film's render folder.
- The review fixed 168 records and folded 46 into the record they repeat (9 of them into records from earlier runs,
  whose statements stayed as they were); it left 63 flags in `review.json`. 511 of the run's records remain.
- One reader broke the read-only rule once: it made an empty folder under `/tmp` and wrote nothing into it.

## Left out

Images, audio and film; data dumps, logs and generated inventories; source code beyond the checks the directions named;
the read-only portal's sourcing; files whose names carry a person's name (read where a direction needed them, never
cited); and every .env, key and token file.
