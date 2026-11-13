// verify_site.js — 지은 사이트(또는 한 파일 내보내기)를 헤드리스 Chromium 으로 열어 검사한다. verify_site.py 가 부른다.
// 쪽마다: (a) MathJax 렌더 오류(mjx-merror 등) (b) 깨진 내부 링크 (c) 390px 폭의 가로 넘침 (d) 콘솔 오류.
// CDN(MathJax, Mermaid)은 --mathjax/--mermaid 로 받은 로컬 파일로 대신 응답한다(CDN 이 막힌 환경에서도 같은 코드가 돈다).
// 사용: NODE_PATH=<전역 node_modules> node verify_site.js --site DIR | --artifact FILE
//        [--mathjax DIR(es5 를 담은 package/)] [--mermaid FILE] [--jobs N] [--width 390] [--json OUT] [--only 정규식]
const fs = require('fs');
const path = require('path');
const http = require('http');
const { chromium } = require('playwright');

const argv = process.argv.slice(2);
const opt = (k, d) => { const i = argv.indexOf('--' + k); return i >= 0 ? argv[i + 1] : d; };
const SITE = opt('site'), ARTIFACT = opt('artifact');
const MATHJAX = opt('mathjax'), MERMAID = opt('mermaid');
const JOBS = parseInt(opt('jobs', '4'), 10), WIDTH = parseInt(opt('width', '390'), 10);
const JSON_OUT = opt('json'), ONLY = opt('only') ? new RegExp(opt('only')) : null;
if (!SITE && !ARTIFACT) { console.error('--site 또는 --artifact 가 필요하다'); process.exit(2); }

const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.json': 'application/json', '.css': 'text/css',
  '.svg': 'image/svg+xml', '.woff': 'font/woff', '.woff2': 'font/woff2', '.otf': 'font/otf', '.ttf': 'font/ttf', '.map': 'application/json' };

function serve(root) {
  const srv = http.createServer((req, res) => {
    let p = decodeURIComponent(req.url.split('?')[0].split('#')[0]);
    if (p.endsWith('/')) p += 'index.html';
    const f = path.join(root, p);
    if (!f.startsWith(root) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.statusCode = 404; res.end('not found'); return; }
    res.setHeader('Content-Type', MIME[path.extname(f)] || 'application/octet-stream');
    fs.createReadStream(f).pipe(res);
  });
  return new Promise(r => srv.listen(0, '127.0.0.1', () => r(srv)));
}

function walk(dir, base = dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const f = path.join(dir, e.name);
    if (e.isDirectory()) walk(f, base, out); else out.push(path.relative(base, f).split(path.sep).join('/'));
  }
  return out;
}

