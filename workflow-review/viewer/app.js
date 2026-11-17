'use strict';
const $ = id => document.getElementById(id);
const esc = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const labels = {reported:'수행 보고', specified:'절차에 명시', unknown:'확인 불가', not_done:'미수행 보고', mixed:'보고·미수행 혼재', observed:'실행 기록 있음', verified:'결과 확인됨'};
const graphs = Object.fromEntries(DATA.graphs.map(g => [g.id, g]));
const params = new URLSearchParams(location.search);
let currentCase = DATA.cases.find(c => c.id === params.get('case')) || DATA.cases[0];
let graph = graphs[params.get('graph')];
if (!graph || graph.case !== currentCase.id) graph = graphs[currentCase.root];
const byId = Object.fromEntries(graph.nodes.map(n => [n.id, n]));
let selected = null, scale = 1, tx = 0, ty = 0, width = 0, height = 0;
let toastTimer;
function status(node) {
  if (!node.detail) return node.status;
  const values = new Set(graphs[node.detail].nodes.map(status));
  return values.size === 1 && values.has(node.status) ? node.status : 'mixed';
}
function url(graphId, nodeId, caseId = currentCase.id) {
  const u = new URL(location.href);
  u.search = new URLSearchParams({case:caseId, graph:graphId, v:DATA.version}).toString();
  u.hash = nodeId ? 'node=' + encodeURIComponent(nodeId) : '';
  return u.href;
}
function badge(node) { const s = status(node); return `<span class="badge ${esc(s)}">${esc(labels[s])}</span>`; }
function sourceUrl(e) {
  const doc = DATA.documents[e.document];
  return `https://github.com/EuijinJeon/math2phys-site/blob/${doc.revision}/${doc.path}#L${e.lines[0]}-L${e.lines[1]}`;
}
function scaleLink(child, title) {
  return `<a class="scale-link" href="${esc(url(child.id))}">더 세밀한 지도 → ${esc(title)}<small>${child.nodes.length}개 단계 · 같은 검토 대상 유지</small></a>`;
}
function evidence(node) {
  return node.evidence.map(id => {
    const e = DATA.evidence[id], d = DATA.documents[e.document];
    return `<div class="evidence"><a href="${esc(sourceUrl(e))}" target="_blank" rel="noopener">${esc(d.title)} · ${e.lines[0]}–${e.lines[1]}행 ↗</a><small>원문 버전 ${esc(d.revision.slice(0,7))} · ${e.kind === 'specification' ? '운영 규칙' : '작성자의 보고'}</small><details><summary>근거 원문 펼치기</summary><pre>${esc(e.excerpt)}</pre></details></div>`;
  }).join('');
}
function related(node, incoming) {
  const edges = graph.edges.filter(e => incoming ? e.target === node.id : e.source === node.id);
  if (!edges.length) return '<p class="muted">없음</p>';
  return `<div class="neighbors">${edges.map(e => {
    const other = byId[incoming ? e.source : e.target];
    return `<button data-select="${esc(other.id)}">${esc(other.title)}<small>${esc(e.label)}</small></button>`;
  }).join('')}</div>`;
}
function panel(node) {
  if (!node) {
    $('panel').innerHTML = `<span class="node-ref">${esc(DATA.version)} · ${esc(currentCase.title)}</span><h2>어떤 과정을 거쳤을까요?</h2><p>노드를 선택하면 목적, 입력과 산출물, 판단 근거를 확인할 수 있습니다.</p><div class="callout">${currentCase.kind === 'report' ? '이 사례는 작성자의 회고 기록입니다. 수행 보고는 당시 실행 로그나 결과를 독립적으로 확인했다는 뜻이 아닙니다.' : '이 지도는 문서가 정한 절차입니다. 특정 작업이 실제로 수행했다는 뜻이 아닙니다.'}</div><h3>더 세밀하게 살펴보기</h3>${graph.nodes.filter(n=>n.detail).map(n=>scaleLink(graphs[n.detail],n.title)).join('') || '<p class="muted">현재 가장 세밀한 지도입니다.</p>'}${graph.parent ? `<h3>상위 지도</h3><a class="scale-link" href="${esc(url(graph.parent.graph,graph.parent.node))}">← ${esc(graphs[graph.parent.graph].title)}</a>` : ''}<h3>질문과 피드백</h3><p>노드를 선택한 뒤 ‘질문 복사’를 눌러 대화에 붙여 넣으세요. 대상·버전·근거 링크가 함께 복사됩니다.</p><h3>현재 검토 범위</h3><p class="muted">${esc(currentCase.description)}</p>`;
    return;
  }
  const state = status(node);
  const statement = state === 'mixed' ? '하위 단계에 수행 보고와 미수행 보고가 섞여 있습니다. 상위 단계를 완료로 단정하지 않습니다.' : state === 'specified' ? '절차에 적힌 요구입니다. 실제 수행 여부를 확인할 실행 기록은 연결되어 있지 않습니다.' : state === 'not_done' ? '작성자가 하지 않았다고 명시한 항목입니다.' : state === 'reported' ? '작성자가 수행했다고 보고했습니다. 원래 실행 로그·산출물과의 대조는 아직 하지 않았습니다.' : '근거와 확인 범위를 확인하세요.';
  $('panel').innerHTML = `<div class="node-ref">${esc(graph.id)} / ${esc(node.id)}</div><h2>${esc(node.title)}</h2>${badge(node)}<p>${esc(node.body)}</p><div class="callout">${esc(statement)}</div>${node.detail ? scaleLink(graphs[node.detail],node.title) : ''}${graph.parent ? `<a class="scale-link" href="${esc(url(graph.parent.graph,graph.parent.node))}">← 상위 지도 · ${esc(graphs[graph.parent.graph].title)}</a>` : ''}<h3>입력과 산출물</h3><dl class="io"><dt>입력</dt><dd>${esc(node.inputs.join(' · '))}</dd><dt>산출물</dt><dd>${esc(node.outputs.join(' · '))}</dd></dl><h3>판단 근거</h3>${evidence(node)}<div class="panel-actions"><button id="copy-link">링크 복사</button><button id="copy-question">질문 복사</button></div><h3>앞 단계</h3>${related(node,true)}<h3>다음 단계</h3>${related(node,false)}`;
  $('panel').querySelectorAll('[data-select]').forEach(b => b.onclick = () => select(b.dataset.select,true,true));
  $('copy-link').onclick = () => copy(url(graph.id,node.id));
  $('copy-question').onclick = () => copy(`[업무 검토 지도 ${DATA.version}]\n대상: ${currentCase.id} / ${graph.id} / ${node.id} — ${node.title}\n확인 수준: ${labels[state]}\n지도: ${url(graph.id,node.id)}\n근거: ${node.evidence.map(id=>sourceUrl(DATA.evidence[id])).join('\n')}\n\n질문/피드백: 이 단계의 근거와 세부 과정을 설명해 주세요.\n변경 범위: 우선 설명과 검토 지도를 갱신해 주세요. 실제 업무 실행 규칙 변경은 별도로 구별해 주세요.`);
}
function select(id, focus = false, push = false) {
  selected = byId[id] ? id : null;
  const lit = new Set(selected ? [selected] : []), stack = selected ? [selected] : [];
  while(stack.length) { const target = stack.pop(); graph.edges.filter(e=>e.target===target).forEach(e=>{if(!lit.has(e.source)){lit.add(e.source);stack.push(e.source);}}); }
  document.querySelectorAll('.node').forEach(el=>{el.classList.toggle('selected',el.dataset.id===selected);el.classList.toggle('dim',!!selected&&!lit.has(el.dataset.id));el.setAttribute('aria-pressed',String(el.dataset.id===selected));});
  document.querySelectorAll('.edge').forEach((el,i)=>el.classList.toggle('active',lit.has(graph.edges[i].source)&&lit.has(graph.edges[i].target)));
  $('jump').value = selected || '';
  panel(byId[selected]);
  $('panel').scrollTop = 0;
  if (push) history.pushState(null,'',url(graph.id,selected));
  if (focus && selected) {
    const n = byId[selected], r = $('viewport').getBoundingClientRect();
    scale = Math.min(1.15, (r.width-40)/238, (r.height-35)/160);
    tx = r.width/2-(n.position[0]*350+40+119)*scale;
    ty = r.height/2-(n.position[1]*230+60+80)*scale;
    transform();
  }
}
function transform() { $('world').style.transform=`translate(${tx}px,${ty}px) scale(${scale})`;$('zoom-level').textContent=Math.round(scale*100)+'%'; }
function fit() { const r=$('viewport').getBoundingClientRect();scale=Math.max(.12,Math.min(1,(r.width-50)/width,(r.height-70)/height));tx=(r.width-width*scale)/2;ty=(r.height-height*scale)/2;transform(); }
function zoom(factor,x,y) {const r=$('viewport').getBoundingClientRect();x??=r.width/2;y??=r.height/2;const next=Math.min(2.5,Math.max(.12,scale*factor));tx=x-(x-tx)*next/scale;ty=y-(y-ty)*next/scale;scale=next;transform();}
function svgEl(tag,attrs,text) {const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attrs).forEach(([k,v])=>el.setAttribute(k,v));if(text)el.textContent=text;return el;}
function draw() {
  for(const n of graph.nodes) {
    const el=document.createElement('button');el.className='node';el.dataset.id=n.id;el.style.left=(40+n.position[0]*350)+'px';el.style.top=(60+n.position[1]*230)+'px';
    el.setAttribute('aria-label',`${n.id} ${n.title} · ${labels[status(n)]}`);
    el.innerHTML=`<span class="id">${esc(n.id)}</span><h2>${esc(n.title)}</h2><span class="summary">${esc(n.summary)}</span><span class="node-bottom">${badge(n)}${n.detail?'<span class="detail-mark">세부 지도 ↗</span>':''}</span>`;
    el.onclick=()=>{if(!dragMoved)select(n.id,false,true);};el.ondblclick=()=>select(n.id,true,false);$('nodes').appendChild(el);
    const option=document.createElement('option');option.value=n.id;option.textContent=`${n.id} · ${n.title}`;$('jump').appendChild(option);
  }
  const dims=Object.fromEntries([...document.querySelectorAll('.node')].map(el=>[el.dataset.id,{x:el.offsetLeft,y:el.offsetTop,w:el.offsetWidth,h:el.offsetHeight}]));
  width=Math.max(...Object.values(dims).map(d=>d.x+d.w))+40;height=Math.max(...Object.values(dims).map(d=>d.y+d.h))+50;
  $('world').style.width=width+'px';$('world').style.height=height+'px';$('edges').setAttribute('width',width);$('edges').setAttribute('height',height);
  graph.edges.forEach((e,i)=>{
    const a=dims[e.source],b=dims[e.target],long=b.x-a.x>750;
    let path,labelX,labelY;
    if(a.x===b.x){const x=a.x+a.w/2,y1=a.y+a.h,y2=b.y;path=`M ${x},${y1} V ${y2}`;labelX=x+40;labelY=(y1+y2)/2;}
    else if(long){const rail=25;path=`M ${a.x+a.w/2},${a.y} V ${rail} H ${b.x+b.w/2} V ${b.y}`;labelX=(a.x+b.x+a.w)/2;labelY=rail-9;}
    else {const x1=a.x+a.w,y1=a.y+a.h/2,x2=b.x,y2=b.y+b.h/2,m=(x1+x2)/2;path=`M ${x1},${y1} C ${m},${y1} ${m},${y2} ${x2},${y2}`;labelX=m;labelY=(y1+y2)/2-12;}
    $('edges').appendChild(svgEl('path',{d:path,class:'edge '+e.kind,'marker-end':'url(#arrow)'}));
    $('edges').appendChild(svgEl('text',{x:labelX,y:labelY,'text-anchor':'middle',class:'edge-label'},e.label));
  });
}
async function copy(text) {try{await navigator.clipboard.writeText(text);$('toast').textContent='복사했습니다. 대화에 붙여 넣어 주세요.';$('toast').hidden=false;clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('toast').hidden=true,2600);}catch{$('copy-content').value=text;$('copy-dialog').showModal();$('copy-content').select();}}
$('copy-close').onclick=()=>$('copy-dialog').close();
$('title').textContent=graph.title;document.title=graph.title+' · 업무 검토 지도';$('description').textContent=graph.description;
$('eyebrow').textContent=currentCase.kind==='report'?'사후 검토 · 문서 기반 재구성':'절차 이해 · 수행 기록 미연결';
$('context').textContent=`v${DATA.version} · ${currentCase.title} · ${DATA.updated}`;
for(const c of DATA.cases){const o=document.createElement('option');o.value=c.id;o.textContent=c.title;$('case').appendChild(o);}$('case').value=currentCase.id;
$('case').onchange=()=>{const c=DATA.cases.find(c=>c.id===$('case').value);location.href=url(c.root,null,c.id);};
const chain=[];let ancestor=graph;while(ancestor){chain.unshift(ancestor);ancestor=ancestor.parent?graphs[ancestor.parent.graph]:null;}
$('breadcrumbs').innerHTML=chain.map((g,i)=>i===chain.length-1?`<span class="current" aria-current="page">${esc(g.title)}</span>`:`<a href="${esc(url(g.id,chain[i+1].parent.node))}">${esc(g.title)}</a><span aria-hidden="true">›</span>`).join('');
let drag=null,dragMoved=false;
$('viewport').addEventListener('pointerdown',e=>{if(e.button!==0)return;drag={x:e.clientX,y:e.clientY,tx,ty};dragMoved=false;});
window.addEventListener('pointermove',e=>{if(!drag)return;if(Math.hypot(e.clientX-drag.x,e.clientY-drag.y)>5)dragMoved=true;if(dragMoved){tx=drag.tx+e.clientX-drag.x;ty=drag.ty+e.clientY-drag.y;transform();}});
window.addEventListener('pointerup',()=>{drag=null;});window.addEventListener('pointercancel',()=>{drag=null;});
$('viewport').addEventListener('wheel',e=>{e.preventDefault();const r=$('viewport').getBoundingClientRect();zoom(Math.exp(-e.deltaY*.0015),e.clientX-r.left,e.clientY-r.top);},{passive:false});
$('viewport').addEventListener('keydown',e=>{if(e.target!==$('viewport'))return;const moves={ArrowLeft:[40,0],ArrowRight:[-40,0],ArrowUp:[0,40],ArrowDown:[0,-40]};if(moves[e.key]){e.preventDefault();tx+=moves[e.key][0];ty+=moves[e.key][1];transform();}if(e.key==='0')fit();if(e.key==='+')zoom(1.25);if(e.key==='-')zoom(.8);if(e.key==='Escape')select(null,false,true);});
$('fit').onclick=fit;$('zoom-in').onclick=()=>zoom(1.25);$('zoom-out').onclick=()=>zoom(.8);$('clear').onclick=()=>select(null,false,true);$('jump').onchange=()=>select($('jump').value,true,true);
function fromHash(){const id=new URLSearchParams(location.hash.slice(1)).get('node');select(id,!!id,false);if(id&&!byId[id]){$('panel').insertAdjacentHTML('afterbegin','<div class="callout">요청한 노드를 찾을 수 없습니다. 현재 지도의 노드를 선택하세요.</div>');}}
draw();fit();fromHash();
window.addEventListener('popstate',fromHash);window.addEventListener('hashchange',fromHash);
new ResizeObserver(()=>selected?select(selected,true,false):fit()).observe($('viewport'));
if(params.get('v')&&params.get('v')!==DATA.version){
  const notice=`요청 버전 ${params.get('v')} → 현재 버전 ${DATA.version}`;
  $('eyebrow').textContent+=' · '+notice;
  $('description').textContent=notice+'. '+graph.description;
}
