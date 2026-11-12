---
id: comp:encoding.s3
kind: step
title: 'branching pattern마다의 확인: backward recursion $G_T(\eta_d)$'
uses: [comp:encoding.s1, comp:encoding.s2, x:tree-sampling, x:model-message, model:chain]
provides: 'comp:encoding.s4 (모든 descendant tree의 결합 출력 법칙 보존)'
math: |
  descendant tree $T$ 를 고정하고 각 terminal leaf에 spin $e_a$ 를 처방한다. 깊이 $r$ 에서 그 조건부 확률은 $G_T(x)=\prod_aq_x(e_a)$ 이다. 깊이 $d<r$ 에서 $T_1,\ldots,T_j$ 를 그 자식들에 뿌리를 둔 부분 tree라 하자. 자식들의 조건부 독립이 backward recursion
  $$G_T(\eta_d)=\prod_{\ell=1}^j\int G_{T_\ell}(\nu)\,\eta_d(d\nu)$$
  를 준다. 귀납으로 이 확률은 prefix 전체에 $\eta_d$ 를 통해서만 의존한다. 그러므로 거꾸로 쌓은 측도들은 unary 구간과 임의의 자식 수를 포함한 모든 descendant tree의 결합 출력 법칙을 보존한다. 이 recursion은 정확히 (2.7)의 branching 판이다.
physics: |
  [[g:replica|replica]]들이 [[g:hierarchy|보조 계층]]에서 어떻게 갈라지든(어느 깊이에서 몇 갈래로), 그 replica들이 site $i$ 에서 보는 spin의 결합 법칙은 깊이마다 "자식 [[g:state|상태]]들에 딸린 다음 단계의 field 법칙 $\eta_{d+1}$(마지막 단계에서는 field $x$)이 서로 독립으로 같은 법칙 $\eta_d$ 에서 뽑힌다"는 계층 cavity field 사슬로 그대로 재현된다.
gap: |
  정확한 진술이다. 다만 재현되는 것은 한 site의 replica 결합 법칙이고, 계층은 보조 계층이다. 물리의 계층 cavity field 사슬과 같은 꼴이라는 것이 여기서 정의로 맞춰진 것이지, [[g:physical-pure-state|물리적 pure state]]의 계층이 유도된 것은 아니다. $\eta_d$ 에서 뽑히는 것은 자식 prefix 자체가 아니라 그 prefix의 함수인 $\eta_{d+1}$ 이다(자식 prefix는 tilted reservoir kernel로 뽑힌다; comparison.tex 29–30, 44–48, 61–67).
abstraction: exact
children: []
source:
  - {file: comparison.tex, lines: [58, 72]}
status: proposed
---

**귀납의 한 걸음 (작성자가 풀어 씀).** 깊이 $d+1$ 의 자식 vertex $\ell$ 에서 귀납 가정으로 부분 tree $T_\ell$ 의 조건부 출력 확률은 $G_{T_\ell}(\eta_{d+1}^{(\ell)})$ 이다($d+1=r$ 이면 $\eta$ 대신 $x$, 그리고 그때의 "측도"는 $\eta_{r-1}$). 자식들은 $\mathscr G_d$ 가 주어지면 조건부 독립이고([[x:tree-sampling]] "distinct children are sampled independently"), 각 자식의 $\eta_{d+1}^{(\ell)}$ 의 조건부 법칙이 정의상 $\eta_d$ 이므로([[comp:encoding.s2]]) 조건부 확률이 $\prod_\ell\int G_{T_\ell}\,d\eta_d$ 이다. 이 값은 $\eta_d$ 만의 함수다.

**(2.7)과의 대응.** [[model:chain]]의 사슬 $\eta_{d+1}\mid\eta_d\sim\eta_d$, $x\mid\eta_{r-1}\sim\eta_{r-1}$ 는 label 하나의 path 하나를 정한다. 여러 replica가 prefix를 공유하며 깊이 $d$ 에서 갈라지면 각 가지가 $\eta_d$ 에서 독립으로 다음 측도를 뽑는다. 위 recursion은 그 tree판 확률이다. trial 쪽 tree의 표본 법칙이 이렇게 정해진다는 것은 원문이 "branching version"이라고만 쓰고 따로 정의하지 않는다(작성자 읽기: trial 사슬을 [[x:tree-path-kernels]]의 path kernel 열로 보고 [[x:tree-sampling]] 규칙을 적용한 것, trees.tex 26–27).
