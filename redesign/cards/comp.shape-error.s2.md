---
id: comp:shape-error.s2
kind: step
title: '극한 순서: 고정 $\eta$ 에서 $N$, 그다음 $L$, 마지막에 $\eta\downarrow0$'
uses: [comp:shape-error-bound, decor:overlap-concentration, x:decor-limit-order, x:comp-standing]
provides: 'comp:shape-error의 결론'
math: |
  decor:overlap-concentration을 먼저 고정한 $\eta$ 에서, 고정 $L$ 의 $N$ 극한을 $L\to\infty$ 보다 먼저 취해 적용하고, 그다음 $\eta\downarrow0$ 으로 보내 (comp:shape-error)를 얻는다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [153, 156]}
status: proposed
---

**풀어 쓴 극한 (작성자).** (comp:shape-error-bound)의 좌변을 $\Sigma_{L,N}$ 라 하자. 좌변은 $\eta$ 에 의존하지 않는다. 고정 $\eta$, 고정 $L$ 에서 선택된 수열을 따라
$$\limsup_N\Sigma_{L,N}\le C_k\Bigl(\eta+L^{-1}+\sum_{U\in\mathfrak S_k}\bigl(\limsup_N\mathcal A_{L,\eta}\operatorname{Var}(R_U)\bigr)^{1/2}\Bigr).$$
[[decor:overlap-concentration]]은 각 $U$ 에서 $\lim_L\limsup_N\mathcal A_{L,\eta}\operatorname{Var}(R_U)=0$ 을 준다(singleton은 각 고정 $L$ 에서 이미 0). $\mathfrak S_k$ 가 유한하므로 $\limsup_L\limsup_N\Sigma_{L,N}\le C_k\eta$. $C_k$ 가 $\eta$ 에 무관하므로 $\eta\downarrow0$ 으로 0. 두 정리의 안쪽 수열이 같은 것은 둘 다 고정 $L$ (과 고정 $\varepsilon$)의 pert:selection 수열이기 때문이다([[x:decor-limit-order]], [[x:comp-standing]]). decor:overlap-concentration은 모든 $\eta>0$ 에 대한 것이므로 $0<\eta<1/2$ 에 적용된다.

**ID.** 첫 단계는 원문의 식 라벨 `comp:shape-error-bound` 를 ID로 쓰므로 이 둘째 단계가 `.s2` 이고 `.s1` 은 없다(검토 2 comp·reduction F5 대응으로 `.s1` 에서 바꿈).
