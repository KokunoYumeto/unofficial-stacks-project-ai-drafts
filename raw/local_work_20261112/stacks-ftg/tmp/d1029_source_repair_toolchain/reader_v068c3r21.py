#!/usr/bin/env python3
"""No-overwrite bilingual reader successor v068c3r21 for D1029."""

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
BASE_BUILDER_EXPECTED = (30417, "A83714697971089C45AB86E981892B585A3F5DA3712184C0D92D6D7DD0E056B2")
PREDECESSOR_REVISION = "v068c3r20"
REVISION = "v068c3r21"
GATE = ROOT / "build" / REVISION
STAGED_SOURCE = GATE / "src"
RECEIPT = GATE / "build.json"
OUTPUT_ROOT = ROOT / "output" / "pdf"
FINAL_OUTPUTS = {lang: OUTPUT_ROOT / f"{lang}-p119-221-{REVISION}.pdf" for lang in ("fr", "en")}
PREDECESSOR_SOURCE = ROOT / "build" / PREDECESSOR_REVISION / "src"
PREDECESSOR_RECEIPT = ROOT / "build" / PREDECESSOR_REVISION / "build.json"
PREDECESSOR_RECEIPT_EXPECTED = (22216, "BA5D7BFDEA8F733CBA65703C5DA017E26A3FEB417297A975EBCAEFEA41D2BEA1")
PREDECESSOR_QA = ROOT / "qa" / "v68r42" / "check.json"
PREDECESSOR_QA_EXPECTED = (5375, "C3D039B399FDA3A2232F07A0D33ABB3E07ADEA431182FCEC26F3C8A9DFD703D0")
PREDECESSOR_STRUCTURAL = ROOT / "qa" / "v68r42" / "structural.json"
PREDECESSOR_STRUCTURAL_EXPECTED = (7900, "06EBFDCE2E77644BADB3A38606662FEBA4B518AECC99A84BEEE70DA930E71171")
PREDECESSOR_MANIFEST = (543, 11855949, 62845, "52559D18F2A77C82A3BBAB69E4949C3A17C7DA1593034719F5B72584E9540310")
PREDECESSOR_PDFS = {
    "fr": (ROOT / "output" / "pdf" / "fr-p119-221-v068c3r20.pdf", 1417551, "91EE76111A240E36AC107FCAC9605A5E32E9E9796AAE86AAB495D5F36DB3AFB8", 94),
    "en": (ROOT / "output" / "pdf" / "en-p119-221-v068c3r20.pdf", 1381128, "3E78467B441F801DE742584CA9FBE906A886B4B9DD6AA4585315DB9482175AA1", 90),
}
SOURCE_ROOT = ROOT / "production" / "p188_fix1"
SOURCE_CHECK = SOURCE_ROOT / "check.json"
SOURCE_CHECK_EXPECTED = (4625, "52D174E72E44BE1DC5E6EE25A405B8C971EA4434F10BA7753F10CA1491851CF6")
SOURCE_FILES = {
    "decisions": (SOURCE_ROOT / "decisions.jsonl", 4600, "DE1B3BB745A6B8FDCC3573F83A272060DB727B87B9A079BA4C0EADCE51951420"),
    "targets": (SOURCE_ROOT / "targets.csv", 613, "A7378FBB1ABEB836C834668C1E84E18A72D0613F2DA546E809B7293386294E01"),
    "reuse": (SOURCE_ROOT / "reuse.txt", 37, "700C6F75C12D72DCCCAC7166921B065D504DA06B29EABEF868760767FAFA3207"),
    "dip": (SOURCE_ROOT / "tex" / "fr_diplomatic" / "p188.tex", 3890, "0C9D3A1133C014C9BB6687580DCFBDE40A87B7FE21E98838BFD820983334D9FF"),
    "fr": (SOURCE_ROOT / "tex" / "fr_corrected" / "p188.tex", 3619, "3CD7D1D8D50DD83627B24AC726EB244E09CAF483890071D68940C551A42ED0CC"),
    "en": (SOURCE_ROOT / "tex" / "en" / "p188.tex", 3498, "A171187600BB72B32FDB4E686D5AC994146BEC8DFC99571F0ACF3C3B1862FA5C"),
}
LEDGER = ROOT / "SOURCE_CORRECTIONS.jsonl"
LEDGER_EXPECTED = (213247, "F2DE702681CF4150C87FDC9C9051A105E94CBD681219ADC600DB9049B1E1E4B1")
P188_PREDECESSOR = {
    "dip/p188.tex": (3890, "0C9D3A1133C014C9BB6687580DCFBDE40A87B7FE21E98838BFD820983334D9FF"),
    "fr/p188.tex": (3623, "CB86F66DB892CDA79F1561AE42BFE39BD63BD0BE715F8E981589E19D08A9A212"),
    "en/p188.tex": (3503, "E1F0A1F899A6E042220929DCA498426A3DDD255629C07B9D6D460EE99094A139"),
}
REPLACEMENT_TARGETS = {"en/p188.tex": "en", "fr/p188.tex": "fr"}
MASTERS = {
    "fr": ("main-fr.tex", 3240, "45C11EE2DBA372D0485FE2FFEFA104DC4F7BE75752600B7384A1C33A23261D3B", 94),
    "en": ("main-en.tex", 3210, "37D0BDB5989439C90298854B36DCD3534F78EED900E3B94E9919FC72B1936C1F", 90),
}
CREATED_UTC = "2026-08-24T08:15:00Z"


