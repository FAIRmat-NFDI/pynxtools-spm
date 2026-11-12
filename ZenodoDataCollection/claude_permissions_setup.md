# Claude Code — Permissions Setup for Zenodo → S3 Pipeline

By default, Claude Code prompts for approval on every shell command it runs.
For long-running pipelines (downloads, uploads, log monitoring), this is
disruptive. The fix is to add an allowlist to the project settings file so
Claude never prompts for those specific commands again.

## What was configured

File: `.claude/settings.json` (project-scoped, applies only to this repo)

```json
"Bash(aws s3 *)",
"Bash(aws s3api *)",
"Bash(ps *)",
"Bash(grep *)",
"Bash(tail *)",
"Bash(curl *)",
"Bash(wget *)",
"Bash(bash ZenodoDataCollection/*)",
"Bash(bash /tmp/*)",
"Bash(mkdir *)",
"Bash(mv *)",
"Bash(cp *)",
"Bash(rm *)",
"Bash(cat *)"
```

## How to apply the same fix in another project

1. Open (or create) `.claude/settings.json` at the project root.
2. Add a `permissions.allow` array with `"Bash(<command> *)"` entries for
   each command pattern you want auto-approved.
3. Start a new Claude Code session (or run `/clear`) to reload the settings.

## How to reload settings without restarting

- **VS Code extension:** `Ctrl+Shift+P` → `Claude: New Session`, or click `+`
- **Terminal CLI:** exit (`/exit`) and run `claude` again
- **Quickest:** type `/clear` in the current chat

## Permission rule syntax

| Pattern | Matches |
|---|---|
| `Bash(aws s3 *)` | `aws s3 ls`, `aws s3 cp ...`, `aws s3 sync ...`, etc. |
| `Bash(aws s3 *)` | Any `aws s3` subcommand |
| `Bash(grep *)` | Any `grep` invocation |
| `Read` | All Read operations (no path restriction) |
| `Read(/path/to/dir/**)` | Read only under a specific directory |

## Scope of this configuration

These permissions are **project-scoped**: they only take effect when Claude
Code is running inside this repository (`pynxtools-spm/`). They are not
applied globally to other projects.

To make a permission global instead, add the same rule to
`~/.claude/settings.json`.
