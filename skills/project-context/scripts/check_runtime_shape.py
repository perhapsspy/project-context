#!/usr/bin/env python3
"""Thin checks for current runtime shape and latest log blocks."""

from __future__ import annotations

import argparse
from collections.abc import Iterator
from dataclasses import dataclass
import re
from datetime import datetime
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[1]
DEFAULT_CWD = Path.cwd().resolve()
DISPLAY_ROOT = DEFAULT_CWD

CORE_TASK_FILES = (
    "BRIEF.md",
    "STATUS.md",
    "logs/DECISIONS.md",
    "logs/WORKLOG.md",
)

KEBAB_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TASK_YEAR_RE = re.compile(r"^[0-9]{4}$")
TASK_DATE_RE = re.compile(r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$")
LOG_DATE_HEADING_RE = re.compile(r"^\*\*[0-9]{4}-[0-9]{2}-[0-9]{2}\*\*$")
MEMORY_CANDIDATE_ENTRY_RE = re.compile(
    r"^- "
    r"(?P<state>PENDING|APPLIED|REJECTED) "
    r"\| (?P<summary>[^|]+?) "
    r"\| (?P<evidence_pointer>logs/(?:DECISIONS|WORKLOG)\.md@L[1-9][0-9]*)"
    r"$"
)
SECRET_LIKE_MARKERS = (
    re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
    re.compile(r"(?i)(api[_-]?key|access[_-]?token|secret)\s*[:=]\s*[A-Za-z0-9_\-]{16,}"),
)
ENVIRONMENT_PATH_MARKERS = (
    re.compile(r"(?<![A-Za-z0-9])~/"),
    re.compile(r"\$HOME(?:/|\\)"),
    re.compile(r"\$\{HOME\}(?:/|\\)"),
    re.compile(r"%USERPROFILE%(?:\\|/)"),
    re.compile(r"file:///[^\s)]+"),
    re.compile(r"/Users/[^/\s`]+(?:/[^\s`)]+)+"),
    re.compile(r"/home/[^/\s`]+(?:/[^\s`)]+)+"),
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s`]+(?:\\[^\s`)]+)+"),
)
MEMORY_CANDIDATE_SUMMARY_HARD_CAP = 120
MEMORY_CANDIDATE_EVIDENCE_HARD_CAP = 32


@dataclass(frozen=True)
class RuntimePaths:
    repo_root: Path
    docs_root: Path
    memory_file: Path
    reference_root: Path
    task_root: Path


def detect_repo_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    git_root: Path | None = None

    for candidate in (current, *current.parents):
        docs_root = candidate / "docs"
        if (
            (docs_root / "memory.md").exists()
            or (docs_root / "reference").exists()
            or (docs_root / "tasks").exists()
        ):
            return candidate
        if git_root is None and (candidate / ".git").exists():
            git_root = candidate

    return git_root or current


def runtime_paths(repo_root: Path) -> RuntimePaths:
    repo_root = repo_root.resolve()
    docs_root = repo_root / "docs"
    return RuntimePaths(
        repo_root=repo_root,
        docs_root=docs_root,
        memory_file=docs_root / "memory.md",
        reference_root=docs_root / "reference",
        task_root=docs_root / "tasks",
    )


def main(
    argv: list[str] | None = None,
    runtime: RuntimePaths | None = None,
) -> int:
    args = parse_args(argv)
    if runtime is None:
        repo_root = (
            Path(args.repo_root).resolve()
            if args.repo_root is not None
            else detect_repo_root(Path.cwd())
        )
        runtime = runtime_paths(repo_root)
    set_display_root(runtime.repo_root)
    failures = run_runtime_shape_checks(runtime)
    return report_failures(failures)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Thin checks for current runtime shape and latest log blocks only. "
            "Does not validate semantic quality, full historical consistency, "
            "completeness, or migration correctness. "
            "Infers the target repo from the current working directory."
        )
    )
    parser.add_argument(
        "--repo-root",
        help=(
            "explicit repo root to validate when current-working-directory "
            "detection would be ambiguous"
        ),
    )
    return parser.parse_args(argv)


