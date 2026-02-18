---
title: "설정 레퍼런스 (Config Reference)"
description: "GameConfig 전체 상수, 열거형, 사전 레퍼런스"
generated: true
source_files:
  - "scripts/core/game_config.gd"
nav_order: 2
---

# GameConfig Reference

📄 source: `scripts/core/game_config.gd` (322 lines)

## 상수

### behavior

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `BEHAVIOR_TICK_INTERVAL` | 10 | `10` | behavior | `scripts/core/game_config.gd:L161` | - |

### building_effect

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `BUILDING_EFFECT_TICK_INTERVAL` | 10 | `10` | building_effect | `scripts/core/game_config.gd:L228` | - |

### childcare

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `CHILDCARE_HUNGER_THRESHOLDS` | {<br>	"infant": 0.85,<br>	"toddler": 0.80,<br>	"child": 0.75,<br>	"teen": 0.70,<br>} | `{<br>	"infant": 0.85,<br>	"toddler": 0.80,<br>	"child": 0.75,<br>	"teen": 0.70,<br>}` | childcare | `scripts/core/game_config.gd:L270` | Per-stage hunger threshold for childcare feeding (higher = feed sooner) |
| `CHILDCARE_FEED_AMOUNTS` | {<br>	"infant": 0.40,<br>	"toddler": 0.50,<br>	"child": 0.50,<br>	"teen": 0.60,<br>} | `{<br>	"infant": 0.40,<br>	"toddler": 0.50,<br>	"child": 0.50,<br>	"teen": 0.60,<br>}` | childcare | `scripts/core/game_config.gd:L278` | Feed amounts per childcare tick (food units from stockpile) |

### construction

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `CONSTRUCTION_TICK_INTERVAL` | 5 | `5` | construction | `scripts/core/game_config.gd:L227` | - |

### family

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `PREGNANCY_DURATION` | 3360 | `3360` | family | `scripts/core/game_config.gd:L29` | - |

### gathering

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `GATHERING_TICK_INTERVAL` | 3 | `3` | gathering | `scripts/core/game_config.gd:L226` | Action-based tick intervals (NOT scaled — affect agent feel) |
| `GATHER_AMOUNT` | 2.0 | `2.0` | gathering | `scripts/core/game_config.gd:L236` | - |
| `CHILD_GATHER_EFFICIENCY` | {<br>	"child": 0.4,<br>	"teen": 0.8,<br>	"elder": 0.5,<br>} | `{<br>	"child": 0.4,<br>	"teen": 0.8,<br>	"elder": 0.5,<br>}` | gathering | `scripts/core/game_config.gd:L304` | Gathering efficiency by age stage (1.0 = full adult rate) |

### job_assignment

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `JOB_RATIOS` | {<br>	"gatherer": 0.5,<br>	"lumberjack": 0.25,<br>	"builder": 0.15,<br>	"miner": 0.1,<br>} | `{<br>	"gatherer": 0.5,<br>	"lumberjack": 0.25,<br>	"builder": 0.15,<br>	"miner": 0.1,<br>}` | job_assignment | `scripts/core/game_config.gd:L218` | Job ratios (target distribution) |
| `JOB_ASSIGNMENT_TICK_INTERVAL` | 24 | `24` | job_assignment | `scripts/core/game_config.gd:L231` | Time-based tick intervals (scaled for TICK_HOURS=2) |

### migration

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `SETTLEMENT_MIN_DISTANCE` | 25 | `25` | migration | `scripts/core/game_config.gd:L247` | ══════════════════════════════════════ Settlement & Migration ══════════════════════════════════════ |
| `MIGRATION_TICK_INTERVAL` | 100 | `100` | migration | `scripts/core/game_config.gd:L250` | - |
| `MIGRATION_MIN_POP` | 40 | `40` | migration | `scripts/core/game_config.gd:L251` | - |
| `MIGRATION_GROUP_SIZE_MIN` | 5 | `5` | migration | `scripts/core/game_config.gd:L252` | - |
| `MIGRATION_GROUP_SIZE_MAX` | 7 | `7` | migration | `scripts/core/game_config.gd:L253` | - |
| `MIGRATION_CHANCE` | 0.05 | `0.05` | migration | `scripts/core/game_config.gd:L254` | - |
| `MIGRATION_SEARCH_RADIUS_MIN` | 30 | `30` | migration | `scripts/core/game_config.gd:L255` | - |
| `MIGRATION_SEARCH_RADIUS_MAX` | 80 | `80` | migration | `scripts/core/game_config.gd:L256` | - |
| `MAX_SETTLEMENTS` | 5 | `5` | migration | `scripts/core/game_config.gd:L257` | - |
| `MIGRATION_COOLDOWN_TICKS` | 500 | `500` | migration | `scripts/core/game_config.gd:L258` | - |
| `MIGRATION_STARTUP_FOOD` | 30.0 | `30.0` | migration | `scripts/core/game_config.gd:L259` | - |
| `MIGRATION_STARTUP_WOOD` | 10.0 | `10.0` | migration | `scripts/core/game_config.gd:L260` | - |
| `MIGRATION_STARTUP_STONE` | 3.0 | `3.0` | migration | `scripts/core/game_config.gd:L261` | - |
| `SETTLEMENT_CLEANUP_INTERVAL` | 250 | `250` | migration | `scripts/core/game_config.gd:L262` | - |

