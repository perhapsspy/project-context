**2026-03-20**
- `runtime-shape` 테스트, migration fixture 테스트, checker 분기, representative fixture 내용을 다시 읽고 현재 underfit / overfit 지점을 나눴다.
- `runtime-shape` 테스트에 missing task core file, empty latest date block, non-bullet latest block branch를 추가하고, CLI output test는 exact full-output match 대신 contract-level line presence를 확인하도록 완화했다.
- migration fixture test에는 case-wide `MEMORY-CANDIDATES.md` cleanup helper를 넣고, alpha/beta에서 `REFERENCE`/`TASK` positive outcome과 task-local leakage 방지를 representative 수준으로 다시 복원했다.
- `python3 skills/project-context/scripts/check_runtime_shape.py`와 `python3 -m unittest discover -s tests -p 'test_*.py'`를 실행해 37 tests 통과를 확인했다.
