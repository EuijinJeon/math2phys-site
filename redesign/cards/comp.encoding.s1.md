---
id: comp:encoding.s1
kind: step
title: '균일 site를 root에 넣고 깊이 $r$ 의 field $x=\operatorname{arctanh}\langle\sigma_i\rangle$'
uses: [x:comp-standing, cavity:increment, x:cavity-tree-sampling, x:tree-extra-variables, tree:original-tilt, x:tree-path-kernels, x:tree-sampling, x:model-message]
provides: 'comp:encoding.s2 ($x$ 와 $\mathscr G_d$), comp:encoding.s3 (terminal spin의 조건부 법칙 $q_x$)'
math: |
  독립 균일 site $i\in[N]$ 를 reservoir root disorder와 함께 root 변수에 넣는다. tilted reservoir 보조 kernel로 각 path를 뽑고, $\mathscr G_d$ 를 이 넓힌 root와 깊이 $d$ 까지의 보조 prefix 전체가 생성하는 $\sigma$-field라 하자. 깊이 $r=L-1$ 에서
  $$x=\operatorname{arctanh}\langle\sigma_i\rangle$$
  로 둔다. 괄호는 leaf Gibbs 기대값이다. 유한 $N$ 에서 모든 배치의 무게가 엄격히 양이므로 $-1<\langle\sigma_i\rangle<1$ 이고 $x$ 는 유한하다. 따라서 $x$ 는 깊이 $L$ 의 terminal spin 전이 전에, 깊이 $r$ 에서 정해진다. 각 terminal replica leaf에서 법칙 $q_x$ 로 spin을 뽑는다. 보조 prefix가 주어지면 이 spin들은 독립이고, 독립인 terminal Gibbs replica들의 one-site 법칙과 정확히 같다.
physics: |
  site $i$ 를 무작위로 고른 뒤, 깊이 $r$ [[g:state|상태]](보조 prefix)가 주어졌을 때의 국소 자화 $\langle\sigma_i\rangle$ 을 [[g:message|cavity field]] $x$ 로 쓴다. 그 상태 안의 [[g:replica|replica]]들이 site $i$ 에서 보는 spin은 평균 $\tanh x$ 의 독립 Ising spin이다.
gap: |
  "one-site 법칙이 같다"는 site $i$ 하나의 spin에 대한 것이다. 같은 prefix 아래 독립 Gibbs replica들의 site $i$ spin이 독립인 것은 tree 표본 규칙(깊이 $L$ 의 서로 다른 자식은 독립)에서 온다. 여러 site의 결합 법칙은 여기서 다루지 않는다. 상태는 섭동 reservoir의 보조 계층 prefix다.
abstraction: exact
children: []
source:
  - {file: comparison.tex, lines: [27, 43]}
status: proposed
---

$q_x(s)=e^{xs}/(2\cosh x)$ 의 평균은 $\tanh x=\langle\sigma_i\rangle$ 이므로 Ising spin 하나의 법칙은 평균으로 정해진다(작성자 확인). 균일 site를 root에 넣는 것은 [[x:tree-extra-variables]]의 "추가 root 변수는 quenched로 남는다"는 약속에 맞다: 원래의 backward logarithm이 $i$ 에 의존하지 않으므로 tilt가 바뀌지 않는다(작성자 읽기, 원문은 이 점을 적지 않는다). "tilted reservoir auxiliary kernels"는 [[x:cavity-tree-sampling]]의 약속(하한의 모든 spin tree는 이 reservoir에서 뽑는다)과 [[tree:original-tilt]]의 kernel이다. leaf Gibbs 기대값은 깊이 $L-1$ 까지의 prefix가 주어진 [[tree:original-tilt]]의 $K_L$ 아래 기대값이다.
