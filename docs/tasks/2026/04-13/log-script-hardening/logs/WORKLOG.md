**2026-04-13**
- Reviewed current log-script contract and scoped the hardening work across shipped guidance, task_logs.py, and related tests.
- Updated shipped guidance and README copy to make task_logs.py the default log-write path, hardened append to bridge malformed latest blocks by emitting a new valid latest block, and added cross-platform regression tests plus malformed-log append coverage.
- Validated with python3 -m unittest tests.project_context.test_task_logs, python3 -m unittest tests.project_context.test_runtime_shape, python3 -m unittest discover -s tests -p 'test_*.py', python3 skills/project-context/scripts/check_runtime_shape.py, and task_logs.py worklog/decision check on the live task.
