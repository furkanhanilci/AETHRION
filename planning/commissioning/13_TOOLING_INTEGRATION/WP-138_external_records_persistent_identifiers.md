# WP-138 — External Records and Persistent Identifiers

## Package card

| Field | Value |
|---|---|
| Work package | `WP-138` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Data Steward |
| Independent verifier | Project Decision Owner |
| Hard dependencies | WP-014 (Artifact manifest), WP-090 (Publication package), WP-131 |
| Related gates | G2, G9 |
| Related controls | CTL-EPI-01 |
| Related acceptance scenarios | ACC-30, ACC-45 |
| Related skill | `submitting-external-records` |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-138_external_records_persistent_identifiers.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-138_external_records_persistent_identifiers.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Internal records verify themselves; **an external record is an independent witness.**

| Record | Destination | Gate | What it buys |
|---|---|---|---|
| Pre-registration (protocol + analysis plan) | **OSF Registries** | **G2** | Timestamped, immutable record + persistent DOI, with an embargo option |
| Code + environment | Zenodo / Software Heritage | G9 | Permanent archive + DOI |
| Dataset | Zenodo / domain repository | G9 | DOI + Croissant metadata |
| Publication package | Zenodo / institutional repository | G9 | RO-Crate + DOI |
| Author identity | ORCID | G9 | Persistent author identity |

**Why an external pre-registration at G2:** the internal
`AnalysisPlanManifest` hash lives in *your* system. An external record is
evidence even to someone who does **not** trust your system. That is the
external anchor of in-principle acceptance.

> **Invariant:** An external submission cannot be undone. Each one requires a
> **full-word** human confirmation (`SUBMIT`).


## Analysis
### What this package actually decides

That someone outside can check. The purpose sentence is the sharpest statement of
the gap in this whole repository: *internal records verify themselves; **an external
record is an independent witness.***

Everything the system produces today is tamper-evident **to a reader who trusts the
operator's infrastructure**. `airl-interim-v0.1` says so in its own `limitations`
list: local key, no transparency log, no external timestamp authority.

### OSF pre-registration is the epistemic half (T01)

A protocol timestamped in an external registry before data exists is the only form
of preregistration a sceptical reader can verify. An internal freeze proves the
protocol did not change **according to the system that holds it**.

The embargo option matters: pre-registration should not force disclosure before the
researcher is ready.

### Zenodo deposit and the DOI are the persistence half (T02)

A publication package that exists only in this repository disappears when the
repository does. A DOI is a commitment by a third party to keep resolving it.

### The metadata trio is what makes the deposit usable (T04)

`CITATION.cff`, CodeMeta, Croissant. Adopted formats (`AETHRION_COMPONENT_REUSE.md`
names Croissant), so a reader's tooling can consume the deposit without knowing
anything about this system — the same argument as RO-Crate in WP-090.

### The full-word confirmation gate is unusual and correct (T05)

A deposit is **irreversible**: once a DOI resolves, the record is public and
permanent. Requiring the operator to type `SUBMIT` is a deliberate friction against
an automated or accidental publication, and it belongs in a system where agents
initiate most actions.

### ORCID binding (T03)

Author identity that resolves outside the system, so authorship is not a string in
a database.

## Out of scope

- Preprint submission cannot be fully automated (arXiv requires a human step)
- The publication content itself (WP-090)

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/WP-090_publication_package.md) | `Publication builder` · `RO-Crate profile` · `Signed publication package` · `Release checklist` |
| [WP-131 — Notification Broker Foundation](../13_TOOLING_INTEGRATION/WP-131_notification_broker.md) | — |

### Full prerequisite closure

**83 of 141 packages (59%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 18 | `WP-027` · `WP-030` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-037` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` · `WP-131` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` |
| 31 | `WP-068` · `WP-071` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` · `WP-085` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-090` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | W-T — Tooling |
| Dependency depth | level **41** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Data Steward |
| Independent verifier | Project Decision Owner |
| Gates touched | `G2` · `G9` |
| Controls | `CTL-EPI-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/ACC-30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |
| [ACC-45 — Irreversible External Record Submission](../12_ACCEPTANCE_SCENARIOS/ACC-45_external_record_submission.md) | Critical | The unapproved attempt is refused; the approved submission produces exactly one identifier; the repeat is idempotent; and the submitted payload hash matches the approved one. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: WP-014 (Artifact manifest), WP-090 (Publication package), WP-131
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
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
| `Publication builder` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `RO-Crate profile` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Signed publication package` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Release checklist` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Supersession record` | `WP-090` | `python3 scripts/progress.py show WP-090` |

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
- **Data Steward** carries the acceptance decision; **Project Decision Owner** must verify independently of whoever implements.
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

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-138-T01 | OSF Registries pre-registration flow with the embargo option | A timestamped record + DOI at G2 |
| WP-138-T02 | Zenodo deposit flow (code, data, publication) | A DOI is returned and written into the manifest |
| WP-138-T03 | Bind ORCID author identity | ORCID appears in the publication package |
| WP-138-T04 | Generate `CITATION.cff` + `CodeMeta` + Croissant | The metadata files validate |
| WP-138-T05 | Full-word confirmation gate (`SUBMIT`) | Submission without confirmation is impossible |
| WP-138-T06 | Write the returned DOI into the `EvidenceManifest` | An unrecorded DOI is not accepted |

## Mandatory deliverables

- The OSF, Zenodo and ORCID connectors
- The `ExternalRegistrationRecord` and `DOIRecord` schemas
- The `CITATION.cff`, `CodeMeta` and Croissant generators
- The full-word confirmation gate

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-138_external_records_persistent_identifiers.tests.md`](WP-138_external_records_persistent_identifiers.tests.md).

- **Confirmation gate:** no submission occurs without typing `SUBMIT`
- **Data class:** D2+ content cannot go to an external record
- **DOI recording:** the package does not close until the returned DOI is in the manifest
- **Embargo:** the embargo option is applied at submission time
- **Irreversibility:** the rollback test produces a new version rather than a deletion

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-138_external_records_persistent_identifiers.acceptance.md`](WP-138_external_records_persistent_identifiers.acceptance.md), together with what this package still cannot establish.

- [ ] An external submission cannot be triggered by an agent
- [ ] Every submission has a full-word human confirmation record
- [ ] Every returned DOI is written into the `EvidenceManifest`
- [ ] The G2 pre-registration is timestamped and immutable
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Risks and control points

- An external record cannot be withdrawn; a correction is a new version, never a deletion
- The provider API's programmatic submission path must be verified before implementation
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

A submitted record cannot be recalled. A new version is published and the old
one is marked `SUPERSEDED`. That is exactly why the pre-submission checks are
non-waivable.

## Handoff into downstream packages

WP-139 binds internal evidence sealing and WP-090 binds the publication package
to these records.
