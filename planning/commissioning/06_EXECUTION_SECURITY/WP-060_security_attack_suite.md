# WP-060 — Agentic Security Attack Suite and Red-Team Acceptance

## Package card

| Field | Value |
|---|---|
| Work package | `WP-060` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Red Team Lead |
| Independent verifier | Safety Owner / Commissioning Board |
| Hard dependencies | WP-049, WP-050, WP-051, WP-052, WP-053, WP-054, WP-055, WP-056, WP-057, WP-058, WP-059 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-SEC-01..05, CTL-OBS-02 |
| Related acceptance scenarios | ACC-05, ACC-06, ACC-09, ACC-15, ACC-16, ACC-17, ACC-18, ACC-25, ACC-32, ACC-37 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Prompt injection, tool misuse, secret exfiltration, memory poisoning, sandbox escape, supply-chain, data poisoning, reviewer manipulation, cost denial and audit tampering attacks become an automated and manual suite that runs on a schedule.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-051 — Four Trust Zones and Network Segmentation](../06_EXECUTION_SECURITY/WP-051_trust_zone_network.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-057 — Default-Deny Egress Proxy, DLP and Allowlist](../06_EXECUTION_SECURITY/WP-057_egress_proxy_dlp.md), [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-060-T01 | Derive the attack cases from the threat-to-control map | Implementation owner | Commit / configuration / record reference |
| WP-060-T02 | Prepare canary secrets and malicious PDF, repository and tool fixtures | Implementation owner | Commit / configuration / record reference |
| WP-060-T03 | Write confused-deputy and target-scope tests against the Tool Broker | Implementation owner | Commit / configuration / record reference |
| WP-060-T04 | Add sandbox, kernel, network, cost and audit attacks | Implementation owner | Commit / configuration / record reference |
| WP-060-T05 | Define the expected deny / contain / detect / respond evidence for each case | Implementation owner | Commit / configuration / record reference |
| WP-060-T06 | Bind the regression schedule and the finding pipeline | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Agentic attack suite`
- `Malicious fixture corpus`
- `Red-team report template`
- `Security regression schedule`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- The attack paths behind ACC-05, 06, 09, 15, 16, 17, 18, 25, 32 and 37
- Audit tampering and hash verification
- Memory poisoning attempting to overwrite a human-authored zone
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every critical attack is denied or contained **and** produces audit evidence.
- [ ] Open critical findings = 0.
- [ ] False positives are corrected without weakening the control that produced them.
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

A failed suite blocks deployment and cutover; corrections are made only against validated findings, after which the full affected regression is rerun.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
