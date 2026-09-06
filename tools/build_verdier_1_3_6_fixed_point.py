#!/usr/bin/env python3
"""Build the direct-prefixed Verdier II.1.3.6 release at a PDF fixed point.

This driver is intentionally dedicated to the direct publication chain rooted
at public R39.  It does not consume the historical v4 registered-insertion
topology (whose candidate and registry paths are unprefixed).  One invocation
performs exactly one sequential 30-chapter build while continuously owning the
machine-wide TeX mutex, and emits one sanitized exact-artifact receipt.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any

import build_fixed_point as core


RECEIPT_SCHEMA = "unofficial-ai-integrated-stacks-fixed-point-build/v1"
DIRECT_BINDING_SCHEMA = (
    "unofficial-ai-integrated-stacks-verdier-1-3-6-direct-composition/v1"
)
RELEASE_VALIDATION_SCHEMA = (
    "unofficial-ai-integrated-stacks-verdier-1-3-6-release-validation/v1"
)

CANDIDATE_ID = "stacks-verdier-a04446e-1-3-6-r1"
NAMESPACE = "commons/stacks/verdier-ast239-1-3-6-r1"
LEASE_ID = "stacks-lease-000044-verdier-ast239-1-3-6-r1"
OPERATION_ID = "VDR-STK-COMP-0002"
WRITER_TASK = "019fca5a-c80e-7890-a46b-4948ff443e6d"
OFFICIAL_COMMIT = "a04446e57ec1fbc252a871afcec7752fb2807b14"
OFFICIAL_TREE = "3feeb703b931a6e7259782c10e7d1575adc83e5e"

PUBLIC_R39_COMMIT = "f73b18165c7162b8386de06cc3c50bd4ced745b6"
PUBLIC_R39_TREE = "5bc25c775349eddf5fa90a7f37f5b11044d89ec1"
LEASE_ISSUE_COMMIT = "601f00d17f49edaa58abf20e572941434b72bb86"
DIRECT_RESOLVER_COMMIT = "ec0a80d418d8fa44c1b9fa077fcec8fe9f88c9df"
CANDIDATE_PACKET_COMMIT = "52eccb5772831e4bd17f9d4306b1ad0f60dec43f"
REPLAY_SEAL_COMMIT = "8f95214f9275cdc698f0c9bf5e7e8e5784772977"
ADMISSION_COMMIT = "d78483415a984eb7b46ad57b6056d8f718e3f395"

DIRECT_CHAIN = (
    ("public_r39", PUBLIC_R39_COMMIT),
    ("lease_issue", LEASE_ISSUE_COMMIT),
    ("direct_candidate_resolver", DIRECT_RESOLVER_COMMIT),
    ("candidate_packet", CANDIDATE_PACKET_COMMIT),
    ("independent_replay_seal", REPLAY_SEAL_COMMIT),
    ("registry_admission", ADMISSION_COMMIT),
)

CANDIDATE_PATH = f"ai-integrated/candidates/{NAMESPACE}"
MANIFEST_PATH = f"{CANDIDATE_PATH}/candidate.manifest.json"
COMPOSITION_PATH = f"{CANDIDATE_PATH}/composition.jsonl"
PAYLOAD_RELATIVE = "payload/fragments/derived-homotopy-category-abelian-split.tex"
PAYLOAD_PATH = f"{CANDIDATE_PATH}/{PAYLOAD_RELATIVE}"
OVERLAYS_PATH = "ai-integrated/registry/overlays.json"
LEASES_PATH = "ai-integrated/registry/leases.json"
DERIVED_PATH = "derived.tex"
DRIVER_PATH = "tools/build_verdier_1_3_6_fixed_point.py"
CORE_PATH = "tools/build_fixed_point.py"
RELEASE_VALIDATOR_PATH = "tools/validate_verdier_1_3_6_release.py"

BASE_BLOB = "f62f8645b22d39a3dd5998256f3a296bcb677d37"
BASE_BYTES = 452_054
BASE_SHA256 = "8B389993D3B364A926C7DCD7AD598E5B8245D8E92BCC5A23646069F9AD617860"
POSTIMAGE_BYTES = 455_727
POSTIMAGE_SHA256 = "726404F52F8E9EFD8D091DA3BF0EE9A1B288E6CFCC7A24DAD20ACB92926C62CE"
PAYLOAD_BYTES = 3_673
PAYLOAD_SHA256 = "C61FEF90594F0B1C3BD48870452A35C95F7DC85F56C551C0C68F40A01BE8BE9E"
PROPOSED_LABEL = "lemma-homotopy-category-abelian-split"

EXPECTED_STABLE_IDS = (
    "verdier:ast239:1.3.6",
    "verdier:ast239:1.3.6:equivalent-conditions",
    "verdier:ast239:1.3.6:proof:i-iff-ii",
    "verdier:ast239:1.3.6:proof:ii-implies-iii",
    "verdier:ast239:1.3.6:construction:hstar-complex",
    "verdier:ast239:1.3.6:claim:hstar-equivalence",
    "verdier:ast239:1.3.6:conclusion:iii-implies-ii",
)

# This is the complete R39-era profile, including the two chapters added after
# the legacy 28-stem profile.  Runtime equality with the shared build core is a
# fail-closed guard against silently drifting either inventory.
REQUIRED_STEMS = (
    "sets",
    "categories",
    "topology",
    "sheaves",
    "sites",
    "algebra",
    "fields",
    "artin",
    "brauer",
    "derived",
    "simplicial",
    "homology",
    "more-algebra",
    "smoothing",
    "modules",
    "sites-modules",
    "schemes",
    "properties",
    "morphisms",
    "more-morphisms",
    "spaces-morphisms",
    "crystalline",
    "spaces-cohomology",
    "spaces-duality",
    "stacks-limits",
    "injectives",
    "cohomology",
    "sites-cohomology",
    "gaga",
    "moduli",
)

PRECOMPOSITION_ALLOWED_PATHS = frozenset(
    {
        # Exact candidate-closure repair identified by the independent replay.
        f"{CANDIDATE_PATH}/.gitattributes",
        f"{CANDIDATE_PATH}/.gitignore",
        f"{CANDIDATE_PATH}/builds/baseline-derived.log",
        f"{CANDIDATE_PATH}/builds/derived.log",
        f"{CANDIDATE_PATH}/builds/derived.pdf",
        # Exact post-admission rights correction and its independent receipt.
        OVERLAYS_PATH,
        "validation/stacks-verdier-a04446e-1-3-6-r1-manifest-closure-correction-2026-09-06.json",
        # Dedicated release tooling committed before the source composition.
        DRIVER_PATH,
        RELEASE_VALIDATOR_PATH,
        "tools/validate_unified_repository.py",
        "tools/verify_github_commit_readback.py",
    }
)

AMBIENT_TEX_SEARCH_VARIABLES = frozenset(
    {
        "BIBINPUTS",
        "BSTINPUTS",
        "TEXINPUTS",
        "TEXMFCNF",
        "TEXMFCONFIG",
        "TEXMFDBS",
        "TEXMFHOME",
        "TEXMFLOCAL",
        "TEXMFOUTPUT",
        "TEXMFSYSCONFIG",
        "TEXMFSYSVAR",
        "TEXMFVAR",
        "VARTEXFONTS",
    }
)

SINGLED_MANIFEST_FIELDS = (
    "stable_unit_manifest",
    "source_map",
    "decision_ledger",
    "rejection_ledger",
    "formula_diagram_inventory",
)
SHA1 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9A-Fa-f]{64}$")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest().upper()


def git_bytes(source: Path, *args: str) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(source), *args],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(detail or f"bounded Git query failed: {' '.join(args)}")
    return completed.stdout


def commit_bytes(source: Path, revision: str, relative: str) -> bytes:
    return git_bytes(source, "show", f"{revision}:{relative}")


def strict_json_bytes(raw: bytes, label: str) -> dict[str, Any]:
    value = core.strict_json_loads(raw.decode("utf-8", errors="strict"), label)
    require(isinstance(value, dict), f"{label} is not a JSON object")
    return value


def safe_relative(value: object, label: str) -> str:
    require(isinstance(value, str) and bool(value), f"invalid {label}")
    assert isinstance(value, str)
    require("\\" not in value, f"{label} is not POSIX-relative: {value!r}")
    path = PurePosixPath(value)
    require(
        not path.is_absolute()
        and value == path.as_posix()
        and all(part not in ("", ".", "..") for part in path.parts),
        f"unsafe {label}: {value!r}",
    )
    return value


def commit_file_identity(source: Path, revision: str, relative: str) -> dict[str, object]:
    blob = core.git(source, "rev-parse", f"{revision}:{relative}")
    require(SHA1.fullmatch(blob) is not None, f"invalid blob for {revision}:{relative}")
    raw = commit_bytes(source, revision, relative)
    return {
        "path": relative,
        "git_blob": blob,
        "bytes": len(raw),
        "sha256": sha256_bytes(raw),
    }


def commit_tree(source: Path, revision: str) -> str:
    tree = core.git(source, "rev-parse", f"{revision}^{{tree}}")
    require(SHA1.fullmatch(tree) is not None, f"invalid tree for commit {revision}")
    return tree


def root_shared_inputs(source: Path) -> tuple[str, ...]:
    """Return the committed union so a deleted shared input cannot disappear."""
    names: set[str] = set()
    for revision in (PUBLIC_R39_COMMIT, "HEAD"):
        for relative in core.git(source, "ls-tree", "--name-only", revision).splitlines():
            path = PurePosixPath(relative)
            if len(path.parts) == 1 and path.suffix.lower() in core.EGA_SHARED_BUILD_SUFFIXES:
                names.add(relative)
    return tuple(sorted(names))


def manifest_references(manifest: dict[str, Any]) -> dict[str, str]:
    references: dict[str, str] = {}

    def add(binding: object, label: str) -> None:
        require(isinstance(binding, dict), f"invalid manifest binding: {label}")
        assert isinstance(binding, dict)
        relative = safe_relative(binding.get("path"), f"{label} path")
        digest = binding.get("sha256")
        require(
            isinstance(digest, str) and SHA256.fullmatch(digest) is not None,
            f"invalid manifest hash: {label}",
        )
        assert isinstance(digest, str)
        require(relative not in references, f"manifest repeats a path: {relative}")
        references[relative] = digest.upper()

    authorities = manifest.get("source_authorities")
    builds = manifest.get("builds")
    require(isinstance(authorities, list) and bool(authorities), "manifest has no authority")
    require(isinstance(builds, list) and bool(builds), "manifest has no build inventory")
    assert isinstance(authorities, list)
    assert isinstance(builds, list)
    for index, binding in enumerate(authorities):
        add(binding, f"source_authorities[{index}]")
    for index, binding in enumerate(builds):
        add(binding, f"builds[{index}]")
    for field in SINGLED_MANIFEST_FIELDS:
        add(manifest.get(field), field)
    require(
        "replay/independent-review.json" in references,
        "manifest does not bind the independent replay receipt",
    )
    return references


def validate_direct_chain(
    source: Path, precomposition_commit: str, composition_commit: str
) -> tuple[list[dict[str, str]], list[dict[str, object]]]:
    for value, label in (
        (precomposition_commit, "precomposition"),
        (composition_commit, "composition"),
    ):
        require(SHA1.fullmatch(value) is not None, f"invalid {label} commit: {value!r}")
        core.require_commit_object(source, value, label)

    chain: list[dict[str, str]] = []
    for index, (role, commit) in enumerate(DIRECT_CHAIN):
        core.require_commit_object(source, commit, role)
        core.require_ancestor(source, commit, role)
        if index:
            core.require_single_parent(source, commit, role, DIRECT_CHAIN[index - 1][1])
        chain.append({"role": role, "commit": commit, "tree": commit_tree(source, commit)})

    require(
        chain[0]["tree"] == PUBLIC_R39_TREE,
        "pinned public R39 tree does not match its commit",
    )
    core.require_ancestor(source, ADMISSION_COMMIT, "admission-to-precomposition", precomposition_commit)
    core.require_linear_suffix(
        source, ADMISSION_COMMIT, precomposition_commit, "precomposition repair suffix"
    )

    suffix_commits = core.git(
        source,
        "rev-list",
        "--reverse",
        f"{ADMISSION_COMMIT}..{precomposition_commit}",
    ).splitlines()
    suffix: list[dict[str, object]] = []
    expected_parent = ADMISSION_COMMIT
    for commit in suffix_commits:
        core.require_single_parent(
            source, commit, "precomposition suffix commit", expected_parent
        )
        changed_paths = core.git(
            source,
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "--no-renames",
            "-r",
            commit,
        ).splitlines()
        require(bool(changed_paths), f"empty precomposition suffix commit: {commit}")
        disallowed = sorted(set(changed_paths) - PRECOMPOSITION_ALLOWED_PATHS)
        require(
            not disallowed,
            "precomposition suffix changes non-allowlisted paths: " + ", ".join(disallowed),
        )
        suffix.append(
            {
                "commit": commit,
                "parent": expected_parent,
                "tree": commit_tree(source, commit),
                "changed_paths": changed_paths,
            }
        )
        expected_parent = commit
    require(
        expected_parent == precomposition_commit,
        "precomposition suffix does not end at the explicitly bound commit",
    )
    core.require_single_parent(
        source, composition_commit, "Verdier composition", precomposition_commit
    )
    core.require_ancestor(source, composition_commit, "composition-to-build-head")
    core.require_linear_suffix(
        source, composition_commit, "HEAD", "post-composition build-tool suffix"
    )
    return chain, suffix


def validate_candidate(
    source: Path, precomposition_commit: str, composition_commit: str
) -> dict[str, object]:
    manifest_raw = commit_bytes(source, precomposition_commit, MANIFEST_PATH)
    manifest = strict_json_bytes(manifest_raw, "precomposition candidate manifest")
    require(
        manifest.get("schema") == "mathematics-commons-stacks-candidate-manifest/v1",
        "candidate manifest schema mismatch",
    )
    for field, expected in (
        ("candidate_id", CANDIDATE_ID),
        ("lease_id", LEASE_ID),
        ("namespace", NAMESPACE),
        ("writer_task", WRITER_TASK),
    ):
        require(manifest.get(field) == expected, f"candidate manifest {field} mismatch")
    require(
        manifest.get("upstream")
        == {
            "lock": "upstream/stacks.lock.json",
            "commit": OFFICIAL_COMMIT,
            "tree": OFFICIAL_TREE,
        },
        "candidate upstream identity mismatch",
    )
    require(
        manifest.get("source_closure")
        == {
            "enumerated": True,
            "expected_units": len(EXPECTED_STABLE_IDS),
            "manifested_units": len(EXPECTED_STABLE_IDS),
            "complete": True,
        },
        "candidate source closure mismatch",
    )
    require(
        manifest.get("review_state") == "performed"
        and manifest.get("independent_replay") == "passed"
        and manifest.get("unresolved_defects") == [],
        "candidate is not in its passing reviewed state",
    )

    references = manifest_references(manifest)
    for relative, expected_sha in references.items():
        observed = sha256_bytes(
            commit_bytes(source, precomposition_commit, f"{CANDIDATE_PATH}/{relative}")
        )
        require(observed == expected_sha, f"manifest hash mismatch: {relative}")

    committed_files = core.git(
        source,
        "ls-tree",
        "-r",
        "--name-only",
        precomposition_commit,
        "--",
        CANDIDATE_PATH,
    ).splitlines()
    expected_files = sorted(
        [MANIFEST_PATH] + [f"{CANDIDATE_PATH}/{relative}" for relative in references]
    )
    require(
        sorted(committed_files) == expected_files,
        "precomposition candidate subtree is not exactly manifest-closed",
    )

    candidate_tree = core.git(source, "rev-parse", f"{precomposition_commit}:{CANDIDATE_PATH}")
    require(SHA1.fullmatch(candidate_tree) is not None, "candidate subtree is not a tree")
    for revision, label in ((composition_commit, "composition"), ("HEAD", "build HEAD")):
        observed = core.git(source, "rev-parse", f"{revision}:{CANDIDATE_PATH}")
        require(observed == candidate_tree, f"candidate subtree changed after precomposition: {label}")

    manifest_identity = commit_file_identity(source, precomposition_commit, MANIFEST_PATH)
    return {
        "path": CANDIDATE_PATH,
        "tree": candidate_tree,
        "manifest": manifest_identity,
        "manifest_reference_count": len(references),
    }


def validate_registries(
    source: Path, precomposition_commit: str, composition_commit: str,
    candidate: dict[str, object]
) -> dict[str, object]:
    overlay_identity = commit_file_identity(source, precomposition_commit, OVERLAYS_PATH)
    lease_identity = commit_file_identity(source, precomposition_commit, LEASES_PATH)
    for relative, expected_blob in (
        (OVERLAYS_PATH, overlay_identity["git_blob"]),
        (LEASES_PATH, lease_identity["git_blob"]),
    ):
        for revision, label in ((composition_commit, "composition"), ("HEAD", "build HEAD")):
            observed = core.git(source, "rev-parse", f"{revision}:{relative}")
            require(
                observed == expected_blob,
                f"precomposition registry changed before the build: {label}:{relative}",
            )

    # The direct suffix may contain a bounded metadata correction after the
    # admission transaction.  Bind the exact final registry state and the last
    # commit that changed each registry, rather than falsely claiming the
    # original admission commit necessarily contains the final metadata bytes.
    registry_last_changes: dict[str, str] = {}
    for relative in (OVERLAYS_PATH, LEASES_PATH):
        last_change = core.git(
            source, "log", "-1", "--format=%H", precomposition_commit, "--", relative
        )
        require(SHA1.fullmatch(last_change) is not None, f"cannot bind registry history: {relative}")
        core.require_ancestor(
            source, ADMISSION_COMMIT, f"admission-to-registry-state:{relative}", last_change
        )
        registry_last_changes[relative] = last_change

    overlays = strict_json_bytes(
        commit_bytes(source, precomposition_commit, OVERLAYS_PATH), "overlay registry"
    )
    leases = strict_json_bytes(
        commit_bytes(source, precomposition_commit, LEASES_PATH), "lease registry"
    )
    require(
        overlays.get("schema") == "mathematics-commons-stacks-overlay-registry/v1",
        "overlay registry schema mismatch",
    )
    require(
        leases.get("schema") == "mathematics-commons-stacks-lease-registry/v1",
        "lease registry schema mismatch",
    )
    entries = overlays.get("registered_entries")
    require(isinstance(entries, list), "overlay registry lacks entries")
    assert isinstance(entries, list)
    matches = [
        row for row in entries
        if isinstance(row, dict) and row.get("id") == CANDIDATE_ID
    ]
    require(len(matches) == 1, "Verdier overlay is not uniquely admitted")
    entry = matches[0]
    assert isinstance(entry, dict)
    manifest_identity = candidate.get("manifest")
    require(isinstance(manifest_identity, dict), "candidate manifest identity missing")
    assert isinstance(manifest_identity, dict)
    for field, expected in (
        ("namespace", NAMESPACE),
        ("writer", WRITER_TASK),
        ("source_commit", OFFICIAL_COMMIT),
        ("source_tree", OFFICIAL_TREE),
        ("manifest_sha256", manifest_identity.get("sha256")),
        ("stable_ids", list(EXPECTED_STABLE_IDS)),
        ("review_receipt", f"candidates/{NAMESPACE}/replay/independent-review.json"),
    ):
        observed = entry.get(field)
        if field == "manifest_sha256" and isinstance(observed, str):
            observed = observed.upper()
        require(observed == expected, f"overlay admission mismatch: {field}")

    all_stable_ids: list[str] = []
    for row in entries:
        require(isinstance(row, dict), "overlay registry contains a non-object entry")
        assert isinstance(row, dict)
        stable_ids = row.get("stable_ids")
        if isinstance(stable_ids, str):
            stable_ids = stable_ids.split()
        require(
            isinstance(stable_ids, list)
            and bool(stable_ids)
            and all(isinstance(value, str) and value for value in stable_ids),
            "overlay registry contains an invalid stable-ID inventory",
        )
        all_stable_ids.extend(stable_ids)
    require(len(entries) == 41, "direct admission does not yield 41 overlays")
    require(len(all_stable_ids) == 1_156, "direct admission does not yield 1156 stable IDs")
    require(
        len(set(all_stable_ids)) == len(all_stable_ids),
        "overlay registry contains duplicate stable IDs",
    )
    require(entries[-1] == entry, "Verdier overlay is not the registry cutoff entry")

    events = leases.get("events")
    require(isinstance(events, list), "lease registry lacks events")
    assert isinstance(events, list)
    event_ids = [row.get("event_id") if isinstance(row, dict) else None for row in events]
    expected_event_ids = [f"lease-event-{number:06d}" for number in range(1, len(events) + 1)]
    require(event_ids == expected_event_ids, "lease registry event sequence is not contiguous")
    related = [
        row for row in events
        if isinstance(row, dict) and row.get("lease_id") == LEASE_ID
    ]
    require(len(related) == 2, "Verdier lease lifecycle is not exactly issue then release")
    issued, released = related
    require(
        issued.get("event_id") == "lease-event-000084"
        and issued.get("event") == "issued"
        and issued.get("state") == "active",
        "Verdier lease issue event mismatch",
    )
    require(
        released.get("event_id") == "lease-event-000085"
        and released.get("event") == "released"
        and released.get("state") == "released"
        and released.get("supersedes_event_id") == "lease-event-000084",
        "Verdier lease release event mismatch",
    )
    common = {
        "lease_id": LEASE_ID,
        "namespace": NAMESPACE,
        "candidate_path": f"candidates/{NAMESPACE}",
        "writer_task": WRITER_TASK,
        "upstream_commit": OFFICIAL_COMMIT,
        "upstream_tree": OFFICIAL_TREE,
        "writer_contract": "candidates/CONTRACT.md",
    }
    for event in related:
        for field, expected in common.items():
            require(event.get(field) == expected, f"Verdier lease {field} mismatch")

    return {
        "admission_commit": ADMISSION_COMMIT,
        "state_commit": precomposition_commit,
        "last_change_commits": registry_last_changes,
        "registered_overlays": len(entries),
        "registered_stable_ids": len(all_stable_ids),
        "last_admitted_overlay": CANDIDATE_ID,
        "overlays": overlay_identity,
        "leases": lease_identity,
        "lease_issue_event": "lease-event-000084",
        "lease_release_event": "lease-event-000085",
    }


def validate_composition(
    source: Path, precomposition_commit: str, composition_commit: str
) -> dict[str, object]:
    changed_paths = core.git(
        source,
        "diff-tree",
        "--no-commit-id",
        "--name-only",
        "-r",
        composition_commit,
    ).splitlines()
    require(
        changed_paths == [DERIVED_PATH],
        "composition commit must change exactly derived.tex",
    )

    operation_raw = commit_bytes(source, precomposition_commit, COMPOSITION_PATH)
    lines = [line for line in operation_raw.decode("utf-8", errors="strict").splitlines() if line.strip()]
    require(len(lines) == 1, "composition ledger must contain exactly one operation")
    operation = core.strict_json_loads(lines[0], "Verdier composition operation")
    require(isinstance(operation, dict), "composition operation is not a JSON object")
    assert isinstance(operation, dict)
    require(
        operation.get("schema") == "mathematics-commons-stacks-composition-operation/v1"
        and operation.get("operation_id") == OPERATION_ID
        and operation.get("operation") == "insert_bytes"
        and operation.get("mode") == "insertion_only",
        "Verdier composition operation identity mismatch",
    )
    target = operation.get("target")
    insertion = operation.get("insertion")
    payload_record = operation.get("payload")
    constraints = operation.get("constraints")
    require(
        all(isinstance(value, dict) for value in (target, insertion, payload_record, constraints)),
        "composition contract is incomplete",
    )
    assert isinstance(target, dict)
    assert isinstance(insertion, dict)
    assert isinstance(payload_record, dict)
    assert isinstance(constraints, dict)
    expected_target = {
        "base_kind": "published_unified_main",
        "repository": "https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts",
        "commit": PUBLIC_R39_COMMIT,
        "tree": PUBLIC_R39_TREE,
        "path": DERIVED_PATH,
        "blob": BASE_BLOB,
        "bytes": BASE_BYTES,
        "preimage_sha256": BASE_SHA256,
        "postimage_bytes": POSTIMAGE_BYTES,
        "postimage_sha256": POSTIMAGE_SHA256,
    }
    require(target == expected_target, "composition target differs from the frozen R39 contract")
    require(
        constraints
        == {
            "existing_target_bytes_changed": 0,
            "delete_bytes": 0,
            "replace_bytes": 0,
            "insert_payload_once": True,
        },
        "composition is not strictly insertion-only",
    )
    require(
        payload_record.get("path") == PAYLOAD_RELATIVE
        and payload_record.get("bytes") == PAYLOAD_BYTES
        and str(payload_record.get("sha256", "")).upper() == PAYLOAD_SHA256
        and payload_record.get("proposed_label") == PROPOSED_LABEL,
        "composition payload record mismatch",
    )

    base = commit_bytes(source, precomposition_commit, DERIVED_PATH)
    require(
        len(base) == BASE_BYTES and sha256_bytes(base) == BASE_SHA256,
        "precomposition derived.tex is not the frozen public R39 preimage",
    )
    require(
        core.git(source, "rev-parse", f"{precomposition_commit}:{DERIVED_PATH}") == BASE_BLOB,
        "precomposition derived.tex blob mismatch",
    )
    payload = commit_bytes(source, precomposition_commit, PAYLOAD_PATH)
    require(
        len(payload) == PAYLOAD_BYTES and sha256_bytes(payload) == PAYLOAD_SHA256,
        "committed Verdier payload identity mismatch",
    )
    offset = insertion.get("byte_offset")
    start = insertion.get("context_start_byte")
    end = insertion.get("context_end_byte_exclusive")
    require(
        type(offset) is int and type(start) is int and type(end) is int,
        "composition context offsets are not integers",
    )
    assert isinstance(offset, int)
    assert isinstance(start, int)
    assert isinstance(end, int)
    require(0 <= start <= offset <= end <= len(base), "composition offsets are out of range")
    context = base[start:end]
    before = base[start:offset]
    after = base[offset:end]
    for raw, bytes_field, sha_field, label in (
        (context, "context_bytes", "context_sha256", "context"),
        (before, "before_context_bytes", "before_context_sha256", "before context"),
        (after, "after_context_bytes", "after_context_sha256", "after context"),
    ):
        require(len(raw) == insertion.get(bytes_field), f"{label} byte count mismatch")
        require(
            sha256_bytes(raw) == str(insertion.get(sha_field, "")).upper(),
            f"{label} hash mismatch",
        )
    require(
        insertion.get("required_anchor_occurrences") == 1 and base.count(context) == 1,
        "composition context is not unique",
    )
    label_token = f"\\label{{{PROPOSED_LABEL}}}".encode("ascii")
    require(base.count(payload) == 0 and base.count(label_token) == 0, "payload already in base")
    require(payload.count(label_token) == 1, "payload label inventory mismatch")
    projected = base[:offset] + payload + base[offset:]
    require(
        len(projected) == POSTIMAGE_BYTES and sha256_bytes(projected) == POSTIMAGE_SHA256,
        "computed insertion projection does not match the frozen postimage",
    )

    composed = commit_bytes(source, composition_commit, DERIVED_PATH)
    require(composed == projected, "composition commit is not the exact insertion projection")
    current = commit_bytes(source, "HEAD", DERIVED_PATH)
    require(current == composed, "derived.tex changed after the exact composition commit")
    require(current[:offset] == base[:offset], "preexisting bytes before the insertion changed")
    require(
        current[offset + len(payload):] == base[offset:],
        "preexisting bytes after the insertion changed",
    )

    # Candidate lifecycle and tool commits must not smuggle source changes into
    # the build.  Every selected source and every shared root TeX input remains
    # byte-identical to public R39 except for the one derived.tex insertion;
    # post-composition tool commits must preserve that entire input set.
    shared_inputs = root_shared_inputs(source)
    unchanged_inputs = tuple(
        dict.fromkeys(
            [
                "preamble.tex",
                "chapters.tex",
                "my.bib",
                *(f"{stem}.tex" for stem in REQUIRED_STEMS if stem != "derived"),
                *shared_inputs,
            ]
        )
    )
    unchanged_lines: list[str] = []
    for relative in unchanged_inputs:
        baseline_blob = core.git(source, "rev-parse", f"{PUBLIC_R39_COMMIT}:{relative}")
        require(SHA1.fullmatch(baseline_blob) is not None, f"invalid R39 blob: {relative}")
        for revision, label in (
            (precomposition_commit, "precomposition"),
            (composition_commit, "composition"),
            ("HEAD", "build HEAD"),
        ):
            observed = core.git(source, "rev-parse", f"{revision}:{relative}")
            require(
                observed == baseline_blob,
                f"non-Verdier build input changed after public R39: {label}:{relative}",
            )
        unchanged_lines.append(f"{relative}|{baseline_blob}")

    composed_identity = commit_file_identity(source, composition_commit, DERIVED_PATH)
    operation_identity = commit_file_identity(source, precomposition_commit, COMPOSITION_PATH)
    payload_identity = commit_file_identity(source, precomposition_commit, PAYLOAD_PATH)
    return {
        "operation_id": OPERATION_ID,
        "receipt": COMPOSITION_PATH,
        "receipt_sha256": operation_identity["sha256"],
        "contract": operation_identity,
        "payload": payload_identity,
        "base": {
            "commit": PUBLIC_R39_COMMIT,
            "tree": PUBLIC_R39_TREE,
            "path": DERIVED_PATH,
            "git_blob": BASE_BLOB,
            "bytes": BASE_BYTES,
            "sha256": BASE_SHA256,
        },
        "insertion_offset": offset,
        "postimage": composed_identity,
        "changed_paths": changed_paths,
        "unchanged_r39_build_inputs": {
            "count": len(unchanged_lines),
            "tuple_set_sha256": sha256_bytes(
                (("\n".join(unchanged_lines)) + "\n").encode("utf-8")
            ),
        },
    }


def require_clean_inputs(source: Path) -> None:
    critical = {
        DRIVER_PATH,
        CORE_PATH,
        RELEASE_VALIDATOR_PATH,
        MANIFEST_PATH,
        COMPOSITION_PATH,
        PAYLOAD_PATH,
        OVERLAYS_PATH,
        LEASES_PATH,
        DERIVED_PATH,
        "preamble.tex",
        "chapters.tex",
        "my.bib",
        *(f"{stem}.tex" for stem in REQUIRED_STEMS),
    }
    critical.update(root_shared_inputs(source))
    for relative in sorted(critical):
        tracked = core.git_optional(source, "ls-files", "--error-unmatch", "--", relative)
        require(tracked == relative, f"build-critical path is not tracked: {relative}")
        core.require_clean_path(source, relative)


def run_release_validator(source: Path) -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, "-B", str(source / RELEASE_VALIDATOR_PATH), "--root", str(source)],
        cwd=source,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    try:
        report = json.loads(completed.stdout.decode("utf-8", errors="strict"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("Verdier release validator emitted invalid JSON") from exc
    require(isinstance(report, dict), "Verdier release validator report is not an object")
    assert isinstance(report, dict)
    if completed.returncode != 0 or report.get("status") != "PASS" or report.get("passed") is not True:
        detail = report.get("error") or completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"Verdier release validator failed: {detail}")
    require(report.get("schema") == RELEASE_VALIDATION_SCHEMA, "release validator schema mismatch")
    require(report.get("candidate_id") == CANDIDATE_ID, "release validator candidate mismatch")
    require(report.get("read_only") is True and report.get("tex_run") is False, "release validator contract mismatch")
    return {
        "path": RELEASE_VALIDATOR_PATH,
        "report_schema": report["schema"],
        "report_status": report["status"],
        "report_sha256": sha256_bytes(completed.stdout),
        "candidate_id": report["candidate_id"],
        "read_only": True,
        "tex_run": False,
    }


def normalized_mutex_receipt(details: dict[str, object]) -> dict[str, object]:
    keys = (
        "schema",
        "status",
        "name",
        "namespace",
        "acquisition_timeout_ms",
        "wait_result",
        "abandoned_mutex_recovered",
        "ownership_acquired",
        "held_scope",
        "release_result",
    )
    normalized = {key: details.get(key) for key in keys}
    require(
        normalized.get("name") == core.TEX_MUTEX_NAME
        and normalized.get("status") == "PASS"
        and normalized.get("ownership_acquired") is True
        and normalized.get("release_result") == "released_in_finally",
        "TeX mutex receipt is not a successful acquire-through-release record",
    )
    return normalized


def fixed_point_artifacts(source: Path) -> tuple[list[dict[str, object]], str]:
    rows: list[dict[str, object]] = []
    lines: list[str] = []
    for stem in REQUIRED_STEMS:
        for suffix in core.FIXED_POINT_SUFFIXES:
            relative = f"{stem}{suffix}"
            path = source / relative
            if path.is_file():
                row: dict[str, object] = {
                    "path": relative,
                    "bytes": path.stat().st_size,
                    "sha256": core.sha256(path),
                }
                lines.append(f"{relative}|{row['bytes']}|{row['sha256']}")
            else:
                row = {"path": relative, "state": "ABSENT"}
                lines.append(f"{relative}|ABSENT")
            rows.append(row)
    digest = sha256_bytes((("\n".join(lines)) + "\n").encode("utf-8"))
    return rows, digest


def build_once(
    source: Path,
    max_sweeps: int,
    source_date_epoch: str,
) -> tuple[list[dict[str, object]], dict[str, object], dict[str, str], list[dict[str, object]], str]:
    require(tuple(core.DEFAULT_STEMS) == REQUIRED_STEMS, "shared core no longer has the exact 30-stem profile")
    require(max_sweeps >= 2, "--max-sweeps must be at least 2")
    require(source_date_epoch.isdigit(), "--source-date-epoch must be a nonnegative integer")
    for executable in ("pdflatex", "bibtex", "pdfinfo"):
        require(shutil.which(executable) is not None, f"required executable is unavailable: {executable}")
    for stem in REQUIRED_STEMS:
        require((source / f"{stem}.tex").is_file(), f"missing chapter source: {stem}.tex")

    reference_labels = core.external_reference_labels(source)
    env = os.environ.copy()
    cleared_search_variables = sorted(
        key for key in tuple(env) if key.upper() in AMBIENT_TEX_SEARCH_VARIABLES
    )
    for key in cleared_search_variables:
        env.pop(key, None)
    env["SOURCE_DATE_EPOCH"] = source_date_epoch
    env["FORCE_SOURCE_DATE"] = "1"
    env["TZ"] = "UTC"

    for stem in REQUIRED_STEMS:
        for suffix in core.GENERATED_SUFFIXES:
            artifact = source / f"{stem}{suffix}"
            if artifact.is_file():
                artifact.unlink()
    survivors = [
        f"{stem}{suffix}"
        for stem in REQUIRED_STEMS
        for suffix in core.GENERATED_SUFFIXES
        if (source / f"{stem}{suffix}").exists()
    ]
    require(not survivors, "generated artifacts survived clean-build boundary: " + ", ".join(survivors[:8]))

    latex = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
    ]
    fixed_sweep: int | None = None
    artifacts: list[dict[str, object]] = []
    diagnostics_total = {
        "fatal_markers": 0,
        "missing_glyph_markers": 0,
        "undefined_reference_markers": 0,
        "external_reference_markers": 0,
        "undefined_citation_markers": 0,
        "multiply_defined_markers": 0,
        "rerun_required_markers": 0,
        "destination_warning_markers": 0,
    }
    pages_pattern = re.compile(r"^Pages:\s+(\d+)\s*$", re.MULTILINE)
    mutex = core.WindowsNamedMutex(core.TEX_MUTEX_NAME, core.TEX_MUTEX_TIMEOUT_MS)
    with mutex:
        for stem in REQUIRED_STEMS:
            print(f"prime {stem}", flush=True)
            core.run([*latex, f"{stem}.tex"], source, env, mutex)
        for stem in REQUIRED_STEMS:
            print(f"bibtex {stem}", flush=True)
            core.run(["bibtex", stem], source, env, mutex)

        previous: tuple[str, ...] | None = None
        for sweep in range(1, max_sweeps + 1):
            print(f"global sweep {sweep}", flush=True)
            for stem in REQUIRED_STEMS:
                core.run([*latex, f"{stem}.tex"], source, env, mutex)
            current = core.build_state_vector(source, REQUIRED_STEMS)
            if current == previous:
                fixed_sweep = sweep
                break
            previous = current
        require(
            fixed_sweep is not None,
            f"generated build state did not reach a fixed point in {max_sweeps} sweeps",
        )

        for stem in REQUIRED_STEMS:
            pdf = source / f"{stem}.pdf"
            info = core.run(["pdfinfo", str(pdf)], source, env, mutex)
            match = pages_pattern.search(info)
            require(match is not None and int(match.group(1)) > 0, f"invalid PDF page count: {stem}")
            diagnostics, external_inventory = core.scan_tex_diagnostics(
                source / f"{stem}.log",
                source / f"{stem}.blg",
                stem,
                reference_labels,
            )
            for key, value in diagnostics.items():
                diagnostics_total[key] += value
            artifacts.append(
                {
                    "stem": stem,
                    "pages": int(match.group(1)),
                    "bytes": pdf.stat().st_size,
                    "sha256": core.sha256(pdf),
                    "diagnostics": diagnostics,
                    "external_references": external_inventory,
                }
            )
        failed = {
            key: value
            for key, value in diagnostics_total.items()
            if key != "external_reference_markers" and value
        }
        require(not failed, "final TeX diagnostics are not clean: " + ", ".join(f"{k}={v}" for k, v in failed.items()))
        versions = {
            "pdftex": core.version_line("pdflatex", env, source, mutex),
            "bibtex": core.version_line("bibtex", env, source, mutex),
            "pdfinfo": core.version_line("pdfinfo", env, source, mutex),
        }
    mutex_details = normalized_mutex_receipt(mutex.receipt_details())
    fixed_artifacts, fixed_digest = fixed_point_artifacts(source)
    build = {
        "strategy": "single-invocation-sequential-prime-bibtex-global-state-sweeps",
        "fixed_point_suffixes": list(core.FIXED_POINT_SUFFIXES),
        "stem_selection": "dedicated_exact_30_stem_profile",
        "stems": list(REQUIRED_STEMS),
        "chapter_count": len(REQUIRED_STEMS),
        "global_fixed_point_sweep": fixed_sweep,
        "pdfinfo_readable": len(artifacts),
        "diagnostics": diagnostics_total,
        "worktree_kind": core.worktree_kind(source),
        "machine_wide_tex_mutex": mutex_details,
        "fixed_point_artifacts": fixed_artifacts,
        "fixed_point_artifact_set_sha256": fixed_digest,
        "builds_per_invocation": 1,
        "tex_search_environment": {
            "policy": "ambient_overrides_removed",
            "removed_variable_names": cleared_search_variables,
            "removed_variable_values_recorded": False,
        },
    }
    return artifacts, build, versions, fixed_artifacts, fixed_digest


def output_path(source: Path, requested: Path) -> tuple[Path, str]:
    output = requested if requested.is_absolute() else source / requested
    output = output.resolve()
    try:
        relative = output.relative_to(source).as_posix()
    except ValueError as exc:
        raise RuntimeError("build receipt output must be inside the source worktree") from exc
    require(
        Path(relative).parent.as_posix() == "validation" and output.suffix.lower() == ".json",
        "build receipt must be a JSON file directly under validation/",
    )
    require(not output.exists(), f"refusing to overwrite build receipt: {relative}")
    require(
        core.git_optional(source, "ls-files", "--error-unmatch", "--", relative) is None,
        f"refusing to overwrite tracked build receipt: {relative}",
    )
    return output, relative


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--precomposition-commit", required=True)
    parser.add_argument("--composition-commit", required=True)
    parser.add_argument("--source-date-epoch", default="1785270512")
    parser.add_argument("--max-sweeps", type=int, default=6)
    parser.add_argument(
        "--allow-primary-worktree",
        action="store_true",
        help="allow generated-file mutation in the repository's primary worktree",
    )
    args = parser.parse_args(argv)

    source = args.source.resolve()
    kind = core.worktree_kind(source)
    if kind == "primary" and not args.allow_primary_worktree:
        raise RuntimeError(
            "refusing to mutate generated files in the primary worktree; use a linked disposable worktree"
        )
    initial_commit, initial_tree = core.capture_source_revision(source)
    output, output_relative = output_path(source, args.output)

    chain, precomposition_suffix = validate_direct_chain(
        source, args.precomposition_commit, args.composition_commit
    )
    candidate = validate_candidate(source, args.precomposition_commit, args.composition_commit)
    registries = validate_registries(
        source, args.precomposition_commit, args.composition_commit, candidate
    )
    composition = validate_composition(
        source, args.precomposition_commit, args.composition_commit
    )
    require_clean_inputs(source)
    release_validation = run_release_validator(source)

    artifacts, build, versions, _, _ = build_once(
        source, args.max_sweeps, args.source_date_epoch
    )
    build["worktree_kind"] = kind
    build["primary_worktree_override"] = args.allow_primary_worktree
    core.require_source_revision_unchanged(source, initial_commit, initial_tree)
    require_clean_inputs(source)

    driver_identity = commit_file_identity(source, "HEAD", DRIVER_PATH)
    core_identity = commit_file_identity(source, "HEAD", CORE_PATH)
    validator_identity = commit_file_identity(source, "HEAD", RELEASE_VALIDATOR_PATH)
    tuple_lines = [
        "|".join(
            (
                str(artifact["stem"]),
                str(artifact["pages"]),
                str(artifact["bytes"]),
                str(artifact["sha256"]),
            )
        )
        for artifact in sorted(artifacts, key=lambda item: str(item["stem"]))
    ]
    build["artifact_tuple_set_sha256"] = sha256_bytes(
        (("\n".join(tuple_lines)) + "\n").encode("utf-8")
    )

    composition_binding = {
        "schema": DIRECT_BINDING_SCHEMA,
        "candidate_id": CANDIDATE_ID,
        "namespace": NAMESPACE,
        "lease_id": LEASE_ID,
        "direct_prefixed_paths": True,
        "historical_unprefixed_v4_topology_used": False,
        "direct_chain": chain,
        "precomposition_suffix": precomposition_suffix,
        "precomposition_commit": args.precomposition_commit,
        "precomposition_tree": commit_tree(source, args.precomposition_commit),
        "composition_commit": args.composition_commit,
        "composition_tree": commit_tree(source, args.composition_commit),
        "admission_commit": ADMISSION_COMMIT,
        "registry_cutoff_commit": args.precomposition_commit,
        "candidate": candidate,
        "registry": registries,
        **composition,
        "release_validation": release_validation,
    }
    receipt = {
        "schema": RECEIPT_SCHEMA,
        "status": "PASS",
        "created_utc": core.utc_timestamp(),
        "source": {"commit": initial_commit, "tree": initial_tree},
        "builder": driver_identity,
        "build_core": core_identity,
        "release_validator": validator_identity,
        "composition": composition_binding,
        "environment": {
            "operating_system": platform.platform(),
            "python": platform.python_version(),
            **versions,
            "source_date_epoch": args.source_date_epoch,
        },
        "build": build,
        "artifacts": artifacts,
        "pdfs_committed": False,
        "sanitization": {
            "absolute_paths_recorded": False,
            "environment_variables_recorded": False,
            "credentials_recorded": False,
            "commands_recorded": False,
        },
    }
    core.publish_build_receipt(
        source,
        output,
        output_relative,
        receipt,
        initial_commit,
        initial_tree,
        None,
        None,
        (),
    )
    raw = output.read_bytes()
    print(
        json.dumps(
            {
                "status": "PASS",
                "chapters": len(artifacts),
                "fixed_point_sweep": build["global_fixed_point_sweep"],
                "receipt": output_relative,
                "receipt_bytes": len(raw),
                "receipt_sha256": sha256_bytes(raw),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
