"""Evidence-retention and exact replay failures, not mathematical proof tests."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from test_sites_intake_replay_20260923 import ReplayTests
from verify_stacks_intake_review_20260924 import HERE, verify_proof_evidence, verify_structure


class ProofRetentionTests(unittest.TestCase):
    def setUp(self):
        self.review = json.loads((HERE / 'STACKS_INTAKE_REVIEW_20260923.json').read_bytes())
        self.temp = tempfile.TemporaryDirectory(prefix='stacks-proof-retention-')
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        for row in self.review['required_proof_evidence']:
            shutil.copyfile(HERE / row['path'], self.directory / row['path'])

    def check(self, review=None):
        verify_proof_evidence(self.review if review is None else review, self.directory)

    def test_complete_evidence_passes(self):
        self.check()

    def test_completion_flag_cannot_replace_missing_proofs(self):
        self.review['required_proof_evidence'] = []
        with self.assertRaisesRegex(ValueError, 'missing or duplicated'):
            self.check()

    def test_changed_derivation_rejected(self):
        target = self.directory / 'LOCALIZED_CARTESIAN_DERIVATION_20260924.md'
        target.write_bytes(target.read_bytes() + b'changed')
        with self.assertRaisesRegex(ValueError, 'evidence changed'):
            self.check()

    def test_omitted_source_proof_rejected_even_with_intact_receipts(self):
        self.review['groups'][-1]['operations'][-1]['replacement_text'] = 'Proof omitted.'
        with self.assertRaisesRegex(ValueError, 'checked complete proof'):
            self.check()

    def test_removed_required_proof_link_rejected(self):
        self.review['groups'][-1]['proof_evidence']['required_in_candidate'] = False
        with self.assertRaisesRegex(ValueError, 'complete proof link'):
            self.check()

    def test_dependency_cannot_drop_forward_direction_repairs(self):
        self.review['dependency_groups'][1]['review_ids'].remove('STACKS-RECON-057')
        with self.assertRaisesRegex(ValueError, 'membership changed'):
            self.check()

    def test_dependency_cannot_be_optional(self):
        self.review['dependency_groups'][0]['required_together'] = False
        with self.assertRaisesRegex(ValueError, 'Unbound mathematical dependency'):
            self.check()

    def test_unreviewed_state_rejected(self):
        self.review['mathematical_review_complete'] = False
        with self.assertRaisesRegex(ValueError, 'not yet finalized'):
            self.check()


class ReferencePreservationTests(unittest.TestCase):
    def test_new_reference_change_rejected(self):
        before = br'\ref{original}'
        op = {'review_id': 'STACKS-RECON-077', 'line': 3124,
              'old_text': before.decode(), 'replacement_text': r'\ref{other}',
              'start_byte': 0, 'end_byte_exclusive': len(before)}
        with self.assertRaisesRegex(ValueError, 'Unexpected reference-key exception'):
            verify_structure(before, op['replacement_text'].encode(), [op])

    def test_silent_label_change_rejected(self):
        with self.assertRaisesRegex(ValueError, 'outside bound exceptions'):
            verify_structure(br'\label{retained}', br'\label{changed}', [])


if __name__ == '__main__':
    unittest.main()
