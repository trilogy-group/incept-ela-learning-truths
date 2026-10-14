"""Read explicit authored course tasks without executing course content.

These adapters preserve intended answers and author rubrics as source material.
They do not create assessment labels or infer a task from a lesson objective.
"""

import re


THREE_D_SELECTORS = (
    "unit_video.segments[].check",
    "lessons[].retrieval[]",
    "lessons[].independent[] (explicit prompts and stems)",
    "lessons[].closing[].text",
    "lessons[].guided.screens[]",
    "lessons[].guided.stems[]",
    "lessons[].guided.example",
    "lessons[].guided.extra[]",
    "lessons[].stages.*.more (Stems and TASK sections)",
)


def _pointer(path):
    return "/" + "/".join(str(p).replace("~", "~0").replace("/", "~1") for p in path) if path else ""


def _unit(kind, role, path, prompt, native, context_path, view=None, operation=None):
    unit = {
        "kind": kind,
        "role": role,
        "pointer": _pointer(path),
        "prompt": prompt,
        "native": native,
        "context_pointer": _pointer(context_path),
    }
    if view is not None:
        unit["view"] = view
    if operation is not None:
        unit["operation"] = operation
    return unit


def _text_parts(text):
    """Find authored turn prompts, task blocks, or explicitly headed stems."""
    lines = text.splitlines()
    oral = []
    for line in lines:
        match = re.match(r"\s*A:\s*(.*?)\s*→\s*(.*)\s*$", line)
        if match:
            oral.append(("oral_turn", "subcheck", match.group(1), {"prompt": match.group(1), "stem": match.group(2), "authored_line": line}))
    if oral:
        return oral
    tasks = list(re.finditer(r"(?m)^\s*TASK\s+(\d+)\s*:\s*", text))
    if tasks:
        result = []
        for i, match in enumerate(tasks):
            body = text[match.end():tasks[i + 1].start() if i + 1 < len(tasks) else len(text)].strip()
            number = int(match.group(1))
            role = "model_task" if number == 1 else "subcheck" if number == 2 else "question"
            result.append(("closing_task", role, body, {"n": number, "text": body, "authored_text": text}))
        # The stems before the closing section remain separately authored work.
        prefix = text[:tasks[0].start()]
        result = _text_parts(prefix) + result
        return result
    stems = []
    in_stems = False
    for line in lines:
        stripped = line.strip().strip('"')
        if re.match(r"(?i)^(?:oral\s+)?stems(?:\s+available)?\s*:", stripped):
            in_stems = True
            continue
        if in_stems and (not stripped or re.match(r"(?i)^(independent practice|closing questions|options|stage\s*\d)\s*:", stripped)):
            in_stems = False
        if in_stems and stripped:
            stems.append(("writing_stem", "model_task", stripped, {"stem": stripped, "authored_line": line, "authored_text": text}))
    return stems


