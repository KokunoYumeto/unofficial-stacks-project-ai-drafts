"""Use the available letter-page width and reversible source-identifier wrapping."""
import hashlib
import importlib.util
import json
import re
from datetime import datetime, timezone
from pathlib import Path

C=Path(__file__).resolve().parent
S=C/'ALGEBRA_CONTEXTUAL_COMPANION_20260929'
H='revision-history/before-reading-width'
BREAK=r'\AlgebraIdentifierBreak{}'
sha=lambda b:hashlib.sha256(b).hexdigest().upper()
dump=lambda v:(json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
spec=importlib.util.spec_from_file_location('retained_layout',C/'repair_algebra_companion_layout_20260930.py')
layout=importlib.util.module_from_spec(spec);spec.loader.exec_module(layout)

def wrap_identifiers(s):
    assert BREAK not in s
    protected=layout.protected(s)
    pattern=(r'(?<![A-Za-z0-9-])(?:lemma|proposition|theorem|definition|remark|example|equation|section)-[A-Za-z0-9-]+'
             r'|(?<![A-Za-z0-9-])(?:MC-STK-ERR|ALGEBRA-RECON|PUBUNIT|OCC)-[A-Za-z0-9-]+'
             r'|(?<![A-Za-z0-9-])[a-z][a-z-]*\.tex:\d+(?:(?:--|–)\d+)?(?:,\d+(?:(?:--|–)\d+)?)*')
    changes=[]
    for m in re.finditer(pattern,s):
        if len(m[0])<14 or any(a<m.end() and m.start()<b for a,b in protected):continue
        units=re.findall(r'\\[_#%]|--|.',m[0]);pieces=[];run=0
        for i,u in enumerate(units):
            pieces.append(u);run+=1
            if i<len(units)-1 and (u in ['-',':',',','.','–','--'] or run>=12):
                pieces.append(BREAK);run=0
        replacement=''.join(pieces)
        assert replacement.replace(BREAK,'')==m[0]
        changes.append(dict(start=m.start(),end=m.end(),source_line=s.count('\n',0,m.start())+1,
                            original=m[0],replacement=replacement))
    t=s
    for change in reversed(changes):t=t[:change['start']]+change['replacement']+t[change['end']:]
    assert t.replace(BREAK,'')==s
    return t,changes

def main():
    assert not (S/H).exists()
    old_m=(S/'MANIFEST.json').read_bytes();m=json.loads(old_m)
    assert sha(old_m)=='2B6415E10F494007E8A5A88B15DB3BD318CD69E9838DBE3CBEE16F0DF2BC89DD'
    for row in m['files']:assert sha((S/row['file']).read_bytes())==row['sha256'],row['file']
    files={H+'/MANIFEST.json':old_m};records=[]
    names=sorted({r['tex'] for r in m['proof_notes']} | {'contextual-arguments.tex'} |
       {r['file'] for r in m['files'] if re.fullmatch(r'contexts/ALGEBRA-CONTEXT-\d+\.tex',r['file'])})
    for name in names:
        old=(S/name).read_bytes();new,changes=wrap_identifiers(old.decode())
        if not changes:continue
        files[H+'/'+name]=old;files[name]=new.encode()
        records.append(dict(file=name,before_sha256=sha(old),after_sha256=sha(new.encode()),
                            changes=changes,exact_inverse=True,math_and_link_parameters_unchanged=True))
    old_master=(S/'algebra-editorial.tex').read_bytes()
    marker=b'\\begin{document}\n'
    assert old_master.count(marker)==1
    settings=br'''% The editorial companion uses one-inch side margins on its letter-size pages.
% The original chapter and every mathematical formula retain their exact source.
\setlength{\textwidth}{6.5in}
\setlength{\oddsidemargin}{0pt}
\setlength{\evensidemargin}{0pt}
\newcommand{\AlgebraIdentifierBreak}{\allowbreak}
% Keep natural paragraph spacing; any shortfall stays at the bottom of the page.
\raggedbottom
'''
    new_master=old_master.replace(marker,settings+marker)
    assert new_master.replace(settings,b'')==old_master
    files[H+'/algebra-editorial.tex']=old_master;files['algebra-editorial.tex']=new_master
    receipt=dict(id='RENDER-TEX-010',recorded_at_utc=datetime.now(timezone.utc).isoformat(),
        preceding_build='../ALGEBRA_PORTABLE_BUILD_20260929/attempt-14/BUILD_RECEIPT.json',
        actual_visual_evidence='../ALGEBRA_COMPANION_LAYOUT_REVIEW_20260930/VISUAL_REVIEW_PARTIAL.json',
        decision='The five-inch text block left one-and-three-quarter-inch side margins. A six-and-a-half-inch block gives one-inch margins on the same letter page, provides space for the original full displays and enlarges both retained diagrams. Identifier wrapping is reversible. Natural paragraph spacing places remaining vertical space at the bottom of the page.',
        previous_text_width_points=360,new_text_width='6.5in',side_margins='1in',paper_size_unchanged=True,
        mathematical_formulas_byte_identical=True,inline_math_byte_identical=True,
        source_chapter_unchanged=True,source_routing_records_unchanged=True,
        labels_and_link_destinations_unchanged=True,original_markdown_unchanged=True,
        identifier_changes=records,wrapped_identifiers=sum(len(r['changes']) for r in records),
        exact_identifier_inverse='Remove only AlgebraIdentifierBreak empty-group commands.',
        master_before_sha256=sha(old_master),master_after_sha256=sha(new_master),exact_master_inverse=True,
        figure_bytes_unchanged=True,figure_aspect_ratios_unchanged=True,
        diagnostic_thresholds_unchanged=True,diagnostics_suppressed=False,
        workflow_adjustment='The previous local plan proposed breaking mathematical displays. The wider standard text block is tried first while preserving every display byte. If measured overflow remains, repair that exact displayed layout next.',
        complete_build=False,visual_acceptance=False)
    old_ledger=(S/'TYPESETTING_CORRECTIONS.json').read_bytes();ledger=json.loads(old_ledger)
    ledger['reading_width_repair']={k:v for k,v in receipt.items() if k!='identifier_changes'}
    ledger['reading_width_repair']['full_receipt']='READING_WIDTH_REPAIR.json'
    files[H+'/TYPESETTING_CORRECTIONS.json']=old_ledger
    files['TYPESETTING_CORRECTIONS.json']=dump(ledger);files['READING_WIDTH_REPAIR.json']=dump(receipt)
    files['reproducers/'+Path(__file__).name]=Path(__file__).read_bytes()
    # Retain the exact helper needed to reproduce the protected-math scan.
    helper='reproducers/repair_algebra_companion_layout_20260930.py'
    assert (S/helper).read_bytes()==(C/'repair_algebra_companion_layout_20260930.py').read_bytes()
    for row in m['proof_notes']:
        if row['tex'] in files:
            row['before_identifier_wrapping_tex_sha256']=row['tex_sha256']
            row['tex_sha256']=sha(files[row['tex']]);row['identifier_wrapping_inverse_exact']=True
            row['namespace_inverse_recovers_exact_initial_tex']=False
            row['namespace_inverse_note']='Undo the recorded metadata and identifier wrapping and earlier explicit conversion repairs before comparison with the retained initial conversion.'
    for row in m['source_contexts']:
        name='contexts/'+row['id']+'.tex'
        if name in files:
            row['before_identifier_wrapping_typeset_sha256']=row['typeset_context_sha256']
            row['typeset_context_sha256']=sha(files[name])
    m['typesetting_corrections'].update(sha256=sha(files['TYPESETTING_CORRECTIONS.json']),
                                      reading_width_repair='READING_WIDTH_REPAIR.json')
    m['revised_at_utc']=receipt['recorded_at_utc']
    index={r['file']:r for r in m['files']}
    for name,raw in files.items():index[name]=dict(file=name,bytes=len(raw),sha256=sha(raw))
    m['files']=sorted(index.values(),key=lambda r:r['file'])
    for name,raw in files.items():
        p=S/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
    (S/'MANIFEST.json').write_bytes(dump(m))
    print(json.dumps(dict(result='PASS_EXACT_FORMULA_READING_LAYOUT_REPAIR',
        wrapped_identifiers=receipt['wrapped_identifiers'],changed_identifier_files=len(records),
        manifest_sha256=sha(dump(m)),mathematical_formulas_changed=False,build_verified=False)))

if __name__=='__main__':main()
