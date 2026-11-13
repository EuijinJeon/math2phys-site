# 독자 시험 답안 (v1, Sonnet)

읽은 것: L0, L1, rules, L2 1–7.2절 일부(§6 전부 포함, 6.1–6.4), questions.md. glossary.md는 열지 않았다(링크 [[g:...]] 항목은 못 본 채로 답했고, 그런 곳은 아래에 표시한다). 행 번호는 /tmp/reader-in-v1/ 아래 파일 기준.

---

## 1. 주 식

(a) P6′ ①의 주 식:
$$\partial_{t_1}\cdots\partial_{t_k}\,E^{A_{\boldsymbol t}}_{\mathcal T}\!\Big[\tfrac{G}{A_{\boldsymbol t}^{a_*}}\Big]\Big\rvert_{\boldsymbol t=0}=\sum_E c_E\,E_{\mathcal T_E}\Big[G\prod_{j=1}^kD_j^{a_j(E)}\Big].$$
- 좌변: 삽입 $A_{\boldsymbol t}=1+\sum_jt_jD_j$ 로 바뀐 kernel $K^A_d$ 로 old tree $\mathcal T$ 를 뽑는 기대값 $E^{A_{\boldsymbol t}}_{\mathcal T}$ 아래에서 $G/A^{a_*}_{\boldsymbol t}$ (anchor leaf의 삽입 인자 $A^{a_*}$ 를 분모로 상쇄한 양)를 평균한 것을, $t_1,\ldots,t_k$ 로 각각 한 번씩(혼합 미분, factorial 없음) 미분해 $\boldsymbol t=0$ 에서 읽은 값. 밀도로는 $E_{\mathcal T}[G\prod_{a\ne a_*}A^a\prod_\beta Y_\beta^{\gamma_\beta}]$ (L2 268행).
- 우변: extension history $E$ 에 대한 유한 합. 각 항은 계수 $c_E$ × (history가 만든 마지막 tree $\mathcal T_E$ 를 삽입 없는 원래 kernel로 뽑아 $G$ 와 "color $j$ 를 받은 leaf $a_j(E)$ 에서 본 $D_j$" 들의 곱을 평균한 값).
- $G$ 는 old tree 변수의 유계 함수(t 무관), $D_j$ 는 유계 실수 path 함수.

(b) L2 §6.2 ① 265–269행; rules.md P6′ 22행.
(c) 글에 적혀 있음.

---

## 2. $c_E$ 의 정의

(a) extension history $E$: old tree에서 시작해 color $1,\ldots,k$ 를 차례로 leaf에 주는 선택의 기록. color마다 한 걸음, 선택지는 둘:
- (i) 재사용: anchor가 아니고 아직 color를 받지 않은 old leaf 하나에 준다. 계수 $+1$.
- (ii) fresh path: 현재 tree의 내부 vertex $\beta$ 하나를 골라 거기에 새 자식을 만들고 깊이 $L$ 까지 새 path를 이어, 그 끝 새 leaf에 color를 준다. 계수 $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}<0$.

$n_\beta$ = **그 걸음을 하기 직전의 현재 tree에서 $\beta$ 가 가진 자식 수**. 현재 tree = old path 전부(color 안 받은 것, anchor 포함) + 앞 걸음들에서 붙인 fresh path 전부. old tree만의 자식 수가 아니고, 앞 걸음의 fresh path가 $\beta$ 에 더한 자식도 센다. $\beta$ 는 anchor path 위 vertex도 될 수 있고 unary(자식 1개) vertex도 된다. 이미 color 받은 leaf와 anchor는 재사용 불가. $c_E$ = 걸음별 계수의 곱(부호가 섞이며 확률 가중치가 아님), $k=0$ 이면 빈 history 하나, 계수 1. $\mathcal T_E$ = 마지막 tree, $a_j(E)$ = color $j$ 를 받은 leaf.

(b) L2 276–287행(표와 불릿); 정의의 출처 rules.md P6′ 22행.
(c) 글에 적혀 있음. ($[[g:extension-history]]$ 용어집 항목은 안 봄.)

---

## 3. 계산

설정: old tree = anchor $a_*$ 와 다른 leaf $a'$ (질문의 "$b$" 는 L2에서 $a'$ 로 쓰임) 둘이 깊이 $s$ 에서 갈라짐. $k=1$, $G=1$, $D=1$, $m_0=0$, $m_L=1$.

