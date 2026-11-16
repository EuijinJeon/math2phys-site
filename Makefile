.PHONY: check
check:
	node redesign/proofmap/tools/check_decor.cjs
	node redesign/proofmap/tools/build_decor.cjs
	node redesign/proofmap/checks/2026-11-16-thm-derivation-map/tools/dump_table.cjs > redesign/proofmap/checks/2026-11-16-thm-derivation-map/NODES.md
	@echo '오류 0 · 빌드와 표 갱신 완료'
