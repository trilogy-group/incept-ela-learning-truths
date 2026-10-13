#!/usr/bin/env python3
"""Prepare findings for the learnings-merge workflow. Free-text reports (round-style: numbered bold candidates, then
sections of borderline items and evidence on statements already on record) are split into one item per candidate; a
sweep's synthesis in the first workflow's shape ({truths, added_evidence, counter_to_existing}) becomes one item per
truth. Every "#N" is rewritten as the record id it meant, through the run's existing-order file, and evidence that a
synthesis filed on a record already there goes to onto.json for add_records.py instead.
Usage: make_merge_items.py --order ORDER.json [--synthesis SYNTH.json --run-label LABEL] [--reports R.md ...]
                           --items-out ITEMS.json [--onto-out ONTO.json] [--already ALREADY.json]"""
import argparse, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from redact import scrub

ap = argparse.ArgumentParser()
ap.add_argument("--order", required=True)
ap.add_argument("--synthesis")
ap.add_argument("--run-label", default="run")
ap.add_argument("--reports", nargs="*", default=[])
ap.add_argument("--report-order", help="existing-order file the reports were numbered by (defaults to --order)")
ap.add_argument("--already", help="labels for order entries that are not records yet (e.g. ap-round-2:N)")
ap.add_argument("--journal", help="a sweep's transcript folder: take its verified candidates directly (when its synthesis is missing)")
ap.add_argument("--items-out", required=True)
ap.add_argument("--onto-out")
a = ap.parse_args()
order = json.loads(Path(a.order).read_text())
rorder = json.loads(Path(a.report_order).read_text()) if a.report_order else order
already = json.loads(Path(a.already).read_text()) if a.already else []


def name_of(o, n):
    if not (0 < n <= len(o)):
        return f"#{n}"
    rid = o[n - 1]
    if rid.startswith("ap-round-2:"):
        k = int(rid.split(":")[1])
        return f"[the round-2 learning: {already[k - 1]}]" if k <= len(already) else f"#{n}"
    return f"[record {rid}]"


def renumber(text, o):
    return re.sub(r"#(\d+)\b", lambda m: name_of(o, int(m.group(1))), text)


items, onto = [], []
for rp in a.reports:
    p = Path(rp)
    body = p.read_text()
    body = body.split("## Report", 1)[-1]
    first = re.search(r"(?m)^\*\*\d+\.\s", body)
    legend = body[: first.start()].strip()[:2500] if first else ""
    prefix = f"Path legend for this report (expand abbreviated paths with it):\n{legend}\n\n" if legend else ""
    # candidates: blocks that start with a bold "N." heading, up to the next one or the next section heading
    blocks = re.split(r"(?m)^(?=\*\*\d+\.\s)", body)
    head_cut = re.compile(r"(?m)^(?:#+\s|\*\*(?:Borderline|Evidence (?:bearing|on)|Counter-examples|On your existing|Files with people)[^*]*\*\*)")
    tail = ""
    for b in blocks:
        if not re.match(r"\*\*\d+\.\s", b):
            continue
        m = head_cut.search(b)
        cand, rest = (b[: m.start()], b[m.start():]) if m else (b, "")
        n = re.match(r"\*\*(\d+)\.", b).group(1)
        items.append({"origin": f"{p.parent.name}/{p.stem}#{n}", "text": prefix + renumber(cand.strip(), rorder)})
        tail += rest
    for sec in re.split(r"(?m)^(?=#+\s|\*\*(?:Borderline|Evidence (?:bearing|on)|Counter-examples|On your existing)[^*]*\*\*)", tail):
        if re.match(r"(?:#+\s*)?\**(?:Evidence (?:bearing|on)|Counter-examples|On your existing)", sec.strip(), re.I):
            items.append({"origin": f"{p.parent.name}/{p.stem}#evidence-on-records", "text": prefix + "Evidence on records already there (attach each to the record named; do not make new records from it):\n" + renumber(sec.strip(), rorder)})

