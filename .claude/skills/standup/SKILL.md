---
name: standup
description: Generate a daily standup summary from git log and write a dated log entry. Use when the user wants a summary of what was done today or yesterday, or wants to log their daily standup.
---

# Daily Standup Skill

Generate a concise daily standup from git history and write it to `logs/YYYY-MM-DD.md`.

## Workflow

### 1. Get today's date

```bash
date +%Y-%m-%d
```

### 2. Gather git activity

Run the following to get commits from the last 24 hours across all branches:

```bash
git log --since="24 hours ago" --oneline --all --no-merges
```

Also check for any uncommitted work in progress:

```bash
git status --short
```

### 3. Summarise into standup format

Write a brief standup with these three sections:

```
## Standup — YYYY-MM-DD

### Done
- <bullet per meaningful commit or completed task>

### In Progress
- <anything staged/unstaged or partially done>

### Blockers / Focus Today
- <ask the user: "Any blockers? What's the focus today?" and insert their answer>
```

Keep bullets short — one line each. This is read on mobile.

If there are no commits and no changes, write: "No activity logged."

### 4. Ask the user for blockers/focus

Before writing the file, ask:

> "Any blockers or specific focus for today? (Leave blank to skip)"

Insert their answer under **Blockers / Focus Today**. If blank, write "None."

### 5. Write the log file

Write to `logs/YYYY-MM-DD.md` (create `logs/` directory if it doesn't exist).

### 6. Commit the log

```bash
git add logs/YYYY-MM-DD.md
git commit -m "Add standup log for YYYY-MM-DD"
```

Do not push — the stop hook handles that at session end.

## Wrap up

Confirm the file was written and committed. Show the user the summary inline so they can read it without opening the file.
