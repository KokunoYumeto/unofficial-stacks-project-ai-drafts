"""Typed current and exact-revision EGA binding for direct registry successors.

Historical producer bytes and receipt topology remain authoritative. The new
source endpoint is checked separately; the inherited semantic increment is
validated against its own original cumulative source commit.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

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
require = historical.require
SEMANTIC_PATH = historical.SEMANTIC_PATH
SEMANTIC_PATHS = historical.SEMANTIC_PATHS
PROTECTED_SEMANTIC_PATHS = historical.PROTECTED_SEMANTIC_PATHS
THIS_TOOL, THIS_TEST = historical.THIS_TOOL, historical.THIS_TEST
receipt_anchor = historical.receipt_anchor
verify_historical = historical.verify_historical
verify_semantic = historical.verify_semantic


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


def _load_at(build, source: Path, logical: str, checkpoint: dict, composition: dict, head: str, *, live: bool):
    head = build.require_commit_object(source, head, "direct checkpoint actual revision")
    tree = build.git(source, "rev-parse", f"{head}^{{tree}}")
    require(composition.get("schema") == DIRECT_SCHEMA, "direct checkpoint requires typed direct composition")
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
    semantic, semantic_paths = verify_semantic(build, source, head, inherited_binding)
    # Current inputs are frozen independently of the historical byte inventory.
    paths = set(root_tex + semantic_paths + [logical, "my.bib", "tags/tags",
                "validation/composition-current.json", THIS_TOOL, THIS_TEST])
    paths.update(path for path, _ in build.EGA_PRECONTENT_TOOL_ROLES)
    paths.update(DIRECT_TOOLS)
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
        "schema": SCHEMA,
        "status": STATUS,
        "receipt": build.committed_file_identity(source, head, logical),
        "historical_anchor": {"commit": anchor, "tree": historical["post_content"]["head_tree"],
                              "verification": historical},
        "semantic_successor": semantic, "inherited_composition": {"commit": prior, **inherited_id},
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
                   "historical_and_current_inputs_frozen_through_final_build_recheck"],
    }
    if live:
        build.require_source_checkpoint_unchanged(source, binding, tuple(protected))
    else:
        _recheck_at(build, source, binding, tuple(protected))
    return binding, tuple(sorted(paths)), tuple(protected)
