---
title: "Resource Regen"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/resource_regen_system.gd"
nav_order: 5
system_name: "resource_regen"
---

# Resource Regen

📄 source: `scripts/systems/resource_regen_system.gd` | Priority: 5 | Tick interval: config (GameConfig.RESOURCE_REGEN_TICK_INTERVAL)

## Overview

The **Resource Regen** system implements a domain-specific simulation model to simulate resource regen dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.RESOURCE_REGEN_TICK_INTERVAL`) at priority **5**.

**Core entity data**: No entity fields were extracted.

## Tick Pipeline

1. Run per-entity tick update loop
   📄 source: `scripts/systems/resource_regen_system.gd:L15`

## Formulas

No extracted formulas for this module.

## Config Reference

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `FOOD_REGEN_RATE` | 1.0 | Rate coefficient for change per tick. | Directly scales accumulation/decay velocity each tick. |
| `RESOURCE_REGEN_TICK_INTERVAL` | 120 | System update cadence. | Lower values increase update frequency and responsiveness. |
| `ResourceType` | (not found) | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `WOOD_REGEN_RATE` | 0.3 | Rate coefficient for change per tick. | Directly scales accumulation/decay velocity each tick. |

## Cross-System Effects

### Imported Modules

No import relationships extracted

### Shared Entity Fields

No shared fields inferred

### Signals

No signal metadata extracted

### Downstream Impact

- No downstream dependencies extracted

## Entity Data Model

No entity field metadata extracted for this module.
