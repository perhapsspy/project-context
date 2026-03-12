# Project Context Migration

- owner: worker-a
- started_at: 2026-03-10
- status: done

## 목적

- `case-alpha`의 legacy 문서를 `project-context` 구조로 분류하고 canonical 파일을 만든다.
- migration 판단 근거를 이 task에 감사 표로 남긴다.

## 감사 범위

- `docs/system.md`
- `docs/user-guide.md`
- `runbooks/deploy.md`
- `notes/2026-02-14-auth-spike.md`

## Audit Map

| path | kind | current-or-stale | scope | target | note |
| --- | --- | --- | --- | --- | --- |
| `docs/system.md` | system note | current | reusable | `REFERENCE -> docs/reference/system-overview.md` | 현재 시스템 사실만 담고 있고 운영 상세는 별도 runbook으로 분리되어 있다. |
| `docs/user-guide.md` | product doc | current | human-facing | `LEAVE` | 최종 사용자용 제품 문서라 AI project memory로 옮기지 않는다. |
| `runbooks/deploy.md` | runbook | current | reusable | `REFERENCE -> docs/reference/deploy-runbook.md` | 현재 배포 절차의 current truth다. |
| `notes/2026-02-14-auth-spike.md` | spike note | current-but-unadopted | task-local | `WORK -> docs/tasks/2026/02-14/auth-spike/` | 탐색 메모이며 아직 production-ready가 아니고 다음 릴리스 이후 재검토가 필요하다. |

## 현재 산출물 스냅샷

- `docs/reference/system-overview.md`와 `docs/reference/deploy-runbook.md`가 canonical reference로 존재한다.
- `docs/memory.md`에는 프로젝트 전역에서 자주 필요한 사실만 압축돼 있다.
- 미확정 auth spike는 별도 task으로 남아 있고 legacy 원본도 그대로 유지된다.
