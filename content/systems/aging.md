---
title: "Aging"
description: "Checks age stage transitions, emits growth notifications, and applies yearly personality maturation."
generated: true
source_files:
  - "scripts/systems/age_system.gd"
nav_order: 48
system_name: "aging"
---

# Aging

📄 source: `scripts/systems/age_system.gd` | Priority: 48 | Tick interval: 50

## Overview (개요)

The **Aging** system implements a domain-specific simulation model to simulate checks age stage transitions, emits growth notifications, and applies yearly personality maturation.
It runs every **50 ticks** (0.0 game-years) at priority **48**.

**Core entity data**: `age` (read/write (inferred)), `age_stage` (read/write (inferred)), `entity_name` (read/write (inferred)), `id` (read/write (inferred)), `job` (read/write (inferred)), `personality` (read/write (inferred))

> Checks age stage transitions, emits growth notifications, and applies yearly personality maturation.

## Tick Pipeline (틱 파이프라인)

1. Run per-entity tick update loop
   📄 source: `scripts/systems/age_system.gd:L26`
2. Emit system signals: `ui_notification`
   📄 source: `scripts/systems/age_system.gd:L54`

## Formulas (수식)

No extracted formulas for this module.

## Configuration Reference (설정)

| Constant | Default | Controls | Behavior Effect |
| :-- | :-- | :-- | :-- |
| `TICKS_PER_YEAR` | 4380 | Simulation-time conversion or cadence. | Adjusts baseline system behavior under this module. |
| `get_age_stage` | (not found) | Behavior tuning constant. | Adjusts baseline system behavior under this module. |
| `get_age_years` | (not found) | Behavior tuning constant. | Adjusts baseline system behavior under this module. |

## Cross-System Effects (시스템 간 상호작용)

### Imported Modules (모듈 임포트)

- [`personality_maturation`](personality_maturation.md) via `preload` at `scripts/systems/age_system.gd:L7`

### Shared Entity Fields (공유 엔티티 필드)

| Field | Access | Shared With |
| :-- | :-- | :-- |
| `age` | read/write (inferred) | [`family`](family.md), [`mortality`](mortality.md), [`needs`](needs.md) |
| `age_stage` | read/write (inferred) | [`behavior`](behavior.md), [`childcare`](childcare.md), [`construction`](construction.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md) |
| `entity_name` | read/write (inferred) | [`behavior`](behavior.md), [`chronicle`](chronicle.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`mental_break`](mental_break.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`stress`](stress.md), [`trauma_scar`](trauma_scar.md) |
| `id` | read/write (inferred) | [`behavior`](behavior.md), [`emotions`](emotions.md), [`family`](family.md), [`gathering`](gathering.md), [`job_assignment`](job_assignment.md), [`migration`](migration.md), [`mortality`](mortality.md), [`movement`](movement.md), [`needs`](needs.md), [`population`](population.md), [`social_events`](social_events.md), [`trauma_scar`](trauma_scar.md) |
| `job` | read/write (inferred) | [`behavior`](behavior.md), [`job_assignment`](job_assignment.md) |
| `personality` | read/write (inferred) | [`emotions`](emotions.md), [`mental_break`](mental_break.md), [`stress`](stress.md), [`trait`](trait.md) |

### Signals (시그널)

| Signal | Parameters | Subscribers | Source Line |
| :-- | :-- | :-- | :-- |
| `ui_notification` | message: String, type: String | No known subscribers | L54 |
| `ui_notification` | message: String, type: String | No known subscribers | L57 |
| `ui_notification` | message: String, type: String | No known subscribers | L60 |

### Downstream Impact (다운스트림 영향)

- No explicit downstream dependencies extracted.

## Entity Data Model (엔티티 데이터 모델)

| Field | Access | Type | Represents | Typical Values |
| :-- | :-- | :-- | :-- | :-- |
| `age` | read/write (inferred) | int | Lifecycle progression used for stage-specific behavior and events. | Non-negative tick counts. |
| `age_stage` | read/write (inferred) | String enum | Lifecycle progression used for stage-specific behavior and events. | Named categorical states. |
| `entity_name` | read/write (inferred) | Variant | Entity name. | System-defined value domain. |
| `id` | read/write (inferred) | int | Stable entity identity used for referencing across systems. | Positive integer identifiers. |
| `job` | read/write (inferred) | Variant | Job. | System-defined value domain. |
| `personality` | read/write (inferred) | Dictionary / custom data object | Trait/axis profile used for sensitivity and decision weighting. | Structured object with nested metrics/axes. |
