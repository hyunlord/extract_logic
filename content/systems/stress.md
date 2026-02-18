---
title: "Stress System"
description: "Stress System — Phase 1 Pipeline Lazarus & Folkman (1984) Transactional Model Selye (1956) GAS reserve McEwen (1998) Allostatic Load Hobfoll (1989) COR loss aversion Yerkes & Dodson (1908) Eustress efficiency"
generated: true
source_files:
  - "scripts/systems/stress_system.gd"
nav_order: 34
---

# Stress System

> Stress System — Phase 1 Pipeline Lazarus & Folkman (1984) Transactional Model Selye (1956) GAS reserve McEwen (1998) Allostatic Load Hobfoll (1989) COR loss aversion Yerkes & Dodson (1908) Eustress efficiency

📄 source: `scripts/systems/stress_system.gd` | Priority: 34 | Tick interval: 2

## Overview

Stress System — Phase 1 Pipeline Lazarus & Folkman (1984) Transactional Model Selye (1956) GAS reserve McEwen (1998) Allostatic Load Hobfoll (1989) COR loss aversion Yerkes & Dodson (1908) Eustress efficiency

The extractor found 24 functions, 0 configuration references, and 9 tracked entity fields.

## Configuration

No explicit `GameConfig` references extracted.

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `active_traits` | read | Personality and trait state. |
| `current_action` | read | Current behavior/action state. |
| `emotion_data` | read | Emotion-related state. |
| `energy` | read | Energy or fatigue state. |
| `entity_name` | read | entity name |
| `hunger` | read | Hunger/food state. |
| `personality` | read | Personality and trait state. |
| `settlement_id` | read | Entity identity reference. |
| `social` | read | Social interaction state. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 44-49 (6 lines)

### `init(entity_manager: RefCounted)`

**Parameters**: `entity_manager: RefCounted`
**Lines**: 50-54 (5 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 55-65 (11 lines)

### `_update_entity_stress(entity: RefCounted, is_sleeping: bool, is_safe: bool)`

**Parameters**: `entity: RefCounted, is_sleeping: bool, is_safe: bool`
**Lines**: 66-123 (58 lines)

### `_calc_appraisal_scale(entity: RefCounted, pd, ed)`

**Parameters**: `entity: RefCounted, pd, ed`
**Lines**: 124-154 (31 lines)

### `_calc_continuous_stressors(entity: RefCounted, appraisal_scale: float, breakdown: Dictionary)`

**Parameters**: `entity: RefCounted, appraisal_scale: float, breakdown: Dictionary`
**Lines**: 155-182 (28 lines)

### `_process_stress_traces(ed, breakdown: Dictionary)`

**Parameters**: `ed, breakdown: Dictionary`
**Lines**: 183-207 (25 lines)

### `_calc_emotion_contribution(ed, breakdown: Dictionary)`

**Parameters**: `ed, breakdown: Dictionary`
**Lines**: 208-234 (27 lines)

### `_calc_recovery(entity: RefCounted, ed, pd, is_sleeping: bool, is_safe: bool, breakdown: Dictionary)`

**Parameters**: `entity: RefCounted, ed, pd, is_sleeping: bool, is_safe: bool, breakdown: Dictionary`
**Lines**: 235-256 (22 lines)

### `_update_reserve(ed, pd, is_sleeping: bool)`

**Parameters**: `ed, pd, is_sleeping: bool`
**Lines**: 257-278 (22 lines)

### `_update_allostatic(ed)`

**Parameters**: `ed`
**Lines**: 279-289 (11 lines)

### `_update_stress_state(ed)`

**Parameters**: `ed`
**Lines**: 290-301 (12 lines)

### `_update_resilience(entity: RefCounted, ed, pd)`

**Parameters**: `entity: RefCounted, ed, pd`
**Lines**: 302-333 (32 lines)

### `_apply_stress_to_emotions(ed)`

**Parameters**: `ed`
**Lines**: 334-352 (19 lines)

### `_calc_support_score(entity: RefCounted)`

**Parameters**: `entity: RefCounted`
**Lines**: 353-372 (20 lines)

### `get_work_efficiency(ed)`

**Parameters**: `ed`
**Lines**: 373-388 (16 lines)

### `_load_stressor_defs()`

**Parameters**: `(none)`
**Lines**: 406-432 (27 lines)

### `inject_event(entity, event_id: String, context: Dictionary = {})`

학술: Lazarus (1984) 개인별 appraisal HEXACO: 같은 사건도 성격에 따라 stress 강도가 다름 COR (Hobfoll 1989): is_loss=true → 2.5배

**Parameters**: `entity, event_id: String, context: Dictionary = {}`
**Lines**: 433-494 (62 lines)

### `_calc_personality_scale(entity, p_mods: Dictionary)`

**Parameters**: `entity, p_mods: Dictionary`
**Lines**: 495-538 (44 lines)

### `_calc_relationship_scale(context: Dictionary, r_def: Dictionary)`

**Parameters**: `context: Dictionary, r_def: Dictionary`
**Lines**: 539-550 (12 lines)

### `_calc_context_scale(context: Dictionary, c_mods: Dictionary)`

**Parameters**: `context: Dictionary, c_mods: Dictionary`
**Lines**: 551-558 (8 lines)

### `_entity_has_trait(entity, trait_id: String)`

**Parameters**: `entity, trait_id: String`
**Lines**: 559-565 (7 lines)

### `_inject_emotions(ed, emo_inject: Dictionary, scale: float)`

**Parameters**: `ed, emo_inject: Dictionary, scale: float`
**Lines**: 566-583 (18 lines)

### `_debug_log(entity: RefCounted, ed, delta: float)`

**Parameters**: `entity: RefCounted, ed, delta: float`
**Lines**: 584-598 (15 lines)

## Formulas

### Update Entity Stress Line 88

6) 최종 업데이트

