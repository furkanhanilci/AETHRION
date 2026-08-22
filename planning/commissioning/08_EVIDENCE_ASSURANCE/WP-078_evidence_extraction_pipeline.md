# WP-078 — Structured Evidence Extraction Pipeline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-078` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Lead |
| Independent verifier | Independent Evidence Auditor |
| Hard dependencies | WP-045, WP-047, WP-058, WP-063, WP-068, WP-075, WP-076 |
| Related gates | G3,G5,G6 |
| Related controls | CTL-SEC-01, CTL-EPI-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Sources that have cleared quarantine are decomposed by a read-only extractor into study design, population, intervention, outcome, estimate, limitation and counter-evidence candidates, then verified by an independent second pass.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md), [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-078-T01 | Define the domain-neutral extraction schema and its profile extensions | Implementation owner | Commit / configuration / record reference |
| WP-078-T02 | Write the chunk-, section- and table-aware extraction graph | Implementation owner | Commit / configuration / record reference |
| WP-078-T03 | Emit every field as an `EvidenceCandidate` with a locator and a quote hash | Implementation owner | Commit / configuration / record reference |
| WP-078-T04 | Add deterministic parsing, validation and missing-field checks | Implementation owner | Commit / configuration / record reference |
| WP-078-T05 | Bind independent second-pass sampling and risk-based review | Implementation owner | Commit / configuration / record reference |
| WP-078-T06 | Add correction, versioning and quality telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Extraction pipeline`
- `Extraction schemas`
- `Evidence candidate store`
- `Second-pass review queue`
- `Quality dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Field extraction against a known paper
- Table and figure locator accuracy
- A prompt injection that cannot reach a tool call
- Extraction of contradictions and stated limitations
- A second-pass disagreement
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] An extractor can never mark a claim `VERIFIED`.
- [ ] Every material field carries a source span.
- [ ] A missing or uncertain field stays `UNKNOWN` and is never invented.
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

A faulty extraction becomes `INVALIDATED` or a new version; the source representation and any human note remain untouched.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
