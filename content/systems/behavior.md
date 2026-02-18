---
title: "Behavior"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/ai/behavior_system.gd"
nav_order: 20
system_name: "behavior"
---

# Behavior

📄 source: `scripts/ai/behavior_system.gd` | Priority: 20 | Tick interval: config (GameConfig.BEHAVIOR_TICK_INTERVAL)

## Overview (개요)

The **Behavior** system implements a domain-specific simulation model to simulate behavior dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.BEHAVIOR_TICK_INTERVAL`) at priority **20**.

**Core entity data**: `action_history` (read/write (inferred)), `action_target` (read/write (inferred)), `action_timer` (read/write (inferred)), `age_stage` (read/write (inferred)), `cached_path` (read/write (inferred)), `current_action` (read/write (inferred)), `emotion_data` (read/write (inferred)), `emotions` (read/write (inferred)), `energy` (read/write (inferred)), `entity_name` (read/write (inferred)), `get_total_carry` (read/write (inferred)), `hunger` (read/write (inferred)), `id` (read/write (inferred)), `inventory` (read/write (inferred)), `job` (read/write (inferred)), `partner_id` (read/write (inferred)), `path_index` (read/write (inferred)), `position` (read/write (inferred)), `remove_item` (read/write (inferred)), `settlement_id` (read/write (inferred)), `social` (read/write (inferred))

## Tick Pipeline (틱 파이프라인)

1. Run per-entity tick update loop
   📄 source: `scripts/ai/behavior_system.gd:L27`

## Formulas (수식)

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
0.3 + _rng.randf()  \cdot  0.1
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
"wander": 0.3 + _rng.randf() * 0.1,
			"rest": _urgency_curve(energy_deficit) * 1.2,
			"socialize": _urgency_curve(social_deficit) * 0.8,
```

| Variable | Meaning |
| :-- | :-- |
| `_rng` |  rng |
| `energy_deficit` | energy deficit |
| `social_deficit` | social deficit |

📄 source: `scripts/ai/behavior_system.gd:L60`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
0.3 + _rng.randf()  \cdot  0.1
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
"wander": 0.3 + _rng.randf() * 0.1,
			"rest": _urgency_curve(energy_deficit) * 1.2,
			"socialize": _urgency_curve(social_deficit) * 0.8,
			"gather_food": _urgency_curve(hunger_deficit) * 1.5 * 0.4,
```

| Variable | Meaning |
| :-- | :-- |
| `_rng` |  rng |
| `energy_deficit` | energy deficit |
| `social_deficit` | social deficit |
| `hunger_deficit` | nutrition state input |

📄 source: `scripts/ai/behavior_system.gd:L68`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
(0.3 + _rng.randf()  \cdot  0.1)  \cdot  0.3
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
child_scores["gather_wood"] = (0.3 + _rng.randf() * 0.1) * 0.3
```

| Variable | Meaning |
| :-- | :-- |
| `child_scores` | child scores |
| `_rng` |  rng |

📄 source: `scripts/ai/behavior_system.gd:L74`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
0.2 + _rng.randf()  \cdot  0.1
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
"wander": 0.2 + _rng.randf() * 0.1,
		"gather_food": _urgency_curve(hunger_deficit) * 1.5,
		"rest": _urgency_curve(energy_deficit) * 1.2,
		"socialize": _urgency_curve(social_deficit) * 0.8,
```

| Variable | Meaning |
| :-- | :-- |
| `_rng` |  rng |
| `hunger_deficit` | nutrition state input |
| `energy_deficit` | energy deficit |
| `social_deficit` | social deficit |

📄 source: `scripts/ai/behavior_system.gd:L78`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
0.4 + _rng.randf()  \cdot  0.1
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
scores["visit_partner"] = 0.4 + _rng.randf() * 0.1
```

| Variable | Meaning |
| :-- | :-- |
| `scores` | scores |
| `_rng` |  rng |

📄 source: `scripts/ai/behavior_system.gd:L92`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
0.3 + _rng.randf()  \cdot  0.1
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
scores["gather_wood"] = 0.3 + _rng.randf() * 0.1
```

| Variable | Meaning |
| :-- | :-- |
| `scores` | scores |
| `_rng` |  rng |

📄 source: `scripts/ai/behavior_system.gd:L106`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
0.2 + _rng.randf()  \cdot  0.1
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
scores["gather_stone"] = 0.2 + _rng.randf() * 0.1
```

