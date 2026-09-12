"""Tiny deterministic PDF fixtures only: no TeX, render, Git mutation or network."""

import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

from pypdf import PdfWriter

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import package_direct_successor_pdfs as pack
import validate_direct_successor_release as release
import validate_unified_repository as unified


class PdfPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="stacks-r48-package-test-")
        self.root = Path(self.temp.name)
        self.build_root = self.root / "build"
        self.build_root.mkdir()
        self.receipt_path = self.root / "private-build.json"
        self.public_path = "validation/direct-successor-r48-build-a.json"
        self.source_commit, self.content_commit, self.tree = "1" * 40, "2" * 40, "3" * 40
        writer = PdfWriter()
        writer.add_blank_page(width=300, height=400)
        output = io.BytesIO()
        writer.write(output)
        self.pdf = output.getvalue()
        diagnostics = {key: 0 for key in release.DIAGNOSTICS}
        artifacts = []
        for stem in pack.R48_STEMS:
            (self.build_root / (stem + ".pdf")).write_bytes(self.pdf)
            artifacts.append({"stem": stem, "pages": 1,
                              **{k: pack.identity(self.pdf)[k] for k in ("bytes", "sha256")},
                              "diagnostics": diagnostics.copy(),
                              "external_references": {"count": 0, "sha256": "A" * 64}})
        mutex = {"schema": unified.TEX_MUTEX_RECEIPT_SCHEMA, "status": "PASS",
                 "name": unified.TEX_MUTEX_NAME, "namespace": "Windows Global",
                 "acquisition_timeout_ms": unified.TEX_MUTEX_TIMEOUT_MS,
                 "wait_started_utc": "2026-09-12T10:00:00Z", "acquired_utc": "2026-09-12T10:00:01Z",
                 "wait_duration_ms": 1000.0, "wait_result_code": "0x00000000", "wait_result": "acquired",
                 "abandoned_mutex_recovered": False, "ownership_acquired": True,
                 "held_scope": unified.TEX_MUTEX_HELD_SCOPE, "released_utc": "2026-09-12T10:00:03Z",
                 "held_duration_ms": 2000.0, "release_result": "released_in_finally"}
        binding = {"schema": pack.DIRECT_SCHEMA, "authority_commit": pack.AUTHORITY,
                   "authority_tree": pack.AUTHORITY_TREE, "new_overlay_ids": [pack.R48],
                   "last_admitted_overlay": pack.R48, "required_build_stems": list(pack.R48_STEMS),
                   "affected_source_stems": sorted(pack.DIRECT_PDFS),
                   "composition_source_commit": "4" * 40, "registry_cutoff_commit": "5" * 40}
        self.receipt = {"schema": "unofficial-ai-integrated-stacks-fixed-point-build/v1", "status": "PASS",
                        "source": {"commit": self.source_commit, "tree": self.tree},
                        "composition": binding, "pdfs_committed": False,
                        "environment": {"private_path": "C:/Users/PRIVATE-SENTINEL/raw"},
                        "build": {"strategy": "sequential-prime-bibtex-global-state-sweeps",
                                  "fixed_point_suffixes": list(release.SUFFIXES),
                                  "stem_selection": "composition_receipt", "stems": list(pack.R48_STEMS),
                                  "chapter_count": 36, "pdfinfo_readable": 36, "worktree_kind": "linked",
                                  "primary_worktree_override": False, "global_fixed_point_sweep": 2,
                                  "machine_wide_tex_mutex": mutex, "diagnostics": diagnostics,
                                  "artifact_tuple_set_sha256": release.tuple_hash(artifacts)},
                        "artifacts": artifacts, "private_logs": "C:/Users/PRIVATE-SENTINEL/secrets"}
        self.write_receipt()
        self.objects = mock.Mock()
        self.objects.commit.side_effect = lambda value: value
        self.objects.blob.side_effect = lambda commit, path: self.receipt_path.read_bytes()
        self.patch = mock.patch.object(pack, "Objects", return_value=self.objects)
        self.patch.start()

    def tearDown(self):
        self.patch.stop()
        self.temp.cleanup()

    def write_receipt(self):
        self.receipt_path.write_bytes(pack.canonical_json(self.receipt))

    def run_package(self, name="package"):
        return pack.package(self.root, self.build_root, self.receipt_path,
                            self.root / name, self.content_commit, self.public_path)

    def test_deterministic_complete_and_public_only(self):
        first = self.run_package("a")
        second = self.run_package("b")
        self.assertEqual(first, second)
        self.assertEqual(first["upload_asset_count"], 5)
        self.assertEqual(first["pdfs_checked"], 36)
        self.assertEqual(first["zip_members_checked"], 38)
        for row in first["upload_assets"]:
            left = (self.root / "a" / row["name"]).read_bytes()
            self.assertEqual(left, (self.root / "b" / row["name"]).read_bytes())
            self.assertEqual(pack.identity(left)["sha256"], row["sha256"])
        with zipfile.ZipFile(self.root / "a" / pack.ZIP_NAME) as archive:
            self.assertEqual(len(archive.namelist()), 38)
            for name in archive.namelist():
                self.assertNotIn(b"PRIVATE-SENTINEL", archive.read(name))
            manifest = json.loads(archive.read(pack.MANIFEST_NAME))
            self.assertIn(self.content_commit, manifest["build_receipt"]["url"])
            self.assertIn(self.source_commit, manifest["source"]["url"])
        assets = {row["name"]: row for row in first["upload_assets"]}
        self.assertEqual(set(assets[pack.ZIP_NAME]["pdf_members"].values()), set(pack.R48_STEMS))
        for stem in pack.DIRECT_PDFS:
            self.assertEqual(assets[stem + ".pdf"]["pdf_stem"], stem)
            self.assertEqual((self.root / "a" / (stem + ".pdf")).read_bytes(), self.pdf)
        self.objects.raw.assert_called_with("merge-base", "--is-ancestor", self.source_commit, self.content_commit)

    def test_existing_output_refused_unchanged(self):
        path = self.root / "package"
        path.mkdir()
        (path / "keep").write_text("keep")
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.run_package()
        self.assertEqual((path / "keep").read_text(), "keep")

    def test_size_hash_page_count_drift_refused_before_output(self):
        for kind in ("bytes", "sha256", "pages"):
            with self.subTest(kind=kind):
                original = copy.deepcopy(self.receipt)
                row = self.receipt["artifacts"][0]
                row[kind] = "B" * 64 if kind == "sha256" else row[kind] + 1
                self.receipt["build"]["artifact_tuple_set_sha256"] = release.tuple_hash(self.receipt["artifacts"])
                self.write_receipt()
                with self.assertRaises(ValueError):
                    self.run_package()
                self.assertFalse((self.root / "package").exists())
                self.receipt = original

    def test_partial_duplicate_unsafe_wrong_scope_refused(self):
        changes = [("status", "PASS_PARTIAL"), ("duplicate", None), ("unsafe", None),
                   ("scope", None), ("tuple", None)]
        for kind, value in changes:
            with self.subTest(kind=kind):
                original = copy.deepcopy(self.receipt)
                if kind == "status":
                    self.receipt["status"] = value
                elif kind in ("duplicate", "unsafe"):
                    self.receipt["artifacts"][1]["stem"] = "sets" if kind == "duplicate" else "../secret"
                elif kind == "scope":
                    self.receipt["composition"]["new_overlay_ids"] = ["stacks-errata-a04446e-r49"]
                else:
                    self.receipt["build"]["artifact_tuple_set_sha256"] = "B" * 64
                self.write_receipt()
                with self.assertRaises(ValueError):
                    self.run_package()
                self.assertFalse((self.root / "package").exists())
                self.receipt = original

    def test_wrong_committed_receipt_refused(self):
        self.objects.blob.side_effect = None
        self.objects.blob.return_value = b"different"
        with self.assertRaisesRegex(ValueError, "Git blob"):
            self.run_package()
        self.assertFalse((self.root / "package").exists())

    def test_wrong_git_ancestry_refused(self):
        self.objects.raw.side_effect = ValueError("not an ancestor")
        with self.assertRaisesRegex(ValueError, "ancestor"):
            self.run_package()
        self.assertFalse((self.root / "package").exists())

    def test_malformed_pdf_and_extra_zip_members_refused(self):
        bad = b"%PDF-1.7\nnot a real PDF\n%%EOF\n"
        expected = {"bytes": len(bad), "sha256": pack.identity(bad)["sha256"], "pages": 1}
        with self.assertRaises(Exception):
            pack.check_pdf(bad, expected, "fixture")
        members = {"public.txt": b"ok"}
        archive_path = self.root / "bad.zip"
        pack.write_zip(archive_path, {**members, "private.log": b"private"})
        with self.assertRaisesRegex(ValueError, "unexpected members"):
            pack.verify_zip(archive_path, members, {}, {})

    def test_duplicate_json_keys_and_bad_public_path_refused(self):
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            pack.build_inputs(b'{"status":"PASS","status":"PASS"}', self.public_path)
        with self.assertRaises(ValueError):
            pack.build_inputs(self.receipt_path.read_bytes(), "C:/Users/private/receipt.json")


if __name__ == "__main__":
    unittest.main()
