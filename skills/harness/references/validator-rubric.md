# Validator Rubric

Validators are adversarial and read-only. Try to reject with evidence. Return the result in your final message (handoff-schema "Validator Result"); do not write files.

Reject for:

- Missing acceptance criteria.
- Incorrect source fidelity.
- Broken links or missing assets.
- Failing checks.
- Untested claims.
- Scope expansion.
- Worker self-acceptance.
- Silent changes outside owned files.
- A new or changed dependency version with no registry-lookup evidence.

Checklist rejections (coding missions):

- A contradicted implicit pass: an unlisted item the code violates.
- An `na` with no reason, or with a reason the code contradicts.
- A `fail` on a required item presented as done.

Verify checklist claims independently. Check every `fail` and `na`, then core and the highest-risk selected items against the diff. Run the commands. Read the cited lines. DO NOT accept the worker's word. Report contradictions only, in `checklist_contradicted`.

Communication rejections:

- Worker result not in the handoff schema.
- Compressed or altered code, commands, paths, IDs, or error strings anywhere in the result.

Use `accept_with_fixes` only for trivial nonblocking cleanup. Use `accept` only after required commands and independent probes pass with no blockers.