def extract_three_d(document, path=()):
    """Extract explicit tasks from the authored Act 1 JSON shape.

    A prompt scaffold or guided example is marked as such. Learning-question
    fields and their repeated Stage 1 targets provide context, not extra items.
    Native source objects retain quote references, parenthetical answers and
    surrounding instructions; missing learner history is not manufactured.
    """
    if not isinstance(document, dict):
        return []
    units = []
    video = document.get("unit_video", {})
    segments = video.get("segments", []) if isinstance(video, dict) else []
    for i, segment in enumerate(segments):
        if isinstance(segment, dict) and isinstance(segment.get("check"), str) and segment["check"].strip():
            p = path + ("unit_video", "segments", i)
            units.append(_unit("film_check", "question", p, segment["check"], segment, path + ("unit_video",)))
    lessons = document.get("lessons", [])
    if not isinstance(lessons, list):
        return units
    for i, lesson in enumerate(lessons):
        if not isinstance(lesson, dict):
            continue
        lp = path + ("lessons", i)
        for j, raw in enumerate(lesson.get("retrieval", [])):
            if isinstance(raw, str) and raw.strip():
                units.append(_unit("retrieval", "recall_task", lp + ("retrieval", j), raw, raw, lp))
        for j, raw in enumerate(lesson.get("independent", [])):
            if not isinstance(raw, str):
                continue
            p = lp + ("independent", j)
            parts = _text_parts(raw)
            for part_index, (kind, role, prompt, view) in enumerate(parts):
                units.append(_unit(kind, role, p, prompt, raw, lp, view, "%s:%d" % (kind, part_index)))
            # Explicit instruction rows are retained, but titles and repeated
            # question targets are not promoted into independent questions.
            if not parts and re.match(r"(?i)^\s*(?:write|choose|explain|argue|compare|answer|say|speak)\b", raw):
                units.append(_unit("independent_task", "guided_task", p, raw, raw, lp))
        for j, task in enumerate(lesson.get("closing", [])):
            if not isinstance(task, dict) or not isinstance(task.get("text"), str) or not task["text"].strip():
                continue
            number = task.get("n")
            role = "model_task" if number == 1 else "subcheck" if number == 2 else "question"
            units.append(_unit("closing_task", role, lp + ("closing", j), task["text"], task, lp))
        guided = lesson.get("guided", {})
        if isinstance(guided, dict):
            gp = lp + ("guided",)
            for j, screen in enumerate(guided.get("screens", [])):
                if isinstance(screen, dict) and isinstance(screen.get("quote"), str) and screen["quote"].strip():
                    units.append(_unit("guided_quote", "guided_task", gp + ("screens", j), screen["quote"], screen, lp))
            for j, stem in enumerate(guided.get("stems", [])):
                if isinstance(stem, str) and stem.strip():
                    units.append(_unit("writing_stem", "model_task", gp + ("stems", j), stem, stem, lp))
            if isinstance(guided.get("example"), str) and guided["example"].strip():
                units.append(_unit("model_paragraph", "model_task", gp + ("example",), guided["example"], guided["example"], lp))
            for j, text in enumerate(guided.get("extra", [])):
                if isinstance(text, str) and ("?" in text or re.match(r"(?i)^\s*(?:task|write|choose|explain|rebuild|compare|answer|say|speak)\b", text)):
                    units.append(_unit("guided_task", "guided_task", gp + ("extra", j), text, text, lp))
        stages = lesson.get("stages", {})
        if isinstance(stages, dict):
            for stage, variant in stages.items():
                if not isinstance(variant, dict) or not isinstance(variant.get("more"), str):
                    continue
                p = lp + ("stages", stage, "more")
                for part_index, (kind, role, prompt, view) in enumerate(_text_parts(variant["more"])):
                    units.append(_unit(kind, role, p, prompt, variant["more"], lp, view, "%s:%d" % (kind, part_index)))
    return units


def three_d_omissions(document, path=()):
    """Describe unsupported task-bearing data instead of silently guessing."""
    omissions = []
    if not isinstance(document, dict):
        return [{"pointer": _pointer(path), "reason": "unsupported_document_shape"}]
    known_root = {"_source", "overview", "unit_video", "lessons"}
    for key in document:
        if key not in known_root and re.search(r"question|task|prompt|check", str(key), re.I):
            omissions.append({"pointer": _pointer(path + (key,)), "reason": "unknown_task_bearing_root_field"})
    lessons = document.get("lessons", [])
    if not isinstance(lessons, list):
        omissions.append({"pointer": _pointer(path + ("lessons",)), "reason": "unsupported_lessons_shape"})
        return omissions
    for i, lesson in enumerate(lessons):
        if not isinstance(lesson, dict):
            continue
        lp = path + ("lessons", i)
        if lesson.get("oral"):
            omissions.append({"pointer": _pointer(lp + ("oral",)), "reason": "staging_and_quote_scripts_need_static_companion_content_and_audio_context"})
        for j, text in enumerate(lesson.get("independent", [])):
            if isinstance(text, str) and not _text_parts(text) and not re.match(r"(?i)^\s*(?:write|choose|explain|argue|compare|answer|say|speak)\b", text):
                omissions.append({"pointer": _pointer(lp + ("independent", j)), "reason": "heading_target_or_unparsed_instruction_retained_only_in_context"})
        for key in lesson:
            if re.search(r"question|task|prompt|check", str(key), re.I) and key not in {"retrieval", "independent", "closing", "guided", "stages"}:
                omissions.append({"pointer": _pointer(lp + (key,)), "reason": "unknown_task_bearing_lesson_field"})
        for group in ("guided", "oral"):
            value = lesson.get(group)
            supported = {"screens", "stems", "example", "extra"} if group == "guided" else {"videos", "intro", "quotes"}
            if isinstance(value, dict):
                for key in value:
                    if key not in supported and re.search(r"question|task|prompt|check", str(key), re.I):
                        omissions.append({"pointer": _pointer(lp + (group, key)), "reason": "unknown_task_bearing_companion_field"})
    return omissions


def extract_three_d_omissions(document, path=()):
    return three_d_omissions(document, path)


