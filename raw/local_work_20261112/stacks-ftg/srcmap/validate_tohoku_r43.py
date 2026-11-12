#!/usr/bin/env python3
"""Independent bounded validator for the frozen no-overwrite Tohoku r43 successor."""

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
SOURCE = ROOT / "tohoku_r42"
TARGET = ROOT / "tohoku_r43"
STAGE = ROOT / ".tohoku-r43-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r17"
AUTHORITY = PROJECT / "authority_snapshot"
LEGACY_VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r42.py"
LEGACY_BUILDER = ROOT / "srcmap" / "build_tohoku_r42.py"

EXPECTED_LEGACY_VALIDATOR = (
    49153,
    "517A511FE190B27A79375CC8AB35DD008562165E8A60F69D708FDAB12CED1DF0",
)
EXPECTED_LEGACY_BUILDER = (
    21164,
    "5F638CA638625023AA1095329AC225DD84E2774D4AE468C2AE53AFC7B12B2355",
)

EXPECTED_SOURCE = {
    "STATUS.md": (1027, "40BEFBEB191301E8D934A649F66B88F394C019352D42DB850B85A77DD10997C1"),
    "cfg.json": (4971, "CEF412B87B547C1D988E9EB84977A5D67169414CD2FEFC2BFD5B446328AC86A7"),
    "check.json": (76634, "557F45CB7155EB0DBC14E1C8AF30447EEF69688A774354656D98EB06479592A4"),
    "dec.csv": (359028, "E4C40F09BB002ABBE302FC5E54B222F649B7FD940D40784625EBF9EF57D89534"),
    "intake.json": (1578, "D704348498DA314AA72CB3AF5B66D4DDB134A25E14D9860FB4A9CC33C7B5DB53"),
    "issues.csv": (29535, "3439D68823BF69087F025976FB0AC41C2C4D93B8BFB4E63D6FD3267DB6AC178A"),
    "map.csv": (472581, "5941919A3267B27F98CF18FF5772F1F31F71FE099D2981EB1B71D49705E08F9B"),
    "mcheck.json": (66461, "8AF8ADF41DC3604C0C35C76EFF08ED5DAEE93C972434200D983174E8DA17EBE9"),
    "r42-check.json": (27078, "CEEDA9448469378476F37D6F8E2E23CBF292F71813B7DA18C90B430457769DB9"),
    "stx.csv": (5272935, "6F0AC0791182D00677E6DAFE4B95F5EC0152BB9C064A6FFAAE789AB89A42EB8C"),
    "tcand.csv": (483151, "D02A10BA6C76220EC533FBA46AD915329DEC9434ED33E7927F15D62D32F14491"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (392313, "860A1DB0627F115CF0EF1B5700075C257E4724A5E0DF00301BC855DF7E719B54"),
}
EXPECTED_SOURCE_SURFACE = (
    15,
    7192289,
    "6E613884C627B90D525C91964F167B43E764C7D0D0769B8BC4B70D83E6141006",
)

EXPECTED_SEM = {
    "README.md": (2585, "66D4CF92728AF7FF10E82CDFD97AFCD9D26B55CE9FBC985932FFBCD597DD64B4"),
    "bib.csv": (10422, "93F5A934ADDE0CD92BBB21AF70EFD81BA128CCD2EDF51EB19428B83437EC3516"),
    "catalog.csv": (772, "F1E15DC6CC1667659D73CF6207B1325C9C7A8C7B1F2500BA3B4703E2FB1346C4"),
    "edges.csv": (260944, "F1607445D52F28DA2F3FE93D8F47D7959C35ECFFBC167B5AB0E787A91264C719"),
    "idmap.csv": (473, "977D4A8F59A9642D58926DED8BB600079863AE6AF3F1F532806E83A9AB645BEA"),
    "manifest.json": (25297, "128998F88CD5D3F15142451DBABA507A40123A7B523F3CDCCAB2B00EDF7E8016"),
    "nodes.csv": (583867, "DA5C172DFE1392202E39703692BE0FDE832B5D97AA62C87BFC6AA99AF72DA8EC"),
    "objects.csv": (106319, "82FF34C19C6D17D80DC3A617FD106ED324099CC9D0F2FE752757D0642ED31999"),
    "occ.csv": (515082, "1EF9F42BAD4223F6C351C202E6B7B706E9C08F308F33AFDF9CD6A962DC9ABBB4"),
    "pages.csv": (23686, "E813C410B0A2AE53B4A787FD6C66A74225021E3A0FE22AD10CA2ED0C29807B0D"),
    "refdec.csv": (2313, "6AC5E23C3D4ADA0ABB1427E0533C3033E13B63C28A654A9C7E74A057A045FFA2"),
    "refs.csv": (159815, "995C9526CEC36FB6B437D7C688E4D40547BFC050949E3819A607FEEF53EA1162"),
    "resid.csv": (6415, "DDF53E58E21C7A5BF60C54ADC5EB9EB420B717246F1C69F294BBA5E358A38430"),
    "stacks.csv": (11777, "E13EFA405B525D69BFF38256601E4AF64D22FA3075F3A95AB3DFB78C15CFD060"),
    "subjects.csv": (2133, "A77A81831F752BA21701B150C13C51325E511B2FD5DFC76EED135FE3EDEEB026"),
    "terms.csv": (325587, "6D93CBBD2D6CF3E354FE90DC51605ACD9C7B0932CEF216FB9D606AD97D666E5D"),
    "validation.json": (6285, "7CB31C7A5B2AE59809E5B9007EE371A4BA64347007A9636486D74F9341F6C47E"),
    "xwork.csv": (2446, "7BC42D7026C34AD8B1A111353E0810378F1DB9D1284BAD4C5C34D509D57B9EBB"),
}
EXPECTED_SEM_SURFACE = (
    18,
    2046218,
    "EAFD3352FDDEF93AD19FE1A3994F9B71EA65A2E1CBC0293BE91035450563AE96",
)
EXPECTED_SEM_PAYLOAD_SURFACE = (
    16,
    2014636,
    "C67C606D70367923DEEF7FF64FA3142257871ADEE5E665225D4D9CA9C5EFB4B3",
)

NEW_REPAIRS = {
    "build/v068c3r15/build.json": (31834, "BD35C62A83935B5782109D08FA265E5885C7F63CD2D90401A6B7C0430F511AC5"),
    "build/v068c3r15/fr/main-fr.pdf": (1412572, "C1FC2E2C3726B96F82E02AAEBBC478649823E2BD2A66F9C4AFC526315D494DC9"),
    "build/v068c3r15/en/main-en.pdf": (1377305, "36CF451528D61819F0385415F6929FBBA6D7559278F45B58117839E982817584"),
    "qa/v68r37/check.json": (22946, "48BAE9B34FB5EBA92F03C06E6A3E9F163DDE23C01A96669FD52AF49DD7A59FB6"),
}

COHOMOLOGY_ARTIFACTS = {
    "cohomology.tex": (824473, "1D0FB283E28ADA8952A2BA7983AD41B6969E8BDC9917AD375343C09F3AF496B1"),
    "cohomology.aux": (51948, "5AD4EC3C14CD8E944BDC0FCA76DD4717F9D040D274B11638C7EDC91C981164A0"),
    "cohomology.log": (47540, "557F55E94B12E616E9680B7C4CAB0FC7B9A7EA2D51A7FD28E899260B32874679"),
    "cohomology.pdf": (1845078, "F4E497637F495AA69CE92227B62099337C999A14669B2614DEA4FF37DD9B7767"),
}

DECISION_ROW = {
    "decision_id": "D001000",
    "unit_id": "tohoku:construction:flabby-envelope",
    "action": "replace",
    "disposition": "existing_equivalent",
    "stacks_labels": "cohomology-lemma-pointwise-flasque-envelope-groups;cohomology-lemma-flasque-group-torsors-trivial",
    "rationale": "Stacks now constructs, functorially for every sheaf of sets, the pointwise product sheaf U↦∏_{x∈U}F_x and its canonical germ monomorphism. For sheaves of possibly noncommutative groups this is a flasque group sheaf (and remains abelian in the abelian case), with surjectivity obtained by identity fillers. Stacks also proves by the source's Zorn argument that every torsor under a flasque group sheaf is trivial; hence the torsor-class pointed set is a singleton and H^1 vanishes in the abelian case. The arbitrary-set construction is not claimed flasque when empty stalks occur, and the point factors are not claimed to be the stalks of the product sheaf.",
    "review_state": "integrated_source_stacks_and_independent_review",
    "supersedes": "D000251",
}
DECISION_ROWS = [DECISION_ROW]

EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "decisions": 1000,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 351,
        "existing_stronger": 38,
        "existing_weaker": 9,
        "extend_existing": 22,
        "historical_reference": 33,
        "new_section": 6,
        "new_statement": 22,
        "structural_only": 426,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 29,
    "unit_candidates": 0,
    "units": 991,
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22052,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1263,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_SCAN_OUTPUTS = {
    "stx.csv": (5273402, "8F273D61A82968FCCDCC09584E2310C2DEDE31A644BA6F6442F1646D80D3B50F"),
    "tcand.csv": (483152, "9F8A0688805047612C04F3F09A59FBBEBD8CB963AE055FAD5CF4C265E6977ACC"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
}
NEW_LABEL_ROWS = {
    "cohomology-lemma-flasque-group-torsors-trivial": (
        "cohomology.tex", "2256", "lemma", "lemma-flasque-group-torsors-trivial",
        "Cohomology of Sheaves", "section-flasque", "Flasque sheaves",
        "0D0BA09775F530C0DD7F96EF75B28712DB8D249F344015EE210A0D0688882E97",
    ),
    "cohomology-lemma-pointwise-flasque-envelope-groups": (
        "cohomology.tex", "2210", "lemma", "lemma-pointwise-flasque-envelope-groups",
        "Cohomology of Sheaves", "section-flasque", "Flasque sheaves",
        "3FFAF0C2DEAEDECD1B35B45013EFA07A4101144B2199F72238C6E9E7430F6131",
    ),
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


def load_legacy_validator():
    require_identity(LEGACY_VALIDATOR, EXPECTED_LEGACY_VALIDATOR)
    module = load_module(LEGACY_VALIDATOR, "tohoku_r43_pinned_r42_validator")
    require_identity(LEGACY_VALIDATOR, EXPECTED_LEGACY_VALIDATOR)
    return module


def expected_runtime() -> dict[str, tuple[int, str]]:
    legacy = load_legacy_validator()
    return {
        **legacy.EXPECTED_RUNTIME,
        "srcmap/validate_tohoku_r42.py": EXPECTED_LEGACY_VALIDATOR,
        "srcmap/build_tohoku_r42.py": EXPECTED_LEGACY_BUILDER,
    }


def expected_repairs() -> dict[str, tuple[int, str]]:
    return {**load_legacy_validator().EXPECTED_REPAIRS, **NEW_REPAIRS}


def expected_artifacts() -> dict[str, tuple[int, str]]:
    return {**load_legacy_validator().EXPECTED_ARTIFACTS, **COHOMOLOGY_ARTIFACTS}


def expected_tex_hashes() -> dict[str, str]:
    hashes = dict(strict_json(SOURCE / "check.json")["tex_sha256"])
    require(len(hashes) == 119, "Predecessor TeX manifest is not 119 files")
    hashes["cohomology.tex"] = COHOMOLOGY_ARTIFACTS["cohomology.tex"][1]
    return hashes


def load_mkidx():
    return load_module(ROOT / "fga" / "mkidx.py", "tohoku_r43_pinned_mkidx")


def load_mkmap():
    return load_module(ROOT / "fga" / "mkmap.py", "tohoku_r43_pinned_mkmap")


def load_intake():
    return load_module(ROOT / "srcmap" / "intake.py", "tohoku_r43_pinned_intake")


def verify_semantic() -> dict[str, object]:
    require_plain_directory(SEM)
    entries = list(SEM.iterdir())
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SEM), "sem/r17 file surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected sem/r17 subdirectory")
    records = []
    for name, expected in sorted(EXPECTED_SEM.items()):
        require_identity(SEM / name, expected)
        records.append(record(SEM / name))
    surface = (len(records), sum(int(item["bytes"]) for item in records), aggregate(records))
    require(surface == EXPECTED_SEM_SURFACE, "sem/r17 complete surface aggregate drift")

    manifest = strict_json(SEM / "manifest.json")
    validation = strict_json(SEM / "validation.json")
    require(manifest.get("schema") == "tohoku-semantic-local-successor-manifest-v17", "sem/r17 manifest schema drift")
    require(manifest.get("errors") == [], "sem/r17 manifest errors")
    require(validation.get("schema") == "tohoku-semantic-local-successor-validation-v17", "sem/r17 validation schema drift")
    require(validation.get("status") == "PASS" and validation.get("errors") == [], "sem/r17 validation not PASS")
    require(validation.get("manifest_sha256") == EXPECTED_SEM["manifest.json"][1], "sem/r17 manifest-validation binding drift")
    file_surface = manifest.get("file_surface", {})
    require(
        (file_surface.get("records"), file_surface.get("bytes"), file_surface.get("aggregate_sha256"))
        == EXPECTED_SEM_PAYLOAD_SURFACE,
        "sem/r17 16-record payload surface drift",
    )
    expected_payload = {
        name: {"name": name, "bytes": expected[0], "sha256": expected[1]}
        for name, expected in EXPECTED_SEM.items()
        if name not in {"manifest.json", "validation.json"}
    }
    actual_payload = {str(item.get("name")): item for item in manifest.get("files", [])}
    require(actual_payload == expected_payload, "sem/r17 manifest file records drift")

    oracle = manifest.get("table_delta_oracle", {})
    require(oracle.get("changed_table_count") == 3, "sem/r17 changed-table count drift")
    require(set(oracle.get("changed_tables", {})) == {"catalog.csv", "nodes.csv", "occ.csv"}, "sem/r17 changed-table set drift")
    require(oracle.get("unchanged_table_count") == 12, "sem/r17 unchanged-table count drift")
    require(oracle.get("unchanged_inherited_file_count") == 13, "sem/r17 unchanged-file count drift")
    require(oracle.get("all_row_counts_invariant") is True and oracle.get("all_stable_ids_invariant") is True, "sem/r17 stable-ID/count oracle drift")

    override = manifest.get("semantic_override", {})
    require(override.get("decision_id") == "TOH-P161-COR-003", "sem/r17 override decision drift")
    require(override.get("node_id") == "tohoku:construction:divisor-sequence:p2", "sem/r17 override node drift")
    require(override.get("occurrence_id") == "tohoku:occ:p161:o001", "sem/r17 override occurrence drift")
    require(override.get("segments") == {
        "dip": {"bytes": 286, "sha256": "3F397DBBA23BD4AF86AEF79A55F5A0A1501919D799319FCBF964538BBAC42D73"},
        "fr": {"bytes": 294, "sha256": "F66CF5B2591000E61AB4233CAB9F79D1BB7E68289A8FFC171EE4A307B4E9DEB7"},
        "en": {"bytes": 294, "sha256": "728105454EE2CFCA2BA507F714A7F52C591A8D905AA64DB3C93F4C671B0242F1"},
    }, "sem/r17 p161 segment binding drift")
    reader = manifest.get("reader_binding", {})
    require(reader.get("qa_receipt", {}).get("sha256") == NEW_REPAIRS["qa/v68r37/check.json"][1], "sem/r17 reader QA binding drift")
    require(reader.get("reader_receipt", {}).get("sha256") == NEW_REPAIRS["build/v068c3r15/build.json"][1], "sem/r17 reader receipt binding drift")
    require(reader.get("french_pdf", {}).get("sha256") == NEW_REPAIRS["build/v068c3r15/fr/main-fr.pdf"][1], "sem/r17 French PDF binding drift")
    require(reader.get("english_pdf", {}).get("sha256") == NEW_REPAIRS["build/v068c3r15/en/main-en.pdf"][1], "sem/r17 English PDF binding drift")

    _, nodes = load_csv(SEM / "nodes.csv")
    require(len(nodes) == 991 and len({row["node_id"] for row in nodes}) == 991, "sem/r17 node ID/count drift")
    by_id = {row["node_id"]: row for row in nodes}
    require(DECISION_ROW["unit_id"] in by_id, "D001000 semantic unit missing")
    divisor = by_id["tohoku:construction:divisor-sequence:p2"]
    require(divisor.get("en_label") == override.get("labels", {}).get("en"), "sem/r17 p161 English label drift")
    require(divisor.get("fr_label") == override.get("labels", {}).get("fr"), "sem/r17 p161 French label drift")
    return {
        "generation": "sem/r17",
        "files": records,
        "file_count": len(records),
        "bytes": sum(int(item["bytes"]) for item in records),
        "aggregate_sha256": aggregate(records),
        "manifest_payload_surface": {
            "file_count": EXPECTED_SEM_PAYLOAD_SURFACE[0],
            "bytes": EXPECTED_SEM_PAYLOAD_SURFACE[1],
            "aggregate_sha256": EXPECTED_SEM_PAYLOAD_SURFACE[2],
        },
        "validation_status": "PASS",
        "independent_postbuild_audit": "STRICT_PASS",
        "p161_semantic_override": "EXACT",
    }


def verify_repairs() -> dict[str, object]:
    repairs = expected_repairs()
    records = []
    for relative, expected in sorted(repairs.items()):
        path = PROJECT / relative
        require_identity(path, expected)
        records.append(record(path, relative))
    qa = strict_json(PROJECT / "qa" / "v68r37" / "check.json")
    require(qa.get("status") == "PASS" and qa.get("errors") == [], "reader r15 QA not PASS")
    require(qa.get("stable_id") == "tohoku:reader-qa:v68r37:v068c3r15", "reader r15 QA stable ID drift")
    require(qa.get("conclusion", {}).get("blockers") == [], "reader r15 QA blockers")
    require(qa.get("conclusion", {}).get("reader_successor_accepted") is True, "reader r15 not accepted")
    build = strict_json(PROJECT / "build" / "v068c3r15" / "build.json")
    require(build.get("status") == "PASS" and build.get("errors") == [], "reader r15 build not PASS")
    p161 = strict_json(PROJECT / "production" / "p161_fix1" / "check.json")
    require(p161.get("status") == "PASS" and p161.get("errors") == [], "p161_fix1 not PASS")
    return {
        "files": records,
        "file_count": len(records),
        "bytes": sum(int(item["bytes"]) for item in records),
        "aggregate_sha256": aggregate(records),
        "reader_r15": "PASS",
        "reader_r15_independent_qa": "STRICT_PASS",
        "p161_fix1": "SEALED_REPLAY_PASS",
    }


def verify_builds() -> dict[str, object]:
    artifacts = expected_artifacts()
    for name, expected in artifacts.items():
        require_identity(ROOT / name, expected)
    legacy = load_legacy_validator()
    specs = {**legacy.BUILD_SPECS, "cohomology": {"pages": 216, "visual": [21, 22, 23]}}
    aux_lines = {**legacy.EXPECTED_AUX_LINES}
    aux_lines["cohomology.aux"] = (
        r"\newlabel{definition-fine-abelian-sheaf}{{22.6}{48}{Fine abelian sheaves}{subsection.22.6}{}}",
        r"\newlabel{lemma-fine-phi-soft-and-tensor}{{22.7}{49}{}{subsection.22.7}{}}",
        r"\newlabel{lemma-cartan-resolution-fine-torsion-free}{{22.16}{53}{Cartan resolution}{subsection.22.16}{}}",
        r"\newlabel{lemma-pointwise-flasque-envelope-groups}{{12.2}{22}{Pointwise flasque envelope}{subsection.12.2}{}}",
        r"\newlabel{lemma-flasque-group-torsors-trivial}{{12.3}{22}{}{subsection.12.3}{}}",
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
    for label in (
        "lemma-pointwise-flasque-envelope-groups",
        "lemma-flasque-group-torsors-trivial",
    ):
        require(tex.count(r"\label{" + label + "}") == 1, f"D001000 source label multiplicity drift: {label}")
    for caveat in (
        "the product need not be flasque when\nsome of the factors are empty",
        "they are not asserted\nto be the stalks of $\\Pi(\\mathcal F)$",
        "extend a tuple by putting the identity",
        "Zorn's lemma gives a maximal pair",
    ):
        require(caveat in tex, f"D001000 source proof/caveat drift: {caveat}")
    predecessor_audits = strict_json(SOURCE / "r42-check.json").get("builds", {}).get("independent_audits", {})
    require(set(predecessor_audits) == {"D000996", "D000997", "D000998", "D000999"}, "r42 independent-audit inheritance drift")
    builds["independent_audits"] = {
        **predecessor_audits,
        "D001000": {
            "status": "STRICT_PASS",
            "scope": [
                "pointwise product sheaf and germ monomorphism",
                "group flasqueness by identity fillers",
                "flasque-group torsor triviality by Zorn",
                "abelian H1 vanishing",
                "empty-stalk and non-stalk caveats",
                "216-page strict parse and pages 21-23 clean",
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
    require(set(new_by) - set(old_by) == set(NEW_LABEL_ROWS), "D001000 new-label set drift")
    for label, expected in NEW_LABEL_ROWS.items():
        file, line, kind, short_label, chapter, section_label, section_title, text_sha256 = expected
        require(new_by[label] == {
            "tag": "", "full_label": label, "file": file, "line": line,
            "kind": kind, "short_label": short_label, "chapter": chapter,
            "section_label": section_label, "section_title": section_title,
            "text_sha256": text_sha256,
        }, f"D001000 new-label row drift: {label}")
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
    require(len(index) == 22052 and len(candidates) == 1263 and len(topic_map) == 13, "Scanner count oracle drift")
    require(sum(1 for row in index if row["tag"]) == 21437, "Official-tag join count drift")
    require(len(warnings) == 624, "Scanner warning count drift")
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
            "new_labels": 2,
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
    require({path.name for path in entries if path.is_file()} == set(EXPECTED_SOURCE), "r42 predecessor surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected r42 predecessor subdirectory")
    records = []
    for name, expected in sorted(EXPECTED_SOURCE.items()):
        require_identity(SOURCE / name, expected)
        records.append(record(SOURCE / name))
    require(
        (len(records), sum(int(item["bytes"]) for item in records), aggregate(records)) == EXPECTED_SOURCE_SURFACE,
        "r42 predecessor aggregate drift",
    )
    predecessor = strict_json(SOURCE / "r42-check.json")
    require(predecessor.get("schema") == "tohoku-stacks-mapping-successor-r42-v1", "r42 predecessor receipt schema drift")
    require(predecessor.get("status") == "PASS" and predecessor.get("errors") == [], "r42 predecessor receipt not PASS")
    require(predecessor.get("deltas", {}).get("decisions") == 999, "r42 predecessor decision gate drift")
    require(predecessor.get("deltas", {}).get("mapping_counts", {}).get("dispositions", {}).get("extend_existing") == 23, "r42 predecessor D001000 gap gate drift")
    for name, expected in expected_runtime().items():
        require_identity(ROOT / name, expected)
    legacy = load_legacy_validator()
    for name, expected in legacy.EXPECTED_AUTHORITY.items():
        require_identity(AUTHORITY / name, expected)
    require(sys.version_info[:3] == (3, 13, 9) and sys.implementation.cache_tag == "cpython-313", "Python runtime drift")
    semantic = verify_semantic()
    repairs = verify_repairs()
    builds = verify_builds()
    scanner = verify_scanner_oracle()
    return {
        "predecessor": {
            "name": "tohoku_r42",
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
    _, nodes = load_csv(SEM / "nodes.csv")
    units = load_intake().tohoku_units(nodes, cfg)
    require(len(units) == 991, "Independent unit projection count drift")
    return units


def expected_map(cfg: dict, units: list[dict[str, str]], scanner: dict[str, object], decisions_path: Path) -> list[dict[str, str]]:
    topic_map = {row["topic_id"]: row for row in scanner["topic_map"]}
    structural = set(cfg.get("structural_types", []))
    embedded = set(cfg.get("embedded_types", []))
    historical = set(cfg.get("historical_types", []))
    mapped: list[dict[str, str]] = []
    for unit in units:
        topic_ids = [value for value in unit["topics"].split(";") if value]
        require(set(topic_ids) <= set(topic_map), f"Unknown topic in independent projection: {unit['id']}")
        labels = sorted({
            label for topic in topic_ids
            for label in topic_map[topic]["evidence_labels"].split(";") if label
        })
        tags = sorted({
            tag for topic in topic_ids
            for tag in topic_map[topic]["evidence_tags"].split(";") if tag
        })
        kind = unit["unit_type"]
        if kind in structural:
            disposition, state, rationale = "structural_only", "classified", "Source structure; no independent Stacks object."
        elif kind in embedded:
            disposition, state, rationale = "structural_only", "inherits_parent", "Embedded source component; inherit the parent disposition."
        elif kind in historical:
            disposition, state, rationale = "historical_reference", "needs_link_review", "Historical or bibliographic unit requiring source linkage."
        else:
            disposition, state, rationale = "needs_review", "generated_intake", "Requires statement-level mathematical comparison."
        mapped.append({
            "unit_id": unit["id"], "item": unit["item"], "unit_type": kind,
            "parent_id": unit["parent_id"], "source_start": unit["source_start"],
            "source_end": unit["source_end"],
            "source_loc": f"{unit['source_file']}:{unit['source_line']}",
            "authority_sha256": unit["authority_sha256"],
            "source_topics": ";".join(topic_ids),
            "topic_evidence_labels": ";".join(labels),
            "topic_evidence_tags": ";".join(tags),
            "decision_id": "", "disposition": disposition,
            "review_state": state, "stacks_labels": "", "stacks_tags": "",
            "rationale": rationale,
        })
    mkmap = load_mkmap()
    decisions, errors = mkmap.load_decisions(decisions_path, mapped, scanner["index"])
    require(errors == [], f"Independent decision replay errors: {errors}")
    mkmap.apply_decisions(mapped, decisions)
    return mapped


def verify_stage(root: Path, receipt_mode: bool) -> dict[str, object]:
    external = verify_external()
    require_plain_directory(root)
    entries = list(root.iterdir())
    expected_names = PAYLOAD | ({"r43-check.json"} if receipt_mode else set())
    require({path.name for path in entries if path.is_file()} == expected_names, "Stage/target file surface drift")
    require(not any(path.is_dir() for path in entries), "Unexpected stage/target subdirectory")

    cfg = strict_json(root / "cfg.json")
    require(cfg.get("dossier_id") == "tohoku_r43", "r43 cfg dossier ID drift")
    require(cfg.get("expected_units") == 991, "r43 cfg unit count drift")
    require(cfg.get("semantic_successor", {}).get("generation") == "sem/r17", "r43 cfg semantic generation drift")
    require(cfg.get("semantic_successor", {}).get("surface_files") == 18, "r43 cfg semantic file count drift")
    require(cfg.get("semantic_successor", {}).get("surface_bytes") == 2046218, "r43 cfg semantic bytes drift")
    require(cfg.get("semantic_successor", {}).get("surface_sha256") == EXPECTED_SEM_SURFACE[2], "r43 cfg semantic aggregate drift")
    primary = cfg.get("inputs", {}).get("primary", {})
    require(primary.get("source_file") == "sem/r17/nodes.csv", "r43 cfg primary source drift")
    require(primary.get("sha256") == EXPECTED_SEM["nodes.csv"][1], "r43 cfg node pin drift")
    require(cfg.get("inputs", {}).get("sem_manifest", {}).get("sha256") == EXPECTED_SEM["manifest.json"][1], "r43 cfg manifest pin drift")
    require(cfg.get("inputs", {}).get("sem_validation", {}).get("sha256") == EXPECTED_SEM["validation.json"][1], "r43 cfg validation pin drift")
    require("sem_input" not in cfg.get("inputs", {}) and "sem_check" not in cfg.get("inputs", {}), "Stale semantic QA inputs remain in r43 cfg")

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
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r43 scan counts drift")
    require(check.get("warnings") == scanner["warnings"], "r43 scan warnings drift")
    require(check.get("tex_sha256") == scanner["tex_hashes"], "r43 scan TeX hashes drift")
    runtime = expected_runtime()
    require(check.get("sha256", {}).get("tags/tags") == runtime["tags/tags"][1], "r43 scan tag hash drift")

    unit_fields, units = load_csv(root / "units.csv")
    projected_units = expected_units(cfg)
    require(unit_fields == load_intake().FIELDS, "r43 unit schema drift")
    require(units == projected_units, "r43 units differ from exact sem/r17 intake projection")
    require(intake.get("counts", {}).get("units") == 991, "r43 intake unit receipt drift")
    divisor = next(row for row in units if row["id"] == "tohoku:construction:divisor-sequence:p2")
    require(divisor["source_file"] == "sem/r17/nodes.csv" and divisor["topics"] == "grothendieck-category", "p161 semantic propagation drift")
    require(divisor["title_en"].startswith("D is flabby"), "p161 corrected subject did not propagate")

    fields, old_decisions = load_csv(SOURCE / "dec.csv")
    new_fields, decisions = load_csv(root / "dec.csv")
    require(fields == new_fields, "Decision schema drift")
    require([row["decision_id"] for row in decisions] == [f"D{number:06d}" for number in range(1, 1001)], "Decision sequence drift")
    require(decisions[:999] == old_decisions and decisions[999:] == DECISION_ROWS, "Decision prefix/appended row drift")
    require((root / "dec.csv").read_bytes().startswith((SOURCE / "dec.csv").read_bytes()), "Decision byte prefix drift")
    require(old_decisions[250]["decision_id"] == "D000251" and old_decisions[250]["unit_id"] == DECISION_ROW["unit_id"], "D000251 supersession anchor drift")
    require(old_decisions[250]["disposition"] == "extend_existing", "D000251 predecessor disposition drift")

    _, issues = load_csv(root / "issues.csv")
    require(len(issues) == 29 and all(row["status"] == "resolved" for row in issues), "r43 issue ledger drift")
    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r43 mapping counts drift")
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
    require(map_fields == expected_fields, "r43 map schema drift")
    projected_map = expected_map(cfg, projected_units, scanner, root / "dec.csv")
    require(mapped == projected_map, "r43 map differs from independent sem/r17 + live scanner + ledger replay")
    by_unit = {row["unit_id"]: row for row in mapped}
    d1000 = by_unit[DECISION_ROW["unit_id"]]
    for field in ("decision_id", "disposition", "review_state", "stacks_labels", "rationale"):
        expected = DECISION_ROW[field if field != "decision_id" else "decision_id"]
        require(d1000[field] == expected, f"D001000 mapped {field} drift")
    require(d1000["stacks_tags"] == "", "D001000 unexpectedly claims an official tag")
    d999 = by_unit["tohoku:construction:divisor-sequence:p2"]
    require(d999["decision_id"] == "D000999", "D000999 no longer selected")
    require(d999["source_topics"] == "grothendieck-category", "D000999 sem/r17 topic propagation drift")
    require(d999["topic_evidence_labels"] == "injectives-section-grothendieck-categories;injectives-section-grothendieck-conditions", "D000999 topic evidence label drift")
    require(d999["topic_evidence_tags"] == "05AB;079A", "D000999 topic evidence tag drift")

    gap_count = sum(EXPECTED_MAPPING_COUNTS["dispositions"][name] for name in ("existing_weaker", "extend_existing", "new_statement", "new_section"))
    require(gap_count == 59, "Gap-class arithmetic drift")
    status = (root / "STATUS.md").read_text(encoding="utf-8")
    for token in ("sem/r17", "D001000", "D000251", "D000999", "59 gap-class"):
        require(token in status, f"STATUS missing token: {token}")

    result = {
        "status": "PASS",
        "errors": [],
        "stable_units": 991,
        "decisions": 1000,
        "decisions_appended": DECISION_ROWS,
        "active_source_issues": [],
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": EXPECTED_SCAN_COUNTS,
        "scanner_delta": scanner["delta"],
        "remaining_gap_class_dispositions": 59,
        "semantic_generation": "sem/r17",
        "semantic_p161_propagation": {
            "unit_id": "tohoku:construction:divisor-sequence:p2",
            "corrected_subject": "D",
            "source_topics": "grothendieck-category",
            "selected_decision": "D000999",
        },
        "byte_identical_payloads": ["topics.csv", "issues.csv"],
        "external_evidence": {
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "repair_aggregate_sha256": external["repairs"]["aggregate_sha256"],
        },
    }

    if receipt_mode:
        receipt = strict_json(root / "r43-check.json")
        require(receipt.get("schema") == "tohoku-stacks-mapping-successor-r43-v1", "r43 receipt schema drift")
        require(receipt.get("status") == "PASS" and receipt.get("errors") == [], "r43 receipt not PASS")
        require(receipt.get("deltas") == result, "r43 receipt delta replay mismatch")
        require(receipt.get("files") == [record(root / name) for name in sorted(PAYLOAD)], "r43 receipt output records drift")
        require(receipt.get("predecessor_dossier") == external["predecessor"], "r43 receipt predecessor evidence drift")
        require(receipt.get("semantic_source") == external["semantic"], "r43 receipt semantic evidence drift")
        require(receipt.get("source_repairs") == external["repairs"], "r43 receipt repair evidence drift")
        require(receipt.get("builds") == external["builds"], "r43 receipt build evidence drift")
        execution = receipt.get("execution", {})
        require(execution.get("contract") == "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion_with_rollback", "r43 execution contract drift")
        require(set(execution.get("attestation", {})) == {"driver", "bootstrap", "builder", "validator"}, "r43 execution attestation surface drift")
    return result


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R43_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if not raw:
        return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r43.py", "bytes": actual[0], "sha256": actual[1]}
    expected = json.loads(raw)
    require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator same-bytes attestation drift")
    return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r43.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        require(not os.path.lexists(TARGET), f"No-overwrite r43 target already exists: {TARGET}")
        require(not os.path.lexists(STAGE), f"Unresolved r43 transaction exists: {STAGE}")
        external = verify_external()
        result = {
            "schema": "tohoku-r43-static-input-audit-v1",
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
            "schema": "tohoku-r43-stage-validation-v1",
            "attestation": attestation,
            **verify_stage(args.stage.resolve(), args.receipt),
        }
    print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
