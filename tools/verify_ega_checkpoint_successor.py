"""Bind a later cumulative build without rewriting a historical EGA checkpoint.

The sealed producer is executed in a sparse, detached worktree at its actual
receipt commit. Its original HEAD/topology/byte checks are not emulated or
relaxed. The live source is then checked independently against its cumulative
composition and the separately committed semantic increment.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path


SEMANTIC_PATH = "validation/ega-i-6.6.5-semantic-checkpoint-2026-09-06.json"
SEMANTIC_PATHS = frozenset({
    SEMANTIC_PATH, "ega/README.md", "ega/agent.csv", "ega/check.py",
    "ega/dec.csv", "ega/log.md", "ega/resid.csv", "ega/scope.json", "ega/smap.csv",
})
PROTECTED_SEMANTIC_PATHS = (
    "ega/units.csv", "ega/files.csv", "ega/interface.json",
    "ega/publication-current.json", "ega/issues.csv", "ega/vqa.csv",
    "ega/rej.csv", "reports/qsrc.csv", "tags/tags",
)
THIS_TOOL = "tools/verify_ega_checkpoint_successor.py"
THIS_TEST = "tests/test_ega_checkpoint_successor.py"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def raw_git(source: Path, *args: str, input_bytes: bytes | None = None) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(source), *args], input=input_bytes,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120, check=False,
    )
    require(result.returncode == 0,
            f"historical checkpoint Git operation failed: {result.stderr.decode('utf-8', 'replace')}")
    return result.stdout


def receipt_anchor(build, source: Path, content: str, head: str, receipt: str) -> str:
    build.require_ancestor(source, content, "historical checkpoint content", head)
    suffix = build.git(source, "rev-list", "--first-parent", "--reverse",
                       f"{content}..{head}").splitlines()
    require(bool(suffix), "historical checkpoint has no committed receipt child")
    anchor = suffix[0]
    build.require_single_parent(source, anchor, "historical receipt", content)
    changes = build.committed_path_changes(source, content, anchor)
    require(list(changes) == [receipt] and changes[receipt][4] == "A",
            "historical receipt anchor is not the exact receipt-only child")
    require(build.committed_file_identity(source, anchor, receipt)
            == build.committed_file_identity(source, head, receipt),
            "sealed historical checkpoint was changed in the successor")
    return anchor


def historical_worktree(build, source: Path, anchor: str) -> Path:
    """Materialize only named historical validation inputs; never reset a tree."""
    target = source.parent / f"{source.name}-ega664-anchor-{anchor[:12]}"
    require(target.parent.resolve() == source.parent.resolve(),
            "historical validation worktree escapes the task parent")
    require(not target.is_symlink() and not (
        hasattr(target, "is_junction") and target.is_junction()),
        "historical validation target is a link or junction")
    if target.exists():
        require((target / ".git").is_file(), "existing historical target is not our linked worktree")
        require(Path(build.git(target, "rev-parse", "--show-toplevel")).resolve() == target.resolve(),
                "historical validation worktree root mismatch")
        require(build.git(target, "rev-parse", "HEAD") == anchor,
                "historical validation worktree moved; refusing to reset it")
        require(build.resolved_git_path(target, build.git(target, "rev-parse", "--git-common-dir"))
                == build.resolved_git_path(source, build.git(source, "rev-parse", "--git-common-dir")),
                "historical worktree belongs to another repository")
        return target
    raw_git(source, "worktree", "add", "--detach", "--no-checkout", str(target), anchor)
    # Root TeX/styles/bibliography plus the exact source-checkpoint dependencies.
    # Candidate payloads, PDFs, release bundles and unrelated dossiers are absent.
    patterns = ["/*", "!/*/", "/ega/", "/tags/", "/ai-integrated/registry/"]
    patterns += [f"/{path}" for path, _ in build.EGA_PRECONTENT_TOOL_ROLES]
    patterns += [f"/{path}" for path in (
        build.EGA_SOURCE_CHECKPOINT_PATH, build.EGA_IMPLEMENTATION_RECEIPT_PATH,
        build.EGA_INDEPENDENT_REVIEW_PATH, "validation/composition-current.json",
    )]
    raw_git(target, "-c", "core.autocrlf=false", "sparse-checkout", "set", "--no-cone", "--stdin",
            input_bytes=("\n".join(patterns) + "\n").encode())
    # --no-checkout deliberately starts with an empty index; setting sparse
    # patterns alone does not populate it on every supported Git version.
    raw_git(target, "-c", "core.autocrlf=false", "read-tree", "-mu", anchor)
    require(build.git(target, "rev-parse", "HEAD") == anchor,
            "historical materialization changed the anchor")
    return target


def verify_historical(build, source: Path, anchor: str):
    historical = historical_worktree(build, source, anchor)
    for path, _ in build.EGA_PRECONTENT_TOOL_ROLES:
        expected = build.committed_file_identity(source, anchor, path)
        require(expected is not None, f"historical executable is absent: {path}")
        build.require_clean_path(historical, path)
        working = build.working_file_identity(historical, path)
        require(all(working[key] == expected[key] for key in ("bytes", "sha256")),
                f"historical executable bytes changed before execution: {path}")
    module_path = historical / "tools/build_fixed_point.py"
    spec = importlib.util.spec_from_file_location("sealed_ega664_build_consumer", module_path)
    require(spec is not None and spec.loader is not None, "cannot load sealed historical consumer")
    module = importlib.util.module_from_spec(spec)
    # Execute the verified Git blob directly: a timestamp-valid stale .pyc must
    # never substitute for the source whose hash we just checked.
    module_raw = raw_git(source, "show", f"{anchor}:tools/build_fixed_point.py")
    exec(compile(module_raw, str(module_path), "exec"), module.__dict__)
    logical = "validation/composition-current.json"
    identity = module.committed_file_identity(historical, anchor, logical)
    require(identity is not None, "historical composition reference is missing")
    receipt = module.parse_json_blob(historical, identity, "historical composition reference")
    reference = {
        "receipt": logical, "receipt_git_blob": identity["git_blob"],
        "receipt_sha256": identity["sha256"],
        "composition_source_commit": receipt["composition"]["source_commit"],
    }
    binding, _, protected = module.load_source_checkpoint(
        historical, Path(build.EGA_SOURCE_CHECKPOINT_PATH), Path(logical), reference,
    )
    module.require_source_checkpoint_unchanged(historical, binding, protected)
    require(binding["post_content"]["head_commit"] == anchor,
            "historical verifier did not validate the requested actual anchor")
    return binding, protected


def verify_append_bytes(before: bytes, after: bytes, record: dict, path: str) -> None:
    require(after.startswith(before), f"semantic ledger rewrites prior bytes: {path}")
    append = after[len(before):]
    for raw, size_key, hash_key in (
        (before, "prefix_bytes", "prefix_sha256"),
        (append, "append_bytes", "append_sha256"), (after, "bytes", "sha256"),
    ):
        require(type(record.get(size_key)) is int and record[size_key] == len(raw)
                and record.get(hash_key) == hashlib.sha256(raw).hexdigest().upper(),
                f"semantic ledger exact {size_key}/{hash_key} mismatch: {path}")


def verify_semantic(build, source: Path, head: str, composition: dict) -> tuple[dict, list[str]]:
    identity = build.committed_file_identity(source, head, SEMANTIC_PATH)
    require(identity is not None, "no supported successor semantic checkpoint is committed")
    semantic = build.parse_json_blob(source, identity, "successor semantic checkpoint")
    require(semantic.get("schema") == "ega-i-6.6.5-semantic-checkpoint/v1"
            and semantic.get("status") == "LOCAL_SEMANTIC_VALIDATED"
            and semantic.get("source_unit") == "ega:I.6.6.5"
            and semantic.get("next_semantic_cursor") == "ega:I.6.6.6",
            "unsupported or nonpassing successor semantic contract")
    commit = build.git(source, "log", "-1", "--format=%H", head, "--", SEMANTIC_PATH)
    parents = build.commit_parents(source, commit)
    require(len(parents) == 1, "semantic checkpoint is not a single-parent commit")
    require(parents[0] == composition["composition_source_commit"],
            "semantic increment is not bound to the validated cumulative source commit")
    changes = build.committed_path_changes(source, parents[0], commit)
    require(set(changes) == SEMANTIC_PATHS and changes[SEMANTIC_PATH][4] == "A"
            and all(changes[p][4] == "M" for p in SEMANTIC_PATHS - {SEMANTIC_PATH}),
            "semantic commit does not have the exact bounded nine-path delta")
    for path in SEMANTIC_PATHS:
        require(build.committed_file_identity(source, commit, path)
                == build.committed_file_identity(source, head, path),
                f"semantic checkpoint content drifted after review: {path}")
    baseline = build.require_commit_object(source, semantic.get("starting_content_commit"),
                                           "semantic starting content")
    # A linear successor may replay the cumulative source commits after a
    # concurrently published root-source change.  In that case the sealed
    # semantic receipt still names the historical R47 base (396d60f...), while
    # the replayed composition base has an equivalent tree at a new commit.
    # Rebind only when the two base trees are byte-identical; never weaken the
    # original receipt or accept an arbitrary ancestry substitution.
    if build.git_optional(source, "merge-base", "--is-ancestor", baseline, parents[0]) is None:
        rebound = composition.get("composition_base_commit")
        require(isinstance(rebound, str),
                "semantic baseline is not ancestral and has no exact replay base")
        require(build.git(source, "rev-parse", f"{baseline}^{{tree}}")
                == build.git(source, "rev-parse", f"{rebound}^{{tree}}"),
                "semantic baseline replay base tree differs")
        baseline = rebound
    build.require_ancestor(source, baseline, "semantic baseline", parents[0])
    ledgers = semantic.get("ledgers")
    require(isinstance(ledgers, list)
            and len(ledgers) == 4
            and {row.get("path") for row in ledgers} == {p for p, *_ in build.EGA_LEDGER_CONTRACTS},
            "semantic ledger inventory is not the exact four append-only ledgers")
    for row in ledgers:
        path = row["path"]
        verify_append_bytes(raw_git(source, "show", f"{baseline}:{path}"),
                            raw_git(source, "show", f"{commit}:{path}"), row, path)
    for path in PROTECTED_SEMANTIC_PATHS:
        require(build.committed_file_identity(source, baseline, path)
                == build.committed_file_identity(source, head, path),
                f"protected semantic authority/inventory surface changed: {path}")
    scope = raw_git(source, "show", f"{commit}:ega/scope.json")
    require(semantic.get("scope_identity") == {
        "bytes": len(scope), "sha256": hashlib.sha256(scope).hexdigest().upper(),
    }, "semantic scope hash differs from committed scope")
    checker_identity = build.committed_file_identity(source, commit, "ega/check.py")
    require(checker_identity is not None, "committed semantic checker is absent")
    build.require_clean_path(source, "ega/check.py")
    working_checker = build.working_file_identity(source, "ega/check.py")
    require(all(working_checker[key] == checker_identity[key] for key in ("bytes", "sha256")),
            "semantic checker working bytes changed before execution")
    check = subprocess.run([sys.executable, "-B", "ega/check.py"], cwd=source,
                           capture_output=True, text=True, encoding="utf-8", timeout=600)
    require(check.returncode == 0, f"successor EGA semantic checker failed: {check.stderr or check.stdout}")
    checked = build.strict_json_loads(check.stdout, "successor EGA checker")
    require(isinstance(checked, dict) and checked.get("status") == "PASS"
            and checked.get("errors") == [], "successor semantic checker did not pass")
    expected = semantic["validation"]["scaffold_checker"]["result"]
    require(checked == expected, "successor semantic checker differs from sealed checkpoint result")
    return {"receipt": identity, "commit": commit, "tree": build.git(source, "rev-parse", f"{commit}^{{tree}}"),
            "source_unit": semantic["source_unit"], "next_source_unit": semantic["next_semantic_cursor"],
            "checker": checked, "no_root_source_change": True}, sorted(SEMANTIC_PATHS)


def load_successor(build, source: Path, logical: str, checkpoint: dict, composition: dict):
    head, tree = build.capture_source_revision(source)
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
    semantic, semantic_paths = verify_semantic(build, source, head, composition)
    # Current inputs are frozen independently of the historical byte inventory.
    paths = set(root_tex + semantic_paths + [logical, "my.bib", "tags/tags",
                "validation/composition-current.json", THIS_TOOL, THIS_TEST])
    paths.update(path for path, _ in build.EGA_PRECONTENT_TOOL_ROLES)
    paths.update(p for p in root_names if "/" not in p and Path(p).suffix.lower() in build.EGA_SHARED_BUILD_SUFFIXES)
    for directory in ("ega", "ai-integrated/registry"):
        paths.update(str(row["path"]) for row in build.committed_regular_files(source, head, directory))
    protected = []
    for row in old_protected:
        protected.append({**row, "role": "historical_checkpoint_input"})
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
        "schema": "unofficial-stacks-project-ai-drafts-ega-source-checkpoint-successor/v1",
        "status": "PASS_SOURCE_CHECKPOINT_SUCCESSOR",
        "receipt": build.committed_file_identity(source, head, logical),
        "historical_anchor": {"commit": anchor, "tree": historical["post_content"]["head_tree"],
                              "verification": historical},
        "semantic_successor": semantic, "root_source_stem": "schemes",
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
                   "historical_and_current_inputs_frozen_through_final_build_recheck"],
    }
    build.require_source_checkpoint_unchanged(source, binding, tuple(protected))
    return binding, tuple(sorted(paths)), tuple(protected)
