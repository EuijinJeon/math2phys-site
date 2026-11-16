// 화면 확인. 쓰임: node render_check.cjs <지도.html> <출력폴더> <mathjax tex-svg.js 로컬 경로>
// 게시 전 파일에는 <!doctype>/<body>가 없으므로 감싼 사본을 만들어 연다.
// 이 작업 환경은 cdnjs가 막혀 있어서 같은 판(3.2.2)의 MathJax를 npm으로 받아 요청을 가로채 넣는다.
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const [,,html,outDir,mj]=process.argv;
fs.mkdirSync(outDir,{recursive:true});
const wrapped=path.join(outDir,'wrapped.html');
fs.writeFileSync(wrapped,'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>[hidden]{display:none!important}</style></head><body>'+fs.readFileSync(html,'utf8')+'</body></html>');
(async()=>{
  const b=await chromium.launch();
  const cases=[['desk',1440,900,'light'],['dark',1440,900,'dark'],['phone',400,800,'light']];
  for(const [name,w,h,scheme] of cases){
    const p=await b.newPage({viewport:{width:w,height:h},colorScheme:scheme});
    await p.route(/cdnjs|fonts\.g/,r=>{const u=r.request().url();
      if(u.includes('tex-svg')) return r.fulfill({path:mj,contentType:'application/javascript'});
      return r.abort();});            // 글꼴은 대체 글꼴로 본다
    const errs=[];
    p.on('pageerror',e=>errs.push(e.message));
    p.on('console',m=>{if(m.type()==='error'&&!/ERR_FAILED/.test(m.text()))errs.push(m.text())});
    await p.goto('file://'+path.resolve(wrapped));
    await p.waitForFunction(()=>document.getElementById('loading').hidden,null,{timeout:20000});
    const info=await p.evaluate(()=>({mathjax:document.querySelectorAll('#world mjx-container').length,bounds,nodes:document.querySelectorAll('.node').length,
      overflowX:document.documentElement.scrollWidth>innerWidth}));
    console.log(name,JSON.stringify(info),errs.length?'오류: '+errs.join(' | '):'오류 없음');
    await p.screenshot({path:path.join(outDir,name+'.png')});
    if(name==='desk'){
      await p.click('#focus'); await p.waitForTimeout(600); await p.screenshot({path:path.join(outDir,'focus.png')});
      await p.evaluate(()=>{const c=clusters.s74;Object.assign(view,fitRect(c.x,c.y,c.w*0.5,c.h,1.0));apply()});
      await p.screenshot({path:path.join(outDir,'zoom-left.png')});
      await p.evaluate(()=>{const c=clusters.s74;Object.assign(view,fitRect(c.x+c.w*0.5,c.y,c.w*0.5,c.h,1.0));apply()});
      await p.screenshot({path:path.join(outDir,'zoom-right.png')});
      await p.evaluate(()=>select('THM')); await p.waitForTimeout(300);
      await p.screenshot({path:path.join(outDir,'select-THM.png')});
    }
    await p.close();
  }
  await b.close();
})();
