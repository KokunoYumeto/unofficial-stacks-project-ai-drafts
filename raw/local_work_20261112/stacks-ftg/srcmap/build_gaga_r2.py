#!/usr/bin/env python3
"""Build the no-overwrite GAGA r2 analytic-foundation successor."""

from __future__ import annotations

import csv
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

from build_gaga_r1 import csv_rows, identity, record, require, run, sha256, strict_json


ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "gaga_r1"
STAGE = ROOT / "gaga_r2.__stage__"
FINAL = ROOT / "gaga_r2"
SCAN_ORACLE = ROOT / "tmp" / "gaga_foundation_scan_oracle_r2"
SCAN_REPLAY = ROOT / "tmp" / "gaga_foundation_scan_replay_r2"
DESIGN = ROOT / "tmp" / "gaga_foundation_1_4_design.json"
CANDIDATE = ROOT / "tmp" / "gaga_foundation_1_4_candidate.tex"
VISUAL_ROOT = ROOT / "tmp" / "gaga_foundation_visual_r1"
SOURCE_COMPONENT = (
    ROOT
    / "gaga_source_r1"
    / "english_source_aligned_workpass"
    / "components"
    / "01_analytic_spaces.tex"
)

PREDECESSOR_IDENTITIES = {
    "R1_CHECK.json": (11536, "90ABB05D7CDCA4710370E354F40DCF08429B2A7E4949BFCAC2C7DF2BE4CAC06B"),
    "dec.csv": (8187, "AD7CCC0ABEA0027CA120FD57CC3D1532689FE30FCD739009CFD60DB94DABA4CA"),
    "map.csv": (64686, "B1332587032EA06E3FCCA3C595CDBA8CAEA825D7B8F278035E688B84CD84BE91"),
    "mcheck.json": (74158, "C54A746265B57E8E2202E8E601EB62A1708E9F2FDCF9F30197CBDC9161F142D7"),
    "units.csv": (60100, "8F8DB43D6732A1987ACD9A02BD47E96697CFDC35DFECDF9C6207977B1D515C9B"),
}

SCAN_IDENTITIES = {
    "cfg.json": (2331, "B96D86DB7E186D8A748CBEE9602EEF4E980BC1CA1499795F6AC3FADF0D0295C7"),
    "topics.csv": (1875, "B603A8EE4DB16870D2F2E82ED03A7BFC34D88329CFB9DC612ADDD3BF7A061CF8"),
    "check.json": (86546, "ADF9D89437FBD2E9E2C2C05ADC164B306424BE6BCD74FA73A02B70627DD9CEBB"),
    "stx.csv": (5296860, "C68BFCDF8B1B2FCE9C2A03B48B4795A95CBC6E7108DFBF6D375FAD3A7D5ABFED"),
    "tcand.csv": (248118, "8D49B1053D911F968E6321A1C223081E1C2244709EE894293A627A3A449A677D"),
    "tmap.csv": (1792, "E1798EA106C06DC3E5E04B8A9C659B24409DCE9FD7A451119723C6776027FD99"),
}

