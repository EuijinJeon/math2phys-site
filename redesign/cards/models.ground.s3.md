---
id: models:ground.s3
kind: step
title: '$\beta\to\infty$ 로 $g_N$ 의 수렴, 그리고 (10.1)'
uses: [models:ground.s1, models:ground.s2]
provides: 'models:ground의 결론 (극한 $g$ 의 존재, $[g,g+\log2/\beta]$, (10.1))'
math: |
  $\beta\to\infty$ 로 보내면 $g_N$ 이 극한 $g$ 로 수렴한다. 이제 유한 크기 끼움에서 $N\to\infty$ 로 보내면 $g\le I(\beta)/\beta\le g+\log(2)/\beta$ 이고, 이것이 (10.1)을 증명한다.
physics: |
  s2에서 $\limsup_Ng_N-\liminf_Ng_N\le\log2/\beta$ 가 모든 $\beta$ 에서 성립하므로 둘이 같다. 그러면 각 $\beta$ 에서 $-f(\beta)$ 가 $g$ 와 $g+\log2/\beta$ 사이에 있고, $\beta\to\infty$ 에서 $g$ 로 간다.
gap: |
  정확하다. "$\beta\to\infty$ 로 $g_N$ 의 수렴"의 중간 단계(limsup과 liminf의 차가 $\log2/\beta$ 이하이고, $g_N$ 이 균일 유계라 극한이 유한)는 작성자가 풀어 적었다. 극한 순서는 고정 $\beta$ 에서 $N\to\infty$ 가 먼저다.
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [120, 123]}
status: proposed
---