### movement

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `MOVEMENT_TICK_INTERVAL` | 3 | `3` | movement | `scripts/core/game_config.gd:L162` | - |
| `CHILD_MOVE_SKIP_MOD` | {<br>	"infant": 2,<br>	"toddler": 2,<br>	"child": 3,<br>	"teen": 10,<br>	"elder": 3,<br>} | `{<br>	"infant": 2,<br>	"toddler": 2,<br>	"child": 3,<br>	"teen": 10,<br>	"elder": 3,<br>}` | movement | `scripts/core/game_config.gd:L313` | Movement skip modulo by age stage (skip 1 in N ticks; higher N = faster) infant/toddler: skip every other tick → 50%, child: skip 1/3 → 70% teen: skip 1/10 → 90%, elder: skip 1/3 → 67% |

### needs

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `NEEDS_TICK_INTERVAL` | 2 | `2` | needs | `scripts/core/game_config.gd:L160` | System tick intervals |
| `HUNGER_DECAY_RATE` | 0.002 | `0.002` | needs | `scripts/core/game_config.gd:L165` | Entity need decay rates (per needs tick, adjusted for TICK_HOURS=2) |
| `HUNGER_METABOLIC_MIN` | 0.3 | `0.3` | needs | `scripts/core/game_config.gd:L167` | Metabolic curve: hunger decays slower when already hungry (Keys et al. 1950) |
| `HUNGER_METABOLIC_RANGE` | 0.7 | `0.7` | needs | `scripts/core/game_config.gd:L168` | - |
| `ENERGY_DECAY_RATE` | 0.003 | `0.003` | needs | `scripts/core/game_config.gd:L169` | - |
| `ENERGY_ACTION_COST` | 0.005 | `0.005` | needs | `scripts/core/game_config.gd:L170` | - |
| `SOCIAL_DECAY_RATE` | 0.001 | `0.001` | needs | `scripts/core/game_config.gd:L171` | - |
| `STARVATION_GRACE_TICKS` | 25 | `25` | needs | `scripts/core/game_config.gd:L174` | Starvation grace period (in NeedsSystem ticks, ~4 days) |
| `CHILD_HUNGER_DECAY_MULT` | {<br>	"infant": 0.15,<br>	"toddler": 0.25,<br>	"child": 0.35,<br>	"teen": 0.70,<br>} | `{<br>	"infant": 0.15,<br>	"toddler": 0.25,<br>	"child": 0.35,<br>	"teen": 0.70,<br>}` | needs | `scripts/core/game_config.gd:L287` | Hunger decay multiplier by age stage (applied in NeedsSystem) WHO: infant caloric need is 30-50% of adult |
| `CHILD_STARVATION_GRACE_TICKS` | {<br>	"infant": 50,<br>	"toddler": 40,<br>	"child": 30,<br>	"teen": 20,<br>} | `{<br>	"infant": 50,<br>	"toddler": 40,<br>	"child": 30,<br>	"teen": 20,<br>}` | needs | `scripts/core/game_config.gd:L296` | Child-specific starvation grace ticks (longer than adult STARVATION_GRACE_TICKS=25) Academic basis: Gurven & Kaplan 2007, Pontzer 2018 — child starvation rare in forager societies |

### population

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `MAX_ENTITIES` | 500 | `500` | population | `scripts/core/game_config.gd:L10` | - |
| `POPULATION_TICK_INTERVAL` | 30 | `30` | population | `scripts/core/game_config.gd:L232` | - |

