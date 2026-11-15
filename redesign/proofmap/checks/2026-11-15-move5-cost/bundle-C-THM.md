# 입력 묶음: top.THM 를 연다

## 0. 할 일과 규칙 (구조만 쓰는 판)

수학 논문 한 절의 증명 지도(proof map)를 짓는 중이다. 맨 위 graph의 node 하나를 **연다**: 그 node의 증명 블록을 한 층 아래의 하위 graph로 옮긴다. 이 묶음에 있는 것만 쓴다. 다른 파일, 다른 원문, 기억하는 문헌을 쓰지 않는다. 묶음에 없는 것이 필요하면 지어내지 말고 `missed_dependencies` 나 `parent_change_requests` 에 적는다.

**원문과 카드가 이미 말한 것을 다시 쓰지 않는다.** 화면은 node의 원문 줄과 카드의 번역(`math`)을 그 자리에 펼쳐 보여 준다. 너는 다음만 쓴다:

1. **경계**: 어느 원문 줄 범위가 안쪽 node 하나인가. 원문 증명 순서와 문단 경계를 따르고 9개 안팎. 7절 카드 가운데 그 범위와 맞는 것이 있으면 `card` 에 id를 적는다(카드의 경계가 원문과 맞지 않으면 원문을 따르고 `note` 에 적는다).
2. **의존**: 무엇이 무엇에 쓰이는가. edge는 보낸 쪽의 무엇을(받는 edge의 항목 이름, 또는 앞 node의 결과) 받는 쪽의 어느 줄에서 쓰는지만 적는다.
3. **원문에 없는 걸음**: 원문이 적지 않았는데 그 걸음이 서려면 필요한 것. 이것만 문장과 식으로 쓴다(`author_filled`).

`title` 은 15자 안팎의 짧은 이름. `statement` 칸은 쓰지 않는다. 원문 줄이 그 node의 진술이다.

## 0.1 산출 (JSON 하나)

```json
{
  "graph": {"id": "<NODE 소문자>", "parent": {"graph": "top", "node": "<NODE>"},
    "nodes": [
      {"id": "s1", "kind": "step", "title": "짧은 이름", "lines": [533, 535], "card": "카드 id 또는 null",
       "status": "sketch",
       "author_filled": [{"what": "원문에 없는 걸음 한 줄", "expr": "필요하면 식"}],
       "note": "필요할 때만"},
      {"id": "x_PB", "kind": "external", "external_ref": "PB", "import_edge": "t13", "items": ["projection"]},
      {"id": "out", "kind": "output", "output_items": ["main"], "lines": [65, 74]}
    ],
    "edges": [
      {"id": "e1", "from": "x_PB", "to": "s6", "carries": ["projection"], "used_at": [580]},
      {"id": "e2", "from": "s5", "to": "s9", "carries": ["result"], "used_at": [597]}
    ]},
  "parent_change_requests": [{"target": "...", "kind": "add_item | change_item | new_edge | new_symbol | other", "detail": "...", "source_lines": "..."}],
  "missed_dependencies": [{"what": "...", "used_at": "...", "likely_from": "node id 또는 '모름'"}],
  "notes": "확신이 낮은 곳만, 짧게"
}
```

- 받는 edge(2절)마다 external node 하나: `external_ref` = 그 edge의 `from`, `import_edge` = 그 edge의 `id`, `items` = 실제로 쓰는 항목 이름. 2절의 모든 `from` 이 external로 있어야 한다.
- 1절 계약의 출력 항목은 output node의 `output_items` 가 맡는다. 3절의 보내는 edge가 싣는 항목이 모두 어느 output에서 나와야 한다.
- 안쪽 node에서 나오는 edge의 `carries` 는 `["result"]` 처럼 그 node의 결과를 가리키면 된다(그 node의 원문 줄이 내용이다).
- `status` 는 `sketch`. `grounding.state` 는 쓰지 않는다(모두 `proposed` 로 취급).
- 기호는 4절 기호 표의 id로만 가리킨다. 증명 안에서 새로 정의되는 기호는 node의 `defines: ["기호", ...]` 에 이름만 적는다(정의는 그 node의 원문 줄에 있다).


