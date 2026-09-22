"""Separate R52 registrar reservation and candidate-only materialization/replay."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
from r51_candidate_20260922 import sha, ident, now, require, write, replay

CONTROL = Path(__file__).resolve().parent
BASE = 'a04446e57ec1fbc252a871afcec7752fb2807b14'
TREE = '3feeb703b931a6e7259782c10e7d1575adc83e5e'
PRIOR = '0755a4cee48442859b7ec315c581108a12445663'
WRITER = '019fca5a-c29e-7330-acdc-c93f4a3dc9fb'
PREFIX = 'ai-integrated/candidates/commons/stacks/errata/r52'
BATCH_HASH = 'D6EF326D2A7B97FE87A57EEEB8EB15BF93DEEE798FE5D4DA227B91CE7C67ADF9'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=['lease', 'materialize', 'replay'])
    p.add_argument('--repo', type=Path, required=True)
    a = p.parse_args(); root = a.repo.resolve(); candidate = root / PREFIX
    def git(*args): return subprocess.run(['git', '-C', str(root), *args], capture_output=True, check=True).stdout
    def blob(ref, name): return git('show', ref + ':' + name)
    overlays_path = root / 'ai-integrated/registry/overlays.json'
    leases_path = root / 'ai-integrated/registry/leases.json'
    require(overlays_path.read_bytes() == blob(PRIOR, 'ai-integrated/registry/overlays.json'), 'Registry advanced')
    overlays = json.loads(overlays_path.read_bytes()); leases = json.loads(leases_path.read_bytes())
    raw = (CONTROL / 'CATEGORIES_CORRECTION_BATCH_INPUT_20260922.json').read_bytes()
    require(sha(raw) == BATCH_HASH, 'Batch changed')
    batch = json.loads(raw)
    require(batch['registry_sha256'] == sha(overlays_path.read_bytes()), 'Batch registry mismatch')
    ids = [s for e in overlays['registered_entries'] for s in e['stable_ids'] if re.fullmatch(r'MC-STK-ERR-[0-9]+', s)]
    first = max(int(s.rsplit('-', 1)[-1]) for s in ids) + 1
    require(first == 1605 and len(batch['units']) == 83 and batch['operation_count'] == 107, 'Unexpected scope')
    require(len(batch['sources']) == 1 and batch['sources'][0]['source'] == 'categories.tex', 'Unexpected source')
    if a.action == 'lease':
        require(git('rev-parse', 'HEAD').decode().strip() == PRIOR, 'HEAD advanced')
        require(not candidate.exists(), 'Candidate already exists')
        namespace = 'commons/stacks/errata/r52'
        latest = {e['lease_id']: e for e in leases['events']}
        for e in latest.values():
            n = e['namespace']
            require(e['state'] != 'active' or not (n == namespace or n.startswith(namespace + '/') or namespace.startswith(n + '/')), 'Conflicting lease')
        number = max(int(e['lease_id'].split('-')[2]) for e in leases['events']) + 1
        event = {'event_id': f"lease-event-{len(leases['events'])+1:06d}", 'event': 'issued',
            'lease_id': f'stacks-lease-{number:06d}-errata-r52', 'namespace': namespace,
            'candidate_path': 'candidates/' + namespace, 'writer_task': WRITER,
            'upstream_commit': BASE, 'upstream_tree': TREE, 'issued_at_utc': now(),
            'state': 'active', 'writer_contract': 'candidates/CONTRACT.md'}
        require(number == 57 and event['event_id'] == 'lease-event-000110', 'Lease state advanced')
        leases['events'].append(event)
        from jsonschema import Draft202012Validator
        Draft202012Validator(json.loads((root/'ai-integrated/schemas/lease-registry.schema.json').read_bytes())).validate(leases)
        write(leases_path, leases); write(candidate/'LEASE.json', event)
        print(json.dumps({'action': 'lease', 'event': event, 'source_mutations': 0})); return
    lease = json.loads((candidate/'LEASE.json').read_bytes())
    require({e['lease_id']: e for e in leases['events']}[lease['lease_id']] == lease and lease['state'] == 'active' and lease['writer_task'] == WRITER, 'Not active writer')
    source = batch['sources'][0]; name = source['source']
    authority, prior = blob(BASE, name), blob(PRIOR, name)
    require((root/name).read_bytes() == prior, 'Dirty cumulative Categories source')
    if a.action == 'materialize':
        require(not (candidate/'operation-spec.json').exists(), 'Already materialized')
        write(candidate/'evidence/prepared-batch.json', raw)
        for row in batch['evidence']:
            data = (CONTROL/row['path']).read_bytes()
            require(ident(data) == {'bytes': row['bytes'], 'sha256': row['sha256']}, 'Evidence drift: '+row['path'])
            write(candidate/'evidence'/Path(row['path']).name, data)
        for name_ in ('r52_candidate_20260922.py', 'r51_candidate_20260922.py'):
            write(candidate/'evidence'/name_, (CONTROL/name_).read_bytes())
        review = json.loads((CONTROL/'CATEGORIES_INTAKE_REVIEW_20260922.json').read_bytes())
        units, operations, maps, decisions, formula = [], [], [], [], []
        all_original_ops = [o for u in batch['units'] for o in u['operations']]
        for i, u in enumerate(batch['units']):
            sid = f'MC-STK-ERR-{first+i:04d}'
            kind = u['class'].removeprefix('accepted_missing_')
            unit_ops = []
            for j, o in enumerate(u['operations'], 1):
                line_delta = sum(x['replacement_text'].count('\n')-x['old_text'].count('\n') for x in all_original_ops if x['end_byte_exclusive'] <= o['start_byte'])
                op = {**o, 'source': name, 'stable_id': sid, 'producer_id': u['id'],
                    'producer_operation_id': o['operation_id'], 'operation_id': sid+f'-OP{j}', 'class': kind,
                    'source_start_line': o['line'], 'source_end_line': o['line']+o['old_text'].count('\n'),
                    'payload_start_line': o['line']+line_delta, 'payload_end_line': o['line']+line_delta+o['replacement_text'].count('\n'),
                    'old_bytes': len(o['old_text'].encode()), 'replacement_bytes': len(o['replacement_text'].encode())}
                unit_ops.append(op); operations.append(op)
            ids_ = [o['operation_id'] for o in unit_ops]
            units.append({'id': sid, 'source': name, 'payload': 'payload/'+name, 'class': kind,
                'producer_id': u['id'], 'producer_ids': [u['id']], 'producer_occurrences': u['producer_occurrences'],
                'operation_ids': ids_, 'rationale': u['rationale'], 'status': 'accepted_candidate_not_admitted',
                'discovery': u.get('discovery'), 'occurrence_dispositions': u.get('occurrence_dispositions', {})})
            maps.append({'unit_id': sid, 'producer_id': u['id'], 'source': name, 'operation_ids': ids_,
                'producer_occurrences': u['producer_occurrences'], 'review': 'evidence/'+u['review_file'],
                'authority': 'authority/'+name, 'authority_sha256': sha(authority), 'payload': 'payload/'+name,
                'class': kind, 'rationale': u['rationale'], 'adverse_evidence': u['adverse_evidence'], 'operations': unit_ops})
            decisions.append({'id': sid, 'decision': 'accept_bounded_correction', 'class': kind,
                'rationale': u['rationale'], 'adverse_evidence': u['adverse_evidence'],
                'occurrence_dispositions': u.get('occurrence_dispositions', {}),
                'reviewer': 'OpenAI Codex - GPT-6 Astra, Ultra effort', 'human_review': False})
            formula.append({'unit_id': sid, 'class': kind, 'operation_ids': ids_,
                'formula_policy': 'Only listed tokens change; label, reference, citation and environment inventories are invariant.'})
        write(candidate/'operation-spec.json', {'schema': 'mathematics-commons-stacks-operation-spec/v1', 'apply_order': 'descending_start_byte_per_source', 'operation_count': len(operations), 'operations': operations})
        write(candidate/'stable-units.json', {'schema': 'mathematics-commons-stacks-stable-units/v1', 'authority_commit': BASE, 'unit_count': len(units), 'units': units})
        write(candidate/'source-map.jsonl', ''.join(json.dumps(x, ensure_ascii=False)+'\n' for x in maps))
        write(candidate/'decisions.jsonl', ''.join(json.dumps(x, ensure_ascii=False)+'\n' for x in decisions))
        rejected = [g for g in review['groups'] if g['id'] not in {u['id'] for u in batch['units']} and not g['canonical_ids']]
        require(len(rejected) == 23, 'Rejected/optional coverage changed')
        write(candidate/'rejections.jsonl', ''.join(json.dumps(g, ensure_ascii=False)+'\n' for g in rejected))
        write(candidate/'formula-diagram-inventory.json', {'units': formula, 'dependency_groups': []})
        isolated = replay(authority, operations); cumulative = replay(prior, source['rebound_operations'])
        for data, key in ((authority, 'authority'), (prior, 'cumulative_preimage'), (isolated, 'prospective_isolated_postimage'), (cumulative, 'prospective_cumulative_postimage')):
            require(ident(data) == source[key], 'Identity mismatch: '+key)
        for folder, data in [('authority', authority), ('payload', isolated), ('cumulative-preview', cumulative), ('proof-source/prior', prior), ('proof-source/successor', cumulative)]:
            write(candidate/folder/name, data)
        for dependency in ('preamble.tex', 'stacks-project.cls', 'chapters.tex', 'my.bib'):
            for version in ('prior', 'successor'): write(candidate/'proof-source'/version/dependency, blob(PRIOR, dependency))
        write(candidate/'proof-source/COPYING', blob(BASE, 'COPYING'))
        write(candidate/'materialization.json', {'schema': 'stacks-r52-materialization/v1', 'candidate_id': 'stacks-errata-a04446e-r52',
            'prior_public': PRIOR, 'authority': BASE, 'input_batch_sha256': BATCH_HASH, 'unit_count': len(units),
            'operation_count': len(operations), 'sources': [{'source': name, 'authority': ident(authority), 'prior': ident(prior), 'isolated': ident(isolated), 'cumulative': ident(cumulative)}],
            'source_mutations': 0, 'admission': False, 'created_at_utc': now()})
        text = ['# Categories: proposed corrections and clarifications\n',
            '83 proposed changes: 51 copyedits, 11 clarifications and 21 source corrections. These are not 83 new mathematical errors or theorems. The complete intake review retains all 165 reports, duplicates, rejected claims and adverse evidence.\n',
            'Prepared and reviewed by OpenAI Codex — GPT-6 Astra, Ultra effort. No human review, official acceptance or upstream endorsement is claimed.\n']
        for u in units:
            text.extend([f"## {u['id']} — {u['producer_id']} ({u['class']})\n", u['rationale']+'\n'])
            for op in [o for o in operations if o['stable_id'] == u['id']]:
                text.extend([f"Official source line {op['line']}:\n", '```tex\n'+op['old_text']+'\n```\n', 'Replace with:\n', '```tex\n'+op['replacement_text']+'\n```\n'])
        write(candidate/'REVIEW.md', '\n'.join(text))
        print(json.dumps({'action': 'materialize', 'units': len(units), 'operations': len(operations), 'ids': [units[0]['id'], units[-1]['id']], 'source_mutations': 0})); return
    operations = json.loads((candidate/'operation-spec.json').read_bytes())['operations']
    isolated = replay(authority, operations); cumulative = replay(prior, source['rebound_operations'])
    require(isolated == (candidate/'payload'/name).read_bytes(), 'Isolated replay mismatch')
    require(cumulative == (candidate/'cumulative-preview'/name).read_bytes(), 'Cumulative replay mismatch')
    for before, after in ((authority, isolated), (prior, cumulative)):
        for pattern in (rb'\\label\{([^}]+)\}', rb'\\(?:ref|eqref|cite)\{([^}]+)\}', rb'\\(?:begin|end)\{([^}]+)\}'):
            require(Counter(re.findall(pattern, before)) == Counter(re.findall(pattern, after)), 'Structure/reference drift')
    write(candidate/'replay/source-replay.json', {'schema': 'stacks-r52-independent-source-replay/v1', 'candidate_id': 'stacks-errata-a04446e-r52',
        'passed': True, 'checks': [{'source': name, 'passed': True, 'isolated': ident(isolated), 'cumulative': ident(cumulative), 'labels_refs_citations_environments_unchanged': True}],
        'scope': 'Separate executable replay from frozen Git preimages in the same primary AI task; no second AI or human reviewer claimed. Build and visual gates remain separate.',
        'reviewer': 'OpenAI Codex - GPT-6 Astra, Ultra effort', 'created_at_utc': now()})
    print(json.dumps({'action': 'replay', 'passed': True, 'sources': 1}))


if __name__ == '__main__': main()
