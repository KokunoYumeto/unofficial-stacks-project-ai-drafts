#!/usr/bin/env python3
"""Validate embedded registry successors against immutable committed evidence."""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
if __package__:
    from . import direct_successor_common as _helper
else:
    import direct_successor_common as _helper

Git, require, identity = _helper.Git, _helper.require, _helper.identity
safe_path, parse_json = _helper.safe_path, _helper.parse_json
stable_ids, integer = _helper.stable_ids, _helper.integer
SCHEMA = "unofficial-ai-integrated-stacks-direct-composition/v1"
TRANSPORT = "unofficial-ai-integrated-stacks-embedded-registry-successor/v1"
PREFIX = "ai-integrated/"
OVERLAYS = PREFIX + "registry/overlays.json"
LEASES = PREFIX + "registry/leases.json"
RECEIPT = _helper.RECEIPT
COMPOSER = _helper.COMPOSER
DIRECT_TOOLS = (
    "tools/direct_successor_common.py",
    "tools/direct_successor_composition.py",
    "tools/write_direct_successor_receipt.py",
    "tools/validate_direct_successor_release.py",
    "tools/direct_successor_checkpoint.py",
    "tools/tex_process_guard.py",
    "tools/tex_process_public_receipt.py",
    "tools/instrument_r48_synctex.py",
    "tools/map_r48_visual_loci.py",
)
PREPARATION_TOOLS = frozenset((*DIRECT_TOOLS,
    "tools/build_fixed_point.py", "tools/validate_unified_repository.py",
    "tools/test_direct_successor_composition.py", "tools/test_validate_direct_successor_release.py",
    "tools/test_direct_successor_checkpoint.py", "tools/compare_fixed_point_builds.py",
    "tests/test_tex_process_guard.py", "tests/test_r48_visual_loci.py",
    "tests/test_r48_synctex_instrumentation.py", "tests/test_changes_from_upstream.py",
    "tests/test_build_fixed_point_mutex.py", "tools/test_tex_process_public_receipt.py",
    "tools/package_direct_successor_pdfs.py", "tests/test_direct_successor_pdf_package.py"))
MUTABLE_METADATA = frozenset({RECEIPT, "validation/direct-successor-current.json",
    "README.md", "ai-integrated/README.md", "STATUS.md", "VALIDATION.md",
    "validation/README.md", ".github/workflows/validate.yml", "CHANGES_FROM_UPSTREAM.md",
    "ai-integrated/changes/index.html", "validation/changes-from-upstream-2026-08-30.json"})


def validate_metadata_suffix(git, source, head):
    """Allow only explicit tooling/metadata after the source endpoint.

    Existing historical receipts and every source/registry path are protected.
    New direct validation receipts are additive, except the two explicit current
    pointers. Executable tools are separately bound in each build receipt.
    """
    result, parent = [], source
    for commit in git.linear(source, head):
        changes = git.changes(parent, commit)
        regular_changes(changes)
        for path, row in changes.items():
            additive_receipt = re.fullmatch(r"validation/direct-successor-[A-Za-z0-9._-]+\.json", path)
            require(path in PREPARATION_TOOLS or path in MUTABLE_METADATA or
                    (additive_receipt is not None and row[4] == "A"),
                    f"protected metadata suffix changed unsupported path: {path}")
        result.append(step_row(git, parent, commit, "protected_metadata"))
        parent = commit
    require(parent == head, "metadata suffix does not reach current HEAD")
    return result


def append_exact(before, after, field, count=1):
    require(isinstance(before, dict) and isinstance(after, dict), "append inputs must be objects")
    old, new = before.get(field), after.get(field)
    require(isinstance(old, list) and isinstance(new, list), f"invalid append list: {field}")
    require(new[:len(old)] == old and len(new) == len(old) + count,
            f"not an exact {count}-row {field} append")
    require({k: v for k, v in before.items() if k != field} ==
            {k: v for k, v in after.items() if k != field}, "append changed header")
    return new[len(old):]


def regular_changes(changes):
    require(changes and all(row[4] in {"A", "M"} and row[1] == "100644"
                           and row[0] in {"000000", "100644"} for row in changes.values()),
            "empty commit, deletion, or file-type change is unsupported")


