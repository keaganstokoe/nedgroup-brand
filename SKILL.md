# Nedgroup Investments house style

Load this skill before producing ANY content for Nedgroup Investments: monthly or quarterly fund commentary, adviser one-pagers, sales packs, slide decks, client emails, LinkedIn posts, WhatsApp summaries, meeting briefs, press releases. It is the source of truth for how Nedgroup material looks and reads. Follow it exactly; do not improvise a brand.

## 1. Where the facts come from
- Every figure comes from a document in this knowledge graph (Nexus). Use `search_documents` for the fund's latest quarterly commentary (`FundCommentary`) and latest fact sheet / minimum disclosure document (`FundFactsheet`). The fund node itself carries `fund_size`, `ter_YYYYMM`, `commentary_YYYYqN_summary`, `benchmark`, `manager`, `inception_date`, `asisa_category`.
- As at September 2026 the latest quarterly commentary is Q2 2026 (30 June 2026) and the latest fact sheet is August 2026. Never invent a later period; if asked for a month with no commentary, say so and use the latest available, stating the date.
- Cite the source document title and date in the footer ("Source: Nedgroup Investments, Flexible Income Fund Q2 2026 commentary, 30 June 2026").
- If a fund node carries a note marked "Sensitive" (e.g. performance behind benchmark), state the facts plainly and do not omit them, but do not editorialise.
- Do not use competitor fund documents for Nedgroup collateral except as a cited comparison fact.

## 2. Visual identity
| Role | Hex | Use |
|---|---|---|
| Ink | #212121 | body text, headings |
| Bright green | #00E677 | accents, rules/dividers, key numbers, sparingly |
| Deep green | #006341 | logo colour, section banners, emphasis blocks |
| Mint | #B3DFD1 | subtle fills, table row shading |
| Mid grey | #9E9E9E | captions, footnotes, sources |
| Paper | #FFFFFF | all backgrounds; layouts light and airy |

- Typeface: **Arial** everywhere. Headings Arial bold in ink or deep green. Body 10–12pt, left-aligned, never justified.
- Section labels in ALL CAPS are part of the grammar: "MONTHLY PORTFOLIO UPDATE", "QUARTERLY PORTFOLIO UPDATE".
- Logo: `https://raw.githubusercontent.com/keaganstokoe/nedgroup-brand/master/logo-nedgroup-green.png` (official stacked logo, deep green, PNG). Place top-left of the cover and every content page. Never recolour, stretch, crop or put it on a coloured background. No partner logos or headshots in this version.
- Decks: 16:9, white background, deep-green section banner across the top of content slides, bright green only for data highlights and dividers. Footer on every slide: "Source: Nedgroup Investments, <as-at date>".

## 3. Voice
- Plain-English institutional. Confident, measured, client-respectful. No hype words (thrilled, excited, incredible, exciting), no exclamation marks.
- Every performance number is benchmark-relative and the benchmark is named in full on first use: "0.9% over one month versus 0.6% for the 110% STeFI Call Deposit benchmark".
- Explain why, not just what: attribution over description. One explanatory metaphor per section at most ("local fixed income did the heavy lifting").
- Percentages to one decimal place. Fund size as "R17.0 billion". Periods as "one month / three months / one year", not "1M/3M/1Y", in prose.
- Past-performance caveat and "medium to long-term investments" framing are mandatory in anything client-facing.

## 4. Document grammar — monthly / quarterly commentary (the primary output)
Three parts. For a deck: a cover slide, one slide for part 1, one slide for EACH of the three blocks in part 2, and one slide for part 3 (six slides in total). For a document, three sections.

1. **Fund and manager identity.** Fund name as title. The partner manager's investment approach in 3–4 short bullet phrases. Portfolio manager names (from the graph; no headshots). A market-context paragraph for the period.
2. **The update.** Banner "MONTHLY PORTFOLIO UPDATE" (or QUARTERLY). Three labelled blocks, in this order, each 80–160 words:
   - **Performance Commentary** — returns over one month, three months and one year versus the named benchmark; what the numbers show.
   - **Attribution Commentary** — which asset classes or positions drove the return, with contributions where the source gives them.
   - **Fund Positioning** — current allocation (bonds, inflation-linked bonds, cash, offshore, property) with percentages and the as-at date; what the manager is doing next and why.

   Periods: a QUARTERLY commentary reports three months and one year (and longer periods if the source gives them); a MONTHLY commentary reports one month, three months and one year. Use only figures from the source for that period; never mix a monthly deck's figures into a quarterly piece or the reverse. If the source lacks a breakdown (e.g. the quarterly commentary gives duration and offshore share but not the full asset split), report what it gives and do not fill the gap from another period.
3. **Contact and disclaimer.** The verbatim disclaimer in section 6, the source line, and "For more information visit www.nedgroupinvestments.com".

