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

## Overview (개요)

The **Resource Regen** system implements a domain-specific simulation model to simulate resource regen dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.RESOURCE_REGEN_TICK_INTERVAL`) at priority **5**.

**Core entity data**: No entity fields were extracted.

## Tick Pipeline (틱 파이프라인)

1. Run per-entity tick update loop
   📄 source: `scripts/systems/resource_regen_system.gd:L15`

## Formulas (수식)

No extracted formulas for this module.

## Configuration Reference (설정)

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `FOOD_REGEN_RATE` | 1.0 | Rate coefficient for change per tick. | Directly scales accumulation/decay velocity each tick. |
| `RESOURCE_REGEN_TICK_INTERVAL` | 120 | System update cadence. | Lower values increase update frequency and responsiveness. |
| `ResourceType` | (not found) | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `WOOD_REGEN_RATE` | 0.3 | Rate coefficient for change per tick. | Directly scales accumulation/decay velocity each tick. |

## Cross-System Effects (시스템 간 상호작용)

### Imported Modules (모듈 임포트)

No import relationships extracted for this module.

### Shared Entity Fields (공유 엔티티 필드)

No cross-system shared entity field usage was inferred.

### Signals (시그널)

No emitted signals extracted for this module.

### Downstream Impact (다운스트림 영향)

- No explicit downstream dependencies extracted.

## Entity Data Model (엔티티 데이터 모델)

No entity field metadata extracted for this module.
