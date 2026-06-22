# skill description triggers

이 문서는 skill description을 쓸 때의 현재 기준 맥락을 담는다. 세부 runtime shape와 실행 계약은 shipped skill이 소유한다.

## source basis

- OpenAI Codex docs say skills are available across CLI, IDE extension, and Codex app.
- Codex starts skill discovery from each skill's `name`, `description`, and path, then reads the full `SKILL.md` only after choosing the skill.
- Implicit invocation happens when the user task matches the skill `description`.
- If many skills are installed, Codex may shorten descriptions first; key trigger words should be front-loaded.
- `allow_implicit_invocation` defaults to true unless skill metadata disables it.
- `AGENTS.md` is durable project guidance. Use it for repo conventions that should apply every time, not as the only way to make a reusable workflow discoverable.

Official references:

- https://developers.openai.com/codex/skills
- https://developers.openai.com/codex/concepts/customization
- https://developers.openai.com/codex/guides/agents-md

## description criteria

- Say exactly when the skill should trigger, not just what topic it knows.
- Put the strongest trigger nouns early enough to survive description shortening.
- Name the durable work surface when it matters: repo files, task brief, handoff, logs, reference docs, or equivalent owner.
- Prefer product-neutral workflow terms when they describe the same trigger across surfaces.
- Use product or surface names only when they remove ambiguity. For example, `thread resume` can be useful because thread is the documented session unit; naming a specific product is usually weaker than naming the workflow.
- Keep negative boundaries in the body when they prevent over-triggering, especially read-only questions, one-shot inspections, and migration/adoption boundaries.

## wording bias for this repo

- `project-context` should trigger on durable repo context that must survive the current chat or agent run.
- Strong trigger words are `resume`, `thread`, `handoff`, `long-running`, `subagent`, `task brief`, `logs`, `reference`, and `repo context`.
- Avoid making the description sound like every coding task needs the skill.
- Avoid relying on `AGENTS.md` routing as the only discovery path; it is useful project guidance, but the skill description still needs to stand alone.