## 1. 여는 node의 계약 (top graph). 출력 항목의 진술은 여기에만 있다

```json
{"id": "THM", "kind": "step", "title": "Theorem: 모든 multioverlap의 집중", "inputs": ["CC", "DC", "PB", "X_RT", "X_SAMP", "X_TI"], "symbols": ["R_S", "A_avg", "b_S", "topology", "V_kL", "a_p", "mu", "F_d", "kappa", "anchor", "ext_hist", "delta", "N_lim", "E_root", "eta_regular"], "outputs": [{"id": "main", "lines": [65, 74]}], "statement_span": [63, 75], "proof_span": [532, 611]}
```

## 2. 받는 edge (이 vertex로 들어오는 것 전부). 싣는 항목의 진술은 6절 항목 사전에 있다

```json
[{"id": "t13", "from": "PB", "to": "THM", "kind": "flow", "carries": [{"node": "PB", "item": "projection", "used_at": [580], "origin": "machine"}, {"node": "PB", "item": "product_mean", "used_at": [576], "origin": "supplemented"}], "origin": "mixed", "grounding": {"source": "decorrelation.tex 580, 576"}, "status": "connected", "complete": true}, {"id": "t14", "from": "DC", "to": "THM", "kind": "flow", "carries": [{"node": "DC", "item": "martingale_energy", "used_at": [583], "origin": "machine"}], "origin": "machine", "grounding": {"source": "decorrelation.tex 583"}, "status": "connected", "complete": true}, {"id": "t15", "from": "CC", "to": "THM", "kind": "flow", "carries": [{"node": "CC", "item": "fiber_bound", "used_at": [607], "origin": "machine"}, {"node": "CC", "item": "V_to_zero", "used_at": [601, 609], "origin": "machine"}, {"node": "CC", "item": "main", "used_at": [609], "origin": "machine"}], "origin": "machine", "grounding": {"source": "decorrelation.tex 607, 601, 609, 609"}, "status": "connected", "complete": true}, {"id": "t16", "from": "X_TI", "to": "THM", "kind": "call", "carries": [{"node": "X_TI", "item": "identity", "used_at": [533, 545, 556], "origin": "supplemented"}, {"node": "X_TI", "item": "anchor_constraint", "used_at": [539, 540], "origin": "supplemented"}], "origin": "supplemented", "grounding": {"source": "decorrelation.tex 533, 545, 556, 539, 540"}, "status": "connected", "complete": true}, {"id": "t17", "from": "X_RT", "to": "THM", "kind": "call", "carries": [{"node": "X_RT", "item": "kappa_total", "used_at": [545, 547], "origin": "supplemented"}], "origin": "supplemented", "grounding": {"source": "decorrelation.tex 545, 547"}, "status": "connected", "complete": true}, {"id": "t18", "from": "X_SAMP", "to": "THM", "kind": "call", "carries": [{"node": "X_SAMP", "item": "children_independent", "used_at": [550], "origin": "supplemented"}, {"node": "X_SAMP", "item": "leaf_removal", "used_at": [553, 555], "origin": "supplemented"}], "origin": "supplemented", "grounding": {"source": "decorrelation.tex 550, 553, 555"}, "status": "connected", "complete": true}]
```

## 3. 보내는 edge (이 vertex에서 나가는 것 전부). 싣는 항목의 진술은 1절에 있다

```json
[{"id": "t22", "from": "THM", "to": "OUT", "kind": "flow", "carries": [{"node": "THM", "item": "main", "used_at": ["comparison.tex 153"], "origin": "machine"}], "origin": "machine", "grounding": {"source": "comparison.tex 153"}, "status": "connected", "complete": true}]
```

## 4. 기호 표의 해당 항목

