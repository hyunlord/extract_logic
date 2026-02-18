---
title: "Resource Regen System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/resource_regen_system.gd"
nav_order: 5
---

# Resource Regen System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/resource_regen_system.gd` | Priority: 5 | Tick interval: config (GameConfig.RESOURCE_REGEN_TICK_INTERVAL)

## Overview

This page summarizes the extracted structure and runtime behavior for `Resource Regen`.

The extractor found 2 functions, 4 configuration references, and 0 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `FOOD_REGEN_RATE` | 1.0 | Resource regen rates (per regen tick) |
| `RESOURCE_REGEN_TICK_INTERVAL` | 120 | Resource regen tick interval (time-based, 10 days) |
| `ResourceType` | - | GameConfig function reference |
| `WOOD_REGEN_RATE` | 0.3 | from GameConfig |

## Entity Fields Accessed

No entity field access metadata extracted.

## Functions

### `init(resource_map: RefCounted, world_data: RefCounted)`

**Parameters**: `resource_map: RefCounted, world_data: RefCounted`
**Lines**: 7-14 (8 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 15-33 (19 lines)

## Formulas

No formulas extracted for this module.

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
