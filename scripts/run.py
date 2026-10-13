#!/usr/bin/env python3
"""One command per step of a research run, so every run is done and stored the same way (schema/RUNS.md).
  run.py new --slug SLUG --kind sweep|agents|merge|manual --title TITLE [--date YYYY-MM-DD]
  run.py args RUN [--already FILE] [--focus TEXT]       write args.json and existing-order.json for the sweep
  run.py start RUN --run-id ID --transcript DIR [--step sweep|merge|review]
                                                         note a launched workflow's run ID and folder (the sweep marks it running)
  run.py record RUN                                      store every agent's output, coverage.json, synthesis.json
  run.py items RUN [--reports MD ...] [--journal]        write items.json and onto.json for the merge workflow
  run.py merged RUN                                      rebuild the merge workflow's result from its journal: merged.json
  run.py assimilate RUN --date YYYY-MM-DD [--dry-run]    write merged.json's records and onto.json's evidence; assimilated.json
  run.py review RUN                                      batch the run's new records and the page sections for learnings-review
  run.py reviewed RUN --date YYYY-MM-DD [--dry-run]      apply the review from its journal: fixes, drops, merges; review.json
  run.py status                                          every run, its kind, status and counts"""
import argparse, datetime, hashlib, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lib import VOCAB, anchor, expand, records, shorten
ROOT = HERE.parent
RES = ROOT / "research"
WORKFLOW = ROOT / ".claude" / "workflows" / "learnings-sweep.js"
REVIEW_WORKFLOW = ROOT / ".claude" / "workflows" / "learnings-review.js"
SECTIONS = ["## Scope", "## Method", "## Results", "## Left out"]


def folder(run):
    p = RES / run
    if not p.is_dir():
        sys.exit(f"no run folder research/{run}")
    return p


def meta(p):
    return json.loads((p / "run.json").read_text())


def save(p, m):
    (p / "run.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n")


def py(*args):
    r = subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, cwd=ROOT)
    if r.returncode:
        sys.exit(r.stderr or r.stdout)
    return r.stdout


def cmd_new(a):
    date = a.date or datetime.date.today().isoformat()
    n = 1 + max([int(m.group(1)) for d in RES.iterdir() if (m := re.match(rf"{date}-(\d+)-", d.name))] or [0])
    run = f"{date}-{n}-{a.slug}"
    p = RES / run
    p.mkdir(parents=True)
    (p / "README.md").write_text(f"# {a.title}\n\n{date}.\n\n" + "\n\n".join(f"{s}\n\nTo be written." for s in SECTIONS) + "\n")
    save(p, {"id": run, "title": a.title, "date": date, "kind": a.kind, "status": "planned", "method": {}, "sources": [], "counts": {}})
    print(run)


def cmd_args(a):
    p = folder(a.run)
    m = meta(p)
    extra = (["--already", a.already] if a.already else []) + (["--focus", a.focus] if a.focus else [])
    raw = py(HERE / "sweep_args.py", p / "directions.json", *extra)
    (p / "args.json").write_text(shorten(raw))   # the record; the copy to pass, with full paths, is in .local/args/
    (ROOT / ".local" / "args").mkdir(parents=True, exist_ok=True)
    (ROOT / ".local" / "args" / f"{a.run}.json").write_text(raw)
    dirs = json.loads((p / "directions.json").read_text())
    m["method"].update({"workflow": str(WORKFLOW.relative_to(ROOT)), "workflow_sha256": hashlib.sha256(WORKFLOW.read_bytes()).hexdigest()})
    m["sources"] = sorted({s for d in dirs for s in d.get("sources", [])} | set(m["sources"]))
    m["counts"]["directions"] = len(dirs)
    save(p, m)
    print(f"research/{a.run}/args.json: {len(dirs)} directions; pass the contents of .local/args/{a.run}.json as the Workflow tool's args")


