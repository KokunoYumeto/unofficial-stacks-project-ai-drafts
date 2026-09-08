"""Independent adverse fixtures for I7.2.8--9; not formal mathematics tests."""
import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import unittest

from tools import ega_i729_semantic_contract as contract

ROOT = Path(__file__).resolve().parents[1]


class Semantic729Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt_raw = (ROOT / contract.RECEIPT_PATH).read_bytes()
        cls.frozen = json.loads(cls.receipt_raw)
        cls.frozen_scope = json.loads((ROOT / 'ega/scope.json').read_text(encoding='utf-8'))
        paths = {x['path'] for x in cls.frozen['preserved_inputs']}
        paths |= {x['path'] for x in cls.frozen['ledgers']} | {'ega/i729.md'}
        cls.frozen_raw = {p: (ROOT / p).read_bytes() for p in paths}
        cls.live_raw = dict(cls.frozen_raw)
        cls.frozen_scope, projected, historical_loader = contract.historical_inputs(
            cls.frozen, cls.frozen_scope, lambda p: cls.live_raw[p])
        cls.frozen_raw = {p: historical_loader(p) for p in paths}
        cls.frozen_tables = {}
        for ledger in cls.frozen['ledgers']:
            rows = list(csv.DictReader(io.StringIO(cls.frozen_raw[ledger['path']].decode(), newline='')))
            superseded = {r.get('supersedes') for r in rows if r.get('supersedes')}
            cls.frozen_tables[ledger['path']] = [r for r in rows if r[ledger['id_field']] not in superseded]
        cls.frozen_units = {r['unit_id']: r for r in csv.DictReader(io.StringIO(cls.frozen_raw['ega/units.csv'].decode(), newline=''))}
        target_paths = {t['path'] for t in cls.frozen['targets']} | {'tags/tags'}
        cls.frozen_blobs = {(commit, path): subprocess.check_output(['git', 'show', commit + ':' + path], cwd=ROOT)
                            for commit in (contract.UPSTREAM, contract.BASE) for path in target_paths}
        cls.frozen_tags = {line.split(',', 1)[1]: line.split(',', 1)[0]
                           for line in cls.frozen_blobs[contract.UPSTREAM, 'tags/tags'].decode().splitlines()
                           if line and not line.startswith('#')}

    def setUp(self):
        self.receipt = copy.deepcopy(self.frozen)
        self.scope = copy.deepcopy(self.frozen_scope)
        self.tables = copy.deepcopy(self.frozen_tables)
        self.units = dict(self.frozen_units)
        self.raw = dict(self.frozen_raw)
        self.blobs = dict(self.frozen_blobs)
        self.tags = dict(self.frozen_tags)

    def errors(self):
        return contract.verify(self.receipt, self.scope, self.tables, self.units,
                               lambda c, p: self.blobs[c, p], self.tags, lambda p: self.raw[p])

    def test_frozen_candidate_and_receipt_pass(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(contract.receipt_errors(self.receipt_raw), [])

    def test_exact_five_units_not_six_and_parent_ownership(self):
        historical_scope, historical_tables, loader = contract.historical_inputs(
            self.receipt, self.scope, lambda p: self.live_raw[p])
        self.assertEqual(historical_tables, self.frozen_tables)
        for ledger in self.receipt["ledgers"]:
            self.assertEqual(loader(ledger["path"]), self.frozen_raw[ledger["path"]])
        self.assertEqual([r['unit_id'] for r in self.receipt['english_discovery']['stable_units']],
                         ['ega:I.7.2.8', 'ega:I.7.2.8.1', 'ega:I.7.2.8.1:proof', 'ega:I.7.2.9', 'ega:I.7.2.9:proof'])
        self.assertEqual(self.receipt['owned_unnumbered_parts'], {'ega:I.7.2.8:induced-map': 'ega:I.7.2.8'})
        self.receipt['source_proof_units'].append('ega:I.7.2.8:proof')
        self.assertTrue(self.errors())

    def test_each_semantic_claim_and_numeric_boolean_substitution_rejected(self):
        for key, value in self.frozen['semantic_contract'].items():
            for replacement in ([not value, int(value)] if isinstance(value, bool) else ['ADVERSE']):
                with self.subTest(key=key, replacement=replacement):
                    self.receipt = copy.deepcopy(self.frozen)
                    self.receipt['semantic_contract'][key] = replacement
                    self.assertTrue(self.errors())

    def test_unknown_claim_and_ordinary_relative_repair_rejected(self):
        self.receipt['semantic_contract']['ordinary_domain_equals_relative_domain'] = True
        self.assertTrue(self.errors())
        self.receipt = copy.deepcopy(self.frozen)
        self.receipt['semantic_contract']['I729_ordinary_local_morphism_suffices'] = True
        self.assertTrue(self.errors())

    def test_next_heading_cannot_be_covered_or_advanced(self):
        for key, value in [('next_semantic_cursor', 'ega:I.7.3.1'),
                           ('next_cursor_starts_with_numbered_environment', True),
                           ('starting_content_commit', contract.UPSTREAM)]:
            self.receipt = copy.deepcopy(self.frozen)
            self.receipt[key] = value
            self.assertTrue(self.errors(), key)

    def test_every_bilingual_owner_must_remain_complete_even_after_rehash(self):
        for lang in ('fr', 'en'):
            for section in ('slices', 'numbered_environments', 'owned_parts', 'page_markers'):
                for owner in self.frozen['languages'][lang][section]:
                    for mode in ('omit', 'truncate', 'reassign', 'rehash'):
                        self.receipt = copy.deepcopy(self.frozen)
                        spans = self.receipt['languages'][lang][section]
                        if mode == 'omit':
                            del spans[owner]
                        elif mode == 'truncate':
                            spans[owner]['lf_line_end'] -= 1
                        elif mode == 'reassign':
                            spans['ega:I.7.2.8:proof'] = spans.pop(owner)
                        else:
                            spans[owner]['sha256'] = '0' * 64
                        self.assertTrue(self.errors(), (lang, section, owner, mode))

    def test_nested_proof_cannot_absorb_parent_induced_map(self):
        for lang, end in [('fr', 485), ('en', 287)]:
            self.receipt = copy.deepcopy(self.frozen)
            self.receipt['languages'][lang]['owned_parts']['ega:I.7.2.8.1:proof']['lf_line_end'] = end
            del self.receipt['languages'][lang]['owned_parts']['ega:I.7.2.8:induced-map']
            self.assertTrue(self.errors())

    def test_source_scope_and_live_snapshot_mutations_rejected(self):
        for key in ('statement_review_snapshot', 'residual_snapshot', 'reviewed_source_slices'):
            self.scope = copy.deepcopy(self.frozen_scope)
            self.scope[key] = {}
            self.assertTrue(self.errors(), key)

    def test_receipt_cannot_supply_its_own_rehashed_identity(self):
        raw = self.receipt_raw.replace(b'"SEMANTIC_CANDIDATE"', b'"COMPLETE_EGA"')
        self.assertNotEqual(raw, self.receipt_raw)
        self.assertTrue(contract.receipt_errors(raw))

    def test_dossier_semantic_damage_rejected_even_after_rehash(self):
        raw = self.raw['ega/i729.md']
        cases = [
            (b'coordinate\nrings need not be Noetherian', b'coordinate\nrings must be Noetherian'),
            (b'The last globalization step matters:', b'The last globalization step is omitted:'),
            (b'and $T_a=0$ for other indices', b'and $T_a=1$ for other indices'),
            (b'Finally, $h$ is not over $S$', b'Finally, $h$ is over $S$'),
            (b'separatedness (hence quasi-separatedness)', b'no additional hypotheses'),
        ]
        for before, after in cases:
            damaged = raw.replace(before, after)
            self.assertNotEqual(damaged, raw, before)
            rehashed = dict(contract.DOSSIER, bytes=len(damaged), sha256=hashlib.sha256(damaged).hexdigest().upper())
            self.assertTrue(contract.dossier_errors(damaged, rehashed))
            self.raw['ega/i729.md'] = damaged
            self.assertTrue(self.errors())

    def test_each_official_and_integrated_target_actual_bytes_are_replayed(self):
        for target in self.frozen['targets']:
            for edition, commit in [('official', contract.UPSTREAM), ('integrated', contract.BASE)]:
                with self.subTest(tag=target['tag'], edition=edition):
                    self.blobs = dict(self.frozen_blobs)
                    key = commit, target['path']
                    lines = self.blobs[key].splitlines(keepends=True)
                    lines[target[edition]['lf_line_end'] - 1] = b'ADVERSE\n'
                    self.blobs[key] = b''.join(lines)
                    self.assertTrue(self.errors())

    def test_unequal_current_blocks_cannot_replace_official_evidence(self):
        unequal = {t['tag'] for t in self.frozen['targets'] if t['official']['sha256'] != t['integrated']['sha256']}
        self.assertEqual(unequal, {'00E3', '0052', '01JB'})
        for target in self.frozen['targets']:
            if target['tag'] in unequal:
                self.receipt = copy.deepcopy(self.frozen)
                row = next(t for t in self.receipt['targets'] if t['tag'] == target['tag'])
                row['official'] = copy.deepcopy(row['integrated'])
                self.assertTrue(self.errors())

    def test_seed_and_comparison_targets_cannot_be_promoted(self):
        for tag in ('00PB', '01TT', '0BX8'):
            self.receipt = copy.deepcopy(self.frozen)
            next(t for t in self.receipt['targets'] if t['tag'] == tag)['role'] = 'full_equivalent_theorem'
            self.assertTrue(self.errors())

    def test_tag_label_join_damage_rejected(self):
        for target in self.frozen['targets']:
            self.tags = dict(self.frozen_tags)
            self.tags[target['label']] = 'ZZZZ'
            self.assertTrue(self.errors())

    def test_ledger_actual_append_prefix_and_line_endings_independently_checked(self):
        for ledger in self.frozen['ledgers']:
            path = ledger['path']
            for mode in ('prefix', 'append', 'extra', 'crlf'):
                self.raw = dict(self.frozen_raw)
                raw = self.raw[path]
                if mode == 'prefix':
                    raw = b'X' + raw[1:]
                elif mode == 'append':
                    raw = raw[:ledger['prefix_bytes']] + b'X' + raw[ledger['prefix_bytes'] + 1:]
                elif mode == 'extra':
                    raw += b'ADVERSE\n'
                else:
                    raw = raw.replace(b'\n', b'\r\n')
                self.raw[path] = raw
                self.assertTrue(self.errors(), (path, mode))

    def test_coordinated_receipt_and_table_rehash_cannot_change_rows(self):
        for ledger in self.frozen['ledgers']:
            self.receipt = copy.deepcopy(self.frozen)
            self.tables = copy.deepcopy(self.frozen_tables)
            row = next(l for l in self.receipt['ledgers'] if l['path'] == ledger['path'])['rows'][0]
            key = ledger['id_field']
            identity = row[key]
            field = 'rationale' if key == 'decision_id' else 'evidence' if key in ('edge_id', 'residual_id') else 'returned'
            row[field] = 'ADVERSE'
            next(r for r in self.tables[ledger['path']] if r[key] == identity)[field] = 'ADVERSE'
            self.assertTrue(self.errors())

    def test_prior_twelve_open_gaps_cannot_close(self):
        rows = self.tables['ega/resid.csv']
        self.assertEqual(sum(r['status'] == 'open_gap' for r in rows), 12)
        next(r for r in rows if r['status'] == 'open_gap')['status'] = 'covered_derived'
        self.assertTrue(self.errors())

    def test_discovery_promotion_and_extra_source_rows_rejected(self):
        for unit in contract.UNITS + contract.PROOFS:
            self.units = copy.deepcopy(self.frozen_units)
            self.units[unit]['review_state'] = 'reviewed_existing'
            self.assertTrue(self.errors())
        self.units = dict(self.frozen_units)
        self.tables['ega/smap.csv'].append(dict(self.tables['ega/smap.csv'][-1], edge_id='S001445'))
        self.assertTrue(self.errors())

    def test_runtime_discovery_cannot_invent_a_parent_proof_or_prose_unit(self):
        for identity in ('ega:I.7.2.8:proof', 'ega:I.7.2.8:induced-map'):
            self.units = dict(self.frozen_units)
            self.units[identity] = {'unit_id': identity, 'kind': 'proof', 'parent_id': 'ega:I.7.2.8'}
            self.assertTrue(self.errors(), identity)

    def test_each_preserved_input_checked_as_actual_bytes(self):
        for item in self.frozen['preserved_inputs']:
            self.raw = dict(self.frozen_raw)
            self.raw[item['path']] += b'ADVERSE'
            self.assertTrue(self.errors(), item['path'])

    def test_malformed_top_level_inputs_fail_closed(self):
        for ledger in self.receipt["ledgers"]:
            damaged = dict(self.live_raw)
            damaged[ledger["path"]] = b"X" + damaged[ledger["path"]][1:]
            with self.assertRaises(ValueError):
                contract.historical_inputs(self.receipt, self.scope, lambda p: damaged[p])
        original = [self.receipt, self.scope, self.tables, self.units,
                    lambda c, p: self.blobs[c, p], self.tags, lambda p: self.raw[p]]
        for index in range(len(original)):
            for value in (None, [], 'not an object'):
                arguments = list(original)
                arguments[index] = value
                self.assertTrue(contract.verify(*arguments), (index, value))

    def test_malformed_nested_metadata_and_rows_fail_closed(self):
        for key in self.frozen:
            self.receipt = copy.deepcopy(self.frozen)
            self.receipt[key] = [None]
            self.assertTrue(self.errors(), key)
        self.receipt = copy.deepcopy(self.frozen)
        for path in self.frozen_tables:
            for value in (None, [None], [{'source_unit': []}], 'wrong'):
                self.tables = copy.deepcopy(self.frozen_tables)
                self.tables[path] = value
                self.assertTrue(self.errors(), (path, value))

    def test_unavailable_or_nonbyte_loaders_fail_closed(self):
        for value in (None, [], 'wrong'):
            self.assertTrue(contract.verify(self.receipt, self.scope, self.tables, self.units,
                                           lambda c, p: value, self.tags, lambda p: self.raw[p]))
            self.assertTrue(contract.verify(self.receipt, self.scope, self.tables, self.units,
                                           lambda c, p: self.blobs[c, p], self.tags, lambda p: value))


if __name__ == '__main__':
    unittest.main()