| Variable | Meaning |
| :-- | :-- |
| `scores` | scores |
| `_rng` |  rng |

📄 source: `scripts/ai/behavior_system.gd:L108`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
0.4 + _rng.randf()  \cdot  0.1
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
scores["build"] = 0.4 + _rng.randf() * 0.1
```

| Variable | Meaning |
| :-- | :-- |
| `scores` | scores |
| `_rng` |  rng |

📄 source: `scripts/ai/behavior_system.gd:L133`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
0.4 + _rng.randf()  \cdot  0.1
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
scores["build"] = 0.4 + _rng.randf() * 0.1
```

| Variable | Meaning |
| :-- | :-- |
| `scores` | scores |
| `_rng` |  rng |

📄 source: `scripts/ai/behavior_system.gd:L135`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
return pow(deficit, 2.0)
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
return pow(deficit, 2.0)
```

| Variable | Meaning |
| :-- | :-- |
| `deficit` | deficit |

📄 source: `scripts/ai/behavior_system.gd:L172`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
absi(other.position.x - entity.position.x) + absi(other.position.y - entity.position.y)
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var dist: int = absi(other.position.x - entity.position.x) + absi(other.position.y - entity.position.y)
```

| Variable | Meaning |
| :-- | :-- |
| `dist` | dist |
| `other` | other |
| `position` | position |
| `x` | x |
| `entity` | entity |
| `y` | y |

