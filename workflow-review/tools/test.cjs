const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {validate}=require('./check.cjs');
const baseline=JSON.parse(fs.readFileSync(path.join(__dirname,'../data/review.json'),'utf8'));
assert.deepEqual(validate(baseline),[]);
const tests=[
 ['보고를 검증 완료로 승격',d=>d.graphs[0].nodes[0].status='verified',/직접 증거 없음/],
 ['상위 복귀 대상 불일치',d=>d.graphs[1].parent.node='MISSING',/왕복 연결 오류/],
 ['다른 실행 맥락 연결',d=>d.graphs[1].case='update-procedure',/왕복 연결 오류/],
 ['원문 발췌 변경',d=>d.evidence.scope.excerpt='잘못된 근거',/발췌 불일치/],
 ['없는 연결 대상',d=>d.graphs[0].edges[0].target='MISSING',/없는 edge 끝/],
 ['원문 버전 미고정',d=>d.documents.procedure.revision='main',/버전 미고정/],
];
for(const [name,mutate,pattern] of tests){const d=structuredClone(baseline);mutate(d);assert.match(validate(d).join('\n'),pattern,name);}
console.log(`근거·왕복 링크·버전 검증: 정상 사례 및 결함 ${tests.length}종 통과`);
