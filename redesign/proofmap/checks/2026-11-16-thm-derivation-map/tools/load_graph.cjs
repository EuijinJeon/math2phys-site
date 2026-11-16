// Compatibility loader for the existing check and table tools.
const fs=require('node:fs');
const path=require('node:path');
module.exports=function load(input){
  const file=input&&input.endsWith('.json')?path.resolve(input):path.resolve(__dirname,'../../../graphs/decor-thm.json');
  const {groups:GROUPS,nodes:N,edges:E,positions:POS,subgraphs:SUBGRAPHS}=JSON.parse(fs.readFileSync(file,'utf8'));
  return {GROUPS,N,E,POS,SUBGRAPHS};
};
