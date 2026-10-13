#!/usr/bin/env python3
"""Write a run's findings into learnings/: new records from its records list, and its evidence for or against records
already there. Accepts the learnings-sweep synthesis shape ({records, added_evidence, counter_to_existing, dropped}) or
the learnings-merge shape ({records, onto_existing, dropped}). Every evidence path must sit inside a registered source;
every quote is checked against its file, and one that isn't found verbatim is left out (its path stays). A quote that
names someone or a job role keeps only its longest verbatim stretch without it, if that has six words or more; evidence
from a file whose name carries a person's name is left out. Numbers in a
sweep's output are mapped to ids through the run's existing-order.json.
Usage: add_records.py FINDINGS.json --run RUN --date YYYY-MM-DD [--order existing-order.json] [--dry-run]"""
import argparse, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, SOURCES, anchor, cite_paths, expand, source_root
from verify_quotes_lib import quote_found, git_quote_found, split_archive
from redact import scrub, ROLE_PHRASES

ap = argparse.ArgumentParser()
ap.add_argument("findings")
ap.add_argument("--run", required=True)
ap.add_argument("--date", required=True)
ap.add_argument("--order")
ap.add_argument("--dry-run", action="store_true")
a = ap.parse_args()
F = json.loads(Path(a.findings).read_text())
order = json.loads(Path(a.order).read_text()) if a.order else []
roots = sorted(((k, str(source_root(k))) for k in SOURCES), key=lambda x: -len(x[1]))
stats = {"new": 0, "onto": 0, "quotes_ok": 0, "quotes_trimmed": 0, "quotes_dropped": 0, "name_paths": 0, "unregistered": [], "collisions": []}
ROLES = re.compile(r"\b(?:" + "|".join(re.escape(p) for p in ROLE_PHRASES) + r")s?\b", re.I)


def locate(p):
    full = str(Path(expand(p)).resolve()) if p.startswith(("/", "~")) else None
    if full:
        for k, r in roots:
            if full == r or full.startswith(r + "/"):
                return k, full[len(r) + 1:]
    for k, s in sorted(SOURCES.items(), key=lambda x: -len(x[1]["prefix"])):
        if p.startswith(s["prefix"] + "/"):
            full = str(source_root(k) / p[len(s["prefix"]) + 1:])
            for k2, r in roots:
                if full == r or full.startswith(r + "/"):
                    return k2, full[len(r) + 1:]
            return k, p[len(s["prefix"]) + 1:]
    return None, None


# how readers cite a commit's message, or a file read at a revision: (pattern, evidence field)
GIT_FORMS = [(re.compile(r"^(.+?) \(git commit ([0-9a-f]{7,40})\)$"), "commit"),
             (re.compile(r"^(.+?)/\.git \(commit ([0-9a-f]{7,40}) message\)$"), "commit"),
             (re.compile(r"^(.+?) \(deleted in commit [0-9a-f]{7,40}; read with git show ([0-9a-f]{7,40}\^?):.+\)$"), "at")]


def git_ref(p):
    for rx, field in GIT_FORMS:
        m = rx.match(p)
        if m:
            return m.group(1), field, m.group(2)
    return p, None, None


def name_free(q):
    """A quote that names someone or a job role, or carries a home path, keeps its longest verbatim stretch without them, when that
    stretch has at least six words; otherwise it is left out."""
    s = ROLES.sub("[name]", scrub(q))
    if s == q and "[name]" not in q:
        return q
    parts = [x.strip(" ,;:.-\"'“”‘’()") for x in re.split(r"(?:the |a |an )?\[name\](?:'s|’s)?|~\S*", s)]
    best = max(parts, key=len, default="")
    if len(best.split()) >= 6:
        stats["quotes_trimmed"] += 1; return best
    stats["quotes_dropped"] += 1; return ""


def evidence(items):
    out = []
    for e in items:
        if "[name]" in e["path"] or scrub(e["path"]) != e["path"]:
            stats["name_paths"] += 1; continue   # its file name carries a person's name: left out
        path, field, rev = git_ref(e["path"])
        k, rel = locate(path)
        if not k:
            stats["unregistered"].append(e["path"]); continue
        arc, member = split_archive(rel)
        item = {"source": k, "path": arc, **({"member": member} if member else {}), **({field: rev} if field else {})}
        if e.get("lines"):
            item["lines"] = e["lines"]
        q = name_free((e.get("quote") or "").strip())
        if q:
            if (git_quote_found(source_root(k) / rel, field, rev, q) if field else quote_found(str(source_root(k) / arc) + (f"::{member}" if member else ""), q)):
                item["quote"], item["verified"] = q, "script"; stats["quotes_ok"] += 1
            else:
                stats["quotes_dropped"] += 1
        if item not in out:
            out.append(item)
    return out


RUNS = sorted(p.name for p in (ROOT / "research").iterdir() if p.is_dir())


