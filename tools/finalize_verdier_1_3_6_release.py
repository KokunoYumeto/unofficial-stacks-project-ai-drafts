#!/usr/bin/env python3
"""Finalize the direct-prefixed Verdier II.1.3.6 GitHub release.

The program is a narrow receipt generator/checker.  It does not build TeX,
perform network requests, publish, or read credentials.  Pre-publication mode
binds the exact content head and records public readback as pending.  Published
mode accepts only the sanitized receipt emitted by
``verify_github_commit_readback.py`` and verifies every changed leaf against
the exact local Git objects before recording publication as complete.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import stat
import subprocess
import sys
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any, Mapping, Sequence


SCHEMA = "unofficial-ai-integrated-stacks-verdier-1-3-6-final-release/v1"
COMPOSITION_SCHEMA = "unofficial-ai-integrated-stacks-composition/v4"
BUILD_SCHEMA = "unofficial-ai-integrated-stacks-fixed-point-build/v1"
REPRO_SCHEMA = "unofficial-ai-integrated-stacks-clean-build-reproducibility/v1"
VISUAL_SCHEMA = "unofficial-ai-integrated-stacks-visual-qa/v1"
READBACK_SCHEMA = "unofficial-ai-integrated-stacks-github-commit-readback/v1"
DIRECT_SCHEMA = "unofficial-ai-integrated-stacks-verdier-1-3-6-direct-composition/v1"

REPOSITORY = "KokunoYumeto/unofficial-stacks-project-ai-drafts"
# The insertion contract is frozen against public R39.  The eventual release
# readback, however, is compared with the exact current-main tip that is the
# first parent of the planned integration merge.  Keep these identities
# separate so a newer main-side delta cannot rewrite the historical contract.
HISTORICAL_PUBLIC_BASE = "f73b18165c7162b8386de06cc3c50bd4ced745b6"
HISTORICAL_PUBLIC_BASE_TREE = "5bc25c775349eddf5fa90a7f37f5b11044d89ec1"
PUBLIC_BASE = "e083b71ac21e0ecb7508aa6a1067a1b0016d89a7"
PUBLIC_BASE_TREE = "ea6837e424feda8f9e020b5b3083a503ca7247fb"
CURRENT_MAIN_PARENT = PUBLIC_BASE
CURRENT_MAIN_PARENT_TREE = PUBLIC_BASE_TREE
PRECOMPOSITION = "f5de2fe95ccdf2210379f3eca9edc89673adaa71"
PRECOMPOSITION_TREE = "898f5f83620cfbe757663bb345d150459067c3af"
COMPOSITION = "fa8bcf45a189bc3db3ef15fb86c76a8f11f102ea"
COMPOSITION_TREE = "12d470a05dfe68e59a5d671bf98ab6ac7bcae470"
ADMISSION = "d78483415a984eb7b46ad57b6056d8f718e3f395"
ADMISSION_TREE = "15c4126b285fb4cd31469c7ec8bc6c7b7563a0f6"
RIGHTS_CORRECTION = "0b87e200955ef6f335607a8299d0c3aec3ab1b2a"
RIGHTS_CORRECTION_TREE = "d67e93541029b323d5235a240f05129068981b39"
CLOSURE_CORRECTION = "d5cc67f2f636ef4f6a415159f0282dbd472e83b7"
CLOSURE_CORRECTION_TREE = "c93890ac7c15e04e8cc10e9fcdce4db996008315"
# Immutable single-parent Verdier preparation chain.  Checking these parent
# links prevents a similarly named but unrelated commit from satisfying the
# later composition/registry bindings.
VERDIER_PREPARATION_CHAIN = (
    HISTORICAL_PUBLIC_BASE,
    "601f00d17f49edaa58abf20e572941434b72bb86",
    "ec0a80d418d8fa44c1b9fa077fcec8fe9f88c9df",
    "52eccb5772831e4bd17f9d4306b1ad0f60dec43f",
    "8f95214f9275cdc698f0c9bf5e7e8e5784772977",
    ADMISSION,
    "85500f2243acb39e24ff16505e3f9f520543c8e1",
    RIGHTS_CORRECTION,
    "8cae9e123b715c4b363113ce7887b22099dafe42",
    CLOSURE_CORRECTION,
    "aa506aa6008fb42dbf83fc85082b719c0f69bace",
    PRECOMPOSITION,
    COMPOSITION,
)

CANDIDATE_ID = "stacks-verdier-a04446e-1-3-6-r1"
NAMESPACE = "commons/stacks/verdier-ast239-1-3-6-r1"
LEASE_ID = "stacks-lease-000044-verdier-ast239-1-3-6-r1"
OPERATION_ID = "VDR-STK-COMP-0002"
CANDIDATE = f"ai-integrated/candidates/{NAMESPACE}"
MANIFEST_PATH = f"{CANDIDATE}/candidate.manifest.json"
PAYLOAD_PATH = f"{CANDIDATE}/payload/fragments/derived-homotopy-category-abelian-split.tex"
OPERATION_PATH = f"{CANDIDATE}/composition.jsonl"
OVERLAYS_PATH = "ai-integrated/registry/overlays.json"
LEASES_PATH = "ai-integrated/registry/leases.json"
COMPOSITION_PATH = "validation/composition-current.json"
DERIVED_PATH = "derived.tex"
EGA_SOURCE_CHECKPOINT_PATH = "validation/ega-i-6.6.4-source-checkpoint-2026-08-31.json"
EGA_SOURCE_CHECKPOINT_SCHEMA = "unofficial-stacks-project-ai-drafts-ega-source-checkpoint/v1"
EGA_SOURCE_CHECKPOINT_STATUS = "PASS_SOURCE_CHECKPOINT"
EGA_SOURCE_CHECKPOINT_BYTES = 44426
EGA_SOURCE_CHECKPOINT_SHA256 = "95B8D2B14D7C1CB7E9F826F6EBF0A6723DBDB05DC5D06F06F186E21465CC3352"
EGA_SOURCE_CHECKPOINT_BLOB = "715024558f8480811dc3d27521d65cdaa893ca45"
EGA_BASE_COMMIT = "57efc9c91e7e52cdb70deb56c0e92f4c93037ac9"
EGA_BASE_TREE = "f77e75e1e89508b648611890c90e2238a5cdf25e"
EGA_CONTENT_COMMIT = "571648f5c43c36617629c8ae57b28606d966625f"
EGA_CONTENT_TREE = "12faacf779ad018c4c2729167d1afa1ef6b9d0e5"
EGA_RECEIPT_COMMIT = "91cc89df5804b8c1949d8267602fc076649ee49b"
EGA_RECEIPT_TREE = "060538ea3323b366e8f445fd79725a63c4241d2f"
EGA_SOURCE_CHECKPOINT_CHECKS = (
    "exact_tracked_checkpoint_bytes_and_git_identity",
    "sealed_producer_schema_status_and_check_inventory",
    "historical_base_content_receipt_topology",
    "historical_producer_and_changed_path_identities",
    "historical_composition_and_registry_preservation",
    "known_current_main_input_override_bound_if_present",
    "all_current_build_inputs_rebound_or_exactly_preserved",
    "historical_receipt_is_ancestor_of_current_direct_head",
)
EGA_SOURCE_CHECKPOINT_KEYS = frozenset({
    "authority", "authority_binding", "base", "changed_paths", "checks", "claim",
    "content", "counts", "generated_from_content_commit_utc", "historical_rebind",
    "inputs", "ledger_appends", "ledger_semantics", "post_content_metadata_contract",
    "readme_change", "repository_state_contract", "root_change", "schema", "scope",
    "source_unit", "status", "tooling", "unchanged_surfaces", "validation_scope",
})
EGA_RAW_CHECKS = (
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

MANIFEST_SHA256 = "C007BBFB1AB068843B7759FF69ED338BE0071349975EDCE20472876B89F01F2F"
MANIFEST_BLOB = "f05fbac8ebe368648dfeb69c053872dc23e3a7ea"
PAYLOAD_SHA256 = "C61FEF90594F0B1C3BD48870452A35C95F7DC85F56C551C0C68F40A01BE8BE9E"
PAYLOAD_BLOB = "21303a3a85b27b0fda2790a61de49f44d76076e1"
PAYLOAD_BYTES = 3673
OPERATION_SHA256 = "C3DD45A0CAF2263EF7FF645F0573AE775112012A681706420DB9A86C47F242D7"
OPERATION_BLOB = "37194587a44312a44f027ba31f000bd71a2d03ac"
BASE_SHA256 = "8B389993D3B364A926C7DCD7AD598E5B8245D8E92BCC5A23646069F9AD617860"
BASE_BYTES = 452054
BASE_BLOB = "f62f8645b22d39a3dd5998256f3a296bcb677d37"
POSTIMAGE_SHA256 = "726404F52F8E9EFD8D091DA3BF0EE9A1B288E6CFCC7A24DAD20ACB92926C62CE"
POSTIMAGE_BLOB = "224b3e76847ef0bfe86e0157a35ef3f735872033"
POSTIMAGE_BYTES = 455727

OVERLAYS_BYTES = 66940
OVERLAYS_SHA256 = "FC5149A28734CBB2FB9AFDA624780194FAA4622A1336D238A94F0BDFEBDA5664"
OVERLAYS_BLOB = "6a09c6a43aa62109681bbb4ee11a46026284b18c"
LEASES_BYTES = 52052
LEASES_SHA256 = "8C12B7B63FD439913DC89F32ABB801BED0FCFD39CD53F14BDB4216A286D698E4"
LEASES_BLOB = "f334e121aeb64d8431d67c55aa065c11bb1e88b4"
AUTHORITY_LOCK_PATH = (
    f"{CANDIDATE}/authority/authority.lock.json"
)
AUTHORITY_LOCK_BYTES = 2602
AUTHORITY_LOCK_SHA256 = "BE5854692B1470F74ABA10B84DD057B0F7D209C23863D40B426904EA2FFABE03"
AUTHORITY_LOCK_BLOB = "36ce2caed7a7513a6956d67c4f74cd1488bbe0ca"
AUTHORITY_PDF_BYTES = 19188423
AUTHORITY_PDF_PAGES = 270
AUTHORITY_PDF_SHA256 = "6214C252BACEBA5584E3C4AEB564C129851941C1A9250BABAB45B79A3939B0AE"
AUTHORITY_MAP_BYTES = 873203
AUTHORITY_MAP_SHA256 = "A9AB660EF7E86ADFD5B517F06D9E50AF1E5C6B785F531E2D20746AF0A42D2927"
AUTHORITY_PAGE_BYTES = 2671
AUTHORITY_PAGE_SHA256 = "01D96DD78685171DB3897E129FC3085A4343AC7297169D60C3FA3C6A9E52C532"
OFFICIAL_COMMIT = "a04446e57ec1fbc252a871afcec7752fb2807b14"
OFFICIAL_TREE = "3feeb703b931a6e7259782c10e7d1575adc83e5e"
WRITER_TASK = "019fca5a-c80e-7890-a46b-4948ff443e6d"
MANIFEST_SCHEMA = "mathematics-commons-stacks-candidate-manifest/v1"
AUTHORITY_SCHEMA = "mathematics-commons-stacks-verdier-authority-lock/v1"
OVERLAY_REGISTRY_SCHEMA = "mathematics-commons-stacks-overlay-registry/v1"
LEASE_REGISTRY_SCHEMA = "mathematics-commons-stacks-lease-registry/v1"
RIGHTS_STATE = (
    "Historical-source evidence is limited to locators, hashes, and independent paraphrase. "
    "No verbatim source prose is included, no source-work license is asserted or granted by "
    "this candidate, and no upstream content is relicensed. The proposed Stacks payload is "
    "independently written, subject to GFDL compatibility at composition, and is not reviewed, "
    "approved, affiliated with, or endorsed by the Stacks Project."
)
AUTHORITY_PAGE_PATH = "content/en/p125.tex"
AUTHORITY_MAP_PATH = "sem/final_four_edition_anchor_map.csv"
REVIEW_RELATIVE = "replay/independent-review.json"
PROPOSED_LABEL = "lemma-homotopy-category-abelian-split"
AUTHORITY_PHYSICAL_PAGE = 125
EXPECTED_LOCUS_PAGES = (36, 37, 38, 39)
INTEGRATION_EXACT_PATHS = frozenset({
    DERIVED_PATH,
    OVERLAYS_PATH,
    LEASES_PATH,
    "tools/build_verdier_1_3_6_fixed_point.py",
    "tools/build_fixed_point.py",
    "tools/validate_verdier_1_3_6_release.py",
    "tools/validate_unified_repository.py",
    "tools/verify_github_commit_readback.py",
    "tools/finalize_verdier_1_3_6_release.py",
    COMPOSITION_PATH,
    "validation/stacks-verdier-a04446e-1-3-6-r1-manifest-closure-correction-2026-09-06.json",
})

STABLE_IDS = (
    "verdier:ast239:1.3.6",
    "verdier:ast239:1.3.6:equivalent-conditions",
    "verdier:ast239:1.3.6:proof:i-iff-ii",
    "verdier:ast239:1.3.6:proof:ii-implies-iii",
    "verdier:ast239:1.3.6:construction:hstar-complex",
    "verdier:ast239:1.3.6:claim:hstar-equivalence",
    "verdier:ast239:1.3.6:conclusion:iii-implies-ii",
)
STEMS = (
    "sets", "categories", "topology", "sheaves", "sites", "algebra",
    "fields", "artin", "brauer", "derived", "simplicial", "homology",
    "more-algebra", "smoothing", "modules", "sites-modules", "schemes",
    "properties", "morphisms", "more-morphisms", "spaces-morphisms",
    "crystalline", "spaces-cohomology", "spaces-duality", "stacks-limits",
    "injectives", "cohomology", "sites-cohomology", "gaga", "moduli",
)

SHA1 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9A-F]{64}$")
DRIVE_PREFIX = re.compile(r"^[A-Za-z]:")
LOCAL_PATH = re.compile(
    r"(?i)(?:(?<![A-Za-z0-9])[A-Za-z]:[\\/]|(?:^|[\s\"'(\[])/(?!/)[A-Za-z0-9._~+-]+|(?:^|[\s\"'(\[])\\\\[^\\\s]+\\[^\\\s]+)"
)
SECRET = re.compile(
    r"(?i)(?:authorization\s*[:=]|bearer\s+[A-Za-z0-9._~+/-]+|access[_ -]?token|api[_ -]?key|client[_ -]?secret|password\s*[:=]|github_pat_[A-Za-z0-9_]+|gh[pousr]_[A-Za-z0-9]+)"
)


class FinalizationError(RuntimeError):
    pass


def require(condition: Any, message: str) -> None:
    if not condition:
        raise FinalizationError(message)


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest().upper()


def blob_id(raw: bytes) -> str:
    try:
        digest = hashlib.sha1(usedforsecurity=False)
    except TypeError:  # pragma: no cover
        digest = hashlib.sha1()
    digest.update(f"blob {len(raw)}\0".encode("ascii"))
    digest.update(raw)
    return digest.hexdigest()


def strict_object(raw: bytes, label: str) -> dict[str, Any]:
    def pairs(rows: list[tuple[str, Any]]) -> dict[str, Any]:
        value: dict[str, Any] = {}
        for key, item in rows:
            require(key not in value, f"{label} repeats JSON key {key!r}")
            value[key] = item
        return value

    def constant(value: str) -> Any:
        raise FinalizationError(f"{label} contains non-finite number {value}")

    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                           parse_constant=constant)
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise FinalizationError(f"invalid UTF-8 JSON: {label}") from exc
    require(isinstance(value, dict), f"JSON object required: {label}")
    return value


def safe_relative(value: str, label: str) -> str:
    require(isinstance(value, str) and value != "", f"empty {label}")
    pure = PurePosixPath(value)
    windows = PureWindowsPath(value)
    require(
        "\\" not in value
        and "\x00" not in value
        and all(ord(char) >= 32 and ord(char) != 127 for char in value)
        and not DRIVE_PREFIX.match(value)
        and not pure.is_absolute()
        and not windows.is_absolute()
        and windows.drive == ""
        and windows.root == ""
        and all(part not in ("", ".", "..") for part in pure.parts)
        and pure.as_posix() == value,
        f"unsafe repository-relative {label}",
    )
    return value


def sanitized(value: Any) -> None:
    serialized = json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False)
    require(LOCAL_PATH.search(serialized) is None, "receipt contains a local absolute path")
    require(SECRET.search(serialized) is None, "receipt contains secret-shaped material")

    def visit(item: Any) -> None:
        if isinstance(item, Mapping):
            for key, child in item.items():
                require(isinstance(key, str), "non-string JSON key")
                visit(key); visit(child)
        elif isinstance(item, list):
            for child in item:
                visit(child)
        elif isinstance(item, float):
            require(math.isfinite(item), "non-finite JSON number")
        elif isinstance(item, str):
            win = PureWindowsPath(item)
            require(not win.is_absolute() and win.drive == "" and win.root == "",
                    "receipt contains an absolute Windows path")
            require(not PurePosixPath(item).is_absolute(),
                    "receipt contains an absolute POSIX path")
            require(not item.casefold().startswith("file:"), "receipt contains file URL")
            if "://" in item:
                require(item.startswith("https://"), "receipt contains non-HTTPS URL")
                require("@" not in item.split("/", 3)[2], "receipt contains credential-bearing URL")
                require("?" not in item and "#" not in item,
                        "receipt contains query or fragment URL")
    visit(value)


def lexical_absolute(path: Path) -> Path:
    """Return an absolute lexical path without following reparse points."""
    raw = os.fspath(path)
    require(isinstance(raw, str) and raw != "", "empty local path")
    # Do not let ``abspath`` normalize away a symlink-bearing ``..`` segment
    # before the component-by-component lstat walk below.
    raw_components = re.split(r"[\\/]", raw)
    require(all(component not in {".", ".."} for component in raw_components),
            "dot segments are not allowed in local paths")
    return Path(os.path.abspath(raw))


def reject_symlink_components(path: Path, label: str, *, allow_missing_leaf: bool = False) -> None:
    """Reject symlinks/reparse links before any path resolution or file read.

    ``Path.resolve()`` erases the evidence that the user supplied a symlink.
    Walk the lexical components with ``lstat`` first, allowing only a missing
    final component when an output is about to be created.
    """
    absolute = lexical_absolute(path)
    parts = absolute.parts
    cursor = Path(absolute.anchor) if absolute.anchor else Path()
    for index, part in enumerate(parts[1:] if absolute.anchor else parts):
        cursor = cursor / part
        try:
            info = os.lstat(os.fspath(cursor))
        except FileNotFoundError:
            require(
                allow_missing_leaf and index == len(parts[1:] if absolute.anchor else parts) - 1,
                f"missing local path component: {label}",
            )
            return
        except OSError as exc:
            raise FinalizationError(f"cannot inspect local path: {label}") from exc
        require(not stat.S_ISLNK(info.st_mode), f"symlink/reparse path is not allowed: {label}")
        reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
        require(not (getattr(info, "st_file_attributes", 0) & reparse_flag),
                f"reparse-point path is not allowed: {label}")
        # Windows junctions are reparse points but are not always reported as
        # POSIX symlinks by Python.  ``is_symlink`` is an additional guard on
        # the exact lexical component; ordinary directories/files remain safe.
        require(not Path(cursor).is_symlink(), f"symlink path is not allowed: {label}")


def same_lexical_path(left: Path, right: Path) -> bool:
    return os.path.normcase(os.path.abspath(os.fspath(left))) == os.path.normcase(
        os.path.abspath(os.fspath(right))
    )


def exact_worktree_root(requested: Path) -> Path:
    """Require the caller's root to be this tool's exact worktree."""
    # ``__file__`` may be relative when invoked as ``python tools/...``;
    # convert it to an absolute lexical path before the strict dot-segment
    # guard runs.  This does not resolve symlinks or reparse points.
    expected = lexical_absolute(Path(__file__).absolute().parent.parent)
    supplied = lexical_absolute(requested)
    reject_symlink_components(expected, "tool worktree root")
    reject_symlink_components(supplied, "requested worktree root")
    require(same_lexical_path(supplied, expected), "--root must be this exact tool worktree")
    try:
        info = os.lstat(os.fspath(supplied))
    except OSError as exc:
        raise FinalizationError("cannot inspect requested worktree root") from exc
    require(stat.S_ISDIR(info.st_mode), "requested worktree root is not a directory")
    return supplied


def exact_validation_path(root: Path, path: Path, logical: str, label: str,
                          *, allow_missing_leaf: bool = False) -> Path:
    """Bind a local evidence/output path to ``root/validation/<logical>``."""
    logical = safe_relative(logical, f"{label} logical path")
    require(logical.startswith("validation/") and logical != "validation/",
            f"{label} must be directly under the validation tree")
    validation_root = lexical_absolute(root / "validation")
    expected = lexical_absolute(root.joinpath(*logical.split("/")))
    supplied_raw = path if path.is_absolute() else root / path
    supplied = lexical_absolute(supplied_raw)
    require(same_lexical_path(expected, supplied),
            f"{label} path is not the exact worktree validation path")
    reject_symlink_components(root, "worktree root")
    reject_symlink_components(validation_root, "validation directory")
    reject_symlink_components(supplied, label, allow_missing_leaf=allow_missing_leaf)
    try:
        validation_info = os.lstat(os.fspath(validation_root))
    except OSError as exc:
        raise FinalizationError("cannot inspect validation directory") from exc
    require(stat.S_ISDIR(validation_info.st_mode), "validation path is not a directory")
    if not allow_missing_leaf:
        try:
            info = os.lstat(os.fspath(supplied))
        except OSError as exc:
            raise FinalizationError(f"cannot inspect {label}") from exc
        require(stat.S_ISREG(info.st_mode), f"{label} is not an ordinary file")
    return supplied


def git(root: Path, arguments: Sequence[str], label: str) -> bytes:
    completed = subprocess.run(["git", "-C", os.fspath(root), *arguments],
                               stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, timeout=60, check=False)
    require(completed.returncode == 0, f"bounded Git query failed: {label}")
    require(len(completed.stdout) <= 32 * 1024 * 1024, f"Git output too large: {label}")
    return completed.stdout


def resolve_commit(root: Path, value: str, expected_tree: str | None = None) -> dict[str, str]:
    require(SHA1.fullmatch(value) is not None, "full lowercase commit required")
    object_type = git(root, ["cat-file", "-t", value], "resolve commit type").decode().strip()
    require(object_type == "commit", "resolved object is not a commit")
    observed = git(root, ["rev-parse", "--verify", f"{value}^{{commit}}"], "resolve commit").decode().strip()
    tree = git(root, ["rev-parse", "--verify", f"{value}^{{tree}}"], "resolve tree").decode().strip()
    require(observed == value and SHA1.fullmatch(tree) is not None, "commit identity mismatch")
    require(git(root, ["cat-file", "-t", tree], "resolve tree type").decode().strip() == "tree",
            "resolved object is not a tree")
    if expected_tree is not None:
        require(tree == expected_tree, "commit tree mismatch")
    return {"commit": value, "tree": tree}


def ancestor(root: Path, older: str, newer: str) -> None:
    completed = subprocess.run(["git", "-C", os.fspath(root), "merge-base",
                                "--is-ancestor", older, newer], stdin=subprocess.DEVNULL,
                               stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                               timeout=60, check=False)
    require(completed.returncode == 0, f"required ancestry failed: {older} -> {newer}")


def commit_parents(root: Path, revision: str) -> list[str]:
    """Return the exact parent list for one resolved commit object."""
    raw = git(root, ["rev-list", "--parents", "-n", "1", revision],
              "read commit parents").decode("ascii", "strict").strip()
    fields = raw.split()
    require(fields and fields[0] == revision and
            all(SHA1.fullmatch(item) is not None for item in fields),
            "malformed commit-parent identity")
    return fields[1:]


def validate_integration_merge(root: Path, content_head: str,
                               allowed_paths: set[str] | None = None) -> dict[str, Any]:
    """Require the bounded current-main-first merge topology.

    The content head may have evidence-only single-parent descendants, but its
    Verdier ancestry must contain exactly one two-parent merge.  Parent one is
    the immutable current-main tip; parent two is the Verdier composition
    lineage.  Walking parent two avoids mistaking unrelated current-main
    history for release changes.
    """
    cursor = content_head
    visited: set[str] = set()
    merge: dict[str, Any] | None = None
    while cursor != COMPOSITION:
        require(cursor not in visited, "content ancestry contains a cycle")
        visited.add(cursor)
        require(len(visited) <= 512, "content ancestry is unreasonably long")
        parents = commit_parents(root, cursor)
        require(parents, "content ancestry terminates before composition")
        if len(parents) == 1:
            cursor = parents[0]
            continue
        require(len(parents) == 2, "content ancestry contains an unsupported merge")
        require(merge is None, "content ancestry contains more than one integration merge")
        first, second = parents
        require(first == CURRENT_MAIN_PARENT,
                "integration merge parent 1 is not the exact current-main tip")
        resolve_commit(root, first, CURRENT_MAIN_PARENT_TREE)
        require(git(root, ["merge-base", first, second], "integration merge base")
                .decode("ascii", "strict").strip() == HISTORICAL_PUBLIC_BASE,
                "integration merge does not have the frozen R39 merge base")
        ancestor(root, COMPOSITION, second)
        merge = {
            "commit": cursor,
            "parents": parents,
            "parent_order": ["current_main", "verdier"],
            "tree": resolve_commit(root, cursor)["tree"],
            "current_main_parent": {
                "commit": CURRENT_MAIN_PARENT,
                "tree": CURRENT_MAIN_PARENT_TREE,
            },
            "verdier_parent": second,
            "merge_base": HISTORICAL_PUBLIC_BASE,
        }
        cursor = second
    require(merge is not None, "content head lacks the required current-main-first integration merge")
    # Recompute the complete release delta against current main and reject any
    # source/registry/artifact path that is not explicitly in the integration
    # allowlist or one of the caller-bound validation evidence paths.
    release_rows, release_diff = changed_leaf_identities(
        root, PUBLIC_BASE, content_head
    )
    candidate_paths = {
        path for path in git(root, ["ls-tree", "-r", "--name-only", PRECOMPOSITION,
                                    "--", CANDIDATE], "candidate integration scope")
        .decode("utf-8", "strict").splitlines()
    }
    require(candidate_paths and all(safe_relative(path, "candidate integration path")
                                   for path in candidate_paths),
            "candidate integration scope is malformed")
    allowed = set(INTEGRATION_EXACT_PATHS) | candidate_paths
    if allowed_paths:
        allowed.update(safe_relative(path, "allowed evidence path") for path in allowed_paths)
    disallowed = [row["path"] for row in release_rows if row["path"] not in allowed]
    require(not disallowed,
            "current-main integration changed unbound paths: " + ", ".join(disallowed))
    return {"merge": merge, "release_diff": release_diff,
            "release_changed_paths": [row["path"] for row in release_rows]}


def committed_raw(root: Path, revision: str, relative: str) -> bytes:
    safe_relative(relative, "path")
    return git(root, ["show", f"{revision}:{relative}"], f"read {relative}")


def local_evidence(root: Path, path: Path, logical: str,
                   content_head: str, require_committed: bool = True) -> tuple[dict[str, Any], dict[str, Any]]:
    safe_path = exact_validation_path(root, path, logical, "evidence")
    raw = safe_path.read_bytes()
    if require_committed:
        require(raw == committed_raw(root, content_head, logical),
                f"evidence differs from content head: {logical}")
    value = strict_object(raw, logical)
    sanitized(value)
    return value, {"path": logical, "bytes": len(raw), "sha256": sha256(raw),
                   "git_blob": blob_id(raw)}


def commit_identity(root: Path, revision: str, relative: str) -> dict[str, Any]:
    raw = committed_raw(root, revision, relative)
    return {"path": relative, "bytes": len(raw), "sha256": sha256(raw),
            "git_blob": blob_id(raw)}


def require_identity(row: Mapping[str, Any], identity: Mapping[str, Any], label: str,
                     path_key: str = "path", *, require_blob: bool = False) -> None:
    if path_key in row:
        require(row.get(path_key) == identity["path"], f"{label} path mismatch")
    for key in ("bytes", "sha256"):
        require(row.get(key) == identity[key], f"{label} {key} mismatch")
    if require_blob:
        require(row.get("git_blob") == identity["git_blob"], f"{label} git_blob mismatch")


def tree_leaf_mode_blob(root: Path, revision: str, relative: str) -> tuple[str, str]:
    """Read exactly one ordinary blob leaf from the resolved commit tree."""
    safe_relative(relative, "Git leaf path")
    raw = git(root, ["ls-tree", "-z", "-r", revision, "--", relative],
              f"read tree leaf {relative}")
    records = raw.split(b"\0")
    require(records[-1] == b"" and len(records) == 2,
            f"Git tree leaf inventory is not singular: {relative}")
    try:
        metadata, path_raw = records[0].split(b"\t", 1)
        mode, kind, object_id = metadata.decode("ascii", "strict").split(" ")
        returned = path_raw.decode("utf-8", "strict")
    except (UnicodeDecodeError, ValueError) as exc:
        raise FinalizationError(f"malformed Git tree leaf: {relative}") from exc
    require(returned == relative and kind == "blob" and mode in {"100644", "100755"},
            f"changed leaf is not an ordinary blob: {relative}")
    require(SHA1.fullmatch(object_id) is not None, f"changed leaf blob is malformed: {relative}")
    return mode, object_id


def changed_leaf_identities(root: Path, base: str, head: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Derive the complete changed-leaf inventory from local Git objects.

    No claim in a readback receipt is used to select paths.  The raw no-renames
    diff is parsed first, then each head tree leaf is independently read and
    hashed.  Deletions, renames, type changes, submodules, and duplicate paths
    fail closed.
    """
    # First derive the path/status set using the same bounded name-status
    # contract as the public readback verifier.  The raw diff below supplies
    # mode/blob identities and is cross-checked against this independent list.
    name_raw = git(root, ["diff-tree", "--no-commit-id", "-r", "--name-status",
                          "--no-renames", "-z", f"{base}..{head}", "--"],
                   "derive changed path/status set")
    name_tokens = name_raw.split(b"\0")
    require(name_tokens[-1] == b"" and len(name_tokens) % 2 == 1,
            "malformed name-status Git diff inventory")
    named: dict[str, str] = {}
    for index in range(0, len(name_tokens) - 1, 2):
        try:
            status = name_tokens[index].decode("ascii", "strict")
            path = name_tokens[index + 1].decode("utf-8", "strict")
        except (UnicodeDecodeError, ValueError) as exc:
            raise FinalizationError("malformed name-status Git diff leaf") from exc
        safe_relative(path, "name-status changed path")
        require(status in {"A", "M"},
                f"name-status inventory contains unsupported status {status}: {path}")
        require(path not in named, f"name-status inventory repeats path: {path}")
        named[path] = status
    require(named, "BASE..HEAD name-status inventory is empty")

    raw = git(root, ["diff", "--raw", "--no-renames", "--no-abbrev", "-z",
                     f"{base}..{head}", "--"],
              "derive changed leaves")
    tokens = raw.split(b"\0")
    require(tokens[-1] == b"" and len(tokens) % 2 == 1,
            "malformed no-renames Git diff inventory")
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index in range(0, len(tokens) - 1, 2):
        header = tokens[index]
        path_raw = tokens[index + 1]
        require(header.startswith(b":"), "malformed Git diff header")
        try:
            fields = header[1:].decode("ascii", "strict").split(" ")
            old_mode, new_mode, old_blob, new_blob, status = fields
            path = path_raw.decode("utf-8", "strict")
        except (UnicodeDecodeError, ValueError) as exc:
            raise FinalizationError("malformed Git diff leaf record") from exc
        safe_relative(path, "changed leaf path")
        require(status in {"A", "M"},
                f"changed inventory contains unsupported status {status}: {path}")
        require(named.get(path) == status,
                f"name-status/raw diff status mismatch: {path}")
        require(path not in seen, f"changed inventory repeats path: {path}")
        seen.add(path)
        require(new_mode in {"100644", "100755"}
                and SHA1.fullmatch(new_blob) is not None,
                f"changed inventory contains non-ordinary head leaf: {path}")
        # The raw diff supplies status; the tree independently supplies mode
        # and object identity, preventing a receipt from smuggling a different
        # mode/blob under the same path.
        tree_mode, tree_blob = tree_leaf_mode_blob(root, head, path)
        require(tree_mode == new_mode and tree_blob == new_blob,
                f"diff/tree identity mismatch: {path}")
        payload = committed_raw(root, head, path)
        require(blob_id(payload) == tree_blob, f"head blob bytes do not match Git object: {path}")
        rows.append({
            "path": path,
            "status": {"A": "added", "M": "modified"}[status],
            "mode": tree_mode,
            "bytes": len(payload),
            "sha256": sha256(payload),
            "git_blob": tree_blob,
        })
    rows.sort(key=lambda row: row["path"])
    require(rows, "BASE..HEAD changed-leaf inventory is empty")
    require(set(named) == {row["path"] for row in rows},
            "name-status/raw diff path sets differ")
    tuple_rows = [{key: row[key] for key in ("path", "status", "mode", "bytes", "sha256", "git_blob")}
                  for row in rows]
    summary = {
        "base": base,
        "head": head,
        "rows": rows,
        "count": len(rows),
        "bytes": sum(row["bytes"] for row in rows),
        "tuple_set_sha256": sha256(canonical(tuple_rows)),
    }
    return rows, summary


