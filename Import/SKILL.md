# Good Living Co Portfolio Management Skill

## CORE PROJECT CONTEXT

**Project Owner:** Adam Turton, 40, Manchester. Operations Manager at Starling Bank.

**Mission:** Build a portfolio of 7 passive income sites to generate £3k–£8k/month by year 2-3.

**Status:** All 7 sites live. Technical foundation complete. Revenue ramp in progress: affiliate links to deploy, GA4 setup needed, KDP book 8 to publish.

**All sites built on:** Next.js 14 + TypeScript + Tailwind CSS shared framework template.

---

## THE 7 SITES (Quick Reference)

| # | Site Name | Domain | Niche | Target Audience | Accent | Vercel | GitHub |
|---|---|---|---|---|---|---|---|
| 1 | Good Living Co (GLWC) | goodlivingco.co.uk | Male testosterone & hormone optimisation | UK men 40+ | `#C0392B` | glwc-framework | glwc-framework |
| 2 | LiftLab | liftlab.co.uk | Evidence-based hypertrophy | UK men 25-45 | `#84CC16` | liftlab-framework | liftlab-framework |
| 3 | Fuel Optimal | fueloptimal.co.uk | Male nutrition optimisation | UK men 35-55 | `#D97706` | fuel-optimal-framework | fuel-optimal-framework |
| 4 | GLP-1 Guide UK | glp1guide.co.uk | GLP-1 medications in the UK | UK adults | `#E2E8F0` | glp1-framework | glp1-framework |
| 5 | TradePick | tradepick.co.uk | Vertical SaaS reviews | UK small businesses | `#3B82F6` | tradepick-framework | tradepick-framework |
| 6 | AI By Role | aibyrole.co.uk | AI tools by job role | UK professionals | `#818CF8` | aibyrole-framework | aibyrole-framework |
| 7 | Remote Pivot | remotepivot.co.uk | Career change to remote work | UK non-tech workers | `#F59E0B` | remotepivot-framework | remotepivot-framework |

---

## TECHNICAL STACK & ARCHITECTURE

### Core Framework
- **Next.js 14.2.3** with TypeScript
- **Tailwind CSS** for styling
- **next-mdx-remote/rsc** for MDX content rendering (server-side)
- **@vercel/analytics** for traffic monitoring
- All sites deployed on **Vercel**

### Design System (GLC Design System)
```
- void:      #0a0a0a (darkest background)
- surface:   #111111 (main background)
- elevated:  #161616 (cards, elevated surfaces)
- border:    #222222 (dividers, borders)
- offwhite:  #e0e0e0 (primary text)
- light:     #a0a0a0 (secondary text)
- muted:     #666666 (tertiary text, metadata)
```

### Typography
- **Headings (800/900 weight):** Inter font
- **Display/Logo:** Bebas Neue

### Content Structure
All content lives as `.mdx` files in three directories:
- `/content/guides/` — In-depth guides (1500+ words)
- `/content/lists/` — Listicles & roundups
- `/content/articles/` — News, quick tips, shorter content

### Deployment & Infrastructure
- **GitHub Org:** errorpleasetryagain
- **Vercel Team:** errorpleasetryagains-projects
- **Analytics:** @vercel/analytics imported in layout.tsx
- **Email:** ConvertKit (Kit) form ID: 9259384 (single signup form across all sites)

---

## CRITICAL BUILD & DEPLOYMENT RULES

### MDX Content Rules (MUST FOLLOW)
1. **Never use bare `<` before non-letter characters** — breaks compilation
   - ❌ `< 50 calories`
   - ✅ `&lt; 50 calories`
   - Apply to: `<`, `<=`, `>>`, `<<`, or any operator starting with `<`

2. **Always escape HTML entities in MDX:**
   ```mdx
   The protocol is &lt;= 8 weeks.
   Use &gt; 500g protein daily.
   ```

### Next.js Config Rules
1. **layout.tsx:** ALL import statements must come before any const declarations
   ```typescript
   // CORRECT ORDER:
   import SomeComponent from '...';
   const config = {...};
   export default function RootLayout() {...}
   ```

2. **next.config.js:** Must include these exact settings:
   ```javascript
   const nextConfig = {
     typescript: { ignoreBuildErrors: true },
     eslint: { ignoreDuringBuilds: true },
   };
   export default nextConfig;
   ```

3. **NEVER use:** `experimental: { mdxRs: true }` — incompatible with next-mdx-remote

4. **@vercel/analytics:** If imported in layout.tsx, must exist in package.json

### Pre-Push Validation
**ALWAYS run before git push:**
```bash
python validate-before-push.py
```
This checks for common build failures and MDX syntax errors.