📄 source: `scripts/ai/behavior_system.gd:L347`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
absi(building.tile_x - pos.x) + absi(building.tile_y - pos.y)
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var dist: int = absi(building.tile_x - pos.x) + absi(building.tile_y - pos.y)
```

| Variable | Meaning |
| :-- | :-- |
| `dist` | dist |
| `building` | building |
| `tile_x` | tile x |
| `pos` | pos |
| `x` | x |
| `tile_y` | tile y |
| `y` | y |

📄 source: `scripts/ai/behavior_system.gd:L406`

### Computes a gameplay state update from mathematical relationships in the source logic.

$$
float(absi(building.tile_x - entity.position.x) + absi(building.tile_y - entity.position.y))
$$

**Interpretation**: Computes a gameplay state update from mathematical relationships in the source logic.

**GDScript**:
```gdscript
var dist: float = float(absi(building.tile_x - entity.position.x) + absi(building.tile_y - entity.position.y))
```

| Variable | Meaning |
| :-- | :-- |
| `dist` | dist |
| `building` | building |
| `tile_x` | tile x |
| `entity` | entity |
| `position` | position |
| `x` | x |
| `tile_y` | tile y |
| `y` | y |

📄 source: `scripts/ai/behavior_system.gd:L447`

## Configuration Reference (설정)

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `BEHAVIOR_TICK_INTERVAL` | 10 | System update cadence. | Lower values increase update frequency and responsiveness. |
| `BUILDING_TYPES` | { 	"stockpile": {"cost": {"wood": 2.0}, "build_ticks": 36, "radius": 8}, 	"shelter": {"cost": {"wood": 4.0, "stone": 1.0}, "build_ticks": 60, "radius": 0}, 	"campfire": {"cost": {"wood": 1.0}, "build_ticks": 24, "radius": 5}, } | Building type definitions | Adjusts baseline system behavior under this module. |
| `Biome` | (not found) | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `ResourceType` | (not found) | Behavior tuning constant. | Adjusts baseline system behavior under this module. |

## Cross-System Effects (시스템 간 상호작용)

### Imported Modules (모듈 임포트)

No import relationships extracted for this module.

### Shared Entity Fields (공유 엔티티 필드)

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `action_target` | read/write (inferred) | [`construction`](construction.md), [`migration`](migration.md), [`movement`](movement.md) |
| `action_timer` | read/write (inferred) | [`emotions`](emotions.md), [`migration`](migration.md), [`movement`](movement.md) |
| `age_stage` | read/write (inferred) | [`aging`](aging.md), [`childcare`](childcare.md), [`construction`](construction.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md) |
| `cached_path` | read/write (inferred) | [`migration`](migration.md), [`movement`](movement.md) |
| `current_action` | read/write (inferred) | [`construction`](construction.md), [`emotions`](emotions.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`movement`](movement.md), [`needs`](needs.md), [`social_events`](social_events.md), [`stress`](stress.md) |
| `emotion_data` | read/write (inferred) | [`emotions`](emotions.md), [`family`](family.md), [`mental_break`](mental_break.md), [`stress`](stress.md), [`trait`](trait.md) |
| `emotions` | read/write (inferred) | [`emotions`](emotions.md), [`family`](family.md), [`trait`](trait.md) |
| `energy` | read/write (inferred) | [`building_effect`](building_effect.md), [`emotions`](emotions.md), [`mental_break`](mental_break.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |
| `entity_name` | read/write (inferred) | [`aging`](aging.md), [`chronicle`](chronicle.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`stress`](stress.md) |
| `get_total_carry` | read/write (inferred) | [`gathering`](gathering.md) |
| `hunger` | read/write (inferred) | [`childcare`](childcare.md), [`family`](family.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |
| `id` | read/write (inferred) | [`aging`](aging.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`social_events`](social_events.md) |
| `inventory` | read/write (inferred) | [`movement`](movement.md), [`needs`](needs.md) |
| `job` | read/write (inferred) | [`aging`](aging.md), [`job_assignment`](job_assignment.md) |
| `partner_id` | read/write (inferred) | [`family`](family.md) |
| `path_index` | read/write (inferred) | [`migration`](migration.md), [`movement`](movement.md) |
| `position` | read/write (inferred) | [`construction`](construction.md), [`gathering`](gathering.md), [`movement`](movement.md), [`social_events`](social_events.md) |
| `remove_item` | read/write (inferred) | [`movement`](movement.md), [`needs`](needs.md) |
| `settlement_id` | read/write (inferred) | [`emotions`](emotions.md), [`family`](family.md), [`migration`](migration.md), [`needs`](needs.md), [`population`](population.md), [`stress`](stress.md) |
| `social` | read/write (inferred) | [`building_effect`](building_effect.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |

### Signals (시그널)

No emitted signals extracted for this module.

### Downstream Impact (다운스트림 영향)

- No explicit downstream dependencies extracted.

## Entity Data Model (엔티티 데이터 모델)

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `action_history` | read/write (inferred) | Array | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `action_target` | read/write (inferred) | Variant | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `action_timer` | read/write (inferred) | int | Current behavior intent used by schedulers and downstream systems. | Non-negative tick counts. |
| `age_stage` | read/write (inferred) | String enum | Lifecycle progression used for stage-specific behavior and events. | Named categorical states. |
| `cached_path` | read/write (inferred) | Variant | Cached path. | System-defined value domain. |
| `current_action` | read/write (inferred) | String enum | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `emotion_data` | read/write (inferred) | Dictionary / custom data object | Affective state used for behavior modulation and social propagation. | Structured object with nested metrics/axes. |
| `emotions` | read/write (inferred) | Dictionary / custom data object | Affective state used for behavior modulation and social propagation. | System-defined value domain. |
| `energy` | read/write (inferred) | float | Fatigue/rest capacity controlling action readiness. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
| `entity_name` | read/write (inferred) | Variant | Entity name. | System-defined value domain. |
| `get_total_carry` | read/write (inferred) | Variant | Get total carry. | System-defined value domain. |
| `hunger` | read/write (inferred) | float | Nutritional deprivation level driving survival and action priorities. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
| `id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `inventory` | read/write (inferred) | Variant | Inventory. | System-defined value domain. |
| `job` | read/write (inferred) | Variant | Job. | System-defined value domain. |
| `partner_id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `path_index` | read/write (inferred) | Variant | Path index. | System-defined value domain. |
| `position` | read/write (inferred) | Vector2 / Vector2i | World-space location used for movement and proximity checks. | Grid/world vectors. |
| `remove_item` | read/write (inferred) | Variant | Remove item. | System-defined value domain. |
| `settlement_id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `social` | read/write (inferred) | float | Social fulfillment/deficit level affecting mood and stress. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
