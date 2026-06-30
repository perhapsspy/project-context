# issue-tracker 신규 서비스의 저장소 문서 생성

## 핵심

- 사용자 지적/요청: 첨부 인계와 `project-context` 요청에 따라 채팅이 아니라 저장소 안 문서로 남길 필요가 있었다.
- 에이전트 조치: `task-data` 패턴을 참고해 README, `AGENTS.md`, reference, 작업 `BRIEF.md`를 만들었다.
- 드러난 문제: 신규 저장소의 첫 구조가 채팅에만 있으면 다음 작업이 기준 없이 시작된다.

## 식별

- 저장소: `issue-tracker`
- 작업: issue-tracker 초기 문서
- 대략 날짜: 2026-06-24

## 확인한 사실

- attached 인계와 `project-context` 요청에 따라 chat-only가 아니라 저장소 안 문서를 만들었다.
- `project-context` 형태 검사와 live `/healthz`, `/`, `plant.사건` 흐름 검증이 기록되어 있다.

## 관련 문서

- 루트 README 연결 문서
- concise `AGENTS.md`
- `docs/reference/**`
- 날짜별 `docs/tasks/.../BRIEF.md`

## 증거

- `MEMORY.md:215-255`
- `rollout_summaries/2026-06-24T10-05-14-zI0j-issue_tracker_initial_go_sqlite_service_scaffold.md`
- thread `019ef917-4f0c-7661-850c-fe073aa2d0cb`

## 불확실한 점

- 생성된 각 문서의 실제 본문은 이번 조사에서 열지 않았다.
