---
description: Plan and execute shuttle diplomacy sessions for roadmap alignment
argument-hint: "[stakeholder list or roadmap file]"
---

# Run Shuttle Diplomacy

**Purpose:** This command guides you through the full shuttle diplomacy process — individual one-on-one stakeholder meetings followed by a group alignment session — to build buy-in for a new or updated product roadmap. Use it whenever you need stakeholder alignment before committing to a roadmap direction.

## When to use

- You have a draft roadmap (or roadmap skeleton) and need stakeholder buy-in before finalizing it
- Significant changes to the roadmap need to be communicated and negotiated across departments
- Siloed decision-making has broken down trust or momentum on the product team
- You are relaunching a roadmap and need to re-establish shared direction
- A co-creation workshop is planned and you need one-on-ones to prepare the group session

---

## Steps

### 1. Identify stakeholders

Ask the user: "Who are the internal and external stakeholders who need to be aligned on this roadmap? List names, roles, and departments."

If the user provides a file or document, Read it and Grep for names, roles, or team references to build the list. Produce a table:

| Stakeholder | Role / Department | Internal or External |
|-------------|------------------|----------------------|
| …           | …                | …                    |

### 2. Confirm the draft roadmap artifact

Ask the user to share or describe the current draft roadmap. This artifact is required — per the book's guidance, you should "entice your stakeholders with a draft of your roadmap and ask for their input." If no draft exists, prompt the user to run [`build-roadmap-from-vision.md`](build-roadmap-from-vision.md) first to generate a skeleton.

### 3. Generate the Shuttle Diplomacy Canvas

Create a private tracking table (not to be shared with stakeholders) with one row per stakeholder. Populate what is known; leave cells blank for the user to fill in after each meeting.

**Shuttle Diplomacy Canvas**

| Stakeholder | Desired Outcomes | Reasons / Rationale | Success Metrics | Top Product Priorities | Political Considerations |
|-------------|-----------------|--------------------|-----------------|-----------------------|--------------------------|
| …           | …               | …                  | …               | …                     | …                        |

Remind the user: this canvas is a private guide — do not share it across the team.

### 4. Prepare the GROW meeting guide

For each stakeholder, output a short meeting agenda card using the GROW framework:

**Meeting with [Stakeholder Name] — [Role]**

- **Goals** — "What are you trying to accomplish for the product / business this period?"
- **Reality** — "What's currently on your plate? What constraints or pressures are you working under?"
- **Options** — "Looking at this draft roadmap, what do you think should be added, removed, or reprioritized to achieve your goals?"
- **Way forward** — "Of the options we've discussed, which best serve your stated goals and the organization's objectives?"

Open every meeting by tying the discussion to the organization's goals and objectives before moving into the stakeholder's individual concerns. Focus only on the issues a particular stakeholder cares about, and ignore the rest of the list.

### 5. Run the individual meetings (user action)

Instruct the user to conduct each one-on-one, keeping sessions short and informal. After each meeting, return to this command and provide notes. Use the notes to:

- Fill in the Shuttle Diplomacy Canvas row for that stakeholder
- Flag any conflicts with other stakeholders' priorities
- Confirm that each stakeholder's ideas are captured in the prioritization scorecard so they feel heard

### 6. Synthesize conflicts and trade-offs

After all one-on-one notes are collected, analyze the completed canvas and produce:

1. **Shared priorities** — themes or outcomes that multiple stakeholders named
2. **Conflicts** — areas where stakeholders have directly opposing priorities or success metrics
3. **Trade-off recommendations** — for each conflict, suggest a resolution framed as: "Ensure [result] for [stakeholder]" vs. "Ensure [result] for [stakeholder]" — and recommend which to prioritize and why, drawing on the organization's stated goals

Reference the [prioritization frameworks](../skills/product-roadmaps/references/patterns/prioritization-frameworks.md) (Critical Path, Kano Model, ROI Scorecard, MoSCoW) to support trade-off reasoning if the user has scored themes.

Flag any **Feature Factory** anti-pattern signals (e.g., stakeholders requesting features rather than outcomes). See [roadmap anti-patterns](../skills/product-roadmaps/references/anti-patterns/roadmap-anti-patterns.md) and [bad prioritization](../skills/product-roadmaps/references/anti-patterns/bad-prioritization.md) for details.

### 7. Plan the group alignment session

Once all one-on-ones are complete, produce a recommended agenda for the follow-up group session (co-creation workshop or formal presentation). The book recommends holding this regularly — every quarter or every year depending on business velocity.

Suggested agenda (co-creation workshop format):

| Segment | Duration | Activity |
|---------|----------|----------|
| Intro | 5 min | Agenda and ground rules |
| Hopes and Fears | 10 min | Post-it exercise: one hope and one fear per participant |
| Vision and Goals | 10 min | Validate shared product vision; use MadLibs prompt if needed |
| Back-plan | 15 min | Work backward from future vision to present; each step must be realistic |
| Sizing and Prioritizing | 40 min | $100 test to narrow focus; tally by desirability, feasibility, viability; finalize via discussion |
| Wrap-up | 10 min | Confirm priorities, document decisions, assign next steps |

Remind the user: the $100 test is a good way to narrow focus to a manageable list for discussion, but not a good way to prioritize on its own — use it to generate the discussion list, not to make final calls.

---

## Output

This command produces:

1. **Stakeholder table** — full list with roles and internal/external classification
2. **Shuttle Diplomacy Canvas** (private) — one row per stakeholder tracking outcomes, metrics, priorities, and political considerations
3. **GROW meeting guide cards** — one per stakeholder, ready to use in one-on-one sessions
4. **Synthesis report** — shared priorities, conflicts, and trade-off recommendations after all one-on-ones
5. **Group alignment session agenda** — structured workshop plan for the final buy-in meeting

---

## Verify

The shuttle diplomacy process has succeeded when:

- Every stakeholder's top priorities appear somewhere in the roadmap or synthesis report (they feel heard)
- All identified conflicts have a documented trade-off recommendation
- At least one shared priority is validated across three or more stakeholders
- The group alignment session agenda is confirmed and scheduled
- No decisions made in the group session require re-opening unless significant new information has emerged

---

## Notes

- **Alignment ≠ consensus.** The book is explicit: "People with differing opinions can still align on their intentions." Do not seek unanimous agreement — seek shared understanding of goals and clear accountability for the decision.
- If themes are still expressed as features rather than outcomes, run [`transform-features-to-themes.md`](transform-features-to-themes.md) before proceeding.
- For a detailed view of the alignment and buy-in patterns, see [alignment and buy-in](../skills/product-roadmaps/references/patterns/alignment-and-buyin.md).
- For guidance on presenting the final roadmap to different audiences after alignment is achieved, see [presenting and sharing](../skills/product-roadmaps/references/patterns/presenting-and-sharing.md).
- If the roadmap has broader structural health issues, run [`assess-roadmap-health.md`](assess-roadmap-health.md) first.
- **Persisting results:** This command does not ship with a dedicated template. To archive the stakeholder canvas and synthesis, write them to `./artifacts/shuttle-YYYY-MM-DD.md` as plain markdown. For the structured roadmap and theme files this workflow aligns stakeholders on, see [`${CLAUDE_PLUGIN_ROOT}/skills/product-roadmaps/templates/`](${CLAUDE_PLUGIN_ROOT}/skills/product-roadmaps/templates/).
