# Vendored licences

| Field | Value |
|---|---|
| Document type | Attribution record |
| Scope | Licence text for third-party content vendored into `skills/` |
| Sibling documents | `../../NOTICE` · `../README.md` |
| Status | Reference |
| Date | 2026-08-22 |

Eleven engineering skills are vendored verbatim from
[`obra/superpowers`](https://github.com/obra/superpowers), pinned at commit
`b36e0829c6d0140e93cfef2ca599b1b07d4a7797`, under the MIT licence reproduced in
`LICENSE-superpowers.txt` (Copyright © 2025 Jesse Vincent).

Each vendored skill declares `license: MIT`, `airl.origin: "superpowers"` and its
`airl.upstream_commit`, so provenance is machine-readable rather than a claim in
prose — and `scripts/validate_skills.py` **fails the build** if a vendored skill's
provenance is not pinned to a full commit sha.

> **Do not edit vendored content.** Change it upstream, or fork it into an
> AIRL-native skill that records `airl.derived_from`.
