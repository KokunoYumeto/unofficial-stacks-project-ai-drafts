#!/usr/bin/env python3
"""Independent structural, rendered-page, and replay QA for reader v068c3r21."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from pypdf import PdfReader


ROOT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
FTG = Path(r"user\Documents\stacks-ftg")
SCRIPT = Path(__file__).resolve(strict=True)
QA_ROOT = ROOT / "qa" / "v68r43"
RENDERS = QA_ROOT / "renders"
STRUCTURAL = QA_ROOT / "structural.json"
CHECK = QA_ROOT / "check.json"
ATTESTATION = FTG / "tmp" / "d1029_source_repair_toolchain" / "r43_visual_attestation.json"
BUILD_RECEIPT = ROOT / "build" / "v068c3r21" / "build.json"
BUILD_RECEIPT_EXPECTED = (21071, "EEB4DAE83F5D940681190C24BACC50A9799850A87399D1D36B9E663525B1D6FB")
SOURCE_CHECK = ROOT / "production" / "p188_fix1" / "check.json"
SOURCE_CHECK_EXPECTED = (4625, "52D174E72E44BE1DC5E6EE25A405B8C971EA4434F10BA7753F10CA1491851CF6")
PDFS = {
    "en": {
        "old": (ROOT / "output" / "pdf" / "en-p119-221-v068c3r20.pdf", 1381128, "3E78467B441F801DE742584CA9FBE906A886B4B9DD6AA4585315DB9482175AA1", 90),
        "new": (ROOT / "output" / "pdf" / "en-p119-221-v068c3r21.pdf", 1381119, "C45350A80D39954A203993B3E6B2FB58532425915BFEC517E99DB01BF08AB39F", 90),
        "target_page": 56,
        "needle": "complete this chain",
    },
    "fr": {
        "old": (ROOT / "output" / "pdf" / "fr-p119-221-v068c3r20.pdf", 1417551, "91EE76111A240E36AC107FCAC9605A5E32E9E9796AAE86AAB495D5F36DB3AFB8", 94),
        "new": (ROOT / "output" / "pdf" / "fr-p119-221-v068c3r21.pdf", 1417508, "AADC500F836F5E9397160C4E3BEAB1AD354E35742937D495360D41D2E4A7E865", 94),
        "target_page": 58,
        "needle": "finir les sorites",
    },
}
PDFTOPPM = Path(r"user\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdftoppm.exe")
PDFTOPPM_EXPECTED = (115200, "23335D0EC465C53C2919FBEC02574D4C14936FCE2F22D8673BFD3E4E48C66091")
CREATED_UTC = "2026-08-24T08:30:00Z"


class QAError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def ident(path: Path, data: bytes) -> dict[str, Any]:
    try:
        shown = path.relative_to(ROOT).as_posix()
    except ValueError:
        shown = str(path)
    return {"path": shown, "bytes": len(data), "sha256": sha(data)}


def exact(path: Path, expected: tuple[int, str], label: str) -> bytes:
    if not path.is_file() or path.is_symlink() or path.resolve(strict=True) != path:
        raise QAError(f"{label}: invalid path")
    data = path.read_bytes()
    if (len(data), sha(data)) != expected:
        raise QAError(f"{label}: identity drifted: {(len(data), sha(data))}")
    return data


def pretty(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def page_stream(page: Any) -> bytes:
    contents = page.get_contents()
    return b"" if contents is None else contents.get_data()


def media_box(page: Any) -> list[str]:
    box = page.mediabox
    return [str(box.left), str(box.bottom), str(box.right), str(box.top)]


def open_pdf(path: Path, expected: tuple[int, str, int], label: str) -> tuple[bytes, PdfReader]:
    data = exact(path, expected[:2], label)
    reader = PdfReader(str(path), strict=True)
    if reader.is_encrypted or len(reader.pages) != expected[2]:
        raise QAError(f"{label}: encryption or page-count drift")
    for page in reader.pages:
        _ = page_stream(page)
    return data, reader


def render_page(pdf: Path, language: str, page_number: int) -> Path:
    prefix = RENDERS / f"{language}-p{page_number:03d}"
    output = prefix.with_suffix(".png")
    command = [str(PDFTOPPM), "-f", str(page_number), "-l", str(page_number), "-singlefile", "-png", "-r", "160", str(pdf), str(prefix)]
    result = subprocess.run(command, check=False, shell=False, capture_output=True)
    if result.returncode != 0 or result.stdout or not output.is_file():
        raise QAError(f"render failed for {language} page {page_number}: rc={result.returncode}, stderr={result.stderr!r}")
    return output


def derive(render: bool) -> dict[str, Any]:
    script_data = SCRIPT.read_bytes()
    build_data = exact(BUILD_RECEIPT, BUILD_RECEIPT_EXPECTED, "r21 build receipt")
    build = json.loads(build_data.decode("utf-8"))
    if build.get("status") != "PASS" or build.get("errors") != [] or build.get("revision") != "v068c3r21":
        raise QAError("r21 build receipt semantics drifted")
    source_data = exact(SOURCE_CHECK, SOURCE_CHECK_EXPECTED, "p188_fix1 receipt")
    renderer_data = exact(PDFTOPPM, PDFTOPPM_EXPECTED, "pdftoppm renderer")
    results: dict[str, Any] = {}
    render_records: list[dict[str, Any]] = []
    for language, spec in PDFS.items():
        old_path, old_size, old_sha, old_pages = spec["old"]
        new_path, new_size, new_sha, new_pages = spec["new"]
        old_data, old = open_pdf(old_path, (old_size, old_sha, old_pages), f"r20 {language} PDF")
        new_data, new = open_pdf(new_path, (new_size, new_sha, new_pages), f"r21 {language} PDF")
        if [media_box(page) for page in old.pages] != [media_box(page) for page in new.pages]:
            raise QAError(f"{language}: ordered page geometry changed")
        old_streams = [page_stream(page) for page in old.pages]
        new_streams = [page_stream(page) for page in new.pages]
        changed = [index + 1 for index, (before, after) in enumerate(zip(old_streams, new_streams)) if before != after]
        target = int(spec["target_page"])
        if changed != [target]:
            raise QAError(f"{language}: changed content pages are {changed}, expected {[target]}")
        hits = [index + 1 for index, page in enumerate(new.pages) if spec["needle"] in (page.extract_text() or "")]
        if hits != [target]:
            raise QAError(f"{language}: target text hits are {hits}, expected {[target]}")
        normalized = " ".join((new.pages[target - 1].extract_text() or "").split())
        if "Γ(O" not in normalized:
            raise QAError(f"{language}: corrected Gamma(O^natural) text is not extractable")
        forbidden = "center of Γ(O)" if language == "en" else "centre de Γ(O)"
        if forbidden in normalized:
            raise QAError(f"{language}: false scalar-ring phrase remains extractable")
        results[language] = {
            "predecessor_pdf": {**ident(old_path, old_data), "pages": old_pages},
            "successor_pdf": {**ident(new_path, new_data), "pages": new_pages},
            "changed_content_pages": changed,
            "unique_target_text_page": target,
            "adjacent_content_streams_byte_identical": True,
            "target_stream_predecessor": {"bytes": len(old_streams[target - 1]), "sha256": sha(old_streams[target - 1])},
            "target_stream_successor": {"bytes": len(new_streams[target - 1]), "sha256": sha(new_streams[target - 1])},
            "target_text_sha256": sha(normalized.encode("utf-8")),
        }
        if render:
            for page_number in (target - 1, target, target + 1):
                path = render_page(new_path, language, page_number)
                data = path.read_bytes()
                render_records.append({**ident(path, data), "language": language, "physical_pdf_page": page_number, "role": "target" if page_number == target else "adjacent"})
    return {
        "schema": "tohoku-v068-reader-independent-qa-prepare-v43",
        "qa_revision": "v68r43",
        "reader_revision": "v068c3r21",
        "created_utc": CREATED_UTC,
        "status": "STRUCTURAL_PASS_VISUAL_PENDING" if render else "STRUCTURAL_REPLAY_PASS",
        "errors": [],
        "script": ident(SCRIPT, script_data),
        "build_receipt": ident(BUILD_RECEIPT, build_data),
        "source_admission_receipt": ident(SOURCE_CHECK, source_data),
        "renderer": {**ident(PDFTOPPM, renderer_data), "arguments": "pdftoppm -singlefile -png -r 160"},
        "languages": results,
        "renders": render_records,
        "conclusion": {
            "strict_pdf_parse": True,
            "page_inventory_complete": True,
            "only_target_content_pages_changed": True,
            "adjacent_page_content_streams_byte_identical": True,
            "corrected_scalar_ring_extractable": True,
            "false_scalar_ring_absent_from_corrected_reader": True,
            "visual_review_pending": render,
        },
    }


def write_new(path: Path, data: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(data); handle.flush(); os.fsync(handle.fileno())


def prepare() -> dict[str, Any]:
    if os.path.lexists(QA_ROOT):
        raise FileExistsError("v68r43 QA namespace exists")
    QA_ROOT.mkdir(exist_ok=False)
    RENDERS.mkdir(exist_ok=False)
    structural = derive(render=True)
    data = pretty(structural)
    write_new(STRUCTURAL, data)
    return {"status": "STRUCTURAL_PASS_VISUAL_PENDING", "structural": ident(STRUCTURAL, data), "renders": structural["renders"]}


def commit() -> dict[str, Any]:
    if not STRUCTURAL.is_file() or CHECK.exists():
        raise QAError("structural receipt missing or final check already exists")
    structural_data = STRUCTURAL.read_bytes()
    structural = json.loads(structural_data.decode("utf-8"))
    if structural.get("status") != "STRUCTURAL_PASS_VISUAL_PENDING" or structural.get("errors") != []:
        raise QAError("structural receipt is not ready")
    attestation_data = ATTESTATION.read_bytes()
    attestation = json.loads(attestation_data.decode("utf-8"))
    if attestation.get("schema") != "tohoku-v68r43-visual-attestation-v1" or attestation.get("status") != "PASS" or attestation.get("errors") != []:
        raise QAError("visual attestation did not pass")
    expected_images = {row["path"]: {"bytes": row["bytes"], "sha256": row["sha256"]} for row in structural["renders"]}
    if attestation.get("images") != expected_images or set(expected_images) != {row["path"] for row in structural["renders"]}:
        raise QAError("visual attestation image bindings differ")
    for row in structural["renders"]:
        exact(ROOT / Path(row["path"]), (row["bytes"], row["sha256"]), f"render {row['path']}")
    check = {
        "schema": "tohoku-v068-reader-independent-qa-v1",
        "qa_revision": "v68r43",
        "reader_revision": "v068c3r21",
        "created_utc": CREATED_UTC,
        "status": "PASS",
        "errors": [],
        "structural": ident(STRUCTURAL, structural_data),
        "visual_attestation": ident(ATTESTATION, attestation_data),
        "build_receipt": structural["build_receipt"],
        "source_admission_receipt": structural["source_admission_receipt"],
        "pdfs": {language: value["successor_pdf"] for language, value in structural["languages"].items()},
        "changed_physical_content_pages": {language: value["changed_content_pages"] for language, value in structural["languages"].items()},
        "conclusion": {
            "reader_successor_accepted": True,
            "pdf_pair_accepted": True,
            "source_transition_exact": True,
            "page_inventory_complete": True,
            "visual_review_accepted": True,
            "deterministic_receipt_replay_accepted": True,
            "semantic_replay_claimed": False,
            "blockers": [],
        },
    }
    data = pretty(check)
    write_new(CHECK, data)
    return {"status": "PASS", "qa_receipt": ident(CHECK, data)}


def replay() -> dict[str, Any]:
    structural_data = STRUCTURAL.read_bytes()
    structural = json.loads(structural_data.decode("utf-8"))
    recomputed = derive(render=False)
    for key in ("build_receipt", "source_admission_receipt", "renderer", "languages"):
        if structural.get(key) != recomputed.get(key):
            raise QAError(f"structural replay differs: {key}")
    for row in structural.get("renders", []):
        exact(ROOT / Path(row["path"]), (row["bytes"], row["sha256"]), f"render replay {row['path']}")
    check_data = CHECK.read_bytes()
    check = json.loads(check_data.decode("utf-8"))
    if check.get("status") != "PASS" or check.get("errors") != [] or check.get("qa_revision") != "v68r43":
        raise QAError("final QA receipt semantics drifted")
    attestation_record = check["visual_attestation"]
    exact(ATTESTATION, (attestation_record["bytes"], attestation_record["sha256"]), "visual attestation replay")
    return {"status": "PASS_COMMITTED_AND_REPLAYED", "structural": ident(STRUCTURAL, structural_data), "qa_receipt": ident(CHECK, check_data), "changed_physical_content_pages": check["changed_physical_content_pages"]}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--prepare", action="store_true")
    mode.add_argument("--commit", action="store_true")
    mode.add_argument("--replay", action="store_true")
    args = parser.parse_args(sys.argv[1:] if argv is None else list(argv))
    result = prepare() if args.prepare else commit() if args.commit else replay()
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise SystemExit(1)
