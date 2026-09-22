"""Mechanical regression tests; not a substitute for mathematical review."""
import unittest
from verify_categories_intake_review_20260922 import replace_bound


class BoundReplayTests(unittest.TestCase):
    def test_descending_replay_preserves_non_target_bytes(self):
        raw = b'first\nold and old\nlast\n'
        ops = [{'start_byte': 6, 'end_byte_exclusive': 9, 'old_text': 'old', 'replacement_text': 'new\nlong'},
               {'start_byte': 14, 'end_byte_exclusive': 17, 'old_text': 'old', 'replacement_text': 'x'}]
        self.assertEqual(replace_bound(raw, ops), b'first\nnew\nlong and x\nlast\n')

    def test_repeated_token_cannot_float_to_another_position(self):
        with self.assertRaisesRegex(ValueError, 'Preimage drift'):
            replace_bound(b'old new old', [{'start_byte': 4, 'end_byte_exclusive': 7,
                'old_text': 'old', 'replacement_text': 'fixed'}])

    def test_overlap_is_rejected(self):
        ops = [{'start_byte': 0, 'end_byte_exclusive': 3, 'old_text': 'abc', 'replacement_text': 'one'},
               {'start_byte': 2, 'end_byte_exclusive': 5, 'old_text': 'cde', 'replacement_text': 'two'}]
        with self.assertRaisesRegex(ValueError, 'Overlapping'):
            replace_bound(b'abcdef', ops)


if __name__ == '__main__':
    unittest.main()
