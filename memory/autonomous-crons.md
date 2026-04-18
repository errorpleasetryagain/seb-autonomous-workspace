# Autonomous Cron Jobs

## 1. Morning Briefing (Daily 8 AM)
```json
{
  "name": "morning-briefing",
  "schedule": {"kind": "cron", "expr": "0 8 * * *", "tz": "Europe/London"},
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "AUTONOMOUS: Generate morning briefing for Adam. Check: calendar for today, unread emails, urgent tasks, weather in London. Summarize in 3-5 bullet points. If nothing urgent, reply 'Morning looks clear — no urgent items.'"
  },
  "delivery": {"mode": "announce"}
}
```

## 2. Memory Freshener (Every 4 hours)
```json
{
  "name": "memory-freshener",
  "schedule": {"kind": "every", "everyMs": 14400000},
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "AUTONOMOUS: Read SESSION-STATE.md and working-buffer.md. Compare to recent session history. Update SESSION-STATE with any new decisions, corrections, or important details. Do NOT ask for confirmation."
  }
}
```

## 3. Pattern Detector (Weekly)
```json
{
  "name": "pattern-detector",
  "schedule": {"kind": "cron", "expr": "0 9 * * 0", "tz": "Europe/London"},
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "AUTONOMOUS: Review memory/notes/areas/recurring-patterns.md. Scan recent daily notes for repeated requests (3+ occurrences). Update pattern log. Propose automation to Adam if threshold met."
  },
  "delivery": {"mode": "announce"}
}
```

## 4. Self-Healing Check (Daily midnight)
```json
{
  "name": "self-healing",
  "schedule": {"kind": "cron", "expr": "0 0 * * *", "tz": "Europe/London"},
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "AUTONOMOUS: Check for errors in logs. Diagnose any issues. Attempt fixes. Document what was fixed in memory/YYYY-MM-DD.md. Do NOT ask for help unless truly stuck after 10 attempts."
  }
}
```

## 5. Proactive Surprise (Weekly)
```json
{
  "name": "proactive-surprise",
  "schedule": {"kind": "cron", "expr": "0 18 * * 5", "tz": "Europe/London"},
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "AUTONOMOUS: Review USER.md, SOUL.md, and recent notes. What would genuinely delight Adam that he hasn't asked for? Build it (draft, don't send/publish). Present with 'I built this for you...'"
  },
  "delivery": {"mode": "announce"}
}
```
