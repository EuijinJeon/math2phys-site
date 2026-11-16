// 지도 HTML에서 GROUPS·N·E·POS를 꺼낸다. 브라우저 없이 node만으로.
// 쓰임: const {GROUPS,N,E,POS}=require('./load_graph.cjs')(htmlPath)
const fs=require('fs');
module.exports=function load(htmlPath){
  const s=fs.readFileSync(htmlPath,'utf8');
  const cut=(a,b)=>{const i=s.indexOf(a),j=s.indexOf(b,i);if(i<0||j<0)throw new Error('표지 없음: '+a+' / '+b);return s.slice(i,j)};
  const data=cut('const R=String.raw;','const byId=');
  const pos=cut('const POS={','const COLGAP=');
  return new Function(data+'\n'+pos+'\nreturn {GROUPS,N,E,POS};')();
};
