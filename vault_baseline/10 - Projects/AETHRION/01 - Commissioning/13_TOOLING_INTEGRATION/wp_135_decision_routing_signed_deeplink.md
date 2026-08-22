# WP-135 — Decision Routing and Signed Deep Links

## Package card

| Field | Value |
|---|---|
| Work package | `WP-135` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Governance Lead |
| Independent verifier | Platform Security Lead |
| Hard dependencies | WP-131, WP-132, WP-055 (SPIFFE/Vault identity), WP-093 (Decision Queue UI) |
| Related gates | G1, G4, G8, G9 |
| Related controls | CTL-GOV-01, CTL-SEC-04 |
| Related acceptance scenarios | ACC-25, ACC-26 |
| Related skill | `routing-decision-requests` |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Events requiring a human decision are **announced** by notification, but the
decision itself is taken on an authenticated surface.

> **Invariant:** Messaging is a **notification channel**, not an authorisation
> channel. No decision can be given by a chat reply.

The reasoning: Telegram, Discord, WhatsApp and email accounts can be
compromised, impersonated or forwarded. A `DecisionRecord` is a signed, binding
record; anchoring the end of the evidence chain to a chat message reduces the
entire chain to the security of that channel. This is the preventive side of
the **ACC-25 (Human Approval Forgery)** scenario.

A chat reply **can**: acknowledge receipt, request more information, request an
SLA extension. It **cannot**: approve, reject, or trigger a destructive action.

## Out of scope

- The decision surface UI itself (WP-093)
- The content and rubric of the decision (the relevant gate package)

## Preconditions — Definition of Ready

- Dependencies accepted: WP-131, WP-132, WP-055 (SPIFFE/Vault identity), WP-093 (Decision Queue UI)
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

## Implementation tasks

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-135-T01 | Generate signed, time-limited, single-use deep links | The link is invalid after expiry |
| WP-135-T02 | Enforce that the link carries **surface access**, never authority | A link alone cannot produce a decision |
| WP-135-T03 | User-bound verification (a forwarded link is invalid) | A link opened under a different identity is rejected |
| WP-135-T04 | Reject approval/rejection attempts arriving from a chat channel | The attempt is logged and rejected |
| WP-135-T05 | Apply the human attention-budget quota | When the quota is exhausted the queue waits; no auto-approve |
| WP-135-T06 | Decision telemetry (duration, sections opened, reversal rate) | Measurements flow to Metascience |

## Mandatory deliverables

- The signed deep-link generator and validator
- The authenticated decision-surface link
- Chat-channel approval rejection
- The attention-budget quota
- Decision telemetry

## Test and verification plan

- **Approval from chat:** an "I approve" message on a channel produces no decision
- **Link lifetime:** the link is invalid after its TTL
- **Single use:** a second use is rejected
- **Forwarding:** a link opened under another identity is rejected
- **Quota:** when the weekly quota is exhausted, new decision requests wait; there is no auto-approve

## Acceptance criteria

- [ ] No `DecisionRecord` can originate from a messaging channel
- [ ] Deep links are time-limited, single-use and user-bound
- [ ] When the quota is exhausted the system **waits**; there is no express-review mode
- [ ] The decision-time distribution and the G10 reversal rate are measured
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Risks and control points

- The quota limits the laboratory's throughput. **This is a design choice, not a defect.**
- Link leakage: TTLs are kept short and links are revoked after use
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

If the deep-link mechanism is disabled, decisions are taken only on the surface
itself and notifications degrade to contentless triggers. The decision flow does
not stop.

## Handoff into downstream packages

WP-136 inherits the rule for rejecting approval attempts arriving on inbound channels.
