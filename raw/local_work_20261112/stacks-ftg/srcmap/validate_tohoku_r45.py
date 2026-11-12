#!/usr/bin/env python3
"""Independent bounded validator for the frozen no-overwrite Tohoku r45 successor."""

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
SOURCE = ROOT / "tohoku_r44"
TARGET = ROOT / "tohoku_r45"
STAGE = ROOT / ".tohoku-r45-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r17"
AUTHORITY = PROJECT / "authority_snapshot"
BASE_VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r44.py"
BASE_BUILDER = ROOT / "srcmap" / "build_tohoku_r44.py"
D1002_AUDIT = ROOT / "D1002_CHECK.json"
EXPECTED_BASE_VALIDATOR = (
    32362,
    "69AB91B9B2D657C354FF0B491D041EC0BA99EFE73E238F12FBC3F3B3B45BE5F4",
)
EXPECTED_BASE_BUILDER = (
    18470,
    "96C3D9CCF9D32A7B8DE60ACD4735E521D897510FEE6272D9B59952C5401A2260",
)
EXPECTED_PYTHON = Path(r"user\miniconda3\python.exe")
EXPECTED_PYTHON_IDENTITY = (
    104264,
    "7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264",
)
EXPECTED_D1002_AUDIT = (
    4949,
    "5DFC445C3C0D3FB2DF77748E3069FB22B613A375F74CC953B04F62571083C768",
)

