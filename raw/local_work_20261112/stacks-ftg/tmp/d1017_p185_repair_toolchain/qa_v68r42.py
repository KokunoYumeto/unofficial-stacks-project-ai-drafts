#!/usr/bin/env python3
"""Independent v68r42 QA scaffold for reader v068c3r20.

Future output identities are never guessed.  Preflight/prepare require a
separately frozen post-build binding file and its SHA-256 on the command
line.  Visual commit requires a separately frozen visual attestation and its
SHA-256.  No mode mutates reader/source/semantic inputs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import warnings
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

import pypdf
from pypdf import PdfReader
from pypdf.generic import IndirectObject


ROOT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SCRIPT = Path(__file__).resolve(strict=True)
CONTRACT_ID = "D1017-R001-p185-r20-r42-sem21-v1"
QA_ROOT = ROOT / "qa" / "v68r42"
QA_STAGE = ROOT / "qa" / ".v68r42.stage"
P185_RECEIPT = ROOT / "production" / "p185_fix2" / "check.json"
P185_RECEIPT_EXPECTED = (5_291, "E54AE998A9D8AB863652521E329731789727DD064B48E6A52CAB83584C802EEA")
SOURCE_LEDGER = ROOT / "SOURCE_CORRECTIONS.jsonl"
SOURCE_LEDGER_EXPECTED = (212_239, "31E8894E57B355383B49BB403FAE65B935C81B4C1DAC65C17B20C3C7A6E70439")
STAGED_SOURCE = ROOT / "build" / "v068c3r20" / "src"
STAGED_MANIFEST = (543, 11_855_949, 62_845, "52559D18F2A77C82A3BBAB69E4949C3A17C7DA1593034719F5B72584E9540310")
PREDECESSOR_PDFS = {
    "en": (ROOT / "output" / "pdf" / "en-p119-221-v068c3r19.pdf", 1_381_116, "A7B12B68566D4B2B5DA90DF64C8972D2A80A38EE7BB341E13DC77B75FFD51E96", 90),
    "fr": (ROOT / "output" / "pdf" / "fr-p119-221-v068c3r19.pdf", 1_417_542, "C2BB5BAC3D9641076A906379D4F7AC3C6A12C37C5877C63387B8C9443D6C74DA", 94),
}
PDFTOPPM = Path(r"user\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdftoppm.exe")
PDFTOPPM_EXPECTED = (115_200, "23335D0EC465C53C2919FBEC02574D4C14936FCE2F22D8673BFD3E4E48C66091")
EXPECTED_MEDIA_BOX = ("0", "0", "595.276", "841.89")
STRICT_LOG_PATTERN = re.compile(
    r"overfull|underfull|^latex(?: font)? warning:|^package .+ warning:|^class .+ warning:|"
    r"^pdftex warning|^(?:miktex-pdftex|pdflatex): warning:|^missing character:|undefined|"
    r"multiply defined|fatal error|emergency stop|latex error|no pages of output",
    re.IGNORECASE,
)
snapshot_record = globals().get("__verified_script_snapshot__")


class QAError(RuntimeError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def require_digest(value: str, label: str) -> str:
    if not re.fullmatch(r"[0-9A-F]{64}", value):
        raise QAError(f"{label}: expected uppercase SHA-256")
    return value


def exact(path: Path, expected: tuple[int, str], label: str) -> bytes:
    if not path.is_file() or path.is_symlink() or path.resolve(strict=True) != path:
        raise QAError(f"{label}: missing, non-regular, symlinked, or redirected")
    data = path.read_bytes()
    if (len(data), digest(data)) != expected:
        raise QAError(f"{label}: identity drifted: {(len(data), digest(data))}")
    return data


def parse_json(data: bytes, label: str) -> dict[str, Any]:
    value = json.loads(data.decode("utf-8", errors="strict"))
    if not isinstance(value, dict):
        raise QAError(f"{label}: JSON root is not an object")
    return value


def identity(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    try:
        relative = path.relative_to(ROOT).as_posix()
    except ValueError:
        relative = str(path)
    return {"path": relative, "bytes": len(data), "sha256": digest(data)}


def staged_identity(path: Path) -> dict[str, Any]:
    row = identity(path)
    row["path"] = (QA_ROOT / path.name).relative_to(ROOT).as_posix()
    return row


def require_snapshot() -> dict[str, Any]:
    record = snapshot_record
    if not isinstance(record, dict) or set(record) != {"path", "bytes", "sha256", "contract"}:
        raise QAError("launch through run.py; verified script snapshot is absent")
    live = SCRIPT.read_bytes()
    if (
        record["path"] != str(SCRIPT)
        or record["contract"] != "contract_json_read_hash_then_exec_same_bytes"
        or (len(live), digest(live)) != (record["bytes"], record["sha256"])
    ):
        raise QAError("verified script snapshot drifted")
    return dict(record)


def load_pinned_json(path_text: str, sha256: str, schema: str, status: str, label: str) -> tuple[dict[str, Any], dict[str, Any]]:
    path = Path(path_text)
    expected_sha = require_digest(sha256, f"{label} command-line hash")
    if not path.is_absolute():
        raise QAError(f"{label}: path must be absolute")
    if not path.is_file() or path.is_symlink() or path.resolve(strict=True) != path:
        raise QAError(f"{label}: invalid regular file")
    data = path.read_bytes()
    if digest(data) != expected_sha:
        raise QAError(f"{label}: explicit launch hash mismatch")
    value = parse_json(data, label)
    if value.get("schema") != schema or value.get("status") != status or value.get("contract_id") != CONTRACT_ID:
        raise QAError(f"{label}: schema/status/contract gate is not satisfied")
    return value, {"path": str(path), "bytes": len(data), "sha256": digest(data)}


def manifest(root: Path) -> dict[str, Any]:
    if not root.is_dir() or root.is_symlink() or root.resolve(strict=True) != root:
        raise QAError("r20 staged source root is invalid")
    rows: list[dict[str, Any]] = []
    for current, directories, files in os.walk(root, topdown=True, followlinks=False):
        directories.sort()
        files.sort()
        base = Path(current)
        for name in directories:
            path = base / name
            if path.is_symlink() or not path.is_dir():
                raise QAError(f"invalid staged directory: {path}")
        for name in files:
            path = base / name
            if path.is_symlink() or not path.is_file():
                raise QAError(f"invalid staged file: {path}")
            data = path.read_bytes()
            rows.append({"path": path.relative_to(root).as_posix(), "bytes": len(data), "sha256": digest(data)})
    rows.sort(key=lambda row: row["path"])
    encoded = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {"rows": len(rows), "total_file_bytes": sum(row["bytes"] for row in rows), "bytes": len(encoded), "sha256": digest(encoded)}


def strict_pdf(path: Path, expected: Mapping[str, Any], language: str) -> tuple[dict[str, Any], list[dict[str, Any]], dict[int, int], list[str]]:
    data = exact(path, (int(expected["bytes"]), str(expected["sha256"])), f"{language} PDF")
    expected_pages = int(expected["pages"])
    with warnings.catch_warnings(record=True) as captured:
        warnings.simplefilter("always")
        reader = PdfReader(io.BytesIO(data), strict=True)
        if reader.is_encrypted or len(reader.pages) != expected_pages:
            raise QAError(f"{language} PDF encryption/page count drifted")
        destination_pages: dict[int, list[int]] = {}
        source_rows: list[dict[str, Any]] = []
        anchor_map: dict[int, int] = {}
        pattern = re.compile(rf"^tohoku:source-page:(\d+):{language}:ed$")
        for name, destination in reader.named_destinations.items():
            match = pattern.match(name)
            if not match:
                continue
            printed = int(match.group(1))
            physical = reader.get_destination_page_number(destination) + 1
            source_rows.append({"language": language, "printed_page": printed, "pdf_page": physical, "destination": name})
            anchor_map[printed] = physical
            destination_pages.setdefault(physical, []).append(printed)
        source_rows.sort(key=lambda row: row["printed_page"])
        expected_printed = [page for page in range(119, 222) if page != 184]
        if [row["printed_page"] for row in source_rows] != expected_printed:
            raise QAError(f"{language} source-page destination inventory drifted")
        physical_rows: list[dict[str, Any]] = []
        content_hashes: list[str] = []
        for number, page in enumerate(reader.pages, 1):
            media = tuple(str(value) for value in page.mediabox)
            if media != EXPECTED_MEDIA_BOX:
                raise QAError(f"{language} page {number} MediaBox drifted: {media}")
            contents = page.get_contents()
            content = b"" if contents is None else contents.get_data()
            content_hashes.append(digest(content))
            physical_rows.append({
                "language": language,
                "pdf_page": number,
                "printed_pages": ";".join(str(value) for value in sorted(destination_pages.get(number, []))),
                "anchor_count": len(destination_pages.get(number, [])),
                "content_bytes": len(content),
                "content_sha256": digest(content),
                "media_box": " ".join(media),
            })
        objects = 0
        for generation, entries in reader.xref.items():
            for identifier in entries:
                if identifier > 0:
                    reader.get_object(IndirectObject(identifier, generation, reader))
                    objects += 1
        for identifier in reader.xref_objStm:
            reader.get_object(IndirectObject(identifier, 0, reader))
            objects += 1
    if captured:
        raise QAError(f"{language} strict parser warnings: {[str(item.message) for item in captured]}")
    return (
        {"file": identity(path), "pages": expected_pages, "objects_swept": objects, "encrypted": False, "warnings": [], "media_boxes_uniform": True, "source_page_destinations": len(source_rows), "result": "PASS"},
        physical_rows + source_rows,
        anchor_map,
        content_hashes,
    )


def validate_binding(binding: Mapping[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    required = {"build_receipt", "pdfs", "source_anchors_183_185_186", "content_stream_delta", "visual_pages"}
    if not required.issubset(binding):
        raise QAError("post-build binding is incomplete")
    build_spec = binding["build_receipt"]
    build_path = Path(str(build_spec["path"]))
    build_data = exact(build_path, (int(build_spec["bytes"]), require_digest(str(build_spec["sha256"]), "build receipt hash")), "bound r20 build receipt")
    build = parse_json(build_data, "bound r20 build receipt")
    if (
        build.get("schema") != "tohoku-v068-staged-successor-build-v1"
        or build.get("revision") != "v068c3r20"
        or build.get("predecessor_revision") != "v068c3r19"
        or build.get("status") != "PASS"
        or build.get("errors") != []
        or build.get("compile_order") != ["fr", "en"]
        or build.get("passes_per_language") != 2
        or build.get("shell") is not False
        or build.get("expected_reader_pages") != {"fr": 94, "en": 90}
    ):
        raise QAError("bound r20 build receipt headline drifted")
    verification = build.get("staged_source_verification", {})
    if tuple(verification.get(key) for key in ("rows", "total_file_bytes", "bytes", "sha256")) != STAGED_MANIFEST:
        raise QAError("bound r20 staged-source receipt drifted")
    surface = build.get("revision_surface_contract", {})
    if (
        surface.get("replaced_staged_paths") != ["en/p185.tex", "fr/p185.tex"]
        or surface.get("other_staged_source_changes") != 0
        or surface.get("selected_source_successor") != "production/p185_fix2"
        or surface.get("diplomatic_p185_byte_identical") is not True
    ):
        raise QAError("bound r20 revision surface drifted")
    expected_visual_pages = {"en": [52, 53, 54], "fr": [54, 55, 56]}
    expected_changed_pages = {"en": [53], "fr": [55]}
    replay: dict[str, Any] = {"compiled_to_final_byte_identity": {}, "logs_replayed": {}}
    for language in ("en", "fr"):
        spec = binding["pdfs"][language]
        path = Path(str(spec["path"]))
        if path != ROOT / "output" / "pdf" / f"{language}-p119-221-v068c3r20.pdf":
            raise QAError(f"bound {language} final path drifted")
        data = exact(path, (int(spec["bytes"]), require_digest(str(spec["sha256"]), f"{language} PDF hash")), f"bound r20 {language} final")
        row = build.get("pdfs", {}).get(language, {})
        if row.get("path") != path.relative_to(ROOT).as_posix() or row.get("bytes") != len(data) or row.get("sha256") != digest(data) or row.get("strict_pdf_parse", {}).get("pages") != int(spec["pages"]) or row.get("strict_pdf_parse", {}).get("result") != "PASS":
            raise QAError(f"bound r20 {language} final receipt mismatch")
        compiled = build.get("compile_evidence", {}).get(language, {}).get("built", {})
        compiled_path = ROOT / str(compiled.get("path", ""))
        compiled_data = exact(compiled_path, (len(data), digest(data)), f"bound r20 {language} compiled PDF")
        if compiled_data != data:
            raise QAError(f"r20 {language} compiled/final bytes differ")
        visual = binding["visual_pages"].get(language, {})
        if visual.get("predecessor") != expected_visual_pages[language] or visual.get("successor") != expected_visual_pages[language]:
            raise QAError(f"{language} visual page scope drifted")
        if binding["content_stream_delta"].get(language, {}).get("changed_pages") != expected_changed_pages[language]:
            raise QAError(f"{language} expected changed-page binding drifted")
        replay["compiled_to_final_byte_identity"][language] = True
        replay["logs_replayed"][language] = []
        for log in build.get("compile_evidence", {}).get(language, {}).get("logs", []):
            path_log = ROOT / str(log.get("path", ""))
            payload = exact(path_log, (int(log.get("bytes", -1)), str(log.get("sha256", ""))), f"r20 {language} compile log")
            findings = [line for line in payload.decode("utf-8", errors="replace").splitlines() if STRICT_LOG_PATTERN.search(line)]
            if findings or log.get("findings") != []:
                raise QAError(f"r20 {language} compile log findings: {findings}")
            replay["logs_replayed"][language].append(identity(path_log))
    return build, replay


def render_page(pdf: Path, page: int, prefix: Path) -> Path:
    result = subprocess.run(
        [str(PDFTOPPM), "-f", str(page), "-l", str(page), "-singlefile", "-r", "220", "-png", str(pdf), str(prefix)],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False,
        check=False,
    )
    if result.returncode != 0 or result.stdout or result.stderr:
        raise QAError(f"pdftoppm failed or emitted output for {prefix.name}: {result.returncode}")
    output = prefix.with_suffix(".png")
    if not output.is_file():
        raise QAError(f"render output missing: {output}")
    return output


def write_json_new(path: Path, value: Any) -> None:
    data = (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    with path.open("xb") as output:
        output.write(data)
        output.flush()
        os.fsync(output.fileno())


def preflight(binding: Mapping[str, Any], binding_record: Mapping[str, Any], launch: Mapping[str, Any]) -> dict[str, Any]:
    exact(P185_RECEIPT, P185_RECEIPT_EXPECTED, "p185_fix2 receipt")
    ledger = exact(SOURCE_LEDGER, SOURCE_LEDGER_EXPECTED, "source correction ledger")
    if ledger.count(b'"decision_id":"TOH-SRC-P185-002"') != 1 or b'"layer":"fr_corrected;en"' not in ledger:
        raise QAError("D1017-R001 source ledger row drifted")
    staged = manifest(STAGED_SOURCE)
    if tuple(staged[key] for key in ("rows", "total_file_bytes", "bytes", "sha256")) != STAGED_MANIFEST:
        raise QAError("live r20 staged-source manifest drifted")
    build, replay = validate_binding(binding)
    return {"status": "READY_NOT_EXECUTED", "script": dict(launch), "binding": dict(binding_record), "staged_source": staged, "build_receipt_status": build["status"], "deterministic_build_replay": replay}


def prepare(binding: Mapping[str, Any], binding_record: Mapping[str, Any], launch: Mapping[str, Any]) -> dict[str, Any]:
    summary = preflight(binding, binding_record, launch)
    if os.path.lexists(QA_ROOT) or os.path.lexists(QA_STAGE):
        raise FileExistsError("v68r42 final or stage already exists")
    exact(PDFTOPPM, PDFTOPPM_EXPECTED, "pdftoppm")
    QA_STAGE.mkdir(exist_ok=False)
    inventory_rows: list[dict[str, Any]] = []
    structural: dict[str, Any] = {
        "schema": "tohoku-v068-reader-independent-qa-prepare-v42",
        "qa_revision": "v68r42",
        "reader_revision": "v068c3r20",
        "predecessor_revision": "v068c3r19",
        "created_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "status": "STRUCTURAL_PASS_VISUAL_PENDING",
        "errors": [],
        "launcher": dict(launch),
        "post_build_binding": dict(binding_record),
        "deterministic_build_replay": summary["deterministic_build_replay"],
        "staged_source": summary["staged_source"],
        "pdfs": {},
        "p185_and_seam_review": {},
    }
    for language in ("en", "fr"):
        pred_path, pred_bytes, pred_sha, pred_pages = PREDECESSOR_PDFS[language]
        pred_spec = {"bytes": pred_bytes, "sha256": pred_sha, "pages": pred_pages}
        succ_spec = binding["pdfs"][language]
        succ_path = Path(str(succ_spec["path"]))
        pred_record, _pred_inventory, pred_anchors, pred_hashes = strict_pdf(pred_path, pred_spec, language)
        succ_record, succ_inventory, succ_anchors, succ_hashes = strict_pdf(succ_path, succ_spec, language)
        expected_anchors = {int(key): int(value) for key, value in binding["source_anchors_183_185_186"][language].items()}
        if {page: succ_anchors[page] for page in (183, 185, 186)} != expected_anchors:
            raise QAError(f"{language} p183/p185/p186 source-anchor binding drifted")
        delta = binding["content_stream_delta"][language]
        compared = min(len(pred_hashes), len(succ_hashes))
        changed = [index + 1 for index in range(compared) if pred_hashes[index] != succ_hashes[index]]
        expected_changed = [int(value) for value in delta["changed_pages"]]
        if changed != expected_changed or compared - len(changed) != int(delta["byte_identical_pages"]):
            raise QAError(f"{language} content-stream delta differs from explicit post-build binding")
        structural["pdfs"][language] = {"predecessor": pred_record, "successor": succ_record, "compared_physical_pages": compared, "byte_identical_content_stream_pages": compared - len(changed), "changed_physical_content_stream_pages": changed}
        inventory_rows.extend(succ_inventory)
        pred_pages_visual = [int(value) for value in binding["visual_pages"][language]["predecessor"]]
        succ_pages_visual = [int(value) for value in binding["visual_pages"][language]["successor"]]
        pred_rasters = [render_page(pred_path, page, QA_STAGE / f"{language}-r19-page-{page}") for page in pred_pages_visual]
        succ_rasters = [render_page(succ_path, page, QA_STAGE / f"{language}-r20-page-{page}") for page in succ_pages_visual]
        structural["p185_and_seam_review"][language] = {
            "printed_pages": [183, 185, 186],
            "source_anchor_map": {str(page): succ_anchors[page] for page in (183, 185, 186)},
            "predecessor_rasters": [{"pdf_page": page, "raster": staged_identity(path)} for page, path in zip(pred_pages_visual, pred_rasters)],
            "successor_rasters": [{"pdf_page": page, "raster": staged_identity(path)} for page, path in zip(succ_pages_visual, succ_rasters)],
        }
    inventory = QA_STAGE / "page-inventory.csv"
    fields = ["language", "pdf_page", "printed_pages", "anchor_count", "content_bytes", "content_sha256", "media_box", "printed_page", "destination"]
    with inventory.open("x", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(inventory_rows)
        output.flush()
        os.fsync(output.fileno())
    structural["page_inventory"] = {**staged_identity(inventory), "rows": len(inventory_rows), "physical_page_rows": sum(int(binding["pdfs"][language]["pages"]) for language in ("en", "fr")), "source_anchor_rows": 204, "result": "PASS"}
    write_json_new(QA_STAGE / "structural.json", structural)
    return {"status": structural["status"], "stage": str(QA_STAGE), "structural": identity(QA_STAGE / "structural.json"), "visual_attestation_gate": "PENDING_EXPLICIT_SHA256"}


def commit(binding: Mapping[str, Any], binding_record: Mapping[str, Any], launch: Mapping[str, Any], attestation_path: str, attestation_sha256: str) -> dict[str, Any]:
    _ = preflight(binding, binding_record, launch)
    if os.path.lexists(QA_ROOT) or not QA_STAGE.is_dir() or QA_STAGE.is_symlink():
        raise QAError("v68r42 commit namespace is invalid")
    attestation, attestation_record = load_pinned_json(attestation_path, attestation_sha256, "d1017-r42-visual-attestation-v1", "PASS", "visual attestation")
    structural_path = QA_STAGE / "structural.json"
    structural = parse_json(structural_path.read_bytes(), "v68r42 structural receipt")
    if structural.get("status") != "STRUCTURAL_PASS_VISUAL_PENDING" or structural.get("errors") != [] or structural.get("reader_revision") != "v068c3r20":
        raise QAError("v68r42 structural receipt semantics drifted")
    if attestation.get("structural_sha256") != digest(structural_path.read_bytes()) or attestation.get("defects") != []:
        raise QAError("visual attestation does not bind the exact structural receipt or reports defects")
    expected_visual = {
        language: [item["pdf_page"] for item in structural["p185_and_seam_review"][language]["successor_rasters"]]
        for language in ("en", "fr")
    }
    if attestation.get("inspected_successor_pages") != expected_visual:
        raise QAError("visual attestation page inventory drifted")
    raster_records = {
        Path(item["raster"]["path"]).name: item["raster"]["sha256"]
        for language in ("en", "fr")
        for collection in ("predecessor_rasters", "successor_rasters")
        for item in structural["p185_and_seam_review"][language][collection]
    }
    if attestation.get("raster_sha256") != raster_records:
        raise QAError("visual attestation raster identity surface drifted")
    for name, sha in raster_records.items():
        path = QA_STAGE / name
        if digest(path.read_bytes()) != sha:
            raise QAError(f"visual raster changed after attestation: {name}")
    check = {
        "schema": "tohoku-v068-reader-independent-qa-v1",
        "qa_revision": "v68r42",
        "reader_revision": "v068c3r20",
        "predecessor_revision": "v068c3r19",
        "created_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "status": "PASS",
        "errors": [],
        "stable_id": "tohoku:reader-qa:v68r42:v068c3r20",
        "audit_launcher": dict(launch),
        "post_build_binding": dict(binding_record),
        "visual_attestation": attestation_record,
        "structural_receipt": staged_identity(structural_path),
        "page_inventory": structural["page_inventory"],
        "deterministic_build_replay": structural["deterministic_build_replay"],
        "p185_visual_review": {"status": "PASS", "scope": "physical-page triples en52--54 and fr54--56, binding printed p183/p185/p186 in both editions", "attestation": attestation},
        "conclusion": {"reader_successor_accepted": True, "pdf_pair_accepted": True, "source_transition_exact": True, "visual_review_accepted": True, "page_inventory_complete": True, "deterministic_receipt_replay_accepted": True, "semantic_replay_claimed": False, "blockers": []},
        "nonclaims": ["No semantic graph, Stacks source, mapping, Git, GitHub, release, or publication is changed by this QA gate."],
    }
    write_json_new(QA_STAGE / "check.json", check)
    os.rename(QA_STAGE, QA_ROOT)
    final = QA_ROOT / "check.json"
    if parse_json(final.read_bytes(), "committed v68r42 receipt") != check:
        raise QAError("committed v68r42 receipt readback differs")
    return {"status": "PASS", "qa_root": str(QA_ROOT), "check": identity(final)}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Independent v68r42 QA with explicit post-build and visual identity gates.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--preflight", action="store_true")
    group.add_argument("--prepare", action="store_true")
    group.add_argument("--commit-visual-pass", action="store_true")
    parser.add_argument("--bindings", required=True)
    parser.add_argument("--bindings-sha256", required=True)
    parser.add_argument("--attestation")
    parser.add_argument("--attestation-sha256")
    args = parser.parse_args(sys.argv[1:] if argv is None else list(argv))
    launch = require_snapshot()
    binding, binding_record = load_pinned_json(args.bindings, args.bindings_sha256, "d1017-r20-output-bindings-v1", "PINNED_POST_BUILD", "post-build binding")
    if args.preflight:
        result = preflight(binding, binding_record, launch)
    elif args.prepare:
        result = prepare(binding, binding_record, launch)
    else:
        if not args.attestation or not args.attestation_sha256:
            raise QAError("visual commit requires --attestation and --attestation-sha256")
        result = commit(binding, binding_record, launch, args.attestation, args.attestation_sha256)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise SystemExit(1)
