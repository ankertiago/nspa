"""Command line entry point for the nspa CLI."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from . import __version__
from .operations import InitResult, NspaError, init_project


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="nspa",
        description="Bootstrap .claude command files for a project.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser(
        "init", help="Copy the bundled command templates into a project.",
    )
    init_parser.add_argument(
        "project_path",
        nargs="?",
        default=".",
        help="Project directory where .claude/commands should be created.",
    )
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files instead of skipping them.",
    )

    return parser


def _format_section(label: str, count: int, skipped: int, target: Path) -> str:
    plural = "s" if count != 1 else ""
    section = f"{label}: installed {count} file{plural} into {target}"
    if skipped:
        skipped_plural = "s" if skipped != 1 else ""
        section += f" ({skipped} file{skipped_plural} skipped)"
    return section


def _format_init_summary(result: InitResult) -> str:
    command_section = _format_section(
        "Claude commands",
        len(result.commands.created),
        len(result.commands.skipped),
        result.commands.target_dir,
    )
    nspa_section = _format_section(
        ".nspa bundle",
        len(result.nspa.created),
        len(result.nspa.skipped),
        result.nspa.target_dir,
    )
    return f"{command_section}; {nspa_section}"


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "init":
            result = init_project(Path(args.project_path), force=args.force)
            print(_format_init_summary(result))
        else:
            parser.error("No command provided.")
    except NspaError as exc:  # pragma: no cover - defensive
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