class StaticLiteralError(ValueError):
    pass


class _LiteralReader:
    """Small JS/TS data-literal reader. Calls, identifiers and spreads fail."""

    def __init__(self, text, offset=0):
        self.text = text
        self.pos = offset

    def space(self):
        while self.pos < len(self.text):
            if self.text[self.pos].isspace():
                self.pos += 1
            elif self.text.startswith("//", self.pos):
                end = self.text.find("\n", self.pos)
                self.pos = len(self.text) if end < 0 else end + 1
            elif self.text.startswith("/*", self.pos):
                end = self.text.find("*/", self.pos + 2)
                if end < 0:
                    raise StaticLiteralError("unterminated_comment")
                self.pos = end + 2
            else:
                return

    def string(self):
        quote = self.text[self.pos]
        self.pos += 1
        chars = []
        escapes = {"n": "\n", "r": "\r", "t": "\t", "b": "\b", "f": "\f", "v": "\v", "0": "\0"}
        while self.pos < len(self.text):
            ch = self.text[self.pos]
            self.pos += 1
            if ch == quote:
                return "".join(chars)
            if quote == "`" and ch == "$" and self.text.startswith("{", self.pos):
                raise StaticLiteralError("template_interpolation")
            if ch == "\\":
                if self.pos >= len(self.text):
                    break
                ch = self.text[self.pos]
                self.pos += 1
                if ch in ("u", "x"):
                    size = 4 if ch == "u" else 2
                    digits = self.text[self.pos:self.pos + size]
                    if not re.fullmatch(r"[0-9a-fA-F]{" + str(size) + "}", digits):
                        raise StaticLiteralError("unsupported_character_escape")
                    chars.append(chr(int(digits, 16)))
                    self.pos += size
                elif ch == "\n":
                    continue
                else:
                    chars.append(escapes.get(ch, ch))
            else:
                chars.append(ch)
        raise StaticLiteralError("unterminated_string")

    def value(self):
        self.space()
        if self.pos >= len(self.text):
            raise StaticLiteralError("missing_literal")
        ch = self.text[self.pos]
        if ch in "\"'`":
            return self.string()
        if ch == "[":
            self.pos += 1
            result = []
            self.space()
            while self.pos < len(self.text) and self.text[self.pos] != "]":
                result.append(self.value())
                self.space()
                if self.pos < len(self.text) and self.text[self.pos] == ",":
                    self.pos += 1
                    self.space()
                elif self.pos >= len(self.text) or self.text[self.pos] != "]":
                    raise StaticLiteralError("nonliteral_array_expression")
            if self.pos >= len(self.text):
                raise StaticLiteralError("unterminated_array")
            self.pos += 1
            return result
        if ch == "{":
            self.pos += 1
            result = {}
            self.space()
            while self.pos < len(self.text) and self.text[self.pos] != "}":
                if self.text[self.pos] in "\"'`":
                    key = self.string()
                else:
                    match = re.match(r"(?:[A-Za-z_$][\w$]*|\d+)", self.text[self.pos:])
                    if not match:
                        raise StaticLiteralError("nonliteral_object_key")
                    key = match.group(0)
                    self.pos += len(key)
                self.space()
                if self.pos >= len(self.text) or self.text[self.pos] != ":":
                    raise StaticLiteralError("object_method_or_shorthand")
                self.pos += 1
                result[key] = self.value()
                self.space()
                if self.pos < len(self.text) and self.text[self.pos] == ",":
                    self.pos += 1
                    self.space()
                elif self.pos >= len(self.text) or self.text[self.pos] != "}":
                    raise StaticLiteralError("nonliteral_object_expression")
            if self.pos >= len(self.text):
                raise StaticLiteralError("unterminated_object")
            self.pos += 1
            return result
        match = re.match(r"-?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", self.text[self.pos:])
        if match:
            number = match.group(0)
            self.pos += len(number)
            return float(number) if re.search(r"[.eE]", number) else int(number)
        for word, value in (("true", True), ("false", False), ("null", None)):
            if self.text.startswith(word, self.pos) and not re.match(r"[\w$]", self.text[self.pos + len(word):self.pos + len(word) + 1]):
                self.pos += len(word)
                return value
        raise StaticLiteralError("runtime_or_identifier_expression")


