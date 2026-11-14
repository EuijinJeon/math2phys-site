/* 노드 장애물을 피하는 연결선과 선 위의 라벨 기준점. DOM에 의존하지 않는다. */
function routeHits(a,b,r,pad=9){
  const minX=r.x-pad,maxX=r.x+r.w+pad,minY=r.y-pad,maxY=r.y+r.h+pad;
  let lo=0,hi=1;
  for(const [start,delta,min,max] of [[a[0],b[0]-a[0],minX,maxX],[a[1],b[1]-a[1],minY,maxY]]){
    if(Math.abs(delta)<1e-9){if(start<min||start>max)return false;}
    else{let u=(min-start)/delta,v=(max-start)/delta;if(u>v)[u,v]=[v,u];lo=Math.max(lo,u);hi=Math.min(hi,v);if(lo>hi)return false;}
  }
  return true;
}
function routeLength(points){let len=0;for(let i=1;i<points.length;i++)len+=Math.hypot(points[i][0]-points[i-1][0],points[i][1]-points[i-1][1]);return len;}
function edgeRoute(a,b,obstacles){
  const clip=(r,tx,ty)=>{const cx=r.x+r.w/2,cy=r.y+r.h/2,dx=tx-cx,dy=ty-cy;const k=Math.min(dx?(r.w/2+3)/Math.abs(dx):1e9,dy?(r.h/2+3)/Math.abs(dy):1e9);return [cx+dx*k,cy+dy*k];};
  const direct=[clip(a,b.x+b.w/2,b.y+b.h/2),clip(b,a.x+a.w/2,a.y+a.h/2)];
  const hits=points=>obstacles.reduce((sum,r)=>sum+points.slice(1).filter((p,i)=>routeHits(points[i],p,r)).length,0);
  if(!hits(direct))return direct;
  const ys=[...obstacles.flatMap(r=>[r.y-25,r.y+r.h+25]),Math.min(a.y,b.y)-30,Math.max(a.y+a.h,b.y+b.h)+30];
  let best=null;
  for(const y of ys){
    const start=[a.x+a.w/2,y<a.y+a.h/2?a.y-3:a.y+a.h+3];
    const end=[b.x+b.w/2,y<b.y+b.h/2?b.y-3:b.y+b.h+3];
    const points=[start,[start[0],y],[end[0],y],end];
    // 자기 양 끝 상자를 다시 가로지르는 우회 경로도 배제한다.
    const selfCross=routeHits(points[1],points[2],a,0)||routeHits(points[1],points[2],b,0);
    const score=100000*hits(points)+(selfCross?100000:0)+routeLength(points);
    if(!best||score<best.score)best={points,score};
  }
  const xs=[...obstacles.flatMap(r=>[r.x-25,r.x+r.w+25]),Math.min(a.x,b.x)-30,Math.max(a.x+a.w,b.x+b.w)+30];
  for(const x of xs){
    const start=[x<a.x+a.w/2?a.x-3:a.x+a.w+3,a.y+a.h/2];
    const end=[x<b.x+b.w/2?b.x-3:b.x+b.w+3,b.y+b.h/2];
    const points=[start,[x,start[1]],[x,end[1]],end];
    const selfCross=routeHits(points[1],points[2],a,0)||routeHits(points[1],points[2],b,0);
    const score=100000*hits(points)+(selfCross?100000:0)+routeLength(points);
    if(!best||score<best.score)best={points,score};
  }
  return best.points;
}
function routePoint(points,fraction){
  const total=routeLength(points);let remain=total*fraction;
  for(let i=1;i<points.length;i++){
    const a=points[i-1],b=points[i],len=Math.hypot(b[0]-a[0],b[1]-a[1]);
    if(remain<=len||i===points.length-1){const t=len?remain/len:0;return {x:a[0]+(b[0]-a[0])*t,y:a[1]+(b[1]-a[1])*t,dx:(b[0]-a[0])/(len||1),dy:(b[1]-a[1])/(len||1)};}
    remain-=len;
  }
  return {x:points[0][0],y:points[0][1],dx:1,dy:0};
}
if(typeof module!=='undefined')module.exports={edgeRoute,routeHits,routePoint};
