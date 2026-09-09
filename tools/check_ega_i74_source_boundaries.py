"""Replay independently pinned raw-LF sources for EGA I 7.4.1--7.4.7.

The French and English Chapter I assertions are diplomatic transcriptions.
Err_III 12 is a distinct source object INSIDE source/ega3/ega3-7-fr.tex,
not a fictitious separately named errata file. Its replacement heading, full
replacement and prose inference are owned; Err_III 13 is excluded boundary
evidence. There is no separately wrapped proof of Err_III 12. The List 2 heading
is contextual evidence only, not ownership of the intervening errata.

Pins were independently transcribed from SOURCE_PREPARATION_20260908 and a
bounded retrieval of the exact French Chapter III container. Original printed
page visual evidence belongs to PRINT_AND_ERRATA_BINDING_20260908; this checker
does not claim a new visual reading or establish mathematical admission.

One bounded read per source per replay; 30-second timeout; no retries, no writes.
Tests use owned literal excerpts with clearly synthetic surrounding bytes,
never copies of complete sources and never self-generated whole-source pins.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.request import urlopen

try:
    from tools.ega_raw_source_boundaries import _uncomment
except ModuleNotFoundError:
    from ega_raw_source_boundaries import _uncomment


ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "validation/ega-i-7.4.1-7.4.7-semantic-checkpoint-2026-09-08.json"
MAX_SOURCE_BYTES = 1024 * 1024
LANGUAGES = ("fr", "en", "errata_fr")
SOURCE_URLS = {
    "fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
    "errata_fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega3/ega3-7-fr.tex",
}
SOURCE_IDENTITIES = {
    "fr": (38226, "73581030E142AD91D51F07A6DE7648101ECA92C7542EA52A2575F098F171F522", 786),
    "en": (35788, "B36636DA91ADA9B74A7F2B4BF1C18E4576D35B363947D06EA475BCBA2918ADBC", 466),
    "errata_fr": (172424, "20A61BA348909E4309A3CDA89FD6DDAF8C0FC5BA346FD44232458CDFEA2A2972", 4479),
}
# Inclusive physical LF lines, bytes, SHA256, first byte, exclusive last byte.
# Overlapping subspans do not create additional source owners.
_SPECS = {
    "fr": {
        "owned": (672, 786, 5011, "D03397BDE8F9E84049541D6655294BC8522D29EE09CCA0288A3F022A5A187800", 33215, 38226),
        "heading": (672, 674, 90, "12CFF65F2FA395AFDD547F584045B8225866AFBEE72D6A44BE1731D45B8E8B43", 33215, 33305),
        "ega:I.7.4.1": (675, 698, 1064, "831663FA9EABEDA38E120BC4F847FC490B56EDA6124D8AA5EDA2E3FF04F4476A", 33305, 34369),
        "ega:I.7.4.2": (699, 712, 680, "319D78E1A4376D49B797E72B28F64D5A9BD98C3844DCCD685A5D4E5D2941617F", 34369, 35049),
        "ega:I.7.4.3": (713, 720, 311, "8A31C8975102C28CAD2A51212E0118138D73ADD0B852B6C540F4AD71CB7AE4A5", 35049, 35360),
        "ega:I.7.4.4": (721, 736, 739, "538F1DF9ECDF1D8298460442AD0214BD8C0EBF4095F62461B51CA5DF021B8FF5", 35360, 36099),
        "ega:I.7.4.5": (737, 760, 945, "C84F0B23AF4F39330853E91C6E85F695CF00186A04305F3A3A9CA2704375DB9D", 36099, 37044),
        "ega:I.7.4.6": (761, 777, 774, "3D5DA9528906BE795A768A670798C257E06D098667BAA4B420B5B7DE4BAE73E4", 37044, 37818),
        "ega:I.7.4.7": (778, 786, 408, "89C8E6296395C5A3684B0E7C14D3A1099D3AD3837596B5B11FABDD10249530F9", 37818, 38226),
        "rank-tail": (707, 711, 333, "70CB18EE26722A9CBCD0A93454EC305126507EF663FF184526C4F77EB6760067", 34715, 35048),
        "744-proof": (730, 735, 389, "7B93B52EB51B794C8AA1151F9CA068B0F05644AA4489A0B583A78FF14EE8FCC8", 35709, 36098),
        "745-page-marker": (744, 744, 17, "B184127F51A96D26CFDB884839EE4383A02E81A7ACD2A58623BA91B355BC58D3", 36383, 36400),
        "745-proof": (745, 759, 643, "F886FD4B539E5FFA24E662D986C22A71DC138EA0F6B297574F5CDBE05AAFB3D7", 36400, 37043),
        "746-proof": (770, 776, 408, "BB8004D081DB9B42B6AE8976318BB309017E7F8C50B16CD4E69F128E665F6C62", 37409, 37817),
    },
    "en": {
        "owned": (403, 466, 4382, "78FB59B32F1A355403892294271E94B73DC8FC36E3B4AF684CA8F529B68B1FB5", 31406, 35788),
        "heading": (403, 406, 94, "2E78E310949D0C6D8DCEDF183F7801000C34B60F5EB3A9B40CEA4E4CEDE2FD9B", 31406, 31500),
        "ega:I.7.4.1": (407, 416, 866, "EB9A9AB39E2568E6C349A23BEC7F14335266390C334EACFC66DEF9045FE511BF", 31500, 32366),
        "ega:I.7.4.2": (417, 423, 592, "F8A95A3E9E3E3D081F3785AD0AFC789CAD7211984FB2020DF37DE31695D42AAA", 32366, 32958),
        "ega:I.7.4.3": (424, 428, 277, "33D81D2ECBB163BD50251DCB05C25ED3D9CDBCBB6F538F30E4EFA853546D94A0", 32958, 33235),
        "ega:I.7.4.4": (429, 439, 703, "E9452263EABC2235F54ECAA218F660EFB50AE698C53BC5F6843DFD623B8EFB21", 33235, 33938),
        "ega:I.7.4.5": (440, 452, 816, "5557B8B00EBEEA54156BDBECBD2FCE7AAED9570A23F1B7B16A5977E2CC02B9E5", 33938, 34754),
        "ega:I.7.4.6": (453, 462, 655, "807537DB45068999107A826B08A85567B45C71B0A384CBD79FB98E0182A89D8B", 34754, 35409),
        "ega:I.7.4.7": (463, 466, 379, "4929AE4AEF2C5D506FF8F354A692C8DAA5C363EA1423E94EC58A05B3815C61D0", 35409, 35788),
        "rank-tail": (422, 423, 294, "1ABFCACCED84423B8653DAE1986E25751999BF0893E1CF19B8715880A586EDAD", 32664, 32958),
        "744-proof": (435, 438, 369, "F092210D4AE6993B33F8FB8A0B0C1573D16042B66DE2E943E479BD4EBBE82C22", 33568, 33937),
        "745-page-marker": (446, 446, 17, "B184127F51A96D26CFDB884839EE4383A02E81A7ACD2A58623BA91B355BC58D3", 34193, 34210),
        "745-proof": (447, 451, 543, "5144187F832E130146AF69F3E936263727960C6FF7B023F72A9E45FD73E6AA61", 34210, 34753),
        "746-proof": (459, 461, 323, "CE474CBCC0DD9A9EA7B7246461E5A88EF514ED40ABDBDC0A7112B56D51D5EDB9", 35085, 35408),
    },
    "errata_fr": {
        "list_heading": (3981, 3988, 129, "3DC3FD36E9DB469AF5AEAEBBFE2872AEDD6694F2893A11BDA94697C3609C14FB", 147450, 147579),
        "owned": (4268, 4276, 588, "496B7992D21322769E3FEDB4F767EBC5D405ADFA593376C26688B3D45F7DB56D", 160179, 160767),
        "heading": (4268, 4268, 76, "26441C9DC96F103C89D5302AD568EF9E542975B2B2DC819FF4CC89F9A13C4F7F", 160179, 160255),
        "replacement_body": (4269, 4275, 511, "9CD0A938116A417E359FE1BECA508816F9B5849C74CF32ED76C145C3F3E4C203", 160255, 160766),
        "inference": (4271, 4275, 354, "E86F6B5777DFCBA09544AF4ADAA169A6FB94983DB49F705B8F20AAECF15BB7D5", 160412, 160766),
        "excluded_next": (4277, 4277, 74, "FB40F2B8AA382A6AF9DFF7676F75F4D1D67221B0F8C28CAB7DCBAC80E2AFFFBA", 160767, 160841),
    },
}
WRAPPERS = {
    "fr": (
        (675, "\\begin{env}"),
        (697, "\\end{env}"),
        (699, "\\begin{proposition}"),
        (705, "\\end{proposition}"),
        (713, "\\begin{corollary}"),
        (719, "\\end{corollary}"),
        (721, "\\begin{corollary}"),
        (728, "\\end{corollary}"),
        (737, "\\begin{proposition}"),
        (742, "\\end{proposition}"),
        (745, "\\begin{proof}"),
        (759, "\\end{proof}"),
        (761, "\\begin{proposition}"),
        (768, "\\end{proposition}"),
        (778, "\\begin{env}"),
        (786, "\\end{env}"),
    ),
    "en": (
        (407, "\\begin{env}"),
        (415, "\\end{env}"),
        (417, "\\begin{proposition}"),
        (420, "\\end{proposition}"),
        (424, "\\begin{corollary}"),
        (427, "\\end{corollary}"),
        (429, "\\begin{corollary}"),
        (433, "\\end{corollary}"),
        (435, "\\begin{proof}"),
        (438, "\\end{proof}"),
        (440, "\\begin{proposition}"),
        (444, "\\end{proposition}"),
        (447, "\\begin{proof}"),
        (451, "\\end{proof}"),
        (453, "\\begin{proposition}"),
        (457, "\\end{proposition}"),
        (459, "\\begin{proof}"),
        (461, "\\end{proof}"),
        (463, "\\begin{env}"),
        (466, "\\end{env}"),
    ),
    "errata_fr": (
        (3983, "\\begin{center}"),
        (3988, "\\end{center}"),
    ),
}
UNIQUE_MARKERS = {
    "fr": (
        (673, "\\label{subsection:I.7.4-fr}"),
        (675, "\\begin{env}[7.4.1]"),
        (676, "\\label{I.7.4.1-fr}"),
        (699, "\\begin{proposition}[7.4.2]"),
        (700, "\\label{I.7.4.2-fr}"),
        (713, "\\begin{corollary}[7.4.3]"),
        (714, "\\label{I.7.4.3-fr}"),
        (721, "\\begin{corollary}[7.4.4]"),
        (722, "\\label{I.7.4.4-fr}"),
        (737, "\\begin{proposition}[7.4.5]"),
        (738, "\\label{I.7.4.5-fr}"),
        (744, "\\oldpage[I]{164}"),
        (761, "\\begin{proposition}[7.4.6]"),
        (762, "\\label{I.7.4.6-fr}"),
        (778, "\\begin{env}[7.4.7]"),
        (779, "\\label{I.7.4.7-fr}"),
    ),
    "en": (
        (404, "\\label{subsection:I.7.4}"),
        (405, "\\label{I.7.4}"),
        (407, "\\begin{env}[7.4.1]"),
        (408, "\\label{I.7.4.1}"),
        (417, "\\begin{proposition}[7.4.2]"),
        (418, "\\label{I.7.4.2}"),
        (424, "\\begin{corollary}[7.4.3]"),
        (425, "\\label{I.7.4.3}"),
        (429, "\\begin{corollary}[7.4.4]"),
        (430, "\\label{I.7.4.4}"),
        (440, "\\begin{proposition}[7.4.5]"),
        (441, "\\label{I.7.4.5}"),
        (446, "\\oldpage[I]{164}"),
        (453, "\\begin{proposition}[7.4.6]"),
        (454, "\\label{I.7.4.6}"),
        (463, "\\begin{env}[7.4.7]"),
        (464, "\\label{I.7.4.7}"),
    ),
    "errata_fr": (
        (3981, "\\oldpage[III]{217}"),
        (3982, "\\section*{ERRATA ET ADDENDA}"),
        (4268, "\\noindent\\textbf{$(\\mathbf{Err}_{\\mathrm{III}},\\,12)$}"),
        (4277, "\\noindent\\textbf{$(\\mathbf{Err}_{\\mathrm{III}},\\,13)$}"),
    ),
}

PROOF_FORMS = {
    "fr": {"744": "unwrapped", "745": "wrapped", "746": "unwrapped"},
    "en": {"744": "wrapped", "745": "wrapped", "746": "wrapped"},
    "errata_fr": {"replacement": "inference_in_prose_no_separate_proof"},
}
ENVIRONMENT_TOKEN = re.compile(rb"\\(?:begin|end)\{[^{}\r\n]+\}")


def _language(language):
    if type(language) is not str or language not in LANGUAGES:
        raise ValueError("unsupported source version")


def _span_spec(spec):
    return dict(zip(("lf_line_start", "lf_line_end", "bytes", "sha256",
                     "byte_offset_start", "byte_offset_end_exclusive"), spec))


def expected_contract(language):
    """Fresh independently pinned contract; no receipt access or other I/O."""
    _language(language)
    size, digest, count = SOURCE_IDENTITIES[language]
    return {"url": SOURCE_URLS[language], "full_bytes": size, "full_sha256": digest,
            "full_lf_lines": count, "proof_forms": dict(PROOF_FORMS[language]),
            "end_boundary": "excluded_next" if language == "errata_fr" else "EOF",
            "spans": {key: _span_spec(spec) for key, spec in _SPECS[language].items()}}


def _compare(actual, expected, path):
    """Strict recursive equality including types and complete inventories."""
    if type(actual) is not type(expected):
        return [path + ": malformed type"]
    if isinstance(expected, dict):
        errors = [] if set(actual) == set(expected) else [path + ": exact inventory required"]
        for key in expected:
            if key in actual:
                errors.extend(_compare(actual[key], expected[key], path + "." + key))
        return errors
    return [] if actual == expected else [path + ": pinned identity/boundary mismatch"]


def validate_artifact(receipt, language):
    """Reject self-rehashed, incomplete or version-swapped receipt metadata."""
    try:
        contract = expected_contract(language)
    except ValueError as exc:
        return [str(exc)]
    return _compare(receipt, contract, language)


def raw_lines(raw):
    if (type(raw) is not bytes or len(raw) > MAX_SOURCE_BYTES or b"\r" in raw
            or not raw.endswith(b"\n") or raw.startswith(b"\xef\xbb\xbf")):
        raise ValueError("source must be bounded exact LF-terminated bytes without BOM")
    try:
        raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ValueError("source must be valid exact UTF-8") from exc
    return [line + b"\n" for line in raw.split(b"\n")[:-1]]


def raw_span(lines, start, end):
    """Inclusive one-based physical-LF interval retaining terminal LF."""
    if type(start) is not int or type(end) is not int or not 1 <= start <= end <= len(lines):
        raise ValueError("invalid physical LF line interval")
    block = b"".join(lines[start - 1:end])
    offset = sum(map(len, lines[:start - 1]))
    return {"lf_line_start": start, "lf_line_end": end, "bytes": len(block),
            "sha256": hashlib.sha256(block).hexdigest().upper(), "byte_offset_start": offset,
            "byte_offset_end_exclusive": offset + len(block)}


def artifact(data, language):
    """Extract actual metadata; extraction alone certifies nothing."""
    _language(language)
    lines = raw_lines(data)
    return {"url": SOURCE_URLS[language], "full_bytes": len(data),
            "full_sha256": hashlib.sha256(data).hexdigest().upper(), "full_lf_lines": len(lines),
            "proof_forms": dict(PROOF_FORMS[language]),
            "end_boundary": "excluded_next" if language == "errata_fr" else "EOF",
            "spans": {key: raw_span(lines, *spec[:2]) for key, spec in _SPECS[language].items()}}


source_metadata = artifact


def verify_structure(data, language):
    """Verify exact scoped literals and wrappers, not the unowned mathematics.

