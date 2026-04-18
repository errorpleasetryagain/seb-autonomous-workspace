# The Niche Affiliate Site Framework

**A complete Next.js 14 niche affiliate website — ready to clone, reskin, and rank.**

Built by someone who actually runs these sites. Not a tutorial. Not a boilerplate. A working engine.

---

## What You're Getting

### The Complete Setup
- **Next.js 14 App Router** with MDX content pipeline — write content in Markdown, publish instantly
- **Full SEO infrastructure** out of the box: auto-generated sitemap.xml, robots.txt, JSON-LD Article schema, OpenGraph tags, Twitter cards, canonical URLs, and generateMetadata on every page
- **Three content types**: /guides/ (long-form cornerstone content), /lists/ (affiliate roundups and comparisons), /articles/ (blog posts)
- **Single configuration file** — change your site name, URL, tagline, and description in one place. Everything else updates automatically.
- **Vercel deployment ready** — deploy in under 10 minutes with zero configuration
- **MDX frontmatter system**: title, excerpt (auto-becomes meta description), author, date, pillar, audience, and sections
- **Mobile responsive by default** — tested and optimized for all devices
- **Clean and fast** — no bloat, no unnecessary dependencies, built for performance

### What's NOT Included

**Content.** This framework is a technical foundation — not a content business. You bring the niche knowledge; the framework handles everything else.

What you need to provide:
- Your niche and angle
- Your articles (guides, comparisons, reviews)
- Your affiliate programme accounts
- Your domain name

Two example content files are included (`example-guide.mdx` and `example-money-page.mdx`) to show you exactly how the content system works. Delete them and write your own.

**This is not a done-for-you site.** If you want someone to build the site *and* write the content, that's a different (more expensive) service. This framework is for people who know their niche and want a technical head start.

### What You Need
- Node.js 18 or higher
- A GitHub account (free)
- A Vercel account (free tier works for most niche sites)
- Basic comfort with the terminal (copy/paste commands is fine)

### Setup in 5 Steps

**Step 1: Clone the repo**
```bash
git clone [your-download-link] my-niche-site
cd my-niche-site
npm install
```

**Step 2: Configure your site**
This is the only file you need to edit: `lib/site-config.ts`

```typescript
export const siteConfig = {
  name: "Your Site Name",
  url: "https://yourdomain.com",
  tagline: "Your tagline here",
  description: "Your meta description — appears in Google search results",
  author: "Your Name",
  email: "your-email@example.com",
  twitter: "yourhandle",
  linkedIn: "yourprofile",
  github: "yourprofile",
}
```

That's it. Navigation, footer, structured data, and everything else pulls from this file automatically.

**Step 3: Run locally**
```bash
npm run dev
```
Visit `http://localhost:3000`. You'll see your site live with hot reload — changes appear instantly.

**Step 4: Write your first guide**
Create a new file: `content/guides/your-first-article.mdx`

```mdx
---
title: "The Best Testosterone Boosters for Beginners"
excerpt: "A practical guide to the top testosterone-boosting supplements. What actually works."
date: "2026-03-01"
author: "Your Name"
pillar: "supplements"
audience: "beginners"
sections: 3
---

# The Best Testosterone Boosters for Beginners

Start writing here. Standard Markdown works — **bold**, *italic*, links, code blocks, everything.

## How to Choose a Booster

Your content here.

## The Top 5 Products

[Buy on Amazon](https://amzn.to/yourcode) — affiliate link example

## FAQ

Standard markdown formatting. That's all you need.
```

The excerpt becomes your meta description. The date controls publish order. The pillar groups content together for your site structure.

**Step 5: Deploy to Vercel**
1. Push your repo to GitHub
2. Go to vercel.com, click "New Project"
3. Select your repo
4. Vercel auto-detects Next.js — just click "Deploy"
5. Add your custom domain in Vercel settings
6. Live in minutes

### Adding More Pages

**Guides** (`/content/guides/`) — Your cornerstone content. 2,000–8,000 words. Target primary keywords. Example: "The Best Testosterone Boosters," "Complete Guide to Creatine."

**Lists** (`/content/lists/`) — Comparison and roundup content. Ideal for affiliate monetization. Example: "Best Creatine Supplements 2026," "Top 5 Clothing Brands for Fitness."

**Articles** (`/content/articles/`) — Shorter, fresher content. 1,000–2,500 words. News, updates, how-tos. Drives ongoing traffic and updates your feed.

**Images**: Place them in the `public/` folder (e.g., `public/images/my-image.jpg`) and reference them in MDX:
```mdx
![Image alt text](/images/my-image.jpg)
```

**New pillars**: Edit `lib/site-config.ts` and add a new pillar object. Create a new folder in `/content/` for that pillar. The framework auto-generates the pillar page.

### SEO — What's Already Done For You

Everything below is automatically generated and live on your site:

- **Sitemap.xml** — Lists all your pages for Google
- **robots.txt** — Tells search engines where to crawl
- **JSON-LD Article schema** — Structured data for Google to understand your content
- **OpenGraph tags** — Your excerpts display nicely on Twitter, LinkedIn, and Facebook
- **Twitter Cards** — Same as OG, optimized for Twitter
- **Canonical URLs** — Prevents duplicate content issues
- **Meta descriptions** — Auto-generated from your excerpt

