#!/usr/bin/env python3
"""Build the no-overwrite Tohoku Stacks mapping successor for D000927--D000928."""

from __future__ import annotations

import contextlib
import csv
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from collections import Counter
from collections.abc import Iterator
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r14"
TARGET = ROOT / "tohoku_r15"
STAGE = ROOT / ".tohoku-r15-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r10"
QA = PROJECT / "qa" / "v68r24"
AUTHORITY = PROJECT / "authority_snapshot"

EXPECTED_GIT_NONCLAIM = {
    "inspection_performed": False,
    "reason": "Workspace machine-safety policy forbids repository-wide Git inspection.",
    "predecessor_receipt": {
        "path": "tohoku_r14/r14-check.json",
        "bytes": 14861,
        "sha256": "10F772E07A4A80139DB0CB84797B331B1A214774A0A39212D88C3ED6819139D6",
    },
    "remote_server_freshness_verified": False,
}

EXPECTED_SOURCE = {
    "cfg.json": (5193, "2ECDA97904D4618D5D1B94DFD4EA4C222A669D2D4BD1A634667FE1FAC7C9F137"),
    "check.json": (69900, "A0BFDD90DD5593532AFE84F9ECE9CD1B0CC350BE4AD1004255030E16450514C0"),
    "dec.csv": (313502, "D411C9893C7245A6B4DE3D19424341214E842431BB4F38C0E6475B26FB0B32A3"),
    "intake.json": (1877, "86273E19DB8A912BF9558DE007EF4A39C9C7FB93EBEA64A85D31A4F4A4BE42F2"),
    "issues.csv": (15036, "16DD4BCA450F4030F9EF3FE6F6A3C51CF64BEE81CE59F56AF141D572CB1C4328"),
    "map.csv": (452194, "6DCA94080678C9D2D0ED061ED03963075264B88948A99446E64020D0F98B609E"),
    "mcheck.json": (59729, "FC76787F0E37EC1AE5E4C39D7FCF95A4FE904C303301611276468E20D711BB9F"),
    "r14-check.json": (14861, "10F772E07A4A80139DB0CB84797B331B1A214774A0A39212D88C3ED6819139D6"),
    "STATUS.md": (532, "DDDA09EF3256291792E21E6F8C6DE730E1BA26580626F8B8D74AAF3F57335836"),
    "stx.csv": (5256253, "BF29A52D2B9DDB3B59BB5A2C447E3DDA8184CB47E6650313638EE9F486CE4520"),
    "tcand.csv": (472536, "3D74F3C59DE7094BC46EEF259256C22333A518DC851EDDEED830FAF3B10D66A9"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (391651, "E65D82E4B014B283485CAE6EFC4639E4275467BAEC0A45A15CB81759CA3D1040"),
}

EXPECTED_TOOLS = {
    "srcmap/intake.py": (9923, "CFD53B71649BEF84A166397AA18E39AC5E4EDF00DD860142B2936F886AB080B1"),
    "srcmap/scan.py": (3403, "269E4D2F73405BDA82F373F04AF0109431416FF25CCA874F0051D193BC444D30"),
    "srcmap/map.py": (27167, "57A92E34DB189E0EE95E6816074DB686C5616590C33DF823EF8EB9E9AFC2E1DF"),
    "fga/mkidx.py": (14844, "4425B5D021B3E35371DEBB567881697F88DF6F533ACFC9783A749CE1A5176A6B"),
    "fga/mkmap.py": (22213, "7281F57EC7439E00431F2962DF9A6944779294955A9C4369615FFF04318B0053"),
    "fga/__pycache__/mkidx.cpython-313.pyc": (21123, "A78A1E45C6EB3960139B1D2A8AF42E5B10768034F0A87274448EBA69779BD424"),
    "fga/__pycache__/mkmap.cpython-313.pyc": (26471, "1AA6B79FFE873AB6C2E58FF2A9826DE6FDB6B1DD69A8D3473FD5F56168F2077D"),
    "tags/tags": (991506, "C5C7017FB5C50B60295B30801CA1B5BAB8F5B379F61B084D8219441938125FCF"),
}

EXPECTED_QA = {
    "sem-input.json": (299780, "42437BDDF7BE9AAB14869FD4B1F741191C8BCC9EDE1FFCDA3EB04964F8F1FB26"),
    "sem-check.json": (6395, "A425DDAA035F9E00D01579039F0E3786BCB0B52B079D614A7421D8828D837ADB"),
}

EXPECTED_AUTHORITY = {
    "jstage_part_I_9_2_119.pdf": (7305283, "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF"),
    "jstage_part_II_9_3_185.pdf": (3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53"),
}

EXPECTED_ARTIFACTS = {
    "cohomology.tex": (763989, "44104D421E84A0F4F922EA9F1979E01F630C0DB38501C3EEF4509F8C10A71B55"),
    "cohomology.log": (47224, "D5EDDD6F4A231F7F1E550418D657898E9552B4426F9790F94DA99CC19FD85645"),
    "cohomology.pdf": (1747367, "F364D66FB6E50F15424E60D49B16F6D5ADA4807D265E82114DCE95B0DEB40FC5"),
}

NEW_LABELS = {
    "cohomology-definition-equivariant-ext",
    "cohomology-lemma-equivariant-ext-properties",
    "cohomology-lemma-localize-equivariant-ext",
    "cohomology-lemma-equivariant-ext-slice",
}

DECISION_ROWS = [
    {
        "decision_id": "D000927",
        "unit_id": "tohoku:definition:equivariant-ext",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-definition-equivariant-ext",
        "rationale": (
            "Stacks now defines the group-valued and sheaf-valued equivariant Ext "
            "functors as the right derived functors of h_{O,G,A} and bold h_{O,G,A}, "
            "giving exactly formulas (5.6.6) and the authority-corrected (5.6.7). The "
            "global functor carries the argument X, while the sheaf-valued functor does "
            "not. No functoriality, locality, stalk, acyclicity, or spectral-sequence "
            "claim is included."
        ),
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000606",
    },
    {
        "decision_id": "D000928",
        "unit_id": "tohoku:property:equivariant-ext-functoriality",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": (
            "cohomology-definition-equivariant-ext;"
            "cohomology-lemma-equivariant-ext-properties;"
            "cohomology-lemma-localize-equivariant-ext;"
            "cohomology-lemma-equivariant-ext-slice"
        ),
        "rationale": (
            "Stacks now proves that, for fixed A, the global and sheaf-valued "
            "equivariant Ext families are universal cohomological delta functors in B "
            "and recover the corresponding equivariant Hom functors in degree zero; "
            "identifies the global groups with Ext in Mod_G(O); proves that both "
            "families are contravariant cohomological delta functors in A for fixed B; "
            "proves the local restriction isomorphism (5.6.8) on every open U in Y; and "
            "proves the induced-slice reduction, so for a discontinuous action the local "
            "computation reduces to the finite stabilizer G_x. This is in the inherited "
            "commutative G-ringed-space setting. No stalk-to-fiber comparison, Lemma "
            "5.6.1 acyclicity, or later spectral-sequence claim is included."
        ),
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000626",
    },
]

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
    return load_csv_bytes(path.read_bytes(), str(path))


def load_csv_bytes(data: bytes, source: str = "memory") -> tuple[list[str], list[dict[str, str]]]:
    if b"\r" in data or not data.endswith(b"\n"):
        raise RuntimeError(f"Noncanonical CSV: {source}")
    reader = csv.DictReader(data.decode("utf-8-sig").splitlines())
    rows = list(reader)
    if reader.fieldnames is None or any(None in row or None in row.values() for row in rows):
        raise RuntimeError(f"Malformed CSV: {source}")
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


@contextlib.contextmanager
def deny_write_delete(paths: list[Path]) -> Iterator[None]:
    """Hold Windows read handles that deny write and delete."""
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
    create_file = kernel32.CreateFileW
    create_file.argtypes = [
        wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID,
        wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE,
    ]
    create_file.restype = wintypes.HANDLE
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL
    dotgit = ROOT / ".git"
    if not dotgit.is_file():
        raise RuntimeError("Expected explicit .git worktree pointer is absent")
    pointer = dotgit.read_text(encoding="utf-8").strip()
    if not pointer.startswith("gitdir: "):
        raise RuntimeError("Malformed explicit .git worktree pointer")
    mutex = Path(pointer.removeprefix("gitdir: ")) / "tohoku-r15-dossier.lock"
    if not mutex.parent.is_dir():
        raise RuntimeError("Resolved explicit worktree Git directory is absent")
    mutex.parent.mkdir(parents=True, exist_ok=True)
    handle = create_file(str(mutex), 0xC0000000, 0, None, 4, 0x00000100, None)
    invalid = ctypes.c_void_p(-1).value
    if handle in (None, invalid):
        raise RuntimeError("Another Tohoku r15 transaction is active")
    try:
        yield
    finally:
        close_handle(handle)


def sem_records() -> list[dict[str, object]]:
    check = strict_json(QA / "sem-check.json")
    surface = check.get("semantic_surface")
    if not isinstance(surface, dict) or (
        surface.get("file_count"), surface.get("bytes"), surface.get("aggregate_sha256")
    ) != (18, 2020949, "80A41130E5797219568E87AC0E15F7AF5F996EFE2895A159FC807C0356DCC33D"):
        raise RuntimeError("Semantic surface receipt drift")
    records = surface.get("files")
    if not isinstance(records, list) or len(records) != 18:
        raise RuntimeError("Semantic file records are malformed")
    return records


def expected_tex_hashes() -> dict[str, str]:
    hashes = dict(strict_json(SOURCE / "check.json")["tex_sha256"])
    if len(hashes) != 119 or "cohomology.tex" not in hashes:
        raise RuntimeError("Predecessor TeX surface drift")
    hashes["cohomology.tex"] = EXPECTED_ARTIFACTS["cohomology.tex"][1]
    return hashes


def lock_paths(fresh: bool) -> list[Path]:
    sem = [SEM / str(item["name"]) for item in sem_records()]
    paths = [
        Path(__file__), ROOT / "srcmap" / "start_build_tohoku_r15.py",
        ROOT / "srcmap" / "start_build_tohoku_r15.ps1",
        *[SOURCE / name for name in EXPECTED_SOURCE],
        *[QA / name for name in EXPECTED_QA],
        *[AUTHORITY / name for name in EXPECTED_AUTHORITY],
        *sem,
    ]
    if fresh:
        paths.extend(ROOT / name for name in EXPECTED_TOOLS)
        paths.extend(ROOT / name for name in expected_tex_hashes())
        paths.extend([ROOT / "cohomology.log", ROOT / "cohomology.pdf"])
    elif TARGET.exists():
        paths.extend(path for path in TARGET.iterdir() if path.is_file())
    return paths


def verify_execution_attestation() -> dict[str, object]:
    attestation = globals().get("EXECUTION_ATTESTATION")
    if not isinstance(attestation, dict):
        raise RuntimeError("Run through start_build_tohoku_r15.py")
    builder = attestation.get("builder")
    if not isinstance(builder, dict) or identity(Path(__file__)) != (
        builder.get("bytes"), builder.get("sha256")
    ):
        raise RuntimeError("Same-bytes builder attestation drift")
    return attestation


def verify_inputs(fresh: bool) -> tuple[dict[str, object], bytes]:
    require_plain_directory(SOURCE)
    source_names = {path.name for path in SOURCE.iterdir() if path.is_file()}
    if source_names != set(EXPECTED_SOURCE) or any(path.is_dir() for path in SOURCE.iterdir()):
        raise RuntimeError("Predecessor dossier surface drift")
    for name, expected in EXPECTED_SOURCE.items():
        require_identity(SOURCE / name, expected)
    predecessor = strict_json(SOURCE / "r14-check.json")
    if predecessor.get("status") != "PASS" or predecessor.get("errors") != []:
        raise RuntimeError("Predecessor receipt is not PASS")
    if fresh:
        for name, expected in EXPECTED_TOOLS.items():
            require_identity(ROOT / name, expected)
    for name, expected in EXPECTED_QA.items():
        require_identity(QA / name, expected)
    for name, expected in EXPECTED_AUTHORITY.items():
        require_identity(AUTHORITY / name, expected)
    if fresh:
        for name, expected in EXPECTED_ARTIFACTS.items():
            require_identity(ROOT / name, expected)

    sem_check = strict_json(QA / "sem-check.json")
    if sem_check.get("status") != "PASS" or sem_check.get("errors") != []:
        raise RuntimeError("Semantic check is not PASS")
    sem = sem_records()
    if {path.name for path in SEM.iterdir() if path.is_file()} != {
        str(item["name"]) for item in sem
    } or any(path.is_dir() for path in SEM.iterdir()):
        raise RuntimeError("Semantic directory surface drift")
    current_sem: list[dict[str, object]] = []
    for item in sem:
        path = SEM / str(item["name"])
        require_identity(path, (int(item["bytes"]), str(item["sha256"])))
        current_sem.append(record(path))
    if aggregate(current_sem) != "80A41130E5797219568E87AC0E15F7AF5F996EFE2895A159FC807C0356DCC33D":
        raise RuntimeError("Semantic aggregate drift")

    if fresh:
        tex_hashes = expected_tex_hashes()
        live_names = {path.name for path in ROOT.glob("*.tex")}
        if live_names != set(tex_hashes):
            raise RuntimeError("Live TeX filename surface drift")
        for name, sha256 in tex_hashes.items():
            require_plain_file(ROOT / name)
            if identity(ROOT / name)[1] != sha256:
                raise RuntimeError(f"Live TeX identity drift: {name}")

    if fresh and (
        sys.version_info[:3] != (3, 13, 9)
        or sys.implementation.cache_tag != "cpython-313"
    ):
        raise RuntimeError("Python runtime drift")
    return dict(EXPECTED_GIT_NONCLAIM), b""


def make_config() -> dict:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r15"
    return cfg


def make_decisions() -> bytes:
    fields, rows = load_csv(SOURCE / "dec.csv")
    if [row["decision_id"] for row in rows] != [f"D{number:06d}" for number in range(1, 927)]:
        raise RuntimeError("Predecessor decision sequence drift")
    if rows[-1]["decision_id"] != "D000926":
        raise RuntimeError("Unexpected predecessor decision tail")
    appended = csv_bytes(fields, DECISION_ROWS)
    return (SOURCE / "dec.csv").read_bytes() + appended[appended.index(b"\n") + 1 :]


def run_tool(name: str, *args: str) -> None:
    relative = f"srcmap/{name}"
    require_identity(ROOT / relative, EXPECTED_TOOLS[relative])
    subprocess.run([sys.executable, "-I", "-B", str(ROOT / relative), *args], cwd=ROOT, check=True)
    require_identity(ROOT / relative, EXPECTED_TOOLS[relative])


def intake_args() -> list[str]:
    specs = [
        ("part_i", AUTHORITY / "jstage_part_I_9_2_119.pdf"),
        ("part_ii", AUTHORITY / "jstage_part_II_9_3_185.pdf"),
        ("edges", SEM / "edges.csv"), ("terms", SEM / "terms.csv"),
        ("stacks", SEM / "stacks.csv"), ("sem_manifest", SEM / "manifest.json"),
        ("sem_validation", SEM / "validation.json"),
        ("sem_input", QA / "sem-input.json"), ("sem_check", QA / "sem-check.json"),
    ]
    output: list[str] = []
    for key, path in specs:
        output += ["--extra", f"{key}={path}"]
    return output


def verify_log() -> dict[str, object]:
    text = (ROOT / "cohomology.log").read_text(encoding="utf-8", errors="replace")
    forbidden = [
        r"(?m)^!", r"(?m)^LaTeX Warning:", r"(?m)^Package .* Warning:",
        r"undefined references", r"undefined citations",
        r"Rerun to get cross-references right", r"Label\(s\) may have changed",
    ]
    hits = [pattern for pattern in forbidden if re.search(pattern, text)]
    if hits:
        raise RuntimeError(f"Cohomology build diagnostics failed: {hits}")
    return {
        "tex": record(ROOT / "cohomology.tex"),
        "log": record(ROOT / "cohomology.log"),
        "pdf": record(ROOT / "cohomology.pdf"),
        "pdf_pages": 198,
        "undefined_references": 0,
        "undefined_citations": 0,
        "rerun_notices": 0,
        "new_block_overfull_boxes": 0,
        "visual_reviewed_pages": [160, 161, 162, 163],
    }


def verify_deltas(root: Path) -> dict[str, object]:
    intake = strict_json(root / "intake.json")
    check = strict_json(root / "check.json")
    mcheck = strict_json(root / "mcheck.json")
    for name, receipt in (("intake", intake), ("scan", check), ("map", mcheck)):
        if receipt.get("status") != "PASS" or receipt.get("errors") != []:
            raise RuntimeError(f"{name} receipt is not PASS")
    if mcheck.get("outputs_promoted") is not True:
        raise RuntimeError("Mapping outputs were not promoted")
    old_cfg = strict_json(SOURCE / "cfg.json")
    expected_cfg = dict(old_cfg)
    expected_cfg["dossier_id"] = "tohoku_r15"
    if strict_json(root / "cfg.json") != expected_cfg:
        raise RuntimeError("Configuration differs by more than the dossier ID")
    if (root / "intake.json").read_bytes() != (SOURCE / "intake.json").read_bytes():
        raise RuntimeError("Semantic intake receipt drift")
    if (root / "topics.csv").read_bytes() != (SOURCE / "topics.csv").read_bytes():
        raise RuntimeError("Topic ledger drift")
    if (root / "issues.csv").read_bytes() != (SOURCE / "issues.csv").read_bytes():
        raise RuntimeError("Source issue ledger drift")
    if (root / "units.csv").read_bytes() != (SOURCE / "units.csv").read_bytes():
        raise RuntimeError("Stable source inventory drift")
    if (root / "tmap.csv").read_bytes() != (SOURCE / "tmap.csv").read_bytes():
        raise RuntimeError("Topic map drift")

    old_dec = (SOURCE / "dec.csv").read_bytes()
    new_dec = (root / "dec.csv").read_bytes()
    if not new_dec.startswith(old_dec):
        raise RuntimeError("Decision ledger is not an exact append-only successor")
    _, decisions = load_csv(root / "dec.csv")
    if [row["decision_id"] for row in decisions] != [f"D{number:06d}" for number in range(1, 929)]:
        raise RuntimeError("Decision sequence is not D000001..D000928")
    if decisions[-2:] != DECISION_ROWS:
        raise RuntimeError("D000927--D000928 differ from the frozen rows")

    expected_tex = expected_tex_hashes()
    if check.get("tex_sha256") != expected_tex:
        raise RuntimeError("Scan did not bind the exact live TeX surface")
    counts = check.get("counts", {})
    if (
        counts.get("tex_files"), counts.get("labels"), counts.get("official_tags_joined"),
        counts.get("topics"), counts.get("topic_candidates"), counts.get("topic_coverage"),
    ) != (119, 21992, 21437, 13, 1239, {"direct": 13}):
        raise RuntimeError(f"Stacks scan count drift: {counts}")
    if check.get("sha256", {}).get("tags/tags") != EXPECTED_TOOLS["tags/tags"][1]:
        raise RuntimeError("Tags hash drift in scan receipt")

    if (root / "tmap.csv").read_bytes() != (SOURCE / "tmap.csv").read_bytes():
        raise RuntimeError("Topic map drift")

    _, old_stx = load_csv(SOURCE / "stx.csv")
    _, new_stx = load_csv(root / "stx.csv")
    old_labels = [row["full_label"] for row in old_stx]
    new_labels = [row["full_label"] for row in new_stx]
    if len(new_labels) != len(set(new_labels)) or set(new_labels) != set(old_labels) | NEW_LABELS:
        raise RuntimeError("Stacks label surface is not old labels plus the four new labels")
    if any(new_labels.count(label) != 1 for label in NEW_LABELS):
        raise RuntimeError("A new Stacks label is absent or duplicated")
    old_by_label = {row["full_label"]: row for row in old_stx}
    new_by_label = {row["full_label"]: row for row in new_stx}
    for label, old in old_by_label.items():
        new = new_by_label[label]
        expected_line = old["line"]
        if old["file"] == "cohomology.tex" and int(old["line"]) >= 16774:
            expected_line = str(int(old["line"]) + 261)
        expected = dict(old)
        expected["line"] = expected_line
        if new != expected:
            changed = sorted(field for field in old if old[field] != new[field])
            raise RuntimeError(f"Unexpected predecessor label delta {label}: {changed}")
    expected_new_rows = {
        "cohomology-definition-equivariant-ext": ("16774", "definition"),
        "cohomology-lemma-equivariant-ext-properties": ("16805", "lemma"),
        "cohomology-lemma-localize-equivariant-ext": ("16906", "lemma"),
        "cohomology-lemma-equivariant-ext-slice": ("16950", "lemma"),
    }
    for label, (line, kind) in expected_new_rows.items():
        row = new_by_label[label]
        if (
            row["tag"], row["file"], row["line"], row["kind"], row["chapter"],
            row["section_label"], row["section_title"],
        ) != (
            "", "cohomology.tex", line, kind, "Cohomology of Sheaves",
            "section-cohomology-group-actions", "Cohomology with group actions",
        ):
            raise RuntimeError(f"New label metadata drift: {label}")

    _, old_tcand = load_csv(SOURCE / "tcand.csv")
    _, new_tcand = load_csv(root / "tcand.csv")
    if len(old_tcand) != 1239 or len(new_tcand) != 1239:
        raise RuntimeError("Topic candidate count drift")
    candidate_key = lambda candidate: (candidate["topic_id"], candidate["full_label"])
    old_candidates = {candidate_key(candidate): candidate for candidate in old_tcand}
    new_candidates = {candidate_key(candidate): candidate for candidate in new_tcand}
    removed_candidate = ("sheaf-cohomology", "cohomology-lemma-RHom-triangulated")
    added_candidate = ("sheaf-cohomology", "cohomology-definition-equivariant-ext")
    expected_candidate_keys = (set(old_candidates) - {removed_candidate}) | {added_candidate}
    if set(new_candidates) != expected_candidate_keys:
        raise RuntimeError("Unexpected topic-candidate boundary change")
    for key in set(old_candidates) & set(new_candidates):
        old = old_candidates[key]
        new = new_candidates[key]
        expected = dict(old)
        expected["line"] = new_by_label[old["full_label"]]["line"]
        if new != expected:
            changed = sorted(field for field in old if old[field] != new[field])
            raise RuntimeError(
                f"Unexpected topic-candidate delta {old['topic_id']}/{old['full_label']}: {changed}"
            )
    expected_added_candidate = {
        "topic_id": "sheaf-cohomology",
        "score": "46",
        "hit_fields": "chapter",
        "tag": "",
        "full_label": "cohomology-definition-equivariant-ext",
        "file": "cohomology.tex",
        "line": "16774",
        "kind": "definition",
        "section_title": "Cohomology with group actions",
        "snippet": (
            "egin definition egin reference ite[Chapter V, 5.6, p. 214] Tohoku "
            "egin history The printed formula (5.6.7) includes X among the arguments "
            "of the sheaf-valued Ext functor. The corrected source removes it: unlike "
            "the global Ext group in (5.6.6), this object is a sheaf on Y , as is "
        ),
        "status": "lexical_candidate_only",
    }
    if new_candidates[added_candidate] != expected_added_candidate:
        raise RuntimeError("New equivariant Ext candidate metadata drift")
    old_warnings = strict_json(SOURCE / "check.json").get("warnings", [])
    new_warnings = check.get("warnings", [])
    expected_warning_delta = [
        f"TeX label has no official tag in this snapshot: {label}"
        for label in sorted(NEW_LABELS)
    ]
    if Counter(new_warnings) - Counter(old_warnings) != Counter(expected_warning_delta):
        raise RuntimeError("Unexpected new scan warnings")
    if Counter(old_warnings) - Counter(new_warnings):
        raise RuntimeError("A predecessor scan warning disappeared")

    _, old_map = load_csv(SOURCE / "map.csv")
    _, new_map = load_csv(root / "map.csv")
    if [row["unit_id"] for row in new_map] != [row["unit_id"] for row in old_map]:
        raise RuntimeError("Map unit ID/order drift")
    decisions_by_unit = {row["unit_id"]: row for row in DECISION_ROWS}
    substantive: list[str] = []
    for old, new in zip(old_map, new_map, strict=True):
        changed = {field for field in old if old[field] != new[field]}
        decision = decisions_by_unit.get(new["unit_id"])
        if decision is not None:
            expected_changed = {
                "decision_id", "disposition", "review_state", "stacks_labels",
                "stacks_tags", "rationale",
            }
            if changed != expected_changed:
                raise RuntimeError(f"Unexpected target map delta: {sorted(changed)}")
            expected_values = {
                "decision_id": decision["decision_id"],
                "disposition": decision["disposition"],
                "review_state": decision["review_state"],
                "stacks_labels": decision["stacks_labels"],
                "stacks_tags": "",
                "rationale": decision["rationale"],
            }
            if any(new[key] != value for key, value in expected_values.items()):
                raise RuntimeError(
                    f"Target map row does not exactly realize {decision['decision_id']}"
                )
            substantive.append(new["unit_id"])
        elif changed:
            raise RuntimeError(f"Unexpected map delta {new['unit_id']}: {sorted(changed)}")
    expected_substantive = [
        "tohoku:definition:equivariant-ext",
        "tohoku:property:equivariant-ext-functoriality",
    ]
    if substantive != expected_substantive:
        raise RuntimeError("Unexpected substantive map change set")

    counts = mcheck.get("counts", {})
    old_counts = strict_json(SOURCE / "mcheck.json")["counts"]
    expected_counts = dict(old_counts)
    expected_counts["decisions"] = 928
    expected_dispositions = dict(old_counts["dispositions"])
    expected_dispositions["existing_equivalent"] += 2
    expected_dispositions["extend_existing"] -= 2
    expected_counts["dispositions"] = expected_dispositions
    if counts != expected_counts:
        raise RuntimeError(f"Mapping counts drift: {counts}")
    _, candidates = load_csv(root / "ucand.csv")
    if candidates:
        raise RuntimeError("Unexpected undecided unit candidates")
    return {
        "decisions": DECISION_ROWS,
        "new_labels": sorted(NEW_LABELS),
        "scan_counts": check["counts"],
        "mapping_counts": counts,
        "substantive_map_changes": substantive,
        "remaining_gap_class_dispositions": 124,
    }


def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def source_records() -> list[dict[str, object]]:
    return [record(SOURCE / name) for name in sorted(EXPECTED_SOURCE)]


def receipt_payload(
    root: Path,
    git: dict[str, object],
    attestation: dict[str, object],
    deltas: dict[str, object],
    build: dict[str, object] | None = None,
    execution: dict[str, object] | None = None,
) -> dict[str, object]:
    sources = source_records()
    semantic = [record(SEM / str(item["name"])) for item in sem_records()]
    return {
        "schema": "tohoku-stacks-mapping-successor-r15-v1",
        "status": "PASS",
        "errors": [],
        "predecessor_dossier": {
            "name": "tohoku_r14",
            "files": sources,
            "file_count": len(sources),
            "bytes": sum(int(item["bytes"]) for item in sources),
            "aggregate_sha256": aggregate(sources),
        },
        "semantic_source": {
            "generation": "sem/r10",
            "files": semantic,
            "file_count": len(semantic),
            "bytes": sum(int(item["bytes"]) for item in semantic),
            "aggregate_sha256": aggregate(semantic),
            "sem_input": record(QA / "sem-input.json", "qa/v68r24/sem-input.json"),
            "sem_check": record(QA / "sem-check.json", "qa/v68r24/sem-check.json"),
        },
        "execution": execution if execution is not None else {
            "attestation": attestation,
            "bootstrap": record(ROOT / "srcmap" / "start_build_tohoku_r15.py"),
            "powershell_envelope": record(ROOT / "srcmap" / "start_build_tohoku_r15.ps1"),
            "dependencies": {name: record(ROOT / name) for name in sorted(EXPECTED_TOOLS)},
            "contract": "same_bytes_bootstrap; exact_inputs_locked_against_write_delete_through_generation_replay_and_promotion",
        },
        "git": git,
        "cohomology_build": verify_log() if build is None else build,
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": [
            "No Git command is executed by this ledger-only successor.",
            "No Git commit or push is made by this receipt.",
            "No remote-server freshness check is performed.",
            "The Stacks scan binds the exact live integrated worktree, not the frozen HEAD tree.",
            "The transaction denies write/delete access to every existing consumed file; hostile same-user mutation of directory namespaces is outside this lock contract.",
            "No release, publication, upload, DOI, Zenodo, rights, or whole-paper gate is closed.",
            "124 Tohoku gap-class dispositions remain after D000928.",
        ],
    }


