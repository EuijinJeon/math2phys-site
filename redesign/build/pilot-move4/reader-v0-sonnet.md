# 독자 시험 답안 (v0, 독자: Sonnet)

읽은 것: questions.md, L1, L2 (1–7.3절까지 읽었고 7.3 이후는 읽지 않음; 아래 질문은 §6 중심이라 필요하지 않았음), rules.md의 P4–P10 행, glossary의 모형·변분·계층·tree 항목들. L0은 열지 않았다.
표기: (c)의 "글에 적혀 있음" 등은 질문지의 네 가지 중 하나. 한 답 안에서 부분마다 출처가 다르면 부분별로 적었다.
중요한 사전 고백: **L2 §6만으로는 Q1, Q2가 답이 안 된다.** P6′의 실제 식은 L2 §6.2에 수식으로 없고 rules.md P6′ 행과 용어집에만 있다. 아래는 그 둘을 합쳐 답한 것이다(글 안에서 찾은 것이지 내 지식으로 메운 것은 아니다).

---

## 1. 주 식

**(a)** rules.md P6′ 행의 "정확한 꼴"이 주 식이다.

$$\partial_{t_1}\cdots\partial_{t_k}\,E^{A_{\boldsymbol t}}_{\mathcal T}\!\Big[\tfrac{H}{A^{a_*}_{\boldsymbol t}}\Big]\Big|_{\boldsymbol t=0}\;=\;\sum_{E}c_E\,E_{\mathcal T_E}\Big[H\prod_{j=1}^kD_j^{a_j(E)}\Big],\qquad A_{\boldsymbol t}=1+\sum_jt_jD_j .$$

- 좌변: old tree $\mathcal T$ 위에서, 삽입 $A_{\boldsymbol t}$ 로 kernel을 바꾼(tilt한) 표본추출에 대한 기대값 $E^{A}_{\mathcal T}$ 안에 $H/A^{a_*}$ 를 넣은 것이다. $H$ 는 old tree 변수의 유계 함수로 삽입 매개변수와 무관하다. $1/A^{a_*}$ 는 anchor leaf의 삽입 인자를 나눠 상쇄하는 것이다. 이것을 섭동 크기 $t_1,\dots,t_k$ 로 각각 한 번씩 미분(혼합 미분)해서 $\boldsymbol t=0$ 에서 취한다. $D_j$ 는 유계 실수 path 함수. root가 주어진 조건부 항등식.
- 우변: 합은 **extension history $E$** (새 replica = color $1..k$ 를 하나씩 붙이는 모든 방법)에 대한 것이다. 각 항은 계수 $c_E$ 곱하기 확장된 tree $\mathcal T_E$ 위의 기대값 $E_{\mathcal T_E}[H\prod_jD_j^{a_j(E)}]$ 이고, $a_j(E)$ 는 color $j$ 가 놓인 leaf로 읽힌다.
- 같은 L2 §6.2 본문(P6′ 전개)은 "결과는 extension history $E$ 마다 계수 $c_E$ 가 붙은 tree 기대값의 합"이라고 말로만 쓴다. 혼합 미분이므로 추가 factorial이 없다(L2 §6.2, rules P6′ "쓰임").

**(b)** rules.md P6′ 행 "정확한 꼴(`tree:extension-expansion`)" 문장; L2 §6.2 "P6′ (전개)" 단락(말로만); glossary g:extension-history, g:protected-leaf.
**(c)** 식 자체와 $H$, $D_j$, $E^A_{\mathcal T}$ 의 역할: 글에 적혀 있음(rules.md). $a_j(E)$, $\mathcal T_E$ 의 뜻("color $j$가 놓인 leaf", "확장된 tree"): 글에서 추론함(glossary 기호 칸에 기호만 있고 뜻풀이는 없다). $E^A_{\mathcal T}$ 가 "tilted kernel 아래의 tree 기대값"이라는 것: 글에서 추론함(g:insertion의 $K^A_d$ 에서).

