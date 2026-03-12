# Project Context Migration

## 목표

- `case-alpha-rerun`의 legacy 문서를 `project-context` 구조로 정리한다.
- 원본 legacy 파일은 보존하고 canonical 파일만 추가한다.

## Audit Map

| path | kind | current-or-stale | scope | target | note |
| --- | --- | --- | --- | --- | --- |
| `docs/system.md` | system notes | current | project-wide | `REFERENCE -> docs/reference/system/system-overview.md`, `MEMORY -> docs/memory.md` | 현재 시스템 상수라 current reference state로 정리하고 핵심만 memory로 압축한다. |
| `runbooks/deploy.md` | runbook | current | operational | `REFERENCE -> docs/reference/deployment/deploy-runbook.md` | 현재도 유효한 배포 절차다. |
| `notes/2026-02-14-auth-spike.md` | spike note | exploratory | task-local | `TASK -> docs/tasks/2026/02-14/auth-spike/` | 미완료 탐색이므로 task으로 격리한다. |
| `docs/user-guide.md` | user-facing guide | current | product | `LEAVE` | 인간 대상 제품 문서이므로 project memory로 옮기지 않는다. |

## 적용 순서

1. migration audit task 생성
2. auth spike를 dated task로 정리
3. current reference state를 reference로 정리
4. project-wide working memory만 memory로 압축