class ReaderError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path, data: bytes) -> dict[str, Any]:
    try:
        shown = path.relative_to(ROOT).as_posix()
    except ValueError:
        shown = str(path)
    return {"path": shown, "bytes": len(data), "sha256": sha(data)}


def exact(path: Path, expected: tuple[int, str], label: str) -> bytes:
    if not path.is_file() or path.is_symlink() or path.resolve(strict=True) != path:
        raise ReaderError(f"{label}: invalid path")
    data = path.read_bytes()
    if (len(data), sha(data)) != expected:
        raise ReaderError(f"{label}: identity drifted: {(len(data), sha(data))}")
    return data


def strict_json(data: bytes, label: str) -> dict[str, Any]:
    value = json.loads(data.decode("utf-8"))
    if not isinstance(value, dict):
        raise ReaderError(f"{label}: JSON root is not an object")
    return value


def load_engine() -> tuple[Any, dict[str, Any]]:
    data = exact(BASE_BUILDER, BASE_BUILDER_EXPECTED, "sealed build68r18.py")
    module = types.ModuleType("__d1029_verified_build68r18__")
    module.__file__ = str(BASE_BUILDER)
    module.__package__ = None
    exec(compile(data, str(BASE_BUILDER), "exec", dont_inherit=True), module.__dict__)
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
    return engine, identity(BASE_BUILDER, data)


def validate_predecessor(receipt: Mapping[str, Any], qa: Mapping[str, Any], structural: Mapping[str, Any]) -> None:
    if receipt.get("schema") != "tohoku-v068-staged-successor-build-v1" or receipt.get("revision") != PREDECESSOR_REVISION or receipt.get("status") != "PASS" or receipt.get("errors") != []:
        raise ReaderError("predecessor build semantics drifted")
    staged = receipt.get("staged_source_verification", {})
    if tuple(staged.get(k) for k in ("rows", "total_file_bytes", "bytes", "sha256")) != PREDECESSOR_MANIFEST:
        raise ReaderError("predecessor manifest receipt drifted")
    if qa.get("schema") != "tohoku-v068-reader-independent-qa-v1" or qa.get("qa_revision") != "v68r42" or qa.get("reader_revision") != PREDECESSOR_REVISION or qa.get("status") != "PASS":
        raise ReaderError("predecessor QA semantics drifted")
    if qa.get("conclusion", {}).get("visual_review_accepted") is not True:
        raise ReaderError("predecessor visual QA was not accepted")
    if structural.get("schema") != "tohoku-v068-reader-independent-qa-prepare-v42" or structural.get("status") != "STRUCTURAL_PASS_VISUAL_PENDING":
        raise ReaderError("predecessor structural QA semantics drifted")


