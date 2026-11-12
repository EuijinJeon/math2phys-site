# 검토 2 — §2 model 노드 카드 (독립 검토)

대상: `cards/` 의 `model.*.md` 13장, `x.model-*.md` 6장, `main.theorem*.md` 5장, 모두 24장.
기준: `source/sections/model.tex` 전체, `reduction.tex` 1–87, 그리고 카드가 인용하는 `upper.tex`, `consequences.tex`, `cavity.tex` 1–75, `comparison.tex` 66–76·174–246, `trees.tex` 1–27, `introduction.tex` 70–85, `overview.tex`.
"확인"은 원문과 직접 대조하거나 손으로 다시 계산했다는 뜻이다.

주의: 검토 중에 `layers/glossary.md` 가 다른 작업으로 바뀌고 있었다(21:04 무렵 `g:state`, `g:rsb-steps` 의 문구가 달라짐). 용어집 인용은 그 시점 기준이다.

## 요약

- 읽은 카드: 24 / 24 (머리말과 본문 모두).
- `math` 칸의 식 전사: (2.1)–(2.13), $q_x$, $\widehat\theta$, $D_K$, $d_K$, 두 안정성 상수, 상수 이동을 원문과 한 줄씩 대조했다. 부호·첨자·양화사·범위가 어긋나는 곳은 **찾지 못했다**. 표기 차이 하나(F9)만 있다.
- 작성자가 밝히고 보탠 것 12건은 모두 다시 계산해 **옳았다**(아래 "보탠 것의 확인").
- `main:theorem` 의 분해 s1–s4는 reduction.tex 45–87을 빠짐없이, 순서대로 덮는다. 구멍 없음.
- `model:section` 의 "밖에서 쓰는 곳" 표는 원문의 `\ref` 22건과 전부 일치한다.
- 통과 11장, 지적이 붙은 카드 13장. 지적 15건:

| 유형 | 건수 | 번호 |
|---|---|---|
| 틀림 | 0 | — |
| 과장 | 3 | F1, F2, F4 |
| 구멍 | 0 | — |
| 누수 | 5 | F3, F7, F8, F11, F14 |
| 유형·ID | 2 | F6, F12 |
| 용어 | 1 | F10 |
| 표기 | 4 | F5, F9, F13, F15 |

| 심각도 | 건수 | 번호 |
|---|---|---|
| 높음 | 0 | — |
| 중간 | 4 | F1, F2, F3, F4 |
| 낮음 | 11 | F5–F15 |

## 지적 (심각도 순)

### F1. 과장 (유형 값) — `main:theorem` — 중간
- 카드 `physics`: "Poisson hypergraph 위의 짝수 $p$체 Ising spin glass에서 quenched pressure $F_N$ 의 열역학 극한이 존재하고, 모든 유한 RSB 단계 수의 Mézard–Parisi free entropy 시행값의 inf와 같다." `abstraction: exact`.
- 원문: model.tex 130–132 "Under \eqref{model:integrability}--\eqref{model:positivity}, the thermodynamic limit exists and …". 물리 문장에는 factorization (2.3)과 부호 조건 (2.4)이 없다. 문자 그대로 읽으면 모든 짝수 $p$체 희석 모형에 대한 주장이고, 이것은 증명된 것보다 많다. 차이 칸 (3)에 "가정은 (2.1)–(2.4)"라고 적혀 있기는 하다.
- 근거: HANDOFF 원칙 1("물리 진술이 증명된 것보다 많이 말하면 차이 칸에 적고 유형을 `approximation` 으로"). 거의 같은 문장을 쓴 `model:section` 은 `approximation` 으로 되어 있어 두 카드가 서로 어긋난다.
- 수정: `abstraction: approximation` 으로 바꾸거나, 물리 문장에 "가정([[g:hypotheses]]) 아래"를 넣고 `exact` 를 유지한다. 뒤쪽이 낫다(주정리 카드이므로).

