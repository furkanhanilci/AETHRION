# WP-139 — Evidence Timestamping and Independent Seal

## Package card

| Field | Value |
|---|---|
| Work package | `WP-139` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **S** — small; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Data Platform Lead |
| Independent verifier | Research Integrity Officer |
| Hard dependencies | WP-014 (Artifact manifest), WP-026 (Object store WORM) |
| Related gates | G2, G5, G9 |
| Related controls | CTL-DAT-03, CTL-SUP-01 |
| Related acceptance scenarios | ACC-23, ACC-40 |
| Related skill | `verification-before-completion` |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

It becomes provable that a given `EvidenceManifest` existed at a given time —
**without trusting your system**.

This is the infrastructure-free part of the WP-000 (Interim Evidence Policy)
problem: time evidence can be produced before signed manifests and an immutable
store exist.

| Method | Trusted third party | Cost | Note |
|---|---|---|---|
| **OpenTimestamps** | **not required** | free | Only a hash is sent; the file never leaves the machine. Anchored to Bitcoin; anyone can verify independently |
| **RFC 3161 TSA** | required (the TSA) | free options exist | If the TSA key expires, additional evidence is needed |
| Sigstore / cosign | Sigstore infrastructure | free | Used together with WP-027/059 |
| Signed Git tag | the key holder | free | Weak: the clock can be manipulated |

> **Recommendation:** OpenTimestamps primary, RFC 3161 secondary. Together they
> give a seal that is both third-party-independent and quickly verifiable.

**Critical use:** when the `AnalysisPlanManifest` is locked at G2 its hash is
timestamped. That makes the pre-registration discipline's claim — "the plan
existed before the result" — **externally verifiable**.

## Out of scope

- The manifest content itself (WP-014)
- Signing infrastructure (WP-027, WP-059)

## Preconditions — Definition of Ready

- Dependencies accepted: WP-014 (Artifact manifest), WP-026 (Object store WORM)
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

## Implementation tasks

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-139-T01 | Submit the `EvidenceManifest` hash to OpenTimestamps | An `.ots` proof file is produced |
| WP-139-T02 | Secondary RFC 3161 TSA stamp | The `.tsr` response is stored |
| WP-139-T03 | Bind the stamp files to the manifest and the object store | An unstamped manifest is not accepted |
| WP-139-T04 | Verification command and runbook | A third party can verify independently |
| WP-139-T05 | Automatic stamping when the G2 analysis plan is locked | Plan lock = stamping moment |
| WP-139-T06 | Track stamp latency and maturation | Pending stamps are monitored to completion |

## Mandatory deliverables

- The OpenTimestamps and RFC 3161 stamping flow
- Storage of the `.ots` / `.tsr` proof files
- The verification command and runbook
- The G2 automatic stamping integration

## Test and verification plan

- **Independent verification:** the stamp verifies on a third machine, without the framework
- **Pre-registration proof:** the plan stamp precedes the result artifact's stamp
- **Unstamped manifest:** rejected (negative test)
- **Maturation:** a pending OpenTimestamps proof is tracked and completed
- **Clock manipulation:** changing the local clock does not change the stamp

## Acceptance criteria

- [ ] The existence time of an `EvidenceManifest` is verifiable without trusting the framework
- [ ] The `AnalysisPlanManifest` lock is stamped automatically
- [ ] Stamp files are stored alongside the manifest and the object store
- [ ] The verification runbook is executable by a third party
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Risks and control points

- An OpenTimestamps proof can take several hours to mature; the RFC 3161 stamp bridges that interval
- A stamp proves **existence time** only, never the correctness of the content
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

If stamping is disabled, new manifests are left unstamped while existing stamps
remain valid. Retroactive stamping is **impossible** — that is the whole meaning
of a timestamp.

## Handoff into downstream packages

WP-000 (Interim Evidence Policy) uses this mechanism as the time evidence for
the interim evidence store. Together with WP-138, it provides two independent
witnesses.
