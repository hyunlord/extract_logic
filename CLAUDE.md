# WorldSim Docs — CLAUDE.md

## Agent Identity

You are a **senior technical documentation engineer and data extraction specialist** building a fully automated, self-verifying documentation pipeline for the WorldSim game project.

Core expertise: Python data extraction, GDScript analysis, MkDocs Material, information architecture.

**Your mandate:** Build a system where `python scripts/extract_all.py` is the ONLY command needed. It discovers everything, generates everything, verifies everything. No hardcoded lists. No manual page creation. No stale documentation.

---

## Design Philosophy: Zero-Hardcode Autodiscovery

### The Problem
The game codebase (`../new-world/`) is under heavy active development. Systems, data files, localization keys, and cross-system interactions will grow dramatically. Any hardcoded list of "known systems" or "known pages" will rot immediately.

### The Solution
**Every piece of generated documentation is derived from filesystem scanning + code analysis.** Nothing is assumed to exist. Nothing is hardcoded.

```
../new-world/ (source of truth — READ ONLY, never modify)
        │
        ▼
  python scripts/extract_all.py   ← SINGLE ENTRY POINT
        │
        ├─ Phase 1: DISCOVER
        │   ├─ Scan scripts/systems/*.gd → system registry
        │   ├─ Scan scripts/core/*.gd → core module registry
        │   ├─ Scan scripts/ai/*.gd → AI module registry
        │   ├─ Scan data/**/*.json → data file registry
        │   ├─ Scan localization/**/*.json → locale registry
        │   └─ Output: manifest.json (what exists in the game repo RIGHT NOW)
        │
        ├─ Phase 2: EXTRACT
        │   ├─ For each discovered system → extract metadata, constants, formulas, references
        │   ├─ For each discovered data file → parse JSON structure and content
        │   ├─ For each locale file → build ko/en glossary
        │   ├─ For each core module → extract fields, signals, APIs
        │   ├─ Cross-reference: who imports whom, who emits what signal, who reads what field
        │   └─ Output: extracted/ intermediate JSON files
        │
        ├─ Phase 3: GENERATE
        │   ├─ For each extracted system → generate content/systems/<name>.md
        │   ├─ For each extracted data file → generate content/data/<name>.md
        │   ├─ For each locale category → generate content/glossary/<category>.md
        │   ├─ For each core module → generate content/core/<name>.md
        │   ├─ From cross-references → generate content/interactions/<pair>.md
        │   ├─ Generate content/systems/_index.md (execution order + architecture diagram)
        │   ├─ Generate content/config-reference.md (all constants)
        │   ├─ Generate content/index.md overview with live stats
        │   ├─ Scan content/**/*.md → generate mkdocs.yml nav section
        │   └─ Output: content/*.md + mkdocs.yml (complete, ready to build)
        │
        ├─ Phase 4: EXPORT
        │   ├─ Merge content/ → exports/worldsim-full.md (single LLM-context file)
        │   ├─ Selective merges → exports/worldsim-systems.md, worldsim-data.md, etc.
        │   └─ Size check: warn if >100KB
        │
        └─ Phase 5: VERIFY
            ├─ Coverage check: every .gd file in systems/ has a doc page
            ├─ Coverage check: every .json in data/ has a doc page
            ├─ Coverage check: every locale key appears in glossary
            ├─ Staleness check: no content/*.md references a file that doesn't exist
            ├─ Completeness check: no "TODO" or "Placeholder" left in generated pages
            ├─ Consistency check: constants in docs match actual code values
            ├─ Cross-ref check: every signal emitter has a documented subscriber (or flagged)
            ├─ Link check: all internal Markdown links resolve
            ├─ Size check: exports under limits
            └─ Output: verification_report.json + console summary
```

### Key Principles

1. **manifest.json is the source of truth for what to document.**
   The pipeline discovers what exists, writes it to `manifest.json`, and all subsequent phases read from it. If a system doesn't appear in the game repo scan, it doesn't get a page.

