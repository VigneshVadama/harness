# Packaging

Repo-level packaging map. This file is NOT part of the skill: vendored installs receive only `skills/orchestrator-worker-validator/`. `bunx skills add` writes `.agents/skills/orchestrator-worker-validator/` in consuming repos; they MAY symlink tool dirs to it.

## Model policy

Roles are permanent; models are configuration. Each tool pins role models in exactly one place:

| Tool | Where | Current default |
|---|---|---|
| Claude Code | `agents/*.md` frontmatter `model:` | orchestrator `opus`, worker `sonnet`, validator `haiku`; the orchestrator escalates the validator to `opus` per mission (destructive or replacing plans, migrations, security-sensitive changes) |
| Codex | `templates/codex/.codex/agents/*.toml` `model` + `model_reasoning_effort` | set `model` per deployment; worker effort `low`, validator `high`, orchestrator `xhigh` |
| GitHub Copilot | `github-copilot/agents/*.agent.md` frontmatter `model:` | unset: Copilot default model |
| Claude Managed Agents | `templates/claude-managed-agents/*.yaml` `model:` | coordinator `claude-opus-5-5`, worker `claude-sonnet-5-5`, validator `claude-haiku-5-5` |

Pick a cheap competent model for workers; validators default cheap and escalate for risky missions. When models change, update these files only. Versioned model ids live only in per-tool config files and this table; the skill text names model families only.

## Codex

- Plugin entrypoint: `.codex-plugin/plugin.json`.
- Plugin exposes skills through `"skills": "./skills/"`.
- Subagent templates live in `templates/codex/.codex/agents/`.

## Claude Code

- Plugin entrypoint: `.claude-plugin/plugin.json`.
- Plugin components live at repo root: `skills/` and `agents/`.
- Agents use Claude Code agent Markdown frontmatter and are validated with Anthropic's `validate-agent.sh`.

## GitHub Copilot

- Custom-agent templates live under `github-copilot/agents/` and `templates/github-copilot/.github/agents/`.
- Project skill template lives under `templates/github-copilot/.github/skills/`.
- Do not use unsupported Copilot cloud-agent fields such as `handoffs`.

## Claude Managed Agents

- YAML templates live under `templates/claude-managed-agents/`.
- Worker and validator attach the uploaded custom skill with `skills:`.
- Coordinator uses `agent_toolset_20260401` and `multiagent.type: coordinator`.
