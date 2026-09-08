"""R47 mapping, direct-inspection closure, and simulated mutex tests; no TeX."""
from __future__ import annotations

import copy
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest import mock

from tools import instrument_r47_synctex as instrumenter
from tools import map_r47_visual_qa as mapping
from tools import write_r47_visual_qa_receipt as visual


class FakeMutex:
    def __init__(self, fail=False):
        self.owned = False
        self.fail = fail
        self.exits = 0

    def __enter__(self):
        if self.fail:
            raise RuntimeError("mutex acquisition failed")
        self.owned = True
        return self

    def __exit__(self, *args):
        self.owned = False
        self.exits += 1

    def receipt_details(self):
        if self.owned or not self.exits:
            raise AssertionError("mutex receipt before finally release")
        return {"status": "PASS", "released": True}


class InstrumentationTests(unittest.TestCase):
    def exercise(self, *, drift=False, acquire_fail=False, process_fail=False, missing_sidecar=False):
        source = Path("test-source")
        mutex = FakeMutex(acquire_fail)
        frozen = {"bytes": 1, "sha256": "A" * 64}
        generated, runs = {}, []
        clock = {"now": 0}
        build = {"source": {"commit": "a" * 40}, "build": {"stems": list(mapping.STEMS)},
                 "environment": {"source_date_epoch": "1785270512"}}
        artifacts = {stem: {**frozen, "diagnostics": {}, "external_references": {}}
                     for stem in mapping.STEMS}

        def now():
            clock["now"] += 100
            return clock["now"]

        def exists(path):
            return path.name.removesuffix(".synctex.gz") in generated

        def snapshot(root, stem):
            value = {f"{stem}.pdf": frozen, f"{stem}.aux": frozen}
            if drift and runs and stem == mapping.STEMS[0]:
                value[f"{stem}.aux"] = {"bytes": 2, "sha256": "B" * 64}
            return copy.deepcopy(value)

        def run(command, root, env, owner):
            self.assertIs(owner, mutex)
            self.assertTrue(owner.owned)
            self.assertEqual(root, source)
            self.assertEqual(env["FORCE_SOURCE_DATE"], "1")
            self.assertEqual(command[:5], ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                                           "-file-line-error", "-synctex=1"])
            runs.append(command[-1])
            if process_fail:
                raise RuntimeError("simulated TeX failure")
            if not missing_sidecar:
                generated[Path(command[-1]).stem] = clock["now"] + 1

        def diagnostics(*args):
            self.assertTrue(mutex.owned)
            return {}, {}

        with ExitStack() as stack:
            factory = stack.enter_context(mock.patch.object(instrumenter.builder, "WindowsNamedMutex", return_value=mutex))
            stack.enter_context(mock.patch.object(mapping, "git", return_value="a" * 40))
            stack.enter_context(mock.patch.object(mapping, "fixed_snapshot", side_effect=snapshot))
            stack.enter_context(mock.patch.object(mapping, "identity", return_value=frozen))
            stack.enter_context(mock.patch.object(mapping, "recheck_inputs"))
            stack.enter_context(mock.patch.object(instrumenter.builder, "external_reference_labels", return_value={}))
            stack.enter_context(mock.patch.object(instrumenter.builder, "run", side_effect=run))
            stack.enter_context(mock.patch.object(instrumenter.builder, "scan_tex_diagnostics", side_effect=diagnostics))
            stack.enter_context(mock.patch.object(instrumenter.time, "time_ns", side_effect=now))
            stack.enter_context(mock.patch.object(Path, "exists", autospec=True, side_effect=exists))
            stack.enter_context(mock.patch.object(Path, "is_file", autospec=True, side_effect=exists))
            def sidecar_stat(path):
                return SimpleNamespace(st_size=1,
                                       st_mtime_ns=generated[path.name.removesuffix(".synctex.gz")])
            stack.enter_context(mock.patch.object(Path, "stat", autospec=True, side_effect=sidecar_stat))
            try:
                result = instrumenter.instrument(build, artifacts, source, [])
            except (ValueError, RuntimeError):
                self.assertFalse(mutex.owned)
                if acquire_fail:
                    self.assertEqual(runs, [])
                else:
                    self.assertEqual(mutex.exits, 1)
                raise
            factory.assert_called_once_with(instrumenter.builder.TEX_MUTEX_NAME,
                                            instrumenter.builder.TEX_MUTEX_TIMEOUT_MS)
            self.assertEqual(runs, [f"{stem}.tex" for stem in mapping.STEMS])
            self.assertEqual(mutex.exits, 1)
            return result

    def test_exactly_five_passes_share_one_mutex_through_immediate_checks(self):
        rows, mutex = self.exercise()
        self.assertEqual(len(rows), 5)
        self.assertTrue(mutex["released"])
        self.assertTrue(all(row["tex_mutex_owned_through_immediate_checks"] for row in rows))

    def test_acquisition_failure_launches_nothing(self):
        with self.assertRaisesRegex(RuntimeError, "acquisition failed"):
            self.exercise(acquire_fail=True)

    def test_process_failure_releases_mutex(self):
        with self.assertRaisesRegex(RuntimeError, "TeX failure"):
            self.exercise(process_fail=True)

    def test_any_auxiliary_drift_fails_and_releases_mutex(self):
        with self.assertRaisesRegex(ValueError, "fixed-point bytes changed"):
            self.exercise(drift=True)

    def test_missing_fresh_sidecar_fails_and_releases_mutex(self):
        with self.assertRaisesRegex(ValueError, "SyncTeX missing"):
            self.exercise(missing_sidecar=True)


