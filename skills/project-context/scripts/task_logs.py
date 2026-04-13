#!/usr/bin/env python3
"""Append, tail, and validate project-context task logs."""

from __future__ import annotations

import argparse
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime
import os
from pathlib import Path
import re

LOG_DATE_HEADING_RE = re.compile(r"^\*\*[0-9]{4}-[0-9]{2}-[0-9]{2}\*\*$")
DECISIONS_LOG_NAME = "DECISIONS.md"
WORKLOG_LOG_NAME = "WORKLOG.md"
DECISION_LINE_COUNT = 4


class LogToolError(ValueError):
    """Raised when a log path or its latest block is invalid."""


@dataclass(frozen=True)
class LatestLogBlock:
    path: Path
    heading: str
    bullet_lines: tuple[str, ...]

    @property
    def date(self) -> str:
        return self.heading.strip("*")


@dataclass(frozen=True)
class RawLatestLogBlock:
    path: Path
    heading: str
    block_lines: tuple[str, ...]

    @property
    def date(self) -> str:
        return self.heading.strip("*")


@dataclass(frozen=True)
class CommandTarget:
    task_root: Path
    log_name: str


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        return run_command(args)
    except LogToolError as exc:
        print(f"[FAIL] {exc}")
        return 1


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Append, tail, or validate project-context task logs without "
            "rewriting existing log history."
        ),
        epilog=(
            "append expects an existing task root with BRIEF.md. "
            "In PowerShell, use --bullet= when you need to pass an empty string deliberately."
        ),
    )
    surfaces = parser.add_subparsers(dest="surface", required=True)

    add_worklog_surface(surfaces)
    add_decision_surface(surfaces)

    return parser.parse_args(argv)


def add_worklog_surface(
    surfaces: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    parser = surfaces.add_parser("worklog", help="operate on WORKLOG.md")
    commands = parser.add_subparsers(dest="command", required=True)

    append_parser = commands.add_parser("append", help="append one bullet to WORKLOG.md")
    add_task_root_arg(append_parser)
    append_parser.add_argument("--date", required=True, help="target log date in YYYY-MM-DD")
    append_parser.add_argument("--bullet", required=True, help="bullet text to append")

    tail_parser = commands.add_parser("tail", help="print the latest WORKLOG block only")
    add_task_root_arg(tail_parser)

    check_parser = commands.add_parser("check", help="validate the latest WORKLOG block only")
    add_task_root_arg(check_parser)


def add_decision_surface(
    surfaces: argparse._SubParsersAction[argparse.ArgumentParser],
) -> None:
    parser = surfaces.add_parser("decision", help="operate on DECISIONS.md")
    commands = parser.add_subparsers(dest="command", required=True)

    append_parser = commands.add_parser(
        "append",
        help="append one 4-bullet decision block to DECISIONS.md",
    )
    add_task_root_arg(append_parser)
    append_parser.add_argument("--date", required=True, help="target log date in YYYY-MM-DD")
    append_parser.add_argument("--background", required=True, help="background bullet text")
    append_parser.add_argument("--options", required=True, help="options bullet text")
    append_parser.add_argument("--decision", required=True, help="decision bullet text")
    append_parser.add_argument("--impact", required=True, help="impact bullet text")

    tail_parser = commands.add_parser("tail", help="print the latest DECISIONS block only")
    add_task_root_arg(tail_parser)

    check_parser = commands.add_parser("check", help="validate the latest DECISIONS block only")
    add_task_root_arg(check_parser)


def add_task_root_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--task-root",
        type=Path,
        required=True,
        help="existing task directory that owns the logs folder",
    )


def run_command(args: argparse.Namespace) -> int:
    target = command_target(args)
    log_path = resolve_log_path(target)
    display_log_path = display_path(log_path, target.task_root)

    if args.surface == "worklog" and args.command == "append":
        ensure_append_target(target.task_root)
        append_log_bullet(log_path, args.date, args.bullet)
        print(f"[OK] appended {display_log_path}")
        return 0

    if args.surface == "decision" and args.command == "append":
        ensure_append_target(target.task_root)
        append_decision_block(
            log_path,
            args.date,
            (args.background, args.options, args.decision, args.impact),
        )
        print(f"[OK] appended {display_log_path}")
        return 0

    if args.command == "tail":
        block = read_latest_block_for_log(log_path, target.log_name)
        print(render_latest_block(block))
        return 0

    if args.command == "check":
        read_latest_block_for_log(log_path, target.log_name)
        print(f"[OK] latest block valid: {display_log_path}")
        return 0

    raise LogToolError(f"unsupported command: {args.surface} {args.command}")


