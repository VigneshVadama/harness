# Harness

[![skills.sh](https://skills.sh/b/VigneshVadama/harness)](https://skills.sh/VigneshVadama/harness)

Harness is an agent skill for multi-file and multi-repo engineering work. It splits the work into bounded worker missions, gates each result with an adversarial read-only validator, and ends at a local commit. It also carries an exception-based coding checklist and communication rules (compressed between agents, action-first to people).

## Install

With skills.sh:

```sh
npx skills add VigneshVadama/harness
```

Manual: copy or symlink `skills/harness/` into the skills directory of your agent.

- Claude Code reads `~/.claude/skills/`.
- OpenCode reads `~/.config/opencode/skills/`, `~/.claude/skills/` and `~/.agents/skills/`.

One install serves both: put the directory at `~/.agents/skills/harness/` and symlink `~/.claude/skills/harness` to it. OpenCode keys skills by directory name, so it loads the skill once.

## Workflow

Use it for multi-file or multi-repo engineering work, or by naming `harness`. It is not for questions or single-file edits. It has three roles:

- `orchestrator`: owns scope, mission state, worker dispatch, validation gates, and final acceptance.
- `worker`: executes one bounded mission and returns evidence.
- `validator`: reviews adversarially and read-only, probes claims independently, and returns `accept`, `accept_with_fixes`, or `reject` in its final message.

Models: orchestrator Opus, workers Sonnet, validator Haiku. The validator runs on Opus for destructive or replacing plans, migrations, and security-sensitive changes.

Shared state lives in an ignored mission folder. It is deleted when the mission closes, after durable lessons move into tracked files. The summary goes to the user.

```text
missions/<YYYYMMDD-HHMMSS>-<slug>/
  mission.md
  worker-result.md
```

Coding missions carry the coding checklist, reported by exception: the worker lists only `fail` and `na` (with reason); an unlisted item is an asserted pass. The validator verifies the listed items, checks core items against the diff, and rejects any contradiction. After acceptance the orchestrator runs the delivery loop: docs check, secret scan, explicit-path stage, conventional commit locally. It stops before push, merge, `terraform apply`, and deploy unless you asked for that action in the task.

## Validate

```sh
python3 scripts/validate.py
uvx ruff check .
uvx ruff format --check .
uvx ty check
uvx --from skills-ref agentskills validate skills/harness
```
