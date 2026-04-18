# What To Do Next (Priority Order)

Your sites are live. 568+ articles published. Affiliates coming online. Now it's about getting everything tight before chasing sponsors.

## This Week: Get Sites to 100%

### Day 1: Male Optimal (flagship site)

1. **Open maleoptimal.co.uk in your browser**
   - Click through every page. Does it load? Does it look professional?
   - Check the homepage, About page, Privacy/Disclaimer pages
   - Click 5-10 articles at random. Do they render properly?

2. **Check affiliate links**
   - Open AFFILIATE-LINK-GUIDE.md (in your workspace folder)
   - Search articles for placeholder links (YOURCODE, example.com, #affiliate)
   - Swap any you find with real Amazon UK links (tag: maleoptimal-21)
   - Add `affiliateDisclosure: true` to frontmatter if missing

3. **Log into Medichecks**
   - Find your referral code/link on their affiliate dashboard
   - Replace any Medichecks placeholder links in Male Optimal articles

### Day 2: TradePick + AI By Role

4. **Repeat the site check for tradepick.co.uk and aibyrole.co.uk**
   - Same process: click through, check pages load, spot anything broken

5. **Add Toggl + Clockify links**
   - Toggl: `https://get.toggl.com/g1ivv4qgtynz`
   - Clockify: `https://clockify.me/pricing?fpr=pttinj`
   - These go in any articles about time tracking, productivity tools, or software reviews

6. **Add Make.com links to AI By Role**
   - Link: `https://www.make.com/en/register?pc=goodlivingco`
   - Goes in any article about automation, no-code tools, workflow tools

### Day 3: Remote Pivot + Remaining Sites

7. **Check remotepivot.co.uk, liftlab.co.uk, fueloptimal.co.uk, glp1guide.co.uk**
   - Same process: click through, check pages, spot issues

8. **Add affiliate links where relevant**
   - Remote Pivot: Make.com, Toggl, Clockify, Skillshare (get link from Impact.com dashboard)
   - Lift Lab + Fuel Optimal: Amazon UK product links
   - GLP-1 Guide: Amazon UK, Medichecks

## Ongoing: Things Only You Can Do

These need your manual login. Do them between site checks:

- [ ] **Find KDP suspension email** -- check your iCloud inbox (adam.turton84@icloud.com), not Gmail
- [ ] **Submit ClickUp on PartnerStack** -- needs you to complete CAPTCHA
- [ ] **Submit Writesonic on PartnerStack** -- needs password + terms + signup
- [ ] **Fix AI By Role on Impact.com** -- change registered URL from .com to .co.uk, then re-verify
- [ ] **Reapply to Impact.com marketplace** -- was declined, can reapply
- [ ] **Apply to FreshBooks via Awin** -- log into Awin directory (publisher ID 2838304), search FreshBooks, apply
- [ ] **Set up payment on Clockify/CAKE.com dashboard** -- so you can get paid
- [ ] **Email TRT clinics** -- Optimale, Balance My Hormones, Leger. Ask about referral/affiliate programmes. Short email: "I run maleoptimal.co.uk, a UK men's health site with 156 articles. Do you have a referral programme?"

## When Cowork Is Available Again

These are tasks we do together:

- **Design work** (DRIP workflow) -- pick a site, start with Male Optimal
- **Load email sequences into MailerLite** -- 42 sequences ready, need connecting
- **Link audit** -- automated scan of all 7 sites for broken/placeholder links
- **Content quality check** -- spot-check articles for tone, accuracy, formatting
- **SEO review** -- check GSC data, find quick wins

## How To Use Claude Code (VS Code) Without Me

For simple tasks like finding and replacing links:

1. Open VS Code terminal
2. Type `claude` to start Claude Code
3. Tell it what you want, e.g.:
   - "Find all .mdx files in content/ that contain placeholder affiliate links"
   - "Replace all bare Amazon UK links with tagged versions using maleoptimal-21"
   - "Check which articles have affiliateDisclosure set to false but contain affiliate links"
4. Claude Code will search, show you results, and make changes if you approve
5. Then `git add .` + `git commit -m "message"` + `git push` to deploy

Keep prompts short and specific. Claude Code uses API tokens, not your Max allowance.