### resource_map

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `BIOME_RESOURCES` | {<br>	Biome.GRASSLAND: {"food_min": 5.0, "food_max": 10.0, "wood_min": 0.0, "wood_max": 0.0, "stone_min": 0.0, "stone_max": 0.0},<br>	Biome.FOREST: {"food_min": 2.0, "food_max": 5.0, "wood_min": 5.0, "wood_max": 8.0, "stone_min": 0.0, "stone_max": 0.0},<br>	Biome.DENSE_FOREST: {"food_min": 0.0, "food_max": 1.0, "wood_min": 8.0, "wood_max": 12.0, "stone_min": 0.0, "stone_max": 0.0},<br>	Biome.HILL: {"food_min": 0.0, "food_max": 0.0, "wood_min": 0.0, "wood_max": 1.0, "stone_min": 3.0, "stone_max": 6.0},<br>	Biome.MOUNTAIN: {"food_min": 0.0, "food_max": 0.0, "wood_min": 0.0, "wood_max": 0.0, "stone_min": 5.0, "stone_max": 10.0},<br>	Biome.BEACH: {"food_min": 1.0, "food_max": 2.0, "wood_min": 0.0, "wood_max": 0.0, "stone_min": 0.0, "stone_max": 1.0},<br>} | `{<br>	Biome.GRASSLAND: {"food_min": 5.0, "food_max": 10.0, "wood_min": 0.0, "wood_max": 0.0, "stone_min": 0.0, "stone_max": 0.0},<br>	Biome.FOREST: {"food_min": 2.0, "food_max": 5.0, "wood_min": 5.0, "wood_max": 8.0, "stone_min": 0.0, "stone_max": 0.0},<br>	Biome.DENSE_FOREST: {"food_min": 0.0, "food_max": 1.0, "wood_min": 8.0, "wood_max": 12.0, "stone_min": 0.0, "stone_max": 0.0},<br>	Biome.HILL: {"food_min": 0.0, "food_max": 0.0, "wood_min": 0.0, "wood_max": 1.0, "stone_min": 3.0, "stone_max": 6.0},<br>	Biome.MOUNTAIN: {"food_min": 0.0, "food_max": 0.0, "wood_min": 0.0, "wood_max": 0.0, "stone_min": 5.0, "stone_max": 10.0},<br>	Biome.BEACH: {"food_min": 1.0, "food_max": 2.0, "wood_min": 0.0, "wood_max": 0.0, "stone_min": 0.0, "stone_max": 1.0},<br>}` | resource_map | `scripts/core/game_config.gd:L193` | Biome-resource mapping: biome -> {food_min, food_max, wood_min, wood_max, stone_min, stone_max} |

### resource_regen

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `FOOD_REGEN_RATE` | 1.0 | `1.0` | resource_regen | `scripts/core/game_config.gd:L203` | Resource regen rates (per regen tick) |
| `WOOD_REGEN_RATE` | 0.3 | `0.3` | resource_regen | `scripts/core/game_config.gd:L204` | - |
| `RESOURCE_REGEN_TICK_INTERVAL` | 120 | `120` | resource_regen | `scripts/core/game_config.gd:L208` | Resource regen tick interval (time-based, 10 days) |

### save_manager

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `ui_scale` | 1.0 | `1.0` | save_manager | `scripts/core/game_config.gd:L33` | UI Scale (adjustable at runtime, saved with game) |

### shared

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `TICKS_PER_YEAR` | 4380 | `4380` | age, chronicle, deceased_registry, entity_manager, family | `scripts/core/game_config.gd:L19` | - |
| `FOOD_HUNGER_RESTORE` | 0.3 | `0.3` | childcare, movement, needs | `scripts/core/game_config.gd:L177` | Eating constants |
| `HUNGER_EAT_THRESHOLD` | 0.5 | `0.5` | movement, needs | `scripts/core/game_config.gd:L178` | - |
| `BUILDING_TYPES` | {<br>	"stockpile": {"cost": {"wood": 2.0}, "build_ticks": 36, "radius": 8},<br>	"shelter": {"cost": {"wood": 4.0, "stone": 1.0}, "build_ticks": 60, "radius": 0},<br>	"campfire": {"cost": {"wood": 1.0}, "build_ticks": 24, "radius": 5},<br>} | `{<br>	"stockpile": {"cost": {"wood": 2.0}, "build_ticks": 36, "radius": 8},<br>	"shelter": {"cost": {"wood": 4.0, "stone": 1.0}, "build_ticks": 60, "radius": 0},<br>	"campfire": {"cost": {"wood": 1.0}, "build_ticks": 24, "radius": 5},<br>}` | behavior, building_effect, construction | `scripts/core/game_config.gd:L211` | Building type definitions |
| `MAX_CARRY` | 10.0 | `10.0` | entity_data, gathering | `scripts/core/game_config.gd:L235` | Entity inventory |
| `BIRTH_FOOD_COST` | 3.0 | `3.0` | family, population | `scripts/core/game_config.gd:L239` | Population |