def preflight(engine: Any, base_record: Mapping[str, Any]) -> dict[str, Any]:
    script_data = SCRIPT.read_bytes()
    predecessor_receipt_data = exact(PREDECESSOR_RECEIPT, PREDECESSOR_RECEIPT_EXPECTED, "r20 build receipt")
    qa_data = exact(PREDECESSOR_QA, PREDECESSOR_QA_EXPECTED, "v68r42 QA receipt")
    structural_data = exact(PREDECESSOR_STRUCTURAL, PREDECESSOR_STRUCTURAL_EXPECTED, "v68r42 structural receipt")
    validate_predecessor(strict_json(predecessor_receipt_data, "r20 receipt"), strict_json(qa_data, "r42 QA"), strict_json(structural_data, "r42 structural"))
    predecessor_pdf_records: dict[str, Any] = {}
    for lang, (path, size, digest, pages) in PREDECESSOR_PDFS.items():
        data = exact(path, (size, digest), f"r20 {lang} PDF")
        predecessor_pdf_records[lang] = {**identity(path, data), "pages": pages}

    check_data = exact(SOURCE_CHECK, SOURCE_CHECK_EXPECTED, "p188_fix1 receipt")
    check = strict_json(check_data, "p188_fix1 receipt")
    if check.get("schema") != "tohoku-p188-ext-center-source-admission-v1" or check.get("status") != "PASS" or check.get("decision_id") != "TOH-P188-COR-002" or check.get("source_correction_id") != "TOH-SRC-P188-003":
        raise ReaderError("p188_fix1 receipt semantics drifted")
    source_data = {name: exact(path, (size, digest), f"p188_fix1 {name}") for name, (path, size, digest) in SOURCE_FILES.items()}
    ledger_data = exact(LEDGER, LEDGER_EXPECTED, "source correction ledger")
    if ledger_data.count(b'"decision_id":"TOH-SRC-P188-003"') != 1:
        raise ReaderError("TOH-SRC-P188-003 ledger multiplicity drifted")

    predecessor_payloads, predecessor_manifest = engine.snapshot_predecessor_tree()
    if tuple(predecessor_manifest[k] for k in ("rows", "total_file_bytes", "bytes", "sha256")) != PREDECESSOR_MANIFEST:
        raise ReaderError("live r20 staged-source manifest drifted")
    for name, expected in P188_PREDECESSOR.items():
        data = predecessor_payloads.get(name)
        if data is None or (len(data), sha(data)) != expected:
            raise ReaderError(f"r20 p188 preimage drifted: {name}")
    if predecessor_payloads["dip/p188.tex"] != source_data["dip"]:
        raise ReaderError("p188 diplomatic layer is not byte-identical")
    successor_payloads = dict(predecessor_payloads)
    successor_payloads["fr/p188.tex"] = source_data["fr"]
    successor_payloads["en/p188.tex"] = source_data["en"]
    successor_manifest = engine.manifest_record(successor_payloads)
    setattr(engine, "SUCCESSOR_MANIFEST", tuple(successor_manifest[k] for k in ("rows", "total_file_bytes", "bytes", "sha256")))
    changed = []
    for name in sorted(predecessor_payloads):
        before, after = predecessor_payloads[name], successor_payloads[name]
        if before != after:
            changed.append({"path": name, "predecessor_bytes": len(before), "predecessor_sha256": sha(before), "successor_bytes": len(after), "successor_sha256": sha(after)})
    if [row["path"] for row in changed] != ["en/p188.tex", "fr/p188.tex"]:
        raise ReaderError(f"derived reader source delta is not exact: {changed}")
    for lang, (master, size, digest, _pages) in MASTERS.items():
        data = successor_payloads.get(master)
        if data is None or (len(data), sha(data)) != (size, digest):
            raise ReaderError(f"staged master drifted: {lang}")
    return {
        "_successor_payloads": successor_payloads,
        "toolchain_script": identity(SCRIPT, script_data),
        "nested_transaction_engine": dict(base_record),
        "predecessor_build_receipt": identity(PREDECESSOR_RECEIPT, predecessor_receipt_data),
        "predecessor_qa_receipt": identity(PREDECESSOR_QA, qa_data),
        "predecessor_structural_receipt": identity(PREDECESSOR_STRUCTURAL, structural_data),
        "predecessor_pdfs": predecessor_pdf_records,
        "source_admission": identity(SOURCE_CHECK, check_data),
        "source_admission_files": {name: identity(path, source_data[name]) for name, (path, _size, _digest) in SOURCE_FILES.items()},
        "source_corrections_ledger": identity(LEDGER, ledger_data),
        "source_transition": {
            "predecessor": predecessor_manifest,
            "successor": successor_manifest,
            "changed_files": changed,
            "changed_file_count": 2,
            "byte_identical_file_count": 541,
            "only_changed_printed_page": 188,
            "selected_source_successor": "production/p188_fix1",
            "diplomatic_p188_byte_identical": True,
        },
        "pypdf": engine.pypdf_role(),
    }


