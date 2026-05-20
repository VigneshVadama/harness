# Example: Code Change Workflow

## Orchestrator Setup

```yaml
objective: Implement a scoped feature without broad refactors.
mission_folder: missions/20260519-120000-parser-change
acceptance_criteria:
  - requested behavior works
  - tests/lint/type checks pass
  - no unrelated files changed
  - validator verdict is accept
```

## Worker Mission

```yaml
mission: Implement the parser change in the ingestion module.
mission_folder: missions/20260519-120000-parser-change
scope: parser behavior only.
owned_files:
  - src/ingest/parser.py
  - tests/test_parser.py
forbidden_files:
  - README.md
  - docs/**
required_commands:
  - uv run pytest tests/test_parser.py
stop_conditions:
  - stop if API contract is ambiguous
output_schema:
  changed_paths:
  summary:
  evidence:
  commands_run:
  remaining_risks:
  handoff_for_validator:
```

## Validator Mission

```yaml
mission: Review the parser change adversarially; do not edit files.
mission_folder: missions/20260519-120000-parser-change
required_commands:
  - uv run pytest tests/test_parser.py
independent_probes:
  - inspect changed code paths
  - test edge cases not mentioned by worker
output_schema:
  verdict: accept | accept_with_fixes | reject
  commands_run:
  inspected_files:
  blockers:
  non_blocking_notes:
  confidence:
```
