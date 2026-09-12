"""Pure, allowlisted public projection of a private TeX process capture.

This is not the original capture, a new execution, or an independent mutex
attestation. The exact private UTF-8 document is bound by byte count and SHA-256;
only its successful, path-free lifecycle fields are copied. Command lines,
executable names/paths, working directories, output text and filenames are never
copied. Validation does not read private files or launch any process.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone

from tex_process_guard import RECEIPT_SCHEMA, validate_capture_receipt


PUBLIC_RECEIPT_SCHEMA = "unofficial-stacks-project-ai-drafts-tex-process-tree-public/v1"
PROJECTION_KIND = "allowlisted-private-capture-lifecycle-projection"
LIFECYCLE_CONSTANTS = {
    "status": "PASS", "returncode": 0,
    "mutex": "Global\\InterlanguageTeXSlotV1", "caller_asserted_mutex_owned": True,
    "created_suspended": True, "assigned_before_resume": True, "resumed": True,
    "kill_on_close": True, "breakaway_allowed": False, "observed_empty_tree": True,
    "job_termination_requested": False,
    "empty_tree_evidence": "job_accounting_active_processes_zero",
    "handle_inheritance": "explicit stdin/stdout handles only", "failure": None,
    "cleanup_errors": [],
}
ROOT_FIELDS = {"pid", "creation_filetime_100ns"}
ACCOUNTING_FIELDS = {"active_processes", "total_processes", "total_terminated_processes"}
LIFECYCLE_FIELDS = set(LIFECYCLE_CONSTANTS) | {"root_identity", "initial_accounting", "final_accounting",
                                              "started_utc", "finished_utc"}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _integer(value, minimum=0):
    _require(type(value) is int and value >= minimum, "invalid public capture integer")
    return value


def public_capture_time(value):
    """Parse one path-free, strictly UTC lifecycle timestamp."""
    _require(type(value) is str and re.fullmatch(
        r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]{1,6})?(?:Z|\+00:00)", value),
        "invalid public capture UTC timestamp")
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    _require(result.utcoffset() == timezone.utc.utcoffset(result), "public capture timestamp is not UTC")
    return result


def _strict_json(raw_bytes):
    def pairs(items):
        value = {}
        for key, child in items:
            _require(key not in value, "duplicate private capture JSON key")
            value[key] = child
        return value
    def constant(_):
        raise ValueError("non-finite private capture JSON value")
    _require(type(raw_bytes) is bytes and len(raw_bytes) > 0, "private capture must be nonempty bytes")
    result = json.loads(raw_bytes.decode("utf-8"), object_pairs_hook=pairs, parse_constant=constant)
    _require(type(result) is dict, "private capture must be a JSON object")
    return result


def _validate_lifecycle(lifecycle):
    _require(type(lifecycle) is dict and set(lifecycle) == LIFECYCLE_FIELDS,
             "public capture lifecycle fields differ from the fixed allowlist")
    for field, expected in LIFECYCLE_CONSTANTS.items():
        _require(type(lifecycle[field]) is type(expected) and lifecycle[field] == expected,
                 "invalid public capture lifecycle field: " + field)
    _require(public_capture_time(lifecycle["started_utc"]) <= public_capture_time(lifecycle["finished_utc"]),
             "public capture lifecycle time is reversed")
    root = lifecycle["root_identity"]
    _require(type(root) is dict and set(root) == ROOT_FIELDS, "invalid public captured-root fields")
    for field in ROOT_FIELDS:
        _integer(root[field], 1)
    for field, active in (("initial_accounting", 1), ("final_accounting", 0)):
        accounting = lifecycle[field]
        _require(type(accounting) is dict and set(accounting) == ACCOUNTING_FIELDS,
                 "invalid public process-accounting fields")
        for key in ACCOUNTING_FIELDS:
            _integer(accounting[key], 1 if key == "total_processes" else 0)
        _require(accounting["active_processes"] == active, "invalid public empty-tree accounting")
    _require(lifecycle["initial_accounting"]["total_processes"] == 1
             and lifecycle["initial_accounting"]["total_terminated_processes"] == 0,
             "invalid public suspended-root initial accounting")
    _require(lifecycle["final_accounting"]["total_processes"]
             >= lifecycle["initial_accounting"]["total_processes"], "public process count decreased")
    # This transient object is an adapter for the existing pure field checks,
    # not a replacement raw receipt and is never returned or published.
    validate_capture_receipt({"schema": RECEIPT_SCHEMA, **lifecycle})


def validate_public_capture_receipt(receipt):
    """Fail closed on private fields, malformed provenance, or failed lifecycle."""
    _require(type(receipt) is dict and set(receipt) == {"schema", "status", "provenance", "lifecycle"},
             "public capture wrapper fields differ from the fixed allowlist")
    _require(receipt["schema"] == PUBLIC_RECEIPT_SCHEMA and receipt["status"] == "PASS",
             "unsupported public capture schema/status")
    provenance = receipt["provenance"]
    _require(type(provenance) is dict
             and set(provenance) == {"kind", "private_capture", "private_text_published"}
             and provenance["kind"] == PROJECTION_KIND and provenance["private_text_published"] is False,
             "invalid public capture projection provenance")
    private = provenance["private_capture"]
    _require(type(private) is dict and set(private) == {"schema", "bytes", "sha256"}
             and private["schema"] == RECEIPT_SCHEMA, "invalid private capture hash provenance")
    _integer(private["bytes"], 1)
    _require(type(private["sha256"]) is str and re.fullmatch(r"[0-9A-F]{64}", private["sha256"]),
             "invalid private capture SHA-256")
    _validate_lifecycle(receipt["lifecycle"])


def public_capture_receipt(raw_bytes):
    """Return a new path-free public projection bound to exact private bytes."""
    private = _strict_json(raw_bytes)
    validate_capture_receipt(private)
    lifecycle = {field: private[field] for field in LIFECYCLE_CONSTANTS}
    lifecycle.update({field: private[field] for field in ("started_utc", "finished_utc")})
    # Rebuild nested objects too: shallow filtering would leak arbitrary added
    # fields such as command/cwd inside root_identity or accounting objects.
    lifecycle["root_identity"] = {field: private["root_identity"][field] for field in ROOT_FIELDS}
    for phase in ("initial_accounting", "final_accounting"):
        lifecycle[phase] = {field: private[phase][field] for field in ACCOUNTING_FIELDS}
    public = {
        "schema": PUBLIC_RECEIPT_SCHEMA, "status": "PASS",
        "provenance": {"kind": PROJECTION_KIND, "private_text_published": False,
                       "private_capture": {"schema": RECEIPT_SCHEMA, "bytes": len(raw_bytes),
                                           "sha256": hashlib.sha256(raw_bytes).hexdigest().upper()}},
        "lifecycle": lifecycle,
    }
    validate_public_capture_receipt(public)
    return public


def canonical_public_capture_bytes(receipt):
    """The sole public wire encoding: sorted compact ASCII JSON followed by LF."""
    validate_public_capture_receipt(receipt)
    return (json.dumps(receipt, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
                       allow_nan=False) + "\n").encode("utf-8")
