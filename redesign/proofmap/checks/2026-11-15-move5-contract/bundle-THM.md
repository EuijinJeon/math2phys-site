# 입력 묶음: top.THM 를 연다

## 0. 할 일과 규칙

수학 논문 한 절의 증명 지도(proof map)를 짓는 중이다. 맨 위 graph의 node 하나를 **연다**: 그 node의 증명 블록을 한 층 아래의 하위 graph로 옮긴다. 이 묶음에 있는 것만 쓴다. 다른 파일, 다른 원문, 기억하는 문헌을 쓰지 않는다. 묶음에 없는 것이 필요하면 지어내지 말고 아래 `missed_dependencies` 나 `parent_change_requests` 에 적는다.

- 하위 graph의 안쪽 node는 원문 증명의 걸음이다. 원문 순서와 문단 경계를 따르고 9개 안팎으로 둔다. 물리 해석의 이름을 붙이지 않는다.
- 모든 진술은 5절의 원문 줄과 대조해 옮긴다. 각 node·edge에 줄 범위(`grounding.source`, 예 `"decorrelation.tex 287–290"`)를 단다.
- 원문이 적지 않은 걸음을 채웠으면 그 node 또는 유도 줄에 `author_filled` 로 무엇을 채웠는지 적는다.
- 안쪽 node의 `status` 는 기본 `sketch`. `complete` 는 그 node가 다른 정리를 부르지 않는 한 걸음이고 `derivation` 의 모든 줄의 근거(`by`)가 받는 edge id, 앞선 줄, 바닥(Cauchy–Schwarz 같은 기초 사실, `floor_used` 에 적음) 가운데 있을 때만 쓴다. 망설여지면 `sketch`.
- `grounding.state` 는 언제나 `"proposed"`.
- 상위 graph의 받는 edge(2절)마다 하위 graph에 `external` node 하나를 둔다: `external_ref` = 그 edge의 `from`, `import_edge` = 그 edge의 `id`, `items` = 하위에서 실제로 쓰는 그 edge의 carries 항목 이름. 2절의 모든 `from` 이 빠짐없이 external로 있어야 한다(쓰지 않으면 그렇다고 `note` 에 적는다).
- 1절 계약의 출력 항목마다 `output` node 하나 또는 하나의 `output` node가 여러 항목을 맡게 하고, `output_items` 에 항목 이름을 적는다. 3절의 보내는 edge가 싣는 항목이 모두 어느 output에서 나와야 한다.
- edge는 `{id, from, to, kind: flow|call|definition, statement, carries: [{item, used_at: [줄]}], grounding, status: "connected", complete: true|false}`. `statement` 에 싣는 내용을 다 적었으면 `complete: true`.
- 기호는 4절 기호 표의 id로 참조한다(`symbols`). 증명 안에서만 쓰는 새 기호는 node의 `local_symbols: [{id, tex, defined_at, text}]` 에 적는다. 기호 표에 있어야 할 것(밖에서도 쓰는 것)이 빠졌으면 `parent_change_requests` 에.

## 0.1 산출 (JSON 하나)

```json
{
  "graph": {"id": "<NODE 소문자>", "title": "...", "parent": {"graph": "top", "node": "<NODE>"},
            "summary": "...", "nodes": [...], "edges": [...]},
  "parent_change_requests": [
    {"target": "edge t5 | node AVG | symbol mu | new edge X→NODE | new symbol",
     "kind": "add_item | change_item | new_edge | new_symbol | change_symbol | other",
     "detail": "무엇을 어떻게", "reason": "왜 필요한가", "source_lines": "decorrelation.tex 287"}
  ],
  "missed_dependencies": [
    {"what": "증명이 쓰는데 받는 edge에 없는 것", "used_at": "decorrelation.tex 287", "likely_from": "node id 또는 '모름'"}
  ],
  "notes": "자유. 확신이 낮은 곳."
}
```

`parent_change_requests` 는 상위 graph(이 node의 계약, 받는/보내는 edge, 다른 node, 기호 표)를 바꿔야 할 때만 적는다. 이 node의 계약 출력 항목 문구가 원문과 다르면 `change_item` 으로 적는다. 바꿀 필요가 없으면 빈 배열.


## 1. 여는 node의 계약 (top graph)

