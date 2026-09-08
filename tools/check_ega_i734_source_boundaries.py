"""Replay pinned raw-LF ownership for EGA I 7.3.1--7.3.4.

Mechanical source identity, structure and literal-content checks are not a
semantic admission. Complete source-order slices include separator lines, the
7.3.2 page marker/restriction tail, and the complete 7.3.3 proof. Numbered
environments are separate metadata. No printed 7.3.4 proof is asserted; the
7.3.5 begin/label are excluded boundary evidence, not admitted mathematics.

The independent contract below transcribes the verified preparation of
2026-09-08. It is never generated from the receipt being checked. Fetch each
pinned source once, with a 30-second timeout and at most its byte count plus
one byte (also bounded by 1 MiB). This tool writes neither sources nor receipts.
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
RECEIPT = ROOT / "validation/ega-i-7.3.1-7.3.4-semantic-checkpoint-2026-09-08.json"
MAX_SOURCE_BYTES = 1024 * 1024
SOURCE_URLS = {
    "fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/"
          "6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/"
          "94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
}
SOURCE_IDENTITIES = {
    "fr": (38226, "73581030E142AD91D51F07A6DE7648101ECA92C7542EA52A2575F098F171F522"),
    "en": (35788, "B36636DA91ADA9B74A7F2B4BF1C18E4576D35B363947D06EA475BCBA2918ADBC"),
}
NUMBERS = ("7.3.1", "7.3.2", "7.3.3", "7.3.4")
ENVIRONMENTS = ("env", "definition", "proposition", "corollary")
RANGES = {"fr": ((531, 548), (549, 559), (560, 595), (596, 605)),
          "en": ((313, 320), (321, 328), (329, 343), (344, 349))}
ENVIRONMENT_RANGES = {"fr": ((531, 547), (550, 555), (560, 570), (596, 604)),
                      "en": ((313, 319), (322, 325), (329, 333), (344, 348))}
OWNED_KEYS = ("ega:I.7.3.2:restriction-tail", "ega:I.7.3.3:proof")
OWNED_RANGES = {"fr": ((557, 558), (572, 594)), "en": ((327, 327), (335, 342))}
PAGE_KEY = "ega:I.7.3.2:page-marker"
PAGE_RANGES = {"fr": (549, 549), "en": (321, 321)}
PAGE_MARKER = r"\oldpage[I]{162}"
HEADING_RANGES = {"fr": (528, 530), "en": (310, 312)}
HEADING_MARKERS = {
    "fr": (r"\subsection{Faisceau des fonctions rationnelles.}", r"\label{subsection:I.7.3-fr}"),
    "en": (r"\subsection{Sheaf of rational functions}", r"\label{subsection:I.7.3}"),
}
COMBINED_RANGES = {"fr": (528, 605), "en": (310, 349)}
NEXT_RANGES = {"fr": (606, 607), "en": (350, 351)}
NEXT_NUMBER = "7.3.5"
DISCOVERY_UNIT_IDS = ("ega:I.7.3.1", "ega:I.7.3.2", "ega:I.7.3.3",
                      "ega:I.7.3.3:proof", "ega:I.7.3.4")

# Each tuple is (first LF, last LF, bytes, SHA-256, first byte, exclusive last byte).
# These are fixed witnesses, deliberately separate from artifact() extraction.
_SLICE_SPECS = {
    "fr": (
        (531, 548, 933, "BAA33817E0EC9A863999FD592DD5216E81E57D4895F04A7C77673CA2B74A2BD7", 26599, 27532),
        (549, 559, 411, "82D00571840E9CEF2C4FE3C430A8D91725868DC8259E5EC285AB09F0FD5362B9", 27532, 27943),
        (560, 595, 2193, "079808E74F6A1241F09A5B0CD722C940D94EA21BAD40D0C016F47D3354348B22", 27943, 30136),
        (596, 605, 483, "DCE353247F89D7279258E3C1781DA0FD4E68B51D8EDF5745BC07BAB81B246104", 30136, 30619)),
    "en": (
        (313, 320, 802, "83A0E2D7992175E46E0B2E86D904A201DA0647E5D2CB0268D330E25911BBF8CA", 24548, 25350),
        (321, 328, 370, "6A83ED215E35B81961B92FFFC777F9F95D3CC10F5BA480B7D40EA9C90752904D", 25350, 25720),
        (329, 343, 2115, "4699B88EEB4AA891C8844D275E1F65506E1F1A2A96C95A195F3FC52D7F17EB87", 25720, 27835),
        (344, 349, 443, "E2E7DB3AA2DDB7D3C8E6FFA542569EFF7D3AC470BBB3F85A9BD32929D12E25FD", 27835, 28278)),
}
_ENVIRONMENT_SPECS = {
    "fr": (
        (531, 547, 932, "E48838FC413AA50096F10CB543B019E96C3CB50C743B5166A06082999BA8B809", 26599, 27531),
        (550, 555, 248, "0DA73160346C2996A4142684F0DCDC1AF32368E4A3D6D44A447FC0D9139BC40A", 27549, 27797),
        (560, 570, 637, "803A509410D4DBB6138BE38FC365586C7260275CE93842E0C8DF4E445833C589", 27943, 28580),
        (596, 604, 482, "3D41BF98D8A4AA279AE92AE9FA699EEB1B8DED58EF4EF0BF87E8680F1337FA5E", 30136, 30618)),
    "en": (
        (313, 319, 801, "C54464C80C38743CE3884B536B7C440DCE582F0D89BFAC2F89FAD10306BD87AA", 24548, 25349),
        (322, 325, 224, "733E407F18F81815CF2D47D1BE2ECE1DDA5E5CFC6CF8497219410E9FF7AA4E54", 25367, 25591),
        (329, 333, 627, "8F1BDB5AC0A42828404B05E7F127DC0969297141BAE8B779713DB070E5F1297E", 25720, 26347),
        (344, 348, 442, "31197B7AAEFC2B9F87404142925176AA3DA58E6A97365A98EF905E9FECC8EB57", 27835, 28277)),
}
_OWNED_SPECS = {
    "fr": (
        (557, 558, 144, "8CDB2198EC81CFB0BB13694145C044589B98F5BF8647D415A4E87AF6092D23D4", 27798, 27942),
        (572, 594, 1554, "7E50729D9AF70BC3596D03D9E556CDFA788F4AFBC978051AF3F2D7F8A143484A", 28581, 30135)),
    "en": (
        (327, 327, 127, "E5B4410121585EAF2E12E05D06CD170D2A6D9DE44AF99DB9BCA69F7CF7EC2E07", 25592, 25719),
        (335, 342, 1486, "09F2D6FA737CDDB8F5A702C29B9B0A2E41583F8D7455086D63A8C87ECB2BE88C", 26348, 27834)),
}
_PAGE_SPECS = {
    "fr": (549, 549, 17, "319E29D3E0D7C55979CA9164C0CDE16CE6884D2861E2E1A6953973AF5042D95C", 27532, 27549),
    "en": (321, 321, 17, "319E29D3E0D7C55979CA9164C0CDE16CE6884D2861E2E1A6953973AF5042D95C", 25350, 25367),
}
_HEADING_SPECS = {
    "fr": (528, 530, 79, "930B7EDA64780C61156BE8A61A0168BBBC4229391D9A3A91B88AC28DF6A7F422", 26520, 26599),
    "en": (310, 312, 67, "4C92355CE490AB0C75A15161667B1AF8BDB09D5E1AA1094ADBDF4BDBF74A0005", 24481, 24548),
}
_COMBINED_SPECS = {
    "fr": (528, 605, 4099, "1EDC404D41146486D7095EEBE70DC298A2B63C1351292A4B625848AB80A4D20B", 26520, 30619),
    "en": (310, 349, 3797, "14966D617B087628BEB1D8682988D363D3C192259EA4644796FB2F70EC967F21", 24481, 28278),
}
_NEXT_SPECS = {
    "fr": (606, 607, 44, "4A475209FDC8F82DD042C34E0E03FA263A13589F05401380CD837E486D4B59E4", 30619, 30663),
    "en": (350, 351, 41, "6F66BB32211300C88FD0D4465C2D9F58CB2EF68C172E747797B9EFFA3BCD44C9", 28278, 28319),
}
LITERAL_CONTENT_SHA256 = {
    "fr": {
        "ega:I.7.3.1": "1880365811D4D8D47CE3E461CD48BAB6F3D60485DC36C2E5548B5281FE67B43A",
        "ega:I.7.3.2": "A3F752C25077B18630AE6F4D6E6DC1A125E57CB7862C637C8CE66D556D0A6FE8",
        "ega:I.7.3.3": "37F662F8EC3D8CAC92D905A8CB323E60BEE93F825E7B1AC564CDC9F83EE15DE2",
        "ega:I.7.3.4": "882EDE364E0D086004A85BFE75A77C84264FABEB56463E351645C776D348BF5F",
        "ega:I.7.3.2:restriction-tail": "2865604EAF15C268D98E141BF5A762F1F08DC494440FCE5378D97D261EBB6CB0",
        "ega:I.7.3.3:proof": "CCF542C5A25F7FEB696B99AEF72400E99ACB7697A21912BE36A010FDEF335343",
    },
    "en": {
        "ega:I.7.3.1": "89FD4BB82CF7644435A3E81C74C07985DB20F00CAA369440C9DBEAC6331ED559",
        "ega:I.7.3.2": "8AC6885354607B9E94583962A04AE752CCC6A8B8997E574D425BD926C3613A9E",
        "ega:I.7.3.3": "16FFB5C52CB552F03E867FA5EC810714599304BD30CE82473E684652B7658D3B",
        "ega:I.7.3.4": "A22E08DD94533298C9E2AEB273D40EABA0BD28663B910B29F7F079C40C606DCA",
        "ega:I.7.3.2:restriction-tail": "4313CEC8D29D9DF6B746D65E6E0821083E819850C25B1ED83AC6BBD2C21748FA",
        "ega:I.7.3.3:proof": "1F4ADB65560D5FB065DCD412DF0913DE40C5D5AC4317DFD300EAAD40351283A9",
    },
}
ENVIRONMENT_TOKEN = re.compile(rb"\\(?:begin|end)\{[^{}\r\n]+\}")
NUMBERED_BEGIN = re.compile(rb"\\begin\{([^{}\r\n]+)\}\[([0-9.]+)\]")
LABEL_TOKEN = re.compile(rb"\\label\{[^{}\r\n]+\}")


def _language(language):
    if type(language) is not str or language not in SOURCE_URLS:
        raise ValueError("unsupported source language")


def _span_spec(spec):
    return dict(zip(("lf_line_start", "lf_line_end", "bytes", "sha256",
                     "byte_offset_start", "byte_offset_end_exclusive"), spec))


def expected_contract(language):
    """Return a fresh independently pinned language contract, with no I/O."""
    _language(language)
    suffix = "-fr" if language == "fr" else ""
    return {
        "url": SOURCE_URLS[language], "full_bytes": SOURCE_IDENTITIES[language][0],
        "full_sha256": SOURCE_IDENTITIES[language][1],
        "slices": {"ega:I." + n: _span_spec(s) for n, s in zip(NUMBERS, _SLICE_SPECS[language])},
        "numbered_environments": {
            "ega:I." + n: {"label": "I." + n + suffix, "environment": env,
                "begin_line": spec[0], "label_line": spec[0] + 1,
                "closing_line": spec[1], **_span_spec(spec)}
            for n, env, spec in zip(NUMBERS, ENVIRONMENTS, _ENVIRONMENT_SPECS[language])},
        "owned_parts": {k: _span_spec(s) for k, s in zip(OWNED_KEYS, _OWNED_SPECS[language])},
        "page_markers": {PAGE_KEY: _span_spec(_PAGE_SPECS[language])},
        "section_heading": {"source_unit": "ega:I.7.3", **_span_spec(_HEADING_SPECS[language])},
        "combined": _span_spec(_COMBINED_SPECS[language]),
        "next_excluded_boundary": {"source_unit": "ega:I.7.3.5", **_span_spec(_NEXT_SPECS[language])},
    }


def _compare(actual, expected, path):
    """Strict recursive equality: bool/float never stand in for an integer."""
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
    """Return failures for one language artifact against the fixed contract."""
    try:
        contract = expected_contract(language)
    except ValueError as exc:
        return [str(exc)]
    return _compare(receipt, contract, language)


def raw_lines(raw):
    if type(raw) is not bytes or len(raw) > MAX_SOURCE_BYTES or b"\r" in raw or not raw.endswith(b"\n"):
        raise ValueError("source must be bounded exact LF-terminated bytes")
    try:
        raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ValueError("source must be valid exact UTF-8") from exc
    return [line + b"\n" for line in raw.split(b"\n")[:-1]]


def raw_span(lines, start, end):
    """Inclusive one-based physical-LF interval, preserving its terminal LF."""
    if type(start) is not int or type(end) is not int or not 1 <= start <= end <= len(lines):
        raise ValueError("invalid physical LF line interval")
    block = b"".join(lines[start - 1:end])
    offset = sum(map(len, lines[:start - 1]))
    return {"lf_line_start": start, "lf_line_end": end, "bytes": len(block),
            "sha256": hashlib.sha256(block).hexdigest().upper(), "byte_offset_start": offset,
            "byte_offset_end_exclusive": offset + len(block)}


def _text(lines):
    # Uncomment exactly once, physical line by physical line. Byte split uses
    # ASCII whitespace, not Unicode separators that could change LF ownership.
    return b" ".join(b" ".join(_uncomment(line).strip() for line in lines).split())


def artifact(data, language):
    """Derive mechanical metadata; extraction alone does not certify it."""
    _language(language)
    lines = raw_lines(data)
    suffix = "-fr" if language == "fr" else ""
    return {
        "url": SOURCE_URLS[language], "full_bytes": len(data),
        "full_sha256": hashlib.sha256(data).hexdigest().upper(),
        "slices": {"ega:I." + n: raw_span(lines, *r) for n, r in zip(NUMBERS, RANGES[language])},
        "numbered_environments": {"ega:I." + n: verify_numbered_span(data, *r, "I." + n + suffix)
                                  for n, r in zip(NUMBERS, ENVIRONMENT_RANGES[language])},
        "owned_parts": {k: raw_span(lines, *r) for k, r in zip(OWNED_KEYS, OWNED_RANGES[language])},
        "page_markers": {PAGE_KEY: raw_span(lines, *PAGE_RANGES[language])},
        "section_heading": {"source_unit": "ega:I.7.3", **raw_span(lines, *HEADING_RANGES[language])},
        "combined": raw_span(lines, *COMBINED_RANGES[language]),
        "next_excluded_boundary": {"source_unit": "ega:I.7.3.5", **raw_span(lines, *NEXT_RANGES[language])},
    }


source_metadata = artifact


def verify_structure(data, language):
    """Independent structural/literal failures, even if a fixture is rehashed.

    This does not certify whole-source identity; verify_source additionally
    enforces every pinned byte identity. Later 7.3.5 mathematics is not checked.
    """
    try:
        _language(language)
        lines = raw_lines(data)
    except ValueError as exc:
        return [str(exc)]
    if len(lines) < NEXT_RANGES[language][1]:
        return ["source omits the complete next excluded 7.3.5 begin/label"]
    clean = [_uncomment(line).strip() for line in lines]
    errors = []
    suffix = "-fr" if language == "fr" else ""
    first, last = COMBINED_RANGES[language]
    next_start, next_end = NEXT_RANGES[language]
    expected_wrappers, expected_labels, expected_numbered = [], [], []
    markers = []
    covered = set()
    for number, env, (start, end) in zip(NUMBERS, ENVIRONMENTS, ENVIRONMENT_RANGES[language]):
        begin = (r"\begin{" + env + "}[" + number + "]").encode()
        label = (r"\label{I." + number + suffix + "}").encode()
        close = (r"\end{" + env + "}").encode()
        markers.extend(((start, begin), (start + 1, label), (end, close)))
        expected_wrappers.extend(((start, (r"\begin{" + env + "}").encode()), (end, close)))
        expected_labels.append((start + 1, label))
        expected_numbered.append((start, env, number))
        covered.update(range(start, end + 1))
        owner = "ega:I." + number
        literal = hashlib.sha256(_text(lines[start + 1:end - 1])).hexdigest().upper()
        if literal != LITERAL_CONTENT_SHA256[language][owner]:
            errors.append(owner + ": literal content fingerprint mismatch")
    for index, (owner, (start, end)) in enumerate(zip(OWNED_KEYS, OWNED_RANGES[language])):
        body = lines[start - 1:end]
        if language == "en" and index == 1:
            proof_markers = [(start, b"\\begin{proof}"), (end, b"\\end{proof}")]
            expected_wrappers.extend(proof_markers)
            markers.extend(proof_markers)
            body = lines[start:end - 1]
        covered.update(range(start, end + 1))
        if hashlib.sha256(_text(body)).hexdigest().upper() != LITERAL_CONTENT_SHA256[language][owner]:
            errors.append(owner + ": literal content fingerprint mismatch")
    for offset, text in enumerate(HEADING_MARKERS[language]):
        n = HEADING_RANGES[language][0] + offset
        marker = text.encode()
        markers.append((n, marker))
        if offset == 1:
            expected_labels.append((n, marker))
        if sum(line.count(marker) for line in clean) != 1:
            errors.append("section heading marker must occur exactly once")
    covered.update(range(HEADING_RANGES[language][0], HEADING_RANGES[language][1] + 1))
    if clean[HEADING_RANGES[language][1] - 1]:
        errors.append("section heading separator must not contain substantive text")
    page_line = PAGE_RANGES[language][0]
    page_marker = PAGE_MARKER.encode()
    markers.append((page_line, page_marker))
    covered.add(page_line)
    if sum(line.count(page_marker) for line in clean) != 1:
        errors.append("old-page marker must occur exactly once and belongs only to 7.3.2")
    next_label = (r"\label{I.7.3.5" + suffix + "}").encode()
    markers.extend(((next_start, b"\\begin{corollary}[7.3.5]"), (next_end, next_label)))
    expected_wrappers.append((next_start, b"\\begin{corollary}"))
    expected_labels.append((next_end, next_label))
    expected_numbered.append((next_start, "corollary", "7.3.5"))
    # Complete token inventories reject mismatched, foreign, nested, early,
    # duplicated and inline wrappers even behind a rehashed receipt.
    actual_wrappers = [(n, m.group()) for n in range(first, next_end + 1)
                       for m in ENVIRONMENT_TOKEN.finditer(clean[n - 1])]
    if actual_wrappers != sorted(expected_wrappers):
        errors.append("numbered/proof wrapper inventory differs: nesting, duplication or wrong endpoint")
    actual_labels = [(n, m.group()) for n in range(first, next_end + 1)
                     for m in LABEL_TOKEN.finditer(clean[n - 1])]
    if actual_labels != sorted(expected_labels):
        errors.append("source label inventory differs")
    numbered = [(n + 1, m.group(1).decode(), m.group(2).decode())
                for n, line in enumerate(clean) for m in NUMBERED_BEGIN.finditer(line)]
    if [item for item in numbered if first <= item[0] <= next_end] != expected_numbered:
        errors.append("numbered source order differs")
    for n, env, number in expected_numbered:
        if [item for item in numbered if item[2] == number] != [(n, env, number)]:
            errors.append("I." + number + ": numbered begin must occur exactly once globally")
    for _, label in expected_labels:
        if sum(line.count(label) for line in clean) != 1:
            errors.append("source label must occur exactly once globally: " + label.decode())
    for n, token in markers:
        if clean[n - 1] != token:
            errors.append("exact source marker differs at raw LF " + str(n))
    for n in range(first, last + 1):
        if n not in covered and clean[n - 1]:
            errors.append("unowned substantive source line: " + str(n))
    return errors


def verify_source(data, language, expected=None):
    """Return all pinned identity, ownership and literal-content failures."""
    try:
        contract = expected_contract(language)
    except ValueError as exc:
        return [str(exc)]
    errors = validate_artifact(contract if expected is None else expected, language)
    errors.extend(verify_structure(data, language))
    try:
        actual = artifact(data, language)
        errors.extend(_compare(actual, contract, language + ".source"))
    except ValueError as exc:
        errors.append("raw source extraction failed: " + str(exc))
    return errors


def fetch_source(language, cached=None):
    """One bounded transport read; verify_source must certify returned bytes."""
    _language(language)
    size = SOURCE_IDENTITIES[language][0]
    if not 0 < size < MAX_SOURCE_BYTES:
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
    """729-compatible transport interface; malformed contracts cause no I/O."""
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
    args = parser.parse_args(argv)
    result = {"schema": "ega-i734-raw-source-boundary-replay/v1",
              "scope": "mechanical source ownership and literal identity; not semantic admission",
              "sources": {}, "errors": []}
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
        languages = receipt["languages"]
        if type(languages) is not dict or set(languages) != {"fr", "en"}:
            raise ValueError("languages must contain exactly fr and en")
        for language in ("fr", "en"):
            problems = validate_artifact(languages[language], language)
            if problems:
                raise ValueError("; ".join(problems))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result["errors"].append("source receipt read failed: " + str(exc))
        languages = {}
    for language, cached in (("fr", args.french), ("en", args.english)):
        if language not in languages:
            continue
        try:
            raw = read_source(languages[language], language, cached)
            problems = verify_source(raw, language, languages[language])
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