2. **No placeholder pages.**
   Pages are created by extraction scripts or don't exist. If extraction can't parse something, it generates a page with a `⚠️ EXTRACTION INCOMPLETE` banner — never an empty "Placeholder" page.

3. **mkdocs.yml nav is ALWAYS auto-generated.**
   The `nav:` section in `mkdocs.yml` is rebuilt every run by scanning `content/**/*.md` and reading each file's frontmatter `title` and `nav_order` fields.

4. **Manual content survives regeneration.**
   Files in `content/_manual/` are never overwritten. They're merged into the nav alongside generated pages. For adding narrative context to generated pages, use `<!-- MANUAL:START -->` / `<!-- MANUAL:END -->` markers inside generated files — the generator preserves content between these markers.

5. **Verification is not optional.**
   Phase 5 runs automatically. If critical checks fail, the exit code is non-zero and the gate fails. Warnings are logged but don't block.

---

## Repository Structure

```
worldsim-docs/
├── CLAUDE.md                        # This file
├── AGENTS.md                        # Codex worker instructions
├── PROGRESS.md                      # Append-only work log
├── mkdocs.yml                       # Auto-generated nav + static config
├── requirements.txt                 # Python deps
├── .gitignore
│
├── scripts/
│   ├── extract_all.py               # ★ SINGLE ENTRY POINT — runs entire pipeline
│   ├── config.py                    # Pipeline configuration (source repo path, output dirs)
│   │
│   ├── phase1_discover.py           # Filesystem scan → manifest.json
│   ├── phase2_extract.py            # Code/data parsing → extracted/*.json
│   ├── phase3_generate.py           # Markdown generation → content/**/*.md + mkdocs.yml nav
│   ├── phase4_export.py             # Merge docs → exports/*.md
│   ├── phase5_verify.py             # Coverage/staleness/consistency checks
│   │
│   ├── extractors/                  # Modular extractors (one per source type)
│   │   ├── __init__.py
│   │   ├── gdscript_constants.py    # const/var/enum/dict from .gd files
│   │   ├── gdscript_systems.py      # System metadata (priority, interval, description)
│   │   ├── gdscript_formulas.py     # Math formulas from code + comments
│   │   ├── gdscript_references.py   # Cross-file imports, signal emit/connect, field access
│   │   ├── gdscript_signals.py      # SimulationBus signal definitions
│   │   ├── json_data.py             # Generic JSON data file parser
│   │   └── locale.py                # Localization JSON parser
│   │
│   ├── generators/                  # Modular generators (one per output type)
│   │   ├── __init__.py
│   │   ├── system_page.py           # System documentation page
│   │   ├── data_page.py             # Data file documentation page
│   │   ├── glossary_page.py         # Glossary/terminology page
│   │   ├── core_page.py             # Core module documentation page
│   │   ├── interaction_page.py      # Cross-system interaction page
│   │   ├── config_reference.py      # GameConfig constants page
│   │   ├── index_page.py            # Site index with live stats
│   │   └── nav_builder.py           # mkdocs.yml nav auto-generator
│   │
│   ├── verifiers/                   # Modular verification checks
│   │   ├── __init__.py
│   │   ├── coverage.py              # Every source file has a doc page
│   │   ├── staleness.py             # No doc references non-existent source
│   │   ├── completeness.py          # No TODO/Placeholder in generated pages
│   │   ├── consistency.py           # Doc values match code values
│   │   ├── crossref.py              # Signal emitters have documented subscribers
│   │   └── links.py                 # Internal Markdown links resolve
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── gdscript_parser.py       # Low-level GDScript parsing primitives
│   │   ├── locale_map.py            # Locale key resolver
│   │   ├── markdown_gen.py          # Markdown generation helpers
│   │   └── manual_preserve.py       # MANUAL:START/END block preservation
│   │
│   ├── gate.sh                      # Build verification gate
│   └── gate.ps1                     # Windows gate
│
├── extracted/                       # Intermediate extraction results (JSON)
│   ├── manifest.json                # What exists in the game repo
│   ├── constants.json               # All extracted constants
│   ├── systems.json                 # All system metadata
│   ├── formulas.json                # All extracted formulas
│   ├── references.json              # Cross-file reference graph
│   ├── signals.json                 # Signal definitions + emitters/subscribers
│   ├── data_files.json              # Parsed data file contents
│   ├── locale.json                  # All locale keys and texts
│   └── verification_report.json     # Last verification results
│
├── content/                         # Generated Markdown (MkDocs source)
│   ├── index.md                     # Auto-generated overview with stats
│   ├── config-reference.md          # All GameConfig constants
│   ├── systems/                     # One page per discovered system
│   │   └── _index.md                # Execution order + architecture diagram
│   ├── data/                        # One page per discovered data file
│   │   └── _index.md                # Data file inventory
│   ├── interactions/                # One page per discovered interaction pair
│   │   └── _index.md                # Master dependency graph
│   ├── glossary/                    # One page per locale file category
│   │   └── _index.md                # Master glossary
│   ├── core/                        # One page per core module
│   │   └── _index.md                # Core modules overview
│   └── _manual/                     # Hand-written pages (never overwritten)
│
├── exports/                         # LLM context files
│   ├── worldsim-full.md
│   ├── worldsim-systems.md
│   ├── worldsim-data.md
│   └── worldsim-interactions.md
│
└── .github/
    └── workflows/
        └── deploy.yml               # GitHub Pages deploy on push
```

