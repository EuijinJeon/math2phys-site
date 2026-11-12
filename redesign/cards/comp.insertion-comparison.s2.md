---
id: comp:insertion-comparison.s2
kind: step
title: '개수 절단 $K\le M$ 과 정규화 $A=z(1+D)$, $\lvert D\rvert\le c<1$'
uses: [comp:insertion-comparison.s1.s1, x:cavity-bounded, cavity:increment, tree:Y-recursion, tree:insertion]
provides: 'comp:insertion-comparison.s3 (log 전개를 적용할 꼴), s4 (절단 $M$)'
math: |
  두 삽입 가운데 하나를 생각하고, 먼저 그 Poisson 개수 $K$ 를 고정한 $M$ 에 대해 $K\le M$ 으로 제한한다. $C=H+BM$, $z=\cosh C$, $c=\tanh C<1$ 로 둔다. 이 사건 위에서 reservoir 삽입과 그 trial 판은 둘 다 모든 disorder와 path 변수에 균일하게
  $$A=z(1+D),\qquad\lvert D\rvert\le c$$
  로 쓸 수 있다. 결정적인 항 $\log z$ 는 비교에서 지워진다.
physics: null
gap: null
abstraction: blackbox
children: []
source:
  - {file: comparison.tex, lines: [198, 203]}
status: proposed
---

**확인 (작성자).** [[x:cavity-bounded]]($B(\theta)\le B$, $\lvert h\rvert\le H$)로 $K\le M$ 위에서 $\lvert\log A_{\rm s}\rvert\le H+BK_{\rm s}\le C$, $\lvert\log A_{\rm b}\rvert\le BK_{\rm b}\le C$ 이고 trial 판도 같다(spin 값만 바뀐다). 그러면 $e^{-C}\le A\le e^C$ 이고 $D=A/z-1\in[e^{-C}/\cosh C-1,\ e^C/\cosh C-1]=[-\tanh C,\tanh C]$.

$\log z$ 가 지워지는 것: recursion은 결정적 양의 상수에 대해 동차이므로 $\log Y_0(z(1+D))=\log z+\log Y_0(1+D)$ 이고 양쪽에 같은 $\log z$ 가 붙는다. reservoir 쪽에서는 [[tree:insertion]]의 동차성("root-가측인 양의 상수를 곱하면 모든 $Y_d$ 가 그 상수배")이고, trial 쪽에서는 (tree:Y-recursion)의 정의에서 바로 나온다(작성자 읽기; 원문은 근거를 적지 않는다). 절단 사건 $\{K\le M\}$ 은 root(새 insertion disorder)의 사건이라 root가 주어진 조건부 log 전개와 충돌하지 않는다.