### simulation_engine

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `TICKS_PER_SECOND` | 10 | `10` | simulation_engine | `scripts/core/game_config.gd:L9` | Simulation parameters |
| `MAX_TICKS_PER_FRAME` | 5 | `5` | simulation_engine | `scripts/core/game_config.gd:L12` | - |
| `SPEED_OPTIONS` | [1, 2, 3, 5, 10] | `[1, 2, 3, 5, 10]` | simulation_engine | `scripts/core/game_config.gd:L111` | Speed options (multipliers) |

### unreferenced

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `WORLD_SIZE` | Vector2i(256, 256) | `Vector2i(256, 256)` | - | `scripts/core/game_config.gd:L4` | World constants |
| `TILE_SIZE` | 16 | `16` | - | `scripts/core/game_config.gd:L5` | - |
| `CHUNK_SIZE` | 32 | `32` | - | `scripts/core/game_config.gd:L6` | - |
| `INITIAL_SPAWN_COUNT` | 20 | `20` | - | `scripts/core/game_config.gd:L11` | - |
| `TICK_HOURS` | 2 | `2` | - | `scripts/core/game_config.gd:L15` | Time conversion (1 tick = 2 game hours) |
| `TICKS_PER_DAY` | 12 | `12` | - | `scripts/core/game_config.gd:L16` | - |
| `DAYS_PER_YEAR` | 365 | `365` | - | `scripts/core/game_config.gd:L17` | - |
| `TICKS_PER_MONTH` | 365 | `365` | - | `scripts/core/game_config.gd:L18` | - |
| `AGE_INFANT_END` | 13140 | `13140` | - | `scripts/core/game_config.gd:L23` | Age stage thresholds (in simulation ticks) — 6 stages infant ≤2y, toddler 3-5y, child 6-11y, teen 12-14y, adult 15-55y, elder 56+ |
| `AGE_TODDLER_END` | 26280 | `26280` | - | `scripts/core/game_config.gd:L24` | - |
| `AGE_CHILD_END` | 52560 | `52560` | - | `scripts/core/game_config.gd:L25` | - |
| `AGE_TEEN_END` | 65700 | `65700` | - | `scripts/core/game_config.gd:L26` | - |
| `AGE_ADULT_END` | 245280 | `245280` | - | `scripts/core/game_config.gd:L27` | - |
| `AGE_MAX` | 525600 | `525600` | - | `scripts/core/game_config.gd:L28` | - |
| `PREGNANCY_DURATION_STDEV` | 120 | `120` | - | `scripts/core/game_config.gd:L30` | - |
| `UI_SCALE_MIN` | 0.7 | `0.7` | - | `scripts/core/game_config.gd:L34` | - |
| `UI_SCALE_MAX` | 1.5 | `1.5` | - | `scripts/core/game_config.gd:L35` | - |
| `UI_FONT_SIZES` | {<br>	"hud": 18,<br>	"hud_secondary": 15,<br>	"panel_title": 18,<br>	"panel_body": 14,<br>	"panel_hint": 13,<br>	"bar_label": 13,<br>	"popup_title": 22,<br>	"popup_heading": 16,<br>	"popup_body": 14,<br>	"popup_small": 13,<br>	"popup_close": 14,<br>	"popup_close_btn": 16,<br>	"help_title": 26,<br>	"help_section": 18,<br>	"help_body": 16,<br>	"help_footer": 14,<br>	"legend_title": 14,<br>	"legend_body": 12,<br>	"hint": 13,<br>	"toast": 15,<br>	"minimap_label": 13,<br>	"stats_title": 14,<br>	"stats_body": 12,<br>} | `{<br>	"hud": 18,<br>	"hud_secondary": 15,<br>	"panel_title": 18,<br>	"panel_body": 14,<br>	"panel_hint": 13,<br>	"bar_label": 13,<br>	"popup_title": 22,<br>	"popup_heading": 16,<br>	"popup_body": 14,<br>	"popup_small": 13,<br>	"popup_close": 14,<br>	"popup_close_btn": 16,<br>	"help_title": 26,<br>	"help_section": 18,<br>	"help_body": 16,<br>	"help_footer": 14,<br>	"legend_title": 14,<br>	"legend_body": 12,<br>	"hint": 13,<br>	"toast": 15,<br>	"minimap_label": 13,<br>	"stats_title": 14,<br>	"stats_body": 12,<br>}` | - | `scripts/core/game_config.gd:L38` | Base font sizes (multiplied by ui_scale) |
| `UI_SIZES` | {<br>	"minimap": 250,<br>	"minimap_large": 350,<br>	"mini_stats_width": 250,<br>	"mini_stats_height": 220,<br>	"select_panel_width": 320,<br>	"select_panel_height": 280,<br>	"hud_height": 34,<br>} | `{<br>	"minimap": 250,<br>	"minimap_large": 350,<br>	"mini_stats_width": 250,<br>	"mini_stats_height": 220,<br>	"select_panel_width": 320,<br>	"select_panel_height": 280,<br>	"hud_height": 34,<br>}` | - | `scripts/core/game_config.gd:L65` | Base UI element sizes (multiplied by ui_scale) |
| `BIOME_COLORS` | {<br>	Biome.DEEP_WATER: Color(0.05, 0.10, 0.35),<br>	Biome.SHALLOW_WATER: Color(0.12, 0.30, 0.55),<br>	Biome.BEACH: Color(0.85, 0.80, 0.55),<br>	Biome.GRASSLAND: Color(0.35, 0.65, 0.20),<br>	Biome.FOREST: Color(0.15, 0.45, 0.10),<br>	Biome.DENSE_FOREST: Color(0.08, 0.30, 0.05),<br>	Biome.HILL: Color(0.55, 0.50, 0.35),<br>	Biome.MOUNTAIN: Color(0.45, 0.42, 0.40),<br>	Biome.SNOW: Color(0.90, 0.92, 0.95),<br>} | `{<br>	Biome.DEEP_WATER: Color(0.05, 0.10, 0.35),<br>	Biome.SHALLOW_WATER: Color(0.12, 0.30, 0.55),<br>	Biome.BEACH: Color(0.85, 0.80, 0.55),<br>	Biome.GRASSLAND: Color(0.35, 0.65, 0.20),<br>	Biome.FOREST: Color(0.15, 0.45, 0.10),<br>	Biome.DENSE_FOREST: Color(0.08, 0.30, 0.05),<br>	Biome.HILL: Color(0.55, 0.50, 0.35),<br>	Biome.MOUNTAIN: Color(0.45, 0.42, 0.40),<br>	Biome.SNOW: Color(0.90, 0.92, 0.95),<br>}` | - | `scripts/core/game_config.gd:L127` | Biome colors |
| `CAMERA_ZOOM_MIN` | 0.25 | `0.25` | - | `scripts/core/game_config.gd:L153` | Camera settings |
| `CAMERA_ZOOM_MAX` | 4.0 | `4.0` | - | `scripts/core/game_config.gd:L154` | - |
| `CAMERA_ZOOM_STEP` | 0.1 | `0.1` | - | `scripts/core/game_config.gd:L155` | - |
| `CAMERA_PAN_SPEED` | 500.0 | `500.0` | - | `scripts/core/game_config.gd:L156` | - |
| `CAMERA_ZOOM_SPEED` | 0.15 | `0.15` | - | `scripts/core/game_config.gd:L157` | - |
| `WORLD_SEED` | 42 | `42` | - | `scripts/core/game_config.gd:L181` | World generation |
| `STONE_REGEN_RATE` | 0.0 | `0.0` | - | `scripts/core/game_config.gd:L205` | - |
| `PATHFIND_MAX_STEPS` | 200 | `200` | - | `scripts/core/game_config.gd:L242` | Pathfinding |
| `SETTLEMENT_BUILD_RADIUS` | 15 | `15` | - | `scripts/core/game_config.gd:L248` | - |
| `BUILDING_MIN_SPACING` | 2 | `2` | - | `scripts/core/game_config.gd:L249` | - |
| `CHILDCARE_TICK_INTERVAL` | 10 | `10` | - | `scripts/core/game_config.gd:L267` | ══════════════════════════════════════ Childcare & Child Development ══════════════════════════════════════ |

