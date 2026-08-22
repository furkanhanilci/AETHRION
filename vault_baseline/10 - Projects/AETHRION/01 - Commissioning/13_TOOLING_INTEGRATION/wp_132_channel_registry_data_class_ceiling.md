# WP-132 — Channel Registry and Data-Class Ceiling

## Package card

| Field | Value |
|---|---|
| Work package | `WP-132` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Platform Security Lead |
| Hard dependencies | WP-131, WP-006 (ExecutionProfile) |
| Related gates | Platform |
| Related controls | CTL-DAT-02, CTL-DAT-03 |
| Related acceptance scenarios | ACC-41 |
| Related skill | `notifying-humans` |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Every notification channel is registered with a **data-class ceiling** that is
enforced in code. The ceiling is a pre-send gate, not a recommendation.

| Channel | Ceiling | Rationale |
|---|---|---|
| ntfy (self-hosted) | **D2** | Your own server; no third-party processing |
| Matrix (self-hosted) | **D2** | End-to-end encryption on your own homeserver |
| Signal | D2 | End-to-end encrypted; hard to automate |
| Email (own SMTP) | D1 | Encrypted in transit, not at rest on the server |
| Telegram | **D1** | Cloud; readable server-side |
| Discord / Slack | **D1** | Cloud; third party |
| **WhatsApp** | **D0** | Cloud + a 24-hour window + mandatory approved templates |

> **D3/D4 content never goes to any messaging channel.** Only a contentless
> trigger may be sent: "an identified event exists — check the console."

**WhatsApp operational warning:** on the Business Cloud API, outside the
24-hour window following the user's last message, only pre-approved templates
may be sent. That makes WhatsApp the most fragile channel for agent-initiated
notification, and it is therefore scheduled last.

## Out of scope

- The internal implementation detail of the channel connectors (transport library work)
- The inbound direction (WP-136)

## Preconditions — Definition of Ready

- Dependencies accepted: WP-131, WP-006 (ExecutionProfile)
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

## Implementation tasks

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-132-T01 | Define the `ChannelRegistry` schema (channel, ceiling, egress host, identity) | Schema + populated registry file |
| WP-132-T02 | Enforce the ceiling in code and bind it to the policy engine | An above-ceiling send is rejected in test |
| WP-132-T03 | Make DLP scanning (secrets, tokens, PII) mandatory before send | A message containing a secret is not sent |
| WP-132-T04 | Template registry — free-text sending is disabled | An untemplated send is rejected |
| WP-132-T05 | First channels: ntfy (self-hosted) + Telegram | Both channels work end to end |
| WP-132-T06 | Define the egress allowlist separately per channel | Egress to a host outside the allowlist is blocked |

## Mandatory deliverables

- The `ChannelRegistry` schema and its populated registry
- Data-class ceiling enforcement (code + tests)
- DLP scanning integration
- The message template registry
- A per-channel egress allowlist

## Test and verification plan

- **Ceiling enforcement:** content at ceiling+1 for each channel → send rejected
- **D3/D4:** no content reaches any channel; only a contentless trigger is produced
- **DLP:** sample messages carrying API keys, tokens and PII are caught
- **Templates:** free-text sending is rejected
- **Egress:** a request to a host outside the allowlist is blocked

## Acceptance criteria

- [ ] The per-channel ceiling is defined **in code** and enforced by tests, not only documented
- [ ] D3/D4 content cannot leave through any channel (negative test)
- [ ] There is no code path that skips DLP scanning
- [ ] WhatsApp is reachable only at D0 and only through approved templates
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Risks and control points

- A channel ceiling does not vary by person; there is no "but it's my own Telegram" exception
- Adding a new channel requires Safety/Data Owner approval and a new ceiling entry
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

The channel is removed from the registry; pending messages for that channel are
not dropped — they stay queued and are **not** rerouted to another channel,
because rerouting could breach a ceiling.

## Handoff into downstream packages

WP-133 and WP-134 use the channels in this registry. A channel that is not
registered cannot be used.
