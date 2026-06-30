# Edge Agent 현재 상태 계약 정리

## 핵심

- 사용자 지적/요청: target별 latest가 아니라 Edge Agent instance 기준 current를 소유하게 정리할 필요가 있었다.
- 에이전트 조치: 현재 상태 기준을 `edge_agent_instances`로 닫고 세부 결과는 작업/배포 증거로 보냈다.
- 드러난 문제: 최신 상태 소유자가 여러 collection으로 흩어지면 읽는 쪽이 어느 값을 믿어야 하는지 모호해진다.

## 식별

- 저장소: `edge-agent-workspace`
- 작업: Edge Agent 현재 상태 계약
- 대략 날짜: 2026-06-09부터 2026-06-12

## 확인한 사실

- 최신 current model은 `edge_agent_instances`로 정리됐다.
- app/target 세부 정보는 rollout/task 결과 증거와 object refs로 이동했다.
- metric/guard 검색어는 `edge_current_upserts`로 기록됐다.

## 관련 문서

- `BRIEF.md`
- `PRD.md`
- `SPEC-TO-REHEARSAL-MATRIX.md`
- reference 문서
- 저장소 방지 규칙

## 증거

- `MEMORY.md:1329-1337`
- `MEMORY.md:1357-1359`
- `rollout_summaries/2026-06-09T04-51-17-i6WK-edge_agent_precanary_prd_implementation_closure.md:7-27`
- rollout id `019eaab8-7ba6-7ec1-ab65-a1ae2b69d8d2`

## 불확실한 점

- 이후 운영 준비 상태 세션에서 이 계약이 변경됐는지는 확인하지 않았다.
