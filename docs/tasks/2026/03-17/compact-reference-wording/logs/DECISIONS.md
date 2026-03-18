**2026-03-17**
- 배경: `reference`와 `task` 경계 강화 문장이 의미는 맞지만, 더 compact하게 줄이고 surface 수를 줄일 수 있는지 검토가 필요하다.
- 선택지: 1) 현재 문장을 유지한다. 2) fresh-context 리뷰로 wording과 반영 위치를 다시 줄인다. 3) 규칙 자체를 되돌린다.
- 결정: fresh-context 서브에이전트 리뷰를 거쳐 이 미덕을 꼭 필요한 surface에만 남기고 문장도 더 짧게 다듬는다.
- 영향: 같은 의도를 유지하면서 drift 가능성과 activation-surface 과설명을 줄일 수 있다.
**2026-03-17**
- 배경: 사용자는 이 규칙 자체보다 "같은 역할을 더 적은 텍스트로 수행하게 쓰는 스타일"을 스킬 방향으로 남기길 원했다.
- 선택지: 1) 기존 compact 결과만 유지한다. 2) repo-local 방향 문서에 작성 기준을 추가하고 shipped skill 문장도 그 기준으로 더 압축한다.
- 결정: `AGENTS.md`와 `docs/skill-direction.md`에 compact writing 원칙을 넣고, `project-context`/`project-context-migration` 문장도 실제로 줄인다.
- 영향: 이번 규칙 하나뿐 아니라 이후 skill wording 전체를 더 짧고 덜 반복적으로 유지할 기준이 생긴다.
