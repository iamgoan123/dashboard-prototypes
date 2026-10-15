#!/usr/bin/env bash
set -euo pipefail
cd /workspace
python3 build.py sample-data.csv --out sample-dashboard.html \
  --period "October 2026" --read-on "8 Nov 2026"
