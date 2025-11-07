"""Implementation of the CLI operations."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from importlib import resources
from pathlib import Path


class NspaError(RuntimeError):
    """Base error for CLI failures."""


@dataclass(slots=True)
class InitResult:
    """Result data for the init command."""

    target_dir: Path
    created: list[Path]
    skipped: list[Path]


TEMPLATE_DIRNAME = "templates"
TEMPLATE_SUFFIX = ".md"


def _resolve_template_dir() -> Path:
    root = resources.files("nspa_cli") / TEMPLATE_DIRNAME
    if not root.is_dir():
        raise NspaError("Template directory is missing from the installation.")
    return Path(root)


def init_project(project_root: Path, *, force: bool = False) -> InitResult:
    """Copy template files into the target project's `.claude/commands` directory."""

    if not project_root:
        raise NspaError("A project path must be provided.")

    destination = project_root.expanduser().resolve()
    destination.mkdir(parents=True, exist_ok=True)

    commands_dir = destination / ".claude" / "commands"
    commands_dir.mkdir(parents=True, exist_ok=True)

    template_dir = _resolve_template_dir()
    template_files = sorted(template_dir.glob(f"*{TEMPLATE_SUFFIX}"))
    if not template_files:
        raise NspaError("No template files were bundled with the installation.")

    created: list[Path] = []
    skipped: list[Path] = []

    for source in template_files:
        target = commands_dir / source.name
        if target.exists() and not force:
            skipped.append(target)
            continue

        shutil.copy2(source, target)
        created.append(target)

    if not created and not skipped:
        raise NspaError("No templates were processed. Nothing to do.")

    return InitResult(target_dir=commands_dir, created=created, skipped=skipped)
