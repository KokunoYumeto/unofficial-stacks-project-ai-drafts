#!/usr/bin/env python3
"""Build the no-overwrite Tohoku Stacks mapping successor for D000929--D000933."""

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
SOURCE = ROOT / "tohoku_r15"
TARGET = ROOT / "tohoku_r16"
STAGE = ROOT / ".tohoku-r16-txn"
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
        "path": "tohoku_r15/r15-check.json",
        "bytes": 15403,
        "sha256": "A0E4BF3601FA68AF5FA43D46697B384F655FEF08C208C7DD48FAB4B2E3966ADE",
    },
    "remote_server_freshness_verified": False,
}

EXPECTED_SOURCE = {
    "cfg.json": (5193, "298FC999C14B1B6E942808664076F05B7CD837B074AA26387B9EB9CCFDFF7E31"),
    "check.json": (70283, "29268CA2C499AFD64C47EA206CF3E7F095F0E3985E4CF0EDA081D3DCEA4C02E9"),
    "dec.csv": (315065, "B516296DA756674B9F31ECB4252C00737AFA6D95BD50C03E3B68869618BF47E0"),
    "intake.json": (1877, "86273E19DB8A912BF9558DE007EF4A39C9C7FB93EBEA64A85D31A4F4A4BE42F2"),
    "issues.csv": (15036, "16DD4BCA450F4030F9EF3FE6F6A3C51CF64BEE81CE59F56AF141D572CB1C4328"),
    "map.csv": (453050, "8DE9E955B23200953E123D8264B3F67D4B3903388333EC12EA8C7E6254A5C080"),
    "mcheck.json": (60112, "00C8CE1BE9D796AEBC130EAB5BB99F647BA036DF624941EB49E4C4427305CE75"),
    "r15-check.json": (15403, "A0E4BF3601FA68AF5FA43D46697B384F655FEF08C208C7DD48FAB4B2E3966ADE"),
    "STATUS.md": (518, "6E89984476035E75F09375E8C24D5282A37EA97BE746C6648B43447B7C0AAFFA"),
    "stx.csv": (5257252, "77F9F7EA8292BB8B6F2E192869089D948FBE86D3B1A3CBAE894CB9D29F8EDD23"),
    "tcand.csv": (472664, "51B7838C66549088139BA6B519169571AC88243B3953E411C5AE3652438F655B"),
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
    "cohomology.tex": (774053, "F8D720F5FECC2EF4215438C8E301230550D5ABFBFB6E395476A64F741F1BEEC4"),
    "cohomology.log": (47248, "D91B3B9ECCBB8A3FA6ACF6E6C3D69034CDD42E6B97F9B9E4BF53354E2397C442"),
    "cohomology.pdf": (1763626, "2E08FEA7721E55A50E205014B5F337E875D8B2F6F6E6CE77B8E7031A68CDD29C"),
}

NEW_LABELS = {
    "cohomology-lemma-skew-group-hom-injective-acyclic",
    "cohomology-lemma-equivariant-product-internal-hom",
    "cohomology-lemma-equivariant-hom-injective-acyclic",
}

