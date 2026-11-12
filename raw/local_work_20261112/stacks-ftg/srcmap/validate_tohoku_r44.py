#!/usr/bin/env python3
"""Independent bounded validator for the frozen no-overwrite Tohoku r44 successor."""

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
SOURCE = ROOT / "tohoku_r43"
TARGET = ROOT / "tohoku_r44"
STAGE = ROOT / ".tohoku-r44-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r17"
AUTHORITY = PROJECT / "authority_snapshot"
BASE_VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r43.py"
BASE_BUILDER = ROOT / "srcmap" / "build_tohoku_r43.py"
EXPECTED_BASE_VALIDATOR = (
    45131,
    "56E6B95D0A8A1842B2BF35814FF31CE6456A7F7DEDAFD764B5BBFD9650983F20",
)
EXPECTED_BASE_BUILDER = (
    21241,
    "6B79ACE3B3B2A46409924CD416212C427ED2954179149676CBD49D9418874092",
)
EXPECTED_PYTHON = Path(r"user\miniconda3\python.exe")
EXPECTED_PYTHON_IDENTITY = (
    104264,
    "7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264",
)

EXPECTED_SOURCE = {
    "STATUS.md": (1092, "350B8A1E8E33D578BBB0E6E769B13DC74A8551ACA4BBAA4ECA04DB1F0DC86381"),
    "cfg.json": (5151, "9C33378FBB527855B6F48D9403593A303C60AC2AB3720E237D7E669C8FFBFF02"),
    "check.json": (76842, "2411CC0FEEB9C0755FAB87EBE5FDEFEE0058C95ADF9C0ED9E6457B4FACF2E3A4"),
    "dec.csv": (359919, "B78E3CE4637EC4EEF61E93BF09E0BDD28A57CF549CCCAD4FF47F3142905E7065"),
    "intake.json": (1578, "8279157B8AA7F6AA006E2C434C34D2A7988836D63C25B3465B93896D62E22801"),
    "issues.csv": (29535, "3439D68823BF69087F025976FB0AC41C2C4D93B8BFB4E63D6FD3267DB6AC178A"),
    "map.csv": (473253, "E3E3F2B4495D7A3DF1DF7D5A69FC2E991FECC2620A65DF7993845AD36AE1C2E5"),
    "mcheck.json": (66670, "1A712A63E1BD874E13B3F01516C7AF7952EE40A7EF94AD78C3E99DBA077D2705"),
    "r43-check.json": (25007, "B7E1160C2CBE63BA453925B0676D68A2097FEC6D8BA0AD21A587BDB0E83906E5"),
    "stx.csv": (5273402, "8F273D61A82968FCCDCC09584E2310C2DEDE31A644BA6F6442F1646D80D3B50F"),
    "tcand.csv": (483152, "9F8A0688805047612C04F3F09A59FBBEBD8CB963AE055FAD5CF4C265E6977ACC"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (392568, "3AB04435EEDD9DE59E61DF2443812C2F555DD6CA85542DC7F9C6BBE59DB03081"),
}
EXPECTED_SOURCE_SURFACE = (
    15,
    7193166,
    "DE6370EB1FD73CB32A36ABC28F98980CC6D6E04D4A0D6FE7F2435248615230E9",
)

COHOMOLOGY_ARTIFACTS = {
    "cohomology.tex": (828174, "C610AC61C928E4F0F8B89F4D3FEE0E666DDE59D2C5B68FC699B5A43AF6C8ECFF"),
    "cohomology.aux": (52084, "9643BF58C696916705A966B8A58FAC5E6F2AD3BD3765C21F8E10E6508EFB0066"),
    "cohomology.log": (47546, "705B6BCFD65397A8A05F7F75A704C8918FBFDC273E791D2B9BE78E1200D60E91"),
    "cohomology.pdf": (1850635, "607A5E53D8F4E510C932E0016EEA51E0A33899EC75858A3CD93A90D4DE3A4C4B"),
}

DECISION_ROW = {
    "decision_id": "D001001",
    "unit_id": "tohoku:claim:3.4.2:u-properties",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "cohomology-lemma-pointwise-envelope-crossed-homomorphism",
    "rationale": "Stacks now formalizes the source's specific pointwise-envelope quotient: for an abelian normal sheaf F⊂G it defines A=Π(F), B=Π(G), P=AG as the local-product subsheaf, and F'=A/F as the quotient sheaf; proves A∩G=F and the conjugation action; and constructs the sheaf-of-sets epimorphism u(ag)=a mod F with neutral fibre G, crossed identity, and right-G coset fibres. It explicitly does not claim sectionwise surjectivity or that u is a group homomorphism.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000238",
}
DECISION_ROWS = [DECISION_ROW]

EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "decisions": 1001,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 352,
        "existing_stronger": 38,
        "existing_weaker": 9,
        "extend_existing": 22,
        "historical_reference": 33,
        "new_section": 6,
        "new_statement": 21,
        "structural_only": 426,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 29,
    "unit_candidates": 0,
    "units": 991,
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22053,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1263,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_SCAN_OUTPUTS = {
    "stx.csv": (5273652, "4E8094C09A8856D976E255FC70B400D35CC9C6995D14C36E7CE478838AC7538D"),
    "tcand.csv": (483153, "617F794ABBF0EF39EF08DE2CD1DA8E0CE8B4093319EFF4C55677CA0B29B58F46"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
}
NEW_LABEL_ROW = {
    "tag": "",
    "full_label": "cohomology-lemma-pointwise-envelope-crossed-homomorphism",
    "file": "cohomology.tex",
    "line": "2294",
    "kind": "lemma",
    "short_label": "lemma-pointwise-envelope-crossed-homomorphism",
    "chapter": "Cohomology of Sheaves",
    "section_label": "section-flasque",
    "section_title": "Flasque sheaves",
    "text_sha256": "2836B06CE436010E4F5D6893D6B4D8DAC8E3CE48B125D75FCBFC6D6EF132E425",
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
    module = load_module(BASE_VALIDATOR, "tohoku_r44_pinned_r43_validator")
    require_identity(BASE_VALIDATOR, EXPECTED_BASE_VALIDATOR)
    return module


BASE = load_base_validator()
EXPECTED_SEM = dict(BASE.EXPECTED_SEM)
EXPECTED_SEM_SURFACE = BASE.EXPECTED_SEM_SURFACE
EXPECTED_SEM_PAYLOAD_SURFACE = BASE.EXPECTED_SEM_PAYLOAD_SURFACE


def expected_runtime() -> dict[str, tuple[int, str]]:
    return {
        **BASE.expected_runtime(),
        "srcmap/validate_tohoku_r43.py": EXPECTED_BASE_VALIDATOR,
        "srcmap/build_tohoku_r43.py": EXPECTED_BASE_BUILDER,
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
    return load_module(ROOT / "fga" / "mkidx.py", "tohoku_r44_pinned_mkidx")


def verify_semantic() -> dict[str, object]:
    return BASE.verify_semantic()


def verify_repairs() -> dict[str, object]:
    return BASE.verify_repairs()


def verify_builds() -> dict[str, object]:
    artifacts = expected_artifacts()
    for name, expected in artifacts.items():
        require_identity(ROOT / name, expected)
    r42 = BASE.load_legacy_validator()
    specs = {**r42.BUILD_SPECS, "cohomology": {"pages": 217, "visual": [21, 22, 23, 24, 25]}}
    aux_lines = {**r42.EXPECTED_AUX_LINES}
    aux_lines["cohomology.aux"] = (
        r"\newlabel{lemma-pointwise-flasque-envelope-groups}{{12.2}{22}{Pointwise flasque envelope}{subsection.12.2}{}}",
        r"\newlabel{lemma-flasque-group-torsors-trivial}{{12.3}{22}{}{subsection.12.3}{}}",
        r"\newlabel{lemma-pointwise-envelope-crossed-homomorphism}{{12.4}{23}{The crossed quotient of a pointwise envelope}{subsection.12.4}{}}",
        r"\newlabel{definition-fine-abelian-sheaf}{{22.6}{49}{Fine abelian sheaves}{subsection.22.6}{}}",
        r"\newlabel{lemma-fine-phi-soft-and-tensor}{{22.7}{50}{}{subsection.22.7}{}}",
        r"\newlabel{lemma-cartan-resolution-fine-torsion-free}{{22.16}{54}{Cartan resolution}{subsection.22.16}{}}",
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
    require(tex.count(r"\label{lemma-pointwise-envelope-crossed-homomorphism}") == 1, "D001001 source label multiplicity drift")
    for evidence in (
        r"\mathcal A\cap\mathcal G=\mathcal F",
        r"u(pp')=u(p)\sigma_p(u(p'))",
        r"u^{-1}(1)=\mathcal G",
        "need\nnot be surjective on sections over every open",
        "In general $u$ is not a\nhomomorphism of sheaves of groups",
    ):
        require(evidence in tex, f"D001001 source proof/nonclaim drift: {evidence}")
    inherited = strict_json(SOURCE / "r43-check.json").get("builds", {}).get("independent_audits", {})
    require(set(inherited) == {"D000996", "D000997", "D000998", "D000999", "D001000"}, "r43 independent-audit inheritance drift")
    builds["independent_audits"] = {
        **inherited,
        "D001001": {
            "status": "STRICT_PASS",
            "scope": [
                "pointwise envelopes and local-product subsheaf",
                "A intersect G equals F and conjugation action",
                "quotient-sheaf crossed morphism and neutral fibre",
                "right-G coset fibres",
                "no sectionwise-surjectivity or group-homomorphism claim",
                "217-page strict parse and pages 21-25 clean",
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
    require(set(new_by) - set(old_by) == {NEW_LABEL_ROW["full_label"]}, "D001001 new-label set drift")
    require(new_by[NEW_LABEL_ROW["full_label"]] == NEW_LABEL_ROW, "D001001 new-label row drift")
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
    require(len(index) == 22053 and len(candidates) == 1263 and len(topic_map) == 13, "Scanner count oracle drift")
    require(sum(1 for row in index if row["tag"]) == 21437, "Official-tag join count drift")
    require(len(warnings) == 625, "Scanner warning count drift")
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
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SOURCE), "r43 predecessor surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected r43 predecessor subdirectory")
    records = []
    for name, expected in sorted(EXPECTED_SOURCE.items()):
        require_identity(SOURCE / name, expected)
        records.append(record(SOURCE / name))
    require(
        (len(records), sum(int(item["bytes"]) for item in records), aggregate(records)) == EXPECTED_SOURCE_SURFACE,
        "r43 predecessor aggregate drift",
    )
    predecessor = strict_json(SOURCE / "r43-check.json")
    require(predecessor.get("schema") == "tohoku-stacks-mapping-successor-r43-v1", "r43 predecessor receipt schema drift")
    require(predecessor.get("status") == "PASS" and predecessor.get("errors") == [], "r43 predecessor receipt not PASS")
    require(predecessor.get("deltas", {}).get("decisions") == 1000, "r43 predecessor decision gate drift")
    require(predecessor.get("deltas", {}).get("mapping_counts", {}).get("dispositions", {}).get("new_statement") == 22, "r43 D001001 predecessor gate drift")
    for name, expected in expected_runtime().items():
        require_identity(ROOT / name, expected)
    for name, expected in BASE.load_legacy_validator().EXPECTED_AUTHORITY.items():
        require_identity(AUTHORITY / name, expected)
    require(Path(sys.executable).resolve() == EXPECTED_PYTHON.resolve(), "Python executable path drift")
    require_identity(EXPECTED_PYTHON, EXPECTED_PYTHON_IDENTITY)
    require(sys.version_info[:3] == (3, 13, 9) and sys.implementation.cache_tag == "cpython-313", "Python runtime drift")
    semantic = verify_semantic()
    repairs = verify_repairs()
    builds = verify_builds()
    scanner = verify_scanner_oracle()
    return {
        "predecessor": {
            "name": "tohoku_r43",
            "files": records,
            "file_count": len(records),
            "bytes": sum(int(item["bytes"]) for item in records),
            "aggregate_sha256": aggregate(records),
        },
        "semantic": semantic,
        "repairs": repairs,
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
    expected_names = PAYLOAD | ({"r44-check.json"} if receipt_mode else set())
    require({path.name for path in entries if path.is_file()} == expected_names, "Stage/target file surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected stage/target subdirectory")

    cfg = strict_json(root / "cfg.json")
    require(cfg.get("dossier_id") == "tohoku_r44", "r44 cfg dossier ID drift")
    require(cfg.get("expected_units") == 991, "r44 cfg unit count drift")
    require(cfg.get("semantic_successor", {}).get("generation") == "sem/r17", "r44 cfg semantic generation drift")
    require(cfg.get("semantic_successor", {}).get("surface_files") == 18, "r44 cfg semantic file count drift")
    require(cfg.get("semantic_successor", {}).get("surface_bytes") == EXPECTED_SEM_SURFACE[1], "r44 cfg semantic bytes drift")
    require(cfg.get("semantic_successor", {}).get("surface_sha256") == EXPECTED_SEM_SURFACE[2], "r44 cfg semantic aggregate drift")
    primary = cfg.get("inputs", {}).get("primary", {})
    require(primary.get("source_file") == "sem/r17/nodes.csv", "r44 cfg primary source drift")
    require(primary.get("sha256") == EXPECTED_SEM["nodes.csv"][1], "r44 cfg node pin drift")
    require(cfg.get("inputs", {}).get("sem_manifest", {}).get("sha256") == EXPECTED_SEM["manifest.json"][1], "r44 cfg manifest pin drift")
    require(cfg.get("inputs", {}).get("sem_validation", {}).get("sha256") == EXPECTED_SEM["validation.json"][1], "r44 cfg validation pin drift")

    intake = strict_json(root / "intake.json")
    check = strict_json(root / "check.json")
    mcheck = strict_json(root / "mcheck.json")
    for name, value in (("intake", intake), ("scan", check), ("map", mcheck)):
        require(value.get("status") == "PASS" and value.get("errors") == [], f"{name} receipt not PASS")
    require(mcheck.get("outputs_promoted") is True, "Mapping outputs not promoted")
    require((root / "topics.csv").read_bytes() == (SOURCE / "topics.csv").read_bytes(), "topics.csv drift")
    require((root / "issues.csv").read_bytes() == (SOURCE / "issues.csv").read_bytes(), "issues.csv drift")

    scanner = external["scanner"]
    for name in ("stx.csv", "tcand.csv", "tmap.csv"):
        require((root / name).read_bytes() == scanner["serialized"][name], f"{name} does not match exact live oracle")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r44 scan counts drift")
    require(check.get("warnings") == scanner["warnings"], "r44 scan warnings drift")
    require(check.get("tex_sha256") == scanner["tex_hashes"], "r44 scan TeX hashes drift")
    runtime = expected_runtime()
    require(check.get("sha256", {}).get("tags/tags") == runtime["tags/tags"][1], "r44 scan tag hash drift")

    unit_fields, units = load_csv(root / "units.csv")
    projected_units = expected_units(cfg)
    require(unit_fields == BASE.load_intake().FIELDS, "r44 unit schema drift")
    require(units == projected_units, "r44 units differ from exact sem/r17 intake projection")
    require((root / "units.csv").read_bytes() == (SOURCE / "units.csv").read_bytes(), "Unchanged sem/r17 unit bytes drift")
    require(intake.get("counts", {}).get("units") == 991, "r44 intake unit receipt drift")

    fields, old_decisions = load_csv(SOURCE / "dec.csv")
    new_fields, decisions = load_csv(root / "dec.csv")
    require(fields == new_fields, "Decision schema drift")
    require([row["decision_id"] for row in decisions] == [f"D{number:06d}" for number in range(1, 1002)], "Decision sequence drift")
    require(decisions[:1000] == old_decisions and decisions[1000:] == DECISION_ROWS, "Decision prefix/appended row drift")
    require((root / "dec.csv").read_bytes().startswith((SOURCE / "dec.csv").read_bytes()), "Decision byte prefix drift")
    require(old_decisions[237]["decision_id"] == "D000238" and old_decisions[237]["unit_id"] == DECISION_ROW["unit_id"], "D000238 supersession anchor drift")
    require(old_decisions[237]["disposition"] == "new_statement", "D000238 predecessor disposition drift")

    _, issues = load_csv(root / "issues.csv")
    require(len(issues) == 29 and all(row["status"] == "resolved" for row in issues), "r44 issue ledger drift")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r44 mapping counts drift")
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
    require(map_fields == expected_fields, "r44 map schema drift")
    projected_map = expected_map(cfg, projected_units, scanner, root / "dec.csv")
    require(mapped == projected_map, "r44 map differs from independent sem/r17 + live scanner + ledger replay")
    by_unit = {row["unit_id"]: row for row in mapped}
    d1001 = by_unit[DECISION_ROW["unit_id"]]
    for field in ("decision_id", "disposition", "review_state", "stacks_labels", "rationale"):
        require(d1001[field] == DECISION_ROW[field], f"D001001 mapped {field} drift")
    require(d1001["stacks_tags"] == "", "D001001 unexpectedly claims an official tag")
    require(by_unit["tohoku:construction:flabby-envelope"]["decision_id"] == "D001000", "D001000 no longer selected")
    require(by_unit["tohoku:construction:divisor-sequence:p2"]["decision_id"] == "D000999", "D000999 no longer selected")

    gap_count = sum(EXPECTED_MAPPING_COUNTS["dispositions"][name] for name in ("existing_weaker", "extend_existing", "new_statement", "new_section"))
    require(gap_count == 58, "Gap-class arithmetic drift")
    status = (root / "STATUS.md").read_text(encoding="utf-8")
    for token in ("sem/r17", "D001001", "D000238", "D001000", "58 gap-class"):
        require(token in status, f"STATUS missing token: {token}")

    result = {
        "status": "PASS",
        "errors": [],
        "stable_units": 991,
        "decisions": 1001,
        "decisions_appended": DECISION_ROWS,
        "active_source_issues": [],
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": EXPECTED_SCAN_COUNTS,
        "scanner_delta": scanner["delta"],
        "remaining_gap_class_dispositions": 58,
        "semantic_generation": "sem/r17",
        "byte_identical_payloads": ["topics.csv", "issues.csv", "units.csv"],
        "external_evidence": {
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "repair_aggregate_sha256": external["repairs"]["aggregate_sha256"],
        },
    }

    if receipt_mode:
        receipt = strict_json(root / "r44-check.json")
        require(receipt.get("schema") == "tohoku-stacks-mapping-successor-r44-v1", "r44 receipt schema drift")
        require(receipt.get("status") == "PASS" and receipt.get("errors") == [], "r44 receipt not PASS")
        require(receipt.get("deltas") == result, "r44 receipt delta replay mismatch")
        require(receipt.get("files") == [record(root / name) for name in sorted(PAYLOAD)], "r44 receipt output records drift")
        require(receipt.get("predecessor_dossier") == external["predecessor"], "r44 receipt predecessor evidence drift")
        require(receipt.get("semantic_source") == external["semantic"], "r44 receipt semantic evidence drift")
        require(receipt.get("source_repairs") == external["repairs"], "r44 receipt repair evidence drift")
        require(receipt.get("builds") == external["builds"], "r44 receipt build evidence drift")
        execution = receipt.get("execution", {})
        require(execution.get("contract") == "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion_with_rollback", "r44 execution contract drift")
        require(set(execution.get("attestation", {})) == {"driver", "bootstrap", "builder", "validator"}, "r44 execution attestation surface drift")
    return result


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R44_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if not raw:
        return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r44.py", "bytes": actual[0], "sha256": actual[1]}
    expected = json.loads(raw)
    require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator same-bytes attestation drift")
    return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r44.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not os.path.lexists(TARGET), f"No-overwrite r44 target already exists: {TARGET}")
        require(not os.path.lexists(STAGE), f"Unresolved r44 transaction exists: {STAGE}")
        external = verify_external()
        result = {
            "schema": "tohoku-r44-static-input-audit-v1",
            "status": "PASS",
            "errors": [],
            "attestation": attestation,
            "target_absent": True,
            "stage_absent": True,
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "scanner_delta": external["scanner"]["delta"],
            "builds": external["builds"],
            "projected_mapping_counts": EXPECTED_MAPPING_COUNTS,
            "launch_authorized": False,
        }
    else:
        result = {
            "schema": "tohoku-r44-stage-validation-v1",
            "attestation": attestation,
            **verify_stage(args.stage.resolve(), args.receipt),
        }
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
