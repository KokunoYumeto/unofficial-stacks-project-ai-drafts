#!/usr/bin/env python3
"""No-overwrite semantic successor sem/r22 for the D1029 p.188 repair."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence


ROOT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
FTG = Path(r"user\Documents\stacks-ftg")
SCRIPT = Path(__file__).resolve(strict=True)
PREDECESSOR = ROOT / "sem" / "r21"
FINAL = ROOT / "sem" / "r22"
STAGE = ROOT / "sem" / ".r22.d1029.stage"
RECOVERY = ROOT / "sem" / ".r22.d1029.recovery"
SOURCE_ROOT = ROOT / "production" / "p188_fix1"
BUILD_RECEIPT = ROOT / "build" / "v068c3r21" / "build.json"
QA_CHECK = ROOT / "qa" / "v68r43" / "check.json"
QA_STRUCTURAL = ROOT / "qa" / "v68r43" / "structural.json"
LEDGER = ROOT / "SOURCE_CORRECTIONS.jsonl"
CANDIDATE = FTG / "tmp" / "d1029_ext_center_actions_candidate.tex"
MATH_AUDIT = FTG / "tmp" / "d1029_ext_center_math_source_audit.json"
ISSUE_PROPOSAL = FTG / "tmp" / "d1029_source_repair_toolchain" / "I000033_proposal.json"
TARGET_CATALOG_ID = "TOHOKU-1957-119-221"
TARGET_NODE_ID = "tohoku:remark:ext-center-modules"
TARGET_OCCURRENCE_ID = "tohoku:occ:p188:o002"
TARGET_VERSION = "local-v068c3r21-sem-r22"
CREATED_UTC = "2026-08-24T08:50:00Z"

PREDECESSOR_FILES: dict[str, tuple[int, str]] = {
    "bib.csv": (10422, "93F5A934ADDE0CD92BBB21AF70EFD81BA128CCD2EDF51EB19428B83437EC3516"),
    "catalog.csv": (772, "7726735ABA05D9F5791DBE143EB27D25CBBD9161ABE8F82ABF40FE1D8B489180"),
    "edges.csv": (261660, "5B924BF4E9D0E7CAFF51D3C75D0C85045E985AE21152744ABD38929A87E622D5"),
    "idmap.csv": (473, "977D4A8F59A9642D58926DED8BB600079863AE6AF3F1F532806E83A9AB645BEA"),
    "manifest.json": (32119, "38275B0B2BB116467B3848F2E7EB1740F3692551E531E4130E72279F47F98C59"),
    "nodes.csv": (586416, "C0DD26F979C17DA1DA8E09CAD83FEAA44BA8644DB0625D693C3D20A8B82CCBCA"),
    "objects.csv": (106319, "82FF34C19C6D17D80DC3A617FD106ED324099CC9D0F2FE752757D0642ED31999"),
    "occ.csv": (515088, "637CA9EF1382846C88408D6FF0CBF45F785758EE469C10D60B84943685136833"),
    "pages.csv": (23686, "E813C410B0A2AE53B4A787FD6C66A74225021E3A0FE22AD10CA2ED0C29807B0D"),
    "README.md": (2585, "66D4CF92728AF7FF10E82CDFD97AFCD9D26B55CE9FBC985932FFBCD597DD64B4"),
    "refdec.csv": (2313, "6AC5E23C3D4ADA0ABB1427E0533C3033E13B63C28A654A9C7E74A057A045FFA2"),
    "refs.csv": (161519, "2BB0DC3356C0C4B18E82F7C168334D450DF541586EE89F94FB254C3296ACDE3D"),
    "resid.csv": (6415, "DDF53E58E21C7A5BF60C54ADC5EB9EB420B717246F1C69F294BBA5E358A38430"),
    "stacks.csv": (11777, "E13EFA405B525D69BFF38256601E4AF64D22FA3075F3A95AB3DFB78C15CFD060"),
    "subjects.csv": (2133, "A77A81831F752BA21701B150C13C51325E511B2FD5DFC76EED135FE3EDEEB026"),
    "terms.csv": (325587, "6D93CBBD2D6CF3E354FE90DC51605ACD9C7B0932CEF216FB9D606AD97D666E5D"),
    "validation.json": (9395, "D15C85751526EA144BFA02AFBB580540C93620C7AC12A6656D1C895EEA5A8BDB"),
    "xwork.csv": (2446, "7BC42D7026C34AD8B1A111353E0810378F1DB9D1284BAD4C5C34D509D57B9EBB"),
}
INPUTS = {
    "source_receipt": (SOURCE_ROOT / "check.json", 4625, "52D174E72E44BE1DC5E6EE25A405B8C971EA4434F10BA7753F10CA1491851CF6"),
    "source_decisions": (SOURCE_ROOT / "decisions.jsonl", 4600, "DE1B3BB745A6B8FDCC3573F83A272060DB727B87B9A079BA4C0EADCE51951420"),
    "source_dip": (SOURCE_ROOT / "tex" / "fr_diplomatic" / "p188.tex", 3890, "0C9D3A1133C014C9BB6687580DCFBDE40A87B7FE21E98838BFD820983334D9FF"),
    "source_fr": (SOURCE_ROOT / "tex" / "fr_corrected" / "p188.tex", 3619, "3CD7D1D8D50DD83627B24AC726EB244E09CAF483890071D68940C551A42ED0CC"),
    "source_en": (SOURCE_ROOT / "tex" / "en" / "p188.tex", 3498, "A171187600BB72B32FDB4E686D5AC994146BEC8DFC99571F0ACF3C3B1862FA5C"),
    "ledger": (LEDGER, 213247, "F2DE702681CF4150C87FDC9C9051A105E94CBD681219ADC600DB9049B1E1E4B1"),
    "build_receipt": (BUILD_RECEIPT, 21071, "EEB4DAE83F5D940681190C24BACC50A9799850A87399D1D36B9E663525B1D6FB"),
    "qa_check": (QA_CHECK, 1785, "975A0FAA9E32C6F414AAFC7B0ED5405557ED129D0EDAF08D46EBAE6FDD02CB0E"),
    "qa_structural": (QA_STRUCTURAL, 4962, "1CD7585C165BDCDF2761B3A1EB2A653C66D0A0F57BECF2E395EB2D953E46A7AD"),
    "candidate": (CANDIDATE, 3189, "6B6566697F349854C1866661952A7AC5487FAFEB473354D4403E27886B3287FA"),
    "math_audit": (MATH_AUDIT, 14637, "35C3ECBD18B1F06036C58723D0B59E1CAD48BE29890E8E0026C0A99280A3EC64"),
    "issue_proposal": (ISSUE_PROPOSAL, 1375, "9638FFE1A46D351900C1BA2CFE6E241ED5DAF644915A38CFBF1F7CDA43D97F46"),
}
SEGMENT_SHA = {
    "dip": "608C04856144CBD82A6FEF84C82E017DBF8EF2ACDCC899A8B5689C277AAF2BD4",
    "fr": "C7E91C473DEDB70A7164B8C62C715FDB2F86B839AE1745D71E5A76567B493F09",
    "en": "BF13824866DEB2B4DD2D11136943493204F055017CC35D175DD7A68E8E81E092",
}
UNCHANGED_DATA = [name for name in PREDECESSOR_FILES if name not in {"catalog.csv", "nodes.csv", "occ.csv", "manifest.json", "validation.json"}]
DATA_FILES = [name for name in PREDECESSOR_FILES if name not in {"manifest.json", "validation.json"}]


class SemError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def ident(path: Path, data: bytes, role: str | None = None) -> dict[str, Any]:
    try:
        shown = path.relative_to(ROOT).as_posix()
    except ValueError:
        shown = str(path)
    value = {"path": shown, "bytes": len(data), "sha256": sha(data)}
    if role:
        value["role"] = role
    return value


def exact(path: Path, expected: tuple[int, str], label: str) -> bytes:
    if not path.is_file() or path.is_symlink() or path.resolve(strict=True) != path:
        raise SemError(f"{label}: invalid path")
    data = path.read_bytes()
    if (len(data), sha(data)) != expected:
        raise SemError(f"{label}: identity drifted: {(len(data), sha(data))}")
    return data


def pretty(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def csv_rows(data: bytes, label: str) -> tuple[list[str], list[dict[str, str]]]:
    text = data.decode("utf-8")
    reader = csv.DictReader(io.StringIO(text, newline=""))
    if reader.fieldnames is None or len(reader.fieldnames) != len(set(reader.fieldnames)):
        raise SemError(f"{label}: invalid header")
    rows = [dict(row) for row in reader]
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise SemError(f"{label}: malformed row")
    return list(reader.fieldnames), rows


def csv_bytes(fields: Sequence[str], rows: Sequence[Mapping[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(fields), lineterminator="\n")
    writer.writeheader(); writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def one(rows: Sequence[dict[str, str]], key: str, value: str, label: str) -> dict[str, str]:
    hits = [row for row in rows if row.get(key) == value]
    if len(hits) != 1:
        raise SemError(f"{label}: expected one row for {value}, found {len(hits)}")
    return hits[0]


def patch_csv(data: bytes, label: str, key: str, value: str, patch: Mapping[str, str]) -> bytes:
    fields, rows = csv_rows(data, label)
    row = one(rows, key, value, label)
    if not set(patch).issubset(fields):
        raise SemError(f"{label}: patch fields absent")
    row.update(patch)
    return csv_bytes(fields, rows)


def segment(page: bytes) -> bytes:
    marker = f"\\LayerTarget{{{TARGET_NODE_ID}}}".encode()
    if page.count(marker) != 1:
        raise SemError("target LayerTarget multiplicity drifted")
    start = page.index(marker) + len(marker)
    end = page.find(b"\\LayerTarget{", start)
    return page[start:] if end < 0 else page[start:end]


def detex(value: bytes, limit: int = 320) -> str:
    text = value.decode("utf-8")
    text = re.sub(r"(?m)(?<!\\)%.*$", "", text)
    text = re.sub(r"\\(?:begin|end)\{[^}]+\}", " ", text)
    text = re.sub(r"\\(?:addcontentsline|markboth)\{[^}]*\}(?:\{[^}]*\}){0,2}", " ", text)
    text = re.sub(r"\\(?:SourcePage|TohokuContinuation|TohokuTerminal)\{[^}]*\}", " ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace("\\[", " ").replace("\\]", " ")
    text = text.replace("{", " ").replace("}", " ").replace("$", " ").replace("~", " ")
    text = re.sub(r"\\[^A-Za-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def row_delta(before: bytes, after: bytes, label: str, key: str) -> list[dict[str, str]]:
    fields0, rows0 = csv_rows(before, label + " predecessor")
    fields1, rows1 = csv_rows(after, label + " successor")
    if fields0 != fields1 or [row[key] for row in rows0] != [row[key] for row in rows1]:
        raise SemError(f"{label}: header/order/ID sequence changed")
    delta = []
    for old, new in zip(rows0, rows1):
        for field in fields0:
            if old[field] != new[field]:
                delta.append({"key": old[key], "field": field, "before": old[field], "after": new[field]})
    return delta


def surface(entries: Sequence[Mapping[str, Any]]) -> tuple[int, str]:
    payload = b"".join(str(row["name"]).encode() + b"\0" + str(row["bytes"]).encode() + b"\0" + str(row["sha256"]).encode() + b"\n" for row in entries)
    return len(payload), sha(payload)


def derive() -> dict[str, Any]:
    predecessor = {name: exact(PREDECESSOR / name, spec, f"sem/r21 {name}") for name, spec in PREDECESSOR_FILES.items()}
    inputs = {name: exact(path, (size, digest), name) for name, (path, size, digest) in INPUTS.items()}
    if json.loads(inputs["qa_check"].decode())["status"] != "PASS" or json.loads(inputs["math_audit"].decode())["verdict"] != "STRICT_PASS":
        raise SemError("reader QA or D1029 math audit is not PASS")
    pages = {layer: inputs[f"source_{layer}"] for layer in ("dip", "fr", "en")}
    segments = {layer: segment(page) for layer, page in pages.items()}
    for layer, data in segments.items():
        if sha(data) != SEGMENT_SHA[layer]:
            raise SemError(f"{layer}: target segment identity drifted")
    if b"\\Gamma(O^\\natural)" not in segments["fr"] or b"\\Gamma(O^\\natural)" not in segments["en"]:
        raise SemError("corrected scalar ring absent from aligned segment")
    labels = {layer: detex(segments[layer]) for layer in ("fr", "en")}
    if "centre de (O)" in labels["fr"] or "center of (O)" in labels["en"] or "(O^ )" not in labels["fr"] or "(O^ )" not in labels["en"]:
        raise SemError("semantic label correction did not normalize as expected")

    decision_row = [line for line in inputs["source_decisions"].splitlines(keepends=True) if b'"decision_id":"TOH-P188-COR-002"' in line]
    if len(decision_row) != 1 or (len(decision_row[0]), sha(decision_row[0])) != (651, "C2F4FE4ED7EE537808C803745A19F14005430EED26FD53282720AAC48F8F24EF"):
        raise SemError("TOH-P188-COR-002 row drifted")
    provenance = (
        "production/p188_fix1/decisions.jsonl#TOH-P188-COR-002;"
        "decision_row_sha256=C2F4FE4ED7EE537808C803745A19F14005430EED26FD53282720AAC48F8F24EF;"
        f"dip_segment_sha256={SEGMENT_SHA['dip']};fr_segment_sha256={SEGMENT_SHA['fr']};en_segment_sha256={SEGMENT_SHA['en']};"
        "SOURCE_CORRECTIONS.jsonl#TOH-SRC-P188-003;defect=D1029-R001;"
        "candidate_sha256=6B6566697F349854C1866661952A7AC5487FAFEB473354D4403E27886B3287FA;"
        "audit_sha256=35C3ECBD18B1F06036C58723D0B59E1CAD48BE29890E8E0026C0A99280A3EC64"
    )

    candidate = {name: predecessor[name] for name in DATA_FILES}
    candidate["catalog.csv"] = patch_csv(predecessor["catalog.csv"], "catalog.csv", "catalog_id", TARGET_CATALOG_ID, {
        "french_reader": "output/pdf/fr-p119-221-v068c3r21.pdf",
        "french_sha256": "AADC500F836F5E9397160C4E3BEAB1AD354E35742937D495360D41D2E4A7E865",
        "english_reader": "output/pdf/en-p119-221-v068c3r21.pdf",
        "english_sha256": "C45350A80D39954A203993B3E6B2FB58532425915BFEC517E99DB01BF08AB39F",
        "version": TARGET_VERSION,
        "page_state": "current_r21_visual_gate_closed",
    })
    candidate["nodes.csv"] = patch_csv(predecessor["nodes.csv"], "nodes.csv", "node_id", TARGET_NODE_ID, {
        "fr_label": labels["fr"], "en_label": labels["en"], "provenance": provenance,
    })
    candidate["occ.csv"] = patch_csv(predecessor["occ.csv"], "occ.csv", "occurrence_id", TARGET_OCCURRENCE_ID, {
        "decision_path": "production/p188_fix1/decisions.jsonl", "fr_sha256": SEGMENT_SHA["fr"], "en_sha256": SEGMENT_SHA["en"],
    })
    for name in UNCHANGED_DATA:
        if candidate[name] != predecessor[name]:
            raise SemError(f"unchanged payload drifted: {name}")
    deltas = {
        "catalog.csv": row_delta(predecessor["catalog.csv"], candidate["catalog.csv"], "catalog.csv", "catalog_id"),
        "nodes.csv": row_delta(predecessor["nodes.csv"], candidate["nodes.csv"], "nodes.csv", "node_id"),
        "occ.csv": row_delta(predecessor["occ.csv"], candidate["occ.csv"], "occ.csv", "occurrence_id"),
    }
    if {row["field"] for row in deltas["catalog.csv"]} != {"french_reader", "french_sha256", "english_reader", "english_sha256", "version", "page_state"}:
        raise SemError("catalog delta is not exact")
    if {row["field"] for row in deltas["nodes.csv"]} != {"fr_label", "en_label", "provenance"}:
        raise SemError("node delta is not exact")
    if {row["field"] for row in deltas["occ.csv"]} != {"decision_path", "fr_sha256", "en_sha256"}:
        raise SemError("occurrence delta is not exact")
    if sum(map(len, deltas.values())) != 12:
        raise SemError("semantic delta is not exactly twelve existing fields")
    entries = [{"name": name, "bytes": len(candidate[name]), "sha256": sha(candidate[name])} for name in DATA_FILES]
    aggregate_bytes, aggregate_sha = surface(entries)
    counts = {name: len(csv_rows(candidate[name], name)[1]) for name in DATA_FILES if name.endswith(".csv")}
    script_data = SCRIPT.read_bytes()
    manifest = {
        "schema": "tohoku-semantic-local-successor-manifest-v22",
        "corpus": "tohoku",
        "scope": "printed pages 119-221",
        "version": TARGET_VERSION,
        "binding_state": "local_unpublished",
        "record_binding": "no DOI or public record mutation",
        "created_utc": CREATED_UTC,
        "inputs": [ident(path, inputs[name], name) for name, (path, _size, _digest) in INPUTS.items()],
        "successor_execution": {"script": ident(SCRIPT, script_data), "target": "sem/r22", "no_overwrite": True},
        "reader_binding": {
            "revision": "v068c3r21",
            "build_receipt": ident(BUILD_RECEIPT, inputs["build_receipt"]),
            "qa_check": ident(QA_CHECK, inputs["qa_check"]),
            "french_pdf": {"path": "output/pdf/fr-p119-221-v068c3r21.pdf", "bytes": 1417508, "sha256": "AADC500F836F5E9397160C4E3BEAB1AD354E35742937D495360D41D2E4A7E865", "pages": 94},
            "english_pdf": {"path": "output/pdf/en-p119-221-v068c3r21.pdf", "bytes": 1381119, "sha256": "C45350A80D39954A203993B3E6B2FB58532425915BFEC517E99DB01BF08AB39F", "pages": 90},
        },
        "source_repair_binding": {
            "unit_id": TARGET_NODE_ID,
            "occurrence_id": TARGET_OCCURRENCE_ID,
            "decision_id": "TOH-P188-COR-002",
            "source_correction_id": "TOH-SRC-P188-003",
            "production_successor": "production/p188_fix1",
            "diplomatic_segment_byte_identical": True,
            "segments": {layer: {"bytes": len(data), "sha256": sha(data)} for layer, data in segments.items()},
            "labels": labels,
            "provenance": provenance,
        },
        "issue_binding": {"issue_id": "I000033", "state": "proposal_only_not_appended_by_source_repair", "proposal": ident(ISSUE_PROPOSAL, inputs["issue_proposal"])},
        "stable_id_replay": {"predecessor_node_ids_reused": counts["nodes.csv"], "new_node_ids": [], "predecessor_occurrence_ids_reused": counts["occ.csv"], "new_occurrence_ids": [], "ordering_preserved": True},
        "table_delta_oracle": {"changed_tables": 3, "changed_existing_fields": 12, "appended_rows": 0, "affected_node_ids": [TARGET_NODE_ID], "affected_occurrence_ids": [TARGET_OCCURRENCE_ID], "deltas": deltas},
        "counts": counts,
        "files": entries,
        "file_surface": {"records": len(entries), "bytes": sum(row["bytes"] for row in entries), "aggregate_manifest_bytes": aggregate_bytes, "aggregate_sha256": aggregate_sha, "algorithm": "name+NUL+decimal_bytes+NUL+uppercase_sha256+LF in files order"},
        "external_constraints": {"map_dossier_mutated": False, "live_stacks_tex_mutated": False, "git_used": False, "network_used": False},
        "nonclaims": ["I000033 is proposed but not appended to a mapping dossier in this source-repair transaction.", "The strict-pass Stacks candidate and audit are bound as evidence; this semantic transaction does not claim live insertion."],
        "errors": [],
    }
    manifest_data = pretty(manifest)
    checks = {
        "predecessor identities exact": True,
        "reader and QA bindings exact": True,
        "source decision and ledger IDs unique": True,
        "diplomatic target segment invariant": True,
        "corrected French target segment bound": True,
        "corrected English target segment bound": True,
        "catalog exact six-field patch": True,
        "nodes exact three-field patch": True,
        "occ exact three-field patch": True,
        "exact twelve existing-field changes": True,
        "zero rows appended": True,
        "all node and occurrence IDs preserved": True,
        "thirteen inherited payload files byte-identical": True,
        "manifest payload identities complete": True,
        "I000033 proposal bound without dossier mutation": True,
    }
    validation = {
        "schema": "tohoku-semantic-local-successor-validation-v22",
        "status": "PASS",
        "binding_state": "local_unpublished",
        "contract_id": "D1029-sem-r22-exact-twelve-field-successor",
        "created_utc": CREATED_UTC,
        "successor_execution": manifest["successor_execution"],
        "manifest_sha256": sha(manifest_data),
        "counts": counts,
        "delta_summary": {"changed_tables": 3, "changed_existing_fields": 12, "appended_rows": 0, "unchanged_payload_files": 13, "affected_node_ids": [TARGET_NODE_ID], "affected_occurrence_ids": [TARGET_OCCURRENCE_ID]},
        "checks": checks,
        "errors": [],
    }
    validation_data = pretty(validation)
    candidate["manifest.json"] = manifest_data
    candidate["validation.json"] = validation_data
    return {"files": candidate, "manifest": manifest, "validation": validation}


def write_new(path: Path, data: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(data); handle.flush(); os.fsync(handle.fileno())


def verify(derived: Mapping[str, Any]) -> dict[str, Any]:
    expected = derived["files"]
    actual = sorted(path.name for path in FINAL.iterdir() if path.is_file())
    if actual != sorted(expected):
        raise SemError(f"sem/r22 file surface drifted: {actual}")
    for name, data in expected.items():
        if (FINAL / name).read_bytes() != data:
            raise SemError(f"committed sem/r22 payload differs: {name}")
    return {
        "status": "PASS_COMMITTED_AND_REPLAYED",
        "revision": "sem/r22",
        "manifest": ident(FINAL / "manifest.json", expected["manifest.json"]),
        "validation": ident(FINAL / "validation.json", expected["validation.json"]),
        "delta": derived["validation"]["delta_summary"],
    }


def execute(derived: Mapping[str, Any]) -> dict[str, Any]:
    occupied = [path for path in (FINAL, STAGE, RECOVERY) if os.path.lexists(path)]
    if occupied:
        raise FileExistsError(f"sem/r22 namespace occupied: {occupied}")
    STAGE.mkdir(exist_ok=False)
    try:
        for name, data in sorted(derived["files"].items()):
            write_new(STAGE / name, data)
            if (STAGE / name).read_bytes() != data:
                raise SemError(f"staged semantic readback differs: {name}")
        os.rename(STAGE, FINAL)
        return verify(derived)
    except BaseException:
        if STAGE.exists():
            os.rename(STAGE, RECOVERY)
        raise


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--execute", action="store_true")
    mode.add_argument("--replay", action="store_true")
    args = parser.parse_args(sys.argv[1:] if argv is None else list(argv))
    derived = derive()
    if args.preflight:
        if any(os.path.lexists(path) for path in (FINAL, STAGE, RECOVERY)):
            raise FileExistsError("sem/r22 namespace occupied")
        result = {"status": "READY_NOT_EXECUTED", "revision": "sem/r22", "manifest_sha256": sha(derived["files"]["manifest.json"]), "validation_sha256": sha(derived["files"]["validation.json"]), "delta": derived["validation"]["delta_summary"]}
    elif args.execute:
        result = execute(derived)
    else:
        result = verify(derived)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise SystemExit(1)
