# worklog

**2026-06-22**

- Confirmed from current OpenAI Codex docs that skill implicit invocation depends on the `description`, full `SKILL.md` is loaded only after selection, and descriptions may be shortened when many skills are installed.
- Added a reusable reference doc for skill-description trigger wording.
- Kept the reference current-state-first and left shipped `project-context` wording unchanged pending deep reasoning review.
- Ran a deep reasoning pass on the proposal; recommendation is to avoid product-name wording and instead front-load product-neutral workflow triggers plus official terms such as `thread` and `subagent`.
- Updated `skills/project-context/SKILL.md` description and use-line wording to front-load `resume`, `handoff`, and `long-running repo work` while keeping `subagent follow-through` in the body and preserving the read-only/one-shot exclusion.
