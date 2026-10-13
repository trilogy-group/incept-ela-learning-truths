#!/usr/bin/env python3
"""Build the args for the learnings-sweep workflow from a run's directions file and the records now on file: the
directions, the current statements (numbered in the order saved to existing-order.json beside the directions, so the
run's numbers can be mapped back to record ids), the vocabulary, and optionally what earlier runs already found.
Usage: sweep_args.py research/<run>/directions.json [--already FILE] [--focus TEXT] > args.json"""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import VOCAB, records

ap = argparse.ArgumentParser()
ap.add_argument("directions")
ap.add_argument("--already")
ap.add_argument("--focus")
ap.add_argument("--max-gaps", type=int, default=6)
a = ap.parse_args()
d = Path(a.directions)
rs = records()
(d.parent / "existing-order.json").write_text(json.dumps([r["id"] for r in rs], indent=1) + "\n")
out = {"directions": json.loads(d.read_text()), "vocabulary": VOCAB, "maxGaps": a.max_gaps}
if len(rs) > 300:
    # too many to pass inline: the agents read them, numbered as here, from a file beside the directions
    f = (d.parent / "existing-statements.txt").resolve()
    f.write_text("".join(f"{i + 1} {r['statement']}\n" for i, r in enumerate(rs)))
    out["existingFile"] = str(f)
else:
    out["existing"] = [r["statement"] for r in rs]
if a.already:
    out["alreadyFound"] = [l.strip() for l in Path(a.already).read_text().splitlines() if l.strip()]
if a.focus:
    out["focus"] = a.focus
json.dump(out, sys.stdout, ensure_ascii=False)
