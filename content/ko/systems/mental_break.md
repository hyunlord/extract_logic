---
title: "Mental Break"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/mental_break_system.gd"
nav_order: 35
system_name: "mental_break"
---

# Mental Break

📄 source: `scripts/systems/mental_break_system.gd` | Priority: 35 | Tick interval: 1

## Overview (개요)

The **Mental Break** system implements McEwen (1998) allostatic load model to simulate mental break dynamics for entities and world state.
It runs every **1 ticks** (0.0 game-years) at priority **35**.

**Core entity data**: `emotion_data` (read/write (inferred)), `energy` (read/write (inferred)), `entity_name` (read/write (inferred)), `hunger` (read/write (inferred)), `personality` (read/write (inferred))

## Tick Pipeline (틱 파이프라인)

1. Run per-entity tick update loop
   📄 source: `scripts/systems/mental_break_system.gd:L60`
2. Check mental break conditions
   📄 source: `scripts/systems/mental_break_system.gd:L80`
   Math context: allostatic accumulation model
3. Calculate threshold
   📄 source: `scripts/systems/mental_break_system.gd:L90`
   Math context: load(t+1) = clamp(load(t) + chronic_stress - recovery), allostatic accumulation model
4. Tick active break
   📄 source: `scripts/systems/mental_break_system.gd:L186`

## Formulas (수식)

### Accumulates chronic stress burden over time and models recovery-driven load reduction.

**Model**: McEwen (1998) allostatic load model (McEwen, B. S. (1998). Protective and Damaging Effects of Stress Mediators)

$$
load(t+1) = clamp(load(t) + chronic_stress - recovery)
$$

**Interpretation**: Accumulates chronic stress burden over time and models recovery-driven load reduction.

**GDScript**:
```gdscript
threshold *= (1.0 + 0.40 * (ed.resilience - 0.5) * 2.0)
	threshold *= (1.0 + 0.25 * (C - 0.5) * 2.0)
	threshold *= (1.0 - 0.35 * (E - 0.5) * 2.0)
	threshold *= (1.0 - 0.25 * (ed.allostatic / 100.0))
	threshold *= (0.85 + 0.15 * entity.energy)
	threshold *= (0.85 + 0.15 * entity.hunger)
	threshold = clampf(threshold, THRESHOLD_MIN, THRESHOLD_MAX)
```

| Variable | Meaning |
| :-- | :-- |
| `threshold` | threshold |
| `ed` | ed |
| `resilience` | recovery resilience factor (CD-RISC based) |
| `allostatic` | allostatic load (chronic wear, 0-100) |
| `entity` | entity |
| `energy` | energy |
| `hunger` | nutrition state input |

📄 source: `scripts/systems/mental_break_system.gd:L99`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
clampf((stress - threshold) / BREAK_SCALE, 0.0, BREAK_CAP_PER_TICK)
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var p: float = clampf((stress - threshold) / BREAK_SCALE, 0.0, BREAK_CAP_PER_TICK)
```

| Variable | Meaning |
| :-- | :-- |
| `p` | p |
| `stress` | stress |
| `threshold` | threshold |

📄 source: `scripts/systems/mental_break_system.gd:L125`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
lerpf(1.0, 1.0 + axis_weight, axis_val)
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
w *= lerpf(1.0, 1.0 + axis_weight, axis_val)
```

| Variable | Meaning |
| :-- | :-- |
| `w` | w |
| `axis_weight` | axis weight |
| `axis_val` | axis val |

📄 source: `scripts/systems/mental_break_system.gd:L149`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
lerpf(1.0, 1.0 + absf(axis_weight), 1.0 - axis_val)
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
w *= lerpf(1.0, 1.0 + absf(axis_weight), 1.0 - axis_val)
```

| Variable | Meaning |
| :-- | :-- |
| `w` | w |
| `axis_weight` | axis weight |
| `axis_val` | axis val |

📄 source: `scripts/systems/mental_break_system.gd:L151`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
_rng.randf()  \cdot  total
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var roll: float = _rng.randf() * total
```

| Variable | Meaning |
| :-- | :-- |
| `roll` | roll |
| `_rng` |  rng |
| `total` | total |

📄 source: `scripts/systems/mental_break_system.gd:L158`

### Computes a gameplay state update from mathematical relationships in the source logic.

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var variance: int = bdef.get("duration_variance_ticks", 4)
	var duration: float = float(base + _rng.randi() % (variance + 1))
	duration = clampf(duration, 1.0, 168.0)
```

| Variable | Meaning |
| :-- | :-- |
| `variance` | variance |
| `bdef` | bdef |
| `duration` | duration |
| `base` | base |
| `_rng` |  rng |

📄 source: `scripts/systems/mental_break_system.gd:L173`

## Configuration Reference (설정)

No explicit `GameConfig` references extracted.

## Cross-System Effects (시스템 간 상호작용)

### Imported Modules (모듈 임포트)

No import relationships extracted for this module.

### Shared Entity Fields (공유 엔티티 필드)

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `emotion_data` | read/write (inferred) | [`behavior`](behavior.md), [`emotions`](emotions.md), [`family`](family.md), [`stress`](stress.md), [`trait`](trait.md) |
| `energy` | read/write (inferred) | [`behavior`](behavior.md), [`building_effect`](building_effect.md), [`emotions`](emotions.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |
| `entity_name` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`chronicle`](chronicle.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`stress`](stress.md), [`trait_violation`](trait_violation.md), [`trauma_scar`](trauma_scar.md) |
| `hunger` | read/write (inferred) | [`behavior`](behavior.md), [`childcare`](childcare.md), [`family`](family.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |
| `personality` | read/write (inferred) | [`aging`](aging.md), [`emotions`](emotions.md), [`stress`](stress.md), [`trait`](trait.md), [`trait_violation`](trait_violation.md) |

### Signals (시그널)

No emitted signals extracted for this module.

### Downstream Impact (다운스트림 영향)

- No explicit downstream dependencies extracted.

## Entity Data Model (엔티티 데이터 모델)

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `emotion_data` | read/write (inferred) | Dictionary / custom data object | Affective state used for behavior modulation and social propagation. | Structured object with nested metrics/axes. |
| `energy` | read/write (inferred) | float | Fatigue/rest capacity controlling action readiness. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
| `entity_name` | read/write (inferred) | Variant | Entity name. | System-defined value domain. |
| `hunger` | read/write (inferred) | float | Nutritional deprivation level driving survival and action priorities. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
| `personality` | read/write (inferred) | Dictionary / custom data object | Trait/axis profile used for sensitivity and decision weighting. | Structured object with nested metrics/axes. |
