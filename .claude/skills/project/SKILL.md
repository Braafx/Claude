---
name: project
description: Manage active art commissions and projects. Track status, deliverables, specs, and next steps for ongoing work like emotes, game art, and client commissions. Use when the user wants to check project status, update progress, log a delivery, or start a new commission.
---

# Project Tracker Skill

Manage active commissions and personal projects. Keeps status in `projects/` as simple markdown files.

## Active Projects

When invoked, read all files in `projects/` and summarise each one's status.

```bash
ls projects/ 2>/dev/null || echo "No projects directory yet."
```

If projects directory is empty or missing:
> "No active projects tracked yet. Want to start one? Tell me the project name and I'll set it up."

---

## Workflow

### Starting a new project

When the user says "new project" or gives a project name, create `projects/{slug}.md`:

Ask for (or infer from context):
1. Project name
2. Client / who it's for
3. What's being made (emotes, character sheets, environment, etc.)
4. Number of deliverables
5. Deadline (or "ongoing")
6. Agreed rate (or "TBD")
7. Reference images / brief (note where they are)

Create the file:

```markdown
# {Project Name}

**Client:** {client}
**Type:** {type}
**Status:** 🟡 In Progress
**Deadline:** {deadline}
**Rate:** {rate}

## Deliverables

- [ ] {deliverable 1}
- [ ] {deliverable 2}

## Specs

{key technical specs — size, format, colour mode, etc.}

## Brief / Reference

{link to reference files or description of brief}

## Notes

{any client communication, revision notes, agreements}

## Log

| Date | Update |
|------|--------|
| {today} | Project started |
```

---

### Updating a project

When the user gives an update (e.g. "I finished the first emote" or "client sent new refs"):

1. Find the relevant project file
2. Check off completed items
3. Add a log entry with today's date
4. If all deliverables are done, change Status to `✅ Complete`

Commit the update:
```bash
git add projects/
git commit -m "Update {project name}: {brief summary of change}"
```

---

### Reviewing projects

When the user runs `/project` with no arguments, show:

```
Active Projects:
  🟡 Emotes (streamer colleague) — 0/? emotes done
  🟡 Order of Five — Warlord chess piece — 0/1 done

Run /project emotes or /project chess to see details.
```

---

## Project Templates

### Twitch/Discord Emotes

```markdown
## Specs
- Canvas: 112x112px minimum (also export 56x56 and 28x28)
- Format: PNG, transparent background
- Colour mode: RGB
- Style notes: bold silhouette, max 4–5 colours, reads at 28x28
- Animation: static (unless client requests animated)

## Emote Checklist
- [ ] Agree on expressions/poses with client
- [ ] Rough sketches (all poses)
- [ ] Client approval on roughs
- [ ] Linework pass
- [ ] Flat colour pass
- [ ] Shadow/highlight pass
- [ ] Export all 3 sizes
- [ ] Final client delivery + invoice
```

### Game Character / Chess Piece

```markdown
## Specs
- Deliverable: Character sheet (front + 3/4 view + silhouette)
- Format: PNG or PSD, 300dpi minimum
- Style: match game's existing visual language
- Callouts: material, key design details

## Character Sheet Checklist
- [ ] Receive brief + reference from client
- [ ] 3–5 silhouette explorations
- [ ] Client picks direction
- [ ] Rough character sheet
- [ ] Client approval
- [ ] Final line + colour pass
- [ ] Detail callout panel
- [ ] Export + delivery + invoice
```

---

## Notes for Claude

- Keep project files clean and scannable — the user checks these on mobile.
- When a piece is delivered and approved, suggest posting it to ArtStation (it's portfolio material).
- If a project has been idle for >2 weeks, flag it at the next `/project` call.
- Rate reminders: emotes ~£40–60/ea, character sheets ~£100–200/ea for indie games. Adjust based on scope and usage rights.
- When reference images arrive ("I'll send pics"), update the project Brief section immediately.
