---
id: pert:tree-identity.s4
kind: step
title: '조립: 혼합 전개, mark 평균, site 평균'
uses: [pert:tree-identity.s1, pert:tree-identity.s2, pert:tree-identity.s3, pert:analytic, pert:analytic-difference, tree:extension-expansion, x:pert-colored-extensions]
provides: 'pert:tree-identity의 결론 (6.17)'
math: |
  마지막으로 혼합 canceled-anchor 전개를 차 (6.15)에 적용하고, selector를 써서 mark를 평균하고, 독립 균일 insertion site를 평균한다. 마지막 평균이 정확히 $R_E$ 다. pert:analytic과 polarization이 계수 차를 0으로 보내 (6.17)을 낳는다. 유한 일차결합이 결론을 overlap 단항식에서 진술된 시험함수로 넓힌다. 이 구성은 깊이 $L-1$ 까지의 mark만 쓴다: 확장 규칙은 anchor나 이미 쓴 color를 다시 쓰지 않으므로 깊이 $L$ 에서의 일치 검사가 필요 없다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: perturbations.tex, lines: [526, 536]}
status: proposed
---

풀이(작성자). [[tree:extension-expansion]]을 $D_j=g_j\sigma_i$ 로 쓰면 혼합 도함수의 old tree 쪽은 $\sum_Ec_E\mathbb E[fg_0^{a_*}S_0^{a_*}\prod_jg_j^{a_j(E)}\sigma_i^{a_j(E)}]$ 이고, mark 평균이 [[pert:tree-identity.s2]]의 지시함수를 곱해 허용 history $\mathfrak E(\mathcal T,a_*,\mathcal C)$ 만 남기며, site 평균이 $S_0^{a_*}\prod_j\sigma_i^{a_j(E)}$ 를 $R_E$ 로 바꾼다([[x:pert-colored-extensions]]). anchor 하나 쪽도 같다. 그래서 혼합 도함수가 정확히 (6.17)의 좌변(선형결합의 각 항)이고, s1에 의해 0으로 간다. "overlap 단항식에서 시험함수로"는 $f$ 에 대한 선형성이다. 깊이 $L$: 서로 다른 위치에서 $H_L=0$ 이 자동이므로 selector가 필요 없다.
