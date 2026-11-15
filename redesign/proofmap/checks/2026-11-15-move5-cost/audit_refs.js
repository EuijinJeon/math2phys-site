// 생성 보기(build/move5.html 등)의 브라우저 콘솔에서 돌리는 감사. A3 기준의 결함을 센다.
// 결함 = 패널 글 안에서, 펼침(summary/details.src)·단추·원문 블록(pre)·수식 밖에 남은
//   [NODE.item] / NODE.item / 원문 label(pert:selection 꼴) / 맨 위 node id, 그리고 <code> 로 된 id.
// 패널 자신의 이름(edge 패널 제목의 자기 id)은 참조가 아니므로 뺀다.
// 또한 node마다 닫힌 펼침 하나를 눌러 실제로 열리고 내용이 있는지 본다.
(() => {
  const ids = Object.keys((CARDS.__top_nodes__) || {});
  const nodeIdRe = ids.length ? new RegExp('\\b(' + ids.join('|') + ')\\b') : null;
  const pat = /\b(?:[A-Z][A-Z_]{1,}\.[a-z_]+|[a-z]+:[a-z0-9.-]*[a-z0-9])\b/;
  function bare(root, selfId){
    const hits = []; const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    while (w.nextNode()){
      const t = w.currentNode, p = t.parentElement;
      if (p.closest('summary,button,pre,.katex,details.src')) continue;
      let txt = t.textContent; if (selfId) txt = txt.split(selfId).join('');
      const m = txt.match(pat) || (p.tagName !== 'H2' && nodeIdRe ? txt.match(nodeIdRe) : null);
      if (m) hits.push({hit: m[0], where: p.tagName + '.' + p.className, ctx: t.textContent.slice(0, 70)});
    }
    root.querySelectorAll('code').forEach(c => { if (!c.closest('summary,button') && c.textContent !== selfId) hits.push({hit: c.textContent, where: 'code', ctx: ''}); });
    return hits;
  }
  const res = {}; let opened = 0, failedOpen = 0;
  for (const mid of Object.keys(MAPS)){
    cur = mid; const hits = []; let details = 0, buttons = 0;
    for (const n of MAPS[mid].nodes){
      selNode = n.id; selEdge = null; render();
      bare(panel, null).forEach(h => hits.push([n.id, h]));
      details += panel.querySelectorAll('details').length;
      buttons += panel.querySelectorAll('button.jump-node,button.sel-edge').length;
      const d = [...panel.querySelectorAll('details:not([open])')][0];
      if (d){ d.querySelector('summary').click(); opened++; if (!d.open || !d.textContent.trim()) failedOpen++; }
    }
    MAPS[mid].edges.forEach((e, i) => { selNode = null; selEdge = i; render(); bare(panel, e.id).forEach(h => hits.push([e.id, h])); details += panel.querySelectorAll('details').length; });
    res[mid] = {nodes: MAPS[mid].nodes.length, edges: MAPS[mid].edges.length, defects: hits.length, details, buttons, samples: hits.slice(0, 8)};
  }
  cur = Object.keys(MAPS)[0]; selNode = null; selEdge = null; render();
  return JSON.stringify({res, opened, failedOpen});
})()
