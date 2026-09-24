"""Separate, hash-bound R56 candidate admission and cumulative composition."""
import argparse
from collections import Counter
from datetime import datetime,timezone
import io
import json
from pathlib import Path
import zipfile
try:
    from . import r50_successor as common
except ImportError:
    import r50_successor as common
ROOT=common.ROOT
PRIOR='4fddc4a808dc08f74755ac2327e9e9547bb4501f'
CANDIDATE='ca2c69c79e9c6dcc0f8b309141bcb2c884e79e6e'
MANIFEST='49ED177B294848FF3851114D501DDB2A5A988A795B6FF560B1061B851662BC92'
PREFIX='ai-integrated/candidates/commons/stacks/errata/r56/'
ID='stacks-errata-a04446e-r56'
OVERLAYS=common.OVERLAYS
LEASES=common.LEASES
ADMISSION='validation/r56-admission-2026-09-24.json'
COMPOSITION='validation/r56-source-composition-2026-09-24.json'
require=common.require
git=common.git
blob=common.blob
sha=common.sha
identity=common.identity
write=common.write
def now():return datetime.now(timezone.utc).isoformat().replace('+00:00','Z')

def replay(raw,ops):
    boundary=len(raw)
    for op in sorted(ops,key=lambda o:o['start_byte'],reverse=True):
        a,b=op['start_byte'],op['end_byte_exclusive'];old,new=op['old_text'].encode(),op['replacement_text'].encode()
        require(0<=a<b<=boundary and raw[a:b]==old,'Operation preimage/overlap drift: '+op['operation_id'])
        require(sha(old)==op['old_sha256'] and sha(new)==op['replacement_sha256'],'Operation hash drift')
        raw=raw[:a]+new+raw[b:];boundary=a
    return raw

