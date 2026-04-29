# Project-context

[Korean](README.md) | [English](README.en.md)

> Note: This English text was translated and edited with LLM assistance. If anything reads awkwardly, please check the Korean version or open an issue.

`project-context` is a skill that helps coding agents keep working context in the project, so future sessions can pick up the work without rebuilding the state from scratch. It leaves the minimum useful reference docs and task records as files, so humans can read and edit them directly without relying on a separate system.

- `docs/reference/`: current trusted reference context such as principles, rules, and recent reliable facts
- `docs/tasks/...`: dated task records for most real work

## When to Use

- New repository starting durable work: use `project-context` directly to create `docs/reference/` and a dated task.
- Existing repository with scattered docs: use `project-context-migration` for the first classification and move only the useful context.
- Read-only questions, one-shot inspections, or short answers: do not create files.

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

## Prompt Examples

- General work after wiring it into `AGENTS.md`: `Fix the login redirect bug`
- When mentioning it directly: `$project-context implement the login page`
- To continue a specific task: `Continue docs/tasks/2026/03-11/login`
- To migrate an existing doc structure: `$project-context-migration move the existing docs and context into $project-context`

## Good Record Shape

- `BRIEF.md`: only current trusted facts, current state, and the nearest next action.
- `WORKLOG.md`: meaningful work batches and evidence. It is not a command-by-command transcript.
- `DECISIONS.md`: only decisions that affect future interpretation, in four bullets: `Background / Decision / Why / Impact`.

See [`docs/examples.en.md`](docs/examples.en.md) for concrete examples.

## Good Skills to Use Together

- [`project-context`](https://github.com/perhapsspy/project-context): keep working context in the repo so later sessions can resume quickly
- [`structure-first`](https://github.com/perhapsspy/structure-first): organize code so the primary success path reads top-down

## Support

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/perhapsspy)

## License

[MIT](LICENSE)
