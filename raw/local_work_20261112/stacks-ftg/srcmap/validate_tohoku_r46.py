#!/usr/bin/env python3
"""Independent bounded validator for the frozen no-overwrite Tohoku r46 successor."""

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
SOURCE = ROOT / "tohoku_r45"
TARGET = ROOT / "tohoku_r46"
STAGE = ROOT / ".tohoku-r46-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r17"
AUTHORITY = PROJECT / "authority_snapshot"
BASE_VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r45.py"
BASE_BUILDER = ROOT / "srcmap" / "build_tohoku_r45.py"
D1003_AUDIT = ROOT / "D1003_CHECK.json"
EXPECTED_BASE_VALIDATOR = (
    41034,
    "709540E812E866B44C508ACC275EE6A3C50C37F6116C606869FC1912C7689979",
)
EXPECTED_BASE_BUILDER = (
    18877,
    "5051BFB52199963C0DF2B62A604B7F4E908D493E76938746377E99E192F10A32",
)
EXPECTED_PYTHON = Path(r"user\miniconda3\python.exe")
EXPECTED_PYTHON_IDENTITY = (
    104264,
    "7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264",
)
EXPECTED_D1003_AUDIT = (
    6323,
    "20CEE7D9D4AFAB7D2CFCF613A4D708A9AC9750975C4C65946E9BD9F873F5C65E",
)

