#!/usr/bin/env python3
"""Exact, bounded Illusie AI correction after sealed R48; never an errata round."""
from __future__ import annotations
import argparse
from copy import deepcopy
import json
from pathlib import Path
import re
import sys

if __package__:
    from . import direct_successor_composition as direct
else:
    import direct_successor_composition as direct

Git, require, identity = direct.Git, direct.require, direct.identity
safe_path, parse_json = direct.safe_path, direct.parse_json
SCHEMA = "unofficial-ai-integrated-stacks-ai-source-correction-successor/v1"
MANIFEST_SCHEMA = "unofficial-ai-integrated-stacks-ai-source-correction-manifest/v1"
REVIEW_SCHEMA = "unofficial-ai-integrated-stacks-ai-source-correction-review/v1"
CANDIDATE = "4c3647f926f32a0edade647ebb52adce05d24a8e"
SEALED = "1c7fa79a3d8fdb24a9ec45ba65e65ce1fd8867c2"
CORRECTED = "ea606e202707d215f38e050be2621d0c83cadef0"
SEALED_RECEIPT = "validation/direct-successor-r48-composition.json"
SEALED_RECEIPT_SHA256 = "546206C486E7722D9086B9E4ADF979CCA11DC8587D3E28CCFEA551C700606ADE"
MANIFEST = "validation/direct-successor-r48-illusie-correction-manifest-2026-09-13.json"
NAMED_RECEIPT = "validation/direct-successor-r48-illusie-correction-composition-2026-09-13.json"
RECEIPT = direct.RECEIPT
CORRECTION_ID = "illusie-I-chain-comparison-localization-20260908"
CLAIMS = ["eilenberg-zilber-and-grading", "i1.4-localization"]
EXTRA_TOOLS = ("tools/ai_source_correction_composition.py", "tools/test_ai_source_correction_composition.py",
               "tools/test_ai_source_correction_consumers.py", "tools/tests/test_compare_ai_source_correction.py",
               "tools/package_direct_successor_pdfs.py", "tools/tests/test_package_ai_source_correction.py",
               "tools/test_ai_source_correction_checkpoint.py", "tools/cumulative_source.py", "tools/cumulative_reader.py",
               "tools/reconstruct_cumulative.py", "tools/cumulative-master.json", "tools/CUMULATIVE-RECONSTRUCTION.md",
               "tools/package_cumulative_successor.py", "tools/test_cumulative_packaging.py")
TOOLS = (*direct.DIRECT_TOOLS, *EXTRA_TOOLS)
REF_KEYS = {"path", "bytes", "sha256", "git_blob"}
ID_KEYS = REF_KEYS - {"path"}


def valid_identity(row, *, reference=False):
    keys = REF_KEYS if reference else ID_KEYS
    require(isinstance(row, dict) and set(row) == keys, "invalid exact file identity shape")
    require(type(row["bytes"]) is int and row["bytes"] >= 0, "invalid file byte count")
    require(isinstance(row["sha256"], str) and re.fullmatch(r"[0-9A-F]{64}", row["sha256"]), "invalid SHA-256")
    require(isinstance(row["git_blob"], str) and re.fullmatch(r"[0-9a-f]{40}", row["git_blob"]), "invalid Git blob")
    if reference:
        safe_path(row["path"])


def reference(git, revision, row):
    valid_identity(row, reference=True)
    require(git.ident(revision, row["path"]) == {k: row[k] for k in ID_KEYS},
            "correction reference identity mismatch: " + row["path"])
    return row["path"], {k: row[k] for k in ID_KEYS}


