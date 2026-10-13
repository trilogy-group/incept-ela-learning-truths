"""Redaction for anything recorded as research: people's names from the untracked .local/terms.txt become [name], and
home paths are shortened to ~ (and the home folder spelt as a project folder's name to {home})."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = str(Path.home())
HOME_KEY = HOME.replace("/", "-")
# job roles that point at a person; none may appear in the pages
ROLE_PHRASES = ["curriculum owner", "project owner", "teammate", "team lead", "learning-science lead"]


def names():
    f = ROOT / ".local" / "terms.txt"
    if not f.exists():
        return []
    return [t.strip() for t in f.read_text().splitlines() if t.strip() and not t.startswith("#") and not t.startswith("warn: ")]


def scrub(s):
    s = s.replace(HOME, "~").replace(("/" + "Users" + "/" + "stanhus"), "~").replace(HOME_KEY, "{home}").replace(("-" + "Users" + "-" + "stanhus"), "{home}")
    for n in names():
        flags = re.I if n.islower() else 0
        s = re.sub(rf"(?<![A-Za-z]){re.escape(n)}(?![a-z])", "[name]", s, flags=flags)
        s = re.sub(rf"(?<![A-Za-z]){re.escape(n.lower())}(?![a-z])", "[name]", s)
        s = re.sub(rf"(?<![A-Za-z]){re.escape(n.upper())}(?![A-Za-z])", "[name]", s)   # a name in capitals, as in a file name
    return s
