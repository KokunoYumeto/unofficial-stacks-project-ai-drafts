#!/usr/bin/env python3
"""Build the no-overwrite Tohoku Stacks mapping successor D000992."""

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
from collections.abc import Iterator
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r37"
TARGET = ROOT / "tohoku_r38"
STAGE = ROOT / ".tohoku-r38-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r13"
QA = PROJECT / "qa" / "v68r31"
AUTHORITY = PROJECT / "authority_snapshot"

EXPECTED_GIT_NONCLAIM = {
    "inspection_performed": False,
    "reason": "No Git operation was needed for this bounded local successor.",
    "predecessor_receipt": {
        "path": "tohoku_r37/r37-check.json",
        "bytes": 19509,
        "sha256": "04D966EF558C8BDD09C0DB65D85B3389E1646292C831E11DC2FC9330E418A03D",
    },
    "remote_server_freshness_verified": False,
}

EXPECTED_SOURCE = {
    "cfg.json": (5193, "3F4C31E912D1DE3E8AA17BD77C3B6EDA7A346064D94116BCA70202FA7DB3AC48"),
    "check.json": (74731, "404CE978CA920495A250580E6EB948EEB0312129D580F6D80BD0D4907C0CB810"),
    "dec.csv": (352179, "7DEC48BB787ED567F4FFB396B4A479A400F8D378B8C294C0B158273EDD78AF19"),
    "intake.json": (1877, "EB529D8C7981784C3991C013513DC4E167A198DAFEA774EC92AA22816435F247"),
    "issues.csv": (23487, "B131717123CAF4F444898DACD85AD636A2C70349BA1FC7EE45A0E9012A5CC188"),
    "map.csv": (468523, "9CCC0AB66D46D3D7B2CB5C707EE1230F8FFFD6869589CCE9B5464144E6C0729D"),
    "mcheck.json": (64559, "81BAEF88FC244C4AB737DE29738E4A1DCEB18FC51C9E3F2A4DBA9B6BD28B5046"),
    "r37-check.json": (19509, "04D966EF558C8BDD09C0DB65D85B3389E1646292C831E11DC2FC9330E418A03D"),
    "STATUS.md": (678, "3B78C250FD64DD3C55213C65272A001C43C0ABBC789BEB70CF1A172CA79BA0A8"),
    "stx.csv": (5268167, "8E8F56B0D4FB98933ACCE45FABBA2BFCA33C96134638D2ECA051ABB4EC320D4B"),
    "tcand.csv": (477433, "DB01CF6C3FDE04200203F9A3D1AD67048E84C3496C24D92C7B08BA94D93D0C1C"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (391679, "739F58491FCBF452B41EEE65E97CE515DD2B618438DA77BA08A07E6BD7969B15"),
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
    "sem-input.json": (295453, "779A352039F372BDE7ABBB9A6EEE77AB6446110A398B306BD26F295E002D8AD6"),
    "sem-check.json": (6535, "40EFC1CE15C90F9DF17755FEA991FA9A7B74C5203E924DACF4614A30E001C875"),
}

EXPECTED_AUTHORITY = {
    "jstage_part_I_9_2_119.pdf": (7305283, "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF"),
    "jstage_part_II_9_3_185.pdf": (3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53"),
}

EXPECTED_ARTIFACTS = {
    "homology.tex": (354281, "4B062B95126D68D4EB46BD9B456F8763FEDE53A7CDCCD157B89CB3FB3B8CC1CF"),
    "homology.aux": (27880, "D3A283BE82F4ECAB7BB66A3006BA3EAD8609E490ED16E39CF264435D4C4E1804"),
    "homology.log": (38818, "6AECF99D837BCA8A5CB91B485D3A06655149B44A2072CCE19B504AEF08EE65A8"),
    "homology.pdf": (1024519, "85269A9E67C757D1B0E5BCDB0840E39BCDF221E01F65D967297649671CEE431C"),
    "modules.tex": (227768, "6BDE2852FFC50945A781FE7598FE96EC69D8B650EEF5C4C608C440D9E7E53BC0"),
    "modules.log": (35913, "D2989C27651EACA9A5AA4BD22FCF67E7273EF67D0CC0DA9606C23844E7D94BE1"),
    "modules.pdf": (758941, "1254E015413AFF83541031659835E3B02998D1F43550FB83D00D07A5DE3CB3E9"),
    "cohomology.tex": (814928, "C120A56D9C3788BE467DDDBA310F8A2FDDE0AB3326ED7B9183E8B16337418AD4"),
    "cohomology.log": (47485, "95EFD946BDA79140BBA240055142E4F13E2F8E53A690DD5B74690D6449A386D2"),
    "cohomology.pdf": (1832179, "50DE21B2916AF71A8B05774FCBAB754A750F599CC34C0E2B62CE069526E29822"),
    "injectives.tex": (130520, "5BC898D7A1A1017D28C6C28CA5F318D3E96A12A333CE6684FF13600316DA5D22"),
    "injectives.log": (35028, "5F0474FCF38F15F733CEF9DCA12044FB54D9E87BFAE5FD2B219E830AA46CC404"),
    "injectives.pdf": (633384, "7D651B4DB0A9D03D24195CCF3BCD726817867057BC082F8A996A30AD8E858D58"),
}

BUILD_SPECS = {
    "homology": {"pdf_pages": 106, "visual_reviewed_pages": [44, 45, 46, 47, 48]},
    "modules": {"pdf_pages": 58, "visual_reviewed_pages": [5, 6]},
    "cohomology": {
        "pdf_pages": 214,
        "visual_reviewed_pages": [162, 163, 164],
    },
    "injectives": {"pdf_pages": 38, "visual_reviewed_pages": [18, 19, 20]},
}

NEW_LOCAL_LABELS = (
    "homology-lemma-first-right-satellite-injective-effacements",
    "homology-lemma-right-satellites-injective-effacements",
)

EXPECTED_NEW_LABEL_ROWS = {
    NEW_LOCAL_LABELS[0]: {
        "file": "homology.tex",
        "line": "4101",
        "kind": "lemma",
        "short_label": "lemma-first-right-satellite-injective-effacements",
        "section_label": "section-cohomological-delta-functor",
        "text_sha256": "4BDB8DE4B82D1CD38B4DE5BB74341907B5B912384E839A0184EE6806AC74FA6F",
    },
    NEW_LOCAL_LABELS[1]: {
        "file": "homology.tex",
        "line": "4346",
        "kind": "lemma",
        "short_label": "lemma-right-satellites-injective-effacements",
        "section_label": "section-cohomological-delta-functor",
        "text_sha256": "77914D564AF463971EA4226AD66471972321498BFD7AEA5C92B5D71173566D88",
    },
}

EXPECTED_TOPIC_CANDIDATE_ADDED = (
    ("delta-functor", NEW_LOCAL_LABELS[0]),
    ("delta-functor", NEW_LOCAL_LABELS[1]),
)
EXPECTED_TOPIC_CANDIDATE_DROPPED: tuple[tuple[str, str], ...] = ()

DECISION_ROWS = [
    {
        "decision_id": "D000992",
        "unit_id": "tohoku:thm:2.2.2:p1",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": ";".join(NEW_LOCAL_LABELS),
        "rationale": (
            "Stacks now proves the first assertion of Tohoku Theorem 2.2.2 under the same "
            "hypotheses. If every object of the abelian source category has an injective "
            "effacement, every covariant additive functor to an abelian category admits a "
            "universal graded connecting functor of step +1 in all nonnegative degrees with "
            "degree-zero functor F, and every positive component is effaceable. The "
            "construction forms the first satellite as the cokernel of F(E_A) to F(Q_A), "
            "proves independence of the chosen lifts, functoriality, boundary naturality, the "
            "complex identities, universality, and effaceability, and then iterates it. No "
            "exactness of the satellite system, exactness criterion, negative or left "
            "satellites, contravariant version, or derived-functor identification is asserted."
        ),
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000215",
    },
]

ISSUE_ROWS: list[dict[str, str]] = []

SEMANTIC_SURFACE = (
    18,
    2022622,
    "92CC280A0891E249EF0908EB994C98158EDA5E22871D65EEC3AD766FDEB93D3A",
)

STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- Semantic source: sealed local-unpublished `sem/r13`.\n"
    "- Stable source inventory: 990 units.\n"
    "- Append-only decision `D000992` binds the first assertion of Tohoku Theorem 2.2.2 to the two independently audited right-satellite existence and effaceability lemmas.\n"
    "- All 26 recorded source issues remain resolved; no source-issue row changes in this successor.\n"
    "- The pinned live Stacks index adds the two audited right-satellite labels; the four chapter builds are pinned.\n"
    "- 66 gap-class dispositions remain.\n"
    "- This local dossier makes no release, publication, remote-freshness, DOI, rights, or completion claim.\n"
).encode("utf-8")

PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv",
    "issues.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv",
    "map.csv", "ucand.csv", "mcheck.json", "STATUS.md",
}

