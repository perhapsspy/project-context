# Skill Contract Alignment

- owner: codex
- started_at: 2026-03-19
- status: completed

## Goal
- shipped `project-context` / `project-context-migration` skill wording, migration fixtures, and repo-local support docs를 현재 thin guardrail/runtime 계약에 다시 맞춘다.

## Scope
- checker 실행 안내를 실제 설치/실행 형태와 맞춘다.
- stale `MEMORY-CANDIDATES.md` lifecycle drift를 migration fixture/test에서 제거한다.
- checker보다 강하게 약속하던 wording을 현재 contract 수준으로 줄인다.
- migration fixture test는 representative classification outcome만 고정하고, 저신호 경로/스냅샷 고정은 줄인다.

## Current Understanding
- 최근 review finding 대부분은 새 memory ownership 철학 자체보다, skill wording과 실제 checker/fixture가 서로 다른 수준으로 말하던 contract mismatch였다.
- `skills/project-context/SKILL.md`와 `skills/project-context-migration/SKILL.md`는 checker invocation과 file-shape enforcement를 실제보다 강하게 적은 부분이 있다.
- `tests/project_context_migration/.../case-beta-good/`에는 resolved-only `MEMORY-CANDIDATES.md`가 남아 있어 현재 skill lifecycle 규칙과 어긋난다.

## Current Output Snapshot
- `skills/project-context/SKILL.md`와 `skills/project-context-migration/SKILL.md`가 checker invocation, declared scope label, latest log-block guidance를 현재 thin guardrail contract 수준으로 설명한다.
- `docs/reference/model/context-surfaces.md`와 `docs/skill-direction.md`가 declared scope label guidance를 같은 방향으로 설명한다.
- migration fixture test는 stale `MEMORY-CANDIDATES.md` 부재, leave/reference/memory 경계 같은 representative outcome만 확인하고 task path나 brief 문구 같은 저신호 고정은 줄였다.
