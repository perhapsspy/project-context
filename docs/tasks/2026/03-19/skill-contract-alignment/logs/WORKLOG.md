**2026-03-19**
- `project-context` / `project-context-migration` skill, checker script, migration fixture/test, 로컬 방향 문서를 다시 읽고 actionable contract mismatch를 좁혔다.
- shipped skill 두 개의 checker invocation 문구를 설치된 skill directory 기준으로 다시 적고, `STATUS.md` declared scope label과 latest `DECISIONS.md` block guidance를 thin guardrail 수준에 맞게 낮췄다.
- `case-beta-good` fixture에서 resolved-only `MEMORY-CANDIDATES.md`를 제거하고, migration test가 그 파일이 남지 않는지 직접 확인하게 했다.
- `docs/reference/model/context-surfaces.md`, `docs/skill-direction.md`에 declared scope literal label guidance를 맞춘 뒤 `python3 skills/project-context/scripts/check_runtime_shape.py`와 전체 unittest를 실행해 통과를 확인했다.
- follow-up으로 migration fixture test에서 task file 경로, migration brief 문구, 부수 output path assertion을 덜어내고, leave/reference/memory 경계를 대표하는 assertion만 남겼다.
- 변경 후 `python3 skills/project-context/scripts/check_runtime_shape.py`와 `python3 -m unittest discover -s tests -p 'test_*.py'`를 다시 실행해 통과를 확인했다.
