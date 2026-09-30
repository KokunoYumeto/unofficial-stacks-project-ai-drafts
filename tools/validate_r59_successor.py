"""Validate the bounded R59 successor while preserving the published R58 tree."""
import argparse
import json
import subprocess
import sys
try:
    from . import r59_successor as r
except ImportError:
    import r59_successor as r

CURRENT = 'validation/r59-successor-current.json'
require = r.require


def append_only_registry(before, after, entry, before_leases, after_leases, issued, released):
    require(after == {**before,'registered_entries':before['registered_entries']+[entry]}, 'Registry prefix changed')
    old_ids = [i for row in before['registered_entries'] for i in row['stable_ids']]
    require(not set(old_ids).intersection(entry['stable_ids']), 'Reused stable ID')
    require(len(set(entry['stable_ids'])) == len(entry['stable_ids']), 'Duplicate new stable ID')
    require(issued['state'] == 'active' and released['state'] == 'released'
        and issued['lease_id'] == released['lease_id']
        and released['supersedes_event_id'] == issued['event_id'], 'Broken lease release')
    require(after_leases == {**before_leases,'events':before_leases['events']+[issued,released]}, 'Lease prefix changed')


def allowed_delta(rows, allowed):
    for row in rows:
        require(row['path'] in allowed, 'Unlisted changed path: '+row['path'])
        require(row['status'] in ('A','M'), 'Deletion or rename: '+row['path'])
        require(row['new_mode'] == '100644', 'Unexpected file mode: '+row['path'])


def delta(before, after):
    blocks = r.git('diff-tree','--no-commit-id','--no-renames','-r','--raw','-z',before,after).split(b'\0')
    require(blocks[-1] == b'' and len(blocks[:-1]) % 2 == 0, 'Malformed Git delta')
    rows = []
    for i in range(0,len(blocks)-1,2):
        old_mode,new_mode,old_oid,new_oid,status = blocks[i].decode().split()
        rows.append(dict(path=blocks[i+1].decode(),status=status,new_mode=new_mode,old_mode=old_mode.removeprefix(':')))
    return rows


