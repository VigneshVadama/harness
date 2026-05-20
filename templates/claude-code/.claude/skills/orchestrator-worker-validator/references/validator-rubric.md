# Validator Rubric

Validators are adversarial and read-only by default.

Reject for:

- Missing acceptance criteria.
- Incorrect source fidelity.
- Broken links or missing assets.
- Failing checks.
- Untested claims.
- Scope expansion.
- Worker self-acceptance.
- Silent changes outside owned files.

Use `accept_with_fixes` only for trivial nonblocking cleanup. Use `accept` only after required commands and independent probes pass with no blockers.
