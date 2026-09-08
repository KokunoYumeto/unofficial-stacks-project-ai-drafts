#!/usr/bin/env python3
"""Bind the exact 26-step R40-R47 import and 177-operation composition."""

from __future__ import annotations

import argparse
from functools import cache
import hashlib
import json
import sys

from write_r33_composition_receipt import ROOT, blob_bytes, commit_utc, git, identity, run, tree
from write_r39_composition_receipt import exact_commit, parents, path_changes
from build_fixed_point import (
    required_build_profile, validate_bound_leased_candidate,
    validate_import_preparation_topology, validate_registry_metadata_chain,
)


PREVIOUS_PUBLIC = "f73b18165c7162b8386de06cc3c50bd4ced745b6"
PREVIOUS_REGISTRY = "bf472632906dcfbc032620f8ce203fa687e929e5"
REGISTRY_CUTOFF = "e4a7b1cb0b0e7fa4c499ab26cf85275f4f9fed12"
REGISTRY_IMPORT = "396d60f0e4aef8c11c105a24e26c5519386a9f98"
R40_CLARIFICATION = "2911b4cdf5141e1f3a275aeb83ed5cbc9e980bd4"
EXPECTED_SOURCES = {
    "descent.tex": (395297, "91434AA205AA34ED3AD0E4B74590D30C90FA4BB8945105E6E99CCA6805508B69"),
    "perfect.tex": (417517, "31EF572D294E8C79AB31A1AD3A9C8662CE2ACA6E26CF41BD28B541CB2AFA19B7"),
    "topologies.tex": (166236, "FA88114672E734B6B9677C62378691DFFA761D2376026EAE4340CDEFD053A8A9"),
    "groupoids.tex": (205795, "C6CF7E55C1C4F87EC475F514AED7219AF824EC3AC7734319367E54D5F6DFE7A5"),
    "more-groupoids.tex": (121125, "039BA96AEA5ED3BA59A7CB0EECB5D8F7491CCF1C2FCEB49211BA7CECF1C0BDDF"),
}

# Cache only small immutable metadata, never candidate PDFs or the worktree.
parents = cache(parents)
path_changes = cache(path_changes)
identity = cache(identity)
tree = cache(tree)


@cache
def document(commit: str, path: str) -> dict[str, object]:
    value = json.loads(blob_bytes(commit, path))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {commit}:{path}")
    return value


def import_rows(registry_parent: str, registry_commit: str,
                integrated_parent: str, integrated_commit: str) -> list[dict[str, object]]:
    """Compare both raw deltas, then hash each shared immutable blob once."""
    original = path_changes(registry_parent, registry_commit)
    actual = path_changes(integrated_parent, integrated_commit)
    if not original or actual != {f"ai-integrated/{path}": raw for path, raw in original.items()}:
        raise ValueError("import is not an exact prefixed old/new mode-and-blob replay")
    rows = []
    for path, raw in sorted(original.items()):
        if raw[4] not in {"A", "M"} or raw[1] != "100644":
            raise ValueError("unexpected imported deletion or file type")
        data = blob_bytes(registry_commit, path)
        blob = hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()
        if blob != raw[3]:
            raise ValueError("imported Git blob does not match its actual bytes")
        rows.append({"status": raw[4], "source_path": path, "prefixed_path": f"ai-integrated/{path}",
                     "mode": raw[1], "bytes": len(data), "git_blob": blob,
                     "sha256": hashlib.sha256(data).hexdigest().upper()})
    return rows


def linear_range(base: str, head: str, expected_count: int | None = None) -> list[str]:
    commits = git("rev-list", "--reverse", f"{base}..{head}").splitlines()
    if expected_count is not None and len(commits) != expected_count:
        raise ValueError("bound commit range has an unexpected step count")
    parent = base
    for commit in commits:
        if parents(commit) != [parent]:
            raise ValueError("bound commit range is not a single-parent linear chain")
        parent = commit
    if parent != head:
        raise ValueError("bound commit range did not reach its head")
    return commits


def metadata_row(commit: str) -> dict[str, object]:
    parent = parents(commit)
    if len(parent) != 1:
        raise ValueError("registry metadata must have one parent")
    return {"commit": commit, "parent": parent[0], "tree": tree(commit),
            "paths": [{"path": path, **identity(commit, path)}
                      for path in sorted(path_changes(parent[0], commit))]}


