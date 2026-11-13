---
id: models:ground.s1
kind: step
title: '유한 크기 끼움: $g_N\le P_N(\beta)/\beta\le g_N+\log2/\beta$'
uses: [x:cons-energy-score, models:spin, models:sat]
provides: 'models:ground.s2, models:ground.s3 (끼움 부등식, $g_N$ 의 균일 유계성)'
math: |
  $g_N=N^{-1}\mathbb E\max_\sigma\mathcal E_N(\sigma)$, $P_N(\beta)=N^{-1}\mathbb E\log Z_N(\beta)$ 로 쓴다. 1차 moment 가정으로 $g_N$ 은 유한하고 균일하게 유계다. spin 배치가 $2^N$ 개이므로
  $$g_N\le\frac{P_N(\beta)}\beta\le g_N+\frac{\log2}\beta.$$
physics: |
  1차 moment 가정으로 최댓값 밀도 $g_N$ 은 유한하고 $N$ 에 균일하게 유계다. $\max_\sigma e^{\beta\mathcal E_N}\le Z_N\le2^N\max_\sigma e^{\beta\mathcal E_N}$ 이다. 그래서 유한 크기에서 $-f_N(\beta)$ 와 최댓값 밀도 $g_N$ 의 차이는 0 이상 $\log2/\beta$ 이하다($\log2$ 는 배치 수 $2^N$ 에서 온다).
gap: |
  정확하다. 원문이 적지 않은 두 한계를 작성자가 채운다: $\lvert\max_\sigma\mathcal E_N\rvert\le\sum_{k\le M_N}\lvert J_k\rvert+\sum_i\lvert H_i\rvert$ 이라 $\lvert g_N\rvert\le\alpha\mathbb E\lvert J\rvert+\mathbb E\lvert H\rvert$ (spin), $-\sum_{k\le M_N}W_k\le\max_\sigma\mathcal E_N\le0$ 이라 $\lvert g_N\rvert\le\alpha\mathbb EW$ (SAT). 끼움은 $\beta\max\mathcal E_N\le\log Z_N\le N\log2+\beta\max\mathcal E_N$ 의 기대값을 $N\beta$ 로 나눈 것이다.
abstraction: exact
children: []
source:
  - {file: consequences.tex, lines: [103, 111]}
status: proposed
---
