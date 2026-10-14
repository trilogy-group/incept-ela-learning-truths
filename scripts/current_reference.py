#!/usr/bin/env python3
"""Refresh the current hosted authored reference into the private example cache.

Reads GitHub and hosted static files. No source checkout, model, learner data,
judge request or deployment is used. Older source pins remain in sources.json.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import urljoin, urlsplit
from urllib.request import urlopen

import question_examples as examples
from example_adapters import _LiteralReader, StaticLiteralError

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "trilogy-group/ela-lessons"
HOST = "https://main.d2ugg6yjeo6j4t.amplifyapp.com/"
ENTRY_POINTS = [HOST, HOST + "e1#/intro"]
LESSON_PATH = "src/content/othello-1-1.json"
SOURCE_ID = "animated-current-main"


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(examples.encoded(value))


def github(endpoint, raw=False):
    command = ["gh", "api", "repos/" + REPOSITORY + "/" + endpoint]
    if raw:
        command += ["-H", "Accept: application/vnd.github.raw+json"]
    return subprocess.run(command, check=True, capture_output=True).stdout


class BundleLiteralReader(_LiteralReader):
    """Decode two literal minifier forms; never execute a JavaScript expression."""

    def value(self):
        self.space()
        for token, value in (("!0", True), ("!1", False)):
            if self.text.startswith(token, self.pos):
                self.pos += len(token)
                return value
        value = super().value()
        if isinstance(value, str) and self.text.startswith(".split(", self.pos):
            self.pos += len(".split(")
            self.space()
            if self.text[self.pos] not in "\"'`":
                raise StaticLiteralError("nonliteral_split_delimiter")
            delimiter = self.string()
            self.space()
            if self.text[self.pos] != ")" or not delimiter:
                raise StaticLiteralError("unsupported_split")
            self.pos += 1
            return value.split(delimiter)
        return value


def embedded_lesson(raw):
    text = raw.decode()
    matches = list(re.finditer(r"var ([\w$]+)=\{lessonId:", text))
    if len(matches) != 1:
        raise ValueError("hosted lesson literal is not unique")
    match = matches[0]
    start = text.index("{", match.start())
    reader = BundleLiteralReader(text, start)
    document = reader.value()
    return document, {"variable": match[1], "character_start": start,
                      "character_end": reader.pos,
                      "raw_literal_sha256": sha256(text[start:reader.pos].encode()),
                      "method": "Static literal parse, including minified booleans and literal string split; arbitrary calls and references rejected."}


def fetch(url, output):
    with urlopen(url, timeout=90) as response:
        raw = response.read()
        result = {"url": url, "final_url": response.url, "status": response.status,
                  "content_type": response.headers.get("Content-Type"),
                  "last_modified": response.headers.get("Last-Modified"),
                  "etag": response.headers.get("ETag"), "bytes": len(raw),
                  "sha256": sha256(raw)}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(raw)
    return raw, result


def asset_references(document):
    result = []

    def visit(value, path=()):
        if isinstance(value, dict):
            for key, child in value.items():
                visit(child, path + (key,))
        elif isinstance(value, list):
            for index, child in enumerate(value):
                visit(child, path + (index,))
        elif isinstance(value, str) and re.fullmatch(r"[^\s]*\.(?:jpg|png|webp|svg|mp3|mp4|vtt|glb)(?:\?[^\s]*)?", value):
            result.append({"pointer": examples.pointer(path), "value": value,
                           "url": urljoin(HOST, value)})

    visit(document)
    return result


def write_baseline(output, document, current, directory="positive-reference"):
    """Keep an exact native current-only projection beside the complete source."""
    items, omissions = examples.extract(document, "animated")
    destination = output / directory
    destination.mkdir(exist_ok=True)
    context = "hosted/root-lesson.json" if directory == "hosted-positive-reference" else "repo/" + LESSON_PATH
    rows = [{**item, "extraction_order": order, "source_id": current["id"],
             "source_commit": current["commit"], "source_sha256": current["sha256"],
             "lesson_context": context,
             "baseline_designation": current["baseline"]["designation"],
             "quality_label": None, "intended_answer_status": "author material; not independently validated"}
            for order, item in enumerate(items, 1)]
    (destination / "questions.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    manifest = {"source": current, "questions": directory + "/questions.jsonl",
                "questions_sha256": sha256((destination / "questions.jsonl").read_bytes()),
                "lesson_context": context, "source_occurrences": len(rows),
                "native_wording_keys_and_field_order": "unaltered private source projection",
                "omissions": omissions, "independent_quality_labels": 0}
    write_json(destination / "manifest.json", manifest)
    return manifest


def refresh(output):
    output = output.resolve()
    if not output.is_relative_to(ROOT / ".local") or output.exists():
        raise ValueError("use a new private directory inside .local for each refresh")
    output.mkdir(parents=True, mode=0o700)
    timestamp = datetime.now(timezone.utc).isoformat()
    branch_raw = github("branches/main")
    branch = json.loads(branch_raw)
    pin = branch["commit"]["sha"]
    if not re.fullmatch(r"[0-9a-f]{40}", pin):
        raise ValueError("main needs an exact commit")
    (output / "branch.json").write_bytes(branch_raw)
    tree_raw = github("git/trees/" + pin + "?recursive=1")
    tree = json.loads(tree_raw)
    if tree.get("truncated"):
        raise ValueError("source tree is truncated")
    (output / "tree.json").write_bytes(tree_raw)
    raw_files, files = {}, []
    for path in (LESSON_PATH, "amplify.yml", "media.json", "src/lib/session.tsx", "src/renderer/LessonRenderer.tsx"):
        raw = github("contents/" + path + "?ref=" + pin, raw=True)
        member = output / "repo" / path
        member.parent.mkdir(parents=True, exist_ok=True)
        member.write_bytes(raw)
        entry = next(item for item in tree["tree"] if item["path"] == path)
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        if blob != entry["sha"]:
            raise ValueError("GitHub bytes do not match tree blob: " + path)
        raw_files[path] = raw
        files.append({"path": path, "bytes": len(raw), "sha256": sha256(raw), "git_blob_sha1": blob})
    if "d2ugg6yjeo6j4t" not in raw_files["amplify.yml"].decode():
        raise ValueError("source deployment does not identify the hosted app")
    document = json.loads(raw_files[LESSON_PATH])
    hosted, hosted_documents = [], []
    for index, url in enumerate(ENTRY_POINTS):
        raw, receipt = fetch(url, output / "hosted" / ("root.html" if index == 0 else "e1.html"))
        embedded, extraction = embedded_lesson(raw)
        hosted_documents.append(embedded)
        write_json(output / "hosted" / ("root-lesson.json" if index == 0 else "e1-lesson.json"), embedded)
        hosted.append({**receipt, "lesson_semantic_equal_to_main": embedded == document, "extraction": extraction})
    if any(embedded != hosted_documents[0] for embedded in hosted_documents):
        raise ValueError("hosted entry points contain different lesson contexts; raw captures retained for separate review")
    hosted_match = all(item["lesson_semantic_equal_to_main"] for item in hosted)
    references = asset_references(document)
    if not hosted_match:
        references += [{**item, "variant": "currently-hosted"} for item in asset_references(hosted_documents[0])]
    manifest = json.loads(raw_files["media.json"])
    urls = {item["url"] for item in references}
    urls.update(urljoin(HOST, item["path"]) for item in manifest)
    urls.update(urljoin(HOST, item["path"].removeprefix("public/")) for item in tree["tree"]
                if item["type"] == "blob" and item["path"].startswith("public/") and item["path"].endswith((".json", ".vtt")))
    expected = {urljoin(HOST, item["path"]): item for item in manifest}

    def capture_asset(url):
        name = sha256(url.encode())
        try:
            raw, receipt = fetch(url, output / "assets" / name)
            if "text/html" in (receipt["content_type"] or ""):
                raise ValueError("asset URL returned the SPA document")
            path = "public/" + urlsplit(url).path.lstrip("/")
            source = next((item for item in tree["tree"] if item["path"] == path and item["type"] == "blob"), None)
            if source:
                blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
                receipt.update({"source_path": path, "source_git_blob_sha1": source["sha"], "git_blob_equal_to_main": blob == source["sha"]})
            if url in expected:
                receipt["manifest_sha256"] = expected[url]["sha256"]
                receipt["manifest_equal"] = receipt["sha256"] == expected[url]["sha256"] and receipt["bytes"] == expected[url]["bytes"]
            return {**receipt, "cache": "assets/" + name}
        except Exception as error:
            return {"url": url, "error_type": type(error).__name__, "error": str(error)}

    with ThreadPoolExecutor(max_workers=4) as pool:
        assets = list(pool.map(capture_asset, sorted(urls)))
    write_json(output / "asset-references.json", references)
    write_json(output / "assets.json", assets)
    clean, redactions = examples.sanitize(document)
    items, omissions = examples.extract(clean, "animated")
    routes = [{"source_order": index + 1, "page_id": page["id"], "native_pointer": examples.pointer(("pages", index)),
               "classic_url": HOST + "#/" + page["id"], "e1_url": HOST + "e1#/" + page["id"],
               "extra": page.get("extra"), "chrome": page.get("chrome"),
               "gate": [node.get("gate") for node in page["nodes"]]} for index, page in enumerate(document["pages"])]
    write_json(output / "routes.json", {"routes": routes, "native_order_retained": True,
               "layout_source": "src/lib/session.tsx", "layout_context": "Classic and E1 share authored JSON; pathname chooses layout and separate progress keys. Optional extras and learner gates affect exposure.",
               "rendered_and_timed_exposure": "not tested; source context and hosted embedded data verified"})
    current = {"id": SOURCE_ID, "repository": REPOSITORY, "visibility": "private source repository",
               "cache_repository": "animated", "commit": pin, "path": LESSON_PATH,
               "sha256": sha256(raw_files[LESSON_PATH]), "as_of": timestamp[:10], "adapter": "animated",
               "version_role": "current-hosted-main-at-refresh" if hosted_match else "current-source-main-at-refresh",
               "authorship": "current authored teaching reference; intended answers and draft rubrics remain source material",
               "baseline": {"designation": "user-designated default golden positive baseline", "scope": "this current authored source only",
                            "independent_quality_label": False, "qualification": "not established"},
               "hosted": {"entry_points": ENTRY_POINTS, "bundle_sha256": [item["sha256"] for item in hosted],
                          "lesson_semantic_equal_to_main": hosted_match, "checked_at": timestamp},
               "refresh_command": "python3 scripts/current_reference.py --refresh"}
    write_json(output / "capture.json", {"captured_at": timestamp, "commit": pin,
               "files": files, "hosted": hosted, "current_source": current,
               "asset_errors": [asset for asset in assets if "error" in asset]})
    baseline = write_baseline(output, document, current)
    previous_config = examples.SOURCE_CONFIG.read_bytes()
    (output / "previous-source-config.json").write_bytes(previous_config)
    if examples.DESTINATION.exists():
        shutil.copytree(examples.DESTINATION, output / "previous-question-examples")
        previous_catalog = (output / "previous-question-examples" / "catalog.json").read_bytes()
        write_json(output / "previous-snapshot.json", {
            "catalog_sha256": sha256(previous_catalog), "source_config_sha256": sha256(previous_config),
            "config_matches_previous_catalog": json.loads(previous_catalog)["source_config_sha256"] == sha256(previous_config)})
    config = json.loads(examples.SOURCE_CONFIG.read_text())
    hosted_source = None
    if not hosted_match:
        for candidate in reversed(config["sources"]):
            if candidate["adapter"] != "animated":
                continue
            candidate_path = ROOT / ".local" / "example-sources" / candidate["cache_repository"] / (candidate["commit"] or "archive") / candidate["path"]
            if candidate_path.exists() and examples.source_document(candidate, candidate_path.read_bytes()) == hosted_documents[0]:
                hosted_source = {**candidate, "id": "animated-current-hosted", "as_of": timestamp[:10],
                                 "version_role": "current-hosted-at-refresh",
                                 "baseline": {**current["baseline"], "scope": "this currently hosted teaching reference only"},
                                 "hosted": {**current["hosted"], "lesson_semantic_equal_to_main": False,
                                            "lesson_semantic_equal_to_source_pin": True,
                                            "source_pin_meaning": "matching authored content pin; not proof of the complete hosted build commit"}}
                break
        if hosted_source is None:
            raw_hosted = (json.dumps(hosted_documents[0], ensure_ascii=False, indent=2) + "\n").encode()
            hosted_path = "hosted/" + sha256(raw_hosted) + ".json"
            hosted_source = {**current, "id": "animated-current-hosted", "cache_repository": "animated-hosted",
                             "commit": None, "path": hosted_path, "sha256": sha256(raw_hosted),
                             "version_role": "current-hosted-without-resolved-git-pin",
                             "baseline": {**current["baseline"], "scope": "this currently hosted teaching reference only"},
                             "hosted": {**current["hosted"], "lesson_semantic_equal_to_main": False}}
            hosted_cache = ROOT / ".local" / "example-sources" / "animated-hosted" / "archive" / hosted_path
            hosted_cache.parent.mkdir(parents=True, exist_ok=True)
            hosted_cache.write_bytes(raw_hosted)
        write_json(output / "hosted" / "baseline-source.json", hosted_source)
        hosted_baseline = write_baseline(output, hosted_documents[0], hosted_source, "hosted-positive-reference")
        for row in config["sources"]:
            if row["id"] == "animated-current-hosted":
                if row["sha256"] != hosted_source["sha256"]:
                    archived = {**row, "id": "animated-former-hosted-" + row["sha256"][:8], "version_role": "former-hosted-snapshot"}
                    archived.pop("baseline", None)
                    if not any(source["id"] == archived["id"] for source in config["sources"]):
                        config["sources"].append(archived)
                row.update(hosted_source)
                break
        else:
            config["sources"].append(hosted_source)
    else:
        hosted_baseline = None
        for source in config["sources"]:
            if source["id"] == "animated-current-hosted":
                suffix = (source["commit"] or source["sha256"])[:8]
                archived_id = "animated-former-hosted-" + suffix
                if any(row["id"] == archived_id for row in config["sources"]):
                    archived_id += "-" + re.sub(r"[^a-z0-9]", "", timestamp.lower())
                source["id"] = archived_id
                source["version_role"] = "former-hosted-snapshot"
                source.pop("baseline", None)
    matches = [index for index, source in enumerate(config["sources"]) if source["id"] == SOURCE_ID]
    if matches:
        previous = config["sources"][matches[0]]
        if previous["commit"] != pin:
            archived_id = "animated-former-current-" + previous["commit"][:8]
            if not any(source["id"] == archived_id for source in config["sources"]):
                former_role = "former-hosted-main-snapshot" if previous["version_role"] == "current-hosted-main-at-refresh" else "former-source-main-snapshot"
                archived = {**previous, "id": archived_id, "version_role": former_role}
                archived.pop("baseline", None)
                config["sources"].append(archived)
        config["sources"][matches[0]] = current
    else:
        config["sources"].append(current)
    examples.validate_sources(config)
    cache = ROOT / ".local" / "example-sources" / "animated" / pin / LESSON_PATH
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_bytes(raw_files[LESSON_PATH])
    examples.SOURCE_CONFIG.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n")
    counts = examples.collect(ROOT / ".local" / "example-sources")
    comparisons = examples.check(cache_root=ROOT / ".local" / "example-sources")
    shutil.copytree(examples.DESTINATION, output / "question-examples")
    (output / "source-config.json").write_bytes(examples.SOURCE_CONFIG.read_bytes())
    receipt = {"intent": "Refresh the user-designated current authored teaching reference",
               "human_use": "Review the exact source pin, hosted match, native tasks, route context and asset hashes",
               "ai_use": "Read authored positive reference material without treating source keys as independent labels",
               "refreshed_at": timestamp, "repository": REPOSITORY, "commit": pin, "files": files,
               "hosted": hosted, "source": current, "routes": "routes.json", "assets": "assets.json",
               "frozen_collection": "question-examples", "frozen_source_config": "source-config.json",
               "default_positive_reference": baseline,
               "distinct_hosted_positive_reference": hosted_baseline,
               "current_counts": {"pages": len(document["pages"]), "source_occurrences": len(items),
                                  "by_kind": dict(sorted(Counter(item["kind"] for item in items).items())),
                                  "by_role": dict(sorted(Counter(item["role"] for item in items).items())),
                                  "omissions": omissions, "redactions": redactions,
                                  "assets_fetched": sum("sha256" in asset for asset in assets),
                                  "asset_errors": [asset for asset in assets if "error" in asset],
                                  "asset_source_mismatches": [asset for asset in assets if asset.get("git_blob_equal_to_main") is False or asset.get("manifest_equal") is False]},
               "collection_counts": counts, "source_comparison": comparisons,
               "limits": ["Activities include guided tasks, dependent subchecks, retained alternatives and a confidence self-report.",
                          "The shelf names four volumes; this pin has one authored lesson.",
                          "No runtime model follow-ups, learner records, independent labels or learning outcomes captured."]}
    write_json(output / "receipt.json", receipt)
    write_json(ROOT / ".local" / "current-reference.json", {
               "snapshot": str(output.relative_to(ROOT)), "receipt": str((output / "receipt.json").relative_to(ROOT)),
               "positive_reference": str((output / "positive-reference" / "manifest.json").relative_to(ROOT)),
               "source_id": SOURCE_ID, "commit": pin, "refreshed_at": timestamp,
               "designation": current["baseline"]["designation"]})
    print(json.dumps({"receipt": str((output / "receipt.json").relative_to(ROOT)), "commit": pin,
                      "current_counts": receipt["current_counts"], "collection_counts": counts}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    out = args.output or ROOT / ".local" / "current-reference" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    refresh(out)