---

## 2. $c_E$ 의 정의

**(a)**
- extension history $E$: anchor $a_*$ 가 있는 old tree에서 color $1,\dots,k$ 를 **차례로**, 각 color마다 다음 둘 중 하나를 고른 기록.
  1. 아직 안 쓴 anchor 아닌 old leaf에 그 color를 준다: 계수 $+1$.
  2. 현재 tree의 내부 vertex $\beta$ 에서 새 path(fresh path)를 갈라낸다: 계수 $\gamma_\beta=m_{d_\beta}-n_\beta m_{d_\beta+1}$ (깊이 $d_\beta$). 이 새 path는 $\beta$ 에서 새 자식을 쓰고 그보다 깊은 모든 깊이에서 새 vertex를 쓴다. $\gamma_\beta<0$.
  - anchor는 처음부터 상쇄(protected)되어 다시 고를 수 없다.
- $c_E$ = 각 걸음의 계수의 곱. 부호가 섞인다($+1$ 과 음수 $\gamma$).
- $n_\beta$: **그 걸음에서의 현재 tree**(안 쓴 old path와 이미 붙인 path를 모두 포함)에서 $\beta$ 가 가진 자식 수. (rules.md P6′ 행: "그 걸음의 현재 tree(안 쓴 old path와 이미 붙인 path 포함)의 자식 수".) 그래서 $n_\beta\ge1$, $\gamma_\beta<0$ (단조 $m$ 가정 하에).

**(b)** L2 §6.2 "P6′ (전개)"; rules.md P6′ 행 "$\gamma_\beta$ 의 $n_\beta$ 는 …"; glossary g:extension-history, g:tree-coefficient.
**(c)** 선택지와 계수: 글에 적혀 있음. $n_\beta$ 가 "현재 tree의 자식 수(old 포함)": L2 본문에는 없고 rules.md에만 적혀 있음. L2 §6.1 P6은 "$n_\beta$ 는 자식 수"라고만 한다. "fresh path가 $\beta$ 에서 새 자식을 쓰고 아래 모든 깊이에서 새 vertex를 쓴다"는 glossary에 적혀 있음.
**막힘/추측 표시:** "내부 vertex"에 자식이 하나인(unary) vertex가 들어가는지, leaf(깊이 $L$)는 빠지는지는 L2에 없다. 나는 glossary g:depth-delay의 "anchor path 위 깊이 $d+1$ unary vertex의 fresh split 하나뿐"이라는 문장과, 아래 Q3에서 $2+\delta$ 를 재현하는지로 확인해 unary vertex도 포함, 깊이 $0..L-1$ 로 읽었다(글에서 추론함).

---

## 3. 계산

**설정 읽기.** old tree = 두 leaf(anchor $a_*$, 다른 replica $b$), 공통 prefix가 깊이 $0..s$ 의 vertex들이고 깊이 $s$ 에서 갈라진다. 그 아래 각 가지는 깊이 $s+1..L-1$ 의 vertex(자식 1개)를 지나 깊이 $L$ leaf에 닿는다. $k=1$ (새 replica 1개, 한 걸음), $H=D=1$, $m_d=d/L$ ($m_0=0$, $m_L=1$), $\delta=1/L$.

**가능한 history (한 걸음).**

(R) old replica $b$ 를 쓴다(anchor는 못 씀): $c=+1$. 1개.

(F) fresh split, 현재 tree의 내부 vertex $\beta$ (깊이 $d_\beta\in\{0,\dots,L-1\}$)에서. $\gamma_\beta=m_d-n_\beta m_{d+1}$:
- 공통 prefix의 깊이 $d=0,\dots,s-1$ vertex: $n=1$, $\gamma=m_d-m_{d+1}=-\delta$. ($s$ 개)
- 깊이 $s$ 의 분기 vertex: $n=2$, $\gamma=m_s-2m_{s+1}=\frac{s-2(s+1)}{L}=-(s+2)\delta$. (1개)
- anchor 쪽 가지의 깊이 $d=s+1,\dots,L-1$ vertex: $n=1$, $\gamma=-\delta$. ($L-1-s$ 개)
- $b$ 쪽 가지의 깊이 $d=s+1,\dots,L-1$ vertex: $n=1$, $\gamma=-\delta$. ($L-1-s$ 개)

