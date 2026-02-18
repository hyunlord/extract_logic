---
title: "Chronicle System"
description: "Chronicles significant events in the simulation for historical viewing."
generated: true
source_files:
  - "scripts/systems/chronicle_system.gd"
nav_order: 999
---

# Chronicle System

> Chronicles significant events in the simulation for historical viewing. Events are categorized by type and importance for memory management. Event type constants Memory limits Storage

📄 source: `scripts/systems/chronicle_system.gd` | Priority: n/a | Tick interval: n/a

## Overview

Chronicles significant events in the simulation for historical viewing. Events are categorized by type and importance for memory management. Event type constants Memory limits Storage

The extractor found 8 functions, 1 configuration references, and 2 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `TICKS_PER_YEAR` | 4380 | from GameConfig |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `entity_name` | read | entity name |
| `is_alive` | read | is alive |

## Functions

### `init(entity_manager: RefCounted)`

**Parameters**: `entity_manager: RefCounted`
**Lines**: 34-38 (5 lines)

### `get_world_events(filter_type: String = "", limit: int = 100)`

Get world events (newest first), optionally filtered by type

**Parameters**: `filter_type: String = "", limit: int = 100`
**Lines**: 80-92 (13 lines)

### `get_personal_events(entity_id: int)`

Get personal events for an entity

**Parameters**: `entity_id: int`
**Lines**: 93-97 (5 lines)

### `get_event_count()`

Get total event count

**Parameters**: `(none)`
**Lines**: 98-102 (5 lines)

### `prune_old_events(current_tick: int)`

Periodic memory management

**Parameters**: `current_tick: int`
**Lines**: 103-147 (45 lines)

### `_get_entity_name(entity_id: int)`

Helper: get entity name by ID

**Parameters**: `entity_id: int`
**Lines**: 148-163 (16 lines)

### `to_save_data()`

Serialize for save/load

**Parameters**: `(none)`
**Lines**: 164-171 (8 lines)

### `load_save_data(data: Dictionary)`

Load from saved data

**Parameters**: `data: Dictionary`
**Lines**: 172-174 (3 lines)

## Formulas

No formulas extracted for this module.

## Dependencies

### Imports

- [`game_calendar.gd`](../core/game_calendar.md) - via `preload` (line 6)

### Signals Emitted

- None

### Referenced By

- None
