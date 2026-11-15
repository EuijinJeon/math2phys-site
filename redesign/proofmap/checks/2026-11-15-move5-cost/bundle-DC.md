# 입력 묶음: top.DC 를 연다

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
 "id": "DC",
 "kind": "step",
 "title": "Lemma: 깊이에 대한 평균 연속성",
 "statement": "topology $S$ 와 branching vertex 부분집합 $U$ 를 고정하고 각 $\\eta$-regular 배정에서 $S^U$ 를 둔다. 조상 쪽 평가 깊이 $d$ 에서 같은 표본 prefix로 평균을 비교하면, 충분히 큰 $L$ 에서 $\\mathcal A_{L,\\eta}\\mathbb E\\|\\mu_{d,S^U}-\\mu_{d,S}\\|_N^2\\le C/L$. 평균은 모든 branching 깊이에 대해서이고, $d$ 가 움직이면 $d$ 도 평균하고 아니면 고정한다. $d$ 가 $S$ 의 처음 unary 구간을 따라 움직이면 $\\mathcal A_{L,\\eta}\\mathbb E\\|\\mu_{d+1,S}-\\mu_{d,S}\\|_N^2\\le C/L$. 이 평균은 $d$ 와 모든 branching 깊이를 포함하고, 평균들은 같은 표본 path 위에서 평가한다. 상수는 vertex 수와 shift 수에만 의존하고 $N$, 평가 깊이, transition kernel에 균일하다. $T$ 의 나중 branching 깊이를 고정하고 처음 stem을 따라 path 하나를 뽑으면 $\\mu_{t,T}$ 는 유계 vector martingale이고 $\\sum_t\\mathbb E\\|\\mu_{t+1,T}-\\mu_{t,T}\\|_N^2\\le1$. (증명 블록 안의 식을 밖에서 참조) 관련된 한-prefix 주변 법칙은 다른 표본 가지를 빼도 변하지 않으므로 이 평가들은 더 큰 표본 tree 안에서도 성립한다.",
 "inputs": [
  "AVG",
  "X_SAMP"
 ],
 "symbols": [
  "topology",
  "S_U",
  "mu",
  "F_d",
  "A_avg",
  "eta_regular",
  "A_S"
 ],
 "outputs": [
  {
   "id": "branch_shift",
   "statement": "topology $S$ 와 branching vertex 부분집합 $U$ 를 고정하고 각 $\\eta$-regular 배정에서 $S^U$ 를 둔다. 조상 쪽 평가 깊이 $d$ 에서 같은 표본 prefix로 평균을 비교하면, 충분히 큰 $L$ 에서 $\\mathcal A_{L,\\eta}\\mathbb E\\|\\mu_{d,S^U}-\\mu_{d,S}\\|_N^2\\le C/L$. 평균은 모든 branching 깊이에 대해서이고, $d$ 가 움직이면 $d$ 도 평균하고 아니면 고정한다.",
   "lines": [
    144,
    155
   ]
  },
  {
   "id": "eval_shift",
   "statement": "$d$ 가 $S$ 의 처음 unary 구간을 따라 움직이면 $\\mathcal A_{L,\\eta}\\mathbb E\\|\\mu_{d+1,S}-\\mu_{d,S}\\|_N^2\\le C/L$. 이 평균은 $d$ 와 모든 branching 깊이를 포함하고, 평균들은 같은 표본 path 위에서 평가한다.",
   "lines": [
    155,
    163
   ]
  },
  {
   "id": "uniform_constant",
   "statement": "상수는 vertex 수와 shift 수에만 의존하고 $N$, 평가 깊이, transition kernel에 균일하다.",
   "lines": [
    163,
    165
   ]
  },
  {
   "id": "martingale_energy",
   "statement": "$T$ 의 나중 branching 깊이를 고정하고 처음 stem을 따라 path 하나를 뽑으면 $\\mu_{t,T}$ 는 유계 vector martingale이고 $\\sum_t\\mathbb E\\|\\mu_{t+1,T}-\\mu_{t,T}\\|_N^2\\le1$. (증명 블록 안의 식을 밖에서 참조)",
   "lines": [
    169,
    175
   ]
  },
  {
   "id": "larger_tree",
   "statement": "관련된 한-prefix 주변 법칙은 다른 표본 가지를 빼도 변하지 않으므로 이 평가들은 더 큰 표본 tree 안에서도 성립한다.",
   "lines": [
    203,
    205
   ]
  }
 ],
 "statement_span": [
  142,
  166
 ],
 "proof_span": [
  168,
  206
 ]
}
```

## 2. 받는 edge (이 vertex로 들어오는 것 전부)

```json
[
 {
  "id": "t19",
  "from": "AVG",
  "to": "DC",
  "kind": "definition",
  "summary": "shift_regular",
  "statement": "[AVG.shift_regular] 좌표의 임의 부분집합을 고정 정수만큼 옮기면, 충분히 큰 $L$ 에서 $\\eta$-regular 배정이 $\\eta/2$-regular 배정으로 단사로 간다.",
  "carries": [
   {
    "node": "AVG",
    "item": "shift_regular",
    "used_at": [
     202,
     203
    ],
    "origin": "supplemented"
   }
  ],
  "origin": "supplemented",
  "grounding": {
   "source": "decorrelation.tex 202, 203"
  },
  "status": "connected",
  "complete": true
 },
 {
  "id": "t20",
  "from": "X_SAMP",
  "to": "DC",
  "kind": "call",
  "summary": "leaf_removal",
  "statement": "[X_SAMP.leaf_removal] leaf 몇 개와 남은 leaf가 쓰지 않는 path 부분을 지우면 남은 tree의 표본 법칙이 보존된다.",
  "carries": [
   {
    "node": "X_SAMP",
    "item": "leaf_removal",
    "used_at": [
     204,
     205
    ],
    "origin": "supplemented"
   }
  ],
  "origin": "supplemented",
  "grounding": {
   "source": "decorrelation.tex 204, 205"
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
  "id": "t8",
  "from": "DC",
  "to": "CC",
  "kind": "flow",
  "summary": "branch_shift, eval_shift, larger_tree",
  "statement": "[DC.branch_shift] topology $S$ 와 branching vertex 부분집합 $U$ 를 고정하고 각 $\\eta$-regular 배정에서 $S^U$ 를 둔다. 조상 쪽 평가 깊이 $d$ 에서 같은 표본 prefix로 평균을 비교하면, 충분히 큰 $L$ 에서 $\\mathcal A_{L,\\eta}\\mathbb E\\|\\mu_{d,S^U}-\\mu_{d,S}\\|_N^2\\le C/L$. 평균은 모든 branching 깊이에 대해서이고, $d$ 가 움직이면 $d$ 도 평균하고 아니면 고정한다. [DC.eval_shift] $d$ 가 $S$ 의 처음 unary 구간을 따라 움직이면 $\\mathcal A_{L,\\eta}\\mathbb E\\|\\mu_{d+1,S}-\\mu_{d,S}\\|_N^2\\le C/L$. 이 평균은 $d$ 와 모든 branching 깊이를 포함하고, 평균들은 같은 표본 path 위에서 평가한다. [DC.larger_tree] 관련된 한-prefix 주변 법칙은 다른 표본 가지를 빼도 변하지 않으므로 이 평가들은 더 큰 표본 tree 안에서도 성립한다.",
  "carries": [
   {
    "node": "DC",
    "item": "branch_shift",
    "used_at": [
     368
    ],
    "origin": "machine"
   },
   {
    "node": "DC",
    "item": "eval_shift",
    "used_at": [
     367,
     368
    ],
    "origin": "machine"
   },
   {
    "node": "DC",
    "item": "larger_tree",
    "used_at": [
     368
    ],
    "origin": "supplemented"
   }
  ],
  "origin": "mixed",
  "grounding": {
   "source": "decorrelation.tex 368, 367, 368, 368"
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
 }
]
```

## 4. 기호 표의 해당 항목

```json
[
 {
  "id": "topology",
  "tex": "topology $S$",
  "defined_at": "decorrelation.tex 18–20",
  "text": "labeled leaf를 갖는 유한 rooted tree에서 unary vertex를 지운 것. 각 branching vertex에 $\\{0,\\ldots,L-1\\}$ 의 정수 깊이를 주며, 깊이는 모든 가지를 따라 엄격히 증가한다."
 },
 {
  "id": "S_U",
  "tex": "$S^U$",
  "defined_at": "decorrelation.tex 144–146",
  "text": "$S$ 와 같은 topology에서 branching vertex 부분집합 $U$ 의 깊이를 1씩 올린 것."
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
  "id": "A_avg",
  "tex": "$\\mathcal A_{L,\\eta}$",
  "defined_at": "decorrelation.tex 30–38",
  "text": "$a$ 개 깊이 좌표 위의 음 아닌 배열 $z$ 에 대해 $\\mathcal A_{L,\\eta}z=L^{-a}\\sum_{\\mathbf q\\ \\eta\\text{-regular}}z(\\mathbf q)$. 추가 순서 제한(예: $d<\\min_vq_v$)은 합의 범위에 넣는다. 정규화하지 않은 평균이라 총질량 $\\le1$."
 },
 {
  "id": "eta_regular",
  "tex": "$\\eta$-regular",
  "defined_at": "decorrelation.tex 21–28",
  "text": "모든 배정 깊이$/L$ 이 $(\\eta,1-\\eta)$ 안에 있고 서로 다른 branching vertex의 정규화 깊이가 $\\eta$ 보다 더 떨어진 배정. prefix 깊이 $d$ 가 추가로 지정되면 모든 branching 깊이에 대해 같은 제한을 지킨다. 한 topology의 두 사본이 aligned 깊이를 쓰면 대응 vertex는 깊이 좌표 하나를 공유하고, regularity는 서로 다른 좌표들에 건다."
 },
 {
  "id": "A_S",
  "tex": "$A_S$, $x\\cdot y$, $\\|x\\|_N$",
  "defined_at": "decorrelation.tex 87–93",
  "text": "$S$ 의 표본 사본에 대해 $A_S=(\\prod_{a\\in S}\\sigma_i^a)_{i\\le N}$, $x\\cdot y=N^{-1}\\sum_ix_iy_i$, $\\|x\\|_N^2=x\\cdot x$."
 }
]
```

## 5. 원문 줄 범위 (decorrelation.tex, 줄 번호 포함)

### 142–166
```tex
 142  \begin{lemma}[Averaged continuity in depth]
 143  \label{decor:depth-continuity}
 144  Fix a topology $S$ and a subset $U$ of its branching vertices. For each
 145  $\eta$-regular depth assignment, let $S^U$ have the same topology with
 146  the depths of the vertices in $U$ increased by one. At an ancestral
 147  evaluation depth $d$, compare the means using the same sampled prefix.
 148  Then, for all sufficiently large $L$,
 149  \begin{equation}
 150   \mathcal A_{L,\eta}\mathbb E
 151         \|\mu_{d,S^U}-\mu_{d,S}\|_N^2\le C/L.
 152   \label{decor:branch-depth-continuity}
 153  \end{equation}
 154  The average ranges over all branching depths; the coordinate $d$ is
 155  also averaged if it ranges, and otherwise is held fixed. If $d$ ranges
 156  along an initial unary stretch of $S$, then
 157  \begin{equation}
 158   \mathcal A_{L,\eta}\mathbb E
 159         \|\mu_{d+1,S}-\mu_{d,S}\|_N^2\le C/L,
 160   \label{decor:evaluation-depth-continuity}
 161  \end{equation}
 162  where this average includes $d$ and all branching depths, and the means
 163  are evaluated along the same sampled path. The constant depends only on
 164  the number of vertices and shifts, uniformly in $N$, the evaluation
 165  depth, and the transition kernels.
 166  \end{lemma}
```
### 168–206
```tex
 168  \begin{proof}
 169  Keep the later branching depths of $T$ fixed and sample a single path
 170  along its initial stem. On this path, $\mu_{t,T}$ is a bounded vector
 171  martingale. Orthogonality of its increments gives
 172  \begin{equation}
 173   \sum_t\mathbb E\|\mu_{t+1,T}-\mu_{t,T}\|_N^2\le1.
 174   \label{decor:martingale-energy}
 175  \end{equation}
 176  This proves the evaluation-depth assertion after summing over the
 177  ranged depth and dividing by $L$.
 178  
 179  Consider a branching vertex at depth $q$ with child shapes
 180  $T_1,\ldots,T_s$.  Holding their later depths fixed, its original
 181  conditional mean is $\prod_j \mu_{q,T_j}$, with products understood
 182  coordinatewise.  If the split is delayed to $q+1$, its conditional mean
 183  at the same prefix of depth $q$ is
 184  $\mathbb E[\prod_j \mu_{q+1,T_j}\mid\mathscr F_q]$, where the child means
 185  are evaluated on a common one-step continuation.  Jensen's inequality
 186  and the product difference inequality on $[-1,1]^s$ yield
 187  \begin{equation}
 188   \mathbb E\left\|\prod_j \mu_{q,T_j}
 189         -\mathbb E\left[\prod_j \mu_{q+1,T_j}\mid\mathscr F_q\right]
 190         \right\|_N^2
 191   \le s\sum_j\mathbb E\|\mu_{q+1,T_j}-\mu_{q,T_j}\|_N^2.
 192   \label{decor:one-vertex-shift}
 193  \end{equation}
 194  Summing over $q$ uses \eqref{decor:martingale-energy} with each child
 195  shape fixed.  Propagating a changed subtree mean towards an ancestral
 196  evaluation consists of conditional expectations and multiplication
 197  by factors bounded by one.  Both operations contract this squared
 198  norm.  Averaging over all other depth coordinates therefore proves
 199  the claimed $C/L$ bound for one shift.  For several shifts, change the
 200  vertices one at a time and use the squared triangle inequality with
 201  a factor equal to the number of shifts.  Regularity ensures that the
 202  intermediate shapes have the same ancestry relations and, for large
 203  $L$, lie in the enlarged $\eta/2$-regular domain.  All relevant
 204  one-prefix marginal laws are unchanged when other sampled branches
 205  are omitted, so these estimates hold in any larger sampled tree.
 206  \end{proof}
```
