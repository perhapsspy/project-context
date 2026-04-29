# Logging Guidance Improvements

## Goal
- Improve `project-context` logging guidance from recent `../conalog` task-log evidence without expanding the core contract unnecessarily.

## Scope
- README entry guidance for adoption modes and concrete examples.
- Shipped `skills/project-context/SKILL.md` wording around `WORKLOG`, `BRIEF`, decisions, and long-running task closure.
- `task_logs.py` shape checks only where current tooling blocks a useful log pattern.

## Current Understanding
- Recent conalog logs show the core split is right: `BRIEF.md` should stay resumable, `WORKLOG.md` should hold evidence, and `DECISIONS.md` should hold durable interpretation.
- The main drift is long-running tasks flattening micro-iterations, repeated validation, and investigation history into one chronological block.
- `WORKLOG.md` sometimes needs nested evidence bullets for validation matrices, but `DECISIONS.md` should remain exactly four top-level bullets.
- Prior guardrail work warned against turning wording into enforcement before tests/checkers support it.

## Current State
- README now separates adoption modes and links concrete record-shape examples.
- `docs/examples.md` and `docs/examples.en.md` show good/poor `BRIEF.md`, good `WORKLOG.md`, and good `DECISIONS.md` shapes without encouraging mechanical WORKLOG labels.
- Shipped `SKILL.md` now clarifies outcome/tranche-level worklogs, natural task-language bullets, pre-existing debt separation, and pause/reopen decision handling.
- `task_logs.py` now allows nested WORKLOG evidence bullets while preserving indentation in `tail`; DECISIONS still rejects nested evidence and requires exactly four top-level bullets.
- Validation passed: full unittest discovery, runtime shape check, and gardening check. Gardening still reports the existing 2026/04-09 extra-doc-growth info.

## Next Step
- Review the diff for wording weight and merge if the examples/tooling shape is acceptable.

## Working Boundary
- `README.md`
- `README.en.md`
- `skills/project-context/SKILL.md`
- `skills/project-context/scripts/task_logs.py`
- `tests/project_context/`