def _code_mask(source):
    """Hide quoted text and comments while retaining source offsets."""
    result = list(source)
    i = 0
    while i < len(source):
        if source.startswith("//", i) or source.startswith("/*", i):
            end = source.find("\n", i) if source.startswith("//", i) else source.find("*/", i + 2)
            end = len(source) if end < 0 else end if source.startswith("//", i) else end + 2
            for j in range(i, end):
                if result[j] != "\n":
                    result[j] = " "
            i = end
        elif source[i] == "/" and (not source[:i].rstrip() or source[:i].rstrip()[-1] in "=([{,:;!"):
            # A regular expression may contain quotation marks. Treating those
            # as strings would hide unrelated later declarations.
            j = i + 1
            in_class = False
            while j < len(source):
                if source[j] == "\\":
                    j += 2
                elif source[j] == "[":
                    in_class = True
                    j += 1
                elif source[j] == "]":
                    in_class = False
                    j += 1
                elif source[j] == "/" and not in_class:
                    j += 1
                    while j < len(source) and source[j].isalpha():
                        j += 1
                    break
                else:
                    j += 1
            for k in range(i, min(j, len(source))):
                if result[k] != "\n":
                    result[k] = " "
            i = j
        elif source[i] in "\"'`":
            quote = source[i]
            j = i + 1
            while j < len(source):
                if source[j] == "\\":
                    j += 2
                elif source[j] == quote:
                    j += 1
                    break
                else:
                    j += 1
            for k in range(i, min(j, len(source))):
                if result[k] != "\n":
                    result[k] = " "
            i = j
        else:
            i += 1
    return "".join(result)


def extract_static_literals(source):
    """Recover complete JS/TS const data literals, with explicit omissions.

    This never imports or executes source. It accepts nested arrays/objects,
    primitive values, comments and trailing commas. An expression, reference,
    function, interpolation or spread makes the containing constant omitted.
    """
    constants = []
    omissions = []
    mask = _code_mask(source)
    pattern = re.compile(r"\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)(?:\s*:[^=\n]+)?\s*=")
    for match in pattern.finditer(mask):
        name = match.group(1)
        reader = _LiteralReader(source, match.end())
        line = source.count("\n", 0, match.start()) + 1
        try:
            value = reader.value()
            # Reject literal-looking prefixes of concatenations or calls.
            tail = _LiteralReader(source, reader.pos)
            tail.space()
            remainder = source[tail.pos:]
            if re.match(r"(?:[+*/.%?&|^<>=()-]|\[)", remainder):
                raise StaticLiteralError("literal_followed_by_expression")
            if remainder and not re.match(r"(?:;|,|\}|$|as\s+(?:const\b|[A-Za-z_$]))", remainder) and "\n" not in source[reader.pos:tail.pos]:
                raise StaticLiteralError("literal_followed_by_expression")
            constants.append({"name": name, "line": line, "value": value, "start": match.start(), "end": reader.pos})
        except StaticLiteralError as exc:
            omissions.append({"name": name, "line": line, "reason": str(exc)})
    return {"literals": constants, "omissions": omissions}


def extract_static_literal_fields(source, fields=("q", "prompt", "ask", "nameAsk", "confQ", "confQAns", "rebuildOpen")):
    """Read explicit quoted properties in otherwise unsupported source objects.

    The returned line/offset is a source locator, not an inferred object key or
    answer. Complete companion objects are needed for standalone task context.
    """
    mask = _code_mask(source)
    pattern = re.compile(r"\b(" + "|".join(re.escape(field) for field in fields) + r")\s*:")
    rows = []
    for match in pattern.finditer(mask):
        reader = _LiteralReader(source, match.end())
        try:
            value = reader.value()
        except StaticLiteralError:
            continue
        if isinstance(value, str):
            rows.append({"field": match.group(1), "line": source.count("\n", 0, match.start()) + 1, "start": match.start(), "end": reader.pos, "value": value})
    return rows


def static_three_d_document(source):
    """Materialize only safely parsed source data for pointer verification.

    The source hash must still refer to the original text. ``source_lines``
    preserves explicit quoted properties whose enclosing expression is omitted.
    Its line locators are declared adapter views, not source JSON structure.
    """
    parsed = extract_static_literals(source)
    document = {row["name"]: row["value"] for row in parsed["literals"]}
    document["source_lines"] = {}
    for field in extract_static_literal_fields(source):
        document["source_lines"].setdefault(str(field["line"]), {})[field["field"]] = field["value"]
    return {"document": document, "omissions": parsed["omissions"]}


