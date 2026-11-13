---
id: comp:encoding
kind: lemma
title: 'Recursive law encoding (재귀적 법칙 부호화)'
uses: [x:comp-standing, pert:selection, cavity:increment, x:cavity-tree-sampling, x:tree-path-kernels, x:tree-sampling, tree:original-tilt, x:tree-extra-variables, tree:multioverlap, model:chain, x:model-message, x:pert-mark-specification, pert:factor]
provides: 'comp:patterns (trial label의 pattern 분포 $\bar\pi=\mathbb E\pi$, comp:single-label-moments), comp:insertion-comparison (독립 trial spin 과정과 trial kernel), comp:bounded-lower.s1 ($\zeta_{L,N}\in\mathcal M_L$ 이므로 시행값이 $\inf_r\Phi_r$ 이상). 규칙 P10, L1 수 6'
math: |
  고정한 각 $N$, $L\ge2$, 선택된 매개변수 벡터에 대해, reservoir root disorder를 평균하면 결정적 시행 법칙 $\zeta_{L,N}\in\mathcal M_L$ 이 있어, 그 label 하나의 spin 과정이 모든 prescribed tree 위에서 reservoir의 균일하게 고른 site와 같은 기대 spin 곱을 갖는다. 서로 다른 trial label은 독립으로 고를 수 있다.
physics: |
  고정한 $N$, $L\ge2$, 선택된 섭동 매개변수마다, [[g:reservoir|reservoir]]에서 균일하게 고른 site $i$ 의 [[g:message|cavity field]] $x=\operatorname{arctanh}\langle\sigma_i\rangle$ (깊이 $r=L-1$ 까지의 [[g:state|상태]]가 주어졌을 때의 자화)의 조건부 법칙을 깊이 방향으로 거꾸로 쌓으면 $(L-1)$단 시행 [[g:order-parameter|order parameter]] $\zeta_{L,N}$([[g:encoded-law]])이 되고, 그 label 하나는 모든 [[g:prescribed-tree|prescribed tree]] 위에서 reservoir와 같은 spin 곱 기대값 $\mathbb ER_S$ 를 갖는다($\zeta_{L,N}$ 은 reservoir의 root disorder를 평균한 결정적 법칙이다). 서로 다른 label은 독립으로 고를 수 있다.
gap: |
  (1) 부호화 자체는 정확하다. 다만 "상태"와 깊이는 섭동 [[g:mark|mark]]로 만든 [[g:hierarchy|보조 계층]]의 것이고, $\zeta_{L,N}$ 을 계의 [[g:physical-pure-state|물리적 pure state]] 계층에 따른 order parameter로 읽는 것은 증명되지 않는다(g:encoded-law의 물리 대응 칸, intuition). (2) $\zeta_{L,N}$ 은 $N$, $L$, 선택된 $\mathbf u$ 에 의존하고 극한 order parameter가 아니다. Parisi parameter는 최적화하지 않는다(비교에서 $m_d=d/L$). (3) 보존되는 것은 label **하나**의 tree별 기대 spin 곱, 곧 root disorder와 균일 site를 평균한 한 site의 결합 법칙이다. 서로 다른 label은 reservoir 전체의 독립 사본에서 오므로, reservoir의 여러 site의 결합 법칙은 보존되지 않는다. 그 차이는 comp:patterns가 다룬다.
abstraction: exact
children: [comp:encoding.s1, comp:encoding.s2, comp:encoding.s3, comp:encoding.s4]
source:
  - {file: comparison.tex, lines: [17, 25]}
  - {file: comparison.tex, lines: [27, 83]}
status: proposed
---

**증명의 뼈대.**
- [[comp:encoding.s1]]: 균일 site $i$ 를 root에 넣고, tilted reservoir kernel로 path를 뽑아 $\mathscr G_d$ 를 만든다. 깊이 $r$ 에서 $x=\operatorname{arctanh}\langle\sigma_i\rangle$ 은 유한하고, terminal spin은 $q_x$ 로 뽑아도 된다.
- [[comp:encoding.s2]]: $\eta_{r-1}=\operatorname{Law}(x\mid\mathscr G_{r-1})$, $\eta_d=\operatorname{Law}(\eta_{d+1}\mid\mathscr G_d)$ 로 거꾸로 쌓아 $\zeta_{L,N}=\operatorname{Law}(\eta_0)\in\mathcal M_L$.
- [[comp:encoding.s3]]: 임의의 descendant tree에서 $G_T(\eta_d)=\prod_\ell\int G_{T_\ell}(\nu)\,\eta_d(d\nu)$ 의 귀납으로 결합 출력 법칙이 $\eta_d$ 만으로 정해짐을 보인다. 이것이 (2.7)의 branching 판이다.
- [[comp:encoding.s4]]: (comp:single-label-moments) $\mathbb E\prod_{a\in S}\tau^a=\mathbb ER_S$, 그리고 label마다 전체 구성의 독립 사본.

**평균의 종류.** 진술의 "reservoir root disorder averaged"는 $\zeta_{L,N}$ 이 무작위 측도가 아니라 결정적 법칙이 되게 한다: root(물리 disorder, 섭동 개수·type·site, 그리고 새로 넣은 균일 site $i$)는 $\eta_0$ 의 무작위성 안으로 들어가고, $\zeta_{L,N}$ 은 그 법칙이다. 섭동 매개변수는 선택된 값 $\mathbf u_{L,N}$ 으로 고정되고 평균하지 않는다([[x:comp-standing]]). $\langle\cdot\rangle$ 은 보조 prefix가 주어진 leaf Gibbs 기대값이다([[g:root]]의 §8 문장).

**물리판과의 대조.** 물리의 cavity 방법은 이웃 site의 cavity field가 "같은 분포를 갖는 독립 변수"라고 가정하고 그 분포를 order parameter로 둔다. 여기서는 분포를 reservoir에서 정확히 만들어 내고, 독립성은 따로 비교한다([[comp:patterns]], [[comp:insertion-comparison]]).
