"""Current release validation must consume the full EGA/R47 build contract."""

import unittest
from tests.test_compare_fixed_point_builds import receipt
from tools import validate_unified_repository as validator


class CurrentReleaseTests(unittest.TestCase):
    def test_current_receipts_select_r47_without_rewriting_historical_files(self):
        for name, filename in (
            ("DEFAULT_BUILD_RECEIPT", "stacks-errata-a04446e-r47-illusie-build-2026-09-07.json"),
            ("VISUAL_QA_RECEIPT", "stacks-errata-a04446e-r47-illusie-visual-qa-2026-09-07.json"),
            ("REPRODUCIBILITY_RECEIPT", "stacks-errata-a04446e-r47-illusie-reproducibility-2026-09-07.json"),
            ("SECOND_REPRODUCIBILITY_RECEIPT", "stacks-errata-a04446e-r47-illusie-repro-build-2026-09-07.json"),
            ("CURRENT_RELEASE_RECEIPT", "stacks-errata-a04446e-r47-release-2026-09-06.json"),
        ):
            self.assertEqual(str(getattr(validator, name)).replace("\\", "/"),
                             f"validation/{filename}")

    def test_valid_mutex_observation_changes_pass(self):
        errors = []
        validator.validate_reproducible_pair(receipt(), receipt(11, True), errors)
        self.assertEqual(errors, [])

    def test_source_checkpoint_drift_is_not_ignored(self):
        first, second = receipt(), receipt(11)
        second["source_checkpoint"]["protected_input_tuple_sha256"] = "9" * 64
        errors = []
        validator.validate_reproducible_pair(first, second, errors)
        self.assertTrue(any("source_checkpoint" in error for error in errors))

    def test_both_missing_checkpoint_fail_closed(self):
        first, second = receipt(), receipt(11)
        del first["source_checkpoint"]
        del second["source_checkpoint"]
        errors = []
        validator.validate_reproducible_pair(first, second, errors)
        self.assertTrue(any("source_checkpoint" in error for error in errors))

    def test_malformed_mutex_is_not_normalized_away(self):
        first, second = receipt(), receipt(11)
        second["build"]["machine_wide_tex_mutex"]["release_result"] = "not_released"
        errors = []
        validator.validate_reproducible_pair(first, second, errors)
        self.assertTrue(any("mutex" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
