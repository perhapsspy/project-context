# Backoffice Patch-Fielder Dogfood Review

## Goal
- `../conalog/backoffice`와 `../conalog/patch-fielder`의 `project-context` 운용 상태를 실제 docs surface 기준으로 점검한다.
- 이 dogfood 결과를 바탕으로 `project-context`의 다음 개선 방향을 정리한다.
- 개선 방향을 코어 원칙, repo-specific follow-up, optional gardening checker 설계로 나눠 남긴다.

## Scope
- mature repo dogfood evidence를 바탕으로 `project-context` contract와 gardening 기준을 점검한다.
- shipped skill, repo-local direction/review/dogfood 문서, gardening check를 같은 판정선으로 맞춘다.
- same-turn drift가 보이면 현재 task `BRIEF.md`도 함께 바로잡는다.
- `../conalog/backoffice/docs/**`
- `../conalog/patch-fielder/docs/**`
- 외부 비교용 공식 문서 몇 개

## Current Understanding
- `project-context`의 코어 계약은 여전히 유효하다. `reference`와 dated `task`를 분리하고 `BRIEF.md`를 reopen entrypoint로 두는 방향은 실제 repo에서도 통한다.
- mature repo에서는 legacy surface와 task-local docs가 쉽게 누적돼 `BRIEF` 단일 entrypoint 약속이 흐려진다.
- 새로 도입한 repo에서는 shape가 훨씬 잘 유지되지만, backlog 같은 useful extension이 코어 밖에서 repo-local overlay로 붙는다.
- 다음 진화는 코어 확장보다 long-running drift를 줄이는 companion surface와 gardening loop 쪽이 더 맞다.

## Current State
- `backoffice`와 `patch-fielder`의 AGENTS, reference overview, representative task, backlog/task drift를 읽고 비교했다.
- runtime shape checker를 두 repo에 실행해 실제 실패 항목을 확인했다.
- 개선 원칙 초안, repo follow-up 제안, next-gen gardening checker 설계를 task-local docs로 정리했다.
- 추가로 별도 세션에서 제안된 `fieldwork` 정리 아이디어를 실제 폴더 구조에 대조해 검토했고, long-running task 안에서 `canonical root + working lane + archive/logs`처럼 root current docs와 임시 작업 메모를 나누는 optional pattern을 연구 결과에 반영했다.
- shipped `skills/project-context/SKILL.md`를 `Purpose / Use / Core Bias / Contract / Operating Model / Anti-Patterns / Guardrail Check / Final Gates` 구조로 재편했다.
- `docs/skill-direction.md`도 `Purpose / 역할 경계 / Core Bias / Contract Direction / Spec Shape Direction / Guardrail Direction / Evolution Direction` 구조로 다시 정리했다.
- `skills/project-context-migration/SKILL.md`도 같은 spec shape로 재편했다.
- `skills/project-context/scripts/check_gardening.py`를 추가해 `empty-task-dir`, `legacy-surface-respawn`, `task-extra-doc-growth`, `root-overlay-mixing` 4개 warning/info check를 구현했다.
- `tests/project_context/test_gardening.py`를 추가했고, gardening/runtime-shape/migration 관련 검증은 통과했다.
- gardening checker를 read-only로 `backoffice`, `patch-fielder`에 dogfood한 결과, `patch-fielder`는 `empty-task-dir` 1건만, `backoffice`는 recent `STATUS.md` 군집과 `fieldwork` doc-growth/root-mixing을 잡아 현재 heuristic이 의도한 수준의 drift를 대체로 포착했다.
- 이후 long-running task 개선을 이 레포 안에서만 마무리하기 위해, shipped `project-context`와 `project-context-migration`에 `working/`, `archive/`를 optional advanced guidance 예시로만 짧게 올리고, gardening checker suggestion도 같은 vocabulary로 맞췄다.
- 그 뒤 `docs/skill-direction.md`가 기준 문서보다 진행 문맥과 평가 루프를 섞는 방향으로 비대해졌다는 피드백을 반영해, 해당 문서를 what-why 중심의 기준 문서로 다시 썼다.
- 대신 이 레포의 로컬 리뷰 기준과 절차는 새 `docs/review-method.md`로 분리했고, `AGENTS.md`에서 그 경로를 바로 가리키게 했다.
- 추가로 `backoffice`의 `task-working-docs` 규칙을 다시 읽어, root에는 stable docs만 남기고 임시 실행 메모는 repo-local helper lane으로 빼며, 흡수 후 archive로 내리고, done/undone authority를 고정하는 원칙을 확인했다.
- 이를 반영해 shipped guidance와 gardening suggestion에서 long-running helper lane 예시는 `working/`으로 통일하고, 이 이름도 repo-local example일 뿐 required tree가 아니라는 쪽으로 문구를 다시 조정했다.
- 마지막으로 실제 dogfood loop를 재사용 가능한 로컬 자산 [`docs/dogfood-method.md`](../../../../dogfood-method.md) 로 정리하고, 현재 변경셋에 대해 activation/write/reopen/guardrail/drift pass를 한 번씩 실행한 결과를 [`DOGFOOD-RUN.md`](./DOGFOOD-RUN.md) 로 남겼다.
- 이 실행 중 현재 task `BRIEF.md`의 write scope와 일부 current state 설명이 stale해져 있음을 발견했고, 이번 턴에서 현재 기준으로 다시 맞췄다.

## Next Step
- long-running optional pattern을 여기서 더 강한 core contract로 올릴지, 현재의 optional advanced guidance 선에서 멈출지 결정한다.
- `legacy-surface-respawn`의 recent 기준을 유지할지, repo별 adoption date를 받는 모드가 필요한지 결정한다.
- 새로 정리한 dogfood method와 review method가 다음 shipped-skill 변경에서도 반복 사용 가능한지 다시 검증한다.

## Related Docs
- `IMPROVEMENT-PRINCIPLES.md`
- `REPO-FOLLOWUPS.md`
- `GARDENING-CHECKER-DESIGN.md`
- `../../../../review-method.md`
- `../../../../dogfood-method.md`
- `DOGFOOD-RUN.md`
- `../conalog/backoffice/docs/reference/conventions/task-working-docs.md`
- `../conalog/backoffice/docs/tasks/2026/03-30/project-context-docs-refresh/BRIEF.md`
- `../conalog/patch-fielder/docs/tasks/2026/03-31/project-context-contract-migration/BRIEF.md`

## Working Boundary
- declared read scope: `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/skill-direction.md`, `docs/review-method.md`, `docs/dogfood-method.md`, `AGENTS.md`, `skills/project-context/scripts/check_gardening.py`, `tests/project_context/test_gardening.py`, `../conalog/backoffice/docs/**`, `../conalog/patch-fielder/docs/**`, external official docs used for comparison, this task folder
- declared write scope: `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `docs/skill-direction.md`, `docs/review-method.md`, `docs/dogfood-method.md`, `AGENTS.md`, `skills/project-context/scripts/check_gardening.py`, `tests/project_context/test_gardening.py`, this task folder

## Latest Validation
- `python3 skills/project-context/scripts/check_runtime_shape.py`
- `python3 skills/project-context/scripts/check_gardening.py`
- `python3 -m unittest discover -s tests -p 'test_*.py'`
- `python3 skills/project-context/scripts/check_gardening.py --repo-root <backoffice-repo-root>`
- `python3 skills/project-context/scripts/check_gardening.py --repo-root <patch-fielder-repo-root>`
- 현재 전체 `unittest discover`는 latest `main`에서 들어온 `tests/project_context/test_task_logs.py`의 경로 구분자 기대치 때문에 macOS에서 실패한다.
