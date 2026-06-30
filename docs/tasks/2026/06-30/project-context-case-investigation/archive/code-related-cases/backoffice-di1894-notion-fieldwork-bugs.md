# DI-1894 fieldwork 후속 버그와 Notion 추적

## 핵심

- 사용자 지적/요청: 여러 fieldwork 후속 버그를 기준 Notion 작업으로 묶어 추적할 필요가 있었다.
- 에이전트 조치: `Data Infra Tasks`에 DI-1894를 만들고 `backoffice`와 `fieldwork-data` 수정 기록을 연결했다.
- 드러난 문제: 버그 묶음이 채팅과 저장소 작업 문서에 흩어지면 무엇이 같은 사건인지 알기 어렵다.

## 식별

- 저장소: `backoffice`, `fieldwork-data`
- 작업: DI-1894 fieldwork 버그 추적
- 대략 날짜: 2026-06-12 부터 2026-06-15

## 확인한 사실

- Notion title property는 `이름`이었다.
- 상태 값은 `다음 할 일` / `진행 중` 등이었다.
- 작업명은 `Backoffice 현장 작업 후속 버그 수정`으로 기록됐다.

## 관련 문서

- Notion `Data Infra Tasks`
- DI-1894 brief/worklog
- backoffice DI brief/worklog

## 증거

- `MEMORY.md:1413-1450`
- `rollout_summaries/2026-06-12T08-25-33-gyYV-backoffice_fieldwork_followup_bugs_notion_and_self_check.md`
- rollout id `019ebaef-b9e0-7d12-9c18-c6466baf7469`

## 불확실한 점

- Notion 페이지의 현재 본문은 이번 조사에서 다시 열람하지 않았다.
