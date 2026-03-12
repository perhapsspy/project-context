# Project Context Migration

- owner: worker-c
- started_at: 2026-03-10
- status: completed

## 목표
- `case-beta` legacy 문서를 `project-context` canonical 구조로 옮기고 분류 근거를 남긴다.

## Audit Map

| path | kind | current-or-stale | scope | target | note |
| --- | --- | --- | --- | --- | --- |
| `adr/0001-database.md` | ADR | current | project-wide | `MEMORY`, `REFERENCE` | 수용된 datastore 결론을 memory에 압축하고 reference에 현재 진실로 정리한다. |
| `docs/api/auth.md` | reusable doc | current | topic-scoped | `REFERENCE` | 재사용 가능한 인증 규칙은 reference에 두고 memory에는 중복 승급하지 않는다. |
| `tasks/login-bug.md` | task note | current-but-unresolved | task-local | `TASK` | Safari 로그인 조사 이력과 미확정 상태를 별도 task으로 유지한다. |
| `notes/misc.md` | uncertain note | stale-or-unknown | exploratory | `LEAVE` | 현재성 판단이 안 되는 잡노트라 source 위치에 남기고 canonical truth로 승격하지 않는다. |

## 현재 산출물 스냅샷
- `docs/memory.md`가 생성돼 있다.
- `docs/reference/api/auth.md`와 `docs/reference/data/database-choice.md`가 생성돼 있다.
- `docs/tasks/2026/03-10/login-bug-investigation/`가 생성돼 있다.
- `notes/misc.md`는 source 위치에 그대로 남아 있다.
