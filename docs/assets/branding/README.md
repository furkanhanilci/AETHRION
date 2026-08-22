# Branding Assets

| Field | Value |
|---|---|
| Document type | Convention — asset provenance |
| Scope | The AETHRION logo: which file is canonical, and which files are copies |
| Sibling documents | `../../branding.md` — the terminology this asset belongs to |
| Status | `WORKING` |
| Date | 2026-08-22 |

**In one paragraph.** One file in this repository is the logo. Everything else that looks like the logo is a copy of it, placed where a particular tool needs a local file. Copies are byte-identical and are replaced, never edited — the same rule the figure generators and the vault mirrors already run on.

## Canonical file

```
docs/assets/branding/aethrion-logo.png
```

PNG, 1339 × 1174, 8-bit RGBA, transparent background. Supplied by the project
owner and committed **unmodified**: not re-rendered, not recompressed, not
recoloured, not cropped, not resized. Its geometry, colours, composition and
proportions are the author's, and this repository has no licence to change them.

## Projections

| Path | Why it exists | Rule |
|---|---|---|
| `<vault>/10 - Projects/AETHRION/_assets/aethrion-logo.png` | Obsidian resolves `![[aethrion-logo.png]]` by filename and cannot follow a path outside the vault | **Generated** by `scripts/mirror_vault.py`; byte-identical, overwritten on every mirror run |

Verify the copy has not drifted:

```bash
cmp docs/assets/branding/aethrion-logo.png \
    "vault_baseline/10 - Projects/AETHRION/_assets/aethrion-logo.png"
```

## Where the logo appears

Sparingly, and only where a reader arrives at the project for the first time:

- `README.md` — repository root
- `docs/architecture/AETHRION_ARCHITECTURE.md` — the principal architecture document
- `<vault>/00 - Home/aethrion_home.md` — the Obsidian landing page (human-authored)

It is deliberately **not** placed in per-directory READMEs, in planning
documents, or in the generated figures. A logo repeated on every page stops
carrying information and starts costing attention.

## What is not here

No wordmark, no favicon, no icon set, no colour tokens file and no alternative
lockups — none of those has been supplied, and inventing them would be the
design equivalent of documenting an unbuilt component as if it existed. If they
are needed later they belong here, next to the canonical file, with the same
provenance note.
