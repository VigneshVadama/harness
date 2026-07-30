---
name: orchestrator-worker-validator
description: Complete delivery harness for agent work. Use for non-trivial coding, refactoring, debugging, review, extraction, or any multi-phase task. Combines lean orchestration, bounded worker missions, adversarial validation, a no-skip coding checklist, layered token-efficient communication, and a docs-commit-PR delivery loop. Trigger on complex work, code changes, code review, checklist discipline, commit, pull request, or multi-agent delegation.
license: MIT
---

# Orchestrator Worker Validator

One harness, full loop: plan, bounded missions, adversarial validation, checklist gate, docs, commit, PR, merge. MUST, MUST NOT, SHOULD, MAY are RFC 2119 keywords — capitalize them in every mission, rule, review.

## Roles

Roles permanent. Models = configuration, one place per tool (references/platform-packaging.md). One agent product runs all three roles via subagents — no second peer agent required.

| Role | Duty | Model |
|---|---|---|
| orchestrator | scope, phases, dispatch, integration, user comms, acceptance | session model |
| worker | one bounded mission, evidence, handoff | cheap competent, minimal reasoning |
| validator | adversarial read-only review, independent probes | strong — never economize the gate |

## Core rules

1. Orchestrator context stays lean. Detailed state lives in the mission folder, not chat.
2. Every mission MUST name scope, owned files, forbidden files, deliverables, checks, stop conditions, output schema, mission folder.
3. Validator MUST try to reject with evidence. Verdict exactly `accept` | `accept_with_fixes` | `reject`.
4. No acceptance without validator verdict. Workers MUST NOT self-accept.
5. Coding missions carry the checklist. Silent skip = rejection.
6. Communication law binds all agents.
7. Repeated failures become deterministic checks, tests, scripts, or checklist items.
8. Close finished agents. Keep only structured findings.
9. VERY IMPORTANT — dependency versions come from the package registry at install time (query latest or compatible: `npm view`, `pip index versions`, `go list -m -versions`, registry.terraform.io, `brew info`). MUST NOT write a version from model memory: stale or hallucinated pins are a supply-chain attack surface.

## Communication law

Read references/communication.md before writing anything. Three layers: agent-to-agent compressed; human-facing action-first; durable artifacts in controlled English with RFC 2119 keywords. Code, commands, paths, IDs, secret refs, error strings: EXACT at every layer.

## Checklist gate

references/checklist.md. Orchestrator selects sections by task type in the mission. Worker reports every selected item: `pass` + evidence, `fail`, or `n/a` + one-line justification. DO NOT SKIP silently — missing verdict, evidence-free pass, unjustified n/a = validator rejection. Validator re-verifies independently.

## Workflow

1. Frame objective, constraints, non-goals, acceptance criteria, risks, phases.
2. Create `missions/<YYYYMMDD-HHMMSS>-<slug>/mission.md`.
3. Dispatch bounded workers, disjoint write sets when possible.
4. Run deterministic checks.
5. Dispatch adversarial validator.
6. On reject: repair blockers only, add guards.
7. Deliver per references/delivery.md: docs, secret scan, conventional commit, push, PR, Copilot review to green, merge.
8. Close mission with `summary.md`.

## References

- references/handoff-schema.md — mission, worker, validator output schemas.
- references/missions.md — shared mission-state rules.
- references/validator-rubric.md — rejection rules.
- references/checklist.md — coding checklist; load references/checklist-examples.md only when an item says `see examples`.
- references/communication.md — communication law.
- references/delivery.md — docs, commit, PR, review loop.
- references/platform-packaging.md — plugins, templates, model configuration.
- examples/code-change.md, examples/document-knowledge-extraction.md — complete workflows.