def cmd_start(a):
    p = folder(a.run)
    m = meta(p)
    step = {"run_id": a.run_id, "transcript": shorten(Path(a.transcript).expanduser())}
    if a.step == "sweep":
        m["status"] = "running"
        m["method"].update(step)
    else:
        m["method"].setdefault(a.step, {}).update(step)
    save(p, m)
    print(f"{a.run}: {a.step} running")


def results(transcript):
    """Every agent's result in a workflow's journal, by its label."""
    rows = [json.loads(l) for l in (Path(expand(transcript)) / "journal.jsonl").read_text().splitlines() if l.strip()]
    lab = {r["agentId"]: r.get("label", "") for r in rows if r.get("type") == "started"}
    return {lab.get(r["agentId"], ""): r.get("result") for r in rows if r.get("type") == "result"}


def journal(m):
    t = Path(expand(m["method"]["transcript"]))
    rows = [json.loads(l) for l in (t / "journal.jsonl").read_text().splitlines() if l.strip()]
    lab = {r["agentId"]: r.get("label", "") for r in rows if r.get("type") == "started"}
    return t, {lab.get(r["agentId"], ""): r.get("result") for r in rows if r.get("type") == "result"}, lab


def cmd_record(a):
    p = folder(a.run)
    m = meta(p)
    t, res, lab = journal(m)
    print(py(HERE / "record_workflow.py", t, p).strip())
    reads = {k: v for k, v in res.items() if k.startswith("read:") and isinstance(v, dict)}
    verifies = [v for k, v in res.items() if k.startswith("verify:") and isinstance(v, dict)]
    kept = sum(1 for v in verifies for c in v.get("verified", []) if c.get("verdict") != "drop")
    dropped = sum(1 for v in verifies for c in v.get("verified", []) if c.get("verdict") == "drop")
    m["counts"].update({"agents": len(lab), "candidates": sum(len(v.get("candidates", [])) for v in reads.values()), "kept": kept, "dropped": dropped,
                        "gaps": sum(1 for k in lab.values() if k.startswith("read:gap:"))})
    m["status"] = "recorded"
    save(p, m)
    print(json.dumps(m["counts"]))


def cmd_items(a):
    p = folder(a.run)
    m = meta(p)
    args = [HERE / "make_merge_items.py", "--order", p / "existing-order.json", "--run-label", a.run, "--items-out", p / "items.json", "--onto-out", p / "onto.json"]
    if (p / "already-found.json").exists():
        args += ["--already", p / "already-found.json"]
    if a.journal:
        args += ["--journal", expand(m["method"]["transcript"])]
    elif (p / "synthesis.json").exists():
        args += ["--synthesis", p / "synthesis.json"]
    if a.reports:
        args += ["--reports", *a.reports]
    print(py(*args).strip())
    print(f"next: python3 scripts/merge_args.py research/{a.run}/items.json > $TMPDIR/merge-args.json, run learnings-merge, save its result as research/{a.run}/merged.json")