history 총수 $1+s+1+2(L-1-s)=2L-s$.

**전체 합 (제약 없음).**
$$\sum_Ec_E=1-\delta\big[s+(s+2)+2(L-1-s)\big]=1-\delta\cdot 2L=1-2=-1 .$$

**P6′ 좌변과 대조.** (i) $D=1$, $H=1$ 이면 $A_t=1+t$ 는 상수라 모든 $Y_d=A$, 따라서 $K^A_d=(Y_d/Y_{d-1})^{m_d}K_d=K_d$ (kernel 불변). 그러면 좌변은 $\partial_t E[1/(1+t)]|_0=\partial_t(1+t)^{-1}|_0=-1$. 우변의 $E_{\mathcal T_E}[1]=1$ 이므로 합이 곧 $\sum c_E=-1$. 일치. (ii) 모양별로도 확인: 새 replica가 anchor와 깊이 $d$ 에서 갈라지는 history들의 합.
- $d<s$: fresh 하나, $-\delta$.
- $d>s$: anchor 쪽 가지 깊이 $d$ 의 fresh 하나, $-\delta$.
- $d=s$: (R) $+1$, 깊이 $s$ vertex의 fresh $-(s+2)\delta$, $b$ 쪽 가지의 fresh $(L-1-s)$ 개 각 $-\delta$ (이들은 $b$ 아래에서 갈라져 anchor와는 깊이 $s$ 에서 갈라진다). 합 $=1-(s+2)\delta-(L-1-s)\delta=1-(L+1)\delta=-\delta$.
따라서 모든 $d=0..L-1$ 에서 $-\delta$ 이고 $L\cdot(-\delta)=-1$ 로 위 총합과 같다. 또 $\kappa(S)=m_d-m_{d+1}=-\delta$ (Q5)와도 같다. 
- 처방 $d=s$ 로 제약을 걸면 부호 있는 합 $-\delta$, 절댓값 합 $1+(s+2)\delta+(L-1-s)\delta=1+(L+1)\delta=2+\delta$. 이것이 L2 §6.2의 "부호 있는 합 $-\delta$, 절댓값 합 $2+\delta$" 예와 일치한다(이 일치로 내 vertex 읽기를 확인).
- $d=s$ 의 old subtree(분기 vertex의 다른 자식 아래: (R) + $b$ 쪽 fresh들)의 합은 $1-(L-1-s)\delta=m_{s+1}$ 로 "reference 없는 old 부분 tree의 합이 $m_{d+1}$" telescoping과 맞다.

**(b)** L2 §6.2 "P6′ (전개)", "(모양별 총합)", "왜 이것이 필요한가"; rules.md P6′ 행; glossary g:depth-delay.
**(c)** history 나열과 계수 공식: 글에 적혀 있음(공식), 내 계산은 산수. "unary vertex 포함, 깊이 $0..L-1$" 선택: 글에서 추론함. "좌변 값 $-1$" 도출(kernel 불변): 글에서 추론함(g:insertion의 $K^A_d$ 정의와 g:power-mean의 동차성 문장으로). 이 좌변 계산은 L2에는 없고 내가 한 것이다.

---

## 4. anchor