def validate_evidence_suffix(root: Path, older: str, newer: str,
                             evidence_paths: set[str]) -> list[dict[str, Any]]:
    """Prove every commit after a build source is an evidence-only child.

    A net ``older..newer`` diff is not enough: an intermediate critical-file
    edit could be reverted before the final head.  Walk each parent edge and
    derive its raw leaf identities independently.  Only direct validation
    evidence files are admitted; source, registry, candidate, composition,
    and tool paths can never be authorized by a caller-supplied argument.
    """
    immutable = {
        DERIVED_PATH, OVERLAYS_PATH, LEASES_PATH, COMPOSITION_PATH,
        EGA_SOURCE_CHECKPOINT_PATH,
        MANIFEST_PATH, PAYLOAD_PATH, OPERATION_PATH, AUTHORITY_LOCK_PATH,
        "tools/build_verdier_1_3_6_fixed_point.py", "tools/build_fixed_point.py",
        "tools/validate_verdier_1_3_6_release.py",
        "tools/finalize_verdier_1_3_6_release.py",
        "tools/validate_unified_repository.py",
        "tools/verify_github_commit_readback.py",
    }
    require(evidence_paths and all(
        isinstance(path, str) and path.startswith("validation/")
        and path not in immutable and safe_relative(path, "evidence path")
        for path in evidence_paths
    ), "evidence suffix paths are not a bounded validation-only set")
    ancestor(root, older, newer)
    if older == newer:
        return []
    rows: list[dict[str, Any]] = []
    cursor = newer
    visited: set[str] = set()
    while cursor != older:
        require(cursor not in visited, "source-to-content ancestry contains a cycle")
        visited.add(cursor)
        require(len(visited) <= 128, "source-to-content evidence suffix is too long")
        parents = commit_parents(root, cursor)
        require(len(parents) == 1,
                "source-to-content evidence suffix contains a merge commit")
        parent = parents[0]
        changes, summary = changed_leaf_identities(root, parent, cursor)
        disallowed = sorted(row["path"] for row in changes
                            if row["path"] not in evidence_paths)
        require(not disallowed,
                "source-to-content evidence commit changed unbound paths: "
                + ", ".join(disallowed))
        rows.append({"commit": cursor, "parent": parent,
                     "tree": resolve_commit(root, cursor)["tree"],
                     "changed_paths": [row["path"] for row in changes],
                     "changed_leaf_summary": summary})
        cursor = parent
    return list(reversed(rows))


