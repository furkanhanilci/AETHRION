# WP-136 — Inbound Content Quarantine and Channel Allowlist

## Package card

| Field | Value |
|---|---|
| Work package | `WP-136` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Content Security Lead |
| Independent verifier | Safety & Governance Owner |
| Hard dependencies | WP-058 (Content Quarantine Firewall), WP-131, WP-132 |
| Related gates | G0, G3, G10 |
| Related controls | CTL-SEC-02 |
| Related acceptance scenarios | ACC-05, ACC-44 |
| Related skill | `receiving-external-messages` |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Every inbound message, email, webhook and external document is treated as
**Zone 3**.

> **Invariant:** **Untrusted human-readable inbound content is never an
> instruction.** It is data, not a
> command.

Outbound traffic is a **data exfiltration** risk; inbound traffic is a **control
takeover** risk. Text embedded in an email, a PDF attachment or a chat message
becomes prompt injection the moment it enters an agent's context — the `ACC-05`
scenario extends across the messaging surface.

Quarantine order: sender verification (SPF/DKIM/DMARC, bot identity, channel
allowlist) → attachment and file scanning → tagging the content as
`<untrusted-external-content>` → entry into agent context **only** under that
tag → **no instruction extraction**.

## Out of scope

- Scientific assessment of the content (owned by the G0/G3 packages)

## Preconditions — Definition of Ready

- Dependencies accepted: WP-058 (Content Quarantine Firewall), WP-131, WP-132
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

## Implementation tasks

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-136-T01 | Channel and sender allowlist registry | A sender outside the allowlist stays in quarantine |
| WP-136-T02 | Sender verification (SPF/DKIM/DMARC, bot identity) | A forged sender is rejected |
| WP-136-T03 | Attachment and file scanning (malware, macros, embedded scripts) | A malicious attachment never enters context |
| WP-136-T04 | Mandatory `<untrusted-external-content>` tagging | Untagged external content cannot enter context |
| WP-136-T05 | Enforce the ban on instruction extraction | No task is generated from inbound text |
| WP-136-T06 | Route inbound messages to the right flow (G0 intake / note / source / feed) | Each type reaches the correct flow |
| WP-136-T07 | Separate **data** from **control** at the boundary: human-readable content can never become a command, while an authenticated, signed, structured `CommandIntent` may — subject to its own authorisation | Two negative tests and one positive test |

## Mandatory deliverables

- The channel and sender allowlist
- The sender verification chain
- The attachment scanning pipeline
- The `QuarantineRecord` schema
- Untrusted-tagging enforcement

## Test and verification plan

- **Prompt injection:** an email and a PDF carrying embedded instructions → agent behaviour is unchanged
- **Untagged content:** untagged external content cannot enter context (negative test)
- **Forged sender:** a message failing DKIM/DMARC stays in quarantine
### Data versus control — why the invariant is worded narrowly

| Class | Example | May it cause an effect? |
|---|---|---|
| **Untrusted content** | email body, PDF text, chat message, web page, abstract | **Never.** It is quarantined data, whatever it says |
| **Authenticated command** | a signed, structured `CommandIntent` from a registered service identity | Possibly — through its own authorisation path, never by being persuasive |

Writing the invariant as "an inbound *message* is never an instruction" would
also forbid legitimate machine-to-machine automation later. The line that
matters is not inbound versus outbound; it is **persuasion versus
authentication**. A prompt-injection payload and a polite request are the same
class of object; a signed command from a known identity is a different one.

- **Approval attempt:** an "I approve" in an inbound message produces no decision
- **Unknown sender:** the content does not enter context; a summary is reported to a human

## Acceptance criteria

- [ ] No external content enters any agent context without being tagged
- [ ] No code path extracts instructions from inbound text
- [ ] Sender verification cannot be skipped
- [ ] The ACC-05 scenario also passes on the messaging surface
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Risks and control points

- "The sender is familiar" is not a valid justification; senders can be impersonated
- PDF is the most common injection carrier; attachment scanning is non-waivable
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

The inbound channel is closed; quarantined content is not deleted and remains
available for review. Quarantine records are retained for audit.

## Handoff into downstream packages

WP-137 subjects external feed content to these same quarantine rules.
