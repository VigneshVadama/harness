# Delivery Loop

Run this loop after the validator accepts the work. Delivery is part of the mission, not an afterthought.

## 1. Docs mission

If the change alters behavior, structure, interfaces, or workflow, dispatch a docs worker before committing.

- The docs worker updates the project docs the change touches (README, agent instructions, ADRs).
- Docs output goes through the same validator gate as code when the change is non-trivial.
- DO NOT document features that do not exist. Planned and live MUST be visually distinct.

## 2. Secret scan

Scan the staged diff for credentials before every commit: keys, tokens, passwords, connection strings, cloud credentials, state files.

- A finding blocks the commit. No exceptions.
- Use the project's scanner agent or tool when one exists. Otherwise grep the staged diff for known secret patterns.

## 3. Stage

- Stage explicit paths only. MUST NOT use `git add -A` or `git add .`.
- MUST NOT commit environment files, state files, or secret-bearing tfvars.

## 4. Conventional commit

Format: `type(scope): imperative summary (#issue)`

- Types: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `chore`, `build`, `ci`, `style`, `revert`.
- Imperative mood: "add", "fix", "remove" — not "added", "adds".
- Subject SHOULD stay at or under 50 characters; hard cap 72. No trailing period.
- Body only when the why is not obvious: non-obvious rationale, breaking changes, migration notes. Wrap at 72.
- Reference the issue in the subject. Close it with a `Closes #N` trailer when the change completes it.
- MUST NOT include AI attribution, "This commit does X", or restated file names.
- Always include a body for: breaking changes, security fixes, data migrations, reverts.

## 5. Commit, push

- Git operations are separate calls. MUST NOT chain git commands with `&&`.
- Push immediately after committing.
- MUST NOT skip hooks (`--no-verify`), force-push a default branch, or amend after a hook failure — fix and create a new commit.
- MUST NOT change git config.

## 6. Pull request

- Open the PR against the default branch. Reference the driving issue in the body.
- The PR body states what changed, why, deviations from the plan, and verification commands.
- Request the project's required reviewers (peer agent, Copilot, humans) per project convention.

## 7. Review loop

Review comments are one line per finding: `file:L<line>: <severity>: <problem>. <fix>.`

- Severity: `bug` (broken behavior), `risk` (works but fragile), `nit` (author may ignore), `q` (genuine question).
- Cite the checklist slug or project rubric bullet each finding invokes.
- Keep exact line numbers and backticked symbols. State the concrete fix, not "consider refactoring".
- Security findings and architectural disagreements get full paragraphs, not one-liners.
- Authors MUST triage every reviewer finding with evidence — fix it or rebut it. No silent dismissals.
- Merge only when required reviews and CI are green.
