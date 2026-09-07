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
FINALIZER_PATH = "tools/finalize_verdier_1_3_6_release.py"
COMPOSITION_RECEIPT_PATH = "validation/composition-current.json"
EGA_SOURCE_CHECKPOINT_PATH = core.EGA_SOURCE_CHECKPOINT_PATH

# The EGA source checkpoint was generated and independently checked on its own
# source branch before this direct Verdier lineage was assembled.  The direct
# build is a descendant of that sealed receipt, not a second EGA checkpoint
# generation.  Keep the exact prior identity here so a build cannot silently
# consume a substituted or regenerated checkpoint.
EGA_SOURCE_CHECKPOINT_CONTENT_COMMIT = (
    "571648f5c43c36617629c8ae57b28606d966625f"
)
EGA_SOURCE_CHECKPOINT_CONTENT_TREE = (
    "12faacf779ad018c4c2729167d1afa1ef6b9d0e5"
)
EGA_SOURCE_CHECKPOINT_RECEIPT_COMMIT = (
    "91cc89df5804b8c1949d8267602fc076649ee49b"
)
EGA_SOURCE_CHECKPOINT_RECEIPT_TREE = (
    "060538ea3323b366e8f445fd79725a63c4241d2f"
)
EGA_SOURCE_CHECKPOINT_BYTES = 44_426
EGA_SOURCE_CHECKPOINT_SHA256 = (
    "95B8D2B14D7C1CB7E9F826F6EBF0A6723DBDB05DC5D06F06F186E21465CC3352"
)
EGA_SOURCE_CHECKPOINT_BLOB = "715024558f8480811dc3d27521d65cdaa893ca45"

# The integration branch is expected to be merged once with the exact current
# main parent below.  A merge against any other commit (or with an unexpected
# tree) is rejected; this is a binding, not a general-purpose merge escape
# hatch.  The parent is the current-main tip at the time this Verdier lane was
# scoped and its tree is retained as an immutable identity witness.
CURRENT_MAIN_PARENT_COMMIT = "e083b71ac21e0ecb7508aa6a1067a1b0016d89a7"
CURRENT_MAIN_PARENT_TREE = "ea6837e424feda8f9e020b5b3083a503ca7247fb"
CURRENT_MAIN_MERGE_BASE = PUBLIC_R39_COMMIT
CURRENT_MAIN_ALLOWED_PATHS = frozenset(
    {
        "illusie_volume_I/.gitignore",
        "illusie_volume_I/README.md",
        "illusie_volume_I/build-receipt-i1-2.json",
        "illusie_volume_I/build-receipt-i1-3.json",
        "illusie_volume_I/build-receipt.json",
        "illusie_volume_I/build.py",
        "illusie_volume_I/check.json",
        "illusie_volume_I/map.json",
        "illusie_volume_I/qa-i1-2.json",
        "illusie_volume_I/qa-i1-3.json",
        "illusie_volume_I/qa.json",
        "illusie_volume_I/relative-homotopy.tex",
        "illusie_volume_I/source-lock.json",
        "illusie_volume_I/source-notes.md",
        "illusie_volume_I/test_composition.py",
        "illusie_volume_I/verify.py",
        "simplicial.tex",
        "tools/validate_unified_repository.py",
    }
)
# The current-main integration changes one root build input that is part of
# the 30-stem profile.  Its exact parent-side blob is bound below; no other
# R39/EGA build input receives an override.
CURRENT_MAIN_BUILD_INPUT_PATHS = ("simplicial.tex",)
CURRENT_MAIN_R39_BUILD_INPUT_BLOBS = {
    "simplicial.tex": "bcec4895b138415bea4febc348ad4e3e9f519b44",
}
CURRENT_MAIN_BUILD_INPUT_BLOBS = {
    "simplicial.tex": "3f222b229e864887dc3a64a199dc11dc2a96ed0d",
}

# Exact non-candidate paths that may arrive from the known Verdier side of the
# integration merge.  Candidate paths are resolved against the committed
# manifest-closed inventory at the bound composition commit; every other path
# is rejected.  This intentionally does not include source chapters, ledgers,
# PDFs, or arbitrary validation files.
VERDIER_MERGE_EXACT_PATHS = frozenset(
    {
        OVERLAYS_PATH,
        LEASES_PATH,
        DERIVED_PATH,
        DRIVER_PATH,
        CORE_PATH,
        RELEASE_VALIDATOR_PATH,
        FINALIZER_PATH,
        COMPOSITION_RECEIPT_PATH,
        "tools/validate_unified_repository.py",
        "tools/verify_github_commit_readback.py",
        "validation/stacks-verdier-a04446e-1-3-6-r1-manifest-closure-correction-2026-09-06.json",
    }
)

