"""Bounded live-byte replay of the corrected EGA I 7.1.1-7.1.3 sources.

No source tree is copied or modified. Two pinned files are read at most once,
with bounded time and size. --french and --english accept already cached files.
"""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "validation/ega-i-7.1.1-7.1.3-source-boundary-correction-2026-09-07.json"


def verify_source(raw, language, expected):
    """Derive raw environment boundaries before comparing any claimed slice."""
    errors = []
    if b"\r" in raw or not raw.endswith(b"\n"):
        return ["source must be exact LF-terminated bytes"]
    if (len(raw) != expected["full_bytes"] or
            hashlib.sha256(raw).hexdigest().upper() != expected["full_sha256"]):
        errors.append("whole-source identity mismatch")
    lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
    suffix = "-fr" if language == "fr" else ""
    for number in (1, 2, 3):
        unit = f"ega:I.7.1.{number}"
        scope = expected["slices"][unit]
        env = "definition" if number == 2 else "env"
        begin = f"\\begin{{{env}}}[7.1.{number}]\n".encode()
        label = f"\\label{{I.7.1.{number}{suffix}}}\n".encode()
        close = f"\\end{{{env}}}\n".encode()
        starts = [i for i, line in enumerate(lines) if line == begin]
        if len(starts) != 1:
            errors.append(unit + ": unique numbered begin marker missing")
            continue
        start = starts[0]
        if start + 1 >= len(lines) or lines[start + 1] != label:
            errors.append(unit + ": exact label is not adjacent to its begin")
        closes = [i for i in range(start + 1, len(lines)) if lines[i] == close]
        if not closes:
            errors.append(unit + ": closing marker missing")
            continue
        end = closes[0]
        if any(line.startswith(b"\\begin{") for line in lines[start + 1:end]):
            errors.append(unit + ": unexpected nested environment before closing marker")
        if (scope["lf_line_start"], scope["lf_line_end"]) != (start + 1, end + 1):
            errors.append(unit + ": claimed range is not the complete raw environment")
        block = b"".join(lines[start:end + 1])
        offset = sum(map(len, lines[:start]))
        if (scope["byte_offset_start"] != offset or
                scope["byte_offset_end_exclusive"] != offset + len(block) or
                scope["slice_bytes"] != len(block) or
                scope["slice_sha256"] != hashlib.sha256(block).hexdigest().upper()):
            errors.append(unit + ": complete-environment byte identity mismatch")
        if number == 3:
            ring = (b"\\emph{anneau} $R(X)$." if language == "fr"
                    else b"\\emph{ring} $R(X)$.")
            if ring not in block:
                errors.append(unit + ": final ring conclusion missing")
        if number == 2:
            graph = (b"\\Gamma_{\\mathrm{rat}}((X\\times_S Y)/X)" if language == "fr"
                     else b"\\Gamma_\\mathrm{rat}((X\\times_S Y)/X)")
            if graph not in block:
                errors.append(unit + ": final rational-section correspondence missing")
    line_no = expected["restriction_line"]
    if not 1 <= line_no <= len(lines):
        errors.append("restriction locator outside raw source")
    else:
        line = lines[line_no - 1]
        if (b"U\\cap V\\cap W" not in line or
                hashlib.sha256(line).hexdigest().upper() != expected["restriction_line_sha256"]):
            errors.append("restriction locator does not bind the actual overstatement line")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--french", type=Path)
    parser.add_argument("--english", type=Path)
    args = parser.parse_args()
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    result = {"schema": "ega-i713-raw-source-boundary-replay/v1", "sources": {}, "errors": []}
    for language, cached in (("fr", args.french), ("en", args.english)):
        expected = receipt["raw_source_boundary_witnesses"][language]
        try:
            if cached:
                with cached.open("rb") as handle:
                    raw = handle.read(expected["full_bytes"] + 1)
            else:
                with urlopen(expected["url"], timeout=30) as response:
                    raw = response.read(expected["full_bytes"] + 1)
            problems = verify_source(raw, language, expected)
            result["sources"][language] = {"bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest().upper(),
                "status": "FAIL" if problems else "PASS"}
            result["errors"].extend(language + ": " + p for p in problems)
        except (OSError, ValueError) as exc:
            result["errors"].append(language + ": bounded source read failed: " + str(exc))
    result["status"] = "FAIL" if result["errors"] else "PASS"
    print(json.dumps(result, indent=2))
    return bool(result["errors"])


if __name__ == "__main__":
    raise SystemExit(main())
