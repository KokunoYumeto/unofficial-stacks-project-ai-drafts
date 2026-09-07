"""Check numbered TeX unit boundaries against raw LF bytes, not web text.

This checks the complete labelled environment. Ownership of following prose
proofs, subsidiary lemmas, and cross-references remains a separate semantic
decision; a passing boundary check alone is not a coverage proof.
"""
import hashlib
import re


def _uncomment(line):
    for i, char in enumerate(line):
        if char == 37:
            j = i - 1
            while j >= 0 and line[j] == 92:
                j -= 1
            if (i - j - 1) % 2 == 0:
                return line[:i]
    return line


def verify_numbered_span(raw, start, end, label):
    """Return exact span identity or raise ValueError on incomplete markers.

    start/end are physical one-based LF lines, inclusive. A preceding blank
    separator is allowed, but preceding mathematical text is not. Additional
    trailing prose may be included deliberately by the source-unit reviewer.
    """
    if b"\r" in raw or not raw.endswith(b"\n"):
        raise ValueError("source must be the pinned raw LF serialization")
    lines = raw.splitlines(keepends=True)
    if (not isinstance(start, int) or not isinstance(end, int)
            or isinstance(start, bool) or isinstance(end, bool)
            or not 1 <= start <= end <= len(lines)):
        raise ValueError("invalid physical LF line interval")
    clean = [_uncomment(line).strip() for line in lines]
    wanted = b"\\label{" + label.encode("ascii") + b"}"
    labels = [i for i, line in enumerate(clean) if line == wanted]
    if len(labels) != 1:
        raise ValueError("unit label must occur exactly once in raw source")
    label_at = labels[0]
    begin_at = label_at - 1
    while begin_at >= 0 and not clean[begin_at]:
        begin_at -= 1
    begin = re.fullmatch(rb"\\begin\{([A-Za-z*]+)\}\[([0-9.]+)\]", clean[begin_at]) if begin_at >= 0 else None
    if not begin:
        raise ValueError("unit label lacks an immediately preceding numbered environment")
    number = re.search(r"(?:^|\.)([0-9]+\.[0-9]+\.[0-9]+(?:\.[0-9]+)*)(?:-fr)?$", label)
    if number is None or begin.group(2).decode() != number.group(1):
        raise ValueError("numbered environment and label disagree")
    env = re.escape(begin.group(1))
    token = re.compile(rb"\\(begin|end)\{" + env + rb"\}")
    depth = 0
    close_at = None
    for i in range(begin_at, len(lines)):
        for match in token.finditer(_uncomment(lines[i])):
            depth += 1 if match.group(1) == b"begin" else -1
            if depth == 0:
                close_at = i
                break
        if close_at is not None:
            break
    if close_at is None:
        raise ValueError("numbered environment is unclosed")
    if not start - 1 <= begin_at <= label_at <= close_at < end:
        raise ValueError("declared source slice omits a begin, label, or closing marker")
    if any(clean[start - 1:begin_at]):
        raise ValueError("declared source slice starts in preceding mathematical content")
    block = b"".join(lines[start - 1:end])
    return {
        "label": label, "environment": begin.group(1).decode(),
        "begin_line": begin_at + 1, "label_line": label_at + 1,
        "closing_line": close_at + 1, "lf_line_start": start,
        "lf_line_end": end, "bytes": len(block),
        "sha256": hashlib.sha256(block).hexdigest().upper(),
        "byte_offset_start": sum(map(len, lines[:start - 1])),
        "byte_offset_end_exclusive": sum(map(len, lines[:end])),
    }