# d18363d9 records the v4 composition receipt after the source composition.
# Any later descendant used for this build may contain only that receipt and
# the explicitly scoped release-tool repairs.  Source, candidate, registry,
# and generated-artifact paths are intentionally absent from this set.
POSTCOMPOSITION_ALLOWED_PATHS = frozenset(
    {
        COMPOSITION_RECEIPT_PATH,
        DRIVER_PATH,
        CORE_PATH,
        RELEASE_VALIDATOR_PATH,
        FINALIZER_PATH,
        "tools/validate_unified_repository.py",
        "tools/verify_github_commit_readback.py",
    }
)

EGA_SOURCE_CHECKPOINT_CHECKS = (
    "schema_status",
    "base_content_topology",
    "exact_changed_path_diff",
    "tooling_identities_bound",
    "actual_base_and_content_commits_and_trees_exact",
    "content_is_single_parent_child_of_actual_base",
    "historical_implementation_base_is_ancestor_and_all_eight_preimages_rebind_exactly",
    "exact_ten_path_base_to_content_delta",
    "immutable_implementation_and_independent_review_receipts_bound",
    "unique_01K5_omitted_proof_replaced_230_to_1195_with_1000_byte_proof",
    "01K5_statement_label_and_official_tag_unchanged",
    "schemes_full_preimage_postimage_and_outside_block_bytes_exact",
    "all_other_119_root_tex_blobs_unchanged",
    "tags_registry_and_composition_receipt_unchanged",
    "four_ledger_prefixes_and_reserved_append_ranges_exact",
    "live_counts_recomputed_from_committed_ledgers",
    "prior_scope_slices_preserved_and_6_6_4_slice_exact",
    "continuation_is_EGA_I_6_6_5",
    "source_authority_hashes_bound",
    "canonical_authority_source_receipt_and_slice_cross_bound_exactly",
    "README_6_6_4_insertion_unique_anchored_and_outside_branch_unchanged",
    "four_ledger_headers_rows_IDs_cross_references_and_counts_exact",
    "no_post_content_source_drift_at_generation",
)

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
    return chain, suffix


