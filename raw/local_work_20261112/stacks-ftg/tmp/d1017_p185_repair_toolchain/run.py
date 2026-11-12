#!/usr/bin/env python3
"""Hash-verifying local launcher for the frozen D1017-R001 source pipeline."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Sequence


HERE = Path(__file__).resolve(strict=True).parent
LAUNCHER = Path(__file__).resolve(strict=True)
CONTRACT = HERE / "contract.json"
EXECUTION_TOKEN = "D1017-R001-EXPLICIT-LOCAL-EXECUTION"


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
        or value.get("schema") != "d1017-p185-repair-toolchain-contract-v1"
        or value.get("contract_id") != "D1017-R001-p185-r20-r42-sem21-v1"
        or value.get("status") != "PREPARED_NOT_EXECUTED"
        or value.get("errors") != []
    ):
        raise LaunchError("contract headline is not the frozen prepared state")
    launcher = value.get("launcher")
    if not isinstance(launcher, dict) or set(launcher) != {"path", "bytes", "sha256"}:
        raise LaunchError("contract launcher pin is absent")
    live = LAUNCHER.read_bytes()
    if (
        Path(str(launcher["path"])) != LAUNCHER
        or int(launcher["bytes"]) != len(live)
        or str(launcher["sha256"]) != digest(live)
    ):
        raise LaunchError("launcher identity drifted from contract")
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
        "__name__": f"__d1017_{key}__",
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
    parser = argparse.ArgumentParser(description="Run a frozen D1017-R001 step after exact script verification.")
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
        return execute_script(contract, "reader_v068c3r20", ["--preflight", "--pdflatex", args.pdflatex])
    if args.step == "reader-execute":
        require_write_token(args.execute_token)
        return execute_script(contract, "reader_v068c3r20", ["--execute", "--pdflatex", args.pdflatex])
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
        return execute_script(contract, "qa_v68r42", values)
    raise LaunchError("unreachable step")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise SystemExit(1)
