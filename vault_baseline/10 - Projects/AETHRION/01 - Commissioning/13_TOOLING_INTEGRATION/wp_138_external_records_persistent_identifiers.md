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
| Current status | `NOT_STARTED` |

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

## Out of scope

- Preprint submission cannot be fully automated (arXiv requires a human step)
- The publication content itself (WP-090)

## Preconditions — Definition of Ready

- Dependencies accepted: WP-014 (Artifact manifest), WP-090 (Publication package), WP-131
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

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

- **Confirmation gate:** no submission occurs without typing `SUBMIT`
- **Data class:** D2+ content cannot go to an external record
- **DOI recording:** the package does not close until the returned DOI is in the manifest
- **Embargo:** the embargo option is applied at submission time
- **Irreversibility:** the rollback test produces a new version rather than a deletion

## Acceptance criteria

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
