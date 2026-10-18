# Example: Document Knowledge Extraction

## Orchestrator Setup

```yaml
objective: Convert source documents into readable, linked knowledge files true to source.
mission_folder: missions/20260519-120000-domain-extraction
acceptance_criteria:
  - indexes are navigational
  - content preserves source hierarchy
  - images are extracted and referenced
  - validator verdict is accept
```

## Worker Mission

```yaml
mission: Extract one source section into Markdown knowledge files.
mission_folder: missions/20260519-120000-domain-extraction
scope: Source Section A only.
owned_files:
  - knowledge/source-section-a/**
forbidden_files:
  - knowledge/other-sections/**
required_commands:
  - python scripts/quality_report.py --root knowledge
stop_conditions:
  - stop after Source Section A
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
mission: Validate extraction against source; do not edit files.
mission_folder: missions/20260519-120000-domain-extraction
required_commands:
  - python scripts/quality_report.py --root knowledge
independent_probes:
  - sample source pages against Markdown
  - check image links exist
  - verify heading hierarchy and table structure
output_schema:
  verdict: accept | accept_with_fixes | reject
  commands_run:
  inspected_files:
  blockers:
  non_blocking_notes:
  confidence:
```
