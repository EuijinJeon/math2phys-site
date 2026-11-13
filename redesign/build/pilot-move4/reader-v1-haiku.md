# 독자 시험 v1 답안 (수 4, 통계물리 독자)

읽은 파일: /tmp/reader-in-v1/ 의 L0.md, L1.md, L2.md(612행 전부), rules.md, glossary.md(528행 전부), 그리고 질문지 questions.md. 다른 파일은 열지 않았다. 작업 지시에 "필요하면 다른 파일을 찾아봐도 된다"가 있었지만 앞의 "읽을 수 있는 파일은 다섯 개뿐이다"와 충돌하므로 좁은 쪽을 따랐다. 따라서 "찾지 못함"은 이 파일들 안에서 못 찾았다는 뜻이다.

행 번호는 파일의 행 번호다. "L2 §6.2 ①" 등은 L2.md의 절이다.

---

## 1. P6′ 의 주 식

**(a) 답.**
- 좌변: 삽입 $A_{\boldsymbol t}=1+\sum_j t_jD_j$ 로 바뀐 법칙 $E^{A_{\boldsymbol t}}_{\mathcal T}$ 아래에서 $G/A_{\boldsymbol t}^{a_*}$ 를 평균한 값을, 삽입 크기 $t_1,\ldots,t_k$ 로 한 번씩 미분해 $\boldsymbol t=0$ 에서 본 것이다. 6.1의 밀도로 쓰면 $E_{\mathcal T}\bigl[G\prod_{a\ne a_*}A^a\prod_\beta Y_\beta^{\gamma_\beta}\bigr]$ 이고, 분모 $A^{a_*}$ 가 밀도의 anchor 인자 하나를 지운다.
- 우변: $\sum_E c_E\,E_{\mathcal T_E}\bigl[G\prod_{j}D_j^{a_j(E)}\bigr]$, 유한 합이다. $E$ 는 old tree에서 color $1,\ldots,k$ 를 차례로 주는 extension history 전체다. $c_E$ 는 걸음마다의 계수의 곱이고 부호가 섞인다. $\mathcal T_E$ 는 history가 끝난 tree이고 삽입 없는 원래 kernel로 뽑는다. $a_j(E)$ 는 color $j$ 를 받은 leaf이고 $D_j^{a}$ 는 그 leaf의 path에서 본 $D_j$ 다. $\boldsymbol t=0$ 에서는 $A$ 와 $Y$ 가 모두 1이라 법칙에 삽입의 흔적이 없다.

**(b) 근거.** L2 §6.2 ① 주 식 266행, 좌변 설명 268행, 우변 설명 269행, 기호 271–275행. factorial이 없다는 말은 L2 307행. rules.md P6′ 행(22행) "① 전개". 원문 기호 $H$ 가 $G$ 로 바뀌었다는 말은 L2 273행.

**(c) 출처.** 글에 적혀 있음.

---

## 2. $c_E$ 의 정의

**(a) 답.**
- extension history $E$: old tree $\mathcal T$ 에서 시작해 color $1,\ldots,k$ 를 차례로 준다. color마다 다음 둘 중 하나를 고른다.
  - (i) 재사용: anchor가 아니고 아직 color를 받지 않은 old leaf 하나에 준다. 계수 $+1$.
  - (ii) fresh path: 현재 tree의 내부 vertex $\beta$ 를 골라 거기 새 자식을 만들고 깊이 $L$ 까지 새 path를 잇는다. 그 끝 leaf가 color를 받는다. 계수 $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}<0$.
- 내부 vertex는 깊이 $0,\ldots,L-1$ 의 모든 vertex이고 unary도 포함한다.
- $c_E$ 는 걸음별 계수의 곱이다. $k=0$ 이면 빈 history 하나이고 $c=1$.
- $n_\beta$ 는 **그 걸음을 하기 직전의 현재 tree에서 $\beta$ 가 가진 자식 수**다. old tree에서의 자식 수가 아니다. 앞 걸음의 fresh path가 $\beta$ 에 더한 자식도 센다.
- 현재 tree = old path 전부 + 그때까지 붙인 fresh path 전부. anchor는 처음부터 고를 수 없고, color를 받은 leaf도 다시 고를 수 없다.

