# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| X_SEL | 밖에서 받는 것 (§2·§3·§5·§6·§7) | [1,0] | ext | Lemma pert:selection | 결정론적 parameter 선택 | 고정 $L,\varepsilon$: $N_j\uparrow\infty$, $\mathbf u_j$ 로 $\Delta_{N_j}(\mathbf u_j)\le\underline F+2\varepsilon$ | perturbations.tex 246–266 |
| X_INC | 밖에서 받는 것 (§2·§3·§5·§6·§7) | [1,0] | ext | Lemma cavity:increment · eq cavity:identity | Cavity increment와 두 insertion | $\Delta_N^{L,\mathbf u}=\log2+\mathbb E\log Y_{0,\rm s}-\mathbb E\log Y_{0,\rm b}+o_N(1)$ | cavity.tex 11–12, 43–69 |
| X_Y | 밖에서 받는 것 (§2·§3·§5·§6·§7) | [0,0] | ext | eq tree:Y-recursion · tree:original-tilt | Tilted kernel 위의 power-mean recursion | $Y_L=A,\quad Y_{d-1}=\bigl(K_dY_d^{m_d}\bigr)^{1/m_d}$ | trees.tex 55–72 |
| X_LOG | 밖에서 받는 것 (§2·§3·§5·§6·§7) | [0,0] | ext | Lemma tree:log-expansion · law $Q_k$ | 로그 전개와 tree law $Q_k$ | $\log Y_0=\sum_{k\ge1}\frac{(-1)^{k-1}t^k}{k}\,\mathbb E_{Q_k}E_{\mathcal T}\prod_{a=1}^kD^a$ | trees.tex 205–252 |
| X_REG | 밖에서 받는 것 (§2·§3·§5·§6·§7) | [0,0] | ext | Lemma tree:regular-shapes | Regular shape | $Q_k\{\text{nonregular}\}\le C_k(\eta+L^{-1})$ 한 depth 배정의 확률 $\le C_kL^{-a}$ | trees.tex 457–486 |
| X_B | 밖에서 받는 것 (§2·§3·§5·§6·§7) | [0,0] | ext | §2 model:chain · model:power-means · model:functional | Trial law와 RSB functional $\mathcal B_r$ | $\zeta\in\mathcal M_{r+1}$, $\mathcal B_r(\zeta,\mathbf m)=\log2+\mathbb E\log T_0V_{\rm s}-\alpha(p-1)\mathbb E\log T_0V_{\rm e}$ | model.tex 54–118 |
| X_TB | 밖에서 받는 것 (§2·§3·§5·§6·§7) | [1,0] | ext | eq model:trial-bounds | Trial 값의 유계성 | $\|\log T_0V_{\rm s}\|\le\|h\|+\sum_{j\le k}B(\theta_j)$, $\|\log T_0V_{\rm e}\|\le B(\theta)$ | model.tex 120–127 |
| X_DECOR | 밖에서 받는 것 (§2·§3·§5·§6·§7) | [0,0] | ext | Thm decor:overlap-concentration (§7) | 모든 multioverlap의 깊이 평균 집중 | $\lim_{L\to\infty}\limsup_{N\to\infty}\mathcal A_{L,\eta}\mathrm{Var}(R_S)=0$ 모든 $\eta>0$, 모든 고정 $S$ | decorrelation.tex 14–37, 63–76 |
| SET | (묶음 없음) | [1,1] | 보통 | §8 설정 · eq comp:low-increments | 선택된 수열과 낮은 increment | 고정 $\varepsilon$, 각 $L$의 선택 수열 위에서 $\Delta_N^{L,\mathbf u_{L,N}}\le\underline F+2\varepsilon$ | comparison.tex 8–15 |
| ENC_CON | §8.1 한 site tree의 encoding | [0,1] | 보통 | comp:encoding 증명 (구성) | Site 하나의 branching law를 중첩 measure로 | $x=\operatorname{arctanh}\langle\sigma_i\rangle$, $\eta_{r-1}=\operatorname{Law}(x\mid\mathscr G_{r-1})$, $\eta_d=\operatorname{Law}(\eta_{d+1}\mid\mathscr G_d)$ | comparison.tex 27–57 |
| ENC | §8.1 한 site tree의 encoding | [0,2] | key | Lemma comp:encoding · eq comp:single-label-moments | Recursive law encoding | $\zeta_{L,N}\in\mathcal M_L$ (결정론적), $\ \mathbb E\prod_{a\in S}\tau^a=\frac1N\sum_i\mathbb E\prod_{a\in S}\sigma_i^a=\mathbb ER_S$ | comparison.tex 19–25, 58–83 |
| PAT_PI | §8.2 Multioverlap에서 spin pattern으로 | [0,3] | 보통 | comp:patterns 증명 (경험 분포) | Site pattern의 경험 분포 | $\pi(\boldsymbol e)=2^{-k}\sum_{S\subseteq[k]}R_S\prod_{b\in S}e_b$, $\ \bar\pi=\mathbb E\pi$ | comparison.tex 99–112 |
| PAT | §8.2 Multioverlap에서 spin pattern으로 | [0,4] | key | Lemma comp:patterns · eq comp:pattern-error | Empirical-pattern comparison | 오차 $\le a\sum_{\varnothing\ne S\subseteq[k]}\mathbb E\|R_S-\mathbb ER_S\|$ | comparison.tex 87–97, 110–121 |
| SH_B | §8.2 Multioverlap에서 spin pattern으로 | [0,3] | 보통 | eq comp:shape-error-bound | 모양 오차를 깊이 평균 분산으로 | $\mathbb E_{Q_k}\sum_{S\ne\varnothing}\mathbb E\|R_S-\mathbb ER_S\|$ $\quad\le C_k\bigl(\eta+L^{-1}+\sum_{U\in\mathfrak S_k}(\mathcal A_{L,\eta}\mathrm{Var}(R_U))^{1/2}\bigr)$ | comparison.tex 131–153 |
| SH | §8.2 Multioverlap에서 spin pattern으로 | [0,4] | key | eq comp:shape-error | 모양 오차의 소멸 | $\lim_{L\to\infty}\limsup_{N\to\infty}\mathbb E_{Q_k}\sum_{\varnothing\ne S\subseteq[k]}\mathbb E\|R_S-\mathbb ER_S\|=0$ ($k$ 고정) | comparison.tex 123–130, 153–156 |
| P_TR | §8.3 Insertion 로그의 비교 | [1,3] | 보통 | 증명 1 · trial insertion | Reservoir spin을 trial spin process로 | $A_{\rm s},A_{\rm b}\ \mapsto\ \widetilde A_{\rm s},\widetilde A_{\rm b}$; $\ \widetilde Y_{0,\rm s},\widetilde Y_{0,\rm b}$ | comparison.tex 171–176 |
| P_ID | §8.3 Insertion 로그의 비교 | [1,4] | key | 증명 2 · trial 항등식 | Trial 쪽은 정확히 $\mathcal B_{L-1}$ | $\mathbb E\log\widetilde Y_{0,\rm b}=\alpha(p-1)\mathbb E\log T_0V_{\rm e}$ $\log2+\mathbb E\log\widetilde Y_{0,\rm s}-\mathbb E\log\widetilde Y_{0,\rm b}=\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})$ | comparison.tex 178–196 |
| P_CUT | §8.3 Insertion 로그의 비교 | [1,4] | 보통 | 증명 3 · count cutoff | Poisson count를 $K\le M$으로 자름 | $C=H+BM$, $z=\cosh C$, $c=\tanh C\lt 1$: $\ A=z(1+D)$, $\|D\|\le c$ | comparison.tex 198–203 |
| P_EXP | §8.3 Insertion 로그의 비교 | [1,5] | key | 증명 4 · 전개 항별 비교 | 로그 전개의 각 차수 비교 | 차수 $k$ 오차(고정 tree) $\le pM\sum_{S\ne\varnothing}\mathbb E\|R_S-\mathbb ER_S\|$ 꼬리 $\le\sum_{k>q}c^k/k$ | comparison.tex 205–213 |
| P_TAIL | §8.3 Insertion 로그의 비교 | [1,5] | 보통 | 증명 5 · Poisson 꼬리 | Cutoff 밖의 기여 | $\le2\,\mathbb E[(H+BK)\mathbf 1_{\{K>M\}}]\to0\ (M\to\infty)$ | comparison.tex 215–217 |
| P_ORD | §8.3 Insertion 로그의 비교 | [1,6] | key | 증명 6 · 극한 순서 | Insertion 로그 기댓값의 수렴 | $M$ (Poisson 꼬리) $\to$ $q$ (기하 꼬리) $\to$ 고정 $L$에서 $N$ $\to$ $L\to\infty$ | comparison.tex 218–221 |
| PROP | §8.3 Insertion 로그의 비교 | [1,7] | goal | Proposition comp:insertion-comparison | Cavity increment = RSB functional (극한에서) | $\lim_{L\to\infty}\limsup_{N\to\infty}\bigl\|\Delta_N^{L,\mathbf u_{L,N}}-\mathcal B_{L-1}(\zeta_{L,N},\mathbf m^{(L)})\bigr\|=0$ | comparison.tex 160–167, 221–222 |
| COR | §8 Corollary: 유계 모형의 하한 | [1,8] | key | Corollary comp:bounded-lower | 유계 모형의 하한 | $\liminf_{N\to\infty}F_N\ge\inf_{r\ge0}\Phi_r$ | comparison.tex 225–246 |
| OUT | (묶음 없음) | [1,9] | ext | §9 reduction:section → Thm main:theorem | 받는 곳: 정규화·truncation과 주정리 | truncation $K\to\infty$로 $\liminf_N F_N\ge\inf_r\Phi_r$; upper:bound와 합쳐 main:formula | reduction.tex 4–6, 60–85 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | X_SEL | SET | 선택 수열, (i) 낮은 increment | key |
| 1 | X_Y | ENC_CON | tilted reservoir kernel | 입력 |
| 2 | X_B | ENC_CON | $\mathcal M_j$ 계층 | 입력 |
| 3 | ENC_CON | ENC | 중첩 measure $\eta_d$ | key |
| 4 | X_B | ENC | model:chain의 branching 판 | 입력 |
| 5 | ENC | PAT_PI | $\bar\pi=\mathbb E\pi$ | key |
| 6 | PAT_PI | PAT | $\pi^{\otimes a}$ 대 $\bar\pi^{\otimes a}$ | key |
| 7 | X_LOG | SH_B | tree law $Q_k$ | 입력 |
| 8 | X_REG | SH_B | nonregular 확률, 배정 확률 | key |
| 9 | X_DECOR | SH_B | $\mathcal A_{L,\eta}$ 정의 | 입력 |
| 10 | SH_B | SH | bound | key |
| 11 | X_DECOR | SH | $N$, $L$, 그다음 $\eta\downarrow0$ | key |
| 12 | X_INC | P_TR | $A_{\rm s}$, $A_{\rm b}$ | key |
| 13 | ENC | P_TR | 독립 trial spin process | key |
| 14 | X_Y | P_TR | trial kernel의 recursion | 입력 |
| 15 | P_TR | P_ID | $\widetilde Y_{0,\rm s}$, $\widetilde Y_{0,\rm b}$ | key |
| 16 | X_B | P_ID | $V_{\rm s}$, $V_{\rm e}$, $T_0$, $\mathcal B_r$ | 입력 |
| 17 | P_TR | P_CUT | 두 insertion 쌍 | key |
| 18 | X_INC | P_CUT | $B(\theta)\le B$, $\|h\|\le H$ | 입력 |
| 19 | P_CUT | P_EXP | $A=z(1+D)$, $\|D\|\le c$ | key |
| 20 | X_LOG | P_EXP | 전개와 꼬리 $\sum_{k>q}c^k/k$ | 입력 |
| 21 | PAT | P_EXP | 고정 tree 위 오차 | key |
| 22 | SH | P_EXP | tree 평균 오차 $\to0$ | key |
| 23 | P_CUT | P_TAIL | $K>M$ 쪽 | 입력 |
| 24 | P_EXP | P_ORD | $q$항과 꼬리 | key |
| 25 | P_TAIL | P_ORD | $M\to\infty$ | key |
| 26 | P_ID | PROP | trial 쪽 $=\mathcal B_{L-1}$ | key |
| 27 | P_ORD | PROP | 로그 기댓값 수렴 | key |
| 28 | X_INC | PROP | cavity:identity | 입력 |
| 29 | SET | PROP | 선택 수열 위의 $\Delta_N^{L,\mathbf u_{L,N}}$ | 입력 |
| 30 | PROP | COR | $L\to\infty$ | key |
| 31 | SET | COR | comp:low-increments | key |
| 32 | X_TB | COR | $\inf_r\Phi_r$ 유한 | 입력 |
| 33 | COR | OUT | (라벨 없음) | 입력 |
