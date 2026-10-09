#!/usr/bin/env python3
"""
Build the "Google Business Profile: all brands" dashboard.

Input : a CSV downloaded from the Supermetrics sheet "Master - GMB - All Data"
        (File > Download > Comma-separated values, Sheet1 only).
Output: one self-contained HTML file with the data embedded.

Usage:
    python3 build.py my-export.csv --out dashboard.html --period "October 2026" --read-on "8 Nov 2026"
    python3 build.py sample-data.csv --out sample-dashboard.html   # try it with dummy data

The CSV is read by header name, so column order does not matter. Headers must
match the Supermetrics field labels listed in docs/gbp-dashboard.md.
"""
import argparse, csv, json, pathlib, sys

# Account name in the sheet -> one-letter brand code used by template.html.
# To add or rename a brand, change this dict AND the BR / ORDER objects near the
# top of the <script> in template.html (name, short label, colour, name prefix).
ACCOUNT_CODES = {
    "Baby Bunting": "B",
    "Cable Melbourne": "C",
    "Converse": "V",
    "GAZMAN": "G",
}

def num(v):
    """Blank -> None, otherwise int or float."""
    if v is None:
        return None
    v = str(v).strip().replace(",", "")
    if v == "":
        return None
    f = float(v)
    return int(f) if f.is_integer() else f

def build_rows(csv_path):
    rows, problems = [], []
    with open(csv_path, newline="", encoding="utf-8-sig") as fh:
        for i, r in enumerate(csv.DictReader(fh), start=2):
            acct = (r.get("Account name") or "").strip()
            code = ACCOUNT_CODES.get(acct)
            if code is None:
                problems.append(f"row {i}: unknown account '{acct}' (add it to ACCOUNT_CODES)")
                continue
            region = (r.get("Address region code") or "AU").strip() or "AU"
            tv = num(r.get("Total views"))
            row = [
                code, r["Location name"].strip(), region, (r.get("Postal code") or "").strip(),
                tv,
                num(r.get("Views on maps (Desktop)")), num(r.get("Views on maps (Mobile)")),
                num(r.get("Views on Search (Desktop)")), num(r.get("Views on Search (Mobile)")),
                num(r.get("Total actions")),
                num(r.get("Website visits")), num(r.get("Phone calls")), num(r.get("Directions requests")),
                num(r.get("Monthly search impressions")),
                num(r.get("Reviews")), num(r.get("Avg. review star rating")),
                num(r.get("Review time to respond (minutes)")),
                num(r.get("Total review count")), num(r.get("Avg. overall star rating")),
            ]
            if tv is None:                      # listing returned no performance data
                row[4:13] = [None] * 9
                row[13:] = [None] * 6
            else:                               # integrity checks
                if tv != sum(row[5:9]):
                    problems.append(f"row {i} {row[1]}: views {tv} != maps+search split {sum(row[5:9])}")
                if row[9] != sum(row[10:13]):
                    problems.append(f"row {i} {row[1]}: actions {row[9]} != website+calls+directions {sum(row[10:13])}")
            rows.append(row)
    return rows, problems

def main():
    here = pathlib.Path(__file__).parent
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--template", default=str(here / "template.html"))
    ap.add_argument("--out", default="dashboard.html")
    ap.add_argument("--period", default="September 2026", help="label for the month the data covers")
    ap.add_argument("--read-on", default="9 Oct 2026", help="date the sheet was read (footer)")
    a = ap.parse_args()

    rows, problems = build_rows(a.csv)
    tpl = pathlib.Path(a.template).read_text(encoding="utf-8")
    marker = "/*__DATA__*/[]"
    if tpl.count(marker) != 1:
        sys.exit("template.html must contain exactly one /*__DATA__*/[] marker")
    html = tpl.replace(marker, json.dumps(rows, ensure_ascii=False, separators=(",", ":")))
    html = html.replace("/*__PERIOD__*/'September 2026'", json.dumps(a.period))
    html = html.replace("/*__READ_ON__*/'9 Oct 2026'", json.dumps(a.read_on))
    pathlib.Path(a.out).write_text(html, encoding="utf-8")

    print(f"{len(rows)} locations written to {a.out}")
    if problems:
        print("Check these rows:")
        for p in problems:
            print("  -", p)

if __name__ == "__main__":
    main()
