---
id: decor:conditional-concentration.s2.s1
kind: step
title: '한 층 항등식 (singleton identity)'
uses: [pert:tree-identity, tree:extension-expansion, x:decor-mesh, x:decor-spin-product]
provides: 'decor:conditional-concentration.s2.s2'
math: |
  old tree는 깊이 $d$에서 갈라지는 두 경로 1, 2이고 경로 1이 spin anchor다. 제약: added color 하나가 anchor와 정확히 깊이 $d$에서 갈라진다. 허용된 선택과 계수는 옛 leaf 2 (계수 $1$), 깊이-$d$ vertex에서 fresh (계수 $-c_d$), 경로 2를 따라가다 깊이 $\ell$ ($d<\ell\le L-1$)의 unary vertex에서 fresh (계수 $-c_\ell$)이며
  $$c_d=2m_{d+1}-m_d=(d+2)\delta,\qquad c_\ell=\delta\quad(d<\ell\le L-1).$$
  anchor 혼자일 때의 총 계수는 $-\delta$이다. $X=R_{12}$, $X_\ell=R_{13}$ (경로 3은 해당 fresh 확장)이라 하면 각 $X_\ell$은 $X$와 같은 marginal law를 갖고 $\sum_{\ell=d}^{L-1}c_\ell=1+\delta$이다. $f=X$로 둔 pert:tree-identity에서
  $$\frac12\sum_{\ell=d}^{L-1}c_\ell\,\mathbb E(X-X_\ell)^2=\delta\operatorname{Var}(X)+o_N(1)\le\delta+o_N(1).$$
physics: |
  stochastic stability에서 나오는 Ghirlanda–Guerra 형 항등식의 한 층 판: anchor와 깊이 $d$에서 갈라진 replica 쌍의 overlap $X$와, 새 replica를 tree의 가능한 갈라짐 위치 $\ell$에 가중치 $c_\ell$로 붙였을 때의 overlap $X_\ell$의 차이 제곱 평균의 가중합이 $\delta\operatorname{Var}(X)$와 같다.
gap: |
  pert:selection이 고른 perturbed reservoir의 수열을 따라 고정 $L$에서 $o_N(1)$ 오차로만 성립한다. 가중치 $c_\ell$은 균등 격자 $m_d=d/L$와 tree:extension-expansion의 계수에서 온다. 고전적 GG 항등식의 $P(q)$ 가중치 형태로 바꿔 쓴 것은 아니다.
abstraction: approximation
children: []
source:
  - {file: decorrelation.tex, lines: [263, 286]}
status: proposed
---

계수는 tree:extension-expansion의 규칙 그대로다: 깊이 $d$ vertex는 자식이 둘이므로 $m_d-2m_{d+1}=-c_d$, unary vertex는 $m_\ell-m_{\ell+1}=-\delta$. 총합은 $1-(d+2)\delta-(L-1-d)\delta=-\delta$로 anchor 혼자일 때와 같다(그때는 fresh at $d$, unary, 계수 $-\delta$뿐). 항등식은 $\sum_\ell c_\ell\mathbb E[XX_\ell]=\mathbb EX^2+\delta(\mathbb EX)^2+o_N(1)$을 준다. $\mathbb EX_\ell^2=\mathbb EX^2$와 $\sum c_\ell=1+\delta$를 쓰면 $\frac12\sum c_\ell\mathbb E(X-X_\ell)^2=(1+\delta)\mathbb EX^2-\sum c_\ell\mathbb E[XX_\ell]=\delta\operatorname{Var}X+o_N(1)$이다. trees.tex 316–335의 계산과 같은 구성이다.
