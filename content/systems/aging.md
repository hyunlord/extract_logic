---
title: "Aging System"
description: "Checks age stage transitions, emits growth notifications, and applies yearly personality maturation."
generated: true
source_files:
  - "scripts/systems/age_system.gd"
nav_order: 48
---

# Aging System

> Checks age stage transitions, emits growth notifications, and applies yearly personality maturation. Runs every 50 ticks (~4 days).

📄 source: `scripts/systems/age_system.gd` | Priority: 48 | Tick interval: 50

## Overview

Checks age stage transitions, emits growth notifications, and applies yearly personality maturation. Runs every 50 ticks (~4 days).

The extractor found 4 functions, 3 configuration references, and 6 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `TICKS_PER_YEAR` | 4380 | from GameConfig |
| `get_age_stage` | - | GameConfig function reference |
| `get_age_years` | - | GameConfig function reference |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `age` | read | Age or stage lifecycle state. |
| `age_stage` | read | Age or stage lifecycle state. |
| `entity_name` | read | entity name |
| `id` | read | Entity identity reference. |
| `job` | read | job |
| `personality` | read | Personality and trait state. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 13-18 (6 lines)

### `init(entity_manager: RefCounted, rng: RandomNumberGenerator = null)`

**Parameters**: `entity_manager: RefCounted, rng: RandomNumberGenerator = null`
**Lines**: 19-25 (7 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 26-41 (16 lines)

### `_on_stage_changed(entity: RefCounted, old_stage: String, new_stage: String, tick: int)`

**Parameters**: `entity: RefCounted, old_stage: String, new_stage: String, tick: int`
**Lines**: 42-64 (23 lines)

## Formulas

No formulas extracted for this module.

## Dependencies

### Imports

- [`personality_maturation.gd`](personality_maturation.md) - via `preload` (line 7)

### Signals Emitted

- `ui_notification` - parameters: `message: String, type: String` (line 54)
- `ui_notification` - parameters: `message: String, type: String` (line 57)
- `ui_notification` - parameters: `message: String, type: String` (line 60)

### Referenced By

- None
