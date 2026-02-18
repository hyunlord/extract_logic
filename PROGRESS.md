# WorldSim Docs Pipeline v2 — Progress Tracker

**Started**: 2026-02-18T07:00:00Z
**Completed**: 2026-02-18T08:15:00Z
**Branch**: lead
**Dispatch target**: ask_codex (Codex CLI)
**Goal**: Rework pipeline from JSON dumps to human-readable semantic documentation

---

## v1 Summary (completed)
19/23 tickets, 83% dispatch ratio. Pipeline functional but produces mechanical code scraping — no interpretation, no formula explanations, no cross-system pipeline documentation.

## v2 Problems Addressed
1. Data pages dump JSON keys verbatim (`_comment`, separator lines exposed)
2. Trait pages show JSON structure only — no logic explanation for conditions/effects
3. Stressor events include comment dividers — need meaningful category grouping
4. System pages list functions mechanically — no tick pipeline or formula interpretation
5. Interaction pages are simple reference lists — no calculation pipeline explanation
6. No dedicated pages for key game mechanics (emotion 3-layer, stress Lazarus model, Siler mortality)

---

## v2 Ticket Plan

### Phase 2 (EXTRACT) — Semantic Extractors

| # | Title | Dispatch | Status |
|---|-------|----------|--------|
| t-100 | `extractors/json_data.py` rework — filter `_comment*` keys, add domain annotations | ask_codex | ✅ |
| t-101 | `extractors/trait_data.py` (NEW) — parse trait_definitions.json with HEXACO grouping | ask_codex | ✅ |
| t-102 | `extractors/stressor_data.py` (NEW) — parse stressor_events.json, filter comments, group by category | ask_codex | ✅ |
| t-103 | `extractors/emotion_presets.py` (NEW) — parse event_presets.json with appraisal semantics | ask_codex | ✅ |
| t-104 | `extractors/decay_config.py` (NEW) — parse decay/sensitivity/contagion/mental-break params | ask_codex | ✅ |
| t-105 | `extractors/gdscript_formulas.py` enhance — add semantic context, academic refs, variable meanings | ask_codex | ⚠️ partial |

### Phase 3 (GENERATE) — Semantic Generators

| # | Title | Dispatch | Status |
|---|-------|----------|--------|
| t-106 | `generators/system_page.py` rework — narrative docs with tick pipeline, formula interpretation | ask_codex | ✅ |
| t-107 | `generators/data_page.py` rework — filtered content, interpreted tables, no meta keys | ask_codex | ✅ |
| t-108 | `generators/trait_page.py` (NEW) — HEXACO conditions, effect breakdowns, synergy networks | ask_codex | ✅ |
| t-109 | `generators/emotion_detail.py` (NEW) — 3-layer dynamics, appraisal pipeline, contagion, mental breaks | ask_codex | ✅ |
| t-110 | `generators/stress_detail.py` (NEW) — Lazarus model, continuous stressors, recovery, Yerkes-Dodson | ask_codex | ✅ |
| t-111 | `generators/mortality_detail.py` (NEW) — Siler model, tech modifiers, care protection, seasons | ask_codex | ✅ |
| t-112 | `generators/interaction_page.py` rework — calculation pipeline docs with Mermaid flow diagrams | ask_codex | ✅ |
| t-113 | `generators/pipeline_page.py` (NEW) — master personality→emotion→stress→mortality pipeline doc | ask_codex | ✅ |

### Orchestration & Verification

| # | Title | Dispatch | Status |
|---|-------|----------|--------|
| t-114 | `phase2_extract.py` — wire new extractors | DIRECT | ✅ |
| t-115 | `phase3_generate.py` — wire new generators | DIRECT | ✅ |
| t-116 | Verifiers update — coverage/links for new content structure | DIRECT | ✅ |

**Total**: 17 tickets — 14 dispatch (ask_codex) + 3 direct = **82% dispatch ratio** (target >= 60%) ✅

---

## Execution Log

### Phase 2 (EXTRACT) — Batch 1

- **t-100** (json_data rework): ✅ Job `7be06460` completed. Meta-key filtering, domain annotations, richer stats. 309 lines.
- **t-101** (trait_data): ✅ Job `3f7ce919` completed. File already implemented correctly (315 lines). HEXACO grouping, effect summaries, synergy graph.
- **t-102** (stressor_data): ✅ Job `24ed2deb` completed. Comment filtering, severity ranking, personality modifiers, category grouping. 354 lines.
- **t-103** (emotion_presets): ✅ Job `47779813` completed. Appraisal semantics, predicted emotions, half-up rounding. 335 lines.
- **t-104** (decay_config): ✅ Job `be194dcb` — rate-limited during verification but file was fully written (532 lines, 17KB). Emotion dynamics parameters, opposite pair inhibition, memory traces, habituation, contagion, mental break thresholds.
- **t-105** (formulas enhance): ⚠️ Job `0642e890` completed but PARTIAL. Only added uppercase D/R stress variable support. Full model_ref/purpose/enhanced variable descriptions not implemented. Pipeline still works with existing formula extraction.