def namespace(engine: Any, pdflatex_argument: str) -> Path:
    executable = Path(pdflatex_argument)
    if os.name != "nt" or not executable.is_absolute() or executable.resolve(strict=True) != engine.PDFLATEX:
        raise ReaderError("--pdflatex is not the exact admitted executable")
    if os.path.lexists(GATE) or any(os.path.lexists(path) for path in FINAL_OUTPUTS.values()):
        raise FileExistsError("v068c3r21 gate or revision-named final exists")
    return executable


def create_staged_source(engine: Any, payloads: Mapping[str, bytes]) -> dict[str, Any]:
    GATE.mkdir(exist_ok=False)
    engine.hold(GATE, directory=True)
    owner = GATE / ".build68r21-owner.json"
    owner_data = (json.dumps({"schema": "tohoku-build68r21-owner-v1", "revision": REVISION, "token": secrets.token_hex(32).upper()}, sort_keys=True, separators=(",", ":")) + "\n").encode()
    with owner.open("xb") as handle:
        handle.write(owner_data); handle.flush(); os.fsync(handle.fileno())
    engine.lock_and_require(owner, (len(owner_data), sha(owner_data)), "r21 owner")
    STAGED_SOURCE.mkdir(exist_ok=False)
    engine.hold(STAGED_SOURCE, directory=True)
    directories: set[PurePosixPath] = set()
    for name in payloads:
        member = PurePosixPath(name)
        if member.is_absolute() or ".." in member.parts or member.as_posix() != name:
            raise ReaderError(f"unsafe staged path: {name}")
        for i in range(1, len(member.parts)):
            directories.add(PurePosixPath(*member.parts[:i]))
    for member in sorted(directories, key=lambda item: (len(item.parts), item.as_posix())):
        path = STAGED_SOURCE.joinpath(*member.parts); path.mkdir(exist_ok=False); engine.hold(path, directory=True)
    for name in sorted(payloads):
        path = STAGED_SOURCE.joinpath(*PurePosixPath(name).parts)
        data = payloads[name]
        with path.open("xb") as handle:
            handle.write(data); handle.flush(); os.fsync(handle.fileno())
        engine.staged_file_locks[name] = engine.lock_and_require(path, (len(data), sha(data)), f"staged {name}")
    return {"owner_marker": {**identity(owner, owner_data), "exclusive_create": True}, "staged_source": engine.verify_staged_source(dict(payloads))}