if a.synthesis:
    S = json.loads(Path(a.synthesis).read_text())
    for t in S.get("truths", []):
        t = dict(t)
        noe = t.get("new_or_existing", "new")
        if noe.startswith("adds to #"):
            t["new_or_existing"] = renumber(noe, order).replace("adds to", "refines")
        items.append({"origin": f"{a.run_label}:{'+'.join(t.get('sources', []))}", "text": json.dumps(t, ensure_ascii=False)})
    for kind, effect in (("added_evidence", "supports"), ("counter_to_existing", "counter")):
        for x in S.get(kind, []):
            n = x.get("truth")
            rid = order[n - 1] if isinstance(n, int) and 0 < n <= len(order) else None
            ev = [{"path": x["path"], "lines": x.get("lines", ""), "quote": x.get("quote", "")}]
            if rid and not rid.startswith("ap-round-2:"):
                onto.append({"id": rid, "effect": effect, "note": x.get("summary", ""), "evidence": ev, "origins": [a.run_label]})
            else:
                items.append({"origin": f"{a.run_label}:{kind}", "text": f"{'Counter-evidence' if effect == 'counter' else 'Evidence'} for {name_of(order, n) if isinstance(n, int) else n}: {x.get('summary', '')} \"{x.get('quote', '')}\" ({x['path']}, lines {x.get('lines', '')})"})

if a.journal:
    rows = [json.loads(l) for l in (Path(a.journal).expanduser() / "journal.jsonl").read_text().splitlines() if l.strip()]
    lab = {r["agentId"]: r.get("label", "") for r in rows if r.get("type") == "started"}
    res = {lab.get(r["agentId"], ""): r.get("result") for r in rows if r.get("type") == "result"}
    for label, v in res.items():
        if not label.startswith("verify:") or not isinstance(v, dict):
            continue
        reader = res.get("read:" + label[len("verify:"):]) or {}
        cands = reader.get("candidates", [])
        for c in v.get("verified", []):
            if c.get("verdict") == "drop" or c.get("name_bearing_source"):
                continue
            src = cands[c["index"]] if 0 <= c.get("index", -1) < len(cands) else {}
            item = {**c, "found_by": src.get("found_by", ""), "scope_note": src.get("scope_note", ""), "adds_to_existing": src.get("adds_to_existing", [])}
            items.append({"origin": f"{a.run_label}:{label[len('verify:'):]}", "text": renumber(json.dumps(item, ensure_ascii=False), order)})
        for e in v.get("existing_checked", []):
            n = e.get("truth")
            rid = order[n - 1] if isinstance(n, int) and 0 < n <= len(order) else None
            if e.get("ok") and rid and not rid.startswith("ap-round-2:"):
                onto.append({"id": rid, "effect": "counter" if e.get("effect") == "counter" else "supports", "note": "", "evidence": [{"path": e["path"], "lines": e.get("lines", ""), "quote": e.get("quote", "")}], "origins": [a.run_label]})
            elif e.get("ok") and rid:
                # a learning found in an earlier run that is not a record yet: offer it as a candidate with this evidence,
                # so the merge folds it into the record that run's own candidate becomes
                items.append({"origin": f"{a.run_label}:{label[len('verify:'):]}", "text": f"Candidate learning: {name_of(order, n)}. {'Counter-evidence' if e.get('effect') == 'counter' else 'Evidence'}: \"{e.get('quote', '')}\" ({e['path']}, lines {e.get('lines', '')})."})

Path(a.items_out).write_text(scrub(json.dumps(items, indent=1, ensure_ascii=False)) + "\n")
if a.onto_out:
    Path(a.onto_out).write_text(scrub(json.dumps({"onto_existing": onto}, indent=1, ensure_ascii=False)) + "\n")
print(f"{len(items)} items, {len(onto)} additions to existing records")