class MappingTests(unittest.TestCase):
    def operation(self, old="X", new="long"):
        return {"operation_id": "MC-STK-ERR-1402-OP1", "stable_id": "MC-STK-ERR-1402",
                "round": 40, "start_byte": 2, "end_byte_exclusive": 3,
                "old_text": old, "replacement_text": new,
                "source_start_line": 1, "source_end_line": 1}

    def test_cumulative_replay_preserves_prior_prefix_addition(self):
        authority = b"A X\nB Y\n"
        before, after = b"prior\n" + authority, b"prior\nA long\nB Y\n"
        with mock.patch.dict(mapping.EXPECTED_APPLIED, {"descent": 1}):
            rows = mapping.cumulative_operations(authority, before, after, [self.operation()], "descent.tex", "a" * 40)
        self.assertEqual(rows[0]["start_byte"], 8)
        self.assertEqual(rows[0]["authority_start_byte"], 2)

    def test_no_preapplied_or_unproved_noop_is_permitted(self):
        authority, already = b"A X\nB Y\n", b"A long\nB Y\n"
        with mock.patch.dict(mapping.EXPECTED_APPLIED, {"descent": 1}):
            with self.assertRaisesRegex(ValueError, "cumulative replay mismatch"):
                mapping.cumulative_operations(authority, already, already, [self.operation()], "descent.tex", "a" * 40)

    def test_replay_postimage_drift_rejected(self):
        authority = b"A X\nB Y\n"
        with mock.patch.dict(mapping.EXPECTED_APPLIED, {"descent": 1}):
            with self.assertRaisesRegex(ValueError, "cumulative replay mismatch"):
                mapping.cumulative_operations(authority, authority, b"wrong", [self.operation()], "descent.tex", "a" * 40)

    def test_mapping_binds_complete_line_interval_and_deduplicates_queries(self):
        row = {**self.operation(), "authority_start_byte": 2}
        cache = {}
        with mock.patch.object(mapping, "synctex_pages", return_value=[3]) as query:
            mapped = mapping.mapped_operation(row, [row], b"A long\nB Y\n", Path("repo"), "descent.tex", 4, cache)
            repeated = mapping.mapped_operation(row, [row], b"A long\nB Y\n", Path("repo"), "descent.tex", 4, cache)
        query.assert_called_once()
        self.assertEqual(mapped, repeated)
        self.assertEqual(mapped["pages"], [3])
        self.assertEqual(mapped["final_source_lines"], [{"line": 1, "text": "A long", "pages": [3]}])

    def test_out_of_range_page_and_wrong_final_bytes_fail(self):
        row = {**self.operation(), "authority_start_byte": 2}
        with mock.patch.object(mapping, "synctex_pages", return_value=[5]):
            with self.assertRaisesRegex(ValueError, "outside PDF"):
                mapping.mapped_operation(row, [row], b"A long\n", Path("repo"), "descent.tex", 4, {})
        with self.assertRaisesRegex(ValueError, "replacement"):
            mapping.mapped_operation(row, [row], b"A wrong\n", Path("repo"), "descent.tex", 4, {})

    def test_deletion_maps_exact_surviving_context_instead_of_disappearing(self):
        row = {**self.operation(new=""), "authority_start_byte": 2}
        with mock.patch.object(mapping, "synctex_pages", return_value=[3]):
            result = mapping.mapped_operation(row, [row], b"A \nB Y\n", Path("repo"), "descent.tex", 4, {})
        self.assertTrue(result["deletion"])
        self.assertEqual(result["replacement_bytes"], 0)
        self.assertEqual(result["final_start_byte"], result["final_end_byte_exclusive"])
        self.assertEqual(result["deleted_text"], "X")
        self.assertEqual(result["deletion_context"]["text"], "A \nB Y\n")
        self.assertEqual([row["line"] for row in result["final_source_lines"]], [1, 2])
        self.assertEqual(result["pages"], [3])

    def test_source_map_profile_is_exact_five_sources_177_edits(self):
        self.assertEqual(sum(mapping.EXPECTED_APPLIED.values()), 177)
        self.assertEqual(set(mapping.EXPECTED_APPLIED), set(mapping.STEMS))
        self.assertEqual(mapping.ROUNDS, tuple(range(40, 48)))

    def test_unsafe_evidence_path_rejected(self):
        for path in ("../source", "/source", "C:/source", "a\\b"):
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, "unsafe"):
                mapping.safe_path(path)

    def test_capture_times_must_be_sequential_inside_the_same_mutex(self):
        mutex = {"acquired_utc": "1970-01-01T00:00:01Z", "released_utc": "1970-01-01T00:00:03Z"}
        rows = [{"started_ns": 1_100_000_000, "synctex_mtime_ns": 1_200_000_000,
                 "completed_ns": 1_300_000_000},
                {"started_ns": 2_100_000_000, "synctex_mtime_ns": 2_200_000_000,
                 "completed_ns": 2_300_000_000}]
        mapping.validate_capture_window(mutex, rows)
        for key, value in (("started_ns", 900_000_000), ("started_ns", 1_250_000_000),
                           ("completed_ns", 4_000_000_000), ("synctex_mtime_ns", True)):
            with self.subTest(key=key, value=value):
                changed = copy.deepcopy(rows)
                changed[1][key] = value
                with self.assertRaisesRegex(ValueError, "one recorded mutex window"):
                    mapping.validate_capture_window(mutex, changed)