def validate_postcomposition_suffix(
    source: Path, composition_commit: str
) -> list[dict[str, object]]:
    """Validate the bounded descendant between source composition and build.

    The v4 composition receipt is intentionally recorded in a child commit,
    and release-tool repairs may follow it.  Keep that normal descendant
    shape, but reject every path/status outside the explicit release-tool
    allowlist.  Candidate paths are accepted only when already present in the
    manifest-closed candidate subtree at the bound composition commit.  In
    particular, no source, registry, or generated artifact can be smuggled into
    the build head.
    """
    head = core.git(source, "rev-parse", "HEAD")
    core.require_ancestor(
        source, composition_commit, "composition-to-build-head", head
    )

    def check_changes(
        changes: dict[str, tuple[str, str, str, str, str]],
        label: str,
        path_allowed: object,
    ) -> dict[str, str]:
        require(bool(changes), f"empty {label}")
        disallowed = sorted(
            path for path in changes if not bool(path_allowed(path))
        )
        require(
            not disallowed,
            f"{label} changes non-allowlisted paths: " + ", ".join(disallowed),
        )
        statuses = {path: row[4] for path, row in changes.items()}
        invalid_statuses = sorted(
            path for path, status in statuses.items() if status not in {"A", "M"}
        )
        require(
            not invalid_statuses,
            f"{label} contains deletion/type change: " + ", ".join(invalid_statuses),
        )
        return statuses

    candidate_paths = frozenset(
        core.git(
            source,
            "ls-tree",
            "-r",
            "--name-only",
            composition_commit,
            "--",
            CANDIDATE_PATH,
        ).splitlines()
    )
    require(bool(candidate_paths), "bound Verdier candidate subtree is empty")

    def verdier_path_allowed(path: str) -> bool:
        # Resolve the namespace to the exact committed candidate inventory;
        # a prefix-only rule would let an arbitrary new candidate artifact
        # pass the merge-path gate before the later manifest check runs.
        return path in VERDIER_MERGE_EXACT_PATHS or path in candidate_paths

    # Walk the Verdier ancestry itself rather than asking ``rev-list`` for a
    # linear suffix.  The planned integration commit is current-main-first:
    # parent 1 is the one exact current-main tip above and parent 2 is the
    # Verdier line.  Following parent 2 keeps all current-main history outside
    # the suffix while still binding its immutable parent/tree.
    reverse_rows: list[dict[str, object]] = []
    cursor = head
    visited: set[str] = set()
    merge_row: dict[str, object] | None = None
    while cursor != composition_commit:
        require(cursor not in visited, "post-composition ancestry contains a cycle")
        visited.add(cursor)
        require(len(visited) <= 512, "post-composition ancestry is unreasonably long")
        parents = core.commit_parents(source, cursor)

        if len(parents) == 1:
            expected_parent = parents[0]
            changes = core.committed_path_changes(source, expected_parent, cursor)
            statuses = check_changes(
                changes,
                f"post-composition suffix commit {cursor}",
                lambda path: path in POSTCOMPOSITION_ALLOWED_PATHS,
            )
            reverse_rows.append(
                {
                    "commit": cursor,
                    "parent": expected_parent,
                    "parents": list(parents),
                    "topology": "single_parent",
                    "tree": commit_tree(source, cursor),
                    "changed_paths": sorted(changes),
                    "statuses": statuses,
                }
            )
            cursor = expected_parent
            continue

        require(
            len(parents) == 2,
            "post-composition suffix contains an unsupported merge topology: "
            + cursor,
        )
        require(
            merge_row is None,
            "post-composition suffix contains more than one merge commit",
        )
        require(
            parents[0] == CURRENT_MAIN_PARENT_COMMIT,
            "post-composition merge parent 1 is not the exact current-main tip",
        )
        verdier_parent = parents[1]
        core.require_commit_object(
            source, CURRENT_MAIN_PARENT_COMMIT, "known current-main merge parent"
        )
        require(
            commit_tree(source, CURRENT_MAIN_PARENT_COMMIT)
            == CURRENT_MAIN_PARENT_TREE,
            "known current-main merge parent tree identity drifted",
        )
        core.require_ancestor(
            source,
            CURRENT_MAIN_MERGE_BASE,
            "current-main merge-base",
            CURRENT_MAIN_PARENT_COMMIT,
        )
        require(
            core.git(
                source, "merge-base", CURRENT_MAIN_PARENT_COMMIT, verdier_parent
            )
            == CURRENT_MAIN_MERGE_BASE,
            "post-composition merge does not have the bound R39 merge base",
        )

        # Compare the merge tree to both parents.  The second-parent projection
        # may include the exact current-main delta; the first-parent projection
        # must contain only the direct Verdier namespace/receipt/tool paths.
        # Checking both directions prevents an arbitrary path from being hidden
        # by a conflict resolution or parent ordering.
        verdier_changes = core.committed_path_changes(source, verdier_parent, cursor)
        verdier_statuses = check_changes(
            verdier_changes,
            f"post-composition merge {cursor} against Verdier parent",
            lambda path: verdier_path_allowed(path)
            or path in CURRENT_MAIN_ALLOWED_PATHS,
        )
        current_main_changes = core.committed_path_changes(
            source, CURRENT_MAIN_PARENT_COMMIT, cursor
        )
        current_main_statuses = check_changes(
            current_main_changes,
            f"post-composition merge {cursor} against current-main parent",
            lambda path: verdier_path_allowed(path),
        )
        merge_row = {
            "commit": cursor,
            "parent": verdier_parent,
            "parents": list(parents),
            "parent_order": ["current_main", "verdier"],
            "topology": "known_current_main_merge",
            "tree": commit_tree(source, cursor),
            "changed_paths": sorted(verdier_changes),
            "statuses": verdier_statuses,
            "current_main_changed_paths": sorted(current_main_changes),
            "current_main_statuses": current_main_statuses,
            "current_main_parent": {
                "commit": CURRENT_MAIN_PARENT_COMMIT,
                "tree": CURRENT_MAIN_PARENT_TREE,
            },
        }
        reverse_rows.append(merge_row)
        cursor = verdier_parent

    require(
        cursor == composition_commit,
        "post-composition Verdier ancestry does not end at the composition commit",
    )
    suffix = list(reversed(reverse_rows))
    return suffix


def summarize_current_main_parent(
    suffix: list[dict[str, object]],
) -> dict[str, object]:
    """Return the receipt binding for the optional exact integration parent."""
    merges = [
        row
        for row in suffix
        if row.get("topology") == "known_current_main_merge"
    ]
    require(len(merges) <= 1, "current-main parent appears in multiple merge rows")
    for row in merges:
        binding = row.get("current_main_parent")
        require(
            binding
            == {"commit": CURRENT_MAIN_PARENT_COMMIT, "tree": CURRENT_MAIN_PARENT_TREE},
            "post-composition current-main parent binding is not exact",
        )
        require(
            row.get("parent_order") == ["current_main", "verdier"]
            and row.get("parents", [None])[0] == CURRENT_MAIN_PARENT_COMMIT,
            "post-composition merge parent order is not current-main-first",
        )
    return {
        "optional": True,
        "observed": bool(merges),
        "commit": CURRENT_MAIN_PARENT_COMMIT,
        "tree": CURRENT_MAIN_PARENT_TREE,
        "merge_commits": [row["commit"] for row in merges],
    }


