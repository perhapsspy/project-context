# Repo Follow-Ups

## Backoffice

### Current Read

- 장점
  - `AGENTS.md`와 `docs/reference/overview.md`가 좋은 entrypoint 역할을 한다.
  - `project-context-docs-refresh` 이후 새 contract를 의식적으로 다시 맞춘 흔적이 있다.
  - newer tasks에서는 `STATUS.md` 사용이 줄고 있다.

- 문제
  - task 141개 중 `STATUS.md`가 131개 남아 있다.
  - task top-level extra files가 143개라 legacy surface가 여전히 크다.
  - `fieldwork`처럼 장기 domain이 single task workspace 안에서 quasi-canonical area docs로 변한 사례가 있다.
  - `docs/tasks/2026/03-31/fieldwork/logs/WORKLOG.md`에 절대경로 검증 명령이 남아 checker fail을 만든다.

### Recommended Actions

1. Fix now
- `docs/tasks/2026/03-31/fieldwork/logs/WORKLOG.md`의 `/Users/...` 절대경로를 portable command로 교체한다.

2. Short-term
- `fieldwork`를 계속 single dated task로 유지할지, 아니면 future companion surface 후보로 따로 분리할지 결정한다.
- 최소한 `fieldwork` 안의 reusable rule은 `docs/reference/**`로 더 자주 승격하고, task 폴더에는 current operating state만 남기도록 줄인다.
- `fieldwork`를 그대로 유지한다면 task root 역할을 다시 나눈다.
  - canonical root 유지 후보: `BRIEF.md`, `MODEL.md`, `CONTRACTS.md`, `SYSTEM_BOUNDARIES.md`, `EXECUTION.md`, `ACTIONS.md`
  - active overlay 후보: `AUTHORING_REWORK_PLAN.md`, `IMPROVEMENT_PLAN.md`, `IMPLEMENTATION_BACKLOG.md`, 일부 adoption/chat-engine migration 문서
  - validation/history 후보: `REALTIME_POLICY.md`, `EMPTY_STATE_FLOW.md`, `validation/MULTIUSER_VALIDATION.md`, `product/DEMO_SITE_ANALYSIS.md`
  - active overlay는 `working/` 같은 하위 lane으로 내리고, 끝난 문서는 canonical 반영 후 `archive/`로 보낸다.
  - `working/` 문서는 짧은 current-state note로 유지하고, 흡수 뒤에는 `working/archive/`나 task `archive/`로 내린다.

3. Medium-term
- legacy `STATUS.md`는 일괄 제거보다 reopen 가치가 높은 오래된 task부터 순차 정리한다.
- 새 task에서 `STATUS.md`를 다시 만들지 않는지 periodic gardening check로 감시한다.

4. Optional
- 최근 reopen 빈도가 높은 task만 골라 `BRIEF.md`를 current-overview 기준으로 손보고, `STATUS.md`는 참고용 legacy file로 놔두거나 제거한다.

## Patch-Fielder

### Current Read

- 장점
  - migration 이후 core contract 유지력이 높다.
  - `STATUS.md`가 0개다.
  - task 29개 기준 extra top-level file이 5개뿐이라 task sprawl이 작다.
  - `docs/README.md`가 backlog/work-board extension을 깔끔하게 닫는다.

- 문제
  - `docs/tasks/2026/04-07/ios-blank-page-compat/`가 core files 없이 비어 있어 checker fail을 만든다.
  - backlog surface는 유용하지만 repo-local extension이라 향후 contract drift 설명이 늘어날 수 있다.
  - `AGENTS.md`, `docs/README.md`, `docs/reference/overview.md`의 역할 분리가 지금은 괜찮지만 중복이 더 늘면 second instruction surface가 될 수 있다.

### Recommended Actions

1. Fix now
- `docs/tasks/2026/04-07/ios-blank-page-compat/`를 실제 task로 완성하거나 폴더를 제거한다.

2. Short-term
- `docs/README.md`는 backlog/work-board 같은 repo-specific extension만 다루고, 코어 contract의 설명 복제는 계속 최소화한다.
- backlog 항목과 related task link가 끊기지 않도록 periodic review를 둔다.

3. Medium-term
- backlog surface의 유지 기준을 더 짧게 고정한다.
  - owner
  - evidence
  - next action
  - resolved task link

4. Optional
- patchmap 같은 hot area는 `docs/reference/patchmap/guide.md`에서 "first read set"을 더 압축해 cold-start cost를 줄인다.

## Cross-Repo Follow-Up

1. Portable sibling-repo references
- sibling repo를 가리킬 때 `/Users/...` 절대경로 대신 `../repo-name/...` 또는 `<sibling-repo>/...` placeholder를 우선한다.

2. Dogfood cadence
- mature repo 1개, newly-adopted repo 1개를 기준 샘플로 계속 같이 점검한다.
- 이번 pairing은 `backoffice`와 `patch-fielder`가 적절했다.

3. Success criteria
- core checker fail 0
- recent task에서 `STATUS.md` respawn 0
- empty task dir 0
- long-running domain task는 계속 task로 둘지 분리할지 명시 decision 존재
- long-running task를 유지한다면 task root에는 canonical current docs만 남고 active rework는 별도 overlay lane으로 분리됨
- 새 overlay/workitem 문서는 `structure-first-docs`와 크게 어긋나지 않는 section vocabulary를 사용함
