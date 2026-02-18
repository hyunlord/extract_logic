---
title: "Needs"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/needs_system.gd"
nav_order: 10
system_name: "needs"
---

# Needs

📄 source: `scripts/systems/needs_system.gd` | Priority: 10 | Tick interval: config (GameConfig.NEEDS_TICK_INTERVAL)

## Overview (개요)

The **Needs** system implements Standard exponential decay to simulate needs dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.NEEDS_TICK_INTERVAL`) at priority **10**.

**Core entity data**: `age` (read/write (inferred)), `age_stage` (read/write (inferred)), `birth_tick` (read/write (inferred)), `current_action` (read/write (inferred)), `energy` (read/write (inferred)), `entity_name` (read/write (inferred)), `hunger` (read/write (inferred)), `id` (read/write (inferred)), `inventory` (read/write (inferred)), `remove_item` (read/write (inferred)), `settlement_id` (read/write (inferred)), `social` (read/write (inferred)), `starving_timer` (read/write (inferred))

## Tick Pipeline (틱 파이프라인)

1. Run per-entity tick update loop
   📄 source: `scripts/systems/needs_system.gd:L20`
   Math context: x(t) = x₀·e^{-λt}, Computes a gameplay state update from mathematical relationships in the source logic., exponential decay dynamics
2. Resolve settlement food
   📄 source: `scripts/systems/needs_system.gd:L106`

## Formulas (수식)

### Applies time-based exponential decay using half-life or decay-rate parameters.

**Model**: Standard exponential decay (Standard first-order decay dynamics)

$$
x(t) = x₀·e^{-λt}
$$

**Interpretation**: Applies time-based exponential decay using half-life or decay-rate parameters.

**GDScript**:
```gdscript
entity.hunger -= GameConfig.HUNGER_DECAY_RATE * hunger_mult * metabolic_factor
		entity.energy -= GameConfig.ENERGY_DECAY_RATE
		entity.social -= GameConfig.SOCIAL_DECAY_RATE
```

| Variable | Meaning |
| :-- | :-- |
| `entity` | entity |
| `hunger` | nutrition state input |
| `hunger_mult` | nutrition state input |
| `metabolic_factor` | metabolic factor |
| `energy` | energy |
| `social` | social |

📄 source: `scripts/systems/needs_system.gd:L27`

### Computes a gameplay state update from mathematical relationships in the source logic.

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
entity.hunger = clampf(entity.hunger, 0.0, 1.0)
```

| Variable | Meaning |
| :-- | :-- |
| `entity` | entity |
| `hunger` | nutrition state input |

📄 source: `scripts/systems/needs_system.gd:L47`

### Computes a gameplay state update from mathematical relationships in the source logic.

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
entity.energy = clampf(entity.energy, 0.0, 1.0)
		entity.social = clampf(entity.social, 0.0, 1.0)