def committed_reference(git, commit, directory, reference):
    require(isinstance(reference, dict) and {"path", "bytes", "sha256"}.issubset(reference),
            "incomplete committed reference")
    path = directory + safe_path(reference["path"])
    observed = git.ident(commit, path)
    require(type(reference["bytes"]) is int and reference["bytes"] == observed["bytes"]
            and isinstance(reference["sha256"], str)
            and reference["sha256"].upper() == observed["sha256"], "committed reference identity mismatch")
    if "git_blob" in reference:
        require(reference["git_blob"] == observed["git_blob"], "committed reference blob mismatch")
    return {"path": path, **observed}


def manifest_closure(git, commit, directory, node):
    rows = []
    if isinstance(node, dict):
        if "path" in node:
            rows.append(committed_reference(git, commit, directory + "/", node))
        for value in node.values():
            rows.extend(manifest_closure(git, commit, directory, value))
    elif isinstance(node, list):
        for value in node:
            rows.extend(manifest_closure(git, commit, directory, value))
    return rows


def step_row(git, parent, commit, kind):
    changes = git.changes(parent, commit)
    return {"commit": commit, "parent": parent, "tree": git.tree(commit), "kind": kind,
            "paths": [{"path": path, "old_mode": row[0], "mode": row[1],
                       "old_blob": row[2], "git_blob": row[3], "status": row[4],
                       "bytes": git.ident(commit, path)["bytes"],
                       "sha256": git.ident(commit, path)["sha256"]}
                      for path, row in sorted(changes.items())]}


def lease_identity(issue, release, entry, manifest):
    expected = {"lease_id": manifest.get("lease_id"), "namespace": entry["namespace"],
                "candidate_path": "candidates/" + entry["namespace"],
                "writer_task": entry.get("writer"), "upstream_commit": entry.get("source_commit"),
                "upstream_tree": entry.get("source_tree"), "writer_contract": "candidates/CONTRACT.md"}
    require(all(isinstance(value, str) and value for value in expected.values()), "empty lease identity")
    require(all(issue.get(key) == value and release.get(key) == value for key, value in expected.items()),
            "lease/candidate identity mismatch")
    require(issue.get("event") == "issued" and issue.get("state") == "active"
            and release.get("event") == "released" and release.get("state") == "released",
            "lease state mismatch")
    require(isinstance(issue.get("event_id"), str) and issue["event_id"]
            and isinstance(release.get("event_id"), str) and release["event_id"]
            and release["event_id"] != issue["event_id"]
            and release.get("supersedes_event_id") == issue["event_id"], "lease event binding mismatch")


def lease_document_binding(git, intake, candidate, admission, directory, issue):
    path = directory + "/LEASE.json"
    document = git.document(intake, path)
    expected = {"schema": "mathematics-commons-stacks-candidate-lease/v1",
                "lease_event": issue["event_id"], "lease_id": issue["lease_id"],
                "namespace": issue["namespace"], "candidate_path": issue["candidate_path"],
                "writer_task": issue["writer_task"], "status": "active",
                "authority_commit": issue["upstream_commit"], "authority_tree": issue["upstream_tree"]}
    require(all(document.get(key) == value for key, value in expected.items()),
            "candidate LEASE.json is not bound to its issued event")
    require(git.blob(intake, path) == git.blob(candidate, path) == git.blob(admission, path),
            "candidate LEASE.json changed after issue")