### world_data

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `BIOME_MOVE_COST` | {<br>	Biome.DEEP_WATER: 0.0,<br>	Biome.SHALLOW_WATER: 0.0,<br>	Biome.BEACH: 1.2,<br>	Biome.GRASSLAND: 1.0,<br>	Biome.FOREST: 1.3,<br>	Biome.DENSE_FOREST: 1.8,<br>	Biome.HILL: 1.5,<br>	Biome.MOUNTAIN: 0.0,<br>	Biome.SNOW: 2.0,<br>} | `{<br>	Biome.DEEP_WATER: 0.0,<br>	Biome.SHALLOW_WATER: 0.0,<br>	Biome.BEACH: 1.2,<br>	Biome.GRASSLAND: 1.0,<br>	Biome.FOREST: 1.3,<br>	Biome.DENSE_FOREST: 1.8,<br>	Biome.HILL: 1.5,<br>	Biome.MOUNTAIN: 0.0,<br>	Biome.SNOW: 2.0,<br>}` | world_data | `scripts/core/game_config.gd:L140` | Biome movement cost (0.0 = impassable) |

### world_generator

| Name | Value | Raw Expression | Used By | Source | Notes |
|------|------:|---------------|---------|--------|-------|
| `NOISE_OCTAVES` | 5 | `5` | world_generator | `scripts/core/game_config.gd:L182` | - |
| `ISLAND_FALLOFF` | 0.7 | `0.7` | world_generator | `scripts/core/game_config.gd:L183` | - |