**(a)** 
- 왜 anchor만 상쇄하나: L2 본문은 이유를 말하지 않는다. 쓰여 있는 것: (L2 §6.3) Poisson add-one(Palm) 항등식이 score 곱을 "anchor에 새 섭동 하나를 넣은 tree 기대값"으로 바꾼다; (glossary g:protected-leaf) "Palm 단계에서 anchor 인자 $A^{a_*}$ 가 상쇄되는 것이 이 상황"이다. 내 추론: score $D_\nu=\sum_q g_{0,q}S_{0,q}/(1+t_\nu g_q\sigma_{i_q}+u_\nu g_{0,q}S_{0,q})$ (g:score)는 **한 path(anchor)** 위의 값이고 분모가 그 path의 삽입 인자다. 그래서 $E[fD_\nu^{a_*}]$ 를 삽입 $A$ 로 쓰면 $H/A^{a_*}$ 꼴이 나온다. 다른 old leaf들의 인자는 tree 밀도 $\prod_aA^a$ 에 남아 tilt를 바꾼다(그래서 old tree의 $f$ 와 얽힘이 새 replica 쪽으로 번지는 것이 $c_E$ 로 계산된다).
- P7과의 연결: P6′ 좌변($H=f$, old tree $\mathcal T$)이 Palm 항등식의 $J_{N,\mathcal T}(t,u)$ 이고, anchor 하나만의 tree $\{a_*\}$ 에서 같은 것이 $J_{N,\{a_*\}}$. 차이 $H_N=J_{N,\mathcal T}-\mathbb Ef\,J_{N,\{a_*\}}$ 가 score 오차 $\le\|f\|_\infty e_{\nu,N}\to0$ 로 눌린다(P5(ii)). 이 $H_N(t,u)$ 의 $t$ 에 대한 Taylor 계수를 P6′ 으로 history 합으로 풀면 P7의 첫 합(old tree $\mathcal T$, 시험함수 $f$ 가 $H$ 자리)과 둘째 합(tree $\{a_*\}$, $\mathbb Ef$ 가 앞에 붙음)이 된다. $D_j^{a_j}$ 들의 곱이 $R_E$ 로 가는 것은 polarization과 mark selector로(L2 §6.3 "어디서 오는가").

**(b)** L2 §6.3 "어디서 오는가"; L2 §6.2 첫 문단, "anchor는 처음부터 상쇄되어"; glossary g:protected-leaf(역할), g:palm-identity(기호·뜻), g:score(기호), g:tree-identity.
**(c)** Palm 항등식이 $J_{N,\mathcal T}$ 와 $H_N$ 으로 이어지는 연결: 글에 적혀 있음(glossary). "왜 하필 anchor 한 leaf만"의 이유: **글에서 추론함**(score의 분모와 $H/A^{a_*}$ 의 대응을 내가 맞춘 것, 어디에도 이 문장이 없다). $D_j$ 가 $\to R_E$ 로 가는 구체적 경로: 찾지 못함(L2는 "polarization과 mark selector"라고 이름만 쓴다).

---

## 5. 모양별 총합

**(a)**
- $\kappa(S)=\prod_{v\in\mathrm{Br}(S)}\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$ 는, 처방한 모양 $S$(anchor와 새 replica들이 이루는 갈라짐 모양)를 갖는 **모든 extension history의 $c_E$ 의 합**이다. (glossary: "anchor와 color가 모양 $S$ 를 갖는 모든 확장의 계수 합".)
- old tree와 무관한 이유(글의 설명): 처방은 reference path(anchor와 이미 붙인 path)와의 split 깊이만 지정하고 그 아래 "쓰지 않은 old 부분 tree"는 구별하지 않는다. reference가 없는 old 부분 tree에서의 계수 합이 $m_{d+1}$ 로 telescoping되어 old tree 모양이 지워진다. 나는 Q3에서 두 leaf 경우 $d=s$ 에서 old subtree 합이 $1-(L-1-s)\delta=m_{s+1}$ 임을 직접 확인했다. 일반 old tree에서의 증명은 못 봤고(블랙박스 `tree:reference-total`), 글의 진술을 받아들인 것이다.
- 모양 $S$ = anchor와 새 replica 하나가 깊이 $d$ 에서 갈라짐: branching vertex 하나($d_v=d$), 자식 $a_v=2$ 개로 읽으면
 $\kappa(S)=m_d-m_{d+1}$. 격자 $m_d=d/L$ 에서 $\kappa(S)=-1/L=-\delta$ (모든 $d$ 에서 같은 값). Q3의 모양별 직접 합 $-\delta$ 와 일치.

