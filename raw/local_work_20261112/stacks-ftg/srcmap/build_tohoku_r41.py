#!/usr/bin/env python3
"""Build the no-overwrite Tohoku issue-only mapping successor I000029."""

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
SOURCE = ROOT / "tohoku_r40"
TARGET = ROOT / "tohoku_r41"
STAGE = ROOT / ".tohoku-r41-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r15"
SEM_QA = PROJECT / "qa" / "v68r35"
READER_QA = PROJECT / "qa" / "v68r34" / "check.json"
P142_SOURCE = PROJECT / "production" / "p142_fix1" / "check.json"
READER_BUILD = PROJECT / "build" / "v068c3r13" / "build.json"
AUTHORITY = PROJECT / "authority_snapshot"

EXPECTED_GIT_NONCLAIM = {
    "inspection_performed": False,
    "reason": "No Git operation was needed for this bounded local successor.",
    "predecessor_receipt": {
        "path": "tohoku_r40/r40-check.json",
        "bytes": 22993,
        "sha256": "9876C39834D20F9092945EB17772D4B87C6B39F395A0934D1883EA413D446059",
    },
    "remote_server_freshness_verified": False,
}

EXPECTED_SOURCE = {
    "STATUS.md": (1027, "5B822EA90A4AC8354288960BEAB7ED464325C9AE45381336D6CCAA730082F45C"),
    "cfg.json": (5194, "D27637ECA3FC0D8B8D42C86C55B3189F7998165B21EF40820C59E4E1FDF6282E"),
    "check.json": (75491, "C4B750A635D397BF8A9C26A39B3E320F50345B7A85645880F553547DBF9317C6"),
    "dec.csv": (355505, "B7533F85345E134ECD013221168A0CC1A54DA8C94AFA46CA1D9591DBDBD82029"),
    "intake.json": (1878, "3213469B06D5C7AE58587BA214710172C63A5762A9339EFCF1DE3EB8009D4BFB"),
    "issues.csv": (28045, "84749B6574D937A8D45D342BDE4F97DDA85CB43502CB73F76DDC6B1D4CC615B0"),
    "map.csv": (470572, "992BBCE3ECA7668A6B0B958F15D0E1CEC2CA76C6EE6607C8722024B3DF01D9ED"),
    "mcheck.json": (65319, "AA3C22E1466065F89F122C0D41E4BAEBFD536081BE248F41C3C1E8689EB63709"),
    "r40-check.json": (22993, "9876C39834D20F9092945EB17772D4B87C6B39F395A0934D1883EA413D446059"),
    "stx.csv": (5270117, "319AE1E10C1F1607FF12603C25D0DA412BEDCE1795110EFCE6950D58CB03CB36"),
    "tcand.csv": (480052, "21C181693AF526ACF4CAEB997E8EA86927E1B9BD864B00CADE96E671CF173548"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (392090, "DC5A9609F706B7C8823E6C5495510D365A38E95AE81F1C97071D0B1217480116"),
}
EXPECTED_SOURCE_SURFACE = (
    15,
    7173280,
    "36815199A687DCA7C0AE6258ED2C0BF50582BDF2A698CC1283531344C361544A",
)

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

EXPECTED_SEM_QA = {
    "sem-input.json": (298664, "21DE25BD3E5B30F1FFC6F8D2C6C3F5EB284E864B0EDB49EAD2EC3515E84877C6"),
    "sem-check.json": (6726, "F268C2D8553988384C650B011DB3594467F59588E05412C7A56F2FC9C5C924A9"),
}
EXPECTED_REPAIR_RECEIPTS = {
    "production/p142_fix1/check.json": (
        P142_SOURCE,
        7250,
        "61DC1736262199D5909580C85756ADFA90C59C7D3BF12ADE4848995DA13A2A25",
    ),
    "build/v068c3r13/build.json": (
        READER_BUILD,
        97649,
        "982525DD08B21E8F2C4A04E6F3D1B7FF99F5547E79F95F28496DC6B2CB0FE2EE",
    ),
    "qa/v68r34/check.json": (
        READER_QA,
        13181,
        "188C5E4A6930CBC1597D8582C7E935AAD6160FF0344ABF3401ABC7E7C1A04BD0",
    ),
}

EXPECTED_AUTHORITY = {
    "jstage_part_I_9_2_119.pdf": (7305283, "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF"),
    "jstage_part_II_9_3_185.pdf": (3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53"),
}

EXPECTED_ARTIFACTS = {
    "homology.tex": (373802, "57BD4532F633F36C3F20DD3D2DEC7C45B1B11354FB9A553479A3B0FB73DE5F7A"),
    "homology.aux": (28557, "1F2B34C339F5787074F0D0386CD195C56EDB86B32A34069DABBF46980DC6E546"),
    "homology.log": (39285, "6B2595EB746B33D1EC8B0D3A7BBDF073C2F3FFE9502B4539FF0EDE13E99F4A6C"),
    "homology.pdf": (1070505, "CEDFF4A8641083C9E5076DD440D51DA00FFC5A849396876D482F330C91E595F7"),
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
    "homology": {"pdf_pages": 114, "visual_reviewed_pages": [55, 56]},
    "modules": {"pdf_pages": 58, "visual_reviewed_pages": [5, 6]},
    "cohomology": {"pdf_pages": 214, "visual_reviewed_pages": [162, 163, 164]},
    "injectives": {"pdf_pages": 38, "visual_reviewed_pages": [18, 19, 20]},
}

EXPECTED_AUX_LABEL_LINES = (
    r"\newlabel{lemma-finite-effaceability-universality}{{13.18}{48}{Finite effaceability criterion}{subsection.13.18}{}}",
    r"\newlabel{equation-finite-effaceability-factor}{{13.18.1}{49}{Cohomological delta-functors}{equation.13.18.1}{}}",
    r"\newlabel{lemma-right-satellites-exactness-criterion}{{13.19}{51}{Exactness criterion for right satellites}{subsection.13.19}{}}",
    r"\newlabel{equation-right-satellites-nested-subobjects}{{13.19.1}{51}{Exactness criterion for right satellites}{equation.13.19.1}{}}",
    r"\newlabel{lemma-half-exact-nested-subobjects-enough-injectives}{{13.20}{55}{Enough injectives and the satellite exactness condition}{subsection.13.20}{}}",
)

NEW_LOCAL_LABELS: tuple[str, ...] = ()
EXPECTED_NEW_LABEL_ROWS: dict[str, dict[str, str]] = {}
EXPECTED_TOPIC_CANDIDATE_ADDED: tuple[tuple[str, str], ...] = ()

DECISION_ROWS: list[dict[str, str]] = []

ISSUE_ROWS = [
    {
        "issue_id": "I000029",
        "unit_id": "tohoku:thm:2.2.2:dual",
        "status": "open",
        "kind": "source_global_universality_scope_error",
        "claim": (
            "The printed p. 142 consequence calls the glued all-integer satellite system a "
            "universal graded connecting functor. Printed p. 140 gives an initial universal "
            "property only on finite nonnegative right truncations, while degree reversal "
            "transports the left step-minus-one construction's terminal property to finite "
            "nonpositive truncations; the opposite halfwise variances do not produce global "
            "initial universality."
        ),
        "evidence_labels": (
            "homology-lemma-finite-effaceability-universality;"
            "homology-lemma-right-satellites-injective-effacements;"
            "homology-lemma-graded-connecting-functor-dualities"
        ),
        "evidence": (
            "Official Part I SHA-256 "
            "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF, "
            "printed pp. 140 and 142. For F=(-) tensor_Z Z/2 on Ab, the glued exact system "
            "has S^{-1}(A)=A[2] and S^{-2}=0. The graded connecting functor U concentrated "
            "in degree -1 receives both the zero map and the identity in degree -1 from S "
            "with the same zero degree-zero component, so initial uniqueness fails."
        ),
        "control": (
            "Preserve the printed phrase in diplomatic French. Keep the D000214 mapping "
            "unchanged while creating production/p142_fix2, a fresh bilingual reader and "
            "visual witness, a stable-ID semantic successor reusing "
            "tohoku:thm:2.2.2:dual and tohoku:occ:p142:o003, and the audited Stacks "
            "left-satellite lemma. Resolve only in a later mapping successor whose "
            "replacement decision explicitly asserts halfwise universality and denies "
            "global all-integer universality."
        ),
        "resolution_decision": "",
    },
]

SEMANTIC_SURFACE = (
    18,
    2028413,
    "3F69C64B47DD6B9EE87CDF99F2B0CA06D18959C88C3D30F762AF9B9BBC299A8F",
)
EXPECTED_P142_THEOREM_TITLE = (
    "it is necessary and sufficient that F satisfy the following conditions: F is "
    "half-exact, and for P Q R in C , the kernel of F(Q/P) F(R/P) is contained in "
    "the image of F(Q) F(Q/P) . These conditions are always satisfied if F is left "
    "exact or right exact."
)
EXPECTED_P142_FOOTNOTE_TITLE = (
    "Added in proof. This condition is also automatically satisfied if every object of C "
    "is isomorphic to a subobject of an injective object; see [6, Chap. III]."
)
EXPECTED_P142_PROVENANCE = (
    "TOH-P142-SEM-002 + exact virtual split of aligned reader p142 segment"
)

EXPECTED_SCAN_COUNTS = {
    "labels": 22039,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1255,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}
EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 1,
    "candidate_units": 0,
    "decided_units": 679,
    "decisions": 995,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 346,
        "existing_stronger": 38,
        "existing_weaker": 10,
        "extend_existing": 24,
        "historical_reference": 33,
        "new_section": 6,
        "new_statement": 24,
        "structural_only": 426,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 29,
    "unit_candidates": 0,
    "units": 991,
}

STATUS_BYTES = (
    "# Tohoku Stacks mapping status\n\n"
    "- Semantic source remains the exact independently sealed local-unpublished sem/r15; no semantic byte changes occur.\n"
    "- Stable source inventory remains 991 units.\n"
    "- The decision ledger remains byte-identical through D000995; D000214 and all map substantive fields remain unchanged.\n"
    "- Append-only issue I000029 records the printed p. 142 global-universality scope error as open; it does not resolve or remap the theorem.\n"
    "- There are 29 recorded source issues: 28 resolved and exactly I000029 open.\n"
    "- 64 gap-class dispositions remain.\n"
    "- This local dossier makes no release, publication, remote-freshness, DOI, rights, or completion claim.\n"
).encode("utf-8")

PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv",
    "issues.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv",
    "map.csv", "ucand.csv", "mcheck.json", "STATUS.md",
}

