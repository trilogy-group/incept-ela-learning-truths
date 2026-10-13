#!/usr/bin/env python3
"""Map candidate sources before a sweep: for each folder one level under the given roots, count its documents, how many
are iCloud placeholders (not yet downloaded; reading one downloads it), and how many file names match the keywords.
Read-only; reads names and file flags, never contents.
Usage: triage.py [--keywords REGEX] ROOT [ROOT ...]"""
import argparse, os, re, stat
from pathlib import Path

DOCS = {".md", ".qmd", ".txt", ".docx", ".pdf", ".html", ".htm", ".rst"}
SKIP = {"node_modules", ".git", "__pycache__", ".venv", "venv", "site-packages", "dist", "build"}
DATALESS = getattr(stat, "SF_DATALESS", 0x40000000)

ap = argparse.ArgumentParser()
ap.add_argument("--keywords", default=r"(?i)\bap\b|apush|advanced.placement|knowledge|curriculum|rubric|assessment|lesson|question|item|eval|review|brainlift|learning|feedback|instruction|practice")
ap.add_argument("roots", nargs="+")
a = ap.parse_args()
kw = re.compile(a.keywords)
rows = []
for root in a.roots:
    root = Path(root).expanduser()
    for d in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")):
        docs = dataless = hits = 0
        for dp, dns, fns in os.walk(d):
            dns[:] = [x for x in dns if x not in SKIP]
            for fn in fns:
                if Path(fn).suffix.lower() not in DOCS:
                    continue
                docs += 1
                try:
                    if os.lstat(os.path.join(dp, fn)).st_flags & DATALESS:
                        dataless += 1
                except OSError:
                    pass
                if kw.search(fn) or kw.search(os.path.relpath(dp, d)):
                    hits += 1
        rows.append((docs, dataless, hits, str(d).replace(str(Path.home()), "~")))
print("docs\tplaceholders\tkeyword-named\tfolder")
for r in sorted(rows, reverse=True):
    print("\t".join(map(str, r)))
