"""Export the readable correction selection as upstream-only, replayed patches.

Never changes mathematical sources, the real Git index, or the registry.
The isolated temporary index contains only the three named authority files.
"""
import argparse
import difflib
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path("ai-integrated/review-notes/2026-09-19-proposed-corrections.json")
OUT = ROOT / "possible-fixes"
TITLES = {
    "H100B-SOURCE-006": "Reverse the induced Ext arrows",
    "H100B-SOURCE-007": "Use the cohomological index",
    "H100B-SOURCE-009": "Reverse composition in the inverse-map argument",
    "H100B-SOURCE-011": "Use both endpoint modules in the split sequence",
    "H100B-SOURCE-013": "Write 'instead of' as two words",
    "H100B-SOURCE-014": "Use singular agreement for a diagram",
    "H100B-SOURCE-015": "Write 'have the property'",
    "H100B-SOURCE-016": "Advance the injectivity index",
    "H100B-SOURCE-017": "Use the differential leaving the target degree",
    "H100B-SOURCE-018": "Write 'instead' as one word",
    "H100B-SOURCE-019": "Supply 'to' in 'Choose beta to be'",
    "SPACES-SRC-00178-UNBOUND-Y": "Use the fibre point fixed in this implication",
    "SPACES-SRC-00269-PRODUCTS-VS-LIMITS": "Use finite limits in the fibre-product comparison",
}


def digest(data):
    return hashlib.sha256(data).hexdigest().upper()


