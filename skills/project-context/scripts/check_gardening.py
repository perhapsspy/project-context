#!/usr/bin/env python3
"""Warning-grade gardening checks for project-context drift."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta
from pathlib import Path


def load_runtime_shape_module():
    module_path = Path(__file__).with_name("check_runtime_shape.py")
    spec = importlib.util.spec_from_file_location("check_runtime_shape_gardening", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


runtime_shape = load_runtime_shape_module()

CANONICAL_ROOT_STEMS = {
    "MODEL",
    "CONTRACTS",
    "SYSTEM_BOUNDARIES",
    "EXECUTION",
    "ACTIONS",
}
OVERLAY_KEYWORDS = (
    "PLAN",
    "REWORK",
    "BACKLOG",
    "MIGRATION",
    "POLICY",
    "FLOW",
)
LEGACY_SURFACES = ("STATUS.md", "MEMORY-CANDIDATES.md")


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    detail: str | None = None
    suggestion: str | None = None


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Warning-grade repo hygiene checks for project-context drift. "
            "Does not replace the runtime shape checker."
        )
    )
    parser.add_argument(
        "--repo-root",
        help="explicit repo root to inspect when cwd detection would be ambiguous",
    )
    parser.add_argument(
        "--recent-days",
        type=int,
        default=30,
        help="how many recent task days count for legacy surface respawn checks",
    )
    parser.add_argument(
        "--warn-extra-docs",
        type=int,
        default=7,
        help="warn threshold for top-level extra task docs",
    )
    parser.add_argument(
        "--info-extra-docs",
        type=int,
        default=4,
        help="info threshold for top-level extra task docs",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit findings as JSON",
    )
    return parser.parse_args(argv)


def main(
    argv: list[str] | None = None,
    runtime: runtime_shape.RuntimePaths | None = None,
) -> int:
    args = parse_args(argv)
    if runtime is None:
        repo_root = (
            Path(args.repo_root).resolve()
            if args.repo_root is not None
            else runtime_shape.detect_repo_root(Path.cwd())
        )
        runtime = runtime_shape.runtime_paths(repo_root)

    runtime_shape.set_display_root(runtime.repo_root)
    findings = run_gardening_checks(
        runtime,
        recent_days=args.recent_days,
        warn_extra_docs=args.warn_extra_docs,
        info_extra_docs=args.info_extra_docs,
    )
    report_findings(findings, as_json=args.json)
    return 0


def run_gardening_checks(
    runtime: runtime_shape.RuntimePaths | None = None,
    *,
    recent_days: int = 30,
    warn_extra_docs: int = 7,
    info_extra_docs: int = 4,
) -> list[Finding]:
    runtime = runtime or runtime_shape.runtime_paths(runtime_shape.detect_repo_root(Path.cwd()))
    runtime_shape.set_display_root(runtime.repo_root)

    findings: list[Finding] = []
    findings.extend(check_empty_task_dirs(runtime))
    findings.extend(check_legacy_surface_respawn(runtime, recent_days=recent_days))
    findings.extend(
        check_extra_task_doc_growth(
            runtime,
            warn_extra_docs=warn_extra_docs,
            info_extra_docs=info_extra_docs,
        )
    )
    findings.extend(check_root_overlay_mixing(runtime))
    return findings


def report_findings(findings: list[Finding], *, as_json: bool = False) -> None:
    if as_json:
        print(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2))
        return

    if not findings:
        print("[OK] project-context gardening checks")
        return

    header_severity = "WARN" if any(item.severity == "WARN" for item in findings) else "INFO"
    print(f"[{header_severity}] project-context gardening checks")
    for item in findings:
        line = f"[{item.severity}] {item.code}: {item.path}"
        if item.detail:
            line = f"{line} ({item.detail})"
        print(line)
        if item.suggestion:
            print(f"  suggestion: {item.suggestion}")


def candidate_task_dirs(task_root: Path) -> list[Path]:
    if not task_root.exists():
        return []

    tasks: list[Path] = []
    for year_dir in runtime_shape.visible_children(task_root):
        if not year_dir.is_dir() or not runtime_shape.TASK_YEAR_RE.match(year_dir.name):
            continue
        for date_dir in runtime_shape.visible_children(year_dir):
            if not date_dir.is_dir() or not runtime_shape.TASK_DATE_RE.match(date_dir.name):
                continue
            if not runtime_shape.is_valid_task_date(year_dir.name, date_dir.name):
                continue
            for task_dir in runtime_shape.visible_children(date_dir):
                if task_dir.is_dir() and runtime_shape.KEBAB_NAME_RE.match(task_dir.name):
                    tasks.append(task_dir)
    return tasks


def task_date(task_dir: Path) -> date | None:
    try:
        return datetime.strptime(
            f"{task_dir.parent.parent.name}-{task_dir.parent.name}",
            "%Y-%m-%d",
        ).date()
    except ValueError:
        return None


def is_recent_task(task_dir: Path, *, recent_days: int) -> bool:
    task_day = task_date(task_dir)
    if task_day is None:
        return False
    return task_day >= (date.today() - timedelta(days=recent_days))


def check_empty_task_dirs(runtime: runtime_shape.RuntimePaths) -> list[Finding]:
    runtime_shape.set_display_root(runtime.repo_root)
    findings: list[Finding] = []
    for task_dir in candidate_task_dirs(runtime.task_root):
        existing_core = [rel_name for rel_name in runtime_shape.CORE_TASK_FILES if (task_dir / rel_name).exists()]
        if not existing_core:
            findings.append(
                Finding(
                    severity="WARN",
                    code="empty-task-dir",
                    path=runtime_shape.rel(task_dir),
                    suggestion="create BRIEF/logs or remove the directory",
                )
            )
    return findings


def check_legacy_surface_respawn(
    runtime: runtime_shape.RuntimePaths,
    *,
    recent_days: int,
) -> list[Finding]:
    runtime_shape.set_display_root(runtime.repo_root)
    findings: list[Finding] = []
    memory_doc = runtime.docs_root / "memory.md"
    if memory_doc.exists():
        findings.append(
            Finding(
                severity="WARN",
                code="legacy-surface-respawn",
                path=runtime_shape.rel(memory_doc),
                suggestion="remove the legacy memory surface or migrate its current state into BRIEF/reference",
            )
        )

    for task_dir in candidate_task_dirs(runtime.task_root):
        if not is_recent_task(task_dir, recent_days=recent_days):
            continue
        for filename in LEGACY_SURFACES:
            path = task_dir / filename
            if path.exists():
                findings.append(
                    Finding(
                        severity="WARN",
                        code="legacy-surface-respawn",
                        path=runtime_shape.rel(path),
                        suggestion="keep current state in BRIEF and logs instead of reviving this legacy surface",
                    )
                )
    return findings


def check_extra_task_doc_growth(
    runtime: runtime_shape.RuntimePaths,
    *,
    warn_extra_docs: int,
    info_extra_docs: int,
) -> list[Finding]:
    runtime_shape.set_display_root(runtime.repo_root)
    findings: list[Finding] = []
    for task_dir in candidate_task_dirs(runtime.task_root):
        extra_docs = [
            path
            for path in sorted(task_dir.glob("*.md"))
            if path.name not in {"BRIEF.md", *LEGACY_SURFACES}
        ]
        count = len(extra_docs)
        if count >= warn_extra_docs:
            severity = "WARN"
        elif count >= info_extra_docs:
            severity = "INFO"
        else:
            continue

        findings.append(
            Finding(
                severity=severity,
                code="task-extra-doc-growth",
                path=runtime_shape.rel(task_dir),
                detail=f"{count} extra top-level docs",
                suggestion=(
                    "promote durable rules to docs/reference/**, or if this is one long-running task, "
                    "keep the root canonical and move temporary working notes into working/ plus archive as needed"
                ),
            )
        )
    return findings


def check_root_overlay_mixing(runtime: runtime_shape.RuntimePaths) -> list[Finding]:
    runtime_shape.set_display_root(runtime.repo_root)
    findings: list[Finding] = []
    for task_dir in candidate_task_dirs(runtime.task_root):
        stems = {
            path.stem.upper()
            for path in task_dir.glob("*.md")
            if path.name not in {"BRIEF.md", *LEGACY_SURFACES}
        }
        if not stems:
            continue

        has_canonical = any(stem in CANONICAL_ROOT_STEMS for stem in stems)
        has_overlay = any(any(keyword in stem for keyword in OVERLAY_KEYWORDS) for stem in stems)
        if not (has_canonical and has_overlay):
            continue

        findings.append(
            Finding(
                severity="INFO",
                code="root-overlay-mixing",
                path=runtime_shape.rel(task_dir),
                suggestion="keep canonical docs at root, move temporary working notes into working/, and archive absorbed remnants instead of leaving them mixed at root",
            )
        )
    return findings


if __name__ == "__main__":
    raise SystemExit(main())
