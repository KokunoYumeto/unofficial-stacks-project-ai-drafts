"""Extend direct-successor packaging: reader first, FULL native source second.

No publication is performed. Requires a committed final build receipt and
committed independently recomputable source inventory. Installation happens
before the final source commit; the inventory is committed afterwards.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import package_direct_successor_pdfs as legacy
from cumulative_source import (GitObjects, METADATA, MASTER, SCHEMA, canonical_json, parse_json,
                               expected_source_members, identity, require, safe_path,
                               validate_inventory_shape, validate_master, write_source_zip)
from cumulative_reader import merge_chapters, PDF_NAME

SOURCE_NAME = '02-full-cumulative-editable-source.zip'

def ordered_assets(reader_asset, source_asset, supplemental):
    require(reader_asset.get('name') == PDF_NAME and reader_asset.get('role') == 'cumulative_reader',
            'first asset must be cumulative reader')
    require(source_asset.get('name') == SOURCE_NAME and source_asset.get('role') == 'full_cumulative_editable_source',
            'second asset must be full native source')
    result = [reader_asset,source_asset,*supplemental]
    require(len({row['name'].casefold() for row in result}) == len(result), 'duplicate asset name')
    return result

def package(repository_root, build_root, build_receipt, output_dir, content_commit,
            public_receipt_path, public_source_inventory_path, source_inventory_commit):
    objects = GitObjects(repository_root)
    objects.commit(content_commit)
    objects.commit(source_inventory_commit)
    safe_path(public_source_inventory_path)
    require(public_source_inventory_path.startswith('validation/') and public_source_inventory_path.endswith('.json'),
            'public source inventory must be an explicit validation JSON')
    objects.raw('merge-base','--is-ancestor',source_inventory_commit,content_commit)
    inventory_raw = objects.blob(content_commit,public_source_inventory_path)
    require(inventory_raw == objects.blob(source_inventory_commit,public_source_inventory_path), 'source inventory changed before content head')
    source_inventory = parse_json(inventory_raw)
    validate_inventory_shape(source_inventory)
    raw = Path(build_receipt).read_bytes()
    receipt, binding, artifacts = legacy.build_inputs(raw,public_receipt_path)
    require(source_inventory['source_commit'] == receipt['source']['commit'], 'native source does not match fresh build source')
    require(source_inventory['authority_commit'] == legacy.AUTHORITY, 'wrong preserved printed authority')
    require(source_inventory['chapter_stems'] == list(legacy.R48_STEMS), 'source inventory scope is not release profile')
    expected = expected_source_members(repository_root,source_inventory['source_commit'],
                                       source_inventory['authority_commit'],source_inventory['chapter_stems'])
    require(source_inventory['members'] == [expected[p] for p in sorted(expected)], 'committed source inventory is incomplete')
    for row in expected.values():
        if row['archive_path'].startswith('current/'):
            require(objects.blob(content_commit,row['git_path']) == objects.blob(row['git_commit'],row['git_path']),
                    'current native source changed since final build: '+row['git_path'])
    require(source_inventory['master_path'] == MASTER, 'unexpected cumulative master path')
    master = validate_master(parse_json(objects.blob(source_inventory['source_commit'],'tools/cumulative-master.json')),
                             source_inventory['chapter_stems'])
    result = legacy.package(repository_root,build_root,build_receipt,output_dir,content_commit,public_receipt_path)
    output = Path(output_dir)
    cumulative = merge_chapters(build_root,master,artifacts,output/PDF_NAME)
    write_source_zip(repository_root,inventory_raw,output/SOURCE_NAME)
    reader_asset = {'name':PDF_NAME,'role':'cumulative_reader',**identity((output/PDF_NAME).read_bytes()),
                    'cumulative_reader':cumulative}
    source_ref = {'path':public_source_inventory_path,'commit':source_inventory_commit,**identity(inventory_raw),
                  'git_blob':objects.raw('rev-parse',content_commit+':'+public_source_inventory_path).decode().strip()}
    source_asset = {'name':SOURCE_NAME,'role':'full_cumulative_editable_source',
                    **identity((output/SOURCE_NAME).read_bytes()),
                    'source_archive':{'source_inventory':source_ref,'metadata_member':METADATA}}
    readme = ('# Unofficial Stacks Project AI Drafts\n\n'
        'This is a readable, editable draft collection for later study and reuse. '
        'It is not an official Stacks Project release or endorsement.\n\n'
        '## Read and edit\n\n'
        f'1. [Cumulative 36-chapter reader]({PDF_NAME})\n'
        f'2. [Full cumulative editable source]({SOURCE_NAME})\n\n'
        'The reader contains the 36 chapters in this release, not the entire Stacks Project. '
        'Its chapter bookmarks and included-chapter links stay inside the cumulative reader. '
        'References to chapters outside this release remain external; inherited unresolved '
        'references are not silently supplied or claimed resolved.\n\n'
        'The source archive preserves the complete native LaTeX bodies, shared styles, '
        'bibliography, figures and build support. `current/` is the exact build source; '
        '`baseline/` is the unmodified pinned upstream source, kept separately for comparison. '
        'The executable assembly master is `current/tools/cumulative-master.json`; '
        'native reconstruction instructions are in `current/tools/CUMULATIVE-RECONSTRUCTION.md`.\n\n'
        'Individual chapter PDFs, the supplemental PDF collection, and evidence files follow '
        'these two primary downloads. Package integrity is not a claim of proof-assistant '
        'verification or of comprehensive mathematical review.\n')
    (output/'README.md').write_bytes(readme.encode())
    supplemental = result['upload_assets']
    for asset in supplemental:
        asset.update(identity((output/asset['name']).read_bytes()))
        asset['role'] = 'chapter_pdf' if asset.get('pdf_stem') else 'pdf_bundle' if asset.get('pdf_members') else 'supplement'
    result['upload_assets'] = ordered_assets(reader_asset,source_asset,supplemental)
    result['upload_asset_count'] = len(result['upload_assets'])
    result['upload_total_bytes'] = sum(row['bytes'] for row in result['upload_assets'])
    result['primary_asset_order'] = [PDF_NAME,SOURCE_NAME]
    result['cumulative_reader_visual_qa_performed'] = False
    result['native_source_closure_checked'] = True
    # This replaces only this invocation's unpublished transfer inventory.
    (output/legacy.INVENTORY_NAME).write_bytes(canonical_json(result))
    require(json.loads((output/legacy.INVENTORY_NAME).read_bytes()) == result, 'package inventory readback differs')
    return result

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository-root',required=True,type=Path)
    parser.add_argument('--build-root',required=True,type=Path)
    parser.add_argument('--build-receipt',required=True,type=Path)
    parser.add_argument('--output-dir',required=True,type=Path)
    parser.add_argument('--content-commit',required=True)
    parser.add_argument('--public-build-receipt-path',required=True)
    parser.add_argument('--public-source-inventory-path',required=True)
    parser.add_argument('--source-inventory-commit',required=True)
    args=parser.parse_args()
    result=package(args.repository_root,args.build_root,args.build_receipt,args.output_dir,args.content_commit,
                   args.public_build_receipt_path,args.public_source_inventory_path,args.source_inventory_commit)
    print(json.dumps({'status':result['status'],'assets':result['upload_asset_count'],
                      'primary_asset_order':result['primary_asset_order']}))
