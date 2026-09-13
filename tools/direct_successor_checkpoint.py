"""Typed current and exact-revision EGA binding for direct registry successors.

Historical producer bytes and receipt topology remain authoritative. The new
source endpoint is checked separately; the inherited semantic increment is
validated against its own original cumulative source commit.
"""
from __future__ import annotations

from collections import Counter
from contextlib import contextmanager
import os
from pathlib import Path
import subprocess
import sys
import tempfile

if __package__:
    from . import direct_successor_composition
    from . import verify_ega_checkpoint_successor as historical
else:
    import direct_successor_composition
    import verify_ega_checkpoint_successor as historical

DIRECT_SCHEMA = direct_successor_composition.SCHEMA
DIRECT_TOOLS = direct_successor_composition.DIRECT_TOOLS
SCHEMA = "unofficial-stacks-project-ai-drafts-ega-source-checkpoint-direct-successor/v1"
STATUS = "PASS_SOURCE_CHECKPOINT_DIRECT_SUCCESSOR"
AI_COMPOSITION_SCHEMA = "unofficial-ai-integrated-stacks-ai-source-correction-successor/v1"
SCHEMA_AI = "unofficial-stacks-project-ai-drafts-ega-source-checkpoint-ai-source-correction-successor/v1"
STATUS_AI = "PASS_SOURCE_CHECKPOINT_AI_SOURCE_CORRECTION_SUCCESSOR"
require = historical.require
SEMANTIC_PATH = historical.SEMANTIC_PATH
SEMANTIC_PATHS = historical.SEMANTIC_PATHS
PROTECTED_SEMANTIC_PATHS = historical.PROTECTED_SEMANTIC_PATHS
THIS_TOOL, THIS_TEST = historical.THIS_TOOL, historical.THIS_TEST
receipt_anchor = historical.receipt_anchor
verify_historical = historical.verify_historical
verify_semantic = historical.verify_semantic
CURRENT_EGA_VALIDATION_PATH = "validation/ega-i-7.4.1-7.4.7-integration-validation-2026-09-09.json"
SEMANTIC_JOIN_SCHEMA = "unofficial-stacks-project-ai-drafts-historical-current-ega-join/v1"


@contextmanager
def isolated_checker_import_cache():
    """Avoid stale imported pyc bytes without deleting any existing cache."""
    keys = ("PYTHONPYCACHEPREFIX", "PYTHONDONTWRITEBYTECODE")
    previous = {key: os.environ.get(key) for key in keys}
    with tempfile.TemporaryDirectory(prefix="stacks-ega-checker-cache-") as empty:
        os.environ["PYTHONPYCACHEPREFIX"] = empty
        os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
        try:
            yield
        finally:
            for key, value in previous.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value


def ega_dependency_paths(build, source, revision):
    """Closed bounded committed scope consumed by the EGA checkers.

    Includes nested review crops, source slices and helper tests/receipts read by
    the current EGA contracts. It does not inspect untracked workspace files.
    """
    paths = set()
    for directory in ("ega", "reports"):
        paths.update(build.git(source, "ls-tree", "-r", "--name-only", revision, "--", directory).splitlines())
    for directory in ("validation", "tools", "tests"):
        for path in build.git(source, "ls-tree", "-r", "--name-only", revision, "--", directory).splitlines():
            name = Path(path).name
            if (directory == "validation" and name.startswith("ega-") and name.endswith(".json")
                or directory == "tools" and name.endswith(".py") and
                    (name.startswith("ega_") or name.startswith("check_ega_"))
                or directory == "tests" and name.startswith("test_ega_") and name.endswith(".py")):
                paths.add(path)
    require({"ega/check.py", "ega/intake.py", "ega/map.py", SEMANTIC_PATH,
             "reports/findings.jsonl", "reports/qsrc.csv"}.issubset(paths),
            "EGA checker dependency inventory is incomplete")
    return sorted(paths)


