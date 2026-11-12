#!/usr/bin/env python3
"""Build, validate, and atomically admit the D1017 semantic r21 successor."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import os
import re
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


SCRIPT_PATH = Path(__file__).resolve()
TOOLCHAIN_DIR = SCRIPT_PATH.parent
STACKS_ROOT = TOOLCHAIN_DIR.parent.parent
CANONICAL_ROOT = (
    STACKS_ROOT.parent
    / "interlanguage"
    / "03_projects"
    / "language_management"
    / "english_germanic"
    / "03_working_translations"
    / "tohoku_bilingual_canonical_stacks_20260804_r1"
)
CONTRACT_PATH = TOOLCHAIN_DIR / "sem_r21_contract.json"
PREDECESSOR_DIR = CANONICAL_ROOT / "sem" / "r20"
TARGET_DIR = CANONICAL_ROOT / "sem" / "r21"
STAGE_DIR = CANONICAL_ROOT / "sem" / ".r21.d1017.stage"

CONTRACT_ID = "D1017-R001-p185-r20-r42-sem21-v1"
TARGET_VERSION = "local-v068c3r20-sem-r21"
TARGET_PAGE_STATE = "current_r20_visual_gate_closed"
TARGET_CATALOG_ID = "TOHOKU-1957-119-221"
TARGET_NODE_ID = "tohoku:definition:hom-o-and-local-hom"
TARGET_OCCURRENCE_ID = "tohoku:occ:p185:o003"
DECISION_ID = "TOH-P185-COR-002"
SOURCE_CORRECTION_ID = "TOH-SRC-P185-002"
DEFECT_ID = "D1017-R001"

PREDECESSOR_MANIFEST = {
    "path": "sem/r20/manifest.json",
    "bytes": 33263,
    "sha256": "A5ADE906B63382C3071F8EE4908546F010A3F08ED7DC1F6FD8D2C84D9713782D",
}
PREDECESSOR_VALIDATION = {
    "path": "sem/r20/validation.json",
    "bytes": 10529,
    "sha256": "AF76F4B6A8263586F178D2AA82A0E781590F9824F62BF9A8868A8B87406CF863",
}

TABLE_ROW_COUNTS = {
    "bib.csv": 22,
    "catalog.csv": 1,
    "edges.csv": 1479,
    "idmap.csv": 2,
    "nodes.csv": 991,
    "objects.csv": 234,
    "occ.csv": 1036,
    "pages.csv": 103,
    "refdec.csv": 12,
    "refs.csv": 440,
    "resid.csv": 34,
    "stacks.csv": 35,
    "subjects.csv": 17,
    "terms.csv": 909,
    "xwork.csv": 6,
}
CHANGED_TABLES = ("catalog.csv", "nodes.csv", "occ.csv")
UNCHANGED_TABLES = tuple(name for name in TABLE_ROW_COUNTS if name not in CHANGED_TABLES)
UNCHANGED_DATA_FILES = UNCHANGED_TABLES + ("README.md",)
PAYLOAD_NAMES = set(TABLE_ROW_COUNTS) | {"README.md"}

CANONICAL_INPUTS = {
    "source_admission": {
        "path": "production/p185_fix2/check.json",
        "bytes": 5291,
        "sha256": "E54AE998A9D8AB863652521E329731789727DD064B48E6A52CAB83584C802EEA",
    },
    "repair_decisions": {
        "path": "production/p185_fix2/decisions.jsonl",
        "bytes": 3493,
        "sha256": "BB7813EA38AD72B878C4AE825141A82FEF092F8A99FEDDD7397AE705A56D4D4B",
    },
    "repair_dip": {
        "path": "production/p185_fix2/tex/fr_diplomatic/p185.tex",
        "bytes": 3964,
        "sha256": "C95797FF736C53A873F08DC7124460F7EE7E50E5490C656E8F5F6493A784153A",
    },
    "repair_fr": {
        "path": "production/p185_fix2/tex/fr_corrected/p185.tex",
        "bytes": 4298,
        "sha256": "EBE37CBFBE00FA4CA72C21CC4C542D60603A61E92EE446D15C941FA136B20847",
    },
    "repair_en": {
        "path": "production/p185_fix2/tex/en/p185.tex",
        "bytes": 4178,
        "sha256": "9F3F8C932149B3F2ECC9A25C4D4C2D010A48A2CFE6B621CE12BE178CC4DADE60",
    },
    "source_ledger": {
        "path": "SOURCE_CORRECTIONS.jsonl",
        "bytes": 212239,
        "sha256": "31E8894E57B355383B49BB403FAE65B935C81B4C1DAC65C17B20C3C7A6E70439",
    },
    "reader_receipt": {
        "path": "build/v068c3r20/build.json",
        "bytes": 22216,
        "sha256": "BA5D7BFDEA8F733CBA65703C5DA017E26A3FEB417297A975EBCAEFEA41D2BEA1",
    },
    "fr_built_pdf": {
        "path": "build/v068c3r20/fr/main-fr.pdf",
        "bytes": 1417551,
        "sha256": "91EE76111A240E36AC107FCAC9605A5E32E9E9796AAE86AAB495D5F36DB3AFB8",
    },
    "en_built_pdf": {
        "path": "build/v068c3r20/en/main-en.pdf",
        "bytes": 1381128,
        "sha256": "3E78467B441F801DE742584CA9FBE906A886B4B9DD6AA4585315DB9482175AA1",
    },
    "fr_output_pdf": {
        "path": "output/pdf/fr-p119-221-v068c3r20.pdf",
        "bytes": 1417551,
        "sha256": "91EE76111A240E36AC107FCAC9605A5E32E9E9796AAE86AAB495D5F36DB3AFB8",
    },
    "en_output_pdf": {
        "path": "output/pdf/en-p119-221-v068c3r20.pdf",
        "bytes": 1381128,
        "sha256": "3E78467B441F801DE742584CA9FBE906A886B4B9DD6AA4585315DB9482175AA1",
    },
    "qa_receipt": {
        "path": "qa/v68r42/check.json",
        "bytes": 5375,
        "sha256": "C3D039B399FDA3A2232F07A0D33ABB3E07ADEA431182FCEC26F3C8A9DFD703D0",
    },
    "qa_structural": {
        "path": "qa/v68r42/structural.json",
        "bytes": 7900,
        "sha256": "06EBFDCE2E77644BADB3A38606662FEBA4B518AECC99A84BEEE70DA930E71171",
    },
    "qa_page_inventory": {
        "path": "qa/v68r42/page-inventory.csv",
        "bytes": 28257,
        "sha256": "9B2293746E4D169DC4F4B2E738793BA9127A50A2B080CD9BD34A972A9046DA0E",
    },
    "old_dip_p185": {
        "path": "build/v068c3r19/src/dip/p185.tex",
        "bytes": 3964,
        "sha256": "C95797FF736C53A873F08DC7124460F7EE7E50E5490C656E8F5F6493A784153A",
    },
    "old_fr_p185": {
        "path": "build/v068c3r19/src/fr/p185.tex",
        "bytes": 4302,
        "sha256": "85D04A11FF28F109C9006A850A3D9176A6483C2CAC56AA9B849058934B65C54A",
    },
    "old_en_p185": {
        "path": "build/v068c3r19/src/en/p185.tex",
        "bytes": 4183,
        "sha256": "6D15A561E5FCE6D3071672663DE9969249A5D147F08D6DC61A7CD5F3E43A084D",
    },
    "new_dip_p185": {
        "path": "build/v068c3r20/src/dip/p185.tex",
        "bytes": 3964,
        "sha256": "C95797FF736C53A873F08DC7124460F7EE7E50E5490C656E8F5F6493A784153A",
    },
    "new_fr_p185": {
        "path": "build/v068c3r20/src/fr/p185.tex",
        "bytes": 4298,
        "sha256": "EBE37CBFBE00FA4CA72C21CC4C542D60603A61E92EE446D15C941FA136B20847",
    },
    "new_en_p185": {
        "path": "build/v068c3r20/src/en/p185.tex",
        "bytes": 4178,
        "sha256": "9F3F8C932149B3F2ECC9A25C4D4C2D010A48A2CFE6B621CE12BE178CC4DADE60",
    },
}

STACKS_INPUTS = {
    "formalization_design": {
        "path": "tmp/d1017_p185_formalization_design.json",
        "bytes": 8424,
        "sha256": "C1E54BDFB4F52D6761248992D8C669CFB43FB21976A2539063FD893BDEAF43DC",
    },
    "independent_review": {
        "path": "tmp/d1017_stacks_independent_review_r1.json",
        "bytes": 12100,
        "sha256": "E446CBFC413104F7D0D888F795DDB9C3100C87E615CBC1845667E4830A2A15BC",
    },
    "candidate": {
        "path": "tmp/d1017_noncommutative_internal_hom_candidate.tex",
        "bytes": 5063,
        "sha256": "FB6278770580656A6904DC4505A7E69DAB222710D62633937125C557A2E75190",
    },
    "modules_tex": {
        "path": "modules.tex",
        "bytes": 232828,
        "sha256": "EF800D241EBA37CE7099F9B09440228969710988903EE393261C866F902A12F5",
    },
    "modules_pdf": {
        "path": "modules.pdf",
        "bytes": 767323,
        "sha256": "A35B4D3FDD5A8A106A24570FA6E8890BACF45E83BD01B2F949A838F33D311638",
    },
    "modules_log": {
        "path": "modules.log",
        "bytes": 35923,
        "sha256": "862702CB6A31FDCCCE60E025BF894C60E20E53C5F32A80DE19C1D65EF4B01514",
    },
    "output_bindings": {
        "path": "tmp/d1017_p185_repair_toolchain/r20_output_bindings.json",
        "bytes": 1926,
        "sha256": "B126AE869D2C411922284DF0D5A9545D6FC83CD0593DAD783FC7CBE3313B01E7",
    },
    "visual_attestation": {
        "path": "tmp/d1017_p185_repair_toolchain/r42_visual_attestation.json",
        "bytes": 2058,
        "sha256": "FFD8A778DC32F9A31F9239B0B0B788245D44A83E8989B24E6128DC8DC04EE042",
    },
}

SEGMENT_IDENTITIES = {
    "old": {
        "dip": "3BF8F59B6ED631FE86D797C4EB9AE894D860719F49428A62CF5B65009E97AF1D",
        "fr": "3BF8F59B6ED631FE86D797C4EB9AE894D860719F49428A62CF5B65009E97AF1D",
        "en": "9E090A923EF9E902670BAFC4B0DDD1D80012A4EF949240282356176196D561F6",
    },
    "new": {
        "dip": "3BF8F59B6ED631FE86D797C4EB9AE894D860719F49428A62CF5B65009E97AF1D",
        "fr": "3E97451428511EE1FBAAB18FF58FEEF38EA6A1783FC2DEEE5AE52C684098F075",
        "en": "E2AEF6054B1908D55A32194BB68F0274634F5F0724388C498F0A445A617DDE25",
    },
}
LABEL_IDENTITIES = {
    "fr": "B141BE9E78BD010B2B9703800784C7A8D46E50F1CA917D047752786749FD2964",
    "en": "52C23A2532EBEBCEC53AB6C773851FDFBB066591861078C4D681869EADFEE733",
}
DECISION_APPEND = {
    "bytes": 776,
    "sha256": "E5DCC58D900A1F5EB80D8CB7FDE543B7F15B306FED5711754FE50AE7D6AC8A7A",
}
LEDGER_APPEND = {
    "bytes": 1098,
    "sha256": "ED03ED1D5B4597056D798FA1C22624016D5D2A6D568516E000DB38F6BA790B83",
}


class ContractError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(data: bytes) -> dict[str, Any]:
    return {"bytes": len(data), "sha256": sha256(data)}


def file_identity(path: str, data: bytes, role: str | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"path": path, "bytes": len(data), "sha256": sha256(data)}
    if role is not None:
        result["role"] = role
    return result


def pretty_json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def compact_json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def parse_json(data: bytes, label: str) -> Any:
    try:
        return json.loads(data.decode("utf-8"))
    except Exception as exc:
        raise ContractError(f"{label}: invalid UTF-8 JSON: {exc}") from exc


def verify_bytes(data: bytes, spec: Mapping[str, Any], label: str) -> None:
    require(len(data) == spec["bytes"], f"{label}: byte count mismatch")
    require(sha256(data) == spec["sha256"], f"{label}: SHA-256 mismatch")


def read_exact(root: Path, spec: Mapping[str, Any], label: str) -> bytes:
    path = root / str(spec["path"])
    require(path.is_file() and not path.is_symlink(), f"{label}: missing, non-file, or symlink")
    data = path.read_bytes()
    verify_bytes(data, spec, label)
    return data


def csv_rows(data: bytes, label: str) -> tuple[list[str], list[dict[str, str]]]:
    try:
        reader = csv.DictReader(io.StringIO(data.decode("utf-8"), newline=""))
        require(reader.fieldnames is not None, f"{label}: missing CSV header")
        headers = list(reader.fieldnames)
        rows = [dict(row) for row in reader]
        require(all(None not in row for row in rows), f"{label}: surplus CSV fields")
        return headers, rows
    except ContractError:
        raise
    except Exception as exc:
        raise ContractError(f"{label}: invalid CSV: {exc}") from exc


def csv_output(headers: Sequence[str], rows: Iterable[Mapping[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(headers), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def patch_csv(source: bytes, label: str, key: str, key_value: str, updates: Mapping[str, str]) -> bytes:
    headers, rows = csv_rows(source, label)
    matches = [row for row in rows if row.get(key) == key_value]
    require(len(matches) == 1, f"{label}: expected one {key}={key_value}")
    require(set(updates).issubset(headers), f"{label}: unknown update fields")
    matches[0].update({name: str(value) for name, value in updates.items()})
    return csv_output(headers, rows)


def keyed_csv_delta(before: bytes, after: bytes, label: str, key: str) -> list[dict[str, str]]:
    before_headers, before_rows = csv_rows(before, f"{label}:before")
    after_headers, after_rows = csv_rows(after, f"{label}:after")
    require(before_headers == after_headers, f"{label}: header changed")
    require(len(before_rows) == len(after_rows), f"{label}: row count changed")
    require([row[key] for row in before_rows] == [row[key] for row in after_rows], f"{label}: key order changed")
    result: list[dict[str, str]] = []
    for old, new in zip(before_rows, after_rows):
        for field in before_headers:
            if old[field] != new[field]:
                result.append({"key": old[key], "field": field, "before": old[field], "after": new[field]})
    return result


def one_row(data: bytes, label: str, key: str, value: str) -> dict[str, str]:
    _, rows = csv_rows(data, label)
    matches = [row for row in rows if row.get(key) == value]
    require(len(matches) == 1, f"{label}: expected one {key}={value}")
    return matches[0]


def layer_target_sequence(page_bytes: bytes) -> list[str]:
    return re.findall(r"\\LayerTarget\{([^}]+)\}", page_bytes.decode("utf-8"))


def layer_segment(page_bytes: bytes, semantic_id: str) -> bytes:
    marker = f"\\LayerTarget{{{semantic_id}}}".encode("utf-8")
    require(page_bytes.count(marker) == 1, f"{semantic_id}: LayerTarget count is not one")
    start = page_bytes.index(marker) + len(marker)
    end = page_bytes.find(b"\\LayerTarget{", start)
    return page_bytes[start:] if end < 0 else page_bytes[start:end]


def detex(segment: bytes, limit: int = 320) -> str:
    value = segment.decode("utf-8")
    value = re.sub(r"(?m)(?<!\\)%.*$", "", value)
    value = re.sub(r"\\(?:begin|end)\{[^}]+\}", " ", value)
    value = re.sub(r"\\(?:addcontentsline|markboth)\{[^}]*\}(?:\{[^}]*\}){0,2}", " ", value)
    value = re.sub(r"\\(?:SourcePage|TohokuContinuation|TohokuTerminal)\{[^}]*\}", " ", value)
    value = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", value)
    value = value.replace("\\[", " ").replace("\\]", " ")
    value = value.replace("{", " ").replace("}", " ")
    value = value.replace("$", " ").replace("~", " ")
    value = re.sub(r"\\[^A-Za-z\s]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value[:limit]


def aggregate_surface(entries: Sequence[Mapping[str, Any]]) -> tuple[int, str]:
    payload = b"".join(
        str(entry["name"]).encode("utf-8")
        + b"\0"
        + str(entry["bytes"]).encode("ascii")
        + b"\0"
        + str(entry["sha256"]).encode("ascii")
        + b"\n"
        for entry in entries
    )
    return len(payload), sha256(payload)


def jsonl_row(data: bytes, key: str, value: str, label: str) -> bytes:
    matches: list[bytes] = []
    for line in data.splitlines(keepends=True):
        if not line.strip():
            continue
        try:
            row = json.loads(line.decode("utf-8"))
        except Exception as exc:
            raise ContractError(f"{label}: invalid JSONL row: {exc}") from exc
        if row.get(key) == value:
            matches.append(line)
    require(len(matches) == 1, f"{label}: expected one {key}={value}")
    return matches[0]


def load_contract() -> tuple[dict[str, Any], dict[str, Any]]:
    require(CONTRACT_PATH.is_file() and not CONTRACT_PATH.is_symlink(), "semantic contract missing or unsafe")
    contract_bytes = CONTRACT_PATH.read_bytes()
    contract = parse_json(contract_bytes, "semantic contract")
    require(contract.get("schema") == "d1017-sem-r21-contract-v1", "semantic contract schema mismatch")
    require(contract.get("contract_id") == CONTRACT_ID, "semantic contract ID mismatch")
    script_spec = contract.get("script")
    require(isinstance(script_spec, dict), "semantic contract script pin missing")
    require(script_spec.get("path") == "tmp/d1017_p185_repair_toolchain/sem_r21.py", "semantic contract script path mismatch")
    script_bytes = SCRIPT_PATH.read_bytes()
    verify_bytes(script_bytes, script_spec, "semantic r21 script")
    require(contract.get("predecessor") == PREDECESSOR_MANIFEST, "semantic contract predecessor mismatch")
    require(contract.get("target") == "sem/r21", "semantic contract target mismatch")
    return contract, {
        "script": file_identity(script_spec["path"], script_bytes, "contract_read_hash_then_execute_same_bytes"),
        "contract": file_identity(
            "tmp/d1017_p185_repair_toolchain/sem_r21_contract.json",
            contract_bytes,
            "external_identity_pin_for_semantic_script",
        ),
    }


def _input_entry(prefix: str, spec: Mapping[str, Any], data: bytes, role: str) -> dict[str, Any]:
    return file_identity(f"{prefix}{spec['path']}", data, role)


def load_snapshots(require_target_absent: bool) -> dict[str, Any]:
    contract, execution = load_contract()
    if require_target_absent:
        require(not TARGET_DIR.exists(), "sem/r21 target already exists")
        require(not STAGE_DIR.exists(), "owned semantic r21 stage already exists")

    predecessor_manifest_bytes = read_exact(CANONICAL_ROOT, PREDECESSOR_MANIFEST, "predecessor manifest")
    predecessor_validation_bytes = read_exact(CANONICAL_ROOT, PREDECESSOR_VALIDATION, "predecessor validation")
    predecessor_manifest = parse_json(predecessor_manifest_bytes, "predecessor manifest")
    predecessor_validation = parse_json(predecessor_validation_bytes, "predecessor validation")
    require(predecessor_manifest.get("schema") == "tohoku-semantic-local-successor-manifest-v20", "r20 manifest schema mismatch")
    require(predecessor_manifest.get("version") == "local-v068c3r19-sem-r20", "r20 manifest version mismatch")
    require(predecessor_validation.get("status") == "PASS" and predecessor_validation.get("errors") == [], "r20 validation not PASS")
    require(predecessor_validation.get("manifest_sha256") == PREDECESSOR_MANIFEST["sha256"], "r20 validation/manifest mismatch")

    entries = predecessor_manifest.get("files")
    require(isinstance(entries, list) and len(entries) == 16, "r20 payload manifest surface mismatch")
    require({entry.get("name") for entry in entries if isinstance(entry, dict)} == PAYLOAD_NAMES, "r20 payload names mismatch")
    predecessor_files: dict[str, bytes] = {}
    for entry in entries:
        require(isinstance(entry, dict), "r20 payload entry is not an object")
        name = str(entry.get("name", ""))
        require(name and Path(name).name == name, f"unsafe r20 payload name: {name}")
        predecessor_files[name] = read_exact(
            CANONICAL_ROOT,
            {"path": f"sem/r20/{name}", "bytes": entry["bytes"], "sha256": entry["sha256"]},
            f"r20/{name}",
        )
    predecessor_aggregate = aggregate_surface(entries)
    require(predecessor_aggregate == (1297, "8D3C60D10CA41BACBEBC801C89374ACC8E90D842EA93C3935EE36D049F773B97"), "r20 payload aggregate mismatch")
    for name, expected_rows in TABLE_ROW_COUNTS.items():
        _, rows = csv_rows(predecessor_files[name], f"r20/{name}")
        require(len(rows) == expected_rows, f"r20/{name}: row count mismatch")

    canonical_bytes = {
        name: read_exact(CANONICAL_ROOT, spec, name)
        for name, spec in CANONICAL_INPUTS.items()
    }
    stacks_bytes = {
        name: read_exact(STACKS_ROOT, spec, name)
        for name, spec in STACKS_INPUTS.items()
    }

    source_receipt = parse_json(canonical_bytes["source_admission"], "source admission")
    require(source_receipt.get("status") == "PASS" and source_receipt.get("errors") == [], "source admission not PASS")
    require(source_receipt.get("defect_id") == DEFECT_ID, "source admission defect mismatch")
    require(source_receipt.get("decision_id") == DECISION_ID, "source admission decision mismatch")
    require(source_receipt.get("source_correction_id") == SOURCE_CORRECTION_ID, "source admission correction mismatch")
    require(source_receipt.get("production_successor") == "production/p185_fix2", "source successor mismatch")

    decision_row = jsonl_row(canonical_bytes["repair_decisions"], "decision_id", DECISION_ID, "repair decisions")
    verify_bytes(decision_row, DECISION_APPEND, "repair decision append")
    ledger_row = jsonl_row(canonical_bytes["source_ledger"], "decision_id", SOURCE_CORRECTION_ID, "source corrections")
    verify_bytes(ledger_row, LEDGER_APPEND, "source correction append")

    reader_receipt = parse_json(canonical_bytes["reader_receipt"], "reader receipt")
    require(reader_receipt.get("schema") == "tohoku-v068-staged-successor-build-v1", "reader receipt schema mismatch")
    require(reader_receipt.get("status") == "PASS" and reader_receipt.get("errors") == [], "reader receipt not PASS")
    require(reader_receipt.get("revision") == "v068c3r20", "reader revision mismatch")
    require(reader_receipt.get("predecessor_revision") == "v068c3r19", "reader predecessor mismatch")
    surface = reader_receipt.get("revision_surface_contract", {})
    require(surface.get("replaced_staged_paths") == ["en/p185.tex", "fr/p185.tex"], "reader replaced-path surface mismatch")
    require(surface.get("byte_identical_staged_files") == 541, "reader unchanged staged-file count mismatch")
    require(surface.get("other_staged_source_changes") == 0, "reader unrelated source changes detected")
    require(reader_receipt.get("pdfs", {}).get("fr", {}).get("sha256") == CANONICAL_INPUTS["fr_output_pdf"]["sha256"], "reader French PDF binding mismatch")
    require(reader_receipt.get("pdfs", {}).get("en", {}).get("sha256") == CANONICAL_INPUTS["en_output_pdf"]["sha256"], "reader English PDF binding mismatch")
    require(canonical_bytes["fr_built_pdf"] == canonical_bytes["fr_output_pdf"], "French built/output PDFs differ")
    require(canonical_bytes["en_built_pdf"] == canonical_bytes["en_output_pdf"], "English built/output PDFs differ")

    qa_receipt = parse_json(canonical_bytes["qa_receipt"], "QA receipt")
    require(qa_receipt.get("status") == "PASS" and qa_receipt.get("errors") == [], "QA receipt not PASS")
    require(qa_receipt.get("qa_revision") == "v68r42", "QA revision mismatch")
    require(qa_receipt.get("reader_revision") == "v068c3r20", "QA reader binding mismatch")
    require(qa_receipt.get("stable_id") == "tohoku:reader-qa:v68r42:v068c3r20", "QA stable ID mismatch")
    conclusion = qa_receipt.get("conclusion", {})
    require(conclusion.get("reader_successor_accepted") is True, "QA reader acceptance missing")
    require(conclusion.get("pdf_pair_accepted") is True, "QA PDF-pair acceptance missing")
    require(conclusion.get("visual_review_accepted") is True, "QA visual acceptance missing")
    require(conclusion.get("blockers") == [], "QA blockers are not empty")

    design = parse_json(stacks_bytes["formalization_design"], "formalization design")
    review = parse_json(stacks_bytes["independent_review"], "independent review")
    require(design.get("formalization_id") == "D1017", "formalization design ID mismatch")
    require(design.get("status") == "STACKS_BUILD_PASS_SOURCE_REPAIR_AND_MAPPING_REQUIRED", "formalization design state mismatch")
    require(review.get("formalization_id") == "D1017", "independent review ID mismatch")
    require(review.get("status") == "STRICT_PASS_STACKS_FORMALIZATION", "independent review state mismatch")
    require(stacks_bytes["modules_tex"].count(stacks_bytes["candidate"]) == 1, "candidate not inserted exactly once in modules.tex")
    require(stacks_bytes["modules_tex"].count(b"\\label{definition-hom-left-modules}") == 1, "definition label multiplicity mismatch")
    require(stacks_bytes["modules_tex"].count(b"\\label{lemma-sheaf-hom-left-modules}") == 1, "lemma label multiplicity mismatch")
    require(b"LaTeX Warning: There were undefined references" not in stacks_bytes["modules_log"], "modules log has undefined references")

    old_pages = {
        "dip": canonical_bytes["old_dip_p185"],
        "fr": canonical_bytes["old_fr_p185"],
        "en": canonical_bytes["old_en_p185"],
    }
    new_pages = {
        "dip": canonical_bytes["new_dip_p185"],
        "fr": canonical_bytes["new_fr_p185"],
        "en": canonical_bytes["new_en_p185"],
    }
    require(new_pages["dip"] == canonical_bytes["repair_dip"], "built diplomatic p185 differs from admitted repair")
    require(new_pages["fr"] == canonical_bytes["repair_fr"], "built French p185 differs from admitted repair")
    require(new_pages["en"] == canonical_bytes["repair_en"], "built English p185 differs from admitted repair")
    sequences = [
        layer_target_sequence(page)
        for page in [*old_pages.values(), *new_pages.values()]
    ]
    require(len(sequences[0]) == 13 and all(seq == sequences[0] for seq in sequences), "p185 LayerTarget sequence changed")
    require(TARGET_NODE_ID in sequences[0], "target node absent from p185")

    old_segments = {layer: layer_segment(page, TARGET_NODE_ID) for layer, page in old_pages.items()}
    new_segments = {layer: layer_segment(page, TARGET_NODE_ID) for layer, page in new_pages.items()}
    for state, segments in (("old", old_segments), ("new", new_segments)):
        for layer, segment in segments.items():
            require(sha256(segment) == SEGMENT_IDENTITIES[state][layer], f"{state} {layer} segment mismatch")
    require(new_segments["dip"] == old_segments["dip"], "diplomatic target segment changed")
    require(new_segments["fr"] != old_segments["fr"], "corrected French target segment did not change")
    require(new_segments["en"] != old_segments["en"], "English target segment did not change")
    require(new_segments["fr"].count(b"\\Gamma(O^\\natural)") == 1, "corrected French scalar ring multiplicity mismatch")
    require(new_segments["en"].count(b"\\Gamma(O^\\natural)") == 1, "corrected English scalar ring multiplicity mismatch")
    witness_id = "tohoku:remark:sheaf-hom-o:center-module"
    for layer in ("dip", "fr", "en"):
        require(
            layer_segment(old_pages[layer], witness_id) == layer_segment(new_pages[layer], witness_id),
            f"{layer} internal center-sheaf witness changed",
        )

    labels = {layer: detex(new_segments[layer]) for layer in ("fr", "en")}
    for layer, label in labels.items():
        require(sha256(label.encode("utf-8")) == LABEL_IDENTITIES[layer], f"{layer} semantic label mismatch")

    old_node = one_row(predecessor_files["nodes.csv"], "r20/nodes.csv", "node_id", TARGET_NODE_ID)
    old_occ = one_row(predecessor_files["occ.csv"], "r20/occ.csv", "occurrence_id", TARGET_OCCURRENCE_ID)
    require(old_node["provenance"] == "src/targets.csv + exact aligned layer segments", "r20 target provenance mismatch")
    require(old_occ["decision_path"] == "build/v068c3r13/src/dec/p185.jsonl", "r20 target decision path mismatch")
    for layer in ("dip", "fr", "en"):
        require(old_occ[f"{layer}_sha256"] == SEGMENT_IDENTITIES["old"][layer], f"r20 occurrence {layer} mismatch")

    provenance = (
        "production/p185_fix2/decisions.jsonl#TOH-P185-COR-002;"
        f"decision_row_sha256={DECISION_APPEND['sha256']};"
        f"dip_segment_sha256={SEGMENT_IDENTITIES['new']['dip']};"
        f"fr_segment_sha256={SEGMENT_IDENTITIES['new']['fr']};"
        f"en_segment_sha256={SEGMENT_IDENTITIES['new']['en']};"
        "SOURCE_CORRECTIONS.jsonl#TOH-SRC-P185-002;defect=D1017-R001"
    )

    inputs = [
        file_identity(PREDECESSOR_MANIFEST["path"], predecessor_manifest_bytes, "semantic_predecessor_manifest"),
        file_identity(PREDECESSOR_VALIDATION["path"], predecessor_validation_bytes, "semantic_predecessor_validation"),
    ]
    inputs.extend(
        _input_entry("", CANONICAL_INPUTS[name], canonical_bytes[name], name)
        for name in sorted(CANONICAL_INPUTS)
    )
    inputs.extend(
        _input_entry("stacks-ftg/", STACKS_INPUTS[name], stacks_bytes[name], name)
        for name in sorted(STACKS_INPUTS)
    )

    return {
        "contract": contract,
        "execution": execution,
        "predecessor_manifest": predecessor_manifest,
        "predecessor_files": predecessor_files,
        "canonical_bytes": canonical_bytes,
        "stacks_bytes": stacks_bytes,
        "marker_sequence": sequences[0],
        "segments": {layer: identity(new_segments[layer]) for layer in ("dip", "fr", "en")},
        "labels": labels,
        "label_identities": {layer: identity(labels[layer].encode("utf-8")) for layer in ("fr", "en")},
        "provenance": provenance,
        "inputs": inputs,
    }


def _file_entry(name: str, data: bytes) -> dict[str, Any]:
    return {"name": name, "bytes": len(data), "sha256": sha256(data)}


def _changed_table(predecessor: Mapping[str, bytes], successor: Mapping[str, bytes], name: str, key: str) -> dict[str, Any]:
    deltas = keyed_csv_delta(predecessor[name], successor[name], name, key)
    return {
        "mode": "exact_existing_row_field_patch",
        "key_field": key,
        "field_deltas": deltas,
        "predecessor": identity(predecessor[name]),
        "successor": identity(successor[name]),
        "rows": TABLE_ROW_COUNTS[name],
    }


def build_candidate(snapshots: Mapping[str, Any]) -> dict[str, bytes]:
    predecessor = snapshots["predecessor_files"]
    candidate = dict(predecessor)
    candidate["catalog.csv"] = patch_csv(
        predecessor["catalog.csv"],
        "catalog.csv",
        "catalog_id",
        TARGET_CATALOG_ID,
        {
            "french_reader": "output/pdf/fr-p119-221-v068c3r20.pdf",
            "french_sha256": CANONICAL_INPUTS["fr_output_pdf"]["sha256"],
            "english_reader": "output/pdf/en-p119-221-v068c3r20.pdf",
            "english_sha256": CANONICAL_INPUTS["en_output_pdf"]["sha256"],
            "version": TARGET_VERSION,
            "page_state": TARGET_PAGE_STATE,
        },
    )
    candidate["nodes.csv"] = patch_csv(
        predecessor["nodes.csv"],
        "nodes.csv",
        "node_id",
        TARGET_NODE_ID,
        {
            "fr_label": snapshots["labels"]["fr"],
            "en_label": snapshots["labels"]["en"],
            "provenance": snapshots["provenance"],
        },
    )
    candidate["occ.csv"] = patch_csv(
        predecessor["occ.csv"],
        "occ.csv",
        "occurrence_id",
        TARGET_OCCURRENCE_ID,
        {
            "decision_path": "production/p185_fix2/decisions.jsonl",
            "fr_sha256": snapshots["segments"]["fr"]["sha256"],
            "en_sha256": snapshots["segments"]["en"]["sha256"],
        },
    )
    for name in UNCHANGED_DATA_FILES:
        require(candidate[name] == predecessor[name], f"{name}: inherited bytes changed")

    changed_tables = {
        "catalog.csv": _changed_table(predecessor, candidate, "catalog.csv", "catalog_id"),
        "nodes.csv": _changed_table(predecessor, candidate, "nodes.csv", "node_id"),
        "occ.csv": _changed_table(predecessor, candidate, "occ.csv", "occurrence_id"),
    }
    unchanged_tables = [
        {
            "name": name,
            "bytes": len(candidate[name]),
            "sha256": sha256(candidate[name]),
            "rows": TABLE_ROW_COUNTS[name],
        }
        for name in UNCHANGED_TABLES
    ]
    unchanged_files = [_file_entry(name, candidate[name]) for name in UNCHANGED_DATA_FILES]
    source_sequence = copy.deepcopy(snapshots["predecessor_manifest"]["source_sequence_contract"])
    require(source_sequence.get("raw_reader", {}).get("reader_revision") == "v068c3r19", "r20 source reader mismatch")
    source_sequence["raw_reader"]["reader_revision"] = "v068c3r20"

    file_entries = [_file_entry(name, candidate[name]) for name in sorted(candidate)]
    aggregate_bytes, aggregate_sha = aggregate_surface(file_entries)
    manifest = {
        "schema": "tohoku-semantic-local-successor-manifest-v21",
        "corpus": "Grothendieck Tohoku paper",
        "scope": "printed pp.119-221",
        "version": TARGET_VERSION,
        "binding_state": "local_unpublished",
        "record_binding": copy.deepcopy(snapshots["predecessor_manifest"]["record_binding"]),
        "inputs": snapshots["inputs"],
        "successor_execution": snapshots["execution"],
        "reader_binding": {
            "revision": "v068c3r20",
            "receipt": CANONICAL_INPUTS["reader_receipt"],
            "french_pdf": {
                **CANONICAL_INPUTS["fr_output_pdf"],
                "catalog_path": "output/pdf/fr-p119-221-v068c3r20.pdf",
            },
            "english_pdf": {
                **CANONICAL_INPUTS["en_output_pdf"],
                "catalog_path": "output/pdf/en-p119-221-v068c3r20.pdf",
            },
            "qa_revision": "v68r42",
            "qa_receipt": CANONICAL_INPUTS["qa_receipt"],
            "qa_structural": CANONICAL_INPUTS["qa_structural"],
            "qa_page_inventory": CANONICAL_INPUTS["qa_page_inventory"],
            "visual_attestation": {
                **STACKS_INPUTS["visual_attestation"],
                "path": "stacks-ftg/" + STACKS_INPUTS["visual_attestation"]["path"],
            },
        },
        "source_repair_binding": {
            "successor": "production/p185_fix2",
            "receipt": CANONICAL_INPUTS["source_admission"],
            "decisions": CANONICAL_INPUTS["repair_decisions"],
            "decision_id": DECISION_ID,
            "decision_append": DECISION_APPEND,
            "source_ledger": CANONICAL_INPUTS["source_ledger"],
            "source_correction_id": SOURCE_CORRECTION_ID,
            "source_correction_append": LEDGER_APPEND,
            "defect_id": DEFECT_ID,
        },
        "stacks_formalization_binding": {
            "formalization_id": "D1017",
            "design": {**STACKS_INPUTS["formalization_design"], "path": "stacks-ftg/" + STACKS_INPUTS["formalization_design"]["path"]},
            "independent_review": {**STACKS_INPUTS["independent_review"], "path": "stacks-ftg/" + STACKS_INPUTS["independent_review"]["path"]},
            "candidate": {**STACKS_INPUTS["candidate"], "path": "stacks-ftg/" + STACKS_INPUTS["candidate"]["path"]},
            "modules_tex": {**STACKS_INPUTS["modules_tex"], "path": "stacks-ftg/" + STACKS_INPUTS["modules_tex"]["path"]},
            "modules_pdf": {**STACKS_INPUTS["modules_pdf"], "path": "stacks-ftg/" + STACKS_INPUTS["modules_pdf"]["path"]},
            "labels": [
                "modules-definition-hom-left-modules",
                "modules-lemma-sheaf-hom-left-modules",
            ],
            "result": "STRICT_PASS_STACKS_FORMALIZATION",
        },
        "semantic_admission": {
            "new_layer_targets": 0,
            "layer_target_count": len(snapshots["marker_sequence"]),
            "layer_target_sequence": snapshots["marker_sequence"],
            "affected_existing_node_ids": [TARGET_NODE_ID],
            "affected_existing_occurrence_ids": [TARGET_OCCURRENCE_ID],
            "segments": snapshots["segments"],
            "labels": snapshots["labels"],
            "label_identities": snapshots["label_identities"],
            "provenance": snapshots["provenance"],
            "correction": "replace the printed global-center scalar claim in corrected French and English with Gamma(O^natural), while preserving the diplomatic layer",
        },
        "stable_id_replay": {
            "predecessor_node_ids_reused": 991,
            "new_node_ids": [],
            "predecessor_occurrence_ids_reused": 1036,
            "new_occurrence_ids": [],
            "predecessor_candidate_ids_reused": 440,
            "new_candidate_ids": [],
            "predecessor_edge_ids_reused": 1479,
            "new_edge_ids": [],
        },
        "source_sequence_contract": source_sequence,
        "table_delta_oracle": {
            "predecessor": PREDECESSOR_MANIFEST,
            "changed_table_count": 3,
            "changed_existing_field_count": 12,
            "appended_row_count": 0,
            "changed_tables": changed_tables,
            "unchanged_table_count": len(unchanged_tables),
            "unchanged_tables": unchanged_tables,
            "unchanged_inherited_file_count": len(unchanged_files),
            "unchanged_inherited_files": unchanged_files,
            "all_predecessor_node_and_occurrence_ids_invariant": True,
            "all_predecessor_reference_and_edge_ids_invariant": True,
            "terms_objects_subjects_and_readme_byte_identical": True,
        },
        "counts": copy.deepcopy(snapshots["predecessor_manifest"]["counts"]),
        "files": file_entries,
        "file_surface": {
            "records": len(file_entries),
            "bytes": sum(entry["bytes"] for entry in file_entries),
            "aggregate_manifest_bytes": aggregate_bytes,
            "aggregate_sha256": aggregate_sha,
            "algorithm": "name+NUL+decimal_bytes+NUL+uppercase_sha256+LF in files order",
        },
        "external_constraints": {
            "github": {
                "status": "temporarily_unavailable",
                "cause": "account security suspension reported after VPN use; support ticket filed",
                "effect": "Continue local production and QA; defer GitHub-only actions; this is not a local-work blocker.",
            }
        },
        "nonclaims": [
            "No release, publication, DOI, remote readback, Git mutation, GitHub action, rights determination, official Stacks tag, or mapping resolution is claimed.",
            "No semantic row outside catalog.csv, nodes.csv, and occ.csv changes.",
            "The p.185 diplomatic layer, LayerTarget identities, and LayerTarget order remain unchanged.",
            "No new semantic target, occurrence, reference candidate, edge, residual, term, object, subject, bibliography, or cross-work row is created.",
        ],
        "errors": [],
    }
    candidate["manifest.json"] = pretty_json_bytes(manifest)
    return candidate


def validate_candidate(snapshots: Mapping[str, Any], candidate: Mapping[str, bytes]) -> bytes:
    checks: dict[str, bool] = {}

    def check(condition: bool, message: str) -> None:
        require(condition, message)
        checks[message] = True

    predecessor = snapshots["predecessor_files"]
    check(set(candidate) == PAYLOAD_NAMES | {"manifest.json"}, "exact r21 pre-validation payload surface")
    for name in UNCHANGED_DATA_FILES:
        check(candidate[name] == predecessor[name], f"unchanged byte identity: {name}")
    for name, expected_rows in TABLE_ROW_COUNTS.items():
        before_headers, before_rows = csv_rows(predecessor[name], f"r20/{name}")
        after_headers, after_rows = csv_rows(candidate[name], f"r21/{name}")
        check(before_headers == after_headers, f"{name}: header invariant")
        check(len(after_rows) == expected_rows, f"{name}: row count invariant")
        if name not in CHANGED_TABLES:
            check(after_rows == before_rows, f"{name}: inherited rows invariant")

    catalog_delta = keyed_csv_delta(predecessor["catalog.csv"], candidate["catalog.csv"], "catalog.csv", "catalog_id")
    nodes_delta = keyed_csv_delta(predecessor["nodes.csv"], candidate["nodes.csv"], "nodes.csv", "node_id")
    occ_delta = keyed_csv_delta(predecessor["occ.csv"], candidate["occ.csv"], "occ.csv", "occurrence_id")
    check(
        {row["field"] for row in catalog_delta}
        == {"french_reader", "french_sha256", "english_reader", "english_sha256", "version", "page_state"},
        "catalog: exact six-field patch",
    )
    check({row["field"] for row in nodes_delta} == {"fr_label", "en_label", "provenance"}, "nodes: exact three-field patch")
    check({row["field"] for row in occ_delta} == {"decision_path", "fr_sha256", "en_sha256"}, "occ: exact three-field patch")
    check(len(catalog_delta) == 6 and len(nodes_delta) == 3 and len(occ_delta) == 3, "exact twelve existing-field changes")
    check(all(row["key"] == TARGET_CATALOG_ID for row in catalog_delta), "catalog: only target row changed")
    check(all(row["key"] == TARGET_NODE_ID for row in nodes_delta), "nodes: only target row changed")
    check(all(row["key"] == TARGET_OCCURRENCE_ID for row in occ_delta), "occ: only target row changed")

    catalog = one_row(candidate["catalog.csv"], "r21/catalog.csv", "catalog_id", TARGET_CATALOG_ID)
    check(catalog["french_reader"] == "output/pdf/fr-p119-221-v068c3r20.pdf", "catalog: French reader path bound")
    check(catalog["english_reader"] == "output/pdf/en-p119-221-v068c3r20.pdf", "catalog: English reader path bound")
    check(catalog["french_sha256"] == CANONICAL_INPUTS["fr_output_pdf"]["sha256"], "catalog: French PDF hash bound")
    check(catalog["english_sha256"] == CANONICAL_INPUTS["en_output_pdf"]["sha256"], "catalog: English PDF hash bound")
    check(catalog["version"] == TARGET_VERSION and catalog["page_state"] == TARGET_PAGE_STATE, "catalog: successor version/page state")

    node = one_row(candidate["nodes.csv"], "r21/nodes.csv", "node_id", TARGET_NODE_ID)
    check(node["fr_label"] == snapshots["labels"]["fr"], "node: corrected French label bound")
    check(node["en_label"] == snapshots["labels"]["en"], "node: corrected English label bound")
    check(node["provenance"] == snapshots["provenance"], "node: exact repair/formalization provenance bound")

    occurrence = one_row(candidate["occ.csv"], "r21/occ.csv", "occurrence_id", TARGET_OCCURRENCE_ID)
    check(occurrence["decision_path"] == "production/p185_fix2/decisions.jsonl", "occurrence: repair decision path bound")
    check(occurrence["dip_sha256"] == SEGMENT_IDENTITIES["new"]["dip"], "occurrence: diplomatic hash invariant")
    check(occurrence["fr_sha256"] == SEGMENT_IDENTITIES["new"]["fr"], "occurrence: corrected French hash bound")
    check(occurrence["en_sha256"] == SEGMENT_IDENTITIES["new"]["en"], "occurrence: English hash bound")

    manifest = parse_json(candidate["manifest.json"], "r21 manifest")
    check(manifest.get("schema") == "tohoku-semantic-local-successor-manifest-v21", "manifest schema")
    check(manifest.get("version") == TARGET_VERSION and manifest.get("binding_state") == "local_unpublished", "manifest version/local binding")
    check(manifest.get("errors") == [], "manifest errors empty")
    check(manifest.get("successor_execution") == snapshots["execution"], "manifest exact execution identities")
    check(manifest.get("source_repair_binding", {}).get("decision_id") == DECISION_ID, "manifest repair decision binding")
    check(manifest.get("source_repair_binding", {}).get("source_correction_id") == SOURCE_CORRECTION_ID, "manifest source correction binding")
    check(manifest.get("stacks_formalization_binding", {}).get("formalization_id") == "D1017", "manifest Stacks formalization binding")
    check(manifest.get("semantic_admission", {}).get("affected_existing_node_ids") == [TARGET_NODE_ID], "manifest affected node allocation")
    check(manifest.get("semantic_admission", {}).get("affected_existing_occurrence_ids") == [TARGET_OCCURRENCE_ID], "manifest affected occurrence allocation")
    check(manifest.get("semantic_admission", {}).get("new_layer_targets") == 0, "manifest zero new targets")
    check(manifest.get("source_sequence_contract", {}).get("raw_reader", {}).get("reader_revision") == "v068c3r20", "manifest reader revision transition")
    check(manifest.get("counts") == snapshots["predecessor_manifest"]["counts"], "manifest count oracle invariant")

    expected_entries = [_file_entry(name, candidate[name]) for name in sorted(PAYLOAD_NAMES)]
    check(manifest.get("files") == expected_entries, "manifest payload file identities")
    aggregate_bytes, aggregate_sha = aggregate_surface(expected_entries)
    surface = manifest.get("file_surface", {})
    check(surface.get("records") == 16 and surface.get("bytes") == sum(entry["bytes"] for entry in expected_entries), "manifest file surface counts")
    check(surface.get("aggregate_manifest_bytes") == aggregate_bytes and surface.get("aggregate_sha256") == aggregate_sha, "manifest aggregate file surface")

    oracle = manifest.get("table_delta_oracle", {})
    check(oracle.get("changed_table_count") == 3, "manifest changed table count")
    check(oracle.get("changed_existing_field_count") == 12 and oracle.get("appended_row_count") == 0, "manifest exact delta cardinality")
    check(oracle.get("unchanged_table_count") == len(UNCHANGED_TABLES), "manifest unchanged table count")
    check(oracle.get("all_predecessor_node_and_occurrence_ids_invariant") is True, "manifest node/occurrence ID invariant")
    check(oracle.get("all_predecessor_reference_and_edge_ids_invariant") is True, "manifest reference/edge ID invariant")
    check(manifest.get("external_constraints", {}).get("github", {}).get("status") == "temporarily_unavailable", "GitHub constraint noted without local hold")

    validation = {
        "schema": "tohoku-semantic-local-successor-validation-v21",
        "status": "PASS",
        "binding_state": "local_unpublished",
        "contract_id": CONTRACT_ID,
        "successor_execution": snapshots["execution"],
        "manifest_sha256": sha256(candidate["manifest.json"]),
        "counts": copy.deepcopy(snapshots["predecessor_manifest"]["counts"]),
        "table_projections": {
            name: {"rows": TABLE_ROW_COUNTS[name], "bytes": len(candidate[name]), "sha256": sha256(candidate[name])}
            for name in sorted(TABLE_ROW_COUNTS)
        },
        "delta_summary": {
            "changed_tables": 3,
            "changed_existing_fields": 12,
            "appended_rows": 0,
            "affected_node_ids": [TARGET_NODE_ID],
            "affected_occurrence_ids": [TARGET_OCCURRENCE_ID],
            "unchanged_payload_files": list(UNCHANGED_DATA_FILES),
        },
        "checks": checks,
        "external_constraints": copy.deepcopy(manifest["external_constraints"]),
        "nonclaims": [
            "No release, publication, DOI, remote readback, Git mutation, GitHub action, rights determination, official Stacks tag, or mapping resolution is claimed.",
            "No semantic row outside catalog.csv, nodes.csv, and occ.csv changes.",
            "The reader, QA, source repair, and Stacks formalization inputs are consumed byte-exactly and remain unmodified.",
        ],
        "errors": [],
    }
    return pretty_json_bytes(validation)


def assembled_candidate(require_target_absent: bool) -> tuple[dict[str, Any], dict[str, bytes]]:
    snapshots = load_snapshots(require_target_absent)
    candidate = build_candidate(snapshots)
    candidate["validation.json"] = validate_candidate(snapshots, candidate)
    require(set(candidate) == PAYLOAD_NAMES | {"manifest.json", "validation.json"}, "exact final r21 surface mismatch")
    return snapshots, candidate


def output_summary(status: str, candidate: Mapping[str, bytes]) -> dict[str, Any]:
    return {
        "status": status,
        "target": "sem/r21",
        "files": len(candidate),
        "bytes": sum(len(data) for data in candidate.values()),
        "manifest": identity(candidate["manifest.json"]),
        "validation": identity(candidate["validation.json"]),
        "catalog": identity(candidate["catalog.csv"]),
        "nodes": identity(candidate["nodes.csv"]),
        "occ": identity(candidate["occ.csv"]),
        "changed_existing_fields": 12,
        "new_rows": 0,
        "github": "temporarily_unavailable_local_work_continues",
    }


def preflight() -> None:
    _, candidate = assembled_candidate(True)
    print(json.dumps(output_summary("PASS_PREFLIGHT", candidate), indent=2))


def execute() -> None:
    _, candidate = assembled_candidate(True)
    STAGE_DIR.mkdir(parents=False, exist_ok=False)
    for name in sorted(candidate):
        path = STAGE_DIR / name
        with path.open("xb") as handle:
            handle.write(candidate[name])
            handle.flush()
            os.fsync(handle.fileno())
    require({path.name for path in STAGE_DIR.iterdir()} == set(candidate), "staged r21 surface mismatch")
    for name, expected in candidate.items():
        require((STAGE_DIR / name).read_bytes() == expected, f"staged r21 readback mismatch: {name}")
    require(not TARGET_DIR.exists(), "sem/r21 appeared before promotion")
    STAGE_DIR.rename(TARGET_DIR)
    require(TARGET_DIR.is_dir() and not TARGET_DIR.is_symlink(), "promoted r21 is not a plain directory")
    require({path.name for path in TARGET_DIR.iterdir()} == set(candidate), "promoted r21 surface mismatch")
    for name, expected in candidate.items():
        require((TARGET_DIR / name).read_bytes() == expected, f"promoted r21 readback mismatch: {name}")
    print(json.dumps(output_summary("PASS_COMMITTED", candidate), indent=2))


def replay() -> None:
    require(TARGET_DIR.is_dir() and not TARGET_DIR.is_symlink(), "sem/r21 target missing or unsafe")
    require(not STAGE_DIR.exists(), "owned semantic r21 stage unexpectedly exists")
    _, candidate = assembled_candidate(False)
    require({path.name for path in TARGET_DIR.iterdir()} == set(candidate), "final r21 replay surface mismatch")
    for name, expected in candidate.items():
        require((TARGET_DIR / name).read_bytes() == expected, f"final r21 replay mismatch: {name}")
    print(json.dumps(output_summary("PASS_REPLAY", candidate), indent=2))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("preflight", "execute", "replay"))
    args = parser.parse_args()
    try:
        if args.mode == "preflight":
            preflight()
        elif args.mode == "execute":
            execute()
        else:
            replay()
        return 0
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
