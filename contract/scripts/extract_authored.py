#!/usr/bin/env python3
"""Turn an authored lesson (the animated build's lesson JSON) into the pair's contract, word for word: the lesson's
public context (lesson-context.json) and every question in it as a reference output (question-set.json), each pointing
at where it sits in the lesson. Nothing a student reads or hears is changed: a listed person's name there stops the run.
A name in text only a marker reads (a rubric's requirement, its accepted answers) or in metadata (a draft's source note)
becomes [name], and every such pointer is listed in the source record.

Usage: extract_authored.py --lesson LESSON.json --mirror REPO_DIR --remote NAME --out examples/LESSON_ID"""
import argparse, copy, datetime, hashlib, json, subprocess, sys
from pathlib import Path

# names come from the learnings repository's local list; its scrub also shortens home paths
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from redact import scrub  # noqa: E402

VERSION = "extract-authored 0.1"
# keys whose strings a student reads or hears: a redaction there means the copy is no longer literal, so it stops
STUDENT = {"q", "stem", "options", "text", "why", "yes", "after", "feedback", "line", "lines", "task", "question",
           "nudge", "second_nudge", "third_nudge", "reveal", "reply",
           "meaning", "goal", "mission", "answer", "close", "candidates", "decoys", "strong", "quotes", "stems",
           "checklist", "help", "narration", "title", "label", "words", "w", "lead", "hint", "ask", "repeat", "note",
           "say", "think", "sentence", "parts", "t", "explain_ask", "explain_hint", "explain_reveal", "rebut_ask",
           "rebut_hint", "rebut_reveal", "verdict_task", "starter", "starters", "chips", "tasks", "kicker", "cta",
           "rules", "scene", "who", "means", "context", "context_lines", "term", "how", "check", "visual"}


def walk(x, path=()):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from walk(v, path + (k,))
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from walk(v, path + (i,))
    elif isinstance(x, str):
        yield path, x


def pointer(path):
    return "/" + "/".join(str(p).replace("~", "~0").replace("/", "~1") for p in path)


def set_at(x, path, v):
    for p in path[:-1]:
        x = x[p]
    x[path[-1]] = v


# text a marker reads but a student never sees
MARKER = {"requirement", "evidence", "accept", "looks_like", "keywords", "coach", "misreadings"}


def leaf_key(path):
    """The dict key a string sits under (for a list item, the list's key)."""
    return next((p for p in reversed(path) if isinstance(p, str)), None)


def redact(lesson):
    """Scrub every string; return the scrubbed copy and the pointers changed, each with who reads it. Stop if a string a
    student reads or hears would change."""
    out = copy.deepcopy(lesson)
    changed, student = [], []
    for path, s in walk(lesson):
        t = scrub(s)
        if t != s:
            set_at(out, path, t)
            k = leaf_key(path)
            changed.append({"pointer": pointer(path), "read_by": "marker" if k in MARKER else "student" if k in STUDENT else "metadata"})
            if k in STUDENT:
                student.append(pointer(path))
    if student:
        sys.exit("a student-facing string carries a listed name; resolve by hand before extracting:\n  " + "\n  ".join(student))
    return out, changed


def choice_view(stem, options, key, option_feedback=None, correct_feedback=None, **extra):
    v = {"stem": stem, "options": options, "key": key}
    if option_feedback is not None:
        v["option_feedback"] = option_feedback
    if correct_feedback is not None:
        v["correct_feedback"] = correct_feedback
    v.update({k: x for k, x in extra.items() if x is not None})
    return v