def require_exact_inputs(build, source, revision, paths):
    rows = []
    for path in paths:
        expected = build.committed_file_identity(source, revision, path)
        require(expected is not None, f"committed EGA checker input missing: {path}")
        build.require_clean_path(source, path)
        actual = build.working_file_identity(source, path)
        require(all(actual[k] == expected[k] for k in ("bytes", "sha256")),
                f"EGA checker working input differs: {path}")
        rows.append(expected)
    return rows


def semantic_input_paths(build, source, anchor):
    paths = set(ega_dependency_paths(build, source, anchor))
    paths.update(p for p in build.git(source, "ls-tree", "--name-only", anchor).splitlines()
                 if "/" not in p and (p.endswith(".tex") or Path(p).suffix.lower() in build.EGA_SHARED_BUILD_SUFFIXES))
    paths.update(("tags/tags", "my.bib"))
    return sorted(paths)


def semantic_worktree(build, source, anchor, paths):
    """Materialize a separate exact semantic head; never reset any existing tree."""
    target = source.parent / f"{source.name}-ega665-semantic-{anchor[:12]}"
    require(target.parent.resolve() == source.parent.resolve() and not target.is_symlink()
            and not (hasattr(target, "is_junction") and target.is_junction()),
            "semantic validation worktree escapes its bounded target")
    if target.exists():
        require((target / ".git").is_file()
                and Path(build.git(target, "rev-parse", "--show-toplevel")).resolve() == target.resolve(),
                "existing semantic target is not its own linked worktree")
        require(build.git(target, "rev-parse", "HEAD") == anchor,
                "semantic validation worktree moved; refusing to reset")
        require(build.resolved_git_path(target, build.git(target, "rev-parse", "--git-common-dir"))
                == build.resolved_git_path(source, build.git(source, "rev-parse", "--git-common-dir")),
                "semantic worktree belongs to another repository")
        return target
    historical.raw_git(source, "worktree", "add", "--detach", "--no-checkout", str(target), anchor)
    root_inputs = [p for p in build.git(source, "ls-tree", "--name-only", anchor).splitlines()
                   if "/" not in p and (p.endswith(".tex") or Path(p).suffix.lower() in build.EGA_SHARED_BUILD_SUFFIXES)]
    selected = sorted(set(paths) | set(root_inputs) | {"tags/tags", "my.bib"})
    require(all(build.require_safe_posix_path(p, "semantic materialization path") == p for p in selected),
            "unsafe semantic materialization path")
    patterns = ("\n".join("/" + p for p in selected) + "\n").encode()
    historical.raw_git(target, "-c", "core.autocrlf=false", "sparse-checkout", "set", "--no-cone", "--stdin",
                       input_bytes=patterns)
    historical.raw_git(target, "-c", "core.autocrlf=false", "read-tree", "-mu", anchor)
    require(build.git(target, "rev-parse", "HEAD") == anchor, "semantic materialization changed HEAD")
    return target


def verify_historical_semantic(build, source, prior, head, composition):
    anchor = build.git(source, "log", "-1", "--first-parent", "--format=%H", prior, "--", SEMANTIC_PATH)
    anchor = build.require_commit_object(source, anchor, "actual EGA semantic receipt head")
    build.require_ancestor(source, anchor, "historical semantic to previous public", prior)
    receipt = build.committed_file_identity(source, anchor, SEMANTIC_PATH)
    require(receipt is not None and receipt == build.committed_file_identity(source, prior, SEMANTIC_PATH)
            == build.committed_file_identity(source, head, SEMANTIC_PATH),
            "historical semantic receipt was rewritten after its own head")
    paths = semantic_input_paths(build, source, anchor)
    target = semantic_worktree(build, source, anchor, paths)
    before = require_exact_inputs(build, target, anchor, paths)
    with isolated_checker_import_cache():
        semantic, semantic_paths = verify_semantic(build, target, anchor, composition)
    require(semantic.get("commit") == anchor and semantic.get("receipt") == receipt,
            "historical semantic verifier did not validate its actual own head")
    require(before == require_exact_inputs(build, target, anchor, paths)
            and build.git(target, "rev-parse", "HEAD") == anchor,
            "historical semantic inputs changed during validation")
    protected = [build.protected_input("historical_checkpoint_input", anchor, row) for row in before]
    return {**semantic, "validated_at_own_head": True, "fresh_import_cache": True,
            "checker_input_count": len(before),
            "checker_input_tuple_sha256": build.canonical_tuple_sha256(protected)}, semantic_paths, protected


