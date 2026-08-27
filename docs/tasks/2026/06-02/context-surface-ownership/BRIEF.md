# Context Surface Ownership

## Goal

- Conalog dogfood에서 확인된 `BRIEF.md` 비대화와 task root/`working`/logs/`archive` 소유권 혼선을 줄이는 project-context 개선안을 구현 가능한 형태로 정리한다.

## Scope

- 포함: `BRIEF.md` 섹션 정책과 task root/`working`/logs/`archive` 소유권.
- 이번 구현 slice: shipped skill wording과 repo-local direction 정합화.
- 제외: checker/helper script 직접 수정과 Conalog dogfood 대상 repo 재작성.

## Current Facts

- 선행 task `task-surface-reduction`과 `brief-log-bloat-guardrails`는 `BRIEF.md + logs` 중심 모델과 bloat 방지 방향을 이미 잡았다.
- 최근 Conalog 회고에서는 문서를 만든 뒤 root/current, `working`, logs, `archive`로 다시 분류하지 않아 `BRIEF.md`와 root docs가 커지는 패턴이 반복 확인됐다.
- 큰 task와 작은 task에 같은 surface 계약을 적용하면 작은 task는 과문서화되고, 큰 task는 root에 current/evidence/draft/archive 성격 문서가 섞인다.

## Current State

- Wording-only slice is active: `skills/project-context/SKILL.md` and `docs/skill-direction.md` carry the ownership/lifecycle guidance, including the phase-boundary `BRIEF.md` rewrite rule.
- Commit `d853038` is pushed and the global `project-context` skill install has been refreshed.

## Next Step

- 완료. 새로운 실제 dogfood 근거가 생길 때 별도 task로 검토한다.

## Working Boundary

- `skills/project-context/SKILL.md`
- `skills/project-context/scripts/task_logs.py`
- `tests/project_context/**`
- `docs/tasks/2026/06-02/context-surface-ownership/**`
