# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| X_TI | 밖에서 받는 것 (§3·§6) | [2,0] | ext | Thm pert:tree-identity | Prescribed tree 위의 항등식 | $\sum_{E}c_E\,\mathbb E[fR_E]$ $\quad-\,\mathbb E f\sum_{E\,\text{(anchor만)}}c_E\,\mathbb E[R_E]\to0$ | perturbations.tex 450–465 |
| X_EXT | 밖에서 받는 것 (§3·§6) | [2,0] | ext | §3 extension 규칙 | Extension 계수 $c_E$ | old leaf 재사용 $+1$, fresh 갈라짐 $-c_\ell$ | trees.tex (extension rule), perturbations.tex |
| X_RT | 밖에서 받는 것 (§3·§6) | [2,0] | ext | Lemma tree:reference-total | Reference 계수의 총합 $\kappa(S)$ | $\kappa(S)=\prod_{v\in\mathrm{Br}(S)}\prod_{j=1}^{a_v-1}(m_{d_v}-j\,m_{d_v+1})$ | trees.tex 337–355 |
| X_CH | 밖에서 받는 것 (§3·§6) | [2,0] | ext | Lemma tree:charging | Fresh split의 상대 비용 | 계수 절대합 $\le C\cdot$ 순 계수 | trees.tex 393– |
| X_SAMP | 밖에서 받는 것 (§3·§6) | [2,0] | ext | §3 tree 표본 규칙 | 잎 제거와 조건부 독립 | 갈라진 뒤 자식들은 prefix가 주어지면 조건부 독립 | trees.tex 38–40 |
| X_MO | 밖에서 받는 것 (§3·§6) | [2,0] | ext | eq tree:multioverlap | Multioverlap | $R_S=\frac1N\sum_{i=1}^N\prod_{a\in S}\sigma_i^a$ | trees.tex 44–47 |
| A_DEF | §7.1 깊이 평균 | [0,1] | 보통 | eq decor:average-definition | 깊이 평균 $\mathcal A_{L,\eta}$ | $\mathcal A_{L,\eta}z=L^{-a}\!\!\sum_{\mathbf q\ \eta\text{-regular}}\! z(\mathbf q)$ | decorrelation.tex 15–37 |
| A_HOL | §7.1 깊이 평균 | [0,2] | 보통 | eq decor:average-holder | 분수 거듭제곱 | $\mathcal A_{L,\eta}(z^\gamma)\le(\mathcal A_{L,\eta}z)^\gamma,\ 0<\gamma\le1$ | decorrelation.tex 38–43 |
| A_CMP | §7.1 깊이 평균 | [0,2] | 보통 | §7.1 두 비교 | 쓰지 않는 좌표, 정수 이동 | 이동: $\eta$-regular $\hookrightarrow$ $\eta/2$-regular | decorrelation.tex 44–47 |
| A_ERR | §7.1 깊이 평균 | [0,1] | 보통 | eq decor:identity-error | 항등식 오차의 유한 최대 | $\varepsilon_{N,L,k}\to0\quad(N\to\infty;\ L,k\ \text{고정})$ | decorrelation.tex 48–58 |
| B_DEF | §7.2 조건부 공분산과 깊이 연속성 | [1,1] | 보통 | eq decor:covariance-definition | 조건부 평균과 제곱 공분산 | $\mu_{d,S}=\mathbb E[A_S\mid\mathscr F_d]$ $v_N(S,d)=\frac1{N^2}\mathbb E\sum_{i,j}\mathrm{Cov}(A_{S,i},A_{S,j}\mid\mathscr F_d)^2$ | decorrelation.tex 86–106 |
| B_CON | §7.2 조건부 공분산과 깊이 연속성 | [1,2] | 보통 | Lemma decor:contractions | 축약과 세 사본 | $\\|(A_S-\mu_{d,S})\cdot B\\|_{L^2}\le v_N(S,d)^{1/4}$ | decorrelation.tex 108–140 |
| B_ME | §7.2 조건부 공분산과 깊이 연속성 | [1,2] | 보통 | eq decor:martingale-energy | Martingale energy | $\sum_t\mathbb E\\|\mu_{t+1,T}-\mu_{t,T}\\|_N^2\le1$ | decorrelation.tex 168–175 |
| B_DC | §7.2 조건부 공분산과 깊이 연속성 | [1,3] | 보통 | Lemma decor:depth-continuity | 깊이에 대한 평균 연속성 | $\mathcal A_{L,\eta}\mathbb E\\|\mu_{d,S^U}-\mu_{d,S}\\|_N^2\le C/L$ | decorrelation.tex 142–230 |
| B_PB | §7.2 조건부 공분산과 깊이 연속성 | [1,3] | 보통 | eq decor:projection-bound | 자식을 평균으로 바꾸는 사영 | $\\|(A_S-a_{S,e})\cdot B\\|_{L^2}\le p_N(S,e)$ | decorrelation.tex 205–230 |
| P_V | §7.3 Proposition: 조건부 decorrelation | [0,4] | 보통 | eq decor:V-definition | 귀납 양 $V_{k,L}(\eta)$ | $V_{k,L}(\eta)=\max_{1\le\|S\|\le k}\limsup_{N}\mathcal A_{L,\eta}v_N(S,d)$ | decorrelation.tex 247–260 |
| P_1 | §7.3 Proposition: 조건부 decorrelation | [0,4] | 보통 | §7.3 잎 하나 | 기저: $V_{1,L}(\eta)\le\delta/\eta$ | $\tfrac12\sum_\ell c_\ell\,\mathbb E(X-X_\ell)^2=\delta\,\mathrm{Var}(X)+o_N(1)$ | decorrelation.tex 262–300 |
| P_IND | §7.3 Proposition: 조건부 decorrelation | [0,5] | 보통 | §7.3 귀납 단계 | 늦춘 두 사본과 세 사본 추정 | $J=\kappa(S^+)^2$, 사영 오차, 귀납 항등식 → $v_N(S,d)$ 추정 | decorrelation.tex 300–490 |
| P_FB | §7.3 Proposition: 조건부 decorrelation | [0,5] | 보통 | eq decor:fiber-bound | Fiber 경계 | $L^{-D}\!\sum_{\mathbf q}w_j(\pi_j\mathbf q)^\gamma$ $\quad\le\big(L^{-D_j}\!\sum_{\mathbf y\ \eta/2}w_j(\mathbf y)\big)^\gamma$ | decorrelation.tex 491–511 |
| P_REC | §7.3 Proposition: 조건부 decorrelation | [0,6] | 보통 | eq decor:induction-recursion | 재귀 부등식 | $V_{k,L}(\eta)\le C_{k,\eta}\big(L^{-1/2}+V_{k-1,L}(\eta/2)^{1/4}\big)$ | decorrelation.tex 512–519 |
| PROP | §7.3 Proposition: 조건부 decorrelation | [0,7] | key | Prop decor:conditional-concentration | 조건부 decorrelation | $\lim_{L\to\infty}\limsup_{N\to\infty}\mathcal A_{L,\eta}v_N(S,d)=0$ | decorrelation.tex 234–245, 520–524 |
| T_S | §7.4 정리의 증명 | [1,4] | key | 증명 1 | Singleton | $\mathbb ER_S^2=(\mathbb ER_S)^2+o_N(1)$ | decorrelation.tex 533–535 |
| T_SET | §7.4 정리의 증명 | [1,4] | key | 증명 2 | $e-1$ 에서의 marker anchor | old tree $=S$, 사본 $S$ 를 anchor에서 $e-1$ 에 갈라 붙임 | decorrelation.tex 537–545 |
| T_C | §7.4 정리의 증명 | [1,5] | key | eq decor:marker-coefficient | Marker 계수 | $C(S,e)=-\delta\,\kappa(S)\neq0$ | decorrelation.tex 545–549 |
| T_SIDES | §7.4 정리의 증명 | [1,6] | key | eq decor:marker-variance-identity | 항등식의 두 쪽 | $C(S,e)\big(\mathbb EM^2-(\mathbb ER_S)^2\big)$ $\quad=C(S,e)\,\mathrm{Var}(M)=o_N(1)$ | decorrelation.tex 550–561 |
| T_VM | §7.4 정리의 증명 | [1,7] | key | eq decor:prefix-projection-concentration | Prefix 사영의 집중 | $\mathrm{Var}(M)\to0\quad(L,S,e\ \text{고정})$ | decorrelation.tex 562–569 |
| T_G | §7.4 정리의 증명 | [1,5] | key | 증명 3 | $G$, $G_-$ 와 사영 경계 | $G=\mathbf1\cdot\prod_j\mu_{e,T_j},\ \ G_-=\mathbf1\cdot\prod_j\mu_{e-1,T_j}$ $\mathbb E(R_S-G)^2\le p_N(S,e)^2$ | decorrelation.tex 571–581 |
| T_ADJ | §7.4 정리의 증명 | [1,6] | key | eq decor:adjacent-prefix-error | 이웃 prefix 오차 | $\mathcal A_{L,\eta}\,\mathbb E(G-G_-)^2\le C_k/L$ | decorrelation.tex 582–590 |
| T_L2 | §7.4 정리의 증명 | [1,6] | key | 증명 4 | 조건부 기대값의 $L^2$ 최적성 | $\mathbb E(R_S-M)^2\le\mathbb E(R_S-G_-)^2$ $\qquad\le2p_N^2+2\,\mathbb E(G-G_-)^2$ | decorrelation.tex 591–596 |
| T_FIB | §7.4 정리의 증명 | [1,7] | key | 증명 5 | $p_N^2$ 의 평균 | $p_N(S,e)^2\le s\sum_j v_N(T_j,e)^{1/2}$ $\limsup_N\mathcal A_{L,\eta}\,p_N^2\le C\,V_{k-1,L}(\eta/2)^{1/2}$ | decorrelation.tex 604–609 |
| T_VAR | §7.4 정리의 증명 | [1,8] | key | eq decor:variance-estimate | 분산 추정 | $\limsup_{N}\mathcal A_{L,\eta}\mathrm{Var}(R_S)$ $\quad\le C_k\big(L^{-1}+V_{k-1,L}(\eta/2)^{1/2}\big)$ | decorrelation.tex 597–603 |
| THM | §7.4 정리의 증명 | [1,9] | goal | Thm decor:overlap-concentration | 모든 multioverlap의 집중 | $\lim_{L\to\infty}\limsup_{N\to\infty}\mathcal A_{L,\eta}\mathrm{Var}(R_S)=0$ 모든 $\eta>0$, 모든 고정 $S$ | decorrelation.tex 63–76, 609–611 |
| REM | §7.4 정리의 증명 | [1,8] | note | Remark decor:order-of-limits | 극한 순서 | $N\to\infty$ 먼저, 그 뒤 평균과 $L\to\infty$ | decorrelation.tex 613–623 |
| OUT | (묶음 없음) | [1,10] | ext | §8 comp:section | 받는 곳: 독립 message 비교 | 이 깊이 평균들이 §8의 비교에 필요하다 | decorrelation.tex 11–13 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | X_MO | B_DEF | $R_S=\mathbf1\cdot A_S$ | 입력 |
| 1 | X_TI | A_ERR | 오차를 유한 모음에서 최대 | 입력 |
| 2 | A_DEF | A_HOL | 질량 ≤ 1 | 입력 |
| 3 | A_DEF | A_CMP | (라벨 없음) | 입력 |
| 4 | B_DEF | B_CON | (라벨 없음) | 입력 |
| 5 | B_DEF | B_ME | $\mu_{t,T}$ 는 martingale | 입력 |
| 6 | B_ME | B_DC | 깊이에 대해 더함 | 입력 |
| 7 | A_CMP | B_DC | $\eta/2$-regular 이동 | 입력 |
| 8 | X_SAMP | B_DC | 한 prefix 주변법칙 불변 | 입력 |
| 9 | B_CON | B_PB | 자식마다 축약 경계 | 입력 |
| 10 | X_SAMP | B_PB | $\mu_{e,S}=\prod_j\mu_{e,T_j}$ | 입력 |
| 11 | A_DEF | P_V | (라벨 없음) | 입력 |
| 12 | B_DEF | P_V | $v_N(S,d)$ | 입력 |
| 13 | X_TI | P_1 | spin anchor, color 하나 | 입력 |
| 14 | X_EXT | P_1 | $c_d,\ c_\ell$ | 입력 |
| 15 | B_CON | P_1 | 세 사본 부등식 | 입력 |
| 16 | X_TI | P_IND | 늦춘 두 사본 | 입력 |
| 17 | X_RT | P_IND | $J=\kappa(S^+)^2$ | 입력 |
| 18 | X_CH | P_IND | 상대 절대 비용 | 입력 |
| 19 | B_PB | P_IND | 자식 사영 | 입력 |
| 20 | B_DC | P_IND | 깊이 되돌림 $C/L$ | 입력 |
| 21 | A_CMP | P_FB | (라벨 없음) | 입력 |
| 22 | A_HOL | P_FB | $\gamma\le1$ | 입력 |
| 23 | P_IND | P_REC | (라벨 없음) | 입력 |
| 24 | P_FB | P_REC | $\gamma=1/4$ | 입력 |
| 25 | A_ERR | P_REC | $\varepsilon_{N,L,k}\to0$ | 입력 |
| 26 | P_V | P_REC | (라벨 없음) | 입력 |
| 27 | P_1 | PROP | 기저 | 입력 |
| 28 | P_REC | PROP | 귀납 | 입력 |
| 29 | X_TI | T_S | color 없음, $f=R_S$ | key |
| 30 | X_MO | T_SET | $f=R_S$ | 입력 |
| 31 | B_DEF | T_SET | $\mathscr F_{e-1}$ | 입력 |
| 32 | T_SET | T_C | 첫 path는 $e-1$ 에서 fresh | key |
| 33 | X_EXT | T_C | extension 계수 | 입력 |
| 34 | X_RT | T_C | $\kappa(S)$ | 입력 |
| 35 | T_SET | T_SIDES | $e-1$ 아래 조건부 iid | key |
| 36 | T_C | T_SIDES | 양쪽 같은 계수 | key |
| 37 | X_TI | T_SIDES | marker anchor 항등식 | key |
| 38 | X_SAMP | T_SIDES | continuation 삭제 → 법칙 $S$ | 입력 |
| 39 | T_SIDES | T_VM | $C\,\mathrm{Var}(M)=o_N(1)$ | key |
| 40 | T_C | T_VM | $C\neq0$, 고정 $L$ 에서 나눔 | key |
| 41 | B_PB | T_G | $B=\mathbf1$ | key |
| 42 | B_DEF | T_G | $\mu_{e,T_j}$ | 입력 |
| 43 | T_G | T_ADJ | $G-G_-$ | key |
| 44 | B_ME | T_ADJ | 곱 차이 + energy | 입력 |
| 45 | A_DEF | T_ADJ | $e$ 를 평균 | 입력 |
| 46 | T_G | T_L2 | $\mathbb E(R_S-G)^2\le p_N^2$ | key |
| 47 | T_SET | T_L2 | $M$ 의 정의 | 입력 |
| 48 | B_PB | T_FIB | $p_N=\sum_j v_N^{1/4}$ | 입력 |
| 49 | P_FB | T_FIB | $\gamma=1/2,\ D=b(S)$ | key |
| 50 | P_V | T_FIB | $V_{k-1,L}(\eta/2)$ | 입력 |
| 51 | T_VM | T_VAR | $\mathrm{Var}(M)$ 항 | key |
| 52 | T_L2 | T_VAR | $\mathbb E(R_S-M)^2$ 항 | key |
| 53 | T_ADJ | T_VAR | $C_k/L$ | key |
| 54 | T_FIB | T_VAR | $V_{k-1}^{1/2}$ | key |
| 55 | A_ERR | T_VAR | 고정 $L$: 유한 합 | 입력 |
| 56 | T_VAR | THM | $L^{-1}\to0$ | key |
| 57 | PROP | THM | $V_{k-1,L}(\eta/2)\to0$ | key |
| 58 | T_S | THM | singleton | key |
| 59 | REM | THM | (라벨 없음) | note |
| 60 | THM | OUT | (라벨 없음) | 입력 |