def final_review_binding(review, entry, operation_count):
    round_number = _helper.ROUND.fullmatch(entry["id"]).group(1)
    if review.get("schema") == "stacks-r48-independent-final-frozen-stage-review/v1":
        require(round_number == "48" and review.get("candidate_id") == entry["id"]
                and review.get("passed") is True
                and review.get("status") == "PASS_FINAL_FROZEN_STAGE_WITH_DOCUMENTED_LIMITATIONS"
                and review.get("failures") == [] and review.get("blocking_findings") == [],
                "R48 frozen review type/identity/pass mismatch")
        scope = review.get("scope", {})
        for key in ("actual_frozen_stage_review", "exact_file_set_and_hashes",
                    "source_forward_reverse_replay"):
            require(scope.get(key) is True, f"R48 review lacks {key}")
        tests = review.get("tests")
        require(isinstance(tests, list), "R48 review test inventory missing")
        replay_tests = [item for item in tests if item.get("id") == "source_replay"]
        require(len(replay_tests) == 1 and replay_tests[0].get("result") == "PASS",
                "R48 review source replay is not a unique PASS")
        chapters = replay_tests[0].get("chapters", [])
        require(chapters and all(item.get("forward_reverse_exact") is True for item in chapters)
                and sum(integer(item.get("operations"), "R48 chapter operations", 1)
                        for item in chapters) == operation_count,
                "R48 frozen review does not bind all exact source operations")
        require(isinstance(review.get("bound_evidence"), list) and review["bound_evidence"],
                "R48 frozen review has no bound evidence")
        return
    require(review.get("schema") == f"stacks-r{round_number}-final-independent-review/v1"
            and review.get("candidate_id") == entry["id"] and review.get("passed") is True
            and review.get("status", "PASS") == "PASS", "independent final review type/identity/pass mismatch")
    units, replay = review.get("identity_replay", {}), review.get("source_replay", {})
    require(units.get("stable_ids") == stable_ids(entry) and units.get("stable_ids_unique") is True
            and units.get("operation_ids_unique") is True, "independent review stable-unit binding mismatch")
    require(integer(replay.get("operations"), "review operations", 1) == operation_count
            and integer(replay.get("exact_preimages"), "review preimages", 1) == operation_count
            and integer(replay.get("semantic_units"), "review units", 1) == len(stable_ids(entry))
            and replay.get("nonoverlapping") is True and replay.get("descending_byte_replay_payload_exact") is True
            and integer(replay.get("unlisted_byte_changes"), "review unlisted changes") == 0,
            "independent review source-replay binding mismatch")


def check_admission_evidence(git, candidate, admission, entry, manifest, operation_count):
    """Use the current registrar's explicit admission-receipt shape, not prose."""
    directory = PREFIX + "candidates/" + entry["namespace"]
    path = PREFIX + "registry/admission-receipts/" + entry["namespace"].rsplit("/", 1)[1] + ".json"
    receipt = git.document(admission, path)
    frozen = receipt.get("status") == "PASS_CANDIDATE_REVIEW_AND_FRESH_CHECKOUT"
    require(receipt.get("schema") == "mathematics-commons-stacks-registry-admission-receipt/v1"
            and receipt.get("status") in {"PASS", "PASS_CANDIDATE_REVIEW_AND_FRESH_CHECKOUT"}
            and receipt.get("candidate_id") == entry["id"],
            "admission evidence type/state/identity mismatch")
    require(receipt.get("candidate_commit") == candidate and receipt.get("candidate_tree") == git.tree(candidate),
            "admission evidence candidate binding mismatch")
    refs = {}
    for key, relative in (("manifest", "candidate.manifest.json"),
                          ("operation_spec", "operation-spec.json"),
                          ("source_map", "source-map.jsonl")):
        expected = "candidates/" + entry["namespace"] + "/" + relative if frozen and key == "manifest" else relative
        require(receipt.get(key, {}).get("path") == expected, "admission reference path mismatch")
        refs[key] = committed_reference(git, candidate, PREFIX if frozen and key == "manifest" else directory + "/", receipt[key])
    review_path = safe_path(entry.get("review_receipt"))
    logical_directory = "candidates/" + entry["namespace"] + "/"
    require(review_path.startswith(logical_directory), "review escapes candidate namespace")
    review_relative = review_path[len(logical_directory):]
    review_key = "final_independent_review" if frozen else "final_review"
    require(receipt.get(review_key, {}).get("path") == review_relative, "admission review path mismatch")
    refs["final_review"] = committed_reference(git, candidate, directory + "/", receipt[review_key])
    review = git.document(candidate, PREFIX + review_path)
    final_review_binding(review, entry, operation_count)
    if frozen:
        require(review.get("schema") == "stacks-r48-independent-final-frozen-stage-review/v1",
                "unsupported frozen admission review schema")
        manifest_closure(git, candidate, directory, review["bound_evidence"])
        committed_reference(git, candidate, directory + "/", review["stage_identity"])
    else:
        manifest_closure(git, candidate, directory, review)
    require(manifest.get("review_state") == "performed" and manifest.get("independent_replay") == "passed",
            "manifest review/replay not complete")
    require(receipt.get("stable_ids") == stable_ids(entry)
            and integer(receipt.get("units" if frozen else "stable_id_count"), "admission stable IDs", 1) == len(stable_ids(entry)),
            "admission stable-ID inventory mismatch")
    if frozen:
        fresh = receipt.get("fresh_candidate_checkout", {})
        replay = fresh.get("source_replay", {})
        source_replays = replay.get("source_replays", {})
        require(fresh.get("passed") is True
                and fresh.get("worktree_index_commit_and_fresh_bytes_equal") is True
                and replay.get("passed") is True and replay.get("writes") is False
                and integer(replay.get("units"), "fresh units", 1) == len(stable_ids(entry))
                and integer(replay.get("operations"), "fresh operations", 1) == operation_count
                and source_replays and all(item.get("exact_replay") is True for item in source_replays.values())
                and sum(integer(item.get("operations"), "fresh chapter operations", 1)
                        for item in source_replays.values()) == operation_count,
                "frozen admission fresh replay mismatch")
    else:
        replay = receipt.get("fresh_replay", {})
        require(replay.get("passed") is True and replay.get("exact_preimages_descending_byte_replay") is True
                and integer(replay.get("operations"), "admission operation count", 1) == operation_count,
                "admission replay count/state mismatch")
    return {"path": path, **git.ident(admission, path), "references": refs}


