# Change and Configuration Control

## Baselines

The programme versions at least the following separately:

- Architecture decision bundle
- Role and policy contract bundle
- Event/schema bundle
- Infrastructure/IaC bundle
- Model capability/admission bundle
- Tool registry bundle
- Data/source/claim schema bundle
- Acceptance scenario bundle
- Production release candidate manifest
- **Skill bundle** — the execution discipline agents operate under

The skill bundle is versioned for the same reason as the policy bundle: it
changes agent behaviour, and a result produced under one version is not
comparable to one produced under another.

## Change classes

| Class | Example | Approval |
|---|---|---|
| Editorial | Clarification that does not change meaning | Package owner |
| Compatible | Backward-compatible optional field | Schema owner + contract test |
| Material | Gate, route, owner, retention or acceptance change | Architecture/Governance board |
| Critical | Trust zone, data boundary, canonical owner, blocker waiver | Decision Owner + Safety + Assurance |

## Change flow

```text
Change Request → Impact Scan → ADR/Schema Proposal → Independent Review
               → Decision → Implementation Packages → Regression/Replay
               → Baseline Promotion
```

An Impact Scan lists open workflows, frozen literature sets, claims, admission
profiles, runbooks and acceptance scenarios. A material change takes effect only
with a new baseline; prior decisions and artifacts remain unchanged.

## Configuration drift

- Production changes cannot be made outside GitOps; a break-glass change opens an
  incident and a reconciliation.
- A model alias change is not accepted as a pinned snapshot; requalification is
  required.
- Policy bundle rollback goes to a signed previous version and the decision log is
  preserved.
- Database migrations carry both a forward and a rollback/downgrade strategy; an
  irreversible migration is applied in two stages.
- External edits in Zotero and Obsidian do not automatically become truth in the
  canonical registries; ingest and reconciliation rules run.

## Plan file versioning

An accepted WP file is not modified retroactively. A new requirement adds a file
revision note and a change ID; the prior evidence manifest preserves which
revision it was accepted against.

> **Current applicability.** No package is currently `ACCEPTED`, so every plan
> file is still freely modifiable. This rule becomes binding from the first
> acceptance onward — which is also the point at which the plan stops being a
> draft.

## Progress is not the plan

Each work package records a **status at baseline** — the value frozen when the
baseline was sealed. It is history, and it never changes again.

**Execution state lives in `delivery/progress.json`, outside the seal.** This is
a deliberate separation, and the reason is the seal's own purpose: it proves the
*specification* did not change. If the status of a package lived inside the
sealed file, then starting work on it would invalidate the integrity proof of
the plan the work was against — every day's progress would look like tampering,
and the only way to keep the seal green would be to re-seal constantly, which is
the one prohibited use of it.

So:

| Question | Where it is answered | Sealed? |
|---|---|---|
| What was this package's status when the baseline froze? | The package document | Yes |
| What is its status **now**? | `delivery/progress.json` | No |
| What can be started today? | [`docs/READY.md`](../../../docs/READY.md), generated | No |

`scripts/ready_queue.py` computes the ready queue: a package is ready when its
status is `NOT_STARTED` and **every hard dependency is `ACCEPTED`**. Not
`TECH_COMPLETE` — issuance is not acceptance, and a dependency that has produced
something without being accepted does not release what depends on it. The queue
is short by construction, and it will stay short until the first acceptance.

## The baseline freeze dossier

Sealing the plan proves the specification did not change. It says nothing about
what was *built*, what was *measured*, or what a reader is entitled to believe
about either. A baseline freeze therefore produces a dossier, and the dossier is
an inventory rather than a narrative: every line is a reference to an artifact
that exists, or the line is not written.

