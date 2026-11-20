# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| XT_FAM | 원문의 입력 | [1,0] | ext | 섭동족 · eq pert:parameters, pert:factor | Mark specification과 type $\nu$ | $\psi_\nu=1+t_\nu g\sigma_i+u_\nu g_0S_0$, $t_\nu=j^{-1}$, $u_\nu\in[j^{-j},2j^{-j}]$ | perturbations.tex 26–72 |
| XT_ERR | 원문의 입력 | [0,0] | ext | score · eq pert:score, pert:error | Score $D_\nu$와 오차 $e_{\nu,N}$ | $e_{\nu,N}=\frac{1}{c_\nu s_N}\mathbb E\big\langle\|D_\nu-\mathbb E\langle D_\nu\rangle\|\big\rangle$ | perturbations.tex 74–101 |
| XT_POIS | 원문의 입력 | [0,0] | ext | Poisson add-one | Poisson 합에서 한 항 꺼내기 | $\mathbb E\sum_{q\le n}F(x_q;\text{나머지})=\lambda\,\mathbb E F(x_{\rm new};\text{전체})$ | perturbations.tex 354–358 |
| XT_INS | 원문의 입력 | [1,0] | ext | Lemma tree:insertion · eq tree:density | 삽입 후 tree 밀도 $W_{\mathcal T}(A)$ | $W_{\mathcal T}(A)=\prod_{a\in\mathrm{Leaves}}A^a\prod_{\beta\in\mathrm{Int}}Y_\beta^{\gamma_\beta}$ | trees.tex 84–110 |
| XT_EXP | 원문의 입력 | [2,0] | ext | Lemma tree:extension-expansion | Canceled-anchor expansion | $\partial_{t_1}\cdots\partial_{t_k}E^{A_{\boldsymbol t}}_{\mathcal T}\frac{H}{A^{a_*}_{\boldsymbol t}}\Big\|_0=\sum_Ec_E\,E_{\mathcal T_E}\big[H\prod_jD_j^{a_j(E)}\big]$ | trees.tex 278–300 |
| XT_SEL | 원문의 입력 | [0,0] | ext | Lemma pert:selection (진술만) | 결정적 매개변수 수열 | $N_j\uparrow\infty$, $\mathbf u_j$: (ii) $e_{\nu,N_j}(\mathbf u_j)\to0$ · (iii) 유한 tree moment 수렴 | perturbations.tex 255–306 |
| XT_DEF | 원문의 입력 | [2,0] | ext | 정의 · 색, constraint, $R_E$ | Anchor 종류, 색, constraint, $R_E$ | spin anchor: $R_E=\frac1N\sum_i\sigma_i^{a_*}\prod_j\sigma_i^{a_j(E)}$ · marker anchor: $R_E=\frac1N\sum_i\prod_j\sigma_i^{a_j(E)}$ | perturbations.tex 427–450 |
| XT_SCORE | X_TI · Thm pert:tree-identity의 증명 | [0,1] | 보통 | 단계 0 · eq pert:score-identity | Score와 $f$의 분리 | $\Big\|\frac{\mathbb E[fD_\nu^{a_*}]-\mathbb Ef\,\mathbb E\langle D_\nu\rangle}{c_\nu s_N}\Big\|\le\\|f\\|_\infty e_{\nu,N}$ | perturbations.tex 308–325 |
| XT_HDEF | X_TI · Thm pert:tree-identity의 증명 | [1,1] | 보통 | 정의 · eq pert:palm-expression, pert:analytic-difference | 삽입 함수 $J$와 차 $H_N(t,u)$ | $J_{N,\mathcal T}=\mathbb E\big[f\,\frac{g_0^{a_*}S_0^{a_*}}{A^{a_*}}W_{\mathcal T}(A)\big]$, $H_N=J_{N,\mathcal T}-\mathbb Ef\,J_{N,\{a_*\}}$ | perturbations.tex 327–348 |
| XT_PALM | X_TI · Thm pert:tree-identity의 증명 | [0,2] | 보통 | 단계 1 · Lemma pert:palm | Palm: score를 삽입으로 | $\|H_N(t_\nu,u_\nu)\|\le\\|f\\|_\infty e_{\nu,N}$, 모든 $j$에 같은 $H_N$ | perturbations.tex 350–381 |
| XT_ANA | X_TI · Thm pert:tree-identity의 증명 | [1,2] | 보통 | 단계 2 · Taylor 계수의 꼴 | $H_N(t,0)\to H(t)$, 원판 위에서 균일 | $[t^q]H_N(t,0)$ = 유한 tree multioverlap moment(와 두 moment의 곱)의 $N$ 무관 선형결합 | perturbations.tex 389–409 |
| XT_VAN | X_TI · Thm pert:tree-identity의 증명 | [1,3] | 보통 | 단계 3 · Lemma pert:analytic | 모든 Taylor 계수가 0으로 | $\|H(j^{-1})\|\le2Cj^{-j}$ $\Rightarrow$ $H\equiv0$ $\Rightarrow$ $[t^q]H_N(t,0)\to0$ | perturbations.tex 383–425 |
| XT_K0 | X_TI · Thm pert:tree-identity의 증명 | [0,4] | 보통 | $k=0$ 경우 | 추가 색이 없으면 상수항 | $\mathbb E[fR_{\{a_*\}}]-\mathbb Ef\,\mathbb ER_{\{a_*\}}\to0$ (marker anchor는 자명) | perturbations.tex 473–474 |
| XT_POL | X_TI · Thm pert:tree-identity의 증명 | [1,4] | 보통 | 단계 4 · polarization | 한 방향에서 여러 방향으로 | $\partial_{z_1}\cdots\partial_{z_k}=\frac{k^k}{2^kk!}\sum_{\epsilon\in\{\pm1\}^k}\big(\prod_j\epsilon_j\big)Q_N\big(k^{-1}\sum_j\epsilon_jg_j\big)\to0$ | perturbations.tex 475–494 |
| XT_MSEL | X_TI · Thm pert:tree-identity의 증명 | [2,1] | 보통 | eq pert:mark-selector | Mark selector: 부호로 공유 꼭짓점 고르기 | $\mathbb E_{\rm marks}\big[g_0^{a_*}\prod_jg_j^{a_j(E)}\big]=\prod_{(a,b,d)}\mathbf 1_{\{a,b\ \text{깊이 }d\text{ 꼭짓점 공유}\}}$ | perturbations.tex 496–514 |
| XT_SHAPE | X_TI · Thm pert:tree-identity의 증명 | [2,2] | 보통 | 정확한 갈라짐 | $H_d-H_{d+1}$로 모양 고르기 | $\mathbf 1\{a,b\text{가 정확히 깊이 }d\text{에서 갈라짐}\}=H_d(a,b)-H_{d+1}(a,b)$, $H_0=1$, $H_L=0$ | perturbations.tex 516–525 |
| XT_ASM | X_TI · Thm pert:tree-identity의 증명 | [1,5] | 보통 | 단계 5 · 조립 | 전개, selector, site 평균 | $\sum_{E\in\mathfrak E(\mathcal T,a_*,\mathcal C)}c_E\,\mathbb E[fR_E]-\mathbb Ef\sum_{E\in\mathfrak E(\{a_*\},a_*,\mathcal C)}c_E\,\mathbb E[R_E]$ = 혼합 계수 차의 선형결합 | perturbations.tex 527–536 |
| XT_EQ | X_TI · Thm pert:tree-identity의 증명 | [1,6] | key | eq pert:tree-identity-eq | Prescribed tree 위의 항등식 | $\sum_{E\in\mathfrak E(\mathcal T,a_*,\mathcal C)}c_E\,\mathbb E[fR_E]-\mathbb Ef\sum_{E\in\mathfrak E(\{a_*\},a_*,\mathcal C)}c_E\,\mathbb E[R_E]\longrightarrow0$ | perturbations.tex 452–470, 531–533 |
| XT_U | X_TI · Thm pert:tree-identity의 증명 | [1,7] | 보통 | → X_TI (부모 지도) | 쓰임: 부모 지도의 X_TI | A_ERR, P_1, P_IND, T_S, T_SIDES에 입력 | perturbations.tex 452–470 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | XT_ERR | XT_SCORE | $e_{\nu,N}$ 정의 | key |
| 1 | XT_INS | XT_HDEF | $W_{\mathcal T}(A)$ | 입력 |
| 2 | XT_FAM | XT_HDEF | $A=1+tg\sigma_i+ug_0S_0$ | 입력 |
| 3 | XT_SCORE | XT_PALM | score 경계 | key |
| 4 | XT_HDEF | XT_PALM | $J$, $H_N$ | key |
| 5 | XT_POIS | XT_PALM | 항 하나 꺼내기 | 입력 |
| 6 | XT_INS | XT_PALM | $A^{a_*}$ 소거 | 입력 |
| 7 | XT_SEL | XT_SCORE | (ii) $e_\nu\to0$ | 입력 |
| 8 | XT_HDEF | XT_ANA | $H_N(t,0)$ | key |
| 9 | XT_EXP | XT_ANA | 해석적 경계, 유한 extension | 입력 |
| 10 | XT_SEL | XT_ANA | (iii) moment 수렴 | 입력 |
| 11 | XT_PALM | XT_VAN | $\|H_N(j^{-1},u_\nu)\|\to0$ | key |
| 12 | XT_ANA | XT_VAN | $H_N\to H$ 해석적 | key |
| 13 | XT_FAM | XT_VAN | $u_\nu\le2j^{-j}$ | 입력 |
| 14 | XT_VAN | XT_K0 | 상수 계수 | 입력 |
| 15 | XT_VAN | XT_POL | 차수 $k$ 계수 $\to0$ | key |
| 16 | XT_FAM | XT_POL | 유리 평균도 mark 족 | 입력 |
| 17 | XT_FAM | XT_MSEL | Rademacher 좌표 | 입력 |
| 18 | XT_DEF | XT_MSEL | 색과 split depth | 입력 |
| 19 | XT_MSEL | XT_SHAPE | $H_d$ | 입력 |
| 20 | XT_POL | XT_ASM | 혼합 미분 $\to0$ | key |
| 21 | XT_EXP | XT_ASM | 혼합 전개 $\sum_Ec_E$ | 입력 |
| 22 | XT_SHAPE | XT_ASM | $\mathcal C$ 만족 history만 | key |
| 23 | XT_DEF | XT_ASM | $R_E$ | 입력 |
| 24 | XT_ASM | XT_EQ | $k\ge1$ | key |
| 25 | XT_K0 | XT_EQ | $k=0$ | 입력 |
| 26 | XT_EQ | XT_U | X_TI | key |
