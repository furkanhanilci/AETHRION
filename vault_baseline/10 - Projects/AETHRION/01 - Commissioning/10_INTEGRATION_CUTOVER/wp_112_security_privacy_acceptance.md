---
title: "WP-112 — Security and Privacy Acceptance Package"
aliases:
  - "WP-112"
  - "WP-112 — Security and Privacy Acceptance Package"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Sandbox escape, egress exfiltration, unsigned images, D3 routing, policy rollback and expiry, forged approval, secrets in traces, evaluation contamination and audit tampering all close fail-closed."
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-112_security_privacy_acceptance.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/commissioning
  - aethrion/state/not-started
---

# WP-112 — Security and Privacy Acceptance Package

## Package card

| Field | Value |
|---|---|
| Work package | `WP-112` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Independent Red Team / Privacy Reviewer |
| Hard dependencies | WP-060, WP-109 |
| Related gates | Commissioning |
| Related controls | CTL-SEC-01..05, CTL-OBS-02 |
| Related acceptance scenarios | ACC-15..18, ACC-24..26, ACC-32, ACC-37, ACC-40 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_112_security_privacy_acceptance.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_112_security_privacy_acceptance.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Sandbox escape, egress exfiltration, unsigned images, D3 routing, policy rollback and expiry, forged approval, secrets in traces, evaluation contamination and audit tampering all close fail-closed.


## Analysis
### What this package actually decides

Whether every security control **fails closed** under attack. Ten scenarios, and
the acceptance bar is stated in the purpose: *all close fail-closed.*

### Fail-closed is the specific property, not "the attack failed"

An attack that fails because the attacker made a mistake is not evidence. An attack
that fails because the control denied it, contained it, revoked the lease and opened
an incident is. Every scenario here declares which of **deny / contain / detect /
respond** it expects, and a weaker outcome than expected is a finding.

### `ACC-24` forged approval is the epistemic attack in this set

Sandbox escape and exfiltration are technical. A forged approval attacks the
decision record itself — and if it succeeds, every downstream claim rests on an
authorisation that never happened. WP-055's decision-actor binding and WP-038's
authenticated Update are what must hold.

### `ACC-37` evaluation contamination is the one that fails silently

A contaminated golden set does not error. The metric improves, and improvement is
never investigated. The canary is the only detection, and this scenario is where the
canary must be shown firing.

### `ACC-40` audit tampering closes the loop on the whole system

If the audit record can be altered, every other result in the programme is
unfalsifiable. WP-099's hash chain must break, and the break must name its position.

### Every critical finding is corrected and retested (T05)

Not triaged. `00_PROGRAM/07` places security blockers outside the waiver mechanism,
so a security scenario with an open critical finding does not sign.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/wp_060_security_attack_suite.md) | `Agentic attack suite` · `Malicious fixture corpus` · `Red-team report template` · `Security regression schedule` |
| [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/wp_109_acceptance_registry.md) | `Acceptance Registry` · `Scenario runner` · `Fixture catalog` · `Evidence capture/signing` |

### Full prerequisite closure

**109 of 141 packages (77%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` · `WP-037` · `WP-039` · `WP-045` |
| 22 | `WP-034` · `WP-038` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-036` · `WP-048` · `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-040` · `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-059` · `WP-061` · `WP-092` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-060` · `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` · `WP-098` |
| 33 | `WP-073` · `WP-077` · `WP-078` · `WP-094` · `WP-101` |
| 34 | `WP-074` · `WP-079` · `WP-085` · `WP-103` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-090` · `WP-093` |
| 41 | `WP-095` · `WP-102` · `WP-107` |
| 42 | `WP-104` |
| 43 | `WP-105` |
| 44 | `WP-106` |
| 45 | `WP-108` |
| 46 | `WP-109` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-115` · `WP-123`
- **Transitively reachable:** **16 of 141 packages (11%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W6 — Vertical integration |
| Dependency depth | level **47** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Independent Red Team / Privacy Reviewer |
| Gates touched | `Commissioning` |
| Controls | `CTL-SEC-01..05` · `CTL-OBS-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-15 — Sandbox Escape Attempt](../12_ACCEPTANCE_SCENARIOS/acc_15_sandbox_escape.md) | Critical | Every escape path is denied or contained; no credential or host data leaks, the cell is stopped and a forensic `SecurityEvent` is produced. |
| [ACC-24 — Policy Bundle Rollback](../12_ACCEPTANCE_SCENARIOS/acc_24_policy_bundle_rollback.md) | High | The previous bundle is restored atomically, decision logs and bundle digests are preserved, open tasks are re-evaluated and no unsafe temporary allow is granted. |
| [ACC-32 — Secret in Prompt or Trace](../12_ACCEPTANCE_SCENARIOS/acc_32_secret_in_trace.md) | Critical | The secret never appears in raw telemetry, events or the UI; redaction or quarantine occurs, a security event is raised and the credential is revoked. |
| [ACC-37 — Evaluation Set Contamination](../12_ACCEPTANCE_SCENARIOS/acc_37_eval_contamination.md) | Critical | The evaluation bundle is invalidated; the qualification and profile decisions that depended on it are suspended, and a clean set and re-evaluation process opens. |
| [ACC-40 — Complete Project Audit Export](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) | Critical | The signed export verifies with complete correlation and hash chain; a missing or tampered fixture fails verification and raises an incident. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/wp_060_security_attack_suite.md), [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/wp_109_acceptance_registry.md)
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
| `Agentic attack suite` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Malicious fixture corpus` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Red-team report template` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Security regression schedule` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Acceptance Registry` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Scenario runner` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Fixture catalog` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Evidence capture/signing` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Result dashboard` | `WP-109` | `python3 scripts/progress.py show WP-109` |

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
- **Safety & Governance Owner** carries the acceptance decision; **Independent Red Team / Privacy Reviewer** must verify independently of whoever implements.
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
| WP-112-T01 | Prepare the security acceptance fixtures and attack identities | Implementation owner | Commit / configuration / record reference |
| WP-112-T02 | Run the security paths behind ACC-15–18, 24–26, 32, 37 and 40 | Implementation owner | Commit / configuration / record reference |
| WP-112-T03 | Verify the deny, contain, lease-revoke, incident and audit assertions | Implementation owner | Commit / configuration / record reference |
| WP-112-T04 | Review the forensic artifacts and the alert/runbook response | Implementation owner | Commit / configuration / record reference |
| WP-112-T05 | Correct and retest every critical finding | Implementation owner | Commit / configuration / record reference |
| WP-112-T06 | Sign the security acceptance statement | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Security scenario results`
- `Red-team report`
- `Forensic evidence`
- `Security acceptance statement`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-112_security_privacy_acceptance.tests.md`](wp_112_security_privacy_acceptance.tests.md).

- ACC-15, 16, 17, 18, 24, 25, 26, 32, 37 and 40
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-112_security_privacy_acceptance.acceptance.md`](wp_112_security_privacy_acceptance.acceptance.md), together with what this package still cannot establish.

- [ ] Every critical attack is denied or contained **and** produces audit evidence.
- [ ] D3/D4 violations = 0.
- [ ] Unsigned artifacts in production = 0.
- [ ] Open critical and high security findings = 0.
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

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

A failure blocks production access and cutover; compromised credentials and artifacts are revoked immediately.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
