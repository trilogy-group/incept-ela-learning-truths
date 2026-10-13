#!/usr/bin/env python3
"""Record one finished sweep agent as research: its brief and its final report, taken verbatim from its transcript,
with people's names redacted (the untracked .local/terms.txt) and home paths shortened to ~.
Usage: record_sweep.py <transcript.jsonl> <out.md> <title>"""
import json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from redact import scrub


def text_of(msg):
    c = msg.get("content")
    if isinstance(c, str):
        return c
    return "\n".join(b.get("text", "") for b in c or [] if isinstance(b, dict) and b.get("type") == "text")

src, out, title = sys.argv[1], Path(sys.argv[2]), sys.argv[3]
rows = [json.loads(l) for l in open(src) if l.strip()]
brief = next(text_of(r["message"]) for r in rows if r.get("type") == "user" and text_of(r.get("message", {})).strip())
report = next(text_of(r["message"]) for r in reversed(rows) if r.get("type") == "assistant" and text_of(r.get("message", {})).strip())
first, last = rows[0].get("timestamp", ""), rows[-1].get("timestamp", "")
out.write_text(scrub(f"# {title}\n\nA read-only search agent, {first[:16].replace('T', ' ')} to {last[:16].replace('T', ' ')} UTC. Its brief and its final report, verbatim.\n\n## Brief\n\n{brief.strip()}\n\n## Report\n\n{report.strip()}\n"))
print(out.name, len(report.split()), "words")
