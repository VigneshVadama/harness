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
remaining_risks:
handoff_for_validator:
```

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
blockers:
  - path:
    line:
    issue:
    evidence:
non_blocking_notes:
confidence:
```

Workers never self-accept. Validators must be read-only unless explicitly asked to patch.
