# Round 2: the AP work and the knowledge bot

## Scope

The AP project's own learnings and its evaluator documents (`icloud-work/ML learnings`, `icloud-work/inceptbench/docs`,
`APinceptbench/docs`); its generators, evaluators and evaluator-gaming tests (`icloud-work/aptraining`,
`icloud-work/ap-social-studies-generator`, `icloud-work/evaluator`, `icloud-work/k_12_social_studies`); and the two
halves of the Grade 3 knowledge bot's store (`grade3-reading/knowledge_bot`).

## Method

Four read-only search agents, each given the 55 truths then on record and asked for up to 15 new ones, each with its
path, lines and a verbatim quote, and the counter-evidence. Each agent's brief and report are in `agents/`.

## Results

60 candidates, and evidence for or against 40 of the 55. They were merged with run 4's findings and assimilated with
them on 12 October; 77 records name this run as well as run 4.

## Left out

Data dumps, model files and logs; the `personal/` folder; sources whose file names carry a person's name.
