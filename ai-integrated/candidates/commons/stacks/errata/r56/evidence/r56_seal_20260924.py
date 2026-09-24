"""Collect completed R56 proof evidence and seal the candidate; no registry admission."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import zipfile

CONTROL=Path(__file__).resolve().parent
BUILD_DIRS={'stacks':'r56-build-stacks-20260924'}
def ident(raw):return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest().upper()}
def write(p,v):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(v if isinstance(v,bytes) else (v if isinstance(v,str) else json.dumps(v,indent=2,ensure_ascii=False)+'\n').encode())

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--package-only',action='store_true');a=p.parse_args()
    root=a.repo.resolve(); c=root/'ai-integrated/candidates/commons/stacks/errata/r56'
    assert not (c/'candidate.manifest.json').exists(),'Never rewrite a sealed manifest'
    from verify_stacks_intake_review_20260924 import verify_proof_evidence
    retained_review=json.loads((c/'evidence/STACKS_INTAKE_REVIEW_20260923.json').read_bytes())
    verify_proof_evidence(retained_review,c/'evidence')
    pdfs={'prior':{},'successor':{}}; builds=[]; visuals=[]
    for chapter in ('stacks',):
        work=CONTROL/BUILD_DIRS[chapter]
        build=json.loads((work/'BUILD_RECEIPT.json').read_bytes())
        assert build['builds'][1]['identities']==build['builds'][2]['identities']
        before,after=build['builds'][0]['diagnostics'],build['builds'][1]['diagnostics']
        assert after==build['builds'][2]['diagnostics']
        for key in before:
            assert after[key]<=before[key] if key=='underfull_boxes' else after[key]==before[key], key
        assert not build['builds'][1]['diagnostics']['fatal_duplicate_glyph_rerun']
        for role,folder,index in [('prior','prior',0),('successor','a',1)]:
            raw=(work/folder/(chapter+'.pdf')).read_bytes()
            assert ident(raw)==build['builds'][index]['pdf']
            write(c/f'proofs/{chapter}-{role}.pdf',raw)
            pdfs[role][chapter]=ident(raw)
            for name in (chapter+'.tex','preamble.tex','stacks-project.cls','chapters.tex','my.bib'):
                assert (c/'proof-source'/role/name).read_bytes()==(work/folder/name).read_bytes()
        write(c/f'builds/{chapter}.json',build);builds.append(build)
    for name in ('tex_slot.py','tex_process_guard.py'):
        write(c/'proof-source'/name,(root/'ai-integrated/candidates/commons/stacks/errata/r50/proof-source'/name).read_bytes())
    reproduction_script=(root/'ai-integrated/candidates/commons/stacks/errata/r51/proof-source/reproduce.py').read_text(encoding='utf-8').replace('R51','R56').replace("choices=['sets','schemes','homology','algebra']", "choices=['stacks']")
    write(c/'proof-source/reproduce.py',reproduction_script)
    source=c/'proof-source'
    files=[{'path':p.relative_to(source).as_posix(),**ident(p.read_bytes())} for p in sorted(source.rglob('*')) if p.is_file() and p.name!='inputs.json' and '__pycache__' not in p.parts]
    write(source/'inputs.json',{'files':files,'pdfs':pdfs,'source_date_epoch':'1790010000'})
    write(source/'README.md','# Exact R56 chapter-proof sources\n\nThese are isolated cumulative-draft chapter proofs before and after 86 edits representing 76 proposed corrections and clarifications. External chapter auxiliaries are intentionally absent in both versions; unchanged external references appear as ?? in the proofs. This is not a replacement for the complete Stacks reader.\n\nUse Python with the bundled helper scripts and a TeX installation with the Stacks packages (including Latin Modern and XY-pic). Run `python reproduce.py --role successor --chapter stacks --output /path/to/new-build`; replace the role or chapter as desired. On Windows the script holds Global\\InterlanguageTeXSlotV1 for the full captured build. It fails closed if the slot is unavailable. The exact PDFs were obtained with MiKTeX/pdfTeX; software/font differences may prevent byte-identical reproduction elsewhere. inputs.json records source and target hashes.\n\nModified Stacks source retains GNU FDL 1.2; COPYING is included. AI corrections, packaging and checks: OpenAI Codex — GPT-6 Astra, Ultra effort. No human review or official endorsement is claimed.\n')
    # Re-enumerate after the reader-facing source instructions have been added.
    files=[{'path':p.relative_to(source).as_posix(),**ident(p.read_bytes())} for p in sorted(source.rglob('*')) if p.is_file() and p.name!='inputs.json' and '__pycache__' not in p.parts]
    write(source/'inputs.json',{'files':files,'pdfs':pdfs,'source_date_epoch':'1790010000'})
    archive=c/'proofs/complete-proof-source.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_STORED) as z:
        for item in [*files,{'path':'inputs.json'}]:
            info=zipfile.ZipInfo(item['path'],(2026,9,24,0,0,0));info.create_system=3;info.external_attr=0o100644<<16
            z.writestr(info,(source/item['path']).read_bytes())
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None and len(z.namelist())==len(files)+1
        for name in z.namelist():assert z.read(name)==(source/name).read_bytes()
    if a.package_only:
        print(json.dumps({'packaged':True,'source_zip':ident(archive.read_bytes()),'files':len(files)+1}));return
    inspected=json.loads((CONTROL/'R56_ACTUAL_VISUAL_REVIEW_20260924.json').read_bytes())
    for chapter in ('stacks',):
        work=CONTROL/BUILD_DIRS[chapter]; comparison=json.loads((work/'visual/comparison.json').read_bytes())
        assert inspected[chapter]['pages']==[x['page'] for x in comparison['inspection_images']] and inspected[chapter]['passed']
        comparison.update(status='PASS_CHANGED_PAGE_REGRESSION',changed_pages_visual_review='PASS',
            review_notes=inspected[chapter]['notes'],reviewer='OpenAI Codex - GPT-6 Astra, Ultra effort',
            scope='All pages raster-compared at 72 dpi. Every changed or correction-bearing successor page inspected in complete-page layout sheets, plus corrected-region sheets from 150-dpi renders. The actual page/sheet counts and limitations are recorded in the review notes. Unchanged pages are not claimed to have new mathematical or visual certification.')
        for row in comparison['inspection_images']:
            file=work/row['image'];assert ident(file.read_bytes())=={'bytes':row['bytes'],'sha256':row['sha256']}
            write(c/f'visual/{chapter}/page-{row["page"]}.png',file.read_bytes())
            row['image']=f'visual/{chapter}/page-{row["page"]}.png'
        write(c/f'visual/{chapter}.json',comparison);visuals.append(comparison)
    for chapter in ('stacks',):
        reproduction=(CONTROL/f'r56-proof-reproduction-{chapter}-20260924/REPRODUCTION.json').read_bytes()
        assert json.loads(reproduction)['passed']
        write(c/f'replay/package-reproduction-{chapter}.json',reproduction)
    review={'candidate_id':'stacks-errata-a04446e-r56','passed':True,'review_state':'performed','independent_replay':'passed',
        'unresolved_defects':[],'checks':[
            {'name':'Frozen-official and cumulative preimage replay, unchanged labels, citation keys, environments and reference targets, with complete required proof evidence','passed':True,'receipt':'replay/source-replay.json'},
            {'name':'Prior/successor Stacks builds; two fresh successor identities; no new diagnostics','passed':True},
            {'name':'All pages compared; changed and source-mapped loci inspected','passed':True},
            {'name':'Complete proof-source ZIP reopened member by member; the packaged corrected proof independently reproduced','passed':True}],
        'source_review':'Bounded arguments and adverse evidence are recorded in REVIEW.md and the bound producer reviews. Mathematical edits and copyedits are labelled separately.',
        'reviewer':'OpenAI Codex - GPT-6 Astra, Ultra effort','independence_scope':'Executable replay and fresh builds by the primary AI task; two mathematical derivations and the full localization fragment also received the separately recorded AI checks. This is not a second review of every correction, and no human review is claimed.',
        'generated_at_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z')}
    total_pages=sum(v['page_count'] for v in visuals)
    assert total_pages==sum(b['builds'][1]['pages'] for b in builds)
    write(c/'replay/independent-review.json',review)
    text=['# Stacks: corrections and complete replacement proofs\n',
        'Seventy-six proposed corrections and clarifications, consisting of 86 exact edits: 34 copyedits, 35 source corrections and seven clarifications. These include a missing fibre-isomorphism requirement in the substack criterion and a false converse about cartesian morphisms after localization. The replacements retain complete counterexamples, proofs and the exact comparison maps. The localization proof establishes the correct criterion after refinement and its use in the adjointness argument. [Read each correction and its reason](REVIEW.md).\n',
        'AI correction review, source preparation, builds and visual checks: OpenAI Codex — GPT-6 Astra, Ultra effort. These are unofficial suggestions with no human review or upstream endorsement. Admission and cumulative composition are later, separately recorded transitions.\n',
        'The complete [substack derivation](evidence/SUBSTACK_VERTICAL_DERIVATION_20260923.md), [localization derivation](evidence/LOCALIZED_CARTESIAN_DERIVATION_20260924.md) and [independent proof-fragment check](evidence/STACKS_LOCALIZED_CARTESIAN_PROOF_CHECK_20260924.md) are retained with their primary-source locators.\n',
        '## Chapter proofs and editable sources\n',
        'These are isolated regression proofs, not the complete cross-referenced reader. Inherited external references remain unresolved identically before and after. Modified Stacks source retains GNU FDL 1.2.\n']
    for chapter in ('stacks',):
        text.append(f'- **{chapter.title()}**: [corrected proof PDF](proofs/{chapter}-successor.pdf), [complete chapter LaTeX](proof-source/successor/{chapter}.tex), [complete reproducible-source ZIP](proofs/complete-proof-source.zip); [prior proof PDF](proofs/{chapter}-prior.pdf), [prior chapter LaTeX](proof-source/prior/{chapter}.tex).\n')
    text.append('\nUse the corrected PDF and its direct LaTeX together with the ZIP dependencies. The archive contains both versions of the Stacks chapter, including the complete inserted proof, project preamble/class/chapter-list/bibliography, licence and guarded reproduction instructions. [Source instructions](proof-source/README.md).\n')
    write(c/'README.md','\n'.join(text))
    lease=json.loads((c/'LEASE.json').read_bytes())
    def ref(name):return {'path':name,**ident((c/name).read_bytes())}
    special={'stable_unit_manifest':'stable-units.json','source_map':'source-map.jsonl','decision_ledger':'decisions.jsonl','rejection_ledger':'rejections.jsonl','formula_diagram_inventory':'formula-diagram-inventory.json'}
    authorities=['authority/'+x+'.tex' for x in ('stacks',)]
    others=[p.relative_to(c).as_posix() for p in sorted(c.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.name!='candidate.manifest.json' and p.suffix!='.pyc']
    manifest={'schema':'mathematics-commons-stacks-candidate-manifest/v1','candidate_id':'stacks-errata-a04446e-r56',
        'lease_id':lease['lease_id'],'namespace':lease['namespace'],'writer_task':lease['writer_task'],
        'upstream':{'lock':'upstream/stacks.lock.json','commit':lease['upstream_commit'],'tree':lease['upstream_tree']},
        'source_authorities':[ref(n) for n in authorities],
        'source_closure':{'enumerated':True,'expected_units':76,'manifested_units':76,'complete':True},
        **{k:ref(v) for k,v in special.items()},'builds':[ref(n) for n in others if n not in authorities and n not in special.values()],
        'rights_state':'Modified Stacks source retains GNU FDL 1.2; exact COPYING preserved; no upstream endorsement.',
        'review_state':'performed','independent_replay':'passed','unresolved_defects':[],
        'stop_conditions':['Fail closed on source/hash/lease drift, unlisted edits, new diagnostics, failed deterministic replay or damaged rendering.'],
        'generated_at_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z')}
    from jsonschema import Draft202012Validator
    Draft202012Validator(json.loads((root/'ai-integrated/schemas/candidate-manifest.schema.json').read_bytes())).validate(manifest)
    write(c/'candidate.manifest.json',manifest)
    print(json.dumps({'sealed':True,'files':len(others)+1,'manifest':ident((c/'candidate.manifest.json').read_bytes()),'pages':total_pages}))

if __name__=='__main__':main()