**(b) 근거.** L2 §6.2 ① 기호와 extension history 절, 276–288행. 선택지 표 278–281행. 자식 수 정의 284행. 제약 285행. rules.md P6′ 행(22행) "c_E 는 그 계수들의 곱". glossary g:extension-history 347–352행.

**(c) 출처.** 글에 적혀 있음.

---

## 3. 계산 (old tree 둘, $k=1$, $H=G=1$, $D=1$, $m_0=0$, $m_L=1$)

설정. old tree는 줄기가 깊이 $0,\ldots,s-1$ 에서 unary로 올라가다가 깊이 $s$ 에서 두 가지로 갈라진다. 한 가지는 anchor $a_*$ 로 끝나고 다른 가지는 replica $b$ 로 끝난다. 두 가지는 깊이 $s+1,\ldots,L-1$ 에서 unary다. fresh를 붙일 수 있는 내부 vertex는 다음과 같다.
- 줄기 깊이 $d<s$: 자식 1개 ($n=1$).
- 갈림점 깊이 $s$: 자식 2개 ($n=2$).
- anchor 가지 깊이 $\ell\in(s,L-1]$: $n=1$.
- $b$ 가지 깊이 $\ell\in(s,L-1]$: $n=1$.

$k=1$ 이므로 history는 걸음 하나다.

| history | 개수 | $c_E$ |
|---|---|---|
| $b$ 재사용 | 1 | $+1$ |
| 줄기 깊이 $d$ ($0\le d<s$)에서 fresh | $s$ | $m_d-m_{d+1}$ |
| 갈림점 깊이 $s$ 에서 fresh | 1 | $m_s-2m_{s+1}$ |
| anchor 가지 깊이 $\ell$ ($s<\ell\le L-1$)에서 fresh | $L-1-s$ | $m_\ell-m_{\ell+1}$ |
| $b$ 가지 깊이 $\ell$ ($s<\ell\le L-1$)에서 fresh | $L-1-s$ | $m_\ell-m_{\ell+1}$ |

개수 합은 $1+s+1+2(L-1-s)=2L-s$.

합:
$$
\begin{aligned}
&1+\sum_{d=0}^{s-1}(m_d-m_{d+1})+(m_s-2m_{s+1})+2\sum_{\ell=s+1}^{L-1}(m_\ell-m_{\ell+1})\\
&=1+(m_0-m_s)+(m_s-2m_{s+1})+2(m_{s+1}-m_L)\\
&=1+m_0-2m_L=1+0-2=-1 .
\end{aligned}
$$
$s$ 가 사라졌으므로 $s$ 에 무관하다.

좌변 확인. $A=1+t$ 는 상수이므로 모든 깊이에서 $Y_d=1+t$ 이고 $K^A_d=K_d$ 다. 따라서 $E^A[1/A^{a_*}]=(1+t)^{-1}$ 이고 $t=0$ 에서의 미분은 $-1$ 이다. 밀도로 확인해도 같다. $\prod_a A^a=(1+t)^2$, $\sum_\beta\gamma_\beta=-2$ 이므로 $\prod_\beta Y_\beta^{\gamma_\beta}=(1+t)^{-2}$ 이고 밀도는 1이다. 그러면 $E^A[1/A^{a_*}]=E[(1+t)^{-1}]$ 이고 미분은 $-1$ 이다.

**결과.** 합 $-1$ 과 좌변 $-1$ 이 맞는다.

**(b) 근거.** L2 예 1 표 293–299행, 합 301–302행, 좌변 확인 303행. 좌변의 밀도 표현은 L2 235행과 6.2 ① 268행. $\gamma_\beta$ 의 합이 $-n$ 이라는 telescoping은 glossary g:tree-coefficient가 아니라 L2 245행("$\sum_\beta(-\gamma_\beta)=n$", [[tree:telescoping]])에 있다. 이 telescoping은 나도 두 가지 tree(갈림이 깊이 0, 깊이 1)에서 확인했다.

**(c) 출처.** 나열과 합은 글에 적혀 있음. 나는 표를 다시 세어 같은 값을 얻었다(산수). telescoping의 일반 증명은 찾지 못함(인용 노드 tree:telescoping은 카드에 있다).

---

