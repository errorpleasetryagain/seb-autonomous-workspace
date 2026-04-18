#!/bin/bash
# ============================================
# PUSH ALL 7 REPOS TO GITHUB
# Run from: ~/Library/Mobile Documents/com~apple~CloudDocs/Documents/Claude/Projects/Passive websites
# Updated: 31 March 2026
# ============================================
# All repos have COMMITTED changes ready to push:
#   - Google Search Console verification (meta tag + HTML file) — all 7 repos
#   - Affiliate link fixes (real Amazon UK maleoptimal-21 links) — 6 repos
#   - Content fixes across all guides
# ============================================
# AFTER PUSHING: Go to Google Search Console and add each .vercel.app URL
# as a URL prefix property. The verification files will be live after deploy.
# ============================================

BASE=$(cd "$(dirname "$0")" && pwd)
echo "Working from: $BASE"
echo ""

SUCCESS=0
FAIL=0

for repo in glwc-framework liftlab-framework fuel-optimal-framework glp1-framework tradepick-framework aibyrole-framework remotepivot-framework; do
  DIR="$BASE/$repo"
  if [ -d "$DIR/.git" ]; then
    echo "=== $repo ==="
    cd "$DIR"

    # Check for uncommitted changes and commit them
    if [ -n "$(git status --porcelain)" ]; then
      echo "  Staging uncommitted changes..."
      git add -A 2>/dev/null || true
      if ! git diff --cached --quiet 2>/dev/null; then
        git commit -m "Add Google verification + affiliate link fixes" 2>&1 | tail -2
      fi
    fi

    # Push
    BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")
    echo "  Pushing $BRANCH..."
    if git push -u origin "$BRANCH" 2>&1 | tail -3; then
      echo "  ✓ Pushed successfully"
      SUCCESS=$((SUCCESS + 1))
    else
      echo "  ✗ Push failed — check manually"
      FAIL=$((FAIL + 1))
    fi

    cd "$BASE"
    echo ""
  else
    echo "=== $repo — no .git directory, skipping ==="
    echo ""
  fi
done

echo "============================================"
echo "Results: $SUCCESS pushed, $FAIL failed"
echo ""
echo "NEXT STEPS:"
echo "1. Check Vercel deployments: https://vercel.com/errorpleasetryagains-projects"
echo "2. Add URL prefix properties in Google Search Console:"
echo "   - https://glwc-framework.vercel.app"
echo "   - https://liftlab-framework.vercel.app"
echo "   - https://fuel-optimal.vercel.app"
echo "   - https://glp1-framework.vercel.app"
echo "   - https://tradepick-framework.vercel.app"
echo "   - https://aibyrole-framework.vercel.app"
echo "   - https://remotepivot-framework.vercel.app"
echo "3. Submit sitemaps: each site at /sitemap.xml"
echo "============================================"
