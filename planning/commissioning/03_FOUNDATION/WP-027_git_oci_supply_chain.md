# WP-027 — Git, OCI Registry and Build Provenance Foundation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-027` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Supply Chain Security Lead |
| Independent verifier | Security Reviewer / SRE |
| Hard dependencies | WP-021, WP-022, WP-024, WP-026 |
| Related gates | G5,Platform |
| Related controls | CTL-SEC-05, CTL-SUP-01 |
| Related acceptance scenarios | ACC-17 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-027_git_oci_supply_chain.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-027_git_oci_supply_chain.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The chain from source commit to a digest-pinned OCI image is established, covering SBOM, provenance, signature, vulnerability status and promotion.


## Analysis
### What this package actually decides

That a running image can be traced to a commit. Everything downstream that says
"the same target revision" depends on it: an environment manifest pinning an OCI
digest is only as good as the chain from that digest back to source.

### T05 is the whole package in one line: mutable tags are prohibited

A tag is a pointer someone can move. `latest`, `v1`, even `v1.2.3` on most
registries can be repointed, and an environment manifest that pins a tag pins
nothing. WP-019's reproduction contract already rejects a tag reference; this
package is where the registry stops offering one.

### Reproducible builds are the claim most likely to be overstated (T02)

"Reproducible" has a precise meaning — the same source produces byte-identical
output — and most builds are not, because timestamps, paths and ordering leak in.
The honest positions are: achieve it and demonstrate it twice on different
machines, or **declare it not achieved and say what varies**. Claiming it without
the double build is the plausibility failure this whole repository is built
against.

### SBOM and vulnerability status are different artifacts with different lifetimes (T03)

An SBOM is a fact about the image and is immutable with it. A vulnerability status
is a fact about the world and changes daily — an image clean at build time is not
clean a month later. Storing the second *inside* the first is how a system ends up
asserting an advisory-free image that has three open criticals.

### The adoption boundary

`AETHRION_COMPONENT_REUSE.md` adopts **sigstore** and **SWHID**. Adopted, not
invented — this package configures them and records the `authority_boundary`, and
it must not grow a bespoke signing scheme alongside.

### Baseline v1.3.0 — modular monolith first, and a projection that can be destroyed

The collaboration plane, the conformance checker and the release assurance work
land as **modules**, not as services. A logical plane is an ownership boundary;
turning each into a deployment unit before there is a consumer buys operational
cost and no assurance.

Two guarantees the foundation now owes:

**Every derived projection is destroyable.** The graph, the vector index and the
search index are rebuilt from canonical stores as a routine, tested operation —
ACC-119. A rebuild path that is an emergency procedure will not work on the day
it is needed.

**Release artifacts carry provenance.** SLSA provenance, Sigstore signatures, an
SBOM and its scan result, and the upstream register accounting for every adapted
file. `ADR-019`, delivered by WP-159 and admitted against by WP-024's CI.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md) | `Environment topology` · `Account/network IaC` · `Access baseline` · `Environment promotion policy` |
| [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/WP-022_repository_topology.md) | `Repository skeleton` · `CODEOWNERS` · `Dependency rules` · `Developer guide` |
| [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md) | `CI pipelines` · `Verification summary schema adapter` · `Test ownership registry` · `Flake policy` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |

### Full prerequisite closure

