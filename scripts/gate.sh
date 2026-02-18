#!/usr/bin/env bash
set -euo pipefail

ERRORS=0
WARNINGS=0

log() {
  echo "[gate] $*"
}

print_output() {
  local output="${1:-}"
  if [ -z "$output" ]; then
    return
  fi
  while IFS= read -r line; do
    log "$line"
  done <<< "$output"
}

warn() {
  WARNINGS=$((WARNINGS + 1))
  log "WARN: $*"
}

fail() {
  ERRORS=$((ERRORS + 1))
  log "FAIL: $*"
  log "FAIL: ${ERRORS} errors, ${WARNINGS} warnings"
  exit 1
}

run_critical() {
  local description="$1"
  shift
  local output=""
  log "$description"
  if ! output="$("$@" 2>&1)"; then
    print_output "$output"
    fail "$description"
  fi
  print_output "$output"
}

log "repo: $(pwd)"
log "branch: $(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'not a git repo')"

log "check 1/5: Python syntax"
run_critical "python3 -m py_compile scripts/config.py" python3 -m py_compile scripts/config.py
run_critical "python3 -m py_compile scripts/extract_all.py" python3 -m py_compile scripts/extract_all.py
run_critical "find scripts -name '*.py' -exec python3 -m py_compile {} +" find scripts -name '*.py' -exec python3 -m py_compile {} +

log "check 2/5: Import test"
run_critical "python3 -c 'import scripts.config'" python3 -c "import scripts.config"
run_critical "python3 -c 'import scripts.phase1_discover'" python3 -c "import scripts.phase1_discover"
for mod in scripts/extractors/*.py scripts/generators/*.py scripts/verifiers/*.py; do
  if [ ! -f "$mod" ]; then
    continue
  fi
  if [ "$(basename "$mod")" = "__init__.py" ]; then
    continue
  fi
  modname="${mod%.py}"
  modname="${modname//\//.}"
  output=""
  if ! output="$(python3 -c "import ${modname}" 2>&1)"; then
    print_output "$output"
    warn "cannot import ${modname}"
  else
    print_output "$output"
    log "import OK: ${modname}"
  fi
done

log "check 3/5: Phase pipeline execution"
SOURCE_REPO="${WORLDSIM_SOURCE:-../new-world}"
if [ -d "$SOURCE_REPO/scripts" ]; then
  log "source repo: OK ($SOURCE_REPO)"
  run_critical "python3 scripts/extract_all.py --phase 1" python3 scripts/extract_all.py --phase 1
  if [ ! -f "extracted/manifest.json" ]; then
    fail "manifest.json not generated"
  fi
  run_critical "validate extracted/manifest.json JSON" \
    python3 -c "import json, pathlib; json.loads(pathlib.Path('extracted/manifest.json').read_text(encoding='utf-8'))"
  log "manifest: OK"
else
  warn "source repo not found at $SOURCE_REPO; skipping Phase 1 test"
fi

log "check 4/5: Generated .md frontmatter"
if [ -d "content" ]; then
  output=""
  if ! output="$(python3 - <<'PY'
import glob
import re
import sys

errors = []
files = glob.glob("content/**/*.md", recursive=True)

for path in files:
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        if text.startswith("---"):
            errors.append(f"{path}: unclosed frontmatter")
        else:
            errors.append(f"{path}: missing frontmatter")
        continue
    frontmatter = match.group(1)
    if not re.search(r"^title\s*:\s*.+$", frontmatter, re.MULTILINE):
        errors.append(f"{path}: missing title in frontmatter")
    generated_match = re.search(
        r"^generated\s*:\s*([^\n]+)$", frontmatter, re.MULTILINE
    )
    if not generated_match:
        errors.append(f"{path}: missing generated in frontmatter")
        continue
    generated_value = generated_match.group(1).strip().strip("'\"").lower()
    if generated_value not in {"true", "false"}:
        errors.append(f"{path}: generated must be true/false")

if errors:
    for error in errors:
        print(f"FAIL: {error}")
    sys.exit(1)

print(f"frontmatter: {len(files)} files OK")
PY
)"; then
    print_output "$output"
    fail "frontmatter validation failed"
  fi
  print_output "$output"
else
  warn "content/ directory not found; skipping frontmatter check"
fi

log "check 5/5: Summary"
if [ "$ERRORS" -gt 0 ]; then
  log "FAIL: ${ERRORS} errors, ${WARNINGS} warnings"
  exit 1
fi
log "PASS: ${WARNINGS} warnings"
