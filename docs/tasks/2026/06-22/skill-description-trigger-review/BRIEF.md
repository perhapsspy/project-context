# skill description trigger review

## Goal

- Review whether `project-context` should adjust its skill description so it self-selects better in Codex app usage without over-triggering.

## Scope

- Focus on official Codex skill-discovery guidance, recent local invocation evidence, and wording recommendations for `skills/project-context/SKILL.md`.
- Keep shipped skill edits out of scope until the wording direction is settled.

## Current Understanding

- Official Codex docs make `description` the key field for implicit skill invocation and advise concise, clear scope and front-loaded trigger words.
- Product-neutral workflow terms are preferable unless a Codex surface term such as `thread` removes ambiguity.
- The current `project-context` description is directionally correct but could better name thread resume, subagent follow-through, and durable repo files.

## Current State

- Added `docs/reference/model/skill-description-triggers.md` as the reusable reference owner for skill-description trigger guidance.
- Deep reasoning review recommends product-neutral wording that front-loads `resume`, `handoff`, `long-running`, `subagent`, `multi-agent`, `threads`, `task briefs`, `logs`, and `reference notes`.
- Shipped `skills/project-context/SKILL.md` now uses the narrowed product-neutral trigger wording.

## Next Step

- Push the repo update and refresh the local installed skill.

## Working Boundary

- `skills/project-context/SKILL.md`
- `docs/reference/model/skill-description-triggers.md`
