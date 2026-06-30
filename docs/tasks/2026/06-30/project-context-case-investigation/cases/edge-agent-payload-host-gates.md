# PAYLOAD-CANARY-1와 T-HOST-PROBE 구분

## 핵심

- 사용자 지적/요청: 닫힌 host probe와 열린 payload canary를 같은 상태로 두지 않도록 정리할 필요가 있었다.
- 에이전트 조치: `PAYLOAD-CANARY-1`은 열린 관문으로, `T-HOST-PROBE`는 선택 근거로 분리했다.
- 드러난 문제: 닫힌 증거와 열린 관문이 한 문서에 섞이면 live 전 확인 상태를 오판할 수 있다.

## 식별

- 저장소: `edge-agent-workspace`
- 작업: canary 관문 구분
- 대략 날짜: 2026-05-20

## 확인한 사실

- `PAYLOAD-CANARY-1`은 열린 payload-canary 관문로 기록됐다.
- `T-HOST-PROBE`는 freeze-record 준비를 위한 선택 근거로만 남았다.

## 관련 문서

- `LIVE-GATES.md`
- `CANARY-FREEZE-PACKET.md`
- `working/canary-freeze/TEMPLATE.md`

## 증거

- `MEMORY.md:1351-1353`
- `rollout_summaries/2026-05-20T08-25-05-4X9z-pre_canary_doc_consolidation_before_canary.md:37-41`

## 불확실한 점

- `PAYLOAD-CANARY-1`의 이후 상태는 이번 조사 범위에서 확인하지 않았다.
