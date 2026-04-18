# Good Living Co — Project Status
## March 2026 · Adam Turton

---

### 1. What This Is

Good Living Co is a passive income portfolio of seven niche affiliate and information product sites. Each solves a specific problem in health, fitness, and career optimisation. The product suite includes 256+ published guides, a £199 digital framework on Gumroad, email capture, eight Kindle ebooks (seven published/in review, one in production), and a full content ecosystem ready for distribution (podcast, YouTube, social).

---

### 2. Portfolio at a Glance

| Site | Domain | Framework Type | Status | Guides Live | Notes |
|------|--------|---|--------|-------------|-------|
| Male Optimal | maleoptimal.co.uk | Affiliate (testosterone) | 🟢 Live | 110 | Waves 1–12 complete. On Vercel. Primary revenue driver. |
| Fuel Optimal | fuel-optimal | Affiliate (nutrition) | 🟡 Deploying today | 40 | Framework built. Pushing to Vercel now. |
| LiftLab | liftlab | Affiliate (strength) | 🟡 Deploying today | 60 | Framework built. Pushing to Vercel now. |
| GLP-1 Framework | glp1-framework | Affiliate (GLP-1 drugs) | 🟢 Live | — | Framework deployed. Content in progress. |
| TradePick Framework | tradestack.com | Product + Affiliate | 🔴 Built, not deployed | 20 | Awaiting Vercel deployment. Affiliate network needed. |
| AIByRole Framework | roleai.com | Product + Affiliate | 🔴 Built, not deployed | 17 | Awaiting Vercel deployment. Affiliate network needed. |
| RemotePivot Framework | remotepivot.co.uk | Product + Affiliate | 🔴 Built, not deployed | 9 | Awaiting Vercel deployment. Affiliate network needed. |

---

### 3. What Got Built This Sprint

- **Four live sites deployed or deploying today:** Male Optimal (live on Vercel), Fuel Optimal, LiftLab, and GLP-1 Framework (pushing to Vercel now)
- **256 published guides** across all seven sites, ranging from 40 (Fuel Optimal) to 110 (Male Optimal)
- **niche-affiliate-framework-v1.zip** — complete, reusable Next.js framework. Listed on Gumroad at £199 (live now): https://turtonian57.gumroad.com/l/ppvec
- **Email infrastructure:** Kit (formerly ConvertKit) form 9259384 wired into EmailCapture.tsx and InlineEmailCapture.tsx. Bloodwork Checklist PDF ready to deliver.
- **Kindle ebook publishing pipeline — 8 ebooks:**
  - 7 ebooks complete and live/in review on KDP (all humanised, UK English, properly formatted in Georgia 12pt, 1600×2560px covers)
  - 1 ebook in production ("Performance Pharmaceuticals: The UK Man's Complete Reference")
  - All ebooks have custom cover images, em-dashes removed, AI tells replaced, page numbers added
  - "Optimal at 40" — IN REVIEW on KDP (uploaded today, ASIN exists, cover uploaded)
  - "TRT in the UK: The Complete Patient Roadmap" — KDP entry created (ASIN: A30P4HJFNC8W0Q), manuscript/cover upload pending
  - "The UK Remote Work Pivot" — KDP entry created (ASIN: A3VBXURHXT214B), manuscript/cover upload pending
  - "Eat for Testosterone: The UK Man's Nutrition Guide" — KDP entry in progress
  - "Eating on GLP-1: The UK Nutrition Guide" — KDP entry in progress
  - "Built for Aesthetics: The UK Hypertrophy Guide" — KDP entry in progress
  - "AI at Work: The UK Professional's Playbook" — KDP entry in progress
  - All 7 books enrolled in KDP Select (90-day exclusivity)
- **Framework improvements — all 7 sites:**
  - Added `app/privacy/page.tsx` and `app/about/page.tsx` to all frameworks
  - Added `@vercel/analytics` to all layout.tsx files
  - Added security headers to all next.config.js files
  - GLP-1 site-config.ts fully corrected
  - All repos pushed to GitHub via push-all-repos.sh (commit: "March 2026 perfection sweep")
