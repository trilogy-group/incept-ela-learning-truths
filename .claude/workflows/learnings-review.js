export const meta = {
  name: 'learnings-review',
  description: "Review a run's new learning records against the house standard, and find duplicates across groups: one reviewer per batch of records, one judge per page section; code applies the result",
  whenToUse: 'After a run is assimilated into ~/Projects/learning-truths. Args from `python3 scripts/run.py review RUN`: {batchDir, batchCount, sliceDir, sliceCount, vocabulary}. Then `python3 scripts/run.py reviewed RUN` applies the result from the journal.',
  phases: [
    { title: 'Review', detail: "one agent per batch of the run's new records: fixes to the standard, scope and support" },
    { title: 'Dedupe', detail: 'one agent per page section, old and new records together: the same learning in other words' },
  ],
}

const VOCAB = args.vocabulary
const keys = (o) => Object.keys(o)
const RULES = `Read-only: never create, edit, move or delete a file, and run nothing that writes. Never open .env, key, token or credential files. Never read ~/Library/Mobile Documents/com~apple~CloudDocs/personal/. Write no person's name or job role in any field.`

const CHANGES = { type: 'object', properties: {
  title: { type: 'string' }, statement: { type: 'string' }, example: { type: 'string' }, detail: { type: 'string' },
  group: { type: 'string', enum: keys(VOCAB.groups) }, role: { type: 'string', enum: keys(VOCAB.roles) },
  facets: { type: 'array', items: { type: 'string', enum: keys(VOCAB.facets) } }, stage: { type: 'string', enum: [...keys(VOCAB.stages), 'none'] },
  scope: { type: 'string', enum: VOCAB.scopes }, domains: { type: 'array', items: { type: 'string', enum: keys(VOCAB.domains) } },
  status: { type: 'string', enum: VOCAB.statuses }, kind: { type: 'string', enum: VOCAB.kinds }, against: { type: 'string' },
} }
const REVIEW_SCHEMA = { type: 'object', properties: {
  fixes: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, changes: CHANGES, why: { type: 'string' } }, required: ['id', 'changes', 'why'] } },
  drops: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, why: { type: 'string' } }, required: ['id', 'why'] } },
  flags: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, issue: { type: 'string' } }, required: ['id', 'issue'] } },
}, required: ['fixes', 'drops', 'flags'] }
const DEDUPE_SCHEMA = { type: 'object', properties: {
  merges: { type: 'array', items: { type: 'object', properties: { keep: { type: 'string' }, merge: { type: 'array', items: { type: 'string' } }, statement: { type: 'string' }, why: { type: 'string' } }, required: ['keep', 'merge', 'statement', 'why'] } },
}, required: ['merges'] }

const STANDARD = `The standard:
1. statement: one plain sentence of at most 30 words stating one learning that someone making questions or lessons can apply. Cut a longer one to its core claim and append what you cut to detail as plain sentences, so nothing is lost. A record that holds two separate learnings keeps the main one in its statement; move the other to detail and add a flag saying so.
2. title: two to eight words naming the learning. The title is also the record's id, so change it only when it is wrong or longer than eight words.
3. Support: the statement and example claim no more than the record's evidence shows. Narrow an overreaching statement. If no evidence supports the record at all, put it in drops with the reason.
4. scope: universal when it would hold for questions or lessons in other subjects and settings; domain when it holds only where it was found (an exam's own formats and rules, one programme's conventions, one product's settings), with domains naming where.
5. role, stage and facets: a criterion is what a perfect question or lesson has; a method is how to make or check one, and has a stage (${keys(VOCAB.stages).join(', ')}); context bounds the others (limits, measures, research). Only a method has a stage; give a criterion or context the stage "none". facets: the main facet first, all from the vocabulary.
6. status: open for an open question (group not-settled); contested when against holds counter-evidence that disputes the claim rather than limits it; otherwise held.
7. Words: no person's name or job role, and no product, build, model, team or project name in title, statement or example; name things generically ("an item evaluator", "an animated version", "an AI marker", "a generator"). No internal codes, unit codes, version numbers or run ids in title or statement, and at most one number in the statement. Plain words over jargon: write out what an abbreviation means.
8. example: one sentence with the case or number that shows the learning, or empty.
9. against: the counter-evidence and limits in plain sentences, each said once and starting with a capital, or "none found".
10. kind: measured when a count or rate from real runs backs it; adopted-rule when it is a rule people or a build adopted; external-research only when a published study backs it and the record cites it; open-question for an open question.`

const reviews = []
for (let k = 1; k <= args.batchCount; k++) reviews.push(`${args.batchDir}/batch-${String(k).padStart(3, '0')}.json`)
const slices = []
for (let k = 1; k <= args.sliceCount; k++) slices.push(`${args.sliceDir}/slice-${String(k).padStart(3, '0')}.json`)
log(`${reviews.length} review batches, ${slices.length} dedupe slices`)

const reviewOne = (file, k) => agent(`You review learning records in ~/Projects/learning-truths, a repository whose goal is an understanding of what a perfect question is and how to generate perfect questions. Read the batch file ${file}: a JSON list of full records, each with its evidence (python3 -c "import json; print(json.dumps(json.load(open('${file}')), indent=1))"). Check every record against the standard below and return a fix only where a record falls short: leave a record that meets it alone, and don't rephrase for taste. You may open a cited file (read-only) when a record's support is in doubt.

${STANDARD}

Return fixes ([{id, changes, why}], changes holding only the fields that change, with their new values), drops ([{id, why}]) and flags ([{id, issue}]: anything you see but can't fix by these rules, such as a quote that names someone).

${RULES}

VOCABULARY: ${JSON.stringify(VOCAB)}`, { label: `review:${k + 1}`, phase: 'Review', schema: REVIEW_SCHEMA })

const dedupeOne = (file, k) => agent(`Read ${file} (python3 -c "import json; print(json.dumps(json.load(open('${file}')), indent=1))"): one section of the pages of ~/Projects/learning-truths, a repository of learnings about what a perfect question is and how to generate perfect questions. It holds {name, about, records: [{id, title, statement, group, on_record}]}, or {name, about, pairs: [[a, b], ...]} with each record in records. Find the records that state the same learning: the same rule in other words, or one a special case of the other. For each such set give keep (the id to keep), merge (the ids to fold into it), statement (one plain sentence of at most 30 words that covers them all) and why. A record with on_record true was there before this run: when a set includes one, keep it (its statement stays as it is), and never merge two records that are both on_record; say so in why and leave them. Leave distinct records alone, including close ones that say different things. Use only the ids in the file; for pairs, judge each pair on its own.

${RULES}`, { label: `dedupe:${k + 1}`, phase: 'Dedupe', schema: DEDUPE_SCHEMA })

const [rev, ded] = await Promise.all([
  parallel(reviews.map((f, k) => () => reviewOne(f, k))),
  parallel(slices.map((f, k) => () => dedupeOne(f, k))),
])
const r = rev.filter(Boolean), d = ded.filter(Boolean)
const counts = {
  batches: reviews.length, reviewed: r.length, fixes: r.reduce((n, x) => n + x.fixes.length, 0), drops: r.reduce((n, x) => n + x.drops.length, 0), flags: r.reduce((n, x) => n + x.flags.length, 0),
  slices: slices.length, judged: d.length, merges: d.reduce((n, x) => n + x.merges.length, 0),
}
log(JSON.stringify(counts))
// the results stay in the journal; `python3 scripts/run.py reviewed RUN` applies them
return counts
