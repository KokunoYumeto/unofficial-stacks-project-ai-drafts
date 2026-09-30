"""Reject preservation failures at the R60 admission/publication boundary."""
import copy
import unittest
from tools import validate_r60_successor as v


class R60PreservationTests(unittest.TestCase):
    def fixture(self):
        old={'registered_entries':[{'id':'old','stable_ids':['kept']}]}
        entry={'id':'new','stable_ids':['new']}
        issued={'event_id':'issued','lease_id':'lease','state':'active'}
        released={'event_id':'released','lease_id':'lease','state':'released','supersedes_event_id':'issued'}
        leases={'events':[{'event_id':'earlier'}]}
        return old,{'registered_entries':old['registered_entries']+[entry]},entry,leases,{'events':leases['events']+[issued,released]},issued,released

    def test_exact_append(self):
        v.append_only_registry(*self.fixture())

    def test_rewritten_prior_entry_fails(self):
        args=copy.deepcopy(self.fixture());args[1]['registered_entries'][0]={'id':'replaced','stable_ids':['kept']}
        with self.assertRaisesRegex(ValueError,'prefix'):v.append_only_registry(*args)

    def test_reused_stable_id_fails(self):
        args=copy.deepcopy(self.fixture());args[2]['stable_ids']=['kept'];args[1]['registered_entries'][-1]=args[2]
        with self.assertRaisesRegex(ValueError,'Reused'):v.append_only_registry(*args)

    def test_broken_release_fails(self):
        args=copy.deepcopy(self.fixture());args[6]['supersedes_event_id']='unrelated'
        with self.assertRaisesRegex(ValueError,'lease release'):v.append_only_registry(*args)

    def test_lost_old_lease_fails(self):
        args=copy.deepcopy(self.fixture());args[4]['events'].pop(0)
        with self.assertRaisesRegex(ValueError,'Lease prefix'):v.append_only_registry(*args)

    def test_unlisted_historical_proof_edit_fails(self):
        with self.assertRaisesRegex(ValueError,'Unlisted'):
            v.allowed_delta([dict(path='old/proof.tex',status='M',new_mode='100644')],{'new/receipt.json'})

    def test_allowed_path_cannot_be_deleted(self):
        with self.assertRaisesRegex(ValueError,'Deletion'):
            v.allowed_delta([dict(path='proof.tex',status='D',new_mode='000000')],{'proof.tex'})

    def test_allowed_path_cannot_be_symlink(self):
        with self.assertRaisesRegex(ValueError,'file mode'):
            v.allowed_delta([dict(path='proof.tex',status='M',new_mode='120000')],{'proof.tex'})


if __name__=='__main__':unittest.main()
