---
title: "Family System"
description: "Handles pregnancy, birth, widowhood, and maternal complications."
generated: true
source_files:
  - "scripts/systems/family_system.gd"
nav_order: 52
---

# Family System

> Handles pregnancy, birth, widowhood, and maternal complications. Gaussian gestation duration with preterm birth mechanics (T-2000).

📄 source: `scripts/systems/family_system.gd` | Priority: 52 | Tick interval: 365

## Overview

Handles pregnancy, birth, widowhood, and maternal complications. Gaussian gestation duration with preterm birth mechanics (T-2000).

The extractor found 14 functions, 4 configuration references, and 13 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `BIRTH_FOOD_COST` | 3.0 | Population |
| `PREGNANCY_DURATION` | 3360 | from GameConfig |
| `TICKS_PER_YEAR` | 4380 | from GameConfig |
| `get_age_years` | - | GameConfig function reference |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `age` | read | Age or stage lifecycle state. |
| `age_stage` | read | Age or stage lifecycle state. |
| `emotion_data` | read | Emotion-related state. |
| `emotions` | read | Emotion-related state. |
| `entity_name` | read | entity name |
| `gender` | read | gender |
| `hunger` | read | Hunger/food state. |
| `id` | read | Entity identity reference. |
| `is_alive` | read | is alive |
| `last_birth_tick` | read | last birth tick |
| `partner_id` | read | Entity identity reference. |
| `pregnancy_tick` | read | pregnancy tick |
| `settlement_id` | read | Entity identity reference. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 42-47 (6 lines)

### `init(entity_manager: RefCounted, relationship_manager: RefCounted, building_manager: RefCounted, settlement_manager: RefCounted, rng: RandomNumberGenerator, mortality_system: RefCounted = null)`

