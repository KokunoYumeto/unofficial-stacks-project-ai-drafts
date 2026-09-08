"""Replay physical-LF source ownership for EGA I 7.2.8--7.2.9.

This is mechanical identity/boundary and literal-clause checking, not semantic
adjudication or admission. The nested 7.2.8.1 proof, its page marker, and the
parent's following induced-map prose are separate owners. Historical wording
and the French/English cross-reference discrepancy remain uncorrected.
The following 7.3 heading/label is excluded boundary evidence, not coverage.

Read each pinned URL at most once with a 30-second timeout and a 1 MiB cap,
or use --french/--english cached raw files. Never write sources or receipts.
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
RECEIPT = ROOT / "validation/ega-i-7.2.8-7.2.9-semantic-checkpoint-2026-09-08.json"
MAX_SOURCE_BYTES = 1024 * 1024
SOURCE_URLS = {
    "fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/"
          "6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/"
          "94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
}
NUMBERS = ("7.2.8", "7.2.8.1", "7.2.9")
ENVIRONMENTS = ("env", "lemma", "proposition")
# The parent 7.2.8 complete span intentionally contains its nested lemma.
# These are source ownership identities, not three disjoint byte partitions.
RANGES = {"fr": ((431, 486), (453, 479), (487, 527)),
          "en": ((260, 288), (271, 285), (289, 309))}
ENVIRONMENT_RANGES = {"fr": ((431, 451), (453, 464), (487, 496)),
                      "en": ((260, 269), (271, 276), (289, 295))}
OWNED_KEYS = ("ega:I.7.2.8.1:proof", "ega:I.7.2.8:induced-map",
              "ega:I.7.2.9:proof")
OWNED_RANGES = {"fr": ((466, 478), (480, 485), (498, 526)),
                "en": ((278, 284), (286, 287), (297, 308))}
PROOF_INDICES = (0, 2)
PAGE_KEY = "ega:I.7.2.8.1:page-marker"
PAGE_RANGES = {"fr": (474, 474), "en": (282, 282)}
PAGE_MARKER = r"\oldpage[I]{161}"
ENUM_RANGES = {"fr": (442, 450), "en": (265, 268)}
ENUM_ITEM_MARKERS = {
    "fr": ((443, r"\item[1\textsuperscript{o}]"),
           (448, r"\item[2\textsuperscript{o}]")),
    "en": ((266, r"\item[1st.]"), (267, r"\item[2nd.]")),
}
NEXT_RANGES = {"fr": (528, 529), "en": (310, 311)}
NEXT_NUMBER = "7.3"
NEXT_MARKERS = {
    "fr": ((528, r"\subsection{Faisceau des fonctions rationnelles.}"),
           (529, r"\label{subsection:I.7.3-fr}")),
    "en": ((310, r"\subsection{Sheaf of rational functions}"),
           (311, r"\label{subsection:I.7.3}")),
}

# Independent literal witnesses are intentionally not called semantic proofs.
# They make omission/comment-hiding fail even when damaged fixtures are rehashed.
UNIT_WITNESSES = {
    "fr": (
        (("$X$, $Y$ deux $S$-préschémas", "$X$ étant supposé réduit",
          "$Y$ séparé sur $S$", "$f$ une $S$-application rationnelle",
          r"$\operatorname{Spec}(\mathscr{O}_x)\to X$",
          "pourvu que la trace", "soit dense",
          r"$z\in X$ tels que $x\in\overline{\{z\}}$",
          "$X$ est irréductible (donc intègre)",
          r"le point générique $\xi$ de $X$",
          r"$U\cap\operatorname{Spec}(\mathscr{O}_x)$",
          "$X$ est localement noethérien"), "résulte en effet alors du"),
        (("un préschéma dont l'espace sous-jacent est localement noethérien",
          r"Les composantes irréductibles de $\operatorname{Spec}(\mathscr{O}_x)$",
          "des composantes irréductibles de $X$ contenant $x$",
          r"un ouvert $U\subset X$",
          r"$U\cap\operatorname{Spec}(\mathscr{O}_x)$ soit dense dans $\operatorname{Spec}(\mathscr{O}_x)$",
          "il faut et il suffit",
          "qu'il rencontre les composantes irréductibles de $X$ contenant $x$"),
         "si $U$ est dense dans $X$)."),
        (("$S$ un préschéma localement noethérien", "$X$ un $S$-préschéma réduit",
          "$Y$ un $S$-schéma de type fini",
          "$X$ irréductible ou localement noethérien",
          "$f$ une $S$-application rationnelle",
          "Pour que $f$ soit définie au point $x$", "il faut et il suffit",
          r"$\operatorname{Spec}(\mathscr{O}_x)$", "induite par $f$",
          r"\hyperref[I.7.2.8-fr]{7.2.8}"), "soit un morphisme."),
    ),
    "en": (
        (("$X$ and $Y$ be two $S$-preschemes", "$X$ reduced",
          "$Y$ separated over $S$", "rational $S$-map",
          r"$\Spec(\sh{O}_x)\to X$", "provided that the intersection",
          r"is dense in $\Spec(\sh{O}_x)$",
          r"$z\in X$ such that $x\in\overline{\{z\}}$",
          r"$X$ is \emph{irreducible} (and thus \emph{integral})",
          r"the generic point $\xi$ of $X$",
          r"$U\cap\Spec(\sh{O}_x)$", r"$X$ is \emph{locally Noetherian}"),
         "our claim then follows from:"),
        (("whose underlying space is locally Noetherian",
          r"The irreducible components of $\Spec(\sh{O}_x)$",
          "the irreducible components of $X$ containing $x$",
          r"an open subset $U\subset X$",
          r"$U\cap\Spec(\sh{O}_x)$ is dense in $\Spec(\sh{O}_x)$",
          "necessary and sufficient",
          "a nonempty intersection with the irreducible components of $X$ that contain $x$"),
         r"\emph{(which will be the case whenever $U$ is \emph{dense} in $X$)}."),
        (("$S$ be a locally Noetherian prescheme", "$X$ a reduced $S$-prescheme",
          "$Y$ an $S$-scheme of finite type",
          "$X$ is either irreducible or locally Noetherian",
          "$f$ be a rational $S$-map", "For $f$ to be defined at the point $x$",
          "necessary and sufficient", r"$\Spec(\sh{O}_x)$",
          r"induced by $f$ \sref{I.7.2.8}"), "to be a morphism."),
    ),
}
OWNED_WITNESSES = {
    "fr": (
        ("La seconde assertion résulte évidemment de la première",
         ("il suffit donc de démontrer celle-ci",
          r"$\operatorname{Spec}(\mathscr{O}_x)$ est contenu dans tout ouvert affine",
          "les traces sur $U$ des composantes irréductibles de $X$ contenant $x$",
          r"\hyperref[0.2.1.6-fr]{0, 2.1.6}", "on peut supposer $X$ affine d'anneau $A$",
          "les idéaux premiers de $A_x$ correspondent biunivoquement",
          r"de $A$ contenus dans $\mathfrak{j}_x$",
          r"\hyperref[0.1.2.6-fr]{0, 1.2.6}", "les idéaux premiers minimaux de $A_x$",
          "correspondent aux idéaux premiers minimaux de $A$",
          r"les idéaux premiers minimaux de $A_x$ correspondent aux idéaux premiers minimaux de $A$ contenus dans $\mathfrak{j}_x$"),
         r"(\hyperref[I.1.1.14-fr]{1.1.14})."),
        ("Cela étant, supposons que l'on soit dans l'un des deux cas précités.",
         ("le domaine de définition de la $S$-application rationnelle $f$",
          "désignons par $f'$ l'application rationnelle",
          r"$\operatorname{Spec}(\mathscr{O}_x)$", r"\hyperref[I.2.4.2-fr]{2.4.2}",
          r"$f$ dans $U\cap\operatorname{Spec}(\mathscr{O}_x)$"),
         r"application rationnelle est \emph{induite par $f$}."),
        ("La condition étant évidemment nécessaire",
         (r"$\operatorname{Spec}(\mathscr{O}_x)$ est contenu dans tout ouvert contenant $x$",
          "prouvons qu'elle est suffisante", r"\hyperref[I.6.5.1-fr]{6.5.1}",
          "un voisinage ouvert $U$ de $x$ dans $X$ et un $S$-morphisme $g$",
          "induisant $f'$", "Si $X$ est irréductible", "$U$ est dense dans $X$",
          "le point générique de $X$", "coïncident en ce point",
          "dans un ensemble ouvert non vide de $X$",
          "$f$ et $g$ sont des $S$-applications rationnelles, elles sont identiques",
          "donc $f$ est définie en $x$.",
          "Si maintenant on suppose $X$ localement noethérien",
          "on peut supposer $U$ noethérien", "un nombre fini de composantes irréductibles",
          "les seules rencontrant $U$", "un ouvert plus petit",
          "coïncident dans un ouvert non vide de chacun",
          r"chacun des $X_i$ est contenu dans $\overline U$",
          r"un ouvert dense de $U\cup(X-\overline U)$",
          "égal à $g$ dans $U$ et à $f$",
          "coïncident dans un ouvert dense de $X$",
          "$f$ est une extension de $f_1$",
          r"\hyperref[I.7.2.3-fr]{7.2.3}"), "point $x$."),
    ),
    "en": (
        ("It suffices to show just the first claim",
         ("since the second then follows",
          r"$\Spec(\sh{O}_x)$ is contained in every affine open subset",
          "intersections of $U$ with the irreducible components of $X$ containing $x$",
          r"\sref[0]{0.2.1.6}", "$X$ is affine, given by some ring $A$",
          "the prime ideals of $A_x$ correspond bijectively",
          r"of $A$ that are contained in $\mathfrak{j}_x$ \sref{0.2.1.6}",
          "the minimal prime ideals of $A_x$",
          "the minimal prime ideals of $A$",
          r"the minimal prime ideals of $A_x$ correspond to the minimal prime ideals of $A$ that are contained in $\mathfrak{j}_x$"),
         r"hence the lemma \sref{I.1.1.14}."),
        ("With this in mind, suppose that we are in one of the two cases mentioned",
         (r"\sref{I.7.2.8}", "the domain of definition of the rational $S$-map $f$",
          "denote by $f'$ the rational map", r"$\Spec(\sh{O}_x)$",
          r"\sref{I.2.4.2}", r"$f$ on $U\cap\Spec(\sh{O}_x)$"),
         r"\emph{induced by $f$}."),
        ("The condition clearly being necessary",
         (r"$\Spec(\sh{O}_x)$ is contained in every open subset containing $x$",
          "we show that it is sufficient", r"\sref{I.6.5.1}",
          "an open neighbourhood $U$ of $x$ in $X$, and an $S$-morphism $g$",
          "induces $f'$", "If $X$ is irreducible", "$U$ is dense in $X$",
          "the generic point of $X$", "agree at this point",
          "on a nonempty open subset of $X$",
          "$f$ and $g$ are rational $S$-maps, they are identical",
          "and so $f$ is defined at $x$.",
          "If we now suppose that $X$ is locally Noetherian",
          "we can suppose that $U$ is Noetherian",
          "a finite number of irreducible components",
          "the only ones that have a nonempty intersection with $U$",
          "a smaller open subset", "agree on a nonempty open subset of each",
          r"each of the $X_i$ is contained in $\overline{U}$",
          r"a dense open subset of $U\cup(X\setmin\overline{U})$",
          "equal to $g$ on $U$, and to $f$",
          "agree on a dense open subset of $X$",
          "$f$ is an extension of $f_1$", r"\sref{I.7.2.3}"),
         "defined at the point $x$."),
    ),
}
NUMBERED_BEGIN = re.compile(rb"\\begin\{([A-Za-z*]+)\}\[([0-9.]+)\]")
ENVIRONMENT_TOKEN = re.compile(rb"\\(?:begin|end)\{[A-Za-z*]+\}")
ITEM_TOKEN = re.compile(rb"\\item(?:\[[^\]]*\])?")
SOURCE_KEYS = {"url", "full_bytes", "full_sha256", "slices", "numbered_environments",
               "owned_parts", "page_markers", "combined", "next_excluded_boundary"}


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
    """Build mechanical metadata only; never certify source truth or admission."""
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
    """Return source-identity, independent-ownership and literal-clause failures."""
    if not isinstance(language, str) or language not in RANGES:
        return ["unsupported source language"]
    if not isinstance(expected, dict):
        return ["source receipt must be an object"]
    try:
        lines = raw_lines(raw)
    except ValueError as exc:
        return [str(exc)]
    errors = []
    try:
        _validate_receipt_shape(expected, language)
    except ValueError as exc:
        errors.append(str(exc))
    if (type(expected.get("full_bytes")) is not int or len(raw) != expected.get("full_bytes")
            or hashlib.sha256(raw).hexdigest().upper() != expected.get("full_sha256")):
        errors.append("whole-source identity mismatch")
    if len(lines) < NEXT_RANGES[language][1]:
        return errors + ["source omits the following 7.3 heading/label boundary"]
    clean = [_uncomment(line).strip() for line in lines]
    numbered = [(i + 1, match.group(1).decode(), match.group(2).decode())
                for i, line in enumerate(clean) for match in NUMBERED_BEGIN.finditer(line)]
    units = {"ega:I." + number for number in NUMBERS}
    inventories = {}
    for key, required in (("slices", units), ("numbered_environments", units),
                          ("owned_parts", set(OWNED_KEYS)), ("page_markers", {PAGE_KEY})):
        inventory = expected.get(key)
        inventories[key] = inventory if isinstance(inventory, dict) else {}
        if set(inventories[key]) != required:
            errors.append(key + ": exact inventory of independent source owners required")
    sequence = [(interval[0], env, number) for number, env, interval in zip(
        NUMBERS, ENVIRONMENTS, ENVIRONMENT_RANGES[language])]
    if [entry for entry in numbered if RANGES[language][0][0] <= entry[0] <= NEXT_RANGES[language][1]] != sequence:
        errors.append("numbered source order contains a missing, foreign or moved owner")
    suffix = "-fr" if language == "fr" else ""
    for index, (number, env, interval, env_interval) in enumerate(zip(
            NUMBERS, ENVIRONMENTS, RANGES[language], ENVIRONMENT_RANGES[language])):
        unit = "ega:I." + number
        env_start, env_end = env_interval
        if [entry for entry in numbered if entry[2] == number] != [(env_start, env, number)]:
            errors.append(unit + ": unique numbered begin differs from independent source boundary")
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
            body_lines = clean[actual["label_line"]:actual["closing_line"] - 1]
            wrappers = [(n, m.group()) for n in range(env_start + 2, env_end)
                        for m in ENVIRONMENT_TOKEN.finditer(clean[n - 1])]
            allowed = [(ENUM_RANGES[language][0], b"\\begin{enumerate}"),
                       (ENUM_RANGES[language][1], b"\\end{enumerate}")] if index == 0 else []
            if wrappers != allowed:
                errors.append(unit + ": unexpected or moved nested statement wrapper")
            if index == 0:
                for n, token in ((ENUM_RANGES[language][0], b"\\begin{enumerate}"),
                                 (ENUM_RANGES[language][1], b"\\end{enumerate}")):
                    if clean[n - 1] != token:
                        errors.append(unit + ": enumeration delimiter must occupy its exact LF line")
                items = [(n, m.group()) for n in range(env_start + 2, env_end)
                         for m in ITEM_TOKEN.finditer(clean[n - 1])]
                if items != [(n, token.encode()) for n, token in ENUM_ITEM_MARKERS[language]]:
                    errors.append(unit + ": exact enumeration item inventory differs")
                body_lines = [line for n, line in enumerate(body_lines, start=actual["label_line"] + 1)
                              if n not in ENUM_RANGES[language]]
            body = _text(body_lines)
            required, final = UNIT_WITNESSES[language][index]
            if any(token.encode() not in body for token in required) or not body.endswith(final.encode()):
                errors.append(unit + ": literal statement clause witness missing")
        except ValueError as exc:
            errors.append(unit + ": " + str(exc))
    for index, (key, interval, (initial, required, final)) in enumerate(zip(
            OWNED_KEYS, OWNED_RANGES[language], OWNED_WITNESSES[language])):
        start, end = interval
        if inventories["owned_parts"].get(key) != raw_span(lines, *interval):
            errors.append(key + ": complete independently owned source span identity mismatch")
        body_lines = [line for n, line in enumerate(clean[start - 1:end], start=start)
                      if n != PAGE_RANGES[language][0]]
        if index in PROOF_INDICES and language == "en":
            if (clean[start - 1] != b"\\begin{proof}" or clean[end - 1] != b"\\end{proof}"
                    or not body_lines or body_lines[0] != b"\\begin{proof}"
                    or body_lines[-1] != b"\\end{proof}"
                    or any(ENVIRONMENT_TOKEN.search(line) for line in body_lines[1:-1])):
                errors.append(key + ": complete English proof wrapper missing, moved or duplicated")
            body_lines = body_lines[1:-1]
        elif any(ENVIRONMENT_TOKEN.search(line) for line in body_lines):
            errors.append(key + ": unwrapped source prose has an unexpected wrapper")
        body = _text(body_lines)
        if not body.startswith(initial.encode()) or any(token.encode() not in body for token in required):
            errors.append(key + ": independent source ownership/clause witness missing")
        if not body.endswith(final.encode()):
            errors.append(key + ": final source clause witness missing")
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
        errors.append("next excluded 7.3 boundary must retain only its complete heading/label")
    for n, token in NEXT_MARKERS[language]:
        marker = token.encode()
        if clean[n - 1] != marker or sum(line.count(marker) for line in clean) != 1:
            errors.append("next excluded 7.3 marker must occur exactly once at raw LF " + str(n))
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
    """Validate both language inventories before either source is read."""
    _read_parameters(expected, language)
    if set(expected) != SOURCE_KEYS:
        raise ValueError(language + ": exact source receipt inventory required")
    for key, required in (("slices", {"ega:I." + n for n in NUMBERS}),
                          ("numbered_environments", {"ega:I." + n for n in NUMBERS}),
                          ("owned_parts", set(OWNED_KEYS)), ("page_markers", {PAGE_KEY})):
        inventory = expected.get(key)
        if not isinstance(inventory, dict) or set(inventory) != required:
            raise ValueError(language + ": malformed " + key + " inventory")
        for owner, span in inventory.items():
            extra = ("label", "environment", "begin_line", "label_line", "closing_line") if key == "numbered_environments" else ()
            _validate_span_shape(span, extra)
            if extra:
                index = NUMBERS.index(owner[len("ega:I."):])
                suffix = "-fr" if language == "fr" else ""
                if (span["label"] != "I." + NUMBERS[index] + suffix
                        or span["environment"] != ENVIRONMENTS[index]
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
    result = {"schema": "ega-i729-raw-source-boundary-replay/v1",
              "scope": "mechanical source ownership; not semantic admission",
              "sources": {}, "errors": []}
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
        languages = receipt["languages"]
        if not isinstance(languages, dict) or set(languages) != {"fr", "en"}:
            raise ValueError("languages must contain exactly fr and en")
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
