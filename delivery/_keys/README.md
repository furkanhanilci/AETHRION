# Interim signing keys

| Field | Value |
|---|---|
| Document type | Component note |
| Scope | The key material used by the WP-000 interim attestation profile |
| Sibling documents | `../README.md` · `../../planning/commissioning/01_GOVERNANCE/WP-000_interim_evidence_policy.md` |
| Status | `WORKING` for the interim profile; **not the target** |
| Date | 2026-08-22 |

| File | Committed | Why |
|---|---|---|
| `airl-interim.pub` | **yes** | So anyone with the repository can verify a manifest without trusting the issuer to also supply the verifier |
| `airl-interim.ed25519` | **no** — git-ignored, mode 600 | It is a private key |

## What this profile is, precisely

`airl-interim-v0.1` signs with a **local Ed25519 key**. The target profile is
Sigstore keyless signing with a Rekor inclusion proof, and the difference is not
cosmetic:

> Today one operator controls the repository, the signing key, the manifest
> generator and the clock. That makes an attestation **tamper-evident but not
> externally witnessed** — someone who holds all four could reissue history
> consistently.

Every manifest records this in its own `limitations` list, and verification
prints what is not covered. Moving to `sigstore-python` is the named remaining
work in WP-000.
