---
name: orchestrator-worker-validator
description: Use when complex work needs a lean orchestrator, bounded worker missions, adversarial validation, shared mission state, deterministic checks, and no worker self-acceptance.
license: MIT
---

# Orchestrator Worker Validator

Use this harness when work is too large, fragile, or high-risk for one uninterrupted agent pass.

## Core Rules

1. Keep the orchestrator context lean. It owns scope, phase boundaries, decisions, integration, user communication, and final acceptance.
2. Send workers on bounded missions. Every mission must name scope, ownership, forbidden areas, deliverables, checks, stop conditions, output schema, and the active mission folder.
3. Make validators adversarial. They must try to reject with evidence and return exactly `accept`, `accept_with_fixes`, or `reject`.
4. Accept no worker output without validator review.
5. Convert repeated or validator-found failures into deterministic checks, tests, scripts, or checklist items.
6. Close completed agents and retain only structured findings.

## Workflow

1. Frame objective, constraints, non-goals, acceptance criteria, risks, and phases.
2. Create `missions/<YYYYMMDD-HHMMSS>-<slug>/mission.md`.
3. Dispatch bounded workers with disjoint write sets whenever possible.
4. Run deterministic checks.
5. Dispatch an adversarial validator.
6. If rejected, repair only blockers and add guards when feasible.
7. Close the mission with `summary.md`.

## References

- Read [references/handoff-schema.md](references/handoff-schema.md) for mission, worker, and validator output schemas.
- Read [references/missions.md](references/missions.md) for shared mission-state rules.
- Read [references/validator-rubric.md](references/validator-rubric.md) for adversarial review rules.
- Read [references/platform-packaging.md](references/platform-packaging.md) before changing plugin or template layouts.
- See [examples/code-change.md](examples/code-change.md) and [examples/document-knowledge-extraction.md](examples/document-knowledge-extraction.md) for complete workflows.

## Validation

Run:

```sh
python3 scripts/validate.py
```
