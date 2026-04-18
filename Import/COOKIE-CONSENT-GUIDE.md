# Cookie Consent Banner — Implementation Guide

## What This Does
A GDPR-compliant cookie consent banner for all 7 sites. Works with GA4 consent mode v2 — analytics are blocked by default until the user clicks Accept. Stores consent in a cookie (not localStorage). Styled with Tailwind to match the dark, professional look of the sites.

---

## Claude Code Prompt

Paste this into Claude Code to add the cookie consent banner to all 7 repos:

```
For each of these 7 repos in ~/Library/Mobile Documents/com~apple~CloudDocs/Documents/Claude/Projects/Passive websites/:
- glwc-framework
- liftlab-framework
- fuel-optimal-framework
- tradepick-framework
- aibyrole-framework
- remotepivot-framework
- glp1-framework

Do the following:

1. Create src/components/CookieConsent.tsx with this exact content:

'use client';

import { useState, useEffect } from 'react';

function getCookie(name: string): string | null {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? match[2] : null;
}

function setCookie(name: string, value: string, days: number) {
  const expires = new Date(Date.now() + days * 864e5).toUTCString();
  document.cookie = `${name}=${value}; expires=${expires}; path=/; SameSite=Lax; Secure`;
}

export default function CookieConsent() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const consent = getCookie('cookie_consent');
    if (!consent) {
      setVisible(true);
    } else if (consent === 'accepted') {
      updateConsent(true);
    }
  }, []);

  function updateConsent(granted: boolean) {
    if (typeof window !== 'undefined' && typeof window.gtag === 'function') {
      window.gtag('consent', 'update', {
        analytics_storage: granted ? 'granted' : 'denied',
      });
    }
  }

  function handleAccept() {
    setCookie('cookie_consent', 'accepted', 365);
    updateConsent(true);
    setVisible(false);
  }

  function handleReject() {
    setCookie('cookie_consent', 'rejected', 365);
    updateConsent(false);
    setVisible(false);
  }

  if (!visible) return null;

  return (
    <div className="fixed bottom-0 left-0 right-0 z-50 p-4 bg-gray-900 border-t border-gray-700 shadow-lg">
      <div className="max-w-5xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <p className="text-sm text-gray-300">
          We use cookies to analyse site traffic and improve your experience. No data is collected until you accept.
        </p>
        <div className="flex gap-3 shrink-0">
          <button
            onClick={handleReject}
            className="px-4 py-2 text-sm text-gray-400 hover:text-white border border-gray-600 rounded-md transition-colors"
          >
            Reject
          </button>
          <button
            onClick={handleAccept}
            className="px-4 py-2 text-sm text-white bg-blue-600 hover:bg-blue-700 rounded-md transition-colors"
          >
            Accept
          </button>
        </div>
      </div>
    </div>
  );
}

2. Add this type declaration to src/types/gtag.d.ts (create the file if it doesn't exist):

interface Window {
  gtag: (...args: any[]) => void;
}

3. In the root layout file (src/app/layout.tsx or pages/_app.tsx), import and add <CookieConsent /> just before the closing </body> tag:

import CookieConsent from '@/components/CookieConsent';

Add <CookieConsent /> before </body>.

4. Git add, commit with message "Add GDPR cookie consent banner with GA4 consent mode", and push.

Do all 7 repos.
```

---

## How It Works

- On first visit, the banner appears at the bottom of the page
- GA4 consent mode defaults to `analytics_storage: 'denied'` (set in the GA4 script snippet from GA4-SETUP-GUIDE.md)
- When the user clicks **Accept**, it updates consent to `'granted'` and sets a cookie for 365 days
- When the user clicks **Reject**, it keeps analytics denied and sets the cookie so the banner doesn't reappear
- On return visits, the component reads the cookie and silently updates consent without showing the banner
- UK English copy, no-nonsense, one line of text

## Dependencies

- Requires the GA4 tracking snippet to already be installed (see GA4-SETUP-GUIDE.md)
- The GA4 snippet must include the default consent config:

```js
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {
  analytics_storage: 'denied'
});
```

## Notes

- This is a basic but fully compliant implementation
- For a more advanced setup with granular preferences (marketing, functional cookies), we can upgrade later
- The banner is intentionally minimal — one line of text, two buttons, dark styling
- No third-party cookie consent libraries needed
