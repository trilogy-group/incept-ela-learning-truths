# The questions lane

A third lane beside UI and scripted video supplies the questions for a whole lesson. It owns the knowledge to test, right answers, placement, wording, choices and challenge within the learner's zone of proximal development. It uses the same lesson plan, content keys, knowledge map, pairing tables, source text and media as the other lanes.

We borrow InceptBench's structure: typed inputs and outputs, routing by format, item and sequence checks, versioned runs and replayable traces. Its curriculum, criteria, scores and thresholds are not adopted. Question quality comes from the library's learnings and the course inputs. Learner-specific challenge needs learner evidence.

The generator is the deliverable. The evaluator must earn trust before its approvals select or release questions. Both use the public library and contract. The generator must not consume evaluator code, prompts, checks or cases. Gold labels and sealed holdouts belong outside these public repositories. The evaluator receives finished questions and lesson context without generator identity. Each half needs a different owner; public repositories do not enforce blindness or establish independent judgment.

## Stages

- **Stage 0, shape:** shared formats, the reference example, separation rules and passing checks.
- **Stage 1, working prototype:** an offline template baseline, an optional model writer, explicit lesson/task context, and standalone item and sequence development review. The 14-item text and 50-activity native handoffs demonstrate mock transport and field binding. They do not establish generation or judging quality.
- **Stage 2, next:** review both halves separately, then reconstruct independently judged cases with complete learner context. Measure false accepts, false rejects, uncertainty and repeat variation within a declared scope, against a fixed ordinary AI baseline. Agree qualification criteria before testing and keep final holdouts sealed. Wider generation and individual adaptation follow evidence; they are not prerequisites for this review.

The reference target is the authored Othello Act 1, Scene 1 lesson. The pinned `contract/` archive has forty extracted units across ten native kinds, including guided practice and paragraph subchecks. Later source captures and mock transport fixtures keep their own source versions and roles. Matching a format is only a start. Every generated sequence still needs supported interpretations, useful choices and appropriate challenge.

The library retains 1,279 records from six runs, with their evidence and limits. Pages are generated from the records. Research workflows and journals remain available for traceability. No new research run is part of this transfer.
