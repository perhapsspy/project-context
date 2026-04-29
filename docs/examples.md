# 예시

## 좋은 `BRIEF.md`

```md
# 로그인 리다이렉트 수정

## Goal
- 초대 가입 흐름은 유지하면서 로그인 후 리다이렉트 반복을 고친다.

## Scope
- 로그인 action, 로그인 후 redirect helper, 보호 route smoke path.
- session storage나 invite token 의미는 다시 설계하지 않는다.

## Current Facts
- 오래된 cookie가 더 이상 접근할 수 없는 발전소를 가리킬 수 있다.
- `next` redirect는 허용된 route를 가리킬 때 여전히 유효하다.

## Current State
- redirect helper가 다음 route를 고르기 전에 오래된 발전소 선택 상태를 정리한다.
- 대상 auth 테스트는 통과했고, 전체 lint에는 이번 변경과 무관한 기존 formatting warning이 남아 있다.

## Next Step
- stale-cookie login browser smoke를 돌리고, 기대한 plant page로 도착하면 commit한다.

## Working Boundary
- `src/lib/user/auth/post-login.server.js`
- `src/routes/login/+page.server.js`
```

좋은 이유:
- 지금 믿을 수 있는 상태를 말하고, 지나간 순서를 다시 쓰지 않는다.
- 검증은 현재 상태 한 문장으로 요약하고, 자세한 근거는 `WORKLOG.md`에 둔다.
- `Next Step`은 backlog가 아니라 다시 시작 가능한 가장 가까운 행동 하나다.

## 나쁜 `BRIEF.md`

```md
# 로그인 리다이렉트 수정

## Files Changed
- src/lib/user/auth/post-login.server.js
- src/routes/login/+page.server.js
- src/routes/logout/+server.js

## Investigation
- cookie 상태를 먼저 확인했다.
- auth state 전체 삭제를 시도했다.
- lint가 실패했다.
- redirect helper를 바꿨다.

## Validation
- npm run check ...
- browser logs ...
- raw output ...
```

고칠 점:
- 파일 목록과 명령 세부 내용은 `WORKLOG.md`로 옮긴다.
- 조사 순서는 현재 믿을 수 있는 사실로 압축한다.
- `Next Step`에는 가장 가까운 재개 행동만 둔다.

## 좋은 `WORKLOG.md`

```md
**2026-04-29**
- 로그인 후 redirect helper에서 오래된 발전소 선택 상태를 복구하는 경로를 고치고 invite `next` 경로는 유지했다. 대상 auth 테스트는 통과했고, 오래된 cookie 로그인 browser smoke도 기대한 plant page에 도착했다. 전체 lint에는 이번 변경과 무관한 기존 formatting warning이 남아 있다.
- auth 수정 뒤 보호 route를 다시 확인했다.
  - `/app/plant/old-id`는 오래된 선택 상태를 지우고 첫 접근 가능 plant로 redirect한다.
  - `/org-invite/example`은 signup 뒤 invite flow로 돌아간다.
```

좋은 이유:
- 최상위 bullet 하나가 의미 있는 작업 묶음이다.
- 들여쓴 bullet은 명령 실행 기록이 아니라 작은 검증 표로만 쓴다.
- 이번 작업 검증과 무관한 기존 repo 문제를 분리한다.

## 좋은 `DECISIONS.md`

```md
**2026-04-29**
- Background: 오래된 발전소 선택 상태가 auth token보다 오래 남아 viewer를 접근 불가능한 route로 보낼 수 있다.
- Decision: 로그인 후 routing에서 오래된 선택 상태는 정리하되, 허용된 target을 가리키는 명시적 `next` redirect는 유지한다.
- Why: invite/signup routing 의미를 약하게 만들지 않으면서 복구 경로만 고칠 수 있기 때문이다.
- Impact: 이후 auth 작업에서는 오래된 token 복구와 오래된 선택 상태 복구를 별도 케이스로 다룬다.
```

좋은 이유:
- 미래 작업의 해석에 영향을 주는 판단을 남긴다.
- 정확히 4개의 최상위 bullet이다.
- 일상적인 수정이나 검증 통과를 결정으로 남기지 않는다.
