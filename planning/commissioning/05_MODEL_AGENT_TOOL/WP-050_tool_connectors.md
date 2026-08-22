# WP-050 — Initial Tool Connector Package

## Package card

| Field | Value |
|---|---|
| Work package | `WP-050` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Tool Platform Lead |
| Independent verifier | Security / Connector Owners |
| Hard dependencies | WP-049 |
| Related gates | G3,G5,G9 |
| Related controls | CTL-LIT-03, CTL-OPS-01, CTL-SEC-01 |
| Related acceptance scenarios | ACC-01, ACC-02, ACC-05, ACC-35 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Web, Crossref, Zotero, Git, object store, MLflow and the controlled notification tools run as least-privilege connectors that conform to the broker contract.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-050-T01 | Implement the web read/search connector with its allowlist | Implementation owner | Commit / configuration / record reference |
| WP-050-T02 | Write the Crossref and status-lookup connector | Implementation owner | Commit / configuration / record reference |
| WP-050-T03 | Separate the Zotero read, candidate and update-proposal connectors | Implementation owner | Commit / configuration / record reference |
| WP-050-T04 | Add the Git branch/worktree connector | Implementation owner | Commit / configuration / record reference |
| WP-050-T05 | Build the object store signed-upload and reference connector | Implementation owner | Commit / configuration / record reference |
| WP-050-T06 | Bind the MLflow run and metric connector | Implementation owner | Commit / configuration / record reference |
| WP-050-T07 | Write a target resolver and compensation path for every connector | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Versioned connectors`
- `Connector permission profiles`
- `Connector contract tests`
- `Compensation/reconciliation playbooks`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Quarantine of a web injection attempt
- Denial of any write to the personal Zotero library
- Denial of a write to a protected Git branch
- Object hash mismatch detection
- A connector timeout after the external call actually succeeded
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Each connector operates only within its declared T class and target scope.
- [ ] Connector output is labelled as untrusted data.
- [ ] Every external write is either idempotent or reconcilable.
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

- A model alias is not a pinned identity; results obtained under an alias are not reproducible.
- An agent holding a credential defeats the entire broker design.
- Fallback routes are the least tested and most consequential path in this workstream.

## Rollback / compensation

A connector is disabled by feature flag; uncertain writes go to the reconciliation queue and reads fall back to retry with backoff.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
