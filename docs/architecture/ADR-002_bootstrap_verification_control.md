# ADR-002 — Bootstrap Verification Control

| Field | Value |
|---|---|
| Document type | Architecture decision record — temporary control |
| Scope | How verification is enforced before WP-024 delivers the CI platform |
| Sibling documents | WP-024 (CI foundation) · `../OPERATIONS.md` · `ADR-001` |
| Status | **ACCEPTED — 2026-08-22.** Written as `deploy/bvc-01-verify.yml`; **staged, not yet active** — see §6 |
| Date | 2026-08-22 |

**In one paragraph.** The verification bundle is seven commands and every one of
them is run by hand, so nothing prevents a commit that never ran them — audit
finding **H5**. The obvious response is "stand up CI", but WP-024 hard-depends on
WP-020, WP-022 and WP-023, none of which exist. This record refuses both bad
options — waiting for WP-024, and quietly pulling it forward — and defines a
narrow bootstrap control that expires.

---

## 1. Why not simply build WP-024 now

WP-024 delivers a CI *platform*: schema validation, policy checks, security
scanning, provenance attestation and integration testing, bound to the contract
spine. Pulling it forward means either building it without its dependencies —
which produces a second, unplanned platform — or redefining it downward, which
loses the package's actual scope.

**Neither is acceptable, and the failure mode of doing it quietly is worse than
either**: the plan would say WP-024 is done while something much smaller is
running under its name.

---

## 2. The control

> **BVC-01 — Bootstrap Verification Control.** Until WP-024 is `ACCEPTED`, the
> verification bundle runs automatically on every push to `main`, as a
> **temporary control** recorded in the control catalogue with an owner, an
> expiry and a named retirement package.

| Field | Value |
|---|---|
| Control id | `BVC-01` |
| Scope | `pytest` · `validate_skills.py` · `validate_commissioning_plan.py` · `sha256sum -c` · `make_figures.py --check` · both mirror `--check` runs |
| Explicitly **not** in scope | schema validation · policy bundles · security scanning · provenance attestation · integration testing — those are WP-024 |
| Owner | Engineering Owner |
| Retirement package | **WP-024** |
| Expiry | On WP-024 acceptance, or 2027-02-22, whichever is earlier |
| On expiry without retirement | The control is re-approved explicitly or removed; it does not lapse silently |

**What it does not run is as important as what it does.** `mcp_smoke.py` and
`acceptance_v0.py` need a live Bridge and a local Zotero, so they stay manual and
their absence from CI is recorded rather than hidden.

---

## 3. Why this is legitimate rather than a shortcut

| Property | This control | Quietly pulling WP-024 forward |
|---|---|---|
| Named in the control catalogue | ✅ | ❌ |
| Has an owner | ✅ | ❌ |
| Has an expiry | ✅ | ❌ |
| Names its retirement package | ✅ | ❌ |
| Claims to be WP-024 | ❌ | ✅, falsely |

The plan already provides for exactly this: *"if a temporary manual control is
required, its owner, scope, expiry, compensating control and removal package are
recorded."* This is that mechanism, applied to an automated control rather than a
manual one.

---

## 4. What it closes, and what it does not

**Closes:** the gap between "the checks exist" and "the checks ran". After this,
a push that breaks the seal, the plan semantics, the skill contract or a figure
fails visibly.

**Does not close:** H5 itself. H5 is the absence of a CI *platform*, and it stays
open until WP-024. Recording BVC-01 as closing H5 would be exactly the kind of
overstatement this repository exists to avoid.

---

## 5. Decision

| Field | Value |
|---|---|
| Decision | **BVC-01 adopted.** Written as `deploy/bvc-01-verify.yml`; activation is one commit away |
| Decided by | Engineering Owner |
| Date | 2026-08-22 |
| Expiry | WP-024 acceptance, or 2027-02-22, whichever is earlier |

> This control may be implemented before ADR-001 is decided — it verifies, it
> does not accept. Nothing it runs produces an `ACCEPTED` state.


---

## 6. Activation state

| | |
|---|---|
| Decided | ✅ 2026-08-22 |
| Written | ✅ `deploy/bvc-01-verify.yml`, 9 steps |
| **Active** | ❌ **not yet** |

The workflow is staged in `deploy/` rather than `.github/workflows/` because the
token used to commit it lacks GitHub's `workflow` scope, and GitHub refuses a
push that creates a workflow file without it. This is a credential boundary, not
a design decision.

```bash
gh auth refresh -h github.com -s workflow
mkdir -p .github/workflows
cp deploy/bvc-01-verify.yml .github/workflows/verify.yml
git add .github/workflows/verify.yml
git commit -m "Activate BVC-01"
git push
```

> **Until that runs, the checks still only run when someone remembers.** The gap
> BVC-01 exists to close is not closed yet, and no document in this repository
> may state otherwise.
