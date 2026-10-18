---
name: orchestrator-worker-validator
description: Use for multi-file or multi-repo engineering work (features, refactors, migrations, debugging, code review), or when asked for "harness" or "orchestrator-worker-validator". Runs bounded worker missions gated by an adversarial validator. Not for questions or single-file edits.
license: MIT
---

# Orchestrator Worker Validator

MUST, MUST NOT, SHOULD, MAY are RFC 2119 keywords: capitalize them in every mission and review.

## Roles

| Role | Duty | Model |
|---|---|---|
| orchestrator | scope, dispatch, integration, user comms, acceptance | Opus |
| worker | one bounded mission, evidence, handoff | Sonnet |
| validator | read-only adversarial review, independent probes | Haiku; the orchestrator picks Opus per mission for destructive or replacing plans, migrations, security-sensitive changes |

## Rules

1. Keep orchestrator context lean; state lives in the mission folder.
2. Every mission MUST name scope, owned and forbidden files, deliverables, checks, stop conditions, output schema.
3. Validator MUST try to reject with evidence. Verdict exactly `accept` | `accept_with_fixes` | `reject`.
4. No acceptance without a validator verdict. Workers MUST NOT self-accept.
5. Coding missions carry references/checklist.md, exception-based: workers list only `fail` and `na` (with reason); validator verifies those and reports contradictions.
6. Follow references/communication.md (compressed to agents, action-first to humans; code, paths, errors exact).
7. Repeated failures become deterministic checks, tests, or checklist items.
8. Close finished agents; keep only structured findings.
9. STOP before push, merge, terraform apply, deploy, publish, or sending messages unless the user asked for that action in this task.
10. VERY IMPORTANT: dependency versions come from the package registry at install time (`npm view`, `pip index versions`, `go list -m -versions`, registry.terraform.io, `brew info`). MUST NOT write a version from memory: stale or hallucinated pins are a supply-chain risk.

## Workflow

1. Frame objective, constraints, non-goals, acceptance criteria, risks.
2. Create `missions/<YYYYMMDD-HHMMSS>-<slug>/mission.md`.
3. Dispatch workers, disjoint write sets.
4. Run deterministic checks.
5. Dispatch the validator.
6. On reject: repair blockers only, add guards.
7. Deliver per references/delivery.md. Default ends at a local commit.
8. Close: report the summary to the user, delete the mission folder.

## References

Load when named, not before:

- references/handoff-schema.md: writing a mission or result.
- references/missions.md: first mission folder.
- references/validator-rubric.md: dispatching or acting as the validator.
- references/checklist.md: coding missions; checklist-examples.md only for `see examples`.
- references/communication.md: first message.
- references/delivery.md: after validator acceptance.
- examples/: first run of the workflow.