def run_runtime_shape_checks(runtime: RuntimePaths | None = None) -> list[str]:
    runtime = runtime or runtime_paths(detect_repo_root(Path.cwd()))
    set_display_root(runtime.repo_root)
    return [
        *check_memory_contract(runtime.memory_file),
        *check_reference_contract(runtime.reference_root),
        *check_task_contract(runtime.task_root),
        *check_portable_path_scan(runtime.docs_root, runtime.repo_root),
        *check_secret_marker_scan(runtime.docs_root),
    ]


def report_failures(failures: list[str]) -> int:
    if failures:
        print("[FAIL] project-context current runtime shape checks")
        for item in failures:
            print(f"- {item}")
        return 1

    print("[OK] project-context current runtime shape checks")
    return 0


def check_memory_contract(memory_file: Path | None = None) -> list[str]:
    memory_file = memory_file or runtime_paths(detect_repo_root(Path.cwd())).memory_file
    if not memory_file.exists():
        return [f"Missing required runtime file: {rel(memory_file)}"]
    if not memory_file.is_file():
        return [f"Required runtime file is not a file: {rel(memory_file)}"]

    line_count = count_lines(memory_file)
    if line_count <= 120:
        return []

    return [f"Memory too long: {rel(memory_file)} has {line_count} lines (target <= 120)"]


def check_reference_contract(reference_root: Path | None = None) -> list[str]:
    reference_root = reference_root or runtime_paths(detect_repo_root(Path.cwd())).reference_root
    if not reference_root.exists():
        return [f"Missing required runtime directory: {rel(reference_root)}"]
    if not reference_root.is_dir():
        return [f"Required runtime directory is not a directory: {rel(reference_root)}"]

    failures: list[str] = []
    for path in sorted(reference_root.rglob("*.md")):
        failures.extend(reference_path_failures(path, reference_root))

    return failures


def reference_path_failures(
    path: Path,
    reference_root: Path | None = None,
) -> list[str]:
    reference_root = reference_root or runtime_paths(detect_repo_root(Path.cwd())).reference_root
    parts = path.relative_to(reference_root).parts
    return reference_parts_failures(parts, rel(path))


def reference_parts_failures(parts: tuple[str, ...], display: str) -> list[str]:
    if not parts:
        return [f"Invalid reference path: {display}"]

    *directories, filename = parts
    failures: list[str] = []

    for directory in directories:
        failures.extend(kebab_name_failures(directory, "reference directory", display))

    failures.extend(kebab_name_failures(Path(filename).stem, "reference topic", display))
    return failures


def kebab_name_failures(name: str, label: str, display: str) -> list[str]:
    if KEBAB_NAME_RE.match(name):
        return []
    return [f"Invalid {label} (kebab-case required): {display}"]


def check_task_contract(task_root: Path | None = None) -> list[str]:
    task_root = task_root or runtime_paths(detect_repo_root(Path.cwd())).task_root
    if not task_root.exists():
        return [f"Missing required runtime directory: {rel(task_root)}"]
    if not task_root.is_dir():
        return [f"Required runtime directory is not a directory: {rel(task_root)}"]

    tasks, layout_failures = collect_tasks(task_root)
    failures = list(layout_failures)

    for task_dir in tasks:
        failures.extend(task_failures(task_dir))

    return failures


def collect_tasks(task_root: Path) -> tuple[list[Path], list[str]]:
    tasks: list[Path] = []
    failures: list[str] = []

    for year_dir in visible_children(task_root):
        if not year_dir.is_dir():
            failures.append(f"Unexpected file in tasks root: {rel(year_dir)}")
            continue
        if not TASK_YEAR_RE.match(year_dir.name):
            failures.append(f"Invalid task year directory (expected yyyy): {rel(year_dir)}")
            continue

        for date_dir in visible_children(year_dir):
            if not date_dir.is_dir():
                failures.append(f"Unexpected file in task year directory: {rel(date_dir)}")
                continue
            if not TASK_DATE_RE.match(date_dir.name):
                failures.append(f"Invalid task date directory (expected mm-dd): {rel(date_dir)}")
                continue
            if not is_valid_task_date(year_dir.name, date_dir.name):
                failures.append(f"Invalid task date directory (not a real date): {rel(date_dir)}")
                continue

            for task_dir in visible_children(date_dir):
                if not task_dir.is_dir():
                    failures.append(f"Unexpected file in task date directory: {rel(task_dir)}")
                    continue
                if not KEBAB_NAME_RE.match(task_dir.name):
                    failures.append(f"Invalid task slug (kebab-case required): {rel(task_dir)}")
                    continue
                tasks.append(task_dir)

    return tasks, failures


