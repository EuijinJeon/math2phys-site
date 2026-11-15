# 입력 묶음: top.CC 를 연다

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


## 1. 여는 node의 계약 (top graph). 출력 항목의 진술은 여기에만 있다

```json
{"id": "CC", "kind": "step", "title": "Proposition: 조건부 decorrelation", "inputs": ["AVG", "CON", "DC", "IDE", "PB", "X_CH", "X_EXT", "X_RT", "X_SAMP", "X_TI"], "symbols": ["v_N", "A_avg", "eta_regular", "V_kL", "topology", "b_S", "S_plus", "J", "kappa", "a_p", "ext_hist", "anchor", "eps_NLk", "m_d", "delta", "N_lim", "R_S", "A_S", "mu", "F_d", "E_root"], "outputs": [{"id": "main", "statement": "모든 고정 labeled topology $S$ 와 $\\eta>0$ 에서 $\\lim_{L\\to\\infty}\\limsup_{N\\to\\infty}\\mathcal A_{L,\\eta}v_N(S,d)=0$. 평균은 $S$ 의 모든 branching 깊이와 첫 split보다 엄격히 앞선 regular 깊이 $d$ 에 대해서. singleton이면 $d$ 만.", "lines": [236, 244]}, {"id": "V_to_zero", "statement": "모든 고정 $k,\\eta$ 에서 $V_{k,L}(\\eta)\\to0$ ($L\\to\\infty$).", "lines": [522, 523]}, {"id": "relative_cost", "statement": "증명의 구성($S^+$, $J$) 안에서 Lemma tree:charging 으로 $\\frac1{|J|}\\sum_{\\text{allowed}}|c|\\le C_{k,\\eta}$. (증명 블록 안의 식; 밖의 참조는 remark 하나뿐)", "lines": [345, 353]}, {"id": "fiber_bound", "statement": "깊이 좌표 $D$ 개의 평균 안에서 어떤 항이 좌표 $D_j$ 개만 쓰고, 남는 배정마다 원상이 많아야 $L^{D-D_j}$ 개이며 그 좌표가 큰 $L$ 에서 $\\eta/2$-regular 이면, $0<\\gamma\\le1$ 에 대해 $L^{-D}\\sum_{\\mathbf q\\ \\eta\\text{-reg}}w_j(\\pi_j(\\mathbf q))^\\gamma\\le\\bigl(L^{-D_j}\\sum_{\\mathbf y\\ \\eta/2\\text{-reg}}w_j(\\mathbf y)\\bigr)^\\gamma$. shift하지 않은 항은 좌표를 옮기지 않고 같은 경계.", "lines": [491, 509], "author_filled": "원문은 이 부등식을 aligned 두 사본 구성($D=b(S)+1$)에서만 적고, THM(607–609)이 $D=b(S)$ 로 다시 쓴다. 두 쓰임을 한 항목으로 묶으려고 가정을 일반형으로 적은 것은 작성자다."}], "statement_span": [234, 245], "proof_span": [247, 524]}
```

## 2. 받는 edge (이 vertex로 들어오는 것 전부). 싣는 항목의 진술은 6절 항목 사전에 있다