내부 vertex(= history 후보): 공통 줄기 깊이 $0,\ldots,s-1$ ($s$ 개, 자식 1개), 갈라지는 깊이 $s$ vertex (1개, 자식 2개), anchor 가지 깊이 $s+1,\ldots,L-1$ ($L-1-s$ 개, 자식 1개), $a'$ 가지 깊이 $s+1,\ldots,L-1$ ($L-1-s$ 개, 자식 1개). 걸음 하나이므로 $n_\beta$ 는 old tree의 자식 수.

| history | 개수 | $c_E$ |
|---|---|---|
| $a'$ 재사용 | 1 | $+1$ |
| 줄기 깊이 $d<s$ 에서 fresh | $s$ | $m_d-m_{d+1}$ ($d=0..s-1$) |
| 깊이 $s$ (자식 2개)에서 fresh | 1 | $m_s-2m_{s+1}$ |
| anchor 가지 깊이 $\ell>s$ 에서 fresh | $L-1-s$ | $m_\ell-m_{\ell+1}$ |
| $a'$ 가지 깊이 $\ell>s$ 에서 fresh | $L-1-s$ | $m_\ell-m_{\ell+1}$ |

총 history 수: $1+s+1+2(L-1-s)=2L-s$ 개. $G=D=1$ 이라 각 $E_{\mathcal T_E}[\cdot]=1$ 이므로 우변 = 계수의 합.

합:
- 줄기: $\sum_{d=0}^{s-1}(m_d-m_{d+1})=m_0-m_s$ (telescoping)
- 깊이 $s$: $m_s-2m_{s+1}$
- 두 가지: $2\sum_{\ell=s+1}^{L-1}(m_\ell-m_{\ell+1})=2(m_{s+1}-m_L)$

$$1+(m_0-m_s)+(m_s-2m_{s+1})+2(m_{s+1}-m_L)=1+m_0-2m_L=1+0-2=-1.$$
(균등 격자를 쓸 필요 없이 일반 격자에서 성립.)

좌변: $A=1+t$ 는 (path에 안 의존하는) 상수라서 모든 깊이에서 $Y_d=1+t$, $K^A_d=(Y_d/Y_{d-1})^{m_d}K_d=K_d$ (법칙 불변). 그러면 $E^A_{\mathcal T}[1/A^{a_*}]=(1+t)^{-1}$, $\partial_t|_{t=0}=-1$. 우변 $-1$ 과 일치. 확인됨.

(b) L2 291–303행(계산 예 1)이 같은 계산을 한다. 나는 표의 각 계수를 정의(276–286행)에서 다시 유도해 합을 직접 계산했고 값이 같았다.
(c) 글에 적혀 있음(예 1) + 내가 정의에서 재계산함(글에서 추론함).

---

## 4. anchor

(a) 왜 anchor의 인자만 상쇄하는가: 고른 규약이 아니라 Palm 단계(단계 1)에서 저절로 나온다. 집중하는 양이 $u$ 미분 꼴의 score $D_\nu=\sum g_0S_0/\psi$ 이고, Palm 항등식으로 골라낸 섭동 항 하나가 anchor 쪽에서 $\partial_u\log A=g_0S_0/A^{a_*}$ 를 낸다. 이 분모가 밀도 $W_{\mathcal T}(A)$ 의 anchor leaf 인자 $A^{a_*}$ 를 지운다. 그래서 단계 1이 내는 양이 정확히 "anchor가 protected인 바뀐 법칙의 tree 기대값", 곧 P6′ ①의 좌변이다(anchor는 history 선택지에서 빠진다). 이 상쇄는 anchor 하나(score를 읽는 replica)에 대해서만 생기고 다른 old leaf나 새 leaf의 $A$ 인자는 그대로 남는다.

P7과의 연결: $G=f\,g_0^{a_*}S_0^{a_*}$ 로 두면 $\Pi_{N,\mathcal T}(t,u)=\mathbb E\,E^A_{\mathcal T}[f g_0S_0/A^{a_*}]$ 가 P6′ ① 좌변. old tree가 $\mathcal T$ 일 때 ①을 풀면 P7의 첫째 합 $\sum_{E\in\mathfrak E(\mathcal T,a_*,\mathcal C)}c_E\mathbb E[fR_E]$ 가, anchor 하나뿐인 tree에 시험함수 1로 쓴 $\Pi_{N,\{a_*\}}$ 에서 둘째 합이 나온다. $\Xi_N=\Pi_{N,\mathcal T}-\mathbb Ef\,\Pi_{N,\{a_*\}}$ 가 단계 1에서 $|\Xi_N|\le\|f\|_\infty e_{\nu,N}$ (score 집중, P5(ii))로 작고, 단계 2–5(Taylor 계수 소거, polarization, selector·site 평균)로 P7의 식이 된다.