---

## KEY FILES & DIRECTORIES

### Shell Scripts
- **`/Passive websites/push-all-repos.sh`** — Pushes all 7 frameworks to GitHub in sequence. Use when deploying fixes to all sites.

### Validators & Utilities
- **`/Passive websites/validate-before-push.py`** — Pre-push linter. MUST run before every git push.

### Portfolio Hub
- **`/Passive websites/glc-hub/index.html`** — Landing page for goodlivingco.co.uk portfolio hub

### Email Automation
- **`/Passive websites/kit-sequences/all-welcome-sequences.md`** — All 7 Kit welcome sequences (written, awaiting deployment)

### Kindle/KDP Content
- **`/Passive websites/kindle/`** — Directory containing all 8 Kindle manuscripts and cover designs

---

## THE 8 KINDLE BOOKS

| # | Title | Status | ASIN |
|---|---|---|---|
| 1 | TRT in the UK: The Complete Patient Roadmap | Published | TBC |
| 2 | The UK Testosterone Diet | Published | TBC |
| 3 | Remote Work Career Change | Published | TBC |
| 4 | GLP-1 Nutrition Guide | Published | TBC |
| 5 | Aesthetic Hypertrophy Guide | Published | TBC |
| 6 | AI at Work | Published | TBC |
| 7 | The Anabolic Breakdown | Published | A3OZA09IJRI9MQ |
| 8 | Performance Pharmaceuticals: The UK Man's Complete Reference | Draft Complete | — |

**Pending:** Upload Book 8 manuscript to KDP (draft is ready).

---

## MONETISATION STACK

| Revenue Source | Platform | Commission | Notes |
|---|---|---|---|
| **Supplements** | Amazon UK | 3-10% | Primary: protein, vitamins, minerals |
| — | iHerb | 5-10% | International supplements |
| — | Bulk Powders | 10% | UK supplement retailer |
| **TRT/Hormone Clinics** | Optimale | £30-£100/ref | Private TRT provider |
| — | Balance My Hormones (BMH) | £30-£100/ref | Private TRT provider |
| — | Leger Clinic | £30-£100/ref | Private clinic partner |
| **Testing** | Medichecks | 10-15% | Home blood test kits |
| — | Monitor My Health | 10-15% | Specialist testing |
| **Wearables** | Garmin | 5-10% | Fitness trackers |
| — | Oura | 5-10% | Ring wearables |
| — | WHOOP | 5-10% | Strap wearables |
| **SaaS (TradePick)** | Various software | 20-50% recurring | Enterprise tools |
| **SaaS (AIByRole)** | Various AI tools | 20-40% recurring | AI platforms |
| **Ebooks** | Gumroad | 70-100% margin | Self-published |
| — | KDP | 70% margin | Amazon Kindle |
| **Email List** | ConvertKit | Owned channel | First-party email audience |

---

## CONTENT VOICE & STYLE RULES

### Core Voice
Write like **Andrew Huberman meets a credible bloke you'd have a pint with**: evidence-grounded, intelligent, plain English, no hype.

### Essential Rules
1. **UK English always:** colour, optimise, programme, honour, etc. Never American spellings.

2. **Evidence-based, not bro science:**
   - Cite real studies, not Instagram claims
   - Acknowledge uncertainty when it exists
   - No "proven to" claims without evidence

3. **Plain language:**
   - Write for intelligent people without jargon
   - Short sentences. Shorter paragraphs.
   - Active voice > passive

4. **Direct and breezy:**
   - No waffle, no filler, no generic AI writing
   - Sound like you've actually lived the stuff you're writing about
   - Write like a credible 40-year-old who knows the topic

5. **NEVER use these words:**
   - "Genuinely"
   - "Honestly"
   - "Straightforward"
   - "Deep dive"
   - Generic marketing phrases

### Tone by Site
- **GLWC & Fuel Optimal:** Pragmatic, science-first, slightly irreverent
- **LiftLab:** Technical but accessible, peer-to-peer
- **GLP-1 Guide:** Clinical but human, practical UK focus
- **TradePick & AIByRole:** Business-focused, ROI-obsessed
- **Remote Pivot:** Honest about the pain, practical solutions

---

## CURRENT WORK PRIORITIES (As of March 2026)

### High Priority (Revenue-Blocking)
1. **Deploy push-all-repos.sh** — Push all latest fixes to GitHub & Vercel
2. **Replace 61 placeholder affiliate links** with real referral codes:
   - Amazon tag (one per site)
   - Medichecks code
   - Optimale/BMH/Leger referral links
   - iHerb code
   - MyProtein code
   - Bulk Powders code
   - Udemy codes
   - FlexJobs affiliate link