## 열거형

### Biome

Biome enum

Used by: behavior, world_generator
📄 source: `scripts/core/game_config.gd:L114`

| Key | Value |
|-----|------:|
| `DEEP_WATER` | 0 |
| `SHALLOW_WATER` | 1 |
| `BEACH` | 2 |
| `GRASSLAND` | 3 |
| `FOREST` | 4 |
| `DENSE_FOREST` | 5 |
| `HILL` | 6 |
| `MOUNTAIN` | 7 |
| `SNOW` | 8 |

### ResourceType

Resource types

Used by: behavior, gathering, resource_map, resource_regen
📄 source: `scripts/core/game_config.gd:L190`

| Key | Value |
|-----|------:|
| `FOOD` | 0 |
| `WOOD` | 1 |
| `STONE` | 2 |

## 사전

### UI_FONT_SIZES

Base font sizes (multiplied by ui_scale)

Used by: -
📄 source: `scripts/core/game_config.gd:L38`
Keys: `hud`, `hud_secondary`, `panel_title`, `panel_body`, `panel_hint`, `bar_label`, `popup_title`, `popup_heading`, `popup_body`, `popup_small`, `popup_close`, `popup_close_btn`, `help_title`, `help_section`, `help_body`, `help_footer`, `legend_title`, `legend_body`, `hint`, `toast`, `minimap_label`, `stats_title`, `stats_body`

```gdscript
var UI_FONT_SIZES = {
	"hud": 18,
	"hud_secondary": 15,
	"panel_title": 18,
	"panel_body": 14,
	"panel_hint": 13,
	"bar_label": 13,
	"popup_title": 22,
	"popup_heading": 16,
	"popup_body": 14,
	"popup_small": 13,
	"popup_close": 14,
	"popup_close_btn": 16,
	"help_title": 26,
	"help_section": 18,
	"help_body": 16,
	"help_footer": 14,
	"legend_title": 14,
	"legend_body": 12,
	"hint": 13,
	"toast": 15,
	"minimap_label": 13,
	"stats_title": 14,
	"stats_body": 12,
}
```

### UI_SIZES

Base UI element sizes (multiplied by ui_scale)

Used by: -
📄 source: `scripts/core/game_config.gd:L65`
Keys: `minimap`, `minimap_large`, `mini_stats_width`, `mini_stats_height`, `select_panel_width`, `select_panel_height`, `hud_height`

```gdscript
var UI_SIZES = {
	"minimap": 250,
	"minimap_large": 350,
	"mini_stats_width": 250,
	"mini_stats_height": 220,
	"select_panel_width": 320,
	"select_panel_height": 280,
	"hud_height": 34,
}
```

