# 대조 과제

수학 논문 한 lemma의 증명을 두 사람이 각각 작은 graph(node = 증명의 걸음, edge = 넘기는 내용)로 옮겼다. 판 A와 판 B다. 너는 둘을 **원문과 대조**한다. 이 파일 밖의 것은 쓰지 않는다.

센 것을 아래 JSON 하나로만 답한다(앞뒤 설명 없이).

```json
{"A": {"misstatements": [{"where": "node 또는 edge id", "what": "원문과 어긋난 내용", "lines": "원문 줄"}],
        "missed_dependencies": [{"what": "증명이 쓰는데 graph의 어떤 node·edge에도 없는 것", "lines": "원문 줄"}],
        "unsupported_additions": [{"where": "...", "what": "원문에 없고 author_filled 표시도 없는 주장"}]},
 "B": {...같은 꼴...},
 "notes": "판단이 갈린 곳만 짧게"}
```

정의:
- **misstatement**: node·edge의 진술이나 유도 줄이 원문과 수학적으로 다르다(조건 빠짐, 부등호·지수·상수 틀림, 대상 바뀜). 표기 차이·번역 문체는 세지 않는다.
- **missed dependency**: 원문 증명이 쓰는 사실·가정·정의 가운데 그 판의 어느 node·edge에도 나타나지 않는 것.
- **unsupported addition**: 원문에 없는 주장인데 `author_filled` 표시가 없는 것. 표시가 있으면 세지 않는다.

## 원문 (decorrelation.tex)

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

## 판 A

