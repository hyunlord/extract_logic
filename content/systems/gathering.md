---
title: "Gathering System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/gathering_system.gd"
nav_order: 25
---

# Gathering System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/gathering_system.gd` | Priority: 25 | Tick interval: config (GameConfig.GATHERING_TICK_INTERVAL)

## Overview

This page summarizes the extracted structure and runtime behavior for `Gathering`.

The extractor found 2 functions, 5 configuration references, and 9 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `CHILD_GATHER_EFFICIENCY` | { 	"child": 0.4, 	"teen": 0.8, 	"elder": 0.5, } | Gathering efficiency by age stage (1.0 = full adult rate) |
| `GATHERING_TICK_INTERVAL` | 3 | Action-based tick intervals (NOT scaled — affect agent feel) |
| `GATHER_AMOUNT` | 2.0 | from GameConfig |
| `MAX_CARRY` | 10.0 | Entity inventory |
| `ResourceType` | - | GameConfig function reference |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `add_item` | read | add item |
| `age_stage` | read | Age or stage lifecycle state. |
| `current_action` | read | Current behavior/action state. |
| `entity_name` | read | entity name |
| `get_total_carry` | read | get total carry |
| `id` | read | Entity identity reference. |
| `position` | read | World-space movement data. |
| `speed` | read | speed |
| `total_gathered` | read | total gathered |

## Functions

### `init(entity_manager: RefCounted, resource_map: RefCounted)`

**Parameters**: `entity_manager: RefCounted, resource_map: RefCounted`
**Lines**: 7-14 (8 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 15-63 (49 lines)

## Formulas

No formulas extracted for this module.

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