def validate_ai_source_correction_scope(scope, *, source_commit=None, source_tree=None):
    keys = {"correction_id", "candidate_commit", "candidate_tree", "manifest", "corrected_source_commit",
            "corrected_source_tree", "sealed_predecessor_commit", "sealed_predecessor_receipt_sha256"}
    require(isinstance(scope, dict) and set(scope) == keys, "invalid AI correction scope shape")
    require(scope["correction_id"] == CORRECTION_ID and scope["candidate_commit"] == CANDIDATE
            and scope["corrected_source_commit"] == CORRECTED and scope["sealed_predecessor_commit"] == SEALED
            and scope["sealed_predecessor_receipt_sha256"] == SEALED_RECEIPT_SHA256,
            "AI correction scope identity mismatch")
    for key in ("candidate_tree", "corrected_source_tree"):
        require(isinstance(scope[key], str) and re.fullmatch(r"[0-9a-f]{40}", scope[key]), "invalid correction tree")
    valid_identity(scope["manifest"], reference=True)
    require(scope["manifest"]["path"] == MANIFEST, "noncanonical correction manifest")
    if source_commit is not None:
        require(scope["corrected_source_commit"] == source_commit, "correction source commit mismatch")
    if source_tree is not None:
        require(scope["corrected_source_tree"] == source_tree, "correction source tree mismatch")


def changed_rows(git, before, after):
    changes = git.changes(before, after)
    direct.regular_changes(changes)
    result = []
    for path, row in sorted(changes.items()):
        require(path == "simplicial.tex" or path.startswith("illusie_volume_I/"),
                "correction changed an unrelated path: " + path)
        result.append({"path": path, "before": None if row[4] == "A" else git.ident(before, path),
                       "after": git.ident(after, path)})
    require("simplicial.tex" in changes, "correction omits Simplicial source")
    return result


def validate_manifest(git, manifest, head):
    """Recompute candidate and cumulative deltas; require their exact equality."""
    keys = {"schema", "status", "correction_id", "candidate", "source", "files", "dossier", "independent_review", "visual_loci"}
    require(isinstance(manifest, dict) and set(manifest) == keys
            and manifest["schema"] == MANIFEST_SCHEMA and manifest["status"] == "PASS"
            and manifest["correction_id"] == CORRECTION_ID, "invalid correction manifest contract")
    candidate, source = manifest["candidate"], manifest["source"]
    for obj in (candidate, source):
        require(isinstance(obj, dict) and set(obj) == {"commit", "tree", "parent"}, "invalid source transaction identity")
        for key in ("commit", "parent"):
            git.commit(obj[key])
        require(git.tree(obj["commit"]) == obj["tree"], "transaction tree mismatch")
        require(git.parents(obj["commit"]) == [obj["parent"]], "transaction parent mismatch")
    require(candidate["commit"] == CANDIDATE and source["commit"] == CORRECTED and source["parent"] == SEALED,
            "candidate or sealed source identity mismatch")
    expected = changed_rows(git, candidate["parent"], CANDIDATE)
    actual = changed_rows(git, SEALED, CORRECTED)
    require(isinstance(manifest["files"], list), "invalid changed-path inventory")
    for row in manifest["files"]:
        require(isinstance(row, dict) and set(row) == {"path", "before", "after"}, "invalid changed-path row")
        safe_path(row["path"])
        if row["before"] is not None:
            valid_identity(row["before"])
        valid_identity(row["after"])
    require(expected == actual, "candidate/cumulative preimage or postimage mismatch")
    require(manifest["files"] == actual, "manifest changed-path inventory differs from exact candidate replay")
    require(len(actual) == 21, "bounded correction must retain exactly 21 candidate paths")
    direct.validate_metadata_suffix(git, CORRECTED, head, additional_tools=direct.AI_PREPARATION_TOOLS,
                                    additional_receipts=direct.AI_ADDITIVE_METADATA)
    # Current registry and all original named R48 evidence remain byte-identical.
    for path in (direct.OVERLAYS, direct.LEASES, SEALED_RECEIPT):
        require(git.ident(SEALED, path) == git.ident(head, path), "sealed receipt or registry drift: " + path)
    require(git.ident(SEALED, SEALED_RECEIPT)["sha256"] == SEALED_RECEIPT_SHA256, "wrong sealed R48 receipt")
    require(git.blob(SEALED, SEALED_RECEIPT) == git.blob(SEALED, RECEIPT), "sealed R48 pointer mismatch")
    dossier = manifest["dossier"]
    require(isinstance(dossier, list) and dossier, "correction dossier is absent")
    protected = {}
    for row in dossier:
        path, ident = reference(git, head, row)
        require(path not in protected, "duplicate correction dossier path")
        require(path == "simplicial.tex" or path.startswith("illusie_volume_I/")
                or re.fullmatch(r"validation/direct-successor-[A-Za-z0-9._-]+\.json", path)
                or path in direct.AI_ADDITIVE_METADATA,
                "correction dossier path outside bounded evidence scope")
        require(path not in {MANIFEST, RECEIPT, NAMED_RECEIPT}, "self-referential correction evidence")
        protected[path] = ident
    extension_paths = set(git.text("ls-tree", "-r", "--name-only", CORRECTED, "--", "illusie_volume_I").splitlines())
    require(extension_paths and extension_paths | {"simplicial.tex"} <= set(protected), "incomplete Illusie dossier closure")
    for path in extension_paths | {"simplicial.tex"}:
        require(git.ident(CORRECTED, path) == protected[path], "dossier differs from corrected source: " + path)
    review_path, review_id = reference(git, head, manifest["independent_review"])
    require(protected.get(review_path) == review_id, "review is not dossier-bound")
    review = git.document(head, review_path)
    require(review.get("schema") == REVIEW_SCHEMA and review.get("status") == "PASS"
            and review.get("candidate_commit") == CANDIDATE and review.get("candidate_tree") == candidate["tree"]
            and review.get("source_commit") == CORRECTED and review.get("source_tree") == source["tree"]
            and review.get("reviewed_claims") == CLAIMS and review.get("unresolved_defects") == [],
            "independent review does not certify exact corrected candidate/source and both claims")
    loci = manifest["visual_loci"]
    require(isinstance(loci, list) and len(loci) == len(CLAIMS)
            and [r.get("unit_id") for r in loci] == CLAIMS, "correction visual units incomplete")
    source_bytes = git.blob(CORRECTED, "simplicial.tex")
    for row in loci:
        require(set(row) == {"unit_id", "source", "start_byte", "end_byte_exclusive", "sha256"}
                and row["source"] == "simplicial.tex" and type(row["start_byte"]) is int
                and type(row["end_byte_exclusive"]) is int
                and 0 <= row["start_byte"] < row["end_byte_exclusive"] <= len(source_bytes),
                "invalid correction visual source interval")
        require(identity(source_bytes[row["start_byte"]:row["end_byte_exclusive"]])["sha256"] == row["sha256"],
                "correction visual source interval hash mismatch")
    require(review.get("visual_loci") == loci, "correction visual loci not independently review-bound")
    evidence = review.get("evidence")
    require(isinstance(evidence, list) and evidence, "independent review lacks actual evidence references")
    for row in evidence:
        path, ident = reference(git, head, row)
        require(path != review_path and protected.get(path) == ident, "independent review evidence not closed")
    return protected