def derive_direct_lifecycle(git, previous_public, cutoff, suffix, inventory, authority):
    """Consume actual one-parent issue -> candidate(s) -> admission transactions.

    Every consumed path is embedded. This deliberately has no import mapping.
    Metadata interludes or outstanding post-admission leases fail closed; their
    topology needs an explicit additional contract, not a fabricated transport.
    """
    commits = git.linear(previous_public, cutoff)
    require(commits, "direct registry suffix is empty")
    cursor, index, rows, overlays = previous_public, 0, [], []
    for entry in suffix:
        directory = PREFIX + "candidates/" + safe_path(entry["namespace"])
        require(entry["source_commit"] == authority["commit"] and entry["source_tree"] == authority["tree"],
                "registry authority mismatch")
        require(index < len(commits), "missing lease issue commit")
        intake = commits[index]
        changes = git.changes(cursor, intake)
        regular_changes(changes)
        expected = {LEASES, directory + "/LEASE.json", directory + "/.gitattributes"}
        require(LEASES in changes and directory + "/LEASE.json" in changes and set(changes) <= expected,
                "direct issue commit escapes exact lease scope")
        require(all(row[4] == ("M" if path == LEASES else "A") for path, row in changes.items()),
                "lease issue mutated an existing candidate file")
        issue = append_exact(git.document(cursor, LEASES), git.document(intake, LEASES), "events")[0]
        issued_document = git.document(intake, LEASES)
        rows.append(step_row(git, cursor, intake, "lease_issue"))
        intake_parent, cursor, index = cursor, intake, index + 1
        candidate_commits = []
        while index < len(commits) and OVERLAYS not in git.changes(cursor, commits[index]):
            commit = commits[index]
            changes = git.changes(cursor, commit)
            regular_changes(changes)
            require(all(path.startswith(directory + "/") for path in changes),
                    "direct candidate commit escapes its candidate namespace")
            rows.append(step_row(git, cursor, commit, "candidate"))
            candidate_commits.append(commit)
            cursor, index = commit, index + 1
        require(candidate_commits and index < len(commits), "candidate or admission commit missing")
        candidate, admission = cursor, commits[index]
        manifest = git.document(candidate, directory + "/candidate.manifest.json")
        require(manifest.get("candidate_id") == entry["id"] and manifest.get("namespace") == entry["namespace"]
                and manifest.get("writer_task") == entry.get("writer"), "manifest candidate/writer mismatch")
        require(manifest.get("upstream", {}).get("commit") == authority["commit"]
                and manifest["upstream"].get("tree") == authority["tree"], "manifest authority mismatch")
        closure_state = manifest.get("source_closure", {})
        require(closure_state.get("complete") is True and closure_state.get("enumerated") is True
                and integer(closure_state.get("expected_units"), "expected closure units", 1) == len(stable_ids(entry))
                and integer(closure_state.get("manifested_units"), "manifested closure units", 1) == len(stable_ids(entry)),
                "manifest stable-unit closure mismatch")
        for key in ("builds", "source_authorities"):
            require(isinstance(manifest.get(key), list) and manifest[key], "missing manifest closure list")
        for key in ("source_map", "decision_ledger", "rejection_ledger", "stable_unit_manifest", "formula_diagram_inventory"):
            require(isinstance(manifest.get(key), dict) and {"path", "bytes", "sha256"} <= set(manifest[key]),
                    "missing mandatory manifest reference")
        manifest_id = git.ident(candidate, directory + "/candidate.manifest.json")
        require(manifest_id["sha256"] == entry["manifest_sha256"].upper(), "admission manifest hash mismatch")
        closure = manifest_closure(git, candidate, directory, manifest)
        changes = git.changes(candidate, admission)
        regular_changes(changes)
        receipt_path = PREFIX + "registry/admission-receipts/" + entry["namespace"].rsplit("/", 1)[1] + ".json"
        require(set(changes) == {LEASES, OVERLAYS, receipt_path}
                and all(row[4] == ("A" if path == receipt_path else "M") for path, row in changes.items()),
                "direct admission escapes exact registry-only scope")
        require(git.document(candidate, LEASES) == issued_document, "candidate changed lease state")
        release = append_exact(issued_document, git.document(admission, LEASES), "events")[0]
        lease_identity(issue, release, entry, manifest)
        lease_document_binding(git, intake, candidate, admission, directory, issue)
        old_events = git.document(intake_parent, LEASES)["events"]
        all_ids = [event.get("event_id") for event in old_events + [issue, release]]
        require(all_ids == [f"lease-event-{n:06d}" for n in range(1, len(all_ids) + 1)],
                "lease event IDs are not the exact global sequential inventory")
        admitted = append_exact(git.document(candidate, OVERLAYS), git.document(admission, OVERLAYS), "registered_entries")
        require(admitted == [entry], "admission appends the wrong entry")
        subtree = git.text("rev-parse", candidate + ":" + directory)
        for revision in (admission, cutoff):
            require(git.text("rev-parse", revision + ":" + directory) == subtree,
                    "frozen candidate subtree changed after admission")
        evidence = check_admission_evidence(git, candidate, admission, entry, manifest, inventory[entry["id"]]["operations"])
        rows.append(step_row(git, candidate, admission, "admission"))
        overlays.append({"id": entry["id"], "topology": "embedded_leased_candidate_then_admission",
                         "lease_binding_schema": TRANSPORT, "namespace_path": directory,
                         "stable_ids": len(stable_ids(entry)), "operations": inventory[entry["id"]]["operations"],
                         "manifest_sha256": manifest_id["sha256"],
                         "review_receipt_sha256": evidence["references"]["final_review"]["sha256"],
                         "intake_commit": intake, "intake_parent": intake_parent, "intake_tree": git.tree(intake),
                         "candidate_commits": candidate_commits, "candidate_commit": candidate,
                         "candidate_tree": git.tree(candidate), "candidate_subtree": subtree,
                         "admission_commit": admission, "admission_parent": candidate, "admission_tree": git.tree(admission),
                         "lease_issue_event": issue["event_id"], "lease_release_event": release["event_id"],
                         "manifest_reference_count": len(closure), "admission_receipt": evidence})
        cursor, index = admission, index + 1
    require(index == len(commits) and cursor == cutoff, "unconsumed registry commits after final admission")
    return {"schema": TRANSPORT, "kind": "embedded_direct", "prefix": PREFIX,
            "base_commit": previous_public, "base_tree": git.tree(previous_public),
            "cutoff_commit": cutoff, "cutoff_tree": git.tree(cutoff), "commits": rows,
            "root_sources_unchanged_before_composition": True}, overlays


