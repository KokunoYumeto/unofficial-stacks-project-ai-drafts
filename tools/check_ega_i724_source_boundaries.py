"""Bounded raw-LF source replay for EGA I7.2.1--7.2.4, including 7.2.2.1.

Numbered environments, introductions, proofs and the parent consequence have
separate semantic owners. Storage of the consequence after the nested lemma
does not transfer its ownership. Fetch each immutable URL once (30s, <=1MiB)
or read explicit cached files. No source or receipt is written.
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
RECEIPT = ROOT / "validation/ega-i-7.2.1-7.2.4-semantic-checkpoint-2026-09-07.json"
MAX_SOURCE_BYTES = 1024 * 1024
SOURCE_URLS = {
    "fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
}
NUMBERS = ("7.2.1", "7.2.2", "7.2.2.1", "7.2.3", "7.2.4")
ENVIRONMENTS = ("env", "proposition", "lemma", "corollary", "corollary")
RANGES = {"fr": ((290, 302), (303, 315), (316, 349), (350, 362), (363, 377)),
          "en": ((169, 179), (180, 189), (190, 206), (207, 216), (217, 226))}
ENVIRONMENT_RANGES = {"fr": ((293, 301), (304, 310), (316, 323), (350, 357), (363, 370)),
                      "en": ((173, 178), (181, 186), (190, 194), (207, 211), (217, 221))}
OWNED_KEYS = ("ega:I.7.2:heading", "ega:I.7.2:labels", "ega:I.7.2.2:page_marker",
              "ega:I.7.2.2:proof_introduction", "ega:I.7.2.2.1:proof",
              "ega:I.7.2.2:consequence_and_transition", "ega:I.7.2.3:proof", "ega:I.7.2.4:proof")
OWNED_RANGES = {"fr": ((290, 290), (291, 291), (303, 303), (312, 314),
                       (325, 338), (340, 348), (359, 361), (372, 376)),
                "en": ((169, 169), (170, 171), (180, 180), (188, 188),
                       (196, 202), (204, 206), (213, 215), (223, 225))}
NEXT_RANGE = {"fr": (378, 379), "en": (227, 228)}
# Tokens are independent source-clause witnesses; not normalized replacements.
UNIT_WITNESSES = {
    "fr": (
        (("deux préschémas", "une application rationnelle", r"point $x\in X$", "ouvert partout dense", r"morphisme $U\to Y$", "classe d'équivalence", "domaine de définition"), "clair que c'est un ouvert partout dense dans $X$."),
        (("deux $S$-préschémas", "$X$ soit réduit", "$Y$ séparé sur $S$", "$S$-application rationnelle", "$U_0$ son domaine de définition", "$S$-morphisme et un seul"), "appartenant à la classe $f$."),
        ((r"\hyperref[I.7.2.2-fr]{7.2.2}", "deux ouverts partout denses", r"$f_i:U_i\to Y$", "$S$-morphismes", r"$V\subset U_1\cap U_2$", "dense dans $X$"), r"dans $U_1\cap U_2$."),
        ((r"\hyperref[I.7.2.2-fr]{7.2.2}", "ouvert partout dense", "correspondance biunivoque canonique", "$S$-morphismes", "$S$-applications rationnelles"), "en tous les points de $U$."),
        (("$S$ un schéma", "$S$-préschéma réduit", "$Y$ un $S$-schéma", "$S$-morphisme d'un ouvert dense", r"$\mathbf{Z}$-application rationnelle", r"$\overline f$ est un $S$-morphisme"), "$S$-application rationnelle de $X$ dans $Y$ prolongeant $f$)."),
    ),
    "en": (
        (("be preschemes", "a rational map", r"point $x\in X$", "dense open subset", r"morphism $U\to Y$", "equivalence class", "domain of definition"), "it is clear that it is an open dense subset of $X$."),
        (("$S$-preschemes", "$X$ is reduced", "$Y$ is separated over $S$", "rational $S$-map", "domain of definition $U_0$", "exactly one $S$-morphism"), "belonging to the class of $f$."),
        ((r"\sref{I.7.2.2}", "two dense open subsets", r"$f_i:U_i\to Y$", "$S$-morphisms", r"$V\subset U_1\cap U_2$", "dense in $X$"), r"Then $f_1$ and $f_2$ agree on $U_1\cap U_2$."),
        ((r"\sref{I.7.2.2}", "dense open subset", "canonical bijective correspondence", "$S$-morphisms", "rational $S$-maps"), "that are defined at all points of $U$."),
        (("$S$ be a scheme", "reduced $S$-prescheme", "$Y$ an $S$-scheme", "$S$-morphism from a dense open subset", r"rational $\bb{Z}$-map", r"$\overline{f}$ is an $S$-morphism"), "that extends $f$)."),
    ),
}
OWNED_WITNESSES = {
    "fr": (
        (r"\subsection{Domaine de définition d'une application rationnelle.}", (), r"\subsection{Domaine de définition d'une application rationnelle.}"),
        (r"\label{subsection:I.7.2-fr}", (), r"\label{subsection:I.7.2-fr}"),
        (r"\oldpage[I]{159}", (), r"\oldpage[I]{159}"),
        ("Comme pour tout morphisme", (r"$U\to Y$", "classe $f$", r"$U\subset U_0$"), "conséquence du"),
        ("On peut évidemment", ("$X=U_1=U_2$", "est réduit", "le plus petit sous-préschéma fermé", r"\hyperref[I.5.2.2-fr]{5.2.2}", r"$g=(f_1,f_2)_S:X\to Y\times_S Y$", r"$T=\Delta_Y(Y)$", r"$Z=g^{-1}(T)$", r"\hyperref[I.4.4.1-fr]{4.4.1}", r"$h:V\to Y$", r"$g'=(h,h)_S$", r"$g'=\Delta_Y\circ h$", r"$\Delta_Y^{-1}(T)=Y$", r"$g'^{-1}(T)=V$", "$Z=X$", r"$g^{-1}(T)=X$", r"$\Delta_Y\circ f$"), "définition du morphisme diagonal que $f_1=f_2=f$."),
        ("Il est clair", (r"$U_0\to Y$", r"\hyperref[I.7.2.2-fr]{7.2.2}", "ne puisse être prolongé", "contenant strictement $U_0$", "identifier", "non prolongeables", "ouverts partout denses"), r"(\hyperref[I.7.2.2-fr]{7.2.2}) entraîne~:"),
        ("En vertu de", (r"\hyperref[I.7.2.2-fr]{7.2.2}", "$S$-morphisme $f$", "$S$-application rationnelle et une seule"), r"$\overline f$ de $X$ dans $Y$ qui prolonge $f$."),
        ("En effet", (r"$\varphi:X\to S$", r"$\psi:Y\to S$", "$U_0$ le domaine de définition", r"$\psi\circ\overline f=\varphi\circ j$", r"\hyperref[I.7.2.2.1-fr]{7.2.2.1}"), "$S$-morphisme."),
    ),
    "en": (
        (r"\subsection{Domain of definition of a rational map}", (), r"\subsection{Domain of definition of a rational map}"),
        (r"\label{subsection:I.7.2}", (), r"\label{I.7.2}"),
        (r"\oldpage[I]{159}", (), r"\oldpage[I]{159}"),
        ("Since, for every morphism", (r"$U\to Y$", "class of $f$", r"$U\subset U_0$"), "a consequence of the following:"),
        ("We can clearly", ("$X=U_1=U_2$", "is reduced", "smallest closed subprescheme", r"\sref{I.5.2.2}", r"$g=(f_1,f_2)_S:X\to Y\times_S Y$", r"$T=\Delta_Y(Y)$", r"$Z=g^{-1}(T)$", r"\sref{I.4.4.1}", r"$h:V\to Y$", r"$g'=(h,h)_S$", r"$g'=\Delta_Y\circ h$", r"$\Delta_Y^{-1}(T)=Y$", r"$g'^{-1}(T)=V$", "$Z=X$", r"$g^{-1}(T)=X$", r"$\Delta_Y\circ f$"), "that $f_1=f_2=f$."),
        ("It is clear", (r"$U_0\to Y$", r"\sref{I.7.2.2}", "cannot be extended", "strictly contains $U_0$", "identify", "non-extendible", "dense open subsets"), r"With this identification, Proposition~\sref{I.7.2.2} implies:"),
        ("By", (r"\sref{I.7.2.2}", "$S$-morphism $f$", "exactly one rational $S$-map"), "which extends $f$."),
        ("Indeed", (r"$\vphi:X\to S$", r"$\psi:Y\to S$", "$U_0$ the domain of definition", r"$\psi\circ\overline{f}=\vphi\circ j$", r"\sref{I.7.2.2.1}"), "$S$-morphism."),
    ),
}
NUMBERED_BEGIN = re.compile(rb"\\begin\{([A-Za-z*]+)\}\[([0-9.]+)\]")


def raw_lines(raw):
    if not isinstance(raw, bytes) or b"\r" in raw or not raw.endswith(b"\n"):
        raise ValueError("source must be exact LF-terminated bytes")
    return [line + b"\n" for line in raw.split(b"\n")[:-1]]


def raw_span(lines, start, end):
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
    """Mechanical generation does not certify ownership or semantic witnesses."""
    lines = raw_lines(raw)
    suffix = "-fr" if language == "fr" else ""
    return {
        "url": SOURCE_URLS[language], "full_bytes": len(raw),
        "full_sha256": hashlib.sha256(raw).hexdigest().upper(),
        "slices": {"ega:I." + n: raw_span(lines, *r) for n, r in zip(NUMBERS, RANGES[language])},
        "numbered_environments": {"ega:I." + n: verify_numbered_span(raw, *r, "I." + n + suffix)
            for n, r in zip(NUMBERS, ENVIRONMENT_RANGES[language])},
        "combined": raw_span(lines, RANGES[language][0][0], RANGES[language][-1][1]),
        "parent_proposition_package": raw_span(lines, RANGES[language][1][0], RANGES[language][2][1]),
        "owned_parts": {key: raw_span(lines, *r) for key, r in zip(OWNED_KEYS, OWNED_RANGES[language])},
        "next_excluded_context": {"source_unit": "ega:I.7.2.5", **raw_span(lines, *NEXT_RANGE[language])},
    }


def verify_source(raw, language, expected):
    if language not in RANGES or not isinstance(expected, dict):
        return ["unsupported language or malformed source receipt"]
    try:
        lines = raw_lines(raw)
    except ValueError as exc:
        return [str(exc)]
    errors = []
    if expected.get("url") != SOURCE_URLS[language]:
        errors.append("source URL is not pinned")
    if (type(expected.get("full_bytes")) is not int or len(raw) != expected.get("full_bytes")
            or hashlib.sha256(raw).hexdigest().upper() != expected.get("full_sha256")):
        errors.append("whole-source identity mismatch")
    if len(lines) < NEXT_RANGE[language][1]:
        return errors + ["following 7.2.5 boundary omitted"]
    clean = [_uncomment(line).strip() for line in lines]
    numbered = [(i + 1, m.group(1).decode(), m.group(2).decode())
                for i, line in enumerate(clean) if (m := NUMBERED_BEGIN.fullmatch(line))]
    suffix = "-fr" if language == "fr" else ""
    units = {"ega:I." + n for n in NUMBERS}
    inventories = {}
    for key in ("slices", "numbered_environments", "owned_parts"):
        inv = expected.get(key)
        inventories[key] = inv if isinstance(inv, dict) else {}
        if set(inventories[key]) != (set(OWNED_KEYS) if key == "owned_parts" else units):
            errors.append(key + ": exact inventory of independent semantic owners required")
    for i, (n, env, r, er) in enumerate(zip(NUMBERS, ENVIRONMENTS, RANGES[language], ENVIRONMENT_RANGES[language])):
        unit = "ega:I." + n
        start, end = er
        if [x for x in numbered if x[2] == n] != [(start, env, n)]:
            errors.append(unit + ": unique numbered begin boundary mismatch")
        following = [x for x in numbered if x[0] > start]
        nxt = ((ENVIRONMENT_RANGES[language][i + 1][0], ENVIRONMENTS[i + 1], NUMBERS[i + 1])
               if i + 1 < len(NUMBERS) else (NEXT_RANGE[language][0], "corollary", "7.2.5"))
        if not following or following[0] != nxt:
            errors.append(unit + ": next numbered begin violates source order")
        if inventories["slices"].get(unit) != raw_span(lines, *r):
            errors.append(unit + ": complete source-order span identity mismatch")
        try:
            actual = verify_numbered_span(raw, start, end, "I." + n + suffix)
            if (actual["begin_line"], actual["label_line"], actual["closing_line"], actual["environment"]) != (start, start + 1, end, env):
                errors.append(unit + ": complete numbered environment boundary mismatch")
            if inventories["numbered_environments"].get(unit) != actual:
                errors.append(unit + ": numbered environment identity mismatch")
            body = _text(lines[actual["label_line"]:actual["closing_line"] - 1])
            tokens, final = UNIT_WITNESSES[language][i]
            if any(t.encode() not in body for t in tokens) or not body.endswith(final.encode()):
                errors.append(unit + ": statement semantic witness missing")
        except ValueError as exc:
            errors.append(unit + ": " + str(exc))
    for key, r, (initial, tokens, final) in zip(OWNED_KEYS, OWNED_RANGES[language], OWNED_WITNESSES[language]):
        if inventories["owned_parts"].get(key) != raw_span(lines, *r):
            errors.append(key + ": complete independently owned span identity mismatch")
        body_lines = [line for line in clean[r[0] - 1:r[1]] if line]
        if language == "en" and key.endswith(":proof"):
            if (len(body_lines) < 3 or body_lines[0] != b"\\begin{proof}" or body_lines[-1] != b"\\end{proof}"
                    or any(re.search(rb"\\(?:begin|end)\{proof\}", x) for x in body_lines[1:-1])):
                errors.append(key + ": complete English proof wrapper missing or duplicated")
            body_lines = body_lines[1:-1]
        body = _text(body_lines)
        if not body.startswith(initial.encode()) or any(t.encode() not in body for t in tokens):
            errors.append(key + ": independent ownership/semantic witness missing")
        if not body.endswith(final.encode()):
            errors.append(key + ": final proof/intro semantic conclusion missing")
    covered = set()
    for start, end in (*ENVIRONMENT_RANGES[language], *OWNED_RANGES[language]):
        covered.update(range(start, end + 1))
    for n in range(RANGES[language][0][0], RANGES[language][-1][1] + 1):
        if n not in covered and clean[n - 1]:
            errors.append("unowned substantive source line: " + str(n))
    for key, r in (("combined", (RANGES[language][0][0], RANGES[language][-1][1])),
                   ("parent_proposition_package", (RANGES[language][1][0], RANGES[language][2][1]))):
        if expected.get(key) != raw_span(lines, *r):
            errors.append(key + ": complete source-order identity mismatch")
    if expected.get("next_excluded_context") != {"source_unit": "ega:I.7.2.5", **raw_span(lines, *NEXT_RANGE[language])}:
        errors.append("next excluded 7.2.5 begin and label identity mismatch")
    for n, marker in zip(NEXT_RANGE[language],
                         (r"\begin{corollary}[7.2.5]", r"\label{I.7.2.5" + suffix + "}")):
        if clean[n - 1] != marker.encode() or clean.count(marker.encode()) != 1:
            errors.append("next excluded marker must occur exactly once at LF " + str(n))
    return errors


def read_source(expected, language, cached=None):
    if language not in SOURCE_URLS or not isinstance(expected, dict):
        raise ValueError("unsupported source language or malformed receipt")
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
    result = {"schema": "ega-i724-raw-source-boundary-replay/v1", "sources": {}, "errors": []}
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
        languages = receipt["languages"]
        if not isinstance(languages, dict) or set(languages) != {"fr", "en"}:
            raise ValueError("languages must contain exactly fr and en")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result["errors"].append("source receipt read failed: " + str(exc))
        languages = {}
    for lang, cached in (("fr", args.french), ("en", args.english)):
        if lang not in languages:
            continue
        try:
            raw = read_source(languages[lang], lang, cached)
            errors = verify_source(raw, lang, languages[lang])
            result["sources"][lang] = {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest().upper(),
                                       "status": "FAIL" if errors else "PASS"}
            result["errors"].extend(lang + ": " + e for e in errors)
        except (OSError, ValueError) as exc:
            result["errors"].append(lang + ": bounded source read failed: " + str(exc))
    result["status"] = "FAIL" if result["errors"] else "PASS"
    print(json.dumps(result, indent=2))
    return bool(result["errors"])


if __name__ == "__main__":
    raise SystemExit(main())
