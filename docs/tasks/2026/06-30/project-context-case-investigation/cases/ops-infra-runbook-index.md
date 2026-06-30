# ops runbook 폴더와 짧은 index 정리

## 핵심

- 사용자 지적/요청: 운영 조사 절차를 흩어진 문서가 아니라 찾을 수 있는 runbook 구조로 정리할 필요가 있었다.
- 에이전트 조치: runbook 폴더와 짧은 index를 두고 조사 순서 문서를 연결했다.
- 드러난 문제: 절차 문서가 흩어지면 다음 운영 조사가 매번 출처를 다시 찾는다.

## 식별

- 저장소: `ops-infra`
- 작업: ops runbook 정리
- 대략 날짜: 2026-06-08

## 확인한 사실

- `README.md`는 개별 runbook 목록 대신 runbook index를 가리키도록 축약됐다.
- `logs/`와 `working/`의 과거 경로 치환은 되돌려졌다.
- 현재 재개 표면과 reference 중심으로 새 경로가 유지됐다.

## 관련 문서

- `docs/reference/runbooks/index.md`
- `docs/reference/runbooks/comment-map-object-receive-rate.md`
- `README.md`
- `docs/reference/ops-context.md`
- `docs/reference/device-data-handling.md`

## 증거

- `MEMORY.md:1655-1687`
- `rollout_summaries/2026-06-08T02-43-03-rNNT-ops_infra_runbook_index_and_runbooks_folder.md:19-39`
- `rollout_summaries/2026-06-08T02-43-03-rNNT-ops_infra_runbook_index_and_runbooks_folder.md:48-64`

## 불확실한 점

- 이동된 모든 runbook 파일의 현재 목록은 이번 조사에서 저장소 파일시스템으로 확인하지 않았다.
