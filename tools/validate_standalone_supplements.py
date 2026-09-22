"""Validate unchanged sealed Stacks source plus independently built supplements.

The historical validator remains byte-identical and is run at its exact
previously passing commit. Every current difference must belong to an explicit
supplement/document scope. No root TeX, registry, historical receipt, or legacy
tool may change through this path. This is not a cumulative-source admission.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CORE = "0e40e317e02e7b05437fcc7c7f13659e140e128f"
CORE_TREE = "701a0c6ea3bfe093a38eb13b0952423029e389ed"
NOTES = "15923b8e799b486ed325e14da1cfea7f1cab97d3"
DOCS = {"README.md", "ROADMAP.md", "PROPOSED_CORRECTIONS.md", "POSSIBLE_ADDITIONS.md"}
NEW_TOOLS = {"tools/generate_possible_fix_patches.py", "tools/validate_standalone_supplements.py",
             "tests/test_standalone_supplements.py", ".github/workflows/validate.yml",
             "tools/export_upstream_corrections.py", "tests/test_upstream_correction_export.py"}
MODULE_FILES = {"INTAKE.md", "README.md", "REPRODUCE.md", "REVIEW.md", "build.py", "check.py",
    "01-category-models.pdf", "02-category-models.tex", "03-category-models-source.zip",
    "source-map.json", "received-inventory.json", "integration.json", "build-receipt.json",
    "visual-qa.json", "release.json", "04-homotopy-intervals.pdf", "05-homotopy-intervals.tex",
    "06-homotopy-intervals-source.zip", "INTERVALS_REVIEW.md", "INTERVALS_REPRODUCE.md",
    "intervals-source-map.json", "intervals-integration.json", "intervals-build-receipt.json",
    "intervals-visual-qa.json", "intervals-release.json"}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, check=True).stdout


def sha(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def bound(raw, row):
    require(len(raw) == row["bytes"] and sha(raw) == row["sha256"], "artifact byte/hash mismatch")


def safe(name):
    require(isinstance(name, str) and re.fullmatch(r"[A-Za-z0-9._/-]+", name) and not name.startswith("/") and "\\" not in name
            and all(p not in {"", ".", ".."} for p in name.split("/")), "unsafe package path")
    return name


def check_changes(changes, allowed):
    for status, name in changes:
        require(status in {"A", "M"}, "deletion, rename, or file-type change is not a supplement")
        require(name in allowed, "protected source/evidence/tool changed: " + name)


def check_package(raw, source_path, source):
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        names = archive.namelist()
        require(len(names) == len(set(names)) and archive.testzip() is None, "duplicate or corrupt ZIP entry")
        for name in names:
            safe(name)
        manifest = json.loads(archive.read("source-package.json"))
        rows = manifest["files"]
        require(set(names) == {r["path"] for r in rows} | {"source-package.json"}, "incomplete ZIP inventory")
        require(len(rows) == len({r["path"] for r in rows}), "duplicate package inventory path")
        for row in rows:
            bound(archive.read(row["path"]), row)
        required = {"COPYING", "tools/tex_process_guard.py", "pursuing-stacks/build.py",
                    "pursuing-stacks/check.py", source_path, manifest["reproduction"]}
        require(required <= set(names), "incomplete reproducible source package")
        require(manifest["complete_editable_body"] == source_path, "wrong source-package body")
        require(archive.read(source_path) == source, "direct/archived source mismatch")


def check_module(read, prefix):
    folder = "pursuing-stacks/"
    record = json.loads(read(folder + prefix + "integration.json"))
    release = json.loads(read(folder + prefix + "release.json"))
    require(record["status"] == "VALIDATED_STANDALONE_MODULE" and not record["whole_handoff_integrated"], "invalid module scope")
    source = read(folder + safe(record["source"]["path"]))
    bound(source, record["source"])
    mapping = read(folder + record.get("source_map_path", "source-map.json"))
    require(sha(mapping) == record["source_map_sha256"], "source map changed")
    tex = source.decode("utf-8")
    labels = re.findall(r"\\label\{([^}]+)\}", tex)
    refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", tex)
    require(labels == record["labels"] and len(labels) == len(set(labels)) and set(refs) <= set(labels), "module reference closure")
    require(len(re.findall(r"\\begin\{(?:proposition|lemma)\}", tex)) == tex.count(r"\begin{proof}") == record["proof_bearing_statements"], "statement/proof count")
    require(not re.search(r"\\(?:input|include|includegraphics|bibliography)\b", tex), "undeclared external document input")
    rows = release["files_in_reading_order"]
    require(len(rows) == 3 and [PurePosixPath(r["path"]).suffix for r in rows] == [".pdf", ".tex", ".zip"], "PDF/source/ZIP order")
    assets = [read(folder + safe(row["path"])) for row in rows]
    for data, row in zip(assets, rows):
        bound(data, row)
    require(assets[1] == source, "release source mismatch")
    check_package(assets[2], folder + record["source"]["path"], source)
    build = json.loads(read(folder + record["build_receipt"]))
    visual = json.loads(read(folder + record["visual_receipt"]))
    bound(source, build["source"])
    bound(assets[0], build["pdf"])
    bound(assets[0], visual["pdf"])
    require(len(build["fresh_builds"]) == 2 and build["fresh_builds"][0]["identities"] == build["fresh_builds"][1]["identities"], "fresh builds differ")
    require(build["fresh_builds"][0]["identities"]["pdf"] == sha(assets[0]), "build PDF vector mismatch")
    require(visual["status"] == release["all_page_visual_qa"] == "PASS", "visual QA not passed")
    from pypdf import PdfReader
    pages = len(PdfReader(io.BytesIO(assets[0])).pages)
    require(pages == visual["page_count"] == record["pdf_pages"], "PDF page-count mismatch")
    require([p["page"] for p in visual["pages"]] == list(range(1, pages + 1)), "incomplete all-page QA")
    return {"module": record["source"]["path"], "pages": pages, "statements": record["proof_bearing_statements"]}


def check_head(ref="HEAD"):
    require(git("rev-parse", CORE + "^{tree}").decode().strip() == CORE_TREE, "wrong frozen core tree")
    git("merge-base", "--is-ancestor", CORE, NOTES)
    git("merge-base", "--is-ancestor", NOTES, ref)
    # These older EGA comparison notes are merely preserved, not revised or
    # accepted as new source. Their content remains bound to the old commit.
    notes_paths = git("diff-tree", "-r", "--no-commit-id", "--name-only", CORE, NOTES).decode().splitlines()
    frozen_notes = set(notes_paths) - DOCS
    require(all(p.startswith("ega/coverage/") and p.endswith((".md", ".json"))
                or p == "ai-integrated/review-notes/2026-09-19-proposed-corrections.json" for p in frozen_notes), "unexpected historical note scope")
    read = lambda name: git("show", ref + ":" + safe(name))
    for name in frozen_notes:
        require(read(name) == git("show", NOTES + ":" + name), "older comparison evidence changed: " + name)
    fixes = json.loads(read("possible-fixes/manifest.json"))
    patch_paths = set()
    for row in fixes["patches"]:
        name = "possible-fixes/" + safe(row["file"])
        require(PurePosixPath(row["file"]).name == row["file"] and name.endswith(".patch"), "unsafe patch filename")
        bound(read(name), row)
        patch_paths.add(name)
    require(sha(read(fixes["evidence"])) == fixes["evidence_sha256"], "fix evidence changed")
    export_paths = set()
    export_exists = subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", ref + ":upstream-corrections/downloads.json"], capture_output=True)
    if export_exists.returncode == 0:
        downloads = json.loads(read("upstream-corrections/downloads.json"))
        for row in downloads["files"]:
            name = safe(row["path"])
            require(name in {"README.md", "REVIEW.md", "COPYING", "manifest.json", "ALL-TEXTUAL-CORRECTIONS.patch", "corrections-only.zip"}
                    or re.fullmatch(r"chapters/[a-z0-9-]+\.patch", name)
                    or re.fullmatch(r"reviews/[a-z0-9-]+\.md", name), "unexpected correction export path")
            name = "upstream-corrections/" + name
            require(name not in export_paths, "duplicate correction download")
            bound(read(name), row)
            export_paths.add(name)
        export_paths.add("upstream-corrections/downloads.json")
    allowed = DOCS | NEW_TOOLS | frozen_notes | patch_paths | export_paths | {
        "possible-fixes/README.md", "possible-fixes/manifest.json"} | {"pursuing-stacks/" + p for p in MODULE_FILES}
    changes = [line.split("\t", 1) for line in git("diff-tree", "-r", "--no-commit-id", "--name-status", CORE, ref).decode().splitlines()]
    check_changes(changes, allowed)
    for _, name in changes:
        mode = git("ls-tree", ref, "--", name).decode().split()[0]
        require(mode == "100644", "non-regular supplement file")
    modules = [check_module(read, "")]
    exists = subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", ref + ":pursuing-stacks/intervals-release.json"], capture_output=True)
    if exists.returncode == 0:
        modules.append(check_module(read, "intervals-"))
    return modules


def verify_frozen_core():
    # One disposable checkout of this repository, not a workspace scan or TeX
    # build. Never change the user's worktree, index, or uncommitted sources.
    with tempfile.TemporaryDirectory(prefix="stacks-sealed-core-") as tmp:
        parent = Path(tmp).resolve()
        checkout = parent / "core"
        require(checkout.resolve().parent == parent, "unsafe temporary checkout")
        git("-c", "core.autocrlf=false", "worktree", "add", "--detach", str(checkout), CORE)
        try:
            subprocess.run([sys.executable, "tools/validate_unified_repository.py", "--pre-publication"],
                           cwd=checkout, check=True, timeout=900)
        finally:
            require(checkout.resolve().parent == parent and parent.name.startswith("stacks-sealed-core-"), "unsafe temporary removal")
            git("worktree", "remove", "--force", str(checkout))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-frozen-core", action="store_true")
    args = parser.parse_args()
    modules = check_head()
    if args.verify_frozen_core:
        verify_frozen_core()
    print(json.dumps({"status": "FROZEN_CORE_AND_SUPPLEMENTS_PASS" if args.verify_frozen_core else "SUPPLEMENTS_AND_CORE_IDENTITY_PASS",
                      "frozen_core": CORE, "prior_exact_head_ci": 34785240936, "modules": modules,
                      "cumulative_source_changed": False, "mathematical_certification": False}))


if __name__ == "__main__":
    main()
