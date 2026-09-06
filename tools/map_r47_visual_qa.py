#!/usr/bin/env python3
"""Map the 177 admitted R40--R47 edits to fresh cumulative-PDF SyncTeX.

Mapping is not visual inspection. No TeX or rendering is launched here. The
source/manifest/operation bindings and cumulative replay are independently
rechecked before mapping every final line occupied by each replacement.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path, PurePosixPath

if __package__:
    # The preserved composer still uses script-style sibling imports.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from . import build_fixed_point as builder
    from .compose_overlay_projection import apply_operations, rebase_operations
    from .validate_unified_repository import validate_machine_wide_tex_mutex
else:
    import build_fixed_point as builder
    from compose_overlay_projection import apply_operations, rebase_operations
    from validate_unified_repository import validate_machine_wide_tex_mutex

ROOT = Path(__file__).resolve().parents[1]
STEMS = ("descent", "perfect", "topologies", "groupoids", "more-groupoids")
EXPECTED_APPLIED = {"descent": 36, "perfect": 32, "topologies": 36,
                    "groupoids": 46, "more-groupoids": 27}
ROUNDS = tuple(range(40, 48))
OPERATION_COUNT = 177
OFFICIAL_BASELINE = "a04446e57ec1fbc252a871afcec7752fb2807b14"
BUILD_PATH = "validation/stacks-errata-a04446e-r47-build-2026-09-06.json"
INSTRUMENTATION_PATH = "validation/stacks-errata-a04446e-r47-synctex-instrumentation-2026-09-06.json"
PAGE_MAP_PATH = "validation/stacks-errata-a04446e-r47-source-page-map-2026-09-06.json"
INSTRUMENTATION_SCHEMA = "unofficial-ai-integrated-stacks-synctex-instrumentation/v1"
TOOLS = ("tools/build_fixed_point.py", "tools/compose_overlay_projection.py",
         "tools/verify_overlay_projection.py", "tools/validate_unified_repository.py")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def configure_source(source: Path) -> Path:
    global ROOT
    ROOT = source.resolve()
    git_blob.cache_clear()
    require(Path(git("rev-parse", "--show-toplevel")).resolve() == ROOT,
            "source is not an exact Git worktree root")
    return ROOT


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest().upper()


def identity(path: Path) -> dict:
    raw = path.read_bytes()
    return {"bytes": len(raw), "sha256": sha256(raw)}


def load_json(path: Path) -> dict:
    value = builder.strict_json_loads(path.read_text(encoding="utf-8"), path.name)
    require(isinstance(value, dict), f"JSON object required: {path.name}")
    return value


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def relative_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        # Private render/inspection roots must not expose account or agent paths
        # in the public receipt. Exact hashes, not machine paths, bind them.
        return "private-evidence/" + path.name


def safe_path(value: str) -> str:
    require(isinstance(value, str) and bool(value) and "\\" not in value
            and ":" not in value and not PurePosixPath(value).is_absolute()
            and ".." not in PurePosixPath(value).parts
            and PurePosixPath(value).as_posix() == value, "unsafe evidence path")
    return value


def git(*args: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), *args],
                                   stderr=subprocess.PIPE, timeout=120).decode("utf-8").strip()


@lru_cache(maxsize=512)
def git_blob(revision: str, path: str) -> bytes:
    require(re.fullmatch(r"[0-9a-f]{40}", revision) is not None, "full revision required")
    return subprocess.check_output(["git", "-C", str(ROOT), "cat-file", "blob",
                                    f"{revision}:{safe_path(path)}"],
                                   stderr=subprocess.PIPE, timeout=120)


def require_identity(value: object, expected: dict, label: str) -> None:
    require(isinstance(value, dict) and type(value.get("bytes")) is int
            and all(value.get(k) == expected[k] for k in ("bytes", "sha256")),
            f"identity mismatch: {label}")


def frozen_file(path: str, revision: str) -> dict:
    safe_path(path)
    builder.require_clean_path(ROOT, path)
    raw = git_blob(revision, path)
    require((ROOT / path).read_bytes() == raw, f"live input differs from build source: {path}")
    return {"path": path, "bytes": len(raw), "sha256": sha256(raw)}


def build_inputs(build: dict) -> list[dict]:
    revision = build["source"]["commit"]
    root_names = git("ls-tree", "--name-only", revision).splitlines()
    # Root includes/cross-reference providers are inputs too, even when they do
    # not produce one of this checkpoint's 35 PDFs.
    paths = {name for name in root_names if name.endswith(".tex")}
    paths.update(TOOLS)
    paths.update(("my.bib", "tags/tags", "validation/composition-current.json"))
    paths.update(name for name in root_names
                 if Path(name).suffix.lower() in builder.EGA_SHARED_BUILD_SUFFIXES)
    return [frozen_file(path, revision) for path in sorted(paths)]


def recheck_inputs(rows: list[dict]) -> None:
    for row in rows:
        require_identity(identity(ROOT / row["path"]), row, row["path"])
        builder.require_clean_path(ROOT, row["path"])


def load_build(path: Path) -> tuple[dict, dict[str, dict]]:
    build = load_json(path)
    require(build.get("schema") == "unofficial-ai-integrated-stacks-fixed-point-build/v1"
            and build.get("status") == "PASS", "passing fixed-point build required")
    source = build.get("source", {})
    revision = source.get("commit")
    require(isinstance(revision, str) and re.fullmatch(r"[0-9a-f]{40}", revision) is not None,
            "invalid build source commit")
    require(source.get("tree") == git("rev-parse", f"{revision}^{{tree}}"), "build tree mismatch")
    builder.require_ancestor(ROOT, revision, "build source", git("rev-parse", "HEAD"))
    errors: list[str] = []
    state = build.get("build", {})
    validate_machine_wide_tex_mutex(state.get("machine_wide_tex_mutex"), "first build", errors)
    require(not errors, "; ".join(errors))
    composition = build.get("composition", {})
    checkpoint = build.get("source_checkpoint")
    require(isinstance(checkpoint, dict)
            and checkpoint.get("schema") == "unofficial-stacks-project-ai-drafts-ega-source-checkpoint-successor/v1"
            and checkpoint.get("status") == "PASS_SOURCE_CHECKPOINT_SUCCESSOR"
            and checkpoint.get("post_content", {}).get("head_commit") == revision
            and checkpoint.get("post_content", {}).get("head_tree") == source["tree"],
            "R47 build lacks its exact EGA source-checkpoint successor binding")
    required_ids = [f"stacks-errata-a04446e-r{number}" for number in ROUNDS]
    require([row.get("id") for row in composition.get("new_overlays", [])] == required_ids
            and composition.get("affected_source_stems") == list(STEMS)
            and composition.get("authority_commit") == OFFICIAL_BASELINE,
            "build does not bind the exact R40--R47 scope")
    receipt = git_blob(revision, "validation/composition-current.json")
    require(composition.get("receipt") == "validation/composition-current.json"
            and composition.get("receipt_sha256") == sha256(receipt)
            and composition.get("receipt_git_blob") == hashlib.sha1(
                f"blob {len(receipt)}\0".encode() + receipt).hexdigest(), "composition receipt mismatch")
    composed = builder.strict_json_loads(receipt.decode(), "R47 composition")
    require(composed["composition"]["new_operations"] == OPERATION_COUNT
            and composed["composition"]["new_byte_edit_operations"] == OPERATION_COUNT,
            "R47 composition operation count mismatch")
    require(state.get("stems") == composition.get("required_build_stems")
            and len(state.get("stems", [])) == 35
            and state.get("chapter_count") == 35 and state.get("pdfinfo_readable") == 35
            and type(state.get("global_fixed_point_sweep")) is int
            and state["global_fixed_point_sweep"] > 0, "incomplete R47 build profile")
    artifacts = build.get("artifacts")
    require(isinstance(artifacts, list) and [r.get("stem") for r in artifacts] == state["stems"],
            "build artifact order/coverage mismatch")
    by_stem = {r["stem"]: r for r in artifacts}
    require(len(by_stem) == 35, "duplicate build stem")
    for stem, row in by_stem.items():
        require(type(row.get("pages")) is int and row["pages"] > 0
                and type(row.get("bytes")) is int and row["bytes"] > 0
                and re.fullmatch(r"[0-9A-F]{64}", str(row.get("sha256"))) is not None,
                f"invalid artifact identity: {stem}")
    raw_builder = git_blob(revision, "tools/build_fixed_point.py")
    require(build.get("builder") == {"path": "tools/build_fixed_point.py",
            "git_blob": hashlib.sha1(f"blob {len(raw_builder)}\0".encode() + raw_builder).hexdigest(),
            "sha256": sha256(raw_builder)}, "builder identity mismatch")
    build_inputs(build)
    return build, by_stem


def frozen_operations(build: dict) -> tuple[dict[str, bytes], dict[str, list[dict]], list[dict]]:
    revision = build["source"]["commit"]
    registry_path = "ai-integrated/registry/overlays.json"
    inputs = [frozen_file(registry_path, revision)]
    registry = json.loads(git_blob(revision, registry_path))["registered_entries"]
    indexed = {row["id"]: (index, row) for index, row in enumerate(registry)}
    require(len(indexed) == len(registry), "duplicate registry ID")
    authorities, grouped, seen = {}, defaultdict(list), set()
    prior = -1
    for number in ROUNDS:
        overlay_id = f"stacks-errata-a04446e-r{number}"
        position, entry = indexed[overlay_id]
        require(position > prior, "R47 overlay order differs from registry")
        prior = position
        prefix = f"ai-integrated/candidates/commons/stacks/errata/r{number}/"
        manifest_path = prefix + "candidate.manifest.json"
        manifest_raw = git_blob(revision, manifest_path)
        require(sha256(manifest_raw) == entry["manifest_sha256"].upper(), "admission manifest mismatch")
        manifest = json.loads(manifest_raw)
        inputs.append(frozen_file(manifest_path, revision))
        source_map_path = prefix + "source-map.jsonl"
        source_map_raw = git_blob(revision, source_map_path)
        # The source map must be one of the manifest's exact hash-bound inputs.
        def bound(value):
            if isinstance(value, dict):
                if value.get("path") == "source-map.jsonl" and value.get("sha256", "").upper() == sha256(source_map_raw):
                    return True
                return any(bound(item) for item in value.values())
            return isinstance(value, list) and any(bound(item) for item in value)
        require(bound(manifest), f"source map is not manifest-bound: {overlay_id}")
        inputs.append(frozen_file(source_map_path, revision))
        rows = [json.loads(line) for line in source_map_raw.decode().splitlines()]
        stable_ids = entry["stable_ids"]
        if isinstance(stable_ids, str):
            stable_ids = stable_ids.split()
        require([row["unit_id"] for row in rows] == stable_ids, "admitted stable-ID order mismatch")
        per_source = defaultdict(list)
        payloads = {}
        for row in rows:
            source = row["source"]
            require(source in {f"{stem}.tex" for stem in STEMS}, "unplanned affected source")
            authority_path, payload_path = prefix + safe_path(row["authority"]), prefix + safe_path(row["payload"])
            authority = git_blob(revision, authority_path)
            require(sha256(authority) == row["authority_sha256"].upper()
                    and authority == git_blob(OFFICIAL_BASELINE, source), "official authority mismatch")
            require(source not in authorities or authorities[source] == authority, "authority drift")
            authorities[source] = authority
            require(source not in payloads or payloads[source] == payload_path, "ambiguous isolated payload")
            payloads[source] = payload_path
            for operation in row["operations"]:
                op_id = operation["operation_id"]
                require(op_id not in seen and operation["source"] == source
                        and operation["stable_id"] == row["unit_id"], "operation identity/source mismatch")
                seen.add(op_id)
                enriched = {**operation, "round": number}
                grouped[source].append(enriched)
                per_source[source].append(enriched)
        for source, operations in per_source.items():
            require(apply_operations(authorities[source], operations) == git_blob(revision, payloads[source]),
                    f"isolated payload replay mismatch: {overlay_id}/{source}")
    require(len(seen) == OPERATION_COUNT and set(grouped) == {f"{s}.tex" for s in STEMS},
            "R47 operation inventory is not closed")
    for stem in STEMS:
        require(len(grouped[f"{stem}.tex"]) == EXPECTED_APPLIED[stem], "per-source operation count mismatch")
    return authorities, grouped, inputs


def cumulative_operations(authority: bytes, before: bytes, after: bytes,
                          operations: list[dict], source: str, base: str) -> list[dict]:
    preapplied, semantic = [], []
    rebased = rebase_operations(authority, before, operations, preapplied, {}, semantic, base)
    require(not preapplied and not semantic and len(rebased) == EXPECTED_APPLIED[Path(source).stem]
            and apply_operations(before, rebased) == after, f"cumulative replay mismatch: {source}")
    return rebased


def fixed_snapshot(root: Path, stem: str) -> dict:
    return {stem + suffix: identity(root / (stem + suffix))
            for suffix in builder.FIXED_POINT_SUFFIXES if (root / (stem + suffix)).is_file()}


def validate_capture_window(mutex: dict, rows: list[dict]) -> None:
    acquired = int(datetime.fromisoformat(mutex["acquired_utc"].replace("Z", "+00:00")).timestamp()) * 1_000_000_000
    # Mutex timestamps are emitted at whole-second precision. Do not claim a
    # stricter time measurement than the producer recorded.
    released = (int(datetime.fromisoformat(mutex["released_utc"].replace("Z", "+00:00")).timestamp()) + 1) * 1_000_000_000
    prior = acquired
    for row in rows:
        times = [row.get(key) for key in ("started_ns", "synctex_mtime_ns", "completed_ns")]
        require(all(type(value) is int for value in times)
                and prior <= times[0] <= times[1] <= times[2] < released,
                "captured SyncTeX runs are not sequential within the one recorded mutex window")
        prior = times[2]


def check_instrumentation(path: Path, build_path: Path, build: dict,
                          artifacts: dict, synctex_root: Path) -> dict:
    receipt = load_json(path)
    require(receipt.get("schema") == INSTRUMENTATION_SCHEMA and receipt.get("status") == "PASS"
            and receipt.get("source") == build["source"], "invalid instrumentation source")
    require(receipt.get("build_receipt") == {"path": relative_path(build_path), **identity(build_path)},
            "instrumentation build binding mismatch")
    require(receipt.get("environment") == {"SOURCE_DATE_EPOCH": build["environment"]["source_date_epoch"],
            "FORCE_SOURCE_DATE": "1", "TZ": "UTC"}, "instrumentation environment mismatch")
    errors = []
    validate_machine_wide_tex_mutex(receipt.get("machine_wide_tex_mutex"), "instrumentation", errors)
    require(not errors, "; ".join(errors))
    rows = receipt.get("artifacts")
    require(isinstance(rows, list) and [row.get("stem") for row in rows] == list(STEMS),
            "instrumentation must contain exactly the five R47 stems")
    validate_capture_window(receipt["machine_wide_tex_mutex"], rows)
    tools = receipt.get("tooling")
    expected_tools = [
        {"path": "tools/instrument_r47_synctex.py", **identity(Path(__file__).with_name("instrument_r47_synctex.py"))},
        {"path": "tools/map_r47_visual_qa.py", **identity(Path(__file__))},
    ]
    require(tools == expected_tools, "instrumentation tooling identity changed")
    for row in rows:
        stem = row["stem"]
        require(row.get("command") == ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                "-file-line-error", "-synctex=1", f"{stem}.tex"]
                and row.get("exit_code") == 0 and row.get("synctex_regenerated") is True
                and row.get("sidecar_absent_before") is True, "invalid instrumentation execution")
        require(row.get("tex_mutex_owned_through_immediate_checks") is True
                and row.get("diagnostics") == artifacts[stem].get("diagnostics")
                and row.get("external_references") == artifacts[stem].get("external_references"),
                "instrumentation immediate-check evidence mismatch")
        times = [row.get(key) for key in ("started_ns", "synctex_mtime_ns", "completed_ns")]
        require(all(type(value) is int for value in times) and 0 < times[0] <= times[1] <= times[2],
                "SyncTeX freshness is not proved")
        before, after = row.get("fixed_point_artifacts_before"), row.get("fixed_point_artifacts_after")
        require(isinstance(before, dict) and f"{stem}.aux" in before
                and f"{stem}.pdf" in before and before == after == fixed_snapshot(synctex_root, stem),
                "fixed-point instrumentation byte inventory differs")
        require_identity(row.get("pdf_before"), artifacts[stem], stem)
        require_identity(row.get("pdf_after"), artifacts[stem], stem)
        require_identity(identity(synctex_root / f"{stem}.pdf"), artifacts[stem], stem)
        require_identity(row.get("synctex"), identity(synctex_root / f"{stem}.synctex.gz"), stem)
    return receipt


def synctex_pages(root: Path, source: str, line: int) -> list[int]:
    result = subprocess.run(["synctex", "view", "-i", f"{line}:0:{(root / source).resolve()}",
                             "-o", str(root / f"{Path(source).stem}.pdf")], cwd=root,
                            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
    pages = sorted({int(p) for p in re.findall(r"^Page:(\d+)\s*$", result.stdout, re.MULTILINE)})
    require(result.returncode == 0 and bool(pages), f"SyncTeX lookup failed: {source}:{line}")
    return pages


def mapped_operation(row: dict, rebased: list[dict], final: bytes, root: Path,
                     source: str, page_count: int, cache: dict) -> dict:
    start = row["start_byte"] + sum(len(other["replacement_text"].encode()) - len(other["old_text"].encode())
                                   for other in rebased if other["start_byte"] < row["start_byte"])
    replacement = row["replacement_text"].encode()
    require(0 <= start <= len(final) and final[start:start + len(replacement)] == replacement,
            "final mapped replacement is incorrect")
    texts, records, deletion = final.decode().splitlines(), [], {}
    require(bool(texts), "cannot map an empty cumulative source")
    if replacement:
        first, last = final.count(b"\n", 0, start) + 1, final.count(b"\n", 0, start + len(replacement) - 1) + 1
    else:
        # A deletion has no output glyph. Bind the exact surviving lines on both
        # sides of its final byte position, rather than silently dropping it or
        # pretending an empty interval was a visible replacement.
        line = min(len(texts), final.count(b"\n", 0, start) + 1)
        first, last = max(1, line - 1), min(len(texts), line + 1)
        physical = final.splitlines(keepends=True)
        context_start = sum(map(len, physical[:first - 1]))
        context_end = sum(map(len, physical[:last]))
        context = final[context_start:context_end]
        old = row["old_text"].encode()
        require(bool(old) and bool(context), "deletion requires an old preimage and surviving context")
        deletion = {"deletion": True, "deleted_text": row["old_text"],
                    "deleted_bytes": len(old), "deleted_sha256": sha256(old),
                    "deletion_context": {"start_byte": context_start, "end_byte_exclusive": context_end,
                        "text": context.decode(), "bytes": len(context), "sha256": sha256(context)}}
    for line in range(first, last + 1):
        if line not in cache:
            cache[line] = synctex_pages(root, source, line)
        require(all(type(p) is int and 1 <= p <= page_count for p in cache[line]) and cache[line],
                "mapped page outside PDF")
        records.append({"line": line, "text": texts[line - 1], "pages": cache[line]})
    return {"round": row["round"], "operation_id": row["operation_id"], "stable_id": row["stable_id"],
            "disposition": "applied_byte_edit", "authority_start_byte": row["authority_start_byte"],
            "authority_start_line": row["source_start_line"], "final_start_byte": start,
            "final_end_byte_exclusive": start + len(replacement), "final_cumulative_line": first,
            "final_end_line": last, "replacement_text": row["replacement_text"],
            "replacement_bytes": len(replacement), "replacement_sha256": sha256(replacement),
            "final_source_lines": records, "pages": sorted({p for r in records for p in r["pages"]}),
            **deletion}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT)
    parser.add_argument("--build-receipt", type=Path, default=Path(BUILD_PATH))
    parser.add_argument("--synctex-root", type=Path)
    parser.add_argument("--synctex-receipt", type=Path, default=Path(INSTRUMENTATION_PATH))
    parser.add_argument("--output", type=Path, default=Path(PAGE_MAP_PATH))
    args = parser.parse_args(argv)
    configure_source(args.source)
    resolve = lambda p: p.resolve() if p.is_absolute() else (ROOT / p).resolve()
    output, build_path, instrument_path = map(resolve, (args.output, args.build_receipt, args.synctex_receipt))
    synctex_root = resolve(args.synctex_root) if args.synctex_root else ROOT
    require(synctex_root == ROOT, "SyncTeX must belong to the configured first-build source worktree")
    require(not output.exists() and output.parent == ROOT / "validation", "invalid or existing map output")
    build_identity, instrument_identity = identity(build_path), identity(instrument_path)
    build, artifacts = load_build(build_path)
    check_instrumentation(instrument_path, build_path, build, artifacts, synctex_root)
    authorities, grouped, inputs = frozen_operations(build)
    inputs += build_inputs(build)
    mapper_identity = identity(Path(__file__))
    base, composed = (build["composition"][key] for key in ("composition_base_commit", "composition_source_commit"))
    sources = {}
    for stem in STEMS:
        source = f"{stem}.tex"
        before, final = git_blob(base, source), git_blob(composed, source)
        require(final == git_blob(build["source"]["commit"], source)
                and (synctex_root / source).read_bytes() == final, "cumulative source drift")
        rebased = cumulative_operations(authorities[source], before, final, grouped[source], source, base)
        pdf, sidecar = synctex_root / f"{stem}.pdf", synctex_root / f"{stem}.synctex.gz"
        pdf_id, sidecar_id = identity(pdf), identity(sidecar)
        cache = {}
        mapped = [mapped_operation(row, rebased, final, synctex_root, source, artifacts[stem]["pages"], cache)
                  for row in sorted(rebased, key=lambda item: item["start_byte"])]
        require(identity(pdf) == pdf_id and identity(sidecar) == sidecar_id, "mapped PDF/SyncTeX changed")
        pages = sorted({page for row in mapped for page in row["pages"]})
        sources[source] = {"authority_bytes": len(authorities[source]), "authority_sha256": sha256(authorities[source]),
            "composed_bytes": len(final), "composed_sha256": sha256(final),
            "composed_git_blob": git("rev-parse", f"{composed}:{source}"), "operation_count": len(mapped),
            "operations": mapped, "historical_noop_evidence": [], "historical_noop_pages": [],
            "byte_edit_pages": pages, "unique_pages": pages,
            "pdf": {"path": relative_path(pdf), **pdf_id, "pages": artifacts[stem]["pages"]},
            "synctex": {"path": relative_path(sidecar), **sidecar_id}, "synctex_query_count": len(cache),
            "pdf_and_synctex_identity_preserved": True}
    recheck_inputs(inputs)
    require(identity(build_path) == build_identity and identity(instrument_path) == instrument_identity,
            "build/instrumentation receipt changed during mapping")
    require(identity(Path(__file__)) == mapper_identity, "mapper changed during mapping")
    result = {"schema": "unofficial-ai-integrated-stacks-operation-page-map/v1", "status": "PASS",
        "created_utc": utc_now(), "source": build["source"], "composition_base": base,
        "composition_source": composed, "build_receipt": {"path": relative_path(build_path), **build_identity},
        "synctex_instrumentation_receipt": {"path": relative_path(instrument_path), **instrument_identity},
        "accepted_operation_count": OPERATION_COUNT, "operation_count": OPERATION_COUNT,
        "historical_noop_operation_count": 0, "mapping_failures": 0,
        "mapping_protocol": {"method": "SyncTeX of every final replacement line; exact surviving neighboring lines for zero-length deletions",
            "visual_inspection_performed": False, "pdf_and_synctex_byte_identity_preserved": True},
        "sources": sources, "frozen_inputs": inputs,
        "mapper": {"path": "tools/map_r47_visual_qa.py", **mapper_identity,
                   "committed_at_build_source_required": False}}
    with output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps({"status": "PASS", "output": relative_path(output), **identity(output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