```json
[{"id": "t3", "from": "AVG", "to": "CC", "kind": "definition", "carries": [{"node": "AVG", "item": "holder", "used_at": [262], "origin": "machine"}, {"node": "AVG", "item": "unused_coord", "used_at": [259, 260], "origin": "supplemented"}, {"node": "AVG", "item": "shift_regular", "used_at": [260, 497, 498], "origin": "supplemented"}], "origin": "mixed", "grounding": {"source": "decorrelation.tex 262, 259, 260, 260, 497, 498"}, "status": "connected", "complete": true}, {"id": "t4", "from": "CON", "to": "CC", "kind": "flow", "carries": [{"node": "CON", "item": "three_copy", "used_at": [288, 483], "origin": "machine"}], "origin": "machine", "grounding": {"source": "decorrelation.tex 288, 483"}, "status": "connected", "complete": true}, {"id": "t5", "from": "X_RT", "to": "CC", "kind": "call", "carries": [{"node": "X_RT", "item": "kappa_total", "used_at": [332, 414, 415], "origin": "machine"}, {"node": "X_RT", "item": "one_reference_total", "used_at": [414], "origin": "supplemented"}], "origin": "mixed", "grounding": {"source": "decorrelation.tex 332, 414, 415, 414"}, "status": "connected", "complete": true}, {"id": "t6", "from": "X_CH", "to": "CC", "kind": "call", "carries": [{"node": "X_CH", "item": "relative_charging", "used_at": [348, 352], "origin": "machine"}], "origin": "machine", "grounding": {"source": "decorrelation.tex 348, 352"}, "status": "connected", "complete": true}, {"id": "t7", "from": "PB", "to": "CC", "kind": "flow", "carries": [{"node": "PB", "item": "projection", "used_at": [364, 460], "origin": "machine"}, {"node": "PB", "item": "two_sides", "used_at": [364, 481, 482], "origin": "supplemented"}, {"node": "PB", "item": "scalar_test", "used_at": [453, 454], "origin": "supplemented"}], "origin": "mixed", "grounding": {"source": "decorrelation.tex 364, 460, 364, 481, 482, 453, 454"}, "status": "connected", "complete": true}, {"id": "t8", "from": "DC", "to": "CC", "kind": "flow", "carries": [{"node": "DC", "item": "branch_shift", "used_at": [368], "origin": "machine"}, {"node": "DC", "item": "eval_shift", "used_at": [367, 368], "origin": "machine"}, {"node": "DC", "item": "larger_tree", "used_at": [368], "origin": "supplemented"}], "origin": "mixed", "grounding": {"source": "decorrelation.tex 368, 367, 368, 368"}, "status": "connected", "complete": true}, {"id": "t9", "from": "IDE", "to": "CC", "kind": "flow", "carries": [{"node": "IDE", "item": "eps_def", "used_at": [450, 514], "origin": "machine"}, {"node": "IDE", "item": "eps_to_zero", "used_at": [457, 514], "origin": "machine"}, {"node": "IDE", "item": "L_constants", "used_at": [450], "origin": "supplemented"}], "origin": "mixed", "grounding": {"source": "decorrelation.tex 450, 514, 457, 514, 450"}, "status": "connected", "complete": true}, {"id": "t10", "from": "X_TI", "to": "CC", "kind": "call", "carries": [{"node": "X_TI", "item": "identity", "used_at": [250, 279, 298, 435], "origin": "supplemented"}, {"node": "X_TI", "item": "anchor_constraint", "used_at": [265, 296, 299], "origin": "supplemented"}], "origin": "supplemented", "grounding": {"source": "decorrelation.tex 250, 279, 298, 435, 265, 296, 299"}, "status": "connected", "complete": true}, {"id": "t11", "from": "X_EXT", "to": "CC", "kind": "call", "carries": [{"node": "X_EXT", "item": "rule", "used_at": [266, 269, 391, 393], "origin": "supplemented"}], "origin": "supplemented", "grounding": {"source": "decorrelation.tex 266, 269, 391, 393"}, "status": "connected", "complete": true}, {"id": "t12", "from": "X_SAMP", "to": "CC", "kind": "call", "carries": [{"node": "X_SAMP", "item": "children_independent", "used_at": [287, 363, 395], "origin": "supplemented"}, {"node": "X_SAMP", "item": "leaf_removal", "used_at": [404, 405], "origin": "supplemented"}], "origin": "supplemented", "grounding": {"source": "decorrelation.tex 287, 363, 395, 404, 405"}, "status": "connected", "complete": true}]
```

## 3. 보내는 edge (이 vertex에서 나가는 것 전부). 싣는 항목의 진술은 1절에 있다

```json
[{"id": "t15", "from": "CC", "to": "THM", "kind": "flow", "carries": [{"node": "CC", "item": "fiber_bound", "used_at": [607], "origin": "machine"}, {"node": "CC", "item": "V_to_zero", "used_at": [601, 609], "origin": "machine"}, {"node": "CC", "item": "main", "used_at": [609], "origin": "machine"}], "origin": "machine", "grounding": {"source": "decorrelation.tex 607, 601, 609, 609"}, "status": "connected", "complete": true}]
```

## 4. 기호 표의 해당 항목

