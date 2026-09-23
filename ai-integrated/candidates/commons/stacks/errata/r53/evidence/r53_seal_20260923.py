"""Collect completed R53 proof evidence and seal the candidate; no registry admission."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import zipfile

CONTROL=Path(__file__).resolve().parent
BUILD_DIRS={'introduction':'r53-build-introduction-20260922','topology':'r53-build-topology-v2-20260922'}
def ident(raw):return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest().upper()}
def write(p,v):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(v if isinstance(v,bytes) else (v if isinstance(v,str) else json.dumps(v,indent=2,ensure_ascii=False)+'\n').encode())

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--package-only',action='store_true');a=p.parse_args()
    root=a.repo.resolve(); c=root/'ai-integrated/candidates/commons/stacks/errata/r53'
    assert not (c/'candidate.manifest.json').exists(),'Never rewrite a sealed manifest'
    pdfs={'prior':{},'successor':{}}; builds=[]; visuals=[]
    for chapter in ('introduction','topology'):
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
    reproduction_script=(root/'ai-integrated/candidates/commons/stacks/errata/r51/proof-source/reproduce.py').read_text(encoding='utf-8').replace('R51','R53').replace("choices=['sets','schemes','homology','algebra']", "choices=['introduction','topology']")
    write(c/'proof-source/reproduce.py',reproduction_script)
    source=c/'proof-source'
    files=[{'path':p.relative_to(source).as_posix(),**ident(p.read_bytes())} for p in sorted(source.rglob('*')) if p.is_file() and p.name!='inputs.json' and '__pycache__' not in p.parts]
    write(source/'inputs.json',{'files':files,'pdfs':pdfs,'source_date_epoch':'1790010000'})
    write(source/'README.md','# Exact R53 chapter-proof sources\n\nThese are isolated cumulative-draft chapter proofs before and after 64 edits representing 54 proposed changes. External chapter auxiliaries are intentionally absent in both versions; unchanged external references appear as ?? in the proofs. This is not a replacement for the complete Stacks reader.\n\nUse Python with the bundled helper scripts and a TeX installation with the Stacks packages (including Latin Modern and XY-pic). Run `python reproduce.py --role successor --chapter topology --output /path/to/new-build`; replace the role or chapter as desired. On Windows the script holds Global\\InterlanguageTeXSlotV1 for the full captured build. It fails closed if the slot is unavailable. The exact PDFs were obtained with MiKTeX/pdfTeX; software/font differences may prevent byte-identical reproduction elsewhere. inputs.json records source and target hashes.\n\nModified Stacks source retains GNU FDL 1.2; COPYING is included. AI corrections, packaging and checks: OpenAI Codex — GPT-6 Astra, Ultra effort. No human review or official endorsement is claimed.\n')
    # Re-enumerate after the reader-facing source instructions have been added.
    files=[{'path':p.relative_to(source).as_posix(),**ident(p.read_bytes())} for p in sorted(source.rglob('*')) if p.is_file() and p.name!='inputs.json' and '__pycache__' not in p.parts]
    write(source/'inputs.json',{'files':files,'pdfs':pdfs,'source_date_epoch':'1790010000'})
    archive=c/'proofs/complete-proof-source.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_STORED) as z:
        for item in [*files,{'path':'inputs.json'}]:
            info=zipfile.ZipInfo(item['path'],(2026,9,22,0,0,0));info.create_system=3;info.external_attr=0o100644<<16
            z.writestr(info,(source/item['path']).read_bytes())
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None and len(z.namelist())==len(files)+1
        for name in z.namelist():assert z.read(name)==(source/name).read_bytes()
    if a.package_only:
        print(json.dumps({'packaged':True,'source_zip':ident(archive.read_bytes()),'files':len(files)+1}));return
    inspected=json.loads((CONTROL/'R53_ACTUAL_VISUAL_REVIEW_20260922.json').read_bytes())
    for chapter in ('introduction','topology'):
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
    for chapter in ('introduction','topology'):
        reproduction=(CONTROL/f'r53-proof-reproduction-{chapter}-20260922/REPRODUCTION.json').read_bytes()
        assert json.loads(reproduction)['passed']
        write(c/f'replay/package-reproduction-{chapter}.json',reproduction)
    review={'candidate_id':'stacks-errata-a04446e-r53','passed':True,'review_state':'performed','independent_replay':'passed',
        'unresolved_defects':[],'checks':[
            {'name':'Frozen-official and cumulative preimage replay, labels/references/citations/environments','passed':True,'receipt':'replay/source-replay.json'},
            {'name':'Prior/successor Introduction and Topology builds; two fresh successor identities; no new diagnostics and fewer underfull boxes','passed':True},
            {'name':'All pages compared; changed and source-mapped loci inspected','passed':True},
            {'name':'Complete proof-source ZIP reopened member by member; both packaged corrected proofs independently reproduced','passed':True}],
        'source_review':'Bounded arguments and adverse evidence are recorded in REVIEW.md and the bound producer reviews. Mathematical edits and copyedits are labelled separately.',
        'reviewer':'OpenAI Codex - GPT-6 Astra, Ultra effort','independence_scope':'Separate executable replay and fresh builds by the same primary AI task, not another AI or human reviewer.',
        'generated_at_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z')}
    total_pages=sum(v['page_count'] for v in visuals)
    assert total_pages==sum(b['builds'][0]['pages'] for b in builds)
    write(c/'replay/independent-review.json',review)
    text=['# Topology and Introduction: proposed corrections and clarifications\n',
        'Fifty-four proposed changes, consisting of 64 exact edits: 44 copyedits, five clarifications, four notation clarifications and one source correction. Noteworthy changes make the connected-image proof explicitly restrict its domain, restore a missing inclusion sign in a dimension argument, and clarify the scope of set operations. No new theorems are included. [Read each correction and its reason](REVIEW.md).\n',
        'AI correction review, source preparation, builds and visual checks: OpenAI Codex — GPT-6 Astra, Ultra effort. These are unofficial suggestions with no human review or upstream endorsement. Admission and cumulative composition are later, separately recorded transitions.\n',
        '## Chapter proofs and editable sources\n',
        'These are isolated regression proofs, not the complete cross-referenced reader. Inherited external references remain unresolved identically before and after. Modified Stacks source retains GNU FDL 1.2.\n']
    for chapter in ('introduction','topology'):
        text.append(f'- **{chapter.title()}**: [corrected proof PDF](proofs/{chapter}-successor.pdf), [complete chapter LaTeX](proof-source/successor/{chapter}.tex), [complete reproducible-source ZIP](proofs/complete-proof-source.zip); [prior proof PDF](proofs/{chapter}-prior.pdf), [prior chapter LaTeX](proof-source/prior/{chapter}.tex).\n')
    text.append('\nUse the corrected PDF and its direct LaTeX together with the ZIP dependencies. The archive contains both versions of the Introduction and Topology chapters, project preamble/class/chapter-list/bibliography, licence and guarded reproduction instructions. [Source instructions](proof-source/README.md).\n')
    write(c/'README.md','\n'.join(text))
    lease=json.loads((c/'LEASE.json').read_bytes())
    def ref(name):return {'path':name,**ident((c/name).read_bytes())}
    special={'stable_unit_manifest':'stable-units.json','source_map':'source-map.jsonl','decision_ledger':'decisions.jsonl','rejection_ledger':'rejections.jsonl','formula_diagram_inventory':'formula-diagram-inventory.json'}
    authorities=['authority/'+x+'.tex' for x in ('introduction','topology')]
    others=[p.relative_to(c).as_posix() for p in sorted(c.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.name!='candidate.manifest.json' and p.suffix!='.pyc']
    manifest={'schema':'mathematics-commons-stacks-candidate-manifest/v1','candidate_id':'stacks-errata-a04446e-r53',
        'lease_id':lease['lease_id'],'namespace':lease['namespace'],'writer_task':lease['writer_task'],
        'upstream':{'lock':'upstream/stacks.lock.json','commit':lease['upstream_commit'],'tree':lease['upstream_tree']},
        'source_authorities':[ref(n) for n in authorities],
        'source_closure':{'enumerated':True,'expected_units':54,'manifested_units':54,'complete':True},
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
