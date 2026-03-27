# Test Contract Alignment

- owner: codex
- started_at: 2026-03-20
- status: completed

## Goal
- `project-context`와 `project-context-migration` 테스트를 스킬 방향성에 맞게 다시 정렬한다.

## Scope
- `runtime-shape` 테스트에서 빠진 핵심 shape branch를 보강한다.
- CLI presentation exact-match처럼 brittle한 assertion은 완화한다.
- migration fixture test는 representative 분류 결과를 적정 수준으로 복원하되 output tree 전체 고정으로 돌아가지 않는다.

## Current Understanding
- `tests/project_context/test_runtime_shape.py`는 task core file 누락과 latest log block의 일부 failure branch를 놓치고 있다.
- 같은 파일의 CLI 테스트 일부는 thin contract보다 현재 출력 문구에 더 묶여 있다.
- `tests/project_context_migration/test_migration_fixtures.py`는 최근 단순화 이후 beta의 `REFERENCE`/`TASK` positive outcome과 case-wide `MEMORY-CANDIDATES` cleanup을 충분히 못 본다.

## Current Output Snapshot
- `tests/project_context/test_runtime_shape.py`는 task core file 누락, empty/non-bullet latest log block failure branch를 직접 검증하고, CLI output test는 exact full-output pinning 대신 contract-level signal을 본다.
- `tests/project_context_migration/test_migration_fixtures.py`는 case-wide `MEMORY-CANDIDATES.md` cleanup, alpha의 `REFERENCE`/task-local boundary, beta의 `REFERENCE`/`TASK` positive outcome을 representative 수준으로 본다.
