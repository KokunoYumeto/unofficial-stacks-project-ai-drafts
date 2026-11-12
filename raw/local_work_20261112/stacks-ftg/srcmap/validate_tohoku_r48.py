#!/usr/bin/env python3
"""Independent bounded validator for the frozen no-overwrite Tohoku r48 successor."""

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
SOURCE = ROOT / "tohoku_r47"
TARGET = ROOT / "tohoku_r48"
STAGE = ROOT / ".tohoku-r48-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r17"
AUTHORITY = PROJECT / "authority_snapshot"
BASE_VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r47.py"
BASE_BUILDER = ROOT / "srcmap" / "build_tohoku_r47.py"
D1005_AUDIT = ROOT / "D1005_CHECK.json"
EXPECTED_BASE_VALIDATOR = (
    47238,
    "836531C980B81B81B98897ADAE1DDCC412399768F6221A8C5620A6485540D74D",
)
EXPECTED_BASE_BUILDER = (
    19702,
    "916D182598335A02B82CA417848273A26438719F2544B6A50936F3188269F82A",
)
EXPECTED_PYTHON = Path(r"user\miniconda3\python.exe")
EXPECTED_PYTHON_IDENTITY = (
    104264,
    "7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264",
)
EXPECTED_D1005_AUDIT = (
    6277,
    "43EAEFBBA7B6200A75BD36C38FB1496975BAF650A2E1F2CC4F37B7A9888A58DC",
)

