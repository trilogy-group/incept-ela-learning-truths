export const meta = {
  name: 'learning-truths-deep-sweep',
  description: 'Deep, triaged sweep of every AP and knowledge source for text-independent learning truths, each verified',
  phases: [
    { title: 'Read', detail: 'one deep reader per AP or knowledge direction' },
    { title: 'Verify', detail: 'an adversarial verifier re-reads every cited line' },
    { title: 'Critic', detail: 'what was not read, or read too thinly' },
    { title: 'Gaps', detail: 'readers and verifiers for the gaps' },
    { title: 'Synthesize', detail: 'merge, dedupe and group across directions' },
  ],
}

const W = '~/Library/Mobile Documents/com~apple~CloudDocs/work'
const GR = '~/Projects/grade3-reading'
const EXISTING = args.existing.map((t, i) => `${i + 1} ${t}`).join(' · ')

const RULES = `STRICT RULES. Read-only: never create, edit, move or delete a file, and run no command that writes anywhere (text extraction to stdout is fine: textutil -convert txt -stdout <file>, pdftotext <file> -, unzip -p <file> <member>). No network access. Never open .env files or key, token or credential files, and never print a secret. Files in iCloud Drive may be placeholders that download when read: read documents (.md, .txt, .qmd, .html, .docx, .pdf, small .json), never data dumps (.jsonl beyond a few records, .csv beyond its header and a few rows, .sql, .zip, .parquet, model weights, logs). Never read anything under ~/Library/Mobile Documents/com~apple~CloudDocs/personal/. Never put a person's name or job role in a statement; if a file's path contains a person's name, set name_bearing_source to true on any candidate that relies on it, and prefer evidence from another file.`

const TASK = `Find lessons learned that hold for ANY lesson, course or set of learning materials, whatever the subject, grade or text: rules about teaching, practice, assessment, feedback, texts, media, curriculum and knowledge, and about making, generating, judging, reviewing or measuring learning content. Dig deep: read every document in scope that could hold findings, decisions, postmortems, reviews, specs, QA records or research notes, and prefer the project's own measurements (numbers exactly as written).
For each candidate give: statement (one plain sentence that holds without its source's subject; no subject-specific terms unless essential; no names or roles); kind ("measured", "adopted rule", "external research" with its DOI or URL as written, or "open question"); found_by (what went wrong, what was measured, or what made the rule); evidence (one to three items, each the exact absolute path, the line numbers, and the sentence quoted exactly as it appears); against (counter-evidence or limits from the sources, quoted, or "none found"); adds_to_existing (numbers from the list below that it strengthens, or empty); name_bearing_source.
Also list evidence_for_existing: quotes that support or contradict truths already on the list, by number. In coverage, list what you read (folders or files), what you skipped and why, and any notes.
There is no cap on candidates, but each must be distinct, general and cited. Exclude model-training mechanics that don't bear on making or checking learning content (hyperparameters, GPUs, infrastructure, vendors), organisational matters (approvals, meetings, team direction, people), and anything you cannot cite.
TRUTHS ALREADY ON THE LIST (skip them unless you have new, stronger evidence or a counter-example): ${EXISTING}`

