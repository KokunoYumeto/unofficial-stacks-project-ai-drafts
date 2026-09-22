import unittest
from tools.generate_changes_from_upstream import Operation, EvidenceError, apply_operations, sha256_bytes


def op(old, new, start, legacy=False):
    return Operation(old, new, 1, 1, start, start+len(old.encode()),
        'hash-bound reconstructed diff hunk' if legacy else 'manifest-bound exact operation',
        'test', sha256_bytes(old.encode()), sha256_bytes(new.encode()))


class LegacyContextReplayTests(unittest.TestCase):
    def test_disjoint_changed_spans_inside_shared_context(self):
        source = b'prefix A middle B suffix'
        earlier = op(source.decode(), 'prefix a middle B suffix', 0, True)
        later = op('B', 'b', source.index(b'B'))
        self.assertEqual(apply_operations(source, [earlier, later], 'test'), b'prefix a middle b suffix')
        self.assertEqual(apply_operations(source, [later, earlier], 'test'), b'prefix a middle b suffix')

    def test_real_overlap_is_still_rejected(self):
        source = b'prefix A suffix'
        with self.assertRaises(EvidenceError):
            apply_operations(source, [op(source.decode(), 'prefix a suffix', 0, True), op('A', 'z', 7)], 'test')

    def test_entire_historical_preimage_must_still_match(self):
        with self.assertRaises(EvidenceError):
            apply_operations(b'wrong A suffix', [op('prefix A suffix', 'prefix a suffix', 0, True)], 'test')

    def test_unicode_edges_and_insertion(self):
        self.assertEqual(apply_operations('α A ω'.encode(), [op('α A ω', 'α AB ω', 0, True)], 'test'), 'α AB ω'.encode())

    def test_identical_insertions_rejected(self):
        with self.assertRaises(EvidenceError):
            apply_operations(b'AB', [op('', 'x', 1), op('', 'x', 1)], 'test')


if __name__ == '__main__': unittest.main()