3. **Set up Google Analytics 4** — One property per site, configured in layout.tsx
4. **Set up Google Search Console** — One per site, submit sitemaps, monitor crawl errors

### Medium Priority (Launch Blockers)
5. **Load Kit welcome sequences** — 7 sequences written in kit-sequences/all-welcome-sequences.md; awaiting ConvertKit deployment
6. **Upload Book 8 to KDP** — Performance Pharmaceuticals manuscript complete, ready for publishing
7. **Deploy GLC portfolio hub** — goodlivingco.co.uk currently points to temporary page; replace with /glc-hub/index.html
8. **Deploy TradePick, AIByRole, RemotePivot to production** — Currently in staging on Vercel

### Lower Priority (Growth Tasks)
9. **Expand content on lower-traffic sites** — TradePick and AIByRole need 10-15 more high-quality guides each
10. **Build YouTube channels** — Companion channels for GLWC, LiftLab, GLP-1 Guide (infrastructure ready, content creation pending)

---

## HOW TO WORK ON THIS PROJECT

### Before Starting Any Task
1. **Know which site(s)** you're working on (or if it's cross-site)
2. **Check the accent colour** — used in buttons, highlights, CTAs
3. **Know the target audience** — write for them specifically, not everyone

### When Writing Content
- **Give full drafts, not outlines** (unless specifically asked for outlines)
- Use the voice guidelines above religiously
- Never use bare `<` symbols in MDX — always escape to `&lt;`
- Aim for 1500+ words for guides, 800+ for lists, 400+ for articles
- Include at least 3 credible sources per guide (studies, expert sites, etc.)

### When Writing Code
- Run `validate-before-push.py` before every git push
- Check next.config.js has the two required fields
- Ensure layout.tsx has all imports at the top
- Test MDX compilation locally before committing
- Use the GLC Design System colours consistently

### When Deploying
- Always push via GitHub first (validates pre-commit hooks)
- Vercel auto-deploys on GitHub push
- Monitor Vercel deployment logs for build failures
- If MDX fails: check for bare `<` symbols or import order issues

### When Adding Features
- Think long-term and scalable (this portfolio will grow to 10+ sites)
- New features should be deployable across all 7 sites if relevant
- Document any new build dependencies in this skill

---

## QUICK TROUBLESHOOTING

| Problem | Cause | Solution |
|---|---|---|
| **MDX compilation fails** | Bare `<` in content | Use `&lt;` instead |
| **Build fails with "module not found"** | Missing import in layout.tsx | Move all imports to top of file, before const declarations |
| **@vercel/analytics error** | Not in package.json | Add to dependencies: `npm install @vercel/analytics` |
| **Vercel build fails silently** | ESLint/TypeScript errors ignored | Check Vercel logs; likely next.config.js missing `ignoreBuildErrors` |
| **Form not submitting** | Kit form ID incorrect or stale | Verify form ID is 9259384 across all sites |
| **Accent colour not applying** | Tailwind cache | Clear .next and rebuild: `rm -rf .next && npm run build` |

---

## CRITICAL REMINDERS

1. **Always validate before push:** Run validate-before-push.py
2. **Escaping in MDX:** `<` → `&lt;`, `>` → `&gt;` (when before non-letters)
3. **UK English:** colour, optimise, centre, honour — no American spellings
4. **Voice first:** Evidence, plain language, direct tone — no hype, no bro science
5. **One Kit form:** ID 9259384 — all sites use the same signup form
6. **GitHub org:** errorpleasetryagain — all repos live here
7. **Vercel team:** errorpleasetryagains-projects — deployment target

---

## USEFUL LINKS & COMMANDS

```bash
# Deploy all 7 sites
bash /Passive\ websites/push-all-repos.sh

# Validate before pushing
python /Passive\ websites/validate-before-push.py

# Build locally
npm run build

# Start dev server
npm run dev

# View analytics
# → Vercel dashboard: vercel.com/errorpleasetryagains-projects
```

---

## RELATED CLAUDE SKILLS

This portfolio may benefit from concurrent use of:
- **affiliate-expert** — for monetisation strategy and link placement
- **seo-expert** — for content optimisation and keyword targeting
- **kindle-kdp** — for eBook publishing and KDP optimization
- **youtube-video-creator** — for video content production
- **email-marketing-expert** — for Kit sequences and email campaigns

---

**Last Updated:** March 2026
**Skill Version:** 1.0
**For Questions:** Refer to /Passive websites/ project root
