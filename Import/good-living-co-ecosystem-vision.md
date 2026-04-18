# Good Living Co — Ecosystem Vision

#good-living-co #good-living-co/hub

March 2026 — Future revenue channels beyond the core sites

---

## The Model

Every piece of content we create should be able to live in multiple formats across multiple platforms. One research brief becomes:

- A long-form article on the website (SEO, affiliate income)
- A 5–10 minute YouTube video (ad revenue, affiliate links in description)
- A short-form clip for TikTok / Instagram Reels (audience growth, brand awareness)
- A Twitter/X thread (engagement, traffic back to site)
- A podcast episode (ad revenue, sponsorships)
- A chapter or section of an ebook (direct sales, KDP royalties)

The website is the hub. Everything else drives traffic back to it.

This is the Huberman model applied across all six verticals. The principle is identical: honest, accurate, expert-level content distributed across every platform where the audience already is.

**Stage 1 (now): Build the websites and content pipeline first.**
Everything in this document is Stage 2 and beyond. We document it now so nothing gets forgotten, and so the content pipeline we're building can be designed to feed these channels from the start.

---

## YouTube

**The model:**
Every article published on any Good Living Co site has the potential to become a YouTube video. The research is already done. The structure is already done. The video is essentially a retelling of the article in a more visual format.

**Format:**
- 5–10 minutes per video
- Animation + stock footage (no on-camera presenter needed at Stage 1)
- Tools to research: Pictory, Synthesia, HeyGen, InVideo — AI video generation from a script
- Script generated automatically from the article draft as part of the content pipeline

**Monetisation:**
- YouTube Partner Programme (requires 1,000 subscribers + 4,000 watch hours)
- Affiliate links in video descriptions (same programmes as the site)
- Sponsorships once channels have reach

**Channels to build (one per site):**
| Channel | Site | Content angle |
|---|---|---|
| maleprotocol | Site 1 | Testosterone, TRT, bloodwork, supplements, biohacking |
| tradestack | Site 2 | Software reviews for tradesperson businesses |
| roleai | Site 3 | AI tool walkthroughs for specific job roles |
| remotepivot | Site 4 | How to pivot from traditional jobs into remote work |

**Pipeline integration:**
When an article is approved and ready to publish, the content pipeline should also generate:
- A YouTube script (same content, conversational format)
- A video brief (visuals to source, b-roll suggestions, on-screen text)

This gets added to the `generate-draft.js` script as an optional output flag: `--youtube`

---

## Podcast

**The model:**
AI-generated podcast using a realistic voice model (ElevenLabs or similar). Not pretending to be human — positioned as an AI-hosted show, which is actually a differentiator right now.

Alternatively: interview format where real guests (doctors, coaches, practitioners) are interviewed remotely and the host is Adam or a presenter. This is Stage 3 territory.

**Format for Stage 2:**
- 10–20 minute episodes
- Script generated from article content
- Realistic AI voice via ElevenLabs
- Distributed via Spotify, Apple Podcasts, Amazon Music

**Monetisation:**
- Podcast sponsorships (once listenership established)
- Affiliate mentions within episodes
- Premium episodes / subscriber content

**Channels:**
- The Male Protocol Podcast (Site 1)
- The TradeStack Podcast (Site 2) — software reviews for small businesses
- Others to follow

---

## Social Media

One account per site, across three platforms. Content repurposed from articles automatically.

**Platforms:**
| Platform | Content type | Best for |
|---|---|---|
| Instagram | Carousels, Reels, infographics | Visual content, supplements, bloodwork data |
| TikTok | Short video clips (60–90 sec) | Younger audience, viral reach |
| Twitter/X | Threads, data points, quick takes | Tech/AI niche (Sites 2 + 3) |

**Accounts to build:**
| Account | Site | Priority |
|---|---|---|
| @maleprotocol | Site 1 | Stage 2 — high priority |
| @tradestack | Site 2 | Stage 2 |
| @roleai | Site 3 | Stage 2 |
| @remotepivot | Site 4 | Stage 3 |
| @goodlivingco | Holding brand | Stage 3 |

