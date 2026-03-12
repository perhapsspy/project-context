**2026-03-10**
- `case-alpha`, `case-alpha-rerun`, `case-beta` dogfood 결과를 legacy/good/bad fixture로 정리할 계획을 세웠다.
- repo-local test 자산으로 옮겨도 되는지 현재 tests 구조와 guardrail import 방식을 다시 확인했다.
- fixture를 `tests/project_context_migration/fixtures/project_context_migration/` 아래로 복제했다.

**2026-03-10**
- `tests/project_context_migration/test_migration_fixtures.py`를 추가해 legacy input은 실패하고, migrated bad는 형식 drift로 실패하며, migrated good 둘은 통과하는 contract-driven 검증을 고정했다.
- `python3 -m py_compile`, 신규 fixture test 5건, 전체 unittest 33건, 메인 guardrail까지 다시 통과시켰다.
