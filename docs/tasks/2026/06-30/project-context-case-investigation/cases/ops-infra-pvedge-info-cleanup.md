# PVEdge 정보와 pvedge_logs 정리

## 핵심

- 사용자 지적/요청: PVEdge 정보 수집과 잘못 쌓인 telemetry 정리를 같이 처리할 필요가 있었다.
- 에이전트 조치: 관련 문서를 만들고 운영 PocketBase에서 `pvedge_logs` 정리를 수행한 것으로 기록됐다.
- 드러난 문제: 정보 문서와 실제 telemetry 정리 상태가 분리되면 운영 판단 근거가 어긋난다.

## 식별

- 저장소: `ops-infra`
- 관련 저장소: `edge-c4i`
- 작업: PVEdge 정보 정리
- 대략 날짜: 2026-06-16

## 확인한 사실

- PVEdge 소유권은 `edge-system`, `edge-power-controller`, `pvedge-reporter`, `edge-c4i`, `patch-fielder`로 나뉘어 기록됐다.
- live DB에서 빈 `edge_id` 948건과 뒤섞인 6건 삭제 후 오염 row 0건이 확인됐다.

## 관련 문서

- `docs/tasks/2026/06-16/pvedge-info-collection/BRIEF.md`
- `pvedge-info.md`
- `logs/DECISIONS.md`
- `logs/WORKLOG.md`

## 증거

- `MEMORY.md:1136-1172`
- `rollout_summaries/2026-06-16T07-20-35-V1G7-ops_infra_main_only_branch_policy_pvedge_docs.md:19-33`
- `rollout_summaries/2026-06-16T07-20-35-V1G7-ops_infra_main_only_branch_policy_pvedge_docs.md:34-42`

## 불확실한 점

- 현재 운영 `pvedge_logs` 상태는 이번 조사에서 재확인하지 않았다.
