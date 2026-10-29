// 수식 렌더링 후 페이지 높이가 바뀌므로, 렌더링이 끝나면 URL 의 앵커(#s2-1-p3-s10 등)로 다시 스크롤한다
function m2pScrollToHash() {
  if (!location.hash) return;
  const el = document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if (el) el.scrollIntoView();
}
window.MathJax = {
  loader: { load: ["[tex]/boldsymbol", "[tex]/mathtools", "[tex]/cancel", "[tex]/braket", "[tex]/bbox", "[tex]/color", "[tex]/textmacros"] },
  tex: {
    packages: ["base", "ams", "newcommand", "configmacros", "boldsymbol", "mathtools", "cancel", "braket", "bbox", "color", "textmacros", "noundefined"],
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  startup: {
    // 웹 글꼴이 늦게 도착해도 페이지 높이가 바뀌므로 글꼴 로드 후 한 번 더
    pageReady: () => MathJax.startup.defaultPageReady().then(m2pScrollToHash)
      .then(() => document.fonts && document.fonts.ready).then(m2pScrollToHash)
  }
};
// MkDocs Material 의 instant navigation 용. 첫 페이지 로드는 startup 이 처리하므로 건너뛴다
let m2pFirst = true;
if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    if (m2pFirst) { m2pFirst = false; return; }
    if (!window.MathJax || !MathJax.typesetPromise) return;
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise().then(m2pScrollToHash);
  });
}
