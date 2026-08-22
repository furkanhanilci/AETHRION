# WP-137 — G10 External Feed Connectors

## Package card

| Field | Value |
|---|---|
| Work package | `WP-137` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Monitoring Lead |
| Independent verifier | Citation Auditor |
| Hard dependencies | WP-037 (G10 ImpactScan), WP-063 (Source status), WP-136 |
| Related gates | G10 |
| Related controls | CTL-EPI-04 |
| Related acceptance scenarios | ACC-04, ACC-31, ACC-36 |
| Related skill | `monitoring-external-feeds` |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Post-publication monitoring feeds are connected and versioned.

| Feed | What it watches |
|---|---|
| Crossref + Retraction Watch | Has a cited source been retracted? |
| Crossmark | Correction notices |
| PubMed / domain repository | Corrections and retractions |
| Dataset registry | Dataset version changes and withdrawals |
| CVE / security advisories | Vulnerabilities in a tool we use |
| Provider changelog | A model profile changed or was removed |
| Citation tracking | Who has refuted us? |

> **Invariant:** There is no silent supersession. A material signal opens an
> `ImpactCase` and requires a human decision. Declaring something "immaterial"
> is itself a decision, and it is auditable.

## Out of scope

- The `ImpactCase` resolution decision itself (WP-108)

## Preconditions — Definition of Ready

- Dependencies accepted: WP-037 (G10 ImpactScan), WP-063 (Source status), WP-136
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

## Implementation tasks

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-137-T01 | Feed registry: source, version, access date, poll frequency | Registry file |
| WP-137-T02 | Crossref + Retraction Watch connector | A retraction is caught in test |
| WP-137-T03 | Dataset registry and CVE feeds | A version change is caught |
| WP-137-T04 | Provider model changelog monitoring | A model profile change triggers requalification |
| WP-137-T05 | Materiality scoring with a mandatory rationale | A materiality decision without a rationale is rejected |
| WP-137-T06 | Feed liveness check (dead-man's switch) | A stalled feed raises an alarm |

## Mandatory deliverables

- The feed registry (version + access date)
- The connector implementations
- Materiality scoring and its rationale record
- Feed liveness monitoring

## Test and verification plan

- **Retraction:** when a test DOI is retracted, an `ImpactCase` opens
- **Cascade:** retracted source → span → claim → publication → citing works, end to end
- **Materiality:** a `material=false` decision without a rationale is rejected
- **Silent death:** if a feed does not run for N days, an alarm is raised
- Inbound feed content is subject to the `receiving-external-messages` rules

## Acceptance criteria

- [ ] A material signal cannot be logged and passed over; an `ImpactCase` is mandatory
- [ ] Every materiality decision carries a written rationale
- [ ] A feed cannot sit dead for months without being noticed
- [ ] The cascade chain is tested end to end
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Risks and control points

- If a feed dies silently, monitoring exists only on paper; the liveness check is non-waivable
- Feed content is untrusted and is subject to the WP-136 rules
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

The feed is stopped; open `ImpactCase`s are not closed and remain for human
decision. The missed monitoring window is recorded explicitly.

## Handoff into downstream packages

WP-108 (the retraction/drift vertical slice) consumes these feeds.
