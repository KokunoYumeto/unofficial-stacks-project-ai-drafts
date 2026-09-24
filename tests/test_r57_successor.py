import unittest
from tools import r57_successor as r

class R57Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.manifest,cls.refs,cls.ids,cls.sources,cls.names=r.evidence()
    def test_scope(self):
        self.assertEqual((len(self.ids),sum(len(s['operations']) for s in self.sources)),(47,56))
        self.assertEqual({s['source'] for s in self.sources},{'fields.tex'})
    def test_exact_replay(self):
        for s in self.sources:
            self.assertEqual(r.identity(r.replay(r.blob(r.PRIOR,s['source']),s['operations'])),s['postimage'])
    def test_preimage_and_overlap_fail_closed(self):
        s=self.sources[0];op=s['operations'][0];before=r.blob(r.PRIOR,s['source']);i=op['start_byte']
        with self.assertRaises(ValueError):r.replay(before[:i]+b'?'+before[i+1:],s['operations'])
        with self.assertRaises(ValueError):r.replay(before,[op,op])

if __name__=='__main__':unittest.main()