verify_source must additionally certify the whole-file identity and offsets.
Chapter I ownership reaches exact EOF. Chapter III retains Err_III 13 as the
excluded next boundary, and its List 2 heading as disjoint contextual evidence.
"""
    try:
        _language(language)
        lines = raw_lines(data)
    except ValueError as exc:
        return [str(exc)]
    specs = _SPECS[language]
    last = max(spec[1] for spec in specs.values())
    if len(lines) < last:
        return ["source omits complete owned tail or excluded next boundary"]
    errors = []
    if language != "errata_fr" and len(lines) != specs["owned"][1]:
        errors.append("EOF boundary differs: 7.4.7 must end at exact Chapter I source EOF")
    for key, spec in specs.items():
        actual = raw_span(lines, *spec[:2])
        if actual["bytes"] != spec[2] or actual["sha256"] != spec[3]:
            errors.append(key + ": exact literal source span mismatch")
    scoped = sorted({n for spec in specs.values() for n in range(spec[0], spec[1] + 1)})
    clean = [_uncomment(line) for line in lines]
    wrappers = [(n, match.group().decode("utf-8")) for n in scoped
                for match in ENVIRONMENT_TOKEN.finditer(clean[n - 1])]
    if wrappers != list(WRAPPERS[language]):
        errors.append("wrapper inventory differs: nesting, omission, duplication or wrong proof form")
    for position, marker in UNIQUE_MARKERS[language]:
        token = marker.encode("utf-8")
        occurrences = [n + 1 for n, line in enumerate(clean) for _ in range(line.count(token))]
        if occurrences != [position]:
            errors.append("globally unique source marker differs: " + marker)
    return errors


def verify_source(data, language, expected=None):
    """Return independently pinned whole identity and boundary failures."""
    try:
        contract = expected_contract(language)
    except ValueError as exc:
        return [str(exc)]
    errors = validate_artifact(contract if expected is None else expected, language)
    errors.extend(verify_structure(data, language))
    try:
        errors.extend(_compare(artifact(data, language), contract, language + ".source"))
    except ValueError as exc:
        errors.append("raw source extraction failed: " + str(exc))
    return errors


def fetch_source(language, cached=None):
    """One bounded transport read; verify_source must certify returned bytes."""
    _language(language)
    size = SOURCE_IDENTITIES[language][0]
    if type(size) is not int or not 0 < size < MAX_SOURCE_BYTES:
        raise ValueError("invalid bounded pinned source size")
    if cached is not None:
        with cached.open("rb") as handle:
            data = handle.read(size + 1)
    else:
        with urlopen(SOURCE_URLS[language], timeout=30) as response:
            data = response.read(size + 1)
    if type(data) is not bytes or len(data) != size:
        raise ValueError("bounded source read returned a short or oversized source")
    return data


def read_source(expected, language, cached=None):
    """Malformed or version-swapped contracts cause no source I/O."""
    problems = validate_artifact(expected, language)
    if problems:
        raise ValueError("; ".join(problems))
    return fetch_source(language, cached)


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key: " + key)
        result[key] = value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path, default=RECEIPT)
    parser.add_argument("--french", type=Path)
    parser.add_argument("--english", type=Path)
    parser.add_argument("--errata-french", type=Path)
    args = parser.parse_args(argv)
    result = {"schema": "ega-i74-raw-source-boundary-replay/v1",
              "scope": "three-source mechanical ownership and literal identity; not semantic admission",
              "sources": {}, "errors": []}
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
        languages = receipt["languages"]
        if type(languages) is not dict or set(languages) != set(LANGUAGES):
            raise ValueError("languages must contain exactly fr, en and errata_fr")
        # Finish every contract check before the first transport operation.
        for language in LANGUAGES:
            problems = validate_artifact(languages[language], language)
            if problems:
                raise ValueError("; ".join(problems))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result["errors"].append("source receipt read failed: " + str(exc))
        languages = {}
    for language, cached in zip(LANGUAGES, (args.french, args.english, args.errata_french)):
        if language not in languages:
            continue
        try:
            raw = read_source(languages[language], language, cached)
            problems = verify_source(raw, language, languages[language])
            result["sources"][language] = {"bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest().upper(), "status": "FAIL" if problems else "PASS"}
            result["errors"].extend(language + ": " + problem for problem in problems)
        except (OSError, ValueError) as exc:
            result["errors"].append(language + ": bounded source read failed: " + str(exc))
    result["status"] = "FAIL" if result["errors"] else "PASS"
    print(json.dumps(result, indent=2))
    return bool(result["errors"])


if __name__ == "__main__":
    raise SystemExit(main())
