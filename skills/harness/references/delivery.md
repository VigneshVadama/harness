# Delivery Loop

Run after the validator accepts. The validator is the default reviewer. One agent runs the loop.

Default delivery = sections 1-4 (docs check, secret scan, explicit-path stage, local conventional commit), then STOP.

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

Commit locally. Git operations are separate calls. MUST NOT chain git commands with `&&`. MUST NOT skip hooks, amend after a hook failure (new commit instead), or change git config.

## STOP gate

Sections 5-8 apply only when the user asked for that action in this task. Push, PR, merge, `terraform apply`, and deploy MUST NOT happen on the strength of this skill alone. No ask: report the local commit and stop.

## 5. Push

MUST NOT force-push a default branch.

## 6. Pull request

Open against the default branch. Title: conventional `type(scope): summary` with NO issue number — GitHub shows the PR number beside it and an issue ref there misreads. Issue refs live in commit subjects and the PR body. Body: what, why, plan deviations, verification commands, and the driving issue.

Copilot review is optional: only when the user or project asks. It posts under `copilot-pull-request-reviewer`. `gh pr edit --add-reviewer Copilot` often fails to resolve the bot; the reliable path is the GraphQL mutation:

```sh
BOT=$(gh api "users/copilot-pull-request-reviewer[bot]" --jq .node_id)
PR=$(gh pr view <num> --json id --jq .id)
gh api graphql -f query="mutation { requestReviews(input:{pullRequestId:\"$PR\", botIds:[\"$BOT\"], union:true}) { clientMutationId } }"
```

Add project-required human reviewers when the project names them.

## 7. Review loop — same PR, every thread resolved

Applies to whoever reviewed the PR (human, Copilot, or both). Merge still needs the user's ask. Do not reorder, do not skip a step:

1. Wait for the review. MUST NOT merge before it posts.
2. Triage EVERY finding in the SAME PR: fix it, or rebut it in a thread reply citing code or tests. No silent dismissals. No follow-up-issue deferrals for in-scope findings.
3. Push the fixes. Re-request the reviewer when the diff changed materially (some reviewers auto-review new pushes — check before re-requesting twice).
4. Pushed fixes mark threads outdated; rebuttals leave them open. Either way, RESOLVE every conversation (GraphQL `resolveReviewThread`). Outdated is not resolved — resolve it explicitly. A reply without resolution leaves the conversation open.
5. When the user asked for merge, merge only when: every thread resolved, required reviews done, CI green. All three. Verify thread state with a `reviewThreads` query, not by memory.

Comment format: `file:L<line>: <severity>: <problem>. <fix>.` Severity: bug | risk | nit | q. Cite the checklist slug or project rubric bullet. Security findings and architecture disagreements get full paragraphs, not one-liners.

## 8. Stacked pull requests (`gh stack`, layered changes)

Only for projects that use PR stacks and when the user asked for PRs. Use a stack when one task decomposes into ordered layers that each deserve an independent review (drift fixes, then a refactor, then a feature on top). One layer = one branch = one PR. Field notes from live use (v0.1.0, 2026-08-01):

1. `gh stack init <branch>` on a fresh branch off the default branch (bare `init` needs interactive input — always pass the branch name). `gh stack add <branch>` stacks each next layer. `gh stack submit` pushes all branches and opens the PRs as one stack.
2. `submit` creates PRs as DRAFTS with template bodies. Immediately: `gh pr ready` each one and rewrite every body (What / Verification / issue ref). An unedited template body is itself a review finding.
3. Request the code review on EVERY PR in the stack, not only the top. Each layer's reviewer sees only that layer's diff.
4. Fix findings bottom-up: commit on the owning branch, then `gh stack rebase` to propagate upward, then `gh stack push`. Interactive `gh stack modify` is unavailable in agent environments — restructure with plain git plus `rebase`.
5. Merge with `gh stack merge` only when every PR in the stack has all threads resolved and CI green — it merges bottom-up in one pass. Section 7's gate applies per PR.
6. When the user asked for apply, apply per layer before its PR merges, so plans in PR bodies read converged; post-merge, re-verify the default branch converges once. No apply ask: post the reviewed plan and stop.
