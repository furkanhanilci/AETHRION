# Evidence Index

Test, acceptance, hash, artifact, review and operational evidence.

> **The rule:** a WP or ACC without evidence is never counted `IMPLEMENTED`.
> And the evidence must be **fresh** — evidence quoted from memory or from an
> agent's report is not evidence. See [[verification-before-completion]].

## Evidence records

| Record | Date | Scope |
|---|---|---|
| [[10 - Projects/AI Research Framework/05 - Evidence/2026-08-22_framework_audit_evidence\|Framework Audit Evidence]] | 2026-08-22 | Tests, hashes, plan integrity, service status |

## Measurements produced by the repository about itself

| Measurement | Result | Where |
|---|---|---|
| Reference verification — CoE Audit check 1 | **27/33 corroborated (81.8 %)** | `delivery/measurements/reference_verification.json` |
| Source monitoring — first slice of G10 | 15 of 33 swept, 0 material signals, **positive control fired** | `delivery/measurements/source_monitoring.json` |
| WP-000 attestation | signature, digests and anchor verify; both tamper paths rejected | `delivery/WP-000/` |

> A clean monitoring report proves nothing unless the check can fire, which is
> why every run carries a known-retracted control and fails if it stays silent.

## Sub-areas

- `tests/` — unit, contract and integration output
- `acceptance/` — ACC-01–ACC-51 results (none has ever been run)
- `artifacts/` — manifest, digest and provenance records
- `reviews/` — independent review reports
- `operations/` — service, deployment and readiness evidence

## Evidence layers

| Layer | Question |
|---|---|
| E0 Structural | Does the file, schema or reference exist? |
| E1 Mechanical | Is the behaviour correct under a deterministic test? |
| E2 Security | Is the forbidden path actually blocked? |
| E3 Independent review | Did an actor outside the producer examine it? |
| E4 Reproduction | Does it run again in a clean environment? |
| E5 Operations | Are failure, restore and observability correct? |

## What is missing

`acceptance/` is empty — none of ACC-01 to ACC-40 has been automated.
The first candidate: **ACC-22 (Obsidian Human Edit Preservation)** — the existing
test already does half of it.
