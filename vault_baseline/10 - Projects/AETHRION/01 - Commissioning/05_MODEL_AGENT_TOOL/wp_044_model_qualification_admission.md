# WP-044 — Model Qualification and Admission Pipeline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-044` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Eval Office |
| Independent verifier | Admission Board / Safety / FinOps |
| Hard dependencies | WP-041, WP-042, WP-043 |
| Related gates | G1,G5,G10 |
| Related controls | CTL-MOD-01, CTL-MOD-02 |
| Related acceptance scenarios | ACC-10, ACC-36, ACC-37 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

A new or changed model profile is admitted to a role only on evidence from shadow running, quality, safety, data handling, availability and quality-adjusted cost.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-043 — Role-Based Model Evaluation and Golden Set Management](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-044-T01 | Resolve the qualification request against an immutable model snapshot | Implementation owner | Commit / configuration / record reference |
| WP-044-T02 | Run the role evaluation, safety, latency and cost batches | Implementation owner | Commit / configuration / record reference |
| WP-044-T03 | Compute the baseline comparison and the incremental value | Implementation owner | Commit / configuration / record reference |
| WP-044-T04 | Verify the data and provider contract and its retention terms | Implementation owner | Commit / configuration / record reference |
| WP-044-T05 | Write the Admission Board decision workflow and the profile expiry | Implementation owner | Commit / configuration / record reference |
| WP-044-T06 | Bind the regression/drift schedule to the revocation path | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Qualification pipeline`
- `Admission dossier`
- `CapabilityProfile update`
- `Regression schedule`
- `Ejection procedure`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Passing and failing candidate fixtures
- A silent provider snapshot change
- An availability/SLO failure
- A data-policy failure
- The human triage cost threshold
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Admission rests on role evaluation, not on model popularity or vendor claims.
- [ ] An expired or failed profile cannot be routed to.
- [ ] Qualification evidence carries a reproducible run manifest.
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

A failed admission leaves the profile in `SHADOW` or `SUSPENDED`; existing admitted profiles are unaffected.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
