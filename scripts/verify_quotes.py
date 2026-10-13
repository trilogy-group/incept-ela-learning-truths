#!/usr/bin/env python3
"""Check that each evidence quote appears in its file: verbatim after whitespace and quote-mark normalisation, and
near the cited lines. Reads a JSON list of {id, path, lines, quote} on stdin; prints one verdict per item. Read-only."""
import json, re, sys, subprocess
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import expand

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
    s = re.sub(r"\*\*|__|`", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()

def text_of(p):
    suf = p.suffix.lower()
    if suf in (".docx", ".html", ".htm", ".rtf"):
        return subprocess.run(["textutil", "-convert", "txt", "-stdout", str(p)], capture_output=True, text=True).stdout
    if suf == ".pdf":
        return subprocess.run(["pdftotext", str(p), "-"], capture_output=True, text=True).stdout
    return p.read_text(errors="replace")

out = []
for it in json.load(sys.stdin):
    p = Path(expand(it["path"]))
    q = it["quote"].strip().strip('"').strip("“”")
    # a quote may elide with … or ...; every part of it must be found
    parts = [x for x in re.split(r"\s*(?:…|\.\.\.)\s*", q) if len(x.strip()) >= 6]
    if not p.exists():
        out.append({**it, "verdict": "no-file"}); continue
    try:
        body = text_of(p)
    except Exception as e:
        out.append({**it, "verdict": f"unreadable: {e}"}); continue
    nb = norm(body)
    found = all(norm(x) in nb for x in parts) if parts else False
    near = None
    if found:
        lines = body.splitlines()
        first = norm(parts[0])[:40]
        hits = [i + 1 for i, l in enumerate(lines) if first[:25] in norm(l)]
        m = re.match(r"\D*(\d+)", it.get("lines", ""))
        if m and hits:
            near = min(abs(h - int(m.group(1))) for h in hits)
    out.append({**it, "verdict": "ok" if found else "not-found", "line_offset": near})
json.dump(out, sys.stdout, indent=1)
