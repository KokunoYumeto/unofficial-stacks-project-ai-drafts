#!/usr/bin/env python3
"""Bind a GitHub-only R40--R47 publication to completed, immutable evidence.

This local writer performs no build, network request, authentication or Git
mutation. It runs the committed pre-publication validator, then consumes saved
real observations; a run ID or an asserted PASS alone is not sufficient.

Required observations (repository-relative JSON paths):
--workflow-receipt: the unedited GitHub Actions run API response.
--readback-receipt: schema ``unofficial-stacks-github-source-readback/v1``,
status PASS, checked_utc, authentication ``none``, and github containing
repository, repository_id, repository_public, default_branch, main_head,
main_tree. Its changed_path_readback object is the exact output of
verify_errata_release_readback.verify_changed_paths, covering the complete
previous-public-main to content-head delta (not a selected sample). That
object includes both tree IDs, every row, totals and its canonical JSON hash.
For deletions, also record head_absence_verified=true on the row, from the
anonymous complete remote tree, rather than claiming that reading old bytes
alone proves deletion. Save the outer readback only after these observations.

Recommended noncircular publication sequence:
1. Commit the completed core build/visual/repro receipts and this tooling at C;
   push C to public main and let C's exact-head validation workflow finish.
2. Save C's real successful workflow response and anonymous complete C readback
   as UNTRACKED local JSON files. Neither observation has to be committed at C;
   in particular, never try to commit C's own future workflow response inside C.
3. With C checked out, invoke this writer with BOTH --content-head C and
   --metadata-head C. The empty C-to-C metadata delta is supported. Observation
   files are loaded as local evidence, not read from C's Git tree. The writer
   emits the new release receipt only after checking the actual observations.
4. Commit the two observation files and the new release receipt in successor R;
   push R, check R's workflow, and anonymously read back those three exact files.
   Record that final transaction separately; the receipt written in step 3 does
   not claim to have already observed its own future publication.

All core receipts must already be committed at the content head. A distinct
metadata head is optional, must be checked out, and may follow the content head
only by adding observation files; its own workflow response still comes AFTER
that head exists. The same-head/untracked-observation route above is preferred.

No R47 Zenodo version is created or implied. An optional committed historical
release receipt identifies the last major milestone as historical evidence,
not as a fresh access check or evidence that the R47 files are on Zenodo.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from functools import cache
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "KokunoYumeto/unofficial-stacks-project-ai-drafts"
REPOSITORY_ID = 1332406685
PREFIX = "validation/stacks-errata-a04446e-r47-"
SUFFIX = "-2026-09-06.json"
OUTPUT = PREFIX + "release" + SUFFIX
PATHS = {
    "composition": "validation/composition-current.json",
    "independent": PREFIX + "independent-composition" + SUFFIX,
    "build": PREFIX + "build" + SUFFIX,
    "visual": PREFIX + "visual-qa" + SUFFIX,
    "repro": PREFIX + "reproducibility" + SUFFIX,
    "second": PREFIX + "reproducibility-second" + SUFFIX,
}
CODE_PATHS = (
    "tools/write_r47_github_release_receipt.py",
    "tools/validate_unified_repository.py",
    "tools/compare_fixed_point_builds.py",
    "tools/build_fixed_point.py",
    "tools/verify_ega_checkpoint_successor.py",
    ".github/workflows/validate.yml",
)
OVERLAYS = [f"stacks-errata-a04446e-r{number}" for number in range(40, 48)]
SOURCE_HEAD = "b3c4a28c053dbbd45670dd19cf0dcc45063190dc"
PREVIOUS_PUBLIC = "f73b18165c7162b8386de06cc3c50bd4ced745b6"
CUTOFF = "e4a7b1cb0b0e7fa4c499ab26cf85275f4f9fed12"
CONCEPT_DOI = "10.5281/zenodo.22135180"
DEFECT_KEYS = (
    "clipped_content", "overlapping_content", "blank_pages", "corrupted_pages",
    "missing_or_unreadable_glyphs", "broken_diagrams",
)
BUILD_CODE = frozenset({
    "tools/build_fixed_point.py", "tools/verify_ega_checkpoint_successor.py",
    "tools/compare_fixed_point_builds.py", "tools/validate_unified_repository.py",
})


def require(condition: Any, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def exact(actual: Any, expected: Any, message: str) -> None:
    require(canonical(actual) == canonical(expected), message)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest().upper()


def relative(value: str) -> str:
    require(isinstance(value, str) and value and "\\" not in value and ":" not in value
            and "\x00" not in value, "invalid repository-relative path")
    path = PurePosixPath(value)
    require(not path.is_absolute() and ".." not in path.parts
            and path.as_posix() == value and value != ".", "path escapes repository")
    return value


def identity(path: str, raw: bytes) -> dict[str, Any]:
    return {"path": relative(path), "bytes": len(raw), "sha256": digest(raw),
            "git_blob": hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()}


def parse_json(raw: bytes) -> dict[str, Any]:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON object key")
            result[key] = value
        return result

    def constant(value: str) -> None:
        raise ValueError("non-finite JSON constant")

    value = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs, parse_constant=constant)
    require(isinstance(value, dict), "JSON object required")
    return value


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *args], stderr=subprocess.PIPE)


@cache
def commit(value: str) -> str:
    require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value),
            "exact lowercase forty-character commit required")
    require(git("rev-parse", f"{value}^{{commit}}").decode().strip() == value,
            "commit identity mismatch")
    return value


@cache
def tree(value: str) -> str:
    return git("rev-parse", f"{commit(value)}^{{tree}}").decode().strip()


def ancestor(older: str, newer: str) -> None:
    result = subprocess.run(["git", "-C", str(ROOT), "merge-base", "--is-ancestor",
                             commit(older), commit(newer)], capture_output=True)
    require(result.returncode == 0, "required commit ancestry does not hold")


def blob(revision: str, path: str) -> bytes:
    return git("show", f"{commit(revision)}:{relative(path)}")


def load(path: str, revision: str | None = None) -> tuple[dict, dict]:
    path = relative(path)
    disk = ROOT / path
    require(disk.resolve().is_relative_to(ROOT.resolve()) and not disk.is_symlink(),
            "evidence path escapes repository or is a symlink")
    raw = disk.read_bytes()
    if revision is not None:
        require(raw == blob(revision, path), f"evidence is not exact committed bytes: {path}")
    return parse_json(raw), identity(path, raw)


def delta(base: str, head: str) -> dict[str, tuple[str, str, str]]:
    """Inspect immutable trees only, never enumerate working-tree untracked files."""
    raw = git("diff-tree", "-r", "--no-commit-id", "--raw", "-z", "--no-renames",
              commit(base), commit(head)).split(b"\0")
    require(raw[-1] == b"", "unterminated Git delta")
    raw.pop()
    require(len(raw) % 2 == 0, "malformed Git delta")
    result = {}
    for header, path_bytes in zip(raw[::2], raw[1::2]):
        mode_before, mode_after, before, after, status = header.decode("ascii")[1:].split()
        path = relative(path_bytes.decode("utf-8"))
        require(status in {"A", "M", "D"} and path not in result
                and mode_before in {"000000", "100644", "100755"}
                and mode_after in {"000000", "100644", "100755"},
                "unsupported Git delta entry or file mode")
        result[path] = ({"A": "added", "M": "modified", "D": "deleted"}[status], before, after)
    return result


def validate_workflow(value: dict, metadata: str) -> dict:
    require(value.get("name") == "Unified repository validation"
            and value.get("head_sha") == metadata and value.get("status") == "completed"
            and value.get("conclusion") == "success" and value.get("event") == "push",
            "workflow is not a completed successful exact-head push run")
    repo = value.get("repository", {})
    require(type(repo.get("id")) is int and repo["id"] == REPOSITORY_ID
            and repo.get("full_name") == REPOSITORY and repo.get("private") is False,
            "workflow repository identity/publicity mismatch")
    require(value.get("head_commit", {}).get("id") == metadata
            and value["head_commit"].get("tree_id") == tree(metadata),
            "workflow commit/tree mismatch")
    run_id, attempt = value.get("id"), value.get("run_attempt")
    require(type(run_id) is int and run_id > 0 and type(attempt) is int and attempt > 0,
            "workflow lacks run/attempt identity")
    url = f"https://github.com/{REPOSITORY}/actions/runs/{run_id}"
    require(value.get("html_url") == url, "workflow URL mismatch")
    return {"name": value["name"], "run_id": run_id, "attempt": attempt,
            "head_sha": metadata, "status": "completed", "conclusion": "success",
            "url": url, "role": "successful exact-head R47 metadata validation"}


def validate_readback(value: dict, content: str, metadata: str,
                      decisive: set[str]) -> tuple[list[dict], list[dict]]:
    require(value.get("schema") == "unofficial-stacks-github-source-readback/v1"
            and value.get("status") == "PASS" and value.get("authentication") == "none",
            "missing passing anonymous GitHub source readback")
    require(isinstance(value.get("checked_utc"), str)
            and datetime.fromisoformat(value["checked_utc"].replace("Z", "+00:00")).utcoffset() is not None,
            "readback lacks an observation timestamp")
    gh = value.get("github", {})
    require(gh.get("repository") == REPOSITORY
            and type(gh.get("repository_id")) is int and gh["repository_id"] == REPOSITORY_ID
            and gh.get("repository_public") is True and gh.get("default_branch") == "main"
            and gh.get("main_head") == metadata and gh.get("main_tree") == tree(metadata),
            "public repository/main identity mismatch")
    changed = value.get("changed_path_readback", {})
    require(changed.get("status") == "PASS" and changed.get("base_commit") == PREVIOUS_PUBLIC
            and changed.get("base_tree") == tree(PREVIOUS_PUBLIC)
            and changed.get("head_commit") == content and changed.get("head_tree") == tree(content),
            "changed-path readback base/head/tree mismatch")
    expected = delta(PREVIOUS_PUBLIC, content)
    rows = changed.get("changed_paths")
    require(isinstance(rows, list) and rows, "empty changed-path readback")
    seen, kept, deleted = set(), [], []
    for row in rows:
        require(isinstance(row, dict), "invalid readback row")
        path = relative(row.get("path"))
        require(path in expected and path not in seen, "extra or duplicate changed path")
        seen.add(path)
        status, before, after = expected[path]
        revision = PREVIOUS_PUBLIC if status == "deleted" else content
        require(row.get("status") == status and row.get("status_check") == "PASS"
                and row.get("readback_commit") == revision, "readback status/revision mismatch")
        ident = identity(path, blob(revision, path))
        exact({key: row.get(key) for key in ident}, ident, "public byte/blob identity mismatch")
        if status != "added":
            require(row.get("base_git_blob") == before, "public base blob mismatch")
        if status != "deleted":
            require(row.get("head_git_blob") == after, "public head blob mismatch")
        else:
            require(row.get("head_absence_verified") is True,
                    "deleted path was not proved absent from the public head tree")
        (deleted if status == "deleted" else kept).append(ident)
    require(seen == set(expected), "readback omits changed files")
    exact(changed.get("changed_path_count"), len(rows), "readback count mismatch")
    exact(changed.get("readback_bytes"), sum(row["bytes"] for row in rows), "readback byte total mismatch")
    require(changed.get("changed_path_tuple_set_sha256") == digest(canonical(rows)),
            "readback complete-listing digest mismatch")
    require(decisive.issubset({row["path"] for row in kept}), "readback omits decisive R47 evidence")
    return kept, deleted


def validate_core(evidence: dict, ids: dict, content: str) -> tuple[list[dict], str]:
    comp, build, visual, repro, second, independent = (
        evidence[key] for key in ("composition", "build", "visual", "repro", "second", "independent"))
    require(all(evidence[key].get("status") == "PASS"
                for key in ("composition", "build", "visual", "repro", "second")),
            "core validation evidence has not passed")
    require(comp.get("schema") == "unofficial-ai-integrated-stacks-composition/v3"
            and comp["composition"]["source_commit"] == SOURCE_HEAD
            and comp["registry"]["cutoff_commit"] == CUTOFF
            and comp["previous_cutoff"]["public_main_head"] == PREVIOUS_PUBLIC,
            "wrong R47 composition identity")
    exact([row["id"] for row in comp["new_overlays"]], OVERLAYS, "wrong R47 overlay order")
    exact(comp["composition"]["new_operations"], 177, "wrong R47 operation count")
    exact(comp["composition"]["new_byte_edit_operations"], 177, "wrong R47 byte-edit count")
    require(build["source"]["tree"] == tree(build["source"]["commit"]), "build source tree mismatch")
    ancestor(SOURCE_HEAD, build["source"]["commit"])
    ancestor(build["source"]["commit"], content)
    for path in delta(build["source"]["commit"], content):
        parsed = PurePosixPath(path)
        require(not (len(parsed.parts) == 1 and parsed.suffix in {".tex", ".sty", ".cls", ".bib"})
                and not path.startswith(("ega/", "tags/", "ai-integrated/registry/", "ai-integrated/candidates/"))
                and path not in BUILD_CODE and path != PATHS["composition"]
                and path != "validation/ega-i-6.6.5-semantic-checkpoint-2026-09-06.json",
                f"build-relevant source or validation code changed after the build: {path}")
    require(build["composition"]["receipt_sha256"] == ids["composition"]["sha256"]
            and build["composition"]["receipt_git_blob"] == ids["composition"]["git_blob"]
            and build["composition"]["registry_cutoff_commit"] == CUTOFF,
            "build/composition identity mismatch")
    builder = identity(build["builder"]["path"], blob(build["source"]["commit"], build["builder"]["path"]))
    require(all(build["builder"].get(key) == builder[key] for key in ("path", "sha256", "git_blob")),
            "builder code identity mismatch")
    # Imported only after main has pinned these local implementation bytes.
    if __package__:
        from .compare_fixed_point_builds import compare_receipts
    else:
        from compare_fixed_point_builds import compare_receipts
    compare_receipts(build, second)
    artifacts = build["artifacts"]
    require(isinstance(artifacts, list) and len(artifacts) == 35, "R47 requires 35 built chapters")
    stems = [row["stem"] for row in artifacts]
    require(len(set(stems)) == 35 and set(stems) == set(comp["required_build_stems"]),
            "build chapter inventory mismatch")
    tuples = []
    for row in artifacts:
        require(type(row.get("pages")) is int and row["pages"] > 0
                and type(row.get("bytes")) is int and row["bytes"] > 0
                and isinstance(row.get("sha256"), str) and re.fullmatch(r"[0-9A-F]{64}", row["sha256"]),
                "invalid built PDF identity")
        tuples.append({key: row[key] for key in ("stem", "pages", "bytes", "sha256")})
    tuple_sha = digest(("\n".join("|".join(str(row[key]) for key in ("stem", "pages", "bytes", "sha256"))
                                   for row in sorted(tuples, key=lambda row: row["stem"])) + "\n").encode())
    require(build["build"].get("artifact_tuple_set_sha256") == tuple_sha, "build artifact tuple hash mismatch")
    for key in ("source", "builder", "environment"):
        exact(repro.get(key), build[key], f"reproducibility {key} drift")
    for key, evidence_key in (("first", "build"), ("second", "second")):
        # Raw bytes already bound by load; compare the exact emitted run identity.
        expected = {"receipt": ids[evidence_key]["path"], "created_utc": evidence[evidence_key]["created_utc"],
                    "bytes": ids[evidence_key]["bytes"], "sha256": ids[evidence_key]["sha256"], "status": "PASS",
                    "global_fixed_point_sweep": evidence[evidence_key]["build"]["global_fixed_point_sweep"]}
        exact(repro["runs"][key], expected, "reproducibility invocation binding mismatch")
    exact(repro.get("artifacts"), tuples, "reproducibility PDF inventory drift")
    comparison = {"chapter_count": 35, "matched_artifact_count": 35, "different_artifact_count": 0,
                  "different_artifacts": [], "total_pages_each_run": sum(row["pages"] for row in tuples),
                  "total_pdf_bytes_each_run": sum(row["bytes"] for row in tuples),
                  "artifact_tuple_set_sha256_each_run": tuple_sha,
                  **{key: True for key in ("all_artifact_identities_exactly_equal", "source_identity_equal",
                                          "builder_identity_equal", "environment_identity_equal",
                                          "fixed_point_sweep_equal", "source_checkpoint_identity_equal")}}
    exact(repro.get("comparison"), comparison, "reproducibility comparison mismatch")
    exact(visual.get("source"), build["source"], "visual source mismatch")
    exact(visual.get("build_receipt"), {key: ids["build"][key] for key in ("path", "bytes", "sha256")}
          | {"status": "PASS", "global_fixed_point_sweep": build["build"]["global_fixed_point_sweep"]},
          "visual build binding mismatch")
    affected = sorted(Path(path).stem for path in comp["composition"]["affected_sources"])
    require(len(affected) == 5, "wrong R47 affected chapter count")
    exact(visual["scope"]["affected_chapters"], affected, "visual chapter scope mismatch")
    pages = sum(row["pages"] for row in tuples if row["stem"] in affected)
    for key in ("full_page_render_count", "full_page_contact_sheet_review_count"):
        exact(visual["scope"].get(key), pages, "visual QA does not cover all affected pages")
    for key, expected in (("accepted_operation_count", 177), ("applied_byte_edit_count", 177),
                          ("historical_noop_operation_count", 0)):
        exact(visual["scope"].get(key), expected, "visual operation scope mismatch")
    require(all(type(visual["checks"].get(key)) is int and visual["checks"][key] == 0 for key in DEFECT_KEYS),
            "visual defects remain or counts are missing")
    for key in ("all_pages_rendered", "all_pages_manually_inspected",
                "all_manifest_bound_locus_pages_inspected_at_high_resolution", "page_dimensions_consistent",
                "headers_and_page_numbers_consistent", "text_and_formulas_legible", "diagrams_intact"):
        require(visual["checks"].get(key) is True, f"visual gate not passed: {key}")
    require(independent.get("status") == "PASS_WITH_SEPARATE_RETAINED_INHERITED_FINDINGS"
            and independent["scope"]["composed_source_commit"] == SOURCE_HEAD
            and independent["scope"]["composed_source_tree"] == tree(SOURCE_HEAD),
            "independent composition source mismatch")
    for key in ("import_transport", "manifest_schema_and_closure", "independent_replay_of_177_introduced_operations",
                "all_non_operation_parent_bytes_preserved", "prior_cumulative_differences_preserved",
                "targeted_mathematical_changes_reviewed"):
        require(independent["checks"].get(key) == "PASS", "independent composition did not pass")
    exact(independent["checks"].get("introduced_defects_found"), 0, "introduced composition defects remain")
    return tuples, tuple_sha


def validate_repository(metadata: str, code_ids: list[dict]) -> dict:
    require(git("rev-parse", "HEAD").decode().strip() == metadata, "metadata head must be checked out")
    result = subprocess.run([sys.executable, "-B", "tools/validate_unified_repository.py", "--pre-publication"],
                            cwd=ROOT, capture_output=True, timeout=1800)
    require(result.returncode == 0 and b"Unified repository validation: PASS" in result.stdout,
            "repository pre-publication validation failed (no receipt written)")
    return {"status": "PASS", "head_commit": metadata, "head_tree": tree(metadata),
            "command": ["python", "-B", "tools/validate_unified_repository.py", "--pre-publication"],
            "exit_code": 0, "stdout_bytes": len(result.stdout), "stdout_sha256": digest(result.stdout),
            "stderr_bytes": len(result.stderr), "stderr_sha256": digest(result.stderr), "code": code_ids}


def create_receipt(content: str, metadata: str, workflow_path: str, readback_path: str,
                   zenodo_history: str | None = None) -> dict:
    content, metadata = commit(content), commit(metadata)
    ancestor(content, metadata)
    require(git("rev-parse", "HEAD").decode().strip() == metadata, "metadata head must be checked out")
    allowed_metadata = {relative(workflow_path), relative(readback_path)}
    metadata_changes = delta(content, metadata)
    require(set(metadata_changes).issubset(allowed_metadata)
            and all(row[0] == "added" for row in metadata_changes.values()),
            "metadata successor changed more than newly added publication observations")
    frozen = {}
    for path in CODE_PATHS:
        raw = (ROOT / path).read_bytes()
        require(raw == blob(content, path) == blob(metadata, path), f"uncommitted or drifting implementation: {path}")
        frozen[path] = identity(path, raw)
    evidence, ids = {}, {}
    for key, path in PATHS.items():
        evidence[key], ids[key] = load(path, content)
        require(blob(content, path) == blob(metadata, path), "core evidence changed after publication")
        frozen[path] = ids[key]
    tuples, tuple_sha = validate_core(evidence, ids, content)
    comp, build, visual, repro = (evidence[key] for key in ("composition", "build", "visual", "repro"))
    registry, registry_id = load("ai-integrated/registry/overlays.json", content)
    _, leases_id = load("ai-integrated/registry/leases.json", content)
    for ident in (registry_id, leases_id):
        frozen[ident["path"]] = ident
    entries = registry["registered_entries"]
    exact([row["id"] for row in entries[-8:]], OVERLAYS, "registry tail mismatch")
    exact(len(entries), comp["registry"]["registered_overlays"], "registry overlay count mismatch")
    exact(sum(len(row["stable_ids"]) for row in entries), comp["registry"]["registered_stable_ids"],
          "registry stable-ID count mismatch")
    require(registry_id["sha256"] == comp["registry"]["overlays_sha256"]
            and registry_id["git_blob"] == comp["registry"]["overlays_git_blob"]
            and leases_id["sha256"] == comp["registry"]["leases_sha256"]
            and leases_id["git_blob"] == comp["registry"]["leases_git_blob"], "registry byte identity mismatch")
    sources = []
    for path, expected in comp["composition"]["affected_sources"].items():
        raw = blob(content, path)
        ident = identity(path, raw)
        require(raw == blob(build["source"]["commit"], path) == (ROOT / path).read_bytes(),
                "composed source changed after the build")
        require(all(ident[key] == expected["composed_" + key] for key in ("bytes", "sha256", "git_blob")),
                "composed source differs from admitted operations")
        sources.append(ident)
        frozen[path] = ident
    workflow_raw, workflow_id = load(workflow_path)
    readback_raw, readback_id = load(readback_path)
    require(workflow_id["path"] != readback_id["path"], "workflow and readback must be distinct")
    frozen.update({ident["path"]: ident for ident in (workflow_id, readback_id)})
    workflow = validate_workflow(workflow_raw, metadata)
    decisive = set(PATHS.values()) | {row["path"] for row in sources} | set(CODE_PATHS)
    kept, deleted = validate_readback(readback_raw, content, metadata, decisive)
    zenodo = {"status": "UNCHANGED_NO_NEW_R47_VERSION", "new_version_created": False,
              "policy": "Sparse substantial milestones only; R47 is incremental GitHub publication.",
              "current_access_reverified_by_this_writer": False}
    if zenodo_history:
        history, history_id = load(zenodo_history, content)
        require(history.get("status") == "PUBLICATION_COMPLETE"
                and history.get("preservation", {}).get("status") == "PUBLIC_READBACK_VERIFIED",
                "historical Zenodo publication is not verified")
        zn = history["preservation"]["zenodo"]
        require(zn.get("concept_doi") == CONCEPT_DOI and zn.get("access_right") == "open"
                and type(zn.get("record_id")) is int and zn["record_id"] > 0
                and zn.get("doi") == f"10.5281/zenodo.{zn['record_id']}", "historical Zenodo identity mismatch")
        zenodo.update({"historical_evidence": history_id,
                       "last_major_milestone": {key: zn[key] for key in ("record_id", "doi", "concept_doi", "access_right")}})
        frozen[history_id["path"]] = history_id
    local_validation = validate_repository(metadata, [frozen[path] for path in CODE_PATHS])
    require(git("rev-parse", "HEAD").decode().strip() == metadata, "HEAD moved during receipt validation")
    for path, ident in frozen.items():
        exact(identity(path, (ROOT / path).read_bytes()), ident, "evidence changed during validation")
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    result = {
        "schema": "unofficial-ai-integrated-stacks-errata-release/v1",
        "phase": "published", "status": "PUBLICATION_COMPLETE", "created_utc": now,
        "publication_scope": "GitHub main source, registry, and validation evidence only; no new Zenodo release",
        "release": {"repository": REPOSITORY, "default_branch": "main", "repository_id": REPOSITORY_ID,
                    "previous_public_main_head": PREVIOUS_PUBLIC, "frozen_registry_cutoff": CUTOFF,
                    "frozen_registry_tree": comp["registry"]["cutoff_tree"],
                    "registered_overlays": len(entries), "registered_stable_ids": comp["registry"]["registered_stable_ids"],
                    "published_content_head": content, "content_head": content, "content_tree": tree(content),
                    "metadata_head": metadata, "metadata_tree": tree(metadata), "admitted_and_composed": OVERLAYS},
        "composition": {"receipt": ids["composition"], "independent_review": ids["independent"],
                        "source_commit": SOURCE_HEAD, "source_tree": tree(SOURCE_HEAD),
                        "new_operations": 177, "new_byte_edit_operations": 177,
                        "order": OVERLAYS, "composed_sources": sources,
                        "inherited_findings": "Retained separately in the independent receipt; not claimed resolved."},
        "build": {"receipt_path": PATHS["build"], "receipt_bytes": ids["build"]["bytes"],
                  "receipt_sha256": ids["build"]["sha256"], "receipt_git_blob": ids["build"]["git_blob"],
                  "source_commit": build["source"]["commit"], "source_tree": build["source"]["tree"],
                  "chapters": len(tuples), "pages": sum(row["pages"] for row in tuples),
                  "pdf_bytes": sum(row["bytes"] for row in tuples),
                  "global_fixed_point_sweep": build["build"]["global_fixed_point_sweep"],
                  "artifact_tuple_set_sha256": tuple_sha},
        "visual_qa": {"status": "PASS", "receipt_path": PATHS["visual"],
                      "receipt_bytes": ids["visual"]["bytes"], "receipt_sha256": ids["visual"]["sha256"],
                      "receipt_git_blob": ids["visual"]["git_blob"],
                      "full_page_reviews": visual["scope"]["full_page_contact_sheet_review_count"],
                      "high_resolution_locus_pages": visual["scope"]["high_resolution_locus_page_count"],
                      "defects": sum(visual["checks"][key] for key in DEFECT_KEYS)},
        "reproducibility": {"status": "PASS", "summary_path": PATHS["repro"],
                            "summary_bytes": ids["repro"]["bytes"], "summary_sha256": ids["repro"]["sha256"],
                            "summary_git_blob": ids["repro"]["git_blob"], "second_receipt_path": PATHS["second"],
                            "second_receipt_bytes": ids["second"]["bytes"], "second_receipt_sha256": ids["second"]["sha256"],
                            "second_receipt_git_blob": ids["second"]["git_blob"], "matched_artifacts": len(tuples),
                            "different_artifacts": 0, "artifact_tuple_set_sha256": tuple_sha},
        "registry": {"overlays": registry_id, "leases": leases_id},
        "workflow": workflow, "workflow_evidence": workflow_id,
        "public_readback": {"status": "PASS", "receipt": readback_id, "commit": content,
                            "checked_utc": readback_raw["checked_utc"], "method": "saved anonymous exact changed-file readback",
                            "checked_paths": kept, "deleted_paths_read_at_base": deleted,
                            "changed_path_readback_count": len(kept) + len(deleted),
                            "changed_path_readback_bytes": sum(row["bytes"] for row in kept + deleted)},
        "local_pre_publication_validation": local_validation, "zenodo": zenodo,
        "scope_note": "This is not complete EGA coverage, machine-checked mathematical formalization, or official Stacks review/endorsement.",
        "receipt_publication": "This newly written receipt still requires its own push and anonymous readback; it does not self-certify those future actions.",
    }
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--content-head", required=True, help="published core commit C; normally also pass C as --metadata-head")
    parser.add_argument("--metadata-head", required=True, help="checked-out workflow head; recommended: the same commit C")
    parser.add_argument("--workflow-receipt", required=True, help="saved real workflow response; may be an untracked local JSON file")
    parser.add_argument("--readback-receipt", required=True, help="saved anonymous full readback; may be an untracked local JSON file")
    parser.add_argument("--zenodo-history-receipt")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args(argv)
    try:
        require(not (ROOT / OUTPUT).exists(), "refusing to overwrite an existing release receipt")
        result = create_receipt(args.content_head, args.metadata_head,
                                relative(args.workflow_receipt), relative(args.readback_receipt),
                                relative(args.zenodo_history_receipt) if args.zenodo_history_receipt else None)
        raw = (json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
        if not args.check_only:
            output = ROOT / OUTPUT
            require(output.parent.resolve().is_relative_to(ROOT.resolve()), "output directory escapes repository")
            # Exclusive creation never overwrites historical receipts or a racing writer.
            with output.open("xb") as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
        print(json.dumps({"status": "PASS", "receipt_status": result["status"], "written": not args.check_only,
                          **identity(OUTPUT, raw)}, sort_keys=True))
        return 0
    except (ValueError, KeyError, TypeError, OSError, subprocess.SubprocessError) as error:
        # Public diagnostics never expose a local account path or credentials.
        message = str(error).replace(str(ROOT), "<repository>").replace(ROOT.as_posix(), "<repository>")
        account = Path.home().name
        if account:
            message = re.sub(re.escape(account), "[LOCAL_ACCOUNT]", message, flags=re.IGNORECASE)
        print(json.dumps({"status": "FAIL", "error": message}, sort_keys=True))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
