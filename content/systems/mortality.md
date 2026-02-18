---
title: "Mortality System"
description: "Siler(1979) bathtub-curve mortality model."
generated: true
source_files:
  - "scripts/systems/mortality_system.gd"
nav_order: 49
---

# Mortality System

> Siler(1979) bathtub-curve mortality model. μ(x) = a₁·e^{-b₁·x} + a₂ + a₃·e^{b₃·x} Birthday-based distributed checks (not every-tick iteration). Infants (0-1yr) checked monthly for higher resolution.

📄 source: `scripts/systems/mortality_system.gd` | Priority: 49 | Tick interval: 1

## Overview

Siler(1979) bathtub-curve mortality model. μ(x) = a₁·e^{-b₁·x} + a₂ + a₃·e^{b₃·x} Birthday-based distributed checks (not every-tick iteration). Infants (0-1yr) checked monthly for higher resolution.

The extractor found 17 functions, 1 configuration references, and 7 tracked entity fields.

## Configuration

| Constant | Value | Description |
| --- | --- | --- |
| `get_age_years` | - | GameConfig function reference |

## Entity Fields Accessed

| Field | Access | Description |
| --- | --- | --- |
| `age` | read | Age or stage lifecycle state. |
| `age_stage` | read | Age or stage lifecycle state. |
| `birth_tick` | read | birth tick |
| `entity_name` | read | entity name |
| `frailty` | read | frailty |
| `hunger` | read | Hunger/food state. |
| `id` | read | Entity identity reference. |

## Functions

### `_init()`

**Parameters**: `(none)`
**Lines**: 52-57 (6 lines)

### `init(entity_manager: RefCounted, rng: RandomNumberGenerator)`

**Parameters**: `entity_manager: RefCounted, rng: RandomNumberGenerator`
**Lines**: 58-63 (6 lines)

### `_load_siler_parameters()`

**Parameters**: `(none)`
**Lines**: 64-81 (18 lines)

### `execute_tick(tick: int)`

**Parameters**: `tick: int`
**Lines**: 82-91 (10 lines)

### `_check_birthday_mortality(tick: int)`

**Parameters**: `tick: int`
**Lines**: 92-109 (18 lines)

### `_check_infant_monthly(tick: int)`

**Parameters**: `tick: int`
**Lines**: 110-129 (20 lines)

### `_do_mortality_check(entity: RefCounted, tick: int, is_monthly: bool)`

**Parameters**: `entity: RefCounted, tick: int, is_monthly: bool`
**Lines**: 130-197 (68 lines)

### `_determine_cause(h_infant: float, h_background: float, h_senescence: float)`

**Parameters**: `h_infant: float, h_background: float, h_senescence: float`
**Lines**: 198-212 (15 lines)

### `_check_monthly_pop_log(tick: int)`

**Parameters**: `tick: int`
**Lines**: 213-229 (17 lines)

### `_print_monthly_pop_log(tick: int)`

**Parameters**: `tick: int`
**Lines**: 230-247 (18 lines)

### `_check_annual_demography_log(tick: int)`

**Parameters**: `tick: int`
**Lines**: 248-266 (19 lines)

### `_print_demography_log(year: int, tick: int)`

**Parameters**: `year: int, tick: int`
**Lines**: 267-309 (43 lines)

### `register_birth()`

Register a birth (called externally by FamilySystem)

**Parameters**: `(none)`
**Lines**: 310-315 (6 lines)

### `register_death(is_infant: bool = false, age_stage: String = "", age_years: float = -1.0, cause: String = "")`

Register a death (called externally by NeedsSystem, FamilySystem)

**Parameters**: `is_infant: bool = false, age_stage: String = "", age_years: float = -1.0, cause: String = ""`
**Lines**: 316-340 (25 lines)

### `_calc_theoretical_e0()`

**Parameters**: `(none)`
**Lines**: 341-344 (4 lines)

### `_calc_theoretical_ex(start_age: float)`

**Parameters**: `start_age: float`
**Lines**: 345-377 (33 lines)

### `_inject_bereavement_stress(deceased: RefCounted)`

Inject bereavement stress into survivors of a deceased entity. COR (Hobfoll 1989): loss events use is_loss=true -> x2.5 multiplier.

**Parameters**: `deceased: RefCounted`
**Lines**: 378-428 (51 lines)

## Formulas

### Doc Line 3

Siler(1979) bathtub-curve mortality model.

```gdscript
Siler(1979) bathtub-curve mortality model.
μ(x) = a₁·e^{-b₁·x} + a₂ + a₃·e^{b₃·x}
Birthday-based distributed checks (not every-tick iteration).
Infants (0-1yr) checked monthly for higher resolution.
```

📄 source: `scripts/systems/mortality_system.gd:L3`

### Siler Hazard Rate

Siler hazard components

```gdscript
Siler hazard components
```

📄 source: `scripts/systems/mortality_system.gd:L133`

### Do Mortality Check Line 134

Siler hazard components

$$_a1  \cdot  e^{-_b1  \cdot  age_years}$$

```gdscript
var mu_infant: float = _a1 * exp(-_b1 * age_years)
```

📄 source: `scripts/systems/mortality_system.gd:L134`

### Do Mortality Check Line 136

Formula logic extracted from _do_mortality_check

