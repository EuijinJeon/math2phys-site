---
id: cavity:increment.s2
kind: step
title: '섭동 개수의 맞춤과 항별 비용'
uses: [cavity:factor-bounds, x:cavity-root-convention, x:cavity-bounded, tree:original-tilt, x:tree-extra-variables]
provides: 'cavity:increment.s3 (맞춤 비용 $O(N^{-1/4})$, 항별 비용 $\log2$ 와 $B$), cavity:increment.s4 (coupling estimate)'
math: |
  $(N+1)$-spin 계에서 옛 site의 섭동 개수는 평균 $s_{N+1}N/(N+1)$, 새 site의 개수는 평균 $s_{N+1}/(N+1)$ 이다. 공통 Poisson 점을 써서 이 과정들을 reservoir 섭동에 맞춘다. 맞춰지지 않는 factor 수의 기대값은
  $$\lvert s_{N+1}-s_N\rvert+2s_{N+1}/(N+1)=O(N^{-1/4})$$
  이하다. 섭동 하나를 지우거나 더하면 root logarithm이 많아야 $\log2$ 바뀌고, 상호작용 하나는 많아야 $B$ 바꾼다. 쓰이지 않는 보조 변수는 그 prior로 적분해 없애면 되므로, 보조 변수의 수가 바뀌어도 이 비교들은 유효하다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: cavity.tex, lines: [87, 98]}
status: proposed
---

**풀이 (작성자).** 옛 site 섭동은 $[N+1]$ 의 균일 site를 $[N]$ 으로 제한한 것이라 다시 $[N]$ 에서 균일하다. 평균 차는 $\lvert s_{N+1}N/(N+1)-s_N\rvert\le\lvert s_{N+1}-s_N\rvert+s_{N+1}/(N+1)$ 이고 새 site의 $s_{N+1}/(N+1)$ 을 더하면 위 식이다. $s_N=N^{3/4}$ 이므로 $s_{N+1}-s_N=O(N^{-1/4})$, $s_{N+1}/(N+1)=O(N^{-1/4})$.

항별 비용: $\psi\in[1/2,3/2]$ 이면 $\lvert\log\psi\rvert\le\log2$, $\lvert\theta\rvert\le B$ ([[x:cavity-bounded]])이면 $e^{\pm\theta}\le e^B$. 이 곱셈적 한계(개수와 $\theta$ 는 root 변수)가 backward recursion을 그대로 통과한다([[tree:original-tilt]]의 recursion의 단조성; [[cavity:negligible]]과 같은 논법). 보조 변수의 수가 바뀌는 문제는 [[x:tree-extra-variables]]의 "원래 backward logarithm이 쓰지 않는 변수의 조건부 prior는 tilt되지 않는다"와 같은 관찰이다.
