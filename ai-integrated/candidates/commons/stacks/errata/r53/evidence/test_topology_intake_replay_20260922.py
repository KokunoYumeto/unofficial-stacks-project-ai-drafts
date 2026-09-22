"""Mechanical regressions; these tests do not certify mathematical correctness."""
import unittest

from verify_topology_intake_review_20260922 import line_map, structure
from verify_categories_intake_review_20260922 import replace_bound


class ReplayTests(unittest.TestCase):
    def test_line_mapping_preserves_inserted_theorem(self):
        original=[b'heading\n',b'old\n',b'tail\n']
        current=[b'heading\n',b'new theorem\n',b'proof\n',b'old\n',b'tail\n']
        self.assertEqual(line_map(original,current),{0:0,1:3,2:4})

    def test_changed_source_line_is_not_rebound(self):
        self.assertNotIn(1,line_map([b'a\n',b'old\n',b'z\n'],[b'a\n',b'fixed\n',b'z\n']))

    def test_exact_byte_preimage_cannot_float(self):
        with self.assertRaisesRegex(ValueError,'Preimage drift'):
            replace_bound(b'old new old',[{'start_byte':4,'end_byte_exclusive':7,
                'old_text':'old','replacement_text':'fixed'}])

    def test_overlap_fails(self):
        with self.assertRaisesRegex(ValueError,'Overlapping'):
            replace_bound(b'abcdef',[{'start_byte':0,'end_byte_exclusive':3,'old_text':'abc','replacement_text':'A'},
                {'start_byte':2,'end_byte_exclusive':5,'old_text':'cde','replacement_text':'B'}])

    def test_multibyte_and_multiline_replacement(self):
        raw='before\nβeta\nafter\n'.encode()
        old='βeta'.encode()
        self.assertEqual(replace_bound(raw,[{'start_byte':7,'end_byte_exclusive':7+len(old),
            'old_text':'βeta','replacement_text':'beta\nnext'}]),b'before\nbeta\nnext\nafter\n')

    def test_citation_keys_not_optional_locator_spelling(self):
        a=br'\cite[I, Corrolaire 1]{Bourbaki} \label{a} \ref{b}'
        b=br'\cite[I, Corollaire 1]{Bourbaki} \label{a} \ref{b}'
        self.assertEqual(structure(a),structure(b))
        self.assertNotEqual(structure(a),structure(b.replace(b'{Bourbaki}',b'{Other}')))


if __name__=='__main__':unittest.main()
