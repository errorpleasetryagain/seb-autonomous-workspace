# Portfolio Audit & Skills Report — 31 March 2026

## Part 1: GitHub Repo Audit (All 7 Sites)

### Summary Table

| Site | Repo | Branch | Git Status | Content | Google Verification |
|------|------|--------|------------|---------|---------------------|
| Male Optimal | glwc-framework | master | Uncommitted changes (verification) | 156 articles | File + meta tag (uncommitted) |
| Lift Lab | liftlab-framework | main | Clean | 79 articles | File + meta tag |
| Fuel Optimal | fuel-optimal-framework | master | Clean | 64 articles | File + meta tag |
| TradePick | tradepick-framework | master | Stuck rebase | 42 articles | File + meta tag |
| AI By Role | aibyrole-framework | master | Stuck rebase | 104 articles | File + meta tag |
| Remote Pivot | remotepivot-framework | master | Stuck rebase | 99 articles | File + meta tag |
| GLP-1 Guide | glp1-framework | master | Clean | 24 articles | File + meta tag |

**Total content across portfolio: 568 articles/pages**

---

### Critical Issues Found

#### 1. Three repos stuck in git rebase (BLOCKING)

TradePick, AI By Role, and Remote Pivot all have interrupted rebases from 30 March. The `.git/rebase-merge` directories are locked and `git rebase --abort` fails with a deadlock error.

**Fix:** From your Mac or Claude Code, run this in each repo:

```bash
cd tradepick-framework && rm -rf .git/rebase-merge && git reset --hard HEAD
cd ../aibyrole-framework && rm -rf .git/rebase-merge && git reset --hard HEAD
cd ../remotepivot-framework && rm -rf .git/rebase-merge && git reset --hard HEAD
```

This is safe — the latest commits are already pushed. The rebase state is just leftover junk.

#### 2. package.json name wrong in 4 repos

LiftLab, TradePick, AI By Role, and Remote Pivot all still say `"name": "glwc-framework"` in their package.json — a leftover from cloning the original framework. Doesn't break anything functionally, but looks unprofessional and could cause confusion in dependency tools.

**Fix:** Update the `name` field in each package.json to match the actual repo name.

#### 3. @vercel/analytics missing from 3 repos

TradePick, AI By Role, and Remote Pivot don't have `@vercel/analytics` installed. The other 4 repos do. This means you're not collecting visitor data on half your sites.

**Fix:** `npm install @vercel/analytics` in each, then add `<Analytics />` to their layout.tsx.

#### 4. GLWC verification changes still uncommitted

The Google verification meta tag and HTML file were added to glwc-framework but never committed/pushed. This is the last piece of the Search Console setup from earlier.

#### 5. Missing .gitignore in GLP-1 repo

Only repo without one. Risk of accidentally committing node_modules or .env files.

#### 6. No robots.txt or sitemap.xml in any repo

None of the 7 sites have static robots.txt or sitemap files. Next.js can generate these dynamically via the metadata API, but they need to be configured. This is critical for Google indexing.

---

### Framework Consistency Check

| Component | Consistent? | Notes |
|-----------|-------------|-------|
| Next.js version | Yes (14.2.3) | All 7 repos identical |
| React version | Yes (^18) | All 7 repos |
| Tailwind CSS | Yes (^3.4.1) | All 7 repos |
| MDX processing | Yes | next-mdx-remote + gray-matter |
| Framer Motion | Yes | All repos |
| TypeScript | Yes | All repos |
| @vercel/analytics | **No** | Missing from tradepick, aibyrole, remotepivot |
| Google verification | Yes | All 7 have it (glwc uncommitted) |
| Site config structure | Yes | All use lib/site-config.ts with same shape |
| Content structure | Yes | All use content/ directory with MDX files |

---

## Part 2: Existing Skills Library

You currently have **8 custom skills** plus **7 built-in Cowork skills**.

### Custom Skills (in /skills/)

| Skill | Purpose | Strength | Gap |
|-------|---------|----------|-----|
| affiliate-expert | Programme research, link strategy, compliance | UK programme database, ASA compliance | No live data — recommends but can't check commissions |
| seo-expert | Keywords, on-page SEO, technical SEO | Next.js specific, E-E-A-T for YMYL | No live keyword data (would need Ahrefs/Semrush) |
| podcast-creator | Episode planning, distribution, monetisation | Full production workflow | No video podcast support |
| kindle-kdp | KDP publishing, keywords, launch strategy | Complete end-to-end workflow | Non-fiction focus only |
| youtube-video-creator | AI video scripts, tools, YouTube SEO | ElevenLabs/Pictory/HeyGen workflow | Assumes faceless/AI approach |
| self-improvement-layer | Quality gate, multi-expert routing | Auto-review pipeline before publishing | Meta-skill, depends on others |
| email-marketing-expert | Kit/ConvertKit, sequences, GDPR | UK-specific, complete automation setup | Assumes Kit platform only |
| glc-portfolio | Portfolio management, build validation | 7-site architecture docs, troubleshooting | Project-specific context |

### Built-in Cowork Skills

docx, pptx, pdf, xlsx, schedule, skill-creator

---

## Part 3: Recommended New Skills & Tools

### Tier 1 — High Priority (Genuine Value Add)