def validate_current_v4_composition_receipt(
    source: Path, composition_commit: str
) -> dict[str, object]:
    """Bind the current v4 composition receipt without trusting its prose."""
    identity = commit_file_identity(source, "HEAD", COMPOSITION_RECEIPT_PATH)
    receipt = strict_json_bytes(
        commit_bytes(source, "HEAD", COMPOSITION_RECEIPT_PATH),
        "current v4 composition receipt",
    )
    require(
        receipt.get("schema") == core.COMPOSITION_SCHEMA_V4
        and receipt.get("status") == "PASS",
        "current composition receipt is not a passing v4 receipt",
    )
    require(
        receipt.get("required_build_stems") == list(REQUIRED_STEMS),
        "current v4 composition receipt does not bind the exact 30-stem profile",
    )
    composition = receipt.get("composition")
    require(isinstance(composition, dict), "current v4 composition state is malformed")
    assert isinstance(composition, dict)
    require(
        composition.get("source_commit") == composition_commit
        and composition.get("new_operations") == 1
        and composition.get("changed_paths") == [DERIVED_PATH],
        "current v4 composition receipt source binding is invalid",
    )
    affected = composition.get("affected_sources")
    require(
        isinstance(affected, dict) and set(affected) == {DERIVED_PATH},
        "current v4 composition receipt affected-source scope is invalid",
    )
    row = affected[DERIVED_PATH]
    require(
        isinstance(row, dict)
        and row.get("composed_bytes") == POSTIMAGE_BYTES
        and str(row.get("composed_sha256", "")).upper() == POSTIMAGE_SHA256,
        "current v4 composition receipt postimage binding is invalid",
    )
    return {
        "path": COMPOSITION_RECEIPT_PATH,
        "bytes": identity["bytes"],
        "sha256": identity["sha256"],
        "git_blob": identity["git_blob"],
        "schema": receipt["schema"],
        "status": receipt["status"],
        "composition_source_commit": composition_commit,
    }