```json
[{"id": "v_N", "tex": "$v_N(S,d)$", "defined_at": "decorrelation.tex 99–104", "text": "$v_N(S,d)=N^{-2}\\mathbb E\\sum_{i,j}\\operatorname{Cov}(A_{S,i},A_{S,j}\\mid\\mathscr F_d)^2$. 기대값은 root를 포함한다. $A_S$, $\\mu_{d,S}$ 의 좌표는 절댓값 $\\le1$, $0\\le v_N\\le1$."}, {"id": "A_avg", "tex": "$\\mathcal A_{L,\\eta}$", "defined_at": "decorrelation.tex 30–38", "text": "$a$ 개 깊이 좌표 위의 음 아닌 배열 $z$ 에 대해 $\\mathcal A_{L,\\eta}z=L^{-a}\\sum_{\\mathbf q\\ \\eta\\text{-regular}}z(\\mathbf q)$. 추가 순서 제한(예: $d<\\min_vq_v$)은 합의 범위에 넣는다. 정규화하지 않은 평균이라 총질량 $\\le1$."}, {"id": "eta_regular", "tex": "$\\eta$-regular", "defined_at": "decorrelation.tex 21–28", "text": "모든 배정 깊이$/L$ 이 $(\\eta,1-\\eta)$ 안에 있고 서로 다른 branching vertex의 정규화 깊이가 $\\eta$ 보다 더 떨어진 배정. prefix 깊이 $d$ 가 추가로 지정되면 모든 branching 깊이에 대해 같은 제한을 지킨다. 한 topology의 두 사본이 aligned 깊이를 쓰면 대응 vertex는 깊이 좌표 하나를 공유하고, regularity는 서로 다른 좌표들에 건다."}, {"id": "V_kL", "tex": "$V_{k,L}(\\eta)$", "defined_at": "decorrelation.tex 253–257", "text": "$V_{k,L}(\\eta)=\\max_{1\\le|S|\\le k}\\limsup_{N}\\mathcal A_{L,\\eta}v_N(S,d)$. 최대는 유한 개 labeled topology 위."}, {"id": "topology", "tex": "topology $S$", "defined_at": "decorrelation.tex 18–20", "text": "labeled leaf를 갖는 유한 rooted tree에서 unary vertex를 지운 것. 각 branching vertex에 $\\{0,\\ldots,L-1\\}$ 의 정수 깊이를 주며, 깊이는 모든 가지를 따라 엄격히 증가한다."}, {"id": "b_S", "tex": "$b(S)$", "defined_at": "decorrelation.tex 20–21", "text": "topology $S$ 의 branching vertex 수."}, {"id": "S_plus", "tex": "$S^+$", "defined_at": "decorrelation.tex 297–298", "text": "$S$ 의 모든 내부 branching 깊이를 1씩 올린 topology."}, {"id": "J", "tex": "$J$", "defined_at": "decorrelation.tex 333–336", "text": "$J=\\kappa(S^+)^2$."}, {"id": "kappa", "tex": "$\\kappa(T)$", "defined_at": "trees.tex 346–354", "text": "reference 계수 $\\kappa(S)=\\prod_{v\\in\\operatorname{Br}(S)}\\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$; $a_v$, $d_v$ 는 처방한 reference tree에서 vertex의 자식 수와 깊이."}, {"id": "a_p", "tex": "$a_{S,e}$, $p_N(S,e)$", "defined_at": "decorrelation.tex 208–215", "text": "$S$ 가 깊이 $e$ 에서 처음 proper child shape $T_1,\\ldots,T_s$ 로 갈라질 때 $a_{S,e}=\\prod_j\\mu_{e,T_j}$ (좌표별 곱), $p_N(S,e)=\\sum_jv_N(T_j,e)^{1/4}$."}, {"id": "ext_hist", "tex": "$E$, $c_E$, $\\mathfrak E(\\mathcal T,a_*,\\mathcal C)$", "defined_at": "trees.tex 259–276; perturbations.tex 427–440", "text": "extension history와 그 계수(선택한 계수들의 곱), 제약 $\\mathcal C$ 를 지키는 허용 history의 모음."}, {"id": "anchor", "tex": "spin / marker anchor, $\\mathcal C$, $R_E$", "defined_at": "perturbations.tex 427–450", "text": "$S_0=\\sigma_i$ 이면 spin anchor, $S_0=1$ 이면 marker anchor. $\\mathcal C$ 는 추가 color와 anchor만의 쌍별 split 깊이를 처방한다. $R_E$ 는 history가 고른 새 replica(spin anchor이면 anchor 포함)의 multioverlap."}, {"id": "eps_NLk", "tex": "$\\varepsilon_{N,L,k}$", "defined_at": "decorrelation.tex 49–58", "text": "아래에서 쓰는 유한 모음 위에서 취한 Theorem pert:tree-identity 오차의 최대."}, {"id": "m_d", "tex": "$m_d$", "defined_at": "decorrelation.tex 4", "text": "이 절 전체에서 $m_d=d/L$."}, {"id": "delta", "tex": "$\\delta$", "defined_at": "decorrelation.tex 4", "text": "$\\delta=L^{-1}$."}, {"id": "N_lim", "tex": "$N\\to\\infty$", "defined_at": "decorrelation.tex 4–8", "text": "각 고정 $L$ 에서 $N$ 의 극한은 모두 Lemma pert:selection 이 주는 크기와 매개변수 선택을 따라 취한다. 그 선택은 Theorem pert:tree-identity 의 항등식을 만족한다. $L$ 마다 다른 수열을 써도 된다. (선택 자체는 perturbations.tex 255–268)"}, {"id": "R_S", "tex": "$R_S$", "defined_at": "trees.tex 42–46; decorrelation.tex 60–61, 90", "text": "spin replica leaf 부분집합 $S$ 의 multioverlap $R_S=\\frac1N\\sum_{i}\\prod_{a\\in S}\\sigma_i^a$, $R_\\varnothing=1$. 수 5에서는 표본 leaf에 대해 $R_S=\\mathbf 1\\cdot A_S$."}, {"id": "A_S", "tex": "$A_S$, $x\\cdot y$, $\\|x\\|_N$", "defined_at": "decorrelation.tex 87–93", "text": "$S$ 의 표본 사본에 대해 $A_S=(\\prod_{a\\in S}\\sigma_i^a)_{i\\le N}$, $x\\cdot y=N^{-1}\\sum_ix_iy_i$, $\\|x\\|_N^2=x\\cdot x$."}, {"id": "mu", "tex": "$\\mu_{d,S}$", "defined_at": "decorrelation.tex 97–98", "text": "$\\mu_{d,S}=\\mathbb E[A_S\\mid\\mathscr F_d]$."}, {"id": "F_d", "tex": "$\\mathscr F_d$", "defined_at": "decorrelation.tex 94–95", "text": "처음 stem 위의 깊이 $d$ (첫 branching 깊이 포함)에서 root와 깊이 $d$ 까지의 표본 prefix가 생성하는 sigma field."}, {"id": "E_root", "tex": "$\\mathbb E$", "defined_at": "trees.tex 47–48", "text": "따로 적지 않은 기대값 $\\mathbb E$ 는 root와 해당 tree의 표본추출을 포함한다."}]
```

## 5. 원문 줄 범위 (decorrelation.tex, 줄 번호 포함)

