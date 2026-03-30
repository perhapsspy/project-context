# Migration Fixture Harness

## Goal
- `project-context-migration` dogfood 결과를 repo-local 반복 검증 자산으로 고정한다.

## Scope
- legacy input fixture와 migrated good/bad fixture를 `tests/project_context_migration/fixtures/` 아래로 복제한다.
- fixture를 검사하는 contract-driven test를 추가한다.
- 메인 guardrail와 unit test를 다시 통과시킨다.

## Current State
- status는 completed다.
- legacy fixture는 아직 `project-context` 계약을 만족하지 않는다고 검증된다.
- migrated good fixture는 통과하고 migrated bad fixture는 형식 drift로 실패하도록 고정했다.
- latest validation: repo guardrail, unittest 통과

## Next Step
- 없음

## Working Boundary
- declared read scope: `skills/project-context-migration/**`, `tests/project_context_migration/**`
- declared write scope: `tests/project_context_migration/**`
