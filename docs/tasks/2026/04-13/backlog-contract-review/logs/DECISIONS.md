**2026-04-13**
- 현재 `project-context` 계약은 extra task-local doc을 허용하지만, immediate next step guidance와 더 큰 unresolved backlog의 경계는 충분히 선명하지 않았다.
- repo-level board를 코어 계약에 넣을지, 현재 문구를 유지할지, 아니면 `BRIEF`와 task-local backlog의 경계를 더 또렷하게 잡을지 중에서 정리가 필요했다.
- 코어는 작게 유지하고 backlog/carry-over 문제만 흡수한다. `BRIEF`는 immediate next step을 맡고, 여러 unresolved work가 생기면 역할이 분명한 task-local backlog 문서 하나로 넘긴다.
- 이렇게 하면 small-contract model을 유지하면서 surface 간 work state 중복을 줄이고, long-running task의 carry-over를 별도 board system 없이도 짧게 담을 수 있다.

**2026-04-13**
- earlier wording은 repo-level backlog surface를 계약 밖으로만 밀어냈지만, `patch-fielder` 사례는 아직 active task가 아닌 service improvement를 담는 얇은 repo backlog의 실제 수요를 보여 줬다.
- task-local backlog guidance만 둘지, 좁은 규칙의 optional repo-level overlay를 허용할지, 아니면 full status-board model을 되살릴지 판단이 필요했다.
- `docs/BACKLOG.md` 같은 optional repo-level backlog overlay는 허용하되 required tree에는 넣지 않고, current selectable improvement만 담으며 done 또는 irrelevant 상태가 되면 지우는 current-only surface로 둔다.
- 이렇게 하면 small core를 유지하면서도 operating-service repo가 future refactor를 짧게 parking할 수 있고, task progress mirroring이나 dead completed entry 누적도 피할 수 있다.

**2026-04-14**
- backlog guidance를 넣는 과정에서 `README`와 방향 문서가 내부 rationale과 operational detail을 흡수하기 시작했다.
- 확장된 문구를 유지할지, `README`만 줄일지, 아니면 `skill-direction`을 what-why 쪽으로 되돌리고 `SKILL.md`의 반복 backlog 문구도 함께 압축할지 정리가 필요했다.
- `README`는 user-facing intro로 되돌리고, `skill-direction`은 철학 문서로 다시 줄이며, shipped `SKILL.md`는 같은 계약을 더 짧게 말하도록 압축한다.
- 이렇게 하면 public docs가 각자 역할에 다시 맞고, `README`는 소개 페이지로 남으며, `skill-direction`은 로컬 rationale 메모로, `SKILL.md`는 단일 operational contract로 유지된다.

**2026-04-14**
- 문서 역할을 충분히 자르지 않고 README, direction, reference를 비슷한 밀도로 편집하면서 role drift와 언어 drift가 실제로 발생했다.
- 문서별 역할 가드를 AGENTS.md에 추가하지 않거나, 이번 반성을 로컬 작성 규칙으로 끌어올려 다음 편집 전에 먼저 문서 목적을 확인하게 만들 수 있다.
- AGENTS.md에 문서 역할 선판단, README/방향 문서/reference의 역할 차이, 로컬 문서 기본 언어를 먼저 점검하게 하는 규칙을 추가한다.
- 다음 편집부터는 같은 주제를 다루더라도 문서별 허용 정보 밀도와 톤을 먼저 맞추게 되어 README 오염, 방향 문서의 how-to drift, 로그 언어 혼선을 줄일 수 있다.

**2026-04-14**
- 리뷰 결과 repo backlog와 active task 사이의 handoff rule, README의 운영 가이드 문장, 방향 문서의 잔여 policy 톤이 남아 있었다.
- 현재 문구를 유지하거나, handoff rule을 shipped contract에 명시하고 README의 운영 습관 문장을 제거하며 방향 문서의 concrete owner 언급을 더 걷어낼 수 있다.
- repo backlog는 active task가 생기기 전 future work만 두고, 작업이 시작되면 active state를 task로 옮기며 repo backlog에서는 제거하거나 축약한다는 handoff rule을 shipped skill에 명시한다. README의 task_logs 안내는 제거하고, 방향 문서는 철학 문장만 남기도록 더 줄인다.
- 이렇게 하면 mirrored state 위험을 줄이고, README는 다시 intro 문서로, 방향 문서는 why 중심 메모로 더 분명해진다.

