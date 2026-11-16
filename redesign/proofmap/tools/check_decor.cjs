// JSON syntax is checked by JSON.parse in load_graph; structural checks follow.
const path=require('node:path');
const fs=require('node:fs');
const root=path.resolve(__dirname,'..');
const coarse=JSON.parse(fs.readFileSync(path.join(root,'graphs/decor-thm.json'),'utf8'));
const fine=JSON.parse(fs.readFileSync(path.join(root,'graphs/b-con.json'),'utf8'));
const link=coarse.nodes.find(n=>n.id==='B_CON')?.links?.find(l=>l.href==='b-con-derivation.html');
if(!link||fine.meta?.parent?.href!=='decor-thm-derivation.html#node=B_CON'){
  console.error('오류: B_CON 왕복 링크가 맞지 않음');process.exit(1);
}
const check=path.resolve(__dirname,'../checks/2026-11-16-thm-derivation-map/tools/check_graph.cjs');
process.argv[2]=path.resolve(__dirname,'../graphs/decor-thm.json');
require(check);
