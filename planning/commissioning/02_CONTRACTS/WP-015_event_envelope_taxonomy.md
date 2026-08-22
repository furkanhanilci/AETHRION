# WP-015 — Event Envelope, Subject and Schema Taxonomy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-015` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Event Platform Lead |
| Independent verifier | Control Plane Lead / Security |
| Hard dependencies | WP-011, WP-012, WP-014 |
| Related gates | Platform |
| Related controls | CTL-OPS-01, CTL-OBS-01 |
| Related acceptance scenarios | ACC-12, ACC-34 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

For events published **after** the canonical commit, the identity, causation, actor, data class, payload reference, version and retention contract are completed. Events describe what already happened; they never decide what happens next.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/WP-012_canonical_field_authority.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-015-T01 | Fix the `EventEnvelope` fields | Implementation owner | Commit / configuration / record reference |
| WP-015-T02 | Establish the workflow, artifact, evidence, security, cost and telemetry subject taxonomy | Implementation owner | Commit / configuration / record reference |
| WP-015-T03 | Write the rule separating an inline payload from an encrypted reference | Implementation owner | Commit / configuration / record reference |
| WP-015-T04 | Add the at-least-once delivery and idempotent-consumer expectation | Implementation owner | Commit / configuration / record reference |
| WP-015-T05 | Define schema evolution and `replay_mode` semantics | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `EventEnvelope schema`
- `Event Catalog seed`
- `Subject/retention table`
- `Consumer contract`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A duplicate-event fixture
- A negative test writing a D3 payload into the event body
- A major-schema replay-compatibility test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every event carries event, causation, correlation and idempotency identifiers.
- [ ] No NATS event can change gate state on its own.
- [ ] No PII, D3 or D4 payload enters an event body.
- [ ] All mandatory tests passed **on the same target revision**.
- [ ] No open Critical or High findings; no non-waivable blocker remains.
- [ ] The independent verifier has accepted the evidence package.
- [ ] Rollback/compensation behaviour has been exercised and audited.
- [ ] The related dashboard, alert, audit query or integrity query has produced working evidence.

## Acceptance evidence package

- Test results captured on the same target revision/digest
- An `EvidenceManifest` recording the environment, schema, policy and dependency versions
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The rollback/compensation trial and its result reference
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- If a contract or canonical ownership question is unresolved, implementation **stops** and the question escalates to the Architecture Board.
- Identity, data routing, artifact integrity, independence and critical evidence problems **cannot** be passed by waiver.
- If a temporary manual control is required, its owner, scope, expiry, compensating control and removal package are recorded.
- A "package complete" statement is **not** acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

### Workstream-specific hazards

- A contract that has no consumer has never been tested, only reviewed.
- Optional fields become mandatory in practice; mark real optionality explicitly.
- Two surfaces holding the same field is a canonical-ownership defect, not a sync problem.

## Rollback / compensation

An incompatible event is routed to the DLQ; producer and consumer stay on the old subject and migrate through an adapter.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