### 234–245
```tex
 234  \begin{proposition}
 235  \label{decor:conditional-concentration}
 236  For every fixed labeled topology $S$ and every $\eta>0$,
 237  \begin{equation}
 238   \lim_{L\to\infty}\limsup_{N\to\infty}
 239         \mathcal A_{L,\eta}v_N(S,d)=0,
 240   \label{decor:conditional-concentration-equation}
 241  \end{equation}
 242  where the average ranges over all branching depths of $S$ and an
 243  additional regular depth $d$ strictly before its first split.  For a
 244  singleton, the average ranges over $d$ alone.
 245  \end{proposition}
```
### 247–524
```tex
 247  \begin{proof}
 248  We induct on the number $k$ of leaves. The induction replaces each
 249  proper child by its conditional mean. It then applies the prescribed-tree
 250  identity to two copies with delayed branching depths; after summing the
 251  signed coefficients, this becomes a nonnegative three-copy estimate.
 252  To keep track of the depth averages, let
 253  \begin{equation}
 254   V_{k,L}(\eta)=\max_{1\le |S|\le k}
 255         \limsup_{N\to\infty}\mathcal A_{L,\eta}v_N(S,d).
 256   \label{decor:V-definition}
 257  \end{equation}
 258  The maximum is over finitely many labeled topologies.  Averages of
 259  any lower-order covariance used below, including averages with extra
 260  unused coordinates or shifted depths, are bounded by the appropriate
 261  $V_{k-1,L}(\eta/2)$, using
 262  \eqref{decor:average-holder} when fractional powers occur.
 263  
 264  \paragraph{One leaf.}
 265  Take two old paths splitting at $d$, with path $1$ a spin anchor, and
 266  add one color required to split from the anchor exactly at $d$.
 267  The available old path $2$ has coefficient $1$.  A fresh path can
 268  split from both old paths at $d$, with coefficient $-c_d$, or follow
 269  path $2$ and leave it at $\ell>d$, with coefficient $-c_\ell$, where
 270  \begin{equation}
 271   c_d=2m_{d+1}-m_d=(d+2)\delta,
 272   \qquad c_\ell=\delta\quad(d<\ell\le L-1).
 273   \label{decor:c-weights}
 274  \end{equation}
 275  From the anchor alone the total coefficient is $-\delta$.
 276  Write $X=R_{12}$ and $X_\ell=R_{13}$ for the corresponding fresh
 277  extension.  Each $X_\ell$ has the marginal law of $X$, and
 278  $\sum_{\ell=d}^{L-1}c_\ell=1+\delta$.  The prescribed-tree identity
 279  with $f=X$ therefore gives
 280  \begin{equation}
 281   \frac12\sum_{\ell=d}^{L-1}c_\ell
 282        \mathbb E(X-X_\ell)^2
 283         =\delta\operatorname{Var}(X)+o_N(1)
 284         \le\delta+o_N(1).
 285   \label{decor:singleton-identity}
 286  \end{equation}
 287  For $\ell=d$, the three spin vectors are conditionally independent
 288  below $d$.  Hence \eqref{decor:three-copy-bound} and $c_d\ge\eta$
 289  give $v_N(S,d)\le\delta/\eta+o_N(1)$ at each fixed $L,d$.
 290  This proves $V_{1,L}(\eta)\le\delta/\eta$.
 291  
 292  \paragraph{Shifted copies and their coefficients.}
 293  Let $|S|=k\ge2$, its first split be $e>d$, and its proper child shapes
 294  be $T_1,\ldots,T_s$.  Sample an old tree consisting of two copies of
 295  $S$, denoted I and II, whose stems split at $d$ and whose internal
 296  depth assignments are aligned.  Fix an old leaf in I as the spin
 297  anchor.  Let $S^+$ be the topology $S$ with every internal branching
 298  depth increased by one.  In the prescribed-tree identity require
 299  the anchor and the added colors to form two copies of $S^+$,
 300  separated at $d$, with the anchor in its original labeled position
 301  in the first copy.  These constraints involve only the anchor and
 302  the added colors.  Add all other colors of side I first, then those
 303  of side II. \Cref{decor:shift-figure} illustrates one local shift.
 304  
 305  \begin{figure}[!ht]
 306  \centering
 307  \begin{tikzpicture}[x=1.05cm,y=0.82cm,>=stealth,font=\small]
 308   \draw[gray!45,densely dotted] (-2.9,-1) -- (2.3,-1);
 309   \draw[gray!45,densely dotted] (-2.9,-2) -- (2.3,-2);
 310   \node[left] at (-2.9,-1) {$e$};
 311   \node[left] at (-2.9,-2) {$e+1$};
 312   \draw[thick] (0,0) -- (0,-1) -- (-1,-2) -- (-2,-3.2);
 313   \draw[thick] (0,-1) -- (1.5,-3.2);
 314   \draw[blue!65!black,very thick,dashed] (-1,-2) -- (-0.05,-3.2);
 315   \fill (0,-1) circle (2pt);
 316   \fill[blue!65!black] (-1,-2) circle (2.2pt);
 317   \node[above] at (0,0) {common stem};
 318   \node[below] at (-2,-3.2) {anchor};
 319   \node[below,blue!65!black] at (-0.05,-3.2) {new child};
 320   \node[below] at (1.5,-3.2) {old leaf};
 321   \node[right,blue!65!black] at (-0.5,-2.6) {$-\delta$};
 322  \end{tikzpicture}
 323  \caption{One local effect of delaying a target split. The old tree is solid;
 324  the dashed child creates a split at the previously unary depth-$e+1$ vertex,
 325  with coefficient $m_{e+1}-m_{e+2}=-\delta$.
 326  The proof shifts every internal target depth and charges distinct vertices
 327  separately, even when their depths coincide. Later target colors may reuse
 328  eligible old leaves.}
 329  \label{decor:shift-figure}
 330  \end{figure}
 331  
 332  Let $\kappa(T)$ be the reference coefficient \eqref{tree:K}, and put
 333  \begin{equation}
 334   J=\kappa(S^+)^2.
 335   \label{decor:J-definition}
 336  \end{equation}
 337  At each
 338  vertex the $j=1$ factor is $-\delta$; for $j\ge2$ its absolute value
 339  is at least $\eta/2$ for all sufficiently large $L$.  If $b=b(S)$,
 340  then
 341  \begin{equation}
 342   |J|\ge c_{k,\eta}\delta^{2b}>0.
 343   \label{decor:J-lower-bound}
 344  \end{equation}
 345  For large $L$, regularity ensures that each shifted depth differs from
 346  every branching depth of the old tree, including $d$. Thus these $2b$
 347  target branching vertices must be created by fresh unary splits.
 348  Lemma~\ref{tree:charging} gives
 349  \begin{equation}
 350   \frac1{|J|}\sum_{\text{allowed extensions}}|c|
 351          \le C_{k,\eta}.
 352   \label{decor:relative-absolute-cost}
 353  \end{equation}
 354  The two copies have aligned depths but distinct branching vertices:
 355  each vertex supplies its own factor $\delta$. This is the reason for
 356  the shift. The full signed coefficient has an additional factor
 357  $-\delta$ from separation at $d$; we divide by $J$ and leave that
 358  factor in the identity. Equation~\eqref{decor:relative-absolute-cost}
 359  then controls every projection error after division.
 360  
 361  \paragraph{Projecting the two target sides.}
 362  In every extension, the marginal target tree consists of two
 363  ordinary copies of $S^+$, independent below their separation at $d$.
 364  By \eqref{decor:projection-bound} its multioverlap differs in
 365  $L^2$ from the contraction of its projected means at $e+1$ by at
 366  most $2p_N(S^+,e+1)$.  Change the proper child depths back by one,
 367  then change their evaluation depth from $e+1$ to $e$.  The product
 368  difference inequality and Lemma~\ref{decor:depth-continuity} show
 369  that this adds an error at most $h_N(S)$ in $L^2$, with
 370  \begin{equation}
 371   \mathcal A_{L,\eta}h_N(S)^2\le C_k/L.
 372   \label{decor:projection-shift-error}
 373  \end{equation}
 374  One can take $h_N(S)$ to be the sum of the finitely many
 375  $L^2(\|\cdot\|_N)$ distances in these comparisons, multiplied by
 376  a size-dependent constant.  This definition depends only on the
 377  single-copy marginal shapes, not on the particular extension.
 378  Thus \eqref{decor:projection-shift-error} holds uniformly for the
 379  comparisons in the extension sum, even though the union of the
 380  old and target trees itself need not have regular depths.
 381  
 382  Let $a,b$ denote the vectors $a_{S,e}$ on the old stems I and II.
 383  The target stem in I shares the old prefix through $e$ because it
 384  contains the anchor, so its final projected vector is $a$.
 385  
 386  \paragraph{The signed extension sum.}
 387  Set $f$ to be the overlap of all $2k$ old leaves, an allowed fixed
 388  overlap monomial. All target-I additions stay in the anchor's branch
 389  below $d$, so they leave the old-II stem and its child counts unchanged.
 390  Classify the first added path of target side II by its prefix
 391  through $e$.  It may diverge freshly at $\ell=d$, with coefficient
 392  $-c_d$, or follow the old II stem and diverge at $d<\ell<e$, with
 393  coefficient $-c_\ell=-\delta$.  In such a class let $b_\ell$ be
 394  $a_{S,e}$ on the new stem; it shares the old II prefix through
 395  $\ell$.  At $\ell=d$ the stems carrying $a,b,b_d$ are conditionally
 396  independent below $d$.  Every remaining possibility follows the
 397  old II prefix through $e$ and has final projected vector $b$.
 398  All later target paths in side II follow its first path through
 399  $e$, since their earliest split is $e+1$.
 400  
 401  For a fixed extension history, retain every old path and the first
 402  target-II prefix through $e$, and delete all other new branches.
 403  The target-I projection $a$ already depends only on the retained old
 404  anchor prefix. Each deleted subtree integrates to one under its
 405  probability kernels; a reused old leaf introduces no new variable.
 406  The retained tree depends only on the class: it is the old tree with a
 407  fresh stem attached at $\ell<e$, or just the old tree in the remaining
 408  class. The history is a combinatorial choice, not a condition on sampled
 409  values. Thus the joint marginal of the old paths and projected prefixes
 410  is fixed within each class. In particular, the expectation of $f$ times
 411  the projected overlap is constant within a class and can be multiplied
 412  by its total signed coefficient.
 413  
 414  By Lemma~\ref{tree:reference-total}, summing later side-II colors
 415  backwards gives $\kappa(S^+)$ for each first-path choice.  Summing the
 416  side-I choices gives the other factor $\kappa(S^+)$. The fresh class
 417  at $\ell$ therefore has total coefficient $-c_\ell J$.
 418  The total coefficient is $-\delta J$, both from the old tree and
 419  from the anchor alone. Since
 420  \[
 421   \sum_{\ell=d}^{e-1}c_\ell=(e+1)\delta=m_e+\delta,
 422  \]
 423  the remaining prefix-through-$e$ class has coefficient $m_eJ$.
 424  Thus the projected terms have the following coefficients:
 425  \[
 426   \begin{array}{c|c|c}
 427   \text{side-II prefix} & \text{projected overlap}
 428        & \text{total coefficient}\\ \hline
 429   \text{fresh divergence at }d\le\ell<e & a\cdot b_\ell & -c_\ell J\\
 430   \text{old prefix through }e & a\cdot b & m_eJ
 431   \end{array}
 432  \]
 433  
 434  Multiply the projected overlap in each row by $f$ and divide the
 435  prescribed-tree identity by $J$. Rearranging gives
 436  \begin{equation}
 437   \sum_{\ell=d}^{e-1}c_\ell
 438     \mathbb E\bigl[f(a\cdot b-a\cdot b_\ell)\bigr]
 439   =\delta\bigl(\mathbb E[f(a\cdot b)]
 440            -\mathbb Ef\,\mathbb ER_{\mathrm{target}}\bigr)
 441         +\rho_N(S,d),
 442   \label{decor:induction-identity}
 443  \end{equation}
 444  where $R_{\mathrm{target}}$ on the right is the target overlap in
 445  the anchor-alone extension.  Its absolute value is at most one.
 446  The error satisfies
 447  \begin{equation}
 448   |\rho_N(S,d)|\le C_{k,\eta}
 449         \bigl(p_N(S^+,e+1)+h_N(S)\bigr)
 450         +C_{L,k,\eta}\varepsilon_{N,L,k}.
 451   \label{decor:induction-error}
 452  \end{equation}
 453  Indeed, multiplying a projection error by $f$, even when correlated
 454  with it, costs at most its $L^2$ norm since $|f|\le1$. Sum these errors
 455  with absolute coefficients and apply
 456  \eqref{decor:relative-absolute-cost}. The final term includes division
 457  of the original identity error by $J$ and tends to zero at fixed $L$.
 458  
 459  \paragraph{Closing the induction.}
 460  Equation~\eqref{decor:projection-bound} gives
 461  $\|f-a\cdot b\|_{L^2}\le2p_N(S,e)$.
 462  Moreover
 463  $\sum_{\ell=d}^{e-1}c_\ell=(e+1)\delta\le1$.
 464  Replacing $f$ by $a\cdot b$ on the left of
 465  \eqref{decor:induction-identity} therefore costs at most
 466  $4p_N(S,e)$.  Each $a\cdot b_\ell$ has the same marginal law as
 467  $a\cdot b$, so that left side becomes
 468  \[
 469   \frac12\sum_{\ell=d}^{e-1}c_\ell
 470          \mathbb E(a\cdot b-a\cdot b_\ell)^2.
 471  \]
 472  Its summands are nonnegative and $c_d\ge\eta$.  The right side
 473  of \eqref{decor:induction-identity} is bounded in absolute value
 474  by $2\delta+|\rho_N(S,d)|$.  Hence
 475  \begin{equation}
 476   \mathbb E(a\cdot b-a\cdot b_d)^2
 477   \le C_\eta\bigl(\delta+p_N(S,e)+|\rho_N(S,d)|\bigr).
 478   \label{decor:projected-three-copy}
 479  \end{equation}
 480  Sample three copies of $A_S$ conditionally independently below
 481  $d$.  Projecting each of the two contractions involving the
 482  first copy changes it in $L^2$ by at most $2p_N(S,e)$.
 483  Using \eqref{decor:three-copy-bound},
 484  \eqref{decor:projected-three-copy}, and $p_N(S,e)\le k$, we obtain
 485  \begin{equation}
 486   v_N(S,d)\le C_{k,\eta}\bigl(
 487         \delta+p_N(S,e)+p_N(S^+,e+1)+h_N(S)\bigr)
 488         +C_{L,k,\eta}\varepsilon_{N,L,k}.
 489   \label{decor:covariance-induction-estimate}
 490  \end{equation}
 491  Each child in either $p_N$ has fewer than $k$ leaves. To make the
 492  averaging step explicit, the aligned construction has
 493  $D=b(S)+1$ distinct depth coordinates, including $d$ and $e$.
 494  A term belonging to $T_j$ uses only $D_j=b(T_j)+1$ coordinates.
 495  For the shifted term these are
 496  $\pi_j(\mathbf q)=(e+1,(q_v+1)_{v\in\operatorname{Br}(T_j)})$.
 497  Every retained assignment has at most $L^{D-D_j}$ preimages, and its
 498  coordinates are $\eta/2$-regular for large $L$. If $w_j$ is the child
 499  covariance as a function of these coordinates, then, for $0<\gamma\le1$,
 500  \begin{align}
 501   L^{-D}\sum_{\mathbf q\;\eta\text{-regular}}
 502         w_j(\pi_j(\mathbf q))^\gamma
 503   &\le L^{-D_j}\sum_{\mathbf y\;\eta/2\text{-regular}}w_j(\mathbf y)^\gamma
 504   \notag\\
 505   &\le\left(L^{-D_j}\sum_{\mathbf y\;\eta/2\text{-regular}}
 506         w_j(\mathbf y)\right)^\gamma.
 507   \label{decor:fiber-bound}
 508  \end{align}
 509  The unshifted term has the same bound without translating the coordinates.
 510  Thus the two aligned copies use single-copy estimates; there is no
 511  restriction of an independently averaged pair of copies to a diagonal.
 512  Taking $\gamma=1/4$ and then $\limsup_N$, and using
 513  \eqref{decor:projection-shift-error} and
 514  \eqref{decor:identity-error}, gives, for sufficiently large $L$,
 515  \begin{equation}
 516   V_{k,L}(\eta)\le C_{k,\eta}\left(
 517         L^{-1/2}+V_{k-1,L}(\eta/2)^{1/4}\right).
 518   \label{decor:induction-recursion}
 519  \end{equation}
 520  The maximum over smaller topologies in \eqref{decor:V-definition}
 521  can be absorbed in the right side because these covariances are
 522  bounded by one.  The base case and induction now imply
 523  $V_{k,L}(\eta)\to0$ for every fixed $k,\eta$, proving the proposition.
 524  \end{proof}
```