def command_target(args: argparse.Namespace) -> CommandTarget:
    if args.surface == "worklog":
        return CommandTarget(task_root=args.task_root, log_name=WORKLOG_LOG_NAME)
    if args.surface == "decision":
        return CommandTarget(task_root=args.task_root, log_name=DECISIONS_LOG_NAME)
    raise LogToolError(f"unsupported surface: {args.surface}")


def resolve_log_path(target: CommandTarget) -> Path:
    return target.task_root / "logs" / target.log_name


def canonical_log_name(log_name: str) -> str:
    normalized = log_name.strip().upper()
    if normalized in {"DECISIONS", "DECISIONS.MD"}:
        return DECISIONS_LOG_NAME
    if normalized in {"WORKLOG", "WORKLOG.MD"}:
        return WORKLOG_LOG_NAME
    raise LogToolError(f"unsupported log name: {log_name}")


def ensure_append_target(task_root: Path) -> None:
    if not task_root.exists():
        raise LogToolError(f"missing task root: {display_path(task_root, task_root)}")
    if not task_root.is_dir():
        raise LogToolError(f"task root is not a directory: {display_path(task_root, task_root)}")

    brief_path = task_root / "BRIEF.md"
    if not brief_path.exists():
        raise LogToolError(f"missing task brief: {display_path(brief_path, task_root)}")
    if not brief_path.is_file():
        raise LogToolError(f"task brief is not a file: {display_path(brief_path, task_root)}")


def display_path(path: Path, task_root: Path) -> str:
    repo_root = infer_repo_root(task_root)
    resolved_path = path.resolve()
    if repo_root is None:
        return str(resolved_path)

    try:
        return str(resolved_path.relative_to(repo_root))
    except ValueError:
        return str(resolved_path)


def infer_repo_root(task_root: Path) -> Path | None:
    resolved = task_root.resolve()
    for candidate in (resolved, *resolved.parents):
        if candidate.name != "tasks":
            continue
        docs_dir = candidate.parent
        if docs_dir.name != "docs":
            continue
        return docs_dir.parent.resolve()
    return None


def append_log_bullet(path: Path, date_text: str, bullet: str) -> None:
    normalized_date = normalize_date(date_text)
    bullet_line = normalize_bullet(bullet)
    ensure_log_path_writable(path)

    if not path.exists() or path.stat().st_size == 0:
        path.write_text(f"**{normalized_date}**\n{bullet_line}\n", encoding="utf-8")
        return

    latest_block = latest_raw_block_or_none(path)
    if latest_block is not None and normalized_date < latest_block.date:
        raise LogToolError(
            f"cannot append older date {normalized_date} before latest block {latest_block.date}"
        )

    with path.open("a", encoding="utf-8", newline="") as handle:
        if (
            latest_block is not None
            and normalized_date == latest_block.date
            and raw_block_has_only_bullets(latest_block)
        ):
            if not ends_with_newline(path):
                handle.write("\n")
            handle.write(f"{bullet_line}\n")
            return

        if not ends_with_newline(path):
            handle.write("\n")
        handle.write(f"\n**{normalized_date}**\n{bullet_line}\n")


def append_decision_block(
    path: Path,
    date_text: str,
    decision_lines: tuple[str, str, str, str],
) -> None:
    normalized_date = normalize_date(date_text)
    normalized_lines = [normalize_bullet(line) for line in decision_lines]
    ensure_log_path_writable(path)

    latest_block = latest_raw_block_or_none(path)
    if latest_block is not None and normalized_date < latest_block.date:
            raise LogToolError(
                f"cannot append older date {normalized_date} before latest block {latest_block.date}"
            )

    with path.open("a", encoding="utf-8", newline="") as handle:
        handle.write(block_prefix(path, normalized_date))
        handle.write("\n".join(normalized_lines))
        handle.write("\n")


