# Context Surface Ownership Improvement

## 결론

이번 개선의 핵심은 "문서를 덜 쓰게 하기"가 아니라 "문서 표면의 소유권을 계속 재분류하게 하기"다.

최근 Conalog dogfood에서 반복된 문제는 에이전트가 문서를 하나 만들면 그 문서에 계속 붙이고, 작업이 진행된 뒤에도 root/current, `working/`, logs, `archive/`로 다시 나누지 않는 습관이었다. 그 결과 `BRIEF.md`가 조사 기록, 구현 inventory, 검증 결과, 제품 정책, stale plan까지 품고 커지거나, task root가 active 문서와 완료/초안/evidence 문서가 섞인 문서 창고가 됐다.

## 목표 상태

- task root에는 active/current canonical 문서와 router만 둔다.
- `working/`에는 진행 중 초안, probe, staging evidence, 아직 결정되지 않은 계획을 둔다.
- `logs/`에는 chronology, 실행 기록, retries, dated evidence를 둔다.
- `archive/`에는 완료, 폐기, 대체, stale 문서를 둔다.
- 문서를 새로 만들거나 크게 수정한 뒤에는 그 문서와 각 단락이 아직 현재 표면에 속하는지 다시 확인한다.

## 선행 맥락

- `docs/tasks/2026/03-30/task-surface-reduction/`은 `BRIEF.md + logs` 중심 모델로 surface를 줄였다.
- `docs/tasks/2026/04-23/brief-log-bloat-guardrails/`는 `BRIEF.md`와 logs 과대화를 막는 방향을 잡았다.
- 이번 follow-up은 그 위에 "root/current/working/log/archive 소유권"과 "큰 task/작은 task의 다른 문서 계약"을 더한다.

## 확인된 실패 유형

### 1. `BRIEF.md`가 구현 명세가 되는 경우

대표 dogfood 사례:

- `backoffice/docs/tasks/2026/05-08/inventory-items/BRIEF.md`
- `patch-fielder/docs/tasks/2026/05-11/di-1812-plant-selector-plan/BRIEF.md`
- `patch-map-flutter/docs/tasks/2026/05-04/code-quality-performance-scan/BRIEF.md`

증상:

- `Current Understanding`이 데이터 계약, UI 정책, 조사 결과를 장문으로 품는다.
- `Current State`가 resumable state가 아니라 구현 inventory로 변한다.
- working note에 있어야 할 초기 조사나 benchmark 숫자가 brief에 올라온다.

### 2. Root가 current 표면이 아니라 문서 창고가 되는 경우

대표 dogfood 사례:

- `edge-agent-workspace/docs/tasks/2026/05-13/edge-agent-system-design/`
- `ops-infra/docs/tasks/2026/05-27/oncheon-std50kc-raw-recovery/`
- `backoffice/docs/tasks/2026/03-19/fieldwork/`

증상:

- root markdown이 늘고 어떤 문서를 먼저 읽어야 하는지 불분명해진다.
- 완료된 cleanup plan, obsolete PR 흐름, evidence summary, runbook draft가 current root에 남는다.
- 나중에 사용자가 "한 일은 archive, 작업 중은 working"이라고 다시 지시해야 정리된다.

### 3. Current 문서가 history dump가 되는 경우

대표 dogfood 사례:

- `ops-infra` PatchAgent rollout status 정리
- `edge-agent-workspace` pre-canary doc consolidation

증상:

- active status 문서가 날짜별 업데이트 횟수, 과거 retry, 이전 PR 공유 흐름을 함께 품는다.
- 최신 판단을 보려고 열었는데 chronology를 먼저 읽어야 한다.

## Change Set

### 1. `BRIEF.md` 섹션 정책 재정의

`BRIEF.md`는 compact resume card다. 기본 섹션은 유지하되 의미를 더 좁힌다.

| Section | 판단 | 개선 규칙 |
| --- | --- | --- |
| `Goal` / `Intent` | 유지 | stable task target만 쓴다. 배경 설명을 붙이지 않는다. |
| `Scope` | 유지 | 1-3개 boundary만 쓴다. touched files, UI inventory, implementation list 금지. |
| `Current Facts` | 권장 | investigation/task facts 중 재개에 필요한 것만 쓴다. |
| `Current Understanding` | 제한 | 설계/제품 정책 dump로 커지기 쉬우므로 큰 task에서는 supporting doc으로 빼고, brief에는 결론만 둔다. |
| `Current State` | 유지 | 지금 재개하면 true인 상태만 쓴다. "무엇을 했다" 서술은 logs로 보낸다. |
| `Next Step` | active task에 유지 | nearest restart action 하나만 둔다. 완료 task는 `Reopen if ...` 형태를 허용한다. |
| `Working Boundary` | 제한 유지 | reopen cost를 낮추는 핵심 경로 최대 5개만 둔다. |

