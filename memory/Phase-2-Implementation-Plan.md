---
title: "Phase 2 Implementation Plan: Featured Images + References"
description: "Systematic rollout across all 7 sites"
category: "Project Management"
author: "Seb"
publishedDate: "2026-04-05"
---

# Phase 2 Implementation Plan
## Featured Images + References/Citations

---

## Part A: Featured Image Infrastructure (Code Task)

### Step 1: Create Shared Components (1 hour)
Create in each site's `/components` directory:

**FeaturedImage.tsx** — ✓ Already created for Fuel Optimal
- Copy to all 7 sites
- Adjust import paths if needed
- Test on one site first

**ArticleHeader.tsx**
- Combines title, description, featured image
- Consistent styling across sites

### Step 2: Update Content Parsing (30 min per site)
Modify `/lib/content.ts` or equivalent:
- Add `featuredImage` to Article interface
- Parse frontmatter featuredImage field
- Return null if not present (backwards compatible)

### Step 3: Update Article Templates (30 min per site)
Modify `app/blog/[slug]/page.tsx`:
- Import FeaturedImage or ArticleHeader
- Pass featuredImage from article data
- Add priority={true} for above-fold

### Step 4: Update next.config.js (15 min per site)
Add image configuration:
```javascript
images: {
  formats: ['image/webp', 'image/jpeg'],
  deviceSizes: [640, 750, 828, 1080, 1200],
}
```

---

## Part B: Content Migration (Content Task)

### Image Sourcing Strategy

**Option 1: Unsplash Download (Immediate)**
- Use existing download list
- 2-3 images per site already downloaded
- Scale to 10 more per site this week

**Option 2: Batch Unsplash API (Automated)**
- Sign up for Unsplash API (free 50 requests/hour)
- Script to download relevant images per article
- Add attribution automatically

**Option 3: AI Generation (Controlled)**
- Midjourney for unique concepts
- Remove AI look with techniques from Photo Resource Strategy
- Best for topics not covered by stock

### Priority Order for Image Addition

**Tier 1: Homepage Heroes (This Week)**
- 1 image per site already downloaded
- Integrate into homepage components
- Add to layout files

**Tier 2: Top 10 Articles per Site (Next Week)**
- Highest traffic articles first
- Recipe pages for Fuel Optimal
- Tool guides for AI By Role
- Clinic guides for GLP1Guide

**Tier 3: Remaining Articles (Weeks 3-4)**
- Batch process 5-10 per day
- Use Unsplash API for speed
- Focus on categories first, then individual articles

---

## Part C: References/Sources Infrastructure (Content Task)

### Step 1: Create References Component (1 hour)
**ReferencesSection.tsx:**
```typescript
interface Reference {
  id: string;
  title: string;
  url: string;
  source: string; // PubMed, NICE, etc.
  date?: string;
}

export function ReferencesSection({ references }: { references: Reference[] }) {
  return (
    <section className="references mt-12 pt-8 border-t">
      <h2>Sources & References</h2>
      <ol className="list-decimal pl-5 space-y-2">
        {references.map((ref) => (
          <li key={ref.id}>
            <a href={ref.url} target="_blank" rel="noopener">
              {ref.title}
            </a>
            {ref.source && <span className="text-gray-500"> — {ref.source}</span>}
          </li>
        ))}
      </ol>
    </section>
  );
}
```

### Step 2: Frontmatter Schema
Add to article frontmatter:
```yaml
references:
  - id: "1"
    title: "Testosterone Replacement Therapy: UK Guidelines"
    url: "https://www.british-society.org/guidelines"
    source: "British Society for Sexual Medicine"
    date: "2024"
  - id: "2"
    title: "Effects of TRT on Body Composition"
    url: "https://pubmed.ncbi.nlm.nih.gov/XXXX"
    source: "PubMed"
    date: "2023"
```

### Step 3: Retrofit Existing Articles (Ongoing)
**Strategy:** 5 articles per day per site

**Health Sites (MaleOptimal, GLP1Guide):**
- Add PubMed citations for medical claims
- Link to NHS/NICE guidelines
- Cite clinical studies

**Tech Sites (AI By Role, TradePick, RemotePivot):**
- Link to official documentation
- Cite industry reports
- Reference competitor comparisons

