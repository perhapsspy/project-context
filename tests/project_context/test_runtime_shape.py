from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import sys
import tempfile
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
    spec = importlib.util.spec_from_file_location("check_runtime_shape", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


runtime_shape_check = load_runtime_shape_module()


@contextlib.contextmanager
def pushd(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


def make_valid_runtime_tree(root: Path) -> tuple[runtime_shape_check.RuntimePaths, Path]:
    docs_root = root / "docs"
    reference_root = docs_root / "reference"
    task_root = docs_root / "tasks"
    task_dir = task_root / "2026" / "03-09" / "sample-task"
    logs = task_dir / "logs"

    reference_root.mkdir(parents=True)
    logs.mkdir(parents=True)
    (task_dir / "BRIEF.md").write_text(
        "# Sample Task\n\n"
        "## Goal\n"
        "- sample\n\n"
        "## Current State\n"
        "- sample\n"
        "- latest validation: none\n",
        encoding="utf-8",
    )
    (logs / "DECISIONS.md").write_text(
        "**2026-03-09**\n"
        "- 배경: sample\n"
        "- 선택지: sample\n"
        "- 결정: sample\n"
        "- 영향: sample\n",
        encoding="utf-8",
    )
    (logs / "WORKLOG.md").write_text(
        "**2026-03-09**\n"
        "- sample\n",
        encoding="utf-8",
    )
    runtime = runtime_shape_check.RuntimePaths(
        repo_root=root,
        docs_root=docs_root,
        reference_root=reference_root,
        task_root=task_root,
    )
    return runtime, task_dir


def write_reference_file(root: Path, relative_path: str) -> Path:
    path = root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# sample\n", encoding="utf-8")
    return path


class ReferenceShapeTests(unittest.TestCase):
    def test_missing_reference_directory_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            reference_root = Path(tmp) / "reference"

            failures = runtime_shape_check.check_reference_contract(reference_root)

            self.assertEqual(
                failures,
                [f"Missing required runtime directory: {runtime_shape_check.rel(reference_root)}"],
            )

    def test_empty_reference_directory_passes(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            reference_root = Path(tmp) / "reference"
            reference_root.mkdir()

            self.assertEqual(runtime_shape_check.check_reference_contract(reference_root), [])

    def test_kebab_case_reference_paths_pass(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            reference_root = Path(tmp) / "reference"
            write_reference_file(reference_root, "external-api-conventions.md")
            write_reference_file(reference_root, "integrations/github/auth.md")
            write_reference_file(reference_root, "domains/external-api/error-handling.md")

            failures = runtime_shape_check.check_reference_contract(reference_root)

            self.assertEqual(failures, [])

    def test_invalid_reference_directory_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            reference_root = Path(tmp) / "reference"
            invalid_path = write_reference_file(reference_root, "ProcessDocs/playbook.md")

            failures = runtime_shape_check.check_reference_contract(reference_root)

            self.assertEqual(
                failures,
                [f"Invalid reference directory (kebab-case required): {runtime_shape_check.rel(invalid_path)}"],
            )


class TaskShapeTests(unittest.TestCase):
    def test_missing_task_directory_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            task_root = Path(tmp) / "tasks"

            failures = runtime_shape_check.check_task_contract(task_root)

            self.assertEqual(
                failures,
                [f"Missing required runtime directory: {runtime_shape_check.rel(task_root)}"],
            )

    def test_invalid_task_year_directory_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            task_root = Path(tmp) / "tasks"
            (task_root / "26" / "03-09" / "sample-task").mkdir(parents=True)

            failures = runtime_shape_check.check_task_contract(task_root)

            self.assertEqual(
                failures,
                [
                    "Invalid task year directory (expected yyyy): "
                    f"{runtime_shape_check.rel(task_root / '26')}"
                ],
            )

    def test_invalid_task_date_format_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            task_root = Path(tmp) / "tasks"
            (task_root / "2026" / "3-9" / "sample-task").mkdir(parents=True)

            failures = runtime_shape_check.check_task_contract(task_root)

            self.assertEqual(
                failures,
                [
                    "Invalid task date directory (expected mm-dd): "
                    f"{runtime_shape_check.rel(task_root / '2026' / '3-9')}"
                ],
            )

    def test_impossible_task_date_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            task_root = Path(tmp) / "tasks"
            (task_root / "2026" / "02-31" / "sample-task").mkdir(parents=True)

            failures = runtime_shape_check.check_task_contract(task_root)

            self.assertEqual(
                failures,
                [
                    "Invalid task date directory (not a real date): "
                    f"{runtime_shape_check.rel(task_root / '2026' / '02-31')}"
                ],
            )

    def test_invalid_task_slug_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            task_root = Path(tmp) / "tasks"
            (task_root / "2026" / "03-09" / "BadSlug").mkdir(parents=True)

            failures = runtime_shape_check.check_task_contract(task_root)

            self.assertEqual(
                failures,
                [
                    "Invalid task slug (kebab-case required): "
                    f"{runtime_shape_check.rel(task_root / '2026' / '03-09' / 'BadSlug')}"
                ],
            )

    def test_missing_task_core_file_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            _, task_dir = make_valid_runtime_tree(root)
            missing_brief = task_dir / "BRIEF.md"
            missing_brief.unlink()

            failures = runtime_shape_check.task_failures(task_dir)

            self.assertIn(
                f"Missing task core file: {runtime_shape_check.rel(missing_brief)}",
                failures,
            )

    def test_task_core_file_directory_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            _, task_dir = make_valid_runtime_tree(root)
            decisions = task_dir / "logs" / "DECISIONS.md"
            decisions.unlink()
            decisions.mkdir()

            failures = runtime_shape_check.task_failures(task_dir)

            self.assertIn(
                f"Task core file is not a file: {runtime_shape_check.rel(decisions)}",
                failures,
            )

    def test_extra_task_local_doc_does_not_fail(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            _, task_dir = make_valid_runtime_tree(root)
            (task_dir / "AUDIT-MAP.md").write_text("# audit map\n", encoding="utf-8")

            failures = runtime_shape_check.task_failures(task_dir)

            self.assertEqual(failures, [])

    def test_main_keeps_default_output(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, _ = make_valid_runtime_tree(root)
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = runtime_shape_check.main([], runtime=runtime)

            self.assertEqual(exit_code, 0)
            output = stdout.getvalue().strip()
            self.assertIn("[OK]", output)
            self.assertIn("project-context current runtime shape checks", output)

    def test_main_failure_output_includes_runtime_shape_failures(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, _ = make_valid_runtime_tree(root)
            runtime = runtime_shape_check.RuntimePaths(
                repo_root=runtime.repo_root,
                docs_root=runtime.docs_root,
                reference_root=root / "missing-reference",
                task_root=runtime.task_root,
            )
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = runtime_shape_check.main([], runtime=runtime)

            self.assertEqual(exit_code, 1)
            output_lines = stdout.getvalue().strip().splitlines()
            self.assertEqual(
                output_lines[0],
                "[FAIL] project-context current runtime shape checks",
            )
            self.assertIn(
                f"- Missing required runtime directory: {runtime_shape_check.rel(runtime.reference_root)}",
                output_lines,
            )

    def test_main_detects_repo_root_from_cwd_when_runtime_is_not_passed(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            make_valid_runtime_tree(root)
            stdout = io.StringIO()

            with pushd(root / "docs"), contextlib.redirect_stdout(stdout):
                exit_code = runtime_shape_check.main([])

            self.assertEqual(exit_code, 0)
            output = stdout.getvalue().strip()
            self.assertIn("[OK]", output)

    def test_main_repo_root_override_avoids_nested_docs_ambiguity(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            make_valid_runtime_tree(root)
            nested = root / "packages" / "child"
            (nested / "docs" / "reference").mkdir(parents=True)
            stdout = io.StringIO()

            with pushd(nested), contextlib.redirect_stdout(stdout):
                exit_code = runtime_shape_check.main(["--repo-root", str(root)])

            self.assertEqual(exit_code, 0)
            output = stdout.getvalue().strip()
            self.assertIn("[OK]", output)


class LogShapeTests(unittest.TestCase):
    def test_worklog_requires_latest_date_block(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            worklog = Path(tmp) / "WORKLOG.md"
            worklog.write_text("# WORKLOG\n- legacy\n", encoding="utf-8")

            failures = runtime_shape_check.worklog_file_failures(worklog)

            self.assertEqual(
                failures,
                [f"{runtime_shape_check.rel(worklog)}: missing `**YYYY-MM-DD**` heading"],
            )

    def test_worklog_rejects_empty_latest_date_block(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            worklog = Path(tmp) / "WORKLOG.md"
            worklog.write_text("**2026-03-09**\n", encoding="utf-8")

            failures = runtime_shape_check.worklog_file_failures(worklog)

            self.assertEqual(
                failures,
                [f"{runtime_shape_check.rel(worklog)}: latest date block is empty"],
            )

    def test_worklog_only_latest_date_block_is_validated(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            worklog = Path(tmp) / "WORKLOG.md"
            worklog.write_text(
                "**2026-03-08**\n"
                "legacy bad line\n\n"
                "**2026-03-09**\n"
                "- current valid line\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.worklog_file_failures(worklog)

            self.assertEqual(failures, [])

    def test_decisions_latest_block_rejects_non_bullet_text(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            decisions = Path(tmp) / "DECISIONS.md"
            decisions.write_text(
                "**2026-03-09**\n"
                "- 배경: sample\n"
                "freeform note\n"
                "- 결정: sample\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.decisions_log_failures(decisions)

            self.assertEqual(
                failures,
                [
                    f"{runtime_shape_check.rel(decisions)}: latest date block must contain only bullet lines"
                ],
            )


class SecretShapeTests(unittest.TestCase):
    def test_non_markdown_text_file_is_scanned(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            docs_root = Path(tmp)
            artifact = docs_root / "artifact.txt"
            artifact.write_text("api_key = SECRETSECRET123456", encoding="utf-8")

            failures = runtime_shape_check.check_secret_marker_scan(docs_root)

            self.assertEqual(
                failures,
                [f"Possible secret-like marker found in {runtime_shape_check.rel(artifact)}"],
            )

    def test_binary_file_is_skipped(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            docs_root = Path(tmp)
            artifact = docs_root / "artifact.bin"
            artifact.write_bytes(b"\x00\x01api_key = SECRETSECRET123456")

            failures = runtime_shape_check.check_secret_marker_scan(docs_root)

            self.assertEqual(failures, [])


class PortablePathShapeTests(unittest.TestCase):
    def test_repo_root_absolute_path_is_scanned(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            runtime, _ = make_valid_runtime_tree(Path(tmp))
            artifact = runtime.reference_root / "portability.md"
            artifact.write_text(
                f"Use {runtime.repo_root}/docs/reference/portability.md\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.check_portable_path_scan(runtime)

            self.assertEqual(
                failures,
                [
                    "Possible absolute or environment-specific path marker found in "
                    f"{runtime_shape_check.rel(artifact)}"
                ],
            )

    def test_environment_home_path_is_scanned(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            runtime, task_dir = make_valid_runtime_tree(Path(tmp))
            artifact = task_dir / "BRIEF.md"
            artifact.write_text(
                "- latest validation: copied from ~/work/project/docs/tasks/sample\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.check_portable_path_scan(runtime)

            self.assertEqual(
                failures,
                [
                    "Possible absolute or environment-specific path marker found in "
                    f"{runtime_shape_check.rel(artifact)}"
                ],
            )

    def test_repo_relative_and_placeholders_are_allowed(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            runtime, task_dir = make_valid_runtime_tree(Path(tmp))
            artifact = task_dir / "BRIEF.md"
            artifact.write_text(
                "- related docs: docs/reference/portability.md, <repo-root>/docs/tasks/sample\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.check_portable_path_scan(runtime)

            self.assertEqual(failures, [])

    def test_task_logs_are_scanned_for_portable_paths(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            runtime, task_dir = make_valid_runtime_tree(Path(tmp))
            artifact = task_dir / "logs" / "WORKLOG.md"
            artifact.write_text(
                "**2026-03-09**\n"
                f"- preserved source path: {runtime.repo_root}/legacy/docs/note.md\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.check_portable_path_scan(runtime)

            self.assertEqual(
                failures,
                [
                    "Possible absolute or environment-specific path marker found in "
                    f"{runtime_shape_check.rel(artifact)}"
                ],
            )

    def test_task_decisions_log_is_scanned_for_portable_paths(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            runtime, task_dir = make_valid_runtime_tree(Path(tmp))
            artifact = task_dir / "logs" / "DECISIONS.md"
            artifact.write_text(
                "**2026-03-09**\n"
                f"- 배경: imported from {runtime.repo_root}/legacy/docs/decision.md\n"
                "- 선택지: sample\n"
                "- 결정: sample\n"
                "- 영향: sample\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.check_portable_path_scan(runtime)

            self.assertEqual(
                failures,
                [
                    "Possible absolute or environment-specific path marker found in "
                    f"{runtime_shape_check.rel(artifact)}"
                ],
            )

    def test_nested_task_artifacts_are_not_scanned_for_portable_paths(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            runtime, task_dir = make_valid_runtime_tree(Path(tmp))
            artifact = (
                task_dir
                / "ARTIFACTS"
                / "case-alpha"
                / "docs"
                / "tasks"
                / "2026"
                / "03-09"
                / "legacy-task"
                / "BRIEF.md"
            )
            artifact.parent.mkdir(parents=True)
            artifact.write_text(
                f"- source path: {runtime.repo_root}/legacy/docs/brief.md\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.check_portable_path_scan(runtime)

            self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
