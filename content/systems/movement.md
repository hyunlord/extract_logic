---
title: "Movement System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/movement_system.gd"
nav_order: 30
---

# Movement System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/movement_system.gd` | Priority: 30 | Tick interval: config (GameConfig.MOVEMENT_TICK_INTERVAL)

## Overview

This page summarizes the extracted structure and runtime behavior for `Movement`.

The extractor found 9 functions, 4 configuration references, and 14 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `CHILD_MOVE_SKIP_MOD` | { 	"infant": 2, 	"toddler": 2, 	"child": 3, 	"teen": 10, 	"elder": 3, } | Movement skip modulo by age stage (skip 1 in N ticks; higher N = faster) infant/toddler: skip every other tick → 50%, child: skip 1/3 → 70% teen: skip 1/10 → 90%, elder: skip 1/3 → 67% |
| `FOOD_HUNGER_RESTORE` | 0.3 | Eating constants |
| `HUNGER_EAT_THRESHOLD` | 0.5 | from GameConfig |
| `MOVEMENT_TICK_INTERVAL` | 3 | from GameConfig |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `action_target` | read | Current behavior/action state. |
| `action_timer` | read | Current behavior/action state. |
| `age_stage` | read | Age or stage lifecycle state. |
| `cached_path` | read | World-space movement data. |
| `current_action` | read | Current behavior/action state. |
| `energy` | read | Energy or fatigue state. |
| `entity_name` | read | entity name |
| `hunger` | read | Hunger/food state. |
| `id` | read | Entity identity reference. |
| `inventory` | read | inventory |
| `path_index` | read | World-space movement data. |
| `position` | read | World-space movement data. |
| `remove_item` | read | remove item |
| `social` | read | Social interaction state. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 9-15 (7 lines)

### `init(entity_manager: RefCounted, world_data: RefCounted, pathfinder: RefCounted = null, building_manager: RefCounted = null)`

Initialize (pathfinder and building_manager optional for backward compat)

**Parameters**: `entity_manager: RefCounted, world_data: RefCounted, pathfinder: RefCounted = null, building_manager: RefCounted = null`
**Lines**: 16-22 (7 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 23-61 (39 lines)

### `_move_with_pathfinding(entity: RefCounted, tick: int)`

**Parameters**: `entity: RefCounted, tick: int`
**Lines**: 62-106 (45 lines)

### `_move_toward_target(entity: RefCounted, tick: int)`

**Parameters**: `entity: RefCounted, tick: int`
**Lines**: 107-139 (33 lines)

### `_apply_arrival_effect(entity: RefCounted, tick: int)`

**Parameters**: `entity: RefCounted, tick: int`
**Lines**: 140-193 (54 lines)

### `_try_auto_eat(entity: RefCounted, tick: int)`

**Parameters**: `entity: RefCounted, tick: int`
**Lines**: 194-211 (18 lines)

### `_deliver_to_stockpile(entity: RefCounted, tick: int)`

**Parameters**: `entity: RefCounted, tick: int`
**Lines**: 212-241 (30 lines)

### `_take_from_stockpile(entity: RefCounted, tick: int)`

**Parameters**: `entity: RefCounted, tick: int`
**Lines**: 242-265 (24 lines)

## Formulas

### Deliver To Stockpile Line 220

Formula logic extracted from _deliver_to_stockpile

$$absi(entity.position.x - stockpile.tile_x) + absi(entity.position.y - stockpile.tile_y)$$

```gdscript
var dist: int = absi(entity.position.x - stockpile.tile_x) + absi(entity.position.y - stockpile.tile_y)
```

📄 source: `scripts/systems/movement_system.gd:L220`

### Take From Stockpile Line 250

Formula logic extracted from _take_from_stockpile

$$absi(entity.position.x - stockpile.tile_x) + absi(entity.position.y - stockpile.tile_y)$$

```gdscript
var dist: int = absi(entity.position.x - stockpile.tile_x) + absi(entity.position.y - stockpile.tile_y)
```

📄 source: `scripts/systems/movement_system.gd:L250`

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
