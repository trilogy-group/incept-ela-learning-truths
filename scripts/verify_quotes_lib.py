"""The quote check shared by verify_quotes.py and add_records.py: a quote is found when every part of it (split at
ellipses) appears in the file after whitespace, quote-mark and markdown-emphasis normalisation. A quote can also sit in
a commit's message, or in a file as it was at a revision (git_quote_found)."""
import re, subprocess
from pathlib import Path


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
    s = re.sub(r"\*\*|__|`|\\", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()


# a file inside an archive, as readers cite it: "a.zip!/x", "a.tar.gz::x" or "a.tar.gz:x"
ARCHIVE = re.compile(r"^(?P<arc>.+?\.(?:zip|tar\.gz|tgz|tar))(?:!/|::|:)(?P<member>.+)$")
CODE = (".js", ".mjs", ".cjs", ".ts", ".py", ".sh", ".css")


def split_archive(path):
    """(archive, member) for a path into an archive, else (path, None)."""
    m = ARCHIVE.match(str(path))
    return (m.group("arc"), m.group("member")) if m else (str(path), None)


def member_text(arc, member):
    """A member of a zip or tar archive, read into memory (nothing is extracted to disk); None if it isn't there."""
    import tarfile, zipfile
    try:
        if str(arc).endswith(".zip"):
            with zipfile.ZipFile(arc) as z:
                data = z.read(member)
        else:
            with tarfile.open(arc) as t:
                names = set(t.getnames())
                name = member if member in names else "./" + member if "./" + member in names else None
                f = t.extractfile(name) if name else None
                data = f.read() if f else None
    except (KeyError, OSError, tarfile.TarError, zipfile.BadZipFile):
        return None
    return None if data is None else data.decode("utf-8", errors="replace")


def uncomment(text):
    """Code with each line's comment marker taken off, so a quote of a comment that runs over lines can be found."""
    return re.sub(r"(?m)^[ \t]*(?://+|#+|/?\*+/?)[ \t]?", "", text)


def text_of(p):
    arc, member = split_archive(p)
    if member:
        t = member_text(arc, member) or ""
        return uncomment(t) + "\n" + t if member.lower().endswith(CODE) else t
    suf = p.suffix.lower()
    if suf in CODE:
        t = p.read_text(errors="replace")
        return uncomment(t) + "\n" + t
    if suf in (".docx", ".html", ".htm", ".rtf"):
        return subprocess.run(["textutil", "-convert", "txt", "-stdout", str(p)], capture_output=True, text=True).stdout
    if suf == ".pdf":
        return subprocess.run(["pdftotext", str(p), "-"], capture_output=True, text=True).stdout
    if suf == ".xlsx":
        return subprocess.run(["unzip", "-p", str(p), "xl/sharedStrings.xml"], capture_output=True, text=True).stdout
    return p.read_text(errors="replace")


_cache = {}


def quote_found(path, quote):
    p = Path(path)
    arc, member = split_archive(p)
    if not (Path(arc).is_file() if member else p.exists() and not p.is_dir()):
        return False
    if p not in _cache:
        try:
            _cache[p] = norm(text_of(p))
        except Exception:
            _cache[p] = ""
    return in_text(_cache[p], quote)


def in_text(normed, quote):
    q = quote.strip().strip('"').strip("“”")
    parts = [x for x in re.split(r"\s*(?:…|\.\.\.)\s*", q) if len(x.strip()) >= 6]
    return bool(parts) and all(norm(x) in normed for x in parts)


def git_target(target, field, rev):
    """The repository and the git object a commit or revision citation names: (repo, spec), or (None, None)."""
    target = Path(target)
    if field == "commit":
        return target, f"{rev}^{{commit}}"
    top = subprocess.run(["git", "-C", str(target.parent), "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    if not top:
        return None, None
    return Path(top), f"{rev}:{target.resolve().relative_to(Path(top).resolve())}"


def git_quote_found(target, field, rev, quote):
    """field "commit": the quote is in that commit's message (target is the repository); field "at": it is in the file
    target as it was at revision rev."""
    repo, spec = git_target(target, field, rev)
    if not repo:
        return False
    cmd = ["log", "-1", "--format=%B", rev] if field == "commit" else ["show", spec]
    r = subprocess.run(["git", "-C", str(repo), *cmd], capture_output=True, text=True)
    return r.returncode == 0 and in_text(norm(r.stdout), quote)
