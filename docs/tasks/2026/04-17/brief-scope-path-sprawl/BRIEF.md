# Brief Scope Path Sprawl

## Goal
- `BRIEF.md`의 `Scope`가 touched-file inventory로 길어지지 않게 contract와 gardening check를 보강한다.

## Scope
- `Scope`를 짧은 작업 경계 요약으로 다시 고정한다.
- exact path inventory는 필요할 때만 `Working Boundary`로 미루는 기준을 정리한다.
- repo 안의 representative `BRIEF.md` 예시도 같은 기준으로 맞춘다.

## Current Understanding
- 현재 이 레포에는 `BRIEF.md`를 자동 생성하는 코드가 없고, shipped guidance와 live example이 실제 작성 습관을 만든다.
- 따라서 재발 방지는 contract wording과 warning-grade gardening check를 같이 두는 편이 더 적합하다.
- `Scope`는 reopen entrypoint의 boundary hint면 충분하고, 상세 파일 나열은 같은 정보를 더 비싸게 반복하는 경우가 많다.
- 다만 현재 evidence만으로는 `Scope` 자체를 default skeleton에서 내릴 만큼의 반복 drift가 증명되지는 않았고, 문제는 섹션 존재보다 path-list 오용 쪽에 가깝다.

## Current State
- status는 completed다.
- shipped `project-context`와 `project-context-migration`는 `Scope`를 짧은 boundary summary로 제한하고, exact path inventory는 optional `Working Boundary`로 미루게 정리됐다.
- repo-local direction, review, dogfood 문서도 같은 판정선으로 맞췄다.
- gardening check는 `Scope`에 path-only bullet이 5개 이상 쌓이면 `scope-path-list-sprawl` info finding으로 알려준다.
- representative task `BRIEF.md` 예시 3건도 summary-level `Scope`로 다시 맞췄다.
- 추가 재검토 결과, `Scope`는 default skeleton에 남기고 file-list sprawl만 막는 현재 계약을 유지하는 편이 evidence와 drift 비용 모두에 더 맞는다고 정리했다.
- latest validation: `python3 -m unittest discover -s tests -p 'test_*.py'`, `python3 skills/project-context/scripts/check_runtime_shape.py`, `python3 skills/project-context/scripts/check_gardening.py`, `python3 skills/project-context/scripts/task_logs.py worklog check --task-root docs/tasks/2026/04-17/brief-scope-path-sprawl`, `python3 skills/project-context/scripts/task_logs.py decision check --task-root docs/tasks/2026/04-17/brief-scope-path-sprawl`

## Next Step
- 없음

## Working Boundary
- declared read scope: `AGENTS.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/skill-direction.md`, `docs/review-method.md`, `docs/dogfood-method.md`, `skills/project-context/scripts/check_gardening.py`, `tests/project_context/test_gardening.py`, representative task `BRIEF.md` examples, `docs/tasks/2026/04-17/brief-scope-path-sprawl/**`
- declared write scope: `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/skill-direction.md`, `docs/review-method.md`, `docs/dogfood-method.md`, `skills/project-context/scripts/check_gardening.py`, `tests/project_context/test_gardening.py`, representative task `BRIEF.md` examples, `docs/tasks/2026/04-17/brief-scope-path-sprawl/**`