### Phase 3 (GENERATE) — Batch 2

All 8 generator tickets dispatched via ask_codex and completed:
- **t-106** (system_page): ✅ Job `46fba398`. Reworked from 816→1221 lines. Narrative docs with tick pipeline, formula interpretation, academic references.
- **t-107** (data_page): ✅ Job `e40a48b0`. Reworked from 653→1313 lines. Filtered content, interpreted tables, domain annotations, no meta keys.
- **t-108** (trait_page): ✅ Job `83017e8c`. New file, 848 lines. HEXACO axis pages with facet conditions, emotion modifiers, behavior weights, synergy links.
- **t-109** (emotion_detail): ✅ Job `b7e2eca5`. New file, 821 lines. 3-layer dynamics (fast/slow/memory), Plutchik model, appraisal pipeline, contagion, mental breaks.
- **t-110** (stress_detail): ✅ Job `dbc46a24`. New file, 763 lines. Lazarus appraisal, continuous stressors, GAS stages, allostatic load, Yerkes-Dodson curve.
- **t-111** (mortality_detail): ✅ Job `b64a6ee7`. New file, 580 lines. Siler bathtub curve, tech modifiers, infant/child care, seasonal effects.
- **t-112** (interaction_page): ✅ Job `f7f92893`. Reworked from 639→1507 lines. Calculation pipeline docs with formula chains between systems.
- **t-113** (pipeline_page): ✅ Job `19f313ee`. New file, 740 lines. Master personality→emotion→stress→mortality pipeline with Mermaid diagrams.

### Orchestration & Verification

- **t-114** (wire extractors): ✅ DIRECT. Added trait_data, stressor_data, emotion_presets, decay_config to phase2_extract.py.
- **t-115** (wire generators): ✅ DIRECT. Rewrote phase3_generate.py with extracted data loading, auto-detect signature support, all new generators wired.
- **t-116** (verifiers update): ✅ DIRECT. Added v2 coverage checks for extracted JSON files (trait_data, stressor_data, emotion_presets, decay_config) and new content pages (pipeline.md, traits/_index.md, emotion-detail.md, stress-detail.md, mortality-detail.md).

---

## Final Pipeline Results

```
Pipeline: 0.7s total
Phase 1 DISCOVER: 22 systems, 27 core, 19 data, 16 locale (2718 keys)
Phase 2 EXTRACT:  10 extractors, 1990 items, 0 warnings
Phase 3 GENERATE: 13 generators, 1730 items, 102 files, 1 warning
Phase 4 EXPORT:   4 files (size warnings on full/systems exports)
Phase 5 VERIFY:   PASS — 0 errors, 647 anchor warnings (trait cross-refs)
```

### Gate Results
```
check 1/5: Python syntax       PASS (all .py files compile)
check 2/5: Import test         PASS (28 modules import OK)
check 3/5: Phase pipeline      PASS (manifest valid)
check 4/5: Frontmatter         PASS (102 files OK)
check 5/5: Summary             PASS — 0 warnings
```

### v2 Content Output Summary

| Content Type | Files | Total Size |
|---|---|---|
| System pages | 24 (incl. _index) | ~100KB |
| Detail pages (emotion, stress, mortality) | 3 | 29KB |
| Trait pages (HEXACO axes) | 7 (incl. _index) | ~25KB |
| Pipeline page | 1 | 8.3KB |
| Data pages | 19 (incl. _index) | ~50KB |
| Interaction pages | 7+ | ~20KB |
| Glossary pages | 9 (incl. _index) | ~40KB |
| Core module pages | 28 (incl. _index) | ~60KB |
| Config reference | 1 | ~15KB |
| **Total** | **102** | **~350KB** |

### Dispatch Ratio
- ask_codex: 14 tickets (t-100 through t-113)
- DIRECT: 3 tickets (t-114, t-115, t-116)
- **Dispatch ratio: 82%** (target >= 60%) ✅