## Pipeline Configuration (scripts/config.py)

```python
import os

# Source repository path (read-only)
SOURCE_REPO = os.environ.get("WORLDSIM_SOURCE", os.path.join(os.path.dirname(__file__), "..", "..", "new-world"))

# Output directories (within this repo)
EXTRACTED_DIR = "extracted"
CONTENT_DIR = "content"
EXPORTS_DIR = "exports"

# Discovery patterns
SYSTEM_GLOB = "scripts/systems/*.gd"
CORE_GLOB = "scripts/core/*.gd"
AI_GLOB = "scripts/ai/*.gd"
DATA_GLOB = "data/**/*.json"
LOCALE_GLOB = "localization/**/*.json"

# Export size limits
EXPORT_MAX_BYTES = 150_000  # 150KB warning threshold
EXPORT_TARGET_BYTES = 100_000  # 100KB target

# Verification thresholds
COVERAGE_MIN_PERCENT = 95  # Fail if <95% of source files documented
```

## manifest.json Schema

```json
{
  "generated_at": "2026-02-18T12:00:00Z",
  "source_repo": "../new-world",
  "source_commit": "abc123...",
  "systems": [
    {
      "file": "scripts/systems/emotion_system.gd",
      "system_name": "emotions",
      "priority": 32,
      "tick_interval": 12,
      "description": "Plutchik 8-emotion update engine...",
      "imports": ["res://scripts/core/emotion_data.gd"],
      "signals_emitted": [],
      "signals_connected": [],
      "config_refs": ["GameConfig.TICKS_PER_YEAR"],
      "entity_fields": ["emotion_data", "personality"],
      "species_refs": ["SpeciesManager.decay_parameters"]
    }
  ],
  "core_modules": [...],
  "ai_modules": [...],
  "data_files": [
    {
      "file": "data/species/human/mortality/siler_parameters.json",
      "category": "species/human/mortality",
      "keys_count": 27,
      "top_level_keys": ["model", "comment", "baseline", "tech_modifiers", ...]
    }
  ],
  "locale_files": [
    {
      "file": "localization/ko/emotions.json",
      "lang": "ko",
      "category": "emotions",
      "keys_count": 58
    }
  ],
  "locale_categories": ["buildings", "deaths", "emotions", "events", "game", "traits", "tutorial", "ui"],
  "signals": {
    "entity_born": { "params": "entity_id: int, entity_name: String, parent_ids: Array, tick: int", "emitters": ["family_system.gd"], "subscribers": [] }
  },
  "stats": {
    "total_gd_files": 67,
    "total_json_files": 18,
    "total_locale_keys": 1372,
    "total_lines_gd": 15347
  }
}
```

