#!/usr/bin/env python3
"""Build the exact editable-source ZIP paired with the Verdier candidate PDF."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]
BASE_COMMIT = "f73b18165c7162b8386de06cc3c50bd4ced745b6"
BASE_TREE = "5bc25c775349eddf5fa90a7f37f5b11044d89ec1"
CANDIDATE = Path("ai-integrated/candidates/commons/stacks/verdier-ast239-1-3-6-r1")
OPERATION_PATH = CANDIDATE / "composition.jsonl"
PAYLOAD_PATH = CANDIDATE / "payload/fragments/derived-homotopy-category-abelian-split.tex"
PDF_PATH = CANDIDATE / "builds/derived.pdf"
ZIP_PATH = Path("validation/verdier-ast239-1-3-6-candidate-derived-source.zip")
MANIFEST_PATH = Path("validation/verdier-ast239-1-3-6-candidate-derived-source-manifest.json")
STEMS = (
    "sets", "categories", "algebra", "homology", "more-algebra", "injectives",
    "examples", "derived",
)
BASE_FILES = (
    "COPYING", "CONTRIBUTORS", "README", "README.md", "Makefile", "chapters.tex",
    "hyperref.cfg", "my.bib", "preamble.tex", "stacks-project-book.cls",
    "stacks-project.cls",
) + tuple(stem + ".tex" for stem in STEMS if stem != "derived")
FIXED_ZIP_TIME = (2026, 9, 28, 0, 0, 0)


class PackageError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PackageError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def git_bytes(*args: str) -> bytes:
    done = subprocess.run(
        ["git", "-C", str(ROOT), *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=False, timeout=60,
    )
    require(done.returncode == 0, done.stderr.decode("utf-8", "replace"))
    return done.stdout


def git_text(*args: str) -> str:
    return git_bytes(*args).decode("utf-8").strip()


def load_operation() -> dict:
    rows = [line for line in (ROOT / OPERATION_PATH).read_text(encoding="utf-8").splitlines()
            if line.strip()]
    require(len(rows) == 1, "candidate composition must contain exactly one operation")
    value = json.loads(rows[0])
    require(isinstance(value, dict), "candidate composition is not an object")
    return value


def assembled_derived(operation: dict) -> bytes:
    target = operation.get("target", {})
    require(target.get("commit") == BASE_COMMIT and target.get("tree") == BASE_TREE
            and target.get("path") == "derived.tex", "candidate base identity mismatch")
    require(git_text("rev-parse", BASE_COMMIT + "^{tree}") == BASE_TREE,
            "candidate base tree is unavailable")
    base = git_bytes("show", BASE_COMMIT + ":derived.tex")
    require(len(base) == target.get("bytes") and sha(base) == target.get("preimage_sha256"),
            "candidate derived.tex preimage mismatch")
    payload = (ROOT / PAYLOAD_PATH).read_bytes()
    payload_meta = operation.get("payload", {})
    require(len(payload) == payload_meta.get("bytes") and sha(payload) == payload_meta.get("sha256"),
            "candidate payload mismatch")
    insertion = operation.get("insertion", {})
    start, offset, end = (insertion.get(key) for key in (
        "context_start_byte", "byte_offset", "context_end_byte_exclusive"))
    require(all(type(value) is int for value in (start, offset, end))
            and 0 <= start <= offset <= end <= len(base), "invalid insertion offsets")
    require(sha(base[start:end]) == insertion.get("context_sha256")
            and sha(base[start:offset]) == insertion.get("before_context_sha256")
            and sha(base[offset:end]) == insertion.get("after_context_sha256"),
            "candidate insertion context mismatch")
    result = base[:offset] + payload + base[offset:]
    require(len(result) == target.get("postimage_bytes")
            and sha(result) == target.get("postimage_sha256"),
            "candidate derived.tex postimage mismatch")
    require(result[:offset] == base[:offset] and result[offset + len(payload):] == base[offset:],
            "candidate operation changed pre-existing bytes")
    return result


def build_readme(operation: dict, pdf: bytes) -> bytes:
    return (
        "Verdier II.1.3.6 candidate PDF — exact editable source\n"
        "=======================================================\n\n"
        "This archive reproduces the candidate QA artifact\n"
        f"`{PDF_PATH.as_posix()}` ({len(pdf)} bytes; SHA-256 {sha(pdf)}).\n\n"
        f"The base is commit {BASE_COMMIT}, tree {BASE_TREE}.  `derived.tex` is the exact\n"
        "insertion-only postimage of operation VDR-STK-COMP-0002; all other included source\n"
        "files are byte-exact base-commit files.  The eight stems used by the recorded build\n"
        "are sets, categories, algebra, homology, more-algebra, injectives, examples, and\n"
        "derived.  No unrelated external auxiliary files are required; the original build\n"
        "held them absent in both its baseline and candidate runs.\n\n"
        "Build from this directory with pdfLaTeX and BibTeX.  Prime each of the eight stems\n"
        "once with pdfLaTeX, run BibTeX once for each stem, then run global pdfLaTeX sweeps\n"
        "over the stems in the order above until the PDF/AUX/TOC/OUT/BBL vector is unchanged\n"
        "on two consecutive sweeps (maximum six).  The recorded environment used MiKTeX\n"
        "pdfTeX 4.27 and BibTeX 4.2 with `SOURCE_DATE_EPOCH=1788641805` and timezone UTC.\n\n"
        "AI typesetting and mathematical translation/correction for the inserted material:\n"
        "OpenAI Codex — GPT-5.6 Sol, Ultra effort.  No human review is claimed.\n"
    ).encode("utf-8")


def zip_bytes(entries: dict[str, bytes]) -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(entries):
            info = zipfile.ZipInfo(name, FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, entries[name], compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return output.getvalue()


def render() -> tuple[bytes, bytes]:
    operation = load_operation()
    pdf = (ROOT / PDF_PATH).read_bytes()
    require(len(pdf) == 1_251_089
            and sha(pdf) == "1B45A53DFDC6394AB795855172915794F20634953361E8596AF17FC2E6F97331",
            "candidate PDF identity mismatch")
    entries = {"source/" + path: git_bytes("show", BASE_COMMIT + ":" + path)
               for path in BASE_FILES}
    entries["source/derived.tex"] = assembled_derived(operation)
    entries["BUILD.md"] = build_readme(operation, pdf)
    packed = zip_bytes(entries)
    manifest = {
        "schema": "unofficial-ai-integrated-stacks-rendered-source-package/v1",
        "status": "PASS_COMPLETE_EDITABLE_SOURCE",
        "artifact": {"path": PDF_PATH.as_posix(), "bytes": len(pdf), "sha256": sha(pdf)},
        "direct_editable_source": {
            "path": "derived.tex", "bytes": len(entries["source/derived.tex"]),
            "sha256": sha(entries["source/derived.tex"]),
        },
        "source_basis": {"commit": BASE_COMMIT, "tree": BASE_TREE,
                         "operation_id": operation["operation_id"]},
        "build_profile": {"stems": list(STEMS), "maximum_sweeps": 6,
                          "source_date_epoch": "1788641805", "timezone": "UTC"},
        "archive": {"path": ZIP_PATH.as_posix(), "bytes": len(packed), "sha256": sha(packed),
                    "entry_count": len(entries)},
        "entries": [
            {"path": name, "bytes": len(entries[name]), "sha256": sha(entries[name])}
            for name in sorted(entries)
        ],
        "ai_disclosure": "OpenAI Codex — GPT-5.6 Sol, Ultra effort",
        "human_review_claimed": False,
    }
    encoded = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return packed, encoded


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        packed, manifest = render()
        if args.check:
            require((ROOT / ZIP_PATH).read_bytes() == packed, "source ZIP differs from deterministic output")
            require((ROOT / MANIFEST_PATH).read_bytes() == manifest,
                    "source-package manifest differs from deterministic output")
        else:
            (ROOT / ZIP_PATH).write_bytes(packed)
            (ROOT / MANIFEST_PATH).write_bytes(manifest)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError,
            subprocess.SubprocessError, PackageError) as exc:
        print("Verdier candidate source packaging: FAIL\n- " + str(exc), file=sys.stderr)
        return 1
    print("Verdier candidate source packaging: PASS")
    print(f"- archive: {ZIP_PATH.as_posix()} ({len(packed)} bytes; SHA-256 {sha(packed)})")
    print(f"- manifest: {MANIFEST_PATH.as_posix()} ({len(manifest)} bytes; SHA-256 {sha(manifest)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
