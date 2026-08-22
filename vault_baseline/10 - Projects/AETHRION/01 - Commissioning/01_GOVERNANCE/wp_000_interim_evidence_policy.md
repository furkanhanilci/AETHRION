# WP-000 — Interim Evidence Policy and Attestation Bootstrap

## Package card

| Field | Value |
|---|---|
| Work package | `WP-000` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **S** — small — one owner, one review cycle |
| Accountable owner | Project Decision Owner |
| Independent verifier | Assurance Lead |
| Hard dependencies | — **none, and none is permitted.** A bootstrap package that depends on a downstream package reproduces the deadlock it exists to break |
| Related gates | Program (applies to every gate's evidence requirement) |
| Related controls | CTL-GOV-01, CTL-EPI-01 |
| Related acceptance scenarios | ACC-06 |
| Current status | `TECH_COMPLETE` — tooling implemented, specimen issued and verified; acceptance awaits the verifier arrangement in ADR-001 |

## Purpose and expected outcome

Every Definition of Done requires a signed `EvidenceManifest` held in an
immutable store. That store is delivered by **WP-026**, which sits several
dependency levels downstream of WP-001. As written, **no package can be
`ACCEPTED` — including the first one — so the programme cannot start.** This is
audit finding **C1**.

This package resolves the deadlock by **delegating immutability to existing
public infrastructure instead of building it first**. On completion, a work
package can produce evidence that a verifier can check, that no participant can
retroactively alter, and that requires no trusted third party of the programme's
own.

## Out of scope

- The permanent content-addressed WORM store (**WP-026**), which supersedes this
  policy's storage arrangement without invalidating anything issued under it
- The Claim/Evidence Ledger (**WP-075**)
- **The independence question.** This package makes evidence *tamper-evident*;
  it does **not** decide who may act as an independent verifier in a small
  organisation. That is finding **C2** and remains open. Adopting the attestation
  standards below does not close it, and this package must not be read as if it did.

## Execution record — 2026-08-22

The interim profile is implemented in `scripts/evidence_manifest.py`, and a
specimen manifest for this package exists at `delivery/WP-000/`:

```
signature           OK
subject digest      OK   README.md
subject digest      OK   planning/commissioning/00_PROGRAM/SHA256SUMS.txt
subject digest      OK   planning/commissioning/01_GOVERNANCE/WP-000_interim_evidence_policy.md
time anchor         OK   (interim/local)
payload altered     rejected, as required
```

Both tamper paths are exercised by `tests/test_evidence_manifest.py`: altering a
covered file fails the digest check, and forging the signature fails the envelope
check. Verification exits `1` in both cases.

> **What is implemented is narrower than the target, and the manifest says so.**
> The in-toto Statement and the DSSE envelope are as specified; the signature is
> a **local Ed25519 key** rather than Sigstore keyless, and the attestation is
> **not submitted to a transparency log** — keyless signing needs an interactive
> OIDC flow this environment does not have. The manifest records
> `attestation_profile: airl-interim-v0.1` and carries its own `limitations`
> list, so no reader can mistake it for the full profile. Moving to Sigstore and
> Rekor is the remaining work in this package.

## Interim evidence format

The `EvidenceManifest` is expressed as an **in-toto Statement (ITE-6)**, wrapped
in a **DSSE** envelope, signed through **Sigstore** with a short-lived
OIDC-bound certificate, and recorded in the **Rekor** transparency log.

> **Rekor is a tamper-evident transparency record for signed metadata — not an
> artifact store.** It holds the attestation and its inclusion proof; the
> artifacts, the Sigstore bundle, the certificate chain and the verification
> material still need durable storage. **WP-026 is not cancelled by this
> package**; it is deferred behind it.

**Timestamping is owned here, temporarily.** This package implements its own
minimal external time anchor so that it depends on nothing. **WP-139** later
assumes permanent ownership of timestamping, and this package's implementation
is retired into it — the direction of the dependency is WP-139 → WP-000, never
the reverse.

```
subject:       [{name: <artifact>, digest: {sha256: <hex>}}]
predicateType: https://airl-os.local/EvidenceManifest/v0.1
predicate:
  work_package:     WP-nnn
  gate:             <gate id>
  target_revision:  <git sha / image digest>
  tests:            [{name, result, revision}]
  environment:      {os, runtime, dependency digests}
  schema_versions:  {...}
  policy_versions:  {...}
  verifier:         {identity, decision, timestamp}
  findings_open:    [{id, severity, owner, expiry}]
  residual_risk:    <text>
```

Rationale for adopting rather than inventing is recorded in
`docs/architecture/AETHRION_EXTERNAL_STANDARDS.md` §3.

## Preconditions — Definition of Ready

- A named owner and a verifier **independent of the producer** are assigned, under
  the interim independence arrangement recorded in this package.
- The signing identity provider and the transparency log endpoint are reachable.
- The `predicateType` URI and the predicate schema are fixed and versioned.
- The migration path into WP-026 is written down before the first manifest is issued.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-000-T01 | Fix the `EvidenceManifest` predicate schema and its versioning rule | Implementation owner | Schema file + version record |
| WP-000-T02 | Implement manifest generation, DSSE signing and log submission | Implementation owner | Script + a signed specimen manifest |
| WP-000-T03 | Implement verification: signature, inclusion proof, digest match | Implementation owner | Verification run over the specimen |
| WP-000-T04 | Implement the **interim** external time anchor here — no dependency on WP-139 — and record the anchor reference | Implementation owner | Anchor receipt |
| WP-000-T05 | Write the interim independence and verifier arrangement, with its expiry | Project Decision Owner | Signed policy record |
| WP-000-T06 | Write the WP-026 migration and retirement procedure for this policy | Implementation owner | Migration note |

## Mandatory deliverables

- `Interim Evidence Policy` — a signed governance record with an explicit expiry
- The interim timestamping implementation, owned by this package
- `EvidenceManifest` predicate schema, versioned
- Generation, signing and verification tooling
- One end-to-end specimen manifest, signed, logged, anchored and verified
- The WP-026 migration and retirement procedure
- A signed `EvidenceManifest` **for this package itself** — issued under the
  policy it defines, which is the bootstrap step

## Test and verification plan

- A manifest whose payload is altered after signing **fails** verification
- A manifest whose subject digest does not match the artefact **fails**
- A manifest absent from the transparency log **fails**, even with a valid signature
- Verification succeeds offline against a stored inclusion proof
- The independent verifier can complete verification **without** the producer's tooling
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] An `EvidenceManifest` can be issued, signed, logged, anchored and verified end to end.
- [ ] A tampered manifest is rejected by the verification path.
- [ ] The programme's first packages can reach `ACCEPTED` **without** WP-026.
- [ ] The policy carries an explicit expiry and a named retirement package.
- [ ] The package depends on **no** downstream package, and its timestamping runs without WP-139.
- [ ] The C2 independence question is **restated as still open** in the policy text, not silently absorbed.
- [ ] All mandatory tests passed **on the same target revision**.
- [ ] No open Critical or High findings; no non-waivable blocker remains.
- [ ] The independent verifier has accepted the evidence package.

