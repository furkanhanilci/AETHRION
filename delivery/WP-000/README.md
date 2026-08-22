# WP-000 evidence package

| Field | Value |
|---|---|
| Document type | Evidence package |
| Scope | The specimen `EvidenceManifest` for the bootstrap package |
| Sibling documents | `../README.md` · `../../planning/commissioning/01_GOVERNANCE/WP-000_interim_evidence_policy.md` |
| Status | `TECH_COMPLETE` — issued and verified; **acceptance pending** under ADR-001 |
| Date | 2026-08-22 |

**In one paragraph.** This is the first real evidence artifact the repository has
produced: an in-toto Statement listing the files it covers by digest, wrapped in
a DSSE envelope, signed, and anchored in time. It exists to demonstrate that the
acceptance path works end to end — and it is **not an acceptance**, because
issuing evidence and accepting it are different acts performed by different
parties.

| File | Is |
|---|---|
| `evidence.dsse.json` | The DSSE envelope: the in-toto Statement plus its signature |
| `evidence.anchor.json` | The interim time anchor binding the envelope digest to a clock and a commit |

```bash
uv run python scripts/evidence_manifest.py verify \
    --manifest delivery/WP-000/evidence.dsse.json --tamper-demo
```

## What verification proves, and what it does not

**Proves:** the payload has not changed since signing · every covered file still
hashes to what the manifest recorded · the anchor matches the envelope · an
altered payload is rejected.

**Does not prove:** that an independent party witnessed any of it. The profile is
`airl-interim-v0.1` — a local key and no transparency log — so the manifest is
**tamper-evident, not externally witnessed**. The manifest says so itself, in its
own `limitations` list.

## Why it is not `ACCEPTED`

`verifier.decision` reads `PENDING`. Under ADR-001 an R1 solo acceptance is now
permitted, and that signature belongs to the Project Decision Owner. **Issuance
is not acceptance** — collapsing the two is precisely the failure this package
exists to prevent.

## A property that fell out of building it

A manifest is issued **last**. It covers digests, so changing a covered file
afterwards fails verification — which is the control working, not a defect. In
practice this means the manifest is issued once a change is final, and reissued
if anything it covers moves.
