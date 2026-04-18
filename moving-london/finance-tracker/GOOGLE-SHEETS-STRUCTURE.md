# Finance Tracker — Google Sheets Structure

Create a new Google Sheet: **"Moving to London — Finance Tracker"**
Share with Amy (edit access)

---

## Tab 1: Dashboard

**Purpose:** At-a-glance view of savings progress and monthly budget

| Metric | Target | Current | Progress |
|--------|--------|---------|----------|
| Total Savings Needed | £12,000 | £0 | 0% |
| Monthly Savings Goal | £1,000 | £0 | - |
| Months to Move | 12 | 12 | - |
| Bolton Rent (current) | £XXX | - | - |
| London Rent (target) | £2,400 | - | - |

**Formula for progress bar:**
```
=IF(C2>0, C2/B2, 0)
```
Format as percentage, add conditional formatting (green fill)

**Monthly Budget Comparison:**

| Category | Bolton | London | Difference |
|----------|--------|--------|------------|
| Rent | £XXX | £2,400 | =C2-B2 |
| Council Tax | £XXX | £XXX | =C3-B3 |
| Utilities | £XXX | £XXX | =C4-B4 |
| Transport | £XXX | £XXX | =C5-B5 |
| Groceries | £XXX | £XXX | =C6-B6 |
| **Total** | =SUM(B2:B6) | =SUM(C2:C6) | =C7-B7 |

---

## Tab 2: Savings Goals

**Breakdown of the £12k target:**

| Item | Target | Saved | Remaining | % Complete |
|------|--------|-------|-----------|------------|
| Deposit (6 weeks) | £5,400 | £0 | £5,400 | 0% |
| First Month Rent | £2,400 | £0 | £2,400 | 0% |
| Removals | £800 | £0 | £800 | 0% |
| Emergency Buffer | £3,000 | £0 | £3,000 | 0% |
| Setup Costs (broadband, etc.) | £400 | £0 | £400 | 0% |
| **TOTAL** | £12,000 | £0 | £12,000 | 0% |

**Formulas:**
- Remaining: `=B2-C2`
- % Complete: `=IF(B2>0, C2/B2, 0)` (format as %)

**Monthly Contribution Tracker:**

| Month | Target | Actual | Variance | Notes |
|-------|--------|--------|----------|-------|
| Apr 2026 | £1,000 | £0 | £0 | - |
| May 2026 | £1,000 | £0 | £0 | - |
| Jun 2026 | £1,000 | £0 | £0 | - |
| ... | ... | ... | ... | ... |

---

## Tab 3: Shared Expenses

**Track who paid what:**

| Date | Item | Category | Amount | Paid By | Split | Adam Owes | Amy Owes | Notes |
|------|------|----------|--------|---------|-------|-----------|----------|-------|
| 06/04/26 | Removals quote | Moving | £800 | Adam | 50/50 | £400 | £400 | Initial quote |
| 06/04/26 | Viewings transport | Travel | £50 | Amy | 50/50 | £25 | £25 | Train tickets |

**Formulas:**
- Adam Owes: `=D2*E2` (if E2 is split %, e.g., 0.5)
- Amy Owes: `=D2*(1-E2)`

**Settlement Summary:**

| Person | Total Paid | Should Pay | Balance |
|--------|------------|------------|---------|
| Adam | =SUMIF(F:F, "Adam", D:D) | =SUM(G:G) | =B2-C2 |
| Amy | =SUMIF(F:F, "Amy", D:D) | =SUM(H:H) | =B3-C3 |

Positive balance = they're owed money. Negative = they owe.

---

## Tab 4: Moving Costs (One-Off)

| Item | Estimated | Actual | Paid | Status |
|------|-----------|--------|------|--------|
| Removals van | £800 | - | No | Quote needed |
| Deposit | £5,400 | - | No | - |
| First month rent | £2,400 | - | No | - |
| Broadband setup | £50 | - | No | - |
| Council tax (first month) | £150 | - | No | - |
| Utilities setup | £100 | - | No | - |
| Cleaning | £200 | - | No | Optional |
| New keys/locks | £100 | - | No | Optional |
| **TOTAL** | £9,200 | £0 | - | - |

---

## Tab 5: Monthly Budget (London)

**Projected monthly costs:**

| Category | Estimated | Actual | Variance |
|----------|-----------|--------|----------|
| Rent | £2,400 | - | - |
| Council Tax (Band C) | £140 | - | - |
| Water | £40 | - | - |
| Energy | £80 | - | - |
| Broadband | £35 | - | - |
| Transport (Zone 1-2) | £160 | - | - |
| Groceries | £400 | - | - |
| Eating out | £200 | - | - |
| Entertainment | £150 | - | - |
| Miscellaneous | £200 | - | - |
| **TOTAL** | £3,805 | £0 | - |

**Note:** Adjust based on actual bills once you move in.

---

## Sharing Settings

1. Click **Share** (top right)
2. Add Amy's email → **Editor** access
3. Optional: File → Share → Publish to web (if you want a read-only dashboard view)

---

## Embed in Notion

1. In Google Sheets: File → Share → Publish to web
2. Copy the link
3. In Notion: `/embed` → Paste link
4. Set to "Can view" if publishing, or share directly with Amy's Notion email

---

## Pro Tips

- **Update weekly:** Every Sunday, log expenses and savings contributions
- **Use conditional formatting:** Green for on-track, red for behind
- **Set up bank alerts:** Most UK banks let you set savings goal notifications
- **Consider a joint savings account:** Starling, Monzo, or Chase have shared pots