def committed_json(root: Path, revision: str, relative: str,
                   label: str) -> tuple[dict[str, Any], dict[str, Any]]:
    raw = committed_raw(root, revision, relative)
    value = strict_object(raw, label)
    sanitized(value)
    return value, commit_identity(root, revision, relative)


def validate_authority_and_candidate(root: Path) -> dict[str, Any]:
    """Validate the immutable candidate, authority lock, and manifest closure."""
    manifest, manifest_identity = committed_json(root, PRECOMPOSITION, MANIFEST_PATH,
                                                  "candidate manifest")
    require(manifest.get("schema") == MANIFEST_SCHEMA
            and manifest.get("candidate_id") == CANDIDATE_ID
            and manifest.get("lease_id") == LEASE_ID
            and manifest.get("namespace") == NAMESPACE
            and manifest.get("writer_task") == WRITER_TASK,
            "candidate manifest identity mismatch")
    require(manifest.get("upstream") == {
        "lock": "upstream/stacks.lock.json",
        "commit": OFFICIAL_COMMIT,
        "tree": OFFICIAL_TREE,
    }, "candidate manifest upstream binding mismatch")
    require(manifest.get("source_closure") == {
        "enumerated": True, "expected_units": 7,
        "manifested_units": 7, "complete": True,
    }, "candidate manifest source-closure binding mismatch")
    require(manifest.get("rights_state") ==
            "Source locators and hashes only; payload independently worded; no source relicense asserted; GFDL compatibility required at composition.",
            "candidate manifest rights state mismatch")
    require(manifest.get("review_state") == "performed"
            and manifest.get("independent_replay") == "passed"
            and manifest.get("unresolved_defects") == [],
            "candidate manifest review state is not final")

    references: dict[str, str] = {}

    def add_reference(binding: Any, label: str) -> None:
        require(isinstance(binding, Mapping), f"candidate manifest binding is malformed: {label}")
        path = safe_relative(str(binding.get("path", "")), f"{label} path")
        digest = str(binding.get("sha256", ""))
        require(SHA256.fullmatch(digest.upper()) is not None,
                f"candidate manifest hash is malformed: {label}")
        require(path not in references, f"candidate manifest repeats path: {path}")
        references[path] = digest.upper()

    authorities = manifest.get("source_authorities")
    builds = manifest.get("builds")
    require(isinstance(authorities, list) and len(authorities) == 1
            and isinstance(builds, list) and bool(builds),
            "candidate manifest reference inventories are malformed")
    add_reference(authorities[0], "source authority")
    for index, binding in enumerate(builds):
        add_reference(binding, f"build[{index}]")
    for field in ("stable_unit_manifest", "source_map", "decision_ledger",
                  "rejection_ledger", "formula_diagram_inventory"):
        add_reference(manifest.get(field), field)
    require(references.get("authority/authority.lock.json") == AUTHORITY_LOCK_SHA256,
            "candidate manifest does not bind the exact authority lock")
    require(references.get("payload/fragments/derived-homotopy-category-abelian-split.tex")
            == PAYLOAD_SHA256, "candidate manifest does not bind the exact payload")
    require(references.get("composition.jsonl") is not None,
            "candidate manifest does not bind the composition ledger")

    candidate_files = git(root, ["ls-tree", "-r", "--name-only", PRECOMPOSITION,
                                 "--", CANDIDATE], "candidate closure").decode().splitlines()
    expected_files = sorted([MANIFEST_PATH] + [f"{CANDIDATE}/{path}" for path in references])
    require(sorted(candidate_files) == expected_files,
            "candidate subtree is not exactly manifest-closed")
    for relative, expected_hash in references.items():
        full = f"{CANDIDATE}/{relative}"
        identity = commit_identity(root, PRECOMPOSITION, full)
        require(identity["sha256"] == expected_hash,
                f"candidate manifest hash mismatch: {relative}")

    authority, authority_identity = committed_json(root, PRECOMPOSITION,
                                                   AUTHORITY_LOCK_PATH,
                                                   "authority lock")
    require(authority_identity == {
        "path": AUTHORITY_LOCK_PATH, "bytes": AUTHORITY_LOCK_BYTES,
        "sha256": AUTHORITY_LOCK_SHA256, "git_blob": AUTHORITY_LOCK_BLOB,
    }, "authority lock identity drift")
    require(authority.get("schema") == AUTHORITY_SCHEMA
            and authority.get("authority_id") == "verdier:numdam:asterisque239",
            "authority lock schema/id mismatch")
    require(authority.get("authority") == {
        "file_name": "AST_1996__239__R1_0.pdf",
        "identifier": "AST_1996__239__R1_0",
        "bytes": AUTHORITY_PDF_BYTES,
        "physical_pages": AUTHORITY_PDF_PAGES,
        "sha256": AUTHORITY_PDF_SHA256,
        "role": "controlling_published_source",
        "copied_into_candidate": False,
    }, "authority source binding mismatch")
    require(authority.get("source_project") == {
        "project_id": "verdier_derived_categories_bilingual_canonical_stacks_20260804_r1",
        "workspace_relative_root": "03_projects/language_management/english_germanic/03_working_translations/verdier_derived_categories_bilingual_canonical_stacks_20260804_r1",
    }, "authority project binding mismatch")
    require(authority.get("evidence_files") == [
        {"role": "four_edition_anchor_map", "project_relative_path": AUTHORITY_MAP_PATH,
         "bytes": AUTHORITY_MAP_BYTES, "sha256": AUTHORITY_MAP_SHA256},
        {"role": "english_source_page", "project_relative_path": AUTHORITY_PAGE_PATH,
         "physical_page": AUTHORITY_PHYSICAL_PAGE, "bytes": AUTHORITY_PAGE_BYTES,
         "sha256": AUTHORITY_PAGE_SHA256},
    ], "authority evidence binding mismatch")
    require(authority.get("public_lineage") == {
        "concept_doi": "10.5281/zenodo.21792163",
        "concept_url": "https://doi.org/10.5281/zenodo.21792163",
    }, "authority public-lineage binding mismatch")
    require(authority.get("composition_base") == {
        "repository": "https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts",
        "branch": "main", "commit": HISTORICAL_PUBLIC_BASE, "tree": HISTORICAL_PUBLIC_BASE_TREE,
        "derived_blob": BASE_BLOB, "pinned_official_stacks_commit": OFFICIAL_COMMIT,
        "pinned_official_stacks_tree": OFFICIAL_TREE,
    }, "authority composition-base binding mismatch")
    require(authority.get("scope") == {
        "statement": "Proposition II.1.3.6", "printed_page": 108,
        "authority_physical_pages": [AUTHORITY_PHYSICAL_PAGE],
        "anchor_map_sequences": [1184, 1185, 1186, 1187, 1188, 1189, 1190],
        "anchor_start": "ch2-1-3-6", "anchor_end": "ch2-1-3-6-proof-complete",
        "source_unit_count": 7,
    }, "authority scope binding mismatch")
    require(authority.get("rights_boundary") == {
        "evidence_mode": "locators_hashes_and_independent_paraphrase_only",
        "verbatim_source_prose_in_candidate": False,
        "source_work_license_assertion": "none_by_candidate",
        "source_relicensed": False, "source_public_domain_claimed": False,
        "source_provenance_and_release_terms_remain_controlling": True,
        "payload_requires_independent_wording_and_gfdl_compatibility": True,
    }, "authority rights-boundary binding mismatch")

    lease_pointer_path = f"{CANDIDATE}/LEASE.json"
    pointer, pointer_identity = committed_json(root, PRECOMPOSITION, lease_pointer_path,
                                               "candidate lease pointer")
    require(pointer.get("schema") == "mathematics-commons-stacks-candidate-lease-pointer/v1"
            and pointer.get("lease_registry") == "registry/leases.json"
            and pointer.get("lease_id") == LEASE_ID
            and pointer.get("namespace") == NAMESPACE
            and pointer.get("writer_task") == WRITER_TASK
            and pointer.get("upstream_commit") == OFFICIAL_COMMIT
            and pointer.get("candidate_manifest_schema") == "schemas/candidate-manifest.schema.json"
            and pointer.get("writer_contract") == "candidates/CONTRACT.md",
            "candidate lease pointer binding mismatch")
    return {
        "manifest": manifest_identity,
        "manifest_value": manifest,
        "authority": authority_identity,
        "authority_value": authority,
        "lease_pointer": pointer_identity,
        "references": references,
    }


