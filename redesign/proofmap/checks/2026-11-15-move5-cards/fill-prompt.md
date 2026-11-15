도구를 하나도 쓰지 마. 아래 자료만 보고 답으로 ```json 코드 블록 하나만 낸다(앞뒤 설명 없이).

수학 논문 한 절의 증명 지도를 짓는다. node 몇 개의 증명을 한 층 아래로 열 때, **뼈대(안쪽 걸음과 그 사이의 의존)는 이미 기존 카드에서 기계로 만들었다.** 너는 뼈대를 다시 쓰지 않는다. 원문을 읽고 다음 셋만 쓴다.

1. `edge_used_at`: 뼈대의 edge마다 받는 걸음의 원문에서 그 의존이 실제로 쓰이는 줄. 원문에서 쓰임을 찾지 못하면 `null` 과 짧은 이유.
2. `missing`: 원문의 걸음이 쓰는데 뼈대 edge에 없는 의존. 받는 쪽 걸음 id, 무엇, 원문 줄, 어디서 오는지(`from`: 같은 뼈대의 걸음 id, 아래 '받을 수 있는 항목'의 `NODE.item`, `floor:이름`(초등적 사실), 또는 `모름`).
3. `author_filled`: 원문이 적지 않았는데 그 걸음이 서려면 필요한 것(한 줄씩, 필요하면 식).
4. `mismatch`: 카드의 경계(줄 범위)가 원문 문단·논리와 맞지 않는 곳, 뼈대 edge가 원문과 다른 곳.

진술을 옮겨 적지 않는다. 화면이 원문 줄과 카드 번역을 그 자리에 펼친다.

답의 꼴:
```json
{"<NODE>": {"edge_used_at": [{"from": "...", "to": "...", "lines": [..] , "note": null}],
            "missing": [{"to": "k2", "what": "...", "lines": [..], "from": "..."}],
            "author_filled": [{"at": "k3", "what": "..."}],
            "mismatch": [{"card": "...", "issue": "..."}]},
 "...": {}}
```


---

# AVG: 깊이 평균과 그 두 비교

뼈대 (x_<NODE> 는 위 graph의 그 node에서 오는 입력):
```json
{"inner": [{"id": "k1", "card": "decor:average-definition", "title": "깊이 평균 $\\mathcal A_{L,\\eta}$", "lines": [30, 38]}, {"id": "k2", "card": "decor:average-holder", "title": "깊이 평균의 분수 거듭제곱 부등식", "lines": [36, 43]}, {"id": "k3", "card": "x:decor-average-comparisons", "title": "깊이 평균의 두 기본 비교 (안 쓰는 좌표, 정수 이동)", "lines": [44, 47]}], "edges": [{"from": "k1", "to": "k2"}, {"from": "k1", "to": "k3"}], "symbols_from_cards": ["eta_regular"], "floor_from_cards": []}
```
받을 수 있는 항목 (이 node로 들어오는 입력 전부):
```json
{}
```
원문 (decorrelation.tex):
```tex
  30  For a nonnegative array $z(\mathbf q)$ on $a$ depth coordinates, put
  31  \begin{equation}
  32   \mathcal A_{L,\eta}z
  33     =L^{-a}\sum_{\mathbf q\;\eta\text{-regular}}z(\mathbf q).
  34   \label{decor:average-definition}
  35  \end{equation}
  36  Additional ordering restrictions, such as $d<\min_v q_v$, are included
  37  in the summation domain.  These are unnormalized averages: their total
  38  mass is at most one.  Consequently, for $0<\gamma\le1$,
  39  \begin{equation}
  40   \mathcal A_{L,\eta}(z^\gamma)
  41         \le (\mathcal A_{L,\eta}z)^\gamma.
  42   \label{decor:average-holder}
  43  \end{equation}
  44  Two elementary comparisons will recur. Summing over an unused coordinate
  45  costs at most $L$, canceled by its normalization. A fixed integer shift of
  46  any subset of the coordinates maps $\eta$-regular assignments injectively
  47  into $\eta/2$-regular assignments for all sufficiently large $L$.
