#!/usr/bin/env python3
"""Frozen no-overwrite v068c3r20 reader builder for D1017-R001.

This script composes the sealed build transaction engine in memory and changes
exactly fr/p185.tex and en/p185.tex in a new staged source tree.  It does not
mutate production/p185_r1, v068c3r19, or prior PDFs.  Execution is
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
PREDECESSOR_REVISION = "v068c3r19"
REVISION = "v068c3r20"
GATE = ROOT / "build" / REVISION
STAGED_SOURCE = GATE / "src"
RECEIPT = GATE / "build.json"
OUTPUT_ROOT = ROOT / "output" / "pdf"
FINAL_OUTPUTS = {
    "fr": OUTPUT_ROOT / f"fr-p119-221-{REVISION}.pdf",
    "en": OUTPUT_ROOT / f"en-p119-221-{REVISION}.pdf",
}
PREDECESSOR_RECEIPT = ROOT / "build" / PREDECESSOR_REVISION / "build.json"
PREDECESSOR_RECEIPT_EXPECTED = (22_218, "F31B4D90398DD35783CFF6178305F331F64976EC242135EE1BA933093635608F")
PREDECESSOR_QA = ROOT / "qa" / "v68r41" / "check.json"
PREDECESSOR_QA_EXPECTED = (4_745, "7153FAF431F3767F8C2E581745FD9E90ECD253B8C7B8369F3D9C46DB52B8DC5D")
PREDECESSOR_QA_STRUCTURAL = ROOT / "qa" / "v68r41" / "structural.json"
PREDECESSOR_QA_STRUCTURAL_EXPECTED = (7_900, "9DE87B78D032449E996FA6527E7794501E2E41F0B27194DCC17ED6E75FEE4E5E")
PREDECESSOR_SOURCE = ROOT / "build" / PREDECESSOR_REVISION / "src"
PREDECESSOR_MANIFEST = (543, 11_855_958, 62_845, "D49CC85CF58B08E28A73C71D7A868559AB0B8F6454763BF69861FDAEB7DB8944")
SUCCESSOR_MANIFEST = (543, 11_855_949, 62_845, "52559D18F2A77C82A3BBAB69E4949C3A17C7DA1593034719F5B72584E9540310")
PREDECESSOR_PDFS = {
    "fr": (ROOT / "output" / "pdf" / "fr-p119-221-v068c3r19.pdf", 1_417_542, "C2BB5BAC3D9641076A906379D4F7AC3C6A12C37C5877C63387B8C9443D6C74DA", 94),
    "en": (ROOT / "output" / "pdf" / "en-p119-221-v068c3r19.pdf", 1_381_116, "A7B12B68566D4B2B5DA90DF64C8972D2A80A38EE7BB341E13DC77B75FFD51E96", 90),
}
P185_ROOT = ROOT / "production" / "p185_fix2"
P185_RECEIPT = P185_ROOT / "check.json"
P185_RECEIPT_EXPECTED = (5_291, "E54AE998A9D8AB863652521E329731789727DD064B48E6A52CAB83584C802EEA")
P185_FILES: dict[str, tuple[Path, int, str]] = {
    "decisions": (P185_ROOT / "decisions.jsonl", 3_493, "BB7813EA38AD72B878C4AE825141A82FEF092F8A99FEDDD7397AE705A56D4D4B"),
    "targets": (P185_ROOT / "targets.csv", 735, "1E9B7D440E52EC56F1BB64563B8A1243556E25CAE8083F24FC5BF08EDF8832BF"),
    "reuse": (P185_ROOT / "reuse.txt", 37, "E18934ADECB524EE2605B24D065861B042487811117719A3CD7B919CE5CCE06A"),
    "dip": (P185_ROOT / "tex" / "fr_diplomatic" / "p185.tex", 3_964, "C95797FF736C53A873F08DC7124460F7EE7E50E5490C656E8F5F6493A784153A"),
    "fr": (P185_ROOT / "tex" / "fr_corrected" / "p185.tex", 4_298, "EBE37CBFBE00FA4CA72C21CC4C542D60603A61E92EE446D15C941FA136B20847"),
    "en": (P185_ROOT / "tex" / "en" / "p185.tex", 4_178, "9F3F8C932149B3F2ECC9A25C4D4C2D010A48A2CFE6B621CE12BE178CC4DADE60"),
}
SOURCE_LEDGER = ROOT / "SOURCE_CORRECTIONS.jsonl"
SOURCE_LEDGER_EXPECTED = (212_239, "31E8894E57B355383B49BB403FAE65B935C81B4C1DAC65C17B20C3C7A6E70439")
P185_PREDECESSOR = {
    "dip/p185.tex": (3_964, "C95797FF736C53A873F08DC7124460F7EE7E50E5490C656E8F5F6493A784153A"),
    "fr/p185.tex": (4_302, "85D04A11FF28F109C9006A850A3D9176A6483C2CAC56AA9B849058934B65C54A"),
    "en/p185.tex": (4_183, "6D15A561E5FCE6D3071672663DE9969249A5D147F08D6DC61A7CD5F3E43A084D"),
}
REPLACEMENT_TARGETS = {"en/p185.tex": "en", "fr/p185.tex": "fr"}
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
        or receipt.get("predecessor_revision") != "v068c3r18"
        or receipt.get("status") != "PASS"
        or receipt.get("errors") != []
        or receipt.get("compile_order") != ["fr", "en"]
        or receipt.get("passes_per_language") != 2
        or receipt.get("shell") is not False
    ):
        raise ReaderError("sealed r19 build receipt semantics drifted")
    verification = receipt.get("staged_source_verification", {})
    if tuple(verification.get(key) for key in ("rows", "total_file_bytes", "bytes", "sha256")) != PREDECESSOR_MANIFEST:
        raise ReaderError("sealed r19 staged-source receipt drifted")
    surface = receipt.get("revision_surface_contract", {})
    if surface.get("replaced_staged_paths") != ["en/p179.tex", "fr/p179.tex"] or surface.get("other_staged_source_changes") != 0:
        raise ReaderError("sealed r19 revision surface drifted")
    if (
        qa.get("schema") != "tohoku-v068-reader-independent-qa-v1"
        or qa.get("qa_revision") != "v68r41"
        or qa.get("reader_revision") != PREDECESSOR_REVISION
        or qa.get("status") != "PASS"
        or qa.get("errors") != []
        or qa.get("conclusion", {}).get("reader_successor_accepted") is not True
        or qa.get("conclusion", {}).get("visual_review_accepted") is not True
    ):
        raise ReaderError("sealed v68r41 QA semantics drifted")
    if (
        structural.get("schema") != "tohoku-v068-reader-independent-qa-prepare-v41"
        or structural.get("reader_revision") != PREDECESSOR_REVISION
        or structural.get("status") != "STRUCTURAL_PASS_VISUAL_PENDING"
        or structural.get("errors") != []
    ):
        raise ReaderError("sealed v68r41 structural QA semantics drifted")


def preflight(engine: Any, script_identity: Mapping[str, Any], base_identity: Mapping[str, Any]) -> dict[str, Any]:
    predecessor_receipt_data = exact(PREDECESSOR_RECEIPT, PREDECESSOR_RECEIPT_EXPECTED, "v068c3r19 build receipt")
    predecessor_qa_data = exact(PREDECESSOR_QA, PREDECESSOR_QA_EXPECTED, "v68r41 QA receipt")
    predecessor_structural_data = exact(PREDECESSOR_QA_STRUCTURAL, PREDECESSOR_QA_STRUCTURAL_EXPECTED, "v68r41 structural receipt")
    validate_predecessor(
        parse_json(predecessor_receipt_data, "r19 build receipt"),
        parse_json(predecessor_qa_data, "v68r41 QA receipt"),
        parse_json(predecessor_structural_data, "v68r41 structural receipt"),
    )
    predecessor_pdf_records: dict[str, Any] = {}
    for language, (path, size, sha256, pages) in PREDECESSOR_PDFS.items():
        data = exact(path, (size, sha256), f"r19 {language} PDF")
        predecessor_pdf_records[language] = {"path": path.relative_to(ROOT).as_posix(), "bytes": len(data), "sha256": digest(data), "pages": pages}

    admission_data = exact(P185_RECEIPT, P185_RECEIPT_EXPECTED, "p185_fix2 receipt")
    admission = parse_json(admission_data, "p185_fix2 receipt")
    if (
        admission.get("schema") != "tohoku-p185-sheaf-center-global-sections-source-admission-v1"
        or admission.get("status") != "PASS"
        or admission.get("errors") != []
        or admission.get("decision_id") != "TOH-P185-COR-002"
        or admission.get("source_correction_id") != "TOH-SRC-P185-002"
        or admission.get("production_successor") != "production/p185_fix2"
    ):
        raise ReaderError("p185_fix2 receipt semantics drifted")
    p185_payloads = {name: exact(path, (size, sha), f"p185_fix2 {name}") for name, (path, size, sha) in P185_FILES.items()}
    ledger_data = exact(SOURCE_LEDGER, SOURCE_LEDGER_EXPECTED, "source correction ledger postimage")
    if ledger_data.count(b'"decision_id":"TOH-SRC-P185-002"') != 1 or b'"layer":"fr_corrected;en"' not in ledger_data:
        raise ReaderError("root ledger D1017-R001 row surface drifted")

    predecessor_payloads, predecessor_manifest = engine.snapshot_predecessor_tree()
    if tuple(predecessor_manifest[key] for key in ("rows", "total_file_bytes", "bytes", "sha256")) != PREDECESSOR_MANIFEST:
        raise ReaderError("live r19 staged-source manifest drifted")
    for name, expected in P185_PREDECESSOR.items():
        data = predecessor_payloads.get(name)
        if data is None or (len(data), digest(data)) != expected:
            raise ReaderError(f"r19 p185 staged preimage drifted: {name}")
    if predecessor_payloads["dip/p185.tex"] != p185_payloads["dip"]:
        raise ReaderError("p185 diplomatic layer is not byte-identical")
    successor_payloads = dict(predecessor_payloads)
    successor_payloads["fr/p185.tex"] = p185_payloads["fr"]
    successor_payloads["en/p185.tex"] = p185_payloads["en"]
    successor_manifest = engine.manifest_record(successor_payloads)
    if tuple(successor_manifest[key] for key in ("rows", "total_file_bytes", "bytes", "sha256")) != SUCCESSOR_MANIFEST:
        raise ReaderError(f"derived r20 staged-source manifest drifted: {successor_manifest}")
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
    if [row["path"] for row in changed] != ["en/p185.tex", "fr/p185.tex"]:
        raise ReaderError(f"derived r20 source delta is not exact: {changed}")
    return {
        "_successor_payloads": successor_payloads,
        "toolchain_script": dict(script_identity),
        "nested_transaction_engine": dict(base_identity),
        "predecessor_build_receipt": {"path": PREDECESSOR_RECEIPT.relative_to(ROOT).as_posix(), "bytes": len(predecessor_receipt_data), "sha256": digest(predecessor_receipt_data)},
        "predecessor_qa_receipt": {"path": PREDECESSOR_QA.relative_to(ROOT).as_posix(), "bytes": len(predecessor_qa_data), "sha256": digest(predecessor_qa_data)},
        "predecessor_structural_receipt": {"path": PREDECESSOR_QA_STRUCTURAL.relative_to(ROOT).as_posix(), "bytes": len(predecessor_structural_data), "sha256": digest(predecessor_structural_data)},
        "predecessor_pdfs": predecessor_pdf_records,
        "source_admission": {"path": P185_RECEIPT.relative_to(ROOT).as_posix(), "bytes": len(admission_data), "sha256": digest(admission_data)},
        "source_admission_files": {name: {"path": path.relative_to(ROOT).as_posix(), "bytes": size, "sha256": sha} for name, (path, size, sha) in P185_FILES.items()},
        "source_corrections_ledger": {"path": SOURCE_LEDGER.relative_to(ROOT).as_posix(), "bytes": len(ledger_data), "sha256": digest(ledger_data)},
        "source_transition": {
            "predecessor": predecessor_manifest,
            "successor": successor_manifest,
            "changed_files": changed,
            "changed_file_count": 2,
            "byte_identical_file_count": 541,
            "only_changed_printed_page": 185,
            "selected_source_successor": "production/p185_fix2",
            "diplomatic_p185_byte_identical": True,
            "p183_p185_p186_target_and_seam_gate": "PASS_FROM_SOURCE_ADMISSION",
        },
        "pypdf": engine.pypdf_role(),
    }


def preflight_namespace(engine: Any, pdflatex_argument: str) -> Path:
    if os.name != "nt":
        raise ReaderError("r20 no-overwrite promotion requires Windows semantics")
    executable = Path(pdflatex_argument)
    if not executable.is_absolute() or executable.resolve(strict=True) != engine.PDFLATEX:
        raise ReaderError("--pdflatex is not the exact admitted absolute path")
    if os.path.lexists(GATE) or any(os.path.lexists(path) for path in FINAL_OUTPUTS.values()):
        raise FileExistsError("r20 gate or a revision-named final already exists")
    for parent in (GATE.parent, OUTPUT_ROOT):
        if not parent.is_dir() or parent.is_symlink():
            raise ReaderError(f"required ordinary parent is invalid: {parent}")
    return executable


def create_staged_source(engine: Any, payloads: Mapping[str, bytes]) -> dict[str, Any]:
    GATE.mkdir(parents=False, exist_ok=False)
    engine.hold(GATE, directory=True)
    owner = GATE / ".build68r20-owner.json"
    owner_payload = (json.dumps({"schema": "tohoku-build68r20-owner-v1", "revision": REVISION, "token": secrets.token_hex(32).upper()}, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
    with owner.open("xb") as output:
        output.write(owner_payload)
        output.flush()
        os.fsync(output.fileno())
    engine.lock_and_require(owner, (len(owner_payload), digest(owner_payload)), "r20 owner")
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
    stage = RECEIPT.with_name(".build.json.r20.stage")
    if os.path.lexists(RECEIPT) or os.path.lexists(stage):
        raise FileExistsError("r20 receipt or sibling stage exists")
    with stage.open("xb") as output:
        output.write(data)
        output.flush()
        os.fsync(output.fileno())
    handle = engine.open_locked_path(stage, directory=False, allow_delete_share=True)
    engine.all_locks.append(handle)
    try:
        if engine.read_locked_file(handle) != data:
            raise ReaderError("r20 receipt-stage readback differs")
        engine.move_no_replace(stage, RECEIPT)
        engine.receipt_committed = True
    finally:
        engine.release_handle(handle)
    final = engine.lock_and_require(RECEIPT, (len(data), digest(data)), "committed r20 receipt")
    if engine.read_locked_file(final) != data:
        raise ReaderError("committed r20 receipt readback differs")
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
            "replaced_staged_paths": ["en/p185.tex", "fr/p185.tex"],
            "other_staged_source_changes": 0,
            "selected_source_successor": "production/p185_fix2",
            "diplomatic_p185_byte_identical": True,
            "target_gate": "build/v068c3r20",
            "final_outputs": ["output/pdf/fr-p119-221-v068c3r20.pdf", "output/pdf/en-p119-221-v068c3r20.pdf"],
        },
        "expected_reader_pages": {"fr": 94, "en": 90},
        "downstream_binding_gate": {
            "status": "REQUIRES_EXPLICIT_POST_BUILD_IDENTITIES",
            "required_file": "tmp/d1017_p185_repair_toolchain/r20_output_bindings.json",
            "reason": "v68r42 and sem/r21 must bind the actual receipt and final PDF identities after this deterministic build; they may not infer or guess future hashes.",
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
    parser = argparse.ArgumentParser(description="Preflight or build exact no-overwrite Tohoku bilingual reader v068c3r20.")
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
            "future_identity_gate": "r20_output_bindings.json must be created from exact post-build readbacks",
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