def validate_operation_contract(root: Path) -> dict[str, Any]:
    """Recompute the registered insertion contract from immutable bytes."""
    raw = committed_raw(root, PRECOMPOSITION, OPERATION_PATH)
    lines = [line for line in raw.splitlines() if line.strip()]
    require(len(lines) == 1, "composition ledger must contain exactly one JSON object")
    operation = strict_object(lines[0], "composition operation")
    identity = commit_identity(root, PRECOMPOSITION, OPERATION_PATH)
    require(identity["bytes"] == 1885 and identity["sha256"] == OPERATION_SHA256
            and identity["git_blob"] == OPERATION_BLOB,
            "composition ledger identity drift")
    require(operation.get("schema") == "mathematics-commons-stacks-composition-operation/v1"
            and operation.get("operation_id") == OPERATION_ID
            and operation.get("operation") == "insert_bytes"
            and operation.get("mode") == "insertion_only",
            "composition operation identity mismatch")
    target = operation.get("target")
    insertion = operation.get("insertion")
    payload_record = operation.get("payload")
    constraints = operation.get("constraints")
    require(all(isinstance(value, Mapping) for value in
                (target, insertion, payload_record, constraints)),
            "composition contract is incomplete")
    expected_target = {
        "base_kind": "published_unified_main",
        "repository": "https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts",
        "commit": HISTORICAL_PUBLIC_BASE, "tree": HISTORICAL_PUBLIC_BASE_TREE, "path": DERIVED_PATH,
        "blob": BASE_BLOB, "bytes": BASE_BYTES, "preimage_sha256": BASE_SHA256,
        "postimage_bytes": POSTIMAGE_BYTES, "postimage_sha256": POSTIMAGE_SHA256,
    }
    require(target == expected_target, "composition target differs from frozen contract")
    require(constraints == {
        "existing_target_bytes_changed": 0, "delete_bytes": 0,
        "replace_bytes": 0, "insert_payload_once": True,
    }, "composition constraints are not strictly insertion-only")
    require(payload_record.get("path") == "payload/fragments/derived-homotopy-category-abelian-split.tex"
            and payload_record.get("bytes") == PAYLOAD_BYTES
            and str(payload_record.get("sha256", "")).upper() == PAYLOAD_SHA256
            and payload_record.get("encoding") == "UTF-8"
            and payload_record.get("line_endings") == "LF"
            and payload_record.get("proposed_label") == PROPOSED_LABEL,
            "composition payload binding mismatch")
    payload = committed_raw(root, PRECOMPOSITION, PAYLOAD_PATH)
    require(len(payload) == PAYLOAD_BYTES and sha256(payload) == PAYLOAD_SHA256
            and b"\r" not in payload and not payload.startswith(b"\xef\xbb\xbf"),
            "composition payload bytes are not exact")
    base = committed_raw(root, HISTORICAL_PUBLIC_BASE, DERIVED_PATH)
    require(len(base) == BASE_BYTES and sha256(base) == BASE_SHA256
            and blob_id(base) == BASE_BLOB, "composition preimage bytes are not exact")
    require(base == committed_raw(root, PRECOMPOSITION, DERIVED_PATH),
            "precomposition source is not the frozen public preimage")
    require(isinstance(insertion, Mapping), "composition insertion record is malformed")
    start, offset, end = (insertion.get(key) for key in
                          ("context_start_byte", "byte_offset", "context_end_byte_exclusive"))
    require(all(type(value) is int for value in (start, offset, end))
            and 0 <= start <= offset <= end <= len(base),
            "composition insertion offsets are invalid")
    context, before, after = base[start:end], base[start:offset], base[offset:end]
    for value, bytes_key, hash_key in ((context, "context_bytes", "context_sha256"),
                                       (before, "before_context_bytes", "before_context_sha256"),
                                       (after, "after_context_bytes", "after_context_sha256")):
        require(len(value) == insertion.get(bytes_key)
                and sha256(value) == str(insertion.get(hash_key, "")).upper(),
                f"composition {bytes_key} binding mismatch")
    require(insertion.get("required_anchor_occurrences") == 1 and base.count(context) == 1
            and insertion.get("after_complete_proof_of_label") ==
            "proposition-homotopy-category-triangulated"
            and insertion.get("before_environment_for_label") ==
            "remark-boundedness-conditions-triangulated",
            "composition anchor binding mismatch")
    projected = base[:offset] + payload + base[offset:]
    composed = committed_raw(root, COMPOSITION, DERIVED_PATH)
    require(projected == composed and len(projected) == POSTIMAGE_BYTES
            and sha256(projected) == POSTIMAGE_SHA256
            and blob_id(projected) == POSTIMAGE_BLOB,
            "composition projection does not match committed postimage")
    return {"operation": identity, "target": target, "payload": payload_record,
            "insertion": insertion, "constraints": constraints}