def commit_receipt(engine: Any, value: Mapping[str, Any]) -> dict[str, Any]:
    data = (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    stage = RECEIPT.with_name(".build.json.r21.stage")
    if os.path.lexists(RECEIPT) or os.path.lexists(stage):
        raise FileExistsError("r21 receipt namespace occupied")
    with stage.open("xb") as handle:
        handle.write(data); handle.flush(); os.fsync(handle.fileno())
    locked = engine.open_locked_path(stage, directory=False, allow_delete_share=True)
    engine.all_locks.append(locked)
    try:
        if engine.read_locked_file(locked) != data:
            raise ReaderError("r21 receipt stage readback differs")
        engine.move_no_replace(stage, RECEIPT)
        engine.receipt_committed = True
    finally:
        engine.release_handle(locked)
    final = engine.lock_and_require(RECEIPT, (len(data), sha(data)), "committed r21 receipt")
    if engine.read_locked_file(final) != data:
        raise ReaderError("committed r21 receipt readback differs")
    return identity(RECEIPT, data)


def build(engine: Any, inputs: dict[str, Any], executable: Path, pdflatex_record: Mapping[str, Any]) -> dict[str, Any]:
    payloads = inputs.pop("_successor_payloads")
    stage = create_staged_source(engine, payloads)
    compile_evidence = {lang: engine.compile_language(lang, executable) for lang in ("fr", "en")}
    after = engine.verify_staged_source(payloads)
    if after != stage["staged_source"]:
        raise ReaderError("staged source changed during compilation")
    pdfs, promotion = engine.promote_outputs()
    receipt = {
        "schema": "tohoku-v068-staged-successor-build-v1",
        "revision": REVISION,
        "predecessor_revision": PREDECESSOR_REVISION,
        "created_utc": CREATED_UTC,
        "status": "PASS",
        "errors": [],
        "compile_order": ["fr", "en"],
        "passes_per_language": 2,
        "shell": False,
        "input_snapshots": inputs,
        "gate_ownership": stage["owner_marker"],
        "staged_source_verification": after,
        "pdflatex": dict(pdflatex_record),
        "compile_evidence": compile_evidence,
        "pdfs": pdfs,
        "promotion": promotion,
        "revision_surface_contract": {
            "predecessor_staged_files": 543,
            "successor_staged_files": 543,
            "byte_identical_staged_files": 541,
            "replaced_staged_paths": ["en/p188.tex", "fr/p188.tex"],
            "other_staged_source_changes": 0,
            "selected_source_successor": "production/p188_fix1",
            "diplomatic_p188_byte_identical": True,
            "target_gate": "build/v068c3r21",
            "final_outputs": ["output/pdf/fr-p119-221-v068c3r21.pdf", "output/pdf/en-p119-221-v068c3r21.pdf"],
        },
        "expected_reader_pages": {"fr": 94, "en": 90},
        "qualifications": [
            "The PDF artifact-operation marker is run exactly once before this build.",
            "Only corrected-French and English p188 staged sources differ from v068c3r20; diplomatic p188 is byte-identical.",
            "No live Stacks TeX, map dossier, Git state, or network resource is touched.",
        ],
    }
    receipt_record = commit_receipt(engine, receipt)
    return {"status": "PASS", "build_receipt": receipt_record, "pdfs": pdfs}


def replay() -> dict[str, Any]:
    data = RECEIPT.read_bytes()
    receipt = strict_json(data, "r21 build receipt")
    if receipt.get("revision") != REVISION or receipt.get("status") != "PASS" or receipt.get("errors") != []:
        raise ReaderError("r21 receipt semantics drifted")
    records = {}
    for lang, path in FINAL_OUTPUTS.items():
        expected = receipt["pdfs"][lang]
        pdf = exact(path, (expected["bytes"], expected["sha256"]), f"r21 {lang} PDF")
        records[lang] = {**identity(path, pdf), "pages": expected["strict_pdf_parse"]["pages"]}
    return {"status": "PASS_COMMITTED_AND_REPLAYED", "build_receipt": identity(RECEIPT, data), "pdfs": records}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--execute", action="store_true")
    mode.add_argument("--replay", action="store_true")
    parser.add_argument("--pdflatex")
    args = parser.parse_args(sys.argv[1:] if argv is None else list(argv))
    if args.replay:
        result = replay()
    else:
        if not args.pdflatex:
            raise ReaderError("--pdflatex is required")
        engine, base_record = load_engine()
        inputs = preflight(engine, base_record)
        executable = namespace(engine, args.pdflatex)
        if args.preflight:
            result = {"status": "READY_NOT_EXECUTED", "revision": REVISION, "source_transition": inputs["source_transition"], "intended_outputs": [str(GATE), *(str(path) for path in FINAL_OUTPUTS.values())]}
        else:
            engine.lock_workspace()
            pdflatex_record = engine.acquire_pdflatex_lock(executable)
            try:
                result = build(engine, inputs, executable, pdflatex_record)
            except BaseException:
                engine.rollback_uncommitted_outputs()
                raise
            finally:
                engine.close_handles(engine.all_locks)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise SystemExit(1)
