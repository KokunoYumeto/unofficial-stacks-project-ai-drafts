#!/usr/bin/env python3
"""Map R48's exact cumulative replacements to freshly instrumented PDF pages.

No TeX or rendering is launched by this mapper. A passing map is locator
evidence, not visual inspection. Historical R47 tooling and receipts are not
rewritten or relabelled.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

sys.dont_write_bytecode = True
if __package__:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from . import build_fixed_point as builder
    from .compose_overlay_projection import apply_operations, rebase_operations
    from .tex_process_public_receipt import (validate_public_capture_receipt,
        canonical_public_capture_bytes, public_capture_time)
    from .validate_unified_repository import validate_machine_wide_tex_mutex
else:
    import build_fixed_point as builder
    from compose_overlay_projection import apply_operations, rebase_operations
    from tex_process_public_receipt import (validate_public_capture_receipt,
        canonical_public_capture_bytes, public_capture_time)
    from validate_unified_repository import validate_machine_wide_tex_mutex

ROOT = Path(__file__).resolve().parents[1]
STEMS = ("groupoids", "spaces-perfect")
EXPECTED_APPLIED = {"groupoids": 6, "spaces-perfect": 21}
OPERATION_COUNT = 27
OVERLAY = "stacks-errata-a04446e-r48"
OFFICIAL_BASELINE = "a04446e57ec1fbc252a871afcec7752fb2807b14"
ADMISSION = "54cb855d7f499c885020efb7aebd24959cda5120"
COMPOSED = "0fee11e74c467744052f62e90a4454f9c20719a3"
MANIFEST_SHA256 = "C48ACC7D4DC69A634FDE0D3BA3B3FC55D597DC720A88875B5EFE4038C2D92997"
PREFIX = "ai-integrated/candidates/commons/stacks/errata/r48/"
DIRECT_SCHEMA = "unofficial-ai-integrated-stacks-direct-composition/v1"
INSTRUMENTATION_SCHEMA = "unofficial-ai-integrated-stacks-r48-synctex-instrumentation/v1"
TOOL_PATHS = ("tools/instrument_r48_synctex.py", "tools/map_r48_visual_loci.py")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def identity(path):
    raw = Path(path).read_bytes()
    return {"bytes": len(raw), "sha256": sha256(raw)}


def require_identity(observed, expected, label):
    require(isinstance(observed, dict) and isinstance(expected, dict)
            and type(observed.get("bytes")) is int
            and all(observed.get(key) == expected.get(key) for key in ("bytes", "sha256")),
            f"identity mismatch: {label}")


def safe_path(value):
    require(isinstance(value, str) and value and "\\" not in value and ":" not in value
            and not PurePosixPath(value).is_absolute() and ".." not in PurePosixPath(value).parts
            and PurePosixPath(value).as_posix() == value, "unsafe evidence path")
    return value


def git(*args):
    return builder.git(ROOT, *args)


def git_blob(revision, path):
    require(re.fullmatch(r"[0-9a-f]{40}", revision) is not None, "full commit required")
    return subprocess.check_output(["git", "-C", str(ROOT), "cat-file", "blob",
                                   f"{revision}:{safe_path(path)}"], stderr=subprocess.PIPE, timeout=120)


def configure_source(source):
    global ROOT
    selected = Path(source).resolve()
    require(Path(__file__).resolve() == selected / TOOL_PATHS[1]
            and Path(builder.__file__).resolve() == selected / "tools/build_fixed_point.py",
            "execute the committed tools from the selected build worktree; cross-checkout tooling is forbidden")
    ROOT = selected
    require(Path(git("rev-parse", "--show-toplevel")).resolve() == ROOT,
            "source must be an exact worktree root")
    return ROOT


def load_json(path):
    value = builder.strict_json_loads(Path(path).read_text(encoding="utf-8"), Path(path).name)
    require(isinstance(value, dict), "JSON object required")
    return value


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def relative_path(path):
    return Path(path).resolve().relative_to(ROOT).as_posix()


def frozen_file(path, revision):
    safe_path(path)
    builder.require_clean_path(ROOT, path)
    raw = git_blob(revision, path)
    require((ROOT / path).read_bytes() == raw, f"working bytes differ from build: {path}")
    return {"path": path, "bytes": len(raw), "sha256": sha256(raw)}


def recheck_inputs(context):
    build, binding = context["build"], context["binding"]
    builder.require_source_revision_unchanged(ROOT, build["source"]["commit"], build["source"]["tree"])
    builder.require_direct_tools_unchanged(ROOT, binding)
    builder.require_source_checkpoint_unchanged(ROOT, context["checkpoint"], context["protected"])
    for row in context["files"]:
        builder.require_clean_path(ROOT, row["path"])
        require_identity(identity(ROOT / row["path"]), row, row["path"])


def capture_identity(row):
    root = row["receipt"]["lifecycle"]["root_identity"]
    return root["pid"], root["creation_filetime_100ns"]


def check_captures(rows, expected_count, mutex=None):
    require(isinstance(rows, list) and len(rows) == expected_count,
            "captured launch count differs from actual instrumentation/build")
    seen, processes, private_hashes = set(), set(), set()
    prior = None
    if mutex is not None:
        acquired = public_capture_time(mutex["acquired_utc"])
        # Existing mutex timestamps have whole-second precision.
        from datetime import timedelta
        released = public_capture_time(mutex["released_utc"]) + timedelta(seconds=1)
        prior = acquired
    for row in rows:
        require(isinstance(row, dict) and isinstance(row.get("raw_text"), str), "capture raw bytes missing")
        path = safe_path(row.get("path"))
        require(re.fullmatch(r"tex-process-tree/launch-[0-9]{6}\.json", path) is not None
                and path not in seen, "capture path reused/invalid")
        seen.add(path)
        raw = row["raw_text"].encode("utf-8")
        require_identity({"bytes": len(raw), "sha256": sha256(raw)}, row, path)
        parsed = builder.strict_json_loads(row["raw_text"], "captured tree")
        require(parsed == row.get("receipt"), "capture parsed/raw mismatch")
        validate_public_capture_receipt(parsed)
        require(raw == canonical_public_capture_bytes(parsed), "public capture encoding is not canonical")
        process, private_hash = capture_identity(row), parsed["provenance"]["private_capture"]["sha256"]
        require(process not in processes and private_hash not in private_hashes, "captured invocation reused")
        processes.add(process)
        private_hashes.add(private_hash)
        if mutex is not None:
            start = public_capture_time(parsed["lifecycle"]["started_utc"])
            finish = public_capture_time(parsed["lifecycle"]["finished_utc"])
            require(prior <= start <= finish < released, "captured invocation outside owning mutex interval")
            prior = finish


def load_build(path):
    build = load_json(path)
    require(build.get("schema") == "unofficial-ai-integrated-stacks-fixed-point-build/v1"
            and build.get("status") == "PASS", "passing full fixed-point build required")
    source = build.get("source", {})
    require(source.get("commit") == git("rev-parse", "HEAD")
            and source.get("tree") == git("rev-parse", "HEAD^{tree}"), "build is not this exact HEAD")
    binding, profile, affected = builder.load_composition_receipt(ROOT, Path("validation/composition-current.json"))
    require(binding == build.get("composition") and binding.get("schema") == DIRECT_SCHEMA,
            "build direct-composition binding differs from current verified composition")
    require(binding.get("new_overlay_ids") == [OVERLAY]
            and binding.get("composition_base_commit") == ADMISSION
            and binding.get("composition_source_commit") == COMPOSED
            and binding.get("authority_commit") == OFFICIAL_BASELINE
            and tuple(affected) == STEMS, "not the exact R48 source transition")
    require(len(profile) == len(set(profile)) == 36 and all(stem in profile for stem in STEMS),
            "R48 requires the complete 36-chapter profile")
    state = build.get("build", {})
    require(state.get("stems") == list(profile) and state.get("chapter_count") == 36
            and state.get("pdfinfo_readable") == 36
            and type(state.get("global_fixed_point_sweep")) is int
            and state["global_fixed_point_sweep"] > 0
            and state.get("fixed_point_suffixes") == list(builder.FIXED_POINT_SUFFIXES),
            "incomplete fixed-point build")
    errors = []
    validate_machine_wide_tex_mutex(state.get("machine_wide_tex_mutex"), "R48 build", errors)
    require(not errors, "; ".join(errors))
    captures = build.get("tex_process_tree", {})
    check_captures(captures.get("launches"), 36 * (2 + state["global_fixed_point_sweep"]) + 2,
                   state["machine_wide_tex_mutex"])
    require(captures.get("launch_count") == len(captures["launches"]), "build capture count mismatch")
    checkpoint, _, protected = builder.load_source_checkpoint(
        ROOT, Path(builder.EGA_SOURCE_CHECKPOINT_PATH), Path("validation/composition-current.json"), binding)
    require(checkpoint == build.get("source_checkpoint"), "build protected checkpoint binding differs")
    artifacts = build.get("artifacts")
    require(isinstance(artifacts, list) and [row.get("stem") for row in artifacts] == list(profile),
            "artifact profile/order mismatch")
    by_stem = {row["stem"]: row for row in artifacts}
    for stem, row in by_stem.items():
        require(type(row.get("pages")) is int and row["pages"] > 0
                and type(row.get("bytes")) is int and row["bytes"] > 0
                and re.fullmatch(r"[0-9A-F]{64}", str(row.get("sha256"))) is not None,
                f"invalid PDF identity: {stem}")
        require_identity(identity(ROOT / (stem + ".pdf")), row, stem)
    revision = source["commit"]
    builder_id = builder.committed_file_identity(ROOT, revision, "tools/build_fixed_point.py")
    require(build.get("builder") == {key: builder_id[key] for key in ("path", "git_blob", "sha256")},
            "build builder identity differs")
    guard_id = builder.committed_file_identity(ROOT, revision, "tools/tex_process_guard.py")
    require(captures.get("guard") == guard_id, "build capture guard identity differs")
    paths = {row["path"] for row in protected if row["role"] not in builder.EGA_NON_WORKTREE_PROTECTED_ROLES}
    paths.update(TOOL_PATHS)
    paths.update(("tools/build_fixed_point.py", "tools/compose_overlay_projection.py",
                  "tools/verify_overlay_projection.py", "tools/validate_unified_repository.py"))
    context = {"build": build, "binding": binding, "checkpoint": checkpoint, "protected": protected,
               "files": [frozen_file(path, revision) for path in sorted(paths)]}
    recheck_inputs(context)
    return build, by_stem, context


def manifest_bound(manifest, relative, raw):
    matches = []
    def visit(value):
        if isinstance(value, dict):
            if value.get("path") == relative:
                matches.append(value)
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)
    visit(manifest)
    require(matches and all(row.get("bytes") == len(raw)
                            and row.get("sha256", "").upper() == sha256(raw) for row in matches),
            f"reference is not exactly manifest-bound: {relative}")


def frozen_operations(revision):
    registry_path = "ai-integrated/registry/overlays.json"
    registry = builder.strict_json_loads(git_blob(revision, registry_path).decode(), "registry")
    entries = [row for row in registry["registered_entries"] if row.get("id") == OVERLAY]
    require(len(entries) == 1, "R48 admission not unique")
    entry = entries[0]
    raw = git_blob(revision, PREFIX + "candidate.manifest.json")
    require(sha256(raw) == MANIFEST_SHA256 == entry["manifest_sha256"].upper(), "R48 manifest mismatch")
    manifest = builder.strict_json_loads(raw.decode(), "R48 manifest")
    require(manifest.get("candidate_id") == OVERLAY, "R48 candidate identity mismatch")
    inputs = [frozen_file(registry_path, revision), frozen_file(PREFIX + "candidate.manifest.json", revision)]
    def bound(relative):
        raw = git_blob(revision, PREFIX + safe_path(relative))
        manifest_bound(manifest, relative, raw)
        inputs.append(frozen_file(PREFIX + relative, revision))
        return raw
    source_map = bound("source-map.jsonl")
    rows = [builder.strict_json_loads(line, "R48 source map") for line in source_map.decode().splitlines() if line.strip()]
    ids = entry["stable_ids"].split() if isinstance(entry["stable_ids"], str) else entry["stable_ids"]
    require([row["unit_id"] for row in rows] == ids and len(ids) == len(set(ids)) == 24,
            "R48 stable-ID inventory mismatch")
    specification = builder.strict_json_loads(bound("operation-spec.json").decode(), "R48 operations")
    authorities, grouped, payloads, seen = {}, defaultdict(list), {}, set()
    for row in rows:
        source = row["source"]
        require(source in {stem + ".tex" for stem in STEMS}, "unexpected R48 source")
        authority = bound(row["authority"])
        require(authority == git_blob(OFFICIAL_BASELINE, source)
                and sha256(authority) == row["authority_sha256"].upper(), "authority is not official source")
        require(source not in authorities or authorities[source] == authority, "authority disagreement")
        authorities[source] = authority
        payload = bound(row["payload"])
        require(source not in payloads or payloads[source] == payload, "payload disagreement")
        payloads[source] = payload
        for operation in row["operations"]:
            require(operation["operation_id"] not in seen and operation["stable_id"] == row["unit_id"]
                    and operation["source"] == source, "operation identity/source mismatch")
            seen.add(operation["operation_id"])
            grouped[source].append(operation)
    flattened = {op["operation_id"]: op for ops in grouped.values() for op in ops}
    spec_ops = specification.get("operations", [])
    require(len(spec_ops) == OPERATION_COUNT and len({op["operation_id"] for op in spec_ops}) == OPERATION_COUNT
            and {op["operation_id"]: op for op in spec_ops} == flattened, "specification/source-map operation mismatch")
    require(len(seen) == OPERATION_COUNT and set(grouped) == {stem + ".tex" for stem in STEMS}, "R48 scope not closed")
    for source, operations in grouped.items():
        require(len(operations) == EXPECTED_APPLIED[Path(source).stem]
                and apply_operations(authorities[source], operations) == payloads[source], "isolated replay mismatch")
        grouped[source] = [{**op, "round": 48} for op in operations]
    return authorities, grouped, list({row["path"]: row for row in inputs}.values())


def cumulative_operations(authority, before, after, operations, source):
    preapplied, semantic = [], []
    rebased = rebase_operations(authority, before, operations, preapplied, {}, semantic, ADMISSION)
    require(not preapplied and not semantic and len(rebased) == EXPECTED_APPLIED[Path(source).stem]
            and apply_operations(before, rebased) == after, f"cumulative replay mismatch: {source}")
    return rebased


def fixed_snapshot(root, stem):
    return {stem + suffix: identity(root / (stem + suffix))
            for suffix in builder.FIXED_POINT_SUFFIXES if (root / (stem + suffix)).is_file()}


def recheck_generated(sources, expected_profile):
    for row in sources.values():
        for kind in ("pdf", "synctex"):
            bound = row[kind]
            require_identity(identity(ROOT / safe_path(bound["path"])), bound, bound["path"])
    require({stem: fixed_snapshot(ROOT, stem) for stem in expected_profile} == expected_profile,
            "full-profile fixed-point artifact changed during mapping")


def validate_capture_window(mutex, rows):
    acquired = int(datetime.fromisoformat(mutex["acquired_utc"].replace("Z", "+00:00")).timestamp()) * 1_000_000_000
    released = (int(datetime.fromisoformat(mutex["released_utc"].replace("Z", "+00:00")).timestamp()) + 1) * 1_000_000_000
    prior = acquired
    for row in rows:
        times = [row.get(key) for key in ("started_ns", "synctex_mtime_ns", "completed_ns")]
        require(all(type(value) is int for value in times) and prior <= times[0] <= times[1] <= times[2] < released,
                "instrumentation is not sequential inside the recorded mutex window")
        prior = times[2]


def check_instrumentation(path, build_path, build, artifacts, context):
    receipt = load_json(path)
    require(receipt.get("schema") == INSTRUMENTATION_SCHEMA and receipt.get("status") == "PASS"
            and receipt.get("source") == build["source"], "invalid instrumentation identity")
    require(receipt.get("build_receipt") == {"path": relative_path(build_path), **identity(build_path)},
            "instrumentation build binding differs")
    require(receipt.get("frozen_inputs") == context["files"], "instrumentation protected files differ")
    require(receipt.get("environment") == {"SOURCE_DATE_EPOCH": build["environment"]["source_date_epoch"],
            "FORCE_SOURCE_DATE": "1", "TZ": "UTC"}, "instrumentation environment differs")
    errors = []
    validate_machine_wide_tex_mutex(receipt.get("machine_wide_tex_mutex"), "R48 instrumentation", errors)
    require(not errors, "; ".join(errors))
    rows = receipt.get("artifacts")
    require(isinstance(rows, list) and [row.get("stem") for row in rows] == list(STEMS), "incorrect instrumentation stems")
    validate_capture_window(receipt["machine_wide_tex_mutex"], rows)
    captures = receipt.get("tex_process_tree", {})
    check_captures(captures.get("launches"), len(STEMS), receipt["machine_wide_tex_mutex"])
    require(captures.get("launch_count") == len(STEMS), "instrumentation capture count differs")
    require(not ({capture_identity(row) for row in captures["launches"]}
                 & {capture_identity(row) for row in build["tex_process_tree"]["launches"]}),
            "instrumentation reused a build process capture")
    require(captures.get("guard") == builder.committed_file_identity(ROOT, build["source"]["commit"], "tools/tex_process_guard.py"),
            "instrumentation guard differs")
    expected_all = {stem: fixed_snapshot(ROOT, stem) for stem in build["build"]["stems"]}
    require(receipt.get("full_profile_artifacts_before") == expected_all == receipt.get("full_profile_artifacts_after"),
            "full-profile fixed-point identity changed during/after instrumentation")
    require(receipt.get("tooling") == [{"path": p, **identity(ROOT / p)} for p in TOOL_PATHS], "instrumentation tool drift")
    for row, capture in zip(rows, captures["launches"]):
        stem = row["stem"]
        require(row.get("command") == tex_command(stem) and row.get("capture") == capture
                and row.get("exit_code") == 0 and row.get("sidecar_absent_before") is True
                and row.get("synctex_regenerated") is True
                and row.get("tex_mutex_owned_through_immediate_checks") is True, "invalid guarded instrumentation")
        lifecycle = capture["receipt"]["lifecycle"]
        start_ns = int(public_capture_time(lifecycle["started_utc"]).timestamp() * 1_000_000_000)
        finish_ns = int(public_capture_time(lifecycle["finished_utc"]).timestamp() * 1_000_000_000)
        require(row["started_ns"] - 1000 <= start_ns <= finish_ns <= row["completed_ns"] + 1000,
                "process capture is not within its instrumentation row (microsecond timestamp precision)")
        require(row.get("diagnostics") == artifacts[stem]["diagnostics"]
                and row.get("external_references") == artifacts[stem]["external_references"], "instrumentation diagnostics differ")
        require(row.get("fixed_point_artifacts_before") == expected_all[stem] == row.get("fixed_point_artifacts_after"),
                "instrumented fixed-point identity changed")
        require_identity(row.get("pdf_before"), artifacts[stem], stem)
        require_identity(row.get("pdf_after"), artifacts[stem], stem)
        require_identity(identity(ROOT / (stem + ".synctex.gz")), row["synctex"], stem)
    return receipt


def tex_command(stem):
    require(stem in STEMS, "unplanned instrumentation stem")
    return ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-synctex=1", stem + ".tex"]


def synctex_pages(root, source, line):
    result = subprocess.run(["synctex", "view", "-i", f"{line}:0:{(root / source).resolve()}",
                             "-o", str(root / (Path(source).stem + ".pdf"))], cwd=root,
                            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
    pages = sorted({int(page) for page in re.findall(r"^Page:(\d+)\s*$", result.stdout, re.MULTILINE)})
    require(result.returncode == 0 and pages, f"SyncTeX lookup failed: {source}:{line}")
    return pages


def mapped_operation(row, rebased, final, root, source, page_count, cache):
    start = row["start_byte"] + sum(len(other["replacement_text"].encode()) - len(other["old_text"].encode())
                                  for other in rebased if other["start_byte"] < row["start_byte"])
    replacement = row["replacement_text"].encode()
    require(0 <= start <= len(final) and final[start:start + len(replacement)] == replacement,
            "final replacement byte interval differs")
    texts = final.decode().splitlines()
    require(texts, "cannot map empty source")
    deletion = {}
    if replacement:
        first = final.count(b"\n", 0, start) + 1
        last = final.count(b"\n", 0, start + len(replacement) - 1) + 1
    else:
        line = min(len(texts), final.count(b"\n", 0, start) + 1)
        first, last = max(1, line - 1), min(len(texts), line + 1)
        physical = final.splitlines(keepends=True)
        left, right = sum(map(len, physical[:first - 1])), sum(map(len, physical[:last]))
        context, old = final[left:right], row["old_text"].encode()
        require(old and context, "deletion lacks a surviving locator")
        deletion = {"deletion": True, "deleted_text": row["old_text"], "deleted_bytes": len(old),
                    "deleted_sha256": sha256(old), "deletion_context": {"start_byte": left,
                    "end_byte_exclusive": right, "text": context.decode(), "bytes": len(context), "sha256": sha256(context)}}
    records = []
    for line in range(first, last + 1):
        if line not in cache:
            cache[line] = synctex_pages(root, source, line)
        require(cache[line] and all(type(page) is int and 1 <= page <= page_count for page in cache[line]),
                "mapped page outside PDF")
        records.append({"line": line, "text": texts[line - 1], "pages": cache[line]})
    return {"round": 48, "operation_id": row["operation_id"], "stable_id": row["stable_id"],
            "disposition": "applied_byte_edit", "authority_start_byte": row["authority_start_byte"],
            "authority_start_line": row["source_start_line"], "final_start_byte": start,
            "final_end_byte_exclusive": start + len(replacement), "final_cumulative_line": first,
            "final_end_line": last, "replacement_text": row["replacement_text"],
            "replacement_bytes": len(replacement), "replacement_sha256": sha256(replacement),
            "final_source_lines": records, "pages": sorted({p for record in records for p in record["pages"]}), **deletion}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT)
    parser.add_argument("--build-receipt", type=Path, required=True)
    parser.add_argument("--synctex-receipt", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    configure_source(args.source)
    resolve = lambda p: p.resolve() if p.is_absolute() else (ROOT / p).resolve()
    build_path, instrument_path, output = map(resolve, (args.build_receipt, args.synctex_receipt, args.output))
    require(not output.exists() and output.parent == ROOT / "validation", "invalid or existing output")
    build_id, instrument_id = identity(build_path), identity(instrument_path)
    build, artifacts, context = load_build(build_path)
    instrumentation = check_instrumentation(instrument_path, build_path, build, artifacts, context)
    authorities, grouped, files = frozen_operations(build["source"]["commit"])
    sources = {}
    for stem in STEMS:
        source = stem + ".tex"
        before, final = git_blob(ADMISSION, source), git_blob(COMPOSED, source)
        require(final == (ROOT / source).read_bytes() == git_blob(build["source"]["commit"], source), "cumulative source drift")
        rebased = cumulative_operations(authorities[source], before, final, grouped[source], source)
        pdf, sidecar = ROOT / (stem + ".pdf"), ROOT / (stem + ".synctex.gz")
        pdf_id, sidecar_id, cache = identity(pdf), identity(sidecar), {}
        mapped = [mapped_operation(op, rebased, final, ROOT, source, artifacts[stem]["pages"], cache)
                  for op in sorted(rebased, key=lambda row: row["start_byte"])]
        require(identity(pdf) == pdf_id and identity(sidecar) == sidecar_id, "PDF/SyncTeX changed during mapping")
        pages = sorted({page for op in mapped for page in op["pages"]})
        sources[source] = {"authority_bytes": len(authorities[source]), "authority_sha256": sha256(authorities[source]),
            "composed_bytes": len(final), "composed_sha256": sha256(final),
            "composed_git_blob": git("rev-parse", f"{COMPOSED}:{source}"), "operation_count": len(mapped),
            "operations": mapped, "byte_edit_pages": pages, "unique_pages": pages,
            "pdf": {"path": relative_path(pdf), **pdf_id, "pages": artifacts[stem]["pages"]},
            "synctex": {"path": relative_path(sidecar), **sidecar_id}, "synctex_query_count": len(cache)}
    recheck_inputs(context)
    for row in files:
        require_identity(identity(ROOT / row["path"]), row, row["path"])
        builder.require_clean_path(ROOT, row["path"])
    require(identity(build_path) == build_id and identity(instrument_path) == instrument_id, "input receipt changed")
    recheck_generated(sources, instrumentation["full_profile_artifacts_after"])
    result = {"schema": "unofficial-ai-integrated-stacks-operation-page-map/v1", "status": "PASS",
        "created_utc": utc_now(), "source": build["source"], "composition_base": ADMISSION,
        "composition_source": COMPOSED, "build_receipt": {"path": relative_path(build_path), **build_id},
        "synctex_instrumentation_receipt": {"path": relative_path(instrument_path), **instrument_id},
        "accepted_operation_count": OPERATION_COUNT, "operation_count": OPERATION_COUNT,
        "historical_noop_operation_count": 0, "mapping_failures": 0,
        "mapping_protocol": {"method": "Exact cumulative rebase; every replacement line queried with SyncTeX; surviving neighbors for deletions",
            "visual_inspection_performed": False, "pdf_and_synctex_byte_identity_preserved": True},
        "sources": sources, "frozen_inputs": context["files"] + files,
        "mapper": {"path": TOOL_PATHS[1], **identity(ROOT / TOOL_PATHS[1]), "committed_at_build_source_required": True}}
    with output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps({"status": "PASS", "output": relative_path(output), **identity(output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
