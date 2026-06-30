# task-data 루트 구조 정리와 문서 담당 재확인

## 핵심

- 사용자 지적/요청: 루트에 Go 파일이 몰려 있고 namespace가 정리되지 않았다는 지적이 있었다.
- 에이전트 조치: `cmd/task-data`와 `internal/taskdata`로 옮기고 관련 기준 문서 담당을 유지했다.
- 드러난 문제: 파일 이동만으로는 구조 문제가 닫히지 않아 담당 범위 검토가 따로 필요했다.

## 식별

- 저장소: `task-data`
- 작업: task-data 구조 정리
- 대략 날짜: 2026-06-24

## 확인한 사실

- 지속 문서 담당은 세 기준 문서로 유지되었다.
- 최종 코드 분리와 `just verify`, `project-context` 형태 검사가 검증 묶음에 포함되었다.

## 관련 문서

- `docs/reference/data-model.md`
- `operations.md`
- `screen-contract.md`
- 작업 문서/로그

## 증거

- `MEMORY.md:265-316`
- `rollout_summaries/2026-06-24T01-58-02-5LSu-taskdata_structure_rewrite_and_review.md`
- `rollout_summaries/2026-06-24T07-16-11-7LGK-task_data_restructure_and_calver_alias.md`

## 불확실한 점

- 작업 문서/로그의 구체적 변경 문장은 이번 조사에서 확인하지 않았다.