### F2. 과장 — `model:section` (`gap` (2)) — 중간
- 카드: "가정에 tanh형 전개와 부호 조건이 들어가고, 이것은 상한에만 실제로 쓰인다(P1)."
- 원문: reduction.tex 54–58 "The factorization gives … The multiplier $a$ has disappeared. Independence and identical distribution of the $f_\ell$, and their independence of $b$, show that the law of $\widehat\theta$ is invariant under permutations of its inputs." factorization은 하한 쪽에서도 한 번 쓰인다. 순열 불변성이 없으면 `comp:bounded-lower` 를 적용할 수 없으므로 빠질 수 없는 사용이다. "상한에만"은 부호 조건에만 맞다(upper.tex 125, cavity.tex 13–14).
- 인용한 P1 자신이 "하한 쪽에서 factorization은 한 번만 쓰인다"고 적고 있고, 같은 묶음의 `x:model-hypotheses`·`model:factorization`·`main:theorem.s4` 의 차이 칸도 그렇게 적는다. 이 카드만 어긋난다.
- 수정: "부호 조건은 상한에만 쓰이고, 전개는 상한과 주정리 증명의 상수 이동(main:theorem.s1)에 쓰인다(P1)."

### F3. 누수 (방향이 뒤집힌 `provides`) — `x:model-hypothesis-remarks`, `main:theorem.s1` — 중간
- 카드: `uses: [model:factorization, model:positivity, upper:bound]` 이면서 `provides: 'upper:bound 증명 첫 단락(upper.tex 17–34: 퇴화 경우 처리와 $b$, $M$ 의 본질적 유계성), …'`.
- 원문: model.tex 39–41 "independence and the strict product bound force $b$ and $\max_s|f_1(s)|$ to be essentially bounded, as shown in \cref{upper:bound}". 방향은 한쪽뿐이다. upper.tex 17–34는 이 주석을 받아 쓰지 않고 스스로 증명한다("Otherwise choose $u,v>0$ … Indeed, violating either bound …"). 주석 (i)가 upper:bound의 증명에 기대는 것이지 그 반대가 아니다.
- 위험: §4 카드를 쓰는 사람이 이 `provides` 를 따라 `upper:bound`(또는 그 첫 단계)의 `uses` 에 이 카드를 넣으면 순환이 생긴다.
- 딸린 문제: `main:theorem.s1` 이 이 카드를 `uses` 에 넣어서, 하한 쪽 단계가 `upper:bound` 에 전이적으로 기대는 모양이 된다. s1이 실제로 쓰는 것은 "$a$ 가 입력에 비대칭으로 의존할 수 있다"뿐이고 그것은 s1의 원문 범위(reduction.tex 46–47)에 직접 적혀 있다.
- 수정: `provides` 의 첫 항목을 "upper:bound 증명 첫 단락이 (i)를 증명한다(이 카드가 받는 쪽)"로 고친다. `main:theorem.s1` 의 `uses` 에서 이 카드를 빼고 본문의 `[[x:model-hypothesis-remarks]]` 언급으로 남긴다.

### F4. 과장 — `x:model-hypothesis-remarks` (`physics`) — 중간
- 카드: "엄격한 곱 한계가 사실상 $\lvert\tanh\rvert<1$ 의 균일한 형태라서 모든 moment가 유한하다." `abstraction: exact`.
- 원문: model.tex 39–41 "This is automatic in the nondegenerate case: independence and the strict product bound force …". 조건이 둘 빠졌다.
  1. 비퇴화 조건. 퇴화 경우($M=0$ a.s., upper.tex 19)에는 곱 한계가 $b$ 를 전혀 제약하지 않아 $b$ 의 moment가 유한할 이유가 없다. 원문이 "interpreted as finite real expectations"(38–39)와 "one may take $b=0$"(42–43)을 따로 적는 까닭이다.
  2. 독립성. 유계성은 곱 한계만이 아니라 $b$ 와 $f_\ell$ 들의 독립에서 나온다(upper.tex 26 "independence gives").
  또 얻는 한계는 $\lVert b\rVert_\infty\le u^{-p}$, $\lVert M\rVert_\infty\le(vu^{p-1})^{-1}$ (upper.tex 28–29)이고 1보다 클 수 있다. "$\lvert\tanh\rvert<1$ 의 균일한 형태"는 Viana–Bray($f(s)=s$)에서만 맞는 그림이다.
- `math` (i)는 조건을 정확히 달고 있다. 물리 문장만 넘친다. 차이 칸에 이 초과분이 없다.
- 수정: "비퇴화 경우에는 $b$ 와 $f$ 의 독립과 엄격한 곱 한계가 둘을 본질적으로 유계로 만들어 (2.4)의 moment가 유한하다. 퇴화 경우에는 $b=0$ 으로 잡는다."

