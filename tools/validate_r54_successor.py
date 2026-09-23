"""Validate R54 and all unchanged earlier release gates at their exact checkpoints."""
import argparse
import json
import os
import re
import textwrap
try:
    from . import r54_successor as r
    from . import validate_r53_successor as prior
except ImportError:
    import r54_successor as r
    import validate_r53_successor as prior

CURRENT = 'validation/r54-successor-current.json'

def append_check(before, after, key, count):
    r.require(set(before) == set(after), 'Registry key drift')
    r.require(len(after[key]) == len(before[key])+count and after[key][:len(before[key])] == before[key], 'Non-append registry change')
    r.require(all(before[k] == after[k] for k in before if k != key), 'Other registry field changed')

def validate(ref='HEAD', verify_frozen_core=False):
    earlier = prior.validate(ref=r.PRIOR, verify_frozen_core=verify_frozen_core)
    m, refs, ids, sources, names = r.evidence()
    read = lambda n: r.blob(ref, n)
    doc = lambda n: json.loads(read(n))
    for name in names: r.require(read(name) == r.blob(r.CANDIDATE, name), 'Frozen candidate changed: '+name)
    before = json.loads(r.blob(r.PRIOR, r.OVERLAYS)); after = doc(r.OVERLAYS)
    append_check(before, after, 'registered_entries', 1)
    entry = after['registered_entries'][-1]
    r.require(entry['id'] == r.ID and entry['manifest_sha256'] == r.MANIFEST and entry['stable_ids'] == ids, 'Admission drift')
    oldleases = json.loads(r.blob(r.PRIOR, r.LEASES)); leases = doc(r.LEASES)
    append_check(oldleases, leases, 'events', 2)
    issued, released = leases['events'][-2:]
    r.require(issued['event_id'] == 'lease-event-000116' and issued['state'] == 'active' and released['event_id'] == 'lease-event-000117'
        and released['state'] == 'released' and released['supersedes_event_id'] == issued['event_id'], 'Lease transition drift')
    r.require(issued['lease_id'] == released['lease_id'] == m['lease_id'], 'Lease identity drift')
    current = doc(CURRENT); composition = doc(r.COMPOSITION); admission = doc(r.ADMISSION)
    r.require(current['status'] == 'READY_FOR_PUBLICATION' and current['previous_public'] == r.PRIOR
        and current['candidate_commit'] == r.CANDIDATE and current['manifest_sha256'] == r.MANIFEST, 'Successor binding drift')
    chain = [r.PRIOR, current['lease_commit'], r.CANDIDATE, current['admission_commit'], current['composition_commit'], ref]
    for left, right in zip(chain, chain[1:]): r.git('merge-base', '--is-ancestor', left, right)
    for s in sources:
        for commit in chain[1:4]: r.require(r.identity(r.blob(commit, s['source'])) == s['preimage'], 'Premature composition')
        raw = read(s['source'])
        r.require(r.identity(raw) == s['postimage'] and raw == r.blob(current['composition_commit'], s['source']), 'Cumulative source drift')
    r.require(composition['sources'] == sources and composition['admission_commit'] == current['admission_commit']
        and composition['only_admitted_operations_applied'] and not composition['whole_isolated_payload_copied'], 'Composition receipt drift')
    r.require(admission['passed'] and not admission['source_composed'] and admission['admission'] == entry
        and admission['release_event'] == released and admission['candidate_commit'] == r.CANDIDATE, 'Admission receipt drift')
    for name in (r.OVERLAYS, r.LEASES, r.ADMISSION): r.require(read(name) == r.blob(current['admission_commit'], name), 'Admission history changed')
    export = {'upstream-corrections/downloads.json'}
    for item in doc('upstream-corrections/downloads.json')['files']:
        name = item['path']
        r.require(name in {'README.md','REVIEW.md','COPYING','manifest.json','ALL-TEXTUAL-CORRECTIONS.patch','corrections-only.zip'}
            or re.fullmatch(r'(chapters/[a-z0-9-]+\.patch|reviews/[a-z0-9-]+\.md)', name), 'Unsafe export path')
        path = 'upstream-corrections/'+name; r.require(path not in export, 'Duplicate export'); export.add(path)
        r.require(r.identity(read(path)) == {'bytes':item['bytes'],'sha256':item['sha256']}, 'Export byte drift')
    exp = doc('upstream-corrections/manifest.json')
    r.require(exp['historical_registry_ids'] == 1489 and exp['included_effective_textual_units'] == 1487
        and len(exp['chapters']) == 34 and not exp['contains_new_theorem_additions'], 'Export scope drift')
    allowed = names | export | {r.OVERLAYS,r.LEASES,r.ADMISSION,r.COMPOSITION,CURRENT,
        'sheaves.tex','README.md','ai-integrated/README.md','tools/r54_successor.py',
        'tools/validate_r54_successor.py','tools/generate_changes_from_upstream.py',
        'tests/test_r54_successor.py','tests/test_changes_from_upstream.py','.github/workflows/validate.yml',
        'CHANGES_FROM_UPSTREAM.md','ai-integrated/changes/index.html','validation/changes-from-upstream-2026-08-30.json'}
    changes = [line.split('\t',1) for line in r.git('diff-tree','-r','--no-commit-id','--name-status',r.PRIOR,ref).decode().splitlines()]
    for status,name in changes:
        r.require(status in {'A','M'} and name in allowed, 'Unapproved change: '+status+' '+name)
        r.require(r.git('ls-tree',ref,'--',name).decode().split()[0] == '100644', 'Unexpected file mode')
    workflow = read('ai-integrated/.github/workflows/validate.yml').decode()
    code = textwrap.dedent(workflow.split("python - <<'PY'\n",1)[1].rsplit('\n          PY',1)[0]); cwd = os.getcwd()
    try:
        os.chdir(r.ROOT/'ai-integrated'); exec(compile(code,'r54-full-registry-contract','exec'),{'__name__':'__main__'})
    finally: os.chdir(cwd)
    return {'status':'R54_CUMULATIVE_SUCCESSOR_PASS','units':12,'operations':16,'effective_export_units':1487,
        'chapter_patches':34,'changed_paths':len(changes),'frozen_core_revalidated':verify_frozen_core,'prior':earlier}

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--verify-frozen-core', action='store_true'); a=p.parse_args()
    print(json.dumps(validate(verify_frozen_core=a.verify_frozen_core)))
