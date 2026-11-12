#!/usr/bin/env python3
"""Hash-verifying local launcher for the frozen D1012-R001 steps."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Sequence


HERE = Path(__file__).resolve(strict=True).parent
CONTRACT = HERE / "contract.json"
EXECUTION_TOKEN = "D1012-R001-EXPLICIT-LOCAL-EXECUTION"


class LaunchError(RuntimeError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def load_contract() -> dict[str, Any]:
    if not CONTRACT.is_file() or CONTRACT.is_symlink() or CONTRACT.resolve(strict=True) != CONTRACT:
        raise LaunchError("contract.json is missing or redirected")
    data = CONTRACT.read_bytes()
    value = json.loads(data.decode("utf-8", errors="strict"))
    if (
        not isinstance(value, dict)
        or value.get("schema") != "d1012-p179-repair-toolchain-contract-v1"
        or value.get("contract_id") != "D1012-R001-p179-r19-r41-sem20-v1"
        or value.get("status") != "PREPARED_NOT_EXECUTED"
        or value.get("errors") != []
    ):
        raise LaunchError("contract headline is not the frozen prepared state")
    return value


def execute_script(contract: dict[str, Any], key: str, argv: Sequence[str]) -> int:
    spec = contract.get("scripts", {}).get(key)
    if not isinstance(spec, dict) or set(spec) != {"path", "bytes", "sha256"}:
        raise LaunchError(f"missing frozen script pin: {key}")
    path = Path(str(spec["path"]))
    if path.parent != HERE or path.resolve(strict=True) != path or path.is_symlink() or not path.is_file():
        raise LaunchError(f"invalid frozen script path: {key}")
    data = path.read_bytes()
    if (len(data), digest(data)) != (int(spec["bytes"]), str(spec["sha256"])):
        raise LaunchError(f"frozen script identity drifted: {key}")
    snapshot = {
        "path": str(path),
        "bytes": len(data),
        "sha256": digest(data),
        "contract": "contract_json_read_hash_then_exec_same_bytes",
    }
    namespace: dict[str, Any] = {
        "__name__": f"__d1012_{key}__",
        "__file__": str(path),
        "__package__": None,
        "__verified_script_snapshot__": snapshot,
    }
    exec(compile(data, str(path), "exec", dont_inherit=True), namespace)
    main = namespace.get("main")
    if not callable(main):
        raise LaunchError(f"frozen script lacks callable main: {key}")
    result = main(list(argv))
    if not isinstance(result, int):
        raise LaunchError(f"frozen script returned a non-integer status: {key}")
    return result


def require_write_token(value: str | None) -> None:
    if value != EXECUTION_TOKEN:
        raise LaunchError(f"mutating step requires --execute-token {EXECUTION_TOKEN}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a frozen D1012-R001 step after exact script verification.")
    parser.add_argument(
        "step",
        choices=(
            "source-preflight",
            "source-execute",
            "reader-preflight",
            "reader-execute",
            "qa-preflight",
            "qa-prepare",
            "qa-commit",
            "sem-preflight",
            "sem-execute",
        ),
    )
    parser.add_argument("--execute-token")
    parser.add_argument("--pdflatex", default=r"user\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe")
    parser.add_argument("--bindings")
    parser.add_argument("--bindings-sha256")
    parser.add_argument("--attestation")
    parser.add_argument("--attestation-sha256")
    args = parser.parse_args(sys.argv[1:] if argv is None else list(argv))
    contract = load_contract()

    if args.step == "source-preflight":
        return execute_script(contract, "source_admission", ["--preflight"])
    if args.step == "source-execute":
        require_write_token(args.execute_token)
        return execute_script(contract, "source_admission", ["--execute"])
    if args.step == "reader-preflight":
        return execute_script(contract, "reader_v068c3r19", ["--preflight", "--pdflatex", args.pdflatex])
    if args.step == "reader-execute":
        require_write_token(args.execute_token)
        return execute_script(contract, "reader_v068c3r19", ["--execute", "--pdflatex", args.pdflatex])
    if args.step in {"qa-preflight", "qa-prepare", "qa-commit"}:
        if not args.bindings or not args.bindings_sha256:
            raise LaunchError("QA steps require --bindings and --bindings-sha256")
        mode = {"qa-preflight": "--preflight", "qa-prepare": "--prepare", "qa-commit": "--commit-visual-pass"}[args.step]
        values = [mode, "--bindings", args.bindings, "--bindings-sha256", args.bindings_sha256]
        if args.step != "qa-preflight":
            require_write_token(args.execute_token)
        if args.step == "qa-commit":
            if not args.attestation or not args.attestation_sha256:
                raise LaunchError("qa-commit requires --attestation and --attestation-sha256")
            values.extend(["--attestation", args.attestation, "--attestation-sha256", args.attestation_sha256])
        return execute_script(contract, "qa_v68r41", values)
    if args.step in {"sem-preflight", "sem-execute"}:
        if not args.bindings or not args.bindings_sha256:
            raise LaunchError("semantic steps require --bindings and --bindings-sha256")
        mode = "--preflight" if args.step == "sem-preflight" else "--execute"
        if args.step == "sem-execute":
            require_write_token(args.execute_token)
        return execute_script(contract, "sem_r20", [mode, "--bindings", args.bindings, "--bindings-sha256", args.bindings_sha256])
    raise LaunchError("unreachable step")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise SystemExit(1)
