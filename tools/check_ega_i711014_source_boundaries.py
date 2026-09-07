"""Replay raw-LF source ownership for EGA I 7.1.10--7.1.14.

Complete source-order slices, labelled environments, internal constructions,
unwrapped French proofs, English proof wrappers, page markers, and introductory
prose are separate identities. The introduction of 7.1.15 is explicitly bound
but excluded from this checkpoint. Semantic witnesses are independent of the
receipt, so rehashing an incomplete statement or proof cannot validate it.

Read only the two pinned files, once each, with bounded size and timeout.
--french and --english accept cached raw bytes; no source copy is written.
This is a source-boundary check, not a mathematical proof checker.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.request import urlopen

try:
    from tools.ega_raw_source_boundaries import _uncomment, verify_numbered_span
except ModuleNotFoundError:  # Direct execution from tools/.
    from ega_raw_source_boundaries import _uncomment, verify_numbered_span


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "validation/ega-i-7.1.10-7.1.14-semantic-checkpoint-2026-09-07.json"
MAX_SOURCE_BYTES = 1024 * 1024
SOURCE_URLS = {
    "fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/"
          "6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/"
          "94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
}
NUMBERS = ("7.1.10", "7.1.11", "7.1.12", "7.1.13", "7.1.14")
ENVIRONMENTS = ("env", "proposition", "corollary", "corollary", "corollary")
RANGES = {
    "fr": ((192, 205), (206, 220), (221, 231), (232, 243), (244, 258)),
    "en": ((100, 106), (107, 118), (119, 128), (129, 139), (140, 149)),
}
ENVIRONMENT_RANGES = {
    "fr": ((192, 204), (207, 216), (221, 227), (232, 239), (246, 253)),
    "en": ((100, 105), (108, 113), (119, 123), (129, 134), (141, 144)),
}
OWNED_KEYS = ("ega:I.7.1.10:construction", "ega:I.7.1.11:page-marker",
              "ega:I.7.1.11:proof", "ega:I.7.1.12:proof", "ega:I.7.1.13:proof",
              "ega:I.7.1.14:introduction", "ega:I.7.1.14:proof")
OWNED_RANGES = {
    "fr": ((194, 203), (206, 206), (218, 219), (229, 230), (241, 242),
           (244, 244), (255, 257)),
    "en": ((102, 104), (107, 107), (115, 117), (125, 127), (136, 138),
           (140, 140), (146, 148)),
}
NEXT_CONTEXT_RANGES = {
    "fr": {"introduction": (259, 261), "boundary": (263, 264), "combined": (259, 264)},
    "en": {"introduction": (150, 150), "boundary": (151, 152), "combined": (150, 152)},
}
# (required mathematical tokens, final substantive suffix). These are source
# witnesses, not claims that a token search establishes mathematical coverage.
UNIT_WITNESSES = {
    "fr": (
        (("$X$ irréductible", "point générique $x$", "tout ouvert non vide $U$",
          r"$z\in X$ tel que $x\in\overline{\{z\}}$", "morphisme canonique",
          r"\hyperref[I.2.4.1-fr]{2.4.1}", "coïncident dans une partie ouverte non vide",
          "donnent par composition le même morphisme", "à toute application rationnelle"),
         r"$\operatorname{Spec}(\mathscr{O}_x)\to Y$ bien déterminé."),
        (("$S$-préschémas", "$X$ irréductible", "point générique $x$",
          "$Y$ de type fini sur $S$", "Deux $S$-applications rationnelles", "sont identiques.",
          "$S$ localement noethérien", "tout $S$-morphisme", "(et une seule)"),
         "rationnelle (et une seule) de $X$ dans $Y$."),
        (("$S$ localement noethérien", r"\hyperref[I.7.1.11-fr]{7.1.11}",
          "$S$-applications rationnelles", "aux points du $S$-préschéma $Y$", "à valeurs"),
         r"dans le $S$-préschéma $\operatorname{Spec}(\mathscr{O}_x)$."),
        ((r"\hyperref[I.7.1.12-fr]{7.1.12}", "$s$ l'image de $x$ dans $S$",
          "$S$-application rationnelle", "point $y$ de $Y$ au-dessus de $s$",
          r"$\mathscr{O}_s$-homomorphisme local"), r"$\mathscr{O}_y\to\mathscr{O}_x=R(X)$."),
        ((r"\hyperref[I.7.1.12-fr]{7.1.12}", "$S$-applications rationnelles",
          "(pour $Y$ donné)", r"$S$-préschéma $\operatorname{Spec}(\mathscr{O}_x)$",
          "restent les mêmes lorsqu'on remplace $X$ par"),
         r"$\operatorname{Spec}(\mathscr{O}_z)$, pour tout $z\in X$."),
    ),
    "en": (
        (("$X$ is irreducible", "generic point $x$", "every nonempty open subset $U$",
          r"$z\in X$ such that $x\in\overline{\{z\}}$", "canonical morphism",
          r"\sref{I.2.4.1}", "agree on a nonempty open subset of $X$",
          "give, by composition, the same morphism", "to every rational map"),
         r"well-defined morphism $\Spec(\sh{O}_x)\to Y$."),
        (("$S$-preschemes", "$X$ is irreducible", "generic point $x$",
          "$Y$ is of finite type over $S$", "Any two rational $S$-maps", "are then identical.",
          "$S$ to be locally Noetherian", "every $S$-morphism", "exactly one"),
         "exactly one rational $S$-map from $X$ to $Y$."),
        (("$S$ is locally Noetherian", r"\sref{I.7.1.11}", "rational $S$-maps",
          "points of the $S$-prescheme $Y$", "with values"),
         r"in the $S$-prescheme $\Spec(\sh{O}_x)$."),
        ((r"\sref{I.7.1.12}", "$s$ be the image of $x$ in $S$", "rational $S$-map",
          "point $y$ of $Y$ over $s$", r"local $\sh{O}_s$-homomorphism"),
         r"$\sh{O}_y\to\sh{O}_x=R(X)$."),
        ((r"\sref{I.7.1.12}", "rational $S$-maps", "(for any given $Y$)",
          r"$S$-prescheme $\Spec(\sh{O}_x)$", "remain the same whenever $X$ is replaced by"),
         r"$\Spec(\sh{O}_z)$, for any $z\in X$."),
    ),
}
# (initial anchor, required tokens, final substantive suffix). The English
# proof wrapper must surround all its content, not just have one end marker.
OWNED_WITNESSES = {
    "fr": (
        ("Supposons de nouveau", UNIT_WITNESSES["fr"][0][0], UNIT_WITNESSES["fr"][0][1]),
        (r"\oldpage[I]{158}", (), r"\oldpage[I]{158}"),
        ("Compte tenu de", ("tout ouvert non vide de $X$ est partout dense",),
         r"résulte aussitôt de (\hyperref[I.6.5.1-fr]{6.5.1})."),
        ("Cela n'est autre que", (r"\hyperref[I.7.1.11-fr]{7.1.11}", "terminologie"),
         r"introduite dans (\hyperref[I.3.4.1-fr]{3.4.1})."),
        ("Cela résulte de", (r"\hyperref[I.7.1.11-fr]{7.1.11}",),
         r"(\hyperref[I.2.4.4-fr]{2.4.4})."),
        ("En particulier~:", (), "En particulier~:"),
        ("En effet,", (r"$z\in\overline{\{x\}}$", "$x$ est le point générique",
          r"$Z=\operatorname{Spec}(\mathscr{O}_z)$"), r"$\mathscr{O}_{X,x}=\mathscr{O}_{Z,x}$."),
    ),
    "en": (
        ("Suppose again", UNIT_WITNESSES["en"][0][0], UNIT_WITNESSES["en"][0][1]),
        (r"\oldpage[I]{158}", (), r"\oldpage[I]{158}"),
        ("Taking into account", ("every nonempty open subset of $X$ is dense in $X$",),
         r"this follows from \sref{I.6.5.1}."),
        ("This is nothing but", (r"\sref{I.7.1.11}", "terminology"),
         r"introduced in \sref{I.3.4.1}."),
        ("This follows from", (r"\sref{I.7.1.11}",), r"and \sref{I.2.4.4}."),
        ("In particular:", (), "In particular:"),
        ("Since", (r"$z\in\overline{\{x\}}$", "$x$ is the generic point",
          r"$Z=\Spec(\sh{O}_z)$"), r"$\sh{O}_{X,x}=\sh{O}_{Z,x}$."),
    ),
}
NEXT_WITNESSES = {
    "fr": ("Lorsque $X$ est intègre", (r"$R(X)=\mathscr{O}_x=k(x)$ est un corps",
           r"\hyperref[I.7.1.5-fr]{7.1.5}", "les corollaires précédents se spécialisent"), "alors en~:"),
    "en": ("When $X$ is integral", (r"$R(X)=\sh{O}_x=\kres(x)$ is a field",
           r"\sref{I.7.1.5}", "the preceding corollaries"), "then specialize to the following:"),
}
NUMBERED_BEGIN = re.compile(rb"\\begin\{([A-Za-z*]+)\}\[([0-9.]+)\]")


def raw_lines(raw):
    """Physical LF only: form feeds and Unicode separators are not new lines."""
    if not isinstance(raw, bytes) or b"\r" in raw or not raw.endswith(b"\n"):
        raise ValueError("source must be exact LF-terminated bytes")
    return [line + b"\n" for line in raw.split(b"\n")[:-1]]


def raw_span(lines, start, end):
    """Exact identity of an inclusive physical-LF interval, including final LF."""
    if (type(start) is not int or type(end) is not int or not 1 <= start <= end <= len(lines)):
        raise ValueError("invalid physical LF line interval")
    block = b"".join(lines[start - 1:end])
    offset = sum(map(len, lines[:start - 1]))
    return {"lf_line_start": start, "lf_line_end": end, "bytes": len(block),
            "sha256": hashlib.sha256(block).hexdigest().upper(),
            "byte_offset_start": offset, "byte_offset_end_exclusive": offset + len(block)}


def _text(lines):
    return b" ".join(b" ".join(_uncomment(line).strip() for line in lines).split())


def source_metadata(raw, language):
    """Build receipt identities; this helper alone does not verify semantics."""
    lines = raw_lines(raw)
    suffix = "-fr" if language == "fr" else ""
    return {
        "url": SOURCE_URLS[language], "full_bytes": len(raw),
        "full_sha256": hashlib.sha256(raw).hexdigest().upper(),
        "slices": {"ega:I." + number: raw_span(lines, start, end)
                   for number, (start, end) in zip(NUMBERS, RANGES[language])},
        "numbered_environments": {"ega:I." + number: verify_numbered_span(
            raw, start, end, "I." + number + suffix)
            for number, (start, end) in zip(NUMBERS, ENVIRONMENT_RANGES[language])},
        "combined": raw_span(lines, RANGES[language][0][0], RANGES[language][-1][1]),
        "owned_parts": {key: raw_span(lines, start, end)
                        for key, (start, end) in zip(OWNED_KEYS, OWNED_RANGES[language])},
        "next_excluded_context": {"source_unit": "ega:I.7.1.15", **{
            key: raw_span(lines, start, end)
            for key, (start, end) in NEXT_CONTEXT_RANGES[language].items()}},
    }


def verify_source(raw, language, expected):
    """Independently check fixed boundaries and semantics before trusting hashes."""
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
        return errors + ["source omits the following 7.1.15 introduction or begin/label boundary"]
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
        start, end = interval
        env_start, env_end = env_interval
        if [entry for entry in numbered if entry[2] == number] != [(env_start, env, number)]:
            errors.append(unit + ": unique numbered begin differs from independent source boundary")
        following = [entry for entry in numbered if entry[0] > env_start]
        following_expected = ((ENVIRONMENT_RANGES[language][index + 1][0],
                               ENVIRONMENTS[index + 1], NUMBERS[index + 1])
                              if index + 1 < len(NUMBERS) else
                              (NEXT_CONTEXT_RANGES[language]["boundary"][0], "corollary", "7.1.15"))
        if not following or following[0] != following_expected:
            errors.append(unit + ": next numbered begin violates complete source order")
        if inventories["slices"].get(unit) != raw_span(lines, start, end):
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

    for key, (start, end), (initial, required, final) in zip(
            OWNED_KEYS, OWNED_RANGES[language], OWNED_WITNESSES[language]):
        if inventories["owned_parts"].get(key) != raw_span(lines, start, end):
            errors.append(key + ": complete independently owned span identity mismatch")
        body_lines = [line for line in clean[start - 1:end] if line]
        if language == "en" and key.endswith(":proof"):
            if (len(body_lines) < 3 or body_lines[0] != b"\\begin{proof}"
                    or body_lines[-1] != b"\\end{proof}"
                    or any(re.search(rb"\\(?:begin|end)\{proof\}", line)
                           for line in body_lines[1:-1])):
                errors.append(key + ": complete English proof wrapper missing or duplicated")
            body_lines = body_lines[1:-1]
        body = _text(body_lines)
        if not body.startswith(initial.encode()) or any(token.encode() not in body for token in required):
            errors.append(key + ": independent ownership/semantic witness missing")
        if not body.endswith(final.encode()):
            errors.append(key + ": final proof/construction/intro semantic conclusion missing")

    # Everything in the tranche belongs to a labelled environment or an
    # explicitly recorded prose/page-marker owner; intervening bytes are blank.
    covered = set()
    for start, end in (*ENVIRONMENT_RANGES[language], *OWNED_RANGES[language]):
        covered.update(range(start, end + 1))
    for n in range(RANGES[language][0][0], RANGES[language][-1][1] + 1):
        if n not in covered and clean[n - 1]:
            errors.append("unowned substantive source line: " + str(n))
    combined = raw_span(lines, RANGES[language][0][0], RANGES[language][-1][1])
    if expected.get("combined") != combined:
        errors.append("complete combined source-order span identity mismatch")

    next_parts = {key: raw_span(lines, *interval)
                  for key, interval in NEXT_CONTEXT_RANGES[language].items()}
    if expected.get("next_excluded_context") != {"source_unit": "ega:I.7.1.15", **next_parts}:
        errors.append("next excluded 7.1.15 context must retain its complete introduction and boundary")
    intro_start, intro_end = NEXT_CONTEXT_RANGES[language]["introduction"]
    next_start, next_label = NEXT_CONTEXT_RANGES[language]["boundary"]
    initial, required, final = NEXT_WITNESSES[language]
    next_intro = _text(lines[intro_start - 1:intro_end])
    if (not next_intro.startswith(initial.encode()) or not next_intro.endswith(final.encode())
            or any(token.encode() not in next_intro for token in required)):
        errors.append("next excluded 7.1.15 introduction semantic witness missing")
    if (intro_start != RANGES[language][-1][1] + 1
            or any(clean[intro_end:next_start - 1])
            or clean[next_start - 1] != b"\\begin{corollary}[7.1.15]"
            or clean[next_label - 1] != ("\\label{I.7.1.15" + suffix + "}").encode()
            or [entry for entry in numbered if entry[2] == "7.1.15"] != [(next_start, "corollary", "7.1.15")]):
        errors.append("following 7.1.15 source-order begin/label boundary mismatch")
    return errors


def read_source(expected, language, cached=None):
    """One size-bounded read from either a cache or the immutable pinned URL."""
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
    result = {"schema": "ega-i711014-raw-source-boundary-replay/v1", "sources": {}, "errors": []}
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