| Element | What it pins | Absent means |
|---|---|---|
| Exact git commit and tag | The revision every other line refers to | Nothing below is addressable |
| Schema registry version | The contracts in force | A record validated against an unknown shape |
| WP and ACC inventory | What was in scope | Scope is whatever anyone remembers |
| Generated plan indexes | The derived views, regenerated at the tag | An index describing a different plan |
| Package dependency matrix | The order the work admits | A wave map with no evidence behind it |
| Skill registry versions | The discipline agents operated under | Results produced under two different disciplines, compared |
| Upstream assimilation manifest | Every mechanism taken from elsewhere, its licence and its pin | An obligation nobody can locate |
| SBOM | What is actually inside the artifact | A dependency list that is a guess |
| Vulnerability and Scorecard results | The known state of that inventory | "No known vulnerabilities" meaning "nobody looked" |
| Signed build and provenance attestation | Who built it, from what, on what | An artifact whose origin rests on trust |
| Model qualification snapshots | Which model, at which snapshot, qualified for which task type | A verdict from an unmeasured judge |
| External benchmark results | The comparable, published measurements | A capability claim with no external anchor |
| Internal acceptance results | ACC pass/fail on this candidate | Scenarios passed on some other revision |
| Known limitations | What does not work | A limitation discovered by a user instead |
| Unresolved risks | What is owned and still open | A risk register that closed itself |

### Five maturity words, and the distance between them

The dossier's most load-bearing rule is a vocabulary rule, because the failure it
prevents is the cheapest one in the world to commit: describing a capability at a
maturity it has not reached. **A `SPECIFIED` capability is never presented as
operational.** Release notes use exactly these words and never a synonym:

| Word | Means | Does **not** mean |
|---|---|---|
| `SPECIFIED` | A contract, schema or procedure is written | Any code exists |
| `CODED` | An implementation exists and runs | Anyone has checked it is right |
| `TESTED` | Positive **and** negative tests pass | An independent party looked |
| `ACCEPTED` | Acceptance scenarios passed on this candidate, witnessed | It has met anything outside this repository |
| `EXTERNAL_BENCHMARKED` | Measured on a benchmark this project did not write | The measurement was clean — see the contamination label |
| `MEASURED` | The quality/cost/latency/human-effort frontier is published for it | The numbers are targets that were met |

The gap between `TESTED` and `ACCEPTED` is an independent witness. The gap
between `ACCEPTED` and `EXTERNAL_BENCHMARKED` is a comparison this project does
not control. Both gaps are where a system's self-assessment is normally wrong,
and collapsing either of them into a single word called "done" is how that error
gets published.

> **Current state, stated in the same vocabulary.** Every capability in
> workstreams 14 and 15 is `SPECIFIED`. The Zotero bridge is `CODED` and
> partially `TESTED`. Nothing in this repository is `ACCEPTED`,
> `EXTERNAL_BENCHMARKED` or `MEASURED`, and the dossier above has never been
> produced, because there has been no release to freeze.


## Plan integrity — three checks, not one

The seal is necessary and **not sufficient**. Baseline v1.0.1 exists because
three defects survived it while every file was byte-identical to its sealed
state: colliding acceptance identifiers, a go-live requirement that depended on
post-go-live packages, and stale ranges.

| Check | Proves | Cannot see |
|---|---|---|
| `sha256sum -c` | sealed files did not change | whether they agree with each other |
| `validate_commissioning_plan.py` | references resolve both ways · the DAG is acyclic · phases are valid · go-live is feasible | whether the plan is a *good* plan |
| `check_doc_consistency.py` | declared counts match reality · no decision record contradicts its own status | anything outside the declared numbers |

**A plan change is complete only when all three pass** and the change is recorded
in the implementation log. Re-sealing to silence a failing check is the one
prohibited use of the seal.

**Not every idea is a plan change.** This plan is V1, and its scope is frozen at
the sealed baseline. An idea that *corrects* the plan — a wrong number, a false
claim, a broken reference — is a recorded change and follows the procedure above.
An idea that *adds* to it belongs in
[`docs/V2_CANDIDATES.md`](../../../docs/V2_CANDIDATES.md), which sits outside the
seal on purpose: a V2 candidate inside the V1 baseline would move the finish line
while appearing to be part of it.