```

---

# DC: Lemma: 깊이에 대한 평균 연속성

뼈대 (x_<NODE> 는 위 graph의 그 node에서 오는 입력):
```json
{"inner": [{"id": "k1", "card": "decor:depth-continuity.s1", "title": "martingale energy와 평가 깊이 연속성", "lines": [168, 177]}, {"id": "k2", "card": "decor:depth-continuity.s2", "title": "갈라짐 하나를 한 칸 늦추는 효과", "lines": [178, 193]}, {"id": "k3", "card": "decor:depth-continuity.s3", "title": "이동 하나의 비용 $C/L$", "lines": [194, 199]}, {"id": "k4", "card": "decor:depth-continuity.s4", "title": "여러 이동과 더 큰 tree", "lines": [199, 206]}], "edges": [{"from": "x_AVG", "to": "k1"}, {"from": "k1", "to": "k2"}, {"from": "x_X_SAMP", "to": "k2"}, {"from": "k1", "to": "k3"}, {"from": "k2", "to": "k3"}, {"from": "x_AVG", "to": "k3"}, {"from": "k3", "to": "k4"}, {"from": "x_AVG", "to": "k4"}, {"from": "x_X_SAMP", "to": "k4"}], "symbols_from_cards": ["F_d", "b_S", "eta_regular", "mu", "topology", "v_N"], "floor_from_cards": ["곱 차이 부등식"]}
```
받을 수 있는 항목 (이 node로 들어오는 입력 전부):
```json
{"AVG.shift_regular": "좌표의 임의 부분집합을 고정 정수만큼 옮기면, 충분히 큰 $L$ 에서 $\\eta$-regular 배정이 $\\eta/2$-regular 배정으로 단사로 간다.", "X_SAMP.leaf_removal": "leaf 몇 개와 남은 leaf가 쓰지 않는 path 부분을 지우면 남은 tree의 표본 법칙이 보존된다."}
```
원문 (decorrelation.tex):
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

---

# PB: 자식을 평균으로 바꾸는 사영

뼈대 (x_<NODE> 는 위 graph의 그 node에서 오는 입력):
```json
{"inner": [{"id": "k1", "card": "decor:projection-definition", "title": "첫 갈라짐에서의 사영 $a_{S,e}$와 오차량 $p_N(S,e)$", "lines": [208, 215]}, {"id": "k2", "card": "decor:projection-bound", "title": "첫 갈라짐에서 자식을 평균으로 바꾸는 오차", "lines": [216, 230]}], "edges": [{"from": "x_X_SAMP", "to": "k1"}, {"from": "k1", "to": "k2"}, {"from": "x_CON", "to": "k2"}, {"from": "x_X_SAMP", "to": "k2"}], "symbols_from_cards": ["A_S", "F_d", "R_S", "b_S", "eta_regular", "mu", "topology", "v_N"], "floor_from_cards": []}
```
받을 수 있는 항목 (이 node로 들어오는 입력 전부):
```json
{"CON.contraction": "random vector $B\\in[-1,1]^N$ 이 $\\mathscr F_d$ 가 주어졌을 때 $A_S$ 와 조건부 독립이면 $\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}$.", "X_SAMP.children_independent": "각 vertex에서 서로 다른 자식은 해당 kernel로 독립으로 뽑는다. $E_{\\mathcal T}$ 는 root가 주어진 표본 기대값."}
```
원문 (decorrelation.tex):
```tex
 208  Suppose now that $S$ first branches at depth $e$ into proper child shapes
 209  $T_1,\ldots,T_s$. Conditional independence of the children gives
 210  $\mu_{e,S}=\prod_j\mu_{e,T_j}$. Write
 211  \begin{equation}
 212   a_{S,e}=\prod_{j=1}^s \mu_{e,T_j},
 213   \qquad p_N(S,e)=\sum_{j=1}^s v_N(T_j,e)^{1/4}.
 214   \label{decor:projection-definition}
 215  \end{equation}
 216  For any vector $B\in[-1,1]^N$ independent of the continuation of $S$
 217  given its prefix at $e$, successive replacement of the children,
 218  using \eqref{decor:contraction-bound}, gives
 219  \begin{equation}
 220   \|(A_S-a_{S,e})\cdot B\|_{L^2}\le p_N(S,e).
 221   \label{decor:projection-bound}
 222  \end{equation}
 223  At each replacement the other child vectors and the already replaced
 224  means form a bounded multiplier independent of the child being
 225  replaced, conditionally on $\mathscr F_e$.  In particular this applies
 226  to $B=\mathbf1$, and to a vector sampled on another side separated
 227  before $e$.  For two such sides, both can be projected with total
 228  $L^2$ error at most $2p_N(S,e)$.  Multiplication of the contracted
 229  error by any scalar test $f$ with $|f|\le1$, even a correlated one,
 230  does not increase its $L^1$ bound.