### F5. 표기 (원문에 없는 말을 원문 것으로 돌림) — `x:model-message` — 낮음
- 카드 `math`: "edge 항은 그 삽입에서 (중복으로) 센 상호작용을 보정한다." `gap`: "\"중복으로 센 상호작용을 보정한다\"는 원문의 설명 문장(model.tex 50–52)이고".
- 원문: model.tex 51–52 "the edge term corrects for interactions counted in that insertion". "중복으로"에 해당하는 말이 없다. `math` 에서는 괄호로 표시했지만 `gap` 은 따옴표 안에 넣어 원문 문장이라고 했다.
- 수정: `gap` 의 인용을 "그 삽입에서 센 상호작용을 보정한다"로 고치고, "중복"은 작성자의 읽기라고 적는다(`model:functional` 의 차이 칸은 이미 그렇게 적고 있다).

### F6. 유형 — `x:model-depth-zero` — 낮음 (확신 낮음)
- 카드: `kind: convention`.
- SCHEMA: `convention` 은 "섹션 범위의 약속(예: 이 섹션 내내 $m_d=d/L$)"이다. 이 카드는 대상 $\mathcal B_0(\zeta)$, $\Phi_0$ 을 정한다(model.tex 118–120 "this defines $\cB_0(\zeta)$ and $\Phi_0$"). `main:theorem` 의 $\inf_{r\ge0}$ 과 reduction.tex 19의 "including $r=0$"이 받는 것은 약속이 아니라 이 대상이다.
- 수정: `kind: definition`. ID는 식 라벨이 없으므로 `x:model-depth-zero` 그대로 맞다.

### F7. 누수 (쓰지 않는 `uses`) — `model:functional`, `main:theorem.s1` — 낮음
- `model:functional` `uses: [model:power-means, model:vs, model:ve, model:hamiltonian]`. (2.11)이 `model:hamiltonian` 에서 받는 것은 없다. $\alpha$, $p$ 는 `model:integrability`(model.tex 3)에서 온다.
- `main:theorem.s1` `uses: […, model:hamiltonian, …]`. s1의 내용($c$, $\widehat\theta$, $\lvert c\rvert\le B(\theta)$, 순열 불변성, reduction.tex 45–59)은 $H_N$, $Z_N$, $F_N$ 을 쓰지 않는다.
- 수정: 두 곳에서 `model:hamiltonian` 을 빼고 `model:functional` 에는 `model:integrability` 를 넣는다.

### F8. 누수 (전제의 출처가 `math` 에 없음) — `main:theorem.s3` — 낮음
- 카드: "균일한 시행 안정성(reduction:stability의 시행 functional 부등식)이 … 를 준다."
- 원문: reduction.tex 10–11 "Couple two interaction laws … each satisfying \eqref{model:integrability}", 20 "If $c$ is an integrable random constant". 이 보조정리를 $\widehat\theta$ 와 $\widehat\theta^{(K)}$ 에 쓰려면 $\mathbb EB(\widehat\theta)<\infty$ 와 $c$ 의 적분 가능성이 필요하고, 둘 다 s1에서 온다(reduction.tex 50, 59). s3의 `uses` 에 s1이 있기는 하지만 `math` 는 이 전제를 말하지 않고, s1의 `provides` 는 $\mathbb EB(\widehat\theta)<\infty$ 를 s2에만 준다고 적는다.
- 수정: s3 `math` 에 "$\widehat\theta$ 와 $\widehat\theta^{(K)}$ 는 (2.1)을 만족하고(main:theorem.s1) $c$ 는 적분 가능하므로 reduction:stability가 적용된다" 한 구절을 넣고, s1 `provides` 에 s3를 더한다.

### F9. 표기 — `model:power-means` — 낮음
- 카드: "깊이 1($r=1$)에서 $T_0V=(\mathbb E_{\boldsymbol x}[V^{m_1}\mid\boldsymbol\eta_0])^{1/m_1}$."
- 원문: model.tex 99 `$T_0V=(\E_x[V^{m_1}\mid\boldsymbol\eta_0])^{1/m_1}$`. 원문은 $\mathbb E_x$ 가 굵지 않다. 109행 "bold symbols collect all message labels in $V$"와 깊이 2 식의 $\mathbb E_{\boldsymbol x}$ 에 비추면 카드 쪽이 일관되지만, 밝히지 않고 바꿨다. "($r=1$)", "($r=2$)"라는 풀이는 옳다.
- 수정: 원문대로 $\mathbb E_x$ 로 두거나, 본문에 "원문은 $\mathbb E_x$; 깊이 2 식에 맞춰 굵게 썼다"를 적는다.

