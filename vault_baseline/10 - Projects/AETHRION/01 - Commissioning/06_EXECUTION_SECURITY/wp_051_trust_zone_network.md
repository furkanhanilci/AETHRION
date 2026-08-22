# WP-051 — Four Trust Zones and Network Segmentation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-051` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Security Architecture Lead |
| Independent verifier | Independent Security Reviewer / SRE |
| Hard dependencies | WP-006, WP-010, WP-021 |
| Related gates | Platform |
| Related controls | CTL-SEC-01, CTL-SEC-02 |
| Related acceptance scenarios | ACC-05, ACC-16 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Zone 0 governance, Zone 1 control plane, Zone 2 execution and Zone 3 untrusted content are separated by explicit identity, default-deny networking and audited gateways.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/wp_010_adr_baseline.md), [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/wp_021_environment_account_network_baseline.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-051-T01 | Produce the zone, asset and data-flow inventory | Implementation owner | Commit / configuration / record reference |
| WP-051-T02 | Apply NetworkPolicies, firewalls and security groups through IaC | Implementation owner | Commit / configuration / record reference |
| WP-051-T03 | Define the control↔execution and quarantine↔parser gateways | Implementation owner | Commit / configuration / record reference |
| WP-051-T04 | Establish default-deny ingress/egress and DNS policy | Implementation owner | Commit / configuration / record reference |
| WP-051-T05 | Separate the admin, audit and export paths | Implementation owner | Commit / configuration / record reference |
| WP-051-T06 | Write the trust-boundary threat tests | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Trust zone diagram/data flows`
- `Network IaC`
- `Boundary policy`
- `Threat-test suite`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial of direct Zone 3 → Zone 1 access
- Denial of unknown egress from execution
- Denial of execution credentials against the control database
- A read-only audit export path
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No zone transition occurs without identity, policy, schema validation and audit.
- [ ] Untrusted content never reaches a control prompt or command channel.
- [ ] Network drift raises an alert.
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

- A control not exercised by a negative test is an assumption.
- Default-allow egress anywhere in the chain nullifies every other isolation control.
- Sandbox escape is tested by attempting it, not by reading the configuration.

## Rollback / compensation

A wrong network release is reverted through GitOps rollback; a fail-closed outage is preferred over an unsafe transition.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
