# Edge Tailscale 접속 규칙 문서화

## 핵심

- 사용자 지적/요청: Edge SSH 접근 방식이 바뀐 뒤 runbook에 반영할 필요가 있었다.
- 에이전트 조치: Tailscale IP 조회와 SSH 키 사용 규칙을 관련 runbook과 edge-agent-workspace reference에 반영했다.
- 드러난 문제: 접속 규칙이 문서에 없으면 다음 세션이 로컬 DNS 같은 틀린 전제를 반복한다.

## 식별

- 저장소: `ops-infra`, `edge-agent-workspace`
- 작업: Tailscale 접속 규칙
- 대략 날짜: 2026-06-25

## 확인한 사실

- 새 규칙은 Edge id 또는 lot number `1781794800`으로 새 network 대상을 인식하는 내용을 포함했다.
- 새 Edge Google OAuth 계정 전환과 `tailscale status --json` 확인이 기록됐다.

## 관련 문서

- `docs/reference/runbooks/tailscale-ssh-access.md`
- `docs/reference/edge-repositories.md`
- `edge-agent-workspace/docs/reference/workspace/host-ssh-readback.md`

## 증거

- `MEMORY.md:196-203`
- `rollout_summaries/2026-06-25T05-04-53-UpcJ-ops_infra_edge_tailscale_runbook_and_sensitive_data_policy.md:19-27`
- `rollout_summaries/2026-06-25T05-04-53-UpcJ-ops_infra_edge_tailscale_runbook_and_sensitive_data_policy.md:36-46`

## 불확실한 점

- 2026-06-19 이후 모든 Edge가 실제로 새 network에 있는지는 이번 조사에서 live 확인하지 않았다.