**2026-04-14**
- 브레인스토밍 결과 가장 작은 일관 구조는 README, direction, context-surfaces, SKILL의 4층 분리였고, SKILL은 surface-first contract와 단계형 operating model 조합이 가장 읽기 쉬웠다.
- 현재 문안을 유지하거나, README와 direction을 더 줄이고 context-surfaces를 inventory-only로 만들며 SKILL을 surface one-liner와 6단계 흐름 중심으로 다시 압축할 수 있다.
- README는 surface 정의 링크만 남기고, direction은 철학-only 안 2 형태로 다시 쓰며, context-surfaces는 inventory-only로 더 얇게 두고, SKILL은 surface-first contract와 단계형 operating model로 재구성한다.
- 이렇게 하면 문장 위치가 더 선명해지고, 각 파일이 맡는 정보 밀도가 줄어들며, SKILL도 계약과 흐름을 더 낮은 parsing cost로 전달할 수 있다.

**2026-04-14**
- Operating Model 브레인스토밍 결과, 현재 섹션은 실행 순서, owner 설명, overflow 규칙, fallback 규칙이 한데 섞여 있어 단계형 흐름으로 읽히지 않는 문제가 확인됐다.
- 현 구조를 유지하거나, Operating Model을 linear pipeline으로 다시 짜서 Read, Check, Decide, Write, Overflow, Fallback만 남길 수 있다.
- Operating Model을 6단계 linear pipeline으로 재구성한다. 표면 owner 설명은 Contract에 남기고, Operating Model은 순서와 전이 규칙만 맡게 한다.
- 이렇게 하면 에이전트가 단계별로 한 가지 판단만 하게 되어 parsing cost가 낮아지고, Contract와 Operating Model의 역할도 더 선명해진다.

**2026-04-14**
- SKILL.md 리뷰에서 repo backlog handoff 모호성, write 단계의 혼합 책임, task_logs.py 규칙 중복이 다시 지적됐다.
- 기존 문구 유지, handoff만 수정, handoff와 운영모델 구조를 함께 정리하는 방안을 비교했다.
- repo backlog handoff는 active 시 제거로 단정하고, Operating Model은 task shell 확보와 canonical write를 분리하며, task_logs.py 규칙은 계약부 한 곳을 정본으로 압축한다.
- mirrored state 여지를 줄이고, 에이전트가 lifecycle 판단과 write 순서를 더 선형적으로 읽게 하며, 로그 write 정책의 정본 위치를 분명히 한다.

**2026-04-14**
- SKILL.md 재리뷰에서 운영모델의 logs write 대상이 이름으로 드러나지 않고, task_logs.py 정본 규칙 한 줄이 과적재돼 있다는 지적이 나왔다.
- 현재 구조 유지, 운영모델에 로그 surface를 다시 명시, task_logs.py 규칙을 여러 문장으로 쪼개는 방안을 비교했다.
- Write canonical surfaces 단계에서 logs/DECISIONS.md와 logs/WORKLOG.md를 직접 명시하고, task_logs.py 정본 규칙은 기본 경로, append 기본값, PowerShell caveat로 분리한다.
- 운영 흐름만 읽는 에이전트도 로그 write 대상을 바로 알 수 있고, log write 정책의 정본 문장도 더 짧게 스캔할 수 있다.

**2026-04-14**
- 추가 리뷰에서 task_logs.py 정본 규칙이 세 줄에 나뉘어 있어 한 번에 스캔하기 어렵다는 미세 지적이 남았다.
- 현 상태 유지, 세 줄 유지, 기본 규칙을 한 줄로 합치고 PowerShell caveat만 분리하는 방안을 비교했다.
- task_logs.py 정본 규칙은 append 기본 write path를 한 줄로 합치고, PowerShell caveat만 별도 한 줄로 남긴다.
- correctness는 그대로 두면서 logs write 규칙을 더 짧게 스캔할 수 있게 한다.

**2026-04-14**
- dogfood-method 기준으로 현재 shipped skill을 이 작업에 직접 다시 적용해 Activation, Write/Reopen, Guardrail pass를 짧게 돌렸다.
- 문장 검토만 유지, 현재 task를 reopen해 실제 흐름을 밟기, mature repo spot check까지 더 넓히는 방안을 비교했다.
- 이번 턴은 현재 repo와 현재 task에 대한 dogfood pass로 한정하고, 시작 경로와 write/reopen 흐름, tests/checkers/gardening 결과만 evidence로 남긴다.
- 문장 추측 대신 실제 사용 흐름으로 현재 contract의 마찰점을 점검했고, 남은 gardening warning이 historical long-running task 하나에 국한된다는 근거를 추가했다.