**Parameters**: `entity_manager: RefCounted, relationship_manager: RefCounted, building_manager: RefCounted, settlement_manager: RefCounted, rng: RandomNumberGenerator, mortality_system: RefCounted = null`
**Lines**: 48-56 (9 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 57-116 (60 lines)

### `_check_widowhood(alive: Array, tick: int)`

**Parameters**: `alive: Array, tick: int`
**Lines**: 117-141 (25 lines)

### `_check_coupling(alive: Array, tick: int)`

**Parameters**: `alive: Array, tick: int`
**Lines**: 142-203 (62 lines)

### `_shuffle_array(arr: Array)`

**Parameters**: `arr: Array`
**Lines**: 204-213 (10 lines)

### `_process_births(alive: Array, tick: int)`

**Parameters**: `alive: Array, tick: int`
**Lines**: 214-230 (17 lines)

### `_generate_gestation_days(mother_nutrition: float, mother_age_years: float)`

**Parameters**: `mother_nutrition: float, mother_age_years: float`
**Lines**: 231-245 (15 lines)

### `_give_birth(mother: RefCounted, tick: int, gestation_ticks: int)`

**Parameters**: `mother: RefCounted, tick: int, gestation_ticks: int`
**Lines**: 246-306 (61 lines)

### `_spawn_baby(mother: RefCounted, father: RefCounted, tick: int, gestation_weeks: int, mother_age_years: float, baby_idx: int)`

**Parameters**: `mother: RefCounted, father: RefCounted, tick: int, gestation_weeks: int, mother_age_years: float, baby_idx: int`
**Lines**: 307-409 (103 lines)

### `_calc_newborn_health(gestation_weeks: int, mother_nutrition: float, mother_age: float, genetics_z: float)`

**Parameters**: `gestation_weeks: int, mother_nutrition: float, mother_age: float, genetics_z: float`
**Lines**: 410-450 (41 lines)

### `_check_birth_complications(mother: RefCounted, gestation_weeks: int)`

**Parameters**: `mother: RefCounted, gestation_weeks: int`
**Lines**: 451-480 (30 lines)

### `_get_nutrition_fertility_factor(hunger: float)`

**Parameters**: `hunger: float`
**Lines**: 481-500 (20 lines)

### `_check_pregnancies(alive: Array, tick: int)`

**Parameters**: `alive: Array, tick: int`
**Lines**: 501-548 (48 lines)

## Formulas

### Doc Line 4

Gaussian gestation duration with preterm birth mechanics (T-2000).

```gdscript
Gaussian gestation duration with preterm birth mechanics (T-2000).
```

📄 source: `scripts/systems/family_system.gd:L4`

### Generate Gestation Days Line 232

Formula logic extracted from _generate_gestation_days

```gdscript
var base: float = _rng.randfn(280.0, 10.0)
```

📄 source: `scripts/systems/family_system.gd:L232`

### Give Birth Line 280

Determine number of babies (twins check)

```gdscript
var num_babies: int = 2 if _rng.randf() < TWINS_CHANCE else 1
```

📄 source: `scripts/systems/family_system.gd:L280`

### Spawn Baby Line 334

Calculate newborn health → frailty

```gdscript
var mother_nutrition: float = clampf(mother.hunger, 0.0, 1.0)
```

📄 source: `scripts/systems/family_system.gd:L334`

### Spawn Baby Line 336

Formula logic extracted from _spawn_baby

```gdscript
child.frailty = lerpf(2.0, 0.8, health)
```

📄 source: `scripts/systems/family_system.gd:L336`

### Calc Newborn Health Line 414

Formula logic extracted from _calc_newborn_health

$$lerpf(35.0, 24.0, tech / 10.0)$$

```gdscript
var w50: float = lerpf(35.0, 24.0, tech / 10.0)
	var survival_base: float = 1.0 / (1.0 + exp(-(float(gestation_weeks) - w50) / 2.0))
```

📄 source: `scripts/systems/family_system.gd:L414`

### Calc Newborn Health Damage

Formula logic extracted from _calc_newborn_health

$$lerpf(0.9, 0.3, tech / 10.0)$$

```gdscript
damage = lerpf(0.9, 0.3, tech / 10.0)
```

📄 source: `scripts/systems/family_system.gd:L420`

### Calc Newborn Health Damage

Formula logic extracted from _calc_newborn_health

$$lerpf(0.5, 0.1, tech / 10.0)$$

```gdscript
damage = lerpf(0.5, 0.1, tech / 10.0)
```

📄 source: `scripts/systems/family_system.gd:L422`

### Calc Newborn Health Damage

Formula logic extracted from _calc_newborn_health

$$lerpf(0.2, 0.02, tech / 10.0)$$

```gdscript
damage = lerpf(0.2, 0.02, tech / 10.0)
```

📄 source: `scripts/systems/family_system.gd:L424`

### Calc Newborn Health Line 429

3. Maternal nutrition factor

```gdscript
var nutrition_factor: float = lerpf(0.6, 1.1, clampf(mother_nutrition, 0.0, 1.0))
```

📄 source: `scripts/systems/family_system.gd:L429`

### Calc Newborn Health Line 443

5. Genetics

```gdscript
var genetics_factor: float = clampf(genetics_z, 0.7, 1.3)
```

📄 source: `scripts/systems/family_system.gd:L443`

### Calc Newborn Health Line 445

Formula logic extracted from _calc_newborn_health

$$survival_base  \cdot  (1.0 - damage)  \cdot  nutrition_factor  \cdot  age_factor  \cdot  genetics_factor$$

```gdscript
var health: float = survival_base * (1.0 - damage) * nutrition_factor * age_factor * genetics_factor
	return clampf(health, 0.0, 1.0)
```

📄 source: `scripts/systems/family_system.gd:L445`

### Check Birth Complications Line 455

Formula logic extracted from _check_birth_complications

$$lerpf(MATERNAL_DEATH_BASE, 0.0002, tech / 10.0)$$

```gdscript
var base_risk: float = lerpf(MATERNAL_DEATH_BASE, 0.0002, tech / 10.0)
```

📄 source: `scripts/systems/family_system.gd:L455`

### Doc Line 534

Start pregnancy with Gaussian gestation duration

```gdscript
Start pregnancy with Gaussian gestation duration
```

📄 source: `scripts/systems/family_system.gd:L534`

### Check Pregnancies Line 536

Formula logic extracted from _check_pregnancies

```gdscript
var mother_nutrition: float = clampf(entity.hunger, 0.0, 1.0)
```

📄 source: `scripts/systems/family_system.gd:L536`

## Dependencies

### Imports

- [`game_calendar.gd`](../core/game_calendar.md) - via `preload` (line 6)

### Signals Emitted

- `couple_formed` - parameters: `entity_a_id: int, entity_a_name: String, entity_b_id: int, entity_b_name: String, tick: int` (line 192)
- `entity_born` - parameters: `entity_id: int, entity_name: String, parent_ids: Array, tick: int` (line 378)
- `ui_notification` - parameters: `message: String, type: String` (line 200)
- `ui_notification` - parameters: `message: String, type: String` (line 303)
- `ui_notification` - parameters: `message: String, type: String` (line 404)

### Referenced By

- None