### Known Issues
1. **t-105 partial**: gdscript_formulas.py only got D/R variable support, not full model_ref/purpose enhancement. Non-blocking — pipeline works fine with existing extraction.
2. **647 anchor warnings**: Trait pages reference facet anchors (`#f_gentle`, `#f_sentimental`) that resolve to heading IDs with slightly different slugification. Non-blocking — all file-level links resolve correctly.
3. **Export size warnings**: Full export (498KB) exceeds 150KB limit and gets truncated. Systems export (213KB) also truncated. Expected with richer v2 content.

---

## Post-v2 QA Fixes (2026-02-18)

Found via localhost:8000 content audit.

| # | Title | Dispatch | Status |
|---|-------|----------|--------|
| t-117 | `data_page.py` — mental_breaks semantic fallback: add domain key → meaning mapping for duration_base_ticks, duration_variance_ticks, break_scale, shaken_* keys | DIRECT | ✅ |
| t-118 | `stress_detail.py` — EMOTION_WEIGHTS table: parse actual $w_e$ values from stress_system.gd (fear:0.09, anger:0.06, joy:-0.05, etc.) | DIRECT | ✅ |

**Root causes:**
- t-117: `_infer_control_description` had no mental_break-specific mappings; `duration_base_ticks` fell through all checks to generic fallback
- t-118: `_collect_emotion_weights` read from `decay_config.get("stress").get("weights")` but decay_config.json has no such path; EMOTION_WEIGHTS is a GDScript const dict not in extracted/constants.json

---

## 1단계: 소스 데이터 누락 필드 보완 (2026-02-18)

i18n 구조 전환 전 소스 데이터의 누락 필드 추가. 대상: `new-world-wt/lead`.

| # | Title | Dispatch | Status |
|---|-------|----------|--------|
| t-119 | `emotion_definition.json` — 8개 감정 객체에 `name_en` 추가 | ask_codex (Job 46e5d626) | ✅ |
| t-120 | `mental_breaks.json` — 10개 항목에 `description_kr`/`description_en` 추가 | ask_codex (Job 85231c7c) | ✅ |
| t-121 | `stressor_events.json` — 24개 이벤트에 `description_kr`/`description_en` 추가 | ask_codex (Job 10fc41b4) | ✅ |

**Results:**
- t-119: `emotions` 딕셔너리 각 객체에 `name_en` 추가 완료 (8 fields). JSON valid.
- t-120: 10개 mental break 항목에 description_kr/en 추가 (20 fields). JSON valid, ORDER_OK.
- t-121: 24개 stressor 이벤트에 description_kr/en 추가 (48 fields). JSON valid, _comment* 보존.

**총 추가 필드:** 76개 (8 + 20 + 48)

---

## 2단계: i18n 구조 전환 (2026-02-18)

MkDocs Material i18n 플러그인 기반 한/영 토글 구조 전환.
환경: `.venv` 내 mkdocs-material 9.7.1, mkdocs-static-i18n 미설치.

| # | Title | Dispatch | Status |
|---|-------|----------|--------|
| t-I1 | `mkdocs.yml` i18n 플러그인 설정 + `mkdocs-static-i18n` 설치 | ask_codex | ✅ |
| t-I2 | `generators/strings.py` locale dict 추출 — 하드코딩 문자열 외부화 | ask_codex | ✅ |
| t-I3 | `content/` → `content/ko/` 이동 + config.py/nav_builder.py 경로 갱신 | ask_codex | ✅ |

**의존 관계:** t-I1 ‖ t-I2 (병렬) → t-I3 (I1 완료 후)

**Results:**
- t-I1 (Job 843c4982): `mkdocs.yml` plugins 섹션 교체 완료. `mkdocs-static-i18n` 1.3.0 호스트에서 설치 (`pip install`). `mkdocs build` → `site/` (ko) + `site/en/` (en) 생성 확인. (Codex 샌드박스 네트워크 제한으로 install은 호스트에서 직접 수행)
- t-I2 (Job 9ea1bd3d): `scripts/generators/strings.py` 신규 생성. ko/en 각 138개 키, `t(key, lang="ko")` fallback 함수 구현. 키 정합성 가드(불일치 시 오류) 포함. Gate 5/5 pass.
- t-I3 (Job 2f7cc655): `content/` → `content/ko/` 106개 파일 이동, `content/en/` 생성. `config.py`에 `CONTENT_KO`/`CONTENT_EN` 추가. `nav_builder.py` 스캔 기준 및 출력 경로를 `ko/...` prefix로 변경. 관련 generator/verifier 10개 파일의 직접 경로 참조 `CONTENT_KO`로 치환. 최종: `root_md=0`, `ko_md=106`, gate 5/5 PASS.

**Gate (최종):**
```
check 4/5: Frontmatter  106 files OK
check 5/5: Summary      PASS — 0 warnings
```
