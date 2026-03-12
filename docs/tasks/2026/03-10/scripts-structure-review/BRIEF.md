# Scripts Structure Review

- owner: ai
- started_at: 2026-03-10
- status: done

## 목적
- `skills/project-context/scripts`의 파이썬 스크립트와 테스트를 구조와 contract-driven 관점에서 다시 보고, 더 간결하고 유지보수하기 쉬운 구현으로 정리한다.

## 실행 범위
- `check_runtime_shape.py`의 runtime wiring과 iterator helper를 단순화한다.
- repo-local test asset인 `tests/project_context/test_runtime_shape.py`의 setup 중복을 줄이고 contract-driven 실패 경로를 보강한다.
- 기능 의미는 유지하고 guardrail과 테스트가 계속 통과하는지 확인한다.

## 현재 산출물 스냅샷
- `check_runtime_shape.py`는 `RuntimePaths`로 runtime boundary를 한 곳에 모으고, `main()`/`run_runtime_shape_checks()` 시그니처를 줄인 상태다.
- `iter_memory_candidate_lines()`와 `iter_memory_files()`는 list 구축 대신 iterator를 사용한다.
- repo-local test asset `tests/project_context/test_runtime_shape.py`는 runtime/pack fixture helper와 contract-driven 실패 경로를 포함한다.
- skill 사용 시 직접 쓰는 스크립트는 `skills/project-context/scripts/`에 남고, 안정성을 위한 테스트는 repo root `tests/`로 분리돼 있다.
- guardrail, `py_compile`, unit test가 통과한 상태다.
