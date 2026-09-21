"""Export admitted textual errata without any fork-only theorem additions.

Uses the existing hash-bound comparison model, never the cumulative fork text.
Git replay uses isolated indexes; no source file or user's index is changed.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import dataclasses
import difflib
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import zipfile

try:
    from . import generate_changes_from_upstream as evidence
except ImportError:
    import generate_changes_from_upstream as evidence

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "upstream-corrections"
PUBLIC = "https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts"
RAW = "https://raw.githubusercontent.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/main/upstream-corrections/"
ATTRIBUTION = "Patch export and packaging: OpenAI Codex — GPT-6 Astra, Ultra effort. This is not a new mathematical or human review of the historical corrections."


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def git(*args, data=None, env=None):
    result = subprocess.run(["git", "-C", str(ROOT), *args], input=data,
                            capture_output=True, env=env, check=True)
    return result.stdout


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def source_path(path):
    require(re.fullmatch(r"[a-z0-9-]+\.tex", path) is not None,
            "not an inherited chapter path: " + path)
    return path


def active_operations(units, supersessions):
    owners = {}
    for unit in units:
        for op in unit.operations:
            require(op.operation_id not in owners, "duplicate operation ID")
            owners[op.operation_id] = (unit, op)
    removed = set()
    for successor, predecessor in supersessions.items():
        require(successor in owners and predecessor in owners, "unknown supersession")
        new_unit, new = owners[successor]
        old_unit, old = owners[predecessor]
        require(new_unit.overlay_index > old_unit.overlay_index and
                new_unit.source == old_unit.source and
                new.start_byte < old.end_byte_exclusive and
                old.start_byte < new.end_byte_exclusive, "invalid supersession")
        removed.add(predecessor)
    return owners, removed


def make_patch(path, before, after):
    source_path(path)
    require(before != after and before.endswith(b"\n") and after.endswith(b"\n"),
            "empty change or unsupported missing final newline")
    def blob(raw):
        return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    header = f"diff --git a/{path} b/{path}\nindex {blob(before)}..{blob(after)} 100644\n"
    diff = "".join(difflib.unified_diff(before.decode("utf-8").splitlines(True),
                                     after.decode("utf-8").splitlines(True),
                                     "a/" + path, "b/" + path, n=3))
    return (header + diff).encode("utf-8")


def replay_all(patches, before, after, baseline):
    # Each chapter is independently applicable to the baseline and the chapter
    # series must equal the combined patch byte for byte after application.
    with tempfile.TemporaryDirectory(prefix="stacks-correction-export-") as temporary:
        folder = Path(temporary).resolve()
        require(folder.parent == Path(tempfile.gettempdir()).resolve() and
                folder.name.startswith("stacks-correction-export-"), "unsafe temporary index directory")
        for mode in ("chapters", "combined"):
            env = dict(os.environ, GIT_INDEX_FILE=str(folder / (mode + ".index")))
            git("read-tree", "--empty", env=env)
            entries = []
            for path in sorted(before):
                blob = git("rev-parse", baseline + ":" + path).decode().strip()
                entries.append(f"100644 {blob}\t{path}\n")
            git("update-index", "--index-info", data="".join(entries).encode(), env=env)
            selected = list(patches.values()) if mode == "chapters" else [b"".join(patches.values())]
            for patch in selected:
                git("apply", "--cached", "--check", "--whitespace=nowarn", "-", data=patch, env=env)
                git("apply", "--cached", "--whitespace=nowarn", "-", data=patch, env=env)
            require(git("ls-files", env=env).decode().splitlines() == sorted(before), "patch adds an unexpected path")
            for path, expected in after.items():
                require(git("show", ":" + path, env=env) == expected, "postimage mismatch: " + path)


def archive_bytes(files):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, raw in sorted(files.items()):
            require(not path.startswith("/") and ".." not in Path(path).parts, "unsafe archive path")
            info = zipfile.ZipInfo(path, date_time=(2026, 9, 22, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, raw)
    raw = stream.getvalue()
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        require(archive.testzip() is None and set(archive.namelist()) == set(files), "ZIP inventory failure")
        require(all(archive.read(p) == b for p, b in files.items()), "ZIP byte mismatch")
    return raw


def generate():
    model = evidence.build_model(ROOT)
    units = model.units
    supersessions = {}
    for name in sorted({u.source_map_link for u in units}):
        for row in evidence.jsonl_load(ROOT / name):
            for op in row.get("operations", []):
                if op.get("supersedes_operation_id"):
                    supersessions[op["operation_id"]] = op["supersedes_operation_id"]
    owners, removed = active_operations(units, supersessions)
    before, after, chapter_units, chapter_ops = {}, {}, defaultdict(list), defaultdict(list)
    dispositions = []
    for unit in units:
        if unit.source == "tags/tags":
            dispositions.append({"id": unit.stable_id, "status": "excluded_fork_tag_allocation",
                "reason": "Fork-allocated permanent tags are not proposed official Stacks tag assignments.",
                "evidence": PUBLIC + "/blob/main/CHANGES_FROM_UPSTREAM.md#" + unit.stable_id.lower()})
            continue
        source_path(unit.source)
        effective = [op for op in unit.operations if op.operation_id not in removed]
        if not effective:
            dispositions.append({"id": unit.stable_id, "status": "superseded",
                "replaced_by_operations": [s for s, p in supersessions.items() if p in {o.operation_id for o in unit.operations}]})
            continue
        chapter_units[unit.source].append(unit)
        chapter_ops[unit.source].extend(effective)
        dispositions.append({"id": unit.stable_id, "status": "included", "chapter": unit.source,
                             "operation_ids": [op.operation_id for op in effective]})
    patches = {}
    chapter_records = []
    for path in sorted(chapter_units):
        before[path] = git("show", model.official_commit + ":" + path)
        after[path] = evidence.apply_operations(before[path], chapter_ops[path], path)
        patch = make_patch(path, before[path], after[path])
        patches[path] = patch
        chapter_records.append({"source": path, "file": "chapters/" + path[:-4] + ".patch",
            "units": len(chapter_units[path]), "operations": len(chapter_ops[path]),
            "unit_ids": [u.stable_id for u in chapter_units[path]],
            "bytes": len(patch), "sha256": sha(patch),
            "preimage_bytes": len(before[path]), "preimage_sha256": sha(before[path]),
            "postimage_bytes": len(after[path]), "postimage_sha256": sha(after[path])})
    replay_all(patches, before, after, model.official_commit)
    combined = b"".join(patches.values())
    included_count = sum(len(v) for v in chapter_units.values())
    manifest = {"schema": "stacks-upstream-corrections-only/v1", "official_baseline": model.official_commit,
        "registry_sha256": model.registry_sha256, "admitted_rounds": model.overlay_count,
        "historical_registry_ids": model.unit_count, "included_effective_textual_units": included_count,
        "included_operations": sum(len(v) for v in chapter_ops.values()),
        "chapters": chapter_records, "dispositions": dispositions,
        "combined": {"file": "ALL-TEXTUAL-CORRECTIONS.patch", "bytes": len(combined), "sha256": sha(combined)},
        "replay": {"independent_chapter_patches": "PASS", "combined_patch": "PASS", "identical_exact_postimages": True},
        "contains_new_theorem_additions": False, "contains_fork_tag_assignments": False,
        "includes_13_additional_proposals": False, "current_upstream_checked": False,
        "ai_role": ATTRIBUTION,
        "input_closure": [{"path": p, "bytes": n, "sha256": h} for p, n, h in model.input_closure]}
    rows = ["# Corrections only: review or reuse without adopting this fork", "",
        f"**{included_count:,} effective textual correction units across {len(chapter_records)} chapters.**",
        "Download one chapter patch or the combined patch. You do not need to clone this",
        "repository, import its history, or take any of its added theorems.", "",
        f"- [Download all textual corrections as one patch]({RAW}ALL-TEXTUAL-CORRECTIONS.patch).",
        f"- [Download the patch bundle and offline review index]({RAW}corrections-only.zip).",
        "- [Review exact old/new text, reasons and evidence](REVIEW.md).",
        "- [Machine-readable identities and replay results](manifest.json).", "",
        "## Apply to your own Stacks checkout", "",
        "The patches target the official Stacks revision",
        f"`{model.official_commit}`. Later upstream changes have **not** been checked.",
        "Inspect the diff and use the non-mutating check first:", "", "```sh",
        "git apply --stat /path/to/ALL-TEXTUAL-CORRECTIONS.patch",
        "git apply --check /path/to/ALL-TEXTUAL-CORRECTIONS.patch",
        "git apply /path/to/ALL-TEXTUAL-CORRECTIONS.patch", "```", "",
        "Use a chapter filename instead for a smaller batch. Choose the combined patch",
        "**or** chapter patches, not both. Chapter patches touch disjoint files, so they",
        "can be used independently or together. No commit is created automatically.",
        "If a check fails, inspect conflicts or already-fixed passages; do not force it.",
        "To choose smaller pieces, use the unit-by-unit review below and normal diff",
        "editing or interactive staging in your own checkout.", "",
        "## Choose a chapter", "", "| Chapter | Correction units | Download | Review |",
        "|---|---:|---|---|"]
    for row in chapter_records:
        path = row["source"]
        rows.append(f"| `{path}` | {row['units']} | [patch]({RAW}{row['file']}) | [entries](reviews/{path[:-4]}.md) |")
    rows += ["", "## What is and is not included", "",
        f"The {model.unit_count:,} historical IDs in R1–R{model.overlay_count} remain accounted for:",
        f"{included_count:,} effective textual units are exported; one earlier correction was",
        "superseded by its explicitly recorded replacement, and one fork-specific tag",
        "allocation is excluded. No unofficial permanent tags are proposed for upstream.",
        "The 13 [additional possible-fix proposals](../possible-fixes/README.md) are a",
        "separate, not-yet-composed set and are not silently included here. Translation",
        "choices, Verdier/FGA/FAC/Pursuing Stacks additions and other new exposition are",
        "excluded. Historical correction evidence remains unchanged.", "",
        "These are AI-reviewed suggestions already present in our draft, not officially",
        "accepted Stacks errata. Exact replay proves which bytes change, not mathematical",
        "correctness. There is no claim of human review or upstream endorsement.", "",
        ATTRIBUTION, "Historical candidate review records retain their original provenance.", "",
        "Modified Stacks text retains its existing GNU Free Documentation License; see",
        "[COPYING](COPYING). Reproduce or check the export with",
        "`python tools/export_upstream_corrections.py` (or append `--check`) in this repository.", ""]
    review_header = ["# Textual corrections: exact changes and review evidence", "",
              "These entries are separate from new theorem additions. The chapter patches",
              "and combined patch contain exactly this effective textual set.", "", ATTRIBUTION, ""]
    review = []
    chapter_reviews = {}
    review_index = review_header + ["Review one chapter at a time; there is no need to open a megabyte-sized diff.", ""]
    for path in sorted(chapter_units):
        start = len(review)
        review += ["## " + path[:-4], "", f"[Chapter patch]({RAW}chapters/{path[:-4]}.patch)", ""]
        for unit in chapter_units[path]:
            effective = [o for o in unit.operations if o.operation_id not in removed]
            review += ["### " + unit.stable_id, "", f"`{unit.source}` — {unit.locus}; {unit.defect_class.replace('_', ' ')}.", "",
                f"[Original passage]({evidence.official_source_link(model.official_commit, path, tuple(effective))}) · "
                f"[Review evidence]({PUBLIC}/blob/main/{unit.review_link}) · "
                f"[Manifest]({PUBLIC}/blob/main/{unit.manifest_link})", ""]
            if unit.proof:
                review += [unit.proof, ""]
            if unit.legacy_summary:
                review += [unit.legacy_summary, ""]
            if unit.adverse_evidence:
                review += ["Adverse evidence / qualification: " + unit.adverse_evidence, ""]
            if unit.proofs_link:
                review += [f"[Detailed argument]({PUBLIC}/blob/main/{unit.proofs_link})", ""]
            for op in effective:
                review += ["````diff", *difflib.unified_diff(op.old_text.splitlines(), op.replacement_text.splitlines(),
                                                          "original", "replacement", lineterm=""), "````", ""]
        review_name = "reviews/" + path[:-4] + ".md"
        chapter_reviews[review_name] = "\n".join(review_header + review[start:]).encode("utf-8")
        review_index.append(f"- [{path}]({review_name}) — {len(chapter_units[path])} correction units.")
    files = {row["file"]: patches[row["source"]] for row in chapter_records}
    files.update(chapter_reviews)
    files.update({"ALL-TEXTUAL-CORRECTIONS.patch": combined, "manifest.json": json_bytes(manifest),
                  "README.md": "\n".join(rows).encode(), "REVIEW.md": ("\n".join(review_index) + "\n").encode(),
                  "COPYING": git("show", model.official_commit + ":COPYING")})
    package = archive_bytes(files)
    files["corrections-only.zip"] = package
    files["downloads.json"] = json_bytes({"schema": "stacks-correction-downloads/v1",
        "ai_role": ATTRIBUTION, "files": [{"path": p, "bytes": len(b), "sha256": sha(b)} for p, b in sorted(files.items())],
        "zip_reopened_all_entries_exact": True})
    return manifest, files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    manifest, files = generate()
    for name, raw in files.items():
        target = OUT / name
        if args.check:
            require(target.read_bytes() == raw, "generated export drift: " + name)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
    print(json.dumps({"status": "PASS", "historical_ids": manifest["historical_registry_ids"],
        "effective_textual_units": manifest["included_effective_textual_units"],
        "chapter_patches": len(manifest["chapters"]), "combined_patch_replay": "PASS",
        "source_files_changed": 0, "files": len(files), "check_only": args.check}))


if __name__ == "__main__":
    main()