EXPECTED_SOURCE = {
    "STATUS.md": (1017, "E951AFFACD1327D2CACF3D9151E6CE2C129474A802F956F532AB432DB61F97C7"),
    "cfg.json": (5151, "2232AF92B842B80943DC3B78B7140669C94466410A379701E1A18ACFBA906AE4"),
    "check.json": (76954, "CA49E4447E290BE427D05D6018088EDF014D5B1A1D4FF12767D26282A5C0DBE9"),
    "dec.csv": (360565, "BA363734CB8D1630D55F12D5A561B77EB42789178A57E61B6E3E5F650015E0BC"),
    "intake.json": (1578, "8279157B8AA7F6AA006E2C434C34D2A7988836D63C25B3465B93896D62E22801"),
    "issues.csv": (29535, "3439D68823BF69087F025976FB0AC41C2C4D93B8BFB4E63D6FD3267DB6AC178A"),
    "map.csv": (473630, "466DE4DBEDE2FFE86138A705AEC51EAC12055E6500A5EACB6811DB59952DB6CD"),
    "mcheck.json": (66782, "72FD582BA5005FD9F6D8FAC8C8268542D3C00EBF54AF1C00869259A707380916"),
    "r44-check.json": (25404, "B4D123864469369C01364A8584CBC9E990234C6BD2CC0F9A57D029B67AE1FB5F"),
    "stx.csv": (5273652, "4E8094C09A8856D976E255FC70B400D35CC9C6995D14C36E7CE478838AC7538D"),
    "tcand.csv": (483153, "617F794ABBF0EF39EF08DE2CD1DA8E0CE8B4093319EFF4C55677CA0B29B58F46"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (392568, "3AB04435EEDD9DE59E61DF2443812C2F555DD6CA85542DC7F9C6BBE59DB03081"),
}
EXPECTED_SOURCE_PAYLOAD_SURFACE = (
    14,
    7169582,
    "23472A8673EEEA9A253DC03D8BB00549F0BB80153A46FEDE31BB21363AF88308",
)
EXPECTED_SOURCE_SURFACE = (
    15,
    7194986,
    "C6A19C77DE322D231BB697FEAC477A467BE446A473C0D9BDF3724D4971C831BD",
)

COHOMOLOGY_ARTIFACTS = {
    "cohomology.tex": (834157, "F4F65D273459C98E1F5ACA9B29F929C7BD5F2384B17327290D609D7776EF63EE"),
    "cohomology.aux": (52217, "BD8ECC2E1552C1FB09A81CB2FD398CFE4D7B6D9925D8D24713B98DB0BBA7B6ED"),
    "cohomology.log": (47334, "691B0A79302DB90890D361C4E72441FBA742916FB6BF0CEAEDABF69BA03A6CD1"),
    "cohomology.pdf": (1856980, "09993F4670E57353989005D326AE6495741A63B5D8A027733BD5FF89B1D7C332"),
}

DECISION_ROWS = [
    {
        "decision_id": "D001002",
        "unit_id": "tohoku:claim:3.4.2:H1-bijection",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-pointwise-envelope-torsor-bijection",
        "rationale": "Stacks now proves the source's bijection on nonabelian H1 as a bijection between isomorphism classes of torsors. For A=Π(F), B=Π(G), C=Π(H), and P=AG, it identifies P=B×_C H and B→C as sectionwise surjective, proves every H-torsor lifts to a P-torsor, and proves uniqueness using the flasque twisted kernel A^E≅Π(F^E). It explicitly avoids the false general claim that flasqueness is local and asserts uniqueness only up to isomorphism.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000236",
    },
    {
        "decision_id": "D001003",
        "unit_id": "tohoku:construction:3.4.2:associated-P-bundle",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-pointwise-envelope-torsor-bijection",
        "rationale": "The same Stacks lemma translates the source's fibre-space construction into torsor language: extension of structure group from P to H is bijective on isomorphism classes, so every H-torsor E is induced from a P-torsor Q and Q is unique up to isomorphism. It does not claim a canonical chosen Q.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000241",
    },
    {
        "decision_id": "D001004",
        "unit_id": "tohoku:construction:3.4.2:dQ-obstruction",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-crossed-homomorphism-torsor-obstruction",
        "rationale": "Specializing the Stacks crossed-homomorphism obstruction to A=F', E=Q, and ker(u)=G constructs d_u(Q) in H^1(X,(F')^Q). Because the pointwise-envelope quotient makes u an epimorphism and F' abelian, the class is neutral exactly when Q reduces to a G-torsor, equivalently when [Q] lies in the image of G-torsor classes. No degree-two sign is asserted at this stage.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000242",
    },
]

EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "decisions": 1004,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 355,
        "existing_stronger": 38,
        "existing_weaker": 9,
        "extend_existing": 22,
        "historical_reference": 33,
        "new_section": 6,
        "new_statement": 19,
        "structural_only": 425,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 29,
    "unit_candidates": 0,
    "units": 991,
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22054,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1263,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_SCAN_OUTPUTS = {
    "stx.csv": (5273896, "535EB0E5493A5036A802FE2B96593BBF57160E5A5FAE8B3AEC74AEDE55DFCC07"),
    "tcand.csv": (483154, "349BB31F8C40E297EF0D2C3C6B8026CE202240A622F86C22FC5C6FE48D33C1F5"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
}
NEW_LABEL_ROW = {
    "tag": "",
    "full_label": "cohomology-lemma-pointwise-envelope-torsor-bijection",
    "file": "cohomology.tex",
    "line": "2395",
    "kind": "lemma",
    "short_label": "lemma-pointwise-envelope-torsor-bijection",
    "chapter": "Cohomology of Sheaves",
    "section_label": "section-flasque",
    "section_title": "Flasque sheaves",
    "text_sha256": "59032030733ABA5B2C5E8276BC700A7DF6B92711594E54E15BC31DE9C36E5AF2",
}
OBSTRUCTION_LABEL_ROW = {
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
    module = load_module(BASE_VALIDATOR, "tohoku_r45_pinned_r44_validator")
    require_identity(BASE_VALIDATOR, EXPECTED_BASE_VALIDATOR)
    return module


BASE = load_base_validator()
EXPECTED_SEM = dict(BASE.EXPECTED_SEM)
EXPECTED_SEM_SURFACE = BASE.EXPECTED_SEM_SURFACE
EXPECTED_SEM_PAYLOAD_SURFACE = BASE.EXPECTED_SEM_PAYLOAD_SURFACE


def expected_runtime() -> dict[str, tuple[int, str]]:
    return {
        **BASE.expected_runtime(),
        "srcmap/validate_tohoku_r44.py": EXPECTED_BASE_VALIDATOR,
        "srcmap/build_tohoku_r44.py": EXPECTED_BASE_BUILDER,
    }


def expected_repairs() -> dict[str, tuple[int, str]]:
    return BASE.expected_repairs()


def expected_artifacts() -> dict[str, tuple[int, str]]:
    return {**BASE.expected_artifacts(), **COHOMOLOGY_ARTIFACTS}


def expected_tex_hashes() -> dict[str, str]:
    hashes = dict(strict_json(SOURCE / "check.json")["tex_sha256"])
    require(len(hashes) == 119, "Predecessor TeX manifest is not 119 files")
    hashes["cohomology.tex"] = COHOMOLOGY_ARTIFACTS["cohomology.tex"][1]
    return hashes


def load_mkidx():
    return load_module(ROOT / "fga" / "mkidx.py", "tohoku_r45_pinned_mkidx")


def verify_semantic() -> dict[str, object]:
    return BASE.verify_semantic()


def verify_repairs() -> dict[str, object]:
    return BASE.verify_repairs()


def verify_d1002_audit() -> dict[str, object]:
    require_identity(D1002_AUDIT, EXPECTED_D1002_AUDIT)
    audit = strict_json(D1002_AUDIT)
    require(audit.get("schema") == "tohoku-stacks-d1002-audit-v1", "D1002 audit schema drift")
    require(audit.get("status") == "STRICT_PASS" and audit.get("errors") == [], "D1002 audit not STRICT_PASS")
    require(audit.get("decision") == "D001002", "D1002 audit decision drift")
    require(audit.get("unit") == DECISION_ROWS[0]["unit_id"], "D1002 audit unit drift")
    require(audit.get("stacks_label") == DECISION_ROWS[0]["stacks_labels"], "D1002 audit label drift")
    expected_artifacts = {
        "tex": {"path": str(ROOT / "cohomology.tex"), "bytes": COHOMOLOGY_ARTIFACTS["cohomology.tex"][0], "sha256": COHOMOLOGY_ARTIFACTS["cohomology.tex"][1]},
        "aux": {"path": str(ROOT / "cohomology.aux"), "bytes": COHOMOLOGY_ARTIFACTS["cohomology.aux"][0], "sha256": COHOMOLOGY_ARTIFACTS["cohomology.aux"][1]},
        "log": {"path": str(ROOT / "cohomology.log"), "bytes": COHOMOLOGY_ARTIFACTS["cohomology.log"][0], "sha256": COHOMOLOGY_ARTIFACTS["cohomology.log"][1]},
    }
    for key, expected in expected_artifacts.items():
        require(audit.get("artifacts", {}).get(key) == expected, f"D1002 audit {key} binding drift")
    pdf = audit.get("artifacts", {}).get("pdf", {})
    require(
        (pdf.get("path"), pdf.get("bytes"), pdf.get("sha256"), pdf.get("pages"), pdf.get("media_box"), pdf.get("rotation"), pdf.get("encrypted"))
        == (str(ROOT / "cohomology.pdf"), COHOMOLOGY_ARTIFACTS["cohomology.pdf"][0], COHOMOLOGY_ARTIFACTS["cohomology.pdf"][1], 218, [0, 0, 612, 792], 0, False),
        "D1002 audit PDF binding drift",
    )
    require(audit.get("aux_label") == r"\newlabel{lemma-pointwise-envelope-torsor-bijection}{{12.5}{24}{Pointwise envelopes lift torsors uniquely}{subsection.12.5}{}}", "D1002 audit AUX label drift")
    require(audit.get("math_audit", {}).get("status") == "STRICT_PASS", "D1002 math audit drift")
    require(audit.get("build_audit", {}).get("status") == "STRICT_PASS", "D1002 build audit drift")
    require(audit.get("pdf_audit", {}).get("status") == "STRICT_PASS", "D1002 PDF audit drift")
    require(audit.get("pdf_audit", {}).get("visual_pages") == [23, 24, 25, 26, 27], "D1002 visual-page audit drift")
    require(len(audit.get("pdf_audit", {}).get("render_records", [])) == 5, "D1002 render-record count drift")
    return {"receipt": record(D1002_AUDIT, "D1002_CHECK.json"), "status": "STRICT_PASS", "errors": []}


def verify_builds() -> dict[str, object]:
    artifacts = expected_artifacts()
    for name, expected in artifacts.items():
        require_identity(ROOT / name, expected)
    r42 = BASE.BASE.load_legacy_validator()
    specs = {**r42.BUILD_SPECS, "cohomology": {"pages": 218, "visual": [23, 24, 25, 26, 27]}}
    aux_lines = {**r42.EXPECTED_AUX_LINES}
    aux_lines["cohomology.aux"] = (
        r"\newlabel{lemma-crossed-homomorphism-torsor-obstruction}{{4.4}{5}{The torsor obstruction of a crossed homomorphism}{subsection.4.4}{}}",
        r"\newlabel{lemma-pointwise-flasque-envelope-groups}{{12.2}{22}{Pointwise flasque envelope}{subsection.12.2}{}}",
        r"\newlabel{lemma-flasque-group-torsors-trivial}{{12.3}{22}{}{subsection.12.3}{}}",
        r"\newlabel{lemma-pointwise-envelope-crossed-homomorphism}{{12.4}{23}{The crossed quotient of a pointwise envelope}{subsection.12.4}{}}",
        r"\newlabel{lemma-pointwise-envelope-torsor-bijection}{{12.5}{24}{Pointwise envelopes lift torsors uniquely}{subsection.12.5}{}}",
        r"\newlabel{definition-fine-abelian-sheaf}{{22.6}{51}{Fine abelian sheaves}{subsection.22.6}{}}",
        r"\newlabel{lemma-fine-phi-soft-and-tensor}{{22.7}{51}{}{subsection.22.7}{}}",
        r"\newlabel{lemma-cartan-resolution-fine-torsion-free}{{22.16}{55}{Cartan resolution}{subsection.22.16}{}}",
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
    tex = (ROOT / "cohomology.tex").read_text(encoding="utf-8")
    require(tex.count(r"\label{lemma-pointwise-envelope-torsor-bijection}") == 1, "D1002 source label multiplicity drift")
    require(tex.count(r"\label{lemma-crossed-homomorphism-torsor-obstruction}") == 1, "D1004 source label multiplicity drift")
    for evidence in (
        r"\mathcal P=\mathcal B\times_{\mathcal C}\mathcal H",
        r"\mathcal A^{\mathcal E}\longrightarrow",
        r"\Pi(\mathcal F^{\mathcal E})",
        "Flasqueness is not a local property in general",
        "isomorphism class of such a lift is unique",
        r"d_u(\mathcal{E})\in",
        r"H^1\bigl(X,\mathcal{A}(\sigma)^{\mathcal{E}}\bigr)",
        "is an epimorphism, the converse holds as well.",
        r"\mathcal F'=\mathcal A/\mathcal F",
        r"It is an epimorphism and $u^{-1}(1)=\mathcal G$.",
    ):
        require(evidence in tex, f"D1002 source proof/nonclaim drift: {evidence}")
    inherited = strict_json(SOURCE / "r44-check.json").get("builds", {}).get("independent_audits", {})
    require(set(inherited) == {"D000996", "D000997", "D000998", "D000999", "D001000", "D001001"}, "r44 independent-audit inheritance drift")
    builds["independent_audits"] = {
        **inherited,
        "D001002": {
            "status": "STRICT_PASS",
            "receipt": record(D1002_AUDIT, "D1002_CHECK.json"),
            "scope": [
                "P equals B fibre-product-over C H",
                "sectionwise-surjective B to C",
                "torsor lifting by extension of structure group",
                "flasque twisted kernel via pointwise envelope",
                "bijection only on isomorphism classes",
                "no false local-flasqueness claim",
                "218-page strict parse and pages 23-27 clean",
            ],
        },
        "D001003": {
            "status": "STRICT_PASS",
            "receipt": record(D1002_AUDIT, "D1002_CHECK.json"),
            "scope": [
                "associated P-torsor existence",
                "uniqueness up to isomorphism",
                "no canonical chosen lift claim",
            ],
        },
        "D001004": {
            "status": "STRICT_PASS",
            "source_binding": record(ROOT / "cohomology.tex"),
            "aux_binding": record(ROOT / "cohomology.aux"),
            "scope": [
                "crossed-homomorphism torsor obstruction",
                "abelian H1 realization",
                "neutrality iff reduction for epimorphic u",
                "no degree-two sign claim",
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
    require(set(old_by) <= set(new_by), "Scanner removed an existing label")
    require(set(new_by) - set(old_by) == {NEW_LABEL_ROW["full_label"]}, "D1002 new-label set drift")
    require(new_by[NEW_LABEL_ROW["full_label"]] == NEW_LABEL_ROW, "D1002 new-label row drift")
    require(new_by[OBSTRUCTION_LABEL_ROW["full_label"]] == OBSTRUCTION_LABEL_ROW, "D1004 inherited label row drift")
    changed = []
    for label in old_by:
        if old_by[label] != new_by[label]:
            require(
                all(old_by[label][field] == new_by[label][field] for field in fields if field != "line"),
                f"Existing label substantive metadata drift: {label}",
            )
            changed.append(label)
    require(Counter(old_by[label]["file"] for label in changed) == Counter({"cohomology.tex": 462}), "Existing label line-only oracle drift")

    _, old_candidates = load_csv(SOURCE / "tcand.csv")
    old_c = {(row["topic_id"], row["full_label"]): row for row in old_candidates}
    new_c = {(row["topic_id"], row["full_label"]): row for row in candidates}
    require(set(old_c) == set(new_c), "Candidate key set drift")
    changed_candidates = []
    for key in old_c:
        if old_c[key] != new_c[key]:
            require(
                all(old_c[key][field] == new_c[key][field] for field in old_c[key] if field != "line"),
                f"Existing candidate substantive metadata drift: {key}",
            )
            changed_candidates.append(key)
    require(Counter(old_c[key]["file"] for key in changed_candidates) == Counter({"cohomology.tex": 193}), "Candidate line-only oracle drift")
    require(len(index) == 22054 and len(candidates) == 1263 and len(topic_map) == 13, "Scanner count oracle drift")
    require(sum(1 for row in index if row["tag"]) == 21437, "Official-tag join count drift")
    require(len(warnings) == 626, "Scanner warning count drift")
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
            "changed_tex_files": ["cohomology.tex"],
            "new_labels": 1,
            "existing_rows_line_number_only": 462,
            "existing_text_hash_changes": 0,
            "existing_other_metadata_changes": 0,
            "official_tag_changes": 0,
            "candidate_count_delta": 0,
            "candidate_keys_added": 0,
            "candidate_keys_removed": 0,
            "existing_candidate_rows_line_number_only": 193,
        },
    }


def verify_external() -> dict[str, object]:
    require_plain_directory(SOURCE)
    entries = list(SOURCE.iterdir())
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SOURCE), "r44 predecessor surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected r44 predecessor subdirectory")
    records = []
    for name, expected in sorted(EXPECTED_SOURCE.items()):
        require_identity(SOURCE / name, expected)
        records.append(record(SOURCE / name))
    require(
        (len(records), sum(int(item["bytes"]) for item in records), aggregate(records)) == EXPECTED_SOURCE_SURFACE,
        "r44 predecessor aggregate drift",
    )
    payload_records = [item for item in records if item["name"] != "r44-check.json"]
    require(
        (len(payload_records), sum(int(item["bytes"]) for item in payload_records), aggregate(payload_records)) == EXPECTED_SOURCE_PAYLOAD_SURFACE,
        "r44 predecessor payload aggregate drift",
    )
    predecessor = strict_json(SOURCE / "r44-check.json")
    require(predecessor.get("schema") == "tohoku-stacks-mapping-successor-r44-v1", "r44 predecessor receipt schema drift")
    require(predecessor.get("status") == "PASS" and predecessor.get("errors") == [], "r44 predecessor receipt not PASS")
    require(predecessor.get("deltas", {}).get("decisions") == 1001, "r44 predecessor decision gate drift")
    require(predecessor.get("deltas", {}).get("mapping_counts", {}).get("dispositions", {}).get("new_statement") == 21, "r44 D1002 predecessor gap gate drift")
    for name, expected in expected_runtime().items():
        require_identity(ROOT / name, expected)
    for name, expected in BASE.BASE.load_legacy_validator().EXPECTED_AUTHORITY.items():
        require_identity(AUTHORITY / name, expected)
    require(Path(sys.executable).resolve() == EXPECTED_PYTHON.resolve(), "Python executable path drift")
    require_identity(EXPECTED_PYTHON, EXPECTED_PYTHON_IDENTITY)
    require(sys.version_info[:3] == (3, 13, 9) and sys.implementation.cache_tag == "cpython-313", "Python runtime drift")
    semantic = verify_semantic()
    repairs = verify_repairs()
    d1002 = verify_d1002_audit()
    builds = verify_builds()
    scanner = verify_scanner_oracle()
    return {
        "predecessor": {
            "name": "tohoku_r44",
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
        "d1002_audit": d1002,
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
    expected_names = PAYLOAD | ({"r45-check.json"} if receipt_mode else set())
    require({path.name for path in entries if path.is_file()} == expected_names, "Stage/target file surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected stage/target subdirectory")

    cfg = strict_json(root / "cfg.json")
    require(cfg.get("dossier_id") == "tohoku_r45", "r45 cfg dossier ID drift")
    require(cfg.get("expected_units") == 991, "r45 cfg unit count drift")
    require(cfg.get("semantic_successor", {}).get("generation") == "sem/r17", "r45 cfg semantic generation drift")
    require(cfg.get("semantic_successor", {}).get("surface_files") == 18, "r45 cfg semantic file count drift")
    require(cfg.get("semantic_successor", {}).get("surface_bytes") == EXPECTED_SEM_SURFACE[1], "r45 cfg semantic bytes drift")
    require(cfg.get("semantic_successor", {}).get("surface_sha256") == EXPECTED_SEM_SURFACE[2], "r45 cfg semantic aggregate drift")
    primary = cfg.get("inputs", {}).get("primary", {})
    require(primary.get("source_file") == "sem/r17/nodes.csv", "r45 cfg primary source drift")
    require(primary.get("sha256") == EXPECTED_SEM["nodes.csv"][1], "r45 cfg node pin drift")
    require(cfg.get("inputs", {}).get("sem_manifest", {}).get("sha256") == EXPECTED_SEM["manifest.json"][1], "r45 cfg manifest pin drift")
    require(cfg.get("inputs", {}).get("sem_validation", {}).get("sha256") == EXPECTED_SEM["validation.json"][1], "r45 cfg validation pin drift")

    intake = strict_json(root / "intake.json")
    check = strict_json(root / "check.json")
    mcheck = strict_json(root / "mcheck.json")
    for name, value in (("intake", intake), ("scan", check), ("map", mcheck)):
        require(value.get("status") == "PASS" and value.get("errors") == [], f"{name} receipt not PASS")
    require(mcheck.get("outputs_promoted") is True, "Mapping outputs not promoted")
    for name in ("topics.csv", "issues.csv", "units.csv"):
        require((root / name).read_bytes() == (SOURCE / name).read_bytes(), f"{name} drift")

    scanner = external["scanner"]
    for name in ("stx.csv", "tcand.csv", "tmap.csv"):
        require((root / name).read_bytes() == scanner["serialized"][name], f"{name} does not match exact live oracle")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r45 scan counts drift")
    require(check.get("warnings") == scanner["warnings"], "r45 scan warnings drift")
    require(check.get("tex_sha256") == scanner["tex_hashes"], "r45 scan TeX hashes drift")
    runtime = expected_runtime()
    require(check.get("sha256", {}).get("tags/tags") == runtime["tags/tags"][1], "r45 scan tag hash drift")

    unit_fields, units = load_csv(root / "units.csv")
    projected_units = expected_units(cfg)
    require(unit_fields == BASE.BASE.load_intake().FIELDS, "r45 unit schema drift")
    require(units == projected_units, "r45 units differ from exact sem/r17 intake projection")
    require(intake.get("counts", {}).get("units") == 991, "r45 intake unit receipt drift")

    fields, old_decisions = load_csv(SOURCE / "dec.csv")
    new_fields, decisions = load_csv(root / "dec.csv")
    require(fields == new_fields, "Decision schema drift")
    require([row["decision_id"] for row in decisions] == [f"D{number:06d}" for number in range(1, 1005)], "Decision sequence drift")
    require(decisions[:1001] == old_decisions and decisions[1001:] == DECISION_ROWS, "Decision prefix/appended rows drift")
    require((root / "dec.csv").read_bytes().startswith((SOURCE / "dec.csv").read_bytes()), "Decision byte prefix drift")
    anchors = {"D000236": DECISION_ROWS[0], "D000241": DECISION_ROWS[1], "D000242": DECISION_ROWS[2]}
    old_by_id = {row["decision_id"]: row for row in old_decisions}
    for decision_id, successor in anchors.items():
        anchor = old_by_id.get(decision_id, {})
        require(anchor.get("unit_id") == successor["unit_id"], f"{decision_id} supersession unit drift")
        expected_disposition = "structural_only" if decision_id == "D000242" else "new_statement"
        require(anchor.get("disposition") == expected_disposition, f"{decision_id} predecessor disposition drift")

    _, issues = load_csv(root / "issues.csv")
    require(len(issues) == 29 and all(row["status"] == "resolved" for row in issues), "r45 issue ledger drift")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r45 mapping counts drift")
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
    require(map_fields == expected_fields, "r45 map schema drift")
    projected_map = expected_map(cfg, projected_units, scanner, root / "dec.csv")
    require(mapped == projected_map, "r45 map differs from independent sem/r17 + live scanner + ledger replay")
    _, old_map = load_csv(SOURCE / "map.csv")
    old_by = {row["unit_id"]: row for row in old_map}
    new_by = {row["unit_id"]: row for row in mapped}
    target_units = {row["unit_id"] for row in DECISION_ROWS}
    require(set(old_by) == set(new_by) and len(new_by) == 991, "Map stable-unit set drift")
    for unit_id in set(new_by) - target_units:
        require(new_by[unit_id] == old_by[unit_id], f"Unauthorized r45 map mutation: {unit_id}")
    authorized_fields = {"decision_id", "disposition", "review_state", "stacks_labels", "rationale"}
    for decision in DECISION_ROWS:
        unit_id = decision["unit_id"]
        changed_fields = {field for field in expected_fields if old_by[unit_id][field] != new_by[unit_id][field]}
        require(changed_fields == authorized_fields, f"{decision['decision_id']} map mutation field set drift")
        for field in authorized_fields:
            require(new_by[unit_id][field] == decision[field], f"{decision['decision_id']} mapped {field} drift")
        require(new_by[unit_id]["stacks_tags"] == "", f"{decision['decision_id']} unexpectedly claims an official tag")
    require(new_by["tohoku:claim:3.4.2:u-properties"]["decision_id"] == "D001001", "D001001 no longer selected")
    require(new_by["tohoku:construction:flabby-envelope"]["decision_id"] == "D001000", "D001000 no longer selected")
    require(new_by["tohoku:reduction:3.4.2:E-via-Q"]["decision_id"] == "D000310", "D000310 structural selection drift")
    require(new_by["tohoku:reduction:3.4.2:E-via-Q"]["disposition"] == "structural_only", "D000310 disposition drift")

    gap_count = sum(EXPECTED_MAPPING_COUNTS["dispositions"][name] for name in ("existing_weaker", "extend_existing", "new_statement", "new_section"))
    require(gap_count == 56, "Gap-class arithmetic drift")
    status = (root / "STATUS.md").read_text(encoding="utf-8")
    for token in ("sem/r17", "D001002", "D001003", "D001004", "D000236", "D000241", "D000242", "D001001", "56 gap-class"):
        require(token in status, f"STATUS missing token: {token}")

    result = {
        "status": "PASS",
        "errors": [],
        "stable_units": 991,
        "decisions": 1004,
        "decisions_appended": DECISION_ROWS,
        "active_source_issues": [],
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": EXPECTED_SCAN_COUNTS,
        "scanner_delta": scanner["delta"],
        "remaining_gap_class_dispositions": 56,
        "semantic_generation": "sem/r17",
        "authorized_map_mutations": {
            "units": sorted(target_units),
            "fields_each": sorted(authorized_fields),
            "unchanged_units": 988,
        },
        "byte_identical_payloads": ["topics.csv", "issues.csv", "units.csv"],
        "external_evidence": {
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "repair_aggregate_sha256": external["repairs"]["aggregate_sha256"],
            "d1002_audit_sha256": external["d1002_audit"]["receipt"]["sha256"],
        },
    }

    if receipt_mode:
        receipt = strict_json(root / "r45-check.json")
        require(receipt.get("schema") == "tohoku-stacks-mapping-successor-r45-v1", "r45 receipt schema drift")
        require(receipt.get("status") == "PASS" and receipt.get("errors") == [], "r45 receipt not PASS")
        require(receipt.get("deltas") == result, "r45 receipt delta replay mismatch")
        require(receipt.get("files") == [record(root / name) for name in sorted(PAYLOAD)], "r45 receipt output records drift")
        require(receipt.get("predecessor_dossier") == external["predecessor"], "r45 receipt predecessor evidence drift")
        require(receipt.get("semantic_source") == external["semantic"], "r45 receipt semantic evidence drift")
        require(receipt.get("source_repairs") == external["repairs"], "r45 receipt repair evidence drift")
        require(receipt.get("decision_audit") == external["d1002_audit"], "r45 receipt D1002 evidence drift")
        require(receipt.get("builds") == external["builds"], "r45 receipt build evidence drift")
        execution = receipt.get("execution", {})
        require(execution.get("contract") == "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion_with_rollback", "r45 execution contract drift")
        require(set(execution.get("attestation", {})) == {"driver", "bootstrap", "builder", "validator"}, "r45 execution attestation surface drift")
    return result


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R45_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if not raw:
        return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r45.py", "bytes": actual[0], "sha256": actual[1]}
    expected = json.loads(raw)
    require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator same-bytes attestation drift")
    return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r45.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not os.path.lexists(TARGET), f"No-overwrite r45 target already exists: {TARGET}")
        require(not os.path.lexists(STAGE), f"Unresolved r45 transaction exists: {STAGE}")
        external = verify_external()
        result = {
            "schema": "tohoku-r45-static-input-audit-v1",
            "status": "PASS",
            "errors": [],
            "attestation": attestation,
            "target_absent": True,
            "stage_absent": True,
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "predecessor_payload_aggregate_sha256": external["predecessor"]["payload_aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "d1002_audit": external["d1002_audit"],
            "scanner_delta": external["scanner"]["delta"],
            "builds": external["builds"],
            "projected_mapping_counts": EXPECTED_MAPPING_COUNTS,
            "launch_authorized": False,
        }
    else:
        result = {
            "schema": "tohoku-r45-stage-validation-v1",
            "attestation": attestation,
            **verify_stage(args.stage.resolve(), args.receipt),
        }
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
