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
