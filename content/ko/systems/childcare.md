---
title: "Childcare"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/childcare_system.gd"
nav_order: 8
system_name: "childcare"
---

# Childcare

📄 source: `scripts/systems/childcare_system.gd` | Priority: 8 | Tick interval: 2

## Overview (개요)

The **Childcare** system implements a domain-specific simulation model to simulate childcare dynamics for entities and world state.
It runs every **2 ticks** (0.0 game-years) at priority **8**.

**Core entity data**: `age_stage` (read/write (inferred)), `hunger` (read/write (inferred))

## Tick Pipeline (틱 파이프라인)

1. Run per-entity tick update loop
   📄 source: `scripts/systems/childcare_system.gd:L22`
2. Resolve settlement food
   📄 source: `scripts/systems/childcare_system.gd:L80`

## Formulas (수식)

No extracted formulas for this module.

## Configuration Reference (설정)

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `CHILDCARE_FEED_AMOUNTS` | { 	"infant": 0.40, 	"toddler": 0.50, 	"child": 0.50, 	"teen": 0.60, } | Feed amounts per childcare tick (food units from stockpile) | Adjusts baseline system behavior under this module. |
| `CHILDCARE_HUNGER_THRESHOLDS` | { 	"infant": 0.85, 	"toddler": 0.80, 	"child": 0.75, 	"teen": 0.70, } | Threshold gate for state transitions. | Changing this moves trigger points for behavior changes. |
| `FOOD_HUNGER_RESTORE` | 0.3 | Eating constants | Adjusts baseline system behavior under this module. |

## Cross-System Effects (시스템 간 상호작용)

### Imported Modules (모듈 임포트)

No import relationships extracted for this module.

### Shared Entity Fields (공유 엔티티 필드)

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `age_stage` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`construction`](construction.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md) |
| `hunger` | read/write (inferred) | [`behavior`](behavior.md), [`family`](family.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`stress`](stress.md) |

### Signals (시그널)

No emitted signals extracted for this module.

### Downstream Impact (다운스트림 영향)

- No explicit downstream dependencies extracted.

## Entity Data Model (엔티티 데이터 모델)

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `age_stage` | read/write (inferred) | String enum | Lifecycle progression used for stage-specific behavior and events. | Named categorical states. |
| `hunger` | read/write (inferred) | float | Nutritional deprivation level driving survival and action priorities. | Normalized scalar (commonly 0.0-1.0 or 0-100 by system). |