**2026-04-14**
- dogfood 다음 단계로 gardening warning이 남은 backoffice-patch-fielder review task와 checker heuristic을 read-only로 다시 대조했다.
- warning을 false positive로 보고 checker를 낮추기, shipped guidance 부족으로 보고 contract를 더 키우기, intentionally coarse한 gardening hint로 유지하는 방안을 비교했다.
- 현재 extra-doc-growth warning은 contract drift보다는 intentionally coarse한 gardening hint로 유지한다. long-running research task도 잡히지만, 현 단계에서는 checker noise라기보다 root sprawl early signal로 보는 편이 맞다.
- 문장 추가나 threshold 조정 없이도 현재 checker와 shipped contract의 정렬은 유지된다고 판단했고, 남은 과제는 wording보다 mature long-running task 해석의 운영 선택으로 남긴다.

**2026-04-14**
- GPT Pro 리뷰에서 bootstrap/read-limit/log-shape/script fallback/multi-agent ownership/language rule 보강과 PowerShell note 위치 재검토 제안이 들어왔다.
- 제안을 모두 그대로 수용, 현재 helper script와 충돌하지 않는 항목만 수용, script/test를 같이 바꿔 PowerShell note를 없애는 방안을 비교했다.
- SKILL.md에는 bootstrap 조건, start-with read guidance, explicit log shape, helper-script fallback, parent-agent canonical ownership, existing-task-language 우선 규칙을 반영하고, PowerShell note는 task_logs.py 도움말에 남아 있으므로 SKILL 본문에서는 제거한다.
- 실운용 안정성을 높이면서 shipped contract를 과하게 두껍게 만들지 않았고, PowerShell caveat는 helper script의 local help로만 남겨 본문 scanability를 개선했다.

**2026-04-14**
- 후속 리뷰 제안 중 link-back과 BRIEF optional additions는 보류하고, 운용 안정성을 올리는 소규모 문구 개선만 추가로 검토했다.
- 제안 전체 수용, 장황화 방지/예시 보강/rg 명확화/decision block 표현/adoption 보강만 수용, link-back과 BRIEF optional additions는 보류하는 방안을 비교했다.
- SKILL.md에는 WORKLOG 장황화 금지 anti-pattern, role-named backlog 예시, rg 내용검색 문장, each appended decision block 표현, explicit adoption 보강 문장만 추가 반영하고 나머지는 유지한다.
- 코어를 더 두껍게 만들지 않으면서 에이전트 해석 흔들림을 줄였고, stale link나 과한 BRIEF 팽창을 유발할 가능성이 있는 제안은 의도적으로 제외했다.

**2026-04-14**
- task_logs.py의 decision append가 Options 중심 다중 플래그라 작은 로그 도구치고 과하다는 피드백이 있었다.
- decision append는 named flags 대신 순서형 인자로 단순화하고, decision block 의미도 Background / Decision / Why / Impact로 옮긴다.
- 스크립트 도움말과 SKILL.md, 테스트를 같이 맞춰 인터페이스와 guidance를 정렬한다.
- 실제 append 명령이 더 짧아졌고, PowerShell-specific --bullet caveat도 본문과 스크립트 help에서 제거할 수 있었다.

**2026-04-14**
- 후속 리뷰에서 purpose-named backlog 용어 정합성, dated sections 표현, task_logs.py 경로 해석 비대칭, WORKLOG 문장 강도, current reopen state 표현이 추가로 지적됐다.
- 날짜 형식 자체는 유지하고 문장만 정교화하기, backlog 용어를 purpose-named로 바꾸기, task_logs.py 경로 해석을 checker와 같은 방식으로 짧게 보강하는 방안을 비교했다.
- SKILL.md에는 purpose-named backlog, dated sections 표현, task_logs.py 경로 해석 보강, WORKLOG block 문장 강화, current reopen state 표현만 추가 반영한다.
- checker나 로그 포맷을 다시 흔들지 않으면서 계약 문구의 정합성과 scanability를 더 높였다.

**2026-04-14**
- 마감 전 추가 리뷰에서 backlog 용어가 role-named와 purpose-named로 섞여 있고, BRIEF 설명의 reopen phrasing이 반복처럼 읽힌다는 지적이 남았다.
- 문구를 그대로 유지, purpose-named로 전부 통일, BRIEF/Core Bias의 reopen 표현을 resume 기준으로 다듬는 방안을 비교했다.
- SKILL.md의 계약 트리와 anti-pattern 표현을 purpose-named backlog로 통일하고, BRIEF 설명과 Core Bias는 current state/resume state 기준으로 정리한다.
- 남은 용어 drift를 걷어내고, resume/handoff 중심 톤을 더 자연스럽게 맞췄다.
