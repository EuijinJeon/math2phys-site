const fs=require('node:fs');const path=require('node:path');
const data=JSON.parse(fs.readFileSync(path.join(__dirname,'../data/review.json'),'utf8'));
const [graphId,nodeId]=process.argv.slice(2);const g=data.graphs.find(g=>g.id===graphId);const n=g?.nodes.find(n=>n.id===nodeId);
if(!n){console.error('사용법: node workflow-review/tools/show-node.cjs <graph-id> <node-id>');process.exit(1);}
console.log(JSON.stringify({version:data.version,case:g.case,graph:g.id,node:n,parent:g.parent,edges:g.edges.filter(e=>e.source===n.id||e.target===n.id),evidence:n.evidence.map(id=>({id,...data.evidence[id],source:data.documents[data.evidence[id].document].path,revision:data.documents[data.evidence[id].document].revision}))},null,2));