def extract_three_d_literals(source, path=()):
    """Extract only explicit task selectors from safely parsed companion data."""
    parsed = extract_static_literals(source)
    values = {row["name"]: row["value"] for row in parsed["literals"]}
    units = []
    for symbol in ("CHECKS", "MICRO", "EXTRA_TURNS"):
        value = values.get(symbol, {})
        if not isinstance(value, dict):
            continue
        for group, items in value.items():
            entries = list(enumerate(items)) if isinstance(items, list) else [(None, items)]
            for i, item in entries:
                if not isinstance(item, dict):
                    continue
                prompt = item.get("q", item.get("prompt"))
                if isinstance(prompt, str):
                    p = path + (symbol, group) + (() if i is None else (i,))
                    role = "question" if symbol == "CHECKS" else "guided_task" if symbol == "MICRO" else "subcheck"
                    units.append(_unit("reading_check" if symbol == "CHECKS" else "oral_microtask", role, p, prompt, item, path + (symbol, group)))
    deck_map = values.get("DECKS", {})
    for lesson, decks in (deck_map.items() if isinstance(deck_map, dict) else []):
        if not isinstance(decks, list):
            continue
        for i, deck in enumerate(decks):
            if not isinstance(deck, dict):
                continue
            for j, gap in enumerate(deck.get("gaps", [])):
                if isinstance(gap, dict) and isinstance(gap.get("s"), str):
                    p = path + ("DECKS", lesson, i, "gaps", j)
                    units.append(_unit("vocabulary_gap", "question", p, gap["s"], gap, path + ("DECKS", lesson, i)))
    literal_fields = extract_static_literal_fields(source)
    rebuild_prompt = next((row["value"] for row in literal_fields if row["field"] == "rebuildOpen"), None)
    rebuilds = values.get("REBUILD", {})
    if rebuild_prompt and isinstance(rebuilds, dict):
        for lesson, rebuild in rebuilds.items():
            if not isinstance(rebuild, dict):
                continue
            for i, part in enumerate(rebuild.get("parts", [])):
                if isinstance(part, dict) and isinstance(part.get("options"), list) and "answer" in part:
                    p = path + ("REBUILD", lesson, "parts", i)
                    units.append(_unit("model_rebuild_gap", "model_task", p, rebuild_prompt, part, path + ("REBUILD", lesson)))
    checklist = values.get("CHECKLIST", [])
    if isinstance(checklist, list):
        for i, line in enumerate(checklist):
            if isinstance(line, str):
                units.append(_unit("paragraph_checklist", "subcheck", path + ("CHECKLIST", i), line, line, path + ("CHECKLIST",)))
    web = values.get("WEB")
    if isinstance(web, dict) and isinstance(web.get("opener"), str):
        units.append(_unit("word_web", "recall_task", path + ("WEB",), web["opener"], web, path + ("WEB",)))
    for symbol in ("DECEIT_L1", "SOLILOQUY_L3", "CHAIN_L2"):
        board = values.get(symbol)
        if isinstance(board, dict) and isinstance(board.get("prompt"), str):
            units.append(_unit("relation_board" if symbol != "CHAIN_L2" else "rank_board", "guided_task", path + (symbol,), board["prompt"], board, path + (symbol,)))
            if isinstance(board.get("nameAsk"), str):
                units.append(_unit("relation_name", "subcheck", path + (symbol, "nameAsk"), board["nameAsk"], board["nameAsk"], path + (symbol,)))
    if isinstance(values.get("STAGE_Q"), str):
        context = {key: values[key] for key in ("STAGE_Q", "STAGE_STEM", "STAGE_LINES", "READINGS") if key in values}
        units.append(_unit("staging_comparison", "guided_task", path + ("STAGE_Q",), values["STAGE_Q"], values["STAGE_Q"], path, context))
    actions = values.get("ACTS", {})
    for name, action in (actions.items() if isinstance(actions, dict) else []):
        if isinstance(action, dict) and isinstance(action.get("ask"), str):
            units.append(_unit("stage_move", "guided_task", path + ("ACTS", name), action["ask"], action, path + ("ACTS",)))
    # Unparsed scene constants still expose fixed instructions. Their action
    # targets and zones must be supplied by a complete source-context adapter.
    spans = [(row["start"], row["end"]) for row in parsed["literals"]]
    for field in literal_fields:
        if any(start <= field["start"] < end for start, end in spans):
            continue
        if field["field"] in {"ask", "confQ", "confQAns"}:
            role = "guided_task" if field["field"] == "ask" else "question"
            units.append(_unit("stage_move" if field["field"] == "ask" else "confidence_self_report", role, path + ("source_lines", str(field["line"]), field["field"]), field["value"], field["value"], path, field))
    return units
