---
title: "Population"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/population_system.gd"
nav_order: 50
system_name: "population"
---

# Population

📄 source: `scripts/systems/population_system.gd` | Priority: 50 | Tick interval: config (GameConfig.POPULATION_TICK_INTERVAL)

## Overview

The **Population** system implements Siler (1979) bathtub-curve mortality to simulate population dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.POPULATION_TICK_INTERVAL`) at priority **50**.

**Core entity data**: `entity_name` (read/write (inferred)), `id` (read/write (inferred)), `settlement_id` (read/write (inferred))

## Tick Pipeline

1. Run per-entity tick update loop
   📄 source: `scripts/systems/population_system.gd:L24`
   Math context: μ(x) = a₁·e^{-b₁·x} + a₂ + a₃·e^{b₃·x}
2. Check births
   📄 source: `scripts/systems/population_system.gd:L30`
   Math context: Computes a gameplay state update from mathematical relationships in the source logic., μ(x) = a₁·e^{-b₁·x} + a₂ + a₃·e^{b₃·x}

## Formulas

### Calculates the age-specific mortality hazard rate combining infant decline, constant background risk, and exponential aging.

**Model**: Siler (1979) bathtub-curve mortality (Siler, W. (1979). A Competing-Risk Model for Animal Mortality)

$$
μ(x) = a₁·e^{-b₁·x} + a₂ + a₃·e^{b₃·x}
$$

**Interpretation**: Calculates the age-specific mortality hazard rate combining infant decline, constant background risk, and exponential aging.

**GDScript**:
```gdscript
Natural deaths disabled: handled by MortalitySystem (T-2000, Siler model)
```

| Variable | Meaning |
| :-- | :-- |
| `deaths` | deaths |
| `disabled` | disabled |
| `handled` | handled |
| `by` | by |
| `model` | model |

📄 source: `scripts/systems/population_system.gd:L26`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
alive_count  \cdot  0.5 (lowered from 1.0 — was blocking growth at ~49)
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
Food threshold: need food >= alive_count * 0.5 (lowered from 1.0 — was blocking growth at ~49)
```

| Variable | Meaning |
| :-- | :-- |
| `threshold` | threshold |
| `need` | need |
| `food` | food |
| `alive_count` | alive count |
| `lowered` | lowered |
| `from` | from |
| `was` | was |
| `blocking` | blocking |
| `growth` | growth factor |
| `at` | at |

📄 source: `scripts/systems/population_system.gd:L70`

### Calculates the age-specific mortality hazard rate combining infant decline, constant background risk, and exponential aging.

**Model**: Siler (1979) bathtub-curve mortality (Siler, W. (1979). A Competing-Risk Model for Animal Mortality)

$$
μ(x) = a₁·e^{-b₁·x} + a₂ + a₃·e^{b₃·x}
$$

**Interpretation**: Calculates the age-specific mortality hazard rate combining infant decline, constant background risk, and exponential aging.

**GDScript**:
```gdscript
Old natural death logic removed — replaced by MortalitySystem (Siler model, T-2000)
```

| Variable | Meaning |
| :-- | :-- |
| `natural` | natural |
| `death` | death |
| `logic` | logic |
| `removed` | removed |
| `replaced` | replaced |
| `by` | by |
| `model` | model |

📄 source: `scripts/systems/population_system.gd:L106`

## Config Reference

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `BIRTH_FOOD_COST` | 3.0 | Population | Adjusts baseline system behavior under this module. |
| `MAX_ENTITIES` | 500 | Hard bound for safe state range. | Constrains extremes to stabilize the simulation. |
| `POPULATION_TICK_INTERVAL` | 30 | System update cadence. | Lower values increase update frequency and responsiveness. |

## Cross-System Effects

### Imported Modules

No import relationships extracted

### Shared Entity Fields

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `entity_name` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`chronicle`](chronicle.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |
| `id` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`social_events`](social_events.md) |
| `settlement_id` | read/write (inferred) | [`behavior`](behavior.md), [`emotions`](emotions.md), [`family`](family.md), [`migration`](migration.md), [`needs`](needs.md), [`stress`](stress.md) |

### Signals

No signal metadata extracted

### Downstream Impact

- No downstream dependencies extracted

## Entity Data Model

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `entity_name` | read/write (inferred) | Variant | Entity name. | System-defined value domain. |
| `id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `settlement_id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
