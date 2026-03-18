**2026-03-17**
- `docs/memory.md`, `docs/skill-direction.md`, `docs/reference/model/context-surfaces.md`, `skills/project-context/SKILL.md`, `skills/project-context-migration/SKILL.md`, `README.md`, `README.en.md`를 읽고 현재 task/reference 경계 표현을 확인했다.
- wording drift를 줄이기 위해 서브에이전트 둘에게 짧은 문장 후보 브레인스토밍을 맡겼다.
- 수렴한 문장을 기준으로 shipped skill, migration skill, README, repo-local direction 문서에 task는 경로·근거·변경 흔적만 남기고 주제별 정본 내용은 reference가 소유한다는 규칙을 반영했다.
- `python3 -m unittest discover -s tests -p 'test_*.py'`를 실행해 전체 테스트 통과를 확인했고, checker는 skill-relative 경로로 다시 실행할 예정이다.
- `python3 skills/project-context/scripts/check_runtime_shape.py`를 실행해 runtime shape check 통과를 확인했다.
