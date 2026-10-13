"""Verify literal document/code citations at declared snapshots; no evaluation."""
import hashlib
from pathlib import Path
import re
import subprocess


def verify_evidence(citation, roots):
    alias, name, revision = citation.get('source'), citation.get('path', ''), citation.get('revision', '')
    if alias not in roots or not isinstance(name, str):
        return 'unregistered source'
    relative = Path(name)
    if relative.is_absolute() or '..' in relative.parts or any(p.lower() in {'personal', '.env', 'credentials'} for p in relative.parts):
        return 'source path is not an allowed relative document path'
    if relative.suffix.lower() in {'.csv', '.xlsx', '.parquet', '.pt', '.bin', '.pem', '.key'}:
        return 'source is not an allowed document or code artifact'
    root = Path(roots[alias]).expanduser().resolve()
    source = (root / relative).resolve()
    if not source.is_relative_to(root):
        return 'source path escapes its registered root'
    try:
        if revision.startswith('sha256:'):
            raw = source.read_bytes()
            if hashlib.sha256(raw).hexdigest() != revision[7:]:
                return 'source snapshot hash changed'
        else:
            pin = re.sub(r'^(git:|commit:)', '', revision)
            if not re.fullmatch(r'[0-9a-f]{7,40}', pin):
                return 'citation needs a Git revision or snapshot hash'
            raw = subprocess.check_output(['git', '-C', str(root), 'show', f'{pin}:{name}'], stderr=subprocess.DEVNULL)
        lines = raw.decode('utf-8').splitlines()
    except (OSError, UnicodeError, subprocess.CalledProcessError):
        return 'pinned source cannot be read'
    span = str(citation.get('lines', '')).replace('L', '')
    match = re.fullmatch(r'(\d+)(?:-(\d+))?', span)
    if not match:
        return 'invalid citation line span'
    lo, hi = int(match[1]), int(match[2] or match[1])
    if not 1 <= lo <= hi <= len(lines):
        return 'citation span lies outside the source'
    normalize = lambda s: ' '.join(s.split())
    quote = citation.get('quote', '')
    if not quote or normalize(quote) not in normalize('\n'.join(lines[lo - 1:hi])):
        return 'literal citation does not occur in the specified source lines'
    return None
