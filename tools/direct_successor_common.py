#!/usr/bin/env python3
"""Bounded committed-object, closure and projection checks for direct successors."""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys

sys.dont_write_bytecode = True
SCHEMA = "unofficial-ai-integrated-stacks-composition/v3"
MODE = "manifest-bound registry-order replay rebased onto verified cumulative source"
COMPOSER = "tools/compose_overlay_projection.py"
RECEIPT = "validation/composition-current.json"
ROUND = re.compile(r"stacks-errata-a04446e-r([1-9][0-9]*)\Z")
ROOT_TEX = re.compile(r"[a-z][a-z0-9-]*\.tex\Z")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, name, minimum=0):
    require(type(value) is int and value >= minimum, f"invalid integer: {name}")
    return value


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_json(data):
    return json.loads(data, object_pairs_hook=unique_pairs)


def safe_path(path):
    require(isinstance(path, str) and re.fullmatch(r"[A-Za-z0-9._/-]+", path)
            and not path.startswith("/")
            and all(part not in {"", ".", ".."} for part in path.split("/")),
            f"unsafe relative path: {path!r}")
    return path


def identity(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest().upper(),
            "git_blob": hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()}


def stable_ids(entry):
    ids = entry.get("stable_ids")
    if isinstance(ids, str):
        ids = ids.split()
    require(isinstance(ids, list) and ids and
            all(isinstance(value, str) and value for value in ids), "invalid stable IDs")
    return ids


def admitted_suffix(previous, current):
    require(isinstance(previous, dict) and isinstance(current, dict), "invalid registries")
    old, entries = previous.get("registered_entries"), current.get("registered_entries")
    require(isinstance(old, list) and old and isinstance(entries, list), "empty registry prefix")
    require(entries[:len(old)] == old and len(entries) > len(old),
            "registry must strictly extend the exact previous prefix")
    require({k: v for k, v in previous.items() if k != "registered_entries"} ==
            {k: v for k, v in current.items() if k != "registered_entries"},
            "registry header changed")
    names, ids = [], []
    for entry in entries:
        require(isinstance(entry, dict) and isinstance(entry.get("id"), str), "invalid entry")
        names.append(entry["id"])
        ids.extend(stable_ids(entry))
    require(len(set(names)) == len(names) and len(set(ids)) == len(ids),
            "duplicate overlay or stable ID")
    suffix = entries[len(old):]
    rounds = []
    for entry in suffix:
        match = ROUND.fullmatch(entry["id"])
        require(match is not None, "draft only supports admitted errata rounds")
        rounds.append(int(match.group(1)))
    require(rounds == sorted(set(rounds)), "unordered successor rounds")
    return suffix, rounds, len(ids)


def composer_arguments(existing, target, base, source):
    for name, rounds in (("existing", existing), ("target", target)):
        require(isinstance(rounds, list) and rounds and
                all(type(n) is int and n > 0 for n in rounds) and
                rounds == sorted(set(rounds)), f"invalid {name} rounds")
    require(target[:len(existing)] == existing and len(target) > len(existing),
            "composer target does not strictly extend previous rounds")
    return ["--existing-rounds", *map(str, existing), "--target-rounds", *map(str, target),
            "--base-revision", base, "--check-revision", source]


def previous_rounds(previous):
    verifier = previous.get("projection_verifier", {})
    require(verifier.get("status") == "PASS" and verifier.get("path") == COMPOSER,
            "previous receipt lacks the supported passing composer")
    tokens = shlex.split(verifier.get("command", ""))
    flags = ("--existing-rounds", "--target-rounds", "--base-revision", "--check-revision")
    require(len(tokens) > 2 and tokens[0] in {"python", "python3", Path(sys.executable).name}
            and tokens[1] == COMPOSER and all(tokens.count(flag) == 1 for flag in flags),
            "invalid previous composer command")
    a, b, c, d = [tokens.index(flag) for flag in flags]
    require(a == 2 and a < b < c < d and d + 2 == len(tokens), "invalid previous command shape")
    try:
        existing, target = [int(n) for n in tokens[a+1:b]], [int(n) for n in tokens[b+1:c]]
    except ValueError as exc:
        raise ValueError("invalid previous command rounds") from exc
    comp = previous["composition"]
    expected = composer_arguments(existing, target, comp["base_commit"], comp["source_commit"])
    require(tokens[2:] == expected, "previous command flags or commit bindings differ")
    return target


