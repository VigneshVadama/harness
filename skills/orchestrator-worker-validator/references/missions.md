# Missions

Use `missions/` for ignored shared state when work needs more than one agent or phase.

## Directory

Create one folder per phase:

```text
missions/<YYYYMMDD-HHMMSS>-<slug>/
```

Required files:

- `mission.md`: orchestrator-owned scope, acceptance criteria, worker mission, validator mission, and commands.
- `worker-result.md`: worker-owned changed paths, evidence, commands run, risks, and handoff.
- `validator-result.md`: validator-owned verdict, inspected files, commands, blockers, notes, and confidence.
- `summary.md`: orchestrator-owned accepted result, residual risks, and durable lessons.

Rules:

- Do not commit mission folders.
- Agents may write only inside the active mission folder unless the mission grants explicit file ownership.
- Keep detailed traces in `missions/`; move only stable, validated lessons into tracked skills, agents, tests, or docs.
