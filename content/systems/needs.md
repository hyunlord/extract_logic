---
title: "Needs System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/needs_system.gd"
nav_order: 10
---

# Needs System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/needs_system.gd` | Priority: 10 | Tick interval: config (GameConfig.NEEDS_TICK_INTERVAL)

## Overview

This page summarizes the extracted structure and runtime behavior for `Needs`.

The extractor found 5 functions, 13 configuration references, and 13 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `CHILD_HUNGER_DECAY_MULT` | { 	"infant": 0.15, 	"toddler": 0.25, 	"child": 0.35, 	"teen": 0.70, } | Hunger decay multiplier by age stage (applied in NeedsSystem) WHO: infant caloric need is 30-50% of adult |
| `CHILD_STARVATION_GRACE_TICKS` | { 	"infant": 50, 	"toddler": 40, 	"child": 30, 	"teen": 20, } | Child-specific starvation grace ticks (longer than adult STARVATION_GRACE_TICKS=25) Academic basis: Gurven & Kaplan 2007, Pontzer 2018 — child starvation rare in forager societies |
| `ENERGY_ACTION_COST` | 0.005 | from GameConfig |
| `ENERGY_DECAY_RATE` | 0.003 | from GameConfig |
| `FOOD_HUNGER_RESTORE` | 0.3 | Eating constants |
| `HUNGER_DECAY_RATE` | 0.002 | Entity need decay rates (per needs tick, adjusted for TICK_HOURS=2) |
| `HUNGER_EAT_THRESHOLD` | 0.5 | from GameConfig |
| `HUNGER_METABOLIC_MIN` | 0.3 | Metabolic curve: hunger decays slower when already hungry (Keys et al. 1950) |
| `HUNGER_METABOLIC_RANGE` | 0.7 | from GameConfig |
| `NEEDS_TICK_INTERVAL` | 2 | System tick intervals |
| `SOCIAL_DECAY_RATE` | 0.001 | from GameConfig |
| `STARVATION_GRACE_TICKS` | 25 | Starvation grace period (in NeedsSystem ticks, ~4 days) |
| `get_age_years` | - | GameConfig function reference |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `age` | read | Age or stage lifecycle state. |
| `age_stage` | read | Age or stage lifecycle state. |
| `birth_tick` | read | birth tick |
| `current_action` | read | Current behavior/action state. |
| `energy` | read | Energy or fatigue state. |
| `entity_name` | read | entity name |
| `hunger` | read | Hunger/food state. |
| `id` | read | Entity identity reference. |
| `inventory` | read | inventory |
| `remove_item` | read | remove item |
| `settlement_id` | read | Entity identity reference. |
| `social` | read | Social interaction state. |
| `starving_timer` | read | starving timer |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 8-14 (7 lines)

### `init(entity_manager: RefCounted, building_manager: RefCounted)`

Initialize with entity/building manager references

**Parameters**: `entity_manager: RefCounted, building_manager: RefCounted`
**Lines**: 15-19 (5 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 20-105 (86 lines)

### `_get_settlement_food(settlement_id: int)`

Get total food in stockpiles belonging to a settlement

**Parameters**: `settlement_id: int`
**Lines**: 106-119 (14 lines)

### `_withdraw_food(settlement_id: int, amount: float)`

Withdraw food from stockpiles belonging to a settlement

**Parameters**: `settlement_id: int, amount: float`
**Lines**: 120-139 (20 lines)

## Formulas

### Execute Tick Line 27

Decay formula logic extracted from execute_tick

$$GameConfig.HUNGER_DECAY_RATE  \cdot  hunger_mult  \cdot  metabolic_factor$$

```gdscript
entity.hunger -= GameConfig.HUNGER_DECAY_RATE * hunger_mult * metabolic_factor
		entity.energy -= GameConfig.ENERGY_DECAY_RATE
		entity.social -= GameConfig.SOCIAL_DECAY_RATE
```

📄 source: `scripts/systems/needs_system.gd:L27`

### Execute Tick Line 47

Clamp all needs

```gdscript
entity.hunger = clampf(entity.hunger, 0.0, 1.0)
```

📄 source: `scripts/systems/needs_system.gd:L47`

### Execute Tick Line 51

Formula logic extracted from execute_tick

```gdscript
entity.energy = clampf(entity.energy, 0.0, 1.0)
		entity.social = clampf(entity.social, 0.0, 1.0)
```

📄 source: `scripts/systems/needs_system.gd:L51`

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