```json
{
 "id": "THM",
 "kind": "step",
 "title": "Theorem: 모든 multioverlap의 집중",
 "statement": "모든 고정 labeled topology $S$ 와 $\\eta>0$ 에서 $\\lim_{L\\to\\infty}\\limsup_{N\\to\\infty}\\mathcal A_{L,\\eta}\\operatorname{Var}(R_S)=0$. $b(S)$ 개의 branching 깊이만 평균한다. singleton은 각 고정 $L$ 에서 $\\operatorname{Var}(R_S)\\to0$ ($N\\to\\infty$).",
 "inputs": [
  "CC",
  "DC",
  "PB",
  "X_RT",
  "X_SAMP",
  "X_TI"
 ],
 "symbols": [
  "R_S",
  "A_avg",
  "b_S",
  "topology",
  "V_kL",
  "a_p",
  "mu",
  "F_d",
  "kappa",
  "anchor",
  "ext_hist",
  "delta",
  "N_lim",
  "E_root",
  "eta_regular"
 ],
 "outputs": [
  {
   "id": "main",
   "statement": "모든 고정 labeled topology $S$ 와 $\\eta>0$ 에서 $\\lim_{L\\to\\infty}\\limsup_{N\\to\\infty}\\mathcal A_{L,\\eta}\\operatorname{Var}(R_S)=0$. $b(S)$ 개의 branching 깊이만 평균한다. singleton은 각 고정 $L$ 에서 $\\operatorname{Var}(R_S)\\to0$ ($N\\to\\infty$).",
   "lines": [
    65,
    74
   ]
  }
 ],
 "statement_span": [
  63,
  75
 ],
 "proof_span": [
  532,
  611
 ]
}
```

## 2. 받는 edge (이 vertex로 들어오는 것 전부)

