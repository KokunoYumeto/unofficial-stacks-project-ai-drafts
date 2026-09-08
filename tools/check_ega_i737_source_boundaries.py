"""Replay independently pinned raw-LF ownership for EGA I 7.3.5--7.3.7.

Mechanical byte, structure and literal-content identity is not semantic
admission. All three complete source proofs belong to their unit slices; the
French prose is unwrapped and English proof wrappers are separate from bodies.
The 7.3.7 page marker is nested in its declaration. No section heading is
re-owned, and the 7.3.8 env begin/label is excluded boundary evidence only.

Constants transcribe the verified 2026-09-08 boundary preparation, independently
of any receipt-under-test. One fetch per language uses a 30-second timeout and
at most the pinned size plus one byte, never exceeding 1 MiB. No files are written.
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
RECEIPT = ROOT / "validation/ega-i-7.3.5-7.3.7-semantic-checkpoint-2026-09-08.json"
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
NUMBERS = ("7.3.5", "7.3.6", "7.3.7")
ENVIRONMENTS = ("corollary", "corollary", "proposition")
RANGES = {"fr": ((606, 622), (623, 633), (634, 647)),
          "en": ((350, 358), (359, 367), (368, 379))}
ENVIRONMENT_RANGES = {"fr": ((606, 610), (623, 630), (634, 642)),
                      "en": ((350, 353), (359, 362), (368, 374))}
OWNED_KEYS = ("ega:I.7.3.5:proof", "ega:I.7.3.6:proof", "ega:I.7.3.7:proof")
OWNED_RANGES = {"fr": ((612, 621), (632, 632), (644, 646)),
                "en": ((355, 357), (364, 366), (376, 378))}
BODY_RANGES = {"fr": ((612, 621), (632, 632), (644, 646)),
               "en": ((356, 356), (365, 365), (377, 377))}
PAGE_KEY = "ega:I.7.3.7:page-marker"
PAGE_RANGES = {"fr": (637, 637), "en": (371, 371)}
PAGE_MARKER = r"\oldpage[I]{163}"
COMBINED_RANGES = {"fr": (606, 647), "en": (350, 379)}
NEXT_RANGES = {"fr": (648, 649), "en": (380, 381)}
NEXT_NUMBER = "7.3.8"
DISCOVERY_UNIT_IDS = ("ega:I.7.3.5", "ega:I.7.3.5:proof", "ega:I.7.3.6",
                      "ega:I.7.3.6:proof", "ega:I.7.3.7", "ega:I.7.3.7:proof")

# Fixed witnesses: (first LF, last LF, bytes, SHA-256, first byte, exclusive last byte).
# Extraction below recomputes these independently from the supplied source bytes.
_SLICE_SPECS = {
    "fr": (
        (606, 622, 743, "34483F8049FE5813EC8C0FBC57A6E690612F03D1C5FF554989152FBFC0BCBAD2", 30619, 31362),
        (623, 633, 458, "D1D970C8DFF62B0A5C1291375616BBD0676E3490571885DD75400FFF4A07E5D2", 31362, 31820),
        (634, 647, 561, "8EFE341C64F96835FE3295A142A2448C4B2147D42E77DF4F5480827FD87F4FAB", 31820, 32381)),
    "en": (
        (350, 358, 718, "D30594531D6047DD9CD81B518A8218A67AD23479A98157C7637339EBCFB77515", 28278, 28996),
        (359, 367, 433, "893B0CFECFDEFAA8C0E6448D499F71FABC52D4429E55DCB5350AA99413F824DD", 28996, 29429),
        (368, 379, 507, "530D53B3CC773269A21AA4B58B813EC6A21E3899E5EF0F89701D8FA8B4C1ECF2", 29429, 29936)),
}
_ENVIRONMENT_SPECS = {
    "fr": (
        (606, 610, 169, "F70A090A5FFC2B97B06174041527F2993C3F1EE61AE66F55258A0A23EF0D31DE", 30619, 30788),
        (623, 630, 389, "0CEFF3538EEEF9315487B7249AC969BA8B428DE2E818C9014D3AAFBB1B39EE94", 31362, 31751),
        (634, 642, 399, "F491006BA55652623BD0E1C2B22D5370AF9DAEC988E31B9C34E7FE3C995D72FC", 31820, 32219)),
    "en": (
        (350, 353, 153, "2FBF1401F7185231295444D7AD6B064B8AA2B95EB972E39188C5E94380BB7706", 28278, 28431),
        (359, 362, 342, "B0FADFBF39094A78D0EA688D0C7C6F5995C82C21EF56923814940EB272A594F6", 28996, 29338),
        (368, 374, 365, "4E1CCF0F48EFAAA24DCC34A9F92C2A677EF2FA29505DD5393E4E61E31B455B15", 29429, 29794)),
}
_OWNED_SPECS = {
    "fr": (
        (612, 621, 572, "A6FD0876301AA40E3F763249514DB12F4F82C54606134294F8838E880AC00132", 30789, 31361),
        (632, 632, 67, "D829D5C68D3403BC5B2925BDD6BB01364A901ED22983274B1E4E5BFBF9185D8D", 31752, 31819),
        (644, 646, 160, "E0CF52AB583BC579570348AE5E441558AB2293629AD99DB3D8930EAE713D164F", 32220, 32380)),
    "en": (
        (355, 357, 563, "DD1F92C5AC30FA2168C39751E68742D81220D9D5E2F11E75A4ED491614111712", 28432, 28995),
        (364, 366, 89, "1530415809B971CCE53F35ABDB63B68D4F5573C6311CC224985F182922904A0E", 29339, 29428),
        (376, 378, 140, "7942993D805E3E0FFE29F9FCECFB2C5F3305160F148F018C5FD92E3F0AC93673", 29795, 29935)),
}
_BODY_SPECS = {
    "fr": (
        (612, 621, 572, "A6FD0876301AA40E3F763249514DB12F4F82C54606134294F8838E880AC00132", 30789, 31361),
        (632, 632, 67, "D829D5C68D3403BC5B2925BDD6BB01364A901ED22983274B1E4E5BFBF9185D8D", 31752, 31819),
        (644, 646, 160, "E0CF52AB583BC579570348AE5E441558AB2293629AD99DB3D8930EAE713D164F", 32220, 32380)),
    "en": (
        (356, 356, 537, "A300E6454C37C5681FA5CFA4CCC094D04F25E0CF2595AC2B848A306A6605E6E5", 28446, 28983),
        (365, 365, 63, "0D5A948C172EADCE378C2CDFA1FE6936ABE4938FE4288C00A94C909AFCCBB91A", 29353, 29416),
        (377, 377, 114, "D023D91BD83EEFBE0754725C0A978E8E12F9F9E0BC7287EB36747A94192EC579", 29809, 29923)),
}
_PAGE_SPECS = {
    "fr": (637, 637, 17, "B8E91EDCB9B69BC8BD837C9705DB24887B72667BF33411E1C814559798D1FD0E", 31938, 31955),
    "en": (371, 371, 17, "B8E91EDCB9B69BC8BD837C9705DB24887B72667BF33411E1C814559798D1FD0E", 29534, 29551),
}
_COMBINED_SPECS = {
    "fr": (606, 647, 1762, "44892720D0751CDD5EEC00B030AB61E153260DB6AE29629A6207643B103D55AD", 30619, 32381),
    "en": (350, 379, 1658, "BBB8126EE7F4EB4EEC4235E9154111E17EB2B47AA0E87A4B490AA0F70B4EC29F", 28278, 29936),
}
_NEXT_SPECS = {
    "fr": (648, 649, 38, "52ECAD7A7968E8567124370E8FA99839EF46DAEB8A569A586403DDCDB6798C4A", 32381, 32419),
    "en": (380, 381, 35, "596280977B9ACF64A2850F47A6E746382126A030ED8BA0CE44523FAFC5975FE3", 29936, 29971),
}
LITERAL_CONTENT_SHA256 = {
    "fr": {
        "ega:I.7.3.5": "D2DFBB504E8DFED1BA4FBF7E30D7516F62484A953FBE6D4CF2C796B5331B97B9",
        "ega:I.7.3.5:proof": "44E77CDCA4724C87CBCF3A57CC631DB31EC29F50B016B1C64A46F7EFBEB01742",
        "ega:I.7.3.6": "CF6E9D135CDE09AA777B9908A54E8E5ED6E969469FF07CEE0FEDF236032588FC",
        "ega:I.7.3.6:proof": "07FD182421D4EE1DDEA7A1C36DB593E3398507651AEAD6E511D677A2D0C63318",
        "ega:I.7.3.7": "E00210881E6DBA29EE7A971341BDD812083CBEB1674D235F4F2566B5639A1944",
        "ega:I.7.3.7:proof": "4A50FDEA597222FFF42BAC297B4E2E733DD70716AAADAFA4EC83E5CF7FE3FD95",
    },
    "en": {
        "ega:I.7.3.5": "60E42885B33BE839D57C0874D0C4D13A308886EE2DABC07B06DAC32F8D92AE28",
        "ega:I.7.3.5:proof": "AD4411251E1B462A48917523056FAE3C066BCE72033908C8BF67A7B0B52EF1D3",
        "ega:I.7.3.6": "A323D7DFB83D2A1832B6C75B008330D4CFDD10E072A1A7BED573EBF4CA57605E",
        "ega:I.7.3.6:proof": "F4D36A26B792F0502D2410C0436768BBA13E2C240B6B9F9C719FB7DB98066F26",
        "ega:I.7.3.7": "5C0719E87A1CC49A208EDB733D68AA313B463F3ADD0E014C0D4E4F8440C0769D",
        "ega:I.7.3.7:proof": "F6A612533EC59DDC0FEA2E27BFDE7A633A2DC3AF2213BC8E89ABE7145FFC015F",
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
    """Fresh independently pinned contract, with no receipt access or other I/O."""
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
        "proof_bodies": {k: _span_spec(s) for k, s in zip(OWNED_KEYS, _BODY_SPECS[language])},
        "page_markers": {PAGE_KEY: _span_spec(_PAGE_SPECS[language])},
        "section_heading": None,
        "combined": _span_spec(_COMBINED_SPECS[language]),
        "next_excluded_boundary": {"source_unit": "ega:I.7.3.8", **_span_spec(_NEXT_SPECS[language])},
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
    if (type(raw) is not bytes or len(raw) > MAX_SOURCE_BYTES or b"\r" in raw
            or not raw.endswith(b"\n") or raw.startswith(b"\xef\xbb\xbf")):
        raise ValueError("source must be bounded exact LF-terminated bytes without BOM")
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
    # Comment removal is physical-line based; byte whitespace is ASCII only.
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
        "proof_bodies": {k: raw_span(lines, *r) for k, r in zip(OWNED_KEYS, BODY_RANGES[language])},
        "page_markers": {PAGE_KEY: raw_span(lines, *PAGE_RANGES[language])},
        "section_heading": None,
        "combined": raw_span(lines, *COMBINED_RANGES[language]),
        "next_excluded_boundary": {"source_unit": "ega:I.7.3.8", **raw_span(lines, *NEXT_RANGES[language])},
    }


source_metadata = artifact


def verify_structure(data, language):
    """Check literal/structural ownership even behind a self-rehashed receipt.

    Whole-source certification additionally requires verify_source. Mathematics
    following the excluded 7.3.8 header is not reviewed by this interval.
    """
    try:
        _language(language)
        lines = raw_lines(data)
    except ValueError as exc:
        return [str(exc)]
    if len(lines) < NEXT_RANGES[language][1]:
        return ["source omits the complete next excluded 7.3.8 begin/label"]
    clean = [_uncomment(line).strip() for line in lines]
    errors = []
    suffix = "-fr" if language == "fr" else ""
    first, last = COMBINED_RANGES[language]
    next_start, next_end = NEXT_RANGES[language]
    expected_wrappers, expected_labels, expected_numbered = [], [], []
    markers, covered = [], set()
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
        if hashlib.sha256(_text(lines[start + 1:end - 1])).hexdigest().upper() != LITERAL_CONTENT_SHA256[language][owner]:
            errors.append(owner + ": literal content fingerprint mismatch")
    for owner, (start, end), (body_start, body_end) in zip(OWNED_KEYS, OWNED_RANGES[language], BODY_RANGES[language]):
        if language == "en":
            proof_markers = [(start, b"\\begin{proof}"), (end, b"\\end{proof}")]
            expected_wrappers.extend(proof_markers)
            markers.extend(proof_markers)
        covered.update(range(start, end + 1))
        if hashlib.sha256(_text(lines[body_start - 1:body_end])).hexdigest().upper() != LITERAL_CONTENT_SHA256[language][owner]:
            errors.append(owner + ": literal content fingerprint mismatch")
    page_line = PAGE_RANGES[language][0]
    page_marker = PAGE_MARKER.encode()
    markers.append((page_line, page_marker))
    if sum(line.count(page_marker) for line in clean) != 1:
        errors.append("old-page marker must occur exactly once inside the 7.3.7 declaration")
    next_label = (r"\label{I.7.3.8" + suffix + "}").encode()
    markers.extend(((next_start, b"\\begin{env}[7.3.8]"), (next_end, next_label)))
    expected_wrappers.append((next_start, b"\\begin{env}"))
    expected_labels.append((next_end, next_label))
    expected_numbered.append((next_start, "env", "7.3.8"))
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
    """734-compatible interface; malformed contracts cause no source I/O."""
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
    result = {"schema": "ega-i737-raw-source-boundary-replay/v1",
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
