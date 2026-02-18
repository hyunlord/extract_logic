---
title: "Emotions System"
description: "Plutchik 8-emotion update engine with 3-layer temporal dynamics."
generated: true
source_files:
  - "scripts/systems/emotion_system.gd"
nav_order: 32
---

# Emotions System

> Plutchik 8-emotion update engine with 3-layer temporal dynamics. Fast (episodic decay) + Slow (mood/baseline, OU process) + Memory trace (long-term scars). Appraisal-based impulse from events. HEXACO personality coupling. References: Plutchik (1980, 2001), Russell (1980), Lazarus (1991), Scherer (2009) Verduyn & Brans (2012), Hatfield et al. (1993)

📄 source: `scripts/systems/emotion_system.gd` | Priority: 32 | Tick interval: 12

## Overview

Plutchik 8-emotion update engine with 3-layer temporal dynamics. Fast (episodic decay) + Slow (mood/baseline, OU process) + Memory trace (long-term scars). Appraisal-based impulse from events. HEXACO personality coupling. References: Plutchik (1980, 2001), Russell (1980), Lazarus (1991), Scherer (2009) Verduyn & Brans (2012), Hatfield et al. (1993)

The extractor found 17 functions, 0 configuration references, and 10 tracked entity fields.

## Configuration

No explicit `GameConfig` references extracted.

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `action_timer` | read | Current behavior/action state. |
| `current_action` | read | Current behavior/action state. |
| `current_goal` | read | current goal |
| `emotion_data` | read | Emotion-related state. |
| `emotions` | read | Emotion-related state. |
| `energy` | read | Energy or fatigue state. |
| `entity_name` | read | entity name |
| `id` | read | Entity identity reference. |
| `personality` | read | Personality and trait state. |
| `settlement_id` | read | Entity identity reference. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 35-40 (6 lines)

### `init(entity_manager: RefCounted)`

**Parameters**: `entity_manager: RefCounted`
**Lines**: 41-46 (6 lines)

### `_load_event_presets()`

**Parameters**: `(none)`
**Lines**: 47-61 (15 lines)

### `_load_decay_parameters()`

**Parameters**: `(none)`
**Lines**: 62-88 (27 lines)

### `queue_event(entity_id: int, event_key: String, overrides: Dictionary = {})`

Queue an emotional event for an entity (called by other systems via SimulationBus)

