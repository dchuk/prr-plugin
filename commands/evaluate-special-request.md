---
description: Evaluate a special stakeholder request against the current roadmap
argument-hint: "[request description or feature name]"
---

# Evaluate Special Request

**Purpose:** Walk through the book's three qualifying questions to assess whether a special request (typically from sales or a stakeholder) deserves a place on the roadmap, then apply iron triangle analysis to determine the trade-offs if it is accepted.

**When to use:**
- Sales asks to add a feature or fix for a specific customer to close a deal
- A stakeholder requests a one-off capability not currently on the roadmap
- An executive or partner escalates an ad hoc request that would displace planned work
- You need an objective framework to say yes, defer, or decline without causing conflict

---

## Steps

1. **Capture the request.** Ask the user to describe the request in plain terms: what is being asked for, who is asking, and what deal or outcome is at stake. Read any relevant context files the user provides (e.g., a sales email, Slack thread, or brief).

2. **Trace the problem back to its source.** Apply the first qualifying question:
   > *What problem is this request trying to solve?*

   Do not accept the sales contact's framing at face value. Ask the user: Have you (or can you) speak directly with the person who has the underlying problem — not the salesperson relaying it? Prompt them to describe that person's circumstances and what they are trying to accomplish.

3. **Ask 'why' until you reach root cause.** Walk the user through at least three levels of "why" to uncover the actual need beneath the request. Use the outputs to determine:
   - What the root problem is
   - Whether the requester is in your target market (if not, that is a signal to decline)

4. **Apply the second qualifying question.**
   > *Does solving that need align with our current objectives?*

   Ask the user to share the current business objectives or OKRs for the product. Check whether the root problem maps to any active objective. If it does not align, output a clear recommendation to **decline or defer** the request and briefly explain why. Stop here if declining.

5. **Apply the third qualifying question.**
   > *Is it more important than what is already on the roadmap?*

   Ask the user to share the current roadmap themes or Now / Next / Later items. Evaluate the request's priority relative to existing roadmap items using an objective lens — refer the user to [prioritization frameworks](../skills/product-roadmaps/references/patterns/prioritization-frameworks.md) (Critical Path, Kano Model, Desirability / Feasibility / Viability, ROI Scorecard, MoSCoW) if no scoring exists yet. Output a ranked comparison: does this request outrank current Now items, fit into Next, belong in Later, or fall off the roadmap entirely?

6. **If accepting: run iron triangle analysis.** If the request clears all three questions, immediately determine which iron triangle variable(s) will be compromised to accommodate it. Present the user with four explicit trade-off options:

   | Variable | What giving here means |
   |---|---|
   | **Schedule** | Extend the delivery date for current roadmap items |
   | **Scope** | Drop or reduce features from current committed work |
   | **Budget / Resources** | Add people or spend (use cautiously; for software keep teams 3–7 people) |
   | **Quality** | Accept increased technical debt; make this explicit and time-bound |

   Ask the user which variable(s) they are willing to trade. Do not leave this undecided — `ch13.rule.scope-swap-for-late-requests` requires an explicit choice.

7. **Draft a decision summary.** Produce a structured summary with the following sections:
   - **Request:** one-sentence description
   - **Root problem:** the underlying need uncovered in steps 2–3
   - **Target market fit:** yes / no / partial
   - **Objective alignment:** which objective it maps to (or "none")
   - **Priority verdict:** Now / Next / Later / Decline — with a one-sentence rationale
   - **Iron triangle trade-off** (if accepted): which variable(s) are being compromised and how
   - **Recommended next action:** accept with trade-off, defer to next roadmap review, or decline

8. **Write the evaluation artifact.** Read [`../skills/product-roadmaps/templates/special-request.md`](../skills/product-roadmaps/templates/special-request.md) and write a filled-in copy to `./artifacts/request-YYYY-MM-DD-<slug>.md` (slug = kebab-case of the request's short title, e.g. `acme-sso`). Populate `request_date`, `requester`, `deal_size` (if disclosed), `verdict` (now / next / later / decline), `iron_triangle_give` (the variable chosen in step 6, or null if declined), `linked_theme` (existing theme ID if mapped, otherwise null), and all body sections produced in steps 1–7.

9. **Flag stakeholder communication.** Remind the user that the decision and trade-offs must be communicated to all relevant stakeholders. If the request is accepted and displaces planned work, point them to [communicate-roadmap-change.md](communicate-roadmap-change.md) to draft that update — the change-communication should reference this evaluation artifact by path. If declining, suggest a brief stakeholder note explaining the three-question outcome.

---

## Verify

The command succeeds when:
- All three qualifying questions have been answered explicitly (not skipped)
- A clear verdict (accept / defer / decline) has been produced with a written rationale
- If accepted, at least one iron triangle variable has been named and a trade-off decision recorded
- The decision summary is complete enough to share with the requesting stakeholder

---

## Notes

- **Anti-pattern risk:** Accepting requests that skip the three-question filter is a direct path to the **Feature Factory** and **Requestor-Driven Roadmap** anti-patterns documented in [roadmap-anti-patterns.md](../skills/product-roadmaps/references/anti-patterns/roadmap-anti-patterns.md). Skipping even one question weakens the evaluation.
- **Bad prioritization risk:** If the user relies on sales pressure, deal size alone, or executive seniority to rank this request, flag those as anti-patterns covered in [bad-prioritization.md](../skills/product-roadmaps/references/anti-patterns/bad-prioritization.md).
- **Iron triangle context:** The iron triangle (schedule, scope, quality, budget) is covered in depth in [keeping-roadmap-fresh.md](../skills/product-roadmaps/references/topics/keeping-roadmap-fresh.md).
- **Themes vs. features:** If the request is phrased as a feature, use [transform-features-to-themes.md](transform-features-to-themes.md) first to reframe it as a customer outcome before evaluating priority.
- **Recurring patterns:** If the same type of request comes in repeatedly, treat that as a signal to revisit themes — see [themes-and-needs.md](../skills/product-roadmaps/references/core/themes-and-needs.md).
