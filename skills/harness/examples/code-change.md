# Example: Code Change Workflow

## Orchestrator Setup

```yaml
objective: Implement a scoped feature without broad refactors.
mission_folder: missions/20260519-120000-parser-change
acceptance_criteria:
  - requested behavior works
  - tests/lint/type checks pass
  - no unrelated files changed
  - checklist holds: core plus selected sections, exceptions reported, none contradicted
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
checklist_sections: # new code or refactor
  - core
  - existing-code
  - readability
  - errors
  - tests
  - design
required_commands:
  - uv run pytest tests/test_parser.py
stop_conditions:
  - stop if API contract is ambiguous
output_schema:
  changed_paths:
  summary:
  evidence:
  commands_run:
  checklist:
  remaining_risks:
  handoff_for_validator:
```

## Worker Result (checklist excerpt)

```yaml
checklist:
  sections: [core, existing-code, readability, errors, tests, design]
  fail:
    - slug: errors/concurrency-paths
      evidence: "parse_batch shares a cache across threads (parser.py:140); blocker: the fix needs src/cache.py, a forbidden file"
  na:
    - slug: errors/graceful-shutdown
      reason: "parser is synchronous and holds no resources"
```

Unlisted items are asserted passes. An `na` without a reason, or a contradicted reason, is a validator rejection.

## Validator Mission

```yaml
mission: Review the parser change adversarially; do not edit files.
mission_folder: missions/20260519-120000-parser-change
required_commands:
  - uv run pytest tests/test_parser.py
independent_probes:
  - inspect changed code paths
  - test edge cases not mentioned by worker
  - verify every fail and na; check core and the highest-risk selected items against the diff
output_schema:
  verdict: accept | accept_with_fixes | reject
  commands_run:
  inspected_files:
  checklist_contradicted:
  blockers:
  non_blocking_notes:
  confidence:
```

## Delivery (after accept)

1. The validator is the reviewer. Copilot PR review only if the user or project asks.
2. Docs worker updates affected docs; skip only when no behavior or interface changed.
3. Secret scan on the staged diff. A finding blocks the commit.
4. Stage explicit paths. Commit locally: `feat(ingest): handle empty parser rows (#42)`.
5. STOP. Push, PR, and merge only if the user asked for them.
