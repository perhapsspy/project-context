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
        reference_root=case_root / "docs" / "reference",
        task_root=case_root / "docs" / "tasks",
    )


def runtime_shape_failures(case_root: Path) -> list[str]:
    return runtime_shape_check.run_runtime_shape_checks(runtime_for(case_root))


class LegacyMigrationFixtureTests(unittest.TestCase):
    def test_case_alpha_legacy_input_does_not_validate(self):
        case_root = FIXTURE_ROOT / "legacy" / "case-alpha"

        failures = runtime_shape_failures(case_root)

        self.assertTrue(
            any("Missing required runtime directory" in item for item in failures)
        )

    def test_case_beta_legacy_input_does_not_validate(self):
        case_root = FIXTURE_ROOT / "legacy" / "case-beta"

        failures = runtime_shape_failures(case_root)

        self.assertTrue(
            any("Missing required runtime directory" in item for item in failures)
        )


class MigratedMigrationFixtureTests(unittest.TestCase):
    def assert_task_core_files_exist(self, task_dir: Path):
        self.assertTrue((task_dir / "BRIEF.md").is_file())
        self.assertTrue((task_dir / "logs" / "DECISIONS.md").is_file())
        self.assertTrue((task_dir / "logs" / "WORKLOG.md").is_file())

    def assert_no_legacy_task_surfaces(self, case_root: Path):
        self.assertEqual(list((case_root / "docs" / "tasks").rglob("STATUS.md")), [])
        self.assertEqual(
            list((case_root / "docs" / "tasks").rglob("MEMORY-CANDIDATES.md")),
            [],
        )

    def test_case_alpha_bad_output_fails_on_task_shape(self):
        case_root = FIXTURE_ROOT / "migrated" / "case-alpha-bad"

        failures = runtime_shape_failures(case_root)

        self.assertTrue(
            any("latest date block must contain only bullet lines" in item for item in failures)
        )

    def test_case_alpha_good_output_passes_and_preserves_leave_doc(self):
        case_root = FIXTURE_ROOT / "migrated" / "case-alpha-good"
        migration_task = (
            case_root / "docs" / "tasks" / "2026" / "03-10" / "project-context-migration"
        )
        auth_spike_task = (
            case_root / "docs" / "tasks" / "2026" / "02-14" / "auth-spike"
        )

        failures = runtime_shape_failures(case_root)

        self.assertEqual(failures, [])
        self.assert_task_core_files_exist(migration_task)
        self.assert_task_core_files_exist(auth_spike_task)
        self.assert_no_legacy_task_surfaces(case_root)
        self.assertTrue(
            (case_root / "docs" / "reference" / "system" / "system-overview.md").is_file()
        )
        self.assertTrue(
            (case_root / "docs" / "reference" / "deployment" / "deploy-runbook.md").is_file()
        )
        self.assertTrue((case_root / "docs" / "user-guide.md").is_file())
        self.assertFalse((case_root / "docs" / "memory.md").exists())
        self.assertFalse((case_root / "docs" / "system.md").exists())
        self.assertFalse((case_root / "runbooks" / "deploy.md").exists())
        self.assertFalse((case_root / "docs" / "reference" / "user-guide.md").exists())

    def test_case_beta_good_output_passes_and_keeps_uncertain_note_out_of_reference(self):
        case_root = FIXTURE_ROOT / "migrated" / "case-beta-good"
        migration_task = (
            case_root / "docs" / "tasks" / "2026" / "03-10" / "project-context-migration"
        )
        login_bug_task = (
            case_root / "docs" / "tasks" / "2026" / "03-10" / "login-bug-investigation"
        )

        failures = runtime_shape_failures(case_root)

        self.assertEqual(failures, [])
        self.assert_task_core_files_exist(migration_task)
        self.assert_task_core_files_exist(login_bug_task)
        self.assert_no_legacy_task_surfaces(case_root)
        self.assertTrue((case_root / "AGENTS.md").is_file())
        self.assertFalse((case_root / "docs" / "memory.md").exists())
        self.assertTrue((case_root / "docs" / "reference" / "api" / "auth.md").is_file())
        self.assertTrue(
            (case_root / "docs" / "reference" / "data" / "database-choice.md").is_file()
        )
        self.assertFalse((case_root / "docs" / "api" / "auth.md").exists())
        self.assertFalse((case_root / "tasks" / "login-bug.md").exists())
        self.assertFalse((case_root / "docs" / "reference" / "misc.md").exists())
        self.assertTrue((case_root / "notes" / "misc.md").exists())


if __name__ == "__main__":
    unittest.main()
