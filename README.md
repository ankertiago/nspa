# NSPA CLI

`nspa` is a lightweight bootstrapper that copies the bundled Claude command templates into any project. It mirrors the developer experience of `spec-kit`, but it is hard-wired to Claude Code as requested in `todo.md`.

## Installation

```bash
uv tool install nspa-cli --from git+https://github.com/ankertiago/nspa-kit.git
```

## Usage

```bash
# Inside an existing project (or provide a path)
nspa init .
```

The command creates (or updates) `.claude/commands` inside the target project and copies every bundled `*.md` template into that directory. Use `--force` to overwrite files that already exist.
