# Claude Code Prompt — Copy & Paste Into Claude Code

---

Work through these tasks in order. Don't ask questions, just do them. Commit and push each change individually.

## 1. Clear stuck rebases

```bash
cd tradepick-framework && rm -rf .git/rebase-merge && git reset --hard HEAD && cd ..
cd aibyrole-framework && rm -rf .git/rebase-merge && git reset --hard HEAD && cd ..
cd remotepivot-framework && rm -rf .git/rebase-merge && git reset --hard HEAD && cd ..
```

Verify all 3 are clean with `git status`.

## 2. Commit and push GLWC verification

In glwc-framework: stage `app/layout.tsx` and `public/google57bf41dfef9c8420.html`, commit as "Add Google Search Console verification", push to master.

## 3. Fix package.json names

Change the `"name"` field in package.json:
- liftlab-framework → `"liftlab-framework"`
- tradepick-framework → `"tradepick-framework"`
- aibyrole-framework → `"aibyrole-framework"`
- remotepivot-framework → `"remotepivot-framework"`

Commit each as "Fix package.json name", push. Branches: liftlab uses `main`, others use `master`.

## 4. Install @vercel/analytics on 3 repos

In tradepick-framework, aibyrole-framework, remotepivot-framework:

```bash
npm install @vercel/analytics
```

Then in each repo's `app/layout.tsx`, add `import { Analytics } from '@vercel/analytics/react';` and put `<Analytics />` inside the body JSX (match how glwc-framework does it).

Commit each as "Add @vercel/analytics", push.

## 5. Add .gitignore to glp1-framework

Copy glwc-framework's `.gitignore` into glp1-framework. Commit as "Add missing .gitignore", push to master.

## 6. Add robots.txt to all 7 repos

Create `app/robots.ts` in each repo:

```typescript
import { MetadataRoute } from 'next';

export default function robots(): MetadataRoute.Robots {
  return {
    rules: { userAgent: '*', allow: '/' },
    sitemap: 'https://SITE_URL/sitemap.xml',
  };
}
```

Use the `.vercel.app` URL for each site (read it from `lib/site-config.ts` or use these):
- glwc-framework → glwc-framework.vercel.app
- liftlab-framework → liftlab-framework.vercel.app
- fuel-optimal-framework → fuel-optimal.vercel.app
- tradepick-framework → tradepick-framework.vercel.app
- aibyrole-framework → aibyrole-framework.vercel.app
- remotepivot-framework → remotepivot-framework.vercel.app
- glp1-framework → glp1-framework.vercel.app

Commit each as "Add robots.txt", push.

## 7. Add sitemap.xml to all 7 repos

Create `app/sitemap.ts` in each repo. Read how articles are loaded (check the content directory structure and routing in `app/articles/[slug]/page.tsx`), then generate a sitemap entry for every article plus the homepage. Use Next.js MetadataRoute.Sitemap.

Commit each as "Add dynamic sitemap", push.

## 8. Build-test before pushing

Run `npm run build` in each repo before pushing. Fix any build errors.

## When done

List: which repos changed, commit hashes, any errors.
