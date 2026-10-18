# Coding Checklist

Orchestrator selects sections. Core is always on. Worker reports exceptions only.

## Section selection

| Task type | Sections |
|---|---|
| New code or refactor | core, existing-code, readability, errors, tests, design |
| Debugging | core, errors, bugs, tests |
| Code review | core, readability, simplification, errors, tests, design |
| Pre-commit cleanup | core, readability, simplification, git |
| Release | core, git, release |
| Infrastructure (Terraform) | core, terraform, git |
| Full pass | all sections, only when explicitly requested |

## Rules

- Every item in a selected section MUST hold unless the worker lists it.
- Report exceptions only. List `fail` (slug + evidence) and `na` (slug + reason). An unlisted item is an asserted pass. DO NOT list passes.
- `fail` blocks acceptance. Fix and re-verify, or report the blocker with evidence.
- `na` MUST carry a one-line reason the code supports. No reason, or a contradicted reason, is a rejection.
- The validator checks every `fail` and `na`, then core and the highest-risk selected items against the diff. A contradicted implicit pass is a rejection.
- Cite slug IDs in findings and reviews.

## Core

- [ ] `core/build-runs` Build, tests, or run succeed, or the exact blocker is recorded.
- [ ] `core/follow-conventions` Match surrounding conventions; read neighbors before adding a helper, dependency, or pattern.
- [ ] `core/registry-resolved-versions` Resolve every new or changed dependency version against the live package registry; never write a version from memory.
- [ ] `core/smallest-change` Make the smallest change that meets the goal: write less, build nothing not yet needed, no scope expansion.
- [ ] `core/no-leftovers` Leave no dead code, commented-out code, debug prints, or probes.
- [ ] `core/names-reveal-intent` Names reveal intent and do not lie about type or behavior. see examples
- [ ] `core/comments-why` Comments explain why, not what.
- [ ] `core/check-every-return` Handle every error path and check every return value, rejection, nil, and failed status. see examples
- [ ] `core/no-swallowed-exceptions` No swallowed exceptions. Errors keep context and fail loudly with actionable messages. see examples
- [ ] `core/boundary-inputs` Handle empty, missing, malformed, repeated, and out-of-order boundary inputs.
- [ ] `core/security-closed` Security-sensitive failures fail closed; no secrets in code, logs, or output.
- [ ] `core/root-cause` Fix the root cause, not the symptom; search for the same pattern elsewhere. see examples
- [ ] `core/tests-cover` Tests cover success, failure, and boundary; a regression test fails before the fix when practical.
- [ ] `core/no-implementation-mirror` No tests that only mirror the implementation. see examples
- [ ] `core/reviewable-diff` One intent, no unrelated churn, formatting separate from behavior.
- [ ] `core/verify-acceptance` Verify acceptance criteria through the real entry point; state untested risk plainly.

## Existing-code

- [ ] `existing-code/trace-path` Trace the touched path's inputs, outputs, side effects, and ownership boundaries before editing.
- [ ] `existing-code/check-tests-first` Reuse existing tests, fixtures, scripts, and CI commands before adding new ones.
- [ ] `existing-code/generated-boundaries` Identify generated, vendored, and externally owned files before editing.
- [ ] `existing-code/wrap-before-refactor` Add tests around messy code before refactoring it.

## Readability

- [ ] `readability/clarity-over-brevity` Follow the language's naming conventions; favor descriptive names over cryptic ones and drop redundancy the context implies.
- [ ] `readability/layout-prevents-bugs` Layout never misleads control flow; formatter and linter pass.
- [ ] `readability/short-functions` Short focused functions; split distinct operations into named functions.

## Simplification

- [ ] `simplification/direct-expressions` Return boolean expressions directly; inline trivial branches and single-use temps.
- [ ] `simplification/dry-with-care` Factor duplication into one place only when the coupling cost is worth it. see examples
- [ ] `simplification/reduce-indirection` Cut needless getters, wrappers, and pass-through layers.

## Errors

