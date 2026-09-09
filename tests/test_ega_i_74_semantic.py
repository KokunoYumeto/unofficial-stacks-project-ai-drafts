"""Adversarial evidence regressions, not a formal mathematical proof checker."""
import copy
import csv
import io
import json
from pathlib import Path
import subprocess
import unittest

from tools import ega_i74_semantic_contract as contract

ROOT = Path(__file__).resolve().parents[1]


class Semantic74Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt_raw = (ROOT / contract.RECEIPT_PATH).read_bytes()
        cls.frozen = json.loads(cls.receipt_raw)
        cls.frozen_scope = json.loads((ROOT / 'ega/scope.json').read_bytes())
        paths = {x['path'] for x in cls.frozen['preserved_inputs'] +
                 cls.frozen['reviewed_artifacts'] + cls.frozen['ledgers']}
        paths |= {'ega/i74.md', contract.AUTHORITY['path']}
        cls.frozen_raw = {p: (ROOT / p).read_bytes() for p in paths}
        cls.frozen_tables = {}
        for ledger in cls.frozen['ledgers']:
            rows = list(csv.DictReader(io.StringIO(cls.frozen_raw[ledger['path']].decode(), newline='')))
            superseded = {r.get('supersedes') for r in rows if r.get('supersedes')}
            cls.frozen_tables[ledger['path']] = [r for r in rows if r[ledger['id_field']] not in superseded]
        cls.frozen_units = {r['unit_id']: r for r in csv.DictReader(io.StringIO(cls.frozen_raw['ega/units.csv'].decode(), newline=''))}
        target_paths = {t['path'] for t in cls.frozen['targets']} | {'tags/tags'}
        cls.frozen_blobs = {(c, p): subprocess.check_output(['git', 'show', c + ':' + p], cwd=ROOT)
                            for c in (contract.UPSTREAM, contract.TARGET_COMMIT) for p in target_paths}
        cls.frozen_tags = {line.split(',', 1)[1]: line.split(',', 1)[0]
                           for line in cls.frozen_blobs[contract.UPSTREAM, 'tags/tags'].decode().splitlines()
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
        return contract.verify(self.receipt, self.scope, self.tables, self.units,
            lambda c, p: self.blobs[c, p], self.tags, lambda p: self.raw[p])

    def test_live_candidate_receipt_dossier_and_actual_review(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(contract.receipt_errors(self.receipt_raw), [])
        self.assertEqual(contract.authority_errors(self.raw[contract.AUTHORITY['path']]), [])
        self.assertEqual(self.frozen['review_record']['path'], 'ega/i74-review.md')
        self.assertTrue(any(x['path'] == 'ega/i74-review.md' for x in self.frozen['reviewed_artifacts']))

    def test_seven_units_three_proofs_heading_ranktail_and_next_file(self):
        self.assertEqual(self.frozen['source_units'], ['ega:I.7.4.' + str(n) for n in range(1, 8)])
        self.assertEqual(self.frozen['source_proof_units'], ['ega:I.7.4.' + str(n) + ':proof' for n in (4, 5, 6)])
        self.assertEqual(len(self.frozen['english_discovery']['stable_units']), 12)
        self.assertEqual(self.frozen['owned_unnumbered_parts'], {'rank-tail': 'ega:I.7.4.2', '745-page-marker': 'ega:I.7.4.5'})
        self.assertEqual(self.frozen['next_semantic_cursor'], 'ega:I.8.1.1')
        for key in ('source_units', 'source_proof_units', 'owned_section_heading', 'owned_unnumbered_parts', 'next_semantic_cursor'):
            self.receipt = copy.deepcopy(self.frozen); self.receipt[key] = []
            self.assertTrue(self.errors(), key)

    def test_three_exact_source_versions_all_spans_and_unknown_versions(self):
        self.assertEqual(set(self.frozen['languages']), {'fr', 'en', 'errata_fr'})
        for version, source in self.frozen['languages'].items():
            for name, span in source['spans'].items():
                text = self.frozen['source_passages'][version]['spans'][name]['text'].encode()
                self.assertEqual((len(text), contract.digest(text)), (span['bytes'], span['sha256']))
                self.receipt = copy.deepcopy(self.frozen)
                del self.receipt['languages'][version]['spans'][name]
                self.assertTrue(self.errors(), (version, name))
            for other in set(self.frozen['languages']) - {version}:
                self.receipt = copy.deepcopy(self.frozen)
                self.receipt['languages'][version] = copy.deepcopy(self.frozen['languages'][other])
                self.assertTrue(self.errors(), (version, other))
        self.receipt = copy.deepcopy(self.frozen)
        self.receipt['languages']['unreviewed_8'] = {}
        self.assertTrue(self.errors())

    def test_known_printed_replacement_and_bounded_provenance_not_novel(self):
        obj = json.loads(self.raw[contract.AUTHORITY['path']])
        self.assertFalse(obj['implementation_visual_read'])
        self.assertEqual(obj['original_ega_i']['doi'], '10.1007/BF02684778')
        self.assertEqual([x['printed_page'] for x in obj['original_ega_i']['page_images']], [163, 164])
        self.assertEqual(obj['errata_list_2']['doi'], '10.1007/BF02684890')
        correction = obj['errata_list_2']['correction']
        self.assertEqual(correction['identifier'], 'Err_III 12')
        self.assertEqual((correction['article_printed_page'], correction['additional_printed_footer']), (88, 220))
        self.assertTrue(correction['replacement_is_explicit'])
        self.assertIn('not a novel correction', obj['outcome']['I.7.4.7'])
        self.assertIn('bounded', self.frozen['semantic_contract']['source_744'])
        for value in (None, b'', self.raw[contract.AUTHORITY['path']] + b' '):
            self.assertTrue(contract.authority_errors(value))

    def test_every_semantic_claim_type_and_unknown_claim_is_sealed(self):
        for key, value in self.frozen['semantic_contract'].items():
            for replacement in ([not value, int(value)] if isinstance(value, bool) else ['ADVERSE', None]):
                self.receipt = copy.deepcopy(self.frozen)
                self.receipt['semantic_contract'][key] = replacement
                self.assertTrue(self.errors(), key)
        self.receipt = copy.deepcopy(self.frozen)
        self.receipt['semantic_contract']['novel_error'] = True
        self.assertTrue(self.errors())

    def test_difficult_hypotheses_and_independent_weakenings_remain_distinct(self):
        s = self.frozen['semantic_contract']
        self.assertEqual(s['I741_category'], 'arbitrary O_X-module sheaves on integral X')
        self.assertIn('nonzero quasi-coherent', s['I743_converse'])
        self.assertIn('not residue-field', s['I744_skyscraper'])
        self.assertIn('qc unnecessary', s['I745_derived'])
        self.assertFalse(s['I745_pushforward_qc_claimed'])
        self.assertIn('arbitrary qc', s['I746_derived'])
        self.assertFalse(s['I746_proper_equals_nowhere_dense_without_ft'])
        self.assertFalse(s['I747_global_finite_components_required'])
        self.assertIn('every point', s['I747_corrected_hypothesis'])
        self.assertFalse(s['new_root_theorem'])

    def test_every_choice_has_actual_source_target_and_relevant_edges(self):
        manuscript = self.frozen_raw['ega/i74.md'].decode(); anchors = []
        edge_rows = next(x['rows'] for x in self.frozen['ledgers'] if x['path'] == 'ega/smap.csv')
        for choice in self.frozen['choices']:
            versions = {s['version'] for s in choice['source_versions']}
            self.assertEqual(versions, {'fr', 'en', 'errata_fr'} if choice['source_unit'].endswith('.7') else {'fr', 'en'})
            for source in choice['source_versions']:
                name = 'owned' if source['version'] == 'errata_fr' else choice['source_unit']
                expected = self.frozen['source_passages'][source['version']]['spans'][name]['text']
                self.assertEqual(source['source_text'], expected)
            for segment in choice['target_segments']:
                anchor = segment['target_segment_id']; anchors.append(anchor)
                marker = '<a id="' + anchor + '"></a>\n\n'
                self.assertEqual(manuscript.count(marker), 1)
                self.assertEqual(segment['target_text'], manuscript.split(marker, 1)[1].split('<a id="', 1)[0])
            self.assertEqual(choice['target_edges'], [r['edge_id'] for r in edge_rows if r['decision_id'] == choice['decision_id']])
            self.assertTrue(choice['meaningful_rejected_alternatives'])
            self.assertTrue(choice['consulted_canon'])
            self.assertIn('not a calibrated probability', choice['confidence_reason'])
        self.assertEqual(anchors, ['i74' + str(n) for n in range(1, 8)])

    def test_all17_paired_target_blocks_and_official_tag_joins_are_real(self):
        self.assertEqual(len(self.frozen['targets']), 17)
        for target in self.frozen['targets']:
            for edition, c in [('official', contract.UPSTREAM), ('integrated', contract.TARGET_COMMIT)]:
                self.blobs = dict(self.frozen_blobs); key = c, target['path']
                raw = self.blobs[key]; pos = target[edition]['byte_offset_start']
                self.blobs[key] = raw[:pos] + b'X' + raw[pos + 1:]
                self.assertTrue(self.errors(), (target['tag'], edition))
            self.blobs = dict(self.frozen_blobs); self.tags = dict(self.frozen_tags)
            self.tags[target['label']] = 'ZZZZ'; self.assertTrue(self.errors(), target['tag'])

    def test_whole_target_files_contexts_and_different_versions_bound(self):
        for key, raw in self.frozen_blobs.items():
            if key[1] == 'tags/tags': continue
            self.blobs = dict(self.frozen_blobs); self.blobs[key] = b'X' + raw[1:]
            self.assertTrue(self.errors(), key)
        self.blobs = dict(self.frozen_blobs)
        unequal = {t['tag'] for t in self.frozen['targets'] if t['official']['sha256'] != t['integrated']['sha256']}
        self.assertEqual(unequal, {'01B8', '01BA', '01RV', '01CB'})
        self.receipt['target_contexts'][0]['official']['text'] = 'invented'
        self.assertTrue(self.errors())

    def test_ledger_prefix_append_postimage_and_independent_runtime_view(self):
        for ledger in self.frozen['ledgers']:
            path = ledger['path']
            for mode in ('prefix', 'append', 'extra', 'crlf'):
                self.raw = dict(self.frozen_raw); raw = self.raw[path]
                if mode == 'prefix': raw = b'X' + raw[1:]
                elif mode == 'append':
                    n = ledger['prefix_bytes']; raw = raw[:n] + b'X' + raw[n + 1:]
                elif mode == 'extra': raw += b'ADVERSE\n'
                else: raw = raw.replace(b'\n', b'\r\n')
                self.raw[path] = raw; self.assertTrue(self.errors(), (path, mode))
        self.raw = dict(self.frozen_raw)
        self.tables['ega/smap.csv'].append(dict(self.tables['ega/smap.csv'][-1], edge_id='S999999'))
        self.assertTrue(self.errors())

    def test_twelve_prior_gaps_and_discovery_inventory_never_promoted(self):
        self.assertEqual(sum(r['status'] == 'open_gap' for r in self.tables['ega/resid.csv']), 12)
        next(r for r in self.tables['ega/resid.csv'] if r['status'] == 'open_gap')['status'] = 'covered_derived'
        self.assertTrue(self.errors())
        self.tables = copy.deepcopy(self.frozen_tables)
        self.units['ega:I.7.4.1']['review_state'] = 'reviewed_existing'; self.assertTrue(self.errors())
        self.units = copy.deepcopy(self.frozen_units)
        self.units['ega:I.7.4.2:rank'] = {'unit_id': 'ega:I.7.4.2:rank'}; self.assertTrue(self.errors())

    def test_current_scope_frontier_and_both_authority_scopes_bound(self):
        for key in ('next_semantic_cursor', 'reviewed_source_slices', 'reviewed_errata_slices', 'statement_review_snapshot', 'residual_snapshot'):
            self.scope = copy.deepcopy(self.frozen_scope); self.scope[key] = {}
            self.assertTrue(self.errors(), key)

    def test_dossier_damage_and_coordinated_rehash_cannot_self_authenticate(self):
        raw = self.frozen_raw['ega/i74.md']
        for old, new in [(b'nonzero quasi-coherent', b'arbitrary'),
                         (b'not through the\nresidue field', b'through the\nresidue field'),
                         (b'**any** torsion-free', b'**any** torsion'),
                         (b'every point has an open', b'X has an open'),
                         (b'proper support can be dense', b'proper support is nowhere dense')]:
            damaged = raw.replace(old, new); self.assertNotEqual(raw, damaged, old)
            expected = dict(contract.DOSSIER, bytes=len(damaged), sha256=contract.digest(damaged))
            self.assertTrue(contract.dossier_errors(damaged, expected))
            self.raw['ega/i74.md'] = damaged; self.assertTrue(self.errors())

    def test_actual_preserved_inputs_review_code_and_tests_bound(self):
        for item in self.frozen['preserved_inputs'] + self.frozen['reviewed_artifacts']:
            self.raw = dict(self.frozen_raw); self.raw[item['path']] += b'ADVERSE'
            self.assertTrue(self.errors(), item['path'])

    def test_exact_receipt_bytes_and_every_metadata_field_fail_closed(self):
        self.assertTrue(contract.receipt_errors(self.receipt_raw + b' '))
        self.assertTrue(contract.receipt_errors(None))
        for key in self.frozen:
            self.receipt = copy.deepcopy(self.frozen); self.receipt[key] = [None]
            self.assertTrue(self.errors(), key)

    def test_malformed_runtime_views_and_loaders_fail_closed(self):
        args = [self.receipt, self.scope, self.tables, self.units, lambda c, p: self.blobs[c, p], self.tags, lambda p: self.raw[p]]
        for index in range(len(args)):
            for value in (None, [], 'wrong'):
                bad = list(args); bad[index] = value
                self.assertTrue(contract.verify(*bad), (index, value))
        for path in self.frozen_tables:
            for value in (None, [None], [{'source_unit': []}], 'wrong'):
                self.tables = copy.deepcopy(self.frozen_tables); self.tables[path] = value
                self.assertTrue(self.errors(), (path, value))
        for value in (None, [], 'wrong'):
            self.assertTrue(contract.verify(self.frozen, self.frozen_scope, self.frozen_tables, self.frozen_units,
                lambda c, p: value, self.frozen_tags, lambda p: self.frozen_raw[p]))
            self.assertTrue(contract.verify(self.frozen, self.frozen_scope, self.frozen_tables, self.frozen_units,
                lambda c, p: self.frozen_blobs[c, p], self.frozen_tags, lambda p: value))


if __name__ == '__main__':
    unittest.main()
