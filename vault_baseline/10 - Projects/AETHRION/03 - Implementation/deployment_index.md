---
title: "Deploy"
type: index
category: implementation
status: WORKING
summary: "Three systemd user units run the only component that exists, and one workflow file defines the verification that should run on every push but currently does not."
source: "deploy/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/execution
  - aethrion/index
---

> [!info] Generated view
> This note is generated from `deploy/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Deploy

| Field | Value |
|---|---|
| Document type | Index — deployment units and the verification control |
| Scope | systemd units for the bridge, and the staged CI workflow |
| Sibling documents | `../docs/OPERATIONS.md` · `../docs/architecture/ADR-002_bootstrap_verification_control.md` |
| Status | Units `WORKING`; the verification workflow is **written and not active** |
| Date | 2026-08-22 |

**In one paragraph.** Three systemd user units run the only component that
exists, and one workflow file defines the verification that *should* run on every
push but currently does not. The gap is a credential, not a design choice, and it
is recorded here rather than hidden.

## systemd units — running

| Unit | Role |
|---|---|
| `airl-bridge.service` | The FastAPI bridge, bound to loopback only |
| `airl-bridge-sync.service` | One synchronisation run |
| `airl-bridge-sync.timer` | Triggers the sync every 30 minutes |

```bash
systemctl --user status airl-bridge.service airl-bridge-sync.timer
journalctl --user -u airl-bridge.service -n 50
```

Projection files carry a `generated_at` timestamp, so the timer produces routine
churn under the vault's generated literature area. That diff is expected and is
not a change.

## `bvc-01-verify.yml` — written, **not active**

BVC-01 defines a push-triggered run of the automatable half of the verification
bundle. It sits here rather than in `.github/workflows/` because the token used
to commit it lacks GitHub's `workflow` scope, and GitHub refuses a push that
creates a workflow file without it.

```bash
gh auth refresh -h github.com -s workflow
mkdir -p .github/workflows
cp deploy/bvc-01-verify.yml .github/workflows/verify.yml
git add .github/workflows/verify.yml && git commit -m "Activate BVC-01" && git push
```

> **Until that runs, the checks still only run when someone remembers**, and the
> gap BVC-01 exists to close is not closed. It is a temporary control with an
> owner, an expiry and WP-024 as its retirement package — and it does **not**
> close finding H5, which is the absence of the WP-024 CI platform.
