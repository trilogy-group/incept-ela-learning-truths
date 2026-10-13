export const meta = {
  name: 'learnings-merge',
  description: 'Turn candidate learnings from any run (reports, syntheses, notes) into standard records: classify in batches, then merge duplicates across batches and against the records already there',
  whenToUse: 'After a research run for ~/Projects/learning-truths, when its findings are not yet standard records. Args from scripts/merge_args.py: {items:[{origin, text}] or batchFiles:[path], existing:[{id,title,statement}], vocabulary:<schema/vocabulary.json>, batchSize?:number}',
  phases: [
    { title: 'Standardize', detail: 'one agent per batch of candidates' },
    { title: 'Dedupe', detail: 'one agent per group finds duplicates across batches; code merges them' },
  ],
}

const VOCAB = args.vocabulary
const keys = (o) => Object.keys(o)
// the records already there: inline, or in a file the agents read (scripts/merge_args.py --batch-dir writes it)
const EXISTING = args.existingFile ? `a JSON list of {id, title, statement} in ${args.existingFile}; read it first` : args.existing.map((r) => `${r.id}: ${r.statement}`).join('\n')
const SIZE = args.batchSize ?? 25
const RULES = `Read-only: never create, edit, move or delete a file, and run nothing that writes. Never open .env, key, token or credential files. Never read ~/Library/Mobile Documents/com~apple~CloudDocs/personal/. No person's name or job role in any field; if the only evidence for a candidate sits in a file whose path contains a person's name, drop the candidate and say why.`

const EVID = { type: 'object', properties: { path: { type: 'string' }, lines: { type: 'string' }, quote: { type: 'string' } }, required: ['path', 'lines', 'quote'] }
const RECORD = { type: 'object', properties: {
  title: { type: 'string' }, statement: { type: 'string' }, example: { type: 'string' },
  group: { type: 'string', enum: keys(VOCAB.groups) }, role: { type: 'string', enum: keys(VOCAB.roles) },
  facets: { type: 'array', items: { type: 'string', enum: keys(VOCAB.facets) } }, stage: { type: 'string', enum: [...keys(VOCAB.stages), 'none'] },
  scope: { type: 'string', enum: VOCAB.scopes }, domains: { type: 'array', items: { type: 'string', enum: keys(VOCAB.domains) } },
  kind: { type: 'string', enum: VOCAB.kinds }, status: { type: 'string', enum: VOCAB.statuses },
  detail: { type: 'string' }, against: { type: 'string' }, evidence: { type: 'array', items: EVID },
  citations: { type: 'array', items: { type: 'object', properties: { ref: { type: 'string' }, url: { type: 'string' } }, required: ['ref', 'url'] } },
  origins: { type: 'array', items: { type: 'string' } },
}, required: ['title', 'statement', 'example', 'group', 'role', 'facets', 'stage', 'scope', 'domains', 'kind', 'status', 'detail', 'against', 'evidence', 'citations', 'origins'] }
const BATCH_SCHEMA = { type: 'object', properties: {
  records: { type: 'array', items: RECORD },
  onto_existing: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, effect: { type: 'string', enum: ['supports', 'counter', 'refines'] }, note: { type: 'string' }, evidence: { type: 'array', items: EVID }, origins: { type: 'array', items: { type: 'string' } } }, required: ['id', 'effect', 'note', 'evidence', 'origins'] } },
  dropped: { type: 'array', items: { type: 'string' } },
}, required: ['records', 'onto_existing', 'dropped'] }
const DEDUPE_SCHEMA = { type: 'object', properties: {
  merges: { type: 'array', items: { type: 'object', properties: { keep: { type: 'integer' }, merge: { type: 'array', items: { type: 'integer' } }, statement: { type: 'string' }, why: { type: 'string' } }, required: ['keep', 'merge', 'statement', 'why'] } },
}, required: ['merges'] }

// items inline (small runs), or batch files written by scripts/merge_args.py (large runs: an agent reads its own file)
const batches = []
if (args.batchDir) for (let k = 1; k <= args.batchCount; k++) batches.push({ file: `${args.batchDir}/batch-${String(k).padStart(3, '0')}.json` })
else if (args.batchFiles) args.batchFiles.forEach((f) => batches.push({ file: f }))
else for (let i = 0; i < args.items.length; i += SIZE) batches.push(args.items.slice(i, i + SIZE))
log(`${batches[0]?.file ? batches.length + ' batch files' : args.items.length + ' items in ' + batches.length + ' batches'}`)

