"""Replay three independently pinned raw-LF versions of EGA I 7.3.8.

The old French assertion, later French replacement and corrected English are
different source objects. Byte ownership does not prove their mathematics or
admit the replacement under an older authority receipt. Constants transcribe
the verified source preparation, never a receipt under test. Complete French
proofs are unwrapped; English proof wrappers are distinct from the proof body.
The replacement instruction and internal page 222 marker remain owned, while
the next subsection/paragraph is excluded boundary evidence only.

One read per version, timeout 30 seconds, size at most the expected bytes plus
one, no retries and no writes. Offline literal fixtures are not whole sources.
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
RECEIPT = ROOT / "validation/ega-i-7.3.8-semantic-checkpoint-2026-09-08.json"
MAX_SOURCE_BYTES = 1024 * 1024
LANGUAGES = ("old_fr", "corrected_fr", "en")
SOURCE_URLS = {
    "old_fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega1/ega1-7-fr.tex",
    "corrected_fr": "https://raw.githubusercontent.com/KokunoYumeto/ega-fr/6b38875842e3723b619d4aeeda9ed260a4f94f7c/source/ega2/ega2-errata-addenda-fr.tex",
    "en": "https://raw.githubusercontent.com/KokunoYumeto/ega-en/94d5c73ac9263b26043ad0551646b824b1030c9b/source/ega1/ega1-7.tex",
}
SOURCE_IDENTITIES = {
    "old_fr": (38226, "73581030E142AD91D51F07A6DE7648101ECA92C7542EA52A2575F098F171F522", 786),
    "corrected_fr": (19746, "EC20D329248B99CF0533CB868DBDF8135D5BDAFA233133814DB67F8CD4F09643", 522),
    "en": (35788, "B36636DA91ADA9B74A7F2B4BF1C18E4576D35B363947D06EA475BCBA2918ADBC", 466),
}
# (first physical LF, last physical LF, byte count, SHA-256, first byte,
# exclusive last byte). Nested spans do not create additional source owners.
_SPECS = {
    "old_fr": {
        "owned": (648, 671, 834, "D586BFF4F2A8C402A22772F05E937AFDE75BA69579EBB4E9DA738A6E0DF8F105", 32381, 33215),
        "statement": (648, 659, 457, "322CBD99A5935D39B35495323889432DC8058C4E77F9122D13A27985AE35BF91", 32381, 32838),
        "proof": (661, 670, 375, "38A786F9D2AD885A2FCC4468710B0A55DC72DA3035DE5492252C454F0675A8FF", 32839, 33214),
        "proof_body": (661, 670, 375, "38A786F9D2AD885A2FCC4468710B0A55DC72DA3035DE5492252C454F0675A8FF", 32839, 33214),
        "excluded_next": (672, 676, 128, "C97D443CE4CFB4A5BD30E3603740F91A1F18AB19D048D82A0C5B91E11A849999", 33215, 33343),
    },
    "corrected_fr": {
        "owned": (470, 507, 1502, "E4B20875687FB851816337D513AC2CA29EB75F763D9CA9AD9C494584F23D488A", 17633, 19135),
        "statement": (473, 484, 485, "A6C6E3F0E0E604C73D6C803DEEBF583B71573919E9DE49C1FC2F572A5268A0BD", 17719, 18204),
        "proof": (486, 506, 929, "8FC034560A65725C39D71BD55A42E3F55E683F06B931887248AD5C36A8827F94", 18205, 19134),
        "proof_body": (486, 506, 929, "8FC034560A65725C39D71BD55A42E3F55E683F06B931887248AD5C36A8827F94", 18205, 19134),
        "excluded_next": (508, 508, 24, "200A43550C26FC13B3199F7C0096A831705526013DF3D1D390DFC90DA45800B8", 19135, 19159),
        "replacement_instruction": (470, 471, 85, "ABBE0EDA98922DDDF6144F4B8F55C8AD98FCF51366F5DCEC4BC76EE7D8A55893", 17633, 17718),
        "page_marker": (478, 478, 18, "E766C2D8F01FAE3855C1D5BAE458C31777767B5C3BC2CD4459CF9DD03BF422D0", 18000, 18018),
        "running_header": (479, 479, 70, "2B84856CC62A749ACAE9AC4542440DAB14AB80B543EE3D1AF8F09DC813B0F4DB", 18018, 18088),
        "equation": (480, 484, 116, "3488844AFCAB404132FC4B47F005CDDFF1437F4C6F2B9B90182B887B920D3B56", 18088, 18204),
    },
    "en": {
        "owned": (380, 402, 1470, "DAF1B23ACA4B7E07DA58FABCEB6690B56276C1EEC3C862E54E39CB2BF3D2A5B5", 29936, 31406),
        "statement": (380, 390, 501, "3EDF50FD96BD978996F2481F47D044766E2E8BC1BEC03888C87805F443C67C12", 29936, 30437),
        "proof": (392, 401, 967, "1FD0B9D469CCE2F4A04D00467A1F95BC360379F8B8BFB04BB8ABAD83E2D3E19D", 30438, 31405),
        "proof_body": (393, 400, 941, "EF1F5D1B0267966DCFF9BB0D7556195AEE374D582CF38A7340FD9F9D7CADA9B0", 30452, 31393),
        "excluded_next": (403, 408, 129, "A412AF7815AB8E08C4E1062597F21BC33DB01C2003B153B25EA20063CC25105C", 31406, 31535),
        "translator_note": (382, 382, 88, "7A35A5F9F260503009E2B4BCC4008C384A6BC648325771A9651A6743092A3515", 29971, 30059),
        "proof_open": (392, 392, 14, "82254B80D75A93E42D5A0698010614566C6A1DC34F33F625898E6FD258B9C778", 30438, 30452),
        "proof_close": (401, 401, 12, "23A57D3743025E89E5A2272D88A7987C7C16811D9AF1F0C93631A74A29979132", 31393, 31405),
    },
}
WRAPPERS = {
    "old_fr": ((648, rb"\begin{env}"), (659, rb"\end{env}"), (675, rb"\begin{env}")),
    "corrected_fr": ((480, rb"\begin{equation}"), (484, rb"\end{equation}")),
    "en": ((380, rb"\begin{env}"), (390, rb"\end{env}"), (392, rb"\begin{proof}"),
           (401, rb"\end{proof}"), (407, rb"\begin{env}")),
}
# These scoped identities must occur exactly once in the entire source file.
# Proof wrappers and running headers are not globally unique identifiers.
UNIQUE_MARKERS = {
    "old_fr": ((648, rb"\begin{env}[7.3.8]"), (649, rb"\label{I.7.3.8-fr}"),
               (657, rb"\label{I.7.3.8.1-fr}"), (673, rb"\label{subsection:I.7.4-fr}"),
               (675, rb"\begin{env}[7.4.1]"), (676, rb"\label{I.7.4.1-fr}")),
    "corrected_fr": ((470, rb"\paragraph{(I, 7.3.8).}"), (478, rb"\oldpage[II]{222}"),
                     (481, rb"\label{ega2:addendum:I.7.3.8.1-fr}"), (508, rb"\paragraph{(I, 9.5.2).}")),
    "en": ((380, rb"\begin{env}[7.3.8]"), (381, rb"\label{I.7.3.8}"),
           (386, rb"\label{I.7.3.8.1}"), (404, rb"\label{subsection:I.7.4}"),
           (405, rb"\label{I.7.4}"), (407, rb"\begin{env}[7.4.1]"), (408, rb"\label{I.7.4.1}")),
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
            "full_lf_lines": count, "proof_form": "wrapped" if language == "en" else "unwrapped",
            "spans": {key: _span_spec(spec) for key, spec in _SPECS[language].items()}}


def _compare(actual, expected, path):
    """Strict recursive equality, including types and complete inventories."""
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
    """Check a source artifact against independent constants, not itself."""
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
    """Inclusive one-based physical-LF interval, retaining terminal LF."""
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
            "proof_form": "wrapped" if language == "en" else "unwrapped",
            "spans": {key: raw_span(lines, *spec[:2]) for key, spec in _SPECS[language].items()}}


source_metadata = artifact


def verify_structure(data, language):
    """Verify owned literal bytes and wrappers independently of any rehash.