```json
[
 {
  "id": "t13",
  "from": "PB",
  "to": "THM",
  "kind": "flow",
  "summary": "projection, product_mean",
  "statement": "[PB.projection] $e$ 의 prefix가 주어졌을 때 $S$ 의 연속과 독립인 $B\\in[-1,1]^N$ 에 대해 $\\|(A_S-a_{S,e})\\cdot B\\|_{L^2}\\le p_N(S,e)$. [PB.product_mean] $S$ 가 깊이 $e$ 에서 처음 proper child shape $T_1,\\ldots,T_s$ 로 갈라지면 자식의 조건부 독립으로 $\\mu_{e,S}=\\prod_j\\mu_{e,T_j}$.",
  "carries": [
   {
    "node": "PB",
    "item": "projection",
    "used_at": [
     580
    ],
    "origin": "machine"
   },
   {
    "node": "PB",
    "item": "product_mean",
    "used_at": [
     576
    ],
    "origin": "supplemented"
   }
  ],
  "origin": "mixed",
  "grounding": {
   "source": "decorrelation.tex 580, 576"
  },
  "status": "connected",
  "complete": true
 },
 {
  "id": "t14",
  "from": "DC",
  "to": "THM",
  "kind": "flow",
  "summary": "martingale_energy",
  "statement": "[DC.martingale_energy] $T$ 의 나중 branching 깊이를 고정하고 처음 stem을 따라 path 하나를 뽑으면 $\\mu_{t,T}$ 는 유계 vector martingale이고 $\\sum_t\\mathbb E\\|\\mu_{t+1,T}-\\mu_{t,T}\\|_N^2\\le1$. (증명 블록 안의 식을 밖에서 참조)",
  "carries": [
   {
    "node": "DC",
    "item": "martingale_energy",
    "used_at": [
     583
    ],
    "origin": "machine"
   }
  ],
  "origin": "machine",
  "grounding": {
   "source": "decorrelation.tex 583"
  },
  "status": "connected",
  "complete": true
 },
 {
  "id": "t15",
  "from": "CC",
  "to": "THM",
  "kind": "flow",
  "summary": "fiber_bound, V_to_zero, main",
  "statement": "[CC.fiber_bound] 깊이 좌표 $D$ 개의 평균 안에서 어떤 항이 좌표 $D_j$ 개만 쓰고, 남는 배정마다 원상이 많아야 $L^{D-D_j}$ 개이며 그 좌표가 큰 $L$ 에서 $\\eta/2$-regular 이면, $0<\\gamma\\le1$ 에 대해 $L^{-D}\\sum_{\\mathbf q\\ \\eta\\text{-reg}}w_j(\\pi_j(\\mathbf q))^\\gamma\\le\\bigl(L^{-D_j}\\sum_{\\mathbf y\\ \\eta/2\\text{-reg}}w_j(\\mathbf y)\\bigr)^\\gamma$. shift하지 않은 항은 좌표를 옮기지 않고 같은 경계. [CC.V_to_zero] 모든 고정 $k,\\eta$ 에서 $V_{k,L}(\\eta)\\to0$ ($L\\to\\infty$). [CC.main] 모든 고정 labeled topology $S$ 와 $\\eta>0$ 에서 $\\lim_{L\\to\\infty}\\limsup_{N\\to\\infty}\\mathcal A_{L,\\eta}v_N(S,d)=0$. 평균은 $S$ 의 모든 branching 깊이와 첫 split보다 엄격히 앞선 regular 깊이 $d$ 에 대해서. singleton이면 $d$ 만.",
  "carries": [
   {
    "node": "CC",
    "item": "fiber_bound",
    "used_at": [
     607
    ],
    "origin": "machine"
   },
   {
    "node": "CC",
    "item": "V_to_zero",
    "used_at": [
     601,
     609
    ],
    "origin": "machine"
   },
   {
    "node": "CC",
    "item": "main",
    "used_at": [
     609
    ],
    "origin": "machine"
   }
  ],
  "origin": "machine",
  "grounding": {
   "source": "decorrelation.tex 607, 601, 609, 609"
  },
  "status": "connected",
  "complete": true
 },
 {
  "id": "t16",
  "from": "X_TI",
  "to": "THM",
  "kind": "call",
  "summary": "identity, anchor_constraint",
  "statement": "[X_TI.identity] 섭동족과 Lemma pert:selection 의 모든 수열을 따라 $\\sum_{E\\in\\mathfrak E(\\mathcal T,a_*,\\mathcal C)}c_E\\mathbb E[fR_E]-\\mathbb Ef\\sum_{E\\in\\mathfrak E(\\{a_*\\},a_*,\\mathcal C)}c_E\\mathbb E[R_E]\\to0$. 모든 고정 old tree, 두 종류의 anchor, multioverlap의 모든 유계 다항식 $f$, 유한 개의 순서 있는 추가 color, 모든 처방 제약 $\\mathcal C$ 에서 성립. 빈 추가도 허용. 오차는 고정 $L$, tree, 제약에서 $L$ 의 극한 전에 0으로 간다. [X_TI.anchor_constraint] $S_0=\\sigma_i$ 이면 spin anchor, $S_0=1$ 이면 marker anchor. 추가 color $1..k$ 는 anchor가 아닌 서로 다른 replica 자리를 차지한다. $\\mathcal C$ 는 추가 color와 anchor만의 쌍별 split 깊이의 일관된 모음을 처방하고 다른 old replica에는 제한을 걸지 않는다. $R_E$ 는 spin anchor이면 $\\frac1N\\sum_i\\sigma_i^{a_*}\\prod_j\\sigma_i^{a_j(E)}$, marker anchor이면 $\\frac1N\\sum_i\\prod_j\\sigma_i^{a_j(E)}$.",
  "carries": [
   {
    "node": "X_TI",
    "item": "identity",
    "used_at": [
     533,
     545,
     556
    ],
    "origin": "supplemented"
   },
   {
    "node": "X_TI",
    "item": "anchor_constraint",
    "used_at": [
     539,
     540
    ],
    "origin": "supplemented"
   }
  ],
  "origin": "supplemented",
  "grounding": {
   "source": "decorrelation.tex 533, 545, 556, 539, 540"
  },
  "status": "connected",
  "complete": true
 },
 {
  "id": "t17",
  "from": "X_RT",
  "to": "THM",
  "kind": "call",
  "summary": "kappa_total",
  "statement": "[X_RT.kappa_total] anchor와 color들이 처방한 tree $S$ 를 이루어야 하면, 임의 old tree의 모든 호환 extension 위의 계수 총합은 $\\kappa(S)$. 같은 한 걸음 규칙은 이미 만든 reference 집합에서 시작해 반복할 수 있다.",
  "carries": [
   {
    "node": "X_RT",
    "item": "kappa_total",
    "used_at": [
     545,
     547
    ],
    "origin": "supplemented"
   }
  ],
  "origin": "supplemented",
  "grounding": {
   "source": "decorrelation.tex 545, 547"
  },
  "status": "connected",
  "complete": true
 },
 {
  "id": "t18",
  "from": "X_SAMP",
  "to": "THM",
  "kind": "call",
  "summary": "children_independent, leaf_removal",
  "statement": "[X_SAMP.children_independent] 각 vertex에서 서로 다른 자식은 해당 kernel로 독립으로 뽑는다. $E_{\\mathcal T}$ 는 root가 주어진 표본 기대값. [X_SAMP.leaf_removal] leaf 몇 개와 남은 leaf가 쓰지 않는 path 부분을 지우면 남은 tree의 표본 법칙이 보존된다.",
  "carries": [
   {
    "node": "X_SAMP",
    "item": "children_independent",
    "used_at": [
     550
    ],
    "origin": "supplemented"
   },
   {
    "node": "X_SAMP",
    "item": "leaf_removal",
    "used_at": [
     553,
     555
    ],
    "origin": "supplemented"
   }
  ],
  "origin": "supplemented",
  "grounding": {
   "source": "decorrelation.tex 550, 553, 555"
  },
  "status": "connected",
  "complete": true
 }
]
```