def verify_existing(
    git: dict[str, object], attestation: dict[str, object]
) -> dict[str, object]:
    require_plain_directory(TARGET)
    names = {path.name for path in TARGET.iterdir() if path.is_file()}
    if names != PAYLOAD | {"r15-check.json"} or any(path.is_dir() for path in TARGET.iterdir()):
        raise RuntimeError("Existing r15 dossier surface drift")
    deltas = verify_deltas(TARGET)
    receipt = strict_json(TARGET / "r15-check.json")
    if receipt.get("git") != EXPECTED_GIT_NONCLAIM:
        raise RuntimeError("Existing receipt Git nonclaim drift")
    build = receipt.get("cohomology_build")
    if not isinstance(build, dict):
        raise RuntimeError("Existing build receipt is malformed")
    expected_build = {
        "tex": {
            "name": "cohomology.tex",
            "bytes": EXPECTED_ARTIFACTS["cohomology.tex"][0],
            "sha256": EXPECTED_ARTIFACTS["cohomology.tex"][1],
        },
        "log": {
            "name": "cohomology.log",
            "bytes": EXPECTED_ARTIFACTS["cohomology.log"][0],
            "sha256": EXPECTED_ARTIFACTS["cohomology.log"][1],
        },
        "pdf": {
            "name": "cohomology.pdf",
            "bytes": EXPECTED_ARTIFACTS["cohomology.pdf"][0],
            "sha256": EXPECTED_ARTIFACTS["cohomology.pdf"][1],
        },
        "pdf_pages": 198,
        "undefined_references": 0,
        "undefined_citations": 0,
        "rerun_notices": 0,
        "new_block_overfull_boxes": 0,
        "visual_reviewed_pages": [160, 161, 162, 163],
    }
    if build != expected_build:
        raise RuntimeError("Existing build receipt drift")
    execution = receipt.get("execution")
    if not isinstance(execution, dict):
        raise RuntimeError("Existing execution receipt is malformed")
    expected_execution = {
        "attestation": attestation,
        "bootstrap": record(ROOT / "srcmap" / "start_build_tohoku_r15.py"),
        "powershell_envelope": record(ROOT / "srcmap" / "start_build_tohoku_r15.ps1"),
        "dependencies": {
            name: {
                "name": Path(name).name,
                "bytes": expected[0],
                "sha256": expected[1],
            }
            for name, expected in sorted(EXPECTED_TOOLS.items())
        },
        "contract": "same_bytes_bootstrap; exact_inputs_locked_against_write_delete_through_generation_replay_and_promotion",
    }
    if execution != expected_execution:
        raise RuntimeError("Existing execution receipt drift")
    expected = receipt_payload(
        TARGET, receipt["git"], attestation, deltas, build, execution
    )
    if receipt != expected:
        raise RuntimeError("Existing r15 receipt replay mismatch")
    return receipt


