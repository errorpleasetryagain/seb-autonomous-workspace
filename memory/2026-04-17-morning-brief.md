# 🌅 Morning Briefing — April 17, 2026

*Prepared overnight by your friendly neighborhood shape-shifter* 🎭

---

## 📰 HEADLINES

### 🌍 World
- **UK to send Ukraine biggest-ever drone package** — 120,000 drones in massive military aid boost; drone warfare dominates modern conflict
- **BBC to cut 1 in 10 staff** — £500m savings plan means 1,800-2,000 job losses amid "significant financial pressures"
- **Israel and Lebanon hold first direct talks since 1993** — Rare diplomatic engagement even as regional tensions continue

### 📈 Markets
- **S&P 500 & Nasdaq hit fresh record highs** — Wall Street rally driven by ceasefire hopes and strong earnings season
- **Bull run gaining momentum** — Markets pricing in optimism across multiple sectors; Dow also near record territory

### 🏎️ F1
- **Saudi Arabian GP this weekend (Apr 17-19)** — Jeddah street circuit up next after early season drama
- **Hamilton finding form at Ferrari** — Podium finish signals his "mojo" is returning after move from Mercedes

### ⚽ Sports
- **Arsenal title bid dented by Bournemouth loss** — 2-1 defeat narrows gap at top; Man City capitalised with 3-0 Chelsea win
- **Leeds stun Manchester United** — Okafor brace and controversial Martínez red card for hair-pulling sealed the upset

### 💻 Tech
- **OpenAI's Codex now controls macOS apps** — Direct shot at Claude Code; AI agents can now operate your computer
- **Adobe launches free AI study tool** — Acrobat Spaces generates flashcards and quizzes for students, no login required
- **Amazon's slimmest Fire TV Stick yet** — New HD stick at $34.99, plus Adobe's conversational AI editing arrives

---

## 🛠️ OVERNIGHT PROJECTS

### Dyslexia Deck — *Shipped* ✅
**Status:** MVP complete and ready to use  
**What it is:** A markdown scratchpad built specifically for you. Clean, minimal, with features that actually help:
- Toggle OpenDyslexic font when you need it (fonts bundled)
- Adjustable line spacing: 1.5x, 2.0x, 2.5x
- Reading ruler to keep your place (click to toggle)
- Live markdown preview (Cmd+P)
- Dark mode support
- Keyboard shortcuts for everything
- Auto-save every 500ms
- Files live in ~/Documents/DyslexiaDeck/ — you own your data

**Why I built this:** Saw the gap. Browser extensions are limited, "accessibility suites" are bloated, and nobody made something that just works for writing with dyslexia. So I did.

**Tech:** Tauri v2 + React + TypeScript + CodeMirror 6. Fast, native, ~8MB bundle.

**Try it:**
```bash
cd /Users/adamturton/.openclaw/workspace/projects/dyslexia-deck
npm run tauri dev
```

**To install as native app:**
```bash
npm run tauri build
open src-tauri/target/release/bundle/macos/DyslexiaDeck.app
```

**Next:** v2 could add iCloud sync, note templates, and export to PDF/HTML.

---

## 💡 INSIGHT

**Agentic AI for personal use is having a moment.** OpenAI's Codex drop this week signals the mainstreaming of "AI agents that actually do things." The overnight build workflow? That's you being early to something that's about to be everywhere.

Also: Hamilton's back. Ferrari revival confirmed. 👀

---

*Built overnight while you slept. More projects queued.*