```json
[{"id": "R_S", "tex": "$R_S$", "defined_at": "trees.tex 42–46; decorrelation.tex 60–61, 90", "text": "spin replica leaf 부분집합 $S$ 의 multioverlap $R_S=\\frac1N\\sum_{i}\\prod_{a\\in S}\\sigma_i^a$, $R_\\varnothing=1$. 수 5에서는 표본 leaf에 대해 $R_S=\\mathbf 1\\cdot A_S$."}, {"id": "A_avg", "tex": "$\\mathcal A_{L,\\eta}$", "defined_at": "decorrelation.tex 30–38", "text": "$a$ 개 깊이 좌표 위의 음 아닌 배열 $z$ 에 대해 $\\mathcal A_{L,\\eta}z=L^{-a}\\sum_{\\mathbf q\\ \\eta\\text{-regular}}z(\\mathbf q)$. 추가 순서 제한(예: $d<\\min_vq_v$)은 합의 범위에 넣는다. 정규화하지 않은 평균이라 총질량 $\\le1$."}, {"id": "b_S", "tex": "$b(S)$", "defined_at": "decorrelation.tex 20–21", "text": "topology $S$ 의 branching vertex 수."}, {"id": "topology", "tex": "topology $S$", "defined_at": "decorrelation.tex 18–20", "text": "labeled leaf를 갖는 유한 rooted tree에서 unary vertex를 지운 것. 각 branching vertex에 $\\{0,\\ldots,L-1\\}$ 의 정수 깊이를 주며, 깊이는 모든 가지를 따라 엄격히 증가한다."}, {"id": "V_kL", "tex": "$V_{k,L}(\\eta)$", "defined_at": "decorrelation.tex 253–257", "text": "$V_{k,L}(\\eta)=\\max_{1\\le|S|\\le k}\\limsup_{N}\\mathcal A_{L,\\eta}v_N(S,d)$. 최대는 유한 개 labeled topology 위."}, {"id": "a_p", "tex": "$a_{S,e}$, $p_N(S,e)$", "defined_at": "decorrelation.tex 208–215", "text": "$S$ 가 깊이 $e$ 에서 처음 proper child shape $T_1,\\ldots,T_s$ 로 갈라질 때 $a_{S,e}=\\prod_j\\mu_{e,T_j}$ (좌표별 곱), $p_N(S,e)=\\sum_jv_N(T_j,e)^{1/4}$."}, {"id": "mu", "tex": "$\\mu_{d,S}$", "defined_at": "decorrelation.tex 97–98", "text": "$\\mu_{d,S}=\\mathbb E[A_S\\mid\\mathscr F_d]$."}, {"id": "F_d", "tex": "$\\mathscr F_d$", "defined_at": "decorrelation.tex 94–95", "text": "처음 stem 위의 깊이 $d$ (첫 branching 깊이 포함)에서 root와 깊이 $d$ 까지의 표본 prefix가 생성하는 sigma field."}, {"id": "kappa", "tex": "$\\kappa(T)$", "defined_at": "trees.tex 346–354", "text": "reference 계수 $\\kappa(S)=\\prod_{v\\in\\operatorname{Br}(S)}\\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$; $a_v$, $d_v$ 는 처방한 reference tree에서 vertex의 자식 수와 깊이."}, {"id": "anchor", "tex": "spin / marker anchor, $\\mathcal C$, $R_E$", "defined_at": "perturbations.tex 427–450", "text": "$S_0=\\sigma_i$ 이면 spin anchor, $S_0=1$ 이면 marker anchor. $\\mathcal C$ 는 추가 color와 anchor만의 쌍별 split 깊이를 처방한다. $R_E$ 는 history가 고른 새 replica(spin anchor이면 anchor 포함)의 multioverlap."}, {"id": "ext_hist", "tex": "$E$, $c_E$, $\\mathfrak E(\\mathcal T,a_*,\\mathcal C)$", "defined_at": "trees.tex 259–276; perturbations.tex 427–440", "text": "extension history와 그 계수(선택한 계수들의 곱), 제약 $\\mathcal C$ 를 지키는 허용 history의 모음."}, {"id": "delta", "tex": "$\\delta$", "defined_at": "decorrelation.tex 4", "text": "$\\delta=L^{-1}$."}, {"id": "N_lim", "tex": "$N\\to\\infty$", "defined_at": "decorrelation.tex 4–8", "text": "각 고정 $L$ 에서 $N$ 의 극한은 모두 Lemma pert:selection 이 주는 크기와 매개변수 선택을 따라 취한다. 그 선택은 Theorem pert:tree-identity 의 항등식을 만족한다. $L$ 마다 다른 수열을 써도 된다. (선택 자체는 perturbations.tex 255–268)"}, {"id": "E_root", "tex": "$\\mathbb E$", "defined_at": "trees.tex 47–48", "text": "따로 적지 않은 기대값 $\\mathbb E$ 는 root와 해당 tree의 표본추출을 포함한다."}, {"id": "eta_regular", "tex": "$\\eta$-regular", "defined_at": "decorrelation.tex 21–28", "text": "모든 배정 깊이$/L$ 이 $(\\eta,1-\\eta)$ 안에 있고 서로 다른 branching vertex의 정규화 깊이가 $\\eta$ 보다 더 떨어진 배정. prefix 깊이 $d$ 가 추가로 지정되면 모든 branching 깊이에 대해 같은 제한을 지킨다. 한 topology의 두 사본이 aligned 깊이를 쓰면 대응 vertex는 깊이 좌표 하나를 공유하고, regularity는 서로 다른 좌표들에 건다."}]
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

## 6. 항목 사전 (받는 edge가 싣는 남의 출력 항목, 하나에 한 번)

```json
{"PB.projection": {"statement": "$e$ 의 prefix가 주어졌을 때 $S$ 의 연속과 독립인 $B\\in[-1,1]^N$ 에 대해 $\\|(A_S-a_{S,e})\\cdot B\\|_{L^2}\\le p_N(S,e)$.", "lines": [216, 225], "source": "decorrelation.tex 208–230"}, "PB.product_mean": {"statement": "$S$ 가 깊이 $e$ 에서 처음 proper child shape $T_1,\\ldots,T_s$ 로 갈라지면 자식의 조건부 독립으로 $\\mu_{e,S}=\\prod_j\\mu_{e,T_j}$.", "lines": [208, 210], "source": "decorrelation.tex 208–230"}, "DC.martingale_energy": {"statement": "$T$ 의 나중 branching 깊이를 고정하고 처음 stem을 따라 path 하나를 뽑으면 $\\mu_{t,T}$ 는 유계 vector martingale이고 $\\sum_t\\mathbb E\\|\\mu_{t+1,T}-\\mu_{t,T}\\|_N^2\\le1$. (증명 블록 안의 식을 밖에서 참조)", "lines": [169, 175], "source": "decorrelation.tex 142–206"}, "CC.fiber_bound": {"statement": "깊이 좌표 $D$ 개의 평균 안에서 어떤 항이 좌표 $D_j$ 개만 쓰고, 남는 배정마다 원상이 많아야 $L^{D-D_j}$ 개이며 그 좌표가 큰 $L$ 에서 $\\eta/2$-regular 이면, $0<\\gamma\\le1$ 에 대해 $L^{-D}\\sum_{\\mathbf q\\ \\eta\\text{-reg}}w_j(\\pi_j(\\mathbf q))^\\gamma\\le\\bigl(L^{-D_j}\\sum_{\\mathbf y\\ \\eta/2\\text{-reg}}w_j(\\mathbf y)\\bigr)^\\gamma$. shift하지 않은 항은 좌표를 옮기지 않고 같은 경계.", "lines": [491, 509], "source": "decorrelation.tex 234–524"}, "CC.V_to_zero": {"statement": "모든 고정 $k,\\eta$ 에서 $V_{k,L}(\\eta)\\to0$ ($L\\to\\infty$).", "lines": [522, 523], "source": "decorrelation.tex 234–524"}, "CC.main": {"statement": "모든 고정 labeled topology $S$ 와 $\\eta>0$ 에서 $\\lim_{L\\to\\infty}\\limsup_{N\\to\\infty}\\mathcal A_{L,\\eta}v_N(S,d)=0$. 평균은 $S$ 의 모든 branching 깊이와 첫 split보다 엄격히 앞선 regular 깊이 $d$ 에 대해서. singleton이면 $d$ 만.", "lines": [236, 244], "source": "decorrelation.tex 234–524"}, "X_TI.identity": {"statement": "섭동족과 Lemma pert:selection 의 모든 수열을 따라 $\\sum_{E\\in\\mathfrak E(\\mathcal T,a_*,\\mathcal C)}c_E\\mathbb E[fR_E]-\\mathbb Ef\\sum_{E\\in\\mathfrak E(\\{a_*\\},a_*,\\mathcal C)}c_E\\mathbb E[R_E]\\to0$. 모든 고정 old tree, 두 종류의 anchor, multioverlap의 모든 유계 다항식 $f$, 유한 개의 순서 있는 추가 color, 모든 처방 제약 $\\mathcal C$ 에서 성립. 빈 추가도 허용. 오차는 고정 $L$, tree, 제약에서 $L$ 의 극한 전에 0으로 간다.", "lines": [452, 470], "source": "perturbations.tex 427–470"}, "X_TI.anchor_constraint": {"statement": "$S_0=\\sigma_i$ 이면 spin anchor, $S_0=1$ 이면 marker anchor. 추가 color $1..k$ 는 anchor가 아닌 서로 다른 replica 자리를 차지한다. $\\mathcal C$ 는 추가 color와 anchor만의 쌍별 split 깊이의 일관된 모음을 처방하고 다른 old replica에는 제한을 걸지 않는다. $R_E$ 는 spin anchor이면 $\\frac1N\\sum_i\\sigma_i^{a_*}\\prod_j\\sigma_i^{a_j(E)}$, marker anchor이면 $\\frac1N\\sum_i\\prod_j\\sigma_i^{a_j(E)}$.", "lines": [427, 450], "source": "perturbations.tex 427–470"}, "X_RT.kappa_total": {"statement": "anchor와 color들이 처방한 tree $S$ 를 이루어야 하면, 임의 old tree의 모든 호환 extension 위의 계수 총합은 $\\kappa(S)$. 같은 한 걸음 규칙은 이미 만든 reference 집합에서 시작해 반복할 수 있다.", "lines": [346, 356], "source": "trees.tex 337–356"}, "X_SAMP.children_independent": {"statement": "각 vertex에서 서로 다른 자식은 해당 kernel로 독립으로 뽑는다. $E_{\\mathcal T}$ 는 root가 주어진 표본 기대값.", "lines": [28, 34], "source": "trees.tex 28–39, 47–48"}, "X_SAMP.leaf_removal": {"statement": "leaf 몇 개와 남은 leaf가 쓰지 않는 path 부분을 지우면 남은 tree의 표본 법칙이 보존된다.", "lines": [38, 39], "source": "trees.tex 28–39, 47–48"}}
```

## 7. 이 범위의 카드 (redesign/cards 의 앞머리 일부: id, 제목, math(번역), 원문 줄, uses, children)

```json
[{"id": "decor:overlap-concentration", "title": "모든 multioverlap의 깊이 평균 집중", "math": "모든 고정 labeled topology $S$에 대해\n$$\\lim_{L\\to\\infty}\\limsup_{N\\to\\infty}\\mathcal A_{L,\\eta}\\operatorname{Var}(R_S)=0\\qquad(\\eta>0),$$\n여기서 $\\mathcal A_{L,\\eta}$는 $S$의 $b(S)$개 branching depth만을 $\\eta$-regular 배정에 대해 평균하고, $N$ 극한은 x:decor-limit-order의 수열을 따른다. singleton이면 (평균에 좌표가 없고) 각 고정 $L$에서 $\\operatorname{Var}(R_S)\\to0$ ($N\\to\\infty$).", "uses": "[x:decor-topology, x:decor-eta-regular, decor:average-definition, x:decor-spin-product, x:decor-limit-order, x:decor-mesh, pert:tree-identity, tree:reference-total, decor:projection-bound, decor:depth-continuity, decor:conditional-concentration, decor:identity-error]", "children": "[decor:overlap-concentration.s1, decor:overlap-concentration.s2, decor:overlap-concentration.s3, decor:overlap-concentration.s4, decor:overlap-concentration.s5]", "source_lines": [[63, 83], [526, 530], [532, 611]]}, {"id": "decor:overlap-concentration.s1", "title": "singleton: 추가 color 없는 spin anchor", "math": "singleton $S$에서 old tree를 $S$ 자신, spin anchor를 그 leaf, added color 없음, $f=R_S$로 둔 pert:tree-identity는 $\\mathbb ER_S^2-(\\mathbb ER_S)^2\\to0$, 즉 각 고정 $L$에서 $\\operatorname{Var}(R_S)\\to0$을 준다.", "uses": "[pert:tree-identity, x:pert-colored-extensions, x:decor-spin-product]", "children": "[]", "source_lines": [[532, 536]]}, {"id": "decor:overlap-concentration.s2", "title": "marker anchor로 prefix 사영 $M$을 집중시키기", "math": "$|S|\\ge2$, 첫 갈라짐 $e$, $M=\\mathbb E[R_S\\mid\\mathscr F_{e-1}]$이라 하면 각 고정 $L$, $S$, 깊이 배정에서 $\\operatorname{Var}(M)\\to0$ ($N\\to\\infty$).", "uses": "[pert:tree-identity, tree:reference-total, x:decor-tree-sampling, x:decor-mesh]", "children": "[decor:overlap-concentration.s2.s1, decor:overlap-concentration.s2.s2]", "source_lines": [[537, 570]]}, {"id": "decor:overlap-concentration.s2.s1", "title": "marker anchor 구성과 계수 $C(S,e)$", "math": "old tree는 $S$의 sampled copy, 그 leaf 하나가 marker anchor다. added color $k=|S|$개가 $S$의 사본 하나를 이루고 그 모든 leaf가 anchor와 깊이 $e-1$에서 갈라진다는 제약을 둔다. 그러면 첫 target 경로는 깊이 $e-1$에서 fresh여야 하고(old tree는 거기서 아직 갈라지지 않았고 옛 leaf들은 anchor와 깊이 $e$까지 prefix를 공유하므로 쓸 수 없다), 나머지 target 경로는 그렇게 생긴 fresh 부분 tree 안에 놓인다. 확장 계수의 총합은 old tree 쪽과 anchor 혼자인 쪽 모두\n$$C(S,e)=-\\delta\\,\\kappa(S)\\ne0.$$", "uses": "[pert:tree-identity, x:pert-colored-extensions, tree:reference-total, x:decor-mesh, x:decor-topology]", "children": "[]", "source_lines": [[537, 549]]}, {"id": "decor:overlap-concentration.s2.s2", "title": "$C(S,e)\\operatorname{Var}(M)=o_N(1)$", "math": "target 사본과 old 사본은 $\\mathscr F_{e-1}$가 주어지면 조건부 독립이고 같은 조건부 법칙을 가진다. $f=R_S$ (old), $M=\\mathbb E[R_S\\mid\\mathscr F_{e-1}]$이면 old 쪽 각 항은 $\\mathbb E[fR_E]=\\mathbb EM^2$이다. anchor 혼자인 쪽은 marker의 $e-1$ 아래 continuation을 지우면 보통의 target 법칙 $S$가 남아 평균이 $\\mathbb ER_S$이다. 따라서\n$$C(S,e)\\bigl(\\mathbb EM^2-(\\mathbb ER_S)^2\\bigr)=C(S,e)\\operatorname{Var}(M)=o_N(1),$$\n그리고 고정 $L$에서 $C(S,e)\\ne0$으로 나누어 $\\operatorname{Var}(M)\\to0$ (각 고정 $L,S,e$). $L\\to\\infty$에서 균등한 하계는 필요 없다.", "uses": "[decor:overlap-concentration.s2.s1, pert:tree-identity, x:decor-tree-sampling]", "children": "[]", "source_lines": [[550, 570]]}, {"id": "decor:overlap-concentration.s3", "title": "prefix 아래의 조건부 분산: $G$와 $G_-$", "math": "$|S|=k\\ge2$, 첫 갈라짐 $e$, 자식 $T_1,\\ldots,T_s$에 대해 $G=\\mathbf1\\cdot\\prod_j\\mu_{e,T_j}$, $G_-=\\mathbf1\\cdot\\prod_j\\mu_{e-1,T_j}$로 둔다. $G_-$는 $\\mathscr F_{e-1}$-가측이고, decor:projection-bound ($B=\\mathbf1$)에서 $\\mathbb E(R_S-G)^2\\le p_N(S,e)^2$이다. 자식 깊이를 고정하고 곱 차이 부등식과 martingale energy를 쓰면 $L$이 클 때\n$$\\mathcal A_{L,\\eta}\\,\\mathbb E(G-G_-)^2\\le C_k/L.$$", "uses": "[decor:projection-bound, decor:projection-definition, decor:depth-continuity, decor:depth-continuity.s1, x:decor-product-difference, decor:average-definition]", "children": "[]", "source_lines": [[571, 590]]}, {"id": "decor:overlap-concentration.s4", "title": "분산 추정 $\\limsup_N\\mathcal A\\operatorname{Var}(R_S)\\le C_k(L^{-1}+V_{k-1,L}^{1/2})$", "math": "조건부 기대값이 최적 $L^2$ 사영이므로 $\\mathbb E(R_S-M)^2\\le\\mathbb E(R_S-G_-)^2\\le2p_N(S,e)^2+2\\mathbb E(G-G_-)^2$이다. 분산 분해 $\\operatorname{Var}(R_S)=\\mathbb E(R_S-M)^2+\\operatorname{Var}(M)$와 s2, s3, 그리고 고정 $L$에서 유한 합인 $\\mathcal A_{L,\\eta}$와 $\\limsup_N$의 교환(decor:identity-error: 각 고정 배정에서 $\\operatorname{Var}(M)\\to0$이므로 $\\limsup_N\\mathcal A_{L,\\eta}\\operatorname{Var}(M)=0$)에서, $L$이 충분히 크면\n$$\\limsup_{N\\to\\infty}\\mathcal A_{L,\\eta}\\operatorname{Var}(R_S)\\le C_k\\bigl(L^{-1}+V_{k-1,L}(\\eta/2)^{1/2}\\bigr).$$\n여기서 $p_N(S,e)^2\\le s\\sum_jv_N(T_j,e)^{1/2}$와 fiber bound(conditional-concentration.s7.s3)를 $\\gamma=1/2$로 쓴다. 이번에는 $d$가 없으므로 전체 평균은 $D=b(S)$개 좌표, 자식 항은 여전히 $D_j=b(T_j)+1$개 좌표를 쓴다.", "uses": "[decor:overlap-concentration.s2, decor:overlap-concentration.s3, decor:conditional-concentration.s1, decor:conditional-concentration.s7.s3, decor:conditional-concentration, x:decor-average-comparisons, decor:average-holder, decor:identity-error]", "children": "[]", "source_lines": [[591, 609]]}, {"id": "decor:overlap-concentration.s5", "title": "마무리: conditional-concentration 적용", "math": "decor:conditional-concentration (s1의 동치 형태)에서 $\\lim_{L\\to\\infty}V_{k-1,L}(\\eta/2)=0$이므로 s4의 우변이 $L\\to\\infty$에서 0으로 가고 정리가 증명된다.", "uses": "[decor:overlap-concentration.s4, decor:conditional-concentration]", "children": "[]", "source_lines": [[609, 611]]}]
```
