import json,unittest
from tools import r51_successor as r

class R51Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.manifest,cls.refs,cls.ids,cls.sources,cls.names=r.evidence()
    def test_scope(self):
        self.assertEqual((len(self.ids),sum(len(s['operations']) for s in self.sources)),(29,33))
        self.assertEqual({s['source'] for s in self.sources},{'algebra.tex','homology.tex','schemes.tex','sets.tex'})
    def test_exact_replay(self):
        for s in self.sources:
            self.assertEqual(r.identity(r.replay(r.blob(r.PRIOR,s['source']),s['operations'])),s['postimage'])
    def test_preimage_and_overlap_fail_closed(self):
        s=self.sources[0];op=s['operations'][0];before=r.blob(r.PRIOR,s['source']);i=op['start_byte']
        with self.assertRaises(ValueError):r.replay(before[:i]+b'?'+before[i+1:],s['operations'])
        with self.assertRaises(ValueError):r.replay(before,[op,op])
    def test_all_readable_selection_composed(self):
        status=json.loads((r.ROOT/'ai-integrated/review-notes/proposal-integration-status.json').read_bytes())
        self.assertEqual((status['pending_units'],len(status['composed'])),(0,13))
        self.assertEqual(len({x['finding_id'] for x in status['composed']}),13)

if __name__=='__main__':unittest.main()
