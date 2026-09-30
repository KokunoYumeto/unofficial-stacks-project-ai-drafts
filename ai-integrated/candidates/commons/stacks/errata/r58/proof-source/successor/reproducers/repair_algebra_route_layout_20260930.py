"""Remove the observed enumitem/class conflict from the editorial route index."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

C=Path(__file__).resolve().parent
S=C/'ALGEBRA_CONTEXTUAL_COMPANION_20260929'
H='revision-history/before-route-layout-compatibility'
sha=lambda b:hashlib.sha256(b).hexdigest().upper()
dump=lambda v:(json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
assert not (S/H).exists()
old_m=(S/'MANIFEST.json').read_bytes();m=json.loads(old_m)
assert sha(old_m)=='3168E57C2D1F1C24D00E82396527FC793E014B20164C642BD07F84735B638F04'
for row in m['files']:assert sha((S/row['file']).read_bytes())==row['sha256'],row['file']
old_master=(S/'algebra-editorial.tex').read_bytes()
old_definition=br'''\usepackage{enumitem}
\newlist{AlgebraSourceRoutes}{description}{1}
\setlist[AlgebraSourceRoutes]{style=nextline,leftmargin=1.5em,font=\normalfont\bfseries}'''
new_definition=br'''% The source index uses direct paragraphs to remain compatible with the class.
\newenvironment{AlgebraSourceRoutes}{\par\begingroup\parindent=0pt\relax}{\par\endgroup}
\newcommand{\AlgebraSourceRoute}[1]{\par\smallskip\noindent\textbf{#1}\par\nobreak\noindent}'''
assert old_master.count(old_definition)==1
new_master=old_master.replace(old_definition,new_definition)
assert new_master.replace(new_definition,old_definition)==old_master
old_routing=(S/'source-routing.tex').read_bytes()
items=re.findall(rb'\\item\[([^\]\r\n]+)\]',old_routing)
assert len(items)==1262 and len(set(items))==1246 and all(x.startswith(b'ALGEBRA-RECON-') for x in items)
new_routing=re.sub(rb'\\item\[([^\]\r\n]+)\]',lambda x:br'\AlgebraSourceRoute{'+x[1]+b'}',old_routing)
assert re.sub(rb'\\AlgebraSourceRoute\{([^}\r\n]+)\}',lambda x:br'\item['+x[1]+b']',new_routing)==old_routing
assert br'\item[' not in new_routing
receipt=dict(id='RENDER-TEX-009',recorded_at_utc=datetime.now(timezone.utc).isoformat(),
 failed_build='../ALGEBRA_PORTABLE_BUILD_20260929/attempt-12/BUILD_RECEIPT.json',
 error='Argument of enit@postlabel@i has an extra closing brace at the first source-index item.',
 correction='Replace the package-dependent description clone with a grouped paragraph environment and explicit route-label command.',
 route_occurrences=len(items),unique_route_ids=len(set(items)),source_groups=155,exact_routing_inverse=True,exact_master_inverse=True,
 identifiers_labels_links_and_mathematics_unchanged=True,enumitem_dependency_removed=True,
 master_before_sha256=sha(old_master),master_after_sha256=sha(new_master),
 routing_before_sha256=sha(old_routing),routing_after_sha256=sha(new_routing),build_verified=False)
old_ledger=(S/'TYPESETTING_CORRECTIONS.json').read_bytes();ledger=json.loads(old_ledger)
ledger['route_layout_compatibility']=receipt
files={H+'/MANIFEST.json':old_m,H+'/algebra-editorial.tex':old_master,
 H+'/source-routing.tex':old_routing,H+'/TYPESETTING_CORRECTIONS.json':old_ledger,
 'algebra-editorial.tex':new_master,'source-routing.tex':new_routing,
 'ROUTE_LAYOUT_COMPATIBILITY.json':dump(receipt),'TYPESETTING_CORRECTIONS.json':dump(ledger),
 'reproducers/'+Path(__file__).name:Path(__file__).read_bytes()}
m['typesetting_corrections'].update(sha256=sha(files['TYPESETTING_CORRECTIONS.json']),route_layout_compatibility='ROUTE_LAYOUT_COMPATIBILITY.json')
m['revised_at_utc']=receipt['recorded_at_utc']
index={r['file']:r for r in m['files']}
for name,raw in files.items():index[name]=dict(file=name,bytes=len(raw),sha256=sha(raw))
m['files']=sorted(index.values(),key=lambda r:r['file'])
for name,raw in files.items():
 p=S/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
(S/'MANIFEST.json').write_bytes(dump(m))
print(json.dumps(dict(result='PASS_ROUTE_LAYOUT_COMPATIBILITY_REPAIR',route_count=len(items),manifest_sha256=sha(dump(m)),build_verified=False)))
