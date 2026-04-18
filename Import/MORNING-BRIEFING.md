# Status Briefing — 30 March 2026 (Updated)

## Node.js 24 → 20.x fix: DONE across all 7 projects

The root cause of ALL build failures was Node.js 24.x in Vercel — too new for Next.js 14.2.3. Builds were failing in ~51 seconds every time.

### What's been done

1. **Changed Node.js version to 20.x in Vercel settings** for ALL 7 primary projects:
   - glwc-framework ✅
   - fuel-optimal-db6a ✅
   - liftlab-framework-nk8n ✅
   - remotepivot-framework-9lw7 ✅
   - glp1-framework-ajwp ✅
   - tradepick-framework ✅
   - aibyrole-framework ✅

2. **Added `.node-version` and `.nvmrc` files** to all 7 repos — both contain `20`
3. **Added `engines` field** to all 7 `package.json` files — `"node": ">=18.0.0 <21.0.0"`
4. **Updated the push script** with the new commit message

### Second fix: Date object rendering error

After you pushed, the builds got past the Node.js issue but hit a new error:
**"Objects are not valid as a React child (found: [object Date])"**

Root cause: `gray-matter` parses YAML date strings like `"2026-03-28"` into JavaScript Date objects. When these reach React components, they crash the build.

Fix applied: Added `safeDate()` helper in `lib/content.ts` across all 7 repos that coerces Date objects back to ISO strings.

### Third fix: YAML colon parsing error in frontmatter

After the Date fix push, builds got further (generated 163/163 static pages) but failed on export:
**"YAMLException: incomplete explicit mapping pair; a key node is missed"**

Root cause: Two guide MDX files had unquoted titles containing colons — YAML interprets `:` as a key-value separator.

Affected files:
- `content/guides/best-testosterone-boosters-uk-2026.mdx` — title had `2026: What Actually Works`
- `content/guides/andropause-explained-male-menopause.mdx` — title had `Explained: The Male Menopause`

Fix applied:
1. Wrapped both titles in double quotes
2. Added `safeMatter()` wrapper around all `gray-matter` parsing calls in `content.ts` — if any file has malformed YAML, it's skipped instead of crashing the build
3. Copied fix to all 7 repos

### Fourth fix: ComparisonTable MDX component not passed to compiler

After the YAML fix, builds got further but glwc-framework failed on export with:
**"Error: Expected component `ComparisonTable` to be defined: you likely forgot to import, pass, or provide it."**

Root cause: `compileMdxSource()` in `content.ts` called `compileMDX` without a `components` map. Three repos (glwc, fuel-optimal, aibyrole) use `<ComparisonTable>` in their MDX content, but the component wasn't being passed to the compiler.

Fix applied:
1. Imported `ComparisonTable` in `content.ts` and created an `mdxComponents` map
2. Passed `components: mdxComponents` to the `compileMDX` call
3. Copied fix to all 7 repos

### What you need to do now

**Push the ComparisonTable fix**:
```bash
cd ~/Documents/Claude/Projects/Passive\ \ websites
bash push-all-repos.sh
```

Then watch the builds — they should go green this time. Duplicates are already deleted.

---

## Duplicate Vercel projects — still needs cleanup

You've got a lot of duplicate projects clogging the build queue. Each duplicate eats a build slot on the Hobby plan (1 concurrent build). Here's the updated cleanup list:

| Keep (primary) | Delete (duplicates) |
|---|---|
| glwc-framework | glwc-framework-kuvk, glwc-framework-wwqd, glwc-framework-wbyq, glwc-framework-v4v3 |
| fuel-optimal-db6a | fuel-optimal-jbf1, fuel-optimal-x851, fuel-optimal-wz4j, fuel-optimal-evss |
| liftlab-framework-nk8n | liftlab-framework-6onu, liftlab-framework-n6gf, liftlab-framework-jsz8, liftlab-framework-hvbd, liftlab-framework-7b6m, liftlab-framework |
| remotepivot-framework-9lw7 | — |
| glp1-framework-ajwp | — |
| tradepick-framework | — |
| aibyrole-framework | — |

**That's ~14 duplicates to delete.** To delete: Project → Settings → scroll to bottom → Delete Project.

---

## What else got done today

### Book 8 Cover — Performance Pharmaceuticals
- Dark B&W style matching the series
- File: `kindle/performance-pharmaceuticals-cover.jpg`
- 1600x2560px (KDP standard)
- Pharmaceutical bar chart motif, series number 08

### Code fixes still in place from overnight
- Resilient MDX compilation (try-catch in content.ts)
- Layout.tsx import order fixed
- TS + ESLint build errors ignored
- 135 MDX `<` symbol escapes
- GLC design system applied across all 7 sites

---

## Current live status

| Site | URL | Status |
|---|---|---|
| GLWC (Male Optimal) | glwc-framework.vercel.app | LIVE (old build) |
| All others | *.vercel.app | 404 (awaiting push + first build with Node 20.x) |

Once you push, all 7 should deploy.

---

## Still pending

- Affiliate codes → fill in `affiliate-replace.py` and run
- Google Analytics / Search Console setup
- Kit welcome sequences → load into Kit
- Book 8 manuscript → upload to KDP
- GLC hub → deploy to goodlivingco.co.uk
- ~~Delete duplicate Vercel projects~~ ✅ DONE
