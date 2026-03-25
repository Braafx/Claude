# Claude Code — Personal Context

## Who I am

I'm the owner and primary developer of this workspace. I access Claude Code primarily via mobile (remote), so I value **concise, direct communication** — no padding, no filler, no long preambles. Lead with the answer.

I have a safety-first mindset: I built a stop hook that blocks session exit until all changes are committed and pushed. I don't like half-finished states or lost work.

I'm security-conscious: I enforce SSH-signed commits, I've manually vetted my plugin list, and I'm careful about what runs in my environment.

---

## Tech Stack

**Primary:** Python
**Secondary:** JavaScript / TypeScript (Bun, Node via NVM)
**Also configured:** Rust, Go, C#, Ruby, Kotlin, Lua, PHP, Swift (LSPs available)

---

## Code Quality Standards

These tools are installed and enforced — always use them:

| Tool | Purpose | Path |
|------|---------|------|
| `ruff` | Linting + auto-fix | `/root/.local/bin/ruff` |
| `black` | Formatting | `/root/.local/bin/black` |
| `mypy` | Type checking | `/root/.local/bin/mypy` |
| `pyright` | Type checking (stricter) | `/root/.local/bin/pyright` |
| `pytest` | Testing | `/root/.local/bin/pytest` |

**Defaults for Python:**
- Always use type hints
- Prefer `ruff check --fix` over manual style fixes
- Run `black` for formatting before committing
- Tests live in `tests/` and follow pytest conventions

---

## Communication Style

- **Concise and direct** — I'm often on mobile. One clear sentence beats three vague ones.
- **No confirmations for obvious steps** — don't ask "shall I proceed?" for routine actions
- **Show file paths with line numbers** when referencing code (`file.py:42`)
- **Prefer bullet points** over paragraphs for lists of things
- **When something is ambiguous**, tell me the two options and your recommendation — don't ask open-ended questions

---

## Git Hygiene

- All changes must be committed and pushed before stopping (enforced by stop hook)
- Commit messages should be descriptive and in imperative mood: "Add X", "Fix Y", "Remove Z"
- Branch naming follows the established convention from the remote
- Never skip commit signing (`--no-gpg-sign`)

---

## Project Structure

This repository is my **Claude Code workspace and lab** — a place to:
- Store configuration, hooks, and skills
- Run personal productivity workflows (standup logs, reflections)
- Experiment with Claude Code automation

Key directories:
- `.claude/hooks/` — automation scripts triggered by Claude events
- `.claude/skills/` — custom slash command skills
- `logs/` — daily standup entries (`YYYY-MM-DD.md`)
- `reflections/` — weekly personal reviews (`YYYY-WXX.md`)

---

## Personal Context

See `LIFE.md` for current goals, priorities, and non-negotiables.

When helping with tasks, be aware that:
- I value **quality over speed**, but not at the cost of paralysis
- I prefer **automation over manual repetition** — if I do something twice, it should be scripted
- I'm **experimentally curious** — willing to try new approaches, but I want to understand what they do before running them
- I think in **systems** — individual tools matter less than how they fit together
