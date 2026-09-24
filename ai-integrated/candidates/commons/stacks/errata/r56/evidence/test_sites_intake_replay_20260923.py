"""Mechanical regressions; these tests do not certify mathematical correctness."""
import unittest

from verify_sites_intake_review_20260923 import line_map, structure, verify_structure
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

    def test_multiline_deletion_and_exact_inverse(self):
        raw=b'before\nremove\nthis. Next sentence.\nafter\n'
        edit={'start_byte':7,'end_byte_exclusive':20,'old_text':'remove\nthis. ','replacement_text':''}
        result=replace_bound(raw,[edit])
        self.assertEqual(result,b'before\nNext sentence.\nafter\n')
        self.assertEqual(replace_bound(result,[{'start_byte':7,'end_byte_exclusive':7,
            'old_text':'','replacement_text':'remove\nthis. '}]),raw)

    def test_added_line_between_old_lines_is_not_contiguous(self):
        mapping=line_map([b'a\n',b'b\n'],[b'a\n',b'addition\n',b'b\n'])
        self.assertNotEqual(mapping[1],mapping[0]+1)

    def test_citation_keys_not_optional_locator_spelling(self):
        a=br'\cite[I, Corrolaire 1]{Bourbaki} \label{a} \ref{b}'
        b=br'\cite[I, Corollaire 1]{Bourbaki} \label{a} \ref{b}'
        self.assertEqual(structure(a),structure(b))
        self.assertNotEqual(structure(a),structure(b.replace(b'{Bourbaki}',b'{Other}')))


class ReferenceExceptionTests(unittest.TestCase):
    def fixture(self):
        old = r'\ref{lemma-sieves-set}'
        raw = ('A '+old+'\nB '+old+'\nC '+old+'\n').encode()
        positions = [2, len(('A '+old+'\nB ').encode())]
        ops = [{'review_id':'SITES-RECON-148','line':line,'start_byte':start,
                'end_byte_exclusive':start+len(old),'old_text':old,
                'replacement_text':r'\ref{lemma-topology-basic}'}
               for line,start in zip([11484,11574],positions)]
        return raw,ops

    def test_exact_two_bound_reference_corrections_pass(self):
        raw,ops=self.fixture()
        self.assertEqual(len(verify_structure(raw,replace_bound(raw,ops),ops)),2)

    def test_same_replacement_on_wrong_authority_line_rejected(self):
        raw,ops=self.fixture();ops[0]['line']=11459
        with self.assertRaisesRegex(ValueError,'Unexpected reference-key exception'):
            verify_structure(raw,replace_bound(raw,ops),ops)

    def test_unlisted_third_reference_change_rejected(self):
        raw,ops=self.fixture();after=replace_bound(raw,ops)
        after=after.replace(br'\ref{lemma-sieves-set}',br'\ref{lemma-topology-basic}')
        with self.assertRaisesRegex(ValueError,'outside bound exceptions'):
            verify_structure(raw,after,ops)

    def test_unlisted_label_change_rejected(self):
        raw,ops=self.fixture();raw+=br'\label{retained}'
        after=replace_bound(raw,ops).replace(br'\label{retained}',br'\label{changed}')
        with self.assertRaisesRegex(ValueError,'outside bound exceptions'):
            verify_structure(raw,after,ops)

    def test_wrong_new_key_rejected(self):
        raw,ops=self.fixture();ops[1]['replacement_text']=r'\ref{lemma-other}'
        with self.assertRaisesRegex(ValueError,'Unexpected reference-key exception'):
            verify_structure(raw,replace_bound(raw,ops),ops)


if __name__=='__main__':unittest.main()
