---
title: "Behavior System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/ai/behavior_system.gd"
nav_order: 20
---

# Behavior System

> No module-level documentation comment was extracted.

📄 source: `scripts/ai/behavior_system.gd` | Priority: 20 | Tick interval: config (GameConfig.BEHAVIOR_TICK_INTERVAL)

## Overview

This page summarizes the extracted structure and runtime behavior for `Behavior`.

The extractor found 22 functions, 4 configuration references, and 21 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `BEHAVIOR_TICK_INTERVAL` | 10 | from GameConfig |
| `BUILDING_TYPES` | { 	"stockpile": {"cost": {"wood": 2.0}, "build_ticks": 36, "radius": 8}, 	"shelter": {"cost": {"wood": 4.0, "stone": 1.0}, "build_ticks": 60, "radius": 0}, 	"campfire": {"cost": {"wood": 1.0}, "build_ticks": 24, "radius": 5}, } | Building type definitions |
| `Biome` | - | GameConfig function reference |
| `ResourceType` | - | GameConfig function reference |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `action_history` | read | Current behavior/action state. |
| `action_target` | read | Current behavior/action state. |
| `action_timer` | read | Current behavior/action state. |
| `age_stage` | read | Age or stage lifecycle state. |
| `cached_path` | read | World-space movement data. |
| `current_action` | read | Current behavior/action state. |
| `emotion_data` | read | Emotion-related state. |
| `emotions` | read | Emotion-related state. |
| `energy` | read | Energy or fatigue state. |
| `entity_name` | read | entity name |
| `get_total_carry` | read | get total carry |
| `hunger` | read | Hunger/food state. |
| `id` | read | Entity identity reference. |
| `inventory` | read | inventory |
| `job` | read | job |
| `partner_id` | read | Entity identity reference. |
| `path_index` | read | World-space movement data. |
| `position` | read | World-space movement data. |
| `remove_item` | read | remove item |
| `settlement_id` | read | Entity identity reference. |
| `social` | read | Social interaction state. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 11-17 (7 lines)

### `init(entity_manager: RefCounted, world_data: RefCounted, rng: RandomNumberGenerator, resource_map: RefCounted = null, building_manager: RefCounted = null, settlement_manager: RefCounted = null)`

Initialize with references (resource_map and building_manager optional for backward compat)

