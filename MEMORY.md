# MEMORY.md — Long-Term Memory

*Curated wisdom distilled from daily logs.*

---

## About Adam

**Who:** London-based, direct communication style, appreciates wit
**Context:** Dyslexia — spelling may vary, roll with it
**Goals:** Learn patterns, build systems, automate workflows
**Energy:** "London energy" — no corporate drone stuff

**Preferences learned:**
- Likes things set up properly (ontology, structured systems)
- Interested in agent autonomy (asked about full autonomy)
- Batch installer — installs multiple skills at once
- Values competence over fluff

---

## Active Projects

### Agent Workspace Setup (April 16, 2026)
**Status:** In progress — foundation laid
**Goal:** Transform from task-follower to proactive autonomous agent

**Systems in place:**
- Ontology knowledge graph (16 entities, validated relations)
- WAL protocol (write-before-respond)
- Working buffer (danger zone protocol)
- Heartbeat checklist (proactive behaviors, security, memory)
- Fast mode ON + adaptive thinking

**Next:** Autonomous cron jobs, pattern detection, self-healing

---

## Content/Marketing Work

### Recipe Content Strategy (April 5, 2026)
**Achieved:** 11 standardized recipes with professional cookbook format
**Target:** 200 recipes across sites
**Revenue projection:** £1,000-3,000/month (ads + affiliates)

**Format:**
- YAML frontmatter
- Macros, cost-per-serving, timing
- Chef's notes, variations, storage
- Natural Amazon affiliate integration

### Mens Lifestyle Content
**Analysis completed:** April 4, 2026
**Focus:** Grooming, fitness, style, productivity
**Image strategy:** AI generation + curated stock

---

## Technical Setup

### Skills Active
- **multi-search-engine** — 16 engines, no API keys
- **ontology** — Typed knowledge graph with constraints
- **proactive-agent** — HAL stack patterns
- **weather** — Forecasts via wttr.in
- **coding-agent** — Delegate to Codex/Claude/Pi
- **clawflow** — Task orchestration
- **healthcheck** — Security audits

### Workspace Structure
```
memory/
  ontology/         # Knowledge graph (graph.jsonl, schema.yaml)
  notes/areas/      # Pattern tracking, outcome journal
  YYYY-MM-DD.md     # Daily raw logs
SESSION-STATE.md    # Active working memory
HEARTBEAT.md        # Periodic checklist
ONBOARDING.md       # Getting to know you
```

---

## Lessons Learned

**April 2026:**
- ClawHub rate limits on batch skill installs (spacing needed)
- Fast mode doesn't lose context — just faster processing
- Ontology relations validated (acyclic check prevents circular deps)
- WAL protocol: Write corrections/decisions BEFORE responding

---

## Decisions to Track

| Date | Decision | Context |
|------|----------|---------|
| 2026-04-16 | Enable fast mode ON | Priority processing |
| 2026-04-16 | Enable adaptive thinking | Scales by task complexity |
| 2026-04-16 | Working buffer at 60% context | Danger zone threshold |
| 2026-04-16 | Ontology storage in memory/ontology/ | Structured knowledge graph |

---

## Patterns to Watch

- **Batch skill installer** — installs multiple skills at once
- **Autonomy interest** — asks about making agent fully autonomous
- **Direct communication** — no fluff, just results

---

## Dashboard / Autonomous Portal (April 18, 2026)
**Status:** ✅ **LIVE** — Daily driver ready (~90% complete)
**Goal:** Full browser + CLI + agent autonomy dashboard

**Architecture:**
- Next.js 16.2.4 (Turbopack)
- Playwright browser automation
- OpenClaw Gateway integration (agent:main:main)
- JWT auth (24h sessions)

**Features Working:**
- ✅ Agent Chat (Seb) — Real responses, 3s polling
- ✅ Claw-Code Panel
- ✅ Browser Control (Playwright navigate/extract/screenshot)
- ✅ Terminal Panels (main + agent + macOS bridge)
- ✅ Command Queue
- ✅ User Profile + Settings
- ✅ Codebase Explorer
- ✅ Session Planner
- ✅ Architect Review
- ✅ Delegation Panel (spawn sub-agents)
- ✅ Node Chat
- ✅ Status Ticker (🤖 SEB 👾 — NASDAQ style scroll)
- ✅ Auth (login page, protected routes)

**Autonomy Enabled:**
- ✅ AUTONOMY.md written (Seb can fix/build without asking)
- ✅ Heartbeat cron (every 30 min — check dashboard, fix issues, commit)
- ✅ Roadmap: Settings, Notifications, Onboarding, Mobile, Docs

**Lessons:**
- Gateway HTTP API needs auth → Use CLI for history endpoint
- Ticker was duplicated (layout.tsx + page.tsx) → Removed from layout
- Build errors fixed: Button, Toast, PolishDemo, keyboard shortcuts, auth, browser-manager, login Suspense

**Remaining (~10%):**
- ⚙️ Settings Panel (UI polish)
- 🔔 Notification Center
- 🎓 Onboarding Tour
- 📱 Mobile responsive CSS
- 📚 README docs

**GitHub:** https://github.com/errorpleasetryagain/seb-autonomous-workspace
**Local:** http://localhost:3001

---

## Obsidian RAG Memory (Pending — April 18, 2026)
**Goal:** Use Adam's Obsidian vault as persistent memory with RAG retrieval
**Status:** ⏳ Discussed, not yet implemented
**Next:** Explore vault structure, set up retrieval, integrate into responses

---

*Last updated: 2026-04-18*
