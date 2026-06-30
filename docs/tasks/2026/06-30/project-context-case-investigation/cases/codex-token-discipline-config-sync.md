# codex-token-discipline과 전역 설정 동기화

## 핵심

- 사용자 지적/요청: 상시 읽기 문서와 스킬 본문의 비용 표면을 분리해서 정리할 필요가 있었다.
- 에이전트 조치: 스킬 본문, 전역 `AGENTS.md`, 개인 설정 저장소의 역할을 나눠 정리했다.
- 드러난 문제: 상시 읽기 규칙과 선택 읽기 스킬이 섞이면 토큰 비용과 적용 범위가 불명확해진다.

## 식별

- 저장소: `codex-token-discipline`, `playground/codex-personal-config`, `$CODEX_HOME`
- 작업: 토큰 규율과 전역 설정 동기화
- 대략 날짜: 2026-06-09부터 2026-06-18

## 확인한 사실

- 스킬들은 단계적 공개이고 `AGENTS.md`는 상시 읽기라 비용 표면이 다르다고 기록됐다.
- usage-audit script의 실질 비용은 원본 길이가 아니라 stdout 크기였다.
- dirty worktree rule은 `git status --short`, `git diff --stat`, path-scoped diffs를 한 줄 rule로 `$CODEX_HOME/AGENTS.md`에 두는 형태로 정리됐다.
- portable 비공개 저장소 표면는 `codex/AGENTS.md`와 `codex/agents/*.toml`로 유지됐다.

## 관련 문서

- `SKILL.md`
- `SKILL.ko.md`
- `$CODEX_HOME/AGENTS.md`
- 개인 설정 저장소 파일
- 전역 설치 스킬

## 증거

- `MEMORY.md:1017-1068`
- `rollout_summaries/2026-06-18T02-19-02-1tN9-skill_overhead_mitigation_review_commit_push_gh_account_swit.md`
- `rollout_summaries/2026-06-16T02-36-56-AmNf-minimal_global_agents_md_git_diff_budget.md`
- `rollout_summaries/2026-06-09T01-25-51-lkWU-codex_personal_config_private_repo_machine_neutral_sync.md`
- rollout ids `019ed886-551e-7f53-b645-7df7fa269413`, `019ece49-fdba-72f3-9c05-0679f9c3fad5`, `019ea9fc-666b-7841-b6e3-0a7c8e1a1afc`

## 불확실한 점

- 비공개 설정 저장소의 현재 동기화 상태와 GitHub 계정 상태는 이번 조사에서 재확인하지 않았다.
