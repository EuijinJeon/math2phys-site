#!/usr/bin/env python3
"""2단계(계약)의 작성 도구. move5.json 의 맨 위 graph와 기호 표를 한 번 만든다.

    python3 redesign/proofmap/checks/2026-11-15-move5-contract/build_top.py

원본은 이 스크립트가 쓴 뒤의 graphs/move5.json 이다. 여는 작업은 JSON을 직접 고친다.
이 스크립트는 그 뒤 다시 돌리지 않는다(돌리면 하위 graph가 지워진다; --force 필요).
진술은 decorrelation.tex 와 표시한 줄 범위에서 옮겼다. 해석·물리 라벨은 넣지 않는다.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "redesign/proofmap/graphs/move5.json"
EXTRACT = Path(__file__).with_name("extract.json")
D = "decorrelation.tex"

# ---------------------------------------------------------------- 기호 표
# 한 기호 한 정의 위치. node는 id로만 참조한다.
SYMBOLS = [
    ("m_d", "$m_d$", f"{D} 4", "이 절 전체에서 $m_d=d/L$."),
    ("delta", "$\\delta$", f"{D} 4", "$\\delta=L^{-1}$."),
    ("N_lim", "$N\\to\\infty$", f"{D} 4–8",
     "각 고정 $L$ 에서 $N$ 의 극한은 모두 Lemma pert:selection 이 주는 크기와 매개변수 선택을 따라 취한다. 그 선택은 Theorem pert:tree-identity 의 항등식을 만족한다. $L$ 마다 다른 수열을 써도 된다. (선택 자체는 perturbations.tex 255–268)"),
    ("topology", "topology $S$", f"{D} 18–20",
     "labeled leaf를 갖는 유한 rooted tree에서 unary vertex를 지운 것. 각 branching vertex에 $\\{0,\\ldots,L-1\\}$ 의 정수 깊이를 주며, 깊이는 모든 가지를 따라 엄격히 증가한다."),
    ("b_S", "$b(S)$", f"{D} 20–21", "topology $S$ 의 branching vertex 수."),
    ("eta_regular", "$\\eta$-regular", f"{D} 21–28",
     "모든 배정 깊이$/L$ 이 $(\\eta,1-\\eta)$ 안에 있고 서로 다른 branching vertex의 정규화 깊이가 $\\eta$ 보다 더 떨어진 배정. prefix 깊이 $d$ 가 추가로 지정되면 모든 branching 깊이에 대해 같은 제한을 지킨다. 한 topology의 두 사본이 aligned 깊이를 쓰면 대응 vertex는 깊이 좌표 하나를 공유하고, regularity는 서로 다른 좌표들에 건다."),
    ("A_avg", "$\\mathcal A_{L,\\eta}$", f"{D} 30–38",
     "$a$ 개 깊이 좌표 위의 음 아닌 배열 $z$ 에 대해 $\\mathcal A_{L,\\eta}z=L^{-a}\\sum_{\\mathbf q\\ \\eta\\text{-regular}}z(\\mathbf q)$. 추가 순서 제한(예: $d<\\min_vq_v$)은 합의 범위에 넣는다. 정규화하지 않은 평균이라 총질량 $\\le1$."),
    ("eps_NLk", "$\\varepsilon_{N,L,k}$", f"{D} 49–58",
     "아래에서 쓰는 유한 모음 위에서 취한 Theorem pert:tree-identity 오차의 최대."),
    ("E_root", "$\\mathbb E$", "trees.tex 47–48", "따로 적지 않은 기대값 $\\mathbb E$ 는 root와 해당 tree의 표본추출을 포함한다."),
    ("R_S", "$R_S$", "trees.tex 42–46; " + f"{D} 60–61, 90",
     "spin replica leaf 부분집합 $S$ 의 multioverlap $R_S=\\frac1N\\sum_{i}\\prod_{a\\in S}\\sigma_i^a$, $R_\\varnothing=1$. 수 5에서는 표본 leaf에 대해 $R_S=\\mathbf 1\\cdot A_S$."),
    ("A_S", "$A_S$, $x\\cdot y$, $\\|x\\|_N$", f"{D} 87–93",
     "$S$ 의 표본 사본에 대해 $A_S=(\\prod_{a\\in S}\\sigma_i^a)_{i\\le N}$, $x\\cdot y=N^{-1}\\sum_ix_iy_i$, $\\|x\\|_N^2=x\\cdot x$."),
    ("F_d", "$\\mathscr F_d$", f"{D} 94–95",
     "처음 stem 위의 깊이 $d$ (첫 branching 깊이 포함)에서 root와 깊이 $d$ 까지의 표본 prefix가 생성하는 sigma field."),
    ("mu", "$\\mu_{d,S}$", f"{D} 97–98", "$\\mu_{d,S}=\\mathbb E[A_S\\mid\\mathscr F_d]$."),
    ("v_N", "$v_N(S,d)$", f"{D} 99–104",
     "$v_N(S,d)=N^{-2}\\mathbb E\\sum_{i,j}\\operatorname{Cov}(A_{S,i},A_{S,j}\\mid\\mathscr F_d)^2$. 기대값은 root를 포함한다. $A_S$, $\\mu_{d,S}$ 의 좌표는 절댓값 $\\le1$, $0\\le v_N\\le1$."),
    ("S_U", "$S^U$", f"{D} 144–146", "$S$ 와 같은 topology에서 branching vertex 부분집합 $U$ 의 깊이를 1씩 올린 것."),
    ("a_p", "$a_{S,e}$, $p_N(S,e)$", f"{D} 208–215",
     "$S$ 가 깊이 $e$ 에서 처음 proper child shape $T_1,\\ldots,T_s$ 로 갈라질 때 $a_{S,e}=\\prod_j\\mu_{e,T_j}$ (좌표별 곱), $p_N(S,e)=\\sum_jv_N(T_j,e)^{1/4}$."),
    ("V_kL", "$V_{k,L}(\\eta)$", f"{D} 253–257",
     "$V_{k,L}(\\eta)=\\max_{1\\le|S|\\le k}\\limsup_{N}\\mathcal A_{L,\\eta}v_N(S,d)$. 최대는 유한 개 labeled topology 위."),
    ("S_plus", "$S^+$", f"{D} 297–298", "$S$ 의 모든 내부 branching 깊이를 1씩 올린 topology."),
    ("kappa", "$\\kappa(T)$", "trees.tex 346–354", "reference 계수 $\\kappa(S)=\\prod_{v\\in\\operatorname{Br}(S)}\\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$; $a_v$, $d_v$ 는 처방한 reference tree에서 vertex의 자식 수와 깊이."),
    ("J", "$J$", f"{D} 333–336", "$J=\\kappa(S^+)^2$."),
    ("ext_hist", "$E$, $c_E$, $\\mathfrak E(\\mathcal T,a_*,\\mathcal C)$", "trees.tex 259–276; perturbations.tex 427–440",
     "extension history와 그 계수(선택한 계수들의 곱), 제약 $\\mathcal C$ 를 지키는 허용 history의 모음."),
    ("anchor", "spin / marker anchor, $\\mathcal C$, $R_E$", "perturbations.tex 427–450",
     "$S_0=\\sigma_i$ 이면 spin anchor, $S_0=1$ 이면 marker anchor. $\\mathcal C$ 는 추가 color와 anchor만의 쌍별 split 깊이를 처방한다. $R_E$ 는 history가 고른 새 replica(spin anchor이면 anchor 포함)의 multioverlap."),
]


def items(*xs):
    return [{"id": i, "statement": s, "lines": l, **({"author_filled": a} if a else {})} for i, s, l, a in xs]


# ---------------------------------------------------------------- node
NODES = [
    dict(id="AVG", machine_id="decor:average-holder", rule="E", kind="object", title="깊이 평균과 그 두 비교",
         summary="$\\mathcal A_{L,\\eta}$, Hölder, 쓰지 않는 좌표, 정수 shift",
         span=f"{D} 30–47", stmt=[30, 47], proof=None, layout=(0, 0),
         symbols=["A_avg", "eta_regular", "topology"],
         outputs=items(
             ("def_A", "$\\mathcal A_{L,\\eta}z=L^{-a}\\sum_{\\mathbf q\\ \\eta\\text{-regular}}z(\\mathbf q)$ (음 아닌 $z$, $a$ 개 좌표). 추가 순서 제한은 합의 범위에 넣는다. 총질량 $\\le1$.", [30, 38], None),
             ("holder", "$0<\\gamma\\le1$ 이면 $\\mathcal A_{L,\\eta}(z^\\gamma)\\le(\\mathcal A_{L,\\eta}z)^\\gamma$.", [38, 43], None),
             ("unused_coord", "쓰지 않는 좌표에 대한 합은 많아야 $L$ 배이고 그 좌표의 정규화가 상쇄한다.", [44, 45], None),
             ("shift_regular", "좌표의 임의 부분집합을 고정 정수만큼 옮기면, 충분히 큰 $L$ 에서 $\\eta$-regular 배정이 $\\eta/2$-regular 배정으로 단사로 간다.", [45, 47], None))),
    dict(id="IDE", machine_id="decor:identity-error", rule="E", kind="object", title="항등식 오차의 유한 최대",
         summary="$\\varepsilon_{N,L,k}\\to0$ (고정 $L,k$), 상수는 $L$ 에 의존 가능",
         span=f"{D} 49–58", stmt=[49, 58], proof=None, layout=(0, 1),
         symbols=["eps_NLk", "N_lim", "topology"],
         outputs=items(
             ("eps_def", "유계 크기의 labeled topology는 유한 개이고 고정 $L$ 에서 깊이 배정도 유한 개이므로, Theorem pert:tree-identity 의 오차를 아래의 유한 모음 위에서 $N\\to\\infty$ 전에 최대화할 수 있다. 그 최대가 $\\varepsilon_{N,L,k}$.", [49, 53], None),
             ("eps_to_zero", "각 고정 $L,k$ 에서 $\\varepsilon_{N,L,k}\\to0$ ($N\\to\\infty$).", [53, 57], None),
             ("L_constants", "이 오차에 곱하는 상수는 $L$ 에 임의로 의존해도 된다.", [58, 58], None))),
    dict(id="CON", machine_id="decor:contractions", rule="S", kind="step", title="Lemma: 축약과 세 사본",
         summary="$\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N^{1/4}$; 세 사본 하계",
         span=f"{D} 108–140", stmt=[108, 125], proof=[127, 140], layout=(1, 0),
         symbols=["A_S", "F_d", "mu", "v_N", "E_root"],
         outputs=items(
             ("contraction", "random vector $B\\in[-1,1]^N$ 이 $\\mathscr F_d$ 가 주어졌을 때 $A_S$ 와 조건부 독립이면 $\\|(A_S-\\mu_{d,S})\\cdot B\\|_{L^2}\\le v_N(S,d)^{1/4}$.", [110, 116], None),
             ("three_copy", "$X,Y,Z$ 가 sigma field $\\mathscr G$ 가 주어졌을 때 유계 random vector의 조건부 독립 사본이고 $C$ 가 그 조건부 공분산 행렬이면 $\\mathbb E(X\\cdot Y-X\\cdot Z)^2\\ge\\frac2{N^2}\\mathbb E\\sum_{i,j}C_{ij}^2$.", [117, 124], None))),
    dict(id="DC", machine_id="decor:depth-continuity", rule="S", kind="step", title="Lemma: 깊이에 대한 평균 연속성",
         summary="깊이 1칸 이동의 비용 $\\le C/L$ (깊이 평균)",
         span=f"{D} 142–206", stmt=[142, 166], proof=[168, 206], layout=(1, 1),
         symbols=["topology", "S_U", "mu", "F_d", "A_avg", "eta_regular", "A_S"],
         outputs=items(
             ("branch_shift", "topology $S$ 와 branching vertex 부분집합 $U$ 를 고정하고 각 $\\eta$-regular 배정에서 $S^U$ 를 둔다. 조상 쪽 평가 깊이 $d$ 에서 같은 표본 prefix로 평균을 비교하면, 충분히 큰 $L$ 에서 $\\mathcal A_{L,\\eta}\\mathbb E\\|\\mu_{d,S^U}-\\mu_{d,S}\\|_N^2\\le C/L$. 평균은 모든 branching 깊이에 대해서이고, $d$ 가 움직이면 $d$ 도 평균하고 아니면 고정한다.", [144, 155], None),
             ("eval_shift", "$d$ 가 $S$ 의 처음 unary 구간을 따라 움직이면 $\\mathcal A_{L,\\eta}\\mathbb E\\|\\mu_{d+1,S}-\\mu_{d,S}\\|_N^2\\le C/L$. 이 평균은 $d$ 와 모든 branching 깊이를 포함하고, 평균들은 같은 표본 path 위에서 평가한다.", [155, 163], None),
             ("uniform_constant", "상수는 vertex 수와 shift 수에만 의존하고 $N$, 평가 깊이, transition kernel에 균일하다.", [163, 165], None),
             ("martingale_energy", "$T$ 의 나중 branching 깊이를 고정하고 처음 stem을 따라 path 하나를 뽑으면 $\\mu_{t,T}$ 는 유계 vector martingale이고 $\\sum_t\\mathbb E\\|\\mu_{t+1,T}-\\mu_{t,T}\\|_N^2\\le1$. (증명 블록 안의 식을 밖에서 참조)", [169, 175], None),
             ("larger_tree", "관련된 한-prefix 주변 법칙은 다른 표본 가지를 빼도 변하지 않으므로 이 평가들은 더 큰 표본 tree 안에서도 성립한다.", [203, 205], None))),
    dict(id="PB", machine_id="decor:projection-bound", rule="E", kind="step", title="자식을 평균으로 바꾸는 사영",
         summary="$\\|(A_S-a_{S,e})\\cdot B\\|_{L^2}\\le p_N(S,e)$",
         span=f"{D} 208–230", stmt=[208, 230], proof=None, layout=(2, 0),
         symbols=["a_p", "mu", "v_N", "A_S", "F_d"],
         outputs=items(
             ("product_mean", "$S$ 가 깊이 $e$ 에서 처음 proper child shape $T_1,\\ldots,T_s$ 로 갈라지면 자식의 조건부 독립으로 $\\mu_{e,S}=\\prod_j\\mu_{e,T_j}$.", [208, 210], None),
             ("projection", "$e$ 의 prefix가 주어졌을 때 $S$ 의 연속과 독립인 $B\\in[-1,1]^N$ 에 대해 $\\|(A_S-a_{S,e})\\cdot B\\|_{L^2}\\le p_N(S,e)$.", [216, 225], None),
             ("two_sides", "특히 $B=\\mathbf 1$ 과, $e$ 전에 갈라진 다른 쪽에서 뽑은 vector에 적용된다. 그런 두 쪽은 함께 사영해 총 $L^2$ 오차가 많아야 $2p_N(S,e)$.", [225, 228], None),
             ("scalar_test", "$|f|\\le1$ 인 scalar 시험함수를 축약 오차에 곱하면, 상관되어 있어도 $L^1$ 경계가 커지지 않는다.", [228, 230], None))),
    dict(id="CC", machine_id="decor:conditional-concentration", rule="S", kind="step", title="Proposition: 조건부 decorrelation",
         summary="$\\lim_L\\limsup_N\\mathcal A_{L,\\eta}v_N(S,d)=0$",
         span=f"{D} 234–524", stmt=[234, 245], proof=[247, 524], layout=(3, 0),
         symbols=["v_N", "A_avg", "eta_regular", "V_kL", "topology", "b_S", "S_plus", "J", "kappa", "a_p", "ext_hist", "anchor", "eps_NLk", "m_d", "delta", "N_lim", "R_S", "A_S", "mu", "F_d", "E_root"],
         outputs=items(
             ("main", "모든 고정 labeled topology $S$ 와 $\\eta>0$ 에서 $\\lim_{L\\to\\infty}\\limsup_{N\\to\\infty}\\mathcal A_{L,\\eta}v_N(S,d)=0$. 평균은 $S$ 의 모든 branching 깊이와 첫 split보다 엄격히 앞선 regular 깊이 $d$ 에 대해서. singleton이면 $d$ 만.", [236, 244], None),
             ("V_to_zero", "모든 고정 $k,\\eta$ 에서 $V_{k,L}(\\eta)\\to0$ ($L\\to\\infty$).", [522, 523], None),
             ("relative_cost", "증명의 구성($S^+$, $J$) 안에서 Lemma tree:charging 으로 $\\frac1{|J|}\\sum_{\\text{allowed}}|c|\\le C_{k,\\eta}$. (증명 블록 안의 식; 밖의 참조는 remark 하나뿐)", [345, 353], None),
             ("fiber_bound", "깊이 좌표 $D$ 개의 평균 안에서 어떤 항이 좌표 $D_j$ 개만 쓰고, 남는 배정마다 원상이 많아야 $L^{D-D_j}$ 개이며 그 좌표가 큰 $L$ 에서 $\\eta/2$-regular 이면, $0<\\gamma\\le1$ 에 대해 $L^{-D}\\sum_{\\mathbf q\\ \\eta\\text{-reg}}w_j(\\pi_j(\\mathbf q))^\\gamma\\le\\bigl(L^{-D_j}\\sum_{\\mathbf y\\ \\eta/2\\text{-reg}}w_j(\\mathbf y)\\bigr)^\\gamma$. shift하지 않은 항은 좌표를 옮기지 않고 같은 경계.", [491, 509],
              "원문은 이 부등식을 aligned 두 사본 구성($D=b(S)+1$)에서만 적고, THM(607–609)이 $D=b(S)$ 로 다시 쓴다. 두 쓰임을 한 항목으로 묶으려고 가정을 일반형으로 적은 것은 작성자다."))),
    dict(id="THM", machine_id="decor:overlap-concentration", rule="S", kind="step", title="Theorem: 모든 multioverlap의 집중",
         summary="$\\lim_L\\limsup_N\\mathcal A_{L,\\eta}\\operatorname{Var}(R_S)=0$",
         span=f"{D} 63–75, 532–611", stmt=[63, 75], proof=[532, 611], layout=(4, 0),
         symbols=["R_S", "A_avg", "b_S", "topology", "V_kL", "a_p", "mu", "F_d", "kappa", "anchor", "ext_hist", "delta", "N_lim", "E_root", "eta_regular"],
         outputs=items(
             ("main", "모든 고정 labeled topology $S$ 와 $\\eta>0$ 에서 $\\lim_{L\\to\\infty}\\limsup_{N\\to\\infty}\\mathcal A_{L,\\eta}\\operatorname{Var}(R_S)=0$. $b(S)$ 개의 branching 깊이만 평균한다. singleton은 각 고정 $L$ 에서 $\\operatorname{Var}(R_S)\\to0$ ($N\\to\\infty$).", [65, 74], None))),
]

EXTERNALS = [
    dict(id="X_TI", label="pert:tree-identity", title="Theorem: prescribed tree 위의 항등식", source="perturbations.tex 427–470",
         layout=(0, 3), outputs=items(
             ("identity", "섭동족과 Lemma pert:selection 의 모든 수열을 따라 $\\sum_{E\\in\\mathfrak E(\\mathcal T,a_*,\\mathcal C)}c_E\\mathbb E[fR_E]-\\mathbb Ef\\sum_{E\\in\\mathfrak E(\\{a_*\\},a_*,\\mathcal C)}c_E\\mathbb E[R_E]\\to0$. 모든 고정 old tree, 두 종류의 anchor, multioverlap의 모든 유계 다항식 $f$, 유한 개의 순서 있는 추가 color, 모든 처방 제약 $\\mathcal C$ 에서 성립. 빈 추가도 허용. 오차는 고정 $L$, tree, 제약에서 $L$ 의 극한 전에 0으로 간다.", [452, 470], None),
             ("anchor_constraint", "$S_0=\\sigma_i$ 이면 spin anchor, $S_0=1$ 이면 marker anchor. 추가 color $1..k$ 는 anchor가 아닌 서로 다른 replica 자리를 차지한다. $\\mathcal C$ 는 추가 color와 anchor만의 쌍별 split 깊이의 일관된 모음을 처방하고 다른 old replica에는 제한을 걸지 않는다. $R_E$ 는 spin anchor이면 $\\frac1N\\sum_i\\sigma_i^{a_*}\\prod_j\\sigma_i^{a_j(E)}$, marker anchor이면 $\\frac1N\\sum_i\\prod_j\\sigma_i^{a_j(E)}$.", [427, 450], None))),
    dict(id="X_RT", label="tree:reference-total", title="Lemma: reference-path 총합", source="trees.tex 337–356",
         layout=(2, 2), outputs=items(
             ("one_reference_total", "다음 color가 처방한 reference prefix를 깊이 $d$ 까지 따라가고 거기서 reference path를 담은 $j\\ge1$ 개 자식과 다른 자식으로 들어가야 하면(그 밖의 연속은 자유), 허용 선택의 계수 합은 $m_d-jm_{d+1}$.", [337, 345], None),
             ("kappa_total", "anchor와 color들이 처방한 tree $S$ 를 이루어야 하면, 임의 old tree의 모든 호환 extension 위의 계수 총합은 $\\kappa(S)$. 같은 한 걸음 규칙은 이미 만든 reference 집합에서 시작해 반복할 수 있다.", [346, 356], None))),
    dict(id="X_CH", label="tree:charging", title="Lemma: fresh split의 비용", source="trees.tex 393–414",
         layout=(2, 3), outputs=items(
             ("charging", "$m_d=d/L$, $\\delta=L^{-1}$. $q$ leaf old tree에서 $k$ color를 canceled-anchor 규칙으로 배정하고 reference 모양을 처방(허용 extension에 추가 제한 가능)할 때, 그 모양의 지정 branching vertex $b$ 개의 깊이가 old tree 어디의 branching 깊이도 아니면 $\\sum_{E\\text{ allowed}}|c_E|\\le C_{q,k}\\delta^b$. 상수는 $L$, 지정 깊이, 그 일치와 무관.", [393, 405], None),
             ("relative_charging", "그 $b$ 개 vertex에 대해 $J=\\prod_v\\prod_{j=1}^{a_v-1}(m_{d_v}-jm_{d_v+1})$ 로 두고 그 모두에서 $m_{d_v}\\ge\\eta>0$ 이면 $J\\ne0$ 이고 $\\frac1{|J|}\\sum_{E\\text{ allowed}}|c_E|\\le C_{q,k,\\eta}$.", [406, 414], None))),
    dict(id="X_EXT", label=None, title="extension 규칙 (계수 $1$, $\\gamma_\\beta$)", source="trees.tex 259–276",
         layout=(1, 3), supplemented=True, outputs=items(
             ("rule", "anchor leaf $a_*$ 를 가진 tree $\\mathcal T$ 에서 color $1..k$ 를 차례로 배정한다. 다음 color는 (i) $a_*$ 가 아닌 안 쓴 old leaf (계수 $1$) 또는 (ii) 현재 tree의 내부 vertex $\\beta$ 에서 fresh path (계수 $\\gamma_\\beta=m_{d_\\beta}-n_\\beta m_{d_\\beta+1}$). 현재 tree는 안 쓴 것을 포함한 모든 old path와 이미 붙인 path. $c_E$ 는 계수들의 곱, $\\mathcal T_E$ 는 마지막 tree.", [259, 276], None))),
    dict(id="X_SAMP", label=None, title="tree 표본 규칙", source="trees.tex 28–39, 47–48",
         layout=(0, 2), supplemented=True, outputs=items(
             ("children_independent", "각 vertex에서 서로 다른 자식은 해당 kernel로 독립으로 뽑는다. $E_{\\mathcal T}$ 는 root가 주어진 표본 기대값.", [28, 34], None),
             ("leaf_removal", "leaf 몇 개와 남은 leaf가 쓰지 않는 path 부분을 지우면 남은 tree의 표본 법칙이 보존된다.", [38, 39], None))),
]

OUTS = [dict(id="OUT", label="comp:section", title="밖에서 받는 곳: 독립 message 비교", source="comparison.tex 148–156", layout=(5, 0))]

# ---------------------------------------------------------------- edge
# (from, to, kind, [(item, used_at lines, origin)])
M, S = "machine", "supplemented"
EDGES = [
    ("X_TI", "IDE", "call", [("identity", [51], M)]),
    ("CON", "PB", "flow", [("contraction", [218], M)]),
    ("AVG", "CC", "definition", [("holder", [262], M), ("unused_coord", [259, 260], S), ("shift_regular", [260, 497, 498], S)]),
    ("CON", "CC", "flow", [("three_copy", [288, 483], M)]),
    ("X_RT", "CC", "call", [("kappa_total", [332, 414, 415], M), ("one_reference_total", [414], S)]),
    ("X_CH", "CC", "call", [("relative_charging", [348, 352], M)]),
    ("PB", "CC", "flow", [("projection", [364, 460], M), ("two_sides", [364, 481, 482], S), ("scalar_test", [453, 454], S)]),
    ("DC", "CC", "flow", [("branch_shift", [368], M), ("eval_shift", [367, 368], M), ("larger_tree", [368], S)]),
    ("IDE", "CC", "flow", [("eps_def", [450, 514], M), ("eps_to_zero", [457, 514], M), ("L_constants", [450], S)]),
    ("X_TI", "CC", "call", [("identity", [250, 279, 298, 435], S), ("anchor_constraint", [265, 296, 299], S)]),
    ("X_EXT", "CC", "call", [("rule", [266, 269, 391, 393], S)]),
    ("X_SAMP", "CC", "call", [("children_independent", [287, 363, 395], S), ("leaf_removal", [404, 405], S)]),
    ("PB", "THM", "flow", [("projection", [580], M), ("product_mean", [576], S)]),
    ("DC", "THM", "flow", [("martingale_energy", [583], M)]),
    ("CC", "THM", "flow", [("fiber_bound", [607], M), ("V_to_zero", [601, 609], M), ("main", [609], M)]),
    ("X_TI", "THM", "call", [("identity", [533, 545, 556], S), ("anchor_constraint", [539, 540], S)]),
    ("X_RT", "THM", "call", [("kappa_total", [545, 547], S)]),
    ("X_SAMP", "THM", "call", [("children_independent", [550], S), ("leaf_removal", [553, 555], S)]),
    ("AVG", "DC", "definition", [("shift_regular", [202, 203], S)]),
    ("X_SAMP", "DC", "call", [("leaf_removal", [204, 205], S)]),
    ("X_SAMP", "PB", "call", [("children_independent", [209], S)]),
    ("THM", "OUT", "flow", [("main", ["comparison.tex 153"], M)]),
]


def main():
    if OUT.exists() and "--force" not in sys.argv:
        sys.exit(f"{OUT} 가 이미 있다. 여는 작업 뒤에는 JSON을 직접 고친다(--force 로 덮어쓰기).")
    ext = json.loads(EXTRACT.read_text(encoding="utf-8"))
    machine_ids = {n["id"] for n in ext["nodes"]}
    out_of = {}
    for n in NODES + EXTERNALS + OUTS:
        out_of[n["id"]] = {o["id"]: o for o in n.get("outputs", [])}
    out_of["OUT"] = {}
    nodes = []
    for n in NODES:
        assert n["machine_id"] in machine_ids, n["machine_id"]
        nodes.append({
            "id": n["id"], "kind": n["kind"], "title": n["title"], "summary": n["summary"],
            "statement": " ".join(o["statement"] for o in n["outputs"]),
            "inputs": sorted({e[0] for e in EDGES if e[1] == n["id"]}),
            "abstraction": "exact", "status": "sketch",
            "grounding": {"source": n["span"], "state": "proposed"}, "library": "미대조",
            "contract": {"source_label": n["machine_id"], "extraction_rule": n["rule"],
                         "statement_span": n["stmt"], "proof_span": n["proof"],
                         "outputs": n["outputs"],
                         "needs": [{"from": e[0], "items": [c[0] for c in e[3]]} for e in EDGES if e[1] == n["id"]]},
            "symbols": n["symbols"],
            "layout": {"col": n["layout"][0], "row": n["layout"][1]},
        })
    for x in EXTERNALS:
        nodes.append({
            "id": x["id"], "kind": "external", "title": x["title"],
            "summary": ", ".join(o["id"] for o in x["outputs"]),
            "statement": " ".join(o["statement"] for o in x["outputs"]),
            "grounding": {"source": x["source"], "state": "proposed"},
            "contract": {"source_label": x["label"], "outputs": x["outputs"],
                         "extraction_rule": "supplemented" if x.get("supplemented") else "external-ref"},
            "layout": {"col": x["layout"][0], "row": x["layout"][1]},
        })
    for o in OUTS:
        nodes.append({"id": o["id"], "kind": "external", "title": o["title"],
                      "summary": "Theorem decor:overlap-concentration 을 고정 $\\eta$ 에서 쓴다",
                      "grounding": {"source": o["source"], "state": "proposed"},
                      "contract": {"source_label": o["label"], "extraction_rule": "consumer", "outputs": []},
                      "layout": {"col": o["layout"][0], "row": o["layout"][1]}})
    edges = []
    for i, (f, t, kind, carried) in enumerate(EDGES, 1):
        origins = {c[2] for c in carried}
        stmt = []
        for item, used, _ in carried:
            src = out_of[f][item]
            stmt.append(f"[{f}.{item}] {src['statement']}")
        edges.append({
            "id": f"t{i}", "from": f, "to": t, "kind": kind,
            "summary": ", ".join(c[0] for c in carried),
            "statement": " ".join(stmt),
            "carries": [{"node": f, "item": c[0], "used_at": c[1], "origin": c[2]} for c in carried],
            "origin": origins.pop() if len(origins) == 1 else "mixed",
            "grounding": {"source": f"{D} " + ", ".join(str(l) for c in carried for l in c[1] if isinstance(l, int))
                          if t != "OUT" else "comparison.tex 153"},
            "status": "connected", "complete": True,
        })
    doc = {
        "format": "proofmap/0.1", "id": "move5",
        "title": "수 5 — decorrelation.tex (원문 구조로 자른 계약 graph)",
        "language": "ko",
        "math_syntax": "LaTeX in text: $...$ inline, $$...$$ display (KaTeX-compatible)",
        "source": {"root": "redesign/source/sections", "range": "decorrelation.tex 1–623",
                   "note": "grounding.source 는 이 폴더의 파일과 줄 범위다."},
        "floor": {"reader": ["대학원 확률: 조건부 기대값, martingale, Cauchy–Schwarz, Jensen"],
                  "source": "원문이 적은 수준."},
        "content_note": ("2026-11-15 PoC. node 경계는 원문 구조(extract_tex.py 기계 추출)이고 물리 라벨은 없다. "
                         "모든 node는 계약(진술·출력 항목·필요 입력)만 있는 sketch다. 안쪽 유도는 하위 graph를 연 node에만 있다. "
                         "edge의 carries[].origin 이 machine 이면 \\ref/\\eqref/\\cref 로 기계 추출, supplemented 이면 작성자가 증명 본문에서 보충. "
                         "edge의 complete:true 는 싣는 항목의 진술이 다 적혔다는 뜻이고(SPEC 5절), 의존 목록이 빠짐없다는 보증은 아니다. "
                         "모든 근거는 proposed. 원문 4–9행의 절 머리 가정, figure, remark decor:order-of-limits 는 node가 아니다(기호 표 N_lim, REPORT 참조)."),
        "symbols": [{"id": s[0], "tex": s[1], "defined_at": s[2], "text": s[3]} for s in SYMBOLS],
        "graphs": [{
            "id": "top", "title": "수 5 전체 (계약)", "parent": None,
            "summary": "decorrelation.tex 의 번호 붙은 진술 7개와 외부 입력 5개, 받는 곳 1개.",
            "nodes": nodes, "edges": edges,
        }],
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"node {len(nodes)}, edge {len(edges)}, 기호 {len(SYMBOLS)}")
    print("machine carries", sum(1 for e in EDGES for c in e[3] if c[2] == M),
          "supplemented carries", sum(1 for e in EDGES for c in e[3] if c[2] == S),
          "supplemented-only edges", sum(1 for e in EDGES if all(c[2] == S for c in e[3])))


if __name__ == "__main__":
    main()