Additional rules:

- `BRIEF.md`에 검증 transcript, benchmark matrix, PR/release/deploy chronology, shell output, 상세 조사 결과를 넣지 않는다.
- `BRIEF.md`가 500 words를 넘으면 "왜 supporting doc/log/reference가 아닌가"를 재검토한다.
- 초기 조사에서 알게 된 것은 current fact로 살아남을 때만 brief에 남긴다.

### 2. Task root ownership 도입

작은 task:

- 기본 표면은 `BRIEF.md`, `logs/DECISIONS.md`, `logs/WORKLOG.md`다.
- 추가 표면은 이름보다 owner와 lifecycle이 명확할 때만 둔다.
- `PLAN.md`는 handoff가 실제로 필요한 경우, `working/`은 조사/초안이 실제로 있을 때처럼 역할이 분명할 때만 둔다.

큰 task:

- root에 `README.md`를 둘 수 있다.
- root 문서는 current canonical/router 역할만 한다.
- root 문서가 스캔하기 어려워지면 `README.md`에 문서별 owner를 적거나 supporting docs를 폴더로 내려야 한다.
- 완료/대체된 문서는 root에 두지 않고 `archive/`로 보낸다.

권장 큰 task layout:

```text
BRIEF.md
README.md
<current-canonical>.md
logs/
working/
archive/
research/            # 필요할 때만
```

### 3. Cleanup habit을 skill workflow에 넣기

문서를 만들거나 수정한 뒤 다음 질문을 반복한다.

- 이 단락은 현재 재개에 필요한가?
- 아직 결정되지 않은 초안이면 `working/`인가?
- 실행 기록이면 `logs/WORKLOG.md`인가?
- 판단 변경이면 `logs/DECISIONS.md`인가?
- 완료/대체/stale이면 `archive/`인가?
- root에 남은 문서는 current canonical 또는 router인가?

이 질문은 final gate가 아니라 작업 중 반복되는 maintenance step이어야 한다.

### 4. Helper 개선 후보

`task_logs.py`는 로그 block shape만 관리하지 말고, brief cleanup prompt를 제공할 수 있다.

Candidate command:

```text
task_logs.py brief check --task-root <task-root>
```

확인 항목:

- 섹션이 허용 목록에 있는지.
- word count가 soft limit를 넘는지.
- `Current State`가 progress narration처럼 보이는지.
- `Next Step`이 backlog처럼 보이는지.
- `Working Boundary`가 path inventory처럼 보이는지.

### 5. Reference 승격 기준 명확화

- 한 번 쓰는 조사 결과: task `working/` 또는 logs.
- 현재 작업의 resume state: `BRIEF.md`.
- 반복해서 재사용되는 운영 절차/route owner/validation bundle: `docs/reference/**`.
- 과거 decision 변천: `logs/DECISIONS.md`.
- 완료된 proposal/review/draft: `archive/`.

## Suggested Implementation Slices

1. Shipped skill wording only
   - `skills/project-context/SKILL.md`
   - `docs/skill-direction.md`
   - examples if wording drift appears

2. Brief helper command
   - `skills/project-context/scripts/task_logs.py`
   - tests for oversized brief, progress narration, root markdown budget

3. Dogfood cleanup
   - review selected Conalog examples
   - do not rewrite those repos unless separately requested

## Acceptance Criteria

- 새 task의 `BRIEF.md`만 읽고 현재 재개 상태를 알 수 있다.
- root 문서만 봐도 active/current canonical이 무엇인지 알 수 있다.
- 초기 조사와 진행 중 초안은 root가 아니라 `working/`에 있다.
- 완료/대체/stale 문서는 `archive/`에 있다.
- chronology와 validation detail은 `logs/WORKLOG.md`에 있다.
- checker가 legacy debt와 현재 task 문제를 구분한다.
- 큰 task는 문서가 많아도 router/owner가 명확하고, 작은 task는 불필요한 plan/report를 만들지 않는다.
