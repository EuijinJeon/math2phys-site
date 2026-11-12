---
id: models:ground
kind: corollary
title: '영온도 변분 극한 (Corollary 10.3, 식 (10.1))'
uses: [models:spin, models:sat, x:cons-energy-score, main:theorem]
provides: 'x:cons-ground-scope (consequences.tex 127: (10.1)의 inf). introduction.tex 33–34("their expected ground-state limits"), L0, g:ground-state'
math: |
  models:spin, models:sat의 각 모형에서 극한
  $$g=\lim_{N\to\infty}\frac1N\mathbb E\max_\sigma\mathcal E_N(\sigma)$$
  이 존재하고
  $$g=\lim_{\beta\to\infty}\frac1\beta\inf_{r\ge0}\inf_{\zeta,\mathbf m}\mathcal B_{r,\beta}(\zeta,\mathbf m)\tag{10.1}$$
  를 만족한다. 더 정확히는 온도 극한 안의 식이 $[g,g+\log(2)/\beta]$ 안에 있다. 단위 가중치 SAT에서는 변수당 위반 clause 최소 개수 기대값의 극한이 $-g$ 이다.
physics: |
  [[models:spin]]의 희석 $p$-spin 모형(Viana–Bray 포함)과 [[models:sat]]의 soft $K$-SAT에서, ground-state 에너지 밀도 $-g$([[g:ground-state]])의 열역학 극한이 존재한다. 각 $\beta$ 에서 free energy density $f(\beta)=-\frac1\beta\inf_r\Phi_r(\beta)$ 는 $[-g-\frac{\log2}{\beta},-g]$ 안에 있고(엔트로피 밀도가 $0$ 과 $\log2$ 사이), 그래서 $-g=\lim_{\beta\to\infty}f(\beta)$ 이다. 단위 가중치 SAT에서 $-g$ 는 변수당 최소 위반 clause 수(그 기대값의 밀도 극한)다.
gap: |
  (1) 극한 순서는 각 고정 $\beta$ 에서 $N\to\infty$, 그다음 $\beta\to\infty$ 다. $\beta=\infty$ 에서 직접 세운 변분 공식(영온도 cavity functional)은 주지 않는다. (2) 각 $\beta$ 에서 inf를 따로 취하고, inf의 달성이나 극한 계층, 영온도 [[g:order-parameter|order parameter]]를 요구하지도 주장하지도 않는다(x:cons-ground-scope). (3) 엔트로피로 읽는 것은 작성자의 읽기다. 원문의 근거는 "$2^N$ 개 배치"라는 한 줄이다(models:ground.s1). (4) 물리 문장의 $f(\beta)=-\frac1\beta\inf_r\Phi_r(\beta)$ 는 주정리로 $\lim_NF_N(\beta)$ 와 같다(models:ground.s2). (5) $\max$ 의 기대값 밀도이고 전형적인 표본의 값이라는 진술은 아니다.
abstraction: exact
children: [models:ground.s1, models:ground.s2, models:ground.s3, models:ground.s4]
source:
  - {file: consequences.tex, lines: [86, 101]}
  - {file: consequences.tex, lines: [103, 125]}
status: proposed
---

**식 라벨.** (10.1)의 라벨 `models:ground-formula`(93행)는 이 따름정리 진술 안에 있으므로 따로 카드를 두지 않는다(`main:formula`가 [[main:theorem]] 카드에 담긴 것과 같다). 원문에서 이 식을 가리키는 곳은 증명 123행([[models:ground.s3]])과 본문 127행([[x:cons-ground-scope]])이다.

**증명의 뼈대.**

- [[models:ground.s1]]: $g_N=N^{-1}\mathbb E\max_\sigma\mathcal E_N$ 은 유한하고 균일하게 유계이며, $g_N\le P_N(\beta)/\beta\le g_N+\log2/\beta$.
- [[models:ground.s2]]: 각 $\beta$ 에서 [[main:theorem]]이 $P_N(\beta)\to I(\beta)$ 를 주므로 $\limsup_Ng_N\le I(\beta)/\beta\le\liminf_Ng_N+\log2/\beta$.
- [[models:ground.s3]]: $\beta\to\infty$ 로 $g_N$ 의 수렴, 다시 $N\to\infty$ 로 $g\le I(\beta)/\beta\le g+\log2/\beta$, 곧 (10.1).
- [[models:ground.s4]]: SAT에서 음의 위반 수를 최대화하는 것은 위반 수를 최소화하는 것이다.

**물리 문장의 부호.** $Z_N(\beta)=\sum_\sigma e^{\beta\mathcal E_N}$ 이므로 에너지는 $-\mathcal E_N$, ground-state 에너지 밀도는 $-g$ 다. $P_N(\beta)=-\beta f_N(\beta)$ 이고 $I(\beta)/\beta\in[g,g+\log2/\beta]$ 는 $f(\beta)\in[-g-\log2/\beta,-g]$ 와 같다(작성자 환산).