def cmd_merged(a):
    """Rebuild the learnings-merge workflow's result from its journal (the batches' records, then each group's merges,
    applied exactly as the workflow applies them) and save it as merged.json."""
    p = folder(a.run)
    m = meta(p)
    t = Path(expand(m["method"]["merge"]["transcript"]))
    rows = [json.loads(l) for l in (t / "journal.jsonl").read_text().splitlines() if l.strip()]
    lab = {r["agentId"]: r.get("label", "") for r in rows if r.get("type") == "started"}
    res = {lab.get(r["agentId"], ""): r.get("result") for r in rows if r.get("type") == "result"}
    batches = sorted((k for k in res if k.startswith("standardize:")), key=lambda k: int(k.split(":")[1]))
    missing = [k for k in (f"standardize:{i}" for i in range(1, m["method"]["merge"].get("batches", len(batches)) + 1)) if k not in res]
    records = [r for k in batches for r in (res[k] or {}).get("records", [])]
    onto = [x for k in batches for x in (res[k] or {}).get("onto_existing", [])]
    dropped = [x for k in batches for x in (res[k] or {}).get("dropped", [])]
    gone = set()
    for k in (k for k in res if k.startswith("dedupe:")):
        for mg in (res[k] or {}).get("merges", []):
            ki = mg["keep"]
            if ki >= len(records) or ki in gone:
                continue
            base = records[ki]
            base["statement"] = mg.get("statement") or base["statement"]
            for j in mg["merge"]:
                if j >= len(records) or j == ki or j in gone:
                    continue
                r = records[j]
                seen = {e["path"] + "|" + e.get("quote", "") for e in base["evidence"]}
                base["evidence"] += [e for e in r["evidence"] if e["path"] + "|" + e.get("quote", "") not in seen]
                urls = {c["url"] for c in base["citations"]}
                base["citations"] += [c for c in r["citations"] if c["url"] not in urls]
                base["origins"] = sorted(set(base["origins"]) | set(r["origins"]))
                base["domains"] = sorted(set(base["domains"]) | set(r["domains"]))
                if r.get("against") and r["against"] != "none found" and r["against"] not in base["against"]:
                    base["against"] = r["against"] if base["against"] == "none found" else base["against"] + " " + r["against"]
                gone.add(j)
    final = [r for i, r in enumerate(records) if i not in gone]
    sys.path.insert(0, str(HERE))
    from redact import scrub
    (p / "merged.json").write_text(scrub(json.dumps({"records": final, "onto_existing": onto, "dropped": dropped, "merged": len(gone)}, indent=1, ensure_ascii=False)) + "\n")
    m["counts"].update({"merge_batches": len(batches), "merge_records": len(final), "merge_folded": len(gone)})
    save(p, m)
    print(f"merged.json: {len(final)} records ({len(gone)} folded across batches), {len(onto)} additions to existing records, {len(dropped)} dropped" + (f"; MISSING batches: {missing}" if missing else ""))


def cmd_assimilate(a):
    p = folder(a.run)
    m = meta(p)
    added = updated = ok = dropped = unreg = 0
    new_ids, touched = [], set()
    for f in ("merged.json", "onto.json"):
        if (p / f).exists():
            out = json.loads(py(HERE / "add_records.py", p / f, "--run", a.run, "--date", a.date, "--order", p / "existing-order.json", *(["--dry-run"] if a.dry_run else [])))
            new_ids += out.pop("new_ids"); touched |= set(out.pop("touched_ids"))
            print(f, json.dumps({k: v for k, v in out.items() if k != "unregistered"}), "| first unregistered:", out["unregistered"][:5])
            added += out["new"]; updated += out["onto"]; ok += out["quotes_ok"]; dropped += out["quotes_dropped"]; unreg += out["unregistered_count"]
    if not a.dry_run:
        # which records this run made and which it added to, so later steps (the review) know what is the run's
        (p / "assimilated.json").write_text(json.dumps({"date": a.date, "added": sorted(new_ids), "updated": sorted(touched - set(new_ids))}, indent=1) + "\n")
        m["counts"].update({"records_added": added, "records_updated": updated, "quotes_checked": ok + dropped, "quotes_dropped": dropped, "evidence_unregistered": unreg})
        m["status"] = "assimilated"
        save(p, m)


def section(r):
    """The page section a record shows in, and what it holds."""
    if r["scope"] != "universal":
        return "domain", "learnings that hold only in their domain"
    if r["role"] == "criterion":
        return f"criterion:{r['facets'][0]}", f"criteria whose main facet is {r['facets'][0]} ({VOCAB['facets'][r['facets'][0]]})"
    if r["role"] == "method":
        return f"method:{r['stage']}", f"methods at the {r['stage']} stage ({VOCAB['stages'][r['stage']]})"
    return "context", "context: the limits, measures and research that bound the rest"


def tokens(r):
    return {w for w in re.findall(r"[a-z]+", (r["title"] + " " + r["statement"]).lower()) if len(w) > 3}


