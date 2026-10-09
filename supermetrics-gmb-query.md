# Supermetrics Google My Business query

Where the data comes from and exactly how it was pulled.

## Setup

| Setting | Value |
| --- | --- |
| Connector | Supermetrics, **Google My Business** (Google Business Profile) |
| Destination | Google Sheets (Supermetrics add-on) |
| Spreadsheet | "Master - GMB - All Data" |
| Output range | `Sheet1!A1:AH249` (header row plus 248 locations) |
| Date range type | **Last month** (query created 8 Oct 2026, so September 2026) |
| Accounts | "All locations of" Baby Bunting, Cable Melbourne, Converse, GAZMAN (4 business accounts) |
| Filters, sort, segment | none |
| Max rows | 1,000,000 |
| Support sheet | `SupermetricsQueries` holds the saved query. Do not rename or delete it, or the query cannot refresh |
| Sheet time zone setting | America/Los_Angeles (see the caveat below) |

In the sidebar: Supermetrics > Get data from your data sources > Google My Business > tick the four "All
locations of ..." accounts > Last month > add the metrics and dimensions below > Get data to table.

## Metrics (23)

| Supermetrics field | Sheet column label |
| --- | --- |
| views_total | Total views |
| views_maps | Views on Maps |
| views_search | Views on Search |
| views_maps_desktop | Views on maps (Desktop) |
| views_maps_mobile | Views on maps (Mobile) |
| views_search_desktop | Views on Search (Desktop) |
| views_search_mobile | Views on Search (Mobile) |
| actions_total | Total actions |
| actions_website | Website visits |
| actions_phone | Phone calls |
| actions_driving_directions | Directions requests |
| actions_messages | Messages |
| actions_bookings | Bookings |
| actions_food_menu_clicks | Menu clicks |
| actions_food_orders | Food orders |
| post_count | Posts |
| search_impressions | Monthly search impressions |
| review_total_count | Reviews (new in the period) |
| review_avg_star_rating | Avg. review star rating (period) |
| review_reply_response_time | Review time to respond (minutes) |
| total_review_count | Total review count (all time) |
| total_review_star_rating | Avg. overall star rating (all time) |
| media_total_count | Media items |

## Dimensions (11)

location_account_id, location_account_name, location_name, location_description, location_store_code,
location_website_url, location_latitude, location_longitude, location_attributes,
location_address_region_code, location_address_postal_code.

There is no date dimension in this query, so each row is one location for the whole month.

## Sheet layout (columns A to AH)

A Account ID, B Account name, C Location name, D Location description, E Store code, F Website URL,
G Latitude, H Longitude, I Attributes, J Address region code, K Postal code, L Total views, M Views on Maps,
N Views on Search, O Views on maps (Desktop), P Views on maps (Mobile), Q Views on Search (Desktop),
R Views on Search (Mobile), S Total actions, T Website visits, U Phone calls, V Directions requests,
W Messages, X Bookings, Y Menu clicks, Z Food orders, AA Posts, AB Monthly search impressions, AC Reviews,
AD Avg. review star rating, AE Review time to respond (minutes), AF Total review count,
AG Avg. overall star rating, AH Media items.

`build.py` reads these by header name, so renaming a header breaks the build.

## Field notes and caveats

- **Each location counts as one Supermetrics "account"** against the licence, so total the locations across
  all brands before connecting more.
- Total views = Maps + Search. Maps = desktop + mobile. Search = desktop + mobile. Total actions = website
  visits + phone calls + directions requests (the other action columns were zero for every location).
- **Monthly search impressions** are Google's monthly figure per listing. They are usually available only after
  the month ends, and Google hides low-volume search terms.
- **Avg. review star rating** is for the period only and is blank when there were no new reviews. **Avg. overall
  star rating** and **Total review count** are all time.
- **Review time to respond** is an average per location and has extreme values (one listing is over 500 days),
  so the dashboard shows the median.
- Several columns are blank for brand-new or empty listings. Two Cable David Jones listings returned no data.
- Google counts one impression per user per day, so these views will not match Search Console impressions.
- Supermetrics refreshes Google My Business data best every 2 to 3 days, and location time zones can shift
  daily numbers. Month totals are less affected, but the sheet time zone is not an Australian one.
- Old Google fields (post views, photo views, queries direct and indirect, location followers) are deprecated
  in the connector. Do not add them back.

## Why the sheet instead of a direct query in chat

In the chat the Supermetrics connector only exposed its free utilities (UTM, page speed and link checks), not
the data query tools. The data was therefore exported to a Google Sheet and read with the Google Workspace
connector. If the data tools are available in a future chat, ask Claude to list the data sources, accounts and
fields, then run the same query directly.
