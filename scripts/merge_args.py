#!/usr/bin/env python3
"""Build the args for the learnings-merge workflow: the items to merge, the records already there (id, title,
statement) and the vocabulary. With --batch-dir the items are written there as one JSON file per batch and only the
file paths go into the args (a large run's items do not fit a tool call); each merge agent reads its own file.
Usage: merge_args.py ITEMS.json [--batch-size N] [--batch-dir DIR] > args.json"""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import VOCAB, records

ap = argparse.ArgumentParser()
ap.add_argument("items")
ap.add_argument("--batch-size", type=int, default=25)
ap.add_argument("--batch-dir")
a = ap.parse_args()
items = json.loads(Path(a.items).read_text())
out = {"existing": [{"id": r["id"], "title": r["title"], "statement": r["statement"]} for r in records()], "vocabulary": VOCAB, "batchSize": a.batch_size}
if a.batch_dir:
    d = Path(a.batch_dir).expanduser().resolve()
    d.mkdir(parents=True, exist_ok=True)
    files = []
    for k in range(0, len(items), a.batch_size):
        f = d / f"batch-{k // a.batch_size + 1:03d}.json"
        f.write_text(json.dumps(items[k: k + a.batch_size], ensure_ascii=False, indent=1))
        files.append(str(f))
    (d / "existing.json").write_text(json.dumps(out.pop("existing"), ensure_ascii=False, indent=1))
    out.update({"batchDir": str(d), "batchCount": len(files), "existingFile": str(d / "existing.json")})
else:
    out["items"] = items
json.dump(out, sys.stdout, ensure_ascii=False)
