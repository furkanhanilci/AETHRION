# Role and Responsibility Matrix

## Permanent programme functions

| Function | Accountable role | Responsibility |
|---|---|---|
| Research Strategy & Portfolio | Research Director | Value, portfolio, stop/pivot/continue |
| Scientific Discovery | Scientific Owner | Question, method, literature, interpretation |
| Engineering & Platform | Chief Architect / Platform Lead | System, contracts, execution and release |
| Evaluation & Assurance | Assurance Lead | Review, falsification, verifier, reproduction |
| Safety & Governance | Safety & Governance Owner | Risk, data, policy, exception and veto |
| Knowledge & Communication | Knowledge Lead | Source, Zotero, Obsidian, publication and archive |
| Operations & Economics | SRE Lead / FinOps Lead | SLO, incident, DR, capacity and cost |

### Proposed additional functions

The audit identified seven roles that exist in real research organisations and
are absent here. Full rationale in
`docs/architecture/AETHRION_IDEAL_STRUCTURE.md`.

| Function | Why it is needed | Can block |
|---|---|---|
| **Statistical Methods Owner** | `ProtocolManifest` contains statistical decisions with no owner | G2, G4, G6 |
| **Research Integrity Officer** | G6 lists a fabrication blocker with no process or owner behind it | any gate |
| **Data Steward** | The lab produces datasets; their lifecycle has no owner | G1, G9 |
| **Research Software Engineer** | Producing a result and packaging it reproducibly have opposed incentives | G7 |
| **Scientific Editor** | Overclaiming is the most consistent model failure mode | **G9** |
| **Red Team Lead** | Adversarial review is a task role, not a standing function | G4 |
| **Knowledge Steward** | Models carry no institutional memory across projects | G0 |
| **Metascience Lead** | Nothing measures whether the lab produces correct results | — (measures only) |

## Package role model

Every work package assigns at least:

- `A — Accountable`: sole owner of the acceptance or risk decision.
- `R — Responsible`: the implementer; there may be more than one.
- `V — Verifier`: independent of the producer; validates tests and evidence.
- `C — Consulted`: contract, security, scientific or operations specialist.
- `I — Informed`: downstream owners and programme management.

## Decision rights

| Decision | Accountable | Independent check | Delegable |
|---|---|---|---|
| ProjectCharter acceptance | Project Decision Owner | Research Director / Safety | Time-boxed at R1 |
| Protocol freeze | Scientific Owner | Methodologist / Statistician | No, for a material protocol |
| Literature set freeze | Evidence Lead | Citation Auditor / Methodologist | Broad delegation possible at R1 |
| Opening compute/budget | Scientific + FinOps Owner | Safety / Platform | Hard-limit override is not delegable |
| Review disposition | Assurance Lead | Mechanical verifier / Arbiter | No waiver for a critical blocker |
| Clean-room certificate | Reproduction Owner | Assurance Lead | Not delegable to the producer |
| Residual risk acceptance | Project Decision Owner | Safety / Assurance | Not delegable at R3 |
| Publication / release | Project Decision Owner | Provenance / Citation / Safety | Not delegable |
| Production cutover | Executive Sponsor + SRE/Safety | Commissioning Board | Not delegable |

## Role is a function, not a person

Every function below is bound through a `RoleBinding` carrying
`must_be_independent_from`, `can_combine_with` and `cannot_combine_with`. One
operator may legally hold several of them; **independence is a property of the
separation constraints, never of the headcount.**

```yaml
RoleBinding:
  role_id: statistical_methods_owner
  role_type: governance_function
  actor: {human: ..., model_profile: ..., mechanical: ...}   # any may be empty
  separation:
    must_be_independent_from: [experiment_analyst]
    can_combine_with:         [scientific_owner]
    cannot_combine_with:      [final_independent_verifier]
```

The binding is specified in **WP-013** and enforced by the compiler in
**WP-047**. Full definitions — mandate, decision rights, what each role may never
do, escalation and the combination matrix — are in
`docs/architecture/AETHRION_ROLES.md`.

**The two rows that bite in a one-person operation:** the Assurance Lead and the
Metascience Lead cannot be the producer. ADR-001 decides what follows.

### A cognitive function is not a governance function

Baseline v1.2.0 introduced task-specific specialist cognition — a methodologist,
a statistician, an experimentalist, a skeptic convened for one design problem
(WP-147). Those are **not** entries in the table above, and keeping them out of
it is the point.

Four independent axes, and the predictable defect is collapsing the first two:

| Concept | Answers | Carries authority? |
|---|---|---|
| **Governance function** | Who is accountable, and what may they never do? | **yes** — the table above |
| **Cognitive function** | What way of thinking is applied to this problem? | no — recommendations only |
| **Runtime actor** | What executes the work? | no |
| **Model profile** | Which model, at which snapshot, with which parameters? | no |

A `ScientificCouncilSession` emits a `Recommendation`. It cannot write a
`GateRecord`, a `ClaimVersion`, an `EvidenceSpan` or a `ReviewVerdict`, and that
is enforced by the authority matrix (WP-012) rather than expected of the reader.
**Seven council seats do not make twenty-one governance functions.**

One consequence is the case people get wrong: a council that shaped a protocol at
G2 is not a candidate reviewer for its result at G6. Reusing the function or the
model profile would let the design's own assumptions grade the design's own
output — the same principle ACC-06 applies to a planner approving its own plan,
and ACC-72 tests it here.

## Combining roles in a small team

The same person may wear several hats, provided the required independence
dimensions hold **for the same artifact**.

At R1, different model families, context isolation and separate credentials under
one person's oversight may be sufficient. At R3, full separation including the
human dimension is required for producer, reviewer and reproducer. Where that
cannot be achieved, the task stays `BLOCKED`.

> **Consequence for a solo operator.** Under the rule above, **every R3 project
> is permanently blocked** for a single-person organisation. That is a correct
> reading of the rule, not a loophole. Two responses are available and one must be
> chosen explicitly: reduce scope so that no in-scope package is R3, or define an
> alternative independence mechanism (a sealed-review protocol with measured
> model-family separation) and record it as a governance decision. Leaving the
> question open means the programme silently cannot complete.

## Escalation chain

```text
Implementer → Package Owner → Workstream Lead
            → Chief Architect / Assurance / Safety (by topic)
            → Project Decision Owner
            → Executive Sponsor / Commissioning Board
```

A timeout never converts into an automatic approval. When an SLA expires the
decision escalates one level or the workflow pauses.