### BIOME_COLORS

Biome colors

Used by: -
📄 source: `scripts/core/game_config.gd:L127`
Keys: `Biome.DEEP_WATER`, `Biome.SHALLOW_WATER`, `Biome.BEACH`, `Biome.GRASSLAND`, `Biome.FOREST`, `Biome.DENSE_FOREST`, `Biome.HILL`, `Biome.MOUNTAIN`, `Biome.SNOW`

```gdscript
var BIOME_COLORS = {
	Biome.DEEP_WATER: Color(0.05, 0.10, 0.35),
	Biome.SHALLOW_WATER: Color(0.12, 0.30, 0.55),
	Biome.BEACH: Color(0.85, 0.80, 0.55),
	Biome.GRASSLAND: Color(0.35, 0.65, 0.20),
	Biome.FOREST: Color(0.15, 0.45, 0.10),
	Biome.DENSE_FOREST: Color(0.08, 0.30, 0.05),
	Biome.HILL: Color(0.55, 0.50, 0.35),
	Biome.MOUNTAIN: Color(0.45, 0.42, 0.40),
	Biome.SNOW: Color(0.90, 0.92, 0.95),
}
```

### BIOME_MOVE_COST

Biome movement cost (0.0 = impassable)

Used by: world_data
📄 source: `scripts/core/game_config.gd:L140`
Keys: `Biome.DEEP_WATER`, `Biome.SHALLOW_WATER`, `Biome.BEACH`, `Biome.GRASSLAND`, `Biome.FOREST`, `Biome.DENSE_FOREST`, `Biome.HILL`, `Biome.MOUNTAIN`, `Biome.SNOW`

```gdscript
var BIOME_MOVE_COST = {
	Biome.DEEP_WATER: 0.0,
	Biome.SHALLOW_WATER: 0.0,
	Biome.BEACH: 1.2,
	Biome.GRASSLAND: 1.0,
	Biome.FOREST: 1.3,
	Biome.DENSE_FOREST: 1.8,
	Biome.HILL: 1.5,
	Biome.MOUNTAIN: 0.0,
	Biome.SNOW: 2.0,
}
```

### BIOME_RESOURCES

Biome-resource mapping: biome -> {food_min, food_max, wood_min, wood_max, stone_min, stone_max}

Used by: resource_map
📄 source: `scripts/core/game_config.gd:L193`
Keys: `Biome.GRASSLAND`, `Biome.FOREST`, `Biome.DENSE_FOREST`, `Biome.HILL`, `Biome.MOUNTAIN`, `Biome.BEACH`

```gdscript
var BIOME_RESOURCES = {
	Biome.GRASSLAND: {"food_min": 5.0, "food_max": 10.0, "wood_min": 0.0, "wood_max": 0.0, "stone_min": 0.0, "stone_max": 0.0},
	Biome.FOREST: {"food_min": 2.0, "food_max": 5.0, "wood_min": 5.0, "wood_max": 8.0, "stone_min": 0.0, "stone_max": 0.0},
	Biome.DENSE_FOREST: {"food_min": 0.0, "food_max": 1.0, "wood_min": 8.0, "wood_max": 12.0, "stone_min": 0.0, "stone_max": 0.0},
	Biome.HILL: {"food_min": 0.0, "food_max": 0.0, "wood_min": 0.0, "wood_max": 1.0, "stone_min": 3.0, "stone_max": 6.0},
	Biome.MOUNTAIN: {"food_min": 0.0, "food_max": 0.0, "wood_min": 0.0, "wood_max": 0.0, "stone_min": 5.0, "stone_max": 10.0},
	Biome.BEACH: {"food_min": 1.0, "food_max": 2.0, "wood_min": 0.0, "wood_max": 0.0, "stone_min": 0.0, "stone_max": 1.0},
}
```

### BUILDING_TYPES

Building type definitions

Used by: behavior, building_effect, construction
📄 source: `scripts/core/game_config.gd:L211`
Keys: `stockpile`, `shelter`, `campfire`

```gdscript
var BUILDING_TYPES = {
	"stockpile": {"cost": {"wood": 2.0}, "build_ticks": 36, "radius": 8},
	"shelter": {"cost": {"wood": 4.0, "stone": 1.0}, "build_ticks": 60, "radius": 0},
	"campfire": {"cost": {"wood": 1.0}, "build_ticks": 24, "radius": 5},
}
```

