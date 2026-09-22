"""Verify the exact seven-edit R49 successor of the frozen public supplement tree.

The older supplement checker still rejects source changes. It is run at the
specified immutable parent; this layer permits and verifies only the admitted
R49 source/registry delta, generated comparison, downloads and named QA tooling.
"""
import argparse
import json
import re

try:
    from . import r49_successor as r
    from . import validate_standalone_supplements as prior
except ImportError:
    import r49_successor as r
    import validate_standalone_supplements as prior

CURRENT = 'validation/r49-successor-current.json'
BUILD = 'validation/r49-cumulative-build-2026-09-22.json'
VISUAL = 'validation/r49-visual-qa-2026-09-22.json'
TOOLS = {'tools/r49_successor.py', 'tools/build_r49_chapter.py', 'tools/validate_r49_successor.py',
         'tests/test_r49_successor.py', 'tools/validate_standalone_supplements.py',
         'tools/export_upstream_corrections.py', 'tests/test_upstream_correction_export.py',
         'tests/test_changes_from_upstream.py',
         'tests/test_r48_visual_loci.py',
         '.github/workflows/validate.yml'}


def validate(ref='HEAD', verify_frozen_core=False):
    parent_modules = prior.check_head(ref=r.PREVIOUS)
    r.git('merge-base', '--is-ancestor', r.PREVIOUS, ref)
    read = lambda path: r.blob(ref, prior.safe(path))
    doc = lambda path: json.loads(read(path))
    files, closure, ops, authority = r.evidence()
    for name, raw in files.items():
        r.require(read(name) == raw, 'Admitted immutable evidence changed: ' + name)
    for name in (r.OVERLAYS, r.LEASES):
        r.require(read(name) == r.blob(r.ADMISSION, name), 'Registry import changed')
    post, rebound = r.compose(r.blob(r.PREVIOUS, 'derham.tex'), authority, ops)
    r.require(read('derham.tex') == post, 'Cumulative R49 source replay differs')
    transport = doc(r.IMPORT_RECEIPT)
    r.require(transport['previous_public'] == r.PREVIOUS and transport['admission_commit'] == r.ADMISSION
              and transport['manifest_sha256'] == r.MANIFEST and not transport['source_composed']
              and not transport['new_admission_claimed'], 'Import receipt drift')
    r.require(transport['candidate_files'] == [{'path': p, **r.identity(b)} for p, b in sorted(files.items())]
              and transport['manifest_bound_references'] == closure, 'Imported closure differs')
    source = doc(r.SOURCE_RECEIPT)
    r.require(source['operations'] == rebound and source['postimage'] == r.identity(post)
              and source['preimage'] == r.identity(r.blob(r.PREVIOUS, 'derham.tex'))
              and source['prior_source_additions_preserved'] and not source['whole_isolated_payload_copied'],
              'Composition receipt drift')
    current, build, visual = doc(CURRENT), doc(BUILD), doc(VISUAL)
    r.require(current['status'] == 'READY_FOR_PUBLICATION' and current['previous_public'] == r.PREVIOUS
              and current['admission_commit'] == r.ADMISSION, 'Wrong successor current record')
    for name, item in ((BUILD, current['build']), (VISUAL, current['visual'])):
        prior.bound(read(name), item)
    r.require(current['import_commit'] == source['import_commit'], 'Separate import commit mismatch')
    for a, b in ((r.PREVIOUS, current['import_commit']), (current['import_commit'], current['composition_commit']),
                 (current['composition_commit'], ref)):
        r.git('merge-base', '--is-ancestor', a, b)
    r.require(r.blob(current['import_commit'], 'derham.tex') == r.blob(r.PREVIOUS, 'derham.tex'),
              'Import transition changed source')
    r.require(r.blob(current['composition_commit'], 'derham.tex') == post, 'Wrong source composition commit')
    r.require(build['source_commit'] == current['composition_commit'] and build['prior_public'] == r.PREVIOUS,
              'Build is not bound to current source')
    for item in build['input_files']:
        prior.bound(read(item['path']), item)
    before, first, second = build['builds']
    r.require(first['identities'] == second['identities'] and first['pdf'] == second['pdf'], 'Fresh build mismatch')
    r.require(first['source'] == second['source'] == r.identity(post), 'Built source mismatch')
    r.require(before['diagnostics'] == first['diagnostics'] == second['diagnostics'], 'New diagnostics')
    r.require(before['pages'] == first['pages'] == second['pages'] == visual['page_count'] == 70, 'Page-count drift')
    r.require(not first['diagnostics']['fatal_duplicate_glyph_rerun'], 'Build fatal diagnostics')
    r.require(build['mutex']['name'] == r'Global\InterlanguageTeXSlotV1'
              and 'acquired_utc' in build['mutex'] and 'released_utc' in build['mutex'], 'Missing build mutex evidence')
    r.require(visual['status'] == 'PASS_CHANGED_PAGE_REGRESSION' and visual['changed_pages_visual_review'] == 'PASS'
              and visual['successor_pdf_sha256'] == first['pdf']['sha256']
              and visual['prior_pdf_sha256'] == before['pdf']['sha256'], 'Wrong visual proof identity')
    r.require(visual['changed_pages'] == [6, 7, 9] and visual['unchanged_page_count'] == 67, 'Changed page scope')
    r.require([p['page'] for p in visual['pages']] == list(range(1, 71)), 'Incomplete page comparison')
    for page in visual['pages']:
        r.require((page['prior'] != page['successor']) == bool(page['changed_bbox'])
                  == (page['page'] in visual['changed_pages']), 'Raster comparison inconsistent')
    r.require({sid for item in visual['inspections'] for sid in item['stable_ids']}
              == {op['stable_id'] for op in ops}, 'Incomplete changed-locus inspection')
    downloads = doc('upstream-corrections/downloads.json')
    export = {'upstream-corrections/downloads.json'}
    for item in downloads['files']:
        name = prior.safe(item['path'])
        r.require(name in {'README.md', 'REVIEW.md', 'COPYING', 'manifest.json', 'ALL-TEXTUAL-CORRECTIONS.patch', 'corrections-only.zip'}
                  or re.fullmatch(r'(chapters/[a-z0-9-]+\.patch|reviews/[a-z0-9-]+\.md)', name), 'Unexpected export path')
        name = 'upstream-corrections/' + name
        r.require(name not in export, 'Duplicate export')
        prior.bound(read(name), item)
        export.add(name)
    manifest = doc('upstream-corrections/manifest.json')
    r.require(manifest['historical_registry_ids'] == 1309 and manifest['included_effective_textual_units'] == 1307
              and len(manifest['chapters']) == 31, 'Correction export coverage changed')
    allowed = set(files) | export | TOOLS | {r.OVERLAYS, r.LEASES, r.IMPORT_RECEIPT, r.SOURCE_RECEIPT,
        CURRENT, BUILD, VISUAL, 'derham.tex', 'README.md', 'CHANGES_FROM_UPSTREAM.md',
        'ai-integrated/changes/index.html', 'validation/changes-from-upstream-2026-08-30.json'}
    changes = [line.split('\t', 1) for line in r.git('diff-tree', '-r', '--no-commit-id', '--name-status', r.PREVIOUS, ref).decode().splitlines()]
    prior.check_changes(changes, allowed)
    for _, name in changes:
        r.require(r.git('ls-tree', ref, '--', name).decode().split()[0] == '100644', 'Unexpected file mode')
    if verify_frozen_core:
        prior.verify_frozen_core()
    return {'status': 'R49_CUMULATIVE_SUCCESSOR_PASS', 'source_operations': 7, 'units': 5,
            'effective_export_units': 1307, 'chapter_patches': 31, 'parent_modules': parent_modules,
            'frozen_core_revalidated': verify_frozen_core, 'changed_paths': len(changes)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-frozen-core', action='store_true')
    args = parser.parse_args()
    print(json.dumps(validate(verify_frozen_core=args.verify_frozen_core)))
