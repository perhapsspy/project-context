# ops-infra main-only 규칙 문서화

## 핵심

- 사용자 지적/요청: `ops-infra`는 `main`만 유지하는 저장소라는 사용자 지적이 있었다.
- 에이전트 조치: `AGENTS.md`에 별도 요청 없이는 작업 브랜치를 만들지 않고 `main`에 직접 반영한다는 규칙을 남겼다.
- 드러난 문제: 저장소별 흐름을 확인하지 않으면 불필요한 브랜치를 만들고 전달 경로를 틀릴 수 있다.

## 식별

- 저장소: `ops-infra`
- 작업: ops-infra main-only 규칙
- 대략 날짜: 2026-06-16

## 확인한 사실

- 작업 브랜치 `codex/pvedge-info-docs`는 `main`으로 반영된 뒤 삭제됐다.
- `AGENTS.md`에는 별도 요청이 없으면 작업 브랜치를 만들지 않고 `main`에 직접 커밋/푸시한다는 규칙이 추가됐다.

## 관련 문서

- `AGENTS.md`

## 증거

- `MEMORY.md:1150-1173`
- `rollout_summaries/2026-06-16T07-20-35-V1G7-ops_infra_main_only_branch_policy_pvedge_docs.md:43-69`

## 불확실한 점

- 원격 브랜치 삭제 상태는 이번 조사에서 git remote로 재확인하지 않았다.
