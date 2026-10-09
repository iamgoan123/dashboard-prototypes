# Prompt: Google Business Profile dashboard from a Supermetrics sheet

Paste this into a Claude chat that has the Google Workspace (Sheets) connector and artifact publishing on.
Replace the sheet link, brand list and month.

---

Build me a working dashboard from this Google Sheet: **<SHEET LINK>**

**About the data**
- It is a Supermetrics export from the Google My Business connector, Sheet1, one row per location, for
  **<MONTH YEAR>** (the query used "Last month"). Brands: <BRAND 1>, <BRAND 2>, <BRAND 3>, <BRAND 4>.
- Columns: account and location names, region code, postal code, Total views, Views on Maps and Search split
  by desktop and mobile, Total actions, Website visits, Phone calls, Directions requests, Monthly search
  impressions, Reviews (new this month), Avg. review star rating, Review time to respond (minutes), Total
  review count, Avg. overall star rating. Messages, bookings, menu clicks and food orders are all zero.
- There is no date dimension, so do not draw trend lines or period comparisons.

**Read the data**
- Read every row with the Google Workspace sheets read tool. It returns about 100 rows per call, so read in
  chunks of 99 rows or fewer, and note that trailing empty rows are trimmed.
- Check every row: Total views must equal the four views columns added up, and Total actions must equal
  website visits plus phone calls plus directions. Report any mismatch before building.

**Build**
- One self-contained HTML file, vanilla JavaScript, no external libraries, the data embedded as JSON.
- Global filters: brand buttons (All brands plus one per brand), region drop-down (state worked out from the
  Australian postcode, New Zealand shown as NZ), and a checkbox "Hide closed, coming soon, offices and
  no-data listings" that is ticked by default. Flag listings by name: "(Coming Soon)", "(Closed", "relocated",
  "Corporate Office", "Head Office", and rows with no views.
- Tabs:
  1. Overview: 8 KPI cards (locations, views, actions, interaction rate = actions / views, website visits,
     calls, directions, all-time rating weighted by review count); a brand table that filters the dashboard
     when clicked; stacked bars for views by surface and device and for the action mix, per brand; views by
     state; top 10 locations by views; "seen a lot, acted on little" (lowest interaction rate among
     locations with 3,000+ views).
  2. Locations: scatter of views (log scale) against interaction rate for locations with 500+ views, coloured by
     brand, clickable; a searchable, sortable table of all locations; a detail panel for the selected location
     with surface split, action split, rank within the brand, and review facts.
  3. Reviews: rating by brand, rating bands, median reply time, lowest-rated locations with 50+ reviews.
  4. Data notes: what the numbers mean, which listings are hidden, how to rebuild it in Looker Studio.
- Only rank by interaction rate where a location has 1,000+ views, because small locations have inflated rates.
- Design: clean and data-dense, one accent colour per brand, light and dark mode, readable on a phone,
  tabular numbers, no em dashes in any text.

**Check and publish**
- Test it in a headless browser for JavaScript errors, then check the Cable (or first brand) filter, a location
  detail panel and a phone-width render.
- Publish it as an artifact and give me the link. Tell me it is a snapshot that will not refresh itself.