#### Figma MCP Server
- **What it does:** Reads Figma files, extracts design tokens, generates code from designs, maps components
- **Why you need it:** You've said design is the next phase. This bridges Figma designs directly into your Next.js components without manual translation
- **When:** As soon as your framework is stable and you're ready to design in Figma
- **How:** Connect via Claude's MCP registry or install from GitHub

#### Google Search Console MCP (AminForou/mcp-gsc)
- **What it does:** 20+ tools — search analytics, URL inspection, sitemap management, indexing API
- **Why you need it:** You have 7 sites to monitor in GSC. Asking Claude "how are my sites performing?" and getting real data back is infinitely more useful than checking 7 dashboards manually
- **How:** GitHub install, OAuth to your Google account

#### Google Analytics MCP (surendranb/google-analytics-mcp)
- **What it does:** GA4 data access — traffic, user behaviour, conversions
- **Why you need it:** Same reason as GSC. One question to Claude instead of 7 dashboard checks
- **How:** GitHub install, OAuth to Google

#### Ahrefs MCP (if you have an Ahrefs account)
- **What it does:** 55+ tools — keyword difficulty, content gaps, backlink monitoring, competitor analysis
- **Why you need it:** Your seo-expert skill gives recommendations but has no data. Ahrefs MCP gives it live data to work with. Game-changing combo
- **Cost:** Requires Ahrefs subscription (~$99/month Lite plan)

### Tier 2 — Useful but Not Urgent

#### Cloudinary MCP
- **What:** Image/video upload, transformation, optimisation, CDN delivery
- **Why:** You have 568 articles. Optimised images = faster page loads = better Core Web Vitals = better Google ranking
- **When:** When you start focusing on page speed

#### AirOps MCP (AI Search Optimisation)
- **What:** Optimises content for AI search results (Google SGE, Gemini, ChatGPT)
- **Why:** The search landscape is shifting. Content that ranks in traditional Google AND shows up in AI answers wins twice
- **When:** After your core content is indexed and ranking

#### Marketing Skills Collection (coreyhaines31/marketingskills)
- **What:** CRO (conversion rate optimisation), copywriting, growth engineering skills for Claude Code
- **Why:** Complements your existing affiliate and SEO skills with conversion-focused expertise
- **How:** Clone from GitHub, install relevant skills

### Tier 3 — Watch List (Future Consideration)

| Tool | What | When to Consider |
|------|------|-----------------|
| Stripe MCP | Payment processing | When you sell digital products directly (not just affiliate) |
| MailerLite MCP | Email platform automation | Only if you switch from Kit/ConvertKit |
| Canva MCP | Design creation | Skip if committed to Figma |
| Local Falcon MCP | Local SEO | Only if any site targets geographic keywords |
| Windsor.ai MCP | Multi-source analytics hub | When you have 5+ data sources to unify |

### What NOT to Add

- **Another SEO skill** — your seo-expert + Ahrefs MCP covers it
- **Another email skill** — email-marketing-expert + Kit is solid
- **Generic "AI writing" skills** — your self-improvement-layer already handles quality gating
- **Social media scheduling MCPs** — premature until you have consistent traffic to amplify

---

## Part 4: Community Skill Repos Worth Exploring

| Repository | Stars | Focus | Best Skills for You |
|------------|-------|-------|---------------------|
| travisvn/awesome-claude-skills | 192+ | Curated directory | Marketing & affiliate skills |
| alirezarezvani/claude-skills | 192+ | Full-stack | Content creation, growth engineering |
| coreyhaines31/marketingskills | — | Marketing-specific | CRO, copywriting, analytics |
| Affitor/affiliate-skills | — | Affiliate automation | Research → content → deploy pipeline |
| levnikolaevich/claude-code-skills | — | Dev lifecycle | Codebase audits, performance optimisation |

---

## Part 5: Figma Design Readiness

### Current State
Your framework works. All 7 sites are deployed and serving content. The design is functional but template-based — dark theme, consistent layout, but not bespoke.

### When to Move to Figma
You said "only when the framework is working perfectly." Here's what "perfectly" means in practical terms:

- [ ] All 3 stuck rebases resolved
- [ ] package.json names corrected across all repos
- [ ] @vercel/analytics installed on all 7 sites
- [ ] Google Search Console verified for all 7 sites
- [ ] Sitemaps + robots.txt configured
- [ ] All uncommitted changes pushed
- [ ] Custom domains pointed (at least for the primary sites)

Once those are ticked off, the framework is stable and you can design with confidence that changes will deploy cleanly.

### Figma Workflow with MCP
Once the Figma MCP is connected, the workflow becomes:

1. Design in Figma (layouts, components, colour tokens, typography)
2. Claude reads the Figma file via MCP
3. Claude generates/updates Next.js components to match the design
4. Push to GitHub → Vercel auto-deploys

This eliminates the manual design-to-code translation step entirely.

---

## Recommended Next Actions (Priority Order)

1. **Fix the 3 stuck rebases** (tradepick, aibyrole, remotepivot) — run the `rm -rf .git/rebase-merge` commands above
2. **Commit + push GLWC verification changes** — last piece of Search Console setup
3. **Fix package.json names** across 4 repos
4. **Install @vercel/analytics** on tradepick, aibyrole, remotepivot
5. **Add robots.txt + sitemap generation** to all 7 repos (Next.js metadata API)
6. **Connect Google Search Console MCP** — start getting real indexing data
7. **Connect Figma MCP** — when you're ready to start designing
8. **Explore Ahrefs MCP** — if/when you get an Ahrefs account for keyword data
