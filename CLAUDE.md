# Claude Code — Personal Context

## Who I am

I'm the owner and primary developer of this workspace. I access Claude Code primarily via mobile (remote), so I value **concise, direct communication** — no padding, no filler, no long preambles. Lead with the answer.

I have a safety-first mindset: I built a stop hook that blocks session exit until all changes are committed and pushed. I don't like half-finished states or lost work.

I'm security-conscious: I enforce SSH-signed commits, I've manually vetted my plugin list, and I'm careful about what runs in my environment.

---

## Who I am (extended)

Artist and developer. I draw every day — sketchbook always in my backpack. I work in tech currently but I'm building toward a career as a concept artist in games, film, or TV. Long-term target: Riot Games or comparable AAA/prestige studio. See `LIFE.md` for current goals and `COACHING.md` for the 6-month skill roadmap.

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

## Repository Structure

This repository is my **Claude Code workspace and lab** — configuration, automation, personal productivity workflows, and creative tools.

```
Claude/
├── CLAUDE.md              ← this file — AI context
├── LIFE.md                ← current goals, priorities, non-negotiables (keep it current)
├── COACHING.md            ← 6-month concept art career roadmap
├── requirements.txt       ← Python deps for tools/ (stdlib only by default)
│
├── .claude/
│   ├── settings.json      ← Claude Code hook configuration
│   └── hooks/
│       └── post-edit-lint.sh  ← PostToolUse: auto-runs ruff on .py files after Write/Edit
│
├── .claude/skills/        ← custom slash command skills
│   ├── standup/SKILL.md   ← /standup — daily git log summary → logs/YYYY-MM-DD.md
│   ├── reflect/SKILL.md   ← /reflect — weekly 5-question review → reflections/YYYY-WXX.md
│   ├── draw/SKILL.md      ← /draw   — concept art brief generator
│   ├── post/SKILL.md      ← /post   — artwork → social post pack (4 platforms + monetization)
│   ├── sketch-review/SKILL.md ← /sketch-review — evaluate sketchbook page, pick best
│   ├── project/SKILL.md   ← /project — commission/project tracker
│   └── wednesday/SKILL.md ← /wednesday — structured art business day workflow
│
├── tools/
│   └── newsletter/        ← daily art newsletter tool (Python, stdlib only)
│       ├── run.py         ← entry point: python -m tools.newsletter.run
│       ├── content.py     ← seeded deterministic content picker from data/ pools
│       ├── template.py    ← HTML email renderer
│       ├── emailer.py     ← sends via config.json SMTP settings
│       └── config.example.json
│
├── data/                  ← curated JSON content pools for the newsletter
│   ├── tutorials.json
│   ├── throwbacks.json
│   ├── brushes.json
│   ├── coach_notes.json
│   ├── bonuses.json
│   └── reference_queries.json
│
├── logs/                  ← daily standup entries (YYYY-MM-DD.md) — auto-created by /standup
│   └── wednesday-handoff.md  ← week-to-week continuity note for /wednesday
│
├── reflections/           ← weekly personal reviews (YYYY-WXX.md) — auto-created by /reflect
│
├── social/                ← social post packs — auto-created by /post and /sketch-review
│   └── YYYY-MM-DD-{slug}/
│       └── posts.md
│
├── newsletters/           ← generated newsletter HTML — output of tools/newsletter/run.py
│
└── projects/              ← active commission tracker files — managed by /project
```

---

## Hooks

**PostToolUse hook** (`.claude/hooks/post-edit-lint.sh`):
- Triggered after any `Write` or `Edit` tool call on a `.py` file
- Runs `ruff check --fix --quiet` automatically — no manual step needed
- Silently exits on non-Python files or if ruff isn't found

Configured in `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "Write|Edit", "hooks": [{ "type": "command", "command": "..." }] }
    ]
  }
}
```

---

## Skills Reference

All skills live in `.claude/skills/{name}/SKILL.md` and are invoked as `/name`.

| Skill | Trigger | Output | Commits? |
|-------|---------|--------|----------|
| `/standup` | Any time, daily | `logs/YYYY-MM-DD.md` | Yes |
| `/reflect` | End of week | `reflections/YYYY-WXX.md` | Yes, optionally updates LIFE.md |
| `/draw` | Before a drawing session | Brief in chat (no file) | No |
| `/post` | After finishing a piece | `social/YYYY-MM-DD-{slug}/posts.md` | Yes |
| `/sketch-review` | After a sketchbook session | `social/YYYY-MM-DD-sketch-review/notes.md` | Yes |
| `/project` | Commission management | `projects/{slug}.md` | Yes |
| `/wednesday` | Start/end of Wednesday | `logs/wednesday-handoff.md` | Yes |

**Key skill behaviours:**
- `/standup` and `/reflect` do **not push** — the stop hook handles that at session end
- `/post` and `/sketch-review` save output files and commit them immediately
- `/draw` is chat-only — generates a brief, no filesystem writes
- `/wednesday` wraps the full art business day: morning creative block → mid-day business → afternoon finish → end-of-day handoff note

---

## Newsletter Tool

**Location:** `tools/newsletter/`
**Run:** `python -m tools.newsletter.run`
**Flags:** `--preview` (write HTML, no email) | `--date YYYY-MM-DD` (specific date)

Content is picked **deterministically by date** (MD5 seed) so the same date always generates the same newsletter. No randomness — rerunning is safe.

Content pools in `data/`: tutorials, game art throwbacks, brushes, coach notes, bonuses, reference image queries.

Email requires `tools/newsletter/config.json` (copy from `config.example.json`). Without it, newsletter HTML is written to `newsletters/YYYY-MM-DD.html` and the tool exits with a clear message.

---

## Personal Context

When helping with tasks, be aware that:
- I value **quality over speed**, but not at the cost of paralysis
- I prefer **automation over manual repetition** — if I do something twice, it should be scripted
- I'm **experimentally curious** — willing to try new approaches, but I want to understand what they do before running them
- I think in **systems** — individual tools matter less than how they fit together
- **Concept art career is real and parallel to tech work** — treat `/draw`, `/wednesday`, `/post` with the same rigour as code tasks
