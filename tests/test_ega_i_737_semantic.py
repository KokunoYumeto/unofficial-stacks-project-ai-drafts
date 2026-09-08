"""Independent adversarial evidence checks, not tests of mathematical truth."""
import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import unittest

from tools import ega_i737_semantic_contract as contract

ROOT = Path(__file__).resolve().parents[1]


class Semantic737Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt_raw = (ROOT / contract.RECEIPT_PATH).read_bytes()
        cls.frozen = json.loads(cls.receipt_raw)
        cls.frozen_scope = json.loads((ROOT / 'ega/scope.json').read_bytes())
        paths = {x['path'] for x in cls.frozen['preserved_inputs'] + cls.frozen['reviewed_artifacts'] + cls.frozen['ledgers']}
        paths.add('ega/i737.md')
        cls.frozen_raw = {p: (ROOT / p).read_bytes() for p in paths}
        cls.frozen_tables = {}
        for ledger in cls.frozen['ledgers']:
            rows = list(csv.DictReader(io.StringIO(cls.frozen_raw[ledger['path']].decode(), newline='')))
            superseded = {r.get('supersedes') for r in rows if r.get('supersedes')}
            cls.frozen_tables[ledger['path']] = [r for r in rows if r[ledger['id_field']] not in superseded]
        cls.frozen_units = {r['unit_id']: r for r in csv.DictReader(io.StringIO(cls.frozen_raw['ega/units.csv'].decode(), newline=''))}
        target_paths = {t['path'] for t in cls.frozen['targets']} | {'tags/tags'}
        cls.frozen_blobs = {(c,p): subprocess.check_output(['git','show',c+':'+p], cwd=ROOT)
                            for c in (contract.UPSTREAM,contract.TARGET_COMMIT) for p in target_paths}
        cls.frozen_tags = {line.split(',',1)[1]:line.split(',',1)[0]
                           for line in cls.frozen_blobs[contract.UPSTREAM,'tags/tags'].decode().splitlines()
                           if line and not line.startswith('#')}

    def setUp(self):
        self.receipt = copy.deepcopy(self.frozen)
        self.scope = copy.deepcopy(self.frozen_scope)
        self.tables = copy.deepcopy(self.frozen_tables)
        self.units = copy.deepcopy(self.frozen_units)
        self.raw = dict(self.frozen_raw)
        self.blobs = dict(self.frozen_blobs)
        self.tags = dict(self.frozen_tags)

    def errors(self):
        return contract.verify(self.receipt,self.scope,self.tables,self.units,
                               lambda c,p:self.blobs[c,p],self.tags,lambda p:self.raw[p])

    def test_live_candidate_and_sealed_receipt(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(contract.receipt_errors(self.receipt_raw), [])

    def test_complete_unit_proof_and_excluded_frontier_inventory(self):
        expected = ['ega:I.7.3.5','ega:I.7.3.5:proof','ega:I.7.3.6','ega:I.7.3.6:proof','ega:I.7.3.7','ega:I.7.3.7:proof']
        self.assertEqual([r['unit_id'] for r in self.receipt['english_discovery']['stable_units']],expected)
        self.assertEqual(self.receipt['source_proof_units'],expected[1::2])
        self.assertIsNone(self.receipt['owned_section_heading'])
        self.assertEqual(self.receipt['next_semantic_cursor'],'ega:I.7.3.8')
        for key in ('source_units','source_proof_units','owned_unnumbered_parts','owned_section_heading','next_semantic_cursor'):
            self.receipt=copy.deepcopy(self.frozen)
            self.receipt[key]='ADVERSE'
            self.assertTrue(self.errors(),key)

    def test_every_semantic_claim_boolean_number_and_unknown_claim_rejected(self):
        for key,value in self.frozen['semantic_contract'].items():
            for replacement in ([not value,int(value)] if isinstance(value,bool) else ['ADVERSE']):
                self.receipt=copy.deepcopy(self.frozen)
                self.receipt['semantic_contract'][key]=replacement
                self.assertTrue(self.errors(),key)
        self.receipt=copy.deepcopy(self.frozen)
        self.receipt['semantic_contract']['unreviewed_738']=True
        self.assertTrue(self.errors())

    def test_mathematical_hypotheses_and_normalizations_explicitly_pinned(self):
        required={
            'historical_simple':'constant sheaf; not simple module',
            'I735_presentation_indices':'arbitrary sets; sheaf direct sums, not products',
            'I735_english_missing_parentheses_preserved':True,
            'general_ringed_space_arbitrary_sum_closure_claimed':False,
            'I736_starting_ring':'O_X',
            'I736_finite_rank_required':False,
            'I737_injection':'all reduced schemes, independent of component finiteness',
            'R_equals_K_general_nonreduced':False,
            'reducedness_necessary_for_injection':False,
            'adverse_skyscraper_scalar_action':'S_x(U)=K if x in U and zero otherwise; identity or zero restrictions; O_Xx to K action, not a module pushforward from Spec kappa(x)',
        }
        for key,value in required.items():
            self.assertEqual(self.frozen['semantic_contract'][key],value)

    def test_every_source_owner_subspan_and_self_rehash_bound(self):
        for lang in ('fr','en'):
            for section in ('slices','numbered_environments','owned_parts','proof_bodies','page_markers'):
                for owner in self.frozen['languages'][lang][section]:
                    for mode in ('omit','truncate','reassign','rehash'):
                        self.receipt=copy.deepcopy(self.frozen)
                        spans=self.receipt['languages'][lang][section]
                        if mode=='omit': del spans[owner]
                        elif mode=='truncate': spans[owner]['lf_line_end']-=1
                        elif mode=='reassign': spans['ega:I.7.3.8:proof']=spans.pop(owner)
                        else: spans[owner]['sha256']='0'*64
                        self.assertTrue(self.errors(),(lang,section,owner,mode))

    def test_printed_proof_distinguished_from_independent_arguments(self):
        for lang in ('fr','en'):
            self.receipt=copy.deepcopy(self.frozen)
            self.receipt['source_passages'][lang]['spans']['unit736']['text']+='Invented first-assertion proof'
            self.assertTrue(self.errors())
        self.receipt=copy.deepcopy(self.frozen)
        self.receipt['source_proof_vs_independent_argument']['ega:I.7.3.6']['source_proof']='full tensor proof printed'
        self.assertTrue(self.errors())

    def test_chapter0_language_provenance_and_choice_consultation_bound(self):
        for key in ('chapter0_comparison','original_french_chapter0_attributed','normalization_decisions','choices','review_record'):
            self.receipt=copy.deepcopy(self.frozen)
            self.receipt[key]=[]
            self.assertTrue(self.errors(),key)

    def test_choice_segment_links_resolve_and_bind_exact_target_text(self):
        manuscript=self.frozen_raw['ega/i737.md'].decode('utf-8')
        for n,choice in zip((5,6,7),self.frozen['choices']):
            anchor='ega-i-73'+str(n)
            self.assertEqual(choice['target_segment_id'],anchor)
            self.assertEqual(choice['target_text_ref'],'ega/i737.md#'+anchor)
            marker='<a id="'+anchor+'"></a>'
            self.assertEqual(manuscript.count(marker),1)
            section=manuscript.split(marker+'\n\n',1)[1]
            if n<7: section=section.split('<a id="ega-i-73'+str(n+1)+'"></a>',1)[0]
            self.assertEqual(choice['target_text'],section)
        for decision in self.frozen['normalization_decisions']:
            self.assertIn('attributed to the preflight source reviewer',decision['consultation_provenance'])

    def test_all18_paired_targets_exist_and_actual_bytes_are_checked(self):
        self.assertEqual(len(self.frozen['targets']),18)
        self.assertEqual(len({t['tag'] for t in self.frozen['targets']}),18)
        for t in self.frozen['targets']:
            for edition,c in [('official',contract.UPSTREAM),('integrated',contract.TARGET_COMMIT)]:
                self.blobs=dict(self.frozen_blobs)
                key=(c,t['path']); raw=self.blobs[key]; pos=t[edition]['byte_offset_start']
                self.blobs[key]=raw[:pos]+b'X'+raw[pos+1:]
                self.assertTrue(self.errors(),(t['tag'],edition))

    def test_target_whole_file_and_tag_join_bound(self):
        for key,raw in self.frozen_blobs.items():
            if key[1]=='tags/tags': continue
            self.blobs=dict(self.frozen_blobs); self.blobs[key]=b'X'+raw[1:]
            self.assertTrue(self.errors(),key)
        self.blobs=dict(self.frozen_blobs)
        for t in self.frozen['targets']:
            self.tags=dict(self.frozen_tags); self.tags[t['label']]='ZZZZ'
            self.assertTrue(self.errors(),t['tag'])

    def test_unequal_target_versions_never_conflated(self):
        unequal={t['tag'] for t in self.frozen['targets'] if t['official']['sha256']!=t['integrated']['sha256']}
        self.assertEqual(unequal,{'01CB','01CC','01RV','01HV','00EU','0052'})
        for tag in unequal:
            self.receipt=copy.deepcopy(self.frozen)
            t=next(t for t in self.receipt['targets'] if t['tag']==tag)
            t['official']=t['integrated']
            self.assertTrue(self.errors(),tag)

    def test_ledger_prefix_append_postimage_and_active_view_bound(self):
        for ledger in self.frozen['ledgers']:
            path=ledger['path']
            for mode in ('prefix','append','extra','crlf'):
                self.raw=dict(self.frozen_raw); raw=self.raw[path]
                if mode=='prefix': raw=b'X'+raw[1:]
                elif mode=='append':
                    n=ledger['prefix_bytes']; raw=raw[:n]+b'X'+raw[n+1:]
                elif mode=='extra': raw+=b'ADVERSE\n'
                else: raw=raw.replace(b'\n',b'\r\n')
                self.raw[path]=raw
                self.assertTrue(self.errors(),(path,mode))
        self.raw=dict(self.frozen_raw)
        self.tables['ega/smap.csv'].append(dict(self.tables['ega/smap.csv'][-1],edge_id='S999999'))
        self.assertTrue(self.errors())

    def test_prior12_gaps_and_unchanged_discovery_inventory(self):
        self.assertEqual(sum(r['status']=='open_gap' for r in self.tables['ega/resid.csv']),12)
        next(r for r in self.tables['ega/resid.csv'] if r['status']=='open_gap')['status']='covered_derived'
        self.assertTrue(self.errors())
        self.tables=copy.deepcopy(self.frozen_tables)
        self.units['ega:I.7.3.5']['review_state']='reviewed_existing'
        self.assertTrue(self.errors())
        self.units=copy.deepcopy(self.frozen_units)
        self.units['ega:I.7.3.8:fictional']={'unit_id':'ega:I.7.3.8:fictional'}
        self.assertTrue(self.errors())

    def test_live_frontier_scope_and_snapshots_bound(self):
        for key in ('next_semantic_cursor','reviewed_source_slices','statement_review_snapshot','residual_snapshot'):
            self.scope=copy.deepcopy(self.frozen_scope); self.scope[key]={}
            self.assertTrue(self.errors(),key)

    def test_dossier_damage_and_coordinated_rehash_rejected(self):
        raw=self.frozen_raw['ega/i737.md']
        for before,after in [(b'arbitrary sets',b'finite sets'),(b'not necessarily a field',b'always a field'),
            (b'not canonical',b'canonical'),(b'more general hypothesis',b'stronger premise'),
            (b'every reduced scheme',b'every scheme')]:
            damaged=raw.replace(before,after)
            self.assertNotEqual(raw,damaged,before)
            expected=dict(contract.DOSSIER,bytes=len(damaged),sha256=hashlib.sha256(damaged).hexdigest().upper())
            self.assertTrue(contract.dossier_errors(damaged,expected))
            self.raw['ega/i737.md']=damaged
            self.assertTrue(self.errors())

    def test_all_preserved_and_reviewed_artifacts_actual_bytes_bound(self):
        for item in self.frozen['preserved_inputs']+self.frozen['reviewed_artifacts']:
            self.raw=dict(self.frozen_raw); self.raw[item['path']]+=b'ADVERSE'
            self.assertTrue(self.errors(),item['path'])

    def test_receipt_and_dossier_seals_not_self_authenticating(self):
        self.assertTrue(contract.receipt_errors(self.receipt_raw+b' '))
        self.assertTrue(contract.receipt_errors(None))
        self.receipt['targets'][0]['official']['sha256']='0'*64
        self.assertTrue(self.errors())

    def test_malformed_metadata_views_and_loaders_fail_closed(self):
        args=[self.receipt,self.scope,self.tables,self.units,lambda c,p:self.blobs[c,p],self.tags,lambda p:self.raw[p]]
        for index in range(len(args)):
            for value in (None,[],'wrong'):
                bad=list(args); bad[index]=value
                self.assertTrue(contract.verify(*bad),(index,value))
        for key in self.frozen:
            self.receipt=copy.deepcopy(self.frozen); self.receipt[key]=[None]
            self.assertTrue(self.errors(),key)
        self.receipt=copy.deepcopy(self.frozen)
        for path in self.frozen_tables:
            for value in (None,[None],[{'source_unit':[]}],'wrong'):
                self.tables=copy.deepcopy(self.frozen_tables); self.tables[path]=value
                self.assertTrue(self.errors(),(path,value))
        for value in (None,[],'wrong'):
            self.assertTrue(contract.verify(self.frozen,self.frozen_scope,self.frozen_tables,self.frozen_units,
                lambda c,p:value,self.frozen_tags,lambda p:self.frozen_raw[p]))
            self.assertTrue(contract.verify(self.frozen,self.frozen_scope,self.frozen_tables,self.frozen_units,
                lambda c,p:self.frozen_blobs[c,p],self.frozen_tags,lambda p:value))


if __name__=='__main__':
    unittest.main()