$$continuous_input + trace_input + emotion_input - recovery$$

```gdscript
var delta: float = continuous_input + trace_input + emotion_input - recovery
```

📄 source: `scripts/systems/stress_system.gd:L88`

### Update Entity Stress Line 92

Formula logic extracted from _update_entity_stress

$$clampf(ed.stress + delta, 0.0, STRESS_CLAMP_MAX)$$

```gdscript
ed.stress = clampf(ed.stress + delta, 0.0, STRESS_CLAMP_MAX)
```

📄 source: `scripts/systems/stress_system.gd:L92`

### Calc Appraisal Scale Line 131

Formula logic extracted from _calc_appraisal_scale

$$0.45  \cdot  (1.0 - hunger) + 0.35  \cdot  (1.0 - energy) + 0.20  \cdot  (1.0 - social)$$

```gdscript
var D_dep: float = 0.45 * (1.0 - hunger) + 0.35 * (1.0 - energy) + 0.20 * (1.0 - social)
	var D: float = clampf(0.30 * D_dep + 0.40 * threat + 0.20 * conflict, 0.0, 1.0)
```

📄 source: `scripts/systems/stress_system.gd:L131`

### Calc Appraisal Scale Line 134

Formula logic extracted from _calc_appraisal_scale

$$0.5  \cdot  hunger + 0.5  \cdot  energy$$

```gdscript
var R_physical: float = 0.5 * hunger + 0.5 * energy
	var R_safety: float = 1.0 - threat
```

📄 source: `scripts/systems/stress_system.gd:L134`

### Calc Appraisal Scale Line 137

Formula logic extracted from _calc_appraisal_scale

$$clampf(0.30  \cdot  R_physical + 0.30  \cdot  R_safety + 0.25  \cdot  R_support + 0.15  \cdot  0.5, 0.0, 1.0)$$

```gdscript
var R: float = clampf(0.30 * R_physical + 0.30 * R_safety + 0.25 * R_support + 0.15 * 0.5, 0.0, 1.0)
```

📄 source: `scripts/systems/stress_system.gd:L137`

### Calc Appraisal Scale Appraisal

Appraisal formula logic extracted from _calc_appraisal_scale

$$D  \cdot  (1.0 + 0.55  \cdot  (E_axis - 0.5)  \cdot  2.0 + 0.25  \cdot  (fear_val / 100.0) - 0.15  \cdot  (trust_val / 100.0))$$

```gdscript
var threat_appraisal: float = D * (1.0 + 0.55 * (E_axis - 0.5) * 2.0 + 0.25 * (fear_val / 100.0) - 0.15 * (trust_val / 100.0))
```

📄 source: `scripts/systems/stress_system.gd:L143`

### Calc Appraisal Scale Appraisal

Appraisal formula logic extracted from _calc_appraisal_scale