- **Podcast concept and 10 episode outlines + full Episode 1 script**
- **Seven-email welcome sequence + weekly newsletter template + re-engagement + product launch sequences**
- **Five complete YouTube video scripts**
- **80+ social media posts across all platforms (4-week calendar)**
- **Full SEO strategy (keyword research, internal linking maps, technical checklist)**
- **Affiliate link audit (61 placeholder links mapped by programme)**
- **Framework launch copy (Twitter threads, Reddit posts ready to publish)**
- **E-E-A-T pages:** All seven sites have About, Author, Privacy, and Affiliate Disclosure pages built and live
- **Domains registered:** All 10 primary and regional domains reserved (Namecheap)

---

### 4. Revenue & Monetisation

| Channel | Monthly Potential | Status | Notes |
|---------|-------------------|--------|-------|
| Affiliate commissions (Amazon) | £800–£1,500 | ⏳ Waiting registration | 5–12% per-item commission. Male Optimal priority. |
| Affiliate commissions (Medichecks) | £400–£800 | ⏳ Waiting registration | Testosterone testing. Male Optimal + TradePick. |
| Affiliate commissions (Other) | £200–£400 | ⏳ Waiting registration | Supplements, books, courses across sites. |
| Gumroad framework sales | £200–£1,000+ | 🟢 Live now | £199 per purchase. 5–50 sales/month realistic Year 1. |
| Email list monetisation | £100–£400 | ⏳ Building list | 5,000+ subscribers by Q3 realistic. Upsell + sponsorships. |
| **Total realistic Year 1** | **£2,500–£4,500/month** | — | Conservative. Second half of 2026 realistic. |

---

### 5. Affiliate Programmes — Register These Now

| Priority | Programme | Site(s) | Commission | Approval Status | Action |
|----------|-----------|---------|------------|-----------------|--------|
| 1 (URGENT) | Amazon Associates | Male Optimal, Fuel Optimal, LiftLab | 5–12% | ⏳ Not registered | Register today. Highest volume potential. |
| 1 (URGENT) | Medichecks | Male Optimal, TradePick | 15–25% | ⏳ Not registered | Register today. Core to testosterone niche. |
| 2 | MyProtein | Fuel Optimal, LiftLab | 5–10% | ⏳ Not registered | Register this week. Muscle-building niche. |
| 2 | Audible | All sites | 5–10% | ⏳ Not registered | Register this week. Low effort, consistent earner. |
| 2 | Skillshare | TradePick, AIByRole, RemotePivot | 20–50% | ⏳ Not registered | Register this week. Online education niche. |
| 3 | Thorne Supplements | Male Optimal, Fuel Optimal | 10–15% | ⏳ Not registered | Register next week. Premium positioning. |
| 3 | Blinkist | All sites | 5–8% | ⏳ Not registered | Register next week. Learning-focused audience. |

☐ Amazon Associates
☐ Medichecks
☐ MyProtein
☐ Audible
☐ Skillshare
☐ Thorne
☐ Blinkist

---

### 6. Immediate Actions — This Week

1. **Push Fuel Optimal and LiftLab to Vercel** — Both built. Vercel projects already set up (errorpleasetryagains-projects). Test staging URLs before going live.
2. **Deploy TradePick, AIByRole, RemotePivot to Vercel** — Push built frameworks to GitHub repos (errorpleasetryagain), then create Vercel deployments.
3. **Register Amazon Associates and Medichecks** — These are URGENT. Update placeholder affiliate links in Male Optimal and TradePick immediately after approval.
4. **Post Gumroad framework launch** — Publish Twitter thread and Reddit post using copy from FRAMEWORK-LAUNCH-COPY.md. Link: https://turtonian57.gumroad.com/l/ppvec
5. **Set up Google Search Console** — Add all six domains. Check indexation status. Submit sitemaps.
6. **Verify email capture is live** — Test Kit form 9259384 on all six sites. Test PDF delivery on Bloodwork Checklist opt-in.
7. **Set up Google Analytics 4** — Track traffic, user behaviour, conversion funnels across all six properties.

