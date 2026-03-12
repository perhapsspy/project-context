# Agents and Direction Docs

- owner: ai
- started_at: 2026-03-10
- status: done

## 목적
- repo root `AGENTS.md`와 repo-level 방향성 문서를 추가해, skill 본체와 repo-local 자산의 경계를 짧고 명확하게 남긴다.

## 실행 범위
- root `AGENTS.md`를 만든다.
- `docs/skill-direction.md`를 만든다.
- 현재 스킬/guardrail/test 구조와 맞는 검증 명령을 반영한다.

## 현재 산출물 스냅샷
- `AGENTS.md`에는 repo scope, skill vs repo 경계, guardrail/tests/memory 작업 규칙이 정리돼 있다.
- `docs/skill-direction.md`에는 skill surface, repo surface, guardrail 방향, docs 역할이 bullet list로 정리돼 있다.
- 두 문서는 현재 구조(`skills/project-context/scripts/check_runtime_shape.py`, `tests/project_context/test_runtime_shape.py`, `tests/project_context_migration/test_migration_fixtures.py`)를 기준으로 맞춰져 있다.