EXPECTED_OUTPUTS = {
    "STATUS.md": (667, "80646BBF6EF4B25229306E520F4E00D872D6DD9B98119649C6D32BB50AC52136"),
    "cfg.json": (5194, "27B69C9022454C2DC15FBE8552C35BD38416EF8547C992F72E68B54CDCEA5E80"),
    "check.json": (75491, "872B81C44D5C595A7E36400D514EFA66EF9E363F684773E0BBADD53F4356B386"),
    "dec.csv": (355505, "B7533F85345E134ECD013221168A0CC1A54DA8C94AFA46CA1D9591DBDBD82029"),
    "intake.json": (1878, "3213469B06D5C7AE58587BA214710172C63A5762A9339EFCF1DE3EB8009D4BFB"),
    "issues.csv": (29540, "1C00B88F578BFDE2C0F178A65D0616C6BAAED4597F2E3EFCBC5BBA0380882CF8"),
    "map.csv": (470572, "992BBCE3ECA7668A6B0B958F15D0E1CEC2CA76C6EE6607C8722024B3DF01D9ED"),
    "mcheck.json": (65319, "98EDB484CA1487D41A1241ADCFB02AD79012BB8254E6352E9C312E486D228C81"),
    "stx.csv": (5270117, "319AE1E10C1F1607FF12603C25D0DA412BEDCE1795110EFCE6950D58CB03CB36"),
    "tcand.csv": (480052, "21C181693AF526ACF4CAEB997E8EA86927E1B9BD864B00CADE96E671CF173548"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (392090, "DC5A9609F706B7C8823E6C5495510D365A38E95AE81F1C97071D0B1217480116"),
}
EXPECTED_OUTPUT_SURFACE = (
    14,
    7151422,
    "E764BC4E62A56C811358FDA937A87AFA5D8BD040CF32DF84EFA7A6CDD26037AE",
)

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), digest(data)


