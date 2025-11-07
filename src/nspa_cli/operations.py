"""Implementation of the CLI operations."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path


class NspaError(RuntimeError):
    """Base error for CLI failures."""


@dataclass(slots=True)
class CopyReport:
    """Tracks copy results for a given destination directory."""

    target_dir: Path
    created: list[Path]
    skipped: list[Path]


@dataclass(slots=True)
class InitResult:
    """Result data for the init command."""

    commands: CopyReport
    nspa: CopyReport


PACKAGE_ROOT = Path(__file__).resolve().parent
NSPA_BUNDLE_DIR = PACKAGE_ROOT / "data" / "nspa"
CLAUDE_COMMANDS_DIR = NSPA_BUNDLE_DIR / "AA"
TEMPLATE_SUFFIX = ".md"


def _copy_command_templates(destination: Path, *, force: bool) -> CopyReport:
    if not CLAUDE_COMMANDS_DIR.is_dir():
        raise NspaError("Command templates are missing from the installation.")

    template_files = sorted(CLAUDE_COMMANDS_DIR.glob(f"*{TEMPLATE_SUFFIX}"))
    if not template_files:
        raise NspaError("No command templates were bundled with the installation.")

    destination.mkdir(parents=True, exist_ok=True)

    created: list[Path] = []
    skipped: list[Path] = []

    for source in template_files:
        target_name = source.name
        if not target_name.startswith("nspa."):
            target_name = f"nspa.{target_name}"

        target = destination / target_name
        if target.exists() and not force:
            skipped.append(target)
            continue

        shutil.copy2(source, target)
        created.append(target)

    if not created and not skipped:
        raise NspaError("No command templates were processed. Nothing to do.")

    return CopyReport(target_dir=destination, created=created, skipped=skipped)


def _copy_nspa_bundle(destination: Path, *, force: bool) -> CopyReport:
    if not NSPA_BUNDLE_DIR.is_dir():
        raise NspaError("NSPA bundle is missing from the installation.")

    destination.mkdir(parents=True, exist_ok=True)

    created: list[Path] = []
    skipped: list[Path] = []

    for source in sorted(NSPA_BUNDLE_DIR.rglob("*")):
        relative = source.relative_to(NSPA_BUNDLE_DIR)
        if not relative.parts:
            continue
        if relative.parts[0] == "AA":
            continue
        target = destination / relative

        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue

        if target.exists() and not force:
            skipped.append(target)
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        created.append(target)

    if not created and not skipped:
        raise NspaError("No NSPA files were bundled with the installation.")

    return CopyReport(target_dir=destination, created=created, skipped=skipped)


def init_project(project_root: Path, *, force: bool = False) -> InitResult:
    """Copy .claude templates and the .nspa bundle into the target project."""

    if not project_root:
        raise NspaError("A project path must be provided.")

    destination = project_root.expanduser().resolve()
    destination.mkdir(parents=True, exist_ok=True)

    commands_dir = destination / ".claude" / "commands"
    nspa_dir = destination / ".nspa"

    commands_report = _copy_command_templates(commands_dir, force=force)
    nspa_report = _copy_nspa_bundle(nspa_dir, force=force)

    return InitResult(commands=commands_report, nspa=nspa_report)
