"""Offline tests for public capture projection; never launch TeX or native APIs."""
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import sys
import unittest

TOOL_ROOT = Path(os.environ.get("DIRECT_SUCCESSOR_TEST_TOOLS", str(Path(__file__).resolve().parent)))
sys.path.insert(0, str(TOOL_ROOT))
import tex_process_public_receipt as p


def encode(document):
    return (json.dumps(document, indent=2) + "\n").encode("utf-8")


def private_fixture():
    return {"schema": p.RECEIPT_SCHEMA, **deepcopy(p.LIFECYCLE_CONSTANTS),
            "started_utc": "2026-09-12T10:00:00.000001+00:00", "finished_utc": "2026-09-12T10:00:02+00:00",
            "root_identity": {"pid": 1122, "creation_filetime_100ns": 134099208000000000},
            "initial_accounting": {"active_processes": 1, "total_processes": 1, "total_terminated_processes": 0},
            "final_accounting": {"active_processes": 0, "total_processes": 2, "total_terminated_processes": 0},
            "cwd": "C:/Users/PRIVATE_MACHINE_ID/PRIVATE_WORKTREE",
            "command": ["C:/PRIVATE_TOOLCHAIN/pdflatex.exe", "PRIVATE_SOURCE_FILE.tex"],
            "resolved_executable": "C:/PRIVATE_TOOLCHAIN/pdflatex.exe",
            "stdout": "PRIVATE_OUTPUT_NAME PRIVATE_MACHINE_ID", "private_receipt_path": "PRIVATE_CAPTURE_PATH"}


class PublicCaptureTests(unittest.TestCase):
    def setUp(self):
        self.private = private_fixture()
        self.raw = encode(self.private)
        self.public = p.public_capture_receipt(self.raw)

    def test_projection_is_valid_and_exactly_binds_private_bytes(self):
        p.validate_public_capture_receipt(self.public)
        self.assertEqual(self.public["provenance"]["private_capture"],
                         {"schema": p.RECEIPT_SCHEMA, "bytes": len(self.raw),
                          "sha256": hashlib.sha256(self.raw).hexdigest().upper()})

    def test_private_paths_names_command_and_output_are_omitted(self):
        result = p.canonical_public_capture_bytes(self.public)
        for value in (b"PRIVATE_", b"pdflatex", b'"cwd":', b'"command":', b'"resolved_executable":', b'"stdout":', b"receipt_path"):
            self.assertNotIn(value, result)

    def test_required_lifecycle_fields_are_copied_exactly(self):
        for key in p.LIFECYCLE_FIELDS:
            self.assertEqual(self.public["lifecycle"][key], self.private[key])

    def test_nested_unknown_private_fields_are_not_copied(self):
        for key in ("root_identity", "initial_accounting", "final_accounting"):
            self.private[key]["private_path"] = "C:/PRIVATE_MACHINE_ID/PRIVATE_FILE"
        result = p.public_capture_receipt(encode(self.private))
        self.assertNotIn(b"PRIVATE_", p.canonical_public_capture_bytes(result))

    def test_canonical_bytes_have_one_encoding(self):
        encoded = p.canonical_public_capture_bytes(self.public)
        self.assertTrue(encoded.endswith(b"\n"))
        self.assertEqual(encoded, (json.dumps(self.public, sort_keys=True, separators=(",", ":"),
                                             ensure_ascii=True, allow_nan=False) + "\n").encode())
        self.assertEqual(encoded, p.canonical_public_capture_bytes(json.loads(encode(self.public))))

    def test_failed_raw_capture_cannot_be_projected(self):
        for field, value in (("status", "FAIL"), ("observed_empty_tree", False), ("returncode", 1),
                             ("caller_asserted_mutex_owned", False), ("cleanup_errors", ["PRIVATE_ERROR"])):
            with self.subTest(field=field):
                document = deepcopy(self.private); document[field] = value
                with self.assertRaises((ValueError, RuntimeError)):
                    p.public_capture_receipt(encode(document))

    def test_raw_schema_cannot_masquerade_as_public_projection(self):
        with self.assertRaises(ValueError):
            p.validate_public_capture_receipt(self.private)

    def test_private_field_in_any_public_object_rejected(self):
        locations = ((), ("provenance",), ("provenance", "private_capture"), ("lifecycle",),
                     ("lifecycle", "root_identity"), ("lifecycle", "initial_accounting"),
                     ("lifecycle", "final_accounting"))
        for keys in locations:
            with self.subTest(keys=keys):
                document = deepcopy(self.public); target = document
                for key in keys:
                    target = target[key]
                target["private_path"] = "PRIVATE_MACHINE_ID"
                with self.assertRaises(ValueError):
                    p.validate_public_capture_receipt(document)

    def test_private_text_in_required_scalar_rejected(self):
        for key in ("status", "mutex", "empty_tree_evidence", "handle_inheritance", "started_utc", "finished_utc"):
            with self.subTest(key=key):
                document = deepcopy(self.public); document["lifecycle"][key] = "PRIVATE_MACHINE_ID"
                with self.assertRaises(ValueError):
                    p.validate_public_capture_receipt(document)

    def test_bool_integer_confusion_rejected(self):
        paths = (("provenance", "private_capture", "bytes"), ("lifecycle", "root_identity", "pid"),
                 ("lifecycle", "initial_accounting", "active_processes"),
                 ("lifecycle", "final_accounting", "total_processes"), ("lifecycle", "returncode"))
        for keys in paths:
            with self.subTest(keys=keys):
                document = deepcopy(self.public); target = document
                for key in keys[:-1]:
                    target = target[key]
                target[keys[-1]] = True
                with self.assertRaises(ValueError):
                    p.validate_public_capture_receipt(document)

    def test_malformed_private_hash_rejected(self):
        for value in ("A" * 63, "a" * 64, "PRIVATE_MACHINE_ID", 123):
            with self.subTest(value=value):
                document = deepcopy(self.public); document["provenance"]["private_capture"]["sha256"] = value
                with self.assertRaises(ValueError):
                    p.validate_public_capture_receipt(document)

    def test_missing_lifecycle_or_provenance_field_rejected(self):
        for field in ("lifecycle", "provenance"):
            document = deepcopy(self.public); document.pop(field)
            with self.assertRaises(ValueError):
                p.validate_public_capture_receipt(document)

    def test_invalid_or_reversed_utc_time_rejected(self):
        for value in ("2026-09-12T10:00:03Z", "2026-09-12T10:00:00+01:00", "2026-99-12T10:00:00Z",
                      "2026-09-12T10:00:00Z PRIVATE_MACHINE_ID", 4):
            with self.subTest(value=value):
                document = deepcopy(self.public); document["lifecycle"]["started_utc"] = value
                with self.assertRaises(ValueError):
                    p.validate_public_capture_receipt(document)

    def test_duplicate_json_key_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            p.public_capture_receipt(b'{"schema":"one","schema":"two"}')

    def test_nonfinite_json_value_rejected_even_if_private(self):
        with self.assertRaisesRegex(ValueError, "non-finite"):
            p.public_capture_receipt(b'{"private":NaN}')

    def test_non_utf8_or_non_bytes_input_rejected(self):
        for value in (b"\xff", "{}", b"", b"[]"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    p.public_capture_receipt(value)

    def test_projection_has_no_references_into_input(self):
        other = p.public_capture_receipt(self.raw)
        other["lifecycle"]["root_identity"]["pid"] = 2000
        self.assertEqual(self.public["lifecycle"]["root_identity"]["pid"], 1122)


if __name__ == "__main__":
    unittest.main()
