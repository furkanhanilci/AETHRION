# Evidence and Acceptance Strategy

## Evidence manifest

Every package produces an `EvidenceManifest` carrying at minimum:

```yaml
package_id: WP-xxx
target_revision: sha256-or-git-commit
environment_manifest: artifact-ref
policy_bundle: git-digest
schema_bundle: git-digest
test_results: []
security_results: []
contract_results: []
rollback_result: artifact-ref
review_records: []
open_findings: []
owner_decision: decision-id
created_at: timestamp
signature: sigstore-ref
external_timestamp: ots-ref        # WP-139 — independent time anchor
```

The `external_timestamp` field matters more than it appears. Every other field
in this manifest is verifiable only by someone who already trusts this system.
An external time anchor is the one piece of evidence that survives that
assumption being dropped.

## Evidence layers

| Layer | Question | Example |
|---|---|---|
| E0 Structural | Does the file, schema or reference exist? | JSON Schema validation, hash verification |
| E1 Mechanical | Is the behaviour correct under a deterministic test? | Unit, integration, policy tests |
| E2 Security | Is the forbidden path actually blocked? | Negative route, egress, permission tests |
| E3 Independent review | Did an actor outside the producer examine the semantics? | Blind `ReviewRecord` |
| E4 Reproduction | Does the same package run again in a clean environment? | `ReproductionReport` |
| E5 Operations | Are failure, restore and observability correct? | Chaos / DR / SLO evidence |

Which layers are required varies with package risk, but on critical packages the
applicable layers among E0–E5 cannot be waived.

**Cheap layers run first.** E1 mechanical checks cost seconds; E3 independent
review costs a reviewer's attention. Running them in the wrong order wastes the
expensive resource on problems the cheap one would have caught.

### E1 is two things, and baseline v1.2.0 separated them

The layer above reads "mechanical" as one category. For evidence *about the
repository* — does this file exist, does this digest match, does this policy test
pass — that is right. For evidence *about research*, the word was covering two
incompatible kinds of check, and `ADR-008` splits them:

| Class | What it is | Failure semantics |
|---|---|---|
| **V0** | Deterministic — digest, schema, signature, reference resolution | **Non-waivable.** Same input, same answer, always |
| **V1** | Computational or statistical — score recomputation, statistical test, tolerance | **Non-waivable**, given pinned software and configuration |
| **V2** | Model-mediated semantic — citation entailment, claim scope, method–code alignment | A **finding** with a measured error rate, routed to review. Requires a current qualification |
| **V3** | Human scientific judgement | Authority, not throughput |

The reason this matters to the evidence strategy rather than only to the
architecture: the rule *a mechanical check runs first and cannot be overridden by
a model* is correct for V0 and V1, and absurd at V2, where it says a model's
judgement cannot be overridden by a model. **A verification result carries its
class**, assigned by the verifier service from the procedure that actually ran —
never by the caller.

### A control that has never refused is not evidence

Every critical detector carries a **known-positive that must fail** and a
**known-negative that must pass**, in the same run that produces its clean
result. A suite in which a planted control stays silent fails, regardless of what
it reports.

This is not a new principle here — `scripts/monitor_sources.py` has always exited
non-zero when its planted retracted DOI went undetected. Baseline v1.2.0
generalises it to every verifier, and `check_upstream_lineage.py --self-test` is
the pattern applied to a checker's own rule set.

## Finding lifecycle

```text
REPORTED → STRUCTURALLY_VALID → REPRODUCED → VALIDATED
         ↘ NOT_REPRODUCIBLE / DUPLICATE / OUT_OF_SCOPE
VALIDATED → FIXED → REVERIFIED → CLOSED
```

A correction is opened only for `VALIDATED` findings. A critical finding cannot
be closed as "probably a false positive" — a reproducer result is required.

Every finding must reach a terminal state. A finding that is neither closed nor
explicitly parked with an owner and an expiry has not been handled; it has been
forgotten. See the finding-ledger requirement in
`skills/arbitrating-disagreement`.

## Acceptance levels

- **Package Acceptance:** the package's own contracts and tests.
- **Integration Acceptance:** the real interface between two or more services.
- **Vertical Slice Acceptance:** the business outcome across the relevant portion
  of G0–G10.
- **System Commissioning:** ACC-01–ACC-120, the attack suite, DR and capacity.
- **Human Go-Live Decision:** an authorised decision taken by someone who has
  seen the evidence summary and the residual risk.

## Traceability

Every requirement is bound as `REQ-*`, every control as `CTL-*`, every work
package as `WP-*`, every test as `TST-*`, every acceptance scenario as `ACC-*`,
every finding as `FND-*` and every decision as `DEC-*`.

The go-live dossier must be able to answer the query
`REQ → WP → TST/ACC → Evidence → Decision` for any requirement.

> **Current state.** The WP↔ACC mapping exists in two places — the dependency
> matrix and the ACC documents — with different, undocumented semantics. Until
> one is designated authoritative and the other generated from it, the
> `COMMISSIONED` rule cannot be evaluated mechanically. See finding **M5** in the
> audit report.
