#!/usr/bin/env python3
"""Derive a direct composition receipt; emit JSON or exclusively write a new path.

Never modifies source, registry, Git state, or existing receipts. A caller may
apply the verified result to the canonical current pointer as a separate edit.
"""
import argparse
import json
from pathlib import Path
import sys

from direct_successor_composition import derive, require, Git, protected_tools


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    for name in ("previous-public", "registry-cutoff", "source-commit"):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--output", type=Path, help="New validation/direct-successor-*.json path only; no overwrite")
    parser.add_argument("--check", type=Path, help="Verify an existing receipt instead of writing")
    args = parser.parse_args()
    require(not (args.output and args.check), "--output and --check are mutually exclusive")
    objects = Git(args.repo)
    head = objects.commit(objects.text("rev-parse", "HEAD"))
    tool_ids = protected_tools(objects, head)
    receipt, _ = derive(args.repo, args.previous_public, args.registry_cutoff, args.source_commit)
    require(protected_tools(objects, head) == tool_ids, "direct writer tools changed during derivation")
    encoded = (json.dumps(receipt, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    if args.check:
        target = (objects.root / args.check).resolve() if not args.check.is_absolute() else args.check.resolve()
        require(target.is_relative_to(objects.root), "check path escapes repository")
        require(target.read_bytes() == encoded, "saved direct receipt does not match derived bytes")
        print(json.dumps({"status": "PASS_RECEIPT_CHECK", "path": target.relative_to(objects.root).as_posix()}))
    elif args.output:
        target = (objects.root / args.output).resolve() if not args.output.is_absolute() else args.output.resolve()
        require(target.parent == objects.root / "validation" and target.name.startswith("direct-successor-")
                and target.suffix == ".json" and target.name != "direct-successor-current.json", "unsafe output path")
        with target.open("xb") as handle:
            handle.write(encoded)
        require(target.read_bytes() == encoded, "written receipt byte readback mismatch")
        print(json.dumps({"status": "PASS_COMPOSITION_RECEIPT_WRITTEN", "path": target.relative_to(objects.root).as_posix()}))
    else:
        sys.stdout.buffer.write(encoded)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError, RuntimeError) as exc:
        print("Direct receipt: FAIL: " + str(exc), file=sys.stderr)
        raise SystemExit(1)

