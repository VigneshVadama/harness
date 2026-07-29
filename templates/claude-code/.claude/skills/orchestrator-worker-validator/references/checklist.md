# Coding Checklist

The orchestrator selects sections by task type. The worker reports every item in the selected sections. The validator re-verifies.

## Section selection

| Task type | Sections |
|---|---|
| Code review | naming, presentation, simplification, errors, tests, complexity, collaboration |
| New code or refactor | existing-code, naming, presentation, errors, tests, complexity, release |
| Debugging | existing-code, errors, bugs, tests, complexity |
| Pre-commit cleanup | presentation, simplification, tests, version-control, release |
| Release or handoff | version-control, release, tests, collaboration |
| Team or process review | collaboration, mindset, version-control, release |
| Full pass | all sections, only when explicitly requested |

## Rules

- DO NOT SKIP items in selected sections. Every item gets exactly one verdict: `pass`, `fail`, or `n/a`.
- `pass` MUST cite evidence: code, test output, command output, or explicit reasoning.
- `n/a` MUST carry a one-line justification. An unjustified `n/a` is a validator rejection.
- `fail` on a required item blocks acceptance. Fix and re-verify, or report the blocker with evidence.
- Cite slug IDs in findings and reviews.
- Prefer observable evidence over taste. Tie style feedback to readability, consistency, or risk.
- DO NOT paste this master checklist into a final answer. Report verdicts in the worker result.

## Mindset

- [ ] `mindset/care` Care about the code; treat quality as a personal standard.
- [ ] `mindset/correct-not-working` Aim for demonstrably correct code, not code that merely seems to work.
- [ ] `mindset/leave-better` Leave each touched area better than you found it.
- [ ] `mindset/own-quality` Own the quality of code around you, not just your assigned task.
- [ ] `mindset/humility` Admit gaps, seek feedback, and revise decisions when evidence changes.
- [ ] `mindset/no-autopilot` Stay engaged; do not write code on autopilot.
- [ ] `mindset/avoid-clever` Avoid code cleverer than you can debug.
- [ ] `mindset/practical-improvement` When code is bad, look for practical improvements instead of blame.
- [ ] `mindset/stop-and-think` Stop and think before writing the first solution that occurs to you.
- [ ] `mindset/back-out-mistakes` Back out wrong decisions instead of hobbling forward around them.
- [ ] `mindset/sustainable-pace` Maintain a sustainable pace; exhausted work produces defects.

## Existing-code

- [ ] `existing-code/build-runs` Confirm the target can be built, tested, or run, or record the exact blocker.
- [ ] `existing-code/smallest-path` Identify the smallest code path that matters before editing.
- [ ] `existing-code/trust-code-over-docs` Trust the running code over stale documentation when they diverge.
- [ ] `existing-code/learn-by-modifying` Learn a codebase by changing it, not just reading it.
- [ ] `existing-code/follow-conventions` Match the surrounding style and idioms of the file you are editing.
- [ ] `existing-code/read-neighbors` Read neighboring code before introducing a style, helper, dependency, or pattern.
- [ ] `existing-code/trace-boundaries` Trace inputs, outputs, side effects, and ownership boundaries for the touched path.
- [ ] `existing-code/check-tests-first` Check existing tests, fixtures, scripts, and CI commands before adding new ones.
- [ ] `existing-code/low-risk-first` Start with low-risk, high-visibility changes in unfamiliar code.
- [ ] `existing-code/smoke-test-suite` Verify the test suite actually runs by observing a known failure when practical.
- [ ] `existing-code/map-architecture` Build a quick map of modules, dependencies, and data flow before changing design.
- [ ] `existing-code/generated-boundaries` Identify generated, vendored, and externally owned files before editing.
- [ ] `existing-code/wrap-before-refactor` Add tests around messy code before refactoring it.
- [ ] `existing-code/quarantine-bad-api` Hide a bad internal API behind a clean wrapper you control.
- [ ] `existing-code/verify-before-cleaning` Confirm what code does before tidying it.
- [ ] `existing-code/pick-battles` Decide deliberately whether messy code merits rewriting now.

## Naming

