# Domain Pointing Guide — All 7 Sites to Vercel

## Domains to Point

| Site | Domain | Vercel Project |
|------|--------|---------------|
| MaleOptimal | maleoptimal.co.uk | glwc-framework |
| LiftLab | liftlab.co.uk | liftlab-framework |
| Fuel Optimal | fueloptimal.co.uk | fuel-optimal-framework |
| TradePick | tradepick.co.uk | tradepick-framework |
| AI By Role | aibyrole.co.uk | aibyrole-framework |
| RemotePivot | remotepivot.co.uk | remotepivot-framework |
| GLP-1 Guide | glp1guide.co.uk | glp1-framework |

## Step 1: Add Domains in Vercel (~2 minutes per site)

For each site:

1. Go to [vercel.com/dashboard](https://vercel.com/dashboard)
2. Click the project (e.g. glwc-framework)
3. Go to **Settings** → **Domains**
4. Type your domain (e.g. `maleoptimal.co.uk`) and click **Add**
5. Vercel will show you the DNS records you need — keep this page open
6. Also add `www.maleoptimal.co.uk` — Vercel will auto-redirect www to the root domain

Vercel will give you one of two options:
- **Option A (recommended):** Point nameservers to Vercel — simplest but means Vercel manages all DNS
- **Option B:** Add individual DNS records at your registrar — more control, keeps existing DNS

## Step 2: Update DNS at Your Domain Registrar

### If your domains are at the same registrar (e.g. Namecheap, GoDaddy, 123-reg, Ionos):

**For root domain (maleoptimal.co.uk):**
- Type: **A**
- Host: **@**
- Value: **76.76.21.21** (Vercel's IP)

**For www subdomain:**
- Type: **CNAME**
- Host: **www**
- Value: **cname.vercel-dns.com**

Repeat for all 7 domains.

### Registrar-Specific Instructions

**Namecheap:**
1. Log in → Domain List → click Manage next to domain
2. Go to Advanced DNS tab
3. Delete any existing A records for @ and CNAME for www
4. Add new A record: Host = @, Value = 76.76.21.21
5. Add new CNAME: Host = www, Value = cname.vercel-dns.com

**GoDaddy:**
1. My Products → DNS → Manage next to domain
2. Edit existing A record or add new: Name = @, Value = 76.76.21.21
3. Edit/add CNAME: Name = www, Value = cname.vercel-dns.com

**123-reg / Ionos / other UK registrars:**
1. Find DNS Management or Zone Editor in your control panel
2. Same records: A record @ → 76.76.21.21, CNAME www → cname.vercel-dns.com

## Step 3: Verify in Vercel

After updating DNS:
1. Go back to Vercel → Settings → Domains for each project
2. Vercel will show a status indicator — it checks automatically
3. SSL certificates are provisioned automatically (free via Let's Encrypt)
4. DNS propagation takes 10 minutes to 48 hours (usually under 1 hour for .co.uk)

## Step 4: Update Other Services

Once domains are live, update these:

1. **Google Search Console** — add each custom domain as a new property (URL prefix method, same as before)
2. **GA4** — update the website URL in each data stream (Admin → Data Streams)
3. **Kit.com email forms** — update any form action URLs if they reference Vercel domains
4. **Affiliate programmes** — update your website URL in each affiliate dashboard
5. **Sitemap URLs** — these should auto-update if you're using relative paths in next.config

## Step 5: Redirect Vercel Subdomains

After custom domains are working:
1. In Vercel → Settings → Domains
2. The *.vercel.app domain should auto-redirect to your custom domain
3. Verify by visiting glwc-framework.vercel.app — it should redirect to maleoptimal.co.uk

## Troubleshooting

**Domain shows "Invalid Configuration":**
- DNS hasn't propagated yet — wait 1 hour and check again
- Check you didn't add a trailing dot after the domain name
- Make sure there are no conflicting A records

**SSL certificate not provisioning:**
- Usually resolves within 10 minutes of DNS propagation
- If stuck after 1 hour, remove the domain in Vercel and re-add it

**www not redirecting:**
- Make sure both root and www are added in Vercel
- Check the CNAME record is pointing to cname.vercel-dns.com (not the old host)

## Where Are Your Domains Registered?

If you're not sure which registrar you used, check your email for domain purchase confirmations, or use [who.is](https://who.is) to look up each domain and see the registrar name.
