---
title: "Personality Generator"
description: "Cholesky-based HEXACO personality generator with parental inheritance, sex differences, and culture shifts."
generated: true
source_files:
  - "scripts/systems/personality_generator.gd"
nav_order: 999
system_name: "personality_generator"
---

# Personality Generator

📄 source: `scripts/systems/personality_generator.gd` | Priority: n/a | Tick interval: n/a

## Overview (개요)

The **Personality Generator** system implements HEXACO personality framework to simulate cholesky-based HEXACO personality generator with parental inheritance, sex differences, and culture shifts.
It runs **at an unspecified cadence** at priority **n/a**.

**Core entity data**: No entity fields were extracted.

> Cholesky-based HEXACO personality generator with parental inheritance, sex differences, and culture shifts.

## Tick Pipeline (틱 파이프라인)

1. Resolve culture shift
   📄 source: `scripts/systems/personality_generator.gd:L148`

## Formulas (수식)

### Transforms personality traits into downstream modulation coefficients.

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
[0.12, 1.00, -0.13, -0.08, 0.15, -0.10],
		[-0.11, -0.13, 1.00, 0.05, 0.10, 0.08],
		[0.26, -0.08, 0.05, 1.00, 0.01, 0.03],
```

📄 source: `scripts/systems/personality_generator.gd:L24`

### Transforms personality traits into downstream modulation coefficients.

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
Box-Muller transform for normal distribution (Godot 4 has no randfn)
```

| Variable | Meaning |
| :-- | :-- |
| `transform` | transform |
| `normal` | normal |
| `has` | has |
| `no` | no |

📄 source: `scripts/systems/personality_generator.gd:L42`

### Transforms personality traits into downstream modulation coefficients.

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
var u1: float = _rng.randf()
	var u2: float = _rng.randf()
```

| Variable | Meaning |
| :-- | :-- |
| `u1` | u1 |
| `_rng` |  rng |
| `u2` | u2 |

📄 source: `scripts/systems/personality_generator.gd:L44`

### Transforms personality traits into downstream modulation coefficients.

$$
return mean + std  \cdot  sqrt(-2.0  \cdot  log(u1))  \cdot  cos(2.0  \cdot  PI  \cdot  u2)
$$

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
return mean + std * sqrt(-2.0 * log(u1)) * cos(2.0 * PI * u2)
```

| Variable | Meaning |
| :-- | :-- |
| `mean` | mean |
| `std` | std |
| `u1` | u1 |
| `u2` | u2 |

📄 source: `scripts/systems/personality_generator.gd:L49`

### Transforms personality traits into downstream modulation coefficients.

$$
L  \cdot  L^T
$$

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
Cholesky decomposition: R = L * L^T
```

| Variable | Meaning |
| :-- | :-- |
| `decomposition` | decomposition |

📄 source: `scripts/systems/personality_generator.gd:L52`

### Transforms personality traits into downstream modulation coefficients.

$$
sqrt(R[i][i] - sum_val)
$$

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
L[i][j] = sqrt(R[i][i] - sum_val)
```

| Variable | Meaning |
| :-- | :-- |
| `i` | i |
| `j` | j |
| `sum_val` | sum val |

📄 source: `scripts/systems/personality_generator.gd:L67`

### Transforms personality traits into downstream modulation coefficients.

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
z_indep.append(_randfn(0.0, 1.0))
```

| Variable | Meaning |
| :-- | :-- |
| `z_indep` | z indep |

📄 source: `scripts/systems/personality_generator.gd:L77`

### Transforms personality traits into downstream modulation coefficients.

$$
sqrt(1.0 - 0.5  \cdot  h2  \cdot  h2)
$$

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
var env_factor: float = sqrt(1.0 - 0.5 * h2 * h2)
		var z_child: float = h2 * z_mid + env_factor * z_random[i]
```

| Variable | Meaning |
| :-- | :-- |
| `env_factor` | env factor |
| `h2` | h2 |
| `z_child` | z child |
| `z_mid` | z mid |
| `z_random` | z random |
| `i` | i |

📄 source: `scripts/systems/personality_generator.gd:L113`

### Transforms personality traits into downstream modulation coefficients.

$$
z_axis + _randfn(0.0, _facet_spread)
$$

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
var facet_z: float = z_axis + _randfn(0.0, _facet_spread)
```

| Variable | Meaning |
| :-- | :-- |
| `facet_z` | facet z |
| `z_axis` | z axis |
| `_facet_spread` |  facet spread |

📄 source: `scripts/systems/personality_generator.gd:L135`

## Configuration Reference (설정)

No explicit `GameConfig` references extracted.

## Cross-System Effects (시스템 간 상호작용)

### Imported Modules (모듈 임포트)

- [`personality_generator`](personality_generator.md) via `preload` at `scripts/systems/personality_generator.gd:L5`
- `scripts/core/personality_data.gd` via `preload` at `scripts/systems/personality_generator.gd:L7`
- [`trait`](trait.md) via `preload` at `scripts/systems/personality_generator.gd:L8`

### Shared Entity Fields (공유 엔티티 필드)

No cross-system shared entity field usage was inferred.

### Signals (시그널)

No emitted signals extracted for this module.

### Downstream Impact (다운스트림 영향)

- `scripts/core/entity_manager.gd` depends on this system's outputs.
- [`personality_generator`](personality_generator.md) depends on this system's outputs.

## Entity Data Model (엔티티 데이터 모델)

No entity field metadata extracted for this module.
