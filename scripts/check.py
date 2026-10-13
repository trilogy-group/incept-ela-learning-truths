#!/usr/bin/env python3
"""Check the repository before a commit. Every record follows the schema and the vocabulary; every cited file exists
(at the commit its source is pinned to, or on disk for a dated source); the pages built from the records are current;
nothing names a person or carries an attribution line; the front page stays short. Standard library only."""
import re, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, HOME, HOME_KEY, VOCAB, SOURCES, records, anchor, source_root, by_prefix
from verify_quotes_lib import git_target, member_text, split_archive

FRONT_PAGE_WORDS = 1200
from redact import ROLE_PHRASES
ATTRIBUTION = re.compile(r"co-authored-by:|generated with \[?claude", re.I)   # an attribution line, not the words "generated with"
REQUIRED = ["id", "title", "statement", "group", "role", "facets", "stage", "scope", "domains", "kind", "status",
            "detail", "against", "evidence", "citations", "found_in", "added"]
errors, warnings = [], []
_exists = {}


def exists(key, rel):
    """A path inside a registered source: at its pinned commit if it has one, else on disk."""
    if (key, rel) in _exists:
        return _exists[(key, rel)]
    root, src = source_root(key), SOURCES[key]
    if not root.exists():
        warnings.append(f"source {key} is not on this machine: {rel} not checked")
        ok = True
    elif src.get("commit"):
        rel2 = rel.rstrip("/")
        spec = f"{src['commit']}:{rel2}" if rel2 else f"{src['commit']}^{{tree}}"
        ok = subprocess.run(["git", "-C", str(root), "cat-file", "-e", spec], capture_output=True).returncode == 0
    else:
        ok = (root / rel).exists()
    _exists[(key, rel)] = ok
    return ok


def git_exists(key, e):
    """A cited commit (its message) or a file at a revision, in the repository the evidence path names."""
    if not source_root(key).exists():
        warnings.append(f"source {key} is not on this machine: {e['path']} not checked")
        return True
    field = "commit" if "commit" in e else "at"
    repo, spec = git_target(source_root(key) / e["path"], field, e[field])
    return bool(repo) and subprocess.run(["git", "-C", str(repo), "cat-file", "-e", spec], capture_output=True).returncode == 0


