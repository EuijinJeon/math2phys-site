// node·edge 표를 Markdown으로. 쓰임: node dump_table.cjs <지도.html> > NODES.md
const load=require('./load_graph.cjs');
const {GROUPS,N,E,POS}=load(process.argv[2]);
const strip=s=>(s||'').replace(/<br>/g,' ').replace(/<[^>]+>/g,'').replace(/\|/g,'\\|').replace(/\s+/g,' ').trim();
const out=[];
out.push('# node·edge 표 (생성물)','','`tools/dump_table.cjs` 가 지도 HTML에서 만든다. 직접 고치지 말고 HTML을 고친 뒤 다시 만든다.','');
out.push('## node','','| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |','|---|---|---|---|---|---|---|---|');
for(const n of N) out.push(`| ${n.id} | ${n.g?GROUPS[n.g].label:'(묶음 없음)'} | [${POS[n.id]}] | ${n.cls||'보통'} | ${strip(n.tag)} | ${strip(n.t)} | ${strip(n.f)} | ${n.src} |`);
out.push('','## edge','','| # | 보냄 | 받음 | 싣는 내용 | 종류 |','|---|---|---|---|---|');
E.forEach((e,i)=>out.push(`| ${i} | ${e[0]} | ${e[1]} | ${strip(e[2])||'(라벨 없음)'} | ${e[3]||'입력'} |`));
console.log(out.join('\n'));