$$R  \cdot  (1.0 + 0.35  \cdot  (C_axis - 0.5)  \cdot  2.0 + 0.20  \cdot  (O_axis - 0.5)  \cdot  2.0 + 0.20  \cdot  reserve_ratio)$$

```gdscript
var coping_appraisal: float = R * (1.0 + 0.35 * (C_axis - 0.5) * 2.0 + 0.20 * (O_axis - 0.5) * 2.0 + 0.20 * reserve_ratio)
```

📄 source: `scripts/systems/stress_system.gd:L148`

### Calc Appraisal Scale Line 151

Formula logic extracted from _calc_appraisal_scale

$$return clampf(1.0 + 0.8  \cdot  imbalance, 0.7, 1.9)$$

```gdscript
return clampf(1.0 + 0.8 * imbalance, 0.7, 1.9)
```

📄 source: `scripts/systems/stress_system.gd:L151`

### Calc Continuous Stressors Appraisal

Appraisal formula logic extracted from _calc_continuous_stressors

$$clampf((0.35 - hunger) / 0.35, 0.0, 1.0)$$

```gdscript
var h_def: float = clampf((0.35 - hunger) / 0.35, 0.0, 1.0)
	var s_hunger: float = (3.0 * h_def + 9.0 * h_def * h_def) * appraisal_scale
```

📄 source: `scripts/systems/stress_system.gd:L161`

### Calc Continuous Stressors Appraisal

Appraisal formula logic extracted from _calc_continuous_stressors

$$clampf((0.40 - energy) / 0.40, 0.0, 1.0)$$

```gdscript
var e_def: float = clampf((0.40 - energy) / 0.40, 0.0, 1.0)
	var s_energy: float = (2.0 * e_def + 10.0 * e_def * e_def) * appraisal_scale
```

📄 source: `scripts/systems/stress_system.gd:L167`

### Calc Continuous Stressors Appraisal

Appraisal formula logic extracted from _calc_continuous_stressors

$$clampf((0.25 - social) / 0.25, 0.0, 1.0)$$

```gdscript
var soc_def: float = clampf((0.25 - social) / 0.25, 0.0, 1.0)
	var s_social: float = 2.0 * soc_def * soc_def * appraisal_scale
```

📄 source: `scripts/systems/stress_system.gd:L173`

### Process Stress Traces Line 192

Decay formula logic extracted from _process_stress_traces

```gdscript
var decay: float = trace.get("decay_rate", 0.05)
		trace["per_tick"] = contribution * (1.0 - decay)
```

📄 source: `scripts/systems/stress_system.gd:L192`

### Calc Emotion Contribution Line 224

Formula logic extracted from _calc_emotion_contribution

$$clampf(-valence / 100.0, 0.0, 1.0)$$

```gdscript
var neg: float = clampf(-valence / 100.0, 0.0, 1.0)
	var ar: float = clampf(arousal / 100.0, 0.0, 1.0)
	var va_contrib: float = VA_GAMMA * ar * neg
```

📄 source: `scripts/systems/stress_system.gd:L224`

### Calc Recovery Line 247

Decay formula logic extracted from _calc_recovery

$$1.0 + 0.10  \cdot  (resilience - 0.5)  \cdot  2.0$$

```gdscript
decay *= 1.0 + 0.10 * (resilience - 0.5) * 2.0
```

📄 source: `scripts/systems/stress_system.gd:L247`

### Update Reserve Line 260

Formula logic extracted from _update_reserve

$$maxf(0.0, (ed.stress - 150.0) / 350.0)  \cdot  (0.7 + 0.6  \cdot  (1.0 - resilience))$$

```gdscript
var drain: float = maxf(0.0, (ed.stress - 150.0) / 350.0) * (0.7 + 0.6 * (1.0 - resilience))
	var recover_base: float = 0.4 + 0.6 * resilience
	var recover: float = recover_base * (1.0 if is_sleeping else 0.15)
```

📄 source: `scripts/systems/stress_system.gd:L260`

### Update Reserve Line 264

Formula logic extracted from _update_reserve

$$clampf(ed.reserve - drain + recover, 0.0, RESERVE_MAX)$$

```gdscript
ed.reserve = clampf(ed.reserve - drain + recover, 0.0, RESERVE_MAX)
```

📄 source: `scripts/systems/stress_system.gd:L264`

### Update Allostatic Line 281

