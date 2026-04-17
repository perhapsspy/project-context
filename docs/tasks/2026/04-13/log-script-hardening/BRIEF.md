# Log Script Hardening

## Goal
- `project-context`가 `logs/*.md` 직접 편집보다 `task_logs.py` 경로를 기본으로 타게 하고, latest block이 깨져 있어도 append 흐름이 쉽게 막히지 않게 만든다.

## Scope
- shipped log-write guidance와 log append ergonomics를 함께 다룬다.
- `task_logs.py`를 기본 경로로 더 강하게 쓰게 만들고 관련 tests를 맞춘다.

## Current Understanding
- 현재 guidance는 일반 write-bearing task에서 직접 편집 우회를 아직 남긴다.
- 현재 `task_logs.py`는 malformed latest block을 만나면 append 흐름이 쉽게 막힌다.
- runtime checker는 결과 shape만 검증하므로 provenance 검출보다 contract hardening과 append ergonomics 개선이 우선이다.

## Current State
- status는 completed다.
- shipped guidance와 README는 `task_logs.py`를 기본 log-write path로 쓰게 강화됐다.
- `task_logs.py` append는 malformed latest block이나 heading 없는 legacy tail이 있어도 새 valid latest block을 뒤에 추가해 normal flow를 이어갈 수 있다.
- tests와 checks는 현재 결과와 맞게 통과한다.
- blockers는 없다.

## Next Step
- 없음