### F10. 용어 — `model:power-means` 외 — 낮음 (규율을 얼마나 엄격히 읽느냐에 달림)
- `model:power-means` `physics`: "1RSB cavity 계산의 $Z^m$ 재가중(Monasson) 꼴을 계층마다 쓴 것으로 읽을 수 있다."
- 논문은 이 동일시를 증명하지도 쓰지도 않는다(카드 차이 칸도 "그림"이라고 적고 유형은 `intuition`). 용어 규율 3의 금지 목록(Ruelle cascade, GG, stochastic stability, ultrametricity)에는 없는 이름이지만 HANDOFF 원칙 2의 취지에 걸리고, 용어집은 Monasson 읽기를 다른 항목의 "물리 대응" 칸에 intuition으로만 두고 있다. `g:power-mean` 의 물리 대응 칸에는 이 읽기가 없다.
- 규율 1(`physics`·`gap` 의 전문 용어는 용어집 항목이 있어야 한다)로 보면 항목이 없는 말이 더 있다: "정류점(saddle point)"(`model:section`, `model:functional`, `main:theorem`, `x:model-depth-zero`), "full RSB"(`model:section`, `x:model-theorem-scope`), "replica symmetric(RS)"(`x:model-depth-zero`), "$u$-message"(`model:site-message`), "population of populations"(`model:chain`). 뒤의 둘은 용어집 물리 대응 칸에 같은 말이 나온다.
- 수정: Monasson 문장을 `g:power-mean` 의 물리 대응 칸으로 옮기고 카드에서는 "[[g:power-mean]]의 물리 대응 칸"을 가리킨다. 나머지는 조율 세션이 용어집 항목을 둘지 정한다.
- 확인한 것: 금지된 네 이름은 24장 어디에도 `physics` 에 없다. "cascade"는 `model:section` 차이 칸에 "쓰이지 않는다"는 부정으로 한 번 나온다.

### F11. 누수 (`provides` 과장) — `x:model-cavity-bounds` — 낮음
- 카드 `provides`: "… reduction:stability(각 cavity 상호작용과 edge 로그가 sup-norm 차이만큼만 변함)".
- 원문: reduction.tex 33–34 "Each cavity interaction changes by at most the corresponding sup-norm interaction difference, and so does each edge logarithm." 이것은 차이에 대한 Lipschitz 한계이고, 이 카드의 진술 $\lvert\log C_\theta\rvert,\lvert U_\theta\rvert\le B(\theta)$ 에서 따라 나오지 않는다. 같은 논법(확률 가중 평균)을 다시 쓰는 것일 뿐이다.
- 수정: "reduction:stability는 같은 평균 논법을 차이에 다시 쓴다(이 진술을 받는 것은 아님)"로 고친다.

### F12. 유형·ID (원문 범위의 선택) — `x:model-hypotheses` — 낮음
- 카드: `source: model.tex [130, 131]`, 본문 "원문 범위를 main:theorem의 줄 130–131로 잡은 것은 … 의존 검사가 대상 라벨의 위치로 허용 여부를 본다".
- `tools/check.py` 의 의존 검사를 읽어 확인했다. 대상 라벨의 위치가 `uses` 한 카드의 `source` 범위에 들면 통과하므로 작성자의 설명대로 동작한다. 순환을 피하려는 뜻도 타당하다.
- 다만 SCHEMA의 `source` 는 "진술의 원문 범위"다. 가정의 진술은 model.tex 3–8, 25–38에 있고 130–131은 그것을 이름으로 부르는 줄이다. 범위가 검사기를 통과시키려고 정해졌고 `main:theorem` 의 범위와 겹친다.
- 수정: `source` 에 3–8, 25–38을 더하고 130–131을 함께 둔다. 검사는 그대로 통과한다. 조율 세션이 이 관행을 SCHEMA에 한 줄 적어 두면 §4 작성자가 따라 할 수 있다.