**The current baseline is v1.3.3.** It is the third consecutive baseline that
is a **repair or refinement rather than an addition**, and it is worth being
precise about what that means. It adds no package, no scenario and no scientific
capability.
It makes the v1.3.0 architecture *executable*, which it was not:

- two packages required before go-live depended on Day-2 packages that only
  exist afterwards, so the programme had no valid starting order — and the
  dependency graph was acyclic the entire time, which is why nothing said so;
- the two cutover aggregators bound **two** acceptance scenarios while their own
  cards said the set was "derived, never enumerated", and the generated block —
  the surface an independent verifier actually works from — carried the two;
- the WP↔ACC relation had two owners that disagreed on 98 of 120 scenarios;
- the engineering discipline that governs the engineering path was sequenced
  after the vertical slice that demonstrates it;
- the wave figure rendered a package total nineteen short, deterministically,
  for two baselines.

None of that is visible in prose, and all of it is visible to a check. So
v1.3.1's real content is four new controls — the programme graph validator, the
figure semantic checker, the dynamic-fact rules and the document hygiene checker
— each carrying a self-test that reproduces the defect it was written for.

By the rule in §*Not every idea is a plan change*, this is a **correction**: the
finish line is where v1.3.0 left it. The go-live checklist gained no entry
condition. What changed is that the conditions already there can now be
evaluated.

**The baseline before it was v1.3.0.** It added the reliability and efficiency
workstream — WP-148–159 and ACC-081–120 — and, like v1.2.0 before it, it was an
**addition** rather than a refinement: it moved the finish line, and
`00_PROGRAM/10_go_live_checklist.md` gained entry conditions accordingly. That
is recorded here in the same words used for every other change, because a
baseline that moves the finish line while calling itself a refinement is the
single most expensive kind of undocumented change a plan can carry.

**The baseline before it was v1.2.0**, which opened the scientific-intelligence
workstream (WP-141–147, ACC-052–080) on the same terms.

**Before that, v1.1.0.** It is the largest recorded change so far and it is a **refinement, not an addition**: the finish line — `00_PROGRAM/10_go_live_checklist.md`'s entry conditions — is unmoved, and no package, scenario, dependency or acceptance phase was added or removed. What changed is that every package is now **three documents** (§4): the card, its test procedures and its acceptance criteria. `00_PROGRAM/05` already required this — *a package is genuinely `READY` when its criteria name a number, a threshold or a command* — and the generic template criteria did not. The split also makes the verifier's packet handable, which `00_PROGRAM/06` requires and a criteria section living inside the producer's working card cannot be.

**The previous baseline was v1.0.5.** v1.0.2 carried the project's name change to
AETHRION across 29 files; v1.0.3 corrected three programme documents that claimed
the evidence manifest is recorded in a public transparency log — it is not — and
that still called finding C2 an open decision after ADR-001 decided it. It is the worked example of the rule above: the change
was naming only, the seal was regenerated deliberately rather than to quiet a
failure, all three checks were re-run afterwards, and the reason is written down
here and in the implementation log. A reader can confirm the claim rather than
trust it — `git diff v1.0.1..v1.0.3 -- planning/` shows no requirement,
identifier, dependency, acceptance phase or scenario was touched.

## Plan integrity

The canonical plan is sealed:

```bash
sha256sum -c planning/commissioning/00_PROGRAM/SHA256SUMS.txt
```

Every entry must report `OK`. A mismatch means a plan file changed without the
seal being regenerated. The seal is regenerated deliberately, as part of a
recorded change — never as a routine step to silence a failing check.

The Obsidian mirror is a **generated** reading copy. Plan content changes in the
canonical file first, then propagates. Editing the mirror directly creates a
divergence that the seal will not detect, because the seal does not cover the
mirror.
