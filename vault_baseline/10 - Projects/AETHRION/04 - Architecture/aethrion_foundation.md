> [!info] Generated view
> This note is generated from `docs/architecture/FOUNDATION.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Foundation Layer

| Field | Value |
|---|---|
| Document type | Architecture reference — the foundation layer |
| Scope | Shared contracts, registries and platform services the rest of the system binds to |
| Sibling documents | `AETHRION_ARCHITECTURE.md` · `../../planning/commissioning/03_FOUNDATION/` |
| Status | `TECH_COMPLETE` for the contract core; everything else `DESIGNED` |
| Date | 2026-08-22 |

**In one paragraph.** The foundation is what every later service binds to: one identity and correlation standard, one artifact manifest, one event envelope, one schema registry, and the platform services beneath them. Today the contract core exists in `src/airl_framework` with **no production consumer** and a digest format that contradicts the bridge's — a contract with no consumer is a parallel universe, and closing that gap matters more than adding another contract.

> System-wide context and diagrams: [`AETHRION_ARCHITECTURE.md`](AETHRION_ARCHITECTURE.md).

> **Status:** this document replaces a one-line stub that read
> `# Foundation repository skeleton`. That stub was one of the empty
> "deliverables" behind audit finding **C3** — a file that existed so a checklist
> could be ticked. What follows is what the foundation layer actually is, what
> exists of it today, and what does not.

## What "foundation" means here

The foundation is the layer every other plane binds to: identity, contracts,
environments, repository structure, CI, and the data and event substrate. It is
covered by **WP-021 through WP-030** plus the contract packages **WP-011–020**.

Its defining property is that **nothing above it can be more trustworthy than
it is**. A claim's lineage is only as good as the identity scheme underneath it;
an evidence manifest is only as good as the immutable store it is written to.
That is why the foundation wave comes before the feature waves in
`planning/commissioning/00_PROGRAM/02_wave_and_dependency_map.md`.

## What exists today

| Element | State | Where |
|---|---|---|
| Shared contract core | ⚠️ `TECH_COMPLETE`, **no production consumer** | [`src/airl_framework/contracts.py`](../../src/airl_framework/contracts.py) |
| Canonical source registry | ✅ Working, SQLite V0 | [`src/airl_bridge/database.py`](../../src/airl_bridge/database.py) |
| Repository topology and ownership | ⚠️ Files exist, **not machine-enforced** | [`CODEOWNERS`](../../CODEOWNERS), [`dependency-rules.txt`](../../dependency-rules.txt) |
| Environment configuration | ✅ Working, with two fail-closed boundaries | [`src/airl_bridge/config.py`](../../src/airl_bridge/config.py) |
| Schema registry | ⚠️ In-process `dict`, validates nothing | `src/airl_framework/contracts.py` |
| Contract schemas as JSON Schema | ⬜ Absent | [`schemas/`](../../schemas/) |
| CI | ⬜ **Absent** | — |
| PostgreSQL, object store, NATS, MLflow | ⬜ Absent | — |

## The three gaps that matter

**1. The contract core has no consumer (finding H4).** Nothing in
`src/airl_bridge` imports `src/airl_framework`, and the two already disagree:
the bridge produces `content_hash` as `"sha256:<hex>"` while `ArtifactManifest`
requires a bare 64-character digest. A contract violated by the only data that
exists is not a foundation — it is a parallel universe. Binding it means routing
`SourceRecord.airl_id` through `Identity` and reconciling the hash format, with a
migration and a reversal path.

**2. BVC-01 (`deploy/bvc-01-verify.yml`) defines a push-triggered run of the automatable checks, but it is **staged, not active** — activation needs a workflow-scoped token, and it does not close finding H5, which is the absence of the WP-024 platform.** Without it, `CODEOWNERS` enforces nothing,
`dependency-rules.txt` is prose, the schema registry is unchecked, and every
"the tests pass" statement rests on a manual claim. This is why the audit ranks
the CI foundation as the highest-leverage implementable step: **one workflow file
closes four findings** — H5 itself, the static half of H3, and the mechanical
verification of M4 and M11.

**3. There is no immutable evidence store (finding C1).** Every package's
Definition of Done requires a signed `EvidenceManifest` written to an immutable
store; that store is WP-026, five dependency levels downstream. The evidence
chain is therefore cyclic even though the dependency graph is not, and **no
package can reach `ACCEPTED`** — including WP-001. The proposed way out is
**WP-000 Interim Evidence Policy**, using `delivery/WP-xxx/evidence-manifest.json`
plus the external time anchor from **WP-139** (OpenTimestamps needs no
infrastructure and no trusted third party).

## Order of work

1. **WP-000 Interim Evidence Policy** — without it nothing can be accepted.
2. **CI** (WP-024) — it turns claims into evidence and closes four findings.
3. **Bind the contract core** (WP-011/014/020) — give it one real consumer before
   writing any new contract.
4. Then the data and event substrate (WP-025–030).

## Related documents

- [`ARCHITECTURE_V0.md`](../ARCHITECTURE_V0.md) — the architecture of the working
  vertical slice
- [`AETHRION_IDEAL_STRUCTURE.md`](AETHRION_IDEAL_STRUCTURE.md) — what the target
  architecture is missing
- [`../review/`](../review/) — the evidence behind every finding cited above
- `planning/commissioning/03_FOUNDATION/` — WP-021 to WP-030 in detail