// 쪽 안에서 도는 검사. 반환: 수치와 예.
const inPage = ({ scope }) => {
  const out = {};
  const root = scope ? document.getElementById(scope) : document.body;
  // (a) MathJax 오류
  // MathJax 3.2 는 TeX 오류를 mjx-merror 로, 정의 안 된 매크로(noundefined)를 빨간 글씨(color: red)의 mjx-mtext 로 그린다. 둘 다 센다.
  const dec = (e) => [...e.querySelectorAll('mjx-c')].map(c => { const m = (c.className || '').match(/mjx-c([0-9A-F]+)/); return m ? String.fromCodePoint(parseInt(m[1], 16)) : ''; }).join('');
  const reds = [...document.querySelectorAll('mjx-container [style*="color: red"], mjx-container [style*="color:red"]')]
    .filter(e => !e.parentElement.closest('[style*="color: red"]')).map(e => '정의 안 된 매크로: ' + dec(e).slice(0, 80));
  const merr = [...document.querySelectorAll('mjx-merror, [data-mjx-error]')].map(e => 'merror: ' + (e.getAttribute('data-mjx-error') || e.textContent || '').slice(0, 100));
  out.merror = merr.concat(reds);
  out.mjx = document.querySelectorAll('mjx-container').length;
  // 풀리지 않은 수식 구분자: 코드·pre·mjx 밖의 글에 $..$ 가 남아 있는가
  const bad = [];
  const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  for (let n = w.nextNode(); n; n = w.nextNode()) {
    if (n.parentElement.closest('pre,code,script,style,mjx-container,textarea')) continue;
    if (/\$[^$\s][^$]*\$|\\\(|\\\[|\$\$/.test(n.nodeValue)) bad.push(n.nodeValue.trim().slice(0, 80));
  }
  out.raw = bad;
  // Mermaid 오류
  out.mermaidErr = [...root.querySelectorAll('pre.mermaid')].filter(p => !p.querySelector('svg') || /Syntax error/i.test(p.textContent)).length;
  // (c) 가로 넘침
  const de = document.documentElement;
  out.scrollW = Math.max(de.scrollWidth, document.body.scrollWidth);
  out.clientW = de.clientWidth;
  out.overflow = out.scrollW > out.clientW + 1;
  const offenders = [];
  const scrolls = (e) => { for (let a = e.parentElement; a && a !== document.body; a = a.parentElement) {
    const o = getComputedStyle(a).overflowX; if (o === 'auto' || o === 'scroll' || o === 'hidden') return true; } return false; };
  for (const e of root.querySelectorAll('*')) {
    if (e.closest('svg') && e.tagName !== 'svg') continue;
    const r = e.getBoundingClientRect();
    if (r.width && r.right > de.clientWidth + 1 && !scrolls(e)) {
      offenders.push(e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + (e.className && typeof e.className === 'string' ? '.' + e.className.split(' ')[0] : '') + ' right=' + Math.round(r.right));
      if (offenders.length >= 4) break;
    }
  }
  out.offenders = offenders;
  // (b) 링크와 id
  out.hrefs = [...document.querySelectorAll('a[href], area[href]')].map(a => a.getAttribute('href'))
    .concat([...document.querySelectorAll('svg a')].map(a => a.getAttribute('href') || a.getAttribute('xlink:href')).filter(Boolean));
  out.ids = [...document.querySelectorAll('[id]')].map(e => e.id);
  return out;
};

async function newContext(browser, base) {
  const ctx = await browser.newContext({ viewport: { width: WIDTH, height: 844 } });
  await ctx.route(/^https?:\/\/(cdn\.jsdelivr\.net|cdnjs\.cloudflare\.com|unpkg\.com)\//, async (route) => {
    const url = route.request().url();
    let m = url.match(/mathjax@[^/]+\/(es5\/.*?)(\?.*)?$/);
    if (m && MATHJAX) {
      const f = path.join(MATHJAX, m[1]);
      if (fs.existsSync(f)) return route.fulfill({ path: f, contentType: MIME[path.extname(f)] || 'application/octet-stream' });
    }
    if (/mermaid/.test(url) && MERMAID && fs.existsSync(MERMAID)) return route.fulfill({ path: MERMAID, contentType: 'text/javascript' });
    return route.abort();
  });
  return ctx;
}

// 쪽 하나가 숨김 해제된 뒤 수식 개수가 300ms 동안 변하지 않을 때까지 기다린다(한 파일 내보내기는 쪽을 열 때 typeset 한다).
async function waitStable(page, sel) {
  let last = -1, same = 0;
  for (let i = 0; i < 100 && same < 3; i++) {
    const n = await page.evaluate((s) => document.querySelectorAll(s + ' mjx-container').length, sel);
    same = (n === last) ? same + 1 : 0; last = n;
    await page.waitForTimeout(100);
  }
}

async function waitRender(page) {
  const st = { mathjax: 'none', timeout: false };
  const has = await page.evaluate(() => !!(window.MathJax));
  if (has) {
    try {
      await page.waitForFunction(() => window.MathJax && MathJax.startup && MathJax.startup.promise, null, { timeout: 15000 });
      await page.evaluate(async () => { await MathJax.startup.promise; });   // 두 번째 typeset 은 하지 않는다(assistive MathML 이 중첩된다)
      st.mathjax = 'ok';
    } catch (e) { st.mathjax = 'timeout'; st.timeout = true; }
  }
  const nm = await page.evaluate(() => document.querySelectorAll('pre.mermaid').length);
  if (nm) {
    try { await page.waitForFunction(() => [...document.querySelectorAll('pre.mermaid')].every(p => p.querySelector('svg') || /Syntax/.test(p.textContent)), null, { timeout: 15000 }); }
    catch (e) { st.timeout = true; }
  }
  // 웹 폰트(MathJax 글꼴)가 다 내려온 뒤에 폭이 정해진다. 그 전에 재면 일시적인 넘침을 센다.
  await page.evaluate(async () => { await document.fonts.ready; await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); });
  await page.waitForTimeout(150);
  return st;
}

async function runPool(items, n, fn) {
  let i = 0;
  await Promise.all(Array.from({ length: n }, async () => { for (;;) { const k = i++; if (k >= items.length) return; await fn(items[k], k); } }));
}