def evidence():
    read=lambda name:blob(CANDIDATE,PREFIX+name)
    manifest_raw=read('candidate.manifest.json');require(sha(manifest_raw)==MANIFEST,'Candidate manifest drift')
    m=json.loads(manifest_raw)
    refs=m['source_authorities']+m['builds']+[m[k] for k in ('stable_unit_manifest','source_map','decision_ledger','rejection_ledger','formula_diagram_inventory')]
    names={PREFIX+'candidate.manifest.json'}
    for row in refs:
        name=row['path'];require(not Path(name).is_absolute() and '..' not in Path(name).parts,'Unsafe evidence path')
        raw=read(name);require(identity(raw)=={'bytes':row['bytes'],'sha256':row['sha256']},'Frozen reference drift: '+name)
        require((ROOT/PREFIX/name).read_bytes()==raw,'Working candidate drift: '+name)
        require(PREFIX+name not in names,'Duplicate evidence reference');names.add(PREFIX+name)
    require(names==set(git('ls-tree','-r','--name-only',CANDIDATE,'--',PREFIX).decode().splitlines()),'Git candidate closure incomplete')
    require(m['review_state']=='performed' and m['independent_replay']=='passed' and not m['unresolved_defects'],'Missing review gates')
    review=json.loads(read('replay/independent-review.json'));require(review['passed'] and all(x['passed'] for x in review['checks']),'Review failed')
    stable=json.loads(read('stable-units.json'))['units'];ids=[u['id'] for u in stable]
    require(ids==[f'MC-STK-ERR-{i}' for i in range(1783,1859)],'Unit scope drift')
    operations=json.loads(read('operation-spec.json'))['operations'];require(len(operations)==86,'Operation scope drift')
    maps=[json.loads(line) for line in read('source-map.jsonl').decode().splitlines()]
    require([x['unit_id'] for x in maps]==ids,'Source-map IDs drift')
    canon=lambda v:json.dumps(v,sort_keys=True)
    require(Counter(map(canon,operations))==Counter(canon(o) for row in maps for o in row['operations']),'Source-map operations differ')
    batch=json.loads(read('evidence/prepared-batch.json'));sources=[]
    proof_review=json.loads(read('evidence/STACKS_INTAKE_REVIEW_20260923.json'))
    require(proof_review['mathematical_review_complete'], 'Mathematical review incomplete')
    required={row['path']:row for row in proof_review['required_proof_evidence']}
    require(len(required)==6, 'Complete proof evidence missing')
    for name,row in required.items():
        require(identity(read('evidence/'+name))=={k:row[k] for k in ('bytes','sha256')}, 'Complete proof changed: '+name)
    deps=json.loads(read('mathematical-proof-dependencies.json'))
    canonical={u['producer_id']:u['id'] for u in stable}
    require(deps['groups']==[{**g,'stable_ids':[canonical[rid] for rid in g['review_ids']]} for g in batch['dependency_groups']], 'Mathematical dependency loss')
    require(len(deps['groups'])==2 and all(g['required_together'] for g in deps['groups']), 'Incomplete mathematical dependency groups')
    require(deps['required_proof_evidence']==proof_review['required_proof_evidence'], 'Lost proof dependency')
    fragment=read('evidence/STACKS_LOCALIZED_CARTESIAN_PROOF_20260924.tex').decode().rstrip('\n')
    proof_ops=[o for o in operations if o['producer_id']=='STACKS-RECON-077' and o['line']==3124]
    require(len(proof_ops)==1 and proof_ops[0]['replacement_text']==fragment, 'Complete proof omitted from source')
    for row in batch['sources']:
        name=row['source'];prior=blob(PRIOR,name);authority=blob(common.AUTHORITY,name)
        require(identity(prior)==row['cumulative_preimage'] and authority==read('authority/'+name),'Authority/prior drift')
        original_ops=[o for o in operations if o['source']==name]
        original_content=Counter((o['producer_operation_id'],o['old_text'],o['replacement_text']) for o in original_ops)
        rebound_content=Counter((o['operation_id'],o['old_text'],o['replacement_text']) for o in row['rebound_operations'])
        require(original_content==rebound_content,'Cumulative replay changed an operation')
        require(replay(authority,original_ops)==read('payload/'+name),'Isolated payload has unlisted edits')
        post=replay(prior,row['rebound_operations']);require(post==read('cumulative-preview/'+name),'Preview has unlisted edits')
        require(identity(post)==row['prospective_cumulative_postimage'],'Preview hash drift')
        stem=name[:-4];build=json.loads(read('builds/'+stem+'.json'));visual=json.loads(read('visual/'+stem+'.json'))
        old,first,second=build['builds']
        require(old['source']==identity(prior) and first['source']==second['source']==identity(post),'Built wrong source')
        require(first['identities']==second['identities'] and first['pdf']==second['pdf'],'Nonreproducible proof')
        before,after=old['diagnostics'],first['diagnostics']
        require(after==second['diagnostics'] and set(before)==set(after),'Diagnostic field/replay drift')
        for key in before:
            require(after[key]<=before[key] if key=='underfull_boxes' else after[key]==before[key], 'Diagnostic regression: '+key)
        require(not after['fatal_duplicate_glyph_rerun'],'Fatal diagnostic')
        require(build['mutex']['name']==r'Global\InterlanguageTeXSlotV1' and 'released_utc' in build['mutex'],'Missing guarded TeX lifetime')
        for item in build['input_files']:
            filename=item['build_filename']
            expected=post if filename==name else blob(PRIOR,filename)
            require(identity(expected)=={'bytes':item['bytes'],'sha256':item['sha256']},'Build dependency drift')
        require(visual['status']=='PASS_CHANGED_PAGE_REGRESSION' and visual['changed_pages_visual_review']=='PASS','Visual review missing')
        require(visual['prior_pdf']==old['pdf'] and visual['successor_pdf']==first['pdf'],'Visual identity drift')
        require(visual['prior_page_count']==old['pages'] and visual['page_count']==first['pages'], 'Pagination binding drift')
        require(visual['page_count_change']==first['pages']-old['pages'], 'Pagination delta drift')
        require([r['page'] for r in visual['pages']]==list(range(1,first['pages']+1)),'Missing page comparison')
        require(visual['changed_pages']==[r['page'] for r in visual['pages'] if r['changed_bbox']],'Changed-page list mismatch')
        require(set(visual['changed_pages']).issubset({r['page'] for r in visual['inspection_images']}),'Uninspected changed page')
        require({o['operation_id'] for o in row['rebound_operations']}=={o['operation_id'] for o in visual['mapped_operations']},'Unmapped operation')
        for role,b in [('prior',old),('successor',first)]:
            require(identity(read('proofs/'+stem+'-'+role+'.pdf'))==b['pdf'],'Proof PDF drift')
        sources.append({'source':name,'preimage':identity(prior),'postimage':identity(post),'operations':row['rebound_operations']})
    archive=read('proofs/complete-proof-source.zip')
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        require(z.testzip() is None,'Corrupt editable-source ZIP')
        expected={p.removeprefix(PREFIX+'proof-source/') for p in names if p.startswith(PREFIX+'proof-source/')}
        require(set(z.namelist())==expected,'Incomplete editable-source ZIP')
        for name in z.namelist():require(z.read(name)==read('proof-source/'+name),'ZIP member drift')
    return m,refs,ids,sources,names

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('action',choices=['check','admit','compose']);a=p.parse_args()
    m,refs,ids,sources,names=evidence();head=git('rev-parse','HEAD').decode().strip()
    if a.action=='check':print(json.dumps({'passed':True,'files':len(names),'units':len(ids),'operations':86}));return
    for row in sources:require(identity((ROOT/row['source']).read_bytes())==row['preimage'],'Dirty or already composed chapter')
    if a.action=='admit':
        require(head==CANDIDATE,'Candidate freeze is not HEAD')
        raw=(ROOT/OVERLAYS).read_bytes();require(raw==blob(PRIOR,OVERLAYS),'Registry drift before admission')
        reg=json.loads(raw);require(not set(ids).intersection(s for e in reg['registered_entries'] for s in e['stable_ids']),'Duplicate stable IDs')
        entry={'id':ID,'namespace':m['namespace'],'writer':m['writer_task'],'source_commit':m['upstream']['commit'],
            'source_tree':m['upstream']['tree'],'manifest_sha256':MANIFEST,'stable_ids':ids,'rights_state':m['rights_state'],
            'review_receipt':PREFIX.removeprefix('ai-integrated/')+'replay/independent-review.json','admitted_at_utc':now()}
        reg['registered_entries'].append(entry)
        leases=json.loads((ROOT/LEASES).read_bytes());issued=leases['events'][-1]
        require(issued['event_id']=='lease-event-000120' and issued['state']=='active' and issued['lease_id']==m['lease_id'],'Lease changed')
        release={**issued,'event_id':'lease-event-000121','event':'released','state':'released','issued_at_utc':now(),'supersedes_event_id':issued['event_id']}
        leases['events'].append(release)
        from jsonschema import Draft202012Validator
        for data,schema in [(reg,'overlay-entry'),(leases,'lease-registry')]:
            Draft202012Validator(json.loads((ROOT/f'ai-integrated/schemas/{schema}.schema.json').read_bytes())).validate(data)
        write(ROOT/OVERLAYS,reg);write(ROOT/LEASES,leases)
        write(ROOT/ADMISSION,{'schema':'stacks-r56-separate-admission/v1','passed':True,'previous_public':PRIOR,'candidate_commit':CANDIDATE,
            'candidate_manifest_sha256':MANIFEST,'admission':entry,'release_event':release,'source_composed':False,'candidate_files_checked':len(names)})
    else:
        reg=json.loads((ROOT/OVERLAYS).read_bytes());require(reg['registered_entries'][-1]['id']==ID,'R56 not admitted')
        for path in (OVERLAYS,LEASES,ADMISSION):require((ROOT/path).read_bytes()==blob(head,path),'Admission not committed')
        for row in sources:
            name=row['source'];pre=(ROOT/name).read_bytes();post=replay(pre,row['operations'])
            require(identity(post)==row['postimage'],'Postimage mismatch');(ROOT/name).write_bytes(post)
        write(ROOT/COMPOSITION,{'schema':'stacks-r56-exact-source-composition/v1','passed':True,'previous_public':PRIOR,
            'candidate_commit':CANDIDATE,'manifest_sha256':MANIFEST,'admission_commit':head,'sources':sources,
            'operations':86,'units':76,'whole_isolated_payload_copied':False,'only_admitted_operations_applied':True,
            'prevalidated_preview_bytes_match_composition':True,'prior_additions_preserved':True,
            'build_validation':'Exact source bytes equal the candidate cumulative previews already built twice, with prior comparison and changed-region visual QA.',
            'model':'OpenAI Codex - GPT-6 Astra, Ultra effort'})
    print(json.dumps({'action':a.action,'passed':True,'units':76,'operations':86}))

if __name__=='__main__':main()


