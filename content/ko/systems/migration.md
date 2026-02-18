---
title: "Migration"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/migration_system.gd"
nav_order: 60
system_name: "migration"
---

# Migration

📄 소스: `scripts/systems/migration_system.gd` | 우선순위: 60 | 틱 간격: config (GameConfig.MIGRATION_TICK_INTERVAL)

## 개요

The **Migration** system implements a domain-specific simulation model to simulate migration dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.MIGRATION_TICK_INTERVAL`) at priority **60**.

**핵심 엔티티 데이터**: `action_target` (read/write (inferred)), `action_timer` (read/write (inferred)), `cached_path` (read/write (inferred)), `current_action` (read/write (inferred)), `id` (read/write (inferred)), `path_index` (read/write (inferred)), `settlement_id` (read/write (inferred))

## 틱 파이프라인

1. Run per-entity tick update loop
   📄 source: `scripts/systems/migration_system.gd:L27`
   Math context: Computes a gameplay state update from mathematical relationships in the source logic.
2. Resolve settlement stockpile totals
   📄 source: `scripts/systems/migration_system.gd:L188`
3. Resolve food in radius
   📄 source: `scripts/systems/migration_system.gd:L295`
4. Resolve food score
   📄 source: `scripts/systems/migration_system.gd:L309`

## 수식

### Computes a gameplay state update from mathematical relationships in the source logic.

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var explorer_chance: bool = _rng.randf() < GameConfig.MIGRATION_CHANCE
```

| Variable | Meaning |
| :-- | :-- |
| `explorer_chance` | explorer chance |
| `bool` | bool |
| `_rng` |  rng |

📄 source: `scripts/systems/migration_system.gd:L60`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
absi(other_settlement.center_x - x) + absi(other_settlement.center_y - y)
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var dist_to_settlement: int = absi(other_settlement.center_x - x) + absi(other_settlement.center_y - y)
```

| Variable | Meaning |
| :-- | :-- |
| `dist_to_settlement` | dist to settlement |
| `other_settlement` | other settlement |
| `center_x` | center x |
| `x` | x |
| `center_y` | center y |
| `y` | y |

📄 source: `scripts/systems/migration_system.gd:L265`

## 설정 레퍼런스

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `MAX_SETTLEMENTS` | 5 | Hard bound for safe state range. | Constrains extremes to stabilize the simulation. |
| `MIGRATION_CHANCE` | 0.05 | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `MIGRATION_COOLDOWN_TICKS` | 500 | Simulation-time conversion or cadence. | Adjusts baseline system behavior under this module. |
| `MIGRATION_GROUP_SIZE_MAX` | 7 | Hard bound for safe state range. | Constrains extremes to stabilize the simulation. |
| `MIGRATION_GROUP_SIZE_MIN` | 5 | Hard bound for safe state range. | Constrains extremes to stabilize the simulation. |
| `MIGRATION_MIN_POP` | 40 | Hard bound for safe state range. | Constrains extremes to stabilize the simulation. |
| `MIGRATION_SEARCH_RADIUS_MAX` | 80 | Hard bound for safe state range. | Constrains extremes to stabilize the simulation. |
| `MIGRATION_SEARCH_RADIUS_MIN` | 30 | Hard bound for safe state range. | Constrains extremes to stabilize the simulation. |
| `MIGRATION_STARTUP_FOOD` | 30.0 | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `MIGRATION_STARTUP_STONE` | 3.0 | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `MIGRATION_STARTUP_WOOD` | 10.0 | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `MIGRATION_TICK_INTERVAL` | 100 | System update cadence. | Lower values increase update frequency and responsiveness. |
| `SETTLEMENT_CLEANUP_INTERVAL` | 250 | Behavior tuning constant. | Lower values increase update frequency and responsiveness. |
| `SETTLEMENT_MIN_DISTANCE` | 25 | Hard bound for safe state range. | Constrains extremes to stabilize the simulation. |

## 시스템 간 상호작용

### 모듈 임포트

임포트 관계가 추출되지 않음

### 공유 엔티티 필드

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `action_target` | read/write (inferred) | [`behavior`](behavior.md), [`construction`](construction.md), [`movement`](movement.md) |
| `action_timer` | read/write (inferred) | [`behavior`](behavior.md), [`emotions`](emotions.md), [`movement`](movement.md) |
| `cached_path` | read/write (inferred) | [`behavior`](behavior.md), [`movement`](movement.md) |
| `current_action` | read/write (inferred) | [`behavior`](behavior.md), [`construction`](construction.md), [`emotions`](emotions.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`movement`](movement.md), [`needs`](needs.md), [`social_events`](social_events.md), [`stress`](stress.md) |
| `id` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`social_events`](social_events.md) |
| `path_index` | read/write (inferred) | [`behavior`](behavior.md), [`movement`](movement.md) |
| `settlement_id` | read/write (inferred) | [`behavior`](behavior.md), [`emotions`](emotions.md), [`family`](family.md), [`needs`](needs.md), [`population`](population.md), [`stress`](stress.md) |

### 시그널

시그널 메타데이터가 추출되지 않음

### 다운스트림 영향

- 다운스트림 의존성이 추출되지 않음

## 엔티티 데이터 모델

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `action_target` | read/write (inferred) | Variant | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `action_timer` | read/write (inferred) | int | Current behavior intent used by schedulers and downstream systems. | Non-negative tick counts. |
| `cached_path` | read/write (inferred) | Variant | Cached path. | System-defined value domain. |
| `current_action` | read/write (inferred) | String enum | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `path_index` | read/write (inferred) | Variant | Path index. | System-defined value domain. |
| `settlement_id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