def validate(ref='HEAD', check_exports=True):
    ref = r.git('rev-parse',ref).decode().strip()
    read = lambda name:r.blob(ref,name)
    doc = lambda name:json.loads(read(name))
    manifest, ids, sources, frozen = r.evidence()
    r.frozen_files(ref,frozen)
    current = doc(CURRENT)
    require(current['previous_public'] == r.PRIOR and current['candidate_commit'] == r.CANDIDATE
        and current['manifest_sha256'] == r.MANIFEST, 'Successor identity changed')
    admission = doc(r.ADMISSION); composition = doc(r.COMPOSITION)
    require(admission['passed'] and not admission['source_composed'] and admission['candidate_commit'] == r.CANDIDATE,
        'Admission binding changed')
    require(composition['passed'] and composition['candidate_commit'] == r.CANDIDATE
        and composition['manifest_sha256'] == r.MANIFEST and composition['sources'] == sources,
        'Composition binding changed')
    require(composition['admission_commit'] == current['admission_commit'], 'Composition admission changed')
    for name,commit in ((r.ADMISSION,current['admission_commit']),(r.COMPOSITION,current['composition_commit'])):
        require(read(name) == r.blob(commit,name), 'Immutable transition changed')
    require(current['admission_commit'] == 'c973bb9aa2d768e9a69884c3211a650133e1a3df'
        and current['composition_commit'] == 'f7b41cc57b117efe1b93229d968bbb641b7f469a', 'Transition commit changed')
    allowed_delta(delta(r.CANDIDATE,current['admission_commit']),
        {r.ADMISSION,r.OVERLAYS,r.LEASES,'tools/r59_successor.py'})
    allowed_delta(delta(current['admission_commit'],current['composition_commit']),
        {r.COMPOSITION,*[s['source'] for s in sources]})
    for source in sources:
        name = source['source']
        require(r.identity(read(name)) == source['postimage']
            and r.identity((r.ROOT/name).read_bytes()) == source['postimage'], 'Current chapter changed: '+name)
        require(r.identity(r.blob(current['admission_commit'],name)) == source['preimage'], 'Source composed during admission')
        require(r.identity(r.blob(current['composition_commit'],name)) == source['postimage'], 'Composition source changed')
    before = json.loads(r.blob(r.PRIOR,r.OVERLAYS))
    before_leases = json.loads(r.blob(r.PRIOR,r.LEASES))
    issued = json.loads(read(r.PREFIX+'LEASE.json'))
    append_only_registry(before,doc(r.OVERLAYS),admission['admission'],before_leases,doc(r.LEASES),issued,admission['release_event'])
    require(len(doc(r.OVERLAYS)['registered_entries']) == 62
        and len({i for e in doc(r.OVERLAYS)['registered_entries'] for i in e['stable_ids']}) == 2248,
        'Registry scope changed')
    require(admission['admission']['stable_ids'] == ids, 'Admitted IDs changed')
    exports = doc('upstream-corrections/manifest.json')
    require(exports['historical_registry_ids'] == 2206 and exports['included_effective_textual_units'] == 2204
        and len(exports['chapters']) == 36 and not exports['contains_new_theorem_additions'], 'Correction export scope changed')
    downloads = doc('upstream-corrections/downloads.json')
    exported = {'upstream-corrections/'+x['path'] for x in downloads['files']} | {'upstream-corrections/downloads.json'}
    for row in downloads['files']:
        require(r.identity(read('upstream-corrections/'+row['path'])) == {k:row[k] for k in ('bytes','sha256')}, 'Export identity changed')
    allowed = set(frozen) | exported | {r.OVERLAYS,r.LEASES,r.ADMISSION,r.COMPOSITION,CURRENT,
        'tools/r59_successor.py','tools/validate_r59_successor.py','tests/test_r59_successor.py','tests/test_changes_from_upstream.py',
        '.github/workflows/validate.yml','README.md','ai-integrated/README.md',
        'CHANGES_FROM_UPSTREAM.md','ai-integrated/changes/index.html','validation/changes-from-upstream-2026-08-30.json',
        *[s['source'] for s in sources]}
    changes = delta(r.PRIOR,ref)
    allowed_delta(changes,allowed)
    # Tree-object comparison skips unchanged subtrees. No workspace filesystem
    # scan or rerun of unchanged historical proof builds is required.
    old_workflow = r.blob(r.PRIOR,'.github/workflows/validate.yml').decode().replace('\r\n','\n')
    workflow = read('.github/workflows/validate.yml').decode().replace('\r\n','\n')
    dispatch = ('          if test -f tools/validate_r59_successor.py; then\n'
                '            python tools/validate_r59_successor.py\n'
                '            exit $?\n          fi\n')
    tests = '          python -m unittest tests.test_r59_successor\n'
    require(workflow.count(dispatch) == workflow.count(tests) == 1, 'Missing successor workflow checks')
    require(workflow.replace(dispatch,'').replace(tests,'') == old_workflow, 'Earlier workflow checks changed')
    r.git('merge-base','--is-ancestor',r.PRIOR,ref)
    require(not r.git('rev-list','--min-parents=2',r.PRIOR+'..'+ref).strip(), 'Unexpected merge in bounded successor')
    if check_exports:
        for script in ('generate_changes_from_upstream.py','export_upstream_corrections.py'):
            subprocess.run([sys.executable,'-B',str(r.ROOT/'tools'/script),'--check'],cwd=r.ROOT,check=True)
    return dict(status='R59_BOUNDED_SUCCESSOR_PASS',candidate_files=len(frozen),units=5,operations=13,
        overlays=62,stable_ids=2248,historical_correction_ids=2206,effective_export_units=2204,chapter_patches=36,
        changed_paths=len(changes),previous_public=r.PRIOR,
        prior_artifact_tree_preserved_outside_enumerated_scope=True,publication_readback_claimed=False,
        historical_validation='Published R58 checkpoint retained; unchanged historical mathematical review and builds are not rerun or claimed as new work.')


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ref',default='HEAD')
    args=parser.parse_args()
    print(json.dumps(validate(args.ref)))
