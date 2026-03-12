from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


def load_runtime_shape_module():
    module_path = (
        Path(__file__).resolve().parents[2]
        / "skills"
        / "project-context"
        / "scripts"
        / "check_runtime_shape.py"
    )
    spec = importlib.util.spec_from_file_location("check_runtime_shape_migration", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


runtime_shape_check = load_runtime_shape_module()
FIXTURE_ROOT = (
    Path(__file__).resolve().parent / "fixtures" / "project_context_migration"
)


def runtime_for(case_root: Path) -> runtime_shape_check.RuntimePaths:
    return runtime_shape_check.RuntimePaths(
        repo_root=case_root,
        docs_root=case_root / "docs",
        memory_file=case_root / "docs" / "memory.md",
        reference_root=case_root / "docs" / "reference",
        task_root=case_root / "docs" / "tasks",
    )


def runtime_shape_failures(case_root: Path) -> list[str]:
    return runtime_shape_check.run_runtime_shape_checks(runtime_for(case_root))


def relative_files(case_root: Path) -> set[str]:
    return {
        str(path.relative_to(case_root))
        for path in case_root.rglob("*")
        if path.is_file()
    }


class LegacyMigrationFixtureTests(unittest.TestCase):
    def test_case_alpha_legacy_input_does_not_validate(self):
        case_root = FIXTURE_ROOT / "legacy" / "case-alpha"

        failures = runtime_shape_failures(case_root)

        self.assertTrue(
            any("Missing required runtime file" in item for item in failures)
        )
        self.assertTrue(
            any("Missing required runtime directory" in item for item in failures)
        )

    def test_case_beta_legacy_input_does_not_validate(self):
        case_root = FIXTURE_ROOT / "legacy" / "case-beta"

        failures = runtime_shape_failures(case_root)

        self.assertTrue(
            any("Missing required runtime file" in item for item in failures)
        )
        self.assertTrue(
            any("Missing required runtime directory" in item for item in failures)
        )


class MigratedMigrationFixtureTests(unittest.TestCase):
    def test_case_alpha_bad_output_fails_on_task_shape(self):
        case_root = FIXTURE_ROOT / "migrated" / "case-alpha-bad"

        failures = runtime_shape_failures(case_root)

        self.assertTrue(
            any("non-empty lines must start with '- '" in item for item in failures)
        )
        self.assertTrue(
            any("latest date block must contain only bullet lines" in item for item in failures)
        )

    def test_case_alpha_good_output_passes_and_preserves_leave_doc(self):
        case_root = FIXTURE_ROOT / "migrated" / "case-alpha-good"

        failures = runtime_shape_failures(case_root)
        files = relative_files(case_root)
        migration_brief = (
            case_root
            / "docs"
            / "tasks"
            / "2026"
            / "03-10"
            / "project-context-migration"
            / "BRIEF.md"
        ).read_text(encoding="utf-8")

        self.assertEqual(failures, [])
        self.assertIn("docs/memory.md", files)
        self.assertIn("docs/reference/deployment/deploy-runbook.md", files)
        self.assertIn("docs/reference/system/system-overview.md", files)
        self.assertIn("docs/tasks/2026/02-14/auth-spike/BRIEF.md", files)
        self.assertIn("docs/user-guide.md", files)
        self.assertNotIn("docs/reference/user-guide.md", files)
        self.assertIn("`TASK -> docs/tasks/2026/02-14/auth-spike/`", migration_brief)
        self.assertIn("2. auth spike를 dated task로 정리", migration_brief)
        self.assertIn("3. current reference state를 reference로 정리", migration_brief)
        self.assertNotIn("WORK -> docs/tasks", migration_brief)

    def test_case_beta_good_output_passes_and_keeps_uncertain_note_out_of_reference(self):
        case_root = FIXTURE_ROOT / "migrated" / "case-beta-good"

        failures = runtime_shape_failures(case_root)
        files = relative_files(case_root)

        self.assertEqual(failures, [])
        self.assertIn("docs/memory.md", files)
        self.assertIn("docs/reference/api/auth.md", files)
        self.assertIn("docs/reference/data/database-choice.md", files)
        self.assertIn("docs/tasks/2026/03-10/login-bug-investigation/BRIEF.md", files)
        self.assertIn("notes/misc.md", files)
        self.assertNotIn("docs/reference/misc.md", files)


if __name__ == "__main__":
    unittest.main()
