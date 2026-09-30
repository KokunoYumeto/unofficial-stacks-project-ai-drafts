"""Check Algebra source, immutable evidence, concurrent integration and publication."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import textwrap
try:
    from . import r58_successor as r
except ImportError:
    import r58_successor as r

ROOT=r.ROOT
PUBLIC='9629f0c7311926edf85b1c5ca045a1478becebcc'
LOCAL='db4ab5225904b2161697d7264148326b20edc21d'
MERGED='4a6a43a9e4535e1435e6449fffbb10e5c0019612'
BASE='4828ebac86db7ebf4211227cabe183b09f11c992'
CURRENT='validation/r58-successor-current.json'
RECONCILIATION='validation/r58-concurrent-integration-2026-09-30.json'
TRANSPORT='validation/r58-publication-transport.json'
RELEASE='validation/r58-publication-readback.json'
FOLLOWUP_PATHS={CURRENT,TRANSPORT,RELEASE,'tools/validate_r58_successor.py',
    'tests/test_r58_successor.py','.github/workflows/validate.yml'}
require=r.require

def objects(ref):
    result={}
    for row in r.git('ls-tree','-r','-z',ref).split(b'\0'):
        if not row:continue
        head,name=row.split(b'\t',1);mode,kind,oid=head.decode().split()
        require(kind=='blob','Unexpected tree object')
        result[name.decode()]=(mode,oid)
    return result

def same_except(a,b,allowed):
    changed={p for p in a.keys()|b.keys() if a.get(p)!=b.get(p)}
    require(changed<=set(allowed),'Unlisted change: '+str(sorted(changed-set(allowed))))
    require(all(p in b and b[p][0]=='100644' for p in changed),'Deletion or unexpected file mode')
    return changed

def registry_transport(base,local,public,current,transport):
    require(len(base['events'])==123 and local['events'][:123]==public['events'][:123]==base['events'],'Common lease prefix changed')
    require(len(local['events'])==125 and len(public['events'])==127,'Predecessor event counts changed')
    require(len(transport)==2,'Missing transport')
    expected=[]
    for i,row in enumerate(transport):
        require(row['original']==local['events'][123+i],'Original event changed')
        wanted={**row['original'],'event_id':f'lease-event-{128+i:06d}'}
        if i:wanted['supersedes_event_id']='lease-event-000128'
        require(row['transported']==wanted,'Transport changed non-identifier data')
        expected.append(wanted)
    require(current=={**public,'events':public['events']+expected},'Reconciled registry differs')

def validate(ref='HEAD',pre_publication=False):
    ref=r.git('rev-parse',ref).decode().strip()
    read=lambda n:r.blob(ref,n)
    doc=lambda n:json.loads(read(n))
    m,ids,ops,apparatus,prior,body,visible,frozen=r.evidence()
    r.frozen_files(ref,frozen)
    require(read('algebra.tex')==visible,'Current Algebra differs from reviewed build source')
    require((ROOT/'algebra.tex').read_bytes()==visible,'Working Algebra differs')
    admission=doc(r.ADMISSION);composition=doc(r.COMPOSITION)
    require(admission['passed'] and not admission['source_composed'] and admission['candidate_commit']==r.CANDIDATE,'Admission binding changed')
    require(composition['passed'] and composition['candidate_commit']==r.CANDIDATE
        and composition['manifest_sha256']==r.MANIFEST and composition['editorial_notice_operations']==apparatus,'Composition binding changed')
    require(composition['preimage']==r.identity(prior) and composition['bounded_body_postimage']==r.identity(body)
        and composition['visible_postimage']==r.identity(visible),'Composition source changed')
    current=doc(CURRENT);recon=doc(RECONCILIATION)
    require(current['candidate_commit']==r.CANDIDATE and current['manifest_sha256']==r.MANIFEST,'Current candidate changed')
    require(current['admission_commit']=='11d4d4273efbbeaade7d0f9ebdbec264964a7b49'
        and current['composition_commit']=='168ecc61211057f14ed5081155f99a83b32f70a0','Separate transition identity changed')
    require(read(r.ADMISSION)==r.blob(current['admission_commit'],r.ADMISSION)
        and read(r.COMPOSITION)==r.blob(current['composition_commit'],r.COMPOSITION),'Immutable transition changed')
    require(r.blob(current['admission_commit'],'algebra.tex')==prior,'Source changed before composition')
    require(r.blob(current['composition_commit'],'algebra.tex')==visible,'Wrong composition commit')
    require(read(RECONCILIATION)==r.blob(MERGED,RECONCILIATION),'Reconciliation receipt changed')
    require(r.sha(read(RECONCILIATION))==current['reconciliation']['sha256'],'Reconciliation hash changed')
    require(recon['local_predecessor']==LOCAL and recon['public_predecessor']==PUBLIC,'Predecessor identity changed')
    require(r.git('show','-s','--format=%P',MERGED).decode().split()==[LOCAL,PUBLIC],'Local merge parents changed')
    for row in recon['immutable_public_artifacts_preserved']:
        preserved=r.blob(MERGED,row['path'])
        require(r.identity(preserved)=={k:row[k] for k in ['bytes','sha256']},'Prior public artifact changed: '+row['path'])
        require(preserved==r.blob(PUBLIC,row['path']),'Prior public bytes changed')
        if row['path'] not in FOLLOWUP_PATHS:
            require(read(row['path'])==preserved,'Retained public artifact changed: '+row['path'])
    for row in recon['sources_preserved']:
        require(read(row['path'])==r.blob(row['from_commit'],row['path']),'Concurrent source changed')
    leases=lambda rev:json.loads(r.blob(rev,r.LEASES))
    registry_transport(leases(BASE),leases(LOCAL),leases(PUBLIC),doc(r.LEASES),recon['lease_event_transport'])
    public_overlays=json.loads(r.blob(PUBLIC,r.OVERLAYS))
    expected={**public_overlays,'registered_entries':public_overlays['registered_entries']+[admission['admission']]}
    require(doc(r.OVERLAYS)==expected,'Public overlay prefix or R58 entry changed')
    require(len(expected['registered_entries'])==61 and len({i for e in expected['registered_entries'] for i in e['stable_ids']})==2243,'Registry scope changed')
    require(admission['release_event']==recon['lease_event_transport'][1]['original'],'Original release event changed')

    # All other received work is held at the explicit reconciled snapshot. This
    # comparison covers every tracked path, including all earlier candidates.
    changed=same_except(objects(MERGED),objects(ref),FOLLOWUP_PATHS)
    if 'tools/validate_r58_successor.py' in objects(ref):
        old_dispatch=r.blob(MERGED,'.github/workflows/validate.yml').decode().replace('\r\n','\n')
        new_dispatch=read('.github/workflows/validate.yml').decode().replace('\r\n','\n')
        dispatch=('          if test -f tools/validate_r58_successor.py; then\n'
                  '            python tools/validate_r58_successor.py\n'
                  '            exit $?\n          fi\n')
        tests='          python -m unittest tests.test_r58_successor\n'
        require(new_dispatch.count(dispatch)==new_dispatch.count(tests)==1,'Missing R58 workflow dispatch')
        require(new_dispatch.replace(dispatch,'').replace(tests,'')==old_dispatch,'Earlier workflow checks changed')
    workflow=read('ai-integrated/.github/workflows/validate.yml').decode()
    code=textwrap.dedent(workflow.split("python - <<'PY'\n",1)[1].rsplit('\n          PY',1)[0])
    cwd=os.getcwd()
    try:
        os.chdir(ROOT/'ai-integrated');exec(compile(code,'r58-registry-contract','exec'),{'__name__':'__main__'})
    finally:os.chdir(cwd)
    downloads=doc('upstream-corrections/downloads.json')
    for row in downloads['files']:
        name='upstream-corrections/'+row['path']
        require(r.identity(read(name))=={k:row[k] for k in ['bytes','sha256']},'Export changed: '+name)
    exp=doc('upstream-corrections/manifest.json')
    require(exp['historical_registry_ids']==2201 and exp['included_effective_textual_units']==2199
        and len(exp['chapters'])==35 and not exp['contains_new_theorem_additions'],'Export scope changed')
    # Deterministic generators replay all correction patches and preserve their
    # separate boundary from the companion and the three Verdier insertions.
    for script in ['generate_changes_from_upstream.py','export_upstream_corrections.py']:
        subprocess.run([os.sys.executable,str(ROOT/'tools'/script),'--check'],cwd=ROOT,check=True)

    published_transport=False
    tree=objects(ref)
    if TRANSPORT in tree:
        t=doc(TRANSPORT)
        require(t['schema']=='stacks-r58-exact-tree-publication-transport/v1','Wrong transport schema')
        require(t['public_predecessor']==PUBLIC,'Public predecessor changed')
        dag=t['validated_dag']['commit'];linear=t['linear_content']['commit']
        dagtree=r.git('rev-parse',dag+'^{tree}').decode().strip()
        require(dagtree==t['validated_dag']['tree']==r.git('rev-parse',linear+'^{tree}').decode().strip(),'Public tree differs from validated tree')
        require(r.git('show','-s','--format=%P',linear).decode().split()==[PUBLIC],'Public content has wrong parent')
        require(r.git('rev-parse',t['validated_dag']['tag']+'^{commit}').decode().strip()==dag,'Validated DAG tag changed')
        r.git('merge-base','--is-ancestor',linear,ref)
        require(not r.git('rev-list','--min-parents=2',PUBLIC+'..'+ref).strip(),'Merge in public successor range')
        same_except(objects(dag),objects(ref),{TRANSPORT,RELEASE})
        require(current['status']=='READY_FOR_PUBLICATION','Local preparation incomplete')
        published_transport=True
    else:
        require(pre_publication,'Public transport not yet supplied')
        r.git('merge-base','--is-ancestor',MERGED,ref)
    return dict(status='R58_COMBINED_SUCCESSOR_PASS',candidate_files=len(frozen),units=560,operations=690,
        chapter_pages=484,companion_pages=667,overlays=61,unique_stable_ids=2243,effective_export_units=2199,
        chapter_patches=35,concurrent_public_artifacts_preserved=len(recon['immutable_public_artifacts_preserved']),
        publication_transport_checked=published_transport,publication_readback_claimed=False,
        followup_paths_checked=len(changed),scope='Exact current source, artifact closure, registry transport, retained predecessors and deterministic correction exports; no new mathematical or human review of inherited work.')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--ref',default='HEAD');p.add_argument('--pre-publication',action='store_true');a=p.parse_args()
    print(json.dumps(validate(a.ref,a.pre_publication)))
