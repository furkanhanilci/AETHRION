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
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-139_evidence_timestamping.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-139_evidence_timestamping.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

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


## Analysis
### What this package actually decides

That a manifest's existence at a time is provable **without trusting this system**.
The purpose sentence names the property exactly, and it is the one gap
`airl-interim-v0.1` declares about itself in every manifest it issues.

### What the interim profile actually lacks

`scripts/evidence_manifest.py` states it in its own docstring, and every
verification prints it:

> **not covered** — transparency log · keyless identity · external timestamp
> authority

The interim anchor binds the envelope digest to a wall clock and a git commit. Both
are held by the operator. A reader who trusts the operator gains a real guarantee; a
reader who does not gains nothing — and the whole architecture argues that the
second reader is the one who matters.

### Two independent anchors, deliberately (T01, T02)

**OpenTimestamps** anchors into Bitcoin — no trusted party, slow confirmation.
**RFC 3161** is a trusted timestamp authority — fast, and trusted.

Their failure modes are disjoint: one requires no trust and takes hours; the other
is immediate and requires trusting a TSA. Having both means a verifier can choose
which assumption to make.

### Automatic stamping at the G2 analysis-plan lock is the highest-value trigger (T05)

Preregistration's whole claim is *the analysis plan existed before the data*. An
internal freeze proves it to the system that holds it. An external timestamp proves
it to a reader — and this is the single point where the cost of stamping buys the
most.

### The verification runbook is part of the deliverable (T04)

A stamp nobody can verify is decoration. The command has to work for someone with
the manifest, the stamp file and no access to this system.

### Baseline v1.3.0 — the messaging layer inherits the same two refusals

Nothing changes about what these packages own. Two rules from this baseline
apply to all of them, and both are restatements of things that erode first at the
edges of a system:

**No message and no timeout becomes authority.** An inbound message is never an
instruction; a notification is never an authorisation; an expired SLA escalates
and pages and never approves.

**Alignment with the new paths.** The capability gate governs any action an
inbound message might trigger. Evidence-delta priority drives the decision
queue. The human preliminary flow means a notification announcing a decision may
not carry the recommendation. Every intervention writes an immutable audit
record atomically with the change it describes.

## Out of scope

- The manifest content itself (WP-014)
- Signing infrastructure (WP-027, WP-059)

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |

### Full prerequisite closure

**22 of 160 packages (14%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 15 | `WP-021` |
| 16 | `WP-026` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | W-T — Tooling |
| Dependency depth | level **17** of 55 |
| On the documented critical path | no |
| Effort class | **S** |
| Accountable owner | Data Platform Lead |
| Independent verifier | Research Integrity Officer |
| Gates touched | `G2` · `G5` · `G9` |
| Controls | `CTL-DAT-03` · `CTL-SUP-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-23 — Artifact Overwrite Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-23_artifact_overwrite.md) | Critical | The overwrite is rejected; the new bytes can only be written as a new content address and version, and existing references are unchanged. |
| [ACC-40 — Complete Project Audit Export](../12_ACCEPTANCE_SCENARIOS/ACC-40_audit_export.md) | Critical | The signed export verifies with complete correlation and hash chain; a missing or tampered fixture fails verification and raises an incident. |
| [ACC-45 — Irreversible External Record Submission](../12_ACCEPTANCE_SCENARIOS/ACC-45_external_record_submission.md) | Critical | The unapproved attempt is refused; the approved submission produces exactly one identifier; the repeat is idempotent; and the submitted payload hash matches the approved one. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: WP-014 (Artifact manifest), WP-026 (Object store WORM)
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- The **acquisition surface is classified**: every part of this package is `DEPENDENCY`, `ADAPTER`, `OPTIONAL_BACKEND`, `STANDARD`, `BENCHMARK`, `PATTERN`, `DIRECT_ADAPT`, `ADAPTIVE_REIMPLEMENT` or `BUILD_NATIVE`, and every obligation the mode creates is resolved — see **Implementation acquisition and assimilation** above.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Ordered parent lineage` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Digest normalisation and migration` | `WP-014` | `python3 scripts/progress.py show WP-014` |
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

- **Effort class `S`** — small — one owner, one review cycle.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Data Platform Lead** carries the acceptance decision; **Research Integrity Officer** must verify independently of whoever implements.
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
| `CMP-021` — OpenTimestamps | `DEPENDENCY` | The timestamp proof and its verification path. | What is anchored, and the statement that today's profile is tamper-evident but not externally witnessed. | **2** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `CMP-021` | An anchor establishes that something existed by a time. It says nothing about who produced it or whether it is true. | The anchor as a substitute for an independent verifier. |

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`CMP-021` — OpenTimestamps** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**Acquisition readiness — 2 obligations open across 1 of 1 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

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

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-139_evidence_timestamping.tests.md`](WP-139_evidence_timestamping.tests.md).

- **Independent verification:** the stamp verifies on a third machine, without the framework
- **Pre-registration proof:** the plan stamp precedes the result artifact's stamp
- **Unstamped manifest:** rejected (negative test)
- **Maturation:** a pending OpenTimestamps proof is tracked and completed
- **Clock manipulation:** changing the local clock does not change the stamp

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-139_evidence_timestamping.acceptance.md`](WP-139_evidence_timestamping.acceptance.md), together with what this package still cannot establish.

- [ ] The existence time of an `EvidenceManifest` is verifiable without trusting the framework
- [ ] The `AnalysisPlanManifest` lock is stamped automatically
- [ ] Stamp files are stored alongside the manifest and the object store
- [ ] The verification runbook is executable by a third party
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Acceptance evidence package

- Test results captured on the same target revision/digest
- An `EvidenceManifest` recording the environment, schema, policy and dependency versions
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The rollback/compensation trial and its result reference
- The list of open findings and residual risks with owners and expiry dates

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
