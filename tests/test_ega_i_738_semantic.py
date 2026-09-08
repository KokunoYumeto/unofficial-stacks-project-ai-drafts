"""Adversarial versioned evidence checks; not a mathematical proof checker."""
import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import unittest

from tools import ega_i738_semantic_contract as contract

ROOT = Path(__file__).resolve().parents[1]


class Semantic738Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt_raw = (ROOT / contract.RECEIPT_PATH).read_bytes()
        cls.frozen = json.loads(cls.receipt_raw)
        cls.frozen_scope = json.loads((ROOT / 'ega/scope.json').read_bytes())
        paths = {x['path'] for x in cls.frozen['preserved_inputs'] +
                 cls.frozen['reviewed_artifacts'] + cls.frozen['ledgers']}
        paths |= {'ega/i738.md', contract.AUTHORITY['path']}
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

    def test_live_candidate_receipt_and_printed_authority(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(contract.receipt_errors(self.receipt_raw), [])
        self.assertEqual(contract.authority_errors(self.raw[contract.AUTHORITY['path']]), [])

    def test_exact_unit_subitem_proof_and_excluded_heading_inventory(self):
        self.assertEqual(self.frozen['source_units'], ['ega:I.7.3.8','ega:I.7.3.8.1'])
        self.assertEqual(self.frozen['source_proof_units'], ['ega:I.7.3.8:proof'])
        self.assertEqual([r['unit_id'] for r in self.frozen['english_discovery']['stable_units']],
                         ['ega:I.7.3.8','ega:I.7.3.8.1','ega:I.7.3.8:proof'])
        self.assertIsNone(self.frozen['owned_section_heading'])
        self.assertEqual(self.frozen['next_semantic_cursor'],'ega:I.7.4.1')
        self.assertIs(self.frozen['next_cursor_starts_with_numbered_environment'],False)
        for key in ('source_units','source_proof_units','owned_section_heading','next_semantic_cursor','next_heading'):
            self.receipt=copy.deepcopy(self.frozen);self.receipt[key]='ADVERSE'
            self.assertTrue(self.errors(),key)

    def test_three_complete_source_versions_cannot_be_swapped(self):
        self.assertEqual(set(self.frozen['languages']),{'old_fr','corrected_fr','en'})
        bounds={'old_fr':(648,671),'corrected_fr':(470,507),'en':(380,402)}
        for language,(first,last) in bounds.items():
            source=self.frozen['source_passages'][language]
            self.assertEqual((source['spans']['owned']['first_line'],source['spans']['owned']['last_line']),(first,last))
            for other in set(bounds)-{language}:
                self.receipt=copy.deepcopy(self.frozen)
                self.receipt['languages'][language]=copy.deepcopy(self.frozen['languages'][other])
                self.assertTrue(self.errors(),(language,other))
            self.receipt=copy.deepcopy(self.frozen)
            self.receipt['source_passages'][language]['spans']['proof']['text']=''
            self.assertTrue(self.errors(),language)

    def test_all_source_boundaries_and_metadata_self_rehash_rejected(self):
        for language,entry in self.frozen['languages'].items():
            for span in entry['spans']:
                for mode in ('omit','replace','reassign'):
                    self.receipt=copy.deepcopy(self.frozen);spans=self.receipt['languages'][language]['spans']
                    if mode=='omit':del spans[span]
                    elif mode=='replace':spans[span]={'sha256':'0'*64}
                    else:spans['unreviewed_741']=spans.pop(span)
                    self.assertTrue(self.errors(),(language,span,mode))

    def test_printed_authority_is_new_separate_exact_binding(self):
        path=contract.AUTHORITY['path'];raw=self.raw[path];obj=json.loads(raw)
        self.assertEqual(obj['original']['doi'],'10.1007/BF02699291')
        self.assertEqual(obj['original']['pdf_sha256'],'111834EFFFE9E90D068389D418F08925A82B4A54AE2957F080712D4180E032EB')
        self.assertEqual([p['printed_page'] for p in obj['visual_evidence']['pages']],[221,222])
        self.assertIs(obj['visual_evidence']['performed_by_implementation_owner'],False)
        for ledger in self.frozen['ledgers']:
            if ledger['path']=='ega/smap.csv':
                self.assertTrue(all(r['source_receipt']==path and r['source_receipt_sha256']==contract.AUTHORITY['sha256'] for r in ledger['rows']))
        self.assertIn('not old F37ZW', self.scope['reviewed_errata_slices']['ega:I.7.3.8']['historical_admission'])
        for value in (None,b'',raw+b' ',raw.replace(b'221',b'220')):
            self.assertTrue(contract.authority_errors(value))
            self.raw[path]=value;self.assertTrue(self.errors())
        self.raw=dict(self.frozen_raw)
        self.receipt['french_authority']['primary_binding']['sha256']='0'*64
        self.assertTrue(self.errors())

    def test_every_semantic_claim_and_unknown_claim_rejected(self):
        for key,value in self.frozen['semantic_contract'].items():
            for replacement in ([not value,int(value)] if isinstance(value,bool) else ['ADVERSE']):
                self.receipt=copy.deepcopy(self.frozen);self.receipt['semantic_contract'][key]=replacement
                self.assertTrue(self.errors(),key)
        self.receipt=copy.deepcopy(self.frozen);self.receipt['semantic_contract']['unreviewed_741']=True
        self.assertTrue(self.errors())

    def test_derived_claims_and_hypotheses_are_explicit(self):
        expected={'isomorphism_iff':'entire point-set generic fiber f^-1(eta_Y)={eta_X}',
            'generic_point_set_bijection_suffices':False,'finite_component_reducedness_required':False,
            'target_generic_surjectivity_required':False,'finite_component_global_injection_claimed':False,
            'arbitrary_pullback_exactness_used':False,'old_and_corrected_sources_conflated':False,
            'bridge_0EMF':['every weakly associated point is component generic','every quasi-compact open has finitely many components']}
        for key,value in expected.items():self.assertEqual(self.frozen['semantic_contract'][key],value)
        for key in ('source_version_disposition','choices','prepared_dossier','review_record'):
            self.receipt=copy.deepcopy(self.frozen);self.receipt[key]=[];self.assertTrue(self.errors(),key)

    def test_every_choice_maps_exact_source_target_sections_and_edges(self):
        manuscript=self.frozen_raw['ega/i738.md'].decode();anchors=[]
        for choice in self.frozen['choices']:
            self.assertEqual({s['version'] for s in choice['source_versions']},{'old_fr','corrected_fr','en'})
            for source in choice['source_versions']:
                self.assertEqual(source['source_text'],self.frozen['source_passages'][source['version']]['spans']['owned']['text'])
            for segment in choice['target_segments']:
                anchor=segment['target_segment_id'];anchors.append(anchor);marker='<a id="'+anchor+'"></a>'
                self.assertEqual(manuscript.count(marker),1)
                section=manuscript.split(marker+'\n\n',1)[1].split('<a id="',1)[0]
                self.assertEqual(segment['target_text_ref'],'ega/i738.md#'+anchor)
                self.assertEqual(segment['target_text'],section)
            selected=[r['edge_id'] for r in self.frozen['ledgers'][1]['rows'] if r['decision_id']==choice['decision_id']]
            self.assertEqual(choice['target_edges'],selected)
        self.assertEqual(len(anchors),len(set(anchors)))
        self.assertEqual(len(anchors),6)

    def test_all12_paired_target_blocks_and_tag_joins_exist(self):
        self.assertEqual({t['tag'] for t in self.frozen['targets']},
            {'0CC1','01RV','01X5','02OT','02OU','0EMF','01I9','00DK','00E3','01K1','0H7H','01CB'})
        for t in self.frozen['targets']:
            for edition,c in [('official',contract.UPSTREAM),('integrated',contract.TARGET_COMMIT)]:
                self.blobs=dict(self.frozen_blobs);key=(c,t['path']);raw=self.blobs[key];pos=t[edition]['byte_offset_start']
                self.blobs[key]=raw[:pos]+b'X'+raw[pos+1:];self.assertTrue(self.errors(),(t['tag'],edition))
            self.blobs=dict(self.frozen_blobs);self.tags=dict(self.frozen_tags);self.tags[t['label']]='ZZZZ'
            self.assertTrue(self.errors(),t['tag'])

    def test_whole_target_files_and_unequal_versions_bound(self):
        for key,raw in self.frozen_blobs.items():
            if key[1]=='tags/tags':continue
            self.blobs=dict(self.frozen_blobs);self.blobs[key]=b'X'+raw[1:];self.assertTrue(self.errors(),key)
        self.blobs=dict(self.frozen_blobs)
        unequal={t['tag'] for t in self.frozen['targets'] if t['official']['sha256']!=t['integrated']['sha256']}
        self.assertEqual(unequal,{'01RV','00E3','01CB'})
        for tag in unequal:
            self.receipt=copy.deepcopy(self.frozen);t=next(t for t in self.receipt['targets'] if t['tag']==tag);t['official']=t['integrated']
            self.assertTrue(self.errors(),tag)

    def test_ledger_prefix_append_postimage_and_runtime_active_view(self):
        for ledger in self.frozen['ledgers']:
            path=ledger['path']
            for mode in ('prefix','append','extra','crlf'):
                self.raw=dict(self.frozen_raw);raw=self.raw[path]
                if mode=='prefix':raw=b'X'+raw[1:]
                elif mode=='append':n=ledger['prefix_bytes'];raw=raw[:n]+b'X'+raw[n+1:]
                elif mode=='extra':raw+=b'ADVERSE\n'
                else:raw=raw.replace(b'\n',b'\r\n')
                self.raw[path]=raw;self.assertTrue(self.errors(),(path,mode))
        self.raw=dict(self.frozen_raw);self.tables['ega/smap.csv'].append(dict(self.tables['ega/smap.csv'][-1],edge_id='S999999'))
        self.assertTrue(self.errors())

    def test_prior12gaps_and_discovery_never_promoted(self):
        self.assertEqual(sum(r['status']=='open_gap' for r in self.tables['ega/resid.csv']),12)
        next(r for r in self.tables['ega/resid.csv'] if r['status']=='open_gap')['status']='covered_derived';self.assertTrue(self.errors())
        self.tables=copy.deepcopy(self.frozen_tables);self.units['ega:I.7.3.8']['review_state']='reviewed_existing';self.assertTrue(self.errors())
        self.units=copy.deepcopy(self.frozen_units);self.units['ega:I.7.4.1:fictional']={'unit_id':'ega:I.7.4.1:fictional'};self.assertTrue(self.errors())

    def test_scope_frontier_and_both_source_scopes_bound(self):
        for key in ('next_semantic_cursor','reviewed_source_slices','reviewed_errata_slices','statement_review_snapshot','residual_snapshot'):
            self.scope=copy.deepcopy(self.frozen_scope);self.scope[key]={};self.assertTrue(self.errors(),key)

    def test_dossier_semantic_damage_and_coordinated_rehash_rejected(self):
        raw=self.frozen_raw['ega/i738.md']
        for before,after in [(b'entire',b'generic-point-only'),(b'not necessary',b'necessary'),
            (b'not a global sheaf isomorphism',b'a global sheaf isomorphism'),
            (b'without assuming they',b'assuming they'),(b'not defined',b'defined')]:
            damaged=raw.replace(before,after);self.assertNotEqual(raw,damaged,before)
            expected=dict(contract.DOSSIER,bytes=len(damaged),sha256=hashlib.sha256(damaged).hexdigest().upper())
            self.assertTrue(contract.dossier_errors(damaged,expected));self.raw['ega/i738.md']=damaged;self.assertTrue(self.errors())

    def test_every_preserved_and_reviewed_actual_artifact_bound(self):
        self.assertTrue(self.frozen['reviewed_artifacts'],'Final review must be sealed before acceptance')
        for item in self.frozen['preserved_inputs']+self.frozen['reviewed_artifacts']:
            self.raw=dict(self.frozen_raw);self.raw[item['path']]+=b'ADVERSE';self.assertTrue(self.errors(),item['path'])

    def test_receipt_exact_bytes_and_no_self_authentication(self):
        self.assertTrue(contract.receipt_errors(self.receipt_raw+b' '))
        self.assertTrue(contract.receipt_errors(None))
        self.receipt['targets'][0]['official']['sha256']='0'*64;self.assertTrue(self.errors())

    def test_malformed_metadata_views_and_loaders_fail_closed(self):
        args=[self.receipt,self.scope,self.tables,self.units,lambda c,p:self.blobs[c,p],self.tags,lambda p:self.raw[p]]
        for index in range(len(args)):
            for value in (None,[],'wrong'):
                bad=list(args);bad[index]=value;self.assertTrue(contract.verify(*bad),(index,value))
        for key in self.frozen:
            self.receipt=copy.deepcopy(self.frozen);self.receipt[key]=[None];self.assertTrue(self.errors(),key)
        self.receipt=copy.deepcopy(self.frozen)
        for path in self.frozen_tables:
            for value in (None,[None],[{'source_unit':[]}],'wrong'):
                self.tables=copy.deepcopy(self.frozen_tables);self.tables[path]=value;self.assertTrue(self.errors(),(path,value))
        for value in (None,[],'wrong'):
            self.assertTrue(contract.verify(self.frozen,self.frozen_scope,self.frozen_tables,self.frozen_units,
                lambda c,p:value,self.frozen_tags,lambda p:self.frozen_raw[p]))
            self.assertTrue(contract.verify(self.frozen,self.frozen_scope,self.frozen_tables,self.frozen_units,
                lambda c,p:self.frozen_blobs[c,p],self.frozen_tags,lambda p:value))


if __name__=='__main__':
    unittest.main()
