# WorldSim Docs Pipeline — Progress Tracker

**Started**: 2026-02-18T06:09:00Z
**Completed**: 2026-02-18
**Branch**: lead
**Dispatch target**: ask_codex (Codex CLI)
**Dispatch ratio**: 19/23 = 83% (target: >= 60%) ✅

---

## Ticket Plan

| # | Title | Phase | Dispatch | Status |
|---|-------|-------|----------|--------|
| t-000 | `scripts/gate.sh` — enhanced build gate | Phase 0 (GATE) | ask_codex | ✅ 완료 |
| t-001 | `scripts/extractors/gdscript_constants.py` — const/enum/dict extraction | Phase 2 (EXTRACT) | ask_codex | ✅ 완료 |
| t-002 | `scripts/extractors/gdscript_systems.py` — system logic extraction | Phase 2 (EXTRACT) | ask_codex | ✅ 완료 |
| t-003 | `scripts/extractors/gdscript_formulas.py` — math formula extraction | Phase 2 (EXTRACT) | ask_codex | ✅ 완료 |
| t-004 | `scripts/extractors/gdscript_references.py` — cross-ref graph | Phase 2 (EXTRACT) | ask_codex | ✅ 완료 |
| t-005 | `scripts/extractors/json_data.py` — JSON data parsing | Phase 2 (EXTRACT) | ask_codex | ✅ 완료 |
| t-006 | `scripts/extractors/locale.py` — localization parsing | Phase 2 (EXTRACT) | ask_codex | ✅ 완료 |
| t-007 | `scripts/phase2_extract.py` — Phase 2 orchestrator | Phase 2 (EXTRACT) | DIRECT | ✅ 완료 |
| t-008 | `scripts/generators/system_page.py` — system .md pages | Phase 3 (GENERATE) | ask_codex | ✅ 완료 |
| t-009 | `scripts/generators/data_page.py` — data .md pages | Phase 3 (GENERATE) | ask_codex | ✅ 완료 |
| t-010 | `scripts/generators/glossary_page.py` — glossary .md pages | Phase 3 (GENERATE) | ask_codex | ✅ 완료 |
| t-011 | `scripts/generators/config_reference.py` — GameConfig ref .md | Phase 3 (GENERATE) | ask_codex | ✅ 완료 |
| t-012 | `scripts/generators/interaction_page.py` — interaction .md pages | Phase 3 (GENERATE) | ask_codex | ✅ 완료 |
| t-013 | `scripts/generators/core_page.py` — core module .md pages | Phase 3 (GENERATE) | ask_codex | ✅ 완료 (+ link fix) |
| t-014 | `scripts/generators/index_page.py` — site index.md | Phase 3 (GENERATE) | ask_codex | ✅ 완료 |
| t-015 | `scripts/generators/nav_builder.py` — mkdocs.yml nav gen | Phase 3 (GENERATE) | ask_codex | ✅ 완료 |
| t-016 | `scripts/phase3_generate.py` — Phase 3 orchestrator | Phase 3 (GENERATE) | DIRECT | ✅ 완료 |
| t-017 | `scripts/phase4_export.py` — content merge to exports | Phase 4 (EXPORT) | ask_codex | ✅ 완료 |
| t-018 | `scripts/verifiers/coverage.py` — doc coverage check | Phase 5 (VERIFY) | ask_codex | ✅ 완료 |
| t-019 | `scripts/verifiers/consistency.py` — constant consistency | Phase 5 (VERIFY) | ask_codex | ✅ 완료 (+ whitespace fix) |
| t-020 | `scripts/verifiers/completeness.py` — TODO/placeholder check | Phase 5 (VERIFY) | ask_codex | ✅ 완료 |
| t-021 | `scripts/verifiers/links.py` — internal link check | Phase 5 (VERIFY) | ask_codex | ✅ 완료 |
| t-022 | `scripts/phase5_verify.py` — Phase 5 orchestrator | Phase 5 (VERIFY) | DIRECT | ✅ 완료 |

