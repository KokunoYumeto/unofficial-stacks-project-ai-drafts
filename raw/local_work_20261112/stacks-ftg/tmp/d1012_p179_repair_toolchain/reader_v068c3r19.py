#!/usr/bin/env python3
"""Frozen no-overwrite v068c3r19 reader builder for D1012-R001.

This script composes the sealed v068c3r18 transaction engine in memory and
changes exactly fr/p179.tex and en/p179.tex in a new staged source tree.  It
does not mutate production/p179_r1, v068c3r18, or prior PDFs.  Execution is
possible only through the hash-verifying local runner and an explicit
``--execute`` flag.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import secrets
import sys
import types
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence


ROOT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SCRIPT = Path(__file__).resolve(strict=True)
BASE_BUILDER = ROOT / "tools" / "build68r18.py"
BASE_BUILDER_EXPECTED = (30_417, "A83714697971089C45AB86E981892B585A3F5DA3712184C0D92D6D7DD0E056B2")
PREDECESSOR_REVISION = "v068c3r18"
REVISION = "v068c3r19"
GATE = ROOT / "build" / REVISION
STAGED_SOURCE = GATE / "src"
RECEIPT = GATE / "build.json"
OUTPUT_ROOT = ROOT / "output" / "pdf"
FINAL_OUTPUTS = {
    "fr": OUTPUT_ROOT / f"fr-p119-221-{REVISION}.pdf",
    "en": OUTPUT_ROOT / f"en-p119-221-{REVISION}.pdf",
}
PREDECESSOR_RECEIPT = ROOT / "build" / PREDECESSOR_REVISION / "build.json"
PREDECESSOR_RECEIPT_EXPECTED = (32_685, "287CF9B793BE34598878AD63546B081C27ACEE10C722AF82FBDE03251C92EADB")
PREDECESSOR_QA = ROOT / "qa" / "v68r40" / "check.json"
PREDECESSOR_QA_EXPECTED = (10_374, "9969A37D8CDDE716A29C03EF268C5394A13F967BD4C706A0EB8F59CA9695769F")
PREDECESSOR_QA_STRUCTURAL = ROOT / "qa" / "v68r40" / "structural.json"
PREDECESSOR_QA_STRUCTURAL_EXPECTED = (13_015, "352C82546CA0E6110267718F5DCC413CCC5099C70B7ACFD4764A2A8EAD664A00")
PREDECESSOR_SOURCE = ROOT / "build" / PREDECESSOR_REVISION / "src"
PREDECESSOR_MANIFEST = (543, 11_855_901, 62_845, "F69327761FFFD393108E352EB8C7E86C7C992720FF20E703BBE6EAB990CFAE6E")
SUCCESSOR_MANIFEST = (543, 11_855_958, 62_845, "D49CC85CF58B08E28A73C71D7A868559AB0B8F6454763BF69861FDAEB7DB8944")
PREDECESSOR_PDFS = {
    "fr": (ROOT / "output" / "pdf" / "fr-p119-221-v068c3r18.pdf", 1_417_469, "24EA55FFA0CA94CBD089053B5A0BA2495E2553F798561DB059E77D4F6F724429", 94),
    "en": (ROOT / "output" / "pdf" / "en-p119-221-v068c3r18.pdf", 1_381_057, "58A7F14A50D92CA0EAF9EEC04CE3399D4282144FF618C4887318C962CC9A5DB9", 90),
}
P179_ROOT = ROOT / "production" / "p179_fix2"
P179_RECEIPT = P179_ROOT / "check.json"
P179_RECEIPT_EXPECTED = (4_425, "61AD974EC36B4FB525643EEABF7E12F57AC3FB2B80D7267D32DDCC83035D1D27")
P179_FILES: dict[str, tuple[Path, int, str]] = {
    "decisions": (P179_ROOT / "decisions.jsonl", 3_863, "4B32C9521442CE2330068147C20ACE804A3D3C097E91FB83F02D501556D0200C"),
    "targets": (P179_ROOT / "targets.csv", 775, "A422666287FED6B65180FB6FC41B82E7B6850961741E7BA47014C4AAAC6CBAFF"),
    "reuse": (P179_ROOT / "reuse.txt", 19, "C7BD41655D1420B139B0D69E6AA385AA8BDB6800FB99CB71BC16E6A98118B4BD"),
    "dip": (P179_ROOT / "tex" / "fr_diplomatic" / "p179.tex", 4_413, "3B4424E98669777F4352A6911DA83D6391DD1412F79FE9C5EE77B8172DB75182"),
    "fr": (P179_ROOT / "tex" / "fr_corrected" / "p179.tex", 4_375, "27C6C84EEE0B74133B6376453801DF451B892FF782B7AC09E72146C4A7834C48"),
    "en": (P179_ROOT / "tex" / "en" / "p179.tex", 4_173, "A7491524DBAC64EA345B36384DE39F503A2F4680B995779DEB826D7C21443D73"),
}
SOURCE_LEDGER = ROOT / "SOURCE_CORRECTIONS.jsonl"
SOURCE_LEDGER_EXPECTED = (211_141, "94F39C3058F24A0E8E43B3D3D98679C4EF265C23873ACE2B075F23F8810C262B")
P179_PREDECESSOR = {
    "dip/p179.tex": (4_413, "3B4424E98669777F4352A6911DA83D6391DD1412F79FE9C5EE77B8172DB75182"),
    "fr/p179.tex": (4_347, "C3B0470AC85B9A34A0DFAAF5A0325690756C7FB541B12421CC651A29C7410CC7"),
    "en/p179.tex": (4_144, "3CD9D83B12C0B48B94577F0BBDA2E632B8E6EE8E7778B1B9442D5054D8505FE1"),
}
REPLACEMENT_TARGETS = {"en/p179.tex": "en", "fr/p179.tex": "fr"}
MASTERS = {
    "fr": ("main-fr.tex", 3_240, "45C11EE2DBA372D0485FE2FFEFA104DC4F7BE75752600B7384A1C33A23261D3B", 94),
    "en": ("main-en.tex", 3_210, "37D0BDB5989439C90298854B36DCD3534F78EED900E3B94E9919FC72B1936C1F", 90),
}
snapshot_record = globals().get("__verified_script_snapshot__")


class ReaderError(RuntimeError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def exact(path: Path, expected: tuple[int, str], label: str) -> bytes:
    if not path.is_file() or path.is_symlink() or path.resolve(strict=True) != path:
        raise ReaderError(f"{label}: missing, non-regular, symlinked, or redirected")
    data = path.read_bytes()
    if (len(data), digest(data)) != expected:
        raise ReaderError(f"{label}: identity drifted: {(len(data), digest(data))}")
    return data


def parse_json(data: bytes, label: str) -> dict[str, Any]:
    value = json.loads(data.decode("utf-8", errors="strict"))
    if not isinstance(value, dict):
        raise ReaderError(f"{label}: JSON root is not an object")
    return value


def require_snapshot() -> dict[str, Any]:
    record = snapshot_record
    if not isinstance(record, dict) or set(record) != {"path", "bytes", "sha256", "contract"}:
        raise ReaderError("launch through run.py; verified script snapshot is absent")
    live = SCRIPT.read_bytes()
    if (
        record["path"] != str(SCRIPT)
        or record["contract"] != "contract_json_read_hash_then_exec_same_bytes"
        or (len(live), digest(live)) != (record["bytes"], record["sha256"])
    ):
        raise ReaderError("verified script snapshot drifted")
    return dict(record)


def load_engine() -> tuple[Any, dict[str, Any]]:
    payload = exact(BASE_BUILDER, BASE_BUILDER_EXPECTED, "sealed build68r18.py")
    module = types.ModuleType("__verified_build68r18_base__")
    module.__file__ = str(BASE_BUILDER)
    module.__package__ = None
    exec(compile(payload, str(BASE_BUILDER), "exec", dont_inherit=True), module.__dict__)
    engine = module.engine
    for name, value in {
        "REVISION": REVISION,
        "PREDECESSOR_REVISION": PREDECESSOR_REVISION,
        "GATE": GATE,
        "STAGED_SOURCE": STAGED_SOURCE,
        "RECEIPT": RECEIPT,
        "OUTPUT_ROOT": OUTPUT_ROOT,
        "FINAL_OUTPUTS": FINAL_OUTPUTS,
        "PREDECESSOR_SOURCE": PREDECESSOR_SOURCE,
        "PREDECESSOR_MANIFEST": PREDECESSOR_MANIFEST,
        "SUCCESSOR_MANIFEST": SUCCESSOR_MANIFEST,
        "REPLACEMENT_TARGETS": REPLACEMENT_TARGETS,
        "MASTERS": MASTERS,
    }.items():
        setattr(engine, name, value)
    engine.compiled_paths.clear()
    engine.compiled_records.clear()
    engine.promotion_stages.clear()
    engine.promoted_languages = []
    engine.final_locks.clear()
    engine.receipt_committed = False
    return engine, {
        "path": str(BASE_BUILDER),
        "bytes": len(payload),
        "sha256": digest(payload),
        "contract": "read_hash_then_exec_same_bytes_as_nested_transaction_engine",
    }


def validate_predecessor(receipt: Mapping[str, Any], qa: Mapping[str, Any], structural: Mapping[str, Any]) -> None:
    if (
        receipt.get("schema") != "tohoku-v068-staged-successor-build-v1"
        or receipt.get("revision") != PREDECESSOR_REVISION
        or receipt.get("predecessor_revision") != "v068c3r17"
        or receipt.get("status") != "PASS"
        or receipt.get("errors") != []
        or receipt.get("compile_order") != ["fr", "en"]
        or receipt.get("passes_per_language") != 2
        or receipt.get("shell") is not False
    ):
        raise ReaderError("sealed r18 build receipt semantics drifted")
    verification = receipt.get("staged_source_verification", {})
    if tuple(verification.get(key) for key in ("rows", "total_file_bytes", "bytes", "sha256")) != PREDECESSOR_MANIFEST:
        raise ReaderError("sealed r18 staged-source receipt drifted")
    surface = receipt.get("revision_surface_contract", {})
    if surface.get("replaced_staged_paths") != ["en/p220.tex", "fr/p220.tex"] or surface.get("other_staged_source_changes") != 0:
        raise ReaderError("sealed r18 revision surface drifted")
    if (
        qa.get("schema") != "tohoku-v068-reader-independent-qa-v1"
        or qa.get("qa_revision") != "v68r40"
        or qa.get("reader_revision") != PREDECESSOR_REVISION
        or qa.get("status") != "PASS"
        or qa.get("errors") != []
        or qa.get("conclusion", {}).get("reader_successor_accepted") is not True
        or qa.get("conclusion", {}).get("visual_review_accepted") is not True
    ):
        raise ReaderError("sealed v68r40 QA semantics drifted")
    if (
        structural.get("schema") != "tohoku-v068-reader-independent-qa-prepare-v40"
        or structural.get("reader_revision") != PREDECESSOR_REVISION
        or structural.get("status") != "STRUCTURAL_PASS_VISUAL_PENDING"
        or structural.get("errors") != []
    ):
        raise ReaderError("sealed v68r40 structural QA semantics drifted")


def preflight(engine: Any, script_identity: Mapping[str, Any], base_identity: Mapping[str, Any]) -> dict[str, Any]:
    predecessor_receipt_data = exact(PREDECESSOR_RECEIPT, PREDECESSOR_RECEIPT_EXPECTED, "v068c3r18 build receipt")
    predecessor_qa_data = exact(PREDECESSOR_QA, PREDECESSOR_QA_EXPECTED, "v68r40 QA receipt")
    predecessor_structural_data = exact(PREDECESSOR_QA_STRUCTURAL, PREDECESSOR_QA_STRUCTURAL_EXPECTED, "v68r40 structural receipt")
    validate_predecessor(
        parse_json(predecessor_receipt_data, "r18 build receipt"),
        parse_json(predecessor_qa_data, "v68r40 QA receipt"),
        parse_json(predecessor_structural_data, "v68r40 structural receipt"),
    )
    predecessor_pdf_records: dict[str, Any] = {}
    for language, (path, size, sha256, pages) in PREDECESSOR_PDFS.items():
        data = exact(path, (size, sha256), f"r18 {language} PDF")
        predecessor_pdf_records[language] = {"path": path.relative_to(ROOT).as_posix(), "bytes": len(data), "sha256": digest(data), "pages": pages}

    admission_data = exact(P179_RECEIPT, P179_RECEIPT_EXPECTED, "p179_fix2 receipt")
    admission = parse_json(admission_data, "p179_fix2 receipt")
    if (
        admission.get("schema") != "tohoku-p179-cross-cover-trace-source-admission-v1"
        or admission.get("status") != "PASS"
        or admission.get("errors") != []
        or admission.get("decision_id") != "TOH-P179-COR-002"
        or admission.get("source_correction_id") != "TOH-SRC-P179-009"
        or admission.get("production_successor") != "production/p179_fix2"
    ):
        raise ReaderError("p179_fix2 receipt semantics drifted")
    p179_payloads = {name: exact(path, (size, sha), f"p179_fix2 {name}") for name, (path, size, sha) in P179_FILES.items()}
    ledger_data = exact(SOURCE_LEDGER, SOURCE_LEDGER_EXPECTED, "source correction ledger postimage")
    if ledger_data.count(b'"decision_id":"TOH-SRC-P179-009"') != 1 or b'"layer":"fr_corrected;en"' not in ledger_data:
        raise ReaderError("root ledger D1012-R001 row surface drifted")

    predecessor_payloads, predecessor_manifest = engine.snapshot_predecessor_tree()
    if tuple(predecessor_manifest[key] for key in ("rows", "total_file_bytes", "bytes", "sha256")) != PREDECESSOR_MANIFEST:
        raise ReaderError("live r18 staged-source manifest drifted")
    for name, expected in P179_PREDECESSOR.items():
        data = predecessor_payloads.get(name)
        if data is None or (len(data), digest(data)) != expected:
            raise ReaderError(f"r18 p179 staged preimage drifted: {name}")
    if predecessor_payloads["dip/p179.tex"] != p179_payloads["dip"]:
        raise ReaderError("p179 diplomatic layer is not byte-identical")
    successor_payloads = dict(predecessor_payloads)
    successor_payloads["fr/p179.tex"] = p179_payloads["fr"]
    successor_payloads["en/p179.tex"] = p179_payloads["en"]
    successor_manifest = engine.manifest_record(successor_payloads)
    if tuple(successor_manifest[key] for key in ("rows", "total_file_bytes", "bytes", "sha256")) != SUCCESSOR_MANIFEST:
        raise ReaderError(f"derived r19 staged-source manifest drifted: {successor_manifest}")
    changed: list[dict[str, Any]] = []
    for name in sorted(predecessor_payloads):
        before, after = predecessor_payloads[name], successor_payloads[name]
        if before != after:
            changed.append({
                "path": name,
                "predecessor_bytes": len(before),
                "predecessor_sha256": digest(before),
                "successor_bytes": len(after),
                "successor_sha256": digest(after),
            })
    if [row["path"] for row in changed] != ["en/p179.tex", "fr/p179.tex"]:
        raise ReaderError(f"derived r19 source delta is not exact: {changed}")
    return {
        "_successor_payloads": successor_payloads,
        "toolchain_script": dict(script_identity),
        "nested_transaction_engine": dict(base_identity),
        "predecessor_build_receipt": {"path": PREDECESSOR_RECEIPT.relative_to(ROOT).as_posix(), "bytes": len(predecessor_receipt_data), "sha256": digest(predecessor_receipt_data)},
        "predecessor_qa_receipt": {"path": PREDECESSOR_QA.relative_to(ROOT).as_posix(), "bytes": len(predecessor_qa_data), "sha256": digest(predecessor_qa_data)},
        "predecessor_structural_receipt": {"path": PREDECESSOR_QA_STRUCTURAL.relative_to(ROOT).as_posix(), "bytes": len(predecessor_structural_data), "sha256": digest(predecessor_structural_data)},
        "predecessor_pdfs": predecessor_pdf_records,
        "source_admission": {"path": P179_RECEIPT.relative_to(ROOT).as_posix(), "bytes": len(admission_data), "sha256": digest(admission_data)},
        "source_admission_files": {name: {"path": path.relative_to(ROOT).as_posix(), "bytes": size, "sha256": sha} for name, (path, size, sha) in P179_FILES.items()},
        "source_corrections_ledger": {"path": SOURCE_LEDGER.relative_to(ROOT).as_posix(), "bytes": len(ledger_data), "sha256": digest(ledger_data)},
        "source_transition": {
            "predecessor": predecessor_manifest,
            "successor": successor_manifest,
            "changed_files": changed,
            "changed_file_count": 2,
            "byte_identical_file_count": 541,
            "only_changed_printed_page": 179,
            "selected_source_successor": "production/p179_fix2",
            "diplomatic_p179_byte_identical": True,
            "p178_p179_p180_target_and_seam_gate": "PASS_FROM_SOURCE_ADMISSION",
        },
        "pypdf": engine.pypdf_role(),
    }


def preflight_namespace(engine: Any, pdflatex_argument: str) -> Path:
    if os.name != "nt":
        raise ReaderError("r19 no-overwrite promotion requires Windows semantics")
    executable = Path(pdflatex_argument)
    if not executable.is_absolute() or executable.resolve(strict=True) != engine.PDFLATEX:
        raise ReaderError("--pdflatex is not the exact admitted absolute path")
    if os.path.lexists(GATE) or any(os.path.lexists(path) for path in FINAL_OUTPUTS.values()):
        raise FileExistsError("r19 gate or a revision-named final already exists")
    for parent in (GATE.parent, OUTPUT_ROOT):
        if not parent.is_dir() or parent.is_symlink():
            raise ReaderError(f"required ordinary parent is invalid: {parent}")
    return executable


def create_staged_source(engine: Any, payloads: Mapping[str, bytes]) -> dict[str, Any]:
    GATE.mkdir(parents=False, exist_ok=False)
    engine.hold(GATE, directory=True)
    owner = GATE / ".build68r19-owner.json"
    owner_payload = (json.dumps({"schema": "tohoku-build68r19-owner-v1", "revision": REVISION, "token": secrets.token_hex(32).upper()}, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    with owner.open("xb") as output:
        output.write(owner_payload)
        output.flush()
        os.fsync(output.fileno())
    engine.lock_and_require(owner, (len(owner_payload), digest(owner_payload)), "r19 owner")
    STAGED_SOURCE.mkdir(exist_ok=False)
    engine.hold(STAGED_SOURCE, directory=True)
    directories: set[PurePosixPath] = set()
    for name in payloads:
        member = PurePosixPath(name)
        if member.is_absolute() or ".." in member.parts or member.as_posix() != name:
            raise ReaderError(f"unsafe staged member: {name}")
        for index in range(1, len(member.parts)):
            directories.add(PurePosixPath(*member.parts[:index]))
    for member in sorted(directories, key=lambda item: (len(item.parts), item.as_posix())):
        path = STAGED_SOURCE.joinpath(*member.parts)
        path.mkdir(exist_ok=False)
        engine.hold(path, directory=True)
    for name in sorted(payloads):
        path = STAGED_SOURCE.joinpath(*PurePosixPath(name).parts)
        data = payloads[name]
        with path.open("xb") as output:
            output.write(data)
            output.flush()
            os.fsync(output.fileno())
        engine.staged_file_locks[name] = engine.lock_and_require(path, (len(data), digest(data)), f"staged {name}")
    verification = engine.verify_staged_source(dict(payloads))
    return {
        "owner_marker": {"path": owner.relative_to(ROOT).as_posix(), "bytes": len(owner_payload), "sha256": digest(owner_payload), "exclusive_create": True},
        "staged_source": verification,
    }


def commit_receipt(engine: Any, value: Mapping[str, Any]) -> dict[str, Any]:
    data = (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    stage = RECEIPT.with_name(".build.json.r19.stage")
    if os.path.lexists(RECEIPT) or os.path.lexists(stage):
        raise FileExistsError("r19 receipt or sibling stage exists")
    with stage.open("xb") as output:
        output.write(data)
        output.flush()
        os.fsync(output.fileno())
    handle = engine.open_locked_path(stage, directory=False, allow_delete_share=True)
    engine.all_locks.append(handle)
    try:
        if engine.read_locked_file(handle) != data:
            raise ReaderError("r19 receipt-stage readback differs")
        engine.move_no_replace(stage, RECEIPT)
        engine.receipt_committed = True
    finally:
        engine.release_handle(handle)
    final = engine.lock_and_require(RECEIPT, (len(data), digest(data)), "committed r19 receipt")
    if engine.read_locked_file(final) != data:
        raise ReaderError("committed r19 receipt readback differs")
    return {"path": str(RECEIPT), "bytes": len(data), "sha256": digest(data), "status": "PASS"}


def execute_build(engine: Any, inputs: dict[str, Any], executable: Path, pdflatex_record: Mapping[str, Any]) -> dict[str, Any]:
    payloads = inputs.pop("_successor_payloads")
    stage = create_staged_source(engine, payloads)
    compile_evidence = {language: engine.compile_language(language, executable) for language in ("fr", "en")}
    after_compile = engine.verify_staged_source(payloads)
    if after_compile != stage["staged_source"]:
        raise ReaderError("staged source manifest changed during compilation")
    finals, promotion = engine.promote_outputs()
    value = {
        "schema": "tohoku-v068-staged-successor-build-v1",
        "revision": REVISION,
        "predecessor_revision": PREDECESSOR_REVISION,
        "created_utc": engine.datetime.now(engine.timezone.utc).isoformat().replace("+00:00", "Z"),
        "status": "PASS",
        "errors": [],
        "compile_order": ["fr", "en"],
        "passes_per_language": 2,
        "shell": False,
        "input_snapshots": inputs,
        "gate_ownership": stage["owner_marker"],
        "staged_source_verification": after_compile,
        "pdflatex": dict(pdflatex_record),
        "compile_evidence": compile_evidence,
        "pdfs": finals,
        "promotion": promotion,
        "revision_surface_contract": {
            "predecessor_staged_files": 543,
            "successor_staged_files": 543,
            "byte_identical_staged_files": 541,
            "replaced_staged_paths": ["en/p179.tex", "fr/p179.tex"],
            "other_staged_source_changes": 0,
            "selected_source_successor": "production/p179_fix2",
            "diplomatic_p179_byte_identical": True,
            "target_gate": "build/v068c3r19",
            "final_outputs": ["output/pdf/fr-p119-221-v068c3r19.pdf", "output/pdf/en-p119-221-v068c3r19.pdf"],
        },
        "expected_reader_pages": {"fr": 94, "en": 90},
        "downstream_binding_gate": {
            "status": "REQUIRES_EXPLICIT_POST_BUILD_IDENTITIES",
            "required_file": "tmp/d1012_p179_repair_toolchain/r19_output_bindings.json",
            "reason": "v68r41 and sem/r20 must bind the actual receipt and final PDF identities after this deterministic build; they may not infer or guess future hashes.",
        },
        "external_constraints": {
            "github": {"status": "temporarily_unavailable", "effect": "No GitHub inspection, synchronization, push, or publication is attempted."}
        },
        "qualifications": [
            "The earlier goal-level PDF artifact-operation marker has already been run exactly once; this transaction must not run it again.",
            "Each revision-named final is promoted by an atomic same-directory no-replace move; the build receipt commits only after both final readbacks.",
            "The exact pdflatex executable is identity-locked; TeX packages, fonts, DLLs, configuration, and child runtime remain external runtime dependencies.",
            "No prior source, build, QA, PDF, semantic generation, mapping generation, Git state, or GitHub state is mutated.",
        ],
    }
    receipt_record = commit_receipt(engine, value)
    return {"status": "PASS", "build_receipt": receipt_record, "pdfs": finals, "post_build_binding_gate": value["downstream_binding_gate"]}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Preflight or build exact no-overwrite Tohoku bilingual reader v068c3r19.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preflight", action="store_true")
    group.add_argument("--execute", action="store_true")
    parser.add_argument("--pdflatex", required=True)
    args = parser.parse_args(sys.argv[1:] if argv is None else list(argv))
    script_identity = require_snapshot()
    engine, base_identity = load_engine()
    inputs = preflight(engine, script_identity, base_identity)
    executable = preflight_namespace(engine, args.pdflatex)
    if args.preflight:
        result = {
            "status": "READY_NOT_EXECUTED",
            "revision": REVISION,
            "source_transition": inputs["source_transition"],
            "intended_outputs": [str(GATE), *(str(path) for path in FINAL_OUTPUTS.values())],
            "future_identity_gate": "r19_output_bindings.json remains PENDING until a real build exists",
        }
    else:
        engine.lock_workspace()
        pdflatex_record = engine.acquire_pdflatex_lock(executable)
        try:
            result = execute_build(engine, inputs, executable, pdflatex_record)
        except BaseException:
            engine.rollback_uncommitted_outputs()
            raise
        finally:
            errors = engine.close_handles(engine.all_locks)
            if errors:
                print("PROCESS-EXIT HANDLE-CLOSE WARNING: " + ";".join(errors), file=sys.stderr)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise SystemExit(1)
