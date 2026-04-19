# Migration Policy Boundary

## Goal
- `project-context-migration`가 분류 전에 rollout policy와 shipped authority boundary를 먼저 판단하도록 contract를 다듬는다.

## Scope
- shipped `project-context-migration` wording 재구성
- repo-local direction 최소 동기화
- 필수 검증과 task 기록만 남긴다

## Current Understanding
- 현재 migration skill은 분류 규칙은 설명하지만, 실제 migration correctness를 먼저 가르는 rollout policy와 authority boundary를 앞에 드러내지 못한다.
- 그 결과 `replace`와 `bridge`를 늦게 고르게 되고, shipped skill/script 내용을 repo-local 문서에 다시 쓰는 duplication drift도 막지 못한다.
- 이번 변경은 새 코어 surface를 늘리기보다 판단 순서와 anti-pattern을 더 정확히 적는 쪽이 적절하다.

## Current State
- status는 completed다.
- migration guidance와 representative fixture surface를 더 얇은 최종 지침 쪽으로 다시 줄였다.
- checks는 통과했다.

## Next Step
- 없음