def verify_current_ega(build, source, prior, head):
    paths = ega_dependency_paths(build, source, prior)
    require(paths == ega_dependency_paths(build, source, head), "inherited current EGA input inventory changed")
    for path in paths:
        require(build.committed_file_identity(source, prior, path)
                == build.committed_file_identity(source, head, path),
                f"inherited current EGA input drifted: {path}")
    before = require_exact_inputs(build, source, head, paths)
    validation_id = build.committed_file_identity(source, prior, CURRENT_EGA_VALIDATION_PATH)
    require(validation_id is not None, "current EGA integration evidence is absent")
    validation = build.parse_json_blob(source, validation_id, "already-public EGA integration")
    require(validation.get("schema") == "ega-i74-root-integration-validation/v1"
            and validation.get("status") == "PASS", "unsupported current EGA validation contract")
    integrated = build.require_commit_object(source, validation.get("integrated_source_commit"), "current EGA integration")
    build.require_ancestor(source, integrated, "current EGA integration to previous public", prior)
    candidate_files = validation.get("candidate_files")
    require(isinstance(candidate_files, list) and candidate_files
            and len({row.get("path") for row in candidate_files}) == len(candidate_files),
            "current EGA integration candidate inventory is empty or duplicated")
    for row in candidate_files:
        path = build.require_safe_posix_path(row.get("path"), "EGA integration candidate path")
        require(path in paths, "current EGA validation candidate lies outside dependency closure")
        actual = build.committed_file_identity(source, prior, path)
        require(actual is not None and all(actual[k] == row.get(k) for k in ("bytes", "sha256")),
                f"current EGA integration candidate binding mismatch: {path}")
    gates = [row for row in validation.get("gates", []) if row.get("stage") == "ega_checker"]
    require(len(gates) == 1 and gates[0].get("exit_code") == 0 and isinstance(gates[0].get("output"), str),
            "current EGA validation lacks one passing checker gate")
    expected = build.strict_json_loads(gates[0]["output"], "already-public EGA checker result")
    require(isinstance(expected, dict) and expected.get("schema") == "ega-stacks-scaffold-check-v1"
            and expected.get("status") == "PASS" and expected.get("errors") == [],
            "current EGA sealed checker result is invalid")
    with isolated_checker_import_cache():
        check = subprocess.run([sys.executable, "-X", "utf8", "-B", "ega/check.py"], cwd=source,
                               capture_output=True, text=True, encoding="utf-8", timeout=600)
    require(check.returncode == 0, "current inherited EGA checker failed: " + (check.stderr or check.stdout))
    observed = build.strict_json_loads(check.stdout, "current inherited EGA checker")
    require(observed == expected, "current EGA checker differs from already-public integration result")
    require(before == require_exact_inputs(build, source, head, paths), "current EGA inputs changed during checker")
    return {"schema": SEMANTIC_JOIN_SCHEMA, "status": "PASS_CURRENT_PUBLIC_EGA_PRESERVED",
            "previous_public_commit": prior, "current_commit": head,
            "integration_receipt": validation_id, "integration_source_commit": integrated,
            "checker": observed, "fresh_import_cache": True, "input_count": len(before),
            "input_tuple_sha256": build.canonical_tuple_sha256([
                build.protected_input("successor_current_input", head, row) for row in before]),
            "historical_semantic_receipt_not_relabelled": True}, paths