```

| Variable | Meaning |
| :-- | :-- |
| `entity` | entity |
| `energy` | energy |
| `social` | social |

📄 source: `scripts/systems/needs_system.gd:L51`

## Configuration Reference (설정)

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `CHILD_HUNGER_DECAY_MULT` | { 	"infant": 0.15, 	"toddler": 0.25, 	"child": 0.35, 	"teen": 0.70, } | Decay speed of accumulated state. | Higher values usually lengthen persistence of historical state. |
| `CHILD_STARVATION_GRACE_TICKS` | { 	"infant": 50, 	"toddler": 40, 	"child": 30, 	"teen": 20, } | Simulation-time conversion or cadence. | Adjusts baseline system behavior under this module. |
| `ENERGY_ACTION_COST` | 0.005 | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `ENERGY_DECAY_RATE` | 0.003 | Decay speed of accumulated state. | Higher values usually lengthen persistence of historical state. |
| `FOOD_HUNGER_RESTORE` | 0.3 | Eating constants | Adjusts baseline system behavior under this module. |
| `HUNGER_DECAY_RATE` | 0.002 | Decay speed of accumulated state. | Higher values usually lengthen persistence of historical state. |
| `HUNGER_EAT_THRESHOLD` | 0.5 | Threshold gate for state transitions. | Changing this moves trigger points for behavior changes. |
| `HUNGER_METABOLIC_MIN` | 0.3 | Hard bound for safe state range. | Constrains extremes to stabilize the simulation. |
| `HUNGER_METABOLIC_RANGE` | 0.7 | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `NEEDS_TICK_INTERVAL` | 2 | System update cadence. | Lower values increase update frequency and responsiveness. |
| `SOCIAL_DECAY_RATE` | 0.001 | Decay speed of accumulated state. | Higher values usually lengthen persistence of historical state. |
| `STARVATION_GRACE_TICKS` | 25 | Simulation-time conversion or cadence. | Adjusts baseline system behavior under this module. |
| `get_age_years` | (not found) | Behavior tuning constant. | Adjusts baseline system behavior under this module. |

## Cross-System Effects (시스템 간 상호작용)

### Imported Modules (모듈 임포트)

No import relationships extracted for this module.

### Shared Entity Fields (공유 엔티티 필드)

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `age` | read/write (inferred) | [`aging`](aging.md), [`family`](family.md), [`mortality`](mortality.md) |
| `age_stage` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`childcare`](childcare.md), [`construction`](construction.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mortality`](mortality.md), [`movement`](movement.md) |
| `birth_tick` | read/write (inferred) | [`mortality`](mortality.md) |
| `current_action` | read/write (inferred) | [`behavior`](behavior.md), [`construction`](construction.md), [`emotions`](emotions.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`movement`](movement.md), [`social_events`](social_events.md), [`stress`](stress.md) |
| `energy` | read/write (inferred) | [`behavior`](behavior.md), [`building_effect`](building_effect.md), [`emotions`](emotions.md), [`mental_break`](mental_break.md), [`movement`](movement.md), [`stress`](stress.md) |
| `entity_name` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`chronicle`](chronicle.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`population`](population.md), [`stress`](stress.md) |
| `hunger` | read/write (inferred) | [`behavior`](behavior.md), [`childcare`](childcare.md), [`family`](family.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`stress`](stress.md) |
| `id` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`mortality`](mortality.md), [`movement`](movement.md), [`population`](population.md), [`social_events`](social_events.md) |
| `inventory` | read/write (inferred) | [`behavior`](behavior.md), [`movement`](movement.md) |
| `remove_item` | read/write (inferred) | [`behavior`](behavior.md), [`movement`](movement.md) |
| `settlement_id` | read/write (inferred) | [`behavior`](behavior.md), [`emotions`](emotions.md), [`family`](family.md), [`migration`](migration.md), [`population`](population.md), [`stress`](stress.md) |
| `social` | read/write (inferred) | [`behavior`](behavior.md), [`building_effect`](building_effect.md), [`movement`](movement.md), [`stress`](stress.md) |

### Signals (시그널)

No emitted signals extracted for this module.

### Downstream Impact (다운스트림 영향)

- No explicit downstream dependencies extracted.

## Entity Data Model (엔티티 데이터 모델)

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `age` | read/write (inferred) | int | Lifecycle progression used for stage-specific behavior and events. | Non-negative tick counts. |
| `age_stage` | read/write (inferred) | String enum | Lifecycle progression used for stage-specific behavior and events. | Named categorical states. |
| `birth_tick` | read/write (inferred) | Variant | Birth tick. | System-defined value domain. |
| `current_action` | read/write (inferred) | String enum | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `energy` | read/write (inferred) | float | Fatigue/rest capacity controlling action readiness. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
| `entity_name` | read/write (inferred) | Variant | Entity name. | System-defined value domain. |
| `hunger` | read/write (inferred) | float | Nutritional deprivation level driving survival and action priorities. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
| `id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `inventory` | read/write (inferred) | Variant | Inventory. | System-defined value domain. |
| `remove_item` | read/write (inferred) | Variant | Remove item. | System-defined value domain. |
| `settlement_id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `social` | read/write (inferred) | float | Social fulfillment/deficit level affecting mood and stress. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
| `starving_timer` | read/write (inferred) | Variant | Starving timer. | System-defined value domain. |
