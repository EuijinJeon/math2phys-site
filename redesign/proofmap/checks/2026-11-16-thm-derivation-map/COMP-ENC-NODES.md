# node·edge 표 (생성물)

`make check`가 JSON에서 만든다. 직접 고치지 않는다.

## node

| id | 묶음 | 자리 [띠,열] | 종류 | 원문 표지 | 제목 | 대표식 | 원문 줄 |
|---|---|---|---|---|---|---|---|
| EN_Y | §8 지도에서 받는 것 | [0,0] | ext | ENC_CON ← X_Y · tree:original-tilt | Reservoir의 tilted kernel과 Gibbs kernel | $K_d=e^{m_d(X_d-X_{d-1})}P_d\ (1\le d\lt L)$, $K_L=$ prefix 조건부 Gibbs | trees.tex 52–66; cavity.tex 54–58 |
| EN_TREE | §8 지도에서 받는 것 | [2,0] | ext | §3 tree 표본 규칙 (X_SAMP) | Child는 prefix가 주어지면 독립 | 각 vertex에서 서로 다른 child는 그 vertex의 prefix가 주어지면 kernel로 독립하게 뽑는다 | trees.tex 29–39 |
| EN_Q | §8 지도에서 받는 것 | [1,0] | ext | §2 model.tex 54 | 한 spin의 law $q_x$ | $q_x(s)=\dfrac{e^{xs}}{2\cosh x}$, $\ \sum_s s\,q_x(s)=\tanh x$ | model.tex 54 |
| EN_CHAIN | §8 지도에서 받는 것 | [2,0] | ext | X_B · model:chain | Trial message의 계층과 chain | $\mathcal M_1=\mathcal P(\mathbb R)$, $\mathcal M_{j+1}=\mathcal P(\mathcal M_j)$; $\eta_0\sim\zeta,\ \eta_{d+1}\mid\eta_d\sim\eta_d,\ x\mid\eta_{r-1}\sim\eta_{r-1}$ | model.tex 67–80; trees.tex 24–27 |
| EN_ROOT | ENC · 구성(위)과 확인(가운데) | [0,1] | 보통 | comp:encoding 증명 1 | Root를 넓힌다: uniform site를 넣는다 | root $=(\text{reservoir root disorder},\ i)$, $i\sim\mathrm{Unif}[N]$ 독립; $\mathscr G_d=\sigma(\text{root},\ \text{깊이 }d\text{까지의 auxiliary prefix})$ | comparison.tex 28–32 |
| EN_X | ENC · 구성(위)과 확인(가운데) | [0,2] | 보통 | comp:encoding 증명 2 | 깊이 $r=L-1$의 message $x$ | $x=\operatorname{arctanh}\langle\sigma_i\rangle$, 잎의 spin $\mid\mathscr G_r\ \overset{\text{iid}}{\sim}q_x$ | comparison.tex 33–42 |
| EN_BACK | ENC · 구성(위)과 확인(가운데) | [0,3] | 보통 | comp:encoding 증명 3 | 중첩 measure를 거꾸로 정의 | $\eta_{r-1}=\operatorname{Law}(x\mid\mathscr G_{r-1})$, $\eta_d=\operatorname{Law}(\eta_{d+1}\mid\mathscr G_d)\ (0\le d\lt r-1)$; $\eta_d\in\mathcal M_{r-d}$, $\zeta_{L,N}=\operatorname{Law}(\eta_0)\in\mathcal M_L$ | comparison.tex 43–57 |
| EN_G | ENC · 구성(위)과 확인(가운데) | [1,3] | 보통 | comp:encoding 확인 1 | Leaf 패턴의 조건부 확률 (깊이 $r$) | $G_T(x)=\prod_{a}q_x(e_a)$ | comparison.tex 58–61 |
| EN_REC | ENC · 구성(위)과 확인(가운데) | [1,4] | 보통 | comp:encoding 확인 2 | Reservoir 쪽 backward recursion | $P(\text{패턴}\mid\mathscr G_d)=G_T(\eta_d)=\prod_{\ell=1}^j\int G_{T_\ell}(\nu)\,\eta_d(d\nu)$ | comparison.tex 61–69 |
| EN_TRIAL | ENC · 구성(위)과 확인(가운데) | [2,4] | 보통 | comp:encoding 확인 3 · model:chain | Trial 쪽도 같은 recursion | model:chain의 branching 판: $P_{\rm trial}(\text{패턴}\mid\eta_d)=\prod_\ell\int G_{T_\ell}(\nu)\,\eta_d(d\nu)$ | comparison.tex 71–72; model.tex 72–76 |
| EN_EQ | ENC · 구성(위)과 확인(가운데) | [1,5] | 보통 | comp:encoding 확인 4 | 모든 tree의 출력 law가 같다 | $\mathbb E\,G_T(\eta_0)=\int G_T\,d\zeta_{L,N}$ : reservoir uniform site $=$ trial label | comparison.tex 66–73 |
| EN_MOM | ENC · 구성(위)과 확인(가운데) | [1,6] | 보통 | eq comp:single-label-moments | Spin 곱 기대값 = $\mathbb ER_S$ | $\mathbb E\prod_{a\in S}\tau^a=\dfrac1N\sum_{i=1}^N\mathbb E\prod_{a\in S}\sigma_i^a=\mathbb ER_S$ | comparison.tex 73–79 |
| EN_IND | ENC · 구성(위)과 확인(가운데) | [2,6] | 보통 | comp:encoding 증명 끝 | Label마다 독립 사본 | label마다 reservoir root와 uniform site까지 포함한 구성 전체의 독립 사본 | comparison.tex 80–82 |
| EN_LEM | ENC · 구성(위)과 확인(가운데) | [1,7] | key | Lemma comp:encoding | Recursive law encoding | 결정론적 $\zeta_{L,N}\in\mathcal M_L$: 한 label의 spin process가 모든 prescribed tree에서 reservoir uniform site와 같은 spin 곱 기대값; label들은 독립 | comparison.tex 19–25 |
| EN_U_PAT | ENC · 구성(위)과 확인(가운데) | [0,8] | 보통 | → PAT_PI (comparison.tex 109) | 쓰임: trial pattern 분포 $\bar\pi=\mathbb E\pi$ | $\pi(\boldsymbol e)=2^{-k}\sum_SR_S\prod_{b\in S}e_b\ \Rightarrow\ \bar\pi=2^{-k}\sum_S\mathbb ER_S\prod_{b\in S}e_b=\mathbb E\pi$ | comparison.tex 99–118 |
| EN_U_TR | ENC · 구성(위)과 확인(가운데) | [2,8] | 보통 | → P_TR (comparison.tex 170–175) | 쓰임: reservoir spin을 독립 trial spin으로 | insertion의 site label마다 $\zeta_{L,N}$의 독립 spin process | comparison.tex 170–175 |

