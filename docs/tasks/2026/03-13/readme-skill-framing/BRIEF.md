# README Skill Framing

## Goal
- README와 shipped skill intro의 framing을 맞춰, `project-context`를 세션 복구 도구에만 묶지 않고 작업 맥락을 저장소 안의 평범한 파일로 남기는 스킬로 더 분명하게 설명한다.

## Scope
- `README.md`, `README.en.md`, `docs/skill-direction.md`의 소개 문구를 정리한다.
- `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`의 frontmatter와 intro가 같은 방향을 가리키도록 다듬는다.
- 관련 테스트가 문구 변경으로 깨지지 않는지 확인한다.

## Current State
- status는 completed다.
- README는 작업 맥락을 repo 안에 남겨 다음 세션이 일을 잇기 쉽게 만든다는 framing을 앞에 둔다.
- shipped skill은 contract 본문을 유지하고 frontmatter와 intro만 같은 방향으로 정리했다.
- latest validation: `py -3 -m unittest discover -s tests -p 'test_*.py'` 통과

## Next Step
- 없음

## Working Boundary
- declared read scope: `README.md`, `README.en.md`, `docs/skill-direction.md`, `skills/project-context/**`, `skills/project-context-migration/**`, `tests/**`
- declared write scope: `README.md`, `README.en.md`, `docs/skill-direction.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `tests/project_context_migration/**`, `docs/tasks/2026/03-13/readme-skill-framing/**`