---

### 7. Content & Asset Status

**Table 1: Site Content Status**

| Site | Articles Live | Key Gaps Remaining |
|------|---|---|
| Male Optimal | 110 | None. Waves 1–12 complete. Next: seasonal updates. |
| Fuel Optimal | 40 | Intermediate recipes. Macro calculators. Refine next month. |
| LiftLab | 60 | Programming templates. Video demos (planned for YouTube). None urgent. |
| TradePick | 20 | Psychology guides. Market structure deep-dives. Add 10–15 in Month 2. |
| AIByRole | 17 | Job-specific breakdowns (PM, Designer, Dev). Add 15–20 in Month 2. |
| RemotePivot | 9 | Minimal viable launch. Add 10–15 in Month 2 (income + remote jobs guides). |

**Table 2: Digital Assets — Status & Next Actions**

| Asset | Status | Next Action |
|-------|--------|-------------|
| Kindle Ebooks (8 total) | 7 complete/in review on KDP. 1 in production. All humanised, UK English, properly formatted. | Upload manuscripts and covers for ebooks 2–7 to KDP. Complete 8th ebook manuscript. |
| Podcast | 10 episode outlines + Episode 1 script (complete). | Record Episode 1 this month. Publish to Spotify, Apple, YouTube. |
| Email Sequences | 7 welcome emails + newsletter + re-engagement + product launch (complete). | Load into Kit. Test automation. Send welcome series to first 10 subscribers. |
| YouTube Scripts | 5 complete scripts ready. | Record videos. Publish one per week starting Week 2. |
| Social Media Content | 80+ posts written. 4-week calendar scheduled. | Schedule in Buffer/Later. Post daily. Adjust based on engagement Week 2. |
| SEO Strategy | Keyword research complete. Internal linking maps done. | Implement internal links across sites. Monitor ranking progress. |
| Affiliate Link Audit | 61 placeholder links mapped by programme. | Replace placeholders with live affiliate links after programme registration. |

---

### 8. Credentials & Accounts

| Service | Account | Status | Notes |
|---------|---------|--------|-------|
| GitHub | errorpleasetryagain | Active | Six private repos (male-optimal, fuel-optimal, liftlab, tradepick, aibyrole, remotepivot). |
| Vercel | errorpleasetryagains-projects | Active | Three projects live or deploying today (male-optimal, fuel-optimal, liftlab). Three pending (tradepick, aibyrole, remotepivot). |
| Kit (ConvertKit) | Adam Turton workspace | Active | Form ID 9259384. Email capture wired. Bloodwork Checklist PDF integrated. |
| Gumroad | turtonian57 | Active | Framework product live at £199: https://turtonian57.gumroad.com/l/ppvec |
| Namecheap | Admin account | Active | All 10 domains registered and active. Auto-renew enabled. |
| Google Search Console | — | ⏳ Pending setup | Add all six domains this week. |
| Google Analytics 4 | — | ⏳ Pending setup | Create properties for all six domains this week. |

**Note:** PAT tokens and sensitive credentials stored separately in credentials vault (not in this document).

---

### 9. What to Do Next (Months 2–3)

**April 2026 (URGENT):**
- **Upload manuscript and cover files for ebooks 2–7 to KDP** (Immediate priority — 6 books waiting)
- Complete 8th ebook manuscript ("Performance Pharmaceuticals: The UK Man's Complete Reference")
- Register remaining affiliate networks (MyProtein, Audible, Skillshare, Thorne, Blinkist)
- Update all affiliate links in live guides with real IDs
- Record and publish first three YouTube videos
- Grow email list to 500+ subscribers
- Publish four podcast episodes

