---
title: "Migration System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/migration_system.gd"
nav_order: 60
---

# Migration System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/migration_system.gd` | Priority: 60 | Tick interval: config (GameConfig.MIGRATION_TICK_INTERVAL)

## Overview

This page summarizes the extracted structure and runtime behavior for `Migration`.

The extractor found 13 functions, 14 configuration references, and 7 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `MAX_SETTLEMENTS` | 5 | from GameConfig |
| `MIGRATION_CHANCE` | 0.05 | from GameConfig |
| `MIGRATION_COOLDOWN_TICKS` | 500 | from GameConfig |
| `MIGRATION_GROUP_SIZE_MAX` | 7 | from GameConfig |
| `MIGRATION_GROUP_SIZE_MIN` | 5 | from GameConfig |
| `MIGRATION_MIN_POP` | 40 | from GameConfig |
| `MIGRATION_SEARCH_RADIUS_MAX` | 80 | from GameConfig |
| `MIGRATION_SEARCH_RADIUS_MIN` | 30 | from GameConfig |
| `MIGRATION_STARTUP_FOOD` | 30.0 | from GameConfig |
| `MIGRATION_STARTUP_STONE` | 3.0 | from GameConfig |
| `MIGRATION_STARTUP_WOOD` | 10.0 | from GameConfig |
| `MIGRATION_TICK_INTERVAL` | 100 | from GameConfig |
| `SETTLEMENT_CLEANUP_INTERVAL` | 250 | from GameConfig |
| `SETTLEMENT_MIN_DISTANCE` | 25 | ══════════════════════════════════════ Settlement & Migration ══════════════════════════════════════ |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `action_target` | read | Current behavior/action state. |
| `action_timer` | read | Current behavior/action state. |
| `cached_path` | read | World-space movement data. |
| `current_action` | read | Current behavior/action state. |
| `id` | read | Entity identity reference. |
| `path_index` | read | World-space movement data. |
| `settlement_id` | read | Entity identity reference. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 12-17 (6 lines)

### `init(entity_manager: RefCounted, building_manager: RefCounted, settlement_manager: RefCounted, world_data: RefCounted, resource_map: RefCounted, rng: RandomNumberGenerator)`

**Parameters**: `entity_manager: RefCounted, building_manager: RefCounted, settlement_manager: RefCounted, world_data: RefCounted, resource_map: RefCounted, rng: RandomNumberGenerator`
**Lines**: 18-26 (9 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 27-149 (123 lines)

### `_ensure_group_composition(migrants: Array, candidates: Array)`

**Parameters**: `migrants: Array, candidates: Array`
**Lines**: 150-177 (28 lines)

### `_can_withdraw_from_stockpiles(settlement_id: int, resources: Dictionary)`

**Parameters**: `settlement_id: int, resources: Dictionary`
**Lines**: 178-187 (10 lines)

### `_get_settlement_stockpile_totals(settlement_id: int)`

**Parameters**: `settlement_id: int`
**Lines**: 188-201 (14 lines)

### `_withdraw_from_stockpiles(settlement_id: int, resources: Dictionary)`

**Parameters**: `settlement_id: int, resources: Dictionary`
**Lines**: 202-219 (18 lines)

### `_distribute_startup_resources(migrants: Array, resources: Dictionary)`

**Parameters**: `migrants: Array, resources: Dictionary`
**Lines**: 220-243 (24 lines)

### `_find_migration_site(source: RefCounted, all_settlements: Array)`

**Parameters**: `source: RefCounted, all_settlements: Array`
**Lines**: 244-284 (41 lines)

### `_count_settlement_shelters(settlement_id: int)`

**Parameters**: `settlement_id: int`
**Lines**: 285-294 (10 lines)

### `_get_food_in_radius(cx: int, cy: int, radius: int)`

**Parameters**: `cx: int, cy: int, radius: int`
**Lines**: 295-308 (14 lines)

### `_get_food_score(x: int, y: int, radius: int)`

**Parameters**: `x: int, y: int, radius: int`
**Lines**: 309-322 (14 lines)

### `_sort_social_ascending(a: RefCounted, b: RefCounted)`

**Parameters**: `a: RefCounted, b: RefCounted`
**Lines**: 323-324 (2 lines)

## Formulas

### Execute Tick Line 60

Formula logic extracted from execute_tick

```gdscript
var explorer_chance: bool = _rng.randf() < GameConfig.MIGRATION_CHANCE
```

📄 source: `scripts/systems/migration_system.gd:L60`

### Find Migration Site Line 265

Formula logic extracted from _find_migration_site

$$absi(other_settlement.center_x - x) + absi(other_settlement.center_y - y)$$

```gdscript
var dist_to_settlement: int = absi(other_settlement.center_x - x) + absi(other_settlement.center_y - y)
```

📄 source: `scripts/systems/migration_system.gd:L265`

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
