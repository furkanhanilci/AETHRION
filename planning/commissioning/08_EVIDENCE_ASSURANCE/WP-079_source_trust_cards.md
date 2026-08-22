# WP-079 — SourceTrustCard and Study Quality Assessment

## Package card

| Field | Value |
|---|---|
| Work package | `WP-079` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Methodologist |
| Independent verifier | Independent Domain/Statistician Reviewer |
| Hard dependencies | WP-005, WP-017, WP-063, WP-075, WP-076, WP-078 |
| Related gates | G3,G6,G10 |
| Related controls | CTL-EPI-02, CTL-LIT-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

A source's status, study design, sample, measurement, bias, analysis, external validity and reporting limits are held in a reasoned trust card rather than collapsed into a single score.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md), [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-079-T01 | Define rubrics and profiles per source type | Implementation owner | Commit / configuration / record reference |
| WP-079-T02 | Bind the automatic status, licence and provenance fields | Implementation owner | Commit / configuration / record reference |
| WP-079-T03 | Assess method, bias, precision and applicability as separate dimensions | Implementation owner | Commit / configuration / record reference |
| WP-079-T04 | Write the human/agent assessment and disagreement semantics | Implementation owner | Commit / configuration / record reference |
| WP-079-T05 | Add expiry, new-version and retraction impact rules | Implementation owner | Commit / configuration / record reference |
| WP-079-T06 | Prepare the calibration sample and the reviewer guide | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `SourceTrustCard engine`
- `Rubric profiles`
- `Calibration set`
- `Trust review UI contract`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A prestigious venue with a weak method not yielding high trust
- Retraction overriding every other dimension
- Reviewer calibration
- Missing data recorded as `UNKNOWN` rather than zero
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Trust is not a single authority score.
- [ ] Every card carries its rules, evidence and rationale.
- [ ] Source quality never substitutes for claim entailment or reproduction.
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

A rubric change never mutates an existing card; it produces a re-assessment queue and a new card version.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
