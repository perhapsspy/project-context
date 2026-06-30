# fieldwork-data 응답 계약 정렬

## 핵심

- 사용자 지적/요청: UI 증상만 보지 말고 command 담당과 backoffice policy 판단을 맞출 필요가 있었다.
- 에이전트 조치: `payload.policy` 우선순위와 기존 message 대체 조건을 계약으로 맞췄다.
- 드러난 문제: UI 단에서만 고치면 command 응답 계약과 화면 판단이 다시 어긋날 수 있다.

## 식별

- 저장소: `fieldwork-data`, `backoffice`
- 작업: fieldwork-data 응답 계약
- 대략 날짜: 2026-06-12 부터 2026-06-15

## 확인한 사실

- started message의 `payload.policy`가 우선이라는 계약이 기록됐다.
- 누락된 기존 message만 planned activity policy를 기준으로 대체한다는 계약이 기록됐다.
- `workflow_command_test.go`에는 `activities.policy` schema column이 필요했다.

## 관련 문서

- Notion DI-1894
- backoffice 작업 문서/worklog

## 증거

- `MEMORY.md:1427-1450`
- `rollout_summaries/2026-06-12T08-25-33-gyYV-backoffice_fieldwork_followup_bugs_notion_and_self_check.md:50-69`
- rollout id `019ebaef-b9e0-7d12-9c18-c6466baf7469`

## 불확실한 점

- `fieldwork-data`의 현재 테스트 파일 내용은 이번 조사에서 확인하지 않았다.
