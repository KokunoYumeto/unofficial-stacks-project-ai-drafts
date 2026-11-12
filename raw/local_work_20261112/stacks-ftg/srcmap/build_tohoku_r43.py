#!/usr/bin/env python3
"""Build the atomic no-overwrite Tohoku r43 mapping successor."""

from __future__ import annotations

import contextlib
import csv
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys
from collections.abc import Iterator
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
VALIDATOR = ROOT / "srcmap" / "validate_tohoku_r43.py"
BOOTSTRAP = ROOT / "srcmap" / "start_build_tohoku_r43.py"
DRIVER = ROOT / "srcmap" / "start_build_tohoku_r43.ps1"

EXPECTED_VALIDATOR = (
    45131,
    "56E6B95D0A8A1842B2BF35814FF31CE6456A7F7DEDAFD764B5BBFD9650983F20",
)

STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- The semantic source is the exact independently audited local-unpublished sem/r17 surface; stable unit IDs remain 991.\n"
    "- The sealed r42 decision ledger is preserved byte-for-byte through D000999 and exact decision D001000 is appended.\n"
    "- D001000 supersedes D000251 for the pointwise flabby envelope, flasque group sheaves, torsor triviality, and abelian H^1 vanishing.\n"
    "- The decision explicitly preserves the empty-stalk caveat for arbitrary set-valued products and makes no claim that the point factors are stalks of the product sheaf.\n"
    "- The sem/r17 p. 161 subject repair propagates to the stable divisor-sequence unit while D000999 remains its selected mapping decision.\n"
    "- All 29 source issues remain resolved; issues.csv is byte-identical to r42.\n"
    "- The bounded scanner indexes the exact 119 inherited TeX filenames; only cohomology.tex changes from r42, adding exactly two labels and no topic candidates.\n"
    "- 59 gap-class dispositions remain.\n"
    "- This local dossier makes no release, publication, remote-freshness, DOI, rights, or whole-paper completion claim.\n"
).encode("utf-8")

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


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def no_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"Duplicate JSON key: {key}")
        output[key] = value
    return output


def strict_json(path: Path) -> dict:
    data = path.read_bytes()
    if b"\r" in data or not data.endswith(b"\n"):
        raise RuntimeError(f"Noncanonical JSON: {path}")
    value = json.loads(data.decode("utf-8"), object_pairs_hook=no_duplicate_pairs)
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected JSON object: {path}")
    return value


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    data = path.read_bytes()
    if b"\r" in data or not data.endswith(b"\n"):
        raise RuntimeError(f"Noncanonical CSV: {path}")
    reader = csv.DictReader(data.decode("utf-8-sig").splitlines())
    rows = list(reader)
    if reader.fieldnames is None or any(None in row or None in row.values() for row in rows):
        raise RuntimeError(f"Malformed CSV: {path}")
    return list(reader.fieldnames), rows


