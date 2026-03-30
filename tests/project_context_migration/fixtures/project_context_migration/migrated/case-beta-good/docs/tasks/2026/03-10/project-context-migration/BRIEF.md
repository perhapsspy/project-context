# Project Context Migration

## 목표
- `case-beta` legacy 문서를 `project-context` canonical 구조로 옮기고 분류 근거를 남긴다.

## Audit Map

| path | kind | current-or-stale | scope | target | note |
| --- | --- | --- | --- | --- | --- |
| `AGENTS.md` | repo-local guidance | current | repo-local | `LEAVE` | 작업 기본 규칙은 source surface가 계속 소유한다. |
| `adr/0001-database.md` | ADR | current | project-wide | `REFERENCE` | 수용된 datastore 결론은 canonical reference에 정리한다. |
| `docs/api/auth.md` | reusable doc | current | topic-scoped | `REFERENCE` | 재사용 가능한 인증 규칙은 reference에 둔다. |
| `tasks/login-bug.md` | task note | current-but-unresolved | task-local | `TASK` | Safari 로그인 조사 이력과 미확정 상태를 별도 task으로 유지한다. |
| `notes/misc.md` | uncertain note | stale-or-unknown | exploratory | `LEAVE` | 현재성 판단이 안 되는 잡노트라 source 위치에 남기고 canonical truth로 승격하지 않는다. |

## 현재 산출물 스냅샷
- `docs/reference/api/auth.md`와 `docs/reference/data/database-choice.md`가 생성돼 있다.
- `docs/tasks/2026/03-10/login-bug-investigation/`가 생성돼 있다.
- `AGENTS.md`는 root에 남아 있다.
- `notes/misc.md`는 source 위치에 그대로 남아 있다.

## 현재 상태
- status는 done이다.
- blockers: 없음
- latest validation: migration output snapshot

## Next Step
- 없음

## Working Boundary
- declared read scope: migration audit, legacy 입력 4건
- declared write scope: docs/reference/**, docs/tasks/**
