# Triage

Every folder considered for a sweep, and what was done with it. `scripts/triage.py` maps a root's folders by their
documents, iCloud placeholders and keyword-named files; each run adds what it swept, left out or queued.

## Swept

- Runs 1 to 3 (12 October 2026): `g9`, `othello-unit-video`, `grade3-reading/engine`, `unit-video-kit`,
  `unit-video-modules`, the BrainLift sources in `g9/.local/brainlift-sources`, the AP learnings and builds in iCloud
  Drive, and the knowledge bot's store.
- Run 4, the deep sweep (12 October 2026), in 19 directions (`research/2026-10-12-4-deep-sweep/directions.json`):
  - iCloud Drive `work/`: aptraining and its 21 May snapshot, inceptbench (three copies), evaluator, evaluatorML,
    incept (its generation service, AP Literature quizzes, SAT reading and AP benchmark), ap-social-studies-generator,
    k_12_social_studies, ap-benchmark-standalone, question_generator, ML learnings, auto-memory-backup,
    common-core-resource-aggregator, meaningful_ai_learning, ai_coach, expertise-inflation-index.
  - `~/Documents/APinceptbench`; in `~/Downloads`: the APUSH benchmark files, the knowledge-schema spreadsheets, the
    curriculum folder export `5. Curriculum`, and the BrainLift and walkthrough documents.
  - `grade3-reading`: the knowledge bot (all of it), the artifacts (QA, builds, research), the course plans; and
    `~/Projects/ti-courseplans-quality-standard-audit-handoff-20260806`.
  - Followed by its gap readers: `~/Documents/aptraining` (the local copy of the AP training work: the ideas lab, the
    analyzer, the den of ideation), three read-only mirrors in `~/Projects/shadow` (bench, content-eval, curriculum,
    pinned at their commits, commit messages included), `~/Projects/uae-education-ai`, and agent memories (the AP
    project's, its two helpers', one workspace's daily notes, and the AP training notes among the home folder's).

## Left out, and why

- iCloud Drive `work/`: sales, ContractIgence, abacus_ai, meeter, amplifier, intelligence-to-deck, ASTK_files,
  crossover, heygen, hedra-avatar-starter, ai_fireship, ai_ping_pong, ai_substack, three chatbot folders
  (`ai-coe-substack-chatbot`, `ai-coe-substack-chatbot-1`, `ai_coe-multi_modal_chatbot`), dspy_exploration, demo, imgcount, kiro_testing, wave-tools, waveterm-snapshots, supabase, preserved_models: not about
  learning content. mem0 and memory_agents: agent-memory tooling. `personal/`, beside `work/`: never read.
- `grade3-reading`: folders named after people (the course-approach drafts, the catch-up and feedback folders named
  for a person, two personal draft folders, the chat extracts): read where needed, never cited.
- `~/Downloads/5-Curriculum`: an older copy of `5. Curriculum`.

## The whole map, 12 October 2026

Counted with `scripts/triage.py` (documents: .md, .qmd, .txt, .docx, .pdf, .html; the tables are in `triage/`). Covered
means a run read it; partly means a run read a chosen part.

| where | documents | covered |
|---|---|---|
| `grade3-reading` | 28,623 | knowledge bot (400) fully; artifacts (3,786) and course plans (1,313) partly; engine (66) |
| `grade3-reading`, not yet | | ui-audit-2026-09-08 (10,041), `course-renderer` (1,832), visual-findings (690), edullm-review-hub (258), _archive (235), bias_experiment (83), helpers (39), red_team (36), curriculum-gen (32), agent-kit, incept-read-app, workspace, ti-courseplans-wiki, inbox |
| `g9` | 917 | the film, player, reviews and lesson engine; not yet: `transcript/`, `library/`, `sources/`, and the script, narration, score and art folders' notes |
| `shadow` | 2,105 | bench, content-eval and curriculum: cited by run 4's gap readers; the rest not swept (read-only mirrors of other teams' repositories) |
| `manager` | 974 | not swept: the work registry |
| `othello-course-renderer-draft` | 883 | not yet |
| `incept-package-hub` | 404 | not yet |
| `expanova-labs` | 218 | not yet triaged by content |
| `ti-courseplans-quality-standard-audit-handoff-20260806` | 174 | run 4 |
| small repositories | under 30 each | `othello-unit-video`, `unit-video-kit`: covered; `unit-video-kit-essay`, `othello-archive`, `blog`, `uae-education-ai` and the rest: not yet |
| iCloud Drive `work/` | 30,000 or so | every AP folder in run 4 (aptraining's 23,893 are almost all generated data: only its reports were read); about 20 folders judged unrelated by name, not yet confirmed by content |
| iCloud Drive root and `personal/` | | never: personal files |
| `~/Documents`, `~/Desktop` | 84 and 7 | APinceptbench covered; aptraining's reports read by run 4's gap readers; the rest not yet triaged |
| `~/Downloads` | | the curriculum export, AP files and BrainLifts covered; the rest not yet triaged |

## Queued for a later sweep

- `grade3-reading/ui-audit-2026-09-08` (10,041 documents) and `grade3-reading/visual-findings-2026-09-07` (674): UI and
  visual QA findings.
- `grade3-reading/course-renderer` (1,832 documents): check whether it holds findings or only a renderer's code.
- `~/Projects/incept-package-hub` (362 documents, 4 on AP), `~/Projects/expanova-labs` (218) and
  `~/Projects/uae-education-ai` (8): not yet triaged for learning content.
- The knowledge bot's search sources that point at another machine's files (the Practice, Generic Instruction, Direct
  Instruction, and Curriculum and Knowledge BrainLifts, among others): find local copies or the cloud originals.
