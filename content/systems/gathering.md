---
title: "Gathering"
description: "Generated system documentation page."
generated: true
source_files:
  - "scripts/systems/gathering_system.gd"
nav_order: 25
system_name: "gathering"
---

# Gathering

📄 source: `scripts/systems/gathering_system.gd` | Priority: 25 | Tick interval: config (GameConfig.GATHERING_TICK_INTERVAL)

## Overview (개요)

The **Gathering** system implements a domain-specific simulation model to simulate gathering dynamics for entities and world state.
It runs on a **config-driven cadence** (`GameConfig.GATHERING_TICK_INTERVAL`) at priority **25**.

**Core entity data**: `add_item` (read/write (inferred)), `age_stage` (read/write (inferred)), `current_action` (read/write (inferred)), `entity_name` (read/write (inferred)), `get_total_carry` (read/write (inferred)), `id` (read/write (inferred)), `position` (read/write (inferred)), `speed` (read/write (inferred)), `total_gathered` (read/write (inferred))

## Tick Pipeline (틱 파이프라인)

1. Run per-entity tick update loop
   📄 source: `scripts/systems/gathering_system.gd:L15`

## Formulas (수식)

No extracted formulas for this module.

## Configuration Reference (설정)

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `CHILD_GATHER_EFFICIENCY` | { 	"child": 0.4, 	"teen": 0.8, 	"elder": 0.5, } | Gathering efficiency by age stage (1.0 = full adult rate) | Adjusts baseline system behavior under this module. |
| `GATHERING_TICK_INTERVAL` | 3 | System update cadence. | Lower values increase update frequency and responsiveness. |
| `GATHER_AMOUNT` | 2.0 | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `MAX_CARRY` | 10.0 | Hard bound for safe state range. | Constrains extremes to stabilize the simulation. |
| `ResourceType` | (not found) | Behavior tuning constant. | Adjusts baseline system behavior under this module. |

## Cross-System Effects (시스템 간 상호작용)

### Imported Modules (모듈 임포트)

No import relationships extracted for this module.

### Shared Entity Fields (공유 엔티티 필드)

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `age_stage` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`childcare`](childcare.md), [`construction`](construction.md), [`family`](family.md), [`job_assignment`](job_assignment.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md) |
| `current_action` | read/write (inferred) | [`behavior`](behavior.md), [`construction`](construction.md), [`emotions`](emotions.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`movement`](movement.md), [`needs`](needs.md), [`social_events`](social_events.md), [`stress`](stress.md) |
| `entity_name` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`chronicle`](chronicle.md), [`emotions`](emotions.md), [`family`](family.md), [`job_assignment`](job_assignment.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`stress`](stress.md) |
| `get_total_carry` | read/write (inferred) | [`behavior`](behavior.md) |
| `id` | read/write (inferred) | [`behavior`](behavior.md), [`aging`](aging.md), [`emotions`](emotions.md), [`family`](family.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`social_events`](social_events.md) |
| `position` | read/write (inferred) | [`behavior`](behavior.md), [`construction`](construction.md), [`movement`](movement.md), [`social_events`](social_events.md) |

### Signals (시그널)

No emitted signals extracted for this module.

### Downstream Impact (다운스트림 영향)

- No explicit downstream dependencies extracted.

## Entity Data Model (엔티티 데이터 모델)

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `add_item` | read/write (inferred) | Variant | Add item. | System-defined value domain. |
| `age_stage` | read/write (inferred) | String enum | Lifecycle progression used for stage-specific behavior and events. | Named categorical states. |
| `current_action` | read/write (inferred) | String enum | Current behavior intent used by schedulers and downstream systems. | System-defined value domain. |
| `entity_name` | read/write (inferred) | Variant | Entity name. | System-defined value domain. |
| `get_total_carry` | read/write (inferred) | Variant | Get total carry. | System-defined value domain. |
| `id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `position` | read/write (inferred) | Vector2 / Vector2i | World-space location used for movement and proximity checks. | Grid/world vectors. |
| `speed` | read/write (inferred) | Variant | Speed. | System-defined value domain. |
| `total_gathered` | read/write (inferred) | Variant | Total gathered. | System-defined value domain. |
