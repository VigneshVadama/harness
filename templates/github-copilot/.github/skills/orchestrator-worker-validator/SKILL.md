---
name: orchestrator-worker-validator
description: Complete delivery harness for agent work. Use for non-trivial coding, refactoring, debugging, review, extraction, or any multi-phase task. Combines lean orchestration, bounded worker missions, adversarial validation, a no-skip coding checklist, layered token-efficient communication, and a docs-commit-PR delivery loop. Trigger on complex work, code changes, code review, checklist discipline, commit, pull request, or multi-agent delegation.
license: MIT
---

# Orchestrator Worker Validator

One harness for the full loop: plan, bounded missions, adversarial validation, checklist gate, docs, commit, pull request, merge.

The key words MUST, MUST NOT, SHOULD, and MAY are RFC 2119 keywords. Write them capitalized in every mission, rule, and review.

## Roles

Roles are permanent. Models are configuration.

| Role | Duty | Model policy |
|---|---|---|
| orchestrator | Scope, phases, decisions, dispatch, integration, user communication, final acceptance | Session model — the strongest available |
| worker | One bounded mission with evidence and a validator handoff | Cheap competent model, minimal reasoning |
| validator | Adversarial read-only review with independent probes | Strong model — do not economize on the gate |

Each tool sets role models in exactly one place. See [references/platform-packaging.md](references/platform-packaging.md). When models change, change one line per tool. Never change the roles.

## Core rules

1. The orchestrator MUST keep its context lean. Detailed state lives in the mission folder, not in chat history.
2. Every mission MUST name scope, owned files, forbidden files, deliverables, checks, stop conditions, output schema, and the mission folder.
3. Validators MUST try to reject with evidence and MUST return exactly `accept`, `accept_with_fixes`, or `reject`.
4. The orchestrator MUST NOT accept worker output without a validator verdict. Workers MUST NOT self-accept.
5. Coding missions MUST carry the coding checklist. Every selected item gets an explicit verdict. Silent skips are a rejection. See [Checklist gate](#checklist-gate).
6. All agents MUST follow the communication law. See [Communication law](#communication-law).
7. Repeated failures and validator findings MUST become deterministic checks, tests, scripts, or checklist items.
8. Close completed agents. Retain only structured findings.

## Communication law

Three layers. Read [references/communication.md](references/communication.md) before writing anything.

1. **Agent to agent** (missions, handoffs, results): compressed. Drop articles, filler, hedging, pleasantries. Keep every technical fact.
2. **Human-facing** (chat, reports): action first, numbered steps, no preamble, no recap, one concrete next action.
3. **Durable artifacts** (docs, READMEs, ADRs, PR bodies): controlled technical English — one instruction per sentence, active voice, present tense, RFC 2119 keywords.

Code, commands, paths, IDs, secret references, and error strings stay EXACT at every layer. Compression never touches them.

## Checklist gate

The coding checklist in [references/checklist.md](references/checklist.md) is part of every coding mission and every validation.

1. The orchestrator selects checklist sections by task type and lists them in the mission.
2. The worker works with the selected sections active and reports every selected item in `worker-result.md` with one verdict: `pass` with evidence, `fail`, or `n/a` with a one-line justification.
3. DO NOT SKIP items silently. An unreported item, an evidence-free `pass`, or an unjustified `n/a` is a validator rejection.
4. The validator MUST independently re-verify checklist claims, not just read them.

## Workflow

1. Frame objective, constraints, non-goals, acceptance criteria, risks, and phases.
2. Create `missions/<YYYYMMDD-HHMMSS>-<slug>/mission.md`.
3. Dispatch bounded workers with disjoint write sets whenever possible.
4. Run deterministic checks.
5. Dispatch an adversarial validator.
6. If rejected, repair only blockers and add guards when feasible.
7. Deliver: docs mission, secret scan, conventional commit, push, pull request, review loop. See [references/delivery.md](references/delivery.md).
8. Close the mission with `summary.md`.

## References

- Read [references/handoff-schema.md](references/handoff-schema.md) for mission, worker, and validator output schemas.
- Read [references/missions.md](references/missions.md) for shared mission-state rules.
- Read [references/validator-rubric.md](references/validator-rubric.md) for adversarial review rules.
- Read [references/checklist.md](references/checklist.md) for the coding checklist; load [references/checklist-examples.md](references/checklist-examples.md) only when an item says `see examples`.
- Read [references/communication.md](references/communication.md) for the communication law.
- Read [references/delivery.md](references/delivery.md) for the docs, commit, and pull-request loop.
- Read [references/platform-packaging.md](references/platform-packaging.md) before changing plugin, template, or model configuration.
- See [examples/code-change.md](examples/code-change.md) and [examples/document-knowledge-extraction.md](examples/document-knowledge-extraction.md) for complete workflows.

## Validation

Run:

```sh
python3 scripts/validate.py
```
