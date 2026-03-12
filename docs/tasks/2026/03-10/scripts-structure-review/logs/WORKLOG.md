**2026-03-10**
- `check_runtime_shape.py`에 `RuntimePaths`와 iterator helper를 적용해 runtime wiring을 줄였다.
- repo-local test asset `tests/project_context/test_runtime_shape.py`에 runtime/pack helper를 두고 reference/root/task/main failure 케이스를 보강했다.
- `python3 skills/project-context/scripts/check_runtime_shape.py`, `python3 -m py_compile ...`, `python3 -m unittest discover ...`를 실행했고 28 tests가 통과했다.

**2026-03-10**
- repo-local test asset를 `skills/project-context/scripts/tests/`에서 `tests/project_context/`로 이동했다.
- task과 recent dogfood 예시에 남아 있던 test 경로 참조를 새 위치로 정리했다.
- 이동 후에도 `check_runtime_shape.py`, `py_compile`, `unittest`를 다시 실행해 통과를 확인했다.