def derive(repo, previous_public, cutoff, source):
    git = Git(repo)
    previous_public, cutoff, source = [git.commit(value) for value in (previous_public, cutoff, source)]
    observed_head = git.commit(git.text("rev-parse", "HEAD"))
    validate_metadata_suffix(git, source, observed_head)
    require(git.parents(source) == [cutoff], "direct composition must immediately follow the registry cutoff")
    previous = git.document(previous_public, RECEIPT)
    require(previous.get("schema") in {_helper.SCHEMA, SCHEMA} and previous.get("status") == "PASS",
            "unsupported or nonpassing inherited receipt")
    old = git.document(previous_public, OVERLAYS)
    prior_cutoff = git.commit(previous["registry"]["cutoff_commit"])
    require(git.tree(prior_cutoff) == previous["registry"]["cutoff_tree"], "inherited registry tree mismatch")
    prior_prefix = PREFIX if previous["schema"] == SCHEMA else ""
    for name in ("overlays", "leases"):
        require(git.blob(previous_public, PREFIX + f"registry/{name}.json") ==
                git.blob(prior_cutoff, prior_prefix + f"registry/{name}.json"), "inherited registry bytes differ from historical cutoff")
    require(previous["registry"]["last_admitted_overlay"] == old["registered_entries"][-1]["id"],
            "inherited overlay cutoff mismatch")
    git.raw("merge-base", "--is-ancestor", previous["composition"]["source_commit"], previous_public)
    current = git.document(cutoff, OVERLAYS)
    suffix, new_rounds, stable_count = _helper.admitted_suffix(old, current)
    existing = _helper.previous_rounds(previous)
    target = existing + new_rounds
    arguments = _helper.composer_arguments(existing, target, cutoff, source)
    authority = deepcopy(previous["authority"])
    authority_commit = git.commit(authority["commit"])
    require(git.tree(authority_commit) == authority["tree"], "authority tree mismatch")
    inventory = _helper.target_inventory(git, cutoff, current["registered_entries"], target, new_rounds)
    transport, overlays = derive_direct_lifecycle(git, previous_public, cutoff, suffix, inventory, authority)
    for entry in suffix:
        path = PREFIX + "candidates/" + entry["namespace"] + "/source-map.jsonl"
        for line in git.blob(cutoff, path).splitlines():
            if line.strip():
                require(all(op.get("supersedes_operation_id") is None for op in parse_json(line).get("operations", [])),
                        "new supersessions require a separate contract")
    for name in ("overlays", "leases"):
        git.clean_file(source, PREFIX + f"registry/{name}.json", exact=True)
    tools = {}
    for path in (COMPOSER, "tools/verify_overlay_projection.py"):
        git.clean_file(source, path)
        require(git.ident(previous_public, path) == git.ident(source, path), "registrar transaction changed a composition tool")
        tools[path] = git.ident(source, path)
    result = subprocess.run([sys.executable, "-B", str(git.root / COMPOSER), *arguments], cwd=git.root,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False, timeout=300)
    require(result.returncode == 0, "read-only composer failed: " + result.stderr.decode("utf-8", "replace"))
    projection = parse_json(result.stdout)
    new_ids = [entry["id"] for entry in suffix]
    affected, operation_count = _helper.check_projection(projection, existing, target, cutoff, source,
                                                        inventory, new_ids, git, previous_public)
    for path, row in affected.items():
        auth = git.ident(authority_commit, path)
        require(row["authority_bytes"] == auth["bytes"] and row["authority_sha256"] == auth["sha256"],
                "projection authority identity mismatch")
        row.update({"authority_git_blob": auth["git_blob"], "committed_matches_composition": True,
                    "composition_mode": "Fresh manifest-bound edits on unchanged cumulative preimage"})
    profile = _helper.full_profile(previous, affected)
    preserved, preservation = {}, deepcopy(previous.get("preservation", {}))
    roots = sorted({stem + ".tex" for stem in profile} | {path for path in preservation if _helper.ROOT_TEX.fullmatch(path)})
    for path in roots:
        before, after = git.ident(previous_public, path), git.ident(source, path)
        require(before == git.ident(cutoff, path), "root changed during registry transaction")
        if path not in affected:
            require(before == after, "unaffected retained root changed")
        preserved[path] = {"before": before, "after": after, "newly_affected": path in affected}
        preservation[path] = after
    extensions = {}
    for path in git.text("ls-tree", "-d", "--name-only", previous_public, "--").splitlines():
        if path == "fac" or path.startswith("fac_") or path == "illusie" or path.startswith("illusie_"):
            trees = [git.text("rev-parse", commit + ":" + path) for commit in (previous_public, cutoff, source)]
            require(len(set(trees)) == 1, "FAC/Illusie extension changed")
            extensions[path] = trees[0]
    require("fac" in extensions and any(path.startswith("illusie") for path in extensions),
            "FAC/Illusie extension identities unavailable")
    registry = {"cutoff_commit": cutoff, "cutoff_tree": git.tree(cutoff),
                "registered_overlays": len(current["registered_entries"]), "registered_stable_ids": stable_count,
                "last_admitted_overlay": current["registered_entries"][-1]["id"]}
    for name in ("overlays", "leases"):
        path = PREFIX + f"registry/{name}.json"
        registry[name + "_path"] = path
        registry.update({name + "_" + key: value for key, value in git.ident(cutoff, path).items()})
    created = datetime.fromtimestamp(int(git.text("show", "-s", "--format=%ct", source)), timezone.utc).isoformat().replace("+00:00", "Z")
    receipt = {"schema": SCHEMA, "status": "PASS", "created_utc": created, "authority": authority,
               "previous_cutoff": {"public_main_head": previous_public, "public_main_tree": git.tree(previous_public),
                                   "registry_commit": prior_cutoff, "registry_tree": git.tree(prior_cutoff),
                                   "registry_path_prefix": prior_prefix,
                                   "last_admitted_overlay": old["registered_entries"][-1]["id"],
                                   "receipt": {"path": RECEIPT, **git.ident(previous_public, RECEIPT)},
                                   "source_blobs": {path: git.ident(previous_public, path) for path in sorted(affected)}},
               "registry": registry, "transport": transport, "new_overlays": overlays,
               "composition": {"mode": _helper.MODE, "base_commit": cutoff, "base_tree": git.tree(cutoff),
                               "source_commit": source, "source_tree": git.tree(source),
                               "new_operations": operation_count, "new_byte_edit_operations": operation_count,
                               "total_v2_operations": integer(previous["composition"]["total_v2_operations"], "inherited operation total") + operation_count,
                               "r1_r3_replacements": integer(previous["composition"]["r1_r3_replacements"], "historical replacements"),
                               "r1_tag_additions": integer(previous["composition"]["r1_tag_additions"], "historical tags"),
                               "semantic_dispositions": projection["semantic_dispositions"], "affected_sources": affected},
               "projection_verifier": {"path": COMPOSER, "command": " ".join(["python", COMPOSER, *arguments]), "status": "PASS"},
               "required_build_stems": profile, "preservation": preservation,
               "known_admitted_metadata_defects": deepcopy(previous.get("known_admitted_metadata_defects", []))}
    # The composer reads declared working files. Rehash those exact inputs
    # after execution as well; unchanged HEAD alone does not prove them clean.
    require(_helper.target_inventory(git, cutoff, current["registered_entries"], target, new_rounds) == inventory,
            "composer input inventory changed during derivation")
    for path in (OVERLAYS, LEASES):
        git.clean_file(source, path, exact=True)
    for path, observed in tools.items():
        git.clean_file(source, path)
        require(git.ident(source, path) == observed, "composer tool changed during derivation")
    for path in roots:
        git.clean_file(source, path)
    require(git.text("rev-parse", "HEAD") == observed_head, "HEAD moved during derivation")
    evidence = {"schema": "unofficial-ai-integrated-stacks-direct-composition-evidence/v1", "status": "PASS_COMPOSITION_DERIVATION",
                "claims": {"admitted_suffix_verified": True, "composed_source_verified": True,
                           "public_remote_readback_verified": False, "production_validation_run": False,
                           "build_started": False, "published": False},
                "tools": tools,
                "projection_evidence": projection, "preserved_profile_roots": preserved,
                "unchanged_extension_trees": extensions,
                "consumer_compatibility": "Separate typed direct composition dispatch; historical v3/v4 unchanged",
                "limitations": ["Current public-base remote identity is an external readback obligation",
                                "No production validation, build, visual QA, publication, or full historical proof is claimed",
                                "Only sequential issued/candidate(s)/released admissions with no metadata interlude are supported",
                                "No source preparation gap, preapplied edits, new supersessions, or semantic dispositions",
                                "Admission receipt shape must match the explicit current registrar contract"]}
    return receipt, evidence


