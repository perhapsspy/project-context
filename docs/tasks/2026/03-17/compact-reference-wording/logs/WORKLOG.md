**2026-03-17**
- `AGENTS.md`, shipped skill, migration skill, local direction 문서, README diff를 다시 읽고 현재 wording 범위와 중복 정도를 확인했다.
- fresh-context 서브에이전트 둘에게 compact wording과 최소 surface 추천만 검토하게 했다.
- 두 리뷰 모두 `AGENTS.md`, `docs/skill-direction.md`, shipped skill 두 곳만 authoritative surface로 남기고 README, `docs/memory.md`, model doc에서는 같은 규칙을 걷어내자는 결론으로 수렴했다.
- 그 결론에 맞춰 문장을 `정본 내용은 reference에 두고, task에는 경로·판단 근거·변경 흔적을 남긴다` 수준으로 압축하고 중복 surface를 정리했다.
- `python3 skills/project-context/scripts/check_runtime_shape.py`와 `python3 -m unittest discover -s tests -p 'test_*.py'`를 실행해 runtime shape와 전체 테스트 통과를 확인했다.
- 사용자 의도를 반영해 이 기준을 규칙 하나가 아니라 스킬 기술 방향으로 다루기로 하고, `AGENTS.md`와 `docs/skill-direction.md`에 compact writing 원칙을 추가했다.
- `skills/project-context/SKILL.md`의 `docs/reference/` 설명과 `skills/project-context-migration/SKILL.md`의 `REFERENCE`/migration 규칙 문장을 더 짧게 다듬었다.
