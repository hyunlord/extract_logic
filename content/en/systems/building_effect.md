---
title: "Building Effect"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/building_effect_system.gd"
nav_order: 15
system_name: "building_effect"
---

# Building Effect

📄 source: `scripts/systems/building_effect_system.gd` | Priority: 15 | Tick interval: config (GameConfig.BUILDING_EFFECT_TICK_INTERVAL)

## Overview

The **Building Effect** system implements a domain-specific simulation model to simulate building effect dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.BUILDING_EFFECT_TICK_INTERVAL`) at priority **15**.

**Core entity data**: `energy` (read/write (inferred)), `social` (read/write (inferred))

## Tick Pipeline

1. Run per-entity tick update loop
   📄 source: `scripts/systems/building_effect_system.gd:L17`
2. Apply campfire
   📄 source: `scripts/systems/building_effect_system.gd:L30`
3. Apply shelter
   📄 source: `scripts/systems/building_effect_system.gd:L44`

## Formulas

No extracted formulas for this module.

## Config Reference

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `BUILDING_EFFECT_TICK_INTERVAL` | 10 | System update cadence. | Lower values increase update frequency and responsiveness. |
| `BUILDING_TYPES` | { 	"stockpile": {"cost": {"wood": 2.0}, "build_ticks": 36, "radius": 8}, 	"shelter": {"cost": {"wood": 4.0, "stone": 1.0}, "build_ticks": 60, "radius": 0}, 	"campfire": {"cost": {"wood": 1.0}, "build_ticks": 24, "radius": 5}, } | Building type definitions | Adjusts baseline system behavior under this module. |

## Cross-System Effects

### Imported Modules

No import relationships extracted

### Shared Entity Fields

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `energy` | read/write (inferred) | [`behavior`](behavior.md), [`emotions`](emotions.md), [`mental_break`](mental_break.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |
| `social` | read/write (inferred) | [`behavior`](behavior.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |

### Signals

No signal metadata extracted

### Downstream Impact

- No downstream dependencies extracted

## Entity Data Model

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `energy` | read/write (inferred) | float | Fatigue/rest capacity controlling action readiness. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
| `social` | read/write (inferred) | float | Social fulfillment/deficit level affecting mood and stress. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