def csv_bytes(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def exclusive_write(path: Path, data: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    if path.read_bytes() != data:
        raise RuntimeError(f"Write readback mismatch: {path}")


def is_reparse(path: Path) -> bool:
    return bool(path.stat(follow_symlinks=False).st_file_attributes & 0x400)


def require_plain_file(path: Path) -> None:
    if not path.is_file() or path.is_symlink() or is_reparse(path):
        raise RuntimeError(f"Expected plain file: {path}")


def require_plain_directory(path: Path) -> None:
    if not path.is_dir() or path.is_symlink() or is_reparse(path):
        raise RuntimeError(f"Expected plain directory: {path}")


def require_identity(path: Path, expected: tuple[int, str]) -> None:
    require_plain_file(path)
    if identity(path) != expected:
        raise RuntimeError(f"Input identity drift: {path}")


def load_validator_module():
    require_identity(VALIDATOR, EXPECTED_VALIDATOR)
    spec = importlib.util.spec_from_file_location("tohoku_r43_validator_contract", VALIDATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load frozen r43 validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    require_identity(VALIDATOR, EXPECTED_VALIDATOR)
    return module


@contextlib.contextmanager
def deny_write_delete(paths: list[Path]) -> Iterator[None]:
    """Hold Windows read handles that deny writes and deletion."""
    if os.name != "nt":
        raise RuntimeError("This transaction requires Windows file locks")
    import ctypes
    from ctypes import wintypes

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_file = kernel32.CreateFileW
    create_file.argtypes = [
        wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID,
        wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE,
    ]
    create_file.restype = wintypes.HANDLE
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL
    handles: list[object] = []
    invalid = ctypes.c_void_p(-1).value
    try:
        for path in sorted(set(paths), key=lambda item: str(item).casefold()):
            require_plain_file(path)
            handle = create_file(
                str(path), 0x80000000, 0x00000001, None, 3, 0x00000080, None
            )
            if handle in (None, invalid):
                raise OSError(ctypes.get_last_error(), f"Cannot lock {path}")
            handles.append(handle)
        yield
    finally:
        for handle in reversed(handles):
            close_handle(handle)


@contextlib.contextmanager
def single_writer_mutex() -> Iterator[None]:
    if os.name != "nt":
        raise RuntimeError("This transaction requires a Windows mutex")
    import ctypes
    from ctypes import wintypes

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_mutex = kernel32.CreateMutexW
    create_mutex.argtypes = [wintypes.LPVOID, wintypes.BOOL, wintypes.LPCWSTR]
    create_mutex.restype = wintypes.HANDLE
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL
    handle = create_mutex(None, False, r"Local\FAC-Tohoku-r43-mapping")
    if not handle:
        raise OSError(ctypes.get_last_error(), "Cannot create Tohoku r43 mutex")
    if ctypes.get_last_error() == 183:
        close_handle(handle)
        raise RuntimeError("Another Tohoku r43 transaction is active")
    try:
        yield
    finally:
        close_handle(handle)


def verify_execution_attestation() -> dict[str, object]:
    attestation = globals().get("EXECUTION_ATTESTATION")
    if not isinstance(attestation, dict) or set(attestation) != {
        "driver", "bootstrap", "builder", "validator"
    }:
        raise RuntimeError("Run through start_build_tohoku_r43.ps1")
    expected_paths = {
        "driver": "srcmap/start_build_tohoku_r43.ps1",
        "bootstrap": "srcmap/start_build_tohoku_r43.py",
        "builder": "srcmap/build_tohoku_r43.py",
        "validator": "srcmap/validate_tohoku_r43.py",
    }
    for role, relative in expected_paths.items():
        item = attestation.get(role)
        if not isinstance(item, dict) or item.get("path") != relative:
            raise RuntimeError(f"{role} attestation path drift")
        if set(item) != {"path", "bytes", "sha256", "contract"}:
            raise RuntimeError(f"{role} attestation shape drift")
        require_identity(ROOT / relative, (int(item["bytes"]), str(item["sha256"])))
    if (int(attestation["validator"]["bytes"]), str(attestation["validator"]["sha256"])) != EXPECTED_VALIDATOR:
        raise RuntimeError("Frozen validator attestation drift")
    if identity(Path(__file__)) != (
        int(attestation["builder"]["bytes"]), str(attestation["builder"]["sha256"])
    ):
        raise RuntimeError("Same-bytes builder attestation drift")
    expected_contracts = {
        "driver": "self_read_hash_then_one_shot_bootstrap_envelope",
        "bootstrap": "one_read_hash_compile_exec_builder_and_pin_validator",
        "builder": "read_hash_compile_and_exec_same_payload",
        "validator": "independent_same_bytes_stage_and_receipt_replay",
    }
    if any(attestation[role]["contract"] != contract for role, contract in expected_contracts.items()):
        raise RuntimeError("Execution-role contract drift")
    return attestation


def lock_paths(validator, fresh: bool) -> list[Path]:
    paths = [Path(__file__), BOOTSTRAP, DRIVER, VALIDATOR]
    paths.extend(SOURCE / name for name in validator.EXPECTED_SOURCE)
    paths.extend(SEM / name for name in validator.EXPECTED_SEM)
    paths.extend(ROOT / name for name in validator.expected_runtime())
    legacy = validator.load_legacy_validator()
    paths.extend(AUTHORITY / name for name in legacy.EXPECTED_AUTHORITY)
    paths.extend(PROJECT / name for name in validator.expected_repairs())
    if fresh:
        paths.extend(ROOT / name for name in validator.expected_tex_hashes())
        paths.extend(ROOT / name for name in validator.expected_artifacts())
    elif TARGET.exists():
        paths.extend(path for path in TARGET.iterdir() if path.is_file())
    return paths


def make_config(validator) -> dict:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r43"
    cfg["expected_units"] = 991
    cfg["inputs"]["primary"] = {
        **record(SEM / "nodes.csv", "nodes.csv"),
        "filename": "nodes.csv",
        "source_file": "sem/r17/nodes.csv",
    }
    for key, filename in (
        ("edges", "edges.csv"),
        ("terms", "terms.csv"),
        ("stacks", "stacks.csv"),
    ):
        cfg["inputs"][key] = {
            **record(SEM / filename, filename),
            "filename": filename,
        }
    cfg["inputs"]["sem_manifest"] = {
        **record(SEM / "manifest.json", "sem/r17 manifest"),
        "filename": "manifest.json",
    }
    cfg["inputs"]["sem_validation"] = {
        **record(SEM / "validation.json", "sem/r17 validation"),
        "filename": "validation.json",
    }
    cfg["inputs"].pop("sem_input", None)
    cfg["inputs"].pop("sem_check", None)
    cfg["required_extra_keys"] = [
        "part_i", "part_ii", "edges", "terms", "stacks",
        "sem_manifest", "sem_validation",
    ]
    cfg["semantic_successor"] = {
        "generation": "sem/r17",
        "surface_files": validator.EXPECTED_SEM_SURFACE[0],
        "surface_bytes": validator.EXPECTED_SEM_SURFACE[1],
        "surface_sha256": validator.EXPECTED_SEM_SURFACE[2],
        "manifest_payload_files": validator.EXPECTED_SEM_PAYLOAD_SURFACE[0],
        "manifest_payload_bytes": validator.EXPECTED_SEM_PAYLOAD_SURFACE[1],
        "manifest_payload_sha256": validator.EXPECTED_SEM_PAYLOAD_SURFACE[2],
        "manifest": record(SEM / "manifest.json", "sem/r17/manifest.json"),
        "validation": record(SEM / "validation.json", "sem/r17/validation.json"),
        "independent_postbuild_audit": "STRICT_PASS",
    }
    return cfg


def make_decisions(validator) -> bytes:
    fields, rows = load_csv(SOURCE / "dec.csv")
    if fields != [
        "decision_id", "unit_id", "action", "disposition", "stacks_labels",
        "rationale", "review_state", "supersedes",
    ]:
        raise RuntimeError("Predecessor decision schema drift")
    if [row["decision_id"] for row in rows] != [f"D{number:06d}" for number in range(1, 1000)]:
        raise RuntimeError("Predecessor decision sequence drift")
    suffix = csv_bytes(fields, validator.DECISION_ROWS)
    return (SOURCE / "dec.csv").read_bytes() + suffix[suffix.index(b"\n") + 1 :]


def run_tool(validator, name: str, *args: str) -> None:
    relative = f"srcmap/{name}"
    runtime = validator.expected_runtime()
    require_identity(ROOT / relative, runtime[relative])
    subprocess.run(
        [sys.executable, "-I", "-B", str(ROOT / relative), *args],
        cwd=ROOT,
        check=True,
    )
    require_identity(ROOT / relative, runtime[relative])


def intake_args() -> list[str]:
    specs = [
        ("part_i", AUTHORITY / "jstage_part_I_9_2_119.pdf"),
        ("part_ii", AUTHORITY / "jstage_part_II_9_3_185.pdf"),
        ("edges", SEM / "edges.csv"),
        ("terms", SEM / "terms.csv"),
        ("stacks", SEM / "stacks.csv"),
        ("sem_manifest", SEM / "manifest.json"),
        ("sem_validation", SEM / "validation.json"),
    ]
    output: list[str] = []
    for key, path in specs:
        output += ["--extra", f"{key}={path}"]
    return output


def run_validator(path: Path, receipt: bool = False) -> dict[str, object]:
    require_identity(VALIDATOR, EXPECTED_VALIDATOR)
    env = os.environ.copy()
    env["TOHOKU_R43_VALIDATOR_EXPECTED"] = json.dumps(
        {"bytes": EXPECTED_VALIDATOR[0], "sha256": EXPECTED_VALIDATOR[1]},
        separators=(",", ":"),
    )
    command = [sys.executable, "-I", "-B", str(VALIDATOR), "--stage", str(path)]
    if receipt:
        command.append("--receipt")
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    require_identity(VALIDATOR, EXPECTED_VALIDATOR)
    value = json.loads(completed.stdout, object_pairs_hook=no_duplicate_pairs)
    if not isinstance(value, dict) or value.get("status") != "PASS" or value.get("errors") != []:
        raise RuntimeError("Independent r43 validator did not return PASS")
    return value


def core_deltas(validation: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in validation.items() if key not in {"schema", "attestation"}}


def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def execution_receipt(attestation: dict[str, object], validator) -> dict[str, object]:
    return {
        "attestation": attestation,
        "dependencies": {
            name: {"name": Path(name).name, "bytes": expected[0], "sha256": expected[1]}
            for name, expected in sorted(validator.expected_runtime().items())
        },
        "contract": "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion_with_rollback",
    }


def receipt_payload(
    root: Path,
    attestation: dict[str, object],
    validator,
    deltas: dict[str, object],
) -> dict[str, object]:
    external = validator.verify_external()
    return {
        "schema": "tohoku-stacks-mapping-successor-r43-v1",
        "status": "PASS",
        "errors": [],
        "predecessor_dossier": external["predecessor"],
        "semantic_source": external["semantic"],
        "source_repairs": external["repairs"],
        "builds": external["builds"],
        "execution": execution_receipt(attestation, validator),
        "git": {
            "inspection_performed": False,
            "reason": "No Git operation was needed for this bounded local successor.",
            "predecessor_receipt": record(SOURCE / "r42-check.json", "tohoku_r42/r42-check.json"),
            "remote_server_freshness_verified": False,
        },
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": [
            "No Git command or recursive workspace scan is executed by this mapping successor.",
            "The Stacks scanner is confined to the exact 119 top-level TeX filenames inherited from sealed r42.",
            "No release, publication, upload, DOI, Zenodo, rights, remote-freshness, or whole-paper completion claim is made.",
            "The only appended mapping ledger row is D001000, which supersedes D000251.",
            "issues.csv and topics.csv remain byte-identical to r42.",
            "The arbitrary-set pointwise product is not claimed flasque when empty stalks occur.",
            "The point factors are not claimed to be the stalks of the pointwise product sheaf.",
            "No official Stacks tag is claimed for either D001000 label.",
            "59 Tohoku gap-class dispositions remain.",
        ],
    }


def verify_existing(attestation: dict[str, object], validator) -> dict[str, object]:
    require_plain_directory(TARGET)
    validation = run_validator(TARGET, receipt=True)
    deltas = core_deltas(validation)
    receipt = strict_json(TARGET / "r43-check.json")
    expected = receipt_payload(TARGET, attestation, validator, deltas)
    if receipt != expected:
        raise RuntimeError("Existing r43 receipt replay mismatch")
    return receipt


def rollback_promoted_target() -> None:
    if os.path.lexists(STAGE):
        raise RuntimeError("Cannot roll back promoted r43 target: stage path appeared")
    require_plain_directory(TARGET)
    os.rename(TARGET, STAGE)
    require_plain_directory(STAGE)


def main_locked(attestation: dict[str, object], validator) -> int:
    target_entry = os.path.lexists(TARGET)
    stage_entry = os.path.lexists(STAGE)
    if target_entry and stage_entry:
        raise RuntimeError("Target and unresolved r43 transaction coexist")
    if stage_entry:
        raise FileExistsError(f"Unresolved r43 transaction exists: {STAGE}")
    fresh = not target_entry
    with deny_write_delete(lock_paths(validator, fresh)):
        validator.verify_external()
        if target_entry:
            receipt = verify_existing(attestation, validator)
            print(json.dumps(receipt, ensure_ascii=True, indent=2, sort_keys=True))
            return 0

        STAGE.mkdir()
        exclusive_write(STAGE / "cfg.json", json_bytes(make_config(validator)))
        exclusive_write(STAGE / "topics.csv", (SOURCE / "topics.csv").read_bytes())
        exclusive_write(STAGE / "dec.csv", make_decisions(validator))
        exclusive_write(STAGE / "issues.csv", (SOURCE / "issues.csv").read_bytes())
        run_tool(validator, "intake.py", str(STAGE), str(SEM / "nodes.csv"), *intake_args())
        run_tool(validator, "scan.py", str(STAGE))
        run_tool(validator, "map.py", str(STAGE))
        exclusive_write(STAGE / "STATUS.md", STATUS_BYTES)

        staged_validation = run_validator(STAGE)
        deltas = core_deltas(staged_validation)
        receipt = receipt_payload(STAGE, attestation, validator, deltas)
        exclusive_write(STAGE / "r43-check.json", json_bytes(receipt))
        run_validator(STAGE, receipt=True)
        if {
            path.name for path in STAGE.iterdir() if path.is_file()
        } != PAYLOAD | {"r43-check.json"} or any(path.is_dir() for path in STAGE.iterdir()):
            raise RuntimeError("Staged r43 dossier surface mismatch")

        validator.verify_external()
        if os.path.lexists(TARGET):
            raise FileExistsError(f"No-overwrite target appeared before promotion: {TARGET}")
        os.rename(STAGE, TARGET)
        try:
            with deny_write_delete([path for path in TARGET.iterdir() if path.is_file()]):
                final = verify_existing(attestation, validator)
        except BaseException as replay_error:
            try:
                rollback_promoted_target()
            except BaseException as rollback_error:
                raise RuntimeError(
                    f"Post-promotion replay failed and rollback failed: {rollback_error}"
                ) from replay_error
            raise RuntimeError(
                f"Post-promotion replay failed; exact promoted directory rolled back to {STAGE}"
            ) from replay_error
        print(json.dumps(final, ensure_ascii=True, indent=2, sort_keys=True))
        return 0


def main() -> int:
    attestation = verify_execution_attestation()
    validator = load_validator_module()
    with single_writer_mutex():
        return main_locked(attestation, validator)


if __name__ == "__main__":
    raise SystemExit(main())
