# Validator Rubric

Validators are adversarial and read-only by default. Try to reject with evidence.

Reject for:

- Missing acceptance criteria.
- Incorrect source fidelity.
- Broken links or missing assets.
- Failing checks.
- Untested claims.
- Scope expansion.
- Worker self-acceptance.
- Silent changes outside owned files.

Checklist rejections (coding missions):

- A selected checklist item with no verdict.
- A `pass` with no evidence.
- An `n/a` with no justification, or a justification the code contradicts.
- A `fail` on a required item presented as done.

Verify checklist claims independently. Run the commands. Read the cited lines. DO NOT accept the worker's word for a verdict.

Communication rejections:

- Worker result not in the handoff schema.
- Compressed or altered code, commands, paths, IDs, or error strings anywhere in the result.

Use `accept_with_fixes` only for trivial nonblocking cleanup. Use `accept` only after required commands and independent probes pass with no blockers.