def _recheck_at(build, source, binding, protected):
    """Revalidate an actual old build revision without substituting current HEAD."""
    head = binding["post_content"]["head_commit"]
    require(build.git(source, "rev-parse", head + "^{tree}") == binding["post_content"]["head_tree"],
            "exact checkpoint revision tree drift")
    for row in protected:
        expected = {key: row[key] for key in ("path", "bytes", "sha256", "git_blob")}
        require(build.committed_file_identity(source, row["commit"], row["path"]) == expected,
                "protected exact-revision input identity mismatch")
        if row["role"] not in build.EGA_NON_WORKTREE_PROTECTED_ROLES:
            require(build.committed_file_identity(source, head, row["path"]) == expected,
                    "protected input is not bound to actual build revision")
            build.require_clean_path(source, row["path"])
            actual = build.working_file_identity(source, row["path"])
            require(all(actual[key] == row[key] for key in ("bytes", "sha256")),
                    "working verifier input differs from actual build revision")
    for row in binding["external_authority_inputs"]:
        if (source / row["path"]).exists():
            actual = build.working_file_identity(source, row["path"])
            require(all(actual[key] == row[key] for key in ("bytes", "sha256")),
                    "external checkpoint authority changed")


def load_direct_source_checkpoint(build, source, logical, checkpoint, composition):
    head, _ = build.capture_source_revision(source)
    return _load_at(build, source, logical, checkpoint, composition, head, live=True)


def validate_direct_source_checkpoint_at(root, checkpoint_path, composition_binding, build_commit):
    if __package__:
        from . import build_fixed_point as build
    else:
        import build_fixed_point as build
    source = Path(root).resolve()
    logical = Path(checkpoint_path).as_posix()
    require(logical == build.EGA_SOURCE_CHECKPOINT_PATH, "noncanonical source checkpoint path")
    identity = build.committed_file_identity(source, build_commit, logical)
    require(identity is not None, "source checkpoint absent at actual build revision")
    checkpoint = build.parse_json_blob(source, identity, "exact-revision EGA checkpoint")
    require(isinstance(checkpoint, dict) and set(checkpoint) == build.EGA_CHECKPOINT_KEYS
            and checkpoint.get("schema") == build.EGA_SOURCE_CHECKPOINT_SCHEMA
            and checkpoint.get("status") == build.EGA_SOURCE_CHECKPOINT_STATUS,
            "invalid original checkpoint producer schema")
    binding, _, _ = _load_at(build, source, logical, checkpoint, composition_binding,
                            build_commit, live=False)
    return binding


def verify_current_illusie(build, source, composition, head):
    """Bind actual reviewed proof evidence plus current finite/mechanical checks."""
    if __package__:
        from . import ai_source_correction_composition as correction
    else:
        import ai_source_correction_composition as correction
    scope = composition.get("ai_source_correction_scope")
    correction.validate_ai_source_correction_scope(scope,
        source_commit=composition["composition_source_commit"], source_tree=composition["composition_source_tree"])
    protected = composition.get("correction_protected_inputs")
    require(isinstance(protected, dict) and {correction.MANIFEST, "simplicial.tex", "illusie_volume_I/verify.py",
            "illusie_volume_I/test_composition.py", "illusie_volume_I/test_ez.py"} <= set(protected),
            "current Illusie protected dossier is incomplete")
    require(protected[correction.MANIFEST] == {k: scope["manifest"][k] for k in correction.ID_KEYS},
            "current Illusie scope/manifest identity mismatch")
    for path, expected in protected.items():
        actual = build.committed_file_identity(source, head, path)
        require(actual is not None and {key: actual[key] for key in correction.ID_KEYS} == expected,
                f"current Illusie dossier identity mismatch: {path}")
    before = require_exact_inputs(build, source, head, sorted(protected))
    git = correction.Git(source)
    manifest = git.document(head, correction.MANIFEST)
    # Recompute exact candidate/source replay and review closure at this build head.
    correction.validate_manifest(git, manifest, head)
    checker = build.committed_file_identity(source, head, "illusie_volume_I/verify.py")
    with isolated_checker_import_cache():
        run = subprocess.run([sys.executable, "-X", "utf8", "-B", "illusie_volume_I/verify.py"], cwd=source,
                             capture_output=True, text=True, encoding="utf-8", timeout=120)
        require(run.returncode == 0, "current Illusie mechanical check failed: " + (run.stderr or run.stdout))
        result = build.strict_json_loads(run.stdout, "current Illusie mechanical check")
        require(isinstance(result, dict) and result.get("status") == "PASS"
                and result.get("current_source_sha256") == protected["simplicial.tex"]["sha256"],
                "current Illusie checker source binding mismatch")
        modules = ["illusie_volume_I.test_composition", "illusie_volume_I.test_ez"]
        tests = subprocess.run([sys.executable, "-X", "utf8", "-B", "-m", "unittest", *modules], cwd=source,
                               capture_output=True, text=True, encoding="utf-8", timeout=120)
        import re
        require(tests.returncode == 0 and re.search(r"Ran 5 tests? in ", tests.stderr)
                and re.search(r"\nOK\s*$", tests.stderr), "current Illusie five finite regression tests failed")
    require(before == require_exact_inputs(build, source, head, sorted(protected)), "Illusie inputs changed during validation")
    return {"schema": "unofficial-stacks-project-ai-drafts-current-illusie-correction-binding/v1",
            "status": "PASS_CURRENT_ILLUSIE_CORRECTION_BOUND", "current_commit": head,
            "composition_source_commit": composition["composition_source_commit"],
            "composition_source_tree": composition["composition_source_tree"], "scope": scope,
            "review": manifest["independent_review"], "checker": checker, "checker_result": result,
            "regression_tests": {"status": "PASS", "tests_run": 5, "modules": modules}}


