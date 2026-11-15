| 파일 | 외부 입력 | 역할 | 그쪽 원문 줄 | paper.json 대응 |
|---|---|---|---|---|
| move4 | `XP5` (P5 선택된 수열 (ii)(iii)) | input | — | `pert:selection`.`score_concentration_sequence` (261–262); `pert:selection`.`tree_moments_converge` (263–265) |
| move4 | `XFAM` (섭동족(mark specification, factor, 매개변수)) | input | — | 기호 `mark_specification` (perturbations.tex 28–38); 기호 `pert_factor` (perturbations.tex 51–65); 기호 `pert_parameters` (perturbations.tex 40–50) |
| move4 | `O1.tree_defs` (tree·삽입 재귀·tilted kernel·표본 기대값의 정의) | given | — | 기호 `tree_sampling` (trees.tex 29–39); 기호 `path_kernels` (trees.tex 14–27); `tree:Y-recursion`.`Y_recursion` (67–72); `tree:Y-recursion`.`updated_kernel` (75–80); `tree:Y-recursion`.`updated_probability` (81–82) |
| move4 | `O1.fv_inputs` (첫 변분의 가정·정의·인용 사실 (trees.tex 20–23, 67–82, 107–110, 142–154)) | given | — | 기호 `path_kernels` (trees.tex 14–27); `tree:Y-recursion`.`Y_recursion` (67–72); `tree:Y-recursion`.`standing_boundedness` (73–74); `tree:Y-recursion`.`updated_kernel` (75–80); `tree:insertion`.`monotone_homogeneous` (107–110); `tree:first-variation`.`first_variation` (142–150) |
| move4 | `XM5` (수 5 (decorrelation 이 받는 곳)) | consumer | — | **없음** |
| move4 | `XM6` (수 6 (R2 의 log 전개를 받는 곳)) | consumer | — | **없음** |
| move5 | `X_TI`.`identity` | input | 452–470 | `pert:tree-identity`.`tree_identity` (454–464) |
| move5 | `X_TI`.`anchor_constraint` | input | 427–450 | 기호 `colored_extensions` (perturbations.tex 429–449) |
| move5 | `X_TI`.`empty_addition` | input | 449–468 | `pert:tree-identity`.`empty_addition` (468–468) |
| move5 | `X_RT`.`one_reference_total` | input | 337–345 | `tree:reference-total`.`one_reference_total` (338–345) |
| move5 | `X_RT`.`kappa_total` | input | 346–356 | `tree:reference-total`.`kappa_total` (346–353) |
| move5 | `X_CH`.`charging` | input | 393–405 | `tree:charging`.`charging_bound` (394–401); `tree:charging`.`constant_independence` (402–404) |
| move5 | `X_CH`.`relative_charging` | input | 406–414 | `tree:charging`.`relative_charging` (411–414) |
| move5 | `X_EXT`.`rule` | input | 259–276 | 기호 `extension_history` (trees.tex 259–276) |
| move5 | `X_EXT`.`empty_weight` | input | 295–295 | `tree:extension-expansion`.`empty_extension` (295–295) |
| move5 | `X_SAMP`.`children_independent` | input | 28–34 | 기호 `tree_sampling` (trees.tex 29–39) |
| move5 | `X_SAMP`.`leaf_removal` | input | 38–39 | 기호 `tree_sampling` (trees.tex 29–39) |
| move5 | `OUT` (독립 message 비교가 받는 곳) | consumer | — | **없음** |

입력·선언 입력 항목 15개 가운데 대응 없음 0개. consumer 는 입력이 아니라 세지 않았다.
