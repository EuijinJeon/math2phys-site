const fs = require('node:fs');
const path = require('node:path');
function validate(data) {
  const errors=[];
  const fail=message=>errors.push(message);
  if(data.schema!=='workflow-review/0.1') fail('지원하지 않는 schema');
  const graphs=new Map();
  for(const g of data.graphs){if(graphs.has(g.id))fail('중복 graph: '+g.id);graphs.set(g.id,g);}
  const cases=new Map(data.cases.map(c=>[c.id,c]));
  for(const c of data.cases) if(!graphs.has(c.root)||graphs.get(c.root).case!==c.id)fail('잘못된 case root: '+c.id);
  for(const [id,e] of Object.entries(data.evidence)){
    const d=data.documents[e.document];
    if(!d){fail('없는 원문: '+id);continue;}
    if(!/^[a-f0-9]{40}$/.test(d.revision))fail('원문 버전 미고정: '+id);
    const lines=d.text.split('\n');
    if(e.lines[0]<1||e.lines[1]<e.lines[0]||e.lines[1]>lines.length)fail('잘못된 원문 범위: '+id);
    if(lines.slice(e.lines[0]-1,e.lines[1]).join('\n')!==e.excerpt)fail('원문 발췌 불일치: '+id);
    if(!['report','specification','tool_result','artifact'].includes(e.kind))fail('근거 유형 오류: '+id);
  }
  for(const g of data.graphs){
    const nodes=new Map();const positions=new Set();
    if(!cases.has(g.case))fail('없는 case: '+g.id);
    for(const n of g.nodes){
      const label=g.id+'/'+n.id;
      if(nodes.has(n.id))fail('중복 node: '+label);nodes.set(n.id,n);
      for(const key of ['title','summary','body'])if(!n[key])fail('필수 설명 누락: '+label+'/'+key);
      if(!Array.isArray(n.inputs)||!Array.isArray(n.outputs))fail('입출력 누락: '+label);
      if(!Array.isArray(n.position)||n.position.length!==2||n.position.some(x=>!Number.isInteger(x)||x<0))fail('위치 오류: '+label);
      if(positions.has(String(n.position)))fail('겹치는 위치: '+label);positions.add(String(n.position));
      if(!['reported','not_done','unknown','specified','observed','verified'].includes(n.status))fail('상태 오류: '+label);
      if(!n.evidence?.length)fail('근거 누락: '+label);
      for(const id of n.evidence||[])if(!data.evidence[id])fail('없는 근거: '+label+'/'+id);
      const kinds=(n.evidence||[]).map(id=>data.evidence[id]?.kind);
      if(n.status==='verified'&&!kinds.includes('artifact')&&!kinds.includes('tool_result'))fail('결과 확인됨에 직접 증거 없음: '+label);
      if(n.status==='observed'&&!kinds.includes('tool_result'))fail('실행 기록 있음에 실행 근거 없음: '+label);
      if(n.status==='specified'&&!kinds.includes('specification'))fail('절차 명시에 운영 규칙 없음: '+label);
      if(['reported','not_done'].includes(n.status)&&!kinds.includes('report'))fail('보고 상태에 보고 근거 없음: '+label);
      if(n.detail){const child=graphs.get(n.detail);if(!child||child.case!==g.case||child.parent?.graph!==g.id||child.parent?.node!==n.id)fail('세부 지도 왕복 연결 오류: '+label);}
    }
    for(const e of g.edges){
      if(!nodes.has(e.source)||!nodes.has(e.target))fail('없는 edge 끝: '+g.id);
      if(!['sequence','data','note'].includes(e.kind))fail('edge 유형 오류: '+g.id);
      if(!e.label)fail('edge 설명 누락: '+g.id);
    }
    if(g.parent){const p=graphs.get(g.parent.graph);if(!p||p.case!==g.case||!p.nodes.some(n=>n.id===g.parent.node&&n.detail===g.id))fail('상위 지도 왕복 연결 오류: '+g.id);}
    const seen=new Set();let cursor=g;
    while(cursor){if(seen.has(cursor.id)){fail('계층 순환: '+g.id);break;}seen.add(cursor.id);cursor=graphs.get(cursor.parent?.graph);}
  }
  return errors;
}
module.exports={validate};
if(require.main===module){const data=JSON.parse(fs.readFileSync(path.join(__dirname,'../data/review.json'),'utf8'));const errors=validate(data);if(errors.length){console.error(errors.join('\n'));process.exit(1);}console.log(`업무 검토 지도: ${data.graphs.length}개 그래프 · ${data.graphs.reduce((n,g)=>n+g.nodes.length,0)}개 노드 · 오류 0`);}