const DIRECTIONS = [
  { id: 'aptraining-core', scope: `${W}/aptraining/: its top-level .md files, handover/, coordination/, agents/, memory/, apllm-history/, artifacts/, parallel-ideas-lab/ and helpers/ (documents and docstrings only). Then ${W}/aptraining-crystal-copy-20260521/: find documents that exist only in this snapshot or differ from the current aptraining (postmortems, reports, decisions) and read those. Context: a project that trained and evaluated models to generate AP social studies questions (multiple choice, short answer, document-based, long essay) to a 97% quality bar.` },
  { id: 'aptraining-workspace', scope: `${W}/aptraining/workspace/: find the written reports, summaries, postmortems, analyses, reviews, READMEs and evaluation write-ups (.md) by name (report, summary, postmortem, findings, lessons, analysis, review, readme, eval) and read them; never data files. Then ${W}/aptraining/Cheater/: every document (what gaming of the evaluator or shortcuts were found, and how they were stopped). Context: AP social studies question generation and evaluation.` },
  { id: 'inceptbench', scope: `${W}/inceptbench/, ${W}/inceptbench-main/ and ${W}/inceptbench-latest/: every document on how generated learning items are evaluated: rubrics per item type, hard fails, calibration, changelogs and fixes (what each bug taught), localization guidelines, verifiers; note what changed between the three copies and why. Already used, so look beyond them: docs/AP_EVALUATION.md, docs/legacy/EVALUATORS.md (lines 47-51, 122, 150, 246), docs/MATH_VERIFIER.md, docs/user_guides/api.md, docs/user_guides/examples.md.` },
  { id: 'evaluators', scope: `${W}/evaluator/ and ${W}/evaluatorML/: how generated items were judged, how evaluators were trained or calibrated, failure analyses, agreement with people.` },
  { id: 'incept-core', scope: `${W}/incept/nova_forge/, ${W}/incept/inceptlm/, ${W}/incept/incept-multilingual-generation/ and ${W}/incept/incept-uae-api-website/ (documents only): rules for generating learning content, quality gates, what failed and why.` },
  { id: 'incept-exams', scope: `${W}/incept/aplit-quiz-generation/, ${W}/incept/sat-reading-generation/, ${W}/incept/ap-benchmark-standalone/, ${W}/incept/inceptbench/, ${W}/ap-benchmark-standalone/ and ${W}/question_generator/: exam-style item generation (AP Literature quizzes, SAT reading, AP benchmarks).` },
  { id: 'social-studies', scope: `${W}/ap-social-studies-generator/ and ${W}/k_12_social_studies/ (including ap_files): generation rules, item specs (stimulus-based questions, short answer, document-based and long essay tasks), validation, review findings.` },
  { id: 'ml-learnings-deep', scope: `${W}/ML learnings/: all its documents (INDEX.md first), especially those an earlier pass only skimmed: research_* (with the studies they cite), decisions_and_pivots_timeline, master_strategy_apr24, grpo_failures_deep_dive, grpo_design_and_theory, dpo_and_fdpo_pipeline, agent_delegation_architecture, debugging_methodology, what_is_ap_and_why_it_matters. An earlier pass already found these, so look beyond them: ${args.apRound2.join(' · ')}.` },
  { id: 'memories-and-small', scope: `${W}/auto-memory-backup/ (past agent memories: feedback and lessons recorded during AP and other learning-content projects; skip anything personal), ${W}/common-core-resource-aggregator/, ${W}/meaningful_ai_learning/, ${W}/ai_coach/ and ${W}/expertise-inflation-index/: first decide which of these hold anything about learning or learning content (say so in coverage), then read those deeply.` },
  { id: 'local-ap', scope: `~/Documents/APinceptbench/. In ~/Downloads/: the unit-N-apush-benchmark.jsonl files (read only the first few records of one or two, to learn what each item records and what its quality fields mean), and the "Knowledge Schema Generator - ..." and "AP US History - Knowledge Schema - SME Tracker" spreadsheets (read their text with unzip -p <file> xl/sharedStrings.xml; ignore any person's name in them). Documents mentioning AP in ~/Projects/incept-package-hub/. In ${GR}/: ti-courseplans/courses/hs-civics/reference/ (one file there is named after a person: read it, but flag it as name_bearing_source), ti-courseplans/courses/map-proxy-assessment/ (validity case, exam spec), artifacts/team-direction-2026-09-09/research/, artifacts/wiki-research/hub-review-model.md, artifacts/g5_build_2026_07_02/.` },
  { id: 'kb-learning-science', scope: `${GR}/knowledge_bot/knowledge/ (a store of summarised sources; INDEX.md lists every entry with tags and keywords): pick every entry tagged or keyed reading-science, brainlift, reading-comprehension, science-curriculum, psychometrics, rand-report, pedagogical-llm, assessment-design, standards or teks, or about instruction, practice, curriculum and knowledge, and read each in full. Never open ${GR}/knowledge_bot/.env.` },
  { id: 'kb-reviews-evaluation', scope: `${GR}/knowledge_bot/knowledge/ (INDEX.md first): every entry tagged or keyed reviewer-feedback, reviewer-round, curriculum-review, red-team, anti-leak, calibration, inceptbench, generator, decisions, g3-g5-closeout or coe, or about what reviewers found and how content was evaluated; read each in full. Already used: kb-0069, kb-0070, kb-0099, kb-0235. Never open ${GR}/knowledge_bot/.env.` },
  { id: 'kb-course-builds', scope: `${GR}/knowledge_bot/knowledge/ (INDEX.md first): every entry tagged or keyed g3-reading, grade3-reading, g5-reading, peter-pan, coverage-fill or g9-othello: course builds, coverage, and lessons from building them; read each in full. Never open ${GR}/knowledge_bot/.env.` },
  { id: 'kb-platform-and-bot', scope: `${GR}/knowledge_bot/knowledge/ entries tagged timeback, qti, oneroster, caliper, sdk, alpharead, audio, course-renderer or atom-composite-ledger (keep only what bears on learning or on making and checking learning content), plus ${GR}/knowledge_bot/ BRIEFING.md, HOTBUCKET.md, CHECKLIST.md, MAP.md, ROUTER.md, handoffs/, pr-proposals/, skills/ and templates/. Never open ${GR}/knowledge_bot/.env.` },
  { id: 'artifacts-qa', scope: `${GR}/artifacts/: listen-qa-l4-l7-2026-09-24, listen-qa-l1-orphans-2026-09-24, l1-parity-untracked-2026-09-24, peter-pan-standing-2026-09-11, codex-qa, demo-unit-2026-07-10, alpha-read-packager, art-qa-redcontrol-2026-09-11, curriculum-adherence-2026-09-24, HUMAN-REVIEW-2026-09-21 (folder and .md), AlphaRead-QC-Checklist-v2-2026-09-04.md, the feedback-* folders whose names carry no person's name (feedback-inceptbench-*, feedback-content-review-*, feedback-closing-questions-*, feedback-live-walk-*, feedback-codex-visual-*, feedback-devfactory-*, feedback-argus-ui-*, feedback-pp-*, feedback-aladdin-*, feedback-ela-chat-*), compare-2026-09-2*, eval-suite, cert-layer and criteria-register.csv: what QA and reviewers found in lessons, and why.` },
  { id: 'artifacts-builds-research', scope: `${GR}/artifacts/: g5-course, g5-book-2026-09-29, g5-merged-course, g5_build_2026_07_02, course-json-standard-2026-07-13, course-factory-skills, decision-brief-2026-09-10, decision-matrix, decision-packets-2026-09-03, DECISIONS-2026-08-24.md, CLOSURE-PLAN-2026-08-25.md, PROPOSAL_REVIEW_2026_06_16.md, the LANE*.md files, X1_staar_map_overlap_probe_2026_06_16.md, wiki-research, team-direction-2026-09-09, the edullm-* folders, baseline-submission, build-closing-questions-2026-09-25, and the other dated folders not named after a person. Already used: arc-audit/SIM-REVIEW-D5-D6-D11-D13.md, semantic-judge-calibration-2026-07-10, spine-solve-calibration-2026-07-10, GOAL_grade3_hootl_convergence_2026_06_15.md, g9-prep-pack-2026-10-02 INDEX and MANIFEST.` },
  { id: 'ti-courseplans', scope: `${GR}/ti-courseplans/: docs/, feedback/, brainlift/, skills/, handoff/, service/, and courses/ (each course's README, iteration approval packages, response matrices, analysis and reference documents; skip raw lesson-content dumps). Already used: docs/key-quality-gates.md lines 65-66 and courses/g3-reading/iteration-2/approval-package-v2/sources/RESPONSE-MATRIX.md line 21.` },
  { id: 'quality-standard-audit', scope: `~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806/ and the other ~/Projects/ti-courseplans* folders: the quality standard for course plans, how it was audited, what failed.` },
  { id: 'cloud-curriculum', scope: `~/Downloads/5. Curriculum/ (an export of a cloud curriculum folder: Texts, including Misconception and alignment checks; Instruction: Procedures, Example lesson structure, Lesson Designs; Curriculum maps). Read .md directly, .docx and .html with textutil -convert txt -stdout <file>, .pdf with pdftotext <file> -, .xlsx with unzip -p <file> xl/sharedStrings.xml, all to stdout. Skip ~/Downloads/5-Curriculum/ (an older copy). Also in ~/Downloads/: "BrainLift - What makes a good intro video.md", "WF - Brainlift Opportunities to - 260724-110911.md", the two "WITW Lesson 1 learning walkthrough" .md files and "_G3 curriculum Map.xlsx - Curric Map.csv". This is curriculum material made by others: extract only what it shows or states about how lessons, texts and checks should be built, cite it, and never copy it at length.` },
]

