---
name: project-context-migration
description: Audit scattered repository docs and notes, then move only the right working context into the `project-context` structure.
---

# Project Context Migration

## Purpose

Audit scattered repository docs and notes before moving the right working context into `project-context`. Apply the main [project-context contract](../project-context/SKILL.md) first. Use this companion only for existing legacy context, not to initialize an empty repo.

## Classification

- `TASK`: material that belongs in agent working context but is task-local, historical, exploratory, unresolved, or not trusted as current truth.
- `REFERENCE`: current trusted rules, facts, or shared contracts another task can directly reuse.
- `LEAVE`: product/user/team docs, human-facing top-level notes, and origin/about/repository narrative that do not belong in agent working context.
- `ARCHIVE`: stale duplicates or superseded docs only when cleanup is authorized; it is not a default `project-context` destination.

`LEAVE` is a valid result. If membership in agent working context is uncertain, use `LEAVE`; if membership is clear but current truth or adoption is uncertain, use `TASK`. Do not promote content to `REFERENCE` merely because it is technical.

## Migration Contract

Inventory candidate sources read-only, then resolve each source or separable part to a classification, currentness, existing owner, target or leave decision, and reason. Persist this map in one dated migration task before rewriting, moving, archiving, or deleting content.

Apply only the resolved map. Preserve existing canonical and human-facing owners; merge overlapping working context into one preferred task or reference owner. Rewrite current reference truth instead of copying timeline noise, and keep comparison detail, rationale, uncertainty, and change trace in the migration task.

Preserve shipped authority and human-facing documents outside project-context. Normalize saved paths to repo-relative paths or stable placeholders. If an item lacks a trustworthy date, use the migration date and record that uncertainty in its task.

Run the main runtime-shape checker, then reconcile the map and spot-review representative or high-risk classifications and owner transitions. Shape success does not prove migration correctness.

## Completion

Finish when every inventoried candidate has a disposition, uncertain material remains isolated, human-facing material is preserved, and both destination shape and representative mappings have been checked.
