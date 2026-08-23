# WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-059` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Supply Chain Security Lead |
| Independent verifier | Independent Security Reviewer |
| Hard dependencies | WP-027, WP-052, WP-054, WP-056 |
| Related gates | G5,Platform |
| Related controls | CTL-SEC-05, CTL-SUP-01 |
| Related acceptance scenarios | ACC-17, ACC-26 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-059_supply_chain_admission.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-059_supply_chain_admission.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Kubernetes and tool/runtime deployments accept only digest-pinned, signed artifacts with SBOM and provenance that satisfy policy.


## Analysis
### What this package actually decides

That nothing unverified runs. WP-027 builds the chain from commit to signed,
digest-pinned image; this package is the controller that **refuses** anything
without one — at the moment of deployment, where refusal still costs nothing.

### The admission controller is where policy meets the cluster (T01, T02)

Signature, provenance, SBOM. Three checks, three separate refusals, and the
trust roots are the part that decides what the checks mean: an admission
controller trusting a permissive root admits anything that root signed.

### Allowed builders and source repositories narrow the question (T03)

A valid signature says *someone we trust built this*. Constraining builders and
source repositories says *and they built it from somewhere we recognise* — which
is the difference between supply-chain integrity and supply-chain provenance.

### The CVE exception workflow is where this decays (T04)

A critical advisory blocks a deployment. The pressure is immediate, the exception
is granted, and without an **expiry and a removal criterion** it becomes
permanent. WP-009 already fixes the shape: request, approval, expiry, auto-revoke,
and renewal requires restating the criterion.

An exception register full of indefinite entries is a second, undocumented policy.

### Tool, MCP and plugin artifacts are the forgotten surface (T05)

Container images get scanned. An MCP server, a tool binary or a skill bundle
loaded at runtime often does not — and it executes in the same trust context.
This repository already carries the shape of that risk: 52 skills load into an
agent's context and change its behaviour, and `00_PROGRAM/09` versions the skill
bundle for exactly that reason.

### Revocation must reach running workloads (T06)

Refusing a new deployment is easy. Deciding what happens to the pods already
running a now-revoked image is the real question, and *nothing* is a legitimate
answer only if it is a **recorded** one with an owner.

### Baseline v1.2.0 — adapted source is a supply-chain input

The supply chain covers dependencies that are installed. It must also cover code
that is **adapted** — copied from another project and refactored into this one —
because such code has no package manager entry, no version and no upgrade path,
and is therefore invisible to every other control here.

Admission requires: a permissive licence read at the source, a pinned upstream
commit, a named source-file list, SPDX headers, a `NOTICE` entry and a
characterisation suite written **before** the code moved. A file introduced
without them fails CI before merge — ACC-74.

Drift is monitored rather than merged. When upstream moves past a pin, the
checker reports the divergence and opens a review item; the characterisation
suite reruns and the pin moves through a recorded decision, never automatically
— ACC-73.

The register is `provenance/upstreams.json`, validated by
`scripts/check_upstream_lineage.py`, whose `--self-test` injects a defect per
rule and fails if any rule stays silent. WP-141 owns it; this package binds it to
admission.

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

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md) | `OCI registry` · `Build/promotion pipeline` · `SBOM/provenance artifacts` · `Signature policy seed` |
| [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md) | `Kubernetes clusters` · `Node pool catalog` · `Namespace/security baseline` · `Upgrade/restore runbook` |
| [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md) | `Sandbox profiles` · `Execution Cell controller` · `SandboxAttestation` · `Capture/destroy workflow` |
| [WP-056 — Policy Decision Point and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md) | `Policy decision point` · `PolicyDecision interface conformance suite` · `Policy bundle v1` · `Policy test suite` |

### Full prerequisite closure

**44 of 160 packages (28%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 24 | `WP-054` · `WP-055` |
| 25 | `WP-056` |

### What acceptance of this package releases

- **Directly unblocked:** 7 — `WP-060` · `WP-084` · `WP-099` · `WP-107` · `WP-129` · `WP-141` · `WP-159`
- **Transitively reachable:** **56 of 160 packages (35%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **26** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Supply Chain Security Lead |
| Independent verifier | Independent Security Reviewer |
| Gates touched | `G5` · `Platform` |
| Controls | `CTL-SEC-05` · `CTL-SUP-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-17 — Unsigned or Mutable Image](../12_ACCEPTANCE_SCENARIOS/ACC-17_unsigned_image.md) | Critical | The pod is not created; the signature, provenance and digest policy denies it and produces audit and alert records. A signed-digest counter-example passes. |
| [ACC-26 — Approval, Delegation and Exception Expiry](../12_ACCEPTANCE_SCENARIOS/ACC-26_approval_expiry.md) | Critical | The authority is auto-revoked; new operations are denied and running tasks pause or are contained according to policy. There is no automatic extension or re-approval. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md)
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
| `OCI registry` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Build/promotion pipeline` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `SBOM/provenance artifacts` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Signature policy seed` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Kubernetes clusters` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Node pool catalog` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Namespace/security baseline` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Upgrade/restore runbook` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Sandbox profiles` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Execution Cell controller` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `SandboxAttestation` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Capture/destroy workflow` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Red-team tests` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Four-zone isolation profiles` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Policy decision point` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `PolicyDecision interface conformance suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy bundle v1` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy test suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Bundle promotion pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Decision log pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `M`** — medium — a dedicated integration window.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Supply Chain Security Lead** carries the acceptance decision; **Independent Security Reviewer** must verify independently of whoever implements.
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
| WP-059-T01 | Deploy the admission controller and its trust roots | Implementation owner | Commit / configuration / record reference |
| WP-059-T02 | Write the Cosign signature, provenance and SBOM policy | Implementation owner | Commit / configuration / record reference |
| WP-059-T03 | Define the allowed builders, source repositories and dependency thresholds | Implementation owner | Commit / configuration / record reference |
| WP-059-T04 | Bind the CVE exception and expiry workflow | Implementation owner | Commit / configuration / record reference |
| WP-059-T05 | Add signature checks for tool, MCP and plugin artifacts | Implementation owner | Commit / configuration / record reference |
| WP-059-T06 | Establish revocation behaviour and its impact on running workloads | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Admission policies`
- `Trust root management`
- `CVE/exception workflow`
- `Revocation/impact runbook`
- `Adapted-source admission control`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-059_supply_chain_admission.tests.md`](WP-059_supply_chain_admission.tests.md).

- Denial of an unsigned image
- Denial of a mutable tag
- Denial of provenance from an untrusted builder
- Denial under an expired CVE exception
- An alert on a running workload with a revoked digest
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-059_supply_chain_admission.acceptance.md`](WP-059_supply_chain_admission.acceptance.md), together with what this package still cannot establish.

- [ ] Production never runs an unsigned artifact.
- [ ] Every exception is time-bound and owned.
- [ ] Revocation produces an impact assessment for open and running workloads.
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

On a policy false positive the previous signed bundle is restored; no permanent manual allowlist bypass is granted for an artifact.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