phase('Standardize')
const out = (await parallel(batches.map((b, k) => () => agent(`Turn these candidate learnings into standard records for a repository whose goal is an understanding of what a perfect question is and how to generate perfect questions. Invent nothing: keep every quote verbatim, with its exact path and lines. Every path must be absolute (starting with / or ~): expand an abbreviated path with the path legend the item carries, and if a candidate gives a path and lines but no exact quote, you may open the file (read-only) and copy the sentence exactly. Text that only bears on a record already there goes in onto_existing. A candidate that repeats a record already there goes in onto_existing (supports, counter or refines, with its evidence), not in records. Merge candidates within this batch that say the same thing.
Each record: title (two to eight words), statement (one plain sentence of at most 30 words, nothing about a particular text; what doesn't fit goes in detail), example (one sentence with the number that shows it, or ""), group, role (criterion: what a perfect question or lesson has; method: how to make or check one; context: limits, measures, research), facets (main first), stage (for a method: ${keys(VOCAB.stages).join(', ')}; otherwise "none"), scope (universal, or domain when it holds only in its domain), domains (where the evidence came from: ${keys(VOCAB.domains).join(', ')}), kind, status (held; contested when the sources disagree; open for open questions), detail (two to five plain sentences: how it was found and what the evidence shows, numbers as written), against (counter-evidence or "none found"), evidence, citations (published work with DOI or URL), origins (the origin labels of the candidates it came from).

${RULES}

VOCABULARY: ${JSON.stringify(VOCAB)}

RECORDS ALREADY THERE (id: statement):
${EXISTING}

${b.file ? `CANDIDATES: a JSON list in ${b.file}; read the whole file (the Read tool, or python3 -c "import json; print(json.dumps(json.load(open('${b.file}')), indent=1))")` : `CANDIDATES (JSON):\n${JSON.stringify(b)}`}`, { label: `standardize:${k + 1}`, phase: 'Standardize', schema: BATCH_SCHEMA })))).filter(Boolean)

const records = out.flatMap((o) => o.records)
const onto = out.flatMap((o) => o.onto_existing)
const dropped = out.flatMap((o) => o.dropped)
log(`${records.length} records, ${onto.length} additions to existing records, ${dropped.length} dropped`)

phase('Dedupe')
// duplicates sit in the same group: one agent per group keeps every prompt small, however large the run
const byGroup = {}
records.forEach((r, i) => { (byGroup[r.group] = byGroup[r.group] || []).push(i) })
const dedupes = (await parallel(Object.entries(byGroup).filter(([, ix]) => ix.length > 1).map(([g, ix]) => () =>
  agent(`These are new records in the group "${g}", from separate batches. Find the ones that say the same thing (one is a special case of another, or they are the same rule in other words). For each such group give keep (the index of the record to keep), merge (the indices to fold into it) and the best one-sentence statement for the merged record (at most 30 words: the shared rule, not every special case). Leave distinct records alone. Use only the indices listed:\n${ix.map((i) => `${i}: ${records[i].title}: ${records[i].statement}`).join('\n')}`, { label: `dedupe:${g}`, phase: 'Dedupe', schema: DEDUPE_SCHEMA })))).filter(Boolean)
const ded = { merges: dedupes.flatMap((d) => d.merges) }

const gone = new Set()
for (const m of ded?.merges ?? []) {
  const base = records[m.keep]
  if (!base || gone.has(m.keep)) continue
  base.statement = m.statement || base.statement
  for (const j of m.merge) {
    const r = records[j]
    if (!r || j === m.keep || gone.has(j)) continue
    const seenE = new Set(base.evidence.map((e) => e.path + '|' + e.quote))
    base.evidence.push(...r.evidence.filter((e) => !seenE.has(e.path + '|' + e.quote)))
    const seenC = new Set(base.citations.map((c) => c.url))
    base.citations.push(...r.citations.filter((c) => !seenC.has(c.url)))
    base.origins = [...new Set([...base.origins, ...r.origins])]
    base.domains = [...new Set([...base.domains, ...r.domains])]
    if (r.against && r.against !== 'none found' && !base.against.includes(r.against)) base.against = base.against === 'none found' ? r.against : `${base.against} ${r.against}`
    gone.add(j)
  }
}
const final = records.filter((_, i) => !gone.has(i))
log(`${final.length} records after merging ${gone.size} duplicates`)
return { records: final, onto_existing: onto, dropped, merged: gone.size }
