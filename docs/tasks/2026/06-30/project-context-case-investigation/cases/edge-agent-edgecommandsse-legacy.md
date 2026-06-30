# edgecommandsse를 기존 증거로 분리

## 핵심

- 사용자 지적/요청: `edgecommandsse`를 새 운영 소유자로 볼지 기존 증거로 볼지 구분해야 했다.
- 에이전트 조치: `Conalog/device-agent`의 `edgecommandsse`를 기존 호환성 증거로 분류했다.
- 드러난 문제: 과거 prototype을 현재 운영 소유자로 잘못 읽으면 설계 출처가 틀어진다.

## 식별

- 저장소: `edge-agent-workspace`
- 관련 저장소: `device-agent`
- 작업: edgecommandsse 분류
- 대략 날짜: 2026-06-08

## 확인한 사실

- rollout 요약는 `edgecommandsse` module을 기존 PB realtime + pending catch-up consumer/executor prototype으로 취급했다고 기록한다.

## 관련 문서

- reference 문서
- PRD/task 표면

## 증거

- `MEMORY.md:1355-1356`
- `rollout_summaries/2026-06-08T01-38-19-f4PR-edge_agent_precanary_prd_task_surface_and_handoff.md:7-9`
- `rollout_summaries/2026-06-08T01-38-19-f4PR-edge_agent_precanary_prd_task_surface_and_handoff.md:66-77`

## 불확실한 점

- `device-agent`의 실제 파일은 이번 조사에서 열람하지 않았다.