**Parameters**: `entity_manager: RefCounted, world_data: RefCounted, rng: RandomNumberGenerator, resource_map: RefCounted = null, building_manager: RefCounted = null, settlement_manager: RefCounted = null`
**Lines**: 18-26 (9 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 27-50 (24 lines)

### `_evaluate_actions(entity: RefCounted)`

**Parameters**: `entity: RefCounted`
**Lines**: 51-170 (120 lines)

### `_urgency_curve(deficit: float)`

Exponential urgency: higher deficit = much higher urgency

**Parameters**: `deficit: float`
**Lines**: 171-175 (5 lines)

### `_assign_break_action(entity: RefCounted, break_type: String, tick: int)`

멘탈 브레이크 행동 오버라이드

**Parameters**: `entity: RefCounted, break_type: String, tick: int`
**Lines**: 176-210 (35 lines)

### `_assign_action(entity: RefCounted, action: String, tick: int)`

**Parameters**: `entity: RefCounted, action: String, tick: int`
**Lines**: 211-307 (97 lines)

### `_find_random_walkable_nearby(pos: Vector2i, radius: int)`

**Parameters**: `pos: Vector2i, radius: int`
**Lines**: 308-322 (15 lines)

### `_find_food_tile(pos: Vector2i, radius: int)`

**Parameters**: `pos: Vector2i, radius: int`
**Lines**: 323-338 (16 lines)

### `_find_nearest_entity(entity: RefCounted)`

**Parameters**: `entity: RefCounted`
**Lines**: 339-357 (19 lines)

### `_has_nearby_resource(pos: Vector2i, resource_type: int, radius: int)`

**Parameters**: `pos: Vector2i, resource_type: int, radius: int`
**Lines**: 358-367 (10 lines)

### `_find_resource_tile(pos: Vector2i, resource_type: int, radius: int)`

**Parameters**: `pos: Vector2i, resource_type: int, radius: int`
**Lines**: 368-391 (24 lines)

### `_find_nearest_building_in_settlement(pos: Vector2i, btype: String, settlement_id: int, built_only: bool)`

**Parameters**: `pos: Vector2i, btype: String, settlement_id: int, built_only: bool`
**Lines**: 392-412 (21 lines)

### `_count_settlement_buildings(btype: String, settlement_id: int)`

**Parameters**: `btype: String, settlement_id: int`
**Lines**: 413-425 (13 lines)

### `_count_settlement_alive(settlement_id: int)`

**Parameters**: `settlement_id: int`
**Lines**: 426-433 (8 lines)

### `_find_unbuilt_building(entity: RefCounted)`

**Parameters**: `entity: RefCounted`
**Lines**: 434-453 (20 lines)

### `_should_place_building(entity: RefCounted)`

**Parameters**: `entity: RefCounted`
**Lines**: 454-474 (21 lines)

### `_builder_can_afford_anything(entity: RefCounted)`

**Parameters**: `entity: RefCounted`
**Lines**: 475-484 (10 lines)

### `_try_place_building(entity: RefCounted)`

**Parameters**: `entity: RefCounted`
**Lines**: 485-523 (39 lines)

### `_can_afford_building(entity: RefCounted, cost: Dictionary)`

**Parameters**: `entity: RefCounted, cost: Dictionary`
**Lines**: 524-541 (18 lines)

### `_consume_building_cost(entity: RefCounted, cost: Dictionary)`

**Parameters**: `entity: RefCounted, cost: Dictionary`
**Lines**: 542-559 (18 lines)

### `_find_building_site(pos: Vector2i)`

**Parameters**: `pos: Vector2i`
**Lines**: 560-570 (11 lines)

## Formulas

### Evaluate Actions Line 60

Formula logic extracted from _evaluate_actions

$$0.3 + _rng.randf()  \cdot  0.1$$

```gdscript
"wander": 0.3 + _rng.randf() * 0.1,
			"rest": _urgency_curve(energy_deficit) * 1.2,
			"socialize": _urgency_curve(social_deficit) * 0.8,
```

📄 source: `scripts/ai/behavior_system.gd:L60`

### Evaluate Actions Line 68

Formula logic extracted from _evaluate_actions

$$0.3 + _rng.randf()  \cdot  0.1$$

```gdscript
"wander": 0.3 + _rng.randf() * 0.1,
			"rest": _urgency_curve(energy_deficit) * 1.2,
			"socialize": _urgency_curve(social_deficit) * 0.8,
			"gather_food": _urgency_curve(hunger_deficit) * 1.5 * 0.4,
```

📄 source: `scripts/ai/behavior_system.gd:L68`

### Evaluate Actions Line 74

Formula logic extracted from _evaluate_actions

$$(0.3 + _rng.randf()  \cdot  0.1)  \cdot  0.3$$

```gdscript
child_scores["gather_wood"] = (0.3 + _rng.randf() * 0.1) * 0.3
```

📄 source: `scripts/ai/behavior_system.gd:L74`

### Evaluate Actions Line 78

Formula logic extracted from _evaluate_actions

$$0.2 + _rng.randf()  \cdot  0.1$$

```gdscript
"wander": 0.2 + _rng.randf() * 0.1,
		"gather_food": _urgency_curve(hunger_deficit) * 1.5,
		"rest": _urgency_curve(energy_deficit) * 1.2,
		"socialize": _urgency_curve(social_deficit) * 0.8,
```

📄 source: `scripts/ai/behavior_system.gd:L78`

### Evaluate Actions Line 92

Partner is far, want to visit

$$0.4 + _rng.randf()  \cdot  0.1$$

```gdscript
scores["visit_partner"] = 0.4 + _rng.randf() * 0.1
```

📄 source: `scripts/ai/behavior_system.gd:L92`

### Evaluate Actions Line 106

Formula logic extracted from _evaluate_actions

$$0.3 + _rng.randf()  \cdot  0.1$$

```gdscript
scores["gather_wood"] = 0.3 + _rng.randf() * 0.1
```

📄 source: `scripts/ai/behavior_system.gd:L106`

### Evaluate Actions Line 108

Formula logic extracted from _evaluate_actions

$$0.2 + _rng.randf()  \cdot  0.1$$

```gdscript
scores["gather_stone"] = 0.2 + _rng.randf() * 0.1
```

📄 source: `scripts/ai/behavior_system.gd:L108`

### Evaluate Actions Line 133

Formula logic extracted from _evaluate_actions

$$0.4 + _rng.randf()  \cdot  0.1$$

```gdscript
scores["build"] = 0.4 + _rng.randf() * 0.1
```

📄 source: `scripts/ai/behavior_system.gd:L133`

### Evaluate Actions Line 135

Formula logic extracted from _evaluate_actions

$$0.4 + _rng.randf()  \cdot  0.1$$

```gdscript
scores["build"] = 0.4 + _rng.randf() * 0.1
```

📄 source: `scripts/ai/behavior_system.gd:L135`

### Urgency Curve Line 172

Formula logic extracted from _urgency_curve

$$return pow(deficit, 2.0)$$

```gdscript
return pow(deficit, 2.0)
```

📄 source: `scripts/ai/behavior_system.gd:L172`

### Find Nearest Entity Line 347

Formula logic extracted from _find_nearest_entity

$$absi(other.position.x - entity.position.x) + absi(other.position.y - entity.position.y)$$

```gdscript
var dist: int = absi(other.position.x - entity.position.x) + absi(other.position.y - entity.position.y)
```

📄 source: `scripts/ai/behavior_system.gd:L347`

### Find Nearest Building In Settlement Line 406

Formula logic extracted from _find_nearest_building_in_settlement

$$absi(building.tile_x - pos.x) + absi(building.tile_y - pos.y)$$

```gdscript
var dist: int = absi(building.tile_x - pos.x) + absi(building.tile_y - pos.y)
```

📄 source: `scripts/ai/behavior_system.gd:L406`

### Find Unbuilt Building Line 447

Formula logic extracted from _find_unbuilt_building

$$float(absi(building.tile_x - entity.position.x) + absi(building.tile_y - entity.position.y))$$

```gdscript
var dist: float = float(absi(building.tile_x - entity.position.x) + absi(building.tile_y - entity.position.y))
```

📄 source: `scripts/ai/behavior_system.gd:L447`

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