def git(*args, data=None, env=None):
    result = subprocess.run(["git", "-C", str(ROOT), *args], input=data,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace"))
    return result.stdout


def replay_patch(patch, before, after, base):
    with tempfile.TemporaryDirectory(prefix="stacks-possible-fixes-") as tmp:
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(tmp) / "index"))
        git("read-tree", "--empty", env=env)
        for path in sorted(before):
            blob = git("rev-parse", f"{base}:{path}").decode().strip()
            git("update-index", "--add", "--cacheinfo", "100644", blob, path, env=env)
        git("apply", "--cached", "--check", "--whitespace=nowarn", "-", data=patch, env=env)
        git("apply", "--cached", "--whitespace=nowarn", "-", data=patch, env=env)
        for path, expected in after.items():
            assert git("show", f":{path}", env=env) == expected, path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    raw = (ROOT / EVIDENCE).read_bytes()
    evidence = json.loads(raw)
    status_path = Path('ai-integrated/review-notes/proposal-integration-status.json')
    status_raw = (ROOT / status_path).read_bytes()
    status = json.loads(status_raw)
    integrated = {row['finding_id']: row for row in status['composed']}
    base = evidence["authority_commit"]
    proposals = evidence["proposals"]
    assert len(proposals) == 13
    assert sum(len(p["operations"]) for p in proposals) == 17
    assert set(TITLES) == {p["finding_id"] for p in proposals}
    allowed = {"algebra.tex", "homology.tex", "spaces-limits.tex"}
    sources = {path: git("show", f"{base}:{path}") for path in sorted(allowed)}
    groups = [(p["finding_id"], [p]) for p in proposals]
    ext_ids = {"H100B-SOURCE-006", "H100B-SOURCE-007", "H100B-SOURCE-009"}
    groups += [("EXT-CONTRAVARIANCE", [p for p in proposals if p["finding_id"] in ext_ids]),
               ("ALL-13-PROPOSALS", proposals)]
    generated, records = {}, []
    for name, selected in groups:
        by_path = {}
        for proposal in selected:
            for op in proposal["operations"]:
                path = op["source_path"]
                assert path in allowed
                assert digest(sources[path]) == op["authority_file_sha256"], path
                start, end = op["start_byte"], op["end_byte_exclusive"]
                assert sources[path][start:end] == op["old_text"].encode("utf-8"), name
                by_path.setdefault(path, []).append(op)
        after, pieces = {}, []
        for path, operations in sorted(by_path.items()):
            old = sources[path]
            new, previous_start = old, len(old) + 1
            for op in sorted(operations, key=lambda x: x["start_byte"], reverse=True):
                assert op["end_byte_exclusive"] <= previous_start, "overlapping operations"
                new = new[:op["start_byte"]] + op["replacement_text"].encode("utf-8") + new[op["end_byte_exclusive"]:]
                previous_start = op["start_byte"]
            assert old.endswith(b"\n") and new.endswith(b"\n")
            after[path] = new
            pieces.append(f"diff --git a/{path} b/{path}\n")
            pieces.extend(difflib.unified_diff(old.decode("utf-8").splitlines(True),
                          new.decode("utf-8").splitlines(True), f"a/{path}", f"b/{path}", n=3))
        patch = "".join(pieces).encode("utf-8")
        replay_patch(patch, {p: sources[p] for p in after}, after, base)
        filename = name + ".patch"
        generated[filename] = patch
        records.append({"file": filename, "finding_ids": [p["finding_id"] for p in selected],
                        "bytes": len(patch), "sha256": digest(patch),
                        "git_apply_check": "PASS", "exact_postimage_replay": "PASS",
                        "postimages": {p: digest(b) for p, b in sorted(after.items())}})
    manifest = {"schema": "upstream-only-possible-fixes/v1", "authority_commit": base,
                "evidence": EVIDENCE.as_posix(), "evidence_sha256": digest(raw),
                "proposal_units": 13, "exact_operations": 17, "patches": records,
                "integration_status": {"path": status_path.as_posix(), "sha256": digest(status_raw),
                    "composed_units": len(integrated), "pending_units": status['pending_units']},
                "scope": "Selected proposals only; no theorem additions, translations, or AI-source repairs.",
                "upstream_current_head_checked": False, "mathematical_approval_implied": False}
    generated["manifest.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    lines = ["# Possible fixes: ready-to-inspect patches", "",
        "These patches change only inherited official Stacks text. They contain no new",
        "theorems from this project, no translation changes, and no repairs to AI additions.",
        "They are proposals, not officially accepted errata. Applying cleanly is a byte check,",
        "not a mathematical correctness certificate.", "",
        "[Read the arguments and original/replacement passages](../PROPOSED_CORRECTIONS.md) ·",
        "[Possible new additions (separate)](../POSSIBLE_ADDITIONS.md)", "",
        f"**Current status: {len(integrated)} of these 13 are now in the cumulative draft and",
        f"[combined corrections-only export](../upstream-corrections/README.md); {status['pending_units']} remain pending.**",
        "All thirteen are included in the larger corrections-only export through R51. Do not apply them twice.", "",
        "## Review or use one correction", "",
        f"All patches are based on official commit `{base}`.",
        "Each individual patch and both bundles have been applied in a separate index",
        "containing only the affected official files, with exact postimage verification.",
        "There is no dependency on this fork. Check against your own checkout before applying:", "",
        "```sh", "git apply --check /path/to/chosen.patch", "git apply /path/to/chosen.patch", "```", "",
        "The first command changes nothing; the second applies only the chosen diff.",
        "Current upstream may have changed since the pinned commit: inspect conflicts or",
        "already-fixed passages instead of forcing a patch. No current-upstream check is claimed.", "",
        "The Ext arrow and composition corrections belong together mathematically. Use",
        "[the three-proposal Ext bundle](EXT-CONTRAVARIANCE.patch) for that argument;",
        "individual diffs remain available for inspection. Nearby individual patches may",
        "share context, so do not assume arbitrary sequential application will work.", "",
        "| Possible fix | Original location | Patch |", "|---|---|---|"]
    for p in proposals:
        key, op = p["finding_id"], p["operations"][0]
        lines.append(f"| {TITLES[key]} (`{key}`) | [{op['source_path']}:{op['authority_line']}]({op['source_link']}) | [diff]({key}.patch) |")
    lines += ["", "[All 13 proposals as one patch](ALL-13-PROPOSALS.patch) · [Hashes and replay evidence](manifest.json)", "",
        "## Coverage", "", "This exporter covers the 13-unit, 17-operation readable selection, not every",
        "historical correction. The larger [integrated correction comparison](../CHANGES_FROM_UPSTREAM.md)",
        "and [filterable chapter browser](../ai-integrated/changes/index.html) remain separate.",
        "Their other corrections are not silently included in these downloads. Historical",
        "duplicates and withdrawn suggestions receive no patch. Regenerate or verify with",
        "`python tools/generate_possible_fix_patches.py` or the same command with `--check`.", ""]
    lines += ['Patch export and status maintenance: OpenAI Codex - GPT-6 Astra, Ultra effort.',
        'This is not a new mathematical or human review of the historical selection.', '']
    generated["README.md"] = "\n".join(lines).encode("utf-8")
    for filename, content in generated.items():
        target = OUT / filename
        if args.check:
            assert target.read_bytes() == content, filename
        else:
            OUT.mkdir(exist_ok=True)
            target.write_bytes(content)
    print(json.dumps({"status": "PASS", "proposals": 13, "operations": 17,
                      "replayed_patches": len(records), "generated_files": len(generated),
                      "source_files_changed": 0, "check_only": args.check}))


if __name__ == "__main__":
    main()