def derive_imports() -> tuple[list[dict[str, object]], list[dict[str, object]], list[str]]:
    originals = linear_range(PREVIOUS_REGISTRY, REGISTRY_CUTOFF, 26)
    imports = linear_range(PREVIOUS_PUBLIC, REGISTRY_IMPORT, 26)
    chain, receipts = [], []
    registry_parent, imported_parent = PREVIOUS_REGISTRY, PREVIOUS_PUBLIC
    for original, imported in zip(originals, imports):
        rows = import_rows(registry_parent, original, imported_parent, imported)
        chain.append({"registry_commit": original, "import_commit": imported,
                      "import_tree": tree(imported)})
        receipts.append({"range": f"{registry_parent}..{original}",
                         "registry_commit": original, "import_commit": imported,
                         "import_tree": tree(imported), "parent": imported_parent,
                         "path_count": len(rows), "paths": rows,
                         "transport": "Exact ai-integrated/ prefixed old/new mode-and-blob replay"})
        registry_parent, imported_parent = original, imported
    return chain, receipts, originals


def derive_overlays(originals: list[str], projection: dict[str, object]) -> list[dict[str, object]]:
    final_entries = document(REGISTRY_CUTOFF, "registry/overlays.json")["registered_entries"]
    previous_entries = document(PREVIOUS_REGISTRY, "registry/overlays.json")["registered_entries"]
    if final_entries[:len(previous_entries)] != previous_entries or len(final_entries) != 48:
        raise ValueError("registry does not preserve its exact 40-entry prefix")
    ids = [stable_id for entry in final_entries for stable_id in entry["stable_ids"]]
    if len(ids) != 1292 or len(set(ids)) != 1292:
        raise ValueError("registry stable-ID count or uniqueness mismatch")
    reports = {row["round"]: row for row in projection["overlays"]}
    overlays, admission_cursor = [], PREVIOUS_REGISTRY
    for round_number, entry in zip(range(40, 48), final_entries[-8:]):
        overlay_id = f"stacks-errata-a04446e-r{round_number}"
        if entry.get("id") != overlay_id:
            raise ValueError("new overlays are not exactly R40-R47 in registry order")
        path = f"candidates/{entry['namespace']}"
        admission_candidates = []
        for revision in originals:
            parent = parents(revision)[0]
            changes = path_changes(parent, revision)
            if "registry/overlays.json" not in changes:
                continue
            current = document(revision, "registry/overlays.json")["registered_entries"]
            prior = document(parent, "registry/overlays.json")["registered_entries"]
            if current == prior + [entry]:
                admission_candidates.append(revision)
        if len(admission_candidates) != 1:
            raise ValueError(f"ambiguous admission for {overlay_id}")
        admission = admission_candidates[0]
        candidate = parents(admission)[0]
        manifest = document(candidate, f"{path}/candidate.manifest.json")
        intake_candidates = []
        for revision in originals:
            if "registry/leases.json" not in path_changes(parents(revision)[0], revision):
                continue
            events = document(revision, "registry/leases.json")["events"]
            if events[-1].get("lease_id") == manifest["lease_id"] and events[-1].get("event") == "issued":
                intake_candidates.append(revision)
        if len(intake_candidates) != 1:
            raise ValueError(f"ambiguous lease intake for {overlay_id}")
        intake = intake_candidates[0]
        interludes = linear_range(intake, parents(candidate)[0])
        if interludes != ([R40_CLARIFICATION] if round_number == 41 else []):
            raise ValueError("unexpected candidate intake interlude")
        report = reports[round_number]
        payloads = [{"path": f"payload/{name}", "sha256": row["sha256"]}
                    for name, row in sorted(report["sources"].items())]
        issued = document(intake, "registry/leases.json")["events"][-1]
        released = document(admission, "registry/leases.json")["events"][-1]
        overlay = {
            "id": overlay_id, "stable_ids": report["stable_ids"],
            "operations": sum(row["operations"] for row in report["sources"].values()),
            "manifest_sha256": identity(candidate, f"{path}/candidate.manifest.json")["sha256"],
            "payload_sha256": payloads[0]["sha256"], "payloads": payloads,
            "review_receipt_sha256": identity(candidate, entry["review_receipt"])["sha256"],
            "topology": "leased_candidate_then_admission",
            "lease_binding_schema": "unofficial-ai-integrated-stacks-leased-candidate/v1",
            "intake_commit": intake, "intake_parent": admission_cursor, "intake_tree": tree(intake),
            "intake_successor_commits": [metadata_row(commit) for commit in interludes],
            "candidate_commit": candidate, "candidate_commits": [candidate],
            "candidate_tree": tree(candidate), "candidate_subtree": git("rev-parse", f"{candidate}:{path}"),
            "admission_commit": admission, "admission_parent": candidate, "admission_tree": tree(admission),
            "lease_issue_event": issued["event_id"], "lease_release_event": released["event_id"],
        }
        authority = document(PREVIOUS_PUBLIC, "validation/composition-current.json")["authority"]
        validate_bound_leased_candidate(ROOT, overlay, entry, admission_cursor, REGISTRY_IMPORT, REGISTRY_CUTOFF,
                                         authority["commit"], authority["tree"])
        overlays.append(overlay)
        admission_cursor = admission
    if sum(row["stable_ids"] for row in overlays) != 143 or sum(row["operations"] for row in overlays) != 177:
        raise ValueError("R40-R47 stable-ID or operation counts mismatch")
    if parents(REGISTRY_CUTOFF) != [admission_cursor]:
        raise ValueError("R47 post-admission successor mismatch")
    validate_registry_metadata_chain(ROOT, [metadata_row(REGISTRY_CUTOFF)], admission_cursor,
                                     REGISTRY_IMPORT, REGISTRY_CUTOFF)
    return overlays


