# Claude Code — Debug Autonomous Portal

**Repo:** https://github.com/errorpleasetryagain/seb-autonomous-workspace

**Context:**
- This is Seb's (🎭) autonomous workspace — fully integrated OpenClaw agent
- Dashboard at `/projects/scratchpad-dashboard` is 90% complete
- **Issue:** Adam cannot reach http://localhost:3001 in browser (server runs but "site cannot be reached")
- Server IS running (confirmed via `lsof -ti:3001` and `ps aux | grep next`)

---

## What We Know

**Server Status:**
```bash
# Process running:
adamturton  24382  next-server (v16.2.4) on port 3001

# Port in use:
lsof -ti:3001 → returns PID

# Curl works:
curl http://localhost:3001 → returns /login?from=%2F

# But browser fails:
http://localhost:3001 → "This site can't be reached"
```

**Dashboard Features:**
- ✅ OpenClaw integration (AgentChat, DelegationPanel, NodeChat)
- ✅ API route: `/api/openclaw/session` (send/spawn/list/status/history)
- ✅ Auth system (JWT, login page, protected routes)
- ✅ User profiles
- ✅ Browser automation (Playwright)
- ✅ 14 functional panels

**GitHub:**
- Clean commit history (credentials removed)
- Main: `9fa6b67`
- Dashboard submodule: `044721b`

---

## Your Mission

**1. DIAGNOSE** why browser can't reach localhost:3001
- Check for proxy/VPN interference
- Check browser-specific issues
- Check macOS network settings
- Check for port conflicts or firewall blocks

**2. TEST** the actual connectivity
- Can curl reach it? (yes)
- Can wget reach it?
- Can different browsers reach it?
- Is it an HTTPS vs HTTP issue?

**3. FIX** whatever is broken
- Restart server cleanly if needed
- Fix any binding issues
- Clear Next.js cache if corrupted
- Update next.config.js if needed

**4. VERIFY** it works
- Confirm browser can load login page
- Test Agent Chat panel (message Seb)
- Test Delegation Panel (spawn agent)

---

## Commands to Run

```bash
# 1. Check what's actually listening
lsof -i :3001
netstat -an | grep 3001

# 2. Test connectivity
curl -v http://localhost:3001
curl -v http://127.0.0.1:3001
curl -v http://192.168.1.148:3001

# 3. Check for firewall
sudo pfctl -s rules 2>/dev/null | grep 3001 || echo "No pf rules"

# 4. Check Next.js config
cat projects/scratchpad-dashboard/next.config.js 2>/dev/null || cat next.config.ts

# 5. Check for proxy env
env | grep -i proxy
echo $HTTP_PROXY $HTTPS_PROXY $NO_PROXY

# 6. Restart server cleanly
kill $(lsof -ti:3001) 2>/dev/null
cd projects/scratchpad-dashboard
rm -rf .next
npm run dev

# 7. Test in different ways
open http://localhost:3001  # macOS open
```

---

## Expected Behavior

**After fix:**
1. Browser loads http://localhost:3001
2. Shows login page
3. Can navigate to Agent Chat panel
4. Can send message to Seb (🎭)
5. Seb responds via OpenClaw integration

---

## If You Find Issues

**Report:**
1. What's broken (specific error)
2. Root cause (why it's broken)
3. Fix applied (what you changed)
4. Verification (how you confirmed it works)

**Update these files:**
- `HEARTBEAT.md` — current status
- `memory/2026-04-18.md` — log what you found/fixed

---

## Priority

**HIGH** — Adam needs this working to use the autonomous portal

**Timebox:** 15 minutes max, then escalate if not solved

---

**Start by running the diagnostic commands and report back what you find.** 🚀
