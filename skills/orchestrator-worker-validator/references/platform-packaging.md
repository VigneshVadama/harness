# Platform Packaging

The canonical skill is `skills/orchestrator-worker-validator`.

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
