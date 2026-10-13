#!/usr/bin/env python3
"""One-off: turn the first format (README.md bullets plus EVIDENCE.md sections) into one record per learning in
learnings/. Kept to show how the first 55 records were made."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib import ROOT, by_prefix, SOURCES, anchor

# id: group, role, facets, stage, scope, domains, kind, status
M = {
  "feedback-that-sends-the-student-back": ("what-a-student-is-told", "criterion", ["feedback", "hints"], None, ["g9", "g3"], "adopted-rule", "held"),
  "one-plain-voice-for-every-line": ("what-a-student-is-told", "criterion", ["wording", "feedback"], None, ["g9"], "adopted-rule", "held"),
  "nothing-gives-the-answer-first": ("what-a-student-is-told", "criterion", ["integrity", "media"], None, ["g9", "research"], "adopted-rule", "held"),
  "two-tries-then-the-answer": ("what-a-student-is-told", "criterion", ["practice", "feedback"], None, ["g9"], "adopted-rule", "contested"),
  "a-question-must-need-the-text": ("writing-questions", "criterion", ["integrity", "stimulus"], None, ["g3", "g9"], "measured", "held"),
  "one-answer-the-text-settles": ("writing-questions", "criterion", ["key", "distractors"], None, ["g9"], "adopted-rule", "held"),
  "ask-where-the-answer-was-given": ("writing-questions", "criterion", ["alignment", "media"], None, ["g9"], "measured", "held"),
  "spread-the-right-answers-position": ("writing-questions", "criterion", ["key", "integrity"], None, ["g3", "g9"], "measured", "held"),
  "two-of-a-kind-must-differ": ("writing-questions", "criterion", ["alignment", "integrity"], None, ["g9"], "measured", "held"),
  "unsure-is-neither-yes-nor-no": ("checking-answers", "method", ["marking", "evaluation"], "judge", ["g9", "g3"], "adopted-rule", "held"),
  "mark-meaning-not-wording": ("checking-answers", "method", ["marking"], "judge", ["g9"], "adopted-rule", "held"),
  "keep-the-words-a-hint-not-a-grade": ("checking-answers", "method", ["marking", "feedback"], "judge", ["g9", "research"], "measured", "held"),
  "aimed-at-the-marker": ("checking-answers", "method", ["marking", "integrity"], "judge", ["g9", "g3"], "adopted-rule", "held"),
  "answers-nobody-planned-for": ("checking-answers", "method", ["marking", "key"], "judge", ["g9"], "adopted-rule", "held"),
  "save-the-first-attempt": ("checking-answers", "method", ["evidence-of-learning", "measurement"], "measure", ["g9"], "adopted-rule", "held"),
  "never-adapt-on-one-observation": ("checking-answers", "method", ["evidence-of-learning", "practice"], "measure", ["g3"], "adopted-rule", "held"),
  "words-not-line-numbers": ("the-text", "criterion", ["wording", "stimulus"], None, ["g9", "g3"], "adopted-rule", "held"),
  "exact-quotations": ("the-text", "criterion", ["stimulus", "integrity"], None, ["g9"], "adopted-rule", "held"),
  "words-that-carry-the-knowledge": ("the-text", "criterion", ["wording", "alignment"], None, ["g9"], "adopted-rule", "held"),
  "no-slurs-to-perform": ("the-text", "criterion", ["wording", "integrity"], None, ["g9"], "adopted-rule", "held"),
  "background-at-the-line-that-needs-it": ("the-text", "criterion", ["sequence", "stimulus"], None, ["g9", "research"], "measured", "held"),
  "pictures-that-show-what-is-said": ("pictures-sound-film", "criterion", ["media"], None, ["g9"], "measured", "held"),
  "check-what-a-picture-implies": ("pictures-sound-film", "method", ["media", "integrity"], "review", ["g9"], "measured", "held"),
  "split-dont-cut": ("pictures-sound-film", "method", ["media"], "write", ["g9", "research"], "measured", "held"),
  "measure-from-the-delivered-file": ("pictures-sound-film", "method", ["media", "measurement"], "settle", ["g9"], "adopted-rule", "held"),
  "keep-directions-apart-from-the-words": ("pictures-sound-film", "method", ["media", "generation"], "write", ["g9"], "measured", "held"),
  "few-words-on-screen": ("pictures-sound-film", "criterion", ["media", "wording"], None, ["g9", "research"], "external-research", "held"),
  "reduced-motion-and-colour": ("pictures-sound-film", "criterion", ["accessibility", "media"], None, ["g9"], "adopted-rule", "held"),
  "gate-every-check": ("pictures-sound-film", "criterion", ["practice", "integrity"], None, ["g9", "research"], "measured", "held"),
  "write-little-judge-the-rest": ("generating-with-a-model", "method", ["generation", "evaluation"], "write", ["g9"], "measured", "held"),
  "give-the-judge-what-the-student-sees": ("ai-judges-and-markers", "method", ["evaluation"], "judge", ["g3", "g9", "research"], "measured", "held"),
  "one-question-per-candidate": ("ai-judges-and-markers", "method", ["evaluation"], "judge", ["g3"], "measured", "held"),
  "a-judge-checks-it-doesnt-hunt": ("ai-judges-and-markers", "method", ["evaluation", "review"], "judge", ["g3"], "measured", "held"),
  "give-the-marker-what-the-rule-names": ("ai-judges-and-markers", "method", ["marking", "scoring-guide"], "judge", ["g9"], "measured", "held"),
  "verdicts-vary": ("ai-judges-and-markers", "method", ["evaluation", "measurement"], "measure", ["g9"], "measured", "held"),
  "agreement-is-not-correctness": ("ai-judges-and-markers", "method", ["evaluation", "measurement"], "measure", ["g3", "g9", "research"], "measured", "held"),
  "test-the-fallback": ("ai-judges-and-markers", "method", ["marking"], "review", ["g9"], "measured", "held"),
  "person-labelled-cases-first": ("ai-judges-and-markers", "method", ["evaluation", "measurement"], "measure", ["g9", "g3"], "adopted-rule", "held"),
  "a-check-must-catch-a-planted-fault": ("ai-judges-and-markers", "method", ["evaluation"], "measure", ["g3", "g9"], "measured", "held"),
  "keep-every-judgment-whole": ("ai-judges-and-markers", "method", ["evaluation"], "judge", ["g9", "g3"], "measured", "held"),
  "order-a-lesson": ("how-people-learn", "criterion", ["sequence"], None, ["g3", "research"], "external-research", "held"),
  "a-passed-gate-is-not-learning": ("how-people-learn", "context", ["evidence-of-learning", "measurement"], None, ["g3", "research"], "adopted-rule", "held"),
  "liking-is-not-learning": ("how-people-learn", "context", ["evidence-of-learning", "media"], None, ["research"], "external-research", "held"),
  "remake-under-new-rules": ("making-and-reviewing", "method", ["review"], "improve", ["g9"], "measured", "held"),
  "check-against-something-that-doesnt-assume-the-answer": ("making-and-reviewing", "method", ["evaluation", "review"], "review", ["g9"], "measured", "held"),
  "machine-checks-are-not-judgment": ("making-and-reviewing", "method", ["review"], "review", ["g9"], "adopted-rule", "held"),
  "fix-the-rubric-first": ("making-and-reviewing", "method", ["measurement", "scoring-guide"], "measure", ["g9"], "adopted-rule", "held"),
  "review-as-a-student": ("making-and-reviewing", "method", ["review"], "review", ["g9"], "measured", "held"),
  "scripted-readers-first": ("making-and-reviewing", "method", ["review"], "review", ["g9", "g3"], "adopted-rule", "held"),
  "report-accuracy-by-skill": ("making-and-reviewing", "method", ["measurement", "evidence-of-learning"], "measure", ["g3"], "measured", "held"),
  "record-where-every-asset-came-from": ("making-and-reviewing", "method", ["media", "integrity"], "settle", ["g9"], "adopted-rule", "held"),
  "stills-or-motion": ("not-settled", "context", ["media"], None, ["g9", "research"], "open-question", "open"),
  "captions-and-redundancy": ("not-settled", "context", ["media", "accessibility"], None, ["g9", "research"], "open-question", "open"),
  "who-reads-what-students-write": ("not-settled", "context", ["marking", "evidence-of-learning"], None, ["g9"], "open-question", "open"),
  "nudging-a-stalled-reader": ("not-settled", "context", ["practice"], None, ["g9"], "open-question", "open"),
}
SEED = {"unsure-is-neither-yes-nor-no", "one-answer-the-text-settles", "feedback-that-sends-the-student-back", "keep-the-words-a-hint-not-a-grade",
        "aimed-at-the-marker", "answers-nobody-planned-for", "two-tries-then-the-answer", "words-not-line-numbers", "exact-quotations",
        "background-at-the-line-that-needs-it", "pictures-that-show-what-is-said", "gate-every-check",
        "check-against-something-that-doesnt-assume-the-answer", "scripted-readers-first"}
FIX_REF = {"https://ai.google.dev/gemini-api/docs/speech-generation": "the voice model's documentation",
           "https://www.aft.org/sites/default/files/periodicals/Rosenshine.pdf": "Rosenshine 2012"}


def split_statement(b):
    m = re.match(r"(.+?[.?])\s+(\S.*)$", b)
    if m:
        return m.group(1), m.group(2)
    m = re.match(r"(.+?):\s+(.*\d.*)$", b)
    if m:
        rest = m.group(2)
        return m.group(1) + ".", rest[0].upper() + rest[1:]
    return b, ""


readme = (ROOT / "README.md").read_text()
bullets = {}
for b in re.findall(r"^- .*(?:\n  .*)*", readme, flags=re.M):
    text = re.sub(r"\s+", " ", b[2:])
    a = re.search(r"\[record\]\(EVIDENCE\.md#([^)]+)\)", text)
    if a:
        bullets[a.group(1)] = re.sub(r"\s*\[record\]\([^)]*\)", "", text).strip()

ev = (ROOT / "EVIDENCE.md").read_text()
parts = re.split(r"^### (.+)$", ev, flags=re.M)
made = 0
for title, body in zip(parts[1::2], parts[2::2]):
    body = re.split(r"^## ", body, flags=re.M)[0].strip()
    rid = anchor(title)
    g, role, facets, stage, doms, kind, status = M[rid]
    m = re.search(r"\bAgainst(?:,[^:]*)?:\s*", body)
    detail, against = (body[: m.start()].strip(), body[m.end():].strip()) if m else (body, "none found")
    flat = re.sub(r"\s+", " ", body)
    cites, seen = [], set()
    for ref, url in re.findall(r"\(([^()]*?),\s*(https?://[^\s)]+)\)", flat):
        cites.append({"ref": ref.strip(), "url": url}); seen.add(url)
    for url in re.findall(r"(https?://[^\s)]+)", flat):
        if url not in seen and "github.com/StanHus" not in url:
            cites.append({"ref": FIX_REF.get(url, url), "url": url}); seen.add(url)
    evidence, got = [], set()
    for c in re.findall(r"`([^`\n]+)`", body):
        k = by_prefix(c)
        if k and c != SOURCES[k]["prefix"]:
            rel = c[len(SOURCES[k]["prefix"]) + 1:]
            if (k, rel) not in got:
                got.add((k, rel)); evidence.append({"source": k, "path": rel})
    statement, example = split_statement(bullets[rid])
    rec = {"id": rid, "title": title, "statement": statement, **({"example": example} if example else {}),
           "group": g, "role": role, "facets": facets, "stage": stage, "scope": "universal", "domains": doms,
           "kind": kind, "status": status, "detail": detail, "against": against, "evidence": evidence, "citations": cites,
           "found_in": ["2026-10-12-seed"] if rid in SEED else ["2026-10-12-round-1"], "added": "2026-10-12"}
    (ROOT / "learnings" / f"{rid}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n")
    made += 1
print("records written:", made)