def main_locked(attestation: dict[str, object]) -> int:
    if TARGET.exists() and STAGE.exists():
        raise RuntimeError("Target and unresolved transaction coexist")
    fresh = not TARGET.exists()
    with deny_write_delete(lock_paths(fresh)):
        git, _ = verify_inputs(fresh)
        if TARGET.exists():
            receipt = verify_existing(git, attestation)
            print(json.dumps(receipt, ensure_ascii=False, indent=2))
            return 0
        if STAGE.exists():
            raise FileExistsError(f"Unresolved transaction exists: {STAGE}")
        STAGE.mkdir()
        exclusive_write(STAGE / "cfg.json", json_bytes(make_config()))
        exclusive_write(STAGE / "topics.csv", (SOURCE / "topics.csv").read_bytes())
        exclusive_write(STAGE / "dec.csv", make_decisions())
        exclusive_write(STAGE / "issues.csv", (SOURCE / "issues.csv").read_bytes())
        run_tool("intake.py", str(STAGE), str(SEM / "nodes.csv"), *intake_args())
        run_tool("scan.py", str(STAGE))
        run_tool("map.py", str(STAGE))
        deltas = verify_deltas(STAGE)
        status = (
            "# Tohoku Stacks mapping status\n\n"
            "- Semantic source: sealed local-unpublished `sem/r10`.\n"
            "- Stable source inventory: 990 units.\n"
            "- Append-only decisions: `D000927` and `D000928` supersede `D000606` and `D000626` for equivariant Ext, functoriality, locality, and slice reduction on p. 214.\n"
            "- The successor binds the four new equivariant Ext labels and the exact rebuilt chapter.\n"
            "- 124 gap-class dispositions remain.\n"
            "- This local checkpoint makes no release, publication, remote-freshness, DOI, rights, or completion claim.\n"
        ).encode("utf-8")
        exclusive_write(STAGE / "STATUS.md", status)
        receipt = receipt_payload(STAGE, git, attestation, deltas)
        exclusive_write(STAGE / "r15-check.json", json_bytes(receipt))
        if (
            {path.name for path in STAGE.iterdir() if path.is_file()}
            != PAYLOAD | {"r15-check.json"}
            or any(path.is_dir() for path in STAGE.iterdir())
        ):
            raise RuntimeError("Staged dossier surface mismatch")
        verify_inputs(True)
        os.rename(STAGE, TARGET)
        with deny_write_delete([path for path in TARGET.iterdir() if path.is_file()]):
            final = verify_existing(git, attestation)
        print(json.dumps(final, ensure_ascii=False, indent=2))
        return 0


def main() -> int:
    attestation = verify_execution_attestation()
    with single_writer_mutex():
        return main_locked(attestation)


if __name__ == "__main__":
    raise SystemExit(main())
