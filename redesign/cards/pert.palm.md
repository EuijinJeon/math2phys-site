---
id: pert:palm
kind: lemma
title: 'Palm 항등식 (Lemma 6.3)'
uses: [pert:analytic-difference, pert:palm-expression, pert:score-identity, pert:score, pert:factor, pert:parameters, tree:insertion, x:tree-extra-variables]
provides: 'pert:analytic.s3 (|H_N(t_ν,u_ν)| ≤ ‖f‖e_{ν,N}, 그리고 H_N이 j에 무관). 규칙 P7, L1 수 4'
math: |
  $\nu$ 가 지정된 mark를 가진 type이면
  $$|H_N(t_\nu,u_\nu)|\le\|f\|_\infty e_{\nu,N}.$$
  고정된 mark specification에 대해 함수 $H_N(t,u)$ 는 그 모든 type $j$ 에 대해 같다: base reservoir는 모든 type을 포함한 원래 Poisson 족 전체를 담는다.
physics: null
gap: null
abstraction: blackbox
children: [pert:palm.s1, pert:palm.s2]
source:
  - {file: perturbations.tex, lines: [350, 360]}
  - {file: perturbations.tex, lines: [362, 381]}
status: proposed
---

**증명의 뼈대.** [[pert:palm.s1]]: type-$\nu$ 항의 합인 $D_\nu$ 에 Poisson add-one 항등식을 쓰면, 남은 계는 정확히 원래 reservoir 법칙이고 구별된 항은 매개변수 $(t_\nu,u_\nu)$ 의 독립 새 insertion이 되어 $\mathbb E[fD_\nu^{a_*}]/(c_\nu s_N)=J_{N,\mathcal T}(t_\nu,u_\nu)$, $\mathbb E\langle D_\nu\rangle/(c_\nu s_N)=J_{N,\{a_*\}}(t_\nu,u_\nu)$. [[pert:palm.s2]]: (6.13)에 대입해 (6.16), 그리고 어느 type도 base 법칙에서 지워지지 않았으므로 마지막 주장.

물리 대응은 두지 않았다([[g:palm-identity]]의 물리 대응 칸이 "없음"). 이 lemma가 하는 일은 score의 집중(path·root 평균)이라는 정보를, reservoir에 새 섭동 하나를 넣은 효과의 정보로 옮기는 것이다. "Palm"은 원문의 이름이다.