def validate_registry_contract(root: Path, candidate: Mapping[str, Any], content_head: str) -> dict[str, Any]:
    """Bind the admission/correction registries and lease lifecycle exactly."""
    overlays, overlays_id = committed_json(root, RIGHTS_CORRECTION, OVERLAYS_PATH,
                                           "overlay registry")
    leases, leases_id = committed_json(root, RIGHTS_CORRECTION, LEASES_PATH,
                                       "lease registry")
    require(overlays_id == {"path": OVERLAYS_PATH, "bytes": OVERLAYS_BYTES,
                            "sha256": OVERLAYS_SHA256, "git_blob": OVERLAYS_BLOB},
            "overlay registry identity drift")
    require(leases_id == {"path": LEASES_PATH, "bytes": LEASES_BYTES,
                          "sha256": LEASES_SHA256, "git_blob": LEASES_BLOB},
            "lease registry identity drift")
    for path, expected in ((OVERLAYS_PATH, overlays_id), (LEASES_PATH, leases_id)):
        require(commit_identity(root, content_head, path) == expected,
                f"registry bytes changed after the declared cutoff: {path}")
    registry_changes = git(root, ["diff", "--name-only", "--no-renames",
                                  f"{RIGHTS_CORRECTION}..{content_head}", "--",
                                  OVERLAYS_PATH, LEASES_PATH],
                           "registry post-cutoff scope").decode().splitlines()
    require(registry_changes == [], "registry paths changed after the declared cutoff")
    require(overlays.get("schema") == OVERLAY_REGISTRY_SCHEMA
            and overlays.get("upstream_lock") == "upstream/stacks.lock.json"
            and overlays.get("namespace_root") == "commons/stacks"
            and overlays.get("one_writer_per_ancestor_chain") is True,
            "overlay registry header mismatch")
    entries = overlays.get("registered_entries")
    require(isinstance(entries, list) and len(entries) == 41,
            "overlay registry entry count mismatch")
    matches = [row for row in entries if isinstance(row, Mapping)
               and row.get("id") == CANDIDATE_ID]
    require(len(matches) == 1 and entries[-1] is matches[0],
            "Verdier overlay is not uniquely the registry cutoff entry")
    entry = matches[0]
    candidate_manifest = candidate.get("manifest")
    require(isinstance(candidate_manifest, Mapping)
            and candidate_manifest.get("sha256") == MANIFEST_SHA256
            and candidate_manifest.get("git_blob") == MANIFEST_BLOB,
            "registry candidate binding lacks the exact manifest identity")
    require(entry.get("manifest_sha256") == candidate_manifest.get("sha256"),
            "registry admission does not bind the validated candidate manifest")
    require(entry == {
        "id": CANDIDATE_ID, "namespace": NAMESPACE, "writer": WRITER_TASK,
        "source_commit": OFFICIAL_COMMIT, "source_tree": OFFICIAL_TREE,
        "manifest_sha256": MANIFEST_SHA256, "stable_ids": list(STABLE_IDS),
        "rights_state": RIGHTS_STATE,
        "review_receipt": f"candidates/{NAMESPACE}/{REVIEW_RELATIVE}",
        "admitted_at_utc": entry.get("admitted_at_utc"),
    }, "overlay admission fields mismatch")
    admitted_at = entry.get("admitted_at_utc")
    require(isinstance(admitted_at, str) and re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z", admitted_at),
            "overlay admission timestamp malformed")
    all_ids: list[str] = []
    for row in entries:
        require(isinstance(row, Mapping), "overlay registry has a non-object entry")
        ids = row.get("stable_ids")
        require(isinstance(ids, list) and ids and all(isinstance(item, str) and item for item in ids),
                "overlay registry stable-ID inventory malformed")
        all_ids.extend(ids)
    require(len(all_ids) == 1156 and len(set(all_ids)) == len(all_ids),
            "overlay registry stable-ID count/uniqueness mismatch")
    require(leases.get("schema") == LEASE_REGISTRY_SCHEMA
            and leases.get("upstream_lock") == "upstream/stacks.lock.json"
            and leases.get("namespace_root") == "commons/stacks",
            "lease registry header mismatch")
    events = leases.get("events")
    require(isinstance(events, list) and len(events) >= 85,
            "lease registry event inventory is incomplete")
    require([row.get("event_id") for row in events if isinstance(row, Mapping)] ==
            [f"lease-event-{index:06d}" for index in range(1, len(events) + 1)],
            "lease registry event sequence mismatch")
    related = [row for row in events if isinstance(row, Mapping)
               and row.get("lease_id") == LEASE_ID]
    require(len(related) == 2, "Verdier lease lifecycle is not issue then release")
    common = {"lease_id": LEASE_ID, "namespace": NAMESPACE,
              "candidate_path": f"candidates/{NAMESPACE}", "writer_task": WRITER_TASK,
              "upstream_commit": OFFICIAL_COMMIT, "upstream_tree": OFFICIAL_TREE,
              "writer_contract": "candidates/CONTRACT.md"}
    for row in related:
        require(all(row.get(key) == value for key, value in common.items()),
                "Verdier lease common binding mismatch")
    issued, released = related
    require(issued.get("event_id") == "lease-event-000084"
            and issued.get("event") == "issued" and issued.get("state") == "active",
            "Verdier lease issue event mismatch")
    require(released.get("event_id") == "lease-event-000085"
            and released.get("event") == "released" and released.get("state") == "released"
            and released.get("supersedes_event_id") == "lease-event-000084",
            "Verdier lease release event mismatch")
    # Registry bytes must remain unchanged from the declared cutoff through the
    # content head, and the receipt's admission/cutoff claims are checked later.
    return {"overlays": overlays_id, "leases": leases_id,
            "entry": dict(entry), "overlay_count": len(entries),
            "registered_stable_ids": len(all_ids),
            "lease_issue_event": issued["event_id"],
            "lease_release_event": released["event_id"]}


def validate_topology(root: Path, content_head: str,
                      allowed_paths: set[str] | None = None) -> dict[str, Any]:
    chain_identities: list[dict[str, str]] = []
    for index, revision in enumerate(VERDIER_PREPARATION_CHAIN):
        identity = resolve_commit(root, revision)
        chain_identities.append(identity)
        if index:
            require(commit_parents(root, revision) ==
                    [VERDIER_PREPARATION_CHAIN[index - 1]],
                    f"Verdier preparation parent mismatch at {revision}")
    historical_base = resolve_commit(root, HISTORICAL_PUBLIC_BASE, HISTORICAL_PUBLIC_BASE_TREE)
    base = resolve_commit(root, PUBLIC_BASE, PUBLIC_BASE_TREE)
    pre = resolve_commit(root, PRECOMPOSITION, PRECOMPOSITION_TREE)
    comp = resolve_commit(root, COMPOSITION, COMPOSITION_TREE)
    admission = resolve_commit(root, ADMISSION, ADMISSION_TREE)
    rights = resolve_commit(root, RIGHTS_CORRECTION, RIGHTS_CORRECTION_TREE)
    closure = resolve_commit(root, CLOSURE_CORRECTION, CLOSURE_CORRECTION_TREE)
    content = resolve_commit(root, content_head)
    ancestor(root, HISTORICAL_PUBLIC_BASE, PRECOMPOSITION)
    ancestor(root, HISTORICAL_PUBLIC_BASE, ADMISSION)
    ancestor(root, HISTORICAL_PUBLIC_BASE, PUBLIC_BASE)
    ancestor(root, PRECOMPOSITION, COMPOSITION)
    ancestor(root, COMPOSITION, content_head)
    ancestor(root, ADMISSION, RIGHTS_CORRECTION)
    ancestor(root, RIGHTS_CORRECTION, CLOSURE_CORRECTION)
    ancestor(root, CLOSURE_CORRECTION, PRECOMPOSITION)
    parent = git(root, ["rev-parse", f"{COMPOSITION}^"], "composition parent").decode().strip()
    require(parent == PRECOMPOSITION, "composition is not the single successor of the frozen precomposition")
    composition_rows, composition_diff = changed_leaf_identities(root, PRECOMPOSITION, COMPOSITION)
    require([row["path"] for row in composition_rows] == [DERIVED_PATH]
            and composition_rows[0]["status"] == "modified",
            "composition commit changes more than derived.tex")
    preimage = commit_identity(root, PRECOMPOSITION, DERIVED_PATH)
    require(preimage == {
        "path": DERIVED_PATH, "bytes": BASE_BYTES, "sha256": BASE_SHA256,
        "git_blob": BASE_BLOB,
    }, "precomposition derived.tex identity drift")
    require(commit_identity(root, PRECOMPOSITION, MANIFEST_PATH) == {
        "path": MANIFEST_PATH, "bytes": 5287, "sha256": MANIFEST_SHA256, "git_blob": MANIFEST_BLOB
    }, "candidate manifest identity drift")
    require(commit_identity(root, PRECOMPOSITION, PAYLOAD_PATH) == {
        "path": PAYLOAD_PATH, "bytes": PAYLOAD_BYTES, "sha256": PAYLOAD_SHA256, "git_blob": PAYLOAD_BLOB
    }, "payload identity drift")
    require(commit_identity(root, PRECOMPOSITION, OPERATION_PATH) == {
        "path": OPERATION_PATH, "bytes": 1885,
        "sha256": OPERATION_SHA256, "git_blob": OPERATION_BLOB,
    },
            "operation ledger identity drift")
    derived = commit_identity(root, COMPOSITION, DERIVED_PATH)
    require(derived["bytes"] == POSTIMAGE_BYTES and derived["sha256"] == POSTIMAGE_SHA256
            and derived["git_blob"] == POSTIMAGE_BLOB, "composed derived.tex identity drift")
    require(composition_diff["count"] == 1
            and composition_diff["bytes"] == POSTIMAGE_BYTES
            and composition_diff["tuple_set_sha256"] == sha256(canonical(composition_rows)),
            "composition diff-derived identity summary mismatch")
    integration = validate_integration_merge(root, content_head, allowed_paths)
    return {"public_base": base, "precomposition": pre, "composition": comp,
            "admission": admission, "rights_correction": rights,
            "closure_correction": closure, "content_head": content,
            "historical_public_base": historical_base,
            "verdier_preparation_chain": chain_identities,
            "preimage": preimage, "composition_diff": composition_diff,
            "integration": integration}


def validate_composition_receipt(value: Mapping[str, Any], identity: Mapping[str, Any]) -> dict[str, Any]:
    require(identity == {
        "path": COMPOSITION_PATH,
        "bytes": 18392,
        "sha256": "216EE50CC5AB427BFF9BBEBF0C2BCCB36C42B312D330A751FB5923AA9D25AF34",
        "git_blob": "9314869de9248845921bdee223e6064203bb087b",
    }, "composition-current receipt identity drifted")
    require(value.get("schema") == COMPOSITION_SCHEMA and value.get("status") == "PASS",
            "composition-current is not a passing v4 receipt")
    require(value.get("required_build_stems") == list(STEMS), "composition receipt 30-stem profile mismatch")
    require(value.get("authority") == {"commit": OFFICIAL_COMMIT, "tree": OFFICIAL_TREE},
            "composition receipt authority binding mismatch")
    overlays = value.get("new_overlays")
    require(isinstance(overlays, list) and len(overlays) == 1, "composition receipt must add one overlay")
    overlay = overlays[0]
    require(isinstance(overlay, Mapping) and overlay.get("id") == CANDIDATE_ID,
            "composition receipt overlay mismatch")
    require(overlay.get("manifest_sha256") == MANIFEST_SHA256,
            "composition receipt manifest mismatch")
    require(overlay.get("topology") == "direct_prefixed_leased_candidate_then_admission",
            "composition receipt topology mismatch")
    stable = overlay.get("stable_ids")
    require(stable == len(STABLE_IDS), "composition receipt stable-ID count mismatch")
    require(overlay.get("lease_release_event") == "lease-event-000085",
            "composition receipt lease release mismatch")
    composition = value.get("composition")
    require(isinstance(composition, Mapping), "composition receipt lacks composition state")
    source_commit = composition.get("source_commit")
    require(source_commit == COMPOSITION and composition.get("source_tree") == COMPOSITION_TREE,
            "composition source commit/tree mismatch")
    require(composition.get("base_commit") == PRECOMPOSITION
            and composition.get("base_tree") == PRECOMPOSITION_TREE
            and composition.get("changed_paths") == [DERIVED_PATH]
            and composition.get("new_operations") == 1
            and composition.get("registered_insertion_operations") == 1
            and composition.get("new_byte_edit_operations") == 1,
            "composition receipt topology/scope mismatch")
    affected = composition.get("affected_sources")
    require(isinstance(affected, Mapping) and set(affected) == {DERIVED_PATH},
            "composition receipt affected-source scope mismatch")
    row = affected[DERIVED_PATH]
    require(isinstance(row, Mapping), "invalid derived.tex composition row")
    require(row.get("before_bytes") == BASE_BYTES
            and row.get("before_sha256") == BASE_SHA256
            and row.get("before_git_blob") == BASE_BLOB
            and row.get("composed_bytes") == POSTIMAGE_BYTES
            and str(row.get("composed_sha256", "")).upper() == POSTIMAGE_SHA256
            and row.get("composed_git_blob") == POSTIMAGE_BLOB,
            "composition receipt postimage mismatch")
    frozen = composition.get("frozen_contract")
    require(isinstance(frozen, Mapping)
            and frozen.get("path") == OPERATION_PATH
            and frozen.get("operation_id") == OPERATION_ID
            and frozen.get("bytes") == 1885
            and frozen.get("sha256") == OPERATION_SHA256
            and frozen.get("git_blob") == OPERATION_BLOB
            and frozen.get("base_commit") == HISTORICAL_PUBLIC_BASE
            and frozen.get("base_tree") == HISTORICAL_PUBLIC_BASE_TREE
            and frozen.get("path_target") == DERIVED_PATH
            and frozen.get("base_blob") == BASE_BLOB
            and frozen.get("base_bytes") == BASE_BYTES
            and frozen.get("base_sha256") == BASE_SHA256
            and frozen.get("postimage_bytes") == POSTIMAGE_BYTES
            and frozen.get("postimage_sha256") == POSTIMAGE_SHA256,
            "composition receipt frozen-contract binding mismatch")
    registry = value.get("registry")
    require(isinstance(registry, Mapping)
            and registry.get("admission_commit") == ADMISSION
            and registry.get("admission_tree") == ADMISSION_TREE
            and registry.get("state_commit") == PRECOMPOSITION
            and registry.get("state_tree") == PRECOMPOSITION_TREE
            and registry.get("cutoff_commit") == RIGHTS_CORRECTION
            and registry.get("cutoff_tree") == RIGHTS_CORRECTION_TREE
            and registry.get("post_admission_successor") == RIGHTS_CORRECTION
            and registry.get("last_admitted_overlay") == CANDIDATE_ID
            and registry.get("lease_issue_event") == "lease-event-000084"
            and registry.get("lease_release_event") == "lease-event-000085",
            "composition receipt registry binding mismatch")
    topology = "direct_prefixed_leased_candidate_then_admission"
    return {"receipt": dict(identity), "topology": topology,
            "new_overlay": CANDIDATE_ID, "new_operations": 1,
            "authority": {"commit": OFFICIAL_COMMIT, "tree": OFFICIAL_TREE},
            "preimage": {"path": DERIVED_PATH, "bytes": BASE_BYTES,
                          "sha256": BASE_SHA256, "git_blob": BASE_BLOB},
            "postimage": {"path": DERIVED_PATH, "bytes": POSTIMAGE_BYTES,
                           "sha256": POSTIMAGE_SHA256, "git_blob": POSTIMAGE_BLOB},
            "registry": {"admission_commit": ADMISSION,
                          "cutoff_commit": RIGHTS_CORRECTION,
             "state_commit": PRECOMPOSITION}}