def render_latest_block(block: LatestLogBlock) -> str:
    return "\n".join((block.heading, *block.bullet_lines))


def read_latest_block(path: Path) -> LatestLogBlock:
    raw_block = read_latest_raw_block(path)
    bullet_lines = validate_raw_block_bullets(raw_block.block_lines)
    return LatestLogBlock(path=path, heading=raw_block.heading, bullet_lines=bullet_lines)


def read_latest_raw_block(path: Path) -> RawLatestLogBlock:
    if not path.exists():
        raise LogToolError(f"missing log file: {path}")
    if not path.is_file():
        raise LogToolError(f"log path is not a file: {path}")

    block_lines_reversed: list[str] = []
    for raw_line in iter_lines_reversed(path):
        stripped = raw_line.strip().lstrip("\ufeff")
        if not stripped:
            continue
        if LOG_DATE_HEADING_RE.match(stripped):
            return RawLatestLogBlock(
                path=path,
                heading=stripped,
                block_lines=tuple(reversed(block_lines_reversed)),
            )
        block_lines_reversed.append(stripped)

    raise LogToolError("missing `**YYYY-MM-DD**` heading")


def read_latest_block_for_log(path: Path, log_name: str) -> LatestLogBlock:
    block = read_latest_block(path)
    if canonical_log_name(log_name) == DECISIONS_LOG_NAME:
        validate_decisions_block(block)
    return block


def validate_decisions_block(block: LatestLogBlock) -> None:
    if len(block.bullet_lines) != DECISION_LINE_COUNT:
        raise LogToolError("latest decision block must contain exactly 4 bullet lines")


def latest_raw_block_or_none(path: Path) -> RawLatestLogBlock | None:
    if not path.exists() or path.stat().st_size == 0:
        return None

    try:
        return read_latest_raw_block(path)
    except LogToolError as exc:
        if str(exc) == "missing `**YYYY-MM-DD**` heading":
            return None
        raise


def validate_raw_block_bullets(block_lines: tuple[str, ...]) -> tuple[str, ...]:
    if not block_lines:
        raise LogToolError("latest date block is empty")
    if any(not line.startswith("- ") for line in block_lines):
        raise LogToolError("latest date block must contain only bullet lines")
    return block_lines


def raw_block_has_only_bullets(block: RawLatestLogBlock) -> bool:
    try:
        validate_raw_block_bullets(block.block_lines)
    except LogToolError:
        return False
    return True


def ensure_log_path_writable(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not path.is_file():
        raise LogToolError(f"log path is not a file: {path}")


def block_prefix(path: Path, normalized_date: str) -> str:
    if not path.exists() or path.stat().st_size == 0:
        return f"**{normalized_date}**\n"
    if ends_with_newline(path):
        return f"\n**{normalized_date}**\n"
    return f"\n\n**{normalized_date}**\n"


def iter_lines_reversed(path: Path, chunk_size: int = 4096) -> Iterator[str]:
    with path.open("rb") as handle:
        handle.seek(0, os.SEEK_END)
        position = handle.tell()
        remainder = b""

        while position > 0:
            read_size = min(chunk_size, position)
            position -= read_size
            handle.seek(position)
            remainder = handle.read(read_size) + remainder
            parts = remainder.split(b"\n")
            remainder = parts[0]
            for raw_line in reversed(parts[1:]):
                yield raw_line.decode("utf-8", errors="ignore")

        if remainder:
            yield remainder.decode("utf-8", errors="ignore")


def normalize_date(date_text: str) -> str:
    try:
        return datetime.strptime(date_text, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError as exc:
        raise LogToolError(f"invalid date: {date_text}") from exc


def normalize_bullet(bullet: str) -> str:
    stripped = bullet.strip()
    if not stripped:
        raise LogToolError("bullet must not be empty")
    if "\n" in stripped or "\r" in stripped:
        raise LogToolError("bullet must be one line")
    if stripped.startswith("- "):
        return stripped
    if stripped.startswith("-"):
        return f"- {stripped[1:].lstrip()}"
    return f"- {stripped}"


def ends_with_newline(path: Path) -> bool:
    with path.open("rb") as handle:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            return True
        handle.seek(-1, os.SEEK_END)
        return handle.read(1) == b"\n"


if __name__ == "__main__":
    raise SystemExit(main())
