# WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall

## Package card

| Field | Value |
|---|---|
| Work package | `WP-058` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Content Security Lead |
| Independent verifier | Red Team / Knowledge Lead |
| Hard dependencies | WP-014, WP-017, WP-026, WP-049, WP-050, WP-051, WP-054, WP-056, WP-057 |
| Related gates | G3,G5 |
| Related controls | CTL-SEC-01, CTL-LIT-01 |
| Related acceptance scenarios | ACC-05 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Web, PDF, repository and tool output passes through quarantine, malware/MIME/licence/size scanning, isolated parsing, instruction tagging and read-only extraction — with no active content ever executed.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/wp_050_tool_connectors.md), [WP-051 — Four Trust Zones and Network Segmentation](../06_EXECUTION_SECURITY/wp_051_trust_zone_network.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/wp_054_gvisor_sandbox.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md), [WP-057 — Default-Deny Egress Proxy, DLP and Allowlist](../06_EXECUTION_SECURITY/wp_057_egress_proxy_dlp.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-058-T01 | Establish the quarantine bucket and the ingest gateway | Implementation owner | Commit / configuration / record reference |
| WP-058-T02 | Apply MIME, malware, archive-bomb, size and licence scanning | Implementation owner | Commit / configuration / record reference |
| WP-058-T03 | Run the PDF/HTML/OCR parser inside an isolated cell | Implementation owner | Commit / configuration / record reference |
| WP-058-T04 | Separate the text, metadata, link, script and instruction channels | Implementation owner | Commit / configuration / record reference |
| WP-058-T05 | Tag instruction-like segments as untrusted quoted data | Implementation owner | Commit / configuration / record reference |
| WP-058-T06 | Restrict the extraction tool profile to T0/T1 read-only | Implementation owner | Commit / configuration / record reference |
| WP-058-T07 | Add security events and quarantine disposition | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Content firewall`
- `Parser workers`
- `ContentSafetyRecord`
- `Injection detector`
- `Quarantine UI/API`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A PDF carrying a tool-command injection
- Malware and archive bombs
- Parser crash containment
- Denial of write and tool access from extraction
- Curator disposition of a false positive
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] External content can never become a workflow command.
- [ ] Extraction receives no secret, no write access and no unrestricted network.
- [ ] Every span carries the source representation hash and the parser version.
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

Suspicious content stays in quarantine; the parser or detector is rolled back and the content is reprocessed as a new version.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