def _root_shared_inputs(root: Path, revisions: Sequence[str]) -> tuple[str, ...]:
    """Return the bounded root-level shared TeX inputs used by the builder."""
    names: set[str] = set()
    shared_suffixes = {".bst", ".cfg", ".cls", ".def", ".sty"}
    for revision in revisions:
        raw = git(root, ["ls-tree", "--name-only", revision],
                  "enumerate root shared inputs")
        for item in raw.decode("utf-8", "strict").splitlines():
            path = PurePosixPath(item)
            if len(path.parts) == 1 and path.suffix.lower() in shared_suffixes:
                names.add(item)
    return tuple(sorted(names))


def _expected_current_main_override(root: Path) -> dict[str, Any]:
    """Recompute the one permitted EGA-to-current-main source-input delta."""
    path = "simplicial.tex"
    r39 = commit_identity(root, HISTORICAL_PUBLIC_BASE, path)
    checkpoint = commit_identity(root, EGA_CONTENT_COMMIT, path)
    current = commit_identity(root, CURRENT_MAIN_PARENT, path)
    require(checkpoint == r39, "EGA checkpoint/current R39 simplicial identity drifted")
    require(current["git_blob"] == "3f222b229e864887dc3a64a199dc11dc2a96ed0d",
            "current-main simplicial identity drifted")
    return {
        "schema": "unofficial-ai-integrated-stacks-current-main-input-override/v1",
        "parent": {
            "optional": True,
            "observed": True,
            "commit": CURRENT_MAIN_PARENT,
            "tree": CURRENT_MAIN_PARENT_TREE,
        },
        "paths": [{
            "path": path,
            "from": {"commit": EGA_CONTENT_COMMIT, **checkpoint},
            "r39": r39,
            "to": {"commit": CURRENT_MAIN_PARENT, **current},
            "direction": "checkpoint_content_to_current_main",
            "exact": True,
            "applied": True,
        }],
    }


def _expected_protected_input_binding(root: Path, source_commit: str) -> dict[str, Any]:
    """Recompute the compact protected-input contract emitted by the driver."""
    stems = (
        "sets", "categories", "topology", "sheaves", "sites", "algebra",
        "fields", "artin", "brauer", "derived", "simplicial", "homology",
        "more-algebra", "smoothing", "modules", "sites-modules", "schemes",
        "properties", "morphisms", "more-morphisms", "spaces-morphisms",
        "crystalline", "spaces-cohomology", "spaces-duality", "stacks-limits",
        "injectives", "cohomology", "sites-cohomology", "gaga", "moduli",
    )
    ega_shared = _root_shared_inputs(root, (EGA_CONTENT_COMMIT,))
    source_shared = _root_shared_inputs(root, (source_commit,))
    require(source_shared == ega_shared,
            "source commit introduced an unbound root shared build input")
    paths = list(("preamble.tex", "chapters.tex", "my.bib"))
    paths.extend(f"{stem}.tex" for stem in stems if stem != "derived")
    paths.extend(path for path in _root_shared_inputs(root, (EGA_CONTENT_COMMIT,))
                 if path != "derived.tex")
    paths = list(dict.fromkeys(paths))
    override_path = "simplicial.tex"
    lines: list[str] = []
    for path in paths:
        historical = commit_identity(root, EGA_CONTENT_COMMIT, path)
        current = commit_identity(root, source_commit, path)
        if path == override_path:
            expected = commit_identity(root, CURRENT_MAIN_PARENT, path)
            require(current == expected, "protected current-main override is not exact")
            role = "current_main_override"
        else:
            require(current == historical,
                    f"protected EGA input drifted before finalization: {path}")
            role = "ega_content"
        local = root / PurePosixPath(path)
        reject_symlink_components(local, f"protected input {path}")
        require(local.is_file(), f"protected input is not a regular file: {path}")
        local_raw = local.read_bytes()
        require(len(local_raw) == current["bytes"] and sha256(local_raw) == current["sha256"],
                f"working protected input bytes differ: {path}")
        lines.append("|".join((path, role, str(current["bytes"]),
                              str(current["sha256"]), str(current["git_blob"]))))
    return {
        "count": len(lines),
        "tuple_set_sha256": sha256(("\n".join(sorted(lines)) + "\n").encode("utf-8")),
    }


def validate_source_checkpoint_binding(value: Mapping[str, Any], label: str,
                                       root: Path, content_head: str,
                                       source_commit: str) -> Mapping[str, Any]:
    """Independently validate the driver's custom EGA checkpoint binding."""
    raw_identity = commit_identity(root, source_commit, EGA_SOURCE_CHECKPOINT_PATH)
    expected_identity = {
        "path": EGA_SOURCE_CHECKPOINT_PATH,
        "bytes": EGA_SOURCE_CHECKPOINT_BYTES,
        "sha256": EGA_SOURCE_CHECKPOINT_SHA256,
        "git_blob": EGA_SOURCE_CHECKPOINT_BLOB,
    }
    require(raw_identity == expected_identity,
            f"{label} does not preserve the sealed EGA checkpoint identity")
    require(commit_identity(root, content_head, EGA_SOURCE_CHECKPOINT_PATH)
            == expected_identity,
            f"{label} content head does not preserve the sealed EGA checkpoint identity")
    checkpoint = strict_object(committed_raw(root, source_commit, EGA_SOURCE_CHECKPOINT_PATH),
                               f"{label} EGA source checkpoint")
    sanitized(checkpoint)
    require(set(checkpoint) == EGA_SOURCE_CHECKPOINT_KEYS,
            f"{label} EGA source checkpoint field inventory is not exact")
    require(checkpoint.get("schema") == EGA_SOURCE_CHECKPOINT_SCHEMA
            and checkpoint.get("status") == EGA_SOURCE_CHECKPOINT_STATUS,
            f"{label} EGA source checkpoint schema/status mismatch")
    require(checkpoint.get("base") == {"commit": EGA_BASE_COMMIT, "tree": EGA_BASE_TREE},
            f"{label} EGA base identity mismatch")
    require(checkpoint.get("content") == {
        "commit": EGA_CONTENT_COMMIT, "tree": EGA_CONTENT_TREE, "parent": EGA_BASE_COMMIT,
    }, f"{label} EGA content identity mismatch")
    resolve_commit(root, EGA_BASE_COMMIT, EGA_BASE_TREE)
    resolve_commit(root, EGA_CONTENT_COMMIT, EGA_CONTENT_TREE)
    require(commit_parents(root, EGA_CONTENT_COMMIT) == [EGA_BASE_COMMIT],
            f"{label} EGA content parent topology mismatch")
    repository_contract = checkpoint.get("repository_state_contract")
    require(isinstance(repository_contract, Mapping)
            and repository_contract.get("content_commit") == EGA_CONTENT_COMMIT,
            f"{label} EGA repository contract mismatch")
    require(checkpoint.get("post_content_metadata_contract") == {
        "allowed_changes": [{"path": EGA_SOURCE_CHECKPOINT_PATH, "change": "added"}],
        "source_drift": False,
    }, f"{label} EGA post-content contract mismatch")
    require(checkpoint.get("checks") == list(EGA_RAW_CHECKS),
            f"{label} EGA checkpoint check inventory is not exact")
    resolve_commit(root, EGA_RECEIPT_COMMIT, EGA_RECEIPT_TREE)
    require(commit_parents(root, EGA_RECEIPT_COMMIT) == [EGA_CONTENT_COMMIT],
            f"{label} EGA receipt-child topology mismatch")
    require(commit_identity(root, EGA_RECEIPT_COMMIT, EGA_SOURCE_CHECKPOINT_PATH)
            == expected_identity,
            f"{label} EGA receipt-child file identity mismatch")
    receipt_changes, _ = changed_leaf_identities(root, EGA_CONTENT_COMMIT, EGA_RECEIPT_COMMIT)
    require(len(receipt_changes) == 1
            and receipt_changes[0]["path"] == EGA_SOURCE_CHECKPOINT_PATH
            and receipt_changes[0]["status"] == "added"
            and receipt_changes[0]["mode"] == "100644",
            f"{label} EGA receipt child changed-path inventory is not exact")
    ancestor(root, EGA_RECEIPT_COMMIT, source_commit)
    tooling = checkpoint.get("tooling")
    require(isinstance(tooling, Mapping), f"{label} EGA tooling binding is malformed")
    writer = tooling.get("writer")
    require(isinstance(writer, Mapping) and writer.get("path") == "tools/write_ega_source_checkpoint.py",
            f"{label} EGA producer binding is malformed")
    writer_identity = commit_identity(root, EGA_CONTENT_COMMIT, "tools/write_ega_source_checkpoint.py")
    require(all(writer.get(key) == writer_identity[key]
                for key in ("bytes", "sha256", "git_blob")),
            f"{label} EGA producer identity drifted")
    expected_producer = {"path": writer_identity["path"], "bytes": writer_identity["bytes"],
                         "sha256": writer_identity["sha256"], "git_blob": writer_identity["git_blob"]}
    expected = {
        "schema": EGA_SOURCE_CHECKPOINT_SCHEMA,
        "status": EGA_SOURCE_CHECKPOINT_STATUS,
        "path": EGA_SOURCE_CHECKPOINT_PATH,
        **expected_identity,
        "historical_base": {"commit": EGA_BASE_COMMIT, "tree": EGA_BASE_TREE},
        "historical_content": {
            "commit": EGA_CONTENT_COMMIT, "tree": EGA_CONTENT_TREE, "parent": EGA_BASE_COMMIT,
        },
        "historical_receipt_child": {
            "commit": EGA_RECEIPT_COMMIT, "tree": EGA_RECEIPT_TREE,
            "changed_paths": [EGA_SOURCE_CHECKPOINT_PATH],
        },
        "producer": expected_producer,
        "descends_from_historical_receipt": True,
        "current_head": source_commit,
        "protected_build_inputs": _expected_protected_input_binding(root, source_commit),
        "current_main_build_input_overrides": _expected_current_main_override(root),
        "checks": list(EGA_SOURCE_CHECKPOINT_CHECKS),
    }
    binding = value.get("source_checkpoint")
    require(isinstance(binding, Mapping), f"{label} lacks source_checkpoint binding")
    require(set(binding) == set(expected) | {"build_recheck"},
            f"{label} source_checkpoint field inventory is not exact")
    for key, expected_value in expected.items():
        require(binding.get(key) == expected_value,
                f"{label} source_checkpoint binding mismatch: {key}")
    recheck = binding.get("build_recheck")
    require(recheck == {
        "before_current_head": source_commit,
        "after_current_head": source_commit,
        "exact_binding_equal": True,
    }, f"{label} source_checkpoint build recheck is not exact")
    source = value.get("source")
    require(isinstance(source, Mapping) and source.get("commit") == source_commit,
            f"{label} source/checkpoint commit mismatch")
    return binding


