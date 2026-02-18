---
title: "Population System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/population_system.gd"
nav_order: 50
---

# Population System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/population_system.gd` | Priority: 50 | Tick interval: config (GameConfig.POPULATION_TICK_INTERVAL)

## Overview

This page summarizes the extracted structure and runtime behavior for `Population`.

The extractor found 6 functions, 3 configuration references, and 3 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `BIRTH_FOOD_COST` | 3.0 | Population |
| `MAX_ENTITIES` | 500 | from GameConfig |
| `POPULATION_TICK_INTERVAL` | 30 | from GameConfig |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `entity_name` | read | entity name |
| `id` | read | Entity identity reference. |
| `settlement_id` | read | Entity identity reference. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 10-15 (6 lines)

### `init(entity_manager: RefCounted, building_manager: RefCounted, world_data: RefCounted, rng: RandomNumberGenerator, settlement_manager: RefCounted = null)`

**Parameters**: `entity_manager: RefCounted, building_manager: RefCounted, world_data: RefCounted, rng: RandomNumberGenerator, settlement_manager: RefCounted = null`
**Lines**: 16-23 (8 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 24-29 (6 lines)

### `_check_births(tick: int)`

**Parameters**: `tick: int`
**Lines**: 30-108 (79 lines)

### `_log_population_status(tick: int, alive_count: int)`

**Parameters**: `tick: int, alive_count: int`
**Lines**: 109-140 (32 lines)

### `_find_walkable_near(cx: int, cy: int)`

**Parameters**: `cx: int, cy: int`
**Lines**: 141-151 (11 lines)

## Formulas

### Doc Line 26

Natural deaths disabled: handled by MortalitySystem (T-2000, Siler model)

```gdscript
Natural deaths disabled: handled by MortalitySystem (T-2000, Siler model)
```

📄 source: `scripts/systems/population_system.gd:L26`

### Doc Line 70

Food threshold: need food >= alive_count * 0.5 (lowered from 1.0 — was blocking growth at ~49)

$$alive_count  \cdot  0.5 (lowered from 1.0 — was blocking growth at ~49)$$

```gdscript
Food threshold: need food >= alive_count * 0.5 (lowered from 1.0 — was blocking growth at ~49)
```

📄 source: `scripts/systems/population_system.gd:L70`

### Doc Line 106

Old natural death logic removed — replaced by MortalitySystem (Siler model, T-2000)

```gdscript
Old natural death logic removed — replaced by MortalitySystem (Siler model, T-2000)
```

📄 source: `scripts/systems/population_system.gd:L106`

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
