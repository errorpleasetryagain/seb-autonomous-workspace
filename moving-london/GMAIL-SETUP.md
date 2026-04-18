# Gmail Integration Setup — Moving to London

**Purpose:** Let me monitor your emails for:
- Letting agent responses
- Viewing confirmations
- Application updates
- Reference requests
- Tenancy agreements

---

## Option A: Gmail MCP Server (Recommended)

This gives me real-time access to read/search your Gmail directly through OpenClaw.

### Step 1: Install Gmail MCP

```bash
npm install -g @openclaw/mcp-gmail
```

### Step 2: Get Google OAuth Credentials

1. Go to **https://console.cloud.google.com/**
2. Create new project (or use existing): "OpenClaw Gmail Integration"
3. Enable **Gmail API**:
   - APIs & Services → Library → Search "Gmail API" → Enable
4. Create OAuth 2.0 Credentials:
   - APIs & Services → Credentials → Create Credentials → OAuth 2.0 Client ID
   - Application type: **Desktop app**
   - Download the JSON file
5. Save as: `~/.openclaw/gmail-credentials.json`

### Step 3: Authenticate

```bash
openclaw mcp gmail auth --credentials ~/.openclaw/gmail-credentials.json
```

This opens a browser window → sign in with your Gmail → grant permissions → token saved.

### Step 4: Add to OpenClaw Config

Add to your OpenClaw MCP configuration:

```json
{
  "mcpServers": {
    "gmail": {
      "command": "openclaw-mcp-gmail",
      "args": [],
      "env": {
        "GMAIL_CREDENTIALS_PATH": "/Users/adamturton/.openclaw/gmail-credentials.json"
      }
    }
  }
}
```

### Step 5: Test It

Ask me:
- "Show me my recent emails from letting agents"
- "Search for emails about viewings"
- "Any new emails from Rightmove or Zoopla?"

---

## Option B: Gmail Forwarding (Simpler, Less Secure)

Forward specific emails to a webhook or dedicated address I can access.

### Setup:

1. **Gmail Settings** → Forwarding and POP/IMAP → Add forwarding address
2. Forward emails matching filters:
   - From: `@rightmove.co.uk`, `@zoopla.co.uk`, `@foxtons.co.uk`, etc.
   - Subject contains: "viewing", "application", "tenancy", "reference"
3. Forward to: [your choice — could be a Slack webhook, dedicated email, etc.]

**Downside:** Doesn't give me full search access, just forwarded copies.

---

## Option C: Use Existing Python Scraper (Quick Start)

You already have `gmail_scraper.py` in the workspace. We can adapt it for the move.

### What Exists:
- `/Users/adamturton/.openclaw/workspace/gmail_scraper.py` — Affiliate email monitor
- Searches for: Medichecks, Optimale, PartnerStack, etc.

### Adapt for Moving:

I can modify it to search for:
- "viewing", "tenancy", "application", "reference", "deposit"
- From: letting agents, Rightmove, Zoopla, OpenRent

Then run it via cron job (daily) and push results to Notion.

**Setup needed:**
1. Download `credentials.json` from Google Cloud Console (same as Option A)
2. Run once to authenticate: `python3 gmail_scraper.py`
3. Set up cron job to run daily

---

## Option D: Gmail + Make.com Integration (No Code)

Use Make.com (which you already have active) to connect Gmail → Notion.

### Scenario:
1. **Gmail module:** Watch for new emails matching filters
2. **Filter:** Subject/From contains "viewing", "tenancy", etc.
3. **Notion module:** Create page in Applications database

**Pros:** No OAuth setup, visual builder, already integrated
**Cons:** Slight delay (15-min polling), Make.com credits used

---

## My Recommendation

**For the London move:** Use **Option C (Python scraper)** as a quick start, then migrate to **Option A (Gmail MCP)** for long-term use.

### Why:
- You already have the scraper code
- Works immediately once OAuth is set up
- Can run via cron job (daily email summaries)
- Easy to adapt for affiliate emails too

---

## What I'll Do Once Connected

**Daily Email Summary (8 AM):**
- New emails from letting agents
- Viewing confirmations for the week
- Application status updates
- Reference requests needing action

**On-Demand:**
- "Find all emails about [property address]"
- "Show me viewing confirmations for this week"
- "Any emails from Foxtons?"
- "Search for 'reference request' emails"

**Auto-File to Notion:**
- Forward tenancy agreements → Documents database
- Viewing confirmations → Viewings database
- Application emails → Applications database

---

## Next Steps

**To get this working today:**

1. **Download OAuth credentials:**
   - Go to https://console.cloud.google.com/
   - Create project → Enable Gmail API → Download credentials.json
   - Save to `~/.openclaw/gmail-credentials.json`

2. **Tell me when it's done** — I'll run the authentication flow and set up the daily cron job

3. **Optional:** Install Gmail MCP for full integration (better long-term)

---

## Security Notes

- I can only **read** emails (no sending without explicit approval)
- OAuth token stored locally (not shared externally)
- You can revoke access anytime: https://myaccount.google.com/permissions
- I'll only search for moving-related emails (not your entire inbox)

---

**Let me know when you've got the credentials.json downloaded** and I'll handle the rest.