- [ ] `naming/reveal-intent` Names should reveal purpose, behavior, lifetime, units, and domain meaning. see examples
- [ ] `naming/no-lies` Names must not contradict the type or behavior they describe. see examples
- [ ] `naming/clarity-over-brevity` Favor descriptive names over short cryptic ones.
- [ ] `naming/exploit-context` Drop redundancy already implied by context. see examples
- [ ] `naming/language-idioms` Follow the casing and naming conventions of the language.
- [ ] `naming/accurate-shape` Pick names that match the data structure's actual shape.
- [ ] `naming/consistent-vocabulary` Use the same word for the same concept across code, tests, messages, and docs.
- [ ] `naming/audience-vocabulary` Use vocabulary that matches the domain audience, not just the implementer.

## Presentation

- [ ] `presentation/adopt-team-layout` Adopt the team's layout and avoid formatting debates during behavior work.
- [ ] `presentation/layout-prevents-bugs` Treat layout as a safety concern, not decoration. see examples
- [ ] `presentation/structure-as-prose` Group related lines into paragraphs; split distinct operations into named functions. see examples
- [ ] `presentation/important-first` Order files and classes so important or public content comes first.
- [ ] `presentation/short-functions` Prefer many short focused functions to one long function.
- [ ] `presentation/declare-at-use` Declare variables at the point of first use when the language supports it. see examples
- [ ] `presentation/comments-explain-why` Comments should explain why, not restate what. see examples
- [ ] `presentation/no-commented-out-code` Delete commented-out code; rely on version control.
- [ ] `presentation/no-vanity-formatting` Skip decorative formatting that is hard to maintain.
- [ ] `presentation/layout-for-reading` Optimize layout for reading, not for typing.
- [ ] `presentation/actionable-messages` Make errors, logs, and user-facing messages precise enough to act on.
- [ ] `presentation/separate-formatting` Keep formatting-only churn separate from behavior changes when review risk would increase.

## Simplification

- [ ] `simplification/write-less` Write less code; every line carries maintenance cost.
- [ ] `simplification/yagni` Do not write code you do not yet need.
- [ ] `simplification/kiss` Keep designs as small and simple as the requirements allow.
- [ ] `simplification/delete-dead-code` Delete dead and unreachable code with evidence. see examples
- [ ] `simplification/no-commented-code` Remove commented-out code and rely on version control for recovery.
- [ ] `simplification/remove-debug-scaffolding` Remove debug prints, temporary hooks, one-off probes, and stale generated stubs.
- [ ] `simplification/no-flappy-booleans` Return boolean expressions directly instead of wrapping them in redundant branches. see examples
- [ ] `simplification/trivial-value-branch` Use a compact expression for trivial value selection when it remains readable. see examples
- [ ] `simplification/inline-trivial-temps` Inline single-use intermediate variables that add no clarity. see examples
- [ ] `simplification/dry-with-care` Factor duplication into one place only when the coupling cost is worth it. see examples
- [ ] `simplification/prefer-libraries` Prefer proven libraries or local utilities over hand-rolled plumbing when dependency cost is justified.
- [ ] `simplification/measure-then-optimize` Write clear code first; optimize only when measurement shows it matters.
- [ ] `simplification/reduce-indirection` Cut needless layers of getters, wrappers, forwarding, and pass-through abstractions.
- [ ] `simplification/one-change-at-time` In messy code, make one observable change at a time.
- [ ] `simplification/better-touched-code` Improve touched code without expanding beyond the user's goal.

## Errors