## Acceptance evidence package

- Test results captured on the same target revision/digest
- The specimen `EvidenceManifest` with its log entry and anchor references
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- **A policy that never expires becomes the permanent architecture.** The expiry
  date and the retirement package are part of the deliverable, not commentary.
- Public log submission publishes **hashes and metadata**. Manifest predicates
  must therefore stay at data class **D0/D1**; no D2+ content may enter a
  predicate. This is a non-waivable constraint of using a public log.
- Reachability of an external log is an availability dependency. An offline
  fallback — locally signed, anchored later — must be defined, and a manifest
  awaiting anchoring is **not** yet acceptance evidence.
- Adopting an attestation standard **does not** create independence. Using it to
  imply C2 is resolved would be exactly the overstatement the audit warned about.
- A "package complete" statement is **not** acceptance. Without a verifier
  decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

Manifests already issued and logged are **never** withdrawn; a superseding
manifest is issued and the earlier entry remains as the historical record. If
the interim policy is retired early, packages accepted under it retain their
acceptance and their manifests migrate into WP-026 by reference.

## Handoff into downstream packages

On acceptance, every package in the programme gains a usable acceptance path.
WP-026 consumes this package's manifests by reference and does not re-issue them;
WP-075 links claims to them; **WP-139 takes over timestamping from this package
and retires the interim implementation.**

This package is the **bootstrap phase**. WP-001 remains the first *normal*
commissioning package: no technology installation begins before WP-001 is
accepted, and WP-001 cannot be accepted before this package exists.
