#!/usr/bin/env python3
"""Build and check the knowledge library and contract, then export public generation inputs."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import secrets
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
from export_questions import export


def local_path(name):
    path = Path(name)
    if path.is_absolute() or ".." in path.parts or not path.parts or path.parts[0] != ".local":
        raise ValueError("run outputs must be inside .local")
    cursor = ROOT
    for part in path.parts:
        cursor /= part
        if cursor.is_symlink():
            raise ValueError("run output paths must not use symlinks")
    return cursor


def save(path, value):
    with path.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    os.chmod(path, 0o600)


def execute():
    os.umask(0o077)
    config = json.loads((ROOT / "config.json").read_text())
    if set(config) != {"version", "execution", "run_root", "current_status"} or config["version"] != 1 or config["execution"] != "offline-only":
        raise ValueError("unsupported knowledge configuration")
    parent = local_path(config["run_root"])
    parent.mkdir(parents=True, exist_ok=True)
    directory = parent / ("run-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-") + secrets.token_hex(4))
    directory.mkdir(mode=0o700)
    status = {"state": "running", "run": str(directory.relative_to(ROOT)), "model_calls": 0, "checks": {}}
    steps = {"build": "scripts/build.py", "library": "scripts/check.py", "contract": "contract/scripts/check.py"}
    try:
        for name, script in steps.items():
            result = subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT, capture_output=True, text=True)
            (directory / (name + ".log")).write_text(result.stdout + result.stderr)
            status["checks"][name] = {"command": "python3 " + script, "exit_code": result.returncode}
            if result.returncode:
                raise ValueError(name + " failed; inspect its saved log")
        bundle = export()
        status.update({"state": "passed-package-checks", "record_count": bundle["record_count"], "exports": bundle["exports"],
                       "meaning": "Library consistency, committed reference integrity and reported source comparison; no evaluator qualification or learner-quality claim."})
    except (OSError, ValueError, KeyError) as error:
        status.update({"state": "failed", "error": str(error)})
    save(directory / "run.json", status)
    current = local_path(config["current_status"])
    current.parent.mkdir(parents=True, exist_ok=True)
    temporary = current.with_name(".current-" + secrets.token_hex(4) + ".json")
    save(temporary, status)
    os.replace(temporary, current)
    print(json.dumps(status, indent=2))
    return 0 if status["state"] == "passed-package-checks" else 1


if __name__ == "__main__":
    raise SystemExit(execute())
