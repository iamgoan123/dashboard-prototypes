# Dashboard prototypes

Wireframes and a working dashboard built in Claude chats, so the work can be repeated and handed over.
Everything here is self-contained HTML plus a small Python build script. No client performance data is
committed. The real data lives in the Supermetrics sheet and is read at build time.

## What is in here

| Item | What it is | Link or path |
| --- | --- | --- |
| Google Business Profile, all brands (live) | Working dashboard, 248 locations, 4 brands, September 2026 | https://claude.ai/artifact/YQgouhH8Jd3XkVuVs7VDMn |
| Google Business Profile wireframe | Multi-client layout (portfolio, location detail, reviews) | https://claude.ai/artifact/N3zhvGGWJgobC7VgRx6uwJ |
| LLM page layout wireframe (99 Bikes AU) | GA4 + GSC + optional Ahrefs layout for an AI traffic page | https://claude.ai/artifact/TdejnNJWxfGwAnFrZXYfY7 |
| Pinterest organic wireframe | Supermetrics Pinterest Organic, Profile and Top pins queries | https://claude.ai/artifact/LVtLvxd37rnMRhojm85QEf |

The Claude links are private to the account that published them until that person shares them from the
artifact's share controls. The HTML source for every one of them is in this repo.

```
code/gbp-dashboard/      template.html, build.py, sample-data.csv  (the live dashboard)
wireframes/              the three wireframe pages as standalone HTML
docs/gbp-dashboard.md    full write-up: prompt, data source, logic, gotchas, how to repeat it
docs/supermetrics-gmb-query.md   exact Supermetrics query, metrics, dimensions, sheet columns
prompts/                 reusable prompts for the dashboard and for the wireframes
```

## Repeat the Google Business Profile dashboard

1. In Supermetrics (Google Sheets), run the Google My Business query described in
   `docs/supermetrics-gmb-query.md` for the accounts you want, with the date range set to **Last month**.
2. Download Sheet1 as CSV.
3. Build it:
   ```
   python3 code/gbp-dashboard/build.py export.csv --out dashboard.html --period "October 2026" --read-on "8 Nov 2026"
   ```
   Try it first with `code/gbp-dashboard/sample-data.csv` (made-up numbers).
4. Open `dashboard.html` in a browser, or ask Claude to publish it as an artifact.

Or skip the script and paste `prompts/gbp-dashboard-prompt.md` into Claude with the sheet link.

## Adding a brand

Add the account name to `ACCOUNT_CODES` in `build.py`, then add a matching entry to the `BR` and `ORDER`
objects at the top of the script in `template.html` (display name, short label, colour, prefix to strip from
location names). Add a colour variable such as `--xx` to the `:root` block, and to both dark mode blocks.

## Privacy

Keep this repo private. The wireframe for the LLM page uses sample figures copied from a 99 Bikes report, and
the dashboard is built from client location data. Do not commit exports or the built `dashboard.html`.
