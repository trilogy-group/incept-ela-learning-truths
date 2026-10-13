#!/usr/bin/env python3
"""Render the pages people read from the records: groups/<group>.md, PERFECT-QUESTION.md (criteria by facet),
GENERATING.md (methods by stage) and the generated part of README.md. Run after any change to learnings/;
scripts/check.py fails when a page is out of date."""
import re, sys, json
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, VOCAB, SOURCES, records

ROLE_ORDER = list(VOCAB["roles"])
STATUS_ORDER = VOCAB["statuses"]
START, END = "<!-- generated: start -->", "<!-- generated: end -->"


def link(r, base=""):
    return f"{base}groups/{r['group']}.md#{r['id']}"


def core_cards(filename, key):
    path = ROOT / "public" / filename
    return json.loads(path.read_text()).get(key, []) if path.exists() else []


def card_anchor(card):
    return re.sub(r"[^a-z0-9 -]", "", f"{card['id']}-{card['title']}".lower()).replace(" ", "-")


def compact_core(cards, destination, title, include_anchors=True):
    if not cards:
        return []
    return ["", f"## {title}", "", "Conditional draft. Follow each card for its applicability, evidence and counterexamples; independent qualification remains open.", "", "| Card | Check |", "| --- | --- |"] + [f"| [{card['id']}]({destination}{'#' + card_anchor(card) if include_anchors else ''}) | {card['title']} |" for card in cards] + ["", "## Full evidence library", ""]


def runs():
    out = []
    for d in sorted(p for p in (ROOT / "research").iterdir() if p.is_dir()):
        readme = d / "README.md"
        title = readme.read_text().splitlines()[0].lstrip("# ").strip() if readme.exists() else d.name
        out.append((d.name, title))
    return out


def order(rs):
    return sorted(rs, key=lambda r: (ROLE_ORDER.index(r["role"]), STATUS_ORDER.index(r["status"]), r["title"].lower()))


def cite(e):
    s = SOURCES[e["source"]]
    rev = f" (commit {e['commit']})" if e.get("commit") else f" (at {e['at']})" if e.get("at") else f" ({e['member']} inside it)" if e.get("member") else ""
    return f"`{s['prefix']}/{e['path']}`" + rev + (f" ({e['lines']})" if e.get("lines") else "")


def record_md(r):
    meta = [r["role"], ", ".join(r["facets"]), r["scope"], "from " + ", ".join(r["domains"]), r["kind"], r["status"]]
    if r.get("stage"):
        meta.insert(1, f"stage: {r['stage']}")
    found = ", ".join(f"[{run}](../research/{run}/)" for run in r["found_in"])
    parts = [f"### {r['title']}", " ".join(x for x in [r["statement"], r.get("example", "")] if x), r["detail"].strip()]
    quoted = [e for e in r["evidence"] if e.get("quote")]
    if quoted:
        parts.append("Quoted:\n\n" + "\n".join(f"- {cite(e)}: “{e['quote']}”" for e in quoted))
    if r["citations"]:
        parts.append("Published: " + " · ".join(f"[{c['ref']}]({c['url']})" for c in r["citations"]))
    parts.append(f"Against: {r['against'].strip()}")
    parts.append(f"<sub>{' · '.join(meta)} · found in {found}</sub>")
    return "\n\n".join(parts)


