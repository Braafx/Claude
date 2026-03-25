---
name: wednesday
description: Run the Wednesday art business day workflow. Structures the full day into morning admin, creation, and business blocks. Picks up from where Tuesday left off. Use at the start of each Wednesday, or when the user wants to plan their art business day.
---

# Wednesday Art Business Day Skill

Wednesday is a dedicated art business day. This skill structures the day so it starts with momentum (not a blank page) and ends with something shipped or progressed.

## Core principle

Continuing beats starting cold. The system is designed so Tuesday ends with a handoff note and Wednesday opens it immediately.

---

## Workflow

### 1. Pick up from Tuesday

Check if `logs/wednesday-handoff.md` exists (or the most recent standup log from Tuesday):

```bash
cat logs/wednesday-handoff.md 2>/dev/null || echo "No handoff note found."
```

If a handoff exists, read it and open with:
> "Picking up from Tuesday: [summary of handoff]. Does this match where your head is, or did something shift?"

If no handoff exists, ask:
> "What's the one thing you most want to move forward today — a specific piece, a task, or figuring that out?"

### 2. Set today's intention (one sentence)

Ask:
> "In one sentence: what does a successful Wednesday look like today?"

Write this to the top of today's log when creating it.

### 3. Present the day structure

Lay out the Wednesday template. Adjust based on what the user said in step 1–2:

---

**WEDNESDAY STRUCTURE**

```
MORNING BLOCK — Create (2–3 hrs, peak energy)
  → Work on the primary art piece or study
  → No admin, no email, no social — just make
  → Use /draw if you need a brief

MID-DAY BLOCK — Business (1 hr)
  → Portfolio: is anything ready to post? Post it.
  → Outreach: 1–3 warm messages (fellow artists, studios, communities)
  → Freelance: check pipeline, follow up on anything open
  → Pricing/admin: invoices, rate research, Notion/tracker updates

AFTERNOON BLOCK — Finish or Learn (1–2 hrs)
  → Finish something from the morning, OR
  → Targeted skill study: pick one weakness, do a focused exercise
  → Can also be a second lighter creative session

END OF DAY — Handoff (15 min)
  → Write the Tuesday→Wednesday note for NEXT week
  → Log what was done
  → Run /standup
```

---

### 4. Check portfolio pipeline

Ask: "Anything finished or nearly finished that could be posted today?"

If yes: help draft the ArtStation / social post description. For concept art posts, the description should include:
- What it is (prop, environment, character)
- Mood/intent in one sentence
- Tools used (Procreate, Photoshop, Clip Studio — whatever applies)
- Any relevant tags: #conceptart #gameart #digitalpainting #environmentdesign etc.

If no: note one piece to target finishing next Wednesday.

### 5. Run the business check (optional, ask first)

> "Want to do a quick 5-min business check-in?"

If yes, cover:
1. **Portfolio visibility:** When did you last post publicly? (If >2 weeks, flag it)
2. **Outreach:** Is there anyone in your network or target industry you should message today?
3. **Freelance:** Any open quotes, briefs, or conversations to follow up?
4. **Rate:** Do you know what you'd charge for a prop sheet? A character turnaround? (If no: we can work that out)

### 6. End-of-day handoff (run at end of Wednesday)

When the user signals they're wrapping up, create `logs/wednesday-handoff.md`:

```markdown
# Wednesday Handoff — YYYY-MM-DD

## Today's win
[one sentence: what moved forward]

## In progress (pick up here)
[specific piece or task + exact stage it's at]

## Next Wednesday priority
[one clear thing to do first]

## Notes
[anything else to remember]
```

Commit the handoff file:
```bash
git add logs/wednesday-handoff.md
git commit -m "Add Wednesday handoff note YYYY-MM-DD"
```

---

## Notes for Claude

- Wednesday is the user's art business day, not a hobby day. Treat it with the same rigour as a work day.
- The user's bottleneck is momentum and structure, not discipline — they already draw daily. The job is to keep the thread alive across weeks.
- If they're starting 4-day weeks soon, Wednesday will be their first fully dedicated art day. Make early Wednesdays feel rewarding so the habit cements.
- Long-term goal: work at Riot Games or equivalent. Each Wednesday is one step. Name it.
- The portfolio post text matters — game studios look at ArtStation. If something is postable, help make the post good.
