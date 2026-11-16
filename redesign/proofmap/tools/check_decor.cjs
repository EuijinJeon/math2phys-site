// JSON syntax is checked by JSON.parse in load_graph; structural checks follow.
const path=require('node:path');
const fs=require('node:fs');
const root=path.resolve(__dirname,'..');
for(const name of fs.readdirSync(path.join(root,'graphs')).filter(x=>x.endsWith('.json')&&x!=='decor-thm.json')){
  const fine=JSON.parse(fs.readFileSync(path.join(root,'graphs',name),'utf8'));
  const back=fine.meta?.parent?.href;
  const backUrl=back&&new URL(back,'https://example.test/');
  const parentId=backUrl?.hash.match(/^#node=([^&]+)$/)?.[1];
  const parentName=backUrl?.pathname.split('/').pop()?.replace(/-derivation\.html$/,'');
  const parentFile=parentName&&path.join(root,'graphs',parentName+'.json');
  const parentGraph=parentFile&&fs.existsSync(parentFile)&&JSON.parse(fs.readFileSync(parentFile,'utf8'));
  const parent=parentGraph?.nodes.find(n=>n.id===parentId);
  const target=name.replace(/\.json$/, '-derivation.html');
  const forward=parent?.links?.some(l=>new URL(l.href,'https://example.test/').pathname.endsWith('/'+target));
  if(!parent||!forward||backUrl.pathname!=='/'+parentName+'-derivation.html'){
    console.error(`오류: ${name} 왕복 링크가 맞지 않음`);process.exit(1);
  }
}
const check=path.resolve(__dirname,'../checks/2026-11-16-thm-derivation-map/tools/check_graph.cjs');
process.argv[2]=path.resolve(__dirname,'../graphs/decor-thm.json');
require(check);
