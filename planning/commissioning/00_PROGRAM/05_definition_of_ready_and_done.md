# Definition of Ready and Definition of Done

## Definition of Ready — all packages

A package becomes `READY` only when all of the following hold:

- The package purpose and its single delivery boundary are clear.
- Out-of-scope items are written down.
- An Accountable Owner, an implementer and an independent verifier are assigned.
- Hard dependencies are `ACCEPTED`, or in an explicitly permitted mock-contract
  state.
- Affected canonical owners and interfaces are identified.
- DataClass, ToolEffect, CodeTrust and network/credential scope are classified.
- **The acquisition surface is classified and its obligations are resolved.** Every
  part of the package is one of `DEPENDENCY`, `ADAPTER`, `OPTIONAL_BACKEND`,
  `STANDARD`, `BENCHMARK`, `PATTERN`, `DIRECT_ADAPT`, `ADAPTIVE_REIMPLEMENT` or
  `BUILD_NATIVE`, recorded in `provenance/upstreams.json` or
  `provenance/components.json` and projected into the package's own
  **Implementation acquisition and assimilation** block.
- Required environments and test fixtures are accessible.
- Acceptance criteria are **measurable** and the owner of the test command or
  scenario is identified.
- Migration, rollback or compensation behaviour is defined.
- A three-point effort estimate and a capacity owner exist.
- Open blockers and assumptions are visible.

> **On acquisition, and why it gates `READY` rather than `TECH_COMPLETE`.**
> `READY` means an implementer may start. An implementer who starts against a
> `DIRECT_ADAPT` source with no pinned commit, no selected file list and no
> characterisation suite has two options and both are wrong: copy code that
> `ADR-004` has not permitted to move, or rewrite from scratch a mechanism the
> architecture already decided to take. The same holds for an
> `ADAPTIVE_REIMPLEMENT` source with no written mechanism specification — two
> implementers will read the paper differently and neither will be checkable
> against the other — and for an `OPTIONAL_BACKEND` nobody has chosen, where the
> backend ends up being whichever one a table happened to name first.
>
> `BUILD_NATIVE` is an answer, not an absence. It has to be *recorded* as the
> classification, because silence cannot distinguish a package with no upstream
> from a package whose upstream nobody wrote down — and the second is what
> `WP-144` looked like while AIDE sat in the register, unnamed by the package
> that was supposed to adapt it.
>
> `scripts/ready_queue.py` holds a package out of *Ready now* while any
> obligation is open and lists it under *Held — acquisition unresolved*, so the
> distinction is visible rather than remembered.

> **On measurability.** The generic criteria in the current package template
> ("all mandatory tests have passed") are not measurable in the sense meant here.
> A package is genuinely `READY` when its criteria name a number, a threshold or
> a command. Refinement is where that specificity is added; without it the
> package cannot be closed objectively.

## Technical completion

`TECH_COMPLETE` states only that the implementation is ready:

- Code, policy, schema and IaC are ready for review.
- Unit and package-level integration tests have run.
- Required migration and rollback dry runs have been performed.
- Telemetry, correlation and audit signals are in place.
- Documentation and runbook changes are committed.
- A draft evidence manifest exists.

## Definition of Done — package acceptance

- All acceptance criteria passed **on the same target revision**.
- Test results are bound to artifact hashes and an environment manifest.
- The verifier performed verification **independently of the producer**.
- Security, data and policy negative tests passed.
- Contract compatibility and downstream consumer tests are green.
- No open critical or high findings; accepted medium/low risks carry a named
  owner and an expiry.
- Rollback or compensation behaviour was exercised at least once.
- Working evidence exists via an observability dashboard, alert or audit query.
- The evidence manifest is signed and written to an immutable store.
- The package status is `ACCEPTED`; once the dependent vertical slice passes it
  is recorded as `INTEGRATED`.

> **Bootstrap constraint.** The last item requires an immutable store, delivered
> by WP-026, which itself sits several dependency levels downstream of WP-001.
> As written, no package can satisfy this — including the first one. An interim
> evidence policy defining a temporary, externally time-anchored evidence store
> is a precondition for the programme starting at all. Written as
> [**WP-000**](../01_GOVERNANCE/WP-000_interim_evidence_policy.md); the
> timestamping mechanism it needs is **WP-139**.
>
> WP-000 resolves the **storage** half of the deadlock by expressing the
> `EvidenceManifest` as a signed in-toto attestation with an external time
> anchor, rather than by building an immutable store first. The profile in force
> is `airl-interim-v0.1`: a local signing key and a local anchor, **not** a
> transparency log and **not** keyless — WP-139 supplies those. The **other**
> half, finding **C2**, is decided by
> [`ADR-001`](../../../docs/architecture/ADR-001_solo_operator_independence.md):
> R1 solo, R2 declared partial, R3 `BLOCKED`.

## Definition of Done for a change to the architecture itself

The sections above define done for a *work package*. A change to the
architecture — a new decision record, a new invariant, a mechanism assimilated
from elsewhere — is a different object, and it fails in a different way: it is
declared complete when the idea has been written down and nothing else has moved
with it. Ten conditions, and the item is `DONE` only when every one holds.