**Monetisation:**
- Instagram: Partner programme + affiliate links in bio/stories
- TikTok: TikTok Creator Fund + affiliate links
- Twitter/X: X Premium revenue sharing (requires 500+ followers + engagement threshold)
- Brand partnerships and sponsored posts once reach is established

**Pipeline integration:**
Each approved article should also generate:
- 1 x Twitter/X thread (key points as numbered tweets)
- 1 x Instagram carousel script (5–7 slides, key facts and visuals)
- 1 x short video script (60–90 seconds for TikTok/Reels)

Added to `generate-draft.js` as output flags: `--twitter`, `--instagram`, `--tiktok`

---

## Ebooks & Publications

**The model:**
Once a site has 20–30 articles on a topic, those articles can be compiled, expanded, and published as a Kindle ebook via Amazon KDP. The research is already done. The writing is already done. The ebook is essentially an edited and expanded compilation.

**Examples:**
- *The Male Protocol: A Practical Guide to Testosterone Optimisation for Men Over 40* — from Site 1 content
- *The AI Toolkit: Best AI Tools for Every Job Role* — from Site 3 content
- *The Remote Pivot: How to Move from a Traditional Job to Remote Work* — from Site 4 content

**Revenue:**
- 35% royalty on books priced under £2.99
- 70% royalty on books priced £2.99–£9.99 (the target range)
- A £7.99 ebook at 70% = £5.59 per sale
- 100 sales/month = £559/month passive from a book that cost nothing to write beyond the site content already created

**KDP Select:**
Enrolling in KDP Select gives access to Kindle Unlimited (subscription readers) and promotional tools. Worth considering for the first book on each topic.

**Pipeline integration:**
A separate script (`compile-ebook.js`) could pull all published articles on a given tag, compile them into a structured document, and export as a formatted manuscript ready for KDP upload. Stage 3 build.

---

## The Full Ecosystem Map

```
CONTENT RESEARCH (Cowork — weekly brief)
          ↓
ARTICLE DRAFT (Claude Code — generate-draft.js)
          ↓
    ┌─────┴──────────────────────────────┐
    ↓                                    ↓
WEBSITE ARTICLE                   REPURPOSED CONTENT
(MDX → GitHub → Vercel)           ├── YouTube script
                                  ├── Podcast script
                                  ├── Twitter/X thread
                                  ├── Instagram carousel
                                  └── TikTok script
                                          ↓
                              LONG TERM: Ebook compilation
```

Everything starts from one research brief. Everything is built on accurate, honest, expert-level content. The website is the foundation. Everything else amplifies it.

---

## Stage Roadmap

| Stage | Focus | Timeline |
|---|---|---|
| **Stage 1** | Build websites, content pipeline, affiliate income | Now → Month 6 |
| **Stage 2** | YouTube channels, social media accounts, social automation | Month 6 → Month 12 |
| **Stage 3** | Podcasts, ebooks, KDP publishing | Month 12 → Month 18 |
| **Stage 4** | Brand partnerships, sponsorships, premium content | Month 18+ |

**The rule: do not start Stage 2 until Stage 1 is generating consistent income and the content pipeline is running reliably without constant intervention.**

Stage 2 built on a shaky Stage 1 = chaos. Stage 2 built on a solid Stage 1 = compounding growth.

---

## Notes on AI Video & Voice Tools to Research

These are the tools most likely to power the YouTube and podcast side of the pipeline. Prices and quality change fast — research current options before committing.

| Tool | Use case | Notes |
|---|---|---|
| **Pictory** | Article to video | Converts written content to video with stock footage |
| **Synthesia** | AI presenter video | Realistic AI avatar reads a script on camera |
| **HeyGen** | AI avatar + voice | Strong quality in 2026, improving rapidly |
| **ElevenLabs** | AI voice for podcast | Realistic voice cloning, used for audio content |
| **InVideo** | Short-form video | Good for TikTok/Reels format |
| **Descript** | Video editing | Edit video by editing the transcript |

---

*Part of the Good Living Co project documentation. Tag: #good-living-co/hub*
*Updated: March 2026 — Stage 2+ planning only. Focus is Stage 1 first.*