**What you need to do:**
1. Build your site and deploy to Vercel
2. Go to Google Search Console (google.com/webmasters)
3. Add your domain
4. Paste your sitemap URL: `https://yourdomain.com/sitemap.xml`
5. Click "Request indexing"
6. Wait 1–2 days for your first pages to appear in Google

That's it. The technical SEO is done. Your job is writing better content than your competitors.

### Affiliate Links

Use standard Markdown links. No special syntax needed:

```mdx
[Product Name](https://your-affiliate-link-here)
```

That's it. The framework doesn't assume any affiliate network. Use Amazon Associates, ShareASale, Impact, whatever works for your niche.

### Email Capture

The framework includes two pre-built components:

1. **EmailCapture** — Full-width email signup section (usually homepage hero)
2. **InlineEmailCapture** — Inline within article content

Both are ConvertKit-ready (but work with any service).

**To connect ConvertKit:**
1. Create a ConvertKit account (free up to 10k subscribers)
2. Go to Integrations → Find your Form ID
3. Open `components/EmailCapture.tsx`
4. Replace `CONVERTKIT_FORM_ID` with your actual ID
5. Done — signups start collecting

If you use a different service (ActiveCampaign, Mailchimp, etc.), the components are minimal and easily adaptable.

### Cloning for a New Niche

One purchase = unlimited sites. Here's how:

```bash
# You've already built one site. Now build a second.
cp -r my-niche-site my-second-niche-site
cd my-second-niche-site

# Update the config for the new niche
# lib/site-config.ts → new name, new domain, new tagline

# Clean out old content
rm -rf content/guides/*.mdx
rm -rf content/lists/*.mdx
rm -rf content/articles/*.mdx

# Write new content for the new niche
# Create new guides, lists, articles

# Push to a new GitHub repo
git remote set-url origin https://github.com/yourname/my-second-niche-site
git push -u origin main

# Connect the new repo to Vercel
# Deploy in under an hour
```

You now have two independent sites, same engine, different niches.

### The Content Strategy That Works

**Start here — "Money pages" first:**
Build your initial traffic with comparison lists and "best of" roundups. These rank faster, convert better to affiliate clicks, and give you cashflow while you build deeper content. Examples: "Best Testosterone Boosters," "Top AI Writing Tools 2026," "Best Hydration Salts for Athletes."

**Find keywords without expensive tools:**
- Google autocomplete: Type your topic in Google, look at suggestions
- AnswerThePublic (free): Shows questions people ask about your topic
- Ahrefs free tier: Use the Keywords Explorer to check competition

**Pillars vs. long-tail:**
- **Pillar content** (your guides): 1–2 per pillar. Broad, authoritative, 4,000+ words. Targets primary keywords.
- **Long-tail content** (your articles and lists): 5–10 per pillar. Narrower topics, 1,000–2,500 words. Targets question-based keywords.

Example structure for a testosterone niche:
- Guides: "The Complete Testosterone Optimization Guide," "Creatine 101"
- Lists: "Best Testosterone Boosters," "Best Pre-Workouts"
- Articles: "Does Creatine Increase Testosterone?" "Protein Powder vs. Whole Food"

---

## FAQ

**Do I need to know React or programming?**
No. If you can write Markdown, you can write content. The framework handles all the technical parts. You never touch React code unless you want to customize styling or components.

**Can I sell the sites I build with this?**
Yes. Build one site, run it yourself. Build three sites and sell them. Build ten and flip them. The sites are yours to monetize however you want.

**Can I resell the framework itself?**
No. Single-user license. You get one purchase, unlimited personal use on your own sites.

**Is this a WordPress theme?**
No. It's a Next.js application. Faster than WordPress (2–3x speed difference), better SEO out of the box, no plugin dependencies, no database needed, and Vercel hosting is free. WordPress is a CMS. This is a static site generator with dynamic capabilities where you need them.

**What hosting does it use?**
Vercel (free tier). Sufficient for 100,000+ monthly visitors with zero cost. If you outgrow the free tier, Vercel's paid plans are $20–$100/month depending on usage. Most niche sites never need to upgrade.

**Can I use my own domain?**
Yes. Buy a domain from any registrar (Namecheap, Google Domains, GoDaddy, etc.). Point it at Vercel in your DNS settings. Takes 10 minutes.

**What if I get stuck?**
Email support is included. Response within 48 hours. If you hit a technical wall, I'll help you unstick it or provide a refund (see refund policy below).

---

## Support

If you run into issues during setup or need help customizing the framework:

**Email:** adam@tradepikconsulting.com

Response within 48 hours. Most issues resolve in one email.

**Refund Policy:** If you can't get the framework running after 30 days of purchase and I can't help you fix it, full refund — no questions. You have to genuinely try though.

---

## What's Next?

1. Clone the repo and run it locally (15 minutes)
2. Update `lib/site-config.ts` with your site info (5 minutes)
3. Write your first three guides (depends on you, but expect 6–12 hours for research and writing)
4. Deploy to Vercel (5 minutes)
5. Submit your sitemap to Google Search Console (5 minutes)
6. Wait for indexing (1–2 weeks for first pages)
7. Publish new content consistently (1–2 times per week)
8. Track traffic in Google Analytics (already hooked up)
9. Earn affiliate commissions

The framework is the foundation. Your content is the business.

Ready to build?
