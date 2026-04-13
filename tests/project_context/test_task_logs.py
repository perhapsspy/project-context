from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path


def load_task_logs_module():
    module_path = (
        Path(__file__).resolve().parents[2]
        / "skills"
        / "project-context"
        / "scripts"
        / "task_logs.py"
    )
    spec = importlib.util.spec_from_file_location("task_logs", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


task_logs = load_task_logs_module()


def make_task_dir(root: Path) -> Path:
    task_dir = root / "docs" / "tasks" / "2026" / "04-05" / "sample-task"
    (task_dir / "logs").mkdir(parents=True)
    (task_dir / "BRIEF.md").write_text("# Sample Task\n", encoding="utf-8")
    return task_dir


def rel_display(*parts: str) -> str:
    return str(Path(*parts))


class AppendLogTests(unittest.TestCase):
    def test_append_creates_new_log_with_heading_and_bullet(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = task_logs.main(
                    [
                        "worklog",
                        "append",
                        "--task-root",
                        str(task_dir),
                        "--date",
                        "2026-04-05",
                        "--bullet",
                        "created the first entry",
                    ]
                )

            self.assertEqual(exit_code, 0)
            self.assertIn(
                f"[OK] appended {rel_display('docs', 'tasks', '2026', '04-05', 'sample-task', 'logs', 'WORKLOG.md')}",
                stdout.getvalue(),
            )
            self.assertEqual(
                (task_dir / "logs" / "WORKLOG.md").read_text(encoding="utf-8"),
                "**2026-04-05**\n- created the first entry\n",
            )

    def test_append_uses_same_latest_block_for_same_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            worklog = task_dir / "logs" / "WORKLOG.md"
            worklog.write_text(
                "**2026-04-05**\n"
                "- first entry\n",
                encoding="utf-8",
            )

            task_logs.append_log_bullet(worklog, "2026-04-05", "second entry")

            self.assertEqual(
                worklog.read_text(encoding="utf-8"),
                "**2026-04-05**\n"
                "- first entry\n"
                "- second entry\n",
            )

    def test_append_starts_new_block_for_later_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            worklog = task_dir / "logs" / "WORKLOG.md"
            worklog.write_text(
                "**2026-04-04**\n"
                "- first entry\n",
                encoding="utf-8",
            )

            task_logs.append_log_bullet(worklog, "2026-04-05", "second day")

            self.assertEqual(
                worklog.read_text(encoding="utf-8"),
                "**2026-04-04**\n"
                "- first entry\n"
                "\n"
                "**2026-04-05**\n"
                "- second day\n",
            )

    def test_append_rejects_older_date_than_latest_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            worklog = task_dir / "logs" / "WORKLOG.md"
            worklog.write_text(
                "**2026-04-05**\n"
                "- latest entry\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(task_logs.LogToolError, "cannot append older date"):
                task_logs.append_log_bullet(worklog, "2026-04-04", "older entry")

    def test_append_rejects_missing_task_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing_task_dir = Path(tmp) / "docs" / "tasks" / "2026" / "04-05" / "missing-task"
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = task_logs.main(
                    [
                        "worklog",
                        "append",
                        "--task-root",
                        str(missing_task_dir),
                        "--date",
                        "2026-04-05",
                        "--bullet",
                        "should fail",
                    ]
                )

            self.assertEqual(exit_code, 1)
            self.assertIn(
                f"missing task root: {rel_display('docs', 'tasks', '2026', '04-05', 'missing-task')}",
                stdout.getvalue(),
            )
            self.assertFalse(missing_task_dir.exists())

    def test_append_rejects_task_without_brief(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = Path(tmp) / "docs" / "tasks" / "2026" / "04-05" / "sample-task"
            (task_dir / "logs").mkdir(parents=True)
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = task_logs.main(
                    [
                        "worklog",
                        "append",
                        "--task-root",
                        str(task_dir),
                        "--date",
                        "2026-04-05",
                        "--bullet",
                        "should fail",
                    ]
                )

            self.assertEqual(exit_code, 1)
            self.assertIn(
                f"missing task brief: {rel_display('docs', 'tasks', '2026', '04-05', 'sample-task', 'BRIEF.md')}",
                stdout.getvalue(),
            )

    def test_append_accepts_utf8_bom_prefixed_latest_heading(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            worklog = task_dir / "logs" / "WORKLOG.md"
            worklog.write_bytes(b"\xef\xbb\xbf**2026-04-05**\n- first entry\n")

            task_logs.append_log_bullet(worklog, "2026-04-05", "second entry")

            self.assertEqual(
                worklog.read_text(encoding="utf-8"),
                "\ufeff**2026-04-05**\n"
                "- first entry\n"
                "- second entry\n",
            )

    def test_append_decision_writes_one_four_line_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = task_logs.main(
                    [
                        "decision",
                        "append",
                        "--task-root",
                        str(task_dir),
                        "--date",
                        "2026-04-05",
                        "--background",
                        "배경: sample",
                        "--options",
                        "선택지: sample",
                        "--decision",
                        "결정: sample",
                        "--impact",
                        "영향: sample",
                    ]
                )

            self.assertEqual(exit_code, 0)
            self.assertIn(
                f"[OK] appended {rel_display('docs', 'tasks', '2026', '04-05', 'sample-task', 'logs', 'DECISIONS.md')}",
                stdout.getvalue(),
            )
            self.assertEqual(
                (task_dir / "logs" / "DECISIONS.md").read_text(encoding="utf-8"),
                "**2026-04-05**\n"
                "- 배경: sample\n"
                "- 선택지: sample\n"
                "- 결정: sample\n"
                "- 영향: sample\n",
            )

    def test_append_decision_starts_a_new_block_even_on_same_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            decisions = task_dir / "logs" / "DECISIONS.md"
            decisions.write_text(
                "**2026-04-05**\n"
                "- 배경: first\n"
                "- 선택지: first\n"
                "- 결정: first\n"
                "- 영향: first\n",
                encoding="utf-8",
            )

            task_logs.append_decision_block(
                decisions,
                "2026-04-05",
                ("배경: second", "선택지: second", "결정: second", "영향: second"),
            )

            self.assertEqual(
                decisions.read_text(encoding="utf-8"),
                "**2026-04-05**\n"
                "- 배경: first\n"
                "- 선택지: first\n"
                "- 결정: first\n"
                "- 영향: first\n"
                "\n"
                "**2026-04-05**\n"
                "- 배경: second\n"
                "- 선택지: second\n"
                "- 결정: second\n"
                "- 영향: second\n",
            )

    def test_append_decision_starts_new_valid_block_after_malformed_latest_decision_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            decisions = task_dir / "logs" / "DECISIONS.md"
            decisions.write_text(
                "**2026-04-05**\n"
                "- 배경: only one line\n",
                encoding="utf-8",
            )

            task_logs.append_decision_block(
                decisions,
                "2026-04-05",
                ("배경: second", "선택지: second", "결정: second", "영향: second"),
            )

            self.assertEqual(
                decisions.read_text(encoding="utf-8"),
                "**2026-04-05**\n"
                "- 배경: only one line\n"
                "\n"
                "**2026-04-05**\n"
                "- 배경: second\n"
                "- 선택지: second\n"
                "- 결정: second\n"
                "- 영향: second\n",
            )
            block = task_logs.read_latest_block_for_log(decisions, "DECISIONS")
            self.assertEqual(block.bullet_lines, ("- 배경: second", "- 선택지: second", "- 결정: second", "- 영향: second"))


class LatestBlockTests(unittest.TestCase):
    def test_tail_prints_latest_block_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            worklog = task_dir / "logs" / "WORKLOG.md"
            worklog.write_text(
                "**2026-04-04**\n"
                "- older entry\n"
                "\n"
                "**2026-04-05**\n"
                "- latest entry\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = task_logs.main(
                    [
                        "worklog",
                        "tail",
                        "--task-root",
                        str(task_dir),
                    ]
                )

            self.assertEqual(exit_code, 0)
            self.assertEqual(
                stdout.getvalue().strip(),
                "**2026-04-05**\n- latest entry",
            )

    def test_decision_tail_rejects_malformed_latest_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            decisions = task_dir / "logs" / "DECISIONS.md"
            decisions.write_text(
                "**2026-04-05**\n"
                "- 배경: only one line\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = task_logs.main(
                    [
                        "decision",
                        "tail",
                        "--task-root",
                        str(task_dir),
                    ]
                )

            self.assertEqual(exit_code, 1)
            self.assertIn("latest decision block must contain exactly 4 bullet lines", stdout.getvalue())

    def test_read_latest_block_ignores_invalid_older_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            worklog = task_dir / "logs" / "WORKLOG.md"
            worklog.write_text(
                "**2026-04-04**\n"
                "legacy non-bullet\n"
                "\n"
                "**2026-04-05**\n"
                "- latest entry\n",
                encoding="utf-8",
            )

            block = task_logs.read_latest_block(worklog)

            self.assertEqual(block.heading, "**2026-04-05**")
            self.assertEqual(block.bullet_lines, ("- latest entry",))

    def test_append_worklog_starts_new_valid_block_after_malformed_latest_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            worklog = task_dir / "logs" / "WORKLOG.md"
            worklog.write_text(
                "**2026-04-05**\n"
                "legacy note\n",
                encoding="utf-8",
            )

            task_logs.append_log_bullet(worklog, "2026-04-05", "latest entry")

            self.assertEqual(
                worklog.read_text(encoding="utf-8"),
                "**2026-04-05**\n"
                "legacy note\n"
                "\n"
                "**2026-04-05**\n"
                "- latest entry\n",
            )
            block = task_logs.read_latest_block_for_log(worklog, "WORKLOG")
            self.assertEqual(block.bullet_lines, ("- latest entry",))

    def test_append_worklog_recovers_when_no_heading_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            worklog = task_dir / "logs" / "WORKLOG.md"
            worklog.write_text("legacy note only", encoding="utf-8")

            task_logs.append_log_bullet(worklog, "2026-04-05", "latest entry")

            self.assertEqual(
                worklog.read_text(encoding="utf-8"),
                "legacy note only\n"
                "\n"
                "**2026-04-05**\n"
                "- latest entry\n",
            )
            block = task_logs.read_latest_block_for_log(worklog, "WORKLOG")
            self.assertEqual(block.bullet_lines, ("- latest entry",))


class CheckCommandTests(unittest.TestCase):
    def test_check_accepts_valid_latest_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            decisions = task_dir / "logs" / "DECISIONS.md"
            decisions.write_text(
                "**2026-04-05**\n"
                "- 배경: sample\n"
                "- 선택지: sample\n"
                "- 결정: sample\n"
                "- 영향: sample\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = task_logs.main(
                    [
                        "decision",
                        "check",
                        "--task-root",
                        str(task_dir),
                    ]
                )

            self.assertEqual(exit_code, 0)
            self.assertIn(
                f"[OK] latest block valid: {rel_display('docs', 'tasks', '2026', '04-05', 'sample-task', 'logs', 'DECISIONS.md')}",
                stdout.getvalue(),
            )

    def test_check_rejects_invalid_worklog_latest_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            worklog = task_dir / "logs" / "WORKLOG.md"
            worklog.write_text(
                "**2026-04-05**\n"
                "freeform note\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = task_logs.main(
                    [
                        "worklog",
                        "check",
                        "--task-root",
                        str(task_dir),
                    ]
                )

            self.assertEqual(exit_code, 1)
            self.assertIn("latest date block must contain only bullet lines", stdout.getvalue())

    def test_check_rejects_short_decision_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            task_dir = make_task_dir(Path(tmp))
            decisions = task_dir / "logs" / "DECISIONS.md"
            decisions.write_text(
                "**2026-04-05**\n"
                "- 배경: only one line\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = task_logs.main(
                    [
                        "decision",
                        "check",
                        "--task-root",
                        str(task_dir),
                    ]
                )

            self.assertEqual(exit_code, 1)
            self.assertIn("latest decision block must contain exactly 4 bullet lines", stdout.getvalue())

    def test_display_path_falls_back_to_absolute_outside_canonical_task_tree(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            outside_task_root = root / "scratch" / "sample-task"
            outside_path = outside_task_root / "logs" / "WORKLOG.md"

            display = task_logs.display_path(outside_path, outside_task_root)

            self.assertEqual(display, str(outside_path.resolve()))


if __name__ == "__main__":
    unittest.main()
