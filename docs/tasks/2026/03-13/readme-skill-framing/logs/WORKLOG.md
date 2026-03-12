**2026-03-13**
- `README.md`, `README.en.md`, `docs/skill-direction.md`, `docs/memory.md`, 두 `SKILL.md`, `tests/**`를 검토해 문구 변경 범위를 frontmatter와 intro로 제한했다.
- `skills/project-context/SKILL.md`와 `skills/project-context-migration/SKILL.md`의 intro를 README framing과 맞추도록 수정했다.
- `tests/project_context_migration/test_migration_fixtures.py`의 fixture 상대 경로를 `as_posix()`로 정규화해 Windows와 POSIX에서 같은 기대값으로 비교하도록 맞췄다.
- `py -3 -m unittest discover -s tests -p 'test_*.py'`를 다시 실행해 전체 33 tests 통과를 확인했다.