def check_record(r, path, runs, seen):
    name = path.name
    for k in REQUIRED:
        if k not in r:
            errors.append(f"{name}: missing {k}")
    if errors and errors[-1].startswith(name):
        return
    if r["id"] != anchor(r["title"]) or path.stem != r["id"]:
        errors.append(f"{name}: id must be the title's anchor ({anchor(r['title'])}) and the file name")
    if r["id"] in seen:
        errors.append(f"{name}: duplicate id")
    seen.add(r["id"])
    for field, vocab in [("group", VOCAB["groups"]), ("role", VOCAB["roles"]), ("scope", VOCAB["scopes"]), ("kind", VOCAB["kinds"]), ("status", VOCAB["statuses"])]:
        if r[field] not in vocab:
            errors.append(f"{name}: {field} '{r[field]}' is not in the vocabulary")
    for f in r["facets"]:
        if f not in VOCAB["facets"]:
            errors.append(f"{name}: facet '{f}' is not in the vocabulary")
    for d in r["domains"]:
        if d not in VOCAB["domains"]:
            errors.append(f"{name}: domain '{d}' is not in the vocabulary")
    if not r["facets"] or not r["domains"]:
        errors.append(f"{name}: needs at least one facet and one domain")
    if r["role"] == "method" and r["stage"] not in VOCAB["stages"]:
        errors.append(f"{name}: a method needs a stage from the vocabulary")
    if r["role"] != "method" and r["stage"] is not None:
        errors.append(f"{name}: only a method has a stage")
    if r["status"] == "open" and r["group"] != "not-settled":
        warnings.append(f"{name}: open, but not in not-settled")
    if not re.search(r"[.?]$", r["statement"].strip()):
        errors.append(f"{name}: the statement must be one sentence ending with a full stop")
    for run in r["found_in"]:
        if run not in runs:
            errors.append(f"{name}: found_in '{run}' has no folder under research/")
    if not r["evidence"] and not r["citations"]:
        errors.append(f"{name}: cites nothing")
    for e in r["evidence"]:
        if e.get("source") not in SOURCES:
            errors.append(f"{name}: evidence source '{e.get('source')}' is not registered in sources/sources.json")
        elif ("commit" in e or "at" in e) and not git_exists(e["source"], e):
            errors.append(f"{name}: cites {SOURCES[e['source']]['prefix']}/{e['path']} at {e.get('commit') or e.get('at')}, which its repository does not have")
        elif e.get("member") and exists(e["source"], e["path"]) and source_root(e["source"]).exists() and \
                member_text(source_root(e["source"]) / e["path"], e["member"]) is None:
            errors.append(f"{name}: cites {e['member']} inside {SOURCES[e['source']]['prefix']}/{e['path']}, which the archive does not hold")
        elif not ("commit" in e or "at" in e) and not exists(e["source"], e["path"]):
            errors.append(f"{name}: cites {SOURCES[e['source']]['prefix']}/{e['path']}, which does not exist where the source is pinned")
    at_rev = {(e["source"], e["path"]) for e in r["evidence"] if e.get("at")}
    for c in re.findall(r"`([^`\n]+)`", r["detail"] + "\n" + r["against"]):
        k = by_prefix(c)
        rel = c[len(SOURCES[k]["prefix"]) + 1:] if k else ""
        arc, member = split_archive(rel)
        if k and member:
            if not exists(k, arc) or source_root(k).exists() and member_text(source_root(k) / arc, member) is None:
                errors.append(f"{name}: its text cites {member} inside {SOURCES[k]['prefix']}/{arc}, which the archive does not hold")
            continue
        if k and c != SOURCES[k]["prefix"] and (k, rel) not in at_rev and not exists(k, rel):
            errors.append(f"{name}: its text cites {c}, which does not exist where the source is pinned")
    for c in r["citations"]:
        if not c.get("url", "").startswith("http"):
            errors.append(f"{name}: citation '{c.get('ref')}' has no link")


RUN_KINDS, RUN_STATUSES = ["manual", "agents", "sweep", "merge"], ["planned", "running", "recorded", "assimilated"]
SECTIONS = ["## Scope", "## Method", "## Results", "## Left out"]


def check_runs():
    """Every run folder is stored the same way (schema/RUNS.md)."""
    import json
    for d in sorted(x for x in (ROOT / "research").iterdir() if x.is_dir()):
        n = f"research/{d.name}"
        if not (d / "run.json").exists():
            errors.append(f"{n}: no run.json"); continue
        try:
            m = json.loads((d / "run.json").read_text())
        except ValueError as e:
            errors.append(f"{n}/run.json: not valid JSON ({e})"); continue
        for k in ["id", "title", "date", "kind", "status", "method", "sources", "counts"]:
            if k not in m:
                errors.append(f"{n}/run.json: missing {k}")
        if m.get("id") != d.name or not re.match(r"\d{4}-\d{2}-\d{2}-\d+-[a-z0-9-]+$", d.name):
            errors.append(f"{n}: the folder must be <date>-<n>-<slug> and match run.json's id")
        if m.get("kind") not in RUN_KINDS or m.get("status") not in RUN_STATUSES:
            errors.append(f"{n}/run.json: kind or status not allowed")
        for s_ in m.get("sources", []):
            if s_ not in SOURCES:
                errors.append(f"{n}/run.json: source '{s_}' is not registered")
        readme = (d / "README.md").read_text() if (d / "README.md").exists() else ""
        at = [readme.find(s_) for s_ in SECTIONS]
        if -1 in at or at != sorted(at):
            errors.append(f"{n}/README.md: needs the sections {', '.join(SECTIONS)}, in that order")
        kind, status = m.get("kind"), m.get("status")
        done = status in ("recorded", "assimilated")
        need = []
        if kind == "agents" and done:
            need += ["agents/"]
        if kind == "sweep":
            need += ["directions.json"] + (["args.json", "existing-order.json"] if status != "planned" else [])
            need += (["agents/", "coverage.json"] if done else []) + (["items.json", "merged.json", "onto.json", "assimilated.json"] if status == "assimilated" else [])
        if kind == "merge":
            need += ["items.json"] + (["merged.json"] if done else [])
        for f in need:
            q = d / f.rstrip("/")
            if not q.exists() or (f.endswith("/") and not any(q.glob("*.md"))):
                errors.append(f"{n}: a {kind} run that is {status} keeps {f}")


