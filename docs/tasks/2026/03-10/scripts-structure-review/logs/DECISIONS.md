**2026-03-10**
- 배경: `check_runtime_shape.py`는 기능은 안정적이지만 runtime path 전달이 퍼져 있고, 테스트도 일부 implementation-following 경향과 setup 중복이 있었다.
- 선택지: 1) 기능만 유지하고 그대로 둔다, 2) script 구조만 정리한다, 3) runtime wiring과 테스트 둘 다 더 contract-driven하게 정리한다.
- 결정: `RuntimePaths`로 runtime boundary를 묶고, iterator helper로 불필요한 list 구축을 줄이며, 테스트는 fixture helper와 실패 경로 보강으로 contract-driven하게 정리한다.
- 영향: primary flow가 더 짧아지고, 테스트가 내부 helper보다 사용자-visible contract에 더 가깝게 붙으며, 이후 guardrail 확장 시 시그니처 성장과 setup 중복이 줄어든다.

**2026-03-10**
- 배경: `check_runtime_shape.py`는 skill 사용 중 직접 호출되는 스크립트지만, 그 안정성을 위한 테스트까지 `skills/project-context/scripts/` 아래에 있으면 skill 본체와 repo-local 개발 자산의 경계가 흐려진다.
- 선택지: 1) script와 test를 모두 skill 폴더에 둔다, 2) script도 repo root로 올린다, 3) skill 사용 스크립트는 skill 폴더에 두고 테스트는 repo root `tests/`로 분리한다.
- 결정: `check_runtime_shape.py`는 `skills/project-context/scripts/`에 유지하고, `test_runtime_shape.py`는 repo-local asset로 `tests/project_context/`로 이동한다.
- 영향: skill 소비 표면은 작게 유지되고, repo는 여전히 guardrail 안정성을 충분히 검증할 수 있으며, “스킬 자체”와 “이 리포의 개발 자산”의 경계가 더 명확해진다.
