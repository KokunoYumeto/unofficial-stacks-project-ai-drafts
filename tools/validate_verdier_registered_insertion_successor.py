#!/usr/bin/env python3
"""Validate build, visual, reproducibility, and publication evidence for Verdier II.2.3.1.

Both modes are read-only and never launch TeX.  Pre-publication mode requires
the committed composition, two complete deterministic build receipts, visual
QA, and a reproducibility receipt.  Final mode additionally verifies the
publication receipt and downloads its anonymous public-readback inventory.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import quote

sys.dont_write_bytecode = True

if __package__:
    from . import validate_direct_successor_release as common
    from . import verdier_registered_insertion_successor as verdier
else:
    import validate_direct_successor_release as common
    import verdier_registered_insertion_successor as verdier


require = common.require
exact = common.exact
number = common.number
digest = common.digest
safe_path = common.safe_path
parse_json = common.parse_json
identity = common.identity
Objects = common.Objects

INDEX = "validation/direct-successor-current.json"
INDEX_SCHEMA = "unofficial-ai-integrated-stacks-direct-release-index/v1"
RELEASE_SCHEMA = "unofficial-ai-integrated-stacks-verdier-registered-insertion-release/v1"
REPOSITORY = "KokunoYumeto/unofficial-stacks-project-ai-drafts"
COMPOSITION = verdier.RECEIPT
CORE_ROLES = ("composition", "build", "second_build", "visual_qa", "reproducibility")
REFERENCE_KEYS = {"path", "bytes", "sha256", "git_blob"}
AI_CHECKPOINT_SCHEMA = (
    "unofficial-stacks-project-ai-drafts-ega-source-checkpoint-ai-source-correction-successor/v1"
)
AI_CHECKPOINT_STATUS = "PASS_SOURCE_CHECKPOINT_AI_SOURCE_CORRECTION_SUCCESSOR"
RECEIPT_NAME = re.compile(
    r"(?:direct-successor|verdier-registered-insertion-successor)-[A-Za-z0-9._-]+\.json\Z"
)


def _reference(objects: Objects, row: object, role: str) -> tuple[dict, bytes]:
    require(isinstance(row, dict) and set(row) == REFERENCE_KEYS, "invalid reference: " + role)
    path = safe_path(row["path"])
    if role == "composition":
        require(path == COMPOSITION, "noncanonical composition reference")
    else:
        require(PurePosixPath(path).parent == PurePosixPath("validation")
                and RECEIPT_NAME.fullmatch(PurePosixPath(path).name) is not None
                and path not in {INDEX, COMPOSITION}, "receipt outside the narrow validation namespace")
    raw = objects.clean(path)
    require(identity(raw) == {key: row[key] for key in ("bytes", "sha256", "git_blob")},
            "committed reference identity mismatch: " + role)
    return parse_json(raw), raw


def _index_scope(binding: dict) -> dict[str, object]:
    return {
        "source_commit": binding["composition_source_commit"],
        "registry_cutoff_commit": binding["registry_cutoff_commit"],
        "new_overlay_ids": binding["new_overlay_ids"],
        "ai_source_correction": binding["ai_source_correction_scope"],
        "verdier_registered_insertion": binding["verdier_registered_insertion_scope"],
    }


def _load_index(
    objects: Objects,
    requested: str,
    pre_publication: bool,
) -> tuple[dict, bytes, dict[str, tuple[dict, bytes]]]:
    index, raw = objects.document(INDEX)
    require(index.get("schema") == INDEX_SCHEMA, "unsupported Verdier release index")
    allowed = {"READY_FOR_PUBLICATION", "PUBLICATION_COMPLETE"} if pre_publication else {"PUBLICATION_COMPLETE"}
    require(index.get("status") in allowed, "Verdier release index is not ready")
    refs = index.get("references")
    roles = set(CORE_ROLES) | ({"release"} if index["status"] == "PUBLICATION_COMPLETE" else set())
    require(isinstance(refs, dict) and set(refs) == roles, "incomplete Verdier index references")
    require(len({row.get("path") for row in refs.values() if isinstance(row, dict)}) == len(refs),
            "aliased Verdier receipt roles")
    documents = {role: _reference(objects, refs[role], role) for role in roles}
    require(requested == refs["build"]["path"], "build argument differs from current Verdier index")
    return index, raw, documents


def _checkpoint_scope(checkpoint: object, binding: dict) -> None:
    require(isinstance(checkpoint, dict)
            and checkpoint.get("schema") == AI_CHECKPOINT_SCHEMA
            and checkpoint.get("status") == AI_CHECKPOINT_STATUS,
            "Verdier build lacks the canonical current EGA/Illusie checkpoint")
    require(checkpoint.get("ai_source_correction") == binding["ai_source_correction_scope"],
            "checkpoint inherited AI-correction scope mismatch")
    ega = checkpoint.get("current_ega_successor")
    illusie = checkpoint.get("current_illusie_successor")
    require(isinstance(ega, dict) and str(ega.get("status", "")).startswith("PASS_CURRENT_PUBLIC_EGA")
            and isinstance(illusie, dict) and illusie.get("status") == "PASS_CURRENT_ILLUSIE_CORRECTION_BOUND",
            "current EGA or Illusie revalidation is absent")


def _check_build_shape(receipt: dict, binding: dict, stems: tuple[str, ...], mutex_validator) -> list[dict]:
    require(receipt.get("schema") == "unofficial-ai-integrated-stacks-fixed-point-build/v1"
            and receipt.get("status") == "PASS", "build is not a passing fixed-point run")
    require(receipt.get("composition") == binding, "build Verdier-composition binding mismatch")
    _checkpoint_scope(receipt.get("source_checkpoint"), binding)
    require(receipt.get("pdfs_committed") is False, "build PDFs must remain release assets")
    build = receipt.get("build")
    require(isinstance(build, dict), "missing build state")
    expected = {
        "strategy": "sequential-prime-bibtex-global-state-sweeps",
        "fixed_point_suffixes": list(common.SUFFIXES),
        "stem_selection": "composition_receipt",
        "stems": list(stems),
        "chapter_count": 36,
        "pdfinfo_readable": 36,
        "worktree_kind": "linked",
        "primary_worktree_override": False,
    }
    require(all(build.get(key) == value for key, value in expected.items()),
            "Verdier build is not the mandatory 36-chapter isolated profile")
    require(2 <= number(build.get("global_fixed_point_sweep"), 2) <= 6,
            "invalid fixed-point confirming sweep")
    errors: list[str] = []
    mutex_validator(build.get("machine_wide_tex_mutex"), "Verdier full build", errors)
    require(not errors, "; ".join(errors))
    diagnostics = build.get("diagnostics")
    require(isinstance(diagnostics, dict) and set(diagnostics) == set(common.DIAGNOSTICS),
            "incomplete build diagnostics")
    for key, value in diagnostics.items():
        number(value)
        require(key == "external_reference_markers" or value == 0,
                "nonzero build diagnostic: " + key)
    artifacts = receipt.get("artifacts")
    require(isinstance(artifacts, list) and [row.get("stem") for row in artifacts] == list(stems),
            "build artifact inventory does not cover the exact 36-stem profile")
    totals = {key: 0 for key in common.DIAGNOSTICS}
    for artifact in artifacts:
        require(isinstance(artifact, dict), "invalid build artifact")
        number(artifact.get("pages"), 1)
        number(artifact.get("bytes"), 1)
        digest(artifact.get("sha256"))
        counts = artifact.get("diagnostics")
        require(isinstance(counts, dict) and set(counts) == set(common.DIAGNOSTICS),
                "artifact diagnostics are incomplete")
        for key, value in counts.items():
            totals[key] += number(value)
        external = artifact.get("external_references")
        require(isinstance(external, dict)
                and external.get("count") == counts["external_reference_markers"],
                "artifact external-reference count mismatch")
        digest(external.get("sha256"))
    require(totals == diagnostics, "aggregate build diagnostics mismatch")
    require(build.get("artifact_tuple_set_sha256") == common.tuple_hash(artifacts),
            "artifact tuple hash mismatch")
    return artifacts


def _validate_build(
    objects: Objects,
    receipt: dict,
    binding: dict,
    stems: tuple[str, ...],
    mutex_validator,
    checkpoint_validator,
    checkpoint_replay,
    capture_validator,
) -> list[dict]:
    artifacts = _check_build_shape(receipt, binding, stems, mutex_validator)
    source = receipt.get("source")
    require(isinstance(source, dict) and set(source) == {"commit", "tree"}, "invalid build source")
    commit = objects.commit(source["commit"])
    objects.tree(commit, source["tree"])
    objects.linear(binding["composition_source_commit"], commit)
    objects.linear(commit, objects.text("rev-parse", "HEAD"))
    common.validate_process_tree(objects, receipt, commit, capture_validator)
    require(objects.build_inputs(commit, stems) == objects.build_inputs("HEAD", stems),
            "build-critical input inventory changed")
    protected: dict[str, dict] = {
        COMPOSITION: {"sha256": binding["receipt_sha256"], "git_blob": binding["receipt_git_blob"]},
        binding["registry_overlays_path"]: {
            "sha256": binding["registry_overlays_sha256"],
            "git_blob": binding["registry_overlays_git_blob"],
        },
        binding["registry_leases_path"]: {
            "sha256": binding["registry_leases_sha256"],
            "git_blob": binding["registry_leases_git_blob"],
        },
    }
    for path in objects.build_inputs(commit, stems):
        protected[path] = objects.ident("HEAD", path)
    tools = binding.get("direct_validation_tools")
    require(isinstance(tools, dict) and set(tools) == set(verdier.TOOLS),
            "Verdier validation-tool inventory is incomplete")
    protected.update(tools)
    protected.update(binding["correction_protected_inputs"])
    for path, expected in protected.items():
        observed = objects.ident(commit, path)
        require(all(observed.get(key) == value for key, value in expected.items() if key != "path"),
                "build-source protected input mismatch: " + path)
    builder = receipt.get("builder")
    require(isinstance(builder, dict) and builder.get("path") == "tools/build_fixed_point.py",
            "invalid fixed-point builder binding")
    observed_builder = objects.ident(commit, builder["path"])
    require(builder.get("git_blob") == observed_builder["git_blob"]
            and builder.get("sha256") == observed_builder["sha256"], "builder identity mismatch")
    checkpoint_validator(receipt, "Verdier build")
    checkpoint = receipt["source_checkpoint"]
    checkpoint_ref = checkpoint.get("receipt")
    require(isinstance(checkpoint_ref, dict), "checkpoint canonical receipt identity missing")
    checkpoint_path = safe_path(checkpoint_ref.get("path"))
    require(checkpoint_path == "validation/ega-i-6.6.4-source-checkpoint-2026-08-31.json",
            "noncanonical EGA source checkpoint")
    checkpoint_identity = objects.ident(commit, checkpoint_path)
    require(all(checkpoint_ref.get(key) == value for key, value in checkpoint_identity.items()),
            "checkpoint receipt byte binding mismatch")
    replayed = checkpoint_replay(objects.root, Path(checkpoint_path), binding, commit)
    require(replayed == checkpoint, "exact-build-head source checkpoint replay mismatch")
    return artifacts


def _validate_visual(visual: dict, build_ref: dict, build: dict, artifacts: list[dict], binding: dict) -> None:
    require(visual.get("schema") == "unofficial-ai-integrated-stacks-visual-qa/v1"
            and visual.get("status") == "PASS", "visual QA is not PASS")
    require(visual.get("source") == build["source"], "visual/build source mismatch")
    expected_build = {key: build_ref[key] for key in ("path", "bytes", "sha256")}
    expected_build.update(status="PASS", global_fixed_point_sweep=build["build"]["global_fixed_point_sweep"])
    require(visual.get("build_receipt") == expected_build, "visual build reference mismatch")
    by_stem = {row["stem"]: row for row in artifacts}
    scope = visual.get("scope", {})
    require(scope.get("affected_chapters") == ["derived"], "visual QA must cover exactly derived")
    require(scope.get("verdier_registered_insertion") == binding["verdier_registered_insertion_scope"],
            "visual QA lacks the exact Verdier insertion scope")
    pages = by_stem["derived"]["pages"]
    require(scope.get("full_page_render_count") == pages
            and scope.get("full_page_contact_sheet_review_count") == pages,
            "visual QA does not inspect every affected PDF page")
    loci = scope.get("high_resolution_locus_pages")
    require(isinstance(loci, dict) and set(loci) == {"derived"}
            and isinstance(loci["derived"], list) and loci["derived"]
            and loci["derived"] == sorted(set(loci["derived"]))
            and all(type(page) is int and 1 <= page <= pages for page in loci["derived"]),
            "visual high-resolution insertion locus is incomplete")
    require(scope.get("high_resolution_locus_page_count") == len(loci["derived"]),
            "visual locus-page count mismatch")
    output = visual.get("artifacts")
    require(isinstance(output, dict) and set(output) == {"derived"}, "visual artifact scope mismatch")
    artifact = output["derived"]
    require(all(artifact.get(key) == by_stem["derived"][key] for key in ("pages", "bytes", "sha256"))
            and artifact.get("pdf") == "derived.pdf" and artifact.get("encrypted") is False
            and artifact.get("pages_without_ink") == 0 and artifact.get("duplicate_render_hashes") == 0,
            "visual derived-PDF identity or render state mismatch")
    checks = visual.get("checks", {})
    require(all(checks.get(key) is True for key in common.VISUAL_TRUE),
            "visual inspection check missing")
    require(all(number(checks.get(key)) == 0 for key in common.VISUAL_ZERO),
            "visual defect count is nonzero")
    protocol = visual.get("render_protocol", {})
    require("Poppler" in str(protocol.get("renderer", ""))
            and number(protocol.get("full_page_dpi"), 72) >= 72
            and number(protocol.get("high_resolution_dpi"), 144) >= 144
            and protocol.get("render_intermediates_published") is False,
            "visual render protocol mismatch")


def _validate_repro(
    receipt: dict,
    first_ref: dict,
    second_ref: dict,
    first: dict,
    second: dict,
    artifacts: list[dict],
    binding: dict,
    comparator,
) -> None:
    comparator(first, second)
    require(receipt.get("schema") == "unofficial-ai-integrated-stacks-clean-build-reproducibility/v1"
            and receipt.get("status") == "PASS", "reproducibility receipt is not PASS")
    require(all(receipt.get(key) == first[key] for key in ("source", "builder", "environment")),
            "reproducibility source/builder/environment mismatch")
    artifact_ids = [{key: row[key] for key in ("stem", "pages", "bytes", "sha256")} for row in artifacts]
    require(receipt.get("artifacts") == artifact_ids, "reproducibility artifact inventory mismatch")
    expected_scope = {
        "new_overlay_ids": [verdier.OVERLAY_ID],
        "registry_cutoff_commit": binding["registry_cutoff_commit"],
        "source_commit": first["source"]["commit"],
        "source_tree": first["source"]["tree"],
        "composition_receipt": COMPOSITION,
        "composition_receipt_sha256": binding["receipt_sha256"],
        "ai_source_correction": binding["ai_source_correction_scope"],
        "verdier_registered_insertion": binding["verdier_registered_insertion_scope"],
    }
    require(receipt.get("scope") == expected_scope, "reproducibility scope mismatch")
    expected_method = {
        "execution_model": "independent_linked_worktrees",
        "first_worktree_kind": "linked",
        "second_worktree_kind": "linked",
        "builder_path": first["builder"]["path"],
        "builder_git_blob": first["builder"]["git_blob"],
        "builder_sha256": first["builder"]["sha256"],
    }
    require(receipt.get("method") == expected_method, "reproducibility method mismatch")
    runs = receipt.get("runs")
    require(isinstance(runs, dict) and set(runs) == {"first", "second"},
            "reproducibility run inventory mismatch")
    for role, ref, build in (("first", first_ref, first), ("second", second_ref, second)):
        expected = {
            "receipt": ref["path"], "bytes": ref["bytes"], "sha256": ref["sha256"],
            "status": "PASS", "created_utc": build["created_utc"],
            "global_fixed_point_sweep": build["build"]["global_fixed_point_sweep"],
        }
        require(runs[role] == expected, "reproducibility run binding mismatch")
    comparison = {
        "chapter_count": 36,
        "matched_artifact_count": 36,
        "different_artifact_count": 0,
        "different_artifacts": [],
        "total_pages_each_run": sum(row["pages"] for row in artifacts),
        "total_pdf_bytes_each_run": sum(row["bytes"] for row in artifacts),
        "artifact_tuple_set_sha256_each_run": common.tuple_hash(artifacts),
        "all_artifact_identities_exactly_equal": True,
        "source_identity_equal": True,
        "builder_identity_equal": True,
        "environment_identity_equal": True,
        "fixed_point_sweep_equal": True,
        "source_checkpoint_identity_equal": True,
    }
    require(receipt.get("comparison") == comparison, "reproducibility comparison mismatch")


def _release_required_paths(objects: Objects, content: str, binding: dict, refs: dict) -> set[str]:
    overlay = binding["new_overlays"][0]
    required = {row["path"] for role, row in refs.items() if role != "release"}
    required.update(verdier.TOOLS)
    required.update(binding["correction_protected_inputs"])
    required.update((binding["registry_overlays_path"], binding["registry_leases_path"],
                     "validation/ega-i-6.6.4-source-checkpoint-2026-08-31.json", verdier.TARGET))
    for key in ("manifest", "review", "payload", "operation", "source_map", "stable_units",
                "admission_receipt"):
        required.add(safe_path(overlay[key]["path"]))
    required.update(objects.build_inputs(content, tuple(binding["required_build_stems"])))
    return required


def _validate_release(objects: Objects, release: dict, index: dict, binding: dict) -> None:
    require(release.get("schema") == RELEASE_SCHEMA and release.get("status") == "PUBLICATION_COMPLETE",
            "Verdier release is not publication-complete")
    require(release.get("repository") == REPOSITORY and release.get("default_branch") == "main",
            "Verdier public destination mismatch")
    refs = {role: index["references"][role] for role in CORE_ROLES}
    require(release.get("receipts") == refs, "release receipt-reference mismatch")
    expected_scope = {
        **_index_scope(binding),
        "registered_overlays": binding["registered_overlays"],
        "registered_stable_ids": binding["registered_stable_ids"],
    }
    require(release.get("scope") == expected_scope, "release scope mismatch")
    content, validation = release.get("content", {}), release.get("validation_head", {})
    content_commit = objects.commit(content.get("commit"))
    validation_commit = objects.commit(validation.get("commit"))
    objects.tree(content_commit, content.get("tree"))
    objects.tree(validation_commit, validation.get("tree"))
    objects.linear(binding["composition_source_commit"], content_commit)
    objects.linear(content_commit, validation_commit)
    head = objects.text("rev-parse", "HEAD")
    objects.linear(validation_commit, head)
    required = _release_required_paths(objects, content_commit, binding, index["references"])
    readback = release.get("public_readback")
    require(isinstance(readback, dict) and readback.get("status") == "PASS"
            and readback.get("anonymous") is True and readback.get("commit") == content_commit,
            "anonymous public readback did not pass")
    rows = readback.get("checked_paths")
    require(isinstance(rows, list) and all(isinstance(row, dict) and set(row) == REFERENCE_KEYS for row in rows),
            "invalid public-readback inventory")
    paths = [safe_path(row["path"]) for row in rows]
    require(len(paths) == len(set(paths)) and required <= set(paths),
            "public readback omits required paths or contains duplicates")
    for row in rows:
        path = row["path"]
        require(objects.ident(content_commit, path) == {key: row[key] for key in REFERENCE_KEYS - {"path"}},
                "public-readback local identity mismatch: " + path)
        common.public_object(
            f"https://raw.githubusercontent.com/{REPOSITORY}/{content_commit}/{quote(path, safe='/')}", row
        )
    require(readback.get("checked_file_count") == len(rows)
            and readback.get("checked_total_bytes") == sum(row["bytes"] for row in rows),
            "public-readback totals mismatch")
    workflow = release.get("workflow")
    require(isinstance(workflow, dict) and workflow.get("name") == "Unified repository validation"
            and workflow.get("status") == "completed" and workflow.get("conclusion") == "success"
            and workflow.get("head_sha") == validation_commit
            and type(workflow.get("run_id")) is int and workflow["run_id"] > 0,
            "release workflow binding mismatch")
    remote_run = common.public_json(
        f"https://api.github.com/repos/{REPOSITORY}/actions/runs/{workflow['run_id']}"
    )
    require(remote_run.get("id") == workflow["run_id"]
            and remote_run.get("head_sha") == validation_commit
            and remote_run.get("name") == workflow["name"]
            and remote_run.get("status") == "completed" and remote_run.get("conclusion") == "success",
            "public workflow readback mismatch")
    remote_repo = common.public_json(f"https://api.github.com/repos/{REPOSITORY}")
    require(remote_repo.get("private") is False and remote_repo.get("default_branch") == "main",
            "repository is not publicly readable")
    remote_main = common.public_json(f"https://api.github.com/repos/{REPOSITORY}/git/ref/heads/main")
    require(remote_main.get("object", {}).get("sha") == head,
            "validated final HEAD is not public main")
    for path in (INDEX, index["references"]["release"]["path"]):
        common.public_object(
            f"https://raw.githubusercontent.com/{REPOSITORY}/{head}/{quote(path, safe='/')}",
            {"path": path, **objects.ident(head, path)},
        )


def validate_verdier_successor(root: Path, build_path: Path, pre_publication: bool = False) -> int:
    """CLI-compatible, read-only validator used by unified dispatch."""
    try:
        if __package__:
            from . import compare_fixed_point_builds as compare
            from . import direct_successor_checkpoint as checkpoint
            from . import validate_unified_repository as unified
            from .tex_process_public_receipt import validate_public_capture_receipt
        else:
            import compare_fixed_point_builds as compare
            import direct_successor_checkpoint as checkpoint
            import validate_unified_repository as unified
            from tex_process_public_receipt import validate_public_capture_receipt

        root = Path(root).resolve()
        objects = Objects(root)
        requested = Path(build_path)
        requested = requested.resolve().relative_to(root).as_posix() if requested.is_absolute() else requested.as_posix()
        initial = objects.text("rev-parse", "HEAD")
        index, index_raw, documents = _load_index(objects, safe_path(requested), pre_publication)
        require(documents["composition"][0].get("schema") == verdier.SCHEMA,
                "index does not reference the Verdier successor composition")
        binding, stems, affected = verdier.load_verdier_registered_insertion_successor(root, Path(COMPOSITION))
        require(stems == verdier.EXPECTED_STEMS and affected == ("derived",),
                "Verdier loader returned the wrong mandatory build scope")
        require(index.get("composition_scope") == _index_scope(binding),
                "Verdier index composition scope mismatch")
        first, second = documents["build"][0], documents["second_build"][0]
        artifacts = _validate_build(objects, first, binding, stems,
                                    unified.validate_machine_wide_tex_mutex,
                                    compare.validate_source_checkpoint,
                                    checkpoint.validate_direct_source_checkpoint_at,
                                    validate_public_capture_receipt)
        second_artifacts = _validate_build(objects, second, binding, stems,
                                           unified.validate_machine_wide_tex_mutex,
                                           compare.validate_source_checkpoint,
                                           checkpoint.validate_direct_source_checkpoint_at,
                                           validate_public_capture_receipt)
        require([{key: row[key] for key in ("stem", "pages", "bytes", "sha256")} for row in artifacts]
                == [{key: row[key] for key in ("stem", "pages", "bytes", "sha256")} for row in second_artifacts],
                "two deterministic builds produced different PDF identities")
        _validate_visual(documents["visual_qa"][0], index["references"]["build"], first,
                         artifacts, binding)
        _validate_repro(documents["reproducibility"][0], index["references"]["build"],
                        index["references"]["second_build"], first, second, artifacts,
                        binding, compare.compare_receipts)
        if not pre_publication:
            _validate_release(objects, documents["release"][0], index, binding)
        require(objects.text("rev-parse", "HEAD") == initial and objects.clean(INDEX) == index_raw,
                "validation inputs moved during validation")
        for role, ref in index["references"].items():
            _reference(objects, ref, role)
        verdier.recheck_verdier_successor_tools(root, binding)
    except (OSError, ValueError, KeyError, TypeError, AttributeError, ImportError,
            RuntimeError, json.JSONDecodeError, subprocess.SubprocessError) as exc:
        print("Verdier registered-insertion successor validation: FAIL\n- " + str(exc), file=sys.stderr)
        return 1
    print("Verdier registered-insertion successor validation: "
          + ("PASS_PRE_PUBLICATION" if pre_publication else "PUBLICATION_COMPLETE"))
    print(f"- registered insertion operations: 1; stable IDs: {len(verdier.STABLE_IDS)}")
    print("- full-profile chapters: 36; exact deterministic builds: 2")
    print(f"- affected chapters visually checked: 1; public readback checked: {not pre_publication}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--build-receipt", type=Path, required=True)
    parser.add_argument("--pre-publication", action="store_true")
    args = parser.parse_args(argv)
    return validate_verdier_successor(args.root, args.build_receipt, args.pre_publication)


if __name__ == "__main__":
    raise SystemExit(main())