def cmd_review(a):
    """Write the learnings-review workflow's inputs: the run's new records in batches of 40, and every page section that
    holds one of them (old and new records together), small sections pooled, plus pairs of close records in different
    sections."""
    p = folder(a.run)
    m = meta(p)
    added = json.loads((p / "assimilated.json").read_text())["added"]
    recs = {r["id"]: r for r in records()}
    new = [recs[i] for i in added if i in recs]
    out = ROOT / ".local" / "review" / a.run
    out.mkdir(parents=True, exist_ok=True)
    for f in out.glob("*.json"):
        f.unlink()
    nb = 0
    for i in range(0, len(new), 40):
        nb += 1
        (out / f"batch-{nb:03d}.json").write_text(json.dumps(new[i:i + 40], indent=1, ensure_ascii=False))
    secs, about = {}, {}
    for r in recs.values():
        k, ab = section(r)
        secs.setdefault(k, []).append(r); about[k] = ab
    mine = set(added)
    keep = [k for k in sorted(secs) if any(r["id"] in mine for r in secs[k])]
    line = lambda r: {"id": r["id"], "title": r["title"], "statement": r["statement"], "group": r["group"], "on_record": r["id"] not in mine}
    slices, pool = [], []
    for k in keep:
        if len(secs[k]) >= 15:
            slices.append({"name": k, "about": about[k], "records": [line(r) for r in secs[k]]})
        else:
            pool.append(k)
    while pool:
        names, rs = [], []
        while pool and len(rs) + len(secs[pool[0]]) <= 60:
            k = pool.pop(0); names.append(k); rs += [line(r) for r in secs[k]]
        if not names:
            k = pool.pop(0); names.append(k); rs = [line(r) for r in secs[k]]
        slices.append({"name": " + ".join(names), "about": "; ".join(about[k] for k in names), "records": rs})
    sec_of = {r["id"]: section(r)[0] for r in recs.values()}
    tok = {i: tokens(r) for i, r in recs.items()}
    pairs = set()
    for i in mine & set(recs):
        for j in recs:
            if i == j or sec_of[i] == sec_of[j]:
                continue
            u = tok[i] | tok[j]
            if u and len(tok[i] & tok[j]) / len(u) >= 0.2:
                pairs.add(tuple(sorted((i, j))))
    pairs = sorted(pairs)
    for i in range(0, len(pairs), 60):
        chunk = pairs[i:i + 60]
        ids = sorted({x for pr in chunk for x in pr})
        slices.append({"name": f"pairs {i // 60 + 1}", "about": "pairs of close records from different sections", "pairs": [list(pr) for pr in chunk], "records": [line(recs[x]) for x in ids]})
    for n, sl in enumerate(slices, 1):
        (out / f"slice-{n:03d}.json").write_text(json.dumps(sl, indent=1, ensure_ascii=False))
    args = {"batchDir": str(out), "batchCount": nb, "sliceDir": str(out), "sliceCount": len(slices), "vocabulary": VOCAB}
    (out / "args.json").write_text(json.dumps(args, ensure_ascii=False))
    m["method"].setdefault("review", {}).update({"workflow": str(REVIEW_WORKFLOW.relative_to(ROOT)), "workflow_sha256": hashlib.sha256(REVIEW_WORKFLOW.read_bytes()).hexdigest(),
                                                "batches": nb, "slices": len(slices), "pairs": len(pairs)})
    save(p, m)
    print(f"{len(new)} new records in {nb} batches; {len(slices)} slices ({len(pairs)} cross-section pairs); args in {shorten(out / 'args.json')}")


FIELDS = ["title", "statement", "example", "detail", "group", "role", "facets", "stage", "scope", "domains", "status", "kind", "against"]


def fold(base, r, date):
    """Fold record r into base: its evidence, citations, runs and domains, and any counter-evidence."""
    base["evidence"] += [e for e in r["evidence"] if e not in base["evidence"]]
    base["citations"] += [c for c in r["citations"] if c.get("url") not in {x.get("url") for x in base["citations"]}]
    base["found_in"] = sorted(set(base["found_in"]) | set(r["found_in"]))
    base["domains"] = sorted(set(base["domains"]) | set(r["domains"]))
    if r.get("against") and r["against"] != "none found" and r["against"] not in base["against"]:
        base["against"] = r["against"] if base["against"] == "none found" else base["against"].rstrip() + " " + r["against"]
    base["updated"] = date