---

## Worktree Rules

| Worktree | Purpose | Agent |
|----------|---------|-------|
| `worldsim-docs-wt/lead` | Pipeline architecture, integration, config | Claude Code |
| `worldsim-docs-wt/t-<id>-<slug>` | Individual extractor/generator/verifier tickets | Codex (via ask_codex) |

## Codex Dispatch Rules

Same as game repo. Default is **DISPATCH** via `ask_codex`.

Direct implementation only for:
1. `scripts/extract_all.py` orchestration wiring
2. `scripts/config.py` shared configuration
3. `mkdocs.yml` static config sections (theme, extensions — NOT nav)
4. Cross-module integration (<50 lines)

Target dispatch ratio: ≥60%.

---

## Autopilot Workflow

When the user gives a task:

1. **Plan** — Split into extractor/generator/verifier tickets
2. **Sequence** — Extractors → Generators → Verifiers → Integration
3. **Classify** — 🟢 DISPATCH (individual modules) vs 🔴 DIRECT (orchestration wiring)
4. **Log PROGRESS.md**
5. **Dispatch** via `ask_codex`
6. **Gate** — `bash scripts/gate.sh`

---

## Ticket Structure for This Repo

```markdown
## Objective
[What this module does in the pipeline]

## Pipeline Phase
[Phase 1: DISCOVER | Phase 2: EXTRACT | Phase 3: GENERATE | Phase 4: EXPORT | Phase 5: VERIFY]

## Input
[What files/data this module reads — manifests, extracted JSON, source .gd/.json]

## Output
[What files this module produces — extracted JSON, content .md, verification report]

## Interface Contract
[Function signatures, expected dict keys, file format]

## Scope
Files to create/modify:
- scripts/extractors/xxx.py
- (tests if applicable)

## Non-goals
[What this ticket does NOT do]

## Acceptance Criteria
- [ ] Output matches expected format
- [ ] Handles missing/malformed input gracefully
- [ ] Korean text preserved in UTF-8
- [ ] Gate passes
```

---

## Quality Standards

### Extraction accuracy
- Constants: values must be character-for-character identical to source
- Formulas: must reflect actual GDScript logic, not just comments
- If comment says X but code does Y, document Y and flag discrepancy

### Autodiscovery
- No hardcoded file lists anywhere in the pipeline
- All file discovery uses glob patterns from config.py
- New files in the game repo are picked up on next run automatically

### Verification
- Phase 5 is mandatory — pipeline fails if critical checks fail
- Every generated page must trace to a source file
- Every source file must have a generated page (or be in an explicit ignore list with reason)

### Encoding
- All file I/O: explicit `encoding='utf-8'`
- Korean text must render correctly in Markdown output

### Idempotency
- Running extract_all.py twice produces identical output
- Manual content between MANUAL markers is preserved across runs

---

## Common Mistakes to Avoid

1. **Hardcoding system/file lists** — Use glob discovery. Always.
2. **Writing to source repo** — `../new-world/` is READ ONLY.
3. **Generating mkdocs.yml nav manually** — nav is ALWAYS auto-generated from content/.
4. **Creating placeholder pages** — Pages come from extraction or don't exist.
5. **Skipping Phase 5 verification** — It catches real bugs. Never skip.
6. **Assuming file structure** — The game repo structure will change. Handle gracefully.
7. **Parsing comments instead of code** — Comments may be stale. Code is truth.
8. **Breaking Korean encoding** — Explicit UTF-8 everywhere.
9. **Oversized exports** — Monitor sizes. Summarize when needed.
10. **Not preserving MANUAL blocks** — Check for markers before overwriting any .md file.