## 3. 보내는 edge (이 vertex에서 나가는 것 전부)

```json
[
 {
  "id": "t22",
  "from": "THM",
  "to": "OUT",
  "kind": "flow",
  "summary": "main",
  "statement": "[THM.main] 모든 고정 labeled topology $S$ 와 $\\eta>0$ 에서 $\\lim_{L\\to\\infty}\\limsup_{N\\to\\infty}\\mathcal A_{L,\\eta}\\operatorname{Var}(R_S)=0$. $b(S)$ 개의 branching 깊이만 평균한다. singleton은 각 고정 $L$ 에서 $\\operatorname{Var}(R_S)\\to0$ ($N\\to\\infty$).",
  "carries": [
   {
    "node": "THM",
    "item": "main",
    "used_at": [
     "comparison.tex 153"
    ],
    "origin": "machine"
   }
  ],
  "origin": "machine",
  "grounding": {
   "source": "comparison.tex 153"
  },
  "status": "connected",
  "complete": true
 }
]
```

## 4. 기호 표의 해당 항목

```json
[
 {
  "id": "R_S",
  "tex": "$R_S$",
  "defined_at": "trees.tex 42–46; decorrelation.tex 60–61, 90",
  "text": "spin replica leaf 부분집합 $S$ 의 multioverlap $R_S=\\frac1N\\sum_{i}\\prod_{a\\in S}\\sigma_i^a$, $R_\\varnothing=1$. 수 5에서는 표본 leaf에 대해 $R_S=\\mathbf 1\\cdot A_S$."
 },
 {
  "id": "A_avg",
  "tex": "$\\mathcal A_{L,\\eta}$",
  "defined_at": "decorrelation.tex 30–38",
  "text": "$a$ 개 깊이 좌표 위의 음 아닌 배열 $z$ 에 대해 $\\mathcal A_{L,\\eta}z=L^{-a}\\sum_{\\mathbf q\\ \\eta\\text{-regular}}z(\\mathbf q)$. 추가 순서 제한(예: $d<\\min_vq_v$)은 합의 범위에 넣는다. 정규화하지 않은 평균이라 총질량 $\\le1$."
 },
 {
  "id": "b_S",
  "tex": "$b(S)$",
  "defined_at": "decorrelation.tex 20–21",
  "text": "topology $S$ 의 branching vertex 수."
 },
 {
  "id": "topology",
  "tex": "topology $S$",
  "defined_at": "decorrelation.tex 18–20",
  "text": "labeled leaf를 갖는 유한 rooted tree에서 unary vertex를 지운 것. 각 branching vertex에 $\\{0,\\ldots,L-1\\}$ 의 정수 깊이를 주며, 깊이는 모든 가지를 따라 엄격히 증가한다."
 },
 {
  "id": "V_kL",
  "tex": "$V_{k,L}(\\eta)$",
  "defined_at": "decorrelation.tex 253–257",
  "text": "$V_{k,L}(\\eta)=\\max_{1\\le|S|\\le k}\\limsup_{N}\\mathcal A_{L,\\eta}v_N(S,d)$. 최대는 유한 개 labeled topology 위."
 },
 {
  "id": "a_p",
  "tex": "$a_{S,e}$, $p_N(S,e)$",
  "defined_at": "decorrelation.tex 208–215",
  "text": "$S$ 가 깊이 $e$ 에서 처음 proper child shape $T_1,\\ldots,T_s$ 로 갈라질 때 $a_{S,e}=\\prod_j\\mu_{e,T_j}$ (좌표별 곱), $p_N(S,e)=\\sum_jv_N(T_j,e)^{1/4}$."
 },
 {
  "id": "mu",
  "tex": "$\\mu_{d,S}$",
  "defined_at": "decorrelation.tex 97–98",
  "text": "$\\mu_{d,S}=\\mathbb E[A_S\\mid\\mathscr F_d]$."
 },
 {
  "id": "F_d",
  "tex": "$\\mathscr F_d$",
  "defined_at": "decorrelation.tex 94–95",
  "text": "처음 stem 위의 깊이 $d$ (첫 branching 깊이 포함)에서 root와 깊이 $d$ 까지의 표본 prefix가 생성하는 sigma field."
 },
 {
  "id": "kappa",
  "tex": "$\\kappa(T)$",
  "defined_at": "trees.tex 346–354",
  "text": "reference 계수 $\\kappa(S)=\\prod_{v\\in\\operatorname{Br}(S)}\\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$; $a_v$, $d_v$ 는 처방한 reference tree에서 vertex의 자식 수와 깊이."
 },
 {
  "id": "anchor",
  "tex": "spin / marker anchor, $\\mathcal C$, $R_E$",
  "defined_at": "perturbations.tex 427–450",
  "text": "$S_0=\\sigma_i$ 이면 spin anchor, $S_0=1$ 이면 marker anchor. $\\mathcal C$ 는 추가 color와 anchor만의 쌍별 split 깊이를 처방한다. $R_E$ 는 history가 고른 새 replica(spin anchor이면 anchor 포함)의 multioverlap."
 },
 {
  "id": "ext_hist",
  "tex": "$E$, $c_E$, $\\mathfrak E(\\mathcal T,a_*,\\mathcal C)$",
  "defined_at": "trees.tex 259–276; perturbations.tex 427–440",
  "text": "extension history와 그 계수(선택한 계수들의 곱), 제약 $\\mathcal C$ 를 지키는 허용 history의 모음."
 },
 {
  "id": "delta",
  "tex": "$\\delta$",
  "defined_at": "decorrelation.tex 4",
  "text": "$\\delta=L^{-1}$."
 },
 {
  "id": "N_lim",
  "tex": "$N\\to\\infty$",
  "defined_at": "decorrelation.tex 4–8",
  "text": "각 고정 $L$ 에서 $N$ 의 극한은 모두 Lemma pert:selection 이 주는 크기와 매개변수 선택을 따라 취한다. 그 선택은 Theorem pert:tree-identity 의 항등식을 만족한다. $L$ 마다 다른 수열을 써도 된다. (선택 자체는 perturbations.tex 255–268)"
 },
 {
  "id": "E_root",
  "tex": "$\\mathbb E$",
  "defined_at": "trees.tex 47–48",
  "text": "따로 적지 않은 기대값 $\\mathbb E$ 는 root와 해당 tree의 표본추출을 포함한다."
 },
 {
  "id": "eta_regular",
  "tex": "$\\eta$-regular",
  "defined_at": "decorrelation.tex 21–28",
  "text": "모든 배정 깊이$/L$ 이 $(\\eta,1-\\eta)$ 안에 있고 서로 다른 branching vertex의 정규화 깊이가 $\\eta$ 보다 더 떨어진 배정. prefix 깊이 $d$ 가 추가로 지정되면 모든 branching 깊이에 대해 같은 제한을 지킨다. 한 topology의 두 사본이 aligned 깊이를 쓰면 대응 vertex는 깊이 좌표 하나를 공유하고, regularity는 서로 다른 좌표들에 건다."
 }
]
```

