---
title: "WP-054 — gVisor Sandbox and Execution Cell Lifecycle"
aliases:
  - "WP-054"
  - "WP-054 — gVisor Sandbox and Execution Cell Lifecycle"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Every autonomous code execution runs in an ephemeral cell — resolve → allocate → attest → execute → capture → destroy — that is digest-pinned, privilege-free, scope-mounted and produces forensic evidence."
source: "planning/commissioning/06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/06-execution-security
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g5
  - aethrion/gate/engineering
  - aethrion/state/not-started
---

# WP-054 — gVisor Sandbox and Execution Cell Lifecycle

## Package card

| Field | Value |
|---|---|
| Work package | `WP-054` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Execution Security Lead |
| Independent verifier | Red Team / SRE |
| Hard dependencies | WP-006, WP-014, WP-027, WP-049, WP-052, WP-053 |
| Related gates | G5,Engineering |
| Related controls | CTL-SEC-04, CTL-SEC-05 |
| Related acceptance scenarios | ACC-15, ACC-17 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_054_gvisor_sandbox.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_054_gvisor_sandbox.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Every autonomous code execution runs in an ephemeral cell — resolve → allocate → attest → execute → capture → destroy — that is digest-pinned, privilege-free, scope-mounted and produces forensic evidence.


## Analysis
### What this package actually decides

That autonomous code execution leaves nothing behind and takes nothing with it.
The lifecycle in the purpose sentence is the package: **resolve → allocate →
attest → execute → capture → destroy.** Six steps, and the two that get skipped in
practice are `attest` and `destroy`.

### Ephemeral means destroyed, not reused (T02, T05)

A reused workspace carries state between tasks, and state between tasks is how one
task's output becomes another's input without anyone deciding it should. Worse, it
is how a compromised task persists.

Destruction has to be unconditional — including on failure, including on timeout,
including when the capture step errored. A cell that survives its own failure is
the one an attacker wants.

### Attestation before execution, not after (T03)

The image is checked for signature and SBOM **before** anything runs. Checking
afterwards tells you what happened; checking before decides whether it happens.
WP-059's admission controller is the same rule at the cluster layer, and both are
needed — this one covers the case where the sandbox pulls its own image.

### gVisor is a second kernel boundary, not the only one (T01)

`AETHRION_COMPONENT_REUSE.md` adopts it. The honest framing is layered: node pool
separation (WP-052) assumes the kernel holds; gVisor reduces the kernel surface
the workload can reach; seccomp and capability drops reduce it further. None of
them is a guarantee, and the design does not depend on any one of them being one.

### Forensic snapshotting is what makes an escape investigable (T06)

An escape detected and then destroyed leaves nothing to investigate. The snapshot
has to be taken **at detection**, before teardown, and it is the only artifact
`investigating-integrity-concerns` will have to work from.

### Artifact capture is a boundary crossing (T05)

Whatever the cell produces is Zone 3 content until it has been through WP-058's
quarantine. Hashing and uploading it is not the same as trusting it.

### Baseline v1.3.0 — four zones, a capability gate, and a benchmark firewall

The isolation story gains a fourth zone and two new attack surfaces.

**Four zones, not three.** Producer, evaluator, reproducer and independent
grader, separated in secrets, cache and workspace. The leakage paths that matter
are the quiet ones — a shared cache, an inherited credential, a warm container
layer — and none of them looks like a boundary violation in a log. Each is tested
explicitly rather than inferred from the zone configuration (ACC-113).

**Security is a capability, not a prompt.** *Prompt says safe* is not security;
*the capability is unavailable unless policy grants it* is. External content —
PDF, web page, tool result, reviewer comment — is quarantined into a data object,
and the agent's tool intent passes a policy gate before any credential is
injected (ACC-117).

**A benchmark firewall.** An evaluation run freezes its dataset manifest, network
mode, allowed domains, known identifiers and evaluator isolation before it
starts, and audits every retrieval. Gold answers, private rubrics, hidden tests
and grader prompts are unreachable from the agent environment (ACC-118).

