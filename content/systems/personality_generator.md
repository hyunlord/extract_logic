---
title: "Personality Generator System"
description: "Cholesky-based HEXACO personality generator with parental inheritance, sex differences, and culture shifts."
generated: true
source_files:
  - "scripts/systems/personality_generator.gd"
nav_order: 999
---

# Personality Generator System

> Cholesky-based HEXACO personality generator with parental inheritance, sex differences, and culture shifts. No class_name - use preload("res://scripts/systems/personality_generator.gd").

📄 source: `scripts/systems/personality_generator.gd` | Priority: n/a | Tick interval: n/a

## Overview

Cholesky-based HEXACO personality generator with parental inheritance, sex differences, and culture shifts. No class_name - use preload("res://scripts/systems/personality_generator.gd").

The extractor found 5 functions, 0 configuration references, and 0 tracked entity fields.

## Configuration

No explicit `GameConfig` references extracted.

## Entity Fields Accessed

No entity field access metadata extracted.

## Functions

### `init(rng: RandomNumberGenerator)`

**Parameters**: `rng: RandomNumberGenerator`
**Lines**: 18-42 (25 lines)

### `_randfn(mean: float, std: float)`

Box-Muller transform for normal distribution (Godot 4 has no randfn)

**Parameters**: `mean: float, std: float`
**Lines**: 43-52 (10 lines)

### `_cholesky_decompose(R: Array)`

Cholesky decomposition: R = L * L^T

**Parameters**: `R: Array`
**Lines**: 53-73 (21 lines)

### `_sample_correlated_axes()`

Sample 6 correlated axis z-scores using Cholesky

**Parameters**: `(none)`
**Lines**: 74-90 (17 lines)

### `_get_culture_shift(culture_id: String, axis_id: String)`

Culture z-shift via SpeciesManager

**Parameters**: `culture_id: String, axis_id: String`
**Lines**: 148-149 (2 lines)

## Formulas

### Init Line 24

Formula logic extracted from init

```gdscript
[0.12, 1.00, -0.13, -0.08, 0.15, -0.10],
		[-0.11, -0.13, 1.00, 0.05, 0.10, 0.08],
		[0.26, -0.08, 0.05, 1.00, 0.01, 0.03],
```

📄 source: `scripts/systems/personality_generator.gd:L24`

### Box Muller Normal

Box-Muller transform for normal distribution (Godot 4 has no randfn)

```gdscript
Box-Muller transform for normal distribution (Godot 4 has no randfn)
```

📄 source: `scripts/systems/personality_generator.gd:L42`

### Randfn Line 44

Formula logic extracted from _randfn

```gdscript
var u1: float = _rng.randf()
	var u2: float = _rng.randf()
```

📄 source: `scripts/systems/personality_generator.gd:L44`

### Randfn Line 49

Formula logic extracted from _randfn

$$return mean + std  \cdot  sqrt(-2.0  \cdot  log(u1))  \cdot  cos(2.0  \cdot  PI  \cdot  u2)$$

```gdscript
return mean + std * sqrt(-2.0 * log(u1)) * cos(2.0 * PI * u2)
```

📄 source: `scripts/systems/personality_generator.gd:L49`

### Doc Line 52

Cholesky decomposition: R = L * L^T

$$L  \cdot  L^T$$

```gdscript
Cholesky decomposition: R = L * L^T
```

📄 source: `scripts/systems/personality_generator.gd:L52`

### Cholesky Decompose Line 67

Formula logic extracted from _cholesky_decompose

$$sqrt(R[i][i] - sum_val)$$

```gdscript
L[i][j] = sqrt(R[i][i] - sum_val)
```

📄 source: `scripts/systems/personality_generator.gd:L67`

### Sample Correlated Axes Line 77

Formula logic extracted from _sample_correlated_axes

```gdscript
z_indep.append(_randfn(0.0, 1.0))
```

📄 source: `scripts/systems/personality_generator.gd:L77`

### Generate Personality Line 113

Inheritance + environment noise

$$sqrt(1.0 - 0.5  \cdot  h2  \cdot  h2)$$

```gdscript
var env_factor: float = sqrt(1.0 - 0.5 * h2 * h2)
		var z_child: float = h2 * z_mid + env_factor * z_random[i]
```

📄 source: `scripts/systems/personality_generator.gd:L113`

### Generate Personality Line 135

Intra-axis facet variance from SpeciesManager (0.75 enables contradictory facet combos)

$$z_axis + _randfn(0.0, _facet_spread)$$

```gdscript
var facet_z: float = z_axis + _randfn(0.0, _facet_spread)
```

📄 source: `scripts/systems/personality_generator.gd:L135`

## Dependencies

### Imports

- [`personality_generator.gd`](personality_generator.md) - via `preload` (line 5)
- [`personality_data.gd`](../core/personality_data.md) - via `preload` (line 7)
- [`trait_system.gd`](trait.md) - via `preload` (line 8)

### Signals Emitted

- None

### Referenced By

- `scripts/core/entity_manager.gd` - depends on this module
- [`personality_generator`](personality_generator.md) - depends on this module
