// node redesign/proofmap/tools/show_node.cjs T_SIDES
const fs=require('node:fs');
const path=require('node:path');
const root=path.resolve(__dirname,'..');
const g=JSON.parse(fs.readFileSync(path.join(root,'graphs/decor-thm.json'),'utf8'));
const query=process.argv.slice(2).join(' ');
if(!query){console.error('사용법: node redesign/proofmap/tools/show_node.cjs NODE_ID');process.exit(2)}
let parent=null;
let n=g.nodes.find(n=>n.id===query);
let edges=g.edges;
if(!n) for(const [id,sub] of Object.entries(g.subgraphs||{})){
  const hit=sub.nodes.find(n=>n.id===query||`${id}/${n.id}`===query);
  if(hit){n=hit;parent=id;edges=sub.edges;break}
}
if(!n){
  const matches=g.nodes.filter(n=>[n.tag,n.t].some(x=>x&&x.includes(query)));
  console.error('node를 찾지 못했다.'+(matches.length?' 후보: '+matches.map(n=>n.id+' ('+n.t+')').join(', '):''));process.exit(1)
}
const showEdge=(e,other)=>`${other} ${e[2]||''} ${e[3]||''}`.trim();
console.log(`ID: ${parent?parent+'/':''}${n.id}\n제목: ${n.t}\n표지: ${n.tag||''}\n진술: ${n.f}\n설명: ${n.body||'(없음)'}\n원문 밖 보충: ${!!n.supplement}\n원문 위치: ${n.src}`);
console.log('받는 edge:\n'+(edges.filter(e=>e[1]===n.id).map(e=>showEdge(e,e[0]+' →')).join('\n')||'(없음)'));
console.log('보내는 edge:\n'+(edges.filter(e=>e[0]===n.id).map(e=>showEdge(e,'→ '+e[1])).join('\n')||'(없음)'));
if(g.subgraphs?.[n.id])console.log('하위 node: '+g.subgraphs[n.id].nodes.map(x=>x.id).join(', '));
const sourceDir=path.resolve(root,'../source/sections');
const refs=[...n.src.matchAll(/([\w-]+\.tex)(?:\s+(\d+)(?:[–-](\d*))?)?/g)];
for(const m of refs){
  const file=path.join(sourceDir,m[1]);
  if(!fs.existsSync(file)){console.log(`\n${m[1]}: 파일 없음`);continue}
  const lines=fs.readFileSync(file,'utf8').split(/\r?\n/);
  if(!m[2]){console.log(`\n${m[1]}: 행 지정 없음`);continue}
  const from=Number(m[2]),to=Math.min(Number(m[3]||from+12),from+80,lines.length);
  console.log(`\n${m[1]} ${from}–${to}${m[3]&&Number(m[3])>to?' (나머지 생략)':''}:`);
  for(let i=from;i<=to;i++)console.log(`${i}: ${lines[i-1]}`);
}
