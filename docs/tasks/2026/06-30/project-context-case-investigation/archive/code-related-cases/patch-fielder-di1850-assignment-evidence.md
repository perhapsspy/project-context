# DI-1850 assignment 수정 뒤 실제 변경 증거 반영

## 핵심

- 사용자 지적/요청: 보이는 화면만이 아니라 실제 생성/삭제와 attach/detach 증거를 문서에 남길 필요가 있었다.
- 에이전트 조치: schedule과 resource와 담당자 변경 증거를 `WORKLOG`, QA 매트릭스, 결정 로그에 반영했다.
- 드러난 문제: 화면 가시성만 확인하면 실제 mutation 성공 여부가 남지 않는다.

## 식별

- 저장소: `patch-fielder-di-1850-fieldwork`
- 작업: DI-1850 assignment 증거
- 대략 날짜: 2026-06-23 부터 2026-06-29

## 확인한 사실

- schedule 생성/삭제 증거가 문서에 반영됐다.
- resource 연결/해제 증거가 문서에 반영됐다.
- responsible member 토글 증거가 문서에 반영됐다.
- QA 문서가 표면 가시성 중심에서 실제 변경 실행 완료 상태로 수정됐다.

## 관련 문서

- `logs/WORKLOG.md`
- `working/FIELDWORK-QA-MATRIX.md`
- `logs/DECISIONS.md`

## 증거

- `MEMORY.md:1-58`
- `rollout_summaries/2026-06-23T07-42-52-T4dM-di_1850_fieldwork_assignment_picker_scope_fix.md`
- rollout id `019ef36e-9993-7282-9682-69481c15cc9e`

## 불확실한 점

- 브라우저 session의 현재 상태는 확인하지 않았다.