## 4. anchor 인자만 상쇄한 기대값

**(a) 답.**
- 이유: 집중시키는 양은 anchor의 path 하나에서 본 score $D_\nu^{a_*}$ 다. 이것을 Palm 항등식으로 새 삽입의 tree 기대값으로 바꾸면 score가 $g_0^{a_*}S_0^{a_*}/A^{a_*}$ 꼴이 된다. 그 분모 $A^{a_*}$ 가 밀도 $W_{\mathcal T}(A)$ 의 anchor 인자를 지운다. 그래서 얻는 양은 "anchor가 protected인 바뀐 법칙의 기대값"이고, 6.2 ①의 좌변과 같다(G를 $f\,g_0^{a_*}S_0^{a_*}$ 로 둔 것).
- 상쇄는 골라서 넣은 규약이 아니라 Palm 단계에서 저절로 생긴다고 글에 쓰여 있다.
- P7과의 연결: $\Pi_{N,\mathcal T}(t,u)=E\,E^A_{\mathcal T}[f\,g_0^{a_*}S_0^{a_*}/A^{a_*}]$ 로 놓고, 같은 식을 anchor 하나뿐인 tree와 $f=1$ 로 쓴 $\Pi_{N,\{a_*\}}$ 를 만든다. $\Xi_N=\Pi_{N,\mathcal T}-E f\,\Pi_{N,\{a_*\}}$ 의 Taylor 계수가 0으로 가고(단계 3), 6.2 ①로 풀면 $\sum_E c_E$ 꼴이 나온다. polarization(단계 4)과 mark selector, site 평균(단계 5)을 거치면 P7의 두 합이 된다. 첫째 합은 $\Pi_{N,\mathcal T}$ 쪽, 둘째 합은 $\Pi_{N,\{a_*\}}$ 쪽이다.

**(b) 근거.** L2 §6.3 "anchor를 왜 상쇄하는가" 414행. 단계 0의 "anchor의 path 하나만 보면" 396행. 단계 1 401–404행, 단계 2 406행, 단계 3 408행, 단계 4 410행, 단계 5 412행. 6.2 ① 좌변 268행. P7 주 식 374–375행. glossary g:palm-identity 375–380행, g:protected-leaf 340–345행. rules.md P7 행(23행). L1 4번 항목(23행).

**(c) 출처.** 글에 적혀 있음. 다만 Palm 항등식 자체(pert:palm)의 증명은 L2에 없어서 찾지 못함(카드에 있음, L2 425행 블랙박스).

---

## 5. $\kappa(S)$ 

**(a) 답.**
- $\kappa(S)$ 는 모양 $S$ 를 갖는 모든 extension history의 $c_E$ 의 합이다. 모양 $S$ 는 anchor와 color 받은 path만으로 된 tree, 곧 그들 사이의 쌍별 split 깊이 전부다. 식:
$$\kappa(S)=\prod_{v\in\operatorname{Br}(S)}\ \prod_{j=1}^{a_v-1}\bigl(m_{d_v}-j\,m_{d_v+1}\bigr).$$
$\operatorname{Br}(S)$ 는 $S$ 의 branching vertex, $a_v$ 는 $S$ 안의 자식 수, $d_v$ 는 깊이다.
- old tree와 무관한 이유: 한 걸음을 본다. 새 color가 깊이 $d$ 의 vertex $v$ 까지 reference path를 따라가다가, reference가 지나는 $j$ 개 자식이 아닌 쪽으로 가야 한다. $v$ 의 현재 자식 수를 $n$ 이라 하면 허용 선택은 두 종류다. $v$ 에서 바로 fresh로 가면 $m_d-n\,m_{d+1}$ 이다. 또는 reference가 지나지 않는 $n-j$ 개 자식 가운데 하나로 들어간다. 그 아래 old path만의 모든 선택을 더하면 $m_{d+1}$ 이라고 글이 쓴다. 그러면 한 걸음의 합은 $(m_d-nm_{d+1})+(n-j)m_{d+1}=m_d-j\,m_{d+1}$ 이고 $n$ 이 사라진다. 걸음들의 곱이 $\kappa(S)$ 다.
- 최소 예: anchor와 새 replica 하나가 깊이 $d$ 에서 갈라지는 모양이면 $\kappa(S)=m_d-m_{d+1}$ 이고 균등 격자 $m_d=d/L$ 에서는 $-\delta=-1/L$ 이다. 예 1에서 $d=s$ 일 때 세 history의 합은 $1+(m_s-2m_{s+1})+(m_{s+1}-1)=m_s-m_{s+1}$ 로 이 식과 맞는다.

