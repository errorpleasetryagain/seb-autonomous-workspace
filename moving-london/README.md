# Moving to London — Adam & Amy

**Target:** Move by July 2026  
**Budget:** £2,300-2,500/month rent  
**Primary Area:** Bow (E3)  
**Alternatives:** Bethnal Green, Mile End, Hackney Wick, Stratford, Walthamstow, Limehouse

**Contact:**
- Adam: [your email]
- Amy: amy.dunwoody@icloud.com

---

## Project Structure

```
moving-london/
├── README.md                    # This file
├── property-scraper/            # Apify scraper config + cron job
├── notion-templates/            # Notion page structures to duplicate
├── finance-tracker/             # Google Sheets structure + formulas
├── timeline/                    # Week-by-week moving checklist
└── documents/                   # Reference templates (emails, forms, etc.)
```

---

## Weekly Property Scraper

**Schedule:** Every Saturday 9:00 AM  
**Sources:** Rightmove, Zoopla  
**Filters:**
- Location: Bow, Bethnal Green, Mile End, Hackney Wick, Stratford, Walthamstow, Limehouse
- Price: £2,300-2,500 pcm
- Bedrooms: 1-2
- Available: Now or within 4 weeks
- Property type: Flat/Apartment

**Output:** Notion database + weekly summary message

---

## Finance Tracker (Google Sheets)

**Tabs:**
1. **Dashboard** — Savings progress, monthly budget overview
2. **Savings Goals** — Deposit, first month, removals, buffer (£10k+ target)
3. **Monthly Budget** — Bolton vs London cost comparison
4. **Expenses** — Shared + individual spending
5. **Moving Costs** — One-off expenses tracker

---

## Notion Moving Hub

**Databases:**
- 🏠 Properties (scraper results + manual finds)
- 📅 Viewings (scheduled, completed, feedback)
- ✅ Applications (submitted, references, status)
- 📋 Checklist (timeline tasks)
- 📄 Documents (references, contracts, IDs)

---

## Timeline (12 Weeks to Move)

| Week | Focus |
|------|-------|
| 1-4 (Apr) | Savings ramp-up, research, Notion setup |
| 5-8 (May) | Start viewings, get references ready |
| 9-10 (Jun) | Apply to properties, secure tenancy |
| 11-12 (Jul) | Pack, removals, utilities, move in |

---

## Next Steps

- [ ] Set up Apify scraper + cron job
- [ ] Create Notion workspace structure
- [ ] Build Google Sheets finance tracker
- [ ] Draft reference request emails
- [ ] Book removals quotes (week 8)