### JOB_RATIOS

Job ratios (target distribution)

Used by: job_assignment
📄 source: `scripts/core/game_config.gd:L218`
Keys: `gatherer`, `lumberjack`, `builder`, `miner`

```gdscript
var JOB_RATIOS = {
	"gatherer": 0.5,
	"lumberjack": 0.25,
	"builder": 0.15,
	"miner": 0.1,
}
```

### CHILDCARE_HUNGER_THRESHOLDS

Per-stage hunger threshold for childcare feeding (higher = feed sooner)

Used by: childcare
📄 source: `scripts/core/game_config.gd:L270`
Keys: `infant`, `toddler`, `child`, `teen`

```gdscript
var CHILDCARE_HUNGER_THRESHOLDS = {
	"infant": 0.85,
	"toddler": 0.80,
	"child": 0.75,
	"teen": 0.70,
}
```

### CHILDCARE_FEED_AMOUNTS

Feed amounts per childcare tick (food units from stockpile)

Used by: childcare
📄 source: `scripts/core/game_config.gd:L278`
Keys: `infant`, `toddler`, `child`, `teen`

```gdscript
var CHILDCARE_FEED_AMOUNTS = {
	"infant": 0.40,
	"toddler": 0.50,
	"child": 0.50,
	"teen": 0.60,
}
```

### CHILD_HUNGER_DECAY_MULT

Hunger decay multiplier by age stage (applied in NeedsSystem) WHO: infant caloric need is 30-50% of adult

Used by: needs
📄 source: `scripts/core/game_config.gd:L287`
Keys: `infant`, `toddler`, `child`, `teen`

```gdscript
var CHILD_HUNGER_DECAY_MULT = {
	"infant": 0.15,
	"toddler": 0.25,
	"child": 0.35,
	"teen": 0.70,
}
```

### CHILD_STARVATION_GRACE_TICKS

Child-specific starvation grace ticks (longer than adult STARVATION_GRACE_TICKS=25) Academic basis: Gurven & Kaplan 2007, Pontzer 2018 — child starvation rare in forager societies

Used by: needs
📄 source: `scripts/core/game_config.gd:L296`
Keys: `infant`, `toddler`, `child`, `teen`

```gdscript
var CHILD_STARVATION_GRACE_TICKS = {
	"infant": 50,
	"toddler": 40,
	"child": 30,
	"teen": 20,
}
```

### CHILD_GATHER_EFFICIENCY

Gathering efficiency by age stage (1.0 = full adult rate)

Used by: gathering
📄 source: `scripts/core/game_config.gd:L304`
Keys: `child`, `teen`, `elder`

```gdscript
var CHILD_GATHER_EFFICIENCY = {
	"child": 0.4,
	"teen": 0.8,
	"elder": 0.5,
}
```

### CHILD_MOVE_SKIP_MOD

Movement skip modulo by age stage (skip 1 in N ticks; higher N = faster) infant/toddler: skip every other tick → 50%, child: skip 1/3 → 70% teen: skip 1/10 → 90%, elder: skip 1/3 → 67%

Used by: movement
📄 source: `scripts/core/game_config.gd:L313`
Keys: `infant`, `toddler`, `child`, `teen`, `elder`

```gdscript
var CHILD_MOVE_SKIP_MOD = {
	"infant": 2,
	"toddler": 2,
	"child": 3,
	"teen": 10,
	"elder": 3,
}
```

## 유틸리티 함수

### `get_font_size(key: String)`

Returns: `int`
Used by: -
📄 source: `scripts/core/game_config.gd:L76`

### `get_ui_size(key: String)`

Returns: `int`
Used by: -
📄 source: `scripts/core/game_config.gd:L80`

### `tick_to_date(tick: int)`

Convert simulation tick to calendar date (delegates to GameCalendar)

Returns: `Dictionary`
Used by: save_manager, simulation_engine
📄 source: `scripts/core/game_config.gd:L85`

### `get_age_years(age_ticks: int)`

Convert age in ticks to years (float)

Returns: `float`
Used by: age, family, mortality, needs
📄 source: `scripts/core/game_config.gd:L91`

### `get_age_stage(age_ticks: int)`

Get age stage string from age in ticks (6 stages)

Returns: `String`
Used by: age, entity_manager
📄 source: `scripts/core/game_config.gd:L96`

<!-- MANUAL:START -->

<!-- MANUAL:END -->
