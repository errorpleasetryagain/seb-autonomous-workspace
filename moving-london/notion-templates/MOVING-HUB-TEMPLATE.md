# Moving Hub — Notion Workspace Setup

## Create New Workspace

1. Go to **notion.so**
2. Click **"New workspace"** (bottom left sidebar)
3. Name it: **"Moving to London — Adam & Amy"**
4. Invite Amy: Click **Settings** → **Members** → **Invite** → Enter Amy's email

---

## Create These Pages

### 🏠 Main Dashboard (Home Page)

**Cover image:** London skyline or Bow/Hackney photo  
**Icon:** 🏠

**Content structure:**

```
# Moving to London — Adam & Amy

**Target Move Date:** July 2026  
**Budget:** £2,300-2,500 pcm  
**Areas:** Bow (E3), Hackney (E8/E9)

## Quick Links
- [🏠 Property Tracker](#property-tracker)
- [📅 Viewings](#viewings)
- [✅ Applications](#applications)
- [💰 Finance Tracker](#finance-tracker)
- [📋 Moving Checklist](#moving-checklist)
- [📄 Documents](#documents)

## This Week's Action Items
[ ] Review new scraper results (Saturdays)
[ ] Book 2-3 viewings
[ ] Update savings progress

## Savings Progress
[Embed Google Sheets Finance Tracker here]
```

---

### 🏠 Property Tracker (Database)

**Database type:** Table (with gallery view option)  
**Properties:**

| Property | Type | Title |
|----------|------|-------|
| Property Name | Title | (auto from scraper) |
| Price | Number | £2,300-2,500 |
| Bedrooms | Number | 1-2 |
| Bathrooms | Number | - |
| Location | Select | Bow, Hackney Wick, Hackney Central, etc. |
| Postcode | Text | - |
| Agent | Text | - |
| Link | URL | Rightmove/Zoopla link |
| Images | Files & Media | - |
| Description | Text | - |
| Date Added | Date | - |
| Status | Select | New, Viewing Booked, Applied, Rejected, Offer Accepted |
| Priority | Select | 🔴 High, 🟡 Medium, 🟢 Low |
| Notes | Text | Your thoughts |

**Views to create:**
- **All Properties** (Table)
- **New This Week** (Filter: Date Added = Last 7 days)
- **To View** (Filter: Status = Viewing Booked)
- **Shortlist** (Filter: Priority = High)

---

### 📅 Viewings (Database)

**Database type:** Calendar + Table

| Property | Type | Title |
|----------|------|-------|
| Property | Relation | Link to Property Tracker |
| Date/Time | Date | Include time |
| Type | Select | In-person, Virtual |
| Agent Name | Text | - |
| Agent Contact | Phone/Email | - |
| Address | Text | - |
| Feedback | Text | After viewing |
| Rating | Select | ⭐⭐⭐⭐⭐, ⭐⭐⭐⭐, ⭐⭐⭐, ⭐⭐, ⭐ |
| Follow-up | Checkbox | - |

**Views:**
- **Calendar** (by Date/Time)
- **Upcoming** (Filter: Date ≥ Today)
- **Completed** (Filter: Date < Today)

---

### ✅ Applications (Database)

| Property | Type | Title |
|----------|------|-------|
| Property | Relation | Link to Property Tracker |
| Date Applied | Date | - |
| Status | Select | Submitted, References Requested, Approved, Rejected, Holding Deposit Paid |
| Deposit Paid | Number | £ - |
| References Needed | Checkbox | - |
| Guarantor Needed | Checkbox | - |
| Right to Rent | Checkbox | - |
| Contract Sent | Checkbox | - |
| Move-in Date | Date | - |
| Notes | Text | - |

---

### 💰 Finance Tracker

**Option A:** Embed Google Sheets (recommended for formulas/charts)  
**Option B:** Build native Notion database (simpler, less powerful)

If using Google Sheets:
1. Create sheet (see `/finance-tracker/` folder)
2. In Notion: `/embed` → Paste Google Sheets share link
3. Set to "Can view" for Amy

---

### 📋 Moving Checklist (Database)

**Database type:** Board (by status) + Checklist

| Task | Type | Title |
|------|------|-------|
| Task Name | Title | - |
| Category | Select | Finance, Property, Utilities, Admin, Packing, Removals |
| Due Date | Date | - |
| Assigned To | Select | Adam, Amy, Both |
| Status | Select | Not Started, In Progress, Done |
| Priority | Select | High, Medium, Low |
| Notes | Text | - |

**Pre-populated tasks** (see `/timeline/` folder for full list)

---

### 📄 Documents (Database)

| Document | Type | Title |
|----------|------|-------|
| Document Name | Title | - |
| Type | Select | Reference, Contract, ID, Proof of Income, Right to Rent, Guarantor |
| Status | Select | Needed, Requested, Received, Uploaded |
| File | Files & Media | Upload PDFs/images |
| Expiry Date | Date | For IDs, etc. |
| Notes | Text | - |

**Documents to collect:**
- [ ] Employer reference (both)
- [ ] Previous landlord reference (if applicable)
- [ ] Right to Rent (passport/visa)
- [ ] Proof of income (payslips, 3 months)
- [ ] Guarantor info (if needed)
- [ ] ID (passport/driving licence)

---

## Notion MCP Integration

Once workspace is created, I can push scraper results directly via MCP.

**To connect:**
1. Install Notion integration (if not already done)
2. Share databases with integration
3. I'll configure the scraper to push to your Property Tracker database

---

## Share Settings

- **Workspace:** Private (just Adam + Amy)
- **Individual pages:** Keep private unless you want to share with removals company, etc.
- **Finance Tracker:** If using Google Sheets, share with "Anyone with link can view" or invite Amy directly