The attack suite gains ASB and WASP as external regressions, alongside internal
fixtures for source-PDF injection, malicious citation text, tool-result
injection, memory poisoning and credential exfiltration.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md) | `ExecutionProfile semantics` · `Route/control decision tables` · `Enforcement map` · `Negative examples` |
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/wp_027_git_oci_supply_chain.md) | `OCI registry` · `Build/promotion pipeline` · `SBOM/provenance artifacts` · `Signature policy seed` |
| [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md) | `Tool Registry` · `Tool Broker service` · `Invocation/Receipt persistence` · `Connector SDK` |
| [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md) | `Kubernetes clusters` · `Node pool catalog` · `Namespace/security baseline` · `Upgrade/restore runbook` |
| [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/wp_053_kueue_quota.md) | `Kueue configuration` · `Quota/priority policy` · `Budget admission adapter` · `Queue dashboard` |

### Full prerequisite closure

**41 of 160 packages (26%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 16 | `WP-023` · `WP-025` · `WP-026` · `WP-051` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |

### What acceptance of this package releases

- **Directly unblocked:** 7 — `WP-058` · `WP-059` · `WP-060` · `WP-083` · `WP-084` · `WP-104` · `WP-107`
- **Transitively reachable:** **86 of 160 packages (54%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **24** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Execution Security Lead |
| Independent verifier | Red Team / SRE |
| Gates touched | `G5` · `Engineering` |
| Controls | `CTL-SEC-04` · `CTL-SEC-05` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-15 — Sandbox Escape Attempt](../12_ACCEPTANCE_SCENARIOS/acc_15_sandbox_escape.md) | Critical | Every escape path is denied or contained; no credential or host data leaks, the cell is stopped and a forensic `SecurityEvent` is produced. |
| [ACC-17 — Unsigned or Mutable Image](../12_ACCEPTANCE_SCENARIOS/acc_17_unsigned_image.md) | Critical | The pod is not created; the signature, provenance and digest policy denies it and produces audit and alert records. A signed-digest counter-example passes. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/wp_027_git_oci_supply_chain.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md), [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/wp_053_kueue_quota.md)
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
| `ExecutionProfile semantics` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Route/control decision tables` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Enforcement map` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Negative examples` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Producer and evaluator zone profiles` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `MutationPolicy` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Ordered parent lineage` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Digest normalisation and migration` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `OCI registry` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Build/promotion pipeline` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `SBOM/provenance artifacts` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Signature policy seed` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Tool Registry` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool Broker service` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Invocation/Receipt persistence` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Connector SDK` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Audit events` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Capability gate` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool-result reuse with recorded provenance` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Kubernetes clusters` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Node pool catalog` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Namespace/security baseline` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Upgrade/restore runbook` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Kueue configuration` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Quota/priority policy` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Budget admission adapter` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Queue dashboard` | `WP-053` | `python3 scripts/progress.py show WP-053` |

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
- **Execution Security Lead** carries the acceptance decision; **Red Team / SRE** must verify independently of whoever implements.
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
| WP-054-T01 | Establish the RuntimeClass/gVisor and seccomp/capability baseline | Implementation owner | Commit / configuration / record reference |
| WP-054-T02 | Apply the ephemeral workspace, mount and path policy | Implementation owner | Commit / configuration / record reference |
| WP-054-T03 | Bind the OCI signature and SBOM attestation gate | Implementation owner | Commit / configuration / record reference |
| WP-054-T04 | Add CPU, memory, wall-clock and process limits | Implementation owner | Commit / configuration / record reference |
| WP-054-T05 | Write artifact capture, hashing, upload and teardown | Implementation owner | Commit / configuration / record reference |
| WP-054-T06 | Establish forensic snapshotting and escape detection | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Sandbox profiles`
- `Execution Cell controller`
- `SandboxAttestation`
- `Capture/destroy workflow`
- `Red-team tests`
- `Four-zone isolation profiles`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-054_gvisor_sandbox.tests.md`](wp_054_gvisor_sandbox.tests.md).

- Denial of host mount, privilege and syscall escape attempts
- Denial of unsigned or mutable images
- Termination of a resource bomb
- Artifact capture followed by cell destruction
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-054_gvisor_sandbox.acceptance.md`](wp_054_gvisor_sandbox.acceptance.md), together with what this package still cannot establish.

- [ ] An agent has no direct access to the host kernel, credentials or network.
- [ ] Credentials and compute are destroyed at cell expiry.
- [ ] Artifact hashes and attestations return to the workflow.
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

A suspicious cell is contained and stopped, its forensic snapshot quarantined, and the node drain/reimage runbook is executed.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