- [ ] `errors/all-call-sites` Expose all failure modes through the interface and handle them at every call site.
- [ ] `errors/resource-cleanup` Cleanup, rollback, and partial-write behavior is explicit when operations can fail halfway.
- [ ] `errors/graceful-shutdown` Plan halt, cancel, timeout, and cleanup from the start. see examples
- [ ] `errors/concurrency-paths` Check races, ordering, shared state, and lifetime in async or threaded code.
- [ ] `errors/no-implicit-assumptions` Make assumptions explicit through types, asserts, or validation. see examples

## Bugs

- [ ] `bugs/reproduce-first` Reproduce the bug or state why local reproduction is unavailable.
- [ ] `bugs/minimal-case` Reduce the failure to the smallest input, state, or path.
- [ ] `bugs/one-hypothesis` Test one falsifiable hypothesis at a time. see examples
- [ ] `bugs/bisect-history` Narrow the search by halving; bisect history for regressions. see examples
- [ ] `bugs/suspect-list` For intermittent failures, check serialization, time, concurrency, filesystem, network, permissions, and shared mutable state.

## Tests

- [ ] `tests/right-level` Test at the smallest scope that exercises the behavior; add integration tests when the change crosses boundaries.
- [ ] `tests/one-thing-per-test` One fact per test; setup, action, and assertion visibly separate; spec-style names.
- [ ] `tests/isolate-boundaries` Inject collaborators, not globals; use doubles only where they clarify a boundary.

## Design

- [ ] `design/cohesion` One responsibility per component; no god objects, no entity smeared across objects; behavior lives where it will change.
- [ ] `design/loose-coupling` Minimize coupling; break cycles; each component is constructible in isolation. see examples
- [ ] `design/api-prevents-misuse` Make the wrong call and invalid states hard to write. see examples
- [ ] `design/track-tech-debt` Mark shortcuts as technical debt in the code when they enter.

## Git

- [ ] `git/everything-tracked` Every file needed to rebuild is tracked or in the documented dependency path.
- [ ] `git/exclude-artifacts` Exclude generated files, caches, secrets, and local config.
- [ ] `git/atomic-commits` Each commit is one coherent, reversible step; the message says what and why. see examples

## Release

- [ ] `release/clean-checkout` Build releases from a fresh checkout of a tagged or otherwise identified commit. see examples
- [ ] `release/repeatable-build` One-command repeatable build; record version, artifact identity, and build configuration.
- [ ] `release/final-artifact-tested` Test the packaged or deployed artifact, not only source.
- [ ] `release/release-notes` Notes state implemented, omitted, risky, and changed behavior.

## Terraform

- [ ] `terraform/plan-validated` `terraform fmt -check` and `terraform validate` pass; a plan saved with `terraform plan -out` is reviewed before apply.
- [ ] `terraform/apply-approved` Apply only the saved, reviewed plan, only after explicit user approval for it.
- [ ] `terraform/clean-replan` After apply, `terraform plan -detailed-exitcode` exits 0.
- [ ] `terraform/blast-radius` List every destroy and replace by resource address; none unexplained.
- [ ] `terraform/prevent-destroy` Stateful resources (databases, buckets, keys, state stores) carry `lifecycle { prevent_destroy = true }`.
- [ ] `terraform/import-over-recreate` Bring existing resources in with `import` blocks; never destroy and recreate them.
- [ ] `terraform/no-leftover-blocks` Delete `moved` and `removed` blocks once apply has converged.
- [ ] `terraform/one-root-per-provider` One root module per provider.
- [ ] `terraform/no-secrets-in-vars` No secrets in `*.tfvars` or variable defaults; secret variables set `sensitive = true`.
- [ ] `terraform/plans-are-secrets` Plan files, `terraform show -json`, state, and outputs are secrets: never committed, never pasted into chat, PRs, or logs.
- [ ] `terraform/least-privilege` Least-privilege IAM, no service-account keys, credentials injected via `op run`.
- [ ] `terraform/registry-versions` Provider and module versions resolve from registry.terraform.io; `.terraform.lock.hcl` is committed.
- [ ] `terraform/static-checks` `tflint` and `trivy config` pass; modules with logic carry `terraform test`.
- [ ] `terraform/rollback-plan` State the rollback path before apply.
- [ ] `terraform/cost-impact` State the cost delta of added or resized resources.