INTEGRATION_IDENTITIES = {
    "gaga.tex": (14067, "8D4C4D9C9CF3E7386077E6E00E99415E69696BFC4708C37DAFB1DD7A46FF8800"),
    "Makefile": (7935, "5F185F219D5DCCD96483F6BADA73B4C450A208F2916CFE89C76433A59FD28C4C"),
    "tags/Makefile": (2434, "BEC02700270D972098655F7BAB91E1DC716DEBF098990AEA514DC9749793E9A8"),
    "preamble.tex": (8361, "4D01949F3EA822E137C6D2305B368D86783C069E1E91A3511B6A3254BBA11E6C"),
    "chapters.tex": (8735, "C79BC934FA6DD52DB2A8AF11EECF3667CC3C682FA30239408679D62C4D49B299"),
    "my.bib": (220937, "953C5DFAEE8F1176A1F154B40B99C751EE206D41F030299E0DE7D9807F5128E8"),
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

NEW_DECISIONS = [
    {
        "unit_id": "gaga:no:1",
        "labels": [
            "gaga-definition-analytic-subset",
            "gaga-definition-holomorphic-map-analytic-subsets",
            "gaga-lemma-analytic-subset-basic-properties",
        ],
        "rationale": (
            "The standalone analytic chapter defines Serre analytic subsets, their "
            "holomorphic-function sheaves, holomorphic maps and isomorphisms, and proves "
            "the local-closedness, local-compactness, product, and functoriality claims."
        ),
    },
    {
        "unit_id": "gaga:no:2",
        "labels": [
            "gaga-section-serre-analytic-spaces",
            "gaga-definition-serre-analytic-space",
            "gaga-definition-analytic-subspace",
            "gaga-lemma-serre-analytic-subspaces-products",
        ],
        "rationale": (
            "The standalone chapter gives the reduced Hausdorff analytic-space category, "
            "holomorphic maps, charts, induced analytic subspaces, products, and the product topology."
        ),
    },
    {
        "unit_id": "gaga:def:1",
        "labels": [
            "gaga-definition-serre-analytic-space",
            "gaga-remark-serre-analytic-spaces-reduced",
        ],
        "rationale": (
            "The definition states exactly Serre's Hausdorff local-chart axioms and the "
            "adjacent scope remark makes the logically forced reduced convention explicit."
        ),
    },
    {
        "unit_id": "gaga:no:3",
        "labels": [
            "gaga-section-analytic-modules",
            "gaga-definition-analytic-module",
            "gaga-definition-vanishing-ideal-analytic-subspace",
            "gaga-theorem-oka-cartan-coherence",
            "gaga-remark-examples-coherent-analytic-modules",
            "cohomology-lemma-holomorphic-vector-bundles-locally-free-analytic-modules",
        ],
        "rationale": (
            "The chapter defines analytic modules and vanishing ideals, identifies the "
            "closed-subspace quotient, proves the Oka-Cartan coherence reduction, and records "
            "the coherent vector-bundle examples."
        ),
    },
    {
        "unit_id": "gaga:prop:1",
        "labels": ["gaga-theorem-oka-cartan-coherence"],
        "rationale": (
            "The integrated Oka-Cartan theorem states coherence of the analytic structure "
            "sheaf and every closed analytic subspace's vanishing ideal and gives the source's local reduction."
        ),
    },
    {
        "unit_id": "gaga:no:4",
        "labels": [
            "gaga-section-local-analytic-algebras",
            "gaga-lemma-local-analytic-algebra",
            "gaga-lemma-analytic-germ-local-algebra",
            "gaga-lemma-simple-point-regular-local",
            "gaga-lemma-components-dimension-analytic-space",
        ],
        "rationale": (
            "The local analytic-algebra section gives the convergent-power-series quotient, "
            "germ reconstruction, the regular/simple-point criterion, irreducible components, "
            "and equality of analytic and Krull dimensions, with analytic inputs stated explicitly."
        ),
    },
]


def verify_identities(root: Path, expected: dict[str, tuple[int, str]]) -> None:
    for name, wanted in expected.items():
        path = root / name
        require(path.is_file() and identity(path) == wanted, f"Identity drift: {path}")


def verify_source_and_design() -> dict[str, Any]:
    require(identity(SOURCE_COMPONENT) == (
        12471,
        "49C0C95E80CE4DE5341753689911045E7AD1C00C8E2CD237AA427268C251BB29",
    ), "Foundation source component drift")
    require(identity(DESIGN) == (
        48744,
        "606FE278F4459FB520EC9F0785B5CE9A1EA5E9F383E17B5A487524FC5BEAB7A1",
    ), "Foundation design drift")
    require(identity(CANDIDATE) == INTEGRATION_IDENTITIES["gaga.tex"], "Foundation candidate drift")
    design = strict_json(DESIGN)
    require(design.get("status", "").startswith("DESIGN_COMPLETE"), "Foundation design not complete")
    require([row["unit_id"] for row in design["projected_mapping_transaction"]]
            == [row["unit_id"] for row in NEW_DECISIONS], "Projected unit order drift")
    return {
        "source_component": record(SOURCE_COMPONENT, "gaga_source_r1/.../01_analytic_spaces.tex"),
        "design": record(DESIGN, "tmp/gaga_foundation_1_4_design.json"),
        "candidate": record(CANDIDATE, "tmp/gaga_foundation_1_4_candidate.tex"),
    }


def verify_live_integration() -> dict[str, Any]:
    verify_identities(ROOT, INTEGRATION_IDENTITIES)
    require((ROOT / "gaga.tex").read_bytes() == CANDIDATE.read_bytes(), "gaga.tex differs from candidate")
    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    tags_makefile = (ROOT / "tags" / "Makefile").read_text(encoding="utf-8")
    preamble = (ROOT / "preamble.tex").read_text(encoding="utf-8")
    chapters = (ROOT / "chapters.tex").read_text(encoding="utf-8")
    require("functors equiv gaga \\\n\tpione" in makefile, "Main Makefile registration missing")
    require("functors equiv gaga \\\n\tpione" in tags_makefile, "Tags Makefile registration missing")
    require("\\externaldocument[gaga-]{gaga}" in preamble, "Preamble registration missing")
    require(chapters.count("\\hyperref[gaga-section-phantom]{Complex Analytic Spaces and GAGA}") == 1,
            "Chapter list registration drift")
    for counter in (65, 82, 90, 94, 108, 110):
        require(chapters.count(f"\\setcounter{{enumi}}{{{counter}}}") == 1,
                f"Shifted chapter counter missing: {counter}")
    return {
        "files": [record(ROOT / name, name) for name in INTEGRATION_IDENTITIES],
        "registration": "PASS_MAIN_TAGS_PREAMBLE_CHAPTER_LIST_AND_COUNTERS",
    }


def verify_build() -> dict[str, Any]:
    aux_paths = [ROOT / "gaga.aux", ROOT / "gaga.out", ROOT / "gaga.toc"]
    before = {path.name: sha256(path) for path in aux_paths}
    run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "gaga.tex"])
    after = {path.name: sha256(path) for path in aux_paths}
    require(before == after, "gaga auxiliary state is not at a fixed point")
    log_text = (ROOT / "gaga.log").read_text(encoding="utf-8", errors="replace")
    for phrase in (
        "undefined references",
        "undefined citations",
        "Label(s) may have changed",
        "Rerun to get cross-references right",
        "Fatal error",
        "Emergency stop",
        "Overfull",
    ):
        require(phrase not in log_text, f"Forbidden final GAGA diagnostic: {phrase}")
    bbl = (ROOT / "gaga.bbl").read_text(encoding="utf-8")
    require("\\bibitem[Ser56]{GAGA}" in bbl, "GAGA bibliography item missing")
    info = run(["pdfinfo", str(ROOT / "gaga.pdf")]).stdout
    require(re.search(r"^Pages:\s+6\s*$", info, re.MULTILINE) is not None, "GAGA page count drift")
    visuals = []
    for page in range(1, 7):
        path = VISUAL_ROOT / f"gaga-{page}.png"
        require(path.is_file(), f"Missing rendered GAGA page {page}")
        visuals.append(record(path, f"tmp/gaga_foundation_visual_r1/{path.name}"))
    return {
        "pdf": {**record(ROOT / "gaga.pdf", "gaga.pdf"), "pages": 6},
        "fixed_point_auxiliary_sha256": after,
        "visual_review": {"status": "PASS_ALL_SIX_PAGES_PRIMARY_AGENT", "pages": visuals},
    }