def change(r, ch, scrub):
    """Apply a reviewer's changes to record r, keeping only values the vocabulary allows. Returns the fields changed."""
    before = {k: r.get(k) for k in FIELDS}
    for k in FIELDS:
        if k not in ch:
            continue
        v = ch[k]
        if k in ("title", "statement", "example", "detail", "against"):
            v = scrub(str(v).strip())
            if k == "statement" and v and not re.search(r"[.?]$", v):
                v += "."
            if k in ("title", "statement", "against") and not v:
                continue
        elif k == "group" and v not in VOCAB["groups"] or k == "role" and v not in VOCAB["roles"] or k == "scope" and v not in VOCAB["scopes"] \
                or k == "status" and v not in VOCAB["statuses"] or k == "kind" and v not in VOCAB["kinds"]:
            continue
        elif k == "facets":
            v = [x for x in v if x in VOCAB["facets"]]
            if not v:
                continue
        elif k == "domains":
            v = [x for x in v if x in VOCAB["domains"]]
            if not v:
                continue
        elif k == "stage":
            v = v if v in VOCAB["stages"] else None
        if k == "example" and not v:
            r.pop("example", None)
            continue
        r[k] = v
    if r["role"] == "method" and r.get("stage") not in VOCAB["stages"]:
        r["stage"] = before["stage"] if before["stage"] in VOCAB["stages"] else "review"
    if r["role"] != "method":
        r["stage"] = None
    return [k for k in FIELDS if r.get(k) != before[k]]


def cmd_reviewed(a):
    p = folder(a.run)
    m = meta(p)
    from redact import scrub
    res = results(m["method"]["review"]["transcript"])
    assim = json.loads((p / "assimilated.json").read_text())
    mine = set(assim["added"])
    recs = {r["id"]: r for r in records()}
    log = {"date": a.date, "fixes": [], "drops": [], "merges": [], "flags": [], "skipped": []}
    gone, renamed, touched = set(), {}, set()
    reviews = [res[k] or {} for k in sorted(res) if k.startswith("review:")]
    for rv in reviews:
        for d in rv.get("drops", []):
            if d["id"] in mine and d["id"] in recs and d["id"] not in gone:
                gone.add(d["id"]); log["drops"].append({"id": d["id"], "statement": recs[d["id"]]["statement"], "why": scrub(d["why"])})
            else:
                log["skipped"].append({"drop": d["id"], "why": "not this run's record"})
        log["flags"] += [{"id": f["id"], "issue": scrub(f["issue"])} for f in rv.get("flags", [])]
    for rv in reviews:
        for f in rv.get("fixes", []):
            i = f["id"]
            if i not in mine or i not in recs or i in gone:
                log["skipped"].append({"fix": i, "why": "not this run's record, or dropped"}); continue
            r = recs[i]
            before = {k: r.get(k) for k in FIELDS}
            done = change(r, f.get("changes", {}), scrub)
            if "title" in done:
                nid = anchor(r["title"])
                if nid != i and (nid in recs or nid in renamed.values()):
                    r["title"] = before["title"]; done.remove("title")
                elif nid != i:
                    renamed[i] = nid
            if done:
                r["updated"] = a.date; touched.add(i)
                log["fixes"].append({"id": i, "changed": {k: {"from": before[k], "to": r.get(k)} for k in done}, "why": scrub(f.get("why", ""))})
    for k in sorted(res):
        if not k.startswith("dedupe:"):
            continue
        for mg in (res[k] or {}).get("merges", []):
            keep = mg["keep"]
            if keep not in recs or keep in gone:
                log["skipped"].append({"merge": [keep] + mg["merge"], "why": "kept record missing or dropped"}); continue
            folded, was = [], []
            for j in mg["merge"]:
                if j == keep or j not in recs or j in gone:
                    continue
                if j not in mine:
                    log["skipped"].append({"merge": [keep, j], "why": f"{j} was on record before this run"}); continue
                was.append({"id": j, "statement": recs[j]["statement"], "detail": recs[j]["detail"]})   # kept in review.json, so nothing folded is lost
                fold(recs[keep], recs[j], a.date); gone.add(j); folded.append(j)
            if not folded:
                continue
            if keep in mine and mg.get("statement"):
                st = scrub(mg["statement"].strip())
                recs[keep]["statement"] = st if re.search(r"[.?]$", st) else st + "."
            touched.add(keep)
            log["merges"].append({"keep": keep, "folded": folded, "statement": recs[keep]["statement"], "folded_records": was, "why": scrub(mg.get("why", ""))})
    print(f"fixes {len(log['fixes'])}, drops {len(log['drops'])}, merges {len(log['merges'])} ({sum(len(x['folded']) for x in log['merges'])} folded), "
          f"flags {len(log['flags'])}, renamed {len(renamed)}, skipped {len(log['skipped'])}")
    if a.dry_run:
        return
    L = ROOT / "learnings"
    for i in gone:
        (L / f"{i}.json").unlink(missing_ok=True)
    for i in touched - gone:
        r = recs[i]
        nid = renamed.get(i, i)
        if nid != i:
            (L / f"{i}.json").unlink(missing_ok=True); r["id"] = nid
        (L / f"{nid}.json").write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n")
    assim["added"] = sorted(renamed.get(i, i) for i in assim["added"] if i not in gone)
    assim["review"] = {"date": a.date, "dropped": sorted(x["id"] for x in log["drops"]), "renamed": renamed,
                       "folded_into": {j: renamed.get(x["keep"], x["keep"]) for x in log["merges"] for j in x["folded"]}}
    (p / "assimilated.json").write_text(json.dumps(assim, indent=1) + "\n")
    (p / "review.json").write_text(json.dumps(log, indent=1, ensure_ascii=False) + "\n")
    m["counts"].update({"review_fixes": len(log["fixes"]), "review_drops": len(log["drops"]), "review_folded": sum(len(x["folded"]) for x in log["merges"]),
                        "review_flags": len(log["flags"]), "records_after_review": len(assim["added"])})
    save(p, m)


