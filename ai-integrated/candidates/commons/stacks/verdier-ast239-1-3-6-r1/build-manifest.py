from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "candidate.manifest.json"
SINGLED = {
    "stable_unit_manifest": "stable-units.json",
    "source_map": "source-map.jsonl",
    "decision_ledger": "decisions.jsonl",
    "rejection_ledger": "rejections.jsonl",
    "formula_diagram_inventory": "formula-diagram-inventory.json",
}
REQUIRED_RECEIPTS = (
    "builds/build-receipt.json",
    "builds/validation.json",
    "builds/visual-qa.json",
    "builds/tex-mutex.json",
)


class ManifestBuildError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ManifestBuildError(message)


def ai_root() -> Path:
    for directory in ROOT.parents:
        if (
            (directory / "schemas" / "candidate-manifest.schema.json").is_file()
            and (directory / "registry" / "leases.json").is_file()
            and (directory / "upstream" / "stacks.lock.json").is_file()
        ):
            return directory.resolve()
    raise ManifestBuildError("cannot resolve the bounded ai-integrated root")


AI_ROOT = ai_root()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ManifestBuildError(f"cannot parse {path.name}: {exc}") from exc
    require(isinstance(value, dict), f"{path.name} must contain one JSON object")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        raise ManifestBuildError(f"cannot read {path.name}: {exc}") from exc
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ManifestBuildError(f"invalid JSONL at {path.name}:{number}: {exc}") from exc
        require(isinstance(row, dict), f"non-object JSONL row at {path.name}:{number}")
        rows.append(row)
    return rows


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def evidence(path: Path) -> dict[str, str]:
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256(path)}


def public_files() -> list[Path]:
    files: list[Path] = []
    stack = [ROOT]
    while stack:
        directory = stack.pop()
        with os.scandir(directory) as entries:
            ordered = sorted(entries, key=lambda entry: entry.name)
        for entry in ordered:
            if entry.is_dir(follow_symlinks=False):
                if entry.name in {".work", ".git", "__pycache__"}:
                    continue
                stack.append(Path(entry.path))
            elif entry.is_file(follow_symlinks=False):
                path = Path(entry.path)
                if path.name != MANIFEST.name:
                    files.append(path)
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def timestamp_values(value: Any) -> Iterable[datetime]:
    if isinstance(value, dict):
        for key, child in value.items():
            if isinstance(child, str) and (key.endswith("_utc") or key in {"recorded_at", "generated_at"}):
                try:
                    parsed = datetime.fromisoformat(child.replace("Z", "+00:00"))
                except ValueError:
                    pass
                else:
                    if parsed.tzinfo is not None:
                        yield parsed.astimezone(timezone.utc)
            yield from timestamp_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from timestamp_values(child)


def deterministic_timestamp(objects: list[Any]) -> str:
    values = [stamp for obj in objects for stamp in timestamp_values(obj)]
    require(values, "no timestamp is available to date the manifest")
    return max(values).isoformat(timespec="microseconds").replace("+00:00", "Z")


