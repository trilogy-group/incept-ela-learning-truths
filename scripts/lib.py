"""Shared loading for build.py and check.py: the vocabulary, the source register and the records."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = str(Path.home())
HOME_KEY = HOME.replace("/", "-")   # the home folder as the name of an agent's project folder spells it
VOCAB = json.loads((ROOT / "schema" / "vocabulary.json").read_text())
SOURCES = json.loads((ROOT / "sources" / "sources.json").read_text())


def anchor(text):
    """GitHub's anchor for a heading: lower case, punctuation dropped, spaces to hyphens."""
    return re.sub(r"[^\w\- ]", "", text.strip().lower()).replace(" ", "-")


def records():
    return [json.loads(p.read_text()) for p in sorted((ROOT / "learnings").glob("*.json"))]


def expand(p):
    """A recorded path on this machine: ~ is the home folder, {home} the home folder spelt as a project folder's name."""
    p = str(p).replace("{home}", HOME_KEY)
    return HOME + p[1:] if p.startswith("~") else p


def shorten(p):
    """The recorded form of a path: no account name in it."""
    return str(p).replace(HOME, "~").replace(HOME_KEY, "{home}")


def source_root(key):
    root = Path(expand(SOURCES[key]["root"]))
    return root if root.is_absolute() else ROOT / root


def cite_paths(text):
    """Write each home path in a record's text as its source's prefix and the path within it, the form the check reads."""
    roots = sorted(((k, shorten(source_root(k))) for k in SOURCES), key=lambda x: -len(x[1]))
    for k, r in roots:
        if " " in r:   # a root with spaces in it can't be found as one word: replace it whole
            text = text.replace(r + "/", SOURCES[k]["prefix"] + "/")

    def one(m):
        full = str(Path(expand(m.group(0))))
        for k, r in roots:
            r = expand(r)
            if full == r or full.startswith(r + "/"):
                return SOURCES[k]["prefix"] + full[len(r):]
        return m.group(0)
    text = re.sub(r"~/[^\s`'\"(),;]+", one, text)

    def rehome(m):
        k = by_prefix(m.group(1))
        if not k:
            return m.group(0)
        full = str(source_root(k)) + m.group(1)[len(SOURCES[k]["prefix"]):]
        for k2, r in roots:
            r = expand(r)
            if (full == r or full.startswith(r + "/")) and k2 != k:
                return "`" + SOURCES[k2]["prefix"] + full[len(r):] + "`"
            if full == r or full.startswith(r + "/"):
                break
        return m.group(0)
    return re.sub(r"`([^`\n]+)`", rehome, text)


def by_prefix(cited):
    """The source a prose citation (`prefix/path`) belongs to: the longest registered prefix that covers it."""
    hits = [k for k, s in SOURCES.items() if cited == s["prefix"] or cited.startswith(s["prefix"] + "/")]
    return max(hits, key=lambda k: len(SOURCES[k]["prefix"]), default=None)
