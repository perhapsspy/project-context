# 민감정보 의심 시 staging 전 차단 규칙

## 핵심

- 사용자 지적/요청: 민감정보 의심 파일은 staging 전에 멈추라는 규칙이 필요했다.
- 에이전트 조치: `AGENTS.md`와 관련 문서에 민감정보 의심 시 `git add` 전 중단하는 규칙을 반영했다.
- 드러난 문제: 민감정보 여부가 애매한 상태에서 staging하면 나중에 되돌리기 어렵다.

## 식별

- 저장소: `ops-infra`
- 작업: 민감정보 차단 규칙
- 대략 날짜: 2026-06-25

## 확인한 사실

- 최종 규칙은 민감정보 의심 시 `git add`, 커밋, 푸시를 모두 중단하도록 바뀌었다.
- redaction 또는 사용자 확인을 먼저 하도록 기록됐다.
- 검증은 `guard 검사`, `git diff --check`, push 후 clean `main...origin/main`이었다.

## 관련 문서

- `AGENTS.md`
- 관련 작업 `BRIEF.md`
- 관련 `logs/WORKLOG.md`

## 증거

- `MEMORY.md:182-190`
- `MEMORY.md:197-206`
- `rollout_summaries/2026-06-25T05-04-53-UpcJ-ops_infra_edge_tailscale_runbook_and_sensitive_data_policy.md:48-77`

## 불확실한 점

- 실제 민감정보 샘플의 존재 여부나 내용은 이번 조사 범위에서 확인하지 않았다.
