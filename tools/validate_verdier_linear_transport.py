#!/usr/bin/env python3
"""Validate the merge-free public transport of the Verdier II.2.3.1 successor.

The mathematical/source state and its two-build QA remain frozen in a tagged
validated DAG.  The public content commit has exactly that tree with one parent:
the public predecessor.  This validator proves the tree equivalence, the narrow
transport-only follow-up, source packaging for the rendered candidate PDF, and
eventual anonymous public readback.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote
import zipfile


if __package__:
    from . import validate_direct_successor_release as common
else:
    import validate_direct_successor_release as common


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "KokunoYumeto/unofficial-stacks-project-ai-drafts"
REPOSITORY_ID = 1332406685
BASE_COMMIT = "22dd577923c0faa54474021bc7de93a467aa1f47"
BASE_TREE = "e47b62074035be104f95aaa29c49ac2249a7fa9c"
VALIDATED_DAG_COMMIT = "cb8d4b3e9316519824975465d11a83572ab0512f"
VALIDATED_DAG_TREE = "33b365537c44f0170c901ee212aedb18e34d38f8"
VALIDATED_DAG_TAG = "verdier-ii-2-3-1-validated-dag-20260928"
LINEAR_CONTENT_COMMIT = "e5abd8b3d699697b1ab9e2b611efe9f44d02101c"
RECEIPT = "validation/verdier-linear-transport-current.json"
ATTESTATION = (
    "validation/verdier-registered-insertion-successor-2-3-1-"
    "prepublication-attestation-2026-09-28.json"
)
INDEX = "validation/direct-successor-current.json"
PACKAGE_ZIP = "validation/verdier-ast239-2-3-1-candidate-derived-source.zip"
PACKAGE_MANIFEST = "validation/verdier-ast239-2-3-1-candidate-derived-source-manifest.json"
PACKAGE_TOOL = "tools/package_verdier_candidate_pdf_source.py"
PDF_PATH = (
    "ai-integrated/candidates/commons/stacks/verdier-ast239-2-3-1-r1/"
    "builds/derived.pdf"
)
SCHEMA = "unofficial-ai-integrated-stacks-verdier-linear-publication-transport/v1"
RELEASE_SCHEMA = "unofficial-ai-integrated-stacks-verdier-linear-publication-release/v1"
INDEX_SCHEMA = "unofficial-ai-integrated-stacks-direct-release-index/v1"
ATTESTATION_SCHEMA = "unofficial-ai-integrated-stacks-verdier-prepublication-attestation/v1"
PACKAGE_SCHEMA = "unofficial-ai-integrated-stacks-rendered-source-package/v1"
REFERENCE_KEYS = {"path", "bytes", "sha256", "git_blob"}
CORE_ROLES = ("composition", "build", "second_build", "visual_qa", "reproducibility")
AI_DISCLOSURE = "OpenAI Codex — GPT-5.6 Sol, Ultra effort"
PUBLICATION_PREPARATION_CHANGES = {
    "CHANGES_FROM_UPSTREAM.md": "M",
    "tools/validate_verdier_linear_transport.py": "M",
    "upstream-corrections/corrections-only.zip": "M",
    "upstream-corrections/downloads.json": "M",
    "upstream-corrections/manifest.json": "M",
    "validation/changes-from-upstream-2026-08-30.json": "M",
}


require = common.require
safe_path = common.safe_path
parse_json = common.parse_json
identity = common.identity
Objects = common.Objects


def parents(objects: Objects, commit: str) -> list[str]:
    row = objects.text("rev-list", "--parents", "-n", "1", commit).split()
    require(row and row[0] == commit, "cannot read exact commit parents")
    return row[1:]


def changes(objects: Objects, parent: str, child: str) -> dict[str, str]:
    output = objects.text(
        "diff-tree", "--no-commit-id", "--name-status", "--no-renames", "-r",
        parent, child, "--",
    )
    result: dict[str, str] = {}
    if not output:
        return result
    for line in output.splitlines():
        fields = line.split("\t")
        require(len(fields) == 2 and fields[0] in {"A", "M", "D"},
                "unsupported transport path transition")
        path = safe_path(fields[1])
        require(path not in result, "duplicate transport path transition")
        result[path] = fields[0]
    return result


def reference(row: object, label: str) -> dict:
    require(isinstance(row, dict) and set(row) == REFERENCE_KEYS,
            "invalid reference: " + label)
    safe_path(row["path"])
    common.number(row["bytes"])
    common.digest(row["sha256"])
    require(isinstance(row["git_blob"], str)
            and re.fullmatch(r"[0-9a-f]{40}", row["git_blob"]) is not None,
            "invalid Git blob: " + label)
    return row


def clean_reference(objects: Objects, row: object, label: str, revision: str = "HEAD") -> bytes:
    row = reference(row, label)
    observed = objects.ident(revision, row["path"])
    require(observed == {key: row[key] for key in REFERENCE_KEYS - {"path"}},
            "reference identity mismatch: " + label)
    if revision == "HEAD":
        return objects.clean(row["path"])
    return objects.blob(revision, row["path"])


def validate_attestation(objects: Objects, receipt: dict) -> None:
    ref = reference(receipt.get("prepublication_attestation"), "prepublication attestation")
    require(ref["path"] == ATTESTATION, "noncanonical prepublication attestation")
    attestation = parse_json(clean_reference(objects, ref, "prepublication attestation"))
    require(attestation.get("schema") == ATTESTATION_SCHEMA
            and attestation.get("status") == "PASS_PRE_PUBLICATION"
            and attestation.get("source") == {
                "commit": VALIDATED_DAG_COMMIT, "tree": VALIDATED_DAG_TREE,
            }
            and attestation.get("command") ==
                "python -B tools/validate_verdier_registered_insertion_successor.py "
                "--build-receipt validation/verdier-registered-insertion-successor-2-3-1-"
                "build-a-2026-09-28.json --pre-publication"
            and attestation.get("exit_code") == 0,
            "invalid prepublication attestation")
    expected_output = [
        "Verdier registered-insertion successor validation: PASS_PRE_PUBLICATION",
        "- registered insertion operations: 1; stable IDs: 23",
        "- full-profile chapters: 36; exact deterministic builds: 2",
        "- affected chapters visually checked: 1; public readback checked: False",
    ]
    require(attestation.get("observed_output") == expected_output,
            "prepublication output mismatch")
    index_ref = reference(attestation.get("validated_index"), "validated DAG index")
    require(index_ref["path"] == INDEX, "attestation uses a noncanonical index")
    index = parse_json(clean_reference(objects, index_ref, "validated DAG index", VALIDATED_DAG_COMMIT))
    require(index.get("schema") == INDEX_SCHEMA and index.get("status") == "READY_FOR_PUBLICATION",
            "validated DAG index is not ready")
    refs = index.get("references")
    require(isinstance(refs, dict) and set(refs) == set(CORE_ROLES),
            "validated DAG index core roles mismatch")
    require(attestation.get("core_receipts") == refs,
            "attestation/core-index receipt mismatch")
    for role in CORE_ROLES:
        clean_reference(objects, refs[role], "validated DAG " + role, VALIDATED_DAG_COMMIT)
    tools = attestation.get("validator_tools")
    require(isinstance(tools, dict) and set(tools) == {
        "tools/validate_unified_repository.py",
        "tools/validate_verdier_registered_insertion_successor.py",
        "tools/verdier_registered_insertion_successor.py",
    }, "attestation validator-tool inventory mismatch")
    for path, expected in tools.items():
        require(objects.ident(VALIDATED_DAG_COMMIT, path) == expected,
                "attested validator-tool identity mismatch: " + path)


def validate_source_package(objects: Objects, receipt: dict) -> None:
    package = receipt.get("candidate_pdf_source_package")
    require(isinstance(package, dict) and set(package) == {"archive", "manifest", "generator"},
            "incomplete candidate-PDF source package")
    archive_ref = reference(package["archive"], "source archive")
    manifest_ref = reference(package["manifest"], "source-package manifest")
    generator_ref = reference(package["generator"], "source-package generator")
    require(archive_ref["path"] == PACKAGE_ZIP and manifest_ref["path"] == PACKAGE_MANIFEST
            and generator_ref["path"] == PACKAGE_TOOL, "noncanonical candidate source package")
    archive_raw = clean_reference(objects, archive_ref, "source archive")
    manifest = parse_json(clean_reference(objects, manifest_ref, "source-package manifest"))
    clean_reference(objects, generator_ref, "source-package generator")
    require(manifest.get("schema") == PACKAGE_SCHEMA
            and manifest.get("status") == "PASS_COMPLETE_EDITABLE_SOURCE"
            and manifest.get("archive") == {
                "path": PACKAGE_ZIP,
                "bytes": archive_ref["bytes"],
                "sha256": archive_ref["sha256"],
                "entry_count": len(manifest.get("entries", [])),
            }
            and manifest.get("ai_disclosure") == AI_DISCLOSURE
            and manifest.get("human_review_claimed") is False,
            "candidate source-package manifest mismatch")
    artifact = manifest.get("artifact")
    require(isinstance(artifact, dict) and artifact.get("path") == PDF_PATH
            and objects.ident("HEAD", PDF_PATH) == {
                "bytes": artifact.get("bytes"), "sha256": artifact.get("sha256"),
                "git_blob": objects.ident("HEAD", PDF_PATH)["git_blob"],
            }, "candidate PDF/source-package identity mismatch")
    direct = manifest.get("direct_editable_source")
    require(isinstance(direct, dict) and direct.get("path") == "derived.tex",
            "candidate package lacks direct editable source")
    derived = objects.blob("HEAD", "derived.tex")
    require(len(derived) == direct.get("bytes") and identity(derived)["sha256"] == direct.get("sha256"),
            "direct derived.tex identity mismatch")
    rows = manifest.get("entries")
    require(isinstance(rows, list) and rows and all(
        isinstance(row, dict) and set(row) == {"path", "bytes", "sha256"} for row in rows
    ), "invalid source-package entry inventory")
    expected = {row["path"]: row for row in rows}
    require(len(expected) == len(rows), "duplicate source-package manifest entry")
    from io import BytesIO
    with zipfile.ZipFile(BytesIO(archive_raw)) as archive:
        require(archive.namelist() == sorted(expected), "source ZIP order or entry set mismatch")
        require(len(archive.namelist()) == len(set(archive.namelist())),
                "duplicate source ZIP entry")
        for name in archive.namelist():
            data = archive.read(name)
            row = expected[name]
            require(len(data) == row["bytes"] and identity(data)["sha256"] == row["sha256"],
                    "source ZIP entry identity mismatch: " + name)
        require(archive.read("source/derived.tex") == derived,
                "source ZIP derived.tex differs from direct public source")


def validate_preparation(objects: Objects, receipt: dict) -> str:
    base = receipt.get("public_predecessor")
    require(base == {"commit": BASE_COMMIT, "tree": BASE_TREE},
            "transport public predecessor mismatch")
    original = receipt.get("validated_dag")
    require(original == {
        "tag": VALIDATED_DAG_TAG, "commit": VALIDATED_DAG_COMMIT,
        "tree": VALIDATED_DAG_TREE,
    }, "transport validated-DAG identity mismatch")
    require(objects.text("rev-parse", BASE_COMMIT + "^{tree}") == BASE_TREE,
            "public predecessor tree mismatch")
    require(objects.text("rev-parse", VALIDATED_DAG_COMMIT + "^{tree}") == VALIDATED_DAG_TREE,
            "validated DAG tree mismatch")
    require(objects.text("rev-parse", "refs/tags/" + VALIDATED_DAG_TAG + "^{commit}")
            == VALIDATED_DAG_COMMIT, "validated DAG tag is absent or moved")

    linear = receipt.get("linear_content")
    require(linear == {
        "commit": LINEAR_CONTENT_COMMIT, "parent": BASE_COMMIT, "tree": VALIDATED_DAG_TREE,
        "tree_equivalent_to_validated_dag": True,
    }, "linear content identity mismatch")
    require(parents(objects, LINEAR_CONTENT_COMMIT) == [BASE_COMMIT]
            and objects.text("rev-parse", LINEAR_CONTENT_COMMIT + "^{tree}") == VALIDATED_DAG_TREE,
            "linear content is not the exact validated tree on public main")

    prep = receipt.get("transport_preparation")
    require(isinstance(prep, dict)
            and set(prep) == {"commit", "parent", "tree", "paths"},
            "invalid transport-preparation record")
    commit = objects.commit(prep["commit"])
    require(prep["parent"] == LINEAR_CONTENT_COMMIT
            and parents(objects, commit) == [LINEAR_CONTENT_COMMIT]
            and objects.text("rev-parse", commit + "^{tree}") == prep["tree"],
            "transport preparation is not one exact linear child")
    paths = prep["paths"]
    required_paths = {
        "tools/validate_verdier_linear_transport.py",
        PACKAGE_TOOL,
        ATTESTATION,
        PACKAGE_ZIP,
        PACKAGE_MANIFEST,
    }
    require(isinstance(paths, list) and {row.get("path") for row in paths} == required_paths,
            "transport-preparation path inventory mismatch")
    require(changes(objects, LINEAR_CONTENT_COMMIT, commit) == {
        "tools/validate_verdier_linear_transport.py": "M",
        PACKAGE_TOOL: "M",
        ATTESTATION: "A",
        PACKAGE_ZIP: "A",
        PACKAGE_MANIFEST: "A",
    }, "transport preparation changed non-transport content")
    for row in paths:
        clean_reference(objects, row, "transport-preparation path", commit)
    validate_attestation(objects, receipt)
    validate_source_package(objects, receipt)
    return commit


def validate_transport_seal(objects: Objects, receipt: dict, prep: str, seal: str) -> None:
    """Validate either the first seal or one bounded generated-export refresh."""
    publication = receipt.get("publication_preparation")
    if publication is None:
        require(parents(objects, seal) == [prep]
                and changes(objects, prep, seal) == {RECEIPT: "M"},
                "prepublication transport seal mismatch")
        return
    require(isinstance(publication, dict)
            and set(publication) == {"commit", "parent", "tree", "paths", "reason"},
            "invalid publication-preparation record")
    commit = objects.commit(publication["commit"])
    first_seal = objects.commit(publication["parent"])
    require(parents(objects, first_seal) == [prep]
            and changes(objects, prep, first_seal) == {RECEIPT: "M"},
            "publication preparation does not follow the original transport seal")
    require(parents(objects, commit) == [first_seal]
            and objects.text("rev-parse", commit + "^{tree}") == publication["tree"]
            and changes(objects, first_seal, commit) == PUBLICATION_PREPARATION_CHANGES,
            "publication-preparation commit changed the wrong paths")
    rows = publication["paths"]
    require(isinstance(rows, list)
            and {row.get("path") for row in rows} == set(PUBLICATION_PREPARATION_CHANGES),
            "publication-preparation identity inventory mismatch")
    for row in rows:
        clean_reference(objects, row, "publication-preparation path", commit)
    require(publication["reason"] ==
            "refresh deterministic downstream exports for the newly admitted Verdier overlay",
            "publication-preparation rationale mismatch")
    require(parents(objects, seal) == [commit]
            and changes(objects, commit, seal) == {RECEIPT: "M"},
            "refreshed transport seal mismatch")


def validate_release(objects: Objects, receipt: dict, head: str, prep: str, index: dict) -> None:
    refs = index.get("references")
    require(isinstance(refs, dict) and set(refs) == set(CORE_ROLES) | {"release"},
            "publication-complete index roles mismatch")
    release_ref = reference(refs["release"], "release")
    release = parse_json(clean_reference(objects, release_ref, "release"))
    require(release.get("schema") == RELEASE_SCHEMA
            and release.get("status") == "PUBLICATION_COMPLETE"
            and release.get("repository") == REPOSITORY
            and release.get("default_branch") == "main"
            and release.get("ai_disclosure") == AI_DISCLOSURE,
            "invalid linear-transport release receipt")
    require(release.get("content") == {
        "commit": LINEAR_CONTENT_COMMIT, "tree": VALIDATED_DAG_TREE,
    } and release.get("validated_dag") == {
        "tag": VALIDATED_DAG_TAG, "commit": VALIDATED_DAG_COMMIT,
        "tree": VALIDATED_DAG_TREE,
    }, "release content/provenance mismatch")
    seal = objects.commit(release.get("transport_seal", {}).get("commit"))
    require(release["transport_seal"].get("tree") == objects.text("rev-parse", seal + "^{tree}"),
            "release transport-seal tree mismatch")
    validate_transport_seal(objects, receipt, prep, seal)
    require(parents(objects, head) == [seal]
            and changes(objects, seal, head) == {INDEX: "M", release_ref["path"]: "A"},
            "final publication commit is not the exact two-file seal")

    readback = release.get("public_readback")
    require(isinstance(readback, dict) and readback.get("status") == "PASS"
            and readback.get("anonymous") is True and readback.get("commit") == seal,
            "anonymous public readback did not pass")
    rows = readback.get("checked_paths")
    require(isinstance(rows, list) and all(
        isinstance(row, dict) and set(row) == REFERENCE_KEYS for row in rows
    ), "invalid public-readback inventory")
    expected_paths = set(changes(objects, BASE_COMMIT, seal))
    paths = [safe_path(row["path"]) for row in rows]
    require(len(paths) == len(set(paths)) and set(paths) == expected_paths,
            "public readback is not the exact newly published path set")
    for row in rows:
        require(objects.ident(seal, row["path"]) == {
            key: row[key] for key in REFERENCE_KEYS - {"path"}
        }, "public-readback local identity mismatch: " + row["path"])
        common.public_object(
            f"https://raw.githubusercontent.com/{REPOSITORY}/{seal}/"
            + quote(row["path"], safe="/"), row,
        )
    require(readback.get("checked_file_count") == len(rows)
            and readback.get("checked_total_bytes") == sum(row["bytes"] for row in rows),
            "public-readback totals mismatch")

    workflow = release.get("workflow")
    require(isinstance(workflow, dict) and workflow.get("name") == "Unified repository validation"
            and workflow.get("status") == "completed" and workflow.get("conclusion") == "success"
            and workflow.get("head_sha") == seal
            and type(workflow.get("run_id")) is int and workflow["run_id"] > 0,
            "release workflow binding mismatch")
    remote_run = common.public_json(
        f"https://api.github.com/repos/{REPOSITORY}/actions/runs/{workflow['run_id']}"
    )
    require(remote_run.get("id") == workflow["run_id"]
            and remote_run.get("head_sha") == seal
            and remote_run.get("name") == workflow["name"]
            and remote_run.get("status") == "completed"
            and remote_run.get("conclusion") == "success",
            "public workflow readback mismatch")
    remote_repo = common.public_json(f"https://api.github.com/repos/{REPOSITORY}")
    require(remote_repo.get("id") == REPOSITORY_ID and remote_repo.get("private") is False
            and remote_repo.get("default_branch") == "main", "repository is not public")
    remote_main = common.public_json(f"https://api.github.com/repos/{REPOSITORY}/git/ref/heads/main")
    require(remote_main.get("object", {}).get("sha") == head,
            "validated final HEAD is not public main")
    remote_tag = common.public_json(
        f"https://api.github.com/repos/{REPOSITORY}/git/ref/tags/{VALIDATED_DAG_TAG}"
    )
    require(remote_tag.get("object", {}).get("sha") == VALIDATED_DAG_COMMIT,
            "public validated-DAG tag mismatch")
    for path in (INDEX, release_ref["path"]):
        observed = {"path": path, **objects.ident(head, path)}
        common.public_object(
            f"https://raw.githubusercontent.com/{REPOSITORY}/{head}/" + quote(path, safe="/"),
            observed,
        )


def validate_linear_transport(root: Path, pre_publication: bool = False) -> int:
    try:
        objects = Objects(Path(root).resolve())
        initial = objects.text("rev-parse", "HEAD")
        receipt_raw = objects.clean(RECEIPT)
        receipt = parse_json(receipt_raw)
        require(receipt.get("schema") == SCHEMA
                and receipt.get("status") == "READY_FOR_PUBLICATION"
                and receipt.get("repository") == REPOSITORY
                and receipt.get("default_branch") == "main"
                and receipt.get("ai_disclosure") == AI_DISCLOSURE,
                "invalid Verdier linear-transport receipt")
        prep = validate_preparation(objects, receipt)
        index_raw = objects.clean(INDEX)
        index = parse_json(index_raw)
        require(index.get("schema") == INDEX_SCHEMA, "unsupported current release index")
        status = index.get("status")
        objects.linear(BASE_COMMIT, initial)
        require(not objects.text("rev-list", "--min-parents=2", BASE_COMMIT + ".." + initial),
                "merge commit remains in public transport")
        if status == "READY_FOR_PUBLICATION":
            require(pre_publication, "linear transport is not publication-complete")
            validate_transport_seal(objects, receipt, prep, initial)
        elif status == "PUBLICATION_COMPLETE":
            validate_release(objects, receipt, initial, prep, index)
        else:
            raise ValueError("invalid current release-index status")
        require(objects.text("rev-parse", "HEAD") == initial
                and objects.clean(RECEIPT) == receipt_raw
                and objects.clean(INDEX) == index_raw,
                "linear-transport validation inputs moved")
    except (OSError, ValueError, KeyError, TypeError, AttributeError, ImportError,
            RuntimeError, json.JSONDecodeError, subprocess.SubprocessError,
            zipfile.BadZipFile) as exc:
        print("Verdier linear publication transport: FAIL\n- " + str(exc), file=sys.stderr)
        return 1
    print("Verdier linear publication transport: "
          + ("PASS_PRE_PUBLICATION" if status == "READY_FOR_PUBLICATION"
             else "PUBLICATION_COMPLETE"))
    print("- validated DAG preserved by immutable tag; linear content tree is byte-identical")
    print("- protected main range contains zero merge commits")
    print("- candidate PDF has direct editable LaTeX plus a complete deterministic source ZIP")
    print(f"- anonymous public readback checked: {status == 'PUBLICATION_COMPLETE'}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--pre-publication", action="store_true")
    args = parser.parse_args(argv)
    return validate_linear_transport(args.root, args.pre_publication)


if __name__ == "__main__":
    raise SystemExit(main())