## 5. 원문 줄 범위 (decorrelation.tex, 줄 번호 포함)

### 63–75
```tex
  63  \begin{theorem}
  64  \label{decor:overlap-concentration}
  65  For every fixed labeled topology $S$,
  66  \begin{equation}
  67   \lim_{L\to\infty}\limsup_{N\to\infty}
  68         \mathcal A_{L,\eta}\operatorname{Var}(R_S)=0
  69         \qquad(\eta>0),
  70   \label{decor:overlap-concentration-equation}
  71  \end{equation}
  72  where only the $b(S)$ branching depths are averaged. For a
  73  singleton, whose average has no coordinates,
  74  $\operatorname{Var}(R_S)\to0$ as $N\to\infty$ at every fixed $L$.
  75  \end{theorem}
```
### 532–611
```tex
 532  \begin{proof}[Proof of \cref{decor:overlap-concentration}]
 533  For a singleton, use the spin-anchor identity with no added colors
 534  and $f=R_S$.  It gives
 535  $\mathbb ER_S^2=(\mathbb ER_S)^2+o_N(1)$.
 536  
 537  Suppose $S$ first splits at $e$ and has proper child shapes
 538  $T_1,\ldots,T_s$. We will condition one step before $e$. Use $S$ as
 539  the old tree, designate one of its
 540  leaves as a marker anchor, and add a full copy of $S$ all of whose
 541  leaves split from the anchor at $e-1$.  Its first path must be
 542  fresh at $e-1$, because the old tree has not yet branched there.
 543  All other target paths lie in the resulting fresh subtree.
 544  The extension coefficient on both sides of the prescribed-tree
 545  identity is the same nonzero number
 546  \begin{equation}
 547   C(S,e)=-\delta \kappa(S).
 548   \label{decor:marker-coefficient}
 549  \end{equation}
 550  The target and old copies are conditionally independent and
 551  identically distributed below $\mathscr F_{e-1}$. With
 552  $f=R_S$ and $M=\mathbb E[R_S\mid\mathscr F_{e-1}]$, their product has
 553  conditional expectation $M^2$. On the anchor-alone side, deleting the
 554  marker's continuation below $e-1$ integrates a probability kernel to one
 555  and leaves the ordinary target law $S$, with mean $\mathbb E R_S$.
 556  The identity therefore gives
 557  \begin{equation}
 558   C(S,e)\bigl(\mathbb EM^2-(\mathbb E R_S)^2\bigr)
 559   =C(S,e)\operatorname{Var}(M)=o_N(1),
 560   \label{decor:marker-variance-identity}
 561  \end{equation}
 562  and hence
 563  \begin{equation}
 564   \qquad \operatorname{Var}(M)\longrightarrow0
 565   \quad\text{at each fixed }L,S,e.
 566   \label{decor:prefix-projection-concentration}
 567  \end{equation}
 568  Division by $C(S,e)$ is made only at fixed $L$; no uniform lower
 569  bound as $L\to\infty$ is needed.
 570  
 571  It remains to control the conditional variance below this prefix.
 572  The child covariances are evaluated at $e$, which is separated from
 573  all their branching depths; the move to $e-1$ will use martingale
 574  continuity instead. Set
 575  \[
 576   G=\mathbf1\cdot\prod_j \mu_{e,T_j},
 577   \qquad G_-=\mathbf1\cdot\prod_j \mu_{e-1,T_j}.
 578  \]
 579  The latter is $\mathscr F_{e-1}$-measurable.  By
 580  \eqref{decor:projection-bound},
 581  $\mathbb E(R_S-G)^2\le p_N(S,e)^2$.
 582  Keeping all proper child depths fixed, the product difference
 583  inequality and \eqref{decor:martingale-energy} imply
 584  \begin{equation}
 585   \mathcal A_{L,\eta}\mathbb E(G-G_-)^2\le C_k/L.
 586   \label{decor:adjacent-prefix-error}
 587  \end{equation}
 588  Here $e$ is itself a ranged coordinate, so the one-step increments
 589  are summed before division by $L$.  Since conditional expectation
 590  is the optimal $L^2$ projection,
 591  \[
 592   \mathbb E(R_S-M)^2
 593     \le\mathbb E(R_S-G_-)^2
 594     \le2p_N(S,e)^2+2\mathbb E(G-G_-)^2.
 595  \]
 596  Variance decomposition and
 597  \eqref{decor:prefix-projection-concentration} now show
 598  \begin{equation}
 599   \limsup_{N\to\infty}
 600        \mathcal A_{L,\eta}\operatorname{Var}(R_S)
 601   \le C_k\left(L^{-1}+V_{k-1,L}(\eta/2)^{1/2}\right)
 602   \quad\text{for all sufficiently large }L.
 603   \label{decor:variance-estimate}
 604  \end{equation}
 605  In this estimate we used
 606  $p_N(S,e)^2\le s\sum_jv_N(T_j,e)^{1/2}$ and
 607  \eqref{decor:fiber-bound} with $\gamma=1/2$: here the full average has
 608  $D=b(S)$ coordinates because $d$ is absent, while still
 609  $D_j=b(T_j)+1$. Proposition~\ref{decor:conditional-concentration}
 610  finishes the proof.
 611  \end{proof}
```