EXPECTED_SOURCE = {
    "STATUS.md": (1213, "A151FFF3729989BA06F73724370ADD52F4A5B91E3FDD25EB1C776575ECC5FC9E"),
    "cfg.json": (5151, "1C178FE5D22DBF6045685C0DBCCADAC9AA2C5D93B2EA98810CA1CBDCD88E0351"),
    "check.json": (77062, "435E33E233940C5A84A812DEE2A1463F2BFBF3F84295FB10FE5587C3EB72AD89"),
    "dec.csv": (362235, "9FFF3C343C9045E0383EE56B483C157DF1B4C72159D26BEEB868DE8DE0A9F34B"),
    "intake.json": (1578, "8279157B8AA7F6AA006E2C434C34D2A7988836D63C25B3465B93896D62E22801"),
    "issues.csv": (29535, "3439D68823BF69087F025976FB0AC41C2C4D93B8BFB4E63D6FD3267DB6AC178A"),
    "map.csv": (474483, "E974D868D90DC4BA9AEE0847BB3B2B70FD6D280E66981E6CA8E00F88F138DF5C"),
    "mcheck.json": (66890, "C11202E97143886829AF9B26C20D0008E62348B25290A0319F6D441F48F1D26E"),
    "r45-check.json": (29930, "472CBF29A4D7CE052AC6257B0A5F386A28621D9884C1AF9796D8EF045F9945A5"),
    "stx.csv": (5273896, "535EB0E5493A5036A802FE2B96593BBF57160E5A5FAE8B3AEC74AEDE55DFCC07"),
    "tcand.csv": (483154, "349BB31F8C40E297EF0D2C3C6B8026CE202240A622F86C22FC5C6FE48D33C1F5"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (392568, "3AB04435EEDD9DE59E61DF2443812C2F555DD6CA85542DC7F9C6BBE59DB03081"),
}
EXPECTED_SOURCE_PAYLOAD_SURFACE = (
    14,
    7172762,
    "5A040DDBD107A13022C2AE885687514AD8F59F452537F472BEEC5EFAD933EC8A",
)
EXPECTED_SOURCE_SURFACE = (
    15,
    7202692,
    "A8AC45885C30AB8A9673924931AC7272F09C1DB20E037744D47B927FE240BCD1",
)

COHOMOLOGY_ARTIFACTS = {
    "cohomology.tex": (842749, "67B460C8F90FAA369F99FEEDB4ADD812E3E345B2E1EED0F2247AEEBFFEDF2725"),
    "cohomology.aux": (52358, "18F88EF7A4E4ACB8AF1A0C8906E37E93D8F3078FA8E2D1EA04F010B25B5C8BE8"),
    "cohomology.log": (47595, "0E0A897203DA0DA02FFAE9436BCC46034FAF970C6D1EF41B18E41AE88FEE6D45"),
    "cohomology.pdf": (1870731, "CFE066E9B2A72C0C47526CCFFCFC8A7D635AF9F1C167170E03E5154DD8824FD8"),
}

PRIMARY_SOURCE_ARTIFACTS = {
    "p164.tex": (
        PROJECT / "build" / "v068c3r15" / "src" / "en" / "p164.tex",
        3972,
        "746800D45CF279AD8F8AFA89D7BDE0CDC528C0EB80888FDF0FD0483D44D08D0A",
    ),
    "p165.tex": (
        PROJECT / "build" / "v068c3r15" / "src" / "en" / "p165.tex",
        3955,
        "8428BDCCCFAD48BA788782899AC60C8A3FC9BE0509C622BFA5E6E09ACEEA8CF7",
    ),
}

DECISION_ROWS = [
    {
        "decision_id": "D001005",
        "unit_id": "tohoku:prop:3.4.2:p2",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-pointwise-envelope-degree-two-boundary",
        "rationale": "Stacks now constructs the source's functorial twisted degree-two obstruction from a P-lift Q, proves independence of the lift, identifies the twisted middle term with Π(F^E) rather than using the false locality of flasqueness, and proves that the class vanishes exactly when E is induced from a G-torsor.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000308",
    },
    {
        "decision_id": "D001006",
        "unit_id": "tohoku:cor:3.4.2",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-pointwise-envelope-degree-two-boundary",
        "rationale": "In the central case the H-action on F is trivial, so Stacks' construction gives the source's functorial pointed map H^1(X,H)→H^2(X,F), whose zero fibre is exactly the image of G-torsor classes; in the abelian case it is the usual connecting homomorphism.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000262",
    },
    {
        "decision_id": "D001007",
        "unit_id": "tohoku:remark:3.4.2:1:p1",
        "action": "replace",
        "disposition": "example_or_remark",
        "stacks_labels": "cohomology-lemma-pointwise-envelope-degree-two-boundary",
        "rationale": "Stacks now explains the source's sign sentence exactly: its left-torsor convention makes the class +δ(d_u(Q)), while Tohoku records inverse transition functions and therefore prints ∂(E)=-d(Q); these are the same obstruction, not conflicting signs.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000311",
    },
    {
        "decision_id": "D001008",
        "unit_id": "tohoku:remark:3.4.2:1:p2",
        "action": "replace",
        "disposition": "example_or_remark",
        "stacks_labels": "cohomology-lemma-pointwise-envelope-degree-two-boundary",
        "rationale": "Stacks now proves the source's abelian 3×3 comparison: the connecting square is anticommutative, but the inverse cocycle representing [E] cancels that minus, so +δ(d_u(Q)) is the standard boundary under Stacks conventions and corresponds to Tohoku's printed minus.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000312",
    },
]

EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "decisions": 1008,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 357,
        "existing_stronger": 38,
        "existing_weaker": 9,
        "extend_existing": 22,
        "historical_reference": 33,
        "new_section": 6,
        "new_statement": 17,
        "structural_only": 425,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 29,
    "unit_candidates": 0,
    "units": 991,
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22055,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1263,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_SCAN_OUTPUTS = {
    "stx.csv": (5274150, "F33C011D720587F9B087A654C65BF96C6070E5161DFD5777D18E33B8EE852CD4"),
    "tcand.csv": (483156, "C01B405B2703508E829E9DE7C257CDF35B23C08FFF32EB1B8E28B93512DE16CA"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
}
NEW_LABEL_ROW = {
    "tag": "",
    "full_label": "cohomology-lemma-pointwise-envelope-degree-two-boundary",
    "file": "cohomology.tex",
    "line": "2615",
    "kind": "lemma",
    "short_label": "lemma-pointwise-envelope-degree-two-boundary",
    "chapter": "Cohomology of Sheaves",
    "section_label": "section-flasque",
    "section_title": "Flasque sheaves",
    "text_sha256": "C66CA97D52849BB6E15FD4D3A3D59FC8B515030CB7178728686A044A3C77A436",
}
TORSOR_LABEL_ROW = {
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
    module = load_module(BASE_VALIDATOR, "tohoku_r46_pinned_r45_validator")
    require_identity(BASE_VALIDATOR, EXPECTED_BASE_VALIDATOR)
    return module


BASE = load_base_validator()
EXPECTED_SEM = dict(BASE.EXPECTED_SEM)
EXPECTED_SEM_SURFACE = BASE.EXPECTED_SEM_SURFACE
EXPECTED_SEM_PAYLOAD_SURFACE = BASE.EXPECTED_SEM_PAYLOAD_SURFACE


def expected_runtime() -> dict[str, tuple[int, str]]:
    return {
        **BASE.expected_runtime(),
        "srcmap/validate_tohoku_r45.py": EXPECTED_BASE_VALIDATOR,
        "srcmap/build_tohoku_r45.py": EXPECTED_BASE_BUILDER,
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
    return load_module(ROOT / "fga" / "mkidx.py", "tohoku_r46_pinned_mkidx")


def verify_semantic() -> dict[str, object]:
    return BASE.verify_semantic()


def verify_repairs() -> dict[str, object]:
    return BASE.verify_repairs()


def verify_d1003_audit() -> dict[str, object]:
    require_identity(D1003_AUDIT, EXPECTED_D1003_AUDIT)
    audit = strict_json(D1003_AUDIT)
    require(audit.get("schema") == "tohoku-stacks-d1003-audit-v1", "D1003 audit schema drift")
    require(audit.get("status") == "STRICT_PASS" and audit.get("errors") == [], "D1003 audit not STRICT_PASS")
    require(audit.get("formalization_id") == "D1003", "D1003 formalization ID drift")
    require(audit.get("primary_unit") == DECISION_ROWS[0]["unit_id"], "D1003 primary-unit drift")
    require(
        set(audit.get("related_units", []))
        == {
            "tohoku:eq:3.4.2:obstruction-cohomology",
            "tohoku:eq:3.4.2:twisted-flabby-sequence",
            "tohoku:eq:3.4.2:boundary-as-minus-dQ",
            "tohoku:diagram:3.4.2:boundary-anticommutative-square",
            "tohoku:eq:3.4.2:dQ-minus-boundary-cE",
            "tohoku:cor:3.4.2",
        },
        "D1003 related-unit surface drift",
    )
    require(audit.get("stacks_label") == DECISION_ROWS[0]["stacks_labels"], "D1003 label drift")
    expected_primary = []
    for name, (path, size, sha256) in PRIMARY_SOURCE_ARTIFACTS.items():
        require_identity(path, (size, sha256))
        expected_primary.append({"path": str(path), "bytes": size, "sha256": sha256})
    require(audit.get("primary_source_files") == expected_primary, "D1003 primary-source binding drift")
    expected_artifacts = {
        "tex": {
            "path": str(ROOT / "cohomology.tex"),
            "bytes": COHOMOLOGY_ARTIFACTS["cohomology.tex"][0],
            "sha256": COHOMOLOGY_ARTIFACTS["cohomology.tex"][1],
            "new_block_lines": [2614, 2821],
        },
        "aux": {"path": str(ROOT / "cohomology.aux"), "bytes": COHOMOLOGY_ARTIFACTS["cohomology.aux"][0], "sha256": COHOMOLOGY_ARTIFACTS["cohomology.aux"][1]},
        "log": {"path": str(ROOT / "cohomology.log"), "bytes": COHOMOLOGY_ARTIFACTS["cohomology.log"][0], "sha256": COHOMOLOGY_ARTIFACTS["cohomology.log"][1]},
    }
    for key, expected in expected_artifacts.items():
        require(audit.get("artifacts", {}).get(key) == expected, f"D1003 audit {key} binding drift")
    pdf = audit.get("artifacts", {}).get("pdf", {})
    require(
        (pdf.get("path"), pdf.get("bytes"), pdf.get("sha256"), pdf.get("pages"), pdf.get("media_box"), pdf.get("rotation"), pdf.get("encrypted"))
        == (str(ROOT / "cohomology.pdf"), COHOMOLOGY_ARTIFACTS["cohomology.pdf"][0], COHOMOLOGY_ARTIFACTS["cohomology.pdf"][1], 221, [0, 0, 612, 792], 0, False),
        "D1003 audit PDF binding drift",
    )
    require(
        audit.get("aux_label")
        == r"\newlabel{lemma-pointwise-envelope-degree-two-boundary}{{12.8}{26}{The degree-two boundary of a pointwise envelope}{subsection.12.8}{}}",
        "D1003 audit AUX label drift",
    )
    require(audit.get("math_audit", {}).get("status") == "STRICT_PASS", "D1003 math audit drift")
    require(audit.get("build_audit", {}).get("status") == "STRICT_PASS", "D1003 build audit drift")
    require(audit.get("pdf_audit", {}).get("status") == "STRICT_PASS", "D1003 PDF audit drift")
    require(audit.get("pdf_audit", {}).get("visual_pages") == [25, 26, 27, 28, 29, 30, 31], "D1003 visual-page audit drift")
    require(len(audit.get("pdf_audit", {}).get("render_records", [])) == 7, "D1003 render-record count drift")
    require(
        "This receipt does not update the Tohoku mapping ledger; mapping promotion belongs to the next no-overwrite successor."
        in audit.get("nonclaims", []),
        "D1003 mapping nonclaim drift",
    )
    return {"receipt": record(D1003_AUDIT, "D1003_CHECK.json"), "status": "STRICT_PASS", "errors": []}


def verify_builds() -> dict[str, object]:
    artifacts = expected_artifacts()
    for name, expected in artifacts.items():
        require_identity(ROOT / name, expected)
    r42 = BASE.BASE.BASE.load_legacy_validator()
    specs = {**r42.BUILD_SPECS, "cohomology": {"pages": 221, "visual": [25, 26, 27, 28, 29, 30, 31]}}
    aux_lines = {**r42.EXPECTED_AUX_LINES}
    aux_lines["cohomology.aux"] = (
        r"\newlabel{lemma-crossed-homomorphism-torsor-obstruction}{{4.4}{5}{The torsor obstruction of a crossed homomorphism}{subsection.4.4}{}}",
        r"\newlabel{lemma-pointwise-flasque-envelope-groups}{{12.2}{22}{Pointwise flasque envelope}{subsection.12.2}{}}",
        r"\newlabel{lemma-flasque-group-torsors-trivial}{{12.3}{22}{}{subsection.12.3}{}}",
        r"\newlabel{lemma-pointwise-envelope-crossed-homomorphism}{{12.4}{23}{The crossed quotient of a pointwise envelope}{subsection.12.4}{}}",
        r"\newlabel{lemma-pointwise-envelope-torsor-bijection}{{12.5}{24}{Pointwise envelopes lift torsors uniquely}{subsection.12.5}{}}",
        r"\newlabel{lemma-pointwise-envelope-degree-two-boundary}{{12.8}{26}{The degree-two boundary of a pointwise envelope}{subsection.12.8}{}}",
        r"\newlabel{definition-fine-abelian-sheaf}{{22.6}{53}{Fine abelian sheaves}{subsection.22.6}{}}",
        r"\newlabel{lemma-fine-phi-soft-and-tensor}{{22.7}{54}{}{subsection.22.7}{}}",
        r"\newlabel{lemma-cartan-resolution-fine-torsion-free}{{22.16}{58}{Cartan resolution}{subsection.22.16}{}}",
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
    require(tex.count(r"\label{lemma-pointwise-envelope-degree-two-boundary}") == 1, "D1003 source label multiplicity drift")
    for evidence in (
        "the twisted middle term below with a pointwise envelope",
        "No compatibility with arbitrary inverse image functors is asserted here.",
        r"\mathcal A^{\mathcal E}",
        r"\cong\Pi(\mathcal F^{\mathcal E})",
        r"\partial(\mathcal E)=",
        r"\delta_{\mathcal Q,\alpha}\bigl(d_u(\mathcal Q)\bigr)",
        r"is independent of the choice of $(\mathcal Q,\alpha)$.",
        r"[\mathcal E]\ \text{is induced by a }\mathcal G\text{-torsor}",
        r"Any two possible $\varphi$ differ locally by a section of the twisted",
        "the transition $a_{ij}$ satisfies $a_{ij}+e_i=e_j$.",
        r"\delta_{\mathcal F,\mathcal A,\mathcal F'}",
        r"\partial(E)=-d(Q)$.",
    ):
        require(evidence in tex, f"D1003 source proof/nonclaim drift: {evidence}")
    inherited = strict_json(SOURCE / "r45-check.json").get("builds", {}).get("independent_audits", {})
    require(
        set(inherited)
        == {"D000996", "D000997", "D000998", "D000999", "D001000", "D001001", "D001002", "D001003", "D001004"},
        "r45 independent-audit inheritance drift",
    )
    builds["independent_audits"] = {
        **inherited,
        "D001005": {
            "status": "STRICT_PASS",
            "receipt": record(D1003_AUDIT, "D1003_CHECK.json"),
            "scope": [
                "twisted degree-two obstruction from a P-lift",
                "middle twist identified with the pointwise envelope of F^E",
                "independence from the chosen P-lift and compatible identification",
                "zero iff E is induced from a G-torsor",
                "221-page strict parse and pages 25-31 clean",
            ],
        },
        "D001006": {
            "status": "STRICT_PASS",
            "receipt": record(D1003_AUDIT, "D1003_CHECK.json"),
            "scope": [
                "central-extension pointed map H1(H) to H2(F)",
                "zero fibre equals the image of G-torsor classes",
                "abelian specialization is the usual connecting homomorphism",
            ],
        },
        "D001007": {
            "status": "STRICT_PASS",
            "receipt": record(D1003_AUDIT, "D1003_CHECK.json"),
            "scope": [
                "Stacks left-torsor plus-sign convention",
                "Tohoku inverse-transition minus-sign convention",
                "same obstruction under translated conventions",
            ],
        },
        "D001008": {
            "status": "STRICT_PASS",
            "receipt": record(D1003_AUDIT, "D1003_CHECK.json"),
            "scope": [
                "abelian 3-by-3 anticommutativity",
                "inverse cocycle cancels the comparison minus",
                "agreement with the standard boundary map",
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
    require(set(new_by) - set(old_by) == {NEW_LABEL_ROW["full_label"]}, "D1003 new-label set drift")
    require(new_by[NEW_LABEL_ROW["full_label"]] == NEW_LABEL_ROW, "D1003 new-label row drift")
    require(new_by[TORSOR_LABEL_ROW["full_label"]] == TORSOR_LABEL_ROW, "Inherited torsor-label row drift")
    require(new_by[OBSTRUCTION_LABEL_ROW["full_label"]] == OBSTRUCTION_LABEL_ROW, "Inherited obstruction-label row drift")
    changed = []
    for label in old_by:
        if old_by[label] != new_by[label]:
            require(
                all(old_by[label][field] == new_by[label][field] for field in fields if field != "line"),
                f"Existing label substantive metadata drift: {label}",
            )
            require(
                int(new_by[label]["line"]) - int(old_by[label]["line"]) == 209,
                f"Existing label line-shift drift: {label}",
            )
            changed.append(label)
    require(Counter(old_by[label]["file"] for label in changed) == Counter({"cohomology.tex": 460}), "Existing label line-only oracle drift")

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
            require(
                int(new_c[key]["line"]) - int(old_c[key]["line"]) == 209,
                f"Existing candidate line-shift drift: {key}",
            )
            changed_candidates.append(key)
    require(Counter(old_c[key]["file"] for key in changed_candidates) == Counter({"cohomology.tex": 193}), "Candidate line-only oracle drift")
    require(len(index) == 22055 and len(candidates) == 1263 and len(topic_map) == 13, "Scanner count oracle drift")
    require(sum(1 for row in index if row["tag"]) == 21437, "Official-tag join count drift")
    require(len(warnings) == 627, "Scanner warning count drift")
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
            "existing_rows_line_number_only": 460,
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
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SOURCE), "r45 predecessor surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected r45 predecessor subdirectory")
    records = []
    for name, expected in sorted(EXPECTED_SOURCE.items()):
        require_identity(SOURCE / name, expected)
        records.append(record(SOURCE / name))
    require(
        (len(records), sum(int(item["bytes"]) for item in records), aggregate(records)) == EXPECTED_SOURCE_SURFACE,
        "r45 predecessor aggregate drift",
    )
    payload_records = [item for item in records if item["name"] != "r45-check.json"]
    require(
        (len(payload_records), sum(int(item["bytes"]) for item in payload_records), aggregate(payload_records)) == EXPECTED_SOURCE_PAYLOAD_SURFACE,
        "r45 predecessor payload aggregate drift",
    )
    predecessor = strict_json(SOURCE / "r45-check.json")
    require(predecessor.get("schema") == "tohoku-stacks-mapping-successor-r45-v1", "r45 predecessor receipt schema drift")
    require(predecessor.get("status") == "PASS" and predecessor.get("errors") == [], "r45 predecessor receipt not PASS")
    require(predecessor.get("deltas", {}).get("decisions") == 1004, "r45 predecessor decision gate drift")
    require(predecessor.get("deltas", {}).get("mapping_counts", {}).get("dispositions", {}).get("new_statement") == 19, "r45 D1003 predecessor gap gate drift")
    for name, expected in expected_runtime().items():
        require_identity(ROOT / name, expected)
    for name, expected in BASE.BASE.BASE.load_legacy_validator().EXPECTED_AUTHORITY.items():
        require_identity(AUTHORITY / name, expected)
    require(Path(sys.executable).resolve() == EXPECTED_PYTHON.resolve(), "Python executable path drift")
    require_identity(EXPECTED_PYTHON, EXPECTED_PYTHON_IDENTITY)
    require(sys.version_info[:3] == (3, 13, 9) and sys.implementation.cache_tag == "cpython-313", "Python runtime drift")
    semantic = verify_semantic()
    repairs = verify_repairs()
    d1003 = verify_d1003_audit()
    builds = verify_builds()
    scanner = verify_scanner_oracle()
    return {
        "predecessor": {
            "name": "tohoku_r45",
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
        "d1003_audit": d1003,
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
    expected_names = PAYLOAD | ({"r46-check.json"} if receipt_mode else set())
    require({path.name for path in entries if path.is_file()} == expected_names, "Stage/target file surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected stage/target subdirectory")

    cfg = strict_json(root / "cfg.json")
    require(cfg.get("dossier_id") == "tohoku_r46", "r46 cfg dossier ID drift")
    require(cfg.get("expected_units") == 991, "r46 cfg unit count drift")
    require(cfg.get("semantic_successor", {}).get("generation") == "sem/r17", "r46 cfg semantic generation drift")
    require(cfg.get("semantic_successor", {}).get("surface_files") == 18, "r46 cfg semantic file count drift")
    require(cfg.get("semantic_successor", {}).get("surface_bytes") == EXPECTED_SEM_SURFACE[1], "r46 cfg semantic bytes drift")
    require(cfg.get("semantic_successor", {}).get("surface_sha256") == EXPECTED_SEM_SURFACE[2], "r46 cfg semantic aggregate drift")
    primary = cfg.get("inputs", {}).get("primary", {})
    require(primary.get("source_file") == "sem/r17/nodes.csv", "r46 cfg primary source drift")
    require(primary.get("sha256") == EXPECTED_SEM["nodes.csv"][1], "r46 cfg node pin drift")
    require(cfg.get("inputs", {}).get("sem_manifest", {}).get("sha256") == EXPECTED_SEM["manifest.json"][1], "r46 cfg manifest pin drift")
    require(cfg.get("inputs", {}).get("sem_validation", {}).get("sha256") == EXPECTED_SEM["validation.json"][1], "r46 cfg validation pin drift")

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
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r46 scan counts drift")
    require(check.get("warnings") == scanner["warnings"], "r46 scan warnings drift")
    require(check.get("tex_sha256") == scanner["tex_hashes"], "r46 scan TeX hashes drift")
    runtime = expected_runtime()
    require(check.get("sha256", {}).get("tags/tags") == runtime["tags/tags"][1], "r46 scan tag hash drift")

    unit_fields, units = load_csv(root / "units.csv")
    projected_units = expected_units(cfg)
    require(unit_fields == BASE.BASE.BASE.load_intake().FIELDS, "r46 unit schema drift")
    require(units == projected_units, "r46 units differ from exact sem/r17 intake projection")
    require(intake.get("counts", {}).get("units") == 991, "r46 intake unit receipt drift")

    fields, old_decisions = load_csv(SOURCE / "dec.csv")
    new_fields, decisions = load_csv(root / "dec.csv")
    require(fields == new_fields, "Decision schema drift")
    require([row["decision_id"] for row in decisions] == [f"D{number:06d}" for number in range(1, 1009)], "Decision sequence drift")
    require(decisions[:1004] == old_decisions and decisions[1004:] == DECISION_ROWS, "Decision prefix/appended rows drift")
    require((root / "dec.csv").read_bytes().startswith((SOURCE / "dec.csv").read_bytes()), "Decision byte prefix drift")
    anchors = {
        "D000308": (DECISION_ROWS[0], "new_statement"),
        "D000262": (DECISION_ROWS[1], "new_statement"),
        "D000311": (DECISION_ROWS[2], "example_or_remark"),
        "D000312": (DECISION_ROWS[3], "example_or_remark"),
    }
    old_by_id = {row["decision_id"]: row for row in old_decisions}
    for decision_id, (successor, expected_disposition) in anchors.items():
        anchor = old_by_id.get(decision_id, {})
        require(anchor.get("unit_id") == successor["unit_id"], f"{decision_id} supersession unit drift")
        require(anchor.get("disposition") == expected_disposition, f"{decision_id} predecessor disposition drift")

    _, issues = load_csv(root / "issues.csv")
    require(len(issues) == 29 and all(row["status"] == "resolved" for row in issues), "r46 issue ledger drift")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r46 mapping counts drift")
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
    require(map_fields == expected_fields, "r46 map schema drift")
    projected_map = expected_map(cfg, projected_units, scanner, root / "dec.csv")
    require(mapped == projected_map, "r46 map differs from independent sem/r17 + live scanner + ledger replay")
    _, old_map = load_csv(SOURCE / "map.csv")
    old_by = {row["unit_id"]: row for row in old_map}
    new_by = {row["unit_id"]: row for row in mapped}
    target_units = {row["unit_id"] for row in DECISION_ROWS}
    require(set(old_by) == set(new_by) and len(new_by) == 991, "Map stable-unit set drift")
    for unit_id in set(new_by) - target_units:
        require(new_by[unit_id] == old_by[unit_id], f"Unauthorized r46 map mutation: {unit_id}")
    authorized_fields_by_decision = {
        "D001005": {"decision_id", "disposition", "review_state", "stacks_labels", "rationale"},
        "D001006": {"decision_id", "disposition", "review_state", "stacks_labels", "rationale"},
        "D001007": {"decision_id", "review_state", "stacks_labels", "rationale"},
        "D001008": {"decision_id", "review_state", "stacks_labels", "rationale"},
    }
    for decision in DECISION_ROWS:
        unit_id = decision["unit_id"]
        authorized_fields = authorized_fields_by_decision[decision["decision_id"]]
        changed_fields = {field for field in expected_fields if old_by[unit_id][field] != new_by[unit_id][field]}
        require(changed_fields == authorized_fields, f"{decision['decision_id']} map mutation field set drift")
        for field in authorized_fields:
            require(new_by[unit_id][field] == decision[field], f"{decision['decision_id']} mapped {field} drift")
        require(new_by[unit_id]["stacks_tags"] == "", f"{decision['decision_id']} unexpectedly claims an official tag")
    require(new_by["tohoku:claim:3.4.2:u-properties"]["decision_id"] == "D001001", "D001001 no longer selected")
    require(new_by["tohoku:construction:flabby-envelope"]["decision_id"] == "D001000", "D001000 no longer selected")
    require(new_by["tohoku:claim:3.4.2:H1-bijection"]["decision_id"] == "D001002", "D001002 no longer selected")
    require(new_by["tohoku:construction:3.4.2:associated-P-bundle"]["decision_id"] == "D001003", "D001003 no longer selected")
    require(new_by["tohoku:construction:3.4.2:dQ-obstruction"]["decision_id"] == "D001004", "D001004 no longer selected")
    require(new_by["tohoku:reduction:3.4.2:E-via-Q"]["decision_id"] == "D000310", "D000310 structural selection drift")
    require(new_by["tohoku:reduction:3.4.2:E-via-Q"]["disposition"] == "structural_only", "D000310 disposition drift")

    gap_count = sum(EXPECTED_MAPPING_COUNTS["dispositions"][name] for name in ("existing_weaker", "extend_existing", "new_statement", "new_section"))
    require(gap_count == 54, "Gap-class arithmetic drift")
    status = (root / "STATUS.md").read_text(encoding="utf-8")
    for token in (
        "sem/r17", "D001005", "D001006", "D001007", "D001008",
        "D000308", "D000262", "D000311", "D000312", "D000310", "54 gap-class",
    ):
        require(token in status, f"STATUS missing token: {token}")

    result = {
        "status": "PASS",
        "errors": [],
        "stable_units": 991,
        "decisions": 1008,
        "decisions_appended": DECISION_ROWS,
        "active_source_issues": [],
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": EXPECTED_SCAN_COUNTS,
        "scanner_delta": scanner["delta"],
        "remaining_gap_class_dispositions": 54,
        "semantic_generation": "sem/r17",
        "authorized_map_mutations": {
            "units": sorted(target_units),
            "fields_by_decision": {
                decision_id: sorted(fields)
                for decision_id, fields in sorted(authorized_fields_by_decision.items())
            },
            "unchanged_units": 987,
        },
        "byte_identical_payloads": ["topics.csv", "issues.csv", "units.csv"],
        "external_evidence": {
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "repair_aggregate_sha256": external["repairs"]["aggregate_sha256"],
            "d1003_audit_sha256": external["d1003_audit"]["receipt"]["sha256"],
        },
    }

    if receipt_mode:
        receipt = strict_json(root / "r46-check.json")
        require(receipt.get("schema") == "tohoku-stacks-mapping-successor-r46-v1", "r46 receipt schema drift")
        require(receipt.get("status") == "PASS" and receipt.get("errors") == [], "r46 receipt not PASS")
        require(receipt.get("deltas") == result, "r46 receipt delta replay mismatch")
        require(receipt.get("files") == [record(root / name) for name in sorted(PAYLOAD)], "r46 receipt output records drift")
        require(receipt.get("predecessor_dossier") == external["predecessor"], "r46 receipt predecessor evidence drift")
        require(receipt.get("semantic_source") == external["semantic"], "r46 receipt semantic evidence drift")
        require(receipt.get("source_repairs") == external["repairs"], "r46 receipt repair evidence drift")
        require(receipt.get("decision_audit") == external["d1003_audit"], "r46 receipt D1003 evidence drift")
        require(receipt.get("builds") == external["builds"], "r46 receipt build evidence drift")
        execution = receipt.get("execution", {})
        require(execution.get("contract") == "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion_with_rollback", "r46 execution contract drift")
        require(set(execution.get("attestation", {})) == {"driver", "bootstrap", "builder", "validator"}, "r46 execution attestation surface drift")
    return result


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R46_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if not raw:
        return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r46.py", "bytes": actual[0], "sha256": actual[1]}
    expected = json.loads(raw)
    require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator same-bytes attestation drift")
    return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r46.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not os.path.lexists(TARGET), f"No-overwrite r46 target already exists: {TARGET}")
        require(not os.path.lexists(STAGE), f"Unresolved r46 transaction exists: {STAGE}")
        external = verify_external()
        result = {
            "schema": "tohoku-r46-static-input-audit-v1",
            "status": "PASS",
            "errors": [],
            "attestation": attestation,
            "target_absent": True,
            "stage_absent": True,
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "predecessor_payload_aggregate_sha256": external["predecessor"]["payload_aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "d1003_audit": external["d1003_audit"],
            "scanner_delta": external["scanner"]["delta"],
            "builds": external["builds"],
            "projected_mapping_counts": EXPECTED_MAPPING_COUNTS,
            "launch_authorized": False,
        }
    else:
        result = {
            "schema": "tohoku-r46-stage-validation-v1",
            "attestation": attestation,
            **verify_stage(args.stage.resolve(), args.receipt),
        }
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
