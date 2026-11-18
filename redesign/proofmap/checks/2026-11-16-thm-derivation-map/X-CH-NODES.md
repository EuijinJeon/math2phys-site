# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| XC_GAMMA | §3 앞부분에서 받는 것 | [0,0] | ext | Lemma tree:insertion | Internal vertex의 지수 $\gamma_\beta$ | $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$ | trees.tex 92–104, 126–131 |
| XC_TEL | §3 앞부분에서 받는 것 | [1,0] | ext | eq tree:telescoping | Telescoping | $\sum_{\beta\in\mathrm{Int}(\mathcal T)}(n_\beta m_{d_\beta+1}-m_{d_\beta})=n$ | trees.tex 204–208 |
| XC_EXT | §3 앞부분에서 받는 것 | [1,0] | ext | §3 extension 규칙 | Canceled-anchor extension rule | old leaf $+1$, fresh at $\beta$: $\gamma_\beta$, $\ c_E=\prod(\text{coefficients})$ | trees.tex 259–296 |
| XC_HYP | §3 Lemma tree:charging · 증명 | [2,1] | 보통 | Lemma tree:charging 가정 | 가정: uniform mesh와 빈 깊이의 target | $m_d=d/L,\ \delta=L^{-1}$; target $b$개의 깊이 $\notin$ old branching depths | trees.tex 393–399, 408–410 |
| XC_UNIT | §3 Lemma tree:charging · 증명 | [0,2] | 보통 | 증명 계산 | Uniform mesh에서의 계수 크기 | $n=1:\ \gamma=-\delta;\qquad j\ge2:\ \|m_d-jm_{d+1}\|=(j-1)m_d+j\delta$ | trees.tex 428–430, 449–453 |
| XC_STEP | §3 Lemma tree:charging · 증명 | [1,2] | 보통 | 증명 1 | 제약 없는 한 걸음의 absolute sum | $\sum_{\text{choices}}\|\text{coef}\|\le 2s\le2(q+k)$ | trees.tex 423–427 |
| XC_UNARY | §3 Lemma tree:charging · 증명 | [0,3] | 보통 | 증명 1 | 정해진 깊이의 unary fresh split만 허용한 걸음 | $\sum\|\text{coef}\|\le s\,\delta\le(q+k)\delta$ | trees.tex 427–430 |
| XC_CREATE | §3 Lemma tree:charging · 증명 | [1,3] | 보통 | 증명 2 | Target vertex마다 자기 생성 걸음 | target $v\mapsto$ 서로 다른 step; 배정 수 $\le k!/(k-b)!$ | trees.tex 432–442 |
| XC_J | §3 Lemma tree:charging · 증명 | [0,3] | 보통 | 증명 4 | Reference 계수 $J$의 하한 | $\|J\|\ge\delta^b\,\eta^{\sum_v(a_v-2)}$ | trees.tex 403–411, 448–453 |
| XC_ABS | §3 Lemma tree:charging · 증명 | [2,4] | 보통 | eq tree:charging-bound | Absolute sum의 $\delta^b$ 경계 | $\sum_{E\text{ allowed}}\|c_E\|\le\frac{k!}{(k-b)!}(q+k)^b\big(2(q+k)\big)^{k-b}\delta^b$ | trees.tex 400–406, 443–447 |
| XC_REL | §3 Lemma tree:charging · 증명 | [2,5] | 보통 | eq tree:relative-charging | 상대 경계: absolute sum $/\|J\|$ | $\frac1{\|J\|}\sum_{E\text{ allowed}}\|c_E\|\le C_{q,k,\eta}$ | trees.tex 408–413, 315–332, 448–454 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | XC_GAMMA | XC_UNIT | $n_\beta=1$이면 $-\delta$ | 입력 |
| 1 | XC_HYP | XC_UNIT | $m_d=d/L$ | 입력 |
| 2 | XC_TEL | XC_STEP | fresh 절대합 $=s$ | 입력 |
| 3 | XC_EXT | XC_STEP | old 선택 $\le s$개, 계수 $1$ | 입력 |
| 4 | XC_UNIT | XC_UNARY | unary 계수 $-\delta$ | 입력 |
| 5 | XC_EXT | XC_CREATE | fresh path는 branching 하나 | 입력 |
| 6 | XC_HYP | XC_CREATE | target 깊이가 old에서 비어 있음 | 입력 |
| 7 | XC_UNIT | XC_J | $j=1$: $\delta$, $j\ge2$: $\ge\eta$ | 입력 |
| 8 | XC_HYP | XC_J | $m_{d_v}\ge\eta$ | 입력 |
| 9 | XC_STEP | XC_ABS | 나머지 $k-b$ 걸음 | key |
| 10 | XC_UNARY | XC_ABS | 지정된 $b$ 걸음 | key |
| 11 | XC_CREATE | XC_ABS | 배정 $\le k!/(k-b)!$ | key |
| 12 | XC_ABS | XC_REL | 분자 $C_{q,k}\delta^b$ | key |
| 13 | XC_J | XC_REL | 분모 $\ge\delta^b\eta^{(\cdot)}$ | key |