def task_failures(task_dir: Path) -> list[str]:
    failures: list[str] = []

    for rel_name in CORE_TASK_FILES:
        candidate = task_dir / rel_name
        if not candidate.exists():
            failures.append(f"Missing task core file: {rel(candidate)}")
            continue
        if not candidate.is_file():
            failures.append(f"Task core file is not a file: {rel(candidate)}")

    memory_candidates_path = task_dir / "MEMORY-CANDIDATES.md"
    if memory_candidates_path.exists():
        if not memory_candidates_path.is_file():
            failures.append(
                "Optional MEMORY-CANDIDATES.md is not a file: "
                f"{rel(memory_candidates_path)}"
            )
        else:
            failures.extend(
                memory_candidate_file_failures(task_dir, memory_candidates_path)
            )

    decisions_path = task_dir / "logs" / "DECISIONS.md"
    if decisions_path.is_file():
        failures.extend(decisions_log_failures(decisions_path))

    worklog_path = task_dir / "logs" / "WORKLOG.md"
    if worklog_path.is_file():
        failures.extend(worklog_file_failures(worklog_path))

    return failures


def decisions_log_failures(path: Path) -> list[str]:
    block = latest_log_block(path)
    if isinstance(block, str):
        return [block]
    return []


def worklog_file_failures(path: Path) -> list[str]:
    block = latest_log_block(path)
    if isinstance(block, str):
        return [block]
    return []


def latest_log_block(path: Path) -> list[str] | str:
    lines = read_text(path).splitlines()
    heading_indexes = [
        index for index, raw in enumerate(lines) if LOG_DATE_HEADING_RE.match(raw.strip())
    ]
    if not heading_indexes:
        return f"{rel(path)}: missing `**YYYY-MM-DD**` heading"

    start = heading_indexes[-1] + 1
    block_lines = [raw.strip() for raw in lines[start:] if raw.strip()]
    if not block_lines:
        return f"{rel(path)}: latest date block is empty"

    if any(not raw.startswith("- ") for raw in block_lines):
        return f"{rel(path)}: latest date block must contain only bullet lines"

    return block_lines


def memory_candidate_file_failures(pack: Path, memory_candidates_path: Path) -> list[str]:
    failures: list[str] = []

    for lineno, line in iter_memory_candidate_lines(memory_candidates_path):
        failures.extend(
            memory_candidate_line_failures(pack, memory_candidates_path, lineno, line)
        )

    return failures


