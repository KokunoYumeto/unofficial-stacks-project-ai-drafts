#!/usr/bin/env python3
"""Validate a direct successor's committed full-build and publication evidence.

The current index is validation/direct-successor-current.json. Its schema is
unofficial-ai-integrated-stacks-direct-release-index/v1; references are exact
{path, bytes, sha256, git_blob} objects. Required references: composition,
build, second_build, visual_qa, reproducibility. All but composition name
distinct JSON files directly below validation/. Publication additionally
requires release. READY_FOR_PUBLICATION and PUBLICATION_COMPLETE are distinct
index states. --pre-publication validates every production gate except public
transport; it never emits PUBLICATION_COMPLETE. No TeX is launched here.

The release schema is unofficial-ai-integrated-stacks-direct-release/v1. It
binds the index's non-release references, content/validation commits, scope,
anonymous source readback, an exact-head successful GitHub workflow, and a
GitHub release asset inventory. The published assets must expose all built
PDFs, directly or through hash-bound ZIP members. Zenodo is not required for
each successor; sparse milestone publication remains a separate workflow.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile
from urllib.parse import quote
from urllib.request import Request, urlopen
import zipfile

SCHEMA = "unofficial-ai-integrated-stacks-direct-composition/v1"
AI_SCHEMA = "unofficial-ai-integrated-stacks-ai-source-correction-successor/v1"
AI_CHECKPOINT_SCHEMA = "unofficial-stacks-project-ai-drafts-ega-source-checkpoint-ai-source-correction-successor/v1"
AI_CHECKPOINT_STATUS = "PASS_SOURCE_CHECKPOINT_AI_SOURCE_CORRECTION_SUCCESSOR"
AI_TOOLS = ("tools/ai_source_correction_composition.py", "tools/cumulative_source.py",
            "tools/cumulative_reader.py", "tools/reconstruct_cumulative.py",
            "tools/cumulative-master.json", "tools/CUMULATIVE-RECONSTRUCTION.md",
            "tools/package_cumulative_successor.py", "tools/test_cumulative_packaging.py",
            "tools/test_ai_source_correction_consumers.py", "tools/test_ai_source_correction_composition.py",
            "tools/test_ai_source_correction_checkpoint.py", "tools/tests/test_compare_ai_source_correction.py",
            "tools/package_direct_successor_pdfs.py", "tools/tests/test_package_ai_source_correction.py")
INDEX_SCHEMA = "unofficial-ai-integrated-stacks-direct-release-index/v1"
RELEASE_SCHEMA = "unofficial-ai-integrated-stacks-direct-release/v1"
INDEX = "validation/direct-successor-current.json"
COMPOSITION = "validation/composition-current.json"
REPOSITORY = "KokunoYumeto/unofficial-stacks-project-ai-drafts"
REPOSITORY_ID = 1332406685
AUTHORITY = "a04446e57ec1fbc252a871afcec7752fb2807b14"
AUTHORITY_TREE = "3feeb703b931a6e7259782c10e7d1575adc83e5e"
REFERENCE_KEYS = {"path", "bytes", "sha256", "git_blob"}
CORE_ROLES = ("composition", "build", "second_build", "visual_qa", "reproducibility")
DIAGNOSTICS = ("fatal_markers", "missing_glyph_markers", "undefined_reference_markers",
               "external_reference_markers", "undefined_citation_markers", "multiply_defined_markers",
               "rerun_required_markers", "destination_warning_markers")
SUFFIXES = (".aux", ".bbl", ".idx", ".ind", ".lof", ".lot", ".out", ".toc", ".pdf")
VISUAL_TRUE = ("all_pages_rendered", "all_pages_manually_inspected",
               "all_manifest_bound_locus_pages_inspected_at_high_resolution", "page_dimensions_consistent",
               "headers_and_page_numbers_consistent", "text_and_formulas_legible", "diagrams_intact")
VISUAL_ZERO = ("clipped_content", "overlapping_content", "blank_pages", "corrupted_pages",
               "missing_or_unreadable_glyphs", "broken_diagrams")
TOOLS = ("tools/build_fixed_point.py", "tools/direct_successor_composition.py",
         "tools/direct_successor_common.py", "tools/write_direct_successor_receipt.py",
         "tools/validate_direct_successor_release.py", "tools/validate_unified_repository.py",
         "tools/compare_fixed_point_builds.py", "tools/compose_overlay_projection.py",
         "tools/verify_overlay_projection.py", "tools/direct_successor_checkpoint.py", "tools/tex_process_guard.py",
         "tools/tex_process_public_receipt.py")
DIRECT_PROTECTED_TOOLS = {"tools/direct_successor_common.py", "tools/direct_successor_composition.py",
                          "tools/write_direct_successor_receipt.py", "tools/validate_direct_successor_release.py",
                          "tools/direct_successor_checkpoint.py", "tools/tex_process_guard.py",
                          "tools/tex_process_public_receipt.py"}
SURFACE = ("README.md", "STATUS.md", "ROADMAP.md", "PROVENANCE.md", "VALIDATION.md",
           "CONTRIBUTING.md", "ai-integrated/README.md", "validation/README.md", "COPYING",
           ".github/workflows/validate.yml")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def exact(left, right):
    return json.dumps(left, sort_keys=True, allow_nan=False) == json.dumps(right, sort_keys=True, allow_nan=False)


def number(value, minimum=0):
    require(type(value) is int and value >= minimum, "invalid integer")
    return value


def digest(value):
    require(isinstance(value, str) and re.fullmatch(r"[0-9A-F]{64}", value), "invalid SHA-256")
    return value


def safe_path(value):
    require(isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9._/-]+", value)
            and not value.startswith("/") and all(p not in {"", ".", ".."} for p in value.split("/")),
            "unsafe relative path")
    return value


def parse_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result
    def constant(value):
        raise ValueError("non-finite JSON constant: " + value)
    result = json.loads(raw, object_pairs_hook=pairs, parse_constant=constant)
    require(isinstance(result, dict), "JSON document is not an object")
    return result


def identity(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest().upper(),
            "git_blob": hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()}


class Objects:
    """Exact Git-object reads and explicit bounded working-file checks."""
    def __init__(self, root):
        self.root = Path(root).resolve()

    def raw(self, *args, data=None):
        done = subprocess.run(["git", "-C", str(self.root), *args], input=data,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        require(done.returncode == 0, "Git object read failed: " + done.stderr.decode("utf-8", "replace"))
        return done.stdout

    def text(self, *args):
        return self.raw(*args).decode("utf-8").strip()

    def commit(self, value):
        require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value), "invalid exact commit")
        require(self.text("rev-parse", value + "^{commit}") == value, "missing commit")
        return value

    def tree(self, commit, expected):
        require(self.text("rev-parse", commit + "^{tree}") == expected, "tree identity mismatch")

    def linear(self, base, head):
        self.raw("merge-base", "--is-ancestor", base, head)
        cursor = base
        for commit in self.text("rev-list", "--reverse", base + ".." + head).splitlines():
            require(self.text("rev-list", "--parents", "-n", "1", commit).split()[1:] == [cursor],
                    "nonlinear publication lineage")
            cursor = commit
        require(cursor == head, "incomplete publication lineage")

    def blob(self, commit, path):
        return self.raw("cat-file", "blob", commit + ":" + safe_path(path))

    def ident(self, commit, path):
        return identity(self.blob(commit, path))

    def clean(self, path):
        path = safe_path(path)
        local = (self.root / path).resolve()
        require(local.is_relative_to(self.root), "working path escapes repository")
        data = local.read_bytes()
        expected = self.ident("HEAD", path)
        require(self.raw("hash-object", "--path=" + path, "--stdin", data=data).decode().strip()
                == expected["git_blob"], "working path differs from committed bytes: " + path)
        return self.blob("HEAD", path)

    def document(self, path):
        raw = self.clean(path)
        return parse_json(raw), raw

    def build_inputs(self, commit, stems):
        names = self.text("ls-tree", "--name-only", commit, "--").splitlines()
        return {"preamble.tex", "chapters.tex", "my.bib", *(stem + ".tex" for stem in stems),
                *(safe_path(path) for path in names if "/" not in path
                  and PurePosixPath(path).suffix.lower() in {".bst", ".cfg", ".cls", ".def", ".sty"})}


def reference(objects, row, role):
    require(isinstance(row, dict) and set(row) == REFERENCE_KEYS, "invalid reference: " + role)
    path = safe_path(row["path"])
    if role == "composition":
        require(path == COMPOSITION, "noncanonical composition reference")
    else:
        require(PurePosixPath(path).parent == PurePosixPath("validation")
                and re.fullmatch(r"direct-successor-[A-Za-z0-9._-]+\.json", PurePosixPath(path).name)
                and path not in {INDEX, COMPOSITION}, "receipt outside narrow validation namespace")
    raw = objects.clean(path)
    require(exact(identity(raw), {k: row[k] for k in ("bytes", "sha256", "git_blob")}),
            "committed reference identity mismatch: " + role)
    return parse_json(raw), raw


def validate_index(objects, requested, pre_publication):
    index, raw = objects.document(INDEX)
    require(index.get("schema") == INDEX_SCHEMA, "unsupported direct release index")
    require(index.get("status") in ({"READY_FOR_PUBLICATION", "PUBLICATION_COMPLETE"} if pre_publication
                                     else {"PUBLICATION_COMPLETE"}), "direct index is not ready")
    refs = index.get("references")
    roles = set(CORE_ROLES) | ({"release"} if index["status"] == "PUBLICATION_COMPLETE" else set())
    require(isinstance(refs, dict) and set(refs) == roles, "incomplete direct index references")
    documents = {role: reference(objects, refs[role], role) for role in roles}
    require(len({row["path"] for row in refs.values()}) == len(refs), "aliased receipt roles")
    require(requested == refs["build"]["path"], "build argument differs from current direct index")
    return index, raw, documents


def tuple_hash(artifacts):
    lines = ["|".join(str(row[k]) for k in ("stem", "pages", "bytes", "sha256"))
             for row in sorted(artifacts, key=lambda row: row["stem"])]
    return hashlib.sha256(("\n".join(lines) + "\n").encode()).hexdigest().upper()


def correction_scope(binding):
    """New scope is explicit; old v1 never silently acquires AI-correction fields."""
    if binding.get("schema") == SCHEMA:
        require("ai_source_correction_scope" not in binding and "correction_protected_inputs" not in binding,
                "old direct composition cannot carry an untyped AI correction")
        return None
    require(binding.get("schema") == AI_SCHEMA, "unsupported composition variant")
    from ai_source_correction_composition import validate_ai_source_correction_scope
    scope = binding.get("ai_source_correction_scope")
    validate_ai_source_correction_scope(scope, source_commit=binding["composition_source_commit"],
                                       source_tree=binding["composition_source_tree"])
    return scope


def correction_inputs(binding):
    if correction_scope(binding) is None:
        return {}
    rows = binding.get("correction_protected_inputs")
    require(isinstance(rows, dict) and rows, "missing correction protected-input closure")
    for path, row in rows.items():
        safe_path(path)
        require(isinstance(row, dict) and set(row) in ({"bytes", "sha256", "git_blob"}, REFERENCE_KEYS),
                "untyped correction protected-input identity")
        if "path" in row:
            require(row["path"] == path, "correction protected-input path mismatch")
        number(row["bytes"]); digest(row["sha256"])
        require(isinstance(row["git_blob"], str) and re.fullmatch(r"[0-9a-f]{40}", row["git_blob"]),
                "invalid correction protected Git blob")
    return rows


def scoped_tools(binding):
    return TOOLS + (AI_TOOLS if correction_scope(binding) is not None else ())


def index_composition_scope(binding):
    scope = {"source_commit": binding["composition_source_commit"],
             "registry_cutoff_commit": binding["registry_cutoff_commit"], "new_overlay_ids": binding["new_overlay_ids"]}
    correction = correction_scope(binding)
    if correction is not None:
        scope["ai_source_correction"] = correction
    return scope


def release_core_readback_paths(binding, refs):
    return ({row["path"] for row in refs.values()} | set(scoped_tools(binding))
            | set(SURFACE) | set(correction_inputs(binding)))


def validate_public_readback_inventory(readback, required, content_head):
    require(readback.get("status") == "PASS" and readback.get("anonymous") is True
            and readback.get("commit") == content_head, "public source readback not complete")
    rows = readback.get("checked_paths")
    require(isinstance(rows, list) and all(isinstance(row, dict) and set(row) == REFERENCE_KEYS for row in rows),
            "invalid public path inventory")
    names = [safe_path(row["path"]) for row in rows]
    require(len(names) == len(set(names)) and required <= set(names), "public readback omits required or repeats paths")
    return rows


def validate_correction_build_binding(receipt, binding, stems):
    correction = correction_scope(binding)
    if correction is None:
        return
    require(len(stems) == 36 and {"schemes", "groupoids", "spaces-perfect", "simplicial"} <= set(stems),
            "AI correction requires all 36 cumulative chapters")
    source = receipt.get("source", {})
    require(source.get("commit") != correction["sealed_predecessor_commit"], "old R48 A/B cannot certify the AI correction")
    checkpoint = receipt.get("source_checkpoint", {})
    require(checkpoint.get("schema") == AI_CHECKPOINT_SCHEMA and checkpoint.get("status") == AI_CHECKPOINT_STATUS
            and exact(checkpoint.get("ai_source_correction"), correction), "missing current AI-correction checkpoint")


def check_build_shape(receipt, binding, stems, mutex_validator):
    require(receipt.get("schema") == "unofficial-ai-integrated-stacks-fixed-point-build/v1"
            and receipt.get("status") == "PASS", "build is not a passing full fixed-point run")
    require(exact(receipt.get("composition"), binding), "build direct-composition binding mismatch")
    validate_correction_build_binding(receipt, binding, stems)
    require(receipt.get("pdfs_committed") is False, "build PDFs must be release assets")
    require(isinstance(receipt.get("environment"), dict) and receipt["environment"], "missing build environment")
    build = receipt.get("build")
    require(isinstance(build, dict), "missing build state")
    expected = {"strategy": "sequential-prime-bibtex-global-state-sweeps", "fixed_point_suffixes": list(SUFFIXES),
                "stem_selection": "composition_receipt", "stems": list(stems), "chapter_count": len(stems),
                "pdfinfo_readable": len(stems), "worktree_kind": "linked", "primary_worktree_override": False}
    require(all(exact(build.get(k), value) for k, value in expected.items()), "build profile/strategy/isolation mismatch")
    require(2 <= number(build.get("global_fixed_point_sweep"), 2) <= 6, "invalid fixed-point sweep")
    errors = []
    mutex_validator(build.get("machine_wide_tex_mutex"), "direct build", errors)
    require(not errors, "; ".join(errors))
    diagnostics = build.get("diagnostics")
    require(isinstance(diagnostics, dict) and set(diagnostics) == set(DIAGNOSTICS), "incomplete build diagnostics")
    for key, value in diagnostics.items():
        number(value)
        require(key == "external_reference_markers" or value == 0, "nonzero build diagnostic: " + key)
    artifacts = receipt.get("artifacts")
    require(isinstance(artifacts, list) and all(isinstance(row, dict) for row in artifacts)
            and [row.get("stem") for row in artifacts] == list(stems), "artifact coverage/order mismatch")
    totals = {key: 0 for key in DIAGNOSTICS}
    for row in artifacts:
        number(row.get("pages"), 1); number(row.get("bytes"), 1); digest(row.get("sha256"))
        counts = row.get("diagnostics")
        require(isinstance(counts, dict) and set(counts) == set(DIAGNOSTICS), "artifact diagnostics incomplete")
        for key, value in counts.items():
            totals[key] += number(value)
        external = row.get("external_references")
        require(isinstance(external, dict) and type(external.get("count")) is int
                and external["count"] == counts["external_reference_markers"], "external-reference count mismatch")
        digest(external.get("sha256"))
    require(exact(totals, diagnostics), "aggregate diagnostic totals mismatch")
    require(build.get("artifact_tuple_set_sha256") == tuple_hash(artifacts), "artifact tuple hash mismatch")
    return artifacts


def validate_process_tree(objects, receipt, commit, capture_validator):
    from tex_process_public_receipt import canonical_public_capture_bytes, public_capture_time
    tree = receipt.get("tex_process_tree")
    require(isinstance(tree, dict) and set(tree) == {"schema", "guard", "launch_count", "launches"}
            and tree.get("schema") == "unofficial-ai-integrated-stacks-tex-process-tree-build/v1",
            "missing typed TeX process-tree evidence")
    guard = tree.get("guard")
    require(isinstance(guard, dict) and set(guard) == REFERENCE_KEYS and guard.get("path") == "tools/tex_process_guard.py",
            "missing exact process-tree guard identity")
    expected = objects.ident(commit, guard["path"])
    require(exact({k: guard[k] for k in REFERENCE_KEYS - {"path"}}, expected)
            and expected == objects.ident("HEAD", guard["path"]), "TeX process guard identity mismatch")
    launches = tree.get("launches")
    minimum = len(receipt["build"]["stems"]) * (2 + receipt["build"]["global_fixed_point_sweep"]) + 2
    require(isinstance(launches, list) and number(tree.get("launch_count"), minimum) == len(launches),
            "process-tree launch inventory too short or inconsistent")
    mutex = receipt["build"]["machine_wide_tex_mutex"]
    acquired = public_capture_time(mutex["acquired_utc"])
    released = public_capture_time(mutex["released_utc"])
    names, hashes, private_hashes, root_identities = [], [], [], []
    for row in launches:
        require(isinstance(row, dict) and set(row) == {"path", "bytes", "sha256", "raw_text", "receipt"},
                "incomplete process-tree launch evidence")
        require(isinstance(row["path"], str)
                and re.fullmatch(r"tex-process-tree/launch-[0-9]{6}\.json", row["path"])
                and int(row["path"][-11:-5]) > 0, "process capture path is not a neutral public identifier")
        names.append(row["path"])
        # raw_text is the exact serialized PUBLIC projection, never private capture
        # JSON. The typed pure validator below rejects private fields recursively.
        require(isinstance(row["raw_text"], str), "public process receipt lacks exact UTF-8 text")
        data = row["raw_text"].encode("utf-8")
        observed = identity(data)
        require(number(row["bytes"], 1) == observed["bytes"] and digest(row["sha256"]) == observed["sha256"]
                and exact(parse_json(data), row["receipt"]), "process capture raw identity mismatch")
        hashes.append(row["sha256"])
        capture_validator(row["receipt"])
        require(data == canonical_public_capture_bytes(row["receipt"]), "noncanonical public process capture JSON")
        lifecycle = row["receipt"]["lifecycle"]
        require(acquired <= public_capture_time(lifecycle["started_utc"])
                <= public_capture_time(lifecycle["finished_utc"]) <= released,
                "process capture is outside its owning build mutex interval")
        private_hashes.append(row["receipt"]["provenance"]["private_capture"]["sha256"])
        root = lifecycle["root_identity"]
        root_identities.append((root["pid"], root["creation_filetime_100ns"]))
    require(all(len(values) == len(set(values)) for values in (names, hashes, private_hashes, root_identities)),
            "duplicate process capture evidence")


def validate_build(objects, receipt, binding, stems, mutex_validator, checkpoint_validator, checkpoint_replay, capture_validator):
    artifacts = check_build_shape(receipt, binding, stems, mutex_validator)
    source = receipt.get("source")
    require(isinstance(source, dict) and set(source) == {"commit", "tree"}, "invalid build source")
    commit = objects.commit(source["commit"])
    objects.tree(commit, source["tree"])
    validate_process_tree(objects, receipt, commit, capture_validator)
    objects.linear(binding["composition_source_commit"], commit)
    objects.linear(commit, objects.text("rev-parse", "HEAD"))
    protected = {COMPOSITION: {"sha256": binding["receipt_sha256"], "git_blob": binding["receipt_git_blob"]}}
    for name in ("overlays", "leases"):
        protected[binding[f"registry_{name}_path"]] = {
            "sha256": binding[f"registry_{name}_sha256"], "git_blob": binding[f"registry_{name}_git_blob"]}
    require(objects.build_inputs(commit, stems) == objects.build_inputs("HEAD", stems), "build-critical input scope changed")
    for path in objects.build_inputs(commit, stems):
        protected[path] = objects.ident("HEAD", path)
    tools = binding.get("direct_validation_tools")
    required_tools = DIRECT_PROTECTED_TOOLS | (set(AI_TOOLS) if correction_scope(binding) is not None else set())
    require(isinstance(tools, dict) and required_tools <= set(tools),
            "direct validation-tool inventory incomplete")
    protected.update(tools)
    protected.update(correction_inputs(binding))
    protected.update({path: objects.ident("HEAD", path) for path in scoped_tools(binding)})
    for path, expected in protected.items():
        observed = objects.ident(commit, path)
        require(all(exact(observed.get(k), value) for k, value in expected.items() if k != "path"),
                "build-source protected input mismatch: " + path)
    builder = receipt.get("builder")
    require(isinstance(builder, dict) and builder.get("path") == "tools/build_fixed_point.py", "invalid builder binding")
    observed = objects.ident(commit, builder["path"])
    require(builder.get("git_blob") == observed["git_blob"] and builder.get("sha256") == observed["sha256"],
            "builder identity mismatch")
    # The existing comparator validates the full typed EGA checkpoint shape;
    # additionally bind its actual canonical receipt bytes at this build source.
    checkpoint_validator(receipt, "direct build")
    checkpoint = receipt["source_checkpoint"]
    ref = checkpoint.get("receipt")
    require(isinstance(ref, dict), "checkpoint lacks canonical receipt identity")
    path = safe_path(ref.get("path"))
    require(path == "validation/ega-i-6.6.4-source-checkpoint-2026-08-31.json", "noncanonical EGA checkpoint")
    expected = objects.ident(commit, path)
    require(all(exact(ref.get(k), value) for k, value in expected.items()), "EGA checkpoint byte binding mismatch")
    require(objects.ident("HEAD", path) == expected, "canonical EGA checkpoint changed after build")
    require("schemes" in stems, "full build omits canonical EGA checkpoint chapter")
    actual_checkpoint = checkpoint_replay(objects.root, Path(path), binding, commit)
    require(exact(actual_checkpoint, checkpoint), "exact-build-head EGA checkpoint replay mismatch")
    return artifacts


def validate_visual(visual, build_ref, build, artifacts, affected):
    require(visual.get("schema") == "unofficial-ai-integrated-stacks-visual-qa/v1"
            and visual.get("status") == "PASS", "visual QA not PASS")
    require(exact(visual.get("source"), build["source"]), "visual source mismatch")
    expected_build = {k: build_ref[k] for k in ("path", "bytes", "sha256")}
    expected_build.update(status="PASS", global_fixed_point_sweep=build["build"]["global_fixed_point_sweep"])
    require(exact(visual.get("build_receipt"), expected_build), "visual build reference mismatch")
    by_stem = {row["stem"]: row for row in artifacts}
    scope = visual.get("scope", {})
    correction = correction_scope(build["composition"])
    if correction is not None:
        require(len(affected) == 3 and set(affected) == {"groupoids", "spaces-perfect", "simplicial"},
                "AI-correction visual union mismatch")
        require(exact(scope.get("ai_source_correction"), correction), "visual correction scope mismatch")
    require(scope.get("affected_chapters") == list(affected), "visual affected scope mismatch")
    pages = sum(by_stem[stem]["pages"] for stem in affected)
    require(type(scope.get("full_page_render_count")) is int and scope["full_page_render_count"] == pages
            and type(scope.get("full_page_contact_sheet_review_count")) is int
            and scope["full_page_contact_sheet_review_count"] == pages, "visual full-page coverage mismatch")
    locus = scope.get("high_resolution_locus_pages")
    require(isinstance(locus, dict) and set(locus) == set(affected), "visual locus coverage mismatch")
    for stem, values in locus.items():
        require(isinstance(values, list) and values and all(type(p) is int and 1 <= p <= by_stem[stem]["pages"] for p in values)
                and values == sorted(set(values)), "invalid visual locus pages")
    if correction is not None:
        validate_correction_visual_loci(visual, build, by_stem, locus)
    require(number(scope.get("high_resolution_locus_page_count"), 1) == sum(map(len, locus.values())),
            "visual locus count mismatch")
    output = visual.get("artifacts")
    require(isinstance(output, dict) and set(output) == set(affected), "visual artifact scope mismatch")
    for stem, row in output.items():
        require(isinstance(row, dict) and all(exact(row.get(k), by_stem[stem][k]) for k in ("pages", "bytes", "sha256"))
                and row.get("pdf") == stem + ".pdf" and row.get("encrypted") is False,
                "visual PDF identity mismatch")
        require(number(row.get("pages_without_ink")) == 0 and number(row.get("duplicate_render_hashes")) == 0,
                "visual render defect")
    checks = visual.get("checks", {})
    require(all(checks.get(key) is True for key in VISUAL_TRUE), "visual inspection check missing")
    require(all(number(checks.get(key)) == 0 for key in VISUAL_ZERO), "visual defect count nonzero")
    protocol = visual.get("render_protocol", {})
    require("Poppler" in str(protocol.get("renderer", "")) and number(protocol.get("full_page_dpi"), 72) >= 72
            and number(protocol.get("high_resolution_dpi"), 144) >= 144
            and protocol.get("render_intermediates_published") is False, "invalid visual render protocol")


def validate_correction_visual_loci(visual, build, artifact_by_stem, locus_pages):
    expected = build["composition"].get("correction_visual_units")
    required_units = {"eilenberg-zilber-and-grading", "i1.4-localization"}
    require(isinstance(expected, list) and len(expected) == 2
            and {row.get("unit_id") for row in expected} == required_units, "correction visual-unit inventory missing")
    record = visual.get("ai_correction_loci")
    require(isinstance(record, dict)
            and record.get("schema") == "unofficial-ai-integrated-stacks-ai-correction-visual-loci/v1"
            and exact(record.get("source"), build["source"])
            and record.get("mapping_method") == "exact-current-source-interval-to-final-pdf"
            and record.get("inspection_performed") is True, "actual correction-locus visual mapping missing")
    require(exact(record.get("pdf"), {"path": "simplicial.pdf", **{
        key: artifact_by_stem["simplicial"][key] for key in ("bytes", "sha256", "pages")}}),
        "correction-locus PDF differs from current Simplicial build")
    rows = record.get("units")
    require(isinstance(rows, list) and len(rows) == 2 and {row.get("unit_id") for row in rows} == required_units,
            "correction-locus unit coverage mismatch")
    by_id = {row["unit_id"]: row for row in expected}
    keys = {"unit_id", "source", "start_byte", "end_byte_exclusive", "sha256"}
    for row in rows:
        require(set(row) == keys | {"pages"} and exact({key: row[key] for key in keys}, by_id[row["unit_id"]]),
                "correction-locus source interval differs from reviewed manifest")
        require(row["source"] == "simplicial.tex", "wrong correction locus source")
        pages = row.get("pages")
        require(isinstance(pages, list) and pages and pages == sorted(set(pages))
                and all(type(page) is int and page in locus_pages["simplicial"] for page in pages),
                "corrected unit pages are absent from high-resolution inspection")


def validate_repro(repro, first_ref, second_ref, first, second, artifacts, binding, comparator):
    comparator(first, second)  # Validates both mutexes and both mandatory EGA checkpoint bindings.
    first_captures = {row["receipt"]["provenance"]["private_capture"]["sha256"]
                      for row in first["tex_process_tree"]["launches"]}
    second_captures = {row["receipt"]["provenance"]["private_capture"]["sha256"]
                       for row in second["tex_process_tree"]["launches"]}
    require(first_captures.isdisjoint(second_captures), "reproducibility reuses process-capture evidence")
    def roots(build):
        return {(row["receipt"]["lifecycle"]["root_identity"]["pid"],
                 row["receipt"]["lifecycle"]["root_identity"]["creation_filetime_100ns"])
                for row in build["tex_process_tree"]["launches"]}
    require(roots(first).isdisjoint(roots(second)), "reproducibility reuses captured root identity")
    require(repro.get("schema") == "unofficial-ai-integrated-stacks-clean-build-reproducibility/v1"
            and repro.get("status") == "PASS", "reproducibility not PASS")
    require(all(exact(repro.get(k), first[k]) for k in ("source", "builder", "environment")), "reproducibility identity mismatch")
    ids = [{k: row[k] for k in ("stem", "pages", "bytes", "sha256")} for row in artifacts]
    require(exact(repro.get("artifacts"), ids), "reproducibility artifact mismatch")
    last = binding["last_admitted_overlay"]
    match = re.fullmatch(r"stacks-errata-a04446e-r([1-9][0-9]*)", last)
    require(match is not None, "unsupported direct errata cutoff")
    expected_scope = {"admitted_errata": "R1-R" + match.group(1), "registry_cutoff_commit": binding["registry_cutoff_commit"],
                      "source_commit": first["source"]["commit"], "source_tree": first["source"]["tree"],
                      "composition_receipt": COMPOSITION, "composition_receipt_sha256": binding["receipt_sha256"]}
    correction = correction_scope(binding)
    if correction is not None:
        expected_scope["ai_source_correction"] = correction
    require(exact(repro.get("scope"), expected_scope), "reproducibility scope mismatch")
    method = {"execution_model": "independent_linked_worktrees", "first_worktree_kind": "linked", "second_worktree_kind": "linked",
              "builder_path": first["builder"]["path"], "builder_git_blob": first["builder"]["git_blob"],
              "builder_sha256": first["builder"]["sha256"]}
    require(exact(repro.get("method"), method), "reproducibility method mismatch")
    runs = repro.get("runs", {})
    require(set(runs) == {"first", "second"}, "reproducibility run inventory mismatch")
    for role, ref, receipt in (("first", first_ref, first), ("second", second_ref, second)):
        expected = {"receipt": ref["path"], "bytes": ref["bytes"], "sha256": ref["sha256"], "status": "PASS",
                    "created_utc": receipt["created_utc"], "global_fixed_point_sweep": receipt["build"]["global_fixed_point_sweep"]}
        require(exact(runs[role], expected), "reproducibility run binding mismatch")
    comparison = {"chapter_count": len(artifacts), "matched_artifact_count": len(artifacts), "different_artifact_count": 0,
                  "different_artifacts": [], "total_pages_each_run": sum(row["pages"] for row in artifacts),
                  "total_pdf_bytes_each_run": sum(row["bytes"] for row in artifacts), "artifact_tuple_set_sha256_each_run": tuple_hash(artifacts),
                  "all_artifact_identities_exactly_equal": True, "source_identity_equal": True, "builder_identity_equal": True,
                  "environment_identity_equal": True, "fixed_point_sweep_equal": True, "source_checkpoint_identity_equal": True}
    require(exact(repro.get("comparison"), comparison), "reproducibility comparison mismatch")


def public_json(url):
    request = Request(url, headers={"User-Agent": "Stacks-draft-public-byte-validator", "Accept": "application/vnd.github+json"})
    with urlopen(request, timeout=60) as response:
        raw = response.read(8 * 1024 * 1024 + 1)
    require(len(raw) <= 8 * 1024 * 1024, "public JSON exceeds bounded size")
    return parse_json(raw)


def public_object(url, expected, inspect=None):
    """Stream exactly the declared bytes; optional ZIP inspection uses bounded RAM."""
    number(expected.get("bytes"), 1); digest(expected.get("sha256"))
    count, hasher = 0, hashlib.sha256()
    with tempfile.SpooledTemporaryFile(max_size=8 * 1024 * 1024) as saved:
        with urlopen(Request(url, headers={"User-Agent": "Stacks-draft-public-byte-validator"}), timeout=60) as response:
            while True:
                data = response.read(min(1024 * 1024, expected["bytes"] - count + 1))
                if not data:
                    break
                count += len(data)
                require(count <= expected["bytes"], "public object exceeds bound byte count")
                hasher.update(data)
                if inspect is not None:
                    saved.write(data)
        require(count == expected["bytes"] and hasher.hexdigest().upper() == expected["sha256"], "public object byte identity mismatch")
        if inspect is not None:
            saved.seek(0)
            inspect(saved)


def check_zip_pdfs(handle, members, artifact_by_stem):
    with zipfile.ZipFile(handle) as archive:
        names = archive.namelist()
        require(len(names) == len(set(names)), "duplicate ZIP members")
        for name in names:
            safe_path(name.rstrip("/"))
        for name, stem in members.items():
            info = archive.getinfo(safe_path(name))
            expected = artifact_by_stem[stem]
            require(not info.flag_bits & 1 and info.file_size == expected["bytes"], "encrypted or incorrectly sized PDF member")
            hasher, count = hashlib.sha256(), 0
            with archive.open(info) as stream:
                while True:
                    data = stream.read(min(1024 * 1024, expected["bytes"] - count + 1))
                    if not data:
                        break
                    count += len(data); require(count <= expected["bytes"], "ZIP PDF exceeds byte bound"); hasher.update(data)
            require(count == expected["bytes"] and hasher.hexdigest().upper() == expected["sha256"], "ZIP PDF identity mismatch")


def validate_cumulative_reader_descriptor(row, artifacts):
    require(row.get("name") == "01-cumulative-reader.pdf" and row.get("role") == "cumulative_reader",
            "first release asset must be the cumulative reader PDF")
    info = row.get("cumulative_reader")
    require(isinstance(info, dict) and info.get("scope") == "36-chapter cumulative release, not the full Stacks Project"
            and info.get("chapter_count") == len(artifacts) == 36, "cumulative reader scope mismatch")
    chapters = info.get("chapters")
    require(isinstance(chapters, list) and len(chapters) == len(artifacts), "cumulative chapter inventory incomplete")
    next_page = 1
    for chapter, artifact in zip(chapters, artifacts):
        require(chapter.get("stem") == artifact["stem"] and isinstance(chapter.get("title"), str)
                and chapter["title"].strip(), "cumulative chapter identity/order mismatch")
        require(chapter.get("start_page") == next_page and chapter.get("pages") == artifact["pages"]
                and chapter.get("end_page") == next_page + artifact["pages"] - 1,
                "cumulative chapter range incomplete or overlapping")
        require(exact(chapter.get("source_pdf"), {k: artifact[k] for k in ("bytes", "sha256")}),
                "cumulative chapter differs from verified build PDF")
        next_page += artifact["pages"]
    require(type(info.get("total_pages")) is int and info["total_pages"] == next_page - 1,
            "cumulative reader total mismatch")
    return info


def check_cumulative_reader(handle, info):
    from pypdf import PdfReader
    reader = PdfReader(handle)
    require(not reader.is_encrypted and len(reader.pages) == info["total_pages"],
            "public cumulative reader is encrypted or has the wrong page count")
    require(all(float(page.mediabox.width) > 0 and float(page.mediabox.height) > 0 for page in reader.pages),
            "cumulative reader has invalid page geometry")


def validate_source_archive_descriptor(objects, row, content_head, stems, build_source_commit):
    require(row.get("name") == "02-full-cumulative-editable-source.zip"
            and row.get("role") == "full_cumulative_editable_source",
            "second release asset must be the full cumulative editable-source ZIP")
    descriptor = row.get("source_archive")
    require(isinstance(descriptor, dict) and set(descriptor) == {"source_inventory", "metadata_member"}
            and descriptor["metadata_member"] == "SOURCE-INVENTORY.json", "invalid native-source archive descriptor")
    reference = descriptor["source_inventory"]
    require(isinstance(reference, dict) and set(reference) == REFERENCE_KEYS | {"commit"},
            "native-source inventory lacks exact committed identity")
    path = safe_path(reference["path"])
    inventory_commit = objects.commit(reference["commit"])
    objects.linear(inventory_commit, content_head)
    expected = {key: reference[key] for key in REFERENCE_KEYS - {"path"}}
    require(exact(objects.ident(inventory_commit, path), expected)
            and exact(objects.ident(content_head, path), expected),
            "native-source inventory commit/content identity drift")
    raw = objects.blob(content_head, path)
    inventory = parse_json(raw)
    require(inventory.get("schema") == "native-cumulative-source-inventory/v1"
            and inventory.get("authority_commit") == AUTHORITY
            and inventory.get("chapter_stems") == list(stems), "native-source inventory scope mismatch")
    source_commit = objects.commit(inventory.get("source_commit"))
    require(source_commit == build_source_commit, "native source does not match exact fresh build source")
    objects.linear(source_commit, content_head)
    # The package module owns the deterministic source-closure policy; its pure
    # verifier must derive required Git paths, not trust a checked=true flag.
    from cumulative_source import expected_source_members
    require(exact(inventory.get("closure"), {"policy": "all-committed-native-inputs-plus-build-support", "checked": True}),
            "native-source inventory closure policy mismatch")
    members = inventory.get("members")
    require(isinstance(members, list) and members, "empty cumulative native-source archive")
    names = []
    for member in members:
        require(isinstance(member, dict) and set(member) == {"archive_path", "git_commit", "git_path", "git_blob", "bytes", "sha256"},
                "untyped native-source member")
        name, git_path = safe_path(member["archive_path"]), safe_path(member["git_path"])
        names.append(name)
        revision = objects.commit(member["git_commit"])
        require(revision in {source_commit, AUTHORITY}, "native-source member outside declared source/authority revisions")
        require(name == ("baseline/" if revision == AUTHORITY else "current/") + git_path,
                "native source and printed witness are not separated by exact paths")
        require(exact(objects.ident(revision, git_path), {key: member[key] for key in ("bytes", "sha256", "git_blob")}),
                "native-source member Git identity mismatch")
        if revision == source_commit:
            require(objects.ident(content_head, git_path) == objects.ident(source_commit, git_path),
                    "native source changed before publication")
    require(len(names) == len(set(names)) and descriptor["metadata_member"] not in names,
            "duplicate native-source members")
    expected_members = expected_source_members(objects.root, source_commit, AUTHORITY, list(stems))
    require(isinstance(expected_members, dict)
            and exact({row["archive_path"]: row for row in members}, expected_members),
            "native-source inventory does not equal recomputed cumulative source closure")
    require(inventory.get("master_path") == "current/tools/cumulative-master.json"
            and inventory["master_path"] in expected_members,
            "cumulative editable master is absent")
    return inventory, raw, path


def check_native_source_zip(handle, inventory, inventory_raw):
    with zipfile.ZipFile(handle) as archive:
        names = archive.namelist()
        by_name = {member["archive_path"]: member for member in inventory["members"]}
        require(len(names) == len(set(names)) and set(names) == set(by_name) | {"SOURCE-INVENTORY.json"},
                "native-source ZIP member inventory incomplete or unexpected")
        metadata = archive.getinfo("SOURCE-INVENTORY.json")
        require(not metadata.flag_bits & 1 and metadata.file_size == len(inventory_raw),
                "native-source ZIP inventory member size/encryption mismatch")
        require(archive.read(metadata) == inventory_raw, "native-source ZIP embedded inventory differs")
        for name, expected in by_name.items():
            info = archive.getinfo(name)
            require(not info.is_dir() and not info.flag_bits & 1 and info.file_size == expected["bytes"],
                    "native-source ZIP member type/size/encryption mismatch")
            count, hasher = 0, hashlib.sha256()
            with archive.open(info) as stream:
                while True:
                    data = stream.read(min(1024 * 1024, expected["bytes"] - count + 1))
                    if not data:
                        break
                    count += len(data)
                    require(count <= expected["bytes"], "native-source member exceeds declared bound")
                    hasher.update(data)
            require(count == expected["bytes"] and hasher.hexdigest().upper() == expected["sha256"],
                    "native-source ZIP member byte identity mismatch")


def validate_release(objects, release, index, documents, binding, artifacts):
    require(release.get("schema") == RELEASE_SCHEMA and release.get("status") == "PUBLICATION_COMPLETE", "direct release is not complete")
    require(release.get("repository") == REPOSITORY and release.get("default_branch") == "main", "wrong public destination")
    refs = {role: index["references"][role] for role in CORE_ROLES}
    require(exact(release.get("receipts"), refs), "release receipt-reference mismatch")
    scope = {"new_overlay_ids": binding["new_overlay_ids"], "registry_cutoff_commit": binding["registry_cutoff_commit"],
             "registered_overlays": binding["registered_overlays"], "registered_stable_ids": binding["registered_stable_ids"],
             "composition_source_commit": binding["composition_source_commit"]}
    correction = correction_scope(binding)
    if correction is not None:
        scope["ai_source_correction"] = correction
    require(exact(release.get("scope"), scope), "release scope mismatch")
    content, validation = release.get("content", {}), release.get("validation_head", {})
    content_head, validation_head = objects.commit(content.get("commit")), objects.commit(validation.get("commit"))
    objects.tree(content_head, content.get("tree")); objects.tree(validation_head, validation.get("tree"))
    objects.linear(binding["composition_source_commit"], content_head); objects.linear(content_head, validation_head)
    head = objects.text("rev-parse", "HEAD"); objects.linear(validation_head, head)
    required = release_core_readback_paths(binding, refs)
    packaging = None
    if correction is not None:
        packaged_assets = release.get("github_release", {}).get("assets")
        require(isinstance(packaged_assets, list) and len(packaged_assets) >= 2,
                "cumulative PDF/source release assets missing")
        reader_descriptor = validate_cumulative_reader_descriptor(packaged_assets[0], artifacts)
        source_inventory, source_inventory_raw, source_inventory_path = validate_source_archive_descriptor(
            objects, packaged_assets[1], content_head, binding["required_build_stems"],
            documents["build"][0]["source"]["commit"])
        required.add(source_inventory_path)
        packaging = (reader_descriptor, source_inventory, source_inventory_raw)
    required.update(objects.build_inputs(content_head, binding["required_build_stems"]))
    required.add("validation/ega-i-6.6.4-source-checkpoint-2026-08-31.json")
    required.update(binding[f"registry_{name}_path"] for name in ("overlays", "leases"))
    for overlay in binding["new_overlays"]:
        directory = safe_path(overlay["namespace_path"])
        required.update({directory + "/candidate.manifest.json", directory + "/source-map.jsonl", directory + "/operation-spec.json"})
        admission = overlay.get("admission_receipt", {})
        required.add(safe_path(admission.get("path")))
        # Include every declared candidate reference, not just the review filename.
        manifest = parse_json(objects.blob(content_head, directory + "/candidate.manifest.json"))
        def walk(node):
            if isinstance(node, dict):
                if "path" in node:
                    required.add(directory + "/" + safe_path(node["path"]))
                for value in node.values():
                    walk(value)
            elif isinstance(node, list):
                for value in node:
                    walk(value)
        walk(manifest)
    readback = release.get("public_readback", {})
    rows = validate_public_readback_inventory(readback, required, content_head)
    for row in rows:
        path = row["path"]
        require(exact(objects.ident(content_head, path), {k: row[k] for k in REFERENCE_KEYS - {"path"}}), "readback local identity mismatch")
        require(objects.ident("HEAD", path) == objects.ident(content_head, path)
                == objects.ident(validation_head, path), "release content changed across CI validation lineage")
        public_object(f"https://raw.githubusercontent.com/{REPOSITORY}/{content_head}/{quote(path, safe='/')}", row)
    require(number(readback.get("checked_file_count")) == len(rows)
            and number(readback.get("checked_total_bytes")) == sum(row["bytes"] for row in rows), "public readback total mismatch")
    # The successful CI head is explicit; later receipt-only commits are not
    # dishonestly labelled as having run that workflow themselves.
    workflow = release.get("workflow", {})
    run_id = number(workflow.get("run_id"), 1)
    expected_url = f"https://github.com/{REPOSITORY}/actions/runs/{run_id}"
    require(workflow.get("name") == "Unified repository validation" and workflow.get("head_sha") == validation_head
            and workflow.get("status") == "completed" and workflow.get("conclusion") == "success"
            and workflow.get("url") == expected_url, "exact-head workflow record mismatch")
    remote_run = public_json(f"https://api.github.com/repos/{REPOSITORY}/actions/runs/{run_id}")
    require(remote_run.get("id") == run_id and remote_run.get("head_sha") == validation_head
            and remote_run.get("name") == workflow["name"] and remote_run.get("status") == "completed"
            and remote_run.get("conclusion") == "success" and remote_run.get("html_url") == expected_url
            and remote_run.get("repository", {}).get("id") == REPOSITORY_ID
            and remote_run.get("path") == ".github/workflows/validate.yml", "live workflow verification mismatch")
    ci_index = parse_json(objects.blob(validation_head, INDEX))
    require(ci_index.get("schema") == INDEX_SCHEMA and ci_index.get("status") == "READY_FOR_PUBLICATION"
            and exact(ci_index.get("references"), refs)
            and exact(ci_index.get("composition_scope"), index.get("composition_scope")),
            "CI did not validate the exact ready index and receipt set")
    github = release.get("github_release", {})
    tag = github.get("tag")
    require(isinstance(tag, str) and re.fullmatch(r"[A-Za-z0-9._-]+", tag), "invalid release tag")
    remote_release = public_json(f"https://api.github.com/repos/{REPOSITORY}/releases/tags/{quote(tag, safe='')}")
    require(remote_release.get("draft") is False and remote_release.get("tag_name") == tag
            and remote_release.get("id") == number(github.get("id"), 1), "release is not the public bound release")
    require(objects.text("rev-parse", f"refs/tags/{tag}^{{commit}}") == content_head, "release tag content mismatch")
    public_tag = public_json(f"https://api.github.com/repos/{REPOSITORY}/git/ref/tags/{quote(tag, safe='')}").get("object", {})
    for _ in range(4):
        if public_tag.get("type") == "commit":
            break
        require(public_tag.get("type") == "tag" and re.fullmatch(r"[0-9a-f]{40}", str(public_tag.get("sha"))),
                "unsupported public annotated-tag object")
        public_tag = public_json(f"https://api.github.com/repos/{REPOSITORY}/git/tags/{public_tag['sha']}").get("object", {})
    require(public_tag.get("type") == "commit" and public_tag.get("sha") == content_head, "public tag points to different content")
    assets, remote_assets = github.get("assets"), remote_release.get("assets")
    require(isinstance(assets, list) and assets and isinstance(remote_assets, list), "missing public release assets")
    require(len(assets) == len(remote_assets), "release asset inventory count mismatch")
    if correction is not None:
        required_order = ["01-cumulative-reader.pdf", "02-full-cumulative-editable-source.zip"]
        require([row.get("name") for row in assets[:2]] == required_order
                and [row.get("name") for row in remote_assets[:2]] == required_order,
                "public release file list does not put cumulative reader first and full source second")
        body = remote_release.get("body")
        require(isinstance(body, str), "public release lacks human-readable ordered downloads")
        links = [f"https://github.com/{REPOSITORY}/releases/download/{quote(tag, safe='')}/{name}"
                 for name in required_order]
        require(all(link in body for link in links) and body.index(links[0]) < body.index(links[1]),
                "public release download links omit/reverse cumulative PDF and full source")
    seen, pdf_stems = set(), []
    by_stem = {row["stem"]: row for row in artifacts}
    for row in assets:
        name = safe_path(row.get("name")); require("/" not in name and name not in seen, "unsafe or duplicate release asset")
        seen.add(name)
        matches = [item for item in remote_assets if item.get("name") == name]
        require(len(matches) == 1, "missing or duplicate remote asset")
        remote = matches[0]
        url = f"https://github.com/{REPOSITORY}/releases/download/{quote(tag, safe='')}/{quote(name, safe='')}"
        require(remote.get("browser_download_url") == url and remote.get("size") == number(row.get("bytes"), 1)
                and remote.get("state") == "uploaded", "remote asset inventory mismatch")
        digest(row.get("sha256"))
        members = row.get("pdf_members", {})
        require(isinstance(members, dict) and all(isinstance(stem, str) and stem in by_stem for stem in members.values()), "invalid PDF-member map")
        if row.get("pdf_stem") is not None:
            stem = row["pdf_stem"]
            require(stem in by_stem and name == stem + ".pdf" and not members
                    and all(exact(row.get(k), by_stem[stem][k]) for k in ("bytes", "sha256")), "direct PDF asset identity mismatch")
            pdf_stems.append(stem)
        if members:
            require(name.endswith(".zip"), "PDF members require ZIP asset")
            pdf_stems.extend(members.values())
        inspect = (lambda handle, m=members: check_zip_pdfs(handle, m, by_stem)) if members else None
        if correction is not None and name == "01-cumulative-reader.pdf":
            require(not members and row.get("pdf_stem") is None, "cumulative reader confused with individual PDF")
            inspect = lambda handle: check_cumulative_reader(handle, packaging[0])
        if correction is not None and name == "02-full-cumulative-editable-source.zip":
            require(not members and row.get("pdf_stem") is None, "editable-source ZIP confused with PDF ZIP")
            inspect = lambda handle: check_native_source_zip(handle, packaging[1], packaging[2])
        public_object(url, row, inspect)
    require(set(pdf_stems) == set(by_stem), "published PDF coverage is incomplete")
    repository = public_json(f"https://api.github.com/repos/{REPOSITORY}")
    require(repository.get("id") == REPOSITORY_ID and repository.get("private") is False
            and repository.get("default_branch") == "main", "repository public-access state mismatch")
    remote_head = public_json(f"https://api.github.com/repos/{REPOSITORY}/git/ref/heads/main")
    require(remote_head.get("object", {}).get("sha") == head, "validated HEAD is not public main")
    # These two files close the release after the content commit; they cannot
    # contain their own future commit/hash. Verify them live at final HEAD.
    for path in (INDEX, index["references"]["release"]["path"]):
        public_object(f"https://raw.githubusercontent.com/{REPOSITORY}/{head}/{quote(path, safe='/')}",
                      objects.ident(head, path))


def validate_direct_release(root, build_path, pre_publication=False):
    """Return a CLI-compatible status; no TeX, builds, or mutation are performed."""
    try:
        from direct_successor_composition import load_direct_composition, recheck_direct_validation_tools
        from direct_successor_checkpoint import validate_direct_source_checkpoint_at
        from validate_unified_repository import validate_machine_wide_tex_mutex
        from compare_fixed_point_builds import compare_receipts, validate_source_checkpoint
        from tex_process_public_receipt import validate_public_capture_receipt
        root = Path(root).resolve(); objects = Objects(root)
        requested = Path(build_path)
        requested = requested.resolve().relative_to(root).as_posix() if requested.is_absolute() else requested.as_posix()
        initial = objects.text("rev-parse", "HEAD")
        index, index_raw, documents = validate_index(objects, safe_path(requested), pre_publication)
        composition_schema = documents["composition"][0].get("schema")
        if composition_schema == AI_SCHEMA:
            from ai_source_correction_composition import load_ai_source_correction, recheck_ai_source_correction_tools
            binding, stems, affected = load_ai_source_correction(root, Path(COMPOSITION))
            recheck_composition = recheck_ai_source_correction_tools
        else:
            require(composition_schema == SCHEMA, "unsupported direct composition variant")
            binding, stems, affected = load_direct_composition(root, Path(COMPOSITION))
            recheck_composition = recheck_direct_validation_tools
        require(binding.get("schema") == composition_schema and binding.get("authority_commit") == AUTHORITY
                and binding.get("authority_tree") == AUTHORITY_TREE, "unsupported direct composition authority/schema")
        require(exact(index.get("composition_scope"), index_composition_scope(binding)),
                "direct index composition scope mismatch")
        require(documents["composition"][0].get("schema") == binding["schema"], "index references different composition variant")
        first, second = documents["build"][0], documents["second_build"][0]
        artifacts = validate_build(objects, first, binding, stems, validate_machine_wide_tex_mutex,
                                   validate_source_checkpoint, validate_direct_source_checkpoint_at, validate_public_capture_receipt)
        validate_build(objects, second, binding, stems, validate_machine_wide_tex_mutex,
                       validate_source_checkpoint, validate_direct_source_checkpoint_at, validate_public_capture_receipt)
        validate_visual(documents["visual_qa"][0], index["references"]["build"], first, artifacts, affected)
        validate_repro(documents["reproducibility"][0], index["references"]["build"], index["references"]["second_build"],
                       first, second, artifacts, binding, compare_receipts)
        for path in (*scoped_tools(binding), *SURFACE, *correction_inputs(binding)):
            objects.clean(path)
        if not pre_publication:
            validate_release(objects, documents["release"][0], index, documents, binding, artifacts)
        require(objects.text("rev-parse", "HEAD") == initial and objects.clean(INDEX) == index_raw, "validation inputs moved")
        for role, ref in index["references"].items():
            reference(objects, ref, role)
        recheck_composition(root, binding)
    except (OSError, ValueError, KeyError, TypeError, AttributeError, ImportError, RuntimeError,
            subprocess.SubprocessError, zipfile.BadZipFile) as exc:
        print("Direct successor release validation: FAIL\n- " + str(exc), file=sys.stderr)
        return 1
    print("Direct successor release validation: " + ("PASS_PRE_PUBLICATION" if pre_publication else "PUBLICATION_COMPLETE"))
    print(f"- full-profile chapters: {len(stems)}; affected chapters visually checked: {len(affected)}")
    print(f"- exact reproducible PDF identities: {len(artifacts)}; public readback checked: {not pre_publication}")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--build-receipt", type=Path, required=True)
    parser.add_argument("--pre-publication", action="store_true")
    args = parser.parse_args()
    return validate_direct_release(args.root, args.build_receipt, args.pre_publication)


if __name__ == "__main__":
    raise SystemExit(main())
