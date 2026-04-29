# Examples

## Good `BRIEF.md`

```md
# Login Redirect Fix

## Goal
- Fix the post-login redirect loop without changing the invite signup flow.

## Scope
- Login action, post-login redirect helper, and the protected-route smoke path.
- No redesign of session storage or invite-token semantics.

## Current Facts
- Stale cookies can point at a plant the viewer can no longer access.
- `next` redirects are still valid when they point to an allowed route.

## Current State
- The redirect helper now clears stale plant selection before choosing the next route.
- Targeted auth tests pass; full lint still reports unrelated legacy formatting warnings.

## Next Step
- Run the browser smoke for stale-cookie login, then commit if the redirect lands on the expected plant page.

## Working Boundary
- `src/lib/user/auth/post-login.server.js`
- `src/routes/login/+page.server.js`
```

Why it works:
- It says what to trust now, not everything that happened.
- Validation is one current-state sentence, with details left for `WORKLOG.md`.
- The next step is one restartable action, not a backlog.

## Poor `BRIEF.md`

```md
# Login Redirect Fix

## Files Changed
- src/lib/user/auth/post-login.server.js
- src/routes/login/+page.server.js
- src/routes/logout/+server.js

## Investigation
- First I checked cookies.
- Then I tried clearing all auth state.
- Then lint failed.
- Then I changed the redirect helper.

## Validation
- npm run check ...
- browser logs ...
- raw output ...
```

What to change:
- Move file inventory and command detail into `WORKLOG.md`.
- Replace investigation history with current facts.
- Keep only the nearest restart action in `Next Step`.

## Good `WORKLOG.md`

```md
**2026-04-29**
- Fixed stale plant-selection recovery in the login redirect helper and kept invite `next` routing unchanged. Targeted auth tests passed, browser stale-cookie smoke reached the expected plant page, and full lint still has unrelated pre-existing formatting warnings.
- Rechecked the protected route after the auth fix.
  - `/app/plant/old-id` now clears stale selection and redirects to the first accessible plant.
  - `/org-invite/example` still returns to the invite flow after signup.
```

Why it works:
- Each top-level bullet is a meaningful work batch.
- Nested bullets are used only as compact evidence, not as a command transcript.
- Unrelated repo debt is separated from task validation.

## Good `DECISIONS.md`

```md
**2026-04-29**
- Background: stale plant selection can survive longer than the auth token and send a viewer back to an inaccessible route.
- Decision: clear stale selection during post-login routing, but keep explicit `next` redirects when the target is still allowed.
- Why: this fixes the recovery path without weakening invite/signup routing semantics.
- Impact: future auth work should treat stale token recovery and stale selection recovery as separate cases.
```

Why it works:
- It records interpretation that affects future work.
- It is exactly four top-level bullets.
- It does not log routine edits or validation passes as decisions.
