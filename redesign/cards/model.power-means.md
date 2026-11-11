---
id: model:power-means
kind: definition
title: '조건부 power mean $T_d$ (2.10)'
uses: [model:chain, model:vs, model:ve]
provides: 'model:functional의 $T_0V_{\rm s}$, $T_0V_{\rm e}$. model:trial-bounds. upper.tex(interpolation의 root logarithm), tree:Y-recursion과 cavity.tex의 같은 꼴 재귀, comparison.tex 181–188(독립 label 묶음이 각 power mean을 통과해 인수분해됨)'
math: |
  $0\le d<r$ 에 대해 $\mathscr F_d$ 는 이 식들($V_{\rm s}$, $V_{\rm e}$)의 모든 물리적 disorder와 모든 $\eta^\omega_j$ ($0\le j\le d$) 가 생성하는 $\sigma$-field다.
  $$T_rV=V,\qquad T_dV=\Bigl(\mathbb E\bigl[(T_{d+1}V)^{m_{d+1}}\bigm|\mathscr F_d\bigr]\Bigr)^{1/m_{d+1}}\quad(d=r-1,\ldots,0).\tag{2.10}$$
  이 조건부 기대값에서는 보조 message만 적분된다. 예: 깊이 1($r=1$)에서 $T_0V=(\mathbb E_{\boldsymbol x}[V^{m_1}\mid\boldsymbol\eta_0])^{1/m_1}$. 깊이 2($r=2$)에서는 각 label이 $\eta_0\sim\zeta$, $\eta_1\mid\eta_0\sim\eta_0$, $x\mid\eta_1\sim\eta_1$ 을 뽑고
  $$T_0V=\Bigl(\mathbb E_{\boldsymbol\eta_1}\Bigl[\bigl(\mathbb E_{\boldsymbol x}[V^{m_2}\mid\boldsymbol\eta_1]\bigr)^{m_1/m_2}\Bigm|\boldsymbol\eta_0\Bigr]\Bigr)^{1/m_1}.$$
  굵은 기호는 $V$ 안의 모든 message label을 모은 것이고, 두 줄임 표기를 포함해 물리적 disorder는 내내 고정된다.
physics: |
  계층별 [[g:power-mean|power mean]]: 깊이 $d+1$ 의 보조 변수를 $m_{d+1}$ 거듭제곱 평균으로 적분하는 일을 깊이 $r-1$ 부터 0까지 반복한다. 1RSB cavity 계산의 $Z^m$ 재가중(Monasson) 꼴을 계층마다 쓴 것으로 읽을 수 있다. 조건으로 거는 $\mathscr F_d$ 는 시행 사슬의 깊이 $d$ prefix이고, 이 사이트의 [[g:state|상태]]는 바로 이런 prefix를 가리킨다. [[g:disorder|disorder]]는 적분되지 않고 바깥의 $\mathbb E\log$ 가 평균한다.
gap: |
  재가중 읽기는 그림이고 증명에 쓰이지 않는다. 물리에서 이 꼴은 [[g:physical-pure-state|물리적 pure state]] 계층 위의 가중 평균을 적분해 낸 것으로 유도되지만, 논문은 그런 계층을 가정하지 않고 (2.10)을 정의로 둔다. $\eta_0$ 은 어떤 $T_d$ 로도 적분되지 않고 $\mathscr F_0$ 에 들어 있어 바깥 $\mathbb E$ 가 평균한다.
abstraction: intuition
children: []
source:
  - {file: model.tex, lines: [90, 110]}
status: proposed
---

$m_{d+1}\in(0,1)$ 이고 $T_{d+1}V>0$ 이므로 조건부 기대값은 양의 (무한일 수도 있는) 값으로 잘 정의된다. 실제로는 model:trial-bounds의 곱셈적 상·하한 때문에 유한하다. 이 관찰은 작성자가 보탠 것이다.

$V$ 가 $V_{\rm s}$ 일 때 $k$ 는 $\mathscr F_0$ 에 들어 있는 물리적 disorder이므로 $V_{\rm s}$ 안의 label 수는 $\mathscr F_0$-가측이다.
