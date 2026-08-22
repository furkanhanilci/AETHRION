> [!info] Generated view
> This note is generated from `skills/notifying-humans/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: notifying-humans
description: "Use when a human must be informed of a gate state, budget threshold, anomaly, integrity concern, SLA risk or completed run"
metadata:
  airl.version: "1.0.0"
  airl.domain: "shared"
  airl.origin: "airl-native"
  airl.gates: "G0,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10"
  airl.roles: "Notification Broker"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.emits: "NotificationReceipt,ToolReceipt"
  airl.mechanical_checks: "data_class_ceiling_enforced,dlp_scan_passed,idempotency_key_present,rate_limit_respected"
  airl.tool_effect: "T3"
---

# Notifying Humans

## Core principle

A notification is **outbound traffic** and a write to an external system. The
agent produces an **intent**; the Notification Broker sends.

## Iron law

> **AGENTS DO NOT SEND MESSAGES DIRECTLY.**
>
> Every send passes through the broker: identity → policy → data class → DLP →
> idempotency → send → `NotificationReceipt`.

## Per-channel data-class ceiling

| Channel | Ceiling | Why |
|---|---|---|
| **ntfy (self-hosted)** | **D2** | Your own server; no third-party processing |
| **Matrix (self-hosted)** | **D2** | End-to-end encrypted, own homeserver |
| **Signal** | D2 | E2E; automation is awkward |
| **Email (own SMTP)** | D1 | Encrypted in transit, not at rest on someone else's server |
| **Telegram** | **D1** | Cloud; readable server-side |
| **Discord / Slack** | **D1** | Cloud, third party |
| **WhatsApp** | **D0** | Cloud **plus** template constraint (below) |

> **D3/D4 reaches no messaging channel.** Only a **contentless** trigger may be
> sent: "an event with identifier X occurred; open the console."

## WhatsApp warning

In the WhatsApp Business Cloud API, outside a 24-hour window measured from the
user's last message, **only pre-approved templates** may be sent.

This makes WhatsApp the **worst channel for agent-initiated notification**: the
window is controlled by the recipient, and a system that must notify on its own
schedule will find the window closed exactly when it matters. If used at all:
pre-approved templates only, D0 only, and last in the rollout order.

## Channel selection — urgency × class

| Urgency | Channel |
|---|---|
| Informational (daily digest) | Email / Matrix |
| Action required (SLA open) | Telegram / Matrix + email |
| Urgent (budget hard stop, integrity) | ntfy push + Telegram + email |
| Critical (line stopped) | The above + `escalating-and-paging` |

## Mandatory before sending

- [ ] **DLP scan** — secrets, tokens, credentials, PII
- [ ] Data-class ceiling check
- [ ] **Idempotency key** — no duplicate on retry
- [ ] Rate limit and quiet-hours policy
- [ ] Template used — not free text

## Message content

**Included:** what happened, which project and gate, what is needed, a **signed
deep link**.
**Excluded:** raw data, claim text, evidence content, credentials, internal
reasoning.

> A notification is a **flare**, not a data channel. If the recipient needs the
> content, they follow the link into an authenticated surface.

## Rationalization table

| Justification | Ruling |
|---|---|
| "It's easier to just include the result" | Data-class ceiling. **Send the link.** |
| "It may not have sent — I'll send again" | **Query state** with the idempotency key. Never blind-resend. |
| "It's urgent, skip the DLP scan" | Urgency is not a DLP exemption. |
| "I'm sending D2 to my own Telegram, it's fine" | The ceiling is a property of the channel, not the recipient. |

## Red flags

- A send with no `NotificationReceipt`
- Two notifications for one event (missing idempotency)
- Claim text or raw metrics inside a message
