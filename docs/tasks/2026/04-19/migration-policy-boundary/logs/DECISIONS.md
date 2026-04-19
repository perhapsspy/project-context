

**2026-04-19**
- migration skill dogfood에서 분류 규칙보다 rollout policy와 shipped authority boundary가 먼저 드러나야 한다는 요구가 분명해졌다.
- project-context-migration을 policy-first 구조로 재편하고, repo-local 문서는 shipped skill/script를 참조만 하도록 경계를 올린다.
- 이 방식이 새 core surface를 늘리지 않으면서 replace/bridge 판단, contract duplication, cleanup overreach를 함께 줄인다.
- migration guidance는 classification 전에 policy와 authority boundary를 고르게 되고, repo-local duplication drift를 더 직접적으로 막게 된다.