(b) L2 §6.2 목적 259행, 6.3 "단계 0–1" 396–404행, "anchor를 왜 상쇄하는가" 414행; rules.md P7 23행.
(c) 글에 적혀 있음. (다만 "anchor가 spin anchor/marker anchor 두 종류" 구별이 왜 필요한지는 P8·P9 쪽 이야기라 이 절만으로는 못 봄.)

---

## 5. 모양별 총합

(a) $\kappa(S)$: 모양 $S$(anchor와 color $k$ 개의 path만으로 된 tree, 곧 그들 사이 쌍별 split 깊이 전부)를 갖는 **모든 history의 계수 $c_E$ 의 합**. $\kappa(S)=\prod_{v\in\mathrm{Br}(S)}\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$.

old tree 무관 이유(글의 논증): 한 걸음에서 새 color가 reference(anchor와 color 받은 path)를 따라 깊이 $d$ vertex $v$ 까지 가서 reference가 안 지나는 쪽으로 가야 한다. $v$ 의 현재 자식 수 $n$, reference가 지나는 자식 $j$ 개. 선택 (1) $v$ 에서 바로 fresh: $m_d-nm_{d+1}$. (2) reference가 안 지나는 $n-j$ 개 자식 중 하나로 들어감: 그 아래 부분 tree는 color 안 받은 old path만이고, 그 안의 모든 선택(old leaf 재사용 $+1$들과 fresh 계수들)의 합은 부분 tree 모양과 무관하게 $m_{d+1}$ (telescoping). 합: $(m_d-nm_{d+1})+(n-j)m_{d+1}=m_d-jm_{d+1}$, $n$ 소거. 확인: 예 1의 $a'$ 가지에서 $+1+(m_{s+1}-1)=m_{s+1}$ (L2 321행). 걸음을 곱하면 branching vertex에서 새 가지가 열릴 때마다 $j=1..a_v-1$ 인자가 하나씩.

anchor와 새 replica 하나가 깊이 $d$ 에서 갈라지는 $S$: branching vertex 하나, $a_v=2$, 따라서 $\kappa(S)=m_d-m_{d+1}$. 격자 $m_d=d/L$ 에서 $\kappa(S)=-1/L=-\delta$ (모든 $d$ 에서 같은 값). 예 1로 검산: $d<s$, $d>s$ 는 history 하나(계수 $-\delta$), $d=s$ 는 $1+(m_s-2m_{s+1})+(m_{s+1}-1)=m_s-m_{s+1}=-\delta$. 전부 더하면 $L\cdot(-\delta)=-1$, 3번과 일치.

(b) L2 §6.2 ② 309–325행.
(c) 글에 적혀 있음. 단 "부분 tree 안 모든 선택의 합이 $m_{d+1}$" 자체의 증명은 글에 없고 `tree:reference-total` 블랙박스(363행)로 넘어간다. 나는 예 1 하나로만 확인했다.

---

## 6. P7

(a)
- $f$: old tree의 replica들의 multioverlap으로 쓴 유계 다항식(시험함수), $N$ 과 삽입 매개변수에 따라 바뀌지 않음.
- $E$, $c_E$: P6′의 extension history와 계수.
- $R_E$: history가 고른 새 replica들의 multioverlap. spin anchor면 anchor 포함 $\frac1N\sum_i\sigma_i^{a_*}\prod_j\sigma_i^{a_j(E)}$, marker anchor면 anchor 빼고 $\frac1N\sum_i\prod_j\sigma_i^{a_j(E)}$.
- 첫째 합의 범위: $\mathfrak E(\mathcal T,a_*,\mathcal C)$ = old tree $\mathcal T$ 에서 시작해 제약 $\mathcal C$ 를 지키는 history 전부. 둘째 합의 범위: $\mathfrak E(\{a_*\},a_*,\mathcal C)$ = anchor 하나뿐인 tree에서 시작해 같은 $\mathcal C$ 를 지키는 history 전부. $\mathcal C$ = anchor와 새 color들로 된 집합 안의 쌍별 split 깊이에 대한, 서로 일관된 지정(mark selector로 고름; 새 replica끼리의 쌍 포함, 다른 old replica가 낀 쌍은 지정 못 함). $k\ge0$ 허용.
- $\mathbb E$: 선택된 수열 reservoir에서 root 평균과 tree 표본 포함, 삽입 없는 원래 법칙.

