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
output_schema:
  changed_paths:
  summary:
  evidence:
  commands_run:
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
  sections:
  items:
    - slug:
      verdict: pass | fail | n/a
      evidence_or_justification:
remaining_risks:
handoff_for_validator:
```

The `checklist` block is REQUIRED for coding missions and omitted otherwise. Every item in the selected sections appears exactly once.

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
  blockers:
  non_blocking_notes:
  confidence: low | medium | high
```

## Validator Result

```yaml
verdict:
commands_run:
inspected_files:
checklist_verified:
  - slug:
    worker_verdict:
    validator_finding: confirmed | contradicted
blockers:
  - path:
    line:
    issue:
    evidence:
non_blocking_notes:
confidence:
```

`checklist_verified` is REQUIRED when the worker result carries a `checklist` block. Spot-verify every `n/a` and at least the highest-risk `pass` items.

Workers never self-accept. Validators must be read-only unless explicitly asked to patch.
