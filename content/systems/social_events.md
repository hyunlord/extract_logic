---
title: "Social Events System"
description: "Drives relationship interactions using chunk-based proximity."
generated: true
source_files:
  - "scripts/systems/social_event_system.gd"
nav_order: 37
---

# Social Events System

> Drives relationship interactions using chunk-based proximity. Only checks entities in same chunk (16x16 tiles).

📄 source: `scripts/systems/social_event_system.gd` | Priority: 37 | Tick interval: 30

## Overview

Drives relationship interactions using chunk-based proximity. Only checks entities in same chunk (16x16 tiles).

The extractor found 9 functions, 0 configuration references, and 3 tracked entity fields.

## Configuration

No explicit `GameConfig` references extracted.

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `current_action` | read | Current behavior/action state. |
| `id` | read | Entity identity reference. |
| `position` | read | World-space movement data. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 13-18 (6 lines)

### `init(entity_manager: RefCounted, relationship_manager: RefCounted, rng: RandomNumberGenerator)`

**Parameters**: `entity_manager: RefCounted, relationship_manager: RefCounted, rng: RandomNumberGenerator`
**Lines**: 19-24 (6 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 25-31 (7 lines)

### `_process_social_events(tick: int)`

**Parameters**: `tick: int`
**Lines**: 32-68 (37 lines)

### `_trigger_event(a: RefCounted, b: RefCounted, tick: int)`

**Parameters**: `a: RefCounted, b: RefCounted, tick: int`
**Lines**: 69-120 (52 lines)

### `_can_flirt(a: RefCounted, b: RefCounted, rel: RefCounted)`

**Parameters**: `a: RefCounted, b: RefCounted, rel: RefCounted`
**Lines**: 121-135 (15 lines)

### `_weighted_random(events: Array)`

**Parameters**: `events: Array`
**Lines**: 136-150 (15 lines)

### `_apply_event(event_name: String, a: RefCounted, b: RefCounted, rel: RefCounted, tick: int)`

**Parameters**: `event_name: String, a: RefCounted, b: RefCounted, rel: RefCounted, tick: int`
**Lines**: 151-228 (78 lines)

### `_handle_proposal(a: RefCounted, b: RefCounted, rel: RefCounted, tick: int)`

**Parameters**: `a: RefCounted, b: RefCounted, rel: RefCounted, tick: int`
**Lines**: 229-260 (32 lines)

## Formulas

### Doc Line 106

PROPOSAL: romantic + romantic_interest >= 80 + interactions >= 20

$$80 + interactions \ge  20$$

```gdscript
PROPOSAL: romantic + romantic_interest >= 80 + interactions >= 20
```

📄 source: `scripts/systems/social_event_system.gd:L106`

### Weighted Random Line 142

Formula logic extracted from _weighted_random

$$_rng.randf()  \cdot  total$$

```gdscript
var roll: float = _rng.randf() * total
```

📄 source: `scripts/systems/social_event_system.gd:L142`

### Apply Event Line 203

Formula logic extracted from _apply_event

$$clampf(rel.affinity / 100.0, 0.0, 1.0)$$

```gdscript
var bond: float = clampf(rel.affinity / 100.0, 0.0, 1.0)
```

📄 source: `scripts/systems/social_event_system.gd:L203`

### Doc Line 230

Acceptance probability = (romantic_interest/100) * compatibility

$$(romantic_interest/100)  \cdot  compatibility$$

```gdscript
Acceptance probability = (romantic_interest/100) * compatibility
```

📄 source: `scripts/systems/social_event_system.gd:L230`

## Dependencies

### Imports

- [`personality_system.gd`](../core/personality_system.md) - via `preload` (line 2)

### Signals Emitted

- `couple_formed` - parameters: `entity_a_id: int, entity_a_name: String, entity_b_id: int, entity_b_name: String, tick: int` (line 250)
- `ui_notification` - parameters: `message: String, type: String` (line 248)

### Referenced By

- None
