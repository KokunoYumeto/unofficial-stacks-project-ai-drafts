"""Adverse checks for the concurrent registry transport and frozen scope."""
import copy
import unittest
from tools import validate_r58_successor as v

class R58TransportTests(unittest.TestCase):
    def fixture(self):
        base={'events':[{'event_id':f'lease-event-{i:06d}'} for i in range(1,124)]}
        issued=dict(event_id='lease-event-000124',lease_id='r58',state='active',writer='original')
        release=dict(issued,event_id='lease-event-000125',state='released',supersedes_event_id='lease-event-000124')
        local={'events':base['events']+[issued,release]}
        public={'events':base['events']+[{'event_id':f'lease-event-{i:06d}'} for i in range(124,128)]}
        transported=[dict(issued,event_id='lease-event-000128'),dict(release,event_id='lease-event-000129',supersedes_event_id='lease-event-000128')]
        current={'events':public['events']+transported}
        rows=[dict(original=a,transported=b) for a,b in zip(local['events'][123:],transported)]
        return base,local,public,current,rows

    def test_exact_event_transport(self):
        v.registry_transport(*self.fixture())

    def test_writer_change_fails(self):
        args=copy.deepcopy(self.fixture());args[4][0]['transported']['writer']='replacement'
        with self.assertRaisesRegex(ValueError,'non-identifier'):v.registry_transport(*args)

    def test_missing_public_event_fails(self):
        args=copy.deepcopy(self.fixture());args[3]['events'].pop(124)
        with self.assertRaisesRegex(ValueError,'registry differs'):v.registry_transport(*args)

    def test_dangling_release_fails(self):
        args=copy.deepcopy(self.fixture());args[4][1]['transported']['supersedes_event_id']='lease-event-000124'
        with self.assertRaisesRegex(ValueError,'non-identifier'):v.registry_transport(*args)

    def test_original_receipt_rewrite_fails(self):
        args=copy.deepcopy(self.fixture());args[4][0]['original']=dict(args[4][0]['original'],state='released')
        with self.assertRaisesRegex(ValueError,'Original event'):v.registry_transport(*args)

    def test_frozen_proof_mutation_fails(self):
        before={'proof.tex':('100644','a'),'receipt.json':('100644','b')}
        after={**before,'proof.tex':('100644','c')}
        with self.assertRaisesRegex(ValueError,'Unlisted change'):v.same_except(before,after,{'receipt.json'})

    def test_allowed_receipt_cannot_delete_proof(self):
        with self.assertRaisesRegex(ValueError,'Deletion'):v.same_except({'proof.tex':('100644','a')},{},{'proof.tex'})

    def test_allowed_file_cannot_be_symlink(self):
        with self.assertRaisesRegex(ValueError,'file mode'):v.same_except({'receipt.json':('100644','a')},{'receipt.json':('120000','b')},{'receipt.json'})

if __name__=='__main__':unittest.main()
