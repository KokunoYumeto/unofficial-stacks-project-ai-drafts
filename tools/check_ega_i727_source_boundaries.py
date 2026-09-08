"""Replay raw-LF ownership for EGA I 7.2.5--7.2.7, not semantic admission.

Statements, complete proofs and the old-page marker have separate identities.
The page marker remains inside the 7.2.5 proof's historical storage interval.
The following 7.2.8 begin/label is excluded boundary evidence; its mathematical
content is not reviewed. Witnesses preserve the historical relative/ordinary
wording, including the parenthetical in 7.2.7, without endorsing a strengthening.

Read each immutable URL at most once, bounded by size and timeout, or use
--french/--english cached raw files. Write neither sources nor receipts.
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
RECEIPT = ROOT / "validation/ega-i-7.2.5-7.2.7-semantic-checkpoint-2026-09-08.json"
MAX_SOURCE_BYTES = 1024 * 1024
SOURCE_URLS = {
    "fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/"
          "6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/"
          "94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
}
NUMBERS = ("7.2.5", "7.2.6", "7.2.7")
ENVIRONMENTS = ("corollary",) * 3
RANGES = {"fr": ((378, 391), (392, 403), (404, 430)),
          "en": ((227, 237), (238, 247), (248, 259))}
ENVIRONMENT_RANGES = {"fr": ((378, 385), (392, 397), (404, 414)),
                      "en": ((227, 231), (238, 242), (248, 252))}
OWNED_KEYS = tuple("ega:I." + number + ":proof" for number in NUMBERS)
OWNED_RANGES = {"fr": ((387, 390), (399, 402), (416, 429)),
                "en": ((233, 236), (244, 246), (254, 258))}
PAGE_KEY = "ega:I.7.2.5:page-marker"
PAGE_RANGES = {"fr": (387, 387), "en": (233, 233)}
PAGE_MARKER = r"\oldpage[I]{160}"
NEXT_RANGES = {"fr": (431, 432), "en": (260, 261)}
NEXT_NUMBER = "7.2.8"
NEXT_MARKERS = {
    "fr": ((431, r"\begin{env}[7.2.8]"), (432, r"\label{I.7.2.8-fr}")),
    "en": ((260, r"\begin{env}[7.2.8]"), (261, r"\label{I.7.2.8}")),
}

# Independent clause witnesses survive neither omission nor comment hiding,
# even if an adversary regenerates every receipt hash from damaged bytes.
UNIT_WITNESSES = {
    "fr": (
        (("$X$, $Y$ deux $S$-préschémas", "$X$ réduit", "$X$ et $Y$ séparés sur $S$",
          r"$p:Y\to X$ un $S$-morphisme", "(faisant de $Y$ un $X$-préschéma)",
          "$U$ un ouvert partout dense de $X$", "$f$ une $U$-section de $Y$",
          r"l'application rationnelle $\overline f$ de $X$ dans $Y$ prolongeant $f$"),
         "est une $X$-section rationnelle de $Y$."),
        (("$X$ un préschéma réduit", "$U$ un ouvert partout dense de $X$",
          "correspondance biunivoque canonique",
          r"les sections de $\mathscr{O}_X$ au-dessus de $U$",
          "les fonctions rationnelles $f$ sur $X$"), "définies en tout point de $U$."),
        (("$Y$ un préschéma réduit", r"$f:X\to Y$ un morphisme séparé",
          "$U$ un ouvert partout dense de $Y$",
          r"$g:U\to f^{-1}(U)$ une $U$-section de $f^{-1}(U)$",
          r"$Z$ le sous-préschéma réduit de $X$ ayant $\overline{g(U)}$ pour espace sous-jacent",
          r"\hyperref[I.5.2.1-fr]{5.2.1}", "$g$ soit restriction d'une $Y$-section de $X$",
          r"autrement dit (\hyperref[I.7.2.5-fr]{7.2.5})",
          "l'application rationnelle de $Y$ dans $X$ prolongeant $g$ soit partout définie",
          "il faut et il suffit que la restriction de $f$ à $Z$ soit"),
         "un isomorphisme de $Z$ sur $Y$."),
    ),
    "en": (
        (("$X$ and $Y$ be two $S$-preschemes", "$X$ is reduced",
          "$X$ and $Y$ are separated over $S$", r"$p:Y\to X$ be an $S$-morphism",
          "(making $Y$ an $X$-prescheme)", "$U$ a dense open subset of $X$",
          "$f$ a $U$-section of $Y$",
          r"the rational map $\overline{f}$ from $X$ to $Y$ extending $f$"),
         "is a rational $X$-section of $Y$."),
        (("$X$ be a reduced prescheme", "$U$ a dense open subset of $X$",
          "canonical bijective correspondence", r"sections of $\sh{O}_X$ over $U$",
          "rational functions on $X$"), "defined at every point of $U$."),
        (("$Y$ be a reduced prescheme", r"$f:X\to Y$ a separated morphism",
          "$U$ a dense open subset of $Y$",
          r"$g:U\to f^{-1}(U)$ a $U$-section of $f^{-1}(U)$",
          r"$Z$ the reduced subprescheme of $X$ that has $\overline{g(U)}$ as its underlying space",
          r"\sref{I.5.2.1}", "$g$ to be the restriction of a $Y$-section of $X$",
          r"\emph{(in other words \sref{I.7.2.5}",
          "the rational map from $Y$ to $X$ extending $g$ to be defined everywhere",
          "it is necessary and sufficient for the restriction of $f$ to $Z$ to be"),
         "an isomorphism from $Z$ to $Y$."),
    ),
}
OWNED_WITNESSES = {
    "fr": (
        (r"Il faut prouver que $p\circ\overline f$",
         ("est l'identité dans le domaine de définition", r"de $\overline f$",
          "$X$ est séparé sur $S$"), r"(\hyperref[I.7.2.2.1-fr]{7.2.2.1})."),
        (r"Compte tenu de (\hyperref[I.7.2.3-fr]{7.2.3})",
         (r"\hyperref[I.7.1.2-fr]{7.1.2}", r"\hyperref[I.7.1.3-fr]{7.1.3}",
          r"le $X$-préschéma $X\otimes_{\mathbf Z}\mathbf Z[T]$ est séparé au-dessus de $X$"),
         r"(\hyperref[I.5.5.1-fr]{5.5.1, (iv)})."),
        (r"La restriction de $f$ à $f^{-1}(U)$ est un morphisme séparé",
         (r"\hyperref[I.5.5.1-fr]{5.5.1, (i)}", "$g$ est une immersion fermée",
          r"\hyperref[I.5.4.6-fr]{5.4.6}", r"$g(U)=Z\cap f^{-1}(U)$",
          "le sous-préschéma induit par $Z$", "est identique au sous-préschéma fermé",
          r"de $f^{-1}(U)$ associé à $g$", "la condition de l'énoncé est suffisante",
          r"$f_Z:Z\to Y$", r"$\overline g:Y\to Z$ l'isomorphisme réciproque",
          r"$\overline g$ prolonge $g$", "Inversement", "$Y$-section $h$ de $X$",
          "$h$ est une immersion fermée", "$h(Y)$ est fermé", "il est contenu dans $Z$",
          "il est égal à $Z$", r"\hyperref[I.5.2.1-fr]{5.2.1}"),
         r"$h$ est nécessairement un isomorphisme de $Y$ sur le sous-préschéma fermé $Z$ de $X$."),
    ),
    "en": (
        (r"We have to show that $p\circ\overline{f}$",
         ("is the identity on the domain of definition", r"of $\overline{f}$",
          "$X$ is separated over $S$"), r"\sref{I.7.2.2.1}."),
        (r"Taking \sref{I.7.2.3}",
         (r"\sref{I.7.1.2}", r"\sref{I.7.1.3}",
          r"the $X$-prescheme $X\otimes_{\bb{Z}}\bb{Z}[T]$ is separated over $X$"),
         r"\sref{I.5.5.1}[iv]."),
        (r"The restriction of $f$ to $f^{-1}(U)$ is a separated morphism",
         (r"\sref{I.5.5.1}[i]", "$g$ is a closed immersion", r"\sref{I.5.4.6}",
          r"$g(U)=Z\cap f^{-1}(U)$", "the subprescheme induced by $Z$",
          "is identical to the closed subprescheme", r"of $f^{-1}(U)$ associated to $g$",
          "the stated condition is sufficient", r"$f_Z:Z\to Y$",
          r"$\overline{g}:Y\to Z$ is the inverse isomorphism", r"$\overline{g}$ extends $g$",
          "Conversely", "$Y$-section $h$ of $X$", "$h$ is a closed immersion",
          "$h(Y)$ is closed", "it is contained in $Z$", "is equal to $Z$",
          r"\sref{I.5.2.1}"),
         "$h$ is necessarily an isomorphism from $Y$ to the closed subprescheme $Z$ of $X$."),
    ),
}
NUMBERED_BEGIN = re.compile(rb"\\begin\{([A-Za-z*]+)\}\[([0-9.]+)\]")
ENVIRONMENT_TOKEN = re.compile(rb"\\(?:begin|end)\{[A-Za-z*]+\}")


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
    """Mechanical receipt-builder metadata; not a substitute for verification."""
    if not isinstance(language, str) or language not in RANGES:
        raise ValueError("unsupported source language")
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
        "owned_parts": {key: raw_span(lines, *interval)
                        for key, interval in zip(OWNED_KEYS, OWNED_RANGES[language])},
        "page_markers": {PAGE_KEY: raw_span(lines, *PAGE_RANGES[language])},
        "combined": raw_span(lines, RANGES[language][0][0], RANGES[language][-1][1]),
        "next_excluded_boundary": {"source_unit": "ega:I." + NEXT_NUMBER,
                                   **raw_span(lines, *NEXT_RANGES[language])},
    }


def verify_source(raw, language, expected):
    """Return identity, independent-boundary and source-clause failures."""
    if not isinstance(language, str) or language not in RANGES:
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
    if len(lines) < NEXT_RANGES[language][1]:
        return errors + ["source omits the following 7.2.8 begin/label boundary"]
    clean = [_uncomment(line).strip() for line in lines]
    # Search within lines as well: an injected numbered begin followed by text
    # is still a foreign mathematical owner, not invisible to source order.
    numbered = [(i + 1, match.group(1).decode(), match.group(2).decode())
                for i, line in enumerate(clean) for match in NUMBERED_BEGIN.finditer(line)]
    units = {"ega:I." + number for number in NUMBERS}
    inventories = {}
    for key, required in (("slices", units), ("numbered_environments", units),
                          ("owned_parts", set(OWNED_KEYS)), ("page_markers", {PAGE_KEY})):
        inventory = expected.get(key)
        inventories[key] = inventory if isinstance(inventory, dict) else {}
        if set(inventories[key]) != required:
            errors.append(key + ": exact inventory of independent semantic owners required")
    suffix = "-fr" if language == "fr" else ""
    for index, (number, env, interval, env_interval) in enumerate(zip(
            NUMBERS, ENVIRONMENTS, RANGES[language], ENVIRONMENT_RANGES[language])):
        unit = "ega:I." + number
        env_start, env_end = env_interval
        if [entry for entry in numbered if entry[2] == number] != [(env_start, env, number)]:
            errors.append(unit + ": unique numbered begin differs from independent source boundary")
        following = [entry for entry in numbered if entry[0] > env_start]
        next_expected = ((ENVIRONMENT_RANGES[language][index + 1][0], "corollary", NUMBERS[index + 1])
                         if index < 2 else (NEXT_RANGES[language][0], "env", NEXT_NUMBER))
        if not following or following[0] != next_expected:
            errors.append(unit + ": next numbered begin violates complete source order")
        if inventories["slices"].get(unit) != raw_span(lines, *interval):
            errors.append(unit + ": complete source-order span identity mismatch")
        label = "I." + number + suffix
        label_token = (r"\label{" + label + "}").encode()
        if sum(line.count(label_token) for line in clean) != 1:
            errors.append(unit + ": unit label must occur exactly once, including inline occurrences")
        try:
            actual = verify_numbered_span(raw, env_start, env_end, label)
            if (actual["begin_line"] != env_start or actual["label_line"] != env_start + 1
                    or actual["closing_line"] != env_end or actual["environment"] != env
                    or clean[env_end - 1] != (r"\end{" + env + "}").encode()):
                errors.append(unit + ": complete numbered environment boundary mismatch")
            if inventories["numbered_environments"].get(unit) != actual:
                errors.append(unit + ": numbered environment identity mismatch")
            body = _text(lines[actual["label_line"]:actual["closing_line"] - 1])
            required, final = UNIT_WITNESSES[language][index]
            if any(token.encode() not in body for token in required) or not body.endswith(final.encode()):
                errors.append(unit + ": final statement semantic witness missing")
            if ENVIRONMENT_TOKEN.search(body):
                errors.append(unit + ": unexpected nested statement wrapper")
        except ValueError as exc:
            errors.append(unit + ": " + str(exc))
    for index, (key, interval, (initial, required, final)) in enumerate(zip(
            OWNED_KEYS, OWNED_RANGES[language], OWNED_WITNESSES[language])):
        start, end = interval
        if inventories["owned_parts"].get(key) != raw_span(lines, *interval):
            errors.append(key + ": complete independently owned proof span identity mismatch")
        # The old-page line has its own identity but is also physically retained
        # by the complete first proof span. It is not a proof-body delimiter.
        body_lines = [line for line in clean[start if index == 0 else start - 1:end] if line]
        if language == "en":
            wrapper_start = start + 1 if index == 0 else start
            if (clean[wrapper_start - 1] != b"\\begin{proof}" or clean[end - 1] != b"\\end{proof}"
                    or len(body_lines) < 3 or body_lines[0] != b"\\begin{proof}"
                    or body_lines[-1] != b"\\end{proof}"
                    or any(ENVIRONMENT_TOKEN.search(line) for line in body_lines[1:-1])):
                errors.append(key + ": complete English proof wrapper missing or duplicated")
            body_lines = body_lines[1:-1]
        elif any(ENVIRONMENT_TOKEN.search(line) for line in body_lines):
            errors.append(key + ": French unwrapped proof has an unexpected wrapper")
        body = _text(body_lines)
        if not body.startswith(initial.encode()) or any(token.encode() not in body for token in required):
            errors.append(key + ": independent proof ownership/semantic witness missing")
        if not body.endswith(final.encode()):
            errors.append(key + ": final proof semantic conclusion missing")
    if inventories["page_markers"].get(PAGE_KEY) != raw_span(lines, *PAGE_RANGES[language]):
        errors.append("old-page marker identity mismatch")
    page_line = PAGE_RANGES[language][0]
    marker = PAGE_MARKER.encode()
    if clean[page_line - 1] != marker or sum(line.count(marker) for line in clean) != 1:
        errors.append("old-page marker must occur exactly once at raw LF " + str(page_line))
    covered = set()
    for start, end in (*ENVIRONMENT_RANGES[language], *OWNED_RANGES[language]):
        covered.update(range(start, end + 1))
    for n in range(RANGES[language][0][0], RANGES[language][-1][1] + 1):
        if n not in covered and clean[n - 1]:
            errors.append("unowned substantive source line: " + str(n))
    if expected.get("combined") != raw_span(lines, RANGES[language][0][0], RANGES[language][-1][1]):
        errors.append("complete combined source-order span identity mismatch")
    if expected.get("next_excluded_boundary") != {
            "source_unit": "ega:I." + NEXT_NUMBER, **raw_span(lines, *NEXT_RANGES[language])}:
        errors.append("next excluded 7.2.8 boundary must retain only its complete begin/label")
    for n, text in NEXT_MARKERS[language]:
        marker = text.encode()
        if clean[n - 1] != marker or sum(line.count(marker) for line in clean) != 1:
            errors.append("next excluded 7.2.8 marker must occur exactly once at raw LF " + str(n))
    if [entry for entry in numbered if entry[2] == NEXT_NUMBER] != [
            (NEXT_RANGES[language][0], "env", NEXT_NUMBER)]:
        errors.append("following 7.2.8 numbered begin boundary mismatch")
    return errors


def _read_parameters(expected, language):
    if not isinstance(language, str) or language not in SOURCE_URLS or not isinstance(expected, dict):
        raise ValueError("unsupported source language or malformed source receipt")
    size = expected.get("full_bytes")
    if type(size) is not int or not 0 < size <= MAX_SOURCE_BYTES:
        raise ValueError("invalid bounded whole-source byte count")
    if expected.get("url") != SOURCE_URLS[language]:
        raise ValueError("source URL is not pinned")
    return size


def read_source(expected, language, cached=None):
    size = _read_parameters(expected, language)
    if cached is not None:
        with cached.open("rb") as handle:
            return handle.read(size + 1)
    with urlopen(SOURCE_URLS[language], timeout=30) as response:
        return response.read(size + 1)


def _validate_span_shape(span, extra=()):
    integer_fields = ("lf_line_start", "lf_line_end", "bytes", "byte_offset_start",
                      "byte_offset_end_exclusive")
    if (not isinstance(span, dict) or set(span) != {*integer_fields, "sha256", *extra}
            or any(type(span.get(key)) is not int for key in integer_fields)
            or not 1 <= span["lf_line_start"] <= span["lf_line_end"]
            or span["bytes"] <= 0 or span["byte_offset_start"] < 0
            or span["byte_offset_end_exclusive"] != span["byte_offset_start"] + span["bytes"]
            or not isinstance(span.get("sha256"), str)
            or not re.fullmatch(r"[0-9A-F]{64}", span["sha256"])):
        raise ValueError("malformed raw-LF span identity")


def _validate_receipt_shape(expected, language):
    """Reject malformed nested metadata before either source is read."""
    _read_parameters(expected, language)
    for key, required in (("slices", {"ega:I." + n for n in NUMBERS}),
                          ("numbered_environments", {"ega:I." + n for n in NUMBERS}),
                          ("owned_parts", set(OWNED_KEYS)), ("page_markers", {PAGE_KEY})):
        inventory = expected.get(key)
        if not isinstance(inventory, dict) or set(inventory) != required:
            raise ValueError(language + ": malformed " + key + " inventory")
        for span in inventory.values():
            extra = ("label", "environment", "begin_line", "label_line", "closing_line") if key == "numbered_environments" else ()
            _validate_span_shape(span, extra)
            if extra and (not isinstance(span["label"], str) or span["environment"] != "corollary"
                          or any(type(span[field]) is not int or span[field] < 1
                                 for field in ("begin_line", "label_line", "closing_line"))):
                raise ValueError(language + ": malformed numbered environment identity")
    _validate_span_shape(expected.get("combined"))
    boundary = expected.get("next_excluded_boundary")
    _validate_span_shape(boundary, ("source_unit",))
    if (boundary["source_unit"] != "ega:I." + NEXT_NUMBER
            or not isinstance(expected.get("full_sha256"), str)
            or not re.fullmatch(r"[0-9A-F]{64}", expected["full_sha256"])):
        raise ValueError(language + ": malformed source identity inventory")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, default=RECEIPT)
    parser.add_argument("--french", type=Path)
    parser.add_argument("--english", type=Path)
    args = parser.parse_args(argv)
    result = {"schema": "ega-i727-raw-source-boundary-replay/v1", "sources": {}, "errors": []}
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
        languages = receipt["languages"]
        if not isinstance(languages, dict) or set(languages) != {"fr", "en"}:
            raise ValueError("languages must contain exactly fr and en")
        # Validate both entries before any I/O so malformed inventories cannot
        # trigger a partial network replay.
        for language in ("fr", "en"):
            _validate_receipt_shape(languages[language], language)
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