def full_profile(previous, affected):
    profile = previous.get("required_build_stems")
    require(isinstance(profile, list) and profile and len(set(profile)) == len(profile)
            and all(isinstance(p, str) and ROOT_TEX.fullmatch(p + ".tex") for p in profile),
            "invalid inherited full profile")
    require(affected and all(ROOT_TEX.fullmatch(p) for p in affected), "invalid affected sources")
    return [*profile, *sorted({p[:-4] for p in affected} - set(profile))]


class Git:
    """Only explicit committed-object reads and bounded working-file checks."""
    def __init__(self, root):
        self.root = Path(root).resolve()
        self._identities = {}

    def raw(self, *args, data=None):
        result = subprocess.run(["git", "-C", str(self.root), *args], input=data,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        require(result.returncode == 0, "Git object check failed: " + result.stderr.decode("utf-8", "replace").strip())
        return result.stdout

    def text(self, *args):
        return self.raw(*args).decode("utf-8").strip()

    def commit(self, value):
        require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value),
                "commits must be exact lowercase SHA-1 values, not refs")
        require(self.text("rev-parse", value + "^{commit}") == value, "commit object mismatch")
        return value

    def tree(self, commit):
        return self.text("rev-parse", commit + "^{tree}")

    def parents(self, commit):
        return self.text("rev-list", "--parents", "-n", "1", commit).split()[1:]

    def blob(self, commit, path):
        return self.raw("cat-file", "blob", commit + ":" + safe_path(path))

    def ident(self, commit, path):
        # Only immutable full commit IDs are memoized within this invocation;
        # working files are always reread at each cleanliness boundary.
        key = (commit, safe_path(path))
        immutable = isinstance(commit, str) and re.fullmatch(r"[0-9a-f]{40}", commit)
        if not immutable or key not in self._identities:
            value = identity(self.blob(commit, path))
            if immutable:
                self._identities[key] = value
            return dict(value)
        return dict(self._identities[key])

    def document(self, commit, path):
        value = parse_json(self.blob(commit, path))
        require(isinstance(value, dict), "JSON evidence must be an object")
        return value

    def changes(self, parent, commit):
        raw = self.raw("diff-tree", "--no-commit-id", "--raw", "--no-abbrev",
                       "--no-renames", "-z", "-r", parent, commit, "--")
        chunks = raw.split(b"\0")
        require(chunks[-1] == b"" and (len(chunks)-1) % 2 == 0, "invalid raw delta")
        changes = {}
        for i in range(0, len(chunks)-1, 2):
            fields = chunks[i].decode("ascii").split()
            path = safe_path(chunks[i+1].decode("utf-8"))
            require(len(fields) == 5 and fields[0].startswith(":") and path not in changes,
                    "invalid raw change row")
            changes[path] = (fields[0][1:], *fields[1:])
        return changes

    def linear(self, base, head):
        commits = self.text("rev-list", "--reverse", base + ".." + head).splitlines()
        parent = base
        for commit in commits:
            require(self.parents(commit) == [parent], "nonlinear or skipped commit")
            parent = commit
        require(parent == head, "linear range did not reach endpoint")
        return commits

    def clean_file(self, commit, path, exact=False):
        path = safe_path(path)
        local = (self.root / path).resolve()
        require(local.is_relative_to(self.root), "working path escapes repository")
        data = local.read_bytes()
        if exact:
            require(identity(data) == self.ident(commit, path), f"working bytes differ: {path}")
        else:
            blob = self.raw("hash-object", "--path=" + path, "--stdin", data=data).decode().strip()
            require(blob == self.ident(commit, path)["git_blob"], f"working Git bytes differ: {path}")


def exact_import(original, actual):
    require(original and actual == {"ai-integrated/" + p: row for p, row in original.items()},
            "import is not exact prefixed old/new mode-and-blob replay")
    require(all(row[4] in {"A", "M"} and row[1] == "100644" for row in original.values()),
            "import deletion or file-type change is unsupported")


def source_delta(changes, affected):
    require(set(changes) == set(affected), "source delta differs from admitted affected roots")
    require(all(ROOT_TEX.fullmatch(p) and row[4] == "M" and row[0] == row[1] == "100644"
                for p, row in changes.items()), "source deletion, addition, or type change is unsupported")