# an origin can name an agent's report ("agents/NAME#3"): it belongs to the one run whose agents/ holds NAME.md
AGENT_RUN = {}
for run in RUNS:
    for f in (ROOT / "research" / run / "agents").glob("*.md"):
        AGENT_RUN.setdefault(f.stem, set()).add(run)


def runs_of(origins):
    runs = {run for run in RUNS for o in origins if o.startswith(run + "/") or o.startswith(run + ":") or o == run}
    for o in origins:
        m = re.match(r"agents/([^#:/]+)", o)
        if m and len(AGENT_RUN.get(m.group(1), ())) == 1:
            runs |= AGENT_RUN[m.group(1)]
    return runs


def found_in(r):
    """The runs a record came from: those its origins name, and this run."""
    return sorted(runs_of(r.get("origins", [])) | {a.run})


# a record a review folded into another, or renamed, answers to its old id (each run's assimilated.json keeps the map)
ALIAS = {}
for f in sorted((ROOT / "research").glob("*/assimilated.json")):
    rv = json.loads(f.read_text()).get("review", {})
    ALIAS.update(rv.get("renamed", {})); ALIAS.update(rv.get("folded_into", {}))


def resolve(i):
    seen = set()
    while i in ALIAS and i not in seen:
        seen.add(i); i = ALIAS[i]
    return i


def to_id(n):
    if isinstance(n, int):
        return resolve(order[n - 1]) if 0 < n <= len(order) else None
    return resolve(str(n).lstrip("#"))


writes, new_ids, touched = {}, [], set()
for r in F.get("records", []):
    rid = anchor(r["title"])
    path = ROOT / "learnings" / f"{rid}.json"
    if path.exists() or rid in writes:
        # the same title again: fold its evidence and citations into the record already there
        base = writes.get(rid) or json.loads(path.read_text())
        ev = evidence(r.get("evidence", []))
        base["evidence"] += [e for e in ev if e not in base["evidence"]]
        base["citations"] += [c for c in r.get("citations", []) if c not in base["citations"]]
        base["found_in"] = sorted(set(base["found_in"]) | set(found_in(r)))
        base["updated"] = a.date
        writes[rid] = base; stats["collisions"].append(rid); touched.add(rid); continue
    role = r["role"]
    rec = {"id": rid, "title": r["title"], "statement": r["statement"].strip(), **({"example": r["example"].strip()} if r.get("example", "").strip() else {}),
           "group": r["group"], "role": role, "facets": r["facets"] or ["review"], "stage": (r.get("stage") if role == "method" and r.get("stage") not in (None, "none") else None),
           "scope": r["scope"], "domains": r["domains"] or ["research"], "kind": r["kind"], "status": r["status"],
           "detail": r["detail"].strip(), "against": (r.get("against") or "none found").strip(), "evidence": evidence(r.get("evidence", [])),
           "citations": r.get("citations", []), "found_in": found_in(r), "added": a.date}
    if role == "method" and rec["stage"] is None:
        rec["stage"] = "review"
    writes[rid] = rec; stats["new"] += 1; new_ids.append(rid)

additions = [(x.get("truth"), x, "supports") for x in F.get("added_evidence", [])] + [(x.get("truth"), x, "counter") for x in F.get("counter_to_existing", [])]
additions += [(x["id"], {"evidence": x.get("evidence", []), "summary": x.get("note", ""), "origins": x.get("origins", [])}, x.get("effect", "supports")) for x in F.get("onto_existing", [])]
for key, x, effect in additions:
    rid = to_id(key)
    p = ROOT / "learnings" / f"{rid}.json" if rid else None
    if not p or not p.exists():
        continue
    rec = writes.get(rid) or json.loads(p.read_text())
    ev = evidence(x.get("evidence") or [{"path": x["path"], "lines": x.get("lines", ""), "quote": x.get("quote", "")}])
    rec["evidence"] += [e for e in ev if e not in rec["evidence"]]
    if effect == "counter" and ev:
        e = ev[0]
        note = (x.get("summary") or "").strip().rstrip(".")
        cite = f"`{SOURCES[e['source']]['prefix']}/{e['path']}`"
        line = f"A later run found{': ' + note if note else ' counter-evidence'} ({cite})."
        rec["against"] = line if rec["against"] == "none found" else rec["against"].rstrip() + " " + line
    rec["found_in"] = sorted(set(rec["found_in"]) | {a.run} | runs_of(x.get("origins", [])))
    rec["updated"] = a.date
    writes[rid] = rec; stats["onto"] += 1; touched.add(rid)

for rec in writes.values():
    for k in ("title", "statement", "example", "detail", "against"):
        if isinstance(rec.get(k), str):
            rec[k] = scrub(cite_paths(rec[k]))
if not a.dry_run:
    for rid, rec in writes.items():
        (ROOT / "learnings" / f"{rid}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n")
print(json.dumps({**stats, "unregistered_count": len(stats["unregistered"]), "unregistered": sorted(set(stats["unregistered"]))[:20],
                  "new_ids": new_ids, "touched_ids": sorted(touched - set(new_ids)), "written": 0 if a.dry_run else len(writes)}, indent=1))
