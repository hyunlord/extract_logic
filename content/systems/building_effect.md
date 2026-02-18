---
title: "Building Effect System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/building_effect_system.gd"
nav_order: 15
---

# Building Effect System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/building_effect_system.gd` | Priority: 15 | Tick interval: config (GameConfig.BUILDING_EFFECT_TICK_INTERVAL)

## Overview

This page summarizes the extracted structure and runtime behavior for `Building Effect`.

The extractor found 4 functions, 2 configuration references, and 2 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `BUILDING_EFFECT_TICK_INTERVAL` | 10 | from GameConfig |
| `BUILDING_TYPES` | { 	"stockpile": {"cost": {"wood": 2.0}, "build_ticks": 36, "radius": 8}, 	"shelter": {"cost": {"wood": 4.0, "stone": 1.0}, "build_ticks": 60, "radius": 0}, 	"campfire": {"cost": {"wood": 1.0}, "build_ticks": 24, "radius": 5}, } | Building type definitions |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `energy` | read | Energy or fatigue state. |
| `social` | read | Social interaction state. |

## Functions

### `init(entity_manager: RefCounted, building_manager: RefCounted, sim_engine: RefCounted)`

**Parameters**: `entity_manager: RefCounted, building_manager: RefCounted, sim_engine: RefCounted`
**Lines**: 8-16 (9 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 17-29 (13 lines)

### `_apply_campfire(building: RefCounted)`

**Parameters**: `building: RefCounted`
**Lines**: 30-43 (14 lines)

### `_apply_shelter(building: RefCounted)`

**Parameters**: `building: RefCounted`
**Lines**: 44-50 (7 lines)

## Formulas

No formulas extracted for this module.

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