**(b) 근거.** L2 §6.2 ② 311–325행. 정의 313행, 주 식 315–317행, 왜 무관한가 319–321행, 최소 예 323–325행. glossary g:tree-coefficient 325–331행, g:reference-path 354–360행.

**(c) 출처.** 식, 최소 예, 예 1과의 대조: 글에 적혀 있음. "부분 tree 전체의 합이 $m_{d+1}$ 이다"라는 일반 주장: 글에 적혀 있음(320행). 그 일반 증명은 찾지 못함(L2는 [[tree:reference-total]]로 카드에 넘긴다). 나는 leaf 하나짜리 부분 tree에서 $1+(m_{d+1}-m_L)=m_{d+1}$ 로 직접 확인했다(산수).

---

## 6. P7 식

**(a) 답.**
- $f$: old replica들의 multioverlap으로 쓴 유계 다항식(시험함수). $N$ 에 따라 바뀌지 않는다.
- $c_E$: 6.2의 extension history 계수.
- $R_E$: history가 고른 새 replica들의 multioverlap. spin anchor이면 anchor를 포함해 $R_E=\frac1N\sum_i\sigma_i^{a_*}\prod_j\sigma_i^{a_j(E)}$, marker anchor이면 anchor를 뺀다.
- 첫째 합 범위: $E\in\mathfrak E(\mathcal T,a_*,\mathcal C)$, 곧 old tree $\mathcal T$ 에서 시작하고 제약 $\mathcal C$ 를 지키는 history.
- 둘째 합 범위: $E\in\mathfrak E(\{a_*\},a_*,\mathcal C)$, 곧 anchor 하나뿐인 tree에서 시작해 같은 $\mathcal C$ 를 지키는 history.
- $\mathcal C$: anchor와 color들로 이루어진 집합 안의 쌍별 split 깊이에 대한 일관된 조건들. color끼리의 쌍도 포함하지만 다른 old replica가 관여하는 쌍은 지정하지 못한다. mark 깊이는 $1,\ldots,L-1$ 뿐이다.
- 말로: anchor 옆에 새 섭동 하나를 더해 새 replica를 붙인 효과가 old tree의 시험함수 $f$ 와 분리된다. 분리되는 것은 history 하나하나가 아니라 계수 $c_E$ 를 붙인 부호 있는 합이다. 식으로는 첫째 합이 $\mathbb Ef$ 곱하기 둘째 합과 같아지는 것이다.
- 극한: 선택된 수열(P5)을 따라 $N\to\infty$. 고정한 $L$, old tree, anchor 종류, $f$, color 수 $k$, 제약 $\mathcal C$ 마다 성립한다. 수렴 속도도 $L$ 이나 type에 대한 균일성도 주어지지 않는다.

**(b) 근거.** L2 §6.3 주 식 373–375행, 기호 377–382행, "말로" 384–385행, 처방 386행, 성립 범위 419–423행. 최소 예 389–392행. rules.md P7 행(23행). glossary g:tree-identity 382–388행, g:mark 368–373행.

**(c) 출처.** 글에 적혀 있음.

---

## 7. 흐름

**(a) 답.**
- 받는 것: 수 3의 선택된 수열 위에서 P5 (ii) score 오차 $e_{\nu,N}\to0$, P5 (iii) tree 모멘트의 수렴. 그리고 6.2 ①의 전개. 6.1의 설정(깊이 $L$ tree, 격자 수 $m_0,\ldots,m_L$)과 6.1의 log 전개는 수 4의 설정이다. 수 4가 직접 쓰는 결과로 세지는 않는다. P5 (i)의 상한 $\Delta_{N_j}\le\underline F+2\varepsilon$ 은 수 4가 쓰지 않고 수 6에서 쓴다.
- 넘기는 것: 수 5에 (1) P7의 prescribed-tree 항등식(6.3), (2) 모양별 총합 $\kappa(S)$(6.2 ②), (3) 계수 한계(6.2 ③, 균등 격자에서 절댓값 합 비의 상계)를 넘긴다. 수 5는 여기에 tree 표본 규칙과 모형과 무관한 확률 부등식만 더한다.
- 수 6과의 관계: 6.1의 log 전개(P6)는 수 6이 삽입 계산에 직접 쓴다. 수 4가 수 6에 넘기는 것은 아니다.