def derive_ai_source_correction(source, manifest_path=MANIFEST):
    git = Git(source)
    head = git.commit(git.text("rev-parse", "HEAD"))
    require(safe_path(manifest_path) == MANIFEST, "noncanonical correction manifest")
    git.clean_file(head, manifest_path, exact=True)
    manifest = git.document(head, manifest_path)
    protected = validate_manifest(git, manifest, head)
    prior, historical = direct.load_direct_composition_at(source, SEALED, SEALED_RECEIPT)
    require(prior["registry"]["last_admitted_overlay"] == "stacks-errata-a04446e-r48"
            and len(prior["required_build_stems"]) == 36, "wrong R48 predecessor/profile")
    manifest_ref = {"path": MANIFEST, **git.ident(head, MANIFEST)}
    scope = {"correction_id": CORRECTION_ID, "candidate_commit": CANDIDATE,
             "candidate_tree": manifest["candidate"]["tree"], "manifest": manifest_ref,
             "corrected_source_commit": CORRECTED, "corrected_source_tree": git.tree(CORRECTED),
             "sealed_predecessor_commit": SEALED, "sealed_predecessor_receipt_sha256": SEALED_RECEIPT_SHA256}
    validate_ai_source_correction_scope(scope)
    for path in (MANIFEST, SEALED_RECEIPT):
        protected[path] = git.ident(head, path)
    affected = deepcopy(prior["composition"]["affected_sources"])
    affected["simplicial.tex"] = {"before": git.ident(SEALED, "simplicial.tex"),
                                 "after": git.ident(CORRECTED, "simplicial.tex"),
                                 "committed_matches_composition": True,
                                 "composition_mode": "Exact independently reviewed AI correction; not official errata"}
    receipt = deepcopy(prior)
    receipt.update(schema=SCHEMA,
                   sealed_predecessor={"commit": SEALED, "tree": git.tree(SEALED),
                                       "receipt": {"path": SEALED_RECEIPT, **git.ident(SEALED, SEALED_RECEIPT)}},
                   ai_source_correction_scope=scope, correction_protected_inputs=dict(sorted(protected.items())))
    receipt["created_utc"] = direct.datetime.fromtimestamp(int(git.text("show", "-s", "--format=%ct", CORRECTED)),
                                                         direct.timezone.utc).isoformat().replace("+00:00", "Z")
    receipt["correction_visual_units"] = manifest["visual_loci"]
    receipt["composition"].update(base_commit=SEALED, base_tree=git.tree(SEALED),
                                  source_commit=CORRECTED, source_tree=git.tree(CORRECTED),
                                  mode="Sealed R48 registry composition followed by exact reviewed AI-source correction",
                                  affected_sources=affected)
    receipt["preservation"]["simplicial.tex"] = git.ident(CORRECTED, "simplicial.tex")
    receipt["projection_verifier"] = {"path": "tools/ai_source_correction_composition.py", "status": "PASS",
                                     "command": "python tools/ai_source_correction_composition.py --check",
                                     "inherited_registry_projection": prior["projection_verifier"]}
    # No new official errata operations/IDs were created; inherited counts are retained.
    receipt["ai_source_correction"] = {"classification": "AI-draft correction and independently reviewed extension",
                                       "official_errata_operations_added": 0, "changed_paths": manifest["files"],
                                       "reviewed_claims": CLAIMS}
    for path in protected:
        git.clean_file(head, path, exact=True)
    # Historical validation deliberately does not read historical root bytes
    # from the live tree. Freeze every current profile/preserved root here.
    live_roots = {stem + ".tex" for stem in prior["required_build_stems"]}
    live_roots.update(path for path in prior.get("preservation", {}) if direct._helper.ROOT_TEX.fullmatch(path))
    for path in sorted(live_roots):
        require(git.ident(CORRECTED, path) == git.ident(head, path), "post-correction root drift: " + path)
        git.clean_file(head, path)
    require(git.text("rev-parse", "HEAD") == head, "HEAD moved during correction derivation")
    return receipt, historical


