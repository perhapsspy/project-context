# Scripts Structure Review

## Goal
- `skills/project-context/scripts`의 파이썬 스크립트와 테스트를 구조와 contract-driven 관점에서 다시 보고, 더 간결하고 유지보수하기 쉬운 구현으로 정리한다.

## Scope
- `check_runtime_shape.py`의 runtime wiring과 iterator helper를 단순화한다.
- repo-local test asset인 `tests/project_context/test_runtime_shape.py`의 setup 중복을 줄이고 contract-driven 실패 경로를 보강한다.
- 기능 의미는 유지하고 guardrail과 테스트가 계속 통과하는지 확인한다.

## Current State
- status는 completed다.
- `check_runtime_shape.py`는 `RuntimePaths`로 runtime boundary를 한 곳에 모으는 구조로 정리됐다.
- 테스트는 runtime/fixture helper와 contract-driven 실패 경로를 직접 보도록 다듬었다.
- latest validation: guardrail, `py_compile`, unit test 통과

## Next Step
- 없음

## Working Boundary
- declared read scope: `skills/project-context/scripts/**`, `tests/project_context/**`
- declared write scope: `skills/project-context/scripts/**`, `tests/project_context/**`
