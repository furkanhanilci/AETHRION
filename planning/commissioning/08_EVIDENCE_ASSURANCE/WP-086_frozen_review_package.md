# WP-086 — Frozen and Blind Review Package Builder

## Package card

| Field | Value |
|---|---|
| Work package | `WP-086` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Assurance Platform Lead |
| Independent verifier | Privacy/Security / Blind Reviewer |
| Hard dependencies | WP-007, WP-014, WP-018, WP-026, WP-075, WP-077, WP-080, WP-081, WP-082 |
| Related gates | G6 |
| Related controls | CTL-GOV-02, CTL-EPI-04 |
| Related acceptance scenarios | ACC-06, ACC-07 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

A reviewer receives only the immutable target, the specification or protocol, the relevant evidence, the verification summary and the rubric — with producer identity, model, trace and persuasive intermediate reasoning removed.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-086-T01 | Define review package profiles per artifact type | Implementation owner | Commit / configuration / record reference |
| WP-086-T02 | Write frozen target, hash and manifest assembly | Implementation owner | Commit / configuration / record reference |
| WP-086-T03 | Add producer identity/model/trace redaction and a leak detector | Implementation owner | Commit / configuration / record reference |
| WP-086-T04 | Apply minimum-context and relevant-excerpt selection | Implementation owner | Commit / configuration / record reference |
| WP-086-T05 | Establish package signature, access, expiry and one-way reviewer credentials | Implementation owner | Commit / configuration / record reference |
| WP-086-T06 | Write the unblinding audit and the correction delta package | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Review Package Builder`
- `Blind/redaction rules`
- `Package manifests`
- `Leak detection tests`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Producer metadata removed
- Target hash immutability
- A hidden identity-leak fixture
- Denial of unauthorised source access by a reviewer
- A correction delta producing a new package
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Review is performed against the same frozen target throughout.
- [ ] The reviewer never sees the producer's session or trace.
- [ ] If the package changes, the review is invalidated.
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

- Independence asserted in a record but not enforced by the router is decorative.
- A review that sees the producer's conclusion first is anchored, not independent.
- Reproduction that reuses the producer's environment reproduces the environment, not the result.

## Rollback / compensation

On a detected leak the review becomes `INVALIDATED` and is redone with a new reviewer and a clean package.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
