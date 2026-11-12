// render_maps.js — Mermaid 텍스트(.mmd)를 헤드리스 Chromium 으로 SVG 로 그린다. render_maps.py 가 부른다.
// 사용: NODE_PATH=<전역 node_modules> CHROME=<실행 파일> node render_maps.js <mermaid.min.js> <입출력 디렉터리> <이름>...
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const [mer, dir, ...names] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: process.env.CHROME || undefined, args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setContent('<!doctype html><html><body><div id="x"></div></body></html>');
  await page.addScriptTag({ path: mer });
  let bad = 0;
  for (const name of names) {
    const text = fs.readFileSync(path.join(dir, name + '.mmd'), 'utf8');
    try {
      const svg = await page.evaluate(async ([id, t]) => {
        mermaid.initialize({ startOnLoad: false, securityLevel: 'loose', maxTextSize: 500000, maxEdges: 2000,
                             flowchart: { useMaxWidth: true, htmlLabels: true } });
        const r = await mermaid.render(id, t);
        return r.svg;
      }, ['m' + names.indexOf(name), text]);
      fs.writeFileSync(path.join(dir, name + '.svg'), svg);
      console.log('그림', name, Math.round(svg.length / 1024) + ' KB');
    } catch (e) {
      bad++;
      console.log('실패', name, String(e).split('\n')[0]);
    }
  }
  await browser.close();
  process.exit(bad ? 1 : 0);
})();