DECISION_ROWS = [
    {
        "decision_id": "D000929",
        "unit_id": "tohoku:lemma:5.6.1",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-equivariant-hom-injective-acyclic",
        "rationale": (
            "Stacks now proves all three assertions of Lemma 5.6.1 for an injective "
            "G-O-module B: q_*^G SheafHom_O(A,B) is flasque on Y, Hom_O(A,B) is right "
            "acyclic for G-invariants, and the internal Hom is right acyclic for "
            "Gamma_X^G. It also proves the underlying abelian internal-Hom sheaf "
            "flasque and explicitly makes no false claim that the global Hom module is "
            "injective."
        ),
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000622",
    },
    {
        "decision_id": "D000930",
        "unit_id": "tohoku:construction:coinduced-hom-module",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-equivariant-product-internal-hom",
        "rationale": (
            "Stacks now identifies each orbit product prod_{x in y} H_x canonically "
            "with Coind_{G_y}^G(H_y), proves the Shapiro isomorphisms "
            "H^n(G,Coind_{G_y}^G(M))=H^n(G_y,M), and proves that arbitrary products "
            "preserve this acyclicity. This is exactly the source's clean coinduced-Hom "
            "module step; the separate erroneous quotient-product formula remains open "
            "under D000590."
        ),
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000578",
    },
    {
        "decision_id": "D000931",
        "unit_id": "tohoku:corollary:coinduced-hom-acyclicity",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-skew-group-hom-injective-acyclic",
        "rationale": (
            "Stacks now proves the corollary for an arbitrary ring R with G-action and "
            "semilinear left R-modules A and B: if B is injective in the equivariant "
            "module category, then Hom_R(A,B) is right acyclic for invariants in every "
            "positive degree. It also retains the source's warning that this Hom module "
            "need not be injective."
        ),
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000598",
    },
    {
        "decision_id": "D000932",
        "unit_id": "tohoku:definition:coinduced-module-b-prime",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-skew-group-hom-injective-acyclic",
        "rationale": (
            "Stacks now defines the source's auxiliary coinduced object B' as "
            "prod_{g in G} B, equivalently Map(G,B), and gives its formulas "
            "(r f)_g=g(r)f_g and (h f)_g=f_{gh}; this is the same definition expressed "
            "without separate crossed-product notation."
        ),
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000603",
    },
    {
        "decision_id": "D000933",
        "unit_id": "tohoku:construction:coinduced-u-module-b-prime",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-lemma-skew-group-hom-injective-acyclic",
        "rationale": (
            "Stacks now verifies that the displayed formulas make B' a compatible "
            "semilinear equivariant R-module and that eta:B->B', eta(b)_g=gb, is an "
            "injective equivariant map; injectivity of B then splits eta, exactly giving "
            "the source's U-module construction and direct-summand reduction."
        ),
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000579",
    },
]