def build_receipts(source_commit: str) -> tuple[dict[str, object], dict[str, object]]:
    source_commit = exact_commit(source_commit)
    source_parents = parents(source_commit)
    if len(source_parents) != 1:
        raise ValueError("source composition must have one parent")
    base = source_parents[0]
    chain, imports, originals = derive_imports()
    previous = document(PREVIOUS_PUBLIC, "validation/composition-current.json")
    command = [sys.executable, "tools/compose_overlay_projection.py", "--existing-rounds",
               *map(str, range(18, 40)), "--target-rounds", *map(str, range(18, 48)),
               "--base-revision", base, "--check-revision", source_commit]
    projection = json.loads(run(*command))
    if (projection.get("status") != "PASS" or projection.get("new_operations") != 177
            or projection.get("preapplied_operation_ids") != []
            or projection.get("semantic_dispositions", {}).get("consumed_operation_ids") != []):
        raise ValueError("R40-R47 projection did not apply exactly 177 fresh operations")
    changed = path_changes(base, source_commit)
    affected_names = {name for name, row in projection["sources"].items() if row["new_operations"]}
    if set(changed) != set(EXPECTED_SOURCES) or affected_names != set(EXPECTED_SOURCES):
        raise ValueError("composition source-change inventory mismatch")
    affected = {}
    for path, (size, digest) in EXPECTED_SOURCES.items():
        row = projection["sources"][path]
        after = identity(source_commit, path)
        if (after["bytes"] != size or after["sha256"] != digest
                or row.get("composed_bytes") != size or row.get("composed_sha256") != digest
                or row.get("composed_git_blob") != after["git_blob"]
                or row.get("superseded_operations") != 0
                or row.get("preapplied_operation_ids") != []
                or row.get("semantic_disposition_operation_ids") != []
                or identity(PREVIOUS_PUBLIC, path) != identity(base, path)):
            raise ValueError(f"cumulative source identity or fresh-operation mismatch: {path}")
        affected[path] = {**row,
            "composition_mode": "Exact manifest-bound operations on cumulative source; no preapplied operation or semantic disposition consumed",
            "committed_matches_composition": True,
            "authority_git_blob": git("rev-parse", f"{previous['authority']['commit']}:{path}"), "written": False}
    overlays = derive_overlays(originals, projection)
    preparations = [{"commit": commit, "parent": parents(commit)[0], "tree": tree(commit),
                     "paths": sorted(path_changes(parents(commit)[0], commit))}
                    for commit in linear_range(REGISTRY_IMPORT, base)]
    preservation = dict(previous.get("preservation", {}))
    preservation.update({path: identity(source_commit, path) for path in EXPECTED_SOURCES})
    preservation["r40_r47_state"] = "Eight immutable admissions; 143 stable IDs and 177 fresh byte-edit operations; zero preapplied operations, semantic dispositions, supersessions, or conflicts. R40 clarification and R47 fresh-checkout evidence preserved additively."
    registry = {"cutoff_commit": REGISTRY_CUTOFF, "cutoff_tree": tree(REGISTRY_CUTOFF),
                "post_admission_successor": REGISTRY_CUTOFF,
                "post_admission_metadata_commits": [metadata_row(REGISTRY_CUTOFF)],
                "linear_import_commit": REGISTRY_IMPORT, "linear_import_tree": tree(REGISTRY_IMPORT),
                "linear_import_chain": chain, "preimage_alignment_commits": [],
                "registered_overlays": 48, "registered_stable_ids": 1292,
                "last_admitted_overlay": "stacks-errata-a04446e-r47"}
    for name in ("overlays", "leases"):
        path = f"ai-integrated/registry/{name}.json"
        registry[f"{name}_path"] = path
        registry.update({f"{name}_{key}": value for key, value in identity(REGISTRY_IMPORT, path).items()})
    clarification_path = "registry/admission-receipts/r40-clarification-0001.json"
    receipt = {
        "schema": "unofficial-ai-integrated-stacks-composition/v3", "status": "PASS",
        "created_utc": commit_utc(source_commit), "authority": previous["authority"],
        "previous_cutoff": {"public_main_head": PREVIOUS_PUBLIC, "public_main_tree": tree(PREVIOUS_PUBLIC),
            "registry_commit": PREVIOUS_REGISTRY, "registry_tree": tree(PREVIOUS_REGISTRY),
            "last_admitted_overlay": "stacks-errata-a04446e-r39",
            "source_blobs": {path: identity(PREVIOUS_PUBLIC, path) for path in EXPECTED_SOURCES}},
        "registry": registry, "new_overlays": overlays,
        "composition": {"mode": "manifest-bound registry-order replay rebased onto verified cumulative source",
            "base_commit": base, "base_tree": tree(base), "preparation_commits": preparations,
            "source_commit": source_commit, "source_tree": tree(source_commit),
            "total_v2_operations": previous["composition"]["total_v2_operations"] + 177,
            "new_operations": 177, "new_byte_edit_operations": 177,
            "semantic_dispositions": projection["semantic_dispositions"],
            "r1_r3_replacements": previous["composition"]["r1_r3_replacements"],
            "r1_tag_additions": previous["composition"]["r1_tag_additions"], "affected_sources": affected},
        "preservation": preservation,
        "known_admitted_metadata_defects": [*previous.get("known_admitted_metadata_defects", []), {
            "overlay_id": "stacks-errata-a04446e-r40",
            "defect": "The immutable final-review /source/stable_units_sha256 has one extra trailing C (65 hex characters).",
            "clarification_commit": R40_CLARIFICATION,
            "clarification": {"path": "ai-integrated/" + clarification_path, **identity(R40_CLARIFICATION, clarification_path)},
            "disposition": "Exact append-only registrar clarification verified against the unchanged final review, manifest and stable-units bytes. Use the manifest's effective 64-character binding; preserve the malformed historical assertion."}],
        "projection_verifier": {"path": "tools/compose_overlay_projection.py", "command": " ".join(["python", *command[1:]]), "status": "PASS"},
    }
    receipt["required_build_stems"] = list(required_build_profile(receipt, True))
    topology = validate_import_preparation_topology(ROOT, receipt)
    local = {"schema": "unofficial-ai-integrated-stacks-r47-local-composition/v1", "status": "PASS",
             "created_utc": commit_utc(source_commit), "base": receipt["previous_cutoff"],
             "registry": registry, "imports": imports, "new_overlays": overlays,
             "import_preparation_topology": topology,
             "composition": {"source_commit": source_commit, "source_tree": tree(source_commit),
                 "base_commit": base, "base_tree": tree(base), "existing_rounds": list(range(18, 40)),
                 "target_rounds": list(range(18, 48)), "operation_counts": {"admitted": 177, "applied": 177,
                 "preapplied_or_satisfied": 0, "semantic_dispositions": 0, "superseded": 0, "conflicts": 0},
                 "sources": {path: {"before": identity(PREVIOUS_PUBLIC, path), "after": identity(source_commit, path)}
                             for path in EXPECTED_SOURCES}, "command": receipt["projection_verifier"]["command"]},
             "non_build_validation": {"status": "PASS", "exact_import_steps": 26, "leased_admissions": 8,
                                      "metadata_only_steps": 2, "manifest_closures_checked": 8},
             "build_started": False, "push_performed": False, "publication_performed": False}
    return receipt, local


def verify_or_write_receipts(destinations, *, check_only: bool) -> None:
    """Check the actual saved bytes, or write deterministic newly derived bytes."""
    serialized = {
        path: (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
        for path, value in destinations.items()
    }
    if check_only:
        for path, expected in serialized.items():
            if not path.is_file():
                raise ValueError(f"missing saved composition receipt: {path.name}")
            if path.read_bytes() != expected:
                raise ValueError(f"stale saved composition receipt: {path.name}")
        return
    for path, raw in serialized.items():
        path.write_bytes(raw)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--check-only", action="store_true", help="verify committed evidence without writing receipts")
    args = parser.parse_args()
    receipt, local = build_receipts(args.source_commit)
    destinations = {ROOT / "validation/composition-current.json": receipt,
                    ROOT / "validation/r47-import-composition-receipt.json": local}
    verify_or_write_receipts(destinations, check_only=args.check_only)
    print(json.dumps({"status": "PASS", "written": not args.check_only,
                      "paths": [path.relative_to(ROOT).as_posix() for path in destinations],
                      "registered_overlays": 48, "stable_ids": 1292, "new_operations": 177,
                      "import_steps": 26, "required_build_stems": len(receipt["required_build_stems"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