def validate_build(value: Mapping[str, Any], label: str, root: Path,
                   content_head: str, bound_evidence_paths: set[str]) -> tuple[list[dict[str, Any]], Mapping[str, Any]]:
    require(value.get("schema") == BUILD_SCHEMA and value.get("status") == "PASS",
            f"{label} is not a passing build receipt")
    source = value.get("source")
    require(isinstance(source, Mapping) and SHA1.fullmatch(str(source.get("commit", ""))) is not None
            and SHA1.fullmatch(str(source.get("tree", ""))) is not None,
            f"{label} source identity missing")
    source_commit = str(source.get("commit", "")).lower()
    source_tree = str(source.get("tree", "")).lower()
    resolve_commit(root, source_commit, source_tree)
    require(source.get("commit") == source_commit and source.get("tree") == source_tree,
            f"{label} source commit/tree must be canonical lowercase IDs")
    validate_evidence_suffix(root, source_commit, content_head, bound_evidence_paths)
    validate_source_checkpoint_binding(value, label, root, content_head, source_commit)
    for field, relative in (("builder", "tools/build_verdier_1_3_6_fixed_point.py"),
                            ("build_core", "tools/build_fixed_point.py"),
                            ("release_validator", "tools/validate_verdier_1_3_6_release.py")):
        declared = value.get(field)
        expected = commit_identity(root, source_commit, relative)
        require(isinstance(declared, Mapping), f"{label} lacks {field} identity")
        require_identity(declared, expected, f"{label} {field}", require_blob=True)
    composition = value.get("composition")
    require(isinstance(composition, Mapping) and composition.get("schema") == DIRECT_SCHEMA,
            f"{label} does not use the direct-prefixed composition binding")
    required = {
        "candidate_id": CANDIDATE_ID, "namespace": NAMESPACE, "lease_id": LEASE_ID,
        "operation_id": OPERATION_ID, "precomposition_commit": PRECOMPOSITION,
        "precomposition_tree": PRECOMPOSITION_TREE, "composition_commit": COMPOSITION,
        "composition_tree": COMPOSITION_TREE, "admission_commit": ADMISSION,
        "direct_prefixed_paths": True, "historical_unprefixed_v4_topology_used": False,
        "payload_bytes": PAYLOAD_BYTES, "payload_sha256": PAYLOAD_SHA256,
    }
    for key, expected in required.items():
        require(composition.get(key) == expected, f"{label} composition binding mismatch: {key}")
    manifest = composition.get("candidate")
    require(isinstance(manifest, Mapping), f"{label} lacks candidate binding")
    manifest_id = manifest.get("manifest")
    require(isinstance(manifest_id, Mapping) and manifest_id.get("sha256") == MANIFEST_SHA256
            and manifest_id.get("git_blob") == MANIFEST_BLOB,
            f"{label} candidate manifest binding mismatch")
    registry = composition.get("registry")
    require(isinstance(registry, Mapping) and registry.get("lease_release_event") == "lease-event-000085"
            and registry.get("last_admitted_overlay") == CANDIDATE_ID,
            f"{label} registry/lease binding mismatch")
    build = value.get("build")
    require(isinstance(build, Mapping) and build.get("stems") == list(STEMS)
            and build.get("chapter_count") == len(STEMS)
            and build.get("pdfinfo_readable") == len(STEMS)
            and build.get("builds_per_invocation") == 1,
            f"{label} 30-stem build profile mismatch")
    mutex = build.get("machine_wide_tex_mutex")
    require(isinstance(mutex, Mapping)
            and mutex.get("schema") == "unofficial-ai-integrated-stacks-tex-mutex/v1"
            and mutex.get("status") == "PASS"
            and mutex.get("name") == r"Global\InterlanguageTeXSlotV1"
            and mutex.get("namespace") == "Windows Global"
            and mutex.get("ownership_acquired") is True
            and mutex.get("release_result") == "released_in_finally"
            and mutex.get("wait_result") in ("acquired", "abandoned_recovered")
            and mutex.get("held_scope") == "all TeX/BibTeX passes, TeX/BibTeX version probes, and immediate final log checks",
            f"{label} does not prove full-scope machine mutex ownership")
    diagnostics = build.get("diagnostics")
    require(isinstance(diagnostics, Mapping), f"{label} lacks diagnostics")
    require(all(value == 0 for key, value in diagnostics.items()
                if key != "external_reference_markers"), f"{label} has TeX diagnostics")
    artifacts = value.get("artifacts")
    require(isinstance(artifacts, list) and len(artifacts) == len(STEMS),
            f"{label} artifact count mismatch")
    rows: list[dict[str, Any]] = []
    for expected_stem, artifact in zip(STEMS, artifacts):
        require(isinstance(artifact, Mapping) and artifact.get("stem") == expected_stem,
                f"{label} artifact order mismatch")
        row = {key: artifact.get(key) for key in ("stem", "pages", "bytes", "sha256")}
        require(type(row["pages"]) is int and row["pages"] > 0
                and type(row["bytes"]) is int and row["bytes"] > 0
                and isinstance(row["sha256"], str) and SHA256.fullmatch(row["sha256"]) is not None,
                f"{label} invalid artifact identity")
        rows.append(row)
    tuple_hash = sha256((("\n".join("|".join(str(row[key]) for key in ("stem", "pages", "bytes", "sha256"))
                                     for row in sorted(rows, key=lambda item: item["stem"]))) + "\n").encode())
    require(build.get("artifact_tuple_set_sha256") == tuple_hash,
            f"{label} artifact tuple hash mismatch")
    require(value.get("pdfs_committed") is False, f"{label} falsely claims PDFs committed")
    return rows, build


def validate_repro(value: Mapping[str, Any], first: Mapping[str, Any], second: Mapping[str, Any],
                   first_id: Mapping[str, Any], second_id: Mapping[str, Any], rows: list[dict[str, Any]]) -> dict[str, Any]:
    require(value.get("schema") == REPRO_SCHEMA and value.get("status") == "PASS",
            "reproducibility receipt is not passing")
    runs = value.get("runs")
    require(isinstance(runs, Mapping), "reproducibility receipt lacks run bindings")
    require_identity(runs.get("first", {}), first_id, "first build", "receipt")
    require_identity(runs.get("second", {}), second_id, "second build", "receipt")
    require(runs["first"].get("created_utc") == first.get("created_utc")
            and runs["second"].get("created_utc") == second.get("created_utc"),
            "reproducibility invocation timestamps mismatch")
    require(first.get("created_utc") != second.get("created_utc"), "build invocations are not distinct")
    comparison = value.get("comparison")
    require(isinstance(comparison, Mapping)
            and comparison.get("chapter_count") == len(STEMS)
            and comparison.get("matched_artifact_count") == len(STEMS)
            and comparison.get("different_artifact_count") == 0
            and comparison.get("different_artifacts") == []
            and comparison.get("all_artifact_identities_exactly_equal") is True
            and comparison.get("source_identity_equal") is True
            and comparison.get("builder_identity_equal") is True
            and comparison.get("environment_identity_equal") is True
            and comparison.get("fixed_point_sweep_equal") is True,
            "reproducibility comparison is incomplete")
    require(value.get("artifacts") == rows, "reproducibility artifact inventory mismatch")
    return {"receipt": None, "matched_artifacts": len(rows),
            "different_artifacts": 0,
            "artifact_tuple_set_sha256": comparison.get("artifact_tuple_set_sha256_each_run")}


def validate_visual(value: Mapping[str, Any], first: Mapping[str, Any],
                    first_id: Mapping[str, Any], rows: list[dict[str, Any]]) -> dict[str, Any]:
    require(value.get("schema") == VISUAL_SCHEMA and value.get("status") == "PASS",
            "visual QA receipt is not passing")
    require(value.get("source") == first.get("source"), "visual QA source mismatch")
    binding = value.get("build_receipt")
    require(isinstance(binding, Mapping), "visual QA lacks build receipt binding")
    require_identity(binding, first_id, "visual/build binding")
    scope = value.get("scope")
    require(isinstance(scope, Mapping) and scope.get("affected_chapters") == ["derived"],
            "visual QA must cover exactly the affected derived chapter")
    derived_rows = [row for row in rows if row.get("stem") == "derived"]
    require(len(derived_rows) == 1, "visual QA build inventory lacks one derived artifact")
    derived = derived_rows[0]
    require(type(derived.get("pages")) is int and derived["pages"] > 0,
            "visual QA derived page count is invalid")
    require(scope.get("full_page_render_count") == derived["pages"]
            and scope.get("full_page_contact_sheet_review_count") == derived["pages"],
            "visual QA does not cover every derived page")
    high = scope.get("high_resolution_locus_pages")
    require(isinstance(high, Mapping) and set(high) == {"derived"}
            and isinstance(high["derived"], list)
            and all(type(page) is int for page in high["derived"])
            and bool(high["derived"])
            and high["derived"] == sorted(set(high["derived"]))
            and all(1 <= page <= derived["pages"] for page in high["derived"])
            and high["derived"] == list(EXPECTED_LOCUS_PAGES),
            "visual QA lacks high-resolution locus pages")
    require(scope.get("high_resolution_locus_page_count") == len(high["derived"]),
            "visual QA high-resolution count mismatch")
    checks = value.get("checks")
    require(isinstance(checks, Mapping), "visual QA lacks checks")
    for key in ("all_pages_rendered", "all_pages_manually_inspected",
                "all_manifest_bound_locus_pages_inspected_at_high_resolution",
                "page_dimensions_consistent", "headers_and_page_numbers_consistent",
                "text_and_formulas_legible", "diagrams_intact"):
        require(checks.get(key) is True, f"visual QA gate not passed: {key}")
    for key in ("clipped_content", "overlapping_content", "blank_pages", "corrupted_pages",
                "missing_or_unreadable_glyphs", "broken_diagrams"):
        require(checks.get(key) == 0, f"visual QA reports defect: {key}")
    artifacts = value.get("artifacts")
    require(isinstance(artifacts, Mapping) and set(artifacts) == {"derived"},
            "visual QA artifact scope mismatch")
    visual_derived = artifacts["derived"]
    require(isinstance(visual_derived, Mapping)
            and all(visual_derived.get(key) == derived[key] for key in ("pages", "bytes", "sha256")),
            "visual QA PDF identity mismatch")
    return {"receipt": None, "full_page_reviews": derived["pages"],
            "high_resolution_pages": len(high["derived"]), "defects": 0}


def validate_readback(value: Mapping[str, Any], root: Path, base: str, head: str,
                      head_tree: str, required_paths: set[str]) -> dict[str, Any]:
    require(value.get("schema") == READBACK_SCHEMA and value.get("status") == "PASS",
            "GitHub readback receipt is not passing")
    repository = value.get("repository")
    require(isinstance(repository, Mapping) and repository.get("owner_repo") == REPOSITORY
            and repository.get("public") is True, "readback repository identity/publicity mismatch")
    comparison = value.get("comparison")
    require(isinstance(comparison, Mapping), "readback comparison missing")
    base_identity = resolve_commit(root, base)
    head_identity = resolve_commit(root, head, head_tree)
    # The ancestry and complete leaf set are recomputed from local immutable
    # Git objects.  Values in the submitted receipt are observations only and
    # cannot select a subset of paths to validate.
    ancestor(root, base_identity["commit"], head_identity["commit"])
    expected_rows, diff_summary = changed_leaf_identities(
        root, base_identity["commit"], head_identity["commit"]
    )
    for key, commit, tree in (("base", base_identity["commit"], base_identity["tree"]),
                              ("head", head_identity["commit"], head_identity["tree"])):
        row = comparison.get(key)
        require(isinstance(row, Mapping) and row.get("commit") == commit
                and row.get("tree") == tree and row.get("api_identity_check") == "PASS",
                f"readback {key} identity mismatch")
    require(comparison.get("base_is_ancestor") is True, "readback lacks ancestry proof")
    require(type(value.get("changed_path_count")) is int
            and value.get("changed_path_count") == diff_summary["count"],
            "readback changed-path count does not match local Git diff")
    require(type(value.get("changed_file_bytes")) is int
            and value.get("changed_file_bytes") == diff_summary["bytes"],
            "readback changed-file bytes do not match local Git diff")
    require(value.get("changed_path_identity_tuple_set_sha256") ==
            diff_summary["tuple_set_sha256"],
            "readback changed-path tuple hash does not match local Git diff")
    rows = value.get("changed_paths")
    require(isinstance(rows, list) and len(rows) == value.get("changed_path_count") and bool(rows),
            "readback changed-path inventory invalid")
    by_path: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        require(isinstance(row, Mapping), "invalid readback leaf")
        path = safe_relative(str(row.get("path", "")), "readback path")
        require(path not in by_path and type(row.get("bytes")) is int
                and row.get("bytes") >= 0
                and row.get("status") in ("added", "modified")
                and row.get("mode") in ("100644", "100755")
                and row.get("identity_check") == "PASS", "invalid or duplicate readback leaf")
        require(isinstance(row.get("sha256"), str)
                and SHA256.fullmatch(row["sha256"]) is not None
                and isinstance(row.get("git_blob"), str)
                and SHA1.fullmatch(row["git_blob"]) is not None,
                f"readback leaf identity is malformed: {path}")
        by_path[path] = row
    expected_by_path = {row["path"]: row for row in expected_rows}
    require(set(by_path) == set(expected_by_path),
            "readback changed-path set differs from local Git diff")
    for path, expected in expected_by_path.items():
        observed = by_path[path]
        for key in ("status", "mode", "bytes", "sha256", "git_blob"):
            require(observed.get(key) == expected[key],
                    f"readback/local diff identity mismatch: {path} ({key})")
    require(required_paths <= set(expected_by_path),
            "readback omits required release leaves: " + ", ".join(sorted(required_paths - set(by_path))))
    checks = value.get("checks")
    require(isinstance(checks, Mapping) and all(checks.get(key) is True for key in (
        "repository_public", "base_api_commit_and_tree_equal_local_git",
        "head_api_commit_and_tree_equal_local_git", "base_is_ancestor_of_head",
        "changed_inventory_nonempty_and_bounded", "no_deletions_renames_type_changes_symlinks_or_submodules",
        "all_changed_files_raw_read_back", "all_byte_counts_match", "all_sha256_match",
        "all_git_blob_ids_match")), "readback checks are incomplete")
    return {"status": "PASS", "commit": head, "tree": head_tree,
            "checked_file_count": diff_summary["count"],
            "checked_total_bytes": diff_summary["bytes"],
            "changed_path_identity_tuple_set_sha256": diff_summary["tuple_set_sha256"]}


