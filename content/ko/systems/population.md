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

📄 소스: `scripts/systems/population_system.gd` | 우선순위: 50 | 틱 간격: config (GameConfig.POPULATION_TICK_INTERVAL)

## 개요

The **Population** system implements Siler (1979) bathtub-curve mortality to simulate population dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.POPULATION_TICK_INTERVAL`) at priority **50**.

**핵심 엔티티 데이터**: `entity_name` (read/write (inferred)), `id` (read/write (inferred)), `settlement_id` (read/write (inferred))

## 틱 파이프라인

1. Run per-entity tick update loop
   📄 source: `scripts/systems/population_system.gd:L24`
   Math context: μ(x) = a₁·e^{-b₁·x} + a₂ + a₃·e^{b₃·x}
2. Check births
   📄 source: `scripts/systems/population_system.gd:L30`
   Math context: Computes a gameplay state update from mathematical relationships in the source logic., μ(x) = a₁·e^{-b₁·x} + a₂ + a₃·e^{b₃·x}

## 수식

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

## 설정 레퍼런스

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `BIRTH_FOOD_COST` | 3.0 | Population | Adjusts baseline system behavior under this module. |
| `MAX_ENTITIES` | 500 | Hard bound for safe state range. | Constrains extremes to stabilize the simulation. |
| `POPULATION_TICK_INTERVAL` | 30 | System update cadence. | Lower values increase update frequency and responsiveness. |

## 시스템 간 상호작용

### 모듈 임포트

임포트 관계가 추출되지 않음

### 공유 엔티티 필드

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `entity_name` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`chronicle`](chronicle.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |
| `id` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`social_events`](social_events.md) |
| `settlement_id` | read/write (inferred) | [`behavior`](behavior.md), [`emotions`](emotions.md), [`family`](family.md), [`migration`](migration.md), [`needs`](needs.md), [`stress`](stress.md) |

### 시그널

시그널 메타데이터가 추출되지 않음

### 다운스트림 영향

- 다운스트림 의존성이 추출되지 않음

## 엔티티 데이터 모델

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `entity_name` | read/write (inferred) | Variant | Entity name. | System-defined value domain. |
| `id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `settlement_id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