### F13. 표기 — `model:positivity` (`physics`) — 낮음
- 카드: "coupling의 tanh $b$ 에 대한 부호 조건이다."
- 원문: model.tex 32 "$a>0$ and $b$ are real random variables". $b$ 가 tanh인 것은 Viana–Bray 예뿐이다(consequences.tex 27). soft SAT에서는 $b=e^{-\beta W}-1$ 이다(consequences.tex 59). 같은 문장이 SAT를 예로 드는데 $b$ 를 tanh라고 부른다.
- 수정: "[[g:factorization|전개]]의 계수 $b$ 에 대한 부호 조건".
- 덧붙임: 유형이 카드에서는 `weakening`, 용어집 `g:positivity` 에서는 같은 문장에 `intuition` 이다. 두 예에서 성립한다는 문장은 증명된 사실이므로(consequences.tex 30–31, 61–62) `weakening` 이 맞다고 본다. 용어집 쪽을 맞춘다.

### F14. 누수 (원문 범위 밖의 진술) — `x:model-theorem-scope` — 낮음
- 카드 `physics`: "물리의 full-RSB 극한 order parameter나 물리적 pure state의 계층 구조는 결과에 들어 있지 않다." `source: model.tex [138, 140]`.
- 원문 138–140은 inf의 달성과 "a limiting infinite-depth Gibbs state"만 말한다. 물리적 pure state의 계층에 대한 문장은 introduction.tex 76–77 "no ultrametric organization of the physical Gibbs states is assumed"에 있다. 진술은 참이지만 이 카드의 범위에서 나오지 않는다.
- 수정: `source` 에 `introduction.tex [75, 77]` 을 더하거나 차이 칸에 그 줄을 적는다.
- 딸린 것: `provides` 의 "g:phi … 의 정의 위치"는 맞지 않는다. `g:phi` 의 정의 위치는 `model:functional`, `main:formula` 이고 model.tex 138–140은 물리 대응 칸에서만 인용된다. `g:physical-pure-state` 쪽은 맞다.

### F15. 표기 (줄 번호) — `model:section` (본문) — 낮음
- 카드: "cavity.tex 11–19는 $B(\theta)\le B$, $\lvert h\rvert\le H$ 와 같은 power-mean 재귀를 쓰고".
- 원문: cavity.tex 11–12가 유계 가정, 16–19는 격자 $m_d=d/L$, power-mean 재귀는 34행 "Apply the power-mean recursion to the resulting leaf partition function"이다.
- 수정: "cavity.tex 11–12(유계 가정), 34(같은 power-mean 재귀)".

## 보탠 것의 확인

작성자가 원문에 없다고 밝힌 것을 다시 계산했다. 모두 옳다.

