# Delivery Loop

Run after the validator accepts. Delivery is part of the mission. One agent runs the whole loop; the reviewers are the validator (pre-commit) and Copilot (on the PR).

## 1. Docs mission

Change alters behavior, structure, interfaces, or workflow: dispatch a docs worker before committing. Non-trivial docs pass the validator gate. MUST NOT document unbuilt features. Planned and live stay visually distinct.

## 2. Secret scan

Scan the staged diff: keys, tokens, passwords, connection strings, cloud credentials, state files. A finding blocks the commit. No exceptions. Use the project scanner agent when one exists; otherwise grep the staged diff.

## 3. Stage

Explicit paths only. MUST NOT use `git add -A` or `git add .`. MUST NOT commit env files, state files, or secret-bearing tfvars.

## 4. Conventional commit

`type(scope): imperative summary (#issue)` — feat|fix|refactor|perf|docs|test|chore|build|ci|style|revert.

- Imperative mood. Subject SHOULD stay at or under 50 characters, hard cap 72, no trailing period.
- Body only when the why is not obvious. Wrap at 72. `Closes #N` trailer when the change completes the issue.
- MUST NOT include AI attribution or "This commit does X".
- Body REQUIRED for: breaking changes, security fixes, migrations, reverts.

## 5. Commit, push

Git operations are separate calls. MUST NOT chain git commands with `&&`. Push right after committing. MUST NOT skip hooks, force-push a default branch, amend after a hook failure (new commit instead), or change git config.

## 6. Pull request

Open against the default branch. Reference the driving issue. Body: what, why, plan deviations, verification commands.

Request Copilot code review on every PR: `gh pr edit <num> --add-reviewer Copilot`. The review posts under `copilot-pull-request-reviewer`. Add project-required human reviewers when the project names them.

## 7. Review loop — same PR, to green, then merge

1. Wait for the Copilot review. MUST NOT merge before it posts.
2. Triage EVERY finding with evidence: fix it, or rebut it in a PR comment citing code or tests. No silent dismissals.
3. Push fixes to the same PR. Re-request Copilot when the diff changed materially.
4. Merge only when findings are resolved, required reviews are done, and CI is green.

Comment format: `file:L<line>: <severity>: <problem>. <fix>.` Severity: bug | risk | nit | q. Cite the checklist slug or project rubric bullet. Security findings and architecture disagreements get full paragraphs, not one-liners.