**(b) 근거.** L2 §6 표 216–220행. §1.3 54행 "수 4 ... (P6, P6′, P7)". 6.3 "받는 것 / 넘기는 것" 371행. 6.4 429–431행. rules.md P5 행(20행), P7 행(23행). L1 3번(18행)과 4번(23행).

**(c) 출처.** 글에 적혀 있음.

---

## 8. 계수 한계

**(a) 답.**
- $\delta^{b_{\rm sep}}$ 크기로 작은 것:
  - 절댓값 합 $\sum_E|c_E|\le C_{q,k}\,\delta^{b_{\rm sep}}$. 여기서 $b_{\rm sep}$ 는 처방 모양의 branching vertex 가운데 깊이가 old tree의 어떤 branching 깊이와도 다른 것의 수다.
  - 정규화 인자 $|J_{\rm sep}|$ 도 같은 차수다: $\delta^{b_{\rm sep}}\eta^{\sum_v(a_v-2)}\le|J_{\rm sep}|\le k^k\delta^{b_{\rm sep}}$.
- $L$ 에 균일하게 유계인 것:
  - 상수 $C_{q,k}$ 는 old leaf 수 $q$ 와 color 수 $k$ 에만 의존한다.
  - 비 $\sum_E|c_E|/|J_{\rm sep}|\le C_{q,k,\eta}$ 는 그 vertex들의 깊이 $m_{d_v}\ge\eta$ 일 때 $L$ 에 무관하게 성립한다.
  - 반면 $|J_{\rm sep}|$ 자체는 $L$ 에 균일한 양의 하한이 없다.
- 예: 상쇄 예에서 처방을 깊이 $s$ 로 하면 $b_{\rm sep}=0$ 이고 $\sum|c_E|=2+\delta$ 다. 깊이 $s+1$ 로 하면 $b_{\rm sep}=1$, $J_{\rm sep}=-\delta$, $\sum|c_E|=\delta$ 이고 비는 1이다.

**(b) 근거.** L2 §6.2 ③ 329–361행. 주 식 335–339행, 표 343–348행, 상쇄 예 331–333행과 349–350행, 성립 범위 354–361행. rules.md P6′ 행(22행) ③. glossary g:depth-delay 390–395행(상대 비용 $C_{k,\eta}$ 가 $L$ 에 균일).

**(c) 출처.** 글에 적혀 있음. 나는 예의 $2+\delta$ 와 $2L+1$ 을 다시 계산해 맞는 것을 확인했다(산수).

---

## 9. 막힌 곳

아래는 읽으면서 정의 없이 나왔거나 두 번 읽어야 했던 것들이다. 행은 L2 기준이다.