class InspectionTests(unittest.TestCase):
    def setUp(self):
        self.expected = {"image": {"bytes": 1, "sha256": "A" * 64},
                         "pages": [2], "locus_ids": ["MC-STK-ERR-1402-OP1"]}
        self.row = {"kind": "high_resolution", "result": "PASS", "observations": "Formula is legible.",
                    "image": dict(self.expected["image"]), "pages": [2],
                    "checks": {key: True for key in visual.HIGH_RESOLUTION_CHECKS},
                    "defects": {key: 0 for key in visual.DEFECTS},
                    "locus_checks": [{"operation_id": "MC-STK-ERR-1402-OP1", "result": "PASS",
                                      "observations": "The accepted replacement is visible."}]}

    def test_completed_hash_bound_observation_passes(self):
        self.assertEqual(visual.validate_inspection(self.row, self.expected, "sample"), 1)

    def test_missing_or_duplicate_locus_observation_fails(self):
        for rows in ([], self.row["locus_checks"] * 2):
            with self.subTest(rows=rows):
                candidate = {**self.row, "locus_checks": rows}
                with self.assertRaisesRegex(ValueError, "operation-level inspection"):
                    visual.validate_inspection(candidate, self.expected, "sample")

    def test_stale_image_wrong_page_or_missing_observation_fails(self):
        for key, value in (("image", {"bytes": 2, "sha256": "A" * 64}),
                           ("pages", [1]), ("observations", ""), ("result", "PENDING")):
            with self.subTest(key=key), self.assertRaises(ValueError):
                visual.validate_inspection({**self.row, key: value}, self.expected, "sample")

    def test_failed_check_nonzero_defect_and_boolean_defect_fail(self):
        for value in (1, True):
            candidate = copy.deepcopy(self.row)
            candidate["defects"][visual.DEFECTS[0]] = value
            with self.assertRaisesRegex(ValueError, "defect"):
                visual.validate_inspection(candidate, self.expected, "sample")
        candidate = copy.deepcopy(self.row)
        candidate["checks"][visual.HIGH_RESOLUTION_CHECKS[0]] = False
        with self.assertRaisesRegex(ValueError, "direct-inspection check"):
            visual.validate_inspection(candidate, self.expected, "sample")

    def test_missing_entire_ledger_never_becomes_pass(self):
        with self.assertRaisesRegex(ValueError, "missing or duplicate ledger"):
            visual.validate_ledgers([], {}, {}, {}, visual.Evidence())


