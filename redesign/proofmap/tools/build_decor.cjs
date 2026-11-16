// JSON is the only authored graph data. Keep the viewer template fixed.
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const graph = JSON.parse(fs.readFileSync(path.join(root, 'graphs/decor-thm.json'), 'utf8'));
const template = fs.readFileSync(path.join(root, 'viewer/decor-thm-template.html'), 'utf8');
const marker = '/*__GRAPH_DATA__*/';
if (template.split(marker).length !== 2) throw Error('template marker must occur once');
const data = JSON.stringify(graph).replace(/</g, '\\u003c');
const output = template.replace(marker,
  `const R=String.raw;\nconst GRAPH=${data};\nconst {groups:GROUPS,nodes:N,edges:E,positions:POS,subgraphs:SUBGRAPHS}=GRAPH;`);
fs.writeFileSync(path.join(root, 'build/decor-thm-derivation.html'), output);
console.log('built decor-thm-derivation.html');