(async () => {
  const root = ARTIFACT ? path.dirname(path.resolve(ARTIFACT)) : path.resolve(SITE);
  const srv = await serve(root);
  const origin = 'http://127.0.0.1:' + srv.address().port;
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const results = [];
  let jobs;
  if (ARTIFACT) {
    // 한 파일: 쪽마다 section.page 의 id 로 간다
    const ctx0 = await browser.newContext();
    const p0 = await ctx0.newPage();
    await p0.goto(origin + '/' + path.basename(ARTIFACT), { waitUntil: 'domcontentloaded' });
    jobs = await p0.evaluate(() => [...document.querySelectorAll('section.page')].map(s => s.id));
    await ctx0.close();
    jobs = jobs.filter(id => !ONLY || ONLY.test(id));
  } else {
    jobs = walk(root).filter(f => f.endsWith('.html')).filter(f => !ONLY || ONLY.test(f)).sort();
  }
  const pageIds = {};      // 쪽 → id 집합
  const rawLinks = {};     // 쪽 → href 목록
  let done = 0;
  const t0 = Date.now();

  const handle = async (ctx, job) => {
    const page = await ctx.newPage();
    const cons = [];
    page.on('console', m => { if (m.type() === 'error') cons.push('console: ' + m.text().slice(0, 200)); });
    page.on('pageerror', e => cons.push('pageerror: ' + String(e).slice(0, 200)));
    page.on('requestfailed', r => cons.push('requestfailed: ' + r.url().slice(0, 150)));
    page.on('response', r => { if (r.status() >= 400) cons.push('http ' + r.status() + ': ' + r.url().slice(0, 150)); });
    const rec = { page: job };
    try {
      if (ARTIFACT) {
        await page.goto(origin + '/' + path.basename(ARTIFACT) + '#' + job, { waitUntil: 'load' });
        await page.evaluate((id) => { if (location.hash !== '#' + id) location.hash = id; }, job);
      } else {
        await page.goto(origin + '/' + job, { waitUntil: 'load' });
      }
      const st = await waitRender(page);
      if (ARTIFACT) await waitStable(page, 'section[id="' + job + '"]');
      Object.assign(rec, st);
      if (ARTIFACT) {
        // 보이는 쪽(section#id)만 본다
        rec.visible = await page.evaluate((id) => { const e = document.getElementById(id); return !!e && !e.hidden; }, job);
        const r = await page.evaluate(inPage, { scope: job });
        // 수식·링크 수는 보이는 쪽 하나에 한정
        const scoped = await page.evaluate((id) => {
          const el = document.getElementById(id);
          const o = {};
          const dec = (e) => [...e.querySelectorAll('mjx-c')].map(c => { const m = (c.className || '').match(/mjx-c([0-9A-F]+)/); return m ? String.fromCodePoint(parseInt(m[1], 16)) : ''; }).join('');
          o.merror = [...el.querySelectorAll('mjx-merror, [data-mjx-error]')].map(e => 'merror: ' + (e.getAttribute('data-mjx-error') || e.textContent || '').slice(0, 100))
            .concat([...el.querySelectorAll('mjx-container [style*="color: red"], mjx-container [style*="color:red"]')]
              .filter(e => !e.parentElement.closest('[style*="color: red"]')).map(e => '정의 안 된 매크로: ' + dec(e).slice(0, 80)));
          o.mjx = el.querySelectorAll('mjx-container').length;
          o.hrefs = [...el.querySelectorAll('a[href]')].map(a => a.getAttribute('href'));
          o.ids = [...el.querySelectorAll('[id]')].map(e => e.id);
          return o;
        }, job);
        Object.assign(r, scoped);
        Object.assign(rec, r);
      } else {
        Object.assign(rec, await page.evaluate(inPage, { scope: null }));
      }
    } catch (e) {
      rec.fatal = String(e).slice(0, 200);
    }
    rec.console = cons;
    results.push(rec);
    await page.close();
    done++;
    if (done % 25 === 0) console.error(`  ${done}/${jobs.length} (${Math.round((Date.now() - t0) / 1000)} s)`);
  };

  // 여러 맥락(각각 캐시를 따로) 대신 맥락 하나에 쪽 JOBS 개씩
  const ctx = await newContext(browser);
  await runPool(jobs, JOBS, (job) => handle(ctx, job));
  await ctx.close();
  await browser.close();
  srv.close();

  results.sort((a, b) => (a.page < b.page ? -1 : 1));
  // (b) 링크 확인
  const known = new Set(results.map(r => r.page));
  for (const r of results) { pageIds[r.page] = new Set(r.ids || []); }
  const broken = [];
  const exists = (rel) => known.has(rel) || fs.existsSync(path.join(root, rel));
  for (const r of results) {
    for (const h of (r.hrefs || [])) {
      if (!h || /^(https?:|mailto:|javascript:|data:)/.test(h)) continue;
      if (ARTIFACT) {
        if (h[0] !== '#') { broken.push({ page: r.page, href: h, why: '한 파일 안에서 # 로 시작하지 않는 링크' }); continue; }
        const id = h.slice(1);
        if (!known.has(id)) broken.push({ page: r.page, href: h, why: '쪽 id 없음' });
        continue;
      }
      const [p, frag] = h.split('#');
      let target = p ? path.posix.normalize(path.posix.join(path.posix.dirname(r.page), p)) : r.page;
      if (target.endsWith('/')) target += 'index.html';
      if (!exists(target)) { broken.push({ page: r.page, href: h, why: '대상 파일 없음' }); continue; }
      if (frag) {
        const ids = pageIds[target];
        if (ids && !ids.has(decodeURIComponent(frag))) broken.push({ page: r.page, href: h, why: '앵커 없음' });
      }
    }
  }
  const sum = {
    mode: ARTIFACT ? 'artifact' : 'site', width: WIDTH, pages: results.length,
    pages_with_merror: results.filter(r => (r.merror || []).length).length,
    merror_total: results.reduce((s, r) => s + (r.merror || []).length, 0),
    merror_undefined_macro: results.reduce((s, r) => s + (r.merror || []).filter(x => x.startsWith('정의 안 된')).length, 0),
    pages_with_raw_math: results.filter(r => (r.raw || []).length).length,
    pages_with_mathjax: results.filter(r => r.mjx > 0).length,
    mjx_total: results.reduce((s, r) => s + (r.mjx || 0), 0),
    mathjax_timeouts: results.filter(r => r.mathjax === 'timeout').length,
    mermaid_pages_with_error: results.filter(r => r.mermaidErr > 0).length,
    broken_links: broken.length, pages_with_broken_links: new Set(broken.map(b => b.page)).size,
    links_total: results.reduce((s, r) => s + (r.hrefs || []).length, 0),
    pages_overflow: results.filter(r => r.overflow).length,
    pages_with_console_errors: results.filter(r => (r.console || []).length).length,
    console_errors_total: results.reduce((s, r) => s + (r.console || []).length, 0),
    fatal: results.filter(r => r.fatal).length,
  };
  const outp = { summary: sum, broken, pages: results.map(r => { const c = Object.assign({}, r); delete c.hrefs; delete c.ids; return c; }) };
  if (JSON_OUT) fs.writeFileSync(JSON_OUT, JSON.stringify(outp, null, 1));
  console.log(JSON.stringify(sum, null, 1));
  const show = (title, rows) => { if (rows.length) { console.log('\n' + title); rows.slice(0, 12).forEach(x => console.log('  ' + x)); if (rows.length > 12) console.log(`  … 외 ${rows.length - 12}`); } };
  show('MathJax 오류', results.filter(r => (r.merror || []).length).map(r => `${r.page}: ${r.merror.length}건 ${JSON.stringify(r.merror[0])}`));
  show('풀리지 않은 수식 구분자', results.filter(r => (r.raw || []).length).map(r => `${r.page}: ${r.raw.length}곳 ${JSON.stringify(r.raw[0])}`));
  show('깨진 링크', broken.map(b => `${b.page}: ${b.href} (${b.why})`));
  show(`${WIDTH}px 가로 넘침`, results.filter(r => r.overflow).map(r => `${r.page}: scrollWidth ${r.scrollW} > ${r.clientW}; ${(r.offenders || []).join(' | ')}`));
  show('콘솔 오류', results.filter(r => (r.console || []).length).map(r => `${r.page}: ${r.console[0]}`));
  show('치명 오류', results.filter(r => r.fatal).map(r => `${r.page}: ${r.fatal}`));
  const bad = sum.pages_with_merror || sum.broken_links || sum.pages_overflow || sum.pages_with_console_errors || sum.fatal || sum.mathjax_timeouts || sum.mermaid_pages_with_error;
  process.exit(bad ? 1 : 0);
})();
