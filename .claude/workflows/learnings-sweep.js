export const meta = {
  name: 'learnings-sweep',
  description: 'Sweep sources for learnings about making questions and lessons: a deep reader per direction, an adversarial verifier, a critic and gap round, and a synthesis into standard records',
  whenToUse: 'A research run for ~/Projects/learning-truths (see its learnings-sweep skill). Args from scripts/run.py args: {directions:[{id,scope}], existing:[statement] or existingFile:path, vocabulary:<schema/vocabulary.json>, alreadyFound?:[string], maxGaps?:number, focus?:string}',
  phases: [
    { title: 'Read', detail: 'one deep reader per direction' },
    { title: 'Verify', detail: 'an adversarial verifier re-reads every cited line' },
    { title: 'Critic', detail: 'what was not read, or read too thinly' },
    { title: 'Gaps', detail: 'readers and verifiers for the gaps' },
    { title: 'Synthesize', detail: 'count what was kept; the learnings-merge workflow standardizes it' },
  ],
}

// Inputs. directions: [{id, scope}] where scope names exact paths and what to read there. existing: the statements already
// on record (numbered here, so readers can say which they strengthen). vocabulary: schema/vocabulary.json, parsed.
const DIRECTIONS = args.directions
// the statements on record: inline, numbered; or (a large record) a file the agents read, its lines numbered the same way
const EXISTING = args.existingFile ? `numbered one per line in ${args.existingFile}; read it first` : args.existing.map((t, i) => `${i + 1} ${t}`).join(' · ')
const VOCAB = args.vocabulary
const FOCUS = args.focus || 'the ultimate goal is an understanding of what a perfect question is and of how to generate perfect questions'
const ALREADY = (args.alreadyFound || []).join(' · ')
const MAX_GAPS = args.maxGaps ?? 6

const RULES = `STRICT RULES. Read-only: never create, edit, move or delete a file, and run no command that writes anywhere (text extraction to stdout is fine: textutil -convert txt -stdout <file>, pdftotext <file> -, unzip -p <file> <member>). No network access. Never open .env files or key, token or credential files, and never print a secret. Files in iCloud Drive may be placeholders that download when read: read documents (.md, .txt, .qmd, .html, .docx, .pdf, small .json), never data dumps (.jsonl beyond a few records, .csv beyond its header and a few rows, .sql, .zip, .parquet, model weights, logs). Never read anything under ~/Library/Mobile Documents/com~apple~CloudDocs/personal/. Never put a person's name or job role in a statement; if a file's path contains a person's name, set name_bearing_source to true on any candidate that relies on it, and prefer evidence from another file.`

const TASK = `Find lessons learned about making questions and lessons: rules about teaching, practice, assessment, questions and their options, keys, distractors, stimuli, scoring guides, feedback, texts, media, curriculum and knowledge, and about generating, judging, reviewing or measuring learning content. Keep in mind that ${FOCUS}. Universal lessons come first, but a lesson that holds only in its domain (an exam, a grade, a subject) is welcome when you say so in scope_note. Dig deep: read every document in scope that could hold findings, decisions, postmortems, reviews, specs, QA records or research notes, and prefer the project's own measurements (numbers exactly as written).
For each candidate give: statement (one plain sentence; nothing about a particular text; no names or roles); kind ("measured", "adopted rule", "external research" with its DOI or URL as written, or "open question"); found_by (what went wrong, what was measured, or what made the rule); evidence (one to three items, each the exact absolute path, the line numbers, and the sentence quoted exactly as it appears); against (counter-evidence or limits from the sources, quoted, or "none found"); scope_note ("universal", or the domain it holds in); adds_to_existing (numbers from the list below that it strengthens, or empty); name_bearing_source.
Also list evidence_for_existing: quotes that support or contradict statements already on the list, by number. In coverage, list what you read (folders or files), what you skipped and why, and any notes.
There is no cap on candidates, but each must be distinct and cited. Exclude model-training mechanics that don't bear on making or checking learning content (hyperparameters, GPUs, infrastructure, vendors), organisational matters (approvals, meetings, team direction, people), and anything you cannot cite.${ALREADY ? `\nALREADY FOUND IN EARLIER RUNS (look beyond these): ${ALREADY}` : ''}
STATEMENTS ALREADY ON RECORD (skip them unless you have new, stronger evidence or a counter-example): ${EXISTING}`