EXPECTED_SOURCE = {
    "STATUS.md": (1329, "D88E3EE1320071EB612B5DDFE5B5DF58A8255DCE4B107AD7CA5906AD1633D72E"),
    "cfg.json": (5151, "28CE83C939C64B33635BEA3C37901E4F54EA0E6AF4F55F89A7E09C077A8C2D34"),
    "check.json": (77292, "B3D6421DAFDC38063AD8E521B0552014A723C23892D57819F969E428A1FA37C2"),
    "dec.csv": (366120, "EF353C15C1D27CADAD931198400E0F1AA93C261021D2B483B773D057B31A38CF"),
    "intake.json": (1578, "8279157B8AA7F6AA006E2C434C34D2A7988836D63C25B3465B93896D62E22801"),
    "issues.csv": (29535, "3439D68823BF69087F025976FB0AC41C2C4D93B8BFB4E63D6FD3267DB6AC178A"),
    "map.csv": (476350, "227699F3CEA49FE588327E9FB27FB847761C1E19209980A9E60A3B4F2372B46B"),
    "mcheck.json": (67120, "2A30549CFCDF5F4DFFC3F4B7C0EA86B37D51C3448000B8D77E10D321603A3146"),
    "r47-check.json": (35870, "2550B832E93B5C0EC0F5EB8EE22A7507BFEFDF610FE99979B1651039C7011535"),
    "stx.csv": (5274419, "6E09A558EE54BF0F1413FE7BD84234EFF3C4E3CA743AE6375AF0039C42063842"),
    "tcand.csv": (483157, "829E82C4A6FA6C2474A77BBF6AF2A6ECC6873B8735D06EB1C44ED64472578C47"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (392568, "3AB04435EEDD9DE59E61DF2443812C2F555DD6CA85542DC7F9C6BBE59DB03081"),
}
EXPECTED_SOURCE_PAYLOAD_SURFACE = (
    14,
    7179616,
    "A57F39A9ADA38460279E774AE155697546C639D061A18F8BC9F861DB756D81C9",
)
EXPECTED_SOURCE_SURFACE = (
    15,
    7215486,
    "5CBEFBEA79384CC4509FE5EA9A610AD42400F34CA6A8D978C1F6AFEB439D10F3",
)

INJECTIVES_ARTIFACTS = {
    "injectives.tex": (135243, "FE126B54B6B22511976AF99D61F561280A66FFFCD135F97634962C8C2F7576CE"),
    "injectives.aux": (10363, "A9EDF69C8722FA0F62928176E1FF0767C047D6D5EE5E1480B315031A71AA8CCE"),
    "injectives.log": (35033, "557F9408127E99ACDAB0711F6F19D48768526FE397CC6E5479DE924F48A5FD40"),
    "injectives.pdf": (641346, "B32C26C9A021FD5C454B87972802667576F33B49B32B50175631EF5D714409B1"),
}

PRIMARY_SOURCE_ARTIFACTS = {
    "p169.tex": (
        PROJECT / "build" / "v068c3r15" / "src" / "en" / "p169.tex",
        5133,
        "01E2B58B2EBC1CC3A1C494AB4D65EA1B41BAB89C6554CEA80B10988D29EAA423",
    ),
}
SOURCE_WITNESS_ARTIFACTS = {}

DECISION_ROWS = [
    {
        "decision_id": "D001013",
        "unit_id": "tohoku:construction:diagram-category-resolution",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "injectives-lemma-filtered-diagram-injective-resolutions",
        "rationale": "Stacks now proves the source's corrected diagram-category step for a small filtered partially ordered set I: the exact left adjoints F_i to evaluation yield the generator ⊕_i F_i(U) of A^I, so A^I is Grothendieck, and evaluation sends injectives to injectives. It does not repeat the false generator assertion for arbitrary diagram schemes.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000361",
    },
    {
        "decision_id": "D001014",
        "unit_id": "tohoku:construction:inductive-injective-resolutions",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "injectives-lemma-filtered-diagram-injective-resolutions",
        "rationale": "Stacks now proves the source's compatible-resolution construction: every covariant system M in A^I has a right resolution by injectives of A^I, and evaluation gives injective resolutions of all M_i whose transition maps lift the original system. It does not claim that objectwise injective diagrams or colimits of the resolution terms are injective.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000367",
    },
]

EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "decisions": 1014,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 361,
        "existing_stronger": 38,
        "existing_weaker": 7,
        "extend_existing": 22,
        "historical_reference": 33,
        "new_section": 6,
        "new_statement": 16,
        "structural_only": 424,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 29,
    "unit_candidates": 0,
    "units": 991,
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22057,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1264,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_SCAN_OUTPUTS = {
    "stx.csv": (5274693, "428203575DA7B351CBB16B8A2AC81A434A197F5E72D5BDD48CE8D7EDE627EEE2"),
    "tcand.csv": (483615, "6B806C8C03C0A9AFC2F9C6CBDBE01CCD35D2B34998CBE8BDA1DE6F0338AEF389"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
}
NEW_LABEL_ROW = {
    "tag": "",
    "full_label": "injectives-lemma-filtered-diagram-injective-resolutions",
    "file": "injectives.tex",
    "line": "2206",
    "kind": "lemma",
    "short_label": "lemma-filtered-diagram-injective-resolutions",
    "chapter": "Injectives",
    "section_label": "section-grothendieck-categories",
    "section_title": "Injectives in Grothendieck categories",
    "text_sha256": "2A99CA7E224719D14B55EE727D4056721FB6ACC534636F8B8F580942A329FE4C",
}
PREDECESSOR_LABEL_ROW = {
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

EXECUTION_ROLES = {
    "driver": ("srcmap/start_build_tohoku_r48.ps1", "self_read_hash_then_one_shot_bootstrap_envelope"),
    "bootstrap": ("srcmap/start_build_tohoku_r48.py", "one_read_hash_compile_exec_builder_and_pin_validator"),
    "builder": ("srcmap/build_tohoku_r48.py", "read_hash_compile_and_exec_same_payload"),
    "validator": ("srcmap/validate_tohoku_r48.py", "independent_same_bytes_stage_and_receipt_replay"),
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
    module = load_module(BASE_VALIDATOR, "tohoku_r48_pinned_r47_validator")
    require_identity(BASE_VALIDATOR, EXPECTED_BASE_VALIDATOR)
    return module


BASE = load_base_validator()
EXPECTED_SEM = dict(BASE.EXPECTED_SEM)
EXPECTED_SEM_SURFACE = BASE.EXPECTED_SEM_SURFACE
EXPECTED_SEM_PAYLOAD_SURFACE = BASE.EXPECTED_SEM_PAYLOAD_SURFACE


def expected_runtime() -> dict[str, tuple[int, str]]:
    return {
        **BASE.expected_runtime(),
        "srcmap/validate_tohoku_r47.py": EXPECTED_BASE_VALIDATOR,
        "srcmap/build_tohoku_r47.py": EXPECTED_BASE_BUILDER,
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
    return load_module(ROOT / "fga" / "mkidx.py", "tohoku_r48_pinned_mkidx")


def verify_semantic() -> dict[str, object]:
    return BASE.verify_semantic()


def verify_repairs() -> dict[str, object]:
    return BASE.verify_repairs()


def verify_d1005_audit() -> dict[str, object]:
    require_identity(D1005_AUDIT, EXPECTED_D1005_AUDIT)
    audit = strict_json(D1005_AUDIT)
    require(audit.get("schema") == "tohoku-stacks-d1005-audit-v1", "D1005 audit schema drift")
    require(audit.get("status") == "STRICT_PASS" and audit.get("errors") == [], "D1005 audit not STRICT_PASS")
    require(audit.get("formalization_id") == "D1005", "D1005 formalization ID drift")
    require(audit.get("primary_unit") == "tohoku:construction:diagram-category-resolution", "D1005 primary-unit drift")
    require(
        set(audit.get("related_units", []))
        == {
            "tohoku:construction:inductive-injective-resolutions",
            "tohoku:eq:diagram-injective-resolution",
            "tohoku:eq:component-injective-complex",
        },
        "D1005 related-unit surface drift",
    )
    require(
        audit.get("stacks_label") == "injectives-lemma-filtered-diagram-injective-resolutions"
        and {row["stacks_labels"] for row in DECISION_ROWS} == {audit.get("stacks_label")},
        "D1005 label drift",
    )
    require(
        audit.get("mapping_authority_sha256")
        == "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF",
        "D1005 mapping-authority drift",
    )
    expected_primary = []
    for _, (path, size, sha256) in PRIMARY_SOURCE_ARTIFACTS.items():
        require_identity(path, (size, sha256))
        expected_primary.append({"path": str(path), "bytes": size, "sha256": sha256})
    require(audit.get("primary_source_files") == expected_primary, "D1005 primary-source binding drift")
    require(SOURCE_WITNESS_ARTIFACTS == {} and "source_witness_files" not in audit, "D1005 witness-source surface drift")
    require(
        audit.get("source_reference")
        == "Tohoku, Chapter III, Section 3.6, proof of Proposition 3.6.2, p. 169",
        "D1005 source-reference drift",
    )
    expected_artifacts = {
        "tex": {
            "path": str(ROOT / "injectives.tex"),
            "bytes": INJECTIVES_ARTIFACTS["injectives.tex"][0],
            "sha256": INJECTIVES_ARTIFACTS["injectives.tex"][1],
            "new_block_lines": [2205, 2321],
        },
        "aux": {"path": str(ROOT / "injectives.aux"), "bytes": INJECTIVES_ARTIFACTS["injectives.aux"][0], "sha256": INJECTIVES_ARTIFACTS["injectives.aux"][1]},
        "log": {"path": str(ROOT / "injectives.log"), "bytes": INJECTIVES_ARTIFACTS["injectives.log"][0], "sha256": INJECTIVES_ARTIFACTS["injectives.log"][1]},
    }
    for key, expected in expected_artifacts.items():
        require(audit.get("artifacts", {}).get(key) == expected, f"D1005 audit {key} binding drift")
    pdf = audit.get("artifacts", {}).get("pdf", {})
    require(
        (pdf.get("path"), pdf.get("bytes"), pdf.get("sha256"), pdf.get("pages"), pdf.get("media_box"), pdf.get("rotation"), pdf.get("encrypted"))
        == (str(ROOT / "injectives.pdf"), INJECTIVES_ARTIFACTS["injectives.pdf"][0], INJECTIVES_ARTIFACTS["injectives.pdf"][1], 39, [0, 0, 612, 792], 0, False),
        "D1005 audit PDF binding drift",
    )
    require(
        audit.get("aux_label")
        == r"\newlabel{lemma-filtered-diagram-injective-resolutions}{{12.8}{23}{Compatible injective resolutions of filtered systems}{subsection.12.8}{}}",
        "D1005 audit AUX label drift",
    )
    for section in ("source_audit", "math_audit", "build_audit", "pdf_audit"):
        require(audit.get(section, {}).get("status") == "STRICT_PASS", f"D1005 {section} drift")
    require(audit.get("pdf_audit", {}).get("visual_pages") == [22, 23, 24, 25, 26], "D1005 visual-page audit drift")
    require(len(audit.get("pdf_audit", {}).get("render_records", [])) == 5, "D1005 render-record count drift")
    require(
        "This receipt does not update the Tohoku mapping ledger; mapping promotion belongs to the next no-overwrite successor."
        in audit.get("nonclaims", []),
        "D1005 mapping nonclaim drift",
    )
    return {"receipt": record(D1005_AUDIT, "D1005_CHECK.json"), "status": "STRICT_PASS", "errors": []}


def verify_builds() -> dict[str, object]:
    artifacts = expected_artifacts()
    for name, expected in artifacts.items():
        require_identity(ROOT / name, expected)
    r42 = BASE.BASE.BASE.BASE.BASE.load_legacy_validator()
    specs = {
        **r42.BUILD_SPECS,
        "cohomology": {"pages": 222, "visual": [27, 28, 29, 30, 31, 32]},
        "injectives": {"pages": 39, "visual": [22, 23, 24, 25, 26]},
    }
    aux_lines = {**r42.EXPECTED_AUX_LINES}
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
        r"\newlabel{theorem-injective-embedding-grothendieck}{{12.7}{22}{}{subsection.12.7}{}}",
        r"\newlabel{lemma-filtered-diagram-injective-resolutions}{{12.8}{23}{Compatible injective resolutions of filtered systems}{subsection.12.8}{}}",
        r"\newlabel{section-K-injective}{{13}{24}{K-injectives in Grothendieck categories}{section.13}{}}",
        r"\newlabel{lemma-surjection-bounded-size}{{13.1}{24}{}{subsection.13.1}{}}",
        r"\newlabel{lemma-characterize-K-injective}{{13.3}{25}{}{subsection.13.3}{}}",
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
                not any(start <= 2321 and end >= 2205 for start, end in box_ranges),
                "D1005 source block has an overfull box",
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
    require(tex.count(r"\label{lemma-filtered-diagram-injective-resolutions}") == 1, "D1005 source label multiplicity drift")
    for evidence in (
        "The printed proof invokes Proposition 1.9.2",
        "the generator assertion",
        "For the small filtered poset used here",
        r"$F_i$ to evaluation give the generator $\bigoplus_i F_i(U)$",
        r"\label{lemma-filtered-diagram-injective-resolutions}",
        r"F_i(B)_j =",
        r"$F_i \dashv \operatorname{ev}_i$",
        r"\ref{homology-lemma-adjoint-preserve-injectives}",
        "by injective objects of $\\mathcal{A}^I$",
        "its transition morphisms form the asserted morphisms of",
    ):
        require(evidence in tex, f"D1005 source proof/nonclaim drift: {evidence}")
    inherited = strict_json(SOURCE / "r47-check.json").get("builds", {}).get("independent_audits", {})
    require(
        set(inherited)
        == {f"D{number:06d}" for number in range(996, 1013)},
        "r47 independent-audit inheritance drift",
    )
    builds["independent_audits"] = {
        **inherited,
        "D001013": {
            "status": "STRICT_PASS",
            "receipt": record(D1005_AUDIT, "D1005_CHECK.json"),
            "scope": [
                "small filtered covariant diagram category",
                "exact left adjoints to evaluation and generator coproduct",
                "evaluation preserves injectives",
            ],
        },
        "D001014": {
            "status": "STRICT_PASS",
            "receipt": record(D1005_AUDIT, "D1005_CHECK.json"),
            "scope": [
                "right resolution by injective objects in the diagram category",
                "compatible evaluated injective resolutions",
                "39-page strict parse and pages 22-26 clean",
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
    require(set(new_by) - set(old_by) == {NEW_LABEL_ROW["full_label"]}, "D1005 new-label set drift")
    require(new_by[NEW_LABEL_ROW["full_label"]] == NEW_LABEL_ROW, "D1005 new-label row drift")
    require(new_by[PREDECESSOR_LABEL_ROW["full_label"]] == PREDECESSOR_LABEL_ROW, "Inherited D1004-label row drift")
    require(new_by[OBSTRUCTION_LABEL_ROW["full_label"]] == OBSTRUCTION_LABEL_ROW, "Inherited obstruction-label row drift")
    changed = []
    for label in old_by:
        if old_by[label] != new_by[label]:
            require(
                all(old_by[label][field] == new_by[label][field] for field in fields if field != "line"),
                f"Existing label substantive metadata drift: {label}",
            )
            require(
                int(new_by[label]["line"]) - int(old_by[label]["line"]) == 119,
                f"Existing label line-shift drift: {label}",
            )
            changed.append(label)
    require(Counter(old_by[label]["file"] for label in changed) == Counter({"injectives.tex": 30}), "Existing label line-only oracle drift")

    _, old_candidates = load_csv(SOURCE / "tcand.csv")
    old_c = {(row["topic_id"], row["full_label"]): row for row in old_candidates}
    new_c = {(row["topic_id"], row["full_label"]): row for row in candidates}
    expected_added_candidates = {
        ("grothendieck-category", NEW_LABEL_ROW["full_label"]),
        ("injectives", NEW_LABEL_ROW["full_label"]),
    }
    expected_removed_candidates = {
        ("grothendieck-category", "local-cohomology-proposition-uniform-artin-rees"),
    }
    require(set(new_c) - set(old_c) == expected_added_candidates, "Candidate-key addition drift")
    require(set(old_c) - set(new_c) == expected_removed_candidates, "Candidate-key removal drift")
    require(new_c[("injectives", NEW_LABEL_ROW["full_label"])]["score"] == "21", "Injectives candidate score drift")
    require(new_c[("injectives", NEW_LABEL_ROW["full_label"])]["hit_fields"] == "text", "Injectives candidate evidence drift")
    require(new_c[("grothendieck-category", NEW_LABEL_ROW["full_label"])]["score"] == "92", "Grothendieck candidate score drift")
    require(new_c[("grothendieck-category", NEW_LABEL_ROW["full_label"])]["hit_fields"] == "section;text", "Grothendieck candidate evidence drift")
    changed_candidates = []
    for key in set(old_c) & set(new_c):
        if old_c[key] != new_c[key]:
            require(
                all(old_c[key][field] == new_c[key][field] for field in old_c[key] if field != "line"),
                f"Existing candidate substantive metadata drift: {key}",
            )
            require(
                int(new_c[key]["line"]) - int(old_c[key]["line"]) == 119,
                f"Existing candidate line-shift drift: {key}",
            )
            changed_candidates.append(key)
    require(Counter(old_c[key]["file"] for key in changed_candidates) == Counter({"injectives.tex": 29}), "Candidate line-only oracle drift")
    require(len(index) == 22057 and len(candidates) == 1264 and len(topic_map) == 13, "Scanner count oracle drift")
    require(sum(1 for row in index if row["tag"]) == 21437, "Official-tag join count drift")
    require(len(warnings) == 629, "Scanner warning count drift")
    require(
        "TeX label has no official tag in this snapshot: injectives-lemma-filtered-diagram-injective-resolutions"
        in warnings,
        "D1005 no-official-tag warning drift",
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
            "existing_rows_line_number_only": 30,
            "existing_text_hash_changes": 0,
            "existing_other_metadata_changes": 0,
            "official_tag_changes": 0,
            "candidate_count_delta": 1,
            "candidate_keys_added": 2,
            "candidate_keys_removed": 1,
            "candidate_keys_added_values": [list(key) for key in sorted(expected_added_candidates)],
            "candidate_keys_removed_values": [list(key) for key in sorted(expected_removed_candidates)],
            "existing_candidate_rows_line_number_only": 29,
        },
    }


def verify_external() -> dict[str, object]:
    require_plain_directory(SOURCE)
    entries = list(SOURCE.iterdir())
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SOURCE), "r47 predecessor surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected r47 predecessor subdirectory")
    records = []
    for name, expected in sorted(EXPECTED_SOURCE.items()):
        require_identity(SOURCE / name, expected)
        records.append(record(SOURCE / name))
    require(
        (len(records), sum(int(item["bytes"]) for item in records), aggregate(records)) == EXPECTED_SOURCE_SURFACE,
        "r47 predecessor aggregate drift",
    )
    payload_records = [item for item in records if item["name"] != "r47-check.json"]
    require(
        (len(payload_records), sum(int(item["bytes"]) for item in payload_records), aggregate(payload_records)) == EXPECTED_SOURCE_PAYLOAD_SURFACE,
        "r47 predecessor payload aggregate drift",
    )
    predecessor = strict_json(SOURCE / "r47-check.json")
    require(predecessor.get("schema") == "tohoku-stacks-mapping-successor-r47-v1", "r47 predecessor receipt schema drift")
    require(predecessor.get("status") == "PASS" and predecessor.get("errors") == [], "r47 predecessor receipt not PASS")
    require(predecessor.get("deltas", {}).get("decisions") == 1012, "r47 predecessor decision gate drift")
    require(predecessor.get("deltas", {}).get("mapping_counts", {}).get("dispositions", {}).get("existing_weaker") == 9, "r47 D1005 predecessor gap gate drift")
    require(predecessor.get("deltas", {}).get("remaining_gap_class_dispositions") == 53, "r47 predecessor gap-count drift")
    for name, expected in expected_runtime().items():
        require_identity(ROOT / name, expected)
    for name, expected in BASE.BASE.BASE.BASE.BASE.load_legacy_validator().EXPECTED_AUTHORITY.items():
        require_identity(AUTHORITY / name, expected)
    require(Path(sys.executable).resolve() == EXPECTED_PYTHON.resolve(), "Python executable path drift")
    require_identity(EXPECTED_PYTHON, EXPECTED_PYTHON_IDENTITY)
    require(sys.version_info[:3] == (3, 13, 9) and sys.implementation.cache_tag == "cpython-313", "Python runtime drift")
    semantic = verify_semantic()
    repairs = verify_repairs()
    d1005 = verify_d1005_audit()
    builds = verify_builds()
    scanner = verify_scanner_oracle()
    return {
        "predecessor": {
            "name": "tohoku_r47",
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
        "d1005_audit": d1005,
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
    expected_names = PAYLOAD | ({"r48-check.json"} if receipt_mode else set())
    require({path.name for path in entries if path.is_file()} == expected_names, "Stage/target file surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected stage/target subdirectory")

    cfg = strict_json(root / "cfg.json")
    require(cfg.get("dossier_id") == "tohoku_r48", "r48 cfg dossier ID drift")
    require(cfg.get("expected_units") == 991, "r48 cfg unit count drift")
    require(cfg.get("semantic_successor", {}).get("generation") == "sem/r17", "r48 cfg semantic generation drift")
    require(cfg.get("semantic_successor", {}).get("surface_files") == 18, "r48 cfg semantic file count drift")
    require(cfg.get("semantic_successor", {}).get("surface_bytes") == EXPECTED_SEM_SURFACE[1], "r48 cfg semantic bytes drift")
    require(cfg.get("semantic_successor", {}).get("surface_sha256") == EXPECTED_SEM_SURFACE[2], "r48 cfg semantic aggregate drift")
    primary = cfg.get("inputs", {}).get("primary", {})
    require(primary.get("source_file") == "sem/r17/nodes.csv", "r48 cfg primary source drift")
    require(primary.get("sha256") == EXPECTED_SEM["nodes.csv"][1], "r48 cfg node pin drift")
    require(cfg.get("inputs", {}).get("sem_manifest", {}).get("sha256") == EXPECTED_SEM["manifest.json"][1], "r48 cfg manifest pin drift")
    require(cfg.get("inputs", {}).get("sem_validation", {}).get("sha256") == EXPECTED_SEM["validation.json"][1], "r48 cfg validation pin drift")

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
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r48 scan counts drift")
    require(check.get("warnings") == scanner["warnings"], "r48 scan warnings drift")
    require(check.get("tex_sha256") == scanner["tex_hashes"], "r48 scan TeX hashes drift")
    runtime = expected_runtime()
    require(check.get("sha256", {}).get("tags/tags") == runtime["tags/tags"][1], "r48 scan tag hash drift")

    unit_fields, units = load_csv(root / "units.csv")
    projected_units = expected_units(cfg)
    require(unit_fields == BASE.BASE.BASE.BASE.BASE.load_intake().FIELDS, "r48 unit schema drift")
    require(units == projected_units, "r48 units differ from exact sem/r17 intake projection")
    require(intake.get("counts", {}).get("units") == 991, "r48 intake unit receipt drift")

    fields, old_decisions = load_csv(SOURCE / "dec.csv")
    new_fields, decisions = load_csv(root / "dec.csv")
    require(fields == new_fields, "Decision schema drift")
    require([row["decision_id"] for row in decisions] == [f"D{number:06d}" for number in range(1, 1015)], "Decision sequence drift")
    require(decisions[:1012] == old_decisions and decisions[1012:] == DECISION_ROWS, "Decision prefix/appended rows drift")
    require((root / "dec.csv").read_bytes().startswith((SOURCE / "dec.csv").read_bytes()), "Decision byte prefix drift")
    anchors = {
        "D000361": (DECISION_ROWS[0], "existing_weaker"),
        "D000367": (DECISION_ROWS[1], "existing_weaker"),
    }
    old_by_id = {row["decision_id"]: row for row in old_decisions}
    for decision_id, (successor, expected_disposition) in anchors.items():
        anchor = old_by_id.get(decision_id, {})
        require(anchor.get("unit_id") == successor["unit_id"], f"{decision_id} supersession unit drift")
        require(anchor.get("disposition") == expected_disposition, f"{decision_id} predecessor disposition drift")

    _, issues = load_csv(root / "issues.csv")
    require(len(issues) == 29 and all(row["status"] == "resolved" for row in issues), "r48 issue ledger drift")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r48 mapping counts drift")
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
    require(map_fields == expected_fields, "r48 map schema drift")
    projected_map = expected_map(cfg, projected_units, scanner, root / "dec.csv")
    require(mapped == projected_map, "r48 map differs from independent sem/r17 + live scanner + ledger replay")
    _, old_map = load_csv(SOURCE / "map.csv")
    old_by = {row["unit_id"]: row for row in old_map}
    new_by = {row["unit_id"]: row for row in mapped}
    target_units = {row["unit_id"] for row in DECISION_ROWS}
    require(set(old_by) == set(new_by) and len(new_by) == 991, "Map stable-unit set drift")
    for unit_id in set(new_by) - target_units:
        require(new_by[unit_id] == old_by[unit_id], f"Unauthorized r48 map mutation: {unit_id}")
    authorized_fields_by_decision = {
        "D001013": {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
        "D001014": {"decision_id", "disposition", "review_state", "stacks_labels", "stacks_tags", "rationale"},
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
        ("D001009", "tohoku:remark:3.4.2:3:p1"),
        ("D001010", "tohoku:def:adjoint-obstruction-class"),
        ("D001011", "tohoku:construction:constant-transition-reduction:p1"),
        ("D001012", "tohoku:remark:3.4.2:3:p2"),
    ):
        require(new_by[unit_id]["decision_id"] == decision_id, f"{decision_id} no longer selected")
    for unit_id in (
        "tohoku:eq:diagram-injective-resolution",
        "tohoku:eq:component-injective-complex",
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
    require(new_by["tohoku:proposition:3.6.2"] == old_by["tohoku:proposition:3.6.2"], "Proposition 3.6.2 row drift")
    require(new_by["tohoku:proposition:3.6.2"]["decision_id"] == "D000425", "Proposition 3.6.2 decision drift")

    gap_count = sum(EXPECTED_MAPPING_COUNTS["dispositions"][name] for name in ("existing_weaker", "extend_existing", "new_statement", "new_section"))
    require(gap_count == 51, "Gap-class arithmetic drift")
    status = (root / "STATUS.md").read_text(encoding="utf-8")
    for token in (
        "sem/r17", "D001013", "D001014", "D000361", "D000367",
        "51 gap-class", "diagram-injective-resolution", "component-injective-complex",
    ):
        require(token in status, f"STATUS missing token: {token}")

    result = {
        "status": "PASS",
        "errors": [],
        "stable_units": 991,
        "decisions": 1014,
        "decisions_appended": DECISION_ROWS,
        "active_source_issues": [],
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": EXPECTED_SCAN_COUNTS,
        "scanner_delta": scanner["delta"],
        "remaining_gap_class_dispositions": 51,
        "semantic_generation": "sem/r17",
        "authorized_map_mutations": {
            "units": sorted(target_units),
            "fields_by_decision": {
                decision_id: sorted(fields)
                for decision_id, fields in sorted(authorized_fields_by_decision.items())
            },
            "unchanged_units": 989,
        },
        "byte_identical_payloads": ["intake.json", "issues.csv", "tmap.csv", "topics.csv", "ucand.csv", "units.csv"],
        "external_evidence": {
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "repair_aggregate_sha256": external["repairs"]["aggregate_sha256"],
            "d1005_audit_sha256": external["d1005_audit"]["receipt"]["sha256"],
        },
    }

    if receipt_mode:
        receipt = strict_json(root / "r48-check.json")
        require(receipt.get("schema") == "tohoku-stacks-mapping-successor-r48-v1", "r48 receipt schema drift")
        require(receipt.get("status") == "PASS" and receipt.get("errors") == [], "r48 receipt not PASS")
        require(receipt.get("deltas") == result, "r48 receipt delta replay mismatch")
        require(receipt.get("files") == [record(root / name) for name in sorted(PAYLOAD)], "r48 receipt output records drift")
        require(receipt.get("predecessor_dossier") == external["predecessor"], "r48 receipt predecessor evidence drift")
        require(receipt.get("semantic_source") == external["semantic"], "r48 receipt semantic evidence drift")
        require(receipt.get("source_repairs") == external["repairs"], "r48 receipt repair evidence drift")
        require(receipt.get("decision_audit") == external["d1005_audit"], "r48 receipt D1005 evidence drift")
        require(receipt.get("builds") == external["builds"], "r48 receipt build evidence drift")
        execution = receipt.get("execution", {})
        require(execution.get("contract") == "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion_with_rollback", "r48 execution contract drift")
        require(execution.get("attestation") == expected_execution_attestation(), "r48 execution attestation replay drift")
    return result


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R48_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if not raw:
        return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r48.py", "bytes": actual[0], "sha256": actual[1]}
    expected = json.loads(raw)
    require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator same-bytes attestation drift")
    return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r48.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not os.path.lexists(TARGET), f"No-overwrite r48 target already exists: {TARGET}")
        require(not os.path.lexists(STAGE), f"Unresolved r48 transaction exists: {STAGE}")
        external = verify_external()
        result = {
            "schema": "tohoku-r48-static-input-audit-v1",
            "status": "PASS",
            "errors": [],
            "attestation": attestation,
            "target_absent": True,
            "stage_absent": True,
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "predecessor_payload_aggregate_sha256": external["predecessor"]["payload_aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "d1005_audit": external["d1005_audit"],
            "scanner_delta": external["scanner"]["delta"],
            "builds": external["builds"],
            "projected_mapping_counts": EXPECTED_MAPPING_COUNTS,
            "launch_authorized": False,
        }
    else:
        result = {
            "schema": "tohoku-r48-stage-validation-v1",
            "attestation": attestation,
            **verify_stage(args.stage.resolve(), args.receipt),
        }
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
