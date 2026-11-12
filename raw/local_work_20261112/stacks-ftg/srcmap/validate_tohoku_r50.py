#!/usr/bin/env python3
"""Independent bounded validator for the frozen no-overwrite Tohoku r50 successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r49"
TARGET = ROOT / "tohoku_r50"
STAGE = ROOT / ".tohoku-r50-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r17"
AUTHORITY = PROJECT / "authority_snapshot"
BASE_VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r49.py"
BASE_BUILDER = ROOT / "srcmap" / "build_tohoku_r49.py"
D1007_AUDIT = ROOT / "D1007_CHECK.json"
EXPECTED_BASE_VALIDATOR = (
    65460,
    "F631B7A8E6E718D88AC17963985FF3963795EF9258CF18DE8E8EC746264AA420",
)
EXPECTED_BASE_BUILDER = (
    19799,
    "64BD728F019F4DD76F16700C830BA16A36E07A4017BACA70C7F02A0AF986533E",
)
EXPECTED_PYTHON = Path(r"user\miniconda3\python.exe")
EXPECTED_PYTHON_IDENTITY = (
    104264,
    "7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264",
)
EXPECTED_D1007_AUDIT = (
    10622,
    "07DDEDE20E8D2DC7C5EA4331C4A5C26DB23A7F2E2883B76BDD4B22556CBEB60B",
)

EXPECTED_SOURCE = {
    "STATUS.md": (1374, "32DB175A0FE24217ADF4F93BEACBDB1BB6CBACBC64DACFBBEF2EB4531733D857"),
    "cfg.json": (5151, "7BC1BE02E8EB2601CFC864620B8DE3FBE7C7D2A21153A3C08FC090BAC126FDD2"),
    "check.json": (77860, "26861958487CC4514FEEBE9FDA79BBEFC321DEA00710A4284BED5EC5A42777D0"),
    "dec.csv": (367898, "F0A62DC0A4CB95F32224DFBE17F8393783144C9C1BC4F62D58B4BF8C2F5C7512"),
    "intake.json": (1578, "8279157B8AA7F6AA006E2C434C34D2A7988836D63C25B3465B93896D62E22801"),
    "issues.csv": (29535, "3439D68823BF69087F025976FB0AC41C2C4D93B8BFB4E63D6FD3267DB6AC178A"),
    "map.csv": (476889, "324C6579B9EC75AD253C63ACA8A78F4C2DF017E349A11B9261F9220E96633CB1"),
    "mcheck.json": (67688, "F5EACF845A40C0CC99EAAB0A07F5976AA58080A89BE8577D89F3ACD3F0C19FCD"),
    "r49-check.json": (39889, "8BE3F295E873F4AE897B320AA7361C7572A432AC137B53C329ADD138C83C6354"),
    "stx.csv": (5275896, "3C99FAA5306E29E84D048D99F4B7A4F0084AE8DD93F6A39CB337080846465C02"),
    "tcand.csv": (485239, "34FA522127782ADD2121A003AE7DECF46FD4E4D5B19AA9966C5E88EE73CD147F"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (392568, "3AB04435EEDD9DE59E61DF2443812C2F555DD6CA85542DC7F9C6BBE59DB03081"),
}
EXPECTED_SOURCE_PAYLOAD_SURFACE = (
    14,
    7186673,
    "4B28212B9363B38F34349DE147C85985B3E0438AE37522F3197F92ED2C79760A",
)
EXPECTED_SOURCE_SURFACE = (
    15,
    7226562,
    "7348555CB0657DDC3519CC1AE97A40E1E4D381BA0080831556CD38846E73BD93",
)

INJECTIVES_ARTIFACTS = {
    "injectives.tex": (139285, "FEBCC2562AB17FEC850FD5FD88086DC3EB90017C007F348207ED93479895A283"),
    "injectives.aux": (10440, "35EDCF13B22243EF0C6BE422314F78E22E599F7D7EB476E5E34A1C458BB8B233"),
    "injectives.log": (35038, "A88395A76DD870EEEA728154996211A8200B27FD9239161886D2687CDEEA9EB5"),
    "injectives.pdf": (647072, "B157CF029CA765F596C4C7620A7DFB731F5301E5DF41CB63FE20CA151EFFFB25"),
}

D1007_SOURCE_ARTIFACTS = {
    "english_p185": (PROJECT / "build" / "v068c3r15" / "src" / "en" / "p185.tex", 4183, "6D15A561E5FCE6D3071672663DE9969249A5D147F08D6DC61A7CD5F3E43A084D"),
    "english_p186": (PROJECT / "build" / "v068c3r15" / "src" / "en" / "p186.tex", 3667, "536B9C5C6C23BF8CEB0B783F065B5ED465411BA00EDE11F2B197C7217996013E"),
    "english_p187": (PROJECT / "build" / "v068c3r15" / "src" / "en" / "p187.tex", 3970, "62DB4D72074B9241C580B25C4B5FEBC9F449709AB84D7566B7056C222085FFA7"),
    "french_p185": (PROJECT / "build" / "v068c3r15" / "src" / "fr" / "p185.tex", 4302, "85D04A11FF28F109C9006A850A3D9176A6483C2CAC56AA9B849058934B65C54A"),
    "french_p186": (PROJECT / "build" / "v068c3r15" / "src" / "fr" / "p186.tex", 3904, "CD2E0A570004B73FEC05C8A8045D721811040275B05B39A2F81A7CC6B3EB3F91"),
    "french_p187": (PROJECT / "build" / "v068c3r15" / "src" / "fr" / "p187.tex", 4308, "A709B05718C7422DC3EA6C2D9A94699852EE4A1F36B60B28F190049734EABAA0"),
}

EXPECTED_REPAIR_SURFACE = (
    32,
    8961393,
    "A1EC00B210E2638C0A3B9AB9D861BC1410CB91F0033DC5732AB773BCD0952AD1",
)

DECISION_ROWS = [
    {
        "decision_id": "D001016",
        "unit_id": "tohoku:proposition:4.1.2",
        "action": "replace",
        "disposition": "existing_stronger",
        "stacks_labels": "injectives-lemma-injective-left-module-stalks",
        "rationale": "Stacks now proves the proposition in a stronger pointwise local form for sheaves of not-necessarily-commutative unital rings: coherence of the left regular sheaf near x and left Noetherianity of the single stalk imply that the stalk at x of every injective sheaf of unital left modules is injective. The proof gives the left-sided Baer criterion, the finite-presentation stalk-Hom comparison as abelian groups, and extension by zero; the former commutative lemma is retained as a corollary. No right-module, two-sided-ideal, or unrestricted stalk-preservation claim is made.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000513",
    },
]

EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "decisions": 1016,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 362,
        "existing_stronger": 39,
        "existing_weaker": 6,
        "extend_existing": 22,
        "historical_reference": 33,
        "new_section": 6,
        "new_statement": 15,
        "structural_only": 424,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 29,
    "unit_candidates": 0,
    "units": 991,
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22062,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1270,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_SCAN_OUTPUTS = {
    "stx.csv": (5276137, "C508EA79EB23A25D2911E3174A76AA7ED790947C8876F73817EEE1FEFF99B6BF"),
    "tcand.csv": (485239, "62ABF592201379300DA78F98C91644A4E6747F27F392C9C31AE00FC7AB29361B"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
}
NEW_LABEL_ROWS = {
    "injectives-lemma-injective-left-module-stalks": {
        "tag": "",
        "full_label": "injectives-lemma-injective-left-module-stalks",
        "file": "injectives.tex",
        "line": "487",
        "kind": "lemma",
        "short_label": "lemma-injective-left-module-stalks",
        "chapter": "Injectives",
        "section_label": "section-abelian-sheaves-space",
        "section_title": "Abelian sheaves on a space",
        "text_sha256": "FC86868FD7B3A46F27D02D9D1262E9E11F6E11EDE3011B70D159B7739F5D705B",
    },
}
NEW_LABEL_TEXTS = {
    "injectives-lemma-injective-left-module-stalks": (
        "egin lemma egin reference ite[Chapter IV, 4.1, Proposition 4.1.2, p. 187] "
        "Tohoku For this lemma only, rings are not required to be commutative. Let X be a "
        "topological space and let R be a sheaf of associative rings with 1 whose restriction "
        "maps preserve 1 . All modules are unital"
    ),
}
NEW_LABEL_ROW = NEW_LABEL_ROWS["injectives-lemma-injective-left-module-stalks"]
NEW_LABEL_TEXT = NEW_LABEL_TEXTS["injectives-lemma-injective-left-module-stalks"]
PRESERVED_LABEL_ROW = {
    "tag": "",
    "full_label": "injectives-lemma-injective-module-stalks",
    "file": "injectives.tex",
    "line": "607",
    "kind": "lemma",
    "short_label": "lemma-injective-module-stalks",
    "chapter": "Injectives",
    "section_label": "section-abelian-sheaves-space",
    "section_title": "Abelian sheaves on a space",
    "text_sha256": "B9BE9336B9886CD1DEF4B634FFEB349ADDC2E632CE4F7904B7CC6ED4ED1AC372",
}
PRESERVED_LABEL_TEXT = (
    "egin lemma Let (X, O X) be a ringed space and let x X . Assume that O X is coherent as "
    "an O X -module and that O X, x is Noetherian. If I is an injective O X -module, then I x "
    "is an injective O X, x -module."
)
INHERITED_D1005_LABEL_ROW = {
    "tag": "",
    "full_label": "injectives-lemma-filtered-diagram-injective-resolutions",
    "file": "injectives.tex",
    "line": "2295",
    "kind": "lemma",
    "short_label": "lemma-filtered-diagram-injective-resolutions",
    "chapter": "Injectives",
    "section_label": "section-grothendieck-categories",
    "section_title": "Injectives in Grothendieck categories",
    "text_sha256": "2A99CA7E224719D14B55EE727D4056721FB6ACC534636F8B8F580942A329FE4C",
}
INHERITED_D1004_LABEL_ROW = {
    "tag": "",
    "full_label": "cohomology-lemma-holomorphic-logarithmic-derivative-obstruction",
    "file": "cohomology.tex",
    "line": "2824",
    "kind": "lemma",
    "short_label": "lemma-holomorphic-logarithmic-derivative-obstruction",
    "chapter": "Cohomology of Sheaves",
    "section_label": "section-flasque",
    "section_title": "Flasque sheaves",
    "text_sha256": "D50806E3B497B6176EC5B5C98F43D2AA306C8F55B385AD3BAFBC11AE74C5FC5F",
}
INHERITED_OBSTRUCTION_LABEL_ROW = {
    "tag": "",
    "full_label": "cohomology-lemma-crossed-homomorphism-torsor-obstruction",
    "file": "cohomology.tex",
    "line": "348",
    "kind": "lemma",
    "short_label": "lemma-crossed-homomorphism-torsor-obstruction",
    "chapter": "Cohomology of Sheaves",
    "section_label": "section-h1-torsors",
    "section_title": "First cohomology and torsors",
    "text_sha256": "4988F6BEBA93076DC196C4CF6E12F929889F97BC727E4138AB797631D08E4C56",
}

PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv",
    "issues.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv",
    "map.csv", "ucand.csv", "mcheck.json", "STATUS.md",
}

EXECUTION_ROLES = {
    "driver": ("srcmap/start_build_tohoku_r50.ps1", "self_read_hash_then_one_shot_bootstrap_envelope"),
    "bootstrap": ("srcmap/start_build_tohoku_r50.py", "one_read_hash_compile_exec_builder_and_pin_validator"),
    "builder": ("srcmap/build_tohoku_r50.py", "read_hash_compile_and_exec_same_payload"),
    "validator": ("srcmap/validate_tohoku_r50.py", "independent_same_bytes_stage_and_receipt_replay"),
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), digest(data)


def record(path: Path, name: str | None = None) -> dict[str, object]:
    size, sha256 = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": sha256}


def aggregate(records: list[dict[str, object]]) -> str:
    data = b"".join(
        f"{item['name']}\0{item['bytes']}\0{item['sha256']}\n".encode("utf-8")
        for item in sorted(records, key=lambda value: str(value["name"]))
    )
    return digest(data)


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


def strict_json(path: Path) -> dict:
    data = path.read_bytes()
    require(b"\r" not in data and data.endswith(b"\n"), f"Noncanonical JSON: {path}")

    def no_duplicates(values: list[tuple[str, object]]) -> dict:
        output: dict[str, object] = {}
        for key, value in values:
            require(key not in output, f"Duplicate JSON key {key}: {path}")
            output[key] = value
        return output

    value = json.loads(data.decode("utf-8"), object_pairs_hook=no_duplicates)
    require(isinstance(value, dict), f"Expected JSON object: {path}")
    return value


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    data = path.read_bytes()
    require(b"\r" not in data and data.endswith(b"\n"), f"Noncanonical CSV: {path}")
    reader = csv.DictReader(data.decode("utf-8-sig").splitlines())
    rows = list(reader)
    require(reader.fieldnames is not None, f"Missing CSV header: {path}")
    require(all(None not in row and None not in row.values() for row in rows), f"Malformed CSV: {path}")
    return list(reader.fieldnames), rows


def csv_bytes(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"Cannot load pinned module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_base_validator():
    require_identity(BASE_VALIDATOR, EXPECTED_BASE_VALIDATOR)
    module = load_module(BASE_VALIDATOR, "tohoku_r50_pinned_r49_validator")
    require_identity(BASE_VALIDATOR, EXPECTED_BASE_VALIDATOR)
    return module


BASE = load_base_validator()
EXPECTED_SEM = dict(BASE.EXPECTED_SEM)
EXPECTED_SEM_SURFACE = BASE.EXPECTED_SEM_SURFACE
EXPECTED_SEM_PAYLOAD_SURFACE = BASE.EXPECTED_SEM_PAYLOAD_SURFACE


def expected_runtime() -> dict[str, tuple[int, str]]:
    return {
        **BASE.expected_runtime(),
        "srcmap/validate_tohoku_r49.py": EXPECTED_BASE_VALIDATOR,
        "srcmap/build_tohoku_r49.py": EXPECTED_BASE_BUILDER,
    }


def expected_repairs() -> dict[str, tuple[int, str]]:
    return BASE.expected_repairs()


def expected_artifacts() -> dict[str, tuple[int, str]]:
    return {**BASE.expected_artifacts(), **INJECTIVES_ARTIFACTS}


def expected_tex_hashes() -> dict[str, str]:
    hashes = dict(strict_json(SOURCE / "check.json")["tex_sha256"])
    require(len(hashes) == 119, "Predecessor TeX manifest is not 119 files")
    hashes["injectives.tex"] = INJECTIVES_ARTIFACTS["injectives.tex"][1]
    return hashes


def load_mkidx():
    return load_module(ROOT / "fga" / "mkidx.py", "tohoku_r50_pinned_mkidx")


def verify_semantic() -> dict[str, object]:
    return BASE.verify_semantic()


def verify_repairs() -> dict[str, object]:
    return BASE.verify_repairs()

    # The remainder is the inherited r49 replay implementation. It is
    # intentionally unreachable: BASE owns and pins that sealed evidence.
    repairs = expected_repairs()
    records = []
    for relative, expected in sorted(repairs.items()):
        path = PROJECT / relative
        require_identity(path, expected)
        records.append(record(path, relative))
    surface = (len(records), sum(int(item["bytes"]) for item in records), aggregate(records))
    require(surface == EXPECTED_REPAIR_SURFACE, "D1006 source-repair aggregate drift")

    preflight = strict_json(P169_SOURCE_ARTIFACTS["preflight"][0])
    require(
        preflight.get("schema") == "tohoku-p169-degree-zero-qualification-preflight-v1"
        and preflight.get("status") == "PASS"
        and preflight.get("errors") == []
        and preflight.get("printed_page") == 169
        and preflight.get("unit_id") == "tohoku:proposition:3.6.2"
        and preflight.get("decision_id") == "TOH-SRC-P169-011",
        "p169 qualification preflight drift",
    )
    admission = strict_json(P169_SOURCE_ARTIFACTS["admission"][0])
    require(
        admission.get("schema") == "tohoku-p169-degree-zero-source-repair-v1"
        and admission.get("status") == "PASS"
        and admission.get("errors") == []
        and admission.get("source_state") == "admitted_no_overwrite_successor"
        and admission.get("reader_selector_state") == "advanced_after_persisted_source_preflight"
        and admission.get("reader_build_state") == "NOT_LAUNCHED"
        and admission.get("mapping_state") == "UNCHANGED_R49"
        and admission.get("unit_id") == "tohoku:proposition:3.6.2"
        and admission.get("decision_id") == "TOH-SRC-P169-011",
        "p169 source admission drift",
    )
    require(
        admission.get("exact_source_delta")
        == {
            "diplomatic_french_changes": 0,
            "corrected_french_exact_insertions": 1,
            "english_exact_insertions": 1,
            "other_source_changes": 0,
            "ordered_layer_target_sha256": "C031A569CDDE8D3ACBE22E6F35780FAEC5DB2ABFF4C50A55EA334033E138D003",
        },
        "p169 exact source delta drift",
    )
    require(
        admission.get("qualification")
        == {
            "canonical_map": "T(M)->R^0T(M)",
            "positive_vanishing": "R^qT(M)=0 for q>0",
            "left_exact_specialization": True,
            "arbitrary_additive_requires_full_right_acyclicity": True,
        },
        "p169 mathematical qualification drift",
    )
    decision_data = P169_SOURCE_ARTIFACTS["decisions"][0].read_bytes()
    require(b"\r" not in decision_data and decision_data.endswith(b"\n"), "Noncanonical p169 decision JSONL")
    decision_rows = [json.loads(line) for line in decision_data.decode("utf-8").splitlines()]
    decision_ids = [row.get("decision_id") for row in decision_rows]
    require(len(decision_rows) == 12 and len(set(decision_ids)) == 12, "p169 decision ledger surface drift")
    require(decision_ids[-1] == "TOH-SRC-P169-011", "p169 qualification decision drift")

    build = strict_json(READER_ARTIFACTS["build_receipt"][0])
    require(
        build.get("schema") == "tohoku-v068-staged-successor-build-v1"
        and build.get("revision") == "v068c3r16"
        and build.get("predecessor_revision") == "v068c3r15"
        and build.get("status") == "PASS"
        and build.get("errors") == []
        and build.get("compile_order") == ["fr", "en"]
        and build.get("passes_per_language") == 2
        and build.get("shell") is False,
        "reader r16 build receipt drift",
    )
    require(
        build.get("staged_source_verification")
        == {
            "all_files_locked_against_write_and_delete": True,
            "bytes": 62845,
            "format": "canonical_json_array_utf8_sort_keys_compact over path, bytes, sha256",
            "rows": 543,
            "sha256": "7E465B4A4CF1E6EDA2EA3FFE4AFDFCE05872896842298028E1DA56E28AC249D1",
            "total_file_bytes": 11854663,
            "verified_from_already_open_handles": True,
        },
        "reader r16 staged-source manifest drift",
    )
    require(
        build.get("revision_surface_contract", {}).get("replaced_staged_paths") == ["en/p169.tex", "fr/p169.tex"]
        and build.get("revision_surface_contract", {}).get("byte_identical_staged_files") == 541
        and build.get("revision_surface_contract", {}).get("other_staged_source_changes") == 0,
        "reader r16 source transition drift",
    )
    for language, key, name, pages in (
        ("en", "english_pdf", "en-p119-221-v068c3r16.pdf", 90),
        ("fr", "french_pdf", "fr-p119-221-v068c3r16.pdf", 93),
    ):
        pdf = build.get("pdfs", {}).get(language, {})
        expected = READER_ARTIFACTS[key]
        require(
            (pdf.get("name"), pdf.get("bytes"), pdf.get("sha256"), pdf.get("full_readback"))
            == (name, expected[1], expected[2], True)
            and pdf.get("strict_pdf_parse", {}).get("result") == "PASS"
            and pdf.get("strict_pdf_parse", {}).get("pages") == pages
            and pdf.get("strict_pdf_parse", {}).get("encrypted") is False,
            f"reader r16 {language} PDF evidence drift",
        )
    qa = strict_json(READER_ARTIFACTS["independent_qa"][0])
    require(
        qa.get("schema") == "tohoku-v068-reader-independent-qa-v1"
        and qa.get("qa_revision") == "v68r38"
        and qa.get("reader_revision") == "v068c3r16"
        and qa.get("predecessor_revision") == "v068c3r15"
        and qa.get("stable_id") == "tohoku:reader-qa:v68r38:v068c3r16"
        and qa.get("status") == "PASS"
        and qa.get("errors") == [],
        "reader r38 independent QA drift",
    )
    require(
        qa.get("conclusion")
        == {
            "blockers": [],
            "pdf_pair_accepted": True,
            "reader_successor_accepted": True,
            "source_transition_exact": True,
            "visual_review_accepted": True,
        },
        "reader r38 conclusion drift",
    )
    return {
        "files": records,
        "file_count": len(records),
        "bytes": sum(int(item["bytes"]) for item in records),
        "aggregate_sha256": aggregate(records),
        "p169_source_qualification": "SEALED_REPLAY_PASS",
        "reader_r16": "PASS",
        "reader_r16_independent_qa": "STRICT_PASS",
    }


def verify_d1006_audit() -> dict[str, object]:
    require_identity(D1006_AUDIT, EXPECTED_D1006_AUDIT)
    audit = strict_json(D1006_AUDIT)
    require(audit.get("schema") == "tohoku-stacks-d1006-audit-v1", "D1006 audit schema drift")
    require(audit.get("status") == "STRICT_PASS" and audit.get("errors") == [], "D1006 audit not STRICT_PASS")
    require(audit.get("formalization_id") == "D1006", "D1006 formalization ID drift")
    require(audit.get("primary_unit") == "tohoku:proposition:3.6.2", "D1006 primary-unit drift")
    related_units = {
        "tohoku:subitem:3.6.2:a",
        "tohoku:subitem:3.6.2:b",
        "tohoku:proof:3.6.2:p1",
        "tohoku:proof:3.6.2:p2",
        "tohoku:eq:derived-colimit-comparison",
        "tohoku:eq:colimit-resolution",
        "tohoku:eq:T-acyclic-computation",
        "tohoku:eq:T-colimit-complex",
        "tohoku:eq:cohomology-colimit-comparison",
        "tohoku:eq:derived-colimit-isomorphism",
    }
    require(set(audit.get("related_units", [])) == related_units, "D1006 related-unit surface drift")
    require(
        audit.get("stacks_label") == "derived-lemma-right-derived-functor-commutes-filtered-colimits"
        and DECISION_ROWS[0]["stacks_labels"] == audit.get("stacks_label"),
        "D1006 label drift",
    )
    require(
        audit.get("source_reference")
        == "Tohoku, Chapter III, Section 3.6, Proposition 3.6.2 and proof, pp. 169--170, with the right-derived-functor convention on p. 143",
        "D1006 source-reference drift",
    )
    require(
        audit.get("mapping")
        == {
            "status": "PENDING_NO_OVERWRITE_SUCCESSOR",
            "current_mapping_state": "UNCHANGED_R49",
            "unit": "tohoku:proposition:3.6.2",
            "nonclaim": "This receipt does not update or promote the Tohoku mapping ledger. D1006 mapping admission belongs to a later audited no-overwrite mapping successor.",
        },
        "D1006 pending-mapping state drift",
    )
    qualification = audit.get("source_qualification", {})
    require(
        qualification.get("status") == "STRICT_PASS"
        and qualification.get("decision_id") == "TOH-SRC-P169-011"
        and qualification.get("ordered_layer_target_sha256") == "C031A569CDDE8D3ACBE22E6F35780FAEC5DB2ABFF4C50A55EA334033E138D003"
        and qualification.get("layer_targets_added") == 0
        and qualification.get("layer_targets_removed") == 0,
        "D1006 source-qualification summary drift",
    )
    for key, source_key in (("preflight", "preflight"), ("admission", "admission"), ("decisions", "decisions")):
        path, size, sha256 = P169_SOURCE_ARTIFACTS[source_key]
        row = qualification.get(key, {})
        require(
            (row.get("path"), row.get("bytes"), row.get("sha256")) == (str(path), size, sha256),
            f"D1006 source-qualification {key} binding drift",
        )
    for key, source_key in (("diplomatic_french", "diplomatic_french"), ("corrected_french", "corrected_french"), ("english", "english")):
        path, size, sha256 = P169_SOURCE_ARTIFACTS[source_key]
        row = qualification.get("layers", {}).get(key, {})
        require(
            (row.get("path"), row.get("bytes"), row.get("sha256")) == (str(path), size, sha256),
            f"D1006 source-qualification {key} layer drift",
        )
    reader = audit.get("reader_successor", {})
    require(
        reader.get("status") == "STRICT_PASS"
        and reader.get("revision") == "v068c3r16"
        and reader.get("predecessor_revision") == "v068c3r15",
        "D1006 reader-successor summary drift",
    )
    for key, reader_key in (("build_receipt", "build_receipt"), ("independent_qa", "independent_qa")):
        path, size, sha256 = READER_ARTIFACTS[reader_key]
        row = reader.get(key, {})
        require(
            (row.get("path"), row.get("bytes"), row.get("sha256")) == (str(path), size, sha256),
            f"D1006 reader {key} binding drift",
        )
    require(
        reader.get("staged_source_manifest")
        == {
            "rows": 543,
            "total_file_bytes": 11854663,
            "manifest_bytes": 62845,
            "sha256": "7E465B4A4CF1E6EDA2EA3FFE4AFDFCE05872896842298028E1DA56E28AC249D1",
            "replaced_paths": ["en/p169.tex", "fr/p169.tex"],
            "byte_identical_predecessor_files": 541,
            "other_staged_source_changes": 0,
        },
        "D1006 reader staged-source evidence drift",
    )
    for language, key, pages in (("english", "english_pdf", 90), ("french", "french_pdf", 93)):
        _, build_size, build_sha256 = READER_ARTIFACTS[key]
        output_path, size, sha256 = READER_OUTPUT_ARTIFACTS[language]
        require((size, sha256) == (build_size, build_sha256), f"D1006 reader {language} build/output identity drift")
        require_identity(output_path, (size, sha256))
        pdf = reader.get("pdfs", {}).get(language, {})
        require(
            (pdf.get("path"), pdf.get("bytes"), pdf.get("sha256"), pdf.get("pages"), pdf.get("rotation"), pdf.get("encrypted"), pdf.get("strict_parse"))
            == (str(output_path), size, sha256, pages, 0, False, "PASS"),
            f"D1006 reader {language} PDF drift",
        )
    expected_artifact_rows = {
        "tex": {
            "path": str(ROOT / "derived.tex"),
            "bytes": DERIVED_ARTIFACTS["derived.tex"][0],
            "sha256": DERIVED_ARTIFACTS["derived.tex"][1],
            "new_block_lines": [7237, 7386],
        },
        "aux": {"path": str(ROOT / "derived.aux"), "bytes": DERIVED_ARTIFACTS["derived.aux"][0], "sha256": DERIVED_ARTIFACTS["derived.aux"][1]},
        "log": {"path": str(ROOT / "derived.log"), "bytes": DERIVED_ARTIFACTS["derived.log"][0], "sha256": DERIVED_ARTIFACTS["derived.log"][1]},
    }
    for key, expected in expected_artifact_rows.items():
        require(audit.get("artifacts", {}).get(key) == expected, f"D1006 audit {key} binding drift")
    pdf = audit.get("artifacts", {}).get("pdf", {})
    require(
        (pdf.get("path"), pdf.get("bytes"), pdf.get("sha256"), pdf.get("pages"), pdf.get("media_box"), pdf.get("rotation"), pdf.get("encrypted"))
        == (str(ROOT / "derived.pdf"), DERIVED_ARTIFACTS["derived.pdf"][0], DERIVED_ARTIFACTS["derived.pdf"][1], 148, [0, 0, 612, 792], 0, False),
        "D1006 audit PDF binding drift",
    )
    require(
        audit.get("aux_label")
        == r"\newlabel{lemma-right-derived-functor-commutes-filtered-colimits}{{20.6}{74}{Filtered colimits of objects}{subsection.20.6}{}}",
        "D1006 audit AUX label drift",
    )
    for section in ("source_audit", "math_audit", "build_audit", "pdf_audit"):
        require(audit.get(section, {}).get("status") == "STRICT_PASS", f"D1006 {section} drift")
    require(audit.get("pdf_audit", {}).get("visual_pages") == [72, 73, 74, 75, 76, 77], "D1006 visual-page audit drift")
    require(audit.get("pdf_audit", {}).get("mupdf_interpretation_pages") == 148, "D1006 full-PDF interpretation drift")
    require(
        any("full right T-acyclicity includes the degree-zero isomorphism" in claim for claim in audit.get("nonclaims", []))
        and any("No filtered colimit of injective objects is asserted to be injective." == claim for claim in audit.get("nonclaims", [])),
        "D1006 qualification/nonclaim drift",
    )
    return {"receipt": record(D1006_AUDIT, "D1006_CHECK.json"), "status": "STRICT_PASS", "errors": []}


def verify_d1007_audit() -> dict[str, object]:
    require_identity(D1007_AUDIT, EXPECTED_D1007_AUDIT)
    audit = strict_json(D1007_AUDIT)
    require(audit.get("schema") == "tohoku-stacks-d1007-audit-v1", "D1007 audit schema drift")
    require(audit.get("status") == "STRICT_PASS" and audit.get("errors") == [], "D1007 audit not STRICT_PASS")
    require(audit.get("formalization_id") == "D1007", "D1007 formalization ID drift")
    require(audit.get("primary_unit") == "tohoku:proposition:4.1.2", "D1007 primary-unit drift")
    require(
        set(audit.get("related_source_units", []))
        == {
            "tohoku:question:injectivity-of-stalk",
            "tohoku:lemma:4.1.1",
            "tohoku:proof:lemma-4.1.1",
            "tohoku:proposition:4.1.2",
        },
        "D1007 related-unit surface drift",
    )
    require(
        audit.get("stacks_label") == "injectives-lemma-injective-left-module-stalks"
        and DECISION_ROWS[0]["stacks_labels"] == audit.get("stacks_label")
        and audit.get("preserved_corollary_label") == "injectives-lemma-injective-module-stalks",
        "D1007 label binding drift",
    )
    require(
        audit.get("source_reference")
        == "Tohoku, Chapter IV, Section 4.1, Proposition 4.1.2, p. 187, with its setup and proof on pp. 185--187",
        "D1007 source-reference drift",
    )
    require(
        audit.get("mapping")
        == {
            "status": "PENDING_NO_OVERWRITE_SUCCESSOR",
            "current_mapping_state": "UNCHANGED_R49",
            "planned_successor": "tohoku_r50",
            "planned_decision": "D001016",
            "planned_disposition": "existing_stronger",
            "planned_superseded_decision": "D000513",
            "classification_reason": "The new fixed-point theorem needs left coherence only near x and left Noetherianity only of the single stalk, so it strictly strengthens the global Tohoku proposition while its explicit every-point consequence recovers the source statement.",
            "nonclaim": "This receipt does not mutate or promote the mapping ledger; the mapping transition belongs to a separately validated no-overwrite r50 transaction.",
        },
        "D1007 pending-mapping state drift",
    )
    source = audit.get("source_audit", {})
    require(
        source.get("status") == "STRICT_PASS"
        and source.get("authority_pdf_part_ii_sha256") == "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53"
        and source.get("source_repair_required") is False
        and "Proposition 4.1.3" in source.get("semantic_boundary", ""),
        "D1007 source audit drift",
    )
    for key, (path, size, sha256) in D1007_SOURCE_ARTIFACTS.items():
        require_identity(path, (size, sha256))
        require(
            source.get("layers", {}).get(key)
            == {"path": str(path), "bytes": size, "sha256": sha256},
            f"D1007 source layer drift: {key}",
        )
    convention = audit.get("convention_audit", {})
    require_identity(ROOT / "conventions.tex", (1869, "B37BDC9188B005994D334222886A9C3D878D270F8BB2F79368F8351D12B50880"))
    require(
        (convention.get("status"), convention.get("path"), convention.get("bytes"), convention.get("sha256"))
        == ("STRICT_PASS", str(ROOT / "conventions.tex"), 1869, "B37BDC9188B005994D334222886A9C3D878D270F8BB2F79368F8351D12B50880"),
        "D1007 convention audit drift",
    )
    expected_artifact_rows = {
        "tex": {
            "path": str(ROOT / "injectives.tex"),
            "bytes": INJECTIVES_ARTIFACTS["injectives.tex"][0],
            "sha256": INJECTIVES_ARTIFACTS["injectives.tex"][1],
            "new_block_lines": [486, 623],
            "new_label_line": 487,
            "preserved_corollary_label_line": 607,
        },
        "aux": {"path": str(ROOT / "injectives.aux"), "bytes": INJECTIVES_ARTIFACTS["injectives.aux"][0], "sha256": INJECTIVES_ARTIFACTS["injectives.aux"][1]},
        "log": {"path": str(ROOT / "injectives.log"), "bytes": INJECTIVES_ARTIFACTS["injectives.log"][0], "sha256": INJECTIVES_ARTIFACTS["injectives.log"][1]},
    }
    for key, expected in expected_artifact_rows.items():
        require(audit.get("artifacts", {}).get(key) == expected, f"D1007 audit {key} binding drift")
    pdf = audit.get("artifacts", {}).get("pdf", {})
    require(
        (pdf.get("path"), pdf.get("bytes"), pdf.get("sha256"), pdf.get("pages"), pdf.get("media_box"), pdf.get("rotation"), pdf.get("encrypted"))
        == (str(ROOT / "injectives.pdf"), INJECTIVES_ARTIFACTS["injectives.pdf"][0], INJECTIVES_ARTIFACTS["injectives.pdf"][1], 40, [0, 0, 612, 792], 0, False),
        "D1007 audit PDF binding drift",
    )
    require(
        audit.get("aux_labels")
        == [
            r"\newlabel{lemma-injective-left-module-stalks}{{4.2}{6}{}{subsection.4.2}{}}",
            r"\newlabel{lemma-injective-module-stalks}{{4.3}{8}{}{subsection.4.3}{}}",
        ],
        "D1007 audit AUX-label drift",
    )
    for section_name in ("source_audit", "convention_audit", "math_audit", "build_audit", "pdf_audit"):
        require(audit.get(section_name, {}).get("status") == "STRICT_PASS", f"D1007 {section_name} drift")
    require(
        audit.get("build_audit", {}).get("label") == "Lemma 4.2"
        and audit.get("build_audit", {}).get("label_page") == 6
        and audit.get("build_audit", {}).get("preserved_corollary") == "Lemma 4.3"
        and audit.get("build_audit", {}).get("preserved_corollary_page") == 8
        and audit.get("build_audit", {}).get("new_block_box_diagnostics") == 0,
        "D1007 build audit drift",
    )
    require(
        audit.get("pdf_audit", {}).get("visual_pages") == [6, 7, 8]
        and audit.get("pdf_audit", {}).get("strict_page_parse_errors") == 0
        and audit.get("pdf_audit", {}).get("content_stream_decode_errors") == 0
        and audit.get("pdf_audit", {}).get("poppler_full_text_interpretation") == "PASS",
        "D1007 PDF audit drift",
    )
    require(
        audit.get("external_constraints", {}).get("github", {}).get("status") == "temporarily_unavailable"
        and "No GitHub inspection" in audit.get("external_constraints", {}).get("github", {}).get("effect", ""),
        "D1007 GitHub constraint drift",
    )
    require(
        any("right modules" in claim for claim in audit.get("nonclaims", []))
        and any("internal Hom" in claim and "abelian groups" in claim for claim in audit.get("nonclaims", []))
        and any("No source repair" in claim and "GitHub action" in claim for claim in audit.get("nonclaims", [])),
        "D1007 nonclaim drift",
    )
    return {"receipt": record(D1007_AUDIT, "D1007_CHECK.json"), "status": "STRICT_PASS", "errors": []}


def verify_builds() -> dict[str, object]:
    artifacts = expected_artifacts()
    for name, expected in artifacts.items():
        require_identity(ROOT / name, expected)
    r42 = BASE.BASE.BASE.BASE.BASE.BASE.BASE.load_legacy_validator()
    specs = {
        **r42.BUILD_SPECS,
        "derived": {"pages": 148, "visual": [72, 73, 74, 75, 76, 77]},
        "cohomology": {"pages": 222, "visual": [27, 28, 29, 30, 31, 32]},
        "injectives": {"pages": 40, "visual": [6, 7, 8]},
    }
    aux_lines = {**r42.EXPECTED_AUX_LINES}
    aux_lines["derived.aux"] = (
        r"\newlabel{lemma-right-satellites-to-right-derived-functors}{{20.4}{72}{Comparison from satellites to right derived functors}{subsection.20.4}{}}",
        r"\newlabel{lemma-right-derived-functor-commutes-filtered-colimits}{{20.6}{74}{Filtered colimits of objects}{subsection.20.6}{}}",
        r"\newlabel{equation-filtered-colimit-right-derived-objects-1}{{20.6.1}{74}{Right derived functors and injective resolutions}{equation.20.6.1}{}}",
        r"\newlabel{equation-filtered-colimit-right-derived-objects-2}{{20.6.2}{74}{Right derived functors and injective resolutions}{equation.20.6.2}{}}",
        r"\newlabel{equation-filtered-colimit-right-derived-objects-3}{{20.6.3}{75}{Right derived functors and injective resolutions}{equation.20.6.3}{}}",
    )
    aux_lines["cohomology.aux"] = (
        r"\newlabel{lemma-crossed-homomorphism-torsor-obstruction}{{4.4}{5}{The torsor obstruction of a crossed homomorphism}{subsection.4.4}{}}",
        r"\newlabel{lemma-pointwise-flasque-envelope-groups}{{12.2}{22}{Pointwise flasque envelope}{subsection.12.2}{}}",
        r"\newlabel{lemma-flasque-group-torsors-trivial}{{12.3}{22}{}{subsection.12.3}{}}",
        r"\newlabel{lemma-pointwise-envelope-crossed-homomorphism}{{12.4}{23}{The crossed quotient of a pointwise envelope}{subsection.12.4}{}}",
        r"\newlabel{lemma-pointwise-envelope-torsor-bijection}{{12.5}{24}{Pointwise envelopes lift torsors uniquely}{subsection.12.5}{}}",
        r"\newlabel{lemma-pointwise-envelope-degree-two-boundary}{{12.8}{26}{The degree-two boundary of a pointwise envelope}{subsection.12.8}{}}",
        r"\newlabel{lemma-holomorphic-logarithmic-derivative-obstruction}{{12.9}{28}{The holomorphic logarithmic-derivative obstruction}{subsection.12.9}{}}",
        r"\newlabel{definition-fine-abelian-sheaf}{{22.6}{55}{Fine abelian sheaves}{subsection.22.6}{}}",
        r"\newlabel{lemma-fine-phi-soft-and-tensor}{{22.7}{55}{}{subsection.22.7}{}}",
        r"\newlabel{lemma-cartan-resolution-fine-torsion-free}{{22.16}{59}{Cartan resolution}{subsection.22.16}{}}",
    )
    aux_lines["injectives.aux"] = (
        r"\newlabel{lemma-injective-left-module-stalks}{{4.2}{6}{}{subsection.4.2}{}}",
        r"\newlabel{lemma-injective-module-stalks}{{4.3}{8}{}{subsection.4.3}{}}",
        r"\newlabel{theorem-injective-embedding-grothendieck}{{12.7}{23}{}{subsection.12.7}{}}",
        r"\newlabel{lemma-filtered-diagram-injective-resolutions}{{12.8}{24}{Compatible injective resolutions of filtered systems}{subsection.12.8}{}}",
        r"\newlabel{section-K-injective}{{13}{25}{K-injectives in Grothendieck categories}{section.13}{}}",
        r"\newlabel{lemma-surjection-bounded-size}{{13.1}{25}{}{subsection.13.1}{}}",
        r"\newlabel{lemma-characterize-K-injective}{{13.3}{26}{}{subsection.13.3}{}}",
    )
    forbidden = [
        r"(?m)^! (?:LaTeX|Package|Undefined|Emergency|File|Missing|Extra|Use of|Runaway|Paragraph)",
        r"(?m)^LaTeX Warning:", r"(?m)^Package .* Warning:",
        r"undefined references", r"undefined citations",
        r"Rerun to get cross-references right", r"Label\(s\) may have changed",
    ]
    builds: dict[str, object] = {}
    for chapter, spec in specs.items():
        log = (ROOT / f"{chapter}.log").read_text(encoding="utf-8", errors="replace")
        hits = [pattern for pattern in forbidden if re.search(pattern, log)]
        require(not hits, f"{chapter} build diagnostics: {hits}")
        output = re.findall(
            rf"Output written on {re.escape(chapter)}\.pdf \(([0-9]+) pages?, ([0-9]+) bytes\)\.",
            log,
        )
        require(output == [(str(spec["pages"]), str(artifacts[f"{chapter}.pdf"][0]))], f"{chapter} output receipt drift")
        lines = set((ROOT / f"{chapter}.aux").read_text(encoding="utf-8").splitlines())
        require(all(line in lines for line in aux_lines[f"{chapter}.aux"]), f"{chapter} AUX evidence drift")
        if chapter == "injectives":
            box_ranges = [
                (int(start), int(end or start))
                for start, end in re.findall(r"Overfull \\hbox .*? at lines? ([0-9]+)(?:--([0-9]+))?", log)
            ]
            require(
                not any(start <= 623 and end >= 486 for start, end in box_ranges),
                "D1007 source block has an overfull box",
            )
        builds[chapter] = {
            "tex": record(ROOT / f"{chapter}.tex"),
            "aux": record(ROOT / f"{chapter}.aux"),
            "log": record(ROOT / f"{chapter}.log"),
            "pdf": record(ROOT / f"{chapter}.pdf"),
            "pdf_pages": spec["pages"],
            "visual_reviewed_pages": spec["visual"],
            "undefined_references": 0,
            "undefined_citations": 0,
            "rerun_notices": 0,
            "new_block_overfull_boxes": 0,
        }
    tex = (ROOT / "injectives.tex").read_text(encoding="utf-8")
    require(tex.count(r"\label{lemma-injective-left-module-stalks}") == 1, "D1007 source label multiplicity drift")
    require(tex.count(r"\label{lemma-injective-module-stalks}") == 1, "D1007 preserved-label multiplicity drift")
    for evidence in (
        "For this lemma only, rings are not required to be commutative.",
        "All modules are unital left",
        r"(r_1, \ldots, r_n) \longmapsto \sum r_i a_i",
        r"L = \{r \in R \mid rz \in M'\}",
        "Here we use only its abelian group structure",
        r"\ref{sheaves-lemma-j-shriek-modules}",
        "The second map is injective, as may be checked on stalks.",
        r"\label{lemma-injective-module-stalks}",
        r"\ref{lemma-injective-left-module-stalks}",
    ):
        require(evidence in tex, f"D1007 source proof/nonclaim drift: {evidence}")
    inherited = strict_json(SOURCE / "r49-check.json").get("builds", {}).get("independent_audits", {})
    require(
        set(inherited)
        == {f"D{number:06d}" for number in range(996, 1016)},
        "r49 independent-audit inheritance drift",
    )
    require(inherited["D001013"].get("status") == "STRICT_PASS", "D001013 audit inheritance drift")
    require(inherited["D001014"].get("status") == "STRICT_PASS", "D001014 audit inheritance drift")
    require(inherited["D001015"].get("status") == "STRICT_PASS", "D001015 audit inheritance drift")
    builds["independent_audits"] = {
        **inherited,
        "D001016": {
            "status": "STRICT_PASS",
            "receipt": record(D1007_AUDIT, "D1007_CHECK.json"),
            "scope": [
                "associative unital rings and unital left modules",
                "left Baer criterion and left-oriented generator map",
                "finite-presentation stalk-Hom comparison as abelian groups",
                "extension by zero and preserved commutative corollary",
                "40-page strict parse and pages 6-8 clean",
            ],
        },
    }
    return builds


def index_csv_bytes(rows: list[dict[str, str]]) -> bytes:
    fields = [
        "tag", "full_label", "file", "line", "kind", "short_label",
        "chapter", "section_label", "section_title", "text_sha256",
    ]
    return csv_bytes(fields, [{field: row.get(field, "") for field in fields} for row in rows])


def candidate_csv_bytes(rows: list[dict[str, str]]) -> bytes:
    fields = [
        "topic_id", "score", "hit_fields", "tag", "full_label", "file",
        "line", "kind", "section_title", "snippet", "status",
    ]
    return csv_bytes(fields, [{field: row.get(field, "") for field in fields} for row in rows])


def topic_map_csv_bytes(rows: list[dict[str, str]]) -> bytes:
    fields = [
        "topic_id", "label", "coverage", "confidence", "evidence_labels",
        "evidence_tags", "rationale", "review_state",
    ]
    return csv_bytes(fields, [{field: row.get(field, "") for field in fields} for row in rows])


def verify_scanner_oracle() -> dict[str, object]:
    mkidx = load_mkidx()
    index, errors, warnings, tex_hashes = mkidx.build_index()
    require(errors == [], f"Current bounded scanner errors: {errors}")
    require(tex_hashes == expected_tex_hashes(), "Current 119-file TeX hash oracle drift")
    require({path.name for path in ROOT.glob("*.tex")} == set(tex_hashes), "Live TeX filename surface drift")
    _, topics = load_csv(SOURCE / "topics.csv")
    candidates = mkidx.candidate_rows(index, topics)
    topic_map, map_errors, map_warnings = mkidx.topic_map_rows(index, topics)
    require(map_errors == [], f"Current topic-map errors: {map_errors}")
    warnings = [*warnings, *map_warnings]

    _, old_index = load_csv(SOURCE / "stx.csv")
    fields = list(old_index[0])
    old_by = {row["full_label"]: row for row in old_index}
    new_by = {row["full_label"]: {field: row[field] for field in fields} for row in index}
    full_new_by = {row["full_label"]: row for row in index}
    require(set(old_by) <= set(new_by), "Scanner removed an existing label")
    require(set(new_by) - set(old_by) == set(NEW_LABEL_ROWS), "D1007 new-label set drift")
    for label, expected_row in NEW_LABEL_ROWS.items():
        require(new_by[label] == expected_row, f"D1007 new-label row drift: {label}")
        require(full_new_by[label]["_text"] == NEW_LABEL_TEXTS[label], f"D1007 normalized scanner text drift: {label}")
        require(digest(NEW_LABEL_TEXTS[label].encode("utf-8")) == expected_row["text_sha256"], f"D1007 scanner text hash drift: {label}")
    require(len(NEW_LABEL_TEXT.encode("utf-8")) == 280, "D1007 normalized scanner text is not 280 bytes")
    require(new_by[PRESERVED_LABEL_ROW["full_label"]] == PRESERVED_LABEL_ROW, "D1007 preserved-label row drift")
    require(full_new_by[PRESERVED_LABEL_ROW["full_label"]]["_text"] == PRESERVED_LABEL_TEXT, "D1007 preserved-label text drift")
    require(len(PRESERVED_LABEL_TEXT.encode("utf-8")) == 207, "D1007 preserved normalized text is not 207 bytes")
    require(digest(PRESERVED_LABEL_TEXT.encode("utf-8")) == PRESERVED_LABEL_ROW["text_sha256"], "D1007 preserved scanner text hash drift")
    require(new_by[INHERITED_D1005_LABEL_ROW["full_label"]] == INHERITED_D1005_LABEL_ROW, "Inherited D1005-label row drift")
    require(new_by[INHERITED_D1004_LABEL_ROW["full_label"]] == INHERITED_D1004_LABEL_ROW, "Inherited D1004-label row drift")
    require(new_by[INHERITED_OBSTRUCTION_LABEL_ROW["full_label"]] == INHERITED_OBSTRUCTION_LABEL_ROW, "Inherited obstruction-label row drift")
    line_only = []
    for label in old_by:
        if old_by[label] != new_by[label]:
            if label == PRESERVED_LABEL_ROW["full_label"]:
                require(old_by[label]["line"] == "487", "D1007 preserved predecessor line drift")
                require(old_by[label]["text_sha256"] == "5C5A69BFB3DB0EFC5DDB62AE784636C82105B4E0EBB923424A3336DF7A5E0B63", "D1007 preserved predecessor text hash drift")
                require(
                    all(old_by[label][field] == new_by[label][field] for field in fields if field not in {"line", "text_sha256"}),
                    "D1007 preserved-label metadata drift",
                )
                continue
            require(
                all(old_by[label][field] == new_by[label][field] for field in fields if field != "line"),
                f"Existing label substantive metadata drift: {label}",
            )
            require(
                int(new_by[label]["line"]) - int(old_by[label]["line"]) == 89,
                f"Existing label line-shift drift: {label}",
            )
            line_only.append(label)
    require(Counter(old_by[label]["file"] for label in line_only) == Counter({"injectives.tex": 75}), "Existing label line-only oracle drift")

    _, old_candidates = load_csv(SOURCE / "tcand.csv")
    old_c = {(row["topic_id"], row["full_label"]): row for row in old_candidates}
    new_c = {(row["topic_id"], row["full_label"]): row for row in candidates}
    expected_added_candidates: set[tuple[str, str]] = set()
    expected_removed_candidates: set[tuple[str, str]] = set()
    require(set(new_c) - set(old_c) == expected_added_candidates, "Candidate-key addition drift")
    require(set(old_c) - set(new_c) == expected_removed_candidates, "Candidate-key removal drift")
    changed_candidates = []
    for key in set(old_c) & set(new_c):
        if old_c[key] != new_c[key]:
            require(
                all(old_c[key][field] == new_c[key][field] for field in old_c[key] if field != "line"),
                f"Existing candidate substantive metadata drift: {key}",
            )
            require(
                int(new_c[key]["line"]) - int(old_c[key]["line"]) == 89,
                f"Existing candidate line-shift drift: {key}",
            )
            changed_candidates.append(key)
    require(Counter(old_c[key]["file"] for key in changed_candidates) == Counter({"injectives.tex": 51}), "Candidate line-only oracle drift")
    require(len(index) == 22062 and len(candidates) == 1270 and len(topic_map) == 13, "Scanner count oracle drift")
    require(sum(1 for row in index if row["tag"]) == 21437, "Official-tag join count drift")
    require(len(warnings) == 634, "Scanner warning count drift")
    for label in NEW_LABEL_ROWS:
        require(
            f"TeX label has no official tag in this snapshot: {label}" in warnings,
            f"D1007 no-official-tag warning drift: {label}",
        )
    serialized = {
        "stx.csv": index_csv_bytes(index),
        "tcand.csv": candidate_csv_bytes(candidates),
        "tmap.csv": topic_map_csv_bytes(topic_map),
    }
    for name, data in serialized.items():
        require((len(data), digest(data)) == EXPECTED_SCAN_OUTPUTS[name], f"Scanner serialized identity drift: {name}")
    return {
        "index": index,
        "candidates": candidates,
        "topic_map": topic_map,
        "warnings": warnings,
        "tex_hashes": tex_hashes,
        "serialized": serialized,
        "counts": EXPECTED_SCAN_COUNTS,
        "delta": {
            "changed_tex_files": ["injectives.tex"],
            "new_labels": 1,
            "existing_rows_line_number_only": 75,
            "existing_text_hash_changes": 1,
            "existing_other_metadata_changes": 0,
            "official_tag_changes": 0,
            "candidate_count_delta": 0,
            "candidate_keys_added": 0,
            "candidate_keys_removed": 0,
            "candidate_keys_added_values": [list(key) for key in sorted(expected_added_candidates)],
            "candidate_keys_removed_values": [list(key) for key in sorted(expected_removed_candidates)],
            "existing_candidate_rows_line_number_only": 51,
        },
    }


def verify_external() -> dict[str, object]:
    require_plain_directory(SOURCE)
    entries = list(SOURCE.iterdir())
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SOURCE), "r49 predecessor surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected r49 predecessor subdirectory")
    records = []
    for name, expected in sorted(EXPECTED_SOURCE.items()):
        require_identity(SOURCE / name, expected)
        records.append(record(SOURCE / name))
    require(
        (len(records), sum(int(item["bytes"]) for item in records), aggregate(records)) == EXPECTED_SOURCE_SURFACE,
        "r49 predecessor aggregate drift",
    )
    payload_records = [item for item in records if item["name"] != "r49-check.json"]
    require(
        (len(payload_records), sum(int(item["bytes"]) for item in payload_records), aggregate(payload_records)) == EXPECTED_SOURCE_PAYLOAD_SURFACE,
        "r49 predecessor payload aggregate drift",
    )
    predecessor = strict_json(SOURCE / "r49-check.json")
    require(predecessor.get("schema") == "tohoku-stacks-mapping-successor-r49-v1", "r49 predecessor receipt schema drift")
    require(predecessor.get("status") == "PASS" and predecessor.get("errors") == [], "r49 predecessor receipt not PASS")
    require(predecessor.get("deltas", {}).get("decisions") == 1015, "r49 predecessor decision gate drift")
    require(predecessor.get("deltas", {}).get("mapping_counts", {}).get("dispositions", {}).get("new_statement") == 16, "r49 D1007 predecessor gap gate drift")
    require(predecessor.get("deltas", {}).get("remaining_gap_class_dispositions") == 50, "r49 predecessor gap-count drift")
    for name, expected in expected_runtime().items():
        require_identity(ROOT / name, expected)
    for name, expected in BASE.BASE.BASE.BASE.BASE.BASE.BASE.load_legacy_validator().EXPECTED_AUTHORITY.items():
        require_identity(AUTHORITY / name, expected)
    require(Path(sys.executable).resolve() == EXPECTED_PYTHON.resolve(), "Python executable path drift")
    require_identity(EXPECTED_PYTHON, EXPECTED_PYTHON_IDENTITY)
    require(sys.version_info[:3] == (3, 13, 9) and sys.implementation.cache_tag == "cpython-313", "Python runtime drift")
    semantic = verify_semantic()
    repairs = verify_repairs()
    d1007 = verify_d1007_audit()
    builds = verify_builds()
    scanner = verify_scanner_oracle()
    return {
        "predecessor": {
            "name": "tohoku_r49",
            "files": records,
            "file_count": len(records),
            "bytes": sum(int(item["bytes"]) for item in records),
            "aggregate_sha256": aggregate(records),
            "payload_file_count": len(payload_records),
            "payload_bytes": sum(int(item["bytes"]) for item in payload_records),
            "payload_aggregate_sha256": aggregate(payload_records),
        },
        "semantic": semantic,
        "repairs": repairs,
        "d1007_audit": d1007,
        "builds": builds,
        "scanner": scanner,
    }


def expected_units(cfg: dict) -> list[dict[str, str]]:
    return BASE.expected_units(cfg)


def expected_map(cfg: dict, units: list[dict[str, str]], scanner: dict[str, object], decisions_path: Path) -> list[dict[str, str]]:
    return BASE.expected_map(cfg, units, scanner, decisions_path)


def verify_stage(root: Path, receipt_mode: bool) -> dict[str, object]:
    external = verify_external()
    require_plain_directory(root)
    entries = list(root.iterdir())
    expected_names = PAYLOAD | ({"r50-check.json"} if receipt_mode else set())
    require({path.name for path in entries if path.is_file()} == expected_names, "Stage/target file surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected stage/target subdirectory")

    cfg = strict_json(root / "cfg.json")
    require(cfg.get("dossier_id") == "tohoku_r50", "r50 cfg dossier ID drift")
    require(cfg.get("expected_units") == 991, "r50 cfg unit count drift")
    require(cfg.get("semantic_successor", {}).get("generation") == "sem/r17", "r50 cfg semantic generation drift")
    require(cfg.get("semantic_successor", {}).get("surface_files") == 18, "r50 cfg semantic file count drift")
    require(cfg.get("semantic_successor", {}).get("surface_bytes") == EXPECTED_SEM_SURFACE[1], "r50 cfg semantic bytes drift")
    require(cfg.get("semantic_successor", {}).get("surface_sha256") == EXPECTED_SEM_SURFACE[2], "r50 cfg semantic aggregate drift")
    primary = cfg.get("inputs", {}).get("primary", {})
    require(primary.get("source_file") == "sem/r17/nodes.csv", "r50 cfg primary source drift")
    require(primary.get("sha256") == EXPECTED_SEM["nodes.csv"][1], "r50 cfg node pin drift")
    require(cfg.get("inputs", {}).get("sem_manifest", {}).get("sha256") == EXPECTED_SEM["manifest.json"][1], "r50 cfg manifest pin drift")
    require(cfg.get("inputs", {}).get("sem_validation", {}).get("sha256") == EXPECTED_SEM["validation.json"][1], "r50 cfg validation pin drift")

    intake = strict_json(root / "intake.json")
    check = strict_json(root / "check.json")
    mcheck = strict_json(root / "mcheck.json")
    for name, value in (("intake", intake), ("scan", check), ("map", mcheck)):
        require(value.get("status") == "PASS" and value.get("errors") == [], f"{name} receipt not PASS")
    require(mcheck.get("outputs_promoted") is True, "Mapping outputs not promoted")
    for name in ("intake.json", "issues.csv", "tmap.csv", "topics.csv", "ucand.csv", "units.csv"):
        require((root / name).read_bytes() == (SOURCE / name).read_bytes(), f"{name} drift")

    scanner = external["scanner"]
    for name in ("stx.csv", "tcand.csv", "tmap.csv"):
        require((root / name).read_bytes() == scanner["serialized"][name], f"{name} does not match exact live oracle")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r50 scan counts drift")
    require(check.get("warnings") == scanner["warnings"], "r50 scan warnings drift")
    require(check.get("tex_sha256") == scanner["tex_hashes"], "r50 scan TeX hashes drift")
    runtime = expected_runtime()
    require(check.get("sha256", {}).get("tags/tags") == runtime["tags/tags"][1], "r50 scan tag hash drift")

    unit_fields, units = load_csv(root / "units.csv")
    projected_units = expected_units(cfg)
    require(unit_fields == BASE.BASE.BASE.BASE.BASE.BASE.BASE.load_intake().FIELDS, "r50 unit schema drift")
    require(units == projected_units, "r50 units differ from exact sem/r17 intake projection")
    require(intake.get("counts", {}).get("units") == 991, "r50 intake unit receipt drift")

    fields, old_decisions = load_csv(SOURCE / "dec.csv")
    new_fields, decisions = load_csv(root / "dec.csv")
    require(fields == new_fields, "Decision schema drift")
    require([row["decision_id"] for row in decisions] == [f"D{number:06d}" for number in range(1, 1017)], "Decision sequence drift")
    require(decisions[:1015] == old_decisions and decisions[1015:] == DECISION_ROWS, "Decision prefix/appended rows drift")
    require((root / "dec.csv").read_bytes().startswith((SOURCE / "dec.csv").read_bytes()), "Decision byte prefix drift")
    anchors = {"D000513": (DECISION_ROWS[0], "new_statement")}
    old_by_id = {row["decision_id"]: row for row in old_decisions}
    for decision_id, (successor, expected_disposition) in anchors.items():
        anchor = old_by_id.get(decision_id, {})
        require(anchor.get("unit_id") == successor["unit_id"], f"{decision_id} supersession unit drift")
        require(anchor.get("disposition") == expected_disposition, f"{decision_id} predecessor disposition drift")

    _, issues = load_csv(root / "issues.csv")
    require(len(issues) == 29 and all(row["status"] == "resolved" for row in issues), "r50 issue ledger drift")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r50 mapping counts drift")
    require(mcheck.get("warnings") == check.get("warnings"), "Map/scan warning mismatch")
    _, undecided = load_csv(root / "ucand.csv")
    require(undecided == [], "Unexpected undecided candidates")

    map_fields, mapped = load_csv(root / "map.csv")
    expected_fields = [
        "unit_id", "item", "unit_type", "parent_id", "source_start",
        "source_end", "source_loc", "authority_sha256", "source_topics",
        "topic_evidence_labels", "topic_evidence_tags", "decision_id",
        "disposition", "review_state", "stacks_labels", "stacks_tags",
        "rationale",
    ]
    require(map_fields == expected_fields, "r50 map schema drift")
    projected_map = expected_map(cfg, projected_units, scanner, root / "dec.csv")
    require(mapped == projected_map, "r50 map differs from independent sem/r17 + live scanner + ledger replay")
    _, old_map = load_csv(SOURCE / "map.csv")
    old_by = {row["unit_id"]: row for row in old_map}
    new_by = {row["unit_id"]: row for row in mapped}
    target_units = {row["unit_id"] for row in DECISION_ROWS}
    require(set(old_by) == set(new_by) and len(new_by) == 991, "Map stable-unit set drift")
    for unit_id in set(new_by) - target_units:
        require(new_by[unit_id] == old_by[unit_id], f"Unauthorized r50 map mutation: {unit_id}")
    authorized_fields_by_decision = {
        "D001016": {"decision_id", "disposition", "stacks_labels", "rationale"},
    }
    for decision in DECISION_ROWS:
        unit_id = decision["unit_id"]
        authorized_fields = authorized_fields_by_decision[decision["decision_id"]]
        changed_fields = {field for field in expected_fields if old_by[unit_id][field] != new_by[unit_id][field]}
        require(changed_fields == authorized_fields, f"{decision['decision_id']} map mutation field set drift")
        for field in authorized_fields - {"stacks_tags"}:
            require(new_by[unit_id][field] == decision[field], f"{decision['decision_id']} mapped {field} drift")
        require(new_by[unit_id]["stacks_tags"] == "", f"{decision['decision_id']} unexpectedly claims an official tag")
    for decision_id, unit_id in (
        ("D001013", "tohoku:construction:diagram-category-resolution"),
        ("D001014", "tohoku:construction:inductive-injective-resolutions"),
        ("D001015", "tohoku:proposition:3.6.2"),
    ):
        require(new_by[unit_id]["decision_id"] == decision_id, f"{decision_id} no longer selected")
    for unit_id in (
        "tohoku:subitem:3.6.2:a",
        "tohoku:subitem:3.6.2:b",
        "tohoku:proof:3.6.2:p1",
        "tohoku:proof:3.6.2:p2",
        "tohoku:eq:derived-colimit-comparison",
        "tohoku:eq:colimit-resolution",
        "tohoku:eq:T-acyclic-computation",
        "tohoku:eq:T-colimit-complex",
        "tohoku:eq:cohomology-colimit-comparison",
        "tohoku:eq:derived-colimit-isomorphism",
    ):
        equation = new_by[unit_id]
        require(equation == old_by[unit_id], f"Structural child changed: {unit_id}")
        require(
            (
                equation["decision_id"], equation["disposition"],
                equation["review_state"], equation["stacks_labels"],
                equation["stacks_tags"], equation["rationale"],
            )
            == ("", "structural_only", "inherits_parent", "", "", "Embedded source component; inherit the parent disposition."),
            f"Structural child inheritance drift: {unit_id}",
        )
    gap_count = sum(EXPECTED_MAPPING_COUNTS["dispositions"][name] for name in ("existing_weaker", "extend_existing", "new_statement", "new_section"))
    require(gap_count == 49, "Gap-class arithmetic drift")
    status = (root / "STATUS.md").read_text(encoding="utf-8")
    for token in (
        "sem/r17", "D001016", "D000513", "49 gap-class",
        "tohoku:proposition:4.1.2",
        "injectives-lemma-injective-left-module-stalks",
        "existing_stronger", "left Noetherian", "left modules", "commutative corollary",
    ):
        require(token in status, f"STATUS missing token: {token}")

    result = {
        "status": "PASS",
        "errors": [],
        "stable_units": 991,
        "decisions": 1016,
        "decisions_appended": DECISION_ROWS,
        "active_source_issues": [],
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": EXPECTED_SCAN_COUNTS,
        "scanner_delta": scanner["delta"],
        "remaining_gap_class_dispositions": 49,
        "semantic_generation": "sem/r17",
        "authorized_map_mutations": {
            "units": sorted(target_units),
            "fields_by_decision": {
                decision_id: sorted(fields)
                for decision_id, fields in sorted(authorized_fields_by_decision.items())
            },
            "unchanged_units": 990,
        },
        "byte_identical_payloads": ["intake.json", "issues.csv", "tmap.csv", "topics.csv", "ucand.csv", "units.csv"],
        "external_evidence": {
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "repair_aggregate_sha256": external["repairs"]["aggregate_sha256"],
            "d1007_audit_sha256": external["d1007_audit"]["receipt"]["sha256"],
        },
    }

    if receipt_mode:
        receipt = strict_json(root / "r50-check.json")
        require(receipt.get("schema") == "tohoku-stacks-mapping-successor-r50-v1", "r50 receipt schema drift")
        require(receipt.get("status") == "PASS" and receipt.get("errors") == [], "r50 receipt not PASS")
        require(receipt.get("deltas") == result, "r50 receipt delta replay mismatch")
        require(receipt.get("files") == [record(root / name) for name in sorted(PAYLOAD)], "r50 receipt output records drift")
        require(receipt.get("predecessor_dossier") == external["predecessor"], "r50 receipt predecessor evidence drift")
        require(receipt.get("semantic_source") == external["semantic"], "r50 receipt semantic evidence drift")
        require(receipt.get("source_repairs") == external["repairs"], "r50 receipt repair evidence drift")
        require(receipt.get("decision_audit") == external["d1007_audit"], "r50 receipt D1007 evidence drift")
        require(receipt.get("builds") == external["builds"], "r50 receipt build evidence drift")
        execution = receipt.get("execution", {})
        require(execution.get("contract") == "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion_with_rollback", "r50 execution contract drift")
        require(execution.get("attestation") == expected_execution_attestation(), "r50 execution attestation replay drift")
    return result


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R50_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if not raw:
        return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r50.py", "bytes": actual[0], "sha256": actual[1]}
    expected = json.loads(raw)
    require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator same-bytes attestation drift")
    return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r50.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not os.path.lexists(TARGET), f"No-overwrite r50 target already exists: {TARGET}")
        require(not os.path.lexists(STAGE), f"Unresolved r50 transaction exists: {STAGE}")
        external = verify_external()
        result = {
            "schema": "tohoku-r50-static-input-audit-v1",
            "status": "PASS",
            "errors": [],
            "attestation": attestation,
            "target_absent": True,
            "stage_absent": True,
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "predecessor_payload_aggregate_sha256": external["predecessor"]["payload_aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "d1007_audit": external["d1007_audit"],
            "scanner_delta": external["scanner"]["delta"],
            "builds": external["builds"],
            "projected_mapping_counts": EXPECTED_MAPPING_COUNTS,
            "launch_authorized": False,
        }
    else:
        result = {
            "schema": "tohoku-r50-stage-validation-v1",
            "attestation": attestation,
            **verify_stage(args.stage.resolve(), args.receipt),
        }
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
