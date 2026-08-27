# project-context 스킬 개선안

이 문서는 케이스 조사 32건과 하위 에이전트 검토를 바탕으로, 배포 대상 `project-context` 스킬에 넣을 최소 개선 방향만 정리한다.

## 결론

`project-context`는 새 문서 종류를 늘릴 필요가 없다. 필요한 개선은 문서를 만들기 전 판단과 문서별 역할 경계를 더 선명하게 하는 것이다.

우선순위는 다음 4개다.

- `docs/reference/**`를 코드 색인이나 구현 지도처럼 쓰지 않게 한다.
- 새 작업 문서나 기준 문서를 만들기 전에 기존 기준 문서와 현재 담당 표면을 먼저 찾게 한다.
- `BRIEF.md`, 작업 루트 문서, 로그, `working/`, `archive/` 사이에서 현재 상태와 증거가 섞이지 않게 한다.
- 스킬/상시 지침/설치본을 바꾸는 작업은 실제 사용되는 사본까지 확인하고 닫게 한다.

## 반복 문제

### 기준 문서 풍화

`docs/reference/**`가 현재 믿고 쓸 기준이 아니라 코드 위치 목록, 구현 흐름, 과거 조사 경과를 담는 표면으로 변하기 쉽다.

근거 케이스:

- `ops-infra-runbook-index.md`
- `ops-infra-tailscale-access-rule.md`
- `edge-agent-edgecommandsse-legacy.md`
- `patch-fielder-di1850-direct-port-doc-owners.md`
- `task-csap-progress-workflow.md`

### 기존 기준 문서 미확인

기존 기준 문서나 현재 담당 문서를 찾기 전에 새 문서나 외부 페이지를 만들어 상태가 갈라진다.

근거 케이스:

- `backoffice-di1865-notion-current-state.md`
- `issue-tracker-initial-doc-surface.md`
- `patch-fielder-registrystat-task-shell.md`

### 현재 상태와 증거 혼합

`BRIEF.md`, 작업 루트 문서, `TODO.md`가 현재 상태 대신 이력, 증거, 삭제된 설명, 닫힌 판단 근거를 품는다.

근거 케이스:

- `project-context-brief-correction-boundary.md`
- `patch-fielder-di1850-parity-retriage.md`
- `edge-agent-payload-host-gates.md`
- `ops-infra-patchagent-guardrails.md`

### 인계와 닫힘 조건 부족

큰 세션이나 여러 저장소 작업에서 다음 세션이 어디서 시작해야 하는지, 어떤 환경/동기화/검증 상태가 참인지 빠진다.

근거 케이스:

- `backoffice-di1866-worktree-handoff.md`
- `edge-agent-staging-handoff.md`
- `edge-agent-next-readiness-restart.md`
- `edge-agent-completion-audit-gate.md`
- `ops-infra-stale-local-task-docs.md`

### 호출 조건과 설치본 차이

스킬 본문을 고쳐도 실제 호출 조건이나 설치본이 바뀌지 않아, 문서와 실행 상태가 어긋난다.

근거 케이스:

- `project-context-trigger-review-install-sync.md`
- `perhapsspy-skill-trigger-audit-install-drift.md`
- `structure-first-trigger-description.md`
- `structure-first-docs-trigger-broadening.md`
- `tighten-docs-rename-publish-install.md`

## 제안

### 1. 설명 문구 변경 보류

현재 설명은 이미 재개, 인계, 긴 저장소 작업, 작업 개요, 로그, 기준 메모를 담고 있다. 설명 문구를 넓히면 일반 문서 정리나 `AGENTS.md`/README 연결 작업까지 과하게 호출될 수 있다.

판단:

- 지금은 스킬 설명 문구를 바꾸지 않는다.
- 호출 범위 누락이 다시 반복되고 실제 점검 기준이 생기면 현재 문서와 낡은 문서 정리 정도만 좁게 검토한다.
- 저장소 안 연결, 인계 표면 같은 표현은 기존 설명이나 다른 스킬 소유 범위와 겹치므로 후보에서 뺀다.

### 2. 기준 문서 승격 규칙 추가

`docs/reference/**` 규칙에 아래 판단을 추가한다.

스킬에 넣을 뜻:

```md
- `docs/reference/**`는 코드 색인이나 현재 구현 지도가 아니라, 다음 작업에서도 믿고 쓸 현재 기준만 맡는다. 파일 경로는 기준을 이해하거나 현재 담당을 다시 확인하는 데 필요한 최소한만 쓴다. 구현 탐색용 목차, 긴 파일 목록, 조사 경과, 검증 로그는 작업의 `working/`이나 로그에 둔다.
- 기준 문서로 승격하기 전, 그 내용이 다른 작업에서도 재사용될 현재 규칙인지 확인한다. 불확실하거나 이번 작업에만 필요한 내용은 작업 문서에서 시작한다.
```

효과:

- 기준 문서 풍화를 줄인다.
- 코드 경로 사용을 전면 금지하지 않고, 담당 확인에 필요한 최소 경로는 허용한다.

### 3. 기존 project-context 담당 표면 먼저 찾기

`Operating Model` 앞부분에 작업 문서나 기준 문서를 만들기 전 확인을 더 선명하게 둔다.

스킬에 넣을 뜻:

```md
새 작업 문서나 기준 문서를 만들기 전에 같은 현재 상태를 이미 맡은 `project-context` 표면이 있는지 확인한다. 기준 출처가 코드, API, 설정, 테스트, 또는 사용자가 명시한 외부 담당 표면에 있으면 그 상태를 복제하지 말고 그 표면으로 연결한다.
```

효과:

- 기존 작업 문서/기준 문서가 있는데 새 문서를 만드는 문제를 줄인다.
- 코드 확인 금지로 읽히지 않게 한다.

### 4. 작업 루트 문서 역할 판정 강화

`Task Root Ownership`에 작업 루트 문서의 역할 판정을 더 직접적으로 둔다.

스킬에 넣을 뜻:

```md
- 작업 루트의 마크다운 파일은 현재 기준 문서, 연결 문서, 열린 대기열, 인계 묶음으로 유지한다. 증거, 초안, 낡은 문서는 루트 마크다운에 두지 말고 로그, `working/`, `archive/`로 보낸다.
- 열린 관문, 닫힌 증거, 과거 판단 근거를 상태 표시 없이 한 현재 상태 표면에 섞지 않는다.
```

효과:

- `TODO.md`와 작업 루트 문서가 상태 덤프가 되는 문제를 줄인다.
- 루트 마크다운이 증거/보관 표면처럼 읽히는 오해를 피한다.

### 5. 인계와 완료 전 확인 보강

`Final Gates`에 의미 품질을 보장한다고 쓰지 말고, 닫힘 전 최소 확인만 추가한다.

스킬에 넣을 뜻:

```md
- 인계나 문서 묶음을 완료라고 하기 전 `git status --short`로 미추적 작업 파일을 확인하고, 저장소 전용 문서/묶음 검사가 있으면 실행한다.
```

효과:

- 미추적 파일과 검사 누락으로 문서 묶음이 닫히지 않는 문제를 줄인다.
- runtime-shape 한계 설명은 이미 배포 대상 스킬에 있으므로 반복하지 않는다.

### 6. 스킬 유지보수 닫힘 조건

`Final Gates`나 별도 짧은 문장으로 스킬 유지보수 작업에만 적용되는 닫힘 조건을 둔다.

스킬에 넣을 뜻:

```md
- 이 스킬이나 설치된 다른 스킬을 바꾸는 작업에서는 저장소 사본 수정만으로 실제 동작이 바뀌었다고 보지 않는다. 설치본/실행본을 확인하거나 설치 동기화가 범위 밖임을 남긴다.
```

효과:

- 저장소 문서와 실제 호출 상태가 어긋나는 문제를 줄인다.

## 넣지 말아야 할 것

- 모든 읽기 전용 질문에 작업 루트를 만들게 하는 규칙.
- 모든 문서 수정에 `HANDOFF.md`, `PLAN.md`, backlog를 강제하는 규칙.
- 기준 문서에서 코드 경로를 전면 금지하는 규칙.
- `AGENTS.md`, `structure-first-docs`, `tighten-docs`가 맡는 일반 문서 구조화 규칙을 `project-context`에 반복하는 것.
- runtime-shape 검사로 문서 의미 품질까지 보장한다고 쓰는 것.
- 스킬 수정 시 자동 설치 동기화까지 강제하는 것.

## 반영 순서

1. `skills/project-context/SKILL.md`에 기준 문서 승격 규칙과 기존 `project-context` 담당 표면 확인만 먼저 넣는다.
2. README, 방향 문서, migration 스킬과 중복되는지 확인한다.
3. 케이스 3-4개에 실제 적용해 본다.
   - `backoffice-di1865-notion-current-state.md`
   - `ops-infra-runbook-index.md`
   - `patch-fielder-di1850-parity-retriage.md`
   - `project-context-trigger-review-install-sync.md`
4. `python3 -m unittest discover -s tests -p 'test_*.py'`를 실행한다.
5. `python3 skills/project-context/scripts/check_runtime_shape.py`를 실행한다.
6. 실제 설치본 동기화가 필요한 변경이면 설치본까지 직접 확인한다.

## 하위 에이전트 리뷰 반영

하위 에이전트 리뷰에서 공통으로 지적한 내용은 세 가지였다.

- 설명 문구를 넓히면 `structure-first-docs`, `AGENTS.md` 편집, 일반 문서 정리까지 과하게 호출될 수 있다.
- 기준 문서 풍화를 막는 규칙은 필요하지만, 코드 경로 확인 자체를 금지하면 실제 담당 표면을 잃는다.
- 작업 루트 문서를 증거 보관소처럼 쓰지 말라는 규칙은 필요하지만, 문서 종류를 새로 늘리거나 모든 작업에 인계를 강제하면 안 된다.

이 리뷰를 반영해 설명 문구 변경은 보류했고, 첫 반영 후보를 기준 문서 승격 규칙과 기존 담당 표면 확인으로 줄였다.

## 현재 판단

가장 먼저 반영할 항목은 기준 문서 승격 규칙과 기존 `project-context` 담당 표면 먼저 찾기다. 이 두 항목이 이번 케이스 조사에서 가장 자주 드러났고, 기존 스킬의 방향을 크게 바꾸지 않으면서 문서 어긋남을 줄일 가능성이 높다.

설명 변경, 작업 루트 역할 열거 확장, runtime-shape 한계 문장 반복은 이번 반영 후보에서 제외한다.