## 6. 항목 사전 (받는 edge가 싣는 남의 출력 항목, 하나에 한 번)

```json
{"AVG.holder": {"statement": "$0<\\gamma\\le1$ 이면 $\\mathcal A_{L,\\eta}(z^\\gamma)\\le(\\mathcal A_{L,\\eta}z)^\\gamma$.", "lines": [38, 43], "source": "decorrelation.tex 30–47"}, "AVG.unused_coord": {"statement": "쓰지 않는 좌표에 대한 합은 많아야 $L$ 배이고 그 좌표의 정규화가 상쇄한다.", "lines": [44, 45], "source": "decorrelation.tex 30–47"}, "AVG.shift_regular": {"statement": "좌표의 임의 부분집합을 고정 정수만큼 옮기면, 충분히 큰 $L$ 에서 $\\eta$-regular 배정이 $\\eta/2$-regular 배정으로 단사로 간다.", "lines": [45, 47], "source": "decorrelation.tex 30–47"}, "CON.three_copy": {"statement": "$X,Y,Z$ 가 sigma field $\\mathscr G$ 가 주어졌을 때 유계 random vector의 조건부 독립 사본이고 $C$ 가 그 조건부 공분산 행렬이면 $\\mathbb E(X\\cdot Y-X\\cdot Z)^2\\ge\\frac2{N^2}\\mathbb E\\sum_{i,j}C_{ij}^2$.", "lines": [117, 124], "source": "decorrelation.tex 108–140"}, "X_RT.kappa_total": {"statement": "anchor와 color들이 처방한 tree $S$ 를 이루어야 하면, 임의 old tree의 모든 호환 extension 위의 계수 총합은 $\\kappa(S)$. 같은 한 걸음 규칙은 이미 만든 reference 집합에서 시작해 반복할 수 있다.", "lines": [346, 356], "source": "trees.tex 337–356"}, "X_RT.one_reference_total": {"statement": "다음 color가 처방한 reference prefix를 깊이 $d$ 까지 따라가고 거기서 reference path를 담은 $j\\ge1$ 개 자식과 다른 자식으로 들어가야 하면(그 밖의 연속은 자유), 허용 선택의 계수 합은 $m_d-jm_{d+1}$.", "lines": [337, 345], "source": "trees.tex 337–356"}, "X_CH.relative_charging": {"statement": "그 $b$ 개 vertex에 대해 $J=\\prod_v\\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$ 로 두고 그 모두에서 $m_{d_v}\\ge\\eta>0$ 이면 $J\\ne0$ 이고 $\\frac1{|J|}\\sum_{E\\text{ allowed}}|c_E|\\le C_{q,k,\\eta}$.", "lines": [406, 414], "source": "trees.tex 393–414"}, "PB.projection": {"statement": "$e$ 의 prefix가 주어졌을 때 $S$ 의 연속과 독립인 $B\\in[-1,1]^N$ 에 대해 $\\|(A_S-a_{S,e})\\cdot B\\|_{L^2}\\le p_N(S,e)$.", "lines": [216, 225], "source": "decorrelation.tex 208–230"}, "PB.two_sides": {"statement": "특히 $B=\\mathbf 1$ 과, $e$ 전에 갈라진 다른 쪽에서 뽑은 vector에 적용된다. 그런 두 쪽은 함께 사영해 총 $L^2$ 오차가 많아야 $2p_N(S,e)$.", "lines": [225, 228], "source": "decorrelation.tex 208–230"}, "PB.scalar_test": {"statement": "$|f|\\le1$ 인 scalar 시험함수를 축약 오차에 곱하면, 상관되어 있어도 $L^1$ 경계가 커지지 않는다.", "lines": [228, 230], "source": "decorrelation.tex 208–230"}, "DC.branch_shift": {"statement": "topology $S$ 와 branching vertex 부분집합 $U$ 를 고정하고 각 $\\eta$-regular 배정에서 $S^U$ 를 둔다. 조상 쪽 평가 깊이 $d$ 에서 같은 표본 prefix로 평균을 비교하면, 충분히 큰 $L$ 에서 $\\mathcal A_{L,\\eta}\\mathbb E\\|\\mu_{d,S^U}-\\mu_{d,S}\\|_N^2\\le C/L$. 평균은 모든 branching 깊이에 대해서이고, $d$ 가 움직이면 $d$ 도 평균하고 아니면 고정한다.", "lines": [144, 155], "source": "decorrelation.tex 142–206"}, "DC.eval_shift": {"statement": "$d$ 가 $S$ 의 처음 unary 구간을 따라 움직이면 $\\mathcal A_{L,\\eta}\\mathbb E\\|\\mu_{d+1,S}-\\mu_{d,S}\\|_N^2\\le C/L$. 이 평균은 $d$ 와 모든 branching 깊이를 포함하고, 평균들은 같은 표본 path 위에서 평가한다.", "lines": [155, 163], "source": "decorrelation.tex 142–206"}, "DC.larger_tree": {"statement": "관련된 한-prefix 주변 법칙은 다른 표본 가지를 빼도 변하지 않으므로 이 평가들은 더 큰 표본 tree 안에서도 성립한다.", "lines": [203, 205], "source": "decorrelation.tex 142–206"}, "IDE.eps_def": {"statement": "유계 크기의 labeled topology는 유한 개이고 고정 $L$ 에서 깊이 배정도 유한 개이므로, Theorem pert:tree-identity 의 오차를 아래의 유한 모음 위에서 $N\\to\\infty$ 전에 최대화할 수 있다. 그 최대가 $\\varepsilon_{N,L,k}$.", "lines": [49, 53], "source": "decorrelation.tex 49–58"}, "IDE.eps_to_zero": {"statement": "각 고정 $L,k$ 에서 $\\varepsilon_{N,L,k}\\to0$ ($N\\to\\infty$).", "lines": [53, 57], "source": "decorrelation.tex 49–58"}, "IDE.L_constants": {"statement": "이 오차에 곱하는 상수는 $L$ 에 임의로 의존해도 된다.", "lines": [58, 58], "source": "decorrelation.tex 49–58"}, "X_TI.identity": {"statement": "섭동족과 Lemma pert:selection 의 모든 수열을 따라 $\\sum_{E\\in\\mathfrak E(\\mathcal T,a_*,\\mathcal C)}c_E\\mathbb E[fR_E]-\\mathbb Ef\\sum_{E\\in\\mathfrak E(\\{a_*\\},a_*,\\mathcal C)}c_E\\mathbb E[R_E]\\to0$. 모든 고정 old tree, 두 종류의 anchor, multioverlap의 모든 유계 다항식 $f$, 유한 개의 순서 있는 추가 color, 모든 처방 제약 $\\mathcal C$ 에서 성립. 빈 추가도 허용. 오차는 고정 $L$, tree, 제약에서 $L$ 의 극한 전에 0으로 간다.", "lines": [452, 470], "source": "perturbations.tex 427–470"}, "X_TI.anchor_constraint": {"statement": "$S_0=\\sigma_i$ 이면 spin anchor, $S_0=1$ 이면 marker anchor. 추가 color $1..k$ 는 anchor가 아닌 서로 다른 replica 자리를 차지한다. $\\mathcal C$ 는 추가 color와 anchor만의 쌍별 split 깊이의 일관된 모음을 처방하고 다른 old replica에는 제한을 걸지 않는다. $R_E$ 는 spin anchor이면 $\\frac1N\\sum_i\\sigma_i^{a_*}\\prod_j\\sigma_i^{a_j(E)}$, marker anchor이면 $\\frac1N\\sum_i\\prod_j\\sigma_i^{a_j(E)}$.", "lines": [427, 450], "source": "perturbations.tex 427–470"}, "X_EXT.rule": {"statement": "anchor leaf $a_*$ 를 가진 tree $\\mathcal T$ 에서 color $1..k$ 를 차례로 배정한다. 다음 color는 (i) $a_*$ 가 아닌 안 쓴 old leaf (계수 $1$) 또는 (ii) 현재 tree의 내부 vertex $\\beta$ 에서 fresh path (계수 $\\gamma_\\beta=m_{d_\\beta}-n_\\beta m_{d_\\beta+1}$). 현재 tree는 안 쓴 것을 포함한 모든 old path와 이미 붙인 path. $c_E$ 는 계수들의 곱, $\\mathcal T_E$ 는 마지막 tree.", "lines": [259, 276], "source": "trees.tex 259–276"}, "X_SAMP.children_independent": {"statement": "각 vertex에서 서로 다른 자식은 해당 kernel로 독립으로 뽑는다. $E_{\\mathcal T}$ 는 root가 주어진 표본 기대값.", "lines": [28, 34], "source": "trees.tex 28–39, 47–48"}, "X_SAMP.leaf_removal": {"statement": "leaf 몇 개와 남은 leaf가 쓰지 않는 path 부분을 지우면 남은 tree의 표본 법칙이 보존된다.", "lines": [38, 39], "source": "trees.tex 28–39, 47–48"}}
```
