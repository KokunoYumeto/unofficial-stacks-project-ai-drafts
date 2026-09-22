"""Separate R50 admission and exact composition; immutable candidate evidence."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PREVIOUS = '6be831dd98aa333eff6e3f045cf84346dd86f7a6'
CANDIDATE_COMMIT = 'bc6541c0e06bacf64afe843691a1b5a828bd95f5'
MANIFEST = 'F2B9802F08ADD61B6C63489CAFA705242C70379C087974823877834E43C9AB77'
AUTHORITY = 'a04446e57ec1fbc252a871afcec7752fb2807b14'
ID = 'stacks-errata-a04446e-r50'
PREFIX = 'ai-integrated/candidates/commons/stacks/errata/r50/'
OVERLAYS = 'ai-integrated/registry/overlays.json'
LEASES = 'ai-integrated/registry/leases.json'
ADMISSION_RECEIPT = 'validation/r50-admission-2026-09-22.json'
SOURCE_RECEIPT = 'validation/r50-source-composition-2026-09-22.json'

def git(*args): return subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, check=True).stdout
def blob(ref, name): return git('show', ref + ':' + name)
def sha(raw): return hashlib.sha256(raw).hexdigest().upper()
def identity(raw): return {'bytes': len(raw), 'sha256': sha(raw)}
def require(ok, message):
    if not ok: raise ValueError(message)
def write(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
def now(): return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

def evidence():
    manifest_raw = blob(CANDIDATE_COMMIT, PREFIX + 'candidate.manifest.json')
    require(sha(manifest_raw) == MANIFEST, 'Wrong frozen candidate manifest')
    m = json.loads(manifest_raw)
    refs = m['source_authorities'] + m['builds'] + [m[k] for k in
        ('stable_unit_manifest', 'source_map', 'decision_ledger', 'rejection_ledger', 'formula_diagram_inventory')]
    for row in refs:
        name = row['path']
        require('..' not in Path(name).parts and not Path(name).is_absolute(), 'Unsafe candidate reference')
        raw = blob(CANDIDATE_COMMIT, PREFIX + name)
        require(identity(raw) == {'bytes': row['bytes'], 'sha256': row['sha256']}, 'Frozen reference drift: ' + name)
        require((ROOT / PREFIX / name).read_bytes() == raw, 'Working candidate drift: ' + name)
    require(m['review_state'] == 'performed' and m['independent_replay'] == 'passed' and not m['unresolved_defects'], 'Candidate gates missing')
    review = json.loads(blob(CANDIDATE_COMMIT, PREFIX + 'replay/FINAL_INDEPENDENT_REVIEW.json'))
    require(review['passed'] and all(c['passed'] for c in review['checks']), 'Independent replay failed')
    authority = blob(AUTHORITY, 'spaces-limits.tex')
    require(authority == blob(CANDIDATE_COMMIT, PREFIX + 'authority/source/spaces-limits.tex'), 'Authority mismatch')
    ops = json.loads(blob(CANDIDATE_COMMIT, PREFIX + 'operation-spec.json'))['operations']
    require(len(ops) == 2 and {o['stable_id'] for o in ops} == {'MC-STK-ERR-1574', 'MC-STK-ERR-1575'}, 'Wrong operation scope')
    post = replay(authority, ops)
    require(post == blob(CANDIDATE_COMMIT, PREFIX + 'payload/spaces-limits.tex'), 'Unlisted payload change')
    return m, refs, ops, authority, post

def replay(raw, ops):
    end = len(raw)
    for op in sorted(ops, key=lambda op: op['start_byte'], reverse=True):
        a, b = op['start_byte'], op['end_byte_exclusive']
        old, new = op['old_text'].encode(), op['replacement_text'].encode()
        require(op['source'] == 'spaces-limits.tex' and 0 <= a <= b <= end, 'Wrong source/overlap')
        require(raw[a:b] == old and sha(old) == op['old_sha256'] and sha(new) == op['replacement_sha256'], 'Preimage/hash drift')
        raw = raw[:a] + new + raw[b:]
        end = a
    return raw

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=['check', 'admit', 'compose'])
    args = p.parse_args()
    m, refs, ops, authority, post = evidence()
    current = git('rev-parse', 'HEAD').decode().strip()
    if args.action == 'check':
        print(json.dumps({'passed': True, 'references': len(refs), 'operations': 2, 'postimage': identity(post)}))
        return
    require(blob(PREVIOUS, 'spaces-limits.tex') == authority, 'Cumulative preimage changed from authority')
    require((ROOT / 'spaces-limits.tex').read_bytes() == authority, 'Dirty or already composed source')
    if args.action == 'admit':
        require(current == CANDIDATE_COMMIT, 'Candidate freeze is not current HEAD')
        raw = (ROOT / OVERLAYS).read_bytes()
        require(raw == blob(PREVIOUS, OVERLAYS), 'Registry changed since review')
        reg = json.loads(raw)
        ids = ['MC-STK-ERR-1574', 'MC-STK-ERR-1575']
        require(not set(ids).intersection(s for e in reg['registered_entries'] for s in e['stable_ids']), 'Duplicate IDs')
        entry = {'id': ID, 'namespace': m['namespace'], 'writer': m['writer_task'],
            'source_commit': AUTHORITY, 'source_tree': m['upstream']['tree'], 'manifest_sha256': MANIFEST,
            'stable_ids': ids, 'rights_state': m['rights_state'],
            'review_receipt': PREFIX.removeprefix('ai-integrated/') + 'replay/FINAL_INDEPENDENT_REVIEW.json',
            'admitted_at_utc': now()}
        reg['registered_entries'].append(entry)
        leases = json.loads((ROOT / LEASES).read_bytes())
        issued = leases['events'][-1]
        require(issued['event_id'] == 'lease-event-000106' and issued['lease_id'] == m['lease_id'] and issued['state'] == 'active', 'Lease is not active')
        event = {**issued, 'event_id': f"lease-event-{len(leases['events']) + 1:06d}",
            'event': 'released', 'state': 'released', 'issued_at_utc': now(), 'supersedes_event_id': issued['event_id']}
        leases['events'].append(event)
        from jsonschema import Draft202012Validator
        Draft202012Validator(json.loads((ROOT / 'ai-integrated/schemas/lease-registry.schema.json').read_bytes())).validate(leases)
        write(ROOT / OVERLAYS, reg)
        write(ROOT / LEASES, leases)
        write(ROOT / ADMISSION_RECEIPT, {'schema': 'stacks-r50-separate-admission/v1', 'passed': True,
            'candidate_commit': CANDIDATE_COMMIT, 'candidate_manifest_sha256': MANIFEST,
            'previous_public': PREVIOUS, 'admission': entry, 'release_event': event,
            'candidate_references_checked': len(refs), 'prior_registry_prefix_unchanged': True,
            'source_composed': False, 'reviewer': 'OpenAI Codex - GPT-6 Astra, Ultra effort'})
    else:
        reg = json.loads((ROOT / OVERLAYS).read_bytes())
        require(reg['registered_entries'][-1]['id'] == ID and reg['registered_entries'][-1]['manifest_sha256'] == MANIFEST, 'R50 not admitted')
        require((ROOT / OVERLAYS).read_bytes() == blob(current, OVERLAYS), 'Admission not committed')
        require(blob(current, 'spaces-limits.tex') == authority, 'Admission altered source')
        require((ROOT / ADMISSION_RECEIPT).is_file(), 'Admission receipt missing')
        actual = replay((ROOT / 'spaces-limits.tex').read_bytes(), ops)
        require(actual == post, 'Unexpected composition result')
        (ROOT / 'spaces-limits.tex').write_bytes(actual)
        write(ROOT / SOURCE_RECEIPT, {'schema': 'stacks-r50-separate-source-composition/v1',
            'status': 'PASS_SOURCE_REPLAY_BUILD_PENDING', 'previous_public': PREVIOUS,
            'candidate_commit': CANDIDATE_COMMIT, 'admission_commit': current,
            'manifest_sha256': MANIFEST, 'source': 'spaces-limits.tex', 'preimage': identity(authority),
            'postimage': identity(post), 'operations': ops, 'only_manifest_operations_applied': True,
            'whole_isolated_payload_copied': False, 'prior_additions_preserved': True,
            'model': 'OpenAI Codex - GPT-6 Astra, Ultra effort'})
    print(json.dumps({'action': args.action, 'passed': True, 'source_postimage': identity(post)}))

if __name__ == '__main__': main()