**(b)** L2 §6.2 "P6′ (모양별 총합)"; glossary g:tree-coefficient, g:reference-path; rules.md P6′ 행("telescoping으로 $m_{d+1}$").
**(c)** $\kappa$ 의 정의와 "old tree 무관" 진술: 글에 적혀 있음. telescoping의 이유: 글에 적혀 있음(한 줄)이나 증명은 없음(블랙박스). $a_v$ 가 "$S$ 에서 $v$ 의 자식 수"라는 것: **글에서 추론함**(L2에 $a_v$ 정의 없음; 이 해석이 Q3 직접 계산과 맞는 것으로 확인). $\kappa=-\delta$ 값: 산수.

---

## 6. P7

**(a)**
$$\sum_{E}c_E\,\mathbb E[fR_E]-\mathbb Ef\sum_{E'}c_{E'}\,\mathbb E[R_{E'}]\longrightarrow0 .$$
- $f$: old tree $\mathcal T$ 의 old replica multioverlap에 대한 **유계 다항식**(시험함수).
- $R_E$: 새 replica들(spin anchor이면 anchor 포함)의 multioverlap.
- $c_E$: P6′ 의 extension 계수($+1$ 과 $\gamma_\beta$ 의 곱).
- 첫 합: old tree $\mathcal T$ 에서 split 깊이 제약 $\mathcal C$ 를 지키는 history에 대한 합. 둘째 합: **anchor 하나만으로 된 tree**에서 같은 제약을 지키는 history에 대한 합($E'$ 으로 쓴 지표).
- 말로: anchor에 새 섭동 하나를 더한 효과(부호 있는 계수 합 형태)가 old tree의 시험함수 $f$ 와 분리된다($f$ 와 곱하고 평균한 것이 $f$ 의 평균과 새 replica 쪽 평균의 곱으로 대체된다).
- 극한: 선택된 수열(P5)을 따라 $N\to\infty$ 에서만, 고정한 $L$, old tree, 제약마다. 속도 없음, $L$ 에 대한 균일성 주장 없음. 항등식은 $f$, $\mathcal T$, anchor 종류, 새 replica 수, 제약 $\mathcal C$ 마다 성립.
- 제약 $\mathcal C$ 로 지정 가능한 것: anchor와 새 replica들로 이루어진 집합 안의 쌍별 split 깊이(새 replica끼리 포함), mark 깊이 $1..L-1$ 만. 다른 old replica가 관여하는 쌍은 지정 못 함.

**(b)** L2 §6.3 "P7", "처방할 수 있는 것", "성립 범위", "어디서 오는가"; rules.md P7 행; glossary g:tree-identity, g:palm-identity.
**(c)** 식과 각 기호의 역할: 글에 적혀 있음. 말로 하면 "분리된다": 글에 적혀 있음(L2 한 문장). "첫 합의 $\mathbb E[fR_E]$ 의 기대값이 정확히 어떤 확률공간(tree $\mathcal T_E$ 표본 + root)에 대한 것인가": 글에서 추론함. $E'$ 의 정의: L2에 없고 rules.md에서 "anchor 하나만으로 된 tree의 history"라는 설명으로 추론함.

---

## 7. 흐름

**(a)** 
- 앞에서 받는 것:
 - 수 2: 유계·순열불변 상호작용, 보조 계층(깊이 $L$, $m_d=d/L$, mark 변수가 보조 변수, tilted kernel), 섭동 틀과 reservoir(P3, P4). (2.3), (2.4)는 쓰지 않음.
 - 수 3: 선택된 수열(P5): (ii) score 오차 $e_{\nu,N_j}\to0$ 가 P7로 직접 들어가고, (iii) tree 위 multioverlap 곱 기대값의 수렴이 Taylor 계수의 극한 존재를 준다.
 - 수 1은 직접 받지 않음(상한은 이 단계에서 안 쓰임).
 - tree 계산(P6, P6′)은 임의의 유한 kernel 열에 대한 정확한 항등식이라 입력 없이 설 수 있고 수 4 안에서 쓰인다.
- 수 5에 넘기는 것: P7 항등식과 tree 표본 규칙(이 둘이 수 5가 모형에서 받는 입력의 전부), 그리고 수 5가 따로 더하는 P6′ 의 유한 tree 조합($\kappa$, 계수 한계). 수 5는 이것으로 깊이 미루기, $J=\kappa(S^+)^2$ 로 나눈 항등식, 세 사본 부등식을 거쳐 $v_N$ 과 $\mathrm{Var}(R_S)$ 의 깊이 평균 집중을 얻는다. marker anchor를 쓴 P7의 두 번째 항등식이 $\mathrm{Var}(M)\to0$ 을 준다.
- 수 5–6은 상호작용의 구체적 꼴과 무관. 계층 구조나 overlap 극한값은 이 항등식에서 안 나온다.

**(b)** L2 §6.4; §5(P5 (i)–(iii)); §6.3 "어디서 오는가"; §7.2 "증명의 모양", §7.3 "합치는 방식"; L1 수 4–5.
**(c)** 글에 적혀 있음. (iii)이 "Taylor 계수의 극한 존재"를 주는 것은 L2 §6.3에 한 구절로 적혀 있음. 수 1의 출력이 수 4와 무관하다는 말은 내가 정리한 것(글에서 추론함).

---

## 8. 계수 한계

**(a)** 
- $\delta^b$ 크기로 **작은** 것: (1) 처방한 branching vertex 중 old tree의 어느 branching 깊이와도 겹치지 않는 $b$ 개에 대한 **계수 절댓값 합**이 $\le C_{q,k}\delta^b$. (2) 그 $b$ 개 vertex의 $J=\prod_v\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$ 자체: vertex마다 $j=1$ 인자가 $-\delta$ 라서 $|J|\sim\delta^b$ 이고 $L$ 에 균일한 양의 하한이 없다.
- $L$ 에 **균일하게 유계**인 것: (1) 상수 $C_{q,k}$ (old leaf 수 $q$ 와 새 replica 수 $k$ 에만 의존, $L$ 과 지정 깊이와 무관). (2) 상대 비율 $\frac1{|J|}\sum|c_E|\le C_{q,k,\eta}$ — 모든 $v$ 에서 $m_{d_v}\ge\eta>0$ 이면. "균일한 것은 이 비율뿐이다"(원문 표현).
- 한계는 격자 $m_d=d/L$ 에서만 진술됨.
- 쓰임: 부호 있는 합은 상쇄돼 작아질 수 있지만 오차를 재는 것은 절댓값 합이므로 필요(예: 미루기 전 $-\delta$ 대 $2+\delta$, 미룬 뒤 절댓값 합 $\delta$).

**(b)** L2 §6.2 "P6′ (계수 한계)"와 "왜 이것이 필요한가"; rules.md P6′ 행("하한 $\delta^b\eta^{\sum_v(a_v-2)}$"); glossary g:depth-delay.
**(c)** 글에 적혀 있음. 단, "$C_{q,k}$ 는 $L$ 에 무관"과 "균일한 것은 이 비율뿐"이 한 단락에서 겹쳐 읽혀서 다시 읽었다(Q9 참조): 나는 둘 다 $L$ 에 균일한 것으로(절댓값 합의 상수 $C_{q,k}$, 그리고 비율의 상수) 읽었고, "비율뿐"은 "$|J|$ 자체는 균일하지 않다"를 강조하는 문장으로 해석했다. 이 해석은 글에서 추론함.

---

## 9. 막힌 곳 (구체적으로)

1. **§6.2 "P6′ (전개)" 첫 문단과 단락들에 식이 없다.** "anchor의 삽입 인자를 상쇄한 tree 기대값을 섭동 크기 $t_1..t_k$ 로 한 번씩 미분해 $\boldsymbol t=0$ 에서 본다"가 말뿐이라 좌변이 정확히 무엇인지 L2만으로는 쓸 수 없었다. 식은 rules.md의 P6′ 행(긴 "정확한 꼴" 문장)에서 찾았다. 거기서도 $E^{A_{\boldsymbol t}}_{\mathcal T}$, $H$, $a_j(E)$, $\mathcal T_E$ 는 L2에서 정의 없이 쓰이거나 아예 나오지 않는다. $E^A_{\mathcal T}$ 가 무엇의 기대값인지는 g:insertion의 $K^A_d$ 에서 추측해야 했다.
2. **$c_E$ 계수의 $n_\beta$.** 같은 절 "한 걸음에서 새 replica는 … 내부 vertex $\beta$ 에서 새로 갈라진다(계수 $\gamma_\beta<0$)"에서 $n_\beta$ 가 "현재 tree의 자식 수(안 쓴 old path와 이미 붙인 path 포함)"인지 L2에 안 쓰여 있다. P6(§6.1)의 "$n_\beta$ 는 자식 수"만 있어서, old tree의 자식인지, 새로 붙은 것만 세는지 모호했다. rules.md에서야 확인.
3. **"내부 vertex"의 범위.** 자식 하나뿐인 vertex가 들어가는가, 깊이 $L$ 은 빠지는가. L2 어디에도 없다. Q3의 계산이 이 선택에 따라 달라지므로, 나는 §6.2 마지막 문단의 "$-\delta$ 대 $2+\delta$"가 재현되도록 맞췄다(글에서 추론함).
4. **"아직 쓰지 않은 old replica를 다시 쓰거나(계수 $+1$)".** "다시 쓰다"가 무엇을 뜻하는지(새 color를 그 old leaf에 배정하는 것) L2 본문에 없고, "color"라는 말도 §6.2에 안 나온다(glossary g:extension-history에서만). "새 replica"와 "old replica를 쓴다"가 같은 선택의 두 모양이라는 것을 이해하는 데 시간이 걸렸다.
5. **$\kappa(S)$ 식의 기호.** $\mathrm{Br}(S)$, $a_v$, $d_v$ 가 L2에 정의 없이 나온다(§7.1에서 topology는 나오지만 $a_v$ 는 안 나온다). "처방"과 "reference path"의 뜻도 §6.2 안에서는 한 줄뿐. 나는 $a_v$ = $v$ 의 자식 수로 읽었다.
6. **"reference가 없는 old 부분 tree의 계수 합이 $m_{d+1}$ 로 telescoping"** 한 문장이 "old tree와 무관"의 유일한 근거인데, 어떤 합인지(어느 vertex의 어느 부분 tree) 읽어서는 알 수 없었다. Q3의 2-leaf 예를 직접 풀어서야($1-(L-1-s)\delta=m_{s+1}$) 이해했다. 이 예는 L2에 없다.
7. **§6.2 마지막 문단("왜 이것이 필요한가")의 예**가 설정(두 old leaf, anchor가 그중 하나, 처방이 old split 깊이와 같음)을 말하지 않고 결과($-\delta$, $2+\delta$)만 쓴다. 설정은 glossary g:depth-delay에 있다.
8. **기호 충돌.** $b$: (2.3)의 계수 $b$, 계수 한계의 vertex 개수 $b$, §7.2의 "$S$ 의 branching vertex 수 $b$"(이 둘은 정의가 다르다: 겹치지 않는 처방 vertex 수 대 $S$ 의 전체 branching vertex 수). $H$: Hamiltonian $H_N$, 장의 상계 $H$, §6.2의 유계 함수 $H$, §6.3 Palm 차이의 $H_N(t,u)$ (L2 §6.3에는 $H_N$ 이 나오지만 정의는 glossary에만). $D$: P6의 유계 path 함수 $D$ 와 §6.3의 score $D_\nu$ 가 같은 글자이고, 한쪽이 다른 쪽의 특수한 경우인지 설명이 없다. $E$: history $E$, 기대값 $E_{\mathcal T}$, $\mathbb E$, 지표 $E'$ 이 한 식에 같이 나온다. $d$: 깊이 $d$ 와 질문지의 $D=1$. $t$: L2가 세 가지 용도를 미리 경고한 것은 도움이 됐다. 그러나 P6′ 의 $t_1..t_k$ (삽입 크기)와 섭동 factor의 $t_\nu=1/j$ 의 연결은 §6.3 "어디서 오는가"에서 두 번 읽어야 했다.
9. **P7 식 안에서**: "anchor 종류"(spin anchor/marker anchor)가 §6.3 본문에서 정의 없이 쓰이고($R_E$ 에 anchor가 들어가는지는 "spin anchor이면"으로만), $\mathcal C$ 와 $\mathfrak E(\mathcal T,a_*,\mathcal C)$ 는 L2에는 기호가 없고 glossary에만 있다. 둘째 합의 지표 $E'$ 도 정의 없다.
10. **"어디서 오는가" 단락(§6.3)** 이 한 문단에 Palm 항등식, $u_\nu$ 가 $t_\nu$ 의 모든 고정 거듭제곱보다 작다는 선택, Taylor 계수 0으로 감, P5(iii), polarization, mark selector를 다 담고 있다. 각 단계의 연결을 따라가지 못해서 세 번 읽었고 끝내 "$D_j$ 의 곱이 어떻게 $R_E$ 가 되는가"와 "왜 anchor 한 leaf의 인자만 상쇄인가"는 찾지 못했다.
11. **§6.2 "계수 한계" 단락의 두 문장.** "계수 절댓값 합은 $C_{q,k}\delta^b$ 이하다. $C_{q,k}$ 는 … $L$ 과 지정 깊이에 무관하다"와 바로 뒤의 "$|J|$ 자체는 … 균일한 양의 하한이 없다. 균일한 것은 이 비율뿐이다"가 충돌하는 듯 읽힌다("균일한 것은 이 비율뿐"이면 $C_{q,k}$ 의 균일성은?). 또 "$b$ 개의 깊이가 old tree의 어느 branching 깊이와도 겹치지 않으면"의 "겹치지 않는다"가 old tree의 branching 깊이 집합과의 비교인지, 처방 vertex들끼리인지 모호했다.
12. **혼합 미분과 factorial.** §6.2에서 "추가 factorial이 붙지 않는다"는 문장이 있는데 $D_j=D$ 일 때 $t^k$ 계수가 우변$/k!$ 이라는 사실은 L2에 없고 rules.md에만 있다. 처음에는 두 말이 충돌하는 것으로 읽었다.
13. **Q3 "P6′ 좌변의 값"**: L2에는 좌변을 직접 계산하는 예가 없다. 상수 $D=1$ 에서 kernel이 불변이라는 사실(g:insertion의 $K^A_d$ 와 g:power-mean의 동차성)을 내가 조합해서 $-1$ 을 얻었다. 글은 그 계산을 제공하지 않는다.
14. **"정의 없이 나온 기호" 목록(§6 안)**: $E^{A}_{\mathcal T}$, $H$(§6.2 용도), $a_j(E)$, $\mathcal T_E$, $\mathrm{Br}(S)$, $a_v$, $d_v$, $q$($C_{q,k}$ 의 old leaf 수), $E'$, anchor 종류, $\mathcal C$(기호), $\mathfrak E$, "color", "reference path"(본문은 링크만), "mark selector", "polarization", $J_{N,\mathcal T}$.
