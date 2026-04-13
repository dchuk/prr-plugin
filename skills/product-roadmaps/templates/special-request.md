---
type: special-request-evaluation
request_date: YYYY-MM-DD
requester: <name / role / account>
deal_size: null                     # Optional. USD or relative ("strategic", "SMB")
verdict: now                        # now | next | later | decline
iron_triangle_give: schedule        # schedule | scope | budget | quality
linked_theme: TH-001                # Existing theme ID if the ask maps to one; null if new or declined
evaluator: <name/role>
---

# Special request: <short title>

## Request summary

<Plain description of the ask, in the requester's own framing. Include who is asking, what they want, and what outcome they expect (e.g., close a deal, unblock an integration).>

## Root problem

<The actual customer need beneath the ask. Use 5-Whys or equivalent to move from the stated solution ("add SSO") to the underlying need ("we can't onboard teams without meeting enterprise security review"). Often the real need is already covered by an existing theme.>

## Three qualifying questions

1. **Does this fit our target market?** Yes / No / Partial. <one-line rationale>
2. **Does it align with a business objective?** Which OBJ-* does it serve? <one-line rationale>
3. **Is the customer need validated beyond this one request?** Yes / No. <evidence: other customer signals, support volume, win/loss patterns>

## Priority verdict

**Verdict: <Now | Next | Later | Decline>**

<One paragraph rationale. If accepted, map to an existing theme or describe the new theme that will be created. If declined, explain clearly — "no" now preserves the strategic roadmap.>

## Iron triangle trade-off

If accepted, one of the following must give:

- **Schedule gives:** <which Now/Next theme slips, by how much>
- **Scope gives:** <which Now/Next theme is trimmed or deferred entirely>
- **Budget gives:** <what headcount / spend is added, if any>
- **Quality gives:** <what gets cut — tests, polish, documentation — NOT recommended>

Chosen trade-off: **<schedule | scope | budget | quality>** — <rationale>

## Recommended next action

<Concrete next step: update `roadmap.md` and the affected theme file, draft a change-communication, respond to the requester with the decision and reasoning, schedule a follow-up review date.>
