# Google Analytics 4 (GA4) Setup Guide

## Step 1: Create GA4 Properties (Adam — manual, ~15 minutes)

Go to [analytics.google.com](https://analytics.google.com) and sign in with your Google account.

For each site, repeat:

1. Click the gear icon (Admin) → "Create" → "Property"
2. Property name: use the site name (e.g. "MaleOptimal", "LiftLab")
3. Reporting time zone: United Kingdom
4. Currency: British Pound (GBP)
5. Click Next → select "Small business" → click Create
6. Choose "Web" as your platform
7. Enter the Vercel URL for now (e.g. `https://glwc-framework.vercel.app`) — update to custom domain later
8. Stream name: same as property name
9. Click "Create stream"
10. **Copy the Measurement ID** (starts with `G-`) — you'll need this

Do this 7 times. You'll end up with 7 Measurement IDs.

| Site | Property Name | Domain (for now) | Measurement ID |
|------|--------------|------------------|----------------|
| MaleOptimal | MaleOptimal | glwc-framework.vercel.app | G-40CVVMC814 |
| LiftLab | LiftLab | liftlab-framework.vercel.app | G-JJX8VP1MKP |
| Fuel Optimal | FuelOptimal | fuel-optimal.vercel.app | G-YZW8P11D5B |
| TradePick | TradePick | tradepick-framework.vercel.app | G-Z7FQ9TM28B |
| AI By Role | AIByRole | aibyrole-framework.vercel.app | G-FPJ3D7TJEF |
| RemotePivot | RemotePivot | remotepivot-framework.vercel.app | G-LRY567VCK2 |
| GLP-1 Guide | GLP1Guide | glp1-framework.vercel.app | G-JQYQ8Z0WLL |

## Step 2: Add Tracking Code to All Sites (Claude Code prompt)

Once you have all 7 Measurement IDs, paste this prompt into Claude Code — just fill in the G- codes:

---

```
Add GA4 tracking to all 7 sites. For each repo, add a GoogleAnalytics component to app/layout.tsx using next/script.

Measurement IDs:
- glwc-framework: G-40CVVMC814
- liftlab-framework: G-JJX8VP1MKP
- fuel-optimal-framework: G-YZW8P11D5B
- tradepick-framework: G-Z7FQ9TM28B
- aibyrole-framework: G-FPJ3D7TJEF
- remotepivot-framework: G-LRY567VCK2
- glp1-framework: G-JQYQ8Z0WLL

In each repo's app/layout.tsx, add these two Script tags inside <head> or at the top of <body>:

<Script src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX" strategy="afterInteractive" />
<Script id="google-analytics" strategy="afterInteractive">
  {`window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('consent', 'default', {
    'analytics_storage': 'denied'
  });
  gtag('config', 'G-XXXXXXXXXX');`}
</Script>

Import Script from 'next/script'. Keep existing @vercel/analytics. Commit each repo separately. Push all.
```

---

## Step 3: Update Custom Domains Later

When you point custom domains to Vercel, go back to each GA4 property:
1. Admin → Data Streams → click your stream
2. Update the website URL to the custom domain
3. The Measurement ID stays the same

## Notes
- The consent mode snippet (`analytics_storage: 'denied'`) ensures GDPR compliance by default — analytics only fire after cookie consent
- You'll want a cookie consent banner eventually (CookieYes or similar) that calls `gtag('consent', 'update', {'analytics_storage': 'granted'})` when accepted
- GA4 takes 24–48 hours to start showing data after installation