def iter_memory_candidate_lines(memory_candidates_path: Path) -> Iterator[tuple[int, str]]:
    for lineno, raw in enumerate(read_text(memory_candidates_path).splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        yield lineno, line


def parse_memory_candidate_entry(line: str) -> re.Match[str] | None:
    return MEMORY_CANDIDATE_ENTRY_RE.match(line)


def memory_candidate_line_failures(
    pack: Path,
    memory_candidates_path: Path,
    lineno: int,
    line: str,
) -> list[str]:
    if not line.startswith("- "):
        return [
            f"{rel(memory_candidates_path)}: line {lineno}: non-empty lines must start with '- '"
        ]

    match = parse_memory_candidate_entry(line)
    if not match:
        return [f"{rel(memory_candidates_path)}: line {lineno}: invalid entry format"]

    summary = match.group("summary").strip()
    evidence_pointer = match.group("evidence_pointer")
    failures: list[str] = []

    if not summary:
        failures.append(f"{rel(memory_candidates_path)}: line {lineno}: summary is required")
    if len(summary) > MEMORY_CANDIDATE_SUMMARY_HARD_CAP:
        failures.append(
            f"{rel(memory_candidates_path)}: line {lineno}: summary too long "
            f"({len(summary)} > {MEMORY_CANDIDATE_SUMMARY_HARD_CAP})"
        )
    if len(evidence_pointer) > MEMORY_CANDIDATE_EVIDENCE_HARD_CAP:
        failures.append(
            f"{rel(memory_candidates_path)}: line {lineno}: evidence-pointer too long "
            f"({len(evidence_pointer)} > {MEMORY_CANDIDATE_EVIDENCE_HARD_CAP})"
        )

    failures.extend(
        evidence_pointer_failures(pack, memory_candidates_path, lineno, evidence_pointer)
    )
    return failures


def evidence_pointer_failures(
    pack: Path,
    memory_candidates_path: Path,
    lineno: int,
    evidence: str,
) -> list[str]:
    rel_file, line_token = evidence.rsplit("@L", 1)
    evidence_file = pack / rel_file

    if not evidence_file.exists():
        return [
            f"{rel(memory_candidates_path)}: line {lineno}: evidence file not found: {rel(evidence_file)}"
        ]
    if not evidence_file.is_file():
        return [
            f"{rel(memory_candidates_path)}: line {lineno}: evidence path is not a file: {rel(evidence_file)}"
        ]

    evidence_line = int(line_token)
    max_lines = count_lines(evidence_file)
    if evidence_line > max_lines:
        return [
            f"{rel(memory_candidates_path)}: line {lineno}: evidence line out of range ({evidence_line} > {max_lines})"
        ]

    return []


def check_secret_marker_scan(docs_root: Path | None = None) -> list[str]:
    docs_root = docs_root or runtime_paths(detect_repo_root(Path.cwd())).docs_root
    if not docs_root.exists():
        return []

    failures: list[str] = []
    for path in iter_memory_files(docs_root):
        text = read_text_if_scannable(path)
        if text is None:
            continue

        for pattern in SECRET_LIKE_MARKERS:
            if pattern.search(text):
                failures.append(f"Possible secret-like marker found in {rel(path)}")
                break

    return failures


def check_portable_path_scan(
    docs_root: Path | None = None,
    repo_root: Path | None = None,
) -> list[str]:
    runtime = runtime_paths((repo_root or detect_repo_root(Path.cwd())).resolve())
    docs_root = docs_root or runtime.docs_root
    if not docs_root.exists():
        return []

    repo_markers = tuple(repo_root_markers(runtime.repo_root))
    failures: list[str] = []
    for path in iter_portable_path_files(runtime):
        text = read_text_if_scannable(path)
        if text is None:
            continue
        if contains_portable_path_marker(text, repo_markers):
            failures.append(
                f"Possible absolute or environment-specific path marker found in {rel(path)}"
            )

    return failures


def repo_root_markers(repo_root: Path) -> Iterator[re.Pattern[str]]:
    markers = {str(repo_root.resolve()), repo_root.resolve().as_posix()}
    for marker in sorted(markers):
        if marker and marker not in {".", "/"}:
            yield re.compile(re.escape(marker))


def contains_portable_path_marker(
    text: str,
    repo_markers: tuple[re.Pattern[str], ...],
) -> bool:
    for pattern in repo_markers:
        if pattern.search(text):
            return True

    return any(pattern.search(text) for pattern in ENVIRONMENT_PATH_MARKERS)


def iter_portable_path_files(runtime: RuntimePaths) -> Iterator[Path]:
    if runtime.memory_file.is_file():
        yield runtime.memory_file

    if runtime.reference_root.exists():
        yield from sorted(runtime.reference_root.rglob("*.md"))

    if not runtime.task_root.exists():
        return

    tasks, _ = collect_tasks(runtime.task_root)
    for task_dir in tasks:
        for name in ("BRIEF.md", "STATUS.md", "MEMORY-CANDIDATES.md"):
            path = task_dir / name
            if path.is_file():
                yield path


def iter_memory_files(docs_root: Path) -> Iterator[Path]:
    for path in sorted(docs_root.rglob("*")):
        if path.is_file():
            yield path


def read_text_if_scannable(path: Path) -> str | None:
    sample = path.read_bytes()[:4096]
    if b"\x00" in sample:
        return None
    return path.read_text(encoding="utf-8", errors="ignore")


def visible_children(path: Path) -> list[Path]:
    return [child for child in sorted(path.iterdir()) if not child.name.startswith(".")]


def is_valid_task_date(year: str, month_day: str) -> bool:
    try:
        datetime.strptime(f"{year}-{month_day}", "%Y-%m-%d")
    except ValueError:
        return False
    return True


def count_lines(path: Path) -> int:
    return len(read_text(path).splitlines())


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(DISPLAY_ROOT))
    except ValueError:
        return str(path)


def set_display_root(repo_root: Path) -> None:
    global DISPLAY_ROOT
    DISPLAY_ROOT = repo_root.resolve()


if __name__ == "__main__":
    raise SystemExit(main())
