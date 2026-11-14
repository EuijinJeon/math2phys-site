-- Structure-only export. NOT compiled here; no Lean proof or formalization status.
-- Reference: verso-blueprint v4.35.0 doc/MANUAL.md, Core Block Forms / uses.
import Verso
import VersoManual
import VersoBlueprint

open Verso.Genre
open Verso.Genre.Manual
open Informal

#doc (Manual) "PM: interface and six informal steps" =>

:::group "pm_group"
power mean의 첫 변분. 전체 내용은 비형식 설명이며 Lean 검증 상태를 부여하지 않는다.
:::

:::definition "pm_frame" (parent := "pm_group")
유한 확률 kernel 열 $`K_1,\ldots,K_L`, 수 $`0=m_0<\cdots<m_L=1`. $`A_{\boldsymbol t}=1+\sum_jt_jD_j`, $`D_j` 유계 실수 path 함수, $`\boldsymbol t` 는 $`0<a\le A_{\boldsymbol t}\le b` 인 실수 근방 $`U` 안. $`j` 고정, $`\partial=\partial_{t_j}`, $`c=\lVert D_j\rVert_\infty/a`. $`K_d` 와 $`D_j` 는 $`\boldsymbol t` 에 무관하다. $`\mathscr F_d` 는 깊이 $`d` 까지의 prefix sigma-field이며 $`Y_d` 는 그 prefix의 함수다. root를 고정한다.
:::

:::definition "pm_e1" (parent := "pm_group") (uses := "pm_frame")
$`Y_{d-1}=\bigl(K_d\,Y_d^{m_d}\bigr)^{1/m_d}.` $`Y_d` 는 깊이 $`d` 까지의 prefix의 양의 함수, $`Y_{d-1}` 은 깊이 $`d-1` 까지의 prefix의 함수다.
:::

:::definition "pm_e2" (parent := "pm_group") (uses := "pm_frame")
깊이 $`d` 까지의 prefix의 유계 함수 $`h` 에 대해 $`K_d^{A}[h]=K_d\Bigl[\Bigl(\frac{Y_d}{Y_{d-1}}\Bigr)^{m_d}h\Bigr].`
:::

:::lemma_ "pm_e3" (parent := "pm_group") (uses := "pm_frame")
$`a\le A\le b` 이면 모든 깊이에서 $`a\le Y_d\le b`.
:::

:::lemma_ "pm_ih" (parent := "pm_group") (uses := "pm_frame")
깊이 $`d`의 입력: $`Y_d`는 $`U`에서 미분 가능하고 $`|\partial\log Y_d|\le c`. $`d=L`이면 e4L, 그 뒤에는 직전 깊이의 e4에서 받는다.
:::

:::definition "pm_floor" (parent := "pm_group")
선언된 바닥: 연쇄 법칙 / 적분 기호 아래의 미분: 피적분함수의 도함수가 $`U` 에서 균일하게 유계이면 미분과 확률 적분을 바꿀 수 있다
:::

:::lemma_ "pm_step_1" (parent := "pm_group") (uses := "pm_e1, pm_e3, pm_frame, pm_floor")
$`\log Y_{d-1}=\frac1{m_d}\log K_d\bigl[Y_d^{m_d}\bigr]`

e1. $`d\ge1` 이라 $`m_d>0`, e3으로 $`Y_d\ge a>0`.
:::

:::lemma_ "pm_step_2" (parent := "pm_group") (uses := "pm_step_1, pm_e3, pm_ih, pm_frame, pm_floor")
$`\partial\log Y_{d-1}=\frac1{m_d}\,\frac{K_d\bigl[\partial\,(Y_d^{m_d})\bigr]}{K_d\bigl[Y_d^{m_d}\bigr]}`

연쇄 법칙과 적분 기호 아래의 미분. 균일 유계: $`\lvert\partial(Y_d^{m_d})\rvert=m_dY_d^{m_d}\lvert\partial\log Y_d\rvert\le m_d\,b^{m_d}c` (e3, e4; $`d=L` 이면 e4 대신 e4′).

원문 밖 보충: 균일 유계를 확인하는 부분은 지도 작성자가 채운 것이다. 원문은 "$`A_{\boldsymbol t}` 가 균등하게 양인 실수 근방에서 미분하면"이라고만 적는다.
:::

:::lemma_ "pm_step_3" (parent := "pm_group") (uses := "pm_step_2, pm_e1, pm_floor")
$`=\frac{K_d\bigl[Y_d^{m_d}\,\partial\log Y_d\bigr]}{Y_{d-1}^{m_d}}`

$`\partial(Y^{m})=mY^{m}\,\partial\log Y`. 분모는 e1.
:::

:::lemma_ "pm_step_4" (parent := "pm_group") (uses := "pm_step_3, pm_e1")
$`=K_d\Bigl[\Bigl(\frac{Y_d}{Y_{d-1}}\Bigr)^{m_d}\partial\log Y_d\Bigr]`

$`Y_{d-1}` 은 깊이 $`d` 의 변수에 의존하지 않는다(e1).
:::

:::lemma_ "pm_step_5" (parent := "pm_group") (uses := "pm_step_4, pm_e2, pm_ih")
$`=K_d^{A}\bigl[\partial\log Y_d\bigr]`

e2. h는 d=L이면 e4L(e4′), d<L이면 e4의 귀납 가정으로 유계.
:::

:::lemma_ "pm_step_6" (parent := "pm_group") (uses := "pm_step_5, pm_e1, pm_e2, pm_e3, pm_ih, pm_frame")
$`\bigl\lvert\partial\log Y_{d-1}\bigr\rvert\le c`

$`K_d^A[1]=K_d[Y_d^{m_d}]/Y_{d-1}^{m_d}=1` (e1, e2)이고 가중치가 양수(e3)이므로 확률 kernel이다. d=L에서는 e4L(e4′), 그 뒤에는 e4로 받은 한계 c가 평균에서 유지된다.
:::

:::lemma_ "pm_out_identity" (parent := "pm_group") (uses := "pm_step_5")
고정한 한 깊이 $`d`에서 $`\partial\log Y_{d-1}=K_d^A[\partial\log Y_d]`.
:::

:::lemma_ "pm_out_bound" (parent := "pm_group") (uses := "pm_step_2, pm_step_6")
$`Y_{d-1}`의 미분 가능성과 $`|\partial\log Y_{d-1}|\le c`.
:::

