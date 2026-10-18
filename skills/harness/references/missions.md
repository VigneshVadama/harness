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

The validator is read-only. It reads `mission.md` and `worker-result.md` and returns its result (handoff-schema "Validator Result") in its final message. The orchestrator acts on it and does not store it in the folder.

Rules:

- Do not commit mission folders.
- Workers may write only inside the active mission folder unless the mission grants explicit file ownership. Validators write nothing.
- Keep detailed traces in `missions/` while the mission runs.
- On close: move durable lessons into tracked files (tests, checks, checklist items), then delete the mission folder. The final summary goes to the user, not a file.
