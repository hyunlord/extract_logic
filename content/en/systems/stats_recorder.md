---
title: "Stats Recorder"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/stats_recorder.gd"
nav_order: 90
system_name: "stats_recorder"
---

# Stats Recorder

📄 source: `scripts/systems/stats_recorder.gd` | Priority: 90 | Tick interval: 200

## Overview

The **Stats Recorder** system implements a domain-specific simulation model to simulate stats recorder dynamics for entities and world state.
It runs every **200 ticks** (0.0 game-years) at priority **90**.

**Core entity data**: No entity fields were extracted.

## Tick Pipeline

1. Run per-entity tick update loop
   📄 source: `scripts/systems/stats_recorder.gd:L25`
2. Resolve resource deltas
   📄 source: `scripts/systems/stats_recorder.gd:L73`
3. Resolve settlement stats
   📄 source: `scripts/systems/stats_recorder.gd:L90`

## Formulas

No extracted formulas for this module.

## Config Reference

No GameConfig references extracted

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
