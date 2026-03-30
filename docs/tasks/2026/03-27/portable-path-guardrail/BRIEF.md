# Portable Path Guardrail

## Goal
- `project-context`가 repo docs 안에 절대경로나 환경 의존 경로를 남기지 않도록 막는다.

## Scope
- shipped `project-context`/`project-context-migration` contract
- runtime-shape guardrail
- local direction/reference alignment
- related tests

## Current Understanding
- path portability drift는 contract가 어디에 쓸지만 말하고, 문서 안의 경로 문자열을 어떻게 적을지는 약하게 말할 때 반복되기 쉽다.

## Current State
- status는 completed다.
- portable path rule은 shipped skill과 local direction 문서에 반영됐다.
- 이후 follow-up으로 checker scan 범위가 task log까지 넓어져, 현재는 reference와 task BRIEF, task logs를 함께 본다.
- latest validation: `python3 skills/project-context/scripts/check_runtime_shape.py`; `python3 -m unittest discover -s tests -p 'test_*.py'`

## Next Step
- false positive가 실제 repo에서 반복될 때만 패턴을 더 조인다.

## Working Boundary
- declared read scope: `skills/project-context/**`, `skills/project-context-migration/**`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `README*.md`, `tests/project_context/test_runtime_shape.py`
- declared write scope: `skills/project-context/SKILL.md`, `skills/project-context/scripts/check_runtime_shape.py`, `skills/project-context-migration/SKILL.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `README.md`, `README.en.md`, `tests/project_context/test_runtime_shape.py`, `docs/tasks/2026/03-27/portable-path-guardrail/**`