const EVID = { type: 'object', properties: { path: { type: 'string' }, lines: { type: 'string' }, quote: { type: 'string' } }, required: ['path', 'lines', 'quote'] }
const READ_SCHEMA = {
  type: 'object',
  properties: {
    direction: { type: 'string' },
    coverage: { type: 'object', properties: { read: { type: 'array', items: { type: 'string' } }, skipped: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' } }, required: ['read', 'skipped', 'notes'] },
    candidates: { type: 'array', items: { type: 'object', properties: {
      statement: { type: 'string' }, kind: { type: 'string', enum: ['measured', 'adopted rule', 'external research', 'open question'] },
      found_by: { type: 'string' }, evidence: { type: 'array', items: EVID }, against: { type: 'string' }, scope_note: { type: 'string' },
      adds_to_existing: { type: 'array', items: { type: 'integer' } }, name_bearing_source: { type: 'boolean' },
    }, required: ['statement', 'kind', 'found_by', 'evidence', 'against', 'scope_note', 'adds_to_existing', 'name_bearing_source'] } },
    evidence_for_existing: { type: 'array', items: { type: 'object', properties: {
      truth: { type: 'integer' }, effect: { type: 'string', enum: ['supports', 'counter'] }, path: { type: 'string' }, lines: { type: 'string' }, quote: { type: 'string' },
    }, required: ['truth', 'effect', 'path', 'lines', 'quote'] } },
  },
  required: ['direction', 'coverage', 'candidates', 'evidence_for_existing'],
}
const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    direction: { type: 'string' },
    verified: { type: 'array', items: { type: 'object', properties: {
      index: { type: 'integer' }, verdict: { type: 'string', enum: ['keep', 'keep-with-fix', 'drop'] }, reason: { type: 'string' },
      statement: { type: 'string' }, kind: { type: 'string' },
      evidence: { type: 'array', items: { type: 'object', properties: { path: { type: 'string' }, lines: { type: 'string' }, quote: { type: 'string' }, verbatim: { type: 'boolean' } }, required: ['path', 'lines', 'quote', 'verbatim'] } },
      against: { type: 'string' }, general: { type: 'boolean' }, duplicate_of: { type: 'string' }, name_bearing_source: { type: 'boolean' },
    }, required: ['index', 'verdict', 'reason', 'statement', 'kind', 'evidence', 'against', 'general', 'duplicate_of', 'name_bearing_source'] } },
    existing_checked: { type: 'array', items: { type: 'object', properties: {
      truth: { type: 'integer' }, effect: { type: 'string' }, path: { type: 'string' }, lines: { type: 'string' }, quote: { type: 'string' }, ok: { type: 'boolean' },
    }, required: ['truth', 'effect', 'path', 'lines', 'quote', 'ok'] } },
  },
  required: ['direction', 'verified', 'existing_checked'],
}
const CRITIC_SCHEMA = {
  type: 'object',
  properties: { gaps: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, scope: { type: 'string' }, why: { type: 'string' } }, required: ['id', 'scope', 'why'] } }, notes: { type: 'string' } },
  required: ['gaps', 'notes'],
}
const keys = (o) => Object.keys(o)
const RECORD = { type: 'object', properties: {
  title: { type: 'string' }, statement: { type: 'string' }, example: { type: 'string' },
  group: { type: 'string', enum: keys(VOCAB.groups) }, role: { type: 'string', enum: keys(VOCAB.roles) },
  facets: { type: 'array', items: { type: 'string', enum: keys(VOCAB.facets) } }, stage: { type: 'string', enum: [...keys(VOCAB.stages), 'none'] },
  scope: { type: 'string', enum: VOCAB.scopes }, domains: { type: 'array', items: { type: 'string', enum: keys(VOCAB.domains) } },
  kind: { type: 'string', enum: VOCAB.kinds }, status: { type: 'string', enum: VOCAB.statuses },
  detail: { type: 'string' }, against: { type: 'string' }, evidence: { type: 'array', items: EVID },
  citations: { type: 'array', items: { type: 'object', properties: { ref: { type: 'string' }, url: { type: 'string' } }, required: ['ref', 'url'] } },
  new_or_existing: { type: 'string' }, sources: { type: 'array', items: { type: 'string' } }, independent_sources: { type: 'integer' },
}, required: ['title', 'statement', 'example', 'group', 'role', 'facets', 'stage', 'scope', 'domains', 'kind', 'status', 'detail', 'against', 'evidence', 'citations', 'new_or_existing', 'sources', 'independent_sources'] }
const SYNTH_SCHEMA = {
  type: 'object',
  properties: {
    records: { type: 'array', items: RECORD },
    counter_to_existing: { type: 'array', items: { type: 'object', properties: { truth: { type: 'integer' }, summary: { type: 'string' }, path: { type: 'string' }, lines: { type: 'string' }, quote: { type: 'string' } }, required: ['truth', 'summary', 'path', 'lines', 'quote'] } },
    added_evidence: { type: 'array', items: { type: 'object', properties: { truth: { type: 'integer' }, path: { type: 'string' }, lines: { type: 'string' }, quote: { type: 'string' } }, required: ['truth', 'path', 'lines', 'quote'] } },
    dropped: { type: 'array', items: { type: 'string' } },
  },
  required: ['records', 'counter_to_existing', 'added_evidence', 'dropped'],
}

