# project-context 호출 조건 검토와 설치본 동기화

## 핵심

- 사용자 지적/요청: `project-context`가 너무 자주 불리는지 실제 호출 근거를 분리해 볼 필요가 있었다.
- 에이전트 조치: 세션 JSONL에서 skill read를 세고 설명 문구를 조정한 뒤 설치본을 수동 동기화했다.
- 드러난 문제: CLI update 성공 메시지만 믿으면 설치본이 낡은 상태로 남을 수 있다.

## 식별

- 저장소: `project-context`
- 작업: project-context 호출 조건 검토
- 대략 날짜: 2026-06-22

## 확인한 사실

- 30일 scan에서 hard skill reads 416개가 확인됐다.
- 그중 assistant-autonomous/task-match가 98개로 분리됐다.
- `npx skills update`는 보고와 달리 설치본을 낡은 상태로 남겨 수동 `rsync`와 lock hash 정렬이 필요했다.

## 관련 문서

- `skills/project-context/SKILL.md`
- `docs/reference/model/skill-description-triggers.md`
- 작업 `BRIEF.md`
- 작업 `WORKLOG.md`
- 작업 `DECISIONS.md`

## 증거

- `MEMORY.md:732-787`
- `rollout_summaries/2026-06-22T01-54-32-mmmy-project_context_skill_trigger_review.md:20-30`
- `rollout_summaries/2026-06-22T01-54-32-mmmy-project_context_skill_trigger_review.md:56-80`
- rollout id `019eed09-5452-7423-95e8-a2faa17e248e`

## 불확실한 점

- 이후 현재 설치본 상태는 이번 조사에서 재검증하지 않았다.