1. **$n$ 의 세 가지 뜻.** 6.1 Q_k 확률의 $n$ 은 leaf 수(243행, "leaf가 $n$ 개일 때"). 6.2의 $n_\beta$ 는 vertex의 자식 수(236행, 284행). 6.1 254행의 $n\to0$ 도 replica 수다. 같은 글자가 세 대상을 뜻해서 여러 번 확인했다.
2. **$n_\beta$ 의 시점.** 284행 "그 걸음을 하기 직전 현재 tree에서"를 두 번 읽었다. old tree의 자식 수라고 읽으면 틀린다.
3. **"old tree와 무관하다"의 일반 증명.** 319–321행의 "부분 tree의 모든 선택을 더하면 $m_{d+1}$" 은 문장으로만 주어졌다. 예 1의 $a'$ 가지로 확인되고 leaf 하나짜리 부분 tree는 내가 확인했다. 여러 leaf짜리 부분 tree의 일반 증명은 이 파일들에 없다.
4. **$\mathfrak E(\cdot)$ 와 $\mathcal C$ 가 식 뒤에 정의됨.** P7 주 식 374행에 $\mathfrak E$ 와 $\mathcal C$ 가 나오고 정의는 380–381행에 있다. $\mathcal C$ 의 정확한 조건은 386행 "처방할 수 있는 것" 단락에 흩어져 있다. 식을 처음 볼 때 막혔다.
5. **$S$ 가 셋을 뜻한다.** 6.1 231행의 $R_S$ 에서는 replica 집합, 6.2 ②의 $S$ 는 anchor와 color의 모양, 7.1 447행의 $S$ 는 labeled topology다. 7.2에는 $S^+$, $S^U$ 도 나온다.
6. **$S^+$ 가 정의되지 않았다.** 352행과 465행, glossary g:depth-delay 391행에 $J=\kappa(S^+)^2$ 가 나오는데 $S\to S^+$ 연산의 정의가 없다. 산문으로 "한 칸 늦춘 target"이라고만 한다.
7. **$b$ 가 둘을 뜻한다.** 6.2 ③의 $b_{\rm sep}$ 와 7.1의 $b=b(S)$(branching vertex 수)가 다르다. 352행이 "기호 주의"로 해명하지만 처음 읽을 때 혼동했다.
8. **$G$ 와 $H$.** 273행 "원문과 카드에서는 $H$". 같은 글자 $H$ 는 g:field의 장 상계 $|h|\le H$ 에도 쓰인다.
9. **$\Pi, \Xi_N$ 과 $J, H_N$ 의 이름 두 벌.** 6.3 단계 1(401–404행)은 $\Pi$, $\Xi_N$ 을 쓰고 glossary g:palm-identity는 $J_{N,\mathcal T}$, $H_N$ 을 쓴다. 404행에 "원문 기호로는 $\Pi=J$, $\Xi_N=H_N$" 이라는 말이 있어 맞출 수 있었다.
10. **단계 3 (408행)의 논법.** "$|\Xi(1/j)|\le2Cj^{-j}$ 와 $|\Xi(1/j)|\ge cj^{-q}$ 가 모순"이라는 부분은 따라갔다. 그런데 상한 $2Cj^{-j}$ 가 "단계 1과 $u$ 미분의 균일 경계"에서 나온다는 주장의 근거는 이 파일들에 없다. 찾지 못함.
11. **단계 4 (410행) polarization.** "대칭 다중선형식을 되찾는 항등식"이라고 하고 $g=k^{-1}\sum_j\epsilon_jg_j$, $k!\,[t^k]\Xi_N$ 의 꼴은 주어졌다. 그러나 이 일차결합이 왜 혼합 미분을 주는지는 적혀 있지 않다. 다시 읽었지만 찾지 못함.
12. **"protected" 가 된다는 말.** 289행 "한 번 고른 leaf와 새로 붙은 leaf도 $D_j/A$ 를 받으면서 protected가 된다"는 미분 규칙에서 나오는데 그 유도는 [[tree:first-variation]] 블랙박스다. 받아들이고 넘어갔다.
13. **Taylor 계수 소거의 "$u$ 를 $t$ 의 모든 거듭제곱보다 작게"** (perturbations 40–43 인용, glossary g:palm-identity 377행). 의미는 따라갔지만 이 파일에서는 $u\in[j^{-j},2j^{-j}]$ 와 $t=1/j$ 의 관계를 명시적으로 세는 곳이 없어서 한 번 더 확인했다.
14. **6.1 설정 228행.** "6.1과 6.2의 ①, ②는 일반 격자에서 성립"하고 ③은 균등이라는 구분은 읽었다. 표 355행에 같은 말이 있어 일치한다.

---

## 요약

- 1–7번: 글에 적혀 있음. 3번은 계산을 직접 다시 세어 $-1$ 을 확인했다. 5번의 "무관성"과 6번의 "분리"는 글의 주장을 따른 것이다.
- 8번: 글에 적혀 있음. 계수 한계의 상수와 비는 주장대로 나온다.
- 막힌 곳 대부분은 기호(같은 글자 여러 뜻, 식 뒤의 정의, $S^+$ 미정의)와, 증명이 카드로 넘어간 곳(부분 tree 합, Palm 항등식, 단계 3의 상한, polarization)이다.
