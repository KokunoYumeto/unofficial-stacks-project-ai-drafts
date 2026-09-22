import json
import unittest
from tools import r50_successor as r

class R50Tests(unittest.TestCase):
    def test_exact_two_operation_replay(self):
        m, refs, ops, before, after = r.evidence()
        self.assertEqual(len(ops), 2)
        self.assertEqual(len(after), 209792)
        self.assertEqual(r.sha(after), '32F896F8257C8691D6D0350E346036EE0FFA5DC341668B400F57A70BBE2A4489')
        self.assertEqual({o['line'] for o in ops}, {178, 269})
        self.assertEqual(before, r.blob(r.PREVIOUS, 'spaces-limits.tex'))

    def test_drift_fails_closed(self):
        _, _, ops, before, _ = r.evidence()
        altered = before[:6273] + b'?' + before[6274:]
        with self.assertRaises(ValueError): r.replay(altered, ops)

    def test_overlap_fails_closed(self):
        _, _, ops, before, _ = r.evidence()
        with self.assertRaises(ValueError): r.replay(before, [ops[0], ops[0]])

    def test_historical_proposals_remain_immutable(self):
        path = 'ai-integrated/review-notes/2026-09-19-proposed-corrections.json'
        self.assertEqual((r.ROOT/path).read_bytes(), r.blob(r.PREVIOUS, path))
        status = json.loads((r.ROOT/'ai-integrated/review-notes/proposal-integration-status.json').read_bytes())
        self.assertEqual((status['original_selection_units'], status['pending_units'],len(status['composed'])), (13,11,2))

if __name__ == '__main__': unittest.main()
