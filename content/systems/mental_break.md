---
title: "Mental Break System"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/mental_break_system.gd"
nav_order: 35
---

# Mental Break System

> No module-level documentation comment was extracted.

📄 source: `scripts/systems/mental_break_system.gd` | Priority: 35 | Tick interval: 1

## Overview

This page summarizes the extracted structure and runtime behavior for `Mental Break`.

The extractor found 10 functions, 0 configuration references, and 5 tracked entity fields.

## Configuration

No explicit `GameConfig` references extracted.

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `emotion_data` | read | Emotion-related state. |
| `energy` | read | Energy or fatigue state. |
| `entity_name` | read | entity name |
| `hunger` | read | Hunger/food state. |
| `personality` | read | Personality and trait state. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 22-28 (7 lines)

### `init(entity_manager: RefCounted, rng: RandomNumberGenerator)`

Initialize with references

**Parameters**: `entity_manager: RefCounted, rng: RandomNumberGenerator`
**Lines**: 29-35 (7 lines)

### `_load_break_definitions()`

Load break definitions from JSON

**Parameters**: `(none)`
**Lines**: 36-54 (19 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 55-74 (20 lines)

### `_check_mental_break(entity: RefCounted, ed: RefCounted, tick: int)`

Per-tick: 발동 확률 체크

**Parameters**: `entity: RefCounted, ed: RefCounted, tick: int`
**Lines**: 75-84 (10 lines)

### `_calc_threshold(entity: RefCounted, ed: RefCounted)`

역치 계산 (Connor-Davidson resilience + HEXACO)

**Parameters**: `entity: RefCounted, ed: RefCounted`
**Lines**: 85-111 (27 lines)

### `_select_break_type(entity: RefCounted)`

유형 선택 (HEXACO 가중치 기반 가중 랜덤)

**Parameters**: `entity: RefCounted`
**Lines**: 125-158 (34 lines)

### `_trigger_break(entity: RefCounted, ed: RefCounted, tick: int)`

브레이크 발동

**Parameters**: `entity: RefCounted, ed: RefCounted, tick: int`
**Lines**: 159-176 (18 lines)

### `_tick_active_break(entity: RefCounted, ed: RefCounted)`

진행 중인 브레이크 틱 처리

**Parameters**: `entity: RefCounted, ed: RefCounted`
**Lines**: 177-183 (7 lines)

### `_end_break(entity: RefCounted, ed: RefCounted)`

브레이크 종료 → 카타르시스 + Shaken 설정

**Parameters**: `entity: RefCounted, ed: RefCounted`
**Lines**: 184-217 (34 lines)

## Formulas

### Calc Threshold Threshold

Formula logic extracted from _calc_threshold

$$(1.0 + 0.40  \cdot  (ed.resilience - 0.5)  \cdot  2.0)$$

```gdscript
threshold *= (1.0 + 0.40 * (ed.resilience - 0.5) * 2.0)
	threshold *= (1.0 + 0.25 * (C - 0.5) * 2.0)
	threshold *= (1.0 - 0.35 * (E - 0.5) * 2.0)
	threshold *= (1.0 - 0.25 * (ed.allostatic / 100.0))
	threshold *= (0.85 + 0.15 * entity.energy)
	threshold *= (0.85 + 0.15 * entity.hunger)
	threshold = clampf(threshold, THRESHOLD_MIN, THRESHOLD_MAX)
```

📄 source: `scripts/systems/mental_break_system.gd:L94`

### Calc Break Chance Line 116

Formula logic extracted from _calc_break_chance

$$clampf((stress - threshold) / BREAK_SCALE, 0.0, BREAK_CAP_PER_TICK)$$

```gdscript
var p: float = clampf((stress - threshold) / BREAK_SCALE, 0.0, BREAK_CAP_PER_TICK)
```

📄 source: `scripts/systems/mental_break_system.gd:L116`

### Select Break Type Line 140

Formula logic extracted from _select_break_type

$$lerpf(1.0, 1.0 + axis_weight, axis_val)$$

```gdscript
w *= lerpf(1.0, 1.0 + axis_weight, axis_val)
```

📄 source: `scripts/systems/mental_break_system.gd:L140`

### Select Break Type Line 142

Formula logic extracted from _select_break_type

$$lerpf(1.0, 1.0 + absf(axis_weight), 1.0 - axis_val)$$

```gdscript
w *= lerpf(1.0, 1.0 + absf(axis_weight), 1.0 - axis_val)
```

📄 source: `scripts/systems/mental_break_system.gd:L142`

### Select Break Type Line 149

Formula logic extracted from _select_break_type

$$_rng.randf()  \cdot  total$$

```gdscript
var roll: float = _rng.randf() * total
```

📄 source: `scripts/systems/mental_break_system.gd:L149`

### Trigger Break Duration

Formula logic extracted from _trigger_break

```gdscript
var variance: int = bdef.get("duration_variance_ticks", 4)
	var duration: float = float(base + _rng.randi() % (variance + 1))
	duration = clampf(duration, 1.0, 168.0)
```

📄 source: `scripts/systems/mental_break_system.gd:L164`

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