```json
{
 "nodes": [
  {
   "id": "external_none",
   "kind": "external",
   "title": "받는 edge 없음",
   "grounding": {
    "source": "decorrelation.tex 127–140",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "c1",
   "kind": "step",
   "title": "조건부 제곱 기대값을 $C$ 와 $B$ 로 쓴다",
   "statement": "$\\mathscr F_d$ 와 $B$ 가 주어졌을 때 $\\mathbb E[((A_S-\\mu_{d,S})\\cdot B)^2\\mid\\mathscr F_d,B]=N^{-2}\\sum_{i,j}C_{ij}B_iB_j$. 여기서 $C_{ij}=\\operatorname{Cov}(A_{S,i},A_{S,j}\\mid\\mathscr F_d)$.",
   "local_symbols": [
    {
     "id": "C_d",
     "tex": "$C_{ij}$ (첫 주장)",
     "defined_at": "decorrelation.tex 129 (암묵)",
     "text": "첫 주장의 증명에서 $C_{ij}=\\operatorname{Cov}(A_{S,i},A_{S,j}\\mid\\mathscr F_d)$. 원문은 $C$ 를 lemma 둘째 주장(줄 118)에서만 정의하고 줄 129 에서 따로 정의 없이 다시 쓴다."
    }
   ],
   "derivation": [
    {
     "line": 1,
     "tex": "(A_S-\\mu_{d,S})\\cdot B=N^{-1}\\sum_i(A_{S,i}-\\mu_{d,S,i})B_i",
     "by": "floor: 정의 ($x\\cdot y$, 기호 A_S)"
    },
    {
     "line": 2,
     "tex": "\\mathbb E[((A_S-\\mu_{d,S})\\cdot B)^2\\mid\\mathscr F_d,B]=N^{-2}\\sum_{i,j}B_iB_j\\,\\mathbb E[(A_{S,i}-\\mu_{d,S,i})(A_{S,j}-\\mu_{d,S,j})\\mid\\mathscr F_d,B]",
     "by": "line 1; floor: $B$ 는 조건 안에서 상수"
    },
    {
     "line": 3,
     "tex": "=N^{-2}\\sum_{i,j}C_{ij}B_iB_j",
     "by": "line 2; lemma 가정(조건부 독립)으로 $B$ 를 조건에서 뺌; 기호 mu"
    }
   ],
   "author_filled": "$C$ 가 $\\mathscr F_d$ 조건부 공분산 $\\operatorname{Cov}(A_S\\mid\\mathscr F_d)$ 이라는 것, 그리고 조건부 독립 가정으로 $B$ 를 조건에서 빼는 단계를 채웠다. 원문은 결과식만 적는다.",
   "grounding": {
    "source": "decorrelation.tex 128–129",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "c2",
   "kind": "step",
   "title": "$|B_i|\\le1$ 로 누른다",
   "statement": "$\\bigl|N^{-2}\\sum_{ij}C_{ij}B_iB_j\\bigr|\\le N^{-2}\\sum_{ij}|C_{ij}|$.",
   "derivation": [
    {
     "line": 1,
     "tex": "\\bigl|N^{-2}\\sum_{ij}C_{ij}B_iB_j\\bigr|\\le N^{-2}\\sum_{ij}|C_{ij}||B_i||B_j|\\le N^{-2}\\sum_{ij}|C_{ij}|",
     "by": "edge e1; 삼각부등식; lemma 가정 $B\\in[-1,1]^N$"
    }
   ],
   "grounding": {
    "source": "decorrelation.tex 129–130",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "c3",
   "kind": "step",
   "title": "$i,j$ 에 대한 Cauchy–Schwarz",
   "statement": "$N^{-2}\\sum_{ij}|C_{ij}|\\le\\bigl(N^{-2}\\sum_{ij}C_{ij}^2\\bigr)^{1/2}$.",
   "derivation": [
    {
     "line": 1,
     "tex": "N^{-2}\\sum_{ij}|C_{ij}|\\cdot1\\le\\bigl(N^{-2}\\sum_{ij}C_{ij}^2\\bigr)^{1/2}\\bigl(N^{-2}\\sum_{ij}1\\bigr)^{1/2}=\\bigl(N^{-2}\\sum_{ij}C_{ij}^2\\bigr)^{1/2}",
     "by": "edge e2; floor: Cauchy–Schwarz ($N^2$ 개 항 위의 균등 평균)"
    }
   ],
   "grounding": {
    "source": "decorrelation.tex 130",
    "state": "proposed"
   },
   "status": "complete"
  },
  {
   "id": "c4",
   "kind": "step",
   "title": "prefix 에 대한 Cauchy–Schwarz 와 $v_N$",
   "statement": "$\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}^2\\le\\mathbb E\\bigl(N^{-2}\\sum_{ij}C_{ij}^2\\bigr)^{1/2}\\le v_N(S,d)^{1/2}$, 따라서 $\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}$.",
   "derivation": [
    {
     "line": 1,
     "tex": "\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}^2=\\mathbb E\\,\\mathbb E[((A_S-\\mu_{d,S})\\cdot B)^2\\mid\\mathscr F_d,B]",
     "by": "floor: tower 성질; 기호 E_root"
    },
    {
     "line": 2,
     "tex": "\\le\\mathbb E\\bigl(N^{-2}\\sum_{ij}C_{ij}^2\\bigr)^{1/2}",
     "by": "line 1; edge e3"
    },
    {
     "line": 3,
     "tex": "\\le\\bigl(\\mathbb E N^{-2}\\sum_{ij}C_{ij}^2\\bigr)^{1/2}=v_N(S,d)^{1/2}",
     "by": "line 2; floor: Cauchy–Schwarz (prefix 위 기대값); 기호 v_N"
    },
    {
     "line": 4,
     "tex": "\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}",
     "by": "line 3; 제곱근"
    }
   ],
   "author_filled": "바깥 기대값을 tower 성질로 붙이는 줄과 마지막 제곱근을 채웠다. 원문의 'over the prefix' 는 $\\mathscr F_d$ 를 생성하는 root·prefix 에 대한 기대값(기호 E_root)으로 읽었다.",
   "grounding": {
    "source": "decorrelation.tex 130–131",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "out_contraction",
   "kind": "output",
   "title": "축약 bound",
   "statement": "random vector $B\\in[-1,1]^N$ 이 $\\mathscr F_d$ 가 주어졌을 때 $A_S$ 와 조건부 독립이면 $\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}$.",
   "output_items": [
    "contraction"
   ],
   "grounding": {
    "source": "decorrelation.tex 110–116, 131",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "t1",
   "kind": "step",
   "title": "조건부 평균 $\\mu$ 를 둔다",
   "statement": "둘째 주장에서 $\\mu=\\mathbb E[X\\mid\\mathscr G]$ 로 둔다. $C$ 는 $X$ 의 $\\mathscr G$ 조건부 공분산 행렬이고 $Y,Z$ 도 같은 조건부 법칙을 갖는다.",
   "local_symbols": [
    {
     "id": "mu_G",
     "tex": "$\\mu$",
     "defined_at": "decorrelation.tex 132",
     "text": "$\\mu=\\mathbb E[X\\mid\\mathscr G]$. 기호 표의 $\\mu_{d,S}$ (id mu) 와 다른 것이다."
    },
    {
     "id": "C_G",
     "tex": "$C$",
     "defined_at": "decorrelation.tex 118",
     "text": "$X$ (따라서 $Y,Z$) 의 $\\mathscr G$ 조건부 공분산 행렬."
    },
    {
     "id": "XYZ",
     "tex": "$X,Y,Z$, $\\mathscr G$",
     "defined_at": "decorrelation.tex 117–118",
     "text": "sigma field $\\mathscr G$ 가 주어졌을 때 유계 random vector 의 조건부 독립 사본."
    }
   ],
   "grounding": {
    "source": "decorrelation.tex 117–118, 132",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "t2",
   "kind": "step",
   "title": "조건부 독립으로 조건부 제곱 기대값을 계산",
   "statement": "$\\mathbb E[(X\\cdot Y-X\\cdot Z)^2\\mid\\mathscr G]=\\frac2{N^2}\\operatorname{tr}\\bigl((C+\\mu\\mu^{\\mathsf T})C\\bigr)$.",
   "derivation": [
    {
     "line": 1,
     "tex": "X\\cdot Y-X\\cdot Z=N^{-1}\\sum_iX_i(Y_i-Z_i)",
     "by": "floor: 정의 ($x\\cdot y$)"
    },
    {
     "line": 2,
     "tex": "\\mathbb E[(Y-Z)(Y-Z)^{\\mathsf T}\\mid\\mathscr G,X]=2C",
     "by": "edge e5; 조건부 독립과 같은 조건부 법칙 ($\\mathbb E[Y-Z\\mid\\mathscr G,X]=0$)"
    },
    {
     "line": 3,
     "tex": "\\mathbb E[(X\\cdot Y-X\\cdot Z)^2\\mid\\mathscr G,X]=\\frac2{N^2}X^{\\mathsf T}CX",
     "by": "line 1, line 2"
    },
    {
     "line": 4,
     "tex": "\\mathbb E[X^{\\mathsf T}CX\\mid\\mathscr G]=\\operatorname{tr}(C\\,\\mathbb E[XX^{\\mathsf T}\\mid\\mathscr G])=\\operatorname{tr}(C(C+\\mu\\mu^{\\mathsf T}))",
     "by": "line 3; floor: tower 성질, $\\mathbb E[XX^{\\mathsf T}\\mid\\mathscr G]=C+\\mu\\mu^{\\mathsf T}$, trace 의 순환성"
    }
   ],
   "author_filled": "원문은 'Conditional independence gives' 뒤에 결과만 적는다. $X$ 를 조건에 넣어 $Y-Z$ 의 조건부 이차 모멘트가 $2C$ 임을 쓰고, $\\mathbb E[XX^{\\mathsf T}\\mid\\mathscr G]=C+\\mu\\mu^{\\mathsf T}$ 로 trace 를 만드는 전개를 채웠다.",
   "grounding": {
    "source": "decorrelation.tex 133–136",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "t3",
   "kind": "step",
   "title": "양의 준정부호성으로 $\\mu\\mu^{\\mathsf T}$ 항을 버린다",
   "statement": "$\\frac2{N^2}\\operatorname{tr}((C+\\mu\\mu^{\\mathsf T})C)\\ge\\frac2{N^2}\\operatorname{tr}(C^2)$, $C$ 가 양의 준정부호이므로.",
   "derivation": [
    {
     "line": 1,
     "tex": "\\operatorname{tr}(\\mu\\mu^{\\mathsf T}C)=\\mu^{\\mathsf T}C\\mu\\ge0",
     "by": "edge e6; floor: 공분산 행렬은 양의 준정부호, trace 의 순환성"
    },
    {
     "line": 2,
     "tex": "\\frac2{N^2}\\operatorname{tr}((C+\\mu\\mu^{\\mathsf T})C)\\ge\\frac2{N^2}\\operatorname{tr}(C^2)",
     "by": "line 1"
    }
   ],
   "author_filled": "$\\operatorname{tr}(\\mu\\mu^{\\mathsf T}C)=\\mu^{\\mathsf T}C\\mu\\ge0$ 줄을 채웠다. 원문은 'since $C$ is positive semidefinite' 만 적는다.",
   "grounding": {
    "source": "decorrelation.tex 137–139",
    "state": "proposed"
   },
   "status": "complete"
  },
  {
   "id": "t4",
   "kind": "step",
   "title": "기대값을 취하고 trace 를 성분 합으로",
   "statement": "$\\mathbb E(X\\cdot Y-X\\cdot Z)^2\\ge\\frac2{N^2}\\mathbb E\\operatorname{tr}(C^2)=\\frac2{N^2}\\mathbb E\\sum_{i,j}C_{ij}^2$.",
   "derivation": [
    {
     "line": 1,
     "tex": "\\mathbb E(X\\cdot Y-X\\cdot Z)^2=\\mathbb E\\,\\mathbb E[(X\\cdot Y-X\\cdot Z)^2\\mid\\mathscr G]\\ge\\frac2{N^2}\\mathbb E\\operatorname{tr}(C^2)",
     "by": "edge e7; floor: tower 성질, 기대값의 단조성"
    },
    {
     "line": 2,
     "tex": "\\operatorname{tr}(C^2)=\\sum_{i,j}C_{ij}C_{ji}=\\sum_{i,j}C_{ij}^2",
     "by": "floor: $C$ 대칭"
    }
   ],
   "author_filled": "바깥 기대값을 취하는 것과 $\\operatorname{tr}(C^2)=\\sum_{ij}C_{ij}^2$ 을 채웠다. 원문 증명은 조건부 부등식에서 끝난다.",
   "grounding": {
    "source": "decorrelation.tex 137–139 (원문에 없는 마무리)",
    "state": "proposed"
   },
   "status": "complete"
  },
  {
   "id": "out_three_copy",
   "kind": "output",
   "title": "세 사본 bound",
   "statement": "$X,Y,Z$ 가 sigma field $\\mathscr G$ 가 주어졌을 때 유계 random vector의 조건부 독립 사본이고 $C$ 가 그 조건부 공분산 행렬이면 $\\mathbb E(X\\cdot Y-X\\cdot Z)^2\\ge\\frac2{N^2}\\mathbb E\\sum_{i,j}C_{ij}^2$.",
   "output_items": [
    "three_copy"
   ],
   "grounding": {
    "source": "decorrelation.tex 117–124",
    "state": "proposed"
   },
   "status": "sketch"
  }
 ],
 "edges": [
  {
   "id": "e1",
   "from": "c1",
   "to": "c2",
   "statement": "$\\mathbb E[((A_S-\\mu_{d,S})\\cdot B)^2\\mid\\mathscr F_d,B]=N^{-2}\\sum_{ij}C_{ij}B_iB_j$.",
   "grounding": {
    "source": "decorrelation.tex 128–129",
    "state": "proposed"
   }
  },
  {
   "id": "e2",
   "from": "c2",
   "to": "c3",
   "statement": "조건부 제곱 기대값 $\\le N^{-2}\\sum_{ij}|C_{ij}|$.",
   "grounding": {
    "source": "decorrelation.tex 129–130",
    "state": "proposed"
   }
  },
  {
   "id": "e3",
   "from": "c3",
   "to": "c4",
   "statement": "조건부 제곱 기대값 $\\le(N^{-2}\\sum_{ij}C_{ij}^2)^{1/2}$ (c1–c3 를 이어서).",
   "grounding": {
    "source": "decorrelation.tex 130",
    "state": "proposed"
   }
  },
  {
   "id": "e4",
   "from": "c4",
   "to": "out_contraction",
   "statement": "$\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}$.",
   "grounding": {
    "source": "decorrelation.tex 131",
    "state": "proposed"
   }
  },
  {
   "id": "e5",
   "from": "t1",
   "to": "t2",
   "statement": "$\\mu=\\mathbb E[X\\mid\\mathscr G]$, $C$ 는 $\\mathscr G$ 조건부 공분산, $X,Y,Z$ 는 $\\mathscr G$ 조건부 독립 사본.",
   "grounding": {
    "source": "decorrelation.tex 117–118, 132",
    "state": "proposed"
   }
  },
  {
   "id": "e6",
   "from": "t2",
   "to": "t3",
   "statement": "$\\mathbb E[(X\\cdot Y-X\\cdot Z)^2\\mid\\mathscr G]=\\frac2{N^2}\\operatorname{tr}((C+\\mu\\mu^{\\mathsf T})C)$.",
   "grounding": {
    "source": "decorrelation.tex 135–136",
    "state": "proposed"
   }
  },
  {
   "id": "e7",
   "from": "t3",
   "to": "t4",
   "statement": "$\\mathbb E[(X\\cdot Y-X\\cdot Z)^2\\mid\\mathscr G]\\ge\\frac2{N^2}\\operatorname{tr}(C^2)$.",
   "grounding": {
    "source": "decorrelation.tex 137–139",
    "state": "proposed"
   }
  },
  {
   "id": "e8",
   "from": "t4",
   "to": "out_three_copy",
   "statement": "$\\mathbb E(X\\cdot Y-X\\cdot Z)^2\\ge\\frac2{N^2}\\mathbb E\\sum_{i,j}C_{ij}^2$.",
   "grounding": {
    "source": "decorrelation.tex 121–122, 137",
    "state": "proposed"
   }
  }
 ]
}
```