말로: 첫째 합은 old tree가 있는 자리에서 anchor 옆에 새 replica들을 붙이고 $f$ 와 함께 평균한 것, 둘째는 old tree를 치우고 anchor만 둔 자리에서 같은 일을 한 것. 항등식은 첫째 $\approx\mathbb Ef\times$ 둘째, 곧 anchor에 새 섭동 하나를 더한 효과가 old tree의 시험함수와 분리된다는 뜻. 분리되는 것은 history 하나하나가 아니라 계수를 붙인 부호 있는 합.

극한: 선택된 수열(P5)을 따라 $N\to\infty$, 고정한 $L$, old tree, anchor 종류, $f$, $k$, 제약 $\mathcal C$ 마다. 수렴 속도와 $L$·tree 크기·type에 대한 균일성은 주장되지 않음.

(b) L2 §6.3 373–392행, 419–423행; rules.md P7 23행.
(c) 글에 적혀 있음.

---

## 7. 흐름

(a) 수 4가 받는 것: 수 3(P5)의 선택된 수열과 그 위의 (ii) score 집중, (iii) tree 모멘트 수렴; 수 2의 reservoir·섭동 구성; 6.1의 유한 kernel 열·tree 표본 규칙·log 전개와 같은 미분 규칙(P6). 수 4가 수 5에 넘기는 것: ① P7 항등식(+ tree 표본 규칙) — 수 5가 모형에서 받는 입력은 이것뿐; ② 6.2의 유한 tree 조합 두 가지, 모양별 총합 $\kappa(S)$ (항등식 정규화용)와 절댓값 합 계수 한계(정규화 후 오차 제어). 수 6은 P7이 아니라 6.1의 log 전개를 따로 직접 쓴다. 항등식은 물리적 Gibbs 측도의 계층 구조나 overlap 극한값은 주지 않는다.

(b) L2 214–220행(표), 427–433행(6.4); L1 수 4(23행)·수 5(28행).
(c) 글에 적혀 있음.

---

## 8. 계수 한계

(a)
- $\delta^b$ 크기로 작은 것: 절댓값 합 $\sum_{E\text{ 허용}}|c_E|\le C_{q,k}\,\delta^{b_{\rm sep}}$. 또 $|J_{\rm sep}|$ 도 같은 차수($\delta^{b_{\rm sep}}\eta^{\sum_v(a_v-2)}$ 이상, $k^k\delta^{b_{\rm sep}}$ 이하). 여기서 $b_{\rm sep}$ 는 처방 모양의 branching vertex 중 깊이가 old tree의 어느 branching 깊이와도 다른 것의 수(L1/수 5의 $b$, $J=\kappa(S^+)^2$ 는 떨어진 vertex가 $2b$ 개인 경우). 이유: 그런 vertex는 old tree에서 unary라 누군가 fresh로 갈라져 만들어야 하고 그 계수가 $m_d-m_{d+1}=-\delta$.
- $L$ 에 균일하게 유계인 것: 상수 $C_{q,k}$, $C_{q,k,\eta}$ (old leaf 수 $q$, color 수 $k$, $\eta$ 에만 의존), 그리고 **비** $\frac1{|J_{\rm sep}|}\sum_E|c_E|\le C_{q,k,\eta}$ (그 vertex 모두에서 $m_{d_v}\ge\eta$ 일 때). 절댓값 합 자체나 $|J_{\rm sep}|$ 는 $L$ 에 균일한 양의 하한이 없고 $b_{\rm sep}\ge1$ 이면 0으로 간다. 균등 격자 $m_d=d/L$ 에서만 진술.

(b) L2 §6.2 ③ 327–352행(특히 343–350행 표); rules.md P6′ 22행; L1 수 5(28행).
(c) 글에 적혀 있음.

---

## 9. 막힌 곳

