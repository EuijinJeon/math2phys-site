'use strict';
const fs=require('node:fs');
const [cmd,file]=process.argv.slice(2);
if(cmd==='create')fs.writeFileSync(file,JSON.stringify({nodes:[{id:'A',input:'사용자 요청',output:'대상 ID'},{id:'B',input:'대상 ID',output:'원문 위치'},{id:'C',input:'원문 위치',output:'원문 텍스트'}],edges:[{id:'AB',source:'A',target:'B',label:'대상 ID'},{id:'BC',source:'B',target:'C',label:'원문 위치'}]},null,2)+'\n');
else {const g=JSON.parse(fs.readFileSync(file));if(cmd==='break')g.edges[1].target='MISSING';else if(cmd==='fix'){g.edges[1].target='C';g.edges[1].label='파일 경로와 행 범위';g.nodes[1].output='파일 경로와 행 범위';g.nodes[2].input='파일 경로와 행 범위';}else if(cmd==='check'){const ids=new Set(g.nodes.map(n=>n.id));const errors=g.edges.filter(e=>!ids.has(e.source)||!ids.has(e.target));if(errors.length){console.error('없는 edge 끝: '+errors.map(e=>e.id));process.exit(1);}console.log('구조 검사 통과: '+g.nodes.length+' nodes / '+g.edges.length+' edges');process.exit(0);}else throw Error('명령 오류');fs.writeFileSync(file,JSON.stringify(g,null,2)+'\n');}
console.log(cmd+' → '+file);
