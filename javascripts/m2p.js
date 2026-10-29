// 좁은 화면에서 표를 카드처럼 보이도록 각 칸에 열 이름(data-label)을 붙인다 (CSS 는 m2p.css)
function m2pLabelTables() {
  document.querySelectorAll(".md-typeset table:not([class])").forEach(t => {
    const heads = [...t.querySelectorAll("thead th")].map(th => th.textContent.trim());
    t.querySelectorAll("tbody tr").forEach(tr => {
      [...tr.children].forEach((td, i) => td.setAttribute("data-label", heads[i] || ""));
    });
  });
}
if (typeof document$ !== "undefined") document$.subscribe(m2pLabelTables);
else document.addEventListener("DOMContentLoaded", m2pLabelTables);