def record(path: Path, name: str | None = None) -> dict[str, object]:
    size, sha256 = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": sha256}


def constant_record(name: str, expected: tuple[int, str]) -> dict[str, object]:
    return {"name": Path(name).name, "bytes": expected[0], "sha256": expected[1]}


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
    handle = create_mutex(None, False, r"Local\FAC-Tohoku-r41-mapping")
    if not handle:
        raise OSError(ctypes.get_last_error(), "Cannot create Tohoku r41 mutex")
    if ctypes.get_last_error() == 183:
        close_handle(handle)
        raise RuntimeError("Another Tohoku r41 transaction is active")
    try:
        yield
    finally:
        close_handle(handle)


def sem_records() -> list[dict[str, object]]:
    check = strict_json(SEM_QA / "sem-check.json")
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
        raise RuntimeError("Predecessor TeX manifest drift")
    hashes["homology.tex"] = EXPECTED_ARTIFACTS["homology.tex"][1]
    return hashes


def lock_paths(fresh: bool) -> list[Path]:
    semantic = [SEM / str(item["name"]) for item in sem_records()]
    paths = [
        Path(__file__), ROOT / "srcmap" / "start_build_tohoku_r41.py",
        ROOT / "srcmap" / "start_build_tohoku_r41.ps1",
        *[SOURCE / name for name in EXPECTED_SOURCE],
        *[SEM_QA / name for name in EXPECTED_SEM_QA],
        *[item[0] for item in EXPECTED_REPAIR_RECEIPTS.values()],
        *[AUTHORITY / name for name in EXPECTED_AUTHORITY],
        *semantic,
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
        raise RuntimeError("Run through start_build_tohoku_r41.py")
    bootstrap = attestation.get("bootstrap")
    if bootstrap != {
        "path": "srcmap/start_build_tohoku_r41.py",
        "contract": "read_once_then_execute_builder_same_bytes",
    }:
        raise RuntimeError("Bootstrap attestation drift")
    builder = attestation.get("builder")
    if not isinstance(builder, dict) or set(builder) != {
        "path", "bytes", "sha256", "contract"
    }:
        raise RuntimeError("Builder attestation shape drift")
    if (
        builder.get("path") != "srcmap/build_tohoku_r41.py"
        or builder.get("contract") != "read_hash_compile_and_exec_same_payload"
        or identity(Path(__file__)) != (builder.get("bytes"), builder.get("sha256"))
    ):
        raise RuntimeError("Same-bytes builder attestation drift")
    return attestation

def verify_semantic_and_repair_chain() -> None:
    sem_check = strict_json(SEM_QA / "sem-check.json")
    if (
        sem_check.get("schema") != "tohoku-semantic-local-successor-check-v35"
        or sem_check.get("generation") != "v68r35"
        or sem_check.get("status") != "PASS"
        or sem_check.get("errors") != []
        or sem_check.get("semantic_root") != "sem/r15"
        or sem_check.get("input_manifest") != {
            "name": "qa/v68r35/sem-input.json",
            "bytes": EXPECTED_SEM_QA["sem-input.json"][0],
            "sha256": EXPECTED_SEM_QA["sem-input.json"][1],
        }
    ):
        raise RuntimeError("Semantic check chain drift")
    if sem_check.get("manifest") != {
        "name": "sem/r15/manifest.json",
        "bytes": 10320,
        "sha256": "8C35707629E40C70049B17A02ECD71891264D057A8E32712B3565FFDFEFE3540",
    } or sem_check.get("validation") != {
        "name": "sem/r15/validation.json",
        "bytes": 4129,
        "sha256": "0C15FDE42EF5C32401F2F045450024DACC669920274D996D85F74E110ADC75CF",
    }:
        raise RuntimeError("Semantic manifest/validation receipt drift")
    validation = strict_json(SEM / "validation.json")
    if validation.get("status") != "PASS" or validation.get("errors") != []:
        raise RuntimeError("Semantic validation is not PASS")

    source = strict_json(P142_SOURCE)
    if (
        source.get("status") != "PASS"
        or source.get("errors") != []
        or source.get("exact_source_delta") != {
            "scope": (
                "proof-stage footnote 2 bis categorical-term correction plus a future "
                "semantic split contract"
            ),
            "corrected_french_substitutions": 1,
            "corrected_french_from": "sous-truc",
            "corrected_french_to": "sous-objet",
            "diplomatic_french_changes": 0,
            "english_changes": 0,
            "other_source_changes": 0,
            "ordered_layer_targets_unchanged": True,
            "semantic_graph_files_touched": 0,
            "mapping_files_touched": 0,
        }
        or source.get("semantic_split_contract", {}).get("decision") != "TOH-P142-SEM-002"
        or source.get("semantic_split_contract", {}).get("current_combined_node")
        != "tohoku:thm:2.2.2:p2"
        or source.get("semantic_split_contract", {}).get("future_footnote_node")
        != "tohoku:footnote:2bis"
    ):
        raise RuntimeError("p. 142 source-admission chain drift")
    reader = strict_json(READER_QA)
    if (
        reader.get("status") != "PASS"
        or reader.get("errors") != []
        or reader.get("conclusion", {}).get("reader_successor_accepted") is not True
        or reader.get("conclusion", {}).get("semantic_graph_successor_may_bind_this_receipt")
        is not True
        or reader.get("conclusion", {}).get("blockers") != []
        or reader.get("identities", {}).get("source_admission") != {
            "path": "production/p142_fix1/check.json",
            "bytes": 7250,
            "sha256": "61DC1736262199D5909580C85756ADFA90C59C7D3BF12ADE4848995DA13A2A25",
        }
    ):
        raise RuntimeError("p. 142 reader-audit chain drift")
    build = strict_json(READER_BUILD)
    if build.get("status") != "PASS" or build.get("errors") != []:
        raise RuntimeError("Reader build receipt is not PASS")

    _, nodes = load_csv(SEM / "nodes.csv")
    node_by_id = {row["node_id"]: row for row in nodes}
    if len(node_by_id) != 991:
        raise RuntimeError("sem/r15 node identity surface drift")
    theorem = node_by_id.get("tohoku:thm:2.2.2:p2", {})
    footnote = node_by_id.get("tohoku:footnote:2bis", {})
    if (
        theorem.get("node_type") != "theorem"
        or theorem.get("parent_id") != "tohoku:section:2.2"
        or theorem.get("en_label") != EXPECTED_P142_THEOREM_TITLE
        or theorem.get("provenance") != EXPECTED_P142_PROVENANCE
        or footnote != {
            "node_id": "tohoku:footnote:2bis",
            "node_class": "source_target",
            "node_type": "footnote",
            "parent_id": "tohoku:section:2.2",
            "preferred_id": "tohoku:footnote:2bis",
            "first_page": "142",
            "last_page": "142",
            "pages": "142",
            "occurrences": "1",
            "body_page": "142",
            "printed_ref_labels": "",
            "state": "active_complete",
            "fr_label": (
                "(Note ajoutée pendant la correction des épreuves.) Cette condition est aussi "
                "automatiquement vérifiée si tout objet de C est isomorphe à un sous-objet "
                "d'un objet injectif, cf. [6, Chap. III]."
            ),
            "en_label": EXPECTED_P142_FOOTNOTE_TITLE,
            "provenance": EXPECTED_P142_PROVENANCE,
        }
    ):
        raise RuntimeError("p. 142 semantic split-node drift")

    _, occurrences = load_csv(SEM / "occ.csv")
    occurrence_by_id = {row["occurrence_id"]: row for row in occurrences}
    theorem_occ = occurrence_by_id.get("tohoku:occ:p142:o001", {})
    footnote_occ = occurrence_by_id.get("tohoku:occ:p142:o005", {})
    expected_shared = {
        "decision_path": "production/p142_fix1/decisions.jsonl",
        "parity_state": "PASS",
        "printed_page": "142",
    }
    if (
        any(theorem_occ.get(key) != value for key, value in expected_shared.items())
        or theorem_occ.get("semantic_id") != "tohoku:thm:2.2.2:p2"
        or theorem_occ.get("order") != "1"
        or theorem_occ.get("dip_sha256")
        != "554602A57C9FBA0FB389AA11D2C3C75A2565D4DE7F96AF5FC1C8D113BE0CC705"
        or theorem_occ.get("fr_sha256")
        != "554602A57C9FBA0FB389AA11D2C3C75A2565D4DE7F96AF5FC1C8D113BE0CC705"
        or theorem_occ.get("en_sha256")
        != "DCAC525FF9B9E18D6FACBD67AAD942CF50B7A3D2D86E8A1DB5873E0DCFA113FC"
        or any(footnote_occ.get(key) != value for key, value in expected_shared.items())
        or footnote_occ.get("semantic_id") != "tohoku:footnote:2bis"
        or footnote_occ.get("kind") != "footnote"
        or footnote_occ.get("order") != "2"
        or footnote_occ.get("dip_sha256")
        != "EA8B36BA929EFCA6C8F9ED07DD44DD423DAFF759FD61FAECEEAACC523420458A"
        or footnote_occ.get("fr_sha256")
        != "5B11411F10E0890642AE975252504B71EAC28B3F340BD5DC7D1693E58897CC60"
        or footnote_occ.get("en_sha256")
        != "189974B1A267AE730AE7DEF32084812D2717FD7FB596508E9F4B354617FDF1CA"
    ):
        raise RuntimeError("p. 142 semantic occurrence drift")

def verify_inputs(fresh: bool) -> tuple[dict[str, object], bytes]:
    require_plain_directory(SOURCE)
    source_names = {path.name for path in SOURCE.iterdir() if path.is_file()}
    if source_names != set(EXPECTED_SOURCE) or any(path.is_dir() for path in SOURCE.iterdir()):
        raise RuntimeError("Predecessor dossier surface drift")
    for name, expected in EXPECTED_SOURCE.items():
        require_identity(SOURCE / name, expected)
    source_records_now = [record(SOURCE / name) for name in sorted(EXPECTED_SOURCE)]
    if (
        len(source_records_now),
        sum(int(item["bytes"]) for item in source_records_now),
        aggregate(source_records_now),
    ) != EXPECTED_SOURCE_SURFACE:
        raise RuntimeError("Predecessor dossier aggregate drift")
    predecessor = strict_json(SOURCE / "r40-check.json")
    if predecessor.get("status") != "PASS" or predecessor.get("errors") != []:
        raise RuntimeError("Predecessor receipt is not PASS")

    for name, expected in EXPECTED_SEM_QA.items():
        require_identity(SEM_QA / name, expected)
    for path, size, sha256 in EXPECTED_REPAIR_RECEIPTS.values():
        require_identity(path, (size, sha256))
    for name, expected in EXPECTED_AUTHORITY.items():
        require_identity(AUTHORITY / name, expected)

    semantic = sem_records()
    if {path.name for path in SEM.iterdir() if path.is_file()} != {
        str(item["name"]) for item in semantic
    } or any(path.is_dir() for path in SEM.iterdir()):
        raise RuntimeError("Semantic directory surface drift")
    current_semantic: list[dict[str, object]] = []
    for item in semantic:
        path = SEM / str(item["name"])
        require_identity(path, (int(item["bytes"]), str(item["sha256"])))
        current_semantic.append(record(path))
    if aggregate(current_semantic) != SEMANTIC_SURFACE[2]:
        raise RuntimeError("Semantic aggregate drift")
    verify_semantic_and_repair_chain()

    if fresh:
        for name, expected in EXPECTED_TOOLS.items():
            require_identity(ROOT / name, expected)
        for name, expected in EXPECTED_ARTIFACTS.items():
            require_identity(ROOT / name, expected)
        tex_hashes = expected_tex_hashes()
        live_names = {path.name for path in ROOT.glob("*.tex")}
        if live_names != set(tex_hashes):
            raise RuntimeError("Live TeX filename surface differs from the frozen 119-file manifest")
        for name, sha256 in tex_hashes.items():
            require_plain_file(ROOT / name)
            if identity(ROOT / name)[1] != sha256:
                raise RuntimeError(f"Live TeX identity drift: {name}")
        if sys.version_info[:3] != (3, 13, 9) or sys.implementation.cache_tag != "cpython-313":
            raise RuntimeError("Python runtime drift")
    return dict(EXPECTED_GIT_NONCLAIM), b""


def make_config() -> dict:
    cfg = strict_json(SOURCE / "cfg.json")
    cfg["dossier_id"] = "tohoku_r41"
    cfg["expected_units"] = 991
    cfg["inputs"]["primary"] = {
        **record(SEM / "nodes.csv", "nodes.csv"),
        "filename": "nodes.csv",
        "source_file": "sem/r15/nodes.csv",
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
        **record(SEM / "manifest.json", "sem/r15 manifest"),
        "filename": "manifest.json",
    }
    cfg["inputs"]["sem_validation"] = {
        **record(SEM / "validation.json", "sem/r15 validation"),
        "filename": "validation.json",
    }
    cfg["inputs"]["sem_input"] = {
        **record(SEM_QA / "sem-input.json", "v68r35 sem input"),
        "filename": "sem-input.json",
    }
    cfg["inputs"]["sem_check"] = {
        **record(SEM_QA / "sem-check.json", "v68r35 sem check"),
        "filename": "sem-check.json",
    }
    cfg["semantic_successor"] = {
        "generation": "sem/r15",
        "surface_files": SEMANTIC_SURFACE[0],
        "surface_bytes": SEMANTIC_SURFACE[1],
        "surface_sha256": SEMANTIC_SURFACE[2],
        "receipt": record(SEM_QA / "sem-check.json", "qa/v68r35/sem-check.json"),
    }
    return cfg

def make_decisions() -> bytes:
    fields, rows = load_csv(SOURCE / "dec.csv")
    if [row["decision_id"] for row in rows] != [
        f"D{number:06d}" for number in range(1, 996)
    ] or rows[-1]["decision_id"] != "D000995":
        raise RuntimeError("Predecessor decision sequence drift")
    if fields != [
        "decision_id", "unit_id", "action", "disposition", "stacks_labels",
        "rationale", "review_state", "supersedes",
    ]:
        raise RuntimeError("Predecessor decision schema drift")
    return (SOURCE / "dec.csv").read_bytes()


def make_issues() -> bytes:
    fields, rows = load_csv(SOURCE / "issues.csv")
    if [row["issue_id"] for row in rows] != [
        f"I{number:06d}" for number in range(1, 29)
    ] or any(row["status"] != "resolved" for row in rows):
        raise RuntimeError("Predecessor source-issue sequence drift")
    if fields != [
        "issue_id", "unit_id", "status", "kind", "claim", "evidence_labels",
        "evidence", "control", "resolution_decision",
    ]:
        raise RuntimeError("Predecessor source-issue schema drift")
    appended = csv_bytes(fields, ISSUE_ROWS)
    return (SOURCE / "issues.csv").read_bytes() + appended[appended.index(b"\n") + 1 :]

def run_tool(name: str, *args: str) -> None:
    relative = f"srcmap/{name}"
    require_identity(ROOT / relative, EXPECTED_TOOLS[relative])
    subprocess.run(
        [sys.executable, "-I", "-B", str(ROOT / relative), *args],
        cwd=ROOT,
        check=True,
    )
    require_identity(ROOT / relative, EXPECTED_TOOLS[relative])


def intake_args() -> list[str]:
    specs = [
        ("part_i", AUTHORITY / "jstage_part_I_9_2_119.pdf"),
        ("part_ii", AUTHORITY / "jstage_part_II_9_3_185.pdf"),
        ("edges", SEM / "edges.csv"),
        ("terms", SEM / "terms.csv"),
        ("stacks", SEM / "stacks.csv"),
        ("sem_manifest", SEM / "manifest.json"),
        ("sem_validation", SEM / "validation.json"),
        ("sem_input", SEM_QA / "sem-input.json"),
        ("sem_check", SEM_QA / "sem-check.json"),
    ]
    output: list[str] = []
    for key, path in specs:
        output += ["--extra", f"{key}={path}"]
    return output


def expected_build_receipt() -> dict[str, object]:
    builds: dict[str, object] = {}
    for chapter, spec in BUILD_SPECS.items():
        build: dict[str, object] = {
            "tex": constant_record(f"{chapter}.tex", EXPECTED_ARTIFACTS[f"{chapter}.tex"]),
            "log": constant_record(f"{chapter}.log", EXPECTED_ARTIFACTS[f"{chapter}.log"]),
            "pdf": constant_record(f"{chapter}.pdf", EXPECTED_ARTIFACTS[f"{chapter}.pdf"]),
            "pdf_pages": spec["pdf_pages"],
            "undefined_references": 0,
            "undefined_citations": 0,
            "rerun_notices": 0,
            "new_block_overfull_boxes": 0,
            "visual_reviewed_pages": spec["visual_reviewed_pages"],
        }
        if chapter == "homology":
            build["aux"] = constant_record("homology.aux", EXPECTED_ARTIFACTS["homology.aux"])
        builds[chapter] = build
    return builds


def verify_builds() -> dict[str, object]:
    forbidden = [
        r"(?m)^!", r"(?m)^LaTeX Warning:", r"(?m)^Package .* Warning:",
        r"undefined references", r"undefined citations",
        r"Rerun to get cross-references right", r"Label\(s\) may have changed",
    ]
    for name, expected in EXPECTED_ARTIFACTS.items():
        require_identity(ROOT / name, expected)
    for chapter, spec in BUILD_SPECS.items():
        text = (ROOT / f"{chapter}.log").read_text(encoding="utf-8", errors="replace")
        hits = [pattern for pattern in forbidden if re.search(pattern, text)]
        if hits:
            raise RuntimeError(f"{chapter} build diagnostics failed: {hits}")
        output = re.findall(
            rf"Output written on {re.escape(chapter)}\.pdf \(([0-9]+) pages?, ([0-9]+) bytes\)\.",
            text,
        )
        if output != [(str(spec["pdf_pages"]), str(EXPECTED_ARTIFACTS[f"{chapter}.pdf"][0]))]:
            raise RuntimeError(f"{chapter} output-page receipt drift: {output}")
    aux_lines = set((ROOT / "homology.aux").read_text(encoding="utf-8").splitlines())
    if any(line not in aux_lines for line in EXPECTED_AUX_LABEL_LINES):
        raise RuntimeError("Pinned Homology AUX label/page evidence drift")
    return expected_build_receipt()


def expected_intake_receipt(root: Path) -> dict[str, object]:
    return {
        "schema": "historical-source-intake-v1",
        "corpus": "Tohoku",
        "adapter": "tohoku_nodes",
        "status": "PASS",
        "errors": [],
        "inputs": [
            record(SEM / "nodes.csv"),
            record(AUTHORITY / "jstage_part_I_9_2_119.pdf"),
            record(AUTHORITY / "jstage_part_II_9_3_185.pdf"),
            record(SEM / "edges.csv"),
            record(SEM / "terms.csv"),
            record(SEM / "stacks.csv"),
            record(SEM / "manifest.json"),
            record(SEM / "validation.json"),
            record(SEM_QA / "sem-input.json"),
            record(SEM_QA / "sem-check.json"),
        ],
        "counts": {"units": 991, "units_with_topics": 492},
        "outputs": {
            "units.csv": {
                "bytes": identity(root / "units.csv")[0],
                "sha256": identity(root / "units.csv")[1],
            }
        },
    }

def expected_scan_warnings() -> list[str]:
    old = strict_json(SOURCE / "check.json")["warnings"]
    if len(old) < 9 or any(
        not value.startswith("generated book label is outside chapter TeX:")
        for value in old[:9]
    ):
        raise RuntimeError("Predecessor warning prefix drift")
    additions = [
        f"TeX label has no official tag in this snapshot: {label}"
        for label in NEW_LOCAL_LABELS
    ]
    return [*old[:9], *sorted([*old[9:], *additions])]


def verify_deltas(root: Path) -> dict[str, object]:
    intake = strict_json(root / "intake.json")
    check = strict_json(root / "check.json")
    mcheck = strict_json(root / "mcheck.json")
    for name, receipt in (("intake", intake), ("scan", check), ("map", mcheck)):
        if receipt.get("status") != "PASS" or receipt.get("errors") != []:
            raise RuntimeError(f"{name} receipt is not PASS")
    if mcheck.get("outputs_promoted") is not True:
        raise RuntimeError("Mapping outputs were not promoted")

    actual_outputs = {name: identity(root / name) for name in sorted(PAYLOAD)}
    if actual_outputs != EXPECTED_OUTPUTS:
        raise RuntimeError(f"Canonical output identity drift: {actual_outputs}")
    output_surface = [record(root / name) for name in sorted(PAYLOAD)]
    if (
        len(output_surface),
        sum(int(item["bytes"]) for item in output_surface),
        aggregate(output_surface),
    ) != EXPECTED_OUTPUT_SURFACE:
        raise RuntimeError("Canonical output aggregate drift")
    if strict_json(root / "cfg.json") != make_config():
        raise RuntimeError("Configuration does not exactly preserve sem/r15")
    if intake != expected_intake_receipt(root):
        raise RuntimeError("Intake receipt differs from sealed r40")

    unchanged = (
        "topics.csv", "dec.csv", "intake.json", "units.csv", "stx.csv",
        "tcand.csv", "tmap.csv", "map.csv", "ucand.csv",
    )
    for name in unchanged:
        if (root / name).read_bytes() != (SOURCE / name).read_bytes():
            raise RuntimeError(f"Unexpected byte drift: {name}")
    if (root / "STATUS.md").read_bytes() != STATUS_BYTES:
        raise RuntimeError("Status bytes drift")

    _, sem_nodes = load_csv(SEM / "nodes.csv")
    _, units = load_csv(root / "units.csv")
    if len(units) != 991 or [row["id"] for row in units] != [
        row["node_id"] for row in sem_nodes
    ]:
        raise RuntimeError("Stable semantic unit surface drift")

    _, decisions = load_csv(root / "dec.csv")
    if [row["decision_id"] for row in decisions] != [
        f"D{number:06d}" for number in range(1, 996)
    ] or (root / "dec.csv").read_bytes() != make_decisions():
        raise RuntimeError("Decision ledger is not the exact sealed r40 ledger")
    decision_by_id = {row["decision_id"]: row for row in decisions}
    d214 = decision_by_id.get("D000214", {})
    if (
        d214.get("unit_id") != "tohoku:thm:2.2.2:dual"
        or d214.get("disposition") != "new_statement"
    ):
        raise RuntimeError("D000214 predecessor row drift")

    old_issues = (SOURCE / "issues.csv").read_bytes()
    new_issues = (root / "issues.csv").read_bytes()
    if not new_issues.startswith(old_issues) or new_issues != make_issues():
        raise RuntimeError("Source-issue ledger is not the exact append-only successor")
    _, issues = load_csv(root / "issues.csv")
    if [row["issue_id"] for row in issues] != [
        f"I{number:06d}" for number in range(1, 30)
    ] or issues[-1:] != ISSUE_ROWS:
        raise RuntimeError("I000029 issue sequence/row drift")
    active_issues = [row["issue_id"] for row in issues if row["status"] != "resolved"]
    if active_issues != ["I000029"]:
        raise RuntimeError(f"Unexpected active source issues: {active_issues}")
    if issues[-1]["status"] != "open" or issues[-1]["resolution_decision"] != "":
        raise RuntimeError("I000029 unresolved status contract drift")

    if check.get("counts") != EXPECTED_SCAN_COUNTS:
        raise RuntimeError(f"Scan counts drift: {check.get('counts')}")
    if check.get("warnings") != expected_scan_warnings():
        raise RuntimeError("Scan warning surface drift")
    if check.get("tex_sha256") != expected_tex_hashes():
        raise RuntimeError("TeX hash dictionary drift")
    if check.get("sha256", {}).get("tags/tags") != EXPECTED_TOOLS["tags/tags"][1]:
        raise RuntimeError("Tags hash drift in scan receipt")
    old_check = strict_json(SOURCE / "check.json")
    expected_check = json.loads(json.dumps(old_check))
    expected_check["sha256"] = {
        key.replace("tohoku_r40/", "tohoku_r41/"): value
        for key, value in old_check["sha256"].items()
    }
    for name in ("topics.csv", "stx.csv", "tcand.csv", "tmap.csv"):
        expected_check["sha256"][f"tohoku_r41/{name}"] = identity(root / name)[1]
    if check != expected_check:
        raise RuntimeError("Scan receipt is not the exact bounded path-only successor")

    _, old_map = load_csv(SOURCE / "map.csv")
    _, new_map = load_csv(root / "map.csv")
    old_map_by_id = {row["unit_id"]: row for row in old_map}
    new_map_by_id = {row["unit_id"]: row for row in new_map}
    if old_map_by_id.get("tohoku:thm:2.2.2:dual") != new_map_by_id.get(
        "tohoku:thm:2.2.2:dual"
    ) or new_map_by_id.get("tohoku:thm:2.2.2:dual", {}).get("decision_id") != "D000214":
        raise RuntimeError("D000214 substantive map row changed")

    if mcheck.get("counts") != EXPECTED_MAPPING_COUNTS:
        raise RuntimeError(f"Mapping counts drift: {mcheck.get('counts')}")
    if mcheck.get("warnings") != check.get("warnings"):
        raise RuntimeError("Mapping warning surface differs from scan warnings")
    old_mcheck = strict_json(SOURCE / "mcheck.json")
    expected_mcheck = json.loads(json.dumps(old_mcheck))
    expected_mcheck["counts"] = EXPECTED_MAPPING_COUNTS
    expected_mcheck["sha256"] = {
        key.replace("tohoku_r40/", "tohoku_r41/"): value
        for key, value in old_mcheck["sha256"].items()
    }
    for name in (
        "cfg.json", "dec.csv", "intake.json", "issues.csv", "map.csv",
        "ucand.csv", "units.csv",
    ):
        expected_mcheck["sha256"][f"tohoku_r41/{name}"] = identity(root / name)[1]
    if mcheck != expected_mcheck:
        raise RuntimeError("Mapping receipt is not the exact issue-only successor")
    _, undecided = load_csv(root / "ucand.csv")
    if undecided:
        raise RuntimeError("Unexpected undecided unit candidates")
    gap_count = sum(
        EXPECTED_MAPPING_COUNTS["dispositions"][name]
        for name in ("existing_weaker", "extend_existing", "new_statement", "new_section")
    )
    if gap_count != 64:
        raise RuntimeError(f"Gap-class arithmetic drift: {gap_count}")

    return {
        "decisions_appended": [],
        "source_issues_appended": ISSUE_ROWS,
        "resolved_source_issues_appended": [],
        "active_source_issues": active_issues,
        "semantic_generation": "sem/r15",
        "semantic_files_changed": 0,
        "stable_units": 991,
        "scan_counts": check["counts"],
        "mapping_counts": mcheck["counts"],
        "substantive_map_changes": [],
        "d000214_unchanged": {
            "unit_id": "tohoku:thm:2.2.2:dual",
            "decision_id": "D000214",
            "byte_identical_map_ledger": True,
        },
        "byte_identical_payloads": list(unchanged),
        "stacks_index_changes": 0,
        "topic_candidate_changes": 0,
        "remaining_gap_class_dispositions": gap_count,
    }


def output_records(root: Path) -> list[dict[str, object]]:
    return [record(root / name) for name in sorted(PAYLOAD)]


def source_records() -> list[dict[str, object]]:
    return [record(SOURCE / name) for name in sorted(EXPECTED_SOURCE)]


def repair_receipt_records() -> list[dict[str, object]]:
    return [
        record(path, name)
        for name, (path, _, _) in sorted(EXPECTED_REPAIR_RECEIPTS.items())
    ]


def execution_receipt(attestation: dict[str, object]) -> dict[str, object]:
    return {
        "attestation": attestation,
        "bootstrap": record(ROOT / "srcmap" / "start_build_tohoku_r41.py"),
        "powershell_envelope": record(ROOT / "srcmap" / "start_build_tohoku_r41.ps1"),
        "dependencies": {
            name: constant_record(name, expected)
            for name, expected in sorted(EXPECTED_TOOLS.items())
        },
        "contract": (
            "same_bytes_bootstrap; exact_inputs_locked_against_write_delete_through_"
            "generation_replay_and_promotion"
        ),
    }


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
    repairs = repair_receipt_records()
    return {
        "schema": "tohoku-stacks-mapping-successor-r41-v1",
        "status": "PASS",
        "errors": [],
        "predecessor_dossier": {
            "name": "tohoku_r40",
            "files": sources,
            "file_count": len(sources),
            "bytes": sum(int(item["bytes"]) for item in sources),
            "aggregate_sha256": aggregate(sources),
        },
        "semantic_source": {
            "generation": "sem/r15",
            "files": semantic,
            "file_count": len(semantic),
            "bytes": sum(int(item["bytes"]) for item in semantic),
            "aggregate_sha256": aggregate(semantic),
            "sem_input": record(SEM_QA / "sem-input.json", "qa/v68r35/sem-input.json"),
            "sem_check": record(SEM_QA / "sem-check.json", "qa/v68r35/sem-check.json"),
        },
        "p142_footnote_repair": {
            "receipts": repairs,
            "file_count": len(repairs),
            "bytes": sum(int(item["bytes"]) for item in repairs),
            "aggregate_sha256": aggregate(repairs),
            "issue_id": "I000028",
            "resolution_decision": "D000995",
        },
        "open_issue": {
            "row": ISSUE_ROWS[0],
            "status_token": "open",
            "resolution_decision": "",
            "authority": constant_record(
                "jstage_part_I_9_2_119.pdf",
                EXPECTED_AUTHORITY["jstage_part_I_9_2_119.pdf"],
            ),
        },
        "execution": execution if execution is not None else execution_receipt(attestation),
        "git": git,
        "builds": verify_builds() if builds is None else builds,
        "deltas": deltas,
        "files": output_records(root),
        "nonclaims": [
            "No Git command is executed by this mapping successor.",
            "No Git commit or push is made by this receipt.",
            "No remote-server freshness check is performed.",
            "The Stacks scanner is confined to the exact 119 top-level TeX filenames inherited from the sealed r40 manifest; it performs no recursive workspace scan.",
            "Existing-target replay treats the live Stacks TeX and build artifacts as creation-time evidence bound by the receipt; it does not assert that those external files remain byte-identical later.",
            "The outer-envelope sentinel prevents accidental direct-bootstrap use but is not cryptographic provenance against a same-user forged invocation.",
            "The Stacks scan binds the exact live integrated worktree, not the frozen HEAD tree.",
            "The transaction denies write/delete access to every existing consumed file; hostile same-user mutation of directory namespaces is outside this lock contract.",
            "No decision is appended; dec.csv and map.csv remain byte-identical to sealed r40.",
            "D000214 and all substantive fields of the tohoku:thm:2.2.2:dual map row remain unchanged.",
            "I000029 is appended with schema-valid status open and a blank resolution_decision.",
            "No release, publication, upload, DOI, Zenodo, rights, or whole-paper gate is closed.",
            "64 Tohoku gap-class dispositions remain.",
            "There are 29 recorded source issues: 28 resolved and exactly I000029 open.",
        ],
    }

def verify_existing(
    git: dict[str, object], attestation: dict[str, object]
) -> dict[str, object]:
    require_plain_directory(TARGET)
    names = {path.name for path in TARGET.iterdir() if path.is_file()}
    if names != PAYLOAD | {"r41-check.json"} or any(path.is_dir() for path in TARGET.iterdir()):
        raise RuntimeError("Existing r41 dossier surface drift")
    deltas = verify_deltas(TARGET)
    receipt = strict_json(TARGET / "r41-check.json")
    if receipt.get("git") != EXPECTED_GIT_NONCLAIM:
        raise RuntimeError("Existing receipt Git nonclaim drift")
    builds = receipt.get("builds")
    if builds != expected_build_receipt():
        raise RuntimeError("Existing builds receipt drift")
    execution = receipt.get("execution")
    if execution != execution_receipt(attestation):
        raise RuntimeError("Existing execution receipt drift")
    expected = receipt_payload(
        TARGET, receipt["git"], attestation, deltas, builds, execution
    )
    if receipt != expected:
        raise RuntimeError("Existing r41 receipt replay mismatch")
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
        exclusive_write(STAGE / "r41-check.json", json_bytes(receipt))
        if (
            {path.name for path in STAGE.iterdir() if path.is_file()}
            != PAYLOAD | {"r41-check.json"}
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