def main() -> int:
    try:
        verified = subprocess.run(
            [sys.executable, "-B", str(ROOT / "verify.py"), "--skip-manifest-check"],
            cwd=ROOT,
            stdin=subprocess.DEVNULL,
            check=False,
        )
        require(verified.returncode == 0, "candidate verifier failed before manifest sealing")

        config = load_json(ROOT / "candidate.config.json")
        pointer = load_json(ROOT / "LEASE.json")
        stable = load_json(ROOT / "stable-units.json")
        source_map = load_jsonl(ROOT / "source-map.jsonl")
        inventory = load_json(ROOT / "formula-diagram-inventory.json")
        decisions = load_jsonl(ROOT / "decisions.jsonl")
        rejections = load_jsonl(ROOT / "rejections.jsonl")
        expected_ids = config.get("expected_unit_ids")
        require(isinstance(expected_ids, list) and expected_ids, "config has no expected stable-unit IDs")
        count = len(expected_ids)
        units = stable.get("units")
        require(isinstance(units, list) and [row.get("id") for row in units] == expected_ids, "stable units do not match config order")
        require(stable.get("unit_count") == len(source_map) == count, "unit/source-map count mismatch")
        require(inventory.get("unit_count") == inventory.get("classified_unit_count") == count, "formula inventory count mismatch")
        closure = config.get("source_closure")
        require(isinstance(closure, dict) and closure.get("complete") is True, "source closure is not complete")
        require(closure.get("expected_units") == closure.get("manifested_units") == count, "source closure count mismatch")

        receipts: list[dict[str, Any]] = []
        for relative in REQUIRED_RECEIPTS:
            receipt = load_json(ROOT / relative)
            require(receipt.get("passed") is True and receipt.get("status") == "PASS", f"nonpassing receipt: {relative}")
            receipts.append(receipt)
        mutex = receipts[-1]
        require(mutex.get("acquired") is True and mutex.get("released") is True, "TeX mutex was not acquired and released")
        require(mutex.get("captured_child_exit_code") == 0, "TeX child did not exit successfully")

        review_state = config.get("review_state")
        replay_state = config.get("independent_replay")
        require(review_state in {"partial", "performed"}, "candidate review state is not sealable")
        require(replay_state in {"not_performed", "passed", "failed"}, "candidate replay state is invalid")
        replay_path = ROOT / "replay" / "independent-review.json"
        replay: dict[str, Any] | None = load_json(replay_path) if replay_path.exists() else None
        if replay is None:
            require(review_state == "partial" and replay_state == "not_performed", "absent replay is overstated")
            unresolved = ["Independent frozen-candidate replay has not yet been performed."]
        else:
            passed = replay.get("passed") is True and replay.get("status") == "PASS"
            require(review_state == "performed", "present replay requires performed review")
            require(replay_state == ("passed" if passed else "failed"), "replay/config state mismatch")
            unresolved = [] if passed else ["Independent replay failed; admission and composition are prohibited."]

        files = public_files()
        relative_files = {path.relative_to(ROOT).as_posix(): path for path in files}
        for relative in [*SINGLED.values(), *REQUIRED_RECEIPTS, "authority/authority.lock.json"]:
            require(relative in relative_files, f"required candidate file is absent: {relative}")
        singled_paths = set(SINGLED.values())
        authorities = [evidence(path) for relative, path in relative_files.items() if relative.startswith("authority/")]
        builds = [
            evidence(path)
            for relative, path in relative_files.items()
            if relative not in singled_paths and not relative.startswith("authority/")
        ]
        require(authorities and builds, "manifest evidence groups are empty")

        timestamp_objects: list[Any] = [config, *receipts, decisions, rejections]
        if replay is not None:
            timestamp_objects.append(replay)
        manifest = {
            "$schema": Path(os.path.relpath(AI_ROOT / "schemas" / "candidate-manifest.schema.json", ROOT)).as_posix(),
            "schema": "mathematics-commons-stacks-candidate-manifest/v1",
            "candidate_id": config["candidate_id"],
            "lease_id": pointer["lease_id"],
            "namespace": pointer["namespace"],
            "writer_task": pointer["writer_task"],
            "upstream": {
                "lock": "upstream/stacks.lock.json",
                "commit": config["upstream"]["commit"],
                "tree": config["upstream"]["tree"],
            },
            "source_authorities": authorities,
            "source_closure": {"enumerated": True, "expected_units": count, "manifested_units": count, "complete": True},
            **{key: evidence(ROOT / relative) for key, relative in SINGLED.items()},
            "builds": builds,
            "rights_state": "Source locators and hashes only; payload independently worded; no source relicense asserted; GFDL compatibility required at composition.",
            "review_state": review_state,
            "independent_replay": replay_state,
            "unresolved_defects": unresolved,
            "stop_conditions": ["Do not admit or compose unless manifest closure, deterministic validators, build, visual QA, and independent replay all pass."],
            "generated_at_utc": deterministic_timestamp(timestamp_objects),
        }
        MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        checked = subprocess.run([sys.executable, "-B", str(ROOT / "check-manifest.py")], cwd=ROOT, check=False)
        require(checked.returncode == 0, "generated manifest failed closure checking")
        print(json.dumps({"passed": True, "references": len(authorities) + len(builds) + len(SINGLED), "stable_units": count, "manifest_sha256": sha256(MANIFEST)}, sort_keys=True))
        return 0
    except (ManifestBuildError, OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"MANIFEST BUILD FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