```

---

# THM: Theorem: 모든 multioverlap의 집중

뼈대 (x_<NODE> 는 위 graph의 그 node에서 오는 입력):
```json
{"inner": [{"id": "k1", "card": "decor:overlap-concentration.s1", "title": "singleton: 추가 color 없는 spin anchor", "lines": [532, 536]}, {"id": "k2", "card": "decor:overlap-concentration.s2.s1", "title": "marker anchor 구성과 계수 $C(S,e)$", "lines": [537, 549]}, {"id": "k3", "card": "decor:overlap-concentration.s2.s2", "title": "$C(S,e)\\operatorname{Var}(M)=o_N(1)$", "lines": [550, 570]}, {"id": "k4", "card": "decor:overlap-concentration.s3", "title": "prefix 아래의 조건부 분산: $G$와 $G_-$", "lines": [571, 590]}, {"id": "k5", "card": "decor:overlap-concentration.s4", "title": "분산 추정 $\\limsup_N\\mathcal A\\operatorname{Var}(R_S)\\le C_k(L^{-1}+V_{k-1,L}^{1/2})$", "lines": [591, 609]}, {"id": "k6", "card": "decor:overlap-concentration.s5", "title": "마무리: conditional-concentration 적용", "lines": [609, 611]}], "edges": [{"from": "x_X_TI", "to": "k1"}, {"from": "x_X_TI", "to": "k1"}, {"from": "x_X_TI", "to": "k2"}, {"from": "x_X_TI", "to": "k2"}, {"from": "x_X_RT", "to": "k2"}, {"from": "k2", "to": "k3"}, {"from": "x_X_TI", "to": "k3"}, {"from": "x_X_SAMP", "to": "k3"}, {"from": "x_PB", "to": "k4"}, {"from": "x_DC", "to": "k4"}, {"from": "x_DC", "to": "k4"}, {"from": "x_AVG", "to": "k4"}, {"from": "k3", "to": "k5"}, {"from": "k4", "to": "k5"}, {"from": "x_CC", "to": "k5"}, {"from": "x_CC", "to": "k5"}, {"from": "x_CC", "to": "k5"}, {"from": "x_AVG", "to": "k5"}, {"from": "x_AVG", "to": "k5"}, {"from": "x_IDE", "to": "k5"}, {"from": "k5", "to": "k6"}, {"from": "x_CC", "to": "k6"}], "symbols_from_cards": ["A_S", "R_S", "a_p", "b_S", "delta", "m_d", "topology"], "floor_from_cards": ["곱 차이 부등식"]}
```
받을 수 있는 항목 (이 node로 들어오는 입력 전부):
```json
{"PB.projection": "$e$ 의 prefix가 주어졌을 때 $S$ 의 연속과 독립인 $B\\in[-1,1]^N$ 에 대해 $\\|(A_S-a_{S,e})\\cdot B\\|_{L^2}\\le p_N(S,e)$.", "PB.product_mean": "$S$ 가 깊이 $e$ 에서 처음 proper child shape $T_1,\\ldots,T_s$ 로 갈라지면 자식의 조건부 독립으로 $\\mu_{e,S}=\\prod_j\\mu_{e,T_j}$.", "DC.martingale_energy": "$T$ 의 나중 branching 깊이를 고정하고 처음 stem을 따라 path 하나를 뽑으면 $\\mu_{t,T}$ 는 유계 vector martingale이고 $\\sum_t\\mathbb E\\|\\mu_{t+1,T}-\\mu_{t,T}\\|_N^2\\le1$. (증명 블록 안의 식을 밖에서 참조)", "CC.fiber_bound": "깊이 좌표 $D$ 개의 평균 안에서 어떤 항이 좌표 $D_j$ 개만 쓰고, 남는 배정마다 원상이 많아야 $L^{D-D_j}$ 개이며 그 좌표가 큰 $L$ 에서 $\\eta/2$-regular 이면, $0<\\gamma\\le1$ 에 대해 $L^{-D}\\sum_{\\mathbf q\\ \\eta\\text{-reg}}w_j(\\pi_j(\\mathbf q))^\\gamma\\le\\bigl(L^{-D_j}\\sum_{\\mathbf y\\ \\eta/2\\text{-reg}}w_j(\\mathbf y)\\bigr)^\\gamma$. shift하지 않은 항은 좌표를 옮기지 않고 같은 경계.", "CC.V_to_zero": "모든 고정 $k,\\eta$ 에서 $V_{k,L}(\\eta)\\to0$ ($L\\to\\infty$).", "CC.main": "모든 고정 labeled topology $S$ 와 $\\eta>0$ 에서 $\\lim_{L\\to\\infty}\\limsup_{N\\to\\infty}\\mathcal A_{L,\\eta}v_N(S,d)=0$. 평균은 $S$ 의 모든 branching 깊이와 첫 split보다 엄격히 앞선 regular 깊이 $d$ 에 대해서. singleton이면 $d$ 만.", "X_TI.identity": "섭동족과 Lemma pert:selection 의 모든 수열을 따라 $\\sum_{E\\in\\mathfrak E(\\mathcal T,a_*,\\mathcal C)}c_E\\mathbb E[fR_E]-\\mathbb Ef\\sum_{E\\in\\mathfrak E(\\{a_*\\},a_*,\\mathcal C)}c_E\\mathbb E[R_E]\\to0$. 모든 고정 old tree, 두 종류의 anchor, multioverlap의 모든 유계 다항식 $f$, 유한 개의 순서 있는 추가 color, 모든 처방 제약 $\\mathcal C$ 에서 성립. 빈 추가도 허용. 오차는 고정 $L$, tree, 제약에서 $L$ 의 극한 전에 0으로 간다.", "X_TI.anchor_constraint": "$S_0=\\sigma_i$ 이면 spin anchor, $S_0=1$ 이면 marker anchor. 추가 color $1..k$ 는 anchor가 아닌 서로 다른 replica 자리를 차지한다. $\\mathcal C$ 는 추가 color와 anchor만의 쌍별 split 깊이의 일관된 모음을 처방하고 다른 old replica에는 제한을 걸지 않는다. $R_E$ 는 spin anchor이면 $\\frac1N\\sum_i\\sigma_i^{a_*}\\prod_j\\sigma_i^{a_j(E)}$, marker anchor이면 $\\frac1N\\sum_i\\prod_j\\sigma_i^{a_j(E)}$.", "X_TI.empty_addition": "$k=0$ 이면 $R_E$ 는 spin anchor에서 $R_{\\{a_*\\}}$, marker anchor에서 $1$ 이다(449). 빈 추가도 허용한다(468).", "X_RT.kappa_total": "anchor와 color들이 처방한 tree $S$ 를 이루어야 하면, 임의 old tree의 모든 호환 extension 위의 계수 총합은 $\\kappa(S)$. 같은 한 걸음 규칙은 이미 만든 reference 집합에서 시작해 반복할 수 있다.", "X_SAMP.children_independent": "각 vertex에서 서로 다른 자식은 해당 kernel로 독립으로 뽑는다. $E_{\\mathcal T}$ 는 root가 주어진 표본 기대값.", "X_SAMP.leaf_removal": "leaf 몇 개와 남은 leaf가 쓰지 않는 path 부분을 지우면 남은 tree의 표본 법칙이 보존된다.", "X_EXT.rule": "anchor leaf $a_*$ 를 가진 tree $\\mathcal T$ 에서 color $1..k$ 를 차례로 배정한다. 다음 color는 (i) $a_*$ 가 아닌 안 쓴 old leaf (계수 $1$) 또는 (ii) 현재 tree의 내부 vertex $\\beta$ 에서 fresh path (계수 $\\gamma_\\beta=m_{d_\\beta}-n_\\beta m_{d_\\beta+1}$). 현재 tree는 안 쓴 것을 포함한 모든 old path와 이미 붙인 path. $c_E$ 는 계수들의 곱, $\\mathcal T_E$ 는 마지막 tree.", "X_EXT.empty_weight": "빈 extension의 무게는 $1$ 이다. (trees.tex 295, Lemma tree:extension-expansion 의 문장)"}
```
원문 (decorrelation.tex):
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
