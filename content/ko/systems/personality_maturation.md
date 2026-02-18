---
title: "Personality Maturation"
description: "Age-based personality maturation using OU (Ornstein-Uhlenbeck) process."
generated: true
source_files:
  - "scripts/systems/personality_maturation.gd"
nav_order: 999
system_name: "personality_maturation"
---

# Personality Maturation

📄 소스: `scripts/systems/personality_maturation.gd` | 우선순위: n/a | 틱 간격: n/a

## 개요

The **Personality Maturation** system implements Uhlenbeck & Ornstein (1930) mean-reverting process, Ornstein-Uhlenbeck mean reversion to simulate age-based personality maturation using OU (Ornstein-Uhlenbeck) process.
It runs **at an unspecified cadence** at priority **n/a**.

**핵심 엔티티 데이터**: No entity fields were extracted.

> Age-based personality maturation using OU (Ornstein-Uhlenbeck) process.

## 틱 파이프라인

1. Apply maturation
   📄 source: `scripts/systems/personality_maturation.gd:L41`
   Math context: Transforms personality traits into downstream modulation coefficients.
2. Resolve maturation target
   📄 source: `scripts/systems/personality_maturation.gd:L62`

## 수식

### Updates a latent state by mean-reverting toward baseline while injecting stochastic fluctuation.

**Model**: Uhlenbeck & Ornstein (1930) mean-reverting process (Uhlenbeck, G. E., & Ornstein, L. S. (1930). On the Theory of the Brownian Motion)

$$
dX = θ(μ - X)dt + σdW
$$

**Interpretation**: Updates a latent state by mean-reverting toward baseline while injecting stochastic fluctuation.

**GDScript**:
```gdscript
Age-based personality maturation using OU (Ornstein-Uhlenbeck) process.
Called once per game year for each entity.
Ashton & Lee (2016): H increases ~+1 SD from 18→60, E/X mild increase.
No class_name - use preload("res://scripts/systems/personality_maturation.gd").
```

| Variable | Meaning |
| :-- | :-- |
| `based` | based |
| `personality` | personality |
| `maturation` | maturation |
| `using` | using |
| `process` | process |
| `once` | once |
| `per` | per |
| `game` | game |
| `year` | year |
| `each` | each |
| `entity` | entity |
| `increases` | increases |
| `from` | from |
| `mild` | mild |
| `increase` | increase |
| `use` | use |

📄 source: `scripts/systems/personality_maturation.gd:L3`

### Transforms personality traits into downstream modulation coefficients.

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
Box-Muller normal random
```

| Variable | Meaning |
| :-- | :-- |
| `normal` | normal |
| `random` | random |

📄 source: `scripts/systems/personality_maturation.gd:L30`

### Transforms personality traits into downstream modulation coefficients.

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
var u1: float = _rng.randf()
	var u2: float = _rng.randf()
	if u1 < 1e-10:
		u1 = 1e-10
	return mean + std * sqrt(-2.0 * log(u1)) * cos(2.0 * PI * u2)
```

| Variable | Meaning |
| :-- | :-- |
| `u1` | u1 |
| `_rng` |  rng |
| `u2` | u2 |
| `mean` | mean |
| `std` | std |

📄 source: `scripts/systems/personality_maturation.gd:L32`

### Transforms personality traits into downstream modulation coefficients.

$$
_theta  \cdot  (target - current_z) + _randfn(0.0, _sigma)
$$

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
var dz: float = _theta * (target - current_z) + _randfn(0.0, _sigma)
			pd.facets[fkey] = pd.from_zscore(current_z + dz)
```

| Variable | Meaning |
| :-- | :-- |
| `dz` | dz |
| `_theta` | mean reversion coefficient |
| `target` | target |
| `current_z` | current z |
| `_sigma` | standard deviation/noise scale |
| `pd` | pd |
| `facets` | facets |
| `fkey` | fkey |

📄 source: `scripts/systems/personality_maturation.gd:L53`

### Transforms personality traits into downstream modulation coefficients.

$$
clampf(float(age - start_age) / span, 0.0, 1.0)
$$

**Interpretation**: Transforms personality traits into downstream modulation coefficients.

**GDScript**:
```gdscript
var t: float = clampf(float(age - start_age) / span, 0.0, 1.0)
	return max_shift * t
```

| Variable | Meaning |
| :-- | :-- |
| `t` | t |
| `age` | age-related input |
| `start_age` | age-related input |
| `span` | span |
| `max_shift` | max shift |

📄 source: `scripts/systems/personality_maturation.gd:L82`

## 설정 레퍼런스

GameConfig 참조가 추출되지 않음

## 시스템 간 상호작용

### 모듈 임포트

- [`personality_maturation`](personality_maturation.md) via `preload` at `scripts/systems/personality_maturation.gd:L6`
- `scripts/core/personality_data.gd` via `preload` at `scripts/systems/personality_maturation.gd:L8`
- [`trait`](trait.md) via `preload` at `scripts/systems/personality_maturation.gd:L9`

### 공유 엔티티 필드

공유 필드가 추론되지 않음

### 시그널

시그널 메타데이터가 추출되지 않음

### 다운스트림 영향

- [`aging`](aging.md) depends on this system's outputs.
- [`personality_maturation`](personality_maturation.md) depends on this system's outputs.

## 엔티티 데이터 모델

No entity field metadata extracted for this module.
