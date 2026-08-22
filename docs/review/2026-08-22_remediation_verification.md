# Remediation Verification — 2026-08-22

**In one paragraph.** This report states what is true today, measured against a frozen audit that must not be edited to match the present. Two audit findings were genuinely closed, one had its storage half addressed on paper, and the rest remain open. New surface has been added since the audit — a skill registry, an interim evidence policy, six acceptance scenarios — and none of it is executed, which is stated here precisely so the additions do not read as progress against the audit's central finding.

| Field | Value |
|---|---|
| Document type | Verification report against a frozen audit |
| Audit under verification | [`FRAMEWORK_REVIEW_2026-08-21_CLAUDE.md`](FRAMEWORK_REVIEW_2026-08-21_CLAUDE.md) — frozen, not edited |
| Repository state | commissioning baseline **v1.0** |
| Method | Every claim below was re-checked against the working tree, not against memory |

> **Why this document exists separately.** The audit is evidence, and evidence
> that gets edited to stay current stops being evidence. Its counts are wrong
> *today* and correct *for 2026-08-21*, which is exactly what a snapshot should
> be. Current state belongs here instead.

---

## 1. Inventory drift since the audit

| Item | Audit, 2026-08-21 | Baseline v1.0, 2026-08-22 |
|---|---:|---:|
| Work packages | 130 | 140, plus the **WP-000** bootstrap package |
| Acceptance scenarios | 40 | **46** — ACC-41–46 added for skill governance |
| Sealed files | 186 | **202** |
| Skills | 38, non-conformant, loading nowhere | **49**, conformant, wired for Claude Code |

## 2. Findings: what actually changed

| Finding | Audit verdict | Verified state today |
|---|---|---|
| **C1** evidence deadlock | Critical — programme cannot start | **Storage half addressed on paper.** WP-000 expresses the manifest as an in-toto attestation signed through Sigstore and recorded in Rekor, so immutability no longer waits for WP-026. **No manifest has been issued, signed or logged.** The package is written, not executed |
| **C2** scope vs. organisation | Critical — R3 permanently blocked | **Open.** The architecture now supplies a *shape* — `RoleBinding` with separation constraints instead of headcount — but which combinations count as independent is undecided |
| **M2** smoke test exits 0 with the Bridge down | High-value fix | **Closed.** Asserts the exact five-tool set; exits 1. Verified both ways |
| **M3** acceptance test depended on personal library data | High-value fix | **Closed.** 11 data-independent structural checks |
| **M10** SILBO leakage in unit descriptions | Open | **Closed.** Units reinstalled |
| **H1** ingest capped at 100 records | Open | **Open.** Fix **M9** first, or pagination converts a masked truncation into active data loss |
| **H2** no deletion reconciliation | Open | **Open** |
| **H3** read-only boundary untested behaviourally | Open | **Open** |
| **H4** contract core has no consumer | Open | **Open.** `src/airl_bridge` still imports nothing from `src/airl_framework`, and the digest formats still disagree |
| **H5** no CI | Open | **Open.** The verification bundle is now five checks, all manual |

## 3. New surface added since the audit — and its honest status

| Added | Status |
|---|---|
| Two skill families, 49 skills, Agent Skills format | Format-conformant and mechanically checked; **no behaviour test has been run on any skill** |
| `scripts/validate_skills.py` | Working; part of the verification bundle |
| Skill bootstrap | Wired for **Claude Code only** (`.claude/skills`); other harnesses are format-compatible, not verified |
| WP-000 | Written, **not executed** |
| ACC-41–46 | Written; like all 46, never run |
| WP-013 / 043 / 047 / 048 skill scope | Specified, not built |
| `AIRL_OS_ARCHITECTURE.md`, `AIRL_OS_EXTERNAL_STANDARDS.md` | Documentation |

**The audit's central sentence still holds:** *"a very well written plan and a
small but genuinely working vertical slice; the distance between them is far
greater than the documentation implies."* Baseline v1.0 narrows the plan's
**internal** inconsistencies. It does not narrow that distance, and this report
exists partly to prevent the additions above from reading as if it had.

## 4. Verification run for this report

```
20/20 tests · 49/49 skills conform · plan seal 202/202
MCP smoke: five read-only tools, exits 1 when the Bridge is down
Acceptance: 11 structural checks, data-independent
Mirror drift: 0 · vault and vault_baseline identical
```

Every one of these runs by hand. Nothing enforces that they ran before a commit.