- [ ] `errors/handle-every-error` Handle every error path; never dismiss one as unlikely.
- [ ] `errors/check-every-return` Check every return value, rejected promise, nil result, failed status, and partial return. see examples
- [ ] `errors/no-swallowed-exceptions` Do not catch exceptions just to ignore them. see examples
- [ ] `errors/preserve-context` Preserve enough context in errors for diagnosis.
- [ ] `errors/expose-failures` Expose all failure modes through the interface.
- [ ] `errors/surface-loudly` Make failures unignorable; do not log silently to a place nobody checks.
- [ ] `errors/all-call-sites` Account for failure at every call site, not just the obvious ones.
- [ ] `errors/boundary-inputs` Handle empty, missing, malformed, repeated, delayed, and out-of-order inputs at boundaries that accept them.
- [ ] `errors/resource-cleanup` Make cleanup, rollback, and partial-write behavior explicit when operations can fail halfway.
- [ ] `errors/graceful-shutdown` Plan how things halt, cancel, time out, and clean up from the start. see examples
- [ ] `errors/concurrency-paths` Check races, ordering, shared state, and object lifetime in async or threaded code.
- [ ] `errors/security-closed` Keep security-sensitive failures closed by default.
- [ ] `errors/no-implicit-assumptions` Make assumptions explicit through types, asserts, validation, or clear interfaces. see examples
- [ ] `errors/no-later-bucket` Handle unusual paths while writing the code; do not defer them to an unspecified later pass.

## Bugs

- [ ] `bugs/reproduce-first` Reproduce the bug or state exactly why local reproduction is unavailable.
- [ ] `bugs/minimal-case` Reduce the failure to the smallest input, state, or path that still fails.
- [ ] `bugs/one-hypothesis` Test one falsifiable hypothesis at a time. see examples
- [ ] `bugs/binary-chop` Narrow the search space by halving, not single-stepping. see examples
- [ ] `bugs/bisect-history` Use history or bisect to find the breaking commit when the bug is a regression.
- [ ] `bugs/assertions-and-logs` Place assertions and logs around invariants on the failure path.
- [ ] `bugs/boundary-assumptions` Check serialization, time, concurrency, filesystem, network, permissions, and user input.
- [ ] `bugs/rubber-duck` Explain the problem aloud to expose hidden assumptions.
- [ ] `bugs/fix-immediately` Fix bugs when found; do not let them accumulate.
- [ ] `bugs/check-pattern-elsewhere` After a fix, search the codebase for the same pattern.
- [ ] `bugs/root-cause-not-symptom` Fix the root cause, not the symptom. see examples
- [ ] `bugs/suspect-shared-state` Treat globals, caches, singletons, and shared mutable objects as suspects for intermittent bugs.
- [ ] `bugs/remove-probes` Remove temporary instrumentation and debugging scaffolds before finishing.

## Tests

- [ ] `tests/short-feedback-loop` Write tests at the smallest scope that exercises the behavior.
- [ ] `tests/red-green-regression` Verify a regression test fails before the fix when practical.
- [ ] `tests/multiple-levels` Cover unit, integration, and system levels when the change crosses boundaries.
- [ ] `tests/success-failure-boundary` Cover success, failure, and boundary behavior that the code explicitly handles.
- [ ] `tests/red-green-refactor` Follow the red-green-refactor cycle for new behavior.
- [ ] `tests/test-as-you-go` Write tests alongside the code, not after.
- [ ] `tests/build-runs-tests` Wire important tests into the build or CI path.
- [ ] `tests/one-thing-per-test` Keep tests short, isolated, and focused on a single fact.
- [ ] `tests/arrange-act-assert` Keep setup, action, and assertion visibly separated. see examples
- [ ] `tests/spec-style-names` Name tests as readable specifications, not method labels. see examples
- [ ] `tests/no-implementation-mirror` Avoid tests that only mirror private implementation details. see examples
- [ ] `tests/maintain-test-code` Maintain test code with the same care as production code.
- [ ] `tests/avoid-shared-state` Inject collaborators instead of relying on globals or singletons.
- [ ] `tests/test-doubles` Use stubs, fakes, and mocks to isolate units only where they clarify a boundary. see examples
- [ ] `tests/factor-for-testability` Treat hard-to-test code as a design signal.
- [ ] `tests/flake-is-signal` Treat flaky, skipped, or quarantined tests as information that needs a decision.
- [ ] `tests/untested-risk` State untested risk plainly when no meaningful test can be run.

## Complexity