**Recipe Site (FuelOptimal):**
- Less critical (recipes don't need citations)
- Optional: Link to nutritional data sources
- Food safety references where relevant

---

## Implementation Schedule

### Week 1: Infrastructure Setup
| Day | Task | Sites |
|-----|------|-------|
| Mon | FeaturedImage component | Fuel Optimal (test) |
| Tue | ArticleHeader component | Fuel Optimal |
| Wed | Content parsing update | Fuel Optimal, Male Optimal |
| Thu | Article template update | Fuel Optimal, Male Optimal |
| Fri | next.config.js image setup | Fuel Optimal, Male Optimal |
| Weekend | Test & refine | 2 sites |

### Week 2: Rollout to All Sites
| Day | Task | Sites |
|-----|------|-------|
| Mon | Copy components | GLP1Guide, AI By Role |
| Tue | Copy components | LiftLab, TradePick, RemotePivot |
| Wed | Content parsing all sites | All 7 |
| Thu | Article template all sites | All 7 |
| Fri | Test all sites | All 7 |

### Week 3: References Component
| Day | Task |
|-----|------|
| Mon | ReferencesSection component |
| Tue | Frontmatter schema update |
| Wed | Add to article templates |
| Thu | Test with sample references |
| Fri | Documentation |

### Week 4: Content Migration - Images
| Day | Task | Target |
|-----|------|--------|
| Mon | Homepage heroes | 7 images |
| Tue | Top 10 articles - batch 1 | 20 images |
| Wed | Top 10 articles - batch 2 | 20 images |
| Thu | Category pages | 14 images |
| Fri | Tool/app pages | 10 images |

### Week 5-6: Content Migration - References
| Day | Task | Target |
|-----|------|--------|
| Mon-Fri | MaleOptimal references | 25 articles |
| Mon-Fri | GLP1Guide references | 25 articles |
| Mon-Fri | Remaining sites | As needed |

---

## Quality Checklist

### Featured Images
- [ ] All homepages have hero images
- [ ] Top 50 articles have featured images
- [ ] Images are < 500KB each
- [ ] Alt text is descriptive (SEO)
- [ ] Attribution present where required
- [ ] Responsive sizing works
- [ ] No layout shift (CLS)

### References
- [ ] Medical claims have PubMed citations
- [ ] NHS/NICE guidelines linked where relevant
- [ ] Technical claims have documentation links
- [ ] All references have working URLs
- [ ] Format is consistent across sites

---

## Expected Outcomes

**Week 2 End:**
- All 7 sites have image infrastructure
- 2 sites (Fuel Optimal, Male Optimal) have full image integration

**Week 4 End:**
- 70+ images downloaded and integrated
- All homepages have hero images
- Top 50 articles have featured images

**Week 6 End:**
- References component live on all health sites
- 50+ articles retrofitted with citations
- E-E-A-T signals significantly improved

---

## Resource Requirements

### Time
- Developer: 20 hours (infrastructure)
- Content: 40 hours (sourcing + retrofitting)
- Total: 60 hours over 6 weeks

### Tools
- Unsplash API key (free)
- Image optimization (Sharp/Squoosh)
- Optional: Midjourney ($10/month)

### Budget
- Stock photos: £0 (Unsplash)
- AI generation: £10/month (optional)
- CDN: £0 (Vercel/Next.js built-in)

---

## Blockers/Risks

1. **Image quality from Unsplash** — Some niches lack variety
   - *Mitigation:* Use AI generation for gaps

2. **Time to retrofit references** — Tedious work
   - *Mitigation:* Prioritize health sites only

3. **Vercel image limits** — Free tier has bandwidth limits
   - *Mitigation:* Optimize aggressively, upgrade if needed

4. **Broken Unsplash links** — If images removed
   - *Mitigation:* Download and host locally

---

## Success Metrics

**Technical:**
- 100% of new articles have featuredImage frontmatter
- 0 console errors for images
- < 0.1s image load time

**Content:**
- 70+ images live
- 50+ articles with references
- 0 broken image links

**SEO:**
- Image search traffic increase
- Featured snippet improvements
- E-E-A-T score improvement in audit

---

*Plan created: April 2026*
*Ready for execution*
