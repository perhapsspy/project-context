# Project-context

[Korean](README.md) | [English](README.en.md)

> Note: This English text was translated and edited with LLM assistance. If anything reads awkwardly, please check the Korean version or open an issue.

`project-context` is a skill that helps coding agents keep working context in the project, so future sessions can pick up the work without rebuilding the state from scratch. It leaves the minimum useful notes, reference docs, and task records as files, so humans can read and edit them directly without relying on a separate system.

- `docs/memory.md`: global working memory that is worth reloading often; compresses global rules, current phase, temporary constraints, and currently active cross-task conditions
- `docs/reference/`: topic-scoped domain context reused across tasks
- `docs/tasks/...`: dated task records for most real work

The optional `project-context-migration` skill is only for the first cleanup/adoption pass in an existing repository where docs are scattered or only partially moved into this structure.

## Skill List

- `project-context`: the main skill
- `project-context-migration`: an optional skill used only for the first cleanup/adoption pass in a repository with scattered existing docs

## Quick Start

**Install**

```bash
npx skills add perhapsspy/project-context
```

Or copy the skill(s) you need directly into `skills`.

**Set as a default in `AGENTS.md`**

```md
- Always use $project-context for work
```

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
