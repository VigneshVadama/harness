# Example: Code Change Workflow

## Orchestrator Setup

```yaml
objective: Implement a scoped feature without broad refactors.
mission_folder: missions/20260519-120000-parser-change
acceptance_criteria:
  - requested behavior works
  - tests/lint/type checks pass
  - no unrelated files changed
  - every selected checklist item has a verdict with evidence or justification
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
  - existing-code
  - naming
  - presentation
  - errors
  - tests
  - complexity
  - release
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
  sections: [existing-code, naming, presentation, errors, tests, complexity, release]
  items:
    - slug: errors/check-every-return
      verdict: pass
      evidence_or_justification: "parse_row handles None from _split (parser.py:88); test_parser.py::test_empty_row covers it"
    - slug: release/clean-checkout
      verdict: n/a
      evidence_or_justification: "no release in this mission; change ships via normal PR flow"
```

Every item in the selected sections appears. An `n/a` without a justification is a validator rejection.

## Validator Mission

```yaml
mission: Review the parser change adversarially; do not edit files.
mission_folder: missions/20260519-120000-parser-change
required_commands:
  - uv run pytest tests/test_parser.py
independent_probes:
  - inspect changed code paths
  - test edge cases not mentioned by worker
  - re-verify checklist verdicts; spot-check every n/a
output_schema:
  verdict: accept | accept_with_fixes | reject
  commands_run:
  inspected_files:
  checklist_verified:
  blockers:
  non_blocking_notes:
  confidence:
```

## Delivery (after accept)

1. Docs worker updates affected docs; skip only when no behavior or interface changed.
2. Secret scan on the staged diff. A finding blocks the commit.
3. Stage explicit paths. Commit: `feat(ingest): handle empty parser rows (#42)`.
4. Push. Open the PR referencing the issue. Request required reviewers.
5. Triage every review finding with evidence. Merge when reviews and CI are green.
