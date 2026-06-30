# pre-canary 문서와 방지 규칙 정리

## 핵심

- 사용자 지적/요청: 실제 canary 전에 최신 `main` 기준 문서와 방지 규칙을 정리할 필요가 있었다.
- 에이전트 조치: 실제 운영 작업 범위를 닫고 `just completion-audit`, `git diff --check` 통과 후 `origin/main`에 반영했다.
- 드러난 문제: live 전 문서가 낡으면 실제 Edge 접근과 배포 작업 범위가 섞일 수 있다.

## 식별

- 저장소: `edge-agent-workspace`
- 작업: pre-canary 문서 정리
- 대략 날짜: 2026-05-20

## 확인한 사실

- 실 Edge SSH/read, `systemctl`, payload swap, credential replacement, self-update canary, fleet rollout, Backoffice UI는 범위 밖이었다.
- `just completion-audit`, `git diff --check` 통과 후 `origin/main`에 푸시했다.

## 관련 문서

- `BRIEF.md`
- `README.md`
- `BACKLOG.md`
- `LIVE-GATES.md`
- `LIVE-READINESS-PACKET.md`
- `CANARY-RUNBOOK.md`
- `CANARY-FREEZE-PACKET.md`
- `REMOTE-SHARING-PLAN.md`

## 증거

- `MEMORY.md:1299-1307`
- `rollout_summaries/2026-05-20T08-25-05-4X9z-pre_canary_doc_consolidation_before_canary.md:7-30`
- rollout id `019e447d-0834-7732-9a23-f3bd7e04150d`

## 불확실한 점

- 당시 실제 변경 diff 내용은 이번 조사에서 열람하지 않았다.