def verify_scan() -> dict[str, Any]:
    verify_identities(SCAN_ORACLE, SCAN_IDENTITIES)
    verify_identities(SCAN_REPLAY, SCAN_IDENTITIES)
    check = strict_json(SCAN_ORACLE / "check.json")
    require(check.get("status") == "PASS" and check.get("errors") == [], "R2 scanner not PASS")
    require(check.get("counts") == {
        "labels": 22138,
        "official_tags_joined": 21437,
        "tex_files": 120,
        "topic_candidates": 634,
        "topic_coverage": {"direct": 4, "no_direct": 3, "partial": 2},
        "topics": 9,
    }, "R2 scanner counts drift")
    _, rows = csv_rows(SCAN_ORACLE / "stx.csv")
    gaga_labels = [row for row in rows if row["file"] == "gaga.tex"]
    require(len(gaga_labels) == 21 and len({row["full_label"] for row in gaga_labels}) == 21,
            "GAGA label inventory drift")
    expected_labels = {label for row in NEW_DECISIONS for label in row["labels"] if label.startswith("gaga-")}
    require(expected_labels.issubset({row["full_label"] for row in gaga_labels}), "Mapped GAGA labels missing")
    return {
        "status": "PASS_BYTE_IDENTICAL_ORACLE_AND_REPLAY",
        "counts": check["counts"],
        "warnings": len(check.get("warnings", [])),
        "gaga_labels": 21,
        "files": [record(SCAN_ORACLE / name, f"scanner/{name}") for name in SCAN_IDENTITIES],
    }