def protected_tools(git, revision):
    result = {}
    for path in DIRECT_TOOLS:
        git.clean_file(revision, path)
        result[path] = git.ident(revision, path)
    return result


def recheck_direct_validation_tools(source, binding):
    if binding.get("schema") != SCHEMA:
        return
    git = Git(source)
    head = git.commit(git.text("rev-parse", "HEAD"))
    expected = binding.get("direct_validation_tools")
    require(isinstance(expected, dict) and set(expected) == set(DIRECT_TOOLS), "incomplete protected direct-tool inventory")
    require(protected_tools(git, head) == expected, "protected direct validation tools changed")


def load_direct_composition(source, requested_path=Path(RECEIPT)):
    """Derive, compare and bind the current committed direct receipt.

    Called only after a strict schema dispatch. No aliases to an import are
    manufactured. The return type matches build_fixed_point's loader contract.
    """
    git = Git(source)
    path = Path(requested_path)
    absolute = (git.root / path).resolve() if not path.is_absolute() else path.resolve()
    require(absolute.is_relative_to(git.root), "direct composition receipt escapes worktree")
    relative = absolute.relative_to(git.root).as_posix()
    require(relative == RECEIPT, "direct composition requires canonical receipt path")
    head = git.commit(git.text("rev-parse", "HEAD"))
    git.clean_file(head, relative)
    receipt = git.document(head, relative)
    require(receipt.get("schema") == SCHEMA and receipt.get("status") == "PASS", "invalid direct composition schema or pass state")
    tool_ids = protected_tools(git, head)
    expected, evidence = derive(source, receipt["previous_cutoff"]["public_main_head"],
                                receipt["registry"]["cutoff_commit"], receipt["composition"]["source_commit"])
    require(receipt == expected, "saved direct composition differs from freshly derived committed evidence")
    registry, composition, previous = receipt["registry"], receipt["composition"], receipt["previous_cutoff"]
    required = tuple(receipt["required_build_stems"])
    affected = tuple(sorted(path[:-4] for path in composition["affected_sources"]))
    receipt_id = git.ident(head, relative)
    binding = {
        "schema": SCHEMA, "receipt": relative, "receipt_sha256": receipt_id["sha256"], "receipt_git_blob": receipt_id["git_blob"],
        "authority_commit": receipt["authority"]["commit"], "authority_tree": receipt["authority"]["tree"],
        "previous_public_main_head": previous["public_main_head"], "previous_public_main_tree": previous["public_main_tree"],
        "previous_registry_commit": previous["registry_commit"], "previous_last_admitted_overlay": previous["last_admitted_overlay"],
        "previous_source_blobs": previous["source_blobs"], "previous_receipt": previous["receipt"],
        "composition_mode": composition["mode"], "composition_base_commit": composition["base_commit"],
        "composition_base_tree": composition["base_tree"], "composition_source_commit": composition["source_commit"],
        "composition_source_tree": composition["source_tree"], "registry_cutoff_commit": registry["cutoff_commit"],
        "registry_cutoff_tree": registry["cutoff_tree"], "registered_overlays": registry["registered_overlays"],
        "registered_stable_ids": registry["registered_stable_ids"], "last_admitted_overlay": registry["last_admitted_overlay"],
        "new_overlays": receipt["new_overlays"], "new_overlay_ids": [item["id"] for item in receipt["new_overlays"]],
        "new_overlay_candidate_commits": [item["candidate_commit"] for item in receipt["new_overlays"]],
        "new_overlay_intake_commits": [item["intake_commit"] for item in receipt["new_overlays"]],
        "new_overlay_admission_commits": [item["admission_commit"] for item in receipt["new_overlays"]],
        "required_build_stems": list(required), "affected_source_stems": list(affected),
        "affected_source_identities": composition["affected_sources"], "transport": receipt["transport"],
        "direct_validation_tools": tool_ids, "verifier_reports": {"overlay_projection": evidence["projection_evidence"]},
    }
    for name in ("overlays", "leases"):
        for key in ("path", "git_blob", "sha256"):
            binding[f"registry_{name}_{key}"] = registry[f"{name}_{key}"]
    require(git.text("rev-parse", "HEAD") == head, "HEAD moved while loading direct composition")
    git.clean_file(head, relative)
    recheck_direct_validation_tools(source, binding)
    return binding, required, affected
