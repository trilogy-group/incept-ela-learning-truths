#!/usr/bin/env python3
"""Check the contract before a commit: every example's items resolve to their place in the lesson context, every string
a student reads is word for word the authored lesson at its pinned commit, the kinds are known, and no tracked file
carries a listed person's name or a home path. Exits non-zero on any error."""
import argparse, hashlib, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "scripts"))
from redact import names  # noqa: E402
sys.path.insert(0, str(ROOT / "scripts"))
from extract_authored import STUDENT, walk, leaf_key, items_of  # noqa: E402

KINDS = {"film_mcq", "reading_mcq", "key_term_mcq", "rebuild_choice", "open_check", "open_prompt", "word_web",
         "evidence_select", "say_back", "classify"}
HOME = str(Path.home())
errors = []
proofs = []


def at(doc, ptr):
    x = doc
    for p in ptr.strip("/").split("/"):
        p = p.replace("~1", "/").replace("~0", "~")
        x = x[int(p)] if isinstance(x, list) else x[p]
    return x


def check_example(d, source_root=None):
    ctx = json.loads((d / "lesson-context.json").read_text())
    qs = json.loads((d / "question-set.json").read_text())
    src = ctx["source"]
    if qs["source"] != src:
        errors.append(f"{d.name}: question set and context name different sources")
    mirror = Path(source_root) if source_root else Path(src["mirror"].replace("~", HOME, 1))
    original = None
    if mirror.exists():
        r = subprocess.run(["git", "-C", str(mirror), "show", f"{src['commit']}:{src['path']}"], capture_output=True)
        original = json.loads(r.stdout) if r.returncode == 0 else None
        if original is None:
            errors.append(f"{d.name}: {src['path']} is not at {src['commit'][:7]} in the mirror")
        elif hashlib.sha256(r.stdout).hexdigest() != src["sha256"]:
            errors.append(f"{d.name}: pinned source bytes do not match its recorded hash")
    proofs.append({"example": d.name, "source_commit": src["commit"],
                   "external_git_comparison": "verified" if original is not None else "unavailable",
                   "snapshot_integrity": "checked against committed fixture manifest"})
    if qs["items"] != items_of(ctx["native"]):
        errors.append(f"{d.name}: item views/order differ from the contract extractor")
    if original is not None:
        for path, text in walk(ctx["native"]):
            if leaf_key(path) in STUDENT:
                value = original
                for part in path:
                    value = value[part]
                if value != text:
                    errors.append(f"{d.name}: learner-facing context text at {'/'.join(map(str, path))} differs from its source")
    seen = set()
    for it in qs["items"]:
        if it["kind"] not in KINDS:
            errors.append(f"{it['id']}: unknown kind {it['kind']}")
        if it["id"] in seen:
            errors.append(f"{it['id']}: duplicate id")
        seen.add(it["id"])
        try:
            here = at(ctx["native"], it["pointer"])
        except (KeyError, IndexError, ValueError):
            errors.append(f"{it['id']}: pointer {it['pointer']} does not resolve in the lesson context"); continue
        if here != it["native"]:
            errors.append(f"{it['id']}: its native copy differs from the lesson context at {it['pointer']}")
        if original is not None:
            orig = at(original, it["pointer"])
            for path, s in walk(it["native"]):
                if leaf_key(path) in STUDENT:
                    o = orig
                    for p in path:
                        o = o[p]
                    if o != s:
                        errors.append(f"{it['id']}: student-facing text at {it['pointer']}/{'/'.join(map(str, path))} is not the authored text")
    return len(qs["items"])


def check_manifest():
    manifest = json.loads((ROOT / "manifest.json").read_text())
    actual = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for folder in ("examples", "schema") for p in (ROOT / folder).rglob("*.json")}
    if manifest.get("version") != 1 or manifest.get("files") != actual:
        errors.append("reference/schema files differ from their committed snapshot manifest")
    for example, expected in manifest.get("source_provenance", {}).items():
        context = json.loads((ROOT / "examples" / example / "lesson-context.json").read_text())
        if context.get("source") != expected:
            errors.append(f"{example}: source provenance differs from the snapshot manifest")


def scan_names():
    ns = names()
    for f in ROOT.rglob("*"):
        rel = str(f.relative_to(ROOT))
        if not f.is_file() or f.suffix not in (".md", ".json", ".py", ".js", ".mjs"):
            continue
        t = f.read_text(errors="replace")
        if HOME in t or HOME.replace("/", "-") in t:
            errors.append(f"{rel}: a home path")
        for n in ns:
            flags = re.I if n.islower() else 0
            if re.search(rf"(?<![A-Za-z]){re.escape(n)}(?![A-Za-z])", t, flags) or re.search(rf"(?<![A-Za-z]){re.escape(n.upper())}(?![A-Za-z])", t):
                errors.append(f"{rel}: a listed name"); break


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", help="optional local Git clone containing the pinned authored lesson")
    args = parser.parse_args()
    check_manifest()
    total = 0
    for d in sorted(p for p in (ROOT / "examples").iterdir() if p.is_dir()):
        total += check_example(d, args.source_root)
    scan_names()
    for e in errors:
        print("error:", e)
    print(f"{total} items checked, {len(errors)} errors")
    print(json.dumps({"source_proof": proofs}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
