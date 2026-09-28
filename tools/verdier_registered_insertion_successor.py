#!/usr/bin/env python3
"""Validate one current-main-first Verdier registered-insertion successor.

The contract is deliberately narrower than the historical v4 workflow.  It
accepts exactly the already-public R48/Illusie state, the already-recorded
Verdier II.1.3.6 candidate prefix, one independent-review transaction, one
registry admission, and one insertion-only source transaction.  Future commit
and tree identities are read from the committed receipt and then proved from
Git objects; they are not compiled into this program.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

sys.dont_write_bytecode = True

if __package__:
    from . import ai_source_correction_composition as ai_correction
    from . import direct_successor_composition as direct
else:
    import ai_source_correction_composition as ai_correction
    import direct_successor_composition as direct


Git = direct.Git
require = direct.require
identity = direct.identity
safe_path = direct.safe_path
parse_json = direct.parse_json

SCHEMA = "unofficial-ai-integrated-stacks-verdier-registered-insertion-successor/v1"
TRANSPORT_SCHEMA = "unofficial-ai-integrated-stacks-verdier-linear-transport/v1"
MODE = "registered insertion rebased through unique unchanged context"
RECEIPT = "validation/composition-current.json"
INDEX = "validation/direct-successor-current.json"

AUTHORITY_COMMIT = "a04446e57ec1fbc252a871afcec7752fb2807b14"
AUTHORITY_TREE = "3feeb703b931a6e7259782c10e7d1575adc83e5e"
PREVIOUS_PUBLIC = "4828ebac86db7ebf4211227cabe183b09f11c992"
PREVIOUS_PUBLIC_TREE = "d351c98e5a4655f20b2ddf34783314cda21e6c91"
INHERITED_RECEIPT_HEAD = "00856c315dabb2516cad6d956a25030909419947"
INHERITED_RECEIPT_TREE = "11aeb66e85471278dd828476c122b6b19c1d952f"
INHERITED_RECEIPT_ID = {
    "bytes": 165405,
    "sha256": "7CFA04B3A5F7BAD0653B63BC4D1BE2E84828CFB61DFC7880B7D8BAB2F7837AD2",
    "git_blob": "ea590d297f07b484bfc1906c14ac9de7ba6350e6",
}

# This prefix is already committed and is part of the requested exact topology.
PROVENANCE_COMMIT = "3102126f69604d3008029cd098f6a790acd9f027"
PROVENANCE_TREE = PREVIOUS_PUBLIC_TREE
PROVENANCE_SECOND_PARENT = "288a082f3f98438d824c22d1534fb168edd05728"
PROVENANCE_SECOND_PARENT_TREE = "c58a417324696717c5add769c86d0e124dd3301b"
LEASE_ISSUE_COMMIT = "8b5c4fb74822a225ce8aaa227d0496b9978b9db0"
LEASE_ISSUE_TREE = "821a89b797890e6bff3d7f5e1f63c851201d7ac0"
CANDIDATE_FREEZE_COMMIT = "65da408e2209f68e134067bf8102f68522062a5c"
CANDIDATE_FREEZE_TREE = "bb8fb0db2fd0f87e5667a2a7863d178eb12a792b"

OVERLAY_ID = "stacks-verdier-a04446e-1-3-6-r1"
NAMESPACE = "commons/stacks/verdier-ast239-1-3-6-r1"
CANDIDATE_DIR = "ai-integrated/candidates/" + NAMESPACE
LEASE_ID = "stacks-lease-000064-verdier-ast239-1-3-6-r1"
WRITER_TASK = "019fca5a-c80e-7890-a46b-4948ff443e6d"
ISSUE_EVENT = "lease-event-000124"
RELEASE_EVENT = "lease-event-000125"
REVIEW_SHA256 = "010870DCEDE1C2FD52CC2FEDBF3A72691BEFA15EA668EAD25E810BD7C606F557"
FINAL_MANIFEST_SHA256 = "36C212923227798F4C4AEDEA09ED6385A79CD29FC944DD09946FC97AA267AF0E"
FINAL_CANDIDATE_SUBTREE = "22b5f87d722f9f2b6d22aaeac4c1c2b69904e555"
OVERLAYS = "ai-integrated/registry/overlays.json"
LEASES = "ai-integrated/registry/leases.json"
ADMISSION_RECEIPT = "ai-integrated/registry/admission-receipts/verdier-ast239-1-3-6-r1.json"
COMPOSER = "tools/compose_registered_insertion.py"
TARGET = "derived.tex"
PAYLOAD = "payload/fragments/derived-homotopy-category-abelian-split.tex"
COMPOSITION = "composition.jsonl"
STABLE_UNITS = "stable-units.json"
SOURCE_MAP = "source-map.jsonl"

STABLE_IDS = (
    "verdier:ast239:1.3.6",
    "verdier:ast239:1.3.6:equivalent-conditions",
    "verdier:ast239:1.3.6:proof:i-iff-ii",
    "verdier:ast239:1.3.6:proof:ii-implies-iii",
    "verdier:ast239:1.3.6:construction:hstar-complex",
    "verdier:ast239:1.3.6:claim:hstar-equivalence",
    "verdier:ast239:1.3.6:conclusion:iii-implies-ii",
)

EXPECTED_STEMS = (
    "sets", "categories", "topology", "sheaves", "sites", "algebra",
    "fields", "artin", "brauer", "derived", "simplicial", "homology",
    "more-algebra", "smoothing", "modules", "sites-modules", "schemes",
    "properties", "morphisms", "more-morphisms", "spaces-morphisms",
    "crystalline", "spaces-cohomology", "spaces-duality", "stacks-limits",
    "injectives", "cohomology", "sites-cohomology", "gaga", "moduli",
    "descent", "perfect", "topologies", "groupoids", "more-groupoids",
    "spaces-perfect",
)

FIXED_CANDIDATE_PATHS = tuple(
    CANDIDATE_DIR + "/" + path for path in (
        ".gitattributes", ".gitignore", "LEASE.json", "README.md", "_build_impl.py",
        "authority/authority.lock.json",
        "build-manifest.py", "build.py", "builds/baseline-derived.log",
        "builds/build-receipt.json", "builds/derived.log", "builds/derived.pdf",
        "builds/tex-mutex.json", "builds/validation.json", "builds/visual-qa.json",
        "builds/visual/derived-036.png", "builds/visual/derived-037.png",
        "builds/visual/derived-038.png", "builds/visual/derived-039.png",
        "candidate.config.json", "candidate.manifest.json", "check-manifest.py",
        "composition.jsonl", "decisions.jsonl", "formula-diagram-inventory.json",
        PAYLOAD, "rejections.jsonl", SOURCE_MAP, STABLE_UNITS, "verify.py",
    )
)

PREPARATION_PATHS = (
    "tools/build_fixed_point.py",
    "tools/direct_successor_checkpoint.py",
    "tools/validate_unified_repository.py",
    "tools/verdier_registered_insertion_successor.py",
    "tools/validate_verdier_registered_insertion_successor.py",
    "tools/tests/test_verdier_registered_insertion_successor.py",
)

POST_COMPOSITION_REPAIR_PATHS = (
    "tools/direct_successor_checkpoint.py",
    "tools/verdier_registered_insertion_successor.py",
    "tools/tests/test_verdier_registered_insertion_successor.py",
)

TOOLS = (
    "tools/verdier_registered_insertion_successor.py",
    "tools/validate_verdier_registered_insertion_successor.py",
    "tools/compose_registered_insertion.py",
    "tools/build_fixed_point.py",
    "tools/direct_successor_checkpoint.py",
    "tools/validate_unified_repository.py",
    "tools/ai_source_correction_composition.py",
    "tools/direct_successor_composition.py",
    "tools/direct_successor_common.py",
    "tools/compare_fixed_point_builds.py",
    "tools/validate_direct_successor_release.py",
    "tools/tex_process_guard.py",
    "tools/tex_process_public_receipt.py",
    "tools/tests/test_verdier_registered_insertion_successor.py",
)

ID_KEYS = {"bytes", "sha256", "git_blob"}
REFERENCE_KEYS = ID_KEYS | {"path"}


def _valid_sha(value: object, label: str) -> str:
    require(isinstance(value, str) and re.fullmatch(r"[0-9A-F]{64}", value),
            f"invalid SHA-256 for {label}")
    return value


def _valid_identity(row: object, label: str, *, reference: bool = False) -> dict:
    keys = REFERENCE_KEYS if reference else ID_KEYS
    require(isinstance(row, dict) and set(row) == keys, f"invalid identity shape for {label}")
    require(type(row["bytes"]) is int and row["bytes"] >= 0, f"invalid byte count for {label}")
    _valid_sha(row["sha256"], label)
    require(isinstance(row["git_blob"], str) and re.fullmatch(r"[0-9a-f]{40}", row["git_blob"]),
            f"invalid Git blob for {label}")
    if reference:
        safe_path(row["path"])
    return row


def _reference(git: Git, revision: str, path: str) -> dict[str, object]:
    return {"path": safe_path(path), **git.ident(revision, path)}


def _commit(git: Git, value: object, label: str) -> str:
    require(isinstance(value, str), f"missing {label} commit")
    try:
        return git.commit(value)
    except ValueError as exc:
        raise ValueError(f"invalid {label} commit: {exc}") from exc


def _step(git: Git, parent: str, commit: str, kind: str) -> dict[str, object]:
    changes = git.changes(parent, commit)
    return {
        "kind": kind,
        "commit": commit,
        "parent": parent,
        "parents": git.parents(commit),
        "tree": git.tree(commit),
        "paths": [
            {
                "path": path,
                "old_mode": row[0],
                "mode": row[1],
                "old_blob": row[2],
                "git_blob": row[3],
                "status": row[4],
                "bytes": git.ident(commit, path)["bytes"],
                "sha256": git.ident(commit, path)["sha256"],
            }
            for path, row in sorted(changes.items())
        ],
    }


def _require_step(
    git: Git,
    parent: str,
    commit: str,
    tree: str | None,
    kind: str,
    paths: set[str] | None,
) -> dict[str, object]:
    _commit(git, commit, kind)
    require(git.parents(commit) == [parent], f"{kind} is not the exact one-parent successor")
    if tree is not None:
        require(git.tree(commit) == tree, f"{kind} tree mismatch")
    changes = git.changes(parent, commit)
    if paths is not None:
        require(set(changes) == paths, f"{kind} path inventory mismatch")
    for path, row in changes.items():
        require(row[1] == "100644" and row[4] in {"A", "M"},
                f"{kind} contains a deletion or non-regular path: {path}")
    return _step(git, parent, commit, kind)


def _append_one(before: object, after: object, field: str, label: str) -> dict:
    require(isinstance(before, dict) and isinstance(after, dict), f"invalid {label} documents")
    old, new = before.get(field), after.get(field)
    require(isinstance(old, list) and isinstance(new, list) and new[:len(old)] == old
            and len(new) == len(old) + 1, f"{label} is not an exact one-row append")
    require({k: v for k, v in before.items() if k != field}
            == {k: v for k, v in after.items() if k != field}, f"{label} header changed")
    require(isinstance(new[-1], dict), f"invalid appended {label} row")
    return new[-1]


def _jsonl(raw: bytes, label: str) -> list[dict]:
    rows = [parse_json(line) for line in raw.splitlines() if line.strip()]
    require(rows and all(isinstance(row, dict) for row in rows), f"invalid JSONL: {label}")
    return rows


def _validate_inherited(git: Git) -> tuple[dict, dict[str, dict[str, object]]]:
    require(git.tree(PREVIOUS_PUBLIC) == PREVIOUS_PUBLIC_TREE, "wrong previous public tree")
    require(git.tree(INHERITED_RECEIPT_HEAD) == INHERITED_RECEIPT_TREE,
            "wrong inherited AI validation-head tree")
    observed = git.ident(PREVIOUS_PUBLIC, RECEIPT)
    require(observed == INHERITED_RECEIPT_ID, "wrong inherited R48 AI receipt identity")
    require(git.blob(PREVIOUS_PUBLIC, RECEIPT)
            == git.blob(PREVIOUS_PUBLIC, ai_correction.NAMED_RECEIPT),
            "inherited current/named AI receipts differ")
    require(git.blob(INHERITED_RECEIPT_HEAD, RECEIPT) == git.blob(PREVIOUS_PUBLIC, RECEIPT),
            "inherited AI receipt changed after its validation head")
    previous = git.document(PREVIOUS_PUBLIC, RECEIPT)
    require(previous.get("schema") == ai_correction.SCHEMA and previous.get("status") == "PASS",
            "inherited composition is not the passing R48 AI successor")
    require(previous.get("authority") == {"commit": AUTHORITY_COMMIT, "tree": AUTHORITY_TREE},
            "inherited official authority mismatch")
    comp = previous.get("composition", {})
    ai_correction.validate_ai_source_correction_scope(
        previous.get("ai_source_correction_scope"),
        source_commit=comp.get("source_commit"),
        source_tree=comp.get("source_tree"),
    )
    require(tuple(previous.get("required_build_stems", ())) == EXPECTED_STEMS,
            "inherited composition is not the exact 36-stem profile")
    require(previous.get("registry", {}).get("last_admitted_overlay") == "stacks-errata-a04446e-r48",
            "inherited registry is not sealed R48")
    manifest = git.document(INHERITED_RECEIPT_HEAD, ai_correction.MANIFEST)
    ai_correction.validate_manifest(git, manifest, INHERITED_RECEIPT_HEAD)
    require(git.blob(INHERITED_RECEIPT_HEAD, ai_correction.MANIFEST)
            == git.blob(PREVIOUS_PUBLIC, ai_correction.MANIFEST),
            "AI correction manifest changed after its validated head")
    protected = deepcopy(previous.get("correction_protected_inputs"))
    require(isinstance(protected, dict) and protected, "inherited Illusie protected inputs missing")
    for path, expected in protected.items():
        _valid_identity(expected, path)
        require(git.ident(PREVIOUS_PUBLIC, path) == expected,
                "inherited Illusie input identity mismatch: " + path)
    protected[ai_correction.NAMED_RECEIPT] = git.ident(PREVIOUS_PUBLIC, ai_correction.NAMED_RECEIPT)
    return previous, dict(sorted(protected.items()))


def _validate_fixed_prefix(git: Git) -> tuple[list[dict[str, object]], dict]:
    _commit(git, PROVENANCE_SECOND_PARENT, "preserved candidate-history parent")
    require(git.tree(PROVENANCE_SECOND_PARENT) == PROVENANCE_SECOND_PARENT_TREE,
            "preserved candidate-history parent tree mismatch")
    require(git.parents(PROVENANCE_COMMIT) == [PREVIOUS_PUBLIC, PROVENANCE_SECOND_PARENT]
            and git.tree(PROVENANCE_COMMIT) == PROVENANCE_TREE
            and git.changes(PREVIOUS_PUBLIC, PROVENANCE_COMMIT) == {},
            "current-main-first provenance merge identity or first-parent tree mismatch")
    provenance = _step(git, PREVIOUS_PUBLIC, PROVENANCE_COMMIT, "current_main_first_provenance_merge")
    rows = [
        provenance,
        _require_step(git, PROVENANCE_COMMIT, LEASE_ISSUE_COMMIT, LEASE_ISSUE_TREE,
                      "lease_issue", {LEASES}),
        _require_step(git, LEASE_ISSUE_COMMIT, CANDIDATE_FREEZE_COMMIT, CANDIDATE_FREEZE_TREE,
                      "candidate_freeze", set(FIXED_CANDIDATE_PATHS)),
    ]
    before = git.document(PROVENANCE_COMMIT, LEASES)
    issued = git.document(LEASE_ISSUE_COMMIT, LEASES)
    issue = _append_one(before, issued, "events", "lease issue")
    require("supersedes_event_id" not in issue,
            "fresh sibling-root lease issue must not supersede another event")
    expected = {
        "event_id": ISSUE_EVENT, "event": "issued", "state": "active",
        "lease_id": LEASE_ID, "namespace": NAMESPACE,
        "candidate_path": "candidates/" + NAMESPACE, "writer_task": WRITER_TASK,
        "upstream_commit": AUTHORITY_COMMIT, "upstream_tree": AUTHORITY_TREE,
        "writer_contract": "candidates/CONTRACT.md",
    }
    require(all(issue.get(key) == value for key, value in expected.items()),
            "lease issue identity mismatch")
    pointer = git.document(CANDIDATE_FREEZE_COMMIT, CANDIDATE_DIR + "/LEASE.json")
    require(pointer.get("schema") == "mathematics-commons-stacks-candidate-lease-pointer/v1"
            and pointer.get("lease_id") == LEASE_ID and pointer.get("namespace") == NAMESPACE
            and pointer.get("writer_task") == WRITER_TASK
            and pointer.get("upstream_commit") == AUTHORITY_COMMIT,
            "candidate lease pointer mismatch")
    return rows, issue


def _manifest_references(git: Git, revision: str, manifest: dict) -> dict[str, dict[str, object]]:
    values: list[object] = []
    values.extend(manifest.get("source_authorities", []))
    values.extend(manifest.get("builds", []))
    for key in ("stable_unit_manifest", "source_map", "decision_ledger", "rejection_ledger",
                "formula_diagram_inventory"):
        values.append(manifest.get(key))
    refs: dict[str, dict[str, object]] = {}
    for row in values:
        require(isinstance(row, dict) and {"path", "sha256"} <= set(row),
                "candidate manifest has an incomplete reference")
        relative = safe_path(row["path"])
        require(relative not in refs and relative != "candidate.manifest.json",
                "candidate manifest repeats or self-references a path")
        observed = git.ident(revision, CANDIDATE_DIR + "/" + relative)
        require(str(row["sha256"]).upper() == observed["sha256"],
                "candidate manifest hash mismatch: " + relative)
        if "bytes" in row:
            require(type(row["bytes"]) is int and row["bytes"] == observed["bytes"],
                    "candidate manifest byte mismatch: " + relative)
        if "git_blob" in row:
            require(row["git_blob"] == observed["git_blob"],
                    "candidate manifest blob mismatch: " + relative)
        refs[relative] = observed
    inventory = {
        path[len(CANDIDATE_DIR) + 1:]
        for path in git.text("ls-tree", "-r", "--name-only", revision, "--", CANDIDATE_DIR).splitlines()
    }
    require(set(refs) == inventory - {"candidate.manifest.json"},
            "candidate manifest does not close the exact final candidate file inventory")
    return refs


def _review_passes(review: dict) -> bool:
    outcome = review.get("outcome")
    return (review.get("status") == "PASS" and review.get("passed") is True) or (
        isinstance(outcome, dict) and outcome.get("passed") is True
        and outcome.get("status", "PASS") == "PASS"
    )


def _validate_review(review: dict, review_path: str) -> None:
    require(review.get("schema") == "mathematics-commons-stacks-independent-review/v1"
            and review.get("candidate_id") == OVERLAY_ID and _review_passes(review),
            "independent review does not pass the exact candidate")
    require(review.get("review_state", "performed") == "performed"
            and review.get("independent_replay", "passed") == "passed",
            "independent review/replay state is incomplete")
    require(review.get("unresolved_defects", []) == [], "independent review has unresolved defects")
    ids = review.get("stable_ids")
    if ids is None and isinstance(review.get("source_closure"), dict):
        ids = review["source_closure"].get("stable_ids")
    if ids is None and isinstance(review.get("authority"), dict):
        source_units = review["authority"].get("source_units")
        if isinstance(source_units, list):
            ids = [row.get("unit_id") for row in source_units if isinstance(row, dict)]
    require(ids == list(STABLE_IDS), "independent review stable-ID binding mismatch")
    require(review_path.startswith("replay/") and review_path.endswith(".json"),
            "independent review path is noncanonical")


def _validate_candidate(git: Git, review_commit: str, entry: dict) -> dict[str, object]:
    manifest_path = CANDIDATE_DIR + "/candidate.manifest.json"
    manifest = git.document(review_commit, manifest_path)
    require(manifest.get("schema") == "mathematics-commons-stacks-candidate-manifest/v1"
            and manifest.get("candidate_id") == OVERLAY_ID and manifest.get("namespace") == NAMESPACE
            and manifest.get("lease_id") == LEASE_ID and manifest.get("writer_task") == WRITER_TASK,
            "final candidate manifest identity mismatch")
    require(manifest.get("upstream", {}).get("commit") == AUTHORITY_COMMIT
            and manifest.get("upstream", {}).get("tree") == AUTHORITY_TREE,
            "candidate manifest official authority mismatch")
    closure = manifest.get("source_closure", {})
    require(closure.get("enumerated") is True and closure.get("complete") is True
            and closure.get("expected_units") == closure.get("manifested_units") == len(STABLE_IDS),
            "candidate seven-unit source closure mismatch")
    require(manifest.get("review_state") == "performed" and manifest.get("independent_replay") == "passed"
            and manifest.get("unresolved_defects") == [], "final manifest is not independently reviewed")
    refs = _manifest_references(git, review_commit, manifest)

    units = git.document(review_commit, CANDIDATE_DIR + "/" + STABLE_UNITS)
    require(units.get("candidate_id") == OVERLAY_ID and units.get("unit_count") == len(STABLE_IDS)
            and [row.get("id") for row in units.get("units", [])] == list(STABLE_IDS),
            "stable-unit manifest is not the exact seven-ID inventory")
    source_rows = _jsonl(git.blob(review_commit, CANDIDATE_DIR + "/" + SOURCE_MAP), "Verdier source map")
    require([row.get("unit_id") for row in source_rows] == list(STABLE_IDS)
            and [row.get("sequence") for row in source_rows] == list(range(1, len(STABLE_IDS) + 1)),
            "source-map order does not match the seven stable IDs")

    operation_rows = _jsonl(git.blob(review_commit, CANDIDATE_DIR + "/" + COMPOSITION),
                            "Verdier composition")
    require(len(operation_rows) == 1, "Verdier candidate must contain exactly one composition operation")
    operation = operation_rows[0]
    require(operation.get("schema") == "mathematics-commons-stacks-composition-operation/v1"
            and operation.get("operation_id") == "VDR-STK-COMP-0002"
            and operation.get("operation") == "insert_bytes" and operation.get("mode") == "insertion_only",
            "candidate operation is not the exact registered insertion")
    require(operation.get("target", {}).get("path") == TARGET
            and operation.get("payload", {}).get("path") == PAYLOAD,
            "candidate target or payload path mismatch")
    constraints = operation.get("constraints", {})
    require(constraints == {"existing_target_bytes_changed": 0, "delete_bytes": 0,
                            "replace_bytes": 0, "insert_payload_once": True},
            "candidate operation is not insertion-only")
    payload = git.blob(review_commit, CANDIDATE_DIR + "/" + PAYLOAD)
    payload_id = identity(payload)
    require(operation["payload"].get("bytes") == payload_id["bytes"]
            and str(operation["payload"].get("sha256", "")).upper() == payload_id["sha256"]
            and refs[PAYLOAD] == payload_id, "candidate payload hash closure mismatch")
    require(units.get("payload_sha256") == payload_id["sha256"]
            and units.get("composition_operation_id") == operation["operation_id"],
            "stable-unit payload/composition binding mismatch")
    require(all(row.get("composition_operation_id", operation["operation_id"]) == operation["operation_id"]
                and ("payload_sha256" not in row or row["payload_sha256"] == payload_id["sha256"])
                for row in source_rows), "source-map payload/composition binding mismatch")

    lock = git.document(review_commit, CANDIDATE_DIR + "/authority/authority.lock.json")
    require(lock.get("schema") == "mathematics-commons-stacks-verdier-authority-lock/v1"
            and lock.get("authority", {}).get("sha256") ==
                "6214C252BACEBA5584E3C4AEB564C129851941C1A9250BABAB45B79A3939B0AE"
            and lock.get("composition_base", {}).get("pinned_official_stacks_commit") == AUTHORITY_COMMIT
            and lock.get("composition_base", {}).get("pinned_official_stacks_tree") == AUTHORITY_TREE,
            "Verdier authority lock or official Stacks authority mismatch")

    review_logical = entry.get("review_receipt")
    require(isinstance(review_logical, str)
            and review_logical.startswith("candidates/" + NAMESPACE + "/"),
            "registry review path escapes the candidate")
    review_relative = review_logical[len("candidates/" + NAMESPACE + "/"):]
    require(review_relative in refs, "final review is not manifest hash-bound")
    review = git.document(review_commit, CANDIDATE_DIR + "/" + review_relative)
    _validate_review(review, review_relative)
    manifest_id = git.ident(review_commit, manifest_path)
    require(manifest_id["sha256"] == FINAL_MANIFEST_SHA256,
            "unexpected final candidate manifest bytes")
    require(entry.get("manifest_sha256") == manifest_id["sha256"],
            "registry/final-manifest hash mismatch")
    review_id = git.ident(review_commit, CANDIDATE_DIR + "/" + review_relative)
    require(review_id["sha256"] == REVIEW_SHA256, "unexpected independent-review bytes")
    declared_review_sha = entry.get("review_receipt_sha256")
    if declared_review_sha is not None:
        require(declared_review_sha == review_id["sha256"], "registry/review hash mismatch")
    return {
        "manifest": {"path": manifest_path, **manifest_id},
        "review": {"path": CANDIDATE_DIR + "/" + review_relative, **review_id},
        "payload": {"path": CANDIDATE_DIR + "/" + PAYLOAD, **payload_id},
        "operation": {"path": CANDIDATE_DIR + "/" + COMPOSITION,
                      **git.ident(review_commit, CANDIDATE_DIR + "/" + COMPOSITION)},
        "source_map": {"path": CANDIDATE_DIR + "/" + SOURCE_MAP,
                       **git.ident(review_commit, CANDIDATE_DIR + "/" + SOURCE_MAP)},
        "stable_units": {"path": CANDIDATE_DIR + "/" + STABLE_UNITS,
                         **git.ident(review_commit, CANDIDATE_DIR + "/" + STABLE_UNITS)},
        "manifest_reference_count": len(refs),
        "review_relative": review_relative,
        "operation_document": operation,
    }


def _admission_references(receipt: dict) -> set[str]:
    found: set[str] = set()

    def walk(node: object) -> None:
        if isinstance(node, dict):
            if isinstance(node.get("path"), str) and isinstance(node.get("sha256"), str):
                found.add(node["path"])
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(receipt)
    return found


def _validate_preparation(
    git: Git,
    review_commit: str,
    admission_commit: str,
) -> tuple[str, dict[str, object]]:
    """Bind the one tooling-only commit needed to validate this successor.

    The preparation identity cannot be compiled into the validator that it
    introduces.  It is therefore derived from the admission parent and then
    constrained to one exact child of the reviewed packet with an exact path
    and change-type allowlist.
    """
    parents = git.parents(admission_commit)
    require(len(parents) == 1, "registry admission must have exactly one parent")
    preparation_commit = parents[0]
    row = _require_step(
        git,
        review_commit,
        preparation_commit,
        None,
        "validation_tool_preparation",
        set(PREPARATION_PATHS),
    )
    changes = git.changes(review_commit, preparation_commit)
    expected_types = {
        "tools/build_fixed_point.py": "M",
        "tools/direct_successor_checkpoint.py": "M",
        "tools/validate_unified_repository.py": "M",
        "tools/verdier_registered_insertion_successor.py": "A",
        "tools/validate_verdier_registered_insertion_successor.py": "A",
        "tools/tests/test_verdier_registered_insertion_successor.py": "A",
    }
    require({path: data[4] for path, data in changes.items()} == expected_types,
            "validation-tool preparation change types mismatch")
    reviewed_subtree = git.text("rev-parse", review_commit + ":" + CANDIDATE_DIR)
    require(git.text("rev-parse", preparation_commit + ":" + CANDIDATE_DIR)
            == reviewed_subtree,
            "validation-tool preparation changed the reviewed candidate")
    return preparation_commit, row


def _validate_post_composition_repair(
    git: Git,
    composition_commit: str,
    repair_commit: str,
) -> list[dict[str, object]]:
    """Bind failed-closed checkpoint repairs without hiding superseded seals.

    The initial derived receipt proved the composition topology but exposed a
    stale EGA-surface comparison during its verifier-only build gate.  The
    replacement receipt records every superseded one-file seal and exact
    three-file repair commit before any TeX process is launched.
    """
    repair_commit = _commit(git, repair_commit, "post-composition validation repair")
    chain: list[str] = []
    cursor = repair_commit
    while cursor != composition_commit:
        require(len(chain) < 32,
                "post-composition validation-repair chain is unexpectedly long")
        parents = git.parents(cursor)
        require(len(parents) == 1,
                "post-composition validation-repair chain must be single-parent")
        chain.append(cursor)
        cursor = parents[0]
    chain.reverse()
    require(chain and len(chain) % 2 == 0,
            "post-composition chain must alternate receipt seals and repairs")
    expected_types = {
        "tools/direct_successor_checkpoint.py": "M",
        "tools/verdier_registered_insertion_successor.py": "M",
        "tools/tests/test_verdier_registered_insertion_successor.py": "M",
    }
    rows: list[dict[str, object]] = []
    parent = composition_commit
    for index, commit in enumerate(chain):
        if index % 2 == 0:
            rows.append(_require_step(
                git, parent, commit, None, "superseded_receipt_seal", {RECEIPT}))
        else:
            rows.append(_require_step(
                git, parent, commit, None, "post_composition_validation_repair",
                set(POST_COMPOSITION_REPAIR_PATHS)))
            changes = git.changes(parent, commit)
            require({path: data[4] for path, data in changes.items()} == expected_types,
                    "post-composition validation repair change types mismatch")
        parent = commit
    return rows


def _validate_admission(
    git: Git,
    review_commit: str,
    preparation_commit: str,
    admission_commit: str,
    issue: dict,
) -> tuple[list[dict[str, object]], dict, dict[str, object]]:
    row = _require_step(git, preparation_commit, admission_commit, None, "registry_admission",
                        {LEASES, OVERLAYS, ADMISSION_RECEIPT})
    changes = git.changes(preparation_commit, admission_commit)
    require(changes[LEASES][4] == changes[OVERLAYS][4] == "M"
            and changes[ADMISSION_RECEIPT][4] == "A", "admission change types mismatch")
    previous_overlays = git.document(preparation_commit, OVERLAYS)
    current_overlays = git.document(admission_commit, OVERLAYS)
    entry = _append_one(previous_overlays, current_overlays, "registered_entries", "overlay registry")
    require(entry.get("id") == OVERLAY_ID and entry.get("namespace") == NAMESPACE
            and entry.get("source_commit") == AUTHORITY_COMMIT
            and entry.get("source_tree") == AUTHORITY_TREE
            and entry.get("writer") == WRITER_TASK
            and direct.stable_ids(entry) == list(STABLE_IDS),
            "admitted overlay identity or seven stable IDs mismatch")

    previous_leases = git.document(preparation_commit, LEASES)
    current_leases = git.document(admission_commit, LEASES)
    release = _append_one(previous_leases, current_leases, "events", "lease release")
    expected = {
        "event_id": RELEASE_EVENT, "event": "released", "state": "released",
        "lease_id": LEASE_ID, "namespace": NAMESPACE,
        "candidate_path": "candidates/" + NAMESPACE, "writer_task": WRITER_TASK,
        "upstream_commit": AUTHORITY_COMMIT, "upstream_tree": AUTHORITY_TREE,
        "writer_contract": "candidates/CONTRACT.md", "supersedes_event_id": ISSUE_EVENT,
    }
    require(all(release.get(key) == value for key, value in expected.items()),
            "lease release does not exactly supersede " + ISSUE_EVENT)
    require(all(issue.get(key) == release.get(key) for key in (
        "lease_id", "namespace", "candidate_path", "writer_task", "upstream_commit",
        "upstream_tree", "writer_contract", "issued_at_utc")),
        "lease issue/release identity mismatch")
    event_ids = [event.get("event_id") for event in current_leases["events"]]
    require(event_ids == [f"lease-event-{number:06d}" for number in range(1, len(event_ids) + 1)],
            "lease event IDs are not globally sequential")

    candidate = _validate_candidate(git, review_commit, entry)
    subtree = git.text("rev-parse", review_commit + ":" + CANDIDATE_DIR)
    require(subtree == FINAL_CANDIDATE_SUBTREE, "unexpected final reviewed candidate subtree")
    require(git.text("rev-parse", preparation_commit + ":" + CANDIDATE_DIR) == subtree,
            "validation-tool preparation changed the independently reviewed candidate subtree")
    require(git.text("rev-parse", admission_commit + ":" + CANDIDATE_DIR) == subtree,
            "admission changed the independently reviewed candidate subtree")
    admission = git.document(admission_commit, ADMISSION_RECEIPT)
    require(admission.get("schema") == "mathematics-commons-stacks-registry-admission-receipt/v1"
            and str(admission.get("status", "")).startswith("PASS")
            and admission.get("candidate_id") == OVERLAY_ID,
            "admission receipt does not pass the exact candidate")
    if "candidate_commit" in admission:
        require(admission.get("candidate_commit") == review_commit
                and admission.get("candidate_tree") == git.tree(review_commit),
                "admission receipt candidate commit/tree mismatch")
    if "stable_ids" in admission:
        require(admission["stable_ids"] == list(STABLE_IDS), "admission stable-ID mismatch")
    refs = _admission_references(admission)
    required_suffixes = {
        "candidate.manifest.json", candidate["review_relative"], PAYLOAD, COMPOSITION,
        SOURCE_MAP, STABLE_UNITS,
    }
    normalized = {
        path[len("candidates/" + NAMESPACE + "/"):] if path.startswith("candidates/" + NAMESPACE + "/")
        else path[len(CANDIDATE_DIR) + 1:] if path.startswith(CANDIDATE_DIR + "/") else path
        for path in refs
    }
    require(required_suffixes <= normalized, "admission receipt omits decisive candidate references")
    candidate.update({"subtree": subtree, "entry": entry,
                      "admission_receipt": _reference(git, admission_commit, ADMISSION_RECEIPT)})
    return [row], candidate, release


def _run_composer(git: Git, admission: str, source: str) -> dict:
    require(git.ident(PREVIOUS_PUBLIC, COMPOSER) == git.ident(source, COMPOSER),
            "generic registered-insertion composer changed across the successor")
    command = [sys.executable, "-B", str(git.root / COMPOSER), "--overlay-id", OVERLAY_ID,
               "--base-revision", admission, "--check-revision", source]
    completed = subprocess.run(command, cwd=git.root, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               check=False, timeout=300)
    require(completed.returncode == 0,
            "generic registered-insertion dry replay failed: "
            + completed.stderr.decode("utf-8", "replace"))
    report = parse_json(completed.stdout)
    require(isinstance(report, dict)
            and report.get("schema") == "unofficial-ai-integrated-stacks-registered-insertion-composition/v1"
            and report.get("status") == "PASS" and report.get("overlay_id") == OVERLAY_ID
            and report.get("operation_id") == "VDR-STK-COMP-0002"
            and report.get("base_revision") == admission and report.get("check_revision") == source
            and report.get("write_requested") is False and report.get("source") == TARGET,
            "generic composer returned a mismatched report")
    canonical = report.get("canonical_composition", {})
    require(canonical.get("prefix_unchanged") is True and canonical.get("suffix_unchanged") is True
            and canonical.get("payload_occurrences_after") == 1
            and canonical.get("label_occurrences_after") == 1,
            "generic composer did not prove insertion-only prefix/suffix preservation")
    before = git.blob(admission, TARGET)
    after = git.blob(source, TARGET)
    offset = canonical.get("rebased_byte_offset")
    payload_bytes = canonical.get("payload_bytes")
    require(type(offset) is int and type(payload_bytes) is int
            and after[:offset] == before[:offset]
            and after[offset + payload_bytes:] == before[offset:],
            "derived.tex prefix or suffix bytes changed outside the insertion")
    require(identity(before) == {"bytes": canonical.get("before_bytes"),
                                 "sha256": canonical.get("before_sha256"),
                                 "git_blob": canonical.get("before_blob")}
            and identity(after) == {"bytes": canonical.get("composed_bytes"),
                                    "sha256": canonical.get("composed_sha256"),
                                    "git_blob": canonical.get("composed_blob")},
            "generic composer source identities mismatch")
    return report


def _metadata_preserved(git: Git, source: str, endpoint: str, protected: dict[str, dict[str, object]]) -> None:
    git.raw("merge-base", "--is-ancestor", source, endpoint)
    decisive = {OVERLAYS, LEASES, CANDIDATE_DIR + "/candidate.manifest.json",
                CANDIDATE_DIR + "/" + PAYLOAD, CANDIDATE_DIR + "/" + COMPOSITION,
                CANDIDATE_DIR + "/" + SOURCE_MAP, CANDIDATE_DIR + "/" + STABLE_UNITS,
                ADMISSION_RECEIPT, TARGET, COMPOSER}
    decisive.update(protected)
    for path in decisive:
        require(git.ident(source, path) == git.ident(endpoint, path),
                "post-composition decisive input drift: " + path)


def derive_successor(
    source: Path,
    review_commit: str,
    admission_commit: str,
    composition_commit: str,
    validation_repair_commit: str,
    *,
    validation_endpoint: str | None = None,
) -> dict:
    """Derive the complete receipt from three future commit identities."""
    git = Git(source)
    review_commit = _commit(git, review_commit, "independent review")
    admission_commit = _commit(git, admission_commit, "registry admission")
    composition_commit = _commit(git, composition_commit, "source composition")
    validation_repair_commit = _commit(
        git, validation_repair_commit, "post-composition validation repair")
    head = _commit(git, git.text("rev-parse", "HEAD"), "HEAD")
    endpoint = head if validation_endpoint is None else _commit(git, validation_endpoint, "validation endpoint")
    require(endpoint == head, "generic composer replay requires the validation endpoint to be current HEAD")
    previous, correction_inputs = _validate_inherited(git)
    prefix_rows, issue = _validate_fixed_prefix(git)
    review_row = _require_step(git, CANDIDATE_FREEZE_COMMIT, review_commit, None,
                               "independent_review", None)
    review_paths = {row["path"] for row in review_row["paths"]}
    require(review_paths and all(path.startswith(CANDIDATE_DIR + "/") for path in review_paths)
            and CANDIDATE_DIR + "/candidate.manifest.json" in review_paths
            and any(path.startswith(CANDIDATE_DIR + "/replay/") and path.endswith(".json")
                    for path in review_paths),
            "independent-review transition escapes the candidate or omits manifest/review")
    preparation_commit, preparation_row = _validate_preparation(
        git, review_commit, admission_commit)
    admission_rows, candidate, release = _validate_admission(
        git, review_commit, preparation_commit, admission_commit, issue)
    source_row = _require_step(git, admission_commit, composition_commit, None,
                               "registered_insertion_composition", {TARGET})
    require(git.changes(admission_commit, composition_commit)[TARGET][4] == "M",
            "composition must modify the existing derived.tex only")
    report = _run_composer(git, admission_commit, composition_commit)
    post_source_rows = _validate_post_composition_repair(
        git, composition_commit, validation_repair_commit)
    git.raw("merge-base", "--is-ancestor", validation_repair_commit, endpoint)
    _metadata_preserved(git, composition_commit, endpoint, correction_inputs)
    for path, expected in correction_inputs.items():
        require(git.ident(endpoint, path) == expected, "current Illusie protected input drift: " + path)

    old_overlays = git.document(PREVIOUS_PUBLIC, OVERLAYS)["registered_entries"]
    old_leases = git.document(PREVIOUS_PUBLIC, LEASES)["events"]
    current_overlays = git.document(admission_commit, OVERLAYS)["registered_entries"]
    require(current_overlays[:-1] == old_overlays and current_overlays[-1] == candidate["entry"],
            "registry is not the exact one-overlay append to current public main")
    all_ids: list[str] = []
    for entry in current_overlays:
        all_ids.extend(direct.stable_ids(entry))
    require(len(all_ids) == len(set(all_ids)), "registered stable IDs are not globally unique")
    prior_ids: list[str] = []
    for entry in old_overlays:
        prior_ids.extend(direct.stable_ids(entry))
    require(len(prior_ids) == len(set(prior_ids)),
            "immediate public predecessor has duplicate stable IDs")

    canonical = report["canonical_composition"]
    affected = {
        TARGET: {
            "before_bytes": canonical["before_bytes"],
            "before_sha256": canonical["before_sha256"],
            "before_git_blob": canonical["before_blob"],
            "context_bytes": canonical["context_bytes"],
            "context_sha256": canonical["context_sha256"],
            "rebased_byte_offset": canonical["rebased_byte_offset"],
            "payload_bytes": canonical["payload_bytes"],
            "payload_sha256": canonical["payload_sha256"],
            "composed_bytes": canonical["composed_bytes"],
            "composed_sha256": canonical["composed_sha256"],
            "composed_git_blob": canonical["composed_blob"],
            "committed_matches_composition": True,
            "composition_mode": MODE,
            "prefix_unchanged": True,
            "suffix_unchanged": True,
        }
    }
    registry = {
        "cutoff_commit": admission_commit,
        "cutoff_tree": git.tree(admission_commit),
        "registered_overlays": len(current_overlays),
        "registered_stable_ids": len(all_ids),
        "last_admitted_overlay": OVERLAY_ID,
    }
    for name, path in (("overlays", OVERLAYS), ("leases", LEASES)):
        registry[name + "_path"] = path
        registry.update({name + "_" + key: value for key, value in git.ident(admission_commit, path).items()})
    overlay = {
        "id": OVERLAY_ID,
        "topology": "current_main_first_reviewed_registered_insertion",
        "namespace_path": CANDIDATE_DIR,
        "stable_ids": len(STABLE_IDS),
        "stable_id_inventory": list(STABLE_IDS),
        "operations": 1,
        "operation_kind": "registered_insertion",
        "manifest_sha256": candidate["manifest"]["sha256"],
        "review_receipt_sha256": candidate["review"]["sha256"],
        "provenance_commit": PROVENANCE_COMMIT,
        "lease_issue_commit": LEASE_ISSUE_COMMIT,
        "candidate_freeze_commit": CANDIDATE_FREEZE_COMMIT,
        "review_commit": review_commit,
        "preparation_commit": preparation_commit,
        "candidate_commit": review_commit,
        "candidate_tree": git.tree(review_commit),
        "candidate_subtree": candidate["subtree"],
        "admission_commit": admission_commit,
        "admission_parent": preparation_commit,
        "admission_tree": git.tree(admission_commit),
        "lease_issue_event": ISSUE_EVENT,
        "lease_release_event": RELEASE_EVENT,
        "manifest_reference_count": candidate["manifest_reference_count"],
        "manifest": candidate["manifest"],
        "review": candidate["review"],
        "payload": candidate["payload"],
        "operation": candidate["operation"],
        "source_map": candidate["source_map"],
        "stable_units": candidate["stable_units"],
        "admission_receipt": candidate["admission_receipt"],
    }
    preservation = deepcopy(previous.get("preservation", {}))
    preservation[TARGET] = git.ident(composition_commit, TARGET)
    created = datetime.fromtimestamp(
        int(git.text("show", "-s", "--format=%ct", composition_commit)), timezone.utc
    ).isoformat().replace("+00:00", "Z")
    return {
        "schema": SCHEMA,
        "status": "PASS",
        "created_utc": created,
        "authority": {"commit": AUTHORITY_COMMIT, "tree": AUTHORITY_TREE},
        "previous_cutoff": {
            "public_main_head": PREVIOUS_PUBLIC,
            "public_main_tree": PREVIOUS_PUBLIC_TREE,
            "receipt": {"path": RECEIPT, **INHERITED_RECEIPT_ID},
            "schema": ai_correction.SCHEMA,
            "composition_source_commit": previous["composition"]["source_commit"],
            "composition_source_tree": previous["composition"]["source_tree"],
            "registry_commit": previous["registry"]["cutoff_commit"],
            "registry_tree": previous["registry"]["cutoff_tree"],
            "last_admitted_overlay": previous["registry"]["last_admitted_overlay"],
            "source_blobs": {TARGET: git.ident(PREVIOUS_PUBLIC, TARGET)},
            "role": "inherited_composition_cutoff_not_immediate_public_registry_predecessor",
        },
        "immediate_public_registry_predecessor": {
            "commit": PREVIOUS_PUBLIC,
            "tree": PREVIOUS_PUBLIC_TREE,
            "registered_overlays": len(old_overlays),
            "registered_stable_ids": len(prior_ids),
            "lease_events": len(old_leases),
            "last_admitted_overlay": old_overlays[-1]["id"],
            "overlays": _reference(git, PREVIOUS_PUBLIC, OVERLAYS),
            "leases": _reference(git, PREVIOUS_PUBLIC, LEASES),
        },
        "registry": registry,
        "transport": {
            "schema": TRANSPORT_SCHEMA,
            "kind": "current_main_first_linear_registered_insertion",
            "base_commit": PREVIOUS_PUBLIC,
            "base_tree": PREVIOUS_PUBLIC_TREE,
            "cutoff_commit": admission_commit,
            "cutoff_tree": git.tree(admission_commit),
            "source_commit": composition_commit,
            "source_tree": git.tree(composition_commit),
            "commits": [*prefix_rows, review_row, preparation_row, *admission_rows,
                        source_row, *post_source_rows],
            "root_sources_unchanged_before_composition": True,
            "lease_issue_is_fresh_root": True,
            "current_public_ega_errata_preservation_contract": (
                "sealed passing EGA integration evidence plus exact immediate-public-to-Verdier "
                "input preservation; no claim of fresh checker replay against later public errata"
            ),
            "inherited_illusie_validation_contract": (
                "manifest suffix replayed at the exact sealed Illusie validation head; every protected "
                "Illusie byte plus the finite checker and regression suite revalidated at the endpoint"
            ),
        },
        "new_overlays": [overlay],
        "composition": {
            "mode": MODE,
            "base_commit": admission_commit,
            "base_tree": git.tree(admission_commit),
            "source_commit": composition_commit,
            "source_tree": git.tree(composition_commit),
            "new_operations": 1,
            "new_byte_edit_operations": 1,
            "affected_sources": affected,
        },
        "projection_verifier": {
            "path": COMPOSER,
            "command": f"python {COMPOSER} --overlay-id {OVERLAY_ID} --base-revision {admission_commit} --check-revision {composition_commit}",
            "status": "PASS",
            "report": report,
        },
        "required_build_stems": list(EXPECTED_STEMS),
        "preservation": preservation,
        "inherited_ai_source_correction": {
            "receipt": {"path": RECEIPT, **INHERITED_RECEIPT_ID},
            "scope": deepcopy(previous["ai_source_correction_scope"]),
            "source_commit": previous["composition"]["source_commit"],
            "source_tree": previous["composition"]["source_tree"],
            "validation_head": INHERITED_RECEIPT_HEAD,
            "validation_tree": INHERITED_RECEIPT_TREE,
        },
        "correction_protected_inputs": correction_inputs,
        "verdier_registered_insertion_scope": {
            "candidate_id": OVERLAY_ID,
            "operation_id": "VDR-STK-COMP-0002",
            "stable_ids": list(STABLE_IDS),
            "candidate_freeze_commit": CANDIDATE_FREEZE_COMMIT,
            "review_commit": review_commit,
            "preparation_commit": preparation_commit,
            "admission_commit": admission_commit,
            "composition_commit": composition_commit,
            "validation_repair_commit": validation_repair_commit,
            "lease_issue_event": ISSUE_EVENT,
            "lease_release_event": RELEASE_EVENT,
        },
    }


def protected_tools(git: Git, revision: str) -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for path in TOOLS:
        git.clean_file(revision, path)
        result[path] = git.ident(revision, path)
    return result


def recheck_verdier_successor_tools(source: Path, binding: dict) -> None:
    require(binding.get("schema") == SCHEMA, "wrong Verdier successor binding schema")
    git = Git(source)
    head = _commit(git, git.text("rev-parse", "HEAD"), "HEAD")
    require(binding.get("direct_validation_tools") == protected_tools(git, head),
            "Verdier successor validation tools changed")
    protected = binding.get("correction_protected_inputs")
    require(isinstance(protected, dict) and protected, "Verdier successor lacks inherited Illusie inputs")
    for path, expected in protected.items():
        _valid_identity(expected, path)
        require(git.ident(head, path) == expected, "inherited Illusie protected input drift: " + path)
        git.clean_file(head, path, exact=True)


def normalize_binding(git: Git, head: str, receipt: dict) -> dict[str, object]:
    """Return the exact shape consumed by ``build_fixed_point``."""
    registry, composition, previous = receipt["registry"], receipt["composition"], receipt["previous_cutoff"]
    overlay = receipt["new_overlays"][0]
    receipt_id = git.ident(head, RECEIPT)
    affected = tuple(sorted(path[:-4] for path in composition["affected_sources"]))
    binding: dict[str, object] = {
        "schema": SCHEMA,
        "receipt": RECEIPT,
        "receipt_sha256": receipt_id["sha256"],
        "receipt_git_blob": receipt_id["git_blob"],
        "authority_commit": AUTHORITY_COMMIT,
        "authority_tree": AUTHORITY_TREE,
        "previous_public_main_head": previous["public_main_head"],
        "previous_public_main_tree": previous["public_main_tree"],
        "previous_registry_commit": previous["registry_commit"],
        "previous_last_admitted_overlay": previous["last_admitted_overlay"],
        "previous_source_blobs": previous["source_blobs"],
        "previous_receipt": previous["receipt"],
        "composition_mode": composition["mode"],
        "composition_base_commit": composition["base_commit"],
        "composition_base_tree": composition["base_tree"],
        "composition_source_commit": composition["source_commit"],
        "composition_source_tree": composition["source_tree"],
        "registry_cutoff_commit": registry["cutoff_commit"],
        "registry_cutoff_tree": registry["cutoff_tree"],
        "registered_overlays": registry["registered_overlays"],
        "registered_stable_ids": registry["registered_stable_ids"],
        "last_admitted_overlay": registry["last_admitted_overlay"],
        "new_overlays": receipt["new_overlays"],
        "new_overlay_ids": [OVERLAY_ID],
        "new_overlay_candidate_commits": [overlay["candidate_commit"]],
        "new_overlay_intake_commits": [overlay["lease_issue_commit"]],
        "new_overlay_admission_commits": [overlay["admission_commit"]],
        "required_build_stems": list(EXPECTED_STEMS),
        "affected_source_stems": list(affected),
        "affected_source_identities": composition["affected_sources"],
        "transport": receipt["transport"],
        "direct_validation_tools": protected_tools(git, head),
        "verifier_reports": {"registered_insertion": receipt["projection_verifier"]["report"]},
        "ai_source_correction_scope": receipt["inherited_ai_source_correction"]["scope"],
        "inherited_ai_source_commit": receipt["inherited_ai_source_correction"]["source_commit"],
        "inherited_ai_source_tree": receipt["inherited_ai_source_correction"]["source_tree"],
        "inherited_ai_validation_head": receipt["inherited_ai_source_correction"]["validation_head"],
        "inherited_ai_validation_tree": receipt["inherited_ai_source_correction"]["validation_tree"],
        "correction_protected_inputs": receipt["correction_protected_inputs"],
        "verdier_registered_insertion_scope": receipt["verdier_registered_insertion_scope"],
    }
    for name in ("overlays", "leases"):
        for key in ("path", "git_blob", "sha256"):
            binding[f"registry_{name}_{key}"] = registry[f"{name}_{key}"]
    return binding


def load_verdier_registered_insertion_successor(
    source: Path,
    requested_path: Path = Path(RECEIPT),
) -> tuple[dict[str, object], tuple[str, ...], tuple[str, ...]]:
    git = Git(source)
    path = Path(requested_path)
    absolute = (git.root / path).resolve() if not path.is_absolute() else path.resolve()
    require(absolute.is_relative_to(git.root)
            and absolute.relative_to(git.root).as_posix() == RECEIPT,
            "Verdier successor requires the canonical composition pointer")
    head = _commit(git, git.text("rev-parse", "HEAD"), "HEAD")
    git.clean_file(head, RECEIPT, exact=True)
    saved = git.document(head, RECEIPT)
    require(saved.get("schema") == SCHEMA and saved.get("status") == "PASS",
            "invalid Verdier registered-insertion successor receipt")
    scope = saved.get("verdier_registered_insertion_scope", {})
    expected = derive_successor(
        source,
        scope.get("review_commit"),
        scope.get("admission_commit"),
        scope.get("composition_commit"),
        scope.get("validation_repair_commit"),
    )
    require(saved == expected, "saved Verdier successor receipt differs from exact derivation")
    binding = normalize_binding(git, head, saved)
    require(tuple(binding["required_build_stems"]) == EXPECTED_STEMS
            and binding["affected_source_stems"] == ["derived"],
            "Verdier successor build profile mismatch")
    recheck_verdier_successor_tools(source, binding)
    require(git.text("rev-parse", "HEAD") == head, "HEAD moved while loading Verdier successor")
    return binding, EXPECTED_STEMS, ("derived",)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("."))
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--review-commit")
    parser.add_argument("--admission-commit")
    parser.add_argument("--composition-commit")
    parser.add_argument("--validation-repair-commit")
    args = parser.parse_args(argv)
    if args.check:
        require(not any((args.review_commit, args.admission_commit, args.composition_commit,
                         args.validation_repair_commit)),
                "--check does not accept derivation commits")
        binding, stems, affected = load_verdier_registered_insertion_successor(args.source)
        print(json.dumps({"status": "PASS", "source": binding["composition_source_commit"],
                          "stems": stems, "affected": affected}))
        return 0
    require(all((args.review_commit, args.admission_commit, args.composition_commit,
                 args.validation_repair_commit)),
            "derivation requires review, admission, composition, and validation-repair commits")
    receipt = derive_successor(args.source, args.review_commit, args.admission_commit,
                               args.composition_commit, args.validation_repair_commit)
    print(json.dumps(receipt, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError,
            subprocess.SubprocessError) as exc:
        print("Verdier registered-insertion successor: FAIL\n- " + str(exc), file=sys.stderr)
        raise SystemExit(1)
