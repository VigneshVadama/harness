# Contributing

Keep this repo focused on reusable agent harness patterns.

## Rules

- Keep the canonical skill in `skills/orchestrator-worker-validator/`.
- Do not edit generated template mirrors by hand; run `python3 scripts/sync_mirrors.py`.
- Keep agents narrow: orchestrator plans and gates, worker executes bounded missions, validator reviews adversarially.
- Run `python3 scripts/validate.py` before submitting changes.
- Do not add vendor-specific claims unless the referenced platform docs or local validator support them.

## Release Checklist

1. Run `python3 scripts/sync_mirrors.py`.
2. Run `python3 scripts/validate.py`.
3. Run platform validators listed in `README.md`.
4. Update the registry tracking issue if any submission state changes.

## Packaging and model policy

`PACKAGING.md` is the repo-level map of plugin entrypoints, per-tool templates, and the model-per-role policy table. It is deliberately outside the skill: vendored installs receive only the skill directory, and installation metadata is not workflow instruction. Update `PACKAGING.md` when plugin layouts or default models change.
