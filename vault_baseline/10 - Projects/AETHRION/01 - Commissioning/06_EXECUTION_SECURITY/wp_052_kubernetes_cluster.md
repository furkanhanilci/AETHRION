---
title: "WP-052 — Kubernetes Cluster and Node Pool Baseline"
aliases:
  - "WP-052"
  - "WP-052 — Kubernetes Cluster and Node Pool Baseline"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Management, service, standard execution, secure/D3+ and untrusted compute node pools are established with HA, quotas, isolation and signed workload admission."
source: "planning/commissioning/06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/06-execution-security
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g5
  - aethrion/gate/platform
  - aethrion/state/not-started
---

# WP-052 — Kubernetes Cluster and Node Pool Baseline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-052` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Infrastructure Lead |
| Independent verifier | SRE / Security |
| Hard dependencies | WP-021, WP-027, WP-051 |
| Related gates | G5,Platform |
| Related controls | CTL-SEC-04, CTL-OPS-03 |
| Related acceptance scenarios | ACC-27, ACC-33 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_052_kubernetes_cluster.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_052_kubernetes_cluster.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Management, service, standard execution, secure/D3+ and untrusted compute node pools are established with HA, quotas, isolation and signed workload admission.


## Analysis
### What this package actually decides

That untrusted compute cannot share a kernel with anything that matters. Node pool
separation — management, service, standard execution, secure/D3+, untrusted — is
the coarse control that makes the fine ones (WP-054's sandbox) survivable if they
fail.

### Taints and tolerations are the enforcement, not the intent (T02)

A pool separation expressed only in scheduling preferences is a suggestion. The
untrusted pool must be **unschedulable** for anything that is not explicitly
tolerating it, and the D3+ pool must be unreachable for workloads without the
matching profile.

### Pod Security and quotas do different jobs (T03)

Pod Security stops a workload from asking for privilege. Quotas stop it from
consuming everything — which is `PR-09`'s cost runaway expressed in CPU rather
than tokens, and also a denial-of-service vector: a research batch that starves
the assurance queue has disabled the laboratory's ability to check itself.

`00_PROGRAM/08` protects the assurance pool explicitly for that reason.

### The upgrade runbook is the part that ages badly (T06)

A cluster is upgraded on someone else's schedule. Without a rehearsed runbook, the
upgrade either does not happen — accumulating CVEs the admission controller will
eventually block — or happens under pressure. Both are worse than a rehearsal.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/wp_021_environment_account_network_baseline.md) | `Environment topology` · `Account/network IaC` · `Access baseline` · `Environment promotion policy` |
| [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/wp_027_git_oci_supply_chain.md) | `OCI registry` · `Build/promotion pipeline` · `SBOM/provenance artifacts` · `Signature policy seed` |
| [WP-051 — Four Trust Zones and Network Segmentation](../06_EXECUTION_SECURITY/wp_051_trust_zone_network.md) | `Trust zone diagram/data flows` · `Network IaC` · `Boundary policy` · `Threat-test suite` |

### Full prerequisite closure

**27 of 141 packages (19%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |
| 8 | `WP-011` |
| 9 | `WP-012` · `WP-013` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-015` · `WP-017` |
| 12 | `WP-018` |
| 13 | `WP-019` |
| 14 | `WP-020` |
| 15 | `WP-021` · `WP-022` |
| 16 | `WP-023` · `WP-026` · `WP-051` |
| 17 | `WP-024` |
| 18 | `WP-027` |

### What acceptance of this package releases

- **Directly unblocked:** 10 — `WP-053` · `WP-054` · `WP-055` · `WP-059` · `WP-060` · `WP-084` · `WP-096` · `WP-100` · `WP-101` · `WP-114`
- **Transitively reachable:** **83 of 141 packages (59%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **19** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Platform Infrastructure Lead |
| Independent verifier | SRE / Security |
| Gates touched | `G5` · `Platform` |
| Controls | `CTL-SEC-04` · `CTL-OPS-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-27 — Regional / Management Plane DR](../12_ACCEPTANCE_SCENARIOS/acc_27_regional_dr.md) | Critical | Temporal workflow state holds at RPO = 0, canonical registries, artifacts and audit records are intact, service returns within the RTO target, and derived views are rebuilt. |
| [ACC-33 — Kueue Preemption](../12_ACCEPTANCE_SCENARIOS/acc_33_kueue_preemption.md) | High | The scout is checkpointed, paused or evicted and the critical reproduction is admitted; canonical task state and artifacts are not lost and the scout resumes later. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/wp_027_git_oci_supply_chain.md), [WP-051 — Four Trust Zones and Network Segmentation](../06_EXECUTION_SECURITY/wp_051_trust_zone_network.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `Environment topology` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Account/network IaC` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Access baseline` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Environment promotion policy` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `OCI registry` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Build/promotion pipeline` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `SBOM/provenance artifacts` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Signature policy seed` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Trust zone diagram/data flows` | `WP-051` | `python3 scripts/progress.py show WP-051` |
| `Network IaC` | `WP-051` | `python3 scripts/progress.py show WP-051` |
| `Boundary policy` | `WP-051` | `python3 scripts/progress.py show WP-051` |
| `Threat-test suite` | `WP-051` | `python3 scripts/progress.py show WP-051` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Platform Infrastructure Lead** carries the acceptance decision; **SRE / Security** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-052-T01 | Establish the cluster topology and control-plane HA | Implementation owner | Commit / configuration / record reference |
| WP-052-T02 | Apply the node pool, taint and toleration separation | Implementation owner | Commit / configuration / record reference |
| WP-052-T03 | Write the Pod Security, namespace and resource quota baseline | Implementation owner | Commit / configuration / record reference |
| WP-052-T04 | Establish the storage, network and ingress classes | Implementation owner | Commit / configuration / record reference |
| WP-052-T05 | Add autoscaling, capacity reserve and maintenance policy | Implementation owner | Commit / configuration / record reference |
| WP-052-T06 | Write the cluster backup, upgrade and restore runbook | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Kubernetes clusters`
- `Node pool catalog`
- `Namespace/security baseline`
- `Upgrade/restore runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-052_kubernetes_cluster.tests.md`](wp_052_kubernetes_cluster.tests.md).

- Node failure and rescheduling
- Denial of a secure workload scheduled onto the wrong node
- A canary cluster upgrade
- A capacity pressure test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-052_kubernetes_cluster.acceptance.md`](wp_052_kubernetes_cluster.acceptance.md), together with what this package still cannot establish.

- [ ] D3/D4 and untrusted workloads never run outside their designated pool.
- [ ] Control-plane worker pods are separated from the execution namespace.
- [ ] Critical assurance capacity is reserved and cannot be consumed by feature work.
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

Cluster and node upgrades roll back, or use a blue-green control plane; workload manifests and artifacts are preserved throughout.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
