# Project-context

[Korean](README.md) | [English](README.en.md)

> Note: This English text was translated and edited with LLM assistance. If anything reads awkwardly, please check the Korean version or open an issue.

`project-context` is a skill that helps coding agents keep working context in the project, so future sessions can pick up the work without rebuilding the state from scratch. It leaves the minimum useful reference docs and task records as files, so humans can read and edit them directly without relying on a separate system.

- `docs/reference/`: topic-scoped domain context reused across tasks
- `docs/tasks/...`: dated task records for most real work; each task keeps `BRIEF.md` as the current overview entrypoint and adds logs or task-specific docs only when needed

The optional `project-context-migration` skill is only for the first cleanup/adoption pass in an existing repository where docs are scattered or only partially moved into this structure.

## Quick Start

**Install**

```bash
npx skills add perhapsspy/project-context
```

Or copy the skill(s) you need directly into `skills`. For migration/adoption work, copy both `project-context` and `project-context-migration`.

**Set as a default in `AGENTS.md`**

```md
- Always use $project-context for work
```

As an operating habit, when the skill updates task logs, use the bundled `skills/project-context/scripts/task_logs.py` flow for append/check instead of making direct patches to `logs/*.md` by default.

## Prompt Examples

- General work after wiring it into `AGENTS.md`: `Fix the login redirect bug`
- When mentioning it directly: `$project-context implement the login page`
- To continue a specific task: `Continue docs/tasks/2026/03-11/login`
- To migrate an existing doc structure: `$project-context-migration move the existing docs and context into $project-context`

## Good Skills to Use Together

- [`project-context`](https://github.com/perhapsspy/project-context): keep working context in the repo so later sessions can resume quickly
- [`structure-first`](https://github.com/perhapsspy/structure-first): organize code so the primary success path reads top-down

## Support

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/perhapsspy)

## License

[MIT](LICENSE)
