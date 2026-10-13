#!/usr/bin/env python3
"""Record a finished learnings-sweep (or learnings-merge) workflow run as research. Reads the run's transcript folder
(journal.jsonl and agent-<id>.jsonl) and writes, under research/<run>/: agents/<label>.md for every agent (its brief,
verbatim, and its structured result), synthesis.json (the synthesize agent's result) and coverage.json (each reader's
coverage), all with names redacted and home paths shortened.
Usage: record_workflow.py <transcript-dir> <research/run-folder>"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from redact import scrub


def text_of(msg):
    c = msg.get("content")
    if isinstance(c, str):
        return c
    return "\n".join(b.get("text", "") for b in c or [] if isinstance(b, dict) and b.get("type") == "text")


src, out = Path(sys.argv[1]).expanduser(), Path(sys.argv[2])
rows = [json.loads(l) for l in (src / "journal.jsonl").read_text().splitlines() if l.strip()]
labels = {r["agentId"]: r.get("label", r["agentId"]) for r in rows if r.get("type") == "started"}
results = {r["agentId"]: r.get("result") for r in rows if r.get("type") == "result"}
(out / "agents").mkdir(parents=True, exist_ok=True)
coverage, n = [], 0
for aid, label in labels.items():
    t = src / f"agent-{aid}.jsonl"
    brief = ""
    if t.exists():
        for l in t.read_text().splitlines():
            r = json.loads(l) if l.strip() else {}
            if r.get("type") == "user" and text_of(r.get("message", {})).strip():
                brief = text_of(r["message"]); break
    res = results.get(aid)
    safe = re.sub(r"[^A-Za-z0-9._-]+", "-", label)
    (out / "agents" / f"{safe}.md").write_text(scrub(f"# {label}\n\nThe agent's brief, verbatim, and its structured result.\n\n## Brief\n\n{brief.strip()}\n\n## Result\n\n```json\n{json.dumps(res, indent=1, ensure_ascii=False)}\n```\n"))
    n += 1
    if label == "synthesize" and res is not None:
        (out / "synthesis.json").write_text(scrub(json.dumps(res, indent=1, ensure_ascii=False)) + "\n")
    if label.startswith("read:") and isinstance(res, dict):
        coverage.append({"direction": label[5:], "candidates": len(res.get("candidates", [])), **res.get("coverage", {})})
(out / "coverage.json").write_text(scrub(json.dumps(coverage, indent=1, ensure_ascii=False)) + "\n")
print(f"recorded {n} agents ({len(results)} with results) into {out}")