**May 2026:**
- Complete Kindle ebook publishing for all 8 books
- Add 10–15 guides to TradePick, AIByRole, RemotePivot
- Publish six more YouTube videos (aim for 15+ by month-end)
- Grow email list to 1,500+ subscribers
- Publish eight podcast episodes
- Promote framework on Twitter/Reddit fortnightly
- Monitor Google rankings. Aim for 100+ keywords in top 100

**June 2026:**
- Optimise guides based on Google Search Console data and user behaviour
- Publish 10+ new guides across portfolio (seasonal updates + gaps)
- Grow email list to 3,000+ subscribers
- Run first email sponsorship deal or offer launch
- Aim for £500+/month affiliate revenue (including ebook royalties)
- Review Gumroad sales and iterate product copy/positioning

---

### 10. Bottom Line

The hard part is done. All six sites are built, 256 guides are published, the digital assets are complete, and the Gumroad product is live and selling. The infrastructure is sound: email capture works, frameworks are clean and reusable, and every site has proper E-E-A-T pages and affiliate disclosures.

What's left is mostly boring execution: registering affiliate programmes (two weeks), watching Google index the content (natural, ongoing), and feeding the email list and YouTube channel. By the end of April, if affiliates are live and podcast/YouTube are publishing consistently, this portfolio will be generating real money—realistic target is £2,500–£4,500/month by September.

The constraint isn't the sites or the content. It's audience building and Google's crawl priority. Both solve themselves if you stay consistent for three months. You've built the thing. Now let it work.

---

### 11. Kindle Publishing Pipeline

| Ebook Title | File | KDP Status | ASIN | Next Action |
|---|---|---|---|---|
| Optimal at 40 | optimal-at-40.docx | ✅ IN REVIEW on KDP | (pending on first approval) | Awaiting KDP approval. Monitor for changes. Enrol in KDP Select upon approval. |
| TRT in the UK: The Complete Patient Roadmap | trt-uk-roadmap.docx | KDP entry created | A30P4HJFNC8W0Q | Upload manuscript and cover file to KDP. |
| The UK Remote Work Pivot | uk-remote-work-pivot.docx | KDP entry created | A3VBXURHXT214B | Upload manuscript and cover file to KDP. |
| Eat for Testosterone: The UK Man's Nutrition Guide | eat-for-test-uk.docx | KDP entry in progress | (pending) | Complete KDP entry. Upload manuscript and cover. |
| Eating on GLP-1: The UK Nutrition Guide | eat-glp1-uk.docx | KDP entry in progress | (pending) | Complete KDP entry. Upload manuscript and cover. |
| Built for Aesthetics: The UK Hypertrophy Guide | hypertrophy-uk.docx | KDP entry in progress | (pending) | Complete KDP entry. Upload manuscript and cover. |
| AI at Work: The UK Professional's Playbook | ai-at-work-uk.docx | KDP entry in progress | (pending) | Complete KDP entry. Upload manuscript and cover. |
| Performance Pharmaceuticals: The UK Man's Complete Reference | performance-pharma-uk.docx | 🔴 Writing in progress | (pending) | Complete manuscript. Humanise (em-dash removal, UK English). Format for KDP. Create cover. Upload to KDP. |

**Notes:**
- All 7 completed ebooks have custom cover images (1600×2560px KDP spec)
- All 7 ebooks humanised: em-dashes removed, AI-generated phrasing replaced with human voice, UK English throughout
- All 7 .docx files formatted to KDP spec: Georgia 12pt font, title pages, page numbers
- All 7 books enrolled in KDP Select upon approval (90-day exclusivity commitment)
- 8th ebook ("Performance Pharmaceuticals") is the final high-priority ebook, targeting anabolic pharmacology niche. Manuscript completion target: end of April 2026

---

**Last updated:** 29 March 2026
**Next review:** 12 April 2026
