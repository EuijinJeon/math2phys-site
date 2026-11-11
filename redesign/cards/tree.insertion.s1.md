---
id: tree:insertion.s1
kind: step
title: 'backward induction: root log의 변화와 바뀐 kernel'
uses: [tree:original-tilt, tree:Y-recursion]
provides: 'tree:insertion의 첫 문단 (log Y_0, tree:updated-kernel)'
math: |
  말단 spin 적분에서 분배함수 비는 $m_L=1$이므로 $K_LA=Y_{L-1}$이다. $X_d$, $X_d^A$를 옛·새 backward logarithm이라 하면, 앞 power mean에 대입해
  $$\exp\bigl(m_d(X_{d-1}^A-X_{d-1})\bigr)=K_d\exp\bigl(m_d(X_d^A-X_d)\bigr).$$
  backward induction이 $X_d^A-X_d=\log Y_d$를 보이고, 이어서 (tree:updated-kernel)을 준다. $d=L$에서 같은 공식은 보통의 Gibbs 밀도비다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: trees.tex, lines: [113, 124]}
status: proposed
---

풀어 쓰면(작성자): $X_{d-1}^A=m_d^{-1}\log P_de^{m_dX_d^A}$이고 $P_d=e^{-m_d(X_d-X_{d-1})}K_d$이므로 $e^{m_d(X_{d-1}^A-X_{d-1})}=K_de^{m_d(X_d^A-X_d)}$. 귀납 가정 $X_d^A-X_d=\log Y_d$를 넣으면 우변은 $K_dY_d^{m_d}=Y_{d-1}^{m_d}$. 시작점은 $X_{L-1}^A-X_{L-1}=\log(Z_A/Z)=\log K_LA=\log Y_{L-1}$. 새 kernel $e^{m_d(X_d^A-X_{d-1}^A)}P_d=e^{m_d(\log Y_d-\log Y_{d-1})}K_d$가 (tree:updated-kernel)이다.