1. **기호 충돌과 대응 (가장 자주 멈춤).**
   - 질문지는 "다른 replica $b$"와 "$H$"를 쓰는데 L2는 $a'$ 와 $G$ 를 쓴다(273행 "원문과 카드에서는 $H$"로 한 번만 언급). 질문지와 글의 기호 대응을 내가 맞춰야 했다. 3번에서 $a'$ 와 $b$ 를 같은 것으로 추측했다.
   - $b$: 1.1절에서 factorization의 계수 $b$($e^\theta=a(1+b\prod f)$), L1 수 5에서 "$S$ 의 branching vertex 수 $b$", rules/L2에서 $b_{\rm sep}$. 같은 문자를 세 뜻으로 읽는다. 352행 "기호 주의"가 있으나 6.2 한복판에서야 나옴.
   - $E$: extension history $E$, 기대값 $\mathbb E$, $E_{\mathcal T}$, $E^A_{\mathcal T}$, $\mathfrak E$, 그리고 $E$ = history 속 $E$ 가 한 문장에 섞임(예 266행 우변 $\sum_E c_E E_{\mathcal T_E}[\cdot]$). 처음 읽을 때 "$\sum_E$ 의 $E$ 와 $E_{\mathcal T_E}$ 의 $E$" 구별에 한참 걸림.
   - $n_\beta$ 가 6.1(235–236행)에서는 "$\mathcal T$ 에서 $\beta$ 의 자식 수", 6.2(284행)에서는 "그 걸음 직전 현재 tree에서의 자식 수", 그리고 $Q_k$ 정의(242행)에서 $n$ 은 leaf 수. 6.1의 $n_\beta$ 는 고정된 $\mathcal T$ 의 값이고 6.2의 것은 걸음마다 바뀌는 값인데, 6.2 쪽을 굵게 강조한 것 외에는 두 뜻의 연결이 안 적혀 있다(둘이 같은 공식에서 왔다는 점을 추론해야 함).
   - $G$ 가 "old tree 변수의 유계 함수"로만 정의되어 6.3에서야 $f\,g_0S_0$ 라는 실체가 나옴. 6.2에서는 $G=1$ 예제만 있어 $G$ 의 역할(6.3과의 연결)이 앞에서 안 보임.
2. **정의 없이 나온 것.**
   - "color"가 274행에서 정의("새로 붙는 replica에 붙인 번호")되지만 265행 주 식에서 이미 "$D_j$ 와 짝"으로 쓰고 $a_j(E)$ 를 "color $j$ 를 받은 leaf"라 부른다. 정의가 사용보다 뒤.
   - "protected leaf"([[g:protected-leaf]])는 289행에서 한 문장으로 설명되나 정의로는 용어집에 있다고만 되어 있고 나는 못 봄. 왜 "anchor가 protected이면 history 선택지에서 빠지는가"가 288–289행 두 문장 + 414행으로 흩어져 있어 다시 읽었다.
   - $\mathfrak E(\mathcal T,a_*,\mathcal C)$ 의 "$\mathcal C$ 를 지키는 history"가 정확히 어떤 history인지(split 깊이 지정이 history의 어느 걸음에서 어떻게 걸러지는지)는 386행 "처방할 수 있는 것" 단락이 mark 평균으로 "정확히 $d$"를 고른다고만 말해 정확한 조건이 안 보인다. "지정"과 "일관"의 정의가 없음.
   - $\mathrm{Br}(S)$ 의 "$S$ 안에서 자식 수 $a_v$" — $S$ 는 anchor와 color 받은 leaf만 남긴 tree이므로 unary 제거 후의 자식 수인데 313행과 317행 사이에서 "branching vertex만 센다"는 점이 한 번 더 확인해야 했다.
   - $R_E$ 에서 marker anchor(anchor를 뺌)와 spin anchor가 왜 구별되는지는 이 절에서 안 설명(P9 쪽 이야기).