def protected_tools(git, head):
    result = {}
    for path in TOOLS:
        git.clean_file(head, path)
        result[path] = git.ident(head, path)
    return result


def recheck_ai_source_correction_tools(source, binding):
    require(binding.get("schema") == SCHEMA, "wrong AI correction binding schema")
    git = Git(source)
    head = git.commit(git.text("rev-parse", "HEAD"))
    require(binding.get("direct_validation_tools") == protected_tools(git, head), "correction tools changed")
    protected = binding.get("correction_protected_inputs")
    require(isinstance(protected, dict) and {MANIFEST, SEALED_RECEIPT, "simplicial.tex"} <= set(protected),
            "correction protected input inventory missing")
    for path, expected in protected.items():
        valid_identity(expected)
        require(git.ident(head, path) == expected, "correction protected input drift: " + path)
        git.clean_file(head, path, exact=True)
    validate_ai_source_correction_scope(binding.get("ai_source_correction_scope"),
        source_commit=binding.get("composition_source_commit"), source_tree=binding.get("composition_source_tree"))
    require(protected[MANIFEST] == {k: binding["ai_source_correction_scope"]["manifest"][k] for k in ID_KEYS},
            "correction scope/manifest identity mismatch")
    require(git.text("rev-parse", "HEAD") == head, "HEAD moved during correction input recheck")


