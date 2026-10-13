# Round 1: the film, the lesson engine, the reading engine, the BrainLift sources and the kits

## Scope

Four groups of sources: the film's reviews, renders, player and research (`g9`, `othello-unit-video`); the lesson engine
(`g9/transformer`); the reading engine and its project (`grade3-reading`); the BrainLift sources and the two pipeline
kits (`g9/.local/brainlift-sources`, `unit-video-kit`, `othello-unit-video/kit`, `unit-video-modules`).

## Method

Four read-only search agents, one per group, each given the 14 truths then on record and asked for up to 15 new
candidates, each with its path, lines and a verbatim quote, and the counter-evidence. Every quote that was used was then
re-read at its line. Each agent's brief and report are in `agents/`.

## Results

About 60 candidates came back, with counter-examples to three of the 14. 41 new truths were kept (55 in all) after
merging duplicates, and four wordings were corrected on re-reading. The run also found gaps in the work itself: one
block with no slur check, no answer-position check in the lesson engine, a film player listing the right option first
in 5 of 7 choice steps, and a review record whose two counts disagree.

## Left out

The agents' own tallies, which no record holds; sources whose file names carry a person's name; anything about the
film's particular text. The BrainLift sources themselves are untracked, so the public kit's copies were cited instead.