class LedgerCoverageTests(unittest.TestCase):
    def setUp(self):
        self.path = Path("test-ledger.json")
        self.build = {"source": {"commit": "a" * 40, "tree": "b" * 40}}
        self.page_map = {"bytes": 1, "sha256": "C" * 64}
        self.rendered, rows = {}, []
        for number, stem in enumerate(mapping.STEMS):
            image = {"bytes": number + 1, "sha256": "D" * 64}
            op_id = f"MC-STK-ERR-{1402 + number}-OP1"
            images = {}
            for kind, file, checks, ids in (
                ("contact_sheet", f"contact-sheets/{stem}_01.png", visual.CONTACT_CHECKS, []),
                ("high_resolution", f"high-resolution/{stem}_p1.png", visual.HIGH_RESOLUTION_CHECKS, [op_id]),
            ):
                images[(stem, kind, file)] = {"image": image, "pages": [1], "locus_ids": ids}
                rows.append({"stem": stem, "kind": kind, "file": file, "image": image, "pages": [1],
                    "result": "PASS", "observations": "Test fixture observation.",
                    "checks": {key: True for key in checks}, "defects": {key: 0 for key in visual.DEFECTS},
                    "locus_checks": [{"operation_id": op, "result": "PASS", "observations": "Test locus."}
                                     for op in ids]})
            self.rendered[stem] = {"images": images, "artifact": {"pages": 1},
                                   "manifest": {"bytes": 1, "sha256": "E" * 64}}
        self.ledger = {"schema": visual.LEDGER_SCHEMA, "status": "COMPLETE",
            "inspection_method": "direct_image_inspection", "reviewer": "test-fixture",
            "source": self.build["source"], "page_map_sha256": self.page_map["sha256"],
            "inspections": rows, "render_manifests": {s: r["manifest"] for s, r in self.rendered.items()}}
        self.evidence = mock.Mock()
        self.evidence.json.side_effect = lambda path: self.ledger
        self.evidence.bind.return_value = {"bytes": 1, "sha256": "F" * 64}

    def validate(self):
        return visual.validate_ledgers([self.path], self.build, self.page_map, self.rendered, self.evidence)

    def test_every_contact_sheet_and_every_mapped_locus_are_covered(self):
        result = self.validate()
        self.assertEqual(result["inspection_count"], 10)
        self.assertEqual(result["locus_check_count"], 5)
        self.assertEqual(result["contact_pages"], {s: {1} for s in mapping.STEMS})

    def test_missing_one_contact_or_high_resolution_image_fails(self):
        original = list(self.ledger["inspections"])
        for index in (0, 1):
            self.ledger["inspections"] = original[:index] + original[index + 1:]
            with self.subTest(index=index), self.assertRaisesRegex(ValueError, "missing completed image inspections"):
                self.validate()

    def test_duplicate_image_inspection_fails(self):
        self.ledger["inspections"].append(self.ledger["inspections"][0])
        with self.assertRaisesRegex(ValueError, "duplicate/conflicting inspection"):
            self.validate()

    def test_stale_render_manifest_or_page_map_fails(self):
        self.ledger["render_manifests"] = copy.deepcopy(self.ledger["render_manifests"])
        self.ledger["render_manifests"][mapping.STEMS[0]]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "identity mismatch"):
            self.validate()
        self.ledger["page_map_sha256"] = "1" * 64
        with self.assertRaisesRegex(ValueError, "different build or page map"):
            self.validate()


if __name__ == "__main__":
    unittest.main()
