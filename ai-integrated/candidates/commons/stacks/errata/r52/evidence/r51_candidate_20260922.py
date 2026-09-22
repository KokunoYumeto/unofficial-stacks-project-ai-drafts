"""Receipt-separated R51 lease and candidate materialization, never source composition."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

CONTROL = Path(__file__).resolve().parent
BASE = 'a04446e57ec1fbc252a871afcec7752fb2807b14'
TREE = '3feeb703b931a6e7259782c10e7d1575adc83e5e'
PRIOR = 'cf3f3a85ccf0ac433524c7a075a1e9b267f49fe7'
WRITER = '019fca5a-c29e-7330-acdc-c93f4a3dc9fb'
PREFIX = 'ai-integrated/candidates/commons/stacks/errata/r51'
BATCH_HASH = 'B686D3A4A37C6F75B1FF441C5E6931E32D1A9772CEEEF51D8C175B89DF35A9F5'

def sha(raw): return hashlib.sha256(raw).hexdigest().upper()
def ident(raw): return {'bytes': len(raw), 'sha256': sha(raw)}
def now(): return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
def require(ok, message):
    if not ok: raise ValueError(message)
def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = value if isinstance(value, bytes) else (value if isinstance(value, str) else json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode()
    path.write_bytes(raw)
def replay(raw, operations):
    boundary = len(raw)
    for op in sorted(operations, key=lambda x:x['start_byte'], reverse=True):
        a,b = op['start_byte'],op['end_byte_exclusive']
        old,new = op['old_text'].encode(),op['replacement_text'].encode()
        require(0 <= a < b <= boundary and raw[a:b] == old, 'Preimage or overlap: '+op['operation_id'])
        require(sha(old)==op['old_sha256'] and sha(new)==op['replacement_sha256'], 'Operation hash drift')
        raw=raw[:a]+new+raw[b:]
        boundary=a
    return raw

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=['lease','materialize','map','replay'])
    p.add_argument('--repo',type=Path,required=True)
    args=p.parse_args(); root=args.repo.resolve(); candidate=root/PREFIX
    def git(*a): return subprocess.run(['git','-C',str(root),*a],capture_output=True,check=True).stdout
    def blob(ref,name): return git('show',ref+':'+name)
    overlays_path=root/'ai-integrated/registry/overlays.json'
    leases_path=root/'ai-integrated/registry/leases.json'
    overlays=json.loads(overlays_path.read_bytes()); leases=json.loads(leases_path.read_bytes())
    raw=(CONTROL/'NEXT_CORRECTION_BATCH_INPUT_20260922.json').read_bytes()
    require(sha(raw)==BATCH_HASH,'Prepared batch changed')
    batch=json.loads(raw)
    require(overlays_path.read_bytes()==blob(PRIOR,'ai-integrated/registry/overlays.json'),'New registry changes require rebase')
    require(batch['registry_sha256']==sha(overlays_path.read_bytes()),'Reviewed registry mismatch')
    ids=[s for e in overlays['registered_entries'] for s in e['stable_ids'] if re.fullmatch(r'MC-STK-ERR-[0-9]+',s)]
    start=max(int(s.rsplit('-',1)[-1]) for s in ids)+1
    require(start==1576 and len(batch['units'])==29 and batch['operation_count']==33,'Unexpected batch/ID scope')
    if args.action=='lease':
        require(git('rev-parse','HEAD').decode().strip()==PRIOR,'Unexpected starting HEAD')
        require(not candidate.exists(),'Candidate already exists; do not allocate again')
        latest={e['lease_id']:e for e in leases['events']}
        namespace='commons/stacks/errata/r51'
        for e in latest.values():
            n=e['namespace']
            require(e['state']!='active' or not (n==namespace or n.startswith(namespace+'/') or namespace.startswith(n+'/')),'Conflicting active writer')
        number=max(int(e['lease_id'].split('-')[2]) for e in leases['events'])+1
        event={'event_id':f"lease-event-{len(leases['events'])+1:06d}",'event':'issued',
            'lease_id':f'stacks-lease-{number:06d}-errata-r51','namespace':namespace,
            'candidate_path':'candidates/'+namespace,'writer_task':WRITER,'upstream_commit':BASE,
            'upstream_tree':TREE,'issued_at_utc':now(),'state':'active','writer_contract':'candidates/CONTRACT.md'}
        require(event['event_id']=='lease-event-000108' and number==56,'Lease head advanced')
        leases['events'].append(event)
        from jsonschema import Draft202012Validator
        Draft202012Validator(json.loads((root/'ai-integrated/schemas/lease-registry.schema.json').read_bytes())).validate(leases)
        write(leases_path,leases); write(candidate/'LEASE.json',event)
        print(json.dumps({'action':'lease','event':event,'source_mutations':0})); return
    lease=json.loads((candidate/'LEASE.json').read_bytes())
    latest={e['lease_id']:e for e in leases['events']}
    require(latest[lease['lease_id']]==lease and lease['state']=='active' and lease['writer_task']==WRITER,'Not current writer')
    for row in batch['sources']:
        require((root/row['source']).read_bytes()==blob(PRIOR,row['source']),'Dirty cumulative source')
    if args.action=='materialize':
        require(not (candidate/'operation-spec.json').exists(),'Materialization already exists')
        write(candidate/'evidence/prepared-batch.json',raw)
        for row in batch['evidence']:
            src = root/row['path'] if '/' in row['path'] else CONTROL/row['path']
            evidence=src.read_bytes()
            require(ident(evidence)=={'bytes':row['bytes'],'sha256':row['sha256']},'Evidence drift')
            write(candidate/'evidence'/Path(row['path']).name,evidence)
        units=[]; ops=[]; source_map=[]; decisions=[]; formula=[]; aliases={}
        for i,unit in enumerate(batch['units']):
            sid=f'MC-STK-ERR-{start+i:04d}'; aliases[unit['id']]=sid
            cls=unit['class']; copyedit=(cls==['EDITORIAL'] or 'copyedit' in cls)
            kind='copyedit' if copyedit else 'diagram_source_correction' if 'diagram' in cls else 'mathematical_source_correction'
            rationale=unit['rationale']; rationale=' '.join(dict.fromkeys(rationale)) if isinstance(rationale,list) else rationale
            operation_ids=[]
            for j,op in enumerate(unit['operations'],1):
                oid=sid+f'-OP{j}'; operation_ids.append(oid)
                end_line=op['line']+op['old_text'].count('\n')
                ops.append({**op,'source':unit['source'],'stable_id':sid,'producer_id':unit['id'],
                    'producer_operation_id':op['operation_id'],'operation_id':oid,'class':kind,
                    'source_start_line':op['line'],'source_end_line':end_line,
                    'payload_start_line':op['line'],'payload_end_line':end_line,
                    'old_bytes':len(op['old_text'].encode()),'replacement_bytes':len(op['replacement_text'].encode())})
            units.append({'id':sid,'source':unit['source'],'payload':'payload/'+unit['source'],'class':kind,
                'producer_id':unit['id'],'producer_ids':[unit['id']], 'operation_ids':operation_ids,
                'rationale':rationale,'status':'accepted_candidate_not_admitted'})
            source_map.append({'unit_id':sid,'producer_id':unit['id'],'source':unit['source'],'operation_ids':operation_ids,
                'producer_occurrences':unit.get('producer_occurrences',[]),'review':'evidence/'+Path(unit['review_file']).name})
            decisions.append({'id':sid,'decision':'accept_bounded_correction','rationale':rationale,
                'adverse_evidence':unit.get('adverse_evidence','See the type/domain checks and original proof context in the bound review.'),
                'class':kind,'reviewer':'OpenAI Codex - GPT-6 Astra, Ultra effort','human_review':False})
            formula.append({'unit_id':sid,'class':kind,'operation_ids':operation_ids,
                'formula_policy':'Only the exact listed source tokens may change; labels, references, citations and environments must remain invariant.'})
        write(candidate/'operation-spec.json',{'schema':'mathematics-commons-stacks-operation-spec/v1','apply_order':'descending_start_byte_per_source','operation_count':len(ops),'operations':ops})
        write(candidate/'stable-units.json',{'schema':'mathematics-commons-stacks-stable-units/v1','authority_commit':BASE,'unit_count':29,'units':units})
        write(candidate/'source-map.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in source_map))
        write(candidate/'decisions.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in decisions))
        write(candidate/'rejections.jsonl',b'')
        write(candidate/'formula-diagram-inventory.json',{'units':formula,'dependency_groups':[[aliases[x] for x in g] for g in batch['dependency_groups']]})
        checked=[]
        for row in batch['sources']:
            name=row['source']; authority=blob(BASE,name); prior=blob(PRIOR,name)
            isolated=replay(authority,[o for o in ops if o['source']==name]); cumulative=replay(prior,row['rebound_operations'])
            for data,key in ((authority,'authority'),(prior,'cumulative_preimage'),(isolated,'prospective_isolated_postimage'),(cumulative,'prospective_cumulative_postimage')):
                require(ident(data)==row[key],name+' '+key)
            write(candidate/'authority'/name,authority); write(candidate/'payload'/name,isolated)
            write(candidate/'cumulative-preview'/name,cumulative)
            write(candidate/'proof-source/prior'/name,prior); write(candidate/'proof-source/successor'/name,cumulative)
            checked.append({'source':name,'authority':ident(authority),'prior':ident(prior),'isolated':ident(isolated),'cumulative':ident(cumulative)})
        for name in ('preamble.tex','stacks-project.cls','chapters.tex','my.bib'):
            for version in ('prior','successor'): write(candidate/'proof-source'/version/name,blob(PRIOR,name))
        write(candidate/'proof-source/COPYING',blob(BASE,'COPYING'))
        write(candidate/'materialization.json',{'schema':'stacks-r51-materialization/v1','candidate_id':'stacks-errata-a04446e-r51',
            'prior_public':PRIOR,'authority':BASE,'input_batch_sha256':BATCH_HASH,'sources':checked,'unit_count':29,
            'operation_count':33,'source_mutations':0,'admission':False,'created_at_utc':now()})
        review=['# Twenty-nine proposed corrections\n',
            'This batch repairs inherited text only. It adds no theorems. It combines missing Sets/Schemes findings with the eleven remaining proposals from the readable selection.\n',
            'AI review and correction preparation: OpenAI Codex — GPT-6 Astra, Ultra effort. No human review or upstream endorsement is claimed. Earlier rejected and optional findings remain in the bound evidence; they are not admitted by this batch.\n']
        for u in units:
            review.extend([f"## {u['producer_id']} — {u['source']} ({u['class']})\n",u['rationale']+'\n'])
            for op in [o for o in ops if o['stable_id']==u['id']]:
                review.extend([f"Official source line {op['line']}:\n",'```tex\n'+op['old_text']+'\n```\n','Replace with:\n','```tex\n'+op['replacement_text']+'\n```\n'])
        write(candidate/'REVIEW.md','\n'.join(review))
        print(json.dumps({'action':'materialize','units':29,'operations':33,'ids':[units[0]['id'],units[-1]['id']],'source_mutations':0})); return
    if args.action=='map':
        # Enrich the human/API review map before sealing; do not change any source operation.
        operations=json.loads((candidate/'operation-spec.json').read_bytes())['operations']
        stable=json.loads((candidate/'stable-units.json').read_bytes())['units']
        oldmaps=[json.loads(line) for line in (candidate/'source-map.jsonl').read_text(encoding='utf-8').splitlines()]
        by_producer={u['id']:u for u in batch['units']}
        rows=[]
        for u,row in zip(stable,oldmaps):
            require(u['id']==row['unit_id'],'Map order drift')
            original=by_producer[u['producer_id']]
            rows.append({**row,'authority':'authority/'+u['source'],'authority_sha256':sha(blob(BASE,u['source'])),
                'payload':u['payload'],'class':u['class'],'rationale':u['rationale'],
                'adverse_evidence':original.get('adverse_evidence','The exact type/domain argument is recorded in the bound review.'),
                'operations':[o for o in operations if o['stable_id']==u['id']]})
        write(candidate/'source-map.jsonl',''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
        print(json.dumps({'action':'map','units':len(rows),'operations':sum(len(r['operations']) for r in rows)})); return
    # A second executable verification route uses frozen Git preimages, not the writer's derived payloads.
    operations=json.loads((candidate/'operation-spec.json').read_bytes())['operations']
    checks=[]
    for row in batch['sources']:
        name=row['source']; authority=blob(BASE,name); prior=blob(PRIOR,name)
        isolated=replay(authority,[o for o in operations if o['source']==name])
        cumulative=replay(prior,row['rebound_operations'])
        require(isolated==(candidate/'payload'/name).read_bytes(),'Payload replay mismatch')
        require(cumulative==(candidate/'cumulative-preview'/name).read_bytes(),'Cumulative preview replay mismatch')
        for original,post in ((authority,isolated),(prior,cumulative)):
            for pattern in (rb'\\label\{([^}]+)\}',rb'\\(?:ref|eqref|cite)\{([^}]+)\}',rb'\\(?:begin|end)\{([^}]+)\}'):
                require(Counter(re.findall(pattern,original))==Counter(re.findall(pattern,post)),'Reference/structure mismatch')
        checks.append({'source':name,'passed':True,'isolated':ident(isolated),'cumulative':ident(cumulative),'labels_refs_citations_environments_unchanged':True})
    write(candidate/'replay/source-replay.json',{'schema':'stacks-r51-independent-source-replay/v1','candidate_id':'stacks-errata-a04446e-r51',
        'passed':True,'checks':checks,'scope':'Separately executed source replay in the same primary AI task; no second AI or human reviewer claimed. Build and visual gates are separate.',
        'reviewer':'OpenAI Codex - GPT-6 Astra, Ultra effort','created_at_utc':now()})
    print(json.dumps({'action':'replay','passed':True,'sources':len(checks)}))

if __name__=='__main__':main()
