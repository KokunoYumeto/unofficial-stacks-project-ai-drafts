#!/usr/bin/env python3
"""Independent bounded validator for the no-overwrite Tohoku r52 successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r51"
TARGET = ROOT / "tohoku_r52"
STAGE = ROOT / ".tohoku-r52-txn"
R51_VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r51.py"
EXPECTED_R51_VALIDATOR = (
    71750,
    "3ABAA38045E610ADF74087FEC22401F42C50ED957FCB85DAC4D8C08CA3636C63",
)
D1009_AUDIT = ROOT / "D1009_CHECK.json"
EXPECTED_D1009_AUDIT = (
    16871,
    "B23A19372E6F055FE2D24FB59B89689651697CFAE1AC77B3878D4CADF2827E80",
)
EXPECTED_PYTHON = Path(r"user\miniconda3\python.exe")
EXPECTED_PYTHON_IDENTITY = (
    104264,
    "7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264",
)

EXPECTED_RUNTIME = {
    "fga/__pycache__/mkidx.cpython-313.pyc": (21123, "A78A1E45C6EB3960139B1D2A8AF42E5B10768034F0A87274448EBA69779BD424"),
    "fga/__pycache__/mkmap.cpython-313.pyc": (26471, "1AA6B79FFE873AB6C2E58FF2A9826DE6FDB6B1DD69A8D3473FD5F56168F2077D"),
    "fga/mkidx.py": (14844, "4425B5D021B3E35371DEBB567881697F88DF6F533ACFC9783A749CE1A5176A6B"),
    "fga/mkmap.py": (22213, "7281F57EC7439E00431F2962DF9A6944779294955A9C4369615FFF04318B0053"),
    "srcmap/intake.py": (9923, "CFD53B71649BEF84A166397AA18E39AC5E4EDF00DD860142B2936F886AB080B1"),
    "srcmap/map.py": (27167, "57A92E34DB189E0EE95E6816074DB686C5616590C33DF823EF8EB9E9AFC2E1DF"),
    "srcmap/scan.py": (3403, "269E4D2F73405BDA82F373F04AF0109431416FF25CCA874F0051D193BC444D30"),
    "tags/tags": (991506, "C5C7017FB5C50B60295B30801CA1B5BAB8F5B379F61B084D8219441938125FCF"),
}

EXPECTED_SEM = {
    "README.md": (2585, "66D4CF92728AF7FF10E82CDFD97AFCD9D26B55CE9FBC985932FFBCD597DD64B4"),
    "bib.csv": (10422, "93F5A934ADDE0CD92BBB21AF70EFD81BA128CCD2EDF51EB19428B83437EC3516"),
    "catalog.csv": (772, "12C8C0D5EB10157AB1DBCD170AFF2147103AB848A3D28A8CA9EDF1C15186540A"),
    "edges.csv": (260944, "F1607445D52F28DA2F3FE93D8F47D7959C35ECFFBC167B5AB0E787A91264C719"),
    "idmap.csv": (473, "977D4A8F59A9642D58926DED8BB600079863AE6AF3F1F532806E83A9AB645BEA"),
    "manifest.json": (38138, "40596FD03A707CF8AC3C1D825D0FEAD4447663F6A57E7BD16735021F14B520AB"),
    "nodes.csv": (585012, "3A3C9B6C22B0FA5E16466C264205D97CCA6041FF785F555A4C28F9639A50550D"),
    "objects.csv": (106319, "82FF34C19C6D17D80DC3A617FD106ED324099CC9D0F2FE752757D0642ED31999"),
    "occ.csv": (515084, "54E545121F4D108E5C88B7039C39E3814F71F03332592C3F3965BD49B7FACED5"),
    "pages.csv": (23686, "E813C410B0A2AE53B4A787FD6C66A74225021E3A0FE22AD10CA2ED0C29807B0D"),
    "refdec.csv": (2313, "6AC5E23C3D4ADA0ABB1427E0533C3033E13B63C28A654A9C7E74A057A045FFA2"),
    "refs.csv": (159815, "995C9526CEC36FB6B437D7C688E4D40547BFC050949E3819A607FEEF53EA1162"),
    "resid.csv": (6415, "DDF53E58E21C7A5BF60C54ADC5EB9EB420B717246F1C69F294BBA5E358A38430"),
    "stacks.csv": (11777, "E13EFA405B525D69BFF38256601E4AF64D22FA3075F3A95AB3DFB78C15CFD060"),
    "subjects.csv": (2133, "A77A81831F752BA21701B150C13C51325E511B2FD5DFC76EED135FE3EDEEB026"),
    "terms.csv": (325587, "6D93CBBD2D6CF3E354FE90DC51605ACD9C7B0932CEF216FB9D606AD97D666E5D"),
    "validation.json": (6102, "2972E56494357AD0ABDB765057E20CA99777E6A6AA73B5AF7571EA1F715AA3D4"),
    "xwork.csv": (2446, "7BC42D7026C34AD8B1A111353E0810378F1DB9D1284BAD4C5C34D509D57B9EBB"),
}
EXPECTED_SEM_SURFACE = (18, 2060023, "76B6EBA7042FCFF59306E6178AC702BFDEDA392D2ADD754DDE932EBFAA6E6302")
EXPECTED_SEM_PAYLOAD_SURFACE = (16, 2015783, "71906EBD41B1777C661B904510BAC999FB5827E018CD1C606CE5007DFD0B9EB7")
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
AUTHORITY_PART_I = PROJECT / "authority_snapshot" / "jstage_part_I_9_2_119.pdf"
EXPECTED_AUTHORITY_PART_I = (
    7305283,
    "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF",
)
SCAN_ORACLE = ROOT / "tmp" / "d1009_scan"

PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv",
    "issues.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv",
    "map.csv", "ucand.csv", "mcheck.json", "STATUS.md",
}

EXECUTION_ROLES = {
    "driver": ("srcmap/start_build_tohoku_r52.ps1", "self_read_hash_then_one_shot_bootstrap_envelope"),
    "bootstrap": ("srcmap/start_build_tohoku_r52.py", "one_read_hash_compile_exec_builder_and_pin_validator"),
    "builder": ("srcmap/build_tohoku_r52.py", "read_hash_compile_and_exec_same_payload"),
    "validator": ("srcmap/validate_tohoku_r52.py", "independent_same_bytes_stage_and_receipt_replay"),
}

EXPECTED_SOURCE = {
    "cfg.json": (5151, "17AE218F11DEF95A76ADF0BD2A447B21150A3BAFF9D1209EC1C1FDFAA51D110A"),
    "check.json": (78159, "ABC8427BEDFA73CA9A7105138F4F49D58FF3CE277C870C7F55F6E743D72BDC81"),
    "dec.csv": (370367, "2B57BED76B6272DACD3F86EDA6E6FA8CAB9F0E5BBDE528668513973359B5BADA"),
    "intake.json": (1578, "7E2B1F451113D57041FB676A4BE85F6C8AE51783FC8A559691AD5D6DCCF9271F"),
    "issues.csv": (29535, "3439D68823BF69087F025976FB0AC41C2C4D93B8BFB4E63D6FD3267DB6AC178A"),
    "map.csv": (478269, "96B83855F504BA974E90798C0D5494120936DB0FE252811374ACD5E9348B4C87"),
    "mcheck.json": (67987, "48E7B9003E652C73F315E47A2707F7BB288C62F5531F1820615EFF610CEDF6D6"),
    "r51-check.json": (48954, "711F5162BB7830ABA202B9A51BE356427126C28624FE7BA3797EF0BF4F528922"),
    "STATUS.md": (1839, "FB251D6A17F1D0BD681ACB521F93755F6535C070CB9D77E6FECE265F582E366C"),
    "stx.csv": (5276647, "CF7E76DE52766F75E7174A1D6B56FC5466BA6D0521BAAC317856EDBF8047A1DB"),
    "tcand.csv": (485239, "2CA303980441ABDB51890EA1A2DA3544D604262589A546ACF2DE60F04391916E"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (393225, "6AAAD1470DDA82604F84D697EC1833FAC4BEE16342FAD8EB415BA17CFB018262"),
}
EXPECTED_SOURCE_SURFACE = (
    15,
    7241947,
    "82DDD6C08EDFD0775E58B22A7D5688B6B37CFBC61003EDC7B016978E0CF7AA7F",
)
EXPECTED_SOURCE_PAYLOAD_SURFACE = (
    14,
    7192993,
    "686AC3287DA298129718E9EF6AF3909EBDC21156BB2E20112C2A9D5B860EE477",
)

EXPECTED_ORACLE_OUTPUTS = {
    "stx.csv": (5278176, "A5535AF7AA7C02780D88DBEAB50417ED0BB7688865AB4A002D7B6656BAD41D14"),
    "tcand.csv": (487516, "7CF3E31793144F7AB87F7A9E79923E7B654E527713C3467823179BA74F224915"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "check.json": (78742, "F674AE16BCC04E12FF97705F7CC29B6E26B3CBA8EC978DD84A80FFA0F27B8808"),
}
EXPECTED_STAGE_SCAN_OUTPUTS = {
    **EXPECTED_ORACLE_OUTPUTS,
    "check.json": (78742, "7D7701B770C6B9B05438D3A1A75B8C561401FEB338465D6F84A67C733BD5D6A0"),
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22069,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1275,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}

DECISION_ROWS = [
    {
        "decision_id": "D001019",
        "unit_id": "tohoku:section:5.7",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-section-equivariant-cohomology-supports",
        "rationale": "The local Stacks chapter now contains a dedicated section developing equivariant cohomology with families of supports for abelian G-sheaves, so the source section heading and its organizing formalism are represented directly. The mapping is limited to the admitted abelian-sheaf setting and makes no module-valued extension claim.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000340",
    },
    {
        "decision_id": "D001020",
        "unit_id": "tohoku:definition:support-antifilter",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-definition-equivariant-cohomology-family-supports",
        "rationale": "Stacks now defines a G-stable family of supports, the supported invariant-section functor, and its right derived groups, matching the source's support antifilter after the documented terminology normalization. No assertion beyond abelian G-sheaves is made.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000612",
    },
    {
        "decision_id": "D001021",
        "unit_id": "tohoku:construction:invariant-support-antifilter",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-equivariant-family-supports-invariant-saturation",
        "rationale": "Stacks now proves that invariant saturation Phi^G is a family of supports contained in Phi and gives the same invariant supported sections, which is exactly the source construction needed for equivariant support cohomology.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000588",
    },
    {
        "decision_id": "D001022",
        "unit_id": "tohoku:spectral-sequence:5.7-i-supported-equivariant",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-orbit-space-equivariant-support-spectral-sequence",
        "rationale": "Stacks now proves the first-quadrant Grothendieck spectral sequence from supported cohomology of the group-cohomology sheaves to supported equivariant cohomology, including additivity, functoriality, and the finite abutment filtration. The orbit-space support family uses closure of q(Z), so no closed-image property of the orbit map is assumed.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000954",
    },
    {
        "decision_id": "D001023",
        "unit_id": "tohoku:obstruction:second-spectral-sequence-with-supports",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-remark-equivariant-support-second-spectral-sequence",
        "rationale": "Stacks now records the failure of automatic Grothendieck acyclicity for the second factorization and states the source's exact sufficient hypothesis that every member of Psi has a neighbourhood again belonging to Psi. It deliberately does not claim the deferred filtered-colimit construction, second spectral sequence, or interchange with group cohomology.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000625",
    },
]

EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "decisions": 1023,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 367,
        "existing_stronger": 41,
        "existing_weaker": 6,
        "extend_existing": 18,
        "historical_reference": 33,
        "new_section": 5,
        "new_statement": 13,
        "structural_only": 424,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 29,
    "unit_candidates": 0,
    "units": 991,
}

STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The sealed r51 dossier is preserved exactly and five reviewed D1009 decisions, D001019 through D001023, are appended.\n"
    "- The decisions map the supported equivariant section, support-family definition, invariant saturation, first supported Grothendieck spectral sequence, and exact second-factorization obstruction to the five new cohomology labels.\n"
    "- The semantic source remains the exact independently audited sem/r18 surface with all 991 stable unit IDs.\n"
    "- D1009 is limited to abelian G-sheaves; it does not claim a module-valued extension, the deferred filtered-colimit construction, the second supported spectral sequence, or interchange with group cohomology.\n"
    "- The bounded scanner indexes the same exact 119 top-level TeX files; stx.csv, tcand.csv, and tmap.csv match the sealed D1009 oracle byte-for-byte, while check.json differs only in the four dossier-relative r51-to-r52 SHA keys.\n"
    "- All 29 source issues remain resolved, 679 units remain decided, and 42 gap-class dispositions remain.\n"
    "- GitHub is temporarily unavailable under the current direct report; local production continues and no GitHub inspection, synchronization, push, or publication is attempted.\n"
    "- This local dossier makes no release, publication, remote-freshness, DOI, rights, or whole-paper completion claim.\n"
).encode("utf-8")

NONCLAIMS = [
    "No Git command or recursive workspace scan is executed by this mapping successor.",
    "The Stacks scanner is confined to the exact 119 top-level TeX filenames in the D1009 oracle.",
    "Exactly D001019 through D001023 are appended; the r51 decision prefix is byte-identical.",
    "The semantic source remains sem/r18 and no reader or semantic source file is changed.",
    "D1009 is restricted to abelian G-sheaves and makes no module-valued extension claim.",
    "The deferred filtered-colimit construction, second supported spectral sequence, and interchange with group cohomology are not claimed.",
    "No official Stacks tag is claimed for any of the five new local labels.",
    "No GitHub inspection, synchronization, push, or publication is attempted while GitHub is temporarily unavailable.",
    "No release, publication, upload, DOI, Zenodo, rights, remote-freshness, or whole-paper completion claim is made.",
    "42 Tohoku gap-class dispositions remain.",
]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), digest(data)


def record(path: Path, name: str | None = None) -> dict[str, object]:
    size, sha256 = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": sha256}


def aggregate(records: list[dict[str, object]]) -> str:
    raw = b"".join(
        f"{item['name']}\0{item['bytes']}\0{item['sha256']}\n".encode("utf-8")
        for item in sorted(records, key=lambda value: str(value["name"]).casefold())
    )
    return digest(raw)


def aggregate_case_sensitive(records: list[dict[str, object]]) -> str:
    raw = b"".join(
        f"{item['name']}\0{item['bytes']}\0{item['sha256']}\n".encode("utf-8")
        for item in sorted(records, key=lambda value: str(value["name"]))
    )
    return digest(raw)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def is_reparse(path: Path) -> bool:
    return os.name == "nt" and bool(path.stat(follow_symlinks=False).st_file_attributes & 0x400)


def require_plain_file(path: Path) -> None:
    require(path.is_file() and not path.is_symlink() and not is_reparse(path), f"Expected plain file: {path}")


def require_plain_directory(path: Path) -> None:
    require(path.is_dir() and not path.is_symlink() and not is_reparse(path), f"Expected plain directory: {path}")


def require_identity(path: Path, expected: tuple[int, str]) -> None:
    require_plain_file(path)
    require(identity(path) == expected, f"Identity drift: {path}")


def no_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_pairs)
    require(isinstance(value, dict), f"Expected JSON object: {path}")
    return value


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    raw = path.read_bytes().decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(raw, newline=""))
    require(reader.fieldnames is not None, f"Missing CSV header: {path}")
    rows = [dict(row) for row in reader]
    return list(reader.fieldnames), rows


def csv_bytes(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def expected_runtime() -> dict[str, tuple[int, str]]:
    return dict(EXPECTED_RUNTIME)


def expected_execution_attestation() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for role, (relative, contract) in EXECUTION_ROLES.items():
        path = ROOT / relative
        require_plain_file(path)
        size, sha256 = identity(path)
        result[role] = {
            "path": relative,
            "bytes": size,
            "sha256": sha256,
            "contract": contract,
        }
    return result


def verify_predecessor() -> dict[str, object]:
    require_plain_directory(SOURCE)
    entries = list(SOURCE.iterdir())
    require(not any(path.is_dir() for path in entries), "Unexpected r51 predecessor subdirectory")
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SOURCE), "r51 predecessor file surface drift")
    records: list[dict[str, object]] = []
    for name, expected in sorted(EXPECTED_SOURCE.items()):
        require_identity(SOURCE / name, expected)
        records.append(record(SOURCE / name))
    complete = (len(records), sum(int(row["bytes"]) for row in records), aggregate(records))
    require(complete == EXPECTED_SOURCE_SURFACE, "r51 predecessor complete aggregate drift")
    payload = [row for row in records if row["name"] != "r51-check.json"]
    payload_surface = (len(payload), sum(int(row["bytes"]) for row in payload), aggregate(payload))
    require(payload_surface == EXPECTED_SOURCE_PAYLOAD_SURFACE, "r51 predecessor payload aggregate drift")
    predecessor = strict_json(SOURCE / "r51-check.json")
    require(predecessor.get("schema") == "tohoku-stacks-mapping-successor-r51-v1", "r51 receipt schema drift")
    require(predecessor.get("status") == "PASS" and predecessor.get("errors") == [], "r51 receipt not PASS")
    require(predecessor.get("deltas", {}).get("decisions") == 1018, "r51 decision count drift")
    require(predecessor.get("deltas", {}).get("remaining_gap_class_dispositions") == 47, "r51 gap count drift")
    require(predecessor.get("files") == [record(SOURCE / name) for name in sorted(PAYLOAD)], "r51 receipt payload records drift")
    require(predecessor.get("deltas", {}).get("mapping_counts") == EXPECTED_MAPPING_COUNTS | {
        "decisions": 1018,
        "dispositions": {
            **EXPECTED_MAPPING_COUNTS["dispositions"],
            "existing_equivalent": 362,
            "extend_existing": 22,
            "new_section": 6,
        },
    }, "r51 sealed mapping-count evidence drift")
    return {
        "name": "tohoku_r51",
        "receipt": record(SOURCE / "r51-check.json", "tohoku_r51/r51-check.json"),
        "complete_surface": {"files": complete[0], "bytes": complete[1], "aggregate_sha256": complete[2]},
        "payload_surface": {"files": payload_surface[0], "bytes": payload_surface[1], "aggregate_sha256": payload_surface[2]},
        "decision_count": 1018,
        "remaining_gap_class_dispositions": 47,
        "independent_sealed_surface_replay": "PASS",
        "historical_live_validator_replay": "NOT_APPLICABLE_AFTER_D1009_TEX_SUCCESSOR",
    }


def verify_runtime() -> dict[str, object]:
    for relative, expected in sorted(EXPECTED_RUNTIME.items()):
        require_identity(ROOT / relative, expected)
    cache_pairs = {
        "mkidx": (ROOT / "fga" / "mkidx.py", ROOT / "fga" / "__pycache__" / "mkidx.cpython-313.pyc"),
        "mkmap": (ROOT / "fga" / "mkmap.py", ROOT / "fga" / "__pycache__" / "mkmap.cpython-313.pyc"),
    }
    cache_evidence: dict[str, object] = {}
    for name, (source, cache) in cache_pairs.items():
        raw = cache.read_bytes()
        require(len(raw) >= 16, f"Truncated pinned bytecode cache: {cache}")
        flags = int.from_bytes(raw[4:8], "little")
        source_size = int.from_bytes(raw[12:16], "little")
        require(flags == 0 and source_size == source.stat().st_size, f"Pinned bytecode header drift: {name}")
        cache_evidence[name] = {
            "source": record(source, f"fga/{source.name}"),
            "timestamp_cache": record(cache, f"fga/__pycache__/{cache.name}"),
            "header_flags": flags,
            "header_source_size": source_size,
            "execution_boundary": "The import may use this exact pinned cache when timestamp-valid, otherwise it compiles the exact pinned source; both files are locked for the transaction.",
        }
    return {
        "python": record(EXPECTED_PYTHON, str(EXPECTED_PYTHON)),
        "dependencies": {
            relative: {"bytes": expected[0], "sha256": expected[1]}
            for relative, expected in sorted(EXPECTED_RUNTIME.items())
        },
        "local_import_cache_evidence": cache_evidence,
    }


def verify_semantic() -> dict[str, object]:
    sem = PROJECT / "sem" / "r18"
    require_plain_directory(sem)
    entries = list(sem.iterdir())
    require(not any(path.is_dir() for path in entries), "Unexpected sem/r18 subdirectory")
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SEM), "sem/r18 file surface drift")
    records: list[dict[str, object]] = []
    for name, expected in sorted(EXPECTED_SEM.items()):
        require_identity(sem / name, expected)
        records.append(record(sem / name))
    surface = (len(records), sum(int(row["bytes"]) for row in records), aggregate_case_sensitive(records))
    require(surface == EXPECTED_SEM_SURFACE, "sem/r18 complete aggregate drift")
    payload = [row for row in records if row["name"] not in {"manifest.json", "validation.json"}]
    payload_surface = (len(payload), sum(int(row["bytes"]) for row in payload), aggregate_case_sensitive(payload))
    require(payload_surface == EXPECTED_SEM_PAYLOAD_SURFACE, "sem/r18 manifest payload aggregate drift")
    manifest = strict_json(sem / "manifest.json")
    validation = strict_json(sem / "validation.json")
    require(manifest.get("schema") == "tohoku-semantic-local-successor-manifest-v18", "sem/r18 manifest schema drift")
    require(validation.get("schema") == "tohoku-semantic-local-successor-validation-v18", "sem/r18 validation schema drift")
    require(validation.get("status") == "PASS" and validation.get("errors") == [], "sem/r18 validation not PASS")
    require(validation.get("manifest_sha256") == EXPECTED_SEM["manifest.json"][1], "sem/r18 manifest-validation binding drift")
    stable_counts = {
        "nodes": len(load_csv(sem / "nodes.csv")[1]),
        "occurrences": len(load_csv(sem / "occ.csv")[1]),
        "edges": len(load_csv(sem / "edges.csv")[1]),
        "references": len(load_csv(sem / "refs.csv")[1]),
    }
    require(stable_counts == {"nodes": 991, "occurrences": 1036, "edges": 1475, "references": 436}, "sem/r18 stable counts drift")
    return {
        "aggregate_sha256": surface[2],
        "bytes": surface[1],
        "file_count": surface[0],
        "files": records,
        "generation": "sem/r18",
        "manifest_payload_surface": {
            "aggregate_sha256": payload_surface[2],
            "bytes": payload_surface[1],
            "file_count": payload_surface[0],
        },
        "p214_semantic_replay": "EXACT",
        "reader_r17_binding": "EXACT",
        "stable_node_ids": stable_counts["nodes"],
        "stable_surfaces": stable_counts,
        "validation_status": "PASS",
    }


def _path_from_record(item: dict, base: Path | None = None) -> Path:
    path = Path(str(item["path"]))
    return path if path.is_absolute() else (base or ROOT) / path


def _require_record(item: dict, path: Path) -> None:
    require_identity(path, (int(item["bytes"]), str(item["sha256"])))


def verify_d1009() -> dict[str, object]:
    require_identity(D1009_AUDIT, EXPECTED_D1009_AUDIT)
    audit = strict_json(D1009_AUDIT)
    require(audit.get("schema") == "tohoku-stacks-d1009-audit-v1", "D1009 audit schema drift")
    require(audit.get("status") == "STRICT_PASS" and audit.get("errors") == [], "D1009 audit not STRICT_PASS")
    require(audit.get("formalization_id") == "D1009", "D1009 formalization ID drift")
    mapping = audit.get("mapping", {})
    require(mapping.get("current_mapping_state") == "UNCHANGED_R51", "D1009 mapping state drift")
    require(mapping.get("planned_successor") == "tohoku_r52", "D1009 successor drift")
    compact = [
        {
            "decision_id": row["decision_id"], "unit_id": row["unit_id"],
            "supersedes": row["supersedes"], "disposition": row["disposition"],
            "stacks_label": row["stacks_labels"],
        }
        for row in DECISION_ROWS
    ]
    require(mapping.get("planned_decisions") == compact, "D1009 planned decision binding drift")
    expected_counts = {
        "units": 991, "decisions": 1023, "decided_units": 679,
        "existing_equivalent": 367, "existing_stronger": 41,
        "existing_weaker": 6, "extend_existing": 18,
        "new_section": 5, "new_statement": 13,
        "remaining_gap_class_dispositions": 42,
    }
    require(mapping.get("expected_postsuccessor_counts") == expected_counts, "D1009 projected counts drift")

    source = audit.get("source_audit", {})
    _require_record(source["authority_pdf"], _path_from_record(source["authority_pdf"]))
    _require_record(source["reader_build_receipt"], _path_from_record(source["reader_build_receipt"], PROJECT))
    for item in source["source_pages"].values():
        _require_record(item, _path_from_record(item, PROJECT))
    ledger_item = source["existing_source_correction"]["ledger"]
    ledger = _path_from_record(ledger_item, PROJECT)
    _require_record(ledger_item, ledger)
    matches = []
    for number, line in enumerate(ledger.read_text(encoding="utf-8").splitlines(), 1):
        value = json.loads(line, object_pairs_hook=no_duplicate_pairs)
        if value.get("decision_id") == "TOH-SRC-P220-004":
            matches.append((number, value))
    require(len(matches) == 1 and matches[0][0] == 368 and matches[0][1].get("state") == "active", "TOH-SRC-P220-004 uniqueness/state drift")

    artifacts = audit.get("artifacts", {})
    for key in ("reviewed_draft", "tex", "aux", "out", "toc", "log", "pdf"):
        item = artifacts[key]
        _require_record(item, _path_from_record(item))
    aux_text = _path_from_record(artifacts["aux"]).read_text(encoding="utf-8", errors="strict")
    for label_line in audit.get("aux_labels", []):
        require(aux_text.count(label_line) == 1, f"D1009 aux label drift: {label_line}")
    require(audit.get("math_audit", {}).get("status") == "STRICT_PASS", "D1009 math audit drift")
    require(audit.get("build_audit", {}).get("status") == "STRICT_PASS", "D1009 build audit drift")
    require(audit.get("pdf_audit", {}).get("status") == "STRICT_PASS", "D1009 PDF audit drift")
    render_dir = ROOT / "tmp" / "pdfs"
    for page, expected_hash in zip(
        audit["pdf_audit"]["visual_pages"], audit["pdf_audit"]["visual_render_sha256"], strict=True
    ):
        image = render_dir / f"d1009-cohomology-{page}.png"
        require_plain_file(image)
        require(identity(image)[1] == expected_hash, f"D1009 visual render drift: page {page}")

    scanner = audit.get("scanner_audit", {})
    require(scanner.get("status") == "STRICT_PASS" and scanner.get("deterministic_replay_identical") is True, "D1009 scanner audit drift")
    require(scanner.get("counts") == {
        "labels": 22069, "official_tags_joined": 21437, "tex_files": 119,
        "topic_candidates": 1275, "topics": 13, "warnings": 641, "errors": 0,
    }, "D1009 scanner counts drift")
    for name, expected in EXPECTED_ORACLE_OUTPUTS.items():
        require_identity(SCAN_ORACLE / name, expected)
        item = scanner["outputs"][name]
        require((int(item["bytes"]), str(item["sha256"])) == expected, f"D1009 scanner receipt output drift: {name}")
    check = strict_json(SCAN_ORACLE / "check.json")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "D1009 scanner oracle count drift")
    require(check.get("errors") == [] and len(check.get("warnings", [])) == 641, "D1009 scanner warning/error drift")
    tex_hashes = check.get("tex_sha256")
    require(isinstance(tex_hashes, dict) and len(tex_hashes) == 119, "D1009 TeX hash surface drift")
    for filename, sha256 in tex_hashes.items():
        path = ROOT / filename
        require_plain_file(path)
        require(identity(path)[1] == sha256, f"D1009 TeX identity drift: {filename}")

    semantic = verify_semantic()
    require(semantic.get("aggregate_sha256") == "76B6EBA7042FCFF59306E6178AC702BFDEDA392D2ADD754DDE932EBFAA6E6302", "sem/r18 aggregate drift")
    return {
        "receipt": record(D1009_AUDIT, "D1009_CHECK.json"),
        "status": "STRICT_PASS",
        "planned_decisions": compact,
        "source_correction": {"decision_id": "TOH-SRC-P220-004", "line": 368, "state": "active"},
        "authority_part_ii": record(_path_from_record(source["authority_pdf"]), "authority_snapshot/jstage_part_II_9_3_185.pdf"),
        "scanner": {
            "outputs": {name: record(SCAN_ORACLE / name, f"tmp/d1009_scan/{name}") for name in sorted(EXPECTED_ORACLE_OUTPUTS)},
            "counts": scanner["counts"],
            "delta_from_r51": scanner["delta_from_r51"],
        },
        "builds": {
            "tex": record(_path_from_record(artifacts["tex"]), "cohomology.tex"),
            "aux": record(_path_from_record(artifacts["aux"]), "cohomology.aux"),
            "out": record(_path_from_record(artifacts["out"]), "cohomology.out"),
            "toc": record(_path_from_record(artifacts["toc"]), "cohomology.toc"),
            "log": record(_path_from_record(artifacts["log"]), "cohomology.log"),
            "pdf": record(_path_from_record(artifacts["pdf"]), "cohomology.pdf"),
            "math_audit": "STRICT_PASS", "build_audit": "STRICT_PASS", "pdf_audit": "STRICT_PASS",
        },
        "semantic": semantic,
    }


def verify_external() -> dict[str, object]:
    require(Path(sys.executable).resolve() == EXPECTED_PYTHON.resolve(), "Python executable path drift")
    require_identity(EXPECTED_PYTHON, EXPECTED_PYTHON_IDENTITY)
    require_identity(R51_VALIDATOR, EXPECTED_R51_VALIDATOR)
    require_identity(AUTHORITY_PART_I, EXPECTED_AUTHORITY_PART_I)
    runtime = verify_runtime()
    predecessor = verify_predecessor()
    d1009 = verify_d1009()
    return {
        "predecessor": predecessor,
        "decision_audit": {key: d1009[key] for key in ("receipt", "status", "planned_decisions", "source_correction")},
        "scanner": d1009["scanner"],
        "builds": d1009["builds"],
        "semantic": d1009["semantic"],
        "runtime": runtime,
        "authority_inputs": {
            "part_i": record(AUTHORITY_PART_I, "authority_snapshot/jstage_part_I_9_2_119.pdf"),
            "part_ii": d1009["authority_part_ii"],
        },
    }


def expected_decision_bytes() -> bytes:
    fields, rows = load_csv(SOURCE / "dec.csv")
    require(fields == [
        "decision_id", "unit_id", "action", "disposition", "stacks_labels",
        "rationale", "review_state", "supersedes",
    ], "r51 decision schema drift")
    require([row["decision_id"] for row in rows] == [f"D{number:06d}" for number in range(1, 1019)], "r51 decision sequence drift")
    suffix = csv_bytes(fields, DECISION_ROWS)
    return (SOURCE / "dec.csv").read_bytes() + suffix[suffix.index(b"\n") + 1:]


def expected_map_rows() -> tuple[list[str], list[dict[str, str]]]:
    fields, rows = load_csv(SOURCE / "map.csv")
    by_unit = {row["unit_id"]: row for row in rows}
    require(len(by_unit) == len(rows) == 991, "r51 map unit surface drift")
    for decision in DECISION_ROWS:
        unit_id = decision["unit_id"]
        old = by_unit[unit_id]
        require(old["decision_id"] == decision["supersedes"], f"Superseded decision drift: {unit_id}")
        replacement = dict(old)
        replacement.update({
            "decision_id": decision["decision_id"],
            "disposition": decision["disposition"],
            "review_state": decision["review_state"],
            "stacks_labels": decision["stacks_labels"],
            "stacks_tags": "",
            "rationale": decision["rationale"],
        })
        by_unit[unit_id] = replacement
    return fields, [by_unit[row["unit_id"]] for row in rows]


def map_delta(new_rows: list[dict[str, str]]) -> dict[str, object]:
    _, old_rows = load_csv(SOURCE / "map.csv")
    old_by = {row["unit_id"]: row for row in old_rows}
    new_by = {row["unit_id"]: row for row in new_rows}
    changed: dict[str, list[str]] = {}
    for unit_id in old_by:
        fields = sorted(key for key in old_by[unit_id] if old_by[unit_id][key] != new_by[unit_id][key])
        if fields:
            changed[unit_id] = fields
    require(set(changed) == {row["unit_id"] for row in DECISION_ROWS}, "Unauthorized r52 map mutation")
    return {"changed_units": len(changed), "changes": changed, "unchanged_units": 991 - len(changed)}


def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def execution_receipt() -> dict[str, object]:
    return {
        "attestation": expected_execution_attestation(),
        "dependencies": {
            name: {"name": Path(name).name, "bytes": expected[0], "sha256": expected[1]}
            for name, expected in sorted(expected_runtime().items())
        },
        "contract": "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion_with_rollback",
    }


def receipt_payload(root: Path, deltas: dict[str, object]) -> dict[str, object]:
    external = verify_external()
    return {
        "schema": "tohoku-stacks-mapping-successor-r52-v1",
        "status": "PASS",
        "errors": [],
        "predecessor_dossier": external["predecessor"],
        "semantic_source": external["semantic"],
        "decision_audit": external["decision_audit"],
        "scanner_oracle": external["scanner"],
        "builds": external["builds"],
        "runtime": external["runtime"],
        "authority_inputs": external["authority_inputs"],
        "execution": execution_receipt(),
        "git": {
            "inspection_performed": False,
            "status": "temporarily_unavailable",
            "reason": "Direct user report: the account was suspended after VPN use and a support ticket is filed; no Git operation is needed for this bounded local successor.",
            "predecessor_receipt": record(SOURCE / "r51-check.json", "tohoku_r51/r51-check.json"),
            "remote_server_freshness_verified": False,
        },
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": NONCLAIMS,
    }


def verify_stage(root: Path, receipt_mode: bool) -> dict[str, object]:
    require_plain_directory(root)
    entries = list(root.iterdir())
    expected_names = PAYLOAD | ({"r52-check.json"} if receipt_mode else set())
    require(not any(path.is_dir() for path in entries), "Unexpected r52 output subdirectory")
    require({path.name for path in entries if path.is_file()} == expected_names, "r52 output surface drift")
    for path in entries:
        require_plain_file(path)

    cfg = strict_json(root / "cfg.json")
    expected_cfg = strict_json(SOURCE / "cfg.json")
    expected_cfg["dossier_id"] = "tohoku_r52"
    require(cfg == expected_cfg, "r52 cfg differs from r51 beyond dossier ID")
    for name in ("intake.json", "units.csv", "topics.csv", "issues.csv", "tmap.csv", "ucand.csv"):
        require(identity(root / name) == identity(SOURCE / name), f"Unauthorized inherited payload drift: {name}")
    for name, expected in EXPECTED_STAGE_SCAN_OUTPUTS.items():
        require_identity(root / name, expected)
    stage_check = strict_json(root / "check.json")
    oracle_check = strict_json(SCAN_ORACLE / "check.json")
    stage_sha = stage_check.get("sha256", {})
    oracle_sha = oracle_check.get("sha256", {})
    require(isinstance(stage_sha, dict) and isinstance(oracle_sha, dict), "Scanner SHA ledger shape drift")
    expected_stage_only = {f"tohoku_r52/{name}" for name in ("stx.csv", "tcand.csv", "tmap.csv", "topics.csv")}
    expected_oracle_only = {f"tohoku_r51/{name}" for name in ("stx.csv", "tcand.csv", "tmap.csv", "topics.csv")}
    require(set(stage_sha) - set(oracle_sha) == expected_stage_only, "r52 scanner SHA path additions drift")
    require(set(oracle_sha) - set(stage_sha) == expected_oracle_only, "r52 scanner SHA path removals drift")
    normalized_stage = dict(stage_sha)
    for name in ("stx.csv", "tcand.csv", "tmap.csv", "topics.csv"):
        normalized_stage[f"tohoku_r51/{name}"] = normalized_stage.pop(f"tohoku_r52/{name}")
    normalized_check = dict(stage_check)
    normalized_check["sha256"] = normalized_stage
    require(normalized_check == oracle_check, "r52 scanner check differs from D1009 oracle beyond dossier-relative SHA keys")
    require((root / "dec.csv").read_bytes() == expected_decision_bytes(), "r52 decision ledger is not exact append-only successor")
    fields, decisions = load_csv(root / "dec.csv")
    require([row["decision_id"] for row in decisions] == [f"D{number:06d}" for number in range(1, 1024)], "r52 decision sequence drift")
    require(decisions[-5:] == DECISION_ROWS, "r52 appended decision rows drift")

    map_fields, mapped = load_csv(root / "map.csv")
    expected_fields, expected_rows = expected_map_rows()
    require(map_fields == expected_fields, "r52 map schema drift")
    require(mapped == expected_rows, "r52 map differs from independent r51 plus five-decision projection")
    delta = map_delta(mapped)
    mcheck = strict_json(root / "mcheck.json")
    check = strict_json(root / "check.json")
    require(mcheck.get("schema") == "historical-source-stacks-map-v1", "r52 mcheck schema drift")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "r52 mapping check not PASS")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r52 mapping counts drift")
    require(mcheck.get("warnings") == check.get("warnings") and len(mcheck.get("warnings", [])) == 641, "r52 warning propagation drift")
    require((root / "STATUS.md").read_bytes() == STATUS_BYTES, "r52 status narrative drift")

    gap_count = sum(EXPECTED_MAPPING_COUNTS["dispositions"][name] for name in (
        "existing_weaker", "extend_existing", "new_section", "new_statement"
    ))
    require(gap_count == 42, "r52 gap count projection drift")
    result = {
        "status": "PASS",
        "errors": [],
        "decisions": 1023,
        "decisions_appended": DECISION_ROWS,
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": {
            **EXPECTED_SCAN_COUNTS,
            "warnings": 641,
            "errors": 0,
        },
        "scanner_delta": strict_json(D1009_AUDIT)["scanner_audit"]["delta_from_r51"],
        "map_delta": delta,
        "remaining_gap_class_dispositions": 42,
        "semantic_generation": "sem/r18",
        "source_repairs_appended": 0,
    }
    if receipt_mode:
        receipt = strict_json(root / "r52-check.json")
        require(receipt == receipt_payload(root, result), "r52 receipt replay mismatch")
    return result


def external_input_paths() -> list[Path]:
    paths = [R51_VALIDATOR, D1009_AUDIT, EXPECTED_PYTHON, AUTHORITY_PART_I]
    paths.extend(SOURCE / name for name in EXPECTED_SOURCE)
    paths.extend(ROOT / relative for relative in expected_runtime())
    audit = strict_json(D1009_AUDIT)
    source = audit["source_audit"]
    paths.append(_path_from_record(source["authority_pdf"]))
    paths.append(_path_from_record(source["reader_build_receipt"], PROJECT))
    paths.extend(_path_from_record(item, PROJECT) for item in source["source_pages"].values())
    paths.append(_path_from_record(source["existing_source_correction"]["ledger"], PROJECT))
    paths.extend(_path_from_record(item) for item in audit["artifacts"].values())
    paths.extend(SCAN_ORACLE / name for name in EXPECTED_ORACLE_OUTPUTS)
    check = strict_json(SCAN_ORACLE / "check.json")
    paths.extend(ROOT / filename for filename in check["tex_sha256"])
    paths.extend(ROOT / "tmp" / "pdfs" / f"d1009-cohomology-{page}.png" for page in audit["pdf_audit"]["visual_pages"])
    sem = PROJECT / "sem" / "r18"
    paths.extend(sem / name for name in EXPECTED_SEM)
    return list(dict.fromkeys(paths))


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R52_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if not raw:
        return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r52.py", "bytes": actual[0], "sha256": actual[1]}
    expected = json.loads(raw)
    require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator same-bytes attestation drift")
    return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r52.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not os.path.lexists(TARGET), f"No-overwrite r52 target already exists: {TARGET}")
        require(not os.path.lexists(STAGE), f"Unresolved r52 transaction exists: {STAGE}")
        external = verify_external()
        _, projection = expected_map_rows()
        result = {
            "schema": "tohoku-r52-static-input-audit-v1",
            "status": "PASS", "errors": [], "attestation": attestation,
            "target_absent": True, "stage_absent": True,
            "predecessor": external["predecessor"],
            "decision_audit": external["decision_audit"],
            "scanner_oracle": external["scanner"],
            "runtime": external["runtime"],
            "authority_inputs": external["authority_inputs"],
            "projected_mapping_counts": EXPECTED_MAPPING_COUNTS,
            "projected_map_delta": map_delta(projection),
            "projected_remaining_gap_class_dispositions": 42,
            "launch_authorized": True,
        }
    else:
        result = {
            "schema": "tohoku-r52-stage-validation-v1",
            "attestation": attestation,
            **verify_stage(args.stage.resolve(), args.receipt),
        }
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
