**2026-03-18**
- 배경: 이 레포에는 dogfood 방식이 task 기록으로는 남아 있지만, 다음 반복에서 바로 재사용할 짧은 repo-local 루프는 정리돼 있지 않다.
- 선택지: 1) 기존 task를 링크만 한다. 2) 공통 패턴을 repo-local 방향으로 압축하고, 같은 루프로 현재 변경을 즉시 점검한다.
- 결정: dogfood 방식은 `docs/skill-direction.md`에 짧게 정리하고, 바로 이번 skill wording/style 변경에 적용해 결과를 task에 남긴다.
- 영향: 이후 wording, README, migration 같은 surface를 점검할 때 같은 절차를 반복 재사용할 수 있다.
**2026-03-18**
- 배경: 실제 dogfood를 돌려보니 현재 `project-context` skill의 `docs/reference/` 설명이 의도는 맞지만 여전히 길었다.
- 선택지: 1) dogfood 결과를 no-op로 끝낸다. 2) 같은 의미를 유지하는 범위에서 문장을 한 단계 더 줄인다.
- 결정: `docs/reference/` 설명은 canonical detail과 task trace 경계만 남기도록 한 번 더 압축한다.
- 영향: 새로 적은 dogfood 루프가 실제 wording 개선으로 이어졌는지 같은 task 안에서 바로 확인할 수 있다.
