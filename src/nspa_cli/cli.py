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


def _format_init_summary(result: InitResult) -> str:
    created_count = len(result.created)
    skipped_count = len(result.skipped)
    parts = [
        f"Installed {created_count} template{'s' if created_count != 1 else ''} ",
        f"into {result.target_dir}",
    ]
    if skipped_count:
        parts.append(f" ({skipped_count} file{'s' if skipped_count != 1 else ''} skipped)")
    return "".join(parts)


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
