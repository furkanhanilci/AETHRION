> [!info] Generated view
> This note is generated from `skills/routing-decision-requests/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: routing-decision-requests
version: 1.0.0
description: Use when a human decision or approval is required, when a DecisionRequest enters the queue, or when an approval arrives through a messaging channel
gates: [G1, G4, G8, G9]
roles: [Notification Broker, Project Decision Owner, Safety/Data Owner]
assurance_classes: [R1, R2, R3]
non_waivable: true
requires_skills: [notifying-humans]
emits: [DecisionRequest, DecisionRecord]
mechanical_checks: [approval_surface_authenticated, deep_link_signed_and_expiring, no_approval_via_chat_reply]
---

# Routing Decision Requests

## Iron law

> **MESSAGING IS A NOTIFICATION CHANNEL, NOT AN AUTHORISATION CHANNEL.**
>
> No decision may be made by replying to a message.

## Why

Telegram, Discord, WhatsApp and email accounts can be compromised, spoofed, or
forwarded. A `DecisionRecord` is a signed, binding record. Binding the end of the
evidence chain to a chat message reduces the security of the entire chain to the
security of that channel — and that channel was not designed for it.

This is the preventive side of the **human approval forgery** scenario.

## The correct flow

```
1. DecisionRequest enters the queue
2. A notification is sent: "Decision pending — <project> <gate>"
   + a SIGNED, EXPIRING, SINGLE-USE deep link
3. The human opens the link → arrives at an AUTHENTICATED surface
4. They see the frozen evidence package
5. They decide THERE → DecisionRecord is signed
6. A confirmation notification is returned
```

## Deep link rules

- Signed (HMAC or asymmetric)
- **Expiring** — short TTL
- **Single use**
- Carries **access to the surface**, not the authority to decide
- Invalid if forwarded (user-bound)

The link is deliberately not a shortcut to approval. It removes friction from
*reaching* the decision surface, not from *making* the decision.

## What a chat reply may do

| Action | Permitted |
|---|---|
| Acknowledgement / "seen" | ✅ |
| Request more information | ✅ — recorded as a queue note |
| Request an SLA extension | ✅ — a request, not a decision |
| **Approve / reject** | ❌ **never** |
| **Destructive action** (`RETRACT` etc.) | ❌ **never** |

## Timeout

> **There is no auto-approve.** When the SLA expires it escalates one level or
> the workflow pauses. **Silence is not consent.**

## Attention budget

The decision queue has a **hard quota** (for example, five G8 decisions per
week). When the quota is exhausted the queue **waits**. There is no express-review
mode.

Measured: decision-time distribution, which evidence sections were opened, G10
reversal rate, and the rate of `ACCEPT` despite an adversarial `REJECT`.

The last metric is the rubber-stamping detector. It is the reason the quota
exists: throughput pressure on a human decision maker produces approvals, not
decisions.

## Rationalization table

| Justification | Ruling |
|---|---|
| "I typed 'approved' in Telegram, that's enough" | **It is not.** Open the link, approve on the surface. |
| "It's urgent, let's approve quickly" | Urgency is not an authentication exemption. |
| "I'm the only user here" | Account compromise happens to single users too. |
| "The bot knows it's me" | The bot knows the channel's identity, not the person's. |

## Red flags

- A `DecisionRecord` sourced from a messaging channel
- A deep link with no expiry or reusable
- A state advancing automatically after an SLA expiry
- Decision times clustered at the very short end