| # | Condition | The failure it prevents |
|---:|---|---|
| 1 | The semantic requirement exists in the canonical architecture | A decision that lives only in the delta document that proposed it |
| 2 | A contract or schema exists wherever the state is durable | A record whose shape is agreed in prose and nowhere else |
| 3 | A runtime implementation exists **if the current milestone includes one** | Either an unimplemented claim, or a demand for code the phase does not call for |
| 4 | Positive **and** negative tests exist | A control nobody has watched refuse |
| 5 | The work package's card, tests and acceptance documents all reflect it | Three documents that describe three different requirements |
| 6 | An acceptance scenario exists, or the acceptance evidence is named explicitly | A requirement that can never be shown to have been met |
| 7 | Telemetry or audit evidence is emitted | A behaviour that is correct and invisible |
| 8 | Documents and figures are not stale | A diagram that contradicts the decision it illustrates |
| 9 | Source and licence provenance is complete | An obligation attached to code nobody can trace |
| 10 | The generators, checks and seal are green | A baseline whose own tooling disagrees with it |

Condition 3 carries the qualifier deliberately. Most of what this repository
currently holds is `SPECIFIED` — see the maturity vocabulary in
[`09_change_and_configuration_control.md`](09_change_and_configuration_control.md).
Demanding a runtime for every architectural item would make every item
permanently `NOT_DONE` and the definition useless; dropping the condition
entirely would let a system describe itself as built. The qualifier is what makes
the word `DONE` mean something at each phase without meaning the same thing.

Condition 4 is the one most often skipped, and it is skipped because a negative
test looks like paranoia until the day the control is quietly broken. The
repository already treats it as non-negotiable — `monitor_sources.py` exits
non-zero when its planted retracted DOI goes undetected, and both
`check_upstream_lineage.py --self-test` and `check_stale_claims.py --self-test`
report any rule that stays silent on the input written to trip it.

### The final audit is a search for wording, and it is mechanical

The last condition a baseline must satisfy before it freezes is that no document
still says something the architecture has made wrong. This is not the same as a
stale count. A count drifts; **a regression contradicts a decision**, and it does
it in prose that reads perfectly well.

Eight wordings are searched for, each because it inverts a specific decision
record:

| Wording | Decision it contradicts |
|---|---|
| A single-agent default for substantial work | `ADR-011` — the cohort is an epistemic requirement, not a capability one |
| A fully-connected topology presented as the target | `ADR-013` — fully-connected is the measurement baseline; the target is the compiled sparse topology |
| "Mechanical verifier" used for a semantic model check | `ADR-008` — a semantic check is V2 and yields a finding with a measured error rate |
| A timeout that approves | `ADR-016` — a timeout escalates, through every interface |
| Publication prose with no `ClaimVersion` binding | `ADR-009` — an assertion binds a claim version, and a number resolves to a `VerifiedValue` |
| A NATS event treated as authority | `ADR-014` — an event announces; the canonical store is re-read |
| Neo4j or a vector store called canonical memory | `ADR-014` and `ADR-005` — every index is a projection that can be destroyed and rebuilt |
| The engineering skills described as merely bootstrap tooling | `ADR-012` — it is a discipline, and a large share of the science's failure modes live in it |

**Every one of those phrases already appears in this repository, inside a
sentence that forbids it.** That is what makes a hand search useless: the grep
returns a wall of correct prose, the auditor stops reading it, and the one
affirmative use is in the middle of the wall. So the search is implemented in
`scripts/check_stale_claims.py` as a third rule family with two guards — a
paragraph-level prohibition marker and a local negation check on the words
immediately before the match — and each rule ships with a specimen that must trip
it and a specimen that must not. Both halves are bound to the suite in
`tests/test_architectural_regressions.py`.

The rules are narrower than the concept, and the gap is stated rather than
implied: an author who asserts a regression inside a paragraph that happens to
refuse something else escapes the rule. That is a smaller gap than not looking,
and it is why the checker prints its rule count on every run — so a reader can
see how much of "nothing is stale" the passing line actually covers.

## Definition of Commissioned

An `ACCEPTED` package is still not production-ready. To become `COMMISSIONED`,
every acceptance scenario that uses the package must pass **on the same release
candidate**. A `SKIPPED` scenario on a critical package does not count as a pass.

## Evidence that is not accepted

- An agent's or implementer's free-text declaration of success.
- Test outputs from different revisions mixed together.
- A screenshot with no hash or environment information.
- An independence claim from a reviewer who saw the producer's trace.
- A test passing against a mock presented as a real integration test.
- A happy-path demonstration only.
- A confidence number with no measurement behind it.

Added by baseline v1.2.0, each because it is a form of evidence that looks
complete and establishes nothing:

- **A clean detector report from a suite whose planted control stayed silent.**
  "No findings" and "no detector" are the same sentence otherwise.
- **A published number that does not resolve to an immutable evaluator output.**
  A figure typed into prose is not a measurement, however accurate it happens to
  be.
- **A semantic verdict from a verifier with no current qualification** for that
  task type at that threshold. A judge that has never been measured is an opinion
  with institutional weight.
- **A reproduction run in the producer's environment**, or by an agent that also
  produced the result. That reproduces the environment, not the finding.
- **A hypothesis marked refuted by a run that failed to execute.** Only a validly
  executed run under the frozen plan can support a `HYPOTHESIS` failure class.
- **A confirmatory claim whose analysis plan was sealed after its first
  outcome**, whatever the plan says.
- **Adapted upstream code with no pinned commit and no characterisation suite.**
  Nothing distinguishes it from a mechanism that was misunderstood.
- **A checker that has never been observed to fail.** Every control in the
  bundle is expected to be demonstrable in both directions.
