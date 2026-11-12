---
id: pert:selection
kind: lemma
title: '결정적 매개변수 선택 (Lemma 6.2)'
uses: [x:pert-increment, pert:error, pert:concentration, x:pert-parameter-measure, x:pert-standing, cavity:negligible, cavity:increment, tree:multioverlap, x:tree-sampling]
provides: '§6: x:pert-selected-limits, pert:score-identity, pert:analytic (iii), pert:tree-identity. §7: x:decor-limit-order, x:decor-mesh, decor:section (decorrelation.tex 4–9). §8: comparison.tex 8–15 (comp:low-increments = (i)), 20 (선택된 매개변수 벡터), 130, 243. overview.tex 18. 규칙 P5, L1 수 3'
math: |
  고정한 모든 $L\ge2$ 와 $\varepsilon>0$ 에 대해, 크기 $N_j\uparrow\infty$ 와 결정적 벡터 $\mathbf u_j$ 가 있어 다음이 성립한다.
  (i) $\Delta_{N_j}(\mathbf u_j)\le\underline F+2\varepsilon$;
  (ii) 모든 고정 type $\nu$ 에 대해 reservoir에서 $e_{\nu,N_j}(\mathbf u_j)\longrightarrow0$;
  (iii) reservoir에서, 깊이 $L$ 의 모든 고정 유한 prescribed tree 위 multioverlap의 모든 유한곱의 기대값이 이 수열을 따라 수렴한다.
physics: |
  [[x:pert-standing]]의 유계 모형에서, 깊이 $L$ 과 여유 $\varepsilon$ 을 고정할 때마다, 크기들의 수열과 그 크기마다 고정된 [[g:perturbation|섭동]] 매개변수를 골라 (i) [[g:increment|cavity 증분]]이 $\underline F+2\varepsilon$([[g:lower-pressure]]) 이하이고, (ii) [[g:reservoir|reservoir]]에서 각 type의 [[g:score|score]]가 [[g:concentration|집중]]하며, (iii) reservoir의 유한 [[g:prescribed-tree|prescribed tree]] 위 [[g:multioverlap|multioverlap]] moment가 모두 수렴하게 할 수 있다. 이 수열이 [[g:selected-sequence|선택된 수열]]이다.
gap: |
  (1) 존재 진술이다: 크기의 부분수열 하나와 크기마다 매개변수 벡터 하나를 고른다. 모든 $N$ 이나 거의 모든 매개변수에서 성립한다고 말하지 않는다. (2) (ii)는 type마다의 수렴이고 type이나 $L$ 에 균등하지 않다. (3) (i)은 상한뿐이고 증분의 극한이나 $\lim F_N$ 의 존재를 말하지 않는다. (4) (iii)은 수렴만 주고 극한값을 식별하지 않는다(대각 부분수열). (5) 수열은 $L$ 과 $\varepsilon$ 마다 다르다. 물리 그림의 "무한소 섭동으로 generic한 계를 고른다"와의 관계는 [[g:selected-sequence]]의 물리 대응 칸에 intuition으로만 있다. 이 수열은 [[g:state|상태]]가 아니다.
abstraction: weakening
children: [pert:selection.s1, pert:selection.s2, pert:selection.s3]
source:
  - {file: perturbations.tex, lines: [255, 267]}
  - {file: perturbations.tex, lines: [269, 306]}
status: proposed
---

**증명의 뼈대.**
- [[pert:selection.s1]]: [[cavity:negligible]]에서 $\liminf_N\frac1N\int P_N^{L,\mathbf u}\pi(d\mathbf u)=\underline F$. telescoping으로 $\int\Delta_N\,d\pi\le\underline F+\varepsilon$ 인 $N$ 이 무한히 많다. [[cavity:increment]]가 $|\Delta_N|\le C$ 를 준다.
- [[pert:selection.s2]]: 그 $N$ 들 가운데 $\sum_{\nu\le j}\int e_{\nu,N_j}\,d\pi\le j^{-3}$ 이 되게 $N_j$ 를 고르고(pert:concentration), Markov로 좋은 집합 $G_j$ 의 여집합 측도가 $j^{-2}$ 이하. $G_j$ 위 조건부 평균 증분이 $\underline F+2\varepsilon$ 이하이므로 그 안에서 한 점 $\mathbf u_j$ 를 고른다.
- [[pert:selection.s3]]: 고정 $L$ 의 유한 tree moment는 가산 개이고 유계라 대각 부분수열로 (iii).

**두 평균의 구별.** $\pi$ 에 대한 적분은 s1, s2에서 점 $\mathbf u_j$ 를 고르는 데만 쓰인다. 결론 (i)–(iii)은 모두 고른 점 $\mathbf u_j$ 를 고정한 값이다: (i)의 $\Delta_{N_j}(\mathbf u_j)$, (ii)의 $e_{\nu,N_j}(\mathbf u_j)$, (iii)의 기대값은 그 벡터에서 [[g:root]]와 tree 표본에 대해서만 평균한다([[x:pert-standing]] 9–10행).

**양화사와 극한.** "for every fixed type $\nu$, $e_{\nu,N_j}(\mathbf u_j)\to0$"은 $\nu$ 를 고정하고 $j\to\infty$ 한 것이다. type에 균등한 수렴은 주지 않는다(s2에서 $j\ge\nu$ 부터 $e_{\nu,N_j}\le j^{-1}$). (ii)와 (iii)은 "in the reservoir"이고 (i)은 $N$-spin 계와 $(N+1)$-spin 계의 증분이다. 규칙 P5가 이 lemma를 blackbox로 쓴다.