def manifest_files(git, revision, directory, node, *, require_bytes=True):
    """Check every declared reference and the exact copy consumed by the composer."""
    if isinstance(node, dict):
        if "path" in node:
            require({"path", "sha256"}.issubset(node) and (not require_bytes or "bytes" in node),
                    "incomplete manifest reference")
            path = directory + "/" + safe_path(node["path"])
            observed = git.ident(revision, path)
            require(("bytes" not in node or (type(node["bytes"]) is int and node["bytes"] == observed["bytes"]))
                    and str(node["sha256"]).upper() == observed["sha256"], "manifest reference mismatch")
            if "git_blob" in node:
                require(node["git_blob"] == observed["git_blob"], "manifest blob mismatch")
            git.clean_file(revision, path, exact=True)
        for value in node.values():
            manifest_files(git, revision, directory, value, require_bytes=require_bytes)
    elif isinstance(node, list):
        for value in node:
            manifest_files(git, revision, directory, value, require_bytes=require_bytes)


def source_map_bindings(row, manifest):
    """Bind the paths actually read by the composer, not merely similar bytes."""
    for key, declarations in (("payload", "builds"), ("authority", "source_authorities")):
        path = safe_path(row.get(key))
        references = [item for item in manifest.get(declarations, []) if item.get("path") == path]
        require(len(references) == 1, f"source-map {key} is not uniquely manifest-declared")
        if key == "authority":
            require(str(row.get("authority_sha256", "")).upper() == str(references[0].get("sha256", "")).upper(),
                    "source-map authority hash differs from manifest")
    for key in ("composition_base", "composition_projection"):
        if row.get(key) is not None:
            path = safe_path(row[key])
            declarations = [*manifest.get("builds", []), *manifest.get("source_authorities", [])] if key == "composition_base" else manifest.get("builds", [])
            require(sum(item.get("path") == path for item in declarations) == 1,
                    f"source-map {key} is not uniquely manifest-declared")


def target_inventory(git, imported, entries, rounds, new_rounds=None):
    by_id = {entry["id"]: entry for entry in entries}
    result, operation_ids = {}, set()
    positions = []
    for number in rounds:
        overlay_id = f"stacks-errata-a04446e-r{number}"
        require(overlay_id in by_id, "previous/target composer includes unadmitted round")
        entry = by_id[overlay_id]
        positions.append(entries.index(entry))
        canonical_namespace = "commons/stacks/errata" + (f"/r{number}" if number != 1 else "")
        require(entry.get("namespace") == canonical_namespace,
                "registry namespace differs from the actual composer candidate directory")
        directory = "ai-integrated/candidates/" + safe_path(entry["namespace"])
        manifest_path = directory + "/candidate.manifest.json"
        require(git.ident(imported, manifest_path)["sha256"] == entry["manifest_sha256"].upper(),
                "registry manifest hash mismatch")
        git.clean_file(imported, manifest_path, exact=True)
        manifest = git.document(imported, manifest_path)
        require(manifest.get("candidate_id") == overlay_id and manifest.get("namespace") == entry["namespace"],
                "manifest identity mismatch")
        is_new = new_rounds is None or number in new_rounds
        if is_new:
            manifest_files(git, imported, directory, manifest)
        else:
            # Immutable old candidate namespaces are preserved by the exact
            # direct transaction delta. Revalidate every composer-consumed
            # reference, retaining their original hash-only manifest contract.
            manifest_files(git, imported, directory, manifest["source_map"], require_bytes=False)
        require(manifest["source_map"]["path"] == "source-map.jsonl", "unsupported source-map layout")
        rows = [parse_json(line) for line in git.blob(imported, directory + "/source-map.jsonl").splitlines() if line.strip()]
        require([row["unit_id"] for row in rows] == stable_ids(entry), "source-map stable-ID order mismatch")
        sources, count = {}, 0
        for row in rows:
            source_map_bindings(row, manifest)
            if not is_new:
                for key, declarations in (("authority", "source_authorities"), ("payload", "builds")):
                    reference = next(item for item in manifest[declarations] if item["path"] == row[key])
                    manifest_files(git, imported, directory, reference, require_bytes=False)
                for key in ("composition_base", "composition_projection"):
                    if key in row:
                        declarations = [*manifest.get("builds", []), *manifest.get("source_authorities", [])] if key == "composition_base" else manifest.get("builds", [])
                        reference = next(item for item in declarations if item["path"] == row[key])
                        manifest_files(git, imported, directory, reference, require_bytes=False)
            operations = row.get("operations", [])
            require(isinstance(operations, list), "invalid operations")
            if not operations:
                continue
            name = row["source"]
            require(isinstance(name, str) and ROOT_TEX.fullmatch(name), "non-root source")
            sources[name] = sources.get(name, 0) + len(operations)
            count += len(operations)
            for operation in operations:
                op_id = operation.get("operation_id")
                require(isinstance(op_id, str) and op_id and op_id not in operation_ids,
                        "duplicate or missing operation ID")
                operation_ids.add(op_id)
        require(count > 0, "overlay has no operations")
        result[overlay_id] = {"manifest": manifest, "sources": sources, "operations": count,
                              "manifest_sha256": entry["manifest_sha256"].upper(),
                              "stable_ids": len(stable_ids(entry))}
    require(positions == sorted(set(positions)), "target overlays out of registry order")
    return result


