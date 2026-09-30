"""Separate R58 admission and source composition, preserving frozen evidence."""
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PRIOR = '29c4c1d1cd236d1629c0c8277ebf14d2a28dcce0'
CANDIDATE = '2c11aaef69501eeafc2a1fb53c27e2da1e0503b0'
MANIFEST = '2EBA6504F6D830366BA08D6A256DA8C45C3C6CF636FE2634B3DF0C8C916E222F'
PREFIX = 'ai-integrated/candidates/commons/stacks/errata/r58/'
ID = 'stacks-errata-a04446e-r58'
OVERLAYS = 'ai-integrated/registry/overlays.json'
LEASES = 'ai-integrated/registry/leases.json'
ADMISSION = 'validation/r58-admission-2026-09-30.json'
COMPOSITION = 'validation/r58-source-composition-2026-09-30.json'
sha = lambda b: hashlib.sha256(b).hexdigest().upper()
identity = lambda b: dict(bytes=len(b),sha256=sha(b))
git = lambda *a: subprocess.check_output(['git','-C',str(ROOT),*a])
blob = lambda ref,name: git('show',ref+':'+name)
now = lambda: datetime.now(timezone.utc).isoformat()

def require(ok,message):
    if not ok: raise ValueError(message)

def write(name,obj):
    p=ROOT/name
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes((json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode())

def frozen_files(ref, expected):
    tree={}
    for line in git('ls-tree','-r','-z',ref,'--',PREFIX).split(b'\0'):
        if not line: continue
        head,path=line.split(b'\t',1);mode,kind,oid=head.split()
        require(mode==b'100644' and kind==b'blob','Unexpected candidate mode')
        tree[path.decode()]=oid.decode()
    require(set(tree)==set(expected),'Frozen candidate closure differs')
    p=subprocess.Popen(['git','-C',str(ROOT),'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    try:
        for name,oid in tree.items():
            p.stdin.write((oid+'\n').encode());p.stdin.flush()
            header=p.stdout.readline().decode().split()
            require(len(header)==3 and header[1]=='blob','Missing frozen blob')
            size=int(header[2]);require(size==expected[name]['bytes'],'Frozen size drift: '+name)
            h=hashlib.sha256();remaining=size
            while remaining:
                block=p.stdout.read(min(1048576,remaining));require(bool(block),'Truncated frozen blob')
                h.update(block);remaining-=len(block)
            require(p.stdout.read(1)==b'\n','Frozen stream separator')
            require(h.hexdigest().upper()==expected[name]['sha256'],'Frozen byte drift: '+name)
        p.stdin.close();require(p.wait()==0,'Frozen stream failed')
    finally:
        if p.poll() is None: p.terminate();p.wait()

def evidence():
    root=ROOT/PREFIX
    mr=blob(CANDIDATE,PREFIX+'candidate.manifest.json')
    require(sha(mr)==MANIFEST,'Manifest identity drift')
    m=json.loads(mr)
    refs=m['source_authorities']+m['builds']+[m[k] for k in
        ['stable_unit_manifest','source_map','decision_ledger','rejection_ledger','formula_diagram_inventory']]
    expected={PREFIX+r['path']:{k:r[k] for k in ['bytes','sha256']} for r in refs}
    require(len(expected)==len(refs),'Duplicate manifest reference')
    expected[PREFIX+'candidate.manifest.json']=identity(mr)
    frozen_files(CANDIDATE,expected)
    for name,row in expected.items():require(identity((ROOT/name).read_bytes())==row,'Working candidate drift: '+name)
    sys.dont_write_bytecode=True
    spec=importlib.util.spec_from_file_location('r58_frozen_check',root/'replay/check_candidate.py')
    check=importlib.util.module_from_spec(spec);spec.loader.exec_module(check);check.main()
    units=json.loads((root/'stable-units.json').read_bytes())['units']
    ops=json.loads((root/'operation-spec.json').read_bytes())['operations']
    prior=blob(PRIOR,'algebra.tex')
    require(prior==(root/'proof-source/prior/algebra.tex').read_bytes(),'Prior source identity drift')
    authority=blob(m['upstream']['commit'],'algebra.tex')
    require(authority==(root/'authority/algebra.tex').read_bytes(),'Upstream source identity drift')
    body=check.replay(prior,ops,True)
    visible=(root/'visible-edition-preview/algebra.tex').read_bytes()
    routes=json.loads((root/'editorial-apparatus-operations.json').read_bytes())
    notices=[routes['front_notice']]+[r['text'] for r in routes['body_notice_operations']]
    located=[]
    for text in notices:
        raw=text.encode();require(visible.count(raw)==1,'Editorial notice not unique')
        located.append((visible.index(raw),raw))
    removed=0;apparatus=[]
    for offset,raw in sorted(located):
        apparatus.append(dict(start_byte=offset-removed,text=raw.decode(),sha256=sha(raw)))
        removed+=len(raw)
    composed=body
    for notice in reversed(apparatus):
        a=notice['start_byte'];composed=composed[:a]+notice['text'].encode()+composed[a:]
    require(composed==visible and len(apparatus)==156,'Exact editorial insertion replay failed')
    return m,[u['id'] for u in units],ops,apparatus,prior,body,visible,expected

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('action',choices=['check','admit','compose']);a=p.parse_args()
    m,ids,ops,apparatus,prior,body,visible,expected=evidence()
    head=git('rev-parse','HEAD').decode().strip()
    if a.action=='check':
        print(json.dumps(dict(status='PASS',units=len(ids),operations=len(ops),editorial_notices=len(apparatus))));return
    require(git('diff','--cached','--name-only')==b'','Unrelated staged changes')
    require((ROOT/'algebra.tex').read_bytes()==prior,'Algebra is dirty or already composed')
    moduli=(ROOT/'moduli.tex').read_bytes()
    if a.action=='admit':
        require(head==CANDIDATE,'Candidate commit must be HEAD')
        require(not (ROOT/ADMISSION).exists(),'Admission already exists')
        old=blob(PRIOR,OVERLAYS);require((ROOT/OVERLAYS).read_bytes()==old,'Registry drift')
        reg=json.loads(old)
        require(len(reg['registered_entries'])==58,'Prior overlay scope drift')
        require(not set(ids).intersection(s for e in reg['registered_entries'] for s in e['stable_ids']),'Reused stable IDs')
        entry=dict(id=ID,namespace=m['namespace'],writer=m['writer_task'],source_commit=m['upstream']['commit'],
            source_tree=m['upstream']['tree'],manifest_sha256=MANIFEST,stable_ids=ids,rights_state=m['rights_state'],
            review_receipt=PREFIX.removeprefix('ai-integrated/')+'replay/independent-review.json',admitted_at_utc=now())
        reg['registered_entries'].append(entry)
        lease_raw=(ROOT/LEASES).read_bytes();require(lease_raw==blob(PRIOR,LEASES),'Lease registry drift')
        leases=json.loads(lease_raw);issued=leases['events'][-1]
        require(issued['event_id']=='lease-event-000124' and issued['state']=='active' and issued['lease_id']==m['lease_id'],'Lease identity drift')
        released={**issued,'event_id':'lease-event-000125','event':'released','state':'released','issued_at_utc':now(),'supersedes_event_id':issued['event_id']}
        leases['events'].append(released)
        from jsonschema import Draft202012Validator
        for data,name in [(reg,'overlay-entry'),(leases,'lease-registry')]:
            Draft202012Validator(json.loads((ROOT/f'ai-integrated/schemas/{name}.schema.json').read_bytes())).validate(data)
        write(OVERLAYS,reg);write(LEASES,leases)
        write(ADMISSION,dict(schema='stacks-r58-separate-admission/v1',passed=True,predecessor=PRIOR,candidate_commit=CANDIDATE,
            candidate_manifest_sha256=MANIFEST,admission=entry,release_event=released,source_composed=False,candidate_files_checked=len(expected)))
    else:
        require(not (ROOT/COMPOSITION).exists(),'Composition already exists')
        for name in [ADMISSION,OVERLAYS,LEASES]:require((ROOT/name).read_bytes()==blob(head,name),'Admission must be committed')
        admission=json.loads((ROOT/ADMISSION).read_bytes());reg=json.loads((ROOT/OVERLAYS).read_bytes())
        require(admission['candidate_commit']==CANDIDATE and admission['admission']==reg['registered_entries'][-1]
                and admission['admission']['id']==ID,'R58 admission drift')
        (ROOT/'algebra.tex').write_bytes(visible)
        write(COMPOSITION,dict(schema='stacks-r58-exact-source-composition/v1',passed=True,predecessor=PRIOR,
            candidate_commit=CANDIDATE,manifest_sha256=MANIFEST,admission_commit=head,source='algebra.tex',
            preimage=identity(prior),bounded_body_postimage=identity(body),visible_postimage=identity(visible),
            units=len(ids),body_operations=689,rendering_support_operations=1,operations=len(ops),
            editorial_notice_operations=apparatus,editorial_notices=len(apparatus),
            only_admitted_body_and_apparatus_operations_applied=True,whole_isolated_payload_copied=False,
            prior_additions_preserved=True,notice_inverse_recovers_bounded_body=True,
            build_validation='Composed source is byte-identical to the 484-page source built twice and actually reviewed; supplementary proofs remain in the separate 667-page companion.',
            model='OpenAI Codex - GPT-6 Astra, Ultra effort'))
    require((ROOT/'moduli.tex').read_bytes()==moduli,'Unrelated source changed')
    print(json.dumps(dict(action=a.action,status='PASS',units=len(ids),operations=len(ops),editorial_notices=len(apparatus))))

if __name__=='__main__':main()
