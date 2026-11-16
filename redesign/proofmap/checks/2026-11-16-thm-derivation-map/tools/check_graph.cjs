// 구조 검사. 쓰임: node check_graph.cjs <지도.html> [목표 node id, 기본 THM]
const load=require('./load_graph.cjs');
const [,,html,goal='THM']=process.argv;
const {GROUPS,N,E,POS,SUBGRAPHS}=load(html);
const ids=new Set(N.map(n=>n.id)); let bad=0;
const err=m=>{bad++;console.log('오류  '+m)};
const warn=m=>console.log('경고  '+m);
// 1. id 중복
if(ids.size!==N.length) err('node id 중복');
// 2. 필수 칸
for(const n of N){
  for(const k of ['tag','t','f','src']) if(!n[k]) err(`${n.id}: ${k} 비어 있음`);
  if(n.g && !GROUPS[n.g]) err(`${n.id}: 없는 묶음 ${n.g}`);
  if(!POS[n.id]) err(`${n.id}: POS에 자리 없음`);
  if(typeof n.supplement!=='undefined' && typeof n.supplement!=='boolean') err(`${n.id}: supplement는 boolean`);
  if(/class=["']warn["']/.test(n.body||'') && n.supplement!==true) err(`${n.id}: 원문 밖 보충에 supplement: true 필요`);
}
for(const k in POS) if(!ids.has(k)) err(`POS의 ${k}: node 없음`);
// 3. edge 양끝
E.forEach((e,i)=>{for(const v of [e[0],e[1]]) if(!ids.has(v)) err(`edge ${i} ${e[0]}→${e[1]}: 없는 node ${v}`)});
// 4. 왼쪽→오른쪽 (보내는 열 < 받는 열)
E.forEach(e=>{if(POS[e[0]]&&POS[e[1]]&&POS[e[0]][1]>=POS[e[1]][1]) err(`${e[0]}→${e[1]}: 열이 오른쪽으로 가지 않음 (${POS[e[0]][1]}→${POS[e[1]][1]})`)});
// 5. 순환
const adj={};E.forEach(e=>(adj[e[0]]=adj[e[0]]||[]).push(e[1]));
const st={};const dfs=v=>{st[v]=1;for(const w of adj[v]||[]){if(st[w]===1){err('순환: '+v+'→'+w)}else if(!st[w])dfs(w)}st[v]=2};
ids.forEach(v=>{if(!st[v])dfs(v)});
// 6. 모든 node가 목표에 닿는가 (목표 뒤의 받는 곳은 예외)
const radj={};E.forEach(e=>(radj[e[1]]=radj[e[1]]||[]).push(e[0]));
const anc=new Set([goal]),q=[goal];while(q.length){const v=q.pop();for(const u of radj[v]||[]) if(!anc.has(u)){anc.add(u);q.push(u)}}
const after=new Set();(adj[goal]||[]).forEach(v=>after.add(v));
for(const n of N) if(!anc.has(n.id)&&!after.has(n.id)) warn(`${n.id}: ${goal}에 닿지 않음`);
// 7. 백슬래시 사고: R`` 대신 '...' 에 TeX를 쓰면 \t,\b,\f,\v 가 제어문자가 되고 \e,\l,\d 등은 사라진다
const ctl=/[\t\b\f\v]/;
const scan=(where,str)=>{if(typeof str!=='string')return;if(ctl.test(str))err(`${where}: 제어문자 (TeX 백슬래시가 이스케이프로 먹힘)`);
  const m=str.match(/\$[^$]*\$/g)||[];for(const x of m) if(/(^|[^\\a-zA-Z])(eta|le|delta|mathbb|mathcal|to|infty|sum|prod|kappa|mu|gamma|sigma)\b/.test(x.replace(/\\[a-zA-Z]+/g,''))) err(`${where}: 백슬래시 빠진 TeX 의심 ${x}`)};
for(const n of N) for(const k of ['tag','t','f','body']) scan(n.id+'.'+k,n[k]);
E.forEach((e,i)=>scan(`edge ${e[0]}→${e[1]}`,e[2]));
// 8. $ 짝
const odd=str=>typeof str==='string'&&((str.match(/(?<!\\)\$/g)||[]).length%2===1);
for(const n of N) for(const k of ['t','f','body']) if(odd(n[k])) err(`${n.id}.${k}: $ 짝이 맞지 않음`);
E.forEach(e=>{if(odd(e[2])) err(`edge ${e[0]}→${e[1]}: $ 짝이 맞지 않음`)});
// A nested graph is local to its parent. Its IDs and edges must be valid.
for(const [parent,g] of Object.entries(SUBGRAPHS||{})){
  if(!ids.has(parent)) err(`하위 그래프 ${parent}: 부모 node 없음`);
  if(!Array.isArray(g.nodes)||!Array.isArray(g.edges)) {err(`하위 그래프 ${parent}: nodes/edges 필요`);continue}
  const local=new Set(g.nodes.map(n=>n.id));
  if(local.size!==g.nodes.length) err(`하위 그래프 ${parent}: id 중복`);
  for(const n of g.nodes){
    if(!n.id||!n.t||!n.f||!n.src) err(`${parent}/${n.id}: 필수 칸 누락`);
    if(/class=["']warn["']/.test(n.body||'')&&n.supplement!==true) err(`${parent}/${n.id}: supplement: true 필요`);
    for(const k of ['t','f','body']) {scan(`${parent}/${n.id}.${k}`,n[k]);if(odd(n[k]))err(`${parent}/${n.id}.${k}: $ 짝`)}
  }
  for(const e of g.edges) if(!local.has(e[0])||!local.has(e[1])) err(`${parent}: 하위 edge의 node 없음`);
}
console.log(`node ${N.length}, edge ${E.length}, key edge ${E.filter(e=>e[3]==='key').length}, ${goal}의 조상 ${anc.size-1}`);
console.log(bad?`오류 ${bad}`:'오류 0');
process.exit(bad?1:0);
