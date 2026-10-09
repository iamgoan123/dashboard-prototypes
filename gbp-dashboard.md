# Google Business Profile dashboard, all brands

Live (private until shared): https://claude.ai/artifact/YQgouhH8Jd3XkVuVs7VDMn

A working dashboard built from the Supermetrics Google My Business export: 248 listings across Baby Bunting,
Cable Melbourne, Converse and GAZMAN, for September 2026. It is a snapshot with the data embedded, so it does
not refresh itself.

## How it was made, in order

1. **Wireframe first.** A three-page layout (portfolio, location detail, reviews) was drafted as a published
   artifact so it could be rebuilt in Looker Studio. See `wireframes/gbp-multi-client-dashboard-wireframe.html`.
2. **Data pulled with Supermetrics.** The query and fields are in `supermetrics-gmb-query.md`. The Supermetrics
   data tools were not available in the chat, so the result was exported to a Google Sheet.
3. **Sheet read in chunks.** The Google Workspace sheets read tool returns about 100 rows per call, so the sheet
   was read in blocks (rows 2 to 100, row 101, rows 102 to 198, rows 199 to 249, and the region and postcode
   columns separately). Trailing empty rows are trimmed by the API, so the last two listings came back with no
   metrics and were padded as no-data rows.
4. **Rows validated before building.** For all 248 rows, Total views equalled the four Maps and Search device
   columns added together, and Total actions equalled website plus calls plus directions. Zero mismatches.
5. **Dashboard generated** as `template.html` with the rows injected at the `/*__DATA__*/[]` marker. Vanilla
   JavaScript, no libraries.
6. **Tested in a headless browser** (Playwright and Chromium): no JavaScript errors, the Cable filter, the
   location detail panel and a phone-width dark mode render all checked, screenshots reviewed, and the layout
   bugs found that way fixed (bar scaling, wrapped value labels, wrong hidden-listing count).
7. **Published as an artifact.**

## What the dashboard does

- Brand buttons, a region filter, and a "hide closed, coming soon, offices and no-data listings" checkbox
  (on by default, 9 listings hidden). Unticking it makes the totals match the sheet.
- Overview: KPI cards, brand comparison table (click a row to filter), views by surface and device, action
  mix, views by state, top 10 locations, and low interaction rate with high views.
- Locations: scatter of views against interaction rate, sortable searchable table, detail panel.
- Reviews: ratings by brand, rating bands, median reply time, lowest-rated locations.
- Data notes tab explains every definition and how to rebuild it in Looker Studio.

## Logic worth knowing

| Item | Rule |
| --- | --- |
| Views | Maps + Search views, from the four device columns |
| Actions | Website visits + phone calls + directions requests |
| Interaction rate | Actions divided by views |
| Rate rankings | Only locations with 1,000+ views (the scatter starts at 500). Tiny listings show inflated rates |
| Brand rating | All-time rating weighted by total review count |
| Reply time | Median of the per-location averages |
| State | From the Australian postcode ranges (ACT, NSW, VIC, QLD, SA, WA, TAS, NT). Region code NZ is shown as NZ |
| Hidden listings | Names containing "(Coming Soon)", "(Closed", "relocated", "Corporate Office", "Head Office", and rows with no views |
| Duplicate names | A repeated location name inside a brand gets its postcode appended |

## Gotchas hit along the way

- Sheets drops leading zeros, so a New Zealand postcode such as 0814 appears as 814. State logic uses the
  region code first, so this does not matter.
- A published page cannot call Google or any other site, so live refresh needs a Looker Studio rebuild or a
  republish after the sheet refreshes.
- Looker Studio bar charts need a dimension, and comparing several metrics side by side needs scorecards.
- Sorting a Looker Studio table by its comparison change is not available, so rank on the rate instead.

## Repeat it next month

1. Refresh the Supermetrics query, or make a new one with the same fields and Last month.
2. Download Sheet1 as CSV.
3. `python3 code/gbp-dashboard/build.py export.csv --out dashboard.html --period "<Month Year>" --read-on "<date>"`
4. Check the warnings the script prints (unknown account, views or actions that do not add up).
5. Open the file locally, or ask Claude to publish it as an artifact.

Or paste `prompts/gbp-dashboard-prompt.md` into Claude with the new sheet link.

## Rebuilding it live in Looker Studio

One data source from the Supermetrics Google My Business connector, date range Last month, no date dimension.
Add a Brand calculated field from the account name. Scorecards use Total views, Total actions, Website visits,
Phone calls, Directions requests and Total review count. The brand table has Brand as the dimension. The scatter
is a bubble chart with Total views on x and a calculated Total actions / Total views on y. Hide non-live
listings with a filter on location name.
