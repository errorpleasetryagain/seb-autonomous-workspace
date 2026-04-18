# Import Finance Tracker to Google Sheets

## Quick Import (2 Minutes)

### 1. Create New Google Sheet
- Go to: **sheets.google.com**
- Click **"+ Blank"**
- Name it: **"Moving to London — Finance Tracker"**

### 2. Import Each CSV

**For each tab below:**

1. **Create tab** (click "+" at bottom)
2. **Name it** (see tab names below)
3. **File → Import → Upload → Choose CSV file**
4. **Import settings:**
   - Convert text to numbers/dates: ✅ Yes
   - Import range: All cells
5. **Click "Import data"**

---

## Tabs To Create

| Tab Name | CSV File |
|----------|----------|
| `Savings Goals` | savings-goals.csv |
| `Monthly Budget` | monthly-budget.csv |
| `Moving Costs` | moving-costs.csv |
| `Shared Expenses` | shared-expenses.csv |
| `Dashboard` | (create manually, see below) |

---

## Dashboard Tab (Manual Setup)

**Create formulas that reference other tabs:**

### Cell A1: Total Savings Progress
```
=SUM('Savings Goals'!C2:C6)
```

### Cell A2: Total Needed
```
=SUM('Savings Goals'!B2:B6)
```

### Cell A3: Progress %
```
=A2/A3
```
Format as percentage

### Cell A5: Monthly Budget Total
```
=SUM('Monthly Budget'!B2:B11)
```

### Cell A7: Moving Costs Total
```
=SUM('Moving Costs'!B2:B9)
```

---

## Share With Amy

1. Click **Share** (top right)
2. Add: `amy.dunwoody@icloud.com`
3. Permission: **Editor**

---

## Embed In Notion

1. **File → Share → Publish to web**
2. Select **"Entire Document"**
3. Select **"Web page"**
4. Click **Publish**
5. Copy the link
6. In Notion (Finance Tracker page): Type `/embed` → Paste link

---

## CSV Files Location

All in: `/Users/adamturton/.openclaw/workspace/moving-london/finance-tracker/`

- savings-goals.csv
- monthly-budget.csv
- moving-costs.csv
- shared-expenses.csv