def check_projection(report, existing, target, base, source, inventory, new_ids, git, previous_public):
    new_count = sum(inventory[name]["operations"] for name in new_ids)
    total = sum(row["operations"] for row in inventory.values())
    expected = {"schema": "unofficial-ai-integrated-stacks-overlay-composition/v1", "status": "PASS",
                "existing_rounds": existing, "target_rounds": target, "base_revision": base,
                "check_revision": source, "write_requested": False, "operations": total,
                "new_operations": new_count}
    for key, value in expected.items():
        require(type(report.get(key)) is type(value) and report.get(key) == value,
                f"projection mismatch: {key}")
    require(report.get("preapplied_operation_ids") == [] and
            report.get("semantic_dispositions", {}).get("consumed_operation_ids") == [],
            "draft supports fresh edits only; preapplied/disposed operations need a separate contract")
    reports = report.get("overlays")
    require(isinstance(reports, list) and [r.get("overlay_id") for r in reports] == list(inventory),
            "projection overlay inventory mismatch")
    expected_sources, affected = set(), set()
    for row, (overlay_id, data) in zip(reports, inventory.items()):
        expected_sources.update(data["sources"])
        if overlay_id in new_ids:
            affected.update(data["sources"])
        require(integer(row.get("round"), "projection round", 1) == int(ROUND.fullmatch(overlay_id).group(1)), "projection round mismatch")
        require(row.get("manifest_sha256") == data["manifest_sha256"] and
                integer(row.get("stable_ids"), "projection stable IDs", 1) == data["stable_ids"],
                "projection manifest or stable-ID binding mismatch")
        require(set(row.get("sources", {})) == set(data["sources"]), "projection overlay sources mismatch")
        for path, count in data["sources"].items():
            require(integer(row["sources"][path].get("operations"), "overlay operations", 1) == count,
                    "projection overlay operation count mismatch")
    require(isinstance(report.get("sources"), dict) and set(report["sources"]) == expected_sources,
            "projection root inventory mismatch")
    source_delta(git.changes(base, source), affected)
    result = {}
    for path, row in report["sources"].items():
        expected_new = sum(inventory[name]["sources"].get(path, 0) for name in new_ids)
        require(integer(row.get("new_operations"), "source new operations") == expected_new,
                "projection source operation count mismatch")
        require(row.get("written") is False and row.get("matches_target_after") is True,
                "projection was writable or does not match source commit")
        for prefix, revision in (("before", base), ("composed", source)):
            integer(row.get(prefix + "_bytes"), "source bytes", 1)
            require({k: row.get(prefix + "_" + k) for k in ("bytes", "sha256", "git_blob")} ==
                    git.ident(revision, path), f"projection source identity mismatch: {path}")
        require(git.ident(previous_public, path) == git.ident(base, path), "cumulative source changed before composition")
        git.clean_file(source, path)
        if path in affected:
            require(row.get("preapplied_operation_ids") == [] and row.get("semantic_disposition_operation_ids") == [],
                    "source includes nonfresh operation")
            # Historical supersessions may remain in the target; new ones are rejected separately.
            result[path] = deepcopy(row)
        else:
            require(git.ident(base, path) == git.ident(source, path), "preserved root changed")
    return result, new_count