## edge

| # | 보냄 | 받음 | 싣는 내용 | 종류 |
|---|---|---|---|---|
| 0 | EN_Y | EN_ROOT | tilted kernel로 path 표본 | 입력 |
| 1 | EN_ROOT | EN_X | site $i$ 고정 | 입력 |
| 2 | EN_Y | EN_X | $K_L$: Gibbs 기대값 | 입력 |
| 3 | EN_Q | EN_X | 평균 $\tanh x$ | key |
| 4 | EN_TREE | EN_X | terminal replica 독립 | 입력 |
| 5 | EN_X | EN_BACK | $x$에서 시작 | key |
| 6 | EN_ROOT | EN_BACK | $\mathscr G_d$ | 입력 |
| 7 | EN_CHAIN | EN_BACK | $\mathcal M_j$ 계층 | 입력 |
| 8 | EN_X | EN_G | 잎 spin $q_x$ | 입력 |
| 9 | EN_Q | EN_G | $q_x(e_a)$ | 입력 |
| 10 | EN_G | EN_REC | 깊이 $r$ 출발점 | key |
| 11 | EN_BACK | EN_REC | $\eta_d=\operatorname{Law}(\eta_{d+1}\mid\mathscr G_d)$ | key |
| 12 | EN_TREE | EN_REC | 자식 조건부 독립 | 입력 |
| 13 | EN_CHAIN | EN_TRIAL | $\eta_{d+1}\mid\eta_d\sim\eta_d$ | 입력 |
| 14 | EN_TREE | EN_TRIAL | 자식 독립 | 입력 |
| 15 | EN_G | EN_TRIAL | 같은 $G_T$ | 입력 |
| 16 | EN_REC | EN_EQ | reservoir $=\mathbb E G_T(\eta_0)$ | key |
| 17 | EN_TRIAL | EN_EQ | trial $=\int G_T d\zeta$ | key |
| 18 | EN_BACK | EN_EQ | $\zeta_{L,N}=\operatorname{Law}(\eta_0)$ | 입력 |
| 19 | EN_EQ | EN_MOM | 패턴 law 일치 | key |
| 20 | EN_ROOT | EN_MOM | uniform $i$ → $\frac1N\sum_i$ | 입력 |
| 21 | EN_ROOT | EN_IND | 구성 전체를 복제 | 입력 |
| 22 | EN_MOM | EN_LEM | moment 등식 | key |
| 23 | EN_IND | EN_LEM | 독립 label | 입력 |
| 24 | EN_LEM | EN_U_PAT | $\mathbb E\prod\tau=\mathbb ER_S$ | key |
| 25 | EN_LEM | EN_U_TR | 독립 trial spin process | key |
