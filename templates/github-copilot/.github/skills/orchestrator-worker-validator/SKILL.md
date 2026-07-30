---
name: orchestrator-worker-validator
description: Use this skill for any non-trivial engineering task — coding, refactoring, debugging, code review, document extraction, or multi-step changes — even when the user only says implement, fix, review, or ship without naming a workflow. It runs the full delivery loop; plan, bounded worker missions, adversarial validation, a no-skip coding checklist, layered token-efficient communication, then docs, conventional commit, pull request, review triage to resolved threads, and merge. Do not use it for one-line answers or trivial single-file edits with no delivery step.
license: MIT
---

# Orchestrator Worker Validator

One harness, full loop: plan, bounded missions, adversarial validation, checklist gate, docs, commit, PR, merge. MUST, MUST NOT, SHOULD, MAY are RFC 2119 keywords — capitalize them in every mission, rule, review.

## Roles

Roles permanent. Models = install-time configuration, one place per tool. One agent product runs all three roles via subagents — no second peer agent required.

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
7. Deliver per references/delivery.md: docs, secret scan, conventional commit, push, PR, review triaged and every thread resolved, merge.
8. Close mission with `summary.md`.

## References

Load each file at the moment named, not before:

- references/handoff-schema.md — when writing a mission, worker result, or validator result.
- references/missions.md — when creating the first mission folder of a task.
- references/validator-rubric.md — when dispatching or acting as the validator.
- references/checklist.md — when a coding mission starts; references/checklist-examples.md only when an item says `see examples`.
- references/communication.md — before the first message or artifact of a session.
- references/delivery.md — when the validator has accepted and delivery begins.
- examples/code-change.md or examples/document-knowledge-extraction.md — when running the workflow for the first time.
