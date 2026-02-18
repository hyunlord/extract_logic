---
title: "Construction System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/construction_system.gd"
nav_order: 28
---

# Construction System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/construction_system.gd` | Priority: 28 | Tick interval: config (GameConfig.CONSTRUCTION_TICK_INTERVAL)

## Overview

This page summarizes the extracted structure and runtime behavior for `Construction`.

The extractor found 2 functions, 2 configuration references, and 5 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `BUILDING_TYPES` | { 	"stockpile": {"cost": {"wood": 2.0}, "build_ticks": 36, "radius": 8}, 	"shelter": {"cost": {"wood": 4.0, "stone": 1.0}, "build_ticks": 60, "radius": 0}, 	"campfire": {"cost": {"wood": 1.0}, "build_ticks": 24, "radius": 5}, } | Building type definitions |
| `CONSTRUCTION_TICK_INTERVAL` | 5 | from GameConfig |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `action_target` | read | Current behavior/action state. |
| `age_stage` | read | Age or stage lifecycle state. |
| `buildings_built` | read | buildings built |
| `current_action` | read | Current behavior/action state. |
| `position` | read | World-space movement data. |

## Functions

### `init(entity_manager: RefCounted, building_manager: RefCounted)`

**Parameters**: `entity_manager: RefCounted, building_manager: RefCounted`
**Lines**: 7-14 (8 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 15-57 (43 lines)

## Formulas

No formulas extracted for this module.

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
