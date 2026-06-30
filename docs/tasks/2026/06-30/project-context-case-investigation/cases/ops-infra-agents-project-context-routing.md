# ops-infra AGENTS의 project-context 연결 강화

## 핵심

- 사용자 지적/요청: 저장소 작업 대부분에서 `project-context` 적용 여부를 먼저 보게 할 필요가 있었다.
- 에이전트 조치: `AGENTS.md`에 read-only와 one-shot 예외를 제외한 적용 기준을 짧게 넣었다.
- 드러난 문제: 상시 지침이 약하면 장기 작업도 작업 문서 없이 진행될 수 있다.

## 식별

- 저장소: `ops-infra`
- 작업: ops-infra AGENTS 연결
- 대략 날짜: 2026-06-22

## 확인한 사실

- read-only 질문과 즉시 끝나는 one-shot 점검을 제외한 저장소 작업에서 `project-context`를 쓰도록 하는 취지의 규칙이 기록됐다.
- 문서 작성, 운영 조사, 인계, subagent follow-through, 재사용 reference, 작업 상태 갱신이 적용 대상으로 기록됐다.
- 검증 명령으로 project-context 런타임 형태 검사가 기록돼 있다.

## 관련 문서

- `AGENTS.md`

## 증거

- `MEMORY.md:490-514`

## 불확실한 점

- 해당 `AGENTS.md`의 현재 내용은 이번 조사에서 직접 열어 확인하지 않았다.