def cmd_status(a):
    for d in sorted(x for x in RES.iterdir() if x.is_dir()):
        f = d / "run.json"
        if not f.exists():
            print(f"{d.name:40s} (no run.json)"); continue
        m = json.loads(f.read_text())
        c = m.get("counts", {})
        print(f"{d.name:40s} {m['kind']:7s} {m['status']:11s} " + " ".join(f"{k}={v}" for k, v in c.items()))


ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
sub = ap.add_subparsers(dest="cmd", required=True)
s = sub.add_parser("new"); s.add_argument("--slug", required=True); s.add_argument("--kind", required=True, choices=["manual", "agents", "sweep", "merge"]); s.add_argument("--title", required=True); s.add_argument("--date")
s = sub.add_parser("args"); s.add_argument("run"); s.add_argument("--already"); s.add_argument("--focus")
s = sub.add_parser("start"); s.add_argument("run"); s.add_argument("--run-id", required=True); s.add_argument("--transcript", required=True); s.add_argument("--step", default="sweep", choices=["sweep", "merge", "review"])
s = sub.add_parser("record"); s.add_argument("run")
s = sub.add_parser("items"); s.add_argument("run"); s.add_argument("--reports", nargs="*"); s.add_argument("--journal", action="store_true")
s = sub.add_parser("merged"); s.add_argument("run")
s = sub.add_parser("assimilate"); s.add_argument("run"); s.add_argument("--date", required=True); s.add_argument("--dry-run", action="store_true")
s = sub.add_parser("review"); s.add_argument("run")
s = sub.add_parser("reviewed"); s.add_argument("run"); s.add_argument("--date", required=True); s.add_argument("--dry-run", action="store_true")
sub.add_parser("status")
a = ap.parse_args()
globals()[f"cmd_{a.cmd}"](a)
