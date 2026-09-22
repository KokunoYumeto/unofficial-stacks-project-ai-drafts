/* Prepare a hash snapshot, then seal only an independently reviewed snapshot.
 * This tool never edits sources, Git state, registries or previous candidates.
 */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const root = __dirname;
const mode = process.argv[2];
const sha = b => crypto.createHash('sha256').update(b).digest('hex').toUpperCase();
const read = p => fs.readFileSync(path.join(root,p));
const json = p => JSON.parse(read(p));
const assert = (v,m) => {if(!v) throw Error(m);};
const write = (p,v) => {fs.mkdirSync(path.dirname(path.join(root,p)),{recursive:true});fs.writeFileSync(path.join(root,p),typeof v==='string'?v:JSON.stringify(v,null,2)+'\n',{flag:'wx'});};
const ref = p => {const b=read(p);return {path:p,bytes:b.length,sha256:sha(b)};};
function files(dir='') {return fs.readdirSync(path.join(root,dir),{withFileTypes:true}).flatMap(e=>{const p=dir?dir+'/'+e.name:e.name;return e.isDirectory()?(e.name==='__pycache__'?[]:files(p)):e.name.endsWith('.pyc')?[]:[p];}).sort();}
function sanitize(s) {return s.replace(/[A-Za-z]:\\\\Users\\\\[^\\"\r\n]+/g,'USERROOT').replace(/[A-Za-z]:\\Users\\[^\\"\r\n]+/g,'USERROOT').replace(/[A-Za-z]:\/Users\/[^/"\r\n]+/g,'USERROOT');}
const config=json('candidate.config.json');
assert(config.candidate_id==='stacks-errata-a04446e-r49','Wrong candidate');
const excluded = new Set(['candidate.manifest.json','replay/FINAL_STAGE.json','replay/FINAL_INDEPENDENT_REVIEW.json']);
if(mode==='prepare') {
  const auditRoot=path.resolve(process.argv[3]||'');
  const auditNames=['BUILD_INDEPENDENT_REVIEW.md','BUILD_INDEPENDENT_VERDICT.json','RECONSTRUCTED_BUILD_A_EXECUTION.json','audit_build.py'];
  for(const n of auditNames) {const p=path.join(auditRoot,n);assert(fs.statSync(p).isFile(),'Missing independent audit');write('authority/review/build/'+n,sanitize(fs.readFileSync(p,'utf8')));}
  const visual=json('replay/PAGE_COMPLETE_VISUAL_ADJUDICATION-derham.json');
  assert(visual.passed===true && !visual.blocking_findings.length,'Visual check failed');
  for(const r of [visual.pdf,visual.render_manifest]) {assert(JSON.stringify(ref(r.path))===JSON.stringify(r),'Visual identity drift');}
  const snapshot=files().filter(p=>!excluded.has(p)).map(ref);
  const body={schema:'stacks-errata-final-stage/v1',candidate_id:config.candidate_id,created_at_utc:new Date().toISOString(),expected_units:5,expected_operations:7,source_map:ref('source-map.jsonl'),build_receipt:ref('builds/build-receipt.json'),deterministic_replay:ref('builds/deterministic-replay.json'),visual_review:ref('replay/PAGE_COMPLETE_VISUAL_ADJUDICATION-derham.json'),snapshot_inventory:snapshot,limitations:visual.limitations,review_state:'awaiting_independent_machine_and_source_closure_check',registry_admission:false,cumulative_composition:false};
  write('replay/FINAL_STAGE.json',body);
  console.log(JSON.stringify({stage:'prepared',snapshot:ref('replay/FINAL_STAGE.json'),files:snapshot.length}));
} else if(mode==='seal') {
  const final=json('replay/FINAL_STAGE.json');
  const review=json('replay/FINAL_INDEPENDENT_REVIEW.json');
  assert(review.passed===true && review.candidate_id===config.candidate_id && review.final_stage_sha256===ref('replay/FINAL_STAGE.json').sha256,'Independent review not bound');
  const actual=files().filter(p=>!excluded.has(p));
  assert(JSON.stringify(actual)===JSON.stringify(final.snapshot_inventory.map(x=>x.path)),'Snapshot file set changed');
  for(const r of final.snapshot_inventory) assert(JSON.stringify(ref(r.path))===JSON.stringify(r),'Snapshot file changed: '+r.path);
  const core={stable_unit_manifest:'stable-units.json',source_map:'source-map.jsonl',decision_ledger:'decisions.jsonl',rejection_ledger:'rejections.jsonl',formula_diagram_inventory:'formula-diagram-inventory.json'};
  const corePaths=new Set(Object.values(core));
  const authorityPaths=files().filter(p=>p.startsWith('authority/')||p==='COPYING');
  const authoritySet=new Set(authorityPaths);
  const manifest={schema:'mathematics-commons-stacks-candidate-manifest/v1',candidate_id:config.candidate_id,lease_id:config.lease_id,namespace:config.namespace,writer_task:config.writer_task,upstream:{lock:'upstream/stacks.lock.json',commit:config.authority_commit,tree:config.authority_tree},source_authorities:authorityPaths.map(ref),source_closure:{enumerated:true,expected_units:config.accepted,manifested_units:config.accepted,complete:true},...Object.fromEntries(Object.entries(core).map(([k,p])=>[k,ref(p)])),builds:files().filter(p=>p!=='candidate.manifest.json'&&!corePaths.has(p)&&!authoritySet.has(p)).map(ref),rights_state:'GNU FDL 1.2 inherited for Stacks source and its modifications; upstream notices and COPYING retained. Independent unofficial AI-produced correction overlay; no upstream endorsement or certification.',review_state:'performed',independent_replay:'passed',unresolved_defects:visualLimitations(),stop_conditions:['Reject any source or operation preimage mismatch.','Reject hash or file-closure drift, failed deterministic checks or introduced formula/diagram damage.','Never replace expanded cumulative source wholesale with the pinned-relative payload; compose only the seven guarded operations.'],generated_at_utc:new Date().toISOString()};
  write('candidate.manifest.json',manifest);
  console.log(JSON.stringify({stage:'sealed',manifest:ref('candidate.manifest.json'),files:files().length,registry_admission:false}));
} else throw Error('Use prepare <independent-audit-folder> or seal');
function visualLimitations(){return json('replay/PAGE_COMPLETE_VISUAL_ADJUDICATION-derham.json').limitations;}