const EVID = { type: 'object', properties: { path: { type: 'string' }, lines: { type: 'string' }, quote: { type: 'string' } }, required: ['path', 'lines', 'quote'] }
const READ_SCHEMA = {
  type: 'object',
  properties: {
    direction: { type: 'string' },
    coverage: { type: 'object', properties: { read: { type: 'array', items: { type: 'string' } }, skipped: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' } }, required: ['read', 'skipped', 'notes'] },
    candidates: { type: 'array', items: { type: 'object', properties: {
      statement: { type: 'string' }, kind: { type: 'string', enum: ['measured', 'adopted rule', 'external research', 'open question'] },
      found_by: { type: 'string' }, evidence: { type: 'array', items: EVID }, against: { type: 'string' },
      adds_to_existing: { type: 'array', items: { type: 'integer' } }, name_bearing_source: { type: 'boolean' },
    }, required: ['statement', 'kind', 'found_by', 'evidence', 'against', 'adds_to_existing', 'name_bearing_source'] } },
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
const SYNTH_SCHEMA = {
  type: 'object',
  properties: {
    truths: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, group: { type: 'string' }, statement: { type: 'string' }, kind: { type: 'string' },
      new_or_existing: { type: 'string' }, evidence: { type: 'array', items: EVID }, against: { type: 'string' },
      sources: { type: 'array', items: { type: 'string' } }, independent_sources: { type: 'integer' },
    }, required: ['id', 'group', 'statement', 'kind', 'new_or_existing', 'evidence', 'against', 'sources', 'independent_sources'] } },
    counter_to_existing: { type: 'array', items: { type: 'object', properties: { truth: { type: 'integer' }, summary: { type: 'string' }, path: { type: 'string' }, lines: { type: 'string' }, quote: { type: 'string' } }, required: ['truth', 'summary', 'path', 'lines', 'quote'] } },
    added_evidence: { type: 'array', items: { type: 'object', properties: { truth: { type: 'integer' }, path: { type: 'string' }, lines: { type: 'string' }, quote: { type: 'string' } }, required: ['truth', 'path', 'lines', 'quote'] } },
    dropped: { type: 'array', items: { type: 'string' } },
  },
  required: ['truths', 'counter_to_existing', 'added_evidence', 'dropped'],
}

const readPrompt = (d) => `${TASK}\n\nYOUR DIRECTION: ${d.id}. SCOPE: ${d.scope}\n\n${RULES}`
const verifyPrompt = (d, r) => `You are an adversarial verifier for candidate learning truths found in the "${d.id}" direction. For every candidate (by its index in the list) and every evidence_for_existing item: open each cited file at the cited lines and read about ten lines around them; confirm the quote appears verbatim (if it is elsewhere in the file, correct the line numbers; if it is not in the file at all, mark it verbatim=false); confirm every number in the statement and the quote matches the source exactly. Then judge each candidate: is the statement general, true beyond its source's subject and grade? Is it supported by the evidence as quoted, without overstating it? Is it a duplicate of a truth already on the list (give the number in duplicate_of, else "")? Does the statement name a person or a job role (rewrite it if so)? Does its evidence rest on a file whose path contains a person's name (name_bearing_source)? Verdicts: keep; keep-with-fix (give the corrected statement and evidence); drop (say why). Default to drop when a quote cannot be found or the claim overstates its evidence. Keep a duplicate only when it adds evidence, and say so in reason.\n\n${RULES}\n\nTRUTHS ALREADY ON THE LIST: ${EXISTING}\n\nTHE READER'S RESULT (JSON):\n${JSON.stringify(r)}`

phase('Read')
const verifiedMain = await pipeline(DIRECTIONS,
  (d) => agent(readPrompt(d), { label: `read:${d.id}`, phase: 'Read', schema: READ_SCHEMA }),
  (r, d) => (r ? agent(verifyPrompt(d, r), { label: `verify:${d.id}`, phase: 'Verify', schema: VERIFY_SCHEMA }).then((v) => ({ id: d.id, read: r, verify: v })) : null),
)
const done = verifiedMain.filter(Boolean)
log(`${done.length} of ${DIRECTIONS.length} directions read and verified`)

phase('Critic')
const coverage = done.map((x) => ({ id: x.id, coverage: x.read.coverage, candidates: x.read.candidates.length }))
const critic = await agent(`Here is the triage map of AP and knowledge sources on this machine, as scopes given to readers, and each reader's coverage report. List what was not read, or read too thinly, that could still hold lessons for making, checking or teaching with learning content: at most 6 gaps, each with an id and a precise scope a new reader could follow (absolute paths). Stay within AP, knowledge and learning-content work; don't propose re-reading what was covered. If coverage is adequate, return no gaps. You may list folders to check what exists, read-only.\n\n${RULES}\n\nSCOPES:\n${DIRECTIONS.map((d) => `- ${d.id}: ${d.scope}`).join('\n')}\n\nCOVERAGE (JSON):\n${JSON.stringify(coverage)}`, { label: 'critic', phase: 'Critic', schema: CRITIC_SCHEMA })
const gaps = (critic?.gaps ?? []).slice(0, 6)
log(`critic: ${gaps.length} gaps${gaps.length ? ': ' + gaps.map((g) => g.id).join(', ') : ''}`)

phase('Gaps')
const verifiedGaps = gaps.length ? (await pipeline(gaps,
  (g) => agent(readPrompt(g), { label: `read:gap:${g.id}`, phase: 'Gaps', schema: READ_SCHEMA }),
  (r, g) => (r ? agent(verifyPrompt(g, r), { label: `verify:gap:${g.id}`, phase: 'Gaps', schema: VERIFY_SCHEMA }).then((v) => ({ id: `gap:${g.id}`, read: r, verify: v })) : null),
)).filter(Boolean) : []

phase('Synthesize')
const all = [...done, ...verifiedGaps]
const kept = all.flatMap((x) => (x.verify?.verified ?? []).filter((c) => c.verdict !== 'drop').map((c) => ({ direction: x.id, ...c, found_by: x.read.candidates[c.index]?.found_by ?? '', adds_to_existing: x.read.candidates[c.index]?.adds_to_existing ?? [] })))
const existingChecked = all.flatMap((x) => (x.verify?.existing_checked ?? []).filter((e) => e.ok).map((e) => ({ direction: x.id, ...e })))
const droppedCount = all.reduce((n, x) => n + (x.verify?.verified ?? []).filter((c) => c.verdict === 'drop').length, 0)
log(`${kept.length} candidates kept after verification, ${droppedCount} dropped; ${existingChecked.length} quotes bear on existing truths`)

const synthesis = await agent(`Merge verified candidate learning truths from ${all.length} directions into one consolidated set, for a repository of rules that hold for any lesson. Use only the verified evidence given; invent nothing.
- Merge duplicates across directions into one truth, keeping the strongest one to four evidence items (verbatim quotes, exact paths and lines), and count independent sources.
- A candidate that is a special case of another merges into it; a candidate that duplicates a truth already on the list becomes added_evidence for that number, not a new truth.
- Each truth: id (short kebab-case), group (one of: "What a student is told", "Writing questions", "Checking answers", "The text", "Pictures, sound and film", "Generating materials with a model", "AI judges and markers", "How people learn", "Making and reviewing lessons", "Not settled yet"), statement (one plain sentence, no names or roles, no subject-specific terms unless essential), kind, new_or_existing ("new", or "adds to #N" when it refines an existing truth enough to change its wording), evidence, against, sources (direction ids), independent_sources.
- Put quotes that contradict an existing truth in counter_to_existing, and quotes that only support one in added_evidence (by number).
- Skip any candidate whose only evidence has name_bearing_source true, and list it in dropped with its reason; also list in dropped anything you merge away or cut.
- Prefer cutting to adding: keep only truths a lesson builder would act on.

TRUTHS ALREADY ON THE LIST: ${EXISTING}

VERIFIED CANDIDATES (JSON):
${JSON.stringify(kept)}

VERIFIED QUOTES ON EXISTING TRUTHS (JSON):
${JSON.stringify(existingChecked)}`, { label: 'synthesize', phase: 'Synthesize', schema: SYNTH_SCHEMA })

return {
  synthesis,
  coverage: all.map((x) => ({ id: x.id, read: x.read.coverage.read.length, skipped: x.read.coverage.skipped, notes: x.read.coverage.notes, candidates: x.read.candidates.length, kept: (x.verify?.verified ?? []).filter((c) => c.verdict !== 'drop').length })),
  gaps,
  criticNotes: critic?.notes ?? '',
  droppedCount,
}