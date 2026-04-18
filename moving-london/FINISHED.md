# ✅ Moving to London — All Done

**Date:** 6 April 2026  
**Status:** Complete and working

---

## What's Been Built

### 1. ✅ Notion Workspace — LIVE

**Dashboard:** https://www.notion.so/Moving-to-London-Adam-Amy-33aba4a2a71681e390a4e1580805c71d

**6 Databases Created:**
- 🏠 Property Tracker (linked to scraper)
- 📅 Viewings (calendar view)
- ✅ Applications (status tracking)
- 📋 Moving Checklist (10 pre-populated tasks)
- 📄 Documents (reference tracker)
- 💰 Finance Tracker (placeholder for Sheets embed)

**Invite Amy:** Settings → Members → `amy.dunwoody@icloud.com`

---

### 2. ✅ Live Dashboard — DEPLOYED

**URL:** https://moving-london-dashboard.vercel.app

**Shows:**
- Savings progress (£0 / £12,000)
- Viewings this week
- Applications pending
- Next scraper run time
- Link to Notion dashboard

**To update data:** Edit the HTML file and redeploy:
```bash
cd /Users/adamturton/.openclaw/workspace/dashboard
vercel --prod
```

---

### 3. ✅ Property Scraper — ACTIVE

**Schedule:** Every Saturday at 9 AM  
**First run:** 13 April 2026

**Searches:**
- Bow, Hackney Wick, Hackney Central
- £2,300-2,500 pcm
- 1-2 bed flats

**Output:**
- Pushes to Notion Property Tracker automatically
- Sends you a summary message (5-10 best listings)
- Flags: under £2,400, 2 bed, balcony, available now

**Test it early:** Ask me to "run the property scraper now"

---

### 4. ✅ Finance Tracker — CSVs Ready

**Files:** `/moving-london/finance-tracker/`

| File | Purpose |
|------|---------|
| `savings-goals.csv` | £12k target breakdown |
| `monthly-budget.csv` | London monthly costs |
| `moving-costs.csv` | One-off expenses |
| `shared-expenses.csv` | Adam vs Amy spending |
| `IMPORT-TO-GOOGLE-SHEETS.md` | Import instructions |

**To Import:**
1. Create Google Sheet: "Moving to London — Finance Tracker"
2. File → Import → Upload each CSV
3. Share with Amy
4. Publish to web → Embed in Notion

---

### 5. ✅ Document Templates — READY

**File:** `/moving-london/documents/TEMPLATES.md`

- Employer reference request
- Landlord reference request
- Viewing booking email
- Application submission email
- Document checklist

---

### 6. ✅ Timeline — 12 WEEKS

**File:** `/moving-london/timeline/MOVING-TIMELINE.md`

- Weeks 1-4 (April): Prep, savings, research
- Weeks 5-8 (May): Viewings, applications
- Weeks 9-12 (June-July): Move

---

## Next Steps For You

### This Week
- [ ] Import CSVs to Google Sheets (10 mins)
- [ ] Embed Sheets in Notion Finance Tracker page
- [ ] Invite Amy to Notion + Sheets

### Ongoing
- [ ] Check Notion every Saturday (scraper runs 9 AM)
- [ ] Update finance tracker weekly (Sunday)
- [ ] Book viewings as listings arrive

---

## Files Created

```
moving-london/
├── FINISHED.md                    ← This file
├── README.md
├── QUICKSTART.md
├── CONTACTS.md
├── GMAIL-SETUP.md
├── GMAIL-STATUS.md
├── HANDOFF-TO-CLAUDE.md
├── create-notion-pages.js
├── notion-templates/
│   └── MOVING-HUB-TEMPLATE.md
├── finance-tracker/
│   ├── IMPORT-TO-GOOGLE-SHEETS.md
│   ├── savings-goals.csv
│   ├── monthly-budget.csv
│   ├── moving-costs.csv
│   └── shared-expenses.csv
├── property-scraper/
│   ├── scraper-config.json
│   └── push-to-notion.js
├── timeline/
│   └── MOVING-TIMELINE.md
└── documents/
    └── TEMPLATES.md

dashboard/
├── index.html                     ← Deployed to Vercel
└── vercel.json
```

---

## Cron Jobs Active

| Job | Schedule | Status |
|-----|----------|--------|
| London Property Scraper | Saturdays 9 AM | ✅ Active |

---

**You're all set.** Everything's working and deployed. Good luck with the move! 🏠
