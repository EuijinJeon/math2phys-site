'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),os=require('node:os');
const r=require('./record.cjs'),{pilot}=require('./pilot.cjs'),{project,render}=require('./review.cjs');
const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'graph-harness-'));let count=0;
function test(name,fn){fn();count++;console.log('OK '+name);}
try{const [a,b]=pilot(path.join(tmp,'pilot'));test('생성·수정 기록과 실제 실패 반환 보존',()=>{for(const d of [a,b])assert.deepEqual(r.validate(d),{errors:[],warnings:[]});assert(r.events(b).some(e=>e.type==='tool.finished'&&e.payload.exit_code===1));assert(r.events(b).some(e=>e.type==='step.finished'&&e.payload.id==='CHECK_OK'&&e.payload.status==='completed'));});
 test('변경 전후 스냅샷과 대상 ID 추적',()=>{const bad=r.events(b).find(e=>e.type==='tool.finished'&&e.payload.step==='EDIT_BAD');assert.notEqual(bad.payload.after[0].sha256,r.events(b).find(e=>e.type==='tool.started'&&e.payload.step==='EDIT_BAD').payload.before[0].sha256);assert(project(b).nodes.find(n=>n.id==='EDIT_FIX').affected.includes('BC'));});
 test('선은 출력 참조에서 생성',()=>{const p=project(a);assert(p.edges.some(e=>e.source==='DESIGN'&&e.target==='EDIT'&&e.output_id==='plan'));});
 test('정정은 원래 event를 덮어쓰지 않음, HTML escape',()=>{const before=fs.readFileSync(path.join(a,'events.jsonl'),'utf8');r.annotate(a,{target:'e1',text:'<script>alert(1)</script>'});assert(fs.readFileSync(path.join(a,'events.jsonl'),'utf8').startsWith(before));const html=fs.readFileSync(render(a),'utf8');assert(html.includes('&lt;script&gt;'));assert(!html.includes('<script>alert'));});
 function copy(name){const d=path.join(tmp,name);fs.cpSync(b,d,{recursive:true});return d;}
 test('저장된 반환 변조 탐지',()=>{const d=copy('corrupt');const out=r.events(d).find(e=>e.type==='tool.finished').payload.stdout;fs.appendFileSync(path.join(d,out.path),'changed');assert(r.validate(d).errors.includes('artifact 내용 변경'));});
 test('사건 삭제·재정렬 탐지',()=>{const d=copy('chain');const es=r.events(d);es.splice(2,1);fs.writeFileSync(path.join(d,'events.jsonl'),es.map(JSON.stringify).join('\n')+'\n');assert(r.validate(d).errors.length);});
 const c=path.join(tmp,'incomplete');r.init(c,{id:'incomplete',request:'검사',mode:'create',cwd:tmp});
 test('없는 출력 참조 거부',()=>assert.throws(()=>r.start(c,{id:'X',title:'x',purpose:'x',done_when:'x',inputs:[{label:'x',from:{step:'MISSING',output:'x'}}]}),/존재하지/));
 r.start(c,{id:'S',title:'오류',purpose:'실패 보존',done_when:'실패 확인',inputs:[]});const result=r.execute(c,{step:'S',argv:[process.execPath,'-e','process.stderr.write("bad");process.exit(2)']});
 test('실패 호출을 완료로 승격 거부',()=>assert.throws(()=>r.finish(c,{id:'S',status:'completed',summary:'거짓 성공',outputs:[],evidence:[result.id],affected:[]}),/실패한/));
 test('미종료 단계 경고와 run 종료 거부',()=>{assert(r.validate(c).warnings.length);assert.throws(()=>r.close(c,{summary:'x',delivery:{published:false}}),/미종료/);});
 test('기존 run 덮어쓰기 거부',()=>assert.throws(()=>r.init(a,{id:'x',request:'x',mode:'create',cwd:tmp})));
 test('종료 뒤 실행 추가 거부',()=>assert.throws(()=>r.start(a,{id:'LATE',title:'x',purpose:'x',done_when:'x',inputs:[]}),/종료한 run/));
 test('동시 writer 거부',()=>{fs.writeFileSync(path.join(c,'.writer.lock'),'');assert.throws(()=>r.execute(c,{step:'S',argv:[process.execPath,'-v']}),/EEXIST/);fs.unlinkSync(path.join(c,'.writer.lock'));});
 console.log(`${count}개 검사 통과`);
}finally{fs.rmSync(tmp,{recursive:true,force:true});}
