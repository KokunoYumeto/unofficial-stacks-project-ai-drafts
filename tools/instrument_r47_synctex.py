#!/usr/bin/env python3
"""Produce fresh R47 SyncTeX under one machine-wide TeX mutex.

The five instrumentation passes must preserve every fixed-point artifact and
all validated inputs. This is instrumentation, not a new mathematical build or
visual-inspection claim. Source and builder are pinned to the actual first
build; this post-build tool's exact bytes are recorded without moving HEAD.
"""
from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

if __package__:
    from . import build_fixed_point as builder
    from . import map_r47_visual_qa as mapping
else:
    import build_fixed_point as builder
    import map_r47_visual_qa as mapping


def instrument(build: dict, artifacts: dict, source: Path, input_rows: list[dict]) -> tuple[list[dict], dict]:
    """Run exactly one guarded batch; no retry, launch, or version probe outside it."""
    head = build["source"]["commit"]
    mapping.require(mapping.git("rev-parse", "HEAD") == head, "instrumentation HEAD differs from first build")
    stems = build["build"]["stems"]
    before_all = {stem: mapping.fixed_snapshot(source, stem) for stem in stems}
    for stem in mapping.STEMS:
        mapping.require(not (source / f"{stem}.synctex.gz").exists(), f"SyncTeX already exists: {stem}")
        mapping.require(f"{stem}.aux" in before_all[stem] and f"{stem}.pdf" in before_all[stem],
                        f"fixed-point PDF/AUX absent: {stem}")
        mapping.require_identity(mapping.identity(source / f"{stem}.pdf"), artifacts[stem], stem)
    env = {**os.environ, "SOURCE_DATE_EPOCH": build["environment"]["source_date_epoch"],
           "FORCE_SOURCE_DATE": "1", "TZ": "UTC"}
    labels = builder.external_reference_labels(source)
    rows = []
    mutex = builder.WindowsNamedMutex(builder.TEX_MUTEX_NAME, builder.TEX_MUTEX_TIMEOUT_MS)
    with mutex:
        mapping.recheck_inputs(input_rows)
        for stem in mapping.STEMS:
            sidecar = source / f"{stem}.synctex.gz"
            mapping.require(not sidecar.exists(), f"sidecar appeared before captured run: {stem}")
            before = mapping.fixed_snapshot(source, stem)
            command = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                       "-file-line-error", "-synctex=1", f"{stem}.tex"]
            started_utc, started_ns = mapping.utc_now(), time.time_ns()
            builder.run(command, source, env, mutex)
            # The same mutex remains owned throughout log, sidecar and byte checks.
            diagnostics, references = builder.scan_tex_diagnostics(
                source / f"{stem}.log", source / f"{stem}.blg", stem, labels)
            mapping.require(diagnostics == artifacts[stem]["diagnostics"]
                            and references == artifacts[stem]["external_references"],
                            f"instrumentation diagnostics changed: {stem}")
            after = mapping.fixed_snapshot(source, stem)
            mapping.require(before == after == before_all[stem], f"fixed-point bytes changed: {stem}")
            mapping.require(sidecar.is_file() and sidecar.stat().st_size > 0,
                            f"fresh SyncTeX missing: {stem}")
            sidecar_id, sidecar_mtime = mapping.identity(sidecar), sidecar.stat().st_mtime_ns
            completed_ns, completed_utc = time.time_ns(), mapping.utc_now()
            mapping.require(0 < started_ns <= sidecar_mtime <= completed_ns,
                            f"SyncTeX generation timestamp is outside run: {stem}")
            rows.append({"stem": stem, "command": command, "exit_code": 0,
                "synctex_regenerated": True, "sidecar_absent_before": True,
                "started_at_utc": started_utc, "completed_at_utc": completed_utc,
                "started_ns": started_ns, "completed_ns": completed_ns,
                "synctex_mtime_ns": sidecar_mtime, "synctex": sidecar_id,
                "pdf_before": before[f"{stem}.pdf"], "pdf_after": after[f"{stem}.pdf"],
                "fixed_point_artifacts_before": before, "fixed_point_artifacts_after": after,
                "diagnostics": diagnostics, "external_references": references,
                "tex_mutex_owned_through_immediate_checks": True})
        mapping.require({stem: mapping.fixed_snapshot(source, stem) for stem in stems} == before_all,
                        "instrumentation changed another fixed-point artifact")
        mapping.recheck_inputs(input_rows)
        mapping.require(mapping.git("rev-parse", "HEAD") == head, "HEAD changed during instrumentation")
    return rows, mutex.receipt_details()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=mapping.ROOT)
    parser.add_argument("--build-receipt", type=Path, default=Path(mapping.BUILD_PATH))
    parser.add_argument("--output", type=Path, default=Path(mapping.INSTRUMENTATION_PATH))
    args = parser.parse_args(argv)
    source = mapping.configure_source(args.source)
    resolve = lambda p: p.resolve() if p.is_absolute() else (source / p).resolve()
    build_path, output = resolve(args.build_receipt), resolve(args.output)
    mapping.require(not output.exists() and output.parent == source / "validation",
                    "instrumentation output is existing or outside validation")
    build_id = mapping.identity(build_path)
    tool_path = Path(__file__).resolve()
    mapper_path = Path(mapping.__file__).resolve()
    tool_id, mapper_id = mapping.identity(tool_path), mapping.identity(mapper_path)
    build, artifacts = mapping.load_build(build_path)
    inputs = mapping.build_inputs(build)
    rows, mutex = instrument(build, artifacts, source, inputs)
    mapping.require(mapping.identity(build_path) == build_id and mapping.identity(tool_path) == tool_id
                    and mapping.identity(mapper_path) == mapper_id, "instrumentation tool/receipt changed")
    result = {"schema": mapping.INSTRUMENTATION_SCHEMA, "status": "PASS",
        "created_utc": mapping.utc_now(), "source": build["source"],
        "build_receipt": {"path": mapping.relative_path(build_path), **build_id},
        "environment": {"SOURCE_DATE_EPOCH": build["environment"]["source_date_epoch"],
                        "FORCE_SOURCE_DATE": "1", "TZ": "UTC"},
        "artifacts": rows, "machine_wide_tex_mutex": mutex, "frozen_inputs": inputs,
        "tooling": [{"path": "tools/instrument_r47_synctex.py", **tool_id},
                    {"path": "tools/map_r47_visual_qa.py", **mapper_id}],
        "scope": "Fresh source-page instrumentation only; all 35 fixed-point artifact inventories remain exact. No visual review is claimed."}
    with output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps({"status": "PASS", "output": mapping.relative_path(output), **mapping.identity(output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
