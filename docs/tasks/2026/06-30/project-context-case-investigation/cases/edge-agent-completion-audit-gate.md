# completion-audit 검사 기준 정리

## 핵심

- 사용자 지적/요청: 문서 묶음이 완료됐는지 눈으로만 판단하지 않고 검사로 확인할 필요가 있었다.
- 에이전트 조치: `just completion-audit`로 작업 상태, 링크 형태, 작업 루트 방지 규칙, `project-context` 묶음을 확인했다.
- 드러난 문제: 문서가 좋아 보여도 새 파일이 미추적이면 실제 인계 묶음은 닫히지 않는다.

## 식별

- 저장소: `edge-agent-workspace`
- 작업: completion-audit 검사 기준
- 대략 날짜: 2026-05-20부터 2026-06-08

## 확인한 사실

- `just completion-audit`는 저장소 상태, T-id 포함 상태, 작업 루트 방지 규칙, `project-context` 묶음을 함께 확인하는 검사 기준으로 기록됐다.
- 새 작업 파일이 미추적 상태일 때 검사가 실패했고, 스테이징 후 통과했다.

## 관련 문서

- 작업 루트
- 저장소 링크 형태
- 묶음 방지 규칙
- `project-context` 형태

## 증거

- `MEMORY.md:1354`
- `MEMORY.md:1363-1365`
- `rollout_summaries/2026-06-08T01-38-19-f4PR-edge_agent_precanary_prd_task_surface_and_handoff.md:59-64`

## 불확실한 점

- 각 audit 실행의 원문 로그는 이번 조사에서 열람하지 않았다.
