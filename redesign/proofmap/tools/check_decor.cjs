// JSON syntax is checked by JSON.parse in load_graph; structural checks follow.
const path=require('node:path');
const check=path.resolve(__dirname,'../checks/2026-11-16-thm-derivation-map/tools/check_graph.cjs');
process.argv[2]=path.resolve(__dirname,'../graphs/decor-thm.json');
require(check);