- [ ] `complexity/cohesion` Give each component a single, well-defined responsibility.
- [ ] `complexity/loose-coupling` Minimize connections between components.
- [ ] `complexity/break-cycles` Break cyclic dependencies that make construction, testing, or reasoning difficult. see examples
- [ ] `complexity/avoid-god-objects` Avoid central objects that every component knows about or mutates.
- [ ] `complexity/subdivide-blobs` Subdivide large components into small, cohesive parts.
- [ ] `complexity/independently-constructible` Each component should be constructible in isolation.
- [ ] `complexity/track-tech-debt` Mark shortcuts as technical debt the moment they enter the code.
- [ ] `complexity/refactor-architecture` Treat architecture as malleable; change it with tests and small steps.
- [ ] `complexity/defer-design-yagni` Defer design decisions until the requirement is clear.
- [ ] `complexity/api-prevents-misuse` Design APIs so the wrong call is hard to write. see examples
- [ ] `complexity/consistency-over-cleverness` Prefer consistency to local cleverness across the codebase.
- [ ] `complexity/invalid-states-hard` Make invalid states hard to represent when the language and codebase make that practical.
- [ ] `complexity/no-distributed-self` Avoid smearing one logical entity across many objects without clear ownership.
- [ ] `complexity/localize-change` Put behavior where future changes to that behavior will naturally happen.
- [ ] `complexity/review-after-code` Re-check the design after implementation and remove structure the final code no longer needs.

## Version-control

- [ ] `version-control/everything-tracked` Keep every file needed to rebuild the software in version control or in the documented dependency path.
- [ ] `version-control/exclude-artifacts` Exclude generated files, IDE caches, secrets, local settings, and personal config.
- [ ] `version-control/atomic-commits` Make each commit one coherent, reversible step.
- [ ] `version-control/reviewable-diff` Keep the diff reviewable: one intent, no unrelated churn.
- [ ] `version-control/separate-tidy-and-behavior` Keep formatting changes separate from behavior changes.
- [ ] `version-control/clear-messages` Write commit messages that explain what changed and why. see examples
- [ ] `version-control/never-break-build` Build and run relevant tests before pushing or handing off.
- [ ] `version-control/branch-risky-work` Use branches for risky, long-running, or speculative work.

## Release

- [ ] `release/clean-checkout` Build releases from a fresh checkout of a tagged or otherwise identified commit. see examples
- [ ] `release/one-command-build` Prefer a repeatable one-command build, test, or package path.
- [ ] `release/tag-artifact-config` Record version, artifact identity, and relevant build configuration.
- [ ] `release/final-artifact-tested` Test the packaged or deployed artifact, not only source-level code.
- [ ] `release/freeze-discipline` During stabilization, reduce change rate and raise review rigor.
- [ ] `release/debt-recorded` Record shortcuts taken under deadline so they can be repaid intentionally.
- [ ] `release/done-defined` Verify against explicit done criteria, not vague confidence.
- [ ] `release/release-notes` Describe implemented, omitted, risky, and changed behavior clearly for testers or operators.

## Collaboration

- [ ] `collaboration/two-eyes` Require risky changes to pass at least two pairs of eyes before merge.
- [ ] `collaboration/accountable-to-peers` Make yourself accountable to peers for code quality.
- [ ] `collaboration/take-criticism-well` Receive criticism without defensiveness; give it tactfully.
- [ ] `collaboration/actionable-review` Make review comments actionable, scoped, and tied to observable risk. see examples
- [ ] `collaboration/no-code-ownership-silos` Avoid exclusive ownership silos in the codebase.
- [ ] `collaboration/test-before-handoff` Test your work before handing it to QA, reviewers, or users.
- [ ] `collaboration/accept-bug-reports` Accept fault reports professionally, not personally.
- [ ] `collaboration/qa-from-start` Involve testers and reviewers while requirements and design are still changeable.
- [ ] `collaboration/match-channel-to-message` Pick the communication channel by urgency, audience size, and need for record.
- [ ] `collaboration/audience-language` Speak in the audience's vocabulary, not internal jargon.
- [ ] `collaboration/raise-bad-news-early` Surface blockers, missed estimates, and quality concerns as soon as they are known.
- [ ] `collaboration/no-deliberate-obscurity` Do not write code only you can read for job security.
- [ ] `collaboration/handoff-context` Leave enough context for the next maintainer to continue without rerunning your thinking.
