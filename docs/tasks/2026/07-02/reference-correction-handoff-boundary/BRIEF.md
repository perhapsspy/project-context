# Reference Correction Handoff Boundary

## Goal

- `project-context`가 사용자 정정과 서브에이전트 handoff에서 현재 사실 경계를 더 분명히 하도록 shipped skill을 작게 보강한다.

## Scope

- `skills/project-context/SKILL.md`의 reference 정정 규칙과 subagent brief 입력 항목만 조정한다.
- README, migration skill, direction 문서는 같은 계약을 복제하지 않는다.

## Current Understanding

- `BRIEF.md`는 이미 사용자 정정과 삭제 요청을 현재 상태 rewrite로 반영한다.
- `docs/reference/**`도 current trusted context이므로 stale claim 제거와 현재 사실 재작성은 `project-context` 직접 책임이다.
- 실제 source/runtime 사실 검증은 이 스킬이 아니라 작업 주체와 source/runtime 검증 도구의 책임이다.
- subagent brief는 최신 사용자 제약과 미확인 가정을 전달해야 하지만, multi-agent 실행 체계 자체는 이 스킬 책임이 아니다.

## Current State

- shipped skill은 reference claim에 영향을 주는 사용자 정정/삭제 요청을 stale claim 제거 또는 corrected reliable fact/source owner pointer로 정리하도록 말한다.
- shipped skill은 subagent brief에 latest user constraints와 unverified assumptions or unknowns를 포함하도록 말한다.
- runtime shape, full unittest, diff whitespace 검증은 통과했다.
- 딥리즈너 리뷰는 shipped skill 문구가 책임 경계를 유지한다고 봤고, 이 BRIEF의 다음 단계만 현재 상태로 고치라고 지적했다.

## Next Step

- Reopen if installed skill 동기화나 publish가 범위에 들어오면 repo source와 installed copy parity를 다시 확인한다.

## Working Boundary

- `skills/project-context/SKILL.md`
- `docs/tasks/2026/07-02/reference-correction-handoff-boundary/`