**Summary**: 23/23 tickets complete — 19 dispatched (ask_codex) + 4 direct = 83% dispatch ratio ✅

---

## Execution Log

### Phase 0 (GATE)
- **t-000**: ✅ gate.sh rewritten — 5-step validation (syntax, imports, pipeline, frontmatter, summary)

### Phase 2 (EXTRACT)
- **t-001**: ✅ gdscript_constants.py — 107 items extracted (consts, enums, dicts, functions)
- **t-002**: ✅ gdscript_systems.py — 23 systems extracted (20 systems + 1 AI + core integration)
- **t-003**: ✅ gdscript_formulas.py — 197 formulas extracted (mortality, emotion, decay, personality)
- **t-004**: ✅ gdscript_references.py — 50 reference edges (imports, signals, config refs)
- **t-005**: ✅ json_data.py — 19 data files parsed with full schema + content
- **t-006**: ✅ locale.py — 1,359 locale entries across 8 categories (ko/en)
- **t-007**: ✅ phase2_extract.py orchestrator — DIRECT implementation
- **Pipeline run**: 1,755 items, 6 files, 0 errors, 0.2s

### Phase 3 (GENERATE)
- **t-008**: ✅ system_page.py — 23 system pages with formulas, config, entity fields, dependencies
- **t-009**: ✅ data_page.py — 19 data file pages with schema + content tables
- **t-010**: ✅ glossary_page.py — 1,359 locale entries in ko/en glossary pages
- **t-011**: ✅ config_reference.py — 107 constants in single reference page
- **t-012**: ✅ interaction_page.py — 3 cross-system interaction pages from reference graph
- **t-013**: ✅ core_page.py — 27 core module pages (+ link slug fix for system page references)
- **t-014**: ✅ index_page.py — site index with live stats (86 items)
- **t-015**: ✅ nav_builder.py — mkdocs.yml nav auto-generated from 87 content pages
- **t-016**: ✅ phase3_generate.py orchestrator — DIRECT implementation
- **Pipeline run**: 1,711 items, 88 files, 0 errors, 0.1s

### Phase 4 (EXPORT)
- **t-017**: ✅ phase4_export.py — 4 export files (full, systems, data, interactions)
- **Pipeline run**: 85 items, 4 files, 5 size warnings (expected — large docs), 0.0s

### Phase 5 (VERIFY)
- **t-018**: ✅ coverage.py — all source files have doc pages
- **t-019**: ✅ consistency.py — constant values match code (+ whitespace normalization fix)
- **t-020**: ✅ completeness.py — no TODO/Placeholder markers in generated pages
- **t-021**: ✅ links.py — all internal Markdown links resolve
- **t-022**: ✅ phase5_verify.py orchestrator — DIRECT implementation
- **Pipeline run**: 488 items checked, 0 errors, 0 warnings, 0.1s

---

## Post-Dispatch Fixes (DIRECT)

1. **Consistency verifier whitespace normalization** (t-019): Multi-line dict values in constants.json had tab-indented newlines while Markdown collapsed whitespace. Added `_normalize_ws()` function to collapse whitespace/`<br>`/`\n`/`\t` before comparison. Fixed 23 false-positive mismatches.

2. **Core page link slug mismatch** (t-013): `core_page.py` generated links like `../systems/emotion_system.md` but `system_page.py` uses `system_name` field (e.g., `emotions.md`). Added `_build_system_slug_map()` to replicate system_page.py's slug logic. Fixed 5 broken internal links.

---

## Final Results

| Metric | Value |
|--------|-------|
| **Dispatch ratio** | 19/23 = 83% ✅ |
| **Total pipeline time** | 0.4s |
| **Phase 2 items** | 1,755 |
| **Phase 3 files** | 88 |
| **Phase 4 exports** | 4 |
| **Phase 5 checks** | 488 (0 errors) |
| **Gate result** | PASS (0 warnings) |
| **Verification** | ALL PASS — coverage, consistency, completeness, links |
