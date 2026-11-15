# 입력 묶음: top.CON 를 연다

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
 "id": "CON",
 "kind": "step",
 "title": "Lemma: 축약과 세 사본",
 "statement": "random vector $B\\in[-1,1]^N$ 이 $\\mathscr F_d$ 가 주어졌을 때 $A_S$ 와 조건부 독립이면 $\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}$. $X,Y,Z$ 가 sigma field $\\mathscr G$ 가 주어졌을 때 유계 random vector의 조건부 독립 사본이고 $C$ 가 그 조건부 공분산 행렬이면 $\\mathbb E(X\\cdot Y-X\\cdot Z)^2\\ge\\frac2{N^2}\\mathbb E\\sum_{i,j}C_{ij}^2$.",
 "inputs": [],
 "symbols": [
  "A_S",
  "F_d",
  "mu",
  "v_N",
  "E_root"
 ],
 "outputs": [
  {
   "id": "contraction",
   "statement": "random vector $B\\in[-1,1]^N$ 이 $\\mathscr F_d$ 가 주어졌을 때 $A_S$ 와 조건부 독립이면 $\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}$.",
   "lines": [
    110,
    116
   ]
  },
  {
   "id": "three_copy",
   "statement": "$X,Y,Z$ 가 sigma field $\\mathscr G$ 가 주어졌을 때 유계 random vector의 조건부 독립 사본이고 $C$ 가 그 조건부 공분산 행렬이면 $\\mathbb E(X\\cdot Y-X\\cdot Z)^2\\ge\\frac2{N^2}\\mathbb E\\sum_{i,j}C_{ij}^2$.",
   "lines": [
    117,
    124
   ]
  }
 ],
 "statement_span": [
  108,
  125
 ],
 "proof_span": [
  127,
  140
 ]
}
```

## 2. 받는 edge (이 vertex로 들어오는 것 전부)

```json
[]
```

## 3. 보내는 edge (이 vertex에서 나가는 것 전부)

```json
[
 {
  "id": "t2",
  "from": "CON",
  "to": "PB",
  "kind": "flow",
  "summary": "contraction",
  "statement": "[CON.contraction] random vector $B\\in[-1,1]^N$ 이 $\\mathscr F_d$ 가 주어졌을 때 $A_S$ 와 조건부 독립이면 $\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}$.",
  "carries": [
   {
    "node": "CON",
    "item": "contraction",
    "used_at": [
     218
    ],
    "origin": "machine"
   }
  ],
  "origin": "machine",
  "grounding": {
   "source": "decorrelation.tex 218"
  },
  "status": "connected",
  "complete": true
 },
 {
  "id": "t4",
  "from": "CON",
  "to": "CC",
  "kind": "flow",
  "summary": "three_copy",
  "statement": "[CON.three_copy] $X,Y,Z$ 가 sigma field $\\mathscr G$ 가 주어졌을 때 유계 random vector의 조건부 독립 사본이고 $C$ 가 그 조건부 공분산 행렬이면 $\\mathbb E(X\\cdot Y-X\\cdot Z)^2\\ge\\frac2{N^2}\\mathbb E\\sum_{i,j}C_{ij}^2$.",
  "carries": [
   {
    "node": "CON",
    "item": "three_copy",
    "used_at": [
     288,
     483
    ],
    "origin": "machine"
   }
  ],
  "origin": "machine",
  "grounding": {
   "source": "decorrelation.tex 288, 483"
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
  "id": "A_S",
  "tex": "$A_S$, $x\\cdot y$, $\\|x\\|_N$",
  "defined_at": "decorrelation.tex 87–93",
  "text": "$S$ 의 표본 사본에 대해 $A_S=(\\prod_{a\\in S}\\sigma_i^a)_{i\\le N}$, $x\\cdot y=N^{-1}\\sum_ix_iy_i$, $\\|x\\|_N^2=x\\cdot x$."
 },
 {
  "id": "F_d",
  "tex": "$\\mathscr F_d$",
  "defined_at": "decorrelation.tex 94–95",
  "text": "처음 stem 위의 깊이 $d$ (첫 branching 깊이 포함)에서 root와 깊이 $d$ 까지의 표본 prefix가 생성하는 sigma field."
 },
 {
  "id": "mu",
  "tex": "$\\mu_{d,S}$",
  "defined_at": "decorrelation.tex 97–98",
  "text": "$\\mu_{d,S}=\\mathbb E[A_S\\mid\\mathscr F_d]$."
 },
 {
  "id": "v_N",
  "tex": "$v_N(S,d)$",
  "defined_at": "decorrelation.tex 99–104",
  "text": "$v_N(S,d)=N^{-2}\\mathbb E\\sum_{i,j}\\operatorname{Cov}(A_{S,i},A_{S,j}\\mid\\mathscr F_d)^2$. 기대값은 root를 포함한다. $A_S$, $\\mu_{d,S}$ 의 좌표는 절댓값 $\\le1$, $0\\le v_N\\le1$."
 },
 {
  "id": "E_root",
  "tex": "$\\mathbb E$",
  "defined_at": "trees.tex 47–48",
  "text": "따로 적지 않은 기대값 $\\mathbb E$ 는 root와 해당 tree의 표본추출을 포함한다."
 }
]
```

## 5. 원문 줄 범위 (decorrelation.tex, 줄 번호 포함)

### 108–125
```tex
 108  \begin{lemma}[Contractions and three copies]
 109  \label{decor:contractions}
 110  If a random vector $B\in[-1,1]^N$ is conditionally independent of $A_S$
 111  given $\mathscr F_d$, then
 112  \begin{equation}
 113   \bigl\|(A_S-\mu_{d,S})\cdot B\bigr\|_{L^2}
 114          \le v_N(S,d)^{1/4}.
 115   \label{decor:contraction-bound}
 116  \end{equation}
 117  If $X,Y,Z$ are conditionally independent copies of a bounded random
 118  vector given a sigma field $\mathscr G$, and $C$ is its conditional
 119  covariance matrix, then
 120  \begin{equation}
 121   \mathbb E(X\cdot Y-X\cdot Z)^2
 122         \ge \frac2{N^2}\mathbb E\sum_{i,j}C_{ij}^2.
 123   \label{decor:three-copy-bound}
 124  \end{equation}
 125  \end{lemma}
```
### 127–140
```tex
 127  \begin{proof}
 128  Conditional on $\mathscr F_d$ and $B$, the squared contraction has
 129  expectation $N^{-2}\sum_{ij}C_{ij}B_iB_j$.  Its absolute value is at
 130  most $N^{-2}\sum_{ij}|C_{ij}|$.  Cauchy--Schwarz, first over $i,j$
 131  and then over the prefix, proves \eqref{decor:contraction-bound}.
 132  For the second assertion, write $\mu=\mathbb E[X\mid\mathscr G]$.
 133  Conditional independence gives
 134  \[
 135   \mathbb E[(X\cdot Y-X\cdot Z)^2\mid\mathscr G]
 136   =\frac2{N^2}\operatorname{tr}\bigl((C+\mu\mu^{\mathsf T})C\bigr)
 137   \ge\frac2{N^2}\operatorname{tr}(C^2),
 138  \]
 139  since $C$ is positive semidefinite.
 140  \end{proof}
```