| 카드 | 보탠 것 | 확인 |
|---|---|---|
| `model:hamiltonian` | $F_N$ 의 유한성 | $e^{-S}\le e^{-H_N(\sigma)}\le e^{S}$, $S=\sum_{k\le M_N}B(\theta_k)+\sum_i\lvert h_i\rvert$ 에서 $\lvert\log Z_N-N\log2\rvert\le S$. $M_N$ 이 $\theta_k$ 와 독립이라 $\mathbb ES=\alpha N\mathbb EB(\theta)+N\mathbb E\lvert h\rvert$. 맞다 |
| `model:hamiltonian` | "한 factor 안에서 같은 site가 반복될 수 있다" | 21–22행 "indices are sampled with replacement"의 귀결. 맞다 |
| `model:factorization` | 곱 한계가 $\lvert b\rvert\prod_\ell\max_s\lvert f_\ell(s)\rvert<1$ a.s. 와 같음 | spin 조가 $2^p$ 개뿐이라 각 $\ell$ 의 최대를 주는 조를 고르면 된다. upper.tex 26과 일치 |
| `x:model-message` | $x\mapsto q_x$ 가 완전히 양인 분포와 일대일 | $q_x(1)=1/(1+e^{-2x})$ 는 $\mathbb R\to(0,1)$ 전단사. 맞다 |
| `x:model-cavity-bounds` | $\lvert\log C_\theta\rvert,\lvert U_\theta\rvert\le B(\theta)$ 의 근거 | 합이 1인 가중치로 $e^{\theta(s)}\in[e^{-B},e^{B}]$ 를 평균. $U_\theta$ 는 $\varepsilon$ 을 고정하고 $p-1$ 개 좌표를 평균. 맞다 |
| `model:site-message` | 새 spin이 마지막 좌표, 순열 불변이면 좌표 무관 | 61행 $\theta(s_1,\ldots,s_{p-1},\varepsilon)$. 맞다 |
| `model:chain` | $\eta_d\in\mathcal M_{r-d}$ | $\zeta\in\mathcal M_{r+1}=\mathcal P(\mathcal M_r)$ 이므로 $\eta_0\in\mathcal M_r$, 귀납으로 $\eta_{r-1}\in\mathcal M_1=\mathcal P(\mathbb R)$, $x\in\mathbb R$. 맞다. trees.tex 26–27과도 일치 |
| `model:power-means` | 조건부 기대값이 잘 정의됨, $k$ 가 $\mathscr F_0$-가측 | $T_{d+1}V>0$. $k$ 는 물리적 disorder(82, 90행). 맞다 |
| `model:functional` | 바깥 $\mathbb E$ 가 disorder와 $\eta_0$ 을 평균 | $T_0V$ 가 $\mathscr F_0$-가측. 맞다 |
| `model:functional` | $\alpha(p-1)$ 의 "중복분" 읽기 | cavity.tex 67 $K_{\rm s}\sim\mathrm{Pois}(\alpha p)$, $K_{\rm b}\sim\mathrm{Pois}(\alpha(p-1))$, 47–48 $\rho_N=\alpha(N+1)(N/(N+1))^p\approx\alpha N-\alpha(p-1)$. $N+1$ 계는 reservoir에 site 삽입 $\alpha p$ 개, $N$ 계는 reservoir에 bond 삽입 $\alpha(p-1)$ 개이고 차이가 $\alpha$. 셈이 맞고, 카드가 작성자의 읽기라고 밝혔으며 유형이 `approximation` 이다 |
| `x:model-depth-zero` | $\mathcal B_0(\zeta)=\log2+\mathbb E\log V_{\rm s}-\alpha(p-1)\mathbb E\log V_{\rm e}$ | 118–120행 "the operators $T_d$ are omitted", upper.tex 43–44 "For $r=0$ all messages are quenched and there is no auxiliary recursion"과 일치. 맞다 |
| `model:trial-bounds` | (2.12)의 귀납, Wald 등식 | $c=\lvert h\rvert+\sum_{j\le k}B(\theta_j)$ 가 모든 $\mathscr F_d$ 에 가측이므로 $e^{-c}\le T_{d+1}V\le e^{c}$ 가 $T_dV$ 로 넘어간다. $k$ 가 $\theta_j$ 와 독립이라 $\mathbb E\sum_{j\le k}B(\theta_j)=\alpha p\,\mathbb EB(\theta)$. 맞다 |
| `main:theorem.s1` | $\lvert\widehat\theta\rvert\le2B(\theta)$, 순열 불변성의 근거 | $\lvert\theta(s)-c\rvert\le2B(\theta)$. $(b,f_1,\ldots,f_p)$ 의 법칙이 $f$ 들의 순열에 불변이고 $\widehat\theta$ 는 그것만의 함수. 맞다 |
| `main:theorem.s2` | 지배 함수 | $\max_s\lvert\widehat\theta-\widehat\theta^{(K)}\rvert\le B(\widehat\theta)$, $\lvert h-h^{(K)}\rvert\le\lvert h\rvert$, 둘 다 점별로 0에 간다. 맞다 |
| `main:theorem.s3` | 부등식 분할 | free-stability로 $\widehat F_N\ge F_N^{(K)}-\alpha D_K-d_K$, bounded-lower로 $\liminf F_N^{(K)}\ge I_K$, trial-stability로 $I_K\ge\widehat I-\alpha(2p-1)D_K-d_K$. 합이 $2\alpha pD_K+2d_K$. 상수가 $r,\zeta,\mathbf m$ 에 무관해 $\widehat\Phi_r=\Phi_r-\alpha\mathbb Ec$. 맞다 |

밝히지 않고 보탠 곳은 F5(따옴표 안의 "중복으로")와 F9(굵은 $\boldsymbol x$) 둘뿐이다.

## 분해 s1–s4와 reduction.tex 45–87