def _load_at(build, source: Path, logical: str, checkpoint: dict, composition: dict, head: str, *, live: bool):
    head = build.require_commit_object(source, head, "direct checkpoint actual revision")
    tree = build.git(source, "rev-parse", f"{head}^{{tree}}")
    is_ai = composition.get("schema") == AI_COMPOSITION_SCHEMA
    require(composition.get("schema") in {DIRECT_SCHEMA, AI_COMPOSITION_SCHEMA},
            "direct checkpoint requires typed direct composition")
    require(build.committed_file_identity(source, head, SEMANTIC_PATH) is not None,
            "post-content receipt topology requires a supported committed semantic successor")
    content = build.require_commit_object(source, checkpoint["content"]["commit"], "EGA historical content")
    anchor = receipt_anchor(build, source, content, head, logical)
    build.require_ancestor(source, anchor, "historical checkpoint to previous public source",
                           composition["previous_public_main_head"])
    historical, old_protected = verify_historical(build, source, anchor)
    for path in ("schemes.tex", "tags/tags"):
        require(build.committed_file_identity(source, anchor, path)
                == build.committed_file_identity(source, head, path),
                f"historical EGA root proof or official tag surface changed: {path}")
    root_names = build.git(source, "ls-tree", "--name-only", head).splitlines()
    root_tex = [p for p in root_names if "/" not in p and p.endswith(".tex")]
    source_commit = composition["composition_source_commit"]
    source_roots = [p for p in build.git(source, "ls-tree", "--name-only", source_commit).splitlines()
                    if "/" not in p and p.endswith(".tex")]
    require(root_tex == source_roots, "root source inventory changed after composition")
    for path in root_tex:
        require(build.committed_file_identity(source, source_commit, path)
                == build.committed_file_identity(source, head, path),
                f"unvalidated post-composition root source change: {path}")
    prior = composition["previous_public_main_head"]
    inherited_id = build.committed_file_identity(source, prior, "validation/composition-current.json")
    require(inherited_id is not None, "direct checkpoint inherited composition is absent")
    inherited = build.parse_json_blob(source, inherited_id, "inherited actual composition")
    require(inherited.get("schema") in {direct_successor_composition._helper.SCHEMA, DIRECT_SCHEMA}
            and inherited.get("status") == "PASS" and isinstance(inherited.get("composition"), dict),
            "inherited composition is not a passing typed source binding")
    # The semantic increment belongs to its original cumulative source endpoint.
    # Never relabel it as a child of the new source-only composition commit.
    inherited_binding = {
        "composition_source_commit": inherited["composition"]["source_commit"],
        "composition_base_commit": inherited["composition"]["base_commit"],
    }
    for path in SEMANTIC_PATHS | set(PROTECTED_SEMANTIC_PATHS):
        require(build.committed_file_identity(source, prior, path)
                == build.committed_file_identity(source, head, path),
                f"inherited EGA semantic input drifted: {path}")
    semantic, semantic_paths, semantic_protected = verify_historical_semantic(
        build, source, prior, head, inherited_binding)
    current_ega, current_ega_paths = verify_current_ega(build, source, prior, head)
    current_illusie = verify_current_illusie(build, source, composition, head) if is_ai else None
    # Current inputs are frozen independently of the historical byte inventory.
    paths = set(root_tex + semantic_paths + [logical, "my.bib", "tags/tags",
                "validation/composition-current.json", THIS_TOOL, THIS_TEST])
    paths.update(path for path, _ in build.EGA_PRECONTENT_TOOL_ROLES)
    paths.update(DIRECT_TOOLS)
    if is_ai:
        paths.update(composition["correction_protected_inputs"])
        paths.update(composition["direct_validation_tools"])
    paths.update(current_ega_paths)
    paths.update(p for p in root_names if "/" not in p and Path(p).suffix.lower() in build.EGA_SHARED_BUILD_SUFFIXES)
    for directory in ("ega", "ai-integrated/registry"):
        paths.update(str(row["path"]) for row in build.committed_regular_files(source, head, directory))
    protected = []
    for row in old_protected:
        protected.append({**row, "role": "historical_checkpoint_input"})
    protected.extend(semantic_protected)
    for path in sorted(paths):
        identity = build.committed_file_identity(source, head, path)
        require(identity is not None, f"successor protected input is absent: {path}")
        build.require_clean_path(source, path)
        working = build.working_file_identity(source, path)
        require(all(working[k] == identity[k] for k in ("bytes", "sha256")),
                f"successor protected working bytes differ: {path}")
        protected.append(build.protected_input("successor_current_input", head, identity))
    protected.sort(key=lambda row: (str(row["role"]), str(row["path"]), str(row["commit"])))
    require(len({(r["commit"], r["path"]) for r in protected}) == len(protected),
            "duplicate successor protected input")
    binding = {
        "schema": SCHEMA_AI if is_ai else SCHEMA,
        "status": STATUS_AI if is_ai else STATUS,
        "receipt": build.committed_file_identity(source, head, logical),
        "historical_anchor": {"commit": anchor, "tree": historical["post_content"]["head_tree"],
                              "verification": historical},
        "semantic_successor": semantic, "current_ega_successor": current_ega,
        "inherited_composition": {"commit": prior, **inherited_id},
        "root_source_stem": "schemes",
        "canonical_composition": {
            "path": composition["receipt"], "git_blob": composition["receipt_git_blob"],
            "sha256": composition["receipt_sha256"], "composition_source_commit": source_commit,
            "composition_source_tree": composition["composition_source_tree"],
        },
        "post_content": {"head_commit": head, "head_tree": tree,
                         "source_paths_unchanged_since_composition": True},
        "protected_input_count": len(protected),
        "protected_input_roles": dict(sorted(Counter(r["role"] for r in protected).items())),
        "protected_input_tuple_sha256": build.canonical_tuple_sha256(protected),
        "external_authority_inputs": historical["external_authority_inputs"],
        "checks": ["original_producer_and_consumer_run_at_actual_historical_receipt_head",
                   "historical_tools_content_receipt_topology_preserved",
                   "historical_schemes_proof_and_tags_unchanged",
                   "all_current_root_tex_exact_at_validated_composition_source",
                   "semantic_increment_exact_append_prefixes_scope_and_checker",
                   "semantic_increment_checker_executed_at_its_actual_own_receipt_head",
                   "later_public_ega_inputs_preserved_and_current_checker_separately_replayed",
                   "historical_and_current_inputs_frozen_through_final_build_recheck"],
    }
    if is_ai:
        binding["ai_source_correction"] = composition["ai_source_correction_scope"]
        binding["current_illusie_successor"] = current_illusie
        binding["checks"].extend(["separate_AI_correction_exact_candidate_replay_and_review_closure",
                                  "current_Illusie_mechanical_checks_and_five_finite_regressions"])
    if live:
        build.require_source_checkpoint_unchanged(source, binding, tuple(protected))
    else:
        _recheck_at(build, source, binding, tuple(protected))
    return binding, tuple(sorted(paths)), tuple(protected)