def load_ai_source_correction(source, requested_path=Path(RECEIPT)):
    git = Git(source)
    absolute = (git.root / requested_path).resolve() if not Path(requested_path).is_absolute() else Path(requested_path).resolve()
    require(absolute.is_relative_to(git.root) and absolute.relative_to(git.root).as_posix() == RECEIPT,
            "AI correction requires canonical composition pointer")
    head = git.commit(git.text("rev-parse", "HEAD"))
    git.clean_file(head, RECEIPT, exact=True)
    saved = git.document(head, RECEIPT)
    expected, historical = derive_ai_source_correction(source)
    require(saved == expected, "saved AI correction receipt differs from exact derivation")
    require(git.blob(head, NAMED_RECEIPT) == git.blob(head, RECEIPT), "named correction receipt/pointer mismatch")
    registry, comp, previous = saved["registry"], saved["composition"], saved["previous_cutoff"]
    required = tuple(saved["required_build_stems"])
    affected = tuple(sorted(path[:-4] for path in comp["affected_sources"]))
    require(set(affected) == {"groupoids", "spaces-perfect", "simplicial"}, "wrong combined visual affected scope")
    binding = {
        "schema": SCHEMA, "receipt": RECEIPT, "receipt_sha256": git.ident(head, RECEIPT)["sha256"],
        "receipt_git_blob": git.ident(head, RECEIPT)["git_blob"],
        "authority_commit": saved["authority"]["commit"], "authority_tree": saved["authority"]["tree"],
        "previous_public_main_head": previous["public_main_head"], "previous_public_main_tree": previous["public_main_tree"],
        "previous_registry_commit": previous["registry_commit"], "previous_last_admitted_overlay": previous["last_admitted_overlay"],
        "previous_source_blobs": previous["source_blobs"], "previous_receipt": previous["receipt"],
        "composition_mode": comp["mode"], "composition_base_commit": comp["base_commit"], "composition_base_tree": comp["base_tree"],
        "composition_source_commit": comp["source_commit"], "composition_source_tree": comp["source_tree"],
        "registry_cutoff_commit": registry["cutoff_commit"], "registry_cutoff_tree": registry["cutoff_tree"],
        "registered_overlays": registry["registered_overlays"], "registered_stable_ids": registry["registered_stable_ids"],
        "last_admitted_overlay": registry["last_admitted_overlay"], "new_overlays": saved["new_overlays"],
        "new_overlay_ids": [x["id"] for x in saved["new_overlays"]],
        "new_overlay_candidate_commits": [x["candidate_commit"] for x in saved["new_overlays"]],
        "new_overlay_intake_commits": [x["intake_commit"] for x in saved["new_overlays"]],
        "new_overlay_admission_commits": [x["admission_commit"] for x in saved["new_overlays"]],
        "required_build_stems": list(required), "affected_source_stems": list(affected),
        "affected_source_identities": comp["affected_sources"], "transport": saved["transport"],
        "direct_validation_tools": protected_tools(git, head),
        "verifier_reports": {"overlay_projection": historical["projection_evidence"]},
        "ai_source_correction_scope": saved["ai_source_correction_scope"],
        "correction_protected_inputs": {**saved["correction_protected_inputs"], NAMED_RECEIPT: git.ident(head, NAMED_RECEIPT)},
        "correction_visual_units": saved["correction_visual_units"],
    }
    for name in ("overlays", "leases"):
        for key in ("path", "git_blob", "sha256"):
            binding[f"registry_{name}_{key}"] = registry[f"{name}_{key}"]
    validate_ai_source_correction_scope(binding["ai_source_correction_scope"], source_commit=comp["source_commit"], source_tree=comp["source_tree"])
    recheck_ai_source_correction_tools(source, binding)
    require(git.text("rev-parse", "HEAD") == head, "HEAD moved while loading correction")
    return binding, required, affected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("."))
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.check:
        require(args.output is None, "check cannot write")
        binding, stems, affected = load_ai_source_correction(args.source)
        print(json.dumps({"status": "PASS", "source": binding["composition_source_commit"], "stems": stems, "affected": affected}))
        return 0
    require(args.output is not None, "--output or --check is required")
    result, _ = derive_ai_source_correction(args.source)
    output = args.output if args.output.is_absolute() else args.source / args.output
    require(output.resolve().is_relative_to(args.source.resolve()), "receipt output escapes source")
    require(output.resolve().relative_to(args.source.resolve()).as_posix() == NAMED_RECEIPT, "noncanonical named receipt output")
    with output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(result, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    print("Created immutable correction receipt; commit it and update the current pointer explicitly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