Formula logic extracted from _update_allostatic

$$ALLO_RATE  \cdot  maxf(0.0, ed.stress - ALLO_STRESS_THRESHOLD) / ALLO_STRESS_THRESHOLD$$

```gdscript
var allo_inc: float = ALLO_RATE * maxf(0.0, ed.stress - ALLO_STRESS_THRESHOLD) / ALLO_STRESS_THRESHOLD
```

📄 source: `scripts/systems/stress_system.gd:L281`

### Update Allostatic Line 283

Formula logic extracted from _update_allostatic

$$clampf(ed.allostatic + allo_inc, 0.0, 100.0)$$

```gdscript
ed.allostatic = clampf(ed.allostatic + allo_inc, 0.0, 100.0)
```

📄 source: `scripts/systems/stress_system.gd:L283`

### Update Allostatic Line 286

Formula logic extracted from _update_allostatic

$$clampf(ed.allostatic - ALLO_RECOVERY_RATE, 0.0, 100.0)$$

```gdscript
ed.allostatic = clampf(ed.allostatic - ALLO_RECOVERY_RATE, 0.0, 100.0)
```

📄 source: `scripts/systems/stress_system.gd:L286`

### Update Resilience Line 323

Formula logic extracted from _update_resilience

$$- 0.30  \cdot  (ed.allostatic / 100.0))$$

```gdscript
- 0.30 * (ed.allostatic / 100.0))
```

📄 source: `scripts/systems/stress_system.gd:L323`

### Update Resilience Line 327

Formula logic extracted from _update_resilience

$$clampf((0.3 - energy) / 0.3, 0.0, 0.3) + clampf((0.3 - hunger) / 0.3, 0.0, 0.2)$$

```gdscript
var fatigue_penalty: float = clampf((0.3 - energy) / 0.3, 0.0, 0.3) + clampf((0.3 - hunger) / 0.3, 0.0, 0.2)
	r -= 0.20 * fatigue_penalty
```

📄 source: `scripts/systems/stress_system.gd:L327`

### Update Resilience Line 330

Formula logic extracted from _update_resilience

```gdscript
ed.resilience = clampf(r, 0.05, 1.0)
```

📄 source: `scripts/systems/stress_system.gd:L330`

### Apply Stress To Emotions Line 335

Formula logic extracted from _apply_stress_to_emotions

$$clampf((ed.stress - 100.0) / 400.0, 0.0, 1.0)$$

```gdscript
var s1: float = clampf((ed.stress - 100.0) / 400.0, 0.0, 1.0)
	var s2: float = clampf((ed.stress - 300.0) / 400.0, 0.0, 1.0)
	var allo_ratio: float = ed.allostatic / 100.0
```

📄 source: `scripts/systems/stress_system.gd:L335`

### Apply Stress To Emotions Line 339

Formula logic extracted from _apply_stress_to_emotions

$$ed.set_meta("stress_mu_sadness", 6.0  \cdot  s1 + 10.0  \cdot  allo_ratio)$$

```gdscript
ed.set_meta("stress_mu_sadness", 6.0 * s1 + 10.0 * allo_ratio)
	ed.set_meta("stress_mu_anger", 4.0 * s1 + 8.0 * allo_ratio)
	ed.set_meta("stress_mu_fear", 5.0 * s1 + 12.0 * allo_ratio)
	ed.set_meta("stress_mu_joy", -(5.0 * s1 + 12.0 * allo_ratio))
	ed.set_meta("stress_mu_trust", -(4.0 * s1 + 10.0 * allo_ratio))
```

📄 source: `scripts/systems/stress_system.gd:L339`

### Apply Stress To Emotions Line 348

Formula logic extracted from _apply_stress_to_emotions

$$1.0 + 0.9  \cdot  allo_ratio  \cdot  (2.0 if allo_ratio > 0.6 else 1.0)$$

```gdscript
var blunt_denom: float = 1.0 + 0.9 * allo_ratio * (2.0 if allo_ratio > 0.6 else 1.0)
	ed.set_meta("stress_blunt_mult", 1.0 / blunt_denom)
```

📄 source: `scripts/systems/stress_system.gd:L348`

### Calc Support Score Line 369

Formula logic extracted from _calc_support_score

$$return clampf(0.65  \cdot  strong + 0.35  \cdot  (1.0 - e^{-weak_sum / 1.5}), 0.0, 1.0)$$

