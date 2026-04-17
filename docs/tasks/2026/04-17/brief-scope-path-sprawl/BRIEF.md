# Brief Scope Path Sprawl

## Goal
- `BRIEF.md`의 `Scope`가 touched-file inventory로 길어지지 않게 contract와 gardening check를 보강한다.

## Scope
- `Scope`를 짧은 작업 경계 요약으로 다시 고정한다.
- exact path inventory는 필요할 때만 `Working Boundary`로 미루는 기준을 정리한다.
- repo 안의 representative `BRIEF.md` 예시도 같은 기준으로 맞춘다.

## Current Understanding
- 현재 이 레포에는 `BRIEF.md`를 자동 생성하는 코드가 없고, shipped guidance와 live example이 실제 작성 습관을 만든다.
- 따라서 재발 방지는 contract wording과 warning-grade gardening check를 같이 두는 편이 더 적합하다.
- `Scope`는 reopen entrypoint의 짧은 boundary hint면 충분하다.
- 현재 evidence로는 `Scope` 제거보다 path-list 오용 억제가 더 맞다.

## Current State
- status는 completed다.
- shipped `project-context`와 `project-context-migration`는 `Scope`를 짧은 boundary summary로 제한하고, exact path inventory는 optional `Working Boundary`로 미루게 정리됐다.
- repo-local direction, review, dogfood 문서도 같은 판정선으로 맞췄다.
- gardening check는 `Scope`에 path-only bullet이 5개 이상 쌓이면 `scope-path-list-sprawl` info finding으로 알려준다.
- representative task `BRIEF.md` 예시 3건도 summary-level `Scope`로 다시 맞췄다.
- `Scope`는 default skeleton에 남기고 file-list sprawl만 막는 현재 계약을 유지한다.
- checks는 이번 상태와 맞게 통과한다.

## Next Step
- 없음
