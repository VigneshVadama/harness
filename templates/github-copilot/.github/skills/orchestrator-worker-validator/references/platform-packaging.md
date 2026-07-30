# Platform Packaging

Paths in this file describe the upstream harness repo (github.com/VigneshVadama/harness). Vendored installs live where the installer puts them — `bunx skills add` writes `.agents/skills/orchestrator-worker-validator/`; consuming repos MAY symlink tool dirs to it. The upstream canonical skill is `skills/orchestrator-worker-validator`.

## Model policy

Roles are permanent; models are configuration. Each tool pins role models in exactly one place:

| Tool | Where | Current default |
|---|---|---|
| Claude Code | `agents/*.md` frontmatter `model:` | orchestrator `inherit` (session), worker `sonnet`, validator `opus` |
| Codex | `templates/codex/.codex/agents/*.toml` `model` + `model_reasoning_effort` | set `model` per deployment; worker effort `low`, validator `high`, orchestrator `xhigh` |
| GitHub Copilot | `github-copilot/agents/*.agent.md` frontmatter `model:` | `GPT-5.4` |
| Claude Managed Agents | `templates/claude-managed-agents/*.yaml` | per-deployment |

Pick a cheap competent model for workers and a strong model for validators. When models change, update these files only. MUST NOT encode model names anywhere else.

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
