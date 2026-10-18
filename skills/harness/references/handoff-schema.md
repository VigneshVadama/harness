# Handoff Schema

Use these schemas so another agent can consume the result without reading the whole conversation.

## Orchestrator Phase Plan

```yaml
objective:
mission_folder:
acceptance_criteria:
constraints:
non_goals:
phases:
  - name:
    purpose:
    worker_missions:
    deterministic_checks:
    validator_mission:
risks:
open_questions:
```

## Worker Mission

```yaml
mission:
mission_folder:
context:
scope:
owned_files:
forbidden_files:
allowed_tools:
required_commands:
stop_conditions:
quality_bar:
checklist_sections: [core, <selected>]
output_schema:
  changed_paths:
  summary:
  evidence:
  commands_run:
  checklist:
  remaining_risks:
  handoff_for_validator:
```

## Worker Result

```yaml
changed_paths:
summary:
evidence:
commands_run:
checklist:
  sections: [core, <selected>]
  fail:
    - slug:
      evidence:
  na:
    - slug:
      reason:
remaining_risks:
handoff_for_validator:
```

The `checklist` block is REQUIRED for coding missions and omitted otherwise. List exceptions only: `fail` with evidence, `na` with a reason. An item not listed is an asserted pass. DO NOT list passes.

## Validator Mission

```yaml
mission:
mission_folder:
scope:
worker_output_to_validate:
required_commands:
independent_probes:
acceptance_criteria:
rejection_criteria:
output_schema:
  verdict: accept | accept_with_fixes | reject
  commands_run:
  inspected_files:
  checklist_contradicted:
  blockers:
  non_blocking_notes:
  confidence: low | medium | high
```

## Validator Result

Returned in the validator's final message; not written to a file.

```yaml
verdict:
commands_run:
inspected_files:
checklist_contradicted:
  - slug:
    evidence:
blockers:
  - path:
    line:
    issue:
    evidence:
non_blocking_notes:
confidence:
```

`checklist_contradicted` is REQUIRED when the worker result carries a `checklist` block; use `[]` when nothing is contradicted. Verify every `fail` and `na`, then check core and the highest-risk selected items against the diff. Report contradictions only.

Workers never self-accept. Validators are read-only.