$$_a3  \cdot  e^{_b3  \cdot  age_years}$$

```gdscript
var mu_senescence: float = _a3 * exp(_b3 * age_years)
```

📄 source: `scripts/systems/mortality_system.gd:L136`

### Do Mortality Check Line 139

Tech modifiers

$$e^{-_tech_k1  \cdot  tech_level}$$

```gdscript
var m1: float = exp(-_tech_k1 * tech_level)
	var m2: float = exp(-_tech_k2 * tech_level)
	var m3: float = exp(-_tech_k3 * tech_level)
```

📄 source: `scripts/systems/mortality_system.gd:L139`

### Do Mortality Check Line 144

Nutrition modifier (based on hunger)

```gdscript
var nutrition: float = clampf(entity.hunger, 0.0, 1.0)
	m1 *= lerpf(2.0, 0.8, nutrition)
	m2 *= lerpf(1.5, 0.9, nutrition)
```

📄 source: `scripts/systems/mortality_system.gd:L144`

### Doc Line 168

Annual death probability: q = 1 - exp(-μ)

$$1 - e^{-μ}$$

```gdscript
Annual death probability: q = 1 - exp(-μ)
```

📄 source: `scripts/systems/mortality_system.gd:L168`

### Do Mortality Check Q Annual

Annual death probability: q = 1 - exp(-μ)

$$1.0 - e^{-mu_total}$$

```gdscript
var q_annual: float = 1.0 - exp(-mu_total)
	q_annual = clampf(q_annual, 0.0, 0.999)
```

📄 source: `scripts/systems/mortality_system.gd:L169`

### Doc Line 175

Monthly: q_month = 1 - (1 - q_annual)^(1/12)

$$1 - (1 - q_annual)^(1/12)$$

```gdscript
Monthly: q_month = 1 - (1 - q_annual)^(1/12)
```

📄 source: `scripts/systems/mortality_system.gd:L175`

### Do Mortality Check Q Check

Monthly: q_month = 1 - (1 - q_annual)^(1/12)

$$1.0 - pow(1.0 - q_annual, 1.0 / 12.0)$$

```gdscript
q_check = 1.0 - pow(1.0 - q_annual, 1.0 / 12.0)
```

📄 source: `scripts/systems/mortality_system.gd:L176`

### Determine Cause Line 202

Formula logic extracted from _determine_cause

$$_rng.randf()  \cdot  total$$

```gdscript
var roll: float = _rng.randf() * total
```

📄 source: `scripts/systems/mortality_system.gd:L202`

### Doc Line 282

Theoretical e0 from current Siler parameters

```gdscript
Theoretical e0 from current Siler parameters
```

📄 source: `scripts/systems/mortality_system.gd:L282`

### Doc Line 347

e(start) = integral from start to 120 of S(x)/S(start) dx

$$integral from start to 120 of S(x)/S(start) dx$$

```gdscript
e(start) = integral from start to 120 of S(x)/S(start) dx
```

📄 source: `scripts/systems/mortality_system.gd:L347`

### Calc Theoretical Ex Line 348

Numerical integration of survival function S(x) from start_age e(start) = integral from start to 120 of S(x)/S(start) dx

$$e^{-_tech_k1  \cdot  tech_level}$$

```gdscript
var m1: float = exp(-_tech_k1 * tech_level)
	var m2: float = exp(-_tech_k2 * tech_level)
	var m3: float = exp(-_tech_k3 * tech_level)
	var dx: float = 0.5  # half-year steps
```

📄 source: `scripts/systems/mortality_system.gd:L348`

### Calc Theoretical Ex Line 359

Hazard formula logic extracted from _calc_theoretical_ex

$$m1  \cdot  _a1  \cdot  e^{-_b1  \cdot  x} + m2  \cdot  _a2 + m3  \cdot  _a3  \cdot  e^{_b3  \cdot  x}$$

```gdscript
var mu: float = m1 * _a1 * exp(-_b1 * x) + m2 * _a2 + m3 * _a3 * exp(_b3 * x)
		cum_hazard_start += mu * dx
```

📄 source: `scripts/systems/mortality_system.gd:L359`

### Calc Theoretical Ex Line 367

Hazard formula logic extracted from _calc_theoretical_ex

$$m1  \cdot  _a1  \cdot  e^{-_b1  \cdot  x} + m2  \cdot  _a2 + m3  \cdot  _a3  \cdot  e^{_b3  \cdot  x}$$

```gdscript
var mu: float = m1 * _a1 * exp(-_b1 * x) + m2 * _a2 + m3 * _a3 * exp(_b3 * x)
		var s_rel: float = exp(-cum_hazard)  # S(x)/S(start)
		integral += s_rel * dx
		cum_hazard += mu * dx
```

📄 source: `scripts/systems/mortality_system.gd:L367`

### Doc Line 377

COR (Hobfoll 1989): loss events use is_loss=true -> x2.5 multiplier.

```gdscript
COR (Hobfoll 1989): loss events use is_loss=true -> x2.5 multiplier.
```

📄 source: `scripts/systems/mortality_system.gd:L377`

## Dependencies

### Imports

- [`game_calendar.gd`](../core/game_calendar.md) - via `preload` (line 8)

### Signals Emitted

- None

### Referenced By

- None
