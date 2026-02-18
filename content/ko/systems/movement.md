---
title: "Movement"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/movement_system.gd"
nav_order: 30
system_name: "movement"
---

# Movement

📄 소스: `scripts/systems/movement_system.gd` | 우선순위: 30 | 틱 간격: config (GameConfig.MOVEMENT_TICK_INTERVAL)

## 개요

The **Movement** system implements a domain-specific simulation model to simulate movement dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.MOVEMENT_TICK_INTERVAL`) at priority **30**.

**핵심 엔티티 데이터**: `action_target` (read/write (inferred)), `action_timer` (read/write (inferred)), `age_stage` (read/write (inferred)), `cached_path` (read/write (inferred)), `current_action` (read/write (inferred)), `energy` (read/write (inferred)), `entity_name` (read/write (inferred)), `hunger` (read/write (inferred)), `id` (read/write (inferred)), `inventory` (read/write (inferred)), `path_index` (read/write (inferred)), `position` (read/write (inferred)), `remove_item` (read/write (inferred)), `social` (read/write (inferred))

## 틱 파이프라인

1. Run per-entity tick update loop
   📄 source: `scripts/systems/movement_system.gd:L23`
2. Apply arrival effect
   📄 source: `scripts/systems/movement_system.gd:L140`

## 수식

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
absi(entity.position.x - stockpile.tile_x) + absi(entity.position.y - stockpile.tile_y)
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var dist: int = absi(entity.position.x - stockpile.tile_x) + absi(entity.position.y - stockpile.tile_y)
```

| Variable | Meaning |
| :-- | :-- |
| `dist` | dist |
| `entity` | entity |
| `position` | position |
| `x` | x |
| `stockpile` | stockpile |
| `tile_x` | tile x |
| `y` | y |
| `tile_y` | tile y |

📄 source: `scripts/systems/movement_system.gd:L220`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
absi(entity.position.x - stockpile.tile_x) + absi(entity.position.y - stockpile.tile_y)
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var dist: int = absi(entity.position.x - stockpile.tile_x) + absi(entity.position.y - stockpile.tile_y)
```

| Variable | Meaning |
| :-- | :-- |
| `dist` | dist |
| `entity` | entity |
| `position` | position |
| `x` | x |
| `stockpile` | stockpile |
| `tile_x` | tile x |
| `y` | y |
| `tile_y` | tile y |

📄 source: `scripts/systems/movement_system.gd:L250`

## 설정 레퍼런스

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `CHILD_MOVE_SKIP_MOD` | { 	"infant": 2, 	"toddler": 2, 	"child": 3, 	"teen": 10, 	"elder": 3, } | Movement skip modulo by age stage (skip 1 in N ticks; higher N = faster) infant/toddler: skip every other tick → 50%, child: skip 1/3 → 70% teen: skip 1/10 → 90%, elder: skip 1/3 → 67% | Adjusts baseline system behavior under this module. |
| `FOOD_HUNGER_RESTORE` | 0.3 | Eating constants | Adjusts baseline system behavior under this module. |
| `HUNGER_EAT_THRESHOLD` | 0.5 | Threshold gate for state transitions. | Changing this moves trigger points for behavior changes. |
| `MOVEMENT_TICK_INTERVAL` | 3 | System update cadence. | Lower values increase update frequency and responsiveness. |

## 시스템 간 상호작용

### 모듈 임포트

임포트 관계가 추출되지 않음

### 공유 엔티티 필드

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `action_target` | read/write (inferred) | [`behavior`](behavior.md), [`construction`](construction.md), [`migration`](migration.md) |
| `action_timer` | read/write (inferred) | [`behavior`](behavior.md), [`emotions`](emotions.md), [`migration`](migration.md) |
| `age_stage` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`childcare`](childcare.md), [`construction`](construction.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mortality`](mortality.md), [`needs`](needs.md) |
| `cached_path` | read/write (inferred) | [`behavior`](behavior.md), [`migration`](migration.md) |
| `current_action` | read/write (inferred) | [`behavior`](behavior.md), [`construction`](construction.md), [`emotions`](emotions.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`needs`](needs.md), [`social_events`](social_events.md), [`stress`](stress.md) |
| `energy` | read/write (inferred) | [`behavior`](behavior.md), [`building_effect`](building_effect.md), [`emotions`](emotions.md), [`mental_break`](mental_break.md), [`needs`](needs.md), [`stress`](stress.md) |
| `entity_name` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`chronicle`](chronicle.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`needs`](needs.md), [`population`](population.md), [`stress`](stress.md) |
| `hunger` | read/write (inferred) | [`behavior`](behavior.md), [`childcare`](childcare.md), [`family`](family.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`needs`](needs.md), [`stress`](stress.md) |
| `id` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`mortality`](mortality.md), [`needs`](needs.md), [`population`](population.md), [`social_events`](social_events.md) |
| `inventory` | read/write (inferred) | [`behavior`](behavior.md), [`needs`](needs.md) |
| `path_index` | read/write (inferred) | [`behavior`](behavior.md), [`migration`](migration.md) |
| `position` | read/write (inferred) | [`behavior`](behavior.md), [`construction`](construction.md), [`gathering`](gathering.md), [`social_events`](social_events.md) |
| `remove_item` | read/write (inferred) | [`behavior`](behavior.md), [`needs`](needs.md) |
| `social` | read/write (inferred) | [`behavior`](behavior.md), [`building_effect`](building_effect.md), [`needs`](needs.md), [`stress`](stress.md) |

### 시그널

시그널 메타데이터가 추출되지 않음

### 다운스트림 영향

- 다운스트림 의존성이 추출되지 않음

## 엔티티 데이터 모델

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `action_target` | read/write (inferred) | Variant | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `action_timer` | read/write (inferred) | int | Current behavior intent used by schedulers and downstream systems. | Non-negative tick counts. |
| `age_stage` | read/write (inferred) | String enum | Lifecycle progression used for stage-specific behavior and events. | Named categorical states. |
| `cached_path` | read/write (inferred) | Variant | Cached path. | System-defined value domain. |
| `current_action` | read/write (inferred) | String enum | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `energy` | read/write (inferred) | float | Fatigue/rest capacity controlling action readiness. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
| `entity_name` | read/write (inferred) | Variant | Entity name. | System-defined value domain. |
| `hunger` | read/write (inferred) | float | Nutritional deprivation level driving survival and action priorities. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
| `id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `inventory` | read/write (inferred) | Variant | Inventory. | System-defined value domain. |
| `path_index` | read/write (inferred) | Variant | Path index. | System-defined value domain. |
| `position` | read/write (inferred) | Vector2 / Vector2i | World-space location used for movement and proximity checks. | Grid/world vectors. |
| `remove_item` | read/write (inferred) | Variant | Remove item. | System-defined value domain. |
| `social` | read/write (inferred) | float | Social fulfillment/deficit level affecting mood and stress. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