ISSUE_ROWS = [
    {
        "issue_id": "I000020",
        "unit_id": "tohoku:construction:product-hom-sheaf",
        "status": "confirmed",
        "kind": "source_orbit_product_overcount",
        "claim": (
            "The printed formula H_y=prod_{q(x)=y}(H_x)^{G_x} is false: it "
            "repeats one stabilizer-fixed factor for every point of a single orbit, "
            "whereas an invariant family on that orbit is determined by one "
            "representative and gives H_{xi(y)}^{G_{xi(y)}}."
        ),
        "evidence_labels": "cohomology-lemma-equivariant-product-internal-hom",
        "evidence": (
            "Official Part II SHA-256 "
            "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53, "
            "printed p. 215. For G=C2 acting freely and transitively on two points "
            "with H_x=Z and identity transport, (prod_{x in y}H_x)^G is the diagonal "
            "Z, while the printed product of stabilizer-fixed groups is Z x Z. The "
            "corrective Stacks lemma proves the one-factor formula."
        ),
        "control": (
            "Preserve the printed product diplomatically. In corrected French, "
            "English, and semantic source replace it by (prod_{q(x)=y}H_x)^G "
            "congruent H_{xi(y)}^{G_{xi(y)}} and hence one factor per orbit; keep "
            "D000590 open until that no-overwrite source correction is admitted, then "
            "append a resolving mapping successor."
        ),
        "resolution_decision": "",
    },
    {
        "issue_id": "I000021",
        "unit_id": "tohoku:construction:two-coinduced-g-actions",
        "status": "confirmed",
        "kind": "source_wrong_coinduction_intertwiner",
        "claim": (
            "With the two displayed G-actions and the claimed direction H'->H'', the "
            "printed formula psi(f)(g)=g f(g) is not G-equivariant; the equivariant "
            "formula in that direction is psi(f)(g)=g^{-1}f(g)."
        ),
        "evidence_labels": "cohomology-lemma-skew-group-hom-injective-acyclic",
        "evidence": (
            "Official Part II SHA-256 "
            "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53, "
            "printed p. 216. For (h v)_g=v_{gh} and (h star v)_g=h dot v_{gh}, "
            "the printed map gives psi(hv)_g=g dot v_{gh}, while "
            "(h star psi(v))_g=(hgh) dot v_{gh} in general; with g^{-1}, both sides "
            "equal g^{-1} dot v_{gh}. The printed g-formula is equivariant only in "
            "the reverse H''->H' direction."
        ),
        "control": (
            "Preserve the printed formula diplomatically. In corrected French, "
            "English, and semantic source replace g by g^{-1} in the stated "
            "H'->H'' direction; keep D000591 open until that no-overwrite correction "
            "is admitted, then append a resolving mapping successor."
        ),
        "resolution_decision": "",
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
    mutex = Path(pointer.removeprefix("gitdir: ")) / "tohoku-r16-dossier.lock"
    if not mutex.parent.is_dir():
        raise RuntimeError("Resolved explicit worktree Git directory is absent")
    mutex.parent.mkdir(parents=True, exist_ok=True)
    handle = create_file(str(mutex), 0xC0000000, 0, None, 4, 0x00000100, None)
    invalid = ctypes.c_void_p(-1).value
    if handle in (None, invalid):
        raise RuntimeError("Another Tohoku r16 transaction is active")
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
        Path(__file__), ROOT / "srcmap" / "start_build_tohoku_r16.py",
        ROOT / "srcmap" / "start_build_tohoku_r16.ps1",
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
        raise RuntimeError("Run through start_build_tohoku_r16.py")
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
    predecessor = strict_json(SOURCE / "r15-check.json")
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
    cfg["dossier_id"] = "tohoku_r16"
    return cfg


def make_decisions() -> bytes:
    fields, rows = load_csv(SOURCE / "dec.csv")
    if [row["decision_id"] for row in rows] != [f"D{number:06d}" for number in range(1, 929)]:
        raise RuntimeError("Predecessor decision sequence drift")
    if rows[-1]["decision_id"] != "D000928":
        raise RuntimeError("Unexpected predecessor decision tail")
    appended = csv_bytes(fields, DECISION_ROWS)
    return (SOURCE / "dec.csv").read_bytes() + appended[appended.index(b"\n") + 1 :]


def make_issues() -> bytes:
    fields, rows = load_csv(SOURCE / "issues.csv")
    if [row["issue_id"] for row in rows] != [f"I{number:06d}" for number in range(1, 20)]:
        raise RuntimeError("Predecessor source-issue sequence drift")
    if rows[-1]["issue_id"] != "I000019":
        raise RuntimeError("Unexpected predecessor source-issue tail")
    appended = csv_bytes(fields, ISSUE_ROWS)
    return (SOURCE / "issues.csv").read_bytes() + appended[appended.index(b"\n") + 1 :]


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
        "pdf_pages": 202,
        "undefined_references": 0,
        "undefined_citations": 0,
        "rerun_notices": 0,
        "new_block_overfull_boxes": 0,
        "visual_reviewed_pages": [162, 163, 164, 165, 166],
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
    expected_cfg["dossier_id"] = "tohoku_r16"
    if strict_json(root / "cfg.json") != expected_cfg:
        raise RuntimeError("Configuration differs by more than the dossier ID")
    if (root / "intake.json").read_bytes() != (SOURCE / "intake.json").read_bytes():
        raise RuntimeError("Semantic intake receipt drift")
    if (root / "topics.csv").read_bytes() != (SOURCE / "topics.csv").read_bytes():
        raise RuntimeError("Topic ledger drift")
    old_issues = (SOURCE / "issues.csv").read_bytes()
    new_issues = (root / "issues.csv").read_bytes()
    if not new_issues.startswith(old_issues):
        raise RuntimeError("Source issue ledger is not an exact append-only successor")
    _, issues = load_csv(root / "issues.csv")
    if [row["issue_id"] for row in issues] != [f"I{number:06d}" for number in range(1, 22)]:
        raise RuntimeError("Source issue sequence is not I000001..I000021")
    if issues[-2:] != ISSUE_ROWS:
        raise RuntimeError("I000020--I000021 differ from the frozen rows")
    if (root / "units.csv").read_bytes() != (SOURCE / "units.csv").read_bytes():
        raise RuntimeError("Stable source inventory drift")
    if (root / "tmap.csv").read_bytes() != (SOURCE / "tmap.csv").read_bytes():
        raise RuntimeError("Topic map drift")

    old_dec = (SOURCE / "dec.csv").read_bytes()
    new_dec = (root / "dec.csv").read_bytes()
    if not new_dec.startswith(old_dec):
        raise RuntimeError("Decision ledger is not an exact append-only successor")
    _, decisions = load_csv(root / "dec.csv")
    if [row["decision_id"] for row in decisions] != [f"D{number:06d}" for number in range(1, 934)]:
        raise RuntimeError("Decision sequence is not D000001..D000933")
    if decisions[-5:] != DECISION_ROWS:
        raise RuntimeError("D000929--D000933 differ from the frozen rows")

    expected_tex = expected_tex_hashes()
    if check.get("tex_sha256") != expected_tex:
        raise RuntimeError("Scan did not bind the exact live TeX surface")
    counts = check.get("counts", {})
    if (
        counts.get("tex_files"), counts.get("labels"), counts.get("official_tags_joined"),
        counts.get("topics"), counts.get("topic_candidates"), counts.get("topic_coverage"),
    ) != (119, 21995, 21437, 13, 1239, {"direct": 13}):
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
        raise RuntimeError("Stacks label surface is not old labels plus the three new labels")
    if any(new_labels.count(label) != 1 for label in NEW_LABELS):
        raise RuntimeError("A new Stacks label is absent or duplicated")
    old_by_label = {row["full_label"]: row for row in old_stx}
    new_by_label = {row["full_label"]: row for row in new_stx}
    for label, old in old_by_label.items():
        new = new_by_label[label]
        expected_line = old["line"]
        if old["file"] == "cohomology.tex" and int(old["line"]) >= 17035:
            expected_line = str(int(old["line"]) + 353)
        expected = dict(old)
        expected["line"] = expected_line
        if new != expected:
            changed = sorted(field for field in old if old[field] != new[field])
            raise RuntimeError(f"Unexpected predecessor label delta {label}: {changed}")
    expected_new_rows = {
        "cohomology-lemma-skew-group-hom-injective-acyclic": ("17035", "lemma"),
        "cohomology-lemma-equivariant-product-internal-hom": ("17152", "lemma"),
        "cohomology-lemma-equivariant-hom-injective-acyclic": ("17290", "lemma"),
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
    if set(new_candidates) != set(old_candidates):
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
        "tohoku:construction:coinduced-hom-module",
        "tohoku:construction:coinduced-u-module-b-prime",
        "tohoku:corollary:coinduced-hom-acyclicity",
        "tohoku:definition:coinduced-module-b-prime",
        "tohoku:lemma:5.6.1",
    ]
    if substantive != expected_substantive:
        raise RuntimeError("Unexpected substantive map change set")

    counts = mcheck.get("counts", {})
    old_counts = strict_json(SOURCE / "mcheck.json")["counts"]
    expected_counts = dict(old_counts)
    expected_counts["decisions"] = 933
    expected_counts["source_issues"] = 21
    expected_counts["active_source_issues"] = 2
    expected_dispositions = dict(old_counts["dispositions"])
    expected_dispositions["existing_equivalent"] += 5
    expected_dispositions["extend_existing"] -= 2
    expected_dispositions["new_statement"] -= 3
    expected_counts["dispositions"] = expected_dispositions
    if counts != expected_counts:
        raise RuntimeError(f"Mapping counts drift: {counts}")
    _, candidates = load_csv(root / "ucand.csv")
    if candidates:
        raise RuntimeError("Unexpected undecided unit candidates")
    return {
        "decisions": DECISION_ROWS,
        "source_issues": ISSUE_ROWS,
        "new_labels": sorted(NEW_LABELS),
        "scan_counts": check["counts"],
        "mapping_counts": counts,
        "substantive_map_changes": substantive,
        "remaining_gap_class_dispositions": 119,
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
        "schema": "tohoku-stacks-mapping-successor-r16-v1",
        "status": "PASS",
        "errors": [],
        "predecessor_dossier": {
            "name": "tohoku_r15",
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
            "bootstrap": record(ROOT / "srcmap" / "start_build_tohoku_r16.py"),
            "powershell_envelope": record(ROOT / "srcmap" / "start_build_tohoku_r16.ps1"),
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
            "119 Tohoku gap-class dispositions remain after D000933.",
            "Two newly confirmed source-formula issues remain open for the translation phase.",
        ],
    }


def verify_existing(
    git: dict[str, object], attestation: dict[str, object]
) -> dict[str, object]:
    require_plain_directory(TARGET)
    names = {path.name for path in TARGET.iterdir() if path.is_file()}
    if names != PAYLOAD | {"r16-check.json"} or any(path.is_dir() for path in TARGET.iterdir()):
        raise RuntimeError("Existing r16 dossier surface drift")
    deltas = verify_deltas(TARGET)
    receipt = strict_json(TARGET / "r16-check.json")
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
        "pdf_pages": 202,
        "undefined_references": 0,
        "undefined_citations": 0,
        "rerun_notices": 0,
        "new_block_overfull_boxes": 0,
        "visual_reviewed_pages": [162, 163, 164, 165, 166],
    }
    if build != expected_build:
        raise RuntimeError("Existing build receipt drift")
    execution = receipt.get("execution")
    if not isinstance(execution, dict):
        raise RuntimeError("Existing execution receipt is malformed")
    expected_execution = {
        "attestation": attestation,
        "bootstrap": record(ROOT / "srcmap" / "start_build_tohoku_r16.py"),
        "powershell_envelope": record(ROOT / "srcmap" / "start_build_tohoku_r16.ps1"),
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
        raise RuntimeError("Existing r16 receipt replay mismatch")
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
        exclusive_write(STAGE / "issues.csv", make_issues())
        run_tool("intake.py", str(STAGE), str(SEM / "nodes.csv"), *intake_args())
        run_tool("scan.py", str(STAGE))
        run_tool("map.py", str(STAGE))
        deltas = verify_deltas(STAGE)
        status = (
            "# Tohoku Stacks mapping status\n\n"
            "- Semantic source: sealed local-unpublished `sem/r10`.\n"
            "- Stable source inventory: 990 units.\n"
            "- Append-only decisions: `D000929`--`D000933` close the five exact Lemma 5.6.1 and coinduction units on pp. 215--216.\n"
            "- `I000020` and `I000021` confirm two source-formula defects; `D000590` and `D000591` remain open pending translation-layer correction.\n"
            "- The successor binds the three new equivariant Hom-acyclicity labels and the exact rebuilt chapter.\n"
            "- 119 gap-class dispositions remain.\n"
            "- This local checkpoint makes no release, publication, remote-freshness, DOI, rights, or completion claim.\n"
        ).encode("utf-8")
        exclusive_write(STAGE / "STATUS.md", status)
        receipt = receipt_payload(STAGE, git, attestation, deltas)
        exclusive_write(STAGE / "r16-check.json", json_bytes(receipt))
        if (
            {path.name for path in STAGE.iterdir() if path.is_file()}
            != PAYLOAD | {"r16-check.json"}
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
