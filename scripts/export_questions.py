"""Export an explicit public generation and transport snapshot.

Only the explicit source files below are eligible. Evaluator prompts, challenge
labels, reports, journals and prototype authoring notes cannot enter these exports.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import shutil

ROOT = Path(__file__).resolve().parents[1]
GENERATION_FILES = {
    "public/generation-standard.json": "public/generation-standard.json",
    "public/formats.json": "public/formats.json",
    "schema/generator-request.schema.json": "public/generator-request.schema.json",
    "schema/generator-response.schema.json": "public/generator-response.schema.json",
    "examples/generator-request.json": "public/examples/generator-request.json",
    "examples/generator-response.json": "public/examples/generator-response.json",
    "schema/lesson-context.schema.json": "contract/schema/lesson-context.schema.json",
    "schema/question-set.schema.json": "contract/schema/question-set.schema.json",
    "examples/othello-1-1/lesson-context.json": "contract/examples/othello-1-1/lesson-context.json",
    "examples/othello-1-1/question-set.json": "contract/examples/othello-1-1/question-set.json",
    "contract-manifest.json": "contract/manifest.json",
}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def encoded(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()


def record_snapshot() -> dict:
    records = sorted((ROOT / "learnings").glob("*.json"))
    hashes = {p.name: sha(p.read_bytes()) for p in records}
    return {"git_commit": subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip(),
            "dirty_worktree": bool(subprocess.check_output(["git", "-C", str(ROOT), "status", "--porcelain"], text=True).strip()),
            "record_count": len(records), "records_sha256": sha(encoded(hashes)),
            "qualification": "Knowledge records retain their own scope, status and counterevidence; inclusion is not universal academic approval."}


def payloads() -> dict[str, tuple[str, dict[str, bytes]]]:
    generation = {dest: (ROOT / source).read_bytes() for dest, source in GENERATION_FILES.items()}
    return {"generator": ("public-generation-only", generation)}


def export(destination: Path | None = None) -> dict:
    destination = ROOT / "exports" if destination is None else destination
    snapshot = record_snapshot()
    if destination.is_symlink():
        raise ValueError("export destination must not be a symlink")
    destination.mkdir(parents=True, exist_ok=True)
    result = {}
    for consumer, (boundary, files) in payloads().items():
        target = destination / consumer
        if target.is_symlink():
            raise ValueError("public bundle destination must not be a symlink")
        temp = Path(tempfile.mkdtemp(prefix=".export-", dir=destination))
        try:
            for name, raw in files.items():
                path = temp / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(raw)
            manifest = {"version": 1, "boundary": boundary, "knowledge_snapshot": snapshot,
                        "files": [{"path": name, "sha256": sha(raw)} for name, raw in sorted(files.items())]}
            (temp / "manifest.json").write_bytes(encoded(manifest))
            # Rebuild only these generated bundle directories. Other source and
            # research folders are never part of this writer's target.
            if target.exists():
                shutil.rmtree(target)
            temp.rename(target)
            manifest_path = target / "manifest.json"
            try:
                display_path = manifest_path.relative_to(ROOT)
            except ValueError:
                display_path = manifest_path.relative_to(destination)
            result[consumer] = {"manifest": str(display_path), "files": len(files), "boundary": boundary}
        finally:
            if temp.exists():
                shutil.rmtree(temp)
    return {"record_count": snapshot["record_count"], "exports": result}


if __name__ == "__main__":
    print(json.dumps(export(), indent=2))
