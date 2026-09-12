#!/usr/bin/env python3
"""Generate R48 SyncTeX while preserving the complete 36-chapter fixed point.

One mutex covers both captured TeX trees, all descendant draining and immediate
checks. The result is instrumentation evidence only, never a visual-review claim.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
from pathlib import Path
import time

if __package__:
    from . import map_r48_visual_loci as mapping
else:
    import map_r48_visual_loci as mapping

builder = mapping.builder


def valid_sidecar(path, stem):
    with gzip.open(path, "rb") as stream:
        raw = stream.read()
    mapping.require(raw.startswith(b"SyncTeX Version:") and b"Content:\n" in raw
                    and b"Postamble:\n" in raw and (stem + ".tex").encode() in raw,
                    f"malformed SyncTeX sidecar: {stem}")
    return {"decompressed_bytes": len(raw), "decompressed_sha256": mapping.sha256(raw)}


def instrument(build, artifacts, source, context):
    mapping.recheck_inputs(context)
    stems = build["build"]["stems"]
    before_all = {stem: mapping.fixed_snapshot(source, stem) for stem in stems}
    for stem in stems:
        mapping.require(stem + ".aux" in before_all[stem] and stem + ".pdf" in before_all[stem],
                        f"fixed-point PDF/AUX missing: {stem}")
        mapping.require_identity(mapping.identity(source / (stem + ".pdf")), artifacts[stem], stem)
    for stem in mapping.STEMS:
        mapping.require(not (source / (stem + ".synctex.gz")).exists(), f"existing sidecar: {stem}")
    env = {**os.environ, "SOURCE_DATE_EPOCH": build["environment"]["source_date_epoch"],
           "FORCE_SOURCE_DATE": "1", "TZ": "UTC"}
    labels, rows = builder.external_reference_labels(source), []
    mutex = builder.WindowsNamedMutex(builder.TEX_MUTEX_NAME, builder.TEX_MUTEX_TIMEOUT_MS)
    with mutex:
        mapping.recheck_inputs(context)
        for stem in mapping.STEMS:
            sidecar = source / (stem + ".synctex.gz")
            mapping.require(not sidecar.exists(), f"sidecar appeared before launch: {stem}")
            command = mapping.tex_command(stem)
            started_utc, started_ns = mapping.utc_now(), time.time_ns()
            previous_captures = len(getattr(mutex, "process_tree_receipts", []))
            builder.run(command, source, env, mutex)
            captures = getattr(mutex, "process_tree_receipts", [])
            mapping.require(len(captures) == previous_captures + 1, "TeX launch lacks unique captured-tree receipt")
            mapping.check_captures([captures[-1]], 1)
            # Capture paths are public virtual names. The sanitized wrapper
            # cryptographically binds native bytes without exposing their path.
            # The builder returns only after the captured Job has no live descendants.
            # Keep the same mutex owned during all of these immediate checks.
            mapping.require(mutex.owned, "TeX mutex not owned through immediate checks")
            diagnostics, references = builder.scan_tex_diagnostics(source / (stem + ".log"), source / (stem + ".blg"), stem, labels)
            mapping.require(diagnostics == artifacts[stem]["diagnostics"]
                            and references == artifacts[stem]["external_references"], f"diagnostics changed: {stem}")
            after = mapping.fixed_snapshot(source, stem)
            mapping.require(after == before_all[stem], f"fixed-point bytes changed: {stem}")
            mapping.require(sidecar.is_file() and sidecar.stat().st_size > 0, f"fresh sidecar missing: {stem}")
            structure = valid_sidecar(sidecar, stem)
            sidecar_id, modified_ns = mapping.identity(sidecar), sidecar.stat().st_mtime_ns
            completed_ns, completed_utc = time.time_ns(), mapping.utc_now()
            mapping.require(0 < started_ns <= modified_ns <= completed_ns, f"sidecar freshness not proved: {stem}")
            rows.append({"stem": stem, "command": command, "exit_code": 0, "capture": captures[-1],
                "sidecar_absent_before": True, "synctex_regenerated": True,
                "started_at_utc": started_utc, "completed_at_utc": completed_utc,
                "started_ns": started_ns, "completed_ns": completed_ns, "synctex_mtime_ns": modified_ns,
                "synctex": sidecar_id, "synctex_structure": structure,
                "pdf_before": before_all[stem][stem + ".pdf"], "pdf_after": after[stem + ".pdf"],
                "fixed_point_artifacts_before": before_all[stem], "fixed_point_artifacts_after": after,
                "diagnostics": diagnostics, "external_references": references,
                "tex_mutex_owned_through_immediate_checks": True})
        after_all = {stem: mapping.fixed_snapshot(source, stem) for stem in stems}
        mapping.require(before_all == after_all, "instrumentation changed another profile artifact")
        mapping.recheck_inputs(context)
    captures = getattr(mutex, "process_tree_receipts", [])
    mapping.check_captures(captures, len(mapping.STEMS), mutex.receipt_details())
    return rows, mutex.receipt_details(), captures, before_all, after_all


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=mapping.ROOT)
    parser.add_argument("--build-receipt", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    source = mapping.configure_source(args.source)
    mapping.require(Path(__file__).resolve() == source / mapping.TOOL_PATHS[0],
                    "instrumenter must execute from the selected build worktree")
    resolve = lambda p: p.resolve() if p.is_absolute() else (source / p).resolve()
    build_path, output = map(resolve, (args.build_receipt, args.output))
    mapping.require(not output.exists() and output.parent == source / "validation", "invalid or existing output")
    build_id = mapping.identity(build_path)
    build, artifacts, context = mapping.load_build(build_path)
    rows, mutex, captures, before, after = instrument(build, artifacts, source, context)
    mapping.recheck_inputs(context)
    mapping.require(mapping.identity(build_path) == build_id, "build receipt changed during instrumentation")
    result = {"schema": mapping.INSTRUMENTATION_SCHEMA, "status": "PASS", "created_utc": mapping.utc_now(),
        "source": build["source"], "build_receipt": {"path": mapping.relative_path(build_path), **build_id},
        "environment": {"SOURCE_DATE_EPOCH": build["environment"]["source_date_epoch"], "FORCE_SOURCE_DATE": "1", "TZ": "UTC"},
        "artifacts": rows, "machine_wide_tex_mutex": mutex,
        "tex_process_tree": {"schema": "unofficial-ai-integrated-stacks-tex-process-tree-build/v1",
            "guard": builder.committed_file_identity(source, build["source"]["commit"], "tools/tex_process_guard.py"),
            "launch_count": len(captures), "launches": captures},
        "frozen_inputs": context["files"], "full_profile_artifacts_before": before, "full_profile_artifacts_after": after,
        "tooling": [{"path": p, **mapping.identity(source / p)} for p in mapping.TOOL_PATHS],
        "scope": "Fresh R48 locator instrumentation only. All 36 fixed-point artifact inventories remain exact. No visual review is claimed."}
    with output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps({"status": "PASS", "output": mapping.relative_path(output), **mapping.identity(output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