| 단계 | 범위 | 원문 내용 | 판정 |
|---|---|---|---|
| s1 | 45–59 | $a$ 의 비대칭, $c=\theta(1,\ldots,1)$, $\widehat\theta$ 의 식, 순열 불변성, $\mathbb EB(\widehat\theta)\le2\mathbb EB(\theta)$ | 빠짐 없음 |
| s2 | 60–69 | truncation, 불변성 보존, bounded-lower의 적용 가능성, $D_K,d_K\to0$ | 빠짐 없음 |
| s3 | 70–84 | $\widehat I$, $I_K$, 시행 안정성, pressure 안정성과 하한, $K\to\infty$, 상수 되돌리기 | 빠짐 없음 (F8은 전제 표기) |
| s4 | 85–87 | upper:bound, 두 극한의 일치 | 빠짐 없음 |

경계는 원문 문단과 맞고 순서와 논리가 바뀌지 않았다. 자식 네 진술에서 부모 진술이 나온다. `main:theorem` 본문이 적은 대로 이 단계 카드들은 reduction.tex에 속하므로 §9 카드를 쓸 때 겹치지 않게 해야 한다.

## `model:section` 인터페이스 표

원문 전체에서 `model:*`, `main:*` 를 가리키는 `\ref` 류를 grep으로 모아 표와 대조했다. model.tex 밖의 22건(upper.tex 12, 63, 125; reduction.tex 11, 45, 86; trees.tex 26; comparison.tex 72, 180, 227, 235; consequences.tex 8, 19, 33, 47, 63, 83, 112, 137; introduction.tex 32, 85; overview.tex 50)이 모두 표에 있고 설명이 그 줄의 내용과 맞다. reduction.tex 45는 증명의 머리 줄이라 표가 아니라 `main:theorem` 의 `source` 에 있다. model.tex 안에서 밖을 가리키는 참조는 41행 `upper:bound` 하나뿐이고 카드의 "받는 것"과 일치한다. "overview.tex가 §2의 소절"이라는 메모도 맞다(`\subsection{Proof strategy}`, main.tex 63–64).

## 통과 카드 (11장)

`model:integrability`, `model:hamiltonian`, `model:factorization`, `model:edge`, `model:site-message`, `model:chain`(❓ 는 아래), `model:vs`, `model:ve`, `model:trial-bounds`, `main:theorem.s2`, `main:theorem.s4`.

"상태"는 24장에서 `model:power-means` `physics` 에 한 번만 나오고 `[[g:state]]` 를 건 깊이 $d$ prefix의 뜻이다. `g:state` 의 정의 위치 칸이 "시행 사슬의 $\mathscr F_d$ 는 model.tex 90–91"을 포함하므로 규율에 맞다. 원문의 "Gibbs state"(140행)는 "Gibbs 측도"로 옮겼고 `x:model-theorem-scope` 차이 칸이 그 사실을 밝힌다. R번호 참조는 없다.

## ❓ `model:chain` 의 message label 집합

원문으로 정해진다고 본다. 작성자의 읽기(셀 수 있게 많은 label을 미리 준비)가 맞다.

- model.tex 80–81 "Use different labels for $x_1,\ldots,x_p$ and for $x_\ell^j$, $j\ge1$, $1\le\ell<p$." $j$ 의 범위가 $j\le k$ 가 아니라 $j\ge1$ 이다. label 집합은 $\{1,\ldots,p\}\sqcup\{(j,\ell):j\ge1,\ 1\le\ell<p\}$, 가산 무한이다.
- 82행 "Take independent $k\sim\Pois(\alpha p)$, $\theta,\theta_1,\ldots$" 도 $\theta_j$ 를 $k$ 와 독립인 무한열로 잡는다. label도 같은 방식이다.
- 71행 "For each message label $\omega$ independently"와 79–80행 "All these variables are independent of the physical disorder"에서, 사슬들은 label끼리 i.i.d.이고 $k$ 와 독립이다. 그래서 $V_{\rm s}$ 는 처음 $k$ 개 묶음만 쓰는 함수이고, 90–91행의 $\mathscr F_d$ ("all $\eta_j^\omega$")는 가산 개 변수가 생성하는 $\sigma$-field라 문제가 없다. 109행 "bold symbols collect all message labels in $V$"는 $k$ 가 주어졌을 때 실제로 쓰인 유한 개를 가리킨다.
- upper.tex 40 "Different cavity terms have disjoint message labels", comparison.tex 182 "edge factors with disjoint message labels"도 같은 약속을 쓴다.