```gdscript
return clampf(0.65 * strong + 0.35 * (1.0 - exp(-weak_sum / 1.5)), 0.0, 1.0)
```

📄 source: `scripts/systems/stress_system.gd:L369`

### Get Work Efficiency Perf

Formula logic extracted from get_work_efficiency

$$1.09 - 0.0004  \cdot  (s - 150.0)$$

```gdscript
perf = 1.09 - 0.0004 * (s - 150.0)
```

📄 source: `scripts/systems/stress_system.gd:L379`

### Get Work Efficiency Perf

Formula logic extracted from get_work_efficiency

$$1.01 - 0.0012  \cdot  (s - 350.0)$$

```gdscript
perf = 1.01 - 0.0012 * (s - 350.0)
```

📄 source: `scripts/systems/stress_system.gd:L381`

### Get Work Efficiency Line 385

Formula logic extracted from get_work_efficiency

```gdscript
return clampf(perf, 0.35, 1.10)
```

📄 source: `scripts/systems/stress_system.gd:L385`

### Inject Stress Event Appraisal

Decay formula logic extracted from inject_stress_event

```gdscript
per_tick: float = 0.0, decay_rate: float = 0.05,
		is_loss: bool = false, appraisal_scale: float = 1.0) -> void:
```

📄 source: `scripts/systems/stress_system.gd:L390`

### Inject Stress Event Line 395

Formula logic extracted from inject_stress_event

$$clampf(ed.stress + final_instant, 0.0, STRESS_CLAMP_MAX)$$

```gdscript
ed.stress = clampf(ed.stress + final_instant, 0.0, STRESS_CLAMP_MAX)
```

📄 source: `scripts/systems/stress_system.gd:L395`

### Inject Stress Event Line 401

Decay formula logic extracted from inject_stress_event

```gdscript
"decay_rate": decay_rate,
```

📄 source: `scripts/systems/stress_system.gd:L401`

### Inject Event Decay Rate

Decay formula logic extracted from inject_event

```gdscript
var decay_rate = float(sdef.get("base_decay_rate", 0.05))
```

📄 source: `scripts/systems/stress_system.gd:L448`

### Inject Event Line 472

7) Stress 주입

$$clampf(ed.stress + final_instant, 0.0, STRESS_CLAMP_MAX)$$

```gdscript
ed.stress = clampf(ed.stress + final_instant, 0.0, STRESS_CLAMP_MAX)
```

📄 source: `scripts/systems/stress_system.gd:L472`

### Inject Event Line 478

Decay formula logic extracted from inject_event

```gdscript
"decay_rate": decay_rate,
```

📄 source: `scripts/systems/stress_system.gd:L478`

### Calc Personality Scale Line 536

Formula logic extracted from _calc_personality_scale

```gdscript
return clampf(scale, 0.05, 4.0)
```

📄 source: `scripts/systems/stress_system.gd:L536`

### Calc Relationship Scale Line 547

Formula logic extracted from _calc_relationship_scale

$$return clampf(min_m + (max_m - min_m)  \cdot  bond, min_m, max_m)$$

```gdscript
return clampf(min_m + (max_m - min_m) * bond, min_m, max_m)
```

📄 source: `scripts/systems/stress_system.gd:L547`

### Calc Context Scale Line 556

Formula logic extracted from _calc_context_scale

```gdscript
return clampf(scale, 0.1, 5.0)
```

📄 source: `scripts/systems/stress_system.gd:L556`

### Inject Emotions Line 577

Formula logic extracted from _inject_emotions

$$clampf(ed.fast.get(emo_name, 0.0) + raw_val, 0.0, 100.0)$$

```gdscript
ed.fast[emo_name] = clampf(ed.fast.get(emo_name, 0.0) + raw_val, 0.0, 100.0)
```

📄 source: `scripts/systems/stress_system.gd:L577`

### Inject Emotions Line 580

Formula logic extracted from _inject_emotions

$$clampf(ed.slow.get(emo_name, 0.0) + raw_val, -50.0, 100.0)$$

```gdscript
ed.slow[emo_name] = clampf(ed.slow.get(emo_name, 0.0) + raw_val, -50.0, 100.0)
```

📄 source: `scripts/systems/stress_system.gd:L580`

## Dependencies

### Imports

- None

### Signals Emitted

- None

### Referenced By

- None