def main():
    check_runs()
    runs = {p.name for p in (ROOT / "research").iterdir() if p.is_dir() and (p / "run.json").exists()}
    seen = set()
    for p in sorted((ROOT / "learnings").glob("*.json")):
        import json
        try:
            r = json.loads(p.read_text())
        except ValueError as e:
            errors.append(f"{p.name}: not valid JSON ({e})"); continue
        check_record(r, p, runs, seen)

    sys.path.insert(0, str(ROOT / "scripts"))
    import build
    for rel, text in build.render().items():
        f = ROOT / rel
        if not f.exists() or f.read_text() != text:
            errors.append(f"{rel} is out of date: run python3 scripts/build.py")

    # names: a list kept on this machine only (.local/terms.txt; "warn: " marks a term only flagged); role phrases
    terms_file = ROOT / ".local" / "terms.txt"
    terms = [t.strip() for t in terms_file.read_text().splitlines() if t.strip() and not t.startswith("#")] if terms_file.exists() else []
    if not terms:
        warnings.append("no .local/terms.txt: names were not checked")
    tracked = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-co", "--exclude-standard"], capture_output=True, text=True).stdout.split()
    for rel in tracked:
        f = ROOT / rel
        if f.suffix not in (".md", ".json", ".py") or rel.startswith("scripts/check.py") or not f.exists():
            continue
        text = f.read_text(errors="replace")
        prose = re.sub(r"`[^`]*`", "", text)
        for phrase in ROLE_PHRASES:
            if f.suffix == ".md" and not rel.startswith("research/") and re.search(rf"\b{re.escape(phrase)}s?\b", prose, re.I):
                errors.append(f"{rel}: role phrase '{phrase}'")
        for t in terms:
            warn = t.startswith("warn: ")
            word = t[6:] if warn else t
            if warn and (rel.startswith("research/") or f.suffix != ".md"):
                continue
            flags = re.I if (warn or word.islower()) else 0
            hay = prose if warn else text
            if re.search(rf"(?<![A-Za-z]){re.escape(word)}(?![A-Za-z])", hay, flags) or \
                    not warn and re.search(rf"(?<![A-Za-z]){re.escape(word.upper())}(?![A-Za-z])", hay):
                (warnings if warn else errors).append(f"{rel}: '{word}'")
        if HOME in text or HOME_KEY in text:
            errors.append(f"{rel}: the home folder's path (record it with ~ or {{home}})")
        if ATTRIBUTION.search(text) and rel not in ("CLAUDE.md",) and not rel.startswith("research/"):
            errors.append(f"{rel}: an attribution line")
    log = subprocess.run(["git", "-C", str(ROOT), "log", "--format=%B"], capture_output=True, text=True).stdout
    if ATTRIBUTION.search(log):
        errors.append("a commit message carries an attribution line")

    readme = (ROOT / "README.md").read_text()
    words = len(re.findall(r"\S+", re.sub(r"\]\([^)]*\)", "]", readme)))
    if words > FRONT_PAGE_WORDS:
        warnings.append(f"README.md is {words} words; keep the front page under {FRONT_PAGE_WORDS}")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"{len(seen)} records, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
