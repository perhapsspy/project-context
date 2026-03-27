# Guardrail Surface Redesign

- owner: codex
- started_at: 2026-03-20
- status: completed

## Goal
- `project-context` shipped checker와 관련 repo-local tests/fixtures를 thin contract surface에 맞게 다시 정렬한다.

## Scope
- shipped `check_runtime_shape.py`에서 과도한 enforcement와 maintainer telemetry를 걷어낸다.
- `runtime-shape` 테스트는 latest-only, path/date, candidate grammar/reachability 같은 핵심 branch를 본다.
- migration good fixture와 test는 current ownership 철학에 맞게 `memory`/`reference` 중복을 제거한다.

## Current Understanding
- 현재 checker는 `DECISIONS.md` 4-bullet를 hard-fail로 강제하고 `--memory-candidate-stats`까지 같은 lane에 둬, thin guardrail보다 무거운 validator처럼 보인다.
- migration good fixture는 일부 standing fact를 `memory`와 `reference`에 동시에 두고 있어 current ownership contract와 충돌한다.
- fresh-context review는 latest-only log validation, date-path branch, candidate state enum, migration provenance/audit surface가 아직 어긋나 있다고 지적했다.

## Current Output Snapshot
- shipped checker는 required surface/path/date, `docs/memory.md` hard cap, latest log-block shape, `MEMORY-CANDIDATES` grammar/reachability, secret-like markers만 확인한다.
- runtime-shape tests는 latest-only log branch, task date/path branch, candidate enum/reachability branch를 직접 본다.
- migration good fixture/tests는 representative task/reference/leave outcome만 고정하고, `memory`/`reference` ownership 중복을 제거한 상태다.
