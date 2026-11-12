#!/usr/bin/env python3
"""Build the no-overwrite GAGA r1 Appendix mapping successor."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "gaga"
STAGE = ROOT / "gaga_r1.__stage__"
FINAL = ROOT / "gaga_r1"
SCAN_ORACLE = ROOT / "tmp" / "gaga_appendix_postedit_scan_oracle_r1"
SCAN_REPLAY = ROOT / "tmp" / "gaga_appendix_postedit_scan_replay_r1"
DESIGN = ROOT / "tmp" / "gaga_appendix_21_24_mapping_design.json"
CANDIDATE = ROOT / "tmp" / "gaga_appendix_21_24_flat_pair_candidate.tex"
AUTHORITY_AUDIT = ROOT / "tmp" / "gaga_source_authority_rehydrated_audit.json"
SOURCE_ROOT = ROOT / "gaga_source_r1"
SOURCE_RECEIPT = SOURCE_ROOT / "SOURCE_RECEIPT.json"
VISUAL_ROOT = ROOT / "tmp" / "gaga_appendix_visual_r1"

BASE_IDENTITIES = {
    "cfg.json": (2267, "1029A91512845ACF813A134B827117FEF7D48A2F46A6358816A7916B4D6B5C28"),
    "check.json": (44117, "5786DE87FF73A982970E437F6C722A3E4577BC53822094E9FB07BA8654082BFB"),
    "dec.csv": (87, "1D302A3273D7E59D6F4BC93EBE1F9D32645ACF605CE21FDE9C155D5795686898"),
    "intake.json": (1200, "281322CD558109A475AE9FCF1A9FC3A246B2ED670BF11A57D9FD881B69C4990C"),
    "issues.csv": (88, "30C973E3978577AEBA6DE60B941DC4D88CACE6C3FCC3DDA50F6EB5F43D8BE9F5"),
    "map.csv": (58008, "8D89199320F8BECF05C73EFCB1468763AC17B0DBD3D78383160BB92887B5C0D7"),
    "mcheck.json": (33500, "0644631A04DD4F75386E92E20D1573A9C5E437F576DF2DD33A7DD35D817BE822"),
    "stx.csv": (5190190, "8EB846999032D8BE275C781BFE7DD15B5112F47AAF371670E5AFE1BFA210754C"),
    "tcand.csv": (216666, "81CD81ABD3B9022E3A0E790342AA078402F5FC2EA96F1BA0BF61A1684D76744F"),
    "tmap.csv": (1792, "E1798EA106C06DC3E5E04B8A9C659B24409DCE9FD7A451119723C6776027FD99"),
    "topics.csv": (1875, "B603A8EE4DB16870D2F2E82ED03A7BFC34D88329CFB9DC612ADDD3BF7A061CF8"),
    "ucand.csv": (460262, "CE780EC593A1E33E4E1F04B58FD3B14EEE8F16342C8AD1C603244B6E1AAC8B89"),
    "units.csv": (60100, "8F8DB43D6732A1987ACD9A02BD47E96697CFDC35DFECDF9C6207977B1D515C9B"),
}

SCAN_IDENTITIES = {
    "cfg.json": (2331, "E42E47FD00EE291C83B490E2260A10F3FF78C9A9E3F9950A12368E7DF65E26D1"),
    "topics.csv": (1875, "B603A8EE4DB16870D2F2E82ED03A7BFC34D88329CFB9DC612ADDD3BF7A061CF8"),
    "check.json": (84524, "662F0128D4B3B96F97E58F96371675B4DB4106A80B8C5238698C53FAB1E2F473"),
    "stx.csv": (5291661, "2AFD11C6BA12EDDF5BBCADFF60973BE4E1ACA58CA1A7A6E9D6C66EE0C2D55D7F"),
    "tcand.csv": (223553, "DCD9B10D7DA25D6CE3F2A29D2CCE2FF12A8CE00484989BDC260E75D26974ECB7"),
    "tmap.csv": (1792, "E1798EA106C06DC3E5E04B8A9C659B24409DCE9FD7A451119723C6776027FD99"),
}

DECISION_FIELDS = [
    "decision_id",
    "unit_id",
    "action",
    "disposition",
    "stacks_labels",
    "rationale",
    "review_state",
    "supersedes",
]

MAP_FIELDS_ALLOWED_TO_CHANGE = {
    "decision_id",
    "disposition",
    "review_state",
    "stacks_labels",
    "stacks_tags",
    "rationale",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256(path)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def strict_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"Expected JSON object: {path}")
    return value


def csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames is not None, f"Missing CSV header: {path}")
        return list(reader.fieldnames), list(reader)


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode:
        tail = "\n".join(result.stdout.splitlines()[-80:])
        raise RuntimeError(f"Command failed ({result.returncode}): {' '.join(command)}\n{tail}")
    return result


def verify_identity_table(root: Path, expected: dict[str, tuple[int, str]]) -> None:
    for name, wanted in expected.items():
        path = root / name
        require(path.is_file(), f"Missing pinned file: {path}")
        require(identity(path) == wanted, f"Identity drift: {path}")


def verify_authority_bundle() -> dict[str, Any]:
    require(identity(AUTHORITY_AUDIT) == (
        110398,
        "40AF33F5884E0344FD2A7401F87DF6E69245E285A2E6F9929C503ED08420AF35",
    ), "Authority audit identity drift")
    audit = strict_json(AUTHORITY_AUDIT)
    require(audit.get("status", "").startswith("PASS_"), "Authority audit is not PASS")
    require(identity(SOURCE_RECEIPT) == (
        5267,
        "92563794355BBDA3889CFB70CD9CC9AF8E6443A8E69E752FA293196514A44831",
    ), "Source receipt identity drift")
    receipt = strict_json(SOURCE_RECEIPT)
    require(receipt.get("status") == "STRICT_PASS", "Source receipt is not STRICT_PASS")
    checks: list[dict[str, Any]] = []
    authority = receipt["primary_authority"]
    inputs = [authority, *receipt["files"]]
    for item in inputs:
        path = SOURCE_ROOT / item["path"]
        actual = identity(path)
        expected = (int(item["bytes"]), str(item["sha256"]).upper())
        require(actual == expected, f"Authority input drift: {item['path']}")
        checks.append({"path": item["path"], "bytes": actual[0], "sha256": actual[1]})
    require(len(checks) == 12, "Authority bundle must contain exactly twelve inputs")
    require(sum(item["bytes"] for item in checks) == 4408413, "Authority byte total drift")
    return {
        "audit": record(AUTHORITY_AUDIT, "tmp/gaga_source_authority_rehydrated_audit.json"),
        "receipt": record(SOURCE_RECEIPT, "gaga_source_r1/SOURCE_RECEIPT.json"),
        "inputs": checks,
        "total_input_bytes": 4408413,
    }


def verify_build() -> dict[str, Any]:
    algebra = ROOT / "algebra.tex"
    bibliography = ROOT / "my.bib"
    pdf = ROOT / "algebra.pdf"
    log = ROOT / "algebra.log"
    aux = ROOT / "algebra.aux"
    out = ROOT / "algebra.out"
    toc = ROOT / "algebra.toc"
    bbl = ROOT / "algebra.bbl"
    require(identity(algebra) == (
        1851008,
        "1AD1C80E33CA42280B09915B7A0D15A91A9F9740C04545ADB7BFAD9B49E3BA37",
    ), "algebra.tex postimage drift")
    require(identity(bibliography) == (
        220937,
        "953C5DFAEE8F1176A1F154B40B99C751EE206D41F030299E0DE7D9807F5128E8",
    ), "my.bib postimage drift")
    source = algebra.read_text(encoding="utf-8")
    require(source.count("\\label{remark-flat-pairs-not-two-out-of-three}") == 1,
            "New Appendix repair label cardinality drift")
    require("\\cite[Appendix, nos. 22--23]{GAGA}" in source,
            "GAGA source citation missing")
    require("@ARTICLE{GAGA," in bibliography.read_text(encoding="utf-8"),
            "GAGA bibliography record missing")
    before = {path.name: sha256(path) for path in (aux, out, toc)}
    run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "algebra.tex"])
    after = {path.name: sha256(path) for path in (aux, out, toc)}
    require(before == after, "algebra auxiliary state is not at a fixed point")
    log_text = log.read_text(encoding="utf-8", errors="replace")
    forbidden = (
        "undefined references",
        "undefined citations",
        "Label(s) may have changed",
        "Rerun to get cross-references right",
        "Fatal error",
        "Emergency stop",
    )
    for phrase in forbidden:
        require(phrase not in log_text, f"Forbidden final TeX diagnostic: {phrase}")
    require(bbl.is_file() and bbl.stat().st_size > 0, "algebra.bbl is absent")
    aux_text = aux.read_text(encoding="utf-8", errors="replace")
    require("\\newlabel{remark-flat-pairs-not-two-out-of-three}{{82.11}{198}" in aux_text,
            "New remark did not stabilize on page 198")
    info = run(["pdfinfo", str(pdf)]).stdout
    require(re.search(r"^Pages:\s+471\s*$", info, re.MULTILINE) is not None,
            "Unexpected algebra.pdf page count")
    visuals = []
    for page in (198, 199):
        path = VISUAL_ROOT / f"algebra-{page}.png"
        require(path.is_file(), f"Missing visual QA page: {path}")
        visuals.append(record(path, f"tmp/gaga_appendix_visual_r1/{path.name}"))
    return {
        "algebra_tex_preimage": {
            "bytes": 1849442,
            "sha256": "EBF5B66A0C9D62263F73815DE03651214CB27259C7DBA39564C859E4A123B7D6",
        },
        "algebra_tex_postimage": record(algebra, "algebra.tex"),
        "my_bib_postimage": record(bibliography, "my.bib"),
        "algebra_pdf": {**record(pdf, "algebra.pdf"), "pages": 471},
        "fixed_point_auxiliary_sha256": after,
        "label": "algebra-remark-flat-pairs-not-two-out-of-three",
        "page": 198,
        "visual_review": {
            "status": "PASS_PRIMARY_AGENT_PAGE_AND_SEAM_INSPECTION",
            "pages": visuals,
        },
    }


def record(path: Path, name: str) -> dict[str, Any]:
    return {"name": name, "bytes": path.stat().st_size, "sha256": sha256(path)}


def decision_rows(design: dict[str, Any]) -> list[dict[str, str]]:
    rows = design.get("rows")
    require(isinstance(rows, list) and len(rows) == 18, "Design must contain eighteen rows")
    result: list[dict[str, str]] = []
    seen_units: set[str] = set()
    for number, row in enumerate(rows, start=1):
        require(row.get("ordinal") == number, "Design row order drift")
        unit_id = str(row["unit_id"])
        require(unit_id not in seen_units, f"Duplicate design unit: {unit_id}")
        seen_units.add(unit_id)
        labels = [str(value) for value in row.get("labels", [])]
        supporting = row.get("supporting_counterexample_label")
        if supporting:
            labels.append(str(supporting))
        labels.extend(str(value) for value in row.get("post_change_additional_labels", []))
        labels = list(dict.fromkeys(labels))
        rationale = str(row["rationale"])
        if unit_id == "gaga:no:22":
            rationale = (
                "The live flatness and universal-injectivity lemmas recover Definition 4 "
                "and Propositions 22 and 23. The integrated flat-pair remark proves "
                "composition and supplies the explicit non-converse, so the complete "
                "subsection is represented."
            )
        elif unit_id == "gaga:prop:23:remark":
            rationale = (
                "The integrated remark proves composition from the flatness and universal-"
                "injectivity lemmas and gives the explicit graph-inclusion counterexample "
                "A=k, B=k[t], C=B times k, with C/B congruent to B/(t) nonflat."
            )
        result.append({
            "decision_id": f"D{number:06d}",
            "unit_id": unit_id,
            "action": "set",
            "disposition": str(row["post_change_disposition"]),
            "stacks_labels": ";".join(labels),
            "rationale": rationale,
            "review_state": "reviewed_source_stacks_integrated_build_and_mapping",
            "supersedes": "",
        })
    require(all(row["disposition"] == "existing_equivalent" for row in result),
            "All Appendix decisions must close as existing_equivalent")
    return result


def write_decisions(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=DECISION_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def verify_scan() -> dict[str, Any]:
    verify_identity_table(SCAN_ORACLE, SCAN_IDENTITIES)
    verify_identity_table(SCAN_REPLAY, SCAN_IDENTITIES)
    check = strict_json(SCAN_ORACLE / "check.json")
    require(check.get("status") == "PASS" and check.get("errors") == [], "Scanner is not PASS")
    require(check.get("counts") == {
        "labels": 22117,
        "official_tags_joined": 21437,
        "tex_files": 119,
        "topic_candidates": 571,
        "topic_coverage": {"direct": 4, "no_direct": 3, "partial": 2},
        "topics": 9,
    }, "Scanner counts drift")
    fields, rows = csv_rows(SCAN_ORACLE / "stx.csv")
    matches = [row for row in rows if row["full_label"] == "algebra-remark-flat-pairs-not-two-out-of-three"]
    require(len(matches) == 1, "New scanner label cardinality drift")
    require(matches[0]["file"] == "algebra.tex" and matches[0]["line"] == "20613",
            "New scanner label location drift")
    return {
        "status": "PASS_BYTE_IDENTICAL_ORACLE_AND_REPLAY",
        "counts": check["counts"],
        "warnings": len(check.get("warnings", [])),
        "files": [record(SCAN_ORACLE / name, f"scanner/{name}") for name in SCAN_IDENTITIES],
        "new_label_row": {field: matches[0][field] for field in fields},
    }


def verify_mapping(base_map: list[dict[str, str]], decisions: list[dict[str, str]]) -> dict[str, Any]:
    mcheck = strict_json(STAGE / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "Mapping is not PASS")
    counts = mcheck.get("counts")
    require(counts.get("units") == 126, "Mapping unit count drift")
    require(counts.get("decisions") == 18 and counts.get("decided_units") == 18,
            "Mapping decision count drift")
    require(counts.get("review_units") == 61 and counts.get("candidate_units") == 61,
            "Mapping review count drift")
    require(counts.get("dispositions") == {
        "existing_equivalent": 18,
        "historical_reference": 20,
        "needs_review": 61,
        "structural_only": 27,
    }, "Mapping disposition histogram drift")
    fields, mapped = csv_rows(STAGE / "map.csv")
    require(len(mapped) == len(base_map) == 126, "Map row count drift")
    expected = {row["unit_id"]: row for row in decisions}
    changed_units: list[str] = []
    for old, new in zip(base_map, mapped, strict=True):
        require(old["unit_id"] == new["unit_id"], "Map order drift")
        changed = {field for field in fields if old[field] != new[field]}
        decision = expected.get(new["unit_id"])
        if decision is None:
            require(not changed, f"Unauthorized map delta: {new['unit_id']} {sorted(changed)}")
            continue
        require(changed == MAP_FIELDS_ALLOWED_TO_CHANGE,
                f"Unexpected decision delta: {new['unit_id']} {sorted(changed)}")
        require(new["decision_id"] == decision["decision_id"], "Decision projection drift")
        require(new["disposition"] == "existing_equivalent", "Appendix gap not closed")
        require(new["stacks_labels"] == decision["stacks_labels"], "Label projection drift")
        changed_units.append(new["unit_id"])
    require(changed_units == [row["unit_id"] for row in decisions], "Changed unit order drift")
    return {
        "counts": counts,
        "changed_units": changed_units,
        "changed_rows": 18,
        "unchanged_rows": 108,
        "appendix_true_gaps_before": 1,
        "appendix_true_gaps_after": 0,
    }


def main() -> int:
    require(not STAGE.exists(), f"No-overwrite stage exists: {STAGE}")
    require(not FINAL.exists(), f"No-overwrite final exists: {FINAL}")
    verify_identity_table(BASE, BASE_IDENTITIES)
    authority = verify_authority_bundle()
    design = strict_json(DESIGN)
    require(identity(DESIGN) == (
        42130,
        "CA52E6475F1523B17D45AFBA66E730278CAEF9279F5C4E3A6E0D50D938D04048",
    ), "Appendix design identity drift")
    require(identity(CANDIDATE) == (
        1572,
        "867657DF57E7C2F6D9CF4E1FFD3E51DC9350A30E9173C4CF903B2DB02612220C",
    ), "Appendix candidate identity drift")
    build = verify_build()
    scan = verify_scan()
    _, base_map = csv_rows(BASE / "map.csv")
    decisions = decision_rows(design)

    shutil.copytree(BASE, STAGE)
    for name in SCAN_IDENTITIES:
        shutil.copy2(SCAN_ORACLE / name, STAGE / name)
    write_decisions(STAGE / "dec.csv", decisions)
    run([sys.executable, str(ROOT / "srcmap" / "map.py"), str(STAGE)])
    first_mapping = {name: identity(STAGE / name) for name in ("map.csv", "ucand.csv", "mcheck.json")}
    run([sys.executable, str(ROOT / "srcmap" / "map.py"), str(STAGE)])
    second_mapping = {name: identity(STAGE / name) for name in ("map.csv", "ucand.csv", "mcheck.json")}
    require(first_mapping == second_mapping, "Mapping replay is not byte-identical")
    mapping = verify_mapping(base_map, decisions)

    cfg = strict_json(STAGE / "cfg.json")
    require(cfg.get("dossier_id") == "gaga_r1", "Successor dossier_id drift")
    rule_map = {row["topic_id"]: row["pattern"] for row in cfg["topic_rules"]}
    require(rule_map["analytic-space"] == "analytic space|analytic subset|analytic sheaf|holomorphic",
            "analytic-space topic repair missing")
    require(rule_map["flatness"] == "flat pair|flat module|flatness|Tor",
            "flatness topic repair missing")
    require(rule_map["proper-projective"] == r"\b(?:complete|compact|projective|proper)\b",
            "proper-projective boundary repair missing")

    status_text = (
        "# GAGA r1\n\n"
        "- The rehydrated 12-input GAGA authority chain is strictly verified.\n"
        "- Appendix nos. 21--24 have 18 audited decisions, all existing-equivalent.\n"
        "- The sole independent Appendix gap is closed by the integrated flat-pair counterexample.\n"
        "- The Algebra PDF is at a fixed point and pages 198--199 passed rendered inspection.\n"
        "- The post-edit scanner and the mapping transaction each have byte-identical replays.\n"
        "- Sixty-one substantive GAGA units remain for later tranches.\n"
    )
    (STAGE / "STATUS.md").write_text(status_text, encoding="utf-8", newline="\n")
    receipt = {
        "schema": "gaga-stacks-mapping-successor-r1-v1",
        "status": "STRICT_PASS",
        "errors": [],
        "predecessor": {
            "path": "gaga",
            "map": record(BASE / "map.csv", "gaga/map.csv"),
            "mcheck": record(BASE / "mcheck.json", "gaga/mcheck.json"),
            "units": record(BASE / "units.csv", "gaga/units.csv"),
        },
        "authority": authority,
        "source_repair": {
            "design": record(DESIGN, "tmp/gaga_appendix_21_24_mapping_design.json"),
            "candidate": record(CANDIDATE, "tmp/gaga_appendix_21_24_flat_pair_candidate.tex"),
            "build": build,
        },
        "scanner": scan,
        "mapping": mapping,
        "mapping_replay": {
            "status": "PASS_BYTE_IDENTICAL",
            "files": [record(STAGE / name, name) for name in ("map.csv", "ucand.csv", "mcheck.json")],
        },
        "topic_rule_repairs": {
            "analytic-space": rule_map["analytic-space"],
            "flatness": rule_map["flatness"],
            "proper-projective": rule_map["proper-projective"],
        },
        "files_before_receipt": [
            record(path, path.name)
            for path in sorted(STAGE.iterdir(), key=lambda item: item.name)
            if path.is_file() and path.name != "R1_CHECK.json"
        ],
        "terminal_condition": {
            "appendix_nos_21_24_true_gaps": 0,
            "remaining_gaga_needs_review": 61,
            "next": "Integrate the standalone analytic foundation and analytification spine.",
        },
    }
    (STAGE / "R1_CHECK.json").write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    require(strict_json(STAGE / "R1_CHECK.json").get("status") == "STRICT_PASS",
            "Receipt reread failed")
    STAGE.rename(FINAL)
    final_receipt = strict_json(FINAL / "R1_CHECK.json")
    require(final_receipt.get("status") == "STRICT_PASS", "Promoted receipt is not PASS")
    result = {
        "status": "STRICT_PASS",
        "path": str(FINAL),
        "receipt": record(FINAL / "R1_CHECK.json", "gaga_r1/R1_CHECK.json"),
        "appendix_true_gaps": 0,
        "remaining_needs_review": 61,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
