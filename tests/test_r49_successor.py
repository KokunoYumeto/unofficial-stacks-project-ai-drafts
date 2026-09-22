import unittest
from tools import r49_successor as r


class R49SuccessorTests(unittest.TestCase):
    def test_append_does_not_allow_history_rewrite(self):
        with self.assertRaises(ValueError):
            r.append_check({'entries': [1]}, {'entries': [2, 3]}, 'entries', 1)

    def test_append_does_not_allow_header_rewrite(self):
        with self.assertRaises(ValueError):
            r.append_check({'entries': [1], 'version': 1},
                           {'entries': [1, 2], 'version': 2}, 'entries', 1)

    def test_preimage_drift_fails(self):
        with self.assertRaises(ValueError):
            r.apply_exact(b'abc', [{'start_byte': 1, 'end_byte_exclusive': 2,
                                   'old_text': 'z', 'replacement_text': 'd'}])

    def test_overlapping_operations_fail(self):
        with self.assertRaises(ValueError):
            r.apply_exact(b'abcd', [
                {'start_byte': 1, 'end_byte_exclusive': 3, 'old_text': 'bc', 'replacement_text': 'BC'},
                {'start_byte': 2, 'end_byte_exclusive': 4, 'old_text': 'cd', 'replacement_text': 'CD'}])

    def test_inserted_source_is_preserved(self):
        authority = b'first\nold\nlast\n'
        prior = b'first\nnew theorem\nold\nlast\n'
        ops = [{'source': 'derham.tex', 'source_start_line': 2, 'source_end_line': 2,
                'start_byte': 6, 'end_byte_exclusive': 9, 'old_text': 'old', 'replacement_text': 'fixed'}]
        post, rebound = r.compose(prior, authority, ops)
        self.assertEqual(post, b'first\nnew theorem\nfixed\nlast\n')
        self.assertEqual(rebound[0]['cumulative_line'], 3)

    def test_changed_cumulative_line_fails_closed(self):
        authority = b'first\nold\nlast\n'
        ops = [{'source': 'derham.tex', 'source_start_line': 2, 'source_end_line': 2,
                'start_byte': 6, 'end_byte_exclusive': 9, 'old_text': 'old', 'replacement_text': 'fixed'}]
        with self.assertRaises(ValueError):
            r.compose(b'first\nchanged old\nlast\n', authority, ops)

    def test_immutable_admitted_evidence_and_cumulative_replay(self):
        files, refs, ops, authority = r.evidence()
        self.assertEqual((len(files), refs, len(ops)), (138, 137, 7))
        prior = r.blob(r.PREVIOUS, 'derham.tex')
        post, rebound = r.compose(prior, authority, ops)
        self.assertEqual(r.sha(prior), '0AA0F22D9765CCBB167D3C63D47143ACD35B241972B6B71FC772D8F0B327CDF3')
        self.assertEqual(r.sha(post), '27108C367245F8F1E44CAC8BC3F92A0D66C040AC5D75FD2CCD59B8AAD9F2F010')
        self.assertEqual(len(post), 237944)
        self.assertNotEqual(post, files[r.PREFIX + 'payload/derham.tex'])
        self.assertEqual(len({op['stable_id'] for op in rebound}), 5)


if __name__ == '__main__':
    unittest.main()
