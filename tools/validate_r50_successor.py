"""Verify the exact R50 delta while retaining R49 and every older frozen-core gate."""
import argparse
import json
import os
import re
import textwrap
try:
    from . import r50_successor as r
    from . import validate_r49_successor as prior
except ImportError:
    import r50_successor as r
    import validate_r49_successor as prior

CURRENT = 'validation/r50-successor-current.json'
BUILD = 'validation/r50-cumulative-build-2026-09-22.json'
VISUAL = 'validation/r50-visual-qa-2026-09-22.json'
STATUS = 'ai-integrated/review-notes/proposal-integration-status.json'
TOOLS = {'tools/r50_successor.py', 'tools/build_errata_chapter.py', 'tools/validate_r50_successor.py',
    'tests/test_r50_successor.py', 'tests/test_changes_from_upstream.py',
    'tools/export_upstream_corrections.py', 'tools/generate_possible_fix_patches.py',
    '.github/workflows/validate.yml', 'ai-integrated/.github/workflows/validate.yml'}

def validate(ref='HEAD', verify_frozen_core=False):
    earlier = prior.validate(ref=r.PREVIOUS, verify_frozen_core=verify_frozen_core)
    read = lambda name: r.blob(ref, prior.prior.safe(name))
    doc = lambda name: json.loads(read(name))
    manifest, refs, ops, authority, post = r.evidence()
    names = {r.PREFIX + item['path'] for item in refs} | {r.PREFIX + 'candidate.manifest.json'}
    listed = set(r.git('ls-tree', '-r', '--name-only', r.CANDIDATE_COMMIT, '--', r.PREFIX).decode().splitlines())
    r.require(names == listed, 'Frozen candidate closure incomplete')
    for name in names:
        r.require(read(name) == r.blob(r.CANDIDATE_COMMIT, name), 'Frozen candidate changed: ' + name)
    before, after = json.loads(r.blob(r.PREVIOUS, r.OVERLAYS)), doc(r.OVERLAYS)
    prior.r.append_check(before, after, 'registered_entries', 1)
    entry = after['registered_entries'][-1]
    r.require(entry['id'] == r.ID and entry['manifest_sha256'] == r.MANIFEST
        and entry['stable_ids'] == ['MC-STK-ERR-1574', 'MC-STK-ERR-1575'], 'Wrong admitted scope')
    old_leases, leases = json.loads(r.blob(r.PREVIOUS, r.LEASES)), doc(r.LEASES)
    prior.r.append_check(old_leases, leases, 'events', 4)
    a, b, c, d = leases['events'][-4:]
    r.require([e['event_id'] for e in (a,b,c,d)] == [f'lease-event-{i:06d}' for i in range(104,108)], 'Wrong lease event sequence')
    r.require(a['state'] == c['state'] == 'active' and b['state'] == 'superseded'
        and d['state'] == 'released' and d['supersedes_event_id'] == c['event_id'], 'Invalid custody/release transitions')
    r.require(c['lease_id'] == manifest['lease_id'] == d['lease_id'] and c['writer_task'] == manifest['writer_task'], 'Wrong writer lease')
    source, current = doc(r.SOURCE_RECEIPT), doc(CURRENT)
    r.require(current['status'] == 'READY_FOR_PUBLICATION' and current['previous_public'] == r.PREVIOUS
        and current['candidate_commit'] == r.CANDIDATE_COMMIT and current['candidate_manifest_sha256'] == r.MANIFEST, 'Wrong successor binding')
    chain = [r.PREVIOUS, current['custody_commit'], r.CANDIDATE_COMMIT,
             current['admission_commit'], current['composition_commit'], ref]
    for a, b in zip(chain, chain[1:]): r.git('merge-base', '--is-ancestor', a, b)
    for commit in chain[1:4]:
        r.require(r.blob(commit, 'spaces-limits.tex') == authority, 'Source changed before composition')
    r.require(read('spaces-limits.tex') == post == r.blob(current['composition_commit'], 'spaces-limits.tex'), 'Cumulative replay mismatch')
    r.require(source['operations'] == ops and source['preimage'] == r.identity(authority)
        and source['postimage'] == r.identity(post) and source['admission_commit'] == current['admission_commit']
        and source['only_manifest_operations_applied'] and not source['whole_isolated_payload_copied'], 'Invalid composition receipt')
    for path in (r.OVERLAYS, r.LEASES, r.ADMISSION_RECEIPT):
        r.require(read(path) == r.blob(current['admission_commit'], path), 'Admission changed after frozen transition')
    admission = doc(r.ADMISSION_RECEIPT)
    r.require(admission['admission'] == entry and admission['release_event'] == d and admission['passed']
        and not admission['source_composed'] and admission['candidate_commit'] == r.CANDIDATE_COMMIT, 'Admission receipt mismatch')
    for name, row in ((BUILD, current['build']), (VISUAL, current['visual'])):
        prior.prior.bound(read(name), row)
    build, visual = doc(BUILD), doc(VISUAL)
    r.require(build['prior_public'] == r.PREVIOUS and build['source_commit'] == current['composition_commit'], 'Wrong build lineage')
    for item in build['input_files']: prior.prior.bound(read(item['path']), item)
    old, first, second = build['builds']
    r.require(old['source'] == r.identity(authority) and first['source'] == second['source'] == r.identity(post), 'Wrong built source')
    r.require(first['identities'] == second['identities'] and first['pdf'] == second['pdf'], 'Fresh builds differ')
    r.require(old['diagnostics'] == first['diagnostics'] == second['diagnostics'] and not first['diagnostics']['fatal_duplicate_glyph_rerun'], 'Build regression')
    r.require(old['pages'] == first['pages'] == second['pages'] == visual['page_count'] == 57, 'Page scope drift')
    r.require(build['mutex']['name'] == r'Global\InterlanguageTeXSlotV1'
        and 'acquired_utc' in build['mutex'] and 'released_utc' in build['mutex'], 'Missing complete mutex lifetime')
    r.require(visual['status'] == 'PASS_CHANGED_PAGE_REGRESSION' and visual['changed_pages_visual_review'] == 'PASS'
        and visual['prior_pdf'] == old['pdf'] and visual['successor_pdf'] == first['pdf'], 'Visual identity mismatch')
    r.require(visual['changed_pages'] == [3,4] and visual['unchanged_page_count'] == 55, 'Unexpected visual change scope')
    r.require([row['page'] for row in visual['pages']] == list(range(1,58)), 'Incomplete raster comparison')
    for row in visual['pages']:
        r.require((row['prior'] != row['successor']) == bool(row['changed_bbox']) == (row['page'] in [3,4]), 'Visual comparison inconsistent')
    r.require({row['stable_id'] for row in visual['inspections']} == set(entry['stable_ids']), 'Uninspected correction')
    export = {'upstream-corrections/downloads.json'}
    for item in doc('upstream-corrections/downloads.json')['files']:
        name = prior.prior.safe(item['path'])
        r.require(name in {'README.md','REVIEW.md','COPYING','manifest.json','ALL-TEXTUAL-CORRECTIONS.patch','corrections-only.zip'}
            or re.fullmatch(r'(chapters/[a-z0-9-]+\.patch|reviews/[a-z0-9-]+\.md)', name), 'Unexpected export member')
        name = 'upstream-corrections/' + name
        r.require(name not in export, 'Duplicate export member')
        prior.prior.bound(read(name), item)
        export.add(name)
    exported = doc('upstream-corrections/manifest.json')
    r.require(exported['historical_registry_ids'] == 1311 and exported['included_effective_textual_units'] == 1309
        and len(exported['chapters']) == 32 and not exported['contains_new_theorem_additions'], 'Export scope wrong')
    status = doc(STATUS)
    r.require(status['pending_units'] == 11 and {row['stable_id'] for row in status['composed']} == set(entry['stable_ids'])
        and all(row['source_commit'] == current['composition_commit'] for row in status['composed']), 'Readable selection status wrong')
    allowed = names | export | TOOLS | {r.OVERLAYS, r.LEASES, r.ADMISSION_RECEIPT, r.SOURCE_RECEIPT,
        CURRENT, BUILD, VISUAL, STATUS, 'validation/r50-custody-transfer-2026-09-22.json',
        'spaces-limits.tex', 'README.md', 'PROPOSED_CORRECTIONS.md', 'ai-integrated/README.md',
        'CHANGES_FROM_UPSTREAM.md', 'ai-integrated/changes/index.html',
        'validation/changes-from-upstream-2026-08-30.json', 'possible-fixes/README.md', 'possible-fixes/manifest.json'}
    changes = [line.split('\t',1) for line in r.git('diff-tree','-r','--no-commit-id','--name-status',r.PREVIOUS,ref).decode().splitlines()]
    prior.prior.check_changes(changes, allowed)
    for _, name in changes:
        r.require(r.git('ls-tree',ref,'--',name).decode().split()[0] == '100644', 'Unexpected file mode')
    # Execute the complete current registry contract, not only the new entry.
    workflow = read('ai-integrated/.github/workflows/validate.yml').decode()
    code = textwrap.dedent(workflow.split("python - <<'PY'\n",1)[1].rsplit('\n          PY',1)[0])
    old_cwd = os.getcwd()
    try:
        os.chdir(r.ROOT / 'ai-integrated')
        exec(compile(code, 'current-registry-contract', 'exec'), {'__name__':'__main__'})
    finally: os.chdir(old_cwd)
    return {'status':'R50_CUMULATIVE_SUCCESSOR_PASS', 'operations':2, 'units':2,
        'effective_export_units':1309, 'chapter_patches':32, 'changed_paths':len(changes),
        'previous_r49':earlier, 'frozen_core_revalidated':verify_frozen_core}

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--verify-frozen-core', action='store_true')
    args = p.parse_args()
    print(json.dumps(validate(verify_frozen_core=args.verify_frozen_core)))
