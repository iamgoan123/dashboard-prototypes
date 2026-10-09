# Prompts used for the three wireframes

These were written in a chat with the Claude artifact tool on. Each produced a single HTML page with a spec
panel that lists chart type, dimension, metrics and notes per block, so the layout can be rebuilt in Looker
Studio. The HTML files are in `wireframes/`.

## 1. Pinterest organic (Supermetrics, two query types)

> Lets create a pinterest organic dashboard quickly today. There are two query options: Top pins and profile
> based query. Lets make a dashboard that will show all pinterest organic things on a couple of pages, or a
> one pager is also fine. Create an artifact or something to show me the dashboard outline. This can be a
> wireframe model then I can replicate that into Looker Studio as well.

Notes from the build:
- The Profile query returns account totals, the Top pins query returns pin-level rows. They share no join key,
  so keep them on separate charts.
- The Profile source did turn out to have a Date dimension (look in the Time folder of the field list first).
  The Top pins source only has Start date, End date and Pin created date.
- Looker Studio bar charts need a dimension, so metric-only comparisons are built from scorecards.

Live link: https://claude.ai/artifact/LVtLvxd37rnMRhojm85QEf

## 2. LLM page layout (GA4 + GSC + optional Ahrefs)

> Can you create me the same artifact for the LLM page. The data sources I have are GA4 and GSC for this. I can
> also try Ahrefs if needed, what do you say?
>
> I just need more data about AI activity. I have the rest of the dashboard there though, I just need the AI LLM
> page layout so that I can update it.

Notes from the build:
- Blocks are tagged by source (GA4, GSC, Ahrefs) and by New or Revise against the existing page.
- Search Console now has a Generative AI report (AI Overviews and AI Mode impressions, from 18 May 2026), but
  at the time it was not in the Search Analytics API, so it is marked as a CSV import.
- Ahrefs Brand Radar has a Looker Studio connector on Advanced plans and above, and needs its own add-on.
- The sample figures on the page were copied from the existing 99 Bikes report. Keep the repo private.

Live link: https://claude.ai/artifact/TdejnNJWxfGwAnFrZXYfY7

## 3. Google Business Profile, multi-client

> can we create a dashboard for GMB? for like all clients using supermetrics?

Notes from the build:
- Supermetrics counts each location as a separate account, so total the locations against the licence first.
- Pages are tagged Internal only or Client-safe. Page 1 (portfolio) lists every client and must not go into a
  client copy.
- Search terms are monthly only and appear after month end. Average star rating is blank when a period has no
  reviews.

Live link: https://claude.ai/artifact/N3zhvGGWJgobC7VgRx6uwJ

## 4. Turning the GBP wireframe into a working dashboard

> Lets try this with just CABLE as a brand?
> Here is the data then: <sheet link>. Can you create a dashboard, live version, here?
> If you want to use all the data, use all the data instead.

That became `prompts/gbp-dashboard-prompt.md` and `code/gbp-dashboard/`.