3. **다시 읽은 문장.**
   - 319행 "새 color가 깊이 $d$ 의 vertex $v$ 까지 reference를 따라가다가, reference가 지나는 $j$ 개의 자식이 아닌 쪽으로 가야 한다고 하자." — "$j$ 개의 자식"의 $j$ 가 뭔지(reference들이 이미 지나가는 자식 수) 문장만으로는 안 보이고, 뒤 $(n-j)$ 를 보고서야 추론함. $j$ 가 곧 $\kappa$ 의 곱 인덱스 $j=1..a_v-1$ 와 같다는 연결도 321행 마지막 문장에서 압축적으로만 나옴.
   - 320–321행: "부분 tree 안의 모든 선택을 더하면 부분 tree의 모양과 무관하게 $m_{d+1}$" — 이것의 증명이 없고 예 1의 $a'$ 가지 하나로만 확인된다. 일반 부분 tree(old leaf 여러 개, 가지 여러 개)에서 맞는지는 글에서 확인 불가(블랙박스 `tree:reference-total`).
   - 331–333행 상쇄 예: "허용되는 history는 위의 셋이다"에서 "셋"이 history 세 개가 아니라 표의 세 종류(재사용, 깊이 $s$ fresh, $a'$ 가지 fresh $L-1-s$ 개)라는 것을 계산 $1+(s+2)\delta+(L-1-s)\delta$ 를 보고서야 알았다. 같은 문단 앞의 줄기 $d<s$ 와 anchor 가지 fresh가 왜 제외되는지(깊이 $s$ 정확히 갈라짐 처방과 충돌)는 설명이 없어 내가 따져야 했다.
   - 346–347행 표: $|J_{\rm sep}|$ 의 상한 $k^k\delta^{b}$ 는 359행에서 "인자의 크기에서 읽은 것"이라 해서 증명되지 않은 것을 표에 같은 격으로 넣은 듯 보임.
   - 347행: 하한 $\delta^{b_{\rm sep}}\eta^{\sum_v(a_v-2)}$ 의 지수 $\sum_v(a_v-2)$ 에서 $a_v=2$ 일 때 지수 0인 점(인자 $j=1$ 하나는 $-\delta$ 그 자체)이 이유 설명 없이 나옴. $L$ 에 균일한 하한이 없다는 말과 "하한이 있다"는 말(식은 $\delta$ 에 의존)이 한 칸에서 섞여 읽힘.
   - 6.3 "어디서 오는가" 단계 3: $\Xi$ 의 첫 0 아닌 계수가 $q$ 차라면 $|\Xi(1/j)|\ge cj^{-q}$ 라는 논법은 이해되지만 "$u_\nu\in[j^{-j},2j^{-j}]$" 와 $t_\nu=1/j$ 가 선택된 수열의 어느 단계에서 주어지는지는 5절과 연결이 안 되어 한 번 되돌아가서 확인. (Taylor 계수 소거는 블랙박스라 내용 점검은 못 함.)
4. **글에 없는 것을 내 지식이 메운 곳 / 못 메운 곳.**
   - $\gamma_\beta$, power mean, $Q_k$ 에 대해 "Parisi block counting", "Ruelle cascade"는 내 배경에서 연상하지만 글이 증명도 사용도 안 한다고 명시하므로 답에서는 쓰지 않았다. 다만 $c_E$ 의 부호가 섞인다는 점을 보면서 replica $n\to0$ 의 부호 있는 계수를 떠올렸고 글이 그 연결을 부정한다(361행)는 것은 확인.
   - 단계 0–1의 Palm 항등식을 글이 "골라낸 항은 독립인 새 항 하나"라고만 설명하므로, 이 설명만으로 $\Pi_{N,\mathcal T}$ 식이 나오는 계산은 재현하지 못했다(블랙박스로 받아들임).
   - 6.2 ① 자체의 증명(미분 규칙 $\partial_t\log W_{\mathcal T}=\ldots$ 가 (i),(ii)와 protected leaf 회계로 어떻게 정확히 이어지는지)은 289행 한 문단뿐이라 직접 검산하지 못함. 내가 검산한 것은 $L=1$ anchor 하나(예 2)와 old leaf 둘 예 1의 상수 $A$ 경우 둘뿐이고, 이 두 경우는 $D$ 가 상수이거나 $k=1$ 이라 history가 길어지는 경우(예: $k\ge2$ 에서 앞 걸음의 fresh path가 $n_\beta$ 를 바꾸는 효과)는 점검하지 못했다. $k\ge2$ 예가 하나도 없다.
5. **구성상 한 줄 지적.** 6절 서두 표(216–220행)는 "받는 것/넘기는 것" 열이 간결해 좋지만, 정작 6.2 ②가 "수 5에 넘기는 $\kappa(S)$" 라고 하면서 $\kappa(S)$ 가 수 5에서 정확히 어디(항등식 양변의 정규화 $J=\kappa(S^+)^2$)에 쓰이는지는 352행("기호 주의")과 L1 수 5(28행)에서야 보인다. 6.4(429행)는 일반적으로만 말한다.
