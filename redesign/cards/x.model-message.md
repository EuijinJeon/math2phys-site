---
id: x:model-message
kind: definition
title: 'message $x$ 와 $q_x$; site 항과 edge 항의 뜻'
uses: []
provides: 'model:edge, model:site-message, model:chain의 $x$. upper.tex의 $\bar f(x)=\sum_sf(s)q_x(s)$, comparison.tex의 $x=\operatorname{arctanh}\langle\sigma_i\rangle$'
math: |
  여기서 주는 것은 Panchenko–Talagrand functional([PT04, Section 5])의 power-mean 꼴이다. message $x$ 는 spin 하나 위의 확률분포를 정한다: $x\in\mathbb R$ 에 대해
  $$q_x(s)=\frac{e^{xs}}{2\cosh x}\qquad(s=\pm1).$$
  site 항은 새 spin 하나를 그에 붙은 상호작용들과 함께 넣고, edge 항은 그 삽입에서 센 상호작용을 보정한다.
physics: |
  $x$ 는 역온도 단위의 cavity field([[g:message]])이고 $q_x$ 는 그 field 아래 spin 하나의 분포, $\langle s\rangle_{q_x}=\tanh x$ 이다. site 항과 edge 항은 Bethe free entropy의 site 항과 factor 항([[g:site-term]], [[g:edge-term]])이다.
gap: |
  여기의 $x$ 는 실제 계에서 계산한 cavity field가 아니라 임의의 시행 법칙(model:chain)에서 뽑은 변수다. moment 조건도 없다(model:trial-bounds). "그 삽입에서 센 상호작용을 보정한다"("corrects for interactions counted in that insertion")는 원문의 설명 문장(model.tex 50–52)이고 정의의 일부가 아니다. 이것을 "중복으로 센" 상호작용의 보정으로 읽는 것은 작성자의 읽기다(셈은 model:functional의 차이 칸).
abstraction: exact
children: []
source:
  - {file: model.tex, lines: [46, 54]}
status: proposed
---

$s=\pm1$ 에서 $q_x(1)+q_x(-1)=1$ 이므로 $q_x$ 는 확률분포이고, $x\mapsto q_x$ 는 $\{-1,1\}$ 위의 완전히 양인 분포 전체와 일대일이다($x=\pm\infty$ 의 결정적 spin은 빠진다). 이 마지막 관찰은 작성자가 보탠 것이다.