$V_{\rm s}$ 의 label과 $V_{\rm e}$ 의 label이 서로 다른지도 80–81행이 정한다(다르다). (2.11)은 두 기대값을 따로 취하므로 결과에는 영향이 없다. 수정 제안: ❓ 를 지우고 "label 집합은 $\{1,\ldots,p\}\sqcup\{(j,\ell):j\ge1,1\le\ell<p\}$ (model.tex 80–82)"로 적는다.

## 작성자가 본 기존 문서의 어긋남 세 가지

**(a) `g:positivity` 의 "soft SAT($b<0$)".** 작성자가 옳다. consequences.tex 40 "$W\ge0$", 59 "$b=e^{-\beta W}-1$", 61 "Since $0\le-b<1$". $W=0$ 이 양의 확률로 허용되므로 $-1<b\le0$ 이다. $b<0$ 은 $W=1$ (단위 가중 SAT)에서만 맞다. 용어집을 "$-1<b\le0$"으로 고친다. 카드 `model:positivity` 는 이미 그렇게 쓴다.

**(b) `g:site-term` 에 "새 spin이 $\theta$ 의 마지막 좌표".** 빠져 있다. 틀린 것은 아니고 누락이다. model.tex 61 `e^{\theta(s_1,\ldots,s_{p-1},\eps)}` 가 자리를 정하고, 용어집의 기호·뜻 칸에는 이 정보가 없다. 사소하지 않다: 주정리의 $\theta$ 는 순열 불변이 아닐 수 있고(reduction.tex 46–47) 상한은 원래 $\theta$ 에 그대로 쓰이므로(upper.tex 39, 64–66) $\mathcal B_r$ 의 정의가 좌표 선택에 달려 있다. 뜻 칸에 "새 spin은 $\theta$ 의 $p$ 번째 좌표에 놓인다(model.tex 61)"를 더한다.

**(c) `g:rsb-steps` 정의 위치에 model.tex 70.** 빠져 있다. $r$ 이 처음 나오는 곳은 model.tex 70 "Fix $r\ge1$"이고 $r=0$ 은 118–120이다. 지금 정의 위치는 `trees.tex` 24–27, `cavity.tex` 16–19뿐이다($L=r+1$ 쪽만). 검토 시점에 물리 대응 칸은 이미 `model.tex` 70–81을 인용하도록 바뀌어 있었으나 정의 위치 칸은 그대로다. `model:chain`, `x:model-depth-zero`(또는 `model.tex` 70–71, 118–120)를 더한다.

## 새 용어 `g:disorder` 제안에 대한 의견

뜻·역할·정의 위치가 원문과 맞는다. "physical disorder"는 원문이 정의 없이 쓰는 말이고(model.tex 80, 90, 109; upper.tex 9; comparison.tex 82, 182–183) 제안된 뜻이 그 용례와 일치한다. 세 가지를 손보면 좋다.

1. 뜻 칸의 "바깥의 $\mathbb E$ 가 이것을 평균한다"는 덜 말한다. 바깥 $\mathbb E$ 는 $\eta_0$ 도 평균한다($T_0V$ 는 $\mathscr F_0$-가측, model.tex 90–91). `model:functional` 카드는 그렇게 적는다. "disorder와 $\eta_0$ 을 평균한다"로 맞춘다.
2. 역할 칸의 "선택된 매개변수가 root에 더해진다"는 cavity.tex 29–30 "The parameters of the factors … are fixed, not quenched random variables"와 맞지 않게 읽힐 수 있다. 매개변수는 고정값이지 root의 무작위 변수가 아니다. 검토 시점의 `g:state` 는 "섭동 매개변수는 선택된 값으로 고정"으로 바뀌어 있었으므로 그 표현을 따른다.
3. reservoir의 섭동 개수·type·site가 "disorder"인지 "root 변수"인지 원문은 가르지 않는다(cavity.tex 29 "root variables", 56 "new root disorder"). 제안은 "root에 더해진다"고만 써서 단정하지 않으므로 그대로 둬도 된다.

정의 위치의 `model:hamiltonian` 은 모형 쪽만 덮는다. 시행 functional 쪽($k$, $\theta,\theta_1,\ldots$, $h$, 82행)을 위해 `model:vs` 를 더한다.
