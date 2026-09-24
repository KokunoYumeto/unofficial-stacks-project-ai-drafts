"""R57 registrar reservation, then candidate-only single-source materialization/replay."""
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
PRIOR = '4cc7ccca622d29ae9893496e71ed4a162d285c03'
WRITER = '01a0cc46-4ba8-77b1-9c55-33449e55fea7'
PREFIX = 'ai-integrated/candidates/commons/stacks/errata/r57'
BATCH_HASH = '6785D7297F8B7AF05D0118717AD7107646CAB2D4EB42CE415851694E120C73C5'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=['lease', 'materialize', 'revise', 'replay'])
    p.add_argument('--repo', type=Path, required=True)
    a = p.parse_args(); root = a.repo.resolve(); candidate = root / PREFIX
    def git(*args): return subprocess.run(['git', '-C', str(root), *args], capture_output=True, check=True).stdout
    def blob(ref, name): return git('show', ref + ':' + name)
    overlays_path = root / 'ai-integrated/registry/overlays.json'
    leases_path = root / 'ai-integrated/registry/leases.json'
    require(overlays_path.read_bytes() == blob(PRIOR, 'ai-integrated/registry/overlays.json'), 'Registry advanced')
    overlays = json.loads(overlays_path.read_bytes()); leases = json.loads(leases_path.read_bytes())
    raw = (CONTROL / 'FIELDS_CORRECTION_BATCH_INPUT_20260924.json').read_bytes()
    require(sha(raw) == BATCH_HASH, 'Batch changed')
    batch = json.loads(raw)
    require(batch['registry_sha256'] == sha(overlays_path.read_bytes()), 'Batch registry mismatch')
    from verify_fields_intake_review_20260925 import verify_proof_evidence
    review = json.loads((CONTROL/'FIELDS_INTAKE_REVIEW_20260924.json').read_bytes())
    verify_proof_evidence(review)
    require(batch['dependency_groups'] == review['dependency_groups'], 'Batch mathematical dependencies drifted')
    ids = [s for e in overlays['registered_entries'] for s in e['stable_ids'] if re.fullmatch(r'MC-STK-ERR-[0-9]+', s)]
    first = max(int(s.rsplit('-', 1)[-1]) for s in ids) + 1
    require(first == 1859 and len(batch['units']) == 47 and batch['operation_count'] == 56, 'Unexpected scope')
    sources = {s['source']: s for s in batch['sources']}
    require(set(sources) == {'fields.tex'}, 'Unexpected sources')
    if a.action == 'lease':
        require(git('rev-parse', 'HEAD').decode().strip() == PRIOR, 'HEAD advanced')
        require(leases_path.read_bytes() == blob(PRIOR, 'ai-integrated/registry/leases.json'), 'Lease registry dirty')
        require(not candidate.exists(), 'Candidate already exists')
        namespace = 'commons/stacks/errata/r57'
        for e in {e['lease_id']: e for e in leases['events']}.values():
            n = e['namespace']
            require(e['state'] != 'active' or not (n == namespace or n.startswith(namespace + '/') or namespace.startswith(n + '/')), 'Conflicting lease')
        number = max(int(e['lease_id'].split('-')[2]) for e in leases['events']) + 1
        event = {'event_id': f"lease-event-{len(leases['events'])+1:06d}", 'event': 'issued',
            'lease_id': f'stacks-lease-{number:06d}-errata-r57', 'namespace': namespace,
            'candidate_path': 'candidates/' + namespace, 'writer_task': WRITER,
            'upstream_commit': BASE, 'upstream_tree': TREE, 'issued_at_utc': now(),
            'state': 'active', 'writer_contract': 'candidates/CONTRACT.md'}
        require(number == 63 and event['event_id'] == 'lease-event-000122', 'Lease state advanced')
        leases['events'].append(event)
        from jsonschema import Draft202012Validator
        Draft202012Validator(json.loads((root/'ai-integrated/schemas/lease-registry.schema.json').read_bytes())).validate(leases)
        write(leases_path, leases); write(candidate/'LEASE.json', event)
        print(json.dumps({'action': 'lease', 'event': event, 'source_mutations': 0})); return
    lease = json.loads((candidate/'LEASE.json').read_bytes())
    require({e['lease_id']: e for e in leases['events']}[lease['lease_id']] == lease and lease['state'] == 'active' and lease['writer_task'] == WRITER, 'Not active writer')
    authorities = {name: blob(BASE, name) for name in sources}
    priors = {name: blob(PRIOR, name) for name in sources}
    for name in sources:
        require((root/name).read_bytes() == priors[name], 'Dirty cumulative source: '+name)
    if a.action in ('materialize', 'revise'):
        require(not (candidate/'candidate.manifest.json').exists(), 'Never revise a sealed candidate')
        require((candidate/'operation-spec.json').exists() == (a.action == 'revise'), 'Wrong materialization state')
        write(candidate/'evidence/prepared-batch.json', raw)
        for row in batch['evidence']:
            data = (CONTROL/row['path']).read_bytes()
            require(ident(data) == {'bytes': row['bytes'], 'sha256': row['sha256']}, 'Evidence drift: '+row['path'])
            write(candidate/'evidence'/Path(row['path']).name, data)
        for name in ('r57_candidate_20260925.py', 'r51_candidate_20260922.py'):
            write(candidate/'evidence'/name, (CONTROL/name).read_bytes())
        if a.action == 'revise':
            for failure in sorted(CONTROL.glob('R57_*BUILD_REGRESSION_20260923.json')):
                write(candidate/'evidence'/failure.name, failure.read_bytes())
        units, operations, maps, decisions, formula = [], [], [], [], []
        original_ops = {name: [o for u in batch['units'] if u['source'] == name for o in u['operations']] for name in sources}
        for i, u in enumerate(batch['units']):
            sid = f'MC-STK-ERR-{first+i:04d}'; name = u['source']
            kind = u['class'].removeprefix('accepted_missing_'); unit_ops = []
            for j, o in enumerate(u['operations'], 1):
                line_delta = sum(x['replacement_text'].count('\n')-x['old_text'].count('\n') for x in original_ops[name] if x['end_byte_exclusive'] <= o['start_byte'])
                op = {**o, 'source': name, 'stable_id': sid, 'producer_id': u['id'],
                    'producer_operation_id': o['operation_id'], 'operation_id': sid+f'-OP{j}', 'class': kind,
                    'source_start_line': o['line'], 'source_end_line': o['line']+o['old_text'].count('\n'),
                    'payload_start_line': o['line']+line_delta, 'payload_end_line': o['line']+line_delta+o['replacement_text'].count('\n'),
                    'old_bytes': len(o['old_text'].encode()), 'replacement_bytes': len(o['replacement_text'].encode())}
                unit_ops.append(op); operations.append(op)
            operation_ids = [o['operation_id'] for o in unit_ops]
            provenance = {'discovery': u.get('discovery'), 'related_existing_canonical_ids': u.get('related_existing_canonical_ids', []), 'proof_evidence': u.get('proof_evidence')}
            units.append({'id': sid, 'source': name, 'payload': 'payload/'+name, 'class': kind,
                'producer_id': u['id'], 'producer_ids': [u['id']], 'producer_occurrences': u['producer_occurrences'],
                'operation_ids': operation_ids, 'rationale': u['rationale'], 'status': 'accepted_candidate_not_admitted', **provenance})
            maps.append({'unit_id': sid, 'producer_id': u['id'], 'source': name, 'operation_ids': operation_ids,
                'producer_occurrences': u['producer_occurrences'], 'review': 'evidence/'+u['review_file'],
                'authority': 'authority/'+name, 'authority_sha256': sha(authorities[name]), 'payload': 'payload/'+name,
                'class': kind, 'rationale': u['rationale'], 'adverse_evidence': u['adverse_evidence'], 'operations': unit_ops, **provenance})
            decisions.append({'id': sid, 'decision': 'accept_bounded_correction', 'class': kind,
                'rationale': u['rationale'], 'adverse_evidence': u['adverse_evidence'], **provenance,
                'reviewer': 'OpenAI Codex - GPT-6 Astra, Ultra effort', 'human_review': False})
            formula.append({'unit_id': sid, 'class': kind, 'operation_ids': operation_ids,
                'formula_policy': 'Only the exact listed source spans change. Original mathematical data, labels, reference targets, citation keys and environments are retained. The normal decomposition includes its full proof and seven additional prerequisite references; mathematical dependency groups and complete proof notes are mandatory.'})
        require(len(units) == 47 and len(operations) == 56, 'Materialized count drift')
        write(candidate/'operation-spec.json', {'schema': 'mathematics-commons-stacks-operation-spec/v1', 'apply_order': 'descending_start_byte_per_source', 'operation_count': len(operations), 'operations': operations})
        write(candidate/'stable-units.json', {'schema': 'mathematics-commons-stacks-stable-units/v1', 'authority_commit': BASE, 'unit_count': len(units), 'units': units})
        write(candidate/'source-map.jsonl', ''.join(json.dumps(x, ensure_ascii=False)+'\n' for x in maps))
        if a.action == 'materialize':
            write(candidate/'decisions.jsonl', ''.join(json.dumps(x, ensure_ascii=False)+'\n' for x in decisions))
        else:
            original_decisions = [json.loads(x) for x in (candidate/'decisions.jsonl').read_text(encoding='utf-8').splitlines()]
            require(original_decisions == decisions, 'Decision changes need an explicit append-only supersession')
        rejected = []
        for review_file in sorted({u['review_file'] for u in batch['units']}):
            review = json.loads((CONTROL/review_file).read_bytes())
            rejected += [g for g in review['groups'] if g['id'] not in {u['id'] for u in batch['units']} and not g.get('canonical_ids')]
        require(len(rejected) == 9, 'Rejected/optional coverage changed')
        write(candidate/'rejections.jsonl', ''.join(json.dumps(g, ensure_ascii=False)+'\n' for g in rejected))
        canonical = {u['producer_id']:u['id'] for u in units}
        dependencies = [{**group, 'stable_ids':[canonical[rid] for rid in group['review_ids']]} for group in batch['dependency_groups']]
        write(candidate/'formula-diagram-inventory.json', {'units': formula, 'dependency_groups': dependencies})
        write(candidate/'mathematical-proof-dependencies.json', {'groups': dependencies, 'required_proof_evidence': review['required_proof_evidence']})
        source_receipts = []
        for name, source in sources.items():
            authority, prior = authorities[name], priors[name]
            isolated = replay(authority, [o for o in operations if o['source'] == name])
            cumulative = replay(prior, source['rebound_operations'])
            for data, key in ((authority, 'authority'), (prior, 'cumulative_preimage'), (isolated, 'prospective_isolated_postimage'), (cumulative, 'prospective_cumulative_postimage')):
                require(ident(data) == source[key], 'Identity mismatch: '+name+'/'+key)
            for folder, data in [('authority', authority), ('payload', isolated), ('cumulative-preview', cumulative), ('proof-source/prior', prior), ('proof-source/successor', cumulative)]:
                write(candidate/folder/name, data)
            source_receipts.append({'source': name, 'authority': ident(authority), 'prior': ident(prior), 'isolated': ident(isolated), 'cumulative': ident(cumulative)})
        for dependency in ('preamble.tex', 'stacks-project.cls', 'chapters.tex', 'my.bib'):
            for version in ('prior', 'successor'): write(candidate/'proof-source'/version/dependency, blob(PRIOR, dependency))
        write(candidate/'proof-source/COPYING', blob(BASE, 'COPYING'))
        write(candidate/'materialization.json', {'schema': 'stacks-r57-materialization/v1', 'candidate_id': 'stacks-errata-a04446e-r57',
            'prior_public': PRIOR, 'authority': BASE, 'input_batch_sha256': BATCH_HASH, 'unit_count': len(units),
            'operation_count': len(operations), 'sources': source_receipts, 'source_mutations': 0, 'admission': False, 'created_at_utc': now()})
        text = ['# Fields: corrections and complete decomposition proof\n',
            '47 proposed corrections and clarifications: 21 copyedits, 21 source corrections and five clarifications. All 75 received reports retain their decisions and adverse evidence, including optional proposals and previously composed repairs. All eight earlier Fields corrections remain intact. The normal algebraic decomposition now has its complete multiplication-map proof. The transcendence-basis statement exposes the extension property already proved in its source. Further consequences are proved separately in the retained proof evidence; no new theorem is mislabelled as a received defect.\n',
            'Prepared and reviewed by OpenAI Codex — GPT-6 Astra, Ultra effort. No human review, official acceptance or upstream endorsement is claimed.\n']
        for u in units:
            text.extend([f"## {u['id']} — {u['producer_id']} ({u['class']})\n", u['rationale']+'\n'])
            for op in [o for o in operations if o['stable_id'] == u['id']]:
                text.extend([f"Official {op['source']} line {op['line']}:\n", '```tex\n'+op['old_text']+'\n```\n', 'Replace with:\n', '```tex\n'+op['replacement_text']+'\n```\n'])
        write(candidate/'REVIEW.md', '\n'.join(text))
        print(json.dumps({'action': 'materialize', 'units': len(units), 'operations': len(operations), 'ids': [units[0]['id'], units[-1]['id']], 'source_mutations': 0})); return
    verify_proof_evidence(json.loads((candidate/'evidence/FIELDS_INTAKE_REVIEW_20260924.json').read_bytes()), candidate/'evidence')
    retained = json.loads((candidate/'mathematical-proof-dependencies.json').read_bytes())
    canonical = {u['producer_id']:u['id'] for u in json.loads((candidate/'stable-units.json').read_bytes())['units']}
    require(retained['groups'] == [{**g, 'stable_ids':[canonical[rid] for rid in g['review_ids']]} for g in batch['dependency_groups']], 'Candidate dependency loss')
    require(retained['required_proof_evidence'] == review['required_proof_evidence'], 'Candidate proof evidence loss')
    operations = json.loads((candidate/'operation-spec.json').read_bytes())['operations']; checks = []
    for name, source in sources.items():
        authority, prior = authorities[name], priors[name]
        isolated = replay(authority, [o for o in operations if o['source'] == name])
        cumulative = replay(prior, source['rebound_operations'])
        require(isolated == (candidate/'payload'/name).read_bytes(), 'Isolated replay mismatch: '+name)
        require(cumulative == (candidate/'cumulative-preview'/name).read_bytes(), 'Cumulative replay mismatch: '+name)
        from verify_fields_intake_review_20260925 import verify_structure
        original_bound = [{**o, 'review_id':o['producer_id']} for o in operations if o['source']==name]
        cumulative_bound = [{**o, 'review_id':o['operation_id'].rsplit('-OP',1)[0]} for o in source['rebound_operations']]
        reference_checks = []
        for before, after, bound in ((authority, isolated, original_bound), (prior, cumulative, cumulative_bound)):
            reference_checks.append(verify_structure(before, after, bound))
            pattern = rb'\\(?:begin|end)\{([^}]+)\}'
            require(re.findall(pattern, before) == re.findall(pattern, after), 'Environment drift')
        checks.append({'source':name,'passed':True,'isolated':ident(isolated),'cumulative':ident(cumulative),
            'labels_citation_keys_environments_unchanged':True,'bound_reference_changes':reference_checks,
            'other_references_unchanged':True})
    write(candidate/'replay/source-replay.json', {'schema': 'stacks-r57-independent-source-replay/v1', 'candidate_id': 'stacks-errata-a04446e-r57',
        'passed': True, 'checks': checks,
        'scope': 'Separate executable replay from frozen Git preimages in the same primary AI task; no second AI or human reviewer claimed. Build and visual gates remain separate.',
        'reviewer': 'OpenAI Codex - GPT-6 Astra, Ultra effort', 'created_at_utc': now()})
    print(json.dumps({'action': 'replay', 'passed': True, 'sources': len(checks)}))


if __name__ == '__main__': main()