const readPrompt = (d) => `${TASK}\n\nYOUR DIRECTION: ${d.id}. SCOPE: ${d.scope}\n\n${RULES}`
const verifyPrompt = (d, r) => `You are an adversarial verifier for candidate learnings found in the "${d.id}" direction. For every candidate (by its index in the list) and every evidence_for_existing item: open each cited file at the cited lines and read about ten lines around them; confirm the quote appears verbatim (if it is elsewhere in the file, correct the line numbers; if it is not in the file at all, mark it verbatim=false); confirm every number in the statement and the quote matches the source exactly. Then judge each candidate: does it hold as scoped (universally, or in the domain its scope_note names)? Is it supported by the evidence as quoted, without overstating it? Is it a duplicate of a statement already on record (give the number in duplicate_of, else "")? Does the statement name a person or a job role (rewrite it if so)? Does its evidence rest on a file whose path contains a person's name (name_bearing_source)? Verdicts: keep; keep-with-fix (give the corrected statement and evidence); drop (say why). Default to drop when a quote cannot be found or the claim overstates its evidence. Keep a duplicate only when it adds evidence, and say so in reason.\n\n${RULES}\n\nSTATEMENTS ALREADY ON RECORD: ${EXISTING}\n\nTHE READER'S RESULT (JSON):\n${JSON.stringify(r)}`
const sweep = (items, phaseRead, phaseVerify, prefix) => pipeline(items,
  (d) => agent(readPrompt(d), { label: `read:${prefix}${d.id}`, phase: phaseRead, schema: READ_SCHEMA }),
  (r, d) => (r ? agent(verifyPrompt(d, r), { label: `verify:${prefix}${d.id}`, phase: phaseVerify, schema: VERIFY_SCHEMA }).then((v) => ({ id: `${prefix}${d.id}`, read: r, verify: v })) : null),
)

phase('Read')
const done = (await sweep(DIRECTIONS, 'Read', 'Verify', '')).filter(Boolean)
log(`${done.length} of ${DIRECTIONS.length} directions read and verified`)

phase('Critic')
const coverage = done.map((x) => ({ id: x.id, coverage: x.read.coverage, candidates: x.read.candidates.length }))
const critic = await agent(`Here are the scopes given to readers and each reader's coverage report. List what was not read, or read too thinly, that could still hold lessons for making, checking or teaching with learning content: at most ${MAX_GAPS} gaps, each with an id and a precise scope a new reader could follow (absolute paths). Don't propose re-reading what was covered. If coverage is adequate, return no gaps. You may list folders to check what exists, read-only.\n\n${RULES}\n\nSCOPES:\n${DIRECTIONS.map((d) => `- ${d.id}: ${d.scope}`).join('\n')}\n\nCOVERAGE (JSON):\n${JSON.stringify(coverage)}`, { label: 'critic', phase: 'Critic', schema: CRITIC_SCHEMA })
const gaps = (critic?.gaps ?? []).slice(0, MAX_GAPS)
log(`critic: ${gaps.length} gaps${gaps.length ? ': ' + gaps.map((g) => g.id).join(', ') : ''}`)

phase('Gaps')
const gapDone = gaps.length ? (await sweep(gaps, 'Gaps', 'Gaps', 'gap:')).filter(Boolean) : []

phase('Synthesize')
// No single synthesis agent: a large run's verified candidates do not fit one prompt (run 4: 1,864). They stay in the
// journal; `scripts/run.py items RUN --journal` and the learnings-merge workflow turn them into standard records in batches.
const all = [...done, ...gapDone]
const kept = all.reduce((n, x) => n + (x.verify?.verified ?? []).filter((c) => c.verdict !== 'drop').length, 0)
const droppedCount = all.reduce((n, x) => n + (x.verify?.verified ?? []).filter((c) => c.verdict === 'drop').length, 0)
log(`${kept} candidates kept after verification, ${droppedCount} dropped; next: run.py record, items --journal, learnings-merge`)

return {
  coverage: all.map((x) => ({ id: x.id, read: x.read.coverage.read.length, skipped: x.read.coverage.skipped, notes: x.read.coverage.notes, candidates: x.read.candidates.length, kept: (x.verify?.verified ?? []).filter((c) => c.verdict !== 'drop').length })),
  gaps,
  criticNotes: critic?.notes ?? '',
  kept,
  droppedCount,
}
