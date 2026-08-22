---
title: "Delivery — Evidence Packages"
cssclasses:
  - aethrion-index
type: index
category: evidence
source: "delivery/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/evidence
  - aethrion/index
---

> [!info] Generated view
> This note is generated from `delivery/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Delivery — Evidence Packages

Evidence packages for each work package and acceptance scenario live here.

```
delivery/
  WP-xxx/
    evidence-manifest.json     # required
    evidence-manifest.json.ots # OpenTimestamps proof (WP-139)
    tests/                     # fresh run outputs
    reviews/                   # independent review records
    decisions/                 # references to the relevant DecisionRecord
  ACC-xx/
    ...
```

## Minimum fields of `evidence-manifest.json`

```json
{
  "package_id": "WP-xxx",
  "target_revision": "<git commit sha>",
  "produced_at": "<ISO 8601>",
  "producer": "<role / model profile>",
  "verifier": "<actor independent of the producer>",
  "environment": {"python": "...", "os": "...", "deps_lock_sha256": "..."},
  "artifacts": [{"path": "...", "sha256": "...", "size_bytes": 0}],
  "commands": [{"cmd": "...", "exit_code": 0, "output_sha256": "..."}],
  "open_findings": [],
  "decision": "<decision-id or null>"
}
```

## Rules

1. **No delivery is accepted without a manifest.** A package may be
   `TECH_COMPLETE`; reaching `ACCEPTED` requires an independent verifier's
   decision.
2. **Evidence comes from a fresh run.** Not from memory, not from a previous
   run, not from an agent's report — see
   [`skills/verification-before-completion`](../skills/verification-before-completion/SKILL.md).
3. **Time evidence is anchored externally** (WP-139). Without an `.ots` file, a
   manifest's "when did this exist" can only be established by trusting this
   repository.
4. **This directory is append-only in spirit.** Deletion requires an
   `IntegrityCase`.

> ⚠️ **Currently empty — and that is correct.** No work package is `ACCEPTED`,
> because the signed `EvidenceManifest` and immutable-store mechanisms have not
> been built. See finding **C1** in [`docs/review/`](../docs/review/) and the
> proposed **WP-000 Interim Evidence Policy**.


---

## Issued evidence

| Package | Manifest | Profile | State |
|---|---|---|---|
| **WP-000** | `WP-000/evidence.dsse.json` + `WP-000/evidence.anchor.json` | `airl-interim-v0.1` | Verified; **acceptance pending** under ADR-001 |

Verify it:

```bash
uv run python scripts/evidence_manifest.py verify \
    --manifest delivery/WP-000/evidence.dsse.json --tamper-demo
```

Issuance is **not** acceptance. Every manifest records
`verifier.decision: PENDING` until an independent verifier — as defined by
`docs/architecture/ADR-001_solo_operator_independence.md` — records a decision
against it.

**A manifest is issued last, not first.** It covers file digests, so any change
to a covered file after issuance fails verification — which is the control
working, not a defect. In practice this means the manifest for a change is
issued once the change is final, and re-issued if anything it covers moves.

`_keys/` holds the interim signing key. The private key is git-ignored; the
public key is committed so that anyone with the repository can verify a manifest
without trusting the issuer to also supply the verifier.
