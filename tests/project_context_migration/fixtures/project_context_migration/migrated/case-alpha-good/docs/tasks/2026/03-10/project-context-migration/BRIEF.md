# Project Context Migration

## 목표

- `case-alpha` legacy 문서를 `project-context` 구조로 정리한다.
- canonical current owner는 target tree에 두고, `LEAVE` 대상만 source surface의 현재 owner로 남긴다.

## Audit Map

| path | kind | current-or-stale | scope | target | note |
| --- | --- | --- | --- | --- | --- |
| `docs/system.md` | system notes | current | project-wide | `REFERENCE -> docs/reference/system/system-overview.md` | 현재 시스템 상수는 canonical reference로 정리한다. |
| `runbooks/deploy.md` | runbook | current | operational | `REFERENCE -> docs/reference/deployment/deploy-runbook.md` | 현재도 유효한 배포 절차다. |
| `notes/2026-02-14-auth-spike.md` | spike note | exploratory | task-local | `TASK -> docs/tasks/2026/02-14/auth-spike/` | 미완료 탐색이므로 task으로 격리한다. |
| `docs/user-guide.md` | user-facing guide | current | product | `LEAVE` | 인간 대상 제품 문서이므로 agent working context로 옮기지 않는다. |
