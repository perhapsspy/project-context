**2026-03-10**
- 배경: migration skill dogfood는 useful했지만, 결과가 `docs/tasks` 안에만 있으면 다음 반복에서 검증 자산으로 재사용하기 어렵다.
- 선택지: 1) dogfood 기록만 남긴다. 2) legacy/good/bad fixture를 repo-local tests 자산으로 복제하고 contract-driven test를 붙인다.
- 결정: fixture를 `tests/project_context_migration/fixtures/project_context_migration/` 아래에 고정하고, legacy/good/bad를 함께 다루는 반복 검증 테스트를 추가한다.
- 영향: 같은 dogfood를 다시 돌릴 때 입력 fixture와 기대 결과를 공유할 수 있고, migration skill 회귀를 unit test로 빨리 잡을 수 있다.