EXPECTED_OUTPUTS = {
    "cfg.json": (5193, "A088704D7E156113C62FD95B3344DBB08D8EEAD543F934A60152E70C3CB5A446"),
    "intake.json": (1877, "EB529D8C7981784C3991C013513DC4E167A198DAFEA774EC92AA22816435F247"),
    "units.csv": (391679, "739F58491FCBF452B41EEE65E97CE515DD2B618438DA77BA08A07E6BD7969B15"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "dec.csv": (353176, "E3F0D5396A824C41F1EFBF7683CF522DC901AB18EF6CE0DBD8083E7695E8A50E"),
    "issues.csv": (23487, "B131717123CAF4F444898DACD85AD636A2C70349BA1FC7EE45A0E9012A5CC188"),
    "check.json": (74954, "58E6F6A024AF9A6BD3CC309EC7727C4BCC05C12602EA299BED3165E4DB3520F1"),
    "stx.csv": (5268730, "61459E55403E3CDEC3F9AB851336FAAD0C2EBEE45154BB6482E8ECA921CBCC8D"),
    "tcand.csv": (478316, "FD899040BC1C9D1B85C904DDC15B0771C8E3B877DBB6417A32CC159649C9FDB8"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "map.csv": (469114, "1EC4E4F85D89DD65CBBB31783249DE239C28B9E230BB0223CD6CFCF19F0B6DEB"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "mcheck.json": (64782, "8B64D2840C3FC9AFB79CC5EF1DB69C3E576E65CED7486B83E64E2D1B26CE3431"),
    "STATUS.md": (641, "EFD593429E3AC37859580629B2F8340ABC246D839443BACDD75AD62EF92BE8FE"),
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
    create_mutex = kernel32.CreateMutexW
    create_mutex.argtypes = [wintypes.LPVOID, wintypes.BOOL, wintypes.LPCWSTR]
    create_mutex.restype = wintypes.HANDLE
    close_handle = kernel32.CloseHandle
    close_handle.argtypes = [wintypes.HANDLE]
    close_handle.restype = wintypes.BOOL
    handle = create_mutex(None, False, r"Local\FAC-Tohoku-r38-mapping")
    if not handle:
        raise OSError(ctypes.get_last_error(), "Cannot create Tohoku r38 mutex")
    if ctypes.get_last_error() == 183:
        close_handle(handle)
        raise RuntimeError("Another Tohoku r38 transaction is active")
    try:
        yield
    finally:
        close_handle(handle)


def sem_records() -> list[dict[str, object]]:
    check = strict_json(QA / "sem-check.json")
    surface = check.get("semantic_surface")
    if not isinstance(surface, dict) or (
        surface.get("file_count"), surface.get("bytes"), surface.get("aggregate_sha256")
    ) != SEMANTIC_SURFACE:
        raise RuntimeError("Semantic surface receipt drift")
    records = surface.get("files")
    if not isinstance(records, list) or len(records) != 18:
        raise RuntimeError("Semantic file records are malformed")
    return records


def expected_tex_hashes() -> dict[str, str]:
    hashes = dict(strict_json(SOURCE / "check.json")["tex_sha256"])
    if len(hashes) != 119:
        raise RuntimeError("Predecessor TeX surface drift")
    hashes["homology.tex"] = EXPECTED_ARTIFACTS["homology.tex"][1]
    return hashes


def lock_paths(fresh: bool) -> list[Path]:
    sem = [SEM / str(item["name"]) for item in sem_records()]
    paths = [
        Path(__file__), ROOT / "srcmap" / "start_build_tohoku_r38.py",
        ROOT / "srcmap" / "start_build_tohoku_r38.ps1",
        *[SOURCE / name for name in EXPECTED_SOURCE],
        *[QA / name for name in EXPECTED_QA],
        *[AUTHORITY / name for name in EXPECTED_AUTHORITY],
        *sem,
    ]
    if fresh:
        paths.extend(ROOT / name for name in EXPECTED_TOOLS)
        paths.extend(ROOT / name for name in expected_tex_hashes())
        paths.extend(ROOT / name for name in EXPECTED_ARTIFACTS)
    elif TARGET.exists():
        paths.extend(path for path in TARGET.iterdir() if path.is_file())
    return paths


def verify_execution_attestation() -> dict[str, object]:
    attestation = globals().get("EXECUTION_ATTESTATION")
    if not isinstance(attestation, dict) or set(attestation) != {"bootstrap", "builder"}:
        raise RuntimeError("Run through start_build_tohoku_r38.py")
    bootstrap = attestation.get("bootstrap")
    if bootstrap != {
        "path": "srcmap/start_build_tohoku_r38.py",
        "contract": "read_once_then_execute_builder_same_bytes",
    }:
        raise RuntimeError("Bootstrap attestation drift")
    builder = attestation.get("builder")
    if not isinstance(builder, dict) or set(builder) != {
        "path", "bytes", "sha256", "contract"
    }:
        raise RuntimeError("Builder attestation shape drift")
    if (
        builder.get("path") != "srcmap/build_tohoku_r38.py"
        or builder.get("contract") != "read_hash_compile_and_exec_same_payload"
        or identity(Path(__file__)) != (builder.get("bytes"), builder.get("sha256"))
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
    predecessor = strict_json(SOURCE / "r37-check.json")
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
    sem_validation = strict_json(SEM / "validation.json")
    if sem_validation.get("status") != "PASS" or sem_validation.get("errors") != []:
        raise RuntimeError("Semantic validation is not PASS")
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
    if aggregate(current_sem) != SEMANTIC_SURFACE[2]:
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
    cfg["dossier_id"] = "tohoku_r38"
    cfg["inputs"]["primary"] = {
        **record(SEM / "nodes.csv", "nodes.csv"),
        "filename": "nodes.csv",
        "source_file": "sem/r13/nodes.csv",
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
        **record(SEM / "manifest.json", "sem/r13 manifest"),
        "filename": "manifest.json",
    }
    cfg["inputs"]["sem_validation"] = {
        **record(SEM / "validation.json", "sem/r13 validation"),
        "filename": "validation.json",
    }
    cfg["inputs"]["sem_input"] = {
        **record(QA / "sem-input.json", "v68r31 sem input"),
        "filename": "sem-input.json",
    }
    cfg["inputs"]["sem_check"] = {
        **record(QA / "sem-check.json", "v68r31 sem check"),
        "filename": "sem-check.json",
    }
    cfg["semantic_successor"] = {
        "generation": "sem/r13",
        "surface_files": SEMANTIC_SURFACE[0],
        "surface_bytes": SEMANTIC_SURFACE[1],
        "surface_sha256": SEMANTIC_SURFACE[2],
        "receipt": record(QA / "sem-check.json", "qa/v68r31/sem-check.json"),
    }
    return cfg


def make_decisions() -> bytes:
    fields, rows = load_csv(SOURCE / "dec.csv")
    if [row["decision_id"] for row in rows] != [
        f"D{number:06d}" for number in range(1, 992)
    ]:
        raise RuntimeError("Predecessor decision sequence drift")
    if rows[-1]["decision_id"] != "D000991":
        raise RuntimeError("Unexpected predecessor decision tail")
    appended = csv_bytes(fields, DECISION_ROWS)
    return (SOURCE / "dec.csv").read_bytes() + appended[appended.index(b"\n") + 1 :]


def make_issues() -> bytes:
    fields, rows = load_csv(SOURCE / "issues.csv")
    if [row["issue_id"] for row in rows] != [
        f"I{number:06d}" for number in range(1, 27)
    ]:
        raise RuntimeError("Predecessor source-issue sequence drift")
    active = [row["issue_id"] for row in rows if row["status"] != "resolved"]
    if active:
        raise RuntimeError(f"Unexpected predecessor active source issues: {active}")
    if ISSUE_ROWS:
        raise RuntimeError("D000992 must not append a source-issue row")
    return (SOURCE / "issues.csv").read_bytes()


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


def verify_builds() -> dict[str, object]:
    forbidden = [
        r"(?m)^!", r"(?m)^LaTeX Warning:", r"(?m)^Package .* Warning:",
        r"undefined references", r"undefined citations",
        r"Rerun to get cross-references right", r"Label\(s\) may have changed",
    ]
    builds: dict[str, object] = {}
    for chapter, spec in BUILD_SPECS.items():
        text = (ROOT / f"{chapter}.log").read_text(
            encoding="utf-8", errors="replace"
        )
        hits = [pattern for pattern in forbidden if re.search(pattern, text)]
        if hits:
            raise RuntimeError(f"{chapter} build diagnostics failed: {hits}")
        build = {
            "tex": record(ROOT / f"{chapter}.tex"),
            "log": record(ROOT / f"{chapter}.log"),
            "pdf": record(ROOT / f"{chapter}.pdf"),
            "pdf_pages": spec["pdf_pages"],
            "undefined_references": 0,
            "undefined_citations": 0,
            "rerun_notices": 0,
            "new_block_overfull_boxes": 0,
            "visual_reviewed_pages": spec["visual_reviewed_pages"],
        }
        if chapter == "homology":
            build["aux"] = record(ROOT / "homology.aux")
        builds[chapter] = build
    return builds


def verify_deltas(root: Path) -> dict[str, object]:
    intake = strict_json(root / "intake.json")
    check = strict_json(root / "check.json")
    mcheck = strict_json(root / "mcheck.json")
    for name, receipt in (("intake", intake), ("scan", check), ("map", mcheck)):
        if receipt.get("status") != "PASS" or receipt.get("errors") != []:
            raise RuntimeError(f"{name} receipt is not PASS")
    if mcheck.get("outputs_promoted") is not True:
        raise RuntimeError("Mapping outputs were not promoted")

    if strict_json(root / "cfg.json") != make_config():
        raise RuntimeError("Configuration does not exactly bind sem/r13")
    actual_outputs = {name: identity(root / name) for name in sorted(PAYLOAD)}
    if actual_outputs != EXPECTED_OUTPUTS:
        raise RuntimeError(f"Canonical output identity drift: {actual_outputs}")
    if (root / "STATUS.md").read_bytes() != STATUS_BYTES or identity(
        root / "STATUS.md"
    ) != EXPECTED_OUTPUTS["STATUS.md"]:
        raise RuntimeError("Status canonical-byte identity drift")
    for name in ("topics.csv", "tmap.csv", "ucand.csv", "units.csv", "issues.csv"):
        if (root / name).read_bytes() != (SOURCE / name).read_bytes():
            raise RuntimeError(f"Unexpected byte drift: {name}")

    old_unit_fields, old_units = load_csv(SOURCE / "units.csv")
    new_unit_fields, new_units = load_csv(root / "units.csv")
    if old_unit_fields != new_unit_fields:
        raise RuntimeError("Unit field surface drift")
    if [row["id"] for row in new_units] != [row["id"] for row in old_units]:
        raise RuntimeError("Unit ID/order drift")
    for old_row, new_row in zip(old_units, new_units, strict=True):
        if old_row != new_row:
            changed = sorted(field for field in old_row if old_row[field] != new_row[field])
            raise RuntimeError(f"Unexpected unit delta {new_row['id']}: {changed}")

    old_dec = (SOURCE / "dec.csv").read_bytes()
    new_dec = (root / "dec.csv").read_bytes()
    if not new_dec.startswith(old_dec):
        raise RuntimeError("Decision ledger is not an exact append-only successor")
    if new_dec != make_decisions():
        raise RuntimeError("Decision ledger bytes differ from the canonical successor")
    if identity(root / "dec.csv") != EXPECTED_OUTPUTS["dec.csv"]:
        raise RuntimeError("Decision ledger canonical-byte identity drift")
    _, decisions = load_csv(root / "dec.csv")
    if [row["decision_id"] for row in decisions] != [
        f"D{number:06d}" for number in range(1, 993)
    ]:
        raise RuntimeError("Decision sequence is not D000001..D000992")
    if decisions[-1:] != DECISION_ROWS:
        raise RuntimeError("D000992 differs from the frozen row")

    if (root / "issues.csv").read_bytes() != make_issues():
        raise RuntimeError("Source-issue ledger is not the exact append-only successor")
    if identity(root / "issues.csv") != EXPECTED_OUTPUTS["issues.csv"]:
        raise RuntimeError("Source-issue ledger canonical-byte identity drift")
    _, issues = load_csv(root / "issues.csv")
    if [row["issue_id"] for row in issues] != [
        f"I{number:06d}" for number in range(1, 27)
    ]:
        raise RuntimeError("Source-issue sequence drift")
    if len(issues) != 26:
        raise RuntimeError("Source-issue count drift")
    active_issues = [row["issue_id"] for row in issues if row["status"] != "resolved"]
    if active_issues:
        raise RuntimeError(f"Unexpected active source issues: {active_issues}")

    expected_scan_counts = {
        "labels": 22034,
        "official_tags_joined": 21437,
        "tex_files": 119,
        "topic_candidates": 1250,
        "topic_coverage": {"direct": 13},
        "topics": 13,
    }
    if check.get("counts") != expected_scan_counts:
        raise RuntimeError(f"Scan counts drift: {check.get('counts')}")
    if check.get("tex_sha256") != expected_tex_hashes():
        raise RuntimeError("TeX hash dictionary drift")
    if check.get("sha256", {}).get("tags/tags") != EXPECTED_TOOLS["tags/tags"][1]:
        raise RuntimeError("Tags hash drift in scan receipt")
    old_check = strict_json(SOURCE / "check.json")
    expected_check = json.loads(json.dumps(old_check))
    expected_check["counts"] = expected_scan_counts
    expected_check["warnings"] = [
        *old_check["warnings"][:9],
        *sorted([
            *old_check["warnings"][9:],
            *[
                f"TeX label has no official tag in this snapshot: {label}"
                for label in NEW_LOCAL_LABELS
            ],
        ]),
    ]
    expected_check["tex_sha256"] = expected_tex_hashes()
    expected_check["sha256"] = {
        key.replace("tohoku_r37/", "tohoku_r38/"): value
        for key, value in old_check["sha256"].items()
    }
    expected_check["sha256"].update({
        "tohoku_r38/stx.csv": EXPECTED_OUTPUTS["stx.csv"][1],
        "tohoku_r38/tcand.csv": EXPECTED_OUTPUTS["tcand.csv"][1],
    })
    if check != expected_check:
        raise RuntimeError("Scan receipt is not the exact bounded two-label successor")
    if identity(root / "check.json") != EXPECTED_OUTPUTS["check.json"]:
        raise RuntimeError("Scan receipt canonical-byte identity drift")

    _, old_stx = load_csv(SOURCE / "stx.csv")
    _, new_stx = load_csv(root / "stx.csv")
    old_labels = [row["full_label"] for row in old_stx]
    new_labels = [row["full_label"] for row in new_stx]
    if len(old_labels) != len(set(old_labels)) or len(new_labels) != len(set(new_labels)):
        raise RuntimeError("Stacks index full-label uniqueness drift")
    if set(new_labels) - set(old_labels) != set(NEW_LOCAL_LABELS):
        raise RuntimeError("Stacks index added-label surface drift")
    if set(old_labels) - set(new_labels):
        raise RuntimeError("Stacks index unexpectedly dropped labels")
    old_stx_by_label = {row["full_label"]: row for row in old_stx}
    new_stx_by_label = {row["full_label"]: row for row in new_stx}
    for label, expected in EXPECTED_NEW_LABEL_ROWS.items():
        row = new_stx_by_label[label]
        if row["tag"] != "" or any(row[field] != value for field, value in expected.items()):
            raise RuntimeError(f"New Stacks index row drift: {label}")
    index_line_shifts: list[str] = []
    for label in sorted(set(old_stx_by_label) & set(new_stx_by_label)):
        old_row = old_stx_by_label[label]
        new_row = new_stx_by_label[label]
        changed = {field for field in old_row if old_row[field] != new_row[field]}
        if changed:
            if changed != {"line"} or int(new_row["line"]) - int(old_row["line"]) != 312:
                raise RuntimeError(f"Unexpected Stacks index row shift: {label}")
            index_line_shifts.append(label)
    if len(index_line_shifts) != 168:
        raise RuntimeError(f"Stacks index line-shift count drift: {len(index_line_shifts)}")

    _, old_tcand = load_csv(SOURCE / "tcand.csv")
    _, new_tcand = load_csv(root / "tcand.csv")
    old_tcand_by_key = {(row["topic_id"], row["full_label"]): row for row in old_tcand}
    new_tcand_by_key = {(row["topic_id"], row["full_label"]): row for row in new_tcand}
    if len(old_tcand_by_key) != len(old_tcand) or len(new_tcand_by_key) != len(new_tcand):
        raise RuntimeError("Topic-candidate key uniqueness drift")
    candidate_added = tuple(sorted(set(new_tcand_by_key) - set(old_tcand_by_key)))
    candidate_dropped = tuple(sorted(set(old_tcand_by_key) - set(new_tcand_by_key)))
    if candidate_added != EXPECTED_TOPIC_CANDIDATE_ADDED:
        raise RuntimeError(f"Topic-candidate additions drift: {candidate_added}")
    if candidate_dropped != EXPECTED_TOPIC_CANDIDATE_DROPPED:
        raise RuntimeError(f"Topic-candidate drops drift: {candidate_dropped}")
    candidate_line_shifts: list[tuple[str, str]] = []
    for key in sorted(set(old_tcand_by_key) & set(new_tcand_by_key)):
        old_row = old_tcand_by_key[key]
        new_row = new_tcand_by_key[key]
        changed = {field for field in old_row if old_row[field] != new_row[field]}
        if changed:
            if changed != {"line"} or int(new_row["line"]) - int(old_row["line"]) != 312:
                raise RuntimeError(f"Unexpected topic-candidate row shift: {key}")
            candidate_line_shifts.append(key)
    if len(candidate_line_shifts) != 89:
        raise RuntimeError(
            f"Topic-candidate line-shift count drift: {len(candidate_line_shifts)}"
        )

    old_map_fields, old_map = load_csv(SOURCE / "map.csv")
    new_map_fields, new_map = load_csv(root / "map.csv")
    if old_map_fields != new_map_fields:
        raise RuntimeError("Map field surface drift")
    if [row["unit_id"] for row in new_map] != [row["unit_id"] for row in old_map]:
        raise RuntimeError("Map unit ID/order drift")
    decisions_by_unit = {row["unit_id"]: row for row in DECISION_ROWS}
    exact_changed_fields = {
        "tohoku:thm:2.2.2:p1": {
            "decision_id", "disposition", "review_state", "stacks_labels",
            "stacks_tags", "rationale",
        },
    }
    substantive: list[str] = []
    for old_row, new_row in zip(old_map, new_map, strict=True):
        changed = {field for field in old_row if old_row[field] != new_row[field]}
        decision = decisions_by_unit.get(new_row["unit_id"])
        if decision is None:
            if changed:
                raise RuntimeError(
                    f"Unexpected map delta {new_row['unit_id']}: {sorted(changed)}"
                )
            continue
        expected_values = {
            "decision_id": decision["decision_id"],
            "disposition": decision["disposition"],
            "review_state": decision["review_state"],
            "stacks_labels": decision["stacks_labels"],
            "stacks_tags": "",
            "rationale": decision["rationale"],
        }
        if changed != exact_changed_fields[new_row["unit_id"]]:
            raise RuntimeError(
                f"Unexpected {decision['decision_id']} map fields: {sorted(changed)}"
            )
        if any(new_row[field] != value for field, value in expected_values.items()):
            raise RuntimeError(
                f"Map row does not exactly realize {decision['decision_id']}"
            )
        substantive.append(new_row["unit_id"])
    if substantive != ["tohoku:thm:2.2.2:p1"]:
        raise RuntimeError("Unexpected substantive map change order")
    if identity(root / "map.csv") != EXPECTED_OUTPUTS["map.csv"]:
        raise RuntimeError("Map canonical-byte identity drift")

    expected_counts = {
        "active_graph_corrections": 0,
        "active_source_issues": 0,
        "candidate_units": 0,
        "decided_units": 678,
        "decisions": 992,
        "dispositions": {
            "example_or_remark": 84,
            "existing_equivalent": 343,
            "existing_stronger": 38,
            "existing_weaker": 11,
            "extend_existing": 24,
            "historical_reference": 33,
            "new_section": 6,
            "new_statement": 25,
            "structural_only": 426,
        },
        "graph_corrections": 0,
        "review_units": 0,
        "source_issues": 26,
        "unit_candidates": 0,
        "units": 990,
    }
    if mcheck.get("counts") != expected_counts:
        raise RuntimeError(f"Mapping counts drift: {mcheck.get('counts')}")
    if mcheck.get("warnings") != check.get("warnings"):
        raise RuntimeError("Mapping warning surface differs from scan warnings")
    old_mcheck = strict_json(SOURCE / "mcheck.json")
    expected_mcheck = json.loads(json.dumps(old_mcheck))
    expected_mcheck["counts"] = expected_counts
    expected_mcheck["warnings"] = expected_check["warnings"]
    expected_mcheck["sha256"] = {
        key.replace("tohoku_r37/", "tohoku_r38/"): value
        for key, value in old_mcheck["sha256"].items()
    }
    for name in (
        "cfg.json", "dec.csv", "intake.json", "issues.csv", "map.csv",
        "ucand.csv", "units.csv",
    ):
        expected_mcheck["sha256"][f"tohoku_r38/{name}"] = EXPECTED_OUTPUTS[name][1]
    if mcheck != expected_mcheck:
        raise RuntimeError("Mapping receipt is not the exact bounded successor")
    if identity(root / "mcheck.json") != EXPECTED_OUTPUTS["mcheck.json"]:
        raise RuntimeError("Mapping receipt canonical-byte identity drift")
    _, candidates = load_csv(root / "ucand.csv")
    if candidates:
        raise RuntimeError("Unexpected undecided unit candidates")
    gap_count = sum(
        expected_counts["dispositions"][name]
        for name in ("existing_weaker", "extend_existing", "new_statement", "new_section")
    )
    if gap_count != 66:
        raise RuntimeError(f"Gap-class arithmetic drift: {gap_count}")
    return {
        "decisions": DECISION_ROWS,
        "resolved_source_issues": [],
        "active_source_issues": active_issues,
        "semantic_title_changes": [],
        "scan_counts": check["counts"],
        "mapping_counts": mcheck["counts"],
        "substantive_map_changes": substantive,
        "stacks_index_line_shifts": {"count": len(index_line_shifts), "delta": 312},
        "topic_candidate_churn": {
            "added": [list(key) for key in candidate_added],
            "dropped": [list(key) for key in candidate_dropped],
            "line_only_shifts": len(candidate_line_shifts),
            "line_delta": 312,
        },
        "remaining_gap_class_dispositions": gap_count,
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
    builds: dict[str, object] | None = None,
    execution: dict[str, object] | None = None,
) -> dict[str, object]:
    sources = source_records()
    semantic = [record(SEM / str(item["name"])) for item in sem_records()]
    return {
        "schema": "tohoku-stacks-mapping-successor-r38-v1",
        "status": "PASS",
        "errors": [],
        "predecessor_dossier": {
            "name": "tohoku_r37",
            "files": sources,
            "file_count": len(sources),
            "bytes": sum(int(item["bytes"]) for item in sources),
            "aggregate_sha256": aggregate(sources),
        },
        "semantic_source": {
            "generation": "sem/r13",
            "files": semantic,
            "file_count": len(semantic),
            "bytes": sum(int(item["bytes"]) for item in semantic),
            "aggregate_sha256": aggregate(semantic),
            "sem_input": record(QA / "sem-input.json", "qa/v68r31/sem-input.json"),
            "sem_check": record(QA / "sem-check.json", "qa/v68r31/sem-check.json"),
        },
        "execution": execution if execution is not None else {
            "attestation": attestation,
            "bootstrap": record(ROOT / "srcmap" / "start_build_tohoku_r38.py"),
            "powershell_envelope": record(ROOT / "srcmap" / "start_build_tohoku_r38.ps1"),
            "dependencies": {name: record(ROOT / name) for name in sorted(EXPECTED_TOOLS)},
            "contract": "same_bytes_bootstrap; exact_inputs_locked_against_write_delete_through_generation_replay_and_promotion",
        },
        "git": git,
        "builds": verify_builds() if builds is None else builds,
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": [
            "No Git command is executed by this mapping successor.",
            "No Git commit or push is made by this receipt.",
            "No remote-server freshness check is performed.",
            "Existing-target replay treats the live Stacks TeX and build artifacts as creation-time evidence bound by the receipt; it does not assert that those external files remain byte-identical later.",
            "The outer-envelope sentinel prevents accidental direct-bootstrap use but is not cryptographic provenance against a same-user forged invocation.",
            "The Stacks scan binds the exact live integrated worktree, not the frozen HEAD tree.",
            "The transaction denies write/delete access to every existing consumed file; hostile same-user mutation of directory namespaces is outside this lock contract.",
            "No release, publication, upload, DOI, Zenodo, rights, or whole-paper gate is closed.",
            "66 Tohoku gap-class dispositions remain after D000992.",
            "All 26 recorded source issues are resolved; no active source issue remains.",
        ],
    }


def verify_existing(
    git: dict[str, object], attestation: dict[str, object]
) -> dict[str, object]:
    require_plain_directory(TARGET)
    names = {path.name for path in TARGET.iterdir() if path.is_file()}
    if names != PAYLOAD | {"r38-check.json"} or any(path.is_dir() for path in TARGET.iterdir()):
        raise RuntimeError("Existing r38 dossier surface drift")
    deltas = verify_deltas(TARGET)
    receipt = strict_json(TARGET / "r38-check.json")
    if receipt.get("git") != EXPECTED_GIT_NONCLAIM:
        raise RuntimeError("Existing receipt Git nonclaim drift")
    builds = receipt.get("builds")
    if not isinstance(builds, dict):
        raise RuntimeError("Existing builds receipt is malformed")
    expected_builds: dict[str, object] = {}
    for chapter, spec in BUILD_SPECS.items():
        expected_builds[chapter] = {
            "tex": {
                "name": f"{chapter}.tex",
                "bytes": EXPECTED_ARTIFACTS[f"{chapter}.tex"][0],
                "sha256": EXPECTED_ARTIFACTS[f"{chapter}.tex"][1],
            },
            "log": {
                "name": f"{chapter}.log",
                "bytes": EXPECTED_ARTIFACTS[f"{chapter}.log"][0],
                "sha256": EXPECTED_ARTIFACTS[f"{chapter}.log"][1],
            },
            "pdf": {
                "name": f"{chapter}.pdf",
                "bytes": EXPECTED_ARTIFACTS[f"{chapter}.pdf"][0],
                "sha256": EXPECTED_ARTIFACTS[f"{chapter}.pdf"][1],
            },
            "pdf_pages": spec["pdf_pages"],
            "undefined_references": 0,
            "undefined_citations": 0,
            "rerun_notices": 0,
            "new_block_overfull_boxes": 0,
            "visual_reviewed_pages": spec["visual_reviewed_pages"],
        }
        if chapter == "homology":
            expected_builds[chapter]["aux"] = {
                "name": "homology.aux",
                "bytes": EXPECTED_ARTIFACTS["homology.aux"][0],
                "sha256": EXPECTED_ARTIFACTS["homology.aux"][1],
            }
    if builds != expected_builds:
        raise RuntimeError("Existing builds receipt drift")
    execution = receipt.get("execution")
    if not isinstance(execution, dict):
        raise RuntimeError("Existing execution receipt is malformed")
    expected_execution = {
        "attestation": attestation,
        "bootstrap": record(ROOT / "srcmap" / "start_build_tohoku_r38.py"),
        "powershell_envelope": record(ROOT / "srcmap" / "start_build_tohoku_r38.ps1"),
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
        TARGET, receipt["git"], attestation, deltas, builds, execution
    )
    if receipt != expected:
        raise RuntimeError("Existing r38 receipt replay mismatch")
    return receipt


def main_locked(attestation: dict[str, object]) -> int:
    target_entry = os.path.lexists(TARGET)
    stage_entry = os.path.lexists(STAGE)
    if target_entry and stage_entry:
        raise RuntimeError("Target and unresolved transaction coexist")
    if stage_entry:
        raise FileExistsError(f"Unresolved transaction exists: {STAGE}")
    fresh = not target_entry
    with deny_write_delete(lock_paths(fresh)):
        git, _ = verify_inputs(fresh)
        if target_entry:
            receipt = verify_existing(git, attestation)
            print(json.dumps(receipt, ensure_ascii=False, indent=2))
            return 0
        STAGE.mkdir()
        exclusive_write(STAGE / "cfg.json", json_bytes(make_config()))
        exclusive_write(STAGE / "topics.csv", (SOURCE / "topics.csv").read_bytes())
        exclusive_write(STAGE / "dec.csv", make_decisions())
        exclusive_write(STAGE / "issues.csv", make_issues())
        run_tool("intake.py", str(STAGE), str(SEM / "nodes.csv"), *intake_args())
        run_tool("scan.py", str(STAGE))
        run_tool("map.py", str(STAGE))
        exclusive_write(STAGE / "STATUS.md", STATUS_BYTES)
        deltas = verify_deltas(STAGE)
        receipt = receipt_payload(STAGE, git, attestation, deltas)
        exclusive_write(STAGE / "r38-check.json", json_bytes(receipt))
        if (
            {path.name for path in STAGE.iterdir() if path.is_file()}
            != PAYLOAD | {"r38-check.json"}
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
