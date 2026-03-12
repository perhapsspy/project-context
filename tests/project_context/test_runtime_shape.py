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
    memory_file = docs_root / "memory.md"
    reference_root = docs_root / "reference"
    task_root = docs_root / "tasks"
    task_dir = task_root / "2026" / "03-09" / "sample-task"
    logs = task_dir / "logs"

    memory_file.parent.mkdir(parents=True)
    memory_file.write_text("line\n", encoding="utf-8")
    reference_root.mkdir(parents=True)
    logs.mkdir(parents=True)
    (task_dir / "BRIEF.md").write_text("# sample\n", encoding="utf-8")
    (task_dir / "STATUS.md").write_text("- state: sample\n", encoding="utf-8")
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
        memory_file=memory_file,
        reference_root=reference_root,
        task_root=task_root,
    )
    return runtime, task_dir


def make_memory_candidate_pack(
    root: Path,
    *,
    log_name: str = "DECISIONS.md",
    log_text: str = "- decision\n",
) -> tuple[Path, Path, Path]:
    pack = root / "pack"
    logs = pack / "logs"
    logs.mkdir(parents=True)
    (logs / log_name).write_text(log_text, encoding="utf-8")
    memory_candidates = pack / "MEMORY-CANDIDATES.md"
    memory_candidates.write_text("", encoding="utf-8")
    return pack, logs, memory_candidates


def write_reference_file(root: Path, relative_path: str) -> Path:
    path = root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# sample\n", encoding="utf-8")
    return path


