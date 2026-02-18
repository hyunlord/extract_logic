---
title: "Childcare System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/childcare_system.gd"
nav_order: 8
---

# Childcare System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/childcare_system.gd` | Priority: 8 | Tick interval: 2

## Overview

This page summarizes the extracted structure and runtime behavior for `Childcare`.

The extractor found 6 functions, 3 configuration references, and 2 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `CHILDCARE_FEED_AMOUNTS` | { 	"infant": 0.40, 	"toddler": 0.50, 	"child": 0.50, 	"teen": 0.60, } | Feed amounts per childcare tick (food units from stockpile) |
| `CHILDCARE_HUNGER_THRESHOLDS` | { 	"infant": 0.85, 	"toddler": 0.80, 	"child": 0.75, 	"teen": 0.70, } | Per-stage hunger threshold for childcare feeding (higher = feed sooner) |
| `FOOD_HUNGER_RESTORE` | 0.3 | Eating constants |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `age_stage` | read | Age or stage lifecycle state. |
| `hunger` | read | Hunger/food state. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 10-15 (6 lines)

### `init(entity_manager: RefCounted, building_manager: RefCounted, settlement_manager: RefCounted)`

**Parameters**: `entity_manager: RefCounted, building_manager: RefCounted, settlement_manager: RefCounted`
**Lines**: 16-21 (6 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 22-79 (58 lines)

### `_get_settlement_food(settlement_id: int)`

**Parameters**: `settlement_id: int`
**Lines**: 80-90 (11 lines)

### `_withdraw_food(settlement_id: int, amount: float)`

**Parameters**: `settlement_id: int, amount: float`
**Lines**: 91-113 (23 lines)

### `_sort_hunger_ascending(a: RefCounted, b: RefCounted)`

**Parameters**: `a: RefCounted, b: RefCounted`
**Lines**: 114-115 (2 lines)

## Formulas

No formulas extracted for this module.

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
