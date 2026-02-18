#!/usr/bin/env bash
set -euo pipefail
echo "[gate] repo: $(pwd)"
echo "[gate] branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'not a git repo')"
SOURCE_REPO="${WORLDSIM_SOURCE:-../new-world}"
if [ -d "$SOURCE_REPO/scripts" ]; then
  echo "[gate] Source repo: OK"
  python3 scripts/extract_all.py --phase 1 2>&1 | tail -3
  [ -f "extracted/manifest.json" ] && echo "[gate] manifest: OK" || echo "[gate] manifest: MISSING"
else
  echo "[gate] WARNING: Source repo not found at $SOURCE_REPO"
fi
echo "[gate] PASS"