class MemoryShapeTests(unittest.TestCase):
    def test_missing_memory_file_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            memory_file = Path(tmp) / "memory.md"

            failures = runtime_shape_check.check_memory_contract(memory_file)

            self.assertEqual(
                failures,
                [f"Missing required runtime file: {runtime_shape_check.rel(memory_file)}"],
            )

    def test_memory_over_budget_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            memory_file = Path(tmp) / "memory.md"
            memory_file.write_text("\n".join(["line"] * 121), encoding="utf-8")

            failures = runtime_shape_check.check_memory_contract(memory_file)

            self.assertEqual(
                failures,
                [f"Memory too long: {runtime_shape_check.rel(memory_file)} has 121 lines (target <= 120)"],
            )

    def test_memory_directory_fails_without_exception(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            memory_file = Path(tmp) / "memory.md"
            memory_file.mkdir()

            failures = runtime_shape_check.check_memory_contract(memory_file)

            self.assertEqual(
                failures,
                [f"Required runtime file is not a file: {runtime_shape_check.rel(memory_file)}"],
            )


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
            self.assertEqual(runtime_shape_check.check_reference_contract(Path(tmp)), [])

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


class MemoryCandidateShapeTests(unittest.TestCase):
    def test_collect_memory_candidate_stats_ignores_blank_lines(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, pack = make_valid_runtime_tree(root)
            memory_candidates = pack / "MEMORY-CANDIDATES.md"
            memory_candidates.write_text(
                "\n"
                "- APPLIED | "
                + ("x" * 85)
                + " | logs/DECISIONS.md@L1\n",
                encoding="utf-8",
            )

            stats = runtime_shape_check.collect_memory_candidate_stats(runtime.task_root)

            self.assertEqual(stats["candidate_files"], 1)
            self.assertEqual(stats["entries"], 1)
            self.assertEqual(stats["invalid_lines"], 0)
            self.assertEqual(stats["summary_80_100"], 1)
            self.assertEqual(stats["evidence_pointer_le_32"], 1)

    def test_memory_candidate_title_line_is_invalid(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            pack, _, memory_candidates = make_memory_candidate_pack(Path(tmp))
            memory_candidates.write_text("# Memory Candidates\n", encoding="utf-8")

            failures = runtime_shape_check.memory_candidate_file_failures(
                pack,
                memory_candidates,
            )

            self.assertEqual(
                failures,
                [
                    f"{runtime_shape_check.rel(memory_candidates)}: line 1: non-empty lines must start with '- '"
                ],
            )

    def test_old_targeted_format_is_invalid(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            pack, _, memory_candidates = make_memory_candidate_pack(Path(tmp))

            failures = runtime_shape_check.memory_candidate_line_failures(
                pack,
                memory_candidates,
                1,
                "- APPLIED MEMORY | sample summary | logs/DECISIONS.md@L1",
            )

            self.assertTrue(any("invalid entry format" in item for item in failures))

    def test_evidence_line_out_of_range_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            pack, _, memory_candidates = make_memory_candidate_pack(
                Path(tmp),
                log_name="WORKLOG.md",
                log_text="- entry\n",
            )

            failures = runtime_shape_check.memory_candidate_line_failures(
                pack,
                memory_candidates,
                1,
                "- APPLIED | sample summary | logs/WORKLOG.md@L9",
            )

            self.assertTrue(any("evidence line out of range" in item for item in failures))

    def test_summary_over_hard_cap_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            pack, _, memory_candidates = make_memory_candidate_pack(Path(tmp))
            summary = "x" * 121

            failures = runtime_shape_check.memory_candidate_line_failures(
                pack,
                memory_candidates,
                1,
                f"- APPLIED | {summary} | logs/DECISIONS.md@L1",
            )

            self.assertTrue(any("summary too long" in item for item in failures))

    def test_evidence_over_hard_cap_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            pack, _, memory_candidates = make_memory_candidate_pack(Path(tmp))
            evidence = "logs/DECISIONS.md@L123456789012345"

            failures = runtime_shape_check.memory_candidate_line_failures(
                pack,
                memory_candidates,
                1,
                f"- APPLIED | sample summary | {evidence}",
            )

            self.assertTrue(any("evidence-pointer too long" in item for item in failures))

    def test_valid_memory_candidate_entry_passes(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            pack, _, memory_candidates = make_memory_candidate_pack(Path(tmp))

            failures = runtime_shape_check.memory_candidate_line_failures(
                pack,
                memory_candidates,
                1,
                "- APPLIED | sample summary | logs/DECISIONS.md@L1",
            )

            self.assertEqual(failures, [])


class TaskShapeTests(unittest.TestCase):
    def test_missing_task_directory_fails(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            task_root = Path(tmp) / "tasks"

            failures = runtime_shape_check.check_task_contract(task_root)

            self.assertEqual(
                failures,
                [f"Missing required runtime directory: {runtime_shape_check.rel(task_root)}"],
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

    def test_main_without_memory_candidate_stats_keeps_default_output(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, _ = make_valid_runtime_tree(root)
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = runtime_shape_check.main([], runtime=runtime)

            self.assertEqual(exit_code, 0)
            self.assertEqual(
                stdout.getvalue().strip(),
                "[OK] project-context current runtime shape checks",
            )

    def test_main_failure_output_includes_runtime_shape_failures(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, _ = make_valid_runtime_tree(root)
            runtime = runtime_shape_check.RuntimePaths(
                repo_root=runtime.repo_root,
                docs_root=runtime.docs_root,
                memory_file=root / "missing-memory.md",
                reference_root=runtime.reference_root,
                task_root=runtime.task_root,
            )
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = runtime_shape_check.main([], runtime=runtime)

            self.assertEqual(exit_code, 1)
            self.assertEqual(
                stdout.getvalue().strip().splitlines(),
                [
                    "[FAIL] project-context current runtime shape checks",
                    f"- Missing required runtime file: {runtime_shape_check.rel(runtime.memory_file)}",
                ],
            )

    def test_main_detects_repo_root_from_cwd_when_runtime_is_not_passed(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            make_valid_runtime_tree(root)
            stdout = io.StringIO()

            with pushd(root / "docs"), contextlib.redirect_stdout(stdout):
                exit_code = runtime_shape_check.main([])

            self.assertEqual(exit_code, 0)
            self.assertEqual(
                stdout.getvalue().strip(),
                "[OK] project-context current runtime shape checks",
            )

    def test_main_with_memory_candidate_stats_prints_summary_and_evidence_distribution(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            root = Path(tmp)
            runtime, pack = make_valid_runtime_tree(root)
            memory_candidates = pack / "MEMORY-CANDIDATES.md"
            memory_candidates.write_text(
                "- APPLIED | "
                + ("x" * 75)
                + " | logs/DECISIONS.md@L1\n"
                + "- APPLIED | "
                + ("x" * 90)
                + " | logs/WORKLOG.md@L1\n"
                + "- APPLIED | "
                + ("x" * 110)
                + " | logs/DECISIONS.md@L1\n",
                encoding="utf-8",
            )
            stdout = io.StringIO()

            with contextlib.redirect_stdout(stdout):
                exit_code = runtime_shape_check.main(
                    ["--memory-candidate-stats"],
                    runtime=runtime,
                )

            self.assertEqual(exit_code, 0)
            self.assertEqual(
                stdout.getvalue().strip().splitlines(),
                [
                    "[OK] project-context current runtime shape checks",
                    "[MEMORY CANDIDATE STATS]",
                    "- scope: candidate_files=1 entries=3 invalid_lines=0",
                    "- summary chars: <80=1 80-100=1 101-120=1 >120=0",
                    "- evidence-pointer chars: <=32=3 >32=0",
                ],
            )

    def test_memory_candidates_directory_fails_without_exception(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            pack = Path(tmp) / "pack"
            logs = pack / "logs"
            logs.mkdir(parents=True)
            (pack / "BRIEF.md").write_text("", encoding="utf-8")
            (pack / "STATUS.md").write_text("", encoding="utf-8")
            (pack / "MEMORY-CANDIDATES.md").mkdir()
            (logs / "DECISIONS.md").write_text(
                "**2026-03-09**\n- 배경: sample\n- 선택지: sample\n- 결정: sample\n- 영향: sample\n",
                encoding="utf-8",
            )
            (logs / "WORKLOG.md").write_text(
                "**2026-03-09**\n- sample\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.task_failures(pack)

            self.assertEqual(
                failures,
                [
                    "Optional MEMORY-CANDIDATES.md is not a file: "
                    f"{runtime_shape_check.rel(pack / 'MEMORY-CANDIDATES.md')}"
                ],
            )

    def test_evidence_directory_fails_without_exception(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            pack = Path(tmp) / "pack"
            logs = pack / "logs"
            logs.mkdir(parents=True)
            (logs / "DECISIONS.md").mkdir()
            memory_candidates = pack / "MEMORY-CANDIDATES.md"
            memory_candidates.write_text("", encoding="utf-8")

            failures = runtime_shape_check.memory_candidate_line_failures(
                pack,
                memory_candidates,
                1,
                "- APPLIED | sample summary | logs/DECISIONS.md@L1",
            )

            self.assertEqual(
                failures,
                [
                    f"{runtime_shape_check.rel(memory_candidates)}: line 1: evidence path is not a file: "
                    f"{runtime_shape_check.rel(logs / 'DECISIONS.md')}"
                ],
            )

    def test_worklog_requires_latest_date_block(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            worklog = Path(tmp) / "WORKLOG.md"
            worklog.write_text("# WORKLOG\n- legacy\n", encoding="utf-8")

            failures = runtime_shape_check.worklog_file_failures(worklog)

            self.assertEqual(
                failures,
                [f"{runtime_shape_check.rel(worklog)}: missing `**YYYY-MM-DD**` heading"],
            )

    def test_decisions_latest_block_requires_four_bullet_lines(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            decisions = Path(tmp) / "DECISIONS.md"
            decisions.write_text(
                "# DECISIONS\n\n**2026-03-09**\n- 결정: sample\n- 이유: sample\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.decisions_log_failures(decisions)

            self.assertEqual(
                failures,
                [f"{runtime_shape_check.rel(decisions)}: latest date block must contain at least 4 bullet lines"],
            )

    def test_decisions_latest_block_accepts_non_korean_adr_lite_block(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            decisions = Path(tmp) / "DECISIONS.md"
            decisions.write_text(
                "**2026-03-09**\n"
                "- background: sample\n"
                "- options: sample\n"
                "- decision: sample\n"
                "- impact: sample\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.decisions_log_failures(decisions)

            self.assertEqual(failures, [])

    def test_legacy_preamble_is_allowed_when_latest_block_is_valid(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            decisions = Path(tmp) / "DECISIONS.md"
            decisions.write_text(
                "- 결정: legacy\n"
                "- 이유: legacy\n\n"
                "**2026-03-09**\n"
                "- 배경: sample\n"
                "- 선택지: sample\n"
                "- 결정: sample\n"
                "- 영향: sample\n",
                encoding="utf-8",
            )

            failures = runtime_shape_check.decisions_log_failures(decisions)

            self.assertEqual(failures, [])


class SecretShapeTests(unittest.TestCase):
    def test_non_markdown_text_file_is_scanned(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            memory_root = Path(tmp)
            artifact = memory_root / "artifact.txt"
            artifact.write_text("api_key = SECRETSECRET123456", encoding="utf-8")

            failures = runtime_shape_check.check_secret_marker_scan(memory_root)

            self.assertEqual(
                failures,
                [f"Possible secret-like marker found in {runtime_shape_check.rel(artifact)}"],
            )

    def test_binary_file_is_skipped(self):
        with tempfile.TemporaryDirectory(dir=runtime_shape_check.REPO_ROOT) as tmp:
            memory_root = Path(tmp)
            artifact = memory_root / "artifact.bin"
            artifact.write_bytes(b"\x00\x01api_key = SECRETSECRET123456")

            failures = runtime_shape_check.check_secret_marker_scan(memory_root)

            self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