Whole-file certification additionally requires verify_source. Changes outside
the owned/excluded intervals are not semantic claims of this scoped checker.
"""
    try:
        _language(language)
        lines = raw_lines(data)
    except ValueError as exc:
        return [str(exc)]
    specs = _SPECS[language]
    first, last = specs["owned"][0], specs["excluded_next"][1]
    if len(lines) < last:
        return ["source omits the complete owned proof or next excluded boundary"]
    errors = []
    for key, spec in specs.items():
        actual = raw_span(lines, *spec[:2])
        if actual["bytes"] != spec[2] or actual["sha256"] != spec[3]:
            errors.append(key + ": exact literal source span mismatch")
    clean = [_uncomment(line) for line in lines]
    wrappers = [(n, match.group()) for n in range(first, last + 1)
                for match in ENVIRONMENT_TOKEN.finditer(clean[n - 1])]
    if wrappers != list(WRAPPERS[language]):
        errors.append("wrapper inventory differs: nesting, duplication, wrong endpoint or wrapped French proof")
    for position, marker in UNIQUE_MARKERS[language]:
        occurrences = [n + 1 for n, line in enumerate(clean) for _ in range(line.count(marker))]
        if occurrences != [position]:
            errors.append("globally unique source marker differs: " + marker.decode("utf-8"))
    return errors


def verify_source(data, language, expected=None):
    """Return pinned identity, exact ownership and structural failures."""
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
    """One bounded transport read; verify_source must certify the bytes."""
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
    """Malformed or one-version-swapped contracts cause no source I/O."""
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
    parser.add_argument("--old-french", type=Path)
    parser.add_argument("--corrected-french", type=Path)
    parser.add_argument("--english", type=Path)
    args = parser.parse_args(argv)
    result = {"schema": "ega-i738-raw-source-boundary-replay/v1",
              "scope": "three-version mechanical ownership and literal identity; not semantic admission",
              "sources": {}, "errors": []}
    try:
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
        languages = receipt["languages"]
        if type(languages) is not dict or set(languages) != set(LANGUAGES):
            raise ValueError("languages must contain exactly old_fr, corrected_fr and en")
        # Complete all three receipt checks before the first transport read.
        for language in LANGUAGES:
            problems = validate_artifact(languages[language], language)
            if problems:
                raise ValueError("; ".join(problems))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result["errors"].append("source receipt read failed: " + str(exc))
        languages = {}
    for language, cached in zip(LANGUAGES, (args.old_french, args.corrected_french, args.english)):
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
