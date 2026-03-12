# Migration Fixture Harness

- owner: ai
- started_at: 2026-03-10
- status: done

## 목적
- `project-context-migration` dogfood 결과를 repo-local 반복 검증 자산으로 고정한다.

## 실행 범위
- legacy input fixture와 migrated good/bad fixture를 `tests/project_context_migration/fixtures/` 아래로 복제한다.
- fixture를 검사하는 contract-driven test를 추가한다.
- 메인 guardrail와 unit test를 다시 통과시킨다.

## 성공 기준
- legacy fixture는 아직 `project-context` 계약을 만족하지 않는다고 검증된다.
- migrated good fixture는 통과하고 migrated bad fixture는 형식 drift로 실패한다.
- 분류 기대치가 테스트로 고정된다.