def render():
    rs = records()
    pages = {}
    for g, title in VOCAB["groups"].items():
        mine = order([r for r in rs if r["group"] == g])
        if not mine:
            continue
        head = (f"# {title}\n\n{len(mine)} learnings. Each says where it came from and what argues against it. "
                "[What a perfect question is](../PERFECT-QUESTION.md) collects the criteria by facet, and "
                "[How to generate perfect questions](../GENERATING.md) collects the methods by stage.")
        pages[f"groups/{g}.md"] = head + "\n\n" + "\n\n".join(record_md(r) for r in mine) + "\n"

    universal = [r for r in rs if r["scope"] == "universal"]
    crit = [r for r in universal if r["role"] == "criterion"]
    lines = ["# What a perfect question is", "",
             f"The universal criteria on record, {len(crit)} of them, by the part of a question or lesson they govern. Each "
             "links to its record, which says where it came from and what argues against it. A criterion marked contested "
             "or open is not settled. Criteria that hold only in one domain are on its page under [domains/](domains/); how to "
             "make questions that meet them is in [GENERATING.md](GENERATING.md)."]
    for f, about in VOCAB["facets"].items():
        mine = order([r for r in crit if r["facets"][0] == f])
        if mine:
            lines += ["", f"## {f.replace('-', ' ').capitalize()}: {about}", ""]
            for r in mine:
                mark = "" if r["status"] == "held" else f" ({r['status']})"
                lines.append(f"- {r['statement']}{mark} [record]({link(r)})")
    pages["PERFECT-QUESTION.md"] = "\n".join(lines) + "\n"

    meth = [r for r in universal if r["role"] == "method"]
    lines = ["# How to generate perfect questions", "",
             f"The universal methods on record, {len(meth)} of them, in the order a question is made. Each links to its record. "
             "Methods that hold only in one domain are on its page under [domains/](domains/); the criteria they serve are in "
             "[PERFECT-QUESTION.md](PERFECT-QUESTION.md)."]
    lines += compact_core(core_cards("generation-standard.json", "cards"), "public/generation-standard.json", "Short core: generation", include_anchors=False)
    for i, (s, about) in enumerate(VOCAB["stages"].items(), 1):
        mine = order([r for r in meth if r["stage"] == s])
        if mine:
            lines += ["", f"## {i}. {s.capitalize()}: {about}", ""]
            lines += [f"- {r['statement']} [record]({link(r)})" for r in mine]
    pages["GENERATING.md"] = "\n".join(lines) + "\n"

    # a page per domain for the learnings that hold only there: criteria by facet, methods by stage, then context
    for d, label in VOCAB["domains"].items():
        mine = [r for r in rs if r["scope"] == "domain" and d in r["domains"]]
        if not mine or d == "research":
            continue
        lines = [f"# {label}", "", f"{len(mine)} learnings that hold in {label} work rather than everywhere. The universal ones are in "
                 "[PERFECT-QUESTION.md](../PERFECT-QUESTION.md) and [GENERATING.md](../GENERATING.md)."]
        dc = [r for r in mine if r["role"] == "criterion"]
        if dc:
            lines += ["", "## What a perfect question is, here"]
            for f, about in VOCAB["facets"].items():
                fm = order([r for r in dc if r["facets"][0] == f])
                if fm:
                    lines += ["", f"### {f.replace('-', ' ').capitalize()}: {about}", ""] + [f"- {r['statement']} [record](../{link(r)})" for r in fm]
        dm = [r for r in mine if r["role"] == "method"]
        if dm:
            lines += ["", "## How to generate them, here"]
            for i, (st, about) in enumerate(VOCAB["stages"].items(), 1):
                sm = order([r for r in dm if r["stage"] == st])
                if sm:
                    lines += ["", f"### {i}. {st.capitalize()}: {about}", ""] + [f"- {r['statement']} [record](../{link(r)})" for r in sm]
        cx = order([r for r in mine if r["role"] == "context"])
        if cx:
            lines += ["", "## Context", ""] + [f"- {r['statement']} [record](../{link(r)})" for r in cx]
        pages[f"domains/{d}.md"] = "\n".join(lines) + "\n"

    roles, doms, kinds, stats = Counter(r["role"] for r in rs), Counter(d for r in rs for d in r["domains"]), Counter(r["kind"] for r in rs), Counter(r["status"] for r in rs)
    gen = [START, "", "## What is here", "",
           f"{len(rs)} learnings: {roles['criterion']} criteria, {roles['method']} methods and {roles['context']} on context. "
           f"Where the evidence came from: " + ", ".join(f"{VOCAB['domains'][d]} in {doms[d]}" for d in VOCAB["domains"] if doms[d]) + " (a learning can draw on several). "
           f"{stats['held']} are held, {stats['contested']} contested and {stats['open']} open.", "",
           "- [What a perfect question is](PERFECT-QUESTION.md): the criteria, by facet",
           "- [How to generate perfect questions](GENERATING.md): the methods, by stage"]
    gen += [f"- [{t}](groups/{g}.md): {sum(1 for r in rs if r['group'] == g)}" for g, t in VOCAB["groups"].items() if any(r["group"] == g for r in rs)]
    doms = [(d, l, sum(1 for r in rs if r["scope"] == "domain" and d in r["domains"])) for d, l in VOCAB["domains"].items() if d != "research"]
    if any(n for _, _, n in doms):
        gen += ["", "Learnings that hold only in one domain: " + ", ".join(f"[{l}](domains/{d}.md) {n}" for d, l, n in doms if n) + "."]
    gen += ["", "Research runs, each recorded in full under [research/](research/):", ""]
    gen += [f"- [{t}](research/{name}/)" for name, t in runs()]
    gen += ["", END]
    readme = (ROOT / "README.md").read_text()
    if START in readme and END in readme:
        readme = readme[: readme.index(START)] + "\n".join(gen) + readme[readme.index(END) + len(END):]
    else:
        readme = readme.rstrip() + "\n\n" + "\n".join(gen) + "\n"
    pages["README.md"] = readme
    return pages


if __name__ == "__main__":
    pages = render()
    for g in VOCAB["groups"]:
        p = ROOT / "groups" / f"{g}.md"
        if f"groups/{g}.md" not in pages and p.exists():
            p.unlink()
    for d in VOCAB["domains"]:
        p = ROOT / "domains" / f"{d}.md"
        if f"domains/{d}.md" not in pages and p.exists():
            p.unlink()
    for rel, text in pages.items():
        (ROOT / rel).parent.mkdir(parents=True, exist_ok=True)
        (ROOT / rel).write_text(text)
    print(f"rendered {len(pages)} pages from {len(records())} records")
