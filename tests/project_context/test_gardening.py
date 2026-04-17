from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path


def load_runtime_shape_module():
    module_path = (
        Path(__file__).resolve().parents[2]
        / "skills"
        / "project-context"
        / "scripts"
        / "check_runtime_shape.py"
    )
    spec = importlib.util.spec_from_file_location("check_runtime_shape_for_gardening", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_gardening_module():
    module_path = (
        Path(__file__).resolve().parents[2]
        / "skills"
        / "project-context"
        / "scripts"
        / "check_gardening.py"
    )
    spec = importlib.util.spec_from_file_location("check_gardening", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


runtime_shape = load_runtime_shape_module()
gardening = load_gardening_module()


@contextlib.contextmanager
def pushd(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


def make_valid_runtime_tree(root: Path) -> tuple[runtime_shape.RuntimePaths, Path]:
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
        "- sample\n",
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
    runtime = runtime_shape.RuntimePaths(
        repo_root=root,
        docs_root=docs_root,
        reference_root=reference_root,
        task_root=task_root,
    )
    return runtime, task_dir


def make_task_dir(root: Path, *, days_ago: int, slug: str) -> Path:
    day = date.today() - timedelta(days=days_ago)
    task_dir = root / "docs" / "tasks" / f"{day.year:04d}" / f"{day:%m-%d}" / slug
    task_dir.mkdir(parents=True, exist_ok=True)
    return task_dir


class GardeningCheckTests(unittest.TestCase):
    def test_empty_task_dir_warns(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, _ = make_valid_runtime_tree(root)
            empty_task = make_task_dir(root, days_ago=0, slug="empty-task")
            runtime_shape.set_display_root(runtime.repo_root)

            findings = gardening.check_empty_task_dirs(runtime)

            self.assertEqual(
                findings,
                [
                    gardening.Finding(
                        severity="WARN",
                        code="empty-task-dir",
                        path=runtime_shape.rel(empty_task),
                        suggestion="create BRIEF/logs or remove the directory",
                    )
                ],
            )

    def test_recent_status_respawn_warns(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, _ = make_valid_runtime_tree(root)
            task_dir = make_task_dir(root, days_ago=0, slug="legacy-task")
            (task_dir / "STATUS.md").write_text("# status\n", encoding="utf-8")

            findings = gardening.check_legacy_surface_respawn(runtime, recent_days=30)

            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].code, "legacy-surface-respawn")
            self.assertTrue(findings[0].path.endswith("STATUS.md"))

    def test_old_status_respawn_is_ignored(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, _ = make_valid_runtime_tree(root)
            task_dir = make_task_dir(root, days_ago=90, slug="old-legacy-task")
            (task_dir / "STATUS.md").write_text("# status\n", encoding="utf-8")

            findings = gardening.check_legacy_surface_respawn(runtime, recent_days=30)

            self.assertEqual(findings, [])

    def test_extra_task_doc_growth_reports_info(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, task_dir = make_valid_runtime_tree(root)
            for name in ("MODEL.md", "CONTRACTS.md", "SYSTEM_BOUNDARIES.md", "EXECUTION.md"):
                (task_dir / name).write_text("# sample\n", encoding="utf-8")

            findings = gardening.check_extra_task_doc_growth(
                runtime,
                warn_extra_docs=7,
                info_extra_docs=4,
            )

            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].severity, "INFO")
            self.assertEqual(findings[0].code, "task-extra-doc-growth")
            self.assertEqual(findings[0].detail, "4 extra top-level docs")
            self.assertEqual(
                findings[0].suggestion,
                "promote durable rules to docs/reference/**, or if this is one long-running task, keep the root canonical and move temporary working notes into working/ plus archive as needed",
            )

    def test_root_overlay_mixing_reports_info(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, task_dir = make_valid_runtime_tree(root)
            runtime_shape.set_display_root(runtime.repo_root)
            (task_dir / "MODEL.md").write_text("# model\n", encoding="utf-8")
            (task_dir / "CONTRACTS.md").write_text("# contracts\n", encoding="utf-8")
            (task_dir / "IMPROVEMENT_PLAN.md").write_text("# plan\n", encoding="utf-8")
            (task_dir / "REALTIME_POLICY.md").write_text("# policy\n", encoding="utf-8")

            findings = gardening.check_root_overlay_mixing(runtime)

            self.assertEqual(
                findings,
                [
                    gardening.Finding(
                        severity="INFO",
                        code="root-overlay-mixing",
                        path=runtime_shape.rel(task_dir),
                        suggestion="keep canonical docs at root, move temporary working notes into working/, and archive absorbed remnants instead of leaving them mixed at root",
                    )
                ],
            )

    def test_scope_path_list_sprawl_reports_info(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, task_dir = make_valid_runtime_tree(root)
            runtime_shape.set_display_root(runtime.repo_root)
            (task_dir / "BRIEF.md").write_text(
                "# Sample Task\n\n"
                "## Scope\n"
                "- `src/lib/patchMap/patchmap.svelte`\n"
                "- `src/lib/patchMap/recovery/policy.js`\n"
                "- `src/lib/patchMap/recovery/policy.test.js`\n"
                "- `src/lib/patchMap/recovery/runtime.js`\n"
                "- `src/lib/patchMap/recovery/runtime.test.js`\n",
                encoding="utf-8",
            )

            findings = gardening.check_scope_path_list_sprawl(runtime)

            self.assertEqual(
                findings,
                [
                    gardening.Finding(
                        severity="INFO",
                        code="scope-path-list-sprawl",
                        path=runtime_shape.rel(task_dir / "BRIEF.md"),
                        detail="5 path-only bullets in Scope",
                        suggestion=(
                            "keep Scope to 1-3 boundary bullets and move exact file lists to "
                            "Working Boundary only when they materially lower reopen cost"
                        ),
                    )
                ],
            )

    def test_scope_path_list_sprawl_ignores_short_or_descriptive_scope(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, task_dir = make_valid_runtime_tree(root)
            runtime_shape.set_display_root(runtime.repo_root)
            (task_dir / "BRIEF.md").write_text(
                "# Sample Task\n\n"
                "## Scope\n"
                "- patch map recovery boundary 정리\n"
                "- viewport/runtime policy alignment\n"
                "- `src/lib/patchMap/patchmap.svelte`\n",
                encoding="utf-8",
            )

            findings = gardening.check_scope_path_list_sprawl(runtime)

            self.assertEqual(findings, [])

    def test_main_returns_zero_and_supports_json_output(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, _ = make_valid_runtime_tree(root)
            task_dir = make_task_dir(root, days_ago=0, slug="legacy-task")
            (task_dir / "logs").mkdir()
            (task_dir / "BRIEF.md").write_text("# brief\n", encoding="utf-8")
            (task_dir / "logs" / "DECISIONS.md").write_text(
                "**2026-03-09**\n"
                "- 배경: sample\n"
                "- 선택지: sample\n"
                "- 결정: sample\n"
                "- 영향: sample\n",
                encoding="utf-8",
            )
            (task_dir / "logs" / "WORKLOG.md").write_text(
                "**2026-03-09**\n"
                "- sample\n",
                encoding="utf-8",
            )
            (task_dir / "STATUS.md").write_text("# status\n", encoding="utf-8")
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = gardening.main(["--json"], runtime=runtime)

            self.assertEqual(exit_code, 0)
            payload = json.loads(stdout.getvalue())
            self.assertEqual(payload[0]["code"], "legacy-surface-respawn")

    def test_main_detects_repo_root_from_cwd(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape.REPO_ROOT) as tmp:
            root = Path(tmp)
            make_valid_runtime_tree(root)
            stdout = io.StringIO()

            with pushd(root / "docs"), contextlib.redirect_stdout(stdout):
                exit_code = gardening.main([])

            self.assertEqual(exit_code, 0)
            self.assertIn("[OK]", stdout.getvalue())

    def test_report_findings_uses_info_header_for_info_only_results(self):
        findings = [
            gardening.Finding(
                severity="INFO",
                code="task-extra-doc-growth",
                path="docs/tasks/2026/03-09/sample-task",
                detail="4 extra top-level docs",
            )
        ]
        stdout = io.StringIO()

        with contextlib.redirect_stdout(stdout):
            gardening.report_findings(findings)

        output = stdout.getvalue()
        self.assertIn("[INFO] project-context gardening checks", output)
        self.assertNotIn("[WARN] project-context gardening checks", output)


if __name__ == "__main__":
    unittest.main()
