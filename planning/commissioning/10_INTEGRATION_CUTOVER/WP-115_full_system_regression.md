# WP-115 — Full System Regression and Commissioning Dossier

## Package card

| Field | Value |
|---|---|
| Work package | `WP-115` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Assurance Lead |
| Independent verifier | Commissioning Board |
| Hard dependencies | WP-110, WP-111, WP-112, WP-113, WP-114 |
| Related gates | Commissioning |
| Related controls | All controls |
| Related acceptance scenarios | every scenario whose `Acceptance phase` is `PRE_GO_LIVE` (ACC-01 – ACC-51 excluding the Day-2 set) |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

The `PRE_GO_LIVE` scenarios plus the contract, replay, attack, restore and capacity evidence are consolidated for one release candidate into a single signed Commissioning Dossier.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-110 — Research and Literature Acceptance Package](../10_INTEGRATION_CUTOVER/WP-110_research_acceptance.md), [WP-111 — Reliability, Event and FinOps Acceptance Package](../10_INTEGRATION_CUTOVER/WP-111_reliability_finops_acceptance.md), [WP-112 — Security and Privacy Acceptance Package](../10_INTEGRATION_CUTOVER/WP-112_security_privacy_acceptance.md), [WP-113 — Evidence, Reproduction and Publication Acceptance Package](../10_INTEGRATION_CUTOVER/WP-113_evidence_repro_acceptance.md), [WP-114 — Operations, DR and Restore Acceptance Package](../10_INTEGRATION_CUTOVER/WP-114_operations_dr_acceptance.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-115-T01 | Freeze the RC digest and every bundle version | Implementation owner | Commit / configuration / record reference |
| WP-115-T02 | Verify that every `PRE_GO_LIVE` scenario result comes from the same RC | Implementation owner | Commit / configuration / record reference |
| WP-115-T03 | Consolidate the contract, replay, security, reproduction, DR, cost and trace evidence manifests | Implementation owner | Commit / configuration / record reference |
| WP-115-T04 | Sweep for open findings, risks, exceptions and expiries | Implementation owner | Commit / configuration / record reference |
| WP-115-T05 | Produce the KPI, SLO, capacity and owner readiness scorecard | Implementation owner | Commit / configuration / record reference |
| WP-115-T06 | Hold the independent board review and record the BLOCKED/READY verdict | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Commissioning Dossier`
- `RC evidence manifest`
- `Finding/risk register snapshot`
- `Readiness scorecard`
- `Board verdict`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Consistency of the RC and bundle versions
- Evidence link, hash and signature verification
- An open-critical query returning zero
- An expired exception and profile scan
- Completeness of all scenarios
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every `PRE_GO_LIVE` scenario PASSes.
- [ ] Open critical findings = 0.
- [ ] Required high findings = 0, or an explicitly permitted residual risk.
- [ ] The dossier is independently verified and signed.
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

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

Without a READY verdict the RC is not promoted; a correction produces a new RC digest and the affected plus baseline regression is rerun.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