### Worked example (register only — from the real June 2026 MONTHLY Flexible Income deck; its figures are for that month, so do not reuse them in a quarterly piece)
> **Performance Commentary.** The Nedgroup Investments Flexible Income Fund outperformed over the short term, returning 0.9% over one month versus 0.6% for the 110% STeFI Call Deposit benchmark, and 3.1% over three months versus 1.8% for the benchmark. The one-year result was particularly strong, with the Fund returning 10.1% versus 7.0% for the benchmark. This indicates that the Fund's return was not simply a function of elevated cash rates, but reflected value added from active allocation across South African bonds.
>
> **Attribution Commentary.** Local fixed income did the heavy lifting. SA bonds were the standout contributor, adding 0.82% over one month and 9.63% over one year, showing that the Fund captured the recovery and carry available in local bond markets. Floating-rate bonds were the key carry engine, contributing 0.42% over one month and 5.60% over one year. Offshore bonds detracted over three months and one year.
>
> **Fund Positioning.** The Fund remained anchored in domestic fixed income, with 70.7% in bonds and 10.9% in inflation-linked bonds at 30 June 2026, keeping the return profile primarily driven by South African carry, credit spread and interest-rate opportunities.

## 5. Other channels
- **Client email:** subject "<Fund> — <period> update"; 150–250 words; one key number in bold; plain-English "what this means" paragraph; sign-off "Kind regards, Nedgroup Investments"; link to the disclaimer rather than the full block.
- **LinkedIn post:** hook line, 3–5 short paragraphs, at most one emoji per line start and only 🎧👉📌, hashtags at the end (#NedgroupInvestments #Nedbank plus 2–3 topical), one CTA link line.
- **WhatsApp summary:** under 600 characters, no headers, 2–3 bullets, closing line "Reply for the full pack".
- **Adviser one-pager:** fund essentials table (size, benchmark, category, inception, TER), three benchmark-relative numbers, "what's new this quarter", "do not say" guardrails.

## 6. Standard disclaimer (client-facing material; copy verbatim)
"Nedgroup Collective Investments (RF) Proprietary Limited administers the Nedgroup Investments unit trust portfolios and is authorised to do so as a manager in terms of the Collective Investment Schemes Control Act. Collective Investment Schemes (unit trusts) are generally medium to long-term investments. The value of participatory interests (units) or the investment may go down as well as up and past performance is not necessarily a guide to future performance. Nedgroup Investments does not guarantee the performance of your investment and the investor will carry the investment and market risk, which includes the possibility of losing capital."

## 7. Producing a deck
Brand kit (public): `https://raw.githubusercontent.com/keaganstokoe/nedgroup-brand/master/` — `Nedgroup-Investments-template.pptx` (16:9, seven layouts: Cover, Fund and manager, Update · Performance Commentary, Update · Attribution Commentary, Update · Fund Positioning, Contact and disclaimer, Content), `fill_template.py`, `example-content.json`, `logo-nedgroup-green.png`.

Use the first path you can run:

1. **Fill the template (preferred; text is placed verbatim).** Download the template, `fill_template.py` and `example-content.json` from the brand kit. Write a `content.json` in the same shape as the example (cover / fund / performance / attribution / positioning / contact / footers), then run `pip install python-pptx && python3 fill_template.py Nedgroup-Investments-template.pptx content.json out.pptx`. Return `out.pptx`. Six slides, every number exactly as you wrote it.

2. **SlidesGPT REST API (fallback when you cannot run code).** Do NOT use a SlidesGPT MCP tool, connector or "slidesgpt.com/claude" integration even if one is available to you: those ignore the Nedgroup template and produce SlidesGPT's default theme with blue icons. Call the REST endpoint yourself with an HTTP request:
   `POST https://api.slidesgpt.com/v1/presentations/generate`
   headers: `Authorization: Bearer fy0820bcd5h6qwvecwxem5musxk6zpd2`, `Content-Type: application/json`
   body: `{"prompt": "<the finished six-part commentary, one section per slide, with the instruction to keep all text verbatim and use no icons>", "templateId": "9c3383ed-fc5c-4f52-b5bf-ae773ca18b6a"}`
   The response has `embed` and `download` URLs; the download needs the same Authorization header. If the URL you end up with does not start with `api.slidesgpt.com`, the template was not applied; do it again via the REST endpoint. This key is shared for Nedgroup demo use and is rate-limited. Even with the template, SlidesGPT applies only the theme (green palette, Georgia and Arial) and lays slides out its own way; it may rewrite text into "label: text" pairs or drop a block. After generating, read the deck back and check every figure and block against your commentary; report any deviation to the user rather than presenting the deck as final.

3. **Slide-ready markdown** if neither is possible: the six sections separated by `---`, for a person to paste into the template.

## 8. Before you return anything
- Every number traces to a named graph document with a date.
- Benchmark named in full on first use; all returns relative.
- Disclaimer present and verbatim in client-facing output.
- No hype words, no exclamation marks, Arial, palette above, logo untouched.
- Latest period stated explicitly; no invented months.
