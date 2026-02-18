---
title: "Personality Maturation System"
description: "Age-based personality maturation using OU (Ornstein-Uhlenbeck) process."
generated: true
source_files:
  - "scripts/systems/personality_maturation.gd"
nav_order: 999
---

# Personality Maturation System

> Age-based personality maturation using OU (Ornstein-Uhlenbeck) process. Called once per game year for each entity. Ashton & Lee (2016): H increases ~+1 SD from 18→60, E/X mild increase. No class_name - use preload("res://scripts/systems/personality_maturation.gd").

📄 source: `scripts/systems/personality_maturation.gd` | Priority: n/a | Tick interval: n/a

## Overview

Age-based personality maturation using OU (Ornstein-Uhlenbeck) process. Called once per game year for each entity. Ashton & Lee (2016): H increases ~+1 SD from 18→60, E/X mild increase. No class_name - use preload("res://scripts/systems/personality_maturation.gd").

The extractor found 6 functions, 0 configuration references, and 0 tracked entity fields.

## Configuration

No explicit `GameConfig` references extracted.

## Entity Fields Accessed

No entity field access metadata extracted.

## Functions

### `init(rng: RandomNumberGenerator)`

**Parameters**: `rng: RandomNumberGenerator`
**Lines**: 17-21 (5 lines)

### `_load_maturation_parameters()`

**Parameters**: `(none)`
**Lines**: 22-30 (9 lines)

### `_randfn(mean: float, std: float)`

Box-Muller normal random

**Parameters**: `mean: float, std: float`
**Lines**: 31-40 (10 lines)

### `apply_maturation(pd: RefCounted, age: int)`

Apply one year of maturation to a PersonalityData. age: entity's current age in years (integer).

**Parameters**: `pd: RefCounted, age: int`
**Lines**: 41-61 (21 lines)

### `_get_maturation_target(axis_id: String, age: int)`

Get maturation target z-shift for axis at given age. Data-driven from SpeciesManager.personality_distribution.maturation.

**Parameters**: `axis_id: String, age: int`
**Lines**: 62-75 (14 lines)

### `_linear_target(age: int, max_shift: float, start_age: int = 18, end_age: int = 60)`

Linear maturation target: 0 at start_age, max_shift at end_age, clamped.

**Parameters**: `age: int, max_shift: float, start_age: int = 18, end_age: int = 60`
**Lines**: 76-83 (8 lines)

## Formulas

### Ornstein Uhlenbeck Update

Age-based personality maturation using OU (Ornstein-Uhlenbeck) process.

```gdscript
Age-based personality maturation using OU (Ornstein-Uhlenbeck) process.
Called once per game year for each entity.
Ashton & Lee (2016): H increases ~+1 SD from 18→60, E/X mild increase.
No class_name - use preload("res://scripts/systems/personality_maturation.gd").
```

📄 source: `scripts/systems/personality_maturation.gd:L3`

### Box Muller Normal

Box-Muller normal random

```gdscript
Box-Muller normal random
```

📄 source: `scripts/systems/personality_maturation.gd:L30`

### Randfn U1

Formula logic extracted from _randfn

```gdscript
var u1: float = _rng.randf()
	var u2: float = _rng.randf()
	if u1 < 1e-10:
		u1 = 1e-10
	return mean + std * sqrt(-2.0 * log(u1)) * cos(2.0 * PI * u2)
```

📄 source: `scripts/systems/personality_maturation.gd:L32`

### Apply Maturation Line 53

OU drift toward target + random noise.

$$_theta  \cdot  (target - current_z) + _randfn(0.0, _sigma)$$

```gdscript
var dz: float = _theta * (target - current_z) + _randfn(0.0, _sigma)
			pd.facets[fkey] = pd.from_zscore(current_z + dz)
```

📄 source: `scripts/systems/personality_maturation.gd:L53`

### Linear Target Line 82

Formula logic extracted from _linear_target

$$clampf(float(age - start_age) / span, 0.0, 1.0)$$

```gdscript
var t: float = clampf(float(age - start_age) / span, 0.0, 1.0)
	return max_shift * t
```

📄 source: `scripts/systems/personality_maturation.gd:L82`

## Dependencies

### Imports

- [`personality_maturation.gd`](personality_maturation.md) - via `preload` (line 6)
- [`personality_data.gd`](../core/personality_data.md) - via `preload` (line 8)
- [`trait_system.gd`](trait.md) - via `preload` (line 9)

### Signals Emitted

- None

### Referenced By

- [`aging`](aging.md) - depends on this module
- [`personality_maturation`](personality_maturation.md) - depends on this module
