# WP-005 — Research Risk and Assurance Profile

## Package card

| Field | Value |
|---|---|
| Work package | `WP-005` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Research Director / Assurance Lead |
| Hard dependencies | WP-001, WP-002 |
| Related gates | G0,G1 |
| Related controls | CTL-GOV-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The materiality, uncertainty, exposure and safety/ethics/regulation dimensions produce an R1/R2/R3 assurance class through small decision tables rather than a combinatorial cross-product.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/WP-001_commissioning_charter.md), [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/WP-002_scope_nfr_traceability.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-005-T01 | Define the M/U/X/S dimensions with a 0–3 rubric | Implementation owner | Commit / configuration / record reference |
| WP-005-T02 | Write the max/precedence rules and the hard-promotion rules | Implementation owner | Commit / configuration / record reference |
| WP-005-T03 | Define the fail-closed effect of an `UNKNOWN` value | Implementation owner | Commit / configuration / record reference |
| WP-005-T04 | Map R1/R2/R3 onto review, literature and reproduction depth | Implementation owner | Commit / configuration / record reference |
| WP-005-T05 | Assign the decision rights for raising and lowering a risk class | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `RiskProfile schema semantics`
- `AssuranceClass decision tables`
- `Promotion rules`
- `Worked examples`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Boundary-value policy tests
- A consistency and calibration test applying the same case twice
- Negative tests for `UNKNOWN` handling and for class downgrade
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The decision tables require no cross-product enumeration.
- [ ] Identical inputs produce a deterministic class.
- [ ] R3 and hard promotion cannot be compensated by any low score on another dimension.
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

- A policy that is written but not machine-checkable is an intention, not a control.
- Role and authority documents drift silently; every change here needs a baseline bump.
- The hardest failure in this workstream is a rule that everyone agrees with and nobody can enforce.

## Rollback / compensation

A new table is evaluated in shadow mode before promotion; on failure the previous signed policy version is restored.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
