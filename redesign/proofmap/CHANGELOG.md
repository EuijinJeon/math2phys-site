# 증명 지도 변경 기록

- 2026-11-20 · “PROP의 입력들이 어떻게 PROP의 결과를 내는지 세부그래프 그려줘” · PROP(body·links), 새 지도 comp-prop: PR_INC, PR_Y, PR_ENC, PR_B, PR_BD, PR_LOG, PR_PAT, PR_SH, PR_TR, PR_SITE, PR_BOND, PR_TID, PR_CUT, PR_POIS, PR_TERM, PR_PERR, PR_GEO, PR_AVG, PR_CONV, PR_EQ, PR_U · 원문 밖 보충 있음(PR_BOND: Wald 항등식으로 기대값; PR_CUT: cosh 표현과 homogeneity로 log z 상쇄) · 각 지도 검사 오류 0 (check_decor.cjs는 기존 move4.json 때문에 실패) · 같은 날의 node 패널 템플릿 수정(a81fcca)은 사용자 요청으로 보류하고 되돌림(6ffa36b)
- 2026-11-20 · “§8 지도 새 세션에서 그려줘” · OUT(body·links·src), 새 지도 comp-thm(§8 comparison.tex): X_SEL, X_INC, X_Y, X_LOG, X_REG, X_B, X_TB, X_DECOR, SET, ENC_CON, ENC, PAT_PI, PAT, SH_B, SH, P_TR, P_ID, P_CUT, P_EXP, P_TAIL, P_ORD, PROP, COR, OUT · 원문 밖 보충 없음 · 각 지도 검사 오류 0 (check_decor.cjs는 기존 move4.json 때문에 실패)
- 2026-11-20 · “X_TI 유도하는 그래프… 새 세션에서 x-ti 지도 만들어줘” · X_TI(body·links), 새 지도 x-ti: XT_FAM, XT_ERR, XT_POIS, XT_INS, XT_EXP, XT_SEL, XT_DEF, XT_SCORE, XT_HDEF, XT_PALM, XT_ANA, XT_VAN, XT_K0, XT_POL, XT_MSEL, XT_SHAPE, XT_ASM, XT_EQ, XT_U · 원문 밖 보충 있음(XT_POIS: add-one 식의 꼴; XT_K0: $k=0$ 경우의 풀이) · 각 지도 검사 오류 0 (check_decor.cjs는 기존 move4.json 때문에 실패)
- 2026-11-20 · “T_SIDE의 상세 그래프가 필요할거같은데” · T_SIDES(body·links), 새 지도 t-sides: TS_TI, TS_SET, TS_C, TS_SAMP, TS_APPLY, TS_LSHAPE, TS_RSHAPE, TS_CI, TS_DEL, TS_SUB, TS_VAR, TS_U_VM · 원문 밖 보충 있음(TS_LSHAPE: 허용 history가 모두 같은 결합 tree를 준다는 것; TS_VAR: tower property) · 각 지도 검사 오류 0 (check_decor.cjs는 기존 move4.json 때문에 실패)
- 2026-11-20 · “T_VAR derivation 상세그래프 써줘. 입력이 많아서 절차를 그래프로 보여주면 도움이 될듯” · T_VAR(body·links), 새 지도 t-var: TV_SET, TV_L2, TV_ADJ, TV_FIB, TV_VM, TV_ERR, TV_ADEF, TV_DEC, TV_BND, TV_AVG, TV_T1, TV_SUM · 원문 밖 보충 없음 · 각 지도 검사 오류 0 (check_decor.cjs는 기존 move4.json 때문에 실패)
- 2026-11-19 · “X_SAMP 이것도 상세 유도 그려줘” · X_SAMP(body·links), 새 지도 x-samp: XS_KER, XS_TREE, XS_JOINT, XS_PROJ, XS_CI, XS_U_DC, XS_U_PB, XS_U_SIDES · 원문 밖 보충 있음(XS_JOINT·XS_PROJ·XS_CI의 유도; 원문 trees.tex 32–39는 진술만 한다) · 각 지도 검사 오류 0 (check_decor.cjs는 기존 move4.json 때문에 실패)
- 2026-11-19 · “X_CH는 논문 §3에서 나오는거야? 그러면 그쪽 노드들 만들고 이어서 X_CH 유도과정 그래프로 보여줘.” · X_CH(f·body·links), 새 지도 x-ch: XC_GAMMA, XC_TEL, XC_EXT, XC_HYP, XC_UNIT, XC_STEP, XC_UNARY, XC_CREATE, XC_J, XC_ABS, XC_REL · 원문 밖 보충 없음 · 각 지도 검사 오류 0 (check_decor.cjs는 기존 move4.json의 meta.parent 부재로 실패, 이번 변경과 무관)
- 2026-11-16 · “근데 B 조건이 statement에 있었던가?” · B_CON · 원문 밖 보충 없음(원문의 조건을 대표식에 복원) · 검사 오류 0
- 2026-11-16 · “이 내용 DC_ONE 노드에서 링크하도록 해줘” · DC_ONE, DO_SETUP, DO_TELE, DO_CS, DO_JEN · 원문 밖 보충 없음 · 검사 오류 0
- 2026-11-16 · “DC_PROD 이게 뭔지 이해 안돼” · DC_PROD · 원문 밖 보충 있음(두 자식 조건부 공분산 예시) · 검사 오류 0
- 2026-11-16 · “노드 질문부터 그래프·원문 탐색, 유도 작성, 지도 반영, 웹페이지 갱신까지 따라 할 절차를 문서화” · PROCEDURE, UPDATE-PROCEDURE, AGENTS, show_node, check_decor · 원문 밖 보충 없음 · 검사 오류 0
- 2026-11-16 · “B_DC 이건 어떻게 유도하지?” · B_DC, DC_ME, DC_EVAL, DC_PROD, DC_ONE, DC_SUM, DC_ALL · 원문 밖 보충 없음 · 세부 지도와 왕복 링크
- 2026-11-16 · “B_ME 설명해줘” · B_ME · 원문 밖 보충 없음 · 두 지도 검사 오류 0
- 2026-11-16 · “모바일 하위 유도가 깨짐; 원래 페이지 같은 별도 페이지와 왕복 링크” · B_CON, BC_C, BC_Q, BC_CS, BC_DIFF, BC_TRACE · 원문 밖 보충 없음 · 두 지도 검사 오류 0
- 2026-11-16 · “B_CON 좀더 설명해줘” · B_CON, BC_C, BC_Q, BC_CS, BC_DIFF, BC_TRACE · 원문 밖 보충 없음 · 검사 오류 0
- 2026-11-16 · “로컬 Chrome에서 복사 실패, 스케일 간 링크 필요; X_TI→A_ERR의 기호 정의 찾기” · X_TI, A_ERR, viewer · 원문 밖 보충 없음 · 검사 오류 0
- 2026-11-16 · “입구·JSON 분리·node 조회·ID 복사·설명 층위·변경 기록·make check 구성” · 전체, T_C · 기존 원문 밖 보충 1건(T_C) 표시 · 검사 오류 0
- 2026-11-16 · 지도 처음 작성 · 전체 · 보충 1건(T_C: $C(S,e)\neq0$ 근거) · 검사 오류 0
