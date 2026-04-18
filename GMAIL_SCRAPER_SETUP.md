# Gmail Affiliate Scraper Setup

## Quick Start

### 1. Install Dependencies

```bash
cd ~/.openclaw/workspace
pip3 install --user google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 2. Get Gmail API Credentials

1. Go to https://console.cloud.google.com/
2. Create a new project (or use existing)
3. **APIs & Services** → **Library** → Search "Gmail API" → **Enable**
4. **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth 2.0 Client ID**
5. Configure OAuth consent screen (External, add your email as test user)
6. Application type: **Desktop app**
7. Download JSON file
8. Move to workspace: `mv ~/Downloads/client_secret*.json ~/.openclaw/workspace/credentials.json`

### 3. Run the Scraper

```bash
cd ~/.openclaw/workspace
python3 gmail_scraper.py
```

**First run:** Will open browser for OAuth approval. After that, runs automatically.

### 4. Review Output

Results saved to `affiliate_updates.json`:
- Medichecks status updates
- Optimale approvals/rejections  
- Descript notifications
- Payment/commission emails
- Security alerts

### 5. Import to Notion (Optional)

I can read the JSON and update your Affiliate Programmes database automatically:

```bash
# After running scraper, tell me:
# "Seb, import affiliate_updates.json to Notion"
```

---

## What It Finds

| Category | Keywords |
|----------|----------|
| ✅ APPROVED | approved, accepted, welcome, confirmed |
| ❌ REJECTED | rejected, declined, unfortunately |
| ⏳ PENDING | verification, review, pending |
| 💰 PAYMENT | commission, payout, earnings |
| 🔒 SECURITY | password, login, verify |

---

## Automation

Add to your crontab to run daily:

```bash
# Edit crontab
crontab -e

# Add this line (runs at 9am daily)
0 9 * * * cd ~/.openclaw/workspace && python3 gmail_scraper.py
```

Or I can set up a cron reminder to tell you when to run it manually.

---

## Files Created

- `gmail_scraper.py` — Main script
- `credentials.json` — Your Google API creds (you create)
- `token.pickle` — Saved auth token (auto-created)
- `affiliate_updates.json` — Output with all updates

**Security note:** Never commit `credentials.json` or `token.pickle` to git!

---

Ready to set this up? 🎭