def items_of(lesson):
    """Every question-bearing part of the lesson, in the order a student meets it, with a normalised view beside it."""
    out = []

    def add(page, local, kind, path, view):
        node = lesson
        for p in path:
            node = node[p]
        out.append({"id": f"{page}/{local}", "page": page, "order": len(out) + 1, "kind": kind,
                    "pointer": pointer(path), "view": view, "native": node})

    for pi, page in enumerate(lesson["pages"]):
        pid, n = page["id"], page["nodes"][0]
        base = ("pages", pi, "nodes", 0)
        t = n.get("type")
        if t == "unit_film":
            for si, seg in enumerate(n.get("segments", [])):
                for mi, m in enumerate(seg.get("mcq", [])):
                    add(pid, f"segment-{si + 1}-check-{mi + 1}", "film_mcq", base + ("segments", si, "mcq", mi),
                        choice_view(m["stem"], m["options"], [m["answer"]], m.get("feedback"), None,
                                    shown_at_seconds=m.get("at"), spoken_check=seg.get("check"), segment=si + 1))
        elif t == "word_web":
            add(pid, "web", "word_web", base, {"prompt": [n.get("idea", {}).get("lead"), n.get("line")], "centre": n.get("centre"),
                                               "likely": n.get("likely"), "families": n.get("families"), "rubric": n.get("rubric")})
        elif t == "key_term":
            add(pid, "term", "key_term_mcq", base,
                choice_view(n["task"], [o["text"] for o in n["options"]], [n["correct"]], [o.get("why") for o in n["options"]],
                            n.get("yes"), term=n.get("term"), word_class=n.get("cls"), meaning=n.get("meaning"), after=n.get("after")))
        elif t == "reading":
            for mi, m in enumerate(n.get("mcqs", [])):
                add(pid, f"mcq-{mi + 1}", "reading_mcq", base + ("mcqs", mi),
                    choice_view(m["q"], [o["text"] for o in m["options"]], [m["correct"]], [o.get("why") for o in m["options"]], m.get("yes")))
            if n.get("rubric"):
                add(pid, "check", "open_check", base + ("rubric",), {"prompt": n.get("check"), "rubric": n["rubric"]})
        elif t == "dose":
            add(pid, "select", "evidence_select", base,
                {"prompt": n.get("goal"), "mission": n.get("mission"), "candidates": n.get("candidates"), "decoys": n.get("decoys"), "strong": n.get("strong")})
            add(pid, "explain", "open_prompt", base, {"prompt": n.get("explain_ask"), "hint": n.get("explain_hint"), "reveal": n.get("explain_reveal")})
            add(pid, "rebut", "open_prompt", base, {"prompt": n.get("rebut_ask"), "hint": n.get("rebut_hint"), "reveal": n.get("rebut_reveal")})
            if n.get("verdict"):
                add(pid, "verdict", "open_check", base + ("verdict",), {"prompt": n.get("close") or n.get("verdict_task"), "rubric": n["verdict"]})
        elif t == "model":
            slots = [e for e in n.get("rebuild", []) if "options" in e]
            sentence = "".join(e["text"] if "text" in e else "___" for e in n.get("rebuild", []))
            for si, e in enumerate(slots):
                idx = [i for i, x in enumerate(n["rebuild"]) if "options" in x][si]
                add(pid, f"rebuild-{si + 1}", "rebuild_choice", base + ("rebuild", idx),
                    choice_view(sentence, e["options"], [e["options"].index(e["correct"])], slot=si + 1, label=n.get("rebuild_label")))
        elif t == "independent":
            if n.get("rubric"):
                add(pid, "paragraph", "open_check", base + ("rubric",),
                    {"prompt": n.get("line"), "rubric": n["rubric"], "frame": {"quotes": n.get("quotes"), "stems": n.get("stems"), "checklist": n.get("checklist"), "locked": n.get("locked")}})
            for mk, mr in sorted((n.get("moves", {}).get("rubrics") or {}).items(), key=lambda kv: int(kv[0])):
                add(pid, f"move-{mk}", "open_check", base + ("moves", "rubrics", mk), {"prompt": (mr or {}).get("question"), "rubric": mr})
        elif t == "mimicry":
            add(pid, "say-back", "say_back", base, {"prompt": n.get("line"), "expected": n.get("repeat"), "definitions": n.get("definitions")})
        elif t == "apply":
            for ri, r in enumerate(n.get("rubrics", [])):
                add(pid, f"apply-{ri + 1}", "open_check", base + ("rubrics", ri),
                    {"prompt": r.get("question"), "rubric": r, "frame": {"stems": n.get("stems"), "how": n.get("how")}})
        elif t == "evaluate":
            add(pid, "evaluate", "open_check", base + ("rubric",), {"prompt": n.get("question"), "rubric": n["rubric"], "help": n.get("help")})
        elif t == "pin_words":
            add(pid, "pin", "classify", base,
                {"prompt": n.get("goal"), "items": [{"word": w["w"], "to": w["to"], "kind": w["kind"], "meaning": w.get("meaning")} for w in n.get("words", [])],
                 "boxes": n.get("boxes")})
            if n.get("verdict"):
                add(pid, "verdict", "open_check", base + ("verdict",), {"prompt": n["verdict"].get("question"), "rubric": n["verdict"]})
        elif t == "record":
            add(pid, "character-file", "open_check", base + ("rubric",), {"prompt": n["rubric"].get("question"), "rubric": n["rubric"], "choices": n.get("file_words")})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lesson", required=True)
    ap.add_argument("--mirror", required=True)
    ap.add_argument("--remote", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    lesson_path, mirror, out = Path(a.lesson).resolve(), Path(a.mirror).resolve(), Path(a.out)
    rel = str(lesson_path.relative_to(mirror))
    commit = subprocess.run(["git", "-C", str(mirror), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    if subprocess.run(["git", "-C", str(mirror), "diff", "--quiet", "HEAD", "--", rel]).returncode:
        sys.exit(f"{rel} has uncommitted changes in the mirror; extract only a committed lesson")
    raw = lesson_path.read_bytes()
    lesson, changed = redact(json.loads(raw))
    out.mkdir(parents=True, exist_ok=True)
    source = {"mirror": scrub(str(mirror)), "remote": a.remote, "commit": commit, "path": rel, "sha256": hashlib.sha256(raw).hexdigest(),
              "extracted": datetime.date.today().isoformat(), "by": VERSION, "redacted": changed}
    context = {"contract": "lesson-context 0.1", "source": source,
               "lesson": {"id": lesson.get("lessonId"), "title": lesson.get("title"), "subtitle": lesson.get("subtitle"),
                          "learning_question": lesson.get("question"), "keywords": lesson.get("keywords")},
               "native": lesson}
    items = items_of(lesson)
    qset = {"contract": "question-set 0.1", "source": source, "lesson": lesson.get("lessonId"),
            "made_by": {"kind": "authored", "note": "the authored lesson's own questions, copied word for word: the reference for what a generator returns"},
            "items": items}
    (out / "lesson-context.json").write_text(json.dumps(context, indent=1, ensure_ascii=False) + "\n")
    (out / "question-set.json").write_text(json.dumps(qset, indent=1, ensure_ascii=False) + "\n")
    kinds = {}
    for it in items:
        kinds[it["kind"]] = kinds.get(it["kind"], 0) + 1
    print(json.dumps({"items": len(items), "kinds": kinds, "redacted_pointers": len(changed), "commit": commit[:7]}))


if __name__ == "__main__":
    main()