## 판 B

```json
{
 "nodes": [
  {
   "id": "c1",
   "kind": "step",
   "title": "축약 제곱의 조건부 기대값",
   "statement": "$\\mathscr F_d$ 와 $B$ 가 주어졌을 때 $((A_S-\\mu_{d,S})\\cdot B)^2$ 의 조건부 기대값은 $N^{-2}\\sum_{ij}C_{ij}B_iB_j$ 이다.",
   "local_symbols": [
    {
     "id": "C_F",
     "tex": "$C_{ij}$ (첫 주장)",
     "defined_at": "decorrelation.tex 129 (원문에 정의 없음)",
     "text": "$C_{ij}=\\operatorname{Cov}(A_{S,i},A_{S,j}\\mid\\mathscr F_d)$ 로 읽는다."
    }
   ],
   "derivation": [
    {
     "line": 1,
     "tex": "((A_S-\\mu_{d,S})\\cdot B)^2=N^{-2}\\sum_{i,j}(A_{S,i}-\\mu_{d,S,i})(A_{S,j}-\\mu_{d,S,j})B_iB_j",
     "by": "floor: x·y 의 정의를 전개"
    },
    {
     "line": 2,
     "tex": "\\mathbb E[((A_S-\\mu_{d,S})\\cdot B)^2\\mid\\mathscr F_d,B]=N^{-2}\\sum_{i,j}C_{ij}B_iB_j",
     "by": "lemma 가정: $\\mathscr F_d$ 가 주어졌을 때 $B$ 와 $A_S$ 는 조건부 독립; line 1"
    }
   ],
   "author_filled": "원문은 첫 주장에서 $C$ 를 정의하지 않는다(정의는 둘째 주장 118–119에만 있다). $C_{ij}=\\operatorname{Cov}(A_{S,i},A_{S,j}\\mid\\mathscr F_d)$ 로 채웠다. 또 조건부 독립 때문에 $B$ 를 조건에 넣어도 $\\mathbb E[(A_{S,i}-\\mu_i)(A_{S,j}-\\mu_j)\\mid\\mathscr F_d,B]=C_{ij}$ 라는 걸음도 채웠다.",
   "grounding": {
    "source": "decorrelation.tex 128–129",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "c2",
   "kind": "step",
   "title": "절댓값 상계",
   "statement": "$|N^{-2}\\sum_{ij}C_{ij}B_iB_j|\\le N^{-2}\\sum_{ij}|C_{ij}|$.",
   "local_symbols": [],
   "derivation": [
    {
     "line": 1,
     "tex": "\\bigl|N^{-2}\\sum_{ij}C_{ij}B_iB_j\\bigr|\\le N^{-2}\\sum_{ij}|C_{ij}||B_i||B_j|\\le N^{-2}\\sum_{ij}|C_{ij}|",
     "by": "e1; lemma 가정 $B\\in[-1,1]^N$; floor: 삼각부등식"
    }
   ],
   "author_filled": "$|B_i|\\le1$ 을 쓴다는 것은 원문에 적혀 있지 않아 채웠다.",
   "grounding": {
    "source": "decorrelation.tex 129–130",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "c3",
   "kind": "step",
   "title": "i,j 에 대한 Cauchy–Schwarz",
   "statement": "$N^{-2}\\sum_{ij}|C_{ij}|\\le\\bigl(N^{-2}\\sum_{ij}C_{ij}^2\\bigr)^{1/2}$.",
   "local_symbols": [],
   "derivation": [
    {
     "line": 1,
     "tex": "N^{-2}\\sum_{ij}|C_{ij}|\\le N^{-2}\\Bigl(\\sum_{ij}1\\Bigr)^{1/2}\\Bigl(\\sum_{ij}C_{ij}^2\\Bigr)^{1/2}=\\Bigl(N^{-2}\\sum_{ij}C_{ij}^2\\Bigr)^{1/2}",
     "by": "e2; floor: Cauchy–Schwarz ($N^2$ 개 항)"
    }
   ],
   "author_filled": "원문은 \"first over $i,j$\" 라고만 적었다. 부등식의 명시적 꼴을 채웠다.",
   "grounding": {
    "source": "decorrelation.tex 130",
    "state": "proposed"
   },
   "status": "complete"
  },
  {
   "id": "c4",
   "kind": "step",
   "title": "prefix 에 대한 Cauchy–Schwarz",
   "statement": "$\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}^2\\le v_N(S,d)^{1/2}$ 이므로 \\eqref{decor:contraction-bound} 가 성립한다.",
   "local_symbols": [],
   "derivation": [
    {
     "line": 1,
     "tex": "\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}^2=\\mathbb E\\,\\mathbb E[((A_S-\\mu_{d,S})\\cdot B)^2\\mid\\mathscr F_d,B]\\le\\mathbb E\\Bigl(N^{-2}\\sum_{ij}C_{ij}^2\\Bigr)^{1/2}",
     "by": "e3; floor: tower property"
    },
    {
     "line": 2,
     "tex": "\\le\\Bigl(\\mathbb E\\,N^{-2}\\sum_{ij}C_{ij}^2\\Bigr)^{1/2}=v_N(S,d)^{1/2}",
     "by": "line 1; floor: Cauchy–Schwarz (Jensen) over the prefix; 기호 v_N 의 정의"
    },
    {
     "line": 3,
     "tex": "\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}",
     "by": "line 2; 제곱근"
    }
   ],
   "author_filled": "tower property, $v_N$ 정의와 맞추는 걸음, 마지막 제곱근은 원문에 없어 채웠다.",
   "grounding": {
    "source": "decorrelation.tex 130–131",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "o1",
   "kind": "output",
   "title": "축약 상계",
   "statement": "random vector $B\\in[-1,1]^N$ 이 $\\mathscr F_d$ 가 주어졌을 때 $A_S$ 와 조건부 독립이면 $\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}$.",
   "output_items": [
    "contraction"
   ],
   "grounding": {
    "source": "decorrelation.tex 110–116",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "c5",
   "kind": "step",
   "title": "조건부 평균 두기",
   "statement": "$\\mu=\\mathbb E[X\\mid\\mathscr G]$ 로 둔다. $C$ 는 $\\mathscr G$ 가 주어졌을 때 $X$ 의 조건부 공분산 행렬이다.",
   "local_symbols": [
    {
     "id": "mu_G",
     "tex": "$\\mu$ (둘째 주장)",
     "defined_at": "decorrelation.tex 132",
     "text": "$\\mu=\\mathbb E[X\\mid\\mathscr G]$. 기호 표의 $\\mu_{d,S}$ 와는 다르다."
    },
    {
     "id": "C_G",
     "tex": "$C$ (둘째 주장)",
     "defined_at": "decorrelation.tex 118–119",
     "text": "$\\mathscr G$ 가 주어졌을 때 $X$ 의 조건부 공분산 행렬."
    },
    {
     "id": "G",
     "tex": "$\\mathscr G$",
     "defined_at": "decorrelation.tex 118",
     "text": "임의의 sigma field."
    }
   ],
   "derivation": [],
   "grounding": {
    "source": "decorrelation.tex 132",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "c6",
   "kind": "step",
   "title": "조건부 독립으로 trace 계산",
   "statement": "$\\mathbb E[(X\\cdot Y-X\\cdot Z)^2\\mid\\mathscr G]=\\frac2{N^2}\\operatorname{tr}\\bigl((C+\\mu\\mu^{\\mathsf T})C\\bigr)$.",
   "local_symbols": [],
   "derivation": [
    {
     "line": 1,
     "tex": "X\\cdot Y-X\\cdot Z=N^{-1}X^{\\mathsf T}(Y-Z)",
     "by": "floor: 내적 전개"
    },
    {
     "line": 2,
     "tex": "\\mathbb E[(Y-Z)(Y-Z)^{\\mathsf T}\\mid\\mathscr G]=2C",
     "by": "lemma 가정: $Y,Z$ 는 조건부 독립인 같은 법칙의 사본"
    },
    {
     "line": 3,
     "tex": "\\mathbb E[XX^{\\mathsf T}\\mid\\mathscr G]=C+\\mu\\mu^{\\mathsf T}",
     "by": "e5"
    },
    {
     "line": 4,
     "tex": "\\mathbb E[(X\\cdot Y-X\\cdot Z)^2\\mid\\mathscr G]=N^{-2}\\operatorname{tr}\\bigl(\\mathbb E[XX^{\\mathsf T}\\mid\\mathscr G]\\,\\mathbb E[(Y-Z)(Y-Z)^{\\mathsf T}\\mid\\mathscr G]\\bigr)=\\frac2{N^2}\\operatorname{tr}\\bigl((C+\\mu\\mu^{\\mathsf T})C\\bigr)",
     "by": "lemma 가정: $X$ 와 $(Y,Z)$ 의 조건부 독립; lines 1–3"
    }
   ],
   "author_filled": "원문은 \"Conditional independence gives\" 와 결과만 적었다. lines 1–4 의 계산을 모두 채웠다.",
   "grounding": {
    "source": "decorrelation.tex 133–136",
    "state": "proposed"
   },
   "status": "sketch"
  },
  {
   "id": "c7",
   "kind": "step",
   "title": "양의 준정부호성으로 항 버리기",
   "statement": "$C$ 가 양의 준정부호이므로 $\\frac2{N^2}\\operatorname{tr}((C+\\mu\\mu^{\\mathsf T})C)\\ge\\frac2{N^2}\\operatorname{tr}(C^2)$. 기대값을 취하면 \\eqref{decor:three-copy-bound} 를 얻는다.",
   "local_symbols": [],
   "derivation": [
    {
     "line": 1,
     "tex": "\\operatorname{tr}(\\mu\\mu^{\\mathsf T}C)=\\mu^{\\mathsf T}C\\mu\\ge0",
     "by": "e6; floor: trace 순환성, 공분산 행렬은 양의 준정부호"
    },
    {
     "line": 2,
     "tex": "\\mathbb E[(X\\cdot Y-X\\cdot Z)^2\\mid\\mathscr G]\\ge\\frac2{N^2}\\operatorname{tr}(C^2)=\\frac2{N^2}\\sum_{i,j}C_{ij}^2",
     "by": "e6; line 1; floor: 대칭 행렬에서 $\\operatorname{tr}(C^2)=\\sum_{ij}C_{ij}^2$"
    },
    {
     "line": 3,
     "tex": "\\mathbb E(X\\cdot Y-X\\cdot Z)^2\\ge\\frac2{N^2}\\mathbb E\\sum_{i,j}C_{ij}^2",
     "by": "line 2; floor: tower property"
    }
   ],
   "author_filled": "$\\operatorname{tr}(C^2)=\\sum C_{ij}^2$ 와 바깥 기대값을 취하는 걸음(line 3)은 원문에 없어 채웠다.",
   "grounding": {
    "source": "decorrelation.tex 137–139",
    "state": "proposed"
   },
   "status": "complete"
  },
  {
   "id": "o2",
   "kind": "output",
   "title": "세 사본 하계",
   "statement": "$X,Y,Z$ 가 sigma field $\\mathscr G$ 가 주어졌을 때 유계 random vector의 조건부 독립 사본이고 $C$ 가 그 조건부 공분산 행렬이면 $\\mathbb E(X\\cdot Y-X\\cdot Z)^2\\ge\\frac2{N^2}\\mathbb E\\sum_{i,j}C_{ij}^2$.",
   "output_items": [
    "three_copy"
   ],
   "grounding": {
    "source": "decorrelation.tex 117–124",
    "state": "proposed"
   },
   "status": "sketch"
  }
 ],
 "edges": [
  {
   "id": "e1",
   "from": "c1",
   "to": "c2",
   "statement": "축약 제곱의 조건부 기대값은 $N^{-2}\\sum_{ij}C_{ij}B_iB_j$.",
   "grounding": {
    "source": "decorrelation.tex 128–129",
    "state": "proposed"
   }
  },
  {
   "id": "e2",
   "from": "c2",
   "to": "c3",
   "statement": "그 절댓값은 $N^{-2}\\sum_{ij}|C_{ij}|$ 이하.",
   "grounding": {
    "source": "decorrelation.tex 129–130",
    "state": "proposed"
   }
  },
  {
   "id": "e3",
   "from": "c3",
   "to": "c4",
   "statement": "$\\mathscr F_d$ 와 $B$ 가 주어졌을 때 축약 제곱의 조건부 기대값은 $(N^{-2}\\sum_{ij}C_{ij}^2)^{1/2}$ 이하.",
   "grounding": {
    "source": "decorrelation.tex 130",
    "state": "proposed"
   }
  },
  {
   "id": "e4",
   "from": "c4",
   "to": "o1",
   "statement": "$\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}$.",
   "grounding": {
    "source": "decorrelation.tex 131",
    "state": "proposed"
   }
  },
  {
   "id": "e5",
   "from": "c5",
   "to": "c6",
   "statement": "$\\mu=\\mathbb E[X\\mid\\mathscr G]$ 이므로 $\\mathbb E[XX^{\\mathsf T}\\mid\\mathscr G]=C+\\mu\\mu^{\\mathsf T}$.",
   "grounding": {
    "source": "decorrelation.tex 132, 136",
    "state": "proposed"
   }
  },
  {
   "id": "e6",
   "from": "c6",
   "to": "c7",
   "statement": "$\\mathbb E[(X\\cdot Y-X\\cdot Z)^2\\mid\\mathscr G]=\\frac2{N^2}\\operatorname{tr}((C+\\mu\\mu^{\\mathsf T})C)$.",
   "grounding": {
    "source": "decorrelation.tex 135–137",
    "state": "proposed"
   }
  },
  {
   "id": "e7",
   "from": "c7",
   "to": "o2",
   "statement": "$\\mathbb E(X\\cdot Y-X\\cdot Z)^2\\ge\\frac2{N^2}\\mathbb E\\sum_{i,j}C_{ij}^2$.",
   "grounding": {
    "source": "decorrelation.tex 137–139",
    "state": "proposed"
   }
  }
 ]
}
```
