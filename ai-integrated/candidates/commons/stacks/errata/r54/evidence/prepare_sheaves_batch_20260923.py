"""Prepare the hash-bound single-source candidate input; no canonical IDs or edits."""
import argparse
from collections import Counter
import json

import sheaves_intake_20260923 as source
from verify_categories_intake_review_20260922 import replace_bound, require
from verify_sets_intake_review_20260922 import git
import reconcile_correction_occurrences_20260922 as intake


def identity(raw):return {'bytes':len(raw),'sha256':intake.digest(raw)}


def main():
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args()
    registry=(source.ROOT/'ai-integrated/registry/overlays.json').read_bytes()
    require(registry==git('show',source.CURRENT+':ai-integrated/registry/overlays.json'),'Registry drift')
    units,sources,evidence,reports=[],[],[],{}
    for name,expected in [('sheaves.tex',146)]:
        stem=name.removesuffix('.tex').upper()
        review_path=source.HERE/f'{stem}_INTAKE_REVIEW_20260923.json'
        replay_path=source.HERE/f'{stem}_INTAKE_REVIEW_REPLAY_20260923.json'
        review_raw,replay_raw=review_path.read_bytes(),replay_path.read_bytes()
        review,replay=json.loads(review_raw),json.loads(replay_raw)
        require(replay['review']['sha256']==intake.digest(review_raw),'Stale replay')
        require(replay['occurrence_coverage']['reviewed']==expected and replay['occurrence_coverage']['exactly_once'],
                'Incomplete occurrence closure')
        all_ops,rebound=[],[]
        for g in review['groups']:
            if not g['disposition'].startswith('accepted_missing_'):continue
            ops=[]
            for j,op in enumerate([o for o in replay['operations'] if o['review_id']==g['id']],1):
                bound={k:op[k] for k in ('line','old_text','replacement_text','start_byte',
                    'end_byte_exclusive','old_sha256','replacement_sha256')}
                bound['operation_id']=f'{g["id"]}-OP{j}'
                ops.append(bound)
                rebound.append({**bound,'start_byte':op['current_start_byte'],
                    'end_byte_exclusive':op['current_start_byte']+len(op['old_text'].encode()),
                    'cumulative_line':op['current_line']})
            all_ops.extend(ops)
            units.append({'id':g['id'],'source':name,'operations':ops,'producer_occurrences':g['occurrences'],
                'class':g['disposition'],'rationale':g['rationale'],'adverse_evidence':g['adverse_evidence'],
                'review_file':review_path.name,'discovery':g.get('discovery'),
                'related_existing_canonical_ids':g['canonical_ids']})
        authority=git('show',source.BASE+':'+name)
        current=git('show',source.CURRENT+':'+name)
        isolated,cumulative=replace_bound(authority,all_ops),replace_bound(current,rebound)
        require(identity(isolated)['sha256']==replay['git_replays'][0]['postimage_sha256'],'Isolated mismatch')
        require(identity(cumulative)['sha256']==replay['git_replays'][1]['postimage_sha256'],'Cumulative mismatch')
        sources.append({'source':name,'authority':identity(authority),'cumulative_preimage':identity(current),
            'prospective_isolated_postimage':identity(isolated),'prospective_cumulative_postimage':identity(cumulative),
            'operations':len(all_ops),'rebound_operations':rebound,'exact_preimages':True,
            'prior_corrections_preserved':True,'legacy_context_envelope_overlaps':
                [o for o in replay['operations'] if o['admitted_context_envelope_overlaps']]})
        for f in [review_path.name,replay_path.name,f'{stem}_PENDING_SOURCE_REPAIRS_20260923.patch',
                  f'{stem}_PENDING_CUMULATIVE_REPAIRS_20260923.patch']:
            evidence.append({'path':f,**identity((source.HERE/f).read_bytes())})
        reports[name]=dict(Counter(g['disposition'] for g in review['groups'] for _ in g['occurrences']))
    for f in ['SHEAVES_PRIOR_ADMITTED_UNITS_20260923.json','sheaves_intake_20260923.py','verify_sheaves_intake_review_20260923.py',
              'test_sheaves_intake_replay_20260923.py','prepare_sheaves_batch_20260923.py']:
        evidence.append({'path':f,**identity((source.HERE/f).read_bytes())})
    result={'schema':'stacks-next-correction-batch-input/v1','prepared_on':'2026-09-23',
        'authority_commit':source.BASE,'checked_public_main':source.CURRENT,'registry_sha256':intake.digest(registry),
        'units':units,'unit_count':len(units),'operation_count':sum(len(u['operations']) for u in units),
        'sources':sources,'evidence':evidence,'dependency_groups':[],
        'scope':'All 146 received Sheaves on Spaces reports adjudicated; 12 new proposed units / 16 operations: 11 copyedits and one clarification making an existing isomorphism and factorization explicit. Optional/rejected and already-composed reports remain in bound review evidence. No new theorem additions.',
        'registry_admission':False,'canonical_ids_allocated':False,'source_mutations':0,'build_claimed':False,
        'reviewer':'OpenAI Codex — GPT-6 Astra, Ultra effort','workers_used':False,
        'next_action':'Allocate the next available single-source errata candidate after live registry/ref checks; complete source closure, bounded comparative deterministic builds under the TeX mutex, visual QA, separate executable replay/admission/composition, fixes-only regeneration and public readback. Do not rerun finished source adjudication.'}
    require(result['unit_count']==12 and result['operation_count']==16,'Unexpected batch scope')
    raw=(json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode()
    target=source.HERE/'SHEAVES_CORRECTION_BATCH_INPUT_20260923.json'
    if a.check:require(target.read_bytes()==raw,'Non-deterministic batch')
    else:target.write_bytes(raw)
    print(json.dumps({'path':str(target),**identity(raw),'units':12,'operations':16,
        'physical_report_dispositions':reports},indent=2))


if __name__=='__main__':main()
