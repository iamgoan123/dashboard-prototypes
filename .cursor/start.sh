#!/usr/bin/env bash
set -euo pipefail
cd /workspace
PORT=8080
if curl -sf "http://127.0.0.1:${PORT}/sample-dashboard.html" >/dev/null 2>&1; then
  exit 0
fi
exec python3 -m http.server "$PORT" --bind 0.0.0.0
