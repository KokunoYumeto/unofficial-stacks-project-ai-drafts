#!/usr/bin/env python3
"""Append the confirmed p. 218 sequence-V typing issue without rewriting r19."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r19"
TARGET = ROOT / "tohoku_r20"
STAGE = ROOT / ".tohoku-r20-txn"
BASE_PATH = ROOT / "srcmap" / "build_tohoku_r19.py"
BASE_IDENTITY = (
    40547,
    "C2C2A1F8A58A86DDCF7D662073889C00F653620DB3E103717DC9B0879D894123",
)

GIT_NONCLAIM = {
    "inspection_performed": False,
    "reason": "Workspace machine-safety policy forbids repository-wide Git inspection.",
    "predecessor_receipt": {
        "path": "tohoku_r19/r19-check.json",
        "bytes": 15351,
        "sha256": "7A36482D9D549CF2FA613FF5CC30D17C9848C008705041979BB781F4BD9A4DF8",
    },
    "remote_server_freshness_verified": False,
}

EXPECTED_SOURCE = {
    "STATUS.md": (836, "A8BB15854CDE4873AF36ED436A0B258011C58ED0CDB6A6381A31C8D97D320AE7"),
    "cfg.json": (5193, "A82D62E531A1A951957375D4F535F6FDFD1BFC9953FEC9CAF1327216922AC395"),
    "check.json": (71262, "956A03E03411A3BED95DCB869EC89F6C5BBFA184A28A429B8DC4B0D0E671116A"),
    "dec.csv": (322185, "8052A9B92110463AC781FEF7CE773468925AA7DC5B2A4D873CBBA65CB63204DF"),
    "intake.json": (1877, "86273E19DB8A912BF9558DE007EF4A39C9C7FB93EBEA64A85D31A4F4A4BE42F2"),
    "issues.csv": (18227, "AABA123C53D04D9DF99FC693BFB3C21222973BB5194C16F4B48B9C90BDA2AA69"),
    "map.csv": (455434, "E728D857F5B5C7C4015499109C30D34BD371C3267926D4129FE865453EB5FA47"),
    "mcheck.json": (61091, "D9B836BAD11F29123EE8914A04498BB17BA5CF7D5EC6743388A3BC4AC1380D8C"),
    "r19-check.json": (15351, "7A36482D9D549CF2FA613FF5CC30D17C9848C008705041979BB781F4BD9A4DF8"),
    "stx.csv": (5259723, "7012998E449D3AB11A2938B6F2AF4D4849E7263F8B5AF6599323127B938DA8F9"),
    "tcand.csv": (472644, "804E6D3435C85F8E4857C684ADCEF18891D2F65B0E9A7F3EA66AD1C6F2941B60"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (391651, "E65D82E4B014B283485CAE6EFC4639E4275467BAEC0A45A15CB81759CA3D1040"),
}

ISSUE_ROW = {
    "issue_id": "I000023",
    "unit_id": "tohoku:spectral-sequence:v",
    "status": "confirmed",
    "kind": "source_coefficient_module_type_error",
    "claim": (
        "For a nontrivial action of G on R, the fixed subgroup N^G of a "
        "semilinear R-module is generally only an R^G-module, not an R-module. "
        "Consequently the printed claims that N^G is an injective R-module and "
        "that Ext_R^p(M,H^q(X;G,B)) is the initial term of sequence V are not "
        "typed at the stated generality."
    ),
    "evidence_labels": "cohomology-lemma-equivariant-ext-crossed-product-spectral-sequence",
    "evidence": (
        "Official Part II SHA-256 8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53, "
        "printed p. 218. Take R=k[t], G=C2 acting by t maps to -t, and the "
        "semilinear module N=R. Then N^G=k[t^2], which is not stable under "
        "multiplication by t and hence is not an R-submodule. The adjacent "
        "formalized sequence IV uses the correctly typed skew group ring U."
    ),
    "control": (
        "Preserve the printed formula diplomatically. Keep D000644 and D000651 "
        "open. During the translation phase, adjudicate either an added trivial "
        "G-action hypothesis on R or a corrected coefficient functor/ring, then "
        "create no-overwrite corrected source and semantic successors before any "
        "resolving mapping decision."
    ),
    "resolution_decision": "",
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


def load_base():
    if identity(BASE_PATH) != BASE_IDENTITY:
        raise RuntimeError("Frozen r19 builder identity drift")
    spec = importlib.util.spec_from_file_location("tohoku_r19_frozen", BASE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load frozen r19 builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASE = load_base()


def source_records() -> list[dict[str, object]]:
    return [BASE.record(SOURCE / name) for name in sorted(EXPECTED_SOURCE)]


def output_records(root: Path) -> list[dict[str, object]]:
    return [BASE.record(root / name) for name in sorted(PAYLOAD)]


def verify_source() -> None:
    BASE.require_plain_directory(SOURCE)
    names = {path.name for path in SOURCE.iterdir() if path.is_file()}
    if names != set(EXPECTED_SOURCE) or any(path.is_dir() for path in SOURCE.iterdir()):
        raise RuntimeError("r19 predecessor surface drift")
    for name, expected in EXPECTED_SOURCE.items():
        BASE.require_identity(SOURCE / name, expected)
    receipt = BASE.strict_json(SOURCE / "r19-check.json")
    if receipt.get("status") != "PASS" or receipt.get("errors") != []:
        raise RuntimeError("r19 predecessor receipt is not PASS")


def make_config() -> dict:
    cfg = BASE.strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r20"
    return cfg


def make_issues() -> bytes:
    fields, rows = BASE.load_csv(SOURCE / "issues.csv")
    if [row["issue_id"] for row in rows] != [f"I{number:06d}" for number in range(1, 23)]:
        raise RuntimeError("Predecessor source-issue sequence drift")
    appended = BASE.csv_bytes(fields, [ISSUE_ROW])
    return (SOURCE / "issues.csv").read_bytes() + appended[appended.index(b"\n") + 1 :]


def verify_deltas(root: Path) -> dict[str, object]:
    intake = BASE.strict_json(root / "intake.json")
    check = BASE.strict_json(root / "check.json")
    mcheck = BASE.strict_json(root / "mcheck.json")
    for name, receipt in (("intake", intake), ("scan", check), ("map", mcheck)):
        if receipt.get("status") != "PASS" or receipt.get("errors") != []:
            raise RuntimeError(f"{name} receipt is not PASS")
    if mcheck.get("outputs_promoted") is not True:
        raise RuntimeError("Mapping outputs were not promoted")

    expected_cfg = BASE.strict_json(SOURCE / "cfg.json")
    expected_cfg["dossier_id"] = "tohoku_r20"
    if BASE.strict_json(root / "cfg.json") != expected_cfg:
        raise RuntimeError("Configuration differs by more than dossier ID")
    for name in ("intake.json", "units.csv", "topics.csv", "dec.csv", "stx.csv", "tcand.csv", "tmap.csv", "map.csv", "ucand.csv"):
        if (root / name).read_bytes() != (SOURCE / name).read_bytes():
            raise RuntimeError(f"Unexpected ledger or scan drift: {name}")

    old_issues = (SOURCE / "issues.csv").read_bytes()
    new_issues = (root / "issues.csv").read_bytes()
    if not new_issues.startswith(old_issues):
        raise RuntimeError("Issue ledger is not an exact append-only successor")
    _, issues = BASE.load_csv(root / "issues.csv")
    if [row["issue_id"] for row in issues] != [f"I{number:06d}" for number in range(1, 24)]:
        raise RuntimeError("Issue sequence is not I000001..I000023")
    if issues[-1] != ISSUE_ROW:
        raise RuntimeError("I000023 differs from the frozen row")

    if check.get("tex_sha256") != BASE.strict_json(SOURCE / "check.json")["tex_sha256"]:
        raise RuntimeError("Stacks TeX scan identity drift")
    if check.get("counts") != BASE.strict_json(SOURCE / "check.json")["counts"]:
        raise RuntimeError("Stacks scan count drift")
    if check.get("warnings") != BASE.strict_json(SOURCE / "check.json")["warnings"]:
        raise RuntimeError("Stacks scan warning drift")

    old_counts = BASE.strict_json(SOURCE / "mcheck.json")["counts"]
    expected_counts = dict(old_counts)
    expected_counts["source_issues"] += 1
    expected_counts["active_source_issues"] += 1
    counts = mcheck.get("counts", {})
    if counts != expected_counts:
        raise RuntimeError(f"Mapping count drift: {counts}")
    return {
        "decision_delta": [],
        "source_issues": [ISSUE_ROW],
        "scan_counts": check["counts"],
        "mapping_counts": counts,
        "substantive_map_changes": [],
        "remaining_gap_class_dispositions": 112,
        "review_queue_units": 0,
        "candidate_units": 0,
    }


def receipt_payload(
    root: Path,
    attestation: dict[str, object],
    deltas: dict[str, object],
    build: dict[str, object] | None = None,
    execution: dict[str, object] | None = None,
) -> dict[str, object]:
    sources = source_records()
    semantic = [BASE.record(BASE.SEM / str(item["name"])) for item in BASE.sem_records()]
    return {
        "schema": "tohoku-stacks-source-issue-successor-r20-v1",
        "status": "PASS",
        "errors": [],
        "predecessor_dossier": {
            "name": "tohoku_r19",
            "files": sources,
            "file_count": len(sources),
            "bytes": sum(int(item["bytes"]) for item in sources),
            "aggregate_sha256": BASE.aggregate(sources),
        },
        "semantic_source": {
            "generation": "sem/r10",
            "files": semantic,
            "file_count": len(semantic),
            "bytes": sum(int(item["bytes"]) for item in semantic),
            "aggregate_sha256": BASE.aggregate(semantic),
            "sem_input": BASE.record(BASE.QA / "sem-input.json", "qa/v68r24/sem-input.json"),
            "sem_check": BASE.record(BASE.QA / "sem-check.json", "qa/v68r24/sem-check.json"),
        },
        "execution": execution if execution is not None else {
            "attestation": attestation,
            "bootstrap": BASE.record(ROOT / "srcmap" / "start_build_tohoku_r20.py"),
            "powershell_envelope": BASE.record(ROOT / "srcmap" / "start_build_tohoku_r20.ps1"),
            "frozen_r19_builder": BASE.record(BASE_PATH),
            "dependencies": {name: BASE.record(ROOT / name) for name in sorted(BASE.EXPECTED_TOOLS)},
            "contract": "same_bytes_bootstrap; exact fixed inputs locked against write/delete through generation replay and promotion",
        },
        "git": dict(GIT_NONCLAIM),
        "cohomology_build": BASE.verify_log() if build is None else build,
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": [
            "No Git command, commit, push, or remote-server freshness check is performed.",
            "No Stacks mathematical statement or mapping disposition changes in this issue-only successor.",
            "Sequence V remains open; no source repair or unstated coefficient hypothesis is adopted.",
            "All 990 source units retain reviewed dispositions; the mapper has zero review and candidate queues.",
            "The 112 residual gap-class dispositions are explicit scope results, not undecided rows.",
            "No release, publication, upload, DOI, rights, or whole-paper gate is closed by this receipt.",
        ],
    }


def lock_paths(fresh: bool) -> list[Path]:
    paths = [
        Path(__file__), BASE_PATH,
        ROOT / "srcmap" / "start_build_tohoku_r20.py",
        ROOT / "srcmap" / "start_build_tohoku_r20.ps1",
        *[SOURCE / name for name in EXPECTED_SOURCE],
        *BASE.lock_paths(fresh),
    ]
    if not fresh and TARGET.exists():
        paths.extend(path for path in TARGET.iterdir() if path.is_file())
    unique: dict[str, Path] = {}
    for path in paths:
        unique[str(path)] = path
    return list(unique.values())


def verify_attestation() -> dict[str, object]:
    attestation = globals().get("EXECUTION_ATTESTATION")
    if not isinstance(attestation, dict):
        raise RuntimeError("Run through start_build_tohoku_r20.py")
    builder = attestation.get("builder")
    if not isinstance(builder, dict) or identity(Path(__file__)) != (
        builder.get("bytes"), builder.get("sha256")
    ):
        raise RuntimeError("Same-bytes builder attestation drift")
    return attestation


def verify_existing(attestation: dict[str, object]) -> dict[str, object]:
    BASE.require_plain_directory(TARGET)
    names = {path.name for path in TARGET.iterdir() if path.is_file()}
    if names != PAYLOAD | {"r20-check.json"} or any(path.is_dir() for path in TARGET.iterdir()):
        raise RuntimeError("Existing r20 dossier surface drift")
    deltas = verify_deltas(TARGET)
    receipt = BASE.strict_json(TARGET / "r20-check.json")
    build = receipt.get("cohomology_build")
    execution = receipt.get("execution")
    if not isinstance(build, dict) or not isinstance(execution, dict):
        raise RuntimeError("Existing r20 receipt is malformed")
    expected_build = {
        "tex": {"name": "cohomology.tex", "bytes": 788892, "sha256": "82FDAE359BED05E263D28CBE0E4DA5089E4F5EB9F0F126B6A37060FF83403180"},
        "log": {"name": "cohomology.log", "bytes": 47266, "sha256": "CC996E7A5F7ADCBAADF8CFF50D29F079F418ADFAF24E7F2A8B6CE98BC598F944"},
        "pdf": {"name": "cohomology.pdf", "bytes": 1786462, "sha256": "F0A5BC1BB4F4A3FA521D2E59D7B737D52E0AF67C7546D7CEDF0B2B5916E43EE5"},
        "pdf_pages": 205,
        "undefined_references": 0,
        "undefined_citations": 0,
        "rerun_notices": 0,
        "new_block_overfull_boxes": 0,
        "visual_reviewed_pages": [168, 169, 170, 171],
    }
    if build != expected_build:
        raise RuntimeError("Existing r20 build receipt drift")
    expected_execution = {
        "attestation": attestation,
        "bootstrap": BASE.record(ROOT / "srcmap" / "start_build_tohoku_r20.py"),
        "powershell_envelope": BASE.record(ROOT / "srcmap" / "start_build_tohoku_r20.ps1"),
        "frozen_r19_builder": {"name": "build_tohoku_r19.py", "bytes": BASE_IDENTITY[0], "sha256": BASE_IDENTITY[1]},
        "dependencies": {
            name: {"name": Path(name).name, "bytes": expected[0], "sha256": expected[1]}
            for name, expected in sorted(BASE.EXPECTED_TOOLS.items())
        },
        "contract": "same_bytes_bootstrap; exact fixed inputs locked against write/delete through generation replay and promotion",
    }
    if execution != expected_execution:
        raise RuntimeError("Existing r20 execution receipt drift")
    expected = receipt_payload(TARGET, attestation, deltas, build, execution)
    if receipt != expected:
        raise RuntimeError("Existing r20 receipt replay mismatch")
    return receipt


def main_locked(attestation: dict[str, object]) -> int:
    if TARGET.exists() and STAGE.exists():
        raise RuntimeError("Target and unresolved transaction coexist")
    fresh = not TARGET.exists()
    with BASE.deny_write_delete(lock_paths(fresh)):
        verify_source()
        BASE.verify_inputs(fresh)
        if TARGET.exists():
            print(json.dumps(verify_existing(attestation), ensure_ascii=False, indent=2))
            return 0
        if STAGE.exists():
            raise FileExistsError(f"Unresolved transaction exists: {STAGE}")
        STAGE.mkdir()
        BASE.exclusive_write(STAGE / "cfg.json", BASE.json_bytes(make_config()))
        BASE.exclusive_write(STAGE / "topics.csv", (SOURCE / "topics.csv").read_bytes())
        BASE.exclusive_write(STAGE / "dec.csv", (SOURCE / "dec.csv").read_bytes())
        BASE.exclusive_write(STAGE / "issues.csv", make_issues())
        BASE.run_tool("intake.py", str(STAGE), str(BASE.SEM / "nodes.csv"), *BASE.intake_args())
        BASE.run_tool("scan.py", str(STAGE))
        BASE.run_tool("map.py", str(STAGE))
        deltas = verify_deltas(STAGE)
        status = (
            "# Tohoku Stacks mapping status\n\n"
            "- Semantic source: sealed local-unpublished `sem/r10`.\n"
            "- Stable source inventory: 990 units; review and candidate queues: zero.\n"
            "- Decisions D000001--D000941 and all mapping dispositions are byte-identical to `tohoku_r19`.\n"
            "- Confirmed issue I000023 records the coefficient-module type error in p. 218 sequence V; D000644 and D000651 remain open.\n"
            "- The bounded crosswalk has 112 explicit residual gap-class dispositions and no undecided row.\n"
            "- This local checkpoint makes no Git, release, publication, remote-freshness, DOI, rights, or whole-paper claim.\n"
        ).encode("utf-8")
        BASE.exclusive_write(STAGE / "STATUS.md", status)
        receipt = receipt_payload(STAGE, attestation, deltas)
        BASE.exclusive_write(STAGE / "r20-check.json", BASE.json_bytes(receipt))
        if (
            {path.name for path in STAGE.iterdir() if path.is_file()}
            != PAYLOAD | {"r20-check.json"}
            or any(path.is_dir() for path in STAGE.iterdir())
        ):
            raise RuntimeError("Staged dossier surface mismatch")
        verify_source()
        BASE.verify_inputs(True)
        os.rename(STAGE, TARGET)
        with BASE.deny_write_delete([path for path in TARGET.iterdir() if path.is_file()]):
            final = verify_existing(attestation)
        print(json.dumps(final, ensure_ascii=False, indent=2))
        return 0


def main() -> int:
    attestation = verify_attestation()
    with BASE.single_writer_mutex():
        return main_locked(attestation)


if __name__ == "__main__":
    raise SystemExit(main())