def make_receipt(args: argparse.Namespace) -> dict[str, Any]:
    # Bind every caller-controlled filesystem path before any Git query or
    # evidence read.  In particular, do not resolve a symlink first: that
    # would erase the lexical evidence that the caller supplied an alias.
    root = exact_worktree_root(args.root)
    args.root = root
    if args.composition is None:
        args.composition = root / COMPOSITION_PATH
        args.composition_logical = COMPOSITION_PATH
    actual_raw = git(root, ["rev-parse", "--show-toplevel"], "repository root").decode("utf-8", "strict").strip()
    actual = lexical_absolute(Path(actual_raw))
    reject_symlink_components(actual, "Git-reported repository root")
    require(same_lexical_path(root, actual), "--root must be the exact Git top level")
    if args.output is not None:
        args.output = exact_validation_path(
            root, args.output, logical_default(args.output), "output", allow_missing_leaf=True
        )
    if args.check_receipt is not None:
        args.check_receipt = exact_validation_path(
            root, args.check_receipt, logical_default(args.check_receipt),
            "checked receipt"
        )
    content_head = args.content_head.lower()
    bound_evidence_paths = {
        logical for logical in (
            args.first_build_logical,
            args.second_build_logical, args.reproducibility_logical,
            args.visual_qa_logical, args.public_readback_logical,
            args.metadata_readback_logical,
        ) if logical is not None
    }
    topology = validate_topology(root, content_head, bound_evidence_paths)
    candidate_binding = validate_authority_and_candidate(root)
    operation_binding = validate_operation_contract(root)
    registry_binding = validate_registry_contract(root, candidate_binding, content_head)

    comp, comp_id = local_evidence(root, args.composition, args.composition_logical, content_head)
    composition = validate_composition_receipt(comp, comp_id)
    require(composition["preimage"] == {
        "path": DERIVED_PATH, "bytes": BASE_BYTES,
        "sha256": BASE_SHA256, "git_blob": BASE_BLOB,
    }, "composition receipt preimage does not match the validated source")
    require(composition["postimage"] == {
        "path": DERIVED_PATH, "bytes": POSTIMAGE_BYTES,
        "sha256": POSTIMAGE_SHA256, "git_blob": POSTIMAGE_BLOB,
    }, "composition receipt postimage does not match the validated source")
    require(operation_binding["operation"]["git_blob"] == OPERATION_BLOB,
            "composition operation binding drifted")
    require(registry_binding["entry"]["manifest_sha256"] ==
            candidate_binding["manifest"]["sha256"],
            "composition registry/candidate manifest binding mismatch")
    overlay_rows = comp.get("new_overlays")
    require(isinstance(overlay_rows, list) and len(overlay_rows) == 1
            and isinstance(overlay_rows[0], Mapping),
            "composition overlay binding is malformed")
    overlay = overlay_rows[0]
    manifest_id = candidate_binding["manifest"]
    payload_id = commit_identity(root, PRECOMPOSITION, PAYLOAD_PATH)
    operation_id = operation_binding["operation"]
    review_id = commit_identity(root, PRECOMPOSITION,
                                f"{CANDIDATE}/{REVIEW_RELATIVE}")
    authority_id = candidate_binding["authority"]
    expected_overlay_fields = {
        "id": CANDIDATE_ID,
        "candidate_path": CANDIDATE,
        "namespace": NAMESPACE,
        "lease_id": LEASE_ID,
        "manifest_path": "candidate.manifest.json",
        "manifest_bytes": manifest_id["bytes"],
        "manifest_sha256": manifest_id["sha256"],
        "manifest_git_blob": manifest_id["git_blob"],
        "payload_path": "payload/fragments/derived-homotopy-category-abelian-split.tex",
        "payload_bytes": payload_id["bytes"],
        "payload_sha256": payload_id["sha256"],
        "payload_git_blob": payload_id["git_blob"],
        "composition_path": "composition.jsonl",
        "composition_bytes": operation_id["bytes"],
        "composition_sha256": operation_id["sha256"],
        "composition_git_blob": operation_id["git_blob"],
        "review_receipt_path": REVIEW_RELATIVE,
        "review_receipt_bytes": review_id["bytes"],
        "review_receipt_sha256": review_id["sha256"],
        "review_receipt_git_blob": review_id["git_blob"],
        "authority_lock_path": "authority/authority.lock.json",
        "authority_lock_bytes": authority_id["bytes"],
        "authority_lock_sha256": authority_id["sha256"],
        "authority_lock_git_blob": authority_id["git_blob"],
        "operations": 1,
        "operation_kind": "registered_insertion",
        "operation_id": OPERATION_ID,
        "topology": "direct_prefixed_leased_candidate_then_admission",
        "stable_ids": len(STABLE_IDS),
        "lease_issue_event": "lease-event-000084",
        "lease_release_event": "lease-event-000085",
    }
    require(all(overlay.get(key) == expected for key, expected in
                expected_overlay_fields.items()),
            "composition overlay does not bind the validated candidate packet")
    first, first_id = local_evidence(root, args.first_build, args.first_build_logical, content_head)
    second, second_id = local_evidence(root, args.second_build, args.second_build_logical, content_head)
    repro, repro_id = local_evidence(root, args.reproducibility, args.reproducibility_logical, content_head)
    visual, visual_id = local_evidence(root, args.visual_qa, args.visual_qa_logical, content_head)

    first_rows, first_build = validate_build(
        first, "first build", root, content_head, bound_evidence_paths
    )
    second_rows, second_build = validate_build(
        second, "second build", root, content_head, bound_evidence_paths
    )
    for key in ("schema", "status", "source", "builder", "build_core", "release_validator",
                "composition", "environment", "build", "artifacts", "source_checkpoint",
                "pdfs_committed", "sanitization"):
        require(first.get(key) == second.get(key), f"build receipts differ in exact bound field: {key}")
    require(first_rows == second_rows and first_build == second_build,
            "build receipts do not prove exact fixed-point equality")
    ancestor(root, COMPOSITION, str(first["source"]["commit"]))
    ancestor(root, str(first["source"]["commit"]), content_head)
    repro_summary = validate_repro(repro, first, second, first_id, second_id, first_rows)
    repro_summary["receipt"] = repro_id
    visual_summary = validate_visual(visual, first, first_id, first_rows)
    visual_summary["receipt"] = visual_id

    required_paths = {MANIFEST_PATH, PAYLOAD_PATH, OPERATION_PATH, OVERLAYS_PATH,
                      LEASES_PATH, DERIVED_PATH, COMPOSITION_PATH,
                      args.first_build_logical, args.second_build_logical,
                      args.reproducibility_logical, args.visual_qa_logical}
    if args.pre_publication:
        publication: dict[str, Any] = {
            "status": "PENDING", "reason": "content head has not yet been anonymously read back",
            "expected_repository": REPOSITORY, "expected_commit": content_head,
            "expected_tree": topology["content_head"]["tree"],
        }
        status = "READY_FOR_PUBLICATION"
    else:
        require(args.public_readback is not None, "published mode requires --public-readback")
        readback_value, readback_id = local_evidence(
            root, args.public_readback, args.public_readback_logical, content_head,
            require_committed=False)
        publication = validate_readback(readback_value, root, PUBLIC_BASE, content_head,
                                        topology["content_head"]["tree"], required_paths)
        publication["receipt"] = readback_id
        status = "PUBLICATION_VERIFIED"

    metadata: dict[str, Any] | None = None
    if args.metadata_readback is not None:
        require(not args.pre_publication, "metadata readback is invalid in pre-publication mode")
        require(args.metadata_head is not None, "--metadata-readback requires --metadata-head")
        metadata_commit = resolve_commit(root, args.metadata_head.lower())
        ancestor(root, content_head, metadata_commit["commit"])
        metadata_value, metadata_id = local_evidence(
            root, args.metadata_readback, args.metadata_readback_logical, content_head,
            require_committed=False)
        metadata = validate_readback(metadata_value, root, content_head,
                                     metadata_commit["commit"], metadata_commit["tree"], set())
        metadata["receipt"] = metadata_id

    result: dict[str, Any] = {
        "schema": SCHEMA,
        "status": status,
        "phase": "pre_publication" if args.pre_publication else "published",
        "repository": {"owner_repo": REPOSITORY, "public_access_required": True},
        "topology": topology,
        "validated_bindings": {
            "candidate": candidate_binding,
            "operation": operation_binding,
            "registry": registry_binding,
        },
        "candidate": {
            "id": CANDIDATE_ID, "namespace": NAMESPACE, "lease_id": LEASE_ID,
            "operation_id": OPERATION_ID, "stable_ids": list(STABLE_IDS),
            "manifest": commit_identity(root, PRECOMPOSITION, MANIFEST_PATH),
            "payload": commit_identity(root, PRECOMPOSITION, PAYLOAD_PATH),
            "lease_issue_event": "lease-event-000084",
            "lease_release_event": "lease-event-000085",
        },
        "composition": composition,
        "evidence": {
            "first_build": first_id, "second_build": second_id,
            "reproducibility": repro_summary, "visual_qa": visual_summary,
        },
        "fixed_point": {
            "chapter_count": len(STEMS), "stems": list(STEMS),
            "artifacts": first_rows,
            "pages": sum(row["pages"] for row in first_rows),
            "pdf_bytes": sum(row["bytes"] for row in first_rows),
            "artifact_tuple_set_sha256": first_build["artifact_tuple_set_sha256"],
            "two_distinct_exact_builds": True,
            "serialized_non_overlap": {
                "status": "PASS", "mechanism": r"Global\InterlanguageTeXSlotV1",
                "proof": "both complete build scopes acquired and released the same exclusive machine-wide mutex",
            },
        },
        "public_readback": publication,
        "metadata_successor_readback": metadata,
        "sanitization": {
            "local_paths_recorded": False, "credentials_recorded": False,
            "environment_values_recorded": False, "authenticated_urls_recorded": False,
        },
    }
    sanitized(result)
    result["receipt_content_sha256"] = sha256(canonical(result))
    sanitized(result)
    return result


def logical_default(path: Path) -> str:
    return f"validation/{path.name}"


def parse(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).absolute().parents[1])
    parser.add_argument("--content-head", required=True)
    # Resolve the canonical composition path only after the exact worktree has
    # been established in ``make_receipt``; a relative argparse default must
    # never be interpreted against the caller's current directory.
    parser.add_argument("--composition", type=Path)
    parser.add_argument("--composition-logical", default=COMPOSITION_PATH)
    parser.add_argument("--first-build", type=Path, required=True)
    parser.add_argument("--first-build-logical")
    parser.add_argument("--second-build", type=Path, required=True)
    parser.add_argument("--second-build-logical")
    parser.add_argument("--reproducibility", type=Path, required=True)
    parser.add_argument("--reproducibility-logical")
    parser.add_argument("--visual-qa", type=Path, required=True)
    parser.add_argument("--visual-qa-logical")
    parser.add_argument("--pre-publication", action="store_true")
    parser.add_argument("--public-readback", type=Path)
    parser.add_argument("--public-readback-logical")
    parser.add_argument("--metadata-head")
    parser.add_argument("--metadata-readback", type=Path)
    parser.add_argument("--metadata-readback-logical")
    output = parser.add_mutually_exclusive_group(required=True)
    output.add_argument("--output", type=Path)
    output.add_argument("--check-receipt", type=Path)
    args = parser.parse_args(argv)
    args.content_head = args.content_head.lower()
    require(SHA1.fullmatch(args.content_head) is not None, "--content-head must be a full commit")
    if args.metadata_head is not None:
        args.metadata_head = args.metadata_head.lower()
        require(SHA1.fullmatch(args.metadata_head) is not None,
                "--metadata-head must be a full commit")
    if args.composition is None:
        args.composition_logical = COMPOSITION_PATH
    for stem in ("first_build", "second_build", "reproducibility", "visual_qa"):
        logical = stem + "_logical"
        if getattr(args, logical) is None:
            setattr(args, logical, logical_default(getattr(args, stem)))
    if args.public_readback is not None and args.public_readback_logical is None:
        args.public_readback_logical = logical_default(args.public_readback)
    if args.metadata_readback is not None and args.metadata_readback_logical is None:
        args.metadata_readback_logical = logical_default(args.metadata_readback)
    require(args.pre_publication == (args.public_readback is None),
            "choose --pre-publication or supply --public-readback, exclusively")
    return args


def write_new(path: Path, value: Mapping[str, Any]) -> None:
    require(not path.exists() and not path.is_symlink(), "refusing to overwrite output")
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2,
                     allow_nan=False).encode("utf-8") + b"\n"
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    descriptor = os.open(path, flags, 0o644)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    except BaseException:
        try:
            path.unlink()
        except OSError:
            pass
        raise


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = parse(argv)
        receipt = make_receipt(args)
        if args.check_receipt is not None:
            observed = strict_object(args.check_receipt.read_bytes(), "checked final receipt")
            sanitized(observed)
            require(observed == receipt, "checked final receipt differs from recomputed truth")
            action = "checked"
        else:
            write_new(args.output, receipt)
            action = "written"
        print(json.dumps({"status": "PASS", "action": action,
                          "phase": receipt["phase"],
                          "receipt_content_sha256": receipt["receipt_content_sha256"]},
                         sort_keys=True))
        return 0
    except (FinalizationError, OSError, UnicodeError, ValueError, TypeError,
            KeyError, IndexError, StopIteration, subprocess.TimeoutExpired) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
