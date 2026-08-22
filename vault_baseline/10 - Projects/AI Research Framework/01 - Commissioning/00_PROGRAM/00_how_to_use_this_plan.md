# Using the Plan and the Execution Protocol

## Purpose

This file defines how 140 work packages are managed as a single programme. The
packages are deliberately small, but a small package does not mean an
independent architectural decision. Every package realises one invariant of the
target architecture and is bound to the dependency graph.

## Core execution rules

1. Every package has one `Accountable Owner`, one `Responsible Implementer` and
   a `Verifier` separate from the producer.
2. A package becomes `READY` only when the acceptance evidence of its
   prerequisites is accessible — not merely when those packages are "finished".
3. Before implementation starts, the base revision, environment, policy bundle
   and schema version are recorded.
4. Scope expansion is never quietly folded into the same package; a change
   request or a new package is opened.
5. Code, policy, schema and IaC changes are tracked through Git; runtime results
   are tracked through immutable artifacts.
6. External system writes are not turned into manual automation while the Tool
   Broker contract is unavailable.
7. Where a temporary manual step is unavoidable, a `TemporaryControlRecord` with
   a name, an owner, an expiry date and a removal criterion is required.
8. A dependent package is not treated as production-ready until the package it
   depends on has passed its acceptance test.
9. A package cannot become `ACCEPTED` while a critical finding is open. A waiver
   is possible only outside the non-waivable list.
10. The end of a wave is measured by defined integration evidence, not by a
    count of delivered features.

## Weekly programme rhythm

| Session | Input | Output |
|---|---|---|
| Package refinement | Backlog, dependencies, risks | Packages meeting DoR, with updated estimates |
| Architecture/contract board | ADRs, schema deltas, interface impact | Approval, revision, or a new decision requirement |
| Assurance triage | Test, review and reproducer findings | Dispositions and correction packets |
| Integration checkpoint | Vertical slice results | Blocked dependencies and scenario status |
| Programme review | KPIs, budget, risk, capacity | Stop/pivot/continue and owner decisions |

## Package artifact directory

Each package produces the following logical directory while work is in progress:

```text
delivery/WP-xxx/
  package-state.yaml
  design/
  implementation/
  tests/
  evidence/
    evidence-manifest.json
    evidence-manifest.json.ots     # external time anchor (WP-139)
    verification-summary.json
  reviews/
  decisions/
  handoff/
```

These plan files do not replace the implementation repository. The repository
structure is settled in WP-022.

## Non-waivable blockers

None of the following can be passed by policy exception:

- The identity of a decision maker or an actor cannot be verified.
- D3/D4 data could be routed incorrectly.
- Critical producer/reviewer/reproducer independence cannot be achieved.
- A critical claim has no locator or representation hash.
- An artifact can be overwritten, or the provenance chain is broken.
- An unsigned or mutable execution image is accepted.
- A T4/T5 effect operation can bypass the required human decision.
- A Temporal replay or idempotency test shows critical state loss or a double
  effect.
- Clean-room results fall outside the defined tolerance and the root cause is
  unresolved.
- A restore rehearsal fails its RPO/RTO or integrity queries.
- An open critical security, assurance or data finding exists.

## Updating the plan

The plan is a living implementation artifact. A package identifier is never
reused. When scope changes, the file revision and change record are updated;
the prior conditions of an accepted package are never deleted. An update that
changes a target-architecture invariant requires an ADR and Architecture
Decision Owner approval first.
