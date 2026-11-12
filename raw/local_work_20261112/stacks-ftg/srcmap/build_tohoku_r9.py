#!/usr/bin/env python3
"""Build and commit an isolated Tohoku sem/r9 Stacks dossier."""

from __future__ import annotations

import contextlib
import csv
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path
from typing import Iterator


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "tohoku"
TARGET_DIR = ROOT / "tohoku_r9"
TXN_ROOT = ROOT / ".tohoku-r9-txn"
STAGE_DIR = TXN_ROOT / "tohoku_r9"
SNAPSHOT_DIR = TXN_ROOT / "inputs"
OWNER_PATH = TXN_ROOT / "OWNER.json"
PROJECT = (
    ROOT.parent
    / "interlanguage"
    / "03_projects"
    / "language_management"
    / "english_germanic"
    / "03_working_translations"
    / "tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r9"
QA = PROJECT / "qa" / "v68r21"
AUTHORITY = PROJECT / "authority_snapshot"

EXPECTED_BRANCH = "codex/fac-tohoku-gaga"
EXPECTED_HEAD = "952bb0e39acfa050db054d7ae7ea91c51487b7a9"
EXPECTED_TREE = "5a07bc1e20e706f88e2d7a4856bba6a7d7bf29b9"
EXPECTED_SEM_INPUT = (
    292652,
    "C83700598551492E09664D5DB7ABBC6D4210F3958363B5F60DE84F842AA5F67A",
)
EXPECTED_SEM_CHECK = (
    6392,
    "6798E389882B11FCE013473959FA3512911F077F48A2E45D315B0772805B3622",
)
EXPECTED_R9_SURFACE = (
    18,
    2020713,
    "249990551A69E72B905EE7B91BACED426E5888D7414FA0381E8193DAC57784E0",
)
EXPECTED_DEC = (
    65376,
    "A8C5374BFF33BB998BBF7001CC9F4534CF664298D02EB73C1B2E1798493B60BD",
)
EXPECTED_ISSUES = (
    11098,
    "D3735FFCEFDE2711CEC6AB7779C0233451CF9A1BE246172A905C25A3DD6960F9",
)
EXPECTED_AUTHORITY = {
    "part_i": (
        7305283,
        "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF",
    ),
    "part_ii": (
        3984260,
        "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53",
    ),
}
EXPECTED_TOPIC_CHANGES = {
    "tohoku:application:classical-spaces-with-operators": ("ext", ""),
    "tohoku:calculation:fixed-point-free-g-cover-cochains": ("ext", ""),
    "tohoku:construction:inverse-image-comparison:p2": ("ext", ""),
    "tohoku:def:composite-arrow": ("ext", ""),
    "tohoku:def:injective-object": ("abelian;ext;injectives", "abelian;injectives"),
    "tohoku:eq:2.5.5": ("ext", ""),
    "tohoku:eq:cover-cochains-product": ("cech;ext", "cech"),
    "tohoku:eq:divisor-class-cohomology": ("cech;ext", "cech"),
    "tohoku:equation:product-stalk-invariants": (
        "derived-functor;ext", "derived-functor"
    ),
    "tohoku:footnote:9": ("ext", ""),
    "tohoku:introduction:II:b": ("ext", ""),
    "tohoku:lemma:1.10.1:1": (
        "ext;grothendieck-category;injectives", "grothendieck-category;injectives"
    ),
    "tohoku:proof:proposition-4.1.3": ("ext;injectives", "injectives"),
    "tohoku:question:injectivity-of-stalk": (
        "abelian;ext;injectives", "abelian;injectives"
    ),
    "tohoku:section:1.3:footnote:1ter:text": ("abelian;ext", "abelian"),
}

# The launcher attests this helper itself. Embedding the helper hash here would
# create a self-reference; this table contains only separately read dependencies.
EXPECTED_TOOL_IDENTITIES: dict[str, tuple[int, str]] = {
    "fga/mkidx.py": (
        14844,
        "4425B5D021B3E35371DEBB567881697F88DF6F533ACFC9783A749CE1A5176A6B",
    ),
    "fga/mkmap.py": (
        22213,
        "7281F57EC7439E00431F2962DF9A6944779294955A9C4369615FFF04318B0053",
    ),
    "srcmap/intake.py": (
        9923,
        "CFD53B71649BEF84A166397AA18E39AC5E4EDF00DD860142B2936F886AB080B1",
    ),
    "srcmap/map.py": (
        27167,
        "57A92E34DB189E0EE95E6816074DB686C5616590C33DF823EF8EB9E9AFC2E1DF",
    ),
    "srcmap/scan.py": (
        3403,
        "269E4D2F73405BDA82F373F04AF0109431416FF25CCA874F0051D193BC444D30",
    ),
}

AUTHORIZED_DIRTY_PATHS = {
    ".gitattributes",
    "srcmap/build_tohoku_r9.py",
    "srcmap/intake.py",
    "srcmap/map.py",
    "srcmap/scan.py",
    "srcmap/start_build_tohoku_r9.ps1",
}
COPY_INPUTS = ("topics.csv", "dec.csv", "issues.csv")
PAYLOAD_FILES = {
    "STATUS.md",
    "cfg.json",
    "check.json",
    "dec.csv",
    "intake.json",
    "issues.csv",
    "map.csv",
    "mcheck.json",
    "stx.csv",
    "tcand.csv",
    "tmap.csv",
    "topics.csv",
    "ucand.csv",
    "units.csv",
}
MAP_TRANSACTION_FILES = {
    ".map.csv.tmp",
    ".ucand.csv.tmp",
    ".mcheck.json.tmp",
    ".mcheck.fail.tmp",
    ".map.txn.json",
    ".map.txn.tmp",
    ".map.bak",
    ".ucand.bak",
    ".mcheck.bak",
    ".map.restore.tmp",
    ".ucand.restore.tmp",
    ".mcheck.restore.tmp",
}
SNAPSHOT_RELATIVE_PATHS = {
    "sem/nodes.csv",
    "sem/edges.csv",
    "sem/terms.csv",
    "sem/stacks.csv",
    "sem/manifest.json",
    "sem/validation.json",
    "qa/sem-input.json",
    "qa/sem-check.json",
    "authority/part_i.pdf",
    "authority/part_ii.pdf",
    "source/cfg.json",
    "source/topics.csv",
    "source/dec.csv",
    "source/issues.csv",
    "source/units.csv",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256(path)


def identity_dict(path: Path, name: str | None = None) -> dict[str, object]:
    size, digest = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": digest}


def record(path: Path, name: str | None = None) -> dict[str, object]:
    return identity_dict(path, name)


def json_bytes(value: object) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def strict_json(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf") or b"\r" in raw or not raw.endswith(b"\n"):
        raise RuntimeError(f"Noncanonical JSON bytes: {path}")

    def no_duplicates(items: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in items:
            if key in result:
                raise RuntimeError(f"Duplicate JSON key in {path}: {key}")
            result[key] = value
        return result

    value = json.loads(raw.decode("utf-8"), object_pairs_hook=no_duplicates)
    if not isinstance(value, dict):
        raise RuntimeError(f"JSON root is not an object: {path}")
    return value


def exclusive_write(path: Path, data: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    if path.read_bytes() != data:
        raise RuntimeError(f"Exclusive write readback mismatch: {path}")


def is_reparse(path: Path) -> bool:
    info = os.lstat(path)
    return bool(getattr(info, "st_file_attributes", 0) & 0x400)


def require_plain_file(path: Path) -> None:
    absolute = path.absolute()
    if not absolute.exists() or not stat.S_ISREG(os.lstat(absolute).st_mode):
        raise RuntimeError(f"Required ordinary file is absent: {absolute}")
    current = absolute
    while True:
        if is_reparse(current):
            raise RuntimeError(f"Reparse path is forbidden: {current}")
        if current.parent == current:
            break
        current = current.parent


def require_plain_directory(path: Path) -> None:
    absolute = path.absolute()
    if not absolute.exists() or not stat.S_ISDIR(os.lstat(absolute).st_mode):
        raise RuntimeError(f"Required ordinary directory is absent: {absolute}")
    current = absolute
    while True:
        if is_reparse(current):
            raise RuntimeError(f"Reparse directory is forbidden: {current}")
        if current.parent == current:
            break
        current = current.parent


def tree_relative_files(root: Path) -> set[str]:
    require_plain_directory(root)
    files: set[str] = set()
    stack = [root]
    while stack:
        directory = stack.pop()
        for item in os.scandir(directory):
            item_path = Path(item.path)
            if is_reparse(item_path):
                raise RuntimeError(f"Reparse entry is forbidden: {item_path}")
            relative = item_path.relative_to(root).as_posix()
            if item.is_dir(follow_symlinks=False):
                stack.append(item_path)
            elif item.is_file(follow_symlinks=False):
                files.add(relative)
            else:
                raise RuntimeError(f"Unsupported filesystem entry: {item_path}")
    return files


def tree_directories(root: Path) -> set[Path]:
    require_plain_directory(root)
    directories: set[Path] = set()
    stack = [root]
    while stack:
        directory = stack.pop()
        for item in os.scandir(directory):
            item_path = Path(item.path)
            if is_reparse(item_path):
                raise RuntimeError(f"Reparse entry is forbidden: {item_path}")
            if item.is_dir(follow_symlinks=False):
                directories.add(item_path)
                stack.append(item_path)
            elif not item.is_file(follow_symlinks=False):
                raise RuntimeError(f"Unsupported filesystem entry: {item_path}")
    return directories


@contextlib.contextmanager
def deny_write_delete(paths: list[Path]) -> Iterator[None]:
    """Hold Windows read handles that deny write/delete for the whole build."""
    if os.name != "nt":
        raise RuntimeError("The frozen dossier transaction requires Windows locks")
    import ctypes
    from ctypes import wintypes

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_file = kernel32.CreateFileW
    create_file.argtypes = [
        wintypes.LPCWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.HANDLE,
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
                str(path),
                0x80000000,  # GENERIC_READ
                0x00000001,  # FILE_SHARE_READ only
                None,
                3,  # OPEN_EXISTING
                0x00000080,  # FILE_ATTRIBUTE_NORMAL
                None,
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
    """Create and hold one zero-share lock for the entire transaction."""
    if os.name != "nt":
        raise RuntimeError("The frozen dossier transaction requires Windows locks")
    import ctypes
    from ctypes import wintypes

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    create_file = kernel32.CreateFileW
    create_file.argtypes = [
        wintypes.LPCWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.HANDLE,
    ]
    create_file.restype = wintypes.HANDLE
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL
    mutex_path = Path(run_git("rev-parse", "--git-path", "tohoku-r9-dossier.lock"))
    if not mutex_path.is_absolute():
        mutex_path = ROOT / mutex_path
    mutex_path.parent.mkdir(parents=True, exist_ok=True)
    handle = create_file(
        str(mutex_path),
        0xC0000000,  # GENERIC_READ | GENERIC_WRITE
        0,  # no sharing
        None,
        4,  # OPEN_ALWAYS
        0x00000100,  # FILE_FLAG_DELETE_ON_CLOSE
        None,
    )
    invalid = ctypes.c_void_p(-1).value
    if handle in (None, invalid):
        raise RuntimeError("Another Tohoku r9 dossier transaction is active")
    try:
        yield
    finally:
        close_handle(handle)


def run_git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=True, encoding="utf-8"
    ).strip()


def status_paths() -> set[str]:
    # Do not strip the output: porcelain's two status columns are significant,
    # including the leading blank in the first row.
    rows = subprocess.check_output(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
    ).splitlines()
    return {row[3:].replace("\\", "/") for row in rows if row}


def require_scanned_tree_matches_head() -> None:
    changed = {
        path.replace("\\", "/")
        for path in run_git("diff", "--name-only", "HEAD", "--", "*.tex", "tags/tags")
        .splitlines()
        if path
    }
    if changed:
        raise RuntimeError(f"Stacks TeX/tag scan inputs differ from HEAD: {sorted(changed)}")


def require_git_baseline() -> str:
    paths = status_paths()
    reserved = {
        path
        for path in paths
        if path.startswith(".tohoku-r9-txn/") or path.startswith("tohoku_r9/")
    }
    if paths - reserved != AUTHORIZED_DIRTY_PATHS:
        raise RuntimeError(f"Unexpected Stacks worktree surface: {sorted(paths)}")
    if run_git("branch", "--show-current") != EXPECTED_BRANCH:
        raise RuntimeError("Stacks branch drift")
    if run_git("rev-parse", "HEAD") != EXPECTED_HEAD:
        raise RuntimeError("Stacks HEAD drift")
    if run_git("rev-parse", "HEAD^{tree}") != EXPECTED_TREE:
        raise RuntimeError("Stacks tree drift")
    if run_git("rev-parse", "@{upstream}") != EXPECTED_HEAD:
        raise RuntimeError("Local upstream-tracking ref drift")
    if run_git("rev-list", "--left-right", "--count", "HEAD...@{upstream}") != "0\t0":
        raise RuntimeError("Local branch and upstream-tracking ref differ")
    require_scanned_tree_matches_head()
    return run_git("status", "--porcelain=v1", "--untracked-files=no")


def validate_helper_snapshot() -> dict[str, object]:
    value = globals().get("__verified_helper_snapshot__")
    if not isinstance(value, dict) or set(value) != {
        "path", "bytes", "sha256", "contract"
    }:
        raise RuntimeError("Missing exact launcher attestation")
    if (
        value.get("path") != "srcmap/build_tohoku_r9.py"
        or type(value.get("bytes")) is not int
        or not re.fullmatch(r"[0-9A-F]{64}", str(value.get("sha256", "")))
        or value.get("contract") != "one_read_hash_then_exec_same_bytes"
    ):
        raise RuntimeError("Invalid launcher attestation")
    if identity(Path(__file__)) != (value["bytes"], value["sha256"]):
        raise RuntimeError("Helper path bytes differ from executed launcher snapshot")
    return dict(value)


def validate_envelope_snapshot() -> dict[str, object]:
    value = globals().get("__verified_envelope_snapshot__")
    expected_path = "srcmap/start_build_tohoku_r9.ps1"
    if not isinstance(value, dict) or set(value) != {
        "path", "bytes", "sha256", "contract"
    }:
        raise RuntimeError("Missing launcher-envelope attestation")
    if (
        value.get("path") != expected_path
        or type(value.get("bytes")) is not int
        or not re.fullmatch(r"[0-9A-F]{64}", str(value.get("sha256", "")))
        or value.get("contract") != "self_read_hash_before_helper_exec"
    ):
        raise RuntimeError("Invalid launcher-envelope attestation")
    if identity(ROOT / expected_path) != (value["bytes"], value["sha256"]):
        raise RuntimeError("Launcher envelope drift")
    return dict(value)


def expected_owner(
    helper: dict[str, object], envelope: dict[str, object]
) -> dict[str, object]:
    return {
        "schema": "tohoku-r9-dossier-transaction-owner-v1",
        "generation": "tohoku_r9",
        "git_head": EXPECTED_HEAD,
        "git_tree": EXPECTED_TREE,
        "helper": helper,
        "envelope": envelope,
        "tools": {
            name: {"bytes": value[0], "sha256": value[1]}
            for name, value in sorted(EXPECTED_TOOL_IDENTITIES.items())
        },
        "sem_input": {
            "bytes": EXPECTED_SEM_INPUT[0],
            "sha256": EXPECTED_SEM_INPUT[1],
        },
        "sem_check": {
            "bytes": EXPECTED_SEM_CHECK[0],
            "sha256": EXPECTED_SEM_CHECK[1],
        },
    }


def owner_without_envelope(owner: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in owner.items() if key != "envelope"}


def owner_equivalent(
    actual: dict[str, object], expected: dict[str, object]
) -> bool:
    """Allow only launcher self-hash drift across an interrupted retry."""
    return owner_without_envelope(actual) == owner_without_envelope(expected)


def validate_tool_identities() -> dict[str, dict[str, object]]:
    if not EXPECTED_TOOL_IDENTITIES:
        raise RuntimeError("Successor tool identities are not frozen")
    output: dict[str, dict[str, object]] = {}
    for relative, expected in sorted(EXPECTED_TOOL_IDENTITIES.items()):
        path = ROOT / relative
        require_plain_file(path)
        if identity(path) != expected:
            raise RuntimeError(f"Frozen successor tool drift: {relative}")
        output[relative] = record(path, relative)
    return output


def transaction_allowed_files() -> set[str]:
    return {
        "OWNER.json",
        *{f"inputs/{name}" for name in SNAPSHOT_RELATIVE_PATHS},
        *{f"tohoku_r9/{name}" for name in PAYLOAD_FILES},
        "tohoku_r9/r9-check.json",
        *{f"tohoku_r9/{name}" for name in MAP_TRANSACTION_FILES},
    }


def clean_owned_transaction(owner: dict[str, object]) -> None:
    if not TXN_ROOT.exists():
        return
    files = tree_relative_files(TXN_ROOT)
    if not files:
        for directory in sorted(
            tree_directories(TXN_ROOT), key=lambda path: len(path.parts), reverse=True
        ):
            directory.rmdir()
        TXN_ROOT.rmdir()
        return
    if files == {"OWNER.json"}:
        raw = OWNER_PATH.read_bytes()
        if raw != json_bytes(owner):
            # A crash during the exclusive owner write leaves no payload and is
            # safe to discard; any payload would require the exact marker.
            for directory in sorted(
                tree_directories(TXN_ROOT),
                key=lambda path: len(path.parts),
                reverse=True,
            ):
                directory.rmdir()
            OWNER_PATH.unlink()
            TXN_ROOT.rmdir()
            return
    if "OWNER.json" not in files:
        raise RuntimeError("Unowned or mismatched Tohoku r9 transaction is preserved")
    try:
        actual_owner = strict_json(OWNER_PATH)
    except Exception as exc:
        raise RuntimeError("Unreadable Tohoku r9 transaction owner is preserved") from exc
    if not owner_equivalent(actual_owner, owner):
        raise RuntimeError("Unowned or mismatched Tohoku r9 transaction is preserved")
    unexpected = files - transaction_allowed_files()
    if unexpected:
        raise RuntimeError(
            f"Unexpected owned-transaction surface is preserved: {sorted(unexpected)}"
        )
    # Delete the already-validated derivative payload bottom-up. OWNER stays
    # until the payload is gone, so every crash state remains attributable.
    directories: set[Path] = tree_directories(TXN_ROOT)
    for relative in files - {"OWNER.json"}:
        parent = (TXN_ROOT / relative).parent
        while parent != TXN_ROOT:
            directories.add(parent)
            parent = parent.parent
    ordered_directories = sorted(
        directories,
        key=lambda path: len(path.parts),
        reverse=True,
    )
    for relative in sorted(files - {"OWNER.json"}):
        (TXN_ROOT / relative).unlink()
    for directory in ordered_directories:
        if directory.exists():
            directory.rmdir()
    OWNER_PATH.unlink()
    TXN_ROOT.rmdir()
    if TXN_ROOT.exists():
        raise RuntimeError("Owned transaction cleanup did not complete")


def prepare_transaction(owner: dict[str, object]) -> None:
    clean_owned_transaction(owner)
    TXN_ROOT.mkdir()
    exclusive_write(OWNER_PATH, json_bytes(owner))
    SNAPSHOT_DIR.mkdir()
    STAGE_DIR.mkdir()


def snapshot_specs() -> dict[str, Path]:
    return {
        "sem/nodes.csv": SEM / "nodes.csv",
        "sem/edges.csv": SEM / "edges.csv",
        "sem/terms.csv": SEM / "terms.csv",
        "sem/stacks.csv": SEM / "stacks.csv",
        "sem/manifest.json": SEM / "manifest.json",
        "sem/validation.json": SEM / "validation.json",
        "qa/sem-input.json": QA / "sem-input.json",
        "qa/sem-check.json": QA / "sem-check.json",
        "authority/part_i.pdf": AUTHORITY / "jstage_part_I_9_2_119.pdf",
        "authority/part_ii.pdf": AUTHORITY / "jstage_part_II_9_3_185.pdf",
        "source/cfg.json": SOURCE_DIR / "cfg.json",
        "source/topics.csv": SOURCE_DIR / "topics.csv",
        "source/dec.csv": SOURCE_DIR / "dec.csv",
        "source/issues.csv": SOURCE_DIR / "issues.csv",
        "source/units.csv": SOURCE_DIR / "units.csv",
    }


def create_snapshots() -> None:
    specs = snapshot_specs()
    if set(specs) != SNAPSHOT_RELATIVE_PATHS:
        raise RuntimeError("Internal snapshot surface mismatch")
    for relative, source in sorted(specs.items()):
        target = SNAPSHOT_DIR / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        data = source.read_bytes()
        exclusive_write(target, data)
        if identity(target) != identity(source):
            raise RuntimeError(f"Snapshot identity mismatch: {relative}")


def verify_semantic_receipts() -> None:
    if identity(QA / "sem-input.json") != EXPECTED_SEM_INPUT:
        raise RuntimeError("Frozen sem-input identity drift")
    if identity(QA / "sem-check.json") != EXPECTED_SEM_CHECK:
        raise RuntimeError("Frozen sem-check identity drift")
    validation = strict_json(SEM / "validation.json")
    check = strict_json(QA / "sem-check.json")
    if validation.get("status") != "PASS" or validation.get("errors") != []:
        raise RuntimeError("sem/r9 validation is not PASS")
    if check.get("status") != "PASS" or check.get("errors") != []:
        raise RuntimeError("sem/r9 check is not PASS")
    expected_input = {
        "name": "qa/v68r21/sem-input.json",
        "bytes": EXPECTED_SEM_INPUT[0],
        "sha256": EXPECTED_SEM_INPUT[1],
    }
    if check.get("input_manifest") != expected_input:
        raise RuntimeError("sem-check does not bind the frozen sem-input")
    surface = check.get("semantic_surface")
    if not isinstance(surface, dict):
        raise RuntimeError("sem-check lacks semantic_surface")
    if (
        surface.get("file_count"),
        surface.get("bytes"),
        surface.get("aggregate_sha256"),
    ) != EXPECTED_R9_SURFACE:
        raise RuntimeError("sem/r9 receipt surface mismatch")
    expected_files = surface.get("files")
    if not isinstance(expected_files, list) or any(
        not isinstance(item, dict) for item in expected_files
    ):
        raise RuntimeError("sem/r9 receipt lacks exact file records")
    actual_names = sorted(path.name for path in SEM.iterdir() if path.is_file())
    if actual_names != sorted(str(item.get("name", "")) for item in expected_files):
        raise RuntimeError("sem/r9 live filename surface mismatch")
    actual_records = [record(SEM / str(item["name"])) for item in expected_files]
    if actual_records != expected_files:
        raise RuntimeError("sem/r9 live file identity mismatch")
    payload = b"".join(
        item["name"].encode("utf-8")
        + b"\0"
        + str(item["bytes"]).encode("ascii")
        + b"\0"
        + item["sha256"].encode("ascii")
        + b"\n"
        for item in sorted(actual_records, key=lambda value: value["name"])
    )
    if hashlib.sha256(payload).hexdigest().upper() != EXPECTED_R9_SURFACE[2]:
        raise RuntimeError("sem/r9 live aggregate mismatch")


def build_config() -> dict[str, object]:
    cfg = strict_json(SNAPSHOT_DIR / "source" / "cfg.json")
    inputs = cfg.get("inputs")
    if not isinstance(inputs, dict):
        raise RuntimeError("Source configuration lacks inputs")
    inputs["primary"] = {
        **record(SNAPSHOT_DIR / "sem" / "nodes.csv", "nodes.csv"),
        "filename": "nodes.csv",
        "source_file": "sem/r9/nodes.csv",
    }
    for key, filename in (
        ("edges", "edges.csv"),
        ("terms", "terms.csv"),
        ("stacks", "stacks.csv"),
    ):
        inputs[key] = {
            **record(SNAPSHOT_DIR / "sem" / filename, filename),
            "filename": filename,
        }
    inputs["sem_manifest"] = {
        **record(SNAPSHOT_DIR / "sem" / "manifest.json", "sem/r9 manifest"),
        "filename": "manifest.json",
    }
    inputs["sem_validation"] = {
        **record(SNAPSHOT_DIR / "sem" / "validation.json", "sem/r9 validation"),
        "filename": "validation.json",
    }
    inputs["sem_input"] = {
        **record(SNAPSHOT_DIR / "qa" / "sem-input.json", "v68r21 sem input"),
        "filename": "sem-input.json",
    }
    inputs["sem_check"] = {
        **record(SNAPSHOT_DIR / "qa" / "sem-check.json", "v68r21 sem check"),
        "filename": "sem-check.json",
    }
    inputs["part_i"] = {
        **record(SNAPSHOT_DIR / "authority" / "part_i.pdf", "J-STAGE Part I"),
        "filename": "part_i.pdf",
    }
    inputs["part_ii"] = {
        **record(SNAPSHOT_DIR / "authority" / "part_ii.pdf", "J-STAGE Part II"),
        "filename": "part_ii.pdf",
    }
    cfg["required_extra_keys"] = [
        "part_i",
        "part_ii",
        "edges",
        "terms",
        "stacks",
        "sem_manifest",
        "sem_validation",
        "sem_input",
        "sem_check",
    ]
    cfg["dossier_id"] = "tohoku_r9"
    cfg["integration_base"] = EXPECTED_HEAD
    for rule in cfg["topic_rules"]:
        if rule.get("topic_id") == "ext":
            rule["pattern"] = r"\bExt\b|extension"
    cfg["semantic_successor"] = {
        "generation": "sem/r9",
        "surface_files": EXPECTED_R9_SURFACE[0],
        "surface_bytes": EXPECTED_R9_SURFACE[1],
        "surface_sha256": EXPECTED_R9_SURFACE[2],
        "receipt": record(
            SNAPSHOT_DIR / "qa" / "sem-check.json", "qa/v68r21/sem-check.json"
        ),
    }
    cfg["stacks_baseline"] = {
        "branch": EXPECTED_BRANCH,
        "commit": EXPECTED_HEAD,
        "tree": EXPECTED_TREE,
        "remote_server_freshness_verified": False,
    }
    return cfg


def write_json(path: Path, value: object) -> None:
    exclusive_write(path, json_bytes(value))


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        if any(None in row or any(value is None for value in row.values()) for row in rows):
            raise RuntimeError(f"Malformed CSV row: {path}")
        return rows


def run_tool(script: str, *args: str) -> None:
    relative = f"srcmap/{script}"
    expected = EXPECTED_TOOL_IDENTITIES[relative]
    if identity(ROOT / relative) != expected:
        raise RuntimeError(f"Tool drift before execution: {relative}")
    subprocess.run(
        [sys.executable, "-I", "-B", str(ROOT / relative), *args],
        cwd=ROOT,
        check=True,
    )
    if identity(ROOT / relative) != expected:
        raise RuntimeError(f"Tool drift after execution: {relative}")


def expected_extra_arguments() -> list[str]:
    values = [
        f"part_i={SNAPSHOT_DIR / 'authority' / 'part_i.pdf'}",
        f"part_ii={SNAPSHOT_DIR / 'authority' / 'part_ii.pdf'}",
        f"edges={SNAPSHOT_DIR / 'sem' / 'edges.csv'}",
        f"terms={SNAPSHOT_DIR / 'sem' / 'terms.csv'}",
        f"stacks={SNAPSHOT_DIR / 'sem' / 'stacks.csv'}",
        f"sem_manifest={SNAPSHOT_DIR / 'sem' / 'manifest.json'}",
        f"sem_validation={SNAPSHOT_DIR / 'sem' / 'validation.json'}",
        f"sem_input={SNAPSHOT_DIR / 'qa' / 'sem-input.json'}",
        f"sem_check={SNAPSHOT_DIR / 'qa' / 'sem-check.json'}",
    ]
    output: list[str] = []
    for value in values:
        output.extend(["--extra", value])
    return output


def unit_deltas(
    old_units: list[dict[str, str]], new_units: list[dict[str, str]]
) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    observed_topic_changes: dict[str, tuple[str, str]] = {}
    for old, new in zip(old_units, new_units, strict=True):
        for field in old:
            if old[field] != new[field] and field not in {
                "title_en", "source_file", "topics"
            }:
                raise RuntimeError(f"Unexpected generated unit delta: {new['id']} {field}")
        if old["source_file"] != "sem/r7/nodes.csv" or new["source_file"] != "sem/r9/nodes.csv":
            raise RuntimeError(f"Unexpected semantic source transition: {new['id']}")
        if old["title_en"] != new["title_en"]:
            output.append(
                {"id": new["id"], "old_title_en": old["title_en"], "new_title_en": new["title_en"]}
            )
        if old["topics"] != new["topics"]:
            observed_topic_changes[new["id"]] = (old["topics"], new["topics"])
    if len(output) != 17:
        raise RuntimeError(f"Expected 17 title changes, found {len(output)}")
    if observed_topic_changes != EXPECTED_TOPIC_CHANGES:
        raise RuntimeError("Generated topic changes differ from the exact Ext false-positive repair")
    return output


def verify_results(root: Path) -> list[dict[str, str]]:
    intake = strict_json(root / "intake.json")
    check = strict_json(root / "check.json")
    mcheck = strict_json(root / "mcheck.json")
    if intake.get("status") != "PASS" or intake.get("errors") != []:
        raise RuntimeError("r9 intake is not PASS")
    if check.get("status") != "PASS" or check.get("errors") != []:
        raise RuntimeError("r9 Stacks scan is not PASS")
    if check.get("integration_base") != EXPECTED_HEAD:
        raise RuntimeError("r9 Stacks scan does not bind the frozen HEAD")
    if (
        mcheck.get("status") != "PASS"
        or mcheck.get("errors") != []
        or mcheck.get("outputs_promoted") is not True
    ):
        raise RuntimeError("r9 source map is not PASS")
    units = load_csv(root / "units.csv")
    decisions = load_csv(root / "dec.csv")
    mapped = load_csv(root / "map.csv")
    old_units = load_csv(SOURCE_DIR / "units.csv")
    old_map = load_csv(SOURCE_DIR / "map.csv")
    if [row["id"] for row in units] != [row["id"] for row in old_units]:
        raise RuntimeError("r9 unit ID/order drift")
    changes = unit_deltas(old_units, units)
    if [row["decision_id"] for row in decisions] != [
        f"D{number:06d}" for number in range(1, 219)
    ]:
        raise RuntimeError("decision ledger is not the exact D000001..D000218 prefix")
    counts = mcheck.get("counts", {})
    expected = {
        "units": 990,
        "decisions": 218,
        "decided_units": 218,
        "review_units": 437,
        "candidate_units": 437,
    }
    if any(type(counts.get(key)) is not int or counts.get(key) != value for key, value in expected.items()):
        raise RuntimeError("r9 mapping counts drift")
    if sum(row["review_state"] == "needs_link_review" for row in mapped) != 23:
        raise RuntimeError("bibliography review count drift")
    if identity(root / "dec.csv") != EXPECTED_DEC:
        raise RuntimeError("decision ledger bytes drift")
    if identity(root / "issues.csv") != EXPECTED_ISSUES:
        raise RuntimeError("issue ledger bytes drift")
    old_by_id = {row["unit_id"]: row for row in old_map}
    fixed_fields = {
        "decision_id",
        "disposition",
        "review_state",
        "stacks_labels",
        "stacks_tags",
        "rationale",
    }
    for row in mapped:
        if not row["decision_id"]:
            continue
        old = old_by_id[row["unit_id"]]
        if any(row[field] != old[field] for field in fixed_fields):
            raise RuntimeError(f"Reviewed mapping decision drift: {row['unit_id']}")
    return changes


def write_status() -> None:
    text = """# Tohoku sem/r9 mapping status

- Semantic source: the independently validated local-unpublished `sem/r9` successor.
- Source inventory: 990 stable units; all identifiers and their order match the preserved dossier.
- Preserved reviewed work: `D000001`--`D000218` remain byte-identical and resolve to the same units.
- Current Stacks scan: regenerated from the exact TeX/tag tree of commit `952bb0e39acfa050db054d7ae7ea91c51487b7a9`; only the allowlisted dossier tools differed in the worktree.
- Current mapping receipt: `mcheck.json` is `PASS`, `errors=[]`, and `outputs_promoted=true`.
- Remaining work: 437 mathematical units and 23 bibliography links require direct statement-level review.
- Two active Chapter III diagram/source issues remain recorded in `issues.csv`.
- This dossier is a local mapping checkpoint. It does not authorize release, publication, DOI/Zenodo mutation, Git push, rights conclusions, or whole-paper completion.
"""
    exclusive_write(STAGE_DIR / "STATUS.md", text.encode("utf-8"))


def source_surface() -> list[dict[str, object]]:
    return [record(path, path.name) for path in sorted(SOURCE_DIR.iterdir(), key=lambda item: item.name) if path.is_file()]


def expected_static_receipt_fields(
    helper: dict[str, object],
    envelope: dict[str, object],
    tools: dict[str, dict[str, object]],
    source_before: list[dict[str, object]],
    title_changes: list[dict[str, str]],
    root: Path,
) -> dict[str, object]:
    return {
        "schema": "tohoku-stacks-sem-r9-dossier-v1",
        "status": "PASS",
        "errors": [],
        "git": {
            "branch": EXPECTED_BRANCH,
            "head": EXPECTED_HEAD,
            "tree": EXPECTED_TREE,
            "local_upstream_tracking_ref": EXPECTED_HEAD,
            "ahead": 0,
            "behind": 0,
            "worktree_clean_before_generation": False,
            "authorized_dossier_tool_changes_only": True,
            "scanned_tex_and_tags_match_head": True,
            "remote_server_freshness_verified": False,
        },
        "semantic_source": {
            "generation": "sem/r9",
            "surface_files": EXPECTED_R9_SURFACE[0],
            "surface_bytes": EXPECTED_R9_SURFACE[1],
            "surface_sha256": EXPECTED_R9_SURFACE[2],
            "sem_input": record(QA / "sem-input.json", "qa/v68r21/sem-input.json"),
            "sem_check": record(QA / "sem-check.json", "qa/v68r21/sem-check.json"),
        },
        "execution": {
            "helper": helper,
            "envelope": envelope,
            "dependencies": tools,
            "dependency_contract": "locked_read_only_and_identity_checked_before_and_after_execution",
            "python_runtime_byte_attested": False,
        },
        "authority": {
            "part_i": record(AUTHORITY / "jstage_part_I_9_2_119.pdf"),
            "part_ii": record(AUTHORITY / "jstage_part_II_9_3_185.pdf"),
        },
        "preserved_source_dossier": source_before,
        "preserved_ledgers": {
            "dec.csv": record(root / "dec.csv"),
            "issues.csv": record(root / "issues.csv"),
        },
        "title_changes": title_changes,
        "counts": {
            "units": 990,
            "decisions": 218,
            "remaining_mathematical_units": 437,
            "remaining_bibliography_links": 23,
        },
        "files": [record(root / name) for name in sorted(PAYLOAD_FILES)],
        "nonclaims": [
            "No Git commit or push has been made by this receipt.",
            "No remote-server freshness check was performed.",
            "No release, publication, DOI, Zenodo, rights, or whole-paper gate is closed.",
            "The remaining mathematical and bibliography review is not complete.",
        ],
    }


def write_receipt(
    helper: dict[str, object],
    envelope: dict[str, object],
    tools: dict[str, dict[str, object]],
    title_changes: list[dict[str, str]],
    source_before: list[dict[str, object]],
) -> None:
    receipt = expected_static_receipt_fields(
        helper, envelope, tools, source_before, title_changes, STAGE_DIR
    )
    write_json(STAGE_DIR / "r9-check.json", receipt)


def verify_committed_target(
    helper: dict[str, object],
    envelope: dict[str, object],
    tools: dict[str, dict[str, object]],
    source_before: list[dict[str, object]],
) -> dict[str, object]:
    files = tree_relative_files(TARGET_DIR)
    expected = PAYLOAD_FILES | {"r9-check.json"}
    if files != expected:
        raise RuntimeError(f"Committed dossier surface mismatch: {sorted(files)}")
    receipt = strict_json(TARGET_DIR / "r9-check.json")
    if receipt.get("schema") != "tohoku-stacks-sem-r9-dossier-v1" or receipt.get("status") != "PASS" or receipt.get("errors") != []:
        raise RuntimeError("Committed dossier receipt is not PASS")
    actual_files = [record(TARGET_DIR / name) for name in sorted(PAYLOAD_FILES)]
    if receipt.get("files") != actual_files:
        raise RuntimeError("Committed dossier receipt/file mismatch")
    title_changes = verify_results(TARGET_DIR)
    if receipt != expected_static_receipt_fields(
        helper, envelope, tools, source_before, title_changes, TARGET_DIR
    ):
        raise RuntimeError("Committed dossier receipt differs from exact replay")
    return receipt


def lock_paths() -> list[Path]:
    return [
        Path(__file__),
        ROOT / "srcmap" / "start_build_tohoku_r9.ps1",
        *[ROOT / name for name in EXPECTED_TOOL_IDENTITIES],
        *snapshot_specs().values(),
        *[path for path in SEM.iterdir() if path.is_file()],
        *[path for path in SOURCE_DIR.iterdir() if path.is_file()],
        *sorted(ROOT.glob("*.tex"), key=lambda path: path.name),
        ROOT / "tags" / "tags",
    ]


def main() -> int:
    helper = validate_helper_snapshot()
    envelope = validate_envelope_snapshot()
    tools = validate_tool_identities()
    with single_writer_mutex():
        return main_locked(helper, envelope, tools)


def main_locked(
    helper: dict[str, object],
    envelope: dict[str, object],
    tools: dict[str, dict[str, object]],
) -> int:
    tracked_status = require_git_baseline()
    owner = expected_owner(helper, envelope)
    with deny_write_delete(lock_paths()):
        # All hashes and consumed inputs are now stable until the receipt and
        # promoted target have been independently replayed.
        if (
            validate_helper_snapshot() != helper
            or validate_envelope_snapshot() != envelope
            or validate_tool_identities() != tools
        ):
            raise RuntimeError("Execution identity drift after lock acquisition")
        verify_semantic_receipts()
        for key, path in (
            ("part_i", AUTHORITY / "jstage_part_I_9_2_119.pdf"),
            ("part_ii", AUTHORITY / "jstage_part_II_9_3_185.pdf"),
        ):
            if identity(path) != EXPECTED_AUTHORITY[key]:
                raise RuntimeError(f"Authority identity drift: {key}")
        source_before = source_surface()
        if TARGET_DIR.exists():
            receipt = verify_committed_target(helper, envelope, tools, source_before)
            clean_owned_transaction(owner)
            print(json.dumps(receipt, ensure_ascii=False, indent=2))
            return 0

        prepare_transaction(owner)
        create_snapshots()
        write_json(STAGE_DIR / "cfg.json", build_config())
        for name in COPY_INPUTS:
            source = SNAPSHOT_DIR / "source" / name
            target = STAGE_DIR / name
            exclusive_write(target, source.read_bytes())
        intake_args = [
            str(STAGE_DIR),
            str(SNAPSHOT_DIR / "sem" / "nodes.csv"),
            *expected_extra_arguments(),
        ]
        run_tool("intake.py", *intake_args)
        run_tool("scan.py", str(STAGE_DIR))
        run_tool("map.py", str(STAGE_DIR))
        title_changes = verify_results(STAGE_DIR)
        write_status()
        write_receipt(helper, envelope, tools, title_changes, source_before)

        if run_git("status", "--porcelain=v1", "--untracked-files=no") != tracked_status:
            raise RuntimeError("Tracked Stacks files changed during isolated generation")
        require_scanned_tree_matches_head()
        if validate_tool_identities() != tools:
            raise RuntimeError("Successor tool identity drift at end of generation")
        verify_semantic_receipts()
        if source_surface() != source_before:
            raise RuntimeError("Preserved Tohoku dossier changed during generation")

        os.rename(STAGE_DIR, TARGET_DIR)
        receipt = verify_committed_target(helper, envelope, tools, source_before)
        clean_owned_transaction(owner)
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
