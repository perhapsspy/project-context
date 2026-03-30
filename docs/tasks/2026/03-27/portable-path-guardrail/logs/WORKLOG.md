**2026-03-27**
- shipped skill, migration skill, local direction/reference/memory, README, runtime-shape tests를 읽고 path portability rule과 guardrail 추가 지점을 정했다.
- shipped/local surface에 portable path 규칙을 반영하고, checker에 repo-root 절대경로와 환경 경로 marker scan 및 대응 tests를 추가했다.
- `python3 skills/project-context/scripts/check_runtime_shape.py`와 `python3 -m unittest discover -s tests -p 'test_*.py'`를 실행해 모두 통과했다.
- shipped/local wording을 더 짧게 압축하되 portable path rule과 checker 설명 범위는 유지했다.
- 리뷰 지적에 맞춰 path scan 범위를 `docs/` 전체에서 `memory/reference/current task snapshots`로 좁히고, task logs 및 nested artifacts는 스캔하지 않는 회귀 테스트를 추가했다.
**2026-03-30**
- README에서는 portable-path 한 줄을 제거하고, `docs/memory.md`에서는 standing rule 중복을 삭제했다.
- local direction/reference wording은 `<repo-root>`, `<task-root>`, `$CODEX_HOME` 같은 project-owned placeholder 예시를 직접 적어 checker와 허용 경계를 맞췄다.
- `python3 skills/project-context/scripts/check_runtime_shape.py`와 `python3 -m unittest discover -s tests -p 'test_*.py'`를 다시 실행해 모두 통과했다.