def append_decisions(path: Path) -> list[dict[str, str]]:
    fields, rows = csv_rows(path)
    require(fields == DECISION_FIELDS and len(rows) == 18, "Predecessor decision ledger drift")
    require([row["decision_id"] for row in rows] == [f"D{n:06d}" for n in range(1, 19)],
            "Predecessor decision sequence drift")
    for offset, item in enumerate(NEW_DECISIONS, start=19):
        rows.append({
            "decision_id": f"D{offset:06d}",
            "unit_id": item["unit_id"],
            "action": "set",
            "disposition": "existing_equivalent",
            "stacks_labels": ";".join(item["labels"]),
            "rationale": item["rationale"],
            "review_state": "reviewed_source_stacks_integrated_build_and_mapping",
            "supersedes": "",
        })
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=DECISION_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def verify_mapping(base_map: list[dict[str, str]], decisions: list[dict[str, str]]) -> dict[str, Any]:
    mcheck = strict_json(STAGE / "mcheck.json")
    require(mcheck.get("status") == "PASS" and mcheck.get("errors") == [], "R2 mapping not PASS")
    counts = mcheck["counts"]
    require(counts.get("units") == 126 and counts.get("decisions") == 24
            and counts.get("decided_units") == 24, "R2 mapping count drift")
    require(counts.get("review_units") == 55 and counts.get("candidate_units") == 55,
            "R2 review count drift")
    require(counts.get("dispositions") == {
        "existing_equivalent": 24,
        "historical_reference": 20,
        "needs_review": 55,
        "structural_only": 27,
    }, "R2 disposition histogram drift")
    fields, mapped = csv_rows(STAGE / "map.csv")
    require(len(mapped) == len(base_map) == 126, "R2 map size drift")
    new_by_unit = {row["unit_id"]: row for row in decisions[18:]}
    changed_units = []
    required = {"decision_id", "disposition", "review_state", "stacks_labels", "rationale"}
    for old, new in zip(base_map, mapped, strict=True):
        require(old["unit_id"] == new["unit_id"], "R2 map order drift")
        changed = {field for field in fields if old[field] != new[field]}
        decision = new_by_unit.get(new["unit_id"])
        if decision is None:
            require(not changed, f"Unauthorized R2 map delta: {new['unit_id']} {sorted(changed)}")
        else:
            require(changed in (required, required | {"stacks_tags"}),
                    f"Unexpected R2 map delta: {new['unit_id']} {sorted(changed)}")
            require(new["decision_id"] == decision["decision_id"]
                    and new["disposition"] == "existing_equivalent"
                    and new["stacks_labels"] == decision["stacks_labels"],
                    f"R2 decision projection drift: {new['unit_id']}")
            changed_units.append(new["unit_id"])
    require(changed_units == [row["unit_id"] for row in decisions[18:]], "R2 changed-unit order drift")
    return {
        "counts": counts,
        "changed_units": changed_units,
        "changed_rows": 6,
        "unchanged_rows": 120,
        "foundation_true_gaps_after": 0,
    }


