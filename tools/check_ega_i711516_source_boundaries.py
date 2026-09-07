"""Replay exact raw-LF ownership for EGA I 7.1.15--7.1.16.

Keep both introductory passages and the complete 7.1.15 proof distinct from
the numbered statements. The following 7.2 heading/labels/begin boundary are
excluded context, not reviewed mathematics. Historical geometric-point wording
is preserved as source evidence; this primitive does not adjudicate terminology
or prove the mathematical correspondence.

Read two immutable source URLs once each, with bounded size and timeout, or use
--french/--english cached raw files. No source copy or receipt is written.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.request import urlopen

try:
    from tools.ega_raw_source_boundaries import _uncomment, verify_numbered_span
except ModuleNotFoundError:
    from ega_raw_source_boundaries import _uncomment, verify_numbered_span


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "validation/ega-i-7.1.15-7.1.16-semantic-checkpoint-2026-09-07.json"
MAX_SOURCE_BYTES = 1024 * 1024
SOURCE_URLS = {
    "fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/"
          "6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/"
          "94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
}
NUMBERS = ("7.1.15", "7.1.16")
ENVIRONMENTS = ("corollary", "corollary")
RANGES = {"fr": ((259, 278), (279, 289)), "en": ((150, 161), (162, 168))}
ENVIRONMENT_RANGES = {"fr": ((263, 272), (281, 288)), "en": ((151, 156), (163, 167))}
OWNED_KEYS = ("ega:I.7.1.15:introduction", "ega:I.7.1.15:proof", "ega:I.7.1.16:introduction")
OWNED_RANGES = {"fr": ((259, 261), (274, 277), (279, 279)),
                "en": ((150, 150), (158, 160), (162, 162))}
NEXT_CONTEXT_RANGES = {
    "fr": {"heading": (290, 290), "labels": (291, 291), "boundary": (293, 294), "combined": (290, 294)},
    "en": {"heading": (169, 169), "labels": (170, 171), "boundary": (173, 174), "combined": (169, 174)},
}
NEXT_MARKERS = {
    "fr": ((290, r"\subsection{Domaine de définition d'une application rationnelle.}"),
           (291, r"\label{subsection:I.7.2-fr}"), (293, r"\begin{env}[7.2.1]"),
           (294, r"\label{I.7.2.1-fr}")),
    "en": ((169, r"\subsection{Domain of definition of a rational map}"),
           (170, r"\label{subsection:I.7.2}"), (171, r"\label{I.7.2}"),
           (173, r"\begin{env}[7.2.1]"), (174, r"\label{I.7.2.1}")),
}
# Required tokens and final substantive suffix, independent of receipt hashes.
# Both the fixed fibre and the base-compatible embedding are source clauses.
UNIT_WITNESSES = {
    "fr": (
        ((r"\hyperref[I.7.1.12-fr]{7.1.12}", "$X$ est intègre", "$s$ l'image de $x$ dans $S$",
          "$S$-applications rationnelles de $X$ dans $Y$", "aux points géométriques",
          r"de $Y\otimes_S k(s)$", "à valeurs dans l'extension $R(X)$ de $k(s)$",
          "chacune d'elles équivaut à la donnée", r"d'un point $y\in Y$ au-dessus de $s$",
          "$k(s)$-monomorphisme de $k(y)$ dans"), "$k(x)=R(X)$."),
        (("$k$ un corps", "$X$, $Y$ deux préschémas algébriques",
          r"\hyperref[I.6.4.1-fr]{6.4.1}", "sur $k$", "$X$ intègre",
          "$k$-applications rationnelles de $X$ dans $Y$", "aux points géométriques de $Y$",
          "à valeurs dans l'extension $R(X)$ de $k$"), r"(\hyperref[I.3.4.4-fr]{3.4.4})."),
    ),
    "en": (
        ((r"\sref{I.7.1.12}", "$X$ is integral", "$s$ be the image of $x$ in $S$",
          "rational $S$-maps from $X$ to $Y$", "the geometric points",
          r"of $Y\otimes_S\kres(s)$", r"with values in the extension $R(X)$ of $\kres(s)$",
          "every such map is equivalent to the data", r"of a point $y\in Y$ above $s$",
          r"$\kres(s)$-monomorphism from $\kres(y)$ to"), r"$\kres(x)=R(X)$."),
        (("$k$ be a field", "$X$ and $Y$ two algebraic preschemes over $k$",
          r"\sref{I.6.4.1}", "$X$ is integral", "rational $k$-maps from $X$ to $Y$",
          "the geometric points of $Y$", "with values in the extension $R(X)$ of $k$"),
         r"\sref{I.3.4.4}."),
    ),
}
OWNED_WITNESSES = {
    "fr": (
        ("Lorsque $X$ est intègre", (r"$R(X)=\mathscr{O}_x=k(x)$ est un corps",
         r"\hyperref[I.7.1.5-fr]{7.1.5}", "les corollaires précédents se spécialisent"), "alors en~:"),
        ("Les points de $Y$ au-dessus de $s$", ("s'identifient en effet à ceux de",
         r"$Y\otimes_S k(s)$", r"\hyperref[I.3.6.3-fr]{3.6.3}",
         r"$\mathscr{O}_s$-homomorphismes locaux $\mathscr{O}_y\to R(X)$"),
         r"$k(s)$-monomorphismes $k(y)\to R(X)$."),
        ("Plus particulièrement~:", (), "Plus particulièrement~:"),
    ),
    "en": (
        ("When $X$ is integral", (r"$R(X)=\sh{O}_x=\kres(x)$ is a field",
         r"\sref{I.7.1.5}", "the preceding corollaries"), "then specialize to the following:"),
        ("The points of $Y$ above $s$", ("are identified with the points of",
         r"$Y\otimes_S\kres(s)$", r"\sref{I.3.6.3}",
         r"local $\sh{O}_s$-homomorphisms $\sh{O}_y\to R(X)$"),
         r"$\kres(s)$-monomorphisms $\kres(y)\to R(X)$."),
        ("More precisely:", (), "More precisely:"),
    ),
}
NUMBERED_BEGIN = re.compile(rb"\\begin\{([A-Za-z*]+)\}\[([0-9.]+)\]")


def raw_lines(raw):
    if not isinstance(raw, bytes) or b"\r" in raw or not raw.endswith(b"\n"):
        raise ValueError("source must be exact LF-terminated bytes")
    return [line + b"\n" for line in raw.split(b"\n")[:-1]]


def raw_span(lines, start, end):
    """Identity of an inclusive physical-LF interval, retaining its final LF."""
    if type(start) is not int or type(end) is not int or not 1 <= start <= end <= len(lines):
        raise ValueError("invalid physical LF line interval")
    block = b"".join(lines[start - 1:end])
    offset = sum(map(len, lines[:start - 1]))
    return {"lf_line_start": start, "lf_line_end": end, "bytes": len(block),
            "sha256": hashlib.sha256(block).hexdigest().upper(), "byte_offset_start": offset,
            "byte_offset_end_exclusive": offset + len(block)}


def _text(lines):
    return b" ".join(b" ".join(_uncomment(line).strip() for line in lines).split())


def source_metadata(raw, language):
    """Mechanical receipt generator; not a substitute for verify_source."""
    lines = raw_lines(raw)
    suffix = "-fr" if language == "fr" else ""
    return {
        "url": SOURCE_URLS[language], "full_bytes": len(raw),
        "full_sha256": hashlib.sha256(raw).hexdigest().upper(),
        "slices": {"ega:I." + number: raw_span(lines, *interval)
                   for number, interval in zip(NUMBERS, RANGES[language])},
        "numbered_environments": {"ega:I." + number: verify_numbered_span(
            raw, *interval, "I." + number + suffix)
            for number, interval in zip(NUMBERS, ENVIRONMENT_RANGES[language])},
        "combined": raw_span(lines, RANGES[language][0][0], RANGES[language][-1][1]),
        "owned_parts": {key: raw_span(lines, *interval)
                        for key, interval in zip(OWNED_KEYS, OWNED_RANGES[language])},
        "next_excluded_context": {"source_unit": "ega:I.7.2.1", **{
            key: raw_span(lines, *interval) for key, interval in NEXT_CONTEXT_RANGES[language].items()}},
    }


def verify_source(raw, language, expected):
    """Return all source-identity, independent-boundary and witness failures."""
    if language not in RANGES:
        return ["unsupported source language"]
    if not isinstance(expected, dict):
        return ["source receipt must be an object"]
    try:
        lines = raw_lines(raw)
    except ValueError as exc:
        return [str(exc)]
    errors = []
    if expected.get("url") != SOURCE_URLS[language]:
        errors.append("source URL is not the pinned authority/discovery URL")
    if (type(expected.get("full_bytes")) is not int or len(raw) != expected.get("full_bytes")
            or hashlib.sha256(raw).hexdigest().upper() != expected.get("full_sha256")):
        errors.append("whole-source identity mismatch")
    if len(lines) < NEXT_CONTEXT_RANGES[language]["boundary"][1]:
        return errors + ["source omits the following 7.2 heading/labels/begin boundary"]
    clean = [_uncomment(line).strip() for line in lines]
    suffix = "-fr" if language == "fr" else ""
    numbered = [(i + 1, match.group(1).decode(), match.group(2).decode())
                for i, line in enumerate(clean) if (match := NUMBERED_BEGIN.fullmatch(line))]
    units = {"ega:I." + number for number in NUMBERS}
    inventories = {}
    for key in ("slices", "numbered_environments", "owned_parts"):
        inventory = expected.get(key)
        inventories[key] = inventory if isinstance(inventory, dict) else {}
        required = set(OWNED_KEYS) if key == "owned_parts" else units
        if set(inventories[key]) != required:
            errors.append(key + ": exact inventory of independent semantic owners required")
    for index, (number, env, interval, env_interval) in enumerate(zip(
            NUMBERS, ENVIRONMENTS, RANGES[language], ENVIRONMENT_RANGES[language])):
        unit = "ega:I." + number
        env_start, env_end = env_interval
        if [entry for entry in numbered if entry[2] == number] != [(env_start, env, number)]:
            errors.append(unit + ": unique numbered begin differs from independent source boundary")
        following = [entry for entry in numbered if entry[0] > env_start]
        next_expected = ((ENVIRONMENT_RANGES[language][1][0], "corollary", "7.1.16") if index == 0
                         else (NEXT_CONTEXT_RANGES[language]["boundary"][0], "env", "7.2.1"))
        if not following or following[0] != next_expected:
            errors.append(unit + ": next numbered begin violates complete source order")
        if inventories["slices"].get(unit) != raw_span(lines, *interval):
            errors.append(unit + ": complete source-order span identity mismatch")
        try:
            actual = verify_numbered_span(raw, env_start, env_end, "I." + number + suffix)
            if (actual["begin_line"] != env_start or actual["label_line"] != env_start + 1
                    or actual["closing_line"] != env_end or actual["environment"] != env):
                errors.append(unit + ": complete numbered environment boundary mismatch")
            if inventories["numbered_environments"].get(unit) != actual:
                errors.append(unit + ": numbered environment identity mismatch")
            body = _text(lines[actual["label_line"]:actual["closing_line"] - 1])
            required, final = UNIT_WITNESSES[language][index]
            if any(token.encode() not in body for token in required) or not body.endswith(final.encode()):
                errors.append(unit + ": final statement semantic witness missing")
        except ValueError as exc:
            errors.append(unit + ": " + str(exc))
    for key, interval, (initial, required, final) in zip(
            OWNED_KEYS, OWNED_RANGES[language], OWNED_WITNESSES[language]):
        start, end = interval
        if inventories["owned_parts"].get(key) != raw_span(lines, *interval):
            errors.append(key + ": complete independently owned span identity mismatch")
        body_lines = [line for line in clean[start - 1:end] if line]
        if language == "en" and key.endswith(":proof"):
            if (len(body_lines) < 3 or body_lines[0] != b"\\begin{proof}"
                    or body_lines[-1] != b"\\end{proof}"
                    or any(re.search(rb"\\(?:begin|end)\{proof\}", line) for line in body_lines[1:-1])):
                errors.append(key + ": complete English proof wrapper missing or duplicated")
            body_lines = body_lines[1:-1]
        body = _text(body_lines)
        if not body.startswith(initial.encode()) or any(token.encode() not in body for token in required):
            errors.append(key + ": independent ownership/semantic witness missing")
        if not body.endswith(final.encode()):
            errors.append(key + ": final proof/intro semantic conclusion missing")
    # These explicitly assigned owners exhaust the tranche. In particular there
    # is no unwrapped or wrapped continuation proof following 7.1.16.
    covered = set()
    for start, end in (*ENVIRONMENT_RANGES[language], *OWNED_RANGES[language]):
        covered.update(range(start, end + 1))
    for n in range(RANGES[language][0][0], RANGES[language][-1][1] + 1):
        if n not in covered and clean[n - 1]:
            errors.append("unowned substantive source line: " + str(n))
    if expected.get("combined") != raw_span(lines, RANGES[language][0][0], RANGES[language][-1][1]):
        errors.append("complete combined source-order span identity mismatch")

    parts = {key: raw_span(lines, *interval) for key, interval in NEXT_CONTEXT_RANGES[language].items()}
    if expected.get("next_excluded_context") != {"source_unit": "ega:I.7.2.1", **parts}:
        errors.append("next excluded 7.2.1 context must retain complete section heading/labels/begin boundary")
    markers = NEXT_MARKERS[language]
    for n, marker in markers:
        if clean[n - 1] != marker.encode() or clean.count(marker.encode()) != 1:
            errors.append("next excluded 7.2 marker must occur exactly once at raw LF " + str(n))
    first = NEXT_CONTEXT_RANGES[language]["heading"][0]
    last = NEXT_CONTEXT_RANGES[language]["boundary"][1]
    marker_lines = {n for n, _ in markers}
    if any(clean[n - 1] for n in range(first, last + 1) if n not in marker_lines):
        errors.append("next excluded context has unowned prose before 7.2.1")
    after_end = ENVIRONMENT_RANGES[language][-1][1]
    next_nonblank = next((i + 1 for i in range(after_end, len(clean)) if clean[i]), None)
    if next_nonblank != first:
        errors.append("7.1.16 has unexpected trailing proof/content before the next section heading")
    next_start = NEXT_CONTEXT_RANGES[language]["boundary"][0]
    if [entry for entry in numbered if entry[2] == "7.2.1"] != [(next_start, "env", "7.2.1")]:
        errors.append("following 7.2.1 numbered begin boundary mismatch")
    return errors


def read_source(expected, language, cached=None):
    if language not in SOURCE_URLS or not isinstance(expected, dict):
        raise ValueError("unsupported source language or malformed source receipt")
    size = expected.get("full_bytes")
    if type(size) is not int or not 0 < size <= MAX_SOURCE_BYTES:
        raise ValueError("invalid bounded whole-source byte count")
    if expected.get("url") != SOURCE_URLS[language]:
        raise ValueError("source URL is not pinned")
    if cached is not None:
        with cached.open("rb") as handle:
            return handle.read(size + 1)
    with urlopen(SOURCE_URLS[language], timeout=30) as response:
        return response.read(size + 1)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, default=RECEIPT)
    parser.add_argument("--french", type=Path)
    parser.add_argument("--english", type=Path)
    args = parser.parse_args(argv)
    result = {"schema": "ega-i711516-raw-source-boundary-replay/v1", "sources": {}, "errors": []}
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
        languages = receipt["languages"]
        if not isinstance(languages, dict) or set(languages) != {"fr", "en"}:
            raise ValueError("languages must contain exactly fr and en")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result["errors"].append("source receipt read failed: " + str(exc))
        languages = {}
    for language, cached in (("fr", args.french), ("en", args.english)):
        if language not in languages:
            continue
        try:
            expected = languages[language]
            raw = read_source(expected, language, cached)
            problems = verify_source(raw, language, expected)
            result["sources"][language] = {"bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest().upper(),
                "status": "FAIL" if problems else "PASS"}
            result["errors"].extend(language + ": " + problem for problem in problems)
        except (OSError, ValueError) as exc:
            result["errors"].append(language + ": bounded source read failed: " + str(exc))
    result["status"] = "FAIL" if result["errors"] else "PASS"
    print(json.dumps(result, indent=2))
    return bool(result["errors"])


if __name__ == "__main__":
    raise SystemExit(main())
