# NSPA CLI

`nspa` 是一个轻量级脚手架，安装后运行 `nspa init <PROJECT>` 就会把内置的 Claude commands 以及 `.nspa` 所需的 `memory/`, `templates/`, `scripts/` 三类文件同步到任意工程中，整体体验与 `spec-kit` 类似，但默认面向 Claude Code。

## Installation

```bash
uv tool install nspa-cli --from git+https://github.com/ankertiago/nspa.git
```

## Usage

```bash
# Inside an existing project (or provide a path)
nspa init .
```

运行后会：

- 创建/更新 `.claude/commands`，将所有 `*.md` 模板复制进去；
- 创建 `.nspa` 目录，并保留 `memory/`, `templates/`, `scripts/` 的子目录结构与文件；
- 通过 `--force` 可以覆盖目标项目中已存在的同名文件。

## Update

```bash
uv tool update nspa-cli --from git+https://github.com/ankertiago/nspa.git
```

如果 `uv` 版本较老尚未提供 `tool update`，可以退一步执行：

```bash
uv tool install nspa-cli --from git+https://github.com/ankertiago/nspa.git --reinstall
```

上述命令会拉取最新仓库代码并覆盖现有的 `nspa` 工具。
