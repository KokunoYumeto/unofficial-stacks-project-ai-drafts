"""Replay the complete raw-LF EGA I 7.1.4--7.1.9.1 source boundaries.

The numbered slices run through the line before the next numbered unit.
Unwrapped prose ownership is checked independently: the deduction following
the 7.1.9.1 statement belongs to 7.1.9, not to the lemma's proof.
Only two pinned source files are read, once each, with bounded size and time.
No source copy is created. --french and --english accept cached raw files.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.request import urlopen

try:
    from tools.ega_raw_source_boundaries import _uncomment, verify_numbered_span
except ModuleNotFoundError:  # Also support direct execution from tools/.
    from ega_raw_source_boundaries import _uncomment, verify_numbered_span


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "validation/ega-i-7.1.4-7.1.9.1-semantic-checkpoint-2026-09-07.json"
MAX_SOURCE_BYTES = 1024 * 1024
SOURCE_URLS = {
    "fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/"
          "6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/"
          "94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
}
NUMBERS = ("7.1.4", "7.1.5", "7.1.6", "7.1.7", "7.1.8", "7.1.9", "7.1.9.1")
ENVIRONMENTS = ("env", "proposition", "env", "proposition", "corollary", "corollary", "lemma")
RANGES = {
    "fr": ((72, 84), (85, 114), (115, 131), (132, 141), (142, 149), (150, 159), (160, 191)),
    "en": ((37, 44), (45, 58), (59, 68), (69, 74), (75, 80), (81, 87), (88, 99)),
}
OWNED_KEYS = ("ega:I.7.1.5:proof", "ega:I.7.1.5:tail",
              "ega:I.7.1.9:deduction", "ega:I.7.1.9.1:proof")
OWNED_RANGES = {
    "fr": ((95, 103), (105, 113), (167, 175), (177, 190)),
    "en": ((51, 55), (57, 57), (93, 93), (95, 98)),
}
# These witnesses are independent of the receipt. They bind the final
# mathematical clauses, not merely the closing environment or arbitrary hash.
UNIT_WITNESSES = {
    "fr": (
        (r"\emph{germes de morphismes}", "générique $x$ de $X$. En particulier~:"),
        (r"corps des fractions de $A(X)$", "$X$ est un schéma affine."),
        ("(arbitrairement)", "Donc~:"),
        (r"produit des $R_i$", r"($1\leq i\leq n$)."),
        (r"$\mathscr{O}_{x_i}$", "de $X$."),
        ("idéaux premiers minimaux", r"fractions $Q^{-1}A$."),
        ("tout ouvert dense", r"de la forme $D(f)$, où $f\in Q$."),
    ),
    "en": (
        (r"\emph{germs of morphisms}", "In particular:"),
        ("a local Artinian ring", r"field of fractions of $A(X)$."),
        ("(arbitrarily)", r"a morphism from each of the $U_i$ to $Y$."),
        (r"product of the $R_i$", r"($1\leq i\leq n$)."),
        (r"$\sh{O}_{x_i}$", "irreducible components of $X$."),
        ("minimal prime ideals", r"ring of fractions $Q^{-1}A$."),
        ("every dense open subset", r"where $f\in Q$."),
    ),
}
# (initial anchor, required mathematical tokens, final substantive suffix).
OWNED_WITNESSES = {
    "fr": (
        ("Vu ce qui précède", ("nilradical", "est nilpotent", r"$\mathscr{O}_x=A_{\mathfrak{j}_x}$"),
         r"$\mathscr{O}_x=A_{\mathfrak{j}_x}$ artinien."),
        (r"Si $X$ est \emph{intègre}", (r"\emph{corps des fractions de $\mathscr{O}_z$}",
         r"un sous-anneau de $R(X)$"), "partout dense) ayant pour germe $s$ au point $z$."),
        ("En effet, supposons ce lemme démontré", (r"\Gamma(D(f),\mathscr{O}_X)",
         "ensemble cofinal", r"limite inductive des $A_f$", r"$Q^{-1}A$"),
         r"(\hyperref[0.1.4.5-fr]{0, 1.4.5})."),
        (r"Pour démontrer (\hyperref[I.7.1.9.1-fr]{7.1.9.1})", ("idéaux premiers minimaux",
         "n'est donc pas contenu dans leur réunion", r"$D(f)\subset U$"), "achève la démonstration."),
    ),
    "en": (
        (r"\begin{proof}", ("nilradical", "is nilpotent", r"$\sh{O}_x=A_{\mathfrak{j}_x}$"),
         r"$\sh{O}_x=A_{\mathfrak{j}_x}$ is Artinian."),
        (r"If $X$ is \emph{integral}", (r"\emph{field of fractions of $\sh{O}_z$}",
         r"with a subring of $R(X)$"), "having $s$ as its germ at the point $z$."),
        ("Indeed, suppose the lemma proved.", (r"\Gamma(D(f),\sh{O}_X)",
         "cofinal family", r"direct limit of the $A_f$", r"$Q^{-1}A$"), r"\sref[0]{0.1.4.5}."),
        (r"\begin{proof}", (r"To show \hyperref[I.7.1.9.1]{(7.1.9.1)}", "minimal prime ideals",
         "not contained in their union", r"$D(f)\subset U$"), "which finishes the proof."),
    ),
}
NUMBERED_BEGIN = re.compile(rb"\\begin\{([A-Za-z*]+)\}\[([0-9.]+)\]")


def raw_span(lines, start, end):
    """Identity of an independently chosen inclusive physical-LF interval."""
    block = b"".join(lines[start - 1:end])
    offset = sum(map(len, lines[:start - 1]))
    return {"lf_line_start": start, "lf_line_end": end, "bytes": len(block),
            "sha256": hashlib.sha256(block).hexdigest().upper(),
            "byte_offset_start": offset, "byte_offset_end_exclusive": offset + len(block)}


def _text(lines):
    return b" ".join(b" ".join(_uncomment(line).strip() for line in lines).split())


def verify_source(raw, language, expected):
    """Return all structural, ownership, semantic, and byte-identity errors."""
    if language not in RANGES:
        return ["unsupported source language"]
    if not isinstance(expected, dict):
        return ["source receipt must be an object"]
    if not isinstance(raw, bytes) or b"\r" in raw or not raw.endswith(b"\n"):
        return ["source must be exact LF-terminated bytes"]
    errors = []
    if expected.get("url") != SOURCE_URLS[language]:
        errors.append("source URL is not the pinned authority/discovery URL")
    if (type(expected.get("full_bytes")) is not int or len(raw) != expected.get("full_bytes")
            or hashlib.sha256(raw).hexdigest().upper() != expected.get("full_sha256")):
        errors.append("whole-source identity mismatch")
    lines = [line + b"\n" for line in raw.split(b"\n")[:-1]]
    clean = [_uncomment(line).strip() for line in lines]
    if len(lines) < RANGES[language][-1][1] + 2:
        return errors + ["source omits the following 7.1.10 begin/label boundary"]
    numbered = [(i + 1, match.group(1).decode(), match.group(2).decode())
                for i, line in enumerate(clean) if (match := NUMBERED_BEGIN.fullmatch(line))]
    slices = expected.get("slices")
    if not isinstance(slices, dict):
        slices = {}
    if set(slices) != {"ega:I." + number for number in NUMBERS}:
        errors.append("numbered slice inventory must contain exactly the seven source units")
    suffix = "-fr" if language == "fr" else ""
    for index, (number, env, (start, end)) in enumerate(zip(NUMBERS, ENVIRONMENTS, RANGES[language])):
        unit = "ega:I." + number
        if [entry for entry in numbered if entry[2] == number] != [(start, env, number)]:
            errors.append(unit + ": unique numbered begin differs from independent source boundary")
        following = [entry for entry in numbered if entry[0] > start]
        next_number = NUMBERS[index + 1] if index + 1 < len(NUMBERS) else "7.1.10"
        if not following or following[0][0] != end + 1 or following[0][2] != next_number:
            errors.append(unit + ": source-order span must run through the next numbered begin")
        try:
            actual = verify_numbered_span(raw, start, end, "I." + number + suffix)
        except ValueError as exc:
            errors.append(unit + ": " + str(exc))
            continue
        if slices.get(unit) != actual:
            errors.append(unit + ": complete source-order span identity mismatch")
        required, final = UNIT_WITNESSES[language][index]
        body = _text(lines[actual["label_line"]:actual["closing_line"] - 1])
        if required.encode() not in body or not body.endswith(final.encode()):
            errors.append(unit + ": final statement semantic witness missing")
    sentinel = RANGES[language][-1][1] + 1
    if (clean[sentinel - 1] != b"\\begin{env}[7.1.10]" or
            clean[sentinel] != ("\\label{I.7.1.10" + suffix + "}").encode()):
        errors.append("following 7.1.10 begin/label boundary mismatch")
    combined = raw_span(lines, RANGES[language][0][0], RANGES[language][-1][1])
    if expected.get("combined") != combined:
        errors.append("complete combined source-order span identity mismatch")
    owned = expected.get("owned_parts")
    if not isinstance(owned, dict):
        owned = {}
    if set(owned) != set(OWNED_KEYS):
        errors.append("owned-parts inventory must preserve the four independent semantic owners")
    for key, (start, end), witnesses in zip(OWNED_KEYS, OWNED_RANGES[language], OWNED_WITNESSES[language]):
        if owned.get(key) != raw_span(lines, start, end):
            errors.append(key + ": complete independently owned proof/tail span identity mismatch")
        first, required, final = witnesses
        block_lines = [line for line in clean[start - 1:end] if line]
        body = _text(lines[start - 1:end])
        if not body.startswith(first.encode()) or any(token.encode() not in body for token in required):
            errors.append(key + ": independent ownership/semantic witness missing")
        if language == "en" and key.endswith(":proof"):
            if not block_lines or block_lines[-1] != b"\\end{proof}":
                errors.append(key + ": complete English proof wrapper missing")
            else:
                block_lines = block_lines[:-1]
        if not block_lines or not _text(block_lines).endswith(final.encode()):
            errors.append(key + ": final proof/tail semantic conclusion missing")
    return errors


def read_source(expected, language, cached=None):
    """One size-bounded read from either a cache or the fixed pinned URL."""
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
    result = {"schema": "ega-i719-raw-source-boundary-replay/v1", "sources": {}, "errors": []}
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
            if not isinstance(expected, dict):
                raise ValueError("source receipt must be an object")
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
