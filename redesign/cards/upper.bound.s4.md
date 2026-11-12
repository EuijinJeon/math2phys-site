---
id: upper:bound.s4
kind: step
title: '$t\in[0,1]$ 에서 적분'
uses: [upper:derivative, upper:bound.s2, upper:bound.s3, model:functional]
provides: 'upper:bound의 결론'
math: |
  $t\in[0,1]$ 에서 적분하면 명제가 나온다.
  (작성자 풀이: upper:bound.s3의 끝점 연속성과 (4.1)에서 $F_N-\log2-\mathbb E\log T_0V_{\rm s}=\varphi(1)-\varphi(0)=\int_0^1\varphi'(t)\,dt\le-\alpha(p-1)\mathbb E\log T_0V_{\rm e}$, 곧 $F_N\le\mathcal B_r(\zeta,\mathbf m)$. 시행 법칙과 $r$ 에 대해 inf를 취하면 $F_N\le\inf_{r\ge0}\Phi_r$.)
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: upper.tex, lines: [126, 128]}
status: proposed
---

원문 126행은 "Taking $\lambda\uparrow1$ proves (4.1)"([[upper:remainder]])과 이 단계의 시작을 함께 담는다.