**Parameters**: `entity_id: int, event_key: String, overrides: Dictionary = {}`
**Lines**: 89-102 (14 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 103-214 (112 lines)

### `_calculate_event_impulse(events: Array, pd: RefCounted, ed: RefCounted)`

**Parameters**: `events: Array, pd: RefCounted, ed: RefCounted`
**Lines**: 215-264 (50 lines)

### `_get_personality_sensitivity(pd: RefCounted)`

**Parameters**: `pd: RefCounted`
**Lines**: 265-287 (23 lines)

### `_get_adjusted_half_life(emo: String, pd: RefCounted, layer: String)`

**Parameters**: `emo: String, pd: RefCounted, layer: String`
**Lines**: 288-298 (11 lines)

### `_get_baseline(emo: String, pd: RefCounted)`

**Parameters**: `emo: String, pd: RefCounted`
**Lines**: 299-315 (17 lines)

### `_get_habituation(ed: RefCounted, category: String)`

**Parameters**: `ed: RefCounted, category: String`
**Lines**: 316-324 (9 lines)

### `_record_habituation(ed: RefCounted, category: String, current_tick: int)`

**Parameters**: `ed: RefCounted, category: String, current_tick: int`
**Lines**: 325-337 (13 lines)

### `_apply_contagion_settlement(members: Array, dt_hours: float)`

Apply emotional contagion within a settlement Scope: settlement-only to avoid O(n²) global computation

**Parameters**: `members: Array, dt_hours: float`
**Lines**: 338-404 (67 lines)

### `_check_mental_break(entity: RefCounted, dt_hours: float, tick: int)`

Check if entity should enter a mental break state

**Parameters**: `entity: RefCounted, dt_hours: float, tick: int`
**Lines**: 405-479 (75 lines)

### `_determine_break_type(ed: RefCounted)`

Determine break type based on dominant negative emotion

**Parameters**: `ed: RefCounted`
**Lines**: 480-506 (27 lines)

### `_create_memory_trace(ed: RefCounted, impulse: Dictionary, event: Dictionary)`

**Parameters**: `ed: RefCounted, impulse: Dictionary, event: Dictionary`
**Lines**: 507-536 (30 lines)

### `_randfn()`

**Parameters**: `(none)`
**Lines**: 541-553 (13 lines)

## Formulas

### Ornstein Uhlenbeck Update

Plutchik 8-emotion update engine with 3-layer temporal dynamics.

```gdscript
Plutchik 8-emotion update engine with 3-layer temporal dynamics.
Fast (episodic decay) + Slow (mood/baseline, OU process) + Memory trace (long-term scars).
Appraisal-based impulse from events. HEXACO personality coupling.
References:
Plutchik (1980, 2001), Russell (1980), Lazarus (1991), Scherer (2009)
Verduyn & Brans (2012), Hatfield et al. (1993)
```

📄 source: `scripts/systems/emotion_system.gd:L3`

### Load Event Presets Line 48

Formula logic extracted from _load_event_presets

```gdscript
var path: String = "res://data/emotions/event_presets.json"
```

📄 source: `scripts/systems/emotion_system.gd:L48`

### Load Decay Parameters  Fast Half Life

Formula logic extracted from _load_decay_parameters

```gdscript
_fast_half_life = dp.get("fast_half_life_hours", {"joy": 0.75, "trust": 2.0, "fear": 0.3, "surprise": 0.05, "sadness": 0.5, "disgust": 0.1, "anger": 0.4, "anticipation": 3.0})
	_slow_half_life = dp.get("slow_half_life_hours", {"joy": 48.0, "trust": 72.0, "fear": 24.0, "surprise": 6.0, "sadness": 120.0, "disgust": 12.0, "anger": 12.0, "anticipation": 36.0})
```

📄 source: `scripts/systems/emotion_system.gd:L64`

### Load Decay Parameters Mt Default Days

Formula logic extracted from _load_decay_parameters

```gdscript
var mt_default_days = float(dp.get("memory_trace_default_half_life_days", 30))
	_memory_trace_default_hl_hours = mt_default_days * 24.0
	var mt_trauma_days = float(dp.get("memory_trace_trauma_half_life_days", 365))
	_memory_trace_trauma_hl_hours = mt_trauma_days * 24.0
```

📄 source: `scripts/systems/emotion_system.gd:L70`

### Load Decay Parameters  Half Life Adjustments

Formula logic extracted from _load_decay_parameters

```gdscript
_half_life_adjustments = dp.get("half_life_adjustments", {})
```

📄 source: `scripts/systems/emotion_system.gd:L85`

### Execute Tick Line 132

Formula logic extracted from execute_tick

```gdscript
var hl: float = _get_adjusted_half_life(emo, pd, "fast")
			var k: float = 0.693147 / hl
```

📄 source: `scripts/systems/emotion_system.gd:L132`

### Execute Tick Line 140

Formula logic extracted from execute_tick

$$ed.fast[emo]  \cdot  e^{-k  \cdot  dt_hours} + emo_impulse$$

```gdscript
ed.fast[emo] = ed.fast[emo] * exp(-k * dt_hours) + emo_impulse
```

📄 source: `scripts/systems/emotion_system.gd:L140`

### Ornstein Uhlenbeck Update

Step 3: Slow layer update (Ornstein-Uhlenbeck mean-reverting process)

```gdscript
Step 3: Slow layer update (Ornstein-Uhlenbeck mean-reverting process)
★ stress shifts OU target baselines
```

📄 source: `scripts/systems/emotion_system.gd:L143`

### Execute Tick Line 155

Formula logic extracted from execute_tick

$$clampf(baseline + mu_shift, 0.0, 30.0)$$

```gdscript
var effective_baseline: float = clampf(baseline + mu_shift, 0.0, 30.0)
			var hl_slow: float = _slow_half_life.get(emo, 48.0)
			var k_slow: float = 0.693147 / hl_slow
			var sigma: float = 0.5  # mood fluctuation
			ed.slow[emo] = effective_baseline + (ed.slow[emo] - effective_baseline) * exp(-k_slow * dt_hours)
			ed.slow[emo] += sigma * sqrt(dt_hours) * _randfn()
			ed.slow[emo] = clampf(ed.slow[emo], 0.0, 30.0)
```

📄 source: `scripts/systems/emotion_system.gd:L155`

### Execute Tick Line 167

Decay formula logic extracted from execute_tick

$$e^{-traces[j].decay_rate  \cdot  dt_hours}$$

```gdscript
traces[j].intensity *= exp(-traces[j].decay_rate * dt_hours)
```

📄 source: `scripts/systems/emotion_system.gd:L167`

### Calculate Event Impulse Line 240

Formula logic extracted from _calculate_event_impulse

$$base_intensity  \cdot  maxf(0.0, g)  \cdot  (1.0 + 0.5  \cdot  n)  \cdot  sens.get("joy", 1.0)$$

```gdscript
impulse["joy"] = base_intensity * maxf(0.0, g) * (1.0 + 0.5 * n) * sens.get("joy", 1.0)
		impulse["sadness"] = base_intensity * maxf(0.0, -g) * (1.0 - c) * sens.get("sadness", 1.0)
		impulse["anger"] = base_intensity * maxf(0.0, -g) * c * maxf(0.0, -a + m) * sens.get("anger", 1.0)
		impulse["fear"] = base_intensity * maxf(0.0, -g) * (1.0 - c) * (0.5 + 0.5 * n) * sens.get("fear", 1.0)
		impulse["disgust"] = base_intensity * (p + 0.7 * m) * (0.5 + 0.5 * maxf(0.0, -g)) * sens.get("disgust", 1.0)
		impulse["surprise"] = base_intensity * n * sens.get("surprise", 1.0)
		impulse["trust"] = base_intensity * maxf(0.0, b) * (1.0 - p) * (1.0 - m) * sens.get("trust", 1.0)
		impulse["anticipation"] = base_intensity * fr * (0.5 + 0.5 * maxf(0.0, g)) * sens.get("anticipation", 1.0)
```

📄 source: `scripts/systems/emotion_system.gd:L240`

### Get Personality Sensitivity Line 277

Formula logic extracted from _get_personality_sensitivity

$$e^{total}$$

```gdscript
result[emo] = exp(total)
```

📄 source: `scripts/systems/emotion_system.gd:L277`

### Get Personality Sensitivity Line 282

Formula logic extracted from _get_personality_sensitivity

$$e^{coeff  \cdot  z}$$

```gdscript
result[emo] = exp(coeff * z)
```

📄 source: `scripts/systems/emotion_system.gd:L282`

### Get Adjusted Half Life Adj

Formula logic extracted from _get_adjusted_half_life

```gdscript
var adj = _half_life_adjustments.get(emo, {})
```

📄 source: `scripts/systems/emotion_system.gd:L290`

### Get Adjusted Half Life Line 296

Formula logic extracted from _get_adjusted_half_life

$$return base  \cdot  e^{coeff  \cdot  z}$$

```gdscript
return base * exp(coeff * z)
```

📄 source: `scripts/systems/emotion_system.gd:L296`

### Get Baseline Line 309

Formula logic extracted from _get_baseline

$$return clampf(base_val + scale_val  \cdot  z, min_val, max_val)$$

```gdscript
return clampf(base_val + scale_val * z, min_val, max_val)
```

📄 source: `scripts/systems/emotion_system.gd:L309`

### Get Habituation Line 322

Formula logic extracted from _get_habituation

$$return exp(-eta  \cdot  float(n_count))$$

```gdscript
return exp(-eta * float(n_count))
```

📄 source: `scripts/systems/emotion_system.gd:L322`

### Apply Contagion Settlement Line 363

Formula logic extracted from _apply_contagion_settlement

$$e^{0.2  \cdot  z_E + 0.1  \cdot  z_A}$$

```gdscript
var susceptibility: float = exp(0.2 * z_E + 0.1 * z_A)
```

📄 source: `scripts/systems/emotion_system.gd:L363`

### Apply Contagion Settlement Line 379

Formula logic extracted from _apply_contagion_settlement

$$sqrt(dx  \cdot  dx + dy  \cdot  dy)$$

```gdscript
var distance: float = sqrt(dx * dx + dy * dy)
			var distance_factor: float = exp(-distance / _contagion_distance_scale)
```

📄 source: `scripts/systems/emotion_system.gd:L379`

### Apply Contagion Settlement Line 392

Formula logic extracted from _apply_contagion_settlement

$$_contagion_kappa[emo]  \cdot  source_val  \cdot  distance_factor  \cdot  relationship  \cdot  susceptibility  \cdot  dt_hours$$

```gdscript
delta[emo] += _contagion_kappa[emo] * source_val * distance_factor * relationship * susceptibility * dt_hours
```

📄 source: `scripts/systems/emotion_system.gd:L392`

### Check Mental Break Line 419

Formula logic extracted from _check_mental_break

$$maxf(0.0, entity.energy - drain  \cdot  dt_hours / 24.0)$$

```gdscript
entity.energy = maxf(0.0, entity.energy - drain * dt_hours / 24.0)
```

📄 source: `scripts/systems/emotion_system.gd:L419`

### Check Mental Break Line 450

Sigmoid probability

$$1.0 / (1.0 + exp(-(ed.stress - threshold) / _break_beta))$$

```gdscript
var p: float = 1.0 / (1.0 + exp(-(ed.stress - threshold) / _break_beta))
```

📄 source: `scripts/systems/emotion_system.gd:L450`

### Create Memory Trace Line 528

Decay formula logic extracted from _create_memory_trace

```gdscript
"decay_rate": base_decay,
```

📄 source: `scripts/systems/emotion_system.gd:L528`

### Box Muller Normal

Box-Muller Transform (randfn replacement)

```gdscript
Box-Muller Transform (randfn replacement)
═══════════════════════════════════════════════════
```

📄 source: `scripts/systems/emotion_system.gd:L534`

### Randfn Line 545

Formula logic extracted from _randfn

```gdscript
var u: float = randf()
	var v: float = randf()
```

📄 source: `scripts/systems/emotion_system.gd:L545`

### Randfn U

Formula logic extracted from _randfn

```gdscript
u = randf()
	var mag: float = sqrt(-2.0 * log(u))
	_spare_normal = mag * sin(TAU * v)
```

📄 source: `scripts/systems/emotion_system.gd:L549`

### Randfn Line 553

Formula logic extracted from _randfn

$$return mag  \cdot  cos(TAU  \cdot  v)$$

```gdscript
return mag * cos(TAU * v)
```

📄 source: `scripts/systems/emotion_system.gd:L553`

## Dependencies

### Imports

- [`emotion_data.gd`](../core/emotion_data.md) - via `preload` (line 10)

### Signals Emitted

- None

### Referenced By

- None