def validate_source_checkpoint(
    source: Path,
    requested: Path,
    current_main_parent: dict[str, object] | None = None,
) -> dict[str, object]:
    """Bind the sealed EGA checkpoint while building its later descendant.

    ``core.load_source_checkpoint`` deliberately targets the original EGA
    source worktree, where the receipt is the single child of the content
    commit.  This Verdier branch is later than that child (and intentionally
    has a different v4 composition receipt), so invoking that loader against
    the live branch would conflate two topologies.  Recheck the immutable
    historical receipt and its producer identities here, then bind the exact
    receipt child as an ancestor of the current direct Verdier head.  When the
    planned current-main-first integration merge is present, retain the EGA
    protected-input contract and record the one exact ``simplicial.tex``
    parent-side override rather than weakening protection globally.
    """
    core.require_canonical_source_checkpoint_argument(source, requested)
    candidate = requested if requested.is_absolute() else source / requested
    candidate = candidate.resolve()
    try:
        logical = candidate.relative_to(source).as_posix()
    except ValueError as exc:
        raise RuntimeError("source checkpoint must be inside the source worktree") from exc
    require(logical == EGA_SOURCE_CHECKPOINT_PATH, "source checkpoint path is not canonical")
    original = requested if requested.is_absolute() else source / requested
    require(not original.is_symlink(), "source checkpoint must be a regular file")
    require(candidate.is_file(), f"source checkpoint is missing: {logical}")
    require(
        core.git_optional(source, "ls-files", "--error-unmatch", "--", logical)
        == logical,
        f"source checkpoint is not tracked: {logical}",
    )
    core.require_clean_path(source, logical)

    raw = candidate.read_bytes()
    identity = commit_file_identity(source, "HEAD", logical)
    require(
        identity["bytes"] == EGA_SOURCE_CHECKPOINT_BYTES
        and identity["sha256"] == EGA_SOURCE_CHECKPOINT_SHA256
        and identity["git_blob"] == EGA_SOURCE_CHECKPOINT_BLOB,
        "tracked EGA source checkpoint identity is not the sealed receipt",
    )
    require(
        len(raw) == identity["bytes"]
        and sha256_bytes(raw) == identity["sha256"],
        "working EGA source checkpoint bytes differ from the sealed receipt",
    )
    checkpoint = strict_json_bytes(raw, "EGA source checkpoint")
    require(
        set(checkpoint) == set(core.EGA_CHECKPOINT_KEYS),
        "EGA source checkpoint does not match the exact producer schema",
    )
    require(
        checkpoint.get("schema") == core.EGA_SOURCE_CHECKPOINT_SCHEMA
        and checkpoint.get("status") == core.EGA_SOURCE_CHECKPOINT_STATUS,
        "EGA source checkpoint schema or status is invalid",
    )
    require(
        checkpoint.get("checks") == list(EGA_SOURCE_CHECKPOINT_CHECKS),
        "EGA source checkpoint producer check inventory is not exact",
    )
    require(
        checkpoint.get("validation_scope")
        == {
            "source_and_review_checkpoint": "PASS",
            "tex_pdf_build": "NOT_CLAIMED_HERE",
            "visual_qa": "NOT_CLAIMED_HERE",
            "publication": "NOT_CLAIMED_HERE",
            "anonymous_public_readback": "NOT_CLAIMED_HERE",
        },
        "EGA source checkpoint validation scope is untruthful",
    )

    base = checkpoint.get("base")
    content = checkpoint.get("content")
    require(
        isinstance(base, dict)
        and set(base) == {"commit", "tree"}
        and isinstance(content, dict)
        and set(content) == {"commit", "tree", "parent"},
        "EGA source checkpoint base/content binding is malformed",
    )
    assert isinstance(base, dict)
    assert isinstance(content, dict)
    base_commit = core.require_commit_object(source, base.get("commit"), "EGA checkpoint base")
    base_tree = core.require_tree_identity(
        source, base_commit, base.get("tree"), "EGA checkpoint base"
    )
    content_commit = core.require_commit_object(
        source, content.get("commit"), "EGA checkpoint content"
    )
    content_tree = core.require_tree_identity(
        source, content_commit, content.get("tree"), "EGA checkpoint content"
    )
    require(
        base_commit == "57efc9c91e7e52cdb70deb56c0e92f4c93037ac9"
        and base_tree == "f77e75e1e89508b648611890c90e2238a5cdf25e"
        and content_commit == EGA_SOURCE_CHECKPOINT_CONTENT_COMMIT
        and content_tree == EGA_SOURCE_CHECKPOINT_CONTENT_TREE
        and content.get("parent") == base_commit,
        "EGA source checkpoint historical base/content identity drifted",
    )
    core.require_single_parent(source, content_commit, "EGA checkpoint content", base_commit)

    generated = checkpoint.get("generated_from_content_commit_utc")
    expected_generated = core.git(source, "show", "-s", "--format=%cI", content_commit)
    require(
        generated == expected_generated,
        "EGA source checkpoint generation timestamp is not content-bound",
    )

    source_unit = checkpoint.get("source_unit")
    require(
        source_unit
        == {
            "name": "EGA I 6.6.4",
            "next_source_unit": "EGA I 6.6.5",
            "label": "lemma-quasi-compact-preserved-base-change",
            "official_tag": "01K5",
            "dependencies": ["01K4", "01JS"],
        },
        "EGA source checkpoint source-unit identity is not exact",
    )
    root_change = checkpoint.get("root_change")
    require(
        isinstance(root_change, dict)
        and root_change.get("path") == "schemes.tex"
        and root_change.get("label") == source_unit["label"]
        and root_change.get("official_tag") == source_unit["official_tag"],
        "EGA source checkpoint root-change binding is invalid",
    )

    # The source checkpoint JSON deliberately does not self-embed a receipt
    # identity; its repository-state contract only describes the required
    # relation.  Bind that relation to the known checked-in receipt child and
    # verify the child directly from Git objects.
    receipt_commit = core.require_commit_object(
        source, EGA_SOURCE_CHECKPOINT_RECEIPT_COMMIT, "EGA checkpoint receipt child"
    )
    receipt_tree = core.require_tree_identity(
        source,
        receipt_commit,
        EGA_SOURCE_CHECKPOINT_RECEIPT_TREE,
        "EGA checkpoint receipt child",
    )
    require(
        receipt_commit == EGA_SOURCE_CHECKPOINT_RECEIPT_COMMIT
        and receipt_tree == EGA_SOURCE_CHECKPOINT_RECEIPT_TREE,
        "EGA source checkpoint receipt-child identity drifted",
    )
    core.require_single_parent(source, receipt_commit, "EGA checkpoint receipt child", content_commit)
    receipt_changes = core.committed_path_changes(source, content_commit, receipt_commit)
    require(
        list(receipt_changes) == [logical]
        and receipt_changes[logical][4] == "A",
        "EGA source checkpoint receipt child is not the exact receipt-only addition",
    )
    current_head = core.git(source, "rev-parse", "HEAD")
    core.require_ancestor(
        source, receipt_commit, "historical EGA checkpoint receipt", current_head
    )
    receipt_at_anchor = commit_file_identity(source, receipt_commit, logical)
    require(
        receipt_at_anchor["bytes"] == identity["bytes"]
        and receipt_at_anchor["sha256"] == identity["sha256"]
        and receipt_at_anchor["git_blob"] == identity["git_blob"],
        "current branch does not preserve the sealed EGA checkpoint bytes",
    )

    repository_contract = checkpoint.get("repository_state_contract")
    expected_allowed = [{"path": logical, "change": "added"}]
    require(
        repository_contract
        == {
            "content_commit": content_commit,
            "content_tree": content_tree,
            "required_head_relation": core.EGA_HEAD_RELATION,
            "allowed_changes": expected_allowed,
            "validated": True,
        },
        "EGA source checkpoint repository-state contract drifted",
    )
    require(
        checkpoint.get("post_content_metadata_contract")
        == {"allowed_changes": expected_allowed, "source_drift": False},
        "EGA source checkpoint metadata contract drifted",
    )

    # The declared producer and its tests must still identify the exact blobs
    # at the historical base/content commits.  We intentionally do not demand
    # that later Verdier tool repairs retain those old bytes at current HEAD.
    tooling = checkpoint.get("tooling")
    require(
        isinstance(tooling, dict)
        and set(tooling) == {"writer", "tests"}
        and isinstance(tooling.get("writer"), dict)
        and isinstance(tooling.get("tests"), list)
        and len(tooling["tests"]) == 1,
        "EGA source checkpoint tooling inventory is malformed",
    )
    assert isinstance(tooling, dict)
    declared_tools = [tooling["writer"], *tooling["tests"]]
    for declared, expected_path in zip(
        declared_tools,
        (core.EGA_SOURCE_CHECKPOINT_WRITER, core.EGA_SOURCE_CHECKPOINT_WRITER_TEST),
    ):
        require(
            isinstance(declared, dict)
            and set(declared)
            == {
                "path", "bytes", "sha256", "git_blob", "committed_at_base",
                "committed_at_content", "unchanged",
            }
            and declared.get("path") == expected_path
            and declared.get("committed_at_base") is True
            and declared.get("committed_at_content") is True
            and declared.get("unchanged") is True,
            f"EGA source checkpoint producer identity is malformed: {expected_path}",
        )
        base_identity = commit_file_identity(source, base_commit, expected_path)
        content_identity = commit_file_identity(source, content_commit, expected_path)
        require(
            all(
                declared.get(key) == base_identity[key]
                for key in ("bytes", "sha256", "git_blob")
            )
            and content_identity == base_identity,
            f"EGA source checkpoint producer bytes drifted: {expected_path}",
        )

    changed = checkpoint.get("changed_paths")
    require(
        isinstance(changed, list)
        and [row.get("path") for row in changed if isinstance(row, dict)]
        == sorted(core.EGA_CHANGED_PATH_ROLES),
        "EGA source checkpoint changed-path inventory is not exact",
    )
    for row in changed:
        require(isinstance(row, dict) and set(row) == {"path", "change", "base", "content"},
                "EGA source checkpoint changed-path row is malformed")
        assert isinstance(row, dict)
        path = str(row["path"])
        require(path in core.EGA_CHANGED_PATH_ROLES, f"unexpected EGA changed path: {path}")
        actual = core.committed_file_identity(source, content_commit, path)
        require(actual is not None, f"EGA changed path is absent at content: {path}")
        require(row["content"] == {key: actual[key] for key in ("bytes", "sha256", "git_blob")},
                f"EGA content identity mismatch: {path}")
        if row["change"] == "modified":
            before = core.committed_file_identity(source, base_commit, path)
            require(before is not None and row["base"] == {
                key: before[key] for key in ("bytes", "sha256", "git_blob")
            }, f"EGA base identity mismatch: {path}")
        else:
            require(row["change"] == "added" and row["base"] is None,
                    f"EGA changed-path class mismatch: {path}")

    unchanged = checkpoint.get("unchanged_surfaces")
    require(
        isinstance(unchanged, dict)
        and set(unchanged)
        == {"other_root_tex", "tags_tree", "tags_file", "registry_tree", "composition_receipt"},
        "EGA unchanged-surface inventory is malformed",
    )
    assert isinstance(unchanged, dict)
    composition_record = unchanged["composition_receipt"]
    require(
        isinstance(composition_record, dict)
        and composition_record.get("path") == COMPOSITION_RECEIPT_PATH
        and composition_record.get("unchanged") is True,
        "EGA checkpoint composition-reference binding is invalid",
    )
    assert isinstance(composition_record, dict)
    for commit, field in ((base_commit, "base"), (content_commit, "content")):
        comp_identity = commit_file_identity(source, commit, COMPOSITION_RECEIPT_PATH)
        declared = composition_record.get(field)
        require(
            isinstance(declared, dict)
            and declared == {key: comp_identity[key] for key in ("bytes", "sha256", "git_blob")},
            f"EGA checkpoint composition-reference identity mismatch at {field}",
        )
    registry_record = unchanged["registry_tree"]
    require(
        isinstance(registry_record, dict)
        and registry_record.get("path") == "ai-integrated/registry"
        and registry_record.get("unchanged") is True,
        "EGA checkpoint registry preservation binding is invalid",
    )
    assert isinstance(registry_record, dict)
    for commit, field in ((base_commit, "base_git_tree"), (content_commit, "content_git_tree")):
        tree = core.git(source, "rev-parse", f"{commit}:ai-integrated/registry")
        require(registry_record.get(field) == tree, f"EGA checkpoint registry tree mismatch: {field}")
    require(
        registry_record.get("base_git_tree") == registry_record.get("content_git_tree"),
        "EGA checkpoint registry changed across its content step",
    )

    current_main_inputs = validate_current_main_build_input_overrides(
        source, current_main_parent
    )
    override_rows = current_main_inputs.get("paths")
    require(isinstance(override_rows, list), "current-main input override inventory is malformed")
    assert isinstance(override_rows, list)
    applied_current_main_paths = {
        str(row["path"])
        for row in override_rows
        if isinstance(row, dict)
        and set(row)
        == {"path", "from", "r39", "to", "direction", "exact", "applied"}
        and row.get("direction") == "checkpoint_content_to_current_main"
        and row.get("exact") is True
        and row.get("applied") is True
    }
    # Keep a compact, deterministic inventory of every root input protected by
    # the EGA checkpoint.  ``derived.tex`` is intentionally omitted because
    # the bound Verdier composition is its explicit post-content change; the
    # only other permitted deviation is the exact current-main simplicial
    # override above.
    protected_paths = tuple(
        dict.fromkeys(
            [
                "preamble.tex",
                "chapters.tex",
                "my.bib",
                *(f"{stem}.tex" for stem in REQUIRED_STEMS if stem != "derived"),
                *(path for path in root_shared_inputs(source) if path != DERIVED_PATH),
            ]
        )
    )
    protected_lines: list[str] = []
    for path in protected_paths:
        historical = core.committed_file_identity(source, content_commit, path)
        current = core.committed_file_identity(source, "HEAD", path)
        require(
            historical is not None and current is not None,
            f"EGA protected build input is absent: {path}",
        )
        assert isinstance(historical, dict)
        assert isinstance(current, dict)
        if path in applied_current_main_paths:
            expected = next(
                row["to"]
                for row in override_rows
                if isinstance(row, dict)
                and row.get("path") == path
                and row.get("applied") is True
            )
            require(
                isinstance(expected, dict)
                and set(expected) == {"commit", "path", "bytes", "sha256", "git_blob"},
                f"current-main override identity is malformed: {path}",
            )
            assert isinstance(expected, dict)
            require(
                current
                == {key: expected[key] for key in ("path", "bytes", "sha256", "git_blob")},
                f"current-main protected-input override is not exact: {path}",
            )
            source_role = "current_main_override"
        else:
            require(
                current == historical,
                f"EGA protected build input drifted after the checkpoint: {path}",
            )
            source_role = "ega_content"
        core.require_clean_path(source, path)
        working = core.working_file_identity(source, path)
        require(
            all(working[key] == current[key] for key in ("bytes", "sha256")),
            f"working protected build input differs: {path}",
        )
        protected_lines.append(
            "|".join(
                (
                    path,
                    source_role,
                    str(current["bytes"]),
                    str(current["sha256"]),
                    str(current["git_blob"]),
                )
            )
        )

    writer = tooling["writer"]
    assert isinstance(writer, dict)
    return {
        "schema": checkpoint["schema"],
        "status": checkpoint["status"],
        "path": logical,
        "bytes": identity["bytes"],
        "sha256": identity["sha256"],
        "git_blob": identity["git_blob"],
        "historical_base": {"commit": base_commit, "tree": base_tree},
        "historical_content": {
            "commit": content_commit,
            "tree": content_tree,
            "parent": base_commit,
        },
        "historical_receipt_child": {
            "commit": receipt_commit,
            "tree": receipt_tree,
            "changed_paths": [logical],
        },
        "producer": {
            "path": writer["path"],
            "bytes": writer["bytes"],
            "sha256": writer["sha256"],
            "git_blob": writer["git_blob"],
        },
        "descends_from_historical_receipt": True,
        "current_head": current_head,
        "protected_build_inputs": {
            "count": len(protected_lines),
            "tuple_set_sha256": sha256_bytes(
                (("\n".join(sorted(protected_lines))) + "\n").encode("utf-8")
            ),
        },
        "current_main_build_input_overrides": current_main_inputs,
        "checks": [
            "exact_tracked_checkpoint_bytes_and_git_identity",
            "sealed_producer_schema_status_and_check_inventory",
            "historical_base_content_receipt_topology",
            "historical_producer_and_changed_path_identities",
            "historical_composition_and_registry_preservation",
            "known_current_main_input_override_bound_if_present",
            "all_current_build_inputs_rebound_or_exactly_preserved",
            "historical_receipt_is_ancestor_of_current_direct_head",
        ],
    }


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


