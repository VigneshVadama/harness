# Harness

[![skills.sh](https://skills.sh/b/VigneshVadama/harness)](https://skills.sh/VigneshVadama/harness)

Reusable orchestrator-worker-validator harness for agent workflows across Codex, Claude Code, GitHub Copilot, skills.sh, and Claude Managed Agents.

## What It Provides

- A canonical `orchestrator-worker-validator` skill.
- Claude Code plugin metadata with orchestrator, worker, and validator agents.
- Codex plugin metadata for the skill plus copyable Codex subagent templates.
- GitHub Copilot custom-agent templates and plugin metadata.
- Claude Managed Agents YAML templates and optional creation script.
- Validation scripts that check structure, frontmatter, mirror drift, and platform-specific constraints.

## Install

### skills.sh

```sh
npx skills add VigneshVadama/harness
```

### Claude Code Plugin

For local testing:

```sh
claude --plugin-dir .
```

The plugin includes:

- `skills/orchestrator-worker-validator/`
- `agents/orchestrator.md`
- `agents/worker.md`
- `agents/validator.md`

### Codex Plugin

Use this repo as a Codex plugin. The Codex plugin manifest is at `.codex-plugin/plugin.json` and exposes the canonical skill through `skills/`.

To use the Codex subagent templates in a project, copy `templates/codex/.codex/` into that project. The templates point at the plugin skill path `./skills/orchestrator-worker-validator/SKILL.md`.

### GitHub Copilot

Copy `templates/github-copilot/.github/` into a repository to use the Copilot cloud custom agents and project skill.

The custom agents are also available in `github-copilot/agents/` for awesome-copilot style submissions.

### Claude Managed Agents

Use `templates/claude-managed-agents/*.yaml` as API templates. Upload the custom skill first, set `HARNESS_SKILL_ID`, then run the optional helper:

```sh
templates/claude-managed-agents/scripts/create-managed-agents.sh --dry-run
```

The script is dry-run by default and does not create live agents unless `--apply` is passed.

## Workflow

The harness separates work into three roles:

- `orchestrator`: owns scope, mission state, worker dispatch, validation gates, and final acceptance.
- `worker`: executes one bounded mission and returns evidence.
- `validator`: reviews adversarially, independently probes claims, and returns `accept`, `accept_with_fixes`, or `reject`.

Use ignored mission folders for shared state:

```text
missions/<YYYYMMDD-HHMMSS>-<slug>/
  mission.md
  worker-result.md
  validator-result.md
  summary.md
```

## Validate

```sh
python3 scripts/validate.py
uvx ruff check .
uvx pyright .
uvx --from skills-ref agentskills validate skills/orchestrator-worker-validator
gh skill publish skills --dry-run
claude plugin validate .
curl -fsSL https://raw.githubusercontent.com/anthropics/claude-code/main/plugins/plugin-dev/skills/agent-development/scripts/validate-agent.sh -o /tmp/validate-agent.sh
bash /tmp/validate-agent.sh agents/orchestrator.md
bash /tmp/validate-agent.sh agents/worker.md
bash /tmp/validate-agent.sh agents/validator.md
```

Hosted GitHub Copilot Cloud Agent and Claude Managed Agents runtime tests require their external surfaces and are tracked separately.
