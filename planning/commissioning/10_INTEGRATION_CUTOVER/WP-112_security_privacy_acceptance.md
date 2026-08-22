# WP-112 — Security and Privacy Acceptance Package

## Package card

| Field | Value |
|---|---|
| Work package | `WP-112` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Independent Red Team / Privacy Reviewer |
| Hard dependencies | WP-060, WP-109 |
| Related gates | Commissioning |
| Related controls | CTL-SEC-01..05, CTL-OBS-02 |
| Related acceptance scenarios | ACC-15..18, ACC-24..26, ACC-32, ACC-37, ACC-40 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Sandbox escape, egress exfiltration, unsigned images, D3 routing, policy rollback and expiry, forged approval, secrets in traces, evaluation contamination and audit tampering all close fail-closed.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md), [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-112-T01 | Prepare the security acceptance fixtures and attack identities | Implementation owner | Commit / configuration / record reference |
| WP-112-T02 | Run the security paths behind ACC-15–18, 24–26, 32, 37 and 40 | Implementation owner | Commit / configuration / record reference |
| WP-112-T03 | Verify the deny, contain, lease-revoke, incident and audit assertions | Implementation owner | Commit / configuration / record reference |
| WP-112-T04 | Review the forensic artifacts and the alert/runbook response | Implementation owner | Commit / configuration / record reference |
| WP-112-T05 | Correct and retest every critical finding | Implementation owner | Commit / configuration / record reference |
| WP-112-T06 | Sign the security acceptance statement | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Security scenario results`
- `Red-team report`
- `Forensic evidence`
- `Security acceptance statement`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- ACC-15, 16, 17, 18, 24, 25, 26, 32, 37 and 40
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every critical attack is denied or contained **and** produces audit evidence.
- [ ] D3/D4 violations = 0.
- [ ] Unsigned artifacts in production = 0.
- [ ] Open critical and high security findings = 0.
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

A failure blocks production access and cutover; compromised credentials and artifacts are revoked immediately.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