def validate_current_main_build_input_overrides(
    source: Path,
    current_main_parent: dict[str, object] | None,
) -> dict[str, object]:
    """Bind the narrow root-input delta carried by the known main parent."""
    observed = bool(current_main_parent and current_main_parent.get("observed"))
    expected_parent = {
        "optional": True,
        "observed": observed,
        "commit": CURRENT_MAIN_PARENT_COMMIT,
        "tree": CURRENT_MAIN_PARENT_TREE,
    }
    if current_main_parent is not None:
        require(
            all(current_main_parent.get(key) == value for key, value in expected_parent.items()),
            "current-main build-input parent binding is not exact",
        )
    overrides: list[dict[str, object]] = []
    for path in CURRENT_MAIN_BUILD_INPUT_PATHS:
        r39 = commit_file_identity(source, PUBLIC_R39_COMMIT, path)
        checkpoint_content = commit_file_identity(
            source, EGA_SOURCE_CHECKPOINT_CONTENT_COMMIT, path
        )
        main = commit_file_identity(source, CURRENT_MAIN_PARENT_COMMIT, path)
        require(
            checkpoint_content == r39
            and r39["git_blob"] == CURRENT_MAIN_R39_BUILD_INPUT_BLOBS[path]
            and main["git_blob"] == CURRENT_MAIN_BUILD_INPUT_BLOBS[path]
            and r39["git_blob"] != main["git_blob"],
            f"known current-main build-input identity drifted: {path}",
        )
        if observed:
            head = commit_file_identity(source, "HEAD", path)
            require(
                head == main,
                f"merged HEAD does not preserve the known current-main input: {path}",
            )
        overrides.append(
            {
                "path": path,
                "from": {
                    "commit": EGA_SOURCE_CHECKPOINT_CONTENT_COMMIT,
                    **checkpoint_content,
                },
                "r39": r39,
                "to": {
                    "commit": CURRENT_MAIN_PARENT_COMMIT,
                    **main,
                },
                "direction": "checkpoint_content_to_current_main",
                "exact": True,
                "applied": observed,
            }
        )
    return {
        "schema": "unofficial-ai-integrated-stacks-current-main-input-override/v1",
        "parent": expected_parent,
        "paths": overrides,
    }


