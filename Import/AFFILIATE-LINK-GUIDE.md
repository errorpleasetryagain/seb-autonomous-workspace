# How to Add Affiliate Links to Your Sites

A step-by-step guide for swapping placeholder links with real affiliate links across all 7 sites.

## How It Works

Your articles are `.mdx` files in each repo's `/content/` folder. Affiliate links are just normal markdown links:

```markdown
[Product Name](https://affiliate-url-here)
```

That's it. No special components, no plugins. Just links.

## Your Live Affiliate Links

These are confirmed active and ready to use:

| Programme | Link Format | Use On |
|-----------|------------|--------|
| Amazon UK | `https://www.amazon.co.uk/dp/PRODUCT-ID?tag=maleoptimal-21` | Male Optimal, Lift Lab, Fuel Optimal |
| Make.com | `https://www.make.com/en/register?pc=goodlivingco` | AI By Role, Remote Pivot |
| Toggl | `https://get.toggl.com/g1ivv4qgtynz` | AI By Role, Remote Pivot, TradePick |
| Clockify | `https://clockify.me/pricing?fpr=pttinj` | AI By Role, Remote Pivot, TradePick |
| Awin (publisher 2838304) | Per-advertiser (apply via Awin directory) | All sites |
| Skillshare | Via Impact.com (get link from dashboard) | Remote Pivot, AI By Role |

## Step-by-Step: Adding Links in Claude Code (VS Code)

### 1. Open the right repo

```bash
cd ~/Documents/Claude/Projects/Passive\ websites/glwc-framework
```

Change `glwc-framework` to whichever site you're working on:
- `glwc-framework` = Male Optimal
- `liftlab-framework` = Lift Lab
- `fuel-optimal-framework` = Fuel Optimal
- `tradepick-framework` = TradePick
- `aibyrole-framework` = AI By Role
- `remotepivot-framework` = Remote Pivot
- `glp1-framework` = GLP-1 Guide

### 2. Find articles that mention products

Use Claude Code to search:

```
Find all articles in /content/ that mention "Amazon" or "supplement" or "Medichecks"
```

Or search manually:

```bash
grep -rl "placeholder\|YOURCODE\|example\.com\|#affiliate" content/
```

### 3. Open the article and find the link

Links in your articles look like this:

```markdown
We recommend [Medichecks Male Hormone Blood Test](https://medichecks.com/YOURCODE) for a full panel.
```

### 4. Swap the placeholder URL

Change the URL inside the brackets to your real affiliate link:

```markdown
We recommend [Medichecks Male Hormone Blood Test](https://medichecks.com/your-real-referral-code) for a full panel.
```

### 5. Commit and deploy

```bash
git add content/articles/the-article-you-changed.mdx
git commit -m "Add affiliate link for Medichecks"
git push
```

Vercel auto-deploys when you push. Done.

## Quick Reference: What Goes Where

### Male Optimal (maleoptimal.co.uk)
- Amazon UK links for supplements (Vitamin D, Zinc, Magnesium, Ashwagandha, Omega-3)
- Medichecks/Monitor My Health for blood testing kits
- TRT clinic referrals (Optimale, Balance My Hormones, Leger) -- waiting on referral codes
- Wearables (Oura, WHOOP, Garmin) via Amazon UK

### Lift Lab (liftlab.co.uk)
- Amazon UK for supplements and gym gear
- MyProtein via Awin (apply in Awin directory first)

### Fuel Optimal (fueloptimal.co.uk)
- Amazon UK for nutrition supplements
- Meal prep/kitchen tools via Amazon UK

### TradePick (tradepick.co.uk)
- Toggl, Clockify for time tracking
- Jobber, Housecall Pro (when approved) for trade software
- SimplyBook.me, Setmore (when approved) for booking software

### AI By Role (aibyrole.co.uk)
- Make.com for automation
- Toggl, Clockify for productivity
- Descript, Writesonic (when approved) for AI tools

### Remote Pivot (remotepivot.co.uk)
- Make.com for automation
- Toggl, Clockify for time tracking
- Skillshare, Udemy (when approved) for courses
- FlexJobs (when approved) for job boards

### GLP-1 Guide (glp1guide.co.uk)
- Amazon UK for scales, supplements
- Medichecks for blood testing

## Amazon UK Link Format

For any product on Amazon UK:

1. Go to the product page
2. Copy the ASIN (the code in the URL after `/dp/`)
3. Build your link:

```
https://www.amazon.co.uk/dp/ASIN-HERE?tag=maleoptimal-21
```

Example for a Vitamin D supplement:

```
https://www.amazon.co.uk/dp/B01GGOX0KI?tag=maleoptimal-21
```

## The Affiliate Disclosure

Every article with affiliate links needs `affiliateDisclosure: true` in the frontmatter:

```yaml
---
title: "Your Article Title"
affiliateDisclosure: true
---
```

This triggers the disclosure notice on the page. Already set on most articles.

## Bulk Find-and-Replace with Claude Code

If you want to swap all placeholder links at once, tell Claude Code:

```
Search all .mdx files in /content/ for any URLs containing "YOURCODE",
"placeholder", or "example.com" and list them so I can replace them
with real affiliate links.
```

Or to add Amazon tags to bare Amazon links:

```
Find all Amazon UK links in /content/ that don't have ?tag=maleoptimal-21
and add the tag parameter.
```

## What You Still Need

Before you can add links for these, you need the referral codes/URLs:

1. **Medichecks** -- log into your Medichecks affiliate dashboard, copy your referral code
2. **TRT clinics** -- email Optimale, Balance My Hormones, Leger asking about referral programmes
3. **Jobber / Housecall Pro** -- waiting on approval (submitted)
4. **SimplyBook.me / Setmore** -- waiting on approval (submitted via Tapfiliate)
5. **Udemy** -- waiting on Impact.com approval
6. **FlexJobs** -- need to apply

## Tips

- Start with Male Optimal. It has the most articles (156) and the most obvious affiliate opportunities (supplements, testing kits).
- Do one site at a time. Don't try to do all 7 in one go.
- Every link should feel natural in the article. If it reads like an ad, rewrite the sentence.
- Test every link after deploying. Click it, make sure it goes to the right page with your tracking code visible.
