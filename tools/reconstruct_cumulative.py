"""Reconstruct from a verified extracted source ZIP, without a Git checkout.

Builds in an exclusively new copy, preserves current/ and baseline/, and uses
the original bounded process runner and machine-wide Windows TeX mutex.
This is reconstruction, not the release's independent validation certificate.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import shutil
from cumulative_source import (MASTER, assert_no_reparse, canonical_json, identity, parse_json,
                               require, safe_path, validate_inventory_shape, validate_master,
                               verified_member_bytes, verify_extracted)
from cumulative_reader import merge_chapters
from build_fixed_point import (WindowsNamedMutex, TEX_MUTEX_NAME, TEX_MUTEX_TIMEOUT_MS,
                               run, build_state_vector, scan_tex_diagnostics)
from pypdf import PdfReader

def disjoint_reconstruction_paths(extracted_root, output):
    extracted_root = assert_no_reparse(extracted_root).resolve(strict=True)
    output = assert_no_reparse(output,missing_ok=True).resolve(strict=False)
    require(output != extracted_root and not output.is_relative_to(extracted_root)
            and not extracted_root.is_relative_to(output), 'reconstruction output and preserved source must be disjoint')
    require(not os.path.lexists(output), 'reconstruction output must be new')
    return extracted_root, output

def copy_verified_current(extracted_root, output, inventory):
    validate_inventory_shape(inventory)
    extracted_root, output = disjoint_reconstruction_paths(extracted_root,output)
    output.mkdir(parents=False,exist_ok=False)
    for row in inventory['members']:
        if not row['archive_path'].startswith('current/'):
            continue
        # Only the allowlisted, rechecked bytes are copied, never directory extras.
        raw = verified_member_bytes(extracted_root,row)
        relative = safe_path(row['archive_path'][len('current/'):])
        destination = output/relative
        assert_no_reparse(destination.parent,missing_ok=True)
        destination.parent.mkdir(parents=True,exist_ok=True)
        require(assert_no_reparse(destination.parent).resolve(strict=True).is_relative_to(output),
                'destination parent escapes reconstruction root')
        with destination.open('xb') as stream:
            stream.write(raw)
        verified_member_bytes(output,row,strip_current=True)
    return output

def archived_reference_labels(source, inventory):
    validate_inventory_shape(inventory)
    labels = {'index-section-phantom':'shared-index'}
    pattern = re.compile(r'\\label\{([^}]+)\}')
    for row in inventory['members']:
        name = row['archive_path']
        if not (name.startswith('current/') and name.count('/')==1 and name.endswith('.tex')):
            continue
        stem = Path(name[len('current/'):]).stem
        raw = verified_member_bytes(source,row,strip_current=True)
        for label in pattern.findall(raw.decode('utf-8')):
            key = stem+'-'+label
            require(labels.get(key) in (None,stem), 'ambiguous external-reference provider: '+key)
            labels[key] = stem
    return labels

def prepare_reconstruction(extracted_root, output):
    """Exercise all archive validation/copy/label preparation without TeX or Git."""
    extracted_root, output = disjoint_reconstruction_paths(extracted_root,output)
    inventory = verify_extracted(extracted_root)
    members = validate_inventory_shape(inventory)
    master = validate_master(parse_json(verified_member_bytes(extracted_root,members[MASTER])),inventory['chapter_stems'])
    copy_verified_current(extracted_root,output,inventory)
    labels = archived_reference_labels(output,inventory)
    return output,inventory,master,labels

def reconstruct(extracted_root, output, source_date_epoch, max_sweeps=12):
    require(os.name == 'nt', 'This archived runner requires Windows named-mutex semantics; no TeX was started')
    require(str(source_date_epoch).isdigit(), 'SOURCE_DATE_EPOCH must be explicit numeric build-receipt value')
    require(2 <= max_sweeps <= 30, 'bounded sweep limit must be 2..30')
    for command in ('pdflatex','bibtex'):
        require(shutil.which(command), 'missing runtime tool: '+command)
    output,inventory,master,labels = prepare_reconstruction(extracted_root,output)
    stems = inventory['chapter_stems']
    env = os.environ.copy()
    env.update({'SOURCE_DATE_EPOCH':str(source_date_epoch),'FORCE_SOURCE_DATE':'1','TZ':'UTC'})
    mutex = WindowsNamedMutex(TEX_MUTEX_NAME, TEX_MUTEX_TIMEOUT_MS)
    fixed_sweep, diagnostics = None, {}
    with mutex:
        latex = ['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error']
        for stem in stems:
            run([*latex,stem+'.tex'],output,env,mutex)
        for stem in stems:
            run(['bibtex',stem],output,env,mutex)
        previous = None
        for sweep in range(1,max_sweeps+1):
            for stem in stems:
                run([*latex,stem+'.tex'],output,env,mutex)
            current = build_state_vector(output,stems)
            if current == previous:
                fixed_sweep = sweep
                break
            previous = current
        require(fixed_sweep is not None, 'native reconstruction did not reach a fixed point')
        for stem in stems:
            counts, external = scan_tex_diagnostics(output/(stem+'.log'), output/(stem+'.blg'), stem, labels)
            require(not {k:v for k,v in counts.items() if k != 'external_reference_markers' and v},
                    'native reconstruction diagnostics failed: '+stem)
            diagnostics[stem] = {'counts':counts,'external_references':external}
    artifacts = []
    for stem in stems:
        path = output/(stem+'.pdf')
        artifacts.append({'stem':stem,'pages':len(PdfReader(path,strict=True).pages),**identity(path.read_bytes())})
    cumulative = merge_chapters(output,master,artifacts,output/'01-cumulative-reader.pdf')
    receipt = {'schema':'cumulative-native-reconstruction/v1','status':'PASS_MECHANICAL_RECONSTRUCTION',
               'source_commit':inventory['source_commit'],'source_date_epoch':str(source_date_epoch),
               'fixed_point_sweep':fixed_sweep,'machine_wide_tex_mutex':mutex.receipt_details(),
               'artifacts':artifacts,'cumulative_reader':cumulative,'diagnostics':diagnostics,
               'release_validation_or_visual_qa_claimed':False}
    with (output/'cumulative-reconstruction-receipt.json').open('xb') as stream:
        stream.write(canonical_json(receipt))
    return receipt

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--extracted-root',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--source-date-epoch',required=True)
    parser.add_argument('--max-sweeps',type=int,default=12)
    args=parser.parse_args()
    result=reconstruct(args.extracted_root,args.output,args.source_date_epoch,args.max_sweeps)
    print(json.dumps({'status':result['status'],'chapters':len(result['artifacts'])}))