**25 of 160 packages (16%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 16 | `WP-023` · `WP-026` |
| 17 | `WP-024` |

### What acceptance of this package releases

- **Directly unblocked:** 10 — `WP-031` · `WP-048` · `WP-052` · `WP-054` · `WP-059` · `WP-084` · `WP-087` · `WP-107` · `WP-129` · `WP-159`
- **Transitively reachable:** **122 of 160 packages (76%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **18** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Supply Chain Security Lead |
| Independent verifier | Security Reviewer / SRE |
| Gates touched | `G5` · `Platform` |
| Controls | `CTL-SEC-05` · `CTL-SUP-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-17 — Unsigned or Mutable Image](../12_ACCEPTANCE_SCENARIOS/ACC-17_unsigned_image.md) | Critical | The pod is not created; the signature, provenance and digest policy denies it and produces audit and alert records. A signed-digest counter-example passes. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md), [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/WP-022_repository_topology.md), [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- The **acquisition surface is classified**: every part of this package is `DEPENDENCY`, `ADAPTER`, `OPTIONAL_BACKEND`, `STANDARD`, `BENCHMARK`, `PATTERN`, `DIRECT_ADAPT`, `ADAPTIVE_REIMPLEMENT` or `BUILD_NATIVE`, and every obligation the mode creates is resolved — see **Implementation acquisition and assimilation** above.
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
| `Repository skeleton` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `CODEOWNERS` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Dependency rules` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Developer guide` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `CI pipelines` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Verification summary schema adapter` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Test ownership registry` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Flake policy` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `SPDX/REUSE and OSV admission checks` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |

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
- **Supply Chain Security Lead** carries the acceptance decision; **Security Reviewer / SRE** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation acquisition and assimilation

<!-- generated:implementation-sources — produced by scripts/expand_acquisition.py; do not edit inside this block -->

**What is already solved elsewhere, and on what terms.** Before the first task starts, an implementer has to know which parts of this package are called at runtime, which are copied and refactored, which are reimplemented from a specification, and which have no upstream at all. Those decisions are recorded in [`provenance/upstreams.json`](../../../provenance/upstreams.json) — mechanisms assimilated into this repository's own code — and in [`provenance/components.json`](../../../provenance/components.json) — components adopted at runtime. This block is derived from both, so a decision and the place it is used cannot drift apart.

### Acquisition map

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| `ASM-056` — SLSA — build and source provenance levels | `STANDARD` | the running implementation | the contract this is held behind | **1** |
| `CMP-019` — sigstore-python | `DEPENDENCY` | Keyless OIDC identity, certificate issuance and the Rekor inclusion proof. | The attestation profile and what a signature is taken to mean. The named upgrade out of `airl-interim-v0.1`. | **2** |
| `CMP-024` — SWHID | `STANDARD` | The identifier scheme itself. | Where a software identity is required in the evidence chain. | none |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-056` | Provenance establishes what built an artifact from which source. It says nothing about whether the artifact is correct. | Any bespoke provenance format. |
| `CMP-019` | A signature establishes who issued an artifact and that it has not changed. It never establishes that the content is correct, and a verified signature is not an acceptance. | Sigstore identity as an AETHRION role binding. |
| `CMP-024` | An intrinsic identifier establishes identity, not availability and not correctness. Computing one does not archive the code. | SWHID as a substitute for an environment manifest. |

### Where a plain row would mislead

- **`CMP-019`** — Renaming the interim profile `airl-interim-v0.1` or the `https://airl-os.local/…` predicateType invalidates a signature that verifies today — AGENTS.md §7.5.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-056` — SLSA — build and source provenance levels** · `STANDARD` · status `PROPOSED`

- a conformance suite against the published specification

**`CMP-019` — sigstore-python** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**Acquisition readiness — 3 obligations open across 2 of 3 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-027-T01 | Set up the OCI registry environment and repository structure | Implementation owner | Commit / configuration / record reference |
| WP-027-T02 | Produce reproducible builds and provenance metadata | Implementation owner | Commit / configuration / record reference |
| WP-027-T03 | Add SBOM generation and vulnerability scanning | Implementation owner | Commit / configuration / record reference |
| WP-027-T04 | Bind the Sigstore keyless or key policy | Implementation owner | Commit / configuration / record reference |
| WP-027-T05 | Prohibit the use of mutable tags | Implementation owner | Commit / configuration / record reference |
| WP-027-T06 | Establish the dev → staging → prod digest promotion flow | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `OCI registry`
- `Build/promotion pipeline`
- `SBOM/provenance artifacts`
- `Signature policy seed`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-027_git_oci_supply_chain.tests.md`](WP-027_git_oci_supply_chain.tests.md).

- A negative promotion test with an unsigned image
- An admission fixture rejecting a mutable tag
- A reproducible-build comparison from the same commit
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-027_git_oci_supply_chain.acceptance.md`](WP-027_git_oci_supply_chain.acceptance.md), together with what this package still cannot establish.

- [ ] Production runs only signed digests.
- [ ] Every build artifact is bound to a source commit and a dependency lock.
- [ ] A critical vulnerability does not promote without an explicit policy decision.
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

- Infrastructure built by hand once is infrastructure that cannot be rebuilt under pressure.
- A backup that has never been restored is not a backup.
- Environment parity erodes from the staging side first, and quietly.

## Rollback / compensation

A compromised digest is revoked and quarantined; the previous signed image is restored and an impact scan is performed.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