def main() -> int:
    require(not STAGE.exists() and not FINAL.exists(), "No-overwrite R2 target exists")
    verify_identities(BASE, PREDECESSOR_IDENTITIES)
    predecessor = strict_json(BASE / "R1_CHECK.json")
    require(predecessor.get("status") == "STRICT_PASS", "R1 predecessor not PASS")
    source = verify_source_and_design()
    integration = verify_live_integration()
    build = verify_build()
    scan = verify_scan()
    _, base_map = csv_rows(BASE / "map.csv")

    shutil.copytree(BASE, STAGE)
    for name in SCAN_IDENTITIES:
        shutil.copy2(SCAN_ORACLE / name, STAGE / name)
    decisions = append_decisions(STAGE / "dec.csv")
    run([sys.executable, str(ROOT / "srcmap" / "map.py"), str(STAGE)])
    first = {name: identity(STAGE / name) for name in ("map.csv", "ucand.csv", "mcheck.json")}
    run([sys.executable, str(ROOT / "srcmap" / "map.py"), str(STAGE)])
    second = {name: identity(STAGE / name) for name in ("map.csv", "ucand.csv", "mcheck.json")}
    require(first == second, "R2 mapping replay not byte-identical")
    mapping = verify_mapping(base_map, decisions)

    status = (
        "# GAGA r2\n\n"
        "- Inherits the strictly sealed Appendix r1 successor.\n"
        "- The standalone reduced complex-analytic foundation chapter is integrated and registered.\n"
        "- All six GAGA nos. 1--4 units are existing-equivalent after source, build, visual, scanner, and mapping QA.\n"
        "- The six-page chapter and both deterministic replays pass.\n"
        "- Fifty-five substantive GAGA units remain for later tranches.\n"
    )
    (STAGE / "STATUS.md").write_text(status, encoding="utf-8", newline="\n")
    receipt = {
        "schema": "gaga-stacks-mapping-successor-r2-v1",
        "status": "STRICT_PASS",
        "errors": [],
        "predecessor": {
            "receipt": record(BASE / "R1_CHECK.json", "gaga_r1/R1_CHECK.json"),
            "map": record(BASE / "map.csv", "gaga_r1/map.csv"),
            "mcheck": record(BASE / "mcheck.json", "gaga_r1/mcheck.json"),
        },
        "source": source,
        "integration": integration,
        "build": build,
        "scanner": scan,
        "mapping": mapping,
        "mapping_replay": {
            "status": "PASS_BYTE_IDENTICAL",
            "files": [record(STAGE / name, name) for name in ("map.csv", "ucand.csv", "mcheck.json")],
        },
        "files_before_receipt": [
            record(path, path.name)
            for path in sorted(STAGE.iterdir(), key=lambda item: item.name)
            if path.is_file() and path.name != "R2_CHECK.json"
        ],
        "terminal_condition": {
            "foundation_nos_1_4_true_gaps": 0,
            "remaining_gaga_needs_review": 55,
            "next": "Integrate analytification, sheaf correspondence, and comparison proofs.",
        },
    }
    (STAGE / "R2_CHECK.json").write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    require(strict_json(STAGE / "R2_CHECK.json").get("status") == "STRICT_PASS", "R2 receipt reread failed")
    STAGE.rename(FINAL)
    result = {
        "status": "STRICT_PASS",
        "path": str(FINAL),
        "receipt": record(FINAL / "R2_CHECK.json", "gaga_r2/R2_CHECK.json"),
        "foundation_true_gaps": 0,
        "remaining_needs_review": 55,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