def validate_composition(
    source: Path,
    precomposition_commit: str,
    composition_commit: str,
    current_main_parent: dict[str, object] | None = None,
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
    # byte-identical to public R39 except for the one explicitly bound
    # current-main simplicial.tex override and the derived.tex insertion;
    # post-composition tool commits must preserve that entire input set.
    current_main_inputs = validate_current_main_build_input_overrides(
        source, current_main_parent
    )
    override_rows = current_main_inputs.get("paths")
    require(isinstance(override_rows, list), "current-main input override inventory is malformed")
    assert isinstance(override_rows, list)
    applied_current_main_paths = {
        str(row["path"])
        for row in override_rows
        if isinstance(row, dict) and row.get("applied") is True
    }
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
            # The historical Verdier commits intentionally retain the R39
            # preimage.  The exact current-main override is introduced only
            # by the integration merge at HEAD; do not retroactively claim it
            # was present in precomposition or composition.
            expected_blob = (
                CURRENT_MAIN_BUILD_INPUT_BLOBS[relative]
                if revision == "HEAD" and relative in applied_current_main_paths
                else baseline_blob
            )
            observed = core.git(source, "rev-parse", f"{revision}:{relative}")
            require(
                observed == expected_blob,
                (
                    "non-Verdier build input changed after its bound baseline: "
                    f"{label}:{relative}"
                ),
            )
        unchanged_lines.append(f"{relative}|{expected_blob}")

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
        "current_main_build_input_overrides": current_main_inputs,
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
        EGA_SOURCE_CHECKPOINT_PATH,
        FINALIZER_PATH,
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
    parser.add_argument(
        "--source-checkpoint",
        type=Path,
        default=Path(EGA_SOURCE_CHECKPOINT_PATH),
        help=(
            "canonical tracked EGA source checkpoint (default: %(default)s); "
            "the sealed historical receipt is validated before the descendant build"
        ),
    )
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
    postcomposition_suffix = validate_postcomposition_suffix(
        source, args.composition_commit
    )
    current_main_parent = summarize_current_main_parent(postcomposition_suffix)
    v4_composition_receipt = validate_current_v4_composition_receipt(
        source, args.composition_commit
    )
    candidate = validate_candidate(source, args.precomposition_commit, args.composition_commit)
    registries = validate_registries(
        source, args.precomposition_commit, args.composition_commit, candidate
    )
    composition = validate_composition(
        source,
        args.precomposition_commit,
        args.composition_commit,
        current_main_parent,
    )
    source_checkpoint = validate_source_checkpoint(
        source, args.source_checkpoint, current_main_parent
    )
    require_clean_inputs(source)
    release_validation = run_release_validator(source)

    artifacts, build, versions, _, _ = build_once(
        source, args.max_sweeps, args.source_date_epoch
    )
    build["worktree_kind"] = kind
    build["primary_worktree_override"] = args.allow_primary_worktree
    core.require_source_revision_unchanged(source, initial_commit, initial_tree)
    source_checkpoint_after = validate_source_checkpoint(
        source, args.source_checkpoint, current_main_parent
    )
    require(
        source_checkpoint_after == source_checkpoint,
        "EGA source checkpoint identity changed during the build",
    )
    source_checkpoint = {
        **source_checkpoint,
        "build_recheck": {
            "before_current_head": source_checkpoint["current_head"],
            "after_current_head": source_checkpoint_after["current_head"],
            "exact_binding_equal": True,
        },
    }
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
        "postcomposition_suffix": postcomposition_suffix,
        "known_current_main_parent": current_main_parent,
        "v4_composition_receipt": v4_composition_receipt,
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
        "source_checkpoint": source_checkpoint,
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
        args.source_checkpoint,
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
